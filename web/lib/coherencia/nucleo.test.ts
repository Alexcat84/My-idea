/**
 * La parte pura de la prueba de coherencia (construccion 7). Las cuentas se hicieron a mano antes de escribir cada
 * assert (AGENTS.md): el valor esperado sale del comentario, no de correr la funcion.
 */
import { describe, expect, it } from "vitest";
import {
  PERSONAS,
  TRAMPAS,
  ahorroCache,
  arrastraLoAnterior,
  construirLote,
  contar,
  dictaminar,
  leerVeredictos,
  pedidoAlJuez,
  SYSTEM_JUEZ_COHERENCIA,
  sumarMetricas,
  type ClaveItem,
  type Metricas,
  type VeredictoItem,
} from "./nucleo";

const vacias: Metricas = {
  preguntasReales: 0, desajustesPapel: 0, desajustesContexto: 0, adaptadasReales: 0, adaptadasFieles: 0,
  trampas: 0, trampasCazadas: 0, sinVeredicto: [],
};

describe("las personas y las trampas, fijadas antes de la corrida", () => {
  it("tres personas: sola, con dos empleados, y empleado de una empresa mediana con jefe", () => {
    expect(PERSONAS.map((p) => p.id)).toEqual(["sola", "dos_empleados", "empleado_mediana"]);
    expect(PERSONAS.map((p) => p.ficha.tiene_jefe)).toEqual([false, false, true]);
  });

  it("cada persona tiene sus trampas de papel, de contexto y de fidelidad (12 en total)", () => {
    // 3 personas x (2 de papel + 1 de contexto + 1 de fidelidad) = 3 x 4 = 12
    expect(TRAMPAS).toHaveLength(12);
    for (const p of PERSONAS) {
      const suyas = TRAMPAS.filter((t) => t.persona === p.id).map((t) => t.tipo).sort();
      expect(suyas).toEqual(["contexto", "fidelidad", "papel", "papel"]);
    }
    expect(TRAMPAS.filter((t) => t.tipo === "fidelidad").every((t) => t.base)).toBe(true);
  });
});

describe("construirLote: ciego y reproducible", () => {
  const reales = [
    { sesion: "s1", espacio: "core", pregunta: "¿Cuánto vendes al mes?" },
    { sesion: "s1", espacio: "core", pregunta: "¿Cuánto te cuesta un pastel?", base: "¿Cuánto cuesta producir una unidad?" },
  ];

  it("mezcla las reales con las trampas de ESA persona, con ids opacos, y la misma semilla da el mismo orden", () => {
    const a = construirLote("sola", reales);
    const b = construirLote("sola", reales);
    // 2 reales + 4 trampas de 'sola' = 6
    expect(a.items).toHaveLength(6);
    expect(a.items.map((i) => i.id)).toEqual(["p1", "p2", "p3", "p4", "p5", "p6"]);
    expect(a).toEqual(b);
    expect(a.clave.filter((c) => c.origen === "trampa")).toHaveLength(4);
    // lo que viaja al juez no dice que es trampa
    expect(JSON.stringify(a.items)).not.toMatch(/trampa|origen|real/);
    // la adaptada lleva su base
    const conBase = a.items.find((i) => i.pregunta === "¿Cuánto te cuesta un pastel?")!;
    expect(conBase.base).toBe("¿Cuánto cuesta producir una unidad?");
  });

  it("otra semilla da otro orden", () => {
    const a = construirLote("sola", reales, TRAMPAS, 1).items.map((i) => i.pregunta);
    const b = construirLote("sola", reales, TRAMPAS, 2).items.map((i) => i.pregunta);
    expect(a).not.toEqual(b);
  });
});

describe("contar y dictaminar contra el umbral del fundador", () => {
  const clave: ClaveItem[] = [
    { id: "p1", origen: "real", espacio: "core", adaptada: false },
    { id: "p2", origen: "real", espacio: "core", adaptada: true },
    { id: "p3", origen: "trampa", tipoTrampa: "papel", adaptada: false },
    { id: "p4", origen: "trampa", tipoTrampa: "fidelidad", adaptada: true },
    { id: "p5", origen: "trampa", tipoTrampa: "contexto", adaptada: false },
  ];

  it("todo bien y todas las trampas cazadas: cumple", () => {
    const v: VeredictoItem[] = [
      { id: "p1", papel: "ok", contexto: "ok", fiel: null },
      { id: "p2", papel: "ok", contexto: "ok", fiel: "si" },
      { id: "p3", papel: "desajuste", contexto: "ok", fiel: null },
      { id: "p4", papel: "ok", contexto: "ok", fiel: "no" },
      { id: "p5", papel: "ok", contexto: "desajuste", fiel: null },
    ];
    // A mano: 2 reales, 0 papel, 0 contexto, 1 adaptada y 1 fiel; 3 trampas y 3 cazadas.
    const m = contar(v, clave);
    expect(m).toEqual({ ...vacias, preguntasReales: 2, adaptadasReales: 1, adaptadasFieles: 1, trampas: 3, trampasCazadas: 3 });
    expect(dictaminar(m)).toEqual({ cumple: true, motivos: [] });
  });

  it("una trampa sin cazar o una real sin veredicto hacen fallar", () => {
    const v: VeredictoItem[] = [
      { id: "p2", papel: "ok", contexto: "ok", fiel: "si" },
      { id: "p3", papel: "ok", contexto: "ok", fiel: null }, // trampa de papel NO cazada
      { id: "p4", papel: "ok", contexto: "ok", fiel: "no" },
      { id: "p5", papel: "desajuste", contexto: "ok", fiel: null }, // contexto cazado por papel: vale
    ];
    // A mano: p1 sin veredicto -> cuenta como 1 desajuste de papel; trampas 3, cazadas 2 (p4, p5).
    const m = contar(v, clave);
    expect(m.desajustesPapel).toBe(1);
    expect(m.sinVeredicto).toEqual(["p1"]);
    expect(m.trampasCazadas).toBe(2);
    const d = dictaminar(m);
    expect(d.cumple).toBe(false);
    expect(d.motivos).toEqual(["1 desajuste(s) de papel (umbral 0)", "2 de 3 trampas cazadas (umbral todas)"]);
  });

  it("contexto: 1 por cada 10 preguntas es el tope; fidelidad: el 95 %", () => {
    // 20 preguntas y 2 de contexto: 2 x 10 = 20 <= 20, cumple. 3 de contexto: 30 > 20, no.
    const base = { ...vacias, preguntasReales: 20, adaptadasReales: 20, adaptadasFieles: 19 };
    expect(dictaminar({ ...base, desajustesContexto: 2 }).cumple).toBe(true);
    expect(dictaminar({ ...base, desajustesContexto: 3 }).motivos).toEqual(["3 desajuste(s) de contexto en 20 preguntas (umbral 1 por cada 10)"]);
    // 19 de 20 = 95 %: cumple. 18 de 20 = 90 %: no.
    expect(dictaminar({ ...base, adaptadasFieles: 18 }).motivos).toEqual(["18 de 20 adaptadas fieles (umbral 95 %)"]);
  });

  it("sin preguntas reales no hay medicion", () => {
    expect(dictaminar(vacias).cumple).toBe(false);
  });

  it("sumarMetricas suma campo a campo", () => {
    const a = { ...vacias, preguntasReales: 3, trampas: 4, trampasCazadas: 4, sinVeredicto: ["x"] };
    const b = { ...vacias, preguntasReales: 5, desajustesContexto: 1, trampas: 4, trampasCazadas: 3 };
    expect(sumarMetricas([a, b])).toEqual({ ...vacias, preguntasReales: 8, desajustesContexto: 1, trampas: 8, trampasCazadas: 7, sinVeredicto: ["x"] });
  });
});

describe("ahorroCache", () => {
  it("una lectura de 1000 tokens en Haiku ahorra el 90 % de su entrada", () => {
    // A mano (Haiku, 1 USD por millon de entrada): con cache = (100 + 1000 x 0,1) / 1e6 = 0,0002;
    // sin cache = (100 + 1000) / 1e6 = 0,0011; ahorro = 0,0009.
    const r = ahorroCache([
      { componente: "turnos", modelo: "claude-haiku-4-5", in: 100, out: 0, cache_read: 1000, cache_write_5m: 0, cache_write_1h: 0, usd: 0, stop_reason: null },
    ]);
    expect(r.conCache).toBeCloseTo(0.0002, 10);
    expect(r.sinCache).toBeCloseTo(0.0011, 10);
    expect(r.ahorro).toBeCloseTo(0.0009, 10);
  });

  it("una escritura de 1 hora sin lecturas cuesta mas que no cachear", () => {
    // A mano: con cache = 1000 x 2 / 1e6 = 0,002; sin cache = 1000 / 1e6 = 0,001; ahorro = -0,001.
    const r = ahorroCache([
      { componente: "turnos", modelo: "claude-haiku-4-5", in: 0, out: 0, cache_read: 0, cache_write_5m: 0, cache_write_1h: 1000, usd: 0, stop_reason: null },
    ]);
    expect(r.ahorro).toBeCloseTo(-0.001, 10);
  });
});

describe("mundo tras mundo", () => {
  it("el contexto del siguiente espacio trae lo que la persona conto en el anterior", () => {
    const ctx = "CONTEXTO DEL PROYECTO\n- [primer_equipo] P: ¿Qué esperas de Rosa? R: Que llegue a las ocho y deje listo el molde.";
    expect(arrastraLoAnterior(ctx, ["Que llegue a las ocho y deje listo el molde."])).toBe(true);
    expect(arrastraLoAnterior(ctx, ["Otra cosa que nunca dijo."])).toBe(false);
    expect(arrastraLoAnterior(null, ["x"])).toBe(false);
  });
});

describe("el juez", () => {
  it("su rubrica lleva el criterio de papeles (regla de la casa 5) y la regla unica", () => {
    expect(SYSTEM_JUEZ_COHERENCIA).toContain("un jefe");
    expect(SYSTEM_JUEZ_COHERENCIA).toContain("recursos humanos");
    expect(SYSTEM_JUEZ_COHERENCIA).toContain("CONTEXTO REAL DE LA PERSONA");
  });

  it("recibe la ficha verdadera y las preguntas, nunca la clave", () => {
    const { items } = construirLote("sola", []);
    const pedido = JSON.parse(pedidoAlJuez(PERSONAS[0], items));
    expect(pedido.ficha_verdadera.tiene_jefe).toBe(false);
    expect(pedido.preguntas).toHaveLength(4);
    expect(Object.keys(pedido)).toEqual(["ficha_verdadera", "preguntas"]);
  });

  it("leerVeredictos descarta lo que no tiene forma valida", () => {
    const texto = 'Aquí va: [{"id":"p1","papel":"ok","contexto":"ok","fiel":null},{"id":"p2","papel":"quizas","contexto":"ok","fiel":null}]';
    expect(leerVeredictos(texto)).toEqual([{ id: "p1", papel: "ok", contexto: "ok", fiel: null }]);
    expect(leerVeredictos("no hay json")).toEqual([]);
  });
});
