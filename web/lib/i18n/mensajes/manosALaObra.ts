/** Manos a la Obra (app/ui/ManosALaObra.tsx): el checklist por etapa, el ritual
 * de continuar, el modo del camino, el ritual de fechas, el registro de
 * protección, los mundos en su hub, las tarjetas de acceso y el ritmo. */
import type { PorIdioma } from "../config";

const es = {
  /** compartidos por varias secciones */
  cambiar: "cambiar",
  todaviaNo: "Todavía no",
  cerrando: "Cerrando…",
  etapaN: "Etapa {{n}}",

  /** una fila del checklist */
  fila: {
    verDetalle: "Ver el detalle de esta actividad",
    noAplica: "no aplica",
    noAplicaConMotivo: "no aplica · {{motivo}}",
    estaSemana: "esta semana",
    paraEl: "para el {{fecha}}",
    hechoEl: "hecho el {{fecha}}",
    cambiarFecha: "cambiar fecha",
    cambiarLaFecha: "Cambiar la fecha:",
    ariaCambiarFecha: "Cambiar la fecha en que lo hiciste",
    listo: "listo",
  },

  /** el ritual de 3 tarjetas de "Continuar mi idea" (núcleo y mundo) */
  ritual: {
    encabezado: "Continuar mi idea · {{paso}} de 3",
    encabezadoMundo: "Continuar {{mundo}} · {{paso}} de 3",
    cerrar: "Cerrar",
    aunNoArrancas: "¿Aún no arrancas? Cuéntame qué cambió desde que armamos el plan.",
    aunNoArrancasMundo: "¿Aún no arrancas con {{mundo}}? Cuéntame qué cambió desde que armamos su plan.",
    realidadSeMueve:
      "A veces la realidad se mueve antes que uno: un proveedor que falla, algo que se cayó, una oportunidad nueva. Si ya hiciste algo, márcalo arriba y lo tomo en cuenta.",
    teCuento: "Te cuento",
    checklistEsHistoria: "Tu checklist es tu historia: ¿ya refleja lo que hiciste?",
    llevasHechas:
      "Llevas {{hechos}} de {{total}} acciones hechas. Ajusta arriba lo que haga falta. De eso compongo el «qué ha pasado», sin que lo redactes dos veces.",
    llevasHechasMundo:
      "Llevas {{hechos}} de {{total}} acciones de {{mundo}} hechas. Ajusta arriba lo que haga falta. De eso compongo el «qué ha pasado», sin que lo redactes dos veces.",
    asiVaSigamos: "Así va, sigamos",
    algoMas: "¿Algo más que deba saber?",
    fueraDelChecklist: "Lo que pasó fuera del checklist: una sorpresa, un cambio, algo que descubriste. Opcional.",
    placeholderDetalles: "Cuéntame en tus palabras, escribe o dicta…",
    seguir: "Seguir",
    atras: "Atrás",
    haciaDonde: "¿Hacia dónde profundizamos?",
    siAlgoTeQuita: "Si algo te quita el sueño o te urge resolver, dilo aquí. Si no, yo te guío según tu avance.",
    placeholderEnfoque: "Lo que más me interesa ahora es… (escribe o dicta)",
    pensando: "Pensando…",
    botonMiIdea: "Continuar mi idea · {{n}} créditos",
    botonMundo: "Continuar este mundo · {{n}} créditos",
    noEstoySeguro: "No estoy seguro",
    garantiaCobro: "Se descuentan al entregarse. Si algo falla, no se cobra nada.",
  },

  /** la elección del modo del camino (canon 10, vista A) */
  modo: {
    pregunta: "¿Cómo quieres llevar tu camino?",
    ritmoTitulo: "A mi ritmo",
    ritmoDesc: "Marca tu avance cuando suceda. Sin fechas ni presiones.",
    fechasTitulo: "Con fechas y recordatorios",
    fechasDesc: "Te sugiero un calendario; tú lo ajustas.",
    elegirEste: "Elegir este",
    puedesCambiar: "Puedes cambiar de modo cuando quieras.",
    /** el modo compacto: "Modo: a mi ritmo" */
    actual: "Modo: <b>{{modo}}</b>",
    aMiRitmo: "a mi ritmo",
    conFechas: "con fechas",
  },

  /** los chips de capacidad (la clave es el valor que viaja a la base) */
  capacidad: {
    "2-5": "2 a 5 horas",
    "5-10": "5 a 10 horas",
    "10-20": "10 a 20 horas",
    "20+": "Más de 20 horas",
  },

  /** el ritual de la línea base (canon 10, vista B) */
  fechas: {
    tituloRecalcular: "Recalcular las fechas pendientes",
    tituloPoner: "Ponle fechas a tu camino",
    propongo: "Te propongo estas fechas en lenguaje humano; ajusta la que quieras. La hora es opcional.",
    preguntaCapacidad: "¿Cuántas horas por semana puedes darle a este espacio?",
    reparto:
      "Reparto las semanas según el trabajo que lleva cada tarea, y planeo con el piso de lo que me des: si te sobra tiempo, vas adelantado. Puedes cambiarlo cuando quieras.",
    moverEtapa: "Mover esta etapa una semana",
    avisoAncla: "Esta protección no llega antes de {{protegido}}: muévela o acepta el riesgo con los ojos abiertos.",
    ariaFecha: "Fecha para: {{tarea}}",
    guardando: "Guardando…",
    aceptar: "Aceptar estas fechas",
    ponerlasDespues: "Ponerlas después",
    sinFechas: "Sin fechas no podré recordarte nada.",
  },

  /** el registro visible de un mundo de protección (<v/> es el valor) */
  registro: {
    titulo: "Registro de {{mundo}}",
    camino: "El camino: <v/>",
    protege: "Protege: <v/>",
    tuRespuesta: "Tu respuesta: <v/>",
  },

  /** las horas por semana de un espacio, ya declaradas */
  capacidadEspacio: {
    leDas: "Le das <b>{{horas}}</b> por semana.",
    preguntaAhora: "¿Cuántas horas por semana puedes darle ahora?",
    nuevasHoras: "Las nuevas horas entran cuando toques Recalcular pendientes.",
  },

  /** el panel del modo y las fechas de un espacio */
  panel: {
    ponerFechasAhora: "Poner fechas ahora",
    fechasActivas: "<b>Fechas activas.</b> Tu camino tiene línea base.",
    anadirCalendario: "Añadir a mi calendario",
    recalcularPendientes: "Recalcular pendientes",
  },

  /** los errores de red de esta pantalla */
  errores: {
    guardarEleccion: "no pudimos guardar tu elección; revisa tu internet e intenta de nuevo",
    guardarHoras: "no pudimos guardar tus horas por semana; revisa tu internet e intenta de nuevo",
    guardarFechas: "no pudimos guardar tus fechas; revisa tu internet e intenta de nuevo",
    moverFecha: "no pudimos mover la fecha; revisa tu internet e intenta de nuevo",
    guardar: "no pudimos guardar; revisa tu internet e intenta de nuevo",
    guardarCambio: "no pudimos guardar el cambio; revisa tu internet e intenta de nuevo",
    conectar: "no pudimos conectar; revisa tu internet e intenta de nuevo",
  },

  /** las tres caras del espacio */
  caras: {
    plan: "Plan",
    manos: "Manos a la Obra",
    avance: "Tu avance",
  },

  /** el núcleo (el viaje core) */
  nucleo: {
    tuViajePrincipal: "Tu viaje principal",
    avanza: "Tu idea avanza en el mundo real",
    tuPlan: "Tu plan",
    /** nombre del calendario .ics y prefijo [Espacio] de sus eventos */
    miIdea: "Mi idea",
    tuViaje: "Tu viaje",
    volverEntrevista: "Volver a la entrevista",
    tuViajeCore: "Tu viaje principal · <b>{{hechos}}/{{total}}</b>",
    pistaEstado: "Toca el círculo de una tarea para elegir su estado (hecha, en proceso, no aplica…).",
    sinChecklist: "Tu checklist nace del plan: genera tu plan y aquí aparecerán sus acciones.",
    historia: "Historia ({{n}})",
    planHistoria: "Plan {{etiqueta}} · {{cuando}}",
    planEtiqueta: "Plan {{etiqueta}}",
  },

  /** un mundo, apilado o en su hub */
  mundo: {
    completado: "Completado",
    activoConteo: "Mundo activo · {{hechos}}/{{total}}",
    listoParaGenerar: "Listo para generar tu plan",
    activo: "Mundo activo",
    porExplorar: "Por explorar",
    terminado: "Lo diste por terminado {{cuando}}.",
    terminadoConPendientes: "Lo diste por terminado {{cuando}}. Lo que quedó pendiente sigue aquí: es parte de tu historia.",
    exploracion: "Exploración",
    plan: "Plan",
    manos: "Manos a la Obra",
    manosConteo: "Manos a la Obra · {{hechos}}/{{total}}",
    planBasico: "El plan de {{mundo}} es una versión básica: se armó sin la redacción con IA y no se te cobró.",
    usaraSiEntrega: "Esto usará <b>{{n}} créditos</b> de tu saldo, solo si la IA lo entrega.",
    generarCompleto: "Generar el plan completo · {{n}} créditos",
    tuDiagnostico: "Tu diagnóstico",
    elPlanDe: "El plan de {{mundo}}",
    usara: "Esto usará <b>{{n}} créditos</b> de tu saldo.",
    generarMiPlan: "Generar mi plan de {{mundo}} · {{n}} créditos",
    preparando: "Preparando tu mundo…",
    explorar: "Explorar este mundo",
    reabriendo: "Reabriendo…",
    reabrir: "Reabrir este mundo",
    siVuelves: "Si vuelves a él, tu checklist te espera igual.",
    disteTerminado: "¿Diste {{mundo}} por terminado? Podrás reabrirlo cuando quieras.",
    llevas: "Llevas {{hechos}} de {{total}} acciones de este mundo. Las que queden pendientes se guardan tal cual. Cerrar este mundo no cierra tu idea.",
    llevasPct:
      "Llevas {{hechos}} de {{total}} acciones de este mundo ({{pct}}%). Las que queden pendientes se guardan tal cual. Cerrar este mundo no cierra tu idea.",
    porQueCierras: "¿Por qué lo cierras aquí? <s>(opcional, para tu propia memoria)</s>",
    placeholderMotivo: "Lo cierro porque…",
    siTerminado: "Sí, lo doy por terminado",
    cicloDesc: "¿La realidad te cambió el plan de {{mundo}}? Cuéntame qué pasó y lo recalculo desde donde estás.",
    cerrarTitulo: "¿Diste {{mundo}} por terminado?",
    cerrarDesc:
      "Márcalo como completado cuando lo sientas cerrado. Lo que quede pendiente se guarda; podrás reabrirlo cuando quieras.",
    bitacoraTitulo: "Bitácora de {{mundo}}",
    bitacoraDesc: "La historia de este mundo, paso a paso: cada decisión que has tomado aquí.",
    calendarioTitulo: "Calendario de {{mundo}}",
    calendarioDesc: "Lo que viene en este mundo, día por día. Sus fechas, hacia adelante.",
    analisisTitulo: "Análisis de {{mundo}}",
    analisisDesc: "El ritmo, las etapas y el cumplimiento de este mundo, calculados de lo que hiciste.",
    documentosTitulo: "Documentos de {{mundo}}",
    documentosDesc: "El reporte de este mundo y lo que deje cada fase de su camino, en .md o PDF.",
  },

  /** las tarjetas de acceso y acción del núcleo */
  tarjetas: {
    cicloTitulo: "Ciclo de profundización",
    cicloDesc: "¿La realidad te cambió el plan? Cuéntame qué pasó y lo recalculo desde donde estás.",
    bitacoraTitulo: "Mi bitácora",
    bitacoraDesc: "La historia de tu viaje, paso a paso: cada decisión que has tomado.",
    calendarioTitulo: "Tu calendario",
    calendarioDesc: "Lo que viene, día por día. Llévate tus fechas al calendario del teléfono.",
    analisisTitulo: "Análisis del proyecto",
    analisisDesc: "Tu ritmo, tus etapas y tu cumplimiento, calculados de lo que hiciste.",
    documentosTitulo: "Tus documentos",
    documentosDesc: "Tu plan, cada seguimiento y el expediente completo, en .md o en PDF.",
    realizarTitulo: "¿Tu idea ya es un proyecto?",
    realizarDesc: "Cuando lo sientas real, ciérrala. No hace falta terminar todo el checklist.",
  },

  /** el acta de cierre de la idea */
  cierre: {
    realizada: "Tu idea está realizada: el ciclo de profundización vuelve si la reabres desde su celebración.",
    cierraTuIdea: "Esto cierra tu idea y nace tu proyecto. Podrás reabrirla cuando quieras.",
    llevas: "Llevas {{hechos}} de {{total}} acciones. Las que queden pendientes se guardan tal cual: son parte de tu historia.",
    llevasPct:
      "Llevas {{hechos}} de {{total}} acciones ({{pct}}%). Las que queden pendientes se guardan tal cual: son parte de tu historia.",
    porQueCierras: "¿Por qué la cierras aquí? <s>(opcional, para tu propia memoria)</s>",
    placeholderMotivo: "La cierro porque…",
    siProyecto: "Sí, es un proyecto",
  },

  /** el panel Ritmo del lateral */
  ritmo: {
    titulo: "Ritmo",
    ultimaAccion: "Última acción",
    aunNinguna: "aún ninguna",
    desde: "Manos a la Obra desde",
    ciclosAjuste: "Ciclos de ajuste",
    pausa: "Pausa cuando lo necesites. Cuando vuelvas, el checklist te espera exactamente donde quedaste.",
  },
};

const en: typeof es = {
  cambiar: "change",
  todaviaNo: "Not yet",
  cerrando: "Closing…",
  etapaN: "Stage {{n}}",

  fila: {
    verDetalle: "See the details of this activity",
    noAplica: "doesn't apply",
    noAplicaConMotivo: "doesn't apply · {{motivo}}",
    estaSemana: "this week",
    paraEl: "due {{fecha}}",
    hechoEl: "done on {{fecha}}",
    cambiarFecha: "change date",
    cambiarLaFecha: "Change the date:",
    ariaCambiarFecha: "Change the date you did it",
    listo: "done",
  },

  ritual: {
    encabezado: "Continue my idea · {{paso}} of 3",
    encabezadoMundo: "Continue {{mundo}} · {{paso}} of 3",
    cerrar: "Close",
    aunNoArrancas: "Haven't gotten started yet? Tell me what's changed since we put the plan together.",
    aunNoArrancasMundo: "Haven't gotten started on {{mundo}} yet? Tell me what's changed since we put its plan together.",
    realidadSeMueve:
      "Sometimes reality moves before you do: a supplier falls through, something breaks down, a new opportunity shows up. If you've already done something, mark it above and I'll take it into account.",
    teCuento: "Let me tell you",
    checklistEsHistoria: "Your checklist is your story: does it show what you've done so far?",
    llevasHechas:
      "You've done {{hechos}} of {{total}} actions. Adjust anything above that needs it. I'll build the “what's happened” from that, so you don't have to write it twice.",
    llevasHechasMundo:
      "You've done {{hechos}} of {{total}} {{mundo}} actions. Adjust anything above that needs it. I'll build the “what's happened” from that, so you don't have to write it twice.",
    asiVaSigamos: "That's where it stands, let's keep going",
    algoMas: "Anything else I should know?",
    fueraDelChecklist: "What happened outside the checklist: a surprise, a change, something you discovered. Optional.",
    placeholderDetalles: "Tell me in your own words, type or dictate…",
    seguir: "Next",
    atras: "Back",
    haciaDonde: "Where should we go deeper?",
    siAlgoTeQuita: "If something is keeping you up at night or needs solving soon, say it here. If not, I'll guide you based on your progress.",
    placeholderEnfoque: "What matters most to me right now is… (type or dictate)",
    pensando: "Thinking…",
    botonMiIdea: "Continue my idea · {{n}} credits",
    botonMundo: "Continue this world · {{n}} credits",
    noEstoySeguro: "I'm not sure",
    garantiaCobro: "Credits come off only once it's delivered. If something fails, you aren't charged anything.",
  },

  modo: {
    pregunta: "How do you want to move along your path?",
    ritmoTitulo: "At my own pace",
    ritmoDesc: "Mark your progress as it happens. No dates, no pressure.",
    fechasTitulo: "With dates and reminders",
    fechasDesc: "I'll suggest a schedule; you adjust it.",
    elegirEste: "Choose this one",
    puedesCambiar: "You can switch modes anytime.",
    actual: "Mode: <b>{{modo}}</b>",
    aMiRitmo: "at my own pace",
    conFechas: "with dates",
  },

  capacidad: {
    "2-5": "2 to 5 hours",
    "5-10": "5 to 10 hours",
    "10-20": "10 to 20 hours",
    "20+": "More than 20 hours",
  },

  fechas: {
    tituloRecalcular: "Recalculate your pending dates",
    tituloPoner: "Put dates on your path",
    propongo: "Here are the dates I suggest, in plain words; adjust any you like. The time of day is optional.",
    preguntaCapacidad: "How many hours a week can you give this space?",
    reparto:
      "I spread the weeks according to the work each task takes, and I plan around the low end of what you give me: if you end up with time to spare, you'll be ahead. You can change it anytime.",
    moverEtapa: "Move this stage by a week",
    avisoAncla: "This safeguard doesn't land before {{protegido}}: move it, or accept the risk with your eyes open.",
    ariaFecha: "Date for: {{tarea}}",
    guardando: "Saving…",
    aceptar: "Accept these dates",
    ponerlasDespues: "Set them later",
    sinFechas: "Without dates, I won't be able to remind you of anything.",
  },

  registro: {
    titulo: "{{mundo}} register",
    camino: "The path: <v/>",
    protege: "Protects: <v/>",
    tuRespuesta: "Your answer: <v/>",
  },

  capacidadEspacio: {
    leDas: "You give it <b>{{horas}}</b> a week.",
    preguntaAhora: "How many hours a week can you give it now?",
    nuevasHoras: "The new hours kick in when you tap Recalculate pending dates.",
  },

  panel: {
    ponerFechasAhora: "Set dates now",
    fechasActivas: "<b>Dates on.</b> Your path has a baseline.",
    anadirCalendario: "Add to my calendar",
    recalcularPendientes: "Recalculate pending dates",
  },

  errores: {
    guardarEleccion: "we couldn't save your choice; check your connection and try again",
    guardarHoras: "we couldn't save your hours per week; check your connection and try again",
    guardarFechas: "we couldn't save your dates; check your connection and try again",
    moverFecha: "we couldn't move the date; check your connection and try again",
    guardar: "we couldn't save; check your connection and try again",
    guardarCambio: "we couldn't save the change; check your connection and try again",
    conectar: "we couldn't connect; check your connection and try again",
  },

  caras: {
    plan: "Plan",
    manos: "Get to Work",
    avance: "Your progress",
  },

  nucleo: {
    tuViajePrincipal: "Your main journey",
    avanza: "Your idea is moving forward in the real world",
    tuPlan: "Your plan",
    miIdea: "My idea",
    tuViaje: "Your Journey",
    volverEntrevista: "Back to the interview",
    tuViajeCore: "Your main journey · <b>{{hechos}}/{{total}}</b>",
    pistaEstado: "Tap a task's circle to choose its status (done, in progress, doesn't apply…).",
    sinChecklist: "Your checklist grows out of your plan: generate your plan and its actions will show up here.",
    historia: "History ({{n}})",
    planHistoria: "Plan {{etiqueta}} · {{cuando}}",
    planEtiqueta: "Plan {{etiqueta}}",
  },

  mundo: {
    completado: "Completed",
    activoConteo: "Active world · {{hechos}}/{{total}}",
    listoParaGenerar: "Ready to generate your plan",
    activo: "Active world",
    porExplorar: "Still to explore",
    terminado: "You called it done {{cuando}}.",
    terminadoConPendientes: "You called it done {{cuando}}. Whatever was left pending is still here: it's part of your story.",
    exploracion: "Exploration",
    plan: "Plan",
    manos: "Get to Work",
    manosConteo: "Get to Work · {{hechos}}/{{total}}",
    planBasico: "The {{mundo}} plan is a basic version: it was put together without AI writing, and you weren't charged for it.",
    usaraSiEntrega: "This will use <b>{{n}} credits</b> from your balance, only if the AI delivers it.",
    generarCompleto: "Generate the full plan · {{n}} credits",
    tuDiagnostico: "Your diagnosis",
    elPlanDe: "The {{mundo}} plan",
    usara: "This will use <b>{{n}} credits</b> from your balance.",
    generarMiPlan: "Generate my {{mundo}} plan · {{n}} credits",
    preparando: "Getting your world ready…",
    explorar: "Explore this world",
    reabriendo: "Reopening…",
    reabrir: "Reopen this world",
    siVuelves: "If you come back to it, your checklist will be waiting just as you left it.",
    disteTerminado: "Are you calling {{mundo}} done? You can reopen it anytime.",
    llevas: "You've done {{hechos}} of {{total}} actions in this world. Any still pending are kept just as they are. Closing this world doesn't close your idea.",
    llevasPct:
      "You've done {{hechos}} of {{total}} actions in this world ({{pct}}%). Any still pending are kept just as they are. Closing this world doesn't close your idea.",
    porQueCierras: "Why are you closing it here? <s>(optional, just for your own memory)</s>",
    placeholderMotivo: "I'm closing it because…",
    siTerminado: "Yes, I'm calling it done",
    cicloDesc: "Did reality change your {{mundo}} plan? Tell me what happened and I'll recalculate from where you are.",
    cerrarTitulo: "Are you calling {{mundo}} done?",
    cerrarDesc:
      "Mark it as completed when it feels closed. Anything still pending is kept; you can reopen it anytime.",
    bitacoraTitulo: "{{mundo}} Logbook",
    bitacoraDesc: "The story of this world, step by step: every decision you've made here.",
    calendarioTitulo: "{{mundo}} calendar",
    calendarioDesc: "What's coming up in this world, day by day. Its dates, looking ahead.",
    analisisTitulo: "{{mundo}} analysis",
    analisisDesc: "The pace, the stages and the follow-through of this world, calculated from what you did.",
    documentosTitulo: "{{mundo}} documents",
    documentosDesc: "This world's report and whatever each phase of its path leaves behind, as .md or PDF.",
  },

  tarjetas: {
    cicloTitulo: "Deepening Cycle",
    cicloDesc: "Did reality change your plan? Tell me what happened and I'll recalculate from where you are.",
    bitacoraTitulo: "My Logbook",
    bitacoraDesc: "The story of your journey, step by step: every decision you've made.",
    calendarioTitulo: "Your calendar",
    calendarioDesc: "What's coming up, day by day. Take your dates to your phone's calendar.",
    analisisTitulo: "Project analysis",
    analisisDesc: "Your pace, your stages and your follow-through, calculated from what you did.",
    documentosTitulo: "Your documents",
    documentosDesc: "Your plan, every Follow-up and the complete Full Record, as .md or PDF.",
    realizarTitulo: "Is your idea a project yet?",
    realizarDesc: "When it feels real, close it. You don't need to finish the whole checklist.",
  },

  cierre: {
    realizada: "Your idea is achieved: the Deepening Cycle comes back if you reopen it from its celebration.",
    cierraTuIdea: "This closes your idea, and your project is born. You can reopen it anytime.",
    llevas: "You've done {{hechos}} of {{total}} actions. Any still pending are kept just as they are: they're part of your story.",
    llevasPct:
      "You've done {{hechos}} of {{total}} actions ({{pct}}%). Any still pending are kept just as they are: they're part of your story.",
    porQueCierras: "Why are you closing it here? <s>(optional, just for your own memory)</s>",
    placeholderMotivo: "I'm closing it because…",
    siProyecto: "Yes, it's a project",
  },

  ritmo: {
    titulo: "Pace",
    ultimaAccion: "Last action",
    aunNinguna: "none yet",
    desde: "Started Get to Work",
    ciclosAjuste: "Adjustment cycles",
    pausa: "Take a break whenever you need to. When you come back, your checklist will be waiting exactly where you left off.",
  },
};

export const MANOS_A_LA_OBRA: PorIdioma<typeof es> = { es, en };
