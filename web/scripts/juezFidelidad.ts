/**
 * EXTRACTOR DEL JUEZ DE FIDELIDAD DE LA SALIDA (corrida final, paso D; docs/producto/CORRIDA_FINAL.md y
 * docs/producto/JUEZ_FIDELIDAD.md; ficha `juez-fidelidad-salida` de docs/PENDIENTES.md). Corre DESPUES de B y C.
 *
 * Lee de Supabase (service role, del .env raiz) cada salida que la persona leyo como consejo dentro de la ventana de
 * la corrida (planes del nucleo, Claridades, planes de mundo y replanteamientos del usuario indicado), arma un paquete
 * por salida con su material (lib/coherencia/juezFidelidad.ts) y planta 1 trampa sin marca por cada 5 salidas.
 *
 * Escribe en DOS carpetas fuera del repo, distintas y vacias:
 *  - la de los paquetes: un <id>.json por paquete, lo unico que abre cada juez (junto con JUEZ_FIDELIDAD.md);
 *  - la de las claves: claves.json, que dice que paquete es real (y de que plan y sesion) y cual es trampa (con su
 *    tipo y su frase plantada). Ningun juez la abre.
 *
 * No llama a la API de Anthropic: los jueces y el arbitro son agentes de Claude Code.
 *
 * Uso (desde web/, con el .env raiz):
 *   npx tsx scripts/juezFidelidad.ts --desde <ISO UTC> [--hasta <ISO UTC>] [--usuario <email>] \
 *     --paquetes <carpeta> --claves <carpeta>             # dice lo que haria; no escribe nada
 *   ... --escribir                                         # escribe los paquetes y las claves
 * --desde y --hasta son las horas 4 y 11 de la lista de comprobacion; --hasta por defecto es ahora y --usuario el dev
 * user. Sale con codigo 1 si falta algo o si no hay ninguna salida en la ventana.
 */
import { createClient, type SupabaseClient } from "@supabase/supabase-js";
import { existsSync, mkdirSync, readdirSync, writeFileSync } from "node:fs";
import path from "node:path";
import { cargarEnvRaiz, ROOT } from "./_shared/http";
import { cargarEntrySeeds, cargarGrafo } from "../lib/engine/graph";
import {
  armarSalidas,
  plantarTrampas,
  SEMILLA_FIDELIDAD,
  tipoDeSalida,
  type FilaItemJuez,
  type FilaPlanJuez,
  type FilaProyectoJuez,
  type FilaSesionJuez,
  type FilaVisitaJuez,
} from "../lib/coherencia/juezFidelidad";

cargarEnvRaiz();

const DEV_EMAIL = "dev@my-idea.local";
const LOTE_IDS = 100;
const PAGINA = 1000;

function arg(nombre: string): string | null {
  const i = process.argv.indexOf(nombre);
  if (i < 0) return null;
  const v = process.argv[i + 1];
  return v && !v.startsWith("--") ? v : "";
}

function fecha(nombre: string, v: string | null): string | null {
  if (v === null) return null;
  const t = Date.parse(v);
  if (!v || Number.isNaN(t)) throw new Error(`${nombre} no es una fecha valida: '${v}' (ej. 2026-10-08T14:00:00Z)`);
  return new Date(t).toISOString();
}

/** Las dos carpetas: fuera del repo, distintas, una no dentro de la otra, y vacias si ya existen. */
function problemasDeCarpetas(paquetes: string | null, claves: string | null): string[] {
  const p: string[] = [];
  if (!paquetes) p.push("falta --paquetes <carpeta fuera del repo>");
  if (!claves) p.push("falta --claves <carpeta fuera del repo, distinta de la de los paquetes>");
  if (!paquetes || !claves) return p;
  const dentro = (hijo: string, padre: string) => {
    const rel = path.relative(padre, hijo);
    return rel === "" || (!rel.startsWith("..") && !path.isAbsolute(rel));
  };
  for (const [nombre, dir] of [["--paquetes", paquetes], ["--claves", claves]] as const) {
    if (dentro(dir, ROOT)) p.push(`${nombre} (${dir}) esta dentro del repo: tiene que ir fuera`);
    if (existsSync(dir) && readdirSync(dir).length > 0) p.push(`${nombre} (${dir}) no esta vacia: no se mezclan tandas`);
  }
  if (dentro(paquetes, claves) || dentro(claves, paquetes)) p.push("las claves no pueden vivir en la carpeta de los paquetes (ni al reves)");
  return p;
}

async function idDelUsuario(admin: SupabaseClient, email: string): Promise<string> {
  for (let page = 1; ; page++) {
    const { data, error } = await admin.auth.admin.listUsers({ page, perPage: PAGINA });
    if (error) throw new Error(`no se pudieron leer los usuarios: ${error.message}`);
    const u = data.users.find((x) => x.email?.toLowerCase() === email.toLowerCase());
    if (u) return u.id;
    if (data.users.length < PAGINA) throw new Error(`no existe el usuario ${email}`);
  }
}

/** Todas las filas de `tabla` cuyo `columna` esta en `ids`, por lotes y por paginas (orden estable por id). */
async function leerPorLotes<T>(admin: SupabaseClient, tabla: string, columnas: string, columna: string, ids: string[]): Promise<T[]> {
  const out: T[] = [];
  for (let i = 0; i < ids.length; i += LOTE_IDS) {
    const lote = ids.slice(i, i + LOTE_IDS);
    for (let desde = 0; ; desde += PAGINA) {
      const { data, error } = await admin.from(tabla).select(columnas).in(columna, lote).order("id").range(desde, desde + PAGINA - 1);
      if (error) throw new Error(`${tabla}: ${error.message}`);
      const filas = (data ?? []) as unknown as T[];
      out.push(...filas);
      if (filas.length < PAGINA) break;
    }
  }
  return out;
}

async function planesDeLaVentana(admin: SupabaseClient, userId: string, desde: string, hasta: string): Promise<FilaPlanJuez[]> {
  const out: FilaPlanJuez[] = [];
  for (let i = 0; ; i += PAGINA) {
    const { data, error } = await admin
      .from("plans")
      .select("id, session_id, etiqueta, dominio, contenido_md, created_at")
      .eq("user_id", userId)
      .gte("created_at", desde)
      .lt("created_at", hasta)
      .order("id")
      .range(i, i + PAGINA - 1);
    if (error) throw new Error(`plans: ${error.message}`);
    const filas = (data ?? []) as FilaPlanJuez[];
    out.push(...filas);
    if (filas.length < PAGINA) break;
  }
  return out;
}

const unicos = (xs: string[]) => [...new Set(xs)];

async function main() {
  const escribir = process.argv.includes("--escribir");
  const desde = fecha("--desde", arg("--desde"));
  const hasta = fecha("--hasta", arg("--hasta")) ?? new Date().toISOString();
  const usuario = arg("--usuario") || DEV_EMAIL;
  const dirPaquetes = arg("--paquetes") ? path.resolve(arg("--paquetes")!) : null;
  const dirClaves = arg("--claves") ? path.resolve(arg("--claves")!) : null;

  console.log("JUEZ DE FIDELIDAD DE LA SALIDA: el extractor de paquetes");
  const faltan: string[] = [];
  if (!desde) faltan.push("falta --desde <ISO UTC> (la hora 4 de la lista de comprobacion)");
  for (const v of ["NEXT_PUBLIC_SUPABASE_URL", "SUPABASE_SERVICE_ROLE_KEY"]) if (!process.env[v]?.trim()) faltan.push(`falta ${v} en el entorno (.env raiz)`);
  const carpetas = problemasDeCarpetas(dirPaquetes, dirClaves);
  if (escribir) faltan.push(...carpetas);
  if (faltan.length) {
    for (const f of faltan) console.error(`  NO: ${f}`);
    process.exit(1);
  }

  const admin = createClient(process.env.NEXT_PUBLIC_SUPABASE_URL!, process.env.SUPABASE_SERVICE_ROLE_KEY!);
  const userId = await idDelUsuario(admin, usuario);
  console.log(`  usuario: ${usuario}`);
  console.log(`  ventana: ${desde} a ${hasta}`);

  const enVentana = (await planesDeLaVentana(admin, userId, desde!, hasta)).filter((p) => tipoDeSalida(p.etiqueta, p.dominio));
  if (enVentana.length === 0) {
    console.error("  NO: ninguna salida que juzgar en la ventana (planes, Claridades ni replanteamientos)");
    process.exit(1);
  }
  const idsVentana = new Set(enVentana.map((p) => p.id));

  // Los proyectos de esas salidas, con TODAS sus sesiones y planes: el plan anterior puede ser de antes de la ventana.
  const sesionesVentana = await leerPorLotes<{ id: string; project_id: string }>(admin, "sessions", "id, project_id", "id", unicos(enVentana.map((p) => p.session_id)));
  const idsProyectos = unicos(sesionesVentana.map((s) => s.project_id));
  const sesiones = await leerPorLotes<FilaSesionJuez>(
    admin,
    "sessions",
    "id, project_id, dominio, tipo, mensaje_entrada, ruta, estado_recorrido, created_at",
    "project_id",
    idsProyectos
  );
  const idsSesiones = sesiones.map((s) => s.id);
  const planes = await leerPorLotes<FilaPlanJuez>(admin, "plans", "id, session_id, etiqueta, dominio, contenido_md, created_at", "session_id", idsSesiones);
  const proyectos = await leerPorLotes<FilaProyectoJuez>(admin, "projects", "id, entrada_original, memoria, numeros_proyecto", "id", idsProyectos);

  // La cosecha: del diario (037). Sin el diario, del estado (que solo guarda la primera vez de cada nodo).
  let visitas: FilaVisitaJuez[];
  try {
    visitas = await leerPorLotes<FilaVisitaJuez>(admin, "node_visits", "session_id, node_id, tipo", "session_id", idsSesiones);
  } catch (e) {
    console.warn(`  AVISO: sin node_visits (${e instanceof Error ? e.message : e}); la cosecha sale de project_nodes y puede quedar corta`);
    visitas = await leerPorLotes<FilaVisitaJuez>(admin, "project_nodes", "session_id, node_id, tipo", "session_id", idsSesiones);
  }
  // nodos_por_etapa: persistido item a item en checklist_items.nodos_origen (037).
  let items: FilaItemJuez[];
  try {
    items = await leerPorLotes<FilaItemJuez>(admin, "checklist_items", "plan_id, etapa, nodos_origen", "plan_id", unicos(planes.map((p) => p.id)));
  } catch (e) {
    console.warn(`  AVISO: sin checklist_items.nodos_origen (${e instanceof Error ? e.message : e}); los paquetes van sin etapas`);
    items = [];
  }

  const grafo = cargarGrafo();
  const salidas = armarSalidas({ planes, sesiones, proyectos, visitas, items }, grafo, cargarEntrySeeds(grafo), (p) => idsVentana.has(p.id));
  const { paquetes, claves } = plantarTrampas(salidas, SEMILLA_FIDELIDAD);

  const porTipo = new Map<string, number>();
  for (const s of salidas) porTipo.set(s.contenido.tipo_salida, (porTipo.get(s.contenido.tipo_salida) ?? 0) + 1);
  const trampas = claves.flatMap((c) => (c.origen === "trampa" ? [c.trampa.tipo] : []));
  console.log(`  salidas: ${salidas.length} en ${idsProyectos.length} proyecto(s) (${[...porTipo].map(([t, n]) => `${t} ${n}`).join(", ")})`);
  console.log(`  trampas: ${trampas.length} (${trampas.join(", ")}), semilla ${SEMILLA_FIDELIDAD}`);
  console.log(`  paquetes: ${paquetes.length} (${paquetes[0]?.paquete} a ${paquetes[paquetes.length - 1]?.paquete})`);
  const sinNodos = salidas.filter((s) => s.contenido.nodos.length === 0);
  if (sinNodos.length) console.warn(`  AVISO: ${sinNodos.length} salida(s) sin nodos: ${sinNodos.map((s) => s.ref.plan_id).join(", ")}`);

  if (!escribir) {
    for (const c of carpetas) console.log(`  (para escribir) ${c}`);
    console.log(`\nNo se ha escrito nada. Escribiria ${paquetes.length} paquetes en ${dirPaquetes ?? "<--paquetes>"} y claves.json en ${dirClaves ?? "<--claves>"}.`);
    console.log("Para escribirlos: --escribir");
    process.exit(0);
  }

  mkdirSync(dirPaquetes!, { recursive: true });
  mkdirSync(dirClaves!, { recursive: true });
  for (const p of paquetes) writeFileSync(path.join(dirPaquetes!, `${p.paquete}.json`), JSON.stringify(p, null, 1) + "\n");
  writeFileSync(
    path.join(dirClaves!, "claves.json"),
    JSON.stringify(
      {
        generado: new Date().toISOString(),
        ventana: { desde, hasta },
        usuario,
        semilla: SEMILLA_FIDELIDAD,
        salidas: salidas.length,
        trampas: trampas.length,
        por_tipo: Object.fromEntries(porTipo),
        claves,
      },
      null,
      1
    ) + "\n"
  );
  console.log(`\nEscritos ${paquetes.length} paquetes en ${dirPaquetes} y las claves en ${path.join(dirClaves!, "claves.json")}.`);
}

main().catch((e) => {
  console.error("EL EXTRACTOR FALLO:", e instanceof Error ? e.message : e);
  process.exit(1);
});
