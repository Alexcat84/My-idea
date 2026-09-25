// AUD-09 M33 (tanda 7B, confianza; decisión del fundador 25 sep 2026): el plan
// cerraba con "Para profundizar, continua la conversacion en esta misma
// sesion", cuando la sesión ya está cerrada (y sin tildes), y lo que falta
// cubrir decía "MVP". Fuera la invitación a una sesión cerrada; "MVP" en español
// llano; tildes. Una sola fuente de esos textos (constants.ts) y paridad con el
// prototipo Python.
import { readFileSync } from "node:fs";
import path from "node:path";
import { describe, expect, it } from "vitest";
import { TEXTO_FAMILIA_FALTANTE } from "./constants";
import { MOTOR_PLAN } from "../i18n/mensajes/motorPlan";
import { evaluarRuta } from "../readiness";

const leer = (rel: string) => readFileSync(path.join(__dirname, "..", "..", rel), "utf8");
const redactor = leer("lib/engine/planRedactor.ts");
// i18n F2: los textos del redactor viven en su catálogo.
const catalogoRedactor = leer("lib/i18n/mensajes/motorPlan.ts");
const readiness = leer("lib/readiness.ts");
const pyReadiness = leer("../engine/plan_readiness.py");
const pyMotor = leer("../engine/prototipo_motor.py");

describe("el cierre del plan no invita a una sesión cerrada (AUD-09 M33)", () => {
  it("sin la invitación a continuar en la misma sesión", () => {
    expect(redactor).not.toMatch(/continua la conversacion/);
    expect(catalogoRedactor).not.toMatch(/continua la conversacion/);
    expect(MOTOR_PLAN.es.noCubre).toBe("## Lo que este plan aún no cubre");
    expect(redactor).toMatch(/partes\.push\("", t\.noCubre, ""\)/);
  });

  it("lo que falta cubrir, en español llano y con tildes", () => {
    expect(TEXTO_FAMILIA_FALTANTE.accion_clientes).toBe(
      "validar con clientes reales (conversaciones, una primera versión sencilla de tu producto, pruebas con usuarios, una venta o preventa real)"
    );
    expect(TEXTO_FAMILIA_FALTANTE.viabilidad_economica).toBe(
      "si tu idea puede sostenerse económicamente (costos, precios, punto de equilibrio)"
    );
    expect(TEXTO_FAMILIA_FALTANTE.profundidad).toBe("más profundidad en el recorrido");
  });

  it("readiness usa esos mismos textos (una sola fuente)", () => {
    // i18n: readiness elige los textos por idioma de la misma fuente.
    expect(readiness).toMatch(/textosFamiliaFaltante\(idioma\)/);
    expect(readiness).toMatch(/texto\.accion_clientes/);
    expect(evaluarRuta([], {}).familias_faltantes).toEqual([
      TEXTO_FAMILIA_FALTANTE.accion_clientes,
      TEXTO_FAMILIA_FALTANTE.viabilidad_economica,
      TEXTO_FAMILIA_FALTANTE.profundidad,
    ]);
    expect(readiness).not.toMatch(/MVP/);
  });

  it("paridad con el prototipo Python", () => {
    for (const t of Object.values(TEXTO_FAMILIA_FALTANTE)) {
      expect(pyReadiness + pyMotor).toContain(t);
    }
    expect(pyReadiness).not.toMatch(/MVP/);
  });
});
