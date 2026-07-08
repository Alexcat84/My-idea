// Fase 3.0: paridad de comportamiento contra
// engine/test_reporte_tipo_oferta.py (prueba mandatada 8d de Motor v2.2):
// el guardian GIGO textual debe abortar el molde de preguntas al 2do
// "no aplica", reclasificar tipo_oferta, y continuar con el molde
// correcto -- sin dejar rastro del molde abandonado en numeros_proyecto.
// Mockea solo las dos funciones de ./reporte que llaman a la API
// (clasificarOferta/narrarReporte); todo lo demas (deteccion de "no
// aplica", extraccion de numeros, preguntas por tipo) corre real.
import { beforeEach, describe, expect, it, vi } from "vitest";

const clasificarOfertaFalso = vi.fn();
const narrarReporteFalso = vi.fn();

vi.mock("./reporte", async (importOriginal) => {
  const real = await importOriginal<typeof import("./reporte")>();
  return {
    ...real,
    clasificarOferta: (...args: unknown[]) => clasificarOfertaFalso(...args),
    narrarReporte: (...args: unknown[]) => narrarReporteFalso(...args),
  };
});

import { usoVacio } from "../costmeter";
import { avanzarReporte, iniciarReporte, type EstadoReporte, type ResultadoPasoReporte } from "./reporteFlow";

const acumuladoVacio = usoVacio();

beforeEach(() => {
  clasificarOfertaFalso.mockReset();
  narrarReporteFalso.mockReset();
});

describe("reporteFlow: guardian GIGO textual aborta el molde y reclasifica (mirror de test_reporte_tipo_oferta.py)", () => {
  beforeEach(() => {
    clasificarOfertaFalso.mockResolvedValue({ tipo: "digital", unidad: "suscripcion", acumulado: acumuladoVacio });
    narrarReporteFalso.mockResolvedValue({ contenido: "narracion simulada", acumulado: acumuladoVacio });
  });

  it("consume las 7 respuestas del guion y termina con exactamente los 4 campos digitales, sin rastro del molde fisico", async () => {
    const respuestas = [
      "no tengo piezas, esto no es un producto fisico", // costo_materiales_unidad (fisico)
      "no funciona asi, es una suscripcion digital", // horas_por_unidad (fisico) -> 2do "no aplica"
      "es una app de suscripciones para gestionar pagos recurrentes", // aclaracion
      "200", // costos_fijos_mensuales (digital)
      "0", // costo_materiales_unidad / variable (digital)
      "13", // precio_tentativo (digital)
      "20", // unidades_vendidas / meta (digital)
    ];

    // El proyecto ya tenia el molde 'producto_fisico' asignado de una
    // corrida anterior (simula --reporte ya corrido bajo el default).
    let r: ResultadoPasoReporte = await iniciarReporte(
      {} as never,
      {},
      "producto_fisico",
      "pieza",
      acumuladoVacio
    );
    expect(r.tipo).toBe("pregunta");

    let idx = 0;
    while (r.tipo === "pregunta") {
      const respuesta = respuestas[idx];
      idx++;
      r = await avanzarReporte({} as never, r.estado as EstadoReporte, r.numeros, respuesta, r.acumulado);
    }

    expect(idx).toBe(respuestas.length);
    expect(r.tipo).toBe("reporte_listo");
    if (r.tipo !== "reporte_listo") throw new Error("esperaba reporte_listo");

    const camposDigitalesEsperados = new Set([
      "costos_fijos_mensuales",
      "costo_materiales_unidad",
      "precio_tentativo",
      "unidades_vendidas",
    ]);
    expect(new Set(Object.keys(r.numeros))).toEqual(camposDigitalesEsperados);
    expect(r.numeros.costos_fijos_mensuales.valor).toBe(200);
    expect(r.numeros.costos_fijos_mensuales.unidad).toBe("por mes");
    expect(r.numeros.precio_tentativo.valor).toBe(13);
    expect(r.numeros.unidades_vendidas.valor).toBe(20);
    expect(r.numeros.unidades_vendidas.unidad).toBe("suscripcion/mes");

    // clasificarOferta se llamo dos veces: la aclaracion (reclasifica a
    // digital) es la unica que cambia algo; el resto de las respuestas
    // "no aplica" no dispara clasificacion hasta el 2do conteo.
    expect(clasificarOfertaFalso).toHaveBeenCalledTimes(1);
    expect(narrarReporteFalso).toHaveBeenCalledTimes(1);
  });
});

describe("reporteFlow: sin tipo_oferta previo, pregunta primero que vende", () => {
  it("iniciarReporte sin tipo_oferta pregunta PREGUNTA_TIPO_OFERTA antes que cualquier campo", async () => {
    const r = await iniciarReporte({} as never, {}, null, null, acumuladoVacio);
    expect(r.tipo).toBe("pregunta");
    if (r.tipo !== "pregunta") throw new Error("esperaba pregunta");
    expect(r.estado.fase).toBe("clasificando_oferta");
  });
});

describe("reporteFlow: si ya estan todos los campos esenciales, genera el reporte sin preguntar nada", () => {
  it("con numeros_proyecto completos, iniciarReporte devuelve reporte_listo de inmediato", async () => {
    narrarReporteFalso.mockResolvedValue({ contenido: "reporte narrado", acumulado: acumuladoVacio });
    const numerosCompletos = {
      costo_materiales_unidad: { valor: 68, unidad: "por pieza", texto_original: null, session_id: null, updated_at: null },
      horas_por_unidad: { valor: 0, unidad: "por pieza", texto_original: null, session_id: null, updated_at: null },
      valor_hora: { valor: 0, unidad: "por hora", texto_original: null, session_id: null, updated_at: null },
      precio_tentativo: { valor: 85, unidad: "por pieza", texto_original: null, session_id: null, updated_at: null },
      capacidad_semanal: { valor: 10, unidad: "pieza", texto_original: null, session_id: null, updated_at: null },
      costos_fijos_mensuales: { valor: 200, unidad: "por mes", texto_original: null, session_id: null, updated_at: null },
    };
    const r = await iniciarReporte({} as never, numerosCompletos, "producto_fisico", "pieza", acumuladoVacio);
    expect(r.tipo).toBe("reporte_listo");
    expect(clasificarOfertaFalso).not.toHaveBeenCalled();
  });
});
