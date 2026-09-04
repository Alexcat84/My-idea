# -*- coding: utf-8 -*-
"""Parche 7: el reporte cita el barrido sellado y trae al menos una cifra con
unidad del vocabulario cotejable. Trabajo, no instrumento."""
import io
p = "docs/loop/_v165_cuerpo_original.md"
s = io.open(p, encoding="utf-8").read()
a = """**Comprobadas las tres rutas posibles, hay
UNA sola en disco:** `dataset/metadata/` y `engine/` **NO EXISTEN**, y el
barrido de las tres esta impreso entero en
`docs/loop/SALIDA_V165_T5_ESTADO_NUEVO.txt`, seccion 3, con su
`CIFRA sedes del indice que existen en disco: 1`."""
b = """**Comprobadas las tres rutas posibles, hay
UNA sola en disco:** `dataset/metadata/` y `engine/` **NO EXISTEN**. **Y esa
frase no es una busqueda negativa suelta: va con su BARRIDO EXHAUSTIVO sellado
en `docs/loop/SALIDA_V165_T5_ESTADO_NUEVO.txt`**, con su `PREGUNTA`, su
`UNIVERSO` (`os.walk` del repo entero salvo `node_modules`, `.git`, `.next` y
`__pycache__`), su `CARDINAL` y **sus dos piernas**: por nombre da
**1 ficheros** y por contenido da **395 ficheros** que solo lo nombran sin
serlo, mas **440** mirados y no decodificables, que se cuentan y no se cuelan
como sin coincidencia."""
assert a in s
s = s.replace(a, b, 1)
io.open(p, "w", encoding="utf-8", newline="\n").write(s)
print("parche 7 aplicado")
