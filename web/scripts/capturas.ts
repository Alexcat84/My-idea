// Fase 3.6: capturas del preview contra los HTML de referencia del canon.
// Reusa la autenticacion real del vuelo (dev user) y captura, con el dev
// server corriendo en :3000, las pantallas convergidas: home de cintas,
// La Chispa, centro de creditos, la vista de idea (plan) y Manos a la
// Obra. Guarda PNGs desktop (1240) y mobile (380) en examples/capturas/.
//
// Uso: pnpm dev en otra terminal, luego:
//   npx tsx scripts/capturas.tsx [projectId]
// Sin projectId toma la idea mas reciente del dev user via /api/projects.
import { chromium, type BrowserContext } from "playwright";
import { mkdirSync } from "node:fs";
import path from "node:path";
import { autenticarComoDevUser, BASE_URL, cargarEnvRaiz, getJson, ROOT } from "./_shared/http";

cargarEnvRaiz();

const OUT = path.join(ROOT, "web", "examples", "capturas");

async function contextoConSesion(cookieHeader: string, viewport: { width: number; height: number }) {
  const browser = await chromium.launch();
  const context = await browser.newContext({ viewport, deviceScaleFactor: 1 });
  const url = new URL(BASE_URL);
  await context.addCookies(
    cookieHeader.split("; ").map((par) => {
      const i = par.indexOf("=");
      return {
        name: par.slice(0, i),
        value: par.slice(i + 1),
        domain: url.hostname,
        path: "/",
      };
    })
  );
  return { browser, context };
}

async function capturar(context: BrowserContext, ruta: string, archivo: string) {
  const page = await context.newPage();
  await page.goto(`${BASE_URL}${ruta}`, { waitUntil: "networkidle" });
  // las animaciones planIn duran 0.6s + delays escalonados
  await page.waitForTimeout(1800);
  await page.screenshot({ path: path.join(OUT, archivo), fullPage: true });
  await page.close();
  console.log(`  ${archivo} <- ${ruta}`);
}

async function main() {
  mkdirSync(OUT, { recursive: true });
  const cookie = await autenticarComoDevUser();

  let projectId = process.argv[2];
  if (!projectId) {
    const proyectos = (await getJson(cookie, "/api/projects")) as { proyectos?: Array<{ id: string }> };
    const lista = (proyectos.proyectos ?? (proyectos as unknown as Array<{ id: string }>)) as Array<{ id: string }>;
    if (!Array.isArray(lista) || lista.length === 0) {
      throw new Error("el dev user no tiene ideas; corre el vuelo primero o pasa un projectId");
    }
    projectId = lista[0].id;
  }
  console.log(`projectId: ${projectId}`);

  const rutas: Array<[string, string]> = [
    ["/ideas", "01_home_cintas"],
    ["/nueva", "02_la_chispa"],
    [`/idea/${projectId}`, "05_tu_plan"],
    [`/idea/${projectId}?vista=manos`, "06_manos_a_la_obra"],
    ["/potenciadores", "07_potenciadores"],
  ];

  for (const [ancho, sufijo] of [
    [1240, "desktop"],
    [380, "mobile"],
  ] as Array<[number, string]>) {
    console.log(`\n--- ${sufijo} (${ancho}px) ---`);
    const { browser, context } = await contextoConSesion(cookie, { width: ancho, height: 900 });
    for (const [ruta, nombre] of rutas) {
      await capturar(context, ruta, `${nombre}_${sufijo}.png`);
    }
    await browser.close();
  }
  console.log(`\nCapturas en ${OUT}`);
}

main();
