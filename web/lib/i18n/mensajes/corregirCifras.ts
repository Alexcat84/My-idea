/** CorregirCifras: el recolector de las cifras de Tus Números (canon 14). */
import type { PorIdioma } from "../config";

const es = {
  unidadPorDefecto: "unidad",
  /** La etiqueta de cada campo por su clave (la clave es el DATO); {{u}} es la unidad de venta y {{unidades}} su plural. */
  campos: {
    costo_materiales_unidad: "Costo de materiales por {{u}}",
    horas_por_unidad: "Horas de trabajo por {{u}}",
    valor_hora: "Cuánto vale tu hora",
    precio_tentativo: "Precio al que vendes cada {{u}}",
    capacidad_semanal: "Número de {{unidades}} que haces por semana",
    costos_fijos_mensuales: "Tu gasto fijo mensual",
    unidades_vendidas: "Número de {{unidades}} que vendes al mes (o tu meta)",
    dias_inventario: "Días que tu dinero pasa en inventario",
    dias_cobro_clientes: "Días que tardas en cobrar",
    dias_pago_proveedores: "Días que tardas en pagar a proveedores",
  },
  /** Por qué importa cada dato del ciclo de caja. */
  porque: {
    dias_inventario: "afecta cuándo vuelve la plata a tu bolsillo",
    dias_cobro_clientes: "cobrar tarde aprieta tu caja",
    dias_pago_proveedores: "pagar más tarde alivia tu caja",
  },
  errorNumero: 'Revisa "{{campo}}": debe ser un número de 0 en adelante.',
  errorGuardar: "no pudimos guardar tus cifras",
  errorConectar: "no pudimos conectar; revisa tu internet e intenta de nuevo",
  titulo: "Corrige tus cifras",
  intro:
    "Ajusta lo que cambió y vuelve a calcular. El recálculo es gratis e ilimitado; tus versiones anteriores quedan guardadas con su fecha.",
  cicloTitulo: "Tu ciclo de caja (opcional)",
  cicloIntro: "Si los tienes, afinan tu foto de caja; si no, sigue sin ellos.",
  calculando: "Calculando…",
  volverACalcular: "Volver a calcular",
  cancelar: "Cancelar",
};

const en: typeof es = {
  unidadPorDefecto: "unit",
  campos: {
    costo_materiales_unidad: "Material cost per {{u}}",
    horas_por_unidad: "Hours of work per {{u}}",
    valor_hora: "What an hour of your time is worth",
    precio_tentativo: "Price you sell each {{u}} for",
    capacidad_semanal: "Number of {{unidades}} you make per week",
    costos_fijos_mensuales: "Your monthly fixed costs",
    unidades_vendidas: "Number of {{unidades}} you sell per month (or your goal)",
    dias_inventario: "Days your money sits in inventory",
    dias_cobro_clientes: "Days it takes you to get paid",
    dias_pago_proveedores: "Days you take to pay your suppliers",
  },
  porque: {
    dias_inventario: "it affects when the money comes back to your pocket",
    dias_cobro_clientes: "getting paid late squeezes your cash",
    dias_pago_proveedores: "paying later eases your cash",
  },
  errorNumero: 'Check "{{campo}}": it has to be a number, 0 or higher.',
  errorGuardar: "we couldn't save your figures",
  errorConectar: "we couldn't connect; check your internet and try again",
  titulo: "Correct your figures",
  intro:
    "Adjust what changed and recalculate. Recalculating is free and unlimited; your earlier versions stay saved with their date.",
  cicloTitulo: "Your cash cycle (optional)",
  cicloIntro: "If you have them, they sharpen your cash picture; if not, carry on without them.",
  calculando: "Calculating…",
  volverACalcular: "Recalculate",
  cancelar: "Cancel",
};

export const CORREGIR_CIFRAS: PorIdioma<typeof es> = { es, en };
