/**
 * Contrato del LENGUAJE DE BOTÓN (fundador, ago 2026): el azul es tinta, no
 * mancha. Un botón primario es borde y texto azul sobre fondo tenue; jamás un
 * relleno azul con texto blanco, que se lee lavado.
 *
 * Se vigila sobre el fuente porque el fallo no es romperlo hoy: es que el
 * próximo botón nazca copiado de un ejemplo viejo.
 */
import { readdirSync, readFileSync, statSync } from "node:fs";
import path from "node:path";
import { describe, expect, it } from "vitest";
import { BOTON_PRIMARIO } from "@/lib/boton";

const RAIZ = path.join(__dirname, "..");

/** Todos los .tsx del frente. */
function tsxs(dir: string, out: string[] = []): string[] {
  for (const e of readdirSync(dir)) {
    const p = path.join(dir, e);
    if (statSync(p).isDirectory()) tsxs(p, out);
    else if (e.endsWith(".tsx")) out.push(p);
  }
  return out;
}

/** La ÚNICA excepción declarada: el micrófono usa el relleno como ESTADO de
 * "grabando", no como botón. Un estado activo sí puede ser una mancha. */
const EXCEPCIONES = [path.join("ui", "CampoConVoz.tsx")];

describe("el azul es tinta, no mancha", () => {
  it("ningún botón del frente usa relleno azul con texto blanco", () => {
    const culpables: string[] = [];
    for (const p of tsxs(RAIZ)) {
      const rel = path.relative(RAIZ, p);
      if (EXCEPCIONES.some((e) => rel.endsWith(e))) continue;
      for (const [i, l] of readFileSync(p, "utf-8").split("\n").entries()) {
        // `bg-accent ` con espacio = el relleno pleno (bg-accent/10 no cuenta)
        if (l.includes("bg-accent ") && l.includes("text-white")) culpables.push(`${rel}:${i + 1}`);
      }
    }
    expect(culpables, `estos botones volvieron al relleno azul: ${culpables.join(", ")}`).toEqual([]);
  });

  it("la constante de la casa dice el tratamiento completo", () => {
    expect(BOTON_PRIMARIO).toContain("border-accent/40");
    expect(BOTON_PRIMARIO).toContain("bg-accent/10");
    expect(BOTON_PRIMARIO).toContain("text-accent");
    expect(BOTON_PRIMARIO).not.toContain("text-white");
  });
});
