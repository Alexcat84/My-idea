// /api/fundador/opiniones (decisión del fundador, 8 oct 2026): el panel lee y exporta las opiniones de todas las
// cuentas. Protegido con FUNDADOR_EMAILS: para cualquier otro es 404 (ni siquiera se sabe que existe).
// Prueba en rojo primero.
import { readFileSync } from "node:fs";
import path from "node:path";
import { afterEach, beforeEach, describe, expect, it, vi } from "vitest";

type Usuario = { id: string; email?: string; is_anonymous?: boolean } | null;
let usuario: Usuario = null;
vi.mock("@/lib/supabase/server", () => ({
  createClient: async () => ({ auth: { getUser: async () => ({ data: { user: usuario } }) } }),
}));

const filtrosPedidos: unknown[] = [];
vi.mock("@/lib/opinionesServidor", () => ({
  listarOpiniones: async (f: unknown) => (
    filtrosPedidos.push(f),
    [
      {
        id: "o1",
        created_at: "2026-10-20T12:00:00Z",
        tipo: "plan",
        valoracion: "malo",
        motivo: "confuso",
        texto: "no entendí",
        idioma: "es",
        proyecto_id: "p1",
        objeto_id: "plan-1",
        contexto: { etiqueta: "inicial", ciclo: 1, mundo: "core", nodos: ["a"] },
      },
    ]
  ),
}));

import { GET } from "./route";

const ORIGINAL = process.env.FUNDADOR_EMAILS;
beforeEach(() => {
  process.env.FUNDADOR_EMAILS = "dueno@ejemplo.com";
  usuario = { id: "f1", email: "dueno@ejemplo.com", is_anonymous: false };
  filtrosPedidos.length = 0;
});
afterEach(() => {
  if (ORIGINAL === undefined) delete process.env.FUNDADOR_EMAILS;
  else process.env.FUNDADOR_EMAILS = ORIGINAL;
});
const get = (q = "") => GET(new Request(`http://test/api/fundador/opiniones${q}`));

describe("solo el fundador", () => {
  it("otra cuenta real: 404", async () => {
    usuario = { id: "u2", email: "otra@ejemplo.com" };
    expect((await get()).status).toBe(404);
  });
  it("la identidad invisible: 404", async () => {
    usuario = { id: "anon", is_anonymous: true };
    expect((await get()).status).toBe(404);
  });
  it("sin la variable FUNDADOR_EMAILS: 404 para todos", async () => {
    delete process.env.FUNDADOR_EMAILS;
    expect((await get()).status).toBe(404);
  });
});

describe("listar y filtrar", () => {
  it("el fundador recibe las opiniones con su contexto", async () => {
    const r = await get();
    expect(r.status).toBe(200);
    const j = await r.json();
    expect(j.opiniones[0].contexto).toEqual({ etiqueta: "inicial", ciclo: 1, mundo: "core", nodos: ["a"] });
  });
  it("los filtros válidos pasan; los inventados se ignoran", async () => {
    await get("?tipo=plan_mundo&valoracion=malo");
    await get("?tipo=inventado&valoracion=sin");
    expect(filtrosPedidos).toEqual([
      { tipo: "plan_mundo", valoracion: "malo" },
      { tipo: null, valoracion: "sin" },
    ]);
  });
});

describe("exportar a CSV", () => {
  it("descarga un CSV con su nombre de archivo y sin caché", async () => {
    const r = await get("?formato=csv");
    expect(r.headers.get("content-type")).toBe("text/csv; charset=utf-8");
    expect(r.headers.get("content-disposition")).toMatch(/^attachment; filename="opiniones-\d{4}-\d{2}-\d{2}\.csv"$/);
    expect(r.headers.get("cache-control")).toBe("no-store");
    const bytes = new Uint8Array(await r.arrayBuffer());
    // El BOM (EF BB BF) va primero, para que la hoja de c\u00E1lculo lea los acentos.
    expect([...bytes.slice(0, 3)]).toEqual([0xef, 0xbb, 0xbf]);
    const csv = new TextDecoder().decode(bytes);
    expect(csv.startsWith("fecha,tipo,valoracion")).toBe(true);
    expect(csv).toContain("2026-10-20T12:00:00Z,plan,malo,confuso,no entendí,es,p1,plan-1,inicial,1,core,a,o1");
  });
});

describe("la página del panel", () => {
  const pagina = readFileSync(path.join(__dirname, "..", "..", "..", "fundador", "opiniones", "page.tsx"), "utf8");
  it("comprueba al fundador en el servidor y, si no lo es, responde como si no existiera", () => {
    expect(pagina).toMatch(/if \(!esFundador\(user\)\) notFound\(\);/);
    expect(pagina).not.toMatch(/^"use client"/);
  });
  it("filtra por tipo y valoración y exporta a CSV por la ruta protegida", () => {
    expect(pagina).toMatch(/name="tipo"/);
    expect(pagina).toMatch(/name="valoracion"/);
    expect(pagina).toMatch(/\/api\/fundador\/opiniones\?\$\{/);
    expect(pagina).toMatch(/formato=csv/);
  });
  it("muestra el contexto interno de cada opinión", () => {
    expect(pagina).toMatch(/<details/);
    expect(pagina).toMatch(/contexto/);
  });
});
