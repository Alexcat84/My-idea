/** CorregirCifras: el recolector de las cifras de Tus Números (canon 14). */
import type { PorIdioma } from "../config";

const es = {
  unidadPorDefecto: "unidad",
  /** La etiqueta de cada campo por su clave (la clave es el DATO); {{u}} es la unidad de venta. */
  campos: {
    costo_materiales_unidad: "Costo de materiales por {{u}}",
    horas_por_unidad: "Horas de trabajo por {{u}}",
    valor_hora: "Cuánto vale tu hora",
    precio_tentativo: "Precio al que vendes cada {{u}}",
    capacidad_semanal: "Cuántas {{u}}s haces por semana",
    costos_fijos_mensuales: "Tu gasto fijo mensual",
    unidades_vendidas: "Cuántas {{u}}s vendes al mes (o tu meta)",
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

export const CORREGIR_CIFRAS: PorIdioma<typeof es> = { es };
