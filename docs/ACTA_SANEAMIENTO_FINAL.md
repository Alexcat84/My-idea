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
| G5 | Títulos y autores fuera de lo que ve la persona | `engine/test_fuentes_de_cara.py`, `engine/test_fuentes_internas.py`, `web/lib/reglaSinFuentes.test.ts` |
| G6 | Voz de libro y de exposición | `web/lib/vozDeCliente.test.ts` (guarda de voz de cliente) sobre el grafo vivo y la caché |
| G7 | Rutas y marcas de auditoría | la misma guarda (regla `marcasInternas`) |
| G8 | Jurisdicción: toda entrada con país y clase | `engine/test_jurisdiccion.py` |
| G9 | Vigencia de las traducciones de etiquetas | la guardia de vigencia de etiquetas (i18n) |
| G10 | Nada interno en el navegador | `web/lib/assets/sinInternos.test.ts` |
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
