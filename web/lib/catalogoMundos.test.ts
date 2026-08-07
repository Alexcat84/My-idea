import { readFileSync } from "node:fs";
import path from "node:path";
import { describe, expect, it } from "vitest";
import { MUNDOS, estaPublicado, filtrarVisibles, mundo, mundosVisibles, nombreDeMundo } from "./catalogoMundos";
import { PRECIOS } from "./precios";

const RAIZ = path.resolve(__dirname, "..");
const leer = (rel: string) => readFileSync(path.join(RAIZ, rel), "utf-8");

/**
 * Los NUEVE mundos están publicados. Compras y entrega entraron ocultos el
 * 2026-08-07 y el fundador los publicó el mismo día.
 *
 * El mecanismo de ocultar sigue vivo para el próximo mundo que nazca, y se
 * prueba con datos SINTÉTICOS (filtrarVisibles) justo porque ya no hay ningún
 * pack oculto de verdad: un mecanismo sin sujeto deja de estar probado sin que
 * nadie lo note, y se descubriría roto el día que hiciera falta.
 */
const NUEVOS = ["compras", "entrega"];

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
    //
    // Se revisan las CLAVES de cada pack, no el texto del archivo: el
    // comentario del catálogo nombra los campos para explicar por qué se
    // fueron, y un grep crudo confundiría esa explicación con una recaída.
    for (const m of MUNDOS) {
      expect(Object.keys(m).sort().join(","), m.clave).toBe("clave,nombre,promesa");
    }
    expect(PRECIOS.mundo_activar).toBe(5);
  });

  it("los nueve están publicados: ninguno queda escondido", () => {
    const visibles = mundosVisibles().map((m) => m.clave);
    expect(visibles).toHaveLength(9);
    for (const clave of NUEVOS) {
      expect(visibles, `${clave} no se está ofreciendo`).toContain(clave);
      expect(estaPublicado(clave)).toBe(true);
    }
  });

  it("se resuelven por clave, con su nombre y su promesa", () => {
    for (const clave of NUEVOS) {
      expect(mundo(clave), clave).toBeDefined();
      expect(nombreDeMundo(clave)).not.toBe(clave);
      expect(mundo(clave)!.promesa.length).toBeGreaterThan(10);
      // su precio no sale de aquí: sale de precios.ts, igual que el de todos
      expect(mundo(clave)).not.toHaveProperty("creditos_activar");
    }
  });

  it("familia MEJORA: ninguno de los dos entra en los mundos de protección", () => {
    // Un mundo de protección arrastra el snapshot del núcleo y el reformulador
    // de anclaje. Compras y entrega no protegen nada: mejoran lo que ya haces.
    const espacios = leer("lib/espacios.ts");
    const linea = espacios.split("\n").find((l) => l.includes("MUNDOS_PROTECCION ="))!;
    for (const clave of NUEVOS) {
      expect(linea, `${clave} quedó como mundo de protección`).not.toContain(clave);
    }
  });

  it("ninguna vitrina importa el catálogo crudo para listar", () => {
    // La regla de la casa: una sola fuente. Quien LISTA mundos pasa por
    // mundosVisibles(); quien resuelve UNO por clave puede seguir usando el
    // .find de siempre sobre el JSON. La invariante que importa es que una
    // VITRINA no tenga en la mano la lista cruda: teniéndola, tarde o
    // temprano alguien la recorre entera y se salta el filtro.
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

describe("el mecanismo de ocultar, para el próximo mundo", () => {
  const CATALOGO_DE_PRUEBA = [
    { clave: "publicado", nombre: "Publicado", promesa: "Se ofrece." },
    { clave: "naciendo", nombre: "Naciendo", promesa: "Aún no se ofrece.", oculto: true },
  ];

  it("un pack oculto no se lista", () => {
    expect(filtrarVisibles(CATALOGO_DE_PRUEBA).map((m) => m.clave)).toEqual(["publicado"]);
  });

  it("la puerta del mini-gate lo revela sin publicarlo", () => {
    // Sin la puerta no habría mini-gate posible: un mundo sin tarjeta no tiene
    // por dónde empezar su preview, y no se podría caminar antes de decidir si
    // se publica. La puerta lo hace alcanzable, no ofrecido.
    const conPuerta = filtrarVisibles(CATALOGO_DE_PRUEBA, true).map((m) => m.clave);
    expect(conPuerta).toEqual(["publicado", "naciendo"]);
    // y abrirla no cambia el estado de publicación de nadie
    expect(filtrarVisibles(CATALOGO_DE_PRUEBA)).toHaveLength(1);
  });

  it("y un mundo sin publicar se vería MARCADO", () => {
    // Un paseo de prueba que se ve igual que un mundo en venta es la confusión
    // que hay que evitar: la tarjeta lleva su marca cuando el pack está oculto.
    const fuente = leer("app/ui/PotenciaTuIdea.tsx");
    expect(fuente).toContain("sin publicar");
    expect(fuente).toContain("p.oculto &&");
    // la puerta llega desde la URL, no está encendida en el código
    expect(leer("app/idea/[id]/IdeaView.tsx")).toContain('searchParams.get("ver") === "ocultos"');
  });
});
