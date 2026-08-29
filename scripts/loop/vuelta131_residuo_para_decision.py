# -*- coding: utf-8 -*-
"""vuelta131_residuo_para_decision.py . TAREA 3.d de la vuelta 131: lo
que las TRES reglas mecanicas (cadena entera, titulo, localizador) dejan
SIN COLAPSAR, es decir los grupos de UNA sola grafia (94 de los 108
grupos de esta vuelta). MIDE Y LISTA, NO DECIDE: la decision es del
auditor.

DETECTOR MECANICO DE TRUNCAMIENTO, el mismo que documenta
`docs/PENDIENTES.md` (ficha `campos-sucios-dataset`) y que la vuelta 130
midio en el acta (4.5): el recorte de importacion corta EL TITULO A 31
CARACTERES EXACTOS y el sufijo " - Autor" queda DETRAS del corte. Una
grafia residual se marca TRUNCADA cuando `len(titulo) == 31` Y el RESTO
(autor) no esta vacio; sin el segundo requisito el detector fichaba
`Guia de empaque para transporte` (31 caracteres exactos, SIN autor, un
titulo completo por coincidencia de longitud, no un corte a mitad de
palabra) como falso positivo.

DOS BOLSAS PARA LAS GRAFIAS TRUNCADAS residuales (y solo para esas):
  BOLSA 1, RECONSTRUIBLE: existe en el censo de 129 grafias OTRA grafia,
  sin truncar, del mismo libro, que las tres reglas no unieron.
  BOLSA 2, FORASTERA: no existe tal contraparte en el censo; el titulo
  completo NO se puede reconstruir desde el dataset.
Las grafias residuales que NO son truncadas (la inmensa mayoria: citas
por capitulo del mismo libro que SI anaden informacion, titulos unicos,
codigos de documento) no entran en ninguna bolsa.

Salida: docs/loop/SALIDA_V131_3D_RESIDUO_PARA_DECISION.txt

Uso:
  python scripts/loop/vuelta131_residuo_para_decision.py
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from vuelta131_grupos_por_titulo import (  # noqa: E402
    cargar_censo,
    prefijo_cadena_entera_une,
    prefijo_titulo_une,
    titulo_de,
    resto_de,
    UnionFind,
)

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SALIDA = os.path.join(RAIZ, "docs", "loop", "SALIDA_V131_3D_RESIDUO_PARA_DECISION.txt")


def calcular_singletons():
    censo = cargar_censo()
    grafias = sorted(censo.keys())
    uf = UnionFind(grafias)
    for a in grafias:
        for b in grafias:
            if prefijo_cadena_entera_une(a, b):
                uf.une(a, b)
            if prefijo_titulo_une(a, b):
                uf.une(a, b)
    grupos = {}
    for g in grafias:
        grupos.setdefault(uf.find(g), []).append(g)
    singles = [m[0] for r, m in grupos.items() if len(m) == 1]
    return censo, grafias, singles


def es_truncada(g):
    return len(titulo_de(g)) == 31 and bool(resto_de(g))


def tiene_contraparte(g, todas_las_grafias):
    """Contraparte = otra grafia del censo cuyo titulo (>=20 chars) es
    prefijo estricto del titulo truncado de 31 caracteres de g, o
    viceversa (misma prueba de la regla de titulo, sin la guarda de
    RESTO: aqui buscamos evidencia de la MISMA obra, autor aparte)."""
    tg = titulo_de(g)
    for otro in todas_las_grafias:
        if otro == g:
            continue
        to = titulo_de(otro)
        if to == tg:
            continue
        if to.startswith(tg) and len(tg) >= 20:
            return otro
    return None


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    censo, grafias, singles = calcular_singletons()

    truncadas = [g for g in singles if es_truncada(g)]
    bolsa1, bolsa2 = [], []
    for g in truncadas:
        contraparte = tiene_contraparte(g, grafias)
        if contraparte:
            bolsa1.append((g, contraparte))
        else:
            bolsa2.append(g)

    residuo_ordenado = sorted(singles, key=lambda g: (-censo[g], g))

    with open(SALIDA, "w", encoding="utf-8") as fh:
        fh.write("RESIDUO: %d grupos de UNA sola grafia sobre %d grafias del censo, ordenado de mayor a menor recuento de nodos.\n\n" % (len(singles), len(grafias)))
        for g in residuo_ordenado:
            marca = " [TRUNCADA]" if g in truncadas else ""
            fh.write("%d\t%s%s\n" % (censo[g], g, marca))

        fh.write("\nBOLSA 1, RECONSTRUIBLE (%d): la grafia truncada TIENE en el catalogo una contraparte sin truncar que las reglas no unieron.\n" % len(bolsa1))
        for g, contraparte in sorted(bolsa1, key=lambda t: -censo[t[0]]):
            fh.write("  %d\t%s\n    contraparte: %s\n" % (censo[g], g, contraparte))
        if not bolsa1:
            fh.write("  (vacia esta vuelta: ninguna truncada residual tiene contraparte sin truncar en el censo)\n")

        fh.write("\nBOLSA 2, FORASTERA (%d): la grafia truncada NO tiene contraparte en el catalogo, titulo completo no reconstruible desde el dataset.\n" % len(bolsa2))
        for g in sorted(bolsa2, key=lambda g: -censo[g]):
            fh.write("  %d\t%s\n" % (censo[g], g))

    print("residuo (grupos de 1 grafia): %d" % len(singles))
    print("truncadas (len(titulo)=31 y resto no vacio): %d" % len(truncadas))
    print("BOLSA 1 reconstruible: %d" % len(bolsa1))
    print("BOLSA 2 forastera: %d" % len(bolsa2))
    for g in bolsa2:
        print("  forastera: %d\t%s" % (censo[g], g))
    print("EXITCODE: 0")


if __name__ == "__main__":
    raise SystemExit(main())
