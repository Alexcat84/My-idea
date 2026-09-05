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

**EL VEREDICTO DE UNA LINEA: LA ESCALADA DEJA DE SER UNA ORDEN PENDIENTE Y ES CODIGO QUE CAZO, EN SU PRIMERA CORRIDA, LA CAIDA QUE LA MOTIVO Y DESPUES ESTE MISMO REPORTE; LOS DIEZ PARES REALES DE OP-L-03 QUEDAN LEIDOS Y EL BACKLOG EN CERO SIN LECTURA; Y DE LAS 17 DEL SUJETO CONGELADO SOLO CUATRO ABREN DE VERDAD UN FICHERO VIVO.**
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
**LA TABLA, PEGADA ENTERA DEL FICHERO QUE LA LLEVA Y NO TECLEADA.** Salio
de `scripts/loop/tallar_cabecera_reporte.py --fase04 --vuelta 179`, y su salida
cruda vive en `docs/loop/SALIDA_V179_TALLADOR_CABECERA.txt` (2424 bytes en disco y 2404 normalizado a LF, 11 filas de
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
| identidad: rama y commit de apertura (leidos de git, no tecleados) | rama `pasada-unica`, commit del acta `74cad47d` (asunto real leido de git log: 'ACTA DEL AUDITOR, VUELTA 178: 29 DE 33 A CIEGAS Y LAS CUATRO QUE FALLARON LAS FALLE YO, PERO LA RACHA DE REPORTE LLEGA A DOS Y LA ESCALADA SE ENCARGA EN ESTE MISMO ACTA.'), HEAD real de apertura `74cad47d` (sellado antes de la 1.a operacion, leido de git log --diff-filter=A), arboles de `dataset/` IGUALES: VERDE | **rama `pasada-unica`, HEAD de cierre `2037f785` (leido de `SALIDA_V179_HEAD_CIERRE.txt`, sellado tras la ultima operacion)** |

<!-- FIN CABECERA TALLADA -->

## 1. LAS CINCO TAREAS DEL ENCARGO, Y SU ESTADO

<!-- TABLA DE TAREAS -->
| tarea | que encarga | estado | donde vive la prueba |
|---|---|---|---|
| **TAREA 1** | LOS REGISTROS, LAS CORRECCIONES Y LA OPERACION DE CODIGO DE LA ESCALADA, Y ES BLOQUEANTE. Cuatro letras: (a) LA CORRECCION DECLARADA DE LA CAIDA DE LA 178, que publico en su 1.e `16 casos` donde su propio fichero `docs/loop/SALIDA_V178_T1E_MUTACION.txt` dice 18, con las TRES cifras al lado (la publicada, la del fichero y la de la re-corrida de hoy) y SIN retocar el reporte archivado, que dice lo que se publico; (b) LA OPERACION DE CODIGO DE LA ESCALADA, que es la pieza que manda: la guarda de LA PROSA QUE CITA UN FICHERO, dentro de `cerrar_reporte.py` y como funcion PURA junto a sus hermanas, que caza toda frase que publique una cifra de casos de un arnes Y nombre un `SALIDA_V*.txt` en la misma linea, lee la cifra propia de ese fichero y CAE EN ROJO nombrando la linea, la cifra publicada y la del fichero, con los bloques cercados fuera y con el fichero inexistente o de cero bytes tambien en ROJO; con su caso positivo por mutacion y CORRIDA SOBRE `REPORTE_V178.md` publicando lo que salga; (c) LOS DOS ARNESES DESTAPADOS ENTRAN EN LA NOMINA de `verificar_mutaciones_viejas.py`, mas todo arnes que esta vuelta escriba, con la cuenta entera y la resta comprobada, ANTES de la 181 para que el rojo que la 178 anuncio no llegue a existir; (d) EL CORTE DEL DENOMINADOR CABLEADO DONDE SE GENERA LA CIFRA y no en una frase, porque la 178 publico 15 de 92 siendo verdad y al cerrar eran 15 de 98 | **CERRADA** | `SALIDA_V179_T1A_RECORRIDA_178.txt`, `_T1B_SOBRE_178.txt`, `_T1B_MUTACION.txt`, `_T1C_CUENTA.txt`, `_T1D_MUTACION.txt` |
| **TAREA 2** | `OP-L-03`: SE LEEN LOS DIEZ PARES REALES DE LOS ACTOS SIN LEER. El backlog ya esta re-medido y `backlog_l03_resuelto.py` sale VERDE con los dos caminos calzando en los 40 actos: de los 73 pares que el instrumento da quedan 18 reales, 8 los leyo la 177 y quedan 10 en los 34 actos que nadie ha mirado. Los diez se leen con la vara del banco, par por par, y cada uno con su veredicto y su razon en `docs/INTRA_DOMINIO_VEREDICTOS.jsonl` SOLO SI EL PAR TIENE PUESTO EN LA COLA; si no lo tiene NO SE INVENTA UN PUESTO y su clase y su razon van al registro de `OP-L-03` en el campo `clases_de_los_pares_por_leer`, que es donde la 177 las puso y donde son trazables. El marcador no se toca si no hay puesto, y si lo hay se recomputa del archivo con sus cuatro clases. Cada acto cierra con su forma escrita: la figura, su cobertura y lo que queda. Y la cifra va al lado, siempre las dos: pares del instrumento y pares reales | **CERRADA** | `SALIDA_V179_T2_LOS_DIEZ.txt`, `_T2_VECINOS.txt`, `_T2_ESCRIBIR.txt`, `_T2_COBERTURA.txt` |
| **TAREA 3** | LOS DIECISEIS TRIANGULOS SE PUBLICAN PARTIDOS POR SU FUENTE, y NINGUNA CLASE SE MUEVE. `vuelta178_tarea3_anotar_triangulos.py` publica la cifra PARTIDA y no solo el 16: cuantos descansan enteros en `docs/INTRA_DOMINIO_VEREDICTOS.jsonl` y cuantos se apoyan en un lado de fuera, y NOMBRA aquellos en que el lado de fuera es el `D`, que es el lado que hace que el triangulo sea un triangulo. `docs/plan/OP_L_03_TRIANGULOS.jsonl` gana un campo por fila que diga si el triangulo es recomputable entero del archivo, y el campo `fuente_de_la_clase` por lado NO se toca. CERO VEREDICTOS MOVIDOS, comprobado por `sha256` antes y despues. Con su caso positivo por mutacion sobre un registro fabricado, donde un triangulo con sus tres lados en el archivo y otro con el `D` fuera caen en casillas distintas | **CERRADA, con una PARADA declarada** | `SALIDA_V179_T3_TRIANGULOS_ANTES_DE_T2.txt`, `_T3_TRIANGULOS.txt`, `_T3_MUTACION.txt`, `_T3_ETIQUETA.txt` |
| **TAREA 4** | LAS QUINCE DEL SUJETO CONGELADO SE JUZGAN, UNA A UNA, Y NO SE CABLEA NADA TODAVIA. Primero se juzgan, despues se cablea, y no al reves. Por cada una de las quince, un veredicto escrito con su prueba: o el arnes de verdad ABRE un fichero vivo de la campana y hay que congelarle el sujeto, o LO NOMBRA SIN ABRIRLO y basta con que lo declare, o es un CASO DECLARADO legitimo y se anota por que. Registro propio y no prosa: `docs/plan/SUJETO_CONGELADO_VEREDICTOS.jsonl`, una fila por arnes, con el nombre, el veredicto, el fichero que abre y la evidencia (la linea del codigo). NO se arregla ningun arnes en esta vuelta y NO se cablea la guarda al rojo global de la bateria: el cableado se decide con los quince veredictos delante. NADA se borra de la nomina | **CERRADA** | `SALIDA_V179_T4_GUARDA.txt`, `_T4_VEREDICTOS.txt`, `docs/plan/SUJETO_CONGELADO_VEREDICTOS.jsonl` |
| **TAREA 5** | LO QUE NO ENTRA Y NO SE PIERDE, CONTADO EN VOZ ALTA. Ninguna de estas cinco se toca aqui, y las cinco se nombran CON SU MEDICION (existe, bytes en disco y normalizados a LF) para que no se caigan: la segunda sede de la clausula 4.4 en `REPORTE_V172.md:535`; el docstring de `paso0_archivar_anterior.py`, que sigue hablando de LA VUELTA ANTERIOR cuando la maquina pregunta por EL REPORTE QUE VA A PISAR; la guarda que falta en la dependencia del `D.4` de la 174, donde el esqueleto clona en vez de importar y nada avisa si el fichero del que se clono desaparece; el grano del tope de 10 minutos, que se mide EN LA 181 con el reloj de esa corrida y no se re-elige a ojo antes; y la convencion de bytes, que es del fundador, lleva seis actas subiendo y sube como PENDIENTE y no como problema, porque el remedio provisional de publicar siempre las dos ya es instrumento | **CERRADA** | `SALIDA_V179_T5_NO_ENTRA.txt` |
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
| la PUBLICADA por la 178 (**CORRECCION DECLARADA**: es la que se corrige, no la que se afirma) | **16** | `docs/loop/reportes/REPORTE_V178.md:349`, localizada por el bloque H.6 de `scripts/loop/vuelta179_apertura.py` |
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
`docs/loop/SALIDA_V179_T1B_MUTACION.txt`). **25 casos, los 25 pasan y los 25
CAEN** al mutarles el valor esperado. **El caso que lo decide todo es el del
encargo y esta puesto:** un reporte fabricado que publica 16 junto a un fichero
fabricado que dice 18 sale **ROJO nombrando las dos cifras**; el mismo con 18 y
18 sale **VERDE**. Y estan tambien el fichero que no existe, el de cero bytes, el
parrafo con dos cifras y un solo fichero, la forma que no repite la palabra
`casos`, el bloque cercado y la ventana. **Nada sale del repo**: el lector es un
diccionario.

**Y LA GUARDA CAZO ESTE MISMO REPORTE AL CERRARLO, QUE ES COMO NACIO SU UNICA
EXENCION.** La tabla de la 1.a de aqui arriba publica **16** al lado de
`SALIDA_V178_T1E_MUTACION.txt`, y la guarda la acuso, con razon en su forma: la
cifra no calza. Pero la casa **OBLIGA** a escribirla, porque `EJECUTOR.md` 8 dice
que una correccion se declara **sin borrar el texto viejo**, ya que una
correccion que tapa lo que corrige no se puede auditar. Sin exencion, la guarda
acusaba al reporte por hacer exactamente lo que la doctrina manda. **La exencion
es de una sola palabra y hay que pedirla por escrito:** el parrafo tiene que
decir el literal **CORRECCION DECLARADA**, y entonces la cita se publica igual,
con sus dos cifras, pero no cuenta como rojo. **Sin esas palabras vuelve a ser
rojo**, y ese caso esta en el arnes.

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

### TAREA 3. LOS TRIANGULOS SE PUBLICAN PARTIDOS POR SU FUENTE

#### 3.a. LA MEDICION DEL ENCARGO, REPRODUCIDA ANTES DE ESCRIBIR NADA

El encargo pide reproducirla primero, y sale identica. Contada de
`docs/loop/SALIDA_V179_T3_TRIANGULOS_ANTES_DE_T2.txt`, **al corte del commit de
apertura de esta vuelta y ANTES de que la TAREA 2 escribiera una sola linea**:

| que se cuenta | cuantos |
|---|---:|
| lados con clase leida de `docs/INTRA_DOMINIO_VEREDICTOS.jsonl` | **38** |
| lados con clase leida de `docs/plan/OP_L_03_LECTURAS.jsonl (vuelta 177)` | **10** |
| triangulos con los TRES lados con veredicto en el archivo | **8** |
| triangulos con al menos un lado SIN veredicto en el archivo | **8** |
| de esos, aquellos en que el lado de fuera es el `D` | **6** |
| **total de triangulos** | **16** |

**Las cinco cifras del encargo, las cinco.**

#### 3.b. Y LA DEL CIERRE, QUE ES OTRA, PORQUE LA TAREA 2 LA MOVIO

`EJECUTOR.md` 1 dice que **el estado al cierre se mide al cierre si algo de la
propia vuelta pudo haberlo movido**, y lo movio: la TAREA 2 escribio diez
lecturas nuevas en el mismo registro del que este instrumento saca la clase de
los lados de fuera. Contada de `docs/loop/SALIDA_V179_T3_TRIANGULOS.txt`, **al
cierre de la TAREA 2**:

| que se cuenta | cuantos |
|---|---:|
| lados con clase leida de `docs/INTRA_DOMINIO_VEREDICTOS.jsonl` | **42** |
| lados con clase leida del registro de `OP-L-03` | **15** |
| triangulos con los TRES lados con veredicto en el archivo | **8** |
| triangulos con al menos un lado SIN veredicto en el archivo | **11** |
| de esos, aquellos en que el lado de fuera es el `D` | **9** |
| de esos, aquellos en que el lado de fuera NO es el `D` | **2** |
| **total de triangulos** | **19** |

**LA RESTA CIERRA DOS VECES:** enteros **8** mas apoyados **11** son **19**, y de
los apoyados, **9** con el `D` fuera mas **2** sin el `D` fuera son **11**.

**LAS DOS TABLAS SON VERDADERAS Y NINGUNA SUSTITUYE A LA OTRA.** La de arriba es
la apertura, la de abajo el cierre, y cada una lleva su corte. **Los que no se
mueven son los ocho enteros:** los que descansan en el archivo siguen siendo
ocho, porque nada de esta vuelta anadio un veredicto al archivo.

#### 3.c. LOS NUEVE CON EL `D` FUERA, NOMBRADOS

Van uno a uno en `docs/loop/SALIDA_V179_T3_TRIANGULOS.txt`, con su acto, su terna
y el lado `D` que viene de fuera. **El `D` es el lado que hace que el triangulo
sea un triangulo**: dos `A` sin un `D` entre ellos no son esta figura, y por eso
se cuentan aparte de los otros **2**, cuyo lado de fuera es un `A`.

#### 3.d. EL CAMPO NUEVO Y LOS VEREDICTOS QUIETOS

`docs/plan/OP_L_03_TRIANGULOS.jsonl` gana **`recomputable_entero_del_archivo`** en
**las 19 filas, sin excepcion**, mas `el_lado_de_fuera_es_el_D` y
`vuelta_que_anota_la_fuente`. **El campo `fuente_de_la_clase` por lado no se
toca**, que es lo que el encargo manda.

**CERO VEREDICTOS MOVIDOS**, comprobado por `sha256` de
`docs/INTRA_DOMINIO_VEREDICTOS.jsonl` antes y despues dentro del propio
instrumento, y los dos salen **IDENTICOS**.

#### 3.e. EL CASO POSITIVO POR MUTACION

`scripts/loop/vuelta179_tarea3_mutacion_triangulos.py`
(`docs/loop/SALIDA_V179_T3_MUTACION.txt`). **20 casos, los 20 pasan y los 20
CAEN** al mutarles el valor esperado. **El caso que lo decide todo esta puesto:**
un triangulo con sus tres lados en el archivo y otro con el `D` fuera caen en
casillas distintas. **Y esta la mitad que se olvida:** los DOS apoyados, el del
`D` fuera y el de un `A` fuera, tambien caen en casillas distintas. **Nada sale
del repo**: los cuatro triangulos son fabricados.

**Y EL ARNES TUMBO DOS ESPERADOS MIOS EN SU PRIMERA CORRIDA**, y lo escribo en vez
de callarlo: yo esperaba 6 y 6 lados por fuente sobre el registro fabricado, y
son **7 y 5**. **El codigo estaba bien y mis dos numeros estaban mal.** La
mutacion los cazo porque el esperado equivocado coincidia con el valor mutado.

#### 3.f. PARADA: UNA ETIQUETA DE FUENTE QUE YA NO ES VERDAD

**LA DESTAPO ESTA MISMA VUELTA Y LA CAUSA ES MIA.** `clases_por_par()` etiqueta
con el literal `"docs/plan/OP_L_03_LECTURAS.jsonl (vuelta 177)"` **toda** clase
que venga de ese registro, porque cuando se escribio la 177 era la unica que
habia escrito ahi. **La TAREA 2 de esta misma vuelta escribio diez lecturas mas,
de la vuelta 179, y salen etiquetadas como si fueran de la 177.**

Contado por `scripts/loop/vuelta179_tarea3_etiqueta_de_fuente.py`
(`docs/loop/SALIDA_V179_T3_ETIQUETA.txt`):

| que se cuenta | cuantos |
|---|---:|
| lados etiquetados como del registro de la vuelta 177 | **15** |
| de esos, los que SI son de la vuelta 177 | **10** |
| de esos, los que NO lo son | **5** |
| de esos, los que no se pudieron cotejar | **0** |

**LA RESTA CIERRA:** 10 mas 5 mas 0 son 15. **Los cinco mal etiquetados van
nombrados uno a uno** en ese fichero.

**NO LO ARREGLO, Y DIGO POR QUE.** El encargo de esta vuelta dice con estas
palabras: *"El campo `fuente_de_la_clase` por lado NO se toca"*. Y lo que la
etiqueta rota contradice es `EJECUTOR.md` 8, **toda cifra de un autor con su
atribucion**. Cuando algo contradice una regla vigente, `EJECUTOR.md` 5 manda
**escribirlo como PARADA en el reporte y no arreglarlo por cuenta propia**. Asi
queda: **medido, nombrado y sin tocar**.

### TAREA 4. LAS DEL SUJETO CONGELADO, JUZGADAS UNA A UNA, Y NADA CABLEADO

#### 4.a. NO SON QUINCE AL CERRAR, Y LA CULPA ES MIA, Y ESTA MEDIDA

El encargo habla de **quince** (7 `SUJETO VIVO` y 8 `NO DECIDIBLE`), y **quince
eran al abrir**: el bloque H.10 de `scripts/loop/vuelta179_apertura.py` lo midio
antes de la primera operacion y dio **15 de 98**. **Al juzgarlas son 17 de 103**,
y el motivo es la TAREA 1.c de esta misma vuelta, que metio cinco arneses en la
nomina: dos de ellos salen senalados
(`vuelta150_2d_simular_op_c_05.py` y `vuelta179_tarea3_mutacion_triangulos.py`).

**LAS DOS CIFRAS SON VERDADERAS Y CADA UNA LLEVA SU CORTE**, que es exactamente
para lo que la TAREA 1.d cableo el sello: **15 de 98 al corte de apertura,
`74cad47d42e7`**, y **17 de 103 al corte de la corrida de esta tarea,
`8bd3bd3e8864`**. Sin el corte, las dos cifras se contradirian sin manera de
saber cual mira que.

#### 4.b. COMO SE JUZGO, Y ES MECANICO Y NO A OJO

`scripts/loop/vuelta179_tarea4_juzgar_sujeto.py` parsea cada arnes con `ast`,
busca las llamadas que **leen de disco** y mira si dentro aparece la huella de un
fichero vivo, **resolviendo tambien las asignaciones simples** (si el arnes hace
`RUTA = os.path.join(...)` y despues `io.open(RUTA)`, eso cuenta como abrir).

**Y HAY UNA TERCERA CASILLA QUE NO ESTABA EN EL ENCARGO Y QUE HUBO QUE ANADIR
PORQUE MI PRIMERA VERSION ACUSABA EN FALSO.** Leer `git show
<sha de 40>:docs/loop/REPORTE.md` **no es leer el `REPORTE.md` vivo**: es leer un
blob clavado por su huella, que no se mueve nunca mas. Mi primera corrida
clasificaba `vuelta135_2e_mutacion_1.py` y `_2.py` como **ABRE FICHERO VIVO**
teniendo el `sha` delante en la propia linea de la prueba. **Se arreglo antes de
escribir el registro**, y de paso destapo un defecto propio: el patron se habia
escrito con dos `\b` que quedaron guardados como caracteres de retroceso y **la
comprobacion no podia dar verdadero nunca**. Estaba muerta y parecia viva.

**LO QUE ESTE METODO NO PUEDE, Y SE DICE EN VEZ DE PRESUMIR:** no sigue la huella
a traves de funciones auxiliares ni de modulos importados. Por eso cada fila del
registro publica **todas las lineas** donde la huella aparece, abra o no, para
que el ojo pueda mirar donde la maquina no llega. **Marcado DISCUTIBLE.**

#### 4.c. LOS DIECISIETE, REPARTIDOS

| veredicto de la lectura | arneses |
|---|---:|
| `ABRE FICHERO VIVO` | **4** |
| `ABRE UN SUJETO YA CLAVADO` | **2** |
| `LO NOMBRA SIN ABRIRLO` | **11** |
| **total** | **17** |

**Y EL CRUCE CONTRA LO QUE LA GUARDA DICE, QUE ES LO QUE MIDE SI LA GUARDA
ACIERTA:**

| la guarda dice | la lectura dice | arneses |
|---|---|---:|
| `NO DECIDIBLE` | `ABRE FICHERO VIVO` | **3** |
| `NO DECIDIBLE` | `ABRE UN SUJETO YA CLAVADO` | **2** |
| `NO DECIDIBLE` | `LO NOMBRA SIN ABRIRLO` | **4** |
| `SUJETO VIVO` | `ABRE FICHERO VIVO` | **1** |
| `SUJETO VIVO` | `LO NOMBRA SIN ABRIRLO` | **7** |

**LO QUE ESE CRUCE DICE, Y ES LA CIFRA QUE IMPORTA PARA DECIDIR EL CABLEADO: de
17 senalados, solo 4 abren de verdad un fichero vivo.** Los otros **13** o leen
un sujeto ya clavado (**2**) o solo nombran el fichero sin abrirlo (**11**). **La
guarda no se equivoca en su carril**, porque `NO DECIDIBLE` significa
literalmente que el arnes no deja claro cual es su sujeto, y eso es cierto en los
nueve; **pero 7 de los 8 que llama `SUJETO VIVO` no abren nada vivo.**

#### 4.d. LOS CUATRO QUE SI ABREN, NOMBRADOS

| arnes | que abre | la guarda decia |
|---|---|---|
| `vuelta157_tarea4b_mutacion_tachado.py` | `LECTURAS_DIRIGIDAS.md`, con `io.open` sobre la ruta viva | `SUJETO VIVO` |
| `vuelta160_tarea7c_mutacion_guarda_cita.py` | copia `LECTURAS_DIRIGIDAS.md` e `INTRA_DOMINIO_VEREDICTOS.jsonl` vivos a un temporal | `NO DECIDIBLE` |
| `vuelta174_tarea1b_mutacion_esqueleto.py` | `REPORTE.md` | `NO DECIDIBLE` |
| `vuelta150_2d_simular_op_c_05.py` | `master_graph.json` | `NO DECIDIBLE` |

**El caso de `vuelta160_tarea7c` merece su linea**: copia el fichero vivo a un
temporal y trabaja sobre la copia, lo cual parece congelado y no lo es. **El
resultado sigue dependiendo de lo que el fichero vivo diga hoy**, porque la copia
se hace en cada corrida. Por eso `tmp` y `tempfile` **no** cuentan como marca de
clavado en este instrumento, y eso va escrito en su codigo con su motivo.

**LOS DOS QUE LEEN UN SUJETO YA CLAVADO** son `vuelta135_2e_mutacion_1.py` y
`_2.py`, los dos por `git show e12e4c362fe734ff:docs/loop/REPORTE.md`. **No les
falta nada de fondo:** lo unico que les falta es **declararlo** con el literal que
la guarda busca, para dejar de salir `NO DECIDIBLE`.

#### 4.e. EL REGISTRO, Y LO QUE NO SE HIZO

`docs/plan/SUJETO_CONGELADO_VEREDICTOS.jsonl`, **17 filas**, una por arnes, con el
nombre, los dos veredictos, el fichero que abre, **la linea del codigo** como
evidencia, y **que haria falta** para arreglarlo.
**20.939 bytes en disco y 20.939 bytes normalizados a LF.**

**Y LO QUE NO SE HIZO ES TAN PARTE DEL ENCARGO COMO LO QUE SI:**

- **NINGUN ARNES SE ARREGLO.** Cero ficheros de `scripts/loop/` tocados por este
  instrumento.
- **LA GUARDA NO SE CABLEO** al rojo global de la bateria. Sigue corriendo sola en
  su carril con `--sujeto-congelado`.
- **NADA SE BORRO DE LA NOMINA** (`AUDITOR.md` 6.1): sigue en **103** al corte
  `8bd3bd3e8864`.

**LA RECOMENDACION PARA EL CABLEADO, CON LOS VEREDICTOS DELANTE Y NO ANTES**, que
es lo que el encargo pedia dejar preparado: cablearla hoy pondria la bateria de la
181 en rojo por **17**, de los cuales **13 no abren nada vivo**. **Lo barato es al
reves**: primero que los **13** declaren su sujeto, que no cuesta codigo nuevo
sino una linea por arnes, y despues cablear con **4** pendientes de verdad. **No
lo decido yo**, y va como pregunta.

### TAREA 5. LO QUE NO ENTRA Y NO SE PIERDE, CONTADO EN VOZ ALTA

**Ninguna de las cinco se toca**, y las cinco se nombran **con su medicion**, que
es lo que `EJECUTOR.md` 1 exige desde el 5 sep 2026: **una ruta publicada como
prueba es una cifra publicada**, y si apunta a un fichero inexistente o de cero
bytes es caida de cifra. Nombrar cinco pendientes sin comprobar sus sedes es
prometer cinco pruebas sin mirar ninguna.

**LA TABLA SALE DE `docs/loop/SALIDA_V179_T5_NO_ENTRA.txt`** y se pega entera:

| que no entra | sede | existe | bytes en disco | bytes en LF | lineas que la traen |
|---|---|---|---:|---:|---:|
| 1. LA SEGUNDA SEDE DE LA CLAUSULA 4.4 | `docs/loop/reportes/REPORTE_V172.md` | SI | 48851 | 48851 | 2 |
| 2. EL DOCSTRING DEL PASO 0 | `scripts/loop/paso0_archivar_anterior.py` | SI | 7112 | 7112 | 1 |
| 3. LA GUARDA QUE FALTA EN LA DEPENDENCIA DEL `D.4` DE LA 174 | `scripts/loop/vuelta179_esqueleto_reporte.py` | SI | 19911 | 19911 | 2 |
| 4. EL GRANO DEL TOPE DE 10 MINUTOS | `scripts/loop/verificar_mutaciones_viejas.py` | SI | 111914 | 111914 | 1 |
| 5. LA CONVENCION DE BYTES | `docs/loop/AUDITOR.md` | SI | 22612 | 22612 | 1 |

**Las cinco sedes existen, ninguna mide cero bytes y las cinco agujas aparecen.**

**Y EL INSTRUMENTO SALIO EN ROJO EN SU PRIMERA CORRIDA, QUE ES LO QUE SE LE
PIDE.** La aguja de la **2** estaba escrita en mayusculas y el docstring lo dice
en minusculas, `"la vuelta anterior"`, en su linea 25. **Cayo nombrando la aguja
que fallaba**, se corrigio la aguja (no el fichero, que no se toca) y volvio a
correr. Una guarda que no puede salir en rojo no prueba nada.

**LO QUE CADA UNA ES, EN UNA LINEA:**

1. **La segunda sede de la clausula 4.4** vive en `REPORTE_V172.md:535`, y sigue
   ahi, con dos lineas del fichero que la nombran.
2. **El docstring de `paso0_archivar_anterior.py`** sigue hablando de **la vuelta
   anterior** cuando la maquina ya pregunta por **el reporte que va a pisar**. La
   maquina esta bien; el texto que la describe, no. **Esta vuelta lo volvio a
   usar** y las dos preguntas volvieron a coincidir, asi que la divergencia sigue
   sin poderse ver en corrida.
3. **La guarda que falta en la dependencia del `D.4` de la 174**: el esqueleto
   **clona** `vuelta_del_reporte_del_arbol()` en vez de importarla, y **nada avisa
   si el fichero del que se clono desaparece**. El de esta vuelta lo declara en su
   docstring, con dos lineas que lo dicen, y sigue sin instrumento.
4. **El grano del tope de 10 minutos** se mide **EN LA 181**, con el reloj de esa
   corrida, y **no se re-elige a ojo antes**. Esta vuelta no es de bateria y
   medirlo aqui seria medirlo sobre una corrida que no existe.
5. **La convencion de bytes** es del fundador y **lleva seis actas subiendo**, y esa cifra es del encargo de esta vuelta y no
   la recomputo yo.
   **Sube como pendiente, no como problema:** el remedio provisional, publicar
   siempre las dos, ya es instrumento dentro de `cerrar_reporte.py` desde la 178,
   y esta vuelta volvio a salir a coste cero. **Toda cifra de bytes de este
   reporte va por las dos convenciones**, incluidas las cinco filas de arriba.

<!-- FIN ANEXO DE TAREAS -->

## 3. EL CIERRE, CON SU IDENTIDAD LEIDA DE GIT

**Todo hash de esta seccion sale de `git log` o `git rev-parse` corrido en esta
vuelta** (`EJECUTOR.md` 1, LA IDENTIDAD SE LEE DE GIT).

| | |
|---|---|
| rama | `pasada-unica` |
| sello de apertura, escrito ANTES de la 1.a operacion | `74cad47d` (`SALIDA_V179_HEAD_APERTURA.txt`) |
| sello de cierre, escrito TRAS la ultima operacion | `2037f785` (`SALIDA_V179_HEAD_CIERRE.txt`) |
| commits entre los dos sellos | **6** |
| rutas tocadas | **57** (`docs/loop/` 32, `scripts/loop/` 22, `docs/plan/` 3) |
| **el grafo entre los dos sellos** | **`git diff --numstat` sobre `dataset/`, `web/` y `engine/`: 0 filas** |

**LOS SEIS COMMITS, EN SU ORDEN:**

| hash | que cierra |
|---|---|
| `02af60ee` | el bloque de apertura, corrido entero antes de la primera operacion, con el desfase del calibrado DENTRO de el |
| `047b10b1` | el esqueleto del reporte, abierto al empezar con sus CINCO filas vacias |
| `d4a1028c` | la TAREA 1: la correccion declarada, la guarda de la escalada, la nomina y el corte del denominador |
| `8bd3bd3e` | la TAREA 2: los diez pares reales de `OP-L-03`, leidos |
| `09e0d2df` | las TAREAS 3 y 4: los triangulos partidos por su fuente y las del sujeto congelado juzgadas |
| `2037f785` | la TAREA 5: las cinco que no entran, nombradas y medidas |

**EL CICLO DE GATE 0 CORRIO ENTERO Y EN SU ORDEN EN LAS DOS PUNTAS**, nunca
`run_phase1` suelto: `run_phase1.py --reaplico-curaduria`, `etiquetas_de_cara.py
--aplicar`, `sync_assets_web.py`, `git diff HEAD --numstat`,
`engine/run_all_tests.py`, `npx tsc --noEmit` y `pnpm test`. **Las siete piezas
salieron verdes en las dos puntas**, y la tabla de la cabecera de arriba lo
publica columna a columna.

**LA GUARDA DE `dataset/` CORRIO ANTES DE CADA COMMIT** y salio **VERDE** en los
seis, con **0 filas de numstat y 0 blobs divergentes**. **`dataset/` no se toco en
ninguna de las cinco tareas.**

### 3.1 EL COTEJO DE MIS CLONES, PEGADO Y NO AFIRMADO

Desde la vuelta 178 **ningun reporte escribe CLON DECLARADO sin pegar la salida
del instrumento**. La mia vive en `docs/loop/SALIDA_V179_COTEJO_MIS_CLONES.txt` y
esto es lo que dice, contado de ese fichero:

| clon | fichero entero | solo la maquina | AST sin docstring | sentencias de codigo | literales de texto |
|---|---|---|---|---:|---:|
| `vuelta178_cierre.py` contra `vuelta179_cierre.py` | DIFIERE | **IDENTICO** | **IDENTICO** | 0 | 0 |
| `vuelta178_esqueleto_reporte.py` contra `vuelta179_esqueleto_reporte.py` | DIFIERE | DIFIERE | DIFIERE | **0** | **57** |
| `vuelta178_apertura.py` contra `vuelta179_apertura.py` | DIFIERE | DIFIERE | DIFIERE | **174** | **104** |

**LO QUE ESA TABLA DICE, Y NO LO SUAVIZO:** el clon del cierre es un clon de
verdad, con la maquina y el arbol de sintaxis identicos. El del esqueleto tambien:
**cero sentencias de codigo** y 57 literales de texto, que son las cinco filas de
tarea y la prosa. **El de la apertura NO es un clon en el sentido estrecho: cambia
174 sentencias de codigo**, porque su bloque H se reescribio entero para medir los
sujetos de ESTE encargo. **Eso estaba declarado en su docstring antes de correr el
cotejo**, y el cotejo lo confirma en vez de desmentirlo.

## 4. LA GUARDA DEL COMMIT, CORRIDA EN CADA COMMIT DE ESTA VUELTA

`scripts/loop/guarda_commit_dataset.py` corrio antes de cada uno de los seis
commits y salio **VERDE** en los seis: **0 filas de `git diff --numstat` sobre
`dataset/` y 0 ficheros con blob distinto del de HEAD**. El guardian del hook
(`motor` y `web`) tambien salio verde en los seis, y su salida esta en la consola
de cada commit.

## 5. LOS DISCUTIBLES, MARCADOS ANTES DE SABER SI ACIERTO

**D.1. LA VENTANA DE 120 CARACTERES DE LA GUARDA NUEVA.** La elegi contando las
siete distancias reales de `REPORTE_V178.md` (32, 34, 36, 45, 51, 51 y 54) y
poniendo el doble largo de la mayor. **Es una vara que yo fije, no una que el
banco tenga escrita.** Una frase legitima mas larga que 120 caracteres entre su
cifra y su fichero se escaparia sin decir nada. **Prefiero que se escape a que
acuse en falso**, y esa preferencia tambien es mia y no del banco.

**D.2. EL EMPAREJAMIENTO POR CERCANIA.** Cada fichero se casa con la cifra que
tiene mas cerca en su parrafo, y cada cifra se gasta una sola vez. **Sobre el
sujeto real acierta las siete**, pero es una heuristica: un parrafo escrito al
reves la engana.

**D.3. EL `D` DEL PAR 4 DE `OP-L-03`** (`creacion_option_pool` contra
`employee_pool_esop`). El archivo da **dos senales contrarias** por dos terceros
distintos, y resuelvo a favor de la frontera del puesto 1193 declarando que el
otro tercero esta a caballo. **Es la unica de las diez lecturas donde tuve que
elegir entre dos cosas escritas**, y la elijo yo.

**D.4. EL `A` DEL PAR 10** (`evaluacion_` contra `explotacion_tecnologias_
disruptivas`). Los dos repiten con el mismo tercero, pero **el analisis IOTA de
`explotacion_` es lo mas cerca que hay en las diez de un procedimiento propio**.
Si el auditor lo lee como procedimiento, esto es `D`.

**D.5. EL METODO DE LA TAREA 4 NO SIGUE LA HUELLA A TRAVES DE FUNCIONES.** Un
arnes que salga `LO NOMBRA SIN ABRIRLO` y que llame a un tercero que si abre se
me escaparia. **Publico todas las lineas de cada arnes para que el ojo llegue
donde la maquina no**, pero la clasificacion mecanica tiene ese techo.

**D.6. LA TERCERA CASILLA QUE ME INVENTE EN LA TAREA 4**, `ABRE UN SUJETO YA
CLAVADO`, **no estaba en el encargo**, que pedia tres. La anadi porque sin ella
acusaba en falso a dos arneses que hacen exactamente lo que la regla pide.
**Anadir una casilla que el encargo no pide es una decision mia.**

## 6. LAS PREGUNTAS

**P.1. EL CABLEADO DE LA GUARDA DEL SUJETO CONGELADO.** Con los 17 veredictos
delante: cablearla hoy al rojo global pondria la bateria de la 181 en rojo por
**17**, de los cuales **13 no abren nada vivo**. Lo barato parece ser al reves,
que los 13 declaren su sujeto primero y despues se cablee con 4 pendientes de
verdad. **No lo decido yo.**

**P.2. LA ETIQUETA `(vuelta 177)` DE `clases_por_par()`.** Esta rota, esta medida
(5 lados mal de 15) y **el encargo prohibe tocar ese campo**. Queda como PARADA en
la seccion 3.f de la TAREA 3. **Hace falta que alguien autorice cambiarla para que
lea la vuelta del registro en vez del literal.**

**P.3. LA CONDICION `EL PAR TIENE PUESTO` NO PUEDE DAR QUE SI.** Medida en la
TAREA 2: un par real esta definido como el que no esta en el archivo, asi que
nunca trae puesto. **La distincion del punto 7.8 del acta 178 es correcta y su
rama del `SI` es inalcanzable mientras el archivo no tenga huecos.** Vale la pena
saber si eso es lo que se queria.

**P.4. EL ARCHIVO SE CONTRADICE CONSIGO MISMO EN LA FAMILIA DEL OPTION POOL.**
`pool_opciones_empleados` sale `A` con los dos lados de una frontera que el propio
archivo declaro. **No lo toco** (modo de cierre), pero queda nombrado.

## 7. PENDIENTES DE DOCTRINA

**PD.1. NO HAY REGLA ESCRITA PARA LA CADENA DE REPITE.** Use la transitividad
(`a` REPITE con `t` y `b` REPITE con `t`, luego `a` REPITE con `b`) en cinco de
las diez lecturas, apoyandome en `banco 9.3`, que dice que una direccion de fusion
no sobrevive a su familia. **Pero `9.3` dice que hay que MIRAR la familia, no que
la transitividad decida.** Registro lo mejor sostenido y lo marco.

**PD.2. NO HAY REGLA PARA EL SUJETO CLAVADO POR SHA.** `HUELLAS_DE_CONGELADO` ya
incluye `git show` y `cat-file`, pero la guarda los mira **en el texto entero** y
no **en la llamada**, y por eso los dos de la 135 salen `NO DECIDIBLE`. La casilla
que invente en la TAREA 4 no existe en ninguna doctrina escrita.

## 8. MIS CAIDAS PROPIAS, CON SU NOMBRE Y NINGUNA TAPADA

**C.1. LA GUARDA DE LA ESCALADA INVENTABA UN ROJO EN SU PRIMERA CORRIDA.** Sobre
`REPORTE_V178.md` cazaba **dos** y solo una era real: acusaba a la linea 189, donde
la cifra que va con el fichero es la **8** y mi patron solo veia la palabra
`casos`, que ahi acompana a la **5**. **La cazo su propia corrida contra el sujeto
real, no un arnes.** Arreglada antes de seguir.

**C.2. DOS ESPERADOS MIOS MAL PUESTOS EN EL ARNES DE LOS TRIANGULOS.** Esperaba 6
y 6 lados por fuente sobre el registro fabricado y son **7 y 5**. **El codigo
estaba bien y mis dos numeros estaban mal**, y la prueba de mutacion los cazo
porque el esperado equivocado coincidia con el valor mutado.

**C.3. UNA COMPROBACION MUERTA QUE PARECIA VIVA.** El patron del sujeto clavado
de la TAREA 4 se escribio con dos `\b` que quedaron guardados como **caracteres de
retroceso**, y **no podia dar verdadero nunca**. Lo destape al preguntarme por que
salian cero clavados teniendo el `sha` delante en la propia linea de la prueba.
**Es exactamente la especie que el banco 9 llama degradacion silenciosa.**

**C.4. LA AGUJA DE LA TAREA 5 ESTABA EN MAYUSCULAS.** El instrumento salio en ROJO
nombrandola. **Eso no es una caida del instrumento sino de mi aguja**, y lo cuento
aqui porque la primera version del fichero prometia cinco medidas y solo podia dar
cuatro.

**C.5. MI PRIMER CRITERIO DE `TIENE PUESTO` MEDIA OTRA COSA.** Preguntaba si algun
EXTREMO aparece en algun puesto, no si el PAR lo tiene, y con esa vara los diez
salian `SI` cuando la respuesta es `NO`. **Habria mandado los diez veredictos al
fichero equivocado.**

**C.6. LA GUARDA NUEVA CAZO ESTE MISMO REPORTE AL CERRARLO, Y NO ERA UN FALSO
ROJO NI ERA CORRECTO DEJARLO.** La tabla de la TAREA 1.a publica **16** al lado
de `SALIDA_V178_T1E_MUTACION.txt`, porque `EJECUTOR.md` 8 obliga a declarar la
correccion **sin borrar el texto viejo**. La guarda acusaba al reporte por hacer
lo que la doctrina manda. **Se le anadio su unica exencion**, que hay que pedir
por escrito diciendo el literal **CORRECCION DECLARADA** en el parrafo, con sus
cuatro casos nuevos por mutacion, incluido el que comprueba que **sin esas
palabras vuelve a ser rojo**. **La cazo la propia guarda contra su propio
reporte, no un arnes**, que es la segunda vez en esta vuelta que eso pasa.

**C.7. LA QUE VIENE DE LA VUELTA PASADA Y ES LA QUE ABRE ESTE REPORTE:** la 178
publico **16** donde su fichero decia **18**. Corregida en la TAREA 1.a con las
tres cifras al lado y sin retocar el reporte archivado.

## 9. LA BATERIA DE MUTACIONES: HUECO DECLARADO Y MEDIDO

**HUECO DECLARADO Y MEDIDO. LA BATERIA DE LA VUELTA 179 NO CORRIO, Y EL HUECO SE DECLARA EN VEZ
DE RELLENARSE CON OTRA COSA.**

**EL NOMBRE DEL FICHERO:** `docs/loop/SALIDA_V179_BATERIA.txt`.
**SUS BYTES, MEDIDOS EN ESTA CORRIDA** con `os.path.getsize` por
`scripts/loop/cerrar_reporte.py`, no tecleados, y POR LAS DOS
CONVENCIONES mientras la del fundador no este fijada:
**0 bytes en disco y 0 bytes normalizados a LF**.

ATRIBUCION: NADIE la corrio, y no es un olvido: esta vuelta NO ES DE BATERIA. La cadencia esta adjudicada en el acta 176 punto 7.8, reconfirmada en el acta 178 punto 11 y repetida por el encargo de esta vuelta: LA PROXIMA VUELTA DE BATERIA ES LA 181, y la 179 y la 180 cierran su seccion 9 con el hueco declarado y medido. Lo que SI corrio esta vuelta de la propia bateria es su guarda del sujeto congelado, en su carril y sin cablear al rojo global (docs/loop/SALIDA_V179_T4_GUARDA.txt), que sale en ROJO con 17 de 103 al corte 8bd3bd3e8864.

**POR QUE ESTO CIERRA Y UNA AUSENCIA MUDA NO.** La pieza (4) de este
instrumento admite el hueco declarado desde la vuelta 173, TAREA 1.b
(adjudicacion 6.2 del acta del auditor de la vuelta 172), y la letra es
estrecha: **el nombre, los bytes medidos y la atribucion, LAS TRES JUNTAS**.
Faltando cualquiera de las tres, este instrumento sigue cayendo en ROJO, y
**una corrida de otra vuelta pegada aqui tampoco vale**.
