### TAREA 5. LOS TRES INSTRUMENTOS QUE FALTAN (adjudicaciones 6.6, 6.9 y 6.12)

**5.a EL ARCHIVADOR SE ENCHUFA, Y SE ENTREGO ANTES QUE EL RESTO PORQUE VIVE
DENTRO DEL ESQUELETO.** Nace `scripts/loop/paso0_archivar_anterior.py`, **con
nombre estable y sin numero de vuelta** para que el enchufe no se pierda en el
proximo clon, y `vuelta171_esqueleto_reporte.py` lo llama como **PASO 0**. **El
esqueleto se niega a escribir** si el reporte anterior no esta a salvo, y la
guarda tiene cuatro clausulas:

| clausula | que mira |
|---|---|
| (a) | el archivador no sale VERDE para la vuelta anterior |
| (b) | no existe `docs/loop/reportes/REPORTE_V<N>.md` |
| (c) | ese fichero existe pero lleva el reporte de OTRA vuelta |
| **(d)** | **el `REPORTE.md` que se va a PISAR no esta guardado byte a byte en el archivo**, cotejando los dos sha256 |

**LA (d) ES LA QUE CONVIERTE ESTO EN UNA GUARDA Y NO EN UN RECORDATORIO:** las
tres primeras se cumplen con un archivo VIEJO, y solo la cuarta mira lo que se va
a destruir.

**CASO POSITIVO POR MUTACION:**
`scripts/loop/vuelta171_tarea5a_mutacion_enchufe.py`, salida
`docs/loop/SALIDA_V171_T5A_MUTACION_ENCHUFE.txt`, **exit 0**: **10 casos, 10
pasan, 10 caen al mutar el esperado**. Tumba la guarda en sus modos (b), (c) y
(d), comprueba que **un solo byte de diferencia ya la tumba**, y corre el caso
verde contra el repo real en modo solo comprobacion, sin escribir. **Y la corrida
real lo confirmo en la 1.d**: los dos sha256 dieron `0b85f30e9c78e2b4` y el
esqueleto escribio.

**5.b EL CENSO DEL CAMPO `forma`, Y LA RESPUESTA ES QUE NO HAY VOCABULARIO.**
Instrumento `scripts/loop/vuelta171_tarea5_censo_y_barrido.py`, salida
`docs/loop/SALIDA_V171_T5BC_CENSO_Y_BARRIDO.txt`, **exit 0**. **672 entradas,
672 con `forma` no vacio, 0 sin el.** Tres varas, para no depender de una sola
forma de mirar:

**Vara (i), la CABEZA del campo: 22 cabezas distintas, y solo OCHO abren en
mayusculas.**

| cabeza | entradas |
|---|---:|
| `MEZCLADO` | 5 |
| `MEDIDO` | 3 |
| `DOS` | 2 |
| `PURO` | 2 |
| `SUB-PURO` | 2 |
| `FUNDIDA` | **1** |
| `PROVISIONAL` | 1 |
| `SIETE` | 1 |
| las otras 14 cabezas abren en minusculas | **655** (`componente` 556, `ids` 53, `defecto` 14, `figura` 13, `cribado` 10, y nueve mas con 1 cada una) |

**Vara (ii), todo token en mayusculas de 4 letras o mas en CUALQUIER sitio del
campo: 43 tokens distintos**, y la lista incluye palabras que no son formas
(`VIVOS`, `SOLO`, `TIENE`, `MISMA`, `HABLAN`).

**Vara (iii), la nomina escrita en las paginas de doctrina: NO EXISTE, y esta vez
la busqueda esta corrida y se publica.** En `docs/BANCO_DE_TEXTOS.md` y
`docs/plan/BANCO_DEL_PLAN.md`, las frases *"nomina de formas"*, *"el campo
`forma`"*, *"campo forma"*, *"formas posibles"* y *"valores de `forma`"* dan
**0 apariciones cada una en las dos paginas**.

**LO QUE EL CENSO SOSTIENE, Y NI UNA PALABRA MAS: NO HAY VOCABULARIO CERRADO
PARA EL CAMPO `forma`.** No es que `FUNDIDA` este fuera de una nomina: **es que
no hay nomina**. El campo es prosa libre en el **97,5 por ciento** de las
entradas (655 de 672 abren en minusculas). **Sube al fundador como hallazgo, que
es la rama que la `6.9` deja abierta**, y **la palabra se queda** como la propia
adjudicacion manda: describe un hecho verificado y ninguna regla escrita la
prohibe.

**Y UNA CORRECCION QUE EL CENSO OBLIGA A HACERLE AL `D.5` DE LA VUELTA 170**,
que decia que el vocabulario de la casa era *"`MEZCLADO`, `SUB-PURO`, `PARTIDO`,
`PROVISIONAL`, `REPITE`"*: medido, **`REPITE` no aparece en NINGUNA de las 672
entradas**, ni como cabeza ni como token. **La lista que se cito como vocabulario
de la casa traia una palabra que la casa no usa.** No mueve ninguna cifra
publicada; se declara y ya.

**5.c LOS 8 PARES SIN LEER: NINGUNA OPERACION LOS RECOGE, Y AHORA ESTA MEDIDO.**
Los 8 pares **no se teclean**: se computan con el resolutor delante (`P.1`) desde
los 10 miembros escritos del racimo, que colapsan a **7 vivos** (3 colapsos,
todos a `comprension_capacidades_limitaciones_ia`), **21 pares posibles, 13
leidos, 8 sin veredicto**. Los ocho, uno a uno:

| # | par |
|---:|---|
| 1 | `alineacion_etica_ia_negocio` contra `comprension_capacidades_limitaciones_ia` |
| 2 | `comprender_alineacion_etica_ia` contra `comprension_capacidades_limitaciones_ia` |
| 3 | `comprender_alineacion_etica_ia` contra `human_in_the_loop_ia` |
| 4 | `comprender_alineacion_etica_ia` contra `mitigar_falling_asleep_wheel` |
| 5 | `comprender_alineacion_etica_ia` contra `principio_humano_en_el_loop` |
| 6 | `comprender_alineacion_etica_ia` contra `riesgo_sobredependencia_ia` |
| 7 | `comprension_capacidades_limitaciones_ia` contra `mitigar_falling_asleep_wheel` |
| 8 | `comprension_capacidades_limitaciones_ia` contra `riesgo_sobredependencia_ia` |

**EL RESULTADO: 0 de los 8 pares aparece ENTERO en ninguna de las 71 fichas**, y
mas fuerte todavia, **ninguno de los 7 nodos aparece en `nodos`, `preservar`,
`eliminar` ni `superviviente` de ninguna ficha**.

**Y UN CERO SOLO VALE SI EL BARRIDO SABIA BUSCAR** (`EJECUTOR.md` 9), asi que va
con contraprueba (`docs/loop/SALIDA_V171_T5C_CONTRAPRUEBA.txt` y
`docs/loop/SALIDA_V171_T5C_BARRIDO_CORREGIDO.txt`): **los 7 ids existen en el
grafo, 7 de 7, y ninguno esta deprecado**; el barrido si encuentra fichas cuando
las hay; y el universo real de los cuatro campos son **251 ids distintos tras
resolver** de **416 valores** que resuelven a id.

**LA CONTRAPRUEBA DESTAPO ADEMAS DOS COSAS QUE MI PRIMERA PASADA NO DECIA, Y LAS
DOS SE PUBLICAN:**

1. **`comprender_alineacion_etica_ia` SI esta nombrado en una ficha**, aunque no
   en los cuatro campos operativos: en `OP-E-02.nota`, como *"el SUELTO del
   racimo de la supervision de la IA"*. O sea que **el nodo esta visto, pero no
   recogido por ninguna operacion**.
2. **El racimo, por su nombre, aparece en CINCO fichas**: `OP-F-02.evidencia`,
   `OP-E-02.nota`, `OP-L-01.verificacion`, `OP-L-02.nota` y `OP-I-01.nota`.
   **Un cero de ids no es un cero de menciones**, y decir solo lo primero habria
   sido cierto y engañoso a la vez.

**LO QUE NO DIGO, PORQUE NO LO HE MEDIDO: si son backlog nuevo.** Lo medido es
que **ninguna operacion escrita los recoge en sus campos operativos**. Ponerles
la etiqueta *backlog* es una decision de doctrina y va en `P.3`.

**Y UNA CAIDA MIA, DECLARADA CON SU NOMBRE Y CON EL TEXTO VIEJO SIN TOCAR** (va
como `CAIDA 1` de la seccion 8): mi primera version del barrido publico *"345
nodos distintos que esos cuatro campos nombran"*. **Esa cifra no es de nodos**:
`preservar` y `eliminar` guardan **prosa** ademas de ids (94 de 510 valores no
resuelven a ningun id, y `preservar` no trae **ni uno** real), y mi propio caso
de control lo destapo al imprimir como *nodo* una frase entera. **La cifra de
aciertos, 0 de 8, no se mueve** (una prosa nunca iba a ser igual a un id); lo que
cambia es lo que se puede DECIR del universo. La salida vieja se queda entera y
sin tocar.
