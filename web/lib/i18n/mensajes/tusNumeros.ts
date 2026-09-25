/** TusNumeros: la pantalla de Tus Números (canon 14): tiles, barra de la verdad, palancas, escenarios, faltantes y versiones. */
import type { PorIdioma } from "../config";

const es = {
  /** Un rango de dinero: "$10 a $20". */
  rango: "{{min}} a {{max}}",
  unidadPorDefecto: "unidad",
  tiles: {
    teCuestaCada: "te cuesta cada {{u}}",
    precioHoy: "precio al que la vendes hoy",
    margenPorPieza: "margen por pieza",
    noHay: "No hay",
    puntoEquilibrio: "punto de equilibrio",
  },
  barra: {
    teCuesta: "Te cuesta",
    cobras: "Cobras",
    enPerdida:
      "La barra de lo que te cuesta es más larga que la de lo que cobras. Ese pedazo que sobresale es <b>la pérdida que pones de tu bolsillo en cada venta</b>. Mientras se vea así, vender más solo agranda el hueco.",
    conMargen:
      "La barra de lo que cobras es la larga, y la de lo que te cuesta no la alcanza. Ese espacio de sobra es <b>tu margen</b>. Aquí, vender más sí te acerca a tu meta.",
  },
  palanca: {
    cierreVolumen: "Es tu palanca más fuerte porque el margen ya es sano.",
    volumenSinMeta:
      "Cuando me digas cuántas puedes hacer por semana, aquí te digo cuántas al mes te dejan ganancia. {{cierre}}",
    volumenSinGanancia:
      "A {{unidades}} al mes llegas a tu capacidad plena; dime tus gastos fijos del mes y te digo cuánto te queda. {{cierre}}",
    volumenConGanancia: "A {{unidades}} al mes, tras cubrir tus fijos, te quedan {{ganancia}} de ganancia. {{cierre}}",
    precioTest:
      "Prueba subiendo a {{meta}} (un 10% más): tu margen sube a {{margen}} por {{u}}. Pruébalo con un lote antes de subirlo a todos.",
    precioVentas: ", y cubres tus fijos con unas {{n}} ventas",
    precioArreglo: "A {{meta}} tu margen pasa a {{margen}} por {{u}}{{ventas}}.",
    costoTest: "Prueba bajando el costo a {{meta}} (un 10% menos): te deja {{margen}} por {{u}}, sin tocar el precio.",
    costoArreglo: "Bajar el costo a {{meta}} te deja {{margen}} por {{u}}, sin tocar el precio.",
    nombrePrecio: "Sube el precio a",
    nombreCosto: "Baja el costo a",
    nombreVolumen: "Vende al mes",
    hoyCobras: "hoy cobras {{v}}",
    hoyTeCuesta: "hoy te cuesta {{v}}",
    badgeMeta: "tu meta",
    badgeDirecta: "la mas directa",
    bloqueadaTitulo: "Vender mas, por ahora, no",
    bloqueadaTexto:
      "<b>Con el margen en rojo, el volumen agranda la pérdida.</b> Primero arregla el margen con la palanca 1 o 2; cuando esté en verde, aquí te diré cuántas necesitas para tu meta.",
    unidadesSufijo: "{{u}}s",
    porUnidad: "por {{u}}",
    acentoMargen: "{{margen}} por {{u}}",
    acentoGanancia: "{{ganancia}} de ganancia",
    tituloSano: "Tres caminos para exprimir estos numeros",
    tituloArreglo: "Tres caminos para que estos numeros funcionen",
  },
  escenarios: {
    escenario: "Escenario",
    ganancia: "Ganancia",
  },
  /** Cada faltante por su clave de campo (la clave es el DATO; esto es su etiqueta). */
  faltantes: {
    costo_materiales_unidad: { texto: "Costo de materiales por unidad", porque: "es la base para saber cuánto te cuesta cada una" },
    horas_por_unidad: { texto: "Tu tiempo por unidad, valorado en dinero", porque: "si te pagaras el rato que tardas, el costo real sube" },
    valor_hora: { texto: "Cuánto vale tu hora de trabajo", porque: "sin ella no se puede poner precio a tu tiempo" },
    precio_tentativo: { texto: "El precio al que vendes", porque: "sin precio no hay margen que calcular" },
    capacidad_semanal: { texto: "Cuántas puedes hacer en una semana", porque: "marca el techo real de lo que alcanzas a producir" },
    costos_fijos_mensuales: { texto: "Tu gasto fijo mensual", porque: "es lo que pagas cada mes vendas o no" },
    unidades_vendidas: { texto: "Cuántas vendes al mes, o tu meta", porque: "sin ella no hay escenarios de venta" },
    precio_pagado_real: { texto: "Lo que de verdad te han pagado", porque: "el precio real puede diferir del que pusiste" },
    dias_inventario: { texto: "Días que tu dinero pasa en inventario", porque: "afecta cuándo vuelve la plata a tu bolsillo" },
    dias_cobro_clientes: { texto: "Días que tardas en cobrar", porque: "cobrar tarde aprieta tu caja" },
    dias_pago_proveedores: { texto: "Días que tardas en pagar a proveedores", porque: "pagar más tarde alivia tu caja" },
  },
  anadir: "Añadir →",
  todoLoEsencial: "Tienes todo lo esencial. Buen trabajo.",
  leyGratis: "Añadir o corregir cifras es gratis, siempre: tu tablero se recalcula al momento.",
  secciones: {
    deUnVistazo: "De un vistazo",
    barraDeLaVerdad: "La barra de la verdad",
    escenarios: "Escenarios, a tu precio de hoy",
    faltantes: "Los números que te faltan",
    cicloDeCaja: "Tu ciclo de caja",
    versionesAnteriores: "Versiones anteriores",
  },
  dias: "días",
  guardianTitulo: "Guardián de datos.",
  guardianTexto:
    "Estos números valen exactamente lo que valen las cifras que metiste. Cuando agregues las que faltan, el número real puede cambiar. No sustituye contabilidad formal ni asesoría fiscal.",
  /** La etiqueta de cada tono del veredicto (el tono es el DATO). */
  tonos: {
    perdida: "pérdida",
    ajuste: "margen delgado",
    sano: "sano",
    datos: "faltan datos",
  },
  ver: "Ver →",
  errorCargar: "no pudimos cargar tus numeros",
  calculando: "Calculando tus números…",
  misIdeas: "Mis ideas /",
  tuIdea: "Tu idea",
  volverAlPlan: "← Volver al plan",
  compuerta: {
    eyebrow: "Tus Números",
    titulo: "Tus cifras reales, convertidas en decisiones",
    texto:
      "Margen, punto de equilibrio, tres palancas calculadas y escenarios, sobre las cifras que tú declares. Vienen incluidos con tu plan. Se activan una vez por idea; corregir cifras y recalcular, cuando quieras.",
    errorActivar: "no pudimos activar Tus Números; intenta de nuevo",
    errorConectar: "no pudimos conectar; revisa tu internet e intenta de nuevo",
    activando: "Activando…",
    sacarConCosto: "Sacar mis números · {{n}} créditos",
    activarIncluido: "Activar mis números · incluido con tu plan",
  },
  insigniaIncluido: "Tus Números · incluido",
  historico: {
    viendo: "Estás viendo tus números del {{momento}}",
    volverAHoy: "Volver a hoy",
  },
  losNumerosDe: "Los números de {{titulo}}",
  tuIdeaMinuscula: "tu idea",
  recienActualizado: "recién actualizado",
  calculadoPorCodigo: "Calculado por código, sobre tus cifras",
  tusNumerosDeHoy: "Tus números de HOY",
  calculadoConCifrasDel: "· calculado con tus cifras del {{sello}}",
  corregirGratis: "Corregir mis cifras · gratis",
};

export const TUS_NUMEROS: PorIdioma<typeof es> = { es };
