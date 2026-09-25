// AUD-09 B14a (tanda 7A, dinero): cuando la IA no puede leer la respuesta, el
// respaldo decidía por SUBCADENAS: "playa" contiene "ya" y cortaba la
// exploración que el usuario está pagando, directo a "listo para tu plan"; lo
// mismo "ya tengo tres clientes". La regla: frases explícitas a cualquier largo;
// palabras sueltas solo enteras y en una respuesta corta (una decisión, no una
// respuesta). Paridad con engine/prototipo_motor.py (_decision_por_palabras).
import { describe, expect, it } from "vitest";
import { decisionPorPalabras } from "./recorrido";

describe("decisionPorPalabras (AUD-09 B14a)", () => {
  const casos: Array<[string, "generar_ya" | "continuar"]> = [
    ["playa", "continuar"],
    ["vendo en la playa", "continuar"],
    ["ya tengo tres clientes fijos", "continuar"],
    ["", "continuar"],
    ["ya", "generar_ya"],
    ["Listo.", "generar_ya"],
    ["ya, dale", "generar_ya"],
    ["dame mi plan ya, con esto alcanza", "generar_ya"],
    ["Así está bien", "generar_ya"],
  ];
  for (const [texto, esperado] of casos) {
    it(`"${texto}" -> ${esperado}`, () => {
      expect(decisionPorPalabras(texto)).toBe(esperado);
    });
  }
});

// i18n F5: la persona responde en el idioma de su idea. El respaldo reconoce el
// "dame mi plan" en los once (frases explícitas; en chino y japonés, sin
// espacios, la frase dentro del texto). Palabras sueltas ambiguas entre
// idiomas quedan fuera: "pronto" es "listo" en portugués e italiano pero
// "enseguida/luego" en español, y "ja" es "sí" en alemán. En la duda, seguir.
describe("decisionPorPalabras en otros idiomas (i18n F5)", () => {
  const casos: Array<[string, "generar_ya" | "continuar"]> = [
    ["Give me my plan", "generar_ya"],
    ["now", "generar_ya"],
    ["I sell now at the beach every day", "continuar"],
    ["Me dê meu plano", "generar_ya"],
    ["Donne-moi mon plan", "generar_ya"],
    ["Gib mir meinen Plan", "generar_ya"],
    ["Dammi il mio piano", "generar_ya"],
    ["プランをください", "generar_ya"],
    ["私は毎日ビーチで売っています", "continuar"],
    ["给我计划", "generar_ya"],
    ["계획 주세요", "generar_ya"],
    ["أعطني خطتي", "generar_ya"],
    ["योजना दो", "generar_ya"],
    ["pronto", "continuar"],
    ["ja", "continuar"],
  ];
  for (const [texto, esperado] of casos) {
    it(`"${texto}" -> ${esperado}`, () => {
      expect(decisionPorPalabras(texto)).toBe(esperado);
    });
  }
});
