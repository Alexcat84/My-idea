# -*- coding: utf-8 -*-
r"""vuelta164_tarea7_escribir_reporte.py . EL CIERRE DE LA VUELTA 164.

ESCRIBE `docs/loop/REPORTE.md` DE LAS DOS VUELTAS, LA 163 Y LA 164, por la
adjudicacion 6.1 del acta 163.

LA CABECERA NO SE TECLEA: SE LEE DEL FICHERO QUE LA TALLA. El cuerpo es prosa
del ejecutor; la cabecera se pega ENTERA desde
`docs/loop/SALIDA_V164_T7_CABECERA.txt`, que es la salida de
`scripts/loop/tallar_cabecera_reporte.py --fase04 --vuelta 164`. Este script
PARA si ese fichero no esta o no trae su tabla: la regla de la casa es que la
celda que no salga de un instrumento NO SE ESCRIBE.

USO:  python scripts/loop/vuelta164_tarea7_escribir_reporte.py
"""
import io
import os
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(os.path.dirname(AQUI))
CABECERA = os.path.join(RAIZ, "docs", "loop", "SALIDA_V164_T7_CABECERA.txt")
REPORTE = os.path.join(RAIZ, "docs", "loop", "REPORTE.md")


def cabecera_tallada():
    if not os.path.exists(CABECERA):
        raise SystemExit("ROJO: no existe %s. La cabecera no se teclea." % CABECERA)
    t = io.open(CABECERA, encoding="utf-8").read()
    if "| | **apertura**" not in t:
        raise SystemExit("ROJO: el tallador no publico su tabla. No se escribe nada.")
    ini = t.index("| | **apertura**")
    fin = t.index("\nFIN")
    return t[ini:fin].rstrip() + "\n"


CUERPO = r"""# REPORTE DE LAS VUELTAS 163 Y 164 (ejecutor). FASE III, EJECUCION. Rama `pasada-unica`.

**ESTE REPORTE CUBRE DOS VUELTAS Y NO UNA, por la adjudicacion 6.1 del acta 163**
(`docs/loop/ACTA_AUDITOR.md:54293`, leida hoy): *"LA VUELTA 163 NO SE CIERRA POR
ACTA: SE TERMINA, Y LA SIGUIENTE ES LA 164."* La 163 se corto dentro de su TAREA
2 y la 164 absorbe su cola. **Lo que la 163 dejo ya sellado se CITA con su
fichero y no se re corre**; lo que dejo a medias se termina aqui.

**EL VEREDICTO DE UNA LINEA: EL ENCARGO ENTREGADO ENTERO, LAS SEIS TAREAS, Y LA
COLA DE LA 163 CERRADA.** La bateria de las 53 corre por fin de punta a punta y
sale VERDE con su cronometro publicado; sus dos rojos se arreglaron EN LA FUENTE
y ninguno en verde alegado. **UNA CLASE PUBLICADA SE MUEVE Y ES CAIDA MIA**: la
`LD-OPC05-005` pasa de `C` a `D` con correccion declarada. **La `LD-OPC05-101` se
sostiene en `D` y su veredicto se publica re derivado de la vara congelada, sin
las dos sub varas que no son ejemplares.** **Cero nodos tocados, cero aristas
movidas y el grafo intacto.** Traigo **CINCO DISCUTIBLES MARCADOS**, dos
**PREGUNTAS** y una **PENDIENTE DE DOCTRINA**, y los marco antes de saber si
acierto.

## 0. LA IDENTIDAD Y LA CABECERA, TALLADAS Y NO TECLEADAS

Todo lo de esta seccion sale de
`scripts/loop/tallar_cabecera_reporte.py --fase04 --vuelta 164`, salida
`docs/loop/SALIDA_V164_T7_CABECERA.txt`, pegada entera por
`scripts/loop/vuelta164_tarea7_escribir_reporte.py`, que la LEE del fichero y
PARA si no esta.

<!-- CABECERA TALLADA -->
%(CABECERA)s<!-- FIN CABECERA TALLADA -->

**EL CORREDOR DE ESTA VUELTA NO ADMITE NINGUN HASH Y NO HIZO FALTA ADMITIR
NINGUNO.** El acta 163 (`70358b97`) escribe su encargo en el mismo commit. El
bloque de apertura nace como HIJO DIRECTO del acta en `28dde491`, y la guarda lo
confirma: `verificar_apertura_sellada.py --vuelta 164` sale **VERDE exit 0** con
los diez `SALIDA_V164_*_APERTURA.txt` nacidos todos ahi
(`docs/loop/SALIDA_V164_APERTURA_GUARDA.txt`).

**LA COLA DE LA 163 ENTRO EN ESE MISMO COMMIT Y NO EN UNO SUYO**, que es la
adjudicacion 6.2 del acta 163 (`docs/loop/ACTA_AUDITOR.md:54301`): un commit
entre el acta y la apertura es intruso salvo que el encargo cite su hash, y ese
hash no existia cuando se escribio el encargo. **El bloque no se fragmento.**

**LA APERTURA Y EL CIERRE NO HEREDAN UNO DEL OTRO.** El ciclo de Gate 0 se
corrio ENTERO y en su orden las dos veces, nunca `run_phase1` suelto:
`--reaplico-curaduria`, `etiquetas_de_cara --aplicar`, `sync_assets_web` y
despues `git diff HEAD --numstat -- dataset/ web/ engine/`, que da **cero filas**
(`docs/loop/SALIDA_V164_CICLO_NUMSTAT_CIERRE.txt`).

**LAS TRES CONSTANCIAS DEL CIERRE, CADA UNA CON SU FICHERO AL LADO.** GATE 0 OK
en `docs/loop/SALIDA_V164_GATE0_CMD1_CIERRE.txt`. El motor da 25/25 en
`docs/loop/SALIDA_V164_MOTOR_CIERRE.txt`. Y la cabecera de este reporte sale
IDENTICA AL TALLADOR en `docs/loop/SALIDA_V164_T7_CABECERA_COMPARADA.txt`.

## 1. QUE ENTREGO LA 163 Y QUE TERMINA LA 164, TAREA A TAREA

**LO DE LA 163 NO SE RE CORRE Y SE CITA.** El auditor verifico una a una en la
seccion 2 de su acta 163 las siete que si llegaron: `1.a` (`R.32` escrita,
`docs/loop/SALIDA_V163_T1A_REGISTRO_ACTA_162.txt`), `1.b` (dossier de la `101`,
`docs/loop/SALIDA_V163_T1B_DOSSIER_101.txt`), `1.c` (tramo al doble,
`docs/loop/SALIDA_V163_T1C_TRAMO.txt`), `3` (arnes `162_1a`,
`docs/loop/SALIDA_V163_T3_ARNES_ARREGLADO.txt`), `4.a` (cobertura de cifras,
`docs/loop/SALIDA_V163_T4A_MUTACION.txt`), `4.b` (re sellado ciego,
`docs/loop/SALIDA_V163_T4B_MUTACION.txt`) y `5.a` (contador estable,
`docs/loop/SALIDA_V163_T5A_COTEJO.txt`).

**LO QUE FALTABA, Y ESTA HECHO HOY:** la corrida de la bateria (2.a), la
declaracion de las tres `SALIDA_V135_2E_MUTACION` (2.b), el anclaje del arnes de
la 4.b (2.c), la medicion de los pre 148 (5), la TAREA 6, el cierre y este
reporte.

## 2. TAREA 1, EL ACTA 163 REGISTRADA COMO `R.33`, Y DOS DEFECTOS MIOS CAZADOS ANTES DE COMMITEAR

**EL NUMERO Y LA SEDE, COMPUTADOS.** `scripts/loop/serie_de_registros.py` antes
de escribir (`docs/loop/SALIDA_V164_T1_SERIE_ANTES.txt`): **24 entradas, cero
colisiones, cero huecos, siguiente libre `R.33`**. Despues
(`docs/loop/SALIDA_V164_T1_SERIE_DESPUES.txt`): **25, cero y cero, siguiente
libre `R.34`**. La SEDE sale de la adjudicacion 6.3 del acta 162, leida hoy en
`docs/loop/ACTA_AUDITOR.md:53933`, **y se DECLARA que el acta 163 no la repite**:
contada hoy, esa frase aparece UNA sola vez en todo el fichero.

**LAS DIEZ ADJUDICACIONES Y MI CAIDA DEL AUDITOR, EN `docs/PENDIENTES.md:10684`**
(`docs/loop/SALIDA_V164_T1_REGISTRO_ACTA_163.txt`). Reparto CONTADO y no
tecleado: **2 EN CODIGO** (6.6, 6.8), **2 EN EL PROCEDIMIENTO** (6.1, 6.2), **3
EN EL REPORTE** (6.4, 6.5, 6.7), **1 EN MEDICION** (6.9) y **2 SIN TOCAR NADA**
(6.3, 6.10). **Adicion pura: 69 anadidas y CERO borradas.** Y la CAIDA 1 de la
seccion 4 del acta se registra igual que las mias, por letra del encargo.

**Y AQUI EL ARNES DE MUTACION ME CAZO DOS COSAS MIAS, LAS DOS ANTES DE
COMMITEAR.** Van con su nombre porque callarlas seria lo contrario del banco 9.

  **(3) LA NEGRITA QUE NUNCA PARA.** `titulo_de_la_negrita`, heredada del
  instrumento de la 163, acumulaba HASTA EL FINAL DEL ACTA buscando el asterisco
  de cierre, **sin frontera ninguna**. Su camino de PARADA *"la negrita no
  cierra"* era **INALCANZABLE** en cualquier documento donde despues venga otra
  negrita: al no cerrar la suya se comia el marcador de APERTURA de la entrada
  siguiente y salia en VERDE con un titulo trunco. **Una guarda cuyo rojo no
  puede dispararse.** La frontera que se pone es la LINEA EN BLANCO, y esta
  MEDIDA: las **once** negritas del acta 163 se leen con la funcion arreglada
  **sin un solo error**, y los **once** titulos leidos hoy aparecen verbatim en
  la `R.33` escrita. La funcion VIEJA se copia byte a byte dentro del arnes y se
  corre sobre el MISMO sujeto: no para, y devuelve como titulo el texto sin
  cerrar de la 6.9 porque tomo por delimitador el asterisco de apertura de la
  6.10.

  **(4) LA IDEMPOTENCIA CIEGA, Y ESTA LA COBRE EN VIVO.** La comprobacion de
  *"ya estaba"* busca el titulo en lo que devuelve `serie_de_registros.py`, y ese
  instrumento lee el titulo **de la linea del doble almohadilla y solo de esa
  linea**. El instrumento heredado escribia su cabecera PARTIDA en tres lineas,
  o sea que el titulo que la serie ve queda TRUNCADO y **la idempotencia no puede
  dar positiva jamas**. Medido en vivo: la primera corrida escribio `R.33` y la
  segunda, sobre la misma acta, escribio `R.34`. `docs/PENDIENTES.md` se restauro
  con `git checkout --` ANTES de commitear nada, la cabecera pasa a UNA SOLA
  LINEA y la comprobacion deja de fiarse de si misma: si el titulo esta escrito
  pero la serie no lo ve, PARA. **Re corrido hoy: `YA ESTABA: la entrada vive
  como R.33` y escribe cero.**

**CASO POSITIVO POR MUTACION** (`docs/loop/SALIDA_V164_T1_MUTACION.txt`): **38
casos, los 38 pasan y los 38 CAEN** al mutarles el esperado. Cero escrituras: las
actas de mentira son listas de lineas en memoria. Los esperados que podrian
caducar son DELTAS.

## 3. TAREA 2, LA COLA DE LA 163 CERRADA

### 3.a LA BATERIA ENTERA, CON SU CRONOMETRO (adjudicacion 6.8)

**LA CORRIDA COMPLETA QUE LA 163 NO LLEGO A HACER**
(`docs/loop/SALIDA_V164_T2A_BATERIA_SEGUNDA.txt`, la definitiva tras los
arreglos): **53 entradas en la nomina**, **92** arneses de mutacion en
`scripts/loop/`, **CERO posteriores fuera** medido al abrir Y **recomputado al
cierre**. **ANCLA PERDIDA 0, NO MORDIO 0, NO REPRODUCIBLE 0, CASO DECLARADO 2**
(`vuelta135_2e_mutacion_3.py` y `vuelta140_2a_mutaciones.py`, los dos con su exit
declarado y su marca obligatoria). **RUIDO DE CONCURRENCIA: NINGUNO**, o sea
que se corrio sola como manda la casa. **VERDE, exit 0.**

**EL CRONOMETRO, QUE ES LO QUE LA 6.8 ENCARGA:** tiempo total **978,2 segundos,
16,3 minutos**; el mas lento `vuelta159_tarea6c_mutacion_exencion.py` con
**375,7s**; el mas rapido `vuelta162_tarea2a_mutacion_puerta.py` con **1,8s**;
mediana **3,0s**; **SEIS** arneses pasan de 30 segundos. Y el aviso queda impreso
dentro de la propia guarda: **cada entrada se corre DOS VECES** por el cotejo de
reproducibilidad de la 141, asi que ese total ya incluye las dos pasadas.
**Matarla antes NO es un rojo: es no haberla medido.** La nomina **NO se
recorto** y no se quito ni una comprobacion.

**LOS DOS ROJOS DE LA PRIMERA CORRIDA**
(`docs/loop/SALIDA_V164_T2A_BATERIA.txt`, sellada y no borrada), **arreglados en
la fuente y ninguno en verde alegado. Son la misma enfermedad: un esperado
clavado a un estado que otra vuelta mueve legitimamente.**

  **ROJO 1, `vuelta163_tarea5a_mutacion_contador.py`.** Su vara tenia los cinco
  numeros del encargo de la 163 TECLEADOS. **Mi propia TAREA 4 de hoy** le
  escribio a la `LD-OPC05-005` y a la `101` sus marcas de relectura conjunta, que
  son CONTABLES por `P.5.2`, y `con dos o mas` paso de 16 a 17, `actos sobre
  filas` de 115 a 117 y `tipos de acto` de 8 a 9. **El arnes cayo sin que nadie
  tocara su codigo.** Arreglado: la vara se RECOMPUTA corriendo el contador sobre
  el registro **del commit de apertura de la vuelta 163** (`75ad1e06`, leido de
  `git log --diff-filter=A` sobre su sello de HEAD, cero hashes tecleados),
  importando el contador y sin reimplementar una linea de su cuenta, con el
  temporal retirado siempre (P.16). **La vara tecleada NO se borra**: queda al
  lado y se COTEJA contra la recomputada, y **reproduce las cinco al digito, 0
  discrepancias** (`docs/loop/SALIDA_V164_T2A_COTEJO_CONTADOR.txt`). Los tres
  corredores dan **92 / 17 / 30 / 117 / 9** los tres. **16 casos, los 16 pasan y
  los 16 CAEN.**

  **ROJO 2, `vuelta157_tarea5c_mutacion_ruido.py`.** Su caso (D) era literalmente
  `len(VIEJAS) == 23`, **una constante literal**. **Llevaba ROJO desde la vuelta
  163**, cuando la 6.8 del acta 162 hizo crecer la nomina de 23 a 51, y **nadie
  lo vio porque la bateria de aquella vuelta nunca termino**. Arreglado midiendo
  lo que ese caso queria decir de verdad, **que la nomina NO MENGUA**: se importa
  la guarda del commit de apertura de la vuelta 157 (`abb2fe4e`, que el propio
  arnes ya sacaba de git) y se exige CONTENCION. Medido
  (`docs/loop/SALIDA_V164_T2A_RUIDO_ARREGLADO.txt`): **23 en el commit de
  apertura, 53 hoy, CERO perdidas**. Crecer ya no lo tumba y encoger si. Su
  `--mutar` sigue cayendo con exit 1.

### 3.b LAS TRES `SALIDA_V135_2E_MUTACION`, DECLARADAS (adjudicacion 6.7)

**NO SE PROHIBE RE SELLAR: SE PROHIBE RE SELLAR EN SILENCIO.** La 163 las re
sello y su reporte no llego a existir. Van nombradas con su `numstat` medido
antes del commit de apertura y con su motivo:

| fichero | `numstat` | motivo |
|---|---|---|
| `docs/loop/SALIDA_V135_2E_MUTACION_1.txt` | **+1 / -1** | la TAREA 4.a de la 163 anadio a la linea `COBERTURA` el segmento `afirmaciones de cierre PRESENTES`, y la salida se regenero con el segmento nuevo |
| `docs/loop/SALIDA_V135_2E_MUTACION_2.txt` | **+1 / -1** | igual que la anterior |
| `docs/loop/SALIDA_V135_2E_MUTACION_3.txt` | **+1 / -1** | igual que la anterior |

**SU VEREDICTO NO SE MUEVE**, y es lo que hace que el re sellado sea inocuo: las
tres siguen en **ROJO con `EXITCODE proceso: 1`** antes y despues. Y en el mismo
commit entro la bateria nueva, `scripts/loop/verificar_mutaciones_viejas.py`, con
**+282 / -5**.

**Y VA TAMBIEN LA FORMA LITERAL QUE `verificar_re_sellado.py` EXIGE, QUE MIDE
CONTRA OTRA REFERENCIA Y POR ESO DA OTRO NUMERO.** Mi tabla de arriba mide el
delta de la 163 contra el commit anterior; la guarda mide contra **el commit de
su tarea**, que es `53cca3cd`, el de la vuelta 135 que las creo. **Las dos
cifras son ciertas y se publican las dos, en vez de elegir la que convenga:**

RE SELLADO DECLARADO: SALIDA_V135_2E_MUTACION_1.txt numstat +7/-4, lineas CIFRA con valor cambiado: 0 (ninguna)

RE SELLADO DECLARADO: SALIDA_V135_2E_MUTACION_2.txt numstat +7/-4, lineas CIFRA con valor cambiado: 0 (ninguna)

RE SELLADO DECLARADO: SALIDA_V135_2E_MUTACION_3.txt numstat +8/-8, lineas CIFRA con valor cambiado: 0 (ninguna)

**LO QUE ESAS TRES LINEAS DICEN Y QUE NO SE ME ESCAPA: `lineas CIFRA con valor
cambiado: 0` en las tres.** El re sellado anadio un segmento a la linea
`COBERTURA` y **no movio ni una cifra**, que es exactamente por que no cambia
nada de lo que esas salidas prueban.

### 3.c EL ARNES DE LA 4.b, ANCLADO (adjudicacion 6.6), Y LA GUARDA SIN TOCAR

**LA GUARDA `verificar_re_sellado.py` NO SE TOCA**: esta bien y muerde de verdad.
Lo que estaba roto era el arnes. **Tres casos leian el arbol de trabajo vivo y
clavaban su estado**, y su letra vieja **no se borra**: queda impresa dentro de la
propia salida del arnes.

  - `F_hoy_la_guarda_sale_VERDE` y `F_hoy_no_hay_ninguna_sin_nombrar`: sellados
    dieron 17 de 17; corridos por el auditor con tres `SALIDA_*` modificadas en
    vuelo dieron 14 de 17 **sin que nadie tocara una linea de codigo**. No es un
    falso verde: es un **falso rojo**.
  - `G_mismo_exit` era ademas **FALSO POR CONSTRUCCION** el dia que el camino
    nuevo muerde: si la nueva ve algo que la vieja no puede ver, sus exit TIENEN
    que diferir. **Exigir que coincidan es exigir que el remedio no remedie.**

**CON QUE SE SUSTITUYEN, Y NINGUNO MIRA EL ESTADO DEL ARBOL:** pares FIJOS Y
COMPUTADOS (el de la 161 sale entero de `git log --diff-filter=A` sobre sus dos
sellos de HEAD, sin un digito tecleado, y los dos hashes tecleados del par 162 se
COTEJAN contra su version computada); INVARIANTES (la lista de la guarda contra
`git` en crudo); e IMPLICACIONES (la nueva nunca afloja; si los exit difieren lo
explica el camino nuevo; el exit de hoy lo explica su propia cuenta). **24 casos,
los 24 pasan y los 24 CAEN** (`docs/loop/SALIDA_V164_T2C_ARNES_ANCLADO.txt`).

**Y LA PRUEBA DE QUE EL ANCLAJE FUNCIONA ESTA CORRIDA, NO ALEGADA**
(`docs/loop/SALIDA_V164_T2C_PRUEBA_DEL_ANCLAJE.txt`): se ensucian a proposito las
tres `SALIDA_V135_2E_MUTACION`, **la guarda sale ROJO exit 1 nombrandolas** y
**este arnes sigue dando 24 de 24 VERDE sobre ese mismo arbol sucio**. P.16: las
tres se restauran y se comprueba que el arbol queda limpio.

## 4. TAREA 3, EL VEREDICTO DE LA `LD-OPC05-101`: **SOSTENGO LA `D`**

**LA VARA, LEIDA HOY DEL BANCO** (`docs/plan/BANCO_DEL_PLAN.md:342`):
*"LA SEGUNDA LINEA DE UN PAR SOLO CUENTA COMO EXPANSION SI TRAE PROCEDIMIENTO
PROPIO, Y NO SOLO EL NOMBRE DE OTRO"*, **mas sus cuatro ejemplares**, que son la
vara tanto como la frase: `052` y `095` ACEPTAN, `122` y `100` EXCLUYEN.

**LA LINEA 1 NO ESTA EN DISCUSION Y ES LIMPIA:** el paso 8 de
`search_for_business_model` lo expanden los doce pasos de
`lienzo_modelo_negocio`.

**LA PREGUNTA CONCRETA, CONTESTADA CON SUS PALABRAS: los pasos 3, 4 y 5 de
`search`, SIN EL PASO 2, NO PASAN LA FRASE DE `P.5.1`.** Y va uno a uno.

  - **PASO 3** (*aplica el proceso de Customer Development para salir a probar
    cada hipotesis con clientes reales*): **nombra un cuerpo externo y no enumera
    nada de el**. Contra el ejemplar que la vara ACEPTA: en la `052` el paso que
    pasa es *las 6 preguntas de Chopra y Meindl*, y pasa porque **ENUMERA sus
    seis dimensiones dentro de la propia linea**. La segunda mitad de la frase,
    *"y no solo el nombre de otro"*, **cae exactamente ahi**, y para decirlo **no
    hace falta la `027`**: lo dice la frase con el ejemplar `052` al lado.
  - **PASO 4** (*evita montar estructuras o roles de ejecucion antes de validar el
    modelo*): es una **PROHIBICION**. No dice que hacer, dice que no hacer, y no
    produce nada. Ninguno de los cuatro ejemplares acepta una linea de esta forma.
  - **PASO 5** (*itera y pivota segun la evidencia recogida hasta encontrar un
    modelo repetible y escalable*): **orden mas complemento mas criterio de
    parada**. Tiene el *hasta*, pero **no dice QUE cambiar ni COMO**. Contra la
    `095`, que la vara ACEPTA: sus cinco pasos son **cinco objetos distintos que
    se encadenan** y producen un entregable propio.
  - **Y LOS TRES JUNTOS TAMPOCO**, porque de los tres **solo dos producen algo**
    (el 3 produce evidencia y el 5 la consume; el 4 no produce nada) y **el nucleo
    productivo del 3 esta delegado entero a un cuerpo que no se enumera**.

**POR QUE EL PASO 2 NO SE PUEDE CONTAR AQUI, Y NO ES POR PEDIRLO EL AUDITOR:** el
paso 2 de `search` es **el unico de esa vecindad que enumera**, o sea el unico
con forma de `052`, **pero ya esta del lado de la direccion limpia**: la propia
razon de la vuelta 160 lo pone ahi con todas sus letras. Contarlo tambien como
expansion de la linea 2 lo pondria **en los dos lados**, que es la figura que el
9.22 excluye y **por la que la vuelta 157 tumbo la `LD-OPC05-005`**.

**LO QUE LE CONCEDO AL AUDITOR, Y NO ME LO CALLO PORQUE ME CONVENGA: TIENE RAZON
EN QUE EL SEGUNDO CRITERIO DE LA `100` NO SIRVE AQUI.** Alli se escribio que *"un
procedimiento que no recibe el vacio no puede ser el como se llena ese vacio"*, y
en la `101` **`search` SI RECIBE el lienzo**: su entregable es *"un lienzo de
hipotesis de modelo de negocio marcado explicitamente como no probado"*. Ese
criterio, que en la `100` fue una de las tres patas, **aqui no tumba nada**. **La
`D` se sostiene SOLO por la primera pata, LA FORMA**, que es la que la frase
congelada mide.

**LO QUE MIDO Y NO USO, POR LA ADJUDICACION 6.3:** el cruce de entregables es
**corroborador y no decisor**, y ademas, mecanizado sobre los cuatro ejemplares,
**reproduce 1 de 4** (recomputado hoy en
`docs/loop/SALIDA_V164_T4_DOSSIER_005.txt`). **Un corroborador que solo acierta
una parte de su propia vara no sostiene un veredicto, ni a favor ni en contra.**

**Y LA RAZON VIGENTE CITA DOS SUB VARAS QUE NO SON EJEMPLARES**, la `027` y la
`004`: medido por el dossier de la 163 en su seccion F, **CIFRA sub varas citadas
en la razon que NO son ejemplares de `P.5.1`: 2**. **Eso no invalida la `D`:
obliga a re derivarla, y aqui se re deriva.** El veredicto queda escrito en la
razon del registro y ya no vive en un asunto de commit
(`docs/loop/SALIDA_V164_T34_VEREDICTOS.txt`).

## 5. TAREA 4, LA `LD-OPC05-005`: **PASA DE `C` A `D`, Y ES CAIDA DE CLASE MIA**

**NO SE LA DOY POR SER SUYA, Y DIGO QUE LA DECIDE.** Lo decisivo no es la pluma
del auditor: es **una reserva que mi propia relectura de la vuelta 161 dejo
escrita y que hoy vence**. Aquella sostuvo la `C` diciendo, literal en la razon:
*"SE SOSTIENE PORQUE LOS TRES PASOS LEEN COMO SECUENCIA, no porque ninguno de
ellos solo procedimente"*. **La `C` descansaba ENTERA sobre que los TRES pasos
(1, 3 y 5 de `aim_of_leadership`) forman secuencia.**

**Y EL PRIMERO DE ESOS TRES NO PUEDE ESTAR AHI, POR LO QUE LA PROPIA RAZON YA
DECIA ANTES DE HOY:** la vuelta 157 declaro, y la relectura conjunta de la 159 lo
**re confirmo por escrito**, que el paso 1 de `aim_of_leadership` y el paso 13 de
`causas_comunes_vs_especiales` **SI COLAPSAN en la misma linea**. **Un paso que
repite la linea no puede ser el como se hace esa linea.**

**Y LO MIDO EN VEZ DE CITARLO DE MEMORIA, CON SU LIMITACION DECLARADA**
(`docs/loop/SALIDA_V164_T4_DOSSIER_005.txt`, seccion E): de los seis pasos de
`aim_of_leadership`, el paso 1 esta en el **maximo** de solape lexico con el paso
13, y el solape medio de los otros cinco es una fraccion del suyo. **PERO EMPATA
CON EL PASO 5, y lo digo en vez de publicar "es el mayor" a secas: el solape
lexico por si solo NO decide.** Lo que decide es que **el colapso ya estaba
establecido en el registro desde la 157**.

**QUITADO EL PASO 1, QUEDAN EL 3 Y EL 5, Y NINGUNO TRAE PROCEDIMIENTO PROPIO.**

  - **PASO 3** (*disenar formas de ayuda individual o de reconocimiento segun
    corresponda*): orden mas complemento mas una condicion vaga. **No trae
    metodo, ni instrumento con autor, ni secuencia, ni entregable propio**, que
    son las cuatro palabras con las que la razon de la `100` excluyo su paso 2.
  - **PASO 5** (*reconocer y estudiar a quienes tienen un desempeno excepcional
    para replicar sus metodos*): orden mas complemento mas finalidad. No dice
    COMO se estudia ni con que instrumento ni que produce; **y ademas cubre UNA
    SOLA de las dos colas** de la linea 13, la alta, cuando la linea habla de
    quienes caen fuera de las tolerancias en cualquier direccion.

**EL EXISTENCIAL DE LA 6.3 DEL ACTA 158 SE RECORRIO ENTERO ANTES DE DECIRLO**,
porque descartar UN par no descarta la figura. **La respuesta es NINGUNA linea, y
el motivo es estructural y medible:** `aim_of_leadership` tiene **6 pasos**,
**uno solo enumera**, **ninguno trae criterio de parada** y su entregable es **un
plan de liderazgo**, o sea un documento, no un metodo aplicable a la linea de
otro nodo. Los tres pares mas fuertes descartados van nombrados en la razon: el
paso 7 de `causas` contra el paso 4 de `aim` (otro colapso), el paso 15 de
`causas` contra el paso 6 de `aim` (**la direccion esta al reves**: refuerza la
limpia) y el paso 11 de `causas` contra el paso 3 de `aim` (sujetos distintos).

**Quitada la linea 2 queda EXACTAMENTE UNA SOLA DIRECCION**, madre e hijo, y la
misma vara que escribio *"UNA SOLA DIRECCION ES MADRE E HIJO Y EL PAR CONTINUA"*
en la `004` y en la `100` **da `D` aqui tambien**.

**EL CRUCE DE ENTREGABLES NO SE USA (6.3) Y ADEMAS NO DICE NADA EN ESTE PAR:**
medido hoy da **NINGUNO**, ningun entregable nombra al otro. Se publica para que
no se herede como si hubiera dicho algo.

**Y UNA COSA MAS QUE NO ME CALLO PORQUE ME FAVORECE AL REVES:** la ciega del
auditor de la vuelta 161 dio `C` sobre este par y coincidio; la de la 163 da `D`.
**Dos ciegas de la misma pluma con letras distintas**, y el propio auditor lo
declaro antes que nadie. **Esta clase NO se mueve por esa segunda ciega: se mueve
porque mi reserva de la 161 vencio contra los nodos.**

**UNA GUARDA VIEJA MORDIO EN EL SITIO, Y ES LA MEJOR NOTICIA DE ESTA SECCION.**
El motor comun escribe `clase`, `razon` y la celda del `.md` **pero no el campo
`cita`**; en la vuelta 160 eso dejo CUATRO citas mintiendo y no lo vio nadie hasta
el cierre. **Hoy la guarda `C.7`, que nacio de aquella caida, salio ROJA con exit
1 nombrando `LD-OPC05-005` antes de que nada se publicara.**
`scripts/loop/vuelta164_tarea4_unificar_cita.py` la reescribe a la forma unica de
la 6.6 del acta 158 (`docs/loop/SALIDA_V164_T4_CITA.txt`) y el motor re corrido da
**`C.7` en CERO** (`docs/loop/SALIDA_V164_T34_VEREDICTOS_RECORRIDO.txt`).

**CASO POSITIVO POR MUTACION DE LO MECANICO**
(`docs/loop/SALIDA_V164_T34_MUTACION.txt`): **36 casos, los 36 pasan y los 36
CAEN**. **Y SE DECLARA QUE NO HAY CASO ROJO AUTOMATICO PARA EL VEREDICTO**: la
clasificacion de un paso como procedimiento propio o como orden mas complemento
es lectura del ejecutor, y fabricarle un caso que se apruebe solo seria la caida
2 de la vuelta 89.

## 6. LAS CIFRAS QUE SE MUEVEN, DECLARADAS Y NO ESCONDIDAS

**EL MARCADOR DEL ARCHIVO NO SE MUEVE Y EL GRAFO TAMPOCO**
(`docs/loop/SALIDA_V164_T7_MARCADOR_CIERRE.txt`, recomputado al cierre): `n`
**3.388**, `A` **551**, `B` **72**, `C` **5**, `D` **2.760**, **huecos 0 y
duplicados 0**. Censo **3.853 / 3.169 / 684**. Aristas **8.780 / 8.740 / 17.520 /
9.914** con `solo_sig` 1.174, `solo_prev` 1.134 y **cero auto enlaces**. El motor
de veredictos comprueba ademas que el `sha256` de `dataset/` es **IDENTICO antes
y despues**.

**LO QUE SI SE MUEVE, Y SE DICE POR QUE:**

| cifra | apertura de la 164 | cierre de la 164 | por que |
|---|---:|---:|---|
| registro, `LECTURA_DIRIGIDA` clase `C` | 14 | **13** | la `LD-OPC05-005` pasa a `D` |
| registro, `LECTURA_DIRIGIDA` clase `D` | 108 | **109** | la misma |
| `P.5.2`, con AL MENOS UNA | 92 | **92** | las dos filas ya tenian marca |
| `P.5.2`, con DOS O MAS | 16 | **17** | la `101` gana su segunda marca |
| `P.5.2`, con NINGUNA | 30 | **30** | no se mueve |
| `P.5.2`, total de actos sobre filas | 115 | **117** | las dos marcas nuevas |
| `P.5.2`, actos distintos (tipo, vuelta) | 8 | **9** | nace el acto `RELECTURA_CONJUNTA` de la vuelta 164 |

Antes y despues sellados en `docs/loop/SALIDA_V164_T34_P52_ANTES.txt` y
`docs/loop/SALIDA_V164_T34_P52_DESPUES.txt`. **Las filas del registro siguen
siendo 154 y las citas con rastro de correccion siguen siendo 110.**

**NO SE DECLARA PARADA, Y CITO LA REGLA.** `AUDITOR.md` 4: *"Caida de CLASE o de
CIFRA PUBLICADA... Dos tandas seguidas: PARADA."* **La caida de clase es UNA**, y
la racha de cifra publicada esta en **CERO** por la decision del fundador del 3
sep 2026, medida y publicada por el propio auditor en la seccion 7 del acta 163.
**Quien cuenta la racha es el auditor y no yo**: lo que hago es declararla y
dejarla contable.

## 7. TAREA 5, LOS ARNESES PRE 148: **MEDIDOS, Y PARO AHI**

**ES UNA MEDICION, NO UNA OPERACION** (adjudicacion 6.9). La nomina se COMPUTA
importando el censo de la propia bateria: **92** arneses en `scripts/loop/`,
**53** en la nomina, **41 fuera y anteriores a la vuelta 148**. Corridos UNA vez
cada uno (`docs/loop/SALIDA_V164_T5_PRE148.txt`).

| medida | cifra |
|---|---:|
| medidos | **41** |
| dan `exit 0` | **30** |
| dan ROJO | **11** |
| de esos, `NO MORDIO` | **8** |
| de esos, `ANCLA PERDIDA` | **3** |
| tiempo total, segundos | **1.091,4** |
| tiempo total, minutos | **18,2** |
| mediana por arnes, segundos | **0,3** |

**NINGUNO ENTRA EN LA BATERIA, NINGUNO SE ARREGLA Y NO SE AFIRMA QUE LA REGLA DE
LA VUELTA 144 LES ALCANCE:** esa regla no dice si es retroactiva. **Con la cifra
delante se decide, y esa decision no es del ejecutor.**

**Y LA MEDICION ENSUCIO CINCO SALIDAS SELLADAS, LO DIGO YO ANTES QUE NADIE**
(`docs/loop/SALIDA_V164_T5_LIMPIEZA.txt`, con el diff dentro). Correr esos
arneses reescribe las salidas que ellos mismos escriben. **Medido y restaurado
con `git checkout` (P.16)**, y comprobado que `docs/loop/` queda sin ninguna
sellada modificada. **Y LO QUE EL DIFF ENSENA NO ES MENOR, aunque no se pedia:**
esas salidas de la vuelta 118 decian *aristas 0 de 9 PRESENTES* y hoy dicen *9 de
9*, y sus tablas pasan de `LISTA` a `HECHA`. **Su sujeto es el grafo vivo y
envejecen solas**, que es la enfermedad que la CORRECCION 22 curo. **Es dato para
quien decida si estos 41 entran o no.**

## 8. TAREA 6, EL ORDEN HASTA EL MURO, Y EL MURO ESTA DONDE DECIA

Medido hoy en `docs/loop/SALIDA_V164_T6_ORDEN_Y_MURO.txt`: el plan entero suma
**82** en su catalogo, **36** cumplidas y **46** sin cumplir, de ellas **44** SIN
VARA ESCRITA y **2** CON VARA QUE MIDE, las dos en `03_FUSIONES`. **La columna que muerde es la ultima**, no la
de "sin cumplir": esa incluye las que nadie ha escrito con que medir.

**LAS CINCO FASES QUE EL ENCARGO PIDE REPRODUCIR, TALLADAS UNA A UNA:**

| fase | catalogo | cumplidas | sin cumplir | fichero |
|---|---:|---:|---:|---|
| `02_DESTEJIDOS` | 9 | 2 | 7 | `docs/loop/SALIDA_V164_T7_FASE_02.txt` |
| `03_FUSIONES` | 16 | 12 | 4 | `docs/loop/SALIDA_V164_T7_FASE_03.txt` |
| `06_MESAS` | 16 | 16 | 0 | `docs/loop/SALIDA_V164_T7_FASE_06.txt` |
| `08_VERIFICACION` | 1 | 0 | 1 | `docs/loop/SALIDA_V164_T7_FASE_08.txt` |
| `09_LECTURAS_DIRIGIDAS` | 3 | 0 | 3 | `docs/loop/SALIDA_V164_T7_FASE_09.txt` |

**EL CALIBRADO SIGUE COMO EN LA 162 Y EN LA 163.** El recomputo final publica **4 aristas** rastreadas como distintas del grafo, las mismas cuatro de siempre (`docs/loop/SALIDA_V164_DESFASE_CALIBRADO_CIERRE.txt`), y ninguna de ellas mueve el estado de la `06_MESAS`, cuyo tallado de hoy dice `sin cumplir: 0` (`docs/loop/SALIDA_V164_T7_FASE_06.txt`).

**Identicas a lo que el acta 163 midio al abrir.** La `06_MESAS` es la unica sin
nada sin cumplir, y su fichero lo dice: `sin cumplir: 0`
(`docs/loop/SALIDA_V164_T7_FASE_06.txt`).

**LA FASE 08 NO CIERRA, Y LA QUE FALTA ES `OP-V-01`**
(`docs/loop/SALIDA_V164_T7_FASE_08.txt`, `sin cumplir: 1`). Su punto 9 es la
verificacion TRANSVERSAL, y tres de sus piezas necesitan credencial. **Medido hoy:
`.env` NO esta en el arbol y SI esta en `.gitignore:1`; `scripts/rumbos/prueba_rumbos.py`
sale `exit 2` con `ERROR: falta VOYAGE_API_KEY en .env`.** **SE PARA Y SE DICE:
no es un fallo del bucle, es su frontera** (acta 149, 3.10,
`docs/loop/ACTA_AUDITOR.md:50182`, leida hoy). **Hace falta una sesion con
credencial y con el fundador delante. EL MERGE NO SE PIDE NI SE HACE.**

**Y EL INSTRUMENTO DE LA 6 SE ARREGLA UN ESCALON MAS ARRIBA, EN LA FUENTE.** El
de la 163 ya leia el contraste de la salida sellada de la vuelta anterior en vez
de teclearlo, y **ese arreglo se hereda importandolo**. Lo que quedaba rancio era
**la RUTA de esa salida**, una constante con el numero de vuelta dentro. Ahora se
COMPUTA: se listan las `SALIDA_V<N>_*_ORDEN_Y_MURO.txt` que existen y se elige la
de mayor vuelta menor que la de hoy. **Y aqui importaba de verdad: la 163 NO dejo
salida**, asi que el contraste es contra la 162 y **el instrumento lo AVISA con
todas sus letras**. Las cuatro cifras del contraste dan **delta CERO**.

## 9. LOS DISCUTIBLES, MARCADOS ANTES DE SABER SI ACIERTO

  **DISCUTIBLE 1, EL MAS GORDO: SOSTENGO LA `D` DE LA `101` APOYANDOME EN QUE EL
  PASO 3 "SOLO NOMBRA", Y ESA LECTURA ES FINA.** El paso 3 no es solo un nombre:
  trae su objeto (*probar cada hipotesis*) y su modo (*con clientes reales*). Lo
  que digo es que **enumerar es lo que separo al `052` del `122`**, y el paso 3
  no enumera. **Pero si el auditor lee que "nombre de otro" significa el nombre A
  SECAS y no "el nombre mas su objeto", entonces el paso 3 pasa y la `101` es
  `C`.** Lo marco porque es exactamente la frontera de la vara congelada.

  **DISCUTIBLE 2: MUEVO LA `005` A `D` APOYANDOME EN QUE EL PASO 1 COLAPSA, Y ESE
  COLAPSO LO ESTABLECIO LA 157, NO YO HOY.** Si alguien sostuviera que el paso 1
  **si puede** estar en la expansion de la linea 2 (porque colapsar como PAR no
  es lo mismo que no poder ser TERMINO de una secuencia), entonces vuelven a ser
  tres pasos y la `C` de la 161 se sostiene. **No lo creo, y digo por que: un
  termino que repite la linea no aporta procedimiento aunque acompane a otros
  dos.** Pero es discutible y no lo escondo.

  **DISCUTIBLE 3: LA MEDICION DE SOLAPE LEXICO DE LA SECCION E DEL DOSSIER ES
  DEBIL Y LO DIGO EN EL PROPIO FICHERO.** El paso 1 **empata** con el paso 5 y la
  unica palabra comun es *fuera*. **No decide nada** y no la uso como decisor;
  esta ahi para que el colapso no se cite solo de memoria. Si el auditor cree que
  una medicion que empata no debe publicarse, lo acepto.

  **DISCUTIBLE 4: RESTAURE CON `git checkout` LAS CINCO SALIDAS QUE LA TAREA 5
  ENSUCIO, EN VEZ DE COMMITEARLAS.** Lo hice por P.16 y porque el registro de lo
  que paso vive en `SALIDA_V164_T5_LIMPIEZA.txt` con su `numstat` y su diff. **Un
  criterio contrario seria igual de defendible**: commitearlas y declararlas, que
  es lo que la 6.7 hizo con las tres de la 135. **Elegi restaurar porque esas
  cinco no son artefactos de esta vuelta: son de las 118, 135 y 137, y su
  contenido de hoy no prueba nada que el fichero de la medicion no diga mejor.**

  **DISCUTIBLE 5: METI LOS DOS ARNESES QUE NACEN HOY EN LA NOMINA DE LA BATERIA
  EL MISMO DIA QUE NACEN.** Es lo que la 144 y la 163 hicieron con los suyos y lo
  que la letra vigente permite (la condicion es sujeto congelado, no plazo).
  **Pero los meti ANTES de que ninguna vuelta ajena los hubiera corrido**, asi
  que su verde de hoy es el de su propio autor.

## 10. PREGUNTAS Y PENDIENTES DE DOCTRINA

  **PREGUNTA 1.** El campo `cita` en su forma unica solo guarda **la clase
  inmediatamente anterior**. La `LD-OPC05-005` ha ido `C -> D -> C -> D` y hoy su
  cita dice *"clase D [ANTES C, RECLASIFICADA EN LA VUELTA 164]"*, que es cierto
  pero **aplana una historia de cuatro tramos**. La historia entera si esta en la
  razon. **Se pregunta si la forma unica tiene que crecer o si esta bien asi.** No
  la toco por mi mano: la forma la fijo la adjudicacion 6.6 del acta 158.

  **PREGUNTA 2.** `node_modules/` del raiz sigue **sin versionar y sin ignorar**
  en `.gitignore`. La adjudicacion 6.12 del acta 162 lo dejo anotado y sin tocar,
  y esta vuelta hace lo mismo. **Se pregunta si sigue siendo alcance del fundador
  o si ya se puede ignorar**, porque un `git add -A` distraido lo commitea.

  **PENDIENTE DE DOCTRINA 1.** Los **41** arneses pre 148 estan medidos y **no hay
  regla que diga si la regla de entrada de la vuelta 144 es retroactiva**. La
  cifra esta: 30 en verde y 11 en rojo. **No invento la regla y no meto ninguno.**
  Queda para el auditor o para el fundador.

## 11. LO QUE NO HICE Y LO QUE DEJO ABIERTO

  - **Los cinco `sha256` de los assets** siguen sin recomputarse. Es la deuda mas
    vieja abierta y viene del acta 161. **No estaba en el encargo y no la toque.**
  - **Las lecturas dirigidas que nadie ha vuelto a mirar siguen sin releerse.** No
    doy el numero de memoria: el instrumento que lo mide es el contador de
    `P.5.2`, y su salida de hoy dice `CIFRA con NINGUNA: 30`
    (`docs/loop/SALIDA_V164_T34_P52_DESPUES.txt`). El acta 163 publico otra cifra
    con otro universo; **no la copio encima de la mia y no la resuelvo aqui**.
  - **`vuelta163_tarea1a_registrar_acta162.py` conserva los dos defectos que su
    heredero arreglo** (la negrita sin frontera y la cabecera partida). **No lo
    toco**: su entrada `R.32` esta escrita y verificada por el auditor, y
    re correrlo seria un no-op. **Queda declarado aqui para que no se herede.**
  - **La `LD-OPC05-101` queda en `D` y la `LD-OPC05-005` en `D`.** Ninguna otra
    clase se movio, y el motor lo comprueba: **CLASES MOVIDAS: 1**.

**Cero guiones largos y cero guiones medios. El hook corrio en los cinco commits
de esta vuelta y ninguno se salto.**
"""


def main():
    cab = cabecera_tallada()
    texto = CUERPO % {"CABECERA": cab}
    with io.open(REPORTE, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(texto)
    print("REPORTE.md escrito: %d lineas" % len(texto.split("\n")))
    print("cabecera pegada desde docs/loop/SALIDA_V164_T7_CABECERA.txt: %d lineas"
          % len(cab.rstrip().split("\n")))
    return 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    raise SystemExit(main())
