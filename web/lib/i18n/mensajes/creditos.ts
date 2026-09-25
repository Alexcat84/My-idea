/**
 * /creditos, el centro de créditos (app/creditos/page.tsx). Sin cifras de
 * precio: los números salen de lib/precios.ts y solo de ahí (AGENTS.md).
 */
import type { PorIdioma } from "../config";

const es = {
  misIdeas: "Mis ideas /",
  titulo: "Créditos",
  disponibles: "{{saldo}} disponibles",
  saldoNoDisponible: "saldo no disponible",
  /** La píldora del costo, a la derecha de la cifra. */
  creditos: "créditos",
  heroe: {
    tuSaldo: "Tu saldo",
    noPudeLeer: "No pude leer tu saldo en este momento. Recarga la página en un rato.",
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
    "<b>Manos a la obra:</b> ejecuta tu plan. Marca lo hecho, añade tus notas y ve tu avance en tiempo real. Incluido, siempre.",
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
    "<b>Su plan y su Manos a la obra:</b> las etapas, tareas y fechas de ese frente, listas para ejecutar igual que tu viaje.",
    "<b>Todo lo del mundo, por separado:</b> su avance, sus documentos y su bitácora, solo de ese frente.",
    "<b>Y queda en tu Expediente:</b> el único documento que reúne tu idea, tu plan y cada mundo, cada uno en su propia sección.",
    "<b>Un mismo proyecto:</b> no es otra cuenta ni otra idea.",
  ],
  mundosPorDesbloquear: "Los mundos que puedes desbloquear",
};

export const CREDITOS: PorIdioma<typeof es> = { es };
