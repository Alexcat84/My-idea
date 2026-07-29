# FASE 3.8 — EL SENTIDO DEL TIEMPO
Celebración + modo del camino + línea base opcional + análisis del proyecto.
Repo "My-idea", rama staging. El usuario adjunta 3 archivos de canon:
HTML 09 (La Celebración), HTML 10 (Modo y Fechas), HTML 11 (Análisis del
Proyecto). PRIMER COMMIT de la fase: recommittearlos a docs/diseno-canon/.
Implementar contra ellos extrayendo estilos y animaciones del HTML, jamás
reinterpretando. Las notificaciones NO se construyen en esta fase (son la
4.1); esta fase deja sus datos listos.

## 1. Migración 018 + dbContract + tests
- projects.realizada_at (timestamptz null)
- projects.modo_camino (text null, CHECK 'ritmo' | 'fechas')
- plans.baseline_confirmada_at (timestamptz null)
- checklist_items.completed_at (timestamptz null)
- checklist_items.fecha_base (timestamptz null)
- checklist_items.fecha_base_origen (text null, CHECK 'sugerida' | 'ajustada' | 'manual')
- checklist_items.fecha_base_original (timestamptz null)

## 2. Timeline real (para TODOS los usuarios, cero fricción)
Al marcar un ítem como Hecho: "¿Cuándo lo hiciste? HOY / elegir fecha".
HOY es el default y un solo toque; la fecha elegida puede ser pasada.
Se persiste en completed_at y es editable después desde el ítem.
PATCH del checklist ampliado y validado.

## 3. Modo del camino (HTML 10, vista A)
Al entrar por PRIMERA vez a Manos a la Obra de cada idea: la tarjeta
"¿Cómo quieres llevar tu camino?" con dos opciones de peso visual IGUAL:
"A mi ritmo" y "Con fechas y recordatorios". La elección persiste en
projects.modo_camino y queda registrada en la bitácora del proyecto.
- "A mi ritmo": todo funciona como hoy (checklist, estados, notas,
  completed_at). Nada de fechas base.
- "Con fechas": abre el ritual del punto 4.
Interruptor permanente en Manos a la Obra ("Fechas y recordatorios:
activados/pausados"): activarlo a mitad de camino abre el ritual con
sugerencias recalculadas desde los ítems pendientes; pausarlo silencia
sin borrar fechas. Cada cambio de modo va a la bitácora.

## 4. Línea base (HTML 10, vista B; solo modo fechas)
- Sugeridor determinístico, CERO LLM, corre al abrir el ritual:
  ítems de la etapa N -> plan.created_at + N semanas (fin de semana
  laboral, sin hora); los ítems "Esta semana" de la etapa N -> inicio de
  su semana. Si existen completed_at previos con patrón de día de la
  semana, las sugerencias del ciclo siguiente respetan ese día.
- El usuario ve las fechas sugeridas en lenguaje humano ("viernes 20 de
  marzo"). Botón héroe "Aceptar estas fechas" (un toque confirma todo);
  edición inline por ítem (date picker; hora OPCIONAL y colapsada);
  acción rápida por etapa ("mover esta etapa una semana").
- Al confirmar: plans.baseline_confirmada_at del ciclo se sella y los
  ítems guardan fecha_base + fecha_base_origen. Ediciones POSTERIORES a
  la confirmación preservan la primera fecha en fecha_base_original.
- La base VIGENTE para toda lectura es la del último plan con baseline
  confirmada.
- "Ponerlas después" nunca bloquea el acceso al checklist.

## 5. La Celebración (HTML 09)
- Acción "Marcar como realizada" en Manos a la Obra, con confirmación en
  palabras de persona. NO exige el checklist al 100% (las ideas reales
  cierran con pendientes). Persiste realizada_at.
- La pantalla: timeline vertical del viaje construido SOLO de lo
  persistido (chispa = projects.created_at, Claridad, cada plan por
  ciclo, ítems completados por completed_at, unlocks de mundos con su
  matiz, REALIZADA al final). Cero LLM, cero costo por render.
- Animación: la barra azul desciende encendiendo hitos; duración FIJA
  6-8s sin importar el largo del viaje; saltable con un toque;
  prefers-reduced-motion -> directo al estado estático. Al final, UN
  pulso verde, se estampa el pill "Proyecto" y aparece el héroe "Aquí
  acaba tu idea y nace tu proyecto".
- Sección "Estadísticas de {nombre del proyecto}": métricas reales
  (días desde la chispa, ciclos, acciones X/N, mundos). La línea de
  cumplimiento (a tiempo / adelantadas / tardías) SOLO si hubo baseline
  confirmada (variante "a mi ritmo" del canon: solo fechas reales).
- Link "Ver análisis completo" -> pantalla del punto 6.
- "Reabrir esta idea" pone realizada_at a null.
- Home: la cinta de una idea realizada gana el pill "Proyecto" (verde,
  con forma además de color) y las realizadas se agrupan en una sección
  al final de la lista.

## 6. Análisis del proyecto (HTML 11)
Pantalla "Análisis de {nombre}", accesible desde Manos a la Obra y desde
la celebración. Todo calculado de lo persistido, cero LLM:
- CAPA UNIVERSAL (siempre): duración total, duración real por etapa,
  ritmo (acciones por semana), racha más larga, ciclos de plan, mundos.
- CAPA DE CUMPLIMIENTO (solo con baseline confirmada): a tiempo /
  adelantadas / tardías con conteos y porcentajes (umbral: a tiempo =
  |completed_at - fecha_base| <= 1 día), desviación media en días,
  barras gemelas base-vs-real por etapa, replanificaciones (contadas
  por fecha_base_original no nulo).
- Tono espejo, jamás regaño: tardías en ámbar, nunca rojo.
- Botón "Descargar mi informe (.md)" con el informe completo.

## 7. Verificación y cierre
- Los conteos de analytics se prueban contra casos calculados A MANO
  (regla AGENTS.md): sembrar un proyecto sintético con fechas conocidas
  y asertar cada métrica.
- Vuelo extendido, dos ciclos: (a) modo fechas: elegir modo -> aceptar
  sugerencias -> marcar ítems con fechas pasadas -> realizada ->
  celebración y análisis coherentes con lo sembrado; (b) modo a-mi-ritmo:
  sin base, capa universal sola, celebración en su variante.
- Gate lado a lado de las tres pantallas nuevas desde sesión real.
- Suites verdes en clon limpio. Commits "Phase 3.8:". Tag web-v0.7.0.
- Reportar costos reales de la fase.
