import { readFileSync } from "node:fs";
import path from "node:path";
import { describe, expect, it } from "vitest";
import { MUNDOS, estaPublicado, mundo, mundosVisibles, nombreDeMundo } from "./catalogoMundos";
import { PRECIOS } from "./precios";

const RAIZ = path.resolve(__dirname, "..");
const leer = (rel: string) => readFileSync(path.join(RAIZ, rel), "utf-8");

/**
 * LA PUBLICACIÓN ES UN INTERRUPTOR DEL FUNDADOR.
 *
 * Compras y entrega están integrados en el grafo, cableados y cobrables, pero
 * NO se ofrecen hasta que el fundador los camine (preview, plan y hub sobre su
 * proyecto real) y dé su visto. Estos tests son el pestillo: si alguien los
 * publica sin querer, o añade una vitrina nueva que no respete `oculto`, esto
 * se pone rojo.
 */
const OCULTOS_HASTA_EL_VISTO = ["compras", "entrega"];

describe("el catálogo de mundos", () => {
  it("tiene los nueve mundos, con los dos nuevos por su nombre de cara", () => {
    expect(MUNDOS).toHaveLength(9);
    expect(nombreDeMundo("compras")).toBe("Tu Compra Correcta");
    expect(nombreDeMundo("entrega")).toBe("Del Taller a sus Manos");
  });

  it("el catálogo NO guarda precios: los guarda precios.ts y nadie más", () => {
    // El catálogo los llevaba y envejecieron en silencio: decían 3 y 2 mientras
    // se cobraban 5, porque quien cobra (montoDelPlan) y quien pinta la tarjeta
    // leen precios.ts. Se quitaron en vez de alinearlos, que es lo único que
    // impide que se vuelvan a separar.
    // Se revisan las CLAVES de cada pack, no el texto del archivo: el
    // comentario del catalogo nombra los campos para explicar por que se
    // fueron, y un grep crudo confundiria esa explicacion con una recaida.
    for (const m of MUNDOS) {
      expect(Object.keys(m).sort().join(","), m.clave)
        .toMatch(/^(clave,nombre,oculto,promesa|clave,nombre,promesa)$/);
    }
    // y el mundo cuesta lo que dice la única fuente
    expect(PRECIOS.mundo_activar).toBe(5);
  });

  it("los dos nuevos NO se listan: siguen ocultos hasta el visto del fundador", () => {
    const visibles = mundosVisibles().map((m) => m.clave);
    for (const clave of OCULTOS_HASTA_EL_VISTO) {
      expect(visibles, `${clave} se publicó sin el visto`).not.toContain(clave);
      expect(estaPublicado(clave)).toBe(false);
    }
    expect(visibles).toHaveLength(7);
  });

  it("la puerta del mini-gate los revela sin publicarlos", () => {
    // Sin la puerta no habria mini-gate posible: un mundo sin tarjeta no tiene
    // por donde empezar su preview, y el fundador no podria caminarlo antes de
    // decidir si lo publica. La puerta los hace alcanzables, no ofrecidos.
    const conPuerta = mundosVisibles(true).map((m) => m.clave);
    for (const clave of OCULTOS_HASTA_EL_VISTO) expect(conPuerta).toContain(clave);
    expect(conPuerta).toHaveLength(9);
    // y abrirla NO cambia el estado de publicacion de nadie
    for (const clave of OCULTOS_HASTA_EL_VISTO) expect(estaPublicado(clave)).toBe(false);
    // la puerta es explicita: por defecto sigue cerrada
    expect(mundosVisibles()).toHaveLength(7);
  });

  it("un mundo sin publicar se ve MARCADO como tal", () => {
    // Un paseo de prueba que se ve igual que un mundo en venta es la confusion
    // que hay que evitar: la tarjeta lleva su marca cuando el pack esta oculto.
    const fuente = leer("app/ui/PotenciaTuIdea.tsx");
    expect(fuente).toContain("sin publicar");
    expect(fuente).toContain("p.oculto &&");
    // y la puerta llega desde la URL, no esta encendida en el codigo
    expect(leer("app/idea/[id]/IdeaView.tsx")).toContain('searchParams.get("ver") === "ocultos"');
  });

  it("pero SÍ se resuelven por clave: ocultar no es romper", () => {
    // El fundador camina el mundo por URL en su mini-gate. Tiene que ver su
    // nombre y su precio de verdad, no un hueco ni "mundo desconocido".
    for (const clave of OCULTOS_HASTA_EL_VISTO) {
      expect(mundo(clave), clave).toBeDefined();
      expect(nombreDeMundo(clave)).not.toBe(clave);
      expect(mundo(clave)!.promesa.length).toBeGreaterThan(10);
      // su precio no sale de aqui: sale de precios.ts, igual que el de todos
      expect(mundo(clave)).not.toHaveProperty("creditos_activar");
    }
  });

  it("familia MEJORA: ninguno de los dos entra en los mundos de protección", () => {
    // Un mundo de protección arrastra el snapshot del núcleo y el reformulador
    // de anclaje. Compras y entrega no protegen nada: mejoran lo que ya haces.
    const espacios = leer("lib/espacios.ts");
    const linea = espacios.split("\n").find((l) => l.includes("MUNDOS_PROTECCION ="))!;
    for (const clave of OCULTOS_HASTA_EL_VISTO) {
      expect(linea, `${clave} quedó como mundo de protección`).not.toContain(clave);
    }
  });

  it("ninguna vitrina importa el catálogo crudo para listar", () => {
    // La regla de la casa: una sola fuente. Quien LISTA mundos pasa por
    // mundosVisibles(); quien resuelve UNO por clave puede seguir usando el
    // .find de siempre sobre el JSON. La invariante que importa es que una
    // VITRINA no tenga en la mano la lista cruda: teniéndola, tarde o
    // temprano alguien la recorre entera y se salta el pestillo.
    for (const archivo of ["app/creditos/page.tsx", "app/ui/PotenciaTuIdea.tsx"]) {
      const fuente = leer(archivo);
      expect(fuente, `${archivo} tiene el catálogo crudo a mano`)
        .not.toContain("assets/packs_catalog.json");
      expect(fuente).toContain("mundosVisibles");
    }
    // y el espejo de nombres que vivía en ideas.ts no puede volver
    expect(leer("lib/ideas.ts")).not.toContain("NOMBRE_MUNDO");
  });
});
