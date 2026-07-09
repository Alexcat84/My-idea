// Fase 3.0.1: helpers HTTP compartidos entre los scripts de vuelo/prueba
// (web/scripts/vuelo.ts, web/scripts/probar.ts). Autenticacion real via
// @supabase/ssr con un cookie-jar en memoria (el mismo mecanismo de
// cookies que usan las rutas reales, lib/supabase/server.ts) y un
// consumidor generico de Server-Sent Events para /api/session/[id]/plan.
import { createServerClient } from "@supabase/ssr";
import { existsSync } from "node:fs";
import path from "node:path";

export const ROOT = path.resolve(import.meta.dirname, "..", "..", "..");

export function cargarEnvRaiz() {
  const envPath = path.join(ROOT, ".env");
  if (existsSync(envPath)) process.loadEnvFile(envPath);
  if (!process.env.NEXT_PUBLIC_SUPABASE_URL && process.env.SUPABASE_URL) {
    process.env.NEXT_PUBLIC_SUPABASE_URL = process.env.SUPABASE_URL;
  }
  if (!process.env.NEXT_PUBLIC_SUPABASE_ANON_KEY && process.env.SUPABASE_ANON_KEY) {
    process.env.NEXT_PUBLIC_SUPABASE_ANON_KEY = process.env.SUPABASE_ANON_KEY;
  }
}

export const BASE_URL = process.env.VUELO_BASE_URL ?? "http://localhost:3000";
const DEV_EMAIL = "dev@my-idea.local";
// Seguridad (Fase 3.2): la contrasena del dev user salio del codigo -- vive
// en VUELO_DEV_PASSWORD del .env raiz (no versionado). La que estuvo
// committeada se considera quemada; setup_dev_user.py la rota.
function devPassword(): string {
  const password = (process.env.VUELO_DEV_PASSWORD ?? "").trim();
  if (!password) {
    throw new Error(
      "falta VUELO_DEV_PASSWORD en el .env raiz -- la contrasena del dev user ya no vive en el codigo; " +
        "definela (larga y aleatoria) y corre `python scripts/setup_dev_user.py` para rotarla en Supabase"
    );
  }
  return password;
}

/** Inicia sesion como el dev user (scripts/setup_dev_user.py) y devuelve
 * el header Cookie ya armado -- proxy.ts/allowlist (item 9 de Fase 3.0)
 * todavia no existen, asi que cualquier usuario autenticado pasa el
 * chequeo de las rutas reales. */
export async function autenticarComoDevUser(): Promise<string> {
  const jar = new Map<string, string>();
  const client = createServerClient(process.env.NEXT_PUBLIC_SUPABASE_URL!, process.env.NEXT_PUBLIC_SUPABASE_ANON_KEY!, {
    cookies: {
      getAll() {
        return [...jar.entries()].map(([name, value]) => ({ name, value }));
      },
      setAll(cookiesToSet) {
        for (const { name, value } of cookiesToSet) jar.set(name, value);
      },
    },
  });
  const { data, error } = await client.auth.signInWithPassword({ email: DEV_EMAIL, password: devPassword() });
  if (error || !data.session) {
    throw new Error(`fallo el login del dev user (${DEV_EMAIL}): ${error?.message}`);
  }
  return [...jar.entries()].map(([k, v]) => `${k}=${v}`).join("; ");
}

export interface EventoSSE {
  evento: string;
  data: unknown;
}

/** Parsea un stream SSE (event: X\ndata: Y\n\n) frame a frame, ignorando
 * los comentarios de heartbeat (": heartbeat"). */
export async function consumirSSE(response: Response, onEvento: (e: EventoSSE) => void): Promise<void> {
  const reader = response.body!.getReader();
  const decoder = new TextDecoder();
  let buffer = "";
  while (true) {
    const { done, value } = await reader.read();
    if (done) break;
    buffer += decoder.decode(value, { stream: true });
    let idx: number;
    while ((idx = buffer.indexOf("\n\n")) !== -1) {
      const frame = buffer.slice(0, idx);
      buffer = buffer.slice(idx + 2);
      if (!frame.trim() || frame.startsWith(":")) continue;
      let evento = "message";
      let dataRaw = "";
      for (const linea of frame.split("\n")) {
        if (linea.startsWith("event: ")) evento = linea.slice(7);
        else if (linea.startsWith("data: ")) dataRaw += linea.slice(6);
      }
      onEvento({ evento, data: dataRaw ? JSON.parse(dataRaw) : null });
    }
  }
}

export async function postJson(cookie: string, ruta: string, body: unknown): Promise<Record<string, unknown>> {
  const res = await fetch(`${BASE_URL}${ruta}`, {
    method: "POST",
    headers: { "Content-Type": "application/json", Cookie: cookie },
    body: JSON.stringify(body),
  });
  const json = (await res.json()) as Record<string, unknown>;
  if (!res.ok) {
    throw new Error(`POST ${ruta} -> ${res.status}: ${JSON.stringify(json)}`);
  }
  return json;
}

export async function getJson(cookie: string, ruta: string): Promise<Record<string, unknown>> {
  const res = await fetch(`${BASE_URL}${ruta}`, { headers: { Cookie: cookie } });
  const json = (await res.json()) as Record<string, unknown>;
  if (!res.ok) {
    throw new Error(`GET ${ruta} -> ${res.status}: ${JSON.stringify(json)}`);
  }
  return json;
}
