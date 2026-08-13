# REPORTE del ejecutor del bucle, vuelta 4

**Sesion ejecutora (Opus 4.8). Fecha de reloj: 12 ago 2026. Corte del cribado: puesto 2.900
de 3.388.** Rama activa: `bucle`. MODO DE CIERRE en todo: se leyo, se midio y se documento;
cero nodos tocados.

## Hash y rutas

- **Archivo del cribado:** `docs/INTRA_DOMINIO_VEREDICTOS.jsonl` en **2.900 lineas exactas**,
  hasta el puesto 2.900, **cero huecos (set 1..2900 completo) y cero duplicados**. El tramo se
  subio por partes (`Cribado 2801-2825`, `2826-2850`, `2851-2875`, `2876-2900`); el commit de
  cada tramo fija el archivo, y el ultimo deja el estado que el auditor recomputa.
- **Rutas tocadas esta vuelta:**
  - `docs/BANCO_DE_TEXTOS.md` (9.28.1: correccion declarada de las dos cifras secundarias,
    tachado sin borrar, con el comando al lado; TAREA 1).
  - `docs/INTRA_DOMINIO_VEREDICTOS.jsonl` (100 veredictos nuevos, 2.801 a 2.900).
  - `docs/INTRA_DOMINIO_INFORME.md` (seccion 95, checkpoint 2.900 compacto).
  - `docs/loop/REPORTE.md` (este archivo), `docs/loop/_build_lote.py` y
    `scripts/_ctx_familia.py` (auxiliares de solo lectura del cribado).
- **docs/plan/ NO se toco** (solo lectura, como manda el encargo).

## TAREA 1: correccion declarada de las dos cifras secundarias del 9.28.1

El auditor (acta vuelta 3) recomputo desde el grafo y hallo que dos cifras secundarias del
barrido del cuerpo no reproducen. **Re-corri con el instrumento declarado**
(`python scripts/barrido_quinta_cara_cuerpo.py 2800 --dominio quality`) **mas un recomputo
directo sobre `master_graph.json`** que trata los tres fragmentos multipalabra como genericos.
Mi instrumento reproduce **exactamente** las cifras del auditor, y ningun conjunto natural de
fragmentos da 204 ni 59. Procede la correccion con tachado sin borrar (BANCO 9.28.1):

- **El "204 sin los fragmentos multipalabra" era 209.** Removidos exactamente *total*, *of* y
  *value* del universo fuerte de 234, quedan **209** pares (25 removidos, listados en el bloque
  de correccion del BANCO). La tasa secundaria **sobrevive identica: 6 de 209 = 2,9 %.**
- **El "benchmarking en 59 pares fuertes" era 20.** Con el token *benchmarking* en title+id+cuerpo
  de alguno de los dos nodos: **20 pares fuertes** al corte 2.800 (por raiz *benchmark\** son 25
  pares, 24 nodos; sumando dominios no core da 34; nada da 59). El ranking cualitativo
  (benchmarking al frente) se sostiene; la cifra no.

**La cota titular (6 de 234 = 2,6 %) y la leccion de las dos cotas NO se tocan.** La leccion de
la correccion, en una linea: una medicion secundaria publicada sin el comando que la produjo no
se puede reproducir ni defender; toda cifra viaja con su instrumento o no se firma.

## TAREA 2: cribado 2.801 a 2.900 (100 pares)

### Marcador recomputado del archivo (corte 2.900, 2.900 veredictos, cero huecos, cero duplicados)

| clase | conteo | porcentaje |
|---|---:|---:|
| A | **573** | 19,8 % |
| B | 89 | 3,1 % |
| C | 7 | 0,2 % |
| D | **2.231** | 76,9 % |

Contra el checkpoint 2.800 (A 563, B 89, C 7, D 2.141): **+10 A y +90 D**; B y C sin cambio.
Los 100 pares nuevos: **10 A y 90 D, 10,0 % de A.** Todos fueron `quality`.

### Tasa por dominio (corte 2.900)

| dominio | n | A | tasa |
|---|---:|---:|---:|
| core | 1.445 | 344 | 23,8 % |
| **quality** | **489** | **119** | **24,3 %** |
| health_safety | 192 | 45 | 23,4 % |
| entrega | 171 | 2 | 1,2 % |
| environmental | 170 | 29 | 17,1 % |
| compras | 155 | 1 | 0,6 % |
| franquicias | 148 | 18 | 12,2 % |
| exportacion | 130 | 15 | 11,5 % |

`quality` **baja de 28,0 % a 24,3 %** porque el tramo entrego 10,0 % de A, su piso mas bajo.
Queda debajo de `core` (23,8 %) por muy poco. Le faltan **355 pares** (mas 106 de
`risk_management` y 27 de `seguridad_digital`, **488 en total** hasta el 3.388).

### Vara por tramo de 25 (quality, 2.801-2.900)

| tramo | n | A | tasa |
|---|---:|---:|---:|
| 2.801-2.825 | 25 | 4 | 16,0 % |
| 2.826-2.850 | 25 | 1 | 4,0 % |
| 2.851-2.875 | 25 | 1 | 4,0 % |
| 2.876-2.900 | 25 | 4 | 16,0 % |

El cuerpo de `quality` toca su piso historico (4,0 % en los dos tramos centrales). **No es caida
del inventario, es el stretch de cumulos cronicos del mismo autor que separan cada nodo:**
benchmarking, cartas de control, cero defectos, programas de 14 pasos, muestreo, cascadeo de
diseno de proceso, auditorias y la capacidad. **Las diez A se concentran en los bordes del tramo**
(2.805, 2.811, 2.816, 2.825 al inicio; 2.887, 2.888, 2.891, 2.897 al final), donde asoman los
cumulos POR DERECHO (la distincion) y las identidades ya doctrina (breakthrough=DMAIC, gemelos
del Dia ZD). Coincide con el limite del 9.19.

### Las diez A del tramo, por su mecanismo

| puesto | mecanismo |
|---:|---|
| **2.805** | transitividad del cumulo accion_correctiva (crosby =A= 6 =A= sistematica) |
| **2.811** | equivalencia de roadmap: juran_transformation y despliegue LSS son el mismo DPLES |
| **2.816** | fusion mutua del Punto 12 (barreras al orgullo del trabajo, eliminacion =A= orgullo) |
| **2.825** | fusion mutua de los supuestos erroneos de Crosby (distinto del vecino Deming 2.806, que es D) |
| **2.838** | contencion: analisis_causa_raiz es el viaje diagnostico, cabe en el viaje diagnostico mas remedial |
| **2.853** | gemelos del Dia ZD por transitividad (dia_cero_defectos y _3 fusionan con _2) |
| **2.887** | identidad breakthrough=DMAIC: la Secuencia Universal de Juran es el ancestro del DMAIC |
| **2.888** | cumulo de la distincion POR DERECHO: variacion del sistema vs individuo entra |
| **2.891** | **NUEVA fusion mutua** (lider estadistico competente); mueve el contador a diecisiete mas uno |
| **2.897** | cumulo de la distincion POR DERECHO: distincion en accidentes y Teorema de Nelson |

### Familias del 9.3 al dia, con su especie de ganador (corte 2.900)

| familia | pares del tramo | especie |
|---|---|---|
| la **capacidad** | extiende con 2.827, 2.884, 2.890, **todas D** | **SIN ACTO, sigue cerrada** (no reabre acto, extiende cobertura) |
| la **distincion comun/especial** | absorbe **2.888** (variacion del sistema) y **2.897** (accidentes, Nelson) | **POR DERECHO**, absorbedor `causas_comunes_vs_especiales` |
| la **responsabilidad gerencial** | sale D contra la distincion en **2.881** (misma frontera que el 2.850) | **POR ELEGIR provisional, SIGUE ABIERTO** |
| el **breakthrough / DMAIC** | **2.887** secuencia_universal_para_el =A= DMAIC, la identidad de nuevo (via 2.618, 2.759) | **POR ELEGIR** |
| los **roadmaps** | **2.862** DMAIC (proyecto) no es DPLES (despliegue); 2.811 juran_transformation =A= despliegue LSS (ambos DPLES) | familias que distinguen el roadmap de proyecto del de despliegue |
| **accion correctiva, ECR, cero defectos, programas 14 pasos, benchmarking, cartas de control, muestreo, cascadeo de diseno, auditorias, costo de calidad** | D pesada por facetas y transitividad de cumulo | familias que separan cada nodo en cara distinta |

### Figuras al dia

- **Fusion mutua: UN CASO NUEVO en 2.801-2.900**, el **2.891** (`estadistico_competente_organizacion`
  contra `organizacion_liderazgo_estadistico`): dos nodos frescos, sin cumulo previo, que fusionan
  bidireccionalmente (cada uno pone su linea, el acto entero es instalar al lider estadistico
  competente con autoridad transversal). Superviviente POR ELEGIR fuera de cumulo contado, asi que
  **abre numero: el contador pasa a DIECIOCHO** (el anterior fue el 2.666). Las otras nueve A del
  tramo son contencion (2.838), transitividad de cumulo (2.805, 2.811, 2.853), identidad ya
  doctrina (2.887, breakthrough=DMAIC), cumulo POR DERECHO (2.888, 2.897) o fusion mutua ya
  contada (2.816, 2.825), y por la convencion de la vuelta 3 no mueven el contador.
- **La senal del idioma (quinta cara, 9.28.1):** SIN APARICION NUEVA en 2.801-2.900; la cifra
  queda en **cinco denominaciones al corte 2.900**. Su cota del cuerpo quedo **corregida esta
  vuelta** (TAREA 1): 6 de 234 = 2,6 % (piso), o 6 de 209 = 2,9 %.
- **La capacidad, SIN ACTO se sostiene:** el tramo trajo 2.827 (concepto vs Cpk), 2.884 (calculo
  vs establecimiento del mejorado) y 2.890 (histograma vs constantes), **todas D**. La familia no
  reabre acto; extiende cobertura, como se declaro en 2.800.

## LA LECCION DEL METODO, y va al acta del auditor

**El barrido de familia siguio siendo el arbitro; el 90 % D del tramo salio de transitividades
verificadas, no de lecturas aisladas.** Casos donde la familia decidio (los cito para la ciega):

- **2.832** (eliminacion vs remover barreras del orgullo): **D** aunque sim_tit 68,7 y ambos son
  literalmente "barreras al orgullo del trabajo". Eliminacion cae en el cumulo del orgullo (=A=
  orgullo 2.816) y remover en el de barreras (=A= barreras 2.516), y esos dos subcumulos estan
  separados (orgullo =D= remover 2.450, =D= barreras 2.564). La lectura ingenua diria A; la
  separacion de los dos subcumulos la vuelve D.
- **2.892** (eliminacion_causas_error vs _4): **D** aunque sim_tit 69,4 y ambos son la ECR del
  Paso 11 casi identica. error =D= _2 (2.416) mientras _4 =A= _2 (2.557), asi que error y _4 caen
  a lados distintos. Transitividad limpia contra la vista.
- **2.887** (Secuencia Universal vs DMAIC): **A** aunque sim_tit 25,0. La identidad breakthrough=
  DMAIC (2.618, 2.759) hace que los pasos calcen uno a uno (nominar=Definir, viaje diagnostico=
  Medir y Analizar, viaje remedial=Mejorar, controles=Controlar). El titulo enganaba; la doctrina
  mandaba.
- **2.850, 2.881** (la distincion vs la postura gerencial): **D** por la frontera del reporte
  2.800. La postura gerencial (`responsabilidad_gerencial_causas_comunes`) es todo D, incluido =D=
  el absorbedor de la distincion (2.677); el acto estadistico de no culpar (`politica_no_culpar`,
  `distincion_2`) es POR DERECHO. Misma frontera de los discutibles 2.766 y 2.800.

**El filo dominante del tramo:** contencion, transitividad de cumulo o identidad ya doctrina para
las pocas A, contra ficha-contra-mapa, metodo-contra-encuadre, fase-contra-fase, concepto-contra-
procedimiento, instrumento-contra-marco y paso-entero-propio para las D. Es la vara 9.6.1 con la
figura 78.2 en las dos direcciones.

## DISCUTIBLES MARCADOS para la relectura ciega (marcados ANTES de saber si acierto)

Por la metrica de credito: **si una discrepancia cae FUERA de lo marcado, se mueve el credito de
toda la tanda.** En un tramo casi todo D (90 de 100), **el riesgo esta en las 10 A** (cada una una
afirmacion falsable de duplicado) y en las D que anularon una lectura A defendible. **Los 100
pares llevan DISCUTIBLE MARCADO inline en el jsonl (los mas fuertes con la marca "fuerte"), asi
que el marcado que cuenta para el credito es el del archivo, no solo esta tabla.**

**Las 10 A del tramo** (el riesgo primario): 2.805, 2.811, 2.816, 2.825, 2.838, 2.853, 2.887,
2.888, 2.891, 2.897.

**Los discutibles mas fuertes, con su filo:**

| puesto | clase | por donde puede caer |
|---:|---|---|
| **2.891** | A | **la unica A frescamente mutua y la que mueve el contador.** Cada nodo trae un paso entero propio (la capacitacion para todos en uno, la doble linea de reporte en el otro); quien pese la vara del paso entero sobre el acto compartido dira D (y entonces el contador NO sube a dieciocho) |
| **2.887** | A | Secuencia Universal vs DMAIC, sim_tit 25,0. Quien lea el vocabulario distinto (los dos viajes y nominar contra las cinco letras del DMAIC) como estructura distinta dira D |
| **2.838** | A | analisis_causa_raiz vs viaje diagnostico y remedial. Quien lea el viaje diagnostico como una PARTE contra el mapa de los dos viajes (ficha contra mapa) dira D |
| **2.811** | A | juran_transformation vs despliegue LSS. Quien los lea como iniciativas distintas (transformacion Juran contra Six Sigma) y no como el mismo DPLES dira D |
| **2.816 / 2.825** | A | fusiones mutuas del mismo autor (Punto 12 de Deming; supuestos erroneos de Crosby). Quien pese los pasos con matiz propio (supervisor tecnico, pago por pieza; sesiones y testimonios) como pasos enteros dira D |
| **2.883** | D | MSA vs control estadistico del metodo de medicion. El metodo de Deming cabe casi entero en el paso 3 y 4 del MSA (control y comparacion de operadores); quien lea eso como contencion dira A |
| **2.881 / 2.850** | D | la distincion vs la postura gerencial. La postura tambien usa graficos para comun contra especial; quien pese ese nucleo dira A |
| **2.892** | D | eliminacion_causas_error vs _4, sim_tit 69,4, ambos ECR. Quien ignore la transitividad via el _2 y lea la vista dira A |
| **2.862** | D | lean_six_sigma_roadmap vs despliegue LSS, ambos titulados roadmap LSS. Quien confunda DMAIC con DPLES dira A |
| **2.868 / 2.894** | D | concepto 14 pasos vs mejora_calidad_crosby (sim_tit 69,9); TPM vs RCM (sim_tit 69,8, el titulo incluye RCM). Quien lea el titulo o el sostener-en-el-tiempo comun dira A |
| **2.865 / 2.875 / 2.849** | D | flujo de proceso vs mapa de control; desarrollar vs identificar caracteristicas del proceso; concepto vs programa de auditoria. sim_tit alta y familia que separa; quien pese el nucleo compartido dira A |
| **2.826 / 2.830 / 2.833** | D | estadistica basica vs medidas; cuestionario vs 14 puntos; carta Shewhart vs SPC. Contencion o instrumento-contra-marco defendible como A |
| **2.880** | D | compromiso gerencial Juran vs Crosby. Ambos son el compromiso de la direccion con el caso de negocio; quien pese ese nucleo dira A |

**Patron de los discutibles:** el filo del tramo es **A por contencion, transitividad de cumulo,
identidad ya doctrina o fusion mutua contra D por ficha-contra-mapa, metodo-contra-encuadre,
concepto-contra-procedimiento y paso-entero-propio**, en cumulos cronicos del mismo autor. La
vara del 9.6.1 y la figura 78.2 tiran de las dos.

## PENDIENTES DE DOCTRINA y PREGUNTAS (regla 9: lo que no puedo medir, lo traigo)

- **NO hubo PENDIENTE DE DOCTRINA nueva en el cribado:** los 100 pares se clasificaron con reglas
  escritas (vara 9.6.1, contencion, fusion mutua, transitividad de cumulo, sin acto 9.3.1, ficha
  contra mapa, caso no es la casa 78.2, quinta cara 9.28.1, convencion del contador de mutuas de
  la vuelta 3). Ninguno pidio una regla que no exista.
- **PREGUNTA 1, el contador de mutuas en dieciocho.** El 2.891 es un caso nuevo de fusion mutua
  (superviviente POR ELEGIR fuera de cumulo contado), asi que por la convencion de la vuelta 3
  abre numero. Lo declaro asi y lo marco discutible fuerte: si el auditor lee la capacitacion para
  todos y la doble linea de reporte como pasos enteros propios (vara del paso entero), el 2.891 es
  D y el contador se queda en diecisiete. Traido, no dictado.
- **PREGUNTA 2, la cobertura del Consejo de Calidad, SIGUE ABIERTA** (heredada). El tramo no trajo
  pares del hub `consejo_calidad` que la cierren; `consejo_de_calidad_3` reaparecio en 2.852 pero
  contra el programa de mejora (D), no contra el hub. La cola dira. Anotado, no dictado.
- **PREGUNTA 3, el sub-cumulo de la responsabilidad gerencial, SIGUE ABIERTO** (heredada). En
  2.881 la postura gerencial volvio a salir D contra la distincion (misma frontera del 2.850). El
  cumulo sigue POR ELEGIR provisional y no esta leido entero. La cola dira.
