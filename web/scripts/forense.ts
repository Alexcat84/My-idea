// Fase 3.9 (E): FORENSE DE SESION -- herramienta de operador (la beta la
// necesitara muchas veces). Recibe un session_id o un project_id (o busca el
// proyecto por texto de su entrada) y vuelca a examples/forense/<id>.md TODO
// lo que la caja de vidrio ya persiste: el recorrido en orden con el tipo de
// cada nodo, la decision de cada turno (accion, salto, razonamiento, score de
// la brujula, prioridad declarada), los saltos con sus candidatos perdedores,
// la procedencia del plan (recorrido vs vecindario, con nombres), el veredicto
// del juez, los eventos del guardian, y los costos reales por componente.
// Lee Supabase directo con service-role (como salud.ts), no simula un usuario.
//
// Uso:
//   pnpm tsx scripts/forense.ts <session_id | project_id>
//   pnpm tsx scripts/forense.ts --buscar "auditor HSEQ"
import { createClient, type SupabaseClient } from "@supabase/supabase-js";
import { mkdirSync, writeFileSync } from "node:fs";
import path from "node:path";
import { cargarEnvRaiz, ROOT } from "./_shared/http";
import { cargarGrafo, etiquetaArbol, type Grafo } from "../lib/engine/graph";
import { cargarFamilies } from "../lib/readiness";

cargarEnvRaiz();

interface FilaSesion {
  id: string;
  project_id: string;
  tipo: string;
  dominio: string | null;
  created_at: string;
  closed_at: string | null;
  estado_recorrido: {
    recorrido?: { ruta?: string[]; modos?: string[]; prioridadDeclarada?: unknown; perfilSesion?: string };
  } | null;
  decisiones: Array<Record<string, unknown>> | null;
  calidad: Record<string, unknown> | null;
  costo_usd: number | null;
  costo_desglose: Record<string, number> | null;
  presupuesto_excedido: boolean | null;
}
interface FilaPlan {
  session_id: string;
  etiqueta: string;
  contenido_md: string;
  created_at: string;
  dominio: string | null;
}
interface FilaNodo {
  session_id: string | null;
  node_id: string;
  tipo: string;
}
interface FilaProyecto {
  id: string;
  titulo: string | null;
  entrada_original: string | null;
  fase_actual: string | null;
}

const TIPO_LEGIBLE: Record<string, string> = {
  conversado: "conversado",
  silencioso: "cubierto en silencio",
  salto: "salto semantico",
  cosechado: "vecindario (cosechado)",
};

function fmtNodo(nid: string, graph: Grafo, families: Record<string, string>): string {
  const n = graph[nid];
  const fam = families[nid] ?? "general";
  const et = etiquetaArbol(nid, graph);
  const titulo = n?.titulo_concepto ?? nid;
  return `\`${nid}\` — **${et}** (titulo: _${titulo}_ · familia: ${fam} · fase: ${n?.fase_proyecto ?? "?"})`;
}

function recorta(s: unknown, n = 220): string {
  const t = String(s ?? "").replace(/\s+/g, " ").trim();
  return t.length > n ? t.slice(0, n) + "…" : t;
}

function fmtFecha(iso: string | null): string {
  if (!iso) return "—";
  return new Date(iso).toISOString().replace("T", " ").slice(0, 16);
}

async function main() {
  const url = process.env.NEXT_PUBLIC_SUPABASE_URL ?? process.env.SUPABASE_URL;
  const key = process.env.SUPABASE_SERVICE_ROLE_KEY;
  if (!url || !key) {
    console.error("Faltan SUPABASE_URL / SUPABASE_SERVICE_ROLE_KEY en el entorno.");
    process.exit(1);
  }
  const supabase: SupabaseClient = createClient(url, key);

  const args = process.argv.slice(2);
  const idxBuscar = args.indexOf("--buscar");
  let projectId: string | null = null;

  if (idxBuscar >= 0) {
    const texto = args[idxBuscar + 1];
    if (!texto) throw new Error("--buscar requiere un texto");
    const { data, error } = await supabase
      .from("projects")
      .select("id, titulo, entrada_original")
      .ilike("entrada_original", `%${texto}%`)
      .order("created_at", { ascending: false })
      .limit(1);
    if (error) throw error;
    const fila = (data ?? [])[0] as FilaProyecto | undefined;
    if (!fila) throw new Error(`sin proyecto que contenga "${texto}" en su entrada`);
    projectId = fila.id;
  } else {
    const id = args[0];
    if (!id) throw new Error("uso: forense.ts <session_id | project_id> | --buscar <texto>");
    // Un id de sesion resuelve a su proyecto; un id de proyecto se usa tal cual.
    const { data: ses } = await supabase.from("sessions").select("project_id").eq("id", id).limit(1);
    const filaSes = (ses ?? [])[0] as { project_id: string } | undefined;
    projectId = filaSes?.project_id ?? id;
  }

  const [{ data: proyRows }, { data: sesRows }, { data: nodoRows }] = await Promise.all([
    supabase.from("projects").select("id, titulo, entrada_original, fase_actual").eq("id", projectId).limit(1),
    supabase
      .from("sessions")
      .select("id, project_id, tipo, dominio, created_at, closed_at, estado_recorrido, decisiones, calidad, costo_usd, costo_desglose, presupuesto_excedido")
      .eq("project_id", projectId)
      .order("created_at", { ascending: true }),
    supabase.from("project_nodes").select("session_id, node_id, tipo").eq("project_id", projectId),
  ]);
  const proyecto = (proyRows ?? [])[0] as FilaProyecto | undefined;
  if (!proyecto) throw new Error(`proyecto ${projectId} no encontrado`);
  const sesiones = (sesRows ?? []) as FilaSesion[];
  const nodos = (nodoRows ?? []) as FilaNodo[];
  const idsSesiones = sesiones.map((s) => s.id);
  const { data: planRows } = idsSesiones.length
    ? await supabase
        .from("plans")
        .select("session_id, etiqueta, contenido_md, created_at, dominio")
        .in("session_id", idsSesiones)
        .order("created_at", { ascending: true })
    : { data: [] };
  const planes = (planRows ?? []) as FilaPlan[];

  const graph = cargarGrafo();
  const families = cargarFamilies() as unknown as Record<string, string>;

  const L: string[] = [];
  const log = (linea = "") => L.push(linea);

  log(`# Forense de sesion — ${proyecto.titulo ?? proyecto.id}`);
  log("");
  log(`- **Proyecto:** \`${proyecto.id}\``);
  log(`- **Idea original:** ${recorta(proyecto.entrada_original, 400)}`);
  log(`- **Fase actual:** ${proyecto.fase_actual ?? "?"}`);
  log(`- **Sesiones:** ${sesiones.length}`);
  log(`- **Generado:** ${new Date().toISOString().slice(0, 16).replace("T", " ")}`);
  log("");

  // Acumuladores de proyecto para la procedencia global.
  const tiposGlobales = new Map<string, number>();
  const prioridadTurnos: Array<{ sesion: number; turno: number; prioridad: unknown }> = [];
  let prioridadRegistrada = false; // ¿la bitacora TRAE el campo (Fase 3.9+)?

  sesiones.forEach((s, si) => {
    log(`---`);
    log("");
    log(`## Sesion ${si + 1} — \`${s.id}\``);
    log(
      `tipo: **${s.tipo}** · dominio: ${s.dominio ?? "core"} · abierta ${fmtFecha(s.created_at)} · cerrada ${fmtFecha(s.closed_at)} · costo $${(s.costo_usd ?? 0).toFixed(4)}${s.presupuesto_excedido ? " · ⚠ PRESUPUESTO EXCEDIDO" : ""}`
    );
    log("");

    // --- Recorrido en orden ---
    const rec = s.estado_recorrido?.recorrido;
    const ruta = rec?.ruta ?? [];
    const modos = rec?.modos ?? [];
    log(`### Recorrido (${ruta.length} nodos)`);
    if (ruta.length === 0) log("_sin recorrido persistido (sesion sin entrevista, p.ej. organizador)._");
    ruta.forEach((nid, i) => {
      const modo = modos[i] ?? "conversado";
      log(`${i + 1}. [${TIPO_LEGIBLE[modo] ?? modo}] ${fmtNodo(nid, graph, families)}`);
    });
    log("");

    // --- Decisiones por turno ---
    const decisiones = s.decisiones ?? [];
    const turnos = decisiones.filter((e) => e.tipo === "decision_turno");
    log(`### Decisiones por turno (${turnos.length})`);
    turnos.forEach((e, ti) => {
      const dec = (e.decision ?? {}) as { accion?: string; camino?: string[]; es_salto?: boolean };
      const saltos = (e.saltos_posibles ?? []) as Array<{ id: string; titulo: string; afinidad: number }>;
      const topSaltos = [...saltos].sort((a, b) => b.afinidad - a.afinidad).slice(0, 3);
      const nodoActual = e.nodo_actual ? etiquetaArbol(String(e.nodo_actual), graph) : "—";
      log(`**Turno ${ti + 1}** · nodo actual: ${nodoActual}`);
      log(`- respuesta del usuario: ${recorta(e.respuesta_usuario)}`);
      log(`- decision: **${dec.accion ?? "?"}**${dec.es_salto ? " · ES SALTO" : ""} → camino [${(dec.camino ?? []).join(", ") || "—"}]`);
      log(`- razonamiento: ${e.razonamiento ? recorta(e.razonamiento) : "_(automatico, sin razonamiento)_"}`);
      // score de la brujula (SI persistido): top candidatos de salto por afinidad
      if (topSaltos.length > 0) {
        log(`- brujula (top saltos por afinidad): ${topSaltos.map((c) => `${etiquetaArbol(c.id, graph)} = ${c.afinidad}`).join(" · ")}`);
      }
      log(`- candidatos locales: ${((e.candidatos_locales ?? []) as string[]).length}`);
      // prioridad_declarada (Fase 3.9): puede faltar en sesiones previas al fix
      if ("prioridad_declarada" in e) {
        prioridadRegistrada = true;
        if (e.prioridad_declarada) {
          prioridadTurnos.push({ sesion: si + 1, turno: ti + 1, prioridad: e.prioridad_declarada });
          log(`- **prioridad declarada este turno:** \`${JSON.stringify(e.prioridad_declarada)}\``);
        }
      }
      log("");
    });

    // --- Saltos con candidatos perdedores ---
    const saltosReales = turnos.filter((e) => (e.decision as { es_salto?: boolean })?.es_salto);
    if (saltosReales.length > 0) {
      log(`### Saltos semanticos (${saltosReales.length})`);
      saltosReales.forEach((e) => {
        const dec = e.decision as { camino?: string[] };
        const destino = (dec.camino ?? []).at(-1);
        const saltos = (e.saltos_posibles ?? []) as Array<{ id: string; afinidad: number }>;
        const ganador = saltos.find((c) => c.id === destino);
        const perdedores = saltos.filter((c) => c.id !== destino).sort((a, b) => b.afinidad - a.afinidad).slice(0, 4);
        log(`- desde ${etiquetaArbol(String(e.nodo_actual), graph)} → **${destino ? etiquetaArbol(destino, graph) : "?"}** (afinidad ${ganador?.afinidad ?? "?"})`);
        if (perdedores.length > 0) {
          log(`  - candidatos que perdieron: ${perdedores.map((c) => `${etiquetaArbol(c.id, graph)} = ${c.afinidad}`).join(" · ")}`);
        }
      });
      log("");
    }

    // --- Otros eventos de la caja de vidrio ---
    const otros = decisiones.filter((e) => e.tipo !== "decision_turno");
    if (otros.length > 0) {
      log(`### Otros eventos (${otros.length})`);
      const porTipo = new Map<string, number>();
      for (const e of otros) porTipo.set(String(e.tipo), (porTipo.get(String(e.tipo)) ?? 0) + 1);
      for (const [tipo, n] of porTipo) log(`- \`${tipo}\`: ${n}`);
      // muestra de los que importan al auditor
      for (const e of otros) {
        if (["cifra_mercado_inventada", "numero_huerfano", "salida_sin_acentos"].includes(String(e.tipo))) {
          log(`  - **${e.tipo}**: ${recorta(e.contexto ?? e.muestra ?? e.valor)}`);
        }
      }
      log("");
    }

    // --- Veredicto del juez ---
    if (s.calidad) {
      log(`### Veredicto del juez de sesion`);
      log("```json");
      log(JSON.stringify(s.calidad, null, 2));
      log("```");
      log("");
    }

    // --- Costos por componente ---
    if (s.costo_desglose && Object.keys(s.costo_desglose).length > 0) {
      log(`### Costos por componente`);
      for (const [comp, usd] of Object.entries(s.costo_desglose)) log(`- ${comp}: $${Number(usd).toFixed(4)}`);
      log("");
    }

    for (const m of modos) tiposGlobales.set(m, (tiposGlobales.get(m) ?? 0) + 1);
  });

  // --- Procedencia del plan (recorrido vs vecindario, con nombres) ---
  log(`---`);
  log("");
  log(`## Procedencia de lo persistido (project_nodes)`);
  const porTipoNodo = new Map<string, FilaNodo[]>();
  for (const n of nodos) {
    if (!porTipoNodo.has(n.tipo)) porTipoNodo.set(n.tipo, []);
    porTipoNodo.get(n.tipo)!.push(n);
  }
  const delRecorrido = nodos.filter((n) => n.tipo !== "cosechado").length;
  const delVecindario = (porTipoNodo.get("cosechado") ?? []).length;
  log(`Total ${nodos.length} nodos: **${delRecorrido} del recorrido** (conversado/silencioso/salto) + **${delVecindario} del vecindario** (cosechado).`);
  log("");
  for (const [tipo, lista] of porTipoNodo) {
    log(`**${TIPO_LEGIBLE[tipo] ?? tipo}** (${lista.length}):`);
    for (const n of lista) log(`- ${fmtNodo(n.node_id, graph, families)}`);
    log("");
  }
  log(
    "_Nota: el desglose POR ETAPA del plan (que nodo alimento cada etapa) vive en la " +
      "autodeclaracion ===JSON=== del redactor, que NO se persiste separada; lo que si " +
      "queda es esta procedencia global por tipo._"
  );
  log("");

  // --- Planes ---
  if (planes.length > 0) {
    log(`## Planes generados (${planes.length})`);
    for (const p of planes) {
      const pie = p.contenido_md.match(/_Este plan se aliment[oó][\s\S]*?_/);
      log(`- **${p.etiqueta}** (${p.dominio ?? "core"}, ${fmtFecha(p.created_at)}) — ${pie ? recorta(pie[0]) : "sin pie de procedencia"}`);
    }
    log("");
  }

  // --- E16: ¿disparo la regla de prioridad_declarada? ---
  log(`## Prioridad declarada (Fase 3.9 E16)`);
  if (!prioridadRegistrada) {
    log(
      "⚠ La bitacora de esta(s) sesion(es) **NO registra** `prioridad_declarada` por turno: " +
        "las sesiones son PREVIAS al fix de Fase 3.9 que empezo a persistirla. No puede " +
        "afirmarse desde la bitacora en que turnos disparo la regla."
    );
  } else if (prioridadTurnos.length === 0) {
    log("La regla de prioridad_declarada **no disparo en ningun turno** registrado.");
  } else {
    log("La regla disparo en:");
    for (const p of prioridadTurnos) log(`- Sesion ${p.sesion}, turno ${p.turno}: \`${JSON.stringify(p.prioridad)}\``);
  }
  // La prioridad FINAL acumulada si esta en el estado (dato de lectura directa).
  const prioridadFinal = sesiones
    .map((s, i) => ({ i: i + 1, p: s.estado_recorrido?.recorrido?.prioridadDeclarada }))
    .filter((x) => x.p);
  if (prioridadFinal.length > 0) {
    log("");
    log("Prioridad final acumulada en el estado de la sesion (estado_recorrido):");
    for (const x of prioridadFinal) log(`- Sesion ${x.i}: \`${JSON.stringify(x.p)}\``);
  }
  log("");

  const outDir = path.join(ROOT, "examples", "forense");
  mkdirSync(outDir, { recursive: true });
  const outPath = path.join(outDir, `${projectId}.md`);
  writeFileSync(outPath, L.join("\n") + "\n", "utf-8");
  console.log(`Forense escrito en ${outPath} (${L.length} lineas, ${sesiones.length} sesiones).`);
}

main().catch((e) => {
  console.error(e);
  process.exit(1);
});
