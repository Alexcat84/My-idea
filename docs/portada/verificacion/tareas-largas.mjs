import { createRequire } from "node:module";
const require = createRequire(new URL("../../../web/package.json", import.meta.url));
const { chromium } = require("playwright");
const base = process.argv[2]; const q = process.argv[3] ?? "";
const nav = await chromium.launch({ headless: true, channel: "chrome" });
const ctx = await nav.newContext({ viewport: { width: 412, height: 823 }, deviceScaleFactor: 1.75, isMobile: true, hasTouch: true });
const p = await ctx.newPage();
await p.addInitScript(() => {
  window.__largas = [];
  new PerformanceObserver((l) => { for (const e of l.getEntries()) window.__largas.push([Math.round(e.startTime), Math.round(e.duration)]); }).observe({ type: "longtask", buffered: true });
});
await p.goto(`${base}/${q}`, { waitUntil: "load" });
await p.waitForTimeout(12000);
const r = await p.evaluate(() => {
  const c = document.createElement("canvas").getContext("webgl2");
  const i = c.getExtension("WEBGL_debug_renderer_info");
  return { gpu: c.getParameter(i.UNMASKED_RENDERER_WEBGL), paralelo: !!c.getExtension("KHR_parallel_shader_compile"), nivel: document.querySelector(".portada-masa").dataset.nivel, largas: window.__largas };
});
console.log(JSON.stringify(r));
await nav.close();
