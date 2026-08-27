# -*- coding: utf-8 -*-
"""vuelta86_tarea4_vara_tramo11.py . VUELTA 86, TAREA 4 (y TAREA 2.b, la pieza
BLOQUEANTE de la escalada de EJECUTOR.md regla 1). Sucesor directo de
scripts/loop/vuelta85_tarea5_vara_tramo10.py, mismo metodo (5.a y 5.b se
renumeran 4.a y 4.b, sin cambio de maquina), con el alcance fijado por la
adjudicacion 6.5 del acta de la vuelta 84 (sin ambiguedad):

(4.a) Cruza las 30 unidades frescas del tramo 11 contra
docs/INTRA_DOMINIO_VEREDICTOS.jsonl SIN DIRECCION (el par no dirigido {a, b}).
(4.b) Cruza las mismas 30 contra la bolsa filtrada de la vuelta ANTERIOR
(docs/plan/PASO_NODO_CALIBRADO_FILTRADO_V85.jsonl) buscando la reciproca (el
par al reves).

Los pares se LEEN de docs/loop/SALIDA_V86_TRAMO11_FILTRO_P91_GUARDA_CADENA.txt,
nunca tecleados.

(4.c / TAREA 2.b) LA TABLA DEL PATRON HISTORICO, la pieza que la escalada de
EJECUTOR.md regla 1 encarga (adjudicacion 5.3 del acta 85): la racha de
caidas de REPORTE llego a DOS tandas seguidas (dos en la vuelta 84, una en la
85), y las tres caidas fueron la misma especie exacta: prosa que compara un
tramo contra "el patron de tramos anteriores" sin que ningun instrumento la
sostenga. La caida de la vuelta 85 (acta 85, seccion 4.1) fue "en los tramos
8 y 9, los pares con veredicto D coincidieron siempre con NO SE ENLAZA",
desmentida por dos secciones del propio reporte de esa vuelta: el par
formulacion_teorias_causa -> diagrama_causa_efecto (tramo 9, clase D) figura
HOY como ESCRITA porque la TAREA 2 de esa misma vuelta lo escribio.

construir_patron_historico() talla, para CADA tramo de OP-E-01 que tenga
pares con veredicto, el par, su clase, su puesto, su dominio y SU DECISION
TAL COMO ESTA HOY EN EL REGISTRO (docs/plan/OP_E_01_DECIDIDAS.jsonl), cruzado
contra docs/INTRA_DOMINIO_VEREDICTOS.jsonl SIN DIRECCION (el mismo cruce sin
direccion que 4.a): nunca de memoria, nunca de un reporte viejo. Con esa
tabla delante, una frase como la que cayo no se puede volver a escribir sin
que la tabla la contradiga en el acto.

USO:
  python scripts/loop/vuelta86_tarea4_vara_tramo11.py
  python scripts/loop/vuelta86_tarea4_vara_tramo11.py --solo-patron-historico
"""
import argparse
import io
import json
import os
import re

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
FILTRO = os.path.join(RAIZ, "docs", "loop", "SALIDA_V86_TRAMO11_FILTRO_P91_GUARDA_CADENA.txt")
VEREDICTOS = os.path.join(RAIZ, "docs", "INTRA_DOMINIO_VEREDICTOS.jsonl")
BOLSA_ANTERIOR = os.path.join(RAIZ, "docs", "plan", "PASO_NODO_CALIBRADO_FILTRADO_V85.jsonl")
REGISTRO = os.path.join(RAIZ, "docs", "plan", "OP_E_01_DECIDIDAS.jsonl")

RE_UNIDAD = re.compile(r"^\s*(\d+):\s*(.+?)\s*->\s*(.+?)\s*\(paso\s*(.+?),\s*dominio\s*(.+?)\)\s*\|")


def leer_unidades():
    unidades = []
    for linea in io.open(FILTRO, encoding="utf-8"):
        m = RE_UNIDAD.match(linea)
        if m:
            idx, madre, hijo, paso, dominio = m.groups()
            unidades.append((int(idx), madre, hijo, paso, dominio))
    return unidades


def leer_veredictos():
    veredictos = {}
    total = 0
    for linea in io.open(VEREDICTOS, encoding="utf-8"):
        linea = linea.strip()
        if not linea:
            continue
        d = json.loads(linea)
        total += 1
        veredictos[frozenset((d["nodo_a"], d["nodo_b"]))] = d
    return veredictos, total


def leer_bolsa_anterior():
    filas = []
    if os.path.exists(BOLSA_ANTERIOR):
        for linea in io.open(BOLSA_ANTERIOR, encoding="utf-8"):
            linea = linea.strip()
            if linea:
                filas.append(json.loads(linea))
    return filas


def leer_registro():
    filas = []
    if os.path.exists(REGISTRO):
        for linea in io.open(REGISTRO, encoding="utf-8"):
            linea = linea.strip()
            if linea:
                filas.append(json.loads(linea))
    return filas


def par_de(fila):
    for clave_a, clave_b in (("madre", "hijo"), ("nodo_a", "nodo_b"),
                              ("origen", "destino"), ("desde", "hasta"), ("a", "b")):
        if clave_a in fila and clave_b in fila:
            return fila[clave_a], fila[clave_b]
    return None


def construir_patron_historico(registro, veredictos):
    """TAREA 2.b: para CADA tramo con pares con veredicto, imprime el par, su
    clase, su puesto, su dominio y SU DECISION TAL COMO ESTA HOY en el
    registro. Devuelve una lista de filas (tramo, madre, hijo, clase, puesto,
    dominio, decision), ordenada por tramo y luego por puesto."""
    filas = []
    for r in registro:
        v = veredictos.get(frozenset((r["madre"], r["hijo"])))
        if v is None:
            continue
        filas.append({
            "tramo": r["tramo"], "madre": r["madre"], "hijo": r["hijo"],
            "clase": v["clase"], "puesto": v["puesto_intra"], "dominio": v["dominio"],
            "decision": r["decision"],
        })
    filas.sort(key=lambda f: (f["tramo"], f["puesto"]))
    return filas


def imprimir_patron_historico(filas):
    print("=" * 78)
    print("LA TABLA DEL PATRON HISTORICO (TAREA 2.b, escalada de EJECUTOR.md regla 1,")
    print("adjudicacion 5.3 del acta 85). Tallada de docs/plan/OP_E_01_DECIDIDAS.jsonl")
    print("y docs/INTRA_DOMINIO_VEREDICTOS.jsonl. CADA fila es un par del registro que")
    print("SI tiene veredicto (cruce sin direccion); la columna decision es la de HOY.")
    print("=" * 78)
    print()
    print("| tramo | par | clase | puesto | dominio | decision (registro de hoy) |")
    print("|---:|---|:---:|---:|---|---|")
    for f in filas:
        print("| %s | `%s -> %s` | %s | %s | %s | %s |"
              % (f["tramo"], f["madre"], f["hijo"], f["clase"], f["puesto"], f["dominio"], f["decision"]))
    print()
    por_tramo = {}
    for f in filas:
        por_tramo.setdefault(f["tramo"], []).append(f)
    print("RESUMEN POR TRAMO (pares con veredicto | clase D | decision ESCRITA | decision NO SE ENLAZA):")
    for tramo in sorted(por_tramo, key=lambda t: (str(t))):
        grupo = por_tramo[tramo]
        d = sum(1 for f in grupo if f["clase"] == "D")
        escrita = sum(1 for f in grupo if f["decision"] == "ESCRITA")
        no_enlaza = sum(1 for f in grupo if f["decision"] == "NO SE ENLAZA")
        print("  tramo %s: %d con veredicto | %d clase D | %d ESCRITA | %d NO SE ENLAZA"
              % (tramo, len(grupo), d, escrita, no_enlaza))
    print()
    caso = [f for f in filas if f["madre"] == "formulacion_teorias_causa"
            and f["hijo"] == "diagrama_causa_efecto"]
    if caso:
        f = caso[0]
        print("CASO OBLIGATORIO (acta 85, adjudicacion 5.3): formulacion_teorias_causa -> "
              "diagrama_causa_efecto, tramo %s, clase %s, decision %s"
              % (f["tramo"], f["clase"], f["decision"]))
    else:
        print("CASO OBLIGATORIO: ROJO, formulacion_teorias_causa -> diagrama_causa_efecto "
              "no aparece en la tabla del patron historico (deberia, con veredicto D)")


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--solo-patron-historico", action="store_true",
                    help="corre solo la TAREA 2.b (no necesita el fichero del filtro del tramo 11)")
    a = ap.parse_args()

    veredictos, total = leer_veredictos()
    registro = leer_registro()

    if a.solo_patron_historico:
        print("veredictos leidos: %d | pares no dirigidos unicos: %d" % (total, len(veredictos)))
        print("registro leido: %d filas" % len(registro))
        print()
        filas_patron = construir_patron_historico(registro, veredictos)
        imprimir_patron_historico(filas_patron)
        return

    unidades = leer_unidades()
    frescas_idx = sorted({u[0] for u in unidades}, reverse=True)[:30]
    frescas = [u for u in unidades if u[0] in frescas_idx]
    print("unidades leidas del filtro: %d | frescas: %d" % (len(unidades), len(frescas)))
    assert len(frescas) == 30, "no son 30 frescas"

    print("veredictos leidos: %d | pares no dirigidos unicos: %d" % (total, len(veredictos)))

    bolsa_anterior = leer_bolsa_anterior()
    print("bolsa filtrada V85: %d unidades" % len(bolsa_anterior))

    pares_bolsa = set()
    for fila in bolsa_anterior:
        p = par_de(fila)
        if p:
            pares_bolsa.add(p)

    print()
    print("| # | par | veredicto sin direccion (4.a) | reciproca en la bolsa V85 (4.b) |")
    print("|---:|---|---|---|")
    con_veredicto = 0
    con_reciproca = 0
    for idx, madre, hijo, paso, dominio in frescas:
        v = veredictos.get(frozenset((madre, hijo)))
        if v:
            con_veredicto += 1
            celda = "%s puesto %d (%s), dirigido %s -> %s" % (
                v["clase"], v["puesto_intra"], v["dominio"], v["nodo_a"], v["nodo_b"])
        else:
            celda = "sin veredicto"
        reciproca = (hijo, madre) in pares_bolsa
        if reciproca:
            con_reciproca += 1
        print("| %d | `%s -> %s` (paso %s, dominio %s) | %s | %s |"
              % (idx, madre, hijo, paso, dominio, celda, "SI" if reciproca else "no"))

    print()
    print("RESUMEN: %d de 30 con veredicto, %d de 30 con reciproca" % (con_veredicto, con_reciproca))
    print()

    filas_patron = construir_patron_historico(registro, veredictos)
    imprimir_patron_historico(filas_patron)


if __name__ == "__main__":
    main()
