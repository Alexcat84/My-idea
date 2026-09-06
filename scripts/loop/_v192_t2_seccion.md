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
