// BORRADO REAL DE LA CUENTA (decisión del fundador, 26 sep 2026, D5 de i18n):
// la doctrina "nada se borra jamás" es del catálogo de conocimiento, NO de los
// datos de los usuarios. Borrar la cuenta debe borrar o anonimizar de verdad
// sus datos personales y sus ideas en TODAS las tablas.
//
// Hoy la ruta solo llama a auth.admin.deleteUser y confía en el ON DELETE
// CASCADE. Sobreviven:
//   B1. credit_refund_log: user_id sin FK a auth.users (migración 024).
//   B2. revenuecat_webhook_events: app_user_id sin FK (migración 023).
//   B3. beta_allowlist: el correo en claro, con quién invitó y notas (008).
//   B4. las identidades invisibles anotadas en app_metadata.adopcion_pendiente
//       (adopción fallida): siguen siendo dueñas de las ideas escritas antes de
//       entrar, y nadie las borra.
//
// HALLAZGOS EN ROJO a propósito: cada prueba va con `it.fails` porque el
// arreglo va en su propia tanda (a main con el visto del fundador) y una suite
// en rojo no entra al historial. El arreglo las pasa a `it`.
import { beforeEach, describe, expect, it, vi } from "vitest";

vi.mock("@/lib/seguridad", async (importOriginal) => ({
  ...(await importOriginal<typeof import("@/lib/seguridad")>()),
  sesionRealDeCookies: async () => ({ user: { id: "u1", email: "ana@example.com" }, sessionId: "s1" }),
  estadoSeguridad: async () => ({ habilitado: false }),
  desafioSuperadoEnSesion: async () => false,
}));

const borrados: Array<{ tabla: string; col: string; val: unknown }> = [];
const usuariosBorrados: string[] = [];
vi.mock("@/lib/supabase/admin", () => ({
  createAdminClient: () => ({
    from: (tabla: string) => ({
      select: () => ({ eq: () => ({ maybeSingle: async () => ({ data: null }) }) }),
      upsert: async () => ({ error: null }),
      delete: () => ({
        eq: async (col: string, val: unknown) => (borrados.push({ tabla, col, val }), { error: null }),
      }),
    }),
    auth: {
      admin: {
        getUserById: async () => ({ data: { user: { id: "u1", app_metadata: { adopcion_pendiente: ["anon-1"] } } }, error: null }),
        deleteUser: async (id: string) => (usuariosBorrados.push(id), { error: null }),
      },
    },
  }),
}));

import { POST } from "./route";

const pedir = () =>
  POST(new Request("http://test/api/cuenta/eliminar", { method: "POST", body: JSON.stringify({ confirmacion: "ELIMINAR" }) }));

describe("borrar la cuenta borra todo lo del usuario (hallazgos del borrado real)", () => {
  beforeEach(() => {
    borrados.length = 0;
    usuariosBorrados.length = 0;
  });

  it("la cuenta se borra (lo que ya funciona)", async () => {
    expect((await pedir()).status).toBe(200);
    expect(usuariosBorrados).toContain("u1");
  });

  it.fails("B1: borra sus reembolsos (credit_refund_log no cuelga de auth.users)", async () => {
    await pedir();
    expect(borrados).toContainEqual({ tabla: "credit_refund_log", col: "user_id", val: "u1" });
  });

  it.fails("B2: borra sus eventos de pago (revenuecat_webhook_events no cuelga de auth.users)", async () => {
    await pedir();
    expect(borrados).toContainEqual({ tabla: "revenuecat_webhook_events", col: "app_user_id", val: "u1" });
  });

  it.fails("B3: borra su correo de la lista de invitados", async () => {
    await pedir();
    expect(borrados).toContainEqual({ tabla: "beta_allowlist", col: "email", val: "ana@example.com" });
  });

  it.fails("B4: borra las identidades invisibles pendientes de adopción (y con ellas sus ideas)", async () => {
    await pedir();
    expect(usuariosBorrados).toContain("anon-1");
  });
});
