// AUD-09 H16: el borrado de cuenta es irreversible, así que su candado de
// doble factor falla CERRADO. Antes, si la lectura de user_seguridad lanzaba,
// el error se registraba y el borrado seguía sin haber mirado el 2FA.
import { beforeEach, describe, expect, it, vi } from "vitest";

const sesionFalsa = { user: { id: "u1", email: "ana@example.com" }, sessionId: "s1" };
let estadoSeguridadFalso: () => Promise<{ habilitado: boolean }> = async () => ({ habilitado: false });
let desafioFalso: () => Promise<boolean> = async () => false;

vi.mock("@/lib/seguridad", async (importOriginal) => ({
  ...(await importOriginal<typeof import("@/lib/seguridad")>()),
  sesionRealDeCookies: async () => sesionFalsa,
  estadoSeguridad: () => estadoSeguridadFalso(),
  desafioSuperadoEnSesion: () => desafioFalso(),
}));

const deleteUser = vi.fn(async () => ({ error: null }));
vi.mock("@/lib/supabase/admin", () => ({
  createAdminClient: () => ({
    from: () => ({
      select: () => ({ eq: () => ({ maybeSingle: async () => ({ data: null }) }) }),
      upsert: async () => ({ error: null }),
    }),
    auth: { admin: { deleteUser } },
  }),
}));

import { POST } from "./route";

function pedir() {
  return new Request("http://test/api/cuenta/eliminar", {
    method: "POST",
    body: JSON.stringify({ confirmacion: "ELIMINAR" }),
  });
}

describe("POST /api/cuenta/eliminar: el candado de 2FA falla cerrado", () => {
  beforeEach(() => {
    deleteUser.mockClear();
    estadoSeguridadFalso = async () => ({ habilitado: false });
    desafioFalso = async () => false;
  });

  it("si no se puede leer la seguridad, NO borra y responde 503", async () => {
    estadoSeguridadFalso = async () => {
      throw new Error("user_seguridad no responde");
    };
    const res = await POST(pedir());
    expect(res.status).toBe(503);
    expect(deleteUser).not.toHaveBeenCalled();
  });

  it("si falla la lectura del desafío con 2FA activo, NO borra", async () => {
    estadoSeguridadFalso = async () => ({ habilitado: true });
    desafioFalso = async () => {
      throw new Error("two_factor_attempts no responde");
    };
    const res = await POST(pedir());
    expect(res.status).toBe(503);
    expect(deleteUser).not.toHaveBeenCalled();
  });

  it("con 2FA activo y sin desafío superado responde 403 y no borra", async () => {
    estadoSeguridadFalso = async () => ({ habilitado: true });
    const res = await POST(pedir());
    expect(res.status).toBe(403);
    expect(deleteUser).not.toHaveBeenCalled();
  });

  it("sin 2FA, con la palabra escrita, borra", async () => {
    const res = await POST(pedir());
    expect(res.status).toBe(200);
    expect(deleteUser).toHaveBeenCalledWith("u1");
  });
});
