// FASE B (canon 12) - par del gate del Cierre honesto. El cierre es un estado
// dentro de IdeaView, no una ruta; se captura desde el harness /dev/cierre
// (tokens reales, los dos estados) junto al frame del canon 12. Dos viewports.
//
// Uso: con `pnpm dev` en :3000,  npx tsx scripts/gate_cierre.ts
// Salida: web/examples/gate-canon/cierre_{camino|mundo}_{app|canon}[_380].png
import { chromium, type Page } from "playwright";
import { mkdirSync } from "node:fs";
import path from "node:path";
import { pathToFileURL } from "node:url";
import { autenticarComoDevUser, BASE_URL, cargarEnvRaiz, ROOT } from "./_shared/http";

cargarEnvRaiz();
const OUT = path.join(ROOT, "web", "examples", "gate-canon");
const CANON = path.join(ROOT, "docs", "diseno-canon");
const VP_ESCRITORIO = { width: 1240, height: 900 };
const VP_MOVIL = { width: 380, height: 844 };

async function capturarEstado(app: Page, label: string, base: string) {
  await app.setViewportSize(VP_ESCRITORIO);
  await app.goto(`${BASE_URL}/dev/cierre`);
  await app.waitForSelector(`[data-screen-label="${label}"]`, { timeout: 30000 });
  await app.waitForTimeout(600);
  await app.locator(`[data-screen-label="${label}"]`).screenshot({ path: path.join(OUT, `${base}_app.png`) });
  console.log(`  ${base}_app.png`);
  await app.setViewportSize(VP_MOVIL);
  await app.waitForTimeout(600);
  await app.locator(`[data-screen-label="${label}"]`).screenshot({ path: path.join(OUT, `${base}_app_380.png`) });
  console.log(`  ${base}_app_380.png`);
  await app.setViewportSize(VP_ESCRITORIO);
}

async function capturarCanon(canon: Page, label: string, archivo: string) {
  await canon.goto(pathToFileURL(path.join(CANON, "12_el_cierre_honesto.html")).href);
  await canon.waitForTimeout(500);
  await canon.locator(`[data-screen-label="${label}"]`).first().screenshot({ path: path.join(OUT, archivo) });
  console.log(`  ${archivo} <- canon [${label}]`);
}

async function main() {
  mkdirSync(OUT, { recursive: true });
  const cookie = await autenticarComoDevUser();
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
  await canon.setViewportSize(VP_ESCRITORIO);

  try {
    console.log("CAMINO sin salida (core):");
    await capturarEstado(app, "Cierre honesto camino", "cierre_camino");
    await capturarCanon(canon, "Cierre honesto camino desktop", "cierre_camino_canon.png");
    await capturarCanon(canon, "Cierre honesto camino movil 380", "cierre_camino_canon_380.png");

    console.log("MUNDO que no encaja (reembolso):");
    await capturarEstado(app, "Cierre honesto mundo", "cierre_mundo");
    await capturarCanon(canon, "Cierre honesto mundo desktop", "cierre_mundo_canon.png");
    await capturarCanon(canon, "Cierre honesto mundo movil 380", "cierre_mundo_canon_380.png");
  } finally {
    await browser.close();
  }
  console.log("\nGATE DEL CIERRE HONESTO: par app-vs-canon 12 capturado (camino + mundo, 2 viewports).");
}

main().catch((e) => {
  console.error(e);
  process.exit(1);
});
