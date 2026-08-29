# -*- coding: utf-8 -*-
"""vuelta132_prefijo_sobre_recortada.py . TAREA 3.d de la vuelta 132.
PREGUNTA ABIERTA, NO ORDEN: se MIDE y NO SE APLICA (lo adjudica el
fundador en el acta 132).

Si ademas de la igualdad EXACTA de la forma recortada por localizador
(3.a) se admitiera tambien PREFIJO ESTRICTO sobre esa forma recortada
(guarda de longitud >=20 caracteres para el mas corto de los dos, igual
que la guarda de la regla de TITULO de la 131, para no fundir por una
coincidencia corta), CUANTOS GRUPOS resultarian y CUALES colapsos nuevos
se ganarian sobre los 106 de 3.a.

EJEMPLO QUE EL PROPIO ENCARGO NOMBRA: la familia 'Diana L. Lindstrom,
Procurement Project Management Success' (grupo sintetico de 3.a/3.b, tres
miembros con cola de capitulo) se fundiria con 'Diana L. Lindstrom,
Procurement Project Management Success (J. Ross, 2014)' (grafia sin cola,
recorte = si misma), porque la recortada del primero es PREFIJO ESTRICTO
de la recortada del segundo.

Salida: docs/loop/SALIDA_V132_3D_PREFIJO_SOBRE_RECORTADA.txt

Uso:
  python scripts/loop/vuelta132_prefijo_sobre_recortada.py
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from vuelta131_grupos_por_titulo import (  # noqa: E402
    cargar_censo,
    prefijo_cadena_entera_une,
    prefijo_titulo_une,
    UnionFind,
)
from vuelta132_grupos_por_localizador import recortar_localizador  # noqa: E402

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SALIDA = os.path.join(RAIZ, "docs", "loop", "SALIDA_V132_3D_PREFIJO_SOBRE_RECORTADA.txt")

GUARDA_LONGITUD = 20


def calcular_base():
    """Reproduce exactamente los 106 grupos de 3.a (R1 cadena entera + R2
    titulo + R3 localizador, igualdad exacta)."""
    censo = cargar_censo()
    grafias = sorted(censo.keys())
    uf = UnionFind(grafias)
    for a in grafias:
        for b in grafias:
            if prefijo_cadena_entera_une(a, b):
                uf.une(a, b)
    for a in grafias:
        for b in grafias:
            if prefijo_titulo_une(a, b):
                uf.une(a, b)
    buck = {}
    for g in grafias:
        buck.setdefault(recortar_localizador(g), []).append(g)
    for _, miembros in buck.items():
        base = miembros[0]
        for m in miembros[1:]:
            uf.une(base, m)
    return censo, grafias, uf


def main():
    sys.stdout.reconfigure(encoding="utf-8")

    censo, grafias, uf = calcular_base()
    grupos_base = {}
    for g in grafias:
        grupos_base.setdefault(uf.find(g), []).append(g)
    n_base = len(grupos_base)

    recortada_de_raiz = {r: recortar_localizador(max(m, key=len)) for r, m in grupos_base.items()}

    raices = sorted(grupos_base.keys())
    pares_nuevos = []
    for ra in raices:
        for rb in raices:
            if ra >= rb:
                continue
            ca, cb = recortada_de_raiz[ra], recortada_de_raiz[rb]
            if ca == cb:
                continue
            corto, largo = (ca, cb) if len(ca) <= len(cb) else (cb, ca)
            if len(corto) < GUARDA_LONGITUD:
                continue
            if largo.startswith(corto):
                pares_nuevos.append((ra, rb))

    uf2 = UnionFind(raices)
    for ra, rb in pares_nuevos:
        uf2.une(ra, rb)
    n_final = len({uf2.find(r) for r in raices})

    colapsos = {}
    for ra, rb in pares_nuevos:
        colapsos.setdefault(uf2.find(ra), set()).update([ra, rb])
    fusiones = [v for v in colapsos.values() if len(v) > 1]

    with open(SALIDA, "w", encoding="utf-8") as fh:
        fh.write("MEDIDO, NO APLICADO (pregunta abierta 3.d, la adjudica el fundador en el acta 132).\n")
        fh.write("Guarda de longitud: recortada mas corta >= %d caracteres.\n\n" % GUARDA_LONGITUD)
        fh.write("GRUPOS BASE (3.a, R1+R2+R3 igualdad exacta): %d\n" % n_base)
        fh.write("GRUPOS SI ADEMAS SE ADMITIERA PREFIJO SOBRE LA RECORTADA: %d\n" % n_final)
        fh.write("COLAPSOS NUEVOS: %d\n\n" % (n_base - n_final))
        fh.write("TODOS LOS COLAPSOS NUEVOS, UNO POR UNO, CON SUS MIEMBROS:\n")
        for fusion in sorted(fusiones, key=lambda f: -sum(len(grupos_base[r]) for r in f)):
            raices_fusion = sorted(fusion, key=lambda r: -len(grupos_base[r]))
            fh.write("  FUSION (%d grupos base, %d grafias):\n" % (
                len(raices_fusion), sum(len(grupos_base[r]) for r in raices_fusion)))
            for r in raices_fusion:
                fh.write("    recortada=%r\n" % recortada_de_raiz[r])
                for m in sorted(grupos_base[r], key=len):
                    fh.write("      %d\t%s\n" % (censo[m], m))
        fh.write("\nTOTAL grupos base: %d\n" % n_base)
        fh.write("TOTAL grupos con prefijo sobre recortada: %d\n" % n_final)
        fh.write("TOTAL fusiones nuevas: %d\n" % len(fusiones))

    print("MEDIDO, NO APLICADO.")
    print("grupos base (3.a): %d" % n_base)
    print("grupos con prefijo sobre recortada: %d" % n_final)
    print("colapsos nuevos: %d" % (n_base - n_final))
    print("fusiones nuevas listadas: %d" % len(fusiones))
    print("EXITCODE: 0")


if __name__ == "__main__":
    raise SystemExit(main())
