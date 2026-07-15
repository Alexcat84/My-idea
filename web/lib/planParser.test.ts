import { describe, it, expect } from "vitest";
import { parsearSeccion } from "./planParser";

// Fase 3.9.2 (C9): el texto REAL de la seccion de numeros del plan del auditor
// HSEQ que el fundador cazo en produccion -- un parrafo denso con las etiquetas
// en negrita EN LINEA y la accion del lunes suelta al final. El respaldo de la
// UI debe rescatarlo aunque el redactor no lo emita como lista.
const NUMEROS_HSEQ_REAL = `Todavia no tienes datos reales de costos, precio ni volumen, y eso es normal en esta etapa. Pero hay numeros que necesitas definir pronto para saber si el proyecto puede financiar su propio desarrollo. Lo que debes calcular antes de terminar la Etapa 5: **Costo por iteracion del motor:** cuanto te cuesta cada ciclo de construir, medir y ajustar el motor. **Precio validado con usuarios:** el precio que un auditor senior estaria dispuesto a pagar segun la conversacion de la Etapa 5. **Punto de equilibrio minimo:** cuantos auditores pagando ese precio cubren tu costo mensual de operar el motor. **Tasa de quema actual:** cuanto estas gastando ahora en desarrollar el motor. El lunes, abre un spreadsheet con cuatro columnas: costo por ciclo, precio estimado por usuario, usuarios necesarios para cubrir costos, meses de runway disponibles.`;

describe("parsearSeccion — respaldo C9 de la seccion de numeros", () => {
  const s = parsearSeccion("¿Puede sostenerse tu idea? Los numeros en simple", NUMEROS_HSEQ_REAL);

  it("la reconoce como seccion de cierre", () => {
    expect(s.tipo).toBe("cierre");
  });

  it("parte las 4 etiquetas en linea en items con punto", () => {
    // esperado: los 4 numeros del plan real, en un solo bloque
    expect(s.bloquesPasos).toHaveLength(1);
    expect(s.bloquesPasos[0].pasos).toHaveLength(4);
    expect(s.bloquesPasos[0].pasos[0]).toContain("**Costo por iteracion del motor:**");
    expect(s.bloquesPasos[0].pasos[3]).toContain("**Tasa de quema actual:**");
  });

  it("eleva la accion del lunes suelta a la caja verde", () => {
    expect(s.estaSemana).toBeTruthy();
    expect(s.estaSemana).toMatch(/^El lunes, abre un spreadsheet/);
    // y ya no vive dentro del ultimo numero ni de la prosa
    expect(s.descripcion).not.toContain("El lunes, abre");
    expect(s.bloquesPasos[0].pasos[3]).not.toContain("El lunes, abre");
  });

  it("la prosa de contexto queda antes de los numeros, sin las etiquetas", () => {
    expect(s.descripcion).toContain("Todavia no tienes datos reales");
    expect(s.descripcion).not.toContain("**Costo por iteracion");
  });
});

describe("parsearSeccion — el respaldo NO se pasa de listo", () => {
  it("una sola nota en negrita dentro de una etapa no dispara el troceo", () => {
    const etapa = parsearSeccion(
      "Etapa 1: Define tu cliente",
      "Antes de vender necesitas saber a quien.\n\n**Nota critica:** si el costo supera al precio, es perdida real.\n\n**Entregable:** una ficha de cliente."
    );
    expect(etapa.tipo).toBe("etapa");
    expect(etapa.bloquesPasos).toHaveLength(0); // sigue siendo prosa
    expect(etapa.descripcion).toContain("**Nota critica:**");
    expect(etapa.entregable).toBe("una ficha de cliente.");
  });

  it("una etapa con dos sub-bloques de pasos los trata igual (C8)", () => {
    const etapa = parsearSeccion(
      "Etapa 2: Construye el MVP",
      "El motor minimo no es la app completa.\n\n**Pasos para construir:**\n1. Elige UNA norma.\n2. Estructura el banco.\n\n**Pasos para atacarlo:**\n- Ronda 1: casos claros.\n- Ronda 2: casos ambiguos."
    );
    expect(etapa.bloquesPasos).toHaveLength(2);
    expect(etapa.bloquesPasos[0].label).toBe("Pasos para construir");
    expect(etapa.bloquesPasos[0].pasos).toEqual(["Elige UNA norma.", "Estructura el banco."]);
    expect(etapa.bloquesPasos[1].label).toBe("Pasos para atacarlo");
    expect(etapa.bloquesPasos[1].pasos).toEqual(["Ronda 1: casos claros.", "Ronda 2: casos ambiguos."]);
  });
});
