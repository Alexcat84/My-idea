# AUD-03 — Fase 2.6 a 2.9: cierre funcional del motor

**Estado: cerrado. Tag `motor-v2.0`.** Cada fase de este tramo nace de una
auditoría honesta de la anterior — el patrón de trabajo de todo este
período fue: correr la misma sesión real (macetas de calcita: resina + QR
+ NFT, fundador solo), auditar la transcripción con lupa, y corregir
exactamente lo que la evidencia mostró, nunca lo que "en teoría" podría
fallar. Evidencia completa (transcripciones + planes) en `examples/`.

---

## Fase 2.6 — preguntas adaptadas por turno, prompt caching real

**Motivación**: auditoría de Motor v1.0 encontró dos problemas reales sobre
la sesión de macetas: (1) nodos vecinos repetían la misma pregunta
disfrazada, incluyendo un nodo que preguntó por validar clientes cuando el
usuario ya había contado que sí validó (regaló prototipos, encantaron); (2)
un nodo tipo Stage-Gate le habló a un artesano solo en lenguaje de I+D
corporativo ("tu organización"). Causa raíz: las preguntas cacheadas eran
ciegas al contexto — generadas una vez por nodo, en aislamiento.

**Cambio**: el intérprete de turno devuelve `pregunta_adaptada` — reformula
la pregunta cacheada (que pasa a ser solo un "plano de intención", nunca
mostrada cruda) al registro del `perfil_sesion`, descontando lo ya
respondido y sin repetir la estructura de las últimas 2 preguntas.

**Hallazgo técnico separado**: `cache_read` daba 0 en las 9 llamadas Haiku
de la sesión auditada porque ambos system prompts estaban por debajo del
mínimo cacheable real (Haiku 4.5 necesita 4096 tokens, Sonnet 4.6 necesita
2048 — no 2048/1024 como se asumió al principio). Corregido ampliando los
prompts con ejemplos few-shot genuinos.

**Verificado** (`examples/fase2_6_macetas_con_cache.txt`): costo Haiku por
llamada bajó de $0.0078 (pre-fix) a $0.0047 (post-fix, ~40% menos) una vez
el caché realmente se activó (`cache_read`: 0 → 62,640 tokens). Cero
vocabulario corporativo en el plan final. Nota honesta registrada en su
momento: sobre 10 preguntas, un par (nodos 2 y 4) todavía comparte molde
retórico — mejora sobre la duplicación casi literal detectada antes, pero
no una eliminación perfecta.

## Fase 2.7 — escucha activa, cobertura del bloqueo declarado, caching incremental

**Motivación**: auditoría de 2.6 encontró que la entrevista "discutía" con
el usuario — tres veces seguidas dijo que su bloqueo era técnico (resina +
QR) y el sistema respondió con la misma plantilla ("Entiendo que X... pero
antes de eso, ¿ya validaste Y?"), desviando en vez de escuchar.
Consecuencia real en el plan: perdió la etapa de experimentos técnicos
concretos que sí tenía un plan de una fase anterior.

**Cambios**: (1) `prioridad_declarada` — si el usuario reafirma 2+ veces el
mismo bloqueo, prohibido desviar; la siguiente intervención debe
reconocerlo como frente legítimo. (2) La cosecha reserva hasta 8/25 cupos
para nodos afines al bloqueo declarado. (3) Memoria anti-plantillas
ampliada a las últimas 3 intervenciones (incluye repreguntas). (4) Tope
editorial: 5-7 etapas máximo. (5) Caching incremental de conversación
(`llamar_claude_conversacion`) — el intérprete deja de reenviar
`entrada_original`/perfil completo cada turno; además se corrigió un bug
real de contabilidad (`costo_acumulado_usd` ignoraba el precio de
`cache_read`/`cache_creation`, subestimando el costo real).

**Verificado** (`examples/fase2_7_macetas_escucha_activa.txt`, plan en
`fase2_7_plan_macetas.md`): cero apariciones de "pero antes" en toda la
transcripción; el plan dedica su Etapa 2 completa al método que el propio
usuario propuso (variar una variable a la vez), reconociéndolo por
nombre. `prioridad_declarada` final con `conteo: 3`. Costo $0.1842, dentro
del techo de $0.30.

## Fase 2.8 — navegación libre con brújula semántica, "sigamos" dirigido

**Motivación**: auditoría de 2.7 aprobada en 85% — el 15% pendiente era que
el motor navegaba "sobre un riel" (solo podía elegir entre sucesores a 2
niveles del nodo actual). Dos bugs adicionales detectados: la "promesa
rota del sigamos" (aceptar profundizar y generar el plan sin preguntar
nada nuevo) y una incoherencia etiqueta/contenido (un plan con costeo real
igual declaraba "no cubre viabilidad económica").

**Cambios**: (1) Brújula semántica — `engine/build_semantic_index.py`
genera embeddings locales (costo cero) de los 1265 nodos;
`buscar_afines()` ofrece hasta 8 "saltos posibles" de cualquier parte del
grafo cada turno. (2) "Sigamos" dirigido — usa la brújula para elegir 2-3
nodos reales de la familia faltante en vez de devolver el control al riel
local. (3) Coherencia por autodeclaración — el redactor declara él mismo
qué familias trató con sustancia real, en vez de que un clasificador por
keywords lo infiera.

**Dos bugs reales encontrados durante la propia verificación de esta
fase** (no solo el resultado final, el proceso de encontrarlos es parte
del registro): el modelo casi nunca saltaba (resuelto restringiendo
`repreguntar` a desambiguación pura + chequeo obligatorio de salto antes
de decidir); y `extender_sigamos_dirigido` comparaba claves cortas contra
frases largas y nunca encontraba candidatos (resuelto derivando las claves
correctas antes de llamar la función).

**Verificado** (`examples/fase2_8_macetas_navegacion_libre.txt`, plan en
`fase2_8_plan_macetas.md`): 3 saltos semánticos reales en la ruta, el más
notable — "cobro por pieza pero no he calculado bien cuánto me cuesta" →
salto directo a una Hoja de Estimación de Costos de otra rama del grafo
que ningún sucesor local ofrecía. Plan `_Plan completo_` coherente, sin
sección "no cubre". Costo $0.2746.

## Fase 2.9 — cierre del motor (tag `motor-v2.0`)

**Motivación**: auditoría de 2.8, turno por turno — lo esencial funcionaba,
pero con un bug real y un hallazgo de calidad: (1) dentro de la extensión
dirigida, el usuario dijo "dame mi plan" tres veces seguidas y el sistema
igual hizo dos preguntas más antes de generar el plan (la versión inversa
de la "promesa rota": preguntar de más ignorando la salida). (2) De los 3
saltos de la corrida 2.8, uno (`alfabetizacion_en_materiales_maliciosos`)
era temáticamente flojo pese a tener el score de afinidad MÁS ALTO del
grupo (0.409) — los saltos necesitaban permiso explícito para NO ocurrir.

**Cambios**: (1) `extender_sigamos_dirigido` pasa cada respuesta por
`_detectar_decision_plan` (clasificador real, `SYSTEM_PROFUNDIZAR`); al
primer "dame mi plan" dentro de la extensión, corta de inmediato. (2)
`MIN_SCORE_SALTO = 0.42` filtra candidatos débiles antes de ofrecerlos,
calibrado exactamente contra los 3 saltos de la corrida 2.8
(`hoja_estimacion_costos` 0.474 pasa; `alfabetizacion_en_materiales_
maliciosos` 0.409 queda excluido).

**Verificado**: el filtro de umbral confirmado directamente contra la
brújula real; el corte de intención dentro de la extensión verificado dos
veces — con mock (`engine/test_sigamos_salida.py`) **y con API real**
(`engine/live_tests/test_sigamos_salida_real.py`, costo $0.0021) — ambos
casos cortan exactamente donde deben, sin llegar a un tercer nodo. Corrida
completa (`examples/fase2_9_macetas_cierre_motor.txt`, plan en
`fase2_9_plan_macetas.md`): cero saltos de baja afinidad (de hecho cero
saltos en esa corrida particular — el umbral más estricto los redujo, tal
como se esperaba), plan `_Plan completo_` coherente, costo $0.2413.

**Límite de método reconocido en su momento**: las respuestas guionizadas
de estas 4 fases son las mismas de la corrida original de 2.6, pero las
preguntas ya evolucionaron tanto entre fases que varias parejas
pregunta-respuesta dejaron de corresponderse exactamente. El motor lo
manejó con gracia, pero la coherencia conversacional fina ya no se podía
verificar con guiones reciclados — la conclusión explícita en ese momento
fue que la siguiente validación real requería una sesión en vivo, sin
guion. Esa sesión se hizo después, en el hotfix v2.1.2 (ver
[AUD-04](AUD-04-Motor_v2_1_y_Hotfixes.md)).

Con esta fase, `prototipo_motor.py` quedó **funcionalmente completo** —
tag `motor-v2.0`. Desde aquí en adelante el archivo solo recibe fixes de
bugs; toda funcionalidad nueva va a la Fase 3 (el porte web), salvo el
complemento aditivo de Motor v2.1 (ver AUD-04).
