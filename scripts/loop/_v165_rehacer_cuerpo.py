# -*- coding: utf-8 -*-
"""Reinyecta el bloque de re sellado (TALLADO por verificar_re_sellado.py, no
tecleado) en el cuerpo del reporte de la vuelta 165. Trabajo, no instrumento.

LAS LINEAS SE LEEN DE LA SALIDA DE LA GUARDA cuando esta las reclama, y del
propio REPORTE.md cuando la guarda ya esta verde y por tanto no las imprime.
Si no salen OCHO, esto PARA en vez de publicar un bloque corto."""
import io
import os
import re

ESPERADAS = 8
RUTA_GUARDA = "docs/loop/SALIDA_V165_RE_SELLADO.txt"

lineas = []
if os.path.exists(RUTA_GUARDA):
    lineas = [l.strip() for l in io.open(RUTA_GUARDA, encoding="utf-8")
              if l.strip().startswith("RE SELLADO DECLARADO:")]
if len(lineas) != ESPERADAS and os.path.exists("docs/loop/REPORTE.md"):
    rep = io.open("docs/loop/REPORTE.md", encoding="utf-8").read()
    del_reporte = re.findall(r"^  - `(RE SELLADO DECLARADO: .+?)`$", rep, re.M)
    vistas = set(lineas)
    for l in del_reporte:
        if l not in vistas:
            lineas.append(l)
            vistas.add(l)
lineas = sorted(set(lineas))
if len(lineas) != ESPERADAS:
    raise SystemExit("PARADA: se esperaban %d lineas de re sellado y hay %d"
                     % (ESPERADAS, len(lineas)))

bloque = "\n".join("  - `%s`" % l for l in lineas)
extra = (
    "\n\n**Y TRES DE LAS OCHO SON SALIDAS DE ESTA MISMA VUELTA, RE CORRIDAS\n"
    "DESPUES DEL COMMIT DE SU TAREA, Y SE DECLARAN IGUAL.**\n"
    "`SALIDA_V165_T2_CENSO_ANTES_DESPUES.txt` se re corrio cada vez que la\n"
    "nomina crecio, y por eso mueve OCHO lineas `CIFRA`;\n"
    "`SALIDA_V165_T4_MUTACION_SUJETO.txt` se re corrio al anadirle el bloque\n"
    "`C2` de la transitividad, y mueve DOS; y `SALIDA_V165_T5_ESTADO_NUEVO.txt`\n"
    "se re corrio cuando su instrumento gano el `BARRIDO EXHAUSTIVO` que la vara\n"
    "de ausencias pedia, y mueve TRES. **Nacer no es re sellar, pero re correr si\n"
    "lo es, y la guarda no distingue de quien es la mano.**")

s = io.open("docs/loop/_v165_cuerpo_original.md", encoding="utf-8").read()
if "<<<RESELLADO>>>" not in s:
    raise SystemExit("PARADA: el cuerpo original no trae la marca")
s = s.replace("<<<RESELLADO>>>", bloque + extra)
io.open("docs/loop/_v165_cuerpo_reporte.md", "w", encoding="utf-8",
        newline="\n").write(s)
print("cuerpo reconstruido con %d lineas de re sellado" % len(lineas))
