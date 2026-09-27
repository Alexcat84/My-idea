// i18n F6: la elisión del italiano ante una cifra (decisión del fundador del
// 25 sep 2026: "l'8 marzo", no "il 8 marzo").
//
// LA REGLA (gramática italiana): el artículo "il" y las preposiciones
// articuladas que lo contienen (dal, al, del, nel, sul) se ELIDEN ante una
// palabra que empieza por vocal: il → l', dal → dall', al → all', del → dell',
// nel → nell', sul → sull'. Ante una cifra manda cómo SE LEE la cifra:
//   - 8 "otto", 11 "undici", 80-89 "ottanta…", 800-899 "ottocento…",
//     8.000-8.999 "ottomila…", 11.000-11.999 "undicimila…" empiezan por vocal:
//     se elide ("l'8 marzo", "dall'11 aprile", "l'80%", "l'11.000").
//   - Todo lo demás empieza por consonante: 1 "uno" se lee "primo" en una fecha
//     y se escribe "1º" ("il 1º marzo", sin elisión), 9 "nove", 18 "diciotto",
//     110 "centodieci", 1100 "millecento", 2026 "duemilaventisei": sin elisión.
//   En general: la parte entera (sin los puntos de miles) empieza por 8, o
//   empieza por 11 y tiene 2, 5, 8… cifras (undici, undicimila, undici milioni).
// Solo en italiano: el español "del 8 al 11" no se toca.
//
// Cada caso de abajo está contado a mano con esa regla (AGENTS.md: el valor
// esperado sale del cálculo manual, no de la función).
import { describe, expect, it } from "vitest";
import { elidir, interpolarEn } from "./elision";
import { fechaHumanaConAno, fechaHumanaCorta } from "../fechas";

describe("elidir (italiano): el artículo ante una cifra que suena a vocal", () => {
  it.each([
    // 8 "otto" → il 8 = l'8
    ["Chiusa il 8 marzo 2026", "Chiusa l'8 marzo 2026"],
    // 11 "undici" → l'11
    ["fatta il 11 aprile 2026", "fatta l'11 aprile 2026"],
    // dal → dall', al → all'
    ["Dal 8 marzo al 11 aprile", "Dall'8 marzo all'11 aprile"],
    ["dal 8 marzo al 11 aprile", "dall'8 marzo all'11 aprile"],
    // del → dell', nel → nell', sul → sull'
    ["i tuoi numeri del 8 marzo", "i tuoi numeri dell'8 marzo"],
    ["nel 8 per cento dei casi", "nell'8 per cento dei casi"],
    ["sul 80% delle vendite", "sull'80% delle vendite"],
    // la mayúscula del artículo al empezar la frase se conserva
    ["Il 8 marzo", "L'8 marzo"],
    ["Del 11 marzo", "Dell'11 marzo"],
    // 80-89 "ottanta…": 81 = ottantuno
    ["il 81", "l'81"],
    // 800 "ottocento"
    ["il 800", "l'800"],
    // 11.000 "undicimila" (5 cifras sin el punto)
    ["il 11.000", "l'11.000"],
    // 8.000 "ottomila"
    ["il 8.000", "l'8.000"],
    // 8,5 "otto virgola cinque"
    ["il 8,5%", "l'8,5%"],
    // dentro de un enlace-centinela del Expediente
    ["[fatta il 8 marzo 2026](#f-hecho)", "[fatta l'8 marzo 2026](#f-hecho)"],
    // con markdown pegado antes
    ["**Hai iniziato** il 11 marzo 2026", "**Hai iniziato** l'11 marzo 2026"],
    // entro il / per il: solo cambia el "il"
    ["entro il 8 maggio", "entro l'8 maggio"],
    ["prevista per il 11 maggio", "prevista per l'11 maggio"],
    // dos en la misma frase
    ["il 8 e il 11", "l'8 e l'11"],
  ])("%s → %s", (entrada, esperado) => {
    expect(elidir("it", entrada)).toBe(esperado);
  });

  it.each([
    // 1 se lee "primo" en una fecha: "il 1º marzo" (consonante)
    "il 1º marzo",
    // 9 "nove", 18 "diciotto", 28 "ventotto", 31 "trentuno"
    "il 9 marzo",
    "il 18 marzo",
    "il 28 marzo",
    "il 31 marzo",
    // 110 "centodieci", 111 "centoundici", 1100 "millecento", 111.000 "centoundicimila"
    "il 110",
    "il 111",
    "il 1100",
    "il 111.000",
    // la fecha ISO del acta: 2026 "duemila…"
    "Chiusa il 2026-03-08",
    // "il" dentro de otra palabra no es un artículo
    "un profil 8",
    "l'aprile 8",
    // ya elidido: no se toca (idempotente)
    "l'8 marzo",
    "dall'11 aprile",
  ])("sin cambio: %s", (entrada) => {
    expect(elidir("it", entrada)).toBe(entrada);
  });

  it("es idempotente", () => {
    const una = elidir("it", "Dal 8 marzo al 11 aprile, il 80%");
    expect(elidir("it", una)).toBe(una);
  });

  it("fuera del italiano no toca nada (el español dice «del 8 al 11»)", () => {
    expect(elidir("es", "del 8 al 11 de marzo")).toBe("del 8 al 11 de marzo");
    expect(elidir("es", "Cerrada el 8 de marzo")).toBe("Cerrada el 8 de marzo");
    expect(elidir("pt", "do 8 ao 11 de março")).toBe("do 8 ao 11 de março");
    expect(elidir("fr", "il 8")).toBe("il 8");
    expect(elidir("en", "il 8")).toBe("il 8");
  });

  it("interpolarEn: interpola y elide en el idioma dado", () => {
    expect(interpolarEn("it", "Chiusa il {{fecha}}", { fecha: "8 marzo" })).toBe("Chiusa l'8 marzo");
    expect(interpolarEn("it", "Dal {{desde}} al {{hasta}}", { desde: "11 marzo", hasta: "8 aprile" })).toBe(
      "Dall'11 marzo all'8 aprile"
    );
    expect(interpolarEn("es", "del {{desde}} al {{hasta}}", { desde: "8 de marzo", hasta: "11 de abril" })).toBe(
      "del 8 de marzo al 11 de abril"
    );
  });
});

describe("el primer día del mes en italiano se escribe 1º (se lee «primo»)", () => {
  // Fechas locales a mediodía: el día del calendario no se corre por zona.
  const PRIMERO = new Date(2026, 2, 1, 12).toISOString();
  const OCHO = new Date(2026, 2, 8, 12).toISOString();
  it("1 de marzo de 2026 en italiano: «1º marzo 2026»; el resto de días sin marca", () => {
    expect(fechaHumanaConAno(PRIMERO, "it")).toBe("1º marzo 2026");
    expect(fechaHumanaCorta(PRIMERO, "it")).toBe("1º marzo");
    expect(fechaHumanaConAno(OCHO, "it")).toBe("8 marzo 2026");
  });
  it("en español no cambia nada", () => {
    expect(fechaHumanaConAno(PRIMERO, "es")).toBe("1 de marzo de 2026");
    expect(fechaHumanaCorta(OCHO, "es")).toBe("8 de marzo");
  });
});
