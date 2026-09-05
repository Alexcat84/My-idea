### TAREA 2. LAS DOS SUB-TAREAS QUE LA VUELTA 173 NO EJECUTO

**2.a EL ACTA 172 ENTERA QUEDA EN EL `R.42`.** Instrumento
`scripts/loop/vuelta174_tarea2a_registrar_acta172.py`, salida
`docs/loop/SALIDA_V174_T2A_REGISTRO_ACTA_172.txt`. **Ninguna cifra tecleada:**

| que se computa | de donde sale | valor |
|---|---|---|
| numero de la entrada | `serie_de_registros.py`, siguiente libre de las DOS sedes | **R.42** |
| adjudicaciones | barrido `6.n` del cuerpo acotado, parando en el primer hueco | **11** |
| caidas propias del auditor | negritas `CAIDA n` del cuerpo acotado | **2** |
| cuerpo del acta 172 | acotado por su cabecera y la siguiente | `ACTA_AUDITOR.md` **58375 a 58940** |
| serie despues de escribir | recomputada | **34 entradas, 0 colisiones, 0 huecos** |
| sede | frase de la `6.3` del acta 162, hallada **1** vez en el fichero entero | `docs/PENDIENTES.md` |

**EL REPARTO POR VIA, CONTADO Y NO TECLEADO:** EJECUTADA **2** (`6.2`, `6.4`);
NO SE CORRIO **2** (`6.3`, `6.11`); SIN TOCAR NADA **7** (`6.1`, `6.5`, `6.6`,
`6.7`, `6.8`, `6.9`, `6.10`).

**LA MAQUINA NO SE CLONA, SE IMPORTA, Y ES LO UNICO NUEVO DEL INSTRUMENTO.** Los
dos registradores anteriores copiaban el mecanismo entero cada vuelta, o sea tres
sitios donde arreglar el mismo fallo. Aqui `PAT_CAIDA`, `PALABRA`,
`titulo_de_la_negrita`, `claves_de_adjudicacion` y `_cuenta_caidas` **se importan
de `vuelta172_tarea1_registrar_acta171.py`**, que es su ultima sede y la que la
bateria ya vigila con `vuelta172_tarea1b_mutacion_registro.py`. Lo unico propio
del fichero nuevo es **el acote de su acta y sus tablas de glosas**. Es la `6.6`
de la propia acta 172 aplicada a si misma (discutible `D.3`).

**Y LA DIFERENCIA DE FONDO CON EL `R.41`, QUE CIERRA EL CIRCULO DE LA `6.4`.** El
`R.41` se escribio **la primera** de su vuelta y por eso su campo era **VIA
PREVISTA** y sus glosas hablaban en futuro. **El `R.42` se escribe la penultima**,
con la TAREA 1 entera ya cerrada y medida, asi que su campo es **VIA** a secas,
sus glosas **si afirman en pasado** y **cada una lleva al lado la linea o la
salida que la mide**. Por eso el `R.42` **no necesita ningun fichero de
confirmacion posterior**: no hay nada que confirmar despues porque nada se afirmo
antes de tiempo.

**UNA ETIQUETA QUE NO ALCANZA, DECLARADA EN VEZ DE INVENTADA.** La `6.3` del acta
172 (mover la bateria al principio de la vuelta) **quedo sin objeto por una
decision posterior del fundador**, la del 5 sep 2026 que la saca del ciclo por
vuelta. Las tres etiquetas de VIA escritas son `EJECUTADA`, `SIN TOCAR NADA` y
`NO SE CORRIO`, y **ninguna dice "superada por decision del fundador"**. Se usa
la mas cercana y **el hueco sube como PENDIENTE DE DOCTRINA** (`EJECUTOR.md` 5),
en vez de estrenar una etiqueta por mano del ejecutor.

**2.b NACE `scripts/loop/vuelta172_tarea1b_confirmar_r41.py`, QUE LLEVABA DOS
VUELTAS PROMETIDO Y SIN EXISTIR.** Salida
`docs/loop/SALIDA_V174_T2B_CONFIRMAR_R41.txt`.

**EL NOMBRE LLEVA `vuelta172` Y NO `vuelta174`, Y ES DELIBERADO:** es el nombre
exacto que el recuadro del `R.41` publica (`docs/PENDIENTES.md:12455`, leido hoy).
**Renombrarlo dejaria la promesa apuntando igual a un vacio**, que es justo la
caida `4.5` que esta sub-tarea paga.

**QUE MIDE, Y LAS DOS COLUMNAS SE MIDEN SIN TECLEARSE:** la tarea que cada glosa
nombra se extrae del texto del propio `R.41` con expresion regular; el estado de
esa tarea se lee de la tabla de `docs/loop/reportes/REPORTE_V172.md`, **48.851
bytes medidos con `os.path.getsize` en la corrida**. **12 glosas leidas, 7 con
tarea nombrada y estado hallado, 5 que se acatan sin tarea.** La anexion es
**adicion pura de 2.686 bytes**, con **9 comprobaciones de relectura y 0 fallan**,
incluidas *"el texto de ARRIBA del `R.41` no se toco"* y *"el `R.42` de al lado
no se toco"*.

**Y EL INSTRUMENTO NO PODIA CORRER ANTES DE HOY, DICHO COMO CAUSA Y NO COMO
EXCUSA:** su fuente de estados es el reporte de la 172 **cerrado y archivado**, y
ese fichero no existio hasta la TAREA 1.a de esta misma vuelta. **Eso explica las
dos vueltas de promesa vacia, no las excusa.** Y el instrumento aplica la regla a
si mismo: **cae en rojo y no escribe nada si su fuente no existe o mide cero
bytes.**

**UN CONTRASTE DECLARADO Y NO RESUELTO COPIANDO** (`EJECUTOR.md` 2): las filas de
la `6.4` y la `6.5` leen **`ABIERTA, SIN CERRAR`**, que es lo que la fila entera
de la TAREA 4 publica. La clausula `4.6` del acta del auditor de la 172 midio
aparte que **la 4.a y la 4.b si estan hechas y verificadas** y que solo falta la
`4.c`. **Las dos cosas son ciertas y la discrepancia queda escrita en el bloque
anexado**, sin elegir una.

**LA GUARDA QUE MORDIO, Y NO SE AFLOJO SINO QUE SE REAPUNTO.** La primera corrida
salio **ROJA** por *"se colaron guiones largos o medios"*: `docs/PENDIENTES.md` es
un fichero historico que **ya traia** guiones largos de 2026, cosa que la TAREA
2.b de la vuelta 172 ya habia medido y dejado escrita. La guarda pasa a mirar **el
DELTA y no el total**, que es el remedio que la casa ya uso, y **el caso positivo
prueba las dos mitades**: que PASA sobre una sede que ya traia uno de antes y que
**CAE igualmente si el bloque anade uno nuevo sobre esa misma sede**.

**EL CASO POSITIVO POR MUTACION:**
`scripts/loop/vuelta174_tarea2b_mutacion_confirmar.py`
(`docs/loop/SALIDA_V174_T2B_MUTACION_CONFIRMAR.txt`), **34 de 34**, sobre SUJETO
CONGELADO y con cero lecturas de disco y cero escrituras. Tumba las cinco
funciones puras una a una: el acote cae si la cabecera falta o esta duplicada y
**para en la cabecera del `R.42` sin comersela**; las glosas devuelven **otra**
tarea si el texto dice otra (no hay constante escondida); los estados se leen sin
suavizar el `ABIERTA, SIN CERRAR`; y los cinco rojos de la anexion devuelven el
texto **INTACTO**.
