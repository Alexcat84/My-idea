# Motor v1.0 — prueba de dos actos, limpia (contra Supabase real)

Caso: la app de navegación por sonar para personas ciegas. Corrida en vivo
contra el proyecto Supabase real (no `--offline`), con las credenciales de
`.env` y el usuario fijo de desarrollo creado por `scripts/setup_dev_user.py`.

Esta es la corrida **posterior al cierre de Fase 2** (cierre elegante +
auto-corrección invisible). A diferencia de la corrida anterior de Fase 2.5
(que quedó documentada en el historial de commits, no en estos archivos),
**ninguna de las tres transcripciones de abajo contiene un traceback o un
menú numerado visible** — verificado con `grep -c Traceback` sobre cada
archivo (resultado: 0 en los tres).

## Acto 1a — `acto1a_gratis.txt`

`--gratis`: una sola llamada Haiku, organiza la idea sin instruir.
Verificado a mano: cero verbos imperativos en las cuatro secciones de
salida (todo descriptivo: "existe un problema...", "la solución
utiliza...", nunca "haz esto"). Guardado en Supabase como
`plans.etiqueta = 'organizador'`, `conceptos_usados = 0`.

## Acto 1b — `acto1b_sesion_completa.txt`

Sesión completa (proyecto nuevo), misma entrada, hasta el plan — **en un
solo pase, sin interrupciones**. 13 llamadas a Haiku para una ruta de 12
nodos (varias más de las estrictamente necesarias: el intérprete tropezó
internamente más de una vez, pero la auto-corrección lo resolvió sin que
el usuario viera nada — ni error, ni menú, ni pausa rara).

Resultado: `_Plan completo_`, 37 conceptos (12 de ruta + 25 de cosecha),
`familias_cubiertas = ['accion_clientes', 'viabilidad_economica']` en
Supabase — coherente porque ambas familias SÍ fueron tocadas.

## Acto 2 — `acto2_seguir.txt`

**`--seguir PROJECT_ID`** con el mensaje de campo: 40% de confusión de
usuarios con ruido urbano de fondo, dos instituciones interesadas en
pilotear, costo real de fabricación de $600–900 por sensor, y voluntad de
construir un sistema robusto en vez de otro prototipo desechable —
seguido de dos turnos más de profundización.

Verificado:

- **Entrada por nodo avanzado**: aterrizó en "Etapa 4: Pruebas y
  Validación" — no es una de las 20 puertas curadas, confirma que
  `--seguir` elige de todo el grafo, no solo las puertas de entrada.
- **Cero nodos repetidos del proyecto**: `project_nodes` en Supabase —
  44 filas totales entre las dos sesiones del proyecto, 44 `node_id`
  únicos, cero solapamiento (37 de la sesión inicial + 7 de esta).
- **Coherencia etiqueta/cobertura**: esta sesión de seguimiento no volvió
  a tocar `accion_clientes` (el mensaje se centró en costos e iteración
  técnica), y el plan lo declara honestamente en "Lo que este plan aún no
  cubre" — `plans.etiqueta = 'seguimiento'`,
  `familias_cubiertas = ['viabilidad_economica']` en Supabase, sin
  contradicción entre lo que dice el plan y lo que realmente contiene.
- **Cero tracebacks ni menús visibles** en las 5 respuestas de esta
  sesión, pese a que internamente el intérprete tropezó al menos una vez
  (ver `fallback_events` en `engine/sessions/*.json` de corridas previas
  de esta misma prueba, donde sí quedó registrado un evento
  `fallback_auto`).

## Costo real reportado

| Sesión | Modelo(s) | Costo |
|---|---|---|
| Acto 1a (`--gratis`) | Haiku | $0.0042 |
| Acto 1b (sesión completa, proyecto nuevo, en un solo pase) | Haiku + Sonnet | $0.1489 |
| Acto 2 (`--seguir`, 5 turnos hasta el plan, en un solo pase) | Haiku + Sonnet | $0.0791 |

## Fase 2.6 — preguntas adaptadas por turno, prompt caching real

Auditoria posterior a motor-v1.0: dos hallazgos sobre la sesion real de las
macetas de calcita (resina + QR + NFT). (1) Redundancia: nodos vecinos
hacian la misma pregunta con otro disfraz, y un nodo pregunto por validar
clientes cuando el usuario ya habia contado que regalo prototipos y le
encantaron a la gente ("eso ya lo valide"). (2) Tecnicismo: el nodo tipo
Stage-Gate-TD pregunto en lenguaje de I+D corporativo ("tu organizacion")
a un artesano solo. Causa raiz unica: las preguntas cacheadas son ciegas al
contexto (se generaron una vez por nodo, en aislamiento). Ademas, un hallazgo
tecnico separado: `cache_read` era 0 en las 9 llamadas Haiku de esa sesion
porque ambos system prompts (interprete y redactor) estaban por debajo del
minimo cacheable de sus modelos (Haiku 4.5 necesita 4096 tokens, Sonnet 4.6
necesita 2048 — no 2048/1024 como se penso al principio).

Cambios: el interprete de turno (que ya corria en cada paso) ahora tambien
devuelve `pregunta_adaptada`: reformula la pregunta cacheada (que pasa a ser
solo un "plano de intencion", nunca mostrada cruda) al registro del
perfil_sesion (prohibido vocabulario corporativo para un fundador
solitario), descontando lo ya respondido (si no queda nada nuevo, el nodo se
marca silencioso) y sin repetir la estructura de las ultimas 2 preguntas
hechas. El ruteo tambien penaliza candidatos que presuponen estructura
organizacional cuando el perfil es una persona sola. Los system prompts del
interprete y del redactor se ampliaron con ejemplos genuinos (few-shot) que
de paso los llevan por encima del minimo cacheable real de cada modelo.
Cosmetico: al repreguntar ya no se reimprime el encabezado del nodo.

Verificado con dos corridas reales de la misma sesion de macetas (mismo
`entrada_original` literal, mismas respuestas guionizadas realistas basadas
en el perfil_sesion original), la primera con los prompts aun cortos (antes
de corregir el umbral) y la segunda ya con los prompts ampliados:

| Corrida | Llamadas Haiku | cache_read Haiku | Costo Haiku | Costo Sonnet | Total |
|---|---|---|---|---|---|
| `fase2_6_macetas_con_cache.txt` (post-fix) | 18 | 62,640 tokens | $0.0842 | $0.1280 | $0.2122 |
| (pre-fix, mismo harness, sin guardar transcript) | 14 | 0 | $0.1091 | $0.1177 | $0.2268 |

Costo Haiku por llamada: $0.0078 (pre-fix) -> $0.0047 (post-fix), una baja
del ~40%, tal como se esperaba una vez el cache realmente activa. El total
de la sesion no es directamente comparable al $0.1445 que reporto el
usuario en su sesion real original (esa sesion tuvo otra profundidad de
ruta y no quedo transcripcion guardada para repetir el guion exacto), pero
la mecanica de cache ahora aplica igual a cualquier sesion en vivo.

Verificado en la transcripcion (`fase2_6_macetas_con_cache.txt`): cero
vocabulario corporativo en las preguntas generadas o en el plan final (grep
de organizacion/portafolio/unidad de negocio/comite/stakeholders da cero
coincidencias reales), los nodos de validacion con clientes se marcaron
silenciosos 4 veces porque el usuario ya habia contado que regalo
prototipos y le encantaron ("cubierto por lo que ya contaste"), y ningun
encabezado de nodo se reimprime al repreguntar. Nota honesta: sobre 10
preguntas conversadas en esta corrida, una pareja (nodos 2 y 4) comparte el
molde "¿que es lo que mas te preocupa/duda: A, o B?" aunque el contenido de
fondo difiere en cada una — mejor que la duplicacion casi literal que
detecto la auditoria original, pero no una eliminacion perfecta de
plantillas repetidas.

## Fase 2.7 — escucha activa, cobertura del bloqueo declarado, caching incremental

Auditoria de la Fase 2.6: el plan de macetas era bueno pero la entrevista
"discutia" con el usuario — tres veces seguidas el usuario dijo que su
bloqueo era tecnico (resina + QR) y el sistema respondio con la misma
plantilla ("Entiendo que X... pero antes de eso, ¿ya validaste Y?"),
desviando la conversacion en vez de escucharla. Consecuencia directa en el
plan: perdio la etapa de experimentos tecnicos concretos que si tenia el
plan de Fase 2.4, y le exigia al usuario vender macetas reales sin haberle
dado como fabricarlas sin defectos. Ademas, la plantilla repetida
"Entiendo que X, pero antes de Y" aparecia 4 veces en las repreguntas
(la memoria anti-repeticion solo miraba las ultimas 2 preguntas
principales, no las repreguntas).

Cambios: (1) `prioridad_declarada` — el interprete rastrea si el usuario
reafirma 2+ veces el mismo bloqueo; a partir de ahi, prohibido desviar:
la siguiente intervencion debe reconocer esa prioridad como frente
legitimo y, si sugiere validar algo mas, presentarlo como complemento en
paralelo ("mientras...", "en paralelo..."), nunca como sustituto. (2) La
cosecha reserva hasta 8/25 cupos para nodos afines al bloqueo declarado, y
el redactor recibe `bloqueo_declarado` con instruccion dura de darle
tratamiento explicito — si el usuario propuso su propio metodo (p.ej.
"variar una variable a la vez"), reconocerlo por nombre y estructurarlo
con pasos concretos, y de revisar dependencias (ninguna etapa puede pedir
un insumo que el plan no ayudo a producir antes). (3) La memoria
anti-plantillas se amplio a las ultimas 3 intervenciones (incluye
repreguntas), con las dos plantillas reincidentes nombradas
explicitamente. (4) Tope editorial: 5-7 etapas maximo, fusionar las que
midan lo mismo, max_tokens del plan a 5000. (5) Caching incremental de
conversacion: el interprete ya no reenvia entrada_original ni el perfil
completo en cada turno — desde el segundo turno, esa parte vive en el
prefijo cacheado (`llamar_claude_conversacion`, historial que crece turno
a turno); ademas se corrigio un bug real en la contabilidad de costos
(`costo_acumulado_usd`/`reportar_costo` ignoraban por completo el precio
de `cache_read`/`cache_creation`, subestimando el costo real), y se agrego
desglose de costo por componente (`clasificacion`/`turnos`/`plan`/
`estado_vivo`) persistido en `sessions.costo_desglose` (columna nueva,
`supabase/migrations/my_idea_002_costo_desglose.sql`, aplicar manualmente).

Verificado con una corrida real (`fase2_7_macetas_escucha_activa.txt`,
plan completo en `fase2_7_plan_macetas.md`), mismas respuestas literales
que la corrida de Fase 2.6:

- **Cero apariciones de "pero antes"** en toda la transcripcion, y **cero**
  del molde "¿que te preocupa mas: A o B?". Hubo exactamente UNA pregunta
  con forma de desviacion, ocurrida ANTES de que la prioridad alcanzara
  conteo=2 (permitido por la regla); desde que el usuario reafirmo el
  bloqueo tecnico por segunda vez, la respuesta fue "La resina y el QR son
  tu frente tecnico principal y vamos a atacarlos de una vez; para avanzar
  rapido ahi, ¿ya probaste cambiar una sola variable a la vez...?" — cero
  desviaciones despues de eso.
- **prioridad_declarada final**: `{"texto": "resolver la resina y el QR
  antes de vender en volumen (acoplados tecnicamente)", "conteo": 3}`.
- **El plan dedica su Etapa 2 completa** ("Ataca el bloqueo tecnico con
  experimentos de una variable a la vez") al metodo que el propio usuario
  propuso, reconociendolo explicitamente ("Mencionaste algo importante
  durante la sesion...") y estructurandolo con tarjetas de experimento
  (hipotesis, variable, metrica, umbral) mas alternativas de fijacion del
  QR con criterio de exito medible — al nivel del plan de Fase 2.4.
- **Dependencias resueltas**: la Etapa 3 (MVP) explicita que se prueba
  "aunque tenga defectos de resina que no afecten la lectura del codigo",
  en vez de exigir unidades sin defectos que ninguna etapa anterior
  ensena a producir.
- **5 etapas** (dentro del tope de 5-7), cero vocabulario corporativo.
- **Costo**: $0.1842 total (`turnos` $0.0817 con cache_read de 232,984
  tokens confirmando el caching incremental activo; `plan` $0.0948;
  `estado_vivo` $0.0043; `clasificacion` $0.0033) — por debajo del techo
  duro de $0.30, mejor que los $0.2122 de la corrida de Fase 2.6, pero por
  encima del objetivo aspiracional de $0.15: el costo de `turnos` bajo
  bien gracias al cache, pero la llamada unica del redactor (Sonnet) sigue
  siendo cara por su propio precio por token y no se beneficia de cache
  dentro de una sola sesion (solo se llama una vez).

## Fase 2.8 — navegacion libre con brujula semantica, "sigamos" dirigido, coherencia por autodeclaracion

Auditoria de la Fase 2.7: aprobada en un 85% — la escucha activa, la
cobertura del bloqueo declarado y el caching funcionan. El 15% pendiente:
el motor navegaba adaptativo pero "sobre un riel" — en cada turno solo
podia elegir entre los sucesores del nodo actual (2 niveles), asi que una
respuesta que apuntaba a otra rama de la telaraña (o a una fase anterior)
quedaba absorbida al perfil en vez de saltar ahi. Ademas se detectaron dos
bugs nuevos: (1) la "promesa rota del sigamos" — el usuario aceptaba
profundizar, el sistema decia "sigamos un poco mas" y generaba el plan
sin una sola pregunta nueva (la ruta ya iba en el tope de profundidad); y
(2) la incoherencia etiqueta/contenido volvia por otra puerta — un plan
con etapa completa de costeo aun asi declaraba "no cubre viabilidad
economica" porque ese contenido entro via nodos etiquetados "general" que
el clasificador por keywords no detectaba.

Cambios: (1) **Brujula semantica** — `engine/build_semantic_index.py` genera
embeddings locales (sentence-transformers, `paraphrase-multilingual-MiniLM-
L12-v2`, costo cero por sesion) de los 1265 nodos en `engine/semantic_
index.npz`. `buscar_afines()` los usa cada turno para ofrecerle al
interprete, ademas de los sucesores locales, hasta 8 "saltos_posibles" de
CUALQUIER parte del grafo (cualquier fase, incluso anteriores). El
interprete puede saltar (`salto_semantico`, max 1 por turno, registrado en
la ruta con modo "salto") cuando la respuesta introduce un tema que ningun
sucesor local atiende bien. Si sentence-transformers o el indice no estan
disponibles, la brujula se desactiva silenciosamente y el motor sigue
navegando solo local. (2) **"Sigamos" dirigido** — en vez de devolver el
control al riel local, `extender_sigamos_dirigido` usa la brujula para
elegir 2-3 nodos reales de la familia faltante y los conversa como
extension (hasta 3 turnos por encima de `MAX_DEPTH`); si no hay
candidatos genuinos, lo dice honestamente en vez de fingir continuar. (3)
**Coherencia por autodeclaracion** — el redactor ya no se evalua por tags
de `node_families` para la etiqueta del plan: declara el mismo, en un
bloque final `===JSON===`, que familias trato CON SUSTANCIA REAL (regla
11 del `SYSTEM_PLAN`), y esa autodeclaracion es la unica fuente de la
etiqueta inicial/completo y de "Lo que este plan aun no cubre".

**Dos bugs reales encontrados y corregidos durante la verificacion de esta
misma fase** (documentados aqui porque son parte de la historia de la
prueba, no solo el resultado final):
- El modelo casi nunca saltaba: prefería seguir localmente porque
  `pregunta_adaptada` es tan flexible que puede hacer sonar relevante casi
  cualquier nodo local, y `repreguntar` servia de valvula de escape para
  explorar temas nuevos sin comprometerse a un salto. Se cerro
  restringiendo `repreguntar` a desambiguacion pura (nunca exploracion de
  tema nuevo) y agregando un "chequeo obligatorio" mecanico antes de
  decidir accion: si algun salto_posible es mas especifico al dato nuevo
  que los sucesores locales, saltar es obligatorio aunque lo local
  tambien suene razonable. Ademas se subio el numero de saltos ofrecidos
  de 5 a 8 (el mejor candidato a veces rankeaba 6to en similitud coseno).
- `extender_sigamos_dirigido` siempre encontraba cero candidatos: comparaba
  `families.get(nid)` (claves cortas: `"accion_clientes"`,
  `"viabilidad_economica"`) contra `evaluacion["familias_faltantes"]`, que
  en realidad son las FRASES largas para el usuario (`plan_readiness.
  evaluar_ruta` devuelve texto legible, no claves) — la comparacion nunca
  podia ser verdadera. Se corrigio derivando las claves cortas directamente
  de `tiene_accion_clientes`/`tiene_viabilidad_economica` antes de llamar a
  la funcion.

Verificado con una corrida real (`fase2_8_macetas_navegacion_libre.txt`,
plan completo en `fase2_8_plan_macetas.md`), mismas respuestas literales
que las corridas de Fase 2.6/2.7:

- **3 saltos semanticos** en la ruta (`[SALTO]alfabetizacion_en_materiales_
  maliciosos`, `[SALTO]trabajo_en_lotes_pequenos`, `[SALTO]hoja_
  estimacion_costos`) — el ultimo especialmente bien justificado: el
  usuario dijo "cobro por pieza pero no he calculado bien cuanto me
  cuesta" y el sistema salto directo a una "Hoja de Trabajo de Estimacion
  de Costos" de otra rama del grafo, algo que ningun sucesor local de ese
  punto ofrecia.
- **"Sigamos" dirigido**: tras aceptar profundizar, el sistema hizo 3
  preguntas economicas reales y especificas (estructura de costos, modelo
  de precios, curva de demanda/estrategia de precio) antes de generar el
  plan — no la falsa promesa de la auditoria anterior.
- **Plan etiquetado `_Plan completo_`, coherente con el contenido**: trata
  con sustancia real tanto accion_clientes (ventas reales, etapas 3-4) como
  viabilidad_economica (formulas de costeo explicitas en "¿Puede
  sostenerse tu idea?"), sin inventar cifras que el usuario no dio, y sin
  seccion "no cubre" (no aplica porque la autodeclaracion dice que ambas
  familias si se trataron).
- **Costo**: $0.2746 total — por debajo del techo duro de $0.30, aunque
  por encima del objetivo aspiracional de $0.25 de la prueba. La razon es
  directa: esta corrida SI disparo correctamente la extension dirigida
  (3 preguntas economicas reales + sus llamadas de interpretacion), a
  diferencia de una corrida previa (con el bug de comparacion de claves
  aun sin corregir) que resultaba mas barata solo porque fallaba en
  silencio sin preguntar nada. Se prefirio corregir el bug sobre cumplir
  el objetivo de costo.

## Los dos cierres verificados en esta prueba

**Cierre elegante**: forzando EOF a mitad de sesión (`leer_entrada()`
envuelve todo `input()`), el proceso ya no termina en traceback. Imprime
"Sesión interrumpida. Tu progreso quedó guardado." con el comando exacto
de `--continuar` (y `--seguir`, si aplica), sale con código 0, y retomar
con `--continuar` funciona porque el estado ya se guardaba turno a turno
desde antes.

**Auto-corrección invisible**: verificado con un mock de `llamar_claude`
que fuerza un id inventado en el intento inicial Y en el reintento
(`scratchpad/test_autocorreccion.py`, no versionado): confirma que (a) el
reintento incluye `error_previo` + `ids_validos` literales en el
contexto, (b) tras fallar dos veces seguidas selecciona en silencio el
candidato de mayor afinidad con la última respuesta del usuario, (c) el
resultado es un `avanzar` válido (nunca `None`), y (d) el evento queda
registrado como `fallback_auto` en la sesión. Un caso de control (fallo
de red simulado) confirma que ESE camino sigue devolviendo `None` — el
menú numerado de emergencia sigue existiendo, pero ahora es
estrictamente el último recurso tras fallo de red total, no la respuesta
por defecto ante una alucinación del modelo.
