// Pre-beta: el fusible global y el rate limit por IP son la única
// protección de gasto antes de la beta — se testean con Upstash simulado
// (fetch global mockeado) para verificar el contrato exacto: contador,
// tope, TTL de la primera del día, exención del dev user fuera de
// producción, palanca de reversión por env, y elección de identidad.
import { afterEach, beforeEach, describe, expect, it, vi } from "vitest";
import { identidadLimite, MENSAJE_FUSIBLE, verificarFusibleGlobal, verificarLimiteDiario } from "./rateLimit";

const ENV_GUARDADO = { ...process.env };

function mockUpstash(contador: { valor: number }) {
  const llamadas: string[] = [];
  vi.stubGlobal(
    "fetch",
    vi.fn(async (url: string | URL) => {
      const u = String(url);
      llamadas.push(u);
      if (u.includes("/incr/")) {
        contador.valor += 1;
        return new Response(JSON.stringify({ result: contador.valor }), { status: 200 });
      }
      if (u.includes("/expire/")) {
        return new Response(JSON.stringify({ result: 1 }), { status: 200 });
      }
      return new Response("?", { status: 404 });
    })
  );
  return llamadas;
}

beforeEach(() => {
  process.env.UPSTASH_REDIS_REST_URL = "https://upstash.fake";
  process.env.UPSTASH_REDIS_REST_TOKEN = "token-fake";
  delete process.env.FUSIBLE_SESIONES_DIA;
  delete process.env.LIMITE_ARRANQUES_DIA;
  delete process.env.RATE_LIMIT_POR;
});

afterEach(() => {
  vi.unstubAllGlobals();
  process.env = { ...ENV_GUARDADO };
});

describe("verificarFusibleGlobal (tope diario de TODA la app)", () => {
  it("permite hasta el tope y corta en el arranque 31 (default 30)", async () => {
    const contador = { valor: 0 };
    mockUpstash(contador);
    for (let i = 1; i <= 30; i++) {
      const r = await verificarFusibleGlobal();
      expect(r.permitido).toBe(true);
      expect(r.usados).toBe(i);
    }
    const r31 = await verificarFusibleGlobal();
    expect(r31.permitido).toBe(false);
    expect(r31.usados).toBe(31);
    expect(r31.limite).toBe(30);
  });

  it("FUSIBLE_SESIONES_DIA manda sobre el default", async () => {
    process.env.FUSIBLE_SESIONES_DIA = "2";
    const contador = { valor: 0 };
    mockUpstash(contador);
    expect((await verificarFusibleGlobal()).permitido).toBe(true);
    expect((await verificarFusibleGlobal()).permitido).toBe(true);
    expect((await verificarFusibleGlobal()).permitido).toBe(false);
  });

  it("FUSIBLE_SESIONES_DIA=0 desactiva el fusible (palanca de reversión)", async () => {
    process.env.FUSIBLE_SESIONES_DIA = "0";
    const contador = { valor: 999 };
    const llamadas = mockUpstash(contador);
    const r = await verificarFusibleGlobal();
    expect(r.permitido).toBe(true);
    expect(llamadas).toHaveLength(0); // ni siquiera toca Upstash
  });

  it("clave con fecha UTC y TTL de 48h en la primera del día", async () => {
    const contador = { valor: 0 };
    const llamadas = mockUpstash(contador);
    await verificarFusibleGlobal();
    const dia = new Date().toISOString().slice(0, 10);
    expect(llamadas[0]).toContain(encodeURIComponent(`myidea:fusible:${dia}`));
    expect(llamadas[1]).toContain("/expire/");
    expect(llamadas[1]).toContain("/172800");
  });

  it("dev user exento fuera de producción; Upstash caído permite", async () => {
    const contador = { valor: 999 };
    mockUpstash(contador);
    const r = await verificarFusibleGlobal("dev@my-idea.local");
    expect(r.permitido).toBe(true);

    vi.stubGlobal("fetch", vi.fn(async () => new Response("boom", { status: 500 })));
    const caido = await verificarFusibleGlobal();
    expect(caido.permitido).toBe(true);
  });

  it("el mensaje del 503 habla como persona", () => {
    expect(MENSAJE_FUSIBLE).toBe("Estamos a capacidad por hoy; tus ideas te esperan mañana.");
  });
});

describe("verificarLimiteDiario + identidadLimite (5/día por IP)", () => {
  it("corta en el arranque 6 para la misma identidad", async () => {
    const contador = { valor: 0 };
    mockUpstash(contador);
    for (let i = 1; i <= 5; i++) {
      expect((await verificarLimiteDiario("ip:1.2.3.4")).permitido).toBe(true);
    }
    const r6 = await verificarLimiteDiario("ip:1.2.3.4");
    expect(r6.permitido).toBe(false);
    expect(r6.limite).toBe(5);
  });

  it("LIMITE_ARRANQUES_DIA es configurable por env", async () => {
    process.env.LIMITE_ARRANQUES_DIA = "1";
    const contador = { valor: 0 };
    mockUpstash(contador);
    expect((await verificarLimiteDiario("ip:1.2.3.4")).permitido).toBe(true);
    expect((await verificarLimiteDiario("ip:1.2.3.4")).permitido).toBe(false);
  });

  it("la identidad default es la IP del proxy (x-forwarded-for gana, primer salto)", () => {
    const req = new Request("http://x", { headers: { "x-forwarded-for": "9.8.7.6, 10.0.0.1", "x-real-ip": "2.2.2.2" } });
    expect(identidadLimite("user-123", req)).toBe("ip:9.8.7.6");
    const soloReal = new Request("http://x", { headers: { "x-real-ip": "2.2.2.2" } });
    expect(identidadLimite("user-123", soloReal)).toBe("ip:2.2.2.2");
  });

  it("sin headers de proxy cae al user-id (dev local), y RATE_LIMIT_POR=usuario revierte todo", () => {
    expect(identidadLimite("user-123", new Request("http://x"))).toBe("user-123");
    process.env.RATE_LIMIT_POR = "usuario";
    const req = new Request("http://x", { headers: { "x-forwarded-for": "9.8.7.6" } });
    expect(identidadLimite("user-123", req)).toBe("user-123");
  });

  it("la clave del contador lleva la identidad y el día UTC", async () => {
    const contador = { valor: 0 };
    const llamadas = mockUpstash(contador);
    await verificarLimiteDiario("ip:9.8.7.6");
    const dia = new Date().toISOString().slice(0, 10);
    expect(llamadas[0]).toContain(encodeURIComponent(`myidea:rl:ip:9.8.7.6:${dia}`));
  });
});
