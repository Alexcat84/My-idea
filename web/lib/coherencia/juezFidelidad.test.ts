/**
 * El extractor del juez de fidelidad de la salida (corrida final, paso D; docs/producto/JUEZ_FIDELIDAD.md). Prueba
 * escrita ANTES que la implementacion (AGENTS.md). Las cuentas se hacen a mano en los comentarios y el valor esperado
 * sale de ahi, no de correr la funcion.
 *
 * El escenario: un proyecto con su Claridad (organizador), su plan del nucleo, un plan de mundo (calidad), un
 * seguimiento del nucleo, un replanteamiento del nucleo y un reporte de numeros (que NO se juzga).
 */
import { describe, expect, it } from "vitest";
import type { Grafo, NodoGrafo } from "../engine/graph";
import {
  armarSalidas,
  cuantasTrampas,
  FRASES_INVENCION,
  FRASES_PROCEDENCIA,
  plantarTrampas,
  SEMILLA_FIDELIDAD,
  tipoDeSalida,
  type ClavePaquete,
  type FilasJuez,
  type SalidaReal,
} from "./juezFidelidad";

const nodo = (id: string, extra: Partial<NodoGrafo> = {}): NodoGrafo => ({
  node_id: id,
  fase_proyecto: "validacion",
  titulo_concepto: `titulo interno de ${id}`,
  fuente: `fuente interna de ${id}`,
  resumen_teorico: `resumen de ${id}`,
  pasos_accionables: [`paso 1 de ${id}`, `paso 2 de ${id}`],
  entregable_esperado: `entregable de ${id}`,
  etiqueta_arbol: `Etiqueta de ${id}`,
  ...extra,
});

// "viejo" se fusiono dentro de "c": su texto vigente es el de "c" (la historia resuelve).
const GRAFO: Grafo = {
  a: nodo("a"),
  b: nodo("b"),
  c: nodo("c", { ids_alias: ["viejo"] }),
  d: nodo("d", { dominio: "quality" }),
};
const SEMILLAS = ["a", "b"];

const T = (min: number) => new Date(Date.UTC(2026, 9, 7, 10, min)).toISOString();

const recorrido = (extra: Record<string, unknown>) => ({
  recorrido: {
    ruta: [],
    modos: [],
    perfilSesion: "perfil",
    textoOriginal: "texto original",
    estadoVivoPrevio: null,
    ...extra,
  },
  acumulado: {},
});

function filas(): FilasJuez {
  return {
    proyectos: [
      {
        id: "P",
        entrada_original: "Hago pasteles por encargo en mi casa.",
        memoria: {
          version: 1,
          ficha: { papel: "dueno", tiene_jefe: false, equipo: { personas: 0, descripcion: "sola" }, sector: "reposteria", etapa: "validacion", prioridad_declarada: null, dijo_textual: [] },
          hilo: [
            { sesion: "s1", dominio: "core", nodo: "a", pregunta: "¿Cuánto vendes?", respuesta: "Unos 12 pasteles al mes.", en: T(5) },
            { sesion: "s3", dominio: "core", nodo: "b", pregunta: "¿Qué cambió?", respuesta: "Ya tengo tres clientes fijos.", en: T(25) },
          ],
        },
        numeros_proyecto: {
          precio_unitario: { valor: 45, unidad: "USD", texto_original: "a 45 dólares", session_id: "s1", updated_at: T(5) },
          costo_unitario: { valor: 20, unidad: "USD", texto_original: "me cuesta 20", session_id: "s3", updated_at: T(25) },
        },
      },
    ],
    sesiones: [
      { id: "s0", project_id: "P", dominio: "core", tipo: "gratuito", mensaje_entrada: "Hago pasteles por encargo en mi casa.", ruta: [], estado_recorrido: null, created_at: T(0) },
      {
        id: "s1", project_id: "P", dominio: "core", tipo: "inicial", mensaje_entrada: "Hago pasteles",
        ruta: [{ node_id: "a", tipo: "conversado" }, { node_id: "viejo", tipo: "silencioso" }],
        estado_recorrido: recorrido({
          perfilSesion: "Vende 12 pasteles al mes.",
          ficha: { papel: "dueno", tiene_jefe: false, equipo: { personas: 0, descripcion: "sola" }, sector: "reposteria", etapa: "validacion", prioridad_declarada: null, dijo_textual: [] },
        }),
        created_at: T(1),
      },
      {
        id: "s2", project_id: "P", dominio: "quality", tipo: "inicial", mensaje_entrada: "mundo calidad",
        ruta: [{ node_id: "d", tipo: "conversado" }],
        estado_recorrido: recorrido({ estadoVivoPrevio: "estado tras el primer plan", snapshotNucleo: "1. Habla con 5 clientes" }),
        created_at: T(12),
      },
      {
        id: "s3", project_id: "P", dominio: "core", tipo: "seguimiento", mensaje_entrada: "Quiero profundizar",
        ruta: [{ node_id: "b", tipo: "conversado" }],
        estado_recorrido: recorrido({ estadoVivoPrevio: "estado tras el mundo" }),
        created_at: T(20),
      },
      {
        id: "s4", project_id: "P", dominio: "core", tipo: "seguimiento", mensaje_entrada: "Quiero replantear mi camino.",
        ruta: [{ node_id: "b", tipo: "silencioso" }],
        estado_recorrido: recorrido({
          ciclo: {
            tipo: "replantear",
            historia: "Los clientes fijos piden tartas, no pasteles.",
            conserva: [{ id: "t1", texto: "Hablar con 5 clientes" }],
            suelta: [{ id: "t2", texto: "Abrir un local" }],
            caminos: [
              { id: "a", titulo: "Tartas por encargo", descripcion: "Cambiar a tartas", nodos: ["b"] },
              { id: "b", titulo: "Seguir con pasteles", descripcion: "Quedarse", nodos: ["a", "c"] },
            ],
            caminoElegido: "a",
          },
        }),
        created_at: T(30),
      },
      { id: "s5", project_id: "P", dominio: "core", tipo: "reporte", mensaje_entrada: "numeros", ruta: [], estado_recorrido: null, created_at: T(40) },
    ],
    planes: [
      { id: "p0", session_id: "s0", etiqueta: "organizador", dominio: "core", contenido_md: "# Tu Claridad\n\nHaces pasteles.", created_at: T(0) },
      { id: "p1", session_id: "s1", etiqueta: "inicial", dominio: "core", contenido_md: "# Plan\n\n## Etapa 1: Clientes\n- Habla con 5 clientes\n\n## Etapa 2: Costos\n- Anota lo que gastas", created_at: T(10) },
      { id: "p2", session_id: "s2", etiqueta: "inicial", dominio: "quality", contenido_md: "# Plan de calidad\n\n- Revisa cada pastel", created_at: T(15) },
      { id: "p3", session_id: "s3", etiqueta: "seguimiento", dominio: "core", contenido_md: "# Plan 2\n\n- Sube el precio", created_at: T(26) },
      { id: "p4", session_id: "s4", etiqueta: "replanteamiento", dominio: "core", contenido_md: "# Plan 3\n\n- Vende tartas", created_at: T(35) },
      { id: "p5", session_id: "s5", etiqueta: "reporte_numeros", dominio: "core", contenido_md: "# Tus numeros", created_at: T(41) },
    ],
    visitas: [
      { session_id: "s1", node_id: "a", tipo: "conversado" },
      { session_id: "s1", node_id: "viejo", tipo: "silencioso" },
      { session_id: "s1", node_id: "b", tipo: "cosechado" },
      { session_id: "s3", node_id: "c", tipo: "cosechado" },
    ],
    items: [
      { plan_id: "p1", etapa: 1, nodos_origen: ["a"] },
      { plan_id: "p1", etapa: 2, nodos_origen: ["viejo", "b"] },
      { plan_id: "p1", etapa: 2, nodos_origen: ["viejo", "b"] },
      { plan_id: "p4", etapa: 1, nodos_origen: null },
    ],
  };
}

describe("tipoDeSalida: lo que la persona lee como consejo", () => {
  it("organizador es Claridad; los ciclos del nucleo son plan del nucleo; los de un mundo, plan de mundo; el replanteamiento aparte; el reporte no se juzga", () => {
    expect(tipoDeSalida("organizador", "core")).toBe("claridad");
    expect(tipoDeSalida("inicial", "core")).toBe("plan_nucleo");
    expect(tipoDeSalida("completo", null)).toBe("plan_nucleo");
    expect(tipoDeSalida("seguimiento", "core")).toBe("plan_nucleo");
    expect(tipoDeSalida("inicial", "quality")).toBe("plan_mundo");
    expect(tipoDeSalida("seguimiento", "primer_equipo")).toBe("plan_mundo");
    expect(tipoDeSalida("replanteamiento", "core")).toBe("replanteamiento");
    expect(tipoDeSalida("replanteamiento", "quality")).toBe("replanteamiento");
    expect(tipoDeSalida("reporte_numeros", "core")).toBeNull();
  });
});

describe("armarSalidas: una salida por plan, con su material y el contexto de su momento", () => {
  const salidas = armarSalidas(filas(), GRAFO, SEMILLAS);
  const de = (planId: string) => salidas.find((s) => s.ref.plan_id === planId)!;

  it("cinco salidas (p0 a p4) en orden de creacion; el reporte de numeros (p5) queda fuera", () => {
    // 6 planes - 1 reporte_numeros = 5
    expect(salidas.map((s) => s.ref.plan_id)).toEqual(["p0", "p1", "p2", "p3", "p4"]);
    expect(salidas.map((s) => s.contenido.tipo_salida)).toEqual(["claridad", "plan_nucleo", "plan_mundo", "plan_nucleo", "replanteamiento"]);
    expect(de("p2").contenido.espacio).toBe("quality");
    expect(de("p1").ref).toMatchObject({ session_id: "s1", project_id: "P", etiqueta: "inicial", dominio: "core" });
  });

  it("filtra por lo que se pide juzgar sin perder el material de los demas (el plan anterior sigue saliendo)", () => {
    const solo = armarSalidas(filas(), GRAFO, SEMILLAS, (p) => p.id === "p3");
    expect(solo.map((s) => s.ref.plan_id)).toEqual(["p3"]);
    expect(solo[0].contenido.contexto.plan_anterior).toContain("Habla con 5 clientes");
  });

  it("la salida es el texto tal cual lo leyo la persona", () => {
    expect(de("p1").contenido.salida).toBe(filas().planes[1].contenido_md);
    expect(de("p1").contenido.calculadora).toBeNull();
  });

  it("la Claridad trae las semillas que se le ofrecieron, con su texto vigente", () => {
    expect(de("p0").contenido.nodos.map((n) => [n.node_id, n.papel])).toEqual([["a", "semilla"], ["b", "semilla"]]);
    expect(de("p0").contenido.nodos[0]).toMatchObject({
      etiqueta: "Etiqueta de a",
      resumen: "resumen de a",
      pasos: ["paso 1 de a", "paso 2 de a"],
      entregable: "entregable de a",
    });
  });

  it("el plan del nucleo trae la ruta (con su modo), la cosecha y las etapas de nodos_por_etapa, y un id fusionado se lee con el texto de quien lo representa hoy", () => {
    const nodos = de("p1").contenido.nodos;
    // ruta: a (conversado, etapa 1), viejo (silencioso, etapa 2, hoy es c); cosecha: b (etapa 2)
    expect(nodos.map((n) => [n.node_id, n.papel, n.modo ?? null, n.etapas ?? []])).toEqual([
      ["a", "ruta", "conversado", [1]],
      ["viejo", "ruta", "silencioso", [2]],
      ["b", "cosecha", null, [2]],
    ]);
    expect(nodos[1].vigente_como).toBe("c");
    expect(nodos[1].resumen).toBe("resumen de c");
    expect(nodos[0].vigente_como).toBeUndefined();
  });

  it("ningun nodo del paquete lleva material interno (fuente ni titulo del concepto)", () => {
    const texto = JSON.stringify(salidas.map((s) => s.contenido));
    expect(texto).not.toMatch(/fuente interna|titulo interno|"fuente"|titulo_concepto/);
  });

  it("el replanteamiento trae la ruta del camino elegido y los candidatos de los demas caminos, sin repetir", () => {
    // ruta: b (silencioso). Caminos: a -> [b], b -> [a, c]. Candidatos que no estan en la ruta: a, c.
    expect(de("p4").contenido.nodos.map((n) => [n.node_id, n.papel])).toEqual([["b", "ruta"], ["a", "candidato"], ["c", "candidato"]]);
    expect(de("p4").contenido.contexto.replanteamiento).toEqual({
      historia: "Los clientes fijos piden tartas, no pasteles.",
      se_conserva: ["Hablar con 5 clientes"],
      se_suelta: ["Abrir un local"],
      camino_elegido: { titulo: "Tartas por encargo", descripcion: "Cambiar a tartas" },
      otros_caminos: [{ titulo: "Seguir con pasteles", descripcion: "Quedarse" }],
    });
  });

  it("el plan anterior es el ultimo ciclo del MISMO espacio creado antes; la Claridad no cuenta como ciclo", () => {
    expect(de("p0").contenido.contexto.plan_anterior).toBeNull();
    expect(de("p1").contenido.contexto.plan_anterior).toBeNull();
    expect(de("p2").contenido.contexto.plan_anterior).toBeNull(); // calidad no tenia plan antes
    expect(de("p3").contenido.contexto.plan_anterior).toBe(filas().planes[1].contenido_md); // p1
    expect(de("p4").contenido.contexto.plan_anterior).toBe(filas().planes[3].contenido_md); // p3
  });

  it("lo que la persona conto llega solo hasta el momento de la salida (el hilo de projects.memoria cortado por fecha)", () => {
    // hilo: T5 (s1) y T25 (s3). p0 en T0: nada. p1 en T10: la de T5. p3 en T26: las dos.
    expect(de("p0").contenido.contexto.lo_que_conto).toEqual([]);
    expect(de("p1").contenido.contexto.lo_que_conto).toEqual([{ espacio: "core", pregunta: "¿Cuánto vendes?", respuesta: "Unos 12 pasteles al mes." }]);
    expect(de("p3").contenido.contexto.lo_que_conto).toHaveLength(2);
  });

  it("las cifras que dio la persona, tambien cortadas por fecha", () => {
    // precio_unitario (T5) antes de p1 (T10); costo_unitario (T25) despues de p1 y antes de p3 (T26)
    expect(Object.keys(de("p1").contenido.contexto.numeros_que_dio ?? {})).toEqual(["precio_unitario"]);
    expect(Object.keys(de("p3").contenido.contexto.numeros_que_dio ?? {}).sort()).toEqual(["costo_unitario", "precio_unitario"]);
    expect(de("p1").contenido.contexto.numeros_que_dio?.precio_unitario).toEqual({ valor: 45, unidad: "USD", texto_original: "a 45 dólares" });
  });

  it("la idea, el mensaje de entrada, el perfil, la ficha de la sesion y el estado vivo de su momento", () => {
    const c1 = de("p1").contenido.contexto;
    expect(c1.idea).toBe("Hago pasteles por encargo en mi casa.");
    expect(c1.perfil_sesion).toBe("Vende 12 pasteles al mes.");
    expect(c1.ficha).toMatchObject({ papel: "dueno", tiene_jefe: false });
    expect(c1.estado_vivo).toBeNull();
    const c2 = de("p2").contenido.contexto;
    expect(c2.estado_vivo).toBe("estado tras el primer plan");
    expect(c2.actividades_del_nucleo).toBe("1. Habla con 5 clientes");
    // la Claridad solo vio el texto de la idea: sin ficha
    expect(de("p0").contenido.contexto.ficha).toBeNull();
    expect(de("p0").contenido.contexto.mensaje_entrada).toBe("Hago pasteles por encargo en mi casa.");
  });
});

describe("cuantasTrampas: 1 por cada 5 salidas", () => {
  it("redondea hacia arriba: ninguna tanda queda con menos de 1 de cada 5", () => {
    // 0/5 = 0 -> 0; 1/5 = 0,2 -> 1; 5/5 = 1 -> 1; 6/5 = 1,2 -> 2; 16/5 = 3,2 -> 4 (14 planes + 2 organizadores)
    expect([0, 1, 5, 6, 16].map(cuantasTrampas)).toEqual([0, 1, 1, 2, 4]);
  });
});

/** Doce salidas sinteticas, con nodos que tienen etiqueta, para plantar 3 trampas (12/5 = 2,4 -> 3). */
function doce(): SalidaReal[] {
  return Array.from({ length: 12 }, (_, i) => ({
    ref: { plan_id: `plan${i}`, session_id: `ses${i}`, project_id: "P", etiqueta: "inicial", dominio: "core", tipo_salida: "plan_nucleo" as const, creado: T(i) },
    contenido: {
      tipo_salida: "plan_nucleo" as const,
      espacio: "core",
      salida: `# Plan ${i}\n\n## Etapa 1: Empieza\n- Habla con clientes del plan ${i}\n- Anota lo que gastas\n\nCierre del plan ${i}.`,
      nodos: [
        { node_id: `n${i}`, papel: "ruta" as const, modo: "conversado", etiqueta: `Observa a tus Clientes ${i}`, resumen: "r", pasos: [], entregable: null },
      ],
      contexto: {
        idea: "idea", mensaje_entrada: null, perfil_sesion: null, ficha: null, lo_que_conto: [], estado_vivo: null,
        actividades_del_nucleo: null, plan_anterior: null, replanteamiento: null, numeros_que_dio: null,
      },
      calculadora: null,
    },
  }));
}

describe("plantarTrampas: copias sin marca, deterministas con la semilla", () => {
  const reales = doce();
  const r = plantarTrampas(reales);

  it("12 reales + 3 trampas = 15 paquetes, con ids opacos f001..f015 y una clave por paquete", () => {
    // 12/5 = 2,4 -> 3 trampas; 12 + 3 = 15
    expect(r.paquetes).toHaveLength(15);
    expect(r.paquetes.map((p) => p.paquete)).toEqual(Array.from({ length: 15 }, (_, i) => `f${String(i + 1).padStart(3, "0")}`));
    expect(r.claves.map((c) => c.paquete)).toEqual(r.paquetes.map((p) => p.paquete));
    expect(r.claves.filter((c) => c.origen === "trampa")).toHaveLength(3);
  });

  it("la misma semilla da exactamente lo mismo; otra semilla, otro orden", () => {
    expect(plantarTrampas(doce())).toEqual(r);
    expect(SEMILLA_FIDELIDAD).toBeTypeOf("number");
    const otra = plantarTrampas(doce(), SEMILLA_FIDELIDAD + 1);
    expect(otra.claves.map((c) => (c.origen === "real" ? c.ref.plan_id : `T:${c.ref.plan_id}`))).not.toEqual(
      r.claves.map((c) => (c.origen === "real" ? c.ref.plan_id : `T:${c.ref.plan_id}`))
    );
  });

  it("con tres trampas sale una de cada tipo: contrario, invencion y procedencia", () => {
    const tipos = r.claves.flatMap((c) => (c.origen === "trampa" ? [c.trampa.tipo] : [])).sort();
    expect(tipos).toEqual(["contrario", "invencion", "procedencia"]);
  });

  it("cada trampa es la copia de una salida real con UNA frase plantada: quitandola vuelve el original", () => {
    const porId = new Map(r.paquetes.map((p) => [p.paquete, p]));
    for (const c of r.claves.filter((x): x is Extract<ClavePaquete, { origen: "trampa" }> => x.origen === "trampa")) {
      const trampa = porId.get(c.paquete)!;
      const original = porId.get(c.copia_de)!;
      expect(r.claves.find((x) => x.paquete === c.copia_de)?.origen).toBe("real");
      expect(trampa.salida.split(c.trampa.frase)).toHaveLength(2); // aparece una sola vez
      expect(trampa.salida.replace(` ${c.trampa.frase}`, "")).toBe(original.salida);
      expect(original.salida).not.toContain(c.trampa.frase);
      // el resto del paquete es identico al original
      expect({ ...trampa, paquete: "", salida: "" }).toEqual({ ...original, paquete: "", salida: "" });
      expect(c.ref).toEqual(r.claves.find((x) => x.paquete === c.copia_de)!.ref);
    }
  });

  it("la frase sale del catalogo escrito antes de leer; el contrario niega un nodo del paquete por su etiqueta", () => {
    const porId = new Map(r.paquetes.map((p) => [p.paquete, p]));
    for (const c of r.claves) {
      if (c.origen !== "trampa") continue;
      if (c.trampa.tipo === "invencion") expect(FRASES_INVENCION).toContain(c.trampa.frase);
      if (c.trampa.tipo === "procedencia") expect(FRASES_PROCEDENCIA).toContain(c.trampa.frase);
      if (c.trampa.tipo === "contrario") {
        const nodos = porId.get(c.paquete)!.nodos;
        const n = nodos.find((x) => x.node_id === c.trampa.nodo)!;
        expect(n).toBeDefined();
        expect(c.trampa.frase).toContain(n.etiqueta!);
      } else {
        expect(c.trampa.nodo).toBeNull();
      }
    }
  });

  it("nada en los paquetes delata la clave: ni origen, ni tipo de trampa, ni frase, ni de que plan o sesion es", () => {
    const texto = JSON.stringify(r.paquetes);
    expect(texto).not.toMatch(/trampa|origen|copia_de|"frase"|"ref"|plan_id|session_id/);
    for (const ref of reales.map((s) => s.ref)) {
      expect(texto).not.toContain(ref.plan_id);
      expect(texto).not.toContain(ref.session_id);
    }
    // todos los paquetes tienen la misma forma
    const forma = (p: object) => Object.keys(p).sort().join(",");
    expect(new Set(r.paquetes.map(forma)).size).toBe(1);
    expect(forma(r.paquetes[0])).toBe("calculadora,contexto,espacio,nodos,paquete,salida,tipo_salida");
  });

  it("sin nodos con etiqueta, un contrario no se puede plantar y se planta una invencion", () => {
    const sinNodos = doce().slice(0, 5).map((s) => ({ ...s, contenido: { ...s.contenido, nodos: [] } }));
    // 5/5 = 1 trampa; la primera del ciclo seria contrario, pero no hay nodo que contradecir
    const t = plantarTrampas(sinNodos).claves.filter((c) => c.origen === "trampa");
    expect(t).toHaveLength(1);
    expect(t[0].origen === "trampa" && t[0].trampa.tipo).toBe("invencion");
  });

  it("sin salidas no hay paquetes ni trampas", () => {
    expect(plantarTrampas([])).toEqual({ paquetes: [], claves: [] });
  });
});
