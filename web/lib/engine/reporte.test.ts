import { describe, expect, it } from "vitest";
import {
  camposEsencialesPorTipo,
  detectarNoAplica,
  extraerNumero,
  preguntasPorTipo,
  reporteGigoInconsistente,
  reporteOffline,
  unidadDeclaradaCampo,
} from "./reporte";

describe("extraerNumero", () => {
  it("extrae numeros en distintos formatos de lenguaje natural", () => {
    expect(extraerNumero("$8")).toBe(8);
    expect(extraerNumero("8 dolares")).toBe(8);
    expect(extraerNumero("8.5")).toBe(8.5);
    expect(extraerNumero("unos 8")).toBe(8);
    expect(extraerNumero("200")).toBe(200);
  });

  it("trata las comas como separador de miles, no decimal", () => {
    expect(extraerNumero("1,200")).toBe(1200);
  });

  it("devuelve null si el usuario dice que no sabe", () => {
    expect(extraerNumero("no se")).toBeNull();
    expect(extraerNumero("no sé")).toBeNull();
    expect(extraerNumero("ni idea")).toBeNull();
  });

  it("devuelve null si no hay ningun numero reconocible", () => {
    expect(extraerNumero("")).toBeNull();
    expect(extraerNumero("no tengo piezas")).toBeNull();
  });
});

describe("detectarNoAplica", () => {
  it("detecta las frases del guardian GIGO (Motor v2.2)", () => {
    expect(detectarNoAplica("no tengo piezas, esto no es un producto fisico")).toBe(true);
    expect(detectarNoAplica("no funciona asi, es una suscripcion digital")).toBe(true);
    expect(detectarNoAplica("Es Una Suscripción")).toBe(true);
  });

  it("no marca una respuesta numerica normal como 'no aplica'", () => {
    expect(detectarNoAplica("200")).toBe(false);
    expect(detectarNoAplica("cobro 68 por pieza")).toBe(false);
  });
});

describe("unidadDeclaradaCampo", () => {
  it("costos_fijos_mensuales siempre es 'por mes'", () => {
    expect(unidadDeclaradaCampo("costos_fijos_mensuales", "producto_fisico", "pieza")).toBe("por mes");
  });

  it("valor_hora siempre es 'por hora'", () => {
    expect(unidadDeclaradaCampo("valor_hora", "servicio", "sesion")).toBe("por hora");
  });

  it("unidades_vendidas es '{unidad}/mes' para digital, la unidad plana para el resto", () => {
    expect(unidadDeclaradaCampo("unidades_vendidas", "digital", "suscripcion")).toBe("suscripcion/mes");
    expect(unidadDeclaradaCampo("unidades_vendidas", "producto_fisico", "pieza")).toBe("pieza");
  });

  it("el resto de los campos es 'por {unidad}'", () => {
    expect(unidadDeclaradaCampo("costo_materiales_unidad", "producto_fisico", "pieza")).toBe("por pieza");
    expect(unidadDeclaradaCampo("precio_tentativo", "producto_fisico", null)).toBe("por unidad");
  });
});

describe("camposEsencialesPorTipo / preguntasPorTipo", () => {
  it("digital pide solo 4 campos, sin horas/valor_hora", () => {
    const campos = camposEsencialesPorTipo("digital");
    expect(campos).toEqual(["costos_fijos_mensuales", "costo_materiales_unidad", "precio_tentativo", "unidades_vendidas"]);
    const preguntas = preguntasPorTipo("digital", "usuario");
    expect(Object.keys(preguntas).sort()).toEqual([...campos].sort());
    expect(preguntas.horas_por_unidad).toBeUndefined();
  });

  it("producto_fisico y servicio piden los mismos 6 campos", () => {
    expect(camposEsencialesPorTipo("producto_fisico")).toEqual(camposEsencialesPorTipo("servicio"));
  });

  it("tipo_oferta desconocido o null cae al default de producto_fisico", () => {
    expect(camposEsencialesPorTipo(null)).toEqual(camposEsencialesPorTipo("producto_fisico"));
    expect(camposEsencialesPorTipo("algo_no_reconocido")).toEqual(camposEsencialesPorTipo("producto_fisico"));
  });
});

describe("reporteGigoInconsistente", () => {
  it("nunca calcula margen ni equilibrio, solo muestra los numeros crudos declarados", () => {
    const md = reporteGigoInconsistente("el margen da -2976.9%, algo esta mal", {
      costo_materiales_unidad: { valor: 200, unidad: "por mes", texto_original: null, session_id: null, updated_at: null },
      precio_tentativo: { valor: 13, unidad: "por pack", texto_original: null, session_id: null, updated_at: null },
    });
    expect(md).toContain("-2976.9%");
    expect(md).toContain("costo_materiales_unidad: 200");
    expect(md).toContain("precio_tentativo: 13");
    expect(md).not.toContain("punto de equilibrio: ");
  });
});

describe("reporteOffline", () => {
  it("lista los numeros calculados disponibles y los insumos_faltantes", () => {
    const md = reporteOffline({
      costo_unitario: { valor: 68, insumos_usados: [], insumos_faltantes: [] },
      margen: { valor: 17, porcentaje: 20, insumos_usados: [], insumos_faltantes: [] },
      punto_equilibrio: { valor: 12, insumos_usados: [], insumos_faltantes: [] },
      capacidad: { unidades_mes: null, ingreso: null, margen_mensual: null, insumos_usados: [], insumos_faltantes: ["capacidad_semanal"] },
      ciclo_conversion_efectivo: { valor: null, insumos_usados: [], insumos_faltantes: ["dias_inventario", "dias_cobro_clientes", "dias_pago_proveedores"] },
      escenarios: { insumos_usados: [], insumos_faltantes: [] } as never,
    });
    expect(md).toContain("Costo por unidad: 68");
    expect(md).toContain("Margen por unidad: 17 (20%)");
    expect(md).toContain("Punto de equilibrio: 12 unidades/mes");
    expect(md).toContain("capacidad_semanal");
  });
});
