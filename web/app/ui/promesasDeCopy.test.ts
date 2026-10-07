// AUD-09 B03a (tanda 7B, confianza; decisión del fundador 25 sep 2026): tres
// promesas del copy sin respaldo. "Tu teléfono te recuerda cada tarea el día
// antes" (el aviso del calendario salta el MISMO día: TRIGGER:-PT0M) pasa a lo
// que de verdad hace; "Yo te recuerdo" (no hay sistema de recordatorios propio)
// y "El más elegido" (sin dato que lo respalde) se quitan.
import { readFileSync } from "node:fs";
import path from "node:path";
import { describe, expect, it } from "vitest";
import { LOCALES } from "../../lib/i18n/config";
import { BITACORA } from "../../lib/i18n/mensajes/bitacora";
import { CORREGIR_CIFRAS } from "../../lib/i18n/mensajes/corregirCifras";
import { DETALLE_ACTIVIDAD } from "../../lib/i18n/mensajes/detalleActividad";
import { MANOS_A_LA_OBRA } from "../../lib/i18n/mensajes/manosALaObra";
import { POTENCIA_TU_IDEA } from "../../lib/i18n/mensajes/potenciaTuIdea";
import { TUS_NUMEROS } from "../../lib/i18n/mensajes/tusNumeros";

const leer = (rel: string) => readFileSync(path.join(__dirname, rel), "utf8");

describe("el copy no promete lo que no pasa (AUD-09 B03a)", () => {
  it("el aviso del calendario es el mismo día, y así se dice", () => {
    // i18n F2: el copy vive en el catálogo del calendario; el componente lo pinta con t.info.
    const s = leer("SuscripcionCalendario.tsx");
    const cat = readFileSync(path.join(__dirname, "..", "..", "lib", "i18n", "mensajes", "calendario.ts"), "utf8");
    expect(s).not.toMatch(/el día\s+antes/);
    expect(cat).not.toMatch(/el día\s+antes/);
    // Auditoría final M14 (7 oct 2026): el aviso va en cada evento, pero no todos los
    // programas lo respetan en un calendario suscrito; se dice así (lib/i18n/promesasPublicas.test.ts).
    expect(cat).toMatch(/Cada tarea lleva un aviso para su día, pero según el calendario que uses/);
    expect(s).toMatch(/\{t\.info\}/);
    expect(readFileSync(path.join(__dirname, "..", "..", "lib", "ics.ts"), "utf8")).toMatch(/TRIGGER:-PT0M/);
  });
  it("sin 'Yo te recuerdo'", () => {
    expect(leer("ManosALaObra.tsx")).not.toMatch(/Yo te recuerdo/);
    // i18n F2: los textos de Manos a la Obra viven en su catálogo.
    expect(readFileSync(path.join(__dirname, "..", "..", "lib", "i18n", "mensajes", "manosALaObra.ts"), "utf8")).not.toMatch(
      /Yo te recuerdo/
    );
  });
  it("sin 'El más elegido'", () => {
    expect(readFileSync(path.join(__dirname, "..", "creditos", "page.tsx"), "utf8")).not.toMatch(/El más elegido/);
    // i18n F2: los textos de /creditos (y los nombres de las recargas) viven en sus catálogos.
    for (const cat of ["creditos.ts", "packsRecarga.ts"]) {
      expect(readFileSync(path.join(__dirname, "..", "..", "lib", "i18n", "mensajes", cat), "utf8")).not.toMatch(/El más elegido/);
    }
  });
});

// Auditoría final, promesas públicas B11 a B13 (7 oct 2026): las cifras son las
// que la persona da, los avisos dependen de sincronizar el calendario (no hay
// recordatorios propios) y lo que va dentro de un plan pagado es "incluido":
// BANCO reserva "gratis" para la Claridad y los diagnósticos de mundos.
const GRATIS = /gratis|grátis|gratuit|\bfree\b|kostenlos|無料|免费|무료|مجان|मुफ़्त/i;
const RECORDATORIOS = /recordatorio|reminder|rappel|lembrete|Erinnerung|promemoria|リマインダー|提醒|알림|تذكير|रिमाइंडर/i;

describe("promesas bajas de la auditoría final (B11 a B13), en los once idiomas", () => {
  it("B11: Tus Números trabaja con las cifras que das, no con 'tus cifras reales'", () => {
    expect(POTENCIA_TU_IDEA.es.tusNumerosPromesa).toBe(
      "Las cifras que nos das, convertidas en margen, punto de equilibrio y escenarios."
    );
    expect(POTENCIA_TU_IDEA.es.tusNumerosPromesa).not.toMatch(/reales/);
  });
  it("B12: elegir fechas no promete recordatorios; los avisos son los del calendario sincronizado", () => {
    for (const l of LOCALES) {
      expect(MANOS_A_LA_OBRA[l].modo.fechasTitulo, l).not.toMatch(RECORDATORIOS);
      expect(BITACORA[l].historia.modoFechas, l).not.toMatch(RECORDATORIOS);
    }
    expect(MANOS_A_LA_OBRA.es.modo.fechasTitulo).toBe("Con fechas");
    expect(MANOS_A_LA_OBRA.es.modo.fechasDesc).toMatch(/si lo sincronizas/);
  });
  it("B13: corregir cifras, recalcular y anotar van incluidos, nunca 'gratis'", () => {
    for (const l of LOCALES) {
      for (const [donde, texto] of [
        ["tusNumeros.leyGratis", TUS_NUMEROS[l].leyGratis],
        ["tusNumeros.corregirGratis", TUS_NUMEROS[l].corregirGratis],
        ["corregirCifras.intro", CORREGIR_CIFRAS[l].intro],
        ["detalleActividad.notaGratis", DETALLE_ACTIVIDAD[l].notaGratis],
      ] as const) {
        expect(texto, `${l} ${donde}`).not.toMatch(GRATIS);
      }
    }
    expect(TUS_NUMEROS.es.corregirGratis).toBe("Corregir mis cifras · incluido");
  });
});
