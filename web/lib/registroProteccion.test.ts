/**
 * Mundos de protección (P3) — el registro visible.
 *
 * Lo que se vigila: la severidad SIEMPRE en palabras y JAMÁS en puntajes (patrón
 * del test del colchón de esperas), el ruido cero (un mundo sin enlaces todavía
 * dice honesto que se llenará, en vez de fingir un registro), y que la pantalla
 * y el papel salgan del MISMO armador.
 */
import { readFileSync } from "node:fs";
import path from "node:path";
import { describe, expect, it } from "vitest";
import {
  armarRegistro,
  PALABRA_CAMINO,
  registroMarkdown,
  severidadEnPalabras,
  textoProtege,
  type ActividadProtegida,
  type FilaRespuesta,
} from "./registroProteccion";

const NUCLEO: ActividadProtegida[] = [
  { id: "nuc-a", indice: 1, titulo: "Cierra el acuerdo con el proveedor" },
  { id: "nuc-b", indice: 2, titulo: "Compra el lote inicial" },
];

function respuesta(over: Partial<FilaRespuesta> & { id: string }): FilaRespuesta {
  return {
    texto: "Consigue un proveedor alterno",
    etapa: 1,
    orden: 1,
    estado: "pendiente",
    protege_item: null,
    deteccion: null,
    probabilidad: null,
    dolor: null,
    ...over,
  };
}

describe("qué entra al registro", () => {
  it("una respuesta enlazada entra con su detección, su severidad y a qué protege", () => {
    const [e] = armarRegistro(
      [
        respuesta({
          id: "r1",
          deteccion: "depende de un solo proveedor",
          protege_item: "nuc-a",
          probabilidad: "probable",
          dolor: "mucho",
        }),
      ],
      NUCLEO
    );
    expect(e.deteccion).toBe("depende de un solo proveedor");
    expect(e.protege).toMatchObject({ indice: 1, titulo: "Cierra el acuerdo con el proveedor" });
    expect(textoProtege(e)).toBe("#1 · Cierra el acuerdo con el proveedor");
  });

  it("una respuesta SISTÉMICA dice que protege al negocio entero, sin fingir un enlace", () => {
    const [e] = armarRegistro(
      [respuesta({ id: "r1", deteccion: "no hay respaldo de los datos", protege_item: null })],
      NUCLEO
    );
    expect(e.protege).toBeNull();
    expect(textoProtege(e)).toBe("tu negocio entero");
  });

  it("una tarea sin detección, sin enlace y sin severidad NO se inventa como fila", () => {
    // Si la estimación o el enlazador fallaron, la tarea existe en el plan pero
    // no es una respuesta a nada: el registro no la disfraza de hallazgo.
    expect(armarRegistro([respuesta({ id: "r1" })], NUCLEO)).toEqual([]);
  });

  it("se ordena por etapa y luego por orden", () => {
    const r = armarRegistro(
      [
        respuesta({ id: "c", etapa: 2, orden: 1, deteccion: "c" }),
        respuesta({ id: "a", etapa: 1, orden: 1, deteccion: "a" }),
        respuesta({ id: "b", etapa: 1, orden: 2, deteccion: "b" }),
      ],
      NUCLEO
    );
    expect(r.map((e) => e.id)).toEqual(["a", "b", "c"]);
  });

  it("si lo protegido ya no está, lo DICE en vez de callarlo", () => {
    const [e] = armarRegistro(
      [respuesta({ id: "r1", deteccion: "algo", protege_item: "borrado-hace-tiempo" })],
      NUCLEO
    );
    expect(e.protegidaDesaparecida).toBe(true);
    expect(textoProtege(e)).toBe("la actividad que protegía ya no está en tu plan");
  });
});

describe("LA SEVERIDAD: en palabras, jamás en puntajes", () => {
  it("las dos mitades juntas se leen como una frase de persona", () => {
    expect(severidadEnPalabras({ probabilidad: "muy_probable", dolor: "mucho" })).toBe(
      "muy probable y dolería mucho"
    );
    expect(severidadEnPalabras({ probabilidad: "poco_probable", dolor: "poco" })).toBe(
      "poco probable y dolería poco"
    );
  });

  it("con una sola mitad se dice esa; sin ninguna, se CALLA (nada de 'sin definir')", () => {
    expect(severidadEnPalabras({ probabilidad: "probable", dolor: null })).toBe("probable");
    expect(severidadEnPalabras({ probabilidad: null, dolor: "bastante" })).toBe("dolería bastante");
    expect(severidadEnPalabras({ probabilidad: null, dolor: null })).toBeNull();
  });

  it("el documento no contiene NINGÚN puntaje, porcentaje ni escala numérica", () => {
    const md = registroMarkdown("Riesgos Bajo Control", [
      ...armarRegistro(
        [
          respuesta({
            id: "r1",
            deteccion: "depende de un solo proveedor",
            protege_item: "nuc-a",
            probabilidad: "muy_probable",
            dolor: "mucho",
          }),
        ],
        NUCLEO
      ),
    ]);
    expect(md).toContain("muy probable y dolería mucho");
    // ni puntajes, ni porcentajes, ni "riesgo 8", ni matrices de colores
    expect(md).not.toMatch(/\b\d+\s*(\/|de)\s*\d+\b/);
    expect(md).not.toMatch(/%/);
    for (const teatro of ["puntaje", "score", "rojo", "amarillo", "verde", "crítico", "severidad alta"]) {
      expect(md.toLowerCase()).not.toContain(teatro);
    }
  });

  it("el módulo no calcula ningún número de riesgo (contrato sobre su fuente)", () => {
    const fuente = readFileSync(path.join(__dirname, "registroProteccion.ts"), "utf-8");
    // nada de multiplicar probabilidad por impacto: esa es justo la matriz que engaña
    expect(fuente).not.toMatch(/probabilidad\s*\*\s*/);
    expect(fuente).not.toMatch(/Math\.(round|max|min)\(.*dolor/);
  });
});

describe("EL CAMINO en la fila: se muestra cuando existe, se calla cuando no", () => {
  it("con camino, el documento lo dice en palabras de persona", () => {
    const md = registroMarkdown(
      "Riesgos Bajo Control",
      armarRegistro(
        [respuesta({ id: "r1", deteccion: "depende de un solo proveedor", protege_item: "nuc-a", camino: "mitigar" })],
        NUCLEO
      )
    );
    expect(md).toContain("El camino: reducirlo.");
  });

  it("sin camino, NO hay línea de camino (nada de 'sin clasificar')", () => {
    const md = registroMarkdown(
      "Riesgos Bajo Control",
      armarRegistro([respuesta({ id: "r1", deteccion: "algo", protege_item: "nuc-a" })], NUCLEO)
    );
    expect(md).not.toContain("El camino:");
    expect(md.toLowerCase()).not.toContain("sin clasificar");
  });

  it("los cuatro caminos tienen su palabra y ninguna es un tecnicismo", () => {
    expect(PALABRA_CAMINO).toEqual({
      evitar: "evitarlo",
      mitigar: "reducirlo",
      transferir: "pasárselo a otro",
      aceptar: "aceptarlo con los ojos abiertos",
    });
  });
});

describe("RUIDO CERO: el mundo sin enlaces todavía", () => {
  // AUD-09 M48: el registro solo se muestra con el plan ya entregado; vacío es
  // que el enlace falló (antes decía "se llenará con el plan", que era falso).
  it("el registro vacío dice que el enlace no se armó", () => {
    const md = registroMarkdown("Riesgos Bajo Control", []);
    expect(md).toContain("No alcancé a enlazar este plan con tus actividades");
    // y no finge filas ni encabezados de tabla vacíos
    expect(md).not.toContain("###");
  });

  it("el markdown lleva el nombre del mundo en su título", () => {
    expect(registroMarkdown("Seguridad Digital", [])).toContain("## Registro de Seguridad Digital");
  });
});

describe("pantalla y papel salen del MISMO armador", () => {
  it("el markdown usa las mismas frases de severidad y de protección", () => {
    const entradas = armarRegistro(
      [
        respuesta({
          id: "r1",
          texto: "Consigue un proveedor alterno y pide su cotización",
          deteccion: "depende de un solo proveedor",
          protege_item: "nuc-a",
          probabilidad: "probable",
          dolor: "mucho",
        }),
      ],
      NUCLEO
    );
    const md = registroMarkdown("Riesgos Bajo Control", entradas);
    expect(md).toContain(severidadEnPalabras(entradas[0])!);
    expect(md).toContain(textoProtege(entradas[0]));
    expect(md).toContain("Consigue un proveedor alterno y pide su cotización");
  });
});

// AUD-09 M15 (decisión del fundador, 25 sep 2026): la protección apunta al NODO
// de la tarea, no al id de la tarea de un ciclo. Hoy, un seguimiento del núcleo
// inserta tareas con ids nuevos y todo el registro pasa a "la actividad que
// protegía ya no está en tu plan", y las anclas de fecha desaparecen sin aviso.
import { resolverProtegido } from "./registroProteccion";

describe("la protección sobrevive a un ciclo nuevo del núcleo (AUD-09 M15)", () => {
  // Ciclo 1: la respuesta protegía la tarea "c1-a" (nodo precio_de_venta).
  // Ciclo 2 (vigente): la misma tarea renace como "c2-a" con el mismo nodo.
  const vigente = [
    { id: "c2-a", indice: 1, titulo: "Fija tu precio de venta", nodos_origen: ["precio_de_venta"] },
    { id: "c2-b", indice: 2, titulo: "Consigue tu primer cliente", nodos_origen: ["primer_cliente"] },
  ];

  it("se resuelve contra el plan vigente por el nodo, aunque el id del ciclo viejo ya no exista", () => {
    const [e] = armarRegistro(
      [{ id: "r1", texto: "Revisa el costo antes", etapa: 1, orden: 1, estado: "pendiente", protege_item: "c1-a", protege_nodos: ["precio_de_venta"] }],
      vigente
    );
    expect(e.protege?.id).toBe("c2-a");
    expect(e.protegidaDesaparecida).toBe(false);
  });

  it("si el nodo ya no está en el plan vigente, se dice en claro", () => {
    const [e] = armarRegistro(
      [{ id: "r1", texto: "Algo", etapa: 1, orden: 1, estado: "pendiente", protege_item: "c1-z", protege_nodos: ["nodo_que_se_fue"] }],
      vigente
    );
    expect(e.protege).toBeNull();
    expect(e.protegidaDesaparecida).toBe(true);
    expect(textoProtege(e)).toBe("la actividad que protegía ya no está en tu plan");
  });

  it("resolverProtegido: sin nodos (filas viejas) se resuelve por id, como antes", () => {
    expect(resolverProtegido({ protege_item: "c2-b", protege_nodos: null }, vigente)).toBe("c2-b");
    expect(resolverProtegido({ protege_item: "c1-a", protege_nodos: null }, vigente)).toBeNull();
  });

  // nodos_origen se guarda por ETAPA: dos tareas de la misma etapa comparten
  // nodos. Dentro del MISMO ciclo el id sigue vivo y manda; el nodo solo
  // resuelve cuando el id ya no está en el plan vigente.
  it("en el mismo ciclo manda el id, aunque otra tarea de la etapa comparta el nodo", () => {
    const mismaEtapa = [
      { id: "c2-a", nodos_origen: ["precio_de_venta"] },
      { id: "c2-z", nodos_origen: ["precio_de_venta"] },
    ];
    expect(resolverProtegido({ protege_item: "c2-z", protege_nodos: ["precio_de_venta"] }, mismaEtapa)).toBe("c2-z");
  });

  // Las actividades del registro vienen SIN las retiradas. Si la protegida se
  // retiró en el MISMO ciclo, su id sigue en el plan vigente: el nodo no puede
  // mudarla a una hermana de etapa (sería afirmar una protección que nadie hizo).
  it("una protegida retirada en el mismo ciclo no salta a otra tarea de su etapa", () => {
    const sinRetiradas = [{ id: "c2-a", indice: 1, titulo: "Fija tu precio de venta", nodos_origen: ["precio_de_venta"] }];
    const idsDelPlan = new Set(["c2-a", "c2-retirada"]);
    const [e] = armarRegistro(
      [{ id: "r1", texto: "Algo", etapa: 1, orden: 1, estado: "pendiente", protege_item: "c2-retirada", protege_nodos: ["precio_de_venta"] }],
      sinRetiradas,
      idsDelPlan
    );
    expect(e.protege).toBeNull();
    expect(e.protegidaDesaparecida).toBe(true);
  });
});
