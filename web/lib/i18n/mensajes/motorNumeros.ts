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

export const MOTOR_NUMEROS: PorIdioma<typeof es> = { es };
