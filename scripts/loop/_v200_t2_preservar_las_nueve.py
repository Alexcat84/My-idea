# -*- coding: utf-8 -*-
r"""_v200_t2_preservar_las_nueve.py . LAS NUEVE SELLADAS DE LA VUELTA 183,
PRESERVADAS POR COPIA ANTES DE QUE LA BATERIA DE LA 200 LAS PISE.

PREFIJO DE GUION BAJO, por la moratoria `AUDITOR.md` 6.3 y la adjudicacion `4.5`
del acta 199: un computo de una vuelta que muere con ella no es maquinaria.

DE DONDE SALE, PALABRA POR PALABRA. Encargo de la vuelta 200, punto `2.b`:
*"correr el tramo 1 PISA la sellada del 183. PRESERVA LAS NUEVE ANTES DE TOCAR
NADA, por copia, con sus bytes y su sha256 medidos antes y despues, y publica las
dos medidas. Copiar no es borrar: no se pierde ninguna prueba y por eso lo mando
asi."* Y el hallazgo `5.2` del acta 199 lo mide corriendo el lanzador.

POR QUE UNA SUBCARPETA Y NO UN PREFIJO NUEVO. Las copias conservan el NOMBRE
EXACTO del original, que es lo que las hace citables como la misma prueba, y
viven en `docs/loop/preservadas/v183/`. Un prefijo nuevo dentro de `docs/loop/`
tendria que evitar ademas el patron `SALIDA_V<N>_..._BATERIA` que la guarda de la
seccion 9 de `cerrar_reporte.py` busca, y una carpeta lo evita sin inventarse
nombres: los instrumentos que cuentan selladas hacen `os.listdir(docs/loop)` sin
recursion y no la ven.

USO:
  python scripts/loop/_v200_t2_preservar_las_nueve.py
  python scripts/loop/_v200_t2_preservar_las_nueve.py --copiar
"""
import argparse
import hashlib
import io
import os
import re
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(os.path.dirname(AQUI))
LOOP = os.path.join(RAIZ, "docs", "loop")
DESTINO = os.path.join(LOOP, "preservadas", "v183")
NL = chr(10)
VUELTA_ORIGEN = 183
PATRON = re.compile(r"^SALIDA_V%d_BATERIA_TRAMO_(\d+)\.txt$" % VUELTA_ORIGEN)


def medir(ruta):
    datos = io.open(ruta, "rb").read()
    lf = datos.replace(b"\r\n", b"\n")
    return (len(datos), len(lf), hashlib.sha256(datos).hexdigest(),
            hashlib.sha256(lf).hexdigest())


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--copiar", action="store_true")
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")

    L = []
    w = L.append
    w("=" * 78)
    w("LAS SELLADAS DE LA VUELTA %d, PRESERVADAS ANTES DE QUE LA 200 LAS PISE"
      % VUELTA_ORIGEN)
    w("=" * 78)
    w("")
    w("destino: docs/loop/preservadas/v%d/ (el nombre del fichero NO cambia)"
      % VUELTA_ORIGEN)
    w("")

    originales = sorted(
        (n for n in os.listdir(LOOP) if PATRON.match(n)),
        key=lambda n: int(PATRON.match(n).group(1)))
    w("A) LAS ORIGINALES, CONTADAS DE DISCO Y MEDIDAS ANTES DE TOCAR NADA")
    w("   CIFRA selladas SALIDA_V%d_BATERIA_TRAMO_N.txt en docs/loop/: %d"
      % (VUELTA_ORIGEN, len(originales)))
    antes = {}
    vacias = []
    for n in originales:
        d, lf, sd, slf = medir(os.path.join(LOOP, n))
        antes[n] = (d, lf, sd, slf)
        if d == 0:
            vacias.append(n)
        w("   %-34s disco %7d | LF %7d | sha256 disco %s | sha256 LF %s"
          % (n, d, lf, sd[:16], slf[:16]))
    w("   CIFRA selladas que miden CERO BYTES: %d" % len(vacias))
    w("")

    if a.copiar:
        if not os.path.isdir(DESTINO):
            os.makedirs(DESTINO)
        w("B) LA COPIA, HECHA BYTE A BYTE EN MODO BINARIO")
        for n in originales:
            datos = io.open(os.path.join(LOOP, n), "rb").read()
            io.open(os.path.join(DESTINO, n), "wb").write(datos)
            w("   copiada: %s" % n)
    else:
        w("B) MODO MEDICION: no se copia nada.")
    w("")

    w("C) LAS COPIAS, REMEDIDAS DEL DISCO Y COTEJADAS UNA A UNA")
    iguales = distintas = ausentes = 0
    for n in originales:
        ruta = os.path.join(DESTINO, n)
        if not os.path.isfile(ruta):
            w("   AUSENTE: %s" % n)
            ausentes += 1
            continue
        d, lf, sd, slf = medir(ruta)
        o = antes[n]
        calza = (d, lf, sd, slf) == o
        w("   %-34s disco %7d | LF %7d | sha256 LF %s | CALZA: %s"
          % (n, d, lf, slf[:16], "SI" if calza else "NO"))
        iguales += 1 if calza else 0
        distintas += 0 if calza else 1
    w("   CIFRA copias IDENTICAS a su original: %d" % iguales)
    w("   CIFRA copias DISTINTAS: %d" % distintas)
    w("   CIFRA copias AUSENTES: %d" % ausentes)
    w("")

    w("D) LAS ORIGINALES, REMEDIDAS DESPUES DE COPIAR")
    w("   COPIAR NO ES BORRAR, y eso se comprueba en vez de prometerse.")
    intactas = 0
    for n in originales:
        d, lf, sd, slf = medir(os.path.join(LOOP, n))
        calza = (d, lf, sd, slf) == antes[n]
        intactas += 1 if calza else 0
        w("   %-34s disco %7d | LF %7d | sha256 LF %s | INTACTA: %s"
          % (n, d, lf, slf[:16], "SI" if calza else "NO"))
    w("   CIFRA originales INTACTAS tras la copia: %d de %d"
      % (intactas, len(originales)))
    w("")

    ok = (ausentes == 0 and distintas == 0 and intactas == len(originales)
          and len(originales) > 0 and not vacias) if a.copiar else True
    w("VEREDICTO: %s" % ("VERDE: las %d estan preservadas, identicas y con su "
                         "original intacto." % len(originales) if ok
                         else "ROJO o MEDICION, ver arriba."))
    salida = NL.join(L) + NL
    print(salida)
    io.open(os.path.join(LOOP, "SALIDA_V200_T2_PRESERVAR_LAS_NUEVE.txt"), "w",
            encoding="utf-8", newline=NL).write(salida)
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
