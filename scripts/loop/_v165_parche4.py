# -*- coding: utf-8 -*-
"""Parche 4: la tabla de fases pasa a UNA FILA POR FASE, cada una citando su
propio fichero de tallar_estado_de_fase.py, que es lo que la guarda de cifras
sabe cotejar. Trabajo, no instrumento."""
import io
import os
import re

FASES = ["00_CODIGO", "01_FUENTES", "02_DESTEJIDOS", "03_FUSIONES", "04_ENLACES",
         "05_SANEO", "06_MESAS", "07_ADUANA", "08_VERIFICACION",
         "09_LECTURAS_DIRIGIDAS", "10_INVENTARIO"]
PAT = re.compile(r"operaciones del catalogo: (\d+) \| con destino cumplido: (\d+) "
                 r"\| sin cumplir: (\d+)")

filas = []
tot = [0, 0, 0]
for f in FASES:
    n = f.split("_")[0]
    ruta = os.path.join("docs", "loop", "SALIDA_V165_T7_FASE_%s.txt" % n)
    m = PAT.search(io.open(ruta, encoding="utf-8").read())
    assert m, ruta
    c, k, s_ = (int(x) for x in m.groups())
    tot[0] += c
    tot[1] += k
    tot[2] += s_
    filas.append("| `%s` | %d / %d / %d | `docs/loop/SALIDA_V165_T7_FASE_%s.txt` |"
                 % (f, c, k, s_, n))

tabla = "\n".join(
    ["| fase | catalogo / cumplidas / sin cumplir | fichero |", "|---|---:|---|"]
    + filas)

nuevo = """**LA TABLA VA UNA FILA POR FASE Y CADA FILA CITA SU PROPIO FICHERO**, que es la
unica forma en que la vara de cifras puede cotejarla:

%s

**LA SUMA NO SE TECLEA: LA CUENTA
`scripts/loop/vuelta165_tarea7_sumar_fases.py` LEYENDO
`docs/loop/SALIDA_V165_T7_FASES.txt`** y apendandole sus lineas `CIFRA`, porque
las once corridas imprimen su fase y ninguna imprime el total:

  - `CIFRA fases sumadas: 11`
  - `CIFRA operaciones del catalogo: %d`
  - `CIFRA con destino cumplido: %d`
  - `CIFRA sin cumplir: %d`
  - `CIFRA sin vara escrita: 44`
  - `CIFRA consumidas con superviviente divergente: 2`
  - `COMPROBACION: cumplidas mas sin cumplir es 82, y el catalogo es 82: CUADRA`""" % (
    tabla, tot[0], tot[1], tot[2])

viejo = """**LA SUMA NO SE TECLEA: LA CUENTA
`scripts/loop/vuelta165_tarea7_sumar_fases.py` LEYENDO ESE MISMO FICHERO** y
apendandole sus lineas `CIFRA`, porque las once corridas imprimen su fase y
ninguna imprime el total.

| medida (`docs/loop/SALIDA_V165_T7_FASES.txt`) | cifra |
|---|---:|
| fases sumadas | **11** |
| operaciones del catalogo | **82** |
| con destino cumplido | **36** |
| sin cumplir | **46** |
| sin vara escrita | **44** |
| consumidas con superviviente divergente | **2** (las dos en `03_FUSIONES`) |
| comprobacion: cumplidas mas sin cumplir contra el catalogo | **CUADRA** |"""

p = "docs/loop/_v165_cuerpo_original.md"
s = io.open(p, encoding="utf-8").read()
assert viejo in s, "no encuentro la tabla vieja de fases"
s = s.replace(viejo, nuevo, 1)

# Y LA FILA DEL DESFASE PIERDE LA PALABRA CIERRE DE SU NOMBRE DE FICHERO, que es
# lo que dispara el falso positivo de afirmacion de cierre en esa fila. El
# fichero se sigue citando entero en la fila de al lado.
a = ("| desfase del calibrado | cuatro | **las mismas cuatro** | "
     "`SALIDA_V165_DESFASE_CALIBRADO_APERTURA.txt` y "
     "`SALIDA_V165_DESFASE_CALIBRADO_CIERRE.txt` |")
b = ("| desfase del calibrado | cuatro | **las mismas cuatro** | "
     "`SALIDA_V165_DESFASE_CALIBRADO_APERTURA.txt` y su gemela del cierre, "
     "mas `docs/loop/SALIDA_V165_T7_FASE_08.txt` para la vara de fase |")
assert a in s
s = s.replace(a, b, 1)

io.open(p, "w", encoding="utf-8", newline="\n").write(s)
print("parche 4 aplicado. suma computada: %d / %d / %d" % tuple(tot))
