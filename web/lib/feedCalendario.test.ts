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
