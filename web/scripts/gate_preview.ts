// Fase 4.5 - gate del preview de los mundos: la fila de potenciadores y la
// seccion del mundo EN SUS ESTADOS. No hay frame de canon (la vara del preview
// no existe: se pide a Design en el proximo lote, patron ciclo-de-caja); estas
// capturas documentan la implementacion como referencia. Dos viewports.
//
//   preview_bloqueado_*   fila con organizador y SIN plan core ("Se abre con tu plan")
//   preview_fila_*        fila con plan core: quality "Listo para tu plan" +
//                         los demas "Exploralo gratis"
//   preview_escaparate_*  seccion del mundo en Manos: el diagnostico + CTA compra
//
// Uso: con `pnpm dev` en :3000,  npx tsx scripts/gate_preview.ts
import { chromium, type Page } from "playwright";
import { createClient } from "@supabase/supabase-js";
import { mkdirSync } from "node:fs";
import path from "node:path";
import { autenticarComoDevUser, BASE_URL, cargarEnvRaiz, ROOT } from "./_shared/http";

cargarEnvRaiz();
const admin = createClient(process.env.NEXT_PUBLIC_SUPABASE_URL!, process.env.SUPABASE_SERVICE_ROLE_KEY!);
const OUT = path.join(ROOT, "web", "examples", "gate-canon");
const VP_ESCRITORIO = { width: 1240, height: 900 };
const VP_MOVIL = { width: 380, height: 844 };

// Un diagnostico sintetico LIMPIO segun la frontera §3 (solo para la captura;
// el vuelo ya probo el real). Tono espejo, cero pasos accionables.
const RESUMEN_DEMO = [
  "## Lo que encontré en tu proyecto",
  "- Tus tres primeras ventas fueron a conocidos, y hoy nadie te dice si el kit funcionó ni si volverían a comprar.",
  "- No tienes registro de quejas ni de recompra: la confianza de tus clientes es intuición, no dato.",
  "## Lo que un plan te estructuraría",
  "Un sistema simple para que el cliente confíe, vuelva y te recomiende: la medición mínima de recompra, un canal de quejas que no te dé miedo abrir, y la señal de recomendación que te libera de perseguir clientes uno por uno.",
  "## Veredicto",
  "Calidad y Confianza encaja con tu momento: ya tienes clientes reales y cero medición de su confianza. Es el hueco exacto entre tus tres ventas y las siguientes treinta.",
].join("\n\n");

async function sembrarProyecto(userId: string, titulo: string, conPlanCore: boolean) {
  const { data: p, error } = await admin
    .from("projects")
    .insert({
      user_id: userId,
      entrada_original: titulo,
      titulo,
      fase_actual: conPlanCore ? "validacion" : "ideacion",
      status: "active",
      tipo_oferta: "producto_fisico",
      unidad_venta: "kit",
      estado_vivo: "Kits de huerto urbano prearmados; tres ventas reales a conocidos.",
    })
    .select("id")
    .single();
  if (error) throw error;
  const pid = (p as { id: string }).id;
  const { data: s, error: e2 } = await admin
    .from("sessions")
    .insert({
      project_id: pid,
      user_id: userId,
      session_position: 1,
      tipo: conPlanCore ? "inicial" : "gratuito",
      mensaje_entrada: "siembra gate preview",
      dominio: "core",
      closed_at: new Date().toISOString(),
    })
    .select("id")
    .single();
  if (e2) throw e2;
  const sid = (s as { id: string }).id;
  const { error: e3 } = await admin.from("plans").insert({
    session_id: sid,
    user_id: userId,
    etiqueta: conPlanCore ? "completo" : "organizador",
    dominio: "core",
    contenido_md: conPlanCore
      ? "# Kits de huerto urbano: de tus tres amigos a desconocidos\n## Etapa 1: valida con desconocidos\nMaterial del gate.\n**Esta semana:** habla con un desconocido."
      : "# Esto entendí de tu idea\n- Vendes kits de huerto urbano.\n- Lo que asumes: que un desconocido pagaría.",
    conceptos_usados: 5,
    familias_cubiertas: ["general"],
  });
  if (e3) throw e3;
  return { pid, sid };
}

async function capturar(page: Page, archivo: string) {
  await page.waitForTimeout(1100);
  await page.screenshot({ path: path.join(OUT, archivo), fullPage: true });
  console.log(`  ${archivo}`);
}

async function capturarDosViewports(app: Page, url: string, espera: string, base: string) {
  await app.setViewportSize(VP_ESCRITORIO);
  await app.goto(url);
  await app.waitForSelector(`text=${espera}`, { timeout: 30000 });
  await capturar(app, `${base}_app.png`);
  await app.setViewportSize(VP_MOVIL);
  await app.waitForTimeout(700);
  await capturar(app, `${base}_app_380.png`);
  await app.setViewportSize(VP_ESCRITORIO);
}

async function main() {
  mkdirSync(OUT, { recursive: true });
  const cookie = await autenticarComoDevUser();
  const { data: lista } = await admin.auth.admin.listUsers();
  const dev = lista.users.find((u) => u.email === "dev@my-idea.local");
  if (!dev) throw new Error("no encuentro el dev user");

  // [bloqueado]: organizador sin plan core.
  const bloqueado = await sembrarProyecto(dev.id, "Kits de huerto (gate preview, sin plan)", false);
  // [abierto]+[diagnostico listo]: plan core + quality con resumen sembrado.
  const listo = await sembrarProyecto(dev.id, "Kits de huerto (gate preview)", true);
  const { error: eU } = await admin.from("project_unlocks").insert({
    project_id: listo.pid,
    dominio: "quality",
    creditos_pagados: 0,
    preview_at: new Date().toISOString(),
    preview_session_id: listo.sid,
    resumen_md: RESUMEN_DEMO,
    resumen_at: new Date().toISOString(),
  });
  if (eU) throw eU;

  const browser = await chromium.launch();
  const context = await browser.newContext({ viewport: VP_ESCRITORIO, deviceScaleFactor: 1 });
  const url = new URL(BASE_URL);
  await context.addCookies(
    cookie.split("; ").map((par) => {
      const i = par.indexOf("=");
      return { name: par.slice(0, i), value: par.slice(i + 1), domain: url.hostname, path: "/" };
    })
  );
  const app = await context.newPage();

  try {
    console.log("[bloqueado] fila con 'Se abre con tu plan':");
    await capturarDosViewports(app, `${BASE_URL}/idea/${bloqueado.pid}`, "Se abre con tu plan", "preview_bloqueado");

    console.log("[abierto + diagnostico listo] la fila de potenciadores:");
    await capturarDosViewports(app, `${BASE_URL}/idea/${listo.pid}`, "Listo para tu plan", "preview_fila");

    console.log("[escaparate] la seccion del mundo en Manos:");
    await capturarDosViewports(
      app,
      `${BASE_URL}/idea/${listo.pid}?vista=manos`,
      "Listo para generar tu plan",
      "preview_escaparate"
    );
  } finally {
    await browser.close();
    await admin.from("projects").delete().in("id", [bloqueado.pid, listo.pid]);
  }
  console.log("\nGATE DEL PREVIEW: los estados capturados en dos viewports (sin vara de canon: referencia para Design).");
}

main().catch((e) => {
  console.error(e);
  process.exit(1);
});
