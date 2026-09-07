### TAREA 1. LOS REGISTROS: `R.67` PARA EL ACTA 177 Y `R.68` PARA EL ACTA 178

**LO QUE SE HIZO:** se escribieron las dos entradas siguientes de la deuda del
`4.9` del acta 201, en `docs/PENDIENTES.md`, **por adicion pura**. Va PRIMERA
porque `AUDITOR.md` 1.4 pone los registros en la TAREA 1.

**EL COMPUTO NO SE ESCRIBIO POR TERCERA VEZ Y TAMPOCO SE CLONO: SE IMPORTA.** El
encargo daba dos puertas (*importalo o clonalo con su cifra de `difflib` al
lado*) y **se tomo la que no fabrica fichero**: `_v204_t1_registros.py` hace
`import _v203_reparto_de_actas_viejas as REP` en su linea 50. **Por eso no hay
cifra de `difflib` del reparto: no hay clon del reparto que medir.** Lo que si es
clon, y va medido y no afirmado, es el REGISTRADOR:
`scripts/loop/_v204_t1_registros.py` sale de `_v203_t4_registros.py` con
`_gen_v204_t1_registros.py`, que imprime **485 lineas en la fuente y 495 en el
destino, de las que 459 vienen SIN TOCAR y 36 son nuevas o cambiadas**, contadas
con `difflib.SequenceMatcher` y no a ojo, mas **11 cambios puntuales, cada uno
con su cuenta de apariciones comprobada por `assert`**.

**LA DEUDA, REMEDIDA HOY Y NO COPIADA DEL ENCARGO.** Antes de escribir nada, el
instrumento conto **4** actas de la 173 a la 180 sin entrada propia: **177, 178,
179 y 180**. Al cerrar la tarea quedan **2**: **179 y 180**. El encargo decia 4 y
**lo medido calza**.

**LA PRUEBA POR MUTACION, CORRIDA ANTES DE ESCRIBIR NADA** (`EJECUTOR.md` 1, EL
CASO ROJO SE PRUEBA POR MUTACION), y **no se hereda el verde de otra corrida**:
`docs/loop/SALIDA_V204_T1_REGISTROS.txt` publica **9 casos, los 9 pasan, 0 rojos,
y con el esperado mutado CAEN los 9**. En 4 de los 9 la plantilla ancha y la
heredada discrepan, y la tercera columna prueba que **ningun llamante viejo se
mueve**: llamada sin el parametro nuevo da exactamente lo mismo que la heredada.

#### DE QUE CONVENCION SON, COMPROBADO Y NO SUPUESTO

**LAS DOS SON DE LA CONVENCION ANTERIOR A LA 184, Y ESO NO SE DEDUJO DE QUE 177 Y
178 SEAN MENORES QUE 184: SE MIDIO.** El lector heredado, que EXIGE comillas
inversas, da **0** sobre las secciones de adjudicaciones de las dos actas,
mientras la vara ancha del `4.1` del acta 202 da **11** en la 177 y **13** en la
178. **El heredado NO basta, y se dice.** La medicion entera esta en
`docs/loop/SALIDA_V204_T1C_AMBIGUEDAD.txt`.

#### EL REPARTO, CADA NUMERAL CON LA SECCION DE LA QUE SALE NOMBRADA POR SU TITULO

| acta | cuerpo acotado HOY | secciones | adjudicaciones | hallazgos | caidas del auditor | caidas del ejecutor | preguntas |
|---|---|---:|---|---|---|---|---:|
| 177 | lineas 60866 a 61490, 625 lineas | 12 | **NO COMPUTABLE**, 2 secciones lo titulan | **NO COMPUTABLE**, ninguna seccion lo titula | **NO COMPUTABLE por una sola forma**, seccion 6 `MIS CAIDAS PROPIAS, CON SU NOMBRE` | **NO COMPUTABLE**, ninguna seccion lo titula | 0 |
| 178 | lineas 61491 a 62018, 528 lineas | 12 | **NO COMPUTABLE**, 2 secciones lo titulan | **NO COMPUTABLE**, ninguna seccion lo titula | **NO COMPUTABLE**, ninguna seccion lo titula | **NO COMPUTABLE**, ninguna seccion lo titula | 0 |

**NINGUNO DE ESOS `NO COMPUTABLE` ES UN CERO, Y ESA ES LA DIFERENCIA QUE EL
ENCARGO PIDE MARCAR.** Un cero de convencion se leeria como que el acta no
adjudico nada, y es falso: la 177 adjudica 11 veces y la 178 trece.

**LAS TRES LECTURAS DE LAS CAIDAS DE LA 177, PUBLICADAS JUNTAS PORQUE DISCREPAN:**
por la vara `N.M` da **0**, por la forma vieja ``**`CAIDA n`.`` da **0**, y por
lead en negrita que abre con `CAIDA` o `AMAGO` da **3** (`CAIDA PROPIA 1` en la
linea 61218, `CAIDA PROPIA 2` en la 61230 y `CAIDA PROPIA 3, CAZADA POR MI EN
ESTA MISMA AUDITORIA` en la 61238). El heredado
`R94.caidas_propias_entrecomilladas()` da **0** sobre ese mismo cuerpo.

#### EL COTEJO CONTRA LA FILA DE METRICA DE CADA ACTA, QUE LA ESCRIBIO OTRO

| acta | lo que su propia fila de metrica publica | lo que este computo mide | calza |
|---|---|---|---|
| 177 | linea 61434, caidas propias del auditor **3** | **3** por lead en negrita, **0** por `CAIDA n` | **SI por la lectura de lead** |
| 178 | linea 61971, caidas propias del auditor **1** | **NO COMPUTABLE**: ninguna seccion titula ese numeral | **NO, y se declara** |

**LA DISCREPANCIA DE LA 178 SE DECLARA EN VEZ DE RESOLVERSE COPIANDO**
(`EJECUTOR.md` 2). Medido y no supuesto: esa acta pone su caida propia DENTRO de
su seccion 2, cuyo titulo literal es `EL ORDEN EN QUE CORRI, Y MI CAIDA PROPIA
DELANTE`, y la etiqueta `C.1` en la linea 61526. La vara del `4.1` toma el
numeral **de la seccion cuyo PROPIO TITULO lo nombra**, y `MI CAIDA PROPIA
DELANTE` no es `MIS CAIDAS PROPIAS`. **La fila del auditor de aquella vuelta dice
1 y tiene razon; lo que no se puede es computarlo por la vara vigente sin
decidir, y decidir no me toca.**

#### LA VIA DEL NUMERAL DE PREGUNTAS, DICHA Y NO SUPUESTA

Los dos reportes archivados **existen**: `docs/loop/reportes/REPORTE_V177.md` con
**53201 bytes** y `docs/loop/reportes/REPORTE_V178.md` con **59617 bytes**,
medidos hoy con `os.path.isfile` y `os.path.getsize`. **Pero ninguno de los dos
titula seccion de PREGUNTAS**, asi que el filtro no se puede correr y se usa la
vara del `4.8` del acta 203, que extiende el `4.7` del acta 201: **un reporte que
existe pero no titula seccion de preguntas se trata como el que no existe,
DECLARANDOLO**. El numeral sale **NOMBRADAS EN LOS TITULOS DE LAS ADJUDICACIONES**
y da **0** en las dos.

#### LA GUARDA, OBLIGATORIA Y CORRIDA DOS VECES

- **PRIMERA CORRIDA, Y LA RUTA SE QUEDA CON SU TAMANO AL CIERRE.** La sede entra
  con **1131953 bytes en disco y 1131953 normalizado a LF**, y ese es su tamano
  DE ENTRADA, que por eso va **sin nombrar la ruta en su renglon**: pegarle una
  ruta a una cifra intermedia hace una pareja completa y falsa.
  El `sha256` de entrada era **725b85e12050a0ae** en disco y **725b85e12050a0ae** normalizado a LF.
  AL CIERRE, `docs/PENDIENTES.md` mide **1145356 bytes en disco y 1145356 normalizado a LF**,
  con `sha256` **de3311c2a8d5aa8c** en disco y **de3311c2a8d5aa8c** normalizado a LF.
  El crecimiento es de **13403** por las dos convenciones, y de **209** lineas.
- **LINEAS BORRADAS O CAMBIADAS: 0.** La guarda recorre el texto de entrada
  renglon a renglon contra el de salida y cuenta cuantos no estan, en orden:
  **0**. **Adicion pura.**
- **SEGUNDA CORRIDA, la que sella la idempotencia**, y su salida vive en
  `docs/loop/SALIDA_V204_T1_REGISTROS_SEGUNDA.txt`.
  El crecimiento es de **0** por las dos convenciones, **0 lineas** y **0 entradas
  escritas**, porque la guarda de idempotencia mira **el sujeto** y no solo el
  numero.
- **LA SERIE, RECOMPUTADA CON `scripts/loop/serie_de_registros.py` Y NO CON UNA
  EXPRESION REGULAR MIA** (que es la `C.4` del acta 203): antes **58 entradas, 0
  colisiones, 0 huecos, siguiente libre `R.67`**; despues **60 entradas, 0
  colisiones, 0 huecos, siguiente libre `R.69`**.

#### LO QUE PROPONGO Y NO DECIDO, Y VA MARCADO COMO DISCUTIBLE

**`D.1` LA AMBIGUEDAD DE `ADJUDICACIONES` PUEDE NO SER AMBIGUEDAD, Y LO MIDO EN
VEZ DE OPINARLO.** En las dos actas las DOS secciones que titulan el numeral son
la **7** y la **10**, y **la 10 no aporta ni una sola clave**: en la 177 la
seccion 10 (`LAS ADJUDICACIONES QUE CITAN REGLA ESCRITA, EN UNA LISTA`, 10
lineas) da **0 claves `10.M` por la vara ancha y 0 por el heredado**, y en la 178
esa misma seccion (12 lineas) da **0 y 0**. O sea que **la ambiguedad es de
TITULO y no de contenido**: si la vara se leyera como *la seccion titulada que
APORTA claves*, el numeral seria **11** en la 177 y **13** en la 178, sin decidir
nada a ojo. **NO LO APLICO Y NO LO ESCRIBI EN LAS ENTRADAS**: seria doctrina
nueva y la doctrina es del auditor. Lo dejo medido, con su salida, para que se
adjudique sobre cifras.
