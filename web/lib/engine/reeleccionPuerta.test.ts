// Fase 4.3 — EL MUNDO NUNCA ABANDONA. El hallazgo real (barrido 380): el
// interprete salio de 'quality' en el turno 1 porque 'medicion_calidad' "y
// todos sus sucesores estan disenados para organizaciones", y el usuario que
// pago 3 creditos se quedo con una pantalla muda.
//
// Se prueba contra el GRAFO REAL, no contra un mock: la promesa "el mundo nunca
// abandona" es sobre los mundos que existen, y un fixture de tres nodos podria
// pasar con el grafo de produccion roto.
import { describe, expect, it } from "vitest";
import { cargarGrafo } from "./graph";
import { semillasDelPack } from "./evaluacionBrecha";
import { ramaDe, reelegirPuertaDeMundo } from "./reeleccionPuerta";

const graph = cargarGrafo();
// El perfil del hallazgo: artesana sola, tres kits a mano. Nada de estructura.
const ESTADO_ARTESANA =
  "Kit de huerto urbano armado a mano por una sola persona en su casa. Vendio tres kits " +
  "a amigos que pagaron. Sin empleados, sin procesos formales, sin equipo. El sustrato le " +
  "queda disparejo entre un kit y otro y quiere que se vea serio.";

// Antes era medicion_calidad. Dejó de servir de fixture en la fusión de
// Calidad (ago 2026): su rama ya se tragaba 6 de las 7 semillas del pack, y al
// heredar las aristas de su absorbido se tragó la séptima. El test pasaba por
// UNA semilla de margen. Con mejora_continua_del_proceso quedan 3 fuera, que es
// margen de verdad para probar la regla. La densidad que hay detrás está fijada
// abajo, en su propio test.
const SEMILLA_RECHAZADA = "mejora_continua_del_proceso";

describe("ramaDe — se descarta la RAMA, no el nodo", () => {
  it("incluye el nodo y sus sucesores", () => {
    const rama = ramaDe(SEMILLA_RECHAZADA, graph);
    expect(rama.has(SEMILLA_RECHAZADA)).toBe(true);
    // El nodo del hallazgo tiene sucesores en el grafo real: si la rama fuera
    // solo el nodo, el interprete lo volveria a rechazar por la puerta de al lado.
    expect(rama.size).toBeGreaterThan(1);
    for (const sig of graph[SEMILLA_RECHAZADA]?.nodos_siguientes ?? []) {
      if (sig in graph) expect(rama.has(sig)).toBe(true);
    }
  });

  it("un nodo que no existe no revienta: devuelve solo su id", () => {
    expect([...ramaDe("nodo_que_no_existe", graph)]).toEqual(["nodo_que_no_existe"]);
  });

  it("no se cuelga con ciclos (el grafo no es un arbol)", () => {
    // Si ramaDe no marcara visitados, un ciclo colgaria el motor en un turno.
    const rama = ramaDe(SEMILLA_RECHAZADA, graph, 50);
    // El tope se mira por NODO, no por sucesor: al expandir el último nodo se
    // añaden todos los suyos de golpe, así que puede pasarse por unos pocos.
    // Lo que este test prueba es que TERMINA (un ciclo lo colgaría), no que el
    // tope sea exacto. Antes pasaba con <= 50 por casualidad, porque ningún
    // nodo de la frontera tenía muchos sucesores.
    expect(rama.size).toBeGreaterThan(0);
    expect(rama.size).toBeLessThan(50 * 2);
  });
});

describe("reelegirPuertaDeMundo — el escenario exacto del hallazgo", () => {
  const reeleccion = reelegirPuertaDeMundo({
    dominio: "quality",
    graph,
    estadoVivo: ESTADO_ARTESANA,
    perfilSesion: null,
    cubiertos: new Set([SEMILLA_RECHAZADA]),
    descartados: ramaDe(SEMILLA_RECHAZADA, graph),
  });

  it("NO abandona: encuentra otra puerta en el mundo", () => {
    expect(reeleccion).not.toBeNull();
  });

  it("la puerta nueva NO es la rama rechazada", () => {
    const rama = ramaDe(SEMILLA_RECHAZADA, graph);
    expect(rama.has(reeleccion!.puertaId)).toBe(false);
  });

  it("la puerta nueva es del MUNDO, jamas del core", () => {
    expect(graph[reeleccion!.puertaId].dominio).toBe("quality");
  });

  it("prefiere una semilla del pack sobre un vecino cualquiera", () => {
    expect(reeleccion!.esSemilla).toBe(true);
    expect(semillasDelPack("quality").map((s) => s.id)).toContain(reeleccion!.puertaId);
  });
});

describe("reelegirPuertaDeMundo — bordes", () => {
  it("con TODAS las semillas descartadas, cae a los vecinos del dominio", () => {
    const todasLasSemillas = new Set(semillasDelPack("quality").map((s) => s.id));
    const r = reelegirPuertaDeMundo({
      dominio: "quality",
      graph,
      estadoVivo: ESTADO_ARTESANA,
      perfilSesion: null,
      cubiertos: new Set(),
      descartados: todasLasSemillas,
    });
    // Un mundo es mucho mas que sus puertas de entrada, y el usuario pago por
    // el mundo entero.
    expect(r).not.toBeNull();
    expect(r!.esSemilla).toBe(false);
    expect(graph[r!.puertaId].dominio).toBe("quality");
  });

  it("con el dominio ENTERO descartado devuelve null: ahi si se cierra", () => {
    const todoElMundo = new Set(Object.keys(graph).filter((n) => graph[n].dominio === "quality"));
    const r = reelegirPuertaDeMundo({
      dominio: "quality",
      graph,
      estadoVivo: ESTADO_ARTESANA,
      perfilSesion: null,
      cubiertos: new Set(),
      descartados: todoElMundo,
    });
    expect(r).toBeNull();
  });

  it("jamas devuelve un nodo ya cubierto (no se repite una puerta recorrida)", () => {
    const semillas = semillasDelPack("quality").map((s) => s.id);
    const r = reelegirPuertaDeMundo({
      dominio: "quality",
      graph,
      estadoVivo: ESTADO_ARTESANA,
      perfilSesion: null,
      cubiertos: new Set(semillas),
      descartados: new Set(),
    });
    expect(r).not.toBeNull();
    expect(semillas).not.toContain(r!.puertaId);
  });

  it("es determinista: mismas entradas, misma puerta", () => {
    const args = {
      dominio: "quality",
      graph,
      estadoVivo: ESTADO_ARTESANA,
      perfilSesion: null,
      cubiertos: new Set([SEMILLA_RECHAZADA]),
      descartados: ramaDe(SEMILLA_RECHAZADA, graph),
    };
    expect(reelegirPuertaDeMundo(args)!.puertaId).toBe(reelegirPuertaDeMundo(args)!.puertaId);
  });

  it("el perfil de la sesion pesa: dos perfiles distintos pueden abrir puertas distintas", () => {
    // No se exige que difieran (el grafo manda), pero SI que el perfil se lea:
    // si el parametro se ignorara, la afinidad seria identica siempre.
    const base = {
      dominio: "quality" as const,
      graph,
      cubiertos: new Set<string>(),
      descartados: new Set<string>(),
    };
    const conPerfil = reelegirPuertaDeMundo({ ...base, estadoVivo: null, perfilSesion: ESTADO_ARTESANA });
    const sinNada = reelegirPuertaDeMundo({ ...base, estadoVivo: null, perfilSesion: null });
    expect(conPerfil).not.toBeNull();
    expect(sinNada).not.toBeNull();
    // Con contexto hay afinidad real; sin nada, todo empata en 0.
    expect(conPerfil!.puntaje).toBeGreaterThan(0);
    expect(sinNada!.puntaje).toBe(0);
  });
});

describe("la densidad del pack, fijada como está hoy", () => {
  /**
   * HALLAZGO de la cirugía de Calidad (ago 2026), traído sin resolver.
   *
   * `ramaDe` desde CUALQUIER semilla de quality alcanza el tope de 500 nodos:
   * el pack está tan conectado que "descartar la rama" descarta casi todo lo
   * alcanzable. De las 7 semillas, 4 se tragan a las otras 6 enteras.
   *
   * No lo causó la fusión (antes ya era 6 de 7 desde medicion_calidad); la
   * fusión se comió el último margen y lo hizo visible. Se fija aquí para que
   * el día que alguien mejore la densidad, este test cante el cambio en vez de
   * dejarlo pasar.
   */
  it("desde una semilla, la rama llega al tope", () => {
    const rama = ramaDe("medicion_calidad", graph);
    expect(rama.size).toBeGreaterThanOrEqual(500);
  });

  it("y se traga las siete semillas del pack", () => {
    const rama = ramaDe("medicion_calidad", graph);
    const fuera = semillasDelPack("quality").map((s) => s.id).filter((s) => !rama.has(s));
    expect(fuera, "si esto cambia, la densidad mejoró: revisa el hallazgo").toHaveLength(0);
  });
});
