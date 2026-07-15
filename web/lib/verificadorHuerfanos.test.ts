// Fase 3.1 (caja de vidrio): paridad de comportamiento contra
// engine/test_verificador_huerfanos.py. Casos mandatados: tolerancia de
// formato (1.700 vs 1700), y un caso sintetico con un numero inyectado
// fuera de material que debe disparar el flag.
import { describe, expect, it } from "vitest";
import {
  cerraduraAritmetica,
  detectarCifrasDeMercado,
  extraerNumeros,
  numerosDeCalculadora,
  numerosDeclarados,
  verificarNumerosHuerfanos,
} from "./verificadorHuerfanos";

describe("detectarCifrasDeMercado (Fase 3.9 D12)", () => {
  it("caza una cifra de tamano de mercado disfrazada en un condicional", () => {
    const texto = "Si en el pais hay 500 auditores certificados activos, el modelo tiene espacio.";
    expect(detectarCifrasDeMercado(texto).map((c) => c.valor)).toContain("500");
  });

  it("no marca un numero de accion legitimo (5 personas, < 20)", () => {
    const texto = "Entrevista a 5 personas de tu publico objetivo esta semana.";
    expect(detectarCifrasDeMercado(texto)).toEqual([]);
  });

  it("no marca la forma correcta: manda a buscar el dato, sin cifra concreta", () => {
    const texto = "Si en tu zona hay X auditores certificados (buscalo en el registro), hay espacio.";
    expect(detectarCifrasDeMercado(texto)).toEqual([]);
  });

  it("emite el evento cifra_mercado_inventada al registrarEvento", () => {
    const eventos: Record<string, unknown>[] = [];
    detectarCifrasDeMercado("En el mercado nacional existen 12000 empresas objetivo.", (e) => eventos.push(e));
    expect(eventos).toContainEqual(expect.objectContaining({ tipo: "cifra_mercado_inventada", valor: "12000" }));
  });
});

describe("tolerancia de formato", () => {
  it("1.700 (miles, estilo hispano) normaliza a 1700", () => {
    expect(extraerNumeros("cuesta 1.700").map((n) => n.valor)).toEqual([1700]);
  });
  it("1,700 (coma de miles) normaliza a 1700", () => {
    expect(extraerNumeros("cuesta 1,700").map((n) => n.valor)).toEqual([1700]);
  });
  it("0.35 (2 decimales) NO se confunde con separador de miles", () => {
    expect(extraerNumeros("presupuesto de 0.35").map((n) => n.valor)).toEqual([0.35]);
  });
  it("17.5 (1 decimal) es un decimal real", () => {
    expect(extraerNumeros("vale 17.5").map((n) => n.valor)).toEqual([17.5]);
  });
  it("$85 y -2976.9% se extraen correctamente", () => {
    const nums = extraerNumeros("vendes a $85 con margen -2976.9%").map((n) => n.valor);
    expect(nums).toEqual([85, -2976.9]);
  });
});

describe("numerosDeCalculadora / numerosDeclarados: extraccion recursiva", () => {
  it("extrae solo los valores numericos hoja, ignora null/arrays/strings", () => {
    const resultadosCalc = {
      margen: { valor: 13, porcentaje: 100.0, insumos_usados: ["a"], insumos_faltantes: [] },
      punto_equilibrio: { valor: 16, insumos_faltantes: [] },
      capacidad: { unidades_mes: null, ingreso: null },
    };
    expect(numerosDeCalculadora(resultadosCalc)).toEqual(new Set([13, 100, 16]));
  });

  it("numerosDeclarados extrae los valores del usuario", () => {
    const numerosProyecto = { precio_tentativo: { valor: 13 }, costos_fijos_mensuales: { valor: 200 } };
    expect(numerosDeclarados(numerosProyecto)).toEqual(new Set([13, 200]));
  });
});

describe("verificarNumerosHuerfanos: caso mandatado (numero inyectado fuera de material)", () => {
  const textoSano =
    "Tu margen por unidad es de $13 (100%). Con costos fijos de $200/mes, tu punto de equilibrio es de 16 unidades/mes.";
  const permitidos = new Set([13, 100, 200, 16]);

  it("un reporte que solo usa numeros permitidos no dispara ningun flag", () => {
    expect(verificarNumerosHuerfanos(textoSano, permitidos)).toEqual([]);
  });

  it("un numero inyectado fuera de material dispara 'numero_huerfano' con su contexto", () => {
    const contaminado = textoSano + " Si escalas, podrias llegar a vender 4500 unidades el proximo trimestre.";
    const eventos: Record<string, unknown>[] = [];
    const huerfanos = verificarNumerosHuerfanos(contaminado, permitidos, (e) => eventos.push(e));
    expect(huerfanos).toHaveLength(1);
    expect(huerfanos[0].valor).toBe("4500");
    expect(eventos).toHaveLength(1);
    expect(eventos[0]).toMatchObject({ tipo: "numero_huerfano", valor: "4500" });
  });
});

describe("bugs reales encontrados en vivo (vuelo.ts fase 3)", () => {
  it("numeros en CLAVES de dict ('50%'/'100%'/'200%' de escenarios_adopcion) tambien se extraen", () => {
    const resultadosConClavesPct = {
      escenarios: {
        "50%": { unidades: 10, ingreso: 130 },
        "100%": { unidades: 20, ingreso: 260 },
        "200%": { unidades: 40, ingreso: 520 },
      },
    };
    const nums = numerosDeCalculadora(resultadosConClavesPct);
    expect(nums.has(50)).toBe(true);
    expect(nums.has(100)).toBe(true);
    expect(nums.has(200)).toBe(true);
  });

  it("cerraduraAritmetica tolera narracion derivada de un paso sin dejar de detectar huerfanos reales", () => {
    const base = new Set([16, 20, 200, 260, 130, 520]);
    const cerradura = cerraduraAritmetica(base);
    expect(cerradura.has(17)).toBe(true); // 16+1 -- "a partir del usuario 17"
    expect(cerradura.has(4)).toBe(true); // 20-16 -- "lo supera por 4"
    expect(cerradura.has(60)).toBe(true); // 260-200 -- "$60 de ganancia"
    expect(cerradura.has(70)).toBe(true); // 200-130 -- "deficit de $70"
    expect(cerradura.has(320)).toBe(true); // 520-200 -- "$320 de ganancia"
    expect(cerradura.has(4500)).toBe(false); // no se vuelve tan laxa que acepte cualquier cosa
  });
});
