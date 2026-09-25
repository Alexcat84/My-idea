// El dictado llegaba al tope de 4000 caracteres con poco hablado (reporte del
// fundador, 26 sep 2026, Samsung S23 con Chrome): el texto se DUPLICABA solo.
// La copia que pegó el fundador mostró el patrón: Chrome en Android manda cada
// frase como una versión FINAL nueva que crece ("…probablemente", luego
// "…probablemente en", luego "…en algún"), a veces la reinicia desde la mitad
// de la anterior y a veces cambia un acento o una mayúscula ("este"/"esté").
// El primer arreglo (web-v2.6.7) solo esperaba repeticiones desde el inicio de
// la sesión, así que cada versión se pegaba entera. Ahora: (1) cada evento se
// lee entero y las versiones de una misma frase se funden en la más reciente;
// (2) cada sesión del micrófono REEMPLAZA su propio aporte en el campo, nunca
// lo pega. Resultados esperados calculados a mano en cada caso.
import { describe, expect, it } from "vitest";
import { alEditarAMano, componerDictado, estadoDictadoInicial, textoDeSesion, type ResultadoVoz } from "./dictado";

const f = (t: string): ResultadoVoz => ({ isFinal: true, transcript: t });
const i = (t: string): ResultadoVoz => ({ isFinal: false, transcript: t });

type Paso = "sesion" | ResultadoVoz[] | ((valor: string) => string);

/** Simula el campo como lo hace CampoConVoz: "sesion" arranca o reanuda el
 * micrófono, una lista es un evento del reconocedor (e.results entero) y una
 * función es el usuario editando a mano. */
function campo(pasos: Paso[], inicial = ""): string {
  let valor = inicial;
  let estado = estadoDictadoInicial();
  let ultimo = "";
  for (const p of pasos) {
    if (p === "sesion") {
      estado = estadoDictadoInicial();
      ultimo = "";
    } else if (Array.isArray(p)) {
      ultimo = textoDeSesion(p);
      const r = componerDictado(valor, estado, ultimo);
      valor = r.valor;
      estado = r.estado;
    } else {
      const v = p(valor);
      if (v === valor) continue; // eco del teclado: nada cambió
      estado = alEditarAMano(v, estado, ultimo);
      valor = v;
    }
  }
  return valor;
}

describe("el patrón real del S23 (estructura de la copia del fundador, otro contenido)", () => {
  // Cada versión llega como un final NUEVO y la lista crece evento a evento.
  const versiones = [
    "te cuento tengo una idea de abrir una panaderia de barrio",
    // la misma frase, crecida y con el acento corregido
    "te cuento tengo una idea de abrir una panadería de barrio pero pequeña además quiero vender por internet y repartir en bicicleta rápido",
    // reinicia desde la mitad, y más corta que lo que ya había (reenvío viejo)
    "quiero vender por internet y repartir en bicicleta",
    "quiero vender por internet y repartir en bicicleta rápido y barato",
    // una mayúscula cambia
    "quiero vender por Internet y repartir en bicicleta rápido y barato para empresas",
    "para empresas de la zona que esté cerca",
    // un acento se pierde y vuelve
    "para empresas de la zona que este cerca del centro",
    "para empresas de la zona que esté cerca del centro",
  ];
  // A mano: la frase 1 queda hasta "además", la 2 (la de "quiero") hasta
  // "barato", y la 3 (la de "para empresas") en su última forma:
  const esperado =
    "te cuento tengo una idea de abrir una panadería de barrio pero pequeña además " +
    "quiero vender por Internet y repartir en bicicleta rápido y barato " +
    "para empresas de la zona que esté cerca del centro";

  it("una sola sesión larga (continua): cada frase una vez", () => {
    const pasos: Paso[] = ["sesion"];
    for (let k = 1; k <= versiones.length; k++) pasos.push(versiones.slice(0, k).map(f));
    expect(campo(pasos)).toBe(esperado);
  });
});

describe("el dictado no se duplica, lo mande como lo mande el navegador", () => {
  it("el estándar (escritorio): la frase cerrada y la siguiente", () => {
    // "hola qué tal" + "vendo pan" = "hola qué tal vendo pan"
    expect(
      campo(["sesion", [i("hola")], [f("hola qué tal")], [f("hola qué tal"), i("vendo")], [f("hola qué tal"), f("vendo pan")]])
    ).toBe("hola qué tal vendo pan");
  });

  it("cada frase final acumula las anteriores", () => {
    // la última lista ya trae todo: "hola qué tal vendo pan", una sola vez
    expect(
      campo([
        "sesion",
        [f("hola")],
        [f("hola"), i("hola qué")],
        [f("hola"), f("hola qué tal")],
        [f("hola"), f("hola qué tal"), f("hola qué tal vendo pan")],
      ])
    ).toBe("hola qué tal vendo pan");
  });

  it("reenvía la misma frase con otra puntuación o mayúsculas", () => {
    // "Hola qué tal" y "hola, qué tal." son la misma frase: queda la última forma
    expect(campo(["sesion", [f("Hola qué tal")], [f("Hola qué tal"), f("hola, qué tal.")]])).toBe("hola, qué tal.");
  });

  it("la misma frase final llega diez veces", () => {
    const pasos: Paso[] = ["sesion"];
    for (let k = 0; k < 10; k++) pasos.push([f("vendo pan de masa madre")]);
    expect(campo(pasos)).toBe("vendo pan de masa madre");
  });

  it("una frase que crece palabra por palabra en muchos eventos", () => {
    // 1 evento por palabra (provisional) y el final: la frase una vez
    const frase = "quiero abrir una panadería de barrio con pan de masa madre";
    const palabras = frase.split(" ");
    const pasos: Paso[] = ["sesion"];
    for (let k = 1; k <= palabras.length; k++) pasos.push([i(palabras.slice(0, k).join(" "))]);
    pasos.push([f(frase)]);
    expect(campo(pasos)).toBe(frase);
  });

  it("varias sesiones seguidas se suman, una frase cada una", () => {
    // "tengo una panadería" + "en Montreal"
    expect(
      campo(["sesion", [i("tengo una")], [f("tengo una panadería")], "sesion", [i("en")], [f("en Montreal")]])
    ).toBe("tengo una panadería en Montreal");
  });

  it("respeta lo que ya estaba escrito", () => {
    // "tengo" + la sesión "dos clientes y" = "tengo dos clientes y"
    expect(campo(["sesion", [i("dos")], [f("dos clientes"), i("y")]], "tengo")).toBe("tengo dos clientes y");
  });

  it("lo provisional ya está en el campo: detener a mitad de frase no lo pierde", () => {
    // la sesión 1 quedó en "hola" (provisional); la 2 dice "adiós"
    expect(campo(["sesion", [i("hola")], "sesion", [f("adiós")]])).toBe("hola adiós");
  });
});

describe("editar a mano mientras se dicta no duplica ni borra", () => {
  it("editar lejos del final: el dictado sigue reemplazando su parte", () => {
    // "Idea: vendo" → "Mi idea: vendo" (lo dictado sigue al final) → final "vendo pan"
    expect(
      campo(["sesion", [i("vendo")], (v) => v.replace("Idea:", "Mi idea:"), [f("vendo pan")]], "Idea:")
    ).toBe("Mi idea: vendo pan");
  });

  it("escribir al final: lo ya dicho no se vuelve a pegar, solo lo nuevo", () => {
    // "vendo pan" + tecleado " rico"; la sesión sigue: "vendo pan de masa"
    // lo ya colocado son 2 palabras ("vendo pan"); lo nuevo es "de masa"
    // = "vendo pan rico de masa"
    expect(campo(["sesion", [i("vendo pan")], (v) => v + " rico", [f("vendo pan de masa")]])).toBe("vendo pan rico de masa");
  });

  it("borrar lo dictado: no reaparece", () => {
    // "vendo pan" borrado entero; la sesión sigue con "vendo pan barato": solo "barato"
    expect(campo(["sesion", [i("vendo pan")], () => "", [f("vendo pan barato")]])).toBe("barato");
  });
});

describe("textoDeSesion", () => {
  it("frases distintas se unen con un espacio", () => {
    expect(textoDeSesion([f("hola qué tal "), f(" vendo pan")])).toBe("hola qué tal vendo pan");
  });
  it("una sola palabra que repite el principio de lo anterior se conserva", () => {
    // "no sé" y luego "no": son dos cosas dichas
    expect(textoDeSesion([f("no sé"), f("no")])).toBe("no sé no");
  });
  it("una repetición más corta de lo ya dicho se ignora", () => {
    // "hola qué tal" ya contiene "hola qué"
    expect(textoDeSesion([f("hola qué tal"), i("hola qué")])).toBe("hola qué tal");
  });
  it("repetir una expresión a propósito no borra lo que había entre medio", () => {
    // "en tiempo real y además" vs "en tiempo real con gafas": 3 de 5 palabras
    // coinciden (menos del 70 %): es frase nueva, se suma
    expect(textoDeSesion([f("lo veo en tiempo real y además"), f("en tiempo real con gafas")])).toBe(
      "lo veo en tiempo real y además en tiempo real con gafas"
    );
  });
  it("sin resultados, nada", () => {
    expect(textoDeSesion([])).toBe("");
  });
});
