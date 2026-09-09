## 3. LAS CIFRAS DE LA VUELTA, CONTADAS DE SUS FICHEROS

### 3.1. EL CICLO ENTERO DE GATE 0, LOS DOS LADOS, NUNCA `run_phase1.py` A SECAS

**Contado de las dos salidas de consola, no de memoria.**

| lado | comandos con exitcode leido | los que no dan 0 | peor |
|---|---:|---:|---|
| **APERTURA** | (sin fichero de consola) | | |
| **CIERRE** | (sin fichero de consola) | | |

**`numstat` del lado de cierre: 2 fila(s).** **`numstat` de `dataset/`
al cerrar: 0 fila(s).**

### 3.2. LAS SEDES QUE LA VUELTA MOVIO Y LAS QUE NO, POR LAS DOS CONVENCIONES

**El `sha256` de apertura se LEE de `docs/loop/SALIDA_V214_APERTURA.txt`, que se
sello antes de la primera operacion; el de cierre se computa ahora.**

| sede | sha256 LF al abrir | sha256 LF al cerrar | | bytes disco / LF |
|---|---|---|---|---|
| `docs/plan/INVENTARIO.jsonl` | 69666b73339f2afe | 43cea06634e6fc1a | **SE MOVIO** | 629533 / 629533 |
| `docs/plan/OPERACIONES.jsonl` | ca1d95b5b3d19e9e | 650578474361eb2b | **SE MOVIO** | 517181 / 517181 |
| `docs/plan/08_VERIFICACION.md` | 76bfebb6b2d8ef72 | 578eeefab6db2fd4 | **SE MOVIO** | 73652 / 73652 |
| `docs/INTRA_DOMINIO_VEREDICTOS.jsonl` | 758edf1f5c313c18 | 758edf1f5c313c18 | quieta | 4057130 / 4057130 |
| `docs/INTRA_DOMINIO_INFORME.md` | c05b6bcd20188a9c | c05b6bcd20188a9c | quieta | 943970 / 943970 |
| `docs/plan/00_INDICE.md` | 2e71336cc2fdc387 | 2e71336cc2fdc387 | quieta | 45278 / 45278 |
| `docs/BANCO_DE_TEXTOS.md` | 8adbd60239509bb4 | 8adbd60239509bb4 | quieta | 186490 / 186490 |
| `docs/plan/BANCO_DEL_PLAN.md` | 7836c8976c585143 | 7836c8976c585143 | quieta | 61554 / 61554 |
| `dataset/metadata/master_graph.json` | 627cc662296f7f00 | 627cc662296f7f00 | quieta | 8375817 / 8375817 |
| `docs/loop/ACTA_AUDITOR.md` | d78556e9744b4925 | d78556e9744b4925 | quieta | 5011522 / 5011522 |
| `docs/loop/PROMPT_SIGUIENTE.md` | 2d777a347a04b0fc | 2d777a347a04b0fc | quieta | 3358 / 3358 |

**CIFRA sedes cotejadas: 11 | CIFRA que se movieron: 3.** **Y
las que se movieron son EXACTAMENTE las tres que las tareas 1 y 2 nombran, ni una
mas:** el inventario (las 95), el expediente (la evidencia de `OP-I-01`) y la vara
del criterio de hecho. **`docs/loop/ACTA_AUDITOR.md` y
`docs/loop/PROMPT_SIGUIENTE.md`, que son sede del auditor, quedan QUIETAS**, y
esa es la prueba de que la TAREA 3 se quedo en mi reporte.

### 3.3. LAS RUTAS QUE ESTE REPORTE CITA, MEDIDAS CON EL INSTRUMENTO DE LA CASA

`scripts/loop/vuelta186_rutas_del_reporte.py` se corre **DESPUES** de cerrar el
reporte, que es cuando el texto ya esta entero, y su salida se cita en el commit
de cierre. **Es el instrumento que en la 213 cazo la `C.1`, y esta vuelta lo lleva
ademas metido en tres de mis compositores como guarda previa: los tres cuentan
los directorios de dos o mas tramos entre comillas inversas ANTES de escribir, y
los tres me mordieron al menos una vez.**

## 4. LO QUE SE TOCO, Y LO QUE NO

### 4.1. LA MORATORIA DE MAQUINARIA, Y LO QUE ESTA VUELTA ESCRIBIO

**Ningun arnes, guarda ni lector nuevo, y ninguno reparado.** Todo lo que esta
vuelta escribio en el arbol de scripts del bucle lleva **prefijo de guion bajo**,
vive **fuera del censo y fuera de la nomina**, y **muere con la vuelta**.

**CONTADO DE `git diff --name-only` entre el HEAD de apertura y el de ahora:
14 fichero(s) tocados ahi, de los cuales 14 llevan el
prefijo `_v214_` y 0 no lo llevan.**

**LA NOMINA DE LA BATERIA SIGUE CONGELADA EN 135**, medida por mi en esta
vuelta con el carril `--plan` del lanzador, que no la toca.

**LO QUE LA APERTURA SELLADA PUBLICA, REPETIDO AQUI PORQUE UNA CIFRA AUSENTE Y
UNA CIFRA QUE CALZA NO SON LO MISMO** (guarda `D.1` de `cerrar_reporte.py`, que me
la exigio y tenia razon):

- **`git status --porcelain` al entrar: 1 linea**, y era mi propio script
  de apertura sin rastrear.
- **CIFRA filas de git diff --numstat -- dataset/ AL ENTRAR: 0.**

### 4.2. LO QUE ESTA VUELTA NO HIZO, DICHO PARA QUE NO SE BUSQUE

- **No declaro la campaña consumada y no pidio ningun merge.** El bucle no funde
  ramas.
- **No escribio una linea en la sede del auditor**, y esta medido arriba con los
  dos `sha256` quietos.
- **No movio ningun campo `estado`**, ni en `OP-I-01` ni en ninguna de las 71, y
  la guarda de la TAREA 1 lo comprueba sobre el fichero entero.
- **No toco ni un nodo, ni un veredicto, ni la vara del expediente.**
- **No corrio la bateria**: la 214 no es vuelta de bateria.

### 4.3. LA FECHA DE LA VUELTA, MEDIDA Y NO SUPUESTA

- **commit de apertura**: 2026-09-09 06:07:10 -0400
- **primer commit de la vuelta**: 2026-09-09 06:14:26 -0400
- **ultimo commit al componer este cierre**: 2026-09-09 06:49:11 -0400

## 5. LOS DISCUTIBLES, MARCADOS ANTES DE SABER SI ACIERTO

- **`D.3` LA `P3` DE LA VARA SE VA A DISPARAR CON MIS PROPIOS COMMITS.** La `P3`
  pide un commit cuyo mensaje nombre el `id_op` **y que toque `scripts/`,
  `dataset/`, `engine/` o `web/`**; mis commits nombran `OP-I-01` y tocan
  `scripts/`, porque ahi viven mis instrumentos. **El trabajo real aterrizo en el
  arbol del plan, que es justo lo que la `P3` descuenta a proposito.** No toco la
  vara y **no me apoyo en esa `P3`** para decir que la ficha cierra.
- **LA SEDE DE LA MARCA DE LAS 95 ES EL CAMPO `forma`.** Lo elegi por el
  precedente medido de la **linea 258** de `scripts/loop/_v203_t3_op_i_01.py`,
  pero **es una eleccion mia** y otra sede (una clave nueva) habria sido
  defendible. **Marco que es discutible.**
- **ESCRIBI EN `docs/plan/OPERACIONES.jsonl`, QUE LA VUELTA 213 TENIA PROHIBIDO
  TOCAR.** Mi encargo me manda cerrar la ficha con su prueba y use el carril que
  la propia ficha ya habia usado, **pero la prohibicion de la 213 era de la 213 y
  la mia no la repite**: si el auditor entiende que esa escritura necesitaba
  mandato explicito, **la marca es esta**.
- **LA REGLA DE EXCLUSION DE LA `2.a` LA ESCRIBI YO.** Que una clausula que abre
  con el numero de una fase con fila ya existente **no sea** la vara de su fase es
  una lectura mia, mecanica pero mia. **Sin ella, la fila 08 habria repetido la
  tabla entera.**

## 6. LAS PREGUNTAS

1. **¿La `2.a` deberia haber metido las tres filas DENTRO de la tabla, como hice,
   o como bloque aparte?** Las meti dentro porque el encargo dice que **la tabla
   gana sus filas**, y lo hice **sin tocar una letra de las viejas**. Si la casa
   prefiere el bloque aparte, se dice y se mueve.
2. **¿Un `numstat` de 95 lineas modificadas en un fichero del arbol del plan necesita
   algo mas que la decision del fundador por su ruta?** Lo hice con esa decision y
   con conteo antes y despues, y lo pregunto porque es la escritura mas ancha que
   una vuelta ha hecho ahi en mucho tiempo.

## 7. PENDIENTES DE DOCTRINA

1. **EL MARCADOR CONTRA SU CIFRA VIEJA (`D.5`).** La clausula de `OP-L-01` y
   `OP-L-02` escribe *"sigue en 2.117"* y el archivo mide **3388** hoy. **Leida a
   la letra no calza; leida por su corte, pide que ESA operacion no lo mueva, y lo
   movio el cribado al cerrar.** **Cual de las dos lecturas manda no esta escrito
   en ningun banco**, y no lo decido yo.
2. **SI LOS PUNTOS EN `A MEDIAS` BLOQUEAN UN CIERRE DE FASE.** `OP-I-01` queda con
   **2 en CUBRE y 2 en A MEDIAS**, y los dos que quedan lo estan por motivos
   estructurales (una negativa que no se puede citar, y una vista humana que su
   propio documento declara que no se regenera ahi). **Nada dice si eso cierra o
   no cierra.**

## 8. MIS CAIDAS PROPIAS, CADA UNA CON SU NOMBRE Y CONTADA UNA SOLA VEZ

**Son SIETE, y las siete las cazaron mis propias guardas ANTES de publicar nada.**
Las escribo porque una guarda que muerde y no se cuenta es una guarda que la
proxima vuelta no sabe que existe.

- **`D.1` EL FICHERO TENIA DOS CONVENCIONES DE VOLCADO Y YO NO LO SABIA.** Mi
  primera version de la TAREA 1 re-volcaba con `json.dumps` por defecto; la
  **simulacion** midio que **335 de las 672 lineas** estan volcadas con
  separadores compactos y **337** con los de por defecto. **Un re-volcado ciego
  habria reformateado 335 lineas que nadie mando tocar, y el cotejo semantico lo
  habria dado por bueno.** Remedio: medir la convencion de **cada** linea antes de
  tocarla, mas una **guarda de bytes** sobre las que no son de las 95.
- **`D.2` MI MUTANTE ERA EL DEFECTUOSO, NO MI JUICIO.** El mutante *A* quitaba
  **una sola** aparicion de la palabra y el texto de la marca la dice **dos
  veces**: la entrada seguia marcada y el mutante **pasaba**. Corregido a quitar
  todas.
- **`D.4` MI LECTOR DE NUMEROS DE FASE LEIA TODO EL FICHERO** y se tragaba **707,
  1096 y 2464** como si fueran fases. **No cambiaba el resultado, pero una vara que
  acierta por suerte no es una vara.** Acotado a la tabla del criterio.
- **`D.7` MI SONDA ERA MAS LAXA QUE SU CLAUSULA Y HABRIA PUBLICADO UNA ALARMA
  FALSA.** Preguntaba si **los dos nombres** de un par estaban en el archivo, cosa
  que da que si para casi cualquier par del catalogo: salia **27 de 27** contra una
  clausula que en realidad **se cumple**. Corregida a comparar **el par** contra
  `nodo_a` y `nodo_b`: da **0 de 27**.
- **`C.1` UN `%d` LITERAL SE ME COLO EN LA PROSA DE UNA SONDA**, y salio impreso
  tal cual en la primera corrida de la `2.b`.
- **`C.2` CITE EL ARBOL DEL PLAN ENTRE COMILLAS INVERSAS, DOS VECES**, que es
  exactamente la `C.1` de la 213. **Me lo conto mi propia guarda del compositor** y
  el texto se reescribio sin comillas.
- **`C.3` CITE UN FICHERO QUE NO EXISTE COMO SI FUERA RUTA DE PRUEBA.** La
  `PARA_ALEXIS.md` **todavia no esta escrita**, y nombrarla entre comillas
  inversas es una ruta que promete prueba apuntando a nada. Cazada por la guarda
  de rutas de mi compositor de la TAREA 3.

## LO QUE PROPONGO PARA LA VUELTA SIGUIENTE

**Va entero en la TAREA 3 de este reporte, que es mi sede.** En una linea: **la
215 es vuelta de bateria y el reparto da 11 tramos, no nueve**; **el carril
`--siguiente` dice hoy que no falta ninguno porque esta viendo los sellos de la
vuelta anterior**; y **el `PARA_ALEXIS.md` de campaña consumada, si se gana, lo
escribe el AUDITOR de la 215 y no su ejecutor**.
