// AUD-09 H07: la idea del invitado se quedaba sin dueño si la cuenta se
// confirmaba desde otro navegador, si se recuperaba la contraseña o si la
// adopción fallaba (solo quedaba en el log). La regla: se adopta en todo camino
// de sesión, y si falla, falla en voz alta y se reintenta.
import { beforeEach, describe, expect, it, vi } from "vitest";
import type { User } from "@supabase/supabase-js";

// Un admin falso mínimo: proyectos por dueño, app_metadata por usuario.
const proyectos: Array<{ id: string; user_id: string }> = [];
const appMetadata: Record<string, Record<string, unknown>> = {};
let fallosRestantes = 0;

function tabla(nombre: string) {
  const filtros: Record<string, unknown> = {};
  let update: Record<string, unknown> | null = null;
  let inIds: string[] | null = null;
  const b = {
    select: () => b,
    update: (u: Record<string, unknown>) => ((update = u), b),
    eq: (c: string, v: unknown) => ((filtros[c] = v), b),
    in: (_c: string, v: string[]) => ((inIds = v), b),
    then(res: (x: unknown) => unknown) {
      if (nombre === "projects" && fallosRestantes > 0) {
        fallosRestantes -= 1;
        return Promise.resolve({ data: null, error: new Error("la base no responde") }).then(res);
      }
      if (nombre === "projects" && update) {
        for (const p of proyectos) if (p.user_id === filtros.user_id && (!inIds || inIds.includes(p.id))) p.user_id = String(update.user_id);
        return Promise.resolve({ data: null, error: null }).then(res);
      }
      if (nombre === "projects") {
        return Promise.resolve({ data: proyectos.filter((p) => p.user_id === filtros.user_id), error: null }).then(res);
      }
      return Promise.resolve({ data: [], error: null }).then(res);
    },
  };
  return b;
}

vi.mock("./supabase/admin", () => ({
  createAdminClient: () => ({
    from: (n: string) => tabla(n),
    auth: {
      admin: {
        getUserById: async (id: string) => ({ data: { user: { id, app_metadata: appMetadata[id] ?? {} } }, error: null }),
        updateUserById: async (id: string, attrs: { app_metadata: Record<string, unknown> }) => {
          appMetadata[id] = { ...(appMetadata[id] ?? {}), ...attrs.app_metadata };
          return { data: {}, error: null };
        },
      },
    },
  }),
}));

import { bienvenidaTrasLogin, registrarAdopcionPendiente } from "./cuentas";

const real = (id: string) => ({ id, is_anonymous: false, app_metadata: appMetadata[id] ?? {} }) as unknown as User;

describe("la adopción del invitado", () => {
  beforeEach(() => {
    proyectos.length = 0;
    for (const k of Object.keys(appMetadata)) delete appMetadata[k];
    fallosRestantes = 0;
  });

  it("al registrarse, la identidad invisible queda anotada como adopción pendiente", async () => {
    await registrarAdopcionPendiente("real-1", "anon-1");
    expect(appMetadata["real-1"].adopcion_pendiente).toEqual(["anon-1"]);
  });

  it("confirmar desde OTRO navegador (sin cookie) adopta lo pendiente y lo limpia", async () => {
    proyectos.push({ id: "idea-1", user_id: "anon-1" });
    appMetadata["real-1"] = { adopcion_pendiente: ["anon-1"] };
    const r = await bienvenidaTrasLogin(real("real-1"), null);
    expect(proyectos[0].user_id).toBe("real-1");
    expect(r.pendientes).toBe(0);
    expect(appMetadata["real-1"].adopcion_pendiente).toEqual([]);
  });

  it("un fallo pasajero se reintenta en el momento", async () => {
    proyectos.push({ id: "idea-1", user_id: "anon-1" });
    fallosRestantes = 1;
    const r = await bienvenidaTrasLogin(real("real-1"), "anon-1");
    expect(proyectos[0].user_id).toBe("real-1");
    expect(r.pendientes).toBe(0);
  });

  it("si la adopción sigue fallando, lo dice y la deja pendiente para el próximo ingreso", async () => {
    proyectos.push({ id: "idea-1", user_id: "anon-1" });
    fallosRestantes = 99;
    const errores = vi.spyOn(console, "error").mockImplementation(() => {});
    const r = await bienvenidaTrasLogin(real("real-1"), "anon-1");
    expect(r.pendientes).toBe(1);
    expect(appMetadata["real-1"].adopcion_pendiente).toEqual(["anon-1"]);
    expect(errores).toHaveBeenCalled();
    errores.mockRestore();
  });
});
