// LA EVALUACIÓN NO SE ENVÍA SIN ACEPTACIÓN REGISTRADA (corrección del fundador, 7 oct 2026, punto 6). Se cumple en el
// SERVIDOR, no en la pantalla: las rutas que mandan la idea a la IA por primera vez (el organizador gratuito, en SSE
// y en JSON, y el arranque de La Exploración, la primera que usa el buscador) rechazan la petición si la identidad
// que la manda (invitada o con cuenta) no tiene registrada la aceptación de la versión vigente. El rechazo es un 428
// con `consentimiento_requerido: true`, la versión vigente y un mensaje en palabras de persona, y llega ANTES de
// crear la idea, de contar el límite diario y de tocar la IA. Fallar ruidoso: si no se puede leer el registro, 503
// y tampoco se envía nada.
// Prueba en rojo primero: escrita antes de poner la guarda en las rutas.
import { beforeEach, describe, expect, it, vi } from "vitest";
import { VERSION_LEGAL } from "@/lib/legal/consentimiento";

type Usuario = { id: string; email?: string; is_anonymous?: boolean };
let usuarioFalso: Usuario = { id: "anon-1", is_anonymous: true };
vi.mock("@/lib/supabase/server", () => ({
  createClient: async () => ({
    auth: { getUser: async () => ({ data: { user: usuarioFalso } }) },
    from: () => {
      throw new Error("la ruta no debía tocar la base del usuario antes de la guarda");
    },
  }),
}));

let filasFalsas: { data: Array<{ version: string; aceptada_at: string }> | null; error: { message: string } | null } = {
  data: [],
  error: null,
};
const lecturas: string[] = [];
vi.mock("@/lib/supabase/admin", () => ({
  createAdminClient: () => ({
    from: (tabla: string) => ({ select: () => ({ eq: async () => (lecturas.push(tabla), filasFalsas) }) }),
  }),
}));

const crearClienteIA = vi.fn(() => ({ messages: {} }));
vi.mock("@/lib/anthropicClient", () => ({ createAnthropicClient: () => crearClienteIA() }));
const nacerIdea = vi.fn(async () => ({ projectId: "p1", idioma: "es" }));
vi.mock("@/lib/nacerIdea", () => ({ nacerIdea: () => nacerIdea() }));
const fusible = vi.fn(async () => ({ permitido: false, caido: false }));
vi.mock("@/lib/rateLimit", async (importOriginal) => ({
  ...(await importOriginal<typeof import("@/lib/rateLimit")>()),
  verificarFusibleGlobal: () => fusible(),
}));
vi.mock("@/lib/seguridad", async (importOriginal) => ({
  ...(await importOriginal<typeof import("@/lib/seguridad")>()),
  faltaSegundoFactor: async () => false,
}));
const verificarSaldo = vi.fn(async () => ({ alcanza: false, creditos: 0 }));
vi.mock("@/lib/creditos", async (importOriginal) => ({
  ...(await importOriginal<typeof import("@/lib/creditos")>()),
  verificarSaldo: () => verificarSaldo(),
}));

import { POST as organizadorStream } from "@/app/api/organizer/stream/route";
import { POST as organizadorJson } from "@/app/api/organizer/route";
import { POST as arrancarExploracion } from "@/app/api/session/start/route";

const pedir = (ruta: string) =>
  new Request(`http://test${ruta}`, { method: "POST", body: JSON.stringify({ texto: "Quiero vender velas de soya en ferias." }) });

const RUTAS_DEL_ORGANIZADOR = [
  ["/api/organizer/stream", organizadorStream],
  ["/api/organizer", organizadorJson],
] as const;

beforeEach(() => {
  usuarioFalso = { id: "anon-1", is_anonymous: true };
  filasFalsas = { data: [], error: null };
  lecturas.length = 0;
  crearClienteIA.mockClear();
  nacerIdea.mockClear();
  fusible.mockClear();
  verificarSaldo.mockClear();
});

describe("el organizador gratuito (la evaluación) no se envía sin aceptación", () => {
  for (const [ruta, POST] of RUTAS_DEL_ORGANIZADOR) {
    it(`${ruta}: la identidad invisible sin aceptación recibe 428 y nada se crea ni se manda a la IA`, async () => {
      const res = await POST(pedir(ruta));
      expect(res.status).toBe(428);
      const cuerpo = await res.json();
      expect(cuerpo.consentimiento_requerido).toBe(true);
      expect(cuerpo.version).toBe(VERSION_LEGAL);
      expect(cuerpo.motivo).toBe("primera_aceptacion");
      expect(typeof cuerpo.error).toBe("string");
      expect(lecturas).toEqual(["aceptaciones_legales"]);
      expect(nacerIdea).not.toHaveBeenCalled();
      expect(fusible).not.toHaveBeenCalled();
      expect(crearClienteIA).not.toHaveBeenCalled();
    });

    it(`${ruta}: con una versión vieja aceptada, también 428 (versión nueva)`, async () => {
      filasFalsas = { data: [{ version: "2000-01-01", aceptada_at: "2000-01-01T00:00:00Z" }], error: null };
      const res = await POST(pedir(ruta));
      expect(res.status).toBe(428);
      expect((await res.json()).motivo).toBe("nueva_version");
      expect(crearClienteIA).not.toHaveBeenCalled();
    });

    it(`${ruta}: si no se puede leer el registro, 503 y tampoco se envía nada`, async () => {
      filasFalsas = { data: null, error: { message: "la base no responde" } };
      const spy = vi.spyOn(console, "error").mockImplementation(() => undefined);
      const res = await POST(pedir(ruta));
      spy.mockRestore();
      expect(res.status).toBe(503);
      expect(nacerIdea).not.toHaveBeenCalled();
      expect(crearClienteIA).not.toHaveBeenCalled();
    });

    it(`${ruta}: con la versión vigente aceptada, la guarda deja pasar (llega al fusible)`, async () => {
      filasFalsas = { data: [{ version: VERSION_LEGAL, aceptada_at: "2026-10-07T12:00:00Z" }], error: null };
      const res = await POST(pedir(ruta));
      expect(res.status).toBe(503);
      expect(fusible).toHaveBeenCalledTimes(1);
      expect(crearClienteIA).not.toHaveBeenCalled();
    });
  }
});

describe("el arranque de La Exploración (la primera llamada al buscador) tampoco", () => {
  beforeEach(() => {
    usuarioFalso = { id: "u1", email: "ana@example.com", is_anonymous: false };
  });

  it("una cuenta sin la versión vigente aceptada recibe 428, antes de mirar el saldo o tocar la IA", async () => {
    const res = await arrancarExploracion(pedir("/api/session/start"));
    expect(res.status).toBe(428);
    expect((await res.json()).consentimiento_requerido).toBe(true);
    expect(verificarSaldo).not.toHaveBeenCalled();
    expect(crearClienteIA).not.toHaveBeenCalled();
  });

  it("al día, la guarda deja pasar (llega a la verificación del saldo)", async () => {
    filasFalsas = { data: [{ version: VERSION_LEGAL, aceptada_at: "2026-10-07T12:00:00Z" }], error: null };
    const res = await arrancarExploracion(pedir("/api/session/start"));
    expect(res.status).toBe(402);
    expect(verificarSaldo).toHaveBeenCalledTimes(1);
  });

  it("la identidad invisible sigue yendo al login primero (la frontera no cambia)", async () => {
    usuarioFalso = { id: "anon-1", is_anonymous: true };
    const res = await arrancarExploracion(pedir("/api/session/start"));
    expect(res.status).toBe(401);
    expect((await res.json()).login_requerido).toBe(true);
  });
});
