# Acta del saneamiento final del dataset

**Encargo del fundador, 28 sep 2026:** auditoría final sobre main, antes de su recorrido y de la corrida final.
**Estado:** EN CURSO. Esta acta solo abrirá con "DATASET CERTIFICADO" y la fecha si todos los criterios quedan en PASA.

**Regla de la API en esta auditoría:** la lectura la hacen agentes; las guardas y la navegación no usan IA. La única API
permitida es Voyage, para recalcular los vectores de los nodos que la auditoría corrija. Ninguna llamada a Anthropic,
ninguna entrevista simulada, ningún recorrido.

Las secciones 1 a 5 se escribieron y se commitearon **ANTES de medir nada**: umbrales, definiciones, diseño de la
muestra con su semilla y la regla del veredicto. Los resultados van en la sección 6.

## 1. Umbrales (fijados por el fundador antes de medir)

| # | Criterio | Umbral | Dónde se mide |
|---|---|---|---|
| U1 | Contrarios | 0 en la muestra | muestra (3) |
| U2 | Invenciones | 0 en la muestra | muestra (3) |
| U3 | Fase | ≤ 3 % de los nodos | muestra (3) |
| U4 | Dominio | ≤ 2 % | muestra (3) |
| U5 | Condiciones de activación | ≤ 2 % | muestra (3) |
| U6 | Etiquetas del riel | ≤ 2 % | muestra (3) |
| U7 | Ortografía | ≤ 1 % | muestra (3) |
| U8 | Matices perdidos | como mucho 1 cada 5 nodos (≤ 0,2 por nodo) | muestra (3) |
| U9 | Calcos | como mucho 1 cada 5 nodos | muestra (3) |
| U10 | Regionalismos o glosario | como mucho 1 cada 5 nodos | muestra (3) |
| U11 | Jurisdicción sin clase | 0 | guarda, 100 % (2) |
| U12 | Alcanzabilidad | 100 % | navegación, 100 % (4) |
| U13 | Guardas | todas en verde | 100 % del catálogo (2) |
| U14 | Copias fieles: texto de nodo que copia o traduce palabra por palabra un pasaje de un libro (regla dura D2, fundador, 30 sep 2026; criterio nuevo de la medida 2) | 0 | muestra (3) y comprobación de copias |

**Cómo se lee un umbral:**
- **Tasa de nodos (U3 a U7):** la proporción de nodos de la muestra con al menos un defecto confirmado por el árbitro
  de ese tipo. Se da con su intervalo de Wilson al 95 %.
- **Tasa por nodo (U8 a U10):** los defectos confirmados de ese tipo divididos entre los nodos de la muestra. Se da con
  su intervalo de Poisson exacto al 95 %.
- **PASA** si la tasa observada no supera el umbral. El intervalo se informa siempre y no cambia el veredicto.
- **U1 y U2 piden 0:** un solo contrario o una sola invención confirmados dan NO PASA.

## 2. Guardas sobre el 100 % del catálogo (sin IA)

Cada guarda PASA con 0 hallazgos; una excepción solo vale si ya estaba adjudicada por escrito antes de esta auditoría.

| # | Guarda | Instrumento |
|---|---|---|
| G1 | Gate 0 | `python scripts/run_phase1.py` (una corrida sobre el árbol limpio) |
| G2 | Alcanzabilidad por mundo y por núcleo | sección 4 |
| G3 | Ley del ancla: ningún nodo del núcleo ancla más de 2 puentes del mismo mundo, y todo puente ancla en el núcleo y llega a un nodo vivo de su mundo | `engine/test_puentes_tejidos.py` y sección 4 |
| G4 | Cero aristas a deprecados | Gate 0 y `engine/test_gate_deprecado_reciproco.py` |
| G5 | Títulos y autores fuera de lo que ve la persona | `engine/test_fuentes_internas.py` y la guarda única de procedencia `web/lib/procedencia.test.ts` (desde el 30 sep 2026 junta `engine/test_fuentes_de_cara.py` y `web/lib/reglaSinFuentes.test.ts`) |
| G6 | Voz de libro y de exposición | `web/lib/vozDeCliente.test.ts` (guarda de voz de cliente) sobre el grafo vivo y la caché |
| G7 | Rutas y marcas de auditoría | la misma guarda (regla `marcasInternas`) |
| G8 | Jurisdicción: toda entrada con país y clase | `engine/test_jurisdiccion.py` |
| G9 | Vigencia de las traducciones de etiquetas | la guardia de vigencia de etiquetas (i18n) |
| G10 | Nada interno en el navegador | la guarda única de procedencia `web/lib/procedencia.test.ts` (antes `web/lib/assets/sinInternos.test.ts`) |
| G11 | Puentes tejidos | `engine/test_puentes_tejidos.py` |
| G12 | Las dos suites, tsc y el índice semántico (todo nodo vivo con vector) | `python engine/run_all_tests.py`, `pnpm vitest run`, `npx tsc --noEmit`, Gate 0 |

**Antes de medir, se corrige la voz de libro de los nodos antiguos (encargo del fundador).** Un barrido previo
encontró 11 nodos vivos que hablan del libro o se exponen como libro y que la guarda de voz no cazaba:
- "como se ilustra en el caso de…", "se ilustra con el ejemplo…";
- "se presenta como…", "se analizan…", "aunque se presenta de forma lineal";
- "vistos anteriormente", "se detallan en capítulos posteriores";
- "los libros llaman a esto…", "los libros de management tradicional".

Se corrigen por la doctrina: una tanda VOZ declarada en cada nodo, que no cambia el sentido. La guarda aprende esos
patrones, con su prueba en rojo primero.

## 3. Muestra estratificada con lectura ciega

- **Semilla:** 20260929, escrita aquí antes de sortear.
- **Universo:** los 3.634 nodos vivos del catálogo.
- **Reparto:** 200 nodos, con 10 por espacio como mínimo y el resto proporcional por el método de los restos mayores.

| Espacio | Vivos | Muestra |
|---|---|---|
| core | 1.410 | 45 |
| quality | 686 | 27 |
| primer_equipo (mundo 11) | 465 | 22 |
| environmental | 263 | 17 |
| health_safety | 258 | 16 |
| franquicias | 181 | 14 |
| exportacion | 130 | 13 |
| entrega | 67 | 12 |
| risk_management | 66 | 12 |
| compras | 55 | 11 |
| seguridad_digital | 53 | 11 |
| **Total** | **3.634** | **200** |

- **Sorteo:** dentro de cada espacio, en orden de `node_id`, con `random.Random(20260929 + índice del espacio en esta
  tabla)`.
- **Lotes:** 20 lotes de 10 nodos de la muestra, con los espacios juntos en lo posible.
- **Trampas SIN MARCA, plantadas ANTES de generar cualquier contexto de lectura:**
  - Cada lote lleva 1 trampa bajo un id real que no está en la muestra, del espacio del lote: un nodo vivo con un
    defecto plantado en la copia del lector, nunca en el dataset.
  - Son 20 trampas, 2 de cada tipo: contrario, invención, fase, dominio, condición, etiqueta, ortografía, matiz
    perdido, calco y regionalismo o glosario.
  - La clave vive fuera de toda carpeta que lean los agentes.
- **Lectores ciegos:** un agente por lote. No sabe que hay trampas ni cuáles son los ids de la muestra.
  - Lee cada nodo entero contra su libro: los ficheros de `docs/fidelidad/INVENTARIO_LIBROS.json`, con la búsqueda
    de `docs/fidelidad/herramientas`, y para el mundo 11 `forja-lectura/fuentes`.
  - Marca cada defecto con su tipo, el campo, el fragmento y la evidencia (fichero y líneas).
- **Criterios**, con las definiciones de las instrucciones del mundo 11 (`docs/saneamiento/resultados/M11/`):
  - **contrario:** dice lo opuesto al libro;
  - **invención:** una causa, un efecto, una cifra o un contenido que el libro no dice;
  - **fase:** `fase_proyecto` contra la vara `docs/puente_forja/paso4/vara_fases.md`;
  - **dominio:** el espacio al que pertenece;
  - **condición:** una condición de activación que no describe cuándo aplica el nodo;
  - **etiqueta:** la `etiqueta_arbol` no es fiel al nodo o no está en segunda persona;
  - **ortografía;**
  - **matiz perdido;**
  - **calco del inglés;**
  - **regionalismo o glosario:** la tabla del glosario del mundo 11,
    `docs/saneamiento/resultados/M11/glosario/DECISIONES.md`, se aplica a todo el catálogo.
- **Árbitro:** un agente independiente relee contra el libro cada defecto marcado en un nodo de la muestra y lo
  confirma o lo rechaza. Solo cuenta lo confirmado. Las trampas se cuentan en la lectura: cazada es marcada con su
  tipo, o con un tipo que la cubre.
- **Regla de segunda lectura, fijada ahora:** si un lector no caza la trampa de su lote, ese lote entero lo relee un
  segundo lector independiente, y cuenta la unión de lo confirmado. Una trampa que tampoco caza el segundo lector se
  declara como fallo de método del criterio.
- **Sin texto de libro en el repositorio:** la evidencia se guarda como fichero y líneas.

## 4. Navegación sin IA (100 % del catálogo)

- **Murallas de dominio:** ninguna arista (`nodos_siguientes` o `nodos_previos`) une nodos vivos de dos mundos
  distintos. Un mundo solo toca el núcleo, por sus puentes.
- **Puentes:** todo mundo tiene al menos un puente al núcleo, y se cumple la ley del ancla (G3).
- **Puertas por mundo:** todo mundo tiene al menos una puerta. Toda puerta es un nodo vivo de su mundo con pregunta en
  la caché.
- **Alcanzabilidad:**
  - **Núcleo:** todo nodo vivo del núcleo se alcanza desde las semillas del núcleo por `nodos_siguientes`, dentro del
    núcleo.
  - **Mundo:** todo nodo vivo de un mundo se alcanza desde las puertas de ese mundo por `nodos_siguientes`, pasando
    por nodos del mundo o del núcleo, que es lo que recorre una sesión de mundo.
  - Se informa también el alcance desde las puertas del mundo sin pasar por el núcleo.
  - PASA con el 100 % en el núcleo y en cada mundo.

## 5. Veredicto

- **Veredicto por criterio:** cada criterio de las secciones 1, 2 y 4 queda en PASA o NO PASA.
- **Si algo no pasa:** se corrige por la doctrina, con una tanda declarada en cada nodo, y se vuelve a medir **solo ese
  punto**. Si es de la muestra, con semilla nueva escrita antes.
- **Vectores:** los nodos corregidos se re-embeben con Voyage. Después se comprueba que el índice sigue coherente:
  todo nodo vivo tiene vector, con la dimensión del índice, y los vectores nuevos son los de los nodos corregidos.
- **Certificación:** solo con todo en PASA, esta acta abre con "DATASET CERTIFICADO" y la fecha.

## 6. Resultados (medida 1, 28 sep 2026)

### 6.1 Guardas y navegación (100 % del catálogo)

| # | Guarda | Primera medida | Corrección por la doctrina | Estado |
|---|---|---|---|---|
| G1 | Gate 0 | OK | tras retirar las murallas: 3 componentes y OP-C-05 con 3 pares mutuos sin cita; tras las aristas y el registro de los 3 pares (clase C, LD-FINAL-001 a 003): OK | **PASA** |
| G2 | Alcanzabilidad | núcleo 1.410 de 1.410; mundos: 65 nodos de 7 mundos sin alcanzar desde sus puertas | 19 aristas verificadas a ciegas, en 3 rondas y con 8 de 8 trampas cazadas (tandas `final-aristas-1` y `final-aristas-2`). Quedan 2: `repartir_supervision_puesto_funcional_mision` (mundo 11) y `gestion_riesgo_seguridad_ia` (seguridad digital); ninguna de sus 18 candidatas se sostuvo | **NO PASA** (2 nodos) |
| G3 | Ley del ancla | 0 anclas con más de 2 puentes del mismo mundo | — | **PASA** |
| G4 | Aristas a deprecados | 0 | — | **PASA** |
| — | Murallas de dominio | 23 aristas entre dos mundos | retiradas (tanda `final-murallas`, 37 nodos): el acoplamiento mundo a mundo está prohibido (AUD-08) y ninguna sesión las recorre (AUD-09 M16) | **PASA** |
| G5 | Títulos y autores | en verde | — | **PASA** |
| G6 y G7 | Voz de libro y marcas | la guarda no cazaba la voz de exposición ni la etiqueta interna del aviso jurisdiccional; extendida con prueba en rojo, cazó 65 nodos | 3 tandas VOZ: `final-voz` (53 vivos), `final-voz-deprecados` (8) y `final-voz-3` (4, "al momento de la fuente") | **PASA** |
| G8 | Jurisdicción sin clase | 0 | — | **PASA** (U11) |
| G9 | Vigencia de traducciones | en verde (`web/lib/i18n/etiquetasVigencia.test.ts`); ninguna etiqueta cambió | — | **PASA** |
| G10 | Nada interno en el navegador | en verde | — | **PASA** |
| G11 | Puentes tejidos | en verde | — | **PASA** |
| G12 | Suites, tsc e índice | en verde; todo nodo vivo tiene vector | los 65 nodos corregidos esperan su vector nuevo de Voyage | **PASA** con el re-embebido pendiente |

**Sobre los 11 nodos antiguos con voz de libro del encargo:** el barrido previo, con el criterio escrito en la sección 2,
encontró 15 que hablan de su fuente o se exponen como libro. El resto de apariciones de "el texto", "el material" o
"capítulo" eran usos legítimos: el texto de una garantía, un material físico, el capítulo de un tratado. La lista está en
la tanda `final-voz` y en el commit 059422b8.

### 6.2 Muestra (200 nodos, 20 lotes)

- **Lectura:** los 220 nodos (200 de la muestra y 20 trampas) se cotejaron contra su libro; ninguno quedó sin pasaje.
- **Árbitro:** de 465 defectos marcados en nodos de la muestra, confirmó 406, reclasificó 5 y rechazó 54.
- **Trampas:** los lectores cazaron 19 de 20.
  - La de matiz del lote 20 (`funcion_identify_inventario_activos`: "una lista completa de todo el equipo, software y
    datos" pasa a "una lista del equipo y el software") no la cazaron ni el primer lector ni el segundo, que por la
    regla fijada antes releyó el lote entero.
  - **FALLO DE MÉTODO DECLARADO en el criterio matiz:** los lectores dejan pasar parte de los matices, así que la tasa
    de matiz es un mínimo.
- Evidencia en `docs/auditoria_final/`: defectos arbitrados, clave de trampas, aristas verificadas e instrucciones.

| # | Criterio | Confirmado en la muestra | Tasa | IC 95 % | Umbral | Veredicto |
|---|---|---|---|---|---|---|
| U1 | Contrarios | 4 | | | 0 | **NO PASA** |
| U2 | Invenciones | 25 | | | 0 | **NO PASA** |
| U3 | Fase | 10 nodos | 5,0 % | 2,7 a 9,0 % | ≤ 3 % | **NO PASA** |
| U4 | Dominio | 3 nodos | 1,5 % | 0,5 a 4,3 % | ≤ 2 % | **PASA** |
| U5 | Condiciones | 6 nodos | 3,0 % | 1,4 a 6,4 % | ≤ 2 % | **NO PASA** |
| U6 | Etiquetas | 12 nodos | 6,0 % | 3,5 a 10,2 % | ≤ 2 % | **NO PASA** |
| U7 | Ortografía | 39 nodos | 19,5 % | 14,6 a 25,5 % | ≤ 1 % | **NO PASA** |
| U8 | Matices perdidos | 99 | 0,50 por nodo | 0,40 a 0,60 | ≤ 0,2 | **NO PASA** (y es un mínimo) |
| U9 | Calcos | 144 | 0,72 por nodo | 0,61 a 0,85 | ≤ 0,2 | **NO PASA** |
| U10 | Regionalismos o glosario | 5 | 0,025 por nodo | 0,008 a 0,058 | ≤ 0,2 | **PASA** |

**Por espacio**, defectos confirmados. Solo el mundo 11, el único que pasó la certificación de contenido completa
(`docs/INTEGRACION_MUNDO_11.md`, sección 2), sale limpio.

| Espacio | Nodos | Contr. | Inv. | Matiz | Calco | Ortog. | Fase | Cond. | Etiq. |
|---|---|---|---|---|---|---|---|---|---|
| core | 45 | 1 | 8 | 23 | 53 | 21 | 2 | 5 | 6 |
| quality | 27 | 0 | 4 | 9 | 10 | 19 | 0 | 0 | 1 |
| primer_equipo (mundo 11) | 22 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 1 |
| environmental | 17 | 2 | 2 | 5 | 14 | 11 | 1 | 0 | 0 |
| health_safety | 16 | 0 | 0 | 7 | 10 | 0 | 0 | 0 | 3 |
| franquicias | 14 | 0 | 0 | 13 | 14 | 3 | 2 | 2 | 0 |
| exportacion | 13 | 0 | 1 | 12 | 9 | 10 | 1 | 0 | 0 |
| entrega | 12 | 1 | 7 | 7 | 5 | 13 | 1 | 0 | 0 |
| risk_management | 12 | 0 | 1 | 7 | 0 | 0 | 1 | 0 | 0 |
| compras | 11 | 0 | 1 | 7 | 5 | 20 | 2 | 0 | 1 |
| seguridad_digital | 11 | 0 | 1 | 9 | 23 | 5 | 0 | 0 | 0 |

### 6.3 Veredicto de la medida 1

**NO CERTIFICADO.**
- **No pasan en la muestra:** U1, U2, U3, U5, U6, U7, U8 y U9.
- **No pasa en la navegación:** G2, con 2 nodos.

Lo demás pasa. Los defectos de contenido no son de unos pocos nodos: se reparten por los 10 espacios que no pasaron la
certificación del mundo 11. Por la doctrina, corregir solo los 200 nodos de la muestra no bastaría, porque la próxima
muestra, con semilla nueva, volvería a caer. El remedio es el método que certificó el mundo 11, aplicado a los 3.169
nodos vivos restantes. Su alcance y su coste los decide el fundador antes de empezar.

## 7. Diagnóstico de los defectos confirmados (solo lectura, 28 sep 2026) y propuesta de remedio SIN LANZAR

Encargo del fundador tras la medida 1. **Nada de esta sección cambia el dataset:** la campaña de remedio espera su
visto. Base del diagnóstico: los 411 defectos que el árbitro confirmó o reclasificó
(`docs/auditoria_final/defectos_arbitrados.json`; 406 confirmados y 5 reclasificados).

### 7.1 Reparto por campo, para cada criterio

| Criterio | Pasos | Resumen | Entregable | Condiciones | Título | Etiqueta | Fase o dominio |
|---|---|---|---|---|---|---|---|
| Contrario | 0 | **4** | 0 | 0 | 0 | 0 | |
| Invención | 2 | **22** | 1 | 0 | 0 | 0 | |
| Fase | | | | | | | 10 |
| Dominio | | | | | | | 3 |
| Condición | | | | 7 | | | |
| Etiqueta | | | | | | 12 | |
| Ortografía | 2 | **44** | 0 | **42** | 3 | 11 | |
| Matiz | 44 | 53 | 2 | 0 | 0 | 0 | |
| Calco | 55 | 57 | 17 | 7 | 8 | 0 | |
| Regionalismo | 3 | 1 | 0 | 1 | 0 | 0 | |

**Por espacio** (defectos confirmados; nodos de la muestra entre paréntesis):

| Criterio | core (45) | quality (27) | mundo 11 (22) | environmental (17) | health_safety (16) | franquicias (14) | exportacion (13) | entrega (12) | risk_management (12) | compras (11) | seguridad_digital (11) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Contrario | 1 | 0 | 0 | 2 | 0 | 0 | 0 | 1 | 0 | 0 | 0 |
| Invención | 8 | 4 | 0 | 2 | 0 | 0 | 1 | **7** | 1 | 1 | 1 |
| Matiz | 23 | 9 | 0 | 5 | 7 | 13 | 12 | 7 | 7 | 7 | 9 |
| Calco | 53 | 10 | 1 | 14 | 10 | 14 | 9 | 5 | 0 | 5 | 23 |
| Ortografía | 21 | 19 | 0 | 11 | 0 | 3 | 10 | 13 | 0 | **20** | 5 |

Fase, condiciones y etiquetas, por espacio, en la tabla de la sección 6.2.

### 7.2 Los 4 contrarios y las 25 invenciones contra el registro de la campaña de fidelidad

**Qué leyó la campaña de fidelidad** (`docs/fidelidad/INFORME_FINAL_CAMPANIA.md`):
- **Los pasos:** los 15.311 pasos vivos, con al menos dos lecturas ciegas cada uno (secciones 1 y 2).
- **Los demás campos que llegan a la persona** (resumen, entregable, condiciones, título y etiqueta): una pasada aparte
  (sección 10) que buscaba **solo contrarios y añadidos de cifra, plazo o norma**. El propio informe declara: "en esos
  campos no se buscaron añadidos prácticos".
- **Cómo se decidió cada nodo en esa pasada:** según `docs/fidelidad/campania/campos/VEREDICTOS_CAMPOS.jsonl`, un nodo
  limpio y no muestreado quedaba decidido con **una sola lectura** ("lector (limpio no muestreado)").

| Dónde está el defecto | Cómo lo decidió la campaña | Contrarios | Invenciones |
|---|---|---|---|
| Resumen | una sola lectura ("lector (limpio no muestreado)") | 4 | 19 |
| Resumen | lector y verificador de acuerdo | 0 | 3 |
| Entregable | una sola lectura | 0 | 1 |
| Pasos (`observar_al_cliente_en_su_contexto` p3, `cierre_de_ciclos_industriales` p4) | **dos lecturas, veredicto OPERATIVO** (`campania/c2/VEREDICTOS_CAMPANIA.jsonl`) | 0 | 2 |

**Lectura:**
- **27 de los 29 están en campos que no pasaron por doble lectura con libro:** 26 los decidió una sola lectura, y los
  3 que tuvieron dos buscaban solo cifra, plazo o norma. La mayoría de las invenciones confirmadas son de causa, efecto
  o contenido, justo lo que esa pasada no buscaba.
- **Los 2 de pasos son un desacuerdo de vara:** la campaña los dio por OPERATIVOS con dos lecturas y este árbitro los
  da por invención. La frontera entre OPERATIVO e invención se arbitra en el remedio.
- **Ninguno está en un paso que la campaña marcara FIEL con dos lecturas.**

### 7.3 Defectos anteriores o introducidos por correcciones posteriores

Para cada defecto se miraron las correcciones declaradas de su campo. Si el fragmento aparece en un texto nuevo y no
en el anterior, lo introdujo esa corrección. La comparación es por fragmento, así que la atribución es aproximada.

- **398 de 411 son anteriores:** vienen de la extracción. 373 están en campos que ninguna corrección tocó y 21
  sobrevivieron a una corrección del mismo campo. En 4 más el fragmento no aparece en ningún texto de corrección.
- **13 los introdujo una corrección posterior:**

| Corrección | Qué introdujo |
|---|---|
| Tanda `n1-condicion` (condiciones reescritas, COHERENCIA) | 5 faltas de ortografía |
| Tanda `n1-orto` (ortografía) | 2 matices perdidos |
| Limpieza del mundo 11 (`m11-limpieza`) | 2 regionalismos |
| Tandas de fidelidad `fidelidad-t1`, `fidelidad-t7` y `fidelidad-t15` | 1 invención, 1 calco y 1 matiz |
| Tanda `n1-fase` | 1 fase |

### 7.4 Ortografía: las dos varas

- **La pasada O** (`docs/SANEAMIENTO_DATASET.md`, punto 16):
  - leyó 21.649 textos de **etiquetas, pasos y entregables** y las preguntas de la caché;
  - hizo 1.036 correcciones;
  - su residuo del 1,3 % es de **faltas**: 3 que el primer lector no vio sobre 227, en 1 de cada 5 lotes;
  - **no cubrió ni el resumen, ni las condiciones de activación, ni el título.**
- **Esta medida** cuenta **nodos** con al menos una falta confirmada, en **todos** los campos que ve la persona.

| | Nodos con falta | Tasa |
|---|---|---|
| Todo lo confirmado | 39 | 19,5 % |
| Sin las mayúsculas a la inglesa de las etiquetas | 34 | 17 % |
| Solo en resumen, condiciones y título (fuera de la pasada O) | 32 | 16 % |
| Solo en los campos que la pasada O sí cubrió | 4 | 2 % |

- **Cuál es la correcta:** las dos lo son para lo que miden. La del umbral U7 (≤ 1 % de nodos) es la de esta medida,
  porque cuenta todo lo que ve la persona. La pasada O dejó limpios sus campos (2 %, en el orden de su residuo); lo que
  falla es lo que nunca leyó.
- **Una decisión de vara que es del fundador:** 3.541 de las 3.634 etiquetas vivas usan mayúsculas interiores a la
  inglesa ("Traza tu Plan de Exportación"). Es el estilo de hecho, sin regla escrita, y la ortografía académica pide
  minúscula. Los lectores marcaron algunas (8 confirmadas). Hay que decidir si es estilo de la casa (se escribe la regla
  y no cuenta como falta) o falta (1 tanda mecánica sobre las 3.541).
- **Qué es mecánico:**
  - el 70 % de las faltas confirmadas son tildes que faltan;
  - en todo el catálogo hay **1.231 palabras sin tilde, en 305 nodos**, cuya forma con tilde domina en el propio
    catálogo ("decision", "pais", "despues", "segun", "tambien", "garantia", "operacion"…): 899 en resúmenes y 264 en
    condiciones;
  - una lista curada de formas sin ambigüedad las corrige de forma mecánica y declarada (veredicto ORTOGRAFIA);
  - quedan para la lectura las ambiguas ("critica", "especifica", "limites" también son verbos; que/qué, esta/está) y
    las faltas que no son de tilde (unas 30 de las 102).

### 7.5 Propuesta de remedio, por orden de daño (SIN LANZAR: espera el visto del fundador)

Todas las etapas siguen la doctrina de siempre:
- **Correcciones:** tandas declaradas en `correcciones`, que no borran nada.
- **Método de lectura:** trampas sin marca plantadas antes de todo contexto, clave fuera de lo que leen los agentes,
  semilla escrita antes y árbitro en los desacuerdos.
- **Regla de parada:** una muestra ciega nueva por etapa, con su umbral. Si no cumple, se relee lo del mismo libro o
  espacio que falló, no otra pasada completa.
- **Voyage:** al final de todo, una sola pasada con todos los nodos corregidos (decisión del fundador).
- **Coste:** en agentes. La lectura de esta auditoría gastó unos 100.000 a 130.000 tokens por lector de 11 nodos con
  libro.

| Etapa | Criterio | Alcance | Método | Regla de parada | Coste estimado |
|---|---|---|---|---|---|
| 1 | Contrarios e invenciones | Resumen y entregable de los 3.169 nodos vivos fuera del mundo 11 (ahí están 27 de los 29); los pasos, solo los OPERATIVOS de la frontera | Doble lectura ciega contra el libro buscando contrario e invención de cualquier tipo (causa, efecto, cifra, contenido), no solo cifra, plazo o norma; árbitro en los desacuerdos. Antes, el fundador fija la frontera OPERATIVO/invención con los 2 casos de pasos | Muestra ciega de 150 nodos, semilla nueva: 0 contrarios y 0 invenciones | Lotes de 12 nodos: ~265 lotes × 2 lectores ≈ **530 agentes**, más ~50 árbitros y ~10 de verificación extra: **unos 590** |
| 2 | Fase, condiciones y etiquetas | Los 3.169 nodos | Sin libro: la fase contra la vara, las condiciones contra el propio nodo, la etiqueta contra el nodo. Un lector por lote y un verificador ciego en 1 de cada 4 lotes | Muestra de 200: fase ≤ 3 %, condiciones ≤ 2 %, etiquetas ≤ 2 % | Lotes de 25: ~127 lectores, ~32 verificadores y ~10 árbitros: **unos 170** |
| 3 | Ortografía | Resumen, condiciones y título de los 3.169 nodos (lo que la pasada O no cubrió) | Primero, lo mecánico: la lista curada de tildes sin ambigüedad (unas 1.000 correcciones en ~300 nodos) y, si el fundador lo decide así, las mayúsculas de etiqueta. Un verificador ciego muestrea el 5 %. Después, un lector por lote para lo ambiguo y lo que no es tilde | Muestra de 200: ≤ 1 % de nodos | Lo mecánico, **0 agentes** (script y prueba) más ~5 de verificación; la lectura en lotes de 30: ~106 lectores y ~20 de segunda lectura: **unos 130** |
| 4 | Matices y calcos | Pasos, resumen y entregable de los 3.169 nodos | Matices, contra el libro, con listas dirigidas por nodo como en el mundo 11. Calcos: primero un detector con la tabla del glosario más los calcos confirmados en esta muestra, luego lectura | Muestra de 200: matices ≤ 0,2 por nodo y calcos ≤ 0,2 por nodo; la trampa de matiz tiene que cazarse | Matices: ~265 lotes con libro, **unos 300 agentes**. Calcos sin libro: **unos 130** |

- **Total estimado:** unos **1.300 agentes**, más de 100 millones de tokens de subagente.
- **Alternativa que ahorra una pasada entera con libro:** leer matices dentro de la etapa 1, porque ya se tiene el
  libro abierto en los mismos campos. Las correcciones se aplicarían igual en el orden de daño. Quedaría en unos 1.000
  agentes.
- **Por qué un pase entero y no solo los nodos de la muestra:** los defectos se reparten por todos los espacios fuera
  del mundo 11 (sección 6.2). Corregir la muestra y volver a medir con semilla nueva volvería a caer.
- **Lo que no se toca:** el mundo 11. Su método de certificación es el que esta propuesta aplica al resto.

## 8. Decisiones del fundador del 28 sep 2026: las puertas y el BANCO

### 8.1 Los 2 nodos sin alcanzar pasan a ser puertas (G2)

Decisión: cada uno entra como puerta de su mundo con una condición precisa, verificada a ciegas con trampas sin marca.
Evidencia completa (lo que vio el lector, sus veredictos y el papel de cada caso) en
`docs/auditoria_final/puertas_verificacion.json`.

**Método:** un lector ciego por ronda, con las instrucciones de siempre para puertas (condición `precisa`/`vaga`/
`no_corresponde`; pregunta `adecuada`/`floja`/`no_corresponde`). Cada ronda lleva dos trampas bajo ids reales que no
son puerta, sorteadas antes de armar el paquete (una con condición mala y otra con pregunta mala). La clave queda fuera
de lo que lee el lector.

| Ronda | Caso | Condición | Pregunta | Resultado |
|---|---|---|---|---|
| 1 | `repartir_supervision_puesto_funcional_mision`, pregunta escrita a mano | precisa | **floja** | Suponía un equipo sin condicional y encadenaba dos preguntas. Se reescribe |
| 1 | `gestion_riesgo_seguridad_ia`, pregunta base de la caché | precisa | **no_corresponde** | Ver abajo: queda para el fundador |
| 1 | Trampa de condición (`csf_funcion_recover`) | vaga | no_corresponde | **Cazada** |
| 1 | Trampa de pregunta (`fijar_proceso_trabajo_equipo`) | precisa | no_corresponde | **Cazada** |
| 2 | `repartir_supervision_puesto_funcional_mision`, pregunta reescrita | precisa | **adecuada** | **Pasa** |
| 2 | Trampa de condición (`definir_que_cuenta_como_dano_antes_de_probar_empaque`) | no_corresponde | adecuada | **Cazada** |
| 2 | Trampa de pregunta (`wizard_of_oz_testing`) | precisa | no_corresponde | **Cazada** |
| 2 | Control: puerta vigente `accion_correctiva` con su pregunta base | precisa | floja | Ver abajo |

- **`repartir_supervision_puesto_funcional_mision` es puerta de Primer Equipo** (la vigésima). Su pregunta es nueva y
  se AÑADE a la caché, porque el nodo no tenía ninguna (Principio 2): "Si alguien de tu negocio responde a la vez a dos
  personas o a dos áreas, ¿cómo está repartido hoy entre ellas quién le marca las prioridades y quién cuida que haga
  bien su oficio?". Su versión neutral la genera la corrida final (tope de `cacheNeutrales.test.ts` de 3.287 a 3.288,
  declarado). No tiene sucesores: la salida la da el motor (AUD-09 H13). Primer Equipo queda alcanzable al 100 %.
- **`gestion_riesgo_seguridad_ia` NO entra todavía.** Su condición pasa, pero su pregunta base de la caché ("Más allá de
  protegerse contra estos ataques, ¿qué tan preparada está tu idea para que las personas […] confíen realmente en las
  decisiones […] de la IA?") sale `no_corresponde`: da por trabajado el concepto, salta al siguiente y supone un
  equipo. El Principio 2 prohíbe tocar una base, así que no la cambio. **Decide el fundador.**
- **Una duda de vara que se ve en las dos rondas:** las preguntas base se escribieron para elegir entre los siguientes
  y por eso miran al concepto que viene. El lector de puertas pide que la primera pregunta parta del concepto de la
  puerta. Con esa vara fallan también dos bases vigentes: la de `csf_funcion_recover` (la pregunta real de la trampa de
  condición de la ronda 1, `no_corresponde`) y la del control `accion_correctiva` (`floja`). No es un defecto de estas
  dos puertas: es una pregunta de diseño para el fundador (¿la primera pregunta de una puerta es la base del nodo o
  necesita la suya propia?).
- **G2 tras esta decisión:** `scripts/auditoria_final/navegacion.py` queda en rojo por 1 nodo
  (`gestion_riesgo_seguridad_ia`, seguridad digital, 52 de 53). Gate 0 OK.

### 8.2 El choque del BANCO con la regla sin fuentes

Seis pasajes de `docs/BANCO_DE_TEXTOS.md` decían que el plan cita libro y capítulo en el detalle de cada concepto (§3,
§5, §6 y dos notas de §7). Quedan tachados con su corrección declarada, por la regla de `AGENTS.md` del 26 sep 2026, y
el claim "cada plan cita su fuente" pasa a PROHIBIDO en §6. **Ningún prompt pide citar libro, capítulo ni autor:**
`SYSTEM_PLAN` dice "sin autores" y prohíbe "fuentes nuevas que no esten en el material". `docs/REGLAS_DE_LA_CASA.md`
marca el choque como resuelto (commit 2f7285ec).

## 9. El remedio (visto del fundador, 28 sep 2026)

Decisiones del fundador sobre el diagnóstico de la sección 7. El remedio va por orden de daño. **Todo lo de esta
sección, del 9.1 al 9.5, se escribe y se commitea ANTES de leer nada:** el diseño, las semillas, las trampas y las reglas de
parada. Sigue sin ninguna llamada a Anthropic. Voyage, una sola pasada al final del remedio.

### 9.1 La frontera entre lo operativo y la invención (C29 y R6 de `docs/REGLAS_DE_LA_CASA.md`)

- **OPERATIVO:** concreta el cómo (orden, formato, herramienta común) sin afirmar nada nuevo. Se queda.
- **INVENCIÓN:** añade un qué, un por qué o un cuánto que el libro no dice (hecho, causa, cifra, plazo, resultado
  prometido), o endurece lo que el libro dice con cautela. Sale, o pasa a "Sugerencia de My Idea:" si es un consejo
  práctico útil.

**Los 2 casos de pasos del diagnóstico (7.2), reclasificados con esta regla:** los dos son INVENCIÓN y se corrigen en
la tanda `final-frontera`, declarada en cada nodo con su cita:
- `observar_al_cliente_en_su_contexto`, paso 3: "esas pepitas de oro que valen más que cualquier encuesta" añade una
  comparación que el libro no hace. Queda: "son las pepitas de oro que pueden cambiar el rumbo de la relación con tu
  cliente".
- `cierre_de_ciclos_industriales`, paso 4: "como insumo principal" endurece un consejo que el libro da con cautela. Sale
  "principal".

### 9.2 Las mayúsculas de las etiquetas (C30)

Se quedan: la mayúscula de rótulo es estilo de la casa, sin tanda de corrección. Los lectores de ortografía no la
cuentan como falta. Las 8 faltas de la medida 1 que eran solo eso dejan de contar.

### 9.3 Antes de la etapa 1: las tildes mecánicas

- **Qué entra:** solo las palabras que SIEMPRE llevan tilde, sin otra lectura posible sin ella (por ejemplo "decision",
  "pais", "despues", "tambien", "garantia"). Un script las propone a partir de las formas con tilde del propio catálogo.
  Reviso a mano toda la lista de palabras antes de aplicar nada, y el script solo corrige las que quedan en ella.
- **Qué no entra:** las palabras ambiguas van a los lectores ("solo", "este", "tu", "si", "mas", "el", "aun", que/qué,
  esta/está, como/cómo, "critica", "practica", "publico", "calculo", "continua", "limites", "numero" y similares).
  Tampoco entran las palabras dentro de un nombre en inglés ("Decision Day", "Mission", "Commission").
- **Dónde:** en los campos que ve la persona o la IA: el resumen, los pasos, las condiciones, el entregable, la
  etiqueta y el título (el aplicador admite ORTOGRAFIA en el título).
- **Cómo:** una tanda ORTOGRAFIA declarada por campo y nodo, con una prueba en rojo primero sobre la lista curada.

### 9.4 Etapa 1: contrarios, invenciones y matices, ENTERA, con doble lectura

- **Universo:** los 3.169 nodos vivos fuera del mundo 11.
- **Campos juzgados:** el resumen, los pasos y el entregable, que es donde el diagnóstico sitúa los tres defectos
  (tabla 7.1). El lector ve el nodo entero para entenderlo.
- **Lotes:**
  - Hasta 12 nodos, todos del mismo libro (su `fuentes_internas`). Hay 61 libros y salen 297 lotes.
  - Cada libro se parte en `ceil(n/12)` lotes casi iguales, en orden de `node_id`.
  - El orden de lectura de los lotes se sortea con `random.Random(20260930)`.
- **Trampas sin marca, plantadas antes de generar ningún paquete.** Hay 1 por lote, en la COPIA del lector de un nodo
  del propio lote, nunca en el dataset. El nodo se sortea con `random.Random(20260930 + 1000 + lote)`. El tipo va por
  turnos según el número de lote:
  - **Contrario:** un par de antónimos cambiado en el resumen ("aumenta"/"reduce", "antes de"/"después de"…).
  - **Invención de cifra:** una frase con una cifra o un plazo inventados, añadida al resumen.
  - **Invención por endurecer:** un "puede", "suele" o "a menudo" que pasa a "debe", "siempre" o "siempre".
  - **Matiz:** un elemento que se cae de una enumeración del resumen o de un paso.

  Si el nodo sorteado no admite el tipo, se prueba el siguiente del lote. La clave vive en
  `auditoria-final-claves/remedio/`, que no lee ningún agente.
- **Lectores:** dos lectores ciegos independientes (A y B) por lote, con el mismo paquete.
  - Cada uno marca contrario, invención (con la frontera 9.1) y matiz, con fichero y líneas de evidencia.
  - Cada uno propone el texto corregido con el cambio mínimo: quitar lo inventado, devolver el matiz, o pasar un
    consejo útil a "Sugerencia de My Idea:".
- **Trampa cazada:** alguno de los dos lectores marca el fragmento plantado con cualquiera de los tres tipos de la
  etapa.
- **Regla de relectura:** si ninguno de los dos caza la trampa de su lote, un tercer lector independiente relee el lote
  entero y cuenta la unión. Si el tercero tampoco la caza, se declara fallo de método en ese lote.
- **Árbitro:** relee contra el libro la unión de lo que marcaron los lectores fuera del fragmento plantado.
  - Decide confirmado, reclasificado o rechazado.
  - En lo confirmado, escribe el texto final con su cita (fichero, líneas y una frase de 15 palabras como mucho).
  - Los paquetes de arbitraje juntan lotes del mismo libro.
- **Aplicación:** tandas declaradas `final-e1-*` con `scripts/fidelidad/aplicar_correcciones.py`, con estos veredictos:
  - contrario → CONTRARIO;
  - invención y matiz → ANADIDO, como en el mundo 11.

  El aplicador se niega si el texto viejo no es el vigente.
- **Regla de parada (fijada ahora):**
  - **La muestra:** 150 nodos del mismo universo, estratificada por espacio (8 como mínimo por espacio y el resto por
    restos mayores), con semilla 20261001. La leen dos lectores y un árbitro con el mismo método, en 15 lotes de 10
    con una trampa sin marca cada uno.
  - **PASA con:** 0 contrarios, 0 invenciones, matiz ≤ 0,2 por nodo, y todas las trampas de matiz cazadas.
  - **Si no pasa:** se releen los lotes del libro o del espacio donde cayó lo confirmado, y se mide otra muestra con
    semilla 20261001 + k (k = 1, 2…).

### 9.5 Etapas 2 a 4, hasta donde alcance la cuota, cerrando siempre en un punto limpio

| Etapa | Criterio | Método | Regla de parada (fijada ahora) |
|---|---|---|---|
| 2 | Fase, condiciones y etiquetas | Sin libro, lotes de 25 del mismo espacio, 1 lector y un verificador ciego en 1 de cada 4 lotes, 1 trampa por lote, árbitro en lo marcado | Muestra de 200, semilla 20261002: fase ≤ 3 %, condiciones ≤ 2 %, etiquetas ≤ 2 % |
| 3 | Ortografía (lo que dejan las tildes mecánicas: ambiguas y faltas que no son de tilde) | Lotes de 30, 1 lector, segunda lectura de 1 de cada 5 lotes, 1 trampa por lote | Muestra de 200, semilla 20261003: ≤ 1 % de nodos, sin contar C30 |
| 4 | Calcos | Un detector con la tabla del glosario y los calcos confirmados en la medida 1 y en la etapa 1, y después lectura en lotes de 30 con 1 trampa por lote | Muestra de 200, semilla 20261004: ≤ 0,2 por nodo |

**El certificado:** al acabar, una medida 2 de todos los criterios, con el diseño de la sección 3 y semilla 20261010.

### 9.6 Resultados del remedio (se añaden a medida que avanza)

**Tildes mecánicas (9.3), 28 sep 2026:**
- **La lista:** `docs/saneamiento/ortografia/tildes_mecanicas.json`, 451 palabras revisadas a mano sobre 707
  candidatas. Salieron las que tienen otra lectura sin tilde (formas verbales como "negocio" o "llegara", adjetivos
  como "seria" o "continua", "periodo", que admite las dos) y las que llevan tilde en más de un sitio ("diseno", "dano",
  "envio", "guia").
- **La tanda:** `final-tildes`, 450 correcciones ORTOGRAFIA declaradas en 247 nodos: 222 en condiciones, 206 en
  resúmenes, 16 en títulos, 3 en etiquetas, 2 en entregables y 1 en pasos. Los nombres en inglés ("Decision Log",
  "Cash Conversion Cycle", "Discovery/Decision Day") se quedan.
- **La guarda:** `engine/test_tildes_mecanicas.py` hace que ningún nodo vivo vuelva a traer una palabra de la lista.
  Gate 0 y las dos suites pasan.

**Puertas con pregunta de entrada (punto 3 del fundador), 28 sep 2026:**
- **El motor:** la pregunta de entrada vive en un campo aparte de la caché (`pregunta_entrada`). Sale al entrar a un
  mundo y al reelegir puerta; la base no se toca (Principio 2). El adaptador la trata igual que las demás, y su salida
  segura es ella misma.
- **Las preguntas:** 86, las 85 puertas de los mundos más `gestion_riesgo_seguridad_ia`. Cuatro redactores las
  escribieron leyendo cada nodo.
- **La verificación ciega:** 9 lotes con 10 trampas sin marca bajo ids reales que no son puerta (otro tema, papeles
  supuestos, genérica, dos preguntas encadenadas, salto al siguiente). **Las 10 cazadas.**
  - 79 salieron adecuadas a la primera.
  - 7 salieron flojas; se reescribieron con el reparo del lector y pasaron en la segunda ronda.
  - Un ajuste posterior sin reverificar: la de `responder_critica_abrasiva_cuatro_reglas` quita el supuesto de género.
  - Evidencia en `docs/auditoria_final/preguntas_entrada.json`.
- **`gestion_riesgo_seguridad_ia` entra como puerta de Seguridad Digital:** G2 pasa. La navegación queda en verde, con
  alcanzabilidad del 100 % en el núcleo y en cada mundo, y pasa a ser guarda permanente de la suite
  (`engine/test_navegacion_catalogo.py`).
- **Lo que queda para la etapa 2:** los lectores marcaron 14 condiciones de entrada de puertas como vagas o como un
  punto intermedio. Van a la etapa 2 (condiciones), con su método.

**Etapa 1, cambios de método declarados mientras corre (antes de que los lotes afectados se leyeran):**
- **Instrucciones v2 del lector, desde el lote 17 y en los terceros lectores:**
  - Tras los 9 primeros lotes, las trampas de endurecer y de matiz no las cazaba ningún lector.
  - Se añade una comprobación obligatoria nodo a nodo de enumeraciones y de grados de certeza, con un campo `cotejo`
    que la deja escrita.
  - Los lotes 1 a 16 se leyeron con la v1.
- **Trampas v2, desde el lote 25, que nadie había abierto:**
  - **El defecto de diseño:** el `cotejo` mostró que los lectores sí veían las diferencias. La trampa de matiz quitaba
    un elemento de una lista que muchas veces no cambia el consejo ("y otros costos" lo cubría). La de endurecer caía a
    veces dentro de una pregunta.
  - **El arreglo:** desde el lote 25, el matiz quita una condición o una excepción ("salvo que…", "solo si…"), que
    siempre cambia el consejo. Endurecer va solo en el resumen, con "siempre va a", y nunca tras un clítico.
  - Las trampas y los paquetes de los lotes 1 a 24 no cambian. La cuenta de trampas se da por versión.

**Etapa 1, reanudación tras el límite semanal de cuota (decisión del fundador, 29 sep 2026):**
- **Lo que cayó:** los árbitros de los paquetes 62 a 66 y los lectores de los lotes 88 a 95, a mitad de trabajo.
- **Cuarentena:** sus salidas a medias (lecturas 90a, 93a, 93b, 94a y 95a y el fallo 64) quedan fuera del repo y no se
  tomaron como válidas en ninguna tanda ni paquete. Esos trabajos se relanzan desde cero, en Opus.
- **La quinta tanda** aplica los arbitrajes 57 a 61.

**Piloto de lectores en Sonnet (fijado ANTES de lanzar ningún lector del piloto):**
- **Diseño:** los 10 lotes siguientes en el orden de lectura, del 96 al 105, con sus trampas sin marca v2. Los DOS
  lectores en el Sonnet más reciente; el árbitro, en Opus 5.5, con el método de siempre.
- **Umbral 1:** los lectores del piloto cazan el 100 % de las trampas (10 de 10, por A o por B, sin tercer lector).
- **Umbral 2:** el árbitro confirma en el piloto al menos el 90 % de los hallazgos reales que confirma a los lectores de
  Opus en lotes comparables.
  - **Hallazgo real confirmado:** un elemento del nodo (resumen, paso o entregable) con al menos una marca confirmada
    o reclasificada por el árbitro.
  - **Base de Opus por lote:** los confirmados por nodo de los lotes del mismo libro leídos por Opus con las
    instrucciones v2 (61 lotes arbitrados). Para los libros sin lotes previos (The Founder's Dilemmas, lotes 100 y 103;
    NIST SP 1318, lote 102) se usa la base global de Opus: 804 confirmados en 665 nodos, 1,209 por nodo.
  - **Esperado en los 10 lotes:** 128,6 confirmados (suma de nodos del lote por su base). **Pasa con 115,7 o más.**
- **Si pasan los dos umbrales,** todos los lectores de la etapa pasan a Sonnet. **Si no,** pareja mixta: un lector
  Opus y uno Sonnet. Los árbitros y el agente principal siguen en Opus 5.5. La muestra ciega final que certifica, en
  Opus.

**Resultado del piloto Sonnet (29 sep 2026; árbitros en Opus, paquetes 67 a 74):**
- **Umbral 1, PASA:** 10 de 10 trampas cazadas, y por los DOS lectores en cada lote (20 de 20), sin tercer lector.
- **Umbral 2, NO PASA:** 76 hallazgos reales confirmados contra 115,7 exigidos (128,6 esperados; 59 %).

  | Lote | Nodos | Esperado | Confirmados |
  |---|---|---|---|
  | 96 | 11 | 12,9 | 6 |
  | 97 | 12 | 15,5 | 10 |
  | 98 | 12 | 8,7 | 8 |
  | 99 | 10 | 10,0 | 3 |
  | 100 | 12 | 14,5 | 7 |
  | 101 | 11 | 9,2 | 8 |
  | 102 | 12 | 14,5 | 8 |
  | 103 | 11 | 13,3 | 3 |
  | 104 | 12 | 15,5 | 14 |
  | 105 | 11 | 14,5 | 9 |

- **Contraste informativo, no es el umbral:** los lotes 88 a 95, leídos por Opus y arbitrados en los mismos paquetes,
  dan 82 confirmados en 92 nodos (0,891 por nodo). El piloto da 76 en 114 (0,667 por nodo), el 75 % de esa cifra. No
  pasaría ni contra ese contraste, así que el veredicto no depende de la base elegida.
- **Lo que mide:** Sonnet es preciso, con 128 de 134 marcas confirmadas (Opus: 162 de 173), pero encuentra menos.
- **Incidencia de forma:** la lectura 102a salió como JSON inválido (rutas de Windows sin escapar). Se reparó solo el
  escape de las rutas, sin tocar el contenido, y el original queda en la cuarentena de claves. Desde el lote 106 la
  consigna del lector pide rutas escapadas.
- ~~**Consecuencia, por la regla fijada antes:** pareja mixta desde el lote 106, con el lector A en Opus y el lector B
  en Sonnet.~~ *Superado por la decisión del fundador del 30 sep 2026, abajo.* Los árbitros, el agente principal y la muestra de parada siguen en Opus. Los lectores B de los lotes 106
  a 117 se lanzaron en Sonnet mientras se arbitraba el piloto, porque ambos resultados posibles ponían un Sonnet en
  ese puesto.
- **Sexta y séptima tandas:** los arbitrajes 62 a 66 y 67 a 74, incluido el piloto.

**Decisión del fundador (30 sep 2026): Sonnet queda fuera de la etapa 1, sin pareja mixta.**
- **Motivo:** Sonnet caza las trampas, pero el árbitro solo confirma el 59 % de los hallazgos esperados. Para un
  saneamiento que tiene que certificar, un lector que deja pasar cuatro de cada diez defectos reales no sirve, ni
  siquiera como segundo lector.
- **Configuración:** todos los lectores, los árbitros y la muestra de parada, en Opus 5.5.
- **Lotes 96 a 105 (el piloto):** se releen con dos lectores Opus y se arbitran.
  - Las correcciones del piloto ya aplicadas en la séptima tanda se conservan; se añaden las que falten.
  - El paquete de cada lote se rehace sobre el texto VIGENTE, con la misma trampa sin marca: el fragmento plantado sigue
    presente en los 10 nodos. El orden del paquete sale de la misma semilla. Los paquetes del piloto quedan en las claves.
- **Lotes 106 a 117:** las lecturas B en Sonnet no cuentan como lectura. Cada lote lleva sus dos lectores Opus.
- **Qué pasa con las 32 lecturas Sonnet** (96 a 105 A y B; 106 a 117 B): salen del circuito, se guardan fuera del repo
  y no entran en ninguna tanda ni paquete. Sus trabajos vuelven a la cola.

**Etapa 1, cierre de la lectura (30 sep 2026), fijado ANTES de sortear la muestra de parada:**
- **Fallo de método declarado (regla de relectura, 9.4):** en 10 lotes ninguno de los tres lectores cazó la trampa
  sin marca: 128, 149, 175, 181, 189, 197, 228, 240, 241 y 268. Nueve son del tipo contrario y casi todos cambian
  "antes de" por "después de" (la 175 dejó además una frase agramatical); la 228 es de matiz. El patrón se anota para
  la medida 2: el cambio de orden temporal es el punto ciego de la lectura contra el libro.
- **Correcciones FUERA:** el árbitro las confirmó, pero su texto no pasó los filtros de la tanda (una baranda nueva,
  contenido de país en un nodo sin clase de jurisdicción, el largo del resumen o la cita). El hallazgo no se reabre:
  - Un reescritor Opus recibe el texto vigente, el del árbitro, las razones confirmadas, la cita, la regla que no
    pasa y el fragmento que la dispara. Escribe un texto que conserve el arreglo y cumpla la regla, o lo deja en null
    con su motivo.
  - Su texto vuelve a pasar los mismos filtros (`tanda_e1.py`) y se aplica en una tanda `final-e1-fuera` con las
    marcas del árbitro original.
- **Detalle del sorteo de la muestra de parada (semilla 20261001, regla de 9.4):**
  - **Universo:** los 3.169 nodos vivos fuera del mundo 11, con el texto que quede tras la tanda FUERA.
  - **Reparto:** 8 por espacio y los 70 restantes en proporción al tamaño del espacio, por restos mayores. Sale: core
    39, quality 23, environmental 14, health_safety 14, franquicias 12, exportacion 11, entrega 10, risk_management 9,
    compras 9 y seguridad_digital 9.
  - **Sorteo:** espacios en orden de tamaño descendente (empate por nombre); dentro de cada uno, ids en orden
    alfabético y `random.Random(20261001 + índice del espacio)`.
  - **Lotes:** los 150 se barajan con `random.Random(20261001)` y se parten en 15 lotes de 10. Un lote mezcla libros;
    cada nodo trae sus ficheros.
  - **Trampas:** una por lote, con el mismo plantado v2 de la etapa. El nodo sale de `random.Random(20261001 + 1000 +
    L)` y el tipo va por turnos (contrario, cifra, endurecer, matiz); si ningún nodo lo admite, pasa al siguiente.
  - **Lectura:** dos lectores Opus con las instrucciones de la etapa, un tercero si ninguno caza la trampa, y árbitro
    Opus.
  - **La cuenta:** un defecto es un elemento (resumen, paso o entregable) con al menos una marca confirmada o
    reclasificada de ese tipo. PASA con 0 contrarios, 0 invenciones, matiz ≤ 0,2 por nodo (30 en 150) y todas las
    trampas de matiz cazadas.
  - **Código:** `parada_e1.py`, en las claves del remedio.

**Etapa 1, correcciones aplicadas (30 sep 2026):** tandas `final-e1-01` a `final-e1-32` (arbitrajes 1 a 176), más
`final-e1-fuera` (46) y `final-e1-fuera-2` (2), las correcciones FUERA reescritas solo en la forma. Los 289 lotes
se leyeron con dos lectores Opus y, donde hizo falta, un tercero.

**Muestra de parada de la etapa 1 (semilla 20261001), 30 sep 2026: NO PASA.**

| Criterio | Umbral | Resultado |
|---|---|---|
| Contrarios | 0 | **1** (un elemento) |
| Invenciones | 0 | **39** elementos en 34 nodos |
| Matiz | ≤ 0,2 por nodo (30 en 150) | **0,553** por nodo (83 elementos en 66 nodos) |
| Trampas de matiz cazadas | todas | **1 de 2**: la del lote p12 no la cazó ninguno de los tres lectores |

- **Trampas:** cazadas 14 de 15.
  - La que falló (p12) quitaba un "solo" de alcance ("solo a ciertos destinos" pasó a "a ciertos destinos"). Es el
    plantado de reserva, que se usa cuando el nodo no tiene condición ni excepción que quitar, y es la más débil de
    las trampas de matiz.
  - La regla la cuenta como fallo.
- **El árbitro:** confirmó o reclasificó 180 de las 190 marcas. 88 de los 150 nodos tienen al menos un defecto
  confirmado.
  - Los contrarios e invenciones caen en los diez espacios: core 12, risk_management 6, compras 4, y de 2 a 3 en cada
    uno de los demás.
- **Dónde estaban:** de 39 invenciones, 15 están en elementos que la etapa 1 ya había corregido y 24 en elementos que
  sus dos lectores dejaron pasar. De 83 matices, 26 y 57. El único contrario estaba en un elemento sin tocar.
  - 5 invenciones se resuelven pasando el paso a "Sugerencia de My Idea:". Varias son un "puede" del libro que el nodo
    da como seguro.
- **Lo que dice sobre el método:** una segunda lectura doble y ciega, con el mismo método, sigue encontrando
  defectos a un ritmo parecido en texto ya leído y corregido.
  - La etapa 1 no converge hacia cero con una sola pasada.
  - La muestra tampoco mide lo mismo que la medida 1: allí leía un lector por nodo sin cotejo, aquí dos lectores con
    cotejo obligatorio y un árbitro. Las cifras no se comparan directamente.
- **Aplicado:** las 116 correcciones confirmadas de la muestra, en 87 nodos, en la tanda `final-e1-parada`. Otras 2
  quedan FUERA por baranda (`proteger_fragiles_caja_dentro_de_caja`, resumen; `seguimiento_accion_correctiva`,
  paso 4), pendientes de reescritura.
- **Lo que manda la regla (9.4) y queda pendiente de decisión del fundador:** "se releen los lotes del libro o del
  espacio donde cayó lo confirmado, y se mide otra muestra con semilla 20261001 + k".
  - Lo confirmado cae en los diez espacios, así que la regla pide releer la etapa entera: unos 600 agentes más.
  - Con k = 1, la semilla sería 20261002, que ya es la semilla fijada para la muestra de la etapa 2 (9.5). Hay que
    fijar otra antes de sortear.
  - No se relanza nada hasta su decisión.
- **Fallo de método declarado en la muestra (regla de relectura, 9.4):** la trampa de matiz del lote p12 (nodo
  `clausula_antidesviacion`, resumen: se quitó el "solo" de "solo a ciertos destinos") no la cazó ninguno de los tres
  lectores. Queda como fallo de método de la lectura, igual que los 10 lotes de la etapa.

### 9.7 Decisión del fundador tras la muestra de parada (30 sep 2026): pase dirigido, no completo

**Decisión:** opción 2, con ajustes. Todo en Opus 5.5 (lectores, árbitros, verificadores y la muestra).

**1. Clases nuevas** (`docs/REGLAS_DE_LA_CASA.md`, C29 y R7):

| Clase | Qué es | Umbral en la muestra |
|---|---|---|
| Contrario | lo opuesto al libro | 0 |
| Invención dura | hecho, cifra, causa, plazo, norma o resultado prometido que el libro no dice | 0 |
| Paso práctico sin etiqueta | consejo útil sin "Sugerencia de My Idea:"; se etiqueta | 0,1 por nodo |
| Certeza endurecida | un "puede" del libro dado por seguro; cuenta como matiz | 0,2 por nodo, junto con los matices |

**2. Política de corrección** (C32 y R8): quitar lo que sobra o devolver las palabras del libro antes que redactar.
Toda frase nueva, o toda corrección que trae palabras que no estaban en el texto, la lee un verificador ciego contra el
libro antes de aplicarse. El árbitro declara el `modo` de cada corrección (`quitar`, `devolver`, `etiquetar` o
`redactar`).

**3. El pase dirigido (e1b), fijado antes de generar ningún paquete:**
- **Universo, por elementos (resumen, paso o entregable):**
  - **3a:** todo elemento que cambió alguna tanda de la etapa 1 (`final-e1-*`, con las FUERA y la de la muestra), con
    su texto vigente. Son 3.548 elementos, contando la tanda de la muestra.
  - **3b:** el barrido mecánico de marcas de certeza. Entra todo elemento, fuera de 3a, cuyo texto contenga una de
    estas marcas: "siempre", "nunca", "jamás", "debe", "deben", "va a", "van a", "vas a", "garantiza…", "sin duda",
    "necesariamente", "inevitable…", "en todos los casos", "seguro que", "te asegura…", "asegura que", "con toda
    seguridad", "sin excepción". Salen 673 elementos. El lector coteja cada marca con el grado del libro.
  - **3c:** los pasos que los lectores del pase y la muestra marcan como paso práctico sin etiqueta se etiquetan.
    Etiquetar no es redactar: solo antepone "Sugerencia de My Idea:" al texto vigente.
  - **Además:** las 2 correcciones FUERA de la muestra de parada (una ya estaba en 3a).
- **Lotes:** por libro (el primero de `fuentes_internas`), nodos en orden de `node_id`, hasta 16 nodos por lote. El
  lector ve el nodo entero y juzga solo los elementos de su lista. Orden de lectura: `random.Random(20270501)`.
- **Trampas sin marca:** una por lote, en un elemento de la lista.
  - El nodo sale de `random.Random(20270501 + 1000 + L)`.
  - El tipo va por turnos: contrario, invención dura (cifra), certeza endurecida, matiz. Es el plantado v2 de la etapa.
  - Orden del paquete: `random.Random(20270501 + 2000 + L)`.
- **Lectura:** dos lectores Opus con las instrucciones v3 (clases nuevas y política de corrección) y un tercero si
  ninguno caza la trampa. Árbitro Opus con las instrucciones v3. Verificador ciego Opus para lo que redacta o trae
  palabras nuevas.
- **Generado (`e1b.py generar`, antes de abrir ningún paquete):** 4.222 elementos (3.548 de 3a, 673 de 3b y 1 FUERA)
  en 2.523 nodos. Salen 184 lotes, de 14 nodos y 23 elementos de media. Las trampas: 63 contrarios, 48 cifras, 39
  certezas endurecidas y 34 matices.
- **Filtro de la tanda:** los mismos de la etapa, más la verificación ciega. En modo `quitar`, el piso del resumen baja
  a 200 caracteres, para que quitar lo inventado no quede bloqueado por el largo.

**4. Semillas nuevas, fijadas aquí antes de sortear nada:**
- **Muestra de cierre de la etapa 1: 20271001.** Deriva 20271001 a 20271011 (espacios), 20272002 a 20272016
  (trampas) y 20273002 a 20273016 (orden del paquete).
- **Pase dirigido: 20270501.** Deriva 20271502 a 20271701 y 20272502 a 20272701.
- **Sin choque:** las semillas ya asignadas en el repo y en las claves van de 20260807 a 20261021, y sus derivadas de
  la etapa 1 llegan como mucho a 20263219.

**5. La muestra de cierre (semilla 20271001):**
- **Diseño:** el mismo del detalle de 9.6 (150 nodos, 8 por espacio, restos mayores, 15 lotes de 10, una trampa por
  lote), leída con las instrucciones v3 y contada con las clases nuevas.
- **Regla de parada, fijada ahora:**
  - **La etapa 1 queda CERRADA si:** 0 contrarios, 0 invenciones duras, paso práctico sin etiqueta ≤ 0,1 por nodo,
    matiz (con la certeza endurecida) ≤ 0,2 por nodo y todas las trampas de matiz cazadas.
  - **Si aparece un contrario o una invención dura suelta:**
    1. Se corrige.
    2. Se relee su vecindad: el mismo campo en los nodos del mismo libro, con el método del pase.
    3. La etapa se cierra declarando el riesgo residual estimado.
  - **Sin tercer pase completo.**
  - **Si lo que se pasa es otra clase:** se trata igual; es una lectura mía de "el resto dentro de su umbral" que el
    fundador puede corregir.
- **Cómo se estima el riesgo residual:** por clase, la tasa por nodo de la muestra con su intervalo de Wilson al 95 %,
  llevada a los 3.169 nodos del universo.

**Pase dirigido, control del verificador (añadido mientras corre, antes de los paquetes afectados):**
- **Motivo:** tras los 6 primeros paquetes de verificación, el verificador ciego había sostenido 122 de 122
  correcciones. Un verificador que nunca dice que no puede ser un sello.
- **Desde el paquete v07:** cada paquete de verificación lleva una corrección falsa sin marca. Es la copia de un
  elemento real con una frase de cifra inventada al final, bajo un id con la misma forma que los reales. El
  verificador tiene que decir `no_sostiene`; la tanda nunca la aplica.
- **Clave:** `e1b_verif_trampas.json`, en las claves.
- **Primeros resultados:** v07 y v08 la rechazaron, las dos por la cifra que el libro no dice.
- **Trampas de matiz "de alcance"** (quitar un "solo"): 29 de las 34 trampas de matiz del pase son de este tipo de
  reserva. Las de los lotes 004, 011 y 024 no las cazó ningún lector, igual que la p12 de la muestra de parada:
  fallo de método en esos lotes. Queda pendiente de decisión del fundador si la muestra de cierre usa solo matices de
  condición o excepción.

**Decisión del fundador sobre las trampas de matiz (30 sep 2026):**
- **La regla nueva:** en la muestra de cierre y en lo que queda del pase dirigido, una trampa de matiz quita una
  condición o excepción real que cambia el sentido ("salvo que…", "solo si…", "siempre que…"), nunca un "solo" de
  refuerzo.
- **La validación:** antes de plantarla, un agente aparte (validador Opus, `INSTRUCCIONES_E1B_VALIDADOR_TRAMPAS.md`)
  confirma contra el libro que quitarla es un defecto real según la rúbrica.
- **Aplicado en el pase dirigido (`regen_matiz.py`):** los 23 lotes sin leer con trampa de matiz se replantaron con la
  semilla 20270501 + 4000 + L.
  - En 6 lotes había una condición o excepción real y el validador confirmó el defecto en las 7 candidatas.
  - En los otros 17 no había ninguna, y la trampa pasó al siguiente tipo por turnos (contrario).
  - Las trampas anteriores quedan en `e1b_trampas_antes_regen.json`, en las claves.
- **Revisión de las trampas "solo" que ningún lector cazó:**

  | Lote | ¿Quitar el "solo" cambiaba el sentido? | Registro |
  |---|---|---|
  | 004 | no | **trampa inválida** |
  | 011 | no | **trampa inválida** |
  | 024 | no | **trampa inválida** |
  | 052 | sí ("no solo al arranque" pasaba a "no al arranque") | **fallo de método** |
  | 056 | no | **trampa inválida** |
  | p12 (muestra de parada) | no | **trampa inválida** |

- **Cómo se leen los dos datos:** cinco de las seis trampas "solo" eran inválidas y no cuentan como fallo de los
  lectores. La del lote 052 cambiaba el sentido y sigue como fallo de método.
- **En la muestra de parada:** con p12 inválida, sus trampas de matiz válidas son 1 de 1 cazadas. El veredicto NO PASA
  no cambia; lo sostienen el contrario, las invenciones y el matiz por nodo.

**Pase dirigido, trampas no cazadas por los dos lectores (registro mientras corre):**
- **Lote 057 (contrario):** los dos lectores no la cazaron y la cazó el tercero. No es fallo de método.
- **Lote 076 (contrario, nodo `clasificar_tipo_paquete`):** la trampa cambiaba el orden temporal de una prueba ("antes
  de que salga de tus manos" pasaba a "después de"). Es una trampa válida del plan original, y ninguno de los tres
  lectores la cazó. Queda como **fallo de método** en ese lote. Es el mismo punto ciego del orden temporal que ya se
  había visto en la etapa 1, y la instrucción v3 no lo cerró.
- **Lote 129 (contrario, nodo `diseno_consecuencias_no_intencionadas`):** otra vez el orden temporal. La corrección,
  reversión o mitigación pasaba de hacerse "antes de escalar una solución" a hacerse "después de". Ninguno de los tres
  lectores la cazó. Queda como **fallo de método** en ese lote.
- **Lectura de los dos casos:** las dos trampas de contrario que nadie cazó en el pase cambian "antes de" por "después
  de". Las demás trampas de contrario sí se cazaron. El punto ciego es concreto: la inversión de orden temporal
  dentro de una frase que por lo demás sigue siendo verdad. La muestra de cierre lo mide con trampas del mismo
  diseño, sin retocarlas.
- **Lote 176 (matiz validado, nodo `comprender_definicion_legal_franquicia`):** la trampa quitaba una condición de
  jurisdicción: que la obligación rige solo si vendes o piensas vender franquicias en Estados Unidos. El validador la
  había confirmado como defecto real. Ninguno de los tres lectores la cazó. Queda como **fallo de método** en ese lote.

**Pase dirigido, lectura terminada (184 lotes, 377 lecturas):**

| Tipo de trampa | Lotes | Cazadas | Sin cazar |
|---|---|---|---|
| Invención con cifra | 48 | 48 | 0 |
| Certeza endurecida | 39 | 39 | 0 |
| Contrario | 80 | 78 (una solo por el tercer lector, lote 057) | 2 (lotes 076 y 129, fallo de método) |
| Matiz de condición validado | 6 | 5 | 1 (lote 176, fallo de método) |
| Matiz "solo" anterior a la decisión | 11 | 6 | 5 (004, 011, 024 y 056 inválidas; 052 fallo de método) |

- **Fallos de método del pase:** cuatro lotes, 052, 076, 129 y 176. Dos son la inversión "antes de / después de". Los
  otros dos son la caída de una condición que acota a quién o cuándo aplica el consejo.
- **Control del verificador ciego:** rechazó las 32 correcciones falsas de los paquetes v07 a v38.
- **Correcciones aplicadas:** tandas `final-e1b-01` a `final-e1b-24`, con 747 correcciones en 679 nodos, todas por la
  tubería de siempre (GATE 0, etiquetas, preparación de planes y copia web) y con las dos suites en verde.
- **FUERA del pase (7):** son correcciones que no entraron.
  - Cuatro dejaban una baranda de la casa (voz de libro o residuo corporativo).
  - Una metía contenido de país en un nodo sin clase de jurisdicción.
  - Una no la sostuvo el verificador.
  - Una traía una cita incompleta.

  Sus elementos siguen con el texto vigente, que el pase no pudo corregir de forma segura. La muestra de cierre los
  mide como a cualquier otro nodo. Están listados en `e1b_aplicados.json`, en las claves, para el método FUERA si la
  muestra lo pide.

**Muestra de cierre de la etapa 1 (semilla 20271001), 30 sep 2026: NO CIERRA; aplica la regla de parada.**

- **Diseño:** el mismo de la muestra de parada. Son 150 nodos en 15 lotes, con 8 por espacio y el resto por
  tamaño. Hay una trampa por lote:
  - Las de matiz quitan una condición real, que confirmó antes un validador aparte (3 de 3 confirmadas).
  - El lote 4 no tenía condición que quitar y pasó al siguiente tipo.
  - Quedaron 5 de cifra, 4 contrarios, 4 de certeza endurecida y 2 de matiz.
  - Código: `cierre_e1.py`, en las claves.
- **Lectura:** dos lectores Opus por lote, con las instrucciones v3. **Las 15 trampas las cazaron los dos lectores de
  cada lote (30 de 30)**, así que no hizo falta ningún tercero.
- **Árbitro (v3):** confirmó 194 marcas y rechazó 11, en 133 elementos. 83 de los 150 nodos tienen al menos un
  defecto confirmado.

| Clase (R7) | Defectos (elemento) | Nodos | Por nodo | Umbral | Resultado |
|---|---|---|---|---|---|
| Contrario | 2 | 2 | | 0 | **sobre umbral** |
| Invención dura | 13 | 12 | | 0 | **sobre umbral** |
| Paso sin etiqueta | 40 | 29 | 0,267 | 0,1 | **sobre umbral** |
| Matiz (con certeza endurecida) | 71 | 53 | 0,473 | 0,2 | **sobre umbral** |

- **Los dos contrarios son de orden temporal:** una carta de crédito que se revisa "antes" de lo que dice el libro, y
  una clasificación de paquete puesta antes de empacar. Es el mismo punto ciego de los fallos de método del pase.
- **Comparación con la muestra de parada, con cautela porque las clases cambiaron:**
  - Invenciones: pasan de 39 elementos en 34 nodos a 13 invenciones duras en 12 nodos, más 40 pasos sin etiqueta,
    que antes contaban dentro de las invenciones.
  - Matiz por nodo: baja de 0,553 a 0,473.
  - Nodos con algún defecto: bajan de 88 a 83.
- **Riesgo residual estimado (Wilson 95 %, sobre los 3.169 nodos vivos fuera del mundo 11):**

  | Clase | Tasa | IC 95 % | Nodos estimados |
  |---|---|---|---|
  | Contrario | 1,3 % | 0,4 a 4,7 % | 12 a 150 |
  | Invención dura | 8,0 % | 4,6 a 13,5 % | 147 a 427 |
  | Paso sin etiqueta | 19,3 % | 13,8 a 26,4 % | 438 a 836 |
  | Matiz | 35,3 % | 28,1 a 43,3 % | 892 a 1.371 |

- **Lo que manda la regla (9.7):** se corrigen los defectos de la muestra, se relee la vecindad de cada contrario e
  invención dura, y la etapa se cierra declarando el riesgo residual, sin un tercer pase completo.
  - La vecindad es el mismo libro y el mismo campo: 423 pares nodo-campo en 8 libros.
  - Antes de cerrar va el barrido de puntos ciegos que decidió el fundador el 30 sep, tras el informe: construcciones
    "antes de / después de" y condiciones que acotan a quién o cuándo aplica el consejo.

### 9.8 Decisión del fundador sobre la procedencia (30 sep 2026)

**Reglas duras**, las primeras de `docs/REGLAS_DE_LA_CASA.md`:
- **D1:** jamás un usuario debe saber, ni poder intuir, de dónde provienen las respuestas de la app. Todo origen es
  control interno.
- **D2:** ninguna copia fiel. Ningún texto de nodo es copia ni traducción palabra por palabra de un pasaje de un libro.
- **D3:** ningún nodo vivo y funcional se retira.

**Aplicado, cada paso con su prueba en rojo primero y las dos suites en verde:**
- **Guarda única de procedencia** (`web/lib/procedencia.test.ts`, c8eed6b8).
  - Junta las cuatro guardas que había.
  - Exige, en los once idiomas, que ningún texto de cara al cliente lleve un título, una clave interna, un aviso con
    año, el prefijo de procedencia o una atribución genérica.
  - `REGLA_SIN_FUENTES` se amplía a estudios, investigaciones, expertos, etiquetas de procedencia y a no insinuar el
    origen.
- **Aviso de vigencia sin año** en los once idiomas: "Verifica la norma vigente en tu país: estas reglas cambian con el
  tiempo". La copia web de `vigencia.json` ya no lleva el año (e0cc913b).
- **El prefijo "Sugerencia de My Idea:" sale de 280 pasos en 231 nodos** (tanda `procedencia-prefijo`, 7bb43edb).
  Uno de ellos lo llevaba a media frase.
  - No hay campo nuevo ni cambio de esquema: la constancia de que es un paso de la casa queda en el registro de
    correcciones.
  - El aplicador gana el veredicto CASA, una constancia sin tocar el texto, para los barridos futuros.
  - El aplicador rechaza cualquier prefijo de procedencia visible.
  - Se ajustan C14, C29, C32 y R6 a R8, y las instrucciones de lectores, árbitros y verificadores: la clase pasa a
    "paso sin marca" y el modo, a "marcar".
- **Atribuciones genéricas:** salen las 19 reales de 16 nodos, incluido el caso con nombres de fuente entre paréntesis
  (tanda `procedencia-atribuciones`, 186e4c5a).
  - Del conteo de 26, siete eran instrucciones al usuario o negaciones y se quedan: "busca en la literatura", "según
    los datos obtenidos", "no se ha probado".
- **Política de corrección aclarada (C32, R8 e instrucciones):** devolver es devolver el sentido y el término preciso
  del libro, nunca copiar ni traducir un pasaje palabra por palabra.
- **Licencias (punto 8):** cada fuente lleva su licencia en la lista canónica, y el inventario interno la muestra en
  una columna. Ninguna fuente se retira.
  - Las nueve guías del gobierno de EE. UU. y el manual de pymes de OSHA son de dominio público.
  - La guía de IDEO.org figura como CC BY-NC-ND 3.0, según el fundador. Tiene 20 nodos vivos.
  - Los libros comerciales y las guías de empresas tienen copyright sin licencia abierta.

**Comprobación de copias (punto 7): sin pase aparte, por ajuste del fundador (30 sep 2026).**
- La copia fiel se mide como un criterio más de la medida 2 (U14, umbral 0), que ya lee una muestra con el libro
  delante. El lector de la medida 2 la marca con la definición de D2, y el árbitro la confirma y la reescribe en
  palabras de la casa sin cambiar el sentido.
- Se había sorteado un pase aparte (semilla 20271101: 540 elementos en 22 lotes, con trampas preparadas). Se detuvo
  tras el ajuste, con 2 lotes leídos. **No se cuenta ni se usa:** la vara de copias es la de la medida 2.
- La política de corrección aclarada (punto 6: devolver es devolver el sentido, nunca copiar) ya está aplicada.

**Prioridades del fundador hasta el jueves 8 de octubre** (la cuota se renueva el martes 6 a las 23:00):
1. **Procedencia (puntos 1 a 6):** hecho.
2. **Cerrar la etapa 1:**
   - corrección de la muestra de cierre;
   - vecindad de los 15 defectos duros;
   - barridos de puntos ciegos, de cifras y plazos, y de pasos sin marca;
   - cierre declarando el riesgo residual.
3. **Medida 2**, que certifica, con el criterio de copias incluido.
4. **Etapa 2** si cabe. Ortografía y calcos, solo en lo que ve el cliente; si no caben, pasan a mejora continua con
   su ficha.
5. **Antes de agotar la cuota del jueves:** `docs/PROXIMOS_PASOS.md` con lo que quede: la corrida final con el saldo
   de la API, el re-embebido con Voyage y la copia de las reglas a la forja.

**Después:** se retoman la corrección de la muestra de cierre y los barridos.

### 9.9 Cierre de la etapa 1: pase dirigido de los barridos (diseño fijado antes de generar, 30 sep 2026)

- **Qué entra:** los elementos de los campos de la etapa 1 (resumen, pasos y entregable) de los nodos vivos que caen
  en alguno de los tres barridos que pidió el fundador, más la vecindad de los 15 defectos duros de la muestra de
  cierre.
  - **Puntos ciegos, orden temporal:** "antes de", "antes que", "después de", "después que", "una vez que", "tras".
  - **Puntos ciegos, condiciones que acotan a quién o cuándo:** "cuando", "si tienes", "si tu", "si vas", "si eres",
    "si ya", "si no", "solo en", "solo si", "salvo que", "salvo si", "excepto si", "excepto cuando", "a menos que",
    "siempre que", "en caso de que", "únicamente si", "únicamente cuando".
  - **Cifras y plazos:** un número con %, días, semanas, meses, años, horas, minutos o veces, en cifra o en letra.
  - **Vecindad:** 423 pares nodo-campo en 8 libros, el mismo libro y el mismo campo de cada contrario e invención
    dura.
  - Quedan fuera los 150 nodos de la muestra de cierre, recién leídos y corregidos.
  - Tamaño medido: 4.109 elementos en 2.108 nodos, más la vecindad.
- **Lectura:**
  - Un lector Opus por lote lee contra el libro, con las instrucciones v3 y las reglas duras D1 y D2.
  - Cada lote lleva una trampa sin marca: contrario de orden temporal, cifra inventada o certeza endurecida. Semilla
    20271201.
  - Si el lector no caza la trampa, un segundo lector relee el lote entero.
  - Un árbitro Opus confirma, corrige y declara el modo.
  - Un verificador ciego lee toda corrección que trae palabras nuevas. Cada paquete lleva una corrección falsa de
    control.
- **Pasos sin marca:** el lector los marca en los elementos que lee. Se registran como constancia CASA, sin prefijo
  visible (D1).
  - No hay un barrido de todos los pasos del catálogo, porque no hay filtro mecánico posible.
  - El resto se declara como riesgo residual y lo mide la medida 2.
- **Cierre de la etapa 1:** con las tandas aplicadas, la etapa se cierra declarando el riesgo residual (Wilson 95 %)
  de la muestra de cierre, sin un tercer pase completo (regla de parada, 9.7).
- **Cuota:** el pase se avanza en oleadas hasta el aviso del 90 %, se para en un punto limpio y se termina tras la
  renovación del martes 6 de octubre a las 23:00.
- **Código:** `barrido.py`, en las claves del remedio.
- **Plan generado:** 3.873 elementos en 1.803 nodos, en 176 lotes, con la vecindad expandida a 969 elementos.
  - Trampas: 70 de cifra, 64 contrarios y 42 de certeza endurecida.
  - En un lote sin elemento listado que admitiera trampa, la trampa va a otro elemento del mismo nodo, y ese elemento
    se añade a lo que se juzga.

**Corrección de la muestra de cierre (tanda `final-e1-cierre`, 30 sep 2026):** 117 correcciones en 77 nodos.
- 40 son constancias CASA de pasos de la casa, sin tocar el texto (D1).
- Las demás están en modo `devolver` o `quitar`, y el verificador ciego leyó todas las que traían palabras nuevas. Los
  tres paquetes rechazaron su corrección falsa de control.
- El verificador rechazó tres correcciones por ser traducción casi palabra por palabra del libro (D2).
- **Quedan 6 FUERA**, pendientes de reescritura en palabras de la casa:
  - dos defectos duros: `separa_la_visita_de_evaluacion_de_la_decision_de_compra` (resumen) y
    `clausula_antidesviacion` (paso 3);
  - `diseno_estructura_recompensas_roles`, `reevolucion_industrial`, `desarrollo_expertos_capaces` y
    `sesgo_retrospectivo_hindsight_2`.


### 9.10 Etapa 1 CERRADA con riesgo residual declarado (30 sep 2026)

**Barridos de cierre (9.9) terminados:** 176 lotes y 3.873 elementos leídos contra su libro en 1.803 nodos, en 14
oleadas cerradas de como mucho 20 agentes, todo en Opus. Tandas `final-e1-barrido-01` a `-12`.

**Lo que encontraron y se corrigió.** El árbitro confirmó defecto en 360 elementos (9,3 % de lo leído). Por clase,
contando la más grave de cada elemento:

| Clase | Elementos | Umbral R7 |
|---|---|---|
| Contrario | 8 | 0 |
| Invención dura | 28 | 0 |
| Paso sin marca | 101 | 0,1 por nodo |
| Certeza endurecida | 34 | 0,2 por nodo (con matiz) |
| Matiz | 189 | 0,2 por nodo (con certeza) |

- **Aplicado:** 343 correcciones en 301 nodos:
  - 8 por contrario;
  - 236 añadidos quitados o devueltos al sentido del libro;
  - 99 constancias CASA de pasos de la casa, sin tocar el texto (D1).
- **Verificador ciego:** leyó toda corrección con palabras nuevas, en 14 paquetes. Los 14 rechazaron su corrección
  falsa de control. Rechazó además correcciones reales que:
  - traducían casi palabra por palabra el libro (D2);
  - ponían una condición que el libro no pone;
  - añadían algo que el libro no dice.
- **Arreglo del método:** el constructor de tandas descartaba los pasos en modo `marcar` por "igual al vigente", así
  que se habrían perdido sus constancias. Se arregló desde la primera tanda y las 99 constancias entraron.

**Reescritura final de lo que quedó FUERA (tanda `final-e1-fuera-final`).** Entran 25 elementos:
- 5 del pase dirigido;
- 6 de la muestra de cierre, entre ellos los dos defectos duros `separa_la_visita_de_evaluacion_de_la_decision_de_compra`
  y `clausula_antidesviacion`;
- 14 de los barridos.

El hallazgo ya estaba arbitrado. El reescritor rehízo la forma, porque los textos tropezaban con la baranda, la cita,
la jurisdicción, la copia literal (D2), el prefijo (D1) o una adición que el verificador no sostuvo. El verificador
ciego sostuvo los 25 y rechazó su control. **Ya no queda ninguna corrección arbitrada sin aplicar en la etapa 1.**

**Sensibilidad de la lectura, medida con las trampas:**

| | Cazadas | Wilson 95 % |
|---|---|---|
| Primer lector | 168 de 176 | 91,3 % a 97,7 % |
| Primer o segundo lector | 171 de 175 válidas | 94,3 % a 99,1 % |

- La trampa del lote 103 no cuenta: cambiaba "para siempre" por "para nunca" y dejaba una frase agramatical.
- **Las 4 trampas que no cazó ningún lector tienen la misma forma:** un "antes de" cambiado por "después de".
  - En los lotes 106, 133 y 153 es la misma frase: "verifica la regulación vigente en tu jurisdicción antes de
    actuar". Los lectores la leen como aviso fijo y no la cotejan.
  - En el lote 057 es "después de eso" en un resumen.
- **Cierre mecánico de ese punto ciego:** la frase aparece en 42 nodos vivos y en ninguno está invertida. Las cinco
  apariciones de "después de actuar" del catálogo son legítimas (`vuelve_a_medir_despues_del_susto`).

**Riesgo residual declarado (regla de parada, 9.7).** Si la lectura deja pasar defectos al ritmo que deja pasar
trampas, lo que queda en los 3.873 elementos barridos es:

| Clase | Encontrados | Residual esperado | Cota 95 % |
|---|---|---|---|
| Contrarios e invenciones duras | 36 | 0,8 | 2,2 |
| Pasos sin marca | 101 | 2,4 | 6,1 |
| Matiz y certeza | 223 | 5,2 | 13,6 |

- **Fuera del universo barrido:** los elementos sin construcción temporal, condición ni cifra, y sin vecindad con un
  defecto duro, solo los cubren el pase dirigido (9.7) y la muestra de cierre. Antes de sus correcciones, la muestra
  midió 15 defectos duros en 150 nodos (Wilson 95 %: 6,2 % a 15,8 % por nodo).
- Ese universo lo mide la **medida 2** (semilla 20261010), con el criterio de copias fieles (U14) incluido. **La
  etapa 1 no se declara certificada: la certificación es la medida 2.**

**Fallos de método anotados:** las trampas de los lotes 057, 106, 133 y 153 (patrón antes/después, cubierto arriba).
Trampa inválida: la del lote 103.

## 10. Medida 2: diseño fijado antes de sortear (30 sep 2026)

La medida 2 certifica. Repite el diseño de la sección 3, con los cambios de abajo, y se cuenta contra los umbrales de
la sección 1 (U1 a U14).

- **Semilla:** 20261010, escrita aquí antes de sortear.
- **Universo y reparto:** los mismos 3.634 nodos vivos y la misma tabla de la sección 3 (200 nodos). El sorteo usa
  `random.Random(20261010 + índice del espacio)`. Un nodo puede salir en las dos medidas: son sorteos independientes.
- **Lotes y trampas:**
  - 22 lotes de 9 o 10 nodos, con 1 trampa sin marca por lote.
  - Son 22 trampas, 2 de cada uno de los 11 tipos: los 10 de la sección 3 y la **copia fiel**.
  - Cada trampa va bajo un id real del espacio del lote que no está en la muestra. El defecto se planta en la copia
    del lector, nunca en el dataset.
  - La trampa de copia sustituye un elemento por la traducción literal de un tramo de 30 a 50 palabras del libro del
    nodo. La prepara un agente que no lee ningún lote.
  - Las claves viven fuera de toda carpeta que lean los lectores.
- **Lectores ciegos:** como en la sección 3, con cuatro precisiones:
  1. **Copia fiel (U14, regla dura D2):** un elemento que reproduce un pasaje del libro casi palabra por palabra y en
     su mismo orden, traducido o no. Basta una frase larga, de más de unas 20 palabras, o dos o más frases seguidas.
     No lo es un término preciso, el nombre de un método o una definición breve.
  2. **Pasos de la casa (C29, D1):** el lote trae `pasos_casa`, los índices de los pasos con constancia CASA. Un paso
     práctico que el libro no da y que no afirma nada como hecho no es invención. Sí lo es si afirma una cifra, una
     causa o un resultado que el libro no dice.
  3. **Procedencia (D1):** el lector marca como defecto cualquier texto que nombre un libro, un autor, "los estudios" o
     "los expertos" como respaldo, o que lleve una marca de procedencia.
  4. **Alcance de ortografía y calcos (decisión del fundador, 30 sep 2026, escrita antes de medir):**
     - El lector los marca en cualquier campo.
     - **Cuentan para U7 y U9 solo en los campos que el cliente ve crudos:** `etiqueta_arbol`, `pasos_accionables`,
       `entregable_esperado` y la pregunta del nodo, que el lote trae en `pregunta`.
     - En `resumen_teorico`, `condiciones_activacion` y `titulo_concepto`, que solo lee la IA, se anotan para la mejora
       continua (ficha de nivel 2) y no cuentan.
     - Motivo: esos campos son los que llegan tal cual al plan sin IA y a la pantalla. Lo demás lo reformula la IA
       antes de mostrarlo.
- **Árbitro:** como en la sección 3. Cuando confirma una copia fiel, la reescribe en palabras de la casa, con el mismo
  sentido y el término preciso.
- **Segunda lectura:** la misma regla de la sección 3. Si el lector no caza la trampa, un segundo lector relee el lote
  entero y cuenta la unión. Una trampa que tampoco caza el segundo lector es un fallo de método del criterio.
- **Veredicto:** el de la sección 5. Con todos los criterios en PASA, esta acta abre con "DATASET CERTIFICADO" y la
  fecha. Lo que no pase se corrige por la doctrina y se vuelve a medir solo ese punto, con semilla nueva escrita antes.
- **Guardas y navegación (U11 a U13):** se repiten al 100 % del catálogo el mismo día de la medida.

### 10.1 Resultado de la medida 2 (1 oct 2026): NO CERTIFICADO

**Método:** 22 lotes, 200 nodos de la muestra y 22 trampas. El arbitraje dio 403 defectos confirmados, 1
reclasificado y 37 rechazados. Las cifras están en `docs/auditoria_final/medida_2.json`.

**Trampas:**
- El primer lector cazó 21 de 22, incluidas las 2 de copia fiel.
- La trampa de fase del lote 10 (`escalonar_complejidad_puesto_empleado_nuevo`, de planificación a ejecución) no la
  cazó ninguno de los dos lectores: es un fallo de método del criterio de fase.

**Guardas y navegación, repetidas hoy al 100 % del catálogo:** en verde.
- Navegación: murallas, puentes, ley del ancla, puertas, alcanzabilidad del 100 % en el núcleo y en cada mundo, y 0
  aristas a deprecados.
- Los dos nodos que la medida 1 dejó sin alcanzar ya se alcanzan.
- U11, U12 y U13 pasan.

| # | Criterio | Medida 1 | Medida 2 | Intervalo 95 % | Umbral | Veredicto |
|---|---|---|---|---|---|---|
| U1 | Contrarios | 4 | 1 | | 0 | **NO PASA** |
| U2 | Invenciones | 25 | 4 | | 0 | **NO PASA** |
| U3 | Fase | 5,0 % | 2,5 % | 1,1 a 5,7 % | ≤ 3 % | **PASA** |
| U4 | Dominio | 1,5 % | 1,0 % | 0,3 a 3,6 % | ≤ 2 % | **PASA** |
| U5 | Condiciones | 3,0 % | 6,0 % | 3,5 a 10,2 % | ≤ 2 % | **NO PASA** |
| U6 | Etiquetas | 6,0 % | 8,0 % | 5,0 a 12,6 % | ≤ 2 % | **NO PASA** |
| U7 | Ortografía, solo campos crudos | 19,5 % (todo) | 6,0 % | 3,5 a 10,2 % | ≤ 1 % | **NO PASA** |
| U8 | Matices | 0,50 por nodo | 0,075 por nodo | 0,042 a 0,124 | ≤ 0,2 | **PASA** |
| U9 | Calcos, solo campos crudos | 0,72 por nodo (todo) | 0,44 por nodo | 0,35 a 0,54 | ≤ 0,2 | **NO PASA** |
| U10 | Regionalismos | 0,025 | 0,04 | 0,017 a 0,079 | ≤ 0,2 | **PASA** |
| U14 | Copias fieles (D2) | no medido | 148 elementos en 53 nodos | 20,8 a 33,1 % de los nodos | 0 | **NO PASA** |
| D1 | Procedencia | no medido | 4 | | 0 | **NO PASA** |

- **Mejora continua:** fuera de los campos crudos se anotaron 58 calcos y 31 faltas de ortografía. No cuentan (sección
  10) y van a la ficha de nivel 2.
- **Lo que mejoró el remedio:**
  - Contrarios e invenciones bajan de 29 a 5.
  - Matiz baja de 0,50 a 0,075 por nodo y pasa.
  - Fase baja a 2,5 % y pasa.
- **Lo que no pasa:**
  - Contrarios e invenciones, con umbral 0.
  - Condiciones y etiquetas.
  - Ortografía y calcos en los campos crudos.
  - Procedencia.
  - Y la **copia fiel**, el hallazgo de más peso:
    - El 26,5 % de los nodos de la muestra trae al menos un elemento que traduce un pasaje del libro casi palabra por
      palabra. Son 117 pasos, 29 resúmenes y 2 condiciones.
    - Proyectado al catálogo, son entre unos 750 y 1.200 nodos.
    - Es sistémico: los nodos se escribieron traduciendo, y la regla D2 es posterior a su extracción.
- **Veredicto:** el catálogo **no se certifica**. Corregir la copia fiel a escala es una decisión del fundador (alcance,
  método y coste), igual que el resto de los criterios que no pasan.

## 11. Prioridad única del fundador: contrarios, invenciones y procedencia (1 oct 2026)

**Decisión del fundador tras la medida 2:**
- Se cierran solo los contrarios, las invenciones duras y la procedencia.
- No se relee el catálogo desde cero ni se vuelve sobre lo ya leído y corregido: se continúa desde aquí.
- La copia fiel, las etiquetas, la ortografía y los calcos esperan.

**Principio:** todo lo que presenta la app es consejo de My Idea (regla dura D4).
- Se elimina la clase "paso sin marca" de las reglas (R7, C29 y R8), de las instrucciones de lectura y de esta acta, y
  su barrido no se hace.
- La regla de procedencia de los métodos queda como D5 en `docs/REGLAS_DE_LA_CASA.md`.

### 11.1 Lo que ya estaba hecho de procedencia (comprobado el 1 oct 2026)

- **Prefijo "Sugerencia de My Idea":**
  - quitado de 280 pasos en 231 nodos (tanda `procedencia-prefijo`);
  - 0 campos visibles lo llevan;
  - la copia web del grafo no lo lleva;
  - solo queda en el registro interno de correcciones (`texto_anterior`), que es control interno.
- **Atribuciones genéricas:** de los 26 casos que dio la búsqueda, 19 eran atribuciones y se corrigieron en 16 nodos
  (tanda `procedencia-atribuciones`). Los otros 7 eran falsos positivos: instrucciones al usuario.
- **Aviso de vigencia:** sin año en los 11 idiomas ("Verifica la norma vigente en tu país: estas reglas cambian con el
  tiempo"). La copia web de vigencia no lleva el año.
- **Guarda única de procedencia** (`web/lib/procedencia.test.ts`): en verde.

### 11.2 Lo que se hizo hoy

- **Métodos con persona y atribuciones a personas.** La guarda nueva (sección 7, prueba en rojo primero) encontró 47
  campos visibles con una persona como fuente o con un método con persona que tiene nombre neutro.
  - Ejemplos: "Como decía Drucker", "Jane Jacobs demostró", "ciclo de Shewhart", "triángulo de Heinrich", "trilogía
    de Juran".
  - Se corrigieron con 3 procedencias de la medida 2 en la tanda `procedencia-metodos`: 50 correcciones ATRIBUCION en
    44 nodos.
  - La etiqueta `no_usar_triangulo_heinrich` pasó a "Deja la pirámide de accidentes" y se retradujo a los 10 idiomas
    con su huella.
  - `REGLA_SIN_FUENTES` dice ahora que el método se nombra, nunca se atribuye, y con su nombre neutro.
- **Medida 2, defectos duros:**
  - 3 invenciones en campos visibles: corregidas, quitando o devolviendo, con verificador ciego.
  - 4 procedencias: corregidas en `procedencia-metodos`.
  - Quedan 2 casos para el visto del fundador, porque tocarlos choca con una regla vigente:
    - El **contrario está en la pregunta base** de `outsourcing_ventas_fso`. La pregunta atribuye al equipo externo
      la generación de candidatos, y el libro dice lo contrario. Las bases de la caché no se tocan.
    - Una **invención está en el `titulo_concepto`** de `tratar_packaging_costo_marca` ("variable de costo y de
      marca"). El título es material interno y no se modifica por doctrina.
- **Barridos dirigidos.** Ya hechos: "antes de / después de" y condiciones, y cifras y plazos (barridos de cierre,
  9.9 y 9.10). Faltaba el de marcas de certeza ("siempre", "nunca", "garantiza", "sin duda"…).
  - Se hace solo sobre resúmenes, pasos y entregables que ninguna pasada leyó: 40 elementos.
  - Va con la vecindad, mismo libro y mismo campo, de las 3 invenciones: 288 elementos.
  - En total, 30 lotes con trampa sin marca (`barrido2.py`, semilla 20271501).
  - En las condiciones de activación, una marca de certeza ("si nunca has…") describe cuándo aplica el nodo y no
    afirma nada contra el libro: no entran.
  - **Resultado del barrido de certeza y vecindad:**
    - Trampas: el primer lector cazó 29 de 30. En el lote 027 la trampa, una certeza endurecida, se le escapó también
      al segundo lector. Queda anotado como fallo de detección de ese lote.
    - Arbitraje: 9 paquetes. Tanda `final-e1-barrido2-01`: 26 correcciones en 26 nodos (25 ANADIDO, sobre todo
      certezas endurecidas devueltas al matiz del libro, y 1 CONTRARIO), en 19 resúmenes, 6 pasos y 1 entregable.
    - Verificación ciega: 3 paquetes, 3 de 3 trampas cazadas, 24 de 24 correcciones sostenidas. Las 2 restantes son
      quitas puras, sin palabra nueva, y por diseño no se verifican.

### 11.3 Medida final: diseño fijado antes de sortear

- **Semilla:** 20261101, escrita aquí antes de sortear. La misma tabla de reparto de la sección 3: 200 nodos vivos.
- **Qué mide:** solo contrarios (U1), invenciones duras (U2) y procedencia (D1, D5).
- **Lotes y trampas:** 20 lotes de 10 nodos, con 1 trampa sin marca por lote.
  - Son 7 contrarios, 7 invenciones duras y 6 procedencias.
  - Una trampa de procedencia es una atribución a una persona, a un libro, a "los estudios" o a "los expertos", o un
    método con persona que tiene nombre neutro.
- **Lectura:**
  - Lector ciego por lote, contra el libro.
  - Segundo lector si no caza la trampa.
  - Árbitro de cada defecto marcado en un nodo de la muestra.
- **Lo que aparezca** se corrige y se relee su vecindad (mismo libro y mismo campo, sin volver sobre lo ya leído). No
  hay otra pasada.
- **Veredicto en esta acta:**
  - "SANEADO en contrarios, invenciones y procedencia" si da 0;
  - si no da 0, el residuo estimado por nodo con su intervalo de Wilson al 95 %.

## 12. Ninguna referencia de origen llega a la IA (añadido del fundador, 1 oct 2026)

Encargo: que ningún título de libro ni autor de la lista canónica llegue nunca a la IA, para que nunca pueda aparecer
en lo que escribe. No basta con la orden `REGLA_SIN_FUENTES`. Se hizo antes de la medida final. La regla queda como D6
en `docs/REGLAS_DE_LA_CASA.md`.

### 12.1 A. Campos internos, llamada por llamada

Inventario del código de producción (`web/`): 21 llamadas a la IA.

| Llamada | Lo que lleva del grafo |
|---|---|
| Claridad / organizador (2 rutas) | id, fase, `titulo_concepto` y resumen recortado de las semillas de entrada |
| Clasificación de la entrada | id, fase, `titulo_concepto` y resumen recortado de las semillas |
| Intérprete de la entrevista (turno, variante sin historial, reintento) | id, `titulo_concepto`, 2 condiciones y pregunta en caché del nodo actual y sus sucesores; saltos con id, título, fase y condiciones |
| Adaptador de preguntas | la pregunta base de la caché y las etiquetas de los candidatos |
| Pregunta dirigida, decisión de plan | la pregunta en caché, o solo la respuesta de la persona |
| Puerta del seguimiento | candidatos: id, título, fase, resumen recortado y 2 condiciones |
| Replanteamiento | candidatos: id, título, fase y resumen recortado; el plan anterior |
| Plan | id, `titulo_concepto`, etiqueta, pasos y entregable de la ruta |
| Estado vivo, juez de la sesión | títulos de los nodos recorridos |
| Diagnóstico del mundo | etiquetas de los nodos recorridos |
| Estimación, enlazador y reformulador de protección, consulta al español, oferta y narración del reporte | nada del grafo |

- **Ninguna llamada envía `fuente`, `fuentes_internas`, `correcciones`, `merged_originals`, `notas_extraccion` ni
  campos con citas, líneas o rutas de libro.** Todas leen el nodo de la vista web (`cargarGrafo`) y eligen sus
  campos uno a uno. La vista web ya no lleva esas claves (`scripts/sync_assets_web.py`), y ningún código de `web/` lee
  `dataset/`. Las preguntas en caché tampoco las llevan.
- No había nada que quitar en las llamadas.
- Fuera de producción: el motor Python (herramienta local de línea de órdenes) lee el grafo completo, con los campos
  internos, pero también elige sus campos uno a uno y no envía ninguno interno. No lleva `REGLA_SIN_FUENTES`. Los
  scripts de extracción de libros envían texto de libro por diseño: son la forja, no la app.

### 12.2 B. El filtro único

- `scripts/origen_ia.py`: la función única por la que pasa **todo** texto de nodo (título, etiqueta, resumen, pasos,
  entregable y condiciones) y toda pregunta en caché antes de llegar a la vista web.
  - Quita los títulos de la lista canónica con sus comillas.
  - Quita los autores: entre paréntesis ("(Juran)", "(Shewhart-Deming)"), al final de un paréntesis ("…, Crosby)"),
    tras "de" ("Paso 6 de Crosby"), o como adjetivo ("Modelo Juran de…").
  - No toca el resto del texto ni los nombres de método. Un autor se busca con mayúscula y como palabra entera, así
    que "reason to buy" y "brown-bag" quedan intactos. "MINI Cooper" es una excepción declarada.
  - Cada quita queda en `dataset/metadata/quitas_origen_ia.json`, un registro interno que no viaja a la web.
- **Por qué va al sincronizar y no en cada llamada.** Las 21 llamadas leen el texto de nodo de esa misma vista, así que
  el filtro vale para todas por construcción, y para las que vengan. Filtrar en cada llamada obligaría a copiar la
  lista canónica de libros y autores a `web/`, y la decisión del 27 sep lo prohíbe.
  - El dataset no cambia: el `titulo_concepto` sigue intacto por doctrina.
  - El validador (`run_phase1.py`) compara ya la copia web con la copia filtrada del dataset.
- **La orden fija de toda llamada** (`REGLA_SIN_FUENTES`) nombraba a Blank, Osterwalder y Deming como ejemplos de lo
  prohibido. Ahora sus ejemplos no nombran a nadie ("según el autor", "como decía tal persona").
- **Lo visible no depende del filtro.** Las personas citadas en campos visibles salieron por corrección declarada.
  - Tanda `origen-ia-atribuciones`: 5 correcciones ATRIBUCION. Fuera "Andy Grove" en 3 resúmenes, "Steve Jobs" y
    "Bill Campbell" del mismo resumen, y "liderado por Homer y Horowitz". El "modelo de Reason" pasa a "el modelo del
    queso suizo".
  - Tanda `origen-ia-atribuciones-2`: sale "al momento de esta fuente" de `antiboycott_regulations`.

### 12.3 C. La prueba en rojo primero

- `web/lib/origenIA.test.ts` construye los mensajes **reales** que recibe la IA, con un cliente falso que los
  captura:
  - la clasificación de la entrada;
  - el intérprete, con cada nodo de la muestra como nodo actual;
  - la puerta del seguimiento, en las cuatro fases;
  - el material del plan.
- La muestra es de 3 nodos vivos por cada uno de los espacios, más los 9 nodos con autor en el título que más pesan
  (entre ellos los tres "(Juran)"). La prueba mira también el grafo entero, las preguntas en caché, la orden fija y
  que no viaje ningún campo interno.
- **Antes del filtro, 6 pruebas en rojo:**
  - el grafo, con 98 textos;
  - la clasificación;
  - el intérprete, con 131 apariciones;
  - la puerta, con 13;
  - el plan;
  - la orden fija.
- **Después, 10 de 10 en verde.** `engine/test_origen_ia.py` prueba el filtro con casos calculados a mano y la vista
  entera.

### 12.4 D. Lo que quitaría el filtro en todo el catálogo

100 quitas.

- **En nodos vivos: 18 quitas en 18 nodos, todas en `titulo_concepto`.**

  | Nodo | Título que llega a la IA |
  |---|---|
  | `accion_correctiva_sistematica` | "Acción Correctiva Sistemática (Paso 6)" |
  | `adaptacion_14_puntos_servicio_medico` | "Adaptación de los 14 Puntos al Servicio Médico" |
  | `aim_of_leadership` | "Objetivo del Liderazgo" |
  | `benchmarking_7_pasos_juran` | "Proceso de Benchmarking de 7 Pasos" |
  | `benchmarking_trilogia_juran` | "Benchmarking y la Trilogía" |
  | `ciclo_pdca_pdsa` | "Ciclo PDCA/PDSA" |
  | `consejo_de_calidad` | "Consejo de Calidad (Liderazgo y Selección de Proyectos)" |
  | `consejo_de_calidad_2` | "Consejo de Calidad (Red Autogestionada de Profesionales)" |
  | `control_calidad_definicion` | "Control de Calidad como Proceso Universal (Trilogía)" |
  | `cuatro_etapas_del_pensamiento_creativo` | "Las Cuatro Etapas del Pensamiento Creativo" |
  | `juran_quality_by_design` | "Modelo de Calidad por Diseño (Quality by Design)" |
  | `juran_rcca_metodo` | "Método RCCA (Análisis de Causa Raíz)" |
  | `los_14_puntos_deming` | "Los 14 Puntos para la Transformación de la Gestión" |
  | `modelo_lubin_esty_4_etapas` | "Modelo de 4 Etapas de Creación de Valor en Sostenibilidad" |
  | `modelo_transformacion_juran` | "Modelo de Transformación (Cinco Breakthroughs)" |
  | `planificacion_cero_defectos` | "Planificación de Cero Defectos (Paso 7)" |
  | `proceso_benchmarking_juran_7pasos` | "Ciclo de Benchmarking de 7 Pasos" |
  | `trilogia_de_juran` | "Trilogía (Planificación, Control y Mejora)" |

- **En nodos deprecados: 82 quitas en 73 nodos** (72 en resúmenes, 9 en títulos y 1 en un paso). Son autores citados
  como fuente ("Crosby define…", "Deming enfatiza…"). Ningún nodo deprecado llega a una llamada ni al cliente.
- **Falsos positivos: ninguno.** Las 100 quitas son el autor de la lista. Las coincidencias con palabras comunes
  quedan fuera por diseño:
  - "reason to buy" y "brown-bag", en minúscula;
  - "MINI Cooper", la excepción declarada.

### 12.5 E. Cierre, y lo que no se puede cumplir sin una decisión del fundador

- A cumplido: ninguna llamada envía un campo interno. B aplicado a todas las llamadas por construcción. C en verde.
  D reportado.
- **Lo que no se puede cumplir tal cual: los identificadores de nodo.**
  - 25 nodos vivos llevan un apellido de la lista en su `node_id`. Ejemplos: `trilogia_de_juran`,
    `los_14_puntos_deming`, `wallas_etapa_incubacion` y 10 que empiezan o acaban en `crosby`.
  - Los ids viajan en el texto de 7 llamadas: Claridad (2), clasificación, intérprete, puerta, replanteamiento y plan.
    El modelo tiene que responder con ellos.
  - El filtro limpia textos, no identificadores. La guarda los mide aparte con una lista pendiente declarada, que no
    puede crecer.
  - Tres caminos:
    - **(a) Renombrar los 25 nodos** a ids neutros y dejar el viejo en `ids_alias`, el mecanismo que ya resuelve los
      proyectos guardados. Toca el dataset, los enlaces, las claves de la caché, las etiquetas traducidas y el índice
      semántico, sin re-embeber. Recomendado.
    - **(b) Traducir los ids en la frontera de cada llamada** y deshacerlo en la respuesta. Más cirugía y más riesgo.
    - **(c) Aceptarlos** como claves técnicas que la orden fija prohíbe citar.
- **Residuo histórico.** Las conversaciones y los estados vivos guardados antes de hoy en la base llevan los títulos
  viejos, con autor, y el intérprete reenvía ese historial en cada turno de una sesión abierta. Lo nuevo sale limpio.
  Limpiarlo pide un script sobre la base: no se hace sin el visto.
- **Herramienta local.** El motor Python no lleva `REGLA_SIN_FUENTES`. No es producción.

## 13. Decisiones del fundador sobre el añadido (1 oct 2026)

1. **Los nombres de método con apellido no son defecto.** Juran, Deming, Wallas, Crosby y similares son nombres de
   método, no atribuciones.
   - En lo que ve el cliente se prefiere el nombre neutro cuando existe (trilogía de la calidad, las cuatro etapas
     del proceso creativo). Si no existe ("los 14 puntos de Deming"), se queda.
   - La guarda de procedencia (sección 7) deja pasar los nombres sin alternativa neutra. Está en D5.
2. **Identificadores de nodo: opción (c).** Los 25 identificadores con apellido se aceptan como claves técnicas y no se
   renombra ninguno. La guarda impide que aparezca uno nuevo. Está en D6.
3. **Filtro hacia la IA con nombre neutro.** Si quitar el apellido deja el título sin sentido, el filtro pone el
   nombre neutro del método. Las sustituciones (`NEUTROS` en `scripts/origen_ia.py`) van antes de las quitas:
   - "Paso N de Crosby" pasa a "Paso N del programa de cero defectos";
   - "Trilogía de Juran" pasa a "Trilogía de la Calidad";
   - "14 Puntos de Deming" pasa a "14 Principios de Gestión de la Calidad";
   - "ciclo de Deming" o "de Shewhart" pasa a "ciclo PDCA";
   - "Cuatro Etapas de Wallas" pasa a "Cuatro Etapas del Proceso Creativo".

   Revisados los 18 títulos vivos, más uno nuevo (`ciclo_shewhart_pdsa`, "Ciclo PDCA (PDSA) para la Mejora
   Continua"), con este criterio:
   - Cambian a nombre neutro siete: los dos "Paso 6/7 de Crosby", los dos "14 Puntos de Deming" y las tres
     "Trilogía de Juran".
   - Los demás ya tenían sentido sin el apellido.

   La prueba web fija a mano el título que llega a la IA en cada uno de los 19, y el registro anota cada sustitución
   como "original -> neutro". El filtro hace ahora 101 quitas.
4. **Conversaciones guardadas antes de hoy:** no se limpian, porque todavía no hay usuarios reales.
5. **Los 2 casos pendientes de la medida 2, corregidos**, verificados a ciegas (paquete `paq_vp`: 3 elementos con 1
   trampa sin marca, una cifra inventada; la trampa se cazó y las 2 correcciones se sostienen):
   - a. `tratar_packaging_costo_marca`, título. "Trata el empaque como una variable de costo y de marca" pasa a "Trata
     el empaque como una variable de peso y de eficiencia en tus envíos". Es la tanda `medida2-pendientes` (ANADIDO):
     el libro habla del peso que añade el empaque y de su efecto en la eficiencia, no de la marca.
   - b. `outsourcing_ventas_fso`, pregunta base. La versión anterior atribuía al equipo externo conseguir a los
     posibles franquiciados; el libro dice que no genera los contactos. La pregunta nueva dice que atiende a los que
     atrae tu propia mercadotecnia y los lleva hasta el cierre, y conserva sus dos opciones.
     - Se corrigió directamente, sin campo aparte (corrección del fundador al punto 5b), con la herramienta nueva
       `scripts/fidelidad/corregir_preguntas.py` (tanda `preguntas-medida2-pendientes`, veredicto CONTRARIO).
     - El texto anterior queda en el registro interno `dataset/metadata/correcciones_preguntas.json`.
   - La regla queda en R1 y en R3 (excepción): las preguntas no se reescriben para adaptarlas, pero se reemplazan
     cuando son contrarias, inventan o su lógica no encaja.

## 14. Medida final: contrarios, invenciones duras y procedencia (1 oct 2026)

Diseño fijado en 11.3 antes de sortear: semilla 20261101, 200 nodos vivos con el reparto de la sección 3, 20 lotes de
10 con una trampa sin marca cada uno (7 contrarios, 7 invenciones duras y 6 procedencias), lector ciego contra el
libro, segundo lector si no caza la trampa, y árbitro. Las instrucciones son las de 11.3, con la precisión del fundador
de 13.1: un nombre de método con apellido no es procedencia. Cuenta en `docs/auditoria_final/medida_final.json`.

- **Detección:** el primer lector cazó 19 de 20 trampas. La del lote 05 (una invención) la cazó el segundo lector:
  20 de 20.
- **Arbitraje:** 9 defectos marcados en 7 nodos, los 9 confirmados como procedencia.

| Clase | Hallazgos | Por nodo | Wilson 95 % | Umbral | Resultado |
|---|---|---|---|---|---|
| Contrarios (U1) | 0 | 0 | 0 a 1,9 % | 0 | **PASA** |
| Invenciones duras (U2) | 0 | 0 | 0 a 1,9 % | 0 | **PASA** |
| Procedencia (D1) | 9 en 7 nodos | 3,5 % | 1,7 a 7,1 % | 0 | **NO PASA** |

- **Las 9 procedencias** son atribuciones blandas que las guardas mecánicas no ven:
  - "los datos muestran";
  - "según una estimación" y "según algunas estimaciones";
  - "al estilo Darwin";
  - "se dice que un fundador atribuía…" y "el fundador de una gran empresa explicaba";
  - y, en el mundo 11, "una directiva" o "en la experiencia de una directiva", que es como la forja anonimizó a la
    autora.
- **Corregidas** en la tanda `medida3-procedencia`: 9 correcciones ATRIBUCION en 7 nodos. Sale la atribución y queda
  el consejo dicho directamente.
- **Vecindad** (mismo libro y mismo campo, sin la muestra): 3.711 elementos en 6 libros. Se relee solo para
  procedencia, con trampas sin marca de atribución blanda (sección 14.1).

**Veredicto:**
- **Contrarios e invenciones: SANEADO en la muestra.** 0 en 200 nodos, con un residuo por nodo de como mucho 1,9 % al
  95 %.
- **Procedencia: no da 0.** El residuo estimado antes de corregir era 3,5 % de los nodos (1,7 a 7,1 %). Se cierra con
  la relectura de la vecindad, sin otra pasada.

### 14.1 Vecindad de la procedencia, corregida

Máquina en `auditoria-final-claves/medida3/vecindad.py`, semilla 20261111.

- **Qué se releyó:** 3.485 elementos, todos los resúmenes y pasos vivos de los 6 libros y campos de las 9 procedencias,
  sin la muestra. Fueron 24 lotes de unos 150, solo para procedencia, con una trampa sin marca de atribución blanda por
  lote.
- **Detección:** 24 de 24 trampas cazadas.
- **Arbitraje:** 226 marcas reales y 218 confirmadas. El grueso está en los dos libros del mundo 11, donde la forja
  escribió "una directiva", "hay quien" o "la autora" en lugar del nombre de la autora; el resto son "se estima que" y
  "los datos".
- **Corrección, por el método de la casa (C32/R8):**
  - 54 quitas puras.
  - 129 correcciones con palabras nuevas verificadas a ciegas (7 paquetes, 7 de 7 trampas cazadas). Están en la tanda
    `medida3-vecindad`: 183 correcciones en 122 nodos.
  - 35 no se sostuvieron. Al quitar la atribución, lo que el libro cuenta como la experiencia de una persona, un caso
    único o un estudio quedaba como ley universal; en 7 casos, además, la frase seguía el libro casi palabra por
    palabra. Se reescribieron conservando el alcance ("puede pasar que…") y se verificaron a ciegas (2 de 2 trampas
    cazadas): 26 se sostienen, en la tanda `medida3-vecindad-2` (26 correcciones en 21 nodos).
- **Quedan 9 sin corregir, para el visto del fundador.** El contenido es la vivencia de una sola persona: cualquier
  generalización la endurece, y conservarla tal cual exige la atribución.
  - Son 8 pasos del mundo 11 y un resumen de `riesgo_litigios_franquicia`.
  - Propuesta: quitar la frase anecdótica entera cuando el resto del elemento se sostiene solo (quitar antes que
    redactar). Si no se sostiene, el elemento se queda con la vivencia y sin nombre, como residuo declarado.

**Veredicto final de la medida:**
- **Contrarios e invenciones duras: SANEADO en la muestra** (0 en 200 nodos; residuo por nodo de 0 a 1,9 % al 95 %).
- **Procedencia: NO da 0 en la muestra** (3,5 %, de 1,7 a 7,1 %).
  - Se corrigieron las 9 de la muestra y 209 de su vecindad.
  - El residuo conocido son las 9 de arriba.
  - Fuera de esos 6 libros puede quedar atribución blanda, que ninguna guarda mecánica ve. La prevalencia medida antes
    de corregir (3,5 % de los nodos) es la cota que se declara para el resto del catálogo.

### 14.2 Auditoría de preguntas: tamaño y coste (para el visto del fundador, sin lanzar)

- **Preguntas:** 3.374, que son 3.288 bases de nodos vivos y 86 de entrada de las puertas. Las versiones neutrales
  todavía no existen: se generan con la API en el paso A2 de la corrida final, y tendrán que leerse después de
  generarse.
- **Método:** lotes de 40 preguntas, cada una con su nodo saneado y las etiquetas de sus candidatos. Una trampa sin
  marca por lote, de las tres clases (contraria, inventa, lógica que no encaja), plantada antes. Dos lectores Opus por
  lote, árbitro, y las que fallen se reemplazan con verificación ciega.
- **Agentes estimados: unos 210 a 220, en unas 12 olas de hasta 20.**
  - Lectores: 85 lotes × 2 = 170.
  - Preparadores de trampas: 4.
  - Árbitros: unos 28.
  - Reescritores: de 5 a 8.
  - Verificadores: de 5 a 8.
- **Coste:** unos 20 a 25 millones de tokens de subagente, a la vista de lo medido hoy. Una ola de 20 lectores de
  procedencia gastó 1,4 millones, y un lector de nodo contra su texto gasta unos 100.000.

### 14.3 Los 9 elementos con anécdota (decisión del fundador, 1 oct 2026)

Aprobada la propuesta: se quita la frase anecdótica cuando el resto se sostiene solo, por corrección declarada y sin
palabras nuevas.

- **Corregidos 4** (tanda `medida3-anecdotas`):
  - `reservar_valor_unico_prioridades_arriba`, paso 8: sale la vivencia de la directiva.
  - `pedir_critica_equipo_premiarla`, paso 6: queda "No reacciones a la defensiva."
  - `riesgo_litigios_franquicia`, resumen: sale la frase del estudio y su 26 %.
  - `alinear_prioridades_reporte_directivo`, paso 10: queda la pregunta sobre procesos sanos.
- **No se tocan 5, porque el consejo no se sostiene sin la anécdota** (el elemento entero es la vivencia). Quedan como
  residuo declarado de procedencia: no nombran a nadie, pero cuentan la experiencia de una persona.
  - `mover_rapido_persona_papel_equivocado`, pasos 0 y 1;
  - `pedir_ayuda_grupo_apoyo`, paso 0;
  - `disenar_entorno_rendir_mejor`, paso 4;
  - `admitir_pronto_mal_desempenio_cuatro_razones`, paso 0.

## 15. El encargo del fundador del 6 oct 2026

Prioridad: el dataset correcto (cero contrarios, cero invenciones, cero procedencia). En paralelo, las páginas legales
y de cuenta. La copia fiel no es prioridad: lo literal del libro no llega literal a la persona.

### 15.1 Puntos 1 a 3 y 6 (cerrados)

- **Punto 1:** la calculadora y el estimador de esfuerzo son métodos validados (REGLAS M1), sellados en
  `docs/metodos_validados.json` con su guarda (`engine/test_metodos_validados.py`). Para resellar hace falta el visto
  del fundador en el mensaje del commit.
- **Punto 2:** los 5 elementos de procedencia que quedaban se reescribieron como consejo con su matiz ("suele", "tiende
  a", "es fácil"), sin endurecerlos ni atribuirlos. Verificados a ciegas: 5 de 5, trampa cazada (tanda
  `procedencia-matiz`).
- **Punto 3, barrido de procedencia en todo el catálogo:**
  - Búsqueda mecánica de atribuciones blandas: 365 elementos, 60 confirmados.
  - Lectura dirigida del mundo 11 fuera de la vecindad: 2.416 elementos, 17 de 17 trampas, 30 confirmados.
  - Corregidos: 77 en 58 nodos (tanda `barrido-procedencia`) y 13 reescritos con su matiz (tanda
    `barrido-procedencia-2`, 13 de 13 verificados a ciegas).
- **Punto 6:** páginas públicas `/privacidad`, `/terminos`, `/cookies` (español y francés, con fecha),
  `/eliminar-cuenta` (sin app ni sesión) y `/preguntas-frecuentes`, con la estructura de iching-app. Siguen pendientes
  dos cosas del fundador: la revisión profesional y la dirección postal del comerciante.

### 15.2 Auditoría de preguntas (punto 4): CERRADA

Método de 14.2. Cada pregunta se leyó contra su propio nodo saneado. Fueron 3.374 preguntas: las bases de los nodos
vivos y las de entrada de las puertas.
- **Lotes:** 85, de unas 40 preguntas. Cada uno llevaba una trampa sin marca (contraria, inventa o lógica que no
  encaja), plantada antes.
- **Lectura:** dos lectores Opus independientes por lote, y un árbitro para cada pregunta marcada.
- **Reemplazos:** las que fallan se reemplazan por corrección declarada (`scripts/fidelidad/corregir_preguntas.py`,
  cita contra el nodo), con verificación ciega y una trampa sin marca por paquete. Máquina en
  `auditoria-final-claves/preguntas/` (auditoria.py, hacer_vq.py, hacer_tanda.py).

- **Detección:**
  - El lector A cazó 82 de 85 trampas y el B, 83 de 85.
  - En dos lotes (37 y 49) ninguno de los dos cazó la trampa. Las dos eran contrarias. Es el punto débil de la
    lectura: una pregunta contraria a su nodo es más difícil de ver que una que inventa o que no encaja.
- **Arbitraje:** de 182 preguntas marcadas, el árbitro confirma 171 y rechaza 11.
- **Corregidas: 171 preguntas en 171 nodos**, en las tandas `preguntas-auditoria-01` a `-04`:
  - 146 de lógica: preguntaba por otra cosa, presuponía algo falso o no servía para elegir entre los candidatos;
  - 15 contrarias a su nodo;
  - 10 que inventaban.
  - Todas tienen verificación ciega, en 6 paquetes con 6 de 6 trampas cazadas. Los reemplazos que no se sostuvieron
    se reescribieron hasta sostenerse, en tres rondas. Uno (`P004-24`, el M&OP) necesitó cuatro intentos.
- **Residuo:**
  - No queda ninguna pregunta con falla confirmada sin corregir.
  - El residuo posible es lo que ningún lector vio: 2 de 85 lotes con su trampa no cazada por ninguno. Las
    contrarias son las que más se escapan.
- **Las versiones neutrales** (A2 de la corrida final) todavía no existen. Se generan con la API y se auditan igual
  antes de usarse.

### 15.3 Medida 4, solo procedencia: diseño fijado antes de sortear (6 oct 2026, 23:35)

- **Semilla: 20261006**, escrita aquí antes de sortear. Muestra con `scripts/auditoria_final/muestra.py 20261006`:
  200 nodos vivos con el reparto de la sección 3. Puede repetir nodos de muestras anteriores; mide el catálogo de hoy,
  después de los puntos 2 y 3.
- **Qué mide:** solo procedencia (D1). Es atribuir lo que se dice a una persona (con nombre o sin él), a un libro, a
  "los estudios", "los datos", "una estimación", "los expertos" o "se dice que". Un nombre de método con apellido no
  es procedencia (13.1).
- **Qué se lee:** todos los textos de cara de cada nodo, uno por elemento. Son la etiqueta, el resumen, cada paso,
  cada condición, el entregable y la pregunta base.
- **Lotes y trampas:** 20 lotes de 10 nodos. Cada lote lleva un elemento trampa sin marca: un texto real de un nodo
  del mismo espacio, fuera de la muestra, con una atribución blanda plantada. Las trampas son de las formas que se
  encontraron en las medidas y barridos.
- **Lectura:**
  - Un lector Opus ciego por lote, con las instrucciones de la relectura de procedencia (14.1).
  - Segundo lector si no caza la trampa.
  - Árbitro de cada marca.
- **Veredicto:**
  - "SANEADO en procedencia" si da 0 nodos.
  - Si no, nodos con procedencia confirmada sobre 200, con su intervalo de Wilson al 95 %.
  - Los 5 elementos del residuo declarado (14.3) cuentan si salen en la muestra.
  - Lo que aparezca se corrige por el método de la casa. No hay otra pasada.

### 15.4 Resultado de la medida 4 (6 y 7 oct 2026): NO da 0

Máquina en `auditoria-final-claves/medida4/medida4.py`.

- **Lectura:** 20 lotes de 96 a 147 elementos, uno por cada texto de cara de los 200 nodos.
  - El primer lector cazó 20 de 20 trampas.
  - Hubo 24 marcas reales, y el árbitro confirmó 20.

| Clase | Hallazgos | Por nodo | Wilson 95 % | Umbral | Resultado |
|---|---|---|---|---|---|
| Procedencia (D1) | 20 en 18 nodos | 9 % | 5,8 a 13,8 % | 0 | **NO PASA** |

- **Lo nuevo, que ninguna guarda veía:**
  - Nombres propios de personas como fuente: "El filósofo … llama", "Popularizada por …", "Basado en el modelo de …",
    "las 6 preguntas de … y …".
  - Una referencia: "(ver NIST SP 800-60)".
  - Juicios ajenos impersonales: "se estima", "considerado la base", "es la recomendada", "el primer paso sugerido".
  - El barrido 1 (punto 3) buscaba atribuciones blandas genéricas. La guarda de títulos solo conoce los libros de la
    lista canónica.
- **Corrección de las 20, por el método de la casa:**
  - Las 20 pasaron por verificación ciega contra el libro, también las que solo quitaban: cambiar "se estima" por
    "es" endurece. Fueron 2 paquetes, con 2 de 2 trampas cazadas.
  - 13 se sostienen (tanda `medida4-procedencia`).
  - 7 endurecían: quitaban "se estima", "en un estudio" o "según los autores" y dejaban una regla general. Se
    reescribieron con el alcance del libro y se verificaron a ciegas: 7 de 7, trampa cazada (tanda
    `medida4-procedencia-2`).
  - **Las 20 de la muestra quedan corregidas.**

**Remedio en todo el catálogo: barrido 2.** No cambia el veredicto medido; reduce el residuo.
- **Búsqueda mecánica** (`barrido_nombres.py`) de lo que la medida descubrió. Encontró 1.392 elementos:
  - nombres propios (un par de palabras con mayúscula en el que alguna nunca aparece en minúscula en el catálogo);
  - verbos de autoría, "basado en el modelo de", "según" seguido de un nombre;
  - oficios de autor, citas y referencias;
  - juicios impersonales.
- **Arbitraje:** 20 árbitros Opus, uno por paquete de unas 70, con una trampa sin marca por paquete (una atribución a
  una persona con nombre inventado). Cazaron 20 de 20 trampas.
  - Confirmaron 81 en 80 nodos. Entre ellas: George Box, Kaoru Ishikawa, Goldratt, Kim y Mauborgne, Alan Kay, Peter
    Senge, Bill Campbell, Saarinen, Jens Rasmussen, Charles Perrow, Heider y Simmel, "la investigación de Huthwaite" y
    organizaciones como origen de un método (XPLANE, Boeing).
- **Verificación ciega contra el libro:** 5 paquetes, 5 de 5 trampas cazadas.
  - 58 se sostienen (tanda `barrido2-procedencia`).
  - 16 endurecían o dejaban una traducción literal. Se reescribieron con su matiz y se verificaron otra vez: 15 de
    16, trampa cazada (tanda `barrido2-procedencia-2`).
  - Van con ellas dos quitas puras del origen de un método en una organización (Motorola, Shell), con el precedente
    de los árbitros.
  - La guarda de voz cazó un "Se ilustra con" que dejó una corrección; sale por quita pura (tanda
    `barrido2-procedencia-voz`).
  - La última, el hallazgo temprano de productividad de la IA (B15-045), se sostuvo al tercer intento (tanda
    `barrido2-procedencia-3`, trampa cazada).
- **Guarda nueva:** `engine/test_procedencia_nombres.py` (REGLAS D1). Ninguna persona u organización con nombre como
  fuente en los textos de cara del grafo: autoría, "basado en el modelo de", "según X", "el filósofo X", citas y
  referencias.
  - Prueba en rojo primero: cazó 6. Cuatro se corrigieron; las otras dos eran etiquetas en mayúscula de título, que
    la guarda ya no lee para "según".

**Veredicto de la medida 4: procedencia NO da 0 en la muestra** (9 % de los nodos, de 5,8 a 13,8 % al 95 %).
- Corregidos: los 20 de la muestra y 76 correcciones del barrido 2 (58 + 17 + 1).
- El residuo que se declara es lo que ni la búsqueda mecánica ni la lectura de la muestra ven: atribución sin nombre
  propio ni verbo de autoría. La prevalencia medida antes de corregir (9 %) es la cota para el resto del catálogo.
- Lo que queda pendiente se decide con el fundador: si medir otra vez con semilla nueva después del barrido 2, o leer
  el catálogo entero solo para procedencia (unos 350 lotes; ver `docs/PROXIMOS_PASOS.md`).

### 15.5 Punto 8: promesas no graves y condiciones de los nodos de otro país

**Promesas:** los 28 hallazgos medios y bajos del informe de promesas públicas quedan corregidos en los 11 idiomas.
- Hay guardas nuevas que impiden volver a cada promesa.
- El precio del plan en la portada sale de `PRECIOS`.
- Quedan para el visto: el nombre "Riesgos Bajo Control" y los mockups del canon (`promesas_publicas.md`, estado).

**Condiciones de activación de los nodos-frontera de otro país** (clase C de `jurisdiccion.json`, 104 nodos vivos).
Es el único campo de estos nodos que la etapa 1 no leyó contra el libro. Máquina en
`auditoria-final-claves/condiciones/condiciones.py`.
- **Lectura:** 8 lotes de 13 nodos, con dos lectores Opus por lote y las instrucciones del lector E1B, limitados a las
  condiciones con `a_juzgar`.
  - Cada lote llevaba un nodo trampa de clase B con una invención plantada en una condición.
  - Cazaron 16 de 16 trampas.
- **Marcas:** 103 defectos en 57 nodos.
- **Arbitraje:** 4 árbitros (instrucciones E1B), sobre 61 elementos.
  - Confirmados: 88 de matiz, 4 invenciones duras, 2 contrarios y 2 certezas endurecidas.
  - Correcciones: 55 elementos, en modo devolver casi todos.
- **Verificación ciega contra el libro:** de las 53 que traían palabras nuevas se sostienen 53, en 3 paquetes con 3 de
  3 trampas cazadas.
- **Aplicadas:** 55 correcciones en 52 nodos (tanda `condiciones-frontera`).
- **Lo que no se leyó:** las condiciones de los nodos de clase B (123) y A (12). Un nodo B se reencuadra a lo
  universal, así que sus condiciones no limitan a un país. Si se quiere, la misma máquina las lee cambiando la clase.

### 15.6 Medida 5, solo procedencia, después del barrido 2: diseño fijado antes de sortear (7 oct 2026, 01:15)

Es la decisión 1 (a) de `docs/PROXIMOS_PASOS.md`, tomada con la cuota que queda antes del jueves. No cambia el
veredicto de la medida 4: mide el catálogo de hoy, después del barrido 2 y de su guarda.
- **Semilla: 20261008**, escrita aquí antes de sortear. Muestra con `scripts/auditoria_final/muestra.py 20261008`:
  200 nodos vivos con el reparto de la sección 3.
- **Igual que la medida 4 (15.3):** 20 lotes de 10 nodos, todos los textos de cara, una trampa sin marca por lote
  (atribución blanda, ahora también con nombre propio), lector Opus ciego, segundo lector si no caza, árbitro.
- **Veredicto:**
  - "SANEADO en procedencia" si da 0 nodos.
  - Si no, nodos sobre 200 con su Wilson al 95 %.
  - Lo que aparezca se corrige por el método de la casa.

### 15.7 Resultado de la medida 5 (7 oct 2026): NO da 0, pero baja a la mitad

Máquina en `auditoria-final-claves/medida5/medida5.py`.
- **Lectura:** el primer lector cazó 20 de 20 trampas, también las de nombre propio inventado.
- **Arbitraje:** 11 marcas reales; el árbitro confirmó 10.

| Clase | Hallazgos | Por nodo | Wilson 95 % | Medida 4 (antes del barrido 2) | Resultado |
|---|---|---|---|---|---|
| Procedencia (D1) | 10 en 10 nodos | 5 % | 2,7 a 9,0 % | 9 % (5,8 a 13,8 %) | **NO PASA** |

- **Lo que queda** son formas que ninguna búsqueda mecánica ve:
  - "los mejores administradores a menudo…", "los mejores pensadores de diseño…";
  - "hay quien…";
  - "la experiencia con la certificación enseña…";
  - un autor nombrado sin verbo de autoría ("Aristóteles entendía…", "del enfoque de Papanek…", "ejemplificada por
    guías turísticos como …");
  - una cita entre comillas sin fuente;
  - "Los couriers coinciden";
  - "(Caso 2)", una remisión a la numeración de casos del libro.
- **Corrección:**
  - Verificación ciega contra el libro, con la trampa cazada: 7 se sostienen (tanda `medida5-procedencia`).
  - 3 endurecían o dejaban una traducción literal. Se reescribieron con su matiz y se verificaron a ciegas: 3 de 3,
    trampa cazada (tanda `medida5-procedencia-2`).
  - **Las 10 de la muestra quedan corregidas.**

**Lectura del resultado:**
- El barrido 2 redujo el residuo del 9 % al 5 %. Los intervalos se solapan, así que la bajada no es concluyente con
  200 nodos.
- Lo que queda pide lectura humana o de agente, no búsqueda: unos 350 lotes para leer el catálogo entero (decisión 1 de
  `docs/PROXIMOS_PASOS.md`).

### 15.8 Lectura total de procedencia (decisión 1 b de `docs/PROXIMOS_PASOS.md`, 6 y 7 oct 2026)

Máquina en `auditoria-final-claves/lectura_total/lectura_total.py`, semilla 20261019. Instrucciones de los agentes en
`auditoria-final/lectura_total/` (lector, árbitro y reescritor; el verificador es el de siempre,
`remedio/INSTRUCCIONES_E1B_VERIFICADOR.md`).

**Qué se leyó:** todos los nodos vivos de los once espacios, 3.634 nodos en 368 lotes de 10, con los mismos campos de
cara que la medida 4. Fueron 40.536 elementos, cada uno leído por un lector. Cada lote llevaba una trampa sin marca (un
elemento real con una atribución plantada).

| Paso | Resultado |
|---|---|
| Lectura | 368 de 368 trampas cazadas; 503 marcas reales |
| Árbitro | 458 confirmadas, 45 descartadas |
| Verificación ciega contra el libro | 61 paquetes, 61 de 61 trampas cazadas |
| Se sostienen a la primera | 404 |
| Reescritas con la misma certeza y verificadas otra vez | 52 a la primera reescritura, 2 a la segunda |
| **Aplicadas** | **458 correcciones en 393 nodos**, en 42 tandas `lectura-total-*` |

Por campo: 309 resúmenes, 136 pasos, 7 condiciones, 4 entregables y 2 etiquetas. Las dos etiquetas cambiadas se
tradujeron a los diez idiomas (guardia de vigencia de etiquetas).

**Lo que la verificación no vio y pararon las guardas** (tres casos, ninguno llegó al catálogo):
- una etiqueta de 9 palabras. Desde entonces la tanda rechaza sola toda etiqueta de más de 6;
- "tu organización", que la guarda de residuo corporativo de `aplicar_correcciones.py` rechazó;
- un dato al que se le quitó "estudios" pero que contaba en qué país y en qué década se observó. Lo paró la guarda de
  jurisdicción. Desde entonces el reescritor, el árbitro y el verificador tienen escrito que contar dónde o cuándo se
  observó algo también es procedencia.

**Lo que se aprendió por el camino:** en la ola 30 el árbitro dejaba casos como tendencia ("suele") y calcaba listas
del libro. La verificación rechazó 10 de 33. Con la instrucción afinada ("suele", "a menudo" y "en general" también
endurecen), las olas siguientes bajaron a entre 0 y 6 rechazos por ola.

**Lectura del resultado:**
- Cada elemento del catálogo fue leído una vez buscando procedencia, y cada corrección pasó por árbitro, libro y
  suites.
- Esto **no es una medida**. Un solo lector por lote y una trampa de forma conocida no dicen cuánta procedencia sutil
  queda. Para saberlo hace falta una medida 6 con semilla nueva, sobre una muestra que no se haya leído para corregir.
- El alcance fue solo procedencia: contrarios e invenciones siguen con el estado de la sección 14.

### 15.9 Medida 6, solo procedencia, después de la lectura total: diseño fijado antes de sortear (7 oct 2026)

Mide cuánta procedencia queda en el catálogo después de la lectura total (15.8). No reinterpreta las medidas 4 y 5.
- **Semilla: 20261023**, escrita aquí antes de sortear. Muestra con `scripts/auditoria_final/muestra.py 20261023`:
  200 nodos vivos con el reparto de la sección 3. (La primera versión de esta sección escribió 20261021, que ya era la
  semilla de la ciega de fases del mundo 11. Se cambió antes de sortear nada.)
- **Igual que las medidas 4 y 5 (15.3 y 15.6):**
  - 20 lotes de 10 nodos, con todos los textos de cara;
  - una trampa sin marca por lote, con la misma lista de atribuciones blandas de la medida 5;
  - lector Opus ciego, segundo lector si no caza, y árbitro.
- **Lector:** las instrucciones de la lectura total (`auditoria-final/lectura_total/INSTRUCCIONES_LECTOR.md`), que
  añaden las formas que más se escaparon: "los mejores X", "hay quien", el autor nombrado de pasada, la cita sin fuente,
  y contar dónde o cuándo se observó un dato.
- **Veredicto:**
  - "SANEADO en procedencia" si da 0 nodos.
  - Si no, nodos sobre 200 con su Wilson al 95 %.
  - Lo que aparezca se corrige por el método de la casa.

### 15.10 Resultado de la medida 6 (7 oct 2026): 1 de 200, NO da 0

Máquina en `auditoria-final-claves/medida6/medida6.py`, semilla 20261023, muestra en
`docs/auditoria_final/muestra_20261023.json`.
- **Lectura:** el primer lector cazó 20 de 20 trampas; no hizo falta segundo lector.
- **Arbitraje:** 13 marcas reales; el árbitro confirmó 1 y descartó 12.

| Clase | Hallazgos | Por nodo | Wilson 95 % | Medida 5 (antes de la lectura total) | Resultado |
|---|---|---|---|---|---|
| Procedencia (D1) | 1 en 1 nodo | 0,5 % | 0,09 a 2,8 % | 5 % (2,7 a 9,0 %) | **NO PASA** (no es 0) |

- **Lo que queda:** "Ejemplos documentados incluyen…" en un resumen. Es una insinuación de fuente sin nombre, del tipo
  "los datos muestran".
- **Lo que el árbitro descartó** fueron casos que ilustran sin respaldar: "como hizo una directiva", "como en un caso
  de discos de freno", un método con nombre propio (el Sistema de Producción Toyota, igual que el ciclo PDCA), "hay
  quien es de mañana" (que describe la diversidad que el texto afirma) y pasivas sin agente ("el orden propuesto").
- **Corrección:** verificación ciega contra el libro con la trampa cazada; se sostiene. Tanda `medida6-procedencia`:
  1 corrección en 1 nodo. **La muestra queda corregida.**

**Lectura del resultado:**
- La lectura total bajó el residuo del 5 % al 0,5 %. Esta vez los intervalos no se solapan (2,7 a 9,0 % frente a
  0,09 a 2,8 %), así que la bajada sí es concluyente con 200 nodos.
- El techo al 95 % es del 2,8 % por nodo: como mucho unos 100 de los 3.634 nodos vivos con alguna procedencia sutil, y
  lo más probable es que sean unos 20.
- Llegar a 0 en la muestra pediría otra lectura total del catálogo, que es la decisión 1 de `docs/PROXIMOS_PASOS.md`.

### 15.11 Decisiones del fundador sobre la medida 6 (7 oct 2026)

1. **Procedencia: se acepta el residuo declarado (opción c).** No se hace una segunda lectura total. El veredicto de
   procedencia del catálogo queda así:
   - 1 nodo con procedencia en una muestra de 200 (0,5 %), ya corregido;
   - residuo estimado por nodo, con Wilson al 95 %: de 0,09 a 2,8 %. Sobre los 3.634 nodos vivos son entre 3 y 100
     nodos, lo más probable unos 20;
   - lo que queda son formas muy blandas, del tipo "ejemplos documentados", sin nombre propio ni verbo de autoría.
   - Cuando un nodo aparezca con procedencia, se corrige por el método de la casa, sin medida nueva.
2. **El recompilado no vuelve a dejar el grafo sin curaduría.** Fue la segunda vez que correr `run_phase1.py` dos
   veces dejó el dataset con etiquetas de libro (15.10). El paso 6 aplica ahora la curaduría antes de escribir, con la
   función y las listas de `etiquetas_de_cara.py`, que siguen siendo la única fuente. Prueba en rojo primero:
   `test_recompilar_no_deja_el_grafo_sin_curaduria` en `engine/test_aviso_curaduria.py`. Dos corridas seguidas dejan
   el grafo idéntico, byte a byte. Regla M19 de `docs/REGLAS_DE_LA_CASA.md`.
3. **La licencia de IDEO.org:** decisión tomada, los 20 nodos se quedan. Anotada en `fuentes_canonicas.json` y en el
   inventario interno de fuentes.

### 15.12 Condiciones de los nodos de clase B y A: diseño fijado antes de sortear (7 oct 2026)

Es lo que quedó sin leer en 15.5 (`docs/PROXIMOS_PASOS.md`, sección 7). Tras cerrar las decisiones de 15.11, es lo
primero del plan que no espera a nadie.
- **Qué se lee:** las condiciones de activación de los nodos vivos de clase B (123) y A (12) de `jurisdiccion.json`,
  135 nodos y 258 condiciones, contra su libro.
- **Semilla: 20261024**, escrita aquí antes de sortear.
- **La misma máquina que la clase C:** `auditoria-final-claves/condiciones_ba/condiciones_ba.py`.
  - 10 lotes, con dos lectores Opus por lote y las instrucciones del lector E1B, limitados a las condiciones con
    `a_juzgar`.
  - Una trampa sin marca por lote, plantada en una condición de un nodo de clase C (ya corregido), con las mismas
    invenciones de 15.5.
  - Árbitro E1B y verificador ciego contra el libro de toda corrección que traiga palabras nuevas, con una trampa
    por paquete.
- **Lo que sale:** una tanda `condiciones-ba` con lo que se sostiene. Lo que no se sostiene se queda como está.

**Resultado (7 oct 2026):**

| Paso | Resultado |
|---|---|
| Lectura | 20 lectores, 20 de 20 trampas cazadas; 39 marcas en 24 condiciones |
| Árbitro | 2 paquetes: 22 condiciones corregidas (15 de matiz, 5 contrarias, 1 invención dura y 1 certeza endurecida); 2 rechazadas |
| Modo | 4 quitan y 18 devuelven el sentido del libro |
| Verificación ciega contra el libro | las 18 que traían palabras nuevas se sostienen, con la trampa cazada |
| **Aplicadas** | **22 correcciones en 22 nodos** (tanda `condiciones-ba`) |

- Una pega que paró la guarda: tres citas apuntaban a ficheros de `txt/` y la tanda solo sabía normalizar `books/`.
  `aplicar_correcciones.py` rechazó la tanda entera ("cita sin libro") y no escribió nada. Se corrigió la tanda, que
  ahora toma el libro del campo `fuente` del nodo.
- El re-embebido no crece: los 22 nodos ya estaban entre los 2.808 de la línea de `docs/PROXIMOS_PASOS.md`, que
  incluye `condiciones-*.json`.
- **Con esto, las condiciones de los 239 nodos de `jurisdiccion.json` (clases A, B y C) quedan leídas contra el
  libro.**

**Errata declarada de 15.10:** el campo `decision` de la tanda `medida6-procedencia` dice "medida 5 de procedencia"
por un resto del script copiado. Es la medida 6; el campo `auditoria` sí es el correcto (15.9). Es metadato interno y
no cambia nada de lo aplicado; el script ya está corregido.

### 15.13 Saneamiento continuo del resto del dataset: diseño fijado antes de sortear (7 oct 2026)

Instrucción del fundador del 7 oct 2026: el saneamiento del dataset corre en paralelo con el resto del trabajo, ola
tras ola, y no se detiene. Sigue fuera la copia fiel. Dos corrientes, cada una con su semilla escrita aquí antes de
sortear.

**Corriente 1, condiciones del resto de nodos (semilla 20261025).**
- Se leen contra su libro las condiciones de activación de los nodos vivos que no están en `jurisdiccion.json`. Las
  de esos 239 nodos ya se leyeron (15.5 y 15.12).
- Máquina: `auditoria-final-claves/condiciones_resto/condiciones_resto.py`.
  - Lotes de 14 nodos, con un lector Opus por lote con las instrucciones del lector E1B, limitado a las condiciones.
  - Una trampa sin marca por lote, en un nodo de `jurisdiccion.json` ya corregido.
  - Si el lector no caza su trampa, un segundo lector relee el lote.
  - Árbitro E1B por ola y verificador ciego contra el libro de toda corrección con palabras nuevas, con una trampa
    por paquete.
  - Una tanda `condiciones-resto-<ola>` por ola.

**Corriente 2, la voz de lo que ve el cliente (semilla 20261026).**
- Se leen los campos que el cliente ve crudos: `etiqueta_arbol`, `pasos_accionables` y `entregable_esperado`, de
  todos los nodos vivos. Es la decisión del fundador del 30 sep 2026 (10.4).
- Defectos, con las definiciones del lector de la medida 1:
  - **etiqueta:** no es fiel a su nodo (promete otra cosa), o no le habla a la persona en segunda persona con un
    verbo, o trae jerga cruda o inglés, o no tiene de 4 a 6 palabras;
  - **ortografía:** una falta, incluidas tildes y signos de apertura;
  - **calco del inglés:** una traducción literal que en español suena ajena, o un término en inglés sin traducir
    cuando hay uno corriente.
- No hace falta el libro: se juzga contra el propio nodo.
- Las etiquetas que ya fija la curaduría (`etiquetas_de_cara_v1*.json`) no se leen: las revisó el fundador o el
  auditor, y la curaduría manda sobre el nodo.
- Máquina: `auditoria-final-claves/voz/voz.py`.
  - Lotes de 25 nodos con un lector Opus.
  - Una trampa sin marca por lote; el tipo rota entre ortografía, calco y etiqueta.
  - Árbitro por ola.
  - Verificador ciego que comprueba que la corrección arregla el defecto sin cambiar el sentido, con una trampa por
    paquete que sí lo cambia.
- Veredictos de la tanda `voz-<ola>`:
  - `ORTOGRAFIA`;
  - `VOZ` para calcos y forma de la etiqueta, con los fragmentos que salen;
  - `COHERENCIA` para una etiqueta infiel a su nodo.
- Toda etiqueta que cambie se retraduce a los diez idiomas, con su huella.

**Cadencia.**
- Solo la sesión principal hace commit.
- Cada tanda entra con el ciclo entero: aplicar, Gate 0, etiquetas, familias, sincronizar y las dos suites.
- Los ficheros derivados del grafo se regeneran, nunca se fusionan a mano.
- Se alternan con los commits de código.

### 15.14 Saneamiento continuo: fallos de método declarados (7 oct 2026)

Las cifras de cada ola están en sus tandas (`docs/saneamiento/tandas/voz-*.json` y `condiciones-resto-*.json`). Aquí
queda lo que el método no hizo bien, para que nadie lo dé por cubierto.

- **Lote de voz 035: la cobertura no está certificada.** Ni el lector a ni el segundo lector cazaron la trampa. Sus
  marcas pasaron igual por el árbitro y por el verificador ciego (cada paquete con su trampa, cazada), así que lo
  aplicado de ese lote está comprobado. Lo que no se puede afirmar es que esos 25 nodos estén limpios: pudo quedar un
  defecto sin marcar. Queda para la pasada de cierre del saneamiento continuo, con un lector nuevo y su trampa.
- **Lo que la verificación no sostiene no entra.** Cada ola guarda esos elementos en `no_sostienen_<ola>.json`
  (fuera del repositorio, junto a las claves). Esta noche son 20 de voz y 0 de condiciones. Quedan para una pasada de
  reescritura: el defecto que marcó el lector puede ser real aunque la corrección propuesta no sirviera.
- **La lista de tildes mecánicas traía una palabra ambigua.** Tenía "cambiaria" → "cambiaría", que rompe el adjetivo
  ("cobertura cambiaria"). Dañó un nodo (`gestion_riesgo_cambiario`, entregable), y los lectores de voz-v07 lo
  devolvieron a su forma correcta. La guarda permanente de la lista lo habría vuelto a romper. La palabra sale de la
  lista y entra a las ambiguas de su prueba (`engine/test_tildes_mecanicas.py`, en rojo primero). Las demás
  "cambiaría" del grafo son verbo.
- **La máquina de voz no contaba los nodos deprecados al buscar choques de etiqueta.** El grafo de la web los
  conserva y su guarda de unicidad los cuenta. Así, voz-v07 le dio a `nueve_pasos_iniciar_programa` la etiqueta de su
  gemelo deprecado y la suite web lo paró antes del commit. Suplemento voz-v07b con una etiqueta distinta y fiel, y
  `voz.py` ahora mira todos los nodos.

#### 15.14 (cierre) La pasada de cierre del saneamiento continuo (7 oct 2026, noche)

Las dos corrientes están leídas enteras: 146 lotes de voz y 243 de condiciones, cada uno con su trampa cazada por su
lector o por el segundo. Cifras totales en las tandas: **voz, 3.524 correcciones en 1.798 nodos** (3.295 de voz, 162
de ortografía, 67 de coherencia); **condiciones del resto, 196 correcciones en 189 nodos** (36 contrarios, 160
añadidos). Lo que quedó abierto arriba se cerró así:

- **Lote de voz 035, certificado.** `voz.py releer 035` lo rearmó como lote `035r` con el texto vigente de los mismos
  25 nodos y una trampa de otro tipo (ortografía, antes calco). Un lector nuevo la cazó y marcó un defecto, que pasó por
  árbitro y verificador ciego (tanda voz-v20).
- **Dos nodos del lote de condiciones 190, leídos.** Su lector no pudo abrir las carpetas de sus libros (el sistema de
  permisos negó el acceso) y los dejó sin juzgar, dicho en su salida. `condiciones_resto.py releer 190` los rearmó como
  lote `190r` con su trampa; el lector nuevo abrió los libros, cazó la trampa y no halló defecto.
- **Lo que la verificación no sostuvo, reescrito.** 48 de voz y 2 de condiciones, de todas las olas. Casi todos eran
  arreglos fieles que chocaban con una baranda de la casa (23 añadían "puntuación" o "del 1 al 10", 2 formas de
  organigrama) o etiquetas que no tenían de 4 a 6 palabras (10). Un reescritor recibió el texto vigente, la propuesta
  retenida y el motivo (`voz.py reescritura`, `condiciones_resto.py reescritura` y `reescritos`; instrucciones
  `INSTRUCCIONES_REESCRITOR.md` y `INSTRUCCIONES_E1B_REESCRITOR.md`) y su salida pasó por el verificador ciego con
  trampa como cualquier ola: voz-v21 (46 correcciones; el reescritor dejó 1 como estaba porque el defecto no se
  sostenía) y condiciones-resto-c27 (2).
- **Residuo declarado: una etiqueta.** `V140-112`, la etiqueta del concepto del índice Cpk: el verificador no sostuvo
  ninguna de las dos propuestas porque una etiqueta corta pierde lo que distingue al Cpk del Cp. Se queda la vigente.

### 15.15 Copia fiel (regla D2): diseño y regla de parada fijados antes de sortear (7 oct 2026)

Decisión del fundador del 7 oct 2026: con la cuota que queda se corrige ya la copia fiel (ningún texto de nodo es copia
ni traducción palabra por palabra de un pasaje de su libro), sin releer lo ya certificado para otros criterios.

- **Orden:** primero los **pasos** de los 3.634 nodos vivos (lo que el cliente ve en el plan sin IA); después los
  **resúmenes** y las **condiciones**. Los pasos que la casa declaró suyos (constancia CASA) no se leen: no vienen de
  ningún libro.
- **Contra su libro:** cada elemento se compara con el libro de su nodo; en los 54 nodos fusionados, con todos los
  libros de `fuentes_internas`, y la frase se juzga contra el libro del que viene.
- **Lector** (uno por lote, nodos agrupados por libro, semilla de lotes **20261027**): decide `copia` o `no_copia` y, si
  es copia, reescribe la FORMA (palabras, orden, estructura) sin tocar el contenido: ningún matiz perdido, ninguna
  condición ni plazo que caiga, nada añadido. Cada lote lleva una trampa sin marca: una traducción literal de un tramo
  de su libro, preparada por un agente aparte. Si el lector no la caza, un segundo lector relee el lote.
- **Verificador ciego** con dos trampas sin marca por paquete: una copia que no se corrigió (el texto nuevo es el viejo)
  y una reescritura que cambia el sentido. Comprueba a la vez que el texto nuevo ya no es copia y que dice exactamente lo
  mismo que el libro. Lo que no sostiene no entra y va a una pasada de reescritura con su motivo.
- **Reglas de la casa:** sin voz de libro, sin procedencia, tuteo neutro, el glosario y las palabras reservadas; la
  tanda no entra si sube cualquier guarda o baranda. Veredicto de la corrección: `COPIA`, con su cita (libro, líneas y
  una frase de 15 palabras como mucho).
- **Regla de parada:** al terminar, una muestra de **200 nodos con semilla 20261028** mide SOLO copia fiel y, de
  control, contrarios e invenciones. Si la copia da como mucho **1 cada 20 nodos** (10 de 200) y contrarios e
  invenciones dan **0**, se cierra declarando el residuo con su intervalo de Wilson al 95 %. Si no, se corrige lo hallado
  y su vecindad (mismo libro y mismo campo), sin otra pasada completa.
- **Voyage al final**, en una sola pasada con todo corregido.
- Lo que no quepa antes de que se agote la cuota del jueves 8 queda al día en `docs/PROXIMOS_PASOS.md`, con prioridad a
  que los pasos queden terminados.

### 15.16 Copia fiel: lo hecho y resultado de la medida 7 (7 oct 2026): NO CERTIFICADO

**La pasada completa.** Se leyeron y verificaron los 728 lotes del plan:
- 242 lotes de pasos;
- 243 de resúmenes;
- 243 de condiciones.

Cada lector cazó su trampa, y los verificadores ciegos cazaron todas las suyas.

Entraron 4.750 correcciones de forma en 1.698 nodos:
- 3.361 pasos en 804 nodos;
- 1.314 resúmenes;
- 75 condiciones.

Eso incluye dos pasadas de reescritura sobre lo que el verificador no sostuvo: r1 sobre los pasos y r2 sobre los
resúmenes y las condiciones. Quedan como residuo declarado 49 pasos y 30 resúmenes o condiciones. Para esos elementos
el reescritor y el verificador no encontraron una forma nueva que dijera exactamente lo mismo.

**Voyage, primera pasada** (orden del fundador del 7 oct 2026, antes de la medida y del fin de la cuota):
- Re-embebió los 2.706 nodos cuyo texto embebible cambió desde el índice anterior.
- El índice quedó coherente y Gate 0 y las dos suites quedaron en verde.
- Está desplegado en producción (commit d4dc7377).

**Medida 7.** Se usó la muestra de 200 nodos con la semilla 20261028, fijada antes de sortear en 15.15.
- Se leyeron 20 lotes con una trampa sin marca cada uno, y se cazaron las 20.
- Los lectores dejaron 148 marcas, y el árbitro confirmó 144 y rechazó 4.

| tipo | nodos con al menos un defecto confirmado | proporción | Wilson 95 % |
|---|---:|---:|---|
| copia | 57 de 200 | 28,5 % | 22,7 a 35,1 % |
| contrario | 0 de 200 | 0 % | 0,0 a 1,9 % |
| invención | 1 de 200 | 0,5 % | 0,1 a 2,8 % |

La regla pedía como mucho 10 de 200 en copia, y cero contrarios y cero invenciones. **No se cumple: la copia fiel NO
queda certificada.**

**Dónde está la copia que quedó.**
- Pasos: el árbitro confirmó 106 elementos. De ellos, 93 vienen de cuatro libros (42, 34, 10 y 7), los cuatro del
  mundo Primer Equipo.
- Resúmenes: confirmó 38 elementos, repartidos entre 21 libros.
- La primera pasada sí había leído todos los nodos de esos cuatro libros: 425 nodos y 3.767 pasos. Los dejó pasar.
- La medida aplicó la vara del criterio con más rigor: una frase de más de unas 15 palabras, o dos frases seguidas, que
  siguen al original término a término. Es la lección de método de esta campaña. Un lector que corrige reescribiendo
  tiende a aceptar como paráfrasis una traducción con alguna palabra cambiada; un lector que solo mide no.

**Lo que se corrige** (regla de 15.15: lo hallado y su vecindad, sin otra pasada completa):
1. **Lo hallado:** los 143 elementos de copia confirmados pasan por la máquina de siempre: reescritor, verificador ciego
   con dos trampas y tanda (ola h7). La invención, en `eficiencia_hidrica_edificios_2`, entra por corrección declarada
   ANADIDO (`docs/saneamiento/tandas/medida7-invencion.json`). El libro liga bajar la temperatura del agua caliente al
   ahorro de la energía que se gasta en calentarla, no al consumo de agua.
2. **La vecindad de los pasos** (mismo libro y mismo campo): los pasos de los 1.280 nodos vivos que comparten libro con
   un paso confirmado, en 13 libros. Son 86 lotes (V001 a V086) con trampa del mismo libro, y la vara de la medida va
   escrita en el encargo del lector.
3. **La vecindad de los resúmenes** abarca 2.154 nodos, prácticamente todos, porque los 38 resúmenes confirmados están
   repartidos entre 21 libros. Equivale a una segunda pasada completa, que la regla no permite. Queda declarada como
   pendiente en `docs/PROXIMOS_PASOS.md`, para que el fundador decida.

**Encargo del lector de la vecindad** (para que se reproduzca igual): `auditoria-final/copia/INSTRUCCIONES_LECTOR.md`
más esta vara, escrita en el encargo: *"una frase de más de unas 15 palabras, o dos frases seguidas, que siguen al
original término a término (traducido al español) es copia aunque cambie alguna palabra suelta; una paráfrasis de
verdad, con otra estructura y palabras propias, no lo es"*.
- Cada lote V lleva como trampa una traducción literal de otro pasaje del mismo libro, sacada de las trampas de los
  lotes P. Va como último elemento del lote, colgada de un nodo de ese libro.
- Los lectores la cazaron como copia y varios avisaron de que "no pertenece al nodo". Es la trampa, no un defecto del
  nodo.

### 15.17 Copia fiel: parada segura por cuota (7 oct 2026)

El fundador pidió parar de forma segura antes del 90 % de la cuota.

**Aplicado en main:** todo lo que el verificador ciego sostuvo. No queda ninguna corrección verificada sin aplicar.

| tanda | qué | correcciones aplicadas | no sostienen |
|---|---|---:|---:|
| h7 | lo hallado por la medida 7 | 137 | 6 |
| medida7-invencion | la invención confirmada | 1 | 0 |
| k29 | vecindad de pasos, lotes V001 a V026 | 72 | 5 |
| k30 | vecindad de pasos, 15 lotes con mucha copia (Primer Equipo) | 666 | 111 |

**Se paró a medias:**
- **Ola k31:** 1.915 propuestas de 32 lotes V ya leídos, empaquetadas para el verificador en 96 paquetes. No se
  verificó ninguna. Lo que el verificador no ha visto no se aplica, así que no entra ninguna.
- **Lotes V sin leer:** V063, V067, V075, V076, V078, V079 y V081 a V086. Sus lectores se pararon antes de escribir.
- **Retenidos:** 122 (6 de h7, 5 de k29 y 111 de k30), sin la reescritura r3.
- **Vecindad de los resúmenes:** pendiente de la decisión del fundador (15.16).

Los pasos para retomar están en `docs/PROXIMOS_PASOS.md`, sección 8.

**La copia fiel no queda certificada.** El residuo de copia en pasos baja con cada tanda de la vecindad, pero no se
volvió a medir. La medida 7 vale para el estado anterior a h7, k29 y k30.

### 15.18 Alto del fundador (8 oct 2026): el cierre del dataset queda para después

El fundador detuvo los agentes del dataset. Cuando llegó el alto acababa de terminar la primera oleada de verificadores
de la ola k31 (paquetes 01 a 20, todas las trampas cazadas). Esa oleada se terminó sin agentes: `tanda k31 parcial`
aplica solo las propuestas de los paquetes ya verificados, 347 correcciones en 48 nodos, con 53 que no sostienen.

Quedan para después:
- los paquetes 21 a 96 de k31;
- los 12 lotes V sin leer;
- la reescritura r3;
- la medida nueva.

El orden y el aviso sobre los ids de la segunda tanda de k31 están en `docs/PROXIMOS_PASOS.md`, sección 8. La copia
fiel sigue sin certificar.

### 15.19 Copia fiel: se retoma por guiones de la API (decisión del fundador, 10 oct 2026), escrito antes de lanzar

**Cambio de método.** Lo que queda (15.18) ya no lo hacen subagentes del entorno de desarrollo, sino guiones que
llaman a la API de Anthropic con la clave del `.env` (crédito promocional), con **Sonnet 5.5**:
`auditoria-final-claves/copia/api_copia.py`.
- **Las instrucciones son las mismas:** `INSTRUCCIONES_LECTOR.md` (con la vara de 15.16 en el encargo),
  `INSTRUCCIONES_VERIFICADOR.md` e `INSTRUCCIONES_REESCRITOR.md`, con los mismos ficheros de entrada y de salida que
  lee `copia.py`.
- **Las trampas son las mismas:** la de cada lote V y las dos de cada paquete del verificador.
- **El árbitro es Opus 5.5,** solo si hace falta: segunda lectura de un lote cuya trampa no cazó el primer lector, o
  relectura de una trampa del verificador que no se cazó.
- **Diferencia declarada:** el modelo no abre los libros con sus herramientas del entorno. El guion le da dos
  herramientas equivalentes que ejecuta él mismo sobre los ficheros de libro del elemento: buscar (como Grep, sin
  distinguir mayúsculas) y leer un tramo de líneas. Al verificador y al reescritor, además, les pone en el mensaje el
  pasaje que cita la evidencia del lector.

**Piloto, antes de lanzar (condición del fundador).** El guion verifica tres paquetes que ya verificaron los
subagentes (k31: 03, 09 y 15) y se comparan los veredictos. Se lanza solo si coinciden en lo esencial: las trampas
cazadas y el mismo veredicto en la gran mayoría de las propuestas. Si no, se para y se reporta.

**Orden y topes (visto del fundador):**

| Parte | Qué | Tope (USD) |
|---|---|---:|
| 1 | Paquetes 21 a 96 de k31, como ola **k31b** (los ids de tanda llevan `k31b` y no chocan con los de k31) | 8 |
| 2a | Lectura de los 12 lotes V sin leer | 10 |
| 2b | Verificación de lo que propongan (ola **k32**) | 4 |
| 3 | Reescritura **r3** de lo que no sostuvo desde k29, y su verificación | 7 |
| — | Árbitro, solo si hace falta | 2 |

Se deja una reserva de al menos 12 USD del crédito para la medición final del redactor.

**Cómo entra:** lo que sostiene el verificador entra por tandas declaradas (`docs/saneamiento/tandas/copia-<ola>.json`),
con Gate 0 y las suites en verde; lo que no, va a la reescritura r3. La copia fiel sigue sin certificar hasta la
medida nueva.

### 15.20 Copia fiel por la API: piloto y parte 1 (10 oct 2026)

**Piloto del verificador** sobre los paquetes 03, 09 y 15 de k31, que ya habían verificado los subagentes:
- primera pasada: trampas 6 de 6 y el mismo veredicto en 54 de 60 propuestas (90 %); tres veces el guion sostuvo un
  cambio de matiz que el subagente no sostuvo («puede ayudar» por «puedes», «con más tiempo» por «con más calma»);
- se añadió al encargo, una sola vez y para todo lo que sigue, la lista de matices que manda la propia instrucción
  («ante la duda sobre el sentido, no_sostiene»);
- segunda pasada: trampas 6 de 6 y 55 de 60 (92 %), con las cinco diferencias del lado estricto. Se lanzó.

**Piloto del lector** sobre el lote V050, que ya había leído un subagente: trampa cazada; el mismo veredicto en 106 de
118 elementos (90 %); 69 copias contra 73 del subagente (8 solo del subagente, 4 solo del guion).

**Parte 1, ola k31b** (paquetes 21 a 96 de k31): verificados 66 de 76 paquetes, con 132 de 132 trampas cazadas, antes
de llegar al tope (8 USD; gasto del guion 8,76, porque seis llamadas en curso terminaron después del tope). Quedan los
paquetes 67 a 76.
- **Tanda `copia-k31b` (parcial):** 1.086 correcciones en 169 nodos; Gate 0 y las dos suites en verde.
- **No sostienen: 234,** que van a la reescritura r3. Una de ellas la quitó la guarda de voz de cliente: la reescritura
  metía «el libro» en un paso (V046-027).

**Parte 2a, lectura de los 12 lotes V** (V063, V067, V075, V076, V078, V079 y V081 a V086): leídos por el guion con
Sonnet 5.5; cada lector cazó su trampa (814 de 814 lotes del plan leídos, sin segunda lectura ni árbitro). Gasto del
guion: 3,84 USD (tope 10).

**Parte 2b, ola k32:** 253 propuestas en 13 paquetes, verificadas a ciegas con 26 de 26 trampas cazadas (gasto del
guion 1,85 USD, tope 4). **Tanda `copia-k32`:** 200 correcciones en 70 nodos; Gate 0 y las dos suites en verde.
No sostienen 53, que van a la reescritura r3.
