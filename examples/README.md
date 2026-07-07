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
