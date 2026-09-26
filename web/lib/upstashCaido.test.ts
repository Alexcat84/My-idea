// UPSTASH CAÍDO (decisión del fundador, 25 sep 2026): si la base del contador
// no responde, la app FALLA CERRADA en todo uso de la IA (fusible y límite
// diario), con un mensaje claro en pantalla y un error explícito en los
// registros; nunca un genérico. El incidente del 24 sep: la base desapareció,
// `fetch` lanzó `getaddrinfo ENOTFOUND`, nadie lo atrapó y toda la IA dio 500
// con "algo se atoró de nuestro lado". El comentario del código prometía
// "se permite y se registra" y solo lo cumplía si Upstash RESPONDÍA con error.
import { afterEach, beforeEach, describe, expect, it, vi } from "vitest";
import { MENSAJE_SERVICIO_NO_DISPONIBLE, limitarPorClave, mensajeServicioNoDisponible, verificarFusibleGlobal, verificarLimiteDiario } from "./rateLimit";

const caida = () => vi.fn(async () => { throw new TypeError("fetch failed (getaddrinfo ENOTFOUND tough-fox-158997.upstash.io)"); });

beforeEach(() => {
  vi.stubEnv("UPSTASH_REDIS_REST_URL", "https://prueba.upstash.io");
  vi.stubEnv("UPSTASH_REDIS_REST_TOKEN", "token-de-prueba");
  vi.stubEnv("FUSIBLE_SESIONES_DIA", "30");
  vi.stubEnv("LIMITE_ARRANQUES_DIA", "5");
});
afterEach(() => {
  vi.unstubAllEnvs();
  vi.unstubAllGlobals();
  vi.restoreAllMocks();
});

describe("base caída: la IA se detiene, dicho con claridad", () => {
  it("no se puede alcanzar la base (fetch lanza): fusible y límite frenan, marcados como caída", async () => {
    vi.stubGlobal("fetch", caida());
    const error = vi.spyOn(console, "error").mockImplementation(() => {});
    expect(await verificarFusibleGlobal("ana@example.com")).toMatchObject({ permitido: false, caido: true });
    expect(await verificarLimiteDiario("ip:1.2.3.4", "ana@example.com")).toMatchObject({ permitido: false, caido: true });
    // error explícito en los registros (no un aviso suelto ni un genérico)
    expect(error).toHaveBeenCalledWith(expect.stringContaining("UPSTASH NO RESPONDE"), expect.anything());
  });

  it("la base responde con error (500): también frena", async () => {
    vi.stubGlobal("fetch", vi.fn(async () => new Response("caida", { status: 500 })));
    vi.spyOn(console, "error").mockImplementation(() => {});
    expect(await verificarFusibleGlobal("ana@example.com")).toMatchObject({ permitido: false, caido: true });
  });

  it("el mensaje de pantalla dice qué pasa y que no se cobró nada", () => {
    expect(MENSAJE_SERVICIO_NO_DISPONIBLE).toBe(
      "Servicio temporalmente no disponible. No se te cobró nada; intenta de nuevo en unos minutos."
    );
    expect(mensajeServicioNoDisponible("es")).toBe(MENSAJE_SERVICIO_NO_DISPONIBLE);
  });

  it("el límite de envíos del doble factor (no es IA) no bloquea el acceso: deja pasar y lo registra", async () => {
    vi.stubGlobal("fetch", caida());
    const error = vi.spyOn(console, "error").mockImplementation(() => {});
    expect(await limitarPorClave("2fa:u1", 600, 5)).toMatchObject({ permitido: true, caido: true });
    expect(error).toHaveBeenCalled();
  });
});

describe("base viva: todo igual", () => {
  it("cuenta y deja pasar bajo el tope; frena al superarlo, sin marca de caída", async () => {
    let n = 0;
    vi.stubGlobal("fetch", vi.fn(async (url: string) => (String(url).includes("/incr/") ? Response.json({ result: ++n }) : Response.json({ result: 1 }))));
    expect(await verificarLimiteDiario("ip:9.9.9.9")).toEqual({ permitido: true, usados: 1, limite: 5, caido: false });
    n = 5;
    expect(await verificarLimiteDiario("ip:9.9.9.9")).toEqual({ permitido: false, usados: 6, limite: 5, caido: false });
  });
});
