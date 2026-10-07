// /api/cuenta/consentimiento: el estado y el registro de la aceptación de los Términos y la Privacidad por versión
// (tabla aceptaciones_legales, migración 050). Corrección del fundador del 7 oct 2026: la aceptación se pide en el
// primer envío de datos, y SIN CUENTA TAMBIÉN: la identidad invisible (una fila de auth.users) la guarda igual que
// una cuenta, y la adopción la pasa a la cuenta al crearla.
// - Fallar ruidoso, no mentir calladito (BANCO §9): si no se puede leer el estado, 503 (nunca un "al día"
//   inventado); si no se puede guardar, error y nunca un ok, así la pantalla no envía nada.
// - La versión la decide el servidor: si el navegador acepta una que ya no es la vigente, no se guarda (409).
// Prueba en rojo primero: reescrita antes de abrir la ruta a la identidad invisible.
import { beforeEach, describe, expect, it, vi } from "vitest";
import { HUELLA_LEGAL, VERSION_LEGAL } from "@/lib/legal/consentimiento";

type Usuario = { id: string; email?: string; is_anonymous?: boolean } | null;
let usuarioFalso: Usuario = null;
vi.mock("@/lib/supabase/server", () => ({
  createClient: async () => ({ auth: { getUser: async () => ({ data: { user: usuarioFalso } }) } }),
}));

let filasFalsas: { data: Array<{ version: string; aceptada_at: string }> | null; error: { message: string } | null } = {
  data: [],
  error: null,
};
let insertFalso: { error: { code?: string; message: string } | null } = { error: null };
const insertados: Array<Record<string, unknown>> = [];
const lecturas: string[] = [];
vi.mock("@/lib/supabase/admin", () => ({
  createAdminClient: () => ({
    from: (tabla: string) => ({
      select: () => ({
        eq: async () => (lecturas.push(tabla), filasFalsas),
      }),
      insert: async (fila: Record<string, unknown>) => (insertados.push({ tabla, ...fila }), insertFalso),
    }),
  }),
}));

import { GET, POST } from "./route";

const CUENTA = { id: "u1", email: "ana@example.com", is_anonymous: false };
const INVITADO = { id: "anon-1", is_anonymous: true };

function pedirPost(cuerpo: unknown) {
  return new Request("http://test/api/cuenta/consentimiento", {
    method: "POST",
    body: typeof cuerpo === "string" ? cuerpo : JSON.stringify(cuerpo),
  });
}
const pedirGet = () => new Request("http://test/api/cuenta/consentimiento");

beforeEach(() => {
  usuarioFalso = CUENTA;
  filasFalsas = { data: [], error: null };
  insertFalso = { error: null };
  insertados.length = 0;
  lecturas.length = 0;
});

describe("GET: el estado del consentimiento de quien va a enviar datos", () => {
  it("sin ninguna identidad (el proxy no pudo acuñarla): se pide, sin leer la base", async () => {
    usuarioFalso = null;
    const res = await GET(pedirGet());
    expect(res.status).toBe(200);
    expect(await res.json()).toEqual({ identidad: false, requiere: true, motivo: "primera_aceptacion", version: VERSION_LEGAL });
    expect(lecturas).toEqual([]);
  });

  it("la identidad invisible sin aceptación: requiere, primera aceptación (también sin cuenta)", async () => {
    usuarioFalso = INVITADO;
    const res = await GET(pedirGet());
    expect(await res.json()).toEqual({ identidad: true, requiere: true, motivo: "primera_aceptacion", version: VERSION_LEGAL });
    expect(lecturas).toEqual(["aceptaciones_legales"]);
  });

  it("una cuenta con una versión vieja: requiere, versión nueva", async () => {
    filasFalsas = { data: [{ version: "2000-01-01", aceptada_at: "2000-01-01T00:00:00Z" }], error: null };
    const cuerpo = await (await GET(pedirGet())).json();
    expect(cuerpo.requiere).toBe(true);
    expect(cuerpo.motivo).toBe("nueva_version");
  });

  it("al día: no requiere", async () => {
    filasFalsas = {
      data: [
        { version: "2000-01-01", aceptada_at: "2000-01-01T00:00:00Z" },
        { version: VERSION_LEGAL, aceptada_at: "2026-10-07T12:00:00Z" },
      ],
      error: null,
    };
    expect(await (await GET(pedirGet())).json()).toEqual({ identidad: true, requiere: false, version: VERSION_LEGAL });
  });

  it("si la base falla, 503 con su error: jamás un 'al día' inventado", async () => {
    filasFalsas = { data: null, error: { message: "relation does not exist" } };
    const res = await GET(pedirGet());
    expect(res.status).toBe(503);
    const cuerpo = await res.json();
    expect(cuerpo.requiere).not.toBe(false);
    expect(typeof cuerpo.error).toBe("string");
  });
});

describe("POST: guardar la aceptación", () => {
  it("sin ninguna identidad: 401 y nada se guarda", async () => {
    usuarioFalso = null;
    const res = await POST(pedirPost({ version: VERSION_LEGAL, idioma_texto: "es" }));
    expect(res.status).toBe(401);
    expect(insertados).toEqual([]);
  });

  it("la identidad invisible SÍ guarda su aceptación (en su fila de auth.users)", async () => {
    usuarioFalso = INVITADO;
    const res = await POST(pedirPost({ version: VERSION_LEGAL, idioma_texto: "es" }));
    expect(res.status).toBe(200);
    expect(await res.json()).toEqual({ ok: true, version: VERSION_LEGAL });
    expect(insertados).toEqual([
      {
        tabla: "aceptaciones_legales",
        user_id: "anon-1",
        version: VERSION_LEGAL,
        huella_textos: HUELLA_LEGAL,
        idioma_texto: "es",
        motivo: "primera_aceptacion",
      },
    ]);
  });

  it("cuerpo inválido o idioma fuera de es/fr: 400 y nada se guarda", async () => {
    expect((await POST(pedirPost("no es json"))).status).toBe(400);
    expect((await POST(pedirPost({ version: VERSION_LEGAL, idioma_texto: "ja" }))).status).toBe(400);
    expect(insertados).toEqual([]);
  });

  it("una versión que ya no es la vigente: 409 con la vigente, y nada se guarda", async () => {
    const res = await POST(pedirPost({ version: "2000-01-01", idioma_texto: "es" }));
    expect(res.status).toBe(409);
    expect((await res.json()).version).toBe(VERSION_LEGAL);
    expect(insertados).toEqual([]);
  });

  it("guarda la versión vigente con su huella, el idioma leído y el motivo que decide el servidor", async () => {
    filasFalsas = { data: [{ version: "2000-01-01", aceptada_at: "2000-01-01T00:00:00Z" }], error: null };
    const res = await POST(pedirPost({ version: VERSION_LEGAL, idioma_texto: "fr", motivo: "primera_aceptacion" }));
    expect(res.status).toBe(200);
    expect(insertados).toEqual([
      {
        tabla: "aceptaciones_legales",
        user_id: "u1",
        version: VERSION_LEGAL,
        huella_textos: HUELLA_LEGAL,
        idioma_texto: "fr",
        motivo: "nueva_version",
      },
    ]);
  });

  it("ya al día: ok sin escribir otra fila", async () => {
    filasFalsas = { data: [{ version: VERSION_LEGAL, aceptada_at: "2026-10-07T12:00:00Z" }], error: null };
    const res = await POST(pedirPost({ version: VERSION_LEGAL, idioma_texto: "es" }));
    expect(res.status).toBe(200);
    expect(insertados).toEqual([]);
  });

  it("aceptar dos veces la misma versión no es un error (23505 = ya estaba guardada)", async () => {
    insertFalso = { error: { code: "23505", message: "duplicate key" } };
    const res = await POST(pedirPost({ version: VERSION_LEGAL, idioma_texto: "es" }));
    expect(res.status).toBe(200);
    expect((await res.json()).ok).toBe(true);
  });

  it("si falla el guardado: 500 con su error y NUNCA ok (no se da por aceptada en silencio)", async () => {
    insertFalso = { error: { code: "42P01", message: "relation does not exist" } };
    const res = await POST(pedirPost({ version: VERSION_LEGAL, idioma_texto: "es" }));
    expect(res.status).toBe(500);
    const cuerpo = await res.json();
    expect(cuerpo.ok).toBeUndefined();
    expect(typeof cuerpo.error).toBe("string");
  });

  it("si falla la lectura previa (para el motivo): 500 y nada se guarda", async () => {
    filasFalsas = { data: null, error: { message: "timeout" } };
    const res = await POST(pedirPost({ version: VERSION_LEGAL, idioma_texto: "es" }));
    expect(res.status).toBe(500);
    expect(insertados).toEqual([]);
  });
});
