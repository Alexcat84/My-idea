// i18n F6 (D2): el PAPEL (lo que se imprime o se guarda como PDF) va en el
// idioma del proyecto, rótulos incluidos; los botones y la navegación que lo
// rodean, en el de la interfaz.
//
// Lo esperado sale de los catálogos: la secuencia de la bitácora en coreano se
// titula DOCUMENTOS_PAPEL.ko.bitacora.laSecuencia y su fecha es "{{ano}}년
// {{mes}} {{d}}일" → "2026년 3월 8일"; en el plan, "Pasos" = PLAN_DOCUMENTO.ko.pasos
// ("진행 순서"), y "Mi bitácora" y "Empezar con esto" (botones, barra lateral)
// quedan en el español de la interfaz.
import { readFileSync } from "node:fs";
import path from "node:path";
import { renderToStaticMarkup } from "react-dom/server";
import { describe, expect, it } from "vitest";
import { IdiomaProvider } from "@/lib/i18n/IdiomaProvider";
import { DOCUMENTOS_PAPEL } from "@/lib/i18n/mensajes/documentosPapel";
import { PLAN_DOCUMENTO } from "@/lib/i18n/mensajes/planDocumento";
import type { EntradaBitacora } from "@/lib/bitacoraCliente";
import { ContenidoBitacora } from "./BitacoraPapel";
import { PapelEnIdioma } from "./PapelEnIdioma";
import { PlanDocumento } from "./PlanDocumento";

const OCHO_MARZO = new Date(2026, 2, 8, 12).toISOString();
const ENTRADAS: EntradaBitacora[] = [
  { fecha: OCHO_MARZO, texto: "첫 인터뷰", peso: "accion", dominio: "core" },
  { fecha: OCHO_MARZO, texto: "두 번째", peso: "accion", dominio: "core" },
];

describe("PapelEnIdioma", () => {
  it("interfaz en español, proyecto en coreano: la bitácora de papel va en coreano, con lang", () => {
    const html = renderToStaticMarkup(
      <IdiomaProvider idioma="es">
        <PapelEnIdioma idioma="ko">
          <ContenidoBitacora entradas={ENTRADAS} />
        </PapelEnIdioma>
      </IdiomaProvider>
    );
    expect(html).toContain(DOCUMENTOS_PAPEL.ko.bitacora.laSecuencia);
    expect(html).not.toContain(DOCUMENTOS_PAPEL.es.bitacora.laSecuencia);
    expect(html).toContain("2026년 3월 8일");
    expect(html).not.toContain("de marzo");
    expect(html).toContain('lang="ko"');
  });

  it("un proyecto en árabe se imprime de derecha a izquierda aunque la interfaz sea español", () => {
    const html = renderToStaticMarkup(
      <IdiomaProvider idioma="es">
        <PapelEnIdioma idioma="ar">
          <ContenidoBitacora entradas={ENTRADAS} />
        </PapelEnIdioma>
      </IdiomaProvider>
    );
    expect(html).toContain('dir="rtl"');
    expect(html).toContain(DOCUMENTOS_PAPEL.ar.bitacora.laSecuencia);
  });

  it("mismo idioma, o sin idioma de documento: el marcado es idéntico al de siempre", () => {
    const solo = renderToStaticMarkup(<ContenidoBitacora entradas={ENTRADAS} />);
    expect(
      renderToStaticMarkup(
        <PapelEnIdioma idioma="es">
          <ContenidoBitacora entradas={ENTRADAS} />
        </PapelEnIdioma>
      )
    ).toBe(solo);
    expect(
      renderToStaticMarkup(
        <PapelEnIdioma idioma={null}>
          <ContenidoBitacora entradas={ENTRADAS} />
        </PapelEnIdioma>
      )
    ).toBe(solo);
  });
});

describe("PlanDocumento: el cuerpo del plan en el idioma del proyecto, lo de alrededor en el de la interfaz", () => {
  const MD = ["# Plan", "", "## Etapa 1: 첫 고객", "", "**Pasos:**", "1. 전화하기", "", "**Esta semana:** 전화 한 통"].join("\n");

  it("idioma del documento coreano, interfaz español", () => {
    const html = renderToStaticMarkup(
      <IdiomaProvider idioma="es">
        <PlanDocumento md={MD} nombreIdea="Pan" idiomaDocumento="ko" onEmpezar={() => {}} onVerBitacora={() => {}} />
      </IdiomaProvider>
    );
    expect(html).toContain(PLAN_DOCUMENTO.ko.pasos);
    expect(html).not.toContain(`>${PLAN_DOCUMENTO.es.pasos}<`);
    expect(html).toContain(PLAN_DOCUMENTO.es.miBitacora);
    expect(html).toContain(PLAN_DOCUMENTO.es.empezarConEsto);
  });

  it("sin idioma de documento, todo como hoy (la interfaz)", () => {
    const sin = renderToStaticMarkup(
      <IdiomaProvider idioma="es">
        <PlanDocumento md={MD} nombreIdea="Pan" />
      </IdiomaProvider>
    );
    const con = renderToStaticMarkup(
      <IdiomaProvider idioma="es">
        <PlanDocumento md={MD} nombreIdea="Pan" idiomaDocumento="es" />
      </IdiomaProvider>
    );
    expect(con).toBe(sin);
  });
});

describe("Descargas monta el papel en el idioma que dice el servidor", () => {
  const src = readFileSync(path.join(__dirname, "Descargas.tsx"), "utf8");
  it("el papel va dentro de PapelEnIdioma con el idioma del documento", () => {
    expect(src).toMatch(/<PapelEnIdioma idioma=\{paraImprimir\.idioma\}>/);
  });
  it("BitacoraEspacio también", () => {
    const b = readFileSync(path.join(__dirname, "BitacoraEspacio.tsx"), "utf8");
    expect(b).toMatch(/<PapelEnIdioma idioma=\{/);
  });
});
