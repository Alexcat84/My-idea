"""Vuelta 28: declara un id nuevo en docs/plan/INDICE_ROJO_DECLARADO.jsonl.

Es el mecanismo escrito por el fundador el 14 ago 2026 (docs/plan/08_VERIFICACION.md,
CORRECCION DECLARADA: LA OPCION B SE EXTIENDE A TODAS LAS SEDES): una linea por id
declarado, {"id", "operacion", "fecha"}, y SOLO las operaciones de la pasada escriben
ahi, al crear un nodo.

Guardas:
  * el id tiene que EXISTIR en dataset/nodos (no se declara un nodo que no se creo)
  * el id NO puede tener ya vector en el indice semantico (declarar uno que si lo
    tiene seria tapar un rojo que no existe)
  * el id no puede estar ya declarado

Uso:
    python scripts/loop/vuelta28_declarar.py <OPERACION> <fecha> <id> [<id> ...]
"""
import json
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
NODOS = os.path.join(RAIZ, "dataset", "nodos")
LISTA = os.path.join(RAIZ, "docs", "plan", "INDICE_ROJO_DECLARADO.jsonl")
INDICE = os.path.join(RAIZ, "web", "lib", "assets", "semantic_index.json")


def ids_del_indice():
    if not os.path.exists(INDICE):
        return set()
    with open(INDICE, encoding="utf-8") as fh:
        d = json.load(fh)
    # La misma clave que lee el Gate 0 (scripts/run_phase1.py, step7_validate):
    # el indice es un dict con "ids" y "embeddings". No se adivina otra forma.
    return set(d["ids"])


def declarados():
    fuera = []
    if not os.path.exists(LISTA):
        return fuera
    with open(LISTA, encoding="utf-8") as fh:
        for linea in fh:
            linea = linea.strip()
            if linea:
                fuera.append(json.loads(linea))
    return fuera


def main():
    if len(sys.argv) < 4:
        print(__doc__)
        return 2
    operacion, fecha, nuevos = sys.argv[1], sys.argv[2], sys.argv[3:]

    con_vector = ids_del_indice()
    ya = {x["id"] for x in declarados()}
    fallos = []
    for nid in nuevos:
        if not os.path.exists(os.path.join(NODOS, nid + ".json")):
            fallos.append("%s: no existe en dataset/nodos" % nid)
        if nid in con_vector:
            fallos.append("%s: YA tiene vector en el indice, no hay rojo que declarar" % nid)
        if nid in ya:
            fallos.append("%s: ya estaba declarado" % nid)
    if fallos:
        print("PARADA: no se declara nada.")
        for f in fallos:
            print("  - %s" % f)
        return 1

    crudo = ""
    if os.path.exists(LISTA):
        with open(LISTA, "r", encoding="utf-8", newline="") as fh:
            crudo = fh.read()
    cola = "" if (not crudo or crudo.endswith("\n")) else "\n"
    with open(LISTA, "a", encoding="utf-8", newline="") as fh:
        if cola:
            fh.write(cola)
        for nid in nuevos:
            linea = json.dumps({"id": nid, "operacion": operacion, "fecha": fecha},
                               ensure_ascii=False)
            fh.write(linea + "\n")
            print("DECLARADO: %s" % linea)

    print("\nLISTA COMPLETA tras declarar (%d):" % len(declarados()))
    for x in declarados():
        print("  %-46s %-14s %s" % (x["id"], x["operacion"], x["fecha"]))
    return 0


if __name__ == "__main__":
    sys.exit(main())
