# REPORTE del ejecutor del bucle, vuelta 9 (checkpoint 3.300)

**Sesion ejecutora (Sonnet 5). Fecha de reloj: 13 ago 2026. Corte del cribado: puesto 3.300 de
3.388.** Rama activa: `bucle`. Hash de referencia para el estado del cribado (marcador, archivo):
`d498fc0b` (checkpoint 3.300). El commit de este propio reporte y del informe quedara por encima
en la rama; si se cita un hash "final" antes de comitear el reporte, ese hash queda superado por
el commit del reporte, el mismo patron que dejaron anotado las vueltas 6, 7 y 8.

## Hash y rutas

- **Archivo del cribado:** `docs/INTRA_DOMINIO_VEREDICTOS.jsonl` en **3.300 lineas exactas**,
  puestos 1 a 3.300, **cero huecos (set 1..3300 completo), cero duplicados de puesto y cero pares
  duplicados** (nodo_a/nodo_b/dominio), verificado con `python scripts/recomputar_marcador.py
  3300`.
- **Rutas tocadas esta vuelta:** `docs/INTRA_DOMINIO_VEREDICTOS.jsonl` (100 veredictos nuevos,
  3.201 a 3.300, todos sobre puestos nunca antes registrados; ninguna correccion sobre un puesto
  ya registrado esta vez, a diferencia de la vuelta 8), `docs/INTRA_DOMINIO_INFORME.md` (seccion
  98 con seis correcciones declaradas tachadas sin borrar, seccion 99 nueva completa),
  `docs/loop/REPORTE.md` (este archivo). `docs/plan/` NO se toco, como manda el modo de cierre.
  Scripts auxiliares usados, sin crear ninguno nuevo: `scripts/volcar_pares.py`,
  `scripts/recomputar_marcador.py`, `scripts/_registrar_lote.py`. Seis lotes temporales
  (`docs/loop/_lote_*.py` y `.jsonl`) se crearon y se borraron en la misma vuelta tras
  registrarse; ninguno quedo en el repo.
- **Commits de la vuelta:** `a4595f7f` (TAREA 1 completa: los ocho arreglos de registro del
  encargo, cribado 3.201-3.225), `9095686e` (cribado 3.226-3.255, cierra `quality`), `d498fc0b`
  (cribado 3.256-3.300, abre `risk_management`, checkpoint 3.300).

## TAREA 1: reparar el registro, recontar, cerrar el pendiente de medicion

Los seis arreglos de registro que pedia el encargo (mas los dos verificados sin tocar), todos
resueltos con reglas ya escritas, ninguno con doctrina nueva. Detalle completo con cita en
`docs/INTRA_DOMINIO_INFORME.md` seccion 98 (tachado sin borrar sobre el texto original), resumen
aqui.

### 1.1 La regresion del marcado: archivo y tabla reconciliados

El encargo encontro que el conjunto publicado como "discutibles fuertes" (siete: 3.121, 3.147,
3.148, 3.165, 3.173, 3.176, 3.182) no calzaba con el conjunto realmente marcado fuerte en el
archivo (seis: 3.120, 3.121, 3.165, 3.173, 3.176, 3.182). Verificado contando la cadena literal:
"DISCUTIBLE MARCADO fuerte" aparece en esos seis puestos; "DISCUTIBLE MARCADO" sin el calificador
aparece ademas en 3.137 y 3.148 (marca simple); **3.147 no lleva la cadena en ningun grado**, y
sin embargo se habia publicado como fuerte.

**Aplicada la adjudicacion tal cual el encargo la trajo: el archivo manda sobre la tabla, y las
dos se publican del mismo conjunto.** Se anadio 3.120 (estaba marcado fuerte y no se habia
publicado: hoshin_kanri contra planificacion_estrategica_despliegue, D confirmada, comparten
catchball/scorecard con arista pero cada uno trae pasos enteros propios que el otro no tiene). Se
retiro 3.147 del conjunto fuerte (sin marca de ninguna clase; la D se sostiene mejor por la
comparacion directa de pasos, no se le agrego marca retroactiva porque, releido, no es el caso
mas contestado del tramo). Se retiro 3.148 del conjunto fuerte (marca simple, no fuerte). **El
conjunto fuerte corregido y republicado, identico entre archivo y tabla, queda en SEIS: 3.120,
3.121, 3.165, 3.173, 3.176, 3.182.** Verificacion declarada en 98.6 del informe, y la misma
verificacion se corrio de nuevo para el checkpoint de esta vuelta (ver mas abajo, discutibles
3.201-3.300): DOS marcas fuertes en el archivo, dos filas en la tabla, lista identica. Esta
verificacion queda fija desde ahora para cada checkpoint en adelante, como pide el encargo.

### 1.2a Familia "ficha nombrada dentro del paso de otro nodo": de nueve/veintiuno a catorce/veintiseis

El reporte anterior decia "nueve casos nuevos" pero enumeraba DIEZ, y daba "veintiuno acumulados"
(que no sale de sumar ninguno de los dos numeros publicados). Recontado con el instrumento (la
cita literal en la propia razon de cada puesto, criterio adjudicado: cuenta el par donde un nodo
despliega la mecanica de UN paso del otro, y el otro trae pasos enteros que el primero no cubre,
nombrado literal o condensado o implicito): los diez ya enumerados (3.103, 3.107, 3.114, 3.118,
3.156, 3.169, 3.175, 3.186, 3.197, 3.200) mas los CUATRO que el auditor senalo y que verifique uno
por uno contra su propia cita literal ("ficha nombrada dentro del paso de otro nodo" o
equivalente exacto): 3.155 (distribucion_poisson, aplicacion especifica de un paso de
distribuciones_probabilidad), 3.177 (analisis_causa_raiz_diagnostico, metodo especifico
mencionado en un paso de accion_correctiva), 3.181 (codigo_conducta_orientado_cliente, ficha del
paso 2 de normas_culturales_calidad) y 3.195 (deteccion_defectos_raros_control_estadistico,
procedimiento tecnico especifico de un paso de abolir_inspeccion_masiva). **Los catorce
confirmados: CATORCE en el tramo 3.101-3.200, VEINTISEIS acumulados desde el 2.956** (doce previos
mas los catorce, la aritmetica ahora si calza). En el cierre de `quality` (3.201-3.255) aparecieron
seis casos mas (3.205, 3.206, 3.210, 3.223, 3.235, 3.238): **TREINTA Y DOS acumulados al cerrar el
dominio.** La figura reaparecio ademas en el dominio nuevo `risk_management` (3.282, 3.284, 3.285,
3.294): se declara como **reaparicion con precedente citado**, no como continuidad del contador de
`quality`, tal como pide el encargo para las figuras que crucen de un dominio a otro.

### 1.2b Familia "la capacidad del proceso, SIN ACTO": de seis/cinco a cuatro

El reporte anterior decia "seis pares mas" y enumeraba CINCO (3.130, 3.141, 3.149, 3.152, 3.200).
Verificado: el 3.130 NO invoca la familia (su propia razon dice "dos fases sucesivas del mismo
cascadeo de mejora", un marco distinto, DISENAR contra PROBAR/CONFIRMAR). Los que si se declaran
de la familia, con la cita literal "Familia ya reconocida SIN ACTO (la capacidad)" en su propia
razon: 3.141, 3.149, 3.152 y 3.200. **Son CUATRO, no seis ni cinco.** Corregido en 98.5 del
informe. Sin casos nuevos en el cierre de `quality` (3.201-3.255).

### 1.3 Hubs: recontados sobre el archivo, altos por uno cada uno

Contado por puesto sobre el tramo 3.101-3.200: `concepto_haciendo_la_calidad_cierta` D contra
**SEIS** vecinos (3.125, 3.136, 3.137, 3.147, 3.150, 3.190), no siete; `gestion_estrategica_de_
calidad_sqm` D contra **TRES** vecinos (3.151, 3.159, 3.167), no cuatro; `planificacion_calidad_
crosby` D contra tres (3.143, 3.151, 3.161), ese si calzaba y no se toco. Corregido en 98.5. Al
cerrar `quality`, el conteo domino-wide completo de los cuatro hubs (no solo de la sesion del
encargo anterior) queda en la seccion de cierre mas abajo.

### 1.4 La cita del entregable_esperado: no era universal, y la adjudicacion que lo resuelve

El reporte anterior afirmaba haber citado el `entregable_esperado` "en todos los casos de alta
similitud", enumerando los siete discutibles. Verificado contra el archivo: **3.121 y 3.173 NO
mencionan la palabra "entregable" en ninguna forma** dentro de su razon. Los otros cinco (3.147,
3.148, 3.165, 3.176, 3.182) si la mencionan. La afirmacion era una lectura no escrita (regla 9).
Se corrigio la afirmacion, no la razon: en 3.121 y 3.173 la D se sostiene por comparacion directa
de pasos enteros, sin apoyo del entregable, y las dos D siguen correctas.

**Adjudicacion escrita para cerrar la contradiccion aparente:** el desempate por
`entregable_esperado` es una PRUEBA NEGATIVA, no positiva. La adjudicacion 1.4d dice "si dos nodos
producen artefactos distintos, no son el mismo acto"; no dice, ni se puede leer al reves, que
artefactos iguales o casi iguales prueben el mismo acto. La clase la decide siempre la comparacion
de pasos enteros. Consistente entre el 3.165 (el entregable del superviviente anade un puntaje y
aun asi funde, A) y el 3.148 (los entregables se parecen y aun asi no funde, D): en ninguno de los
dos decidio el entregable, decidio si quedaba o no un paso entero fuera. Detalle en 98.7 del
informe. Esta adjudicacion se aplico explicitamente en el cribado nuevo de esta vuelta (los
entregables consultados en cada par de 3.201 a 3.300, siempre como prueba negativa nunca positiva).

### 1.5 El piso de 0,0 %: la glosa corregida y la noticia mas fuerte que la publicada

La 98.4 y el reporte anterior decian "dos tramos en 0,0 % exacto, el primero desde el
2.976-3.000", lo que es falso: recomputada la vara entera desde el 2.901 (doce tramos de 25):
**4,0 / 8,0 / 8,0 / 0,0 / 4,0 / 0,0 / 4,0 / 0,0 / 0,0 / 0,0 / 4,0 / 4,0**. Hay CINCO tramos en
0,0 % en ese rango, no dos, y entre el primero (2.976-3.000) y el 3.101-3.125 hay otro 0,0 % mas
(3.026-3.050). Lo cierto, y es una noticia mas fuerte: el **3.076-3.100, el 3.101-3.125 y el
3.126-3.150 son TRES TRAMOS CONSECUTIVOS EN 0,0 %, la racha mas larga de la campana (75 pares)**,
y despues el cuerpo repunto a 4,0 % dos veces seguidas. Corregido en 98.4 del informe.

### 1.6 Dos detalles menores de 98.1: corregidos

La 98.1 decia "leyendo los 579 veredictos A" cuando la propia seccion declara la caida del 2.630
que los deja en 578 al corte 3.100: corregido a 578. Y esas mismas dos lineas eran las UNICAS DOS
ACENTUADAS de las ultimas 784 lineas del informe ("asi que", "re-derivacion"): quitados los
acentos para respetar la convencion del documento.

### 1.7 El pendiente de medicion del contador de fusiones mutuas: acotado y corrido

El auditor midio la zona ciega (384 A de puesto menor a 2.127 sin palabra clave del barrido
original) y aislo, con una red de epoca sacada de los miembros tempranos de la serie, DIECINUEVE
hits sobre esos 384: 793, 796, 844, 853, 878, 905, 918, 943, 966, 978, 2.022, 2.043, 2.072, 2.074,
2.075, 2.076, 2.079, 2.087, 2.090. **Se leyeron los diecinueve con el criterio de la vuelta 7.**
Resultado: **los diecinueve son REPITE/CONTENCION CON SUPERVIVIENTE DECLARADO** (cada uno nombra
explicitamente "el corto" y "el largo", y declara que el corto "cabe entero" o "cabe casi entero"
dentro del largo, con el largo como superviviente por dominancia, NO "ninguno domina"). Ninguno
cumple el criterio (a) de la fusion mutua (mismo acto SIN dominancia). Cita completa de cada uno
en 98.1 del informe. **Ninguno de los diecinueve entra a la serie de fusiones mutuas.** El
contador se queda en VEINTISIETE (sin cambio por este delta). El pendiente de medicion se acota:
de los 384 A ciegos anteriores al 2.127, 17 ya caian en el barrido de palabra clave original, 19
se leyeron y descartaron esta vuelta, **quedan 365 A sin verificar**, cifra dicha y no laguna
vaga, registrada como PENDIENTE DE MEDICION para quien retome el barrido con mas presupuesto.

### 1.8 Lo verificado y en verde: no se toco

El marcador entero al corte 3.200, las ocho tasas, los cuatro tramos de la vara, la cascada del
2.630 en sus cinco cortes, el 3.165/3.182 en A y el 3.121/3.147/3.148/3.173/3.176 en D: todo
verificado por el auditor en la vuelta anterior, nada de esto se reabrio.

### 1.9 y 1.10: registro de preguntas y figuras

PREGUNTA 2 sigue cerrada. PREGUNTA 3 confirmada de nuevo en el 3.113 y despues en el 3.217 (ver
mas abajo, cierra ABIERTA con el dominio). PREGUNTA 4 con su conteo corregido (1.2a). PREGUNTA 5
sigue como figura reconocida. La senal del idioma y las perdidas de nombre, sin aparicion nueva
desde el corte 3.000 hasta el 3.300 (verificado directo sobre los cuatro A del tramo anterior y
los cero A de este tramo, no por barrido de candidatos): declarado explicitamente en 99.6 del
informe para que una figura que deja de reportarse no se confunda con una que desaparecio.

## TAREA 2: cribado 3.201 a 3.300 (cien pares nuevos), CIERRE de `quality` y APERTURA de
## `risk_management`

### Marcador recomputado del archivo (corte 3.300, cero huecos, cero duplicados, comando
`python scripts/recomputar_marcador.py 3300`)

| clase | conteo | porcentaje |
|---|---:|---:|
| A | **580** | 17,6 % |
| B | 89 | 2,7 % |
| C | 7 | 0,2 % |
| D | **2.624** | 79,5 % |

Contra el checkpoint 3.200 (A 580, D 2.524): **+0 A y +100 D** en los 100 pares nuevos de
3.201 a 3.300. Es el primer checkpoint de cien pares sin ninguna A desde que este ejecutor lleva
el cribado.

### Tasa por dominio (corte 3.300, NUEVE dominios)

| dominio | n | A | tasa |
|---|---:|---:|---:|
| core | 1.445 | 344 | 23,8 % |
| health_safety | 192 | 45 | 23,4 % |
| **quality** | **844** | **126** | **14,9 %** (CERRADO en el 3.255) |
| environmental | 170 | 29 | 17,1 % |
| franquicias | 148 | 18 | 12,2 % |
| exportacion | 130 | 15 | 11,5 % |
| entrega | 171 | 2 | 1,2 % |
| compras | 155 | 1 | 0,6 % |
| **risk_management** | **45** | **0** | **0,0 %** (ABIERTO) |

Quedan **88 pares** hasta el 3.388: risk_management 61 (3.301 a 3.361), seguridad_digital 27
(3.362 a 3.388).

### BLOQUE DE CIERRE DE `quality` (844 pares, 126 A, 14,9 %, corte 3.255)

**Vara por tramo de los dos tramos nuevos mas la cola de cinco:**

| tramo | pares | A | tasa |
|---|---:|---:|---:|
| 3.201-3.225 | 25 | 0 | 0,0 % |
| 3.226-3.250 | 25 | 0 | 0,0 % |
| 3.251-3.255 | 5 | 0 | 0,0 % |

`quality` cierra con **55 pares seguidos sin ninguna A**, del 3.201 al 3.255. No es la racha de
tramos completos mas larga (esa sigue siendo la del 3.076-3.150, 75 pares, ver 1.5), pero es el
cierre entero del dominio en el mismo piso bajo que traia desde el 2.976. No force A para
compensar ni D para sostener la tendencia: cada D de los 55 pares finales tiene su comparacion de
pasos enteros escrita en su propia razon, y su `entregable_esperado` revisado como prueba negativa
antes de decidir.

**Resumen de racimos y familias del dominio entero, al cerrar:**

- **Fusion mutua, la familia que SI funde:** `quality` aporta **VEINTICINCO de los VEINTISIETE**
  casos de la serie completa (98.1 del informe tiene la tabla con puesto y par); solo el 2.127
  (franquicias) y el 2.368 (health_safety) quedan fuera de `quality`. Superviviente **POR ELEGIR**
  en la mayoria de los casos (2.760, 2.762, 2.773, 2.780, 2.787, 2.825, 3.182, entre otros),
  superviviente nombrado en los mas antiguos de la serie.
- **Contencion por procedimiento mas completo:** un solo caso en todo el dominio, el 3.165. Figura
  reconocida, no volvio a aparecer hasta el cierre.
- **La capacidad del proceso, SIN ACTO, la familia que NUNCA funde:** al menos 28 pares la
  invocan explicitamente entre el 2.506 y el 3.200 (cota inferior por barrido de la frase, no
  censo, misma disciplina epistemica del BANCO 9.28); sin casos nuevos en el cierre.
- **Ficha nombrada dentro del paso de otro nodo, la figura mas frecuente:** TREINTA Y DOS
  acumulados al cerrar el dominio (26 al corte 3.200, mas seis en el cierre: 3.205, 3.206, 3.210,
  3.223, 3.235, 3.238). Siempre D, nunca funde.
- **Los cuatro hubs, conteo domino-wide completo (no solo de la sesion del encargo anterior):**
  `concepto_haciendo_la_calidad_cierta` D contra DIEZ vecinos en todo el dominio (2.866, 2.960,
  2.981, 3.125, 3.136, 3.137, 3.147, 3.150, 3.190, 3.249), cero A. `quality_awareness_crosby` D
  contra NUEVE vecinos (2.630 corregido a D, 2.648, 2.696, 2.939, 3.040, 3.067, 3.089, 3.097,
  3.251), cero A. `planificacion_calidad_crosby` D contra SIETE vecinos (2.651, 2.955, 3.007,
  3.143, 3.151, 3.161, 3.230), cero A. `gestion_estrategica_de_calidad_sqm` D contra SIETE
  vecinos (2.925, 3.030, 3.151, 3.159, 3.167, 3.203, 3.239) PERO CON UNA A en todo el dominio, el
  2.787 (fusion mutua, item 22 de la serie): es el UNICO de los cuatro hubs que fundio alguna vez,
  y solo una vez, con un nodo distinto de todos los que le dieron D.
- **PREGUNTA 5, planificar contra ejecutar:** cierra como figura reconocida, sin casos nuevos en
  el tramo final.

**Estado final de las PREGUNTAS 3, 4 y 5 al cerrar el dominio:**
- **PREGUNTA 3** (sub-cumulo de la responsabilidad gerencial): confirmada de nuevo en el 3.217,
  **cierra ABIERTA**. El encargo anterior avisaba que los 55 pares finales eran su ultima
  oportunidad de resolverse dentro de `quality`; no se resolvio. Con el dominio cerrado, la
  pregunta no tiene mas oportunidad AQUI y queda registrada como abierta sin resolucion, para
  quien la retome si aparece un ejemplar equivalente en otro dominio.
- **PREGUNTA 4** (ficha nombrada dentro del paso): cierra como figura reconocida con TREINTA Y DOS
  casos, y REAPARECE en `risk_management` (declarada como reaparicion, no continuidad).
- **PREGUNTA 5** (planificar contra ejecutar): cierra como figura reconocida, sin novedad.

### APERTURA de `risk_management` (45 pares, 0 A, corte 3.300)

Dominio nuevo, tres fuentes (Edwards et al. *Managing Project Risks*, Hubbard *The Failure of
Risk Management*, DeMarco y Lister *Waltzing with Bears*), sin un solo veredicto intra previo en
el archivo. **Cero A en los primeros 45 pares.** No se comparo esta tasa contra `quality` ni
ningun otro dominio (catalogos distintos, aviso explicito del encargo). No se importaron
familias de `quality` como propias: donde la figura de ficha nombrada dentro del paso reaparecio
(3.282, 3.284, 3.285, 3.294) se cito como reaparicion con precedente, no como extension del
contador de `quality`.

El dominio es denso: varios nodos actuan como hub con 3 a 8 toques cada uno, todos D, sin fundir
todavia: `busca_el_riesgo_antes_de_que_te_busque` toca 8 pares del tramo (D los ocho),
`que_hacer_con_un_riesgo_nuevo` toca 7 (D los siete), `el_riesgo_cambia_con_el_tiempo` toca 6 (D
los seis), `amenaza_y_oportunidad` y `caza_las_oportunidades_no_solo_amenazas` tocan 5 cada uno
(D todos). Ningun racimo propio abierto todavia; el mas cercano a fundir es el par 3.262 (ver
discutibles abajo). Figura candidata anotada sin pedir doctrina (3.276): un patron de plan de
contingencia generalizado aplicado despues a un subconjunto mas severo con requisito de
resiliencia mas duro, sin fundir; se nombra para reconocerla si se repite.

## LOS DISCUTIBLES MARCADOS para la relectura ciega (marcados ANTES de saber si acierto)

**Verificacion previa a la publicacion (fija desde ahora):** marcas fuertes contadas en el
archivo del tramo 3.201-3.300 (cadena literal "DISCUTIBLE MARCADO fuerte"): **DOS** (3.257,
3.262). Filas de la tabla siguiente: **DOS**. Lista identica. Conjuntos iguales, verificado.

| puesto | clase | por donde puede caer |
|---:|---|---|
| **3.257** | D | como_sabes_que_tu_metodo_sirve contra tu_gestion_de_riesgo_funciona (risk_management), sim_tit 75,7 el mas alto del checkpoint, con arista; los dos comparan predicciones de riesgo contra la realidad para juzgar el metodo; quien no separe crear-el-registro (paso propio del primero, la materia prima de la comparacion) de auditar-y-mejorar-en-cada-ciclo (paso propio del segundo) dira A |
| **3.262** | D | el_riesgo_cambia_con_el_tiempo contra manten_viva_tu_lista_de_riesgos (risk_management); el entregable del segundo dice literalmente "el mismo registro" que describe el primero; quien no verifique que el segundo NUNCA pregunta por los riesgos que BAJARON (que el primero si marca explicitamente en su paso 3) dira A por el fraseo casi identico del entregable, olvidando que el entregable es prueba negativa, nunca positiva |

**Marca simple, fuera del conjunto fuerte pero declarada:** 3.293 (cuan_probable_y_cuanto_doleria
contra la_matriz_de_colores_te_engana, D, comparten la tesis de reemplazar el color por cifras
honestas de probabilidad/dano, pero cada uno ataca el problema desde un angulo propio: el primero
trae una auditoria de consistencia entre etiquetas y una excepcion para lo improbable-catastrofico
que el segundo no tiene, el segundo trae la critica tecnica de no multiplicar las casillas como si
fueran numeros que el primero no menciona).

**Patron del checkpoint:** por primera vez en la campana, un checkpoint entero de cien pares no
produjo ninguna A. Los dos discutibles fuertes son del dominio nuevo `risk_management`, no de
`quality`: el filo dominante ya no es "nucleo tematico compartido con sim_tit alto pero pasos
propios" (el patron de los checkpoints 6, 7 y 8), sino "dos practicas del mismo libro que
describen el mismo ciclo de vida del riesgo en fases distintas, secuenciales, con el paso
fundacional o el paso de excepcion faltante en uno de los dos lados".

## PENDIENTES DE DOCTRINA y PREGUNTAS (regla 9: lo que no puedo medir, lo traigo)

- **NO hubo PENDIENTE DE DOCTRINA que pida regla nueva.** Los ocho arreglos de la TAREA 1, los
  100 pares del cribado, el cierre de `quality` y la apertura de `risk_management` se resolvieron
  con reglas ya escritas.
- **PENDIENTE DE MEDICION acotado (TAREA 1.7):** de los 384 A ciegos anteriores al puesto 2.127,
  quedan **365 sin verificar** para el contador de fusiones mutuas (17 ya cubiertos por el barrido
  original, 19 leidos y descartados esta vuelta). Cifra dicha, no laguna vaga.
- **PREGUNTA 2:** sigue cerrada, sin novedad.
- **PREGUNTA 3:** cierra ABIERTA con el dominio `quality`, sin oportunidad de resolverse aqui; se
  trae la pregunta de si reaparece un ejemplar equivalente en otro dominio.
- **PREGUNTA 4:** cierra como figura reconocida en `quality` (32 casos), reaparece en
  `risk_management` (4 casos, declarados como reaparicion).
- **PREGUNTA 5:** cierra como figura reconocida en `quality`, sin novedad.
- **Figura candidata sin doctrina (risk_management, 3.276):** plan de contingencia generalizado
  aplicado despues a un subconjunto mas severo del mismo riesgo, con un requisito de resiliencia
  mas duro, sin fundir. Se nombra para reconocerla si se repite en la cola del dominio nuevo.
- **Senal del idioma y perdidas de nombre:** sin aparicion nueva entre el 3.001 y el 3.300,
  declarado explicitamente (no por omision) para que no se lea como figura desaparecida.
