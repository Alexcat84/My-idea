# -*- coding: utf-8 -*-
"""LA VACUNA DEL \\b: todo patron de detector nace con dos fixtures.

TRES VECES EN UN CICLO (ago 2026) un `\\b` escrito dentro de un heredoc llego al
archivo como el caracter BACKSPACE (0x08). Y las tres veces el patron resultante
NO FALLO: se callo. Un `re.sub` que no encuentra nada devuelve el texto igual, y
un detector que no caza nada informa cero hallazgos, que se lee como "esta todo
limpio".

    "Una clave mal escrita no falla, se silencia."

Es la misma familia que la clave `prohibido` que nadie leia y que el fixture del
juez que tomaba la primera clave del grafo: VERDE POR CASUALIDAD. La cura general
es esta: un patron sin fixtures no entra, y un patron que no distingue entre lo
que debe cazar y lo que no, deja la suite en rojo.

Cada patron declara:
  - `caza`:    textos que DEBE marcar. Si no los marca, el patron esta muerto.
  - `no_caza`: textos que NO debe marcar. Si los marca, el patron esta roto por
               el otro lado, que es la averia de la guardia de acentos (39 de 40
               nodos buenos rechazados) y la de `tu equipo`.
"""
import json
import re
import sys
import unicodedata
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE / "scripts"))

from censo_duplicacion import BARANDAS  # noqa: E402
from revoz_pack import VETADO  # noqa: E402

REGISTRO = BASE / "dataset" / "metadata" / "fixtures_de_patrones.json"


def _todos():
    """(familia, grupo, patron) de todos los detectores de la casa."""
    for fam, d in (("BARANDAS", BARANDAS), ("VETADO", VETADO)):
        for grupo, patrones in d.items():
            for p in patrones:
                yield fam, grupo, p


def test_ningun_patron_lleva_caracteres_de_control():
    """LA VACUNA DIRECTA. `\\b` en un heredoc se convierte en 0x08 y el patron
    deja de cazar sin decir nada. Esto lo hace imposible de pasar."""
    malos = []
    for fam, grupo, p in _todos():
        for c in p:
            if unicodedata.category(c) == "Cc":
                malos.append((fam, grupo, repr(p), hex(ord(c))))
                break
    assert not malos, (
        "PATRONES CON CARACTER DE CONTROL (casi seguro un \\b comido por un heredoc): "
        f"{malos}")
    print(f"  ok: los {sum(1 for _ in _todos())} patrones estan limpios de caracteres de control")


def test_todo_patron_tiene_sus_dos_fixtures():
    reg = json.loads(REGISTRO.read_text(encoding="utf-8"))["fixtures"]
    faltan = [(f, g, p) for f, g, p in _todos() if p not in reg]
    assert not faltan, (
        "Patrones sin fixtures. Un patron nuevo entra CON sus dos ejemplos o no entra: "
        f"{faltan}")
    for p, d in reg.items():
        assert d.get("caza"), f"{p}: sin ejemplos que deba cazar"
        assert d.get("no_caza"), f"{p}: sin ejemplos que NO deba cazar"
    print(f"  ok: los {len(reg)} patrones traen su ejemplo positivo y su negativo")


def test_cada_patron_caza_lo_que_debe():
    reg = json.loads(REGISTRO.read_text(encoding="utf-8"))["fixtures"]
    muertos = []
    for p, d in reg.items():
        for t in d["caza"]:
            if not re.search(p, t, re.I):
                muertos.append((p, t))
    assert not muertos, (
        "PATRONES MUERTOS: no cazan lo que existen para cazar. Si un `\\b` se convirtio "
        f"en backspace, aqui es donde se ve: {muertos}")
    print("  ok: todos cazan sus positivos")


def test_ningun_patron_caza_lo_correcto():
    """La otra mitad, y la que mas ha costado en este proyecto: la guardia de
    acentos rechazo 39 nodos buenos de 40, y `tu equipo` marco trece nodos ya
    re-vozados. Una baranda que caza lo correcto no es estricta, esta rota."""
    reg = json.loads(REGISTRO.read_text(encoding="utf-8"))["fixtures"]
    falsos = []
    for p, d in reg.items():
        for t in d["no_caza"]:
            m = re.search(p, t, re.I)
            if m:
                falsos.append((p, t, m.group(0)))
    assert not falsos, f"PATRONES QUE CAZAN LO CORRECTO: {falsos}"
    print("  ok: ninguno caza sus negativos")


def test_el_registro_no_tiene_fixtures_huerfanos():
    """Un fixture de un patron que ya no existe es ruido que envejece: parece
    cobertura y no cubre nada."""
    reg = json.loads(REGISTRO.read_text(encoding="utf-8"))["fixtures"]
    vivos = {p for _, _, p in _todos()}
    huerfanos = [p for p in reg if p not in vivos]
    assert not huerfanos, f"fixtures de patrones que ya no existen: {huerfanos}"
    print("  ok: el registro no arrastra fixtures de patrones muertos")


def main():
    for f in (test_ningun_patron_lleva_caracteres_de_control,
              test_todo_patron_tiene_sus_dos_fixtures,
              test_cada_patron_caza_lo_que_debe,
              test_ningun_patron_caza_lo_correcto,
              test_el_registro_no_tiene_fixtures_huerfanos):
        f()
    print("OK: un patron mal escrito ya no se puede callar.")


if __name__ == "__main__":
    main()
