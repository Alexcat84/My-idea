// UPSTASH CAÍDO en las rutas de la IA (decisión del fundador, 25 sep 2026):
// con la base del contador caída, cada ruta que arranca trabajo de la IA
// responde 503 con el mensaje claro ("servicio temporalmente no disponible, no
// se te cobró nada") y suelta la reserva de créditos: cero cobros.
import { readFileSync } from "node:fs";
import path from "node:path";
import { describe, expect, it } from "vitest";

const RUTAS = [
  "organizer/route.ts",
  "organizer/stream/route.ts",
  // Ciclo de replanteamiento, Fase 2: las puertas del follow y de replantear
  // viven en un solo sitio, lib/cicloApertura.ts (ver la prueba de abajo).
  "../../lib/cicloApertura.ts",
  "project/[id]/report/route.ts",
  "project/[id]/world/[pack]/start/route.ts",
  "session/start/route.ts",
  "session/[id]/regenerar/route.ts",
];

describe("cada ruta de la IA distingue la base caída del tope alcanzado", () => {
  it.each(RUTAS)("%s: fusible y límite responden con el mensaje de servicio no disponible si la base cayó", (ruta) => {
    const src = readFileSync(path.join(__dirname, ruta), "utf8");
    expect(src).toMatch(/fusible\.caido \? mensajeServicioNoDisponible\(idioma\) : mensajeFusible\(idioma\)/);
    expect(src).toMatch(/limite\.caido \? mensajeServicioNoDisponible\(idioma\) : mensajeLimite\(limite\.limite, idioma\)/);
    expect(src).toMatch(/limite\.caido \? 503 : 429/);
  });

  it.each(["project/[id]/follow/route.ts", "project/[id]/replantear/route.ts"])(
    "%s: abre el ciclo por lib/cicloApertura (las mismas puertas)",
    (ruta) => {
      const src = readFileSync(path.join(__dirname, ruta), "utf8");
      expect(src).toMatch(/await abrirCiclo\(/);
    }
  );
});
