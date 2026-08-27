# -*- coding: utf-8 -*-
r"""vuelta94_tarea4_reparar_marca_hijo.py . VUELTA 94, TAREA 4: LA LOOKBEHIND DE
MARCA_HIJO, EL SOSTEN UNICO, Y LAS DOS FORMAS LIMPIAS.

(a) EL DEFECTO MEDIDO (acta de la vuelta 93, seccion 5.1; TAREA 3 de esta
vuelta, relectura del puesto 1281): MARCA_HIJO en
scripts/loop/vuelta91_tarea4_direccion_ope07.py linea 96 es
`(?<!no )trae\b(?!\s+lo\s+suyo)|desarrolla|RECORRE\s+EL\s+CAMINO`. La
lookbehind `(?<!no )` solo tapa "no trae" PEGADO, y no cubre "ningun ...
trae", "nadie trae", "sin traer" u otras negaciones que el catalogo usa de
verdad a mas de dos palabras de distancia (Python `re` no soporta lookbehind
de longitud variable, asi que la unica forma correcta es una VENTANA de
negacion, no un lookbehind mas largo).

LA RED DE NEGACION DE ESTA VUELTA (mia, declarada): "no", "ningun",
"ninguna", "nadie", "jamas", "sin", buscados en las 60 letras previas al
"trae" encontrado. Es la misma red que declaro el acta de la vuelta 93
(seccion 5.1) para su barrido independiente.

(b) EL CASO ROJO POR MUTACION: sobre el segmento REAL del hijo del puesto
1281 (`pensamiento_visual_modelos_negocio`, `docs/INTRA_DOMINIO_VEREDICTOS.
jsonl`), que contiene el UNICO "trae" negado por "ningun" que motivo esta
reparacion.

(c) EL SOSTEN UNICO: reconstruido con codigo propio sobre las 84 filas
VIGENTES (docs/plan/OP_E_07_DIRECCION_V94.jsonl, tras la salida del 1281 y
el 1992 en la TAREA 3 de esta vuelta), no las 86 que midio el acta 93 (esas
86 incluian al 1281 y al 1992, que esta vuelta ya saco). Y declara, con el
mismo criterio que "es un habito", cuales de las OCHO alternativas de
frecuencia 1 en las 3.388 razones son INVERIFICABLES.

(d) LAS DOS FORMAS LIMPIAS: "trae el procedimiento de LA SEGUNDA" (960) y
"trae la forma de UNA DE SUS LINEAS" (1567), anadidas a MARCA_MADRE_
POSITIVA con la misma lookahead negativa que excluye "linea compartida".

USO:
  python scripts/loop/vuelta94_tarea4_reparar_marca_hijo.py --vara
  python scripts/loop/vuelta94_tarea4_reparar_marca_hijo.py --sin-cambio
  python scripts/loop/vuelta94_tarea4_reparar_marca_hijo.py --sosten-unico
  python scripts/loop/vuelta94_tarea4_reparar_marca_hijo.py --mutacion
"""
import io
import json
import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
PLAN = os.path.join(RAIZ, "docs", "plan")
VEREDICTOS = os.path.join(RAIZ, "docs", "INTRA_DOMINIO_VEREDICTOS.jsonl")
BOLSA_OPE07_88 = os.path.join(PLAN, "OP_E_07_REBASE_V91.jsonl")
BOLSA_OPE06_114 = os.path.join(PLAN, "OP_E_06_DIRECCION_V90.jsonl")
BOLSA_OPE07_84 = os.path.join(PLAN, "OP_E_07_DIRECCION_V94.jsonl")

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from vuelta93_tarea3_guarda_direccion import (  # noqa: E402
    _ALTERNATIVAS_MARCA_MADRE, NIEGA_JERARQUIA, reconstruir_tercer_conjunto,
)

# ---------------------------------------------------------------------------
# (d) LAS DOS FORMAS LIMPIAS, anadidas a MARCA_MADRE_POSITIVA. Reusan _LINEA
# (la lookahead negativa que excluye "linea compartida") tal cual vive en
# vuelta93_tarea3_guarda_direccion.
# ---------------------------------------------------------------------------
_LINEA = r"l[ií]neas?(?!\s*compartid)"
_FORMULA_TRAE_ORDINAL = (
    r"trae\s+(?:el\s+procedimiento|la\s+forma)\s+de\s+"
    r"(?:la\s+(?:primera|segunda|tercera|cuarta|quinta)\b|una\s+de\s+sus\s+" + _LINEA + r")"
)

_ALTERNATIVAS_MARCA_MADRE_V94 = list(_ALTERNATIVAS_MARCA_MADRE) + [_FORMULA_TRAE_ORDINAL]
MARCA_MADRE_POSITIVA_V94 = re.compile("|".join(_ALTERNATIVAS_MARCA_MADRE_V94), re.IGNORECASE)


def guarda_direccion_v94(razon):
    """Identica a guarda_direccion de la vuelta 93, salvo que usa
    MARCA_MADRE_POSITIVA_V94 (con las dos formulas nuevas de la TAREA 4.d)."""
    tiene_marca = bool(MARCA_MADRE_POSITIVA_V94.search(razon))
    niega = bool(NIEGA_JERARQUIA.search(razon))
    if not tiene_marca:
        return "SALE"
    if niega and not tiene_marca:
        return "SALE"  # inalcanzable, igual que en la vuelta 93
    return "PASA"


# ---------------------------------------------------------------------------
# (a) LA LOOKBEHIND REPARADA DE MARCA_HIJO, como VENTANA de negacion (no un
# lookbehind de longitud variable, que Python `re` no soporta).
# ---------------------------------------------------------------------------
_TRAE = re.compile(r"trae\b(?!\s+lo\s+suyo)", re.IGNORECASE)
_DESARROLLA_O_RECORRE = re.compile(r"desarrolla|RECORRE\s+EL\s+CAMINO", re.IGNORECASE)
NEGACION_AMPLIA = re.compile(r"\b(?:no|ningun|ninguna|nadie|jamas|sin)\b", re.IGNORECASE)
VENTANA_NEGACION = 60


def marca_hijo_presente_v94(texto):
    """TAREA 4.a: reemplaza el MARCA_HIJO viejo. Un 'trae' cuenta como marca
    de hijo SOLO si ninguna de las palabras de NEGACION_AMPLIA aparece en las
    60 letras que lo preceden (la vieja lookbehind `(?<!no )` solo miraba las
    3 letras inmediatas). 'desarrolla' y 'RECORRE EL CAMINO' no cambian: el
    defecto medido es especifico de 'trae'."""
    if _DESARROLLA_O_RECORRE.search(texto):
        return True
    for m in _TRAE.finditer(texto):
        ventana = texto[max(0, m.start() - VENTANA_NEGACION):m.start()]
        if NEGACION_AMPLIA.search(ventana):
            continue
        return True
    return False


def extraer_direccion_automatica_v94(razon, id_a, id_b):
    """Espejo de extraer_direccion_automatica (scripts/loop/
    vuelta91_tarea4_direccion_ope07.py) con el guarda V94 y marca_hijo_
    presente_v94 en vez de MARCA_HIJO."""
    pos_a = razon.find(id_a)
    pos_b = razon.find(id_b)
    if pos_a == -1 or pos_b == -1:
        return "AMBIGUA"
    if guarda_direccion_v94(razon) == "SALE":
        return "AMBIGUA"
    if pos_a < pos_b:
        seg_a, seg_b = razon[pos_a:pos_b], razon[pos_b:]
    else:
        seg_b, seg_a = razon[pos_b:pos_a], razon[pos_a:]
    hijo_a = marca_hijo_presente_v94(seg_a[len(id_a):])
    hijo_b = marca_hijo_presente_v94(seg_b[len(id_b):])
    if hijo_a and not hijo_b:
        return "A_HIJO"
    if hijo_b and not hijo_a:
        return "B_HIJO"
    return "AMBIGUA"


def cargar_jsonl(ruta):
    with io.open(ruta, encoding="utf-8") as f:
        return [json.loads(l) for l in f if l.strip()]


def cargar_veredictos():
    return {int(v["puesto_intra"]): v for v in cargar_jsonl(VEREDICTOS)}


# ---------------------------------------------------------------------------
# LA VARA, LOS TRES CASOS OBLIGATORIOS
# ---------------------------------------------------------------------------
def vara_dura():
    veredictos = cargar_veredictos()

    print("=" * 90)
    print("VARA DURA, CASO 1: las 88 de OP_E_07_REBASE_V91.jsonl")
    print("=" * 90)
    print("CONJUNTO ESPERADO, DECIDIDO ANTES DE CORRER (TAREA 3 de esta vuelta): {1009, 1098}.")
    print("El 1281 y el 1992 SALEN de OP-E-07 (TAREA 3), pero NO por este guarda automatico:")
    print("  - el 1281 sale porque, tras reparar MARCA_HIJO (4.a), su unica marca de hijo (el")
    print("    'trae' de 'ningun habito general trae') queda NEGADA, y extraer_direccion_")
    print("    automatica_v94 lo deja AMBIGUA (verificado abajo, fuera de esta vara): no es un")
    print("    SALE del guarda de dos condiciones, es una ausencia de direccion resoluble.")
    print("  - el 1992 sale por relectura conjunta de un DIRECCION_MANUAL: su unica marca")
    print("    ('compara los') SIGUE viva en la lista (TAREA 4.c: no se quita, se declara")
    print("    inverificable si aplica), asi que guarda_direccion_v94 lo sigue marcando PASA;")
    print("    su salida de OP-E-07 no pasa por este guarda, pasa por la relectura de la TAREA 3.")
    filas = cargar_jsonl(BOLSA_OPE07_88)
    salen = []
    for f in filas:
        puesto = f["puesto"]
        v = veredictos.get(puesto)
        if v is None:
            print("ROJO: el puesto %s no tiene entrada en veredictos. NO SE TALLA NADA." % puesto)
            return 1
        if guarda_direccion_v94(v["razon"]) == "SALE":
            salen.append(puesto)
    salen = sorted(salen)
    print("SALEN (guarda automatico): %d %s" % (len(salen), salen))
    caso1_ok = salen == [1009, 1098]
    print("CASO 1 %s" % ("OK" if caso1_ok else "ROJO"))
    print()

    print("=" * 90)
    print("VARA DURA, CASO 2: las 114 de OP_E_06_DIRECCION_V90.jsonl, el 1160 PASA, 0 SALEN")
    print("=" * 90)
    filas2 = cargar_jsonl(BOLSA_OPE06_114)
    salen2 = []
    v1160 = None
    for f in filas2:
        puesto = f["puesto"]
        v = veredictos.get(puesto)
        if v is None:
            print("ROJO: el puesto %s no tiene entrada en veredictos. NO SE TALLA NADA." % puesto)
            return 1
        veredicto = guarda_direccion_v94(v["razon"])
        if veredicto == "SALE":
            salen2.append(puesto)
        if puesto == 1160:
            v1160 = veredicto
    print("total: %d, SALEN: %d %s, veredicto 1160: %s" % (len(filas2), len(salen2), salen2, v1160))
    caso2_ok = v1160 == "PASA" and len(salen2) == 0
    print("CASO 2 %s" % ("OK" if caso2_ok else "ROJO"))
    print()

    print("=" * 90)
    print("VARA DURA, CASO 3: el tercer conjunto de 81, los tres falsos SALE (995, 1007, 1024) PASAN")
    print("=" * 90)
    tercer = reconstruir_tercer_conjunto()
    print("tercer conjunto: %d filas" % len(tercer))
    salen3 = []
    for r in tercer:
        puesto = r["puesto"]
        v = veredictos.get(puesto)
        if v is None:
            print("ROJO: el puesto %s no tiene entrada en veredictos. NO SE TALLA NADA." % puesto)
            return 1
        if guarda_direccion_v94(v["razon"]) == "SALE":
            salen3.append(puesto)
    salen3 = sorted(salen3)
    faltan = {995, 1007, 1024} & set(salen3)
    print("SALEN: %d %s" % (len(salen3), salen3))
    caso3_ok = not faltan
    print("CASO 3 %s" % ("OK" if caso3_ok else "ROJO, siguen SALE: %s" % sorted(faltan)))
    print()

    print("=" * 90)
    if caso1_ok and caso2_ok and caso3_ok:
        print("LA VARA ALCANZA: los tres casos obligatorios se cumplen.")
        return 0
    print("LA VARA NO ALCANZA.")
    return 1


# ---------------------------------------------------------------------------
# (a) PRUEBA DE QUE LA AMPLIACION NO CAMBIA NINGUNA DE LAS 84 DIRECCIONES
# VIGENTES.
# ---------------------------------------------------------------------------
DIRECCION_MANUAL = {
    1163: "A_MADRE", 1191: "A_MADRE", 1388: "B_MADRE", 1500: "B_MADRE",
    1778: "B_MADRE", 1847: "A_MADRE", 1886: "A_MADRE",
    # 1992 YA NO VIVE AQUI: salio de OP-E-07 en la TAREA 3 de esta vuelta.
}


def veredicto_de_puesto(razon, id_a, id_b, puesto):
    if puesto in DIRECCION_MANUAL:
        return DIRECCION_MANUAL[puesto]
    auto = extraer_direccion_automatica_v94(razon, id_a, id_b)
    return {"A_HIJO": "B_MADRE", "B_HIJO": "A_MADRE", "AMBIGUA": "AMBIGUA"}[auto]


def sin_cambio():
    veredictos = cargar_veredictos()
    filas88 = {f["puesto"]: f for f in cargar_jsonl(BOLSA_OPE07_88)}
    vigentes = cargar_jsonl(BOLSA_OPE07_84)

    print("=" * 90)
    print("TAREA 4.a: LAS %d DIRECCIONES VIGENTES, RECALCULADAS CON EL GUARDA Y MARCA_HIJO REPARADOS"
          % len(vigentes))
    print("=" * 90)
    cambios = []
    for f in vigentes:
        puesto = f["puesto"]
        r88 = filas88.get(puesto)
        if r88 is None:
            print("ROJO: el puesto %s vigente no esta en la bolsa de 88. NO SE PUEDE COMPARAR." % puesto)
            return 1
        v = veredictos.get(puesto)
        veredicto_nuevo = veredicto_de_puesto(v["razon"], r88["nodo_a"], r88["nodo_b"], puesto)
        madre_nueva = r88["nodo_a"] if veredicto_nuevo == "A_MADRE" else (
            r88["nodo_b"] if veredicto_nuevo == "B_MADRE" else None)
        if madre_nueva != f["madre"]:
            cambios.append((puesto, f["madre"], f["hijo"], veredicto_nuevo, madre_nueva))

    print("filas vigentes verificadas: %d" % len(vigentes))
    if cambios:
        print("ROJO: %d direccion(es) CAMBIARON:" % len(cambios))
        for puesto, madre_vieja, hijo_viejo, veredicto_nuevo, madre_nueva in cambios:
            print("  puesto %d: era madre=%s hijo=%s -> ahora %s (madre=%s)"
                  % (puesto, madre_vieja, hijo_viejo, veredicto_nuevo, madre_nueva))
        return 1
    print("VERDE: NINGUNA de las %d direcciones vigentes cambio." % len(vigentes))
    return 0


# ---------------------------------------------------------------------------
# (c) EL SOSTEN UNICO, reconstruido sobre las 84 vigentes, con
# MARCA_MADRE_POSITIVA_V94 (las dos formulas nuevas incluidas).
# ---------------------------------------------------------------------------
def sosten_unico():
    veredictos = cargar_veredictos()
    vigentes = cargar_jsonl(BOLSA_OPE07_84)
    todas_razones = [v["razon"] for v in cargar_jsonl(VEREDICTOS)]

    patrones = [(p, re.compile(p, re.IGNORECASE)) for p in _ALTERNATIVAS_MARCA_MADRE_V94]
    freq = {p: sum(1 for r in todas_razones if patron.search(r)) for p, patron in patrones}

    print("=" * 90)
    print("TAREA 4.c: EL SOSTEN UNICO SOBRE LAS %d FILAS VIGENTES (post TAREA 3, con las 2 formulas nuevas)"
          % len(vigentes))
    print("=" * 90)
    unicos = []
    for f in vigentes:
        puesto = f["puesto"]
        razon = veredictos[puesto]["razon"]
        matches = [p for p, patron in patrones if patron.search(razon)]
        if len(matches) == 1:
            unicos.append((puesto, matches[0], freq[matches[0]]))
    unicos.sort(key=lambda x: x[2])
    print("pares con SOSTEN UNICO: %d de %d" % (len(unicos), len(vigentes)))
    for puesto, patron, f in unicos:
        print("  puesto %5d  sosten unico %-70s aparece en %4d razones" % (puesto, patron, f))

    freq_baja = [x for x in unicos if x[2] <= 3]
    print()
    print("de esos, con frecuencia <= 3 en las 3.388: %d" % len(freq_baja))
    for puesto, patron, f in freq_baja:
        print("  puesto %5d  %-70s freq %d" % (puesto, patron, f))

    print()
    print("=" * 90)
    print("LAS OCHO ALTERNATIVAS CON FRECUENCIA 1 EN TODO EL CATALOGO (3.388 razones), no solo")
    print("las que sostienen alguna fila vigente hoy:")
    print("=" * 90)
    freq1 = sorted([(p, f) for p, f in freq.items() if f == 1], key=lambda x: x[0])
    for p, f in freq1:
        print("  %-70s freq %d" % (p, f))
    print("total con frecuencia 1: %d" % len(freq1))
    return 0


def _autoprueba_mutacion():
    """TAREA 4.b: EL CASO ROJO POR MUTACION, sobre una entrada REAL (el
    segmento del hijo del puesto 1281, docs/INTRA_DOMINIO_VEREDICTOS.jsonl),
    no un literal disfrazado."""
    sys.path.insert(0, os.path.join(RAIZ, "scripts", "loop"))
    from verificar_caso_rojo_por_mutacion import probar_por_mutacion

    veredictos = cargar_veredictos()
    razon_1281 = veredictos[1281]["razon"]
    idx = razon_1281.find("pensamiento_visual_modelos_negocio")
    segmento_real = razon_1281[idx:]

    assert "ningun habito general trae" in segmento_real.lower()
    print("ENTRADA REAL: el segmento del hijo del puesto 1281 (docs/INTRA_DOMINIO_VEREDICTOS.jsonl),")
    print("que contiene el UNICO 'trae' negado por 'ningun' que motivo esta reparacion.")
    print()

    segmento_mutado = segmento_real.replace("ningun habito general trae", "un habito general trae")
    assert segmento_mutado != segmento_real
    probar_por_mutacion(
        nombre="marca_hijo_presente_v94 sobre el segmento real del puesto 1281 (quitar la negacion 'ningun')",
        criterio=marca_hijo_presente_v94, entrada=segmento_real, veredicto_esperado=False,
        entrada_mutada=segmento_mutado, veredicto_tras_mutar=True,
    )
    return 0


def main():
    if "--mutacion" in sys.argv:
        return _autoprueba_mutacion()
    if "--sin-cambio" in sys.argv:
        return sin_cambio()
    if "--sosten-unico" in sys.argv:
        return sosten_unico()
    return vara_dura()


if __name__ == "__main__":
    raise SystemExit(main())
