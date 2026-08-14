"""Instrumento de la vuelta 27: medicion de la fase 01_FUENTES para EJECUTAR.

No escribe NADA. Lee dataset/nodos, docs/plan/OPERACIONES.jsonl y las paginas de
doctrina, y saca por pantalla lo que la vuelta necesita para decidir por lectura.

Uso:
    python scripts/loop/vuelta27_medir.py citas
    python scripts/loop/vuelta27_medir.py bloque <node_id> [...]
    python scripts/loop/vuelta27_medir.py familia <trozo de fuente>
    python scripts/loop/vuelta27_medir.py nomina <ID_OP>
    python scripts/loop/vuelta27_medir.py objeto <node_id> [...]
    python scripts/loop/vuelta27_medir.py indice
"""
import json
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
NODOS = os.path.join(RAIZ, "dataset", "nodos")
OPS = os.path.join(RAIZ, "docs", "plan", "OPERACIONES.jsonl")
INDICE = os.path.join(RAIZ, "web", "lib", "assets", "semantic_index.json")


def cargar_nodos():
    fuera = {}
    for nombre in sorted(os.listdir(NODOS)):
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
            if linea:
                o = json.loads(linea)
                fuera[o["id_op"]] = o
    return fuera


def vivo(d):
    return not d.get("deprecado") and not d.get("deprecated")


# Las cinco correcciones que el commit del fundador dejo hechas, cada una con el
# fichero donde tiene que estar y el trozo literal que la identifica. El
# instrumento NO las reescribe: comprueba que estan y imprime la linea.
CITAS = [
    ("ROJO DECLARADO del indice semantico, exclusivo para ids nuevos",
     "docs/plan/08_VERIFICACION.md",
     "ROJO DECLARADO DEL INDICE SEMANTICO DURANTE LA FASE III"),
    ("el cierre de la fase III exige reindexado hecho y Gate 0 entero en verde",
     "docs/plan/08_VERIFICACION.md",
     "EL CIERRE DE LA FASE III EXIGE REINDEXADO HECHO"),
    ("P.18 EL DESTINO SE DECIDE POR LECTURA DE OBJETO",
     "docs/plan/BANCO_DEL_PLAN.md",
     "P.18 EL DESTINO SE DECIDE POR LECTURA DE OBJETO"),
    ("tercer desenlace de OP-F-03: familia HUGOS-SISTEMAS",
     "docs/plan/OPERACIONES.jsonl",
     "su bloque va a la familia HUGOS-SISTEMAS"),
    ("P.18 citada en las cuatro OP-F-04",
     "docs/plan/OPERACIONES.jsonl",
     "el miembro receptor se decide por P.18"),
]


def modo_citas():
    print("CITAS DE LAS CORRECCIONES DEL FUNDADOR, comprobadas contra el repo HOY")
    print("=" * 78)
    fallos = 0
    for titulo, ruta, aguja in CITAS:
        texto = open(os.path.join(RAIZ, ruta), encoding="utf-8").read()
        n = texto.count(aguja)
        estado = "PRESENTE" if n else "AUSENTE"
        if not n:
            fallos += 1
        print("\n[%s] %s" % (estado, titulo))
        print("  fichero  : %s" % ruta)
        print("  ocurrenc.: %d de %r" % (n, aguja))
    # las cuatro OP-F-04, una a una
    ops = cargar_ops()
    print("\nP.18 en cada OP-F-04, contada operacion por operacion:")
    for i in ("OP-F-04-COL", "OP-F-04-HOR", "OP-F-04-WEI", "OP-F-04-RAC"):
        nota = ops[i].get("nota") or ""
        print("  %-14s P.18 en la nota: %s" % (i, "SI" if "P.18" in nota else "NO"))
        if "P.18" not in nota:
            fallos += 1
    print("\n%s" % ("=" * 78))
    print("FALLOS: %d" % fallos)
    return 1 if fallos else 0


def modo_bloque(ids):
    nodos = cargar_nodos()
    for n in ids:
        d = nodos.get(n)
        if d is None:
            print("AUSENTE DEL GRAFO: %s" % n)
            continue
        pasos = d.get("pasos_accionables", []) or []
        print("-" * 78)
        print("ID    : %s   PASOS: %d   VIVO: %s" % (d["node_id"], len(pasos), vivo(d)))
        print("TITULO: %s" % d.get("titulo_concepto", ""))
        print("FUENTE: %s" % d.get("fuente", ""))
        print("ENTREG: %s" % d.get("entregable_esperado", ""))
        print("RESUME: %s" % d.get("resumen_teorico", ""))
        print("PREVIO: %s" % ", ".join(d.get("nodos_previos", []) or []))
        print("SIGUIE: %s" % ", ".join(d.get("nodos_siguientes", []) or []))
        print("ETIQUE: %s" % d.get("etiqueta_arbol", ""))
        print("CONDIC: %s" % " | ".join(d.get("condiciones_activacion", []) or []))
        for i, p in enumerate(pasos, 1):
            print("  %2d. %s" % (i, p))


def modo_familia(trozo):
    """La nomina vigente al dia de una familia de libro: los nodos VIVOS cuya
    fuente contiene el trozo. Compacto a proposito: el OBJETO de un nodo, para
    P.18, es su titulo mas su entregable mas su resumen."""
    nodos = cargar_nodos()
    sel = [d for d in nodos.values()
           if trozo.lower() in (d.get("fuente") or "").lower() and vivo(d)]
    unica = [d for d in sel if len(str(d.get("fuente", "")).split("|")) == 1]
    print("FAMILIA por fuente que contiene %r: %d nodos VIVOS, %d con fuente UNICA"
          % (trozo, len(sel), len(unica)))
    print("=" * 78)
    for d in sorted(sel, key=lambda x: x["node_id"]):
        multi = "" if len(str(d.get("fuente", "")).split("|")) == 1 else "  [MULTIFUENTE]"
        print("\n%s%s" % (d["node_id"], multi))
        print("  T: %s" % d.get("titulo_concepto", ""))
        print("  E: %s" % d.get("entregable_esperado", ""))
        print("  R: %s" % (d.get("resumen_teorico", "") or "")[:260])
        print("  dominio=%s fase=%s pasos=%d" % (
            d.get("dominio"), d.get("fase_proyecto"),
            len(d.get("pasos_accionables") or [])))


def modo_objeto(ids):
    nodos = cargar_nodos()
    for n in ids:
        d = nodos.get(n)
        if d is None:
            print("AUSENTE: %s" % n)
            continue
        print("\n%s  (vivo=%s, pasos=%d)" % (
            n, vivo(d), len(d.get("pasos_accionables") or [])))
        print("  T: %s" % d.get("titulo_concepto", ""))
        print("  E: %s" % d.get("entregable_esperado", ""))
        print("  F: %s" % d.get("fuente", ""))
        print("  R: %s" % (d.get("resumen_teorico", "") or "")[:300])


def modo_nomina(id_op):
    nodos = cargar_nodos()
    op = cargar_ops()[id_op]
    print("%s: %d nodos en el campo nodos" % (op["id_op"], len(op["nodos"])))
    print("%-46s %6s %6s  %s" % ("nodo", "pasos", "vivo", "fuente"))
    for n in op["nodos"]:
        d = nodos.get(n)
        if d is None:
            print("%-46s AUSENTE" % n)
            continue
        print("%-46s %6d %6s  %s" % (
            n, len(d.get("pasos_accionables") or []), vivo(d), d.get("fuente", "")))


def modo_indice():
    nodos = cargar_nodos()
    activos = {k for k, d in nodos.items() if vivo(d)}
    if not os.path.exists(INDICE):
        print("NO HAY INDICE en %s" % INDICE)
        return 1
    ids = set(json.load(open(INDICE, encoding="utf-8"))["ids"])
    sin = sorted(activos - ids)
    sobran = sorted(ids - activos)
    print("INDICE SEMANTICO, medido hoy")
    print("  nodos en disco      : %d" % len(nodos))
    print("  activos             : %d" % len(activos))
    print("  ids con vector      : %d" % len(ids))
    print("  ACTIVOS SIN VECTOR  : %d" % len(sin))
    for i in sin:
        print("     - %s" % i)
    print("  vectores sobrantes  : %d" % len(sobran))
    for i in sobran:
        print("     - %s" % i)
    return 0


def main():
    modo = sys.argv[1] if len(sys.argv) > 1 else ""
    if modo == "citas":
        return modo_citas()
    if modo == "bloque":
        modo_bloque(sys.argv[2:])
        return 0
    if modo == "familia":
        modo_familia(" ".join(sys.argv[2:]))
        return 0
    if modo == "objeto":
        modo_objeto(sys.argv[2:])
        return 0
    if modo == "nomina":
        modo_nomina(sys.argv[2])
        return 0
    if modo == "indice":
        return modo_indice()
    print(__doc__)
    return 2


if __name__ == "__main__":
    sys.exit(main())
