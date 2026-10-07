// /api/cuenta/consentimiento (decisión del fundador, 7 oct 2026): el estado y el registro de la aceptación de los
// Términos y la Privacidad por versión (tabla aceptaciones_legales, migración 050).
// - La identidad invisible jamás tiene que aceptar nada (la web es abierta) y no puede escribir el registro.
// - Fallar ruidoso, no mentir calladito (BANCO §9): si no se puede leer el estado, la respuesta lo dice (503), no
//   finge "al día"; si no se puede guardar la aceptación, la respuesta es un error y nunca un ok.
// - La versión la decide el servidor: si el navegador acepta una que ya no es la vigente, no se guarda (409).
// Prueba en rojo primero: nació antes que la ruta.
import { beforeEach, describe, expect, it, vi } from "vitest";
import { HUELLA_LEGAL, VERSION_LEGAL } from "@/lib/legal/consentimiento";

type Sesion = { user: { id: string; email: string }; sessionId: string } | null;
let sesionFalsa: Sesion = null;
vi.mock("@/lib/seguridad", async (importOriginal) => ({
  ...(await importOriginal<typeof import("@/lib/seguridad")>()),
  sesionRealDeCookies: async () => sesionFalsa,
}));

let ultimaFalsa: { data: { version: string } | null; error: { message: string } | null } = { data: null, error: null };
let insertFalso: { error: { code?: string; message: string } | null } = { error: null };
const insertados: Array<Record<string, unknown>> = [];
const lecturas: string[] = [];
vi.mock("@/lib/supabase/admin", () => ({
  createAdminClient: () => ({
    from: (tabla: string) => ({
      select: () => ({
        eq: () => ({
          order: () => ({
            limit: () => ({
              maybeSingle: async () => (lecturas.push(tabla), ultimaFalsa),
            }),
          }),
        }),
      }),
      insert: async (fila: Record<string, unknown>) => (insertados.push({ tabla, ...fila }), insertFalso),
    }),
  }),
}));

import { GET, POST } from "./route";

const REAL = { user: { id: "u1", email: "ana@example.com" }, sessionId: "s1" };

function pedirPost(cuerpo: unknown) {
  return new Request("http://test/api/cuenta/consentimiento", {
    method: "POST",
    body: typeof cuerpo === "string" ? cuerpo : JSON.stringify(cuerpo),
  });
}
const pedirGet = () => new Request("http://test/api/cuenta/consentimiento");

beforeEach(() => {
  sesionFalsa = REAL;
  ultimaFalsa = { data: null, error: null };
  insertFalso = { error: null };
  insertados.length = 0;
  lecturas.length = 0;
});

describe("GET: el estado del consentimiento", () => {
  it("sin cuenta real (invisible o sin sesión) no se pide nada y no se lee la base", async () => {
    sesionFalsa = null;
    const res = await GET(pedirGet());
    expect(res.status).toBe(200);
    expect(await res.json()).toEqual({ cuenta: false, requiere: false });
    expect(lecturas).toEqual([]);
  });

  it("una cuenta real sin aceptación: requiere, primera aceptación, con la versión vigente", async () => {
    const res = await GET(pedirGet());
    expect(await res.json()).toEqual({ cuenta: true, requiere: true, motivo: "primera_aceptacion", version: VERSION_LEGAL });
    expect(lecturas).toEqual(["aceptaciones_legales"]);
  });

  it("una cuenta real con una versión vieja: requiere, versión nueva", async () => {
    ultimaFalsa = { data: { version: "2000-01-01" }, error: null };
    const cuerpo = await (await GET(pedirGet())).json();
    expect(cuerpo.requiere).toBe(true);
    expect(cuerpo.motivo).toBe("nueva_version");
  });

  it("una cuenta real al día: no requiere", async () => {
    ultimaFalsa = { data: { version: VERSION_LEGAL }, error: null };
    expect(await (await GET(pedirGet())).json()).toEqual({ cuenta: true, requiere: false, version: VERSION_LEGAL });
  });

  it("si la base falla, 503 con su error: jamás un 'al día' inventado", async () => {
    ultimaFalsa = { data: null, error: { message: "relation does not exist" } };
    const res = await GET(pedirGet());
    expect(res.status).toBe(503);
    const cuerpo = await res.json();
    expect(cuerpo.requiere).not.toBe(false);
    expect(typeof cuerpo.error).toBe("string");
  });
});

describe("POST: guardar la aceptación", () => {
  it("sin cuenta real: 401 y nada se guarda", async () => {
    sesionFalsa = null;
    const res = await POST(pedirPost({ version: VERSION_LEGAL, idioma_texto: "es" }));
    expect(res.status).toBe(401);
    expect(insertados).toEqual([]);
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
    ultimaFalsa = { data: { version: "2000-01-01" }, error: null };
    const res = await POST(pedirPost({ version: VERSION_LEGAL, idioma_texto: "fr", motivo: "primera_aceptacion" }));
    expect(res.status).toBe(200);
    expect(await res.json()).toEqual({ ok: true, version: VERSION_LEGAL });
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
    ultimaFalsa = { data: null, error: { message: "timeout" } };
    const res = await POST(pedirPost({ version: VERSION_LEGAL, idioma_texto: "es" }));
    expect(res.status).toBe(500);
    expect(insertados).toEqual([]);
  });
});
