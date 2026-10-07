/**
 * JUEZ DE FIDELIDAD DE LA SALIDA (corrida final, paso D; docs/producto/CORRIDA_FINAL.md y
 * docs/producto/JUEZ_FIDELIDAD.md): la parte pura del extractor (web/scripts/juezFidelidad.ts). Aqui no hay red ni
 * base: de las filas ya leidas a los paquetes que leen los jueces ciegos (agentes de Claude Code, no la API).
 *
 * Un paquete es UNA salida que la persona leyo como consejo (plan del nucleo, Claridad, plan de mundo o
 * replanteamiento) con su material: los nodos que se usaron, con su texto vigente del dataset, y el contexto de la
 * persona EN EL MOMENTO de esa salida (lo que conto hasta entonces, su ficha, el estado vivo y el plan anterior).
 *
 * Trampas sin marca: 1 por cada 5 salidas, copias de una salida real con UNA afirmacion plantada (un contrario a un
 * nodo del paquete, una cifra o norma inventada, o una atribucion de procedencia). Las frases se escribieron aqui
 * ANTES de leer ninguna salida. La clave (que paquete es trampa, de que tipo y con que frase) va SOLO al fichero de
 * claves: los paquetes reales y las trampas tienen la misma forma y un id opaco.
 */
import type { RutaNodo, TurnoRegistrado } from "../db";
import { ETIQUETAS_CICLO } from "../dbContract";
import { resolverId, type Grafo } from "../engine/graph";
import { memoriaDe, type FichaContexto } from "../engine/memoria";
import type { EstadoRecorrido } from "../engine/recorrido";
import { prng } from "./nucleo";

/** Semilla del plantado y del orden de los paquetes, escrita antes de la corrida (7 oct 2026). */
export const SEMILLA_FIDELIDAD = 20261007;

export type TipoSalida = "plan_nucleo" | "claridad" | "plan_mundo" | "replanteamiento";
export type TipoTrampaFidelidad = "contrario" | "invencion" | "procedencia";

/** Lo que la persona lee como consejo. El reporte de numeros no se juzga aqui (sus cifras son de la calculadora). */
export function tipoDeSalida(etiqueta: string, dominio: string | null | undefined): TipoSalida | null {
  if (etiqueta === "organizador") return "claridad";
  if (etiqueta === "replanteamiento") return "replanteamiento";
  if (!ETIQUETAS_CICLO.includes(etiqueta)) return null;
  return (dominio ?? "core") === "core" ? "plan_nucleo" : "plan_mundo";
}

// ---------------------------------------------------------------- filas de la base

export interface FilaPlanJuez {
  id: string;
  session_id: string;
  etiqueta: string;
  dominio: string | null;
  contenido_md: string;
  created_at: string;
}

export interface FilaSesionJuez {
  id: string;
  project_id: string;
  dominio?: string | null;
  tipo: string;
  mensaje_entrada: string | null;
  ruta: RutaNodo[] | null;
  /** sessions.estado_recorrido (jsonb): se lee con cuidado, puede venir de cualquier era. */
  estado_recorrido: unknown;
  created_at: string;
}

export interface FilaProyectoJuez {
  id: string;
  entrada_original: string | null;
  /** projects.memoria (migracion 049): ficha e hilo, ver lib/engine/memoria.ts. */
  memoria?: unknown;
  /** projects.numeros_proyecto: las cifras que dio la persona, con su fecha. */
  numeros_proyecto?: unknown;
}

/** node_visits (migracion 037): una fila por visita; la cosecha es la de tipo 'cosechado'. */
export interface FilaVisitaJuez {
  session_id: string;
  node_id: string;
  tipo: string;
}

/** checklist_items: nodos_origen es el nodos_por_etapa del redactor, persistido item a item. */
export interface FilaItemJuez {
  plan_id: string;
  etapa: number;
  nodos_origen: string[] | null;
}

export interface FilasJuez {
  planes: FilaPlanJuez[];
  sesiones: FilaSesionJuez[];
  proyectos: FilaProyectoJuez[];
  visitas: FilaVisitaJuez[];
  items: FilaItemJuez[];
}

// ---------------------------------------------------------------- el paquete

/** semilla: lo que se le ofrecio a la Claridad; candidato: los conceptos de los caminos de un replanteamiento;
 * etapa: un nodo que el redactor declaro en una etapa y no esta en la ruta ni en la cosecha. */
export type PapelNodo = "ruta" | "cosecha" | "etapa" | "semilla" | "candidato";

export interface NodoPaquete {
  node_id: string;
  /** si el id es de otra era (fusionado), el nodo que hoy lo representa y cuyo texto se da */
  vigente_como?: string;
  papel: PapelNodo;
  /** el modo en la ruta: conversado, silencioso o salto */
  modo?: string;
  /** las etapas del plan que el redactor declaro hechas con este nodo */
  etapas?: number[];
  etiqueta: string | null;
  resumen: string | null;
  pasos: string[];
  entregable: string | null;
}

export interface ContextoPaquete {
  idea: string | null;
  mensaje_entrada: string | null;
  perfil_sesion: string | null;
  ficha: FichaContexto | null;
  lo_que_conto: Array<{ espacio: string; pregunta: string | null; respuesta: string }>;
  estado_vivo: string | null;
  /** en un mundo de proteccion: el retrato de las actividades del nucleo que recibio */
  actividades_del_nucleo: string | null;
  plan_anterior: string | null;
  replanteamiento: {
    historia: string;
    se_conserva: string[];
    se_suelta: string[];
    camino_elegido: { titulo: string; descripcion: string } | null;
    otros_caminos: Array<{ titulo: string; descripcion: string }>;
  } | null;
  numeros_que_dio: Record<string, { valor: unknown; unidad: string | null; texto_original: string | null }> | null;
}

/** La forma que pide docs/producto/JUEZ_FIDELIDAD.md. Sin nada que diga de que plan o sesion es. */
export interface PaqueteFidelidad {
  paquete: string;
  tipo_salida: TipoSalida;
  espacio: string;
  salida: string;
  nodos: NodoPaquete[];
  contexto: ContextoPaquete;
  /** el redactor de estas salidas no corre la calculadora: las cifras de la persona van en contexto.numeros_que_dio */
  calculadora: Record<string, unknown> | null;
}

/** De donde sale cada salida: va a la clave, nunca al paquete. */
export interface RefSalida {
  plan_id: string;
  session_id: string;
  project_id: string;
  etiqueta: string;
  dominio: string;
  tipo_salida: TipoSalida;
  creado: string;
}

export interface SalidaReal {
  ref: RefSalida;
  contenido: Omit<PaqueteFidelidad, "paquete">;
}

export type ClavePaquete =
  | { paquete: string; origen: "real"; ref: RefSalida }
  | {
      paquete: string;
      origen: "trampa";
      /** el paquete real del que es copia */
      copia_de: string;
      ref: RefSalida;
      trampa: { tipo: TipoTrampaFidelidad; frase: string; nodo: string | null };
    };

// ---------------------------------------------------------------- armar las salidas

function textoVigente(nid: string, grafo: Grafo): Pick<NodoPaquete, "vigente_como" | "etiqueta" | "resumen" | "pasos" | "entregable"> {
  const real = resolverId(nid, grafo) ?? nid;
  const n = grafo[real];
  return {
    ...(real !== nid ? { vigente_como: real } : {}),
    etiqueta: n?.etiqueta_arbol ?? null,
    resumen: n?.resumen_teorico ?? null,
    pasos: n?.pasos_accionables ?? [],
    entregable: n?.entregable_esperado ?? null,
  };
}

const antesO = (en: unknown, limite: number): boolean => {
  const t = typeof en === "string" ? Date.parse(en) : NaN;
  return Number.isNaN(t) || t <= limite;
};

type EstadoLeido = { recorrido?: Partial<EstadoRecorrido> | null; turnos?: TurnoRegistrado[] } | null;

function numerosQueDio(proyecto: FilaProyectoJuez | undefined, recorrido: Partial<EstadoRecorrido> | null, limite: number): ContextoPaquete["numeros_que_dio"] {
  const out: NonNullable<ContextoPaquete["numeros_que_dio"]> = {};
  const fuentes = [proyecto?.numeros_proyecto, recorrido?.numerosDetectadosSesion];
  for (const f of fuentes) {
    if (!f || typeof f !== "object") continue;
    for (const [campo, v] of Object.entries(f as Record<string, unknown>)) {
      if (!v || typeof v !== "object") continue;
      const e = v as { valor?: unknown; unidad?: unknown; texto_original?: unknown; updated_at?: unknown };
      if (e.valor === null || e.valor === undefined || !antesO(e.updated_at, limite)) continue;
      out[campo] = {
        valor: e.valor,
        unidad: typeof e.unidad === "string" ? e.unidad : null,
        texto_original: typeof e.texto_original === "string" ? e.texto_original : null,
      };
    }
  }
  return Object.keys(out).length ? out : null;
}

/**
 * Una salida por plan juzgable, en orden de creacion. `filas` trae TODOS los planes y sesiones de los proyectos (el
 * plan anterior puede ser de antes de la ventana); `juzgar` dice cuales se juzgan.
 */
export function armarSalidas(
  filas: FilasJuez,
  grafo: Grafo,
  semillas: string[],
  juzgar: (p: FilaPlanJuez) => boolean = () => true
): SalidaReal[] {
  const sesiones = new Map(filas.sesiones.map((s) => [s.id, s]));
  const proyectos = new Map(filas.proyectos.map((p) => [p.id, p]));
  const orden = (a: { created_at: string; id: string }, b: { created_at: string; id: string }) =>
    Date.parse(a.created_at) - Date.parse(b.created_at) || a.id.localeCompare(b.id);
  const planes = [...filas.planes].sort(orden);
  const proyectoDe = (p: FilaPlanJuez): string => {
    const s = sesiones.get(p.session_id);
    if (!s) throw new Error(`el plan ${p.id} apunta a la sesion ${p.session_id}, que no se leyo`);
    return s.project_id;
  };

  const salidas: SalidaReal[] = [];
  for (const plan of planes) {
    const tipo = tipoDeSalida(plan.etiqueta, plan.dominio);
    if (!tipo || !juzgar(plan)) continue;
    const sesion = sesiones.get(plan.session_id);
    if (!sesion) throw new Error(`el plan ${plan.id} apunta a la sesion ${plan.session_id}, que no se leyo`);
    const dominio = plan.dominio ?? sesion.dominio ?? "core";
    const proyecto = proyectos.get(sesion.project_id);
    const limite = Date.parse(plan.created_at);
    const estado = (sesion.estado_recorrido && typeof sesion.estado_recorrido === "object" ? sesion.estado_recorrido : null) as EstadoLeido;
    const recorrido = estado?.recorrido ?? null;

    // ---- los nodos
    const nodos: NodoPaquete[] = [];
    const vistos = new Set<string>();
    const agregar = (nid: string, papel: PapelNodo, modo?: string) => {
      if (vistos.has(nid)) return;
      vistos.add(nid);
      nodos.push({ node_id: nid, papel, ...(modo ? { modo } : {}), ...textoVigente(nid, grafo) });
    };
    if (tipo === "claridad") {
      for (const nid of semillas) agregar(nid, "semilla");
    } else {
      const ruta: RutaNodo[] = sesion.ruta?.length
        ? sesion.ruta
        : (recorrido?.ruta ?? []).map((nid, i) => ({ node_id: nid, tipo: (recorrido?.modos?.[i] ?? "conversado") as RutaNodo["tipo"] }));
      for (const r of ruta) agregar(r.node_id, "ruta", r.tipo);
      for (const v of filas.visitas) if (v.session_id === sesion.id && v.tipo === "cosechado") agregar(v.node_id, "cosecha");
      const etapas = new Map<string, Set<number>>();
      for (const it of filas.items) {
        if (it.plan_id !== plan.id) continue;
        for (const nid of it.nodos_origen ?? []) {
          if (!etapas.has(nid)) etapas.set(nid, new Set());
          etapas.get(nid)!.add(it.etapa);
        }
      }
      for (const nid of etapas.keys()) agregar(nid, "etapa");
      for (const n of nodos) {
        const e = etapas.get(n.node_id);
        if (e?.size) n.etapas = [...e].sort((a, b) => a - b);
      }
    }
    const ciclo = recorrido?.ciclo;
    let replanteamiento: ContextoPaquete["replanteamiento"] = null;
    if (ciclo?.tipo === "replantear") {
      for (const c of ciclo.caminos ?? []) for (const nid of c.nodos ?? []) agregar(nid, "candidato");
      const elegido = (ciclo.caminos ?? []).find((c) => c.id === ciclo.caminoElegido) ?? null;
      replanteamiento = {
        historia: ciclo.historia,
        se_conserva: (ciclo.conserva ?? []).map((t) => t.texto),
        se_suelta: (ciclo.suelta ?? []).map((t) => t.texto),
        camino_elegido: elegido ? { titulo: elegido.titulo, descripcion: elegido.descripcion } : null,
        otros_caminos: (ciclo.caminos ?? []).filter((c) => c !== elegido).map((c) => ({ titulo: c.titulo, descripcion: c.descripcion })),
      };
    }

    // ---- el contexto de su momento
    const memoria = memoriaDe(proyecto?.memoria);
    let loQueConto: ContextoPaquete["lo_que_conto"] = memoria.hilo
      .filter((e) => antesO(e.en, limite))
      .map((e) => ({ espacio: e.dominio, pregunta: e.pregunta ?? null, respuesta: e.respuesta }));
    if (memoria.hilo.length === 0) {
      // proyecto de antes de la memoria (049): lo conversado en esta sesion
      loQueConto = (estado?.turnos ?? []).map((t) => ({ espacio: dominio, pregunta: t.pregunta, respuesta: t.respuesta }));
    }
    const previo = planes
      .filter(
        (p) =>
          p.id !== plan.id &&
          ETIQUETAS_CICLO.includes(p.etiqueta) &&
          (p.dominio ?? "core") === dominio &&
          Date.parse(p.created_at) < limite &&
          proyectoDe(p) === sesion.project_id
      )
      .pop();

    salidas.push({
      ref: {
        plan_id: plan.id,
        session_id: sesion.id,
        project_id: sesion.project_id,
        etiqueta: plan.etiqueta,
        dominio,
        tipo_salida: tipo,
        creado: plan.created_at,
      },
      contenido: {
        tipo_salida: tipo,
        espacio: dominio,
        salida: plan.contenido_md,
        nodos,
        contexto: {
          idea: proyecto?.entrada_original ?? null,
          mensaje_entrada: sesion.mensaje_entrada ?? null,
          perfil_sesion: recorrido?.perfilSesion ?? null,
          // la Claridad solo vio el texto de la idea; lo demas, la ficha de su sesion o la guardada
          ficha: recorrido?.ficha ?? (tipo === "claridad" ? null : memoria.ficha),
          lo_que_conto: loQueConto,
          estado_vivo: recorrido?.estadoVivoPrevio ?? null,
          actividades_del_nucleo: recorrido?.snapshotNucleo ?? null,
          plan_anterior: previo?.contenido_md ?? null,
          replanteamiento,
          numeros_que_dio: numerosQueDio(proyecto, recorrido, limite),
        },
        calculadora: null,
      },
    });
  }
  return salidas;
}

// ---------------------------------------------------------------- las trampas

export function cuantasTrampas(salidas: number): number {
  return Math.ceil(salidas / 5);
}

/** Cifras, normas, plazos y resultados prometidos que ningun nodo dice: escritas antes de leer ninguna salida. */
export const FRASES_INVENCION: readonly string[] = [
  "La ley te obliga a registrar este proceso ante la autoridad en un plazo de 30 días.",
  "Haciéndolo así, tus ventas suben un 35 % en los primeros tres meses.",
  "La norma ISO 4417 exige guardar estos registros durante al menos siete años.",
];

/** Atribuciones a un autor, a un libro o a estudios y especialistas: escritas antes de leer ninguna salida. */
export const FRASES_PROCEDENCIA: readonly string[] = [
  "Así lo explica un autor clásico de la gestión en su libro más conocido: empieza por lo pequeño.",
  "Lo respaldan décadas de estudios sobre pequeños negocios: quien anota cada venta decide mejor.",
  "Es lo que recomiendan los especialistas en emprendimiento: primero vender, después crecer.",
];

/** Lo contrario de un nodo del paquete, nombrado por su etiqueta: lo que el nodo pide hacer, dicho como prescindible. */
export function fraseContrario(etiqueta: string): string {
  return `Este paso puedes saltártelo: «${etiqueta}» no hace falta en tu caso.`;
}

const TIPOS_TRAMPA: readonly TipoTrampaFidelidad[] = ["contrario", "invencion", "procedencia"];

/** La linea donde se planta: una de texto corrido o de lista, mejor si cierra una frase. -1 si no hay ninguna. */
function lineaDonde(lineas: string[], azar: () => number): number {
  const texto = lineas
    .map((l, i) => [l.trim(), i] as const)
    .filter(([l]) => l && !/^(#|\||>|```|---)/.test(l));
  const conPunto = texto.filter(([l]) => /[.!?]$/.test(l));
  const elegibles = conPunto.length ? conPunto : texto;
  if (!elegibles.length) return -1;
  return elegibles[Math.floor(azar() * elegibles.length)][1];
}

/**
 * Los paquetes de la tanda: las salidas reales y sus trampas, barajadas con la semilla, con ids opacos (f001...).
 * Las trampas copian salidas reales distintas; sus tipos rotan contrario, invencion, procedencia (un contrario sin
 * nodo con etiqueta que contradecir pasa a invencion).
 */
export function plantarTrampas(salidas: SalidaReal[], semilla = SEMILLA_FIDELIDAD): { paquetes: PaqueteFidelidad[]; claves: ClavePaquete[] } {
  const azar = prng(semilla);
  const barajar = <T>(xs: T[]): T[] => {
    for (let i = xs.length - 1; i > 0; i--) {
      const j = Math.floor(azar() * (i + 1));
      [xs[i], xs[j]] = [xs[j], xs[i]];
    }
    return xs;
  };

  type Pendiente = { contenido: SalidaReal["contenido"]; ref: RefSalida; real: number; trampa?: { tipo: TipoTrampaFidelidad; frase: string; nodo: string | null } };
  const todos: Pendiente[] = salidas.map((s, i) => ({ contenido: structuredClone(s.contenido), ref: s.ref, real: i }));

  const copiadas = barajar(salidas.map((_, i) => i)).slice(0, cuantasTrampas(salidas.length));
  copiadas.forEach((idx, k) => {
    const original = salidas[idx];
    const contenido = structuredClone(original.contenido);
    let tipo = TIPOS_TRAMPA[k % TIPOS_TRAMPA.length];
    let frase: string;
    let nodo: string | null = null;
    const contradecibles = contenido.nodos.filter((n) => n.etiqueta);
    const preferidos = contradecibles.filter((n) => n.papel === "ruta" || n.papel === "semilla");
    if (tipo === "contrario" && !contradecibles.length) tipo = "invencion";
    if (tipo === "contrario") {
      const lista = preferidos.length ? preferidos : contradecibles;
      const n = lista[Math.floor(azar() * lista.length)];
      nodo = n.node_id;
      frase = fraseContrario(n.etiqueta!);
    } else {
      const catalogo = tipo === "invencion" ? FRASES_INVENCION : FRASES_PROCEDENCIA;
      frase = catalogo[Math.floor(azar() * catalogo.length)];
    }
    const lineas = contenido.salida.split("\n");
    const donde = lineaDonde(lineas, azar);
    if (donde >= 0) lineas[donde] = `${lineas[donde]} ${frase}`;
    else lineas[lineas.length - 1] = `${lineas[lineas.length - 1]} ${frase}`;
    contenido.salida = lineas.join("\n");
    todos.push({ contenido, ref: original.ref, real: idx, trampa: { tipo, frase, nodo } });
  });

  barajar(todos);
  const ancho = Math.max(3, String(todos.length).length);
  const idDe = (i: number) => `f${String(i + 1).padStart(ancho, "0")}`;
  const idDelReal = new Map<number, string>();
  todos.forEach((t, i) => {
    if (!t.trampa) idDelReal.set(t.real, idDe(i));
  });
  const paquetes: PaqueteFidelidad[] = todos.map((t, i) => ({ paquete: idDe(i), ...t.contenido }));
  const claves: ClavePaquete[] = todos.map((t, i) =>
    t.trampa
      ? { paquete: idDe(i), origen: "trampa", copia_de: idDelReal.get(t.real)!, ref: t.ref, trampa: t.trampa }
      : { paquete: idDe(i), origen: "real", ref: t.ref }
  );
  return { paquetes, claves };
}
