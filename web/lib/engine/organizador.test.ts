import { describe, expect, it } from "vitest";
import { construirMarkdown, limpiarOrganizador } from "./organizador";

/**
 * El organizador de la sesión real del fundador salió con dos guiones largos
 * pese a que SYSTEM_ORGANIZADOR ya los prohibía. La causa no era el prompt:
 * la puerta SSE llama a `client.messages.stream()` directo y se salta el
 * punto único de limpieza de `llamarClaude`. Una regla en el prompt es una
 * petición; la garantía es limpiar la salida.
 */
describe("limpiarOrganizador: la voz no depende de que el modelo obedezca", () => {
  it("quita el guion largo de la frase y de cada viñeta", () => {
    const limpio = limpiarOrganizador({
      idea_en_una_frase: "Una app para migrantes — con datos verificados",
      etapa_detectada: "ideacion",
      lo_que_ya_tienes_claro: ["Viviste el problema — de primera mano"],
      lo_que_estas_asumiendo_sin_saberlo: ["Que pagarían – sin haberlo probado"],
      areas_que_cubriria_tu_plan_completo: ["Voz del cliente"],
    });
    expect(JSON.stringify(limpio)).not.toMatch(/[—–]/);
    expect(limpio.idea_en_una_frase).toBe("Una app para migrantes, con datos verificados");
    expect(limpio.lo_que_ya_tienes_claro).toEqual(["Viviste el problema, de primera mano"]);
  });

  it("el markdown que se guarda y se muestra tampoco los lleva", () => {
    const md = construirMarkdown(
      limpiarOrganizador({
        idea_en_una_frase: "Kits de huerto — para balcones",
        etapa_detectada: "validacion",
        lo_que_ya_tienes_claro: ["Tres ventas reales — a amigos"],
        lo_que_estas_asumiendo_sin_saberlo: [],
        areas_que_cubriria_tu_plan_completo: [],
      })
    );
    expect(md).not.toMatch(/[—–]/);
    expect(md).toContain("# Organizador de tu idea");
  });

  it("un texto ya limpio pasa intacto", () => {
    const data = {
      idea_en_una_frase: "Kits de huerto para balcones",
      etapa_detectada: "validacion",
      lo_que_ya_tienes_claro: ["Tres ventas reales"],
      lo_que_estas_asumiendo_sin_saberlo: ["Que un desconocido pagaría"],
      areas_que_cubriria_tu_plan_completo: ["Voz del cliente"],
    };
    expect(limpiarOrganizador(data)).toEqual(data);
  });

  it("aguanta los campos ausentes sin romperse", () => {
    expect(() => construirMarkdown(limpiarOrganizador({}))).not.toThrow();
  });
});
