# -*- coding: utf-8 -*-
"""Reinyecta el bloque de re sellado (tallado por la guarda) en el cuerpo."""
import io, re, os, sys
RUTA_GUARDA = "docs/loop/SALIDA_V165_RE_SELLADO.txt"
lineas = [l.strip() for l in io.open(RUTA_GUARDA, encoding="utf-8")
          if l.strip().startswith("RE SELLADO DECLARADO:")]
if not lineas and os.path.exists("docs/loop/REPORTE.md"):
    rep = io.open("docs/loop/REPORTE.md", encoding="utf-8").read()
    lineas = re.findall(r"^  - `(RE SELLADO DECLARADO: .+?)`$", rep, re.M)
if len(lineas) != 7:
    raise SystemExit("PARADA: se esperaban 7 lineas de re sellado y hay %d" % len(lineas))
bloque = "\n".join("  - `%s`" % l for l in lineas)
extra = ("\n\n**Y DOS DE LAS SIETE SON SALIDAS DE ESTA MISMA VUELTA, RE CORRIDAS\n"
         "DESPUES DEL COMMIT DE SU TAREA, Y SE DECLARAN IGUAL.**\n"
         "`SALIDA_V165_T2_CENSO_ANTES_DESPUES.txt` se re corrio cada vez que la\n"
         "nomina crecio, y por eso mueve OCHO lineas `CIFRA`;\n"
         "`SALIDA_V165_T4_MUTACION_SUJETO.txt` se re corrio al anadirle el bloque\n"
         "`C2` de la transitividad, y mueve DOS. **Nacer no es re sellar, pero re\n"
         "correr si lo es, y la guarda no distingue de quien es la mano.**")
s = io.open("docs/loop/_v165_cuerpo_original.md", encoding="utf-8").read()
if "<<<RESELLADO>>>" not in s:
    raise SystemExit("PARADA: el cuerpo original no trae la marca")
s = s.replace("<<<RESELLADO>>>", bloque + extra)
io.open("docs/loop/_v165_cuerpo_reporte.md", "w", encoding="utf-8", newline="\n").write(s)
print("cuerpo reconstruido con %d lineas de re sellado" % len(lineas))
