/**
 * Contrato de UNIFORMIDAD del frente (ago 2026, de la corrida del fundador).
 *
 * Tres reglas que el fundador cazó en vivo en UNA pantalla y mandó aplicar en
 * TODAS. Se vigilan sobre el fuente porque el fallo típico no es romperlas
 * aquí: es olvidarlas en la próxima pantalla que alguien añada.
 *
 *  1. TODO header de página es sticky. Si el header se va al bajar, se van con
 *     él el saldo y la salida, justo en las pantallas largas donde el usuario
 *     quiere pausar.
 *  2. TODO botón que COBRA dice su precio, y su pantalla dice la garantía. El
 *     plan del mundo lo decía y el del núcleo no: esa asimetría es la que se
 *     cerró.
 *  3. TODO campo donde el usuario NARRA lleva voz (CampoConVoz). Escribir o
 *     dictar es del usuario, no del formulario.
 */
import { readFileSync } from "node:fs";
import path from "node:path";
import { describe, expect, it } from "vitest";
import { MANOS_A_LA_OBRA } from "@/lib/i18n/mensajes/manosALaObra";
import { IDEA_VIEW } from "@/lib/i18n/mensajes/ideaView";

const raiz = path.join(__dirname, "..");
const leer = (rel: string) => readFileSync(path.join(raiz, rel), "utf-8");

/** Las páginas con header propio (las que no viven dentro de la idea). */
const PAGINAS_CON_HEADER = [
  "ideas/page.tsx",
  "potenciadores/page.tsx",
  "creditos/page.tsx",
  "cuenta/page.tsx",
  "idea/[id]/IdeaView.tsx",
];

describe("1. el header nunca abandona al usuario a mitad de pantalla", () => {
  for (const rel of PAGINAS_CON_HEADER) {
    it(`${rel} tiene su header sticky`, () => {
      const fuente = leer(rel);
      const iHeader = fuente.indexOf("<header");
      expect(iHeader).toBeGreaterThan(-1);
      // el sticky vive en el propio tag del header, no en cualquier parte
      const tag = fuente.slice(iHeader, fuente.indexOf(">", iHeader));
      expect(tag).toContain("sticky");
      expect(tag).toContain("top-0");
    });
  }
});

describe("2. lo que cuesta, se dice donde se decide", () => {
  it("los botones del fin de entrevista llevan su precio, leído de la regla del cobro", () => {
    const fuente = leer("idea/[id]/IdeaView.tsx");
    // AUD-09 H01: antes este contrato exigía PRECIOS.plan_completo tecleado, y
    // eso era el fallo: un seguimiento anunciaba 10 y se cobraba 5. El precio
    // sale de finDeEntrevista(dominio, esSeguimiento), la misma regla del cobro.
    expect(fuente).toContain("finDeEntrevista(dominioEntrevista, esSeguimientoEntrevista)");
    // i18n F2: el texto vive en el catálogo de la vista con su {{n}}, y la vista
    // le pone fin.costo (la regla del cobro) en esa misma clave.
    // el que dispara el cobro
    expect(IDEA_VIEW.es.contextoFinal.armarPlan).toBe("Armar mi plan · {{n}} créditos");
    expect(fuente).toContain("interpolar(t.contextoFinal.armarPlan, { n: fin.costo })");
    // y los que llevan a él
    expect(IDEA_VIEW.es.oferta.generarPlan).toBe("Generar mi plan · {{n}} créditos");
    expect(fuente).toContain("interpolar(t.oferta.generarPlan, { n: fin.costo })");
  });

  // i18n F2: los textos de Manos a la Obra viven en su catálogo. El precio
  // sigue saliendo de PRECIOS: el catálogo dice "{{n}} créditos" y el
  // componente le pone la cifra de PRECIOS en esa misma clave.
  const t = MANOS_A_LA_OBRA.es;

  it("el botón del plan de un MUNDO sigue llevando el suyo", () => {
    expect(t.mundo.generarMiPlan).toContain("{{n}} créditos");
    expect(leer("ui/ManosALaObra.tsx")).toMatch(/interpolar\(t\.mundo\.generarMiPlan, \{[^}]*n: PRECIOS\.mundo_activar \}\)/);
  });

  it("los botones del SEGUIMIENTO llevan el suyo (núcleo y mundo)", () => {
    const fuente = leer("ui/ManosALaObra.tsx");
    expect(t.ritual.botonMiIdea).toContain("{{n}} créditos");
    expect(t.ritual.botonMundo).toContain("{{n}} créditos");
    expect(fuente).toContain("interpolar(t.botonMiIdea, { n: PRECIOS.seguimiento })");
    expect(fuente).toContain("interpolar(t.botonMundo, { n: PRECIOS.mundo_seguimiento })");
  });

  it("donde se cobra, se promete: se descuenta a la entrega y el fallo no se cobra", () => {
    // La vista de la idea: la garantía está en su catálogo y la oferta la pinta.
    expect(IDEA_VIEW.es.oferta.garantia).toMatch(/[Ss]e descuentan al entregarse/);
    expect(IDEA_VIEW.es.oferta.garantia).toContain("no se cobra nada");
    expect(leer("idea/[id]/IdeaView.tsx")).toContain("t.oferta.garantia");
    // Manos a la Obra: la garantía está en su catálogo y el ritual la pinta.
    expect(t.ritual.garantiaCobro).toMatch(/[Ss]e descuentan al entregarse/);
    expect(t.ritual.garantiaCobro).toContain("no se cobra nada");
    expect(leer("ui/ManosALaObra.tsx")).toContain("{t.garantiaCobro}");
  });

  it("el precio NO se anuncia donde no hay nada que cobrar (la Claridad)", () => {
    // La Claridad es gratis y queda guardada: anunciar ahí un precio es ruido.
    for (const rel of ["nueva/page.tsx", "ui/Claridad.tsx"]) {
      expect(leer(rel)).not.toContain("La Exploración usa");
    }
  });
});

describe("3. donde el usuario narra, puede dictar", () => {
  const CON_NARRACION = [
    "ui/TarjetaPregunta.tsx", // cada pregunta de la entrevista
    "ui/ManosALaObra.tsx", // el ritual "Contar qué pasó"
    "ui/DetalleActividad.tsx", // la nota y el motivo de retirar
    "nueva/page.tsx", // la chispa
    "idea/[id]/IdeaView.tsx", // el contexto final antes del plan
  ];
  for (const rel of CON_NARRACION) {
    it(`${rel} usa CampoConVoz`, () => {
      expect(leer(rel)).toContain("CampoConVoz");
    });
  }

  it("ningún campo de narración quedó como textarea crudo", () => {
    // Un <textarea> suelto en estas pantallas es un campo sin micrófono: si
    // aparece uno nuevo, este test lo caza antes que el usuario.
    for (const rel of CON_NARRACION) {
      expect(leer(rel)).not.toContain("<textarea");
    }
  });
});
