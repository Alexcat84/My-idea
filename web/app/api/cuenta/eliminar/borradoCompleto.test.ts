// BORRADO REAL DE LA CUENTA (decisiones del fundador, 26 sep 2026): la
// doctrina "nada se borra jamás" es del catálogo de conocimiento, NO de los
// datos de los usuarios. Borrar la cuenta borra o anonimiza de verdad sus datos
// personales y sus ideas en TODAS las tablas.
//
// La ruta solo llamaba a auth.admin.deleteUser y confiaba en el ON DELETE
// CASCADE. Sobrevivían (hallazgos B1 a B4, primero commiteados con it.fails):
//   B1. credit_refund_log: user_id sin FK a auth.users (024). SE ANONIMIZA:
//       queda solo el importe y la fecha (podría ser registro fiscal; si puede
//       borrarse queda POR VERIFICAR con el profesional).
//   B2. revenuecat_webhook_events: app_user_id sin FK (023). SE ANONIMIZA.
//   B3. beta_allowlist: el correo en claro (008). SE BORRA.
//   B4. las identidades invisibles de app_metadata.adopcion_pendiente y las
//       ideas escritas antes de entrar. SE BORRAN (solo si de verdad son
//       invisibles: nunca una cuenta real).
//   B5 (decisión del fundador, 27 sep 2026). credit_transactions: el ON DELETE
//       CASCADE se llevaba el historial entero. SE ANONIMIZA como B1 y B2:
//       queda el monto (con su tipo: compra, consumo o devolución) y la fecha;
//       sin persona, concepto, origen, clave ni saldo acumulado. Los registros
//       fiscales de las ventas los conserva el procesador de pagos.
import { beforeEach, describe, expect, it, vi } from "vitest";

vi.mock("@/lib/seguridad", async (importOriginal) => ({
  ...(await importOriginal<typeof import("@/lib/seguridad")>()),
  sesionRealDeCookies: async () => ({ user: { id: "u1", email: "Ana@Example.com" }, sessionId: "s1" }),
  estadoSeguridad: async () => ({ habilitado: false }),
  desafioSuperadoEnSesion: async () => false,
}));

const borrados: Array<{ tabla: string; col: string; val: unknown }> = [];
const anonimizados: Array<{ tabla: string; cambios: Record<string, unknown>; col: string; val: unknown }> = [];
const usuariosBorrados: string[] = [];
const USUARIOS: Record<string, { id: string; is_anonymous?: boolean; app_metadata?: Record<string, unknown> }> = {
  u1: { id: "u1", app_metadata: { adopcion_pendiente: ["anon-1", "real-2"] } },
  "anon-1": { id: "anon-1", is_anonymous: true },
  "real-2": { id: "real-2", is_anonymous: false },
};
vi.mock("@/lib/supabase/admin", () => ({
  createAdminClient: () => ({
    from: (tabla: string) => ({
      select: () => ({ eq: () => ({ maybeSingle: async () => ({ data: null }) }) }),
      upsert: async () => ({ error: null }),
      delete: () => ({
        eq: async (col: string, val: unknown) => (borrados.push({ tabla, col, val }), { error: null }),
      }),
      update: (cambios: Record<string, unknown>) => ({
        eq: async (col: string, val: unknown) => (anonimizados.push({ tabla, cambios, col, val }), { error: null }),
      }),
    }),
    auth: {
      admin: {
        getUserById: async (id: string) => ({ data: { user: USUARIOS[id] ?? null }, error: null }),
        deleteUser: async (id: string) => (usuariosBorrados.push(id), { error: null }),
      },
    },
  }),
}));

import { POST } from "./route";

const pedir = () =>
  POST(new Request("http://test/api/cuenta/eliminar", { method: "POST", body: JSON.stringify({ confirmacion: "ELIMINAR" }) }));

describe("borrar la cuenta borra o anonimiza todo lo del usuario", () => {
  beforeEach(() => {
    borrados.length = 0;
    anonimizados.length = 0;
    usuariosBorrados.length = 0;
  });

  it("la cuenta se borra", async () => {
    expect((await pedir()).status).toBe(200);
    expect(usuariosBorrados).toContain("u1");
  });

  it("B1: sus reembolsos quedan anónimos (solo importe y fecha)", async () => {
    await pedir();
    expect(anonimizados).toContainEqual({ tabla: "credit_refund_log", cambios: { user_id: null, motivo: null }, col: "user_id", val: "u1" });
  });

  it("B2: sus eventos de pago quedan anónimos", async () => {
    await pedir();
    expect(anonimizados).toContainEqual({ tabla: "revenuecat_webhook_events", cambios: { app_user_id: null }, col: "app_user_id", val: "u1" });
  });

  it("B5: su historial de créditos queda anónimo (solo monto, tipo y fecha)", async () => {
    await pedir();
    expect(anonimizados).toContainEqual({
      tabla: "credit_transactions",
      cambios: { user_id: null, saldo_resultante: null, concepto: null, origen: null, idempotency_key: null },
      col: "user_id",
      val: "u1",
    });
  });

  it("B5: el historial se anonimiza ANTES de borrar la cuenta (si no, el CASCADE se lo lleva)", async () => {
    const orden: string[] = [];
    const antes = anonimizados.push.bind(anonimizados);
    anonimizados.push = (...xs) => (xs.forEach((x) => orden.push(x.tabla)), antes(...xs));
    const antesU = usuariosBorrados.push.bind(usuariosBorrados);
    usuariosBorrados.push = (...xs) => (xs.forEach((x) => orden.push(`borrar:${x}`)), antesU(...xs));
    await pedir();
    anonimizados.push = antes;
    usuariosBorrados.push = antesU;
    expect(orden.indexOf("credit_transactions")).toBeGreaterThan(-1);
    expect(orden.indexOf("credit_transactions")).toBeLessThan(orden.indexOf("borrar:u1"));
  });

  it("B3: su correo sale de la lista de invitados (normalizado como la lista lo guarda)", async () => {
    await pedir();
    expect(borrados).toContainEqual({ tabla: "beta_allowlist", col: "email", val: "ana@example.com" });
  });

  it("B4: se borran sus identidades invisibles pendientes, y con ellas sus ideas", async () => {
    await pedir();
    expect(usuariosBorrados).toContain("anon-1");
  });

  it("B4: una identidad pendiente que NO es invisible jamás se borra", async () => {
    await pedir();
    expect(usuariosBorrados).not.toContain("real-2");
  });
});
