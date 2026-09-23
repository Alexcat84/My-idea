// FPS reales: escritorio (GPU real) y perfil movil (viewport + CPU x4).
// Uso: node fps.mjs <baseURL> [nivel|auto] [segundos]
import { createRequire } from "node:module";
const require = createRequire(new URL("../../../web/package.json", import.meta.url));
const { chromium } = require("playwright");

const base = process.argv[2] ?? "http://localhost:3108";
const nivel = process.argv[3] && process.argv[3] !== "auto" ? process.argv[3] : null;
const segundos = Number(process.argv[4] ?? 8);
const PERFILES = [
  { nombre: "escritorio 1440x900", viewport: { width: 1440, height: 900 }, dpr: 1, movil: false, cpu: 1 },
  { nombre: "movil 390x844 dpr3 CPUx4", viewport: { width: 390, height: 844 }, dpr: 3, movil: true, cpu: 4 },
];

const navegador = await chromium.launch({
  headless: true,
  channel: "chromium",
  args: ["--use-angle=d3d11", "--ignore-gpu-blocklist", "--enable-gpu"],
});
for (const p of PERFILES) {
  const ctx = await navegador.newContext({ viewport: p.viewport, deviceScaleFactor: p.dpr, isMobile: p.movil, hasTouch: p.movil });
  const pagina = await ctx.newPage();
  const errores = [];
  pagina.on("console", (m) => { if (m.type() === "error") errores.push(m.text().slice(0, 300)); });
  pagina.on("pageerror", (e) => errores.push(String(e).slice(0, 300)));
  if (p.cpu > 1) {
    const cdp = await ctx.newCDPSession(pagina);
    await cdp.send("Emulation.setCPUThrottlingRate", { rate: p.cpu });
  }
  await pagina.goto(`${base}/${nivel ? `?masa=${nivel}` : ""}`, { waitUntil: "load" });
  await pagina.waitForSelector('.portada-masa[data-listo="1"], .portada-masa[data-nivel="fija"]', { timeout: 60000 });
  // deja correr la medicion adaptativa (calentamiento + ventana, y posibles caidas)
  await pagina.waitForTimeout(segundos * 1000);
  const r = await pagina.evaluate(async () => {
    const cuadros = [];
    let ultimo = performance.now();
    await new Promise((fin) => {
      const inicio = ultimo;
      const paso = (ahora) => {
        cuadros.push(ahora - ultimo);
        ultimo = ahora;
        if (ahora - inicio < 5000) requestAnimationFrame(paso);
        else fin();
      };
      requestAnimationFrame(paso);
    });
    cuadros.shift();
    const orden = [...cuadros].sort((a, b) => a - b);
    const m = document.querySelector(".portada-masa");
    return {
      nivel: m?.dataset.nivel,
      descartes: m?.dataset.descartes ?? "",
      fpsMedidoPorElMotor: m?.dataset.fps,
      fpsMediana5s: +(1000 / orden[Math.floor(orden.length / 2)]).toFixed(1),
      fpsP10_5s: +(1000 / orden[Math.floor(orden.length * 0.9)]).toFixed(1),
      cuadros: cuadros.length,
    };
  });
  console.log(p.nombre, JSON.stringify(r), errores.length ? `ERRORES: ${errores.join(" | ")}` : "consola limpia");
  await ctx.close();
}
await navegador.close();
