// Catalogo congruente - gate de la beta con cuentas: la COMPUERTA de Tus Numeros
// (ahora INCLUIDA), el CHIP de saldo, los PRECIOS VIVOS del §4 y el CENTRO de
// creditos. Dos viewports. Documenta la implementacion (patron ciclo-de-caja).
//
//   beta_compuerta_*   /idea/[id]/numeros SIN activacion: "Activar mis numeros · incluido con tu plan"
//   beta_fila_*        la fila de potenciadores con precios vivos ("su plan: 5 creditos")
//   beta_ideas_chip_*  /ideas con el chip de saldo del dev user
//   beta_creditos_*    /creditos: 4 packs "alcanza para" + "lo que cuesta cada cosa"
//   espacios_core_manos_*  core Manos con el CAMBIADOR de tabs (Tu viaje | Calidad | +)
//   espacios_hub_mundo_*   el HUB de un mundo (sin explorar, precio al frente)
//
// Uso: con `pnpm dev` en :3000,  npx tsx scripts/gate_beta.ts
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

async function capturarDos(app: Page, url: string, espera: string, base: string) {
  await app.setViewportSize(VP_ESCRITORIO);
  await app.goto(url);
  await app.waitForSelector(`text=${espera}`, { timeout: 30000 });
  await app.waitForTimeout(1000);
  await app.screenshot({ path: path.join(OUT, `${base}_app.png`), fullPage: true });
  console.log(`  ${base}_app.png`);
  await app.setViewportSize(VP_MOVIL);
  await app.waitForTimeout(700);
  await app.screenshot({ path: path.join(OUT, `${base}_app_380.png`), fullPage: true });
  console.log(`  ${base}_app_380.png`);
  await app.setViewportSize(VP_ESCRITORIO);
}

async function main() {
  mkdirSync(OUT, { recursive: true });
  const cookie = await autenticarComoDevUser();
  const { data: lista } = await admin.auth.admin.listUsers();
  const dev = lista.users.find((u) => u.email === "dev@my-idea.local");
  if (!dev) throw new Error("no encuentro el dev user");

  // Compuerta: proyecto con plan core y SIN activacion de Tus Numeros.
  const { data: p, error } = await admin
    .from("projects")
    .insert({
      user_id: dev.id,
      entrada_original: "Velas de soya (gate beta)",
      titulo: "Velas de soya (gate beta)",
      fase_actual: "planificacion",
      status: "active",
      tipo_oferta: "producto_fisico",
      unidad_venta: "vela",
    })
    .select("id")
    .single();
  if (error) throw error;
  const pid = (p as { id: string }).id;
  const { data: s } = await admin
    .from("sessions")
    .insert({ project_id: pid, user_id: dev.id, session_position: 1, tipo: "inicial", mensaje_entrada: "gate", dominio: "core", closed_at: new Date().toISOString() })
    .select("id")
    .single();
  const { data: planCore } = await admin
    .from("plans")
    .insert({
      session_id: (s as { id: string }).id,
      user_id: dev.id,
      etiqueta: "completo",
      dominio: "core",
      contenido_md: "# Velas de soya: de tus conocidos al mercado real\n## Etapa 1: valida\nMaterial del gate.\n**Esta semana:** habla con un desconocido.",
      conceptos_usados: 5,
      familias_cubiertas: ["general"],
    })
    .select("id")
    .single();
  const planId = (planCore as { id: string }).id;
  // Checklist core (para que Manos a la Obra pinte de verdad, no el vacío).
  await admin.from("checklist_items").insert([
    { project_id: pid, plan_id: planId, dominio: "core", etapa: 1, orden: 1, texto: "Habla con un desconocido de tu producto.", destacado: true },
    { project_id: pid, plan_id: planId, dominio: "core", etapa: 1, orden: 2, texto: "Anota qué precio te aceptan sin dudar." },
    { project_id: pid, plan_id: planId, dominio: "core", etapa: 2, orden: 1, texto: "Prepara diez velas para la próxima feria." },
  ]);
  // Campaña "Espacios": un mundo ACTIVO (sin explorar aún) dispara el cambiador
  // de tabs y su hub. quality es válido en el CHECK de project_unlocks (016).
  await admin.from("project_unlocks").insert({ project_id: pid, dominio: "quality" });

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
    console.log("[compuerta de Tus Numeros: incluida con tu plan]");
    await capturarDos(app, `${BASE_URL}/idea/${pid}/numeros`, "Tus cifras reales", "beta_compuerta");

    console.log("[fila de potenciadores con precios vivos]");
    await capturarDos(app, `${BASE_URL}/idea/${pid}`, "Su plan:", "beta_fila");

    console.log("[/ideas con el chip de saldo]");
    await capturarDos(app, `${BASE_URL}/ideas`, "créditos", "beta_ideas_chip");

    console.log("[centro de creditos: packs 'alcanza para' + lo que cuesta cada cosa]");
    await capturarDos(app, `${BASE_URL}/creditos`, "Lo que cuesta cada cosa", "beta_creditos");

    console.log("[Espacios: core Manos con el cambiador de tabs (Tu viaje | Calidad | +)]");
    await capturarDos(app, `${BASE_URL}/idea/${pid}?vista=manos`, "Tu viaje", "espacios_core_manos");

    console.log("[Espacios: hub del mundo (sin explorar, precio al frente)]");
    await capturarDos(app, `${BASE_URL}/idea/${pid}?vista=mundo&dominio=quality`, "Explorar este mundo", "espacios_hub_mundo");
  } finally {
    await browser.close();
    await admin.from("projects").delete().eq("id", pid);
  }
  console.log("\nGATE DE LA BETA: compuerta + precios vivos + chip + centro de creditos + cambiador/hub de Espacios capturados (2 viewports).");
}

main().catch((e) => {
  console.error(e);
  process.exit(1);
});
