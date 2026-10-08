// Decisión del fundador (8 oct 2026), centro de cuenta: las dos opciones de la
// verificación en dos pasos con el MISMO estilo de botón de acción, claramente
// diferenciadas entre sí; la que está activa se muestra activa, en verde, con
// una marca de verificación y la opción de desactivarla.
import { renderToStaticMarkup } from "react-dom/server";
import { describe, expect, it } from "vitest";
import { ACTIVE_LOCALES } from "@/lib/i18n/config";
import { IdiomaProvider } from "@/lib/i18n/IdiomaProvider";
import { CUENTA } from "@/lib/i18n/mensajes/cuenta";
import { OpcionesDobleFactor } from "./CuentaCliente";

const t = CUENTA.es.seguridad;
const noop = () => {};
const esc = (s: string) => s.replace(/&/g, "&amp;").replace(/'/g, "&#x27;").replace(/"/g, "&quot;");

function pintar(metodo: "totp" | "email" | null, idioma: (typeof ACTIVE_LOCALES)[number] = "es") {
  return renderToStaticMarkup(
    <IdiomaProvider idioma={idioma}>
      <OpcionesDobleFactor metodo={metodo} ocupado={false} onActivarApp={noop} onActivarCorreo={noop} onDesactivar={noop} />
    </IdiomaProvider>,
  );
}

/** Las etiquetas <button> del html, con sus atributos. */
const botones = (html: string) => html.match(/<button[^>]*>/g) ?? [];
const clase = (b: string) => b.match(/class="([^"]*)"/)?.[1] ?? "";

describe("ninguna activa", () => {
  const html = pintar(null);
  it("las dos opciones, cada una con su nombre y su descripción", () => {
    for (const s of [t.opcionApp, t.opcionAppDesc, t.opcionCorreo, t.opcionCorreoDesc]) expect(html).toContain(esc(s));
  });
  it("dos botones de acción con el MISMO estilo, ninguno desactivado", () => {
    const bs = botones(html);
    expect(bs).toHaveLength(2);
    expect(clase(bs[0]!)).toBe(clase(bs[1]!));
    for (const b of bs) expect(b).not.toContain('disabled=""');
    expect(html).toContain(esc(t.activarApp));
    expect(html).toContain(esc(t.activarCorreo));
  });
  it("nada aparece como activo", () => {
    expect(html).not.toContain('data-marca="verificado"');
    expect(html).not.toContain("text-done");
  });
});

describe.each([
  ["totp", "opcionApp", "opcionCorreo"],
  ["email", "opcionCorreo", "opcionApp"],
] as const)("con %s activa", (metodo, activa, otra) => {
  const html = pintar(metodo);
  const tarjetas = html.match(/<li[\s\S]*?<\/li>/g) ?? [];
  const tActiva = tarjetas.find((x) => x.includes(esc(t[activa])))!;
  const tOtra = tarjetas.find((x) => x.includes(esc(t[otra])))!;

  it("su tarjeta dice Activa, en verde y con la marca de verificación", () => {
    expect(tActiva).toContain(`</svg>${esc(t.activa)}</span>`);
    expect(tActiva).toMatch(/border-done/);
    expect(tActiva).toMatch(/text-done/);
    expect(tActiva).toContain('data-marca="verificado"');
  });
  it("y ofrece desactivarla", () => {
    expect(tActiva).toMatch(new RegExp(`<button[^>]*>${esc(t.desactivarOpcion)}</button>`));
  });
  it("la otra no se puede activar a la vez: su botón queda desactivado y lo explica", () => {
    expect(tOtra).not.toContain('data-marca="verificado"');
    expect(botones(tOtra).every((b) => b.includes('disabled=""'))).toBe(true);
    expect(tOtra).toContain(esc(t.otraActiva));
  });
});

describe("en los once idiomas", () => {
  it.each([...ACTIVE_LOCALES])("%s: los textos nuevos existen y se pintan", (idioma) => {
    const s = CUENTA[idioma].seguridad;
    for (const k of ["opcionApp", "opcionAppDesc", "opcionCorreo", "opcionCorreoDesc", "activa", "otraActiva", "desactivarOpcion"] as const) {
      expect(s[k], `${idioma}.${k}`).toBeTruthy();
    }
    expect(pintar("totp", idioma)).toContain(`</svg>${esc(s.activa)}</span>`);
  });
});
