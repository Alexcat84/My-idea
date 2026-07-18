// FASE B (canon 14) - par del gate de Tus Numeros. Siembra una idea en
// PERDIDA (velas) y una SANA (kits) para el dev user, navega a
// /idea/[id]/numeros y captura la app viva en los DOS viewports (1240 y 380),
// junto al frame del HTML canon 14 que le corresponde. Foco: producir el par
// app-vs-canon sin correr el gate completo. El veredicto visual es del fundador.
//
// Uso: con `pnpm dev` en :3000,  npx tsx scripts/gate_numeros.ts
// Salida: web/examples/gate-canon/numeros_{perdida|sano}_{app|canon}[_380].png
import { chromium, type Page } from "playwright";
import { createClient } from "@supabase/supabase-js";
import { mkdirSync } from "node:fs";
import path from "node:path";
import { pathToFileURL } from "node:url";
import { autenticarComoDevUser, BASE_URL, cargarEnvRaiz, postJson, ROOT } from "./_shared/http";

cargarEnvRaiz();
const admin = createClient(process.env.NEXT_PUBLIC_SUPABASE_URL!, process.env.SUPABASE_SERVICE_ROLE_KEY!);
const OUT = path.join(ROOT, "web", "examples", "gate-canon");
const CANON = path.join(ROOT, "docs", "diseno-canon");
const VP_ESCRITORIO = { width: 1240, height: 900 };
const VP_MOVIL = { width: 380, height: 844 };

function campo(valor: number) {
  return { valor, unidad: null, texto_original: "" };
}

async function sembrar(userId: string, titulo: string, unidad: string, numeros: Record<string, number>) {
  const envuelto = Object.fromEntries(Object.entries(numeros).map(([k, v]) => [k, campo(v)]));
  const { data, error } = await admin
    .from("projects")
    .insert({
      user_id: userId,
      entrada_original: titulo,
      titulo,
      fase_actual: "planificacion",
      status: "active",
      tipo_oferta: "producto_fisico",
      unidad_venta: unidad,
      numeros_proyecto: envuelto,
    })
    .select("id")
    .single();
  if (error) throw error;
  return (data as { id: string }).id;
}

async function capturar(page: Page, archivo: string, fullPage = true) {
  await page.waitForTimeout(1200);
  await page.screenshot({ path: path.join(OUT, archivo), fullPage });
  console.log(`  ${archivo}`);
}

async function capturarApp(app: Page, pid: string, base: string) {
  await app.setViewportSize(VP_ESCRITORIO);
  await app.goto(`${BASE_URL}/idea/${pid}/numeros`);
  await app.waitForSelector('[data-screen-label="Tus Numeros vista"]', { timeout: 30000 });
  await capturar(app, `${base}_app.png`);
  await app.setViewportSize(VP_MOVIL);
  await app.waitForTimeout(700);
  await capturar(app, `${base}_app_380.png`);
  await app.setViewportSize(VP_ESCRITORIO);
  await app.waitForTimeout(400);
}

async function capturarCanon(canon: Page, label: string, archivo: string) {
  await canon.goto(pathToFileURL(path.join(CANON, "14_tus_numeros.html")).href);
  await canon.waitForTimeout(600);
  const frame = canon.locator(`[data-screen-label="${label}"]`).first();
  await frame.screenshot({ path: path.join(OUT, archivo) });
  console.log(`  ${archivo} <- canon [${label}]`);
}

async function main() {
  mkdirSync(OUT, { recursive: true });
  const cookie = await autenticarComoDevUser();
  const { data: lista } = await admin.auth.admin.listUsers();
  const dev = lista.users.find((u) => u.email === "dev@my-idea.local");
  if (!dev) throw new Error("no encuentro el dev user dev@my-idea.local");

  // PERDIDA (velas del canon): costo 42, precio 38, fijos 200 -> margen -4.
  const pidPerdida = await sembrar(dev.id, "Velas artesanales de soya con esencias importadas", "vela", {
    costo_materiales_unidad: 30,
    horas_por_unidad: 2,
    valor_hora: 6,
    precio_tentativo: 38,
    costos_fijos_mensuales: 200,
    capacidad_semanal: 5,
  });
  // SANO (kits): arranca VACIO; su historial se construye por HTTP mas abajo
  // (dos correcciones reales) para estrenar el sello "HOY" y "Versiones anteriores".
  const pidSano = await sembrar(dev.id, "Kits de huerto urbano para balcones pequenos", "kit", {});

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
  const canon = await context.newPage();

  try {
    console.log("PERDIDA (velas):");
    await capturarApp(app, pidPerdida, "numeros_perdida");
    await canon.setViewportSize(VP_ESCRITORIO);
    await capturarCanon(canon, "Tus Numeros perdida desktop", "numeros_perdida_canon.png");
    await capturarCanon(canon, "Tus Numeros perdida movil 380", "numeros_perdida_canon_380.png");

    console.log("SANO (kits) con historial:");
    const rutaSano = `/api/project/${pidSano}/numeros`;
    // v1: precio 150 -> perdida (margen -30). v2: precio 350 -> sano + ciclo de caja.
    // Dos versiones el MISMO dia: la lista muestra la hora (desambigua gemelas).
    await postJson(cookie, rutaSano, { numeros: { costo_materiales_unidad: 100, horas_por_unidad: 4, valor_hora: 20, precio_tentativo: 150, costos_fijos_mensuales: 1200, capacidad_semanal: 7.5 } });
    await postJson(cookie, rutaSano, { numeros: { precio_tentativo: 350, dias_inventario: 40, dias_cobro_clientes: 30, dias_pago_proveedores: 20 } });
    await capturarApp(app, pidSano, "numeros_sano");
    await capturarCanon(canon, "Tus Numeros sano desktop", "numeros_sano_canon.png");
    await capturarCanon(canon, "Tus Numeros sano movil 380", "numeros_sano_canon_380.png");

    // Modo LECTURA: visitar la version pasada (perdida) desde "Versiones anteriores".
    console.log("SANO (kits) modo lectura:");
    await app.setViewportSize(VP_ESCRITORIO);
    await app.goto(`${BASE_URL}/idea/${pidSano}/numeros`);
    await app.waitForSelector('[data-screen-label="Tus Numeros vista"]', { timeout: 30000 });
    await app.getByText("pérdida", { exact: true }).first().click();
    await app.waitForSelector("text=Estás viendo tus números del", { timeout: 15000 });
    await capturar(app, "numeros_lectura_app.png");
  } finally {
    await browser.close();
    await admin.from("projects").delete().in("id", [pidPerdida, pidSano]);
  }
  console.log("\nGATE DE TUS NUMEROS: par app-vs-canon 14 capturado (perdida + sano, 2 viewports).");
}

main().catch((e) => {
  console.error(e);
  process.exit(1);
});
