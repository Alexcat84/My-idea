# -*- coding: utf-8 -*-
"""El censo de duplicacion es de SOLO LECTURA, y esto lo custodia.

El encargo fue explicito: cero cambios a dataset, packs, grafo o produccion.
Un censo que mide 3.835 nodos y ademas puede escribirlos es un censo que un
dia, por una linea de mas, deja de ser un censo. La promesa esta en su
docstring; esto la vuelve comprobable.

Lo unico que el censo puede escribir son sus propios entregables en docs/.
"""
import ast
import sys
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent
CENSO = BASE / "scripts" / "censo_duplicacion.py"

# Lo unico que tiene permiso de escribir: sus entregables.
SALIDAS_PERMITIDAS = ("docs",)


def _llamadas(arbol):
    for nodo in ast.walk(arbol):
        if isinstance(nodo, ast.Call):
            yield nodo


def _nombre(func):
    if isinstance(func, ast.Name):
        return func.id
    if isinstance(func, ast.Attribute):
        return func.attr
    return ""


def test_no_abre_nada_en_modo_escritura():
    arbol = ast.parse(CENSO.read_text(encoding="utf-8"))
    for c in _llamadas(arbol):
        if _nombre(c.func) != "open":
            continue
        modo = ""
        for i, a in enumerate(c.args):
            if i == 1 and isinstance(a, ast.Constant):
                modo = str(a.value)
        for kw in c.keywords:
            if kw.arg == "mode" and isinstance(kw.value, ast.Constant):
                modo = str(kw.value.value)
        assert not any(x in modo for x in "wax+"), (
            f"open() en modo '{modo}' en la linea {c.lineno}: el censo escribiria")
    print("  ok: ningun open() en modo escritura")


def test_solo_escribe_sus_entregables():
    """Los write_text del censo apuntan a docs/, jamas a dataset ni packs."""
    fuente = CENSO.read_text(encoding="utf-8")
    arbol = ast.parse(fuente)
    lineas = fuente.split("\n")
    escrituras = [c.lineno for c in _llamadas(arbol)
                  if _nombre(c.func) in ("write_text", "dump", "to_csv", "savez", "save")]
    assert escrituras, "no hay ninguna escritura: el censo no entregaria nada"
    for ln in escrituras:
        # La ruta se arma en la misma linea o justo encima (salida = BASE / ...).
        contexto = "\n".join(lineas[max(0, ln - 4):ln])
        assert any(f'"{d}"' in contexto or f"/ {d}" in contexto for d in SALIDAS_PERMITIDAS), (
            f"escritura en la linea {ln} sin destino en docs/: {contexto.strip()[:90]}")
    print(f"  ok: las {len(escrituras)} escrituras van a docs/")


def test_no_nombra_las_carpetas_intocables_para_escribir():
    """dataset/ y packs/ solo pueden aparecer en rutas de LECTURA."""
    fuente = CENSO.read_text(encoding="utf-8")
    for linea in fuente.split("\n"):
        if ('"dataset"' in linea or '"packs"' in linea) and any(
                x in linea for x in ("write_text", "unlink", "rmtree", "mkdir", 'open(')):
            # open() ya se valido por modo arriba; aqui se caza el resto.
            assert 'open(' in linea, f"operacion de escritura sobre intocables: {linea.strip()}"
    print("  ok: dataset/ y packs/ solo aparecen en rutas de lectura")


def test_el_umbral_es_uno_solo():
    """Un umbral distinto por pack invalidaria la comparacion entera."""
    sys.path.insert(0, str(BASE / "scripts"))
    from censo_duplicacion import ERAS, UMBRAL
    assert 0.5 < UMBRAL < 1.0, UMBRAL
    fuente = CENSO.read_text(encoding="utf-8")
    # No puede haber un mapa de umbrales por pack escondido.
    assert "UMBRALES" not in fuente, "hay umbrales en plural: la comparacion no seria justa"
    assert len(ERAS) == 10, f"se miden {len(ERAS)} packs, deberian ser 10"
    print(f"  ok: un solo umbral ({UMBRAL}) para los {len(ERAS)} packs")


def main():
    for f in (test_no_abre_nada_en_modo_escritura,
              test_solo_escribe_sus_entregables,
              test_no_nombra_las_carpetas_intocables_para_escribir,
              test_el_umbral_es_uno_solo):
        f()
    print("OK: el censo mide y no toca.")


if __name__ == "__main__":
    main()
