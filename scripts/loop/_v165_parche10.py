# -*- coding: utf-8 -*-
"""Parche 10: se declara el rojo de tallar_cifras_de_antes.py, que NO es de esta
vuelta y lleva al menos dos rojas sin que nadie lo diga. Trabajo, no
instrumento."""
import io
p = "docs/loop/_v165_cuerpo_original.md"
s = io.open(p, encoding="utf-8").read()

ancla = "**RE SELLADO DECLARADO, PORQUE NO SE PROHIBE RE SELLAR SINO RE SELLAR EN"
assert ancla in s
bloque = """**Y UNA GUARDA SALE EN ROJO Y NO LA ESCONDO, AUNQUE NO SEA DE ESTA VUELTA.**
`tallar_cifras_de_antes.py --fichero docs/loop/REPORTE.md` da **exitcode 1**
sobre el reporte de la 165 (`docs/loop/SALIDA_V165_T7_CIFRAS_DE_ANTES_165.txt`).
**Antes de decir nada la corri sobre el reporte de la 164**, sacado de su propio
commit `c59d111a` (`docs/loop/SALIDA_V165_T7_CIFRAS_DE_ANTES_164.txt`): **tambien
da exitcode 1**.

| sujeto | veredicto | hallazgos |
|---|---|---:|
| reporte de la 164 (`c59d111a`) | ROJO exit 1 | 36 |
| reporte de la 165 (este) | ROJO exit 1 | 23 |

> **Asi que NO es una regresion de esta vuelta y no la arreglo por cuenta
> propia.** Su vara pide una cita de fichero detras de cada oracion que hable en
> pasado, y su vocabulario dispara con palabras corrientes (`antes`, `era`,
> `sigue`, `hoy`), asi que sobre un reporte de fase 04 marca prosa que no es
> ninguna cifra de antes. **Lo que me importa decir es lo otro: llevaba al menos
> dos vueltas en rojo y ningun reporte lo nombraba.** Va como PREGUNTA 3.

"""
s = s.replace(ancla, bloque + ancla, 1)

# y la tercera pregunta
a = """**PENDIENTES DE DOCTRINA: NINGUNA.**"""
b = """  3. **`tallar_cifras_de_antes.py` LLEVA AL MENOS DOS VUELTAS EN ROJO Y NADIE LO
     DICE.** Medido hoy sobre los dos reportes, el de la 164 y el de la 165, con
     su salida sellada cada uno. **No lo arreglo**: o su vocabulario se estrecha,
     o esa vara se declara ajena al reporte de fase 04, y las dos cosas son
     decision de quien tenga la vara, no mia. **Pregunto cual de las dos.**

**PENDIENTES DE DOCTRINA: NINGUNA.**"""
assert a in s
s = s.replace(a, b, 1)

# y el veredicto de una linea deja de decir DOS PREGUNTAS
c = "**CINCO DISCUTIBLES MARCADOS** y **DOS PREGUNTAS**."
d = "**CINCO DISCUTIBLES MARCADOS** y **TRES PREGUNTAS**."
assert c in s
s = s.replace(c, d, 1)

io.open(p, "w", encoding="utf-8", newline="\n").write(s)
print("parche 10 aplicado")
