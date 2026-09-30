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
