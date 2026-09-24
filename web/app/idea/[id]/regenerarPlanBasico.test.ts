// AUD-09, decisiones del fundador (25 sep 2026): el plan básico se puede
// regenerar (sesión nueva, se cobra solo si la IA entrega) y un plan básico de
// mundo NO es una compra: el mundo ofrece "Generar el plan completo".
import { readFileSync } from "node:fs";
import path from "node:path";
import { describe, expect, it } from "vitest";
import { estadoMundo } from "@/lib/engine/previewMundos";
import { AVISO_VERSION_BASICA } from "@/lib/engine/planRedactor";

const app = path.join(__dirname, "..", "..");
const leer = (rel: string) => readFileSync(path.join(app, rel), "utf8");

describe("el plan básico de un mundo no es una compra", () => {
  it("estadoMundo: con plan básico y sin pago, el estado es plan_basico", () => {
    expect(estadoMundo({ resumen_md: "d", resumen_at: "t", plan_basico_at: "t2", plan_pagado_at: null }, true)).toBe(
      "plan_basico"
    );
  });
  it("estadoMundo: si después se pagó el completo, manda el pago", () => {
    expect(estadoMundo({ plan_basico_at: "t1", plan_pagado_at: "t2" }, true)).toBe("plan_comprado");
  });
  it("/api/idea entrega la marca del plan básico y la sesión de cada plan", () => {
    const ruta = leer("api/idea/[id]/route.ts");
    expect(ruta).toMatch(/plan_basico_at: u\.plan_basico_at \?\? null/);
    expect(ruta).toMatch(/session_id: planMundo\.session_id/);
    expect(ruta).toMatch(/session_id: plan\.session_id/);
  });
  it("el espacio del mundo ofrece Generar el plan completo, apuntando a la regeneración", () => {
    const manos = leer("ui/ManosALaObra.tsx");
    expect(manos).toContain("Generar el plan completo");
    expect(manos).toMatch(/onRegenerarPlanMundo\(/);
  });
});

describe("el plan básico del núcleo se puede regenerar", () => {
  it("el aviso ya promete la regeneración", () => {
    expect(AVISO_VERSION_BASICA).toMatch(/regenerar/i);
    expect(AVISO_VERSION_BASICA).toMatch(/solo se cobra si/i);
  });
  it("IdeaView ofrece regenerar junto al aviso y llama a la ruta de regeneración", () => {
    const vista = leer("idea/[id]/IdeaView.tsx");
    expect(vista).toMatch(/\/regenerar`/);
    expect(vista).toMatch(/Regenerar mi plan · \$\{/);
  });
});
