// i18n F3: el selector de idioma cambia de idioma navegando a la misma página
// con ?lang=xx (D9): proxy.ts lo lee, manda en esa visita y escribe la cookie.
// Casos a mano: se agrega o se reemplaza `lang`, lo demás de la URL queda igual.
import { describe, expect, it } from "vitest";
import { urlConIdioma } from "./selector";

describe("urlConIdioma", () => {
  it("agrega lang a una URL sin parámetros", () => {
    expect(urlConIdioma("https://myidea.app/cuenta", "en")).toBe("https://myidea.app/cuenta?lang=en");
  });
  it("reemplaza un lang anterior y conserva los demás parámetros y el ancla", () => {
    expect(urlConIdioma("https://myidea.app/idea/1?vista=mundo&lang=es#plan", "en")).toBe(
      "https://myidea.app/idea/1?vista=mundo&lang=en#plan"
    );
  });
});
