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

/** Los autores de la lista canonica, tal cual (con mayuscula): un apellido es nombre propio, no palabra comun. */
export function autoresCanonicos(): string[] {
  const canon = JSON.parse(readFileSync(CANON, "utf-8")) as { fuentes: Record<string, { autores?: string[] }> };
  return [...new Set(Object.values(canon.fuentes).flatMap((f) => f.autores ?? []))];
}

/** Coincidencias con un apellido de la lista que no son el autor (las mismas de scripts/origen_ia.py). */
export const EXCEPCIONES_AUTOR = ["MINI Cooper"];

/** Los autores canonicos que aparecen en el texto como nombre propio (palabra entera, con mayuscula). */
export function autoresEn(texto: string, autores: string[]): string[] {
  let t = texto;
  for (const e of EXCEPCIONES_AUTOR) t = t.split(e).join(" ");
  const escapar = (s: string) => s.replace(/[.*+?^$|()[\]{}\\]/g, "\\$&");
  return autores.filter((a) => t.includes(a) && new RegExp("(?<![\\p{L}\\p{N}_-])" + escapar(a) + "(?![\\p{L}\\p{N}_-])", "u").test(t));
}

const PATRONES = new Map<string, RegExp>();

export function titulosEn(texto: string, titulos: string[]): string[] {
  const bajo = normal(texto);
  const escapar = (t: string) => t.replace(/[.*+?^$|()[\]{}\\]/g, "\\$&");
  return titulos.filter((t) => {
    // filtro literal barato antes del patron con limites de palabra: mismo veredicto, sin compilar un patron por texto
    if (!bajo.includes(t)) return false;
    let re = PATRONES.get(t);
    if (!re) PATRONES.set(t, (re = new RegExp("(?<![a-z0-9])" + escapar(t) + "(?![a-z0-9])")));
    return re.test(bajo);
  });
}
