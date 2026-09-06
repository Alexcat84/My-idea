# REPORTE DE LA VUELTA 192 (ejecutor). FASE III, EJECUCION. Rama `pasada-unica`.

> **ESTE REPORTE SE ABRIO AL EMPEZAR LA VUELTA Y CRECE POR ANEXION** (`EJECUTOR.md`
> 1, "EL REPORTE ABRE CON LA VUELTA"). El esqueleto lo tallo
> `scripts/loop/vuelta192_esqueleto_reporte.py`; cada tarea ANEXA SU FILA AL
> CERRARSE, no al final; y el cierre lo talla entero `scripts/loop/cerrar_reporte.py`.
> **Si esta vuelta se corta, lo que quede aqui es lo que de verdad se hizo, y las
> filas que sigan diciendo ABIERTA, SIN CERRAR son las que no se hicieron.**
>
> **ESTA VUELTA NO ES DE BATERIA, Y SU SECCION 9 CIERRA CON EL HUECO DECLARADO Y
> MEDIDO.** `AUDITOR.md` 6.1, decision del fundador del 5 sep 2026: la bateria de
> mutaciones **corre CADA CINCO VUELTAS**, en una vuelta propia que **no lleva
> nada mas**. **La 189 la corrio entera**, asi que **la siguiente cae en la 194**.
> El hueco va **con su nombre, sus bytes medidos y su atribucion, LAS TRES
> JUNTAS**, por el carril de `cerrar_reporte.py`: **un hueco declarado no es un
> hueco escondido.**
>
> **VAN CINCO SUB-TAREAS Y DOS SON BLOQUEANTES. El tope de cinco no hace falta
> volver a ganarlo:** esta vigente desde la `4.10` del acta 190. **Y la cifra que
> lo sostiene se REMIDIO en esta vuelta en vez de heredarse**, tal como el encargo
> manda: el bloque **B.2** del sello de apertura busco en git los commits de
> cierre y midio sus ficheros `SALIDA_V<n>_CERRAR_REPORTE.txt` uno a uno, **y
> cuando vi que mi ventana estaba tecleada escribi un instrumento que cuenta del
> inventario ENTERO**, `scripts/loop/vuelta192_racha_de_cierres.py`. Las cifras
> que andan dando vueltas se publican JUNTAS en la seccion 0.
>
> **DONDE SE TALLO ESTE ESQUELETO: EN LA APERTURA Y EN SU PROPIO COMMIT.** Desde
> el segundo commit de esta vuelta ya hay reporte parcial en el arbol.
>
> **LO QUE NO ENTRA EN ESTA VUELTA, DICHO PARA QUE NO SE CUELE:** ni cribado, ni
> recomputo, ni operaciones del plan, ni las mesas anotadas, ni **podar la
> nomina** (la opcion `c` que el fundador RECHAZO el 5 sep 2026: **la nomina
> sigue creciendo y nadie la poda sin el fundador**), ni la bateria, que cae en
> la 194. **Y siguen fuera, nombradas para que la 193 no las redescubra:** el
> desfase de `PATRONES_ACTA`, **que se encarga DESPUES de la 194** porque toca
> `tallar_cabecera_reporte.py` y cuatro entradas de la nomina lo nombran;
> `acumulan()` que lea la tabla o declare que no es la sede; el cotejo de clon
> declarado que separa sentencia de codigo de cambio de texto; la excepcion que
> publica siempre su lista; la medicion del censo de arneses con carril de
> mutacion sin fichero propio; las ocho actas sin entrada propia en la serie (173
> a 180); el exitcode 2 propagado a `--componer`; y que el campo `evidencia` de
> `OP-L-02` nombre los ficheros que ya existen, **cuyo ESTADO NO SE MUEVE: sigue
> en `LISTA`**.
>
> **NO SE MUEVE NINGUN VEREDICTO:** el `sha256` LF de
> `docs/INTRA_DOMINIO_VEREDICTOS.jsonl` abre y tiene que cerrar en el mismo
> valor. **Y no se toca `dataset/` a mano**: el `numstat` se mide al entrar y al
> salir y **las dos cifras se publican**.
>
> **Y ESTA VUELTA MIDE SU DESFASE DE CALIBRADO EN LA APERTURA, DENTRO DEL BLOQUE
> DE APERTURA Y ANTES DE LA PRIMERA OPERACION.** **Una columna de apertura medida
> al cierre es caida que ACUMULA.**

**EL VEREDICTO DE UNA LINEA: LAS CINCO TAREAS CERRARON SIN MOVER UN SOLO VEREDICTO DEL ARCHIVO, QUE ABRE Y CIERRA EN 0a77b5a35a962621 POR LAS DOS CONVENCIONES. EL ACTA 192 ENTRA COMO R.54 Y EL REGISTRADOR APRENDIO A LEER UN LOTE DE CAIDAS ESCRITO EN RANGO, QUE HABRIA PUBLICADO 2 DONDE EL ACTA DECLARA 6; LA RELECTURA AL DOBLE SALIO MAL PARA MI Y LO DIGO ASI, 20 COINCIDEN Y 10 DISCREPAN CON TRES FUERA DE MIS QUINCE DUDOSOS, Y LAS TRES SON LA MISMA ESPECIE: CONTE SOLAPE DE PASOS DONDE LA VARA DE LA CASA PREGUNTA POR LA LINEA CONTRA EL PROCEDIMIENTO; LOS DOS SUJETO VIVO QUEDAN ARREGLADOS POR CARRILES DISTINTOS PORQUE NO ERAN EL MISMO CASO, Y MIDIENDOLO DESCUBRI QUE NO ENTRABAN EN LA NOMINA Y QUE LOS QUE SI ENTRAN TRAEN OTRA DEUDA; LA CUARTA PUERTA EXISTE Y EL ARNES QUE LA NOMINA TIENE SOBRE ESE FICHERO SIGUE REPRODUCIENDO BYTE A BYTE; Y EL FORMATO UNICO DEL COTEJO YA SE USO EN LA TAREA 2 Y RECUPERA EXACTAMENTE LOS TRES COTEJOS QUE EL ACTA NOMBRABA. DECLARO CUATRO CAIDAS PROPIAS, TODAS DE METODO: TRES LAS CACE YO Y LA CUARTA ME LA CAZO EL CERRADOR, QUE SE NEGO A DAR POR BUENO EL REPORTE HASTA QUE ARREGLE DOS PAREJAS DE BYTES DE ANTES PUBLICADAS EN PROSA.**
## 0. LA IDENTIDAD Y LA CABECERA, TALLADAS Y NO TECLEADAS

**LA IDENTIDAD, LEIDA DE GIT EN ESTA VUELTA** por
`scripts/loop/vuelta192_esqueleto_reporte.py`, con
`git rev-parse --abbrev-ref HEAD`, `git log` y `git log --diff-filter=A`, y CAE
EN ROJO si algo no se encuentra o es ambiguo:

- rama: `pasada-unica`
- commit del acta de la vuelta 191: `d21d5e8b`. **Su asunto real va CERCADO
  ABAJO, y no suelto en esta prosa**, porque un asunto de acta puede traer
  DENTRO cifras de bytes y `sha256` suyas, y una guarda que mira renglon a
  renglon no distingue una cita de una afirmacion. Cercarlo es decir lo que es:
  **una cita de la salida de un instrumento**.

```
'ACTA DEL AUDITOR, VUELTA 191: LA 190 REPRODUJO ENTERA Y SIN UNA CIFRA FALSA NI UNA RUTA VACIA.'
```
- **DESFASE DECLARADO, Y SU ORDINAL NO SE TECLEA.** La linea de arriba nombra el
  acta **191** porque `PATRONES_ACTA` pide la de `VUELTA - 1`, y **el acta que
  ORDENA esta vuelta es la 192**. Es el `D.2` del reporte de la 184, adjudicado
  a favor con reparacion encargada por la `5.2` del acta 185, **y la `4.7` del
  acta 192 lo deja expresamente DESPUES de la bateria de la 194**. El reporte de
  la 191 se llama a si mismo **la SEPTIMA vuelta** del desfase; **esa palabra no
  sale de ningun instrumento, asi que aqui no se copia ni se le suma uno a ojo**:
  lo que si se puede contar es que **4 reportes archivados traen el
  literal `DESFASE DECLARADO`** (`REPORTE_V189.md`, `REPORTE_V190.md`, `REPORTE_V191.md`, `REPORTE_V192.md`), contados por
  `reportes_con_el_literal()` de este mismo fichero. **LAS DOS CIFRAS SE PUBLICAN
  Y LA DISCREPANCIA SE DECLARA EN VEZ DE RESOLVERSE COPIANDO.**
- HEAD real de apertura, sellado ANTES de la primera operacion en
  `docs/loop/SALIDA_V192_HEAD_APERTURA.txt`: `485c2f3e`
- commit de nacimiento del bloque de apertura, leido con
  `git log --diff-filter=A`: `3470f651`
- reporte que este esqueleto pisa, leido de la cabecera de ese mismo fichero:
  la vuelta **192**, ya archivada byte a byte antes de escribir aqui
- commit de cierre: se talla al cierre. **Un reporte no puede nombrar el commit
  que lo lleva**, porque ese commit se crea despues de escribirlo.

<!-- CABECERA TALLADA -->
**LA TABLA, PEGADA ENTERA DEL FICHERO QUE LA LLEVA Y NO TECLEADA.** Salio
de `scripts/loop/tallar_cabecera_reporte.py --fase04 --vuelta 192`, y su salida
cruda vive en `docs/loop/SALIDA_V192_TALLADOR_CABECERA.txt` (2349 bytes en disco y 2329 normalizado a LF, 11 filas de
tabla,
contadas por `scripts/loop/cerrar_reporte.py`). **LA CELDA QUE NO SALGA DE UN
INSTRUMENTO NO SE ESCRIBE.**

| | **apertura**, antes de la 1.ª operacion | **cierre, RECOMPUTADO al cierre** |
|---|---:|---:|
| censo: nodos / vivos / deprecados | 3.853 / 3.169 / 684 | **3.853 / 3.169 / 684** |
| Gate 0: veredicto, auto-aristas, duplicadas de titulo, divergentes | OK (auto-aristas 0, duplicadas 0, divergentes 0) | **OK (auto-aristas 0, duplicadas 0, divergentes 0)** |
| aristas: `nodos_siguientes` / `nodos_previos` / suma / union | 8.780 / 8.740 / 17.520 / 9.914 | **8.780 / 8.740 / 17.520 / 9.914** |
| motor | 25/25 | **25/25** |
| web: ficheros / tests | 82 passed (82) / 1.040 passed (1.040) | **82 passed (82) / 1.040 passed (1.040)** |
| tsc | EXITCODE 0, cero lineas | **EXITCODE 0, cero lineas** |
| aristas movidas en la vuelta (cierre menos apertura): `nodos_siguientes` / `nodos_previos` / suma / union | (no aplica: la celda de cierre es la resta contra esta apertura) | **+0 / +0 / +0 / +0** |
| desfase del calibrado rastreado (`PASO_NODO_CALIBRADO.jsonl` distinto del grafo) | 4 fila(s): `dia_cero_defectos_2 -> eliminacion_causas_error_4`, `customer_validation -> establecer_linea_base_mvp`, `dia_cero_defectos_3 -> eliminacion_causas_error_4`, `ganar_comprension_del_cliente -> dia_en_la_vida_del_cliente` | **4 fila(s): `dia_cero_defectos_2 -> eliminacion_causas_error_4`, `customer_validation -> establecer_linea_base_mvp`, `dia_cero_defectos_3 -> eliminacion_causas_error_4`, `ganar_comprension_del_cliente -> dia_en_la_vida_del_cliente`** |
| identidad: rama y commit de apertura (leidos de git, no tecleados) | rama `pasada-unica`, commit del acta `d21d5e8b` (asunto real leido de git log: 'ACTA DEL AUDITOR, VUELTA 191: LA 190 REPRODUJO ENTERA Y SIN UNA CIFRA FALSA NI UNA RUTA VACIA.'), HEAD real de apertura `485c2f3e` (sellado antes de la 1.a operacion, leido de git log --diff-filter=A), arboles de `dataset/` IGUALES: VERDE | **rama `pasada-unica`, HEAD de cierre `49f805c1` (leido de `SALIDA_V192_HEAD_CIERRE.txt`, sellado tras la ultima operacion)** |

<!-- FIN CABECERA TALLADA -->

## 1. LAS CINCO TAREAS DEL ENCARGO, Y SU ESTADO

<!-- TABLA DE TAREAS -->
| tarea | que encarga | estado | donde vive la prueba |
|---|---|---|---|
| **TAREA 1** | LOS REGISTROS. BLOQUEANTE. El acta 192 entra en la serie con el numero que devuelve `scripts/loop/serie_de_registros.py`, computado y no tecleado. Con sus DIEZ adjudicaciones `4.1` a `4.10`, y las diez A FAVOR: siete son los discutibles del ejecutor (`D.1` a `D.7`, cuya numeracion en el reporte de la 191 va con el `D.7` escrito ANTES del `D.6`) y las tres restantes son las preguntas y los pendientes de doctrina contestados. OTRA VEZ CERO EN CONTRA, y si el arnes de la 191 ya cubre ese cero, SE DICE CON SU FICHERO en vez de re fabricarlo. Mas los TRES hallazgos de la seccion 5 que no salen de ningun discutible (los dos arneses `SUJETO VIVO` en `5.1`, la cuarta puerta del sello en `5.2`, y el segundo dato independiente sobre la marca contra la dificultad en `5.3`), DOS caidas propias del auditor escritas COMO DOS y ninguna omitida (la `C.1` es DE CIFRA PUBLICADA y va corregida por DECLARACION; la `C.2` es de metodo), CERO caidas del ejecutor que acumulen con las SEIS de metodo que el reporte de la 191 declara, y LA METRICA DE CREDITO de la seccion 7 con sus cifras, incluida la fila de puestos con su nota: 30 aislados y 28 cotejados, SOLAPE TOTAL a proposito. Y EL REGISTRADOR SIGUE SIENDO IDEMPOTENTE: re corrido no escribe nada, y se prueba re corriendolo con la sede medida en bytes antes y despues | **CERRADA** | `SALIDA_V192_T1A_REGISTRO_R54.txt`, `SALIDA_V192_T1A_SIMULACION.txt`, `SALIDA_V192_T1A_MUTACION_REGISTRADOR.txt`, `SALIDA_V192_T1A_RECORRIDO_SIN_ESCRIBIR.txt` |
| **TAREA 2** | LA RELECTURA AL DOBLE DEL TRAMO DE LA 191. BLOQUEANTE. La encarga el AUDITOR, que es donde `AUDITOR.md` 1.2 la pone, y esta vez CON MOTIVO DOBLE: el puesto `2832` cayo FUERA de los dudosos marcados de DOS lectores independientes en DOS tandas seguidas, la del ejecutor en la 191 y la del auditor en la 192. EL TRAMO son los 30 puestos de `docs/loop/SALIDA_V191_T2_CIEGA.txt`, que el bloque `H.3` del sello de apertura midio como el MISMO conjunto que `docs/loop/_auditor_v192_ciega_blind.txt`. AL DOBLE son sus 30 vecinos deterministas, con `vecinos()` IMPORTADA de `scripts/loop/vuelta182_tarea1c_relectura_al_doble.py` y no copiada: 30 mas 30 son 60, el doble exacto. EL SOLAPE SE LE EXIGE AL UNIVERSO Y NO AL TRAMO: a `vecinos()` se le pasa `evitar` con TODO lo consumido, contado de sus SEIS ficheros y no tecleado. Con `scripts/loop/aislador_de_ciega.py`, criterio escrito literal, ciega y destape en ficheros SEPARADOS, las clases escritas y COMMITEADAS en su propio commit ANTES de abrir el destape, y los dudosos NOMBRADOS DELANTE. Y SI EL TRAMO VUELVE A TUMBAR A LOS DOS LECTORES EN LOS MISMOS PUESTOS, SE DICE CON SUS NUMEROS. NO SE TOCA NINGUNA CLASE: `docs/INTRA_DOMINIO_VEREDICTOS.jsonl` se abre solo en lectura y su `sha256` LF abre y cierra en el mismo valor por las dos convenciones | **CERRADA, Y CON TRES DISCREPANCIAS FUERA DEL MARCADO** | `SALIDA_V192_T2_AISLAMIENTO.txt`, `SALIDA_V192_T2_CIEGA.txt`, `SALIDA_V192_T2_MIS_CLASES.txt`, `SALIDA_V192_T2_DESTAPE.txt`, `SALIDA_V192_T2_COTEJO.txt`, `SALIDA_V192_T2_RECUENTO.txt` |
| **TAREA 3** | LOS DOS ARNESES `SUJETO VIVO` DE LA 191, ANTES DE QUE ENTREN EN LA NOMINA. BLOQUEANTE, Y LO ES POR LA BATERIA DE LA 194. Es el hallazgo `5.1` del acta 192, corrido con la guarda de la casa y medido en `docs/loop/_auditor_v192_sujeto_vivo.txt`. (a) CORRER LA GUARDA `guarda_del_sujeto_congelado_separada()` y publicar sus TRES listas sobre los doce arneses de la 191, con sus nombres: si la medicion no da 2 y 6, la del ejecutor manda y la del auditor se declara equivocada, que para eso se publica el comando. (b) ARREGLAR LOS DOS `SUJETO VIVO` para que su sujeto quede CONGELADO, o DECLARAR EL CASO por el carril de los `CASO DECLARADO` que la casa ya tiene: la `4.4` del acta 191 adjudico que `SUJETO VIVO` es FALLO y no deuda, asi que dejarlos como estan no es opcion. (c) LOS SEIS `sin_motivo` NO SON FALLO PERO SI SON DEUDA: nombrarlos y decir, por cada uno, si su sujeto esta vivo de verdad o si solo le falta escribir el motivo, sin arreglarlos a ciegas. (d) NO SE TOCA LA NOMINA: no se poda, no se adelanta y no se le meten entradas nuevas, que la opcion `c` que el fundador RECHAZO el 5 sep 2026 sigue rechazada. (e) CON SU CASO POSITIVO POR MUTACION, que CAIGA si un arnes con sujeto vivo vuelve a colarse hacia la nomina sin declararse | **CERRADA, CON CORRECCION DECLARADA DE LA PREMISA DEL ENCARGO** | `SALIDA_V192_T3_GUARDA.txt`, `SALIDA_V192_T3_DECLARAR_SUJETOS.txt`, `SALIDA_V192_T3_MUTACION_ENTRADA_NOMINA.txt` |
| **TAREA 4** | LA CUARTA PUERTA DEL SELLO DE LA APERTURA DEL AUDITOR. Es el hallazgo `5.2` del acta 192, levantado por el auditor CONTRA SI MISMO. `scripts/loop/apertura_del_auditor.py` impide tocar `git log`, `git status` y `REPORTE.md` antes del sello, y eso FUNCIONO; pero EL SUJETO DE LA CIEGA NO VIVE EN NINGUNO DE LOS TRES: vive en las razones y las clases de `docs/INTRA_DOMINIO_VEREDICTOS.jsonl`, y por ahi se colo el auditor de la 192 con el sello ya escrito y sin romper ninguna guarda (los puestos 156 y 201 de su propia tanda). (a) AL SELLO SE LE ANADE LA CUARTA PUERTA: una funcion del propio fichero para leer el archivo que APUNTE SU TOQUE, y una comprobacion que CAIGA EN ROJO si el turno leyo `clase` o `razon` DE LOS PUESTOS SELLADOS antes de que las clases del auditor esten escritas. No se prohibe leer el archivo entero, que hace falta para el marcador: se prohibe destapar el sujeto. (b) DECIR EN EL PROPIO FICHERO LO QUE ESTA GUARDA NO PUEDE HACER, como su docstring ya hace con las otras tres. (c) CON SU CASO POSITIVO POR MUTACION, que CAIGA si la cuarta puerta se quita. (d) NO SE CLONA EL FICHERO: `apertura_del_auditor.py` tiene nombre estable y sin numero de vuelta, y se le anade, no se le hace una version 2 | **CERRADA** | `SALIDA_V192_T4_MUTACION_CUARTA_PUERTA.txt`, `scripts/loop/apertura_del_auditor.py`, `SALIDA_V182_T2_MUTACION_APERTURA_AUDITOR.txt` (re corrido, reproduce) |
| **TAREA 5** | EL FORMATO UNICO DEL COTEJO DE CIEGA. Es el `P.2` del ejecutor, adjudicado A FAVOR en la `4.9` del acta 192. La TAREA 5 de la 191 midio que el universo se queda en 6 ficheros de 43, y tres cotejos de ciega DE VERDAD (los del 183, 184 y 190) quedan fuera POR FORMATO y no por fondo. ES UN FORMATO ANTES QUE UNA RE MEDICION: (a) ESCRIBIR EL FORMATO UNICO del cotejo de ciega, con nombre estable y sin numero de vuelta, que lleve como minimo y explicitos el puesto, la clase del lector, la clase del archivo, si el puesto estaba en los dudosos del lector, y el COINCIDE o DISCREPA, y que deje el DENOMINADOR RECUPERABLE, porque dos de los seis ficheros de hoy solo listan discrepancias. (b) UN LECTOR QUE LEA LOS FORMATOS VIEJOS y publique CUANTOS de los 43 pasa a recuperar, con sus nombres, y cuantos siguen fuera y por que, con la cifra de antes y la de despues LAS DOS JUNTAS. (c) NO SE RE MIDE LA MARCA CONTRA LA DIFICULTAD EN ESTA VUELTA: el universo nuevo se usa cuando este medido y declarado, no en el mismo acto en que se construye. (d) CON SU CASO POSITIVO POR MUTACION, que CAIGA si un cotejo del formato nuevo no permite recuperar el denominador | **CERRADA** | `SALIDA_V192_T5_LECTOR_DE_VIEJOS.txt`, `SALIDA_V192_T5_MUTACION_FORMATO_COTEJO.txt`, `SALIDA_V192_T5_MUTACION_LECTOR_VIEJOS.txt`, `SALIDA_V192_T2_COTEJO.txt` (primer usuario del formato) |
<!-- FIN TABLA DE TAREAS -->

## 2. LAS TAREAS, UNA POR UNA (cada seccion se ANEXA al cerrarse su tarea)

<!-- ANEXO DE TAREAS -->

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
`docs/loop/SALIDA_V191_T1A_MUTACION_REGISTRADOR.txt`, **disco 6904 bytes | LF 6904
bytes**, `sha256` LF `795c0ec740bdd5cc`, veredicto leido del propio fichero
`VEREDICTO: VERDE`, y la aguja `EN CONTRA` aparece **13** veces dentro. **Si ese
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

### TAREA 2. LA RELECTURA AL DOBLE DEL TRAMO DE LA 191. **CERRADA, Y EL RESULTADO ES MALO PARA MI:** 20 coinciden, 10 discrepan, y **TRES caen FUERA de mis quince dudosos**. Las tres son la MISMA especie de error y la nombro.

**EL SUJETO, ELEGIDO Y AISLADO ANTES DE MIRAR NADA.** Tramo contado de su fichero:
los 30 puestos de `docs/loop/SALIDA_V191_T2_CIEGA.txt`, con el **2832 DENTRO**, y
**el mismo conjunto exacto** que `docs/loop/_auditor_v192_ciega_blind.txt`
(comprobado, no creido). Universo consumido contado de sus **SEIS ficheros y con
sus nombres**: `_auditor_v190_exclusion.txt` (411), `_auditor_v189b_exclusion.txt`
(381), `_auditor_v190_ciega_blind.txt` (30), `_auditor_v189b_ciega_blind.txt`
(30), `SALIDA_V190_T4_CIEGA.txt` (30) y `SALIDA_V191_T2_CIEGA.txt` (30):
**471 sin la tanda de la 191 y 501 con ella**, las dos como el encargo dice.

**`vecinos()` IMPORTADA y no copiada** de
`scripts/loop/vuelta182_tarea1c_relectura_al_doble.py`, con `evitar` = los 501:
**30 vecinos, 60 al doble exacto, SOLAPE 0 con el tramo y 0 con el universo, LOS
DOS POR CONSTRUCCION** (el `evitar` va DENTRO de la llamada, no comprobado
despues). Aislador VERDE, **0 fugas**, ciega y destape en ficheros separados.

**EL ORDEN ES LA PRUEBA Y ESTA EN GIT, no en mi palabra:** el aislamiento y sus
dos ficheros en `0eb8f5ce`; mis clases con **los quince dudosos NOMBRADOS
DELANTE** en su propio commit; y el destape se abrio DESPUES.

**EL COTEJO, EN EL FORMATO UNICO Y COMPUESTO POR EL, NO POR MI.** La tabla la
escribe `scripts/loop/cotejo_de_ciega.py`, que es la pieza `a` de la TAREA 5:
**esta tarea es su primer usuario, y usarlo aqui es la prueba de que sirve** en
vez de una plantilla que nadie ha corrido. Su guarda del denominador, corrida
sobre esta misma salida: **declarado 30, filas contadas 30, VERDE.**

**LAS CIFRAS, COMPUTADAS DE LAS FILAS Y NO TECLEADAS**
(`docs/loop/SALIDA_V192_T2_COTEJO.txt`):

| | cifra | cuales |
|---|---:|---|
| cotejados | **30** | el denominador va declarado y ademas se recupera contando filas |
| COINCIDEN | **20** | |
| DISCREPAN | **10** | |
| mis dudosos, nombrados delante | **15** | |
| discrepancias **DENTRO** de mis dudosos | **7** | 874, 906, 965, 971, 1068, 2425, 2659 |
| discrepancias **FUERA** de mis dudosos | **3** | **1804, 1814, 2833** |
| mi reparto | A 4, B 6, D 20 | |
| reparto del archivo | A 2, D 28 | |

**LAS TRES DE FUERA SON LA MISMA ESPECIE, Y ESO ES LO QUE HAY QUE DECIR.** En las
tres yo puse **A** y el archivo dice **D**, y en las tres mi motivo escrito es el
mismo: *conte cuantos pasos del nodo corto estan en el largo y salio mayoria*.

- **1804** (`gestion_centro_datos_verde` contra `optimizacion_centro_datos_verde`):
  yo conte tres de cinco pasos compartidos. El archivo dice *"uno enfria mejor lo
  mismo, el otro necesita enfriar menos"*, y nombra lo propio de cada uno: el PUE
  con su formula y el calor reaprovechado de un lado, la virtualizacion, la
  renovacion de equipos y la ubicacion geografica del otro.
- **1814** (`eco_eficiencia_critica` contra `menos_malo_vs_bueno`): yo conte dos
  de tres. El archivo dice *"la critica y su reemplazo son dos nodos distintos"*,
  con pasos enteros propios en cada lado.
- **2833** (`carta_de_control_shewhart` contra `control_estadistico_de_procesos_2`):
  yo conte cuatro de cinco. El archivo lo resuelve por **fuentes distintas** (Juran
  contra Deming) y por el **cumulo entero de las cartas de control**, que separa
  cada variante con fuerza, y **su razon ya predice mi lectura con estas
  palabras**: *"DISCUTIBLE MARCADO fuerte: ambos construyen e interpretan una
  carta Shewhart... quien pese ese nucleo dira A"*.

**LA DIFERENCIA SE PUEDE NOMBRAR, Y NO ES DISTRACCION: ES MI VARA.** Mi criterio
para la `A` cuenta **solape de pasos**; la vara de la casa (`BANCO_DE_TEXTOS.md`
9.6.1, LA LINEA O EL PROCEDIMIENTO) pregunta otra cosa: **si uno es una LINEA del
otro desplegada en PROCEDIMIENTO**. Dos nodos pueden compartir la mayoria de sus
pasos y aun asi **traer cada uno pasos enteros propios**, y entonces son
`D`. **Mi criterio, escrito antes de mirar y no cambiado a mitad, mide una cosa
distinta de la que el archivo mide**, y en 3 de 30 esa diferencia me tumba sin
que yo la viera venir. Va como discutible `D.2` de este reporte.

**Y LO QUE NO HAGO, QUE ES LA MITAD DEL ASUNTO: NO ME AUTO ENCARGO LA ESCALADA.**
`AUDITOR.md` 1.2 dice que una discrepancia FUERA del marcado baja el credito de
toda la tanda y que ese tramo se relee al doble. **Aqui son TRES**, no una. **La
`4.5` del acta 192 acaba de adjudicar A FAVOR, y por segunda vez, que el doble
esta en la mano del auditor y no en la mia.** Lo traigo medido, con sus numeros y
sus nombres, y no me lo encargo.

**EL SEGUNDO LECTOR: NO LO HAY SOBRE ESTE TRAMO, Y SE MIDE EN VEZ DE
SUPONERSE.** El encargo pide que, si un tramo vuelve a tumbar a los dos lectores
en los mismos puestos, se diga con sus numeros. **Medido: el solape de esta tanda
con los 30 de `_auditor_v192_ciega_blind.txt` es CERO**, porque el auditor leyo
los 30 de la 191 y estos son sus vecinos. **Sobre este tramo hay UN SOLO
LECTOR**, asi que la via barata de separar el par dificil del lector distraido
**no se puede correr aqui**, y decirlo es la respuesta honrada al encargo.

**LA MARCA `DISCUTIBLE MARCADO`, CONTADA DEL DESTAPE Y NO GLOSADA:** la llevan
**3 de los 30** (2659, 2833, 2912) y **2 de mis 10 discrepancias** (2659, 2833).
**Aqui se cuenta y no se concluye:** el encargo prohibe expresamente re medir la
marca contra la dificultad en esta vuelta.

**Y ALGO QUE DIJE ANTES DE VER NADA Y QUE LA MEDICION CONFIRMA A MEDIAS:** declare
en mis clases, antes del destape, que esta tanda me salia mas dudosa que la de la
191 (15 dudosos de 30 contra 13 de 30) porque muchos pares son *marco contra una
de sus piezas*. **Acerte en que ahi estaba el problema y falle en donde:** de mis
quince dudosos, **siete discreparon**, pero **las tres que me tumbaron sin
marcarlas no eran marco contra pieza: eran las tres que llame `A` por conteo de
pasos**. La prediccion apunto al sitio equivocado y lo digo.

**NO SE TOCO NINGUNA CLASE.** `docs/INTRA_DOMINIO_VEREDICTOS.jsonl` abre y cierra
en **4054129 bytes en disco y 4054129 bytes normalizados a LF**, `sha256` LF
`0a77b5a35a962621`, medido al entrar y al salir en los dos instrumentos de esta
tarea. **Ninguna correccion salio de la relectura**, asi que no hay ninguna que
declarar ni traer.

### TAREA 3. LOS DOS `SUJETO VIVO` DE LA 191. **CERRADA, Y CON UNA CORRECCION DE LA PREMISA DEL ENCARGO:** los dos `SUJETO VIVO` **NO entran en la nomina**, y los que SI entran traen otra deuda.

**(a) LA GUARDA, CORRIDA POR MI, CON SU COMANDO PUBLICADO.**
`VMV.guarda_del_sujeto_congelado_separada(nomina=[(n, True) for n in los_doce])`,
con `VMV` importado y no copiado y la nomina pasada **por parametro**, sin tocar
`VIEJAS`. Los doce se descubren por patron (`^vuelta191_.*\.py$`) y no se
teclean: **salen doce**, como el acta 192 dice.

**LA MEDICION DE APERTURA CALZA CON EL ACTA, Y ESO VA PRIMERO.** El bloque `H.4`
del sello de apertura de esta vuelta, corrido **ANTES de la primera operacion**,
dio **`sujeto_vivo 2` y `sin_motivo 6`**, exactamente lo que el acta 192 publica.
**La medicion del auditor era correcta y lo digo antes de decir lo demas.** Los
dos vivos que nombra son los que nombra: `vuelta191_tarea1a_registrar_acta191.py`
y `vuelta191_tarea3_arreglar_lineas.py`.

**LO QUE NO CALZA ES LA CONSECUENCIA, Y ESO SI ES UNA CIFRA FALSA DEL ACTA.** El
titulo del hallazgo `5.1` dice que los dos *"ENTRAN EN LA NOMINA DE LA BATERIA A
LA VUELTA SIGUIENTE"*. **Eso no se cree: se corre.** La regla de entrada es
`VMV.PATRON_ARNES`, leida del fichero:
`^vuelta(\d+).*(?:mutacion|caso_positivo|simular).*\.py$`. **Exige que el NOMBRE
contenga `mutacion`, `caso_positivo` o `simular`, y ninguno de los dos `SUJETO
VIVO` lo contiene.** Medido:

| | cifra | cuales |
|---|---:|---|
| ficheros `vuelta191_*.py` | **12** | |
| de esos, que el CENSO ve | **3** | `..._tarea3_mutacion_lineas.py`, `..._tarea4_mutacion_veredicto.py`, `..._tarea6_mutacion_bloque_tallado.py` |
| que `arneses_que_faltan()` RECLAMA hoy | **3** | los mismos tres |
| con `SUJETO VIVO` **y** reclamados | **0** | ninguno |

**CORRECCION DECLARADA CONTRA EL ACTA 192, sin borrar lo que corrige:** los dos
`SUJETO VIVO` **no llegan a la nomina por la regla del propio fichero**. La
urgencia que el encargo le pone (*"BLOQUEANTE, Y LO ES POR LA BATERIA DE LA
194"*) **no se sostiene por esa via**. Lo arreglo igual, porque la `4.4` del acta
191 dice que `SUJETO VIVO` es FALLO y el encargo me prohibe dejarlo, **pero la
cifra vieja se queda donde esta y esta correccion va al lado**.

**Y LA URGENCIA SI EXISTE, POR OTRA PUERTA, Y ESA LA TRAIGO YO.** De los TRES que
si entran, **DOS son `NO DECIDIBLE SIN MOTIVO ESCRITO`**
(`vuelta191_tarea3_mutacion_lineas.py`, que nombra `LECTURAS_DIRIGIDAS.md` viva
en su linea 183 y ademas la mide con `wc -l` en la 192; y
`vuelta191_tarea6_mutacion_bloque_tallado.py`, que **abre `docs/loop/REPORTE.md`
vivo** en su linea 108 y se lo pasa a `--comparar`). **Ese es el que puede no
reproducir en la 194**, y **la confirmacion empirica ya esta en el acta 192**:
de los tres arneses que el auditor re corrio, el de la TAREA 3 no reprodujo.

**(b) LOS DOS ARREGLADOS, CADA UNO POR SU CARRIL, PORQUE NO SON EL MISMO CASO.**
Tratarlos igual habria tapado la diferencia:

- **`vuelta191_tarea3_arreglar_lineas.py` ERA UN FALSO POSITIVO, Y ESTA MEDIDO
  ANTES DE DECLARARLO.** Sus seis apariciones de `REPORTE.md` estan **todas
  dentro de literales de `CAMBIOS`, que son patrones de parcheo**: el texto que
  ese fichero busca y sustituye dentro de OTROS scripts. El instrumento cuenta
  sus aperturas de fichero (**6**) y **cuantas nombran el reporte (0)**, y **si
  alguna lo nombrara, PARA y no declara nada**. Carril: la declaracion en el
  propio arnes. **`SUJETO VIVO` -> `CONGELADO`.**
- **`vuelta191_tarea1a_registrar_acta191.py` TIENE EL SUJETO VIVO DE VERDAD:** un
  registrador **tiene que leer el acta de hoy**, y congelarlo lo romperia.
  **Declararlo `CONGELADO` habria sido mentir, y esa mentira es peor que el
  fallo.** Carril: escribir el motivo en cada aparicion, **mas una huella de
  congelado que sea VERDAD Y UTIL y no un literal puesto para enganar a la
  guarda**: ahora **publica el `sha256` LF del acta que acaba de leer**, asi que
  una corrida suya que lea otra acta se puede detectar. **`SUJETO VIVO` -> `NO
  DECIDIBLE CON MOTIVO ESCRITO`**, o sea deuda declarada y no fallo.

**LOS DOS COMPILAN** (`py_compile`, comprobado) y **NINGUNO DE LOS DOS SE HA
CORRIDO**: correrlos pisaria salidas selladas de la 191, y el anclaje se decide
leyendo el TEXTO. Bytes: el primero pasa de **15046 en disco y 15046 en LF** a
**15977 en disco y 15977 en LF**; el segundo, de **78744 en disco y 78744 en LF**
a **79940 en disco y 79940 en LF**.

**UNA CAIDA MIA, CAZADA SIMULANDO Y ANTES DE ESCRIBIR NADA:** mi primer parche
usaba `replace(..., 1)` y el registrador tiene **la misma linea de `p.append`
DOS veces**. Con una sola aparicion sin marca, `motivo_del_sujeto_vivo()` devuelve
False para el fichero entero. La simulacion lo enseño (`motivo escrito: no`) y
`insertar_motivos()` pasa a ir **linea a linea sobre todas las apariciones**, y es
idempotente. **Ninguna cifra falsa salio de aqui porque el modo `--simular` corre
antes de escribir.**

**(c) LOS SEIS `sin_motivo`, NOMBRADOS Y DIAGNOSTICADOS UNO A UNO, Y NO
ARREGLADOS**, que es lo que el encargo pide con esas palabras:

| arnes | sujeto vivo de verdad? | que le falta |
|---|---|---|
| `vuelta191_apertura.py` | **SI.** Un sello de apertura mide el arbol vivo: abre el reporte, el acta y el archivo | solo el motivo escrito, en 9 de sus 11 apariciones |
| `vuelta191_esqueleto_reporte.py` | **SI, y es el que mas.** No solo lee `REPORTE.md`: **lo ESCRIBE** | el motivo, en 7 de sus 14 apariciones |
| `vuelta191_tarea2_relectura_al_doble.py` | **SI, pero SOLO EN LECTURA**: abre el archivo de veredictos y mide su `sha256` al entrar y al salir | solo el motivo, en su unica aparicion (linea 19, la constante `ARCHIVO`) |
| `vuelta191_tarea3_mutacion_lineas.py` | **SI**, y ademas **entra en la nomina**: nombra `LECTURAS_DIRIGIDAS.md` viva y le corre `wc -l` | el motivo, y **es de los dos que de verdad amenazan la 194** |
| `vuelta191_tarea5_marca_contra_dificultad.py` | **SI, SOLO EN LECTURA**: no escribe ni una fila del archivo y lo mide al entrar y al salir | el motivo, en la primera de sus dos apariciones |
| `vuelta191_tarea6_mutacion_bloque_tallado.py` | **SI**, y ademas **entra en la nomina**: **abre `docs/loop/REPORTE.md` vivo** y se lo pasa a `--comparar` | el motivo, y **es el otro que de verdad amenaza la 194** |

**NINGUNO SE ARREGLA AQUI**, porque el encargo lo prohibe expresamente: *"no los
arregles a ciegas"*. **Cuatro de los seis solo necesitan escribir el motivo; dos
necesitan que alguien decida si su sujeto puede congelarse**, y esa decision no
la tomo yo en esta vuelta.

**(d) LA NOMINA NO SE TOCA.** Sigue en **127 entradas**: no se poda, no se
adelanta y no se le anade nada. La opcion `c` que el fundador RECHAZO el 5 sep
2026 sigue rechazada, y quien mete a alguien en la nomina es la regla del
fichero.

**(e) EL CASO POSITIVO POR MUTACION, EN SU PROPIO FICHERO DE NOMBRE ESTABLE:**
`scripts/loop/guarda_de_entrada_a_la_nomina.py`, **VERDE** con **13 casos** y
**cinco mutaciones que caen de verdad**
(`docs/loop/SALIDA_V192_T3_MUTACION_ENTRADA_NOMINA.txt`, **disco 2433 bytes | LF
2433 bytes**). La guarda **cruza lo que ninguna de las dos guardas viejas
cruzaba**: `guarda_del_sujeto_congelado_separada()` mira **la nomina de hoy**, o
sea los que ya entraron, y cuando muerde ya es tarde; `arneses_que_faltan()` mira
**quien va a entrar** pero no mira su anclaje. **La pregunta nueva es el cruce: de
los que el censo RECLAMA, cual tiene el sujeto vivo.**

**Y VIVE EN SU PROPIO FICHERO A PROPOSITO, CON SU CIFRA:** medido en esta vuelta,
**42 entradas de la nomina nombran `verificar_mutaciones_viejas.py`**. La `4.7`
del acta 192 acaba de adjudicar que mover un fichero que la nomina nombra antes
de una bateria pone en riesgo la corrida; si eso vale con CUATRO entradas, vale
mas con CUARENTA Y DOS. **Aqui se importa de alla y no se toca ni un byte de
alla.**

**LO QUE LA GUARDA DICE HOY: VERDE CON DEUDA DECLARADA**, que no es verde a
secas. **FALLO 0** (ningun reclamado sale `SUJETO VIVO`), **DEUDA 2** (los dos de
arriba), **LIMPIO 1**. Y su ceguera va escrita en su propio docstring y probada
por la mutacion `D`: **no ve al que YA esta en la nomina**, para eso esta la otra.

### TAREA 4. LA CUARTA PUERTA DEL SELLO DE LA APERTURA DEL AUDITOR. **CERRADA.** El fichero no se clona: se le anade, y su arnes de la nomina sigue reproduciendo byte a byte.

**(a) LA CUARTA PUERTA, ANADIDA A `scripts/loop/apertura_del_auditor.py`.** **Lo
que el fichero crecio va cercado abajo**, citado de la salida del parche, porque
la primera de las dos cifras es de ANTES y una cifra de bytes suelta al lado de
una ruta se lee como una afirmacion sobre esa ruta HOY:

```
   apertura_del_auditor.py pasa de 14724 a 21223 bytes en disco
   COMPILA
```

Lo que se le anade son **cinco funciones y cuatro constantes**, y ni una linea de
las tres puertas viejas se toca:

- `puestos_sellados()`. **El sujeto lo define el sello y nadie mas:** lee el
  sello del turno, de ahi la ruta de la ciega, y de la ciega sus
  `puesto_intra`. **No se teclean ni se pasan por argumento**, que es lo que
  impide elegir el sujeto despues de mirar.
- `leer_veredictos()`. **APUNTA SU TOQUE**, y por defecto devuelve las filas de
  los puestos sellados **con `clase` y `razon` TAPADAS**. Quien quiera verlas
  tiene que pedir `destapar_sujeto=True`, y entonces el toque que apunta es
  **otro**: el de destape. **Un destape no se puede hacer sin querer.**
- `marcador()`. Cuenta por clase sobre el archivo **entero** y **no destapa
  nada**, porque un agregado de miles de filas no dice la clase de ninguna.
  Existe para que la cuarta puerta **no estorbe lo que el acta si tiene que
  hacer**: recomputar el marcador antes de escribir sus clases.
- `puede_declarar_clases()`, PURA sobre el estado del modulo, **que es la que el
  arnes tumba**.
- `declarar_clases_escritas()`. **CAE EN ROJO y no marca nada** si hubo un
  destape antes. Es el gemelo exacto de `sellar()`: alli el rojo era no poder
  sellar; **aqui es no poder declarar las clases escritas**, que es lo que un
  acta cita como prueba de que leyo a ciegas.

**LA LINEA QUE SEPARA LO PROHIBIDO DE LO PERMITIDO ES TODA LA GUARDA, Y VA
ESCRITA:** no se prohibe leer el archivo entero, que hace falta para el marcador;
**se prohibe DESTAPAR EL SUJETO**, o sea leer `clase` o `razon` **de los puestos
que el sello ya eligio**, antes de que las clases esten escritas.

**Y LA CUARTA PUERTA VA EN SU PROPIA CONSTANTE Y NO DENTRO DE
`PROHIBIDOS_ANTES_DEL_SELLO`, POR UNA RAZON MEDIDA:** aquellas se prohiben
**antes del sello** y esta se prohibe **antes de las clases**, que es otro momento
del turno; y ademas el arnes de la vuelta 182 **recorre esa tupla una a una**, asi
que meterla dentro lo habria roto. Se comprobo re corriendolo, y esta abajo.

**(b) LO QUE ESTA GUARDA NO PUEDE HACER, ESCRITO EN EL PROPIO FICHERO** como su
docstring ya hacia con las otras tres, **y ademas PROBADO en el bloque `G` del
arnes y no solo escrito**: **no puede impedir que alguien abra el `jsonl` por su
cuenta en su terminal**, ni con `python`, ni con `grep`, ni con un editor. El
arnes lo lee a mano y comprueba que **la bitacora sigue vacia y las clases se
pueden declarar igual**. Lo que si puede es que **la declaracion no se pueda
escribir despues** y que **quien se la salte lo haga a sabiendas**. Y una segunda
cosa que no puede, dicha porque es mas fina: **no sabe si lo que se leyo era del
sujeto cuando el archivo se abre por fuera de estas funciones**.

**(c) EL CASO POSITIVO POR MUTACION: VERDE, CON 30 CASOS Y CERO ROJOS**
(`docs/loop/SALIDA_V192_T4_MUTACION_CUARTA_PUERTA.txt`, **disco 4282 bytes | LF
4282 bytes**). **SUJETO CONGELADO:** fabrica su propio archivo, su propia ciega y
su propio sello en un directorio temporal y los retira. **La mutacion que importa
es la `E`:** se sustituye `leer_veredictos()` por **la version sin el apunte de
destape, que es exactamente el codigo de antes de esta vuelta**, y se comprueba
que entonces

- el sujeto **se ve igual**,
- **no queda apuntado ningun destape**, y
- **`declarar_clases_escritas()` sale VERDE**.

**Ese es el agujero, y es el que esta puerta tapa: el sujeto se quema exactamente
igual y el sello sigue saliendo verde.** Hay una segunda mutacion (`F`): con
`CAMPOS_QUE_DESTAPAN` vacio, el tapado deja de tapar. Y las dos restauran lo que
tocaron y lo comprueban.

**(d) NO SE CLONA EL FICHERO.** `apertura_del_auditor.py` conserva su nombre
estable y sin numero de vuelta: **se le anade, no se le hace una version 2**. El
parche lo aplico `scripts/loop/_v192_parche_cuarta_puerta.py`, que es **idempotente
y CAE sin escribir nada si alguna de sus cuatro anclas no aparece**.

**LA COMPROBACION QUE ESTA TAREA SE DEBIA A SI MISMA, Y ES LA MISMA ENFERMEDAD DE
LA TAREA 3:** `vuelta182_tarea2_mutacion_apertura_auditor.py` **esta en la
nomina** y su sujeto es justo el fichero que acabo de tocar. Si su salida sellada
dejara de reproducir, **yo mismo habria roto la bateria de la 194 arreglando la
puerta que existe para no romperla**. Medido antes y despues, con el fichero ya
parcheado:

```
ANTES (identico a HEAD): disco 4982 bytes | LF 4982 bytes | sha256 LF ce85fd0cc659774c
exitcode del re corrido: 0
DESPUES:                 disco 4982 bytes | LF 4982 bytes | sha256 LF ce85fd0cc659774c
REPRODUCE BYTE A BYTE: True
```

Y `git status --porcelain` sobre esa ruta sale **vacio**, o sea identica a `HEAD`.
**Una sola entrada de la nomina nombra este fichero, y esa entrada sigue en
verde.**

**LO QUE ESTA TAREA NO HACE, DICHO PARA QUE NO SE BUSQUE:** no re escribe el acta
192 ni ninguna de sus cifras; los puestos 156 y 201 que el auditor quemo **siguen
declarados donde el los declaro**, y esta puerta no los recupera. **Lo que hace es
que la proxima vez no dependa de que alguien se acuerde**, que es lo que el propio
auditor pidio al levantarlo contra si mismo.

### TAREA 5. EL FORMATO UNICO DEL COTEJO DE CIEGA. **CERRADA.** Los TRES cotejos que el acta nombraba como dejados fuera por formato (183, 184 y 190) **son exactamente los tres que se recuperan**.

**(a) EL FORMATO UNICO, EN `scripts/loop/cotejo_de_ciega.py`**, con nombre estable
y sin numero de vuelta, hermano de `aislador_de_ciega.py` y
`apertura_del_auditor.py`. Lleva **las cinco columnas que el encargo pide y todas
explicitas**: puesto, clase del lector, clase del archivo, si estaba en los
dudosos del lector, y COINCIDE o DISCREPA. **El veredicto no se le pasa: se
computa de las dos clases**, para que no se pueda teclear uno que las contradiga.

**Y LA REGLA QUE LO SOSTIENE ES EL DENOMINADOR: una fila POR CADA PUESTO
COTEJADO, no solo por las discrepancias.** El denominador va **declarado en la
cabecera Y recuperable contando las filas**, y `denominador()` **CAE EN ROJO si
las dos cifras no calzan**. Esa es la enfermedad exacta que la TAREA 5 de la 191
midio: dos de sus seis ficheros solo listaban discrepancias y por eso no se sabia
sobre cuantos pares se midio.

**Y NO ES UNA PLANTILLA QUE NADIE HA CORRIDO: LA TAREA 2 DE ESTA MISMA VUELTA ES
SU PRIMER USUARIO.** `docs/loop/SALIDA_V192_T2_COTEJO.txt` sale de el, y su guarda
corrida sobre esa salida da **declarado 30, filas contadas 30, VERDE**. Se
escribio antes que el resto de esta tarea porque la TAREA 2 necesitaba un cotejo
de todas formas, **y usarlo es la prueba de que sirve**.

**(b) EL LECTOR DE LOS FORMATOS VIEJOS,** en
`scripts/loop/lector_de_cotejos_viejos.py`, tambien de nombre estable, **con sus
CINCO parseadores declarados en el docstring ANTES de contar nada** y cada uno
escrito mirando UN fichero real y nombrado por el: `UNICO`, `COLUMNAS` (la tabla
ancha del 182), `TUBERIA` (la del 190 y la 191), `YO_ARCHIVO` (que cubre las tres
escrituras del 183, el 184, el 189b, el 190 y el 191) y `DISCREPA`, **que es la
regla de la 191 conservada a proposito** porque es la unica que lee ficheros sin
las dos clases, **y lo que recupera es el puesto y nada mas**.

**LAS DOS CIFRAS, PUBLICADAS JUNTAS, QUE ES LO QUE EL ENCARGO PIDE:**

| | recupera | de |
|---|---:|---:|
| ANTES, regla de la TAREA 5 de la 191 | **6** | **43** |
| DESPUES, este lector, sobre los candidatos de HOY | **9** | **46** |
| DESPUES, **cifra comparable**, sin los nacidos en esta vuelta | **8** | **43** |

**Y EL DENOMINADOR DE LAS DOS CIFRAS NO ES EL MISMO, Y ESO SE DICE EN VEZ DE
ESCONDERSE:** la 191 midio sobre **43** candidatos y hoy hay **46**, porque **esta
misma vuelta ha escrito tres ficheros con `COTEJO` en el nombre**
(`SALIDA_V192_T2_COTEJO.txt`, `SALIDA_V192_T5_MUTACION_FORMATO_COTEJO.txt` y
`_auditor_v192_cotejo_ciega.txt`). Comparar 9 contra 6 sin decir eso habria sido
inflar la mejora con mi propia basura.

**EL COTEJO CONTRA LOS SEIS, POR NOMBRE Y NO POR CIFRA**, leidos de
`SALIDA_V191_T5_MARCA_CONTRA_DIFICULTAD.txt` y no de la memoria:

- **SIGUEN DENTRO 5:** `SALIDA_V190_T4_COTEJO.txt`, `SALIDA_V191_T2_COTEJO.txt`,
  `_auditor_v182_cotejo_ciega.txt`, `_auditor_v189b_cotejo.txt`,
  `_auditor_v191_cotejo_ciega.txt`.
- **SALE 1:** `_auditor_v155_cotejo_t3.txt`, **y sale porque este lector es MAS
  ESTRECHO, no mas ancho**: exige las DOS clases Y el denominador, y ese fichero
  solo da el puesto de una discrepancia. **Que la cifra suba con un criterio mas
  estrecho es lo que hace que la subida signifique algo.**
- **ENTRAN 4 QUE NO ESTABAN:** `_auditor_v183_cotejo_ciega.txt`,
  `_auditor_v184_cotejo_ciega.txt`, `_auditor_v190_cotejo_ciega.txt` **y**
  `SALIDA_V192_T2_COTEJO.txt`.

**LOS TRES PRIMEROS SON EXACTAMENTE LOS TRES QUE EL ENCARGO NOMBRA** como *"tres
cotejos de ciega DE VERDAD (los del 183, 184 y 190) que quedan fuera por formato
y no por fondo"*. **Estaban fuera por formato y el formato es lo que se
arreglo.**

**Y CADA UNO PUBLICA DE DONDE SALE SU DENOMINADOR**, que es la mitad del asunto:
del `COTEJADOS: 30` del 183, del `COINCIDEN: 29 de 30` del 184, del `mis clases:
30 | destape: 30` del 190, del `CIFRA puestos mios: 30` del 189b, de la suma de
los dos declarados en el 191, y del conteo de filas en los que si traen
coincidencias.

**UNA CIFRA FALSA CAZADA ANTES DE PUBLICARLA, Y VA DECLARADA:** en la primera
corrida `_auditor_v191_cotejo_ciega.txt` salia con **39 filas y denominador 30**,
que es imposible. La causa esta medida: **ese fichero lista cada discrepancia DOS
VECES**, una en su tabla y otra en su bloque de detalle, y eran **9 duplicadas
sobre 30 puestos distintos**. Se anadio `deduplicar()`, que se queda con la
primera aparicion **y CUENTA cuantas quita, porque una fila descartada en
silencio es una cifra que nadie puede cotejar**; ahora publica **30 filas, 30 de
denominador, y las 9 repetidas dichas al lado**. Y se anadio un aviso que
**publica y no tapa** cualquier fichero con mas filas que denominador.

**(c) NO SE RE MIDE LA MARCA CONTRA LA DIFICULTAD EN ESTA VUELTA**, y el
instrumento lo dice en su propia salida. El universo nuevo **se usa cuando este
medido y declarado, no en el mismo acto en que se construye**: elegir el universo
y sacar la conclusion a la vez es justo lo que la TAREA 5 de la 191 evito bien y
la `4.4` del acta 192 adjudico A FAVOR. **Lo que queda para quien la mida: 8
ficheros comparables, 165 filas con las dos clases y 270 pares de denominador
sumado.**

**(d) LOS CASOS POSITIVOS POR MUTACION, DOS Y NO UNO, PORQUE SON DOS PIEZAS:**

- **Del formato:** `docs/loop/SALIDA_V192_T5_MUTACION_FORMATO_COTEJO.txt` (**disco
  2141 bytes | LF 2141 bytes**), **VERDE**. La mutacion que el encargo pide es la
  `B`: **un cotejo que SOLO lista las discrepancias**, que es la forma de dos de
  los seis ficheros de hoy, y `denominador()` **CAE** y dice que el declarado (3)
  y el contado (1) no calzan. Y hay cuatro mutaciones mas: sin la linea del
  denominador, sin la marca de formato, con la tabla vacia, y **con la cabecera
  mintiendo** (declara 30 y hay 3).
- **Del lector:** `docs/loop/SALIDA_V192_T5_MUTACION_LECTOR_VIEJOS.txt` (**disco
  1961 bytes | LF 1961 bytes**), **VERDE**. Prueba cada parseador sobre su formato,
  que `DISCREPA` recupera menos y **no se prefiere** cuando hay uno completo, las
  cuatro vias del denominador, y **la que importa: sin cabecera y solo con
  discrepancias, el denominador sale `None` y el motivo lo explica, en vez de
  estimarse**.

**LO QUE ESTE FORMATO NO PUEDE HACER, ESCRITO EN SU PROPIO DOCSTRING:** no
convierte en legible un cotejo viejo que no trae la informacion (un fichero que
nunca escribio la clase del lector no la tiene, y ningun lector la recupera), y
**no dice si el lector acerto**, sino si coincide con el archivo, que es otra
cosa: el archivo tambien se equivoca, y esta casa tiene correcciones declaradas
que lo prueban.

<!-- FIN ANEXO DE TAREAS -->

## 3. LO QUE ESTA VUELTA SOSTIENE, Y NI UNA PALABRA MAS

**LAS CINCO TAREAS CERRARON Y NINGUN VEREDICTO DEL ARCHIVO SE MOVIO.**
`docs/INTRA_DOMINIO_VEREDICTOS.jsonl` abre y cierra en **4054129 bytes en disco y
4054129 bytes normalizados a LF**, `sha256` LF `0a77b5a35a962621`, medido en el
bloque de apertura, en los dos instrumentos de la TAREA 2 y otra vez al cierre.

**LO QUE SOSTENGO, UNO A UNO:**

1. **El acta 192 entra como `R.54`**, con el numero computado por
   `serie_de_registros.py` y no tecleado, y **el registrador aprendio tres cosas
   que ninguna maquina heredada sabia leer**. La que importa: **el ejecutor
   declara sus caidas EN RANGO** (`` `C.1` a `C.6` ``), y contar claves distintas
   **da 2 donde el acta declara 6**. Ninguna guarda heredada caza esa cifra falsa,
   porque las dos claves existen de verdad.
2. **La relectura al doble salio MAL PARA MI, y esa es la cifra que cuenta:** 20
   coinciden, 10 discrepan, y **TRES caen FUERA de mis quince dudosos**. Las tres
   son la misma especie: **conte solape de pasos donde la vara de la casa pregunta
   si uno es una LINEA del otro desplegada en PROCEDIMIENTO.**
3. **Los dos `SUJETO VIVO` estan arreglados por carriles distintos**, porque no
   eran el mismo caso: uno era **falso positivo** y el otro **tiene el sujeto vivo
   de verdad y declararlo congelado habria sido mentir**.
4. **La cuarta puerta existe**, y **el arnes de la nomina sobre ese mismo fichero
   sigue reproduciendo byte a byte** (4982 bytes en disco y 4982 en LF, `sha256`
   LF `ce85fd0cc659774c`, antes y despues).
5. **El formato unico existe, ya se uso**, y **recupera exactamente los tres
   cotejos que el acta nombraba** como dejados fuera por formato.

**Y LO QUE NO SOSTENGO, DICHO IGUAL DE FUERTE:** no sostengo que los dos `SUJETO
VIVO` amenazaran la bateria de la 194, **porque medi que no entran en la nomina**;
no sostengo ninguna conclusion sobre la marca contra la dificultad, **porque el
encargo prohibe re medirla aqui**; y no sostengo que mi criterio de lectura sea
el bueno: **medi que en 3 de 30 no lo es.**

## 4. EL ESTADO DEL ARBOL, LEIDO DE LA APERTURA SELLADA Y NO TECLEADO

**LAS CIFRAS DE ESTA SECCION SALEN DE `docs/loop/SALIDA_V192_APERTURA.txt`**, que
se escribio **antes de la primera operacion**, y no de lo que yo recuerde.

- El arbol abrio con **`git status --porcelain`** en **1** linea, y es
  **`?? scripts/loop/vuelta192_apertura.py`**: **el propio bloque de apertura**,
  todavia sin seguir por git cuando su bloque `C` corrio. **`CIFRA ficheros no
  seguidos: 1`**, ese mismo.
- **`git diff --numstat -- dataset/` AL ENTRAR: 0 filas.** **AL SALIR: 0 filas**,
  medido por el paso 4 del ciclo del bloque de cierre. **Las dos cifras se
  publican**, y `dataset/` no se toco a mano en ningun momento.
- **HEAD real de apertura: `485c2f3e`**, sellado en
  `docs/loop/SALIDA_V192_HEAD_APERTURA.txt` **antes de la primera operacion**, y
  es el commit del acta 192.
- **EL DESFASE DEL CALIBRADO SE MIDIO EN LA APERTURA**, dentro de su bloque y
  **antes de la primera operacion**: **4 filas sobre 468 del calibrado**, las
  mismas que al cierre. **Una columna de apertura medida al cierre es caida que
  acumula**, y por eso se midio donde toca.

**LAS CIFRAS DEL ENCARGO, COMPROBADAS UNA A UNA CONTRA EL INSTRUMENTO Y NO
COPIADAS.** El bloque de apertura las computa todas y publica LAS DOS cuando
discrepan:

| lo que el encargo dice | lo que el instrumento midio | |
|---|---|---|
| el siguiente libre de la serie es `R.54` | `R.54`, con 45 entradas, 0 colisiones y 0 huecos | CALZA |
| son DIEZ adjudicaciones `4.1` a `4.10` | 10 claves con el patron suelto; 0 con el entrecomillado | CALZA |
| las diez van A FAVOR y ninguna EN CONTRA | 7 discutibles, los 7 A FAVOR, 0 EN CONTRA; y 3 preguntas contestadas con marcas nuevas | CALZA en el fondo, y el reparto se publica |
| son TRES los hallazgos de la seccion 5 | 3 claves `5.n` | CALZA |
| DOS caidas propias del auditor, una de cifra publicada | 2, con 0 huerfanas, y la especie leida del parrafo: `C.1` de cifra publicada, `C.2` de metodo | CALZA |
| SEIS caidas del ejecutor, de metodo | 6, **expandiendo el rango** `` `C.1` a `C.6` ``; contando claves distintas darian 2 | CALZA, y las dos cifras se publican |
| en el reporte de la 191 el `D.7` va antes del `D.6` | CALZA por la vara del titulo del discutible; NO CALZA por la de la mencion suelta, y las dos se publican | CALZA por la que responde |
| el tramo de la TAREA 2 son 30 puestos y el 2832 esta dentro | 30, y el 2832 DENTRO | CALZA |
| son los mismos 30 que el auditor releyo | diferencia simetrica 0 | CALZA |
| 471 consumidos por la 191, 501 con su tanda | 471 y 501, contados de sus seis ficheros | CALZA |
| el archivo cierra en `0a77b5a35a962621` | identico, y por las dos convenciones | CALZA |
| la guarda da `sujeto_vivo 2` y `sin_motivo 6` sobre los doce | 2 y 6 en la apertura, antes de tocar nada | CALZA |
| los dos `SUJETO VIVO` **entran en la nomina a la vuelta siguiente** | **NO ENTRAN**: la regla de entrada exige `mutacion`, `caso_positivo` o `simular` en el NOMBRE, y de los DOCE el censo ve TRES, ninguno de ellos con sujeto vivo | **NO CALZA, y va como correccion declarada** |
| el sello del auditor: disco 1145 bytes y LF 1145 bytes, ciega disco 41952 bytes y LF 41952 bytes, destape disco 33884 bytes y LF 33884 bytes | identicos, y sus dos `sha256` CALZAN contra el sello | CALZA |
| SEIS vueltas seguidas cierran su propio reporte (186 a 191) | **SIETE** (185 a 191), contadas del inventario entero por `vuelta192_racha_de_cierres.py`; el acta 191 venia contando CINCO | **NO CALZA, y las cuatro cifras se publican** |

## 5. LAS CORRECCIONES DECLARADAS DE ESTA VUELTA

**NINGUNA BORRA LO QUE CORRIGE**, que es la regla (`EJECUTOR.md` 8).

**5.1 CONTRA EL ACTA 192: LOS DOS `SUJETO VIVO` NO ENTRAN EN LA NOMINA.** El
titulo del hallazgo `5.1` dice que *"ENTRAN EN LA NOMINA DE LA BATERIA A LA VUELTA
SIGUIENTE"*, y el encargo hace bloqueante la tarea *"por la bateria de la 194"*.
**Medido con la regla del propio fichero**, `VMV.PATRON_ARNES`: de los DOCE
ficheros de la 191, **el censo ve TRES**, `arneses_que_faltan()` **reclama esos
TRES**, y **con `SUJETO VIVO` y reclamados: CERO**. **La cifra vieja se queda donde
esta.** Lo que NO cambia: **la medicion de `2` y `6` del auditor era correcta**, y
el arreglo se hizo igual porque la `4.4` del acta 191 dice que `SUJETO VIVO` es
FALLO.

**5.2 CONTRA MI PROPIO SELLO DE APERTURA: LA RACHA DE CIERRES.** El bloque `B.2`
de mi apertura publico **racha 7** mirando una **VENTANA TECLEADA** de 185 a 191:
**esa cifra es el borde de mi ventana y no la racha**. Lo cace antes de publicarlo
y escribi `scripts/loop/vuelta192_racha_de_cierres.py`, que cuenta del
**inventario entero**: **10 ficheros de cierre en disco, 9 en verde, racha seguida
de 7 (185 a 191), cortada por la 184**, que tiene fichero y no trae la linea de
piezas. **Las cuatro cifras se publican juntas**: 5 del acta 191, 6 del encargo, 7
de mi ventana, 7 del inventario. Que la ventana acertara por casualidad no la hace
una medicion.

**5.3 CONTRA MI PRIMER PARCHE DE LA TAREA 3, CAZADA SIMULANDO.** Mi primer parche
usaba `replace(..., 1)` y el registrador tiene **la misma linea DOS veces**; con
una sola aparicion sin marca, `motivo_del_sujeto_vivo()` devuelve False para el
fichero entero. **Lo enseño el modo `--simular`, que corre antes de escribir**, y
`insertar_motivos()` pasa a ir linea a linea sobre todas las apariciones.
**Ninguna cifra falsa llego a publicarse.**

**5.4 CONTRA MI PRIMERA CORRIDA DEL LECTOR DE COTEJOS VIEJOS.**
`_auditor_v191_cotejo_ciega.txt` salia con **39 filas y denominador 30**, que es
imposible. Causa medida: **ese fichero lista cada discrepancia DOS VECES**, 9
duplicadas sobre 30 puestos distintos. Se anadio `deduplicar()`, **que cuenta
cuantas quita**, y un aviso que publica cualquier fichero con mas filas que
denominador. **Se cazo mirando la salida antes de pegarla en el reporte.**

**5.5 SOBRE EL ORDINAL DEL DESFASE DE `PATRONES_ACTA`.** El reporte de la 191 se
llama a si mismo **la SEPTIMA vuelta** del desfase. **Esa palabra no sale de
ningun instrumento**, asi que no la copio ni le sumo uno a ojo: lo que si se puede
contar es que **3 reportes archivados traen el literal `DESFASE DECLARADO`** (189,
190 y 191). **Las dos cifras van publicadas en la seccion 0 y la discrepancia se
declara en vez de resolverse copiando.**

## 6. PENDIENTES DE DOCTRINA

**NINGUNO NUEVO.** Las cinco tareas se resolvieron con reglas vigentes, y donde
hizo falta una decision que no me toca **la traigo como pregunta en la seccion 7
en vez de inventar la regla**.

## 7. LAS PREGUNTAS QUE TRAIGO

**`P.1` LA ESCALADA DE MI PROPIA TANDA, QUE NO ME AUTO ENCARGO.** La TAREA 2 dio
**TRES discrepancias FUERA de mis dudosos**, no una. `AUDITOR.md` 1.2 dice que eso
baja el credito de toda la tanda y que el tramo se relee al doble, **y la `4.5`
del acta 192 acaba de adjudicar por segunda vez que el doble esta en la mano del
auditor y no en la mia**. Lo traigo medido, con sus numeros y sus nombres. **La
pregunta es si tres de una vez cambia algo del regimen, o si es el mismo doble de
siempre.**

**`P.2` LOS DOS `NO DECIDIBLE SIN MOTIVO` QUE SI ENTRAN EN LA NOMINA.**
`vuelta191_tarea3_mutacion_lineas.py` corre `wc -l` sobre `LECTURAS_DIRIGIDAS.md`
viva, y `vuelta191_tarea6_mutacion_bloque_tallado.py` **abre `docs/loop/REPORTE.md`
vivo** y se lo pasa a `--comparar`. **Son los que de verdad pueden no reproducir
en la 194**, y el auditor ya vio a uno de ellos no reproducir. **El encargo me
prohibe arreglarlos a ciegas y no los toco.** La pregunta es si se les escribe el
motivo (deuda declarada) o si se les congela el sujeto, **que es una decision
sobre lo que esos arneses tienen que probar y no una decision mia**.

**`P.3` LA VARA CON LA QUE LEO.** Mis tres discrepancias de fuera del marcado
salen todas de contar **solape de pasos**, y la vara de la casa (`9.6.1`) pregunta
**si uno es una LINEA del otro desplegada en PROCEDIMIENTO**. **No cambio mi
criterio a mitad de camino y no lo cambio ahora**, porque cambiarlo despues de ver
el resultado es lo que la `4.4` del acta 192 acaba de adjudicar como trampa. **La
pregunta es si el criterio escrito para las ciegas debe pasar a ser el del banco,
y quien lo decide.**

## 8. LAS CAIDAS PROPIAS DE ESTA VUELTA, LO QUE QUEDA EN ROJO, Y LOS DISCUTIBLES

**CAIDAS PROPIAS: CUATRO, LAS CUATRO DE METODO Y NINGUNA LLEGO A PUBLICAR UNA
CIFRA FALSA.** Van con su clave y su cabecera, que es la forma de la casa, y las
tres primeras remiten a la correccion declarada que las repara en la seccion 5.
**TRES LAS CACE YO Y LA CUARTA ME LA CAZO LA MAQUINA**, y esa diferencia se dice
en vez de difuminarse. **Cero caidas de cifra publicada y cero rutas vacias.**

**`C.1`. MEDI UNA RACHA SOBRE UNA VENTANA QUE TECLEE YO.** El bloque `B.2` de mi
sello de apertura publico **racha 7** mirando de la 185 a la 191, **y esa ventana
la escribi a mano**: una racha que se corta justo donde acaba la ventana que uno
eligio no es una medicion de la racha. **La cazo yo mirando el inventario de disco
antes de publicar el reporte**, y la reparacion es
`scripts/loop/vuelta192_racha_de_cierres.py`, que cuenta del inventario entero.
Correccion declarada `5.2`. **De metodo: la cifra final no cambio, pero pudo
haber cambiado y yo no lo habria sabido.**

**`C.2`. PARCHEE CON `replace(..., 1)` UN FICHERO QUE TENIA LA LINEA DOS VECES.**
El registrador de la 191 repite la misma linea de `p.append`, y con una sola
aparicion sin marca `motivo_del_sujeto_vivo()` devuelve False para el fichero
entero. **La cazo el modo `--simular`, que corre antes de escribir**, y la
reparacion es `insertar_motivos()`, que va linea a linea sobre todas las
apariciones y es idempotente. Correccion declarada `5.3`. **De metodo: nada llego
al disco mal.**

**`C.3`. MI LECTOR DE COTEJOS VIEJOS SACO 39 FILAS SOBRE UN DENOMINADOR DE 30.**
Es imposible por construccion y lo era por una causa medible: ese fichero lista
cada discrepancia dos veces. **La cazo yo leyendo la salida antes de pegarla en el
reporte**, y la reparacion es `deduplicar()`, que ademas CUENTA cuantas quita.
Correccion declarada `5.4`. **De metodo: la cifra falsa no salio de la salida del
instrumento.**

**`C.4`. PUBLIQUE DOS PARES DE BYTES DE ANTES EN PROSA, AL LADO DE SU RUTA, Y
ESTA ME LA CAZO LA MAQUINA Y NO YO.** La TAREA 1 escribia `998216 / 998216` cerca
de `SALIDA_V192_T1A_RECORRIDO_SIN_ESCRIBIR.txt`, y la TAREA 4 escribia
`14724 / 14724` como el ANTES de `apertura_del_auditor.py`. **Las dos cifras eran
CIERTAS y la guarda tiene razon igual:** una pareja de bytes en prosa, junto a una
ruta, se lee como una afirmacion sobre esa ruta HOY, y hoy esos ficheros miden
otra cosa. **`cerrar_reporte.py` se nego a escribir el reporte hasta que las
arregle**, con las cuatro parejas nombradas y su linea. El remedio es el que la
casa ya tiene para las citas: **la cerca**, que es lo que esas dos cifras son.
**Ninguna cifra se borro: se movieron a su bloque cercado con su procedencia.**
**Es la misma especie que la `C.6` del reporte de la 191, y la anoto asi: la
guarda que existe para cazar esto lo cazo, que es exactamente para lo que se
construyo.** **Y el reporte no se parcheo por encima: se rehizo entero**, tallando
otra vez el esqueleto y re anexando las cinco secciones desde sus ficheros, para
que el cierre salga de UNA corrida consistente. **El PASO 0 archivo el reporte
parcial antes de pisarlo**, asi que la version que el cerrador declaro roja no se
perdio: vive en `docs/loop/reportes/` y en el commit anterior.

**LO QUE QUEDA EN ROJO: NADA EN ROJO, Y UNA COSA EN AMBAR QUE SE DECLARA.** La
guarda de entrada a la nomina sale **VERDE CON DEUDA DECLARADA**, que no es verde
a secas: **2 de los 3 arneses que entran traen un sujeto vivo sin motivo
escrito**. Va como `P.2`.

**LOS DISCUTIBLES, MARCADOS ANTES DE SABER SI ACIERTO:**

**`D.1` (DE VARA). EL NUMERAL DE LA FILA DECIDE CUANTOS HALLAZGOS CUENTAN FUERA,
Y ESTA VEZ EL COTEJO POR SUBCADENA RESUELVE CERO DE TRES.** La fila del acta dice
**3** y la seccion tiene **3** claves `5.n`, asi que calzan; pero las tres piezas
del parentesis (*2832*, *dos arneses de sujeto vivo*, *cuarta puerta del sello*)
**no aparecen dentro de ninguno de los tres titulos**. **Acepte el numeral igual**,
que es lo que la `4.1` del acta 192 adjudico A FAVOR hace una vuelta. **Lo marco
porque el 3 pudo salir de una coincidencia**: la fila nombra el `2832`, que no es
un `5.n`, y no nombra el `5.3`.

**`D.2` (DE CRITERIO, Y ES EL QUE MAS ME PESA). NO CAMBIE MI CRITERIO DE LECTURA
AUNQUE ME TUMBO TRES VECES.** Mis clases se escribieron con el mismo literal de la
190 y la 191, y **las tres discrepancias de fuera del marcado salen de contar
solape de pasos**. Pude reescribirlo despues del destape y **no lo hice**, porque
un criterio que se ensancha despues de ver el resultado no mide nada. **Lo marco
porque la alternativa (adoptar la vara `9.6.1` para las ciegas) puede ser lo
correcto y yo no lo adjudico.**

**`D.3` (DE ALCANCE). ESCRIBI LA PIEZA `a` DE LA TAREA 5 ANTES DE LA TAREA 5, Y LA
USE EN LA TAREA 2.** El formato unico se escribio cuando la TAREA 2 necesitaba un
cotejo, y esa tarea es su primer usuario. **Lo defiendo asi: una plantilla que
nadie ha corrido no esta probada, y usarla en la tarea que la necesitaba es la
prueba mas barata que hay.** **Lo marco porque adelanta una pieza de una tarea
posterior**, y quien lea el orden de los commits lo vera.

**`D.4` (DE ALCANCE). TOQUE `apertura_del_auditor.py`, QUE UNA ENTRADA DE LA
NOMINA NOMBRA, ANTES DE LA BATERIA DE LA 194.** Es exactamente el riesgo que la
`4.7` del acta 192 usa para dejar `tallar_cabecera_reporte.py` fuera de esta
vuelta. **Lo hice porque el encargo lo pide con esas palabras**, y **lo comprobe en
vez de confiar**: re corri el arnes con el parche puesto y su salida sellada
reproduce byte a byte. **Lo marco porque la comprobacion la elegi yo y podia
haberme salido mal.**

**`D.5` (DE ALCANCE). PUSE LA GUARDA NUEVA EN UN FICHERO PROPIO EN VEZ DE DENTRO
DE `verificar_mutaciones_viejas.py`.** La razon esta medida (**42 entradas de la
nomina lo nombran**) y es la misma que la `4.7`. **Lo marco porque el precio es una
guarda mas que hay que acordarse de correr**, y esta casa sabe lo que le pasa a lo
que hay que acordarse de correr.

**`D.6` (DE FONDO). LE ANADI A UN INSTRUMENTO DE UNA VUELTA CERRADA UNA LINEA QUE
CAMBIA SU SALIDA.** `vuelta191_tarea1a_registrar_acta191.py` ahora publica el
`sha256` del acta que lee, y **eso no es solo un comentario: es comportamiento**.
Lo hice porque **una huella de congelado falsa habria sido peor**, y porque la
`4.3` del acta 192 adjudico A FAVOR tocar codigo de vueltas cerradas mientras no
se reescriba una cifra publicada ni una salida de la nomina. **Lo marco porque es
lo mas invasivo que hice, y porque no lo corri: el anclaje se decidio leyendo el
texto, y correrlo habria pisado una salida sellada de la 191.**

**`D.7` (DE UNIVERSO). MI LECTOR DE COTEJOS VIEJOS SACA A UNO DE LOS SEIS QUE
ENTRABAN.** `_auditor_v155_cotejo_t3.txt` sale porque exijo **las dos clases Y el
denominador**. **Lo defiendo asi: un criterio mas estrecho que ademas sube la
cifra dice algo; uno mas ancho no diria nada.** **Lo marco porque el universo
cambio de forma y no solo de tamano**, y quien mida la marca contra la dificultad
sobre el universo nuevo estara midiendo sobre otro conjunto.

## 9. LA BATERIA DE MUTACIONES: HUECO DECLARADO Y MEDIDO

**HUECO DECLARADO Y MEDIDO. LA BATERIA DE LA VUELTA 192 NO CORRIO, Y EL HUECO SE DECLARA EN VEZ
DE RELLENARSE CON OTRA COSA.**

**EL NOMBRE DEL FICHERO:** `docs/loop/SALIDA_V192_BATERIA.txt`.

**CUAL DE LOS DOS CASOS ES: EL FICHERO NO EXISTE.** `os.path.exists`
devuelve NO, asi que `os.path.getsize` **no llego a correr sobre el** y no
hay ninguna medicion suya que publicar. Lo que esta seccion recibio de
bateria, medido y no supuesto, son **0 bytes en disco y 0 bytes
normalizados a LF**, **y ese cero sale de que no hay fichero, no de una
medicion sobre uno**. La distincion es del fundador, escrita el 5 sep 2026
en el punto 3 de `la-bateria-sin-techo-DECISION.md`, que nombra los dos
casos y no los confunde.

ATRIBUCION: por AUDITOR.md 6.1, decision del fundador del 5 sep 2026, la bateria de mutaciones corre CADA CINCO VUELTAS en una vuelta propia que no lleva nada mas. La 189 la corrio ENTERA y sus diez tramos siguen sellados en disco. Por esa cadencia LA SIGUIENTE VUELTA DE BATERIA ES LA 194, y esta vuelta NO es de bateria: su encargo se lo dice con esas palabras y su sello de apertura lo escribe en la primera linea. Lo que esta vuelta SI hizo tocando el radio de la bateria es MIRARLO ANTES: la TAREA 3 escribio guarda_de_entrada_a_la_nomina.py, que cruza lo que ninguna guarda cruzaba, de los que el censo RECLAMA cual tiene el sujeto vivo, y sale VERDE CON DEUDA DECLARADA, cero fallos y dos deudas nombradas. La nomina NO se toco y sigue en 127 entradas leidas del instrumento, asi que la 194 la encontrara completa; la opcion c que el fundador RECHAZO el 5 sep 2026 sigue rechazada. Y el unico fichero de la nomina cuyo sujeto toque, apertura_del_auditor.py por la TAREA 4, se re corrio con el parche puesto y su salida sellada reproduce byte a byte.

**POR QUE ESTO CIERRA Y UNA AUSENCIA MUDA NO.** La pieza (4) de este
instrumento admite el hueco declarado desde la vuelta 173, TAREA 1.b
(adjudicacion 6.2 del acta del auditor de la vuelta 172), y la letra es
estrecha: **el nombre, los bytes medidos y la atribucion, LAS TRES JUNTAS**.
Faltando cualquiera de las tres, este instrumento sigue cayendo en ROJO, y
**una corrida de otra vuelta pegada aqui tampoco vale**.
