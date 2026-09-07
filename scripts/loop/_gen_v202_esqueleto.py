# -*- coding: utf-8 -*-
r"""_gen_v202_esqueleto.py . GENERA scripts/loop/vuelta202_esqueleto_reporte.py
COMO CLON DECLARADO DE LA 201, COPIANDO TODO LO DEMAS BYTE A BYTE.

Fichero de computo con PREFIJO DE GUION BAJO: fuera del censo y fuera de la
nomina. Cambia EXACTAMENTE cuatro cosas y las imprime una a una: el docstring,
la constante `VUELTA`, la lista `TAREAS` y el bloque de prosa del encabezado del
reporte. TODO LO DEMAS, incluidas las cinco funciones puras y las guardas del
PASO 0, se copia sin tocar.
"""
import io
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import _gen_v202_esqueleto_piezas as P   # noqa: E402

NL = chr(10)
RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
FUENTE = os.path.join(RAIZ, "scripts", "loop", "vuelta201_esqueleto_reporte.py")
DESTINO = os.path.join(RAIZ, "scripts", "loop", "vuelta202_esqueleto_reporte.py")

src = io.open(FUENTE, encoding="utf-8").read().replace(chr(13) + NL, NL)
L = src.split(NL)
n_antes = len(L)

# 1. EL DOCSTRING: la linea 1 es el coding, el docstring va de la 2 a la 38.
assert L[0].startswith("# -*- coding"), L[0][:60]
assert L[1].startswith('r' + chr(34) * 3 + 'vuelta201_esqueleto_reporte.py'), L[1][:60]
assert L[37] == chr(34) * 3, repr(L[37])
doc_viejo = NL.join(L[1:38])
resto = NL.join(L[38:])
texto = L[0] + NL + P.DOCSTRING + NL + resto

# 2. LA CONSTANTE.
assert texto.count("VUELTA = 201") == 1
texto = texto.replace("VUELTA = 201", "VUELTA = 202")

# 3. LA LISTA TAREAS: del marcador de apertura al primer ']' en columna 0.
i = texto.index("TAREAS = [")
j = texto.index(NL + "]" + NL, i) + len(NL + "]")
tareas_viejo = texto[i:j]
texto = texto[:i] + P.TAREAS_TXT + texto[j:]

# 4. EL BLOQUE DE PROSA: del primer '> **ESTE REPORTE SE ABRIO' hasta la linea
#    que cierra la prosa, justo antes del veredicto sin escribir.
ini = texto.index("> **ESTE REPORTE SE ABRIO")
fin = texto.index(NL + NL + "**EL VEREDICTO DE UNA LINEA: SIN ESCRIBIR TODAVIA.**")
prosa_vieja = texto[ini:fin]
texto = texto[:ini] + P.PROSA + texto[fin:]

io.open(DESTINO, "w", encoding="utf-8", newline=NL).write(texto)

print("FUENTE : %s (%d bytes, %d lineas)"
      % (os.path.relpath(FUENTE, RAIZ).replace(os.sep, "/"),
         len(src.encode("utf-8")), n_antes))
print("DESTINO: %s (%d bytes, %d lineas)"
      % (os.path.relpath(DESTINO, RAIZ).replace(os.sep, "/"),
         len(texto.encode("utf-8")), len(texto.split(NL))))
print("")
print("LAS CUATRO PIEZAS QUE CAMBIAN, MEDIDAS Y NO NARRADAS:")
print("   docstring : %d caracteres fuera, %d dentro"
      % (len(doc_viejo), len(P.DOCSTRING)))
print("   VUELTA    : 201 -> 202 (1 aparicion)")
print("   TAREAS    : %d caracteres fuera, %d dentro; %d entradas dentro"
      % (len(tareas_viejo), len(P.TAREAS_TXT), P.TAREAS_TXT.count(NL + "    ('")))
print("   prosa     : %d caracteres fuera, %d dentro"
      % (len(prosa_vieja), len(P.PROSA)))
print("")
# LA CIFRA DE LO COPIADO SE MIDE CON difflib Y NO POR POSICION: las cuatro
# piezas que cambian corren las lineas de abajo, y una comparacion posicional
# publicaria una cifra que no dice lo que parece decir.
import difflib   # noqa: E402
a_l = src.split(NL)
b_l = texto.split(NL)
sm = difflib.SequenceMatcher(None, a_l, b_l, autojunk=False)
iguales = sum(bl.size for bl in sm.get_matching_blocks())
print("CIFRA lineas de la fuente: %d | del destino: %d" % (len(a_l), len(b_l)))
print("CIFRA lineas COPIADAS SIN TOCAR, contadas con difflib: %d" % iguales)
print("CIFRA lineas del destino que NO vienen de la fuente: %d"
      % (len(b_l) - iguales))
