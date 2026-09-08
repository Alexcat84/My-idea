### TAREA 1. LOS REGISTROS DE LA VUELTA 208

**NINGUNA CIFRA DE ESTA SECCION ESTA TECLEADA.** Todas se LEEN de
`docs/loop/SALIDA_V209_T1_REGISTROS.txt` y de
`docs/loop/SALIDA_V209_T1_REGISTROS_2.txt` con
`scripts/loop/_v209_t1_seccion.py`, que **cae en rojo si no puede leer una**
o si encuentra mas de una coincidencia. Es la letra de `EJECUTOR.md` 1, LA
TABLA SE CUENTA DE SU FICHERO.

#### 1.a. EL CRECIMIENTO DEL ACTA 208, REMEDIDO CON MIS COMANDOS

El commit del acta se leyo de `git log` y no se tecleo (`EJECUTOR.md` 1, LA
IDENTIDAD SE LEE DE GIT): **`32fc034831256806d0749547efb0e8869d6f44ad`**, con padre **`174717b809400c7d766c298bd79790956238a917`**.
**EL PADRE SE PIDIO CON `~1` Y NUNCA CON EL CIRCUNFLEJO**, y ademas se
comprobo ANTES DE RESTAR que los dos blobs son DISTINTOS: restar dos valores
iguales daria un cero que no es una medicion. La salida lo dice literal:
`los dos blobs son IDENTICOS: NO`.

| que se mide | medido en esta vuelta | contraste del encargo | calza |
|---|---:|---:|---|
| acta ANTES, bytes en disco y bytes normalizado a LF | **4820516** y **4820516** | 4820516 | SI |
| acta DESPUES, bytes en disco y bytes normalizado a LF | **4849108** y **4849108** | 4849108 | SI |
| `sha256` disco y `sha256` LF del acta | **`2abc86822340d1bd`** y **`2abc86822340d1bd`** | `2abc86822340d1bd` | SI |
| linea en que abre la seccion del acta 208 | **73083** | 73083 | SI |

**CIFRA crecimiento del acta: 28592 bytes en disco y 28592 bytes normalizado a LF**,
con **443** lineas anadidas y **0** borradas por `git diff --numstat`. **El
acta solo crece por anexion y su cero de borradas lo prueba.**

**CIFRA discrepancias con el contraste del encargo en el 1.a: 0.** Las seis
celdas cotejadas calzan al digito, asi que **no hay ninguna discrepancia que
declarar en este apartado**, y eso se dice midiendolo y no suponiendolo.

**LO QUE SI DECLARO, PORQUE NO ES DISCREPANCIA PERO LO PARECE:** el acotado
del cuerpo que hace la vara publica `lineas 73083 a 73525, 443 lineas`, y el
fichero mide **73525** lineas por `split` y **73524** por `wc -l`. **Son las
dos convenciones de siempre, no dos mediciones que peleen**, y lo digo en vez
de dejar que parezca un desajuste de una linea.

#### 1.b. `R.73`, ESCRITA POR ADICION PURA Y EN SU SEDE

**EL NUMERO NO ESTA TECLEADO:** lo computa `scripts/loop/serie_de_registros.py`
recomputando la serie de sus DOS sedes, **corrido a la entrada y a la
salida**, y **las dos puntas se publican**.

| la serie `R.N` | punta de ENTRADA | punta de SALIDA | contraste del encargo |
|---|---:|---:|---:|
| entradas | **64** | **65** | 64 |
| de ellas en `docs/PENDIENTES.md` | **63** | **64** | 63 |
| de ellas en `docs/plan/CORRECCIONES_A_APLICAR.md` | **1** | **1** | 1 |
| colisiones | **0** | **0** | 0 |
| huecos | **0** | **0** | 0 |
| mayor escrita | **R.72** | **R.73** | R.72 |
| siguiente libre | **R.73** | **R.74** | R.73 |

**LA SEDE, POR LAS DOS CONVENCIONES Y EN SUS DOS PUNTAS.** Al entrar,
`docs/PENDIENTES.md` mide **1180091** bytes en disco y **1180091** bytes normalizado a
LF, con `sha256` disco **`9cf019a1c9a856f0`** y `sha256` LF **`9cf019a1c9a856f0`**, que calzan al digito con el contraste del
encargo (1180091 por las dos y `9cf019a1c9a856f0`) y con mi propio sello de
apertura. Al salir mide **1190145** bytes en disco y **1190145** bytes normalizado a LF,
con `sha256` disco **`772f6167da46fba8`** y `sha256` LF **`772f6167da46fba8`**.

**CIFRA crecimiento de la sede: 10054 bytes en disco y 10054 bytes normalizado a
LF.** La entrada compuesta mide **10053** bytes y trae **166** lineas, con **0**
guiones largos y **0** guiones medios.

**LAS DOS GUARDAS DE LA ADICION PURA, LAS DOS EN CERO:**

- `git diff --numstat -- docs/PENDIENTES.md` da **167** anadidas y **0**
  borradas. **CERO BORRADAS**, que es lo que el encargo exige.
- La guarda de texto viejo corrio entera encima: **CIFRA lineas del texto de
  ENTRADA que NO estan, en orden, en el de SALIDA: 0**.

**SEGUNDA CORRIDA IDEMPOTENTE:** crece **0** bytes en disco y **0** bytes
normalizado a LF, con **0** entradas escritas. Su salida entera va sellada en
`docs/loop/SALIDA_V209_T1_REGISTROS_2.txt`.

#### 1.c. LAS DIEZ ADJUDICACIONES, POR SU NUMERO Y SU LINEA MEDIDA

**LA VARA DEL `4.1` DEL ACTA 202 CORRIO CON EL LECTOR IMPORTADO Y SIN TOCARLE
UNA LINEA.** `vara_sobre()` viene de `scripts/loop/_v208_t1_registros.py` y
`medir_acta()` de `scripts/loop/_v203_reparto_de_actas_viejas.py`. **IMPORTAR
NO ES CLONAR** (acta 206 `6.5`), y la moratoria de `AUDITOR.md` 6.3 queda
intacta: **ningun lector se ensancho**.

**SU PRUEBA POR MUTACION CORRIO ANTES DE ESCRIBIR NADA Y NO SE HEREDO DE OTRA
CORRIDA** (`EJECUTOR.md` 1, EL CASO ROJO SE PRUEBA POR MUTACION): sobre
`docs/loop/SALIDA_V209_T1_REGISTROS.txt`, **9 casos, 9 verdes y 0 rojos**,
y la segunda pasada muta el esperado y exige que cada caso CAIGA: **9 de 9
caen**. Un caso que no puede fallar no probaria nada.

**LOS CUATRO NUMERALES SALEN COMPUTABLES SOBRE LAS DOS ACTAS: 4 de 4 sobre la
208 y 4 de 4 sobre la 207.** No hubo que declarar ninguno NO COMPUTABLE, y
por eso no se ensancho nada.

| clave | linea medida | que pendiente cierra | titulo, literal del acta |
|---|---:|---|---|
| `6.1` | 73309 | el CHOQUE DE NUEVE ACTAS entre el remedio del acta 205 y `AUDITOR.md` 1 | `6.1` EL REMEDIO DEL ACTA 205 SE AFINA, Y NO ES DOCTRINA NUEVA NI TOCA |
| `6.2` | 73329 | `P.1` del reporte de la 208 | `6.2` LA `P.1` SE ADJUDICA: LA `V.3` DE `OP-L-01` CUBRE, Y NO POR GENEROSIDAD. |
| `6.3` | 73336 | (ninguno) | `6.3` `OP-L-01` NO SE CIERRA AUN, Y EL MOTIVO ES OTRO Y ESTA MEDIDO EN LA `5.2 |
| `6.4` | 73344 | `P.2` del reporte de la 208 | `6.4` LA `P.2` SE ADJUDICA: `OP-L-03` SE CIERRA, Y LAS DOS CUENTAS VAN JUNTAS. |
| `6.5` | 73359 | `P.3` del reporte de la 208 | `6.5` LA `P.3` SE CONTESTA SIN TOCAR NINGUN LECTOR.** El instrumento sellado d |
| `6.6` | 73371 | `PD.1` del reporte de la 208 | `6.6` LA `PD.1` SE ADJUDICA SIN DOCTRINA NUEVA: MANDA LA CONVENCION DEL CORTE |
| `6.7` | 73381 | los TRES DISCUTIBLES del reporte de la 208, los tres ADMITIDOS | `6.7` LOS TRES DISCUTIBLES QUEDAN ADMITIDOS, Y EL MARCADO FUNCIONO EN LOS TRES |
| `6.8` | 73400 | (ninguno) | `6.8` EL TOPE SIGUE EN CINCO Y LE PONGO TRES.** El disparador de `AUDITOR.md` |
| `6.9` | 73408 | (ninguno) | `6.9` LA MORATORIA SE RESPETO Y LO MIDO YO: 19 de 19 CON PREFIJO, 0 SIN EL**, |
| `6.10` | 73412 | (ninguno) | `6.10` LA BATERIA NO CORRE EN LA 209.** Cadencia de cinco (`AUDITOR.md` 6.1): |

**CIFRA adjudicaciones medidas por la vara: 10. CIFRA de ellas que cierran
pendiente: 6. CIFRA de esas que el acta NO trae: 0.** Las cuatro restantes
(`6.3`, `6.8`, `6.9` y `6.10`) **no cierran ningun pendiente numerado**, y eso
se dice en vez de inflar la cuenta.

**EL CERO FALSO QUE NO SE PUBLICA, Y YA NO ES ELECCION MIA.** `titulo_de()`
cuenta las caidas por la forma antigua `CAIDA n`, y el acta 208 escribe las
suyas como `9.1` a `9.4` y `4.1`. Corrido tal cual, el titulo diria **las 0
caidas propias del auditor** sobre un acta que trae **4**. Se le pasa el dato
contado por la forma vigente, **con las dos cuentas y el titulo crudo escritos**,
que es exactamente la letra general que el acta 208 adjudico en su `6.7` al
ADMITIR mi `D.1`. **Se cambia el dato, no la maquina.**

#### 1.d. LA CORRECCION RECIBIDA, SIN CORRECCION QUE APLICAR

El acta 208 levanta **una sola caida contra el ejecutor de esa vuelta**, su
`4.1`: la glosa de la moratoria publicaba `16` ficheros **sin su corte** cuando
el corte de cierre daba `19`. **La recibo y la escribo aqui**, y el encargo ya
dice que **no mueve ningun dato**: el propio auditor midio **19 de 19 con
prefijo de guion bajo y 0 sin el**, asi que la conclusion aguanta y la
moratoria se respeto. **No hay correccion que aplicar en esta tarea.**

**Y LA CAUSA QUEDA APUNTADA PARA NO REPETIRLA:** `_v208_cierre.py` cuenta los
ficheros que la vuelta anadio a `scripts/loop/` **y va en el mismo commit que
cuenta**, asi que su cifra nace corta en uno por construccion. **No lo arreglo,
que es moratoria**: en esta vuelta la glosa lleva su corte, que es el remedio
barato del banco `9.21` y el que el acta 208 encarga en su `7.2`.

#### 1.e. LA DEUDA DE REGISTROS, REMEDIDA AL CIERRE

**CIFRA actas de la 173 a la 208 sin entrada propia: 5** (201, 202, 203, 204, 205). Bajo de 6 a
**5** con `R.73`, y las que quedan son de vueltas anteriores a la 206.

