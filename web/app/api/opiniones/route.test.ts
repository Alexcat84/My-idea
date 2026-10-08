// /api/opiniones (decisión del fundador, 8 oct 2026): la pregunta de un clic y los Comentarios y sugerencias.
// - Solo cuentas reales: la identidad invisible ni ve la tarjeta ni puede guardar (401).
// - El tipo y el contexto interno los decide el servidor a partir del plan de ESA cuenta; el navegador solo dice qué
//   sesión mira, y el contexto jamás vuelve en la respuesta.
// - Una sola vez por plan (la segunda vale como hecha), tope de frecuencia, tope diario de comentarios.
// - Fallar ruidoso (BANCO §9): si no se puede guardar, error y nunca un ok.
// - Revisión de seguridad (8 oct 2026): el seguimiento solo se guarda si la tarjeta tocaba (si no, filas sin fin), y
//   los topes los cuenta un contador atómico (contar y luego insertar dejaba pasar peticiones simultáneas).
// Prueba en rojo primero.
import { beforeEach, describe, expect, it, vi } from "vitest";

type Usuario = { id: string; email?: string; is_anonymous?: boolean } | null;
let usuario: Usuario = null;
vi.mock("@/lib/supabase/server", () => ({
  createClient: async () => ({ auth: { getUser: async () => ({ data: { user: usuario } }) } }),
}));

const SESION = "11111111-1111-4111-8111-111111111111";
const PROYECTO = "22222222-2222-4222-8222-222222222222";
const PLAN = "33333333-3333-4333-8333-333333333333";
const OPINION = "44444444-4444-4444-8444-444444444444";

const guardadas: Array<Record<string, unknown>> = [];
const completadas: unknown[][] = [];
let historial: Array<{ tipo: string; objeto_id: string | null; created_at: string }> = [];
let fallaGuardar = false;
let limites: Record<string, boolean> = {};
const clavesLimitadas: Array<[string, number, number]> = [];
vi.mock("@/lib/rateLimit", () => ({
  limitarPorClave: async (clave: string, ttl: number, limite: number) => {
    clavesLimitadas.push([clave, ttl, limite]);
    const permitido = limites[clave.split(":")[0]] ?? true;
    return { permitido, usados: permitido ? 1 : limite + 1, limite };
  },
}));
let repetida = false;
const planReciente = () => new Date(Date.now() - 2 * 86_400_000).toISOString();

vi.mock("@/lib/opinionesServidor", () => ({
  historialDe: async () => historial,
  eventoDePlan: async (userId: string, sesionId: string) =>
    userId === "u1" && sesionId === SESION
      ? {
          evento: { tipo: "plan_mundo", objetoId: PLAN, creadoAt: planReciente() },
          proyectoId: PROYECTO,
          contexto: { etiqueta: "inicial", ciclo: 1, mundo: "quality", nodos: ["n1", "n2"] },
        }
      : null,
  eventoDeSeguimiento: async (userId: string, proyectoId: string) =>
    userId === "u1" && proyectoId === PROYECTO
      ? { evento: { tipo: "seguimiento", objetoId: PROYECTO, ultimoPlanAt: "2026-01-01T00:00:00Z" }, proyectoId: PROYECTO, contexto: { mundo: "core" } }
      : null,
  guardarOpinion: async (o: Record<string, unknown>) => {
    if (fallaGuardar) throw new Error("caida");
    if (repetida) return "repetida";
    guardadas.push(o);
    return { id: OPINION };
  },
  completarOpinion: async (...args: unknown[]) => (completadas.push(args), true),
}));

import { GET, PATCH, POST } from "./route";

const CUENTA = { id: "u1", email: "ana@example.com", is_anonymous: false };
const get = (q: string) => GET(new Request(`http://test/api/opiniones?${q}`));
const post = (cuerpo: unknown) => POST(new Request("http://test/api/opiniones", { method: "POST", body: JSON.stringify(cuerpo), headers: { cookie: "myidea_idioma=fr" } }));
const patch = (cuerpo: unknown) => PATCH(new Request("http://test/api/opiniones", { method: "PATCH", body: JSON.stringify(cuerpo) }));

beforeEach(() => {
  usuario = CUENTA;
  guardadas.length = 0;
  completadas.length = 0;
  historial = [];
  fallaGuardar = false;
  repetida = false;
  limites = {};
  clavesLimitadas.length = 0;
});

describe("GET: ¿se muestra la tarjeta?", () => {
  it("cuenta real con un plan suyo recién llegado: sí, y dice el tipo (sin contexto)", async () => {
    const r = await get(`sesion=${SESION}`);
    expect(r.status).toBe(200);
    const j = await r.json();
    expect(j).toEqual({ preguntar: true, tipo: "plan_mundo" });
  });

  it("la identidad invisible no ve tarjeta", async () => {
    usuario = { id: "anon-1", is_anonymous: true };
    expect(await (await get(`sesion=${SESION}`)).json()).toEqual({ preguntar: false });
  });

  it("el invitado de respaldo (correo de invitado) tampoco", async () => {
    usuario = { id: "inv-1", email: "x@invitado.my-idea.local" };
    expect(await (await get(`sesion=${SESION}`)).json()).toEqual({ preguntar: false });
  });

  it("una sesión que no es suya: no", async () => {
    expect(await (await get("sesion=55555555-5555-4555-8555-555555555555")).json()).toEqual({ preguntar: false });
  });

  it("ese plan ya tiene opinión: no", async () => {
    historial = [{ tipo: "plan_mundo", objeto_id: PLAN, created_at: new Date().toISOString() }];
    expect(await (await get(`sesion=${SESION}`)).json()).toEqual({ preguntar: false });
  });

  it("seguimiento de una idea suya con plan viejo y sin historial: sí", async () => {
    expect(await (await get(`seguimiento=${PROYECTO}`)).json()).toEqual({ preguntar: true, tipo: "seguimiento" });
  });

  it("un id que no es uuid: 400", async () => {
    expect((await get("sesion=abc")).status).toBe(400);
  });
});

describe("POST: guardar", () => {
  it("valoración de un plan: el servidor pone tipo, objeto, idea, idioma y contexto; la respuesta no trae el contexto", async () => {
    const r = await post({ sesion: SESION, valoracion: "excelente" });
    expect(r.status).toBe(200);
    expect(await r.json()).toEqual({ ok: true, id: OPINION });
    expect(guardadas[0]).toEqual({
      userId: "u1",
      tipo: "plan_mundo",
      objetoId: PLAN,
      proyectoId: PROYECTO,
      valoracion: "excelente",
      motivo: null,
      texto: null,
      idioma: "fr",
      contexto: { etiqueta: "inicial", ciclo: 1, mundo: "quality", nodos: ["n1", "n2"] },
    });
  });

  it("el navegador no puede imponer tipo ni contexto", async () => {
    await post({ sesion: SESION, valoracion: "bueno", tipo: "general", contexto: { nodos: ["falso"] } });
    expect(guardadas[0].tipo).toBe("plan_mundo");
    expect(guardadas[0].contexto).toEqual({ etiqueta: "inicial", ciclo: 1, mundo: "quality", nodos: ["n1", "n2"] });
  });

  it("cerrar sin responder también se guarda (para no volver a preguntar)", async () => {
    expect((await post({ sesion: SESION })).status).toBe(200);
    expect(guardadas[0]).toMatchObject({ valoracion: null, motivo: null, texto: null });
  });

  it("la segunda vez del mismo plan vale como hecha", async () => {
    repetida = true;
    expect(await (await post({ sesion: SESION, valoracion: "bueno" })).json()).toEqual({ ok: true, repetida: true });
  });

  it("la identidad invisible no guarda: 401 con el aviso de entrar", async () => {
    usuario = { id: "anon-1", is_anonymous: true };
    const r = await post({ sesion: SESION, valoracion: "bueno" });
    expect(r.status).toBe(401);
    expect(guardadas).toHaveLength(0);
  });

  it("un plan ajeno: 404", async () => {
    expect((await post({ sesion: "55555555-5555-4555-8555-555555555555", valoracion: "bueno" })).status).toBe(404);
  });

  it("valores inventados: 400", async () => {
    expect((await post({ sesion: SESION, valoracion: "regular" })).status).toBe(400);
    expect((await post({ sesion: SESION, valoracion: "bueno", motivo: "confuso" })).status).toBe(400);
  });

  it("si no se puede guardar: 500, nunca un ok", async () => {
    fallaGuardar = true;
    const r = await post({ sesion: SESION, valoracion: "malo" });
    expect(r.status).toBe(500);
    expect((await r.json()).ok).toBeUndefined();
  });

  it("Comentarios y sugerencias: sin objeto ni idea, con texto y valoración opcional", async () => {
    expect((await post({ general: true, texto: "Me gusta el riel", valoracion: "bueno" })).status).toBe(200);
    expect(guardadas[0]).toMatchObject({ tipo: "general", objetoId: null, proyectoId: null, texto: "Me gusta el riel", valoracion: "bueno", contexto: {} });
  });

  it("un comentario vacío no se guarda", async () => {
    expect((await post({ general: true, valoracion: "bueno" })).status).toBe(400);
  });

  it("tope: los comentarios del día los cuenta un contador atómico (5 por cuenta en 24 h); pasado el tope, 429", async () => {
    expect((await post({ general: true, texto: "uno" })).status).toBe(200);
    expect(clavesLimitadas).toContainEqual(["opiniones-general:u1", 86_400, 5]);
    limites["opiniones-general"] = false;
    expect((await post({ general: true, texto: "otro más" })).status).toBe(429);
  });

  it("tope general de escrituras por cuenta (30 en 24 h, también en PATCH): pasado, 429 y no se guarda", async () => {
    expect((await post({ sesion: SESION, valoracion: "bueno" })).status).toBe(200);
    expect(clavesLimitadas).toContainEqual(["opiniones:u1", 86_400, 30]);
    guardadas.length = 0;
    limites["opiniones"] = false;
    expect((await post({ sesion: SESION, valoracion: "bueno" })).status).toBe(429);
    expect((await patch({ id: OPINION, motivo: "otro" })).status).toBe(429);
    expect(guardadas).toHaveLength(0);
  });

  it("seguimiento que no tocaba (ya se preguntó hace poco): 409 y no se guarda", async () => {
    historial = [{ tipo: "seguimiento", objeto_id: PROYECTO, created_at: new Date().toISOString() }];
    expect((await post({ seguimiento: PROYECTO, valoracion: "bueno" })).status).toBe(409);
    expect(guardadas).toHaveLength(0);
  });

  it("seguimiento que sí tocaba: se guarda", async () => {
    expect((await post({ seguimiento: PROYECTO, valoracion: "excelente" })).status).toBe(200);
    expect(guardadas[0]).toMatchObject({ tipo: "seguimiento", objetoId: PROYECTO });
  });

  it("un plan que ya tenía opinión: vale como hecha sin volver a guardar", async () => {
    historial = [{ tipo: "plan_mundo", objeto_id: PLAN, created_at: new Date().toISOString() }];
    expect(await (await post({ sesion: SESION, valoracion: "bueno" })).json()).toEqual({ ok: true, repetida: true });
    expect(guardadas).toHaveLength(0);
  });
});

describe("PATCH: después de 'Malo', el motivo y el texto", () => {
  it("completa SU opinión", async () => {
    expect((await patch({ id: OPINION, motivo: "no_aplica", texto: "es para otro país" })).status).toBe(200);
    expect(completadas[0]).toEqual(["u1", OPINION, "no_aplica", "es para otro país"]);
  });

  it("la identidad invisible no completa nada", async () => {
    usuario = { id: "anon-1", is_anonymous: true };
    expect((await patch({ id: OPINION, motivo: "otro" })).status).toBe(401);
  });

  it("motivo inventado: 400", async () => {
    expect((await patch({ id: OPINION, motivo: "porque_si" })).status).toBe(400);
  });
});
