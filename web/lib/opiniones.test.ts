// LAS OPINIONES DE LOS USUARIOS (decisión del fundador, 8 oct 2026): cuándo se pregunta, qué se acepta y cómo sale
// el CSV del panel del fundador. Prueba en rojo primero.
//
// Las reglas de frecuencia (REGLAS_FRECUENCIA), escritas antes que el código:
//   · un plan se pregunta UNA vez (respondida o cerrada sin responder, ya no vuelve);
//   · solo si el plan llegó hace 14 días o menos ("al recibirlo", no meses después);
//   · tope: como máximo 2 tarjetas respondidas o cerradas en las últimas 24 horas;
//   · "¿Qué tal va tu idea?" solo si el último plan de la idea tiene 7 días o más, como mucho una vez cada 30 días
//     por idea, y nunca dentro de las 72 horas siguientes a cualquier otra tarjeta.
// Los escenarios usan AHORA = 2026-10-20T12:00Z y cada distancia se calcula a mano en su comentario.
import { describe, expect, it } from "vitest";
import {
  aCsv,
  decidirPregunta,
  numeroDeCiclo,
  REGLAS_FRECUENCIA,
  tipoDePlan,
  validarOpinion,
  type FilaHistorial,
} from "./opiniones";

const AHORA = new Date("2026-10-20T12:00:00Z");
const fila = (tipo: FilaHistorial["tipo"], objeto_id: string | null, created_at: string): FilaHistorial => ({
  tipo,
  objeto_id,
  created_at,
});

describe("las reglas de frecuencia son las acordadas", () => {
  it("14 días de ventana, 2 por día, 7 días de espera, una vez cada 30 días, 72 horas de pausa", () => {
    expect(REGLAS_FRECUENCIA).toEqual({
      ventanaPlanDias: 14,
      topeTarjetasDia: 2,
      seguimientoTrasPlanDias: 7,
      seguimientoCadaDias: 30,
      pausaSeguimientoHoras: 72,
    });
  });
});

describe("¿qué tal salió tu plan? (una vez por plan)", () => {
  const plan = (creadoAt: string) => ({ tipo: "plan" as const, objetoId: "plan-1", creadoAt });

  it("plan de hace 10 días y sin historial: se pregunta", () => {
    // 2026-10-10T12:00 → 2026-10-20T12:00 = 10 días ≤ 14.
    expect(decidirPregunta(plan("2026-10-10T12:00:00Z"), [], AHORA)).toEqual({ preguntar: true });
  });

  it("plan de hace 14 días justos: todavía se pregunta (el borde entra)", () => {
    // 2026-10-06T12:00 → 2026-10-20T12:00 = 14 días exactos ≤ 14.
    expect(decidirPregunta(plan("2026-10-06T12:00:00Z"), [], AHORA).preguntar).toBe(true);
  });

  it("plan de hace 15 días y 1 hora: ya no", () => {
    // 2026-10-05T11:00 → 2026-10-20T12:00 = 15 días + 1 hora > 14.
    expect(decidirPregunta(plan("2026-10-05T11:00:00Z"), [], AHORA)).toEqual({ preguntar: false, razon: "fuera_de_ventana" });
  });

  it("ese plan ya tiene opinión (aunque haya sido cerrar sin responder): no se repite", () => {
    const historial = [fila("plan", "plan-1", "2026-10-11T09:00:00Z")];
    expect(decidirPregunta(plan("2026-10-10T12:00:00Z"), historial, AHORA)).toEqual({ preguntar: false, razon: "ya_respondida" });
  });

  it("dos tarjetas en las últimas 24 horas: tope, no se pregunta", () => {
    // 2026-10-20T01:00 = hace 11 h; 2026-10-19T13:00 = hace 23 h. Las dos < 24 h → 2 ≥ tope 2.
    const historial = [fila("plan_mundo", "plan-a", "2026-10-20T01:00:00Z"), fila("profundizacion", "plan-b", "2026-10-19T13:00:00Z")];
    expect(decidirPregunta(plan("2026-10-19T00:00:00Z"), historial, AHORA)).toEqual({ preguntar: false, razon: "tope_diario" });
  });

  it("una de las dos fue hace 25 horas: solo cuenta una, se pregunta", () => {
    // 2026-10-19T11:00 = hace 25 h (fuera de las 24); 2026-10-20T01:00 = hace 11 h → 1 < 2.
    const historial = [fila("plan_mundo", "plan-a", "2026-10-20T01:00:00Z"), fila("profundizacion", "plan-b", "2026-10-19T11:00:00Z")];
    expect(decidirPregunta(plan("2026-10-19T00:00:00Z"), historial, AHORA).preguntar).toBe(true);
  });

  it("los Comentarios y sugerencias de la cuenta no cuentan para el tope", () => {
    const historial = [fila("general", null, "2026-10-20T10:00:00Z"), fila("general", null, "2026-10-20T11:00:00Z")];
    expect(decidirPregunta(plan("2026-10-19T00:00:00Z"), historial, AHORA).preguntar).toBe(true);
  });
});

describe("¿qué tal va tu idea? (de vez en cuando en el seguimiento)", () => {
  const seg = (ultimoPlanAt: string | null) => ({ tipo: "seguimiento" as const, objetoId: "idea-1", ultimoPlanAt });

  it("sin plan todavía: no", () => {
    expect(decidirPregunta(seg(null), [], AHORA)).toEqual({ preguntar: false, razon: "muy_pronto" });
  });

  it("último plan de hace 6 días: muy pronto", () => {
    // 2026-10-14T12:00 → 6 días < 7.
    expect(decidirPregunta(seg("2026-10-14T12:00:00Z"), [], AHORA)).toEqual({ preguntar: false, razon: "muy_pronto" });
  });

  it("último plan de hace 7 días justos y sin historial: se pregunta", () => {
    // 2026-10-13T12:00 → 7 días exactos ≥ 7.
    expect(decidirPregunta(seg("2026-10-13T12:00:00Z"), [], AHORA)).toEqual({ preguntar: true });
  });

  it("ya se preguntó por esta idea hace 29 días: no", () => {
    // 2026-09-21T12:00 → 2026-10-20T12:00 = 29 días < 30.
    const historial = [fila("seguimiento", "idea-1", "2026-09-21T12:00:00Z")];
    expect(decidirPregunta(seg("2026-09-01T00:00:00Z"), historial, AHORA)).toEqual({ preguntar: false, razon: "reciente" });
  });

  it("se preguntó hace 30 días y 1 hora: vuelve a tocar", () => {
    // 2026-09-20T11:00 → 30 días + 1 hora ≥ 30.
    const historial = [fila("seguimiento", "idea-1", "2026-09-20T11:00:00Z")];
    expect(decidirPregunta(seg("2026-09-01T00:00:00Z"), historial, AHORA).preguntar).toBe(true);
  });

  it("la de otra idea no cuenta para esta", () => {
    const historial = [fila("seguimiento", "idea-2", "2026-10-01T12:00:00Z")];
    expect(decidirPregunta(seg("2026-09-01T00:00:00Z"), historial, AHORA).preguntar).toBe(true);
  });

  it("otra tarjeta hace 71 horas: pausa", () => {
    // 2026-10-17T13:00 → 2026-10-20T12:00 = 71 h < 72.
    const historial = [fila("plan", "plan-9", "2026-10-17T13:00:00Z")];
    expect(decidirPregunta(seg("2026-09-01T00:00:00Z"), historial, AHORA)).toEqual({ preguntar: false, razon: "pausa" });
  });

  it("otra tarjeta hace 73 horas: ya no hay pausa", () => {
    // 2026-10-17T11:00 → 73 h ≥ 72.
    const historial = [fila("plan", "plan-9", "2026-10-17T11:00:00Z")];
    expect(decidirPregunta(seg("2026-09-01T00:00:00Z"), historial, AHORA).preguntar).toBe(true);
  });
});

describe("el tipo lo decide el plan, no el navegador", () => {
  it("primer plan del núcleo, plan de mundo, profundización, replanteamiento; la Claridad no se pregunta", () => {
    expect(tipoDePlan("inicial", "core")).toBe("plan");
    expect(tipoDePlan("completo", "core")).toBe("plan");
    expect(tipoDePlan("inicial", "quality")).toBe("plan_mundo");
    expect(tipoDePlan("seguimiento", "core")).toBe("profundizacion");
    expect(tipoDePlan("seguimiento", "quality")).toBe("profundizacion");
    expect(tipoDePlan("replanteamiento", "franquicias")).toBe("replanteamiento");
    expect(tipoDePlan("organizador", "core")).toBeNull();
    expect(tipoDePlan("reporte_numeros", "core")).toBeNull();
  });
});

describe("lo que se acepta del navegador", () => {
  it("una valoración válida, sin motivo", () => {
    expect(validarOpinion({ valoracion: "bueno" })).toEqual({ ok: true, valoracion: "bueno", motivo: null, texto: null });
  });

  it("malo con motivo y texto (recortado)", () => {
    expect(validarOpinion({ valoracion: "malo", motivo: "confuso", texto: "  no entendí la etapa 3  " })).toEqual({
      ok: true,
      valoracion: "malo",
      motivo: "confuso",
      texto: "no entendí la etapa 3",
    });
  });

  it("cerrar sin responder: todo vacío vale", () => {
    expect(validarOpinion({})).toEqual({ ok: true, valoracion: null, motivo: null, texto: null });
  });

  it("un motivo sin 'malo' se rechaza (la base también lo rechaza)", () => {
    expect(validarOpinion({ valoracion: "bueno", motivo: "confuso" }).ok).toBe(false);
  });

  it("valores inventados y textos de más de 2000 caracteres se rechazan", () => {
    expect(validarOpinion({ valoracion: "regular" }).ok).toBe(false);
    expect(validarOpinion({ valoracion: "malo", motivo: "porque_si" }).ok).toBe(false);
    expect(validarOpinion({ texto: "x".repeat(2001) }).ok).toBe(false);
    expect(validarOpinion({ texto: "x".repeat(2000) }).ok).toBe(true);
  });
});

describe("el CSV del panel", () => {
  it("encabezado fijo, comillas dobladas, saltos de línea dentro de su celda y sin correos", () => {
    const csv = aCsv([
      {
        id: "o1",
        created_at: "2026-10-20T12:00:00Z",
        tipo: "plan",
        valoracion: "malo",
        motivo: "otro",
        texto: 'Dice "rápido"\ny no lo es; escríbeme a ana@example.com',
        idioma: "es",
        proyecto_id: "p1",
        objeto_id: "plan-1",
        contexto: { ciclo: 1, mundo: "core", nodos: ["a", "b"] },
      },
    ]);
    const [cabecera, ...resto] = csv.split("\r\n");
    expect(cabecera).toBe("fecha,tipo,valoracion,motivo,texto,idioma,proyecto,objeto,etiqueta,ciclo,mundo,nodos,id");
    expect(resto.join("\r\n")).toBe(
      '2026-10-20T12:00:00Z,plan,malo,otro,"Dice ""rápido""\ny no lo es; escríbeme a [correo]",es,p1,plan-1,,1,core,a b,o1'
    );
  });

  it("una celda que empieza con = + - @ no se ejecuta como fórmula en la hoja de cálculo", () => {
    const csv = aCsv([
      { id: "o2", created_at: "2026-10-20T12:00:00Z", tipo: "general", valoracion: null, motivo: null, texto: "=HYPERLINK(1)", idioma: "en", proyecto_id: null, objeto_id: null, contexto: {} },
    ]);
    expect(csv.split("\r\n")[1]).toContain(",'=HYPERLINK(1),");
  });
});

describe("la versión del plan es su número de ciclo en su espacio", () => {
  // Núcleo: plan inicial el 1 oct y profundización el 10 oct. Mundo quality: su plan el 5 oct.
  const ciclos = [
    { id: "c1", dominio: "core", created_at: "2026-10-01T00:00:00Z" },
    { id: "m1", dominio: "quality", created_at: "2026-10-05T00:00:00Z" },
    { id: "c2", dominio: "core", created_at: "2026-10-10T00:00:00Z" },
  ];
  it("la profundización del núcleo es el ciclo 2 (c1 antes que ella; el mundo no cuenta)", () => {
    expect(numeroDeCiclo(ciclos, ciclos[2])).toBe(2);
  });
  it("el primer plan del núcleo es el ciclo 1 y el del mundo también (cuentan aparte)", () => {
    expect(numeroDeCiclo(ciclos, ciclos[0])).toBe(1);
    expect(numeroDeCiclo(ciclos, ciclos[1])).toBe(1);
  });
  it("un dominio vacío es el núcleo", () => {
    expect(numeroDeCiclo(ciclos, { id: "c3", dominio: null, created_at: "2026-10-12T00:00:00Z" })).toBe(3);
  });
});
