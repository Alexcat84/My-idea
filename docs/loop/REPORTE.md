# REPORTE del ejecutor del bucle, vuelta 3

**Sesion ejecutora (Opus 4.8). Fecha de reloj: 12 ago 2026. Corte del cribado: puesto 2.800
de 3.388.** Rama activa: `bucle`. MODO DE CIERRE en todo: se leyo, se midio y se documento;
cero nodos tocados.

## Hash y rutas

- **Hash del archivo del cribado (checkpoint 2.800):** el commit del checkpoint (este mismo o el
  inmediatamente posterior) fija el archivo en 2.800 lineas. Es el estado que el auditor
  recomputa. El tramo se subio por partes (`Cribado 2701-2725`, `2726-2750`, `2751-2775`,
  y el cierre 2776-2800).
- **Rutas tocadas esta vuelta:**
  - `docs/INTRA_DOMINIO_VEREDICTOS.jsonl` (100 veredictos nuevos, 2.701 a 2.800).
  - `docs/INTRA_DOMINIO_INFORME.md` (seccion 94, checkpoint 2.800 compacto, con la precision
    de la capacidad adjudicada en el acta vuelta 2).
  - `docs/BANCO_DE_TEXTOS.md` (9.28.1: el barrido del CUERPO, la cota nueva con corte y comando).
  - `scripts/barrido_quinta_cara_cuerpo.py` (nuevo, hermano de solo lectura del barrido title+id,
    para la TAREA 1).
  - `docs/loop/REPORTE.md` (este archivo).
- **docs/plan/ NO se toco** (solo lectura, como manda el encargo).

## TAREA 1: el universo limpio de la quinta cara (9.28.1), corrido

Adjudicado por el auditor (acta vuelta 2) como MEDICION por extension del 9.28. Extendi el
barrido a un hermano de solo lectura, `barrido_quinta_cara_cuerpo.py`, que barre TAMBIEN el
cuerpo del nodo (`resumen_teorico` y `pasos_accionables`), restringido a los dominios de nombre
largo en castellano (fuera `core`), con la lista curada mas la sigla en mayusculas y un conjunto
de genericos excluidos (`control`, `quality`, `process`, `design`, vocabulario traducido de
casi todo nodo). Comando: `python scripts/barrido_quinta_cara_cuerpo.py 2800 --dominio quality`.

**Resultado, dos caras (ambas en 9.28.1 con su corte):**

- **LA GANANCIA, recall pleno del numerador.** Barrer el cuerpo recupera las dos apariciones
  que title+id no veia: el **box plot del 2.517** (vive en el cuerpo) y el **COC del 2.593**
  (deletreado *Concerns, Options, Consequences*, cazado al sumar esos tres tokens). **Las seis
  parejas de aparicion (cinco denominaciones) caen ahora DENTRO de la superficie**, verificado
  par a par (2.464, 2.477, 2.488, 2.517, 2.548, 2.593).
- **EL COSTO, denominador saturado.** El universo de denominacion foranea en title+id+cuerpo de
  `quality` sube a **234 de 389 pares** (o **204** sin los fragmentos de termino multipalabra
  que el regex parte, *total*, *of*, *value*). No es ruido de falso positivo: la prosa de
  `quality` esta saturada de nombres foraneos de metodo reales (benchmarking en 59 pares fuertes,
  y le siguen six sigma, lean, pareto, DMAIC, kaizen, poka yoke, KPI, CPK, ROI, QFD, GMP, AQL).

**Cota firmable al corte 2.800, COTA no censo:** **6 de 234 = 2,6 %** (o 6 de 204 = 2,9 %). Es
un piso mas bajo que el de title+id (4 de 56 = 7,1 %), **y esa diferencia es la leccion:** el
title+id da denominador apretado pero pierde senal; el cuerpo da recall pleno pero denominador
saturado. **Las dos cotas acotan la tasa verdadera; no existe la tasa unica limpia que la figura
pedia.** La senal se firma mejor como cifra cruda, **cinco denominaciones al corte 2.800**, que
como tasa. Limite declarado: los 234 no se curaron par a par a mano (solo las seis apariciones y
los mayores tokens del denominador); 234 es cota superior, asi que 6 de 234 es el piso mas
conservador.

## TAREA 2: cribado 2.701 a 2.800 (100 pares)

### Marcador recomputado del archivo (corte 2.800, 2.800 veredictos, cero huecos, cero duplicados)

| clase | conteo | porcentaje |
|---|---:|---:|
| A | **563** | 20,1 % |
| B | 89 | 3,2 % |
| C | 7 | 0,2 % |
| D | **2.141** | 76,5 % |

Contra el checkpoint 2.700 (A 544, B 89, C 7, D 2.060): **+19 A y +81 D**; B y C sin cambio.
Los 100 pares nuevos: **19 A y 81 D, 19,0 % de A.** Todos fueron `quality`.

### Tasa por dominio (corte 2.800)

| dominio | n | A | tasa |
|---|---:|---:|---:|
| core | 1.445 | 344 | 23,8 % |
| **quality** | **389** | **109** | **28,0 %** |
| health_safety | 192 | 45 | 23,4 % |
| entrega | 171 | 2 | 1,2 % |
| environmental | 170 | 29 | 17,1 % |
| compras | 155 | 1 | 0,6 % |
| franquicias | 148 | 18 | 12,2 % |
| exportacion | 130 | 15 | 11,5 % |

`quality` **baja de 31,1 % a 28,0 %** porque el tramo entrego 19,0 % de A. Empata a `core`
(23,8 %) por arriba y sigue al frente del catalogo. Le faltan **455 pares** (hasta el 3.255).

### Vara por tramo de 25 (quality, 2.701-2.800)

| tramo | n | A | tasa |
|---|---:|---:|---:|
| 2.701-2.725 | 25 | 3 | 12,0 % |
| 2.726-2.750 | 25 | 6 | 24,0 % |
| 2.751-2.775 | 25 | 6 | 24,0 % |
| 2.776-2.800 | 25 | 4 | 16,0 % |

El cuerpo de `quality` sigue por debajo de su banda historica 28-44 %. **No es caida del
inventario, es el cuerpo entregando cumulos todo-D del mismo autor:** ficha contra mapa, metodo
contra encuadre, fase contra fase del roadmap. Coincide con el limite del 9.19: la cabeza de
`quality` dio gemelos, el cuerpo separa familias en caras distintas.

### Familias del 9.3 al dia, con su especie de ganador (corte 2.800)

| familia | pares leidos | especie |
|---|---|---|
| la **capacidad** | **10 de 10, las diez D** (extiende con 2.751 y 2.779 via `capacidad_de_proceso_2`) | **SIN ACTO, sigue cerrada** (no reabre, extiende, como el 2.697) |
| la **distincion comun/especial** | absorbe 2.736, 2.740, 2.752, 2.766, 2.800 | **POR DERECHO**, absorbedor `causas_comunes_vs_especiales`; el cumulo del NO CULPAR cae aqui |
| la **responsabilidad gerencial** | postura gerencial D contra procedimiento (2.741) y contra lemas (2.732, 2.793); mapa y argumento D (2.724, 2.785) | **POR ELEGIR provisional, SIGUE ABIERTO** |
| el **breakthrough / DMAIC** | breakthrough_desempeno_actual =A= DMAIC otra vez (2.759, via 2.618 y 2.548) | **POR ELEGIR** |
| el **Consejo de Calidad** | el nodo Crosby autonomo `consejo_de_calidad_2` queda FUERA (2.703, 2.775 D); consejo ejecutivo D contra equipo (2.774) | **POR ELEGIR**, hub `consejo_calidad`; la cobertura del cumulo sigue sin cerrar |
| **make_certain, auditorias, costo de calidad, benchmarking, roadmap** | D pesada por facetas (2.739, 2.768, 2.778, 2.784, 2.798) | familias que separan cada nodo en cara distinta |

### Figuras al dia

- **Fusion mutua:** SIN CASO NUEVO en 2.701-2.800. Los 19 A del tramo son contencion (MSA
  absorbe errores de medicion 2.727, poka-yoke de servicio 2.737, breakthrough=DMAIC 2.759),
  transitividad de cumulo POR DERECHO (distincion 2.736, 2.740, 2.752, 2.766, 2.800) o fusion
  mutua de nodos gemelos ya en cumulo (gobierno familiar 2.760, loteria 2.762, secuencia
  universal 2.781, revision de progreso 2.780, oficina estrategica 2.787). El contador de
  fusiones mutuas queda en **diecisiete** (el ultimo fue el 2.666).
- **La senal del idioma (quinta cara, 9.28.1):** SIN APARICION NUEVA en 2.701-2.800; la cifra
  queda en **cinco denominaciones al corte 2.800**. Su cota se remidio con el barrido del cuerpo
  (TAREA 1). Nota: el Teorema de Nelson (perdida de nombre 9.28, ya declarada en el 2.577) reasoma
  en el 2.740 al re-emparejarse el nodo que lo carga; no es aparicion nueva.
- **La capacidad, SIN ACTO se sostiene, ahora en 10 de 10:** el nodo nuevo `capacidad_de_proceso_2`
  trajo dos pares mas (2.751, 2.779), ambos D. "Cerrada" era sobre los pares que la cola habia
  traido, no sobre todos los nodos de la raiz; se extiende sin reabrir.

## LA LECCION DEL METODO, y va al acta del auditor

**El barrido de familia siguio corrigiendo la lectura aislada.** Los dictamenes del tramo citan
a sus hermanos como se sistematizo desde el 2.567. Casos donde la familia decidio:

- **2.706** (SPC _2 contra _del_proceso): D por transitividad (2.590 fundio _2 con _de_procesos,
  2.413 separo _de_procesos de _del_proceso).
- **2.759** (breakthrough contra DMAIC_2): A por transitividad (2.618 breakthrough=DMAIC,
  2.548 DMAIC=DMAIC_2), no por lectura aislada (sim_tit 24,7).
- **2.740, 2.752, 2.800** (nodos de la distincion): A por el absorbedor `causas_comunes_vs_especiales`.
- **2.789** (conciencia contra entrenamiento de supervisores): D por transitividad (2.630
  conciencia=quality_awareness, 2.648 entrenamiento=D=quality_awareness).
- **2.739, 2.779** (make_certain, capacidad): D por la familia D pesada, la trampa del 2.652 (A
  por instinto, D por familia).

**El filo dominante del tramo:** en el cuerpo de `quality`, la contencion funde solo cuando el
acto entero de uno cabe en el otro (2.727, 2.759, 2.744); la FICHA que despliega un paso del mapa
NO se subsume, es cara distinta (2.707, 2.735, 2.758, 2.769, 2.772, 2.778, 2.782, 2.790); el
METODO no es su ENCUADRE ni su ADVERTENCIA (2.765, 2.767); y la FASE de un roadmap no es otra
fase (2.798). Es la vara 9.6.1 pesando contenido con la figura 78.2 en las dos direcciones.

## DISCUTIBLES MARCADOS para la relectura ciega (marcados ANTES de saber si acierto)

Por la metrica de credito: **si una discrepancia cae FUERA de lo marcado, se mueve el credito de
toda la tanda.** En un tramo casi todo D (81 de 100), **el riesgo esta en las 19 A** (cada una
una afirmacion falsable de duplicado) y en las D que anularon una lectura A defendible. **Los 100
pares llevan DISCUTIBLE MARCADO inline en el jsonl (22 marcados "fuerte"), asi que el marcado que
cuenta para el credito es el del archivo, no solo esta tabla.**

**Las 19 A del tramo** (el riesgo primario): 2.701, 2.705, 2.709, 2.727, 2.736, 2.737, 2.740,
2.742, 2.744, 2.752, 2.759, 2.760, 2.762, 2.766, 2.773, 2.780, 2.781, 2.787, 2.800.

**Los discutibles mas fuertes, con su filo:**

| puesto | clase | por donde puede caer |
|---:|---|---|
| **2.773** | A | comparacion de inspectores independientes contra riesgos del consenso. Por el patron metodo contra encuadre, quien lea el procedimiento de medicion como cara distinta de la advertencia conceptual dira D |
| **2.727** | A | errores_de_medicion contra MSA. Quien lea errores como el CONCEPTO de los dos tipos de error (sesgo, repetibilidad) y no como el procedimiento contenido dira D |
| **2.737** | A | error-proofing de servicio contra poka-yoke. sim_tit 29,5; quien lea el dominio servicio como cara distinta dira D |
| **2.742** | A | DMAIC Fase Select contra proceso de nominacion. Quien lea Select como ficha de fase del DMAIC (las fases salen D entre si) dira D |
| **2.766 / 2.800** | A | no culpar contra distincion. La familia de la responsabilidad gerencial salio D contra la distincion cuando anadia remover barreras; quien aplique ese prior a la colaboracion entre turnos o la respuesta diferenciada dira D |
| **2.760 / 2.780 / 2.787** | A | gobierno familiar, revision de progreso, oficina estrategica. Quien pese el angulo propio de cada segundo nodo (sucesion, ahorro financiero, auditoria de la Oficina) como cara distinta dira D |
| **2.768** | D | auditoria de proceso contra auditorias de calidad de proceso. sim_tit 57,9 y nucleo compartido auditar con checklist; quien pese ese nucleo dira A por fusion mutua |
| **2.730** | D | acceptance_control contra criticas del muestreo. La tesis compartida migrar del muestreo al SPC con proveedor al origen hace defendible A |
| **2.797** | D | auditoria del sistema contra manual de calidad. sim_tit 66,7; quien lea ambos como el mismo sistema de control de calidad dira A |
| **2.756** | D | definiciones_operacionales _2 contra _defectos. Nucleo criterio de aceptacion con validacion entre inspectores; quien lo pese dira A por contencion |
| **2.790** | D | el enunciado SMART es parte de establecer el proyecto (paso 2 y 4); quien lea la ficha como contenida dira A |
| **2.799** | D | implementacion de controles contra plan de control. plan_de_control fusiona con vecinos (2.562, 2.639); quien lea la implementacion como parte del plan dira A |
| **2.723** | D | ISO/TS 16949 automotriz contra adaptaciones sectoriales. Por el 78.2 los pasos de la automotriz calzan con el patron general; quien lea el caso como repeticion dira A |
| **2.724 / 2.741** | D | sistema estable / responsabilidad gerencial contra sus vecinos. Comparten distinguir comun de especial y no culpar; quien pese ese nucleo dira A |
| **2.702** | D | planes contra muestreo de aceptacion. sim_tit 81,5; quien ignore el diseno economico contra la mecanica dira A |
| **2.784** | D | quality is free contra COPQ. Ambos calculan el costo de la mala calidad para priorizar prevencion; quien pese ese nucleo dira A |
| **2.798** | D | fase Expand contra fase Prepare. sim_tit 73,1 por la plantilla del titulo; quien lea las fases como el mismo roadmap dira A |
| **2.795** | D | AQL/DPM contra indices de muestreo. Comparten la advertencia el AQL no autoriza no conforme; quien pese ese nucleo dira A |

**Patron de los discutibles:** el filo del tramo es **A por contencion, fusion mutua o
transitividad de cumulo contra D por ficha-contra-mapa, metodo-contra-encuadre y fase-contra-fase**,
en cumulos del mismo autor. La vara del 9.6.1 y la figura 78.2 tiran de las dos.

## PENDIENTES DE DOCTRINA y PREGUNTAS (regla 9: lo que no puedo medir, lo traigo)

- **NO hubo PENDIENTE DE DOCTRINA nueva en el cribado:** los 100 pares se clasificaron con reglas
  escritas (vara 9.6.1, contencion, fusion mutua, sin acto 9.3.1, ficha contra mapa, caso no es
  la casa 78.2, transitividad de cumulo, quinta cara 9.28.1). Ninguno pidio una regla que no
  exista.
- **PREGUNTA 1, la cobertura del Consejo de Calidad, SIGUE ABIERTA.** El cumulo es POR ELEGIR con
  hub `consejo_calidad`. El nodo Crosby autonomo `consejo_de_calidad_2` quedo FUERA dos veces
  (2.703, 2.775 D, por su autonomia respecto a la jerarquia). Falta ver si el hub `consejo_calidad`
  pierde algun par que lo vuelva POR ELEGIR de verdad o si es POR DERECHO. La cola dira. Anotado,
  no dictado.
- **PREGUNTA 2, el sub-cumulo de la responsabilidad gerencial, SIGUE ABIERTO.** La postura
  gerencial (`responsabilidad_gerencial_causas_comunes`, `sistema_responsabilidad_gerencial`)
  sale D contra el procedimiento (`sistema_estable`, la distincion) y contra los lemas, pero el
  cumulo es grande y no esta leido entero. Especie POR ELEGIR provisional. La cola dira.
- **PRECISION REGISTRADA, la capacidad en 10 de 10.** La familia crecio dos pares en el tramo
  (2.751, 2.779) via el nodo `capacidad_de_proceso_2`, ambos D. SIN ACTO se sostiene; "cerrada"
  era sobre los pares traidos, no sobre todos los nodos de la raiz. Declarado sin retocar el
  8 de 8 del acta vuelta 2.
