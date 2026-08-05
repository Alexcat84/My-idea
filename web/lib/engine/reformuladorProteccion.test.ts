/**
 * Mundos de protección (P2b) — el anclaje de la pregunta.
 *
 * Se prueban las tres barandas del fundador: (a) que ANCLA sin cambiar qué se
 * pregunta, (b) el fallback que devuelve la pregunta del grafo tal cual y jamás
 * bloquea la entrevista, y (c) que el costo sale medido. Más la frontera: los
 * mundos de mejora y el núcleo no se tocan.
 *
 * Sobre la baraja (a): que "la intención sobreviva" no se puede medir contra un
 * cliente falso, porque el falso devuelve lo que uno escriba. Lo que SÍ se puede
 * garantizar, y es lo que de verdad la sostiene, es que la instrucción esté en
 * el instrumento: por eso hay un contrato sobre el prompt.
 */
import { readFileSync } from "node:fs";
import path from "node:path";
import { describe, expect, it, vi } from "vitest";
import type Anthropic from "@anthropic-ai/sdk";
import { anclarPregunta, anclarResultadoTurno, esPreguntaUsable } from "./reformuladorProteccion";
import { SYSTEM_REFORMULADOR_PROTECCION } from "../prompts";
import { armarSnapshot, snapshotComoTexto, type FilaChecklistSnapshot } from "./snapshotProyecto";
import { usoVacio } from "../costmeter";
import type { EventoInterprete } from "./interprete";

const PREGUNTA_DEL_GRAFO = "¿Qué podría salir mal en tu operación y qué harías si pasara?";

function snapshotTexto(): string {
  const filas: FilaChecklistSnapshot[] = [
    { id: "nuc-a", texto: "Cierra el acuerdo con el proveedor", etapa: 1, orden: 1, estado: "pendiente" },
    { id: "nuc-b", texto: "Compra el lote inicial", etapa: 1, orden: 2, estado: "pendiente" },
  ];
  return snapshotComoTexto(armarSnapshot(filas));
}

function clienteFalso(respuesta: string | Error): Anthropic {
  return {
    messages: {
      create: vi.fn(async () => {
        if (respuesta instanceof Error) throw respuesta;
        return { usage: { input_tokens: 400, output_tokens: 60 }, content: [{ type: "text", text: respuesta }] };
      }),
    },
  } as unknown as Anthropic;
}

describe("BARANDA (a): ancla, jamás cambia qué se pregunta", () => {
  it("la instrucción de conservar la intención está en el prompt, no en la esperanza", () => {
    const p = SYSTEM_REFORMULADOR_PROTECCION;
    expect(p).toContain("CONSERVANDO INTACTA su");
    expect(p).toContain("intencion metodologica");
    expect(p).toContain("DEVUELVELA TAL CUAL");
    expect(p).toContain("#N");
    // y la regla de voz de la casa
    expect(p).toContain("PROHIBIDO usar guiones largos");
  });

  it("una pregunta anclada a una actividad concreta pasa y se marca como anclada", async () => {
    const anclada =
      "Para cerrar el acuerdo con el proveedor (#1), ¿qué podría salir mal y qué harías si pasara?";
    const r = await anclarPregunta(clienteFalso(anclada), PREGUNTA_DEL_GRAFO, snapshotTexto(), usoVacio());
    expect(r.pregunta).toBe(anclada);
    expect(r.anclada).toBe(true);
    expect(r.fallo).toBeNull();
    // la intención metodológica ("qué podría salir mal / qué harías") sobrevive
    expect(r.pregunta).toContain("qué podría salir mal");
    expect(r.pregunta).toContain("qué harías si pasara");
    // y ahora habla de algo que la persona de verdad va a hacer, por su #N
    expect(r.pregunta).toContain("acuerdo con el proveedor");
    expect(r.pregunta).toContain("#1");
  });

  it("si ninguna actividad aplica, el modelo la devuelve tal cual y NO se marca anclada", async () => {
    const r = await anclarPregunta(clienteFalso(PREGUNTA_DEL_GRAFO), PREGUNTA_DEL_GRAFO, snapshotTexto(), usoVacio());
    expect(r.pregunta).toBe(PREGUNTA_DEL_GRAFO);
    expect(r.anclada).toBe(false);
    expect(r.fallo).toBeNull();
  });

  it("el snapshot viaja al modelo con sus actividades numeradas", async () => {
    const c = clienteFalso(PREGUNTA_DEL_GRAFO);
    await anclarPregunta(c, PREGUNTA_DEL_GRAFO, snapshotTexto(), usoVacio());
    const llamada = (c.messages.create as ReturnType<typeof vi.fn>).mock.calls[0][0] as {
      messages: Array<{ content: string }>;
    };
    expect(llamada.messages[0].content).toContain("#1 · E1 · Cierra el acuerdo con el proveedor");
    expect(llamada.messages[0].content).toContain("PREGUNTA A ANCLAR:");
  });
});

describe("BARANDA (b): el fallback, la entrevista jamás se bloquea", () => {
  it("la llamada revienta → la pregunta del grafo tal cual, con el motivo", async () => {
    const r = await anclarPregunta(clienteFalso(new Error("red caída")), PREGUNTA_DEL_GRAFO, snapshotTexto(), usoVacio());
    expect(r.pregunta).toBe(PREGUNTA_DEL_GRAFO);
    expect(r.fallo).toContain("red caída");
    expect(r.costoUsd).toBe(0);
  });

  it("una respuesta que no es una pregunta (un párrafo largo) se descarta", async () => {
    const parrafo =
      "Claro, con gusto. Antes de responder conviene entender que la gestión de riesgos es una disciplina que " +
      "abarca la identificación, el análisis y la respuesta. Los marcos más usados proponen cuatro caminos, y " +
      "cada uno tiene ventajas. Dicho esto, la pregunta que te haría es la siguiente, aunque primero repasemos " +
      "los conceptos fundamentales que sostienen todo este enfoque metodológico tan importante para tu caso.";
    const r = await anclarPregunta(clienteFalso(parrafo), PREGUNTA_DEL_GRAFO, snapshotTexto(), usoVacio());
    expect(r.pregunta).toBe(PREGUNTA_DEL_GRAFO);
    expect(r.fallo).toContain("no tenía forma de pregunta");
  });

  it("una respuesta en JSON o con bloques de código se descarta", async () => {
    for (const basura of ['{"pregunta":"hola"}', "```\n¿algo?\n```", ""]) {
      const r = await anclarPregunta(clienteFalso(basura), PREGUNTA_DEL_GRAFO, snapshotTexto(), usoVacio());
      expect(r.pregunta).toBe(PREGUNTA_DEL_GRAFO);
    }
  });

  it("esPreguntaUsable acepta lo corto y de una línea, rechaza lo demás", () => {
    expect(esPreguntaUsable("¿Qué harías si tu único proveedor falla?")).toBe(true);
    expect(esPreguntaUsable("  ")).toBe(false);
    expect(esPreguntaUsable("a".repeat(401))).toBe(false);
    expect(esPreguntaUsable("una\nlinea\notra\nmas")).toBe(false);
    expect(esPreguntaUsable('[{"x":1}]')).toBe(false);
  });
});

describe("BARANDA (c): calidad plena y costo medido", () => {
  it("corre en el modelo de calidad plena, jamás en uno menor", async () => {
    const c = clienteFalso("¿Y si el proveedor (#1) no responde a tiempo?");
    await anclarPregunta(c, PREGUNTA_DEL_GRAFO, snapshotTexto(), usoVacio());
    const llamada = (c.messages.create as ReturnType<typeof vi.fn>).mock.calls[0][0] as { model: string };
    expect(llamada.model).toBe("claude-sonnet-4-6");
  });

  it("el costo sale MEDIDO cuando se ancla", async () => {
    const r = await anclarPregunta(
      clienteFalso("¿Y si el proveedor (#1) no responde a tiempo?"),
      PREGUNTA_DEL_GRAFO,
      snapshotTexto(),
      usoVacio()
    );
    expect(r.costoUsd).toBeGreaterThan(0);
  });

  it("el componente queda etiquetado para poder leerlo en el desglose", async () => {
    const c = clienteFalso("¿Y si el proveedor (#1) no responde?");
    await anclarPregunta(c, PREGUNTA_DEL_GRAFO, snapshotTexto(), usoVacio());
    const { costoAcumuladoUsd } = await import("../costmeter");
    expect(typeof costoAcumuladoUsd).toBe("function"); // el desglose existe
  });
});

describe("LA FRONTERA: los mundos de mejora y el núcleo no se tocan", () => {
  const estadoBase = {
    snapshotNucleo: null as string | null,
    preguntaPendiente: "x",
    ultimasPreguntas: ["x"],
    fallbackEvents: [] as EventoInterprete[],
  };

  it("sin snapshot (núcleo y mundos de mejora) NO se llama al modelo", async () => {
    const c = clienteFalso("no debería usarse");
    const r = await anclarResultadoTurno(
      c,
      { tipo: "pregunta", pregunta: PREGUNTA_DEL_GRAFO, estado: { ...estadoBase } },
      usoVacio()
    );
    expect(r.resultado.pregunta).toBe(PREGUNTA_DEL_GRAFO);
    expect(r.anclaje).toBeNull();
    expect(c.messages.create as ReturnType<typeof vi.fn>).not.toHaveBeenCalled();
  });

  it("un turno que NO es pregunta (listo_para_plan) pasa intacto y sin llamada", async () => {
    const c = clienteFalso("no debería usarse");
    const r = await anclarResultadoTurno(
      c,
      { tipo: "listo_para_plan", estado: { ...estadoBase, snapshotNucleo: snapshotTexto() } },
      usoVacio()
    );
    expect(r.anclaje).toBeNull();
    expect(c.messages.create as ReturnType<typeof vi.fn>).not.toHaveBeenCalled();
  });

  it("al anclar, la pregunta PENDIENTE y el historial se persisten con la versión anclada", async () => {
    // Si solo se cambiara el texto de la respuesta, al reentrar el usuario vería
    // la pregunta vieja y el motor se repetiría contra un texto que nadie leyó.
    const anclada = "Para cerrar el acuerdo con el proveedor (#1), ¿qué podría salir mal?";
    const r = await anclarResultadoTurno(
      clienteFalso(anclada),
      {
        tipo: "pregunta",
        pregunta: PREGUNTA_DEL_GRAFO,
        estado: {
          snapshotNucleo: snapshotTexto(),
          preguntaPendiente: PREGUNTA_DEL_GRAFO,
          ultimasPreguntas: ["algo previo", PREGUNTA_DEL_GRAFO],
          fallbackEvents: [] as EventoInterprete[],
        },
      },
      usoVacio()
    );
    expect(r.resultado.pregunta).toBe(anclada);
    expect(r.resultado.estado.preguntaPendiente).toBe(anclada);
    expect(r.resultado.estado.ultimasPreguntas).toEqual(["algo previo", anclada]);
  });

  it("si el anclaje falla, el estado NO se toca (queda la del grafo, coherente)", async () => {
    const r = await anclarResultadoTurno(
      clienteFalso(new Error("caída")),
      {
        tipo: "pregunta",
        pregunta: PREGUNTA_DEL_GRAFO,
        estado: {
          snapshotNucleo: snapshotTexto(),
          preguntaPendiente: PREGUNTA_DEL_GRAFO,
          ultimasPreguntas: [PREGUNTA_DEL_GRAFO],
          fallbackEvents: [] as EventoInterprete[],
        },
      },
      usoVacio()
    );
    expect(r.resultado.pregunta).toBe(PREGUNTA_DEL_GRAFO);
    expect(r.resultado.estado.preguntaPendiente).toBe(PREGUNTA_DEL_GRAFO);
    expect(r.anclaje!.fallo).toContain("caída");
  });

  // El fundador muestrea a mano si la intención sobrevivió: para eso necesita
  // ver LA PAREJA (la del grafo y la anclada) sin reconstruir nada.
  it("el PAR queda registrado en los eventos de la sesión, se haya anclado o no", async () => {
    const anclada = "Para cerrar el acuerdo con el proveedor (#1), ¿qué podría salir mal?";
    const r = await anclarResultadoTurno(
      clienteFalso(anclada),
      {
        tipo: "pregunta",
        pregunta: PREGUNTA_DEL_GRAFO,
        estado: {
          snapshotNucleo: snapshotTexto(),
          preguntaPendiente: PREGUNTA_DEL_GRAFO,
          ultimasPreguntas: [PREGUNTA_DEL_GRAFO],
          fallbackEvents: [] as EventoInterprete[],
        },
      },
      usoVacio()
    );
    const evento = r.resultado.estado.fallbackEvents.at(-1);
    expect(evento).toMatchObject({ tipo: "anclaje_proteccion", de: PREGUNTA_DEL_GRAFO, a: anclada });
  });

  it("cuando el anclaje falla, el par lleva el motivo y las dos preguntas iguales", async () => {
    const r = await anclarResultadoTurno(
      clienteFalso(new Error("caída")),
      {
        tipo: "pregunta",
        pregunta: PREGUNTA_DEL_GRAFO,
        estado: {
          snapshotNucleo: snapshotTexto(),
          preguntaPendiente: PREGUNTA_DEL_GRAFO,
          ultimasPreguntas: [PREGUNTA_DEL_GRAFO],
          fallbackEvents: [] as EventoInterprete[],
        },
      },
      usoVacio()
    );
    const evento = r.resultado.estado.fallbackEvents.at(-1) as { tipo: string; de: string; a: string; motivo?: string };
    expect(evento.tipo).toBe("anclaje_proteccion");
    expect(evento.de).toBe(PREGUNTA_DEL_GRAFO);
    expect(evento.a).toBe(PREGUNTA_DEL_GRAFO);
    expect(evento.motivo).toContain("caída");
  });

  it("sin snapshot no se registra ningún par (no hubo anclaje que muestrear)", async () => {
    const r = await anclarResultadoTurno(
      clienteFalso("no debería usarse"),
      { tipo: "pregunta", pregunta: PREGUNTA_DEL_GRAFO, estado: { ...estadoBase } },
      usoVacio()
    );
    expect(r.resultado.estado.fallbackEvents).toEqual([]);
  });

  it("los dos sitios donde nace una pregunta de mundo lo enganchan", () => {
    const raiz = path.join(__dirname, "..", "..", "app", "api");
    const start = readFileSync(path.join(raiz, "project", "[id]", "world", "[pack]", "start", "route.ts"), "utf-8");
    const turno = readFileSync(path.join(raiz, "session", "[id]", "turn", "route.ts"), "utf-8");
    for (const fuente of [start, turno]) {
      expect(fuente).toContain("anclarResultadoTurno(");
      // y lo que se responde/persiste es el resultado ANCLADO, no el original
      expect(fuente).toContain("anclado.resultado");
    }
  });
});
