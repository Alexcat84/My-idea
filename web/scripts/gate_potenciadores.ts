// FASE B (canon 07) - par del gate de Potenciadores y Creditos. /potenciadores
// es ruta real; se captura full-page en dos viewports junto al frame canon 07.
// Uso: con `pnpm dev` en :3000,  npx tsx scripts/gate_potenciadores.ts
import { chromium } from "playwright";
import { mkdirSync } from "node:fs";
import path from "node:path";
import { pathToFileURL } from "node:url";
import { autenticarComoDevUser, BASE_URL, cargarEnvRaiz, ROOT } from "./_shared/http";
cargarEnvRaiz();
const OUT = path.join(ROOT, "web", "examples", "gate-canon");
const CANON = path.join(ROOT, "docs", "diseno-canon");
const VP_ESCRITORIO = { width: 1240, height: 900 };
const VP_MOVIL = { width: 380, height: 844 };
async function main() {
  mkdirSync(OUT, { recursive: true });
  const cookie = await autenticarComoDevUser();
  const browser = await chromium.launch();
  const context = await browser.newContext({ viewport: VP_ESCRITORIO, deviceScaleFactor: 1 });
  const url = new URL(BASE_URL);
  await context.addCookies(cookie.split("; ").map((par) => { const i = par.indexOf("="); return { name: par.slice(0, i), value: par.slice(i + 1), domain: url.hostname, path: "/" }; }));
  const app = await context.newPage();
  const canon = await context.newPage();
  try {
    await app.goto(`${BASE_URL}/potenciadores`);
    await app.waitForSelector("text=Tus créditos", { timeout: 30000 });
    await app.waitForTimeout(800);
    await app.screenshot({ path: path.join(OUT, "potenciadores_app.png"), fullPage: true });
    console.log("  potenciadores_app.png");
    await app.setViewportSize(VP_MOVIL); await app.waitForTimeout(600);
    await app.screenshot({ path: path.join(OUT, "potenciadores_app_380.png"), fullPage: true });
    console.log("  potenciadores_app_380.png");
    await canon.setViewportSize(VP_ESCRITORIO);
    await canon.goto(pathToFileURL(path.join(CANON, "07_potenciadores_y_creditos.html")).href);
    await canon.waitForTimeout(500);
    for (const [label, out] of [["Potenciadores y Creditos desktop", "potenciadores_canon.png"], ["Potenciadores y Creditos movil 380", "potenciadores_canon_380.png"]] as const) {
      await canon.locator(`[data-screen-label="${label}"]`).first().screenshot({ path: path.join(OUT, out) });
      console.log(`  ${out} <- canon [${label}]`);
    }
  } finally { await browser.close(); }
  console.log("\nGATE 07: par app-vs-canon capturado (2 viewports).");
}
main().catch((e) => { console.error(e); process.exit(1); });
