# -*- coding: utf-8 -*-
"""VUELTA 19, TAREA 2.B: instrumento de las TRES figuras que faltaban. SOLO LECTURA.

  1. SUBCONJUNTO ESTRICTO. Localiza las declaraciones y verifica cada puesto
     contra docs/INTRA_DOMINIO_VEREDICTOS.jsonl (existe, clase, nodos). Mide
     las dos cuentas que compiten: las razones que traen la etiqueta en
     mayusculas, y las instancias declaradas por escrito en el informe.
  2. LA FIRMA POSICIONAL DEL INJERTO (P.2). Reproduce con instrumento propio la
     tabla de sede (docs/plan/10_INVENTARIO.md, LAS FUENTES): nodos vivos con
     mas de un libro, y por libro los de primera o unica posicion contra los de
     segunda o posterior. Verifica los ejemplares citables contra el grafo.
  3. EL PASO DE OFICIO. Localiza los puestos cuya razon declara la figura POR SU
     NOMBRE, y mide la cota de la linea generica con DOS criterios declarados:
     el de la vuelta 18 y uno ampliado, para poder decir cuanto calla el
     primero y por que.

EL CRITERIO DE EJEMPLAR es el de la vuelta 18, CONFIRMADO por el acta de la
vuelta 18 (seccion 3, adjudicacion 1): un ejemplar es una instancia DECLARADA
POR ESCRITO, no cualquier par que calce con la forma.
"""
import collections
import io
import json
import sys
from pathlib import Path

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

RAIZ = Path(__file__).resolve().parents[2]
VER = RAIZ / "docs" / "INTRA_DOMINIO_VEREDICTOS.jsonl"
GRAFO = RAIZ / "dataset" / "metadata" / "master_graph.json"

# la nomina del informe, seccion 12064: de 12 ejemplares a 23, once nuevos
ONCE_NUEVOS = [1966, 1967, 2022, 2043, 2072, 2074, 2075, 2076, 2079, 2087, 2090]
# los declarados en prosa por el informe antes de esa tanda
PROSA = {511: "R30, tabla del puesto 511: NADA. Es un subconjunto estricto",
         1182: "seccion 49.4, SEGUNDO SUBCONJUNTO ESTRICTO",
         1332: "seccion 57.3, TERCER SUBCONJUNTO ESTRICTO DEL EJERCICIO",
         1573: "seccion 63.4, CINCO SUBCONJUNTOS ESTRICTOS EN UNA SOLA TANDA",
         1601: "seccion 63.4", 1776: "seccion 63.4", 1794: "seccion 63.4",
         1811: "seccion 63.4"}

# los ejemplares de P.2 citables por nodo, con su sede escrita
P2_EJEMPLARES = [
    ("five_whys_inversion_proporcional", "01_FUENTES.md, corte 1 a 5 / 6 a 9", "SPIN Selling"),
    ("voz_del_cliente_voc", "01_FUENTES.md, corte 1 a 5 / 6 a 10", "Never Lose a Customer Again"),
    ("background_startup_vs_corporativo", "01_FUENTES.md, corte 1 a 4 / 5 a 9", "Hard Thing About Hard Thing"),
    ("enfoque_motor_unico_crecimiento", "01_FUENTES.md, corte 1 a 4 / 5 a 9", "Traction"),
    ("viral_loop_marketing", "01_FUENTES.md, LOS TRES CASOS QUE NO SON UN SIMPLE APENDICE", None),
    ("coeficiente_viral", "01_FUENTES.md, LOS TRES CASOS", None),
    ("decision_de_vender_startup", "01_FUENTES.md, LOS TRES CASOS", None),
    ("future_scenarios_planning", "01_FUENTES.md, OP-F-02 LA TANDA DE MOLLICK", "Co-Intelligence"),
    ("gut_check", "01_FUENTES.md, OP-F-02", "Co-Intelligence"),
    ("brainstorming_divergente", "01_FUENTES.md, OP-F-02", "Co-Intelligence"),
]

CANON = [("Hugos", "Essentials of Supply Chain Man"),
         ("Coleman", "Never Lose a Customer Again"),
         ("Horowitz", "Hard Thing About Hard Thing"),
         ("Weinberg", "Traction"),
         ("Rackham", "SPIN Selling"),
         ("Mollick", "Co-Intelligence")]
CUATRO = ["Coleman", "Horowitz", "Weinberg", "Rackham"]

PISTAS_V18 = ["oficina de comercio exterior", "comercio exterior", "us commercial service",
              "servicio comercial", "district export council", "distrito de exportacion",
              "consulta con la oficina", "oficina que lo administra"]
PISTAS_ANCHA = ["comercio exterior", "commercial service", "servicio comercial",
                "district export council", "distrito de exportacion", "consejo de distrito"]


def cargar_jsonl(ruta):
    filas = []
    with open(ruta, encoding="utf-8") as fh:
        for linea in fh:
            linea = linea.strip()
            if linea:
                filas.append(json.loads(linea))
    return filas


def titulo(t):
    print()
    print("=" * 98)
    print(t)
    print("=" * 98)


def main():
    V = cargar_jsonl(VER)
    por_puesto = {v["puesto_intra"]: v for v in V}
    grafo = json.load(open(GRAFO, encoding="utf-8"))
    nodos = grafo["nodos"]
    vivos = {k: x for k, x in nodos.items() if not x.get("deprecado")}

    # ------------------------------------------------------------------ 1
    titulo("1. SUBCONJUNTO ESTRICTO: localizar las declaraciones y verificarlas")
    etiqueta = sorted(v["puesto_intra"] for v in V
                      if "SUBCONJUNTO ESTRICTO" in (v.get("razon") or ""))
    minus = sorted(v["puesto_intra"] for v in V
                   if "subconjunto" in (v.get("razon") or "").lower())
    print("  razones con la etiqueta SUBCONJUNTO ESTRICTO en mayusculas: %d" % len(etiqueta))
    print("    %s" % etiqueta)
    print("  razones que solo nombran la palabra subconjunto: %d  %s" % (len(minus), minus))
    print()
    print("  VERIFICACION uno por uno contra el archivo:")
    fallos = 0
    for p in etiqueta:
        v = por_puesto.get(p)
        ok = v is not None and v["clase"] == "A"
        if not ok:
            fallos += 1
        print("    %-6s %-5d %s %-16s %s vs %s" % (
            "OK" if ok else "FALLA", p, v["clase"], v["dominio"], v["nodo_a"], v["nodo_b"]))
    print("  verificados %d, fallos %d" % (len(etiqueta), fallos))
    print()
    print("  LA ARITMETICA DEL INFORME (seccion 12064: de 12 a 23, once nuevos):")
    previos = [p for p in etiqueta if p < min(ONCE_NUEVOS)]
    print("    con la etiqueta y anteriores al tramo: %d  %s" % (len(previos), previos))
    print("    los once nuevos que el informe nombra:  %d  %s" % (len(ONCE_NUEVOS), ONCE_NUEVOS))
    print("    los once estan todos con la etiqueta: %s" % all(p in etiqueta for p in ONCE_NUEVOS))
    print("    suma: %d mas %d = %d" % (len(previos), len(ONCE_NUEVOS),
                                        len(previos) + len(ONCE_NUEVOS)))
    print()
    print("  LO QUE NO CALZA, y se declara sin tocar la cifra:")
    for p in sorted(PROSA):
        print("    puesto %-5d etiqueta en su razon: %-5s  declarado en prosa: %s" % (
            p, p in etiqueta, PROSA[p]))
    fuera = sorted(set(PROSA) - set(etiqueta))
    print("    declarados en prosa y SIN la etiqueta: %s" % fuera)
    print("    total de instancias declaradas por escrito (etiqueta mas prosa): %d" % (
        len(set(etiqueta) | set(PROSA))))

    # ------------------------------------------------------------------ 2
    titulo("2. LA FIRMA POSICIONAL DEL INJERTO (P.2): reproducir la tabla de sede")
    multi = {k for k, x in vivos.items() if " | " in x["fuente"]}
    print("  nodos vivos en el grafo: %d" % len(vivos))
    print("  nodos vivos con MAS DE UN LIBRO en su campo fuente: %d" % len(multi))
    seg = collections.defaultdict(set)
    pri = collections.defaultdict(set)
    for k, x in vivos.items():
        partes = [p.strip() for p in x["fuente"].split(" | ")]
        for nombre, pat in CANON:
            if any(pat in p for p in partes[1:]):
                seg[nombre].add(k)
            if pat in partes[0]:
                pri[nombre].add(k)
    print()
    print("  %-10s %10s %12s" % ("libro", "1a o unica", "2a o posterior"))
    total_seg = 0
    for nombre, _ in CANON:
        print("  %-10s %10d %12d" % (nombre, len(pri[nombre]), len(seg[nombre])))
        total_seg += len(seg[nombre])
    print("  suma de la columna 2a o posterior: %d" % total_seg)
    union = set().union(*seg.values())
    print("  nodos DISTINTOS que la componen: %d  (solape %d)" % (
        len(union), total_seg - len(union)))
    solape = sorted(k for k in union if sum(1 for nb, _ in CANON if k in seg[nb]) > 1)
    print("  los nodos que declaran DOS de los seis en 2a o posterior: %s" % solape)
    print("  cuadra con los nodos de mas de un libro: %s" % (union == multi))
    print()
    cuatro_union = set().union(*[seg[b] for b in CUATRO])
    print("  LA TANDA DE LOS CUATRO LIBROS (Coleman, Horowitz, Weinberg, Rackham):")
    print("    por libro: %s" % {b: len(seg[b]) for b in CUATRO})
    print("    suma por libro: %d" % sum(len(seg[b]) for b in CUATRO))
    print("    NODOS DISTINTOS: %d" % len(cuatro_union))
    print("    el doc de sede publica 43 NODOS DISTINTOS y grupos 15/13/13/4")
    print()
    print("  LOS EJEMPLARES CITABLES, verificados contra el grafo:")
    for nid, sede, libro in P2_EJEMPLARES:
        x = vivos.get(nid)
        if x is None:
            print("    FALLA  %-42s NO ES NODO VIVO" % nid)
            continue
        partes = [p.strip() for p in x["fuente"].split(" | ")]
        segundo = len(partes) > 1
        bien = segundo and (libro is None or any(libro in p for p in partes[1:]))
        print("    %-6s %-42s libros %d  pasos %2d  %s" % (
            "OK" if bien else "FALLA", nid, len(partes),
            len(x.get("pasos_accionables") or []), partes[0][:38]))

    # ------------------------------------------------------------------ 3
    titulo("3. EL PASO DE OFICIO: los declarados por su nombre, y las dos cotas")
    decl = sorted(v["puesto_intra"] for v in V
                  if "paso de oficio" in (v.get("razon") or "").lower())
    print("  puestos cuya razon declara la figura POR SU NOMBRE: %d  %s" % (len(decl), decl))
    for p in decl:
        v = por_puesto[p]
        print("    %-5d %s %-14s %s vs %s" % (
            p, v["clase"], v["dominio"], v["nodo_a"], v["nodo_b"]))
    md = [v["puesto_intra"] for v in V if "media docena" in (v.get("razon") or "").lower()]
    print("  el puesto que trae la frase media docena: %s" % md)

    exp_vivos = {k: x for k, x in vivos.items() if x.get("dominio") == "exportacion"}
    pares_exp = [v for v in V if v["dominio"] == "exportacion"]

    def cota(pistas):
        con = {}
        for nid, x in exp_vivos.items():
            m = [i for i, p in enumerate(x.get("pasos_accionables") or [], 1)
                 if any(pi in p.lower() for pi in pistas)]
            if m:
                con[nid] = m
        return con

    a = cota(PISTAS_V18)
    b = cota(PISTAS_ANCHA)
    print()
    print("  nodos VIVOS del dominio exportacion: %d, pares leidos: %d" % (
        len(exp_vivos), len(pares_exp)))
    for etq, con in (("criterio de la vuelta 18", a), ("criterio ampliado", b)):
        p1 = sorted(k for k, m in con.items() if 1 in m)
        toc = [v for v in pares_exp if v["nodo_a"] in con or v["nodo_b"] in con]
        print("  %-26s nodos %3d   con la linea en PASO 1 %2d   pares tocados %3d" % (
            etq, len(con), len(p1), len(toc)))
    print()
    print("  LOS SEIS DEL CRITERIO DE LA VUELTA 18, verificados contra el grafo:")
    for nid in sorted(a):
        print("    %-52s pasos %-8s vivo, deprecado %s" % (
            nid, a[nid], bool(nodos[nid].get("deprecado"))))
    print("  LOS DIEZ PARES que tocan a esos seis:")
    for v in sorted([x for x in pares_exp if x["nodo_a"] in a or x["nodo_b"] in a],
                    key=lambda x: x["puesto_intra"]):
        print("    %-5d %s  %s vs %s" % (
            v["puesto_intra"], v["clase"], v["nodo_a"], v["nodo_b"]))
    print()
    print("  LO QUE EL CRITERIO DE LA VUELTA 18 CALLA, y por que:")
    nuevos = sorted(set(b) - set(a))
    print("    nodos que aparecen solo con el criterio ampliado: %d" % len(nuevos))
    for nid in nuevos:
        i = b[nid][0]
        print("    %-52s paso %d: %s" % (nid, i,
                                         exp_vivos[nid]["pasos_accionables"][i - 1][:78]))
    print("    LA CAUSA: la lista de la vuelta 18 trae us commercial service sin puntos,")
    print("    y el grafo escribe U.S. Commercial Service. La cadena no casa nunca.")
    print()
    print("  LOS TRES DECLARADOS, contra las dos cotas:")
    for p in decl:
        v = por_puesto[p]
        for lado in (v["nodo_a"], v["nodo_b"]):
            print("    %-5d  %-52s v18 %-5s ampliado %-5s" % (
                p, lado, lado in a, lado in b))
    return 0


if __name__ == "__main__":
    sys.exit(main())
