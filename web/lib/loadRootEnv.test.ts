// Fase 3.0: confirma que loadRootEnv.ts efectivamente carga el .env de la
// raiz del repo (fuente unica de verdad para secretos locales, por
// pedido explicito: no duplicar en un web/.env.local separado) y alias
// SUPABASE_URL/SUPABASE_ANON_KEY a sus equivalentes NEXT_PUBLIC_*.
import { describe, expect, it } from "vitest";
import "./loadRootEnv";

describe("loadRootEnv: carga .env de la raiz y alias a NEXT_PUBLIC_*", () => {
  it("carga las variables server-only del .env raiz", () => {
    expect(process.env.ANTHROPIC_API_KEY).toBeTruthy();
    expect(process.env.SUPABASE_SERVICE_ROLE_KEY).toBeTruthy();
    expect(process.env.VOYAGE_API_KEY).toBeTruthy();
    expect(process.env.UPSTASH_REDIS_REST_URL).toBeTruthy();
    expect(process.env.UPSTASH_REDIS_REST_TOKEN).toBeTruthy();
  });

  it("alias SUPABASE_URL/SUPABASE_ANON_KEY a NEXT_PUBLIC_*", () => {
    expect(process.env.NEXT_PUBLIC_SUPABASE_URL).toBe(process.env.SUPABASE_URL);
    expect(process.env.NEXT_PUBLIC_SUPABASE_ANON_KEY).toBe(process.env.SUPABASE_ANON_KEY);
    expect(process.env.NEXT_PUBLIC_SUPABASE_URL).toMatch(/^https:\/\//);
  });
});
