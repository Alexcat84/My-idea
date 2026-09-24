// El dictado llegaba al tope de 4000 caracteres con poco hablado (reporte del
// fundador, 26 sep 2026): el texto se DUPLICABA solo. Chrome, sobre todo en
// Android, no siempre entrega los resultados como el estándar: (A) reenvía en
// cada evento las frases ya cerradas (resultIndex se queda en 0 y la lista
// crece), o (B) entrega cada frase final ACUMULANDO las anteriores. El código
// las volvía a pegar. leerResultados entrega cada cosa una sola vez.
import { describe, expect, it } from "vitest";
import { estadoVozInicial, leerResultados } from "./useSpeech";
import { fusionarDictado } from "./fusionarDictado";

type R = { isFinal: boolean; transcript: string };
const f = (t: string): R => ({ isFinal: true, transcript: t });
const i = (t: string): R => ({ isFinal: false, transcript: t });

/** Pasa una secuencia de eventos del reconocedor por leerResultados y
 * fusionarDictado, como lo hace el campo, y devuelve el texto final. */
function dictar(eventos: Array<{ results: R[]; resultIndex: number }>): string {
  let estado = estadoVozInicial();
  let valor = "";
  let sufijo = "";
  for (const e of eventos) {
    const r = leerResultados(e.results, e.resultIndex, estado);
    estado = r.estado;
    const fu = fusionarDictado(valor, sufijo, r.nuevoFinal, r.provisional);
    valor = fu.valor;
    sufijo = fu.sufijo;
  }
  return valor;
}

describe("el dictado no se duplica, en ningún navegador", () => {
  it("el estándar (escritorio): resultIndex avanza", () => {
    expect(
      dictar([
        { results: [i("hola")], resultIndex: 0 },
        { results: [f("hola qué tal")], resultIndex: 0 },
        { results: [f("hola qué tal"), i("vendo")], resultIndex: 1 },
        { results: [f("hola qué tal"), f("vendo pan")], resultIndex: 1 },
      ])
    ).toBe("hola qué tal vendo pan");
  });

  it("(A) resultIndex se queda en 0 y la lista crece", () => {
    expect(
      dictar([
        { results: [f("hola qué tal")], resultIndex: 0 },
        { results: [f("hola qué tal"), i("vendo")], resultIndex: 0 },
        { results: [f("hola qué tal"), f("vendo pan")], resultIndex: 0 },
        { results: [f("hola qué tal"), f("vendo pan"), f("de masa madre")], resultIndex: 0 },
      ])
    ).toBe("hola qué tal vendo pan de masa madre");
  });

  it("(B) cada frase final acumula las anteriores", () => {
    expect(
      dictar([
        { results: [f("hola")], resultIndex: 0 },
        { results: [f("hola"), i("hola qué")], resultIndex: 1 },
        { results: [f("hola"), f("hola qué tal")], resultIndex: 1 },
        { results: [f("hola"), f("hola qué tal"), f("hola qué tal vendo pan")], resultIndex: 2 },
      ])
    ).toBe("hola qué tal vendo pan");
  });
});
