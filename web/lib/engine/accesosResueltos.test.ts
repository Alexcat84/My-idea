import { readFileSync } from "node:fs";
import path from "node:path";
import { describe, expect, it } from "vitest";
import { seleccionarAfines } from "../compass";
import {
  cargarEntrySeeds,
  conceptosDeRuta,
  esOfrecible,
  faseDeNodo,
  preguntaDeNodo,
  resumenNodo,
  type Grafo,
  type PreguntasCache,
} from "./graph";
import { aMaterial, prepararPlan } from "./planRedactor";

/**
 * FASE 0 DE LA PASADA UNICA: LOS ACCESOS DIRECTOS AL GRAFO PASAN POR EL RESOLUTOR.
 *
 * `OP-S-08` clasifico 42 accesos al grafo por el origen del id. Los que reciben un
 * id que viene de FUERA (de la sesion guardada, de un asset, del indice semantico)
 * pueden recibir un id de otra era, y la pasada unica es exactamente lo que MUEVE
 * IDS. Sin estas guardas, una fusion bien hecha produce un sintoma semanas despues
 * en el recorrido de una persona.
 *
 * EL CRITERIO DE HECHO de la fase 08: una prueba que hoy pase en verde no sirve.
 * Cada bloque de aqui SE CAE contra el codigo anterior a su operacion.
 */
const RAIZ = path.resolve(__dirname, "..", "..");
const leer = (rel: string) => readFileSync(path.join(RAIZ, rel), "utf-8");

/**
 * Las dos formas en que un id llega viejo, las dos reales en el grafo de hoy:
 *   `absorbido`  es nodo, deprecado, y el superviviente lo lista en `ids_alias`;
 *   `borrado`    NO es nodo (la era en que fusionar borraba: 77 alias asi).
 */
const GRAFO: Grafo = {
  superviviente: {
    node_id: "superviviente",
    fase_proyecto: "validacion",
    dominio: "core",
    titulo_concepto: "El concepto que hoy representa esa historia",
    resumen_teorico: "el resumen vigente",
    pasos_accionables: ["paso vigente uno", "paso vigente dos", "paso vigente tres"],
    entregable_esperado: "el entregable vigente",
    ids_alias: ["absorbido", "borrado"],
    nodos_siguientes: ["vecino"],
  },
  absorbido: {
    node_id: "absorbido",
    fase_proyecto: "ideacion",
    dominio: "core",
    titulo_concepto: "El concepto viejo que se fundio dentro",
    resumen_teorico: "el resumen viejo",
    pasos_accionables: ["paso viejo unico"],
    entregable_esperado: "el entregable viejo",
    deprecado: true,
  },
  vecino: {
    node_id: "vecino",
    fase_proyecto: "validacion",
    dominio: "core",
    titulo_concepto: "Un vecino vivo",
    resumen_teorico: "x",
    pasos_accionables: ["paso del vecino"],
    entregable_esperado: "entregable del vecino",
  },
};

describe("OP-C-01 - aMaterial: el material del plan se arma tras resolver", () => {
  it("un id DEPRECADO con alias vivo aporta el material del SUPERVIVIENTE, no el suyo", () => {
    // Hoy `aMaterial` hace `graph[nid]` a secas: le entrega al redactor el texto
    // del nodo que se fundio dentro de otro, o sea la version que la fusion
    // declaro peor. No rompe nada, y por eso no lo caza ninguna prueba verde.
    const m = aMaterial("absorbido", GRAFO, {});
    expect(m.concepto).toBe("El concepto que hoy representa esa historia");
    expect(m.pasos).toEqual(["paso vigente uno", "paso vigente dos", "paso vigente tres"]);
    expect(m.entregable).toBe("el entregable vigente");
  });

  it("un id que YA NO ES NODO aporta material en vez de reventar", () => {
    // 77 de los 285 alias del grafo real apuntan a ids que no existen como nodo.
    // Hoy `graph[nid]` es undefined y la lectura del titulo lanza TypeError: el
    // plan entero se cae por una referencia historica legitima.
    const m = aMaterial("borrado", GRAFO, {});
    expect(m.concepto).toBe("El concepto que hoy representa esa historia");
    expect(m.pasos.length).toBeGreaterThan(0);
  });

  it("la RUTA con un id historico produce un plan con TODOS sus conceptos", () => {
    const ruta = ["absorbido", "vecino"];
    const { payload } = prepararPlan(ruta, GRAFO, {}, "una idea cualquiera", null, null, false, null);
    expect(payload.material_principal).toHaveLength(ruta.length);
    const conceptos = payload.material_principal.map((m) => m.concepto);
    expect(conceptos).toContain("El concepto que hoy representa esa historia");
    expect(conceptos, "el plan cita el texto que la fusion declaro peor").not.toContain(
      "El concepto viejo que se fundio dentro"
    );
  });

  it("la IDENTIDAD del material sigue siendo el id de la ruta, no el resuelto", () => {
    // El contrato de PROCEDENCIA (verificarProcedenciaEtapas y
    // nodosPorEtapaValidados) valida los ids que el redactor autodeclara contra
    // `ruta + cosecha` CRUDAS. Si el material entrara con el id resuelto, el
    // redactor declararia un id que no esta en la ruta y la procedencia lo
    // marcaria invalida: se arreglaria el concepto rompiendo el sensor.
    expect(aMaterial("absorbido", GRAFO, {}).id).toBe("absorbido");
  });

  it("el remache: aMaterial resuelve antes de leer el nodo", () => {
    const src = leer("lib/engine/planRedactor.ts");
    expect(src, "volvio el acceso directo al grafo").toMatch(
      /export function aMaterial[\s\S]{0,300}resolverId/
    );
  });
});

describe("OP-C-01 - las semillas del organizador pasan por la puerta unica", () => {
  it("una semilla DEPRECADA no llega a las puertas que se le ofrecen al usuario", () => {
    const semillas = cargarEntrySeeds();
    expect(semillas.length).toBeGreaterThan(0);
    // El grafo minimo que el organizador mira: las semillas reales, con la
    // primera fundida dentro de otro nodo.
    const grafo: Grafo = {};
    for (const s of semillas) {
      grafo[s] = {
        node_id: s,
        fase_proyecto: "ideacion",
        dominio: "core",
        titulo_concepto: s,
        resumen_teorico: "x",
      };
    }
    grafo[semillas[0]].deprecado = true;
    const ofrecidas = cargarEntrySeeds(grafo);
    expect(ofrecidas, "el organizador abre el recorrido por un nodo fundido").not.toContain(
      semillas[0]
    );
    for (const s of ofrecidas) expect(esOfrecible(s, grafo)).toBe(true);
  });

  it("el remache: los DOS organizadores piden las semillas CON el grafo", () => {
    // `cargarEntrySeeds` ya filtra por la puerta unica cuando recibe el grafo.
    // Los dos organizadores la llamaban sin el, asi que la puerta existia y no
    // estaba cableada en el unico camino por el que entra un usuario nuevo.
    for (const ruta of ["app/api/organizer/route.ts", "app/api/organizer/stream/route.ts"]) {
      const src = leer(ruta);
      expect(src, `${ruta} pide las semillas sin el grafo`).toContain("cargarEntrySeeds(graph)");
      expect(src, `${ruta} conserva la llamada cruda`).not.toContain("cargarEntrySeeds()");
    }
  });
});

describe("OP-C-01 - el indice semantico no ofrece lo que ya no es nodo", () => {
  // El indice guarda ids, y es una de las fuentes externas que OP-S-08
  // identifico: su copia se genera con un corte del grafo y la pasada mueve
  // ids DESPUES. `compass.ts` tenia el unico HUECO AL REVES del inventario: la
  // guarda estaba escrita `opts.graph && opts.graph[id] && !esOfrecible(...)`,
  // asi que un id DESCONOCIDO hacia falsa la condicion entera y PASABA.
  const comoLoVeElIndice = {
    superviviente: { dominio: "core", ids_alias: ["absorbido", "borrado"] },
    absorbido: { dominio: "core", deprecado: true },
  };

  it("un id del indice que ya no es nodo de ninguna era NO se ofrece", () => {
    const r = seleccionarAfines(
      [
        { id: "jamas_fue_un_nodo", score: 0.9 },
        { id: "superviviente", score: 0.5 },
      ],
      new Set(),
      { graph: comoLoVeElIndice, k: 8, minScore: 0.0 }
    );
    expect(r.map((c) => c.id), "el indice ofrecio un id que no existe").not.toContain(
      "jamas_fue_un_nodo"
    );
    expect(r.map((c) => c.id)).toContain("superviviente");
  });

  it("un id del indice de otra era se ofrece RESUELTO, no crudo ni descartado", () => {
    const r = seleccionarAfines([{ id: "borrado", score: 0.9 }], new Set(), {
      graph: comoLoVeElIndice,
      k: 8,
      minScore: 0.0,
    });
    expect(r.map((c) => c.id)).toEqual(["superviviente"]);
  });

  it("un deprecado del indice se ofrece por su superviviente, y una sola vez", () => {
    const r = seleccionarAfines(
      [
        { id: "absorbido", score: 0.9 },
        { id: "superviviente", score: 0.8 },
      ],
      new Set(),
      { graph: comoLoVeElIndice, k: 8, minScore: 0.0 }
    );
    expect(r.map((c) => c.id)).toEqual(["superviviente"]);
  });

  it("lo excluido se excluye tambien cuando el indice lo nombra por su id viejo", () => {
    const r = seleccionarAfines([{ id: "borrado", score: 0.9 }], new Set(["superviviente"]), {
      graph: comoLoVeElIndice,
      k: 8,
      minScore: 0.0,
    });
    expect(r).toEqual([]);
  });

  it("sin grafo la brujula no resuelve ni filtra: el caller viejo ve lo crudo", () => {
    const r = seleccionarAfines([{ id: "borrado", score: 0.9 }], new Set(), {
      k: 8,
      minScore: 0.0,
    });
    expect(r.map((c) => c.id)).toEqual(["borrado"]);
  });
});

/**
 * OP-C-02: LOS DOS MAS CAROS DEL INVENTARIO, y no porque rompan: PORQUE CALLAN.
 * Ninguno lanza un error, ninguno aparece en una prueba verde, y los dos degradan
 * lo que el usuario ve: uno le quita conceptos a su plan y el otro le retrasa la
 * fase de su proyecto. Son exactamente el modo de fallo que el canon de fallar
 * ruidoso prohibe.
 */
describe("OP-C-02 - el plan de la sesion no pierde conceptos ni retrasa la fase", () => {
  it("267: la ruta con ids de otra era entrega UN concepto POR ID, no menos", () => {
    // El `.filter((nid) => nid in graph)` que vivia aqui dejaba caer de la lista
    // el id que ya no es nodo, y el estado vivo se comprimia con menos conceptos
    // de los que la persona recorrio. Sin aviso y sin excepcion.
    const ruta = ["absorbido", "vecino", "borrado"];
    const conceptos = conceptosDeRuta(ruta, GRAFO);
    expect(conceptos, "el plan salio mas corto que la ruta").toHaveLength(ruta.length);
    for (const nid of ruta) {
      expect(conceptos, `${nid} salio como id crudo`).not.toContain(nid);
    }
  });

  it("267: el concepto que se cita es el VIGENTE, no el que la fusion declaro peor", () => {
    const conceptos = conceptosDeRuta(["absorbido"], GRAFO);
    expect(conceptos).toEqual(["El concepto que hoy representa esa historia"]);
  });

  it("405: el ultimo nodo de otra era da SU fase, no ideacion", () => {
    // El `?? "ideacion"` no era un defecto razonable: era una degradacion
    // silenciosa. A la persona se le retrasaba la fase de su proyecto entero por
    // una referencia historica legitima.
    expect(faseDeNodo("absorbido", GRAFO)).toBe("validacion");
    expect(faseDeNodo("borrado", GRAFO)).toBe("validacion");
  });

  it("405: un id que JAMAS existio si cae al defecto declarado", () => {
    // El defecto sigue existiendo y sigue siendo el mismo: lo que cambia es que
    // deja de tragarse las referencias historicas legitimas.
    expect(faseDeNodo("jamas_fue_un_nodo", GRAFO)).toBe("ideacion");
  });

  it("el remache: la ruta del plan no lee el grafo a pelo en ninguno de los dos sitios", () => {
    const src = leer("app/api/session/[id]/plan/route.ts");
    expect(src).toContain("conceptosDeRuta(");
    expect(src).toContain("faseDeNodo(");
    expect(src, "volvio el filtro que dejaba caer conceptos").not.toContain("nid in graph");
    expect(src, "volvio la degradacion silenciosa de la fase").not.toContain('?? "ideacion"');
  });

  it("el remache: los dos ayudantes resuelven antes de leer", () => {
    const src = leer("lib/engine/graph.ts");
    expect(src).toMatch(/export function conceptosDeRuta[\s\S]{0,200}tituloDeNodo/);
    expect(src).toMatch(/export function faseDeNodo[\s\S]{0,200}resolverId/);
  });
});

/**
 * OP-C-03: los accesos que ROMPEN. A diferencia de OP-C-02, estos tres no callan:
 * lanzan TypeError o abortan el arranque de un mundo ya pagado. Que rompan no los
 * hace menos caros, los hace mas visibles.
 */
const CACHE: PreguntasCache = {
  superviviente: { pregunta: "La pregunta curada del que hoy representa esa historia" },
  absorbido: { pregunta: "La pregunta curada del que se fundio dentro" },
};

describe("OP-C-03 - resumenNodo, la pregunta del recorrido y el arranque de mundo", () => {
  it("resumenNodo de un id DEPRECADO cuenta la historia vigente", () => {
    const r = resumenNodo("absorbido", GRAFO, CACHE);
    expect(r.titulo).toBe("El concepto que hoy representa esa historia");
    expect(r.pregunta_cache).toBe("La pregunta curada del que hoy representa esa historia");
  });

  it("resumenNodo de un id que YA NO ES NODO devuelve el del superviviente en vez de reventar", () => {
    // Hoy `graph[nid]` es undefined y la lectura del titulo lanza TypeError: el
    // turno entero del interprete se cae al armar su contexto.
    const r = resumenNodo("borrado", GRAFO, CACHE);
    expect(r.titulo).toBe("El concepto que hoy representa esa historia");
    expect(r.pregunta_cache).toBe("La pregunta curada del que hoy representa esa historia");
  });

  it("la IDENTIDAD del resumen sigue siendo el id que se pidio", () => {
    // Misma razon que en aMaterial: el id del resumen es el del NODO ACTUAL de la
    // sesion, y la sesion guarda su ruta con los ids que recorrio.
    expect(resumenNodo("absorbido", GRAFO, CACHE).id).toBe("absorbido");
  });

  it("la pregunta de un nodo de otra era es la CURADA del vigente, no la generica", () => {
    // Dos averias en una linea: `graph[nid]` revienta con el id borrado, y
    // `cache[nid]` no encuentra la pregunta curada del superviviente, asi que
    // incluso cuando no reventaba entregaba la plantilla generica.
    expect(preguntaDeNodo("absorbido", GRAFO, CACHE)).toBe(
      "La pregunta curada del que hoy representa esa historia"
    );
    expect(preguntaDeNodo("borrado", GRAFO, CACHE)).toBe(
      "La pregunta curada del que hoy representa esa historia"
    );
  });

  it("sin pregunta curada, la generica se arma con el titulo VIGENTE y no revienta", () => {
    expect(preguntaDeNodo("borrado", GRAFO, {})).toContain(
      "El concepto que hoy representa esa historia"
    );
  });

  it("el remache: los dos sitios de recorrido piden la pregunta por el ayudante", () => {
    const src = leer("lib/engine/recorrido.ts");
    expect(src).toContain("preguntaDeNodo(nid, graph, preguntasCache)");
    expect(src).toContain("preguntaDeNodo(nuevoActualId, graph, preguntasCache)");
  });

  it("el remache: resumenNodo y preguntaDeNodo resuelven antes de leer", () => {
    const src = leer("lib/engine/graph.ts");
    expect(src).toMatch(/export function resumenNodo[\s\S]{0,200}resolverId/);
    expect(src).toMatch(/export function preguntaDeNodo[\s\S]{0,200}resolverId/);
  });

  it("el remache: clasificar recibe los seeds ya pasados por la puerta unica", () => {
    // clasificar.ts los lee a pelo en sus lineas 34, 35 y 36. Su texto dice que
    // los recibe filtrados, asi que quien filtra es quien los carga.
    const src = leer("app/api/session/start/route.ts");
    expect(src).toContain("cargarEntrySeeds(graph)");
    expect(src, "clasificar recibe la lista cruda del asset").not.toContain("cargarEntrySeeds()");
  });

  it("el remache: el arranque de mundo exige que la semilla RESUELVA, no que exista", () => {
    // Hoy avisa y ABORTA con un 503 cuando podria resolver y seguir: una semilla
    // renombrada por la pasada mata el arranque del mundo que la persona acaba de
    // pagar.
    const src = leer("app/api/project/[id]/world/[pack]/start/route.ts");
    expect(src).toContain("resolverId(brecha.semillaId, graph)");
    expect(src, "volvio el criterio de existir").not.toContain("brecha.semillaId in graph");
    // Y RESOLVER PARA SEGUIR: el mundo arranca en el nodo que resuelve, no en el
    // id viejo. Dejar el id viejo de nodo actual cambiaria un 503 ruidoso por un
    // recorrido mudo sin sucesores, que es peor.
    expect(src, "el mundo arranca en un id que puede no ser nodo").not.toContain(
      "graph[brecha.semillaId]"
    );
    expect(src).toContain("actualId: semillaId");
  });
});
