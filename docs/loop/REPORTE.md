# REPORTE del ejecutor del bucle, vuelta 11 (ABRE LA FASE II: EL RECOMPUTO)

**Sesion ejecutora (Sonnet 5). Fecha de reloj: 13 ago 2026. Rama activa: `bucle`.** El cribado
intra-dominio sigue cerrado en el puesto 3.388 (Fase I, verificada y cerrada por el auditor la
vuelta pasada). Esta vuelta **NO tocó `dataset/` ni un byte**: modo de cierre completo, cero
reparaciones de nodos, la Fase III (mover nodos de verdad) sigue sin abrir.

## Hash y rutas

- **Hash final de esta vuelta:** `7f4ec6d9` (TAREA 2, el recomputo). El commit de este reporte
  queda por encima.
- **Rutas tocadas:**
  - `docs/INTRA_DOMINIO_VEREDICTOS.jsonl`: 2 razones corregidas (puestos 3.376 y 3.382), misma
    clase D en las dos, mismo total de 3.388 veredictos. Via `scripts/corregir_veredicto.py`.
  - `docs/INTRA_DOMINIO_INFORME.md`: tres secciones nuevas (100.4 ampliada con correccion
    declarada, 100.12 nueva, 101 nueva).
  - `scripts/plan/recomputo_3388.py`: **instrumento nuevo, el unico autorizado esta vuelta**,
    estrictamente de solo lectura.
  - `docs/plan/RECOMPUTO_3388.md`: documento nuevo con el resultado completo de la TAREA 2.
  - `docs/plan/RECOMPUTO_3388_COMPONENTES.jsonl`: salida de detalle del script, las 335
    componentes fila por fila.
  - `docs/plan/DIFERENCIA_CONTRA_COLA.jsonl`: **corrido, sin diferencia contra el estado ya
    commiteado** (ver TAREA 3).
  - `docs/plan/OPERACIONES.jsonl`: **NO TOCADO**, tal como manda el encargo.
  - `docs/loop/REPORTE.md`: este archivo.
- **Commits de la vuelta:** `767d9ca4` (TAREA 1: dos correcciones de registro y cuatro
  adjudicaciones), `7f4ec6d9` (TAREA 2: el recomputo completo).

---

## TAREA 1: dos correcciones de registro y una verificacion fija nueva

### 1.1 Entregable citado en el 3.376 y el 3.382

Contado por el auditor sobre las razones del archivo: de los **once** discutibles marcados del
tramo 3.301-3.388 (seis fuertes mas cinco simples, cifra ya correcta en 100.7/100.8 del informe),
**nueve citaban el `entregable_esperado` y dos no**, el 3.376 y el 3.382. **Verificado con
instrumento propio antes de corregir: confirmado, 9 de 11 citaban, 2 no.** Los dos D se sostenian
sin tocar la razon de fondo: la correccion no fue de lectura, fue de registro.

**Aplicado con `scripts/corregir_veredicto.py`** (sustituye razon, no anade veredicto, no cambia
clase): se anadio al 3.376 la cita de los dos `entregable_esperado` (`csf_funcion_protect` y
`funcion_protect_politica_seguridad`, ambos corroborando sin decidir, la vara sigue siendo los
pasos); y al 3.382 la cita de los de `fundamentos_gestion_riesgo` y `rmf_paso_preparar` (el
primero nombra "responder" de forma explicita, lo que corrobora el hueco de Respond que ya
sostenia el D). **Verificado con el instrumento tras la correccion: de los once discutibles del
tramo, ONCE de ONCE citan hoy el `entregable_esperado`.** Marcador recomputado tras la correccion
(`scripts/corregir_veredicto.py`, salida directa): sin altas ni bajas, `{'D': 2709, 'A': 583, 'B':
89, 'C': 7}`, archivo en 3.388 veredictos, tasa de A 17,2%. Sin cambio contra el checkpoint 3.388
de la vuelta pasada.

**Correccion de registro en el informe (durable, porque `docs/loop/REPORTE.md` se sobreescribe
cada vuelta):** `docs/INTRA_DOMINIO_INFORME.md`, seccion **100.12** nueva. Corrige la frase de la
vuelta 10 ("ocho discutibles marcados") a la cifra correcta, **9 de 11 antes de la correccion**,
con el texto viejo tachado y no borrado, tal como pide la regla.

### 1.2 La lista de hubs de `risk_management`, y una quinta correccion no pedida

El encargo trajo la correccion del auditor: la lista de hubs de siete toques tenia **dos** nodos
publicados y debia tener **cuatro** (faltaban `cultura_que_habla_del_riesgo_sin_miedo` y
`gestionar_el_riesgo_es_de_adultos`, los dos con siete toques y cero A). **Verificado con
instrumento propio contra los 106 pares de `risk_management` antes de escribir la correccion: la
cifra correcta no es cuatro, es CINCO.** Falta un quinto nodo que ni la vuelta 10 ni la correccion
del auditor incluyeron: **`el_riesgo_nunca_se_acaba_se_administra`**, tambien con siete toques y
cero A. Contado dos veces con el mismo instrumento antes de publicar (una vez para confirmar la
cuenta del auditor, otra para verificar que no quedaba nada fuera): los CINCO son
`deja_de_ignorar_el_riesgo`, `vuelve_a_medir_despues_del_susto`,
`cultura_que_habla_del_riesgo_sin_miedo`, `gestionar_el_riesgo_es_de_adultos`,
`el_riesgo_nunca_se_acaba_se_administra`.

**Es la MISMA regla del superlativo aplicada dos veces seguidas: una lista que corta en un valor
trae todos los empates de ese valor.** Primero la aplico el auditor a mi lista de dos; ahora la
aplico yo a la suya de cuatro. Ninguna cifra del dominio se mueve: sigue en 106 pares, 0 A, 0,0%.
**Corregido en `docs/INTRA_DOMINIO_INFORME.md` seccion 100.4**, con correccion declarada y el
texto viejo tachado.

**DISCUTIBLE MARCADO, para que quede dicho antes de que nadie lo verifique por mi:** esta es una
correccion sobre una correccion del propio auditor. La marco porque puede caer de dos formas: si
mi conteo de siete toques esta bien, es un acierto de la disciplina de verificar antes de aplicar;
si me equivoco yo ahora (por ejemplo si hay un sexto nodo que tampoco vi), la cadena de listas
cortadas seguiria sin cerrar.

### 1.3 Verificacion fija nueva: toda frase de "en cada par/en todos/desde el primero" se cuenta
### antes de escribirse

**Aplicada a este mismo reporte.** Frases candidatas que este reporte podria haber escrito sin
contar, y lo que dice el instrumento:

| frase que se iba a escribir | contada con el instrumento | lo que se escribe en su lugar |
|---|---|---|
| "los once discutibles citan el entregable" | **11 de 11**, contado tras la correccion 1.1 (ver arriba) | se escribe la fraccion, arriba |
| "las cuatro comprobaciones del recomputo cuadran" | **4 de 4**, impreso por `recomputo_3388.py` (ver TAREA 2) | se escribe la fraccion, en la tabla de TAREA 2 |
| "ninguna de las 583 A colapsa al resolver" | **0 de 583**, contado por el paso 1 del recomputo | ya es una fraccion (0 de 583), se deja como esta |
| "el marcador no se movio" | comparado A/B/C/D antes y despues de las dos correcciones: identico, `{'D': 2709, 'A': 583, 'B': 89, 'C': 7}` en los dos cortes | se escribe con las dos cifras iguales, no como "no se movio" a secas |

**Esta verificacion queda fija junto a la de discutibles para todo reporte futuro**, tal como pide
el encargo. No se encontro ninguna frase de la familia "en cada", "en todos" o "desde el primero"
que se hubiera escrito sin contar en este reporte: las cuatro candidatas de la tabla se contaron
antes de esta version final.

### 1.4 Las cuatro adjudicaciones del auditor, registradas

Registradas en `docs/INTRA_DOMINIO_INFORME.md`, **seccion 101 nueva**, cada una con la regla de la
que cuelga: (a) el banco 9.6.3 no bloquea la mutua del 3.363 porque los dos residuos viven dentro
del mismo entregable (un unico plan de respuesta a incidentes, NIST SP1318); (b) la vara se aplica
sobre `pasos_accionables`, no sobre `resumen_teorico` (si el resumen contara, la mutua caeria a
REPITE); (c) cuando el 3.363 se funda, el superviviente conserva LOS DOS residuos, o la fusion
pierde catalogo sin declararlo; (d) las tres fusiones nuevas de `seguridad_digital` no abren cola
de relectura post fusion, verificado: de los ocho pares del archivo que tocan los seis nodos de las
tres A, tres son las propias A y cinco son D, cero B y cero C (los 96 B y C del catalogo viven en
`core`, 94, y `compras`, 2, ninguno en `seguridad_digital`; verificado con instrumento, coincide
exacto con la cifra citada por el auditor).

### 1.5 Lo verificado y en verde, no se toco

El marcador entero al 3.388 (A 583, B 89, C 7, D 2.709) y las diez tasas por dominio; las cuatro
fronteras de dominio; la vara por tramo; las cuatro tablas de rachas; el cierre en cero de
`risk_management`; las tres A de `seguridad_digital` y sus supervivientes; el contador de mutuas en
veintiocho con su reparto 25/1/1/1; la ficha nombrada 6 y 3; los 28 SIN ACTO de `quality`; el
pendiente de los 365 A ciegos anteriores al 2.127. Siguen aprobados
`scripts/recomputar_marcador.py`, `scripts/_registrar_lote.py`, `scripts/volcar_pares.py` y
`scripts/corregir_veredicto.py`.

---

## TAREA 2: EL RECOMPUTO DE LA FASE II, los cuatro pasos en orden

**Detalle completo, con todas las tablas y la lista de las 335 componentes por tamano, en**
`docs/plan/RECOMPUTO_3388.md` **y** `docs/plan/RECOMPUTO_3388_COMPONENTES.jsonl`. Resumen con las
cifras que importan:

**Instrumento: `scripts/plan/recomputo_3388.py`**, el unico script nuevo autorizado esta vuelta,
estrictamente de solo lectura (no escribe nodo, veredicto ni operacion). Modelado sobre el
`comp()` de `scripts/plan/nominas.py` y el `res()` de `scripts/volcar_pares.py`. Comando exacto
con el que corrio cada paso: `python scripts/plan/recomputo_3388.py` (los cuatro pasos corren en
la misma pasada, uno detras del otro, cada uno usando la salida del anterior, tal como manda el
orden del 08_VERIFICACION).

### Paso 1: el retrato de las A

**583 A crudas, 583 pares distintos tras resolver por alias, CERO colapsan a auto-arista.**
Ninguna fusion del plan se ha ejecutado contra `dataset/` todavia (verificado:
`nafta_free_trade_agreements`, el ejemplar de `OP-S-01`, sigue sin `deprecado`), asi que los 391
alias vigentes son historia previa a esta campana y no fusionan ninguna de las 583 A consigo
misma. Fecha de corte: puesto 3.388.

### Paso 2: el barrido de confirmadas contra las A

**NO CORRIDO.** Busqueda declarada, empezando por los dos ficheros que pide el encargo:
`docs/plan/01_FUENTES.md` (linea 53 y 62) y `docs/plan/CORRECCIONES_A_APLICAR.md` (lineas
169-174): las dos citan la cifra **11** (costuras confirmadas con pegado de Hugos, de 46 en
total) **como conteo, nunca como lista**. Busqueda ampliada sobre `docs/` completo
(`docs/COSTURAS_INTERNAS_RESUMEN.md`, `docs/FICHA_SUBFUSION_GRADIENTE.md`,
`docs/GRADIENTE_VEREDICTOS.md`): la primera y la segunda repiten el total de 46 sin nomina; la
tercera tiene una familia de nombre parecido, "costuras confirmadas DE REBOTE" (6 casos, esos si
nombrados), pero es otro universo (verificaciones post-cirugia de la cola del gradiente semantico,
no la nomina que el paso 2 necesita). **La nomina no esta escrita como lista en ningun sitio: por
la instruccion del encargo, no se inventa ni se reconstruye de memoria. El paso 2 queda declarado
NO CORRIDO**, y se sigue con los pasos 3 y 4.

### Paso 3: el cierre transitivo

**Sobre el retrato del paso 1, no sobre el archivo crudo.** 854 nodos con al menos una A, **335
componentes de tamano >= 2** (distribucion: 2: 244, 3: 56, 4: 16, 5: 7, 6: 5, 7: 2, 8: 1, 9: 1,
10: 1, 13: 1, 15: 1). Las cinco componentes grandes nombradas por `OP-U-01`/`OP-U-02` al corte
2.117 siguen presentes hoy, **mismo tamano, identificadas por nombre**: la de 13
(`gestion_de_portafolio_gates_go_kill`, puertas y portafolio), la de 9 (`customer_discovery`), la
de 8 (`build_measure_learn`), y las dos de 7 (`customer_validation` y `brainstorming_divergente`).
Dos componentes enteramente nuevas: tamano 15 (`health_safety`, la familia entera de vieja-vision-
contra-nueva-vision del error humano) y tamano 10 (`quality`, la familia de
`causas_comunes_vs_especiales`), ninguna existia al corte 2.117 porque esos dos dominios abrieron
su cribado despues.

### Paso 4: las nominas y los actos, con cobertura al lado

**Reclasificados CERRADO/ABIERTO con el mismo criterio de `OP-U-01`.** Aviso metodologico que
cambia el calculo respecto al 2.117: **la cola intra-dominio esta agotada** (verificado:
`docs/INTRA_DOMINIO_PARES.jsonl` y `docs/INTRA_DOMINIO_VEREDICTOS.jsonl` tienen exactamente los
mismos 3.388 pares, cero diferencia en cualquier sentido), asi que la condicion "ningun miembro
tiene par pendiente en la cola sin leer" es hoy trivialmente cierta para todos; lo unico que deja
un acto abierto es que existan pares posibles entre miembros que **nunca entraron a la cola**
(el universo de `OP-L-02`, "fuera de cola").

| | corte 2.117 (`OP-U-01`/`OP-U-02`) | corte 3.388 (esta vuelta) | diferencia |
|---|---:|---:|---:|
| actos totales | 221 | **335** | **+114** |
| **CERRADOS** | 173 | **280** | **+107** |
| nodos en CERRADOS | 371 | **600** | **+229** |
| **ABIERTOS** | 48 | **55** | **+7** |
| nodos en ABIERTOS | 205 | **254** | **+49** |

CERRADOS por tamano: 2: 244, 3: 32, 4: 4 (SPIN sigue siendo uno de los de cuatro, verificado por
nombre). ABIERTOS por tamano: 3: 24, 4: 12, 5: 7, 6: 5, 7: 2, 8: 1, 9: 1, 10: 1, 13: 1, 15: 1.

**Cuantos de los 48 cerraron y cuantos actos nuevos abrio el cribado de los 1.271 pares que
faltaban, medido por proxy de edad de arista** (la fecha de la A mas antigua que conecta cada
componente; **no es un mapeo 1 a 1 contra la membresia de los 48 antiguos, porque esa membresia
completa nunca se escribio como lista en ningun documento**, solo tamanos y un puñado de nombres):
de los 335 actos de hoy, **221 tienen todas sus aristas anteriores al 2.117** (continuacion pura),
**1 es mixto**, y **113 son enteramente posteriores al 2.117**, formados por completo dentro del
cribado que corrio entre ese corte y el 3.388. De esos 113, **101 nacieron ya cerrados** (en su
mayoria pares de dos de `quality`, que aporta 25 de las 28 fusiones mutuas del catalogo) y **12
nacieron abiertos** (incluidas las dos componentes nuevas mas grandes, tamano 15 y tamano 10).
**Ninguno de los cinco actos grandes nombrados en el paso 3 aparece entre los nuevos**: los cinco
tienen su A mas vieja anterior al 2.117 y siguen abiertos, sin crecer ni cerrar. **Con esa cautela
declarada, no se puede decir con certeza cuantos EXACTAMENTE de los 48 antiguos cerraron** (un
acto abierto viejo pudo partirse o fundirse con otro por una A nueva, y el proxy de edad no
distingue eso de una simple continuacion): lo que si se puede afirmar, medido, es que los cinco
actos grandes identificables por nombre siguen abiertos sin cambio de tamano.

### Las cuatro comprobaciones

| # | comprobacion | resultado |
|---:|---|---|
| i | nodos en actos (854) == suma de tamanos de las componentes (854) | **OK** |
| ii | A vigentes resueltas (583) == suma de aristas A internas (583) | **OK** |
| iii | todo acto CERRADO tiene sus pares internos leidos y ningun miembro con par pendiente | **OK**, sobre los 280 |
| iv | ningun nodo deprecado aparece dentro de una componente | **OK**, 0 encontrados |

**LAS CUATRO DE CUATRO CUADRAN.** El recomputo esta bien hecho por su propio criterio.

**COMPROBACION CRUZADA adicional, no pedida pero barata:** las A con `puesto_intra <= 2.117`,
resueltas y deduplicadas, dan **401** pares, contra las **400 A vigentes al puesto 2.117** citadas
como evidencia de `OP-U-01`. Diferencia de una unidad, **declarada como pregunta abierta y no como
discrepancia que para la vuelta**: la evidencia vieja no publica su comando ni su lista, asi que no
hay con que diferenciar par por par, y ninguna cifra publicada con corte se contradice de forma que
pida parar (regla 3 del EJECUTOR).

### Que NO cambia esta vuelta

`docs/plan/OPERACIONES.jsonl` **no se toco**. `OP-U-02` sigue en DECISION PENDIENTE hasta que el
auditor verifique las cuatro comprobaciones de arriba. `OP-U-01`, `OP-L-02`, las cinco mesas y las
seis `OP-D-*` siguen con sus cifras del corte 2.117 hasta esa misma autorizacion, tal como manda
el encargo.

---

## TAREA 3: `OP-E-03`, la diferencia contra la cola al cierre del catalogo

**Comando:** `python scripts/plan/diferencia_contra_cola.py` (sin `--dominio`, sobre los 477
candidatos del barrido calibrado).

| dominio | filas | par repetido | ya en la cola | **diferencia** |
|---|---:|---:|---:|---:|
| quality | 208 | 1 | 40 | **167** |
| core | 199 | 1 | 36 | **162** |
| environmental | 22 | 0 | 0 | **22** |
| exportacion | 15 | 0 | 2 | **13** |
| franquicias | 15 | 0 | 2 | **13** |
| health_safety | 12 | 0 | 5 | **7** |
| entrega | 4 | 0 | 2 | **2** |
| risk_management | 1 | 0 | 0 | **1** |
| seguridad_digital | 1 | 0 | 1 | **0** |
| **TOTAL** | **477** | **2** | **88** | **387** |

**LA CUENTA NUEVA, corte 3.388 (catalogo entero cribado), CONTRA LA VIEJA, ensayo en vacio del 11
ago 2026: 387 en las dos, sin cambio.** `docs/plan/DIFERENCIA_CONTRA_COLA.jsonl` salio **byte por
byte identico** al ya commiteado (`git diff` vacio tras correr el script): ninguna fila nueva,
ninguna movida de columna.

**Verificado con instrumento independiente antes de publicar** (no solo confiado en el `git diff`
vacio): de los 208 candidatos de `quality` sin arista, **40 ya estaban en la cola y 167 no**,
contado por separado con un script de una linea sobre el jsonl fuente, coincide exacto con la
salida de `diferencia_contra_cola.py`.

**LA COMPROBACION ARITMETICA, escrita como pide el encargo:** filas (477) == pares repetidos (2) +
ya en cola (88) + diferencia (387). **477 = 2 + 88 + 387. Cuadra.**

**POR QUE NO CAMBIO A PESAR DE QUE TRES DOMINIOS CERRARON DESDE EL ENSAYO** (`risk_management`,
`seguridad_digital`, y `quality` que en el 11 ago 2026 ni siquiera habia abierto): el barrido
calibrado y la cola intra-dominio usan heuristicas de generacion de candidatos distintas (similitud
de paso contra nodo, la primera; vecino mas cercano dentro del dominio, la segunda), asi que el
solape entre las dos listas es estructuralmente chico y no depende de cuanto haya avanzado el
cribado. Es una observacion, no una medicion nueva: **se deja escrita para quien lea esta cifra sin
el contexto de por que el 387 no se movio.**

**LA DIFERENCIA (387 filas) va a LECTURAS DIRIGIDAS, marcada como tal.** No entra en la cola, no
mueve el marcador del cribado, y sus veredictos (cuando se lean) se cuentan aparte de la tasa por
dominio, tal como manda el banco 9.27. **Esta vuelta NO SE LEYO NI UNA**, tal como pide el
encargo: solo se midio la bolsa.

---

## LO QUE NO SE MIDIO ESTA VUELTA (regla 9: lo que no puedo medir, lo traigo)

- **El paso 2 del recomputo (barrido de confirmadas contra las A) queda sin correr**, porque la
  nomina de las costuras confirmadas nunca se escribio como lista. Si esa lista existe en algun
  sitio fuera del repositorio (una sesion de chat, un documento externo), traerla resolveria el
  paso.
- **La comprobacion cruzada del paso 1 (401 contra 400 A vigentes al 2.117) queda como pregunta
  abierta, no resuelta**: no hay comando ni lista publicados de la medicion vieja con los que
  diferenciar par por par.
- **El mapeo exacto de cuales de los 48 actos abiertos de 2.117 cerraron** no se puede hacer 1 a 1:
  solo hay proxy de edad de arista, declarado con su limite arriba.
- **Las 205 lecturas fuera de cola de `OP-L-02`** (126 esperan destejido, 55 resto sin mesa, 5 del
  sales roadmap, 3 ya leidas) no se remidieron esta vuelta: el encargo las dejo fuera a proposito,
  para el encargo que corresponde.
- **Las 387 filas de `LECTURAS DIRIGIDAS` de la TAREA 3 no se leyeron.** Solo se midio la bolsa,
  tal como pide el encargo.
- **El pendiente de los 365 A ciegos anteriores al 2.127** sigue sin verificar, sin cambio esta
  vuelta (no era parte del encargo).
- **La trampa del identificador** sigue sin censo sobre `core`, `environmental`, `exportacion`,
  `entrega` ni `compras` (pendiente heredado, sin cambio esta vuelta).
