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
// Consentimiento (corrección del fundador, 7 oct 2026): las aceptaciones de los textos legales por identidad.
type Aceptacion = { user_id: string; version: string; huella_textos: string; idioma_texto: string; motivo: string; aceptada_at: string };
const aceptaciones: Aceptacion[] = [];
let falloAceptaciones = false;

function tabla(nombre: string) {
  const filtros: Record<string, unknown> = {};
  let update: Record<string, unknown> | null = null;
  let inIds: string[] | null = null;
  const b = {
    select: () => b,
    update: (u: Record<string, unknown>) => ((update = u), b),
    eq: (c: string, v: unknown) => ((filtros[c] = v), b),
    in: (_c: string, v: string[]) => ((inIds = v), b),
    insert: async (fila: Aceptacion) => {
      if (falloAceptaciones) return { error: { code: "08006", message: "la base no responde" } };
      if (aceptaciones.some((a) => a.user_id === fila.user_id && a.version === fila.version)) {
        return { error: { code: "23505", message: "duplicate key" } };
      }
      aceptaciones.push({ ...fila });
      return { error: null };
    },
    then(res: (x: unknown) => unknown) {
      if (nombre === "aceptaciones_legales") {
        return Promise.resolve({ data: aceptaciones.filter((a) => a.user_id === filtros.user_id), error: null }).then(res);
      }
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
    aceptaciones.length = 0;
    falloAceptaciones = false;
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

// CONSENTIMIENTO SIN CUENTA (corrección del fundador, 7 oct 2026, punto 2): la aceptación que la identidad invisible
// dio al enviar su idea pasa a la cuenta con la adopción, sin volver a preguntar. La tabla es de solo-añadir: la fila
// se COPIA a la cuenta con la misma versión, huella, idioma y fecha (la prueba de qué se aceptó y cuándo), y el motivo
// se recalcula contra la historia de la cuenta. Si el traslado falla, la adopción queda pendiente y se reintenta.
// Prueba en rojo primero: escrita antes del traslado.
describe("la adopción traslada la aceptación de los textos legales", () => {
  const ACEPTACION_INVITADO: Aceptacion = {
    user_id: "anon-1",
    version: "2026-10-07",
    huella_textos: "a".repeat(64),
    idioma_texto: "fr",
    motivo: "primera_aceptacion",
    aceptada_at: "2026-10-07T15:00:00Z",
  };

  beforeEach(() => {
    proyectos.length = 0;
    for (const k of Object.keys(appMetadata)) delete appMetadata[k];
    fallosRestantes = 0;
    aceptaciones.length = 0;
    falloAceptaciones = false;
  });

  it("al entrar, la cuenta recibe la aceptación del invitado con su versión, huella, idioma y fecha", async () => {
    aceptaciones.push({ ...ACEPTACION_INVITADO });
    const r = await bienvenidaTrasLogin(real("real-1"), "anon-1");
    expect(r.pendientes).toBe(0);
    expect(aceptaciones.filter((a) => a.user_id === "real-1")).toEqual([
      { ...ACEPTACION_INVITADO, user_id: "real-1", motivo: "primera_aceptacion" },
    ]);
  });

  it("también sin ideas que adoptar (el organizador pudo fallar después de aceptar)", async () => {
    aceptaciones.push({ ...ACEPTACION_INVITADO });
    appMetadata["real-1"] = { adopcion_pendiente: ["anon-1"] };
    await bienvenidaTrasLogin(real("real-1"), null);
    expect(aceptaciones.some((a) => a.user_id === "real-1" && a.version === "2026-10-07")).toBe(true);
  });

  it("si la cuenta ya tenía una versión anterior, la trasladada cuenta como versión nueva", async () => {
    aceptaciones.push({ ...ACEPTACION_INVITADO, user_id: "real-1", version: "2026-10-06", aceptada_at: "2026-10-06T10:00:00Z" });
    aceptaciones.push({ ...ACEPTACION_INVITADO });
    await bienvenidaTrasLogin(real("real-1"), "anon-1");
    expect(aceptaciones.find((a) => a.user_id === "real-1" && a.version === "2026-10-07")?.motivo).toBe("nueva_version");
  });

  it("si la cuenta ya tenía esa versión, no se duplica ni es un error", async () => {
    aceptaciones.push({ ...ACEPTACION_INVITADO, user_id: "real-1" });
    aceptaciones.push({ ...ACEPTACION_INVITADO });
    const r = await bienvenidaTrasLogin(real("real-1"), "anon-1");
    expect(r.pendientes).toBe(0);
    expect(aceptaciones.filter((a) => a.user_id === "real-1")).toHaveLength(1);
  });

  it("si el traslado falla, lo dice y la adopción queda pendiente para el próximo ingreso", async () => {
    aceptaciones.push({ ...ACEPTACION_INVITADO });
    falloAceptaciones = true;
    const errores = vi.spyOn(console, "error").mockImplementation(() => {});
    const r = await bienvenidaTrasLogin(real("real-1"), "anon-1");
    expect(r.pendientes).toBe(1);
    expect(appMetadata["real-1"].adopcion_pendiente).toEqual(["anon-1"]);
    expect(errores).toHaveBeenCalled();
    errores.mockRestore();
  });
});
