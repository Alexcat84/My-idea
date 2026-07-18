// Fase 4.5 (PREVIEW_MUNDOS_PLAN §5.5) - vuelo del preview de los mundos.
// HTTP real contra `next dev` en :3000 + verificacion service-role.
//
//   FELIZ:  plan core (sembrado) -> start del mundo = preview GRATIS (fila
//           con preview_at, creditos_pagados 0, bitacora preview_iniciado)
//           -> entrevista real (turnos Sonnet) -> diagnostico (Sonnet, ley de
//           calidad) -> frontera §3 (violacionesFronteraPreview = []) ->
//           resumen persistido + sesion fase cerrada SIN closed_at ->
//           COMPRA: plan por SSE DESDE la misma sesion (sin re-entrevistar)
//           -> plan del dominio + checklist derivado + plan_pagado_at +
//           bitacora preview_a_compra + sesion cerrada.
//   REGRESIONES (deterministas): candado pre-plan-core (409); un-preview-por-
//           mundo (409 tras el diagnostico).
//   ESPEJO (incompatible): NO se fuerza en vivo (el juicio del interprete no
//           es deterministico); su mecanica esta cubierta por los tests de
//           recorrido (mundo_incompatible), apiSesion (cierre estructurado,
//           creditos_devueltos null sin ledger) y CierreHonesto.test (cero
//           claim de dinero). Aqui se declara, no se finge.
//
// Uso: con `pnpm dev` en :3000,  npx tsx scripts/vuelo_preview.ts
// Costo real: entrevista de mundo + diagnostico + plan (~$0.15-0.25).
import { createClient } from "@supabase/supabase-js";
import { autenticarComoDevUser, cargarEnvRaiz, consumirSSE, BASE_URL, postJson } from "./_shared/http";
import { violacionesFronteraPreview } from "../lib/engine/previewMundos";

cargarEnvRaiz();
const admin = createClient(process.env.NEXT_PUBLIC_SUPABASE_URL!, process.env.SUPABASE_SERVICE_ROLE_KEY!);

const MUNDO = "quality"; // Calidad y Confianza: encaja con el caso kits (clientes reales)

let fallos = 0;

/** ETAPA 2: los vuelos ejercen los cobros REALES; el dev user necesita saldo. */
async function asegurarSaldoDev(userId: string) {
  await admin.rpc("otorgar_creditos", {
    p_user_id: userId, p_monto: 100, p_origen: "cortesia",
    p_idempotency_key: `vuelo-topup:${Date.now()}`, p_pack: null,
  });
}

function check(nombre: string, cond: boolean, extra?: unknown) {
  console.log(`${cond ? "OK  " : "FALLO"}: ${nombre}${cond ? "" : `  -> ${JSON.stringify(extra)}`}`);
  if (!cond) fallos++;
}

async function unlockDe(pid: string) {
  const { data } = await admin
    .from("project_unlocks")
    .select("*")
    .eq("project_id", pid)
    .eq("dominio", MUNDO)
    .limit(1);
  return (data?.[0] ?? null) as {
    creditos_pagados: number;
    preview_at: string | null;
    preview_session_id: string | null;
    resumen_md: string | null;
    resumen_at: string | null;
    plan_pagado_at: string | null;
  } | null;
}

async function eventosBitacora(pid: string) {
  const { data } = await admin
    .from("project_bitacora")
    .select("tipo, payload")
    .eq("project_id", pid)
    .order("created_at", { ascending: true });
  return (data ?? []) as Array<{ tipo: string; payload: Record<string, unknown> }>;
}

async function sembrarProyectoConPlanCore(userId: string) {
  const { data: p, error } = await admin
    .from("projects")
    .insert({
      user_id: userId,
      entrada_original:
        "Quiero vender kits de huerto urbano prearmados para balcones pequeños; ya vendí tres a amigos y me los pagaron.",
      titulo: "Kits de huerto urbano (vuelo preview)",
      fase_actual: "validacion",
      status: "active",
      tipo_oferta: "producto_fisico",
      unidad_venta: "kit",
      estado_vivo:
        "Vende kits de huerto urbano prearmados para balcones pequeños. Tres ventas reales a conocidos a $350 " +
        "(costo $180). Su reto actual: validar con desconocidos y lograr que el cliente vuelva y recomiende. " +
        "Aún no mide recompra ni quejas; la confianza del cliente es intuición, no registro.",
    })
    .select("id")
    .single();
  if (error) throw error;
  const pid = (p as { id: string }).id;
  const { data: s, error: e2 } = await admin
    .from("sessions")
    .insert({ project_id: pid, user_id: userId, session_position: 1, tipo: "inicial", mensaje_entrada: "siembra vuelo", dominio: "core", closed_at: new Date().toISOString() })
    .select("id")
    .single();
  if (e2) throw e2;
  const { error: e3 } = await admin.from("plans").insert({
    session_id: (s as { id: string }).id,
    user_id: userId,
    etiqueta: "completo",
    dominio: "core",
    contenido_md: "# Plan core sembrado\n## Etapa 1: valida con desconocidos\nMaterial del vuelo.",
    conceptos_usados: 5,
    familias_cubiertas: ["general"],
  });
  if (e3) throw e3;
  return pid;
}

async function main() {
  // 0) La 028 tiene que estar aplicada: chequeo ruidoso antes de gastar API.
  const { error: err028 } = await admin.from("project_unlocks").select("preview_at").limit(1);
  if (err028) {
    console.error("FALTA LA MIGRACION 028: aplica my_idea_028_preview_mundos.sql y reintenta.", err028.message);
    process.exit(2);
  }

  const cookie = await autenticarComoDevUser();
  const { data: lista } = await admin.auth.admin.listUsers();
  const dev = lista.users.find((u) => u.email === "dev@my-idea.local");
  if (!dev) throw new Error("no encuentro el dev user");
  await asegurarSaldoDev(dev.id);

  // ── REGRESION: candado de secuencia (sin plan core, nada se abre) ─────────
  const { data: pv } = await admin
    .from("projects")
    .insert({ user_id: dev.id, entrada_original: "idea sin plan (vuelo preview)", fase_actual: "ideacion", status: "active" })
    .select("id")
    .single();
  const pidVirgen = (pv as { id: string }).id;
  const rCandado = await fetch(`${BASE_URL}/api/project/${pidVirgen}/world/${MUNDO}/start`, {
    method: "POST",
    headers: { Cookie: cookie },
  });
  check("candado: sin plan core, start responde 409", rCandado.status === 409, rCandado.status);
  check("candado: no se creo ninguna fila de unlock", (await admin.from("project_unlocks").select("id").eq("project_id", pidVirgen)).data?.length === 0);

  // ── FELIZ ────────────────────────────────────────────────────────────────
  const pid = await sembrarProyectoConPlanCore(dev.id);
  console.log(`\nproyecto sembrado: ${pid}`);

  // 1) start = preview gratis
  const inicio = await postJson(cookie, `/api/project/${pid}/world/${MUNDO}/start`, {});
  check("start: devuelve la primera pregunta del mundo", inicio.tipo === "pregunta" && typeof inicio.pregunta === "string", inicio.tipo);
  const sessionId = inicio.session_id as string;
  let u = await unlockDe(pid);
  check("start: la fila nace GRATIS (creditos_pagados 0) con preview_at", u?.creditos_pagados === 0 && u?.preview_at != null, u);
  check("start: preview_session_id amarrado a la sesion", u?.preview_session_id === sessionId, u?.preview_session_id);

  // 2) entrevista real (respuestas del caso kits; cierres explicitos al final)
  const RESPUESTAS = [
    "Mis tres clientes me compraron una vez y no he vuelto a saber de ellos; no registro quejas ni se si el kit les funciono.",
    "No tengo ninguna forma de medir si estan contentos: ni encuesta, ni mensaje de seguimiento, nada.",
    "Me interesa que el que compre vuelva y me recomiende, porque no tengo presupuesto de publicidad.",
    "Con eso te conte lo importante, quiero ver que encontraste.",
    "Suficiente, muestrame el diagnostico.",
    "Ya no tengo mas que agregar.",
  ];
  let listo = false;
  for (const r of RESPUESTAS) {
    const t = await postJson(cookie, `/api/session/${sessionId}/turn`, { respuesta: r });
    if (t.tipo === "listo_para_plan") {
      listo = true;
      break;
    }
    if (t.tipo === "salio") {
      console.log("  (el interprete cerro el mundo durante el preview; espejo en vivo)");
      break;
    }
  }
  console.log(`  entrevista: ${listo ? "llego a listo_para_plan" : "termino por turnos"} `);

  // 3) diagnostico (Sonnet) + frontera §3
  const d = await postJson(cookie, `/api/project/${pid}/world/${MUNDO}/diagnostico`, { session_id: sessionId });
  const resumen = d.resumen as string;
  check("diagnostico: hay resumen", typeof resumen === "string" && resumen.length > 100, (resumen ?? "").length);
  check("diagnostico: estructura del prompt (Lo que encontré / estructuraría / Veredicto)",
    /lo que encontr/i.test(resumen) && /estructurar/i.test(resumen) && /veredicto/i.test(resumen), resumen?.slice(0, 120));
  const violaciones = violacionesFronteraPreview(resumen);
  check("FRONTERA §3: cero pasos accionables en el resumen", violaciones.length === 0, violaciones);
  u = await unlockDe(pid);
  check("diagnostico: resumen persistido en la fila", u?.resumen_md === resumen && u?.resumen_at != null);
  const { data: ses } = await admin.from("sessions").select("closed_at, estado_recorrido").eq("id", sessionId).single();
  const sesTyped = ses as { closed_at: string | null; estado_recorrido: { recorrido: { fase: string } } | null };
  check("diagnostico: sesion fase 'cerrada' SIN closed_at (lista para la compra)",
    sesTyped.closed_at === null && sesTyped.estado_recorrido?.recorrido.fase === "cerrada", sesTyped.closed_at);

  // 4) REGRESION un-preview-por-mundo: repetir start es 409 en palabras de persona
  const rRepite = await fetch(`${BASE_URL}/api/project/${pid}/world/${MUNDO}/start`, { method: "POST", headers: { Cookie: cookie } });
  const bodyRepite = (await rRepite.json()) as { error?: string };
  check("un-preview: repetir start responde 409", rRepite.status === 409, rRepite.status);
  check("un-preview: el mensaje habla en palabras de persona", (bodyRepite.error ?? "").includes("ya está listo"), bodyRepite.error);

  // 5) COMPRA: el plan por SSE desde LA MISMA sesion (sin re-entrevistar)
  const { count: sesionesAntes } = await admin.from("sessions").select("id", { count: "exact", head: true }).eq("project_id", pid);
  const resPlan = await fetch(`${BASE_URL}/api/session/${sessionId}/plan`, {
    method: "POST",
    headers: { "Content-Type": "application/json", Cookie: cookie },
    body: JSON.stringify({}),
  });
  check("compra: la ruta del plan acepta la sesion del preview", resPlan.ok, resPlan.status);
  let planMd = "";
  await consumirSSE(resPlan, ({ evento, data }) => {
    if (evento === "done") planMd = (data as { markdown: string }).markdown;
  });
  check("compra: el plan del mundo llego por SSE", planMd.length > 200, planMd.length);
  const { count: sesionesDespues } = await admin.from("sessions").select("id", { count: "exact", head: true }).eq("project_id", pid);
  check("compra: SIN re-entrevistar (cero sesiones nuevas)", sesionesAntes === sesionesDespues, { antes: sesionesAntes, despues: sesionesDespues });

  const { data: planes } = await admin.from("plans").select("dominio, etiqueta").eq("session_id", sessionId);
  check("compra: el plan quedo con el dominio del mundo", (planes ?? []).some((p) => p.dominio === MUNDO), planes);
  const { count: checklistMundo } = await admin
    .from("checklist_items")
    .select("id", { count: "exact", head: true })
    .eq("project_id", pid)
    .eq("dominio", MUNDO);
  check("paridad 4.1-4.3: checklist del mundo derivado", (checklistMundo ?? 0) > 0, checklistMundo);
  u = await unlockDe(pid);
  check("compra: plan_pagado_at sellado a la entrega (ancla ETAPA 2)", u?.plan_pagado_at != null);
  const { data: sesFin } = await admin.from("sessions").select("closed_at").eq("id", sessionId).single();
  check("compra: la sesion del preview quedo cerrada de verdad", (sesFin as { closed_at: string | null }).closed_at != null);

  // 6) Telemetria §6 en bitacora
  const eventos = await eventosBitacora(pid);
  const tipos = eventos.map((e) => e.tipo);
  check("telemetria: preview_iniciado -> preview_completado -> preview_a_compra",
    tipos.includes("preview_iniciado") && tipos.includes("preview_completado") && tipos.includes("preview_a_compra"), tipos);

  // Limpieza
  await admin.from("projects").delete().in("id", [pid, pidVirgen]);

  console.log(`\n${fallos === 0 ? "VUELO DEL PREVIEW: TODO VERDE" : `VUELO CON ${fallos} FALLO(S)`}`);
  console.log("(espejo incompatible: cubierto a nivel de mecanismo por los tests de recorrido/apiSesion/CierreHonesto)");
  if (fallos > 0) process.exit(1);
}

main().catch((e) => {
  console.error(e);
  process.exit(1);
});
