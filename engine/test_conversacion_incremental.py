# -*- coding: utf-8 -*-
"""Verifica la mecanica de llamar_claude_conversacion en aislamiento (sin
API real): el marcador cache_control debe vivir SOLO en el ultimo bloque
enviado en cada llamada (se quita del turno anterior, se pone en el nuevo),
el historial solo se compromete (append) si la llamada tuvo exito, y una
excepcion a mitad de llamada deja historial_mensajes exactamente como
estaba (nunca un turno de usuario huerfano sin su respuesta)."""
import os
import sys
import types

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))


class _FakeUsage:
    def __init__(self, in_tok=100, out_tok=20, cache_read=0, cache_write=0):
        self.input_tokens = in_tok
        self.output_tokens = out_tok
        self.cache_read_input_tokens = cache_read
        self.cache_creation_input_tokens = cache_write


class _FakeBlock:
    type = "text"
    def __init__(self, text):
        self.text = text


class _FakeMsg:
    def __init__(self, text, **usage_kwargs):
        self.content = [_FakeBlock(text)]
        self.usage = _FakeUsage(**usage_kwargs)


class _FakeMessages:
    def __init__(self, respuestas):
        self._respuestas = list(respuestas)
        self.llamadas = []

    def create(self, **kwargs):
        self.llamadas.append(kwargs)
        item = self._respuestas.pop(0)
        if isinstance(item, Exception):
            raise item
        return item


class _FakeClient:
    def __init__(self, respuestas):
        self.messages = _FakeMessages(respuestas)


def _instalar_anthropic_falso(respuestas):
    fake_client = _FakeClient(respuestas)
    fake_module = types.SimpleNamespace(Anthropic=lambda: fake_client)
    sys.modules["anthropic"] = fake_module
    return fake_client


import prototipo_motor as pm  # noqa: E402  (despues de preparar sys.path)

# --- Caso 1: dos llamadas exitosas seguidas -> el historial crece de a 2,
# y el cache_control se mueve del bloque viejo al nuevo cada vez.
fake = _instalar_anthropic_falso([
    _FakeMsg('{"ok": 1}', cache_write=500),
    _FakeMsg('{"ok": 2}', cache_read=500),
])
historial = []
r1 = pm.llamar_claude_conversacion("system-x", historial, "turno 1", "modelo-fake", componente="turnos")
assert r1 == '{"ok": 1}'
assert len(historial) == 2, f"esperaba 2 mensajes tras la 1a llamada, hay {len(historial)}"
assert historial[0]["role"] == "user" and historial[1]["role"] == "assistant"
assert historial[0]["content"][-1]["cache_control"] == {"type": "ephemeral"}, "el turno 1 debe quedar marcado tras la 1a llamada"

r2 = pm.llamar_claude_conversacion("system-x", historial, "turno 2", "modelo-fake", componente="turnos")
assert r2 == '{"ok": 2}'
assert len(historial) == 4, f"esperaba 4 mensajes tras la 2a llamada, hay {len(historial)}"
# el marcador del turno 1 (bloque en historial[0]) debe haberse quitado...
assert "cache_control" not in historial[0]["content"][-1], "el marcador viejo debia quitarse antes de la 2a llamada"
# ...y el marcador vive ahora solo en el turno 2 (el nuevo ultimo bloque de usuario)
assert historial[2]["content"][-1]["cache_control"] == {"type": "ephemeral"}, "el turno 2 debe quedar marcado"

# La 2a llamada a la API debio incluir los 2 mensajes previos (turno1 user+assistant) + el nuevo turno2 user = 3 mensajes en total en el request
segundo_request = fake.messages.llamadas[1]
assert len(segundo_request["messages"]) == 3, f"la 2a llamada debio enviar 3 mensajes (historial + turno nuevo), envio {len(segundo_request['messages'])}"

print("Caso 1 OK: historial crece de a 2, cache_control se mueve correctamente turno a turno.")

# --- Caso 2: la llamada 3 falla (excepcion de red) -> historial_mensajes
# NO debe mutarse (sigue en 4 elementos, forma valida, sin turno huerfano).
fake2 = _instalar_anthropic_falso([RuntimeError("fallo de red simulado")])
historial_antes = list(historial)  # copia superficial para comparar longitud/orden
try:
    pm.llamar_claude_conversacion("system-x", historial, "turno 3", "modelo-fake", componente="turnos")
    assert False, "se esperaba que la llamada fallida propagara la excepcion"
except RuntimeError:
    pass

assert len(historial) == 4, f"tras un fallo, el historial NO debia crecer; tiene {len(historial)} elementos"
assert historial == historial_antes, "el historial no debe haber cambiado de contenido tras el fallo"

print("Caso 2 OK: una llamada fallida deja historial_mensajes intacto (sin turno de usuario huerfano).")
print("\nTODO OK: mecanica de caching incremental de conversacion verificada sin llamadas reales a la API.")
