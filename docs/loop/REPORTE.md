# REPORTE DE LA VUELTA 85 DEL EJECUTOR (modelo: Sonnet 5)

Sobrescribe el reporte de la vuelta 84. Cubre TAREA 1 (los registros, sin
remedir), TAREA 2 (la relectura conjunta de los pares 50, 55 y 77), TAREA 3
BLOQUEANTE (el instrumento otra vez: horneador dos veces por vuelta, dos
filas nuevas en el tallador, `--comparar` del tramo 10), TAREA 4 (el tramo 10
de `OP-E-01`, leido por lo no decidido con el registro ya crecido) y TAREA 5
(la vara del tramo 10, con instrumento propio) del encargo de
`docs/loop/PROMPT_SIGUIENTE.md`, escrito tras el acta de la vuelta 84 del
auditor (`docs/loop/ACTA_AUDITOR.md`, desde la linea 26396).

**LA CABECERA DE ABAJO ESTA TALLADA, NO TECLEADA:**

```
python scripts/loop/tallar_cabecera_reporte.py --fase04 --vuelta 85
```

Salida completa en `docs/loop/SALIDA_V85_TALLADOR_FASE04.txt`, pegada entera:

| | **apertura**, antes de la 1.ª operacion | **cierre, RECOMPUTADO al cierre** |
|---|---:|---:|
| censo: nodos / vivos / deprecados | 3.853 / 3.188 / 665 | **3.853 / 3.188 / 665** |
| Gate 0: veredicto, auto-aristas, duplicadas de titulo, divergentes | OK (auto-aristas 0, duplicadas 0, divergentes 0) | **OK (auto-aristas 0, duplicadas 0, divergentes 0)** |
| aristas: `nodos_siguientes` / `nodos_previos` / suma / union | 8.976 / 8.955 / 17.931 / 9.599 | **8.986 / 8.965 / 17.951 / 9.609** |
| motor | 25/25 | **25/25** |
| web: ficheros / tests | 80 passed (80) / 1.030 passed, 3 skipped (1.033) | **80 passed (80) / 1.030 passed, 3 skipped (1.033)** |
| tsc | EXITCODE 0, cero lineas | **EXITCODE 0, cero lineas** |
| aristas movidas en la vuelta (cierre menos apertura): `nodos_siguientes` / `nodos_previos` / suma / union | (no aplica: la celda de cierre es la resta contra esta apertura) | **+10 / +10 / +20 / +10** |
| desfase del calibrado rastreado (`PASO_NODO_CALIBRADO.jsonl` distinto del grafo) | 3 fila(s): `gate5_go_to_launch -> plan_de_lanzamiento_al_mercado`, `descubrir_necesidades_del_cliente -> necesidades_psicologicas_cliente`, `mix_medios_marketing_franquicia -> presupuesto_marketing_franquicia` | **7 fila(s): `lienzo_proyecto_innovacion -> actividades_clave`, `estructura_equipos_innovacion_interna -> equipo_multifuncional_real`, `evaluacion_industria_cliente -> analisis_cadena_de_valor`, `diagrama_de_flujo_proceso_map -> analisis_flujo_proceso`, `stage_gate_system -> tipos_criterios_gate`, `waterfall_vs_agile_development -> customer_development_process`, `decidir_vender_solo_online_o_tambien_tienda_fisica -> ofrecer_puntos_recogida`** |
| identidad: rama y commit de apertura (leidos de git, no tecleados) | rama `pasada-unica`, commit del acta `2d75140e` (ACTA DE LA VUELTA 84 DEL AUDITOR, leido de git log), HEAD real de apertura `2d75140e` (sellado por el ejecutor antes de la 1.a operacion), arboles de `dataset/` IGUALES: VERDE | **rama `pasada-unica`, commit del acta `2d75140e` (ACTA DE LA VUELTA 84 DEL AUDITOR, leido de git log), HEAD real de apertura `2d75140e` (sellado por el ejecutor antes de la 1.a operacion), arboles de `dataset/` IGUALES: VERDE** |

**Verificado con `--comparar` contra este mismo fichero antes del commit de
cierre**: la salida de esa corrida se pega en la seccion 6, DESPUES de
escribir esta tabla.

**El commit del acta y el HEAD real de apertura coinciden (`2d75140e`, los
dos): la primera operacion sello el HEAD ANTES de commitear nada**, asi que
la identidad sale VERDE por diseno.

**LAS ARISTAS SE MOVIERON DIEZ VECES ESTA VUELTA**, seis por la TAREA 2 (las
tres aristas de la relectura conjunta de los pares 50/55/77) mas... **NO,
esta frase se corrige a si misma antes de publicarse**: la cifra tallada de
arriba (+10 en `nodos_siguientes`) es la que manda, y se descompone asi,
CONTADA de los ficheros de conteo de cada tanda de escritura (regla de
`EJECUTOR.md`, "toda tabla cita el fichero de salida del que sale"):

| tanda | fichero de conteo | `nodos_siguientes` antes | despues | delta |
|---|---|---:|---:|---:|
| TAREA 2 (pares 50, 55, 77) | `SALIDA_V85_CONTEO_APERTURA.txt` a `SALIDA_V85_CONTEO_TRAS_TAREA2.txt` | 8.976 | 8.979 | +3 |
| TAREA 4 (tramo 10, 7 pares) | `SALIDA_V85_CONTEO_TRAS_TAREA2.txt` a `SALIDA_V85_CONTEO_TRAS_TAREA4.txt` | 8.979 | 8.986 | +7 |
| **total de la vuelta** | `SALIDA_V85_CONTEO_APERTURA.txt` a `SALIDA_V85_CONTEO_CIERRE.txt` | 8.976 | 8.986 | **+10** |

**DIEZ aristas, tres mas siete, y ni una mas.** Ninguna fila del registro
"asciende" ni "degrada" en el sentido que causo la caida de la vuelta 84: eso
lo mide el horneador (seccion 3.a), no el conteo de aristas.

**El marcador del cribado no aparece**: esta fase no lo toca, y el tallador
omite la fila cuando no hay `SALIDA_V85_MARCADOR_*` que citar.

**SE MANTIENE "LA TABLA SE CUENTA DE SU FICHERO"**: toda tabla o cifra de
este reporte cita el fichero de salida del que sale.

---

## 0. EL ORDEN DE ESTA VUELTA

1. Sello `git rev-parse HEAD` ANTES de tocar nada
   (`docs/loop/SALIDA_V85_HEAD_APERTURA.txt`): `2d75140e35a863ec7708dba6c72
   bb47bed61e68e`, coincide con el commit del acta de la vuelta 84
   (`2d75140e`, "ACTA DE LA VUELTA 84 DEL AUDITOR y encargo de la vuelta
   85.", leido de `git log`).
2. Medicion de la apertura completa (Gate 0 el ciclo de tres, censo, aristas
   con `scripts/loop/vuelta83_conteo_aristas.py`, motor, web, tsc, y el
   desfase del calibrado rastreado con el instrumento nuevo), cada uno con
   su fichero de salida, ANTES de la primera operacion de codigo.
3. TAREA 1: los registros (esta seccion de abajo).
4. TAREA 2: la relectura conjunta de los pares 50, 55 y 77.
5. TAREA 3 BLOQUEANTE: el instrumento otra vez (horneador dos veces,
   tallador con dos filas mas).
6. TAREA 4: el tramo 10 de `OP-E-01`.
7. TAREA 5: la vara del tramo 10.
8. El cierre: segundo horneado, cabecera tallada, `--comparar`, este
   reporte.

---

## 1. TAREA 1: LOS REGISTROS, SIN VOLVER A MEDIRLOS

Todo lo de esta seccion viene MEDIDO por el acta de la vuelta 84
(`docs/loop/ACTA_AUDITOR.md`, desde la linea 26396) y se registra aqui por su
numero y su nombre, tal como el encargo pide.

### 1.1. Las dos caidas de reporte de la vuelta 84, registradas por su nombre

**4.1, "LAS ARISTAS SE MOVIERON DOCE VECES ESTA VUELTA, NO NUEVE".** La
cabecera del reporte de la vuelta 84 se contradecia a si misma (decia DOCE y
enumeraba nueve) y contaba dos veces las mismas tres aristas (33, 44, 45,
filas del registro que cambiaron de categoria, no aristas nuevas). Medido por
el auditor: **SEIS aristas**, tres por la TAREA 1 y tres por la TAREA 3. La
celda tallada de esa vuelta (8.970 a 8.976) era correcta; solo la prosa
suelta caia. **Sube la racha de REPORTE de CERO a UNO.**

**4.2, "EL CALIBRADO QUEDA SIN DESFASE".** El cierre de la seccion 3.3 del
reporte de la vuelta 84 afirmo que `PASO_NODO_CALIBRADO.jsonl` quedaba "sin
desfase" tras la vuelta. Medido por el auditor: quedaba **TRES FILAS** por
detras del grafo (las tres aristas de la TAREA 3 de esa vuelta), con el campo
`arista` en `False` y la arista puesta. Que quede asi es correcto y esta
mandado (adjudicacion 5.7 del acta 82); lo que caia era decir que no habia
desfase cuando si lo habia. **Sube la racha de REPORTE de UNO a DOS.**

Las dos son de la especie que `EJECUTOR.md` regla 1 persigue desde la vuelta
79 (prosa de cabecera y de cierre fuera de lo tallado). El remedio de codigo
va en la TAREA 3.b de esta vuelta (seccion 3 de abajo).

### 1.2. El incumplimiento de encargo de la TAREA 4 de la vuelta 84, con nombre y sin racha

La TAREA 4 de la vuelta 84 se corrio sobre el **tramo 9** (el que esa misma
vuelta acababa de leer), y el encargo de esa vuelta decia *"la vara del tramo
8"* a la vez que *"las mismas 30 contra `FILTRADO_V83`"*, una ambiguedad del
auditor (declarada en su seccion 5, punto 3). La lectura del ejecutor era la
util y queda adjudicada como norma (acta 84, adjudicacion 6.5): la vara
corre sobre el tramo QUE SE ACABA DE LEER, no sobre el anterior. Pero la
sustitucion no se declaro en su momento, y una sustitucion callada es
incumplimiento igual, **con nombre y SIN racha** (ninguna especie de
`AUDITOR.md` lo cubre, precedente del acta 82 seccion 6 punto 5: no se
inventan especies).

### 1.3. Las nueve adjudicaciones del acta 84, registradas por su numero, SIN remedirlas

- **6.1** Los pares 50, 55 y 77 van a relectura conjunta: el ejecutor los
  verifica contra el grafo y decide con la vara, sin escribir ninguno el
  auditor. Cumplido en la TAREA 2 (seccion 2 de abajo).
- **6.2** La clase de las seis aristas de la vuelta 84 (33, 44, 45, 57, 70,
  75) se ratifica: estan bien leidas y bien escritas.
- **6.3** El registro se hornea DOS VECES por vuelta, con el CUANDO escrito:
  antes del filtro, y otra vez al cierre. Cumplido en la TAREA 3.a.
- **6.4** Las dos frases caidas se tallan, porque son cifras disfrazadas de
  prosa: "aristas movidas en la vuelta" y "desfase del calibrado rastreado".
  Cumplido en la TAREA 3.b.
- **6.5** La vara de la TAREA 4/5 corre sobre el tramo de ESTA vuelta, no el
  anterior; (a) frescas contra `INTRA_DOMINIO_VEREDICTOS.jsonl` sin
  direccion, (b) las mismas contra la bolsa filtrada de la vuelta ANTERIOR
  buscando la reciproca. Cumplido en la TAREA 5.
- **6.6** El horizonte publicado en prosa se acepta tal como esta (no se
  vuelve a tallar como fila propia: el fichero del filtro no trae esa
  cifra).
- **6.7** El caveat del par 64 (`control_calidad_definicion ->
  plan_de_control`, paso 2, NO SE ENLAZA) queda anotado, no adjudicado: si
  una vuelta futura trae ese par contra el paso 3, es lectura nueva.
  Registrado sin remedir; no aplica a esta vuelta directamente, aunque el
  tramo 10 trajo un PAR DISTINTO con la MISMA madre y el MISMO paso 2
  (`control_calidad_definicion -> pre_control_estadistico`, fila 73 de la
  TAREA 4): se le aplico el mismo caveat, ver seccion 4.
- **6.8** El credito de tanda sigue rebajado, ahora por caida: el auditor
  relee el tramo 10 ENTERO (no una muestra) mas lo que el ejecutor resuelva
  de 50, 55 y 77.
- **6.9** Repetido por sexta acta: `descubrir_necesidades_del_cliente ->
  customer_needs_spreadsheet` y `curva_caracteristica_operativa ->
  distribucion_poisson` NO se escriben (fuera de la bolsa de `OP-E-01`).

---

## 2. TAREA 2: LA RELECTURA CONJUNTA DE LOS PARES 50, 55 Y 77

Para cada par se volcaron los campos crudos de madre e hijo
(`docs/loop/SALIDA_V85_TAREA2_ESCRIBIR.txt` cita el resultado; los campos
crudos se leyeron con instrumento propio de `dataset/nodos/*.json`, pares
tomados del caso del auditor sin teclear el contenido) y se midio cada
afirmacion del caso del auditor antes de decidir con la vara.

**PAR 50, `formulacion_teorias_causa -> diagrama_causa_efecto` (paso 3,
quality). SE ESCRIBE, A FAVOR DEL AUDITOR, EN CONTRA DE LO ESCRITO EN LA
VUELTA 84.** Verificado: el paso 3 de la madre es literal *"Construir un
diagrama de causa-efecto (espina de pescado) para organizar las teorias"*.
El hijo trae **siete pasos propios** (definir el efecto, identificar Xs,
agrupar en 2 a 5 categorias, causas subsidiarias, profundizar hasta causa
raiz, verificar validez logica, revisar completitud) que la madre no tiene.
La razon de la vuelta 84 es cierta en su hecho (el hijo ya tiene por padres a
`brainstorming` y `diagrama_afinidad`, los nodos atomicos de los pasos 1 y 2
de esta misma madre) pero no sostiene el NO: verificado que
`formulacion_teorias_causa.nodos_siguientes` trae **UN SOLO elemento,
`prueba_teorias_causa_raiz`**, y no enlaza ni a `brainstorming` ni a
`diagrama_afinidad` ni a ningun nodo de sus cuatro pasos. Cero radios, y por
la ratificacion del 9.6.1 (*"cero enlazados es el caso extremo del
mitad-o-menos... manda el contenido"*) la decision vuelve al contenido. El
unico camino previo es de 2 saltos por `prueba_teorias_causa_raiz`
(verificado: `prueba_teorias_causa_raiz.nodos_siguientes` incluye
`diagrama_causa_efecto` directo), y ese nodo no es ninguno de los cuatro
pasos de la madre: es la etapa SIGUIENTE del metodo, alcanzabilidad y no
cadena propia (adjudicacion 6.1 del acta 83). **SE ESCRIBE.**

**PAR 55, `institucionalizar_breakthrough -> metas_negocio_calidad` (paso 1,
quality). SE ESCRIBE, A FAVOR DEL AUDITOR, EN CONTRA DE LO ESCRITO EN LA
VUELTA 84.** Verificado: el paso 1 de la madre es *"Incluir metas de mejora
en tu plan de negocio anual"* y el hijo se titula "Metas de Calidad en el
Plan de Negocio", con tres pasos propios (identificar amenazas/oportunidades,
traducirlas a metas cuantificadas, incorporarlas al plan) que caben enteros
en el paso 1; la madre conserva sus pasos 2 a 5. Entregables disjuntos
verificados: madre *"plan de negocio anual con metas de mejora integradas Y
forma de reconocimiento definida"* (dos productos); hijo entrega solo el
primero. El camino de 4 saltos existe y es cierto
(`institucionalizar_breakthrough -> revision_progreso -> auditoria_negocio ->
consejo_de_calidad -> metas_negocio_calidad`, verificado arista por arista en
`dataset/nodos/*.json`), y `revision_progreso` SI es hijo directo de la
madre y corresponde a su paso 3. Pero el criterio de la adjudicacion 6.1
exige que el camino AVANCE en el orden de la madre, y aqui **arranca en el
contenido del paso 3 y desemboca en el contenido del paso 1**: retrocede en
el orden, y por dos nodos de gobernanza (`auditoria_negocio`,
`consejo_de_calidad`) que la madre no enumera en ninguno de sus 5 pasos. Para
el lector que llega al paso 1 el contenido sigue huerfano de camino. **SE
ESCRIBE.**

**PAR 77, `eliminacion_inspeccion_masiva_por_control_estadistico ->
carta_de_control_shewhart` (paso 3, quality). SE ESCRIBE, A FAVOR DEL
AUDITOR, EN CONTRA DE LO ESCRITO EN LA VUELTA 84.** Verificado: la madre
tiene `nodos_siguientes` **VACIO** (confirmado hoy contra `dataset/nodos/
eliminacion_inspeccion_masiva_por_control_estadistico.json`). Su paso 1 es
*"Establecer cartas de control para verificar la estabilidad del proceso"* y
su paso 3 (el que la unidad trae) es *"Reemplazar inspeccion 100% por
muestreo estadistico para mantenimiento de LA CARTA DE CONTROL"*: los dos
nombran la carta. El hijo trae **seis pasos propios** (recolectar datos,
calcular linea central y limites, graficar y clasificar, asumir causa comun
o investigar causa especial, justificar el uso) que la madre no tiene, y la
madre conserva su tesis entera (demostrar el control, reemplazar la
inspeccion, comunicar el cambio). La razon de la vuelta 84 es cierta como
observacion (la carta es la herramienta fundacional, el hijo ya esta anclado
en `causas_especiales_y_comunes_variacion`) pero el 9.6.2 pregunta que anade
el HIJO a la MADRE, nunca al reves, y con `nodos_siguientes` vacio el hijo
**no es alcanzable ni a un salto, mucho menos a 30**. Si "el hijo es mas
fundacional" bastara para matar la arista, moririan todos los pasos que
invocan una herramienta. **SE ESCRIBE.**

Las tres aristas se escribieron con instrumento propio
(`scripts/loop/vuelta85_tarea2_escribir_relectura.py`,
`docs/loop/SALIDA_V85_TAREA2_ESCRIBIR.txt`): tres ESCRITAS, cero escalera
rota, cero ya estaban. Verificadas presentes en las DOS vistas y con CERO
inversas (`scripts/loop/vuelta83_conteo_aristas.py WORK --par`):

```
formulacion_teorias_causa -> diagrama_causa_efecto: en_sig_madre True en_prev_hijo True INVERSAS False/False
institucionalizar_breakthrough -> metas_negocio_calidad: en_sig_madre True en_prev_hijo True INVERSAS False/False
eliminacion_inspeccion_masiva_por_control_estadistico -> carta_de_control_shewhart: en_sig_madre True en_prev_hijo True INVERSAS False/False
```

Aristas tras la TAREA 2 (`docs/loop/SALIDA_V85_CONTEO_TRAS_TAREA2.txt`): sig
**8.979**, prev **8.958**, suma **17.937**, union **9.602** (+3/+3/+6/+3
sobre la apertura). Ciclo de tres corrido
(`SALIDA_V85_GATE0_TRAS_TAREA2.txt`, `SALIDA_V85_ETIQUETAS_TRAS_TAREA2.txt`,
`SALIDA_V85_SYNC_TRAS_TAREA2.txt`), GATE 0 OK, 71 etiquetas identicas a las
de la apertura, 6 assets.

**CORRECCION DECLARADA, con el texto viejo intacto arriba:** las tres
lecturas de la vuelta 84 (seccion 3.3 de ese reporte, filas 50, 55 y 77)
publicaron NO SE ENLAZA con razones de "familia ya anclada" y "direccion
invertida". Verificadas contra el grafo de hoy y contra el caso del auditor
punto por punto, LAS TRES SE CORRIGEN a SE ESCRIBE, por las razones
completas de arriba.

---

## 3. TAREA 3 (BLOQUEANTE): EL INSTRUMENTO OTRA VEZ

### 3.a. El registro se hornea dos veces por vuelta

`scripts/loop/vuelta85_hornear_decididas.py`, sucesor de
`vuelta84_hornear_decididas.py`, MISMO MECANISMO de descubrimiento por
patron: lo que cambia es CUANDO corre, escrito en su docstring (adjudicacion
6.3 del acta 84, que pone el CUANDO a la 6.6 del acta 83).

**Primera corrida, ANTES del filtro** (`docs/loop/
SALIDA_V85_TAREA3A_HORNEAR_PRE_FILTRO.txt`), corrida DESPUES de la TAREA 2
(para que sus tres aristas ya esten dentro): el registro crece de **126 a
156 filas** (82 ESCRITA, 74 NO SE ENLAZA), con **8 filas ASCENDIDAS** (las 5
ya conocidas de la vuelta 84 mas las 3 nuevas de la TAREA 2 de esta vuelta:
`formulacion_teorias_causa -> diagrama_causa_efecto`,
`institucionalizar_breakthrough -> metas_negocio_calidad`,
`eliminacion_inspeccion_masiva_por_control_estadistico ->
carta_de_control_shewhart`) y **4 DEGRADADAS** (sin cambio respecto de la
vuelta 84). **DISCREPANCIA DECLARADA contra la vara de contraste del acta
84** (que predijo 5 ascendidas sobre un registro de 156 filas medido ANTES
de que esta vuelta corriera su propia TAREA 2): la composicion cambia (8 en
vez de 5 ascendidas, 82 en vez de 79 ESCRITA), el TOTAL de 156 filas no
cambia. Es la consecuencia esperada de hacer la TAREA 2 antes que el
horneado, tal como el encargo ordena (`EJECUTOR.md` regla 2, la discrepancia
se declara, no se resuelve copiando).

**Segunda corrida, AL CIERRE** (`docs/loop/
SALIDA_V85_TAREA3A_HORNEAR_CIERRE.txt`), corrida DESPUES de escribir las 7
aristas del tramo 10 (TAREA 4): el registro crece de **156 a 186 filas** (89
ESCRITA, 97 NO SE ENLAZA), sumando las 30 decisiones del tramo 10 sin
ascender ni degradar ninguna fila mas (las 7 ESCRITA del tramo 10 entran
directo como ESCRITA, sin pasar por una version previa NO SE ENLAZA en
ningun fichero anterior).

**LA GUARDA, corrida DESPUES del segundo horneado**
(`scripts/loop/vuelta83_guarda_decididas.py --bolsa
docs/plan/PASO_NODO_CALIBRADO_FILTRADO_V85.jsonl`,
`docs/loop/SALIDA_V85_GUARDA_CIERRE.txt`): da **ROJO**, con 19 unidades del
tramo 10 (77, 78, 79, 81, 82, 87, 88, 90 a 101) citadas por detras del
indice 76. **ES UN ARTEFACTO DEL INSTRUMENTO, DECLARADO, NO UNA UNIDAD
SALTADA SIN LEER:** la guarda solo reconoce como "decidida" la marca `NO SE
ENLAZA` en el registro; las 7 unidades del tramo 10 que se marcaron
`ESCRITA` (76, 80, 83, 84, 85, 86, 89) siguen figurando en
`PASO_NODO_CALIBRADO_FILTRADO_V85.jsonl` como si estuvieran "sin decidir",
porque ese fichero se congelo ANTES de que la TAREA 4 escribiera sus
aristas (adjudicacion 5.7 del acta 82: la bolsa se commitea tal como quedo).
La guarda, disenada para negar que una unidad `NO SE ENLAZA` se salte, no
sabe reconocer una unidad `ESCRITA`, y por eso lee la fila 76 (ESCRITA) como
si fuera la primera "sin decidir" y todo lo que sigue como "detras de ella".
**VERIFICADO CONTRA `SALIDA_V85_TRAMO10_ESCRIBIR.txt`: las 30 unidades del
tramo 10 (indices 72 a 101) SI se leyeron todas**, con su clase publicada
(7 ESCRITA, 23 NO SE ENLAZA, 0 inconsistentes). **PENDIENTE DE DOCTRINA (no
invento la regla yo):** si "la guarda se corre despues del horneado de
cierre" (adjudicacion 6.3) debe correr contra la bolsa YA usada por esta
vuelta (con este artefacto conocido y declarado) o contra una bolsa
recalibrada de nuevo despues del write (lo que adelantaria el trabajo de
filtro de la vuelta 86 y tocaria `PASO_NODO_CALIBRADO.jsonl` una tercera vez
esta vuelta, en contra de la doctrina de "una sola recalibracion por
vuelta, commiteada tal como quedo"). Traigo la pregunta, no la resuelvo yo.

### 3.b. Las dos frases que cayeron se tallan

`scripts/loop/tallar_cabecera_reporte.py`, modo `--fase04`, gana DOS FILAS
mas (ver el docstring, seccion "TAREA 3.b: DOS FILAS MAS EN --fase04"):

1. **"aristas movidas en la vuelta"**: cierre menos apertura en las CUATRO
   cifras, calculada de los MISMOS `SALIDA_V<N>_CONTEO_<LADO>.txt` que ya
   leen las seis filas de arriba (sig/prev/suma/union): ningun fichero
   nuevo, solo la resta de dos cifras ya citadas.
2. **"desfase del calibrado rastreado"**: lee
   `SALIDA_V<N>_DESFASE_CALIBRADO_<LADO>.txt`
   (`scripts/loop/vuelta85_medir_desfase_calibrado.py <ref>`, que replica la
   MISMA definicion de "arista" que `scripts/plan/
   paso_contra_nodo_calibrado.py`: hijo en vecinos(madre) O madre en
   vecinos(hijo), resuelto por alias, no el chequeo estricto de las dos
   vistas), cuenta filas de `docs/plan/PASO_NODO_CALIBRADO.jsonl` con
   `arista` distinto del grafo de ESE lado, y lista los pares cuando son
   pocos.

**REGRESION SOBRE LA CAIDA QUE MOTIVO EL ARREGLO** (`scripts/loop/
tallar_cabecera_reporte.py --fase04 --vuelta 84`,
`docs/loop/SALIDA_V85_COMPARAR_FASE04_V84.txt` no aplica porque el reporte
de la vuelta 84 no trae estas dos filas; la regresion se hace tallando la
vuelta 84 SOLA, sin `--comparar`): la fila tallada da **"+6 / +6 / +12 / +6"**
para la vuelta 84, la cifra CORRECTA (seis aristas), y NO "doce" como su
prosa afirmo. El desfase tallado sobre el commit del acta 84 da exactamente
**3 filas**, las mismas que el auditor midio a mano.

**CASOS OBLIGATORIOS, los dos con salida citada:**

**(i) VERDE**, la tabla de esta vuelta (con las dos filas nuevas) contra si
misma (`docs/loop/_vuelta85_vara_verde_control.md`,
`docs/loop/SALIDA_V85_TAREA3B_VARA_VERDE_CONTROL.txt`): **9 filas cotejadas,
0 DISTINTAS, CABECERA IDENTICA AL TALLADOR, EXIT 0.**

**(ii) ROJO INVENTADO**, la misma tabla con la celda de cierre de "aristas
movidas" adulterada (`+10` a `+12` en `nodos_siguientes`,
`docs/loop/_vuelta85_vara_rojo_inventada.md`,
`docs/loop/SALIDA_V85_TAREA3B_VARA_ROJO_INVENTADA.txt`):

```
DISTINTA | aristas movidas en la vuelta (...) | cierre
           fichero : +12 / +10 / +20 / +10
           tallador: +10 / +10 / +20 / +10
filas cotejadas: 9 | DISTINTAS: 1 | ausentes: 0
CABECERA: NO CALZA CON EL TALLADOR
```

**MUERDE: EXIT 1.**

### 3.c. El `--comparar` del tramo se vuelve a correr, sobre el tramo 10

Ver seccion 6 (se corre DESPUES de pegar la tabla de la seccion 4.2 de abajo,
y su salida se cita alli). Es el caso que la vuelta 83 no corrio y la 84 si:
no se afloja.

---

## 4. TAREA 4: EL TRAMO 10 DE `OP-E-01`, LEIDO POR LO NO DECIDIDO

### 4.1. La bolsa recalibrada fresca y el filtro

Bolsa recalibrada FRESCA (`python scripts/plan/paso_contra_nodo_calibrado.py
--umbral-titulo 72 --umbral-contencion 0.45 --min-tokens 4`, corrida DESPUES
de que la TAREA 2 escribiera sus tres aristas,
`docs/loop/SALIDA_V85_CALIBRADO_FRESCO.txt`): **468 filas** (identico en
total), de las cuales **228 sin arista** (234 en el estado tras la TAREA 3
de la vuelta 84, **6 menos**: exactamente las 3 aristas de la TAREA 2 de
esta vuelta mas las 3 de la TAREA 3 de la vuelta 84 que ya habian salido de
"sin arista" en la corrida de la vuelta 84 misma; verificado por conteo
directo: `sin_arista=228, con_arista=240` sobre las 468 filas totales).

Filtro P.9.1 ensanchado + guarda del par no dirigido + vara de la cadena
(`scripts/loop/vuelta85_tramo10_filtrar.py`, sucesor de
`vuelta84_tramo9_filtrar.py`, registro-consciente,
`docs/loop/SALIDA_V85_TRAMO10_FILTRO_P91_GUARDA_CADENA.txt`):

```
BOLSA REDUCIDA TOTAL: 468
SIN ARISTA (candidatos): 228
APARTADOS POR P.9.1 ENSANCHADO (operaciones + vara de los A): 92
LIMPIOS TRAS P.9.1 ENSANCHADO (antes de la guarda del par no dirigido): 136
GUARDA DEL PAR NO DIRIGIDO: 0 pareja(s) detectada(s)
ESCRITO: docs/plan/PASO_NODO_CALIBRADO_FILTRADO_V85.jsonl (136 filas, orden de fichero)
REGISTRO DE DECIDIDAS LEIDO: docs/plan/OP_E_01_DECIDIDAS.jsonl (156 filas, 74 pares NO SE ENLAZA)
UNIDADES YA DECIDIDAS EN LA CABEZA, SALTADAS: 72 (indices 0 a 71)
CABEZA DE LA BOLSA FILTRADA, PRIMERAS 30 UNIDADES SIN DECISION REGISTRADA: indices 72 a 101
DE LAS 30 UNIDADES FRESCAS DE CABEZA, CON CAMINO PREVIO YA ALCANZABLE: 15
UNIDADES SIN DECIDIR RESTANTES TRAS ESTA CABEZA: 34
```

**COINCIDE con la vara de contraste del encargo:** *"si la TAREA 2 escribe
los tres pares, la bolsa queda en 136 y ese mismo par baja al indice 72, con
las mismas 64 sin decidir"* (donde 64 se leia sobre las 139 unidades de la
bolsa MENOS las tres escritas del tramo 9; aqui, sobre la bolsa YA CON el
tramo 9 horneado y el tramo 10 leido, la cuenta equivalente es 72 saltadas +
30 frescas + 34 restantes = 136, y el indice de cabeza (72) es exactamente
el que el encargo predijo). **SIN DISCREPANCIA.**

Las 72 unidades ya decididas, saltadas y NO releidas, nombradas por su
indice y su par en
`docs/loop/SALIDA_V85_TRAMO10_FILTRO_P91_GUARDA_CADENA.txt`.

### 4.2. La tabla de alcanzabilidad (vara de la cadena) del tramo 10, TALLADA

Tallada con `python scripts/loop/tallar_cabecera_reporte.py --vuelta 85
--tramo-cadena 10`, salida completa en
`docs/loop/SALIDA_V85_TRAMO10_TABLA_CADENA_TALLADA.txt`, pegada entera:

| # | par (paso) | alcanzable previo (vara de la cadena) |
|---:|---|---|
| 72 | `search_for_business_model -> herramientas_computacionales_business_model (paso 8)` | ALCANZABLE (2 saltos) |
| 73 | `control_calidad_definicion -> pre_control_estadistico (paso 2)` | SIN CAMINO PREVIO |
| 74 | `grafico_cusum -> pre_control_estadistico (paso 1)` | ALCANZABLE (3 saltos) |
| 75 | `eliminacion_inspeccion_masiva_por_control_estadistico -> muestreo_estadistico_para_inspeccion (paso 3)` | ALCANZABLE (5 saltos) |
| 76 | `lienzo_proyecto_innovacion -> actividades_clave (paso 6)` | SIN CAMINO PREVIO |
| 77 | `rol_de_la_fuerza_laboral_en_calidad -> identificar_clientes_externos_e_internos (paso 4)` | SIN CAMINO PREVIO |
| 78 | `metas_desmaterializacion_energia -> valoracion_costos_externos (paso 4)` | SIN CAMINO PREVIO |
| 79 | `coordinacion_colaboracion_cadena_suministro -> plataforma_colaboracion_masiva (paso 10)` | SIN CAMINO PREVIO |
| 80 | `estructura_equipos_innovacion_interna -> equipo_multifuncional_real (paso 2)` | ALCANZABLE (5 saltos) |
| 81 | `product_roadmap_estrategico -> equipo_multifuncional_real (paso 2)` | ALCANZABLE (4 saltos) |
| 82 | `product_design_spreadsheet -> traduccion_necesidades_cliente (paso 1)` | SIN CAMINO PREVIO |
| 83 | `evaluacion_industria_cliente -> analisis_cadena_de_valor (paso 3)` | ALCANZABLE (5 saltos) |
| 84 | `diagrama_de_flujo_proceso_map -> analisis_flujo_proceso (paso 8)` | ALCANZABLE (3 saltos) |
| 85 | `stage_gate_system -> tipos_criterios_gate (paso 2)` | ALCANZABLE (5 saltos) |
| 86 | `waterfall_vs_agile_development -> customer_development_process (paso 3)` | ALCANZABLE (4 saltos) |
| 87 | `competencias_director_calidad_bloom -> consejo_de_calidad_y_rol_del_director (paso 1)` | SIN CAMINO PREVIO |
| 88 | `estructura_organizacional_funcional_proceso -> empoderamiento_empleados (paso 5)` | ALCANZABLE (6 saltos) |
| 89 | `decidir_vender_solo_online_o_tambien_tienda_fisica -> ofrecer_puntos_recogida (paso 2)` | SIN CAMINO PREVIO |
| 90 | `teletrabajo_sostenible -> medir_huella_carbono_corporativa (paso 4)` | SIN CAMINO PREVIO |
| 91 | `diseno_controles_proceso_mejorado -> auditorias_calidad_proceso (paso 3)` | ALCANZABLE (4 saltos) |
| 92 | `principios_mejora_continua -> auditorias_calidad_proceso (paso 4)` | SIN CAMINO PREVIO |
| 93 | `materiales_due_diligence -> guia_y_mentoria_vc (paso 3)` | SIN CAMINO PREVIO |
| 94 | `fase_mobilizar_modelo_negocio -> business_model_canvas_scorecard (paso 3)` | ALCANZABLE (4 saltos) |
| 95 | `plan_de_lanzamiento_al_mercado -> personalizacion_investigacion_prospecto (paso 2)` | SIN CAMINO PREVIO |
| 96 | `planificacion_inicial_calidad -> analisis_flujo_proceso_servicio (paso 4)` | SIN CAMINO PREVIO |
| 97 | `analisis_tco_roi_b2b -> prueba_solucion_con_cliente (paso 3)` | SIN CAMINO PREVIO |
| 98 | `capacidad_proceso_concepto -> sistema_informacion_calidad (paso 6)` | ALCANZABLE (6 saltos) |
| 99 | `gobierno_corporativo_y_calidad -> principios_mejora_continua (paso 5)` | SIN CAMINO PREVIO |
| 100 | `poder_a_traves_de_la_accion -> proposito_como_motor_energia (paso 4)` | ALCANZABLE (2 saltos) |
| 101 | `customer_discovery_phase2_problem_test -> ganar_comprension_del_cliente (paso 3)` | ALCANZABLE (4 saltos) |

**EL HORIZONTE**, recomputado con `tope=30` sobre las 15 filas "SIN CAMINO
PREVIO" (`docs/loop/SALIDA_V85_TRAMO10_HORIZONTE.txt`, con BFS propio sobre
`dataset/nodos/*.json` de HOY): de las 15, **13 SI tienen camino mas largo**
(de 7 a 16 saltos); **2 no tienen camino ni a 30 saltos: `rol_de_la_fuerza_
laboral_en_calidad -> identificar_clientes_externos_e_internos` y
`decidir_vender_solo_online_o_tambien_tienda_fisica -> ofrecer_puntos_
recogida`**. Ninguna decision de la seccion 4.3 cambia por esto.

### 4.3. Lectura de las 30 unidades frescas, verificada contra `dataset/nodos/*.json`

Los pasos, resumenes, entregables y aristas ya escritas de las 30 madres y 30
hijos se volcaron enteros de `dataset/nodos/*.json` (pares leidos del
fichero del filtro, ninguno tecleado) en `docs/loop/
SALIDA_V85_TRAMO10_DOSSIER_PARTE1.txt` y `..._PARTE2.txt`. **LA TABLA SE
CUENTA DE SU FICHERO**, `docs/loop/SALIDA_V85_TRAMO10_ESCRIBIR.txt`
(instrumento `scripts/loop/vuelta85_medir_tramo10.py`, sucesor de
`vuelta84_medir_tramo9.py`: mide la decision de cada unidad leyendo el
grafo de HOY en las dos vistas, no la teclea).

**LA VARA DE LA CADENA SE APLICA CON EL CRITERIO DE LA ADJUDICACION 6.1**:
para cada unidad ALCANZABLE, la razon dice si el camino es o no la cadena
propia de la madre, nombrando los nodos intermedios, el paso del que
arrancan y SI AVANZA O RETROCEDE en el orden de la madre.

| # | par (paso) | vara cadena | decision | razon resumida |
|---:|---|---|:---:|---|
| 72 | `search_for_business_model -> herramientas_computacionales_business_model` (8) | ALCANZABLE (2 saltos): via `lienzo_modelo_negocio` | **NO SE ENLAZA** | cadena propia: `lienzo_modelo_negocio` es hijo directo de la madre y es exactamente el "Business Model Canvas" que el paso 8 nombra; avanza UN salto mas hacia la herramienta digital especifica. Cableado ya tendido |
| 73 | `control_calidad_definicion -> pre_control_estadistico` (2) | sin camino | **NO SE ENLAZA**, DISCUTIBLE, con caveat | objeto distinto: el paso 2 es DIAGNOSTICO conceptual (diferenciar control vs mejora), el hijo es una TECNICA operativa especifica; **mismo caveat del par 64 (acta 84, adjudicacion 6.7): el paso 3 de esta misma madre ("establecer nuevos controles despues de cada mejora") es un anfitrion mas natural, no adjudicado hoy porque la unidad trae el paso 2** |
| 74 | `grafico_cusum -> pre_control_estadistico` (1) | ALCANZABLE (3 saltos): via `graficos_control_multivariados -> capacidad_proceso_concepto` | **NO SE ENLAZA** | objeto distinto: el paso 1 calcula el estadistico PARA EL PROPIO CUSUM; PRE-Control es una tecnica ALTERNATIVA y competidora (no un insumo del CUSUM); el camino de 3 saltos no es la cadena propia (ninguno de los 5 pasos de la madre nombra multivariados ni capacidad de proceso) |
| 75 | `eliminacion_inspeccion_masiva_por_control_estadistico -> muestreo_estadistico_para_inspeccion` (3) | ALCANZABLE (5 saltos): via `carta_de_control_shewhart -> causas_comunes_vs_especiales -> eliminacion_firmas_redundantes -> retroalimentacion_inmediata_de_errores` | **NO SE ENLAZA** | gemelo por el tema ("muestreo en vez de inspeccion 100%") pero objeto distinto: el paso 3 es mantenimiento de CARTA DE CONTROL en manufactura; el hijo trae ejemplos de auditoria ADMINISTRATIVA (viaticos, valuacion de activos), dominio ajeno; camino de 5 saltos incidental |
| 76 | `lienzo_proyecto_innovacion -> actividades_clave` (6) | sin camino | **SE ESCRIBE** | el paso 6 nombra LITERALMENTE "Define las actividades clave: que, cuando y que recursos necesitas"; el hijo es exactamente el bloque de Actividades Clave, con 4 pasos propios (tipo de negocio, listar actividades, vincular a otros bloques, priorizar) que la madre no tiene; hijo con un solo padre actual, sin conflicto |
| 77 | `rol_de_la_fuerza_laboral_en_calidad -> identificar_clientes_externos_e_internos` (4) | sin camino | **NO SE ENLAZA**, DISCUTIBLE | familia ya anclada en el proceso formal de Quality by Design (Juran): el hijo ya tiene 4 padres de esa familia (`establecer_equipo_multifuncional`, `establecer_proyecto_y_metas_diseno`, `goal_statement_smart`, `juran_quality_by_design`); objeto distinto: el paso 4 pide FOMENTAR CONOCIMIENTO general en la fuerza laboral (cultura), el hijo es una METODOLOGIA estructurada de 5 pasos para un equipo de diseno |
| 78 | `metas_desmaterializacion_energia -> valoracion_costos_externos` (4) | sin camino | **NO SE ENLAZA** | objeto distinto: el paso 4 pide COMUNICAR ahorros YA logrados (resultado de la propia iniciativa); el hijo es una metodologia de VALORACION MONETARIA de externalidades ambientales (hedonic pricing, costos de restauracion), ya anclada en `contabilidad_ambiental`, tema mas amplio y tecnico |
| 79 | `coordinacion_colaboracion_cadena_suministro -> plataforma_colaboracion_masiva` (10) | sin camino | **NO SE ENLAZA**, DISCUTIBLE | D2: la madre YA enlaza directo a `plataforma_colaboracion_tiempo_real`, gemela casi identica en contenido (plataforma en la nube para colaboracion de multiples actores de la cadena, con visualizacion y simulaciones), que ya satisface el mandato del paso 10 |
| 80 | `estructura_equipos_innovacion_interna -> equipo_multifuncional_real` (2) | ALCANZABLE (5 saltos): via `actitud_de_experimentacion_organizacional -> cultura_de_optimismo -> calidad_de_ejecucion_proceso_innovacion -> sistema_gates_go_kill` | **SE ESCRIBE** | el paso 2 nombra LITERALMENTE "Formar un equipo multifuncional de tiempo completo con representacion de todas las areas"; el hijo trae 7 pasos propios (lider con autoridad real, tiempo liberado, incentivos de equipo, nucleo estable, co-ubicacion, trabajo en paralelo) que la madre no tiene; el camino de 5 saltos no pasa por ninguno de los 5 pasos de la madre, es incidental |
| 81 | `product_roadmap_estrategico -> equipo_multifuncional_real` (2) | ALCANZABLE (4 saltos): via `stage_gate_system -> calidad_de_ejecucion_proceso_innovacion -> sistema_gates_go_kill` | **NO SE ENLAZA** | objeto distinto (contraste con el 80): el paso 2 pide ensamblar un equipo multifuncional PARA EL EJERCICIO DE ROADMAPPING (comite de planificacion periodica), mientras el hijo describe un EQUIPO DE PROYECTO DE INNOVACION dedicado y de tiempo completo, con autoridad real; proposito de equipo distinto |
| 82 | `product_design_spreadsheet -> traduccion_necesidades_cliente` (1) | sin camino | **NO SE ENLAZA**, DISCUTIBLE | el paso 1 usa la traduccion YA HECHA como insumo ("colocar... su traduccion... en el lado izquierdo"), no ejecuta el procedimiento de traducir; el puente ya existe por la via establecida `customer_needs_spreadsheet` (antecesor comun de la madre y del hijo); forzar un enlace directo duplicaria esa via sin que la madre avance sobre contenido nuevo del hijo |
| 83 | `evaluacion_industria_cliente -> analisis_cadena_de_valor` (3) | ALCANZABLE (5 saltos): via `evaluacion_competencias_centrales -> seleccion_arenas_estrategicas -> investigacion_etnografica_ideacion -> analisis_y_sintesis` | **SE ESCRIBE** | el paso 3 nombra LITERALMENTE "Analizar la cadena de valor de la industria"; el hijo trae 4 pasos propios (mapear actores, analizar roles cambiantes, identificar desintermediacion, determinar funciones a capturar) que la madre no desglosa; el camino de 5 saltos pasa por competencias centrales/arenas/etnografia/sintesis, ninguno de los 8 pasos de la madre: incidental |
| 84 | `diagrama_de_flujo_proceso_map -> analisis_flujo_proceso` (8) | ALCANZABLE (3 saltos): via `fmea_analisis_de_modos_de_falla -> key_process_product_characteristics` | **SE ESCRIBE**, DISCUTIBLE | el paso 8 ("Analizar el diagrama de flujo resultante") es exactamente lo que el hijo ejecuta (dividir en estaciones de trabajo, documentar por estacion, usar para auditorias); discutible porque `diagrama_de_flujo_proceso_map` es un mapa GENERICO (producto/servicio/informacion) y existe un gemelo de servicio (`analisis_flujo_proceso_servicio`, ver fila 96); el camino de 3 saltos via FMEA no es la cadena propia |
| 85 | `stage_gate_system -> tipos_criterios_gate` (2) | ALCANZABLE (5 saltos): via `estrategia_innovacion_producto -> metodo_strategic_buckets -> mitos_stage_gate -> estructura_de_gates` | **SE ESCRIBE** | el paso 2 pide "Establecer gates de decision Go/Kill con criterios claros"; el hijo es la taxonomia completa de esos criterios (must-meet, go/kill, should-meet) con contenido que la madre no desglosa; el camino de 5 saltos alcanzable no pasa por ninguno de los 7 pasos de la madre |
| 86 | `waterfall_vs_agile_development -> customer_development_process` (3) | ALCANZABLE (4 saltos): via `producto_minimo_viable -> contabilidad_innovacion_pivote -> search_for_business_model` | **SE ESCRIBE** | el paso 3 nombra LITERALMENTE "el proceso de Customer Development"; el hijo ES ese proceso, con sus 4 etapas propias que la madre no desarrolla; el camino de 4 saltos (via MVP, pivote, search_for_business_model) no es la cadena propia de esta madre de 3 pasos |
| 87 | `competencias_director_calidad_bloom -> consejo_de_calidad_y_rol_del_director` (1) | sin camino | **NO SE ENLAZA** | objeto distinto: el paso 1 pide elaborar una MATRIZ DE COMPETENCIAS individuales del director (habilidades evaluadas via Bloom); el hijo trata de FORMAR UN CONSEJO DE CALIDAD y definir el rol dual del director en la gobernanza, tema organizacional distinto |
| 88 | `estructura_organizacional_funcional_proceso -> empoderamiento_empleados` (5) | ALCANZABLE (6 saltos): via `equipos_autodirigidos_servicio -> six_sigma_dmaic -> sostener_las_ganancias -> trilogia_de_juran -> sistemas_sociotecnicos` | **NO SE ENLAZA**, DISCUTIBLE | objeto distinto pese al calce casi literal del primer paso del hijo con el paso 5 de la madre: el paso 5 pide evaluar el nivel de involucramiento como UN FACTOR para elegir estructura organizacional; el hijo es un MODELO INTEGRAL de evolucion del empoderamiento (Taylor a autogestion), alcance mas amplio que el factor puntual que el paso pide evaluar |
| 89 | `decidir_vender_solo_online_o_tambien_tienda_fisica -> ofrecer_puntos_recogida` (2) | sin camino | **SE ESCRIBE** | el paso 2 pregunta LITERALMENTE si se va a "ofrecer recoger en tienda ademas de entrega a domicilio"; el hijo es exactamente el procedimiento de 5 pasos para implementar esa opcion (puntos aliados, agregarla al checkout, notificar al cliente, revisar adopcion); contenido que la madre no tiene |
| 90 | `teletrabajo_sostenible -> medir_huella_carbono_corporativa` (4) | sin camino | **NO SE ENLAZA** | objeto distinto: el paso 4 pide medir el EFECTO PUNTUAL del teletrabajo en productividad/huella (metrica de seguimiento de una iniciativa); el hijo es la metodologia INTEGRAL del GHG Protocol para inventariar TODA la huella corporativa en tres alcances, ejercicio mucho mas amplio y general |
| 91 | `diseno_controles_proceso_mejorado -> auditorias_calidad_proceso` (3) | ALCANZABLE (4 saltos): via `validacion_sistema_medicion -> autocontrol_y_controlabilidad -> autocontrol_planificacion_servicio` | **NO SE ENLAZA**, DISCUTIBLE | cadena propia ya tendida: el camino arranca en `validacion_sistema_medicion` (contenido del paso 5 de la madre) y avanza a `autocontrol_y_controlabilidad` (paso 6, "establecer el autocontrol"), en el mismo orden de la madre, hasta llegar a la auditoria; cableado ya tendido, no incidental |
| 92 | `principios_mejora_continua -> auditorias_calidad_proceso` (4) | sin camino | **NO SE ENLAZA** | objeto distinto: el paso 4 pide establecer controles de calidad EN EL ORIGEN (prevencion); el hijo es una auditoria independiente que COMPARA el desempeno contra un estandar YA establecido (verificacion posterior), actividad distinta de la prevencion en la fuente |
| 93 | `materiales_due_diligence -> guia_y_mentoria_vc` (3) | sin camino | **NO SE ENLAZA** | gemelo por la palabra "reuniones de junta": el paso 3 pide ORGANIZAR LAS ACTAS ya celebradas (tarea administrativa de archivo para due diligence), mientras el hijo trata de COMO APROVECHAR la mentoria de inversores EN esas reuniones (uso estrategico), objetos distintos |
| 94 | `fase_mobilizar_modelo_negocio -> business_model_canvas_scorecard` (3) | ALCANZABLE (4 saltos): via `fase_entender_modelo_negocio -> customer_scenarios_business_model -> lienzo_modelo_negocio` | **NO SE ENLAZA**, DISCUTIBLE | cadena propia: el camino arranca en `fase_entender_modelo_negocio` (la fase SIGUIENTE de este mismo proceso de 5 fases, hija directa de la madre) y avanza en el orden natural del metodo hasta el uso del canvas como scorecard SEMANAL, que pertenece a una fase posterior (durante el customer discovery en curso), no a la fase inicial "Mobilizar" que solo introduce el lienzo como lenguaje comun |
| 95 | `plan_de_lanzamiento_al_mercado -> personalizacion_investigacion_prospecto` (2) | sin camino | **NO SE ENLAZA** | objeto distinto: el paso 2 pide investigar como compra el cliente EN GENERAL para disenar el lanzamiento (investigacion agregada de mercado); el hijo es una tactica de personalizacion de UN prospecto individual antes de una reunion de venta (dato personal, conexion emocional), escala distinta |
| 96 | `planificacion_inicial_calidad -> analisis_flujo_proceso_servicio` (4) | sin camino | **NO SE ENLAZA**, DISCUTIBLE | D2 de dominio: la madre es "Planificacion Inicial de Calidad EN MANUFACTURA" y su paso 4 YA esta cubierto por el gemelo correcto (`analisis_flujo_proceso`, ya hijo directo de la madre, ver fila 84); `analisis_flujo_proceso_servicio` es el gemelo de SERVICIO, dominio ajeno a esta madre de manufactura |
| 97 | `analisis_tco_roi_b2b -> prueba_solucion_con_cliente` (3) | sin camino | **NO SE ENLAZA** | objeto distinto: el paso 3 es un ejercicio de COMPARACION FINANCIERA (ROI del producto contra la solucion actual del cliente); el hijo es una metodologia de ENTREVISTAS ESTRUCTURADAS (presupuesto, precio, canal, aprobacion), actividad cualitativa distinta de la comparacion cuantitativa |
| 98 | `capacidad_proceso_concepto -> sistema_informacion_calidad` (6) | ALCANZABLE (6 saltos): via `control_estadistico_de_procesos -> causas_comunes_vs_especiales -> control_estadistico_proceso -> costo_de_mala_calidad_copq -> accion_correctiva` | **NO SE ENLAZA** | objeto distinto: el paso 6 pide USAR la informacion de capacidad para tres decisiones especificas (diseno, seleccion de procesos, control); el hijo es el DISENO de todo un sistema de informacion organizacional para la toma de decisiones de calidad en general, alcance mucho mas amplio; camino de 6 saltos incidental |
| 99 | `gobierno_corporativo_y_calidad -> principios_mejora_continua` (5) | sin camino | **NO SE ENLAZA**, DISCUTIBLE | el paso 5 ("capacitate en principios de excelencia y calidad") es GENERICO y no nombra Shingo ni mejora continua especificamente; escribir aqui abriria la puerta a enlazar con cualquier marco de principios candidato, el patron que el 9.6.2 advierte evitar; se prefiere no escribir sobre un paso tan inespecifico |
| 100 | `poder_a_traves_de_la_accion -> proposito_como_motor_energia` (4) | ALCANZABLE (2 saltos): via `compromiso_organismico_en_la_accion` | **NO SE ENLAZA**, DISCUTIBLE | cadena propia, avanza en el orden de la madre: arranca en `compromiso_organismico_en_la_accion` (hijo directo que ejecuta el paso 3, "asegurar que la accion sea genuina y comprometida", escrito por la vuelta 84) y avanza a `proposito_como_motor_energia`, contenido EXACTO del paso 4 (cita a Bentham en los dos textos); avanza paso 3 a paso 4, cadena ya tendida |
| 101 | `customer_discovery_phase2_problem_test -> ganar_comprension_del_cliente` (3) | ALCANZABLE (4 saltos): via `problem_solution_fit -> business_model_canvas_scorecard -> customer_discovery` | **NO SE ENLAZA**, DISCUTIBLE | el hijo declara EXPLICITAMENTE en su propio resumen que "va mas alla de validar que el problema existe" (que es justamente lo que hace el paso 3 de esta madre); el camino arranca en `problem_solution_fit` (hijo directo, el hito natural tras validar el problema) y avanza hacia la comprension profunda, orden natural del proceso, no incidental |

**RESULTADO: 7 SE ESCRIBEN (76, 80, 83, 84, 85, 86, 89), 23 NO SE ENLAZAN, 0
INCONSISTENTES, 0 ESCALERA ROTA**
(`docs/loop/SALIDA_V85_TRAMO10_ESCRIBIR.txt`, verificado contra el grafo de
HOY tras escribir con `scripts/loop/vuelta85_tramo10_escribir.py`,
`docs/loop/SALIDA_V85_TRAMO10_ESCRIBIR_APLICACION.txt`). **TRECE
DISCUTIBLES marcados ANTES de saber si aciertan: 73, 77, 79, 81, 82, 84, 88,
91, 94, 96, 99, 100, 101** (mas del promedio de tramos anteriores porque
esta tanda trajo 15 de 30 unidades ALCANZABLE, que exigen el juicio de
cadena propia en vez de la cita literal simple).

Ciclo de tres corrido tras la TAREA 4 (`SALIDA_V85_GATE0_TRAS_TAREA4.txt`,
`SALIDA_V85_ETIQUETAS_TRAS_TAREA4.txt`, `SALIDA_V85_SYNC_TRAS_TAREA4.txt`),
GATE 0 OK, 71 etiquetas identicas, 6 assets, `git status --porcelain --
dataset/ web/lib/assets/` cero lineas tras el ciclo. Aristas tras la TAREA 4
(`docs/loop/SALIDA_V85_CONTEO_TRAS_TAREA4.txt`): sig **8.986**, prev
**8.965**, suma **17.951**, union **9.609** (+7/+7/+14/+7 sobre el estado
tras la TAREA 2). Las siete aristas verificadas en las DOS vistas, cero
inversas:

```
lienzo_proyecto_innovacion -> actividades_clave: en_sig_madre True en_prev_hijo True INVERSAS False/False
estructura_equipos_innovacion_interna -> equipo_multifuncional_real: en_sig_madre True en_prev_hijo True INVERSAS False/False
evaluacion_industria_cliente -> analisis_cadena_de_valor: en_sig_madre True en_prev_hijo True INVERSAS False/False
diagrama_de_flujo_proceso_map -> analisis_flujo_proceso: en_sig_madre True en_prev_hijo True INVERSAS False/False
stage_gate_system -> tipos_criterios_gate: en_sig_madre True en_prev_hijo True INVERSAS False/False
waterfall_vs_agile_development -> customer_development_process: en_sig_madre True en_prev_hijo True INVERSAS False/False
decidir_vender_solo_online_o_tambien_tienda_fisica -> ofrecer_puntos_recogida: en_sig_madre True en_prev_hijo True INVERSAS False/False
```

**`docs/plan/PASO_NODO_CALIBRADO.jsonl` se commitea recalibrado tal como
quedo** (adjudicacion 5.7 del acta 82): el fichero de esta vuelta refleja
las 3 aristas heredadas de la vuelta 84 (TAREA 3 de esa vuelta) MAS las 7
que la TAREA 4 de esta vuelta escribio DESPUES de calibrar, **CON DESFASE, Y
EL DESFASE ESTA DICHO Y MEDIDO, no negado**: 7 filas al cierre, tabla de la
cabecera de arriba y `docs/loop/SALIDA_V85_DESFASE_CALIBRADO_CIERRE.txt`.

---

## 5. TAREA 5: LA VARA DEL TRAMO 10, CON INSTRUMENTO PROPIO

`scripts/loop/vuelta85_tarea5_vara_tramo10.py`, sucesor de
`vuelta84_tarea4_vara_tramo9.py`, pares LEIDOS del fichero del filtro sin
teclear, con el alcance fijado sin ambiguedad por la adjudicacion 6.5 del
acta 84: **(5.a)** las 30 unidades frescas del tramo 10 contra
`docs/INTRA_DOMINIO_VEREDICTOS.jsonl` SIN direccion; **(5.b)** las mismas 30
contra `docs/plan/PASO_NODO_CALIBRADO_FILTRADO_V84.jsonl` (la bolsa de la
vuelta ANTERIOR) buscando la reciproca. Corrida
(`docs/loop/SALIDA_V85_TAREA5_VARA_TRAMO10.txt`):

```
unidades leidas del filtro: 30 | frescas (72..101): 30
veredictos leidos: 3388 | pares no dirigidos unicos: 3388
bolsa filtrada V84: 142 unidades
RESUMEN: 3 de 30 con veredicto, 0 de 30 con reciproca
```

**Las tres con veredicto, las tres clase D** (la clase mas comun del
marcador, mide semejanza global de contenido y no ejecucion literal de un
paso, sin peso decisorio propio):

| # | par | puesto | dominio | decision de esta vuelta |
|---:|---|---:|---|:---:|
| 80 | `estructura_equipos_innovacion_interna` / `equipo_multifuncional_real` | 1.401 | core | **SE ESCRIBE** |
| 84 | `diagrama_de_flujo_proceso_map` / `analisis_flujo_proceso` | 2.728 | quality | **SE ESCRIBE** |
| 101 | `customer_discovery_phase2_problem_test` / `ganar_comprension_del_cliente` | 1.397 | core | NO SE ENLAZA |

**DIFERENCIA DECLARADA CONTRA EL PATRON DE TRAMOS ANTERIORES, SIN QUE SEA
CONTRADICCION FORMAL:** en los tramos 8 y 9, los pares con veredicto D
coincidieron siempre con la decision NO SE ENLAZA; en este tramo, DOS de los
tres pares con veredicto D (80 y 84) se decidieron SE ESCRIBE. No es una
contradiccion: el marcador D mide semejanza global de titulo/contenido
entre los dos nodos (una senal AJENA a si un paso especifico de la madre
nombra literalmente al hijo como su ejecucion), y en los dos casos la
decision SE ESCRIBE se sostiene sobre una cita LITERAL del paso ("formar un
equipo multifuncional", "analizar el diagrama de flujo resultante"), no
sobre semejanza de titulo. Se declara para que no se lea como patron roto.
**CERO reciprocas**, sin discrepancia contra las cifras que el encargo no
predijo en digitos (la adjudicacion 6.5 fijo el ALCANCE, no una cifra de
contraste para este tramo).

---

## 6. EL CIERRE: SEGUNDO HORNEADO, CABECERA TALLADA Y `--comparar`

Suites y ciclo corridos AL CIERRE, cada una con su fichero: Gate 0
(`SALIDA_V85_GATE0_CMD1_CIERRE.txt`, OK), etiquetas
(`SALIDA_V85_ETIQUETAS_CIERRE.txt`, 71 identicas), assets
(`SALIDA_V85_SYNC_CIERRE.txt`, 6), `git status --porcelain -- dataset/
web/lib/assets/` cero lineas tras el ciclo, motor
(`SALIDA_V85_MOTOR_CIERRE.txt`, 25/25), web (`SALIDA_V85_WEB_CIERRE.txt`, 80
passed / 1.030 passed 3 skipped), tsc (`SALIDA_V85_TSC_CIERRE.txt`, EXITCODE
0, cero lineas), aristas (`SALIDA_V85_CONTEO_CIERRE.txt`: sig 8.986, prev
8.965, suma 17.951, union 9.609, identico al estado tras la TAREA 4: la
TAREA 5 no escribe nada), desfase del calibrado
(`SALIDA_V85_DESFASE_CALIBRADO_CIERRE.txt`, 7 filas). El segundo horneado
(TAREA 3.a) corrio DESPUES de la TAREA 4 y ANTES de estas mediciones de
cierre, dejando el registro en 186 filas.

**CASO OBLIGATORIO (i), el `--comparar` del tramo 10 contra este mismo
reporte, corrido DESPUES de pegar la tabla de la seccion 4.2 arriba:**

```
python scripts/loop/tallar_cabecera_reporte.py --vuelta 85 --tramo-cadena 10 --comparar docs/loop/REPORTE.md
```

Salida (`docs/loop/SALIDA_V85_COMPARAR_TRAMO10.txt`):

```
--- COMPARACION CONTRA docs/loop/REPORTE.md ---

  UNIDADES NO PUBLICADAS EN ESA TABLA: 0

  filas cotejadas: 30 | DISTINTAS: 0 | ausentes (no rojo): 0 | inventadas (ROJO): 0
  TABLA DE LA CADENA: IDENTICA AL TALLADOR (las ausentes listadas no son rojo)
```

**CABECERA Y TABLA DE LA CADENA IDENTICAS, EXIT 0.**

**El `--comparar` de la cabecera `--fase04`, corrido DESPUES de recomputar
el cierre y de terminar de escribir este reporte:**

```
python scripts/loop/tallar_cabecera_reporte.py --fase04 --vuelta 85 --comparar docs/loop/REPORTE.md
```

Salida (`docs/loop/SALIDA_V85_COMPARAR_FASE04.txt`):

```
--- COMPARACION CONTRA docs/loop/REPORTE.md ---

  filas cotejadas: 9 | DISTINTAS: 0 | ausentes: 0
  CABECERA: IDENTICA AL TALLADOR
```

**CABECERA IDENTICA AL TALLADOR, 9 filas cotejadas, 0 distintas, EXIT 0.**

---

## 7. DISCUTIBLES, PENDIENTES Y CORRECCIONES: RESUMEN PARA LA RELECTURA CIEGA

**Discutibles marcados esta vuelta, ANTES de saber si aciertan (tramo 10,
seccion 4.3): 73, 77, 79, 81, 82, 84, 88, 91, 94, 96, 99, 100, 101 (TRECE).**
Los que dependen de "cadena propia ya tendida" (91, 94, 100, 101) o de "D2
por gemelo/familia ya anclada" (79, 96) son los mas discutibles porque son
lecturas de topologia; los que dependen de un caveat de paso (73) o de
alcance/genericidad del paso (88, 99) son juicios de contenido igual de
discutibles.

**Correcciones declaradas esta vuelta:**
1. Los pares 50, 55 y 77 (seccion 2): la clase pasa de NO SE ENLAZA (vuelta
   84) a SE ESCRIBE (esta vuelta), a favor del caso del auditor, verificada
   contra el grafo, con las tres aristas escritas y verificadas en las dos
   vistas.
2. Las dos frases de prosa de la vuelta 84 (seccion 1.1) quedan talladas
   como filas de la cabecera desde esta vuelta (seccion 3.b).

**PENDIENTE DE DOCTRINA (nuevo esta vuelta):** la guarda del registro sobre
la bolsa filtrada, corrida DESPUES del segundo horneado de cierre, da ROJO
por un artefacto conocido y declarado (seccion 3.a): no reconoce las
unidades `ESCRITA` como "decididas", solo las `NO SE ENLAZA`, y por eso lee
como "saltadas" unidades que SI se leyeron esta vuelta (verificado contra
`SALIDA_V85_TRAMO10_ESCRIBIR.txt`). Traigo la pregunta de si la guarda debe
aprender tambien el estado `ESCRITA`, o si el ROJO en esta circunstancia se
acepta como lectura correcta del instrumento y se declara sin mas cada vez.
No lo resuelvo yo (`EJECUTOR.md` regla 5).

**Discrepancia declarada, sin racha:** de los tres pares con veredicto D en
la TAREA 5, dos (80, 84) se decidieron SE ESCRIBE, rompiendo el patron de
los dos tramos anteriores donde todo veredicto D coincidia con NO SE
ENLAZA (seccion 5). No es contradiccion (el marcador mide otra cosa), pero
se declara para que la relectura ciega la vea sin tener que recalcularla.

**Preguntas traidas sin adivinar (`EJECUTOR.md` regla 11):** la del
PENDIENTE DE DOCTRINA de arriba (la guarda y el estado `ESCRITA`).

---

## 8. METRICA DE CREDITO Y RACHAS (para el auditor)

**Freno de la vuelta 84, con su aritmetica:** racha de CLASE O CIFRA
PUBLICADA en CERO (pide dos, sin disparar, siete vueltas limpias de 78 a
84), racha de REPORTE en UNO (pide tres, sin disparar, pero la escalada de
codigo se encargo igual por ser la misma especie de las vueltas 77 a 79).
CREDITO DE TANDA rebajado por caida (dos caidas de reporte en la misma
vuelta): esta vuelta entrega el tramo 10 completo (30 de 30) y la relectura
conjunta completa (3 de 3 pares nombrados) para esa relectura extendida.

**Repaso del encargo, punto por punto, lo que se corrio y lo que no:**

| punto del encargo | se corrio |
|---|---|
| Commitear y pushear lo pendiente antes de tocar nada | SI, `git status` limpio al abrir |
| TAREA 1.1, registrar las dos caidas de reporte sin remedir | SI (1.1) |
| TAREA 1.2, registrar el incumplimiento de la TAREA 4 con nombre y sin racha | SI (1.2) |
| TAREA 1.3, correccion declarada sobre las aristas y el desfase | SI (1.3, cita las nueve adjudicaciones) |
| TAREA 1.5, registrar las nueve adjudicaciones 6.1 a 6.9 | SI (1.3) |
| TAREA 2, relectura conjunta de 50, 55, 77 ANTES del filtro | SI (seccion 2), las tres SE ESCRIBEN |
| TAREA 3.a, horneador dos veces (antes del filtro y al cierre) | SI (3.a), con el ROJO de la guarda declarado como artefacto |
| TAREA 3.b, dos filas nuevas en el tallador + casos obligatorios verde/rojo | SI (3.b) |
| TAREA 3.c, `--comparar` del tramo 10 | SI (seccion 6, caso (i)) |
| TAREA 4, tramo 10 completo (30 unidades), vara de la cadena con criterio 6.1 | SI (4.1 a 4.3), 30 de 30 leidas |
| TAREA 5, vara del tramo 10 (5.a y 5.b) | SI (seccion 5) |
| Cabecera tallada `--fase04 --vuelta 85` + `--comparar` | SI (cabecera arriba, comparar en seccion 6) |
| Sello de HEAD antes de la 1.a operacion | SI (`SALIDA_V85_HEAD_APERTURA.txt`) |
| `PASO_NODO_CALIBRADO.jsonl` commiteado recalibrado, desfase dicho y medido | SI (seccion 4.3, tabla de cabecera) |
| Cero guiones largos/medios | SI, con el hook corriendo |

**NO HAY PARADA.** Ninguna afirmacion de este reporte contradice una regla
vigente ni una cifra publicada sin remedio. El PENDIENTE DE DOCTRINA de la
seccion 7 se trae como pregunta, no como contradiccion: la guarda dio el
resultado que su propio codigo produce, y el resultado se declaro y se
verifico contra el fichero de la lectura real en vez de esconderse.
