/**
 * Contrato del LENGUAJE DE BOTÓN (decisiones del fundador, ago 2026).
 *
 * Dos carriles y solo dos: el HÉROE con su chispa (los momentos que abren
 * camino, uno por pantalla) y el ESTÁNDAR de tinta, que usan por igual el
 * botón principal y el de cancelar. Se vigila sobre el fuente porque el fallo
 * típico no es romperlo hoy: es que el próximo botón nazca copiado de un
 * ejemplo viejo.
 */
import { readdirSync, readFileSync, statSync } from "node:fs";
import path from "node:path";
import { describe, expect, it } from "vitest";
import { BOTON_ESTANDAR, BOTON_PRIMARIO, BOTON_SECUNDARIO } from "@/lib/boton";

const RAIZ = path.join(__dirname, "..");
const leer = (rel: string) => readFileSync(path.join(RAIZ, rel), "utf-8");

function tsxs(dir: string, out: string[] = []): string[] {
  for (const e of readdirSync(dir)) {
    const p = path.join(dir, e);
    if (statSync(p).isDirectory()) tsxs(p, out);
    else if (e.endsWith(".tsx")) out.push(p);
  }
  return out;
}

/** La ÚNICA excepción declarada al relleno: el micrófono usa el azul pleno
 * como ESTADO de "grabando", no como botón. Un estado activo sí puede ser
 * una mancha. */
const EXCEPCIONES_RELLENO = [path.join("ui", "CampoConVoz.tsx")];

describe("el azul es tinta, no mancha", () => {
  it("ningún botón del frente usa relleno azul con texto blanco", () => {
    const culpables: string[] = [];
    for (const p of tsxs(RAIZ)) {
      const rel = path.relative(RAIZ, p);
      if (EXCEPCIONES_RELLENO.some((e) => rel.endsWith(e))) continue;
      for (const [i, l] of readFileSync(p, "utf-8").split("\n").entries()) {
        if (l.includes("bg-accent ") && l.includes("text-white")) culpables.push(`${rel}:${i + 1}`);
      }
    }
    expect(culpables, `estos botones volvieron al relleno azul: ${culpables.join(", ")}`).toEqual([]);
  });

  it("la constante de la casa dice el tratamiento completo", () => {
    expect(BOTON_ESTANDAR).toContain("border-accent/40");
    expect(BOTON_ESTANDAR).toContain("bg-accent/10");
    expect(BOTON_ESTANDAR).toContain("text-accent");
    expect(BOTON_ESTANDAR).not.toContain("text-white");
  });
});

describe("dentro de una página, todos los botones son iguales", () => {
  it("el secundario y el primario son EXACTAMENTE el mismo estilo", () => {
    // Decisión explícita: "cancelar que sea igual que guardar". La jerarquía
    // la carga el héroe contra el resto, no un botón contra su vecino.
    expect(BOTON_SECUNDARIO).toBe(BOTON_ESTANDAR);
    expect(BOTON_PRIMARIO).toBe(BOTON_ESTANDAR);
  });

  it("los botones de cancelar visten como su hermano, no como texto apagado", () => {
    // El fallo que esto caza: un "Cancelar" que se queda en text-dim pelado
    // junto a un botón con caja, que es lo que había antes de la decisión.
    for (const rel of ["ui/DetalleActividad.tsx", "ui/CorregirCifras.tsx", "ui/CuentaCliente.tsx"]) {
      const fuente = leer(rel);
      // La ETIQUETA del botón, no la palabra suelta: un comentario que diga
      // "Cancelar descarta todo" no es un botón.
      const etiquetas: number[] = [];
      for (let i = fuente.indexOf("Cancelar"); i > -1; i = fuente.indexOf("Cancelar", i + 1)) {
        if (fuente.slice(i, i + 45).includes("</button>")) etiquetas.push(i);
      }
      expect(etiquetas.length, `${rel} deberia tener al menos un boton Cancelar`).toBeGreaterThan(0);
      for (const i of etiquetas) {
        const apertura = fuente.lastIndexOf("<button", i);
        expect(fuente.slice(apertura, i), `${rel}: el Cancelar de la posicion ${i} no viste como su hermano`).toContain(
          "bg-accent/10"
        );
      }
    }
  });
});

describe("el héroe: uno por pantalla, y solo donde se abre camino", () => {
  const HEROES = ["idea/[id]/IdeaView.tsx", "nueva/page.tsx", "ui/ManosALaObra.tsx"];

  it("los momentos que abren camino usan BotonHeroe", () => {
    for (const rel of HEROES) expect(leer(rel)).toContain("<BotonHeroe");
  });

  it("el héroe lleva sus chispas y respeta 'menos movimiento'", () => {
    const comp = leer("ui/BotonHeroe.tsx");
    expect(comp).toContain("chispa");
    expect(comp).toContain("aria-hidden");
    const css = readFileSync(path.join(RAIZ, "globals.css"), "utf-8");
    expect(css).toContain(".boton-heroe");
    // el bloque de reduced-motion nombra al héroe: sin movimiento, sin chispas
    const iReduce = css.indexOf("prefers-reduced-motion", css.indexOf(".boton-heroe"));
    expect(iReduce).toBeGreaterThan(-1);
    expect(css.slice(iReduce)).toContain("boton-heroe");
  });

  it("el héroe NO invade el doble CTA de peso igual (canon 04)", () => {
    // "Seguimos explorando" y su pareja pesan lo mismo a propósito: es la
    // honestidad inversa de la oferta. Un héroe ahí rompería la decisión.
    const fuente = leer("idea/[id]/IdeaView.tsx");
    const i = fuente.indexOf("Seguimos explorando");
    expect(i).toBeGreaterThan(-1);
    const bloque = fuente.slice(i - 700, i + 700);
    expect(bloque).not.toContain("<BotonHeroe");
  });
});

describe("el intercambiador de caras", () => {
  it("tiene su luz deslizante y NO late (nada parpadea en bucle)", () => {
    const fuente = leer("ui/SelectorCara.tsx");
    expect(fuente).toContain("cambiador-luz");
    const css = readFileSync(path.join(RAIZ, "globals.css"), "utf-8");
    const i = css.indexOf(".cambiador-luz");
    expect(i).toBeGreaterThan(-1);
    // ninguna animación en bucle sobre la luz
    expect(css.slice(i, i + 600)).not.toContain("animation");
  });

  it("mueve la luz con la MISMA propiedad que el CSS anima", () => {
    // La avería de origen (cazada por el fundador, ago 2026): el CSS animaba
    // `transform` y el componente movía la luz con `left`. Como left no estaba
    // en la lista de transiciones, el salto horizontal era instantáneo: la luz
    // se teletransportaba y solo el ancho rebotaba. Nada fallaba, solo no
    // animaba. Este assert ata las dos mitades.
    const fuente = leer("ui/SelectorCara.tsx");
    const css = readFileSync(path.join(RAIZ, "globals.css"), "utf-8");
    const regla = css.slice(css.indexOf(".cambiador-luz"), css.indexOf(".cambiador-luz") + 400);
    const transicion = regla.slice(regla.indexOf("transition:"), regla.indexOf("}"));

    expect(fuente).toContain("translateX(");
    expect(transicion).toContain("transform");
    expect(transicion).toContain("width");
    // y no la mueve por el carril viejo, que la transición no cubre
    expect(fuente).not.toContain("left: ind.left");
  });

  it("coloca la luz sin transición en el montaje (no entra volando)", () => {
    const fuente = leer("ui/SelectorCara.tsx");
    expect(fuente).toContain('transition: "none"');
  });
});
