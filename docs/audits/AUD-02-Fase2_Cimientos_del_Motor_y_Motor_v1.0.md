# AUD-02 — Fase 2 (kickoff a 2.5) y cierre de Motor v1.0

**Estado: cerrado. Tag `motor-v1.0`.**

Nota de trazabilidad: este documento se reconstruye a partir del historial
de commits, sus diffs, y `examples/README.md` (ya escrito en su momento
para Motor v1.0). Los detalles de Fase 2.1 a 2.5 no fueron presenciados en
primera persona por la instancia de Claude que redacta este registro
(pertenecen a una sesión de trabajo anterior) — se documentan con la
evidencia disponible (título de commit + diff stat), sin inventar
narrativa que no está respaldada por el repositorio. Motor v1.0 sí tiene
evidencia de prueba completa y verificada (ver sección 3).

---

## 1. El punto de partida

Tras el cierre de Fase 1 (dataset saneado, `dataset-v1.0.0`), Fase 2
construye el motor conversacional: el filtro de entrada, el ruteo
turno-a-turno por el grafo, y el ensamblador de planes.

## 2. Ledger de commits (kickoff a 2.5)

### 2.1 Phase 2 kickoff (`c54d5e1`)
- Reemplaza los 10 `entry_seeds` provisionales de Fase 1.8 por 20 puertas
  curadas (5 por fase de proyecto), elegidas por topología (pocos
  prerrequisitos, fan-out moderado) y por contenido (que suenen como un
  primer paso natural). Las 20 verificadas contra el dataset de 1265 nodos
  vigente en ese momento.
- Nuevo `engine/cuestionario_raiz.json` (cuestionario de 2 preguntas que
  mapea el estado del usuario a una de las 20 puertas) y
  `engine/prototipo_motor.py` (prototipo CLI: cuestionario raíz → recorrido
  guiado por `nodos_siguientes` → plan de acción ensamblado).
- Verificado de punta a punta: las 4 puertas de fase corridas con
  recorridos cortos y de profundidad máxima; el plan de ejemplo se
  reprodujo exactamente.
- Bug real encontrado y corregido: las consolas de Windows configuran
  `stdout` en `cp1252` por defecto, que no puede codificar caracteres como
  `->` presentes en contenido de algunos nodos — `UnicodeEncodeError`
  mataba la sesión a mitad de un recorrido en fase de planificación.
  Arreglado reconfigurando `stdout`/`stderr` a UTF-8 con `errors="replace"`
  al arrancar.
- Gate 0 sin afectar: 100% de alcanzabilidad dirigida (1265/1265) desde las
  20 semillas nuevas.

### 2.2 Phase 2.1 revised (`6a74bd0`)
Entrevista guiada abierta: interpretación de texto libre turno a turno, sin
opciones cerradas. `engine/build_question_cache.py` nuevo (161 líneas).
`engine/prototipo_motor.py`: +349/-81 líneas.

### 2.3 Phase 2.2 (`26f880f`)
Medidor de "plan listo" (`engine/plan_readiness.py`, nuevo), sesiones de
"profundizar" (go-deeper), redactor de plan en modo imperativo, ruteo
sensible a señales declaradas. Trae consigo `engine/node_families.json`
(clasificación de los 1267 nodos por familia) y el primer
`engine/preguntas_cache.json` (8959 líneas — caché de preguntas por nodo).

### 2.4 Phase 2.3 (`cf26a64`)
Recorrido silencioso multi-salto (varios nodos por turno sin preguntar en
cada uno), lenguaje "idea primero" en vez de jerga de metodología, parche
de caché. Toca `prototipo_motor.py` (+365/-132 aprox.) y regenera partes
del caché de preguntas.

### 2.5 Phase 2.4 (`00d1855`)
Cosecha de vecindario para los planes (nodos relacionados no visitados que
igual aportan al plan final), enriquecimiento de "choke points" (nodos
puente muy transitados), regeneración de caché con el lenguaje "idea
primero". `scripts/phase2_4_enrich.py` nuevo. 135 archivos tocados (en su
mayoría nodos del dataset recibiendo el enriquecimiento).

### 2.6 Phase 2.5 (`b71ae9e`)
Persistencia real en Supabase (`engine/db.py` nuevo, 255 líneas — antes
todo era JSON local), organizador gratuito (`--gratis`), seguimiento de
proyectos (`--seguir`), topes duros de presupuesto por sesión, fix de
coherencia entre lo que un plan declara cubrir y lo que realmente cubre.
Primeras migraciones (`supabase/migrations/my_idea_001_init.sql`) y
primeros documentos de prueba en `examples/` (`acto1_gratis_y_sesion_completa.txt`,
`acto2_seguir.txt` — luego reemplazados por las versiones limpias de Motor
v1.0, ver abajo).

## 3. Motor v1.0 (`9862e9c`) — cierre elegante, auto-corrección invisible

Cambio de fondo: antes de esta versión, una sesión interrumpida a mitad de
pregunta (Ctrl+C, EOF) terminaba en un traceback visible; y cuando el
intérprete devolvía un `id` de nodo inventado, el usuario podía llegar a
ver un menú numerado de emergencia. Motor v1.0 corrige ambos:

- **Cierre elegante**: `leer_entrada()` envuelve todo `input()` y convierte
  `EOFError`/`KeyboardInterrupt` en un mensaje limpio ("Sesión interrumpida.
  Tu progreso quedó guardado.") con el comando exacto para retomar, nunca
  un traceback.
- **Auto-corrección invisible**: si el intérprete inventa un `id`
  inexistente, el sistema reintenta UNA vez con el error y la lista
  literal de ids válidos; si vuelve a fallar, autoselecciona en silencio
  el candidato de mayor afinidad semántica y continúa sin que el usuario
  vea nada — ni error, ni menú, ni pausa. El evento queda registrado
  igual (`fallback_auto`) para auditoría interna.

**Verificado en vivo, contra Supabase real** (caso: app de navegación por
sonar para personas ciegas), documentado en `examples/README.md` líneas
1-68 y en los archivos `examples/acto1a_gratis.txt`,
`examples/acto1b_sesion_completa.txt`, `examples/acto2_seguir.txt`:

| Acto | Qué prueba | Resultado | Costo |
|---|---|---|---|
| 1a (`--gratis`) | Una sola llamada Haiku, cero verbos imperativos en la salida | `plans.etiqueta='organizador'` en Supabase | $0.0042 |
| 1b (sesión completa, un solo pase) | 12 nodos de ruta + 25 de cosecha, auto-corrección invisible activa internamente | `familias_cubiertas` coherente con lo realmente tocado | $0.1489 |
| 2 (`--seguir`) | Entrada por nodo avanzado (no una de las 20 puertas curadas), cero nodos repetidos (44/44 únicos en Supabase) | Coherencia etiqueta/cobertura confirmada | $0.0791 |

Criterio de cierre verificado explícitamente: `grep -c Traceback` sobre
las tres transcripciones = 0 en las tres. Tag `motor-v1.0` aplicado sobre
`9862e9c`.
