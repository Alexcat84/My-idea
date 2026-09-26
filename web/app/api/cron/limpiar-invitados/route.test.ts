// Borrado real (decisión del fundador, 26 sep 2026): las ideas de invitado sin
// dueño (escritas con la identidad invisible y nunca adoptadas por una cuenta)
// se borran solas a los 30 días sin actividad. Tarea programada de Vercel, que
// llama con el secreto CRON_SECRET; la base hace el borrado (migración 044).
import { afterEach, beforeEach, describe, expect, it, vi } from "vitest";

const rpc = vi.fn<(nombre: string, args: Record<string, unknown>) => Promise<{ data: number | null; error: unknown }>>(
  async () => ({ data: 3, error: null })
);
vi.mock("@/lib/supabase/admin", () => ({ createAdminClient: () => ({ rpc }) }));

import { DIAS_IDEAS_INVITADO, GET } from "./route";

const pedir = (auth?: string) =>
  GET(new Request("http://test/api/cron/limpiar-invitados", { headers: auth ? { authorization: auth } : {} }));

describe("la limpieza de ideas de invitado sin dueño", () => {
  beforeEach(() => {
    rpc.mockClear();
    process.env.CRON_SECRET = "secreto-de-prueba";
  });

  it("son 30 días", () => {
    expect(DIAS_IDEAS_INVITADO).toBe(30);
  });

  it("sin el secreto correcto: 401 y no borra nada", async () => {
    expect((await pedir()).status).toBe(401);
    expect((await pedir("Bearer otro")).status).toBe(401);
    expect(rpc).not.toHaveBeenCalled();
  });

  it("sin CRON_SECRET configurado falla cerrado (503) y no borra nada", async () => {
    delete process.env.CRON_SECRET;
    expect((await pedir("Bearer ")).status).toBe(503);
    expect(rpc).not.toHaveBeenCalled();
  });

  it("con el secreto: borra las de más de 30 días y dice cuántas", async () => {
    const res = await pedir("Bearer secreto-de-prueba");
    expect(res.status).toBe(200);
    expect(rpc).toHaveBeenCalledWith("limpiar_ideas_de_invitado", { p_dias: 30 });
    expect(await res.json()).toMatchObject({ borradas: 3 });
  });

  // UPSTASH (decisión del fundador, 25 sep 2026): la tarea diaria le da un
  // latido a la base del contador para mantenerla activa (una base gratuita sin
  // uso puede archivarse, como la del 24 sep) y deja una ALERTA si no responde.
  describe("el latido diario a Upstash", () => {
    beforeEach(() => {
      vi.stubEnv("UPSTASH_REDIS_REST_URL", "https://prueba.upstash.io");
      vi.stubEnv("UPSTASH_REDIS_REST_TOKEN", "token-de-prueba");
    });
    afterEach(() => {
      vi.unstubAllEnvs();
      vi.unstubAllGlobals();
    });

    it("base viva: el latido pasa y la tarea responde 200", async () => {
      const f = vi.fn(async () => Response.json({ result: 7 }));
      vi.stubGlobal("fetch", f);
      const res = await pedir("Bearer secreto-de-prueba");
      expect(res.status).toBe(200);
      expect(await res.json()).toEqual({ borradas: 3, upstash: "vivo" });
      expect(String((f.mock.calls[0] as unknown[])[0])).toContain("/incr/myidea:latido");
    });

    it("base caída: la limpieza se hace igual, pero la tarea falla (500) con una ALERTA en los registros", async () => {
      vi.stubGlobal("fetch", vi.fn(async () => { throw new TypeError("fetch failed"); }));
      const log = vi.spyOn(console, "error").mockImplementation(() => {});
      const res = await pedir("Bearer secreto-de-prueba");
      expect(rpc).toHaveBeenCalledWith("limpiar_ideas_de_invitado", { p_dias: 30 });
      expect(res.status).toBe(500);
      expect(await res.json()).toEqual({ borradas: 3, upstash: "caido" });
      expect(log).toHaveBeenCalledWith(expect.stringContaining("ALERTA"), expect.anything());
      log.mockRestore();
    });
  });

  it("si la base falla, lo dice (500)", async () => {
    const log = vi.spyOn(console, "error").mockImplementation(() => {});
    rpc.mockResolvedValueOnce({ data: null, error: { message: "boom" } });
    expect((await pedir("Bearer secreto-de-prueba")).status).toBe(500);
    log.mockRestore();
  });
});
