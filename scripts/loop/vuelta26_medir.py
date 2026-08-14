"""Instrumento de la vuelta 26: medicion de la fase 01_FUENTES.

No escribe nada. Solo lee dataset/nodos y docs/plan/OPERACIONES.jsonl y saca por
pantalla lo que la vuelta necesita para ejecutar por lectura.

Uso:
    python scripts/loop/vuelta26_medir.py opf01
    python scripts/loop/vuelta26_medir.py opf02
    python scripts/loop/vuelta26_medir.py racimo
    python scripts/loop/vuelta26_medir.py pasos <node_id> [<node_id> ...]
    python scripts/loop/vuelta26_medir.py nomina <ID_OP>
"""
import json
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
NODOS = os.path.join(RAIZ, "dataset", "nodos")
OPS = os.path.join(RAIZ, "docs", "plan", "OPERACIONES.jsonl")


def cargar_nodos():
    fuera = {}
    for nombre in os.listdir(NODOS):
        if not nombre.endswith(".json"):
            continue
        with open(os.path.join(NODOS, nombre), encoding="utf-8") as fh:
            d = json.load(fh)
        fuera[d["node_id"]] = d
    return fuera


def cargar_ops():
    fuera = {}
    with open(OPS, encoding="utf-8") as fh:
        for linea in fh:
            linea = linea.strip()
            if not linea:
                continue
            o = json.loads(linea)
            fuera[o["id_op"]] = o
    return fuera


def vivo(d):
    return not d.get("deprecated") and not d.get("deprecado")


def imprimir_nodo(d, con_pasos=True):
    print("-" * 78)
    print("ID      : %s" % d["node_id"])
    print("TITULO  : %s" % d.get("titulo_concepto", ""))
    print("FUENTE  : %s" % d.get("fuente", ""))
    print("DOMINIO : %s   FASE: %s" % (d.get("dominio"), d.get("fase_proyecto")))
    print("VIVO    : %s" % vivo(d))
    print("ENTREGABLE: %s" % d.get("entregable_esperado", ""))
    pasos = d.get("pasos_accionables", []) or []
    print("PASOS   : %d" % len(pasos))
    if con_pasos:
        for i, p in enumerate(pasos, 1):
            print("  %2d. %s" % (i, p))
        print("RESUMEN : %s" % d.get("resumen_teorico", ""))
        print("PREVIOS : %s" % ", ".join(d.get("nodos_previos", []) or []))
        print("SIGUIENT: %s" % ", ".join(d.get("nodos_siguientes", []) or []))
        print("ETIQUETA: %s" % d.get("etiqueta_arbol", ""))


PUBLICADO_OPF01 = {
    "seleccion_representante_extranjero": 9,
    "internacionalizacion_sitio_web_exportacion": 9,
    "elaboracion_pro_forma_invoice": 8,
    "elementos_plan_exportacion_ejemplo": 13,
    "principios_medicion_efectiva": 10,
    "fmea_analisis_de_modos_de_falla": 8,
}

RACIMO_IA = [
    "principio_humano_en_el_loop",
    "human_in_the_loop_ia",
    "alineacion_etica_ia_negocio",
    "mitigar_falling_asleep_wheel",
    "riesgo_sobredependencia_ia",
    "comprension_capacidades_limitaciones_ia",
    "jagged_frontier_ia",
    "invitar_ia_a_todo",
    "principio_invitar_ia_siempre",
    "comprender_alineacion_etica_ia",
]


def main():
    modo = sys.argv[1] if len(sys.argv) > 1 else "opf01"
    nodos = cargar_nodos()
    ops = cargar_ops()

    if modo == "opf01":
        op = ops["OP-F-01"]
        print("OP-F-01, campo nodos: %d miembros" % len(op["nodos"]))
        for n in op["nodos"]:
            print("  - %s" % n)
        print()
        print("VERIFICACION 1 y 2, medidas contra el grafo de hoy:")
        print("%-46s %6s %10s %6s" % ("nodo", "pasos", "publicado", "vivo"))
        for n in op["nodos"]:
            d = nodos.get(n)
            if d is None:
                print("%-46s %6s %10s %6s" % (n, "AUSENTE", "-", "-"))
                continue
            print("%-46s %6d %10s %6s" % (
                n, len(d.get("pasos_accionables", [])),
                PUBLICADO_OPF01.get(n, "?"), vivo(d)))
        print()
        print("CRUCE: cada uno de los seis, en que otras operaciones aparece")
        for n in op["nodos"]:
            otras = [i for i, o in ops.items()
                     if i != "OP-F-01" and n in (o.get("nodos") or [])]
            print("  %-46s %s" % (n, otras if otras else "en ninguna otra"))
        print()
        print("BARRIDO: background_startup_vs_corporativo en que operaciones esta")
        otras = [i for i, o in ops.items()
                 if "background_startup_vs_corporativo" in (o.get("nodos") or [])]
        print("  %s" % otras)

    elif modo == "opf02":
        for n in ops["OP-F-02"]["nodos"]:
            imprimir_nodo(nodos[n])

    elif modo == "racimo":
        print("RACIMO DE SUPERVISION DE LA IA, nomina vigente al puesto 1517 (10)")
        for n in RACIMO_IA:
            d = nodos.get(n)
            if d is None:
                print("AUSENTE DEL GRAFO: %s" % n)
                continue
            imprimir_nodo(d)

    elif modo == "bloque":
        # Solo id, fuente y pasos numerados. Sin filtros de consola: un filtro
        # que se traga una linea de paso deja leer un nodo incompleto.
        for n in sys.argv[2:]:
            d = nodos.get(n)
            if d is None:
                print("AUSENTE DEL GRAFO: %s" % n)
                continue
            pasos = d.get("pasos_accionables", []) or []
            print("-" * 78)
            print("ID    : %s   PASOS: %d" % (d["node_id"], len(pasos)))
            print("FUENTE: %s" % d.get("fuente", ""))
            for i, p in enumerate(pasos, 1):
                print("  %2d. %s" % (i, p))

    elif modo == "pasos":
        for n in sys.argv[2:]:
            d = nodos.get(n)
            if d is None:
                print("AUSENTE DEL GRAFO: %s" % n)
                continue
            imprimir_nodo(d)

    elif modo == "nomina":
        op = ops[sys.argv[2]]
        print("%s: %d nodos" % (op["id_op"], len(op["nodos"])))
        print("%-48s %6s %6s  %s" % ("nodo", "pasos", "vivo", "fuente"))
        for n in op["nodos"]:
            d = nodos.get(n)
            if d is None:
                print("%-48s AUSENTE" % n)
                continue
            print("%-48s %6d %6s  %s" % (
                n, len(d.get("pasos_accionables", [])), vivo(d), d.get("fuente", "")))

    else:
        print(__doc__)
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
