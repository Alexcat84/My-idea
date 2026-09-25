/** El reporte de Tus Números (lib/engine/reporte.ts): las preguntas de la
 * mini-entrevista (con {{u}} = la unidad de venta del usuario), el reporte del
 * guardián GIGO y el respaldo sin IA. Los "## ", "- " y "> " son estructura
 * markdown del documento. */
import type { PorIdioma } from "../config";

const es = {
  /** la unidad de venta cuando el usuario no dio ninguna (va dentro de las preguntas) */
  unidadPorOmision: "unidad",
  preguntas: {
    servicio: {
      costo_materiales_unidad:
        "¿Cuánto te cuesta directamente cada {{u}} (insumos, materiales que uses, etc.)? Un número aproximado sirve; si no tienes, responde 0.",
      horas_por_unidad: "¿Cuántas horas de trabajo te toma cada {{u}}?",
      valor_hora: "¿En cuánto valoras tu hora de trabajo (lo que sientes que deberías ganar por hora)?",
      precio_tentativo: "¿A qué precio cobras (o cobrarías) cada {{u}}?",
      capacidad_semanal: "En una semana normal, ¿cuántas veces puedes atender? Cuenta cada {{u}} como una vez.",
      costos_fijos_mensuales: "¿Tienes costos fijos mensuales (renta, herramientas, etc.)? Si sí, ¿cuánto suman al mes?",
    },
    digital: {
      costos_fijos_mensuales:
        "¿Cuánto gastas al mes en costos fijos de infraestructura (hosting, APIs, herramientas, suscripciones)?",
      costo_materiales_unidad:
        "¿Tienes algún costo variable por cada {{u}} (por ejemplo, costo de API por uso)? Si es prácticamente cero, responde 0.",
      precio_tentativo: "¿A qué precio o ingreso promedio vendes (o venderías) cada {{u}}?",
      unidades_vendidas: "Contando por {{u}}, ¿cuánto tienes hoy, o cuál sería una meta mensual realista?",
    },
    productoFisico: {
      costo_materiales_unidad: "¿Cuánto gastas en materiales por {{u}}, más o menos? Un número aproximado sirve.",
      horas_por_unidad: "¿Cuántas horas de trabajo te toma cada {{u}}, de principio a fin?",
      valor_hora: "¿En cuánto valoras tu hora de trabajo (lo que sientes que deberías ganar por hora)?",
      precio_tentativo: "¿A qué precio venderías (o vendes) cada {{u}}?",
      capacidad_semanal: "En una semana normal, ¿cuánto puedes producir, contando por {{u}}?",
      costos_fijos_mensuales: "¿Tienes costos fijos mensuales (renta, herramientas, etc.)? Si sí, ¿cuánto suman al mes?",
    },
  },
  tusNumerosHoy: "## Tus números hoy",
  gigo: {
    algoNoCuadra: "Antes de calcular nada, encontré algo que no cuadra en estos números:",
    noVoyACalcular:
      "No voy a calcular margen ni punto de equilibrio con estos datos: el resultado sería una cifra que suena precisa pero está mal, y eso es peor que no tener el cálculo. Prefiero decírtelo con honestidad.",
    losNumerosQueDiste: "## Los números que diste",
    losQueTeFaltanComo: "## Los números que te faltan (y cómo conseguirlos)",
    revisa:
      "Revisa si alguno de los números de arriba está en una unidad distinta a la que esperaba el reporte (por ejemplo, un gasto mensual anotado como costo por unidad, o un plazo en meses anotado como horas), corrígelo, y vuelve a generar el reporte con la cifra corregida.",
  },
  offline: {
    costo: "- Costo por unidad: {{valor}}",
    margen: "- Margen por unidad: {{valor}} ({{porcentaje}}%)",
    equilibrio: "- Punto de equilibrio: {{valor}} unidades/mes",
    techo: "- Techo de ingreso mensual: {{ingreso}} ({{unidades}} unidades/mes)",
    losQueTeFaltan: "## Los números que te faltan",
  },
};

const en: typeof es = {
  /** la unidad de venta cuando el usuario no dio ninguna (va dentro de las preguntas) */
  unidadPorOmision: "unit",
  preguntas: {
    servicio: {
      costo_materiales_unidad:
        "How much does each {{u}} cost you directly (supplies, materials you use, etc.)? A rough number is fine; if you don't have one, answer 0.",
      horas_por_unidad: "How many hours of work does each {{u}} take you?",
      valor_hora: "How much is an hour of your work worth to you (what you feel you should earn per hour)?",
      precio_tentativo: "What price do you charge (or would you charge) for each {{u}}?",
      capacidad_semanal: "In a normal week, how many can you take on, counting each {{u}}?",
      costos_fijos_mensuales: "Do you have monthly fixed costs (rent, tools, etc.)? If so, how much do they add up to per month?",
    },
    digital: {
      costos_fijos_mensuales:
        "How much do you spend each month on fixed infrastructure costs (hosting, APIs, tools, subscriptions)?",
      costo_materiales_unidad:
        "Do you have any variable cost for each {{u}} (for example, API cost per use)? If it's practically zero, answer 0.",
      precio_tentativo: "At what price or average revenue do you sell (or would you sell) each {{u}}?",
      unidades_vendidas: "How many do you have today, counting each {{u}}, or what would be a realistic monthly goal?",
    },
    productoFisico: {
      costo_materiales_unidad: "Roughly how much do you spend on materials for each {{u}}? A rough number is fine.",
      horas_por_unidad: "How many hours of work does each {{u}} take you, from start to finish?",
      valor_hora: "How much is an hour of your work worth to you (what you feel you should earn per hour)?",
      precio_tentativo: "What price would you sell (or do you sell) each {{u}} for?",
      capacidad_semanal: "In a normal week, how many can you make, counting each {{u}}?",
      costos_fijos_mensuales: "Do you have monthly fixed costs (rent, tools, etc.)? If so, how much do they add up to per month?",
    },
  },
  tusNumerosHoy: "## Your numbers today",
  gigo: {
    algoNoCuadra: "Before calculating anything, I found something in these numbers that doesn't add up:",
    noVoyACalcular:
      "I'm not going to calculate margin or break-even point with these numbers: the result would be a figure that sounds precise but is wrong, and that's worse than having no calculation at all. I'd rather tell you honestly.",
    losNumerosQueDiste: "## The numbers you gave",
    losQueTeFaltanComo: "## The numbers you're missing (and how to get them)",
    revisa:
      "Check whether any of the numbers above is in a different unit than the report expected (for example, a monthly expense entered as a cost per unit, or a timeframe in months entered as hours), correct it, and generate the report again with the corrected figure.",
  },
  offline: {
    costo: "- Cost per unit: {{valor}}",
    margen: "- Margin per unit: {{valor}} ({{porcentaje}}%)",
    equilibrio: "- Break-even point: {{valor}} units/month",
    techo: "- Monthly revenue ceiling: {{ingreso}} ({{unidades}} units/month)",
    losQueTeFaltan: "## The numbers you're missing",
  },
};

export const REPORTE: PorIdioma<typeof es> = { es, en };
