# -*- coding: utf-8 -*-
"""vuelta144_1c_medir_opm04.py . ARNES PROPIO DEL EJECUTOR, vuelta 144.

Mide, CON INSTRUMENTO PROPIO Y CERO ESCRITURAS, lo que la CORRECCION 20 deja
escrito (adjudicacion 3.9 del acta de la vuelta 143):

  (a) `depende_de` de OP-M-04 esta VACIO: no espera a nadie;
  (b) OP-S-12 y OP-U-01 estan en su `bloquea_a`, o sea que OP-M-04 LAS BLOQUEA,
      no depende de ellas; y ninguna de las dos es de la fase 06;
  (c) sus cuatro nodos siguen VIVOS y SIN FUNDIR en el grafo de hoy;
  (d) la rama `es_mesa` de medir() NUNCA mira `nodos`, `eliminar`,
      `superviviente` ni `aristas_nuevas` de la propia ficha: se comprueba
      leyendo el CODIGO FUENTE del tramo, no de memoria;
  (e) que celda saca hoy la vara para OP-M-04.
"""
import ast
import inspect
import io
import json
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(RAIZ, "scripts", "loop"))
import tallar_estado_de_fase as T  # noqa: E402

OPS = os.path.join(RAIZ, "docs", "plan", "OPERACIONES.jsonl")
CAMPOS_PROPIOS = ["nodos", "eliminar", "superviviente", "aristas_nuevas", "preservar"]


def fichas():
    d = {}
    for l in io.open(OPS, encoding="utf-8"):
        l = l.strip()
        if l:
            o = json.loads(l)
            d[o["id_op"]] = o
    return d


def main():
    F = fichas()
    op = F.get("OP-M-04")
    if op is None:
        raise SystemExit("ROJO: no esta OP-M-04")

    print("(a) depende_de de OP-M-04: %r -- %s"
          % (op.get("depende_de"), "VACIO, no espera a nadie"
             if not (op.get("depende_de") or []) else "NO ESTA VACIO"))
    print("")

    bloq = op.get("bloquea_a") or []
    print("(b) bloquea_a de OP-M-04: %r" % bloq)
    for h in bloq:
        f = F.get(h)
        print("      %s -- existe=%s, fase=%s, su depende_de=%r"
              % (h, f is not None, (f or {}).get("fase"), (f or {}).get("depende_de")))
    print("    OP-M-04 esta en depende_de de alguna: %s"
          % [h for h in bloq if "OP-M-04" in ((F.get(h) or {}).get("depende_de") or [])])
    print("    NINGUNA de las dos es de la fase 06: %s"
          % all((F.get(h) or {}).get("fase") != "06_MESAS" for h in bloq))
    print("")

    nodos = T.cargar_grafo("WORK")
    resolver = T.resolver_de(nodos)
    print("(c) LOS CUATRO NODOS DE OP-M-04, en el grafo de hoy:")
    vivos = sinfundir = 0
    for nid in op.get("nodos") or []:
        n = nodos.get(nid)
        existe = n is not None
        depre = bool((n or {}).get("deprecado"))
        r = resolver(nid)
        if existe and not depre:
            vivos += 1
        if r == nid:
            sinfundir += 1
        print("      %-32s existe=%-5s deprecado=%-5s resuelve_a=%s"
              % (nid, existe, depre, r))
    print("    VIVOS: %d de %d | SIN FUNDIR (resuelven a si mismos): %d de %d"
          % (vivos, len(op.get("nodos") or []), sinfundir, len(op.get("nodos") or [])))
    print("")

    # (d) EL CODIGO, LEIDO DEL FUENTE. Se recorta el tramo de la rama es_mesa
    #     dentro de medir() y se buscan en el las cadenas de los campos propios.
    fuente = inspect.getsource(T.medir)
    arbol = ast.parse(fuente.lstrip())
    # El segundo `for x in catalogo` del cuerpo es el bucle de las mesas.
    bucles = [n for n in arbol.body[0].body if isinstance(n, ast.For)]
    tramo_mesa = bucles[1]
    literales = set()
    for n in ast.walk(tramo_mesa):
        if isinstance(n, ast.Constant) and isinstance(n.value, str):
            literales.add(n.value)
    print("(d) LA RAMA es_mesa DE medir(), leida del fuente (%d nodos AST):" % len(list(ast.walk(tramo_mesa))))
    for c in CAMPOS_PROPIOS:
        usa = c in literales
        print("      lee el campo propio %-16s de la ficha: %s" % ("`%s`" % c, "SI" if usa else "NO"))
    print("    CAMPOS DE LA FICHA QUE SI LEE: %s"
          % sorted(x for x in literales if x in ("bloquea_a", "fase", "estado", "tipo", "id_op", "a")))
    print("")

    # (e) LA CELDA DE HOY.
    ops = T.cargar_ops("WORK")
    filas, cifra, fallos = T.medir("06_MESAS", ops, nodos)
    for f in filas:
        if f["id_op"] == "OP-M-04":
            print("(e) LA CELDA DE HOY para OP-M-04:")
            print("      vara      : %s" % f["vara"])
            print("      cumplido  : %r" % f["cumplido"])
            print("      razon     : %s" % f["razon"])
    print("    SIN VARA ESCRITA hoy: %s" % cifra.get("nombres_sin_vara"))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
