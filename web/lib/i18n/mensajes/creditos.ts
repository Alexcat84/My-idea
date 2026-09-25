/**
 * /creditos, el centro de créditos (app/creditos/page.tsx). Sin cifras de
 * precio: los números salen de lib/precios.ts y solo de ahí (AGENTS.md).
 */
import type { PorIdioma } from "../config";

const es = {
  misIdeas: "Mis ideas /",
  titulo: "Créditos",
  disponibles: "Disponible: {{saldo}}",
  saldoNoDisponible: "saldo no disponible",
  /** La píldora del costo, a la derecha de la cifra. */
  creditos: "créditos",
  heroe: {
    tuSaldo: "Tu saldo",
    noPudeLeer: "No pudimos leer tu saldo en este momento. Recarga la página en un rato.",
    garantiaCuenta:
      "Se verifica tu saldo al inicio de cada acción y se descuenta a la entrega. Si algo falla a mitad, no se cobra nada.",
    sinCuenta: "Tus créditos viven en tu cuenta. Entra o crea la tuya para sumar y usar créditos.",
  },
  sumar: {
    titulo: "Sumar créditos",
    nCreditos: "{{n}} créditos",
    compraPronto: "La compra se abre pronto",
  },
  usar: {
    titulo: "Usa tus créditos según lo que necesites",
    gratis:
      "<b>La Claridad</b> es <g>gratis</g>: tu idea ordenada, la frase, lo que tienes y lo que asumes. El <b>diagnóstico de un mundo</b> también es <g>gratis</g>: el primer vistazo de ese frente.",
  },
  proyecto: {
    etiqueta: "Tu proyecto",
    plan: "Tu Plan",
    planTexto: "Tu viaje completo, de la idea a hacerla realidad: el plan y todo para llevarlo a cabo.",
    cambioRumbo: "Un cambio de rumbo",
    cambioRumboTexto:
      "Cuando la realidad te mueve el plan y necesitas replantear sin empezar de cero: cuentas qué pasó, se conserva lo que ya lograste y tu viaje se rehace desde ahí.",
  },
  /** "Lo que incluye" el plan: el prefijo en <b> va en negrita. */
  incluyePlan: [
    "<b>El plan:</b> tus etapas, con sus entregables, tus tareas y tus fechas de un vistazo.",
    "<b>Manos a la Obra:</b> ejecuta tu plan. Marca lo hecho, añade tus notas y ve tu avance en tiempo real. Incluido, siempre.",
    "<b>Tus Números:</b> el tablero de tu idea (margen, punto de equilibrio, escenarios). Corrige cifras y recalcula cuando quieras.",
    "<b>Tus documentos:</b> tu plan y cada resumen, en archivo y PDF, para leer o guardar.",
    "<b>Tu bitácora:</b> la historia de tu viaje, cada decisión, guardada en orden.",
  ],
  mundo: {
    etiqueta: "Un mundo",
    plan: "El plan de un mundo",
    planTexto:
      "Un frente entero de tu negocio (calidad, riesgos, seguridad…), con su propio espacio dentro de tu mismo proyecto.",
    cambioRumbo: "Un cambio de rumbo en un mundo",
    cambioRumboTexto: "Lo mismo dentro de ese frente, cuando ahí necesitas replantear el rumbo.",
  },
  /** "Lo que incluye" el plan de un mundo. */
  incluyeMundo: [
    "<b>Su plan y su Manos a la Obra:</b> las etapas, tareas y fechas de ese frente, listas para ejecutar igual que tu viaje.",
    "<b>Todo lo del mundo, por separado:</b> su avance, sus documentos y su bitácora, solo de ese frente.",
    "<b>Y queda en tu Expediente:</b> el único documento que reúne tu idea, tu plan y cada mundo, cada uno en su propia sección.",
    "<b>Un mismo proyecto:</b> no es otra cuenta ni otra idea.",
  ],
  mundosPorDesbloquear: "Los mundos que puedes desbloquear",
};

const en: typeof es = {
  misIdeas: "My ideas /",
  titulo: "Credits",
  disponibles: "{{saldo}} available",
  saldoNoDisponible: "balance unavailable",
  creditos: "credits",
  heroe: {
    tuSaldo: "Your balance",
    noPudeLeer: "We couldn't read your balance right now. Reload the page in a little while.",
    garantiaCuenta:
      "Your balance is checked when each action starts and charged when it's delivered. If something fails halfway, you're not charged a thing.",
    sinCuenta: "Your credits live in your account. Log in or create yours to add and use credits.",
  },
  sumar: {
    titulo: "Add credits",
    nCreditos: "{{n}} credits",
    compraPronto: "Purchases open soon",
  },
  usar: {
    titulo: "Use your credits for whatever you need",
    gratis:
      "<b>Clarity</b> is <g>free</g>: your idea laid out, its one-line summary, what you have and what you're assuming. A <b>world diagnosis</b> is <g>free</g> too: your first look at that area.",
  },
  proyecto: {
    etiqueta: "Your project",
    plan: "Your Plan",
    planTexto: "Your whole journey, from idea to reality: the plan and everything you need to carry it out.",
    cambioRumbo: "A change of course",
    cambioRumboTexto:
      "When reality shakes up your plan and you need to rethink it without starting over: you share what happened, everything you've achieved is kept, and your journey is rebuilt from there.",
  },
  incluyePlan: [
    "<b>The plan:</b> your stages, with their deliverables, your tasks, and your dates at a glance.",
    "<b>Get to Work:</b> carry out your plan. Check off what's done, add your notes, and see your progress in real time. Always included.",
    "<b>Your Numbers:</b> your idea's dashboard (margin, break-even point, scenarios). Adjust figures and recalculate whenever you want.",
    "<b>Your documents:</b> your plan and every summary, as a file and a PDF, to read or keep.",
    "<b>Your logbook:</b> the story of your journey, every decision, kept in order.",
  ],
  mundo: {
    etiqueta: "A world",
    plan: "The plan for a world",
    planTexto:
      "A whole area of your business (quality, risks, security…), with its own space inside the same project.",
    cambioRumbo: "A change of course in a world",
    cambioRumboTexto: "The same thing within that area, when you need to rethink your direction there.",
  },
  incluyeMundo: [
    "<b>Its plan and its Get to Work:</b> the stages, tasks, and dates for that area, ready to carry out just like your journey.",
    "<b>Everything in the world, kept separate:</b> its progress, its documents, and its logbook, for that area only.",
    "<b>And it goes into your Full Record:</b> the one document that brings together your idea, your plan, and every world, each in its own section.",
    "<b>One and the same project:</b> not another account, not another idea.",
  ],
  mundosPorDesbloquear: "The worlds you can unlock",
};

export const CREDITOS: PorIdioma<typeof es> = { es, en };
