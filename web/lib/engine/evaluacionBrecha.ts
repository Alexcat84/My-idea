/**
 * evaluacionBrecha.ts — Fase 3.5: al activar un mundo, elegir la semilla
 * de entrada del pack. DETERMINÍSTICA (cero llamadas LLM, requisito del
 * plan): puntúa las entry_seeds aprobadas del dominio (P1-HSEQ) contra
 * el estado vivo del proyecto + tipo de oferta + fase actual — el mismo
 * esquema de puntaje que candidatos_seguimiento (fase +5/+3, afinidad
 * de tokens +1 c/u), sobre el asset horneado packs_entry_seeds.json
 * (id, titulo, fase, condiciones de cada semilla; los nodos completos
 * llegan al grafo con la línea de ensamblaje).
 */
import seedsJson from "../assets/packs_entry_seeds.json";
import { tokensCosecha } from "./tokens";

export interface SemillaPack {
  id: string;
  titulo: string;
  fase: string | null;
  condiciones: string[];
}

const ORDEN_FASES: Record<string, number> = { ideacion: 0, validacion: 1, planificacion: 2, ejecucion: 3 };

export function semillasDelPack(pack: string): SemillaPack[] {
  return ((seedsJson as Record<string, SemillaPack[]>)[pack] ?? []);
}

export interface ResultadoBrecha {
  semillaId: string;
  puntaje: number;
  razonamiento: string;
}

export function evaluacionBrecha(
  pack: string,
  estadoVivo: string | null,
  tipoOferta: string | null,
  faseActual: string,
  cubiertos: Set<string> = new Set()
): ResultadoBrecha | null {
  const semillas = semillasDelPack(pack).filter((s) => !cubiertos.has(s.id));
  if (semillas.length === 0) return null;

  const faseIdx = ORDEN_FASES[faseActual] ?? 0;
  const contexto = tokensCosecha(`${estadoVivo ?? ""} ${tipoOferta ?? ""}`);

  let mejor = semillas[0];
  let mejorPuntaje = -1;
  for (const s of semillas) {
    let p = 0;
    const fNodo = ORDEN_FASES[s.fase ?? ""] ?? 0;
    if (fNodo === faseIdx) p += 5;
    else if (fNodo === faseIdx + 1) p += 3;
    if (contexto.size > 0) {
      const textoSemilla = `${s.titulo} ${s.condiciones.join(" ")}`;
      for (const t of tokensCosecha(textoSemilla)) if (contexto.has(t)) p += 1;
    }
    if (p > mejorPuntaje) {
      mejorPuntaje = p;
      mejor = s;
    }
  }
  return {
    semillaId: mejor.id,
    puntaje: mejorPuntaje,
    razonamiento: `semilla '${mejor.titulo}' (fase ${mejor.fase ?? "?"} vs proyecto ${faseActual}, puntaje ${mejorPuntaje})`,
  };
}
