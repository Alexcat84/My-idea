/**
 * MEDICION BARATA (decision del fundador, corrida final, 8 oct 2026): vuelve a redactar los planes del vuelo desde las
 * entrevistas GUARDADAS, sin repetir el vuelo y SIN GUARDAR NADA en la base, con los arreglos ya en el codigo:
 *   A = solo reglas (los prompts y la limpieza de moneda de hoy), con el mismo redactor de produccion;
 *   B = A + el verificador (lib/engine/verificadorPlan.ts) sobre ese mismo borrador.
 * Escribe A/<plan_id>.md, B/<plan_id>.md y costes.json en la carpeta de salida. Tope duro de gasto: --tope (USD).
 *
 * CAMINO DE PRODUCCION (decision del fundador, 9 oct 2026): las mismas funciones de la ruta del plan
 * (app/api/session/[id]/plan/route.ts), con lo guardado de cada sesion: perfilConEstadoVivoActual con el estado vivo
 * que tenia el proyecto en ese momento (leido de la foto del contexto al abrir la sesion; si otro plan del proyecto
 * nacio entre la apertura y este plan, se avisa: ese valor puede haber cambiado), prepararPlan, generarTextoPlan con el
 * contexto de la sesion, y finalizarPlan con las palabras de la persona hasta ese momento (el hilo filtrado por fecha).
 * Diferencias declaradas: el plan anterior de un seguimiento es el que existia ANTES de ese plan, con sus tareas en su
 * estado de hoy; el contexto guardado se pasa al formato de hoy (contextoAlFormatoNuevo), que es lo que produccion
 * arma hoy.
 *
 * Uso (desde web/, con el .env raiz): npx tsx scripts/corrida_final_redactar_planes.ts --claves <claves.json> --salida <dir> [--tope 1.9] [--sin-verificador]
 *   [--comprobador] el comprobador paso contra nodo (punto 3, 10 oct 2026) despues de finalizarPlan; A lleva el plan
 *                   comprobado y A_previo el de antes, para comparar.
 *   [--solo id1,id2] solo los planes cuyo id empieza por esos prefijos.
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
import { contextoDeSesion, estadoVivoDeLaFoto, memoriaDe } from "../lib/engine/memoria";
import { perfilConEstadoVivoActual } from "../lib/engine/perfilDelPlan";
import { numerosDelMomento } from "../lib/engine/numerosDelMomento";
import { planAnteriorParaIA, tituloDeNodoPara } from "../lib/engine/replanteamiento";
import { mensajeAlFormatoSinTexto } from "../lib/engine/seguimientoComposer";
import { idiomaDePlantilla } from "../lib/i18n/detectarIdioma";
import { verificarPlan } from "../lib/engine/verificadorPlan";
import { comprobarPasos } from "../lib/engine/comprobadorPasos";
import { SYSTEM_COMPROBADOR_PASOS } from "../lib/prompts";
import { obtenerTareasDePlan } from "../lib/db";
import type { TipoOferta } from "../lib/calculadora";
import { Presupuesto, TopeAlcanzado, reservaDeLlamada } from "../lib/presupuestoGuion";
import { SYSTEM_PLAN } from "../lib/prompts";

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
  const sinVerificador = process.argv.includes("--sin-verificador");
  const conComprobador = process.argv.includes("--comprobador");
  const solo = (arg("--solo") ?? "").split(",").map((x) => x.trim()).filter(Boolean);
  if (!rutaClaves || !salida) throw new Error("uso: --claves <claves.json> --salida <dir> [--tope 1.9] [--sin-verificador]");
  const claves = JSON.parse(readFileSync(rutaClaves, "utf8")) as {
    claves: Array<{ origen: string; ref: { plan_id: string; session_id: string; project_id: string; dominio: string; tipo_salida: string; creado: string } }>;
  };
  const refs = claves.claves.filter((c) => c.origen === "real" && (c.ref.tipo_salida === "plan_nucleo" || c.ref.tipo_salida === "plan_mundo")).map((c) => c.ref)
    .filter((r) => solo.length === 0 || solo.some((p) => r.plan_id.startsWith(p)));
  console.log(`planes a redactar: ${refs.length}`);
  mkdirSync(path.join(salida, "A"), { recursive: true });
  if (conComprobador) mkdirSync(path.join(salida, "A_previo"), { recursive: true });
  mkdirSync(path.join(salida, "B"), { recursive: true });

  const sb = createClient(process.env.SUPABASE_URL!, process.env.SUPABASE_SERVICE_ROLE_KEY!, { auth: { persistSession: false } });
  const client = new Anthropic({ apiKey: process.env.ANTHROPIC_API_KEY });
  const graph = cargarGrafo();
  const families = cargarFamilies();
  let gastado = 0;
  // Topes (decision del fundador, 10 oct 2026): cada plan reserva su peor caso ANTES de redactarse (lib/presupuestoGuion.ts).
  const presupuesto = new Presupuesto(tope);
  const costes: Array<Record<string, unknown>> = [];
  const avisos: string[] = [];

  for (const ref of refs) {
    const { data: ses, error: e1 } = await sb.from("sessions").select("estado_recorrido, dominio, created_at").eq("id", ref.session_id).single();
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
    // El estado vivo que leeria produccion en el momento del plan: el de la foto al abrir la sesion, si ningun otro plan
    // del proyecto nacio entre la apertura y este plan (si nacio, se avisa).
    const estadoVivoDelMomento = estadoVivoDeLaFoto(recorrido.contextoProyecto);
    const { data: entre } = await sb
      .from("plans")
      .select("id, created_at, session_id")
      .in("session_id", (((await sb.from("sessions").select("id").eq("project_id", ref.project_id)).data ?? []) as Array<{ id: string }>).map((x) => x.id))
      .gt("created_at", ses.created_at as string)
      .lt("created_at", ref.creado);
    if ((entre ?? []).length > 0) {
      const aviso = `${ref.plan_id}: ${(entre ?? []).length} plan(es) del proyecto nacieron entre la apertura de la sesion y este plan; el estado vivo del momento puede no ser el de la foto`;
      avisos.push(aviso);
      console.log(`AVISO ${aviso}`);
    }
    recorrido.perfilSesion = perfilConEstadoVivoActual(recorrido.perfilSesion, {
      dominio,
      esSeguimiento: recorrido.esSeguimiento,
      estadoVivoActual: estadoVivoDelMomento,
    });
    if (recorrido.contextoProyecto) recorrido.contextoProyecto = contextoAlFormatoNuevo(recorrido.contextoProyecto);
    const contexto = contextoDeSesion(recorrido);

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
      if (previo) {
        const tareas = await obtenerTareasDePlan(sb, ref.project_id, previo.id);
        planAnterior = planAnteriorParaIA(previo.contenido_md, tareas, tituloDeNodoPara(graph));
        // El mensaje del seguimiento guardado, al formato de hoy (decision del fundador, 10 oct 2026): sin el texto de
        // ninguna tarea, como lo compone hoy la app (lib/engine/seguimientoComposer.ts).
        if (recorrido.textoOriginal?.startsWith("Desde el último plan")) {
          recorrido.textoOriginal = mensajeAlFormatoSinTexto(recorrido.textoOriginal, tareas, tituloDeNodoPara(graph));
        }
      }
    }
    const ciclo = recorrido.ciclo;
    const caminoElegido = ciclo?.tipo === "replantear" ? ciclo.caminos.find((c) => c.id === ciclo.caminoElegido) : undefined;
    // Las cifras de la persona EN EL MOMENTO del plan, como las tenia la ruta del plan entonces (decision del fundador,
    // 10 oct 2026): las del proyecto anteriores al plan y las de la sesion. Antes se usaban las de hoy (medicion final:
    // las cifras GIGO del vuelo, guardadas despues, llegaron a planes que nacieron antes).
    const momento = numerosDelMomento(proy?.numeros_proyecto, recorrido.numerosDetectadosSesion, ref.creado);
    const numeros = momento.numeros;
    if (momento.fuera.length || momento.sinFecha.length) {
      const aviso = `${ref.plan_id}: cifras del proyecto posteriores al plan (fuera): ${momento.fuera.join(", ") || "ninguna"}; sin fecha: ${momento.sinFecha.join(", ") || "ninguna"}`;
      avisos.push(aviso);
      console.log(`AVISO ${aviso}`);
    }
    // Las palabras de la persona HASTA este plan (produccion las lee de la memoria en ese momento): la moneda y, numeradas,
    // las citas del plan (REDACTOR_CON_RESPALDO punto 3).
    const respuestas = [
      ...(estado.turnos ?? []).map((t) => t.respuesta),
      ...memoriaDe(proy?.memoria).hilo.filter((e) => !e.en || Date.parse(e.en) <= Date.parse(ref.creado)).map((e) => e.respuesta),
    ];
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
        numeros,
        respuestas,
        tipoOferta: (recorrido.tipoOfertaSesion ?? (proy?.tipo_oferta as string | null) ?? null) as TipoOferta,
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

    // El peor caso: la entrada (payload, contexto y el prompt) y dos intentos de salida (5.000 + 10.000 tokens).
    let reserva: number;
    try {
      reserva = presupuesto.reservar(reservaDeLlamada(JSON.stringify(preparacion.payload).length + (contexto?.length ?? 0) + SYSTEM_PLAN.length, 15000, [2, 10]));
    } catch (e) {
      if (!(e instanceof TopeAlcanzado)) throw e;
      console.log(`TOPE: ${e.message}; no se redacta ${ref.plan_id}`);
      break;
    }
    let acc: UsoAcumulado = usoVacio();
    const { rawTexto, acumulado } = await generarTextoPlan(client, preparacion, acc, () => undefined, () => undefined, idiomaSalida, { contexto });
    acc = acumulado;
    if (rawTexto === null) throw new Error(`el redactor no devolvio texto para ${ref.plan_id}`);
    const eventos: Array<Record<string, unknown>> = [];
    const a = finalizarPlan(rawTexto, preparacion, recorrido.ruta, families, recorrido.textoOriginal, (e) => eventos.push(e), numeros, idiomaPlan, respuestas);
    presupuesto.cerrar(reserva, costoAcumuladoUsd(acc));
    let comprobador: Record<string, unknown> | null = null;
    if (conComprobador) {
      writeFileSync(path.join(salida, "A_previo", `${ref.plan_id}.md`), a.markdown, "utf8");
      const nodos = [...preparacion.materialPrincipal, ...preparacion.materialDeApoyo];
      // La entrada del comprobador, para poder repetirlo sin volver a redactar.
      writeFileSync(path.join(salida, "A_previo", `${ref.plan_id}.json`), JSON.stringify({ pasosCitados: a.pasosCitados, nodos }), "utf8");
      // El peor caso del comprobador: los temas, el plan y el prompt de entrada; dos intentos de salida (2.000 + 4.000).
      let reservaC: number;
      try {
        reservaC = presupuesto.reservar(reservaDeLlamada(JSON.stringify(nodos).length + a.markdown.length + SYSTEM_COMPROBADOR_PASOS.length, 6000, [2, 10]));
      } catch (e) {
        if (!(e instanceof TopeAlcanzado)) throw e;
        console.log(`TOPE: ${e.message}; ${ref.plan_id} sale sin comprobar`);
        reservaC = -1;
      }
      if (reservaC >= 0) {
        const antes = costoAcumuladoUsd(acc);
        const c = await comprobarPasos(client, { markdown: a.markdown, pasosCitados: a.pasosCitados, nodos }, acc, { presupuestoUsd: 5, idiomaSalida });
        acc = c.acumulado;
        presupuesto.cerrar(reservaC, costoAcumuladoUsd(acc) - antes);
        a.markdown = c.markdown;
        comprobador = { pasos_con_tema: a.pasosCitados.length, juzgados: c.juzgados, quitados: c.quitados, ignorados: c.ignorados, revision: c.revision, fallo: c.fallo, propuestas: c.propuestas, costo: Number((costoAcumuladoUsd(acc) - antes).toFixed(5)) };
        console.log(`  comprobador: ${c.juzgados} pasos juzgados, quitados ${c.quitados.join(", ") || "ninguno"}, ignorados ${c.ignorados}${c.revision ? ", REVISION" : ""}${c.fallo ? `, FALLO ${c.fallo}` : ""}`);
      }
    }
    const costoA = costoAcumuladoUsd(acc);
    writeFileSync(path.join(salida, "A", `${ref.plan_id}.md`), a.markdown, "utf8");

    if (sinVerificador) {
      gastado += costoA;
      costes.push({ plan_id: ref.plan_id, dominio, tipo: ref.tipo_salida, costo_redactor: Number(costoA.toFixed(5)), eventos_plan: eventos.map((e) => e.tipo), llamadas: acc.llamadas, estado_vivo_del_momento: estadoVivoDelMomento !== null, ...(comprobador ? { comprobador } : {}) });
      console.log(`${ref.plan_id} ${dominio}: redactor $${costoA.toFixed(4)} | acumulado $${gastado.toFixed(4)}`);
      continue;
    }
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
  writeFileSync(path.join(salida, "costes.json"), JSON.stringify({ gastado_usd: Number(gastado.toFixed(5)), avisos, planes: costes }, null, 2), "utf8");
  console.log(`LISTO: ${costes.length} planes, gastado $${gastado.toFixed(4)}`);
}

main().catch((e) => {
  console.error(e);
  process.exit(1);
});
