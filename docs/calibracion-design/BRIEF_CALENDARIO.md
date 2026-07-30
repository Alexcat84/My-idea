# Brief de diseño — El Calendario (fechas + recordatorios + sincronía)

**Fecha del encargo:** 2026-07-30
**Qué es:** una pieza NUEVA, no una calibración. Es la cara del modo **"con
fechas"**: un calendario **interactivo y hacia adelante** con las fechas de las
tareas del usuario, desde el que además podrá **activar recordatorios** que
lleguen a su teléfono y, a futuro, **sincronizar** con el calendario de su
cuenta. Nos abre un frente de **alertas / sincronía / tracking**.

> No confundir con "Tu constancia" (el mapa de calor del Análisis): ese mira
> hacia ATRÁS (los días que ya avanzaste). Este mira hacia ADELANTE (lo que
> viene y hay que recordar). Design puede proponer si conviven separados o si el
> calendario nuevo absorbe también la lectura retrospectiva.

## Para quién y dónde
- Un **fundador NO técnico**: lo tiene que entender y operar solo, sin jerga.
- **Mobile-first**: el móvil es donde vive el recordatorio. Escritorio (1240) y
  móvil (380), pero el móvil manda.

## Las reglas de la casa (no negociables)
- **Ley de color:** azul piensa (navegación/fechas previstas), verde ejecuta
  (hecho/hoy), ámbar guardián (vencida/atención). **Nunca rojo.** Gris = lo que
  falta o ya no se mueve.
- **Espejo, no juez:** una fecha vencida se muestra en ámbar, sin regaño.
- **Sin guiones largos, sin jerga, sin mecánica del motor.** El usuario nunca ve
  nodos, grafos ni conteos internos.

## Qué datos YA existen (para anclar el diseño, cero invención)
- Cada tarea del checklist tiene: **`fecha_base`** (la fecha prevista), su
  **estado** (sin empezar / apenas / en proceso / hecha / no aplica), su
  **etapa**, y su texto.
- Ya se puede **mover una fecha** con oferta de **cascada** a las posteriores
  (endpoint `mover-fecha`), y la **bitácora** registra cada movimiento.
- El proyecto tiene **modo del camino** (`ritmo` | `fechas`): el calendario solo
  aplica en modo **fechas**.

## Lo técnicamente VIABLE (para que las opciones sean realistas)
El diseño debe poder apoyarse en al menos uno de estos, idealmente escalando:

1. **Nivel 0 — sin backend, hoy, en todos los teléfonos:** botón "Añadir a mi
   calendario" que genera un **.ics** (por tarea o por plan). El calendario del
   teléfono (Apple/Google/Outlook) pone el **recordatorio nativo**. Es el MVP.
2. **Nivel 1 — sincronía (cuentas Google):** vía **Google Calendar API** se
   crean/actualizan los eventos en su calendario, con recordatorio. Requiere
   permiso de calendario en el login + backend de sincronía. Fast-follow.
3. **Nivel 2 — push web (PWA):** notificaciones en navegador/PWA. Más costoso y
   de menor cobertura (iOS solo con PWA instalada). Opcional/futuro.

**Recomendación de Claude Code:** diseñar pensando en Nivel 0 como base (siempre
disponible) y Nivel 1 como el "modo conectado". El diseño de los controles debe
degradar con gracia: si no hay cuenta Google, se ofrece el .ics; si la hay, se
ofrece sincronizar.

## Qué diseñar (pedimos OPCIONES)
1. **La vista del calendario.** ¿Mes, semana, agenda/lista, o una combinación?
   Cómo se leen las tareas dateadas: por etapa, por color de estado, hoy,
   vencidas, próximas. Que en móvil una lista/agenda quizá gane al mes.
2. **La interacción.** Mover una fecha desde el calendario (arrastrar o tocar →
   reusa la cascada que ya existe). Marcar hecho. Abrir el detalle de la tarea
   (ya existe el cajón "Detalle de la actividad").
3. **El control de recordatorios.** Cómo el usuario elige "recuérdame":
   ¿por tarea, por etapa, o todo el plan? ¿Con cuánta antelación (el día, la
   víspera, X días antes)? ¿Por qué canal (calendario del teléfono vía .ics /
   Google / in-app)? Estados: recordatorios activados / pausados.
4. **El enganche con "con fechas".** El calendario es la cara del modo fechas;
   cómo entra desde Manos a la Obra / el plan.
5. **La relación con la constancia retrospectiva** (¿separadas, pestañas, una
   sola pieza con "próximo" y "cumplido"?).

## Entrega esperada
Mockups en **1240** (escritorio) y **380** (móvil) de las vistas y de los
estados clave: calendario con tareas dateadas, una fecha **vencida** (ámbar), el
flujo de **"añadir a mi calendario"** (.ics) y de **sincronizar con Google**, y
el panel de **recordatorios** (activados/pausados, antelación, canal). Con sus
`notas.md` (medidas, tokens, estados) como en las entregas anteriores.
