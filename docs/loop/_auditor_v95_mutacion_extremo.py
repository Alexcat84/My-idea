# -*- coding: utf-8 -*-
"""_auditor_v95_mutacion_extremo.py . LA MUTACION QUE EL ENCARGO PIDIO Y QUE
LA PRUEBA DEL EJECUTOR NO HACE: sobre una copia EN MEMORIA del fichero REAL
(docs/plan/04_ENLACES.md), quitar UNA salvedad y comprobar que el REPARTO
con/sin del tallador SE MUEVE. La prueba del ejecutor solo muta la cadena de
contexto que recibe tiene_salvedad(), no el fichero, y por tanto no ejercita
la ventana ni el reparto.

    python docs/loop/_auditor_v95_mutacion_extremo.py
"""
import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(RAIZ, "scripts", "loop"))
from tallar_barrido_cifras import tiene_salvedad, PATRON_SALVEDAD_DEFECTO

PAT = re.compile(r"(?:85 ESCRITA)|(?:87 con direccion)|(?:cifra vigente)")
SAL = re.compile(PATRON_SALVEDAD_DEFECTO)
VENTANA = 200


def reparto(texto):
    con = sin = 0
    for m in PAT.finditer(texto):
        ini = max(0, m.start() - VENTANA)
        fin = min(len(texto), m.end() + VENTANA)
        if tiene_salvedad(texto[ini:fin], SAL):
            con += 1
        else:
            sin += 1
    return con, sin


ruta = os.path.join(RAIZ, "docs", "plan", "04_ENLACES.md")
texto = open(ruta, encoding="utf-8").read()
c0, s0 = reparto(texto)
print("fichero real 04_ENLACES.md          -> con salvedad %d / sin salvedad %d" % (c0, s0))

# la mutacion: quitar UNA sola salvedad de la copia en memoria
antes = texto
for frase in ["hasta la vuelta 92", "hasta la vuelta 94", "desde la vuelta 93"]:
    if frase in texto:
        mutado = texto.replace(frase, "en este momento", 1)
        c1, s1 = reparto(mutado)
        print("copia EN MEMORIA sin '%s' -> con salvedad %d / sin salvedad %d" % (frase, c1, s1))
        if (c1, s1) == (c0, s0):
            print("  ROJO: el reparto NO SE MOVIO al quitar esa salvedad.")
        else:
            print("  VERDE: el reparto SE MOVIO (%+d con / %+d sin)." % (c1 - c0, s1 - s0))
