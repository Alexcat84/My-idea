# EL SCHEDULER INTELIGENTE — factibilidad, investigación y arquitectura
La visión original del fundador como PM: un programador de fechas que entienda
la complejidad y el alcance de cada tarea y sugiera fechas adecuadas cuando el
usuario pida "Con fechas". Investigado ago 2026. Veredicto: SÍ ES CONSTRUIBLE,
por fases, sin traicionar la honestidad de la casa.

## 1. QUÉ EXISTE AFUERA (la investigación)

### a) Motores de optimización open source (la artillería pesada)
- **Timefold Solver** (Apache-2.0, el fork del creador de OptaPlanner; Java/
  Kotlin/Python): constraint solver de clase industrial para rostering,
  job-shop, task assignment. Metaheurísticas (Tabu Search, Simulated
  Annealing) sobre restricciones duras/blandas.
- **Google OR-Tools CP-SAT** (Apache-2.0): programación por restricciones;
  el estándar para scheduling con precedencias y capacidades.
- **Veredicto para My Idea: NO son la pieza.** Resuelven problemas con
  cientos-miles de recursos y restricciones en conflicto. Nuestro caso es
  UN recurso (el usuario), ≤50 tareas, restricciones simples (secuencia de
  etapas + capacidad semanal). Un solver aquí sería teatro de sofisticación:
  stack ajeno (JVM), caja negra inauditable, y cero ventaja sobre un
  empaquetado voraz correcto y testeable a mano. Se citan como prior art y
  como opción futura si algún día hubiera equipos multi-persona.

### b) Estimación de esfuerzo con LLMs (la literatura 2024-2026)
- Los LLMs en zero-shot predicen story points AL NIVEL O MEJOR que modelos
  de deep learning supervisados, sin datos de entrenamiento del proyecto
  (arXiv 2603.06276, 16 proyectos, 4 LLMs, 2026); mejoran más con pocos
  ejemplos.
- RAG con tareas históricas similares mejora la estimación (ICPC 2026);
  fine-tuning ligero (Llama3SP con QLoRA) alcanza SOTA en hardware modesto.
- La lección aplicable: **estimar en BANDAS relativas (tipo story points),
  no en horas precisas, es donde los LLMs son fiables.** La precisión falsa
  es el enemigo; la clasificación gruesa es el punto dulce.

### c) Los schedulers comerciales (Motion, Reclaim, etc.)
- Hacen capacity packing: tareas con duración estimada POR EL USUARIO +
  calendario → auto-colocación. Su límite: el usuario debe saber estimar
  (nuestro usuario NO sabe: por eso existe My Idea) y no tienen método de
  negocio. **Nuestro diferencial: el grafo YA SABE qué implica cada tarea**
  (pasos accionables, entregable esperado): podemos estimar POR el usuario.

## 2. LA ARQUITECTURA PROPUESTA (tres capas, honestas)

### Capa 1 — ESTIMACIÓN (LLM, una sola vez, al nacer el plan)
Cuando el motor redacta el plan, clasifica cada acción en una banda:
- **banda de esfuerzo**: S (≤1 h) · M (2-4 h) · L (una jornada) · XL (varios
  días) — rangos honestos, jamás "3.5 horas".
- **espera externa**: sí/no (¿depende de terceros? "envía 3 correos y espera
  respuestas" tiene lead time aunque el esfuerzo sea S).
Insumos que ya existen: título, pasos_accionables, entregable_esperado del
nodo, y el contexto del usuario (su dedicación declarada en la entrevista).
Costo: centavos por plan (cabe en la misma llamada del plan o una llamada
batch). Se guarda como dato del ítem. El usuario PUEDE corregir la banda
(su corrección es oro: telemetría de calibración).

### Capa 2 — EMPAQUETADO (determinístico, puro, testeable a mano)
Input: bandas + capacidad semanal del usuario (una pregunta nueva del ritual
de fechas: "¿Cuántas horas por semana puedes darle?" con chips 2-5 / 5-10 /
10-20 / 20+) + las reglas duras del método (las etapas son puertas: la N+1
arranca al cerrar la N; dentro de una etapa, las tareas comparten ventana).
Algoritmo: empaquetado voraz por semanas — se suman las horas-medias de las
bandas hasta llenar la capacidad de la semana; lo que no cabe, a la
siguiente; las tareas con espera externa fijan inicio temprano en su etapa y
entrega tras su lead time (p.ej. +1 semana). Salida: fechas por tarea que
RESPIRAN según el usuario (el de 3 h/semana recibe un plan de 10 semanas; el
de 20 h/semana, uno de 3) en vez del viernes fijo por etapa.
Cero IA en runtime: mismo input → mismas fechas, tests con aritmética a mano.

### Capa 3 — APRENDIZAJE (la telemetría que ya existe, cerrando el ciclo)
Ya aprendemos diaDominante y cadenciaRealSemanas. Se añade el multiplicador
personal por banda: si tus tareas "M" reales tardan el doble de lo estimado,
tu siguiente recálculo usa TU factor. Cada "Contar qué pasó" recalibra. Con
el tiempo, el scheduler conoce al usuario mejor que el usuario.

## 3. POR QUÉ ESTO ES EL FOSO (posicionamiento)
Motion/Reclaim: packing sin método ni estimación propia. LivePlan/Upmetrics:
método sin ejecución. ChatGPT: estimaciones sin persistencia ni calibración.
**Nadie une las tres piezas: un grafo metodológico que sabe qué implica cada
tarea + estimación automática honesta en bandas + empaquetado por la
capacidad real del usuario que aprende de su historia.** Es la visión PM del
fundador hecha producto, y ningún competidor tiene la materia prima (el
grafo) para copiarla rápido.

## 4. RIESGOS Y MITIGACIONES
1. **Consistencia del LLM al estimar** (misma tarea, bandas distintas entre
   corridas): mitigado por bandas gruesas (4 opciones, no horas) y por el
   SPIKE DE VALIDACIÓN previo (§5). La literatura respalda el zero-shot en
   esta granularidad.
2. **Falsa precisión percibida**: mitigado por mostrar SIEMPRE rangos
   ("~2-4 h") y por el derecho del usuario a corregir la banda.
3. **Fricción de UX** (una pregunta más en el ritual): una sola pregunta con
   chips, con default sensato (5-10 h/semana) y editable después.
4. **Coste**: centavos por plan, una vez; el empaquetado es gratis.
5. **El sugeridor actual NO muere**: queda como fallback si la estimación
   falta (planes viejos) y como base del modo simple.

## 5. EL CAMINO (fases con puertas)
- **F0 — SPIKE de estimación (la puerta de todo):** tomar 30-40 tareas
  reales de planes existentes, pedirle al LLM las bandas 3 veces por tarea,
  medir concordancia inter-corrida y contra el juicio del fundador (que ES
  PM certificado: el estándar de oro está en casa). Si la concordancia es
  alta (>80% misma banda o adyacente), luz verde; si no, se ajusta el prompt
  o se degrada a 3 bandas. Costo: <$1. SIN tocar producción.
- **F1 — Estimación en el plan nuevo**: las bandas nacen con cada plan
  nuevo (campo nuevo en checklist_items, migración pequeña), visibles como
  "~2-4 h" en el detalle de la tarea. Aún sin scheduler: solo información
  honesta que ya vale por sí sola.
- **F2 — La pregunta de capacidad + el empaquetado**: el ritual de fechas
  gana la pregunta; "Con fechas" usa el empaquetado por capacidad. El
  Gantt honesto ya está listo para dibujar lo que salga.
- **F3 — Esperas externas** (lead times) y **F4 — multiplicador personal**
  (aprendizaje por banda). Cada fase con sus tests a mano y su gate.

## 6. LA DECISIÓN DEL FUNDADOR
Este documento es la factibilidad y el mapa. La palabra del fundador decide:
(a) si la visión se construye ahora (empezando por el spike F0) o post-beta
con telemetría real; (b) la pregunta de capacidad (texto y chips); (c) si
las bandas se muestran al usuario desde F1 o se usan solo internamente.
