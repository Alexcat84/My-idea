/**
 * MEDICION BARATA (decision del fundador, corrida final, 8 oct 2026): vuelve a redactar los planes del vuelo desde las
 * entrevistas GUARDADAS, sin repetir el vuelo y SIN GUARDAR NADA en la base, con los arreglos ya en el codigo:
 *   A = solo reglas (los prompts y la limpieza de moneda de hoy), con el mismo redactor de produccion;
 *   B = A + el verificador (lib/engine/verificadorPlan.ts) sobre ese mismo borrador.
 * Escribe A/<plan_id>.md, B/<plan_id>.md y costes.json en la carpeta de salida. Tope duro de gasto: --tope (USD).
 *
 * Se arma igual que la ruta del plan (app/api/session/[id]/plan/route.ts) con lo guardado de cada sesion. Diferencia
 * declarada: el plan anterior de un seguimiento es el que existia ANTES de ese plan (no el vigente de hoy) con sus
 * tareas en su estado de hoy. El estado vivo NO se vuelve a sumar (el perfil guardado ya trae el de su momento), y el
 * contexto guardado se pasa al formato de hoy (contextoAlFormatoNuevo).
 *
 * Uso (desde web/, con el .env raiz): npx tsx scripts/corrida_final_redactar_planes.ts --claves <claves.json> --salida <dir> [--tope 1.9]
 */
import Anthropic from "@anthropic-ai/sdk";
import { createClient } from "@supabase/supabase-js";
import { mkdirSync, readFileSync, writeFileSync } from "node:fs";
import path from "node:path";
import { cargarEnvRaiz } from "./_shared/http";
import { costoAcumuladoUsd, usoVacio, type UsoAcumulado } from "../lib/costmeter";
import { cargarFamilies } from "../lib/readiness";
import { cargarGrafo } from "../lib/engine/graph";
import { finalizarPlan, prepararPlan } from "../lib/engine/planRedactor";
import { generarTextoPlan } from "../lib/engine/redactorPlan";
import { dominiosDelRecorrido, type EstadoRecorrido } from "../lib/engine/recorrido";
import { contextoDeSesion, memoriaDe } from "../lib/engine/memoria";
import { planAnteriorParaIA } from "../lib/engine/replanteamiento";
import { idiomaDePlantilla } from "../lib/i18n/detectarIdioma";
import { verificarPlan } from "../lib/engine/verificadorPlan";
import { obtenerTareasDePlan } from "../lib/db";

cargarEnvRaiz();

/** El contexto guardado antes del 9 oct ("Lo que la persona ya contó, en orden:" y lineas "- [espacio] P: ... R: ...")
 * en el formato de hoy, con el mismo encabezado que textoContextoProyecto. */
export function contextoAlFormatoNuevo(ctx: string): string {
  const ENCABEZADO_VIEJO = "Lo que la persona ya contó, en orden:";
  const ENCABEZADO_NUEVO =
    "Lo que la persona ya contó, en orden. Solo lo que la persona respondió es dato suyo: lo que afirma una pregunta de la IA no es un dato de la persona, aunque no lo haya negado, y si no respondió a lo que se le preguntó, eso sigue sin saberse.";
  return ctx
    .split("\n")
    .map((linea) => {
      if (linea === ENCABEZADO_VIEJO) return ENCABEZADO_NUEVO;
      const conPregunta = linea.match(/^- \[([^\]]+)\] P: (.*?) R: (.*)$/);
      if (conPregunta) return `- [${conPregunta[1]}] La IA preguntó: «${conPregunta[2]}» La persona respondió: «${conPregunta[3]}»`;
      const sinPregunta = linea.match(/^- \[([^\]]+)\] R: (.*)$/);
      if (sinPregunta) return `- [${sinPregunta[1]}] La persona respondió: «${sinPregunta[2]}»`;
      return linea;
    })
    .join("\n");
}

const arg = (n: string) => {
  const i = process.argv.indexOf(n);
  return i >= 0 ? process.argv[i + 1] ?? null : null;
};

async function main() {
  const rutaClaves = arg("--claves");
  const salida = arg("--salida");
  const tope = Number(arg("--tope") ?? 1.9);
  if (!rutaClaves || !salida) throw new Error("uso: --claves <claves.json> --salida <dir> [--tope 1.9]");
  const claves = JSON.parse(readFileSync(rutaClaves, "utf8")) as {
    claves: Array<{ origen: string; ref: { plan_id: string; session_id: string; project_id: string; dominio: string; tipo_salida: string; creado: string } }>;
  };
  const refs = claves.claves.filter((c) => c.origen === "real" && (c.ref.tipo_salida === "plan_nucleo" || c.ref.tipo_salida === "plan_mundo")).map((c) => c.ref);
  console.log(`planes a redactar: ${refs.length}`);
  mkdirSync(path.join(salida, "A"), { recursive: true });
  mkdirSync(path.join(salida, "B"), { recursive: true });

  const sb = createClient(process.env.SUPABASE_URL!, process.env.SUPABASE_SERVICE_ROLE_KEY!, { auth: { persistSession: false } });
  const client = new Anthropic({ apiKey: process.env.ANTHROPIC_API_KEY });
  const graph = cargarGrafo();
  const families = cargarFamilies();
  let gastado = 0;
  const costes: Array<Record<string, unknown>> = [];

  for (const ref of refs) {
    if (gastado + 0.15 > tope) {
      console.log(`TOPE: gastado $${gastado.toFixed(4)}; no se redacta ${ref.plan_id} (quedaria por encima de $${tope})`);
      break;
    }
    const { data: ses, error: e1 } = await sb.from("sessions").select("estado_recorrido, dominio").eq("id", ref.session_id).single();
    if (e1 || !ses) throw new Error(`sesion ${ref.session_id}: ${e1?.message}`);
    const { data: proy } = await sb.from("projects").select("*").eq("id", ref.project_id).single();
    const estado = ses.estado_recorrido as { recorrido: EstadoRecorrido; turnos?: Array<{ respuesta: string }> };
    const recorrido = estado.recorrido;
    const dominio = (ses.dominio as string | null) ?? "core";
    const idiomaSalida = recorrido.idioma ?? null;
    const idiomaPlan = idiomaDePlantilla(recorrido.idioma ?? "es", "es");
    // El contexto guardado con la sesion, pasado al formato de hoy (misma informacion, la pregunta de la IA y la
    // respuesta de la persona separadas y rotuladas, como lo arma textoContextoProyecto desde el 9 oct 2026). No se
    // rearma desde la memoria de hoy: traeria sesiones posteriores.
    if (recorrido.contextoProyecto) recorrido.contextoProyecto = contextoAlFormatoNuevo(recorrido.contextoProyecto);
    const contexto = contextoDeSesion(recorrido);

    // Sin sumar el estado vivo de HOY (defecto de la primera medicion, 9 oct 2026): el perfil guardado ya trae el estado
    // vivo de su momento, y el de hoy lo siembra la fase 2M del vuelo ("kits de huerto").
    let planAnterior = null;
    if (recorrido.esSeguimiento) {
      const { data: sesProy } = await sb.from("sessions").select("id").eq("project_id", ref.project_id);
      const ids = ((sesProy ?? []) as Array<{ id: string }>).map((x) => x.id);
      const { data: previos } = await sb
        .from("plans")
        .select("id, contenido_md, dominio, created_at")
        .in("session_id", ids)
        .lt("created_at", ref.creado)
        .order("created_at", { ascending: false });
      const previo = ((previos ?? []) as Array<{ id: string; contenido_md: string; dominio: string | null }>).find((p) => (p.dominio ?? "core") === dominio);
      if (previo) planAnterior = planAnteriorParaIA(previo.contenido_md, await obtenerTareasDePlan(sb, ref.project_id, previo.id));
    }
    const ciclo = recorrido.ciclo;
    const caminoElegido = ciclo?.tipo === "replantear" ? ciclo.caminos.find((c) => c.id === ciclo.caminoElegido) : undefined;
    const preparacion = prepararPlan(
      recorrido.ruta,
      graph,
      families,
      recorrido.textoOriginal,
      recorrido.perfilSesion,
      recorrido.prioridadDeclarada,
      recorrido.esSeguimiento,
      recorrido.estadoVivoPrevio,
      recorrido.dominiosDesbloqueados ? dominiosDelRecorrido(recorrido) : null,
      {
        excluir: recorrido.nodosCubiertosPrevios ?? [],
        planAnterior,
        replanteamiento:
          ciclo?.tipo === "replantear"
            ? {
                historia: ciclo.historia,
                se_conserva: ciclo.conserva.map((c) => c.texto),
                se_suelta: ciclo.suelta.map((c) => c.texto),
                camino_elegido: caminoElegido ? { titulo: caminoElegido.titulo, descripcion: caminoElegido.descripcion } : null,
              }
            : null,
      }
    );

    let acc: UsoAcumulado = usoVacio();
    const { rawTexto, acumulado } = await generarTextoPlan(client, preparacion, acc, () => undefined, () => undefined, idiomaSalida, { contexto });
    acc = acumulado;
    if (rawTexto === null) throw new Error(`el redactor no devolvio texto para ${ref.plan_id}`);
    const respuestas = [
      ...(estado.turnos ?? []).map((t) => t.respuesta),
      ...memoriaDe(proy?.memoria).hilo.map((e) => e.respuesta),
    ];
    const numeros = { ...((proy?.numeros_proyecto as Record<string, unknown>) ?? {}), ...(recorrido.numerosDetectadosSesion ?? {}) };
    const eventos: Array<Record<string, unknown>> = [];
    const a = finalizarPlan(rawTexto, preparacion, recorrido.ruta, families, recorrido.textoOriginal, (e) => eventos.push(e), numeros, idiomaPlan, respuestas);
    const costoA = costoAcumuladoUsd(acc);
    writeFileSync(path.join(salida, "A", `${ref.plan_id}.md`), a.markdown, "utf8");

    const v = await verificarPlan(
      client,
      {
        markdown: a.markdown,
        nodos: [...preparacion.materialPrincipal, ...preparacion.materialDeApoyo].map((m) => ({ id: m.id, etiqueta: m.etiqueta, pasos: m.pasos, entregable: m.entregable })),
        respuestas,
      },
      acc,
      { presupuestoUsd: 5, contexto, idiomaSalida }
    );
    acc = v.acumulado;
    const costoTotal = costoAcumuladoUsd(acc);
    writeFileSync(path.join(salida, "B", `${ref.plan_id}.md`), v.markdown, "utf8");
    gastado += costoTotal;
    costes.push({
      plan_id: ref.plan_id, dominio, tipo: ref.tipo_salida, costo_redactor: Number(costoA.toFixed(5)), costo_verificador: Number((costoTotal - costoA).toFixed(5)),
      verificador: { propuestas: v.correcciones.length, aplicadas: v.aplicadas, ignoradas: v.ignoradas, revision: v.revision, fallo: v.fallo },
      correcciones: v.correcciones, eventos_plan: eventos.map((e) => e.tipo), llamadas: acc.llamadas,
    });
    console.log(`${ref.plan_id} ${dominio}: redactor $${costoA.toFixed(4)} + verificador $${(costoTotal - costoA).toFixed(4)} | propuestas ${v.correcciones.length}, aplicadas ${v.aplicadas}, revision ${v.revision}${v.fallo ? `, FALLO ${v.fallo}` : ""} | acumulado $${gastado.toFixed(4)}`);
  }
  writeFileSync(path.join(salida, "costes.json"), JSON.stringify({ gastado_usd: Number(gastado.toFixed(5)), planes: costes }, null, 2), "utf8");
  console.log(`LISTO: ${costes.length} planes, gastado $${gastado.toFixed(4)}`);
}

main().catch((e) => {
  console.error(e);
  process.exit(1);
});
