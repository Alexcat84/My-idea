// TOPE DE TEXTO DE LA IDEA (decisión del fundador 2, 27 sep 2026): sube de
// 4.000 a 12.000 caracteres, con el mensaje honesto de límite si se supera. El
// fundador dicta ideas ricas y 4.000 (una página carta) se quedaba corto.
// Solo la IDEA: las respuestas de la exploración siguen en 4.000, porque cada
// respuesta se arrastra en todas las llamadas siguientes de la sesión (la idea
// entra una vez y luego se lee de caché a una décima del precio).
import { readFileSync } from "node:fs";
import path from "node:path";
import { describe, expect, it, vi } from "vitest";
import { MAX_LARGO_IDEA, MAX_LARGO_TEXTO_USUARIO, MENSAJE_IDEA_LARGA } from "./constants";
import { componerDictado, estadoDictadoInicial, textoDeSesion } from "./dictado";

vi.mock("@/lib/supabase/server", () => ({
  createClient: async () => ({ auth: { getUser: async () => ({ data: { user: null } }) } }),
}));

/** Un dictado largo como lo arma el campo: una sesión del micrófono por frase. */
function dictadoLargo(frases: number): string {
  const frase =
    "quiero abrir una panadería de barrio con pan de masa madre, repartir en bicicleta y vender por internet a las oficinas de la zona";
  let valor = "";
  for (let k = 0; k < frases; k++) {
    const estado = estadoDictadoInicial();
    valor = componerDictado(valor, estado, textoDeSesion([{ isFinal: true, transcript: `${frase} ${k + 1}` }])).valor;
  }
  return valor;
}

const cuerpo = (texto: string) =>
  new Request("http://test", { method: "POST", body: JSON.stringify({ texto }), headers: { "Content-Type": "application/json" } });

describe("la idea admite 12.000 caracteres", () => {
  it("el tope de la idea es 12.000 y el de las respuestas sigue en 4.000", () => {
    expect(MAX_LARGO_IDEA).toBe(12_000);
    expect(MAX_LARGO_TEXTO_USUARIO).toBe(4_000);
  });

  it("el mensaje de límite dice su número, en palabras de persona", () => {
    expect(MENSAJE_IDEA_LARGA).toBe("Tu idea pasa de 12.000 caracteres. Recórtala un poco y seguimos.");
  });

  it("un dictado largo (unas 11.000 letras) llega entero y sin repetirse", () => {
    // A mano: la frase tiene 129 caracteres y lleva " k" al final: 131 para
    // k = 1..9 y 132 para k = 10..85; más 84 espacios entre frases.
    // 9 × 131 + 76 × 132 + 84 = 1179 + 10032 + 84 = 11295
    const texto = dictadoLargo(85);
    expect(texto.length).toBe(11_295);
    expect(texto.length).toBeGreaterThan(MAX_LARGO_TEXTO_USUARIO);
    expect(texto.length).toBeLessThan(MAX_LARGO_IDEA);
    expect(texto.split("panadería de barrio").length - 1).toBe(85);
  });

  it("ordenar la idea: el dictado largo pasa el tope y 12.001 caracteres se rechazan con su número", { timeout: 30_000 }, async () => {
    const { POST } = await import("@/app/api/organizer/stream/route");
    // pasa el tope y sigue hasta la sesión (401: el doble de prueba no tiene usuario)
    expect((await POST(cuerpo(dictadoLargo(85)))).status).toBe(401);
    const largo = await POST(cuerpo("a".repeat(MAX_LARGO_IDEA + 1)));
    expect(largo.status).toBe(400);
    expect(await largo.json()).toEqual({ error: MENSAJE_IDEA_LARGA, limite: MAX_LARGO_IDEA });
  });

  it("empezar la exploración: igual", { timeout: 30_000 }, async () => {
    const { POST } = await import("@/app/api/session/start/route");
    expect((await POST(cuerpo(dictadoLargo(85)))).status).toBe(401);
    const largo = await POST(cuerpo("a".repeat(MAX_LARGO_IDEA + 1)));
    expect(largo.status).toBe(400);
    expect(await largo.json()).toEqual({ error: MENSAJE_IDEA_LARGA, limite: MAX_LARGO_IDEA });
  });

  it("la pantalla de la idea nueva y el organizador JSON usan el tope de la idea; las respuestas, el suyo", () => {
    const leer = (r: string) => readFileSync(path.join(__dirname, "..", r), "utf8");
    for (const r of ["app/nueva/page.tsx", "app/api/organizer/route.ts"]) {
      expect(leer(r)).toMatch(/MAX_LARGO_IDEA/);
      expect(leer(r)).not.toMatch(/MAX_LARGO_TEXTO_USUARIO/);
    }
    expect(leer("app/api/session/[id]/turn/route.ts")).toMatch(/respuesta\.length > MAX_LARGO_TEXTO_USUARIO/);
  });
});
