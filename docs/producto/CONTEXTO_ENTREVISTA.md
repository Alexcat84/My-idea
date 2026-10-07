# El contexto del usuario en la entrevista: diagnóstico y propuesta (28 sep 2026)

Encargo del fundador con el auditor, 28 sep 2026, tras el vuelo del mundo 11. El fallo de "tu propio jefe" no es del
dataset ni del mundo 11: es de prompts y de secuencia, y afecta a todos los mundos. Principio que manda sobre todo lo
de aquí: `docs/REGLAS_DE_LA_CASA.md`, regla 1 (las preguntas de la caché son preguntas base, no ley).

- **Fase 1, diagnóstico:** solo lectura del código de `web/` en la rama `puente-forja` (commit `78b125ec`), con citas
  `ruta:línea`, y de la corrida real exportada en `docs/vuelos/2026-09-28_mundo11/`.
- **Fase 2, propuesta:** **sin construir hasta el visto del fundador.**

Nota de honestidad: el commit `78b125ec` (28 sep, antes de esta reorientación) ya metió medidas parciales: la
prioridad en la búsqueda de saltos y en el respaldo, las reglas "ELEGIR CON LA PRIORIDAD" y "ROLES DE EMPRESA GRANDE"
en los prompts, y una guarda de las preguntas del mundo 11. Quedan descritas donde tocan. La fase 2 las absorbe o las
sustituye; ninguna se da por solución.

---

## FASE 1. Diagnóstico

### 1. Qué recibe cada llamada a la IA

Hay **18 llamadas** a un modelo en el viaje del usuario. Todas pasan por `llamarClaude` (`web/lib/costmeter.ts:180-208`)
salvo el intérprete, que usa `llamarClaudeConversacion` (`costmeter.ts:236-296`), y dos streams directos (organizador
y redactor del plan). Topes de entrada: la idea hasta 12.000 caracteres (`web/lib/constants.ts:23`); cada respuesta,
seguimiento o historia hasta 4.000 (`constants.ts:10`).

| # | Llamada | Cuándo | Modelo, tope de salida | Contexto del usuario que recibe | Recortes |
|---|---|---|---|---|---|
| 1 | Organizador | al pegar la idea | Haiku, 1500 | la idea entera + las puertas | resumen de puerta a 150 |
| 2 | Clasificación | inicio de sesión del núcleo | Haiku, 400 | la idea entera + las puertas | resumen a 200 |
| 3 | Consulta al español (brújula) | cada salto, idea no española | Haiku, 400 | respuesta + prioridad; en el turno 1, la idea entera | **salida a 400 tokens sin aviso** |
| 4 | **Intérprete** | cada turno y cada salto | Haiku, 700 | turno 1: idea, perfil, nodo, sucesores, saltos, respuesta, prioridad. **Desde el turno 2: sin idea ni perfil**, más el historial | ver abajo |
| 5 | Traducir pregunta | fin de turno, idea no española | Haiku, 200 | **solo la pregunta** | — |
| 6 | Profundizar | oferta del plan | Haiku, 100 | solo la respuesta | — |
| 7 | Pregunta dirigida | "seguimos explorando" | Haiku, 150 | perfil + pregunta base + 3 últimas preguntas | — |
| 8 | Anclaje de protección | turno en los 3 mundos de protección | Sonnet, 300 | actividades del núcleo + pregunta (**sin estado vivo**) | salida ≤ 400 caracteres |
| 9 | Redactor del plan | al pedir plan | Sonnet, 5000 | idea, perfil, material, prioridad; en seguimiento, estado vivo y plan anterior | **sin las respuestas del usuario**; contexto final a 2000 |
| 10 | Estado vivo | al entregar un plan | Haiku, 700 | estado vivo anterior + perfil + títulos cubiertos (**sin la idea**) | **salida a 700 tokens sin aviso** |
| 11 | Estimación de banda (×3) | al entregar un plan | Sonnet | solo el texto de las tareas | tareas a 180 |
| 12 | Enlace de protección | plan de mundo de protección | Sonnet | actividades + tareas | tareas a 180 |
| 13 | Juez de sesión | al entregar un plan | Haiku, 400 | decisiones de cada turno, con las respuestas | — |
| 14 | Puerta avanzada | seguimiento | Haiku, 400 | estado vivo + mensaje de seguimiento | candidatos 30 |
| 15 | Caminos (replantear) | replantear | Sonnet, 1200 | historia, plan anterior, realidad, estado vivo | candidatos 30 |
| 16 | Diagnóstico de mundo | fin del preview | Sonnet, 700 | estado vivo, temas, perfil | salida a 700 sin aviso |
| 17 | Clasificar oferta | reporte | Haiku, 150 | solo la respuesta | — |
| 18 | Narrar reporte | reporte | Sonnet, 1800 | solo los números | — |

**Lo que importa para "tu propio jefe":**

- **El intérprete no ve quién es la persona después del primer turno.** Desde el turno 2, `ctxTurno` quita
  `entrada_original` y `perfil_sesion` (`web/lib/engine/interprete.ts:397-400`). Solo los ve en el primer mensaje del
  historial.
- **El perfil actualizado no se le reenvía nunca.** Lo que el propio intérprete aprendió en cada turno (`perfil_update`,
  sumado en `web/lib/engine/recorrido.ts:687-692`) no le llega en los turnos siguientes.
- **Si la persona dijo "soy dueña, tengo dos empleados" en el turno 2, esa frase solo vive en el historial crudo**, sin
  estructura y sin nada que le obligue a mirarla al redactar la pregunta del turno 5.
- **El historial de la conversación no tiene tope** (`costmeter.ts:275`, `:289-293`): crece en cada llamada.
- **No existe en ningún sitio un dato estructurado del papel de la persona** (dueña, empleada, directiva), del tamaño
  de su equipo, de su sector ni de su etapa. Todo es prosa: la idea, el perfil acumulado y el estado vivo.
- **Las llamadas 5 (traducir), 6, 7, 17 y 18 no reciben ni la idea ni el estado vivo.** La 5 es la que pone la pregunta
  base en otro idioma: la traduce sin saber nada de la persona.

**Por qué "el estado vivo aparece cortado a mitad de frase".** Lo medí en la corrida, y **el estado vivo no está
cortado**:

- Sus copias miden entre 1.548 y 2.002 caracteres (unos 500 tokens), todas terminan en frase completa, y ninguna llega
  al tope de 700 tokens. La del final, en `docs/vuelos/2026-09-28_mundo11/proyecto.md`, mide 1.845 caracteres y
  termina en "...correctible antes del desastre.".
- **Lo que sí sale cortado a mitad de palabra son las tareas del checklist.** Al derivar el checklist del plan, cada
  tarea toma la primera oración del paso y, si pasa de 180 caracteres, se queda en 177 más "…"
  (`web/lib/engine/checklist.ts:34`). En la corrida, 74 de 239 tareas; por ejemplo, "...aditivos o resinas sin ficha
  de segu…".
- **Esas tareas cortadas viajan después a:**
  - el mensaje de cada seguimiento, que es la "entrada original" del intérprete y del redactor en esa sesión
    (`web/lib/engine/seguimientoComposer.ts:88`);
  - el plan anterior que recibe el redactor;
  - la estimación de bandas y el enlace de protección;
  - la foto del núcleo de los mundos de protección.
- Las tareas retiradas se cortan a 70 caracteres en el bloque de realidad (`web/lib/engine/bloqueRealidad.ts:19`).
- Por eso el texto de contexto de los seguimientos se lee cortado. Es probable que lo cortado que vio el auditor fuera
  eso, no el estado vivo.

**Riesgo latente real:** `llamarClaude` no mira nunca si el modelo se quedó sin tokens (`stop_reason`). Si un estado
vivo, un diagnóstico o una traducción larga llegaran al tope, se guardarían cortados sin aviso. No pasó en este vuelo.

### 2. Cuándo se muestra una pregunta de la caché SIN adaptar, y en qué idiomas

La caché guarda cada pregunta **en español**. `obtenerPregunta` la devuelve tal cual
(`web/lib/engine/graph.ts:267-280`). Si el nodo no tiene pregunta, devuelve una plantilla genérica con la etiqueta del
nodo, en 11 idiomas (`web/lib/i18n/mensajes/motor.ts`).

| Camino | ¿Sin adaptar? | En español | En otros idiomas |
|---|---|---|---|
| **Primera pregunta al entrar a cualquier mundo** (`world/[pack]/start/route.ts:283-288`) | **SÍ, siempre, por diseño** (cero modelo) | cruda; en los 3 de protección se ancla a una actividad del plan, y si no encaja, cruda | un modelo la **traduce sin adaptarla** (`SYSTEM_TRADUCIR_PREGUNTA`: "la misma intención, no agregues ni quites nada"); si falla, sale en español |
| **Re-elección de puerta** en un mundo (el intérprete decide salir, o el nodo no tiene siguientes) (`recorrido.ts:602-633`, `:733-755`) | **SÍ** | cruda | traducida sin adaptar |
| **Respaldo tras dos respuestas inválidas del modelo** (`interprete.ts:559-588`) | **SÍ** | cruda | traducida sin adaptar |
| **Falla la pregunta dirigida** ("seguimos explorando") (`recorrido.ts:374-376`) | SÍ | cruda | traducida sin adaptar |
| **El intérprete copia la pregunta base literal**, aunque el prompt lo prohíbe | SÍ, de hecho | cruda | traducida sin adaptar |
| **Nodo sin pregunta en caché** | plantilla genérica | en el idioma de la idea | sin traducir ni adaptar |
| Inicio del núcleo, seguimiento, salto, repregunta | **NO**: las redacta el intérprete (`pregunta_adaptada`) | adaptada | adaptada |

**Cuánto pasa:**

- **Cada vez que alguien entra a un mundo, la primera pregunta es la base cruda.** Es el camino más frecuente.
- **Hay 347 nodos activos sin pregunta en caché.** 307 son hojas y no la necesitan. **40 tienen siguientes y les falta**,
  así que en esos saldría la plantilla genérica.
- **La pregunta base del mundo 11 que habló de "tu propio jefe"** era de la caché
  (`responder_primer_aviso_renuncia_subordinado`): el turno 6 del vuelo la muestra idéntica, carácter a carácter. Es
  decir, el intérprete la copió literal.
- **Esa pregunta base la regeneró la integración del mundo 11**, y la verificación ciega de preguntas de puerta la dio
  por adecuada. Aquel verificador miraba si la pregunta partía de la situación del nodo y servía para elegir, pero **no
  miraba los roles supuestos**. La prueba de coherencia de la fase 2 (E) cubre ese hueco.
- **Y aunque el intérprete adapte, lo hace sin el perfil actualizado** (punto 1).

### 3. Cuánto pesa la prioridad declarada al elegir el siguiente nodo

La prioridad la detecta y la cuenta solo el modelo (`interprete.ts:441-446`). Un null no la borra
(`recorrido.ts:693-695`).

- **Antes de `78b125ec`:**
  - Nada determinista.
  - En el prompt, una sola frase: ponderar los candidatos afines a la prioridad "por encima de otros de afinidad
    similar, una vez el conteo llega a 2 o más". Era un desempate, y solo con dos reafirmaciones.
  - En el vuelo, la prioridad se declaró en el turno 2 y cambió en el 5: nunca pasó de conteo 1, así que no pesó nada.
  - El paso a "Sigue los cuatro pasos al contratar" fue un siguiente local elegido sin mirarla.
- **Después de `78b125ec`:**
  - La búsqueda de saltos consulta respuesta más prioridad, lo que cambia qué 8 saltos se ofrecen
    (`interprete.ts:250-252`, `:358-363`).
  - El respaldo sin modelo suma los tokens de la prioridad (`interprete.ts:257-284`).
  - El prompt manda preferir el candidato que la atiende desde conteo 1.
- **Sigue sin ser una regla dura:**
  - `validarCamino` acepta cualquier siguiente estructuralmente válido (`interprete.ts:212-244`).
  - La re-elección de puerta, la extensión dirigida y la puerta avanzada del seguimiento no la miran.
  - Ningún código impide avanzar a un tema ajeno a la prioridad.

---

## FASE 2. Propuesta (sin construir hasta el visto del fundador)

### A. La ficha de contexto del usuario

Un objeto estructurado, no prosa, que viaja completo a **toda** llamada a la IA:

```json
{
  "papel": "duena | empleada | directiva | desconocido",
  "tiene_jefe": false,
  "equipo": { "personas": 2, "desde": "recien contratadas" },
  "sector": "taller de macetas de cemento",
  "etapa": "ideacion | validacion | planificacion | ejecucion",
  "prioridad_declarada": { "texto": "dirigir a mis dos empleados", "conteo": 2 },
  "idioma": "es",
  "dijo_textual": ["termino haciendo yo el trabajo", "les hablo solo cuando hay un problema"]
}
```

- **Se llena desde la primera respuesta:** en el núcleo, con la clasificación; en un mundo o un seguimiento, desde la
  ficha guardada del proyecto.
- **Se actualiza cada turno dentro de la llamada del intérprete**, que ya devuelve `perfil_update` y
  `prioridad_declarada`: un campo más en su salida, sin llamada nueva.
- **Un dato desconocido se queda en `desconocido`**, nunca se inventa.
- **Se guarda en el proyecto**, para que el siguiente mundo o seguimiento arranque sabiendo quién es la persona.
- **Viaja completa en cada turno** y deja de depender del primer mensaje del historial (corrige
  `interprete.ts:397-400`). El historial se recorta a los últimos N turnos, porque la ficha lleva lo que importa.

### B. Ninguna pregunta de la caché se muestra cruda

- **Toda pregunta que va a salir de la caché** pasa por un adaptador con un modelo pequeño (Haiku), que recibe la
  pregunta base, la ficha y el nodo. Son los cinco caminos de la tabla: entrada a un mundo, re-elección, respaldo,
  pregunta dirigida fallida y copia literal. Devuelve la pregunta adaptada **y una línea que diga qué busca**, para
  comprobar que busca lo mismo que la base.
- **La misma llamada sustituye a la de traducir:** adapta y escribe en el idioma de la idea a la vez.
- **Salida segura** si el adaptador falla, tarda o devuelve algo que no pasa las comprobaciones: una **versión neutral**
  de la base, sin roles supuestos. Se genera una vez por nodo y se guarda en la caché, junto a la base, con el mismo
  generador y la regla de la casa. Nunca la base cruda.
- **Los 40 nodos con siguientes y sin pregunta** reciben la suya (base y neutral).
- **Coste estimado por turno, con cifras del vuelo:**
  - El intérprete cuesta hoy **0,0099 USD por turno** de media (39 turnos).
  - El adaptador: unos 500 tokens de entrada sin caché, 600 de prompt en caché y 80 de salida en Haiku (1 USD entrada y
    5 USD salida por millón; caché al 10 %). Son 0,0005 + 0,00006 + 0,0004, unos **0,001 USD por pregunta adaptada**.
  - Solo corre cuando la pregunta sale de la caché. Aunque corriera en todos los turnos, serían **~10 % más por turno y
    entre 2 y 5 % más por sesión** (una sesión completa cuesta hoy entre 0,17 y 0,30 USD).
  - La ficha sale gratis dentro del intérprete (unos 100 tokens de salida, ~0,0005 USD por turno).
  - Las versiones neutrales son un coste de una sola vez: unas 3.300 preguntas por unos 0,0015 USD, **unos 5 USD**.

### C. Regla fija en todos los prompts

- **Una sola regla, escrita una vez y añadida a todos los prompts** que redactan algo para la persona, igual que ya se
  añaden la regla sin fuentes y la de idioma (`web/lib/i18n/idiomaSalida.ts:41-53`): intérprete, pregunta dirigida,
  adaptador, redactor del plan, estado vivo, diagnóstico, caminos y generador de la caché.
- **Contenido:** no suponer roles ni estructuras que la persona no mencionó. Si el nodo supone un jefe y la ficha dice
  dueña, se adapta; si no se puede adaptar sin cambiar el fondo, el nodo se salta.
- **Sustituye a las dos reglas sueltas** de `78b125ec`.
- **Saltar un nodo sin traicionar el camino** se hace con una marca en el nodo: `supone: ["jefe"]`, medida con un
  lector y verificada a ciegas, como las aristas. Si la ficha la contradice, el nodo no se ofrece como siguiente ni como
  puerta. Es un filtro en `esOfrecible`, la puerta única de la casa (`web/lib/engine/graph.ts:227-250`).

### D. La prioridad declarada manda

- **Cada candidato** (siguientes, saltos, puertas de re-elección) se puntúa en código por su parecido con la prioridad.
  Se usa el mismo índice semántico; solo hay que embeber el texto de la prioridad cuando cambia, a unos 0,0000002 USD.
- **Regla dura en `validarCamino`:** si hay prioridad y existe un candidato que la atiende (parecido por encima de un
  umbral), el intérprete no puede elegir uno que no la atienda. Si lo hace, reintento con el motivo.
- **Si ningún candidato la atiende**, sigue el camino local y la pregunta lo dice.
- **Se aplica también a la re-elección de puerta y a la puerta avanzada del seguimiento.**
- **Solo la cambia el usuario:** la ficha la cambia cuando la persona declara otra.

### E. Prueba de coherencia en todos los mundos

- **Tres usuarios sintéticos**, cada uno con su ficha y su guion de respuestas coherente con ella:
  1. fundadora sola;
  2. fundador con dos empleados;
  3. empleado de una empresa mediana, con jefe y recursos humanos.
- **Recorren el núcleo y los 11 mundos:** 36 recorridos, hasta la oferta del plan, sin generar planes.
- **Un juez ciego** (Sonnet) lee cada pregunta mostrada, la ficha y la pregunta base, y cuenta dos cosas:
  - **desajustes de papel o contexto**: supone jefe a una dueña, supone equipo a quien está sola, habla de una empresa
    grande sin que la haya;
  - **fidelidad**: si la adaptada busca lo mismo que la base, es decir, si su respuesta serviría para elegir entre los
    mismos siguientes.
- **Trampas sin marca:** preguntas adaptadas con un desajuste plantado a mano, para medir que el juez las caza.
- **Umbral propuesto, a fijar por el fundador ANTES de medir:**
  - 0 desajustes de papel (suponer un jefe, recursos humanos o equipo que la ficha contradice);
  - como mucho 1 desajuste de contexto por cada 10 preguntas;
  - al menos el 95 % de las adaptadas fieles a su base;
  - el juez caza todas las trampas.
- **Coste estimado:** 36 recorridos de ~6 turnos a ~0,012 USD por turno (con el adaptador), más el juez. **Unos 3 a 5
  USD por medición completa.** Se repite en la auditoría final.

### Orden propuesto, cuando haya visto

1. La regla fija en todos los prompts (C) y la ficha (A), con sus pruebas en rojo primero.
2. El adaptador con salida segura (B) y las versiones neutrales.
3. La prioridad en código (D).
4. La prueba de coherencia (E) con el umbral fijado antes.
5. Aparte, el aviso cuando una llamada se queda sin tokens (`stop_reason`), y que las tareas del checklist no se corten
   a mitad de palabra.

---

## FASE 3. Lo construido (rama `contexto-entrevista`, con el visto del 28 sep 2026)

Cada bloque entró con sus pruebas en rojo primero y las dos suites, tsc y el guardián en verde. **Ninguna llamada a la
API real** desde la regla del fundador del 28 sep 2026: todo se verificó con clientes simulados, y lo que necesita la
IA queda preparado para la corrida final.

| Bloque | Commit | Qué entra |
|---|---|---|
| 1 | `fdd7f389` | Contabilidad del caché (escritura 1 h y 5 min, lectura) por llamada; `costo_usd` con sus tarifas; toda llamada mira el corte por tokens, reintenta con el doble y, si vuelve a cortarse, falla con aviso; regla única en el prefijo fijo |
| 2 | `f183fc32` | Las tareas del checklist se guardan completas; solo se acortan al mostrarlas |
| 3 | `d5fcb898` | Memoria del proyecto (`projects.memoria`, migración 049, aplicada en producción el 28 sep 2026): ficha e hilo; el intérprete actualiza la ficha en su misma llamada; cada sesión abre con la foto del proyecto |
| 4 | `b94a8328` | El contexto completo viaja a toda llamada a la IA con un proyecto detrás (el organizador, la primera de todas, solo tiene el texto de la idea, que ya recibe) |
| 5 | `bcfb19ed` | El adaptador de preguntas y el generador que solo añade |
| 6 | `ecd08a01` | La prioridad declarada, regla en código |
| 7 | este | Reglas de la casa 2 a 5 y el criterio de papeles en el juez de sesión |

**Lo que cambió respecto a la propuesta de la FASE 2:**

- **C, "si no se puede adaptar, el nodo se salta": retirado.** El Principio 2 lo prohíbe: ningún nodo se salta por el
  papel de la persona, todos se adaptan. No hay marca `supone` ni filtro en `esOfrecible`.
- **B, las 199 preguntas en voseo: no se regeneran.** El adaptador las dice en tuteo neutro al momento, y su versión
  neutral también. Las bases no se tocan.
- **B, la salida segura antes de la corrida final.** Las versiones neutrales y las preguntas de los 40 nodos se generan
  en la corrida final (`engine/build_question_cache.py --faltantes` y `--neutrales`). Hasta entonces, si el adaptador
  falla y el nodo no tiene su neutral, sale una **plantilla neutral genérica sin roles supuestos**, nunca la base
  cruda (visto del fundador del 28 sep 2026, punto 1). Es la genérica que nombra el tema por su etiqueta; si la
  etiqueta supone un papel (100 de las 3.169 vivas, como "Alinea a tu Equipo con el Mapa"), es la que no nombra tema.
  El evento dice cuál salió (`plantilla_neutral`). La prueba `cacheNeutrales.test.ts` guarda la cifra (2.940 bases
  vivas sin neutral, 40 nodos sin pregunta): solo puede bajar.
- **B, el adaptador también cubre la genérica** de un nodo sin pregunta, y corre en español, no solo fuera: la base ya
  no sale cruda en ningún idioma. Tarda como mucho 8 segundos antes de dar paso a la salida segura.
- **D, la medida de "atiende la prioridad"** es el coseno contra la prioridad en el mismo índice semántico, con el umbral
  ya calibrado de la brújula (0,30). La prioridad se embebe una vez por texto. Si el modelo elige un destino que no la
  atiende sin `paso_previo`, se le pide otra vez con el motivo; si insiste, el respaldo elige el que mejor la atiende.
  La prioridad pasa de una sesión a la siguiente desde la ficha.
- **A, "el historial se recorta a los últimos N turnos": no se hizo.** El historial crece por el final para que el caché
  acierte (regla de la casa 4); recortarlo cambiaría el prefijo en cada turno. Se revisará con los costes de la
  corrida final.

**Lo que falta:** la prueba de coherencia (E), con el umbral ya fijado por el fundador (0 desajustes de papel, como
mucho 1 de contexto por cada 10 preguntas, al menos el 95 % de las adaptadas fieles a su base, todas las trampas
cazadas), y la corrida final entera.

---

## Lo que sigue en pie en paralelo

- **`.env`:** el fundador lo retira. No se ha vuelto a usar la clave desde su decisión. El **vuelo completo** (todas las
  fases, incluidas de la 2L en adelante, que no corren enteras desde el 9 de septiembre) pasa a la auditoría final, con
  créditos sembrados.
- **Costes a $0:** explicado y corregido en `78b125ec`.
  - Las sesiones de exportación y franquicias cuestan 0 de verdad: el vuelo solo las abre, y la primera pregunta sale
    de la caché sin modelo.
  - Los dos seguimientos sí gastaron (~0,017 USD cada uno), pero la sesión solo escribía el coste al cerrarse. Ahora
    cada turno guarda el coste y su desglose (`web/lib/db.ts`, `guardarEstadoSesion`, con prueba).
- **`mundo_activar`:** el cliente no lo ve. No hay pantalla ni descarga de su historial de créditos, y al borrar la
  cuenta se anonimiza. Queda la ficha `historial-creditos-rotulos` en `docs/PENDIENTES.md`: el día que exista ese
  historial, dirá "Plan del mundo", y el diagnóstico nunca aparecerá como cobro.
