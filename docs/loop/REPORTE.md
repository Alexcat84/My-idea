# REPORTE DE LA VUELTA 195 (ejecutor). FASE III, EJECUCION. Rama `pasada-unica`.

> **ESTE REPORTE SE ABRIO AL EMPEZAR LA VUELTA Y CRECE POR ANEXION** (`EJECUTOR.md`
> 1, "EL REPORTE ABRE CON LA VUELTA"). El esqueleto lo tallo
> `scripts/loop/vuelta195_esqueleto_reporte.py`; cada tarea ANEXA SU FILA AL
> CERRARSE; y el cierre lo talla entero `scripts/loop/cerrar_reporte.py`. **Si esta
> vuelta se corta, las filas que sigan diciendo ABIERTA, SIN CERRAR son las que no
> se hicieron.**
>
> **ESTA NO ES VUELTA DE BATERIA.** `AUDITOR.md` 6.1, decision del fundador del 5
> sep 2026: la bateria corre **CADA CINCO VUELTAS** en una vuelta propia **que no
> lleva nada mas**, **la 194 la corrio entera por sus diez tramos** y **la proxima
> cae en la 199**. **La seccion 9 de este reporte cierra con el HUECO DECLARADO Y
> MEDIDO** por el carril de la TAREA 1.b de la vuelta 173, con su medicion, su
> atribucion y su corrida. **Un hueco declarado no es un hueco escondido.**
>
> **VAN CUATRO SUB-TAREAS Y DOS SON BLOQUEANTES.** El tope de CINCO esta ganado y
> **la cifra se conto del instrumento en esta vuelta**, no se heredo: el bloque `E`
> del sello de apertura corrio `scripts/loop/vuelta193_racha_de_cierres.py`
> sobre el inventario ENTERO. `AUDITOR.md` 6.2 pedia DOS vueltas seguidas cerrando
> su propio reporte con `cerrar_reporte.py`.
>
> **EL BLOQUE DE APERTURA CORRIO EL CICLO COMPLETO, `tsc` Y `pnpm test`
> INCLUIDOS**, y **escribio el mismo los dos literales que la guarda `D.1` de
> `cerrar_reporte.py` busca en la seccion 4**. Esas eran las dos caidas `C.1` y
> `C.2` que el reporte de la 194 se declaro en su seccion 8.1, heredadas dos
> vueltas seguidas por clonar el bloque sin leer esa seccion, que es lo que su
> propia `C.3` nombraba como causa. **Aqui se leyo la seccion 8.1 ANTES de clonar.**
> **El desfase de calibrado se midio DENTRO del bloque de apertura y ANTES de la
> primera operacion.**
>
> **LO QUE NO ENTRA:** ni cribado, ni recomputo, ni operaciones del plan, ni las
> mesas anotadas, ni **podar la nomina**, ni **la bateria entera**, que no es su
> vuelta y cae en la 199. **Y siguen fuera, nombradas para que la 196 no las
> redescubra:** el desfase de `PATRONES_ACTA`, **que el encargo de la 195 pasa
> EXPRESAMENTE a la 196 y EN PRIMER LUGAR DE LA COLA**, con su motivo dicho (las
> cuatro de hoy atacan causas y esa es cosmetica de cabecera); la fila de credito
> del acta con su rotulo arreglado **en el instrumento que la talla**; la guarda de
> codigo del hallazgo `5.3` del acta 194 (mensajes de commit sin clases por puesto
> ni reparto de ciega), **que a mano YA FUNCIONA Y ESTA MEDIDO** y cuya guarda
> durable sigue pendiente; `acumulan()` que lea la tabla o que declare en su salida
> que no es la sede; el cotejo de clon declarado que separa sentencia de codigo de
> cambio de texto; la excepcion que publica siempre su lista; la medicion del censo
> de arneses con carril de mutacion sin fichero propio; las ocho actas sin entrada
> propia en la serie (173 a 180), medidas y no arregladas; que el campo `evidencia`
> de `OP-L-02` nombre los ficheros que ya existen, **cuyo ESTADO NO SE MUEVE: sigue
> en `LISTA`**; y **QUE HACER CON LAS 72 FILAS `B` DEL ARCHIVO**, nombrado y medido
> y **no resuelto, porque mover una clase es del RECOMPUTO**.
>
> **NO SE MUEVE NINGUN VEREDICTO:** el `sha256` LF de
> `docs/INTRA_DOMINIO_VEREDICTOS.jsonl` abre y tiene que cerrar en el mismo valor.
> **Y no se toca `dataset/` a mano**: el `numstat` se mide al entrar y al salir y
> **las dos cifras se publican**.

**EL VEREDICTO DE UNA LINEA: SIN ESCRIBIR TODAVIA.** Se talla al cierre.

## 0. LA IDENTIDAD Y LA CABECERA, TALLADAS Y NO TECLEADAS

**LA IDENTIDAD, LEIDA DE GIT EN ESTA VUELTA** por
`scripts/loop/vuelta195_esqueleto_reporte.py`, con
`git rev-parse --abbrev-ref HEAD`, `git log` y `git log --diff-filter=A`, y CAE
EN ROJO si algo no se encuentra o es ambiguo:

- rama: `pasada-unica`
- commit del acta de la vuelta 194: `edff6568`. **Su asunto real va CERCADO
  ABAJO, y no suelto en esta prosa**, porque un asunto de acta puede traer DENTRO
  cifras de bytes y `sha256` suyas, y una guarda que mira renglon a renglon no
  distingue una cita de una afirmacion.

```
'ACTA DEL AUDITOR, VUELTA 194: LA 193 REPRODUJO ENTERA, PERO SU BATERIA LLEGA CON UNA GUARDA QUE SE DA VERDE A SI MISMA, Y MI PROPIA CIEGA VENIA QUEMADA DESDE EL CONTEXTO DE LA SESION.'
```
- **DESFASE DECLARADO, Y SU ORDINAL NO SE TECLEA, Y LLEVA SU FECHA DE CORTE.** La
  linea de arriba nombra el acta **194** porque `PATRONES_ACTA` pide la de
  `VUELTA - 1`, y **el acta que ORDENA esta vuelta es la 195**. Es el `D.2` del
  reporte de la 184, adjudicado a favor con reparacion encargada por la `5.2` del
  acta 185, **y el encargo de esta vuelta lo pasa EXPRESAMENTE a la 196 y EN
  PRIMER LUGAR DE LA COLA**, con su motivo dicho. Lo que si se puede
  contar: **6 reportes archivados traen el literal `DESFASE DECLARADO`**
  (`REPORTE_V189.md`, `REPORTE_V190.md`, `REPORTE_V191.md`, `REPORTE_V192.md`, `REPORTE_V193.md`, `REPORTE_V194.md`), contados por `reportes_con_el_literal()` de este mismo fichero,
  **con FECHA DE CORTE 2026-09-06** (banco `9.21`, TODA CIFRA DE CRUCE LLEVA SU
  FECHA DE CORTE). **Un inventario que crece cada vuelta sin corte envejece solo.**
- HEAD real de apertura, sellado ANTES de la primera operacion en
  `docs/loop/SALIDA_V195_HEAD_APERTURA.txt`: `124a18a8`
- commit de nacimiento del bloque de apertura, leido con
  `git log --diff-filter=A`: `8bb20f7c`
- reporte que este esqueleto pisa, leido de la cabecera de ese mismo fichero:
  la vuelta **194**, ya archivada byte a byte antes de escribir aqui
- commit de cierre: se talla al cierre. **Un reporte no puede nombrar el commit
  que lo lleva.**

<!-- CABECERA TALLADA -->
**PENDIENTE DE TALLAR AL CIERRE, Y SE DICE EN VEZ DE RELLENARLA.** La tabla sale
de `scripts/loop/tallar_cabecera_reporte.py --fase04 --vuelta 195`. **Esta
vuelta corrio el bloque de apertura entero ANTES de su primera operacion**, asi
que la mitad izquierda ya se puede leer: corrido aqui, el tallador dice **"ROJO, 19 celdas no se pudieron leer"**, y de las lineas de
rojo que imprima, **0 mencionan APERTURA**. Este hueco se rellena con la
tabla tallada entera cuando la vuelta cierre.
<!-- FIN CABECERA TALLADA -->

## 1. LAS CUATRO TAREAS DEL ENCARGO, Y SU ESTADO

<!-- TABLA DE TAREAS -->
| tarea | que encarga | estado | donde vive la prueba |
|---|---|---|---|
| **TAREA 1** | LOS REGISTROS. BLOQUEANTE. El acta 195 entra en la serie con el numero que devuelve `scripts/loop/serie_de_registros.py`, computado y no tecleado. La entrada registra, y cada cifra se cuenta del cuerpo acotado del acta: LAS DIEZ ADJUDICACIONES `4.1` a `4.10`, y LAS DIEZ A FAVOR (siete son los discutibles `D.1` a `D.7` del reporte de la 194 y las tres restantes son las preguntas `P.1`, `P.2` y `P.3`, dos contestadas por extension citable con la cita comprobada contra su fichero), CERO EN CONTRA y es la QUINTA acta seguida; LOS TRES HALLAZGOS DE LA SECCION 5 que no salen de ningun discutible (`5.1` la fila de credito del acta 194 que rotula mal su cifra, `5.2` el rojo de la bateria que SI es reparable, `5.3` `--componer` que publica VERDE sobre diez tramos rojos); CERO CAIDAS DEL EJECUTOR EN LA VUELTA 194, de cifra publicada y de reporte, con LA RACHA DE REPORTE VUELTA A CERO desde el 1 que dejo el acta 194, y SIN ESCALADA QUE ENCARGAR, dicho expresamente para que no se lea como olvido; UNA CAIDA PROPIA DEL AUDITOR, `C.1`, DE METODO (leer `clase` y `razon` del archivo con `json` a mano en vez de por `AP.marcador()` y `AP.leer_veredictos()`, que es la cuarta puerta y ya ofrecia las dos cosas sin coste), con el sujeto NO quemado y probado DESPUES por la propia puerta: 30 de 30 sellados vuelven TAPADOS y 0 destapes apuntados; LA METRICA DE CREDITO de la seccion 7 con sus cifras, incluida la fila de puestos (30 aislados, 30 cotejados, CERO QUEMADOS, que es la diferencia con la 194 y se debe a que los mensajes de commit del ejecutor ya no publican clases por puesto: ESO FUNCIONO); y LA FILA DE CAIDAS PROPIAS PARTIDA EN DOS, las que ACUMULAN y el total del cuerpo, que es el remedio del hallazgo `5.1` aplicado por el auditor a su propia tabla. Y EL REGISTRADOR SIGUE SIENDO IDEMPOTENTE: se prueba re corriendolo, con la sede medida en bytes antes y despues | **CERRADA. R.57 escrita, idempotencia probada en bytes, y el lector tuvo que cambiar TRES veces** | `SALIDA_V195_T1A_REGISTRO_R57.txt`, `SALIDA_V195_T1A_RECORRIDO_SIN_ESCRIBIR.txt`, `SALIDA_V195_T1A_MUTACION_REGISTRADOR.txt`, `SALIDA_V195_T1A_SIMULACION.txt` |
| **TAREA 2** | LA RELECTURA AL DOBLE DEL TRAMO DEL AUDITOR. BLOQUEANTE, Y ES DEUDA SUYA QUE PAGA EL EJECUTOR CON EL INSTRUMENTO. `AUDITOR.md` 1.2: dos discrepancias del auditor cayeron FUERA de su marcado, `654` y `719`, asi que EL CREDITO DE SU TANDA BAJA Y EL TRAMO SE RELEE AL DOBLE. El tramo y el doble estan CERRADOS DESDE ANTES, computados y no tecleados, en `docs/loop/_auditor_v195_doble_para_la_196.txt`, para que no se elijan despues de mirar. (a) `vecinos()` SE IMPORTA de `scripts/loop/vuelta182_tarea1c_relectura_al_doble.py` y NO se copia, con `evitar` cargado de TODO lo consumido y contado de sus ficheros; el solape con el tramo y con el universo tiene que salir CERO POR CONSTRUCCION, no por suerte. (b) LEER LOS 60 A CIEGAS, tramo y doble, con `aislador_de_ciega.py`, y escribir las clases ANTES de abrir el destape. (c) LA VARA ES `docs/BANCO_DE_TEXTOS.md` `9.6.1`, citada por numero y no parafraseada, Y CON EL ERROR DEL AUDITOR PUESTO: la vara de contenido-manda es EL SUELO, NO EL TECHO, y antes de aplicarla se pregunta si el par pertenece a una familia con REGLA PROPIA ya fijada, porque entonces manda la especifica (el `719` se perdio por no preguntarlo: hay regla fijada en el puesto `595` con el `580` de precedente vivo). (d) NO SALTARSE LA `B`: el auditor emitio CERO `B` en 30 pares y el archivo tenia una, el `654`. (e) PUBLICAR EL COTEJO con sus cifras (cuantos coinciden, cuantos discrepan, y cuales caen dentro y fuera del marcado), con los discutibles marcados ANTES de saber si se acierta | **CERRADA, 54 de 60, y con DOS discrepancias FUERA de mi marcado que publico yo** | `SALIDA_V195_T2_SUJETO.txt`, `SALIDA_V195_T2_CIEGA.txt`, `SALIDA_V195_T2_MIS_CLASES.txt`, `SALIDA_V195_T2_DESTAPE.txt`, `SALIDA_V195_T2E_COTEJO.txt` |
| **TAREA 3** | EL ROJO DE LA BATERIA, ATACADO EN SU CAUSA. Es el hallazgo `5.2` del acta 195 y la adjudicacion de la pregunta `P.2` del reporte de la 194. LO RESERVADO AL FUNDADOR ES PODAR LA NOMINA, NO HACERLA CRECER: la opcion `c` que rechazo el 5 sep 2026 era JUBILAR ARNESES VIEJOS, que es lo contrario de anadir, y el NO TOQUES LA NOMINA de los encargos anteriores se escribio para VUELTAS DE BATERIA y contra LA PODA. (a) LOS SEIS QUE EL CENSO VE Y LA NOMINA NO TIENE ENTRAN EN LA NOMINA, cada uno CON SU SUJETO CONGELADO y cotejado contra su blob de git, RECONTADOS del instrumento al empezar. (b) EL QUE NO PUEDA TENER SUJETO CONGELADO ENTRA COMO CASO DECLARADO, con su marca. (c) LAS TRES ENTRADAS SIN SUJETO CONGELADO que ya estan dentro (`vuelta186_tarea2c_mutacion_cierre_tardio.py`, `vuelta187_tarea4_mutacion_dos_convenciones.py`, `vuelta188_tarea4_mutacion_cobertura_parejas.py`, las tres ancladas a `REPORTE.md` VIVO) se resuelven POR LA MISMA REGLA: o se les congela el sujeto, o pasan a CASO DECLARADO con su marca. (d) `vuelta172_tarea5_mutacion_cierre.py` NO MUERDE desde la 189: se arregla para que caiga cuando tiene que caer, o se declara rota con su motivo medido. (e) NO SE PODA NADA: la nomina solo crece. (f) AL CERRAR, LA BATERIA SOLO SOBRE LO QUE SE TOCO, para comprobar que el rojo atacado se apago, PUBLICANDO LA CIFRA de arneses fuera de la nomina y de entradas sin sujeto congelado, y NO la bateria entera, que no es su vuelta. (g) CON SU CASO POSITIVO POR MUTACION, que pruebe lo que falla hoy: que la mirada de la nomina sobre si misma CAIGA cuando un arnes que el censo ve se queda fuera de la nomina sin ser caso declarado | **CERRADA. Las TRES causas del rojo quedan en 0, 0 y 0, y el que no mordia muerde** | `SALIDA_V195_T3F_BATERIA_DE_LO_TOCADO.txt`, `SALIDA_V195_T3G_MUTACION_NOMINA_ENCHUFADA.txt` |
| **TAREA 4** | `--componer` DEJA DE PUBLICAR VERDE SOBRE DIEZ ROJOS. Es el hallazgo `5.3` del acta 195 y la otra mitad de la pregunta `P.3` del reporte de la 194: `SALIDA_V194_BATERIA_COMPUESTA.txt` termina en VERDE, los 10 tramos cubren la nomina entera, con exitcode 0, mientras los diez tramos traen `CLASE DEL VEREDICTO: ROJO POR FALLO` y exitcode 1. Es cierto EN LO QUE MIDE, la cobertura, y enganoso EN LO QUE PARECE DECIR, el estado de la bateria; banco `9.1`, el instrumento debe caerse en vez de mentir. (a) `--componer` PROPAGA EL PEOR VEREDICTO DE LOS TRAMOS a su propio exitcode y a su linea final: cobertura entera y algun tramo en rojo NO es VERDE. (b) LAS DOS COSAS SE SIGUEN DICIENDO POR SEPARADO, la cobertura con su cifra y el veredicto con la suya, porque que propague el rojo no puede borrar que la cobertura estaba completa. (c) CON SU CASO POSITIVO POR MUTACION, con la salida de la 194 de sujeto congelado, que es el caso real: diez tramos rojos con cobertura 127 de 127 tienen que dar ROJO | **CERRADA. --componer propaga el peor veredicto y la cobertura se sigue diciendo aparte** | `SALIDA_V195_T4C_MUTACION_COMPONER_ROJO.txt` |
<!-- FIN TABLA DE TAREAS -->

## 2. LAS TAREAS, UNA POR UNA (cada seccion se ANEXA al cerrarse su tarea)

<!-- ANEXO DE TAREAS -->

### TAREA 2. LA RELECTURA AL DOBLE DEL TRAMO DEL AUDITOR. **CERRADA, CON 54 DE 60, Y CON DOS DISCREPANCIAS FUERA DE MI MARCADO QUE PUBLICO EN VEZ DE ESCONDER.**

**ESTA TAREA SE HIZO ANTES QUE LA 1, Y EL MOTIVO SE DECLARA EN VEZ DE
DEJARLO.** La seccion 2 del acta 195 se titula *"LA RELECTURA CIEGA: 27 DE 30, Y
LAS TRES QUE FALLE SON MIAS"* y publica las clases del auditor sobre **estos
mismos 30 puestos**. Registrar el acta antes de emitir mis clases me habria
quemado la ciega, y el registro no depende del orden. **Las dos tareas
bloqueantes estan cerradas; lo unico que cambia es cual va primero.**

#### 2.a EL SUJETO, RECOMPUTADO Y NO COPIADO

`vecinos()` **se importa** de `scripts/loop/vuelta182_tarea1c_relectura_al_doble.py`
en `scripts/loop/vuelta195_tarea2_relectura_al_doble.py`, con
`from ... import vecinos`. **No se copia y su regla no se toca: cambia lo que se
le pasa**, que es la `5.2` del acta 188.

**EL UNIVERSO CONSUMIDO, CONTADO DE SUS DOCE FICHEROS Y NO COPIADO DEL ENCARGO.**
Cifras de `docs/loop/SALIDA_V195_T2_SUJETO.txt`:

| lo que se cuenta | cifra | de donde sale |
|---|---:|---|
| ficheros del universo que EXISTEN | **12 de 12** | los doce nombrados en `UNIVERSO_CONSUMIDO` |
| universo consumido SIN el tramo de la 195 | **561** | contado de sus ficheros |
| universo consumido CON el tramo de la 195 | **591** | contado de sus ficheros |
| la cifra que el encargo publica | **591** | `PROMPT_SIGUIENTE.md` |
| calzan | **SI** | cotejo en el propio instrumento |

**EL SOLAPE SALE CERO POR CONSTRUCCION Y NO POR SUERTE**, porque `evitar` va
DENTRO de la llamada y no comprobado despues: **solape de los vecinos con el
tramo 0** y **con el universo consumido 0**. Los 30 vecinos recomputados son **el
MISMO CONJUNTO** que la sellada del auditor
`docs/loop/_auditor_v195_doble_para_la_196.txt`, cotejado leyendo solo su linea
`EL DOBLE` para que el cotejo no calce por arrastrar tambien el tramo.

**Y EL 654 Y EL 719, QUE DISPARAN `AUDITOR.md` 1.2, ESTAN LOS DOS DENTRO** del
tramo que se dice releer. El instrumento **PARA** si alguno estuviera fuera.

#### 2.b LOS SESENTA, LEIDOS A CIEGAS, Y LAS CLASES SELLADAS ANTES DEL DESTAPE

`aislador_de_ciega.py` con criterio escrito: **60 pares elegidos, CERO fugas del
destape en la salida ciega**. Ciega `docs/loop/SALIDA_V195_T2_CIEGA.txt` (81838
bytes) y destape `docs/loop/SALIDA_V195_T2_DESTAPE.txt` (64898 bytes), **los dos
existen y ninguno mide cero bytes**.

**EL ORDEN NO SE AFIRMA: SE LEE DE GIT**, y el bloque `A` del cotejo lo publica
con `git log --diff-filter=A`. Mis clases viven en
`docs/loop/SALIDA_V195_T2_MIS_CLASES.txt` y **se commitearon con el destape sin
abrir**.

#### 2.c LA VARA, CITADA POR NUMERO Y NO PARAFRASEADA

`docs/BANCO_DE_TEXTOS.md` **`9.6.1`**, LA VARA DE LA RAMA CONTENIDO-MANDA: LA
LINEA O EL PROCEDIMIENTO, con sus dos precisiones **`9.6.2`** (la vara TIENE
DIRECCION: que anade el HIJO a la MADRE, nunca al reves) y **`9.6.3`** (el TAMANO
del solape NO decide: se pesa el resto y en que lado), y **`9.22`** disponible
para la figura que da `C`.

**Y LA VARA COMO SUELO Y NO COMO TECHO, que es el error que el auditor midio en
su propia tanda y lo mas util que salio de ella.** Va escrito DENTRO del criterio
que la ciega lleva, no en mi cabeza. **Donde se aplico y se ve:** el `719`, que la
regla fijada en el puesto `595` resuelve sin llegar a la vara general (dos nodos
de fases distintas del recorrido son sanos). **Mi clase ahi es `D` y el archivo
dice `D`.**

#### 2.d LA `B` NO SE SALTA, Y ESTA VEZ SE EMITIERON CUATRO

| quien | `B` emitidas | sobre cuantos | la `B` del archivo la vio |
|---|---:|---:|---|
| el auditor, acta 195 | **0** | 30 | no |
| yo, esta tanda | **4** | 60 | **SI, el `654`** |

Contado por el bloque `G` del cotejo: **`B` que el archivo tiene en estos 60: 1
(el `654`)**; **`B` que el archivo tiene y yo NO vi: ninguna**; **`B` que yo emito
y el archivo no tiene: 3 (`1807`, `1808`, `3173`)**. **Paso de perder la clase a
sobre emitirla**, y las tres de mas caen DENTRO de mi marcado.

#### 2.e EL COTEJO, CON SUS CIFRAS, CONTADO DE `SALIDA_V195_T2E_COTEJO.txt`

| lo que se mide | sobre los 60 | sobre los 58 limpios |
|---|---:|---:|
| coinciden | **54** | **52** |
| discrepan | **6** | **6** |
| discrepancias DENTRO de mi marcado | **4** | **4** |
| discrepancias FUERA de mi marcado | **2** | **2** |

**MI REPARTO CONTRA EL DEL ARCHIVO, los dos contados:** mio `A 9 | B 4 | C 0 | D
47`; del archivo `A 8 | B 1 | C 0 | D 51`.

**LAS SEIS DISCREPANCIAS, UNA A UNA:**

| puesto | yo | archivo | mitad | marcado |
|---:|---|---|---|---|
| **976** | `D` | `A` | vecino | **DENTRO** |
| **1807** | `B` | `D` | TRAMO | **DENTRO** |
| **1808** | `B` | `D` | vecino | **DENTRO** |
| **2428** | `A` | `D` | vecino | **FUERA** |
| **2662** | `A` | `D` | vecino | **FUERA** |
| **3173** | `B` | `D` | vecino | **DENTRO** |

**DE MIS SIETE DISCUTIBLES ACERTE 3** (`655`, `1206`, `2427`) **Y FALLE 4**
(`976`, `1807`, `1808`, `3173`). **El marcado hizo su trabajo en cuatro de las
seis**, y no en las otras dos.

**LAS DOS QUE CAEN FUERA DE MI MARCADO SON `2428` Y `2662`, Y LAS DOS TIENEN EL
MISMO PERFIL:** ids que solo se diferencian en una palabra o un numero
(`desarrollar` contra `desarrollo`; `consejo_calidad_2` contra
`consejo_de_calidad_3`), yo lei `A` por eso, y **el archivo dice `D` en las dos**.
**Mi error es el simetrico del que el auditor midio en su tanda:** el suyo fue
aplicar la vara general donde habia regla propia; el mio es **dejar que la
semejanza de los ids pese**, cuando `9.6.3` dice expresamente que **lo que se pesa
es el resto y en que lado**, y en los dos casos el lado largo conserva
procedimiento propio. **Lo digo con esas palabras porque es la leccion que la 196
puede usar, no una disculpa.**

**POR `AUDITOR.md` 1.2 ESO BAJA EL CREDITO DE MI TANDA Y MI TRAMO SE RELEE AL
DOBLE.** Lo declaro yo, con su cifra, sin esperar a que lo encuentre el auditor.

#### 2.f LO QUE ESTA TAREA NO HACE, Y ES LA MITAD QUE IMPORTA

**NO SE MUEVE NINGUNA CLASE.** `docs/INTRA_DOMINIO_VEREDICTOS.jsonl` abre y
cierra en **`sha256` LF `0a77b5a35a962621`** sobre **4054129 bytes**, medido por
las dos convenciones en el bloque `A` del sujeto y en el `H` del cotejo. Las seis
discrepancias **se declaran y se traen**; quien las aplica, si procede, es el
RECOMPUTO.

#### 2.g DOS CORRECCIONES DECLARADAS DENTRO DE ESTA TAREA, Y NINGUNA SE TAPA

**LA PRIMERA, EN MI FICHERO DE CLASES.** La columna que dice a que mitad
pertenece cada puesto salio mal en **tres filas** (`11`, `974`, `975`) y sumaba
**31 y 29** donde solo puede sumar **30 y 30**. **Ninguna clase se toco**: lo que
estaba mal era el rotulo de reparto. La correccion va **anexada al final del
fichero con lo que decia y lo que dice**, sin borrar el texto viejo
(`EJECUTOR.md` 8). Hoy el cotejo mide **0 filas con la columna mal rotulada**.

**LA SEGUNDA, EN EL PROPIO INSTRUMENTO DEL COTEJO, Y LA CAZO SU PROPIA GUARDA.**
`mis_discutibles()` partia el fichero ENTERO por sus filas, asi que **el bloque de
la ultima fila llegaba hasta el fin del fichero** y se tragaba la seccion titulada
`MIS DISCUTIBLES`. Resultado medido: el puesto `3331` salia marcado sin estarlo y
la cuenta daba **OCHO** donde la lista del final dice **SIETE**. **La guarda que
publica las dos cifras y dice si calzan es la que lo enseno**, y por eso la caida
se vio en vez de pasar. Corregido acotando la tabla por su cabecera de cierre; hoy
las dos listas salen **SIETE y SIETE, y LAS DOS SON LA MISMA**. **El codigo viejo
se nombra entero en el docstring de la funcion en vez de borrarse.**

### TAREA 1. LOS REGISTROS. **CERRADA. `R.57` ESCRITA, IDEMPOTENCIA PROBADA EN BYTES, Y EL LECTOR TUVO QUE CAMBIAR TRES VECES PORQUE EL ACTA CAMBIO DE FORMA.**

**EL NUMERO DE LA ENTRADA NO SE TECLEA.** `scripts/loop/serie_de_registros.py`,
corrido en el bloque `G` de la apertura y otra vez dentro del registrador, da
**`SIGUIENTE LIBRE: R.57`** sobre **48 entradas** y **0 colisiones**. El encargo
adelanta `R.57` y **el instrumento dice `R.57`: CALZA**. Tras escribir, la serie
recomputada da **49 entradas, siguiente libre `R.58`, 0 colisiones y 0 huecos**.

#### 1.a LO QUE SE CONTO DEL CUERPO ACOTADO DEL ACTA, Y NINGUNA DEL ENCARGO

Acta 195 acotada en `docs/loop/ACTA_AUDITOR.md`, **lineas 68709 a 69017**, o sea
**309 lineas**. Secciones leidas y no tecleadas: **0, 1, 2, 3, 4, 5, 6, 7 y 8**.
Todo lo de abajo sale de `docs/loop/SALIDA_V195_T1A_REGISTRO_R57.txt`.

| lo que se cuenta | cifra | como se leyo |
|---|---:|---|
| adjudicaciones `4.1` a `4.10` | **10** | patron entrecomillado (el del acta 184) |
| las mismas, con el patron suelto (el del acta 189) | **0** | se publica aunque sea cero |
| de ellas, discutibles del ejecutor | **7** | familia leida del titulo |
| de ellas, preguntas contestadas | **3** | `P.1`, `P.2`, `P.3` |
| discutibles **A FAVOR** | **7** | estado leido del titulo |
| discutibles **EN CONTRA** | **0** | **y es la QUINTA acta seguida** |
| hallazgos de la seccion 5 | **3** | `claves_entrecomilladas` |
| caidas propias del auditor, del CUERPO de la seccion 3 | **1** | `C.1`, linea 68832 |
| caidas del ejecutor, de reporte | **0** | fila de la tabla |
| caidas del ejecutor, de cifra publicada | **0** | fila de la tabla |
| caidas del ejecutor, de metodo | **0** | fila de la tabla |
| actas sin entrada propia en la serie (173 a 194) | **8** | 173 a 180, remedido aqui |

**EL CERO DE `EN CONTRA` NO SE VUELVE A PROBAR POR MUTACION: SE DICE CON SU
FICHERO.** `docs/loop/SALIDA_V191_T1A_MUTACION_REGISTRADOR.txt` mide **6904
bytes** en disco y **6904** por LF, y su veredicto, leido del propio fichero, es
`'VEREDICTO: VERDE'`. La guarda vieja de la 190 corrida sobre esta acta
**PARARIA**, y esa es la medicion que dice que el cero es un resultado y no un
descuido.

**LA RACHA DE REPORTE VUELVE A CERO**, leida de la celda derecha de su propia fila
y no supuesta: **`racha de reporte: 0`**. El acta lo dice expresamente y el
registrador **PARA si esa celda no publica la racha**, para que un cero no se
pueda teclear. **No hay escalada que encargar.**

#### 1.b EL LECTOR TUVO QUE CAMBIAR TRES VECES, Y LAS TRES CON SU CIFRA DELANTE

**Esto no es cosmetica: sin los tres cambios el registrador PARA, y con ellos mal
hechos registra una cifra falsa.** Los tres son ANADIDOS y no ensanches, que es la
diferencia que el acta 184 adjudico a favor en su `5.3`: **ninguna marca vieja se
retira ni se recorta, el lector heredado corre PRIMERO y entero, y la cifra de lo
que el heredado daria se publica al lado.**

**1. LA FILA DE LAS CAIDAS PROPIAS DEL AUDITOR VIENE PARTIDA EN DOS, Y LA AGUJA
VIEJA CASA CON LAS DOS.** El acta escribe `caidas propias del auditor QUE
ACUMULAN` (**0**) y `caidas propias del auditor, TOTAL del cuerpo` (**1**). La
aguja corta que usaba el registrador de la 194 (`caidas propias del auditor`) casa
sobre esta acta con **2 filas**, y quien se quedara con `[0]` **registraria 0
donde el cuerpo declara 1**. `filas_de_las_propias()` lee las dos con su aguja
larga, publica las dos y **coteja contra la del TOTAL**, que es la que mide lo
mismo que el cuerpo: **1 contra 1, CALZA**.

**Y esto merece decirse entero, porque es lo contrario de una rareza: la fila
partida ES EL REMEDIO DEL HALLAZGO `5.1` DEL PROPIO ACTA APLICADO A SU MISMA TABLA
EN LA VUELTA EN QUE LO LEVANTA.** El `5.1` denuncia que la fila del acta 194 decia
*"caidas propias del auditor: 1"* cuando su cuerpo declaraba dos, porque contaba
solo las que acumulan. **Un registrador que no cambiara habria repetido esa misma
confusion desde el otro lado.**

**2. LA FILA DE METODO ESCRIBE `**0 nuevas**` Y EL LECTOR HEREDADO NO LA LEE.**
`R92.numeral_de_la_fila` busca `**<digitos>**` pegados y devuelve `None` sobre esa
celda, o sea que el registrador **PARARIA por una fila que SI trae su cifra y solo
la acompana de un adjetivo**. `numeral_de_la_fila_195()` la lee y da **0**, sin
cambiar lo que el heredado ya leia y **sin dejar de dar `None` ante una celda de
verdad muda**.

**3. DOS ESTADOS DE ADJUDICACION QUE EL VOCABULARIO NO TENIA.** La `4.8` cierra
con *"CONTESTADA, y la respuesta corrige a mi predecesor, no al ejecutor"* y la
`4.10` con *"CONTESTADA, con las dos mitades"*. **Con el vocabulario heredado
entero saldrian `SIN DECIR` 2 adjudicaciones y el registrador PARARIA**, cifra
publicada en la propia salida. Las dos marcas nuevas son **literales del acta**,
no parafrasis.

**Y EN SENTIDO CONTRARIO, UN LECTOR QUE ESTA VUELTA NO HACE FALTA Y NO SE
RETIRA:** `hallazgos_en_titular()`, que la 194 tuvo que anadir porque su acta
titulaba con `###`, **da CERO sobre el acta 195**, que vuelve a la negrita de
apertura de parrafo. Los tres lectores se corren y las tres cifras se publican:
`claves_entrecomilladas` **3**, `claves_de_adjudicacion` **0**,
`hallazgos_en_titular` **0**. **Retirarlo estrecharia el vocabulario a la forma del
acta de hoy, y la proxima que titule con `###` haria PARAR el instrumento.**

#### 1.c LA EXIGENCIA QUE SE HACE CONDICIONAL, Y LA RAMA QUE SIGUE ENTERA

La fila de puestos del acta 195 dice **`30 aislados, 30 cotejados, CERO
quemados`** y **no publica un segundo cotejo**. El registrador de la 194 exigia
SIEMPRE `cotejo limpio va sobre N` y **sobre esta acta PARARIA**. Con **CERO**
quemados **no hay dos cotejos que publicar**, asi que el acta escribe uno solo, y
eso es correcto.

**LA EXIGENCIA SE HACE CONDICIONAL A QUE HAYA QUEMADOS, Y EN ESA RAMA SIGUE
ENTERA:** si los hubiera y faltara el segundo cotejo, el registrador para igual.
**Lo que se estrecha es el caso, no la guarda**, y `quemados_son_cero(None)`
devuelve `False` a proposito: **si no se pudo leer, no se supone que sean cero**.

**Y LA CIFRA DE CERO QUEMADOS TIENE CAUSA MEDIDA, QUE ES LO QUE EL ENCARGO MANDA
REGISTRAR:** la 194 midio **once**, y la diferencia es que **los mensajes de commit
del ejecutor ya no publican clases por puesto ni el reparto de una ciega**. **Eso
funciono, y se registra como lo que es: un remedio a mano que midio.** Su guarda de
codigo sigue pendiente y va nombrada en lo que queda fuera.

#### 1.d LAS TRES PREGUNTAS, CONTESTADAS, Y LO QUE CADA UNA ADJUDICA

| clave | pregunta | estado leido del titulo |
|---|---|---|
| `4.8` | `P.1` | CONTESTADA, y la respuesta corrige al predecesor del auditor |
| `4.9` | `P.2` | CONTESTADA A FAVOR POR EXTENSION CITABLE |
| `4.10` | `P.3` | CONTESTADA con las dos mitades: corrida SI, verde NO |

**LA `4.9` ES LA QUE ABRE LA TAREA 3 DE ESTA VUELTA** y la `4.10` la TAREA 4.
**Registrar no es adjudicar**, y esta seccion solo deja escrito lo que el acta
dice.

#### 1.e EL CASO POSITIVO POR MUTACION, Y LA IDEMPOTENCIA PROBADA EN BYTES

`--mutacion` corre sobre texto FABRICADO, con el valor esperado sacado de como se
fabrico el texto y no de una constante igual a la obtenida:
`docs/loop/SALIDA_V195_T1A_MUTACION_REGISTRADOR.txt`, **`CIFRA casos: 27 | pasan:
27 | fallan: 0`**, **`VEREDICTO: VERDE`**, contado de su propio fichero.

**Y CADA UNO DE LOS TRES CAMBIOS DE LECTOR LLEVA SU MUTACION, que es lo que los
separa de un adorno:** la aguja corta de la 194 tiene que casar con **DOS** filas
sobre la tabla fabricada y su primera tiene que ser el **0**; el heredado tiene que
devolver **`None`** sobre `**0 nuevas**` y **`SIN DECIR`** sobre los dos titulos
nuevos; y la guarda de la entrada tiene que **CAER** si la entrada se queda con una
sola mitad de la fila. **Si alguna de esas no cayera, el cambio no haria falta.**

**LA IDEMPOTENCIA NO SE AFIRMA: SE PRUEBA RE CORRIENDOLO, CON LA SEDE MEDIDA EN
BYTES.**

| momento | bytes de `docs/PENDIENTES.md` |
|---|---:|
| antes de escribir | **1039583** |
| despues de escribir `R.57` | **1050189** |
| **despues del RE CORRIDO** | **1050189** |

El re corrido escribio `docs/loop/SALIDA_V195_T1A_RECORRIDO_SIN_ESCRIBIR.txt` y
**no toco la sede**: el acta 195 aparece ya en **2 linea(s)** por sus dos marcas
literales, y **no se consumio el numero `R.58`**.

### TAREA 3. EL ROJO DE LA BATERIA, ATACADO EN SU CAUSA. **CERRADA, Y LAS TRES CAUSAS DEL ROJO QUEDAN EN CERO, CERO Y CERO.**

**LO QUE ESTABA ROTO, MEDIDO EN EL BLOQUE `F` DEL SELLO DE APERTURA Y ANTES DE LA
PRIMERA OPERACION:** 6 arneses del censo fuera de la nomina, 3 entradas sin sujeto
congelado, y 1 arnes que no muerde. **Las tres cosas ponian en ROJO los diez tramos
de cualquier bateria**, y un rojo permanente y conocido apaga la bateria sola: si
siempre esta roja, nadie mira el rojo nuevo.

#### 3.a LOS SEIS ENTRAN EN LA NOMINA, Y LO RESERVADO ERA PODARLA, NO HACERLA CRECER

**LAS DOS CITAS VAN LEIDAS DE SUS FICHEROS Y NO DE MEMORIA.** De
`scripts/loop/verificar_mutaciones_viejas.py`, desde la vuelta 148: *"LO QUE ESTA
REGLA EXIGE ES SUJETO CONGELADO. EL PLAZO DE UNA VUELTA ERA EL MEDIO, NO EL FIN."*
De `AUDITOR.md` 6.1: *"LA NOMINA SIGUE CRECIENDO: NADIE LA PODA SIN EL FUNDADOR."*
**La opcion `c` que el fundador RECHAZO el 5 sep 2026 era JUBILAR ARNESES VIEJOS**,
que es exactamente lo contrario de anadir.

**LOS SEIS SE RECONTARON DEL INSTRUMENTO AL EMPEZAR** y salieron los mismos seis
que el encargo nombra. Los seis tenian ya **SUJETO CONGELADO comprobado por
`anclaje_de()` antes de entrar**, salvo uno, que lo recibe en la `3.c`.

| lo que se mide | apertura | cierre |
|---|---:|---:|
| entradas de la nomina | **127** | **135** |
| arneses que el censo reconoce | **193** | **195** |
| arneses del censo FUERA de la nomina | **6** | **0** |
| entradas SIN SUJETO CONGELADO | **3** | **0** |
| entradas que el censo NO VE | **0** | **0** |

**LA NOMINA CRECE DE 127 A 135 Y NO SE QUITA NI UNA ENTRADA.** Son los seis del
encargo mas los **dos que nacen hoy** (`3.g` y `4.c`), que entran en su misma
vuelta por la regla aplicada a si misma.

#### 3.b Y 3.c LOS QUE NO TENIAN SUJETO CONGELADO: NINGUNO NECESITO SER CASO DECLARADO

La regla ofrece dos salidas, **o se les congela el sujeto, o pasan a CASO
DECLARADO con su marca**. **Los CUATRO se resolvieron por la primera**, y ninguno
entro como caso declarado: `CASOS_DECLARADOS` sigue en **2** entradas, las mismas
de antes.

**Y LA DECLARACION NO ES UN SELLO DE GOMA: los cuatro se miraron uno a uno ANTES
de escribir nada, y en los cuatro la huella de vivo NO es una apertura del fichero
vivo.** Lo que cada uno hace de verdad va escrito en su propia declaracion, dentro
de su docstring:

| arnes | que ve la guarda | que es de verdad |
|---|---|---|
| `vuelta193_tarea4e_mutacion_sello_entre_procesos.py` | `REPORTE.md` | el argumento de `AP.apuntar("REPORTE.md")`, una CADENA que va a la bitacora del turno para comprobar si sobrevive entre procesos. Todo lo que abre en escritura vive en un `mkdtemp` |
| `vuelta186_tarea2c_mutacion_cierre_tardio.py` | `REPORTE.md` | una linea que el propio arnes IMPRIME para decir que no lo toca. Su sujeto de datos son cadenas fabricadas; lo unico que lee del disco es el codigo bajo prueba, cuyo `sha256` publica |
| `vuelta187_tarea4_mutacion_dos_convenciones.py` | `REPORTE.md` | siempre detras de `git show bb3aaad3:...`, o sea el BLOB de un commit fijo |
| `vuelta188_tarea4_mutacion_cobertura_parejas.py` | `REPORTE.md` | el valor de `RUTA_DEL_187`, que solo se usa detras de `git show` con `COMMIT_DEL_187` delante |

**NO SE TOCA NI UNA LINEA DE MAQUINA DE LOS CUATRO.** La declaracion va en el
docstring, que es donde la guarda busca la huella de congelado y donde esta casa
escribe lo que un fichero declara de si mismo. **La cadena que la guarda confunde
con un fichero no se cambia**: cambiarla para contentar a la guarda seria falsear
la prueba.

#### 3.d EL QUE NO MORDIA: DIAGNOSTICADO, REPARADO, Y CON SU CAUSA ESCRITA

`vuelta172_tarea5_mutacion_cierre.py` llevaba **desde la vuelta 188** sin morder, y
las baterias de la 189 y la 194 lo publicaban como `NO MORDIO` **sin
diagnosticarlo**. Corrido en esta vuelta, la causa sale sola: **su propio caso
verde fabricaba DOS secciones `## 9.`**, la del bucle y la de `CR.CAB_9`.

Eso era inofensivo hasta que **la TAREA 4.b de la vuelta 188 ensancho la pieza (3)
de `cerrar_reporte.py` para cazar SECCIONES DUPLICADAS**. Desde entonces
`A_con_las_cuatro_no_falta_ninguna` daba **1** en vez de **0** y
`A_y_no_nombra_ningun_codigo` devolvia **`['(3)']`** en vez de `[]`.

**NO ES QUE LA GUARDA ESTUVIERA MAL: ES QUE EL SUJETO DE MENTIRA DEL ARNES DEJO DE
SER UN REPORTE VALIDO Y NADIE LO RE APUNTO.** El arreglo es una linea (`tope = 9`
en las dos ramas) y va comentado en su sitio con su causa. **NO SE AFLOJA NINGUN
CASO:** la rama `secciones=False` sigue fabricando un reporte SIN la seccion 9 y la
pieza (3) sigue teniendo que cazarla.

| corrida | resultado |
|---|---|
| antes, en esta vuelta | `ROJO: fallos=2, casos que no caen=1`, exitcode **1** |
| despues | **`VERDE: los 17 casos pasan tal cual y los 17 caen al mutar el esperado`**, exitcode **0** |

#### 3.e NO SE PODA NADA

**No se quito ni una entrada.** La nomina solo crece: 127 a 135, y `CASOS_DECLARADOS`
sigue en 2.

#### 3.f LA BATERIA SOLO SOBRE LO TOCADO, Y EL ROJO SE APAGO

`scripts/loop/vuelta195_tarea3f_bateria_de_lo_tocado.py`. **NO ES LA BATERIA Y NO
SE CITA COMO TAL**: la cadencia de `AUDITOR.md` 6.1 pone la siguiente en la 199.

**LA LISTA DE LO TOCADO NO SE TECLEA A OJO: se computa de git** con
`git diff --name-only <apertura>..HEAD` filtrado por el censo, y se coteja contra
lo que la tarea declara haber tocado. **Se corre la UNION de las dos**, que es el
lado prudente. Salieron **12 arneses**, con las dos listas coincidiendo.

| lo que la corrida acotada encuentra | cifra |
|---|---:|
| arneses corridos, cada uno DOS veces | **12** |
| ANCLA PERDIDA | **0** |
| NO MORDIO | **0** |
| CASO DECLARADO | **0** |
| SIN REPRODUCIR | **0** |
| **CLASE DEL VEREDICTO** | **VERDE, exitcode 0** |

**Y LAS TRES CIFRAS QUE EL ENCARGO MANDA PUBLICAR SALGAN COMO SALGAN, medidas
sobre el repo de hoy y no sobre esta corrida acotada: arneses del censo FUERA de la
nomina 0, entradas SIN SUJETO CONGELADO 0, entradas que el censo NO VE 0.** **Las
tres son cero, y por eso no hay lista que publicar.**

**`dataset/` en 0 filas de `numstat` al entrar y 0 al salir**, y **la sede del
turno del auditor no se movio** (345 bytes, `sha256` LF `2e085e88795b9df2` por los
dos lados), que se remide en vez de creerse porque es la que
`vuelta192_tarea4_mutacion_cuarta_puerta.py` borraba antes de que la 194 lo
arreglara.

**Y ESTA CORRIDA CAZO UNA CAIDA MIA ANTES DE QUE SALIERA DE LA VUELTA.** En su
primera pasada, `vuelta195_tarea3g_mutacion_nomina_enchufada.py` salio **NO
REPRODUCIBLE**: escribia el nombre del temporal de `mkdtemp` en su salida sellada,
y ese nombre cambia en cada corrida. **Una salida sellada que cambia sola no se
puede cotejar con nada.** Corregido quitando el nombre y dejando escrito por que;
la segunda pasada da **0 sin reproducir**. **El cotejo de reproducibilidad de la
vuelta 141 hizo exactamente su trabajo sobre un arnes recien nacido.**

#### 3.g EL CASO POSITIVO POR MUTACION, Y PRUEBA EL CABLE Y NO SOLO LA MIRADA

`scripts/loop/vuelta195_tarea3g_mutacion_nomina_enchufada.py`, salida en
`docs/loop/SALIDA_V195_T3G_MUTACION_NOMINA_ENCHUFADA.txt`: **`CIFRA casos: 15 |
pasan: 15 | fallan: 0`**, **`CIFRA casos que caen al mutar el esperado: 15 de 15`**,
**`VEREDICTO: VERDE`**, contado de su propio fichero.

**POR QUE NO BASTABA CON LO QUE YA HABIA, Y ES LA MITAD QUE IMPORTA.**
`prueba_de_la_nomina()` ya comprobaba que `arneses_que_faltan()` VE a los que estan
fuera. **Lo que no estaba probado por nada es que ese ver MUEVA EL VEREDICTO**, y
la unica forma de saberlo era correr la bateria entera y mirar el color, que es lo
que la adjudicacion `4.4` del acta 190 llama inaceptable. Aqui el cable se prueba
**apagandolo y encendiendolo**: con la lista de faltantes hay `ROJO POR FALLO` y
codigo distinto de cero; con la lista vacia vuelve `VERDE` y codigo cero.

**Y LA TERCERA COSA, QUE ES LA QUE EL ENCARGO SUBRAYA: SER `CASO DECLARADO` NO ES
UNA PUERTA TRASERA PARA SALIRSE DE LA NOMINA.** `arneses_que_faltan()` no consulta
`CASOS_DECLARADOS`, y aqui se prueba en vez de leerse: un arnes declarado que no
este en la nomina **sigue saliendo como que falta**. **Una exencion de exitcode no
es una exencion de estar en la nomina.**

Ademas se prueba que **un hueco de censo es FALLO y no DEUDA** (la precedencia de
`clase_del_rojo()`), y que **la vara del censo sigue protegiendo a los anteriores**,
que no se afloja.

**Todo sobre un directorio de `mkdtemp` y nominas fabricadas en memoria**, sin
tocar `scripts/loop/` ni ningun dato de la campana, y con el temporal retirado al
salir (`P.16`).

### TAREA 4. `--componer` DEJA DE PUBLICAR VERDE SOBRE DIEZ ROJOS. **CERRADA, Y LA LINEA QUE LA 194 PUBLICO YA NO SE PUEDE ESCRIBIR SOBRE ESOS MISMOS DIEZ TRAMOS.**

**EL CASO, MEDIDO Y NO CONTADO.** `docs/loop/SALIDA_V194_BATERIA_COMPUESTA.txt`
termina en *"VERDE: los 10 tramos cubren la nomina entera"* con `exitcode 0`,
mientras los diez tramos que compone traen `CLASE DEL VEREDICTO: ROJO POR FALLO` y
`exitcode 1`. **Las dos cosas eran verdaderas midiendo cosas distintas**: la
cobertura estaba completa (127 de 127) y la bateria estaba roja. Lo que estaba mal
era que la salida **se leyera como si la bateria estuviera bien**. Banco `9.1`: el
instrumento debe caerse en vez de mentir.

#### 4.a EL PEOR VEREDICTO SE PROPAGA AL EXITCODE Y A LA LINEA FINAL

Dos funciones nuevas en `scripts/loop/vuelta194_bateria_por_tramos.py`, que es el
lanzador del que la 199 clonara el suyo:

- **`clase_de_la_salida(ruta)`** lee la `CLASE DEL VEREDICTO` que cada tramo
  publica. **Se lee de la salida y no se recalcula**, igual que la cobertura:
  recalcularla seria preguntarle al reparto por el reparto. **Un tramo que no
  publica su clase devuelve `None`, y `None` NO se confunde con VERDE.**
- **`peor_veredicto(clases)`** devuelve la peor clase, su codigo y la lista de
  ilegibles. **Si hay algun ilegible, el peor es `ROJO POR FALLO`**: no se puede
  componer un verde sobre un tramo cuyo estado no se sabe.

**LOS NOMBRES Y LOS CODIGOS NO SE TECLEAN EN EL LANZADOR: se leen de
`verificar_mutaciones_viejas`**, que es su sede, para que no haya dos tablas que
manana digan cosas distintas.

#### 4.b LAS DOS COSAS SE SIGUEN DICIENDO POR SEPARADO

**Que propague el rojo no puede borrar que la cobertura estaba completa**, que es
informacion util y medida. La salida publica ahora **tres bloques distintos**: la
cobertura con su cifra, el veredicto de cada tramo con la suya, y el peor de los
dos. La linea final dice **las dos cosas juntas**: *"LA COBERTURA: los N tramos
cubren la nomina entera..."* y, debajo, el veredicto propagado con su motivo.

**CORRIDO SOBRE LAS DIEZ SELLADAS DE LA 194**, el composor lee los diez veredictos
y publica `EL PEOR VEREDICTO DE LOS TRAMOS: ROJO POR FALLO (codigo 1)`. **Esa
corrida NO llego a componer nada y NO piso ninguna sellada**, porque con la nomina
ya en 135 el reparto pide 11 tramos y solo hay 10: se paro antes de escribir, y
`SALIDA_V194_BATERIA_COMPUESTA.txt` quedo **byte a byte igual**, comprobado con
`cmp`.

#### 4.c EL CASO POSITIVO POR MUTACION, CON EL CASO REAL Y NO CON UNO COMODO

`scripts/loop/vuelta195_tarea4c_mutacion_componer_rojo.py`, salida en
`docs/loop/SALIDA_V195_T4C_MUTACION_COMPONER_ROJO.txt`: **`CIFRA casos: 15 |
pasan: 15 | fallan: 0`**, **`CIFRA casos que caen al mutar el esperado: 15 de 15`**,
**`VEREDICTO: VERDE`**, contado de su propio fichero.

**SUJETO CONGELADO, Y ES EL DE VERDAD:** las diez salidas de la 194 se leen **por
`git show` del commit `56c2d085`**, que es el que cierra su TAREA 3 y ya tiene las
diez en su arbol. **Un blob de git no se mueve**, y no se abre ningun fichero del
arbol de trabajo.

**LO QUE EXIGE, Y ES EXACTAMENTE LO QUE EL ENCARGO PIDE:** los diez tramos dan
`ROJO POR FALLO`, el peor de los diez es `ROJO POR FALLO`, su codigo NO es cero, y
**con estos diez el veredicto ya no puede ser VERDE**. La linea que la 194 publico
va dentro del arnes **como CITA y no como afirmacion suya**.

**Y LOS TRES CASOS QUE LA 194 NO DEJO VAN FABRICADOS EN MEMORIA**, porque una
guarda probada solo con el caso que ya ocurrio no sabe que hacer con el siguiente:
un tramo verde, un tramo en deuda, y **un tramo que no publica su clase**. Ese
tercero pone `ROJO POR FALLO` y sale nombrado en la lista de ilegibles.

**LA ESCALERA DE GRAVEDAD SE PRUEBA EN SUS TRES PELDANOS:** solo verdes da VERDE,
verde mas deuda da `ROJO POR DEUDA DECLARADA`, y deuda mas fallo da `ROJO POR
FALLO`. **Si el orden estuviera al reves, una bateria con un arnes caido se
publicaria como deuda declarada**, que es la degradacion que la `4.4` del acta 190
ya cazo una vez.

#### 4.d UNA CORRECCION DECLARADA DENTRO DE ESTA TAREA

La primera version del arnes apuntaba el sujeto congelado a **`6a508ca5`**, que es
el commit que anadio **el tramo 1** y en cuyo arbol solo existia **UNO de los
diez**. **Lo cazo su propio caso `los_DIEZ_blobs_se_leen`**, midiendo 1 donde tenia
que medir 10, que es para lo que ese caso esta. Corregido a `56c2d085` y **el
commit viejo se nombra en el codigo en vez de borrarse**, con lo que pasaba.

#### 4.e ESTO LLEVABA VUELTAS EN LA LISTA DE LO QUE SIGUE FUERA

Como *"el exitcode 2 propagado a `--componer`"*. **Hoy entra porque tiene su caso
medido delante**, y lo que se hizo es mas que propagar un 2: **se propaga el peor
de los tres veredictos, sea cual sea**, y la cobertura se sigue diciendo aparte.

<!-- FIN ANEXO DE TAREAS -->
