# REPORTE del ejecutor del bucle, vuelta 10 (checkpoint 3.388, CIERRE DE LA FASE I)

**Sesion ejecutora (Sonnet 5). Fecha de reloj: 13 ago 2026. Corte del cribado: puesto 3.388 de
3.388, LA COLA ESTA AGOTADA.** Rama activa: `bucle`. El hash de referencia para el estado final
del cribado (marcador, archivo) queda fijado por el ultimo commit de esta vuelta, `1c07d53a`
(cribado 3.362-3.388, cierre de `seguridad_digital` y de la Fase I); el commit de este propio
reporte queda por encima en la rama, mismo patron dejado anotado por las vueltas 6 a 9.

## Hash y rutas

- **Archivo del cribado:** `docs/INTRA_DOMINIO_VEREDICTOS.jsonl` en **3.388 lineas exactas**,
  puestos 1 a 3.388, **cero huecos (set 1..3388 completo), cero duplicados de puesto y cero pares
  duplicados** (nodo_a/nodo_b/dominio), verificado con `python scripts/recomputar_marcador.py
  3388`.
- **Rutas tocadas esta vuelta:** `docs/INTRA_DOMINIO_INFORME.md` (cuatro correcciones declaradas
  de la TAREA 1 dentro de las secciones 98 y 99, seccion 99.11 nueva, seccion 100 nueva de cierre
  de fase), `docs/INTRA_DOMINIO_VEREDICTOS.jsonl` (88 veredictos nuevos, 3.301 a 3.388, todos sobre
  puestos nunca antes registrados), `docs/loop/REPORTE.md` (este archivo). `docs/plan/` NO se toco,
  como manda el modo de cierre. Scripts auxiliares usados, sin crear ninguno nuevo:
  `scripts/volcar_pares.py`, `scripts/recomputar_marcador.py`, `scripts/_registrar_lote.py`.
  Cuatro lotes temporales (`docs/loop/_lote_a.jsonl` a `_lote_d.jsonl`) y dos dumps temporales
  (`docs/loop/_tmp_dump.txt`, `_tmp_entregables.txt`) se crearon y se borraron en la misma vuelta
  tras usarse; ninguno quedo en el repo.
- **Commits de la vuelta:** `8e41d120` (TAREA 1 completa: cuatro correcciones de registro),
  `5005cbcf` (cribado 3.301-3.350, cincuenta D), `086dba0a` (cribado 3.351-3.361,
  CIERRA `risk_management` en 106 pares con CERO A), `1c07d53a` (cribado 3.362-3.388, ABRE Y CIERRA
  `seguridad_digital`, tres A, CIERRA LA FASE I).

## TAREA 1: cuatro correcciones de registro, la primera del auditor

Las cuatro se resolvieron con reglas de correccion ya escritas (tachar sin borrar, correccion
declarada), ninguna pidio doctrina nueva. Detalle completo con cita en
`docs/INTRA_DOMINIO_INFORME.md` (dentro de 98.1, 98.2, 98.4, 99.3 y la nueva 99.11), resumen aqui.

### 1.1 La racha mas larga, verificada por mi mismo, no copiada del encargo

El encargo traia la cifra medida por el auditor (el error, segun su propia acta, era mio en la
vuelta anterior): recomputada por mi mismo sobre el archivo entero en tramos de 25 desde el puesto
1 (no copiada), confirmo exactamente lo que el encargo adelanto: SEIS tramos en 0,0 % consecutivos,
1.626-1.775 (150 pares); CINCO tramos, 26-150 (125 pares); CUATRO tramos, 3.201-3.300 (100 pares);
TRES tramos, 3.076-3.150 (75 pares), la cuarta mas larga y no la primera como se habia publicado.
En pares corridos sin ninguna A, sin alinear a tramo: 173 pares (1.603-1.775), 152 (4-155), y la
racha viva al corte 3.300 de 118 pares (3.183-3.300), abierta. **Corregido en 98.4 y 99.3 del
informe con correccion declarada, dejando escrita la adjudicacion: una glosa comparativa sobre "la
campana" se mide sobre la campana entera o se acota al tramo medido (regla 9 aplicada al
superlativo).** Con el cierre de esta vuelta el mapa cambio de nuevo (ver TAREA 2 mas abajo: el
3.201-3.300 se extendio a 3.201-3.350, empatando el primer lugar).

### 1.2 La cita de consulta del entregable, corregida a 31 de 100

El reporte de la vuelta 9 afirmaba que la adjudicacion del entregable como prueba negativa "se
aplico explicitamente... los entregables consultados en cada par de 3.201 a 3.300". **Verificado
con el instrumento: 31 de las 100 razones del tramo mencionan la palabra "entregable" en cualquier
forma, no las 100.** La afirmacion vivia solo en `docs/loop/REPORTE.md` (git, ya superado), asi que
la correccion declarada durable queda en la seccion 99.11 nueva del informe, con la regla fijada
hacia adelante: el entregable se cita en la razon antes de declarar A, antes de declarar
contencion, y en todo par marcado como discutible de cualquier grado; en los demas no es
obligatorio. **Aplicada esta vuelta desde el primer par:** en el tramo 3.301-3.388 cite el
`entregable_esperado` explicitamente en las tres A (3.363, 3.364, 3.367) y en los ocho discutibles
marcados (fuertes y simples), como exige la regla; no lo cite en el resto de los 77 pares D sin
discutible, porque no era obligatorio.

### 1.3 El encabezado de la serie de mutuas, corregido a veintisiete

La 98.1 titulaba la tabla "VEINTISEIS casos" mientras la tabla numeraba hasta 27 y el parrafo de
cierre ya decia "AL CORTE 3.200 ES VEINTISIETE". Corregido con tachado: **VEINTISIETE**, con la
aritmetica dicha (diecinueve menos un retirado, el 2.630, mas nueve anadidos: los ocho de 98.1 mas
el 3.182).

### 1.4 La nomina de `quality_awareness_crosby`, corregida a nueve toques sin el 2.789

La 98.2 citaba el 2.789 como un toque de `quality_awareness_crosby` que da D. **El 2.789 NO TOCA
ese nodo** (es `conciencia_calidad` contra `entrenamiento_supervisores_calidad`, un par distinto).
Verificados con el instrumento los toques reales: NUEVE (2.630, 2.648, 2.696, 2.939, 3.040, 3.067,
3.089, 3.097, 3.251), todos D. Lo que estaba mal era la nomina, no el veredicto: el 2.630 sigue
siendo su unica A historica, ya corregida a D, y sigue cerrado sin reabrirse.

### 1.5 Lo verificado y en verde, no se toco

El marcador entero al corte 3.300, las nueve tasas, la frontera 3.255/3.256, los cuatro hubs de
`quality` domino-wide, los treinta y dos de la ficha nombrada en `quality`, los 28 SIN ACTO, el
contador de mutuas en veintisiete antes de esta vuelta, los diecinueve candidatos leidos y el
pendiente en 365 A, el conjunto fuerte de discutibles del checkpoint 3.300 (3.257, 3.262): todo
verificado por el auditor, nada de esto se reabrio. Scripts usados sin crear ninguno nuevo:
`scripts/volcar_pares.py`, `scripts/recomputar_marcador.py`, `scripts/_registrar_lote.py`.

## TAREA 2: cribado 3.301 a 3.388 (88 pares), CIERRE de `risk_management`, APERTURA Y CIERRE de
## `seguridad_digital`, CIERRE DE LA FASE I

### Marcador recomputado del archivo (corte 3.388, cero huecos, cero duplicados, comando
`python scripts/recomputar_marcador.py 3388`)

| clase | conteo | porcentaje |
|---|---:|---:|
| A | **583** | 17,2 % |
| B | 89 | 2,6 % |
| C | 7 | 0,2 % |
| D | **2.709** | 80,0 % |

Contra el checkpoint 3.300 (A 580, D 2.624): **+3 A y +85 D** en los 88 pares nuevos de 3.301 a
3.388. Las tres A nuevas son todas de `seguridad_digital` (3.363, 3.364, 3.367); `risk_management`
cerro sus ultimos 61 pares sin ninguna.

### Tasa por dominio (corte 3.388, DIEZ dominios, catalogo entero cribado)

| dominio | n | A | tasa |
|---|---:|---:|---:|
| core | 1.445 | 344 | 23,8 % |
| health_safety | 192 | 45 | 23,4 % |
| quality | 844 | 126 | 14,9 % (CERRADO en el 3.255) |
| environmental | 170 | 29 | 17,1 % |
| franquicias | 148 | 18 | 12,2 % |
| exportacion | 130 | 15 | 11,5 % |
| entrega | 171 | 2 | 1,2 % |
| compras | 155 | 1 | 0,6 % |
| **risk_management** | **106** | **0** | **0,0 % (CERRADO en el 3.361)** |
| **seguridad_digital** | **27** | **3** | **11,1 % (ABRE Y CIERRA en el 3.388, catalogo pequeno, tasa con cautela)** |

**Suma de verificacion:** 1.445+192+844+170+148+130+171+155+106+27 = **3.388**, calza con el total
del archivo. **Los DIEZ dominios del catalogo estan cribados. LA COLA ESTA AGOTADA.**

### La vara por tramo del tramo nuevo y la tabla de rachas RECOMPUTADA SOBRE EL ARCHIVO ENTERO

**Vara por tramo de 25 desde el 3.276 hasta el cierre (comando propio sobre
`docs/INTRA_DOMINIO_VEREDICTOS.jsonl`, reproducible, no un script nuevo: una pasada de conteo por
tramo declarada aqui con su formula: para cada tramo de 25 puestos, contar A y dividir por el
tamano del tramo):**

| tramo | pares | A | tasa |
|---|---:|---:|---:|
| 3.276-3.300 | 25 | 0 | 0,0 % |
| 3.301-3.325 | 25 | 0 | 0,0 % |
| 3.326-3.350 | 25 | 0 | 0,0 % |
| 3.351-3.375 | 25 | 3 | 12,0 % |
| 3.376-3.388 | 13 | 0 | 0,0 % |

Las tres A del checkpoint caen todas en el tramo 3.351-3.375 (3.363, 3.364, 3.367), las tres
primeras del dominio `seguridad_digital`.

**RACHAS DE TRAMOS DE 25 EN 0,0 % RECOMPUTADAS SOBRE EL ARCHIVO ENTERO AL CORTE 3.388 (verificacion
propia, no copiada del encargo anterior):**

| lugar | tramos | rango | pares |
|---:|---:|---|---:|
| 1 (empate) | SEIS | 1.626-1.775 | 150 |
| 1 (empate) | SEIS | **3.201-3.350 (NUEVO, crecio de cuatro a seis con esta vuelta)** | 150 |
| 3 | CINCO | 26-150 | 125 |
| 4 | TRES | 3.076-3.150 | 75 |

La racha del 3.201-3.300 (cuatro tramos, corregida en la TAREA 1.1) **se extendio a SEIS tramos,
3.201-3.350**, porque el cribado de esta vuelta anadio dos tramos completos mas en 0,0 % (3.301-
3.325 y 3.326-3.350) antes de que aparecieran las tres A de `seguridad_digital`. **Ahora EMPATA en
primer lugar con la racha 1.626-1.775**, ambas de seis tramos y 150 pares. Se corta en el tramo
3.351-3.375 por las tres A.

**En pares corridos sin ninguna A, sin alinear a tramo (recomputado sobre el archivo entero):**

| lugar | rango | pares |
|---:|---|---:|
| 1 (NUEVO RECORD) | **3.183-3.362** | **180** |
| 2 | 1.603-1.775 | 173 |
| 3 | 4-155 | 152 |
| 4 | 3.065-3.164 | 100 |

**LA RACHA VIVA AL CIERRE DE LA FASE I (corte 3.388): 3.368-3.388, VEINTIUN PARES sin ninguna A,
abierta al corte pero sin mas cola que agotar** (la ultima A de la fase es el 3.367). Esta racha ya
no puede crecer dentro de la Fase I: la cola esta agotada. Queda registrada como el estado final
con el que termina la fase.

### BLOQUE DE CIERRE DE `risk_management` (106 pares, 0 A, 0,0 %, corte 3.361)

**Vara por tramo de los cinco tramos nuevos mas la cola de once:**

| tramo | pares | A | tasa |
|---|---:|---:|---:|
| 3.301-3.325 | 25 | 0 | 0,0 % |
| 3.326-3.350 | 25 | 0 | 0,0 % |
| 3.351-3.361 | 11 | 0 | 0,0 % |

`risk_management` cierra con **CIENTO SEIS PARES, CERO A, 0,0 %**, sin una sola fusion en todo el
dominio desde su apertura en el checkpoint anterior. **AVISO CUMPLIDO, medido y no forzado:** es el
**PRIMER DOMINIO DEL CATALOGO ENTERO QUE CIERRA SIN NINGUNA FUSION**, verificado sobre los nueve
dominios con `python scripts/recomputar_marcador.py 3361` (tabla completa arriba en TASA POR
DOMINIO; el segundo mas bajo es `compras`, 1 A en 155 pares, 0,6 %). No se forzo ninguna A para
romper la cifra redonda ni se forzo ninguna D para sostenerla: cada par de los 106 se decidio con
sus propios pasos enteros, y once de ellos fueron discutibles marcados (uno fuerte, el 3.332, sim_
tit 79.2, la reserva de contingencia contra el plan B por riesgo).

**Resumen de racimos y familias del dominio entero, al cerrar:**

- **Fusion mutua:** CERO casos en todo el dominio. `risk_management` no aporta ningun caso a la
  serie global (que sigue en veintisiete al cerrar este dominio, antes de la apertura de
  `seguridad_digital`).
- **Contencion por procedimiento mas completo:** CERO casos.
- **Ficha nombrada dentro del paso de otro nodo (reaparicion, no continuidad de `quality`):** SEIS
  casos en todo el dominio (3.282, 3.284, 3.285, 3.294 del checkpoint anterior, mas 3.311 y 3.318
  de esta vuelta), verificado con el instrumento (`grep` de la cadena literal sobre el tramo del
  dominio). Siempre D, nunca funde.
- **Figura candidata sin doctrina, anotada en el checkpoint anterior (3.276, plan de contingencia
  generalizado aplicado despues a un subconjunto mas severo):** NO SE REPITIO en el resto del
  dominio. Se queda como caso unico, sin nombrarse figura reconocida (no hay un segundo caso que la
  confirme).
- **Hubs domino-wide, conteo final sobre los 106 pares completos, todos D:**
  `busca_el_riesgo_antes_de_que_te_busque` toca **VEINTE** pares (el hub mas denso de todo el
  dominio), `que_hacer_con_un_riesgo_nuevo` toca **DIECIOCHO**, `amenaza_y_oportunidad` y
  `el_riesgo_cambia_con_el_tiempo` tocan **ONCE** cada uno, `caza_las_oportunidades_no_solo_
  amenazas` y `riesgo_no_es_mala_suerte` tocan **NUEVE** cada uno, `nombra_tus_suposiciones_
  fragiles` y `cuatro_caminos_ante_un_riesgo` tocan **OCHO** cada uno, `deja_de_ignorar_el_riesgo`
  y `vuelve_a_medir_despues_del_susto` tocan **SIETE** cada uno. CERO A en cualquiera de estos
  hubs contra cualquiera de sus vecinos: el dominio es denso en tema compartido (todos giran sobre
  la gestion del ciclo de vida del riesgo del mismo puñado de fuentes) pero cada par retiene pasos
  enteros propios.
- **PREGUNTA 3** (sub-cumulo comun/especial de responsabilidad gerencial, propia de la doctrina de
  calidad de Deming/Crosby/Juran): SIN EJEMPLAR EQUIVALENTE en `risk_management`. El dominio no
  toca la distincion causa comun/especial en ninguno de sus 106 pares. Sigue cerrada abierta, sin
  novedad.
- **PREGUNTA 5** (planificar contra ejecutar): SIN EJEMPLAR EQUIVALENTE en `risk_management`.

### BLOQUE DE CIERRE DE `seguridad_digital` (27 pares, 3 A, 11,1 %, corte 3.388, ABRE Y CIERRA EN
### EL MISMO TRAMO, ULTIMO DOMINIO DEL CATALOGO)

Dominio nuevo de cinco fuentes NIST para pequena empresa (SP1300 Cybersecurity Framework 2.0,
SP1314 Risk Management Framework, SP1318 Protecting CUI/SP800-171 r3, mas "Cybersecurity for Small
Business" y "Getting Started with the NIST Privacy Framework"), sin un solo veredicto intra previo
en el archivo. **NO SE COMPARO ESTA TASA CONTRA NINGUN OTRO DOMINIO** (catalogos distintos, aviso
del encargo) y se declara con la cautela explicita que pide el encargo: **27 pares son un dominio
pequeno, su tasa (11,1 %) no sostiene una comparacion con dominios de cientos de pares.**

**A DIFERENCIA DE `risk_management`, ESTE DOMINIO SI FUNDE, Y DESDE SU PRIMER TRAMO.** Tres A de
veintisiete pares (11,1 %), todas en el rango 3.351-3.375:

- **3.363, A por FUSION MUTUA** (`getting_started_incident_response` =A= `respuesta_incidentes_
  cui`, misma fuente NIST SP1318, sim_tit 87,0, EL SEGUNDO MAS ALTO DE TODA LA COLA RESTANTE segun
  el aviso del encargo): paso 1 casi verbatim en los dos ("designar un responsable business
  champion del plan de respuesta a incidentes"), y verificado que ninguno domina al otro entero
  (uno trae el criterio general de reporte por cualquier ley/regulacion/contrato, el otro trae la
  prueba del plan con ejercicios de mesa/tabletop; ninguna de las dos piezas esta en el otro lado).
  Entregables casi identicos, citados como corroboracion no como prueba (la decision la dan los
  pasos). **MUEVE EL CONTADOR GLOBAL DE FUSIONES MUTUAS DE VEINTISIETE A VEINTIOCHO**, aplicado el
  criterio de la vuelta 7: (a) mismo acto sin dominancia, verificado paso por paso; (b) no es
  reformulacion transitiva de ninguna fusion ya contada (es la primera fusion mutua de
  `seguridad_digital`, un dominio que no comparte nodos con ningun otro).
- **3.364, A por REPITE con superviviente por dominancia** (`getting_started_maintenance` =A=
  `mantenimiento_sistema_cui`, misma fuente, sim_tit 74,6): los cinco pasos de
  `mantenimiento_sistema_cui` tienen contraparte casi verbatim en `getting_started_maintenance`,
  que ademas trae un paso propio (sanitizar/destruir equipos con CUI antes de retirarlos) que el
  nodo nominalmente "de CUI" no tiene. Superviviente: `getting_started_maintenance`. NO mueve el
  contador de mutuas (hay dominancia clara).
- **3.367, A por REPITE con superviviente por dominancia** (`funcion_protect_politica_seguridad`
  =A= `protect_medidas_tecnicas`, distinta fuente, sim_tit 48,1): los seis pasos de
  `protect_medidas_tecnicas` tienen contraparte casi verbatim en `funcion_protect_politica_
  seguridad`, que ademas trae dos pasos propios (redactar la politica con roles, capacitar al
  personal) que el otro no tiene. Superviviente: `funcion_protect_politica_seguridad`. NO mueve el
  contador de mutuas.

**Patron identificado y nombrado para el dominio (figura reconocida con tres casos, no candidata):
NODO GENERAL DE UN CAPITULO INTRODUCTORIO CONTRA NODO ESPECIFICO DEL MISMO DOCUMENTO SOBRE EL MISMO
SUBTEMA.** Los tres A comparten que ambos nodos vienen de guias NIST oficiales para pequena empresa
describiendo la MISMA practica (responder a incidentes, mantener sistemas, proteger tecnicamente)
en dos niveles de resolucion del mismo documento o de documentos hermanos; cuando el nodo
especifico no aporta ningun paso que el general no tenga ya, DOMINA el general (3.364, 3.367);
cuando cada uno aporta una pieza que el otro no tiene, es mutua (3.363).

**El filo opuesto, confirmado en el mismo tramo: FUNCIONES HERMANAS DEL MISMO MARCO NUNCA SON EL
MISMO ACTO POR COMPARTIR PREFIJO**, tal como advertia el encargo. Verificado en TRES pares del CSF
2.0 (seis funciones oficiales: Govern, Identify, Protect, Detect, Respond, Recover), cero solape
literal en cualquiera de los tres:
- **3.370** (`csf_funcion_govern` contra `csf_funcion_identify`, sim_tit 84,4, EL MAS ALTO DE TODA
  LA COLA RESTANTE segun el aviso del encargo): D, entregables distintos (documento de gobernanza
  contra inventario de activos).
- **3.373** (`funcion_recover_restauracion` contra `funcion_respond_plan_incidentes`, sim_tit 51,5,
  funciones secuenciales Respond/Recover del mismo documento): D.
- **3.388** (`csf_funcion_detect` contra `csf_funcion_identify`, sim_tit 75,0, ULTIMO PAR DE LA
  FASE I): D, mismo patron que el 3.370, cierra la fase con la misma confirmacion con la que abrio
  la sospecha.

**Ficha nombrada dentro del paso de otro nodo (reaparicion, no continuidad de `quality` ni de
`risk_management`):** TRES casos nuevos, primera aparicion en el dominio: **3.368**
(`rmf_paso_preparar` dentro del paso "Preparar" de `proceso_rmf_siete_pasos`), **3.372**
(`funcion_identify_inventario_activos` dentro del paso 1 de `csf_funcion_identify`), **3.378**
(`csf_funcion_identify` nombrado condensadamente dentro del paso 1 de `marco_nist_cybersecurity_
framework`). Siempre D, nunca funde.

**Figura nueva del dominio, nombrada sin pedir doctrina (candidata, tres casos ya, mas que
suficiente para reconocerla): PASOS ADYACENTES DE UN MISMO PROCESO FORMAL NUMERADO (el RMF de
siete pasos), CADA UNO SU PROPIA TAREA CON CODIGO PROPIO, NUNCA EL MISMO ACTO.** Tres casos: 3.385
(Seleccionar contra Implementar), 3.386 (Categorizar contra Seleccionar), 3.387 (Implementar contra
Evaluar). Cada paso del RMF consume el resultado del anterior como insumo mencionado, pero ninguno
ejecuta el trabajo del otro. Se nombra para que quien retome un proceso formal numerado similar la
reconozca sin releer desde cero.

**PREGUNTA 3** (comun/especial de calidad): SIN EJEMPLAR EQUIVALENTE en `seguridad_digital`.
**PREGUNTA 5** (planificar contra ejecutar): SIN EJEMPLAR EQUIVALENTE, aunque el patron de "nodo
general contra nodo especifico del mismo documento" (arriba) es un pariente cercano y distinto: no
es planificar-contra-ejecutar, es resumen-contra-detalle del mismo acto ya ejecutado o por
ejecutar.

## LA VERIFICACION FIJA DE DISCUTIBLES antes de publicar la tabla (checkpoint completo 3.301-3.388)

**Marcas fuertes contadas en el archivo del tramo 3.301-3.388 (cadena literal "DISCUTIBLE MARCADO
fuerte", instrumento programatico sobre el jsonl): SEIS** (3.332, 3.363, 3.364, 3.367, 3.370,
3.388). **Filas de la tabla siguiente para el conjunto fuerte: SEIS.** Lista identica. Conjuntos
iguales, verificado. **Marcas simples (cadena "DISCUTIBLE MARCADO" sin "fuerte"): CINCO** (3.327,
3.362, 3.365, 3.376, 3.382), declaradas aparte, fuera del conjunto fuerte. **Esta es la SEGUNDA vez
consecutiva que la verificacion pasa** (la primera fue el checkpoint 3.300, TAREA 1.1 de esa
vuelta); queda fija para todo checkpoint futuro, tal como pedia el encargo.

## LOS DISCUTIBLES MARCADOS para la relectura ciega (marcados ANTES de saber si acierto)

**Conjunto fuerte, SEIS pares:**

| puesto | clase | por donde puede caer |
|---:|---|---|
| **3.332** | D | guarda_un_colchon_de_tiempo_y_dinero contra plan_b_antes_de_necesitarlo (risk_management), sim_tit 79,2 el mas alto del tramo de ese dominio; los dos son preparacion anticipada para cuando un riesgo grave se materialice; quien no separe la RESERVA CUANTITATIVA agregada (tiempo/dinero, sin decir que hacer con cada riesgo puntual) de la ACCION CONCRETA POR RIESGO (que hacer especificamente, sin dimensionar ningun colchon) dira A por el parentesco tematico |
| **3.363** | A | getting_started_incident_response =A= respuesta_incidentes_cui (seguridad_digital), sim_tit 87,0, fusion mutua; quien busque dominancia unidireccional en vez de verificar que CADA lado aporta una pieza que el otro no tiene (el criterio general de reporte de un lado, la prueba con tabletop del otro) podria leerlo como REPITE con superviviente en vez de mutua, o al reves, leer el paso 1 casi identico y declarar REPITE sin ver que ninguno domina entero |
| **3.364** | A | getting_started_maintenance =A= mantenimiento_sistema_cui (seguridad_digital), sim_tit 74,6, REPITE por dominancia; quien no busque el unico paso de diferencia (sanitizar equipos con CUI, presente solo en el nodo general y ausente en el nodo nominalmente "de CUI") podria declarar mutua en vez de dominancia, o D por el nombre "de CUI" sugiriendo contenido especializado que en realidad no esta ahi |
| **3.367** | A | funcion_protect_politica_seguridad =A= protect_medidas_tecnicas (seguridad_digital), sim_tit 48,1 (mas bajo que el par anterior pero el solape de pasos es igual de fuerte); quien se guie solo por el sim_tit moderado sin leer los seis pasos verbatim podria pasarlo de largo como D |
| **3.370** | D | csf_funcion_govern contra csf_funcion_identify (seguridad_digital), sim_tit 84,4 el mas alto de toda la cola restante segun el aviso del encargo; quien funda por el prefijo compartido csf_funcion_ y el sim_tit altisimo, sin comparar los pasos uno por uno, dira A; es la trampa del identificador en su forma mas pura del checkpoint |
| **3.388** | D | csf_funcion_detect contra csf_funcion_identify (seguridad_digital), sim_tit 75,0, ultimo par de la Fase I; misma trampa que el 3.370, con la funcion Detect en vez de Govern |

**Marca simple, fuera del conjunto fuerte pero declarada, CINCO pares:** 3.327
(que_hacer_con_un_riesgo_nuevo contra vuelve_a_medir_despues_del_susto, D, mismo ciclo de vida del
riesgo en fases distintas, entrada contra verificacion posterior), 3.362 (csf_funcion_recover
contra funcion_recover_restauracion, D, sim_sem 0,914 el mas alto del checkpoint entero, misma
funcion CSF descrita por dos guias con contenido genuinamente distinto), 3.365 (csf_funcion_detect
contra funcion_detect_monitoreo_red, D, mismo patron que el 3.362 con la funcion Detect), 3.376
(csf_funcion_protect contra funcion_protect_politica_seguridad, D, solape tematico denso pero con
MFA y contraseñas de fabrica como delta tecnico propio de un lado), 3.382 (fundamentos_gestion_
riesgo contra rmf_paso_preparar, D, el paso Preparar del RMF cubre tres de los cuatro elementos del
ciclo generico pero nunca el elemento de RESPUESTA).

**Patron del checkpoint:** el filo dominante cambio respecto a los tres checkpoints anteriores
(6, 7 y 8 con "nucleo tematico compartido, pasos propios"; el 3.300 con "fases secuenciales del
mismo ciclo de vida sin fundir"). Este checkpoint tiene DOS filos simultaneos y opuestos, uno en
cada dominio: `risk_management` cerro sin ninguna fusion, confirmando que el nucleo tematico denso
compartido por sus hubs NUNCA basta sin pasos enteros compartidos; `seguridad_digital` abrio con
TRES fusiones reales en sus primeros veintisiete pares, todas dentro del patron "nodo general de un
capitulo introductorio contra nodo especifico del mismo documento sobre el mismo subtema", y a la
vez confirmo tres veces que "funciones hermanas del mismo marco oficial" NUNCA son el mismo acto
pese al sim_tit altisimo por prefijo compartido. Los dos filos convivieron en el mismo dominio sin
contradecirse: proximidad de FUENTE Y SUBTEMA puede fundir, proximidad de NOMBRE/PREFIJO de
categorias oficialmente distintas no.

## Estado final de figuras y familias, TODO EL CATALOGO al cierre de la Fase I (corte 3.388)

- **Fusion mutua (contador global, criterio de la vuelta 7):** **VEINTIOCHO** casos (27 al cierre
  del checkpoint anterior, +1 esta vuelta, el 3.363). Reparto por dominio: `quality` aporta 25,
  `franquicias` 1 (2.127), `health_safety` 1 (2.368), `seguridad_digital` 1 (3.363, nuevo).
  `risk_management` aporta CERO. Total de A en el archivo: 583 (`python
  scripts/recomputar_marcador.py 3388`).
- **Ficha nombrada dentro del paso de otro nodo:** `quality` 32 (cerrado, no reabierto),
  `risk_management` 6 (4 del checkpoint anterior mas 2 de esta vuelta, dominio cerrado),
  `seguridad_digital` 3 (dominio cerrado). Siempre D, nunca funde en ningun dominio.
- **La capacidad del proceso, SIN ACTO:** 28 casos en `quality` (cota inferior por barrido, cerrado
  sin novedad). CERO casos nuevos en `risk_management` ni en `seguridad_digital` (verificado con el
  instrumento sobre el tramo 3.301-3.388 completo, cadena "sin acto": cero apariciones). Esta
  familia no cruzo a los dos dominios nuevos.
- **Contencion por procedimiento mas completo:** un solo caso en todo el catalogo, el 3.165
  (`quality`). CERO casos nuevos en `risk_management` ni `seguridad_digital`.
- **Trampa del identificador (sim_tit alto por nombre/prefijo compartido, pasos propios en ambos
  lados):** figura reconocida desde `quality` (3.176), reaparece TRES veces en `seguridad_digital`
  (3.370, 3.373, 3.388), siempre entre funciones hermanas del NIST CSF. Nunca funde.
  **PENDIENTE DE MEDICION nuevo, dicho con su cifra:** no se corrio un barrido exhaustivo de esta
  figura sobre `core`, `environmental`, `exportacion`, `entrega` ni `compras`; el conteo de
  "reconocida" descansa en los casos vistos de pasada en `quality` y `seguridad_digital`, no en un
  censo del catalogo entero.
- **Pasos adyacentes de un proceso formal numerado (figura nueva, nombrada esta vuelta sin pedir
  doctrina):** TRES casos, todos en `seguridad_digital` (3.385, 3.386, 3.387), todos dentro del RMF
  de siete pasos. No se ha visto fuera de `seguridad_digital`.
- **Nodo general de un capitulo introductorio contra nodo especifico del mismo documento (figura
  nueva de `seguridad_digital`, la que SI funde):** TRES casos, los tres A del dominio (3.363,
  3.364, 3.367). Unica figura del catalogo entero que produce fusiones fuera de `quality`,
  `franquicias` y `health_safety`.
- **PREGUNTA 2:** sigue cerrada, sin novedad en ningun dominio de esta vuelta.
- **PREGUNTA 3** (comun/especial de responsabilidad gerencial): cerro ABIERTA con `quality` en el
  checkpoint anterior. Verificado en esta vuelta: SIN EJEMPLAR EQUIVALENTE ni en `risk_management`
  ni en `seguridad_digital`. Queda cerrada abierta para siempre dentro de esta fase (no hay mas
  dominios que cribar).
- **PREGUNTA 4** (ficha nombrada dentro del paso): cerro como figura reconocida en `quality` (32
  casos) y reapareció en `risk_management` (6) y `seguridad_digital` (3), sin cambiar de identidad
  ni de contador entre dominios.
- **PREGUNTA 5** (planificar contra ejecutar): cerro como figura reconocida en `quality`, sin
  ejemplar equivalente en `risk_management` ni `seguridad_digital`.
- **Senal del idioma y perdidas de nombre:** verificado directo sobre los tres A del checkpoint
  (3.363, 3.364, 3.367, el metodo del 99.6: leer las A una por una, no barrido de candidatos):
  ninguna declara perdida de sigla/termino extranjero ni perdida de nombre propio/instrumento con
  nombre pese a que `seguridad_digital` esta lleno de siglas (NIST, CSF, RMF, CUI, MFA, POA&M,
  SSP). **Sin aparicion nueva**, declarado explicitamente. Las cinco denominaciones y las dos
  perdidas de nombre (Amalberti, Taguchi) siguen en su ultimo estado publicado (96.4/97.4/98.5/
  99.6), sin novedad hasta el cierre de la fase.

## PENDIENTE DE MEDICION (repetido con su cifra para que no se pierda al cambiar de fase)

- **Contador de fusiones mutuas, zona ciega anterior al 2.127:** de los 384 A ciegos, quedan
  **365 SIN VERIFICAR** (17 cubiertos por el barrido original de palabra clave, 19 leidos y
  descartados en la vuelta 8). Cifra sin cambio esta vuelta: el barrido de esta vuelta fue sobre
  material nuevo (3.301-3.388), no sobre la zona ciega anterior al 2.127.
- **Trampa del identificador, censo del catalogo entero:** nuevo esta vuelta (ver arriba), no
  corrido fuera de `quality` y `seguridad_digital`.
- **La racha viva sin A al cierre de la Fase I:** 3.368-3.388, veintiun pares. Dato de cierre, no
  proyeccion: no hay mas cola en esta fase para que la racha siga o se corte.

## EL ARCHIVO ESTA EN 3.388 DE 3.388 Y LA COLA ESTA AGOTADA

Verificado con `python scripts/recomputar_marcador.py 3388`: n = 3.388, corte = 3.388, huecos: []
(vacio), duplicados de puesto: 0, pares duplicados (nodo_a, nodo_b, dominio): 0. Los DIEZ dominios
del catalogo (`core`, `health_safety`, `quality`, `environmental`, `franquicias`, `exportacion`,
`entrega`, `compras`, `risk_management`, `seguridad_digital`) suman exactamente 3.388 pares, sin
resto. **NO HAY MAS PARES INTRA-DOMINIO QUE CRIBAR. LA FASE I DEL CRIBADO INTRA-DOMINIO TERMINA
AQUI.**

## DONDE PARO

En el 3.388, con el reporte publicado y `docs/INTRA_DOMINIO_INFORME.md` con la seccion 100 nueva de
cierre de fase. **NO ENTRE A LA FASE II.** El recomputo de OP-U-02 (disparador: puesto 3.388) queda
para el encargo siguiente, despues de que el auditor verifique este cierre. `docs/plan/` sigue en
solo lectura, no se toco ni un archivo suyo esta vuelta. Tuve presupuesto para releer mi propio
tramo antes de publicar: relei los 88 pares completos una segunda vez antes de registrar cada lote
(comparacion paso por paso contra el jsonl fuente, no contra mi propia memoria de la primera
lectura), y volvi a leer literalmente los tres A y los seis discutibles fuertes una tercera vez
antes de escribir este reporte, verificando cada cita de paso contra `dataset/metadata/master_
graph.json` con el mismo comando que usa `volcar_pares.py`.

## Cosas que quedan como preguntas abiertas (regla 9: lo que no puedo medir, lo traigo)

- Las **tres A de `seguridad_digital`** son el hallazgo mas importante de esta vuelta porque
  rompen el patron que `risk_management` acababa de establecer (un dominio nuevo puede cerrar en
  cero). Estan marcadas como discutibles fuertes precisamente porque son las primeras A de un
  dominio sin precedente interno: no hay un cumulo previo contra el cual contrastarlas. Pido
  relectura ciega prioritaria sobre estas tres antes que sobre cualquier D del checkpoint.
- El **9.28 (SIN ACTO)** y la **contencion por procedimiento mas completo** no aparecieron ni una
  vez en 88 pares de dos dominios nuevos. No se si es porque estas dos familias son propias del
  vocabulario de calidad (Deming/Crosby/Juran, con su enfasis en "el proceso" y "el procedimiento
  formal") y no del vocabulario de riesgo/ciberseguridad, o si simplemente no aparecieron todavia
  por azar de la muestra. No lo puedo medir con lo que cribé esta vuelta; lo traigo como
  pregunta para quien tenga mas dominios o mas presupuesto.
- No corri un censo de la "trampa del identificador" sobre `core`, `environmental`, `exportacion`,
  `entrega` ni `compras`. Podria haber mas casos sin marcar en esos dominios. Declarado como
  PENDIENTE DE MEDICION arriba, no como laguna vaga.
