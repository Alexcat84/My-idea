// Fase 3.0: prompts.ts debe re-exportar EXACTAMENTE lo que trae
// web/lib/assets/prompts.json (generado por scripts/sync_assets_web.py
// leyendo las constantes SYSTEM_* de prototipo_motor.py). Este test es la
// red de seguridad contra un futuro cambio que hardcodee un prompt en vez
// de re-exportarlo del JSON -- si alguna vez diverge, el prompt caching
// de Anthropic deja de coincidir con el prefijo de Python en silencio.
import { readFileSync } from "node:fs";
import path from "node:path";
import { describe, expect, it } from "vitest";
import * as prompts from "./prompts";

const promptsJsonPath = path.join(__dirname, "assets", "prompts.json");
const fuente = JSON.parse(readFileSync(promptsJsonPath, "utf-8")) as Record<string, string>;

describe("prompts.ts re-exporta byte a byte desde assets/prompts.json", () => {
  const nombres = [
    "SYSTEM_CLASIFICACION",
    "SYSTEM_PUERTA_AVANZADA",
    "SYSTEM_INTERPRETE_MULTI",
    "SYSTEM_PROFUNDIZAR",
    "SYSTEM_PREGUNTA_DIRIGIDA",
    "SYSTEM_PLAN",
    "SYSTEM_ESTADO_VIVO",
    "SYSTEM_ORGANIZADOR",
    "SYSTEM_REPORTE",
    "SYSTEM_CLASIFICAR_OFERTA",
  ] as const;

  for (const nombre of nombres) {
    it(`${nombre} es identico byte a byte a la constante Python`, () => {
      expect(prompts[nombre]).toBe(fuente[nombre]);
      expect(prompts[nombre].length).toBeGreaterThan(0);
    });
  }
});
