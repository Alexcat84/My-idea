// Fase 3.0.1: el test ya no exige el .env real del repo (secreto local,
// fuera de git). Crea un .env temporal con valores FALSOS, limpia las
// variables del proceso, aplica el loader contra ese archivo, verifica
// carga + alias, y restaura todo. Verde garantizado en un clon limpio.
import { mkdtempSync, rmSync, writeFileSync } from "node:fs";
import { tmpdir } from "node:os";
import path from "node:path";
import { afterEach, beforeEach, describe, expect, it } from "vitest";
import { aplicarEnv } from "./loadRootEnv";

const VARS = [
  "ANTHROPIC_API_KEY",
  "SUPABASE_SERVICE_ROLE_KEY",
  "VOYAGE_API_KEY",
  "UPSTASH_REDIS_REST_URL",
  "UPSTASH_REDIS_REST_TOKEN",
  "SUPABASE_URL",
  "SUPABASE_ANON_KEY",
  "NEXT_PUBLIC_SUPABASE_URL",
  "NEXT_PUBLIC_SUPABASE_ANON_KEY",
] as const;

const FIXTURE_ENV = [
  "ANTHROPIC_API_KEY=test-anthropic-key",
  "SUPABASE_SERVICE_ROLE_KEY=test-service-role",
  "VOYAGE_API_KEY=test-voyage-key",
  "UPSTASH_REDIS_REST_URL=https://fake.upstash.io",
  "UPSTASH_REDIS_REST_TOKEN=test-upstash-token",
  "SUPABASE_URL=https://fake-project.supabase.co",
  "SUPABASE_ANON_KEY=test-anon-key",
  "",
].join("\n");

describe("aplicarEnv: carga un .env de fixture y alias a NEXT_PUBLIC_*", () => {
  let tmpDir: string;
  let envPath: string;
  const respaldo = new Map<string, string | undefined>();

  beforeEach(() => {
    for (const v of VARS) {
      respaldo.set(v, process.env[v]);
      delete process.env[v];
    }
    tmpDir = mkdtempSync(path.join(tmpdir(), "myidea-env-"));
    envPath = path.join(tmpDir, ".env");
    writeFileSync(envPath, FIXTURE_ENV, { encoding: "utf-8" });
  });

  afterEach(() => {
    for (const v of VARS) {
      const original = respaldo.get(v);
      if (original === undefined) {
        delete process.env[v];
      } else {
        process.env[v] = original;
      }
    }
    rmSync(tmpDir, { recursive: true, force: true });
  });

  it("carga las variables server-only del .env de fixture", () => {
    expect(aplicarEnv(envPath)).toBe(true);
    expect(process.env.ANTHROPIC_API_KEY).toBe("test-anthropic-key");
    expect(process.env.SUPABASE_SERVICE_ROLE_KEY).toBe("test-service-role");
    expect(process.env.VOYAGE_API_KEY).toBe("test-voyage-key");
    expect(process.env.UPSTASH_REDIS_REST_URL).toBe("https://fake.upstash.io");
    expect(process.env.UPSTASH_REDIS_REST_TOKEN).toBe("test-upstash-token");
  });

  it("alias SUPABASE_URL/SUPABASE_ANON_KEY a NEXT_PUBLIC_*", () => {
    aplicarEnv(envPath);
    expect(process.env.NEXT_PUBLIC_SUPABASE_URL).toBe(process.env.SUPABASE_URL);
    expect(process.env.NEXT_PUBLIC_SUPABASE_ANON_KEY).toBe(process.env.SUPABASE_ANON_KEY);
    expect(process.env.NEXT_PUBLIC_SUPABASE_URL).toMatch(/^https:\/\//);
  });

  it("no pisa un NEXT_PUBLIC_* ya definido", () => {
    process.env.NEXT_PUBLIC_SUPABASE_URL = "https://ya-definido.example.com";
    aplicarEnv(envPath);
    expect(process.env.NEXT_PUBLIC_SUPABASE_URL).toBe("https://ya-definido.example.com");
  });

  it("devuelve false y no lanza si el archivo no existe", () => {
    expect(aplicarEnv(path.join(tmpDir, "no-existe.env"))).toBe(false);
  });
});
