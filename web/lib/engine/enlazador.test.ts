/**
 * Mundos de protección (P2) — el enlazador.
 *
 * Lo que se vigila aquí es la frontera de "cero invención": todo enlace apunta a
 * una actividad REAL del snapshot o es un NULL declarado; un índice inventado se
 * descarta en vez de disfrazarse de sistémico; la severidad fuera del vocabulario
 * cerrado queda en null; y si la llamada falla, el plan sigue su camino sin
 * enlaces (jamás bloqueado).
 */
import { describe, expect, it, vi } from "vitest";
import type Anthropic from "@anthropic-ai/sdk";
import {
  construirUserTextEnlace,
  enlazarPlanProteccion,
  parsearEnlaces,
  validarEnlaces,
} from "./enlazador";
import { armarSnapshot, type FilaChecklistSnapshot } from "./snapshotProyecto";
import { usoVacio } from "../costmeter";
import { SYSTEM_ENLACE_PROTECCION } from "../prompts";

/** Snapshot del núcleo con tres actividades: #1, #2 y #3. */
function snapshotTres() {
  const filas: FilaChecklistSnapshot[] = [
    { id: "nuc-a", texto: "Cierra el acuerdo con el proveedor", etapa: 1, orden: 1, estado: "pendiente" },
    { id: "nuc-b", texto: "Compra el lote inicial", etapa: 1, orden: 2, estado: "pendiente" },
    { id: "nuc-c", texto: "Abre la tienda en línea", etapa: 2, orden: 1, estado: "pendiente" },
  ];
  return armarSnapshot(filas);
}

const RESPUESTAS = [
  { texto: "Consigue un proveedor alterno y pide su cotización", etapa: 1 },
  { texto: "Haz respaldo semanal de la base de clientes", etapa: 2 },
];

describe("parsearEnlaces: lee lo que hay, no arregla lo que falta", () => {
  it("array limpio", () => {
    const v = parsearEnlaces(
      '[{"item_orden":1,"deteccion":"depende de un solo proveedor","protege_indice":1,"probabilidad":"probable","dolor":"mucho"}]'
    );
    expect(v).toEqual([
      {
        item_orden: 1,
        deteccion: "depende de un solo proveedor",
        protege_indice: 1,
        probabilidad: "probable",
        dolor: "mucho",
        camino: null,
      },
    ]);
  });

  it("envuelto en fences y prosa", () => {
    const t = 'Claro:\n```json\n[{"item_orden":2,"deteccion":"x","protege_indice":null}]\n```\nlisto';
    expect(parsearEnlaces(t)[0]).toMatchObject({ item_orden: 2, protege_indice: null });
  });

  it("sin item_orden entero, la fila no entra", () => {
    expect(parsearEnlaces('[{"deteccion":"x","protege_indice":1},{"item_orden":1.5}]')).toEqual([]);
  });

  it("sin array → vacío", () => {
    expect(parsearEnlaces("no hay json")).toEqual([]);
    expect(parsearEnlaces('{"item_orden":1}')).toEqual([]);
  });
});

describe("validarEnlaces: todo enlace apunta a algo real, o es NULL declarado", () => {
  it("traduce el índice del snapshot a su uuid (el mapa vive en el servidor)", () => {
    const { enlaces } = validarEnlaces(
      [{ item_orden: 1, deteccion: "depende de un solo proveedor", protege_indice: 1, probabilidad: "probable", dolor: "mucho", camino: null }],
      snapshotTres(),
      2
    );
    expect(enlaces[0]).toEqual({
      protege_item: "nuc-a",
      deteccion: "depende de un solo proveedor",
      probabilidad: "probable",
      dolor: "mucho",
      camino: null,
    });
    expect(enlaces[1]).toBeNull();
  });

  it("null es un valor DECLARADO: la respuesta protege al negocio entero", () => {
    const { enlaces, descartados } = validarEnlaces(
      [{ item_orden: 1, deteccion: "el negocio no tiene respaldo de datos", protege_indice: null, probabilidad: null, dolor: null, camino: null }],
      snapshotTres(),
      1
    );
    expect(enlaces[0]).toMatchObject({ protege_item: null, deteccion: "el negocio no tiene respaldo de datos" });
    expect(descartados).toBe(0);
  });

  it("un índice INVENTADO se descarta entero; NO se disfraza de sistémico", () => {
    // #9 no existe en un snapshot de tres. Convertirlo en null diría "protege al
    // negocio entero", que es una intención que el modelo no tuvo.
    const { enlaces, descartados } = validarEnlaces(
      [{ item_orden: 1, deteccion: "algo", protege_indice: 9, probabilidad: "probable", dolor: "poco", camino: null }],
      snapshotTres(),
      1
    );
    expect(enlaces[0]).toBeNull();
    expect(descartados).toBe(1);
  });

  it("un item_orden fuera del plan del mundo también se descarta", () => {
    const { enlaces, descartados } = validarEnlaces(
      [{ item_orden: 7, deteccion: "algo", protege_indice: 1, probabilidad: null, dolor: null, camino: null }],
      snapshotTres(),
      2
    );
    expect(enlaces).toEqual([null, null]);
    expect(descartados).toBe(1);
  });

  it("NINGÚN enlace puede apuntar fuera del núcleo: el snapshot es la única fuente de ids", () => {
    const snap = snapshotTres();
    const idsDelNucleo = new Set(snap.actividades.map((a) => a.id));
    const { enlaces } = validarEnlaces(
      [
        { item_orden: 1, deteccion: "a", protege_indice: 1, probabilidad: null, dolor: null, camino: null },
        { item_orden: 2, deteccion: "b", protege_indice: 3, probabilidad: null, dolor: null, camino: null },
      ],
      snap,
      2
    );
    for (const e of enlaces) {
      if (e?.protege_item) expect(idsDelNucleo.has(e.protege_item)).toBe(true);
    }
  });
});

describe("la severidad: vocabulario CERRADO, y lo inventado se cae", () => {
  it("acepta los seis valores del nodo canónico", () => {
    const { enlaces } = validarEnlaces(
      [
        { item_orden: 1, deteccion: "a", protege_indice: null, probabilidad: "muy_probable", dolor: "bastante", camino: null },
        { item_orden: 2, deteccion: "b", protege_indice: null, probabilidad: "poco_probable", dolor: "poco", camino: null },
      ],
      snapshotTres(),
      2
    );
    expect(enlaces[0]).toMatchObject({ probabilidad: "muy_probable", dolor: "bastante" });
    expect(enlaces[1]).toMatchObject({ probabilidad: "poco_probable", dolor: "poco" });
  });

  it("un PUNTAJE numérico se descarta (la matriz de colores te engaña)", () => {
    const { enlaces } = validarEnlaces(
      [{ item_orden: 1, deteccion: "a", protege_indice: null, probabilidad: "8", dolor: "10", camino: null }],
      snapshotTres(),
      1
    );
    expect(enlaces[0]).toMatchObject({ probabilidad: null, dolor: null });
    // pero la detección y el enlace sobreviven: lo que se cae es la escala inventada
    expect(enlaces[0]!.deteccion).toBe("a");
  });

  it("una escala inventada en palabras tampoco pasa ('alta', 'crítico')", () => {
    const { enlaces } = validarEnlaces(
      [{ item_orden: 1, deteccion: "a", protege_indice: null, probabilidad: "alta", dolor: "critico", camino: null }],
      snapshotTres(),
      1
    );
    expect(enlaces[0]).toMatchObject({ probabilidad: null, dolor: null });
  });
});

describe("EL CAMINO (035): vocabulario cerrado, y lo forzado se calla", () => {
  it("acepta los cuatro caminos del nodo canónico", () => {
    const { enlaces } = validarEnlaces(
      [
        { item_orden: 1, deteccion: "a", protege_indice: null, probabilidad: null, dolor: null, camino: "evitar" },
        { item_orden: 2, deteccion: "b", protege_indice: null, probabilidad: null, dolor: null, camino: "transferir" },
      ],
      snapshotTres(),
      2
    );
    expect(enlaces[0]).toMatchObject({ camino: "evitar" });
    expect(enlaces[1]).toMatchObject({ camino: "transferir" });
  });

  it("un camino inventado ('ignorar', 'escalar') cae a null sin llevarse el resto", () => {
    const { enlaces } = validarEnlaces(
      [{ item_orden: 1, deteccion: "a", protege_indice: 1, probabilidad: "probable", dolor: "poco", camino: "ignorar" }],
      snapshotTres(),
      1
    );
    expect(enlaces[0]).toMatchObject({ camino: null, protege_item: "nuc-a", probabilidad: "probable" });
  });

  it("sin camino (el modelo no clasificó): null declarado, se calla", () => {
    const { enlaces } = validarEnlaces(
      [{ item_orden: 1, deteccion: "a", protege_indice: null, probabilidad: null, dolor: null, camino: null }],
      snapshotTres(),
      1
    );
    expect(enlaces[0]!.camino).toBeNull();
  });

  it("el prompt lo pide contra el enum y con la salida del sin-confianza", () => {
    expect(SYSTEM_ENLACE_PROTECCION).toContain("evitar | mitigar | transferir | aceptar");
    expect(SYSTEM_ENLACE_PROTECCION).toContain("no fuerces la clasificación");
  });
});

describe("el mensaje que se manda: dos listas numeradas, sin uuid", () => {
  it("numera las actividades del núcleo y las respuestas del mundo", () => {
    const t = construirUserTextEnlace(RESPUESTAS, snapshotTres());
    expect(t).toContain("#1 · Cierra el acuerdo con el proveedor");
    expect(t).toContain("#3 · Abre la tienda en línea");
    expect(t).toContain("#1 · E1 · Consigue un proveedor alterno y pide su cotización");
    expect(t).toContain("#2 · E2 · Haz respaldo semanal de la base de clientes");
  });

  it("los uuid del núcleo NO viajan al modelo", () => {
    expect(construirUserTextEnlace(RESPUESTAS, snapshotTres())).not.toContain("nuc-a");
  });
});

// --- Cliente falso, sin red ---
function clienteFalso(respuesta: string | Error): Anthropic {
  return {
    messages: {
      create: vi.fn(async () => {
        if (respuesta instanceof Error) throw respuesta;
        return { usage: { input_tokens: 500, output_tokens: 120 }, content: [{ type: "text", text: respuesta }] };
      }),
    },
  } as unknown as Anthropic;
}

describe("enlazarPlanProteccion: el plan JAMÁS se bloquea", () => {
  it("camino feliz: enlaza y reporta su costo medido", async () => {
    const json =
      '[{"item_orden":1,"deteccion":"depende de un solo proveedor","protege_indice":1,"probabilidad":"probable","dolor":"mucho"},' +
      '{"item_orden":2,"deteccion":"no hay respaldo de la base de clientes","protege_indice":null,"probabilidad":"poco_probable","dolor":"mucho"}]';
    const r = await enlazarPlanProteccion(clienteFalso(json), RESPUESTAS, snapshotTres(), usoVacio());
    expect(r.fallo).toBeNull();
    expect(r.enlaces[0]).toMatchObject({ protege_item: "nuc-a", dolor: "mucho" });
    expect(r.enlaces[1]).toMatchObject({ protege_item: null });
    expect(r.costoUsd).toBeGreaterThan(0); // medido, no supuesto
  });

  it("FALLBACK: si la llamada revienta, enlaces null, sin lanzar y con el motivo", async () => {
    const r = await enlazarPlanProteccion(clienteFalso(new Error("red caída")), RESPUESTAS, snapshotTres(), usoVacio());
    expect(r.enlaces).toEqual([null, null]);
    expect(r.fallo).toContain("red caída");
    expect(r.costoUsd).toBe(0);
    expect(r.acumulado).toEqual(usoVacio());
  });

  it("respuesta ilegible: sin enlaces, sin lanzar (no se inventa ninguno)", async () => {
    const r = await enlazarPlanProteccion(clienteFalso("no pienso responder en JSON"), RESPUESTAS, snapshotTres(), usoVacio());
    expect(r.enlaces).toEqual([null, null]);
    expect(r.fallo).toBeNull(); // la llamada no falló; simplemente no hubo nada válido
  });

  it("sin actividades del núcleo NO se llama al modelo: no hay a qué enlazar", async () => {
    const c = clienteFalso("[]");
    const r = await enlazarPlanProteccion(c, RESPUESTAS, armarSnapshot([]), usoVacio());
    expect(r.fallo).toBe("sin actividades del núcleo que enlazar");
    expect(c.messages.create as ReturnType<typeof vi.fn>).not.toHaveBeenCalled();
  });

  it("plan de protección vacío: ni llamada ni costo", async () => {
    const c = clienteFalso("[]");
    const r = await enlazarPlanProteccion(c, [], snapshotTres(), usoVacio());
    expect(r.enlaces).toEqual([]);
    expect(c.messages.create as ReturnType<typeof vi.fn>).not.toHaveBeenCalled();
  });
});
