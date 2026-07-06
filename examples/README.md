# Fase 2.5 — prueba de dos actos (contra Supabase real)

Caso: la app de navegación por sonar para personas ciegas. Corrida en vivo
contra el proyecto Supabase real (no `--offline`), con las credenciales de
`.env` y el usuario fijo de desarrollo creado por `scripts/setup_dev_user.py`.

## Acto 1 — `acto1_gratis_y_sesion_completa.txt`

1. **`--gratis`**: una sola llamada Haiku, organiza la idea sin instruir.
   Verificado a mano: cero verbos imperativos en las cuatro secciones de
   salida (todo descriptivo: "existe un problema...", "la solución
   utiliza...", nunca "haz esto"). Guardado en Supabase como
   `plans.etiqueta = 'organizador'`, `conceptos_usados = 0`.
2. **Sesión completa (proyecto nuevo)**: la misma entrada, sin `--gratis`,
   hasta el plan. En el camino, el intérprete alucinó un id una vez (mismo
   tipo de fallo que en Fases 2.3/2.4) y cayó correctamente al menú de
   emergencia — visible en la transcripción, retomado con `--continuar`.
   Resultado: `_Plan inicial_` con la sección "Lo que este plan aún no
   cubre" listando `viabilidad_economica` — **coherente**, porque ni la
   ruta ni la cosecha de esa sesión tocaron esa familia (verificado en
   Supabase: `familias_cubiertas = ['accion_clientes']`).

## Acto 2 — `acto2_seguir.txt`

**`--seguir PROJECT_ID`** con el mensaje de campo: 40% de confusión de
usuarios con ruido urbano de fondo, dos instituciones interesadas en
pilotear, costo real de fabricación de $600–900 por sensor, y voluntad de
construir un sistema robusto en vez de otro prototipo desechable.

Verificado:

- **Entrada por nodo avanzado**: aterrizó en "Decisión Pivotar o Proceder"
  — no es una de las 20 puertas curadas, confirma que `--seguir` elige de
  todo el grafo, no solo las puertas de entrada.
- **Cero nodos repetidos del proyecto**: `project_nodes` en Supabase —
  69 filas totales, 69 `node_id` únicos, cero solapamiento entre la sesión
  inicial (35 nodos) y la de seguimiento.
- **El plan toca los tres puntos pedidos**: decisor institucional
  ("habla con las dos instituciones... ¿cuánto podría pagar...?"),
  iteración antes de escalar ("no contrates ni escales hasta que los
  checkpoints técnicos... esten validados"), y costos/escalamiento
  (tres escenarios de costo de fabricación vs. precio institucional).
- **Reconoce el avance**: el plan abre con "Ya tienes algo que la mayoría
  de proyectos tecnológicos nunca alcanza: dos instituciones reales que
  quieren probarlo..." — la regla de "abrir reconociendo el avance" para
  sesiones de seguimiento, funcionando.
- **Coherencia etiqueta/cobertura**: `_Plan completo_`, y esta vez SÍ sin
  contradicción — la cosecha trajo `viabilidad_economica` genuinamente
  (`familias_cubiertas = ['accion_clientes', 'viabilidad_economica']` en
  Supabase, `plans.etiqueta = 'seguimiento'`).
- **`fase_actual` del proyecto** avanzó de `validacion` a `ejecucion`,
  reflejando el progreso real.

## Costo real reportado

| Sesión | Modelo(s) | Costo |
|---|---|---|
| Acto 1a (`--gratis`) | Haiku | $0.0041 |
| Acto 1b (sesión completa, incl. la continuación tras el menú de emergencia) | Haiku + Sonnet | $0.0931 |
| Acto 2 (`--seguir`, incl. la continuación tras el segundo menú de emergencia) | Haiku + Sonnet | $0.1253 |

## Bug encontrado y cerrado durante esta prueba

El intérprete a veces atribuía un nodo de nivel 2 a la rama de nivel 1
equivocada (confundiendo hermanos), y el reparo de un solo nivel no lo
resolvía. Se agregó un segundo reparo (`_reparar_camino_desde_objetivo`)
que reconstruye el camino real hacia el último nodo que el modelo propuso,
buscando su padre correcto en el mismo pool de nivel1+nivel2 que se le
mostró — verificado con los tres casos de fallo reales observados en
sesiones anteriores, más un caso de control (id inventado) para confirmar
que la red de seguridad del menú de emergencia sigue intacta.

Un segundo modo de fallo distinto (`camino vacío`: el modelo dice
`avanzar` sin especificar destino) apareció dos veces en esta prueba — cae
correctamente al menú de emergencia; no es reparable por definición (no
hay destino que reconstruir) y no representa una regresión.
