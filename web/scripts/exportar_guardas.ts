// Vuelca las guardas de contenido a dataset/metadata/guardas_contenido.json (ver lib/guardasContenido.ts).
// Uso (desde web/): npx tsx scripts/exportar_guardas.ts
import { writeFileSync } from "node:fs";
import path from "node:path";
import { guardasContenido } from "../lib/guardasContenido";

const raiz = path.resolve(import.meta.dirname, "..", "..");
const destino = path.join(raiz, "dataset", "metadata", "guardas_contenido.json");
writeFileSync(destino, JSON.stringify(guardasContenido(raiz), null, 1) + "\n", "utf8");
console.log(`escrito: ${destino}`);
