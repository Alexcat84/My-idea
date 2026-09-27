// El destino post-login es un vector clásico de open-redirect: si aceptáramos
// cualquier `next`, un enlace /login?next=//evil.com mandaría al usuario a
// otro dominio tras autenticar. Estos tests fijan que solo pasan rutas
// internas.
import { describe, expect, it } from "vitest";
import { destinoPostLogin, loginConNext } from "./nextSeguro";

describe("destinoPostLogin: solo rutas internas, jamás open-redirect", () => {
  it("acepta rutas internas normales", () => {
    expect(destinoPostLogin("/idea/abc?entrevista=1")).toBe("/idea/abc?entrevista=1");
    expect(destinoPostLogin("/ideas")).toBe("/ideas");
    expect(destinoPostLogin("/potenciadores")).toBe("/potenciadores");
  });

  it("cae a /ideas cuando falta o está vacío", () => {
    expect(destinoPostLogin(null)).toBe("/ideas");
    expect(destinoPostLogin(undefined)).toBe("/ideas");
    expect(destinoPostLogin("")).toBe("/ideas");
  });

  it("RECHAZA los saltos a otro dominio (//, /\\, absolutas, esquemas)", () => {
    expect(destinoPostLogin("//evil.com")).toBe("/ideas");
    expect(destinoPostLogin("/\\evil.com")).toBe("/ideas");
    expect(destinoPostLogin("https://evil.com")).toBe("/ideas");
    expect(destinoPostLogin("http://evil.com")).toBe("/ideas");
    expect(destinoPostLogin("javascript:alert(1)")).toBe("/ideas");
    expect(destinoPostLogin("evil.com")).toBe("/ideas"); // no empieza con /
  });

  // AUD-09 H14: el parser de URL descarta tabuladores y saltos de línea, así
  // que "/<TAB>/evil.com" pasaba el filtro de la segunda posición y resolvía
  // a //evil.com, un dominio ajeno. La vara es el ORIGEN tras resolver.
  it("RECHAZA caracteres de control que el parser de URL descarta", () => {
    expect(destinoPostLogin("/\t/evil.com")).toBe("/ideas");
    expect(destinoPostLogin("/\n/evil.com")).toBe("/ideas");
    expect(destinoPostLogin("/\r/evil.com")).toBe("/ideas");
    expect(destinoPostLogin("/\t\\evil.com")).toBe("/ideas");
    expect(destinoPostLogin("/idea/abc\u0000")).toBe("/ideas");
    expect(destinoPostLogin("/idea/abc\u007f")).toBe("/ideas");
  });

  it("todo destino aceptado resuelve al mismo origen", () => {
    const origen = "https://www.myideaproject.com";
    for (const raw of ["/ideas", "/idea/abc?entrevista=1", "/x/../../evil", "/%2F%2Fevil.com", "/\t/evil.com"]) {
      expect(new URL(destinoPostLogin(raw), origen).origin).toBe(origen);
    }
  });
});

describe("loginConNext", () => {
  it("codifica el destino en el parámetro next", () => {
    expect(loginConNext("/idea/abc?entrevista=1")).toBe("/login?next=%2Fidea%2Fabc%3Fentrevista%3D1");
  });
});
