# -*- coding: utf-8 -*-
"""vuelta132_bolsa2_particion.py . TAREA 3.c de la vuelta 132: parte la
BOLSA 2 (las cuatro truncadas residuales de la 131: Juran 459, Green to
Gold 209, Managing the Risks 90, Co-Intelligence 39) en dos, con el
criterio mecanico que el acta 131 (3.3) ya corrio: se sonda el PREFIJO
seguro de cada grafia (la parte del titulo truncado que no es la ultima
palabra, probablemente cortada a mitad) contra TODO docs/ (excepto
docs/loop/), buscando una CONTINUACION mas larga que el titulo truncado
dentro de un enfasis markdown (*...*) o una celda de tabla (|...|).

BOLSA 2a, RECONSTRUIBLE: la sonda encuentra una continuacion mas larga en
al menos un fichero fuera de docs/loop. El titulo SE COPIA del fichero, no
se propone de memoria, y la fila lleva su fichero:linea.

BOLSA 2b, FORASTERA PURA: la sonda no encuentra nada. Para estas dos y
solo estas dos, LA FUENTE (el ejecutor) PROPONE el titulo real en su
propia columna, marcado FORASTERO (acta 128, 3.3): no se escribe en
ningun otro sitio del repo mas que en esta salida y en la columna de la
tabla de 3.e.

Salida: docs/loop/SALIDA_V132_3C_BOLSA2_PARTIDA.txt

Uso:
  python scripts/loop/vuelta132_bolsa2_particion.py
"""
import glob
import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DOCS = os.path.join(RAIZ, "docs")
LOOP = os.path.join(DOCS, "loop")
SALIDA = os.path.join(LOOP, "SALIDA_V132_3C_BOLSA2_PARTIDA.txt")

RESIDUALES = [
    ("Juran's Quality Handbook_ The C - Joseph A. Defeo", 459),
    ("The Green to Gold Business Play - Daniel C. Esty", 209),
    ("Managing the Risks of Organizat - Reason, J. T_", 90),
    ("Co-Intelligence_ Living and Wor - Ethan Mollick", 39),
]

# BOLSA 2b: propuesta de la fuente (el ejecutor), SOLO para las grafias sin
# reconstruccion en el repo, marcadas FORASTERO. No se escriben en ningun
# otro sitio del repo.
PROPUESTA_FORASTERA = {
    "Juran's Quality Handbook_ The C - Joseph A. Defeo":
        "Juran's Quality Handbook: The Complete Guide to Performance Excellence",
    "Co-Intelligence_ Living and Wor - Ethan Mollick":
        "Co-Intelligence: Living and Working with AI",
}

ITALICA = re.compile(r"(?<!\*)\*(?!\*)([^*]+?)(?<!\*)\*(?!\*)")


def celdas_de(linea):
    if "|" not in linea:
        return []
    return [c.strip() for c in linea.split("|") if c.strip()]


def titulo_de(grafia):
    return grafia.split(" - ", 1)[0].strip()


def prefijo_seguro(titulo):
    if "_" in titulo:
        return titulo.split("_")[0].strip()
    partes = titulo.rsplit(" ", 1)
    return partes[0].strip() if len(partes) > 1 else titulo


def ficheros_docs_fuera_de_loop():
    for p in sorted(glob.glob(os.path.join(DOCS, "**", "*.md"), recursive=True)):
        if os.path.commonpath([p, LOOP]) == LOOP:
            continue
        yield p


def sondar(titulo_truncado):
    prefijo = prefijo_seguro(titulo_truncado)
    hallazgos = []
    for p in ficheros_docs_fuera_de_loop():
        rel = os.path.relpath(p, RAIZ).replace("\\", "/")
        with open(p, encoding="utf-8") as fh:
            for n, linea in enumerate(fh, start=1):
                if prefijo not in linea:
                    continue
                candidatos = ITALICA.findall(linea) + celdas_de(linea)
                for cand in candidatos:
                    cand = cand.strip()
                    cand_titulo = cand.split(" - ", 1)[0].strip()
                    if (cand_titulo.startswith(prefijo) and cand_titulo != titulo_truncado
                            and len(cand_titulo) > len(titulo_truncado)):
                        hallazgos.append((cand_titulo, rel, n))
    por_titulo = {}
    for cand, rel, n in hallazgos:
        por_titulo.setdefault(cand, []).append("%s:%d" % (rel, n))
    return prefijo, por_titulo


def main():
    sys.stdout.reconfigure(encoding="utf-8")

    bolsa_2a = []
    bolsa_2b = []
    lineas_salida = []

    for grafia, n_nodos in RESIDUALES:
        titulo = titulo_de(grafia)
        prefijo, por_titulo = sondar(titulo)
        if por_titulo:
            titulo_completo = max(por_titulo, key=lambda t: len(por_titulo[t]))
            ficheros = sorted(set(por_titulo[titulo_completo]))
            bolsa_2a.append((grafia, n_nodos, titulo_completo, ficheros))
        else:
            propuesta = PROPUESTA_FORASTERA.get(grafia)
            assert propuesta is not None, "grafia sin propuesta forastera: %s" % grafia
            bolsa_2b.append((grafia, n_nodos, propuesta))

    with open(SALIDA, "w", encoding="utf-8") as fh:
        fh.write("BOLSA 2a, RECONSTRUIBLE DESDE EL REPO (%d):\n" % len(bolsa_2a))
        for grafia, n_nodos, titulo_completo, ficheros in bolsa_2a:
            fh.write("  grafia: %s\n" % grafia)
            fh.write("  nodos: %d\n" % n_nodos)
            fh.write("  bolsa: 2a\n")
            fh.write("  titulo propuesto (copiado del fichero): %s\n" % titulo_completo)
            fh.write("  procedencia: %s\n\n" % "; ".join(ficheros))
        fh.write("BOLSA 2b, FORASTERA PURA (%d):\n" % len(bolsa_2b))
        for grafia, n_nodos, propuesta in bolsa_2b:
            fh.write("  grafia: %s\n" % grafia)
            fh.write("  nodos: %d\n" % n_nodos)
            fh.write("  bolsa: 2b\n")
            fh.write("  titulo propuesto (por la fuente, FORASTERO): %s\n" % propuesta)
            fh.write("  procedencia: FORASTERO\n\n")
        fh.write("TOTAL BOLSA 2a: %d\n" % len(bolsa_2a))
        fh.write("TOTAL BOLSA 2b: %d\n" % len(bolsa_2b))

    print("BOLSA 2a (reconstruible): %d" % len(bolsa_2a))
    for grafia, n_nodos, titulo_completo, ficheros in bolsa_2a:
        print("  %d\t%s -> %s\t[%s]" % (n_nodos, grafia, titulo_completo, "; ".join(ficheros)))
    print("BOLSA 2b (forastera pura): %d" % len(bolsa_2b))
    for grafia, n_nodos, propuesta in bolsa_2b:
        print("  %d\t%s -> %s [FORASTERO]" % (n_nodos, grafia, propuesta))
    print("EXITCODE: 0")


if __name__ == "__main__":
    raise SystemExit(main())
