/**
 * Las condiciones nuevas de la prueba de coherencia (docs/auditoria_final/informes/estado_memoria_contexto.md,
 * encargadas por el fundador): ficha, hilo, continuidad desde el nucleo con todas las respuestas, contexto en cada
 * llamada con lista blanca, las cuatro de cache y la condicion de salida.
 *
 * Las cuentas se hicieron a mano antes de escribir cada assert (AGENTS.md): el valor esperado sale del comentario, no
 * de correr la funcion. Los contextos se arman con el textoContextoProyecto real, para que un cambio de su formato
 * rompa aqui y no en la corrida.
 */
import { describe, expect, it } from "vitest";
import type { RegistroLlamada } from "../costmeter";
import { fichaVacia, textoContextoProyecto, type EntradaHilo, type FichaContexto, type MemoriaProyecto } from "../engine/memoria";
import { PERSONAS, type Dictamen } from "./nucleo";
import {
  COMPONENTES_SIN_CONTEXTO,
  condicionDeSalida,
  estadoVivoDelContexto,
  fichaDelContexto,
  juntar,
  verificarCache,
  verificarContextoPorLlamada,
  verificarContinuidad,
  verificarFicha,
  verificarHilo,
} from "./condiciones";

const SOLA = PERSONAS.find((p) => p.id === "sola")!;
const EMPLEADO = PERSONAS.find((p) => p.id === "empleado_mediana")!;

const fichaCon = (parcial: Partial<FichaContexto>): FichaContexto => ({ ...fichaVacia(), ...parcial });

const entrada = (sesion: string, respuesta: string, en = "2026-10-07T10:00:00Z"): EntradaHilo => ({
  sesion,
  dominio: sesion.startsWith("core") ? "core" : "finanzas",
  nodo: null,
  pregunta: "¿?",
  respuesta,
  en,
});

const contexto = (ficha: FichaContexto, hilo: EntradaHilo[], estadoVivo: string | null) =>
  textoContextoProyecto({ version: 1, ficha, hilo } as MemoriaProyecto, { entradaOriginal: SOLA.idea, estadoVivo });

describe("la ficha: el papel y el jefe del retrato", () => {
  it("cumple si la ficha guardada dice el papel y el jefe de la persona", () => {
    // sola: papel dueno, tiene_jefe false (nucleo.ts)
    expect(verificarFicha(fichaCon({ papel: "dueno", tiene_jefe: false }), SOLA, "tras core").ok).toBe(true);
    // empleado_mediana: papel empleado, tiene_jefe true
    expect(verificarFicha(fichaCon({ papel: "empleado", tiene_jefe: true }), EMPLEADO, "tras core").ok).toBe(true);
  });

  it("falla si el papel es otro o sigue desconocido, y si el jefe no consta", () => {
    const v1 = verificarFicha(fichaCon({ papel: "empleado", tiene_jefe: false }), SOLA, "tras core");
    expect(v1.ok).toBe(false);
    expect(v1.motivos.join(" ")).toContain("papel");
    // la ficha vacia: papel desconocido y tiene_jefe null -> dos motivos
    const v2 = verificarFicha(fichaVacia(), SOLA, "tras core");
    expect(v2.ok).toBe(false);
    expect(v2.motivos).toHaveLength(2);
    // null (no se pudo leer la memoria) no cumple
    expect(verificarFicha(null, SOLA, "tras core").ok).toBe(false);
  });
});

describe("el hilo: las respuestas dadas, en orden, creciendo solo al final", () => {
  const dadas = [
    { sesion: "core-1", respuesta: "Vendo 12 pasteles al mes." },
    { sesion: "core-1", respuesta: "A 45 dólares cada uno." },
  ];
  const hilo = [entrada("core-1", "Vendo 12 pasteles al mes."), entrada("core-1", "A 45 dólares cada uno.")];

  it("cumple si el hilo es exactamente las respuestas dadas, con su sesion y en su orden", () => {
    expect(verificarHilo(null, hilo, dadas, "tras core").ok).toBe(true);
  });

  it("falla si falta una respuesta, si sobra una, si cambia el orden o si una va en otra sesion", () => {
    expect(verificarHilo(null, hilo.slice(0, 1), dadas, "tras core").ok).toBe(false);
    expect(verificarHilo(null, [...hilo, entrada("core-1", "Otra")], dadas, "tras core").ok).toBe(false);
    expect(verificarHilo(null, [hilo[1], hilo[0]], dadas, "tras core").ok).toBe(false);
    expect(verificarHilo(null, [hilo[0], { ...hilo[1], sesion: "mundo-1" }], dadas, "tras core").ok).toBe(false);
  });

  it("crece solo al final: lo de antes tiene que seguir igual, al principio", () => {
    const despues = [...hilo, entrada("mundo-1", "No sé cuánto me cuesta.")];
    const dadasDespues = [...dadas, { sesion: "mundo-1", respuesta: "No sé cuánto me cuesta." }];
    expect(verificarHilo(hilo, despues, dadasDespues, "tras finanzas").ok).toBe(true);
    // si una entrada vieja cambio (aqui su fecha), aunque las respuestas cuadren, no crecio solo al final
    const reescrito = [{ ...hilo[0], en: "2026-10-07T11:00:00Z" }, hilo[1], despues[2]];
    const v = verificarHilo(hilo, reescrito, dadasDespues, "tras finanzas");
    expect(v.ok).toBe(false);
    expect(v.motivos.join(" ")).toContain("al final");
  });
});

describe("lo que se lee del contexto de apertura", () => {
  it("saca el estado vivo y la ficha del texto real de textoContextoProyecto", () => {
    const ctx = contexto(fichaCon({ papel: "dueno", tiene_jefe: false, sector: "repostería" }), [], "Valida precios con 12 clientas.");
    expect(estadoVivoDelContexto(ctx)).toBe("Valida precios con 12 clientas.");
    expect(fichaDelContexto(ctx)).toMatchObject({ papel: "dueno", tiene_jefe: false, sector: "repostería" });
  });

  it("sin estado vivo, o sin contexto, no hay estado vivo que leer", () => {
    expect(estadoVivoDelContexto(contexto(fichaVacia(), [], null))).toBeNull();
    expect(estadoVivoDelContexto(null)).toBeNull();
    expect(fichaDelContexto(null)).toBeNull();
  });

  it("una ficha con llaves y comillas dentro de sus frases se lee igual", () => {
    const ctx = contexto(fichaCon({ papel: "dueno", dijo_textual: ['Le digo "pastel {grande}" al de 2 kilos'] }), [entrada("core-1", "x")], "vivo");
    expect(fichaDelContexto(ctx)?.dijo_textual).toEqual(['Le digo "pastel {grande}" al de 2 kilos']);
  });
});

describe("continuidad: desde el nucleo, con todas las respuestas", () => {
  const nucleo = ["Vendo 12 pasteles al mes.", "A 45 dólares cada uno."];
  const hiloNucleo = nucleo.map((r) => entrada("core-1", r));
  const fichaSola = fichaCon({ papel: "dueno", tiene_jefe: false });

  it("el primer mundo cumple con todas las respuestas del nucleo, el estado vivo y la ficha con el papel", () => {
    const ctx = contexto(fichaSola, hiloNucleo, "Valida precios.");
    const v = verificarContinuidad({ persona: SOLA, de: "core", a: "finanzas", contexto: ctx, respuestasAnterior: nucleo, primerMundo: true, snapshotNucleo: null });
    expect(v).toEqual({ ok: true, motivos: [] });
  });

  it("no basta UNA respuesta del espacio anterior: hacen falta todas", () => {
    const ctx = contexto(fichaSola, hiloNucleo.slice(0, 1), "Valida precios.");
    const v = verificarContinuidad({ persona: SOLA, de: "core", a: "finanzas", contexto: ctx, respuestasAnterior: nucleo, primerMundo: true, snapshotNucleo: null });
    expect(v.ok).toBe(false);
    // falta 1 de 2
    expect(v.motivos.join(" ")).toContain("1 de 2");
  });

  it("en el primer mundo, sin estado vivo o con la ficha sin el papel, no cumple", () => {
    const sinVivo = contexto(fichaSola, hiloNucleo, null);
    expect(verificarContinuidad({ persona: SOLA, de: "core", a: "finanzas", contexto: sinVivo, respuestasAnterior: nucleo, primerMundo: true, snapshotNucleo: null }).ok).toBe(false);
    const sinPapel = contexto(fichaVacia(), hiloNucleo, "Valida precios.");
    const v = verificarContinuidad({ persona: SOLA, de: "core", a: "finanzas", contexto: sinPapel, respuestasAnterior: nucleo, primerMundo: true, snapshotNucleo: null });
    expect(v.ok).toBe(false);
    expect(v.motivos.join(" ")).toContain("papel");
  });

  it("de un mundo al siguiente no se exige el estado vivo (solo en el primero)", () => {
    const ctx = contexto(fichaVacia(), hiloNucleo, null);
    expect(verificarContinuidad({ persona: SOLA, de: "finanzas", a: "marketing", contexto: ctx, respuestasAnterior: nucleo, primerMundo: false, snapshotNucleo: null }).ok).toBe(true);
  });

  it("los mundos de proteccion exigen el snapshot del nucleo; los demas no", () => {
    const ctx = contexto(fichaSola, hiloNucleo, "vivo");
    const base = { persona: SOLA, de: "finanzas", contexto: ctx, respuestasAnterior: nucleo, primerMundo: false };
    expect(verificarContinuidad({ ...base, a: "risk_management", snapshotNucleo: null }).ok).toBe(false);
    expect(verificarContinuidad({ ...base, a: "risk_management", snapshotNucleo: "   " }).ok).toBe(false);
    expect(verificarContinuidad({ ...base, a: "risk_management", snapshotNucleo: "Actividades: hornear" }).ok).toBe(true);
    expect(verificarContinuidad({ ...base, a: "marketing", snapshotNucleo: null }).ok).toBe(true);
  });

  it("sin contexto de apertura no hay continuidad", () => {
    expect(verificarContinuidad({ persona: SOLA, de: "core", a: "finanzas", contexto: null, respuestasAnterior: nucleo, primerMundo: true, snapshotNucleo: null }).ok).toBe(false);
  });

  it("un espacio anterior sin respuestas no tiene nada que arrastrar: no cumple (no hay medicion)", () => {
    const ctx = contexto(fichaSola, hiloNucleo, "vivo");
    expect(verificarContinuidad({ persona: SOLA, de: "finanzas", a: "marketing", contexto: ctx, respuestasAnterior: [], primerMundo: false, snapshotNucleo: null }).ok).toBe(false);
  });
});

const llamada = (parcial: Partial<RegistroLlamada>): RegistroLlamada => ({
  componente: "turnos",
  modelo: "claude-haiku-4-5",
  in: 0,
  out: 0,
  cache_read: 0,
  cache_write_5m: 0,
  cache_write_1h: 0,
  usd: 0,
  stop_reason: "end_turn",
  con_contexto: true,
  ...parcial,
});

describe("contexto en cada llamada, con la lista blanca de los organizadores", () => {
  it("la lista blanca es explicita: solo los organizadores", () => {
    expect([...COMPONENTES_SIN_CONTEXTO]).toEqual(["organizador"]);
  });

  it("cumple si toda llamada fuera de la lista blanca llevo contexto", () => {
    const v = verificarContextoPorLlamada([
      llamada({ componente: "turnos" }),
      llamada({ componente: "adaptador" }),
      llamada({ componente: "organizador", con_contexto: false }),
    ]);
    // 3 llamadas, 2 con contexto, la del organizador esta en la lista blanca
    expect(v).toMatchObject({ ok: true, total: 3, conContexto: 2 });
  });

  it("falla con una llamada sin contexto, o con un registro que no dice si lo llevo", () => {
    const v = verificarContextoPorLlamada([
      llamada({ componente: "turnos", con_contexto: false }),
      llamada({ componente: "diagnostico", con_contexto: undefined }),
      llamada({ componente: "adaptador" }),
    ]);
    expect(v.ok).toBe(false);
    // 2 fuera de regla: turnos y diagnostico
    expect(v.motivos.join(" ")).toContain("2 de 3");
    expect(v.motivos.join(" ")).toContain("turnos");
    expect(v.motivos.join(" ")).toContain("diagnostico");
  });

  it("sin llamadas no hay medicion: no cumple", () => {
    expect(verificarContextoPorLlamada([]).ok).toBe(false);
  });
});

describe("las cuatro condiciones de cache", () => {
  // A mano, Haiku (1 USD entrada / 5 USD salida por millon; lectura 0.1x, escritura 1h 2x):
  //  A (primer turno): in 1000, escritura 1h 4000, out 100
  //    con cache = 1000*1 + 4000*2 + 100*5   = 1000 + 8000 + 500 = 9500 -> 0.0095 USD
  //    sin cache = (1000+4000)*1 + 100*5     = 5000 + 500        = 5500 -> 0.0055 USD
  //  B (segundo turno): in 1000, lectura 4000, out 100
  //    con cache = 1000*1 + 4000*0.1 + 100*5 = 1000 + 400 + 500  = 1900 -> 0.0019 USD
  //    sin cache = (1000+4000)*1 + 100*5     = 5500              -> 0.0055 USD
  //  C igual que B.
  //  ahorro(A,B)   = (0.0055+0.0055) - (0.0095+0.0019) = 0.0110 - 0.0114 = -0.0004 (el cache costo mas)
  //  ahorro(A,B,C) = 0.0165 - 0.0133 = +0.0032
  //  turno medio (A,B,C) = 0.0133 / 3 = 0.004433... USD
  //  antes (vuelo del 27 sep) = 0.1352039 / 13 = 0.0104003 USD -> ahora es mas barato
  const A = llamada({ in: 1000, cache_write_1h: 4000, out: 100, usd: 0.0095 });
  const B = llamada({ in: 1000, cache_read: 4000, out: 100, usd: 0.0019 });
  const C = llamada({ in: 1000, cache_read: 4000, out: 100, usd: 0.0019 });
  const ANTES = 0.1352039 / 13;

  it("cumple las cuatro con un cache que acierta", () => {
    const v = verificarCache([{ persona: "sola", sesion: "s1", llamadas: [A, B, C] }], ["sola"], ANTES);
    expect(v.ok).toBe(true);
    expect(v.ahorro).toBeCloseTo(0.0032, 10);
    expect(v.turnoAhoraUsd).toBeCloseTo(0.0133 / 3, 10);
  });

  it("1: el ahorro tiene que ser mayor que 0", () => {
    const v = verificarCache([{ persona: "sola", sesion: "s1", llamadas: [A, B] }], ["sola"], ANTES);
    expect(v.ahorro).toBeCloseTo(-0.0004, 10);
    expect(v.ok).toBe(false);
    expect(v.motivos.join(" ")).toContain("ahorro");
  });

  it("2: una sesion con 2 o mas turnos del interprete sin ninguna lectura de cache no cumple", () => {
    // s2: dos turnos sin lectura (A y A'), aunque s1 acierte y el total ahorre
    // ahorro = 0.0032 (s1) + 2 * (0.0055 - 0.0095) = 0.0032 - 0.008 < 0 -> tambien falla el 1; se mira el motivo del 2
    const v = verificarCache(
      [
        { persona: "sola", sesion: "s1", llamadas: [A, B, C] },
        { persona: "sola", sesion: "s2", llamadas: [A, { ...A }] },
      ],
      ["sola"],
      ANTES
    );
    expect(v.ok).toBe(false);
    expect(v.motivos.join(" ")).toContain("s2");
  });

  it("2: una sesion de un solo turno del interprete no necesita leer", () => {
    // s2: un solo turno (B, que no escribe ni lee nada relevante para el 2) -> no se le exige lectura
    const solo = llamada({ in: 1000, out: 100, usd: 0.0015 });
    const v = verificarCache(
      [
        { persona: "sola", sesion: "s1", llamadas: [A, B, C] },
        { persona: "sola", sesion: "s2", llamadas: [solo, llamada({ componente: "adaptador", in: 10, usd: 0.00001 })] },
      ],
      ["sola"],
      ANTES
    );
    expect(v.motivos.join(" ")).not.toContain("s2");
  });

  it("3: cada persona necesita al menos una escritura de 1 hora", () => {
    // dos_empleados solo tiene lecturas (B, C): sin escritura de 1 h
    const v = verificarCache(
      [
        { persona: "sola", sesion: "s1", llamadas: [A, B, C] },
        { persona: "dos_empleados", sesion: "s2", llamadas: [{ ...B }, { ...C }] },
      ],
      ["sola", "dos_empleados"],
      ANTES
    );
    expect(v.ok).toBe(false);
    expect(v.motivos.join(" ")).toContain("dos_empleados");
    // y una persona sin ninguna sesion medida tampoco cumple
    expect(verificarCache([{ persona: "sola", sesion: "s1", llamadas: [A, B, C] }], ["sola", "empleado_mediana"], ANTES).ok).toBe(false);
  });

  it("4: el turno del interprete tiene que salir mas barato que antes", () => {
    // con la vara en 0.004 USD, el medio 0.004433 ya no es mas barato
    const v = verificarCache([{ persona: "sola", sesion: "s1", llamadas: [A, B, C] }], ["sola"], 0.004);
    expect(v.ok).toBe(false);
    expect(v.motivos.join(" ")).toContain("turno del interprete");
    // sin turnos del interprete no hay medicion
    const sinTurnos = verificarCache([{ persona: "sola", sesion: "s1", llamadas: [{ ...A, componente: "plan" }] }], ["sola"], ANTES);
    expect(sinTurnos.ok).toBe(false);
    expect(sinTurnos.turnoAhoraUsd).toBeNull();
  });
});

describe("la condicion de salida", () => {
  const bien = { ok: true, motivos: [] };
  const dictamenBien: Dictamen = { cumple: true, motivos: [] };

  it("dictamen && continuidad && ficha && hilo && contexto && cache", () => {
    expect(condicionDeSalida({ dictamen: dictamenBien, continuidad: bien, ficha: bien, hilo: bien, contexto: bien, cache: bien })).toEqual({ cumple: true, motivos: [] });
    for (const clave of ["continuidad", "ficha", "hilo", "contexto", "cache"] as const) {
      const r = condicionDeSalida({ dictamen: dictamenBien, continuidad: bien, ficha: bien, hilo: bien, contexto: bien, cache: bien, [clave]: { ok: false, motivos: ["x"] } });
      expect(r.cumple).toBe(false);
      expect(r.motivos.join(" ")).toContain(clave);
    }
    const r = condicionDeSalida({ dictamen: { cumple: false, motivos: ["1 desajuste(s) de papel (umbral 0)"] }, continuidad: bien, ficha: bien, hilo: bien, contexto: bien, cache: bien });
    expect(r).toEqual({ cumple: false, motivos: ["juez: 1 desajuste(s) de papel (umbral 0)"] });
  });

  it("juntar: todos ok, o los motivos de todos; sin nada que juntar no hay medicion", () => {
    expect(juntar([bien, bien])).toEqual(bien);
    expect(juntar([{ ok: false, motivos: ["a"] }, bien, { ok: false, motivos: ["b"] }])).toEqual({ ok: false, motivos: ["a", "b"] });
    expect(juntar([]).ok).toBe(false);
  });
});
