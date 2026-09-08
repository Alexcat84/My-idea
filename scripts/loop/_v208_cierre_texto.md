## 3. LAS CIFRAS DE LA VUELTA, CONTADAS DE SUS FICHEROS

**TODA CIFRA DE ESTA SECCION SALE DE UN FICHERO DE SALIDA DE ESTA VUELTA, Y EL
FICHERO VA AL LADO** (`EJECUTOR.md` 1, LA TABLA SE CUENTA DE SU FICHERO).

### 3.0. LOS HALLAZGOS DE LA VUELTA, QUE SUBEN PARA QUE EL AUDITOR DECIDA

**`3.0.a`. LA MESA DE LA SELECCION DE CANAL DECLARA UNA COBERTURA COMPLETA QUE NO
LO ES SOBRE SU PROPIO DENOMINADOR, Y ESO CAMBIA UNA DE LAS DOS NOMINAS QUE
`OP-L-01` DA POR CERRADAS.** `docs/plan/LECTURAS_DIRIGIDAS.md:291` declara *"10 de
10, cobertura COMPLETA"*. Recomputado de la nomina de miembros, con el resolutor
puesto, el denominador es **15** y no **10**, asi que la cobertura real es **10 de
15** y por el banco `9.26` la forma es **PROVISIONAL**. La causa esta medida: el
**10** sale de la tabla por nomina de la propia mesa,
`docs/plan/LECTURAS_DIRIGIDAS.md:31`, que cuenta **5 miembros**, y la nomina
verificada contra el grafo en `docs/INTRA_DOMINIO_INFORME.md:5313` lleva una
CORRECCION DECLARADA del 11 ago 2026 en su linea **5321** que dice literalmente
*"son SEIS y no cinco"*. **La mesa cuenta sobre el universo anterior a esa
correccion.** Salida: `docs/loop/SALIDA_V208_T2A_DENOMINADOR.txt`. **No lo
resuelvo yo:** escribi la fila con el denominador recomputado y con la cobertura
declarada PROVISIONAL, y dejo la discrepancia con la mesa escrita al lado.

**`3.0.b`. UNA CORRECCION POR ADICION DENTRO DE UNA TABLA ES INVISIBLE PARA UN
LECTOR QUE TOMA LA PRIMERA FILA QUE CASA.** Corri el instrumento sellado de la
207, `scripts/loop/_v207_t2_cotejo.py`, sin tocarle una linea, y sigue publicando
que *"de las 2 nominas que la mesa declara con cobertura COMPLETA, 2 siguen sin
cerrar"*. **Esa frase ya no es cierta entera**: la junta asesora SI cierra en su
fila corregida. La causa esta medida: su busqueda toma `fila_ban[0]`, la **primera**
fila cuya celda de nombre case, y una correccion por adicion deja **dos** filas por
nomina. **Lee la vieja.** **NO LO ENSANCHO**, porque rige la moratoria de
`AUDITOR.md` 6.3 y no hay caida de dato que lo exija: lo declaro. Salida:
`docs/loop/SALIDA_V208_T2D_COTEJO_REPETIDO.txt`.

**`3.0.c`. LA JUNTA ASESORA TIENE DOS DENOMINADORES SEGUN LA CONVENCION, Y NADIE
LO HABIA DICHO.** Sus **4** miembros son **2** nodos distintos **tras resolver**:
`identificar_junta_asesores` resuelve hoy a `identificar_consejo_asesores`, y
`formalize_advisory_board` a `formalizar_junta_asesora`. En esa convencion los
pares posibles son **1** y no **6**. Es HUELLA DE FUSION, que es como la propia
ficha `OP-L-01` llama a este fenomeno: la campana fundio dos de los cuatro
**despues** del `fecha_corte` de la ficha. **Las dos convenciones van publicadas y
ninguna sustituye a la otra**; el cotejo va contra la literal, que es la que las
dos fuentes usan. Salida: `docs/loop/SALIDA_V208_T2A_DENOMINADOR.txt`.

### 3.1. LAS SALIDAS SELLADAS, CON LAS DOS CONVENCIONES EN EL MISMO RENGLON

| salida sellada | bytes | exitcode |
|---|---|---:|
| `docs/loop/SALIDA_V208_APERTURA.txt` | 3478 bytes en disco y 3478 normalizado a LF | 0 |
| `docs/loop/SALIDA_V208_PASO0_ARCHIVAR.txt` | 963 bytes en disco y 946 normalizado a LF | 0 |
| `docs/loop/SALIDA_V208_ESQUELETO.txt` | 4136 bytes en disco y 4071 normalizado a LF | 0 |
| `docs/loop/SALIDA_V208_CICLO_APERTURA.txt` | 926 bytes en disco y 912 normalizado a LF | 0 |
| `docs/loop/SALIDA_V208_SERIE_APERTURA.txt` | 9113 bytes en disco y 9025 normalizado a LF | 0 |
| `docs/loop/SALIDA_V208_SERIE_CIERRE.txt` | 9252 bytes en disco y 9163 normalizado a LF | 0 |
| `docs/loop/SALIDA_V208_T1_REGISTROS.txt` | 14328 bytes en disco y 14328 normalizado a LF | 0 |
| `docs/loop/SALIDA_V208_T1_REGISTROS_IDEM.txt` | 14279 bytes en disco y 14279 normalizado a LF | 0 |
| `docs/loop/SALIDA_V208_T1D_CORRECCION.txt` | 3303 bytes en disco y 3303 normalizado a LF | 0 |
| `docs/loop/SALIDA_V208_T2A_DENOMINADOR.txt` | 11634 bytes en disco y 11634 normalizado a LF | 0 |
| `docs/loop/SALIDA_V208_T2B_TABLA_VIVA.txt` | 4592 bytes en disco y 4592 normalizado a LF | 0 |
| `docs/loop/SALIDA_V208_T2D_V3.txt` | 5403 bytes en disco y 5403 normalizado a LF | 0 |
| `docs/loop/SALIDA_V208_T2E_V14.txt` | 3492 bytes en disco y 3492 normalizado a LF | 0 |
| `docs/loop/SALIDA_V208_T3_VARA.txt` | 11793 bytes en disco y 11793 normalizado a LF | 0 |
| `docs/loop/SALIDA_V208_T3_COTEJO.txt` | 9279 bytes en disco y 9279 normalizado a LF | 0 |

### 3.2. LAS CIFRAS DE CADA TAREA, CON EL FICHERO DEL QUE SE CUENTAN

| cifra | valor | fichero del que se cuenta |
|---|---|---|
| acta 207: bytes antes / despues / anadidos | 4793964 / 4820516 / 26552 | `SALIDA_V208_T1_REGISTROS.txt` |
| acta 207: lineas del fichero y linea de apertura de la seccion | 73081 y 72641 | `SALIDA_V208_T1_REGISTROS.txt` |
| serie de registros: entradas al entrar y al salir | 63 y 64 | `SALIDA_V208_SERIE_APERTURA.txt` y `SALIDA_V208_SERIE_CIERRE.txt` |
| `R.72`: lineas anadidas y borradas en su sede | 140 y 0 | `SALIDA_V208_T1_REGISTROS.txt` |
| vara del `4.1` sobre las actas 206 y 207 | 1 de 4 y 4 de 4 | `SALIDA_V208_T1_REGISTROS.txt` |
| adjudicaciones del acta 207, medidas | 8 | `SALIDA_V208_T1_REGISTROS.txt` |
| elementos de `verificacion` de `OP-L-01`, remedidos | 7 | `SALIDA_V208_T1D_CORRECCION.txt` |
| denominador recomputado: junta asesora y seleccion de canal | 6 y 15 | `SALIDA_V208_T2A_DENOMINADOR.txt` |
| cobertura recomputada: junta asesora y seleccion de canal | 6 de 6 y 10 de 15 | `SALIDA_V208_T2A_DENOMINADOR.txt` |
| banco: lineas anadidas y borradas | 66 y 0 | `SALIDA_V208_T2B_TABLA_VIVA.txt` |
| `OP-L-03`: puntos de la vara y citas que no aparecen verbatim | 18 y 0 | `SALIDA_V208_T3_VARA.txt` |
| `OP-L-03`: reparto sellado, documentales y no documentales | 16 y 2 | `SALIDA_V208_T3_VARA.txt` |
| `OP-L-03`: CUBRE, A MEDIAS, NO CUBRE, NO DOCUMENTAL | 15, 0, 1 y 2 | `SALIDA_V208_T3_COTEJO.txt` |
| ficheros anadidos a `scripts/loop/` y cuantos con prefijo | 16 y 16 | `SALIDA_V208_CIERRE.txt` |

## 4. LO QUE SE TOCO, Y LO QUE NO

**EL ESTADO DEL ARBOL AL ENTRAR, LEIDO DE MI APERTURA SELLADA Y NO TECLEADO.**
`docs/loop/SALIDA_V208_APERTURA.txt`, escrito **antes de la primera operacion**,
publica `CIFRA lineas de status: 1` medidas con `git status --porcelain`, y esa
unica linea era mi propio computo sin seguimiento. Y publica
`CIFRA filas de git diff --numstat -- dataset/ AL ENTRAR: 0`.

**LO QUE SI SE TOCO, Y SON TRES SEDES:**

| sede | lineas anadidas | lineas BORRADAS | por que |
|---|---:|---:|---|
| `docs/PENDIENTES.md` | 140 | **0** | `R.72`, por adicion pura |
| `docs/loop/reportes/REPORTE_V207.md` | 26 | **0** | la correccion declarada de la `4.1` |
| `docs/BANCO_DE_TEXTOS.md` | 66 | **0** | las dos filas de la tabla viva, por adicion |

**CERO LINEAS BORRADAS EN LAS TRES.** Y las tres traen su guarda propia corrida:
las lineas del texto de entrada que **no estan, en orden**, en el de salida son
**0** en las tres.

**LO QUE NO SE TOCO, MEDIDO AL CIERRE Y NO HEREDADO DE LA APERTURA.**
`git diff` contra el HEAD de apertura `0d9e71a3` sobre `dataset/`, `web/`,
`engine/` y `docs/plan/` da **0** filas en las cuatro, y `git diff HEAD --numstat`
sobre esas mismas cuatro da **0** filas tambien. Salida:
`docs/loop/SALIDA_V208_CIERRE.txt`.

**LAS SEDES SELLADAS, REMEDIDAS AL CIERRE POR LAS DOS CONVENCIONES, Y NI UN
VEREDICTO NI UN `estado` SE MOVIERON:** `docs/INTRA_DOMINIO_VEREDICTOS.jsonl` en
**4054129** bytes en disco y **4054129** normalizado a LF, con sha256 disco
`0a77b5a35a962621` y sha256 LF `0a77b5a35a962621`; y `docs/plan/OPERACIONES.jsonl`
en **513043** bytes en disco y **513043** normalizado a LF, con sha256 disco
`829c583eb779cab6` y sha256 LF `829c583eb779cab6`. **Los dos identicos a los de mi
apertura**, y `CIFRA sedes selladas que NO calzan: 0`.

**LAS TRES SEDES DEL AUDITOR, EN 0, 0 Y 0**, con el cero de `PARA_ALEXIS.md`
distinguido como **DE AUSENCIA DE FICHERO**: no existe en disco, y eso no es lo
mismo que un fichero vacio.

**LA MORATORIA SE RESPETO Y LO MIDO YO:** **16** ficheros anadidos a
`scripts/loop/`, **los 16 con prefijo de guion bajo**, **0** sin el. **Ningun
lector heredado se toco.** Los dos parches que esta vuelta corrio,
`_v208_parche_denominador.py` y `_v208_parche_cotejo.py`, tocan **solo computo mio
de esta vuelta**, nunca un instrumento de la casa.

**Y LOS TRES DOCUMENTOS DE LA MESA `OP-L-03` SE LEYERON Y NO SE ESCRIBIERON**, con
los seis calzando al digito contra el contraste del encargo por las dos
convenciones y `CIFRA documentos cuya medicion NO calza: 0`.

## 5. LOS DISCUTIBLES, MARCADOS ANTES DE SABER SI ACIERTO

**`D.1`. LE PASE A `titulo_de()` LAS CAIDAS CONTADAS POR OTRA FORMA EN VEZ DE
DEJAR QUE PUBLICARA UN CERO FALSO.** `REG206.titulo_de()` cuenta las caidas por la
forma antigua `CAIDA n` y el acta 207 las escribe como `9.1` a `9.4`. Corrido tal
cual, el titulo de `R.72` habria dicho **las 0 caidas propias del auditor** sobre
un acta que trae **cuatro**. Le pase el dato contado por la forma que esa acta usa,
sin tocar la funcion, y publique las dos cuentas y el titulo crudo dentro de la
entrada.

**POR DONDE ME PUEDO ESTAR EQUIVOCANDO:** el precedente de la casa para un numeral
que un lector no puede dar es **declararlo NO COMPUTABLE**, no alimentarlo con otro
dato. Un auditor podria decir con razon que lo limpio era dejar el cero y declararlo
al lado, y que cambiar el dato de entrada de una funcion sellada es una forma suave
de cambiar la funcion. **Yo creo que publicar un cero que se sabe falso es peor, y
que la diferencia esta en que las dos cuentas quedan escritas**, pero la letra es
del auditor.

**`D.2`. EL CORTE DE LA TABLA VIVA LO ACTUALICE POR ADICION, CON UN PUNTERO, EN VEZ
DE PISAR LA CABECERA.** El encargo dice en su `2.b` que *"el corte de la tabla se
actualiza tambien"* y en su `2.c` que *"si borras una sola linea de texto viejo, es
rojo"*. Las dos juntas solo se pueden cumplir anadiendo: la cabecera con su
`14 ago 2026` sigue entera y sin tachar, y debajo va un puntero que declara la
correccion posterior con su corte y sus dos filas.

**POR DONDE ME PUEDO ESTAR EQUIVOCANDO:** quien mire solo la cabecera sigue leyendo
un corte viejo, y el encargo podria haber querido literalmente que la linea 938
dijera otra fecha. **Si es asi, la pisada es una linea y se hace en la 209**, pero
yo no piso texto viejo sin que me lo manden con esas palabras.

**`D.3`. DIGO "LA VARA SE SELLA ANTES DE ABRIR NINGUN DOCUMENTO" Y TRES DE LOS SEIS
YA ESTABAN ABIERTOS.** `EJECUTOR.md` lo manda el encargo como primer acto de la
vuelta, `AUDITOR.md` lo cita el encargo, y `LECTURAS_DIRIGIDAS.md` lo midio mi
TAREA 2. Lo declaro dentro del propio sello en vez de dejar la frase suelta.

**POR DONDE ME PUEDO ESTAR EQUIVOCANDO:** un auditor estricto puede decir que
entonces el sello de esos tres no vale y que la mesa habria que rehacerla en una
vuelta que no los toque. **Yo creo que lo que el sello protege es que la vara no se
acomode a lo visto, y ninguno de los tres se abrio buscando puntos de la vara**,
pero la objecion es legitima y por eso la escribo antes de saber si acierta.

## 6. LAS PREGUNTAS

**`P.1`. ¿CUBRE LA `V.3` DE `OP-L-01` CON UNA COBERTURA QUE LA PROPIA FILA DECLARA
PROVISIONAL?** Deje las tres lecturas medidas en el `2.d` y las tres con su cita.
Por el criterio que la 207 uso, **A MEDIAS**; por el criterio que la `6.1` escribio
(*"la cobertura AL LADO"*, y el `9.26` contempla expresamente lo provisional),
**CUBRE**. **Yo propongo CUBRE y paro**, porque cerrar la ficha es adjudicacion
del auditor.

**`P.2`. ¿SE CIERRA `OP-L-03` CON UN `NO CUBRE` QUE LA PROPIA FICHA YA RECONOCIO?**
Su unico `NO CUBRE` es la `V.3`, que sale de `evidencia[2]`, y la CORRECCION
DECLARADA de la vuelta 202 que vive en `evidencia[3]` de esa misma ficha ya escribio
que *"LA EVIDENCIA APUNTABA AL DOCUMENTO EQUIVOCADO"*. **Propongo que no se cierre
mientras `evidencia[2]` siga apuntando ahi**, pero si la casa lee que una evidencia
corregida por adicion deja cubierto el punto, la mesa cierra en **16 de 16**.

**`P.3`. ¿QUE SE HACE CON UN LECTOR QUE TOMA LA PRIMERA FILA QUE CASA CUANDO LA
CASA CORRIGE POR ADICION?** Es el `3.0.b`. La moratoria me impide ensancharlo y no
hay caida de dato que lo exija, asi que lo dejo declarado. **Pero mientras siga
asi, toda correccion por adicion dentro de una tabla sera invisible para el
instrumento que la vigila**, y eso no es un defecto de esta vuelta sino del carril.

## 7. PENDIENTES DE DOCTRINA

**`PD.1`. NO HAY REGLA ESCRITA SOBRE QUE CONVENCION MANDA EN UN DENOMINADOR CUANDO
LA CAMPANA FUNDE MIEMBROS DESPUES DEL CORTE DE UNA FICHA.** El `P.1` manda poner el
resolutor para todo conteo que toque ids; la tabla viva cuenta en literal; y sobre
la junta asesora las dos dan **6** y **1**. **Registre las dos y no elegi**, que es
lo mejor que sostengo sin regla. **PENDIENTE DE DOCTRINA**, y no paro por ello.

## 8. MIS CAIDAS PROPIAS, CADA UNA CON SU NOMBRE Y CONTADA UNA SOLA VEZ

**`C.1`. MI ESQUELETO ESCRIBIA PRIMERO Y VALIDABA DESPUES, Y ME DEJO EL REPORTE
PISADO EN DISCO.** Es exactamente la especie del aviso que el encargo me dio sobre
`cerrar_reporte.py`, cometida por mi en mi propio computo. La primera corrida de
`_v208_esqueleto.py` salio en rojo **despues** de haber escrito
`docs/loop/REPORTE.md`, asi que me dejo en disco un texto que su propia guarda
declaraba malo. Lo cace, lo restaure con `git checkout HEAD --`, comprobe que el
sha256 LF volvia a `e0d67989e21687ce`, y **reordene mi computo**: compone en
memoria, juzga entero, y solo escribe si el juicio da cero fallos, con relectura
del disco al final.

**`C.2`. MI PROSA CITABA LAS CUATRO MARCAS DEL ANEXO Y LA GUARDA LAS CONTABA DOS
VECES.** El texto del esqueleto explicaba la `C.1` de la 207 copiando los cuatro
literales, y la comprobacion los cuenta sobre el fichero entero: salian a **2** y
**2** donde se exige **1**. Arregle la prosa, que ahora los nombra en vez de
copiarlos, y lo dejo escrito dentro del propio fichero.

**`C.3`. `SALIDA_V208_HEAD_APERTURA.txt` NACE AL CIERRE, NO EN LA APERTURA.** El
VALOR es de apertura de verdad y **no esta tecleado**: lo lee un computo de
`docs/loop/SALIDA_V208_APERTURA.txt`, que escribi antes de la primera operacion y
que quedo committeado en `6877f013`. Pero **el fichero con ese nombre nace ahora**,
y el tallador lo dice por su cuenta: su celda de identidad publica *"sello
RECONSTRUIDO DESPUES"* con el commit que lo anade. Es la misma especie que la `C.2`
del reporte de la 207 y **la vuelvo a cometer**, y eso tambien se dice.

**`C.4`. DOS DE MIS TRES `NO CUBRE` DE `OP-L-03` ERAN DE MI PATRON Y NO DEL
MUNDO.** Mi primera corrida del cotejo daba **3 NO CUBRE**. La `V.8` **afirma una
ausencia** y yo la buscaba como presencia, cuando encontrar cero es justo lo que la
confirma; y la `V.13` **si esta**, en `docs/loop/AUDITOR.md:17`, escrita en
versales, y mi sonda buscaba minusculas. **Las cace corriendo el computo, no
razonandolo**, y las arregle sin tocar la vara sellada: lo que cambio es **como
busca el cotejo**, no que se coteja ni contra que documento. Es la misma especie que
mi `C.3` de la 207.

**LAS CUATRO SON MIAS, LAS CUATRO ESTAN CAZADAS POR MIS PROPIAS GUARDAS Y NINGUNA
LLEGO A PUBLICARSE COMO CIFRA.**

## LO QUE PROPONGO PARA LA VUELTA SIGUIENTE

1. **CERRAR `OP-L-01`** si el auditor adjudica la `P.1`: la tabla ya lleva el
   efecto de la mesa y la `V.3` esta medida con sus tres lecturas y sus citas.
2. **DECIDIR SOBRE `OP-L-03`** con la `P.2` delante: la mesa esta medida en
   **15 CUBRE, 1 NO CUBRE y 2 NO DOCUMENTALES** sobre **18** puntos.
3. **LA 210 ES VUELTA DE BATERIA** por la cadencia de `AUDITOR.md` 6.1, y no lleva
   nada mas.
