### TAREA 2. LA GUARDA DEL SUJETO CONGELADO. CERRADA, Y CIERRA EN ROJO CON SU NOMBRE

**EL VEREDICTO DE ESTA TAREA ES `ROJO POR DEUDA DECLARADA`, EXITCODE 2, Y ESE ROJO
SE TRAE SIN APAGARLO**, que es lo que el encargo manda con esas palabras. No se
afloja ninguna guarda para conseguirlo.

**LOS FICHEROS, MEDIDOS EN DISCO POR LAS DOS CONVENCIONES:**

| fichero | bytes en disco | bytes en LF | lineas | `sha256` LF |
|---|---:|---:|---:|---|
| `scripts/loop/vuelta190_tarea2a_simulacion.py` | 11228 | 11228 | 226 | `6105d791a048fb7e` |
| `scripts/loop/vuelta190_tarea2b_mutacion_deuda_y_fallo.py` | 17942 | 17942 | 338 | `7c4bfef637e33c40` |
| `scripts/loop/vuelta190_tarea2_nomina.py` | 11615 | 11615 | 248 | `a14806a6c48a76df` |
| `scripts/loop/verificar_mutaciones_viejas.py` (el sujeto tocado) | 144320 | 144320 | 2533 | `4461658cb4715172` |
| `docs/loop/SALIDA_V190_T2A_SIMULACION.txt` | 4621 | 4621 | 83 | `e409868bd13f1164` |
| `docs/loop/SALIDA_V190_T2B_MUTACION_DEUDA_Y_FALLO.txt` | 6763 | 6763 | 95 | `bc1f0f27849ffced` |
| `docs/loop/SALIDA_V190_T2_NOMINA.txt` | 4510 | 4510 | 77 | `82cc350f1dfbd694` |

El fuente tocado entra en la vuelta con **131802 bytes en `HEAD`** (leido con
`git cat-file -s`) y sale con **144320 bytes en disco y 144320 normalizado a LF**.

#### (a) LA SEPARACION, Y LA VARA VA ESCRITA ANTES DE MEDIR

**LA SIMULACION PREVIA CORRIO SOBRE COPIA EN MEMORIA Y ANTES DE TOCAR EL FUENTE**,
y lo probo en vez de prometerlo: su bloque F publica
`git status sobre el fuente que se va a tocar: 0 fila(s)`. La vara quedo escrita
en esa salida **antes** de medir nada:

- **marcas literales (7):** `GIT SHOW`, `CAT-FILE`, `COMMIT`, `SUJETO_FIJO`,
  `SHA256`, `NO SE TOCA`, `NO SE ESCRIBE`. Las cinco primeras son formas de la
  casa de nombrar un sujeto que no se mueve; las dos ultimas son la declaracion
  expresa de que el fichero vivo no se toca.
- **ventana:** mas o menos **3** lineas, sobre LA MAQUINA (el fichero sin su
  docstring de modulo), que es donde `anclaje_de()` ya busca las huellas de vivo.
- **regla:** TODAS las apariciones con marca da MOTIVO ESCRITO; ALGUNA sin marca
  da SIN MOTIVO ESCRITO. **El lado seguro es ese:** una apertura del fichero vivo
  sin explicar es deuda, no decision.

**LA MEDICION, QUE ES LO QUE EL ENCARGO PIDE CON ESAS PALABRAS** (*mide cuantas de
las tres traen motivo escrito, no lo supongas*), contada de
`docs/loop/SALIDA_V190_T2_NOMINA.txt`:

| entrada `NO DECIDIBLE` | apariciones en la maquina | marcas halladas | motivo escrito |
|---|---:|---|---|
| `vuelta186_tarea2c_mutacion_cierre_tardio.py` | 1 (linea 486) | `NO SE TOCA`, `NO SE ESCRIBE` | **SI** |
| `vuelta187_tarea4_mutacion_dos_convenciones.py` | 2 (lineas 140 y 144) | `GIT SHOW`, `COMMIT` / `COMMIT` | **SI** |
| `vuelta188_tarea4_mutacion_cobertura_parejas.py` | 1 (linea 15) | `COMMIT` | **SI** |

**LA RESPUESTA A LA `P.1`, MEDIDA Y NO SUPUESTA: LAS TRES TRAEN MOTIVO ESCRITO.
`SUJETO VIVO` 0, `NO DECIDIBLE CON MOTIVO ESCRITO` 3, `NO DECIDIBLE SIN MOTIVO
ESCRITO` 0**, y **la suma de las tres es 3, que es exactamente lo que devuelve la
guarda sin separar: CALZA**. Los tres ceros van escritos y no omitidos.

**Y NO SE EXIME A NADIE.** Las tres listas siguen contando para el veredicto y
`CASOS_DECLARADOS` no se abre: lo unico que cambia es que el rojo dice de que
especie es. **La guarda vieja tampoco se toca:** `guarda_del_sujeto_congelado()`
sigue devolviendo tuplas de **3** campos, que es lo que llaman los tres arneses
viejos, y eso se comprueba en el bloque H del arnes.

#### (b) LA GUARDA VUELVE AL VEREDICTO, Y SE PRUEBA QUITANDOLE LA PIEZA

`scripts/loop/vuelta190_tarea2_nomina.py` publica la comparacion que hace visible
lo que la `4.6` arregla, contada de su propia salida:

| | clase | exitcode |
|---|---|---:|
| **CON la guarda DENTRO del veredicto (hoy)** | **`ROJO POR DEUDA DECLARADA`** | **2** |
| SIN la guarda, que es lo que el `D.5` de la 189 hacia | `VERDE` | 0 |

**LAS DOS SON DISTINTAS.** Si fueran iguales, la guarda no estaria enchufada y
esto no probaria nada. **Con el `D.5` puesto, esta misma vuelta habria cerrado en
VERDE con tres entradas en deuda**, que es literalmente lo que el acta 190
describe: *deja sin sintoma al que solo mire el veredicto*.

**LOS TRES CODIGOS, Y NINGUNO AFLOJA:** `VERDE` 0, `ROJO POR FALLO` 1,
`ROJO POR DEUDA DECLARADA` 2. **Los dos rojos siguen siendo distintos de cero**,
asi que nadie que compruebe `!= 0` cambia de conducta. **La precedencia va escrita
y no es discutible: el fallo gana.** Publicar deuda habiendo un arnes caido seria
la misma degradacion silenciosa, pero al reves. Y `SUJETO VIVO` cuenta como
**fallo y no como deuda**, porque un arnes que abre el fichero de hoy sin nada que
lo module no mide su maquina, mide el dia.

#### EL ARNES, Y LOS DOS ROJOS QUE ME CAZO A MI ANTES DE DEJARME CERRAR

`scripts/loop/vuelta190_tarea2b_mutacion_deuda_y_fallo.py`, **8 bloques, CIFRA
casos que CAEN 0, CIFRA mutaciones que NO cayeron 0, VEREDICTO VERDE**, contado de
`docs/loop/SALIDA_V190_T2B_MUTACION_DEUDA_Y_FALLO.txt`. Sus mutaciones caen todas,
y la que decide es la del bloque F: **con la pieza el veredicto es
`ROJO POR DEUDA DECLARADA` y sin ella es `VERDE`**.

**Y LAS DOS COSAS QUE LA CASA ME CAZO A MI, DECLARADAS EN VEZ DE ARREGLADAS EN
SILENCIO:**

1. **MI PROPIO ARNES ESCRIBIA UNA SALIDA QUE CAMBIABA SOLA.** La doble corrida de
   `vuelta190_tarea2_nomina.py` la tumbo: **mismos 6650 bytes y `sha256` distinto
   en cada corrida** (`4678b6db...`, `15fc1632...`, `5c00bdde...`). La causa,
   medida: el arnes imprimia la ruta de su temporal, y `tempfile.mkdtemp` le pone
   un sufijo al azar. **Corregido publicando el prefijo estable en vez de la ruta
   entera**, y remedido: las dos corridas dan ahora **6763 bytes y el mismo
   `sha256` `bc1f0f27849ffced`**.
2. **MI ARNES NUEVO NO ESTABA EN LA NOMINA.** `arneses_que_faltan()` lo acuso con
   su nombre. La regla de la casa es que **un arnes entra en la nomina en su misma
   vuelta** (acta 176, punto 7.2), asi que entran los **dos** que nacen hoy y **la
   nomina pasa de 125 a 127**. **NO SE PODA NADA**: el fundador RECHAZO podarla el
   5 sep 2026.

**Y UNA TERCERA, QUE ES LA `4.9` APLICADA A MANO ANTES DE TENERLA EN CODIGO.** Re
correr `vuelta179_tarea4_juzgar_sujeto.py` (uno de los tres arneses viejos que
usan esta guarda, corrido para comprobar que no rompo nada) **piso una salida
sellada de la vuelta 179**: `docs/plan/SUJETO_CONGELADO_VEREDICTOS.jsonl` paso de
**17 filas a 3**. Se aplico la doctrina de la `4.9` con la mano: **el corte nuevo
al lado con su nombre y su vuelta** (`docs/plan/SUJETO_CONGELADO_VEREDICTOS_V190.jsonl`,
**4356 bytes en disco y 4356 normalizado a LF**, **3 filas**, `sha256` LF
`8f7ad886cf93ca6d`) y **el original restaurado con `git checkout --`** y remedido:
**20956 bytes en disco, 20939 normalizado a LF, 17 filas**, `sha256` LF
`4fa7413a97727357`. **El corte nuevo interesa y por eso se conserva:** dice que la
deuda de aquella vuelta bajo de 17 a 3.

**LOS TRES ARNESES VIEJOS QUE USAN ESTA GUARDA SIGUEN VERDES**, corridos por mi
despues del cambio: `vuelta178_tarea1e_mutacion_higiene.py` (exit 0, 18 casos),
`vuelta180_tarea2c_mutacion_cableado.py` (exit 0, 10 comprobaciones, 0 fallan) y
`vuelta179_tarea4_juzgar_sujeto.py` (exit 0).

**EL CARRIL `--sujeto-congelado` DEL PROPIO INSTRUMENTO**, corrido por mi, cierra
con **`ROJO POR DEUDA DECLARADA`** y **`CIFRA exitcode de este carril: 2`**.

**GATE 0 AL CERRAR LA TAREA:** `GATE 0: OK`, motor **25/25**, `tsc` exit **0**, y
`git diff --numstat -- dataset/` en **0 filas**.
