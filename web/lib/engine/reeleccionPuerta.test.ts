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

const SEMILLA_RECHAZADA = "medicion_calidad";

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
    expect(rama.size).toBeLessThanOrEqual(50);
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
