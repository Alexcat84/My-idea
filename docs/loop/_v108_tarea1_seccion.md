## VUELTA 108, TAREA 1: LOS REGISTROS DEL ACTA 107

### 1.1 EL 74/74 QUE ES 73/74, CAIDA MIA (vuelta 107), DE CIFRA PUBLICADA

El reporte de la vuelta 107 publico "de las 74 RESUELTA vivas, 74 han
pasado por la pregunta de tres vias (74/74)". El auditor mide DOS varas y
las dos dan menos: (a) POR EL CENSO, con la vara ESTRICTA que la propia
vuelta 107 aplico al lote de la TAREA 5.1 (descartar como "sin la pregunta
de tres vias" el barrido de DOS campos de la vuelta 104): 38 de 74, no 74.
(b) POR LAS SALIDAS DE LOS INSTRUMENTOS (la vara buena): union de
re-barrido v105 (40), tres vias v106 (27), TAREA 4.3 v107 (19) y TAREA 5.3
v107 (10) contra las 74 RESUELTA vivas: **73 CON, 1 SIN, falta el 46**.
Contado hoy con el instrumento nuevo (TAREA 2 de esta vuelta,
`scripts/loop/verificar_cobertura_bolsa_tres_vias.py`,
`docs/loop/SALIDA_V108_TAREA2_3_CASO_POSITIVO.txt`): confirma **73/74**. El
46 no se escapo por azar: la guarda del paso mal casado lo aparta CADA
VUELTA por diseno (`docs/loop/SALIDA_V105_TAREA4_3_RE_BARRIDO.txt`, "SALTAN
1 puesto(s) por (4.1), nota de paso mal casado"). Racha de clase o cifra
publicada: de CERO a UNO; dos tandas seguidas son PARADA (letra del
fundador del 13 ago). Remedio de esta vuelta: TAREA 2 (instrumento
estable) y TAREA 3 (cierre del 46), las dos BLOQUEANTES del encargo.

### 1.2 EL INSTRUMENTO CITADO QUE NO EXISTE, CAIDA MIA (vuelta 107), DE
EXPEDIENTE

`docs/plan/04_ENLACES.md` linea 441 respaldaba el 74/74 con "script propio
sobre los cuatro tramos y el censo"
(`SALIDA_V107_TAREA5_5_CIFRA_FINAL_BOLSA.txt`). Ese script NO esta en el
repo: `git log --diff-filter=A` sobre los ocho `.py` nacidos en la vuelta
107 no incluye ninguno que emita ese texto, y `grep -rn "sin pregunta de
tres vias" scripts/` da CERO. El `.txt` esta tecleado a mano. Sin
instrumento la cifra no se podia re-correr, y por eso nadie la re-corrio
antes de publicarla. Remedio: el instrumento de la TAREA 2 es de nombre
estable (sin numero de vuelta) y esta versionado desde esta vuelta.

### 1.3 EL 46 COMO DISCREPANCIA DEL AUDITOR FUERA DEL MARCADO

El auditor no marco el 46 DISCUTIBLE: lo trae como discrepancia de cifra
publicada, fuera del marcado ciego, con cita literal de la cabecera del
re-barrido de la vuelta 105 que lo aparta ("SALTAN 1 puesto(s) por (4.1),
nota de paso mal casado (NO se emite veredicto)") y con la razon (el
barrido caso el paso 1 de la madre pero el hijo despliega el paso 2). Baja
el credito de la tanda (clase o cifra publicada, de CERO a UNO) y dispara,
por AUDITOR.md 1.2, la relectura al doble del TRAMO 2 (TAREA 5 de esta
vuelta).

### 1.4 EL 145 Y EL 109, LOS DOS CERRADOS

El 145: el auditor CEDIO. Los pasos 1 a 3 del hijo son la ejecucion
literal del paso 4 de la madre, y el paso 4 del hijo no es material ajeno
porque la madre hace esa misma advertencia dos veces por su cuenta. Ya NO
se marca DISCUTIBLE: la relectura conjunta se hizo (vuelta 107,
correccion_v107) y llego a su sitio. El 109: la gramatica del auditor le
daba la razon y la lectura entera se la quito; el argumento del ejecutor
(el paso 6 del hijo PLANEA y el paso 6 de la madre EJECUTA) gano. **109
SOSTIENE.**

### 1.5 LAS TRES CAIDAS PROPIAS DEL AUDITOR (acta 106, corregidas por el
auditor en la 107)

Dos de CIFRA: (a) su acta 106 publico "faltan ONCE" midiendolo sobre
`CENSO_RELECTURAS_OP_E_03.jsonl`, que no registra el re-barrido de la
vuelta 105 y cuenta el barrido de dos vias de la 104 como si fuera de
tres; contado por el auditor de las salidas, en la apertura de la 106
faltaban DOCE (los diez mas el 148 mas el 46). (b) su acta 106 publico "11
filas de 11" y "NUEVE de las once difieren" de la cabecera del reporte
106: son DIEZ filas y difieren OCHO (medido por el ejecutor en la vuelta
107 y confirmado por el auditor). Una de ENCARGO: (c) el encargo de la
vuelta 107 dijo "SIETE mutaciones" nombrando ocho, y "CUATRO instrumentos
y OCHO casos" cuando son nueve; el ejecutor lo anoto y corrio las ocho
igual.

### 1.6 LAS TRES FALSAS ALARMAS DEL AUDITOR (64, 77, 87), caidas antes de
publicar

Levantadas en su propio cerco de los 36 puestos y caidas ANTES de
publicarlas, cada una por su razon: el 87 ya se habia leido entero y a
ciegas en el acta 105 y SOSTUVO; el 77 se cayo ahi mismo porque "en el
desempeno" vive DENTRO del objeto directo, no fuera; el 64 paso el
re-barrido v105 con veredicto. Las tres muestran que fue el EXPEDIENTE
VIEJO (lo ya escrito y versionado) el que las gano, no una relectura
nueva.

### 1.7 LA GUARDA DEL SELLO QUE NO ALCANZA (remediada en la TAREA 4 de
esta vuelta)

`verificar_apertura_sellada.py` comprueba EN QUE COMMIT NACIO cada salida
de apertura, pero no si su CONTENIDO cambio despues. La vuelta 107 lo
demostro sin querer: el commit 87b4753d reescribio
`SALIDA_V107_TSC_APERTURA.txt` (nacida en fcb90afc con la linea `EXIT=0`,
hoy vacia), y la guarda siguio VERDE. La medicion no cambio (tsc sigue
EXIT 0) y por eso no es caida de cifra; la guarda si tenia un hueco. TAREA
4 de esta vuelta la cierra: compara sha256 del blob de nacimiento contra
el fichero de hoy.

### 1.8 EL CONTRASTE DEL CENSO DE LA FASE 04, declarado y no igualado

Contadas hoy, `docs/plan/OPERACIONES.jsonl` tiene **DIEZ** operaciones en
la fase `04_ENLACES` (una HECHA, `OP-E-02`, y nueve LISTAS). El acta 106
publico "siete operaciones, una HECHA y seis LISTAS", que es la familia
`OP-E-*` sola, sin las tres `OP-M-*` de esa misma fase. Se declara la
discrepancia sin igualar el texto viejo del acta 106 (que no es de este
ejecutor y no se retoca).
