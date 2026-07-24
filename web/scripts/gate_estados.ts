/**
 * gate_estados.ts — la vara del GESTOR DE ESTADOS sobre el build real, en dos
 * viewports (escritorio 1280 y móvil 380), como pidió el fundador (§6).
 *
 * Siembra un proyecto con checklist (service role, cero LLM), pone una tarea
 * en cada estado — incluida una RETIRADA con motivo — y captura:
 *   - el checklist con los 5 estados visibles,
 *   - el MENÚ de estados abierto (popover en escritorio, hoja inferior a 380),
 *   - el cajón de Detalle con el motivo de "no aplica".
 *
 * REQUISITO: la migración 030 debe estar aplicada (el estado 'no_aplica' viola
 * el CHECK viejo). Sin ella, el sembrado falla con 23514 — ruidoso a propósito.
 *
 * Uso: pnpm dev en otra terminal, luego
 *   npx tsx scripts/gate_estados.ts
 */
import { createClient } from "@supabase/supabase-js";
import { createServerClient } from "@supabase/ssr";
import { chromium, type Page } from "playwright";
import { autenticarComoDevUser, BASE_URL, cargarEnvRaiz } from "./_shared/http";
import { derivarChecklist } from "../lib/engine/checklist";

cargarEnvRaiz();

const DIR = "examples/gate-canon";

async function main() {
  const admin = createClient(process.env.NEXT_PUBLIC_SUPABASE_URL!, process.env.SUPABASE_SERVICE_ROLE_KEY!, {
    auth: { persistSession: false },
  });

  const jar = new Map<string, string>();
  const anon = createServerClient(process.env.NEXT_PUBLIC_SUPABASE_URL!, process.env.NEXT_PUBLIC_SUPABASE_ANON_KEY!, {
    cookies: {
      getAll: () => [...jar].map(([name, value]) => ({ name, value })),
      setAll: (cs) => cs.forEach((c) => jar.set(c.name, c.value)),
    },
  });
  const { data: sesion, error: eLogin } = await anon.auth.signInWithPassword({
    email: "dev@my-idea.local",
    password: process.env.VUELO_DEV_PASSWORD!,
  });
  if (eLogin || !sesion.user) throw eLogin ?? new Error("sin user");
  const userId = sesion.user.id;

  const { data: planReal } = await admin
    .from("plans")
    .select("contenido_md")
    .eq("etiqueta", "completo")
    .order("created_at", { ascending: false })
    .limit(1)
    .single();
  const md = planReal!.contenido_md as string;

  const { data: proy } = await admin
    .from("projects")
    .insert({ user_id: userId, entrada_original: "Kits de huerto para balcones.", titulo: "Gestor de estados", fase_actual: "ejecucion", modo_camino: "fechas" })
    .select("id")
    .single();
  const projectId = proy!.id as string;
  const { data: ses } = await admin
    .from("sessions")
    .insert({ project_id: projectId, user_id: userId, session_position: 1, tipo: "inicial", mensaje_entrada: "kits" })
    .select("id")
    .single();
  const { data: pl } = await admin
    .from("plans")
    .insert({ session_id: ses!.id, user_id: userId, etiqueta: "completo", contenido_md: md, conceptos_usados: 9, familias_cubiertas: [] })
    .select("id")
    .single();

  const items = derivarChecklist(md);
  // Un estado por ítem para que la captura muestre los cinco a la vez.
  const estados = ["hecho", "en_proceso", "empezado", "no_aplica", "pendiente"];
  const filas = items.map((i, idx) => ({
    project_id: projectId,
    plan_id: pl!.id,
    dominio: "core",
    etapa: i.etapa,
    orden: i.orden,
    texto: i.texto,
    destacado: i.destacado,
    estado: estados[idx % estados.length],
    completed_at: idx % estados.length === 0 ? new Date(Date.UTC(2026, 6, 20, 12)).toISOString() : null,
    no_aplica_motivo: idx % estados.length === 3 ? "mi negocio es 100% online, no necesito local" : null,
    fecha_base: new Date(Date.UTC(2026, 6, 31, 12)).toISOString(),
  }));
  const { error: eItems } = await admin.from("checklist_items").insert(filas);
  if (eItems) throw new Error(`sembrado falló (¿migración 030 sin aplicar? ${eItems.code}): ${eItems.message}`);

  const cookie = await autenticarComoDevUser();
  const cookies = cookie.split("; ").map((kv) => {
    const i = kv.indexOf("=");
    return { name: kv.slice(0, i), value: kv.slice(i + 1), domain: "localhost", path: "/" };
  });
  const browser = await chromium.launch();

  async function capturar(ancho: number, sufijo: string) {
    const ctx = await browser.newContext({ viewport: { width: ancho, height: 1200 } });
    await ctx.addCookies(cookies);
    const page: Page = await ctx.newPage();
    await page.goto(`${BASE_URL}/idea/${projectId}?vista=manos`, { waitUntil: "networkidle" });
    await page.waitForTimeout(1500);
    await page.screenshot({ path: `${DIR}/estados_checklist_app${sufijo}.png`, fullPage: false });

    // El menú de estados abierto (popover en escritorio, hoja inferior a 380).
    await page.getByRole("button", { name: /Tocar para elegir el estado/ }).first().click();
    await page.waitForTimeout(500);
    await page.screenshot({ path: `${DIR}/estados_menu_app${sufijo}.png`, fullPage: false });
    await page.keyboard.press("Escape").catch(() => {});

    // El detalle de la tarea retirada, con su motivo.
    await page.getByText(/no necesito local|Contrata|local/).first().click().catch(() => {});
    await page.waitForTimeout(400);
    const retirada = page.getByText("no aplica").first();
    if (await retirada.isVisible().catch(() => false)) {
      // abrir el detalle de esa fila tocando su texto
      const filaRetirada = page.locator("text=no aplica").first();
      await filaRetirada.scrollIntoViewIfNeeded().catch(() => {});
    }
    await ctx.close();
  }

  await capturar(1280, "");
  await capturar(380, "_380");

  // El detalle con el motivo (una sola captura de escritorio basta para la vara).
  const ctx = await browser.newContext({ viewport: { width: 1280, height: 1200 } });
  await ctx.addCookies(cookies);
  const page = await ctx.newPage();
  await page.goto(`${BASE_URL}/idea/${projectId}?vista=manos`, { waitUntil: "networkidle" });
  await page.waitForTimeout(1500);
  // Abrir el detalle de la retirada (su texto lleva el tachado atenuado "no aplica").
  const filas2 = page.locator("[class*='rounded-cinta']");
  const n = await filas2.count();
  for (let i = 0; i < n; i++) {
    const t = await filas2.nth(i).innerText().catch(() => "");
    if (t.includes("no aplica")) {
      await filas2.nth(i).getByRole("button").nth(1).click().catch(() => {});
      break;
    }
  }
  await page.waitForTimeout(600);
  await page.screenshot({ path: `${DIR}/estados_detalle_app.png`, fullPage: false });
  await ctx.close();

  await browser.close();
  await admin.from("projects").delete().eq("id", projectId);
  console.log("gate de estados: capturas en web/examples/gate-canon/ (checklist, menu y detalle; 1280 y 380).");
}

main();
