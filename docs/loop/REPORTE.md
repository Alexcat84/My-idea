# REPORTE DE LA VUELTA 179 (ejecutor). FASE III, EJECUCION. Rama `pasada-unica`.

> **ESTE REPORTE SE ABRIO AL EMPEZAR LA VUELTA Y CRECE POR ANEXION** (`EJECUTOR.md`
> 1, "EL REPORTE ABRE CON LA VUELTA"). El esqueleto lo tallo
> `scripts/loop/vuelta179_esqueleto_reporte.py`; cada tarea ANEXA SU FILA AL
> CERRARSE, no al final; y el cierre lo talla entero `scripts/loop/cerrar_reporte.py`.
> **Si esta vuelta se corta, lo que quede aqui es lo que de verdad se hizo, y las
> filas que sigan diciendo ABIERTA, SIN CERRAR son las que no se hicieron.**
>
> **ESTA VUELTA NO ES DE BATERIA, Y LA CADENCIA NO SE ELIGE AQUI: ESTA
> ADJUDICADA Y RECONFIRMADA DOS VECES.** El acta 176, punto 7.8, reanclo el
> contador a la vuelta que de verdad corrio la bateria y no a la que la tenia
> encargada; **el acta 178, punto 11, lo reconfirmo**; y el encargo de esta vuelta
> lo repite con todas las letras: **la proxima vuelta de bateria es la 181**, y la
> 179 y la 180 cierran su seccion 9 con el **HUECO DECLARADO Y MEDIDO**, con su
> nombre, sus bytes medidos y su atribucion, las tres juntas. Un hueco declarado
> no es un hueco escondido.
>
> **EL TOPE SIGUE EN CINCO, Y NO LO DECIDE NADIE: LO DISPARO LA 177 Y LA 178 LO
> CONFIRMO ENTREGANDO CINCO.** `AUDITOR.md` 6.2 dice que el regimen temporal de
> dos sub-tareas dura **hasta que DOS vueltas seguidas cierren su propio reporte**
> con `cerrar_reporte.py`, y eso se cumplio. **El regimen temporal queda CUMPLIDO
> Y CITABLE, no borrado**, y los cuatro commits que lo sostienen se localizan EN
> GIT en el bloque B.1 de `scripts/loop/vuelta179_apertura.py`, no se teclean.
>
> **Y ESTA VUELTA MIDE SU DESFASE DE CALIBRADO EN LA APERTURA, DENTRO DEL BLOQUE
> DE APERTURA Y ANTES DE LA PRIMERA OPERACION.** El remedio se cableo en
> `vuelta177_apertura.py`, la 178 lo estreno y aqui se repite: el medidor corre
> dentro del bloque de apertura. **Desde la 178, una columna de apertura medida al
> cierre es caida que ACUMULA**, y eso lo dice el encargo, no este reporte.
>
> **Y EL PASO 0 DE ESTE ESQUELETO PREGUNTA POR EL REPORTE QUE VA A PISAR, NO POR
> LA VUELTA ANTERIOR.** Esta vez las dos preguntas vuelven a coincidir, porque la
> 178 escribio su reporte, lo cerro y lo archivo EN SU MISMA VUELTA; el
> fichero corre LAS DOS igualmente y publica lo que salga de cada una, porque una
> guarda que solo se mira cuando difiere no se puede auditar el dia que difiera.

**EL VEREDICTO DE UNA LINEA: SIN ESCRIBIR TODAVIA.** Se talla al cierre, cuando
haya de que hablar.

## 0. LA IDENTIDAD Y LA CABECERA, TALLADAS Y NO TECLEADAS

**LA IDENTIDAD, LEIDA DE GIT EN ESTA VUELTA** por
`scripts/loop/vuelta179_esqueleto_reporte.py`, con
`git rev-parse --abbrev-ref HEAD`, `git log` y `git log --diff-filter=A`, y CAE
EN ROJO si algo no se encuentra o es ambiguo:

- rama: `pasada-unica`
- commit del acta de la vuelta 178: `74cad47d`, asunto real leido de git log:
  'ACTA DEL AUDITOR, VUELTA 178: 29 DE 33 A CIEGAS Y LAS CUATRO QUE FALLARON LAS FALLE YO, PERO LA RACHA DE REPORTE LLEGA A DOS Y LA ESCALADA SE ENCARGA EN ESTE MISMO ACTA.'
- HEAD real de apertura, sellado ANTES de la primera operacion en
  `docs/loop/SALIDA_V179_HEAD_APERTURA.txt`: `74cad47d`
- commit de nacimiento del bloque de apertura, leido con
  `git log --diff-filter=A`: `02af60ee`
- reporte que este esqueleto pisa, leido de la cabecera de ese mismo fichero:
  la vuelta **178**, ya archivada byte a byte antes de escribir aqui
- commit de cierre: se talla al cierre. **Un reporte no puede nombrar el commit
  que lo lleva**, porque ese commit se crea despues de escribirlo.

<!-- CABECERA TALLADA -->
**PENDIENTE DE TALLAR AL CIERRE, Y SE DICE EN VEZ DE RELLENARLA.** La tabla sale
de `scripts/loop/tallar_cabecera_reporte.py --fase04 --vuelta 179`. **Esta
vuelta corrio el bloque de apertura entero ANTES de su primera operacion**, asi
que la mitad izquierda ya se puede leer: corrido aqui, el tallador dice **"ROJO,
19 celdas no se pudieron leer"** y de esas lineas de rojo, **0
mencionan APERTURA**. Este hueco se rellena con la tabla tallada entera cuando la
vuelta cierre.
<!-- FIN CABECERA TALLADA -->

## 1. LAS CINCO TAREAS DEL ENCARGO, Y SU ESTADO

<!-- TABLA DE TAREAS -->
| tarea | que encarga | estado | donde vive la prueba |
|---|---|---|---|
| **TAREA 1** | LOS REGISTROS, LAS CORRECCIONES Y LA OPERACION DE CODIGO DE LA ESCALADA, Y ES BLOQUEANTE. Cuatro letras: (a) LA CORRECCION DECLARADA DE LA CAIDA DE LA 178, que publico en su 1.e `16 casos` donde su propio fichero `docs/loop/SALIDA_V178_T1E_MUTACION.txt` dice 18, con las TRES cifras al lado (la publicada, la del fichero y la de la re-corrida de hoy) y SIN retocar el reporte archivado, que dice lo que se publico; (b) LA OPERACION DE CODIGO DE LA ESCALADA, que es la pieza que manda: la guarda de LA PROSA QUE CITA UN FICHERO, dentro de `cerrar_reporte.py` y como funcion PURA junto a sus hermanas, que caza toda frase que publique una cifra de casos de un arnes Y nombre un `SALIDA_V*.txt` en la misma linea, lee la cifra propia de ese fichero y CAE EN ROJO nombrando la linea, la cifra publicada y la del fichero, con los bloques cercados fuera y con el fichero inexistente o de cero bytes tambien en ROJO; con su caso positivo por mutacion y CORRIDA SOBRE `REPORTE_V178.md` publicando lo que salga; (c) LOS DOS ARNESES DESTAPADOS ENTRAN EN LA NOMINA de `verificar_mutaciones_viejas.py`, mas todo arnes que esta vuelta escriba, con la cuenta entera y la resta comprobada, ANTES de la 181 para que el rojo que la 178 anuncio no llegue a existir; (d) EL CORTE DEL DENOMINADOR CABLEADO DONDE SE GENERA LA CIFRA y no en una frase, porque la 178 publico 15 de 92 siendo verdad y al cerrar eran 15 de 98 | **CERRADA** | `SALIDA_V179_T1A_RECORRIDA_178.txt`, `_T1B_SOBRE_178.txt`, `_T1B_MUTACION.txt`, `_T1C_CUENTA.txt`, `_T1D_MUTACION.txt` |
| **TAREA 2** | `OP-L-03`: SE LEEN LOS DIEZ PARES REALES DE LOS ACTOS SIN LEER. El backlog ya esta re-medido y `backlog_l03_resuelto.py` sale VERDE con los dos caminos calzando en los 40 actos: de los 73 pares que el instrumento da quedan 18 reales, 8 los leyo la 177 y quedan 10 en los 34 actos que nadie ha mirado. Los diez se leen con la vara del banco, par por par, y cada uno con su veredicto y su razon en `docs/INTRA_DOMINIO_VEREDICTOS.jsonl` SOLO SI EL PAR TIENE PUESTO EN LA COLA; si no lo tiene NO SE INVENTA UN PUESTO y su clase y su razon van al registro de `OP-L-03` en el campo `clases_de_los_pares_por_leer`, que es donde la 177 las puso y donde son trazables. El marcador no se toca si no hay puesto, y si lo hay se recomputa del archivo con sus cuatro clases. Cada acto cierra con su forma escrita: la figura, su cobertura y lo que queda. Y la cifra va al lado, siempre las dos: pares del instrumento y pares reales | **CERRADA** | `SALIDA_V179_T2_LOS_DIEZ.txt`, `_T2_VECINOS.txt`, `_T2_ESCRIBIR.txt`, `_T2_COBERTURA.txt` |
| **TAREA 3** | LOS DIECISEIS TRIANGULOS SE PUBLICAN PARTIDOS POR SU FUENTE, y NINGUNA CLASE SE MUEVE. `vuelta178_tarea3_anotar_triangulos.py` publica la cifra PARTIDA y no solo el 16: cuantos descansan enteros en `docs/INTRA_DOMINIO_VEREDICTOS.jsonl` y cuantos se apoyan en un lado de fuera, y NOMBRA aquellos en que el lado de fuera es el `D`, que es el lado que hace que el triangulo sea un triangulo. `docs/plan/OP_L_03_TRIANGULOS.jsonl` gana un campo por fila que diga si el triangulo es recomputable entero del archivo, y el campo `fuente_de_la_clase` por lado NO se toca. CERO VEREDICTOS MOVIDOS, comprobado por `sha256` antes y despues. Con su caso positivo por mutacion sobre un registro fabricado, donde un triangulo con sus tres lados en el archivo y otro con el `D` fuera caen en casillas distintas | **ABIERTA, SIN CERRAR** | (la fila se anexa al cerrarse la tarea) |
| **TAREA 4** | LAS QUINCE DEL SUJETO CONGELADO SE JUZGAN, UNA A UNA, Y NO SE CABLEA NADA TODAVIA. Primero se juzgan, despues se cablea, y no al reves. Por cada una de las quince, un veredicto escrito con su prueba: o el arnes de verdad ABRE un fichero vivo de la campana y hay que congelarle el sujeto, o LO NOMBRA SIN ABRIRLO y basta con que lo declare, o es un CASO DECLARADO legitimo y se anota por que. Registro propio y no prosa: `docs/plan/SUJETO_CONGELADO_VEREDICTOS.jsonl`, una fila por arnes, con el nombre, el veredicto, el fichero que abre y la evidencia (la linea del codigo). NO se arregla ningun arnes en esta vuelta y NO se cablea la guarda al rojo global de la bateria: el cableado se decide con los quince veredictos delante. NADA se borra de la nomina | **ABIERTA, SIN CERRAR** | (la fila se anexa al cerrarse la tarea) |
| **TAREA 5** | LO QUE NO ENTRA Y NO SE PIERDE, CONTADO EN VOZ ALTA. Ninguna de estas cinco se toca aqui, y las cinco se nombran CON SU MEDICION (existe, bytes en disco y normalizados a LF) para que no se caigan: la segunda sede de la clausula 4.4 en `REPORTE_V172.md:535`; el docstring de `paso0_archivar_anterior.py`, que sigue hablando de LA VUELTA ANTERIOR cuando la maquina pregunta por EL REPORTE QUE VA A PISAR; la guarda que falta en la dependencia del `D.4` de la 174, donde el esqueleto clona en vez de importar y nada avisa si el fichero del que se clono desaparece; el grano del tope de 10 minutos, que se mide EN LA 181 con el reloj de esa corrida y no se re-elige a ojo antes; y la convencion de bytes, que es del fundador, lleva seis actas subiendo y sube como PENDIENTE y no como problema, porque el remedio provisional de publicar siempre las dos ya es instrumento | **ABIERTA, SIN CERRAR** | (la fila se anexa al cerrarse la tarea) |
<!-- FIN TABLA DE TAREAS -->

## 2. LAS TAREAS, UNA POR UNA (cada seccion se ANEXA al cerrarse su tarea)

<!-- ANEXO DE TAREAS -->

### TAREA 1. LOS REGISTROS, LAS CORRECCIONES Y LA OPERACION DE CODIGO DE LA ESCALADA

#### 1.a. LA CORRECCION DECLARADA DE LA CAIDA DE LA 178, CON LAS TRES CIFRAS AL LADO

**EL TEXTO VIEJO NO SE BORRA Y EL REPORTE ARCHIVADO NO SE RETOCA**, que es lo que
el encargo manda y lo que `EJECUTOR.md` 8 exige: una correccion que tapa lo que
corrige no se puede auditar. `docs/loop/reportes/REPORTE_V178.md` sigue diciendo
en su **linea 349** lo que se publico.

| cifra | cuanto dice | de donde sale |
|---|---:|---|
| la PUBLICADA por la 178 | **16** | `docs/loop/reportes/REPORTE_V178.md:349`, localizada por el bloque H.6 de `scripts/loop/vuelta179_apertura.py` |
| la DEL FICHERO que esa frase cita | **18** | `docs/loop/SALIDA_V178_T1E_MUTACION.txt`, su linea que empieza por `CIFRA casos` |
| la DE MI RE-CORRIDA DE HOY | **18** | `docs/loop/SALIDA_V179_T1A_RECORRIDA_178.txt`, corrido en esta vuelta |

**Y UNA CUARTA MEDICION QUE NO DEPENDE DE NINGUNA DE LAS TRES:** el bloque H.6 de
la apertura conto las lineas del propio fichero que terminan en `CAE` y salieron
**18**. Cuatro caminos, una sola cifra, y la publicada no es ninguna de ellas.

**LA CAIDA ES MIA Y ASI QUEDA ESCRITA:** la frase de la 1.e de la 178 se tecleo
en vez de contarse del fichero que ella misma citaba. Es exactamente la especie
que `EJECUTOR.md` 1 nombra desde la vuelta 76.

#### 1.b. LA OPERACION DE CODIGO DE LA ESCALADA, QUE ES LA PIEZA QUE MANDA

**LA GUARDA DE LA PROSA QUE CITA UN FICHERO**, dentro de
`scripts/loop/cerrar_reporte.py` y junto a sus hermanas, con la misma forma que
ellas: **cuatro funciones PURAS** que reciben el texto y un lector.
`parrafos_fuera_de_cerca()`, `cifra_propia_del_arnes()`, `emparejar_citas()` y
`citas_de_arnes_que_no_calzan()`. El lector de disco, `lector_de_docs_loop()`, va
aparte a proposito: es la unica pieza que toca el disco, y por eso su arnes puede
tumbar a las otras cuatro sin tocar el repo.

**LO QUE HACE, Y LOS TRES MOTIVOS DE ROJO:** caza toda frase que publique una
cifra de casos y nombre un `SALIDA_V*.txt`, lee la cifra propia de ese fichero
(la linea que empieza por `CIFRA casos`, o su hermana `CIFRA casos que CAEN: X de
Y`, de donde el total es la segunda) y cae en rojo nombrando **la linea, la cifra
publicada y la del fichero** si no calzan, si el fichero no existe o si mide cero
bytes. Los dos ultimos por la letra del 5 sep, LA RUTA QUE PROMETE PRUEBA ES
CIFRA. **Los bloques cercados quedan fuera**, por el mismo motivo que la guarda de
la pareja: ahi va pegada la salida cruda y una cita que se retoca deja de ser una
cita.

**LA CORRIDA SOBRE `REPORTE_V178.md`, Y SE PUBLICA LO QUE SALIO**
(`docs/loop/SALIDA_V179_T1B_SOBRE_178.txt`). La tabla sale de contar ese fichero:

| que se cuenta | cuantos |
|---|---:|
| parejas cifra mas fichero que la guarda emparejo | **7** |
| de esas, las que CALZAN | **6** |
| de esas, las que NO calzan | **1** |
| cifras de casos que la guarda NO empareja con ningun fichero | **6** |

**LA GUARDA CAZA LA CAIDA DE LA 178 EN SU PRIMERA CORRIDA**, y lo digo con esas
palabras porque es lo que el encargo pide: **linea 349, fichero
`SALIDA_V178_T1E_MUTACION.txt`, cifra publicada 16, cifra del fichero 18**.

**Y LA PRIMERA VERSION DE ESTA GUARDA TENIA UN DEFECTO PROPIO, QUE SU PRIMERA
CORRIDA DESTAPO Y QUE ESCRIBO AQUI EN VEZ DE CALLARLO.** Cazaba **DOS**, no una:
acusaba tambien a la **linea 189**, donde la prosa dice *"pasa de 5 casos a 8,
los 8 pasan y los 8 caen"* y el fichero dice 8. La cifra que va con el fichero es
la **8**, y mi patron solo veia la palabra `casos`, que ahi solo acompana a la
**5**. Era un rojo inventado, que es justo lo que el docstring de la propia
guarda condena. **Se arreglo antes de seguir**, como el encargo manda: el patron
caza ahora tambien la forma `los N pasan`, y la ventana bajo de 400 a **120**
caracteres, elegida contando las siete parejas reales (32, 34, 36, 45, 51, 51 y
54) y no a ojo.

**EL CASO POSITIVO POR MUTACION**
(`scripts/loop/vuelta179_tarea1b_mutacion_citas.py`,
`docs/loop/SALIDA_V179_T1B_MUTACION.txt`). **21 casos, los 21 pasan y los 21
CAEN** al mutarles el valor esperado. **El caso que lo decide todo es el del
encargo y esta puesto:** un reporte fabricado que publica 16 junto a un fichero
fabricado que dice 18 sale **ROJO nombrando las dos cifras**; el mismo con 18 y
18 sale **VERDE**. Y estan tambien el fichero que no existe, el de cero bytes, el
parrafo con dos cifras y un solo fichero, la forma que no repite la palabra
`casos`, el bloque cercado y la ventana. **Nada sale del repo**: el lector es un
diccionario.

#### 1.c. LOS DOS ARNESES DESTAPADOS ENTRAN EN LA NOMINA, Y LOS TRES DE HOY CON ELLOS

**LA CUENTA ENTERA CON SU RESTA COMPROBADA**, contada de
`docs/loop/SALIDA_V179_T1C_CUENTA.txt` por
`scripts/loop/vuelta179_tarea1c_cuenta_nomina.py`:

| que se cuenta | cuantos |
|---|---:|
| arneses que ve el censo | **163** |
| entradas de la nomina | **103** |
| del censo, FUERA de la nomina | **60** |
| de la nomina, INVISIBLES al censo | **0** |

**LA RESTA:** censo 163 menos nomina 103 es 60, y los que estan fuera son 60.
**CALZA.**

**LOS CINCO QUE ENTRAN, Y CADA UNO COMPROBADO EN DISCO, EN NOMINA Y EN CENSO:**
`vuelta150_2d_simular_op_c_05.py` y `vuelta160_tarea3b_caso_positivo.py`, que son
los dos que la vara arreglada de la 178 destapo, mas los tres que esta vuelta
escribe, `vuelta179_tarea1b_mutacion_citas.py`,
`vuelta179_tarea3_mutacion_triangulos.py` y
`vuelta179_tarea1d_mutacion_corte.py`. **La nomina no se poda** (`AUDITOR.md`
6.1): pasa de 98 a 103.

**Y EL ROJO QUE LA 178 ANUNCIO PARA LA 181 NO LLEGA A EXISTIR:**
`arneses_que_faltan()`, corrido hoy, **no nombra a nadie**.

#### 1.d. EL CORTE DEL DENOMINADOR, CABLEADO DONDE SE GENERA LA CIFRA

**No en una frase**, que es la letra del encargo.
`verificar_mutaciones_viejas.sello_de_corte()` es **PURA** y recibe el
denominador y el head; `corte_de_git()` es la unica que toca git y va aparte.
Cableado en **SIETE sitios** que publicaban un denominador de la nomina, contados
del propio fichero con `grep -c "sello_de_corte("`, que da **10** apariciones
menos las **3** de su definicion y sus dos menciones en comentario: el rojo y el
verde de la guarda del sujeto congelado, el total de su tabla de reparto, la
nomina entera de la cabecera de `main()`, la nomina entera del tramo, y las dos
cuentas de invisibles al censo, la de apertura y la recomputada al cierre.

**EL MOTIVO ESTA MEDIDO Y SE VE HOY MISMO EN ESTA VUELTA:** la 178 publico **15
de 92** siendo verdad, y al cerrar eran **15 de 98**. En esta vuelta pasa otra
vez, y por eso el corte sirve: al abrir la guarda decia **15 de 98**, y despues de
que la 1.c metiera los cinco de hoy dice **16 de 103**, porque uno de los dos
destapados es `NO DECIDIBLE`. **Las dos cifras son verdaderas y ahora cada una
dice contra que denominador se midio.**

**EL CASO POSITIVO POR MUTACION**
(`scripts/loop/vuelta179_tarea1d_mutacion_corte.py`,
`docs/loop/SALIDA_V179_T1D_MUTACION.txt`). **10 casos, los 10 pasan y los 10
CAEN**. Su caso que manda es el de la 178: el 92 y el 98 no se confunden aunque
el corte sea el mismo, y dos cortes distintos no se confunden aunque el numero
sea el mismo. **No se llama a git en ningun caso.**

### TAREA 2. `OP-L-03`: LOS DIEZ PARES REALES DE LOS ACTOS SIN LEER, LEIDOS

#### 2.a. LA CIFRA AL LADO, SIEMPRE LAS DOS, Y NINGUNA COPIADA DEL ENCARGO

Contada de `docs/loop/SALIDA_V179_T2_LOS_DIEZ.txt`, que sale de correr
`backlog_l03_resuelto.py` por dentro y no de teclear lo que el encargo dice:

| tramo | actos | pares del instrumento | pares reales |
|---|---:|---:|---:|
| actos QUE LA 177 LEYO | 6 | 29 | **8** |
| actos QUE NADIE HA MIRADO | 34 | 44 | **10** |
| **todo el backlog** | 40 | 73 | **18** |

**Los diez de la fila del medio son el trabajo de esta tarea**, y quedan leidos
los diez. **La columna vieja no se borra:** el instrumento sigue dando 73, y al
lado van los 18 reales.

#### 2.b. DONDE VA CADA VEREDICTO, Y LA DISTINCION NO SE DIFUMINA

**Ninguno de los diez tiene puesto en la cola**, medido y no supuesto:

| donde va el veredicto | pares |
|---|---:|
| `docs/INTRA_DOMINIO_VEREDICTOS.jsonl` (TIENEN puesto) | **0** |
| `docs/plan/OP_L_03_LECTURAS.jsonl` (NO tienen puesto) | **10** |

**Y HAY QUE DECIR POR QUE SALE ASI, EN VEZ DE PRESENTARLO COMO UNA CASUALIDAD DE
ESTOS DIEZ.** Mi primera medicion de este campo estaba mal y la corrijo aqui:
preguntaba si alguno de los DOS EXTREMOS aparece en algun puesto, que es otra
cosa, y con esa vara los diez salian **SI**. La pregunta buena es si **EL PAR**
tiene puesto, y la respuesta es **NO para los diez y no puede ser otra**: un par
real esta definido por `medir_acto()` como el que **no esta ya en el archivo**,
asi que un par real nunca puede traer puesto. El archivo tiene hoy **3.388**
puestos ocupados, del **1** al **3.388**, **cero huecos**, y ninguno libre que
asignar. Eso explica ademas por que los **ocho** que la 177 leyo fueron todos al
registro y ninguno al archivo. **Se mide igualmente y se publica**, porque una
guarda que solo se mira cuando difiere no se puede auditar el dia que difiera.

**EL MARCADOR NO SE TOCA**, y se recomputa igual para poder decirlo
(`docs/loop/SALIDA_V179_T2_ESCRIBIR.txt`, bloque G): **A 551, B 72, C 5, D
2.760, total 3.388**. **Cero veredictos movidos**, comprobado por `sha256` antes
y despues, y los dos son `ea6e850d331d14f0`.

#### 2.c. COMO SE LEYERON, Y EL ARCHIVO SE MIRO ANTES DE JUZGAR

**Dos apoyos por par, y los dos van escritos en cada razon.** El primero es **la
vara del banco** (`9.6.1` y su rama contenido-manda, la linea o el
procedimiento) sobre los `pasos_accionables` de los dos extremos. El segundo es
**lo que el archivo ya dijo por un tercer nodo**, que `banco 9.3` obliga a mirar
porque **una direccion de fusion decidida sobre un par no sobrevive a su
familia**.

Lo mide `scripts/loop/vuelta179_tarea2_vecinos_del_archivo.py`
(`docs/loop/SALIDA_V179_T2_VECINOS.txt`), y **el resultado cambio mi lectura**:

| que salio | pares |
|---|---:|
| pares con al menos un tercero ya juzgado contra LOS DOS extremos | **10** |
| de esos, con una CADENA DE REPITE (los dos en `A` con el mismo tercero) | **7** |
| de esos, con una FRONTERA (uno en `A` y el otro en `D` con el mismo tercero) | **4** |
| pares sin ningun tercero comun | **0** |

**LO DIGO CLARO PORQUE ES UNA CORRECCION DE MI PROPIO TRABAJO EN CURSO:** habia
leido los diez por contenido y tenia **nueve `D` y una `A`**. Con el archivo
delante quedan **seis `A` y cuatro `D`**. **Las cinco que cambiaron las cambio el
archivo, no yo**, y en cada razon esta el puesto que lo hizo.

#### 2.d. LAS DIEZ LECTURAS, CON SU CLASE Y SU APOYO

| par | clase | quien lo sostiene en el archivo |
|---|---|---|
| `colaboracion_cadena_suministro` vs `diagnostico_efecto_latigo` | **A** | 730 (`A`) y 329 (`A`) por `efecto_bullwhip` |
| `compartir_datos_cadena_suministro` vs `diagnostico_efecto_latigo` | **D** | frontera 994 (`D`) contra 329 (`A`) |
| `compra_por_precio_mas_bajo_como_error` vs `relacion_largo_plazo_proveedor_unico` | **D** | dos fronteras en espejo, 2424/3102 y 2421/2927 |
| `creacion_option_pool` vs `employee_pool_esop` | **D** | frontera 1112 (`A`) contra 1193 (`D`). **DISCUTIBLE** |
| `disenar_tests_pass_fail` vs `diseno_experimentos_hipotesis` | **A** | 511 y 467, y el 511 declara la familia de TRES |
| `fase_diseno_prototipado_modelos` vs `prototyping_possibilities` | **A** | 641 (`A`) y 1056 (`A`) por `prototipado_modelos_negocio` |
| `proceso_ideacion_modelo_negocio` vs `prototyping_possibilities` | **D** | frontera 572 (`D`) contra 1056 (`A`) |
| `analisis_trafico_competitivo` vs `captura_conocimiento_mercado` | **A** | 508 y 941, y el 941 dice que el tercero es el mismo nodo |
| `crowdfunding_legal_exemptions_jobs_act` vs `cumplimiento_inversionistas_acreditados` | **A** | 462 (`A`) y 916 (`A`) por `equity_crowdfunding` |
| `evaluacion_tecnologias_disruptivas` vs `explotacion_tecnologias_disruptivas` | **A** | 505 (`A`) y 513 (`A`). **DISCUTIBLE** |

**El reparto: seis `A` y cuatro `D`, y seis mas cuatro son diez.**

#### 2.e. LOS OCHO ACTOS, CERRADOS CON SU FORMA Y SU COBERTURA

Cada uno lleva su `forma` escrita y su `cobertura` (`banco 9.26`) en
`docs/plan/OP_L_03_LECTURAS.jsonl`, que pasa de **6** filas a **14**, **ocho
anadidas por anexion y sin pisar ninguna de la 177**. **Los ocho quedan con cero
pares sin cubrir.** Lo que sale de leerlos enteros y no de a pares:

- **`colaboracion_cadena_suministro`**: una madre con **cero hermanos enlazados**
  y **dos hijos de paso**, y el contenido parte el acto en dos: el hijo de la
  medicion repite con la madre y el del compartir no.
- **`compra_por_precio_mas_bajo_como_error`**: **dos familias de dos** que se
  tocan en una linea y no se funden, cada una con su gemelo ya declarado y **los
  dos cruces en `D`**.
- **`creacion_option_pool`**: una familia de cuatro **partida en dos oficios con
  un nodo a caballo**. Es el unico de los ocho **en que el archivo se contradice
  consigo mismo** por dos terceros distintos, y eso queda escrito.
- **`disenar_tests_pass_fail`**: la familia de **tres** que el propio puesto 511
  declara, con una frontera comun enfrente que **no la parte**.
- **`fase_diseno_prototipado_modelos`**: un acto **partido en dos alturas**, y la
  misma pieza es **hija arriba y gemela abajo**. Dos de abajo se funden, el de
  arriba no.
- **`analisis_trafico_competitivo`**: un racimo de tres con un **gemelo
  ortografico** dentro, que es la figura mas barata de las ocho.
- **`crowdfunding_legal_exemptions_jobs_act`**: un racimo de tres sobre la misma
  regla de valores, **cerrado por el tercero**.
- **`evaluacion_tecnologias_disruptivas`**: el **par gemelo por nombre**, y con
  una cosa anotada que no cambia la clase: **no hay arista entre ellos** y el
  paso 4 de uno es la pregunta que el otro contesta. **No se toca**: la campana
  esta en modo de cierre.

#### 2.f. LO QUE QUEDA

**De los 18 pares reales, los 18 quedan leidos**, y no es una suma de cabeza: lo
cuenta `scripts/loop/vuelta179_tarea2_cobertura_final.py`
(`docs/loop/SALIDA_V179_T2_COBERTURA.txt`), que recorre los pares reales que el
instrumento da hoy y busca cada uno, **resuelto por `P.1`**, en el
`clases_de_los_pares_por_leer` de su acto. **Ocho** los escribio la 177 y **diez**
esta vuelta, **18 con lectura y 0 sin lectura**, y la resta cierra. **Cero pares
reales sin lectura en todo el backlog de `OP-L-03`.** El
estado de la ficha **NO se toca**, que es lo que `EJECUTOR.md` 4 manda mientras la
campana este en modo de cierre.

<!-- FIN ANEXO DE TAREAS -->
