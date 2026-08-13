# REPORTE del ejecutor del bucle, vuelta 2

**Sesion ejecutora (Opus 4.8). Fecha de reloj: 12 ago 2026. Corte del cribado: puesto 2.700
de 3.388.** Rama activa: `bucle`. MODO DE CIERRE en todo: se leyo, se midio y se documento;
cero nodos tocados.

## Hash y rutas

- **Hash del archivo del cribado (checkpoint 2.700):** `a5d16eee` (commit "Cribado 2697-2700").
  Es el estado que el auditor debe checar y recomputar. Este reporte va en el mismo commit o
  el inmediatamente posterior.
- **Rutas tocadas esta vuelta:**
  - `docs/INTRA_DOMINIO_VEREDICTOS.jsonl` (100 veredictos nuevos, 2.601 a 2.700).
  - `docs/INTRA_DOMINIO_INFORME.md` (TAREA 1.1: seccion 92, checkpoint 2.600; y seccion 93,
    checkpoint 2.700 compacto).
  - `docs/BANCO_DE_TEXTOS.md` (TAREA 1.2: precision de fecha en 9.21; TAREA 1.3: medicion de la
    tasa de la quinta cara en 9.28.1).
  - `scripts/barrido_quinta_cara.py` (nuevo, solo lectura, para TAREA 1.3).
  - `docs/loop/REPORTE.md` (este archivo) y `.gitignore` (`_lote.jsonl`, scratch por tramo).
- **docs/plan/ NO se toco** (solo lectura, como manda el encargo).

## TAREA 1 (registros de la vuelta 1 del auditor), hecha

1. **CHECKPOINT 2.600 AL INFORME:** seccion 92 de `INTRA_DOMINIO_INFORME.md`, compacta,
   remite a este reporte en git (commits `f3c3750c` y `5834d869`). La fuente de checkpoints
   del informe ya no queda trunca en el 2.500.
2. **PRECISION DE LA FECHA en 9.21** (donde vive la regla del corte, la tercera mitad del
   11 ago): adjudicacion del auditor escrita, EL ORDEN CANONICO ES EL CORTE, NO LA FECHA; lo
   transcrito conserva la fecha de su adjudicador, lo nuevo se firma con reloj real mas corte.
   Nada ya escrito se retoco.
3. **TASA DE LA QUINTA CARA (9.28.1):** medida y anotada con su corte y el comando
   (`python scripts/barrido_quinta_cara.py 2600`). **La cifra NO se dicto como tasa unica de
   catalogo, y esa es la leccion:** el universo de catalogo (863 pares con candidato) lo
   contamina `core`, ingles por diseno (*customer* casa 334 nodos); restringido a `quality`
   son **56 de 189 pares** con denominacion foranea en title+id (corte 2.600); pero **2 de las
   5 apariciones caen fuera de esa superficie** (box plot del 2.517 vive en el cuerpo, COC del
   2.593 esta deletreado en el titulo, no como sigla). Cota firmable sobre la superficie
   title+id de `quality`: **4 de 56 = 7,1 %**, piso no censo. Traido para adjudicacion: el
   universo limpio pide barrer el CUERPO del nodo, no solo title+id.

## TAREA 2: cribado 2.601 a 2.700 (100 pares)

### Marcador recomputado del archivo (corte 2.700, 2.700 veredictos, cero huecos, cero duplicados)

| clase | conteo | porcentaje |
|---|---:|---:|
| A | **544** | 20,1 % |
| B | 89 | 3,3 % |
| C | 7 | 0,3 % |
| D | **2.060** | 76,3 % |

Contra el checkpoint 2.600 (A 522, B 89, C 7, D 1.982): **+22 A y +78 D**; B y C sin cambio.
Los 100 pares nuevos: **22 A y 78 D, 22,0 % de A.**

### Tasa por dominio (corte 2.700)

| dominio | n | A | tasa |
|---|---:|---:|---:|
| core | 1.445 | 344 | 23,8 % |
| **quality** | **289** | **90** | **31,1 %** |
| health_safety | 192 | 45 | 23,4 % |
| entrega | 171 | 2 | 1,2 % |
| environmental | 170 | 29 | 17,1 % |
| compras | 155 | 1 | 0,6 % |
| franquicias | 148 | 18 | 12,2 % |
| exportacion | 130 | 15 | 11,5 % |

`quality` **baja de 36,0 % a 31,1 %** porque el tramo entrego 22,0 % de A. Sigue al frente del
catalogo, por encima del 23,8 % de `core`. Le faltan **555 pares** (hasta el 3.255).

### Vara por tramo de 25 (quality, 2.601-2.700)

| tramo | n | A | tasa |
|---|---:|---:|---:|
| 2.601-2.625 | 25 | 6 | 24,0 % |
| 2.626-2.650 | 25 | 7 | 28,0 % |
| 2.651-2.675 | 25 | 7 | 28,0 % |
| **2.676-2.700** | 25 | 2 | **8,0 %** |

El cuerpo de `quality` **cae por debajo de su banda 28-44 %** en este tramo, y el ultimo cuarto
toca **8,0 %**, el mas bajo del dominio hasta la fecha. **No es una caida de la tasa del
inventario, es un tramo cargado de cumulos todo-D:** consejos y benchmarking (nodos hermanos
que la cola trae juntos), fases del roadmap, definiciones operacionales, capacidad, costo de
calidad, make_certain, QFD, y el cumulo de la responsabilidad gerencial. Coincide con lo que
predijo el 9.19 y su limite: la cabeza de `quality` dio gemelos, el cuerpo entrega familias que
se separan en caras distintas.

### Familias del 9.3 al dia, con su especie de ganador (corte 2.700)

| familia | pares leidos | especie |
|---|---|---|
| la **capacidad** | **7 de 7, las siete D** (cierra el 2.636, extiende el 2.697) | **SIN ACTO, cerrada** (establecimiento_capacidad es otro nodo de la familia, tambien D) |
| el **Consejo de Calidad** | 5 pares A entre `consejo_calidad`, `_2`, `_de_calidad`, `_3` (2.523, 2.631, 2.662, 2.663, 2.670) | **POR ELEGIR**, hub `consejo_calidad`; el nodo `_y_rol_del_director` queda fuera (2.505, 2.549 D) |
| **causas comunes vs especiales** | gana 2.497, 2.501, 2.577, 2.641; sus relativos de otro eje quedan D (2.677, 2.679) | **candidata a POR DERECHO** del sub-cumulo del metodo |
| la **regla kp** | POR DERECHO se sostiene: `regla_todo_o_nada_2` queda fuera otra vez (2.646, 2.690 D) | **POR DERECHO** con el 2_ como nodo del fuera-de-control |
| **sistema estable / resp. gerencial** | actos de `sistema_estable` A (2.453, 2.537, 2.572); el sub-cumulo del mapa y el argumento todo D (2.619, 2.640, 2.656, 2.677, 2.700) | **POR ELEGIR**, provisional, cumulo grande sin leer entero |
| el **histograma** | 3 de 3 | **POR DERECHO, final** |
| la **auditoria de producto** | 3 de 3, las tres D | **SIN ACTO, cerrada** |

### Figuras al dia

- **Fusion mutua:** tres casos nuevos, el **decimoquinto (2.630**, conciencia de calidad Paso
  5), el **decimosexto (2.638**, medicion de calidad Paso 3) y el **decimoseptimo (2.666**, el
  consumidor en la linea de produccion). Los tres con superviviente POR ELEGIR. El
  decimocuarto era el 2.597.
- **La senal del idioma (quinta cara, 9.28.1):** SIN APARICION NUEVA en 2.601-2.700; la cifra
  queda en **cinco al corte 2.700**. Su tasa se midio en TAREA 1.3 (ver arriba).
- **La familia de la capacidad, SIN ACTO cerrada:** el 2.636 la cerro en 6 de 6 y el 2.697
  trajo un septimo par, tambien D. Ningun acto de fusion en toda la familia.
- **El cumulo del Consejo de Calidad, nuevo POR ELEGIR:** cuatro nodos que fusionan entre si
  (Juran y Crosby cruzados) alrededor del hub `consejo_calidad`, con el nodo del rol del
  director quedando fuera. Es el ejemplar mas claro de POR ELEGIR del tramo.

## LA LECCION DEL METODO, y va al acta del auditor

**El barrido de familia siguio corrigiendo la lectura aislada, y esta vez seis veces.** Seis
veredictos que aislados daban A bajaron a D al leer la familia, y uno subio de D a A:

- **2.605** (comite ZD contra planificacion ZD): A por instinto de mismo Paso 7, D porque no
  es el mismo acto (arma el quien contra planea el que).
- **2.609** (rol_black_belt contra roles_six_sigma): A por contencion en aislado, D por
  transitividad (`rol_black_belt` =A= `rol_black_belt_six_sigma` =D= `roles_six_sigma`, 2.498
  mas 2.502).
- **2.610** (definiciones_operacionales _2 contra _3): A por contencion, D por el eje
  adentro/afuera del 2.455.
- **2.614** (estandares de trabajo contra cuotas): A por Punto 11a, D por palancas distintas
  (2.539).
- **2.652** (Make Certain): A por mismo programa, D por familia D pesada (2.493, 2.541, 2.544).
- **2.653** (product design spreadsheet contra QFD): A por contencion, D por transitividad
  (2.469 A con spreadsheet_diseno, 2.425 D contra el mismo).
- **2.620** (caso de la arruga) subio de D a A por la figura EL CASO NO ES LA CASA (78.2, el
  2.335): el caso cuyos pasos calzan uno a uno con el general REPITE y sobrevive el general.

**Sin el barrido, seis de estos veredictos habrian salido mal.** Los dictamenes de este tramo
citan a sus hermanos, como se sistematizo desde el 2.567.

## DISCUTIBLES MARCADOS para la relectura ciega (marcados ANTES de saber si acierto)

Por la metrica de credito: **si una discrepancia cae FUERA de lo marcado, se mueve el credito
de toda la tanda.** En un tramo casi todo D (78 de 100), **el riesgo esta en las 22 A**, cada
una una afirmacion falsable de duplicado, y en las D que anularon una lectura A aislada. La
tabla trae las mas fuertes; **los 68 pares con DISCUTIBLE MARCADO inline en el jsonl son el
conjunto completo** (leves incluidos), asi que el marcado que cuenta para el credito es el del
archivo, no solo esta tabla.

**Las 22 A del tramo** (el riesgo primario): 2.601, 2.613, 2.616, 2.618, 2.620, 2.624, 2.627,
2.630, 2.631, 2.638, 2.639, 2.641, 2.645, 2.662, 2.663, 2.664, 2.666, 2.670, 2.673, 2.674,
2.686, 2.699.

**Los discutibles mas fuertes, con su filo:**

| puesto | clase | por donde puede caer |
|---:|---|---|
| **2.686** | A | definiciones_operacionales _3 contra _4. La familia entera es D; quien aplique ese prior sin ver que estos dos NO tienen eje distinto (mismo eje, palabra vaga con validacion externa) dira D |
| **2.691** | D | estructura estadistica contra doble reporte general. Por EL CASO NO ES LA CASA, quien lea la estructura del estadistico como instancia del patron general dira A por contencion |
| **2.677** | D | causas_comunes_vs_especiales (ganadora absorbedora) contra responsabilidad_gerencial_causas_comunes. Comparten la distincion; quien pese ese nucleo dira A |
| **2.618** | A | breakthrough contra DMAIC. Como el 2.602 separo DFSS de DMAIC por proposito, quien lea breakthrough como metodo de marca aparte dira D |
| **2.641** | A | la distincion causas comunes aplicada a accidentes. Quien lea el angulo de no sancionar al individuo como cara distinta (cultura justa de seguridad) dira D |
| **2.620** | A | el caso de la arruga. Quien lea el caso como ilustracion que merece quedar aparte dira D |
| **2.663 / 2.670** | A | motor de proyectos contra consejo ejecutivo. Por el corte del 2.549 (motor contra politica, D), quien los lea como caras distintas del gobierno dira D |
| **2.673** | A | identificar clientes por dos manos. Quien separe clasificar contra listar-tipos dira D |
| **2.645** | A | el reporte de benchmarking. La familia es D pesada; quien lea el analisis y la entrega como etapas distintas dira D |
| **2.700** | D | mejora_del_sistema (absorbedor via sistema_estable) contra el mapa gerencial. Quien pese la responsabilidad compartida sobre el sistema dira A |
| **2.678 / 2.693 / 2.695** | D | ficha o paso en detalle contra el mapa o el plan entero. Quien los lea subsumidos dira A por contencion |
| **2.679** | D | enrutamiento de accion de Juran contra responsabilidad del trabajador de Deming. sim_tit 82,5 y ambos distinguen comun de especial; quien pese ese nucleo dira A |

**Patron de los discutibles:** el filo del tramo es **A por contencion o fusion mutua contra D
por caras distintas**, en cumulos del mismo autor (consejos, benchmarking, roadmap,
definiciones operacionales, capacidad, costo de calidad). La vara del 9.6.1 tira a A; el patron
del cuerpo de `quality` (ficha contra mapa, paso contra proceso, eje adentro/afuera) tira a D.

## PENDIENTES DE DOCTRINA y PREGUNTAS (regla 9: lo que no puedo medir, lo traigo)

- **PREGUNTA 1, el universo limpio de la quinta cara.** La medicion de TAREA 1.3 mostro que la
  superficie title+id no contiene toda la senal (box plot y COC caen fuera). El universo limpio
  pide **barrer el CUERPO del nodo** (resumen y pasos), no solo title+id, y restringirse a los
  dominios de nombre largo en castellano (fuera `core`, ingles por diseno). No lo corri; lo
  traigo para que se adjudique si vale el barrido del cuerpo.
- **PREGUNTA 2, el hub del Consejo de Calidad.** El cumulo es POR ELEGIR con hub
  `consejo_calidad`, pero no lo lei entero: falta ver si `consejo_calidad` pierde algun par que
  lo vuelva POR ELEGIR de verdad o si es POR DERECHO. La cola dira. Anotado, no dictado.
- **NO hubo PENDIENTE DE DOCTRINA nueva en el cribado:** los 100 pares se clasificaron con
  reglas escritas (vara 9.6.1, fusion mutua, sin acto 9.3.1, caso no es la casa 78.2, ficha
  contra mapa, trampa del identificador, perdida de nombre 9.28). Ninguno pidio una regla que
  no existe.
- **La familia de la capacidad se declaro cerrada en 6 de 6 (2.636) y luego llego un septimo
  par (2.697).** No reabre el acto (sigue todo D, SIN ACTO), pero deja claro que "cerrada" era
  sobre los seis pares que la cola habia traido, no sobre todos los nodos con raiz de capacidad.
  Lo anoto como precision, no como error.
