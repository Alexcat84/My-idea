import { createRequire } from "node:module";
const require = createRequire(new URL("../../../web/package.json", import.meta.url));
const { chromium } = require("playwright");
const base = process.argv[2];
for (const c of [{ n: "GPU real, CPU x20", gpu: true, cpu: 20 }, { n: "SwiftShader (software), CPU x1", gpu: false, cpu: 1 }, { n: "sin WebGL", gpu: false, cpu: 1, sinGl: true }]) {
  const nav = await chromium.launch(c.gpu ? { headless: true, channel: "chromium", args: ["--use-angle=d3d11", "--enable-gpu"] } : { headless: true, args: c.sinGl ? ["--disable-webgl", "--disable-webgl2"] : [] });
  const ctx = await nav.newContext({ viewport: { width: 1440, height: 900 } });
  const p = await ctx.newPage(); const log = [];
  p.on("console", (m) => { if (["error", "warning"].includes(m.type())) log.push(m.text().slice(0, 150)); });
  p.on("pageerror", (e) => log.push(String(e)));
  p.on("worker", (w) => w.on("console", (m) => { if (["error", "warning"].includes(m.type())) log.push("worker: " + m.text().slice(0, 200)); }));
  if (c.cpu > 1) { const cdp = await ctx.newCDPSession(p); await cdp.send("Emulation.setCPUThrottlingRate", { rate: c.cpu }); }
  await p.goto(base + "/", { waitUntil: "load" });
  await p.waitForTimeout(55000);
  const r = await p.evaluate(() => { const m = document.querySelector(".portada-masa"); return { nivel: m.dataset.nivel, descartes: m.dataset.descartes ?? "", fps: m.dataset.fps, lienzos: m.querySelectorAll("canvas").length }; });
  console.log(c.n, JSON.stringify(r), log.length ? log : "consola limpia");
  await nav.close();
}
