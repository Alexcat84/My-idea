// i18n F6 (D4): el Send Email Hook de Supabase. Sin secretos reales (AGENTS.md):
// el entorno falso se pone explícito en cada prueba y fetch (Resend) es un
// doble, así que el veredicto no depende de ningún .env.
import { createHmac, randomBytes } from "node:crypto";
import { afterEach, beforeEach, describe, expect, it, vi } from "vitest";
import { CORREOS_AUTH } from "@/lib/i18n/mensajes/correosAuth";
import { POST } from "./route";

// Un secreto de juguete con la forma que da Supabase ("v1,whsec_<base64>").
const CLAVE = randomBytes(24);
const SECRETO = `v1,whsec_${CLAVE.toString("base64")}`;

const ENTORNO = {
  SEND_EMAIL_HOOK_SECRET: SECRETO,
  RESEND_API_KEY: "test-fake-resend-key",
  TWO_FACTOR_EMAIL_FROM: "My Idea <no-reply@example.com>",
  SUPABASE_URL: "https://abc.supabase.co",
};

function firmar(cuerpo: string, id = "msg_1", ts = Math.floor(Date.now() / 1000), clave = CLAVE) {
  const firma = createHmac("sha256", clave).update(`${id}.${ts}.${cuerpo}`).digest("base64");
  return { "webhook-id": id, "webhook-timestamp": String(ts), "webhook-signature": `v1,${firma}` };
}

function peticion(cuerpo: string, cabeceras: Record<string, string> = {}) {
  return new Request("http://test/api/auth/hook-correo", {
    method: "POST",
    headers: { "content-type": "application/json", ...cabeceras },
    body: cuerpo,
  });
}

const PAYLOAD = JSON.stringify({
  user: { id: "u1", email: "ana@example.com", user_metadata: { idioma: "pt" } },
  email_data: {
    token: "305805",
    token_hash: "pkce_abc",
    redirect_to: "https://www.myideaproject.com/auth/callback",
    email_action_type: "signup",
    site_url: "https://www.myideaproject.com",
    token_new: "",
    token_hash_new: "",
  },
});

const fetchFalso = vi.fn();

beforeEach(() => {
  for (const [k, v] of Object.entries(ENTORNO)) vi.stubEnv(k, v);
  fetchFalso.mockReset();
  fetchFalso.mockResolvedValue(new Response(JSON.stringify({ id: "e1" }), { status: 200 }));
  vi.stubGlobal("fetch", fetchFalso);
  vi.spyOn(console, "error").mockImplementation(() => undefined);
});

afterEach(() => {
  vi.unstubAllEnvs();
  vi.unstubAllGlobals();
  vi.restoreAllMocks();
});

describe("POST /api/auth/hook-correo", () => {
  it("con firma válida manda el correo por Resend en el idioma guardado y responde 200 {}", async () => {
    const res = await POST(peticion(PAYLOAD, firmar(PAYLOAD)));
    expect(res.status).toBe(200);
    expect(await res.json()).toEqual({});
    expect(fetchFalso).toHaveBeenCalledTimes(1);
    const [url, init] = fetchFalso.mock.calls[0] as [string, RequestInit];
    expect(url).toBe("https://api.resend.com/emails");
    expect((init.headers as Record<string, string>).Authorization).toBe("Bearer test-fake-resend-key");
    const body = JSON.parse(String(init.body));
    expect(body.to).toEqual(["ana@example.com"]);
    expect(body.from).toBe("My Idea <no-reply@example.com>");
    expect(body.subject).toBe(CORREOS_AUTH.pt.registro.asunto);
    expect(body.text).toContain(
      "https://abc.supabase.co/auth/v1/verify?token=pkce_abc&type=signup&redirect_to=https%3A%2F%2Fwww.myideaproject.com%2Fauth%2Fcallback"
    );
  });

  it("sin firma: 401 y no manda nada", async () => {
    const res = await POST(peticion(PAYLOAD));
    expect(res.status).toBe(401);
    expect((await res.json()).error.http_code).toBe(401);
    expect(fetchFalso).not.toHaveBeenCalled();
  });

  it("con firma de otro secreto: 401 y no manda nada", async () => {
    const res = await POST(peticion(PAYLOAD, firmar(PAYLOAD, "msg_1", Math.floor(Date.now() / 1000), randomBytes(24))));
    expect(res.status).toBe(401);
    expect(fetchFalso).not.toHaveBeenCalled();
  });

  it("con el cuerpo alterado después de firmar: 401", async () => {
    const otro = PAYLOAD.replace("ana@example.com", "mallory@example.com");
    const res = await POST(peticion(otro, firmar(PAYLOAD)));
    expect(res.status).toBe(401);
    expect(fetchFalso).not.toHaveBeenCalled();
  });

  it("sin el secreto configurado falla cerrada: 500, no manda nada y lo dice en el log", async () => {
    vi.stubEnv("SEND_EMAIL_HOOK_SECRET", "");
    const res = await POST(peticion(PAYLOAD, firmar(PAYLOAD)));
    expect(res.status).toBe(500);
    expect(fetchFalso).not.toHaveBeenCalled();
    expect(console.error).toHaveBeenCalled();
  });

  it("sin la clave de Resend: 500 con el error en el formato de Supabase", async () => {
    vi.stubEnv("RESEND_API_KEY", "");
    const res = await POST(peticion(PAYLOAD, firmar(PAYLOAD)));
    expect(res.status).toBe(500);
    const body = await res.json();
    expect(body.error.http_code).toBe(500);
    expect(typeof body.error.message).toBe("string");
    expect(fetchFalso).not.toHaveBeenCalled();
  });

  it("si Resend falla, responde error (Supabase no da el correo por enviado)", async () => {
    fetchFalso.mockResolvedValue(new Response(JSON.stringify({ message: "caído" }), { status: 500 }));
    const res = await POST(peticion(PAYLOAD, firmar(PAYLOAD)));
    expect(res.status).toBe(500);
    expect((await res.json()).error.http_code).toBe(500);
  });

  it("si Resend limita (429), responde 429 para que Supabase reintente", async () => {
    fetchFalso.mockResolvedValue(new Response("{}", { status: 429 }));
    const res = await POST(peticion(PAYLOAD, firmar(PAYLOAD)));
    expect(res.status).toBe(429);
  });

  it("un tipo desconocido: 500 ruidoso, sin correo", async () => {
    const raro = PAYLOAD.replace('"signup"', '"algo_nuevo"');
    const res = await POST(peticion(raro, firmar(raro)));
    expect(res.status).toBe(500);
    expect(fetchFalso).not.toHaveBeenCalled();
  });

  it("el cambio de correo seguro manda los dos correos", async () => {
    const cambio = JSON.stringify({
      user: { id: "u1", email: "ana@example.com", new_email: "ana2@example.com", user_metadata: {} },
      email_data: {
        token: "1",
        token_hash: "H_NUEVO",
        token_new: "2",
        token_hash_new: "H_ACTUAL",
        redirect_to: "",
        email_action_type: "email_change",
        site_url: "https://www.myideaproject.com",
      },
    });
    const res = await POST(peticion(cambio, firmar(cambio)));
    expect(res.status).toBe(200);
    const destinos = fetchFalso.mock.calls.map(([, init]) => JSON.parse(String((init as RequestInit).body)).to[0]);
    expect(destinos).toEqual(["ana@example.com", "ana2@example.com"]);
  });
});
