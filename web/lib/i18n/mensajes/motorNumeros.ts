/** Los textos que arman para la pantalla los módulos deterministas de Tus Números:
 * calculadora.ts (notas y guardián GIGO), palancas.ts, tableroNumeros.ts y numerosVivo.ts. */
import type { PorIdioma } from "../config";

const es = {
  calculadora: {
    equilibrioSinMargenRango:
      "el margen por unidad no es positivo en todo el rango; no hay punto de equilibrio posible así",
    equilibrioSinMargen: "el margen por unidad no es positivo; no hay punto de equilibrio posible con estos números",
    gigoMargen:
      "con estos números el margen por unidad es {{pct}}%, muy por debajo de -100%: lo más probable es que alguna cifra esté en la unidad equivocada (por ejemplo, un presupuesto mensual leído como costo por unidad, o un plazo en meses leído como horas), no que cada venta pierda esa cantidad de dinero",
    gigoPrecio:
      "el precio declarado es menos del 5% del costo unitario calculado: revisa si el precio y el costo están expresados en la misma unidad (por pieza, por mes, etc.)",
  },
  palancas: {
    volumenBloqueado:
      "Con el margen en rojo, el volumen agranda la pérdida. Primero arregla el margen; cuando esté en verde, aquí va cuántas unidades al mes necesitas para tu meta.",
  },
  escenarios: {
    sinFijos: "falta tu gasto fijo del mes",
    pesimista: "Pesimista",
    tuRitmo: "Tu ritmo de hoy",
    capacidadPlena: "A capacidad plena",
    alMes: "{{n}} al mes",
    /** Las filas de adopción (producto digital), por su nivel (el nivel es el DATO). */
    adopcion: {
      "50%": "mitad de tu meta",
      "100%": "tu meta",
      "200%": "el doble",
    },
  },
  vivo: {
    topeRenarracion:
      "Por hoy llegamos al límite de relecturas. Tus números y tus cambios quedan guardados, el recálculo sigue disponible sin límite, y mañana puedes pedir una relectura nueva.",
    cicloPositivo: "Tu dinero tarda unos {{d}} días en volver a tu bolsillo desde que pagas los materiales.",
    cicloCero: "Tu dinero vuelve el mismo día: cobras justo cuando pagas.",
    cicloNegativo: "Cobras antes de pagar: tu caja trabaja a favor, con unos {{d}} días de holgura.",
    unidadPorDefecto: "unidad",
    datos:
      "Aún me faltan cifras para darte el panorama: cuando completes lo que falta, aquí verás con claridad si cada {{u}} te deja ganancia.",
    perdidaAcento: "{{monto}} más de lo que cobras",
    perdida:
      "Hoy, cada {{u}} que vendes te cuesta {{acento}}: no es problema de vender más, es que el precio todavía no cubre lo que te cuesta hacerla.",
    ajusteAcento: "{{monto}} por {{u}}",
    ajustePct: " ({{pct}}%)",
    ajuste:
      "Cada {{u}} te deja {{acento}}{{pct}}: ya es ganancia, pero un margen delgado, así que conviene reforzarlo antes de crecer.",
    sanoAcento: "{{monto}} limpios",
    sanoCola:
      ", y con vender {{equilibrio}} al mes ya cubres tus {{fijos}} de gasto fijo: de ahí en adelante, cada {{u}} es ganancia",
    sano: "Cada {{u}} te deja {{acento}}{{cola}}.",
  },
};

const en: typeof es = {
  calculadora: {
    equilibrioSinMargenRango:
      "the margin per unit isn't positive across the whole range; there's no possible break-even point like this",
    equilibrioSinMargen: "the margin per unit isn't positive; there's no possible break-even point with these numbers",
    gigoMargen:
      "with these numbers the margin per unit is {{pct}}%, far below -100%: most likely some figure is in the wrong unit (for example, a monthly budget read as a cost per unit, or a timeframe in months read as hours), not that each sale loses that much money",
    gigoPrecio:
      "the price you entered is less than 5% of the calculated unit cost: check that the price and the cost are in the same unit (per piece, per month, etc.)",
  },
  palancas: {
    volumenBloqueado:
      "With your margin in the red, more volume only makes the loss bigger. Fix the margin first; once it's in the green, this is where you'll see how many units a month you need for your goal.",
  },
  escenarios: {
    sinFijos: "your monthly fixed costs are missing",
    pesimista: "Pessimistic",
    tuRitmo: "Your current pace",
    capacidadPlena: "At full capacity",
    alMes: "{{n}} a month",
    adopcion: {
      "50%": "half your goal",
      "100%": "your goal",
      "200%": "double your goal",
    },
  },
  vivo: {
    topeRenarracion:
      "That's the limit for fresh readings today. Your numbers and your changes are saved, recalculating is still unlimited, and tomorrow you can ask for a new reading.",
    cicloPositivo: "Your money takes about {{d}} days to come back to your pocket from the moment you pay for materials.",
    cicloCero: "Your money comes back the same day: you get paid right when you pay.",
    cicloNegativo: "You get paid before you pay: your cash works in your favor, with about {{d}} days of breathing room.",
    unidadPorDefecto: "unit",
    datos:
      "I'm still missing some figures to give you the full picture: once you fill in what's missing, you'll see clearly here whether each {{u}} leaves you a profit.",
    perdidaAcento: "{{monto}} more than you charge",
    perdida:
      "Right now, each {{u}} you sell costs you {{acento}}: the problem isn't selling more, it's that your price doesn't yet cover what it costs you to make it.",
    ajusteAcento: "{{monto}} per {{u}}",
    ajustePct: " ({{pct}}%)",
    ajuste:
      "Each {{u}} leaves you {{acento}}{{pct}}: that's already profit, but a thin margin, so it's worth strengthening before you grow.",
    sanoAcento: "{{monto}} clear",
    sanoCola:
      ", and selling {{equilibrio}} a month already covers your {{fijos}} in fixed costs: from there on, every {{u}} is profit",
    sano: "Each {{u}} leaves you {{acento}}{{cola}}.",
  },
};

export const MOTOR_NUMEROS: PorIdioma<typeof es> = { es, en };
