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
      capacidad_semanal: "¿Cuántas veces de {{u}} puedes atender en una semana normal?",
      costos_fijos_mensuales: "¿Tienes costos fijos mensuales (renta, herramientas, etc.)? Si sí, ¿cuánto suman al mes?",
    },
    digital: {
      costos_fijos_mensuales:
        "¿Cuánto gastas al mes en costos fijos de infraestructura (hosting, APIs, herramientas, suscripciones)?",
      costo_materiales_unidad:
        "¿Tienes algún costo variable por cada {{u}} (por ejemplo, costo de API por uso)? Si es prácticamente cero, responde 0.",
      precio_tentativo: "¿A qué precio o ingreso promedio vendes (o venderías) cada {{u}}?",
      unidades_vendidas: "¿Cuántas de {{u}} tienes hoy, o cuál sería una meta mensual realista?",
    },
    productoFisico: {
      costo_materiales_unidad: "¿Cuánto gastas en materiales por {{u}}, más o menos? Un número aproximado sirve.",
      horas_por_unidad: "¿Cuántas horas de trabajo te toma cada {{u}}, de principio a fin?",
      valor_hora: "¿En cuánto valoras tu hora de trabajo (lo que sientes que deberías ganar por hora)?",
      precio_tentativo: "¿A qué precio venderías (o vendes) cada {{u}}?",
      capacidad_semanal: "¿Cuántas de {{u}} puedes producir en una semana normal?",
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

export const REPORTE: PorIdioma<typeof es> = { es };
