# -*- coding: utf-8 -*-
"""Parche 8: la cita del barrido va en la MISMA linea que la afirmacion de
ausencia y en la MISMA linea que cada cifra, porque la ventana de las guardas es
estrecha. Trabajo, no instrumento."""
import io
p = "docs/loop/_v165_cuerpo_original.md"
s = io.open(p, encoding="utf-8").read()
a = """**Comprobadas las tres rutas posibles, hay
UNA sola en disco:** `dataset/metadata/` y `engine/` **NO EXISTEN**. **Y esa
frase no es una busqueda negativa suelta: va con su BARRIDO EXHAUSTIVO sellado
en `docs/loop/SALIDA_V165_T5_ESTADO_NUEVO.txt`**, con su `PREGUNTA`, su
`UNIVERSO` (`os.walk` del repo entero salvo `node_modules`, `.git`, `.next` y
`__pycache__`), su `CARDINAL` y **sus dos piernas**: por nombre da
**1 ficheros** y por contenido da **395 ficheros** que solo lo nombran sin
serlo, mas **440** mirados y no decodificables, que se cuentan y no se cuelan
como sin coincidencia."""
b = """**Comprobadas las tres rutas posibles, hay
UNA sola en disco:** `dataset/metadata/` y `engine/` **NO EXISTEN** (`docs/loop/SALIDA_V165_T5_ESTADO_NUEVO.txt`).
**Y esa frase no es una busqueda negativa suelta: va con su BARRIDO EXHAUSTIVO
sellado en `docs/loop/SALIDA_V165_T5_ESTADO_NUEVO.txt`**, con su `PREGUNTA`, su
`UNIVERSO` (`os.walk` del repo entero salvo `node_modules`, `.git`, `.next` y
`__pycache__`), su `CARDINAL` y **sus dos piernas**:
por nombre da **1 ficheros** (`docs/loop/SALIDA_V165_T5_ESTADO_NUEVO.txt`),
y por contenido da **395 ficheros** (`docs/loop/SALIDA_V165_T5_ESTADO_NUEVO.txt`) que solo lo nombran sin serlo,
mas **440** mirados y no decodificables, que se cuentan y no se cuelan como sin
coincidencia."""
assert a in s
s = s.replace(a, b, 1)
io.open(p, "w", encoding="utf-8", newline="\n").write(s)
print("parche 8 aplicado")
