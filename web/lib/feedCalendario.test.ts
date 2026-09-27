import { describe, expect, it } from "vitest";

// La clave HMAC se lee de process.env al LLAMAR (no al importar), así que basta
// fijarla antes de las pruebas.
process.env.SUPABASE_SERVICE_ROLE_KEY = "clave-de-prueba-para-el-hmac-del-feed";

import { tokenDeUsuario, usuarioDeToken } from "./feedCalendario";

describe("feedCalendario — token firmado del feed", () => {
  it("round-trip: el token de un usuario devuelve su propio id", () => {
    const uid = "3f2a7c10-abcd-4e00-9999-000000000001";
    expect(usuarioDeToken(tokenDeUsuario(uid))).toBe(uid);
  });

  it("rechaza un token con la firma alterada (forjado)", () => {
    const t = tokenDeUsuario("user-a");
    const forjado = t.slice(0, -2) + (t.endsWith("aa") ? "bb" : "aa");
    expect(usuarioDeToken(forjado)).toBeNull();
  });

  it("rechaza cambiar el userId conservando la firma de otro (no se puede suplantar)", () => {
    const tA = tokenDeUsuario("user-a");
    const firmaA = tA.slice(tA.indexOf(".") + 1);
    const suplantado = `${Buffer.from("user-b").toString("base64url")}.${firmaA}`;
    expect(usuarioDeToken(suplantado)).toBeNull();
  });

  it("rechaza basura", () => {
    expect(usuarioDeToken("basura")).toBeNull();
    expect(usuarioDeToken("")).toBeNull();
    expect(usuarioDeToken(".")).toBeNull();
  });
});

// AUD-09 H11: el calendario suscrito seguía avisando lo que el usuario pausó,
// cerró o reemplazó: el feed leía TODOS los planes y no miraba el modo, la idea
// realizada ni el mundo completado. BANCO §5: "sin fechas no hay recordatorios"
// y "silencio para ideas cerradas". La regla vive en itemsQueAvisan.
import { itemsQueAvisan, type ItemFeed, type PlanFeed } from "./feedCalendario";

describe("itemsQueAvisan: solo avisa lo vigente, con fechas y abierto", () => {
  const planes: PlanFeed[] = [
    { id: "core-viejo", dominio: "core", created_at: "2026-08-01T00:00:00Z", etiqueta: "inicial" },
    { id: "core-nuevo", dominio: "core", created_at: "2026-09-01T00:00:00Z", etiqueta: "seguimiento" },
    { id: "calidad", dominio: "quality", created_at: "2026-08-15T00:00:00Z", etiqueta: "inicial" },
    { id: "riesgos", dominio: "risk_management", created_at: "2026-08-20T00:00:00Z", etiqueta: "inicial" },
  ];
  const item = (id: string, plan_id: string, dominio: string, estado = "pendiente"): ItemFeed => ({
    id, plan_id, dominio, estado, texto: id, etapa: 1, fecha_base: "2026-10-02",
  });
  const items = [
    item("viejo-pendiente", "core-viejo", "core"),
    item("nuevo-pendiente", "core-nuevo", "core"),
    item("nuevo-hecho", "core-nuevo", "core", "hecho"),
    item("calidad-pendiente", "calidad", "quality"),
    item("riesgos-pendiente", "riesgos", "risk_management"),
  ];

  it("un plan reemplazado no avisa; el vigente sí (solo lo pendiente)", () => {
    const ids = itemsQueAvisan({ realizada: false, items, planes, modos: {}, mundosCompletados: [] }).map((i) => i.id);
    expect(ids).toContain("nuevo-pendiente");
    expect(ids).not.toContain("viejo-pendiente");
    expect(ids).not.toContain("nuevo-hecho");
  });

  it("un espacio en modo 'a mi ritmo' no avisa", () => {
    const ids = itemsQueAvisan({ realizada: false, items, planes, modos: { quality: "ritmo" }, mundosCompletados: [] }).map((i) => i.id);
    expect(ids).not.toContain("calidad-pendiente");
    expect(ids).toContain("nuevo-pendiente");
  });

  it("un mundo completado no avisa", () => {
    const ids = itemsQueAvisan({ realizada: false, items, planes, modos: {}, mundosCompletados: ["risk_management"] }).map((i) => i.id);
    expect(ids).not.toContain("riesgos-pendiente");
  });

  it("una idea realizada guarda silencio entera", () => {
    expect(itemsQueAvisan({ realizada: true, items, planes, modos: {}, mundosCompletados: [] })).toEqual([]);
  });
});
