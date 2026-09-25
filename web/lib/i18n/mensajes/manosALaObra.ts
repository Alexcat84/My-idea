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
    manos: "Manos a la obra",
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
    tuViajeCore: "Tu viaje core · <b>{{hechos}}/{{total}}</b>",
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

export const MANOS_A_LA_OBRA: PorIdioma<typeof es> = { es };
