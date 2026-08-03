// Catalogo congruente - gate de la beta con cuentas: la COMPUERTA de Tus Numeros
// (ahora INCLUIDA), el CHIP de saldo, los PRECIOS VIVOS del §4 y el CENTRO de
// creditos. Dos viewports. Documenta la implementacion (patron ciclo-de-caja).
//
//   beta_compuerta_*   /idea/[id]/numeros SIN activacion: "Activar mis numeros · incluido con tu plan"
//   beta_fila_*        la fila de potenciadores con precios vivos ("su plan: 5 creditos")
//   beta_ideas_chip_*  /ideas con el chip de saldo del dev user
//   beta_creditos_*    /creditos: 4 packs "alcanza para" + "lo que cuesta cada cosa"
//   espacios_core_{manos,plan,avance}_*  las 3 CARAS del core (cambiador + segmentado)
//   espacios_hub_sinexplorar_*           un mundo sin explorar (precio al frente)
//   espacios_hub_{manos,plan,avance}_*   las 3 CARAS del hub de un mundo con plan
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
  // Campaña "Espacios": dos mundos activos (dominios válidos en el CHECK de la
  // 016) para el cambiador de tabs. `health_safety` sin explorar (su hub muestra
  // "Explorar este mundo"); `quality` con plan+checklist → su hub muestra las
  // TRES caras (Plan · Manos a la obra · Tu avance).
  await admin.from("project_unlocks").insert([
    { project_id: pid, dominio: "quality" },
    { project_id: pid, dominio: "health_safety" },
  ]);
  const { data: sMundo } = await admin
    .from("sessions")
    .insert({ project_id: pid, user_id: dev.id, session_position: 2, tipo: "inicial", mensaje_entrada: "gate mundo", dominio: "quality", closed_at: new Date().toISOString() })
    .select("id")
    .single();
  const { data: planMundo } = await admin
    .from("plans")
    .insert({
      session_id: (sMundo as { id: string }).id,
      user_id: dev.id,
      etiqueta: "completo",
      dominio: "quality",
      contenido_md: "# Calidad: que tus clientes vuelvan\n## Etapa 1: escucha\n**Esta semana:** llama a un cliente que se fue.",
      conceptos_usados: 4,
      familias_cubiertas: ["general"],
    })
    .select("id")
    .single();
  const planMundoId = (planMundo as { id: string }).id;
  await admin.from("checklist_items").insert([
    { project_id: pid, plan_id: planMundoId, dominio: "quality", etapa: 1, orden: 1, texto: "Llama a un cliente que se fue.", destacado: true },
    { project_id: pid, plan_id: planMundoId, dominio: "quality", etapa: 1, orden: 2, texto: "Anota por qué no volvió." },
  ]);

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

    console.log("[centro de creditos: heroe del saldo + Sumar creditos + Usa tus creditos]");
    await capturarDos(app, `${BASE_URL}/creditos`, "Sumar créditos", "beta_creditos");

    console.log("[Espacios: las 3 caras del CORE (cambiador + segmentado)]");
    await capturarDos(app, `${BASE_URL}/idea/${pid}?vista=manos&cara=manos`, "Tu viaje", "espacios_core_manos");
    await capturarDos(app, `${BASE_URL}/idea/${pid}?vista=manos&cara=plan`, "Tu viaje", "espacios_core_plan");
    await capturarDos(app, `${BASE_URL}/idea/${pid}?vista=manos&cara=avance`, "Tu avance", "espacios_core_avance");

    console.log("[Espacios: hub de un mundo SIN explorar (precio al frente)]");
    await capturarDos(app, `${BASE_URL}/idea/${pid}?vista=mundo&dominio=health_safety`, "Explorar este mundo", "espacios_hub_sinexplorar");

    console.log("[Espacios: las 3 caras del hub de un mundo CON plan]");
    await capturarDos(app, `${BASE_URL}/idea/${pid}?vista=mundo&dominio=quality&cara=manos`, "Manos a la obra", "espacios_hub_manos");
    await capturarDos(app, `${BASE_URL}/idea/${pid}?vista=mundo&dominio=quality&cara=plan`, "Manos a la obra", "espacios_hub_plan");
    await capturarDos(app, `${BASE_URL}/idea/${pid}?vista=mundo&dominio=quality&cara=avance`, "Tu avance", "espacios_hub_avance");

    // Fase 3 tandas 4-5: las lecturas GLOBALES de la campaña.
    console.log("[Espacios: bitacora global con etiquetas de espacio (chips)]");
    await capturarDos(app, `${BASE_URL}/idea/${pid}?vista=bitacora`, "Mi bitácora de mi viaje", "espacios_bitacora_etiquetas");

    console.log("[Espacios: Analisis global con 'Tu proyecto completo' (desglose por mundo)]");
    await capturarDos(app, `${BASE_URL}/idea/${pid}?vista=analisis`, "Tu proyecto completo", "espacios_analisis_desglose");

    console.log("[Espacios: documentos con el Reporte por mundo (tanda 5)]");
    await capturarDos(app, `${BASE_URL}/idea/${pid}?vista=documentos`, "Reporte de", "espacios_documentos_reporte");
  } finally {
    await browser.close();
    await admin.from("projects").delete().eq("id", pid);
  }
  console.log(
    "\nGATE DE LA BETA: compuerta + precios + chip + creditos + Espacios (cambiador, hubs, 3 caras, bitacora con etiquetas, desglose del Analisis, reportes por mundo) capturados (2 viewports).",
  );
}

main().catch((e) => {
  console.error(e);
  process.exit(1);
});
