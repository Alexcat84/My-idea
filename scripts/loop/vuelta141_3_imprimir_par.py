# -*- coding: utf-8 -*-
r"""vuelta141_3_imprimir_par.py . LOS DOS NODOS DE UN PAR, ENTEROS, ANTES DE
ESCRIBIR NINGUNA LECTURA (TAREA 3.a de la vuelta 141).

POR QUE NACE. La TAREA 3 de la vuelta 141 manda releer SEIS pares que una
fusion colapso, con la vara del banco 9.22, y su guarda 3.a dice: "IMPRIME LOS
DOS NODOS ENTEROS, pasos y resumen, ANTES de escribir tu lectura, y di QUE
LINEA expande cada direccion, citando el paso por su numero EN EL NODO DE HOY y
no en la ficha del 12 ago 2026". Este instrumento imprime; NO adjudica nada.

QUE IMPRIME, por cada extremo: el id resuelto, si esta vivo, su titulo, su
resumen_teorico entero y sus pasos_accionables NUMERADOS EN EL NODO DE HOY,
empezando en 1. Y luego, del par: si la ida y la vuelta estan presentes hoy,
medidas con el resolutor de la casa (P.1) en LAS DOS VISTAS.

NO ESCRIBE NADA EN DISCO.

USO:
  python scripts/loop/vuelta141_3_imprimir_par.py --a sistema_gates_go_kill \
      --b gestion_portafolio_dos_niveles
"""
import argparse
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import tallar_estado_de_fase as T


def imprimir_nodo(nodos, resolver, nid):
    r = resolver(nid)
    n = nodos.get(r)
    print("=" * 78)
    print("NODO: %s" % nid)
    if r != nid:
        print("  RESUELVE POR ALIAS A: %s" % r)
    if n is None:
        print("  NO EXISTE EN EL GRAFO")
        return
    print("  vivo: %s | deprecado: %s" % (not n.get("deprecado"), bool(n.get("deprecado"))))
    print("  titulo_concepto: %s" % n.get("titulo_concepto"))
    print("  dominio: %s" % n.get("dominio"))
    print("")
    print("  resumen_teorico:")
    for linea in (n.get("resumen_teorico") or "").splitlines() or [""]:
        print("    %s" % linea)
    print("")
    pasos = n.get("pasos_accionables") or []
    print("  pasos_accionables (%d), NUMERADOS EN EL NODO DE HOY:" % len(pasos))
    for i, p in enumerate(pasos, 1):
        if isinstance(p, dict):
            p = p.get("texto") or p.get("paso") or str(p)
        print("    paso %d: %s" % (i, p))
    print("")
    print("  nodos_siguientes (%d): %s" % (len(n.get("nodos_siguientes") or []),
                                           ", ".join(n.get("nodos_siguientes") or [])))
    print("  nodos_previos (%d): %s" % (len(n.get("nodos_previos") or []),
                                        ", ".join(n.get("nodos_previos") or [])))
    print("")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--a", required=True)
    ap.add_argument("--b", required=True)
    ap.add_argument("--ref", default="WORK")
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")

    nodos = T.cargar_grafo(a.ref)
    resolver = T.resolver_de(nodos)
    imprimir_nodo(nodos, resolver, a.a)
    imprimir_nodo(nodos, resolver, a.b)

    ra, rb = resolver(a.a), resolver(a.b)
    ida, _, _ = T.arista_presente(nodos, resolver, ra, rb)
    vuelta, _, _ = T.arista_presente(nodos, resolver, rb, ra)
    print("=" * 78)
    print("EL PAR, MEDIDO HOY CON EL RESOLUTOR PUESTO EN LAS DOS VISTAS | REF: %s" % a.ref)
    print("  %s -> %s : %s" % (ra, rb, "PRESENTE" if ida else "no presente"))
    print("  %s -> %s : %s" % (rb, ra, "PRESENTE" if vuelta else "no presente"))
    print("  grado total de los dos nodos (aristas unicas de sus dos listas, resueltas):")
    for x in (ra, rb):
        n = nodos.get(x) or {}
        sal = {resolver(y) for y in (n.get("nodos_siguientes") or [])}
        ent = {resolver(y) for y in (n.get("nodos_previos") or [])}
        print("    %s: %d salientes, %d entrantes" % (x, len(sal), len(ent)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
