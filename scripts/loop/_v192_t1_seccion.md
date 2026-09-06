### TAREA 1. LOS REGISTROS. **CERRADA.** El acta 192 entra como `R.54`, y el registrador aprendio a leer un lote de caidas escrito EN RANGO y unas caidas propias que viven en parrafos abiertos por su propia clave.

**EL NUMERO NO SE TECLEA.** `scripts/loop/serie_de_registros.py`, recomputando la
serie de sus DOS sedes: **45 entradas, 0 colisiones, 0 huecos, siguiente libre
`R.54`**. El encargo adelanta `R.54` y el instrumento dice `R.54`: **CALZA**.
Salida: `docs/loop/SALIDA_V192_T1A_REGISTRO_R54.txt`.

**LA MAQUINA NO SE CLONA, SE IMPORTA** (`6.6` del acta 172). De la cadena de
registradores se importan las **veinticinco** piezas que ya existen, incluida la
idempotencia entera del registrador de la 189 y las cinco piezas del de la 191.
**Lo propio de este fichero son TRES cosas, y las tres salen de correr la
maquinaria heredada sobre el acta 192 y ver donde se rompe**, no de suponerlas.

**PRIMERA: LAS TRES PREGUNTAS SE CONTESTAN CON TRES MARCAS QUE EL VOCABULARIO NO
TENIA.** `4.8` cierra en `NO MUEVE NINGUNA DEL EJECUTOR, Y MUEVE UNA MIA`, `4.9`
en `SI, Y LO ENCARGO` y `4.10` en `LA CONTRADICCION SE RESUELVE CON LAS REGLAS DE
CORRECCION QUE YA HAY, ASI QUE NO ES PARADA`. **Corrido con el vocabulario
heredado y nada mas (las nueve marcas de la 190 y la 191), TRES titulos saldrian
`SIN DECIR`** y el instrumento haria PARADA sobre un acta perfectamente legible.
Las tres se anaden LITERALES, **las nueve heredadas se conservan aunque hoy no
muerdan**, y **la PARADA por `SIN DECIR` se conserva entera**.

**SEGUNDA: LAS CAIDAS PROPIAS DEL AUDITOR VIVEN EN PARRAFOS CUYA NEGRITA ES LA
PROPIA CLAVE.** El acta abre el lote con `MIAS: DOS, Y UNA ES DE CIFRA PUBLICADA.`
y despues dedica un parrafo a cada una, abiertos por `` `C.1` `` y `` `C.2` `` y no
por una frase de atribucion. **Las tres maquinas viejas sobre esa seccion, medidas
y no supuestas:**

| maquina | ejecutor | auditor | huerfanas | que le pasa |
|---|---:|---:|---:|---|
| `caidas_en_linea()` de la 190 | 2 | **0** | **2** | su guarda `if not c_aud` PARA |
| `caidas_por_seccion()` de la 189 | 0 | 0 | 2 | su patron es de cabeza de linea |
| `caidas_por_numeral()` de la 191 | 0 | 0 | 1 | cuenta `N.M`, y aqui son `C.n` |
| `caidas_por_lead_heredado()`, la de hoy | 2 | **2** | **0** | las dos del auditor entran POR HERENCIA |

El remedio es que **un parrafo cuya negrita ES una clave HEREDA el dueno del
ultimo parrafo de atribucion**, y **la atribucion la siguen haciendo las mismas
marcas de siempre**, importadas y no reescritas. **La herencia no inventa duenos:**
un parrafo con claves y sin lead previo sigue saliendo HUERFANO y sigue haciendo
PARADA, y eso lo prueba la MUTACION 2 del arnes.

**TERCERA, Y ES LA QUE HABRIA PUBLICADO UNA CIFRA FALSA: LAS CAIDAS DEL EJECUTOR
VIENEN EN UN RANGO Y NO ENUMERADAS.** El acta escribe su lote como `` `C.1` a
`C.6` ``, o sea **DOS claves literales para SEIS caidas**. Contar claves distintas
da **2** donde el acta declara **6**, y **esa cifra falsa no la caza ninguna
guarda heredada**, porque las dos claves existen de verdad.
`expandir_rangos_de_clave()` lee el rango y publica **las dos cifras**, y quien
decide es **el numeral de la fila de la tabla de credito, leido de ella**: dice
**6**, el rango expandido da **6**, y **si no calzaran esto seria PARADA**. La
fila de caidas propias dice **2** y los parrafos dan **2**: tambien calza.

**LAS DIEZ ADJUDICACIONES, CONTADAS Y NO TECLEADAS: `4.1` a `4.10`**, patron sin
comillas inversas **10** y patron entrecomillado **0**, **las dos cifras
publicadas**. Reparto por familia: **7 discutibles, 3 preguntas, 0 otras**. De los
discutibles, **7 A FAVOR y 0 EN CONTRA**.

**EL CERO DE `EN CONTRA` SE REPITE POR SEGUNDA ACTA SEGUIDA, Y ESTA VEZ NO SE
VUELVE A PROBAR POR MUTACION: SE DICE CON SU FICHERO**, que es lo que el encargo
manda con esas palabras. **Y el fichero se MIDE en vez de creerse:**
`docs/loop/SALIDA_V191_T1A_MUTACION_REGISTRADOR.txt`,
**disco 6904 bytes | LF 6904 bytes**, con su `sha256` LF y su veredicto leidos
del propio fichero y no de la memoria:

```
   docs/loop/SALIDA_V191_T1A_MUTACION_REGISTRADOR.txt -> disco 6904 bytes | LF 6904 bytes
   sha256 LF: 795c0ec740bdd5cc1e1b821085c0815f899e92fddd33d3d477f375bb99dc223a
   su veredicto, leido del propio fichero: 'VEREDICTO: VERDE'
   la aguja `EN CONTRA` aparece 13 vez(ces) en el arnes
```
 **Si ese
fichero no existiera o midiera cero bytes, este instrumento haria PARADA**: una
ruta que promete prueba sobre un vacio es caida de cifra (`EJECUTOR.md` 1). La
guarda vieja de la 190 (`if not en_contra: PARADA`) corrida sobre el acta 192
**PARARIA**, y ese es el motivo de que el cero se publique como resultado.

**EL AVISO DEL ENCARGO SOBRE EL ORDEN DE LOS `D.n`, MEDIDO CON DOS VARAS Y NO
CREIDO.** El encargo avisa de que en el reporte de la 191 el `D.7` va escrito
ANTES del `D.6`. Medido sobre `docs/loop/reportes/REPORTE_V191.md`:

- **VARA A, la mencion suelta** (primer sitio donde aparece la clave, sea prosa,
  tabla o titulo): `D.2`@71, `D.1`@111, `D.6`@111, `D.3`@842, `D.4`@849,
  `D.5`@856, `D.7`@863. **El aviso por esta vara: NO CALZA.**
- **VARA B, el titulo del discutible** (la linea que EMPIEZA por la clave en
  negrita): `D.1`@828, `D.2`@835, `D.3`@842, `D.4`@849, `D.5`@856, `D.7`@863,
  `D.6`@879. **El aviso por esta vara: CALZA.**

**LA QUE CONTESTA A LA PREGUNTA DEL ENCARGO ES LA B**, porque el encargo habla de
como estan ESCRITOS los discutibles y no de donde se les nombra de pasada: **la
vara A no puede ordenar dos claves que comparten renglon**, y ahi `D.1` y `D.6`
caen en la misma linea de la tabla de tareas. **Las dos se publican y no se elige
la que conviene.**

**LOS TRES HALLAZGOS DE LA SECCION 5 Y LOS TRES QUE CUENTAN FUERA DEL MARCADO.**
Quien decide es **el numeral de la fila**, que dice **3**, y la seccion tiene **3**
claves `5.n`. **El cotejo por subcadena queda al lado como lo que es, una medicion
mas debil, y esta vez resuelve CERO de TRES**: la fila nombra *2832*, *dos arneses
de sujeto vivo* y *cuarta puerta del sello*, y ninguna de esas tres cadenas
aparece dentro de los titulos, que dicen otra cosa. **Va marcado como discutible
`D.1` de este reporte**, porque el numeral y las claves calzan en 3 por una via
que no distingue cuales.

**LA ESPECIE DE CADA CAIDA PROPIA SE LEE DEL PARRAFO Y NO SE SUPONE:** la `C.1` en
la linea 67869 declara `DE CIFRA PUBLICADA` y la `C.2` en la 67879 declara `DE
METODO`. **Si alguna no declarara especie, PARADA.** El encargo dice que una de
las dos es de cifra publicada y el instrumento lo lee del acta: **1 de 2, y es la
`C.1`**.

**Y EL CERO DEL EJECUTOR SIGUE SIENDO DE RACHA Y NO DE CUENTA:** la negrita es
`DEL EJECUTOR: CERO QUE ACUMULEN.` y en el mismo parrafo declara **6** de metodo.
Tratado como cero de CUENTA el reparto del ejecutor cae a **0**, o sea que
confundirlas borraria **2** claves de la cuenta.

**LA IDEMPOTENCIA, PROBADA RE CORRIENDO Y CON LA SEDE MEDIDA ANTES Y DESPUES**,
que es lo que el encargo pide:

```
ANTES  : disco 1020758 bytes | LF 1020758 bytes | sha256 LF 1a82156ef339813d
exitcode del re corrido: 0
DESPUES: disco 1020758 bytes | LF 1020758 bytes | sha256 LF 1a82156ef339813d
IDENTICO: True
```

El re corrido escribe `docs/loop/SALIDA_V192_T1A_RECORRIDO_SIN_ESCRIBIR.txt` y
dice con sus palabras que **NO consume el numero `R.55`**. **Lo que la sede se
movio AL ESCRIBIR la entrada va cercado abajo**, citado de la salida del propio
registrador, porque son cifras de ANTES y una cifra de bytes suelta al lado de
una ruta se lee como una afirmacion sobre esa ruta HOY:

```
L) ESCRITA EN docs/PENDIENTES.md
   la sede pasa de 998216 a 1020758 bytes
   RELEIDA DEL DISCO: la entrada esta byte a byte: SI
```

**Y en el re corrido no se movio un byte**, que es lo que prueba el bloque de
arriba.

**EL CASO POSITIVO POR MUTACION DE LAS TRES COSAS NUEVAS: VERDE**, en
`docs/loop/SALIDA_V192_T1A_MUTACION_REGISTRADOR.txt` (**disco 3568 bytes | LF 3568
bytes**), con **19 casos** y **cuatro mutaciones que CAEN de verdad**: quitarle la
marca a un titulo lo devuelve a `SIN DECIR`; quitarle el rango al parrafo hace que
la cuenta caiga de 6 a 2; quitarle el lead `MIAS` manda las cuatro claves a
HUERFANAS; y tratar el cero de racha como cero de cuenta deja al ejecutor en 0.
**Ninguna comparacion es una constante literal contra si misma.**

**LA DEUDA DE LA SERIE, REMEDIDA AQUI Y NO HEREDADA DEL `R.53`: OCHO actas sin
entrada propia (173 a 180)**, extremo bajo `R.42` cubriendo el acta 172 y extremo
alto `R.43` cubriendo la 181. **El encargo dice OCHO y el instrumento dice OCHO:
CALZA.** No se rellenan: el encargo las deja expresamente fuera.

**LA ENTRADA ARMADA: 22541 bytes en disco y 22541 bytes normalizados a LF**, 218
lineas por `count(NL)` y 219 por `len(split(NL))`, **0 guiones largos o medios**.
