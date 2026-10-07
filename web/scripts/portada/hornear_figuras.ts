/**
 * El horno de las figuras de la portada (decisión del fundador, 8 oct 2026:
 * "siluetas precalculadas, ligera en móviles").
 *
 * Dibuja cada figura de scripts/portada/dibujos.ts en un lienzo de Chromium
 * (Playwright), calcula su campo de distancia con signo con la MISMA función que
 * usaba el navegador (campoDesdeMascara, masa/figuras.ts) y lo guarda cuantizado
 * en public/portada/figuras/<nombre>.bin (LADO_CAMPO² valores de 16 bits). Escribe
 * también el catálogo (app/ui/portada/masa/catalogo.ts). El navegador ya no
 * dibuja ni calcula nada: baja el campo de la figura que va a formar.
 *
 * Uso (desde web/):
 *   npx tsx scripts/portada/hornear_figuras.ts            hornea todo
 *   npx tsx scripts/portada/hornear_figuras.ts --hoja=x.png   además, la hoja de contactos
 */
import { mkdirSync, readdirSync, rmSync, writeFileSync } from "node:fs";
import path from "node:path";
import { chromium } from "playwright";
import { campoDesdeMascara, codificarCampo, LADO_CAMPO, LADO_RASTER_CAMPO } from "../../app/ui/portada/masa/figuras";
import { crearAyudas, DIBUJOS } from "./dibujos";

const WEB = path.resolve(__dirname, "..", "..");
const DESTINO = path.join(WEB, "public", "portada", "figuras");
const CATALOGO = path.join(WEB, "app", "ui", "portada", "masa", "catalogo.ts");

const hoja = process.argv.find((a) => a.startsWith("--hoja="))?.slice("--hoja=".length) ?? null;
const nombres = Object.keys(DIBUJOS);
// Los dibujos son métodos ("nombre(g, h) { ... }"): como texto se vuelven funciones.
// Solo se evalúa código de este repo, en un Chromium sin red y fuera del producto.
const fuentes = nombres.map((n) => {
  const s = DIBUJOS[n].toString();
  return s.startsWith("function") ? s : `function ${s}`;
});

async function main() {
  const navegador = await chromium.launch();
  const pagina = await navegador.newPage({ viewport: { width: 1400, height: 1000 } });
  await pagina.setContent("<html><body style='margin:0;background:#000'></body></html>");

  // Las máscaras: alfa > 128 en un lienzo de LADO_RASTER_CAMPO (como antes).
  const mascaras: string[] = await pagina.evaluate(
    ({ fuentes, ayudasFuente, lado }) => {
      const crear = new Function(`return (${ayudasFuente})`)();
      return fuentes.map((fuente: string) => {
        const lienzo = new OffscreenCanvas(lado, lado);
        const g = lienzo.getContext("2d", { willReadFrequently: true })!;
        g.scale(lado / 512, lado / 512);
        g.strokeStyle = "#fff";
        g.fillStyle = "#fff";
        g.lineCap = "round";
        g.lineJoin = "round";
        g.lineWidth = 16;
        new Function(`return (${fuente})`)()(g, crear(g));
        const datos = g.getImageData(0, 0, lado, lado).data;
        let bin = "";
        for (let i = 0; i < lado * lado; i++) bin += datos[i * 4 + 3] > 128 ? "1" : "0";
        return bin;
      });
    },
    { fuentes, ayudasFuente: crearAyudas.toString(), lado: LADO_RASTER_CAMPO },
  );

  if (hoja) {
    // Hoja de contactos: cada figura en su celda con su nombre, para mirarlas.
    const columnas = 9;
    const celda = 150;
    const filas = Math.ceil(nombres.length / columnas);
    await pagina.setViewportSize({ width: columnas * celda, height: filas * (celda + 18) });
    await pagina.evaluate(
      ({ fuentes, nombres, ayudasFuente, columnas, celda }) => {
        const crear = new Function(`return (${ayudasFuente})`)();
        const lienzo = document.createElement("canvas");
        const filas = Math.ceil(fuentes.length / columnas);
        lienzo.width = columnas * celda;
        lienzo.height = filas * (celda + 18);
        document.body.appendChild(lienzo);
        const g = lienzo.getContext("2d")!;
        fuentes.forEach((fuente: string, i: number) => {
          const x = (i % columnas) * celda;
          const y = Math.floor(i / columnas) * (celda + 18);
          g.save();
          g.translate(x + 6, y + 4);
          g.scale((celda - 12) / 512, (celda - 12) / 512);
          g.strokeStyle = "#cfd3ff";
          g.fillStyle = "#cfd3ff";
          g.lineCap = "round";
          g.lineJoin = "round";
          g.lineWidth = 16;
          new Function(`return (${fuente})`)()(g, crear(g));
          g.restore();
          g.fillStyle = "#8a8fa0";
          g.font = "12px sans-serif";
          g.fillText(nombres[i], x + 6, y + celda + 12);
        });
      },
      { fuentes, nombres, ayudasFuente: crearAyudas.toString(), columnas, celda },
    );
    await pagina.screenshot({ path: hoja, fullPage: true });
  }
  await navegador.close();

  // Los campos, cuantizados a 16 bits.
  mkdirSync(DESTINO, { recursive: true });
  for (const f of readdirSync(DESTINO)) if (f.endsWith(".bin")) rmSync(path.join(DESTINO, f));
  const r = LADO_RASTER_CAMPO;
  nombres.forEach((nombre, i) => {
    const mascara = Uint8Array.from(mascaras[i], (c) => (c === "1" ? 1 : 0));
    // La caja del dibujo (en px de 512): avisa si se aleja de los ~400 px de la
    // convención, porque una caja chica engorda los trazos al escalar.
    let minX = r, minY = r, maxX = -1, maxY = -1;
    for (let y = 0; y < r; y++) for (let x = 0; x < r; x++) if (mascara[y * r + x]) {
      if (x < minX) minX = x; if (x > maxX) maxX = x; if (y < minY) minY = y; if (y > maxY) maxY = y;
    }
    const caja = (Math.max(maxX - minX + 1, maxY - minY + 1) * 512) / r;
    if (caja < 330 || caja > 440) console.warn(`  aviso: ${nombre} tiene una caja de ${caja.toFixed(0)} px`);
    const campo = campoDesdeMascara(mascara, r);
    const datos = codificarCampo(campo);
    writeFileSync(path.join(DESTINO, `${nombre}.bin`), Buffer.from(datos.buffer, datos.byteOffset, datos.byteLength));
  });

  writeFileSync(
    CATALOGO,
    `/**
 * El catálogo de figuras de la masa de la portada: ideas hechas realidad.
 * GENERADO por scripts/portada/hornear_figuras.ts a partir de
 * scripts/portada/dibujos.ts; no se edita a mano. Cada nombre tiene su campo
 * precalculado en public/portada/figuras/<nombre>.bin (${LADO_CAMPO} x ${LADO_CAMPO}, 16 bits).
 */
export const FIGURAS = [
${nombres.map((n) => `  "${n}",`).join("\n")}
] as const;

export type NombreFigura = (typeof FIGURAS)[number];
`,
  );
  console.log(`${nombres.length} figuras horneadas en ${path.relative(WEB, DESTINO)}`);
}

void main();
