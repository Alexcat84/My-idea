# -*- coding: utf-8 -*-
"""vuelta54_tramo2_nomina.py . LA NOMINA DEL TRAMO 2 DE OP-U-01, RE-MEDIDA AL
ABRIRLO, CON EL ORDEN IMPRESO Y LAS DOS GUARDAS.

DE SOLO LECTURA. No toca ni un nodo, ni un veredicto, ni una operacion:
imprime, y solo escribe el fichero que se le nombre en --salida.

LA DEFINICION VIGENTE DEL TRAMO, citada de docs/plan/03_FUSIONES.md (la
cabecera del registro del tramo 1, 19 ago 2026, vuelta 48):

    "El tramo son los CINCUENTA primeros actos CERRADOS de la nomina re-medida
     al abrirlo, en el orden en que el instrumento los imprime, que es la vara
     que el auditor adjudico."

EL TRAMO 2 SON LOS 50 SIGUIENTES, y aqui esta el problema que este instrumento
resuelve MIDIENDO en vez de decidiendo: "los siguientes" se puede leer de dos
maneras, y las dos se computan y se comparan.

  LECTURA A, por el orden de HOY: se re-mide la nomina hoy, se marcan los
  actos del tramo 1 que siguen vivos (identificados POR SUS MIEMBROS y no por
  su numero, que es la doctrina de la pagina) y el tramo 2 son los 50 actos
  CERRADOS siguientes en el orden impreso.

  LECTURA B, por el orden del dia en que el tramo 1 se abrio: el tramo 2 son
  los actos que ocupaban los puestos 51 a 100 de la nomina de la vuelta 48
  (docs/loop/RECOMPUTO_V48_COMPONENTES.jsonl), los que sigan CERRADOS hoy.

SI LAS DOS COINCIDEN, el tramo esta determinado y no hay nada que decidir. SI
NO COINCIDEN, el instrumento lo dice y NO elige: eso seria una operacion cuyo
texto no alcanza para ejecutarse sin decidir, y entonces para y convoca.

LAS DOS GUARDAS QUE CORRE:
  - LA GUARDA DE LOS CUATRO AJENOS (03_FUSIONES.md, 11 ago 2026): los cuatro
    actos que esa pagina declara fuera de OP-U-01 para siempre.
  - LA GUARDA DE SOLAPE CON EL TRAMO 1: ningun acto del tramo 2 puede tocar un
    miembro de un acto del tramo 1.

Uso:
  python scripts/loop/vuelta54_tramo2_nomina.py --nomina docs/loop/RECOMPUTO_V54_APERTURA.jsonl
        [--salida docs/loop/TRAMO2_V54.jsonl]
"""
import argparse
import io
import json
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
V48 = os.path.join(RAIZ, "docs", "loop", "RECOMPUTO_V48_COMPONENTES.jsonl")

# 03_FUSIONES.md declara desde el 11 ago 2026 que estos cuatro no se resuelven
# nunca en OP-U-01. Misma lista que scripts/loop/vuelta48_dossier_actos.py.
AJENOS = ["gates_go_kill_decision_points", "customer_discovery",
          "ab_testing_optimizacion", "brainstorming_divergente"]

TAM_TRAMO = 50


def cargar(p):
    return [json.loads(l) for l in io.open(p, encoding="utf-8") if l.strip()]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--nomina", required=True)
    ap.add_argument("--salida", default=None)
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")

    hoy = [r for r in cargar(a.nomina) if r["estado"] == "CERRADO"]
    v48 = [r for r in cargar(V48) if r["estado"] == "CERRADO"]

    print("=" * 78)
    print("LA NOMINA DEL TRAMO 2 DE OP-U-01, RE-MEDIDA AL ABRIRLO (vuelta 54)")
    print("=" * 78)
    print()
    print("  nomina de hoy   : %s (%d actos CERRADOS)" % (a.nomina, len(hoy)))
    print("  nomina de la 48 : %s (%d actos CERRADOS)" % (os.path.relpath(V48, RAIZ), len(v48)))
    print()

    # ---- el tramo 1, por sus miembros ----
    tramo1 = v48[:TAM_TRAMO]
    mi1 = set()
    for r in tramo1:
        mi1 |= set(r["miembros"])
    print("--- EL TRAMO 1, IDENTIFICADO POR SUS MIEMBROS Y NO POR SU NUMERO ---")
    print("  actos del tramo 1 en la nomina de la 48: %d" % len(tramo1))
    print("  miembros que esos 50 actos nombraban   : %d" % len(mi1))
    vivos1 = [(i, r) for i, r in enumerate(hoy, 1) if set(r["miembros"]) & mi1]
    print("  actos de HOY que tocan a alguno        : %d, en los puestos %s"
          % (len(vivos1), [i for i, _ in vivos1]))
    print()

    # ---- LECTURA A ----
    resto = [(i, r) for i, r in enumerate(hoy, 1) if not (set(r["miembros"]) & mi1)]
    lectA = resto[:TAM_TRAMO]
    print("--- LECTURA A: los 50 CERRADOS siguientes en el orden impreso de HOY ---")
    print("  puestos de hoy: del %d al %d" % (lectA[0][0], lectA[-1][0]))
    print()

    # ---- LECTURA B ----
    idx48 = {}
    for i, r in enumerate(v48, 1):
        for m in r["miembros"]:
            idx48.setdefault(m, i)
    lectB = []
    for i, r in enumerate(hoy, 1):
        ids = sorted({idx48[m] for m in r["miembros"] if m in idx48})
        if ids and TAM_TRAMO < ids[0] <= 2 * TAM_TRAMO:
            lectB.append((i, r))
    print("--- LECTURA B: los que ocupaban los puestos 51 a 100 en la nomina de la 48 ---")
    print("  actos encontrados hoy: %d" % len(lectB))
    print()

    clave = lambda par: tuple(sorted(par[1]["miembros"]))
    iguales = [clave(x) for x in lectA] == [clave(x) for x in lectB]
    print("--- LAS DOS LECTURAS ---")
    print("  LECTURA A y LECTURA B dan el MISMO tramo, en el MISMO orden: %s"
          % ("SI" if iguales else "NO"))
    if not iguales:
        soloA = {clave(x) for x in lectA} - {clave(x) for x in lectB}
        soloB = {clave(x) for x in lectB} - {clave(x) for x in lectA}
        print("  solo en A: %d | solo en B: %d" % (len(soloA), len(soloB)))
        for c in sorted(soloA):
            print("     A: %s" % (", ".join(c)))
        for c in sorted(soloB):
            print("     B: %s" % (", ".join(c)))
        print()
        print("  ROJO: el tramo NO esta determinado por el texto. PARADA.")
        return 1
    print()

    tramo2 = lectA

    print("--- GUARDA DE LOS CUATRO AJENOS (03_FUSIONES.md, 11 ago 2026) ---")
    sucio = []
    for x in AJENOS:
        dentro = [i for i, r in tramo2 if x in r["miembros"]]
        enlote = [i for i, r in enumerate(hoy, 1) if x in r["miembros"]]
        if dentro:
            sucio.append(x)
        print("   %-38s en el TRAMO 2: %-22s en el lote CERRADO entero: %s"
              % (x, "SI, puestos %s" % dentro if dentro else "NO",
                 enlote if enlote else "NO"))
    print("   GUARDA: %s" % ("ROJO" if sucio else "VERDE, ninguno de los cuatro entra"))
    print()

    print("--- GUARDA DE SOLAPE CON EL TRAMO 1 ---")
    solapan = [(i, sorted(set(r["miembros"]) & mi1)) for i, r in tramo2
               if set(r["miembros"]) & mi1]
    print("   actos del tramo 2 que tocan un miembro del tramo 1: %d" % len(solapan))
    print("   GUARDA: %s" % ("ROJO" if solapan else "VERDE, ningun solape"))
    print()

    print("--- EL TRAMO 2, EN EL ORDEN IMPRESO ---")
    print()
    print("  %-4s %-5s %-6s %-7s %-28s %s"
          % ("#", "hoy", "en 48", "tamano", "clases internas", "miembros"))
    tam = {}
    figuras = {"PURO A": 0, "MIXTO": 0}
    salida = []
    for n, (i, r) in enumerate(tramo2, 1):
        ids = sorted({idx48[m] for m in r["miembros"] if m in idx48})
        cl = r["clases_internas"]
        puro = set(cl) == {"A"}
        figuras["PURO A" if puro else "MIXTO"] += 1
        tam[r["tamano"]] = tam.get(r["tamano"], 0) + 1
        print("  %-4d %-5d %-6s %-7d %-28s %s"
              % (n, i, ids[0] if ids else "nuevo", r["tamano"], cl,
                 ", ".join(sorted(r["miembros"]))))
        fila = dict(r)
        fila["orden_tramo2"] = n
        fila["puesto_hoy"] = i
        fila["puesto_v48"] = ids[0] if ids else None
        fila["figura"] = "PURO A" if puro else "MIXTO"
        salida.append(fila)
    print()
    print("  actos del tramo 2      : %d" % len(tramo2))
    print("  por tamano             : %s" % dict(sorted(tam.items())))
    print("  por figura             : %s" % figuras)
    print("  nodos implicados       : %d" % sum(r["tamano"] for _, r in tramo2))
    print("  nodos que MORIRIAN si se funden todos (tamano menos 1 por acto): %d"
          % sum(r["tamano"] - 1 for _, r in tramo2))
    print()

    if a.salida:
        with io.open(a.salida, "w", encoding="utf-8", newline=chr(10)) as f:
            for fila in salida:
                f.write(json.dumps(fila, ensure_ascii=False) + chr(10))
        print("  escrito: %s" % a.salida)
        print()

    print("FIN")
    return 0 if not sucio and not solapan else 1


if __name__ == "__main__":
    raise SystemExit(main())
