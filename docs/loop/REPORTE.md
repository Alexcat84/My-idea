# REPORTE del ejecutor del bucle, vuelta 8 (checkpoint 3.200)

**Sesion ejecutora (Sonnet 5). Fecha de reloj: 13 ago 2026. Corte del cribado: puesto 3.200 de
3.388.** Rama activa: `bucle`. Hash de referencia para el estado del cribado (marcador, archivo):
`18f1d09b` (checkpoint 3.200). El commit de este propio reporte y del informe quedara por encima
en la rama; si se cita un hash "final" antes de comitear el reporte, ese hash queda superado por
el commit del reporte, el mismo patron que dejaron anotado las vueltas 6 y 7.

## Hash y rutas

- **Archivo del cribado:** `docs/INTRA_DOMINIO_VEREDICTOS.jsonl` en **3.200 lineas exactas**,
  puestos 1 a 3.200, **cero huecos (set 1..3200 completo), cero duplicados de puesto y cero pares
  duplicados** (nodo_a/nodo_b/dominio), verificado con `python scripts/recomputar_marcador.py
  3200`.
- **Rutas tocadas esta vuelta:** `docs/INTRA_DOMINIO_VEREDICTOS.jsonl` (100 veredictos nuevos,
  3.101 a 3.200, mas una correccion sobre un puesto ya registrado: 2.630 de A a D con tachado sin
  borrar), `docs/INTRA_DOMINIO_INFORME.md` (secciones 93 a 97 con correcciones en cascada
  tachadas sin borrar, seccion 98 nueva completa), `docs/loop/REPORTE.md` (este archivo).
  `docs/plan/` NO se toco, como manda el modo de cierre. Scripts auxiliares usados, sin crear
  ninguno nuevo: `scripts/volcar_pares.py`, `scripts/recomputar_marcador.py`,
  `scripts/_registrar_lote.py`. Cuatro lotes temporales (`docs/loop/_lote_*.jsonl`) se crearon y
  se borraron en la misma vuelta tras registrarse; ninguno quedo en el repo.
- **Commits de la vuelta:** `9c7eab96` (TAREA 1 completa: recuento del contador de fusiones
  mutuas, correccion del 2.630, tres cifras publicadas corregidas, cribado 3.101-3.125),
  `5603ee40` (cribado 3.126-3.155), `b703adcc` (cribado 3.156-3.170), `53782609` (cribado
  3.171-3.185), `18f1d09b` (cribado 3.186-3.200, checkpoint 3.200).

## TAREA 1: registros, recuento y relectura conjunta

### 1.1 Recuento del contador de fusiones mutuas: de DIECINUEVE a VEINTISIETE

Recorridas las 3.100 razones existentes al empezar la vuelta con el criterio adjudicado en el
acta vuelta 7 (par A que declara el mismo acto sin dominancia, y que no es reformulacion
transitiva de un cumulo ya contado). Metodo declarado con su limite: barrido `grep` de "mutua"
(57 apariciones) y de "ninguno domina"/"dos sentidos"/"sin dominancia" (33 apariciones en clase
A) sobre el archivo entero, mas lectura citada de cada hit; **limite explicito**: el propio 2.127
(primer caso de la serie) no usa ninguna de esas palabras, asi que el barrido por palabra clave
no prueba ausencia completa antes del 2.127. Esa zona queda **PENDIENTE DE MEDICION** (no de
doctrina) para quien retome el barrido con mas presupuesto; registrado en la seccion 98.1 del
informe, no adivinado.

**Los ocho candidatos del acta, verificados uno por uno con cita** (2.673, 2.760, 2.762, 2.773,
2.780, 2.787, 2.816, 2.825): los ocho pasan el criterio (a) y (b), con la cita exacta de cada uno
en 98.1. **Las tres exclusiones del acta reverificadas** (2.736, 2.766, 2.800): correctas, siguen
fuera. **Once hits mas del barrido amplio**, todos verificados y correctamente fuera (2.253,
2.458, 2.571, 2.577, 2.579, 2.601, 2.627, 2.631, 2.639, 2.699, 2.853): la mayoria declaran un
superviviente con dominancia explicita ("sobrevive X, el mas completo"), no "ninguno domina"; el
2.853 es transitividad de cumulo ya contado (no mueve el contador, convencion de la vuelta 3); el
2.571 se defiende explicitamente de leerse como mutua en su propia razon.

**El 2.630 sale de la serie** (relectura conjunta de la TAREA 1.2, corregido a D esta vuelta).

**Serie completa renumerada, VEINTISEIS casos al corte 3.100** (98.1 del informe tiene la tabla
entera con puesto y par). Durante el cribado de esta misma vuelta aparecio un caso nuevo genuino,
el **3.182** (control_del_proceso_del_proveedor =A= planificacion_tecnologica_conjunta, tres
pasos casi verbatim compartidos), que se declara en su propio veredicto como caso nuevo y se
suma a la serie: **el contador queda en VEINTISIETE al corte 3.200**.

**Correccion declarada** en las secciones donde vivia la cifra vieja, tachada sin borrar y
apuntando a donde vive el recuento (98.1): 93.3, 94.4 (con el detalle de los cinco casos que caen
en ese tramo, 2.760/2.762/2.773/2.780/2.787), 95.4 (con el detalle del 2.816/2.825), 96.4 y 97.4.

### 1.2 Relectura conjunta del 2.630: corregido de A a D

**El par 2.630 (`conciencia_calidad` contra `quality_awareness_crosby`) pasa de A a D.** El caso
del auditor se sostuvo verificado contra el grafo: el 3.067 (`conciencia_de_calidad_2` contra el
MISMO `quality_awareness_crosby`) lee los mismos dos pasos de `quality_awareness_crosby`
(registrar mediciones desde el inicio, evitar amenazas) como "pasos enteros propios", y el 2.630
los leia como "tactica compartida" para declarar identidad; no se puede leer el mismo contenido
de las dos formas. `quality_awareness_crosby` es D contra los ocho demas nodos que lo tocan en el
archivo; el 2.630 era su unica A. El `entregable_esperado` desempata tambien (TAREA 1.4d de la
propia vuelta): "Programa de comunicacion interna con supervisores capacitados" contra "Registro
inicial de mediciones", artefactos distintos. Contrapeso del auditor registrado y respetado: el
2.552 (`conciencia_calidad` =A= `conciencia_de_calidad_2`) no se reabre; la correccion solo le
quita un miembro y una unidad al contador de mutuas. Tachado sin borrar en el jsonl; **efecto en
cascada arrastrado a las cinco secciones del informe donde aparecia la cifra vieja** (93, 94, 95,
96, 97): A baja un escalon en cada corte desde el 2.700 en adelante. Detalle completo en 98.2.

### 1.3 Tres cifras publicadas que no calzaban: corregidas

a) **96.1 y 96.3** no habian arrastrado la correccion del 2.931 (declarada en la propia vuelta 7,
   seccion 97.2, pero nunca aplicada de vuelta a la 96). Corregidas ahora con tachado en cascada
   junto con la del 2.630: 96.1 de A 578/D 2.326 a A 576/D 2.328 (dos escalones, uno por cada
   correccion); 96.3 de quality 124 A/21,1 % a 122 A/20,7 %; el tramo 2.926-2.950 de 3 A a 2 A.
b) **97.3 comparaba contra la cifra muerta** ("baja desde 21,1 % al corte 3.000"): corregido a
   "baja desde 20,7 % al corte 3.000 corregido" (el valor final tras las dos correcciones).
c) **La precision "tres A" a "dos A"** en el tramo nuevo de la 97.3: corregida, quedan solo el
   3.012 y el 3.064 como A del tramo 3.001-3.100; el 2.917 era de la tanda anterior.

Las tres correcciones con tachado sin borrar, comando declarado (`recomputar_marcador.py` a cada
corte afectado) y apuntando a donde vive cada una. Detalle completo verificable seccion por
seccion en `docs/INTRA_DOMINIO_INFORME.md`.

### 1.4 La pregunta sobre REPITE: adjudicada, sin doctrina nueva

Las cuatro partes de la adjudicacion del acta vuelta 7 se aplicaron en toda la tanda nueva: (a)
la transitividad no compone si algun eslabon es contencion; (b) manda el texto del eslabon, no su
etiqueta ("REPITE" no es salvoconducto ni condena); (c) cuando la cadena y la lectura directa
discrepan, manda la lectura directa; (d) el `entregable_esperado` desempata tambien la identidad,
no solo la contencion. **Aplicacion mas visible esta vuelta:** la relectura del 2.630 (1.2) usa
exactamente el punto (b), y el 3.165/3.182/3.173 usan el punto (d) para decidir con el entregable
cuando el contenido solo era casi identico. Ningun caso nuevo de "REPITE historico" se invoco
como eslabon de transitividad sin pasar primero por la disciplina de la cita.

### 1.5 Lo verificado y en verde (no se toco)

Los tres pares que se quedaron en D en la vuelta 7 (3.031, 3.067, 3.095) no se reabrieron. Los
`scripts/recomputar_marcador.py` y `scripts/_registrar_lote.py` siguen aprobados y se usaron con
su comando declarado en cada paso.

## TAREA 2: cribado 3.101 a 3.200 (100 pares nuevos)

### Marcador recomputado del archivo (corte 3.200, cero huecos, cero duplicados, comando
`python scripts/recomputar_marcador.py 3200`)

| clase | conteo | porcentaje |
|---|---:|---:|
| A | **580** | 18,1 % |
| B | 89 | 2,8 % |
| C | 7 | 0,2 % |
| D | **2.524** | 78,9 % |

Contra el checkpoint 3.100 corregido (A 578, D 2.426): **+2 A y +98 D** en los 100 pares nuevos
de 3.101 a 3.200.

### Tasa por dominio (corte 3.200)

| dominio | n | A | tasa |
|---|---:|---:|---:|
| core | 1.445 | 344 | 23,8 % |
| health_safety | 192 | 45 | 23,4 % |
| **quality** | **789** | **126** | **16,0 %** |
| environmental | 170 | 29 | 17,1 % |
| franquicias | 148 | 18 | 12,2 % |
| exportacion | 130 | 15 | 11,5 % |
| entrega | 171 | 2 | 1,2 % |
| compras | 155 | 1 | 0,6 % |

`quality` sigue bajando (18,0 % al corte 3.100 corregido, a 16,0 % al corte 3.200) por el mismo
motivo de los checkpoints anteriores: el cuerpo del dominio sigue entregando su piso, ahora con
dos A en cien pares. Quedan **188 pares** hasta el 3.388: quality 55 (hasta el 3.255),
risk_management 106, seguridad_digital 27.

### Vara por tramo de 25 (quality, 3.101-3.200, cuatro tramos)

| tramo | n | A | tasa |
|---|---:|---:|---:|
| 3.101-3.125 | 25 | 0 | 0,0 % |
| 3.126-3.150 | 25 | 0 | 0,0 % |
| 3.151-3.175 | 25 | 1 | 4,0 % |
| 3.176-3.200 | 25 | 1 | 4,0 % |

**El cuerpo sigue en el piso bajo**, con dos tramos en 0,0 % exacto (el segundo consecutivo desde
el 2.976-3.000) y dos en 4,0 %. Las dos A del tramo (3.165 por contencion, 3.182 por fusion mutua
nueva) son casos aislados de lectura directa, no cumulos nuevos: cada una se sostiene en su
propia comparacion paso por paso, no en cadena. **No forcé A para compensar el piso ni D para
sostener la tendencia**: cada D de este checkpoint tiene su comparacion de pasos enteros propios
escrita en la razon, y cite el `entregable_esperado` en todos los casos de alta similitud de
titulo o contenido antes de decidir (3.121, 3.147, 3.148, 3.165, 3.173, 3.176, 3.182).

### Las dos A del tramo nuevo (3.101-3.200), por su mecanismo

| puesto | mecanismo |
|---:|---|
| **3.165** | A por contencion, sim_tit 75,9 (el mas alto del checkpoint): los cinco pasos de `evaluacion_organizacional_calidad` caben enteros dentro de `evaluacion_riesgo_calidad_organizacional`, que ademas trae equipo/roles, objetivos, plan de comunicacion, pre-evaluacion y puntaje formal por categoria. Superviviente el procedimiento mas completo. No mueve el contador de mutuas (es contencion). |
| **3.182** | A por fusion mutua NUEVA: `control_del_proceso_del_proveedor` y `planificacion_tecnologica_conjunta` comparten tres pasos casi verbatim (solicitar plan de control con SPC al proveedor, clasificar la seriedad de los defectos, estandarizar metodos de prueba entre proveedor y comprador) y cada uno anade lineas propias sin que ninguno domine. Barrido de familia limpio (ningun eslabon previo con A). Mueve el contador de VEINTISEIS a VEINTISIETE. |

Ninguna de las dos abre figura de cumulo nuevo mas alla de si misma; la 3.182 SI abre un numero
nuevo en el contador de mutuas, declarado explicitamente en su propio veredicto como manda la
TAREA 2 del encargo.

### Familias del 9.3 al dia, con su especie de ganador (corte 3.200)

| familia | novedad de este corte | especie |
|---|---|---|
| **fusion mutua** | un caso nuevo, el 3.182 | contador **VEINTISIETE**, serie completa en 98.1 |
| **contencion por procedimiento mas completo** | figura nueva reconocida (3.165): un nodo cabe entero dentro de un procedimiento mas formal y completo del mismo acto | siempre A, superviviente el mas completo, entregables compatibles (no distintos, a diferencia de la ficha vs mapa) |
| la **capacidad del proceso, SIN ACTO** | extiende con seis pares mas de esta tanda (3.130, 3.141, 3.149, 3.152, 3.200), sim_tit hasta 67,4 sin fundir | sigue **SIN ACTO**, la familia mas grande del dominio que nunca funde |
| **ficha nombrada dentro del paso de otro nodo** | figura mas frecuente del checkpoint: nueve casos nuevos (3.103, 3.107, 3.114, 3.118, 3.156, 3.169, 3.175, 3.186, 3.197, 3.200) | siempre D, veintiuno acumulados desde el 2.956 |
| la **distincion comun/especial POR DERECHO** contra **responsabilidad gerencial** | frontera confirmada de nuevo (3.113) | **PREGUNTA 3 sigue ABIERTA**, sin resolverse en este tramo |
| **hubs que no funden con sus vecinos pese al sim_tit alto o la arista** | `concepto_haciendo_la_calidad_cierta` D contra siete vecinos distintos en la sesion; `gestion_estrategica_de_calidad_sqm` D contra cuatro; `planificacion_calidad_crosby` D contra tres | doctrina 9.24/9.25 confirmada repetidamente |
| **trampa del identificador con sim_tit muy alto** | 3.176 (facilitador contra lider de equipo, sim_tit 76,7, D) y 3.165 (sim_tit 75,9, A) | el sim_tit alto no predice la clase; hay que leer los pasos |
| **breakthrough/RCCA/DMAIC** | frontera confirmada de nuevo (3.139) | **POR ELEGIR**, sin cambio de cumulo |

## LOS DISCUTIBLES MARCADOS para la relectura ciega (marcados ANTES de saber si acierto)

| puesto | clase | por donde puede caer |
|---:|---|---|
| **3.121** | D | estructura_reporte_dual_estadistico contra organizacion_liderazgo_estadistico; comparten el nucleo del cumulo del 2.891 (lider estadistico con reporte dual); quien pese ese nucleo sobre los dos pasos enteros propios de cada lado (exigir dominio real; mecanismos de resolucion de diferencias) dira A |
| **3.147** | D | concepto_haciendo_la_calidad_cierta contra concepto_quality_is_free, con arista y sim_tit 56,2; quien lea la tesis del libro y el concepto de apertura como el mismo argumento sin distinguir definicion de contabilidad de costos dira A |
| **3.148** | D | dia_cero_defectos contra zero_defects_concepto; entregables parecidos (los dos "un dia de lanzamiento realizado") y comparten el paso de marcar el dia; quien no separe el evento del acto mas amplio de fijar el estandar (eliminar AQL, compromiso escrito) dira A |
| **3.165** | A | evaluacion_organizacional_calidad contra evaluacion_riesgo_calidad_organizacional, sim_tit 75,9 el mas alto del checkpoint; quien no verifique que los cinco pasos del primero caben enteros en el segundo dira D por ver "solo" un puntaje de mas |
| **3.173** | D | autocontrol_planificacion_servicio contra autocontrol_y_controlabilidad, mismo marco teorico de Juran (las tres condiciones del autocontrol) y entregables casi identicos (los dos "checklist de autocontrol"); quien pese el nucleo compartido sobre los pasos enteros propios (documentar procedimientos y mantenimiento preventivo contra el checklist formal y la pregunta de controlabilidad) dira A |
| **3.176** | D | rol_facilitador_equipos_mejora contra rol_lider_equipo_calidad, sim_tit 76,7, el mas alto del checkpoint entero; trampa del identificador por el titulo comun "Rol del X en Equipos de Mejora"; quien no lea que son dos roles distintos del mismo equipo dira A |
| **3.182** | A | control_del_proceso_del_proveedor contra planificacion_tecnologica_conjunta; tres pasos casi verbatim compartidos; quien pese las lineas propias de cada lado (tareas especiales/estandares sensoriales contra acuerdo de requisitos/trazabilidad de lotes) como pasos enteros que rompen la fusion dira D |

**Patron del checkpoint:** de los siete discutibles fuertes, cinco son D con nucleo compartido
fuerte (3.121, 3.147, 3.148, 3.173, 3.176) y dos son A verificadas con cita exacta de la
contencion o la fusion (3.165, 3.182). El filo dominante sigue siendo "nucleo tematico compartido
con sim_tit alto, pero pasos enteros propios en ambos lados", el mismo patron de los checkpoints
6 y 7.

## PENDIENTES DE DOCTRINA y PREGUNTAS (regla 9: lo que no puedo medir, lo traigo)

- **NO hubo PENDIENTE DE DOCTRINA que pida regla nueva.** Todos los 100 pares del tramo, las dos
  correcciones de la TAREA 1 y el recuento del contador se resolvieron con reglas ya escritas.
- **PENDIENTE DE MEDICION** (no de doctrina, declarado en 98.1 y en la seccion 1.1 de arriba): el
  barrido por palabra clave del contador de fusiones mutuas no prueba ausencia completa antes del
  puesto 2.127, porque el propio 2.127 no usa ninguna de las palabras clave del barrido. Una
  re-derivacion completa leyendo los 580 veredictos A uno por uno no se hizo esta vuelta por
  proporcion con el resto del encargo. Lo traigo como pregunta, sin adivinar la respuesta.
- **PREGUNTA 2, Consejo de Calidad: sigue resuelta en su origen**, sin novedad este tramo.
- **PREGUNTA 3, sub-cumulo de la responsabilidad gerencial: sigue ABIERTA**, confirmada de nuevo
  por lectura directa en el 3.113 (la distincion es la regla de decision, la responsabilidad
  gerencial es la ejecucion), sin fundirse. Anotado, no dictado.
- **PREGUNTA 4, ficha nombrada dentro del paso: sigue como figura reconocida**, con nueve casos
  mas en este checkpoint (veintiuno acumulados). No pide doctrina nueva.
- **PREGUNTA 5, planificar contra ejecutar: sigue como figura reconocida**, sin casos nuevos este
  tramo (el 3.148 se resolvio por el mismo filo pero se registro como su propia figura, "acto mas
  amplio contra evento", ver mecanismo del 3.148 arriba).
- **FIGURA NUEVA, contencion por procedimiento mas completo (3.165):** cuando dos nodos describen
  el mismo acto y uno es una version mas formal/completa del otro (trae equipo, objetivos, plan
  de comunicacion, ademas de todo lo que el otro tiene), funde por contencion con el mas completo
  como superviviente, **incluso si el entregable del superviviente anade una pieza como un
  puntaje formal**, porque el entregable base sigue siendo el mismo tipo de artefacto. Se
  distingue de la ficha-vs-mapa porque aqui NINGUN paso del nodo menor queda fuera; en la
  ficha-vs-mapa, el mapa siempre trae pasos enteros que la ficha no cubre. La vara existente
  (paso entero, entregable) ya la cubre; no pide doctrina nueva, pero merece nombrarse porque
  puede repetirse en la cola.
