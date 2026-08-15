"""Vuelta 32, OP-D-02: MIDE el acto antes de fundir nada. DE SOLO LECTURA.

P.5 del BANCO_DEL_PLAN y la propia nota de OP-D-02 mandan lo mismo: el acto se
lee ENTERO despues del destejido y ANTES de la fusion, y la pregunta que contesta
es si el acto es UNA familia o DOS. Y la verificacion escrita de la operacion
pide, con estas palabras, 'el acto se leyo ENTERO antes de fundirse: cero pares
internos sin veredicto'.

Este script no funde, no escribe y no decide. Mide tres cosas y las imprime:

  1. LA COBERTURA DEL ACTO: los pares posibles entre los nodos de la nomina, y
     cuales tienen veredicto en docs/INTRA_DOMINIO_VEREDICTOS.jsonl y cuales no.
     Los que faltan van POR SU NOMBRE, porque una ausencia solo se afirma con lo
     leido entero (banco 9.26 y el visto primero del 9.3.1).
  2. EL CIERRE TRANSITIVO DE LAS A, que es la definicion de acto que la
     correccion del 18 ago 2026 al banco 9.3.1 fijo, y de cada nodo del acto si
     ALGUN par A declara un ganador.
  3. EL CENSO POR NOMBRE de la familia (banco 9.5.1: el censo por nombre se
     cuenta por script), para ver si la nomina de la operacion cubre a todos los
     nodos vivos que llevan la marca.

Uso: python scripts/loop/vuelta32_acto_opd02.py
"""
import itertools
import json
import os

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
NODOS = os.path.join(RAIZ, "dataset", "nodos")
OPS = os.path.join(RAIZ, "docs", "plan", "OPERACIONES.jsonl")
VER = os.path.join(RAIZ, "docs", "INTRA_DOMINIO_VEREDICTOS.jsonl")

MARCAS = ["voc", "voice_of_customer", "voz_del_cliente"]


def vivo(d):
    return not d.get("deprecado") and not d.get("deprecated")


def main():
    ops = {}
    with open(OPS, encoding="utf-8") as fh:
        for linea in fh:
            if linea.strip():
                o = json.loads(linea)
                ops[o["id_op"]] = o
    nomina = ops["OP-D-02"]["nodos"]

    vs = [json.loads(l) for l in open(VER, encoding="utf-8") if l.strip()]
    por_par = {}
    for v in vs:
        por_par[frozenset((v["nodo_a"], v["nodo_b"]))] = v

    print("=" * 78)
    print("EL ACTO DE OP-D-02, MEDIDO ANTES DE FUNDIR NADA")
    print("=" * 78)
    print()
    print("NOMINA DE LA OPERACION, leida hoy del fichero: %d nodos" % len(nomina))
    for nid in nomina:
        ruta = os.path.join(NODOS, nid + ".json")
        if not os.path.exists(ruta):
            print("  %-32s AUSENTE" % nid)
            continue
        with open(ruta, encoding="utf-8") as fh:
            d = json.load(fh)
        print("  %-32s pasos %2d  vivo %s  fuente: %s"
              % (nid, len(d.get("pasos_accionables") or []), vivo(d), d.get("fuente")))

    print()
    print("--- 1. COBERTURA DEL ACTO: los pares internos, uno por uno ---")
    pares = list(itertools.combinations(sorted(nomina), 2))
    con, sin = [], []
    for a, b in pares:
        v = por_par.get(frozenset((a, b)))
        if v is None:
            sin.append((a, b))
            print("  [SIN VEREDICTO] %-30s contra %-30s" % (a, b))
        else:
            con.append(v)
            print("  [%s puesto %4d] %-30s contra %-30s"
                  % (v["clase"], v["puesto_intra"], v["nodo_a"], v["nodo_b"]))
    print()
    print("  PARES POSIBLES %d, CON VEREDICTO %d, SIN VEREDICTO %d"
          % (len(pares), len(con), len(sin)))
    print("  LA VERIFICACION DE LA OPERACION PIDE CERO SIN VEREDICTO: %s"
          % ("CUMPLE" if not sin else "NO CUMPLE"))

    print()
    print("--- 2. EL CIERRE TRANSITIVO DE LAS A, y quien gana cada par A ---")
    aes = [v for v in con if v["clase"] == "A"]
    print("  pares A dentro de la nomina: %d" % len(aes))
    for v in aes:
        print("    puesto %d: %s contra %s" % (v["puesto_intra"], v["nodo_a"], v["nodo_b"]))
        print("      GANADOR DECLARADO EN LA RAZON: %s"
              % ("NO, la razon no nombra superviviente"
                 if "gana" not in v["razon"].lower() else "SI, la razon dice 'gana'"))
    tocados = set()
    for v in aes:
        tocados |= {v["nodo_a"], v["nodo_b"]}
    print("  nodos dentro del cierre transitivo de las A: %d de %d de la nomina"
          % (len(tocados), len(nomina)))
    print("    %s" % sorted(tocados))
    fuera = sorted(set(nomina) - tocados)
    print("  nodos de la nomina FUERA del cierre: %s" % (fuera or "ninguno"))
    print("  campo superviviente de la operacion, leido hoy: %r"
          % ops["OP-D-02"]["superviviente"])

    print()
    print("--- 3. CENSO POR NOMBRE DE LA FAMILIA (banco 9.5.1) ---")
    todos = {}
    for nombre in sorted(os.listdir(NODOS)):
        if not nombre.endswith(".json"):
            continue
        with open(os.path.join(NODOS, nombre), encoding="utf-8") as fh:
            d = json.load(fh)
        todos[d["node_id"]] = d
    marcados = sorted(k for k, d in todos.items()
                      if vivo(d) and any(m in k for m in MARCAS))
    print("  marcas buscadas: %s" % MARCAS)
    print("  nodos vivos que llevan alguna marca: %d" % len(marcados))
    for k in marcados:
        print("    %-38s %s  %s" % (k, "EN LA NOMINA" if k in nomina else "fuera",
                                    todos[k].get("fuente")))
    print()
    print("=" * 78)
    print("FIN DE LA MEDICION. Nada se fundio y nada se escribio.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
