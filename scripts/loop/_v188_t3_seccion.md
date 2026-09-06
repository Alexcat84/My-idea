### TAREA 3. EL CASO E: EL INVENTARIO DE EXENCIONES. CERRADA EN VERDE

**LA PARADA DE LA 187 NO ERA PARADA, Y EL REMEDIO ESTA PUESTO.** El acta 188,
punto `7.1`, lo adjudica con regla escrita: no habia dos reglas vigentes
peleandose, habia **un esperado tecleado en la vuelta 186** y **una orden escrita
en el encargo de la 187** que lo dejo viejo. **Y el `1` no se ha cambiado por un
`2`**, porque eso deja otra cifra tecleada que la proxima exencion volveria a
dejar vieja.

#### 3.a EL CASO E DEJA DE CONTAR UN TEXTO Y PASA A NOMBRAR

**EL CAMBIO VA DENTRO DEL PROPIO FICHERO**,
`scripts/loop/vuelta186_tarea2c_mutacion_cierre_tardio.py`, **sin clonarlo y sin
escribir un arnes nuevo para esquivarlo**, y **quien lo autoriza queda escrito en
su docstring**: acta 188, punto `7.1`.

**LA LISTA AUTORIZADA VIVE EN EL ARNES Y HOY TIENE DOS ENTRADAS**, cada una con la
vuelta y la decision que la autorizo, y con la **marca literal** que prueba que
esa exencion exige su declaracion:

| guarda eximida | vuelta | decision que la autoriza | marca de que exige su declaracion |
|---|---:|---|---|
| `toda cifra de bytes y todo sha con su pareja` | 178 | acta 186 punto 7.2, contestando la `P.2`: las cifras sin pareja de un reporte viejo NI SE EXIMEN NI SE REESCRIBEN, SE DECLARAN | `declaracion_de_cifras_sin_pareja` |
| `seccion4_que_no_calza` | 187 | encargo de la vuelta 187, TAREA 5.b, respuesta del acta 187 a la `P.2`: en el carril de cierre tardio la guarda de la `2.d` NO bloquea pero SE DECLARA | `if not dentro or sin_declarar:` |

**Anadir una tercera es ahora un acto visible y no un descuido.**

**EL INVENTARIO, LEIDO DEL FUENTE Y NO TECLEADO**, con el sello del sujeto al lado
(`scripts/loop/cerrar_reporte.py`, **97163 bytes normalizados a LF, 1844 lineas**,
`sha256` LF `2e37089d0389e67e`):

- **linea 1748**, forma `columna`, nombre `toda cifra de bytes y todo sha con su
  pareja`
- **linea 1813**, forma `if`, nombre `seccion4_que_no_calza`
- **`CIFRA exenciones halladas en el fuente: 2`**

**Y LA CUENTA VIEJA SE SIGUE PUBLICANDO Y YA NO ES EL VEREDICTO:** `not tardio`
aparece **2** veces. **Una cuenta de dos no distingue si las dos son las de la
lista o si una se cambio por otra**, y por eso el caso E queda **mas apretado**,
no mas flojo: exige tres cosas donde antes exigia una.

- **`(1) EXENCIONES QUE NO ESTAN EN LA LISTA AUTORIZADA: 0`**
- **`(2) DE LA LISTA QUE HAN DESAPARECIDO DEL FUENTE: 0`**
- **`(3) EXIMIDAS QUE NO EXIGEN SU DECLARACION: 0`**
- **`ANONIMAS (que es peor que las tres): 0`**

**LOS TRES ROJOS SE PRUEBAN, SOBRE FUENTES FABRICADOS EN MEMORIA Y NUNCA SOBRE EL
FICHERO VIVO**, y los tres CAEN:

- **(1) aparece una tercera exencion que nadie autorizo** -> `intrusas 1
  ['(sin nombre)']`, ROJO **SI**.
- **(2) desaparece del fuente una de las dos de la lista** -> `ausentes 1 ['toda
  cifra de bytes y todo sha con su pareja']`, ROJO **SI**.
- **(3) una eximida deja de exigir su declaracion** -> `mudas 1
  ['seccion4_que_no_calza']`, ROJO **SI**.

**Y LA MUTACION SOBRE EL FUENTE DE VERDAD, QUE ES LA QUE PRUEBA QUE EL VEREDICTO
NO ES UNA CONSTANTE:** con la lista autorizada mutada a **una** entrada, el cotejo
saca `intrusas 1 ['seccion4_que_no_calza']` y **CAE**.

**LA CORRIDA ENTERA, PEGADA POR SUS CIFRAS.**
`docs/loop/SALIDA_V186_T2C_MUTACION_CIERRE_TARDIO.txt` (**7544 bytes por las dos
convenciones**, `sha256` LF `be4edc90f2889552`): **`CIFRA casos: 22 | pasan:
22`**, **`CIFRA casos que CAEN al mutar su esperado: 21 de 21`**, **`CIFRA fallos:
0`**, **`VEREDICTO: VERDE`**, **exitcode 0**.

**LOS OTROS CASOS NO SE TOCARON, Y LA PRUEBA ES SU CUENTA:** el arnes pasa de
**18 casos con 17 que caen** a **22 casos con 21 que caen**. **Son los mismos mas
cuatro**, y los cuatro nuevos son las tres pruebas de rojo mas la mutacion de la
lista autorizada.

#### 3.b LA SALIDA QUE ENVEJECE SOLA, Y SU REMEDIO DE UNA LINEA

**QUE SE HIZO:** toda salida de arnes que publique numeros de linea de un fichero
vivo publica al lado el **`sha256` de ese fichero**, para que un diff futuro diga
**si se movio el sujeto o se movio el arnes** en vez de dejarlo a que alguien lo
deduzca.

**Y AQUI VA UNA MEDICION QUE ACOTA EL ENCARGO EN VEZ DE DARLO POR HECHO.** El
encargo dice *"hazlo en los arneses que ya lo publican (los cuatro de la 186
juzgan `cerrar_reporte.py`)"*. **Se midio antes de tocarlos, y de los cuatro solo
DOS publican numeros de linea del fichero vivo:**

| arnes de la 186 | publica numeros de linea de `cerrar_reporte.py` | sello anadido |
|---|---|---|
| `vuelta186_tarea2a_mutacion_pieza4.py` | **SI** (lineas 770 y 1446 en su salida) | **SI** |
| `vuelta186_tarea2b_mutacion_pieza2_cercas.py` | no (su salida no publica ninguna) | no |
| `vuelta186_tarea2c_mutacion_cierre_tardio.py` | **SI** (1748 y 1813, desde hoy) | **SI** |
| `vuelta186_tarea2d_mutacion_seccion4.py` | no (sus lineas son de reportes FABRICADOS) | no |

**Ponerselo a los que no lo necesitan habria movido dos salidas selladas para
nada**, y eso se dice en vez de hacerse callando.

**EL `numstat` DE LO QUE SE MOVIO AL HACERLO, PUBLICADO SALGA LO QUE SALGA:**

```
4	0	docs/loop/SALIDA_V186_T2A_MUTACION_PIEZA4.txt
50	11	docs/loop/SALIDA_V186_T2C_MUTACION_CIERRE_TARDIO.txt
23	0	scripts/loop/vuelta186_tarea2a_mutacion_pieza4.py
223	12	scripts/loop/vuelta186_tarea2c_mutacion_cierre_tardio.py
```

**Y LOS OTROS DOS DE LA 186 SALEN EN CERO FILAS**, medido y no supuesto:
`git diff --numstat` sobre `vuelta186_tarea2b_mutacion_pieza2_cercas.py`,
`vuelta186_tarea2d_mutacion_seccion4.py` y sus dos salidas devuelve **0 filas**.
`SALIDA_V186_T2A_MUTACION_PIEZA4.txt` cierra en **3906 bytes por las dos
convenciones**, `sha256` LF `2b444ffe193d27f9`, y su arnes sigue en
**`CIFRA fallos: 0`, `VEREDICTO: VERDE`**, exitcode **0**.

#### 3.c LA DOBLE CORRIDA NO RE CORRE UN ARNES QUE YA SALIO EN ROJO. ES LA `C.3`

**LA CAIDA, QUE LEVANTO EL AUDITOR Y QUE NO TRAJE.** La letra dice, sobre un arnes
ya sellado que cae en rojo: *"te detienes ahi, lo traes con su salida entera, **sin
re-correrlo** y sin arreglarlo"*. En la 187 ese arnes se corrio **dos veces mas**
dentro de la doble corrida de la 5.a, y **no hubo choque de ordenes**: la 5.a pide
*"corre cada arnes NUEVO dos veces"*, y ese no era nuevo.

**EL REMEDIO, EN `scripts/loop/vuelta188_tarea3c_nomina.py`** (clon declarado del
`vuelta187_tarea5a_nomina.py`): la doble corrida **excluye explicitamente
cualquier arnes que ya haya salido en rojo en esa misma vuelta**, y **lo dice en
su salida** con **el nombre del excluido, la ruta de su salida en rojo y el
motivo**. **Una exclusion muda seria peor que el problema.**

**LOS ROJOS NO SE TECLEAN:** salen de un registro en disco,
`docs/loop/ROJOS_DE_LA_VUELTA_188.txt`, una linea por arnes con la forma
`script | ruta de su salida en rojo | motivo`. **Si el fichero no existe, la
exclusion es vacia Y ESO TAMBIEN SE DECLARA**, con esas palabras: un cero que no
se publica no se puede auditar.

**Y QUEDA ESCRITA LA LETRA QUE EL ACTA 188 ADJUDICA EN SU `5.3`, para que no se
re-litigue: un arnes sellado en rojo detiene AL ARNES, no a la vuelta**; la vuelta
se cierra con la parada declarada.

**ARNES OBLIGATORIO, Y NACE EN ESTA VUELTA:**
`scripts/loop/vuelta188_tarea3c_mutacion_exclusion_por_rojo.py`. Salida:
`docs/loop/SALIDA_V188_T3C_MUTACION_EXCLUSION_POR_ROJO.txt` (**3565 bytes por las
dos convenciones**, `sha256` LF `622b67673e6d75f4`), **`CIFRA casos: 11 | pasan:
11`**, **`CIFRA casos que CAEN al mutar su esperado: 11 de 11`**, **`CIFRA fallos:
0`**, **`VEREDICTO: VERDE`**, exitcode **0**. Cinco casos: **(A)** un registro
vacio no excluye a nadie, probado con tres formas de vacio; **(B)** un registro
que nombra un arnes lo excluye y **el excluido desaparece de la lista que se
corre**; **(C)** la exclusion **no es muda**: nombre, ruta del rojo y motivo, los
tres; **(D)** la comparacion es **por nombre de fichero y no por ruta completa**,
probado con barras invertidas, sin directorio y con directorio de mas, y con un
nombre ajeno que **no excluye a nadie**; **(E)** una linea sin motivo **excluye
igual pero lo dice**, `(sin motivo declarado)`, **sin inventarle uno**.

**LA DOBLE CORRIDA DE VERDAD NO CORRE AQUI:** corre al cerrar la vuelta, cuando ya
existan todos los arneses que nacen hoy, y su salida es
`docs/loop/SALIDA_V188_T3C_NOMINA.txt`. **Se dice para que nadie la busque en esta
seccion.**
