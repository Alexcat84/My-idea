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


def test_las_barandas_conocen_el_trabajo_ya_hecho():
    """LA DOCTRINA HERMANA DE LA DE LOS ACENTOS (adjudicada ago 2026):

        "Los detectores deben conocer el trabajo ya hecho, o acaban
         cobrandolo dos veces."

    `tu equipo` estaba en el patron de residuo_corporativo. Era correcto en la
    era de la EXTRACCION. Pero la re-voz lo escribio A PROPOSITO: es la voz de
    la casa para quien tiene dos o tres personas trabajando con el. Trece nodos
    ya re-vozados caian ahi, y OCHO los habia re-vozado esta misma casa.

    No era gratis: re-vozar trece nodos buenos cuesta dinero y arriesga
    DEGRADARLOS, porque el modelo tiene que cambiar algo para justificar su
    turno."""
    sys.path.insert(0, str(BASE / "scripts"))
    import censo_duplicacion as c
    corp = " ".join(c.BARANDAS["residuo_corporativo"])
    assert "tu equipo" not in corp, "la baranda volvio a cazar la voz de la casa"
    # pero la tercera persona SI se queda: esa delata un nodo que le habla a
    # una empresa que no es la del lector.
    for marcador in ("su equipo", "el equipo de", "la gerencia", "el comit"):
        assert marcador in corp, f"se perdio el marcador de tercera persona: {marcador}"

    ya_revozado = {"titulo_concepto": "Autoinspeccion",
                   "resumen_teorico": "Tu y las personas con mas experiencia de tu equipo revisan.",
                   "pasos_accionables": ["Inspecciona junto a tu equipo"],
                   "condiciones_activacion": [], "entregable_esperado": ""}
    assert c.revisar_barandas(ya_revozado) == [], "un nodo ya re-vozado sigue marcado"

    corporativo = dict(ya_revozado, resumen_teorico="La gerencia reune a su equipo y al comite.")
    assert c.revisar_barandas(corporativo), "dejo de cazar la tercera persona de verdad"
    print("  ok: la baranda ya no cobra dos veces el trabajo hecho, y sigue cazando lo corporativo")


def test_la_exencion_de_localizacion():
    """MISMO PRINCIPIO, otra baranda. `adaptaciones_sectoriales_iso` decia:
    "las cGMP que exige la FDA en Estados Unidos, O EL ORGANISMO EQUIVALENTE EN
    TU MERCADO". El nodo YA trae el reencuadre hecho y la baranda saltaba por la
    sigla suelta: detectar por lo que el nodo MENCIONA en vez de por lo que
    DESCRIBE, que es la ley que el auditor ya adjudico.

    Y el limite del perdon: la exencion vale para ESA mencion, no para el nodo
    entero. Un nodo que localiza una sigla al principio no queda absuelto de
    cablear otra al final."""
    sys.path.insert(0, str(BASE / "scripts"))
    import censo_duplicacion as c

    localizado = {"titulo_concepto": "Normas sectoriales",
                  "resumen_teorico": "Las cGMP que exige la FDA en Estados Unidos, o el "
                                     "organismo equivalente en tu mercado, piden trazabilidad.",
                  "pasos_accionables": [], "condiciones_activacion": [], "entregable_esperado": ""}
    assert c.revisar_barandas(localizado) == [], "marca un nodo que ya esta localizado"

    cableado = dict(localizado, resumen_teorico="Registra tus incidentes ante la OSHA cada anio.")
    assert c.revisar_barandas(cableado), "dejo de cazar la sigla cableada de verdad"

    # el limite: una localizada y otra suelta LEJOS -> se marca igual
    mixto = dict(localizado, resumen_teorico=(
        "Las cGMP que exige la FDA en Estados Unidos, o el organismo equivalente en tu "
        "mercado, piden trazabilidad. " + ("Ademas conviene documentar cada lote y guardar "
        "las evidencias de cada control durante el tiempo que corresponda. " * 4) +
        "Presenta el formulario ante la IRS."))
    assert c.revisar_barandas(mixto), (
        "la exencion absolvio al nodo entero: una sigla localizada no perdona a las demas")

    # y el nodo real que origino la regla
    import json as _json, io as _io
    real = _json.load(_io.open(BASE / "dataset" / "nodos" / "adaptaciones_sectoriales_iso.json",
                               encoding="utf-8"))
    assert c.revisar_barandas(real) == [], "el nodo que origino la exencion sigue marcado"
    print("  ok: la exencion perdona la mencion localizada, no el nodo entero")


def main():
    for f in (test_no_abre_nada_en_modo_escritura,
              test_solo_escribe_sus_entregables,
              test_no_nombra_las_carpetas_intocables_para_escribir,
              test_el_umbral_es_uno_solo,
              test_las_barandas_conocen_el_trabajo_ya_hecho,
              test_la_exencion_de_localizacion):
        f()
    print("OK: el censo mide y no toca.")


if __name__ == "__main__":
    main()
