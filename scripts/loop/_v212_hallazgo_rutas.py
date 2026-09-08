# -*- coding: utf-8 -*-
r"""_v212_hallazgo_rutas.py . LA MEDICION DE UN HALLAZGO DE LA VUELTA 212.

COMPUTO DE UNA VUELTA, prefijo de guion bajo: fuera del censo y fuera de la
nomina. Moratoria de AUDITOR.md 6.3. NO REPARA NADA: solo mide y sella.

QUE MIDE. `scripts/loop/vuelta186_rutas_del_reporte.py`, que es la sede de la
regla LA RUTA QUE PROMETE PRUEBA ES CIFRA, se CAE CON EXCEPCION cuando el
reporte cita un DIRECTORIO entre comillas inversas: su patron casa
`docs/plan/`, `os.path.exists` dice que si porque el directorio existe, y
`io.open(...).read()` revienta con IsADirectoryError o FileNotFoundError.

NO ES UN DEFECTO QUE TRAIGA ESTA VUELTA, Y SE PRUEBA: el reporte de la 211, ya
archivado, cita DOS directorios asi, y el de la 210 otros dos. Este fichero
mide los dos textos archivados con
`rutas_del_texto` IMPORTADA de esa misma sede, y no la corrige.
"""
import io
import os
import re
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)
RAIZ = os.path.dirname(os.path.dirname(AQUI))

from vuelta186_rutas_del_reporte import rutas_del_texto  # noqa: E402

NL = chr(10)
VUELTA = int(re.search(r"_v(\d+)_", os.path.basename(os.path.abspath(__file__))).group(1))

# LOS SUJETOS SON LOS DOS REPORTES YA ARCHIVADOS, Y NO EL DE ESTA VUELTA, A
# PROPOSITO: docs/loop/REPORTE.md todavia va a crecer con su cierre, y publicar
# aqui sus bytes seria MEDIR TEMPRANO Y PUBLICAR TARDE, que es la caida de la
# vuelta 28 (EJECUTOR.md 1). A este reporte lo mide, DESPUES del cierre, el
# propio instrumento de la casa: si citara un directorio, se caeria.
SUJETOS = [
    "docs/loop/reportes/REPORTE_V211.md",
    "docs/loop/reportes/REPORTE_V210.md",
]

OUT = []


def di(s=""):
    OUT.append(s)


di("=" * 78)
di("VUELTA %d. HALLAZGO: EL INSTRUMENTO DE RUTAS SE CAE CON UN DIRECTORIO." % VUELTA)
di("=" * 78)
di("")
di("La sede es scripts/loop/vuelta186_rutas_del_reporte.py y NO SE TOCA: la")
di("moratoria de AUDITOR.md 6.3 prohibe reparar lectores. Aqui solo se mide,")
di("importando su propia funcion rutas_del_texto para que el patron sea EL SUYO.")
di("")

total_dirs = 0
for s in SUJETOS:
    p = os.path.join(RAIZ, s.replace("/", os.sep))
    if not os.path.isfile(p):
        di("CIFRA %s: NO EXISTE (ausencia, no cero)" % s)
        continue
    texto = io.open(p, encoding="utf-8").read()
    rutas = rutas_del_texto(texto)
    dirs = []
    faltan = []
    for r in rutas:
        q = os.path.join(RAIZ, r.replace("/", os.sep))
        if os.path.isdir(q):
            dirs.append(r)
        elif not os.path.exists(q):
            faltan.append(r)
    total_dirs += len(dirs)
    di("CIFRA %s: %d rutas distintas, medidas con SU patron" % (s, len(rutas)))
    di("LA TABLA DE RUTAS QUE SON DIRECTORIO Y NO FICHERO, en %s: %d fila(s) "
       "armada(s) sobre las %d rutas de ese texto" % (s, len(dirs), len(rutas)))
    for r in dirs:
        di("   directorio> %s" % r)
    di("CIFRA rutas de %s que no existen en disco: %d %s"
       % (s, len(faltan), faltan if faltan else ""))
    di("CIFRA ese texto TUMBA el instrumento: %s (basta UNA fila de la tabla de "
       "arriba)" % ("SI" if dirs else "NO"))
    di("")

di("CIFRA directorios citados en los DOS sujetos archivados, sumados: %d"
   % total_dirs)
di("")
di("EL CASO ROJO POR MUTACION DE ESTA MEDICION, corrido sobre texto en memoria")
di("y sin tocar ningun fichero: si el detector fuera una constante, un texto sin")
di("directorios daria lo mismo que uno con directorios.")
sin = "cita `docs/loop/REPORTE.md` y `scripts/loop/cerrar_reporte.py` y nada mas"
con = sin + " y ademas `docs/plan/`"
d_sin = [r for r in rutas_del_texto(sin)
         if os.path.isdir(os.path.join(RAIZ, r.replace("/", os.sep)))]
d_con = [r for r in rutas_del_texto(con)
         if os.path.isdir(os.path.join(RAIZ, r.replace("/", os.sep)))]
di("CIFRA directorios en el texto SIN directorio: %d (se exige 0)" % len(d_sin))
di("CIFRA directorios en el texto CON directorio: %d (se exige 1)" % len(d_con))
di("EL CASO ROJO %s: sin mutar da %d y mutado da %d."
   % ("CAE COMO TIENE QUE CAER" if (len(d_sin) == 0 and len(d_con) == 1)
      else "NO CAE", len(d_sin), len(d_con)))
di("")
di("LO QUE ESTO PRUEBA, Y ES LA MITAD QUE IMPORTA: la cifra de rutas que el")
di("reporte de la 211 publica NO PUEDE HABER SALIDO DE ESTE INSTRUMENTO, porque")
di("sobre ese texto el instrumento no llega a imprimir: revienta antes.")

texto = NL.join(OUT) + NL
io.open(os.path.join(RAIZ, "docs", "loop",
                     "SALIDA_V%d_HALLAZGO_RUTAS.txt" % VUELTA),
        "w", encoding="utf-8", newline=NL).write(texto)
sys.stdout.reconfigure(encoding="utf-8")
sys.stdout.write(texto)
