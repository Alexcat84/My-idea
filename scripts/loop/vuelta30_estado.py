"""Vuelta 30: el estado de la campana medido HOY, para APERTURA y para CIERRE.

EJECUTOR.md regla 1, tercer renglon: LA APERTURA SE MIDE ANTES DE LA PRIMERA
OPERACION. Y segundo renglon: EL ESTADO AL CIERRE SE MIDE AL CIERRE. Este
instrumento es el mismo en los dos momentos, para que las dos columnas del
reporte sean comparables digito a digito.

Nada sale de un acta ni de un reporte anterior: todo se mide aqui.

Uso: python scripts/loop/vuelta30_estado.py <APERTURA|CIERRE|etiqueta>
"""
import json
import os
import re
import sys
from collections import Counter

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
VER = os.path.join(RAIZ, "docs", "INTRA_DOMINIO_VEREDICTOS.jsonl")
NODOS = os.path.join(RAIZ, "dataset", "nodos")
OPS = os.path.join(RAIZ, "docs", "plan", "OPERACIONES.jsonl")
INV = os.path.join(RAIZ, "docs", "plan", "INVENTARIO.jsonl")
ROJO = os.path.join(RAIZ, "docs", "plan", "INDICE_ROJO_DECLARADO.jsonl")
FUENTES = os.path.join(RAIZ, "docs", "plan", "01_FUENTES.md")

# Las cinco familias de libro de la fase 01, con el trozo de fuente que las nombra.
# LOS TROZOS SON LOS DE LAS SALIDAS VERIFICADAS DE LAS VUELTAS 27 A 29, no otros:
# 'Traction', 'Hard Thing', 'Hugos', 'Coleman', 'Rackham'. Con el titulo completo
# del libro la nomina sale distinta, porque los nodos escriben la fuente con
# grafias que varian ('The Hard Thing About Hard Thing' sin la ese final vive en
# el grafo, medido hoy). Es el mismo criterio del modo familia de
# scripts/loop/vuelta27_medir.py.
FAMILIAS = [
    ("Weinberg", "Traction"),
    ("Horowitz", "Hard Thing"),
    ("Hugos", "Hugos"),
    ("Coleman", "Coleman"),
    ("Rackham", "Rackham"),
]

# LA FRONTERA PUBLICADA TIENE FORMA, y no basta con que la linea nombre al nodo:
# es la particion de los pasos escrita como '1 a 5 / 6 a 10'. Sin este patron el
# barrido cuenta como frontera cualquier linea de prosa que hable de pasos (la
# primera pasada de este instrumento dio 3 de 15 por eso, y la buena es 2 de 15,
# la que la vuelta 29 publico en 01_FUENTES.md linea 979).
PATRON_FRONTERA = r"\d+\s+a\s+\d+\s*/\s*\d+\s+a\s+\d+"

# Los tres bloques de TOQUE UNICO que la parada de la vuelta 29 dejo sin ejecutar.
TOQUE_UNICO = [
    "coeficiente_viral",
    "viral_loop_marketing",
    "decision_de_vender_startup",
]

OPS_FASE01 = ["OP-F-01", "OP-F-02", "OP-F-03",
              "OP-F-04-COL", "OP-F-04-HOR", "OP-F-04-WEI", "OP-F-04-RAC"]


def leer_jsonl(ruta):
    fuera = []
    with open(ruta, encoding="utf-8") as fh:
        for linea in fh:
            linea = linea.strip()
            if linea:
                fuera.append(json.loads(linea))
    return fuera


def cargar_nodos():
    fuera = {}
    for nombre in sorted(os.listdir(NODOS)):
        if not nombre.endswith(".json"):
            continue
        with open(os.path.join(NODOS, nombre), encoding="utf-8") as fh:
            d = json.load(fh)
        fuera[d["node_id"]] = d
    return fuera


def vivo(d):
    return not d.get("deprecado") and not d.get("deprecated")


def main():
    etiqueta = sys.argv[1] if len(sys.argv) > 1 else "SIN ETIQUETA"
    print("=" * 78)
    print("ESTADO DE LA CAMPANA, MEDICION DE %s" % etiqueta)
    print("=" * 78)

    print()
    print("--- EL MARCADOR ---")
    v = leer_jsonl(VER)
    puestos = [x["puesto_intra"] for x in v]
    clases = Counter(x["clase"] for x in v)
    n = len(v)
    print("n = %d" % n)
    for c in ("A", "B", "C", "D"):
        print("  %s %5d  %5.1f por ciento" % (c, clases[c], 100.0 * clases[c] / n))
    print("clases fuera de ABCD: %s" % (sorted(set(clases) - set("ABCD")) or 0))
    print("rango de puestos: %d a %d" % (min(puestos), max(puestos)))
    print("huecos: %d" % len(set(range(min(puestos), max(puestos) + 1)) - set(puestos)))
    print("duplicados: %d" % len([p for p, c in Counter(puestos).items() if c > 1]))

    print()
    print("--- EL GRAFO ---")
    nodos = cargar_nodos()
    ficheros = [f for f in os.listdir(NODOS) if f.endswith(".json")]
    dep = [k for k, d in nodos.items() if not vivo(d)]
    enl = sum(len(d.get("nodos_previos") or []) + len(d.get("nodos_siguientes") or [])
              for d in nodos.values())
    claves = set()
    for d in nodos.values():
        claves |= set(d.keys())
    print("ficheros        : %d" % len(ficheros))
    print("ids unicos      : %d" % len(nodos))
    print("vivos           : %d" % (len(nodos) - len(dep)))
    print("deprecados      : %d" % len(dep))
    print("enlaces         : %d (previos mas siguientes)" % enl)
    print("claves distintas: %d" % len(claves))

    print()
    print("--- LAS FAMILIAS DE LIBRO (nomina vigente al dia) ---")
    print("%-12s %-42s %6s %8s" % ("familia", "trozo de fuente", "vivos", "unicos"))
    for nombre, trozo in FAMILIAS:
        sel = [d for d in nodos.values()
               if trozo.lower() in (d.get("fuente") or "").lower() and vivo(d)]
        unica = [d for d in sel if len(str(d.get("fuente", "")).split("|")) == 1]
        print("%-12s %-42s %6d %8d" % (nombre, trozo, len(sel), len(unica)))

    print()
    print("--- LAS OPERACIONES ---")
    ops = leer_jsonl(OPS)
    ids = [o["id_op"] for o in ops]
    print("operaciones: %d, ids unicos: %d" % (len(ops), len(set(ids))))
    print("estados: %s" % dict(Counter(o["estado"] for o in ops)))
    rotas = []
    for o in ops:
        for d in (o.get("depende_de") or []) + (o.get("bloquea_a") or []):
            if d not in set(ids):
                rotas.append((o["id_op"], d))
    print("dependencias rotas: %d" % len(rotas))
    porid = {o["id_op"]: o for o in ops}
    print()
    print("%-14s %-8s %6s %8s  %s" % ("op de fase 01", "estado", "nodos", "nota", "HECHA en la nota"))
    for i in OPS_FASE01:
        o = porid[i]
        nota = o.get("nota") or ""
        print("%-14s %-8s %6d %8d  %s" % (
            i, o["estado"], len(o.get("nodos") or []), len(nota),
            "SI" if "HECHA" in nota else "NO"))

    print()
    print("--- EL INVENTARIO ---")
    inv = leer_jsonl(INV)
    print("entradas: %d" % len(inv))
    print("por tipo: %s" % dict(Counter(x["tipo"] for x in inv)))

    print()
    print("--- EL INDICE ROJO DECLARADO ---")
    rojo = leer_jsonl(ROJO) if os.path.exists(ROJO) else []
    print("lineas: %d" % len(rojo))
    print("por operacion: %s" % dict(Counter(x["operacion"] for x in rojo)))
    faltan = [x["id"] for x in rojo if x["id"] not in nodos]
    print("ids del rojo AUSENTES del grafo: %d %s" % (len(faltan), faltan or ""))

    print()
    print("--- LOS TRES NODOS DE TOQUE UNICO (la parada de la vuelta 29) ---")
    for nid in TOQUE_UNICO:
        d = nodos.get(nid)
        if d is None:
            print("%-30s AUSENTE" % nid)
            continue
        print("%-30s pasos %3d  vivo %s  fuente: %s" % (
            nid, len(d.get("pasos_accionables") or []), vivo(d), d.get("fuente")))

    print()
    print("--- FRONTERAS PUBLICADAS DE OP-F-04-COL ---")
    texto = open(FUENTES, encoding="utf-8").read().splitlines()
    col = porid["OP-F-04-COL"]["nodos"]
    con = 0
    for nid in sorted(col):
        lineas = [i + 1 for i, l in enumerate(texto) if nid in l]
        confront = [i for i in lineas if re.search(PATRON_FRONTERA, texto[i - 1])]
        if confront:
            con += 1
        print("  %-38s lineas=%-24s CON FRONTERA: %s" % (
            nid, lineas or "ninguna", confront or "NO"))
    print("CON FRONTERA PUBLICADA: %d de %d" % (con, len(col)))

    print()
    print("=" * 78)
    print("FIN DE LA MEDICION DE %s" % etiqueta)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
