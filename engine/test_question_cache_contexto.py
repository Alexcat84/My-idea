# -*- coding: utf-8 -*-
"""engine/build_question_cache.py: el generador ve la SITUACION del nodo actual, no solo su titulo y su resumen
(integracion del mundo 11, 28 sep 2026: la verificacion a ciegas de las preguntas de las puertas dio por flojas las
que no partian de la situacion del nodo, y el generador nunca la veia).

Caso a mano, con un cliente falso que guarda lo que se le manda (sin API ni clave):
  actual = {titulo_concepto "T", resumen_teorico 500 x "r", condiciones_activacion ["C1", "C2"], entregable_esperado "E"}
  candidato "b" = {titulo_concepto "B", condiciones_activacion ["cb1", "cb2", "cb3", "cb4"]}
    concepto_actual     = {"titulo": "T", "resumen": 400 x "r", "condicion": "C1", "entregable": "E"}
    conceptos_siguientes = [{"titulo": "B", "condiciones_activacion": ["cb1", "cb2", "cb3"]}]
  un actual sin condiciones ni entregable -> "condicion": "" y "entregable": "" (no rompe)
  la pregunta devuelta es la del JSON del modelo: "¿Q?"

    python engine/test_question_cache_contexto.py
"""
import json
import os
import sys
from types import SimpleNamespace

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(RAIZ, "engine"))

import build_question_cache as bqc  # noqa: E402


class ClienteFalso:
    def __init__(self):
        self.enviado = []
        self.messages = self

    def create(self, **kw):
        self.enviado.append(json.loads(kw["messages"][0]["content"]))
        return SimpleNamespace(content=[SimpleNamespace(type="text", text='{"pregunta": "¿Q?"}')], usage=None)


def main():
    fallos = []
    grafo = {"b": {"titulo_concepto": "B", "condiciones_activacion": ["cb1", "cb2", "cb3", "cb4"]}}
    actual = {"titulo_concepto": "T", "resumen_teorico": "r" * 500, "condiciones_activacion": ["C1", "C2"],
              "entregable_esperado": "E"}
    cli = ClienteFalso()
    pregunta, _ = bqc.generar_pregunta(cli, actual, ["b"], grafo)
    ctx = cli.enviado[0]
    esperado = {"titulo": "T", "resumen": "r" * 400, "condicion": "C1", "entregable": "E"}
    if ctx["concepto_actual"] != esperado:
        fallos.append("concepto_actual: %r" % {k: (v[:20] if isinstance(v, str) else v) for k, v in ctx["concepto_actual"].items()})
    if ctx["conceptos_siguientes"] != [{"titulo": "B", "condiciones_activacion": ["cb1", "cb2", "cb3"]}]:
        fallos.append("conceptos_siguientes: %r" % ctx["conceptos_siguientes"])
    if pregunta != "¿Q?":
        fallos.append("pregunta: %r" % pregunta)
    bqc.generar_pregunta(cli, {"titulo_concepto": "T", "resumen_teorico": "r"}, ["b"], grafo)
    c2 = cli.enviado[1]["concepto_actual"]
    if c2.get("condicion") != "" or c2.get("entregable") != "":
        fallos.append("sin condiciones ni entregable: %r" % c2)
    if fallos:
        print("ROJO: %d fallos" % len(fallos), *fallos, sep="\n  ")
        sys.exit(1)
    print("VERDE: el generador de preguntas ve la condicion y el entregable del nodo actual")


if __name__ == "__main__":
    main()
