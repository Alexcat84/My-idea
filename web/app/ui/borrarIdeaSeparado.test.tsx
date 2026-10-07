// Decisión del fundador (8 oct 2026), MIS IDEAS: el icono de borrar no se cruza
// con la flecha de entrar; van separados y con un área de toque cómoda.
//
// La flecha vive en la fila del título (arriba, al final). La papelera baja a la
// esquina INFERIOR del final de la cinta, con 44 px de área de toque (h-11 w-11),
// y la pista del pie le deja su hueco (pe-14) para que el texto no pase debajo.
import { readFileSync } from "node:fs";
import path from "node:path";
import { renderToStaticMarkup } from "react-dom/server";
import { describe, expect, it, vi } from "vitest";
import { IdiomaProvider } from "@/lib/i18n/IdiomaProvider";

vi.mock("next/navigation", () => ({ useRouter: () => ({ refresh: () => {} }) }));
const { BorrarIdeaCinta } = await import("./BorrarIdeaCinta");

describe("la papelera de Mis ideas, lejos de la flecha", () => {
  const html = renderToStaticMarkup(
    <IdiomaProvider idioma="es">
      <BorrarIdeaCinta id="i1" nombre="Pan de barrio" />
    </IdiomaProvider>,
  );

  it("va en la esquina inferior, no en la superior donde está la flecha", () => {
    expect(html).toMatch(/<button[^>]*class="[^"]*\bbottom-1\b/);
    expect(html).not.toMatch(/<button[^>]*class="[^"]*\btop-3\b/);
  });

  it("tiene un área de toque de 44 px", () => {
    expect(html).toMatch(/<button[^>]*class="[^"]*\bh-11 w-11\b/);
  });

  it("la cinta deja el hueco: la pista del pie no pasa bajo la papelera", () => {
    const pagina = readFileSync(path.join(__dirname, "..", "ideas", "page.tsx"), "utf8");
    expect(pagina).toMatch(/<p className="mt-2 pe-14 text-xs text-dim">\{idea\.pista\}<\/p>/);
  });
});
