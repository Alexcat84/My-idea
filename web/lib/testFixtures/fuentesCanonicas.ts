/**
 * SOLO PARA PRUEBAS: los titulos de la lista canonica de fuentes (dataset/metadata/fuentes_canonicas.json),
 * leidos del disco. La lista NO se copia a la web: es metadato interno (REGLA ESTRICTA del fundador,
 * 26 sep 2026). Las guardas la usan para exigir que ningun titulo llegue al cliente.
 */
import { readFileSync } from "node:fs";
import path from "node:path";

const CANON = path.resolve(__dirname, "../../../dataset/metadata/fuentes_canonicas.json");

export function normal(s: string): string {
  return s.normalize("NFKD").replace(/[̀-ͯ]/g, "").replace(/[‘’]/g, "'").replace(/\s+/g, " ").toLowerCase();
}

export function titulosCanonicos(): string[] {
  const canon = JSON.parse(readFileSync(CANON, "utf-8")) as { fuentes: Record<string, { titulos: string[] }> };
  return [...new Set(Object.values(canon.fuentes).flatMap((f) => f.titulos).map(normal))];
}

export function titulosEn(texto: string, titulos: string[]): string[] {
  const bajo = normal(texto);
  const escapar = (t: string) => t.replace(/[.*+?^$|()[\]{}\\]/g, "\\$&");
  return titulos.filter((t) => new RegExp("(?<![a-z0-9])" + escapar(t) + "(?![a-z0-9])").test(bajo));
}
