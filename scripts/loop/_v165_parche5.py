# -*- coding: utf-8 -*-
"""Parche 5: la tabla de fases sube ANTES de las constancias del ciclo, para que
la vara de cifras tenga en la ventana lo que necesita cotejar; y la fila del
desfase deja de citar un fichero de fase que no le toca. Trabajo, no
instrumento."""
import io
import re

p = "docs/loop/_v165_cuerpo_original.md"
s = io.open(p, encoding="utf-8").read()

# 1. la fila del desfase vuelve a citar SOLO lo suyo
a = ("| desfase del calibrado | cuatro | **las mismas cuatro** | "
     "`SALIDA_V165_DESFASE_CALIBRADO_APERTURA.txt` y su gemela del cierre, "
     "mas `docs/loop/SALIDA_V165_T7_FASE_08.txt` para la vara de fase |")
b = ("| desfase del calibrado | cuatro | **las mismas cuatro** | "
     "`SALIDA_V165_DESFASE_CALIBRADO_APERTURA.txt` y su gemela |")
assert a in s
s = s.replace(a, b, 1)

# 2. el bloque de fases se recorta de donde esta y se pega ANTES de las
#    constancias del ciclo.
ini = s.index("**EL ESTADO DE LAS ONCE FASES, TALLADO UNA POR UNA CON")
fin = s.index("## 8. LO QUE SE MOVIO EN ESTA VUELTA Y LO QUE NO")
bloque = s[ini:fin].rstrip() + "\n\n"
s = s[:ini] + s[fin:]

ancla = "**LAS CONSTANCIAS DEL CICLO, CADA CELDA CON EL FICHERO DEL QUE SALE:**"
assert ancla in s
s = s.replace(ancla, bloque + ancla, 1)

# 3. y la frase que anunciaba la tabla de fases "justo debajo" ya no vale
c = """**Y EL ESTADO DE LAS ONCE FASES VA JUSTO DEBAJO, TALLADO Y SUMADO DE SU PROPIO
FICHERO (`docs/loop/SALIDA_V165_T7_FASES.txt`), porque una tabla que habla de
apertura y cierre al lado de la palabra desfase tiene que traer esa vara
delante.**"""
if c in s:
    s = s.replace(c, "", 1)

io.open(p, "w", encoding="utf-8", newline="\n").write(s)
print("parche 5 aplicado; el bloque de fases mide %d caracteres" % len(bloque))
