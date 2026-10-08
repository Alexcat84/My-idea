/**
 * EXPORTADOR DE LA CORRIDA FINAL (decisión del fundador, 8 oct 2026): deja en docs/corrida_final/<fecha>/ todo lo que
 * la corrida generó, legible para el fundador. No llama a la IA.
 *
 * Lee de Supabase (service role del .env raíz) las sesiones del dev user dentro de la ventana y, de cada proyecto
 * tocado, baja por la API de la app (como el dev user, VUELO_BASE_URL) los documentos TAL COMO LOS LEE LA PERSONA
 * (Tu Plan, cada seguimiento, cada plan de mundo, el expediente, la bitácora, el análisis) y su checklist.
 *
 * Escribe:
 *   proyectos/<nn>-<titulo>/README.md               la idea, el estado vivo, la ficha y el índice de sus sesiones
 *   proyectos/<nn>-<titulo>/sesion-<k>-<espacio>.md   preguntas y respuestas turno a turno, el recorrido por los nodos
 *                                                     con el motivo de cada decisión, el veredicto del juez de sesión,
 *                                                     y el coste llamada por llamada (con lo leído y escrito de caché)
 *   proyectos/<nn>-<titulo>/documentos/<clave>.md     cada documento de la app
 *   proyectos/<nn>-<titulo>/checklist.md
 *   COSTES.md                                         por llamada, por sesión, por mundo y total, y la consulta SQL
 *
 * Sin claves, contraseñas ni correos: todo texto pasa por limpiar() antes de escribirse.
 *
 * Uso (desde web/, con el .env raíz y VUELO_BASE_URL en el entorno):
 *   npx tsx scripts/corrida_final_exportar.ts --desde <ISO UTC> --hasta <ISO UTC> --salida ../docs/corrida_final/2026-10-08
 */
import { createClient } from "@supabase/supabase-js";
import { mkdirSync, writeFileSync } from "node:fs";
import path from "node:path";
import { autenticarComoDevUser, BASE_URL, cargarEnvRaiz } from "./_shared/http";
import { cargarGrafo, etiquetaArbol } from "../lib/engine/graph";
import { nombreDeMundo } from "../lib/catalogoMundos";

cargarEnvRaiz();

const DEV_EMAIL = "dev@my-idea.local";

function arg(n: string): string | null {
  const i = process.argv.indexOf(n);
  return i >= 0 ? process.argv[i + 1] ?? null : null;
}

/** Quita correos, claves y tokens de cualquier texto exportado. */
export function limpiar(t: string): string {
  return t
    .replace(/[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}/g, "[correo]")
    .replace(/sk-ant-[A-Za-z0-9_-]+/g, "[clave]")
    .replace(/eyJ[A-Za-z0-9_-]{20,}\.[A-Za-z0-9_-]+\.[A-Za-z0-9_-]+/g, "[token]")
    .replace(/\bpa-[A-Za-z0-9_-]{20,}/g, "[clave]");
}

const slug = (s: string) =>
  s
    .normalize("NFD")
    .replace(/[̀-ͯ]/g, "")
    .toLowerCase()
    .replace(/[^a-z0-9]+/g, "-")
    .replace(/^-|-$/g, "")
    .slice(0, 50) || "sin-titulo";

const espacio = (d: string | null | undefined) => (!d || d === "core" ? "Tu viaje (núcleo)" : nombreDeMundo(d));
const usd = (n: number | null | undefined) => (typeof n === "number" ? `$${n.toFixed(4)}` : "—");

interface Llamada {
  componente: string | null;
  modelo: string;
  in: number;
  out: number;
  cache_read: number;
  cache_write_5m: number;
  cache_write_1h: number;
  usd: number;
  stop_reason?: string | null;
}

function escribir(ruta: string, texto: string) {
  mkdirSync(path.dirname(ruta), { recursive: true });
  writeFileSync(ruta, limpiar(texto), "utf8");
}

async function main() {
  const desde = arg("--desde");
  const hasta = arg("--hasta") ?? new Date().toISOString();
  const salida = arg("--salida");
  if (!desde || !salida) throw new Error("uso: --desde <ISO> [--hasta <ISO>] --salida <carpeta>");
  const sb = createClient(process.env.SUPABASE_URL!, process.env.SUPABASE_SERVICE_ROLE_KEY!, { auth: { persistSession: false } });
  const grafo = cargarGrafo();
  const etiqueta = (nid: string) => (grafo[nid] ? etiquetaArbol(nid, grafo) : nid);

  // el dev user
  let devId: string | null = null;
  for (let page = 1; page <= 200 && !devId; page++) {
    const { data } = await sb.auth.admin.listUsers({ page, perPage: 1000 });
    const u = data.users.find((x) => x.email === DEV_EMAIL);
    if (u) devId = u.id;
    if (data.users.length === 0) break;
  }
  if (!devId) throw new Error("no encuentro el dev user");

  const { data: sesiones, error } = await sb
    .from("sessions")
    .select("id, project_id, tipo, dominio, created_at, closed_at, mensaje_entrada, estado_recorrido, decisiones, calidad, costo_usd, costo_desglose")
    .eq("user_id", devId)
    .gte("created_at", desde)
    .lt("created_at", hasta)
    .order("created_at", { ascending: true });
  if (error) throw error;
  const proyIds = [...new Set((sesiones ?? []).map((s) => s.project_id as string))];
  const { data: proyectos } = await sb
    .from("projects")
    .select("id, titulo, entrada_original, estado_vivo, memoria, created_at, realizada_at")
    .in("id", proyIds.length ? proyIds : ["00000000-0000-0000-0000-000000000000"]);

  const cookie = await autenticarComoDevUser();
  const getApi = async (ruta: string) => {
    const r = await fetch(`${BASE_URL}${ruta}`, { headers: { Cookie: cookie } });
    return r.ok ? r : null;
  };

  const costes: Array<{ proyecto: string; sesion: string; espacio: string; tipo: string; usd: number; llamadas: Llamada[] }> = [];
  const ordenProy = (proyectos ?? []).sort((a, b) => String(a.created_at).localeCompare(String(b.created_at)));
  for (const [ip, p] of ordenProy.entries()) {
    const nombre = (p.titulo as string | null) ?? String(p.entrada_original ?? "").slice(0, 60);
    const dir = path.join(salida, "proyectos", `${String(ip + 1).padStart(2, "0")}-${slug(nombre)}`);
    const memoria = (p.memoria ?? {}) as { ficha?: Record<string, unknown>; hilo?: Array<Record<string, unknown>> };
    const hilo = memoria.hilo ?? [];
    const suyas = (sesiones ?? []).filter((s) => s.project_id === p.id);

    // README del proyecto
    const R: string[] = [`# ${nombre}`, "", "## La idea, tal como la escribió la persona", "", String(p.entrada_original ?? ""), ""];
    R.push("## Estado vivo (memoria del proyecto al cierre)", "", String(p.estado_vivo ?? "—"), "");
    R.push("## Ficha de contexto", "", "```json", JSON.stringify(memoria.ficha ?? {}, null, 2), "```", "");
    R.push("## Sesiones", "");
    for (const [k, s] of suyas.entries()) R.push(`${k + 1}. ${espacio(s.dominio as string)} · ${s.tipo} · ${s.created_at} · ${usd(s.costo_usd as number)}`);
    escribir(path.join(dir, "README.md"), R.join("\n") + "\n");

    // cada sesión
    for (const [k, s] of suyas.entries()) {
      const er = (s.estado_recorrido ?? {}) as {
        recorrido?: { ruta?: string[]; modos?: string[]; fallbackEvents?: Array<Record<string, unknown>> };
        acumulado?: { llamadas?: Llamada[] };
      };
      const L: string[] = [`# Sesión ${k + 1}: ${espacio(s.dominio as string)} (${s.tipo})`, ""];
      L.push(`Abrió: ${s.created_at} · cerró: ${s.closed_at ?? "abierta"} · coste: ${usd(s.costo_usd as number)}`, "");
      L.push("## La entrada", "", String(s.mensaje_entrada ?? ""), "");
      L.push("## Preguntas de la app y respuestas, turno a turno", "");
      const turnos = hilo.filter((t) => t.sesion === s.id);
      if (turnos.length === 0) L.push("_Sin turnos en el hilo de la memoria._");
      for (const [i, t] of turnos.entries()) {
        L.push(`### Turno ${i + 1}${t.nodo ? ` · ${etiqueta(String(t.nodo))}` : ""}`, "");
        L.push(`**App:** ${t.pregunta ?? "—"}`, "", `**Persona:** ${t.respuesta ?? "—"}`, "");
      }
      L.push("## El recorrido por los nodos", "");
      const ruta = er.recorrido?.ruta ?? [];
      const modos = er.recorrido?.modos ?? [];
      ruta.forEach((nid, i) => L.push(`${i + 1}. ${etiqueta(nid)} (\`${nid}\`) · ${modos[i] ?? "—"}`));
      L.push("", "## Las decisiones de cada turno (el motivo)", "");
      const decisiones = Array.isArray(s.decisiones) ? (s.decisiones as Array<Record<string, unknown>>) : [];
      if (decisiones.length === 0) L.push("_Sin decisiones registradas._");
      for (const [i, d] of decisiones.entries()) L.push(`${i + 1}. \`${JSON.stringify(d)}\``);
      const eventos = er.recorrido?.fallbackEvents ?? [];
      if (eventos.length) {
        L.push("", "## Eventos (adaptación de preguntas, respaldos, guardián)", "");
        for (const e of eventos) L.push(`- \`${JSON.stringify(e)}\``);
      }
      L.push("", "## Veredicto del juez de sesión", "", "```json", JSON.stringify(s.calidad ?? null, null, 2), "```", "");
      L.push("## Coste", "", `Por componente: \`${JSON.stringify(s.costo_desglose ?? {})}\``, "");
      const llamadas = er.acumulado?.llamadas ?? [];
      if (llamadas.length) {
        L.push("| # | componente | modelo | entrada | salida | caché leída | caché 5 min | caché 1 h | USD | fin |");
        L.push("|---|---|---|---|---|---|---|---|---|---|");
        llamadas.forEach((c, i) =>
          L.push(`| ${i + 1} | ${c.componente ?? ""} | ${c.modelo} | ${c.in} | ${c.out} | ${c.cache_read} | ${c.cache_write_5m} | ${c.cache_write_1h} | ${c.usd.toFixed(5)} | ${c.stop_reason ?? ""} |`)
        );
      } else {
        L.push("_La sesión no guardó el registro llamada por llamada._");
      }
      escribir(path.join(dir, `sesion-${String(k + 1).padStart(2, "0")}-${slug(espacio(s.dominio as string))}.md`), L.join("\n") + "\n");
      costes.push({ proyecto: nombre, sesion: String(s.id), espacio: espacio(s.dominio as string), tipo: String(s.tipo), usd: Number(s.costo_usd ?? 0), llamadas });
    }

    // documentos de la app, tal como los lee la persona
    const indice = await getApi(`/api/project/${p.id}/documentos`);
    if (indice) {
      const j = (await indice.json()) as { documentos?: Array<{ clave: string; titulo?: string }> };
      for (const [n, d] of (j.documentos ?? []).entries()) {
        const r = await getApi(`/api/project/${p.id}/documentos?doc=${encodeURIComponent(d.clave)}`);
        if (!r) continue;
        const ct = r.headers.get("content-type") ?? "";
        const cuerpo = ct.includes("json") ? ((await r.json()) as { markdown?: string }).markdown ?? "" : await r.text();
        escribir(path.join(dir, "documentos", `${String(n + 1).padStart(2, "0")}-${slug(d.titulo ?? d.clave)}.md`), cuerpo);
      }
    }
    // checklist
    const ck = await getApi(`/api/project/${p.id}/checklist`);
    if (ck) {
      const j = (await ck.json()) as { planes?: Array<{ dominio: string; etapas: Array<{ etapa: number; items: Array<Record<string, unknown>> }> }> };
      const C: string[] = [`# Checklist de ${nombre}`, ""];
      for (const pl of j.planes ?? []) {
        C.push(`## ${espacio(pl.dominio)}`, "");
        for (const e of pl.etapas) {
          C.push(`### Etapa ${e.etapa}`, "");
          for (const it of e.items) {
            C.push(`- [${it.estado === "hecho" ? "x" : " "}] ${it.texto} · estado: ${it.estado}${it.fecha_base ? ` · fecha: ${String(it.fecha_base).slice(0, 10)}` : ""}${it.banda ? ` · banda: ${it.banda}` : ""}`);
          }
          C.push("");
        }
      }
      escribir(path.join(dir, "checklist.md"), C.join("\n") + "\n");
    }
  }

  // COSTES
  const K: string[] = ["# Costes de la corrida final (la app)", "", `Ventana: ${desde} a ${hasta}. Sesiones: ${costes.length}.`, ""];
  const total = costes.reduce((a, c) => a + c.usd, 0);
  K.push(`**Total de la app (suma de sessions.costo_usd): ${usd(total)}**`, "");
  const porEspacio = new Map<string, number>();
  for (const c of costes) porEspacio.set(c.espacio, (porEspacio.get(c.espacio) ?? 0) + c.usd);
  K.push("## Por espacio (núcleo y cada mundo)", "", "| Espacio | USD |", "|---|---|");
  for (const [e, v] of [...porEspacio.entries()].sort((a, b) => b[1] - a[1])) K.push(`| ${e} | ${usd(v)} |`);
  K.push("", "## Por sesión", "", "| Proyecto | Espacio | Tipo | USD | Llamadas | Caché leída | Caché escrita |", "|---|---|---|---|---|---|---|");
  for (const c of costes) {
    const leida = c.llamadas.reduce((a, l) => a + l.cache_read, 0);
    const escrita = c.llamadas.reduce((a, l) => a + l.cache_write_5m + l.cache_write_1h, 0);
    K.push(`| ${c.proyecto.slice(0, 40)} | ${c.espacio} | ${c.tipo} | ${usd(c.usd)} | ${c.llamadas.length} | ${leida} | ${escrita} |`);
  }
  const porModelo = new Map<string, { usd: number; n: number }>();
  for (const c of costes) for (const l of c.llamadas) {
    const m = porModelo.get(l.modelo) ?? { usd: 0, n: 0 };
    porModelo.set(l.modelo, { usd: m.usd + l.usd, n: m.n + 1 });
  }
  K.push("", "## Por modelo (del registro llamada por llamada)", "", "| Modelo | Llamadas | USD |", "|---|---|---|");
  for (const [m, v] of porModelo) K.push(`| ${m} | ${v.n} | ${usd(v.usd)} |`);
  K.push("", "## La consulta para cuadrar con la medición del fundador (SQL Editor)", "", "```sql");
  K.push(
    "SELECT count(*) AS sesiones, round(sum(costo_usd)::numeric, 4) AS usd",
    "FROM sessions",
    `WHERE user_id = (SELECT id FROM auth.users WHERE email = '[correo del dev user]')`,
    `  AND created_at >= '${desde}' AND created_at < '${hasta}';`,
    "```"
  );
  escribir(path.join(salida, "COSTES.md"), K.join("\n") + "\n");
  console.log(`exportadas ${costes.length} sesiones de ${ordenProy.length} proyectos; total app ${usd(total)}`);
}

main().catch((e) => {
  console.error(e);
  process.exit(1);
});
