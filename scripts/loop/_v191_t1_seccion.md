### TAREA 1. LOS REGISTROS. CERRADA EN VERDE.

**EL ACTA 191 ENTRA EN LA SERIE COMO `R.53`, Y EL NUMERO NO ESTA TECLEADO.** Lo
computa `scripts/loop/serie_de_registros.py` recomputando la serie de sus DOS
sedes: **44 entradas, 0 colisiones, 0 huecos, siguiente libre `R.53`** al entrar,
y **45 entradas, 0 colisiones, 0 huecos, siguiente libre `R.54`** despues de
escribir. El encargo decia `R.53` y **el instrumento tambien lo dice: CALZA**.

**EL INSTRUMENTO:** `scripts/loop/vuelta191_tarea1a_registrar_acta191.py`.
Salidas, las tres medidas y ninguna vacia:
`docs/loop/SALIDA_V191_T1A_MUTACION_REGISTRADOR.txt` (disco 6904 bytes | LF 6904 bytes),
`docs/loop/SALIDA_V191_T1A_SIMULACION.txt`,
`docs/loop/SALIDA_V191_T1A_REGISTRO_R53.txt` (disco 9585 bytes | LF 9585 bytes) y
`docs/loop/SALIDA_V191_T1A_RECORRIDO_SIN_ESCRIBIR.txt` (disco 9965 bytes | LF 9965
bytes).

**LO QUE ESTE REGISTRADOR TUVO QUE ESTRENAR, Y LAS CUATRO SALEN DE CORRER LA
MAQUINA HEREDADA SOBRE EL ACTA 191 Y VER DONDE SE ROMPE, NO DE SUPONERLO.** Las
cifras salen de `SALIDA_V191_T1A_REGISTRO_R53.txt`, bloques D, E, F y G:

| lo que estrena | la medicion que lo obliga | fuente |
|---|---|---|
| el cero de `EN CONTRA` no para | discutibles **6**, A FAVOR **6**, EN CONTRA **0**; la guarda vieja `if not en_contra: PARADA` de la 190 **PARARIA** sobre esta acta | bloque D |
| tres marcas nuevas de pregunta contestada | con el vocabulario de la 190 y nada mas, **3** titulos saldrian `SIN DECIR` y el instrumento pararia | bloque D |
| las caidas se cuentan por clave `N.M` y no por `C.n` | el patron `C.n` en linea da **0** sobre la seccion 6; `caidas_en_linea()` de la 190 saca **(0, 0, 0)** y `caidas_por_seccion()` de la 189 tambien | bloque F |
| la fila de la tabla se parte tambien por `,` | partiendo solo por `;` da **1** pieza y casa con **0**; partiendo por `;` y `,` da **3** piezas y casa con **1** | bloque E |

**Y LA CUARTA MERECE SU FRASE, PORQUE ES DONDE MAS FACIL ERA MENTIR:** que el
cotejo por subcadena casara **1 de 3** no autoriza a ensanchar el cotejo hasta que
diga lo que conviene. **Quien decide cuantos hallazgos cuentan fuera del marcado
es el numeral de la propia fila, leido de ella y no tecleado: dice `3`, y la
seccion tiene `3` claves `5.n`.** El cotejo por subcadena queda publicado al lado
**como lo que es, una medicion mas debil**, porque el acta parafrasea (*"la
restauracion que no restaura"*) donde el titulo dice otra cosa (*"`git checkout
--` NO ES RESTAURACION BYTE A BYTE"*).

**LAS CIFRAS QUE LA ENTRADA REGISTRA, TODAS CONTADAS DEL ACTA ACOTADA (lineas
67365 a 67620) Y NINGUNA DEL ENCARGO:** **9** adjudicaciones `4.1` a `4.9` (con
el patron entrecomillado del acta 188 dando **0** y el suelto dando **9**, las dos
publicadas), **6** discutibles `D.1` a `D.6` **los seis A FAVOR**, **0** EN
CONTRA, **3** preguntas contestadas (`4.7` que nombra `P.1`, `4.8` que nombra
`P.2`, `4.9` que nombra `P.3`), **3** hallazgos `5.n` y **los tres** cuentan fuera
del marcado, **1** caida propia del auditor y **3** del ejecutor, **0**
huerfanas.

**LA CAIDA DEL AUDITOR VA ESCRITA COMO UNA Y NO OMITIDA**, bajo su negrita
literal `MIAS: UNA, DE METODO, Y ES LA `5.3``. **Y las tres del ejecutor van con
su cero de racha intacto:** la negrita es `DEL EJECUTOR: CERO QUE ACUMULEN.`, que
es un cero de RACHA y **no neutraliza**. Medido: tratado como cero de CUENTA el
reparto sale **ejecutor 0**, o sea que confundirlas **borraria las 3**.

**Y UNA COSA QUE SE MIDE PORQUE ERA LA TRAMPA:** el parrafo del ejecutor nombra
`5.2` **dos veces**, la segunda para decir que la etiqueta duplicada *no se la
cuenta a el*. Contando **apariciones** salen **4**; contando **claves distintas**
salen **3**, que es lo que el acta declara. Por eso se deduplica por parrafo.

**LA METRICA DE CREDITO DE LA SECCION 7, PEGADA ENTERA DEL FICHERO Y NO
RESUMIDA.** Son **8** filas de datos, contadas por `filas_de_la_metrica()` y no
tecleadas; salen del bloque G de `SALIDA_V191_T1A_REGISTRO_R53.txt`:

| | esta vuelta | acumulado |
|---|---:|---:|
| relecturas | 1 | **326** |
| puestos | 30 aislados, **30 de solape TOTAL a proposito: control, NO cobertura nueva** | **1.006** |
| discrepancias DENTRO del marcado | **9** (las nueve en mis dudosos) | **42** |
| discrepancias y hallazgos FUERA del marcado | **3** (la marca contra la dificultad medida, la etiqueta duplicada, la restauracion que no restaura) | **151** |
| caidas propias del auditor | **1**, de metodo (`5.3`) | ninguna repetida: no abre racha |
| caidas del ejecutor que ACUMULAN por cifra publicada | **0** | **racha de cifra publicada: 0** |
| caidas del ejecutor de reporte | **0** | **racha de reporte: 0** |
| caidas del ejecutor de metodo, registradas y sin racha | **3** (`5.1`, `5.2`, `5.3` del reporte) | |

**LA FILA DE PUESTOS VA CON SU NOTA, QUE ES LO QUE EL ENCARGO MANDA, Y AQUI HAY
UNA CORRECCION DECLARADA SIN BORRAR LO QUE CORRIGE.** La guarda nacio exigiendo
el literal `SOLAPE TOTAL` **tal cual**, que es como lo escribe el encargo, y
**PARO el instrumento en su primera corrida**: el acta escribe `solape TOTAL`, con
minuscula. **Se cambio a comparar en mayusculas y a publicar el literal real**, y
**las dos cifras se publican**: TAL CUAL da **NO**, en mayusculas da **SI**, y lo
que el acta escribe de verdad es `'solape TOTAL'`. Exigir la caja habria hecho
parar el instrumento **por una mayuscula**, que es lo contrario de lo que la
guarda existe para cazar. El caso de mutacion nuevo corre las dos cajas.

**EL CASO POSITIVO POR MUTACION: VERDE, 0 casos que caen y 0 mutaciones que no
cayeron**, en seis bloques (`SALIDA_V191_T1A_MUTACION_REGISTRADOR.txt`). Las que
importan, cada una con su mutacion corrida:

- **el acta fabricada que SI lleva un `EN CONTRA`**: la cuenta lo ve (**1**), y
  mutado el esperado a 0, **CAE**. Es lo que el encargo pide con esas palabras.
- **la guarda vieja de la 190 sobre el acta fabricada SIN ninguna**: **PARA**, y
  por eso este registrador no la hereda.
- **el vocabulario de la 190 sobre las tres marcas nuevas**: las **3** salen
  `SIN DECIR`, o sea que heredarlo habria parado el instrumento.
- **la negrita muda**: reparto `(0, 1, 3)`, las tres huerfanas, y **la PARADA por
  huerfana se conserva entera**.
- **la nota de puestos con la caja del acta real**: comparada TAL CUAL **no se
  ve**; comparada en mayusculas **si**. Y un acta sin la nota da **falso**.
- **la idempotencia**: sede sin la entrada **0**, sede con la entrada **2**.

**LA IDEMPOTENCIA, PROBADA RE CORRIENDOLA Y NO AFIRMADA.** Las tres mediciones de
la sede van CERCADAS y no en prosa, y se dice por que: la de ANTES es una cifra
que hoy ya no se puede volver a medir en el disco, asi que publicarla como pareja
suelta seria darle a la guarda de las dos convenciones una cifra que no puede
cotejar contra el fichero de hoy. **Cercada es lo que es: una cita de la salida
del instrumento.**

```
CIFRA bytes de docs/PENDIENTES.md ANTES de tocar nada: 980013
la sede pasa de 980013 a 998216 bytes
RE CORRIDO: docs/PENDIENTES.md sigue en 998216 bytes, NO SE ESCRIBE NADA
```

La salida del re corrido vive en `SALIDA_V191_T1A_RECORRIDO_SIN_ESCRIBIR.txt`, y
**su nombre lo dice**: una ruta que promete prueba es cifra, asi que el fichero no
se llama con un numero de serie que no se consumio. La comprobacion es **por el
acta y no por el numero**, en LAS DOS SEDES, con las marcas literales computadas
de la vuelta. `git diff --numstat -- dataset/`: **0 filas**, antes y despues.

**LA DEUDA DE LA SERIE, REMEDIDA AQUI Y NO HEREDADA DEL `R.52`:** **8** actas sin
entrada propia, las **173 a 180**, con `R.42` cubriendo el acta 172 y `R.43` el
acta 181. **El encargo las deja expresamente fuera, medidas y no arregladas**, y
esta entrada no rellena ninguna.
