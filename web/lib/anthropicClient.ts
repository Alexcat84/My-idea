/**
 * Fase 3.0: cliente Anthropic compartido por las rutas de API. Server-side
 * only -- ANTHROPIC_API_KEY nunca debe llegar al bundle del navegador.
 */
import Anthropic from "@anthropic-ai/sdk";

let cached: Anthropic | null = null;

export function createAnthropicClient(): Anthropic {
  if (cached) return cached;
  cached = new Anthropic({ apiKey: process.env.ANTHROPIC_API_KEY });
  return cached;
}
