/**
 * CONSTRUCCION 2 (decision del fundador, 28 sep 2026): el ADAPTADOR de preguntas. Toda pregunta que va a salir de la
 * cache (o la generica de un nodo sin pregunta) pasa por Haiku, que la dice a ESTA persona y en su idioma: cambia la
 * forma, nunca el fondo. Si falla, tarda o devuelve algo que no pasa las comprobaciones, sale la version NEUTRAL de la
 * cache, nunca la base cruda (mientras un nodo no tenga neutral, sale la base y el evento lo dice).
 *
 * Todo con clientes falsos: ninguna llamada a la API real hasta la corrida final (regla del fundador, 28 sep 2026).
 */
import { describe, expect, it, vi } from "vitest";
import type Anthropic from "@anthropic-ai/sdk";
import { adaptarPregunta, adaptarResultadoTurno, comprobarAdaptada } from "./adaptadorPregunta";
import { MODEL_HAIKU, usoVacio } from "../costmeter";
import { SYSTEM_ADAPTAR_PREGUNTA } from "../prompts";
import type { Grafo, PreguntasCache } from "./graph";
import type { EventoInterprete } from "./interprete";

const BASE = "¿Qué le dirías a tu propio jefe si te pide un informe de avance?";
const NEUTRAL = "¿Qué le contarías a quien sigue tu avance si te pide un informe?";

function clienteFalso(respuesta: string | Error) {
  const create = vi.fn(async (_req: unknown) => {
    if (respuesta instanceof Error) throw respuesta;
    return { usage: { input_tokens: 500, output_tokens: 80 }, stop_reason: "end_turn", content: [{ type: "text", text: respuesta }] };
  });
  return { client: { messages: { create } } as unknown as Anthropic, create };
}

const json = (pregunta: string, busca = "a quien rinde cuentas y que le cuenta") => JSON.stringify({ pregunta, busca });

/** El texto del turno que recibio el falso: sin contexto, el content es texto; con contexto, el ultimo bloque. */
function turnoEnviado(create: ReturnType<typeof vi.fn>): { pregunta_base: string; sirve_para_elegir_entre: string[] } {
  const content = (create.mock.calls[0][0] as { messages: Array<{ content: string | Array<{ text: string }> }> }).messages[0].content;
  return JSON.parse(typeof content === "string" ? content : content[content.length - 1].text);
}

describe("comprobarAdaptada: lo que el codigo exige antes de mostrar una adaptada", () => {
  it("una pregunta con su 'busca' pasa", () => {
    expect(comprobarAdaptada(BASE, json("¿A quién le cuentas cómo va tu taller?"))).toEqual({
      ok: true,
      pregunta: "¿A quién le cuentas cómo va tu taller?",
      busca: "a quien rinde cuentas y que le cuenta",
    });
  });

  it("acepta el JSON envuelto en un bloque de codigo", () => {
    const r = comprobarAdaptada(BASE, "```json\n" + json("¿A quién le cuentas cómo va?") + "\n```");
    expect(r.ok).toBe(true);
  });

  it("acepta los signos de pregunta de japones, chino y arabe", () => {
    expect(comprobarAdaptada(BASE, json("進捗は誰に報告していますか？")).ok).toBe(true);
    expect(comprobarAdaptada(BASE, json("لمن تقدم تقريرا عن تقدمك؟")).ok).toBe(true);
  });

  it.each([
    ["no es JSON", "¿A quién le cuentas?", "no_json"],
    ["sin signo de pregunta", json("Cuéntame a quién le rindes cuentas."), "no_es_pregunta"],
    ["con guion largo", json("¿A quién le cuentas — si hay alguien — cómo va?"), "guion_largo"],
    ["sin busca", JSON.stringify({ pregunta: "¿A quién le cuentas?", busca: " " }), "sin_busca"],
    ["pregunta vacia", JSON.stringify({ pregunta: "", busca: "x" }), "vacia"],
  ])("%s: no pasa (%s)", (_n, salida, motivo) => {
    expect(comprobarAdaptada(BASE, salida)).toEqual({ ok: false, motivo });
  });

  it("demasiado larga: mas de max(2 x base, base + 200) caracteres", () => {
    // La base mide 64 caracteres: max(2 x 64, 64 + 200) = max(128, 264) = 264.
    expect(BASE.length).toBe(64);
    const de264 = "¿" + "a".repeat(262) + "?"; // 1 + 262 + 1 = 264: pasa
    const de265 = "¿" + "a".repeat(263) + "?"; // 265: no pasa
    expect(comprobarAdaptada(BASE, json(de264)).ok).toBe(true);
    expect(comprobarAdaptada(BASE, json(de265))).toEqual({ ok: false, motivo: "demasiado_larga" });
  });
});

describe("adaptarPregunta: la llamada", () => {
  const entrada = { nodo: "n1", base: BASE, neutral: NEUTRAL, siguientes: ["Cuenta cómo vas", "Pide ayuda a tiempo"] };

  it("va a Haiku con el prompt del adaptador, el contexto en su bloque de 1 hora y la base con sus siguientes", async () => {
    const { client, create } = clienteFalso(json("¿A quién le cuentas cómo va tu taller?"));
    const r = await adaptarPregunta(client, entrada, usoVacio(), { idiomaSalida: "es", contexto: "CONTEXTO DEL PROYECTO\nDueña de un taller" });
    expect(r).toMatchObject({ pregunta: "¿A quién le cuentas cómo va tu taller?", busca: "a quien rinde cuentas y que le cuenta", salida: "adaptada" });
    const req = create.mock.calls[0][0] as {
      model: string;
      system: Array<{ text: string }>;
      messages: Array<{ content: Array<{ text: string; cache_control?: { ttl?: string } }> }>;
    };
    expect(req.model).toBe(MODEL_HAIKU);
    expect(req.system[0].text).toBe(SYSTEM_ADAPTAR_PREGUNTA);
    const [ctx, turno] = req.messages[0].content;
    expect(ctx.text).toContain("Dueña de un taller");
    expect(ctx.cache_control?.ttl).toBe("1h");
    expect(JSON.parse(turno.text)).toEqual({ pregunta_base: BASE, sirve_para_elegir_entre: ["Cuenta cómo vas", "Pide ayuda a tiempo"] });
    expect(r.acumulado.uso_por_componente.adaptador).toBeGreaterThan(0);
  });

  it("si la llamada falla, sale la NEUTRAL, nunca la base cruda", async () => {
    const { client } = clienteFalso(new Error("529 overloaded"));
    const r = await adaptarPregunta(client, entrada, usoVacio(), { idiomaSalida: "es", contexto: null });
    expect(r).toMatchObject({ pregunta: NEUTRAL, salida: "neutral", fallo: "529 overloaded" });
  });

  it("si la salida no pasa las comprobaciones, sale la NEUTRAL con el motivo", async () => {
    const { client } = clienteFalso("Claro, aquí va: ¿a quién le cuentas?");
    const r = await adaptarPregunta(client, entrada, usoVacio(), { idiomaSalida: "es", contexto: null });
    expect(r).toMatchObject({ pregunta: NEUTRAL, salida: "neutral", fallo: "no_json" });
  });

  it("un nodo que aun no tiene neutral: sale la base y el resultado lo dice", async () => {
    const { client } = clienteFalso(new Error("timeout"));
    const r = await adaptarPregunta(client, { ...entrada, neutral: null }, usoVacio(), { idiomaSalida: "es", contexto: null });
    expect(r).toMatchObject({ pregunta: BASE, salida: "base_sin_neutral", fallo: "timeout" });
  });
});

describe("adaptarResultadoTurno: el embudo por el que salen los cinco caminos", () => {
  const graph = {
    n0: { titulo_concepto: "Inicio", etiqueta_arbol: "Empieza por aquí", dominio: "core" },
    n1: { titulo_concepto: "Informe al jefe", etiqueta_arbol: "Cuenta cómo vas", dominio: "core" },
    n2: { titulo_concepto: "Pedir ayuda", etiqueta_arbol: "Pide ayuda a tiempo", dominio: "core" },
    n3: { titulo_concepto: "Sin pregunta", etiqueta_arbol: "Ordena tus números", dominio: "core" },
  } as unknown as Grafo;
  const cache: PreguntasCache = {
    n1: { pregunta: BASE, pregunta_neutral: NEUTRAL, candidatos: ["n2", "no_existe"] },
  };

  function turno(pregunta: string, ruta = ["n0", "n1"]) {
    return {
      tipo: "pregunta" as const,
      pregunta,
      acumulado: usoVacio(),
      estado: {
        ruta,
        idioma: "es",
        preguntaPendiente: pregunta,
        ultimasPreguntas: ["¿Qué vendes?", pregunta],
        fallbackEvents: [] as EventoInterprete[],
      },
    };
  }

  it("la base del ultimo nodo sale adaptada: pendiente, anti-repeticion y el evento con el par", async () => {
    const { client, create } = clienteFalso(json("¿A quién le cuentas cómo va tu taller?"));
    const r = await adaptarResultadoTurno(client, turno(BASE), { graph, preguntasCache: cache, idiomaPlantilla: "es" });
    expect(create).toHaveBeenCalledTimes(1);
    expect(r.pregunta).toBe("¿A quién le cuentas cómo va tu taller?");
    expect(r.estado.preguntaPendiente).toBe("¿A quién le cuentas cómo va tu taller?");
    expect(r.estado.ultimasPreguntas).toEqual(["¿Qué vendes?", "¿A quién le cuentas cómo va tu taller?"]);
    expect(r.estado.fallbackEvents).toEqual([
      {
        tipo: "adaptacion_pregunta",
        nodo: "n1",
        de: BASE,
        a: "¿A quién le cuentas cómo va tu taller?",
        busca: "a quien rinde cuentas y que le cuenta",
        salida: "adaptada",
      },
    ]);
    // los siguientes que existen, por su etiqueta (la etiqueta enamora)
    expect(turnoEnviado(create).sirve_para_elegir_entre).toEqual(["Pide ayuda a tiempo"]);
  });

  it("la neutral que ya se mostro tambien pasa por el adaptador (base = la de la cache)", async () => {
    const { client, create } = clienteFalso(json("¿A quién le cuentas cómo va?"));
    await adaptarResultadoTurno(client, turno(NEUTRAL), { graph, preguntasCache: cache, idiomaPlantilla: "es" });
    expect(turnoEnviado(create).pregunta_base).toBe(BASE);
  });

  it("la generica de un nodo sin pregunta en la cache tambien se adapta", async () => {
    const { client, create } = clienteFalso(json("¿Cómo llevas hoy los números de tu taller?"));
    const { obtenerPregunta } = await import("./graph");
    const generica = obtenerPregunta("n3", graph.n3, cache, "es");
    const r = await adaptarResultadoTurno(client, turno(generica, ["n0", "n3"]), { graph, preguntasCache: cache, idiomaPlantilla: "es" });
    expect(create).toHaveBeenCalledTimes(1);
    expect(r.pregunta).toBe("¿Cómo llevas hoy los números de tu taller?");
  });

  it("una pregunta que ya redacto el interprete no se toca ni cuesta nada", async () => {
    const { client, create } = clienteFalso(json("x?"));
    const t = turno("¿Y a tus dos empleados, cuándo les cuentas cómo va el taller?");
    const r = await adaptarResultadoTurno(client, t, { graph, preguntasCache: cache, idiomaPlantilla: "es" });
    expect(create).not.toHaveBeenCalled();
    expect(r).toBe(t);
  });

  it("un turno que no es pregunta pasa tal cual", async () => {
    const { client, create } = clienteFalso(json("x?"));
    const t = { ...turno(BASE), tipo: "listo_para_plan" as const };
    expect(await adaptarResultadoTurno(client, t, { graph, preguntasCache: cache, idiomaPlantilla: "es" })).toBe(t);
    expect(create).not.toHaveBeenCalled();
  });
});

describe("el prompt del adaptador lleva el contrato", () => {
  it("forma si, fondo no; la ficha; tuteo neutro; JSON con pregunta y busca; sin guiones largos", () => {
    const p = SYSTEM_ADAPTAR_PREGUNTA;
    expect(p).toContain("Cambia la FORMA, nunca el FONDO");
    expect(p).toContain("sirve_para_elegir_entre");
    expect(p).toContain("ficha");
    expect(p).toContain("nada de voseo");
    expect(p).toContain('{"pregunta"');
    expect(p).toContain('"busca"');
    expect(p).toContain("PROHIBIDO usar guiones largos");
  });
});
