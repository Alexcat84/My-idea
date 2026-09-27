# Que campos de un nodo llegan a la IA o a la pantalla

Decision del fundador del 27 sep 2026, punto 2: medir, leyendo el codigo, que campos de un nodo llegan a la IA
(generador de preguntas, redactor de planes, cualquier prompt) o a la pantalla. Medido sobre main el 24 sep 2026
(commit 27adf7f2). La IA de produccion es la de `web/`; los generadores de `engine/` y `scripts/` corren fuera de
linea, pero lo que producen (preguntas y etiquetas) se sirve en pantalla.

Tres destinos:
- **IA**: el texto entra en un prompt.
- **Pantalla**: el texto se pinta tal cual.
- **Local**: solo se cuentan palabras en el servidor para ordenar candidatos; no llega a ningun prompt ni a la pantalla.

## Resultado: si llegan campos aparte de `pasos_accionables`

| campo | llega a | donde (fichero:linea) |
|---|---|---|
| `pasos_accionables` | IA y pantalla | IA: `web/lib/engine/planRedactor.ts:85` (material del plan, `aMaterial`), enviado en `web/app/api/session/[id]/plan/route.ts:118`. Pantalla: plan de respaldo sin conexion, `web/lib/engine/planRedactor.ts:510` |
| `resumen_teorico` | IA | `web/app/api/organizer/route.ts:72` y `web/app/api/organizer/stream/route.ts:114` (150 caracteres, organizador); `web/lib/engine/clasificar.ts:39` (200, clasificador); `web/lib/engine/puertaAvanzada.ts:100` (150, puerta avanzada); `engine/build_question_cache.py:92` (400, generador de preguntas, cuya salida se ve en pantalla); `scripts/generar_etiquetas_arbol.py:94` (220, generador de etiquetas, cuya salida se ve en pantalla) |
| `resumen_teorico` | Local | `web/lib/engine/planRedactor.ts:144`, `web/lib/engine/reeleccionPuerta.ts:68`, `web/lib/readiness.ts:66` |
| `entregable_esperado` | IA y pantalla | IA: `web/lib/engine/planRedactor.ts:86` (material del plan). Pantalla: plan de respaldo, `web/lib/engine/planRedactor.ts:511` ("Punto de control") |
| `condiciones_activacion` | IA | `web/lib/engine/graph.ts:307` (`resumenNodo`, al interprete, `web/lib/engine/interprete.ts:323-348`); `web/lib/engine/interprete.ts:341` (saltos posibles); `web/lib/engine/puertaAvanzada.ts:101`; `engine/build_question_cache.py:97` (candidatos del generador de preguntas) |
| `condiciones_activacion` | Local | `web/lib/engine/interprete.ts:249`, `web/lib/engine/planRedactor.ts:145` y `:165`, `web/lib/engine/puertaAvanzada.ts:51`, `web/lib/engine/reeleccionPuerta.ts:67` |
| `titulo_concepto` | IA y pantalla | IA: `web/app/api/organizer/route.ts:71`, `web/app/api/organizer/stream/route.ts:113`, `web/lib/engine/clasificar.ts:38`, `web/lib/engine/graph.ts:306`, `web/lib/engine/interprete.ts:339`, `web/lib/engine/planRedactor.ts:84`, `web/lib/engine/puertaAvanzada.ts:98`, `engine/build_question_cache.py:91` y `:96`, `scripts/generar_etiquetas_arbol.py:93`. Pantalla: pregunta generica `web/lib/engine/graph.ts:264`, opciones tras un error `web/lib/engine/recorrido.ts:571`, titulo de etapa del plan de respaldo `web/lib/engine/planRedactor.ts:509`, y respaldo de la etiqueta `web/lib/engine/graph.ts:174` |
| `etiqueta_arbol` | Pantalla | `web/lib/engine/graph.ts:174` y `web/lib/engine/recorrido.ts:231` (lo unico que viaja al cliente para nombrar un tema; `web/app/ui/ArbolPensante.tsx`) |
| `fase_proyecto` | IA (una etiqueta de fase, no texto del libro) | `web/app/api/organizer/route.ts:70`, `web/lib/engine/clasificar.ts:37`, `web/lib/engine/interprete.ts:340`, `web/lib/engine/puertaAvanzada.ts:99` |
| `fuente` | Nada | se declara en `web/lib/engine/graph.ts:24` y nada lo lee |
| `correcciones` | Nada | viaja dentro de `web/lib/assets/master_graph.json`, pero ningun codigo lo lee |

Derivados: la cache de preguntas (`web/lib/assets/preguntas_cache.json`) se pinta y se adapta en vivo; nace del
titulo, del resumen (400 caracteres) y de las condiciones de los candidatos. El indice semantico
(`web/lib/assets/semantic_index.json`) es un vector de titulo, resumen y condiciones: sirve para buscar vecinos y no
se muestra.

## Consecuencia

Llegan a la IA o a la pantalla, ademas de los pasos: **resumen, entregable, condiciones de activacion, titulo y
etiqueta de cara**. Por la decision del fundador se lanza una pasada contra la fuente solo sobre esos campos, con el
mismo metodo calibrado (trampas, verificador ciego, arbitro, cita literal), buscando unicamente CONTRARIOS y ANADIDOS
de cifra, plazo o norma. `fase_proyecto` queda fuera: es una etiqueta de la taxonomia de My Idea, no texto del libro.
