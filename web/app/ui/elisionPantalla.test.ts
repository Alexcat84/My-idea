// i18n F6: la elisión del italiano ("l'8 marzo", "dall'11") y el primero del
// mes ("1º" en italiano, "1er" en francés) también EN PANTALLA, no solo en los
// documentos. Las cinco frases de pantalla con un artículo delante de una
// fecha (Análisis, Manos a la Obra, Tus Números, Bitácora, Calendario) se
// interpolan con interpolarEn(idioma, …); en español la salida no cambia.
//
// Lo esperado, contado a mano con los catálogos italianos (it):
//   analisis.actaCerrado  "Chiuso il {{fecha}} con <b>{{hechas}} azioni su {{total}}</b>. …"
//     fecha = fechaHumanaCorta(8 mar 2026, it) = "8 marzo" → "Chiuso l'8 marzo con <b>3 azioni su 5</b>. …"
//   analisis.estadoCerrado "Chiuso il {{fecha}}. Oggi è a <b>{{hechas}} azioni su {{total}}</b>."
//     fecha = "11 marzo" → "Chiuso l'11 marzo. Oggi è a <b>3 azioni su 5</b>."
//   manos.fila.paraEl "entro il {{fecha}}", 8 marzo → "entro l'8 marzo"
//   manos.fila.hechoEl "fatta il {{fecha}}", 1 marzo → "fatta il 1º marzo" (primo: consonante, sin elisión)
//   tusNumeros.historico.viendo "Stai guardando i tuoi numeri del {{momento}}",
//     momento = momentoAbsoluto(8 mar 2026 14:30, ahora 2026, it) = "8 marzo, 14:30"
//     → "Stai guardando i tuoi numeri dell'8 marzo, 14:30"
//   bitacora.rango "dal {{desde}} al {{hasta}}", 8 marzo 2026 / 11 aprile 2026
//     → "dall'8 marzo 2026 all'11 aprile 2026"
//   calendario.rangoSemana "Dal {{d1}} {{m1}} al {{d2}} {{m2}}", meses cortos "feb", "mar":
//     lunes 2 mar, domingo 8 mar 2026   → "Dal 2 mar all'8 mar"
//     lunes 23 feb, domingo 1 mar 2026  → "Dal 23 feb al 1º mar"
//   francés "Du {{d1}} {{m1}} au {{d2}} {{m2}}", "févr.", "mars":
//     23 feb / 1 mar → "Du 23 févr. au 1er mars"
//   español "{{d1}} {{m1}} a {{d2}} {{m2}}": 2 mar / 8 mar → "2 mar a 8 mar"; 23 feb / 1 mar → "23 feb a 1 mar"
//   MapaHitos fechaCorta (hitos) it "{{d}} {{mes}}" "mar" → 1 mar = "1º mar"; fr "1er mars"; es "1 mar"
import { readFileSync } from "node:fs";
import { join } from "node:path";
import { describe, expect, it } from "vitest";
import { fechaHumanaConAno, fechaHumanaCorta, momentoAbsoluto } from "@/lib/fechas";
import { interpolarEn } from "@/lib/i18n/elision";
import { interpolar } from "@/lib/i18n/interpolar";
import { ANALISIS } from "@/lib/i18n/mensajes/analisis";
import { BITACORA } from "@/lib/i18n/mensajes/bitacora";
import { MANOS_A_LA_OBRA } from "@/lib/i18n/mensajes/manosALaObra";
import { TUS_NUMEROS } from "@/lib/i18n/mensajes/tusNumeros";
import { tituloDeSemana } from "./Calendario";
import { fechaMapa } from "./MapaHitos";

const dia = (m: number, d: number, h = 12, min = 0) => new Date(2026, m - 1, d, h, min).toISOString();
const fuente = (archivo: string) => readFileSync(join(__dirname, archivo), "utf8");

describe("las frases de pantalla, en italiano, eliden", () => {
  it("Análisis: acta y estado del cierre", () => {
    const t = ANALISIS.it.proyecto;
    expect(interpolarEn("it", t.actaCerrado, { fecha: fechaHumanaCorta(dia(3, 8), "it"), hechas: 3, total: 5 })).toBe(
      "Chiuso l'8 marzo con <b>3 azioni su 5</b>. Ciò che è rimasto in sospeso resta nella tua storia, così com'è."
    );
    expect(interpolarEn("it", t.estadoCerrado, { fecha: fechaHumanaCorta(dia(3, 11), "it"), hechas: 3, total: 5 })).toBe(
      "Chiuso l'11 marzo. Oggi è a <b>3 azioni su 5</b>."
    );
  });
  it("Manos a la Obra: para el / hecha el", () => {
    const t = MANOS_A_LA_OBRA.it;
    expect(interpolarEn("it", t.fila.paraEl, { fecha: fechaHumanaCorta(dia(3, 8), "it") })).toBe("entro l'8 marzo");
    expect(interpolarEn("it", t.fila.hechoEl, { fecha: fechaHumanaCorta(dia(3, 1), "it") })).toBe("fatta il 1º marzo");
  });
  it("Tus Números: el histórico", () => {
    const momento = momentoAbsoluto(dia(3, 8, 14, 30), new Date(2026, 5, 1), "it");
    expect(interpolarEn("it", TUS_NUMEROS.it.historico.viendo, { momento })).toBe("Stai guardando i tuoi numeri dell'8 marzo, 14:30");
  });
  it("Bitácora: el rango", () => {
    const desde = fechaHumanaConAno(dia(3, 8), "it");
    const hasta = fechaHumanaConAno(dia(4, 11), "it");
    expect(interpolarEn("it", BITACORA.it.pagina.rango, { desde, hasta })).toBe("dall'8 marzo 2026 all'11 aprile 2026");
  });
});

describe("Calendario: el título de la semana", () => {
  it("italiano: elisión y 1º", () => {
    expect(tituloDeSemana(new Date(2026, 2, 2), new Date(2026, 2, 8), "it")).toBe("Dal 2 mar all'8 mar");
    expect(tituloDeSemana(new Date(2026, 1, 23), new Date(2026, 2, 1), "it")).toBe("Dal 23 feb al 1º mar");
  });
  it("francés: 1er", () => {
    expect(tituloDeSemana(new Date(2026, 1, 23), new Date(2026, 2, 1), "fr")).toBe("Du 23 févr. au 1er mars");
  });
  it("español: igual que siempre", () => {
    expect(tituloDeSemana(new Date(2026, 2, 2), new Date(2026, 2, 8), "es")).toBe("2 mar a 8 mar");
    expect(tituloDeSemana(new Date(2026, 1, 23), new Date(2026, 2, 1), "es")).toBe("23 feb a 1 mar");
  });
});

describe("MapaHitos: el primero del mes", () => {
  it("1º en italiano, 1er en francés, 1 en español", () => {
    expect(fechaMapa(dia(3, 1), "it")).toBe("1º mar");
    expect(fechaMapa(dia(3, 1), "fr")).toBe("1er mars");
    expect(fechaMapa(dia(3, 1), "es")).toBe("1 mar");
  });
});

describe("en español la salida no cambia", () => {
  it("interpolarEn('es') = interpolar en las cinco frases", () => {
    const valores = { fecha: "8 de marzo", hechas: 3, total: 5, momento: "8 de marzo, 14:30", desde: "8 de marzo de 2026", hasta: "11 de abril de 2026" };
    for (const texto of [
      ANALISIS.es.proyecto.actaCerrado,
      ANALISIS.es.proyecto.estadoCerrado,
      MANOS_A_LA_OBRA.es.fila.paraEl,
      MANOS_A_LA_OBRA.es.fila.hechoEl,
      TUS_NUMEROS.es.historico.viendo,
      BITACORA.es.pagina.rango,
    ]) {
      expect(interpolarEn("es", texto, valores)).toBe(interpolar(texto, valores));
    }
  });
});

describe("los componentes usan interpolarEn en esas frases", () => {
  it.each([
    ["AnalisisProyecto.tsx", ["t.actaCerrado", "t.estadoCerrado"]],
    ["ManosALaObra.tsx", ["t.fila.paraEl", "t.fila.hechoEl"]],
    ["TusNumeros.tsx", ["tx.historico.viendo"]],
    ["Bitacora.tsx", ["t.rango"]],
  ])("%s", (archivo, claves) => {
    const src = fuente(archivo);
    for (const clave of claves) {
      expect(src).toContain(`interpolarEn(idioma, ${clave},`);
      expect(src).not.toContain(`interpolar(${clave},`);
    }
  });
  it("Calendario arma el título con tituloDeSemana y el día del panel con fechaHumana", () => {
    const src = fuente("Calendario.tsx");
    expect(src).toContain("tituloDeSemana(lunesRef, domRef, idioma)");
    expect(src).not.toContain("interpolar(t.rangoSemana");
    expect(src).not.toMatch(/d:\s*d\.getDate\(\)/);
  });
});
