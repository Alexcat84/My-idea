// Fase 3.0: verifica que los assets copiados por scripts/sync_assets_web.py
// coincidan con su manifest.json (SHA256). Si el grafo Python cambia sin
// que alguien vuelva a correr el sync, este test falla en vez de dejar
// que la web sirva un grafo desactualizado en silencio.
import { createHash } from "node:crypto";
import { readFileSync } from "node:fs";
import path from "node:path";
import { describe, expect, it } from "vitest";

const ASSETS_DIR = path.resolve(__dirname);
const manifest = JSON.parse(
  readFileSync(path.join(ASSETS_DIR, "manifest.json"), "utf-8")
) as Record<string, { sha256: string; bytes: number; fuente: string }>;

function sha256(filePath: string): string {
  return createHash("sha256").update(readFileSync(filePath)).digest("hex");
}

describe("assets sincronizados desde Python (scripts/sync_assets_web.py)", () => {
  for (const [nombre, info] of Object.entries(manifest)) {
    it(`${nombre} coincide con su checksum del manifest`, () => {
      const filePath = path.join(ASSETS_DIR, nombre);
      expect(sha256(filePath)).toBe(info.sha256);
      expect(readFileSync(filePath).length).toBe(info.bytes);
    });
  }

  it("el manifest tiene exactamente los 4 assets esperados", () => {
    expect(Object.keys(manifest).sort()).toEqual([
      "master_graph.json",
      "node_families.json",
      "preguntas_cache.json",
      "prompts.json",
    ]);
  });
});
