// checklist.test.ts — Fase 3.3. Regla AGENTS.md: los esperados de abajo se
// calcularon A MANO sobre el fixture ANTES de escribir el parser.
// Fixture: estructura real de los planes (formato verificado contra
// examples/fase2_9_plan_macetas.md y el plan de la mochila WiFi).
import { readFileSync } from "node:fs";
import path from "node:path";
import { describe, expect, it } from "vitest";
import { derivarChecklist } from "./checklist";

const PLAN = `# Título del plan: de la idea a la validación

Intro en prosa que no genera ítems. Tampoco esta línea.

---

## Etapa 1: Convierte tus suposiciones en apuestas ordenadas

Texto introductorio de la etapa, sin número: no es ítem.

1. Escribe en una hoja dos columnas: hechos comprobados y suposiciones. Todo lo demás va en la segunda columna.

2. **Identifica los saltos de fe.** De tu lista, marca los que destruyen el proyecto si son falsos.
Continuación del párrafo del paso 2 en línea nueva.

**Esta semana:** Escribe la lista y marca con rojo las tres críticas.

---

## Etapa 2: Consigue la puerta de entrada

1. Identifica a 3 profesores específicos con conexiones documentadas.

2. Prepara una presentación de máximo 20 minutos.

3. Dibuja el perfil operativo de tu usuario objetivo.

**Esta semana:** Escríbele a los 3 profesores; menos de 150 palabras.

---

## ¿Puede sostenerse tu idea? Los números en simple

Sección final sin etapas: nada de aquí genera ítems.
1. Este numeral está fuera de una Etapa y NO debe contarse...

===JSON===
{"familias_tratadas": ["accion_clientes"]}`;

// Cálculo manual: Etapa 1 → pasos 1,2 + Esta semana = 3 ítems (destacado el 3º).
// Etapa 2 → pasos 1,2,3 + Esta semana = 4 ítems (destacado el 4º).
// La sección final (## sin "Etapa") resetea a etapaActual=0: su numeral no cuenta.
// TOTAL = 7.

describe("derivarChecklist", () => {
  const items = derivarChecklist(PLAN);

  it("deriva exactamente 7 items (calculado a mano)", () => {
    expect(items).toHaveLength(7);
  });

  it("etapa 1: 2 pasos + 1 destacado 'Esta semana', en orden", () => {
    const e1 = items.filter((i) => i.etapa === 1);
    expect(e1.map((i) => i.destacado)).toEqual([false, false, true]);
    expect(e1[0].orden).toBe(1);
    expect(e1[2].texto).toContain("marca con rojo");
  });

  it("etapa 2: 3 pasos + 1 destacado", () => {
    const e2 = items.filter((i) => i.etapa === 2);
    expect(e2).toHaveLength(4);
    expect(e2.filter((i) => i.destacado)).toHaveLength(1);
  });

  it("el paso multilínea se resume a su primera oración sin markdown", () => {
    const paso2 = items.find((i) => i.etapa === 1 && i.orden === 2)!;
    expect(paso2.texto).toBe("Identifica los saltos de fe.");
    expect(paso2.texto).not.toContain("**");
  });

  it("nada fuera de '## Etapa N:' genera items (intro, secciones finales, JSON)", () => {
    expect(items.every((i) => i.etapa === 1 || i.etapa === 2)).toBe(true);
    expect(items.some((i) => i.texto.includes("fuera de una Etapa"))).toBe(false);
  });

  it("todos los textos <= 180 chars", () => {
    expect(items.every((i) => i.texto.length <= 180)).toBe(true);
  });
});

// Plan REAL (punto 5a del plan de fase): examples/fase2_9_plan_macetas.md.
// Conteo A MANO hecho ANTES de correr el parser (leyendo el archivo):
//   Etapa 1: pasos 1,2,3            + Esta semana = 4
//   Etapa 2: pasos 1,2,3 (resina) y 1,2,3 (QR)  + Esta semana = 7
//   Etapa 3: pasos 1,2,3,4,5        + Esta semana = 6
//   Etapa 4: pasos 1,2,3,4,5,6      + Esta semana = 7
//   Etapa 5: pasos 1,2,3,4,5        + Esta semana = 6
//   Sección final "## ¿Puede sostenerse tu idea?...": 0 (fuera de etapas)
//   TOTAL = 30 ítems; 5 destacados (uno por etapa); 25 pasos.
describe("derivarChecklist contra el plan real de macetas (fase 2.9)", () => {
  const md = readFileSync(
    path.resolve(__dirname, "..", "..", "..", "examples", "fase2_9_plan_macetas.md"),
    "utf-8"
  );
  const items = derivarChecklist(md);

  it("deriva exactamente 30 ítems (conteo manual)", () => {
    expect(items).toHaveLength(30);
  });

  it("exactamente 1 destacado por etapa (5 en total)", () => {
    const destacados = items.filter((i) => i.destacado);
    expect(destacados).toHaveLength(5);
    expect(new Set(destacados.map((i) => i.etapa))).toEqual(new Set([1, 2, 3, 4, 5]));
  });

  it("ítems por etapa: 4, 7, 6, 7, 6 (conteo manual)", () => {
    const porEtapa = [1, 2, 3, 4, 5].map((e) => items.filter((i) => i.etapa === e).length);
    expect(porEtapa).toEqual([4, 7, 6, 7, 6]);
  });

  it("el destacado siempre es el último orden de su etapa", () => {
    for (const etapa of [1, 2, 3, 4, 5]) {
      const deEtapa = items.filter((i) => i.etapa === etapa);
      expect(deEtapa[deEtapa.length - 1].destacado).toBe(true);
    }
  });
});
