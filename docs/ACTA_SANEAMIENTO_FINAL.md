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
