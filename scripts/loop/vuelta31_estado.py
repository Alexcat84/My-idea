"""Vuelta 31: el estado de la campana medido HOY, para APERTURA y para CIERRE.

SUCESOR DE scripts/loop/vuelta30_estado.py. Todo lo que aquel media se mide
igual, digito a digito, para que las dos columnas del reporte sigan siendo
comparables. LO UNICO QUE CAMBIA ES EL DETECTOR DE FRONTERAS, y el cambio va
declarado abajo con su motivo, porque cambiar un instrumento sin declararlo es
justamente lo que la regla 2 del EJECUTOR.md prohibe.

EJECUTOR.md regla 1, tercer renglon: LA APERTURA SE MIDE ANTES DE LA PRIMERA
OPERACION. Y segundo renglon: EL ESTADO AL CIERRE SE MIDE AL CIERRE.

Nada sale de un acta ni de un reporte anterior: todo se mide aqui.

Uso: python scripts/loop/vuelta31_estado.py <APERTURA|CIERRE|etiqueta>
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
# primera pasada del instrumento de la vuelta 30 dio 3 de 15 por eso).
PATRON_FRONTERA = r"\d+\s+a\s+\d+\s*/\s*\d+\s+a\s+\d+"

# ---------------------------------------------------------------------------
# EL CAMBIO DE ESTA VUELTA, DECLARADO (14 ago 2026, vuelta 31, TAREA 1.4 del
# encargo, que lo ordena citando la adjudicacion 4 del acta de la vuelta 30).
#
# EL MOTIVO, con la medicion que lo levanto: el detector de la vuelta 30 exigia
# que el ID DEL NODO y la PARTICION vivieran EN LA MISMA LINEA. Esa es la forma
# TIPICA (la fila de tabla de la tanda de los injertos), pero NO es la unica
# forma que una frontera publicada tiene hoy: P.20 (UN NODO, UN CORTE) le dio a
# viral_loop_marketing una forma distinta y legitima, porque su punto 2 manda
# publicarla COMO REGISTRO UNICO de los tres libros: una SUBSECCION con su
# encabezado propio (que es donde vive el id del nodo), una tabla con el tramo de
# cada libro, y la particion completa escrita en el cuerpo, LINEAS MAS ABAJO
# ('LA FRONTERA ES `1 a 3 / 4 a 25 / 26 a 30`', 01_FUENTES.md).
#
# El instrumento viejo la contaba como SIN FRONTERA. No estaba mal medido: estaba
# midiendo UNA forma. Por eso la vuelta 30 publico su cifra (13 de 15) con su
# limitacion declarada en vez de tocar el detector para que diera el numero que
# le convenia, y el acta de la vuelta 30 adjudico en su punto 4 (linea 6631,
# leida hoy) que 'LAS DOS VIVEN, CADA UNA CON SU NOMBRE, y la vara de cierre es
# la LECTURA', mandando ampliar el detector a la forma de subseccion.
#
# LO QUE SE AMPLIA, y nada mas que eso: se reconoce una segunda FORMA. No se
# afloja el patron de particion (sigue siendo el mismo regex), no se cuenta
# ninguna prosa, y no se mete ninguna excepcion por nombre de nodo: un nodo con
# frontera de forma B tiene que tener su ID EN UN ENCABEZADO y la PARTICION
# DENTRO DEL CUERPO DE ESA MISMA SUBSECCION, delimitada por el siguiente
# encabezado de nivel igual o superior. Si manana otro nodo publica asi, el
# detector lo cuenta solo.
# ---------------------------------------------------------------------------
PATRON_ENCABEZADO = r"^(#{1,6})\s"

# Los tres bloques de TOQUE UNICO que la parada de la vuelta 29 dejo sin ejecutar
# y que la vuelta 30 ejecuto con P.19 y P.20.
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


def subsecciones(texto):
    """Cada encabezado del documento con el rango de lineas de su cuerpo.

    Devuelve [(indice_del_encabezado, nivel, inicio_cuerpo, fin_cuerpo)], con
    los indices en base 0 y fin_cuerpo exclusivo. El cuerpo de un encabezado
    termina en el siguiente encabezado de nivel IGUAL O SUPERIOR (uno mas
    profundo sigue siendo parte del cuerpo del padre).
    """
    cabezas = []
    for i, linea in enumerate(texto):
        m = re.match(PATRON_ENCABEZADO, linea)
        if m:
            cabezas.append((i, len(m.group(1))))
    fuera = []
    for pos, (i, nivel) in enumerate(cabezas):
        fin = len(texto)
        for j, nivel2 in cabezas[pos + 1:]:
            if nivel2 <= nivel:
                fin = j
                break
        fuera.append((i, nivel, i + 1, fin))
    return fuera


def fronteras_del_nodo(nid, texto, secs):
    """Las dos formas. Devuelve (forma, lineas_con_el_id, lineas_de_frontera)."""
    lineas = [i + 1 for i, l in enumerate(texto) if nid in l]

    # FORMA A, la tipica: id y particion en la misma linea.
    a = [i for i in lineas if re.search(PATRON_FRONTERA, texto[i - 1])]
    if a:
        return "A", lineas, a

    # FORMA B, la que P.20 estreno: el id en un encabezado, la particion en el
    # cuerpo de esa misma subseccion.
    b = []
    for i, _nivel, ini, fin in secs:
        if nid not in texto[i]:
            continue
        for j in range(ini, fin):
            if re.search(PATRON_FRONTERA, texto[j]):
                b.append(j + 1)
    if b:
        return "B", lineas, sorted(set(b))

    return None, lineas, []


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
    print("--- LOS TRES NODOS DE TOQUE UNICO (ejecutados en la vuelta 30) ---")
    for nid in TOQUE_UNICO:
        d = nodos.get(nid)
        if d is None:
            print("%-30s AUSENTE" % nid)
            continue
        print("%-30s pasos %3d  vivo %s  fuente: %s" % (
            nid, len(d.get("pasos_accionables") or []), vivo(d), d.get("fuente")))

    print()
    print("--- FRONTERAS PUBLICADAS DE OP-F-04-COL (detector de DOS formas) ---")
    print("  FORMA A: el id y la particion en la MISMA linea (la tipica del grupo)")
    print("  FORMA B: el id en un ENCABEZADO y la particion en el cuerpo de esa")
    print("           subseccion (la que P.20 estreno con viral_loop_marketing)")
    print()
    texto = open(FUENTES, encoding="utf-8").read().splitlines()
    secs = subsecciones(texto)
    col = porid["OP-F-04-COL"]["nodos"]
    con = 0
    sin = []
    for nid in sorted(col):
        forma, lineas, front = fronteras_del_nodo(nid, texto, secs)
        if forma:
            con += 1
        else:
            sin.append(nid)
        print("  %-38s lineas=%-22s FORMA: %-4s FRONTERA: %s" % (
            nid,
            (str(lineas[:6]) + ("..." if len(lineas) > 6 else "")) if lineas else "ninguna",
            forma or "NO",
            front or "NO"))
    print("CON FRONTERA PUBLICADA: %d de %d" % (con, len(col)))
    print("SIN FRONTERA: %s" % (sin or "ninguno"))

    print()
    print("=" * 78)
    print("FIN DE LA MEDICION DE %s" % etiqueta)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
