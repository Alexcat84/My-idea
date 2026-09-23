// Capturas del hero en 3 anchos x 3 momentos del ciclo + consola + geometria.
// Uso: node capturar.mjs <baseURL> <carpetaSalida> [nivel] [soloAncho]
import { createRequire } from "node:module";
import { mkdirSync, writeFileSync } from "node:fs";
import path from "node:path";
const require = createRequire(new URL("../../../web/package.json", import.meta.url));
const { chromium } = require("playwright");

const base = process.argv[2] ?? "http://localhost:3108";
const salida = process.argv[3] ?? "capturas";
const nivel = process.argv[4] && process.argv[4] !== "auto" ? process.argv[4] : null;
const soloAncho = process.argv[5] ? Number(process.argv[5]) : null;
mkdirSync(salida, { recursive: true });

const CICLO = 9.8;
const MOMENTOS = { reposo: 1.7, transformacion: 3.4 + 0.95, figura: 3.4 + 1.9 + 1.3 };
const VISTAS = [
  { ancho: 390, alto: 844, dpr: 3, movil: true },
  { ancho: 768, alto: 1024, dpr: 2, movil: true },
  { ancho: 1440, alto: 900, dpr: 1, movil: false },
].filter((v) => !soloAncho || v.ancho === soloAncho);

const navegador = await chromium.launch({
  headless: true,
  channel: "chromium",
  args: ["--use-angle=d3d11", "--ignore-gpu-blocklist", "--enable-gpu"],
});

// Geometria desde los pixeles: caja de lo que brilla por encima del fondo.
async function medir(pagina, png, anchoCss, altoCss) {
  return pagina.evaluate(async ({ datos, anchoCss, altoCss }) => {
    const img = new Image();
    img.src = "data:image/png;base64," + datos;
    await img.decode();
    const c = document.createElement("canvas");
    c.width = img.width;
    c.height = img.height;
    const g = c.getContext("2d");
    g.drawImage(img, 0, 0);
    const d = g.getImageData(0, 0, c.width, c.height).data;
    let minX = 1e9, minY = 1e9, maxX = -1, maxY = -1;
    const umbral = 60;
    for (let y = 0; y < c.height; y++) {
      for (let x = 0; x < c.width; x++) {
        const i = (y * c.width + x) * 4;
        const l = 0.299 * d[i] + 0.587 * d[i + 1] + 0.114 * d[i + 2];
        if (l > umbral) {
          if (x < minX) minX = x;
          if (x > maxX) maxX = x;
          if (y < minY) minY = y;
          if (y > maxY) maxY = y;
        }
      }
    }
    const k = c.width / anchoCss;
    // brillo en el centro (nucleo): media de un cuadro de 4 % del lado menor
    const lado = Math.round(Math.min(c.width, c.height) * 0.04);
    let suma = 0, cuenta = 0;
    for (let y = Math.round(c.height / 2 - lado / 2); y < c.height / 2 + lado / 2; y++) {
      for (let x = Math.round(c.width / 2 - lado / 2); x < c.width / 2 + lado / 2; x++) {
        const i = (y * c.width + x) * 4;
        suma += 0.299 * d[i] + 0.587 * d[i + 1] + 0.114 * d[i + 2];
        cuenta++;
      }
    }
    if (maxX < 0) return { vacio: true, nucleo: suma / cuenta };
    const menor = Math.min(anchoCss, altoCss);
    const cx = (minX + maxX + 1) / 2 / k;
    const cy = (minY + maxY + 1) / 2 / k;
    return {
      caja: [minX / k, minY / k, (maxX + 1) / k, (maxY + 1) / k].map((v) => Math.round(v)),
      desvioCentroX: +(cx - anchoCss / 2).toFixed(1),
      desvioCentroY: +(cy - altoCss / 2).toFixed(1),
      anchoFrac: +(((maxX - minX + 1) / k) / menor).toFixed(3),
      altoFrac: +(((maxY - minY + 1) / k) / menor).toFixed(3),
      tocaBorde: minX <= 0 || minY <= 0 || maxX >= c.width - 1 || maxY >= c.height - 1,
      nucleo: +(suma / cuenta).toFixed(1),
    };
  }, { datos: png.toString("base64"), anchoCss, altoCss });
}

const informe = [];
for (const v of VISTAS) {
  const contexto = await navegador.newContext({
    viewport: { width: v.ancho, height: v.alto },
    deviceScaleFactor: v.dpr,
    isMobile: v.movil,
    hasTouch: v.movil,
  });
  const pagina = await contexto.newPage();
  const consola = [];
  pagina.on("console", (m) => {
    if (m.type() === "error" || m.type() === "warning") consola.push(`${m.type()}: ${m.text().slice(0, 400)}`);
  });
  pagina.on("pageerror", (e) => consola.push(`pageerror: ${String(e).slice(0, 400)}`));
  pagina.on("worker", (w) => w.on("console", (m) => { if (m.type() === "error" || m.type() === "warning") consola.push(`worker ${m.type()}: ${m.text().slice(0, 400)}`); }));
  const hoja = await navegador.newPage();
  for (const [momento, t] of Object.entries(MOMENTOS)) {
    const q = new URLSearchParams({ "masa-t": String(t) });
    if (nivel) q.set("masa", nivel);
    await pagina.goto(`${base}/?${q}`, { waitUntil: "load" });
    await pagina.waitForSelector('.portada-masa[data-listo="1"], .portada-masa[data-nivel="fija"]', { timeout: 60000 });
    await pagina.waitForTimeout(900);
    const heroe = pagina.locator("#inicio");
    const caja = await heroe.boundingBox();
    // Para medir: sin el boton ni el indicador de desarrollo de Next.
    const ocultar = (v) => pagina.evaluate((vis) => {
      for (const el of document.querySelectorAll(".portada-cta, nextjs-portal")) el.style.visibility = vis;
    }, v);
    await ocultar("hidden");
    const pngMedida = await heroe.screenshot();
    await ocultar("");
    const png = await heroe.screenshot();
    const archivo = `hero-${v.ancho}-${momento}.png`;
    writeFileSync(path.join(salida, archivo), png);
    const datos = await pagina.evaluate(() => {
      const m = document.querySelector(".portada-masa");
      return { nivel: m?.dataset.nivel, descartes: m?.dataset.descartes ?? "" };
    });
    const geo = await medir(hoja, pngMedida, caja.width, caja.height);
    informe.push({ ancho: v.ancho, momento, archivo, hero: [Math.round(caja.width), Math.round(caja.height)], ...datos, ...geo });
  }
  informe.push({ ancho: v.ancho, consola });
  await contexto.close();
}
await navegador.close();
writeFileSync(path.join(salida, "informe.json"), JSON.stringify(informe, null, 2));
console.log(JSON.stringify(informe, null, 1));
