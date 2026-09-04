# -*- coding: utf-8 -*-
"""Parche 11: cada palabra de veredicto queda pegada a SU fichero, que es lo que
la vara de citas cotejaba mal por proximidad. Trabajo, no instrumento."""
import io
p = "docs/loop/_v165_cuerpo_original.md"
s = io.open(p, encoding="utf-8").read()

a = """**Y UNA GUARDA SALE EN ROJO Y NO LA ESCONDO, AUNQUE NO SEA DE ESTA VUELTA.**
`tallar_cifras_de_antes.py --fichero docs/loop/REPORTE.md` da **exitcode 1**
sobre el reporte de la 165 (`docs/loop/SALIDA_V165_T7_CIFRAS_DE_ANTES_165.txt`).
**Antes de decir nada la corri sobre el reporte de la 164**, sacado de su propio
commit `c59d111a` (`docs/loop/SALIDA_V165_T7_CIFRAS_DE_ANTES_164.txt`): **tambien
da exitcode 1**.

| sujeto | veredicto | hallazgos |
|---|---|---:|
| reporte de la 164 (`c59d111a`) | ROJO exit 1 | 36 |
| reporte de la 165 (este) | ROJO exit 1 | 23 |"""
b = """**Y UNA VARA MAS SALE EN EXITCODE 1 Y NO LA ESCONDO, AUNQUE NO SEA DE ESTA
VUELTA.** `tallar_cifras_de_antes.py --fichero docs/loop/REPORTE.md` da
**exitcode 1** sobre el reporte de la 165. **Antes de decir nada la corri sobre
el reporte de la 164**, sacado de su propio commit `c59d111a`, y da **exitcode 1
tambien**:

| sujeto | exitcode | hallazgos | fichero |
|---|---:|---:|---|
| reporte de la 164 (`c59d111a`) | 1 | 36 | `docs/loop/SALIDA_V165_T7_CIFRAS_DE_ANTES_164.txt` |
| reporte de la 165 (este) | 1 | 23 | `docs/loop/SALIDA_V165_T7_CIFRAS_DE_ANTES_165.txt` |"""
assert a in s
s = s.replace(a, b, 1)

c = """  3. **`tallar_cifras_de_antes.py` LLEVA AL MENOS DOS VUELTAS EN ROJO Y NADIE LO
     DICE.**"""
d = """  3. **`tallar_cifras_de_antes.py` LLEVA AL MENOS DOS VUELTAS EN EXITCODE 1 Y
     NINGUN REPORTE LO NOMBRA.**"""
assert c in s
s = s.replace(c, d, 1)
io.open(p, "w", encoding="utf-8", newline="\n").write(s)
print("parche 11 aplicado")
