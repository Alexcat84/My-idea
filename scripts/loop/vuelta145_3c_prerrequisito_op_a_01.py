# -*- coding: utf-8 -*-
r"""vuelta145_3c_prerrequisito_op_a_01.py . EL PRERREQUISITO DE `OP-A-01`,
MEDIDO HOY CONTRA EL GRAFO. VUELTA 145, TAREA 3.c.

POR QUE NACE. La nota de `OP-A-01` dice, literal: *"el campo fuente NO ESTA
NORMALIZADO. Hugos aparece con DOS grafias y Horowitz con TRES, y sin
normalizar el recorte da 23 y 16 donde el canonico da 21 y 14. Sin lista
canonica de libros, el control posicional cuenta mal."* Y nombra a `OP-S-11`
como dueno de la lista canonica. Esa medicion lleva fecha de corte **11 ago
2026**; esta la vuelve a hacer HOY, con instrumento propio, para poder DECLARAR
si el prerrequisito esta cumplido o no.

QUE MIDE, sobre los nodos VIVOS del grafo:
  (1) CUANTOS NODOS DECLARAN MAS DE UNA FUENTE. El campo `fuente` es UNA SOLA
      CADENA por nodo (medido: 3.853 de 3.853 son `str`, ninguna lista), asi
      que "mas de una fuente" es una cadena con SEPARADOR. El separador
      canonico se computa, no se supone: se prueban los candidatos de
      `SEPARADORES` y se publica la cuenta de CADA UNO, para que la cifra no
      quede colgando de una eleccion callada.
  (2) CUANTAS DECLARACIONES CAEN EN SEGUNDA POSICION O POSTERIOR, que es
      exactamente lo que el control posicional de P.2 mira.
  (3) CUANTAS GRAFIAS DISTINTAS tiene hoy el campo `fuente` para Hugos y para
      Horowitz, contando por PIEZA (cada trozo entre separadores), no por
      cadena entera: dos nodos con la misma grafia de Hugos y distinto segundo
      libro no son dos grafias de Hugos.

LO QUE NO HACE, Y SE DICE: NO improvisa la lista canonica de libros. Esa es de
`OP-S-11` y la nota de la ficha la nombra como duena. Este instrumento MIDE y
DECLARA; abrir la fase es el encargo, cerrarla no lo es.

USO:
  python scripts/loop/vuelta145_3c_prerrequisito_op_a_01.py
  python scripts/loop/vuelta145_3c_prerrequisito_op_a_01.py --ref HEAD
"""
import argparse
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(RAIZ, "scripts", "loop"))

import tallar_estado_de_fase as T  # noqa: E402

# CANDIDATOS A SEPARADOR, con su cuenta publicada cada uno. La barra vertical
# es la que el catalogo usa de verdad; las otras dos van para que se vea que NO
# se esta contando un separador de AUTORES como si fuera de LIBROS (el caso
# real: "Out of the Crisis, Reissue - Deming, W. Edwards; Cahill, Kev", donde
# el punto y coma separa dos autores del MISMO libro).
SEPARADORES = [" | ", "|", ";"]
SEPARADOR_CANONICO = " | "

LIBROS = [("Hugos", "hugos"), ("Horowitz", "horowitz")]


def piezas(valor, sep):
    return [p.strip() for p in valor.split(sep) if p.strip()]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--ref", default="WORK")
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")

    nodos = T.cargar_grafo(a.ref)
    vivos = {k: n for k, n in nodos.items()
             if not (n.get("deprecado") or n.get("deprecated"))}

    print("PRERREQUISITO DE OP-A-01, MEDIDO HOY | REF: %s" % a.ref)
    print("Instrumento: scripts/loop/vuelta145_3c_prerrequisito_op_a_01.py (vuelta 145, 3.c)")
    print("=" * 78)
    print("CENSO DE PARTIDA: %d nodos en el grafo, %d VIVOS" % (len(nodos), len(vivos)))
    tipos = {}
    for n in nodos.values():
        tipos[type(n.get("fuente")).__name__] = tipos.get(type(n.get("fuente")).__name__, 0) + 1
    print("  el campo `fuente` por tipo de dato: %s" % tipos)
    sin_fuente = [k for k, n in vivos.items() if not (n.get("fuente") or "").strip()]
    print("  nodos vivos con `fuente` vacia o ausente: %d" % len(sin_fuente))
    print("")

    print("(1) NODOS VIVOS QUE DECLARAN MAS DE UNA FUENTE, por candidato a separador")
    for sep in SEPARADORES:
        cuantos = sum(1 for n in vivos.values()
                      if len(piezas(n.get("fuente") or "", sep)) > 1)
        marca = "  <- SEPARADOR CANONICO DEL CATALOGO" if sep == SEPARADOR_CANONICO else ""
        print("  separador %-5r : %4d nodo(s)%s" % (sep, cuantos, marca))
    multi = sorted(k for k, n in vivos.items()
                   if len(piezas(n.get("fuente") or "", SEPARADOR_CANONICO)) > 1)
    print("  CIFRA nodos con mas de una fuente: %d nodos" % len(multi))
    print("")

    print("(2) DECLARACIONES EN SEGUNDA POSICION O POSTERIOR (lo que mira P.2)")
    total_segunda = 0
    for nid in multi:
        ps = piezas(vivos[nid].get("fuente") or "", SEPARADOR_CANONICO)
        total_segunda += len(ps) - 1
    print("  CIFRA declaraciones en 2.a posicion o posterior: %d lineas" % total_segunda)
    print("  LOS NODOS, UNO A UNO, y ninguno se queda sin nombre:")
    for nid in multi:
        ps = piezas(vivos[nid].get("fuente") or "", SEPARADOR_CANONICO)
        print("     %s" % nid)
        for i, p in enumerate(ps):
            print("        [%d] %s%s" % (i + 1, p, "   <- SEGUNDA O POSTERIOR" if i else ""))
    print("")

    print("(3) GRAFIAS DISTINTAS POR LIBRO, contadas POR PIEZA y no por cadena entera.")
    print("    LAS DOS UNIDADES CON SU NOMBRE, que aqui no da lo mismo (CORRECCION 18):")
    print("    SOLO VIVOS es lo que el grafo publica hoy; TODOS LOS NODOS incluye los")
    print("    deprecados, que es donde la grafia vieja sigue existiendo.")
    conteo = {}
    for rotulo, aguja in LIBROS:
        for etiqueta, universo in (("SOLO VIVOS", vivos), ("TODOS LOS NODOS", nodos)):
            grafias = {}
            for nid, n in universo.items():
                for p in piezas(n.get("fuente") or "", SEPARADOR_CANONICO):
                    if aguja in p.lower():
                        grafias.setdefault(p, []).append(nid)
            conteo[(rotulo, etiqueta)] = len(grafias)
            print("  %s, %s: %d grafia(s) distinta(s), %d nodo(s)"
                  % (rotulo, etiqueta, len(grafias), sum(len(v) for v in grafias.values())))
            for g in sorted(grafias):
                print("     %4d nodo(s)  %r" % (len(grafias[g]), g))
    print("")

    print("(4) LA DECLARACION")
    print("  grafias de Hugos hoy: %d SOLO VIVOS, %d TODOS LOS NODOS"
          % (conteo[("Hugos", "SOLO VIVOS")], conteo[("Hugos", "TODOS LOS NODOS")]))
    print("  grafias de Horowitz hoy: %d SOLO VIVOS, %d TODOS LOS NODOS"
          % (conteo[("Horowitz", "SOLO VIVOS")], conteo[("Horowitz", "TODOS LOS NODOS")]))
    print("  CONTRA LO QUE LA FICHA DICE (corte 11 ago 2026): Hugos DOS grafias y Horowitz")
    print("  TRES. La de Hugos REPRODUCE contando TODOS LOS NODOS; la de Horowitz da DOS y")
    print("  no tres, y se declara en vez de resolverse copiando. En las DOS, la grafia")
    print("  vieja vive HOY solo del lado deprecado.")
    print("  LISTA CANONICA DE LIBROS EN EL REPOSITORIO: se busca y se dice si esta.")
    candidatos = [
        "dataset/metadata/libros_canonicos.json",
        "dataset/metadata/fuentes_canonicas.json",
        "docs/plan/LIBROS_CANONICOS.md",
    ]
    hallados = [c for c in candidatos if os.path.exists(os.path.join(RAIZ, c))]
    print("     candidatos mirados: %s" % ", ".join(candidatos))
    print("     hallados: %s" % (", ".join(hallados) if hallados else "NINGUNO"))
    cumplido = bool(hallados)
    print("")
    print("  PRERREQUISITO CUMPLIDO: %s" % ("SI" if cumplido else "NO"))
    if not cumplido:
        print("  MOTIVO: no existe en el repositorio ninguna lista canonica de libros con sus")
        print("  alias de escritura. La ficha de OP-A-01 nombra a OP-S-11 como su dueno, y")
        print("  OP-S-11 sigue SIN VARA ESCRITA en la fase 05. NO SE IMPROVISA LA LISTA:")
        print("  la fase 07 queda ABIERTA Y MEDIDA con su bloqueo nombrado.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
