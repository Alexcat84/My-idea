import { createRequire } from "node:module";
import { gzipSync } from "node:zlib";
const require = createRequire(new URL("../../../web/package.json", import.meta.url));
const { chromium } = require("playwright");
const base = process.argv[2];
const nav = await chromium.launch({ headless: true, channel: "chromium", args: ["--use-angle=d3d11", "--ignore-gpu-blocklist", "--enable-gpu"] });
const res = {};
for (const q of ["?masa=fija", "?masa=particulas", ""]) {
  const ctx = await nav.newContext({ viewport: { width: 1440, height: 900 } });
  const p = await ctx.newPage(); const pend = []; const js = {};
  p.on("response", (r) => { const u = r.url(); if (u.endsWith(".js")) pend.push(r.body().then((b) => { js[u.split("/").pop()] = [b.length, gzipSync(b).length]; }).catch(() => {})); });
  await p.goto(`${base}/${q}`, { waitUntil: "load" });
  const alCargar = new Set(Object.keys(js));
  await p.waitForSelector('.portada-masa[data-listo="1"], .portada-masa[data-nivel="fija"]', { timeout: 60000 });
  await p.waitForTimeout(2000); await Promise.all(pend);
  res[q || "auto"] = js;
  await ctx.close();
}
const baseSet = res["?masa=fija"];
const tot = (o) => Object.values(o).reduce((a, b) => [a[0] + b[0], a[1] + b[1]], [0, 0]);
console.log("JS de la portada sin motor (fija):", tot(baseSet));
for (const k of ["?masa=particulas", "auto"]) {
  const extra = Object.fromEntries(Object.entries(res[k]).filter(([n]) => !(n in baseSet)));
  console.log(k, "extra diferido:", tot(extra), JSON.stringify(extra));
}
await nav.close();
