/**
 * La vigencia de las etiquetas traducidas del riel (decisión del fundador,
 * 25 sep 2026). Cada traducción guarda la huella del texto español del que
 * salió; si el español cambia, la huella deja de coincidir y la traducción está
 * VENCIDA hasta que se vuelva a traducir. Lo usan la guardia
 * (etiquetasVigencia.test.ts) y la herramienta scripts/i18n/etiquetasRiel.ts
 * (exporta las que faltan y las vencidas; al aplicar, guarda la huella nueva).
 */
import { createHash } from "node:crypto";

/** La huella de un texto español: los 12 primeros hex de su SHA-256 (sin espacios en los extremos). */
export function huellaDe(texto: string): string {
  return createHash("sha256").update(texto.trim(), "utf8").digest("hex").slice(0, 12);
}

/** Los ids cuya traducción no salió del español vigente (sin huella o con otra huella). */
export function etiquetasVencidas(vivos: Record<string, string>, huellas: Record<string, string>): string[] {
  return Object.entries(vivos)
    .filter(([id, espanol]) => huellas[id] !== huellaDe(espanol))
    .map(([id]) => id)
    .sort();
}
