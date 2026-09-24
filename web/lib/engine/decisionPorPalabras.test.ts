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
