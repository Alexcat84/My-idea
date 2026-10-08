// Decisión del fundador (8 oct 2026): en el menú de herramientas (las tarjetas
// de acceso de Manos a la Obra, del núcleo y del hub de cada mundo), una opción
// para comprar y administrar los créditos: lleva a /creditos, donde están el
// saldo, las recargas y el historial.
import { renderToStaticMarkup } from "react-dom/server";
import { describe, expect, it } from "vitest";
import { IdiomaProvider } from "@/lib/i18n/IdiomaProvider";
import { ACTIVE_LOCALES } from "@/lib/i18n/config";
import { MANOS_A_LA_OBRA } from "@/lib/i18n/mensajes/manosALaObra";
import { ManosALaObra, type ChecklistData, type ItemChecklistUI } from "./ManosALaObra";

const t = MANOS_A_LA_OBRA.es;
const FECHA = "2026-09-01T10:00:00.000Z";
const esc = (s: string) => s.replace(/&/g, "&amp;").replace(/'/g, "&#x27;").replace(/"/g, "&quot;");
const noop = () => {};

function item(id: string, dominio: string, plan_id: string): ItemChecklistUI {
  return {
    id, plan_id, dominio, etapa: 1, orden: 1, texto: `tarea ${id}`, destacado: false, estado: "pendiente", nota: null,
    completed_at: null, no_aplica_motivo: null, fecha_base: null, fecha_base_origen: null, fecha_base_original: null,
    banda: null, espera_externa: null, created_at: FECHA, updated_at: FECHA,
  };
}
const CHECKLIST: ChecklistData = {
  planes: [
    { plan_id: "p1", dominio: "core", etapas: [{ etapa: 1, items: [item("c1", "core", "p1")] }] },
    { plan_id: "pm", dominio: "marketing", etapas: [{ etapa: 1, items: [item("m1", "marketing", "pm")] }] },
  ],
  resumen: {},
};

function pintar(soloDominio: string, idioma: (typeof ACTIVE_LOCALES)[number] = "es") {
  return renderToStaticMarkup(
    <IdiomaProvider idioma={idioma}>
      <ManosALaObra
        projectId="p"
        planMd={"# Plan\n\n## Etapa 1: Uno\n"}
        planCreatedAt={FECHA}
        checklist={CHECKLIST}
        historial={[]}
        mundos={[{ dominio: "marketing", nombre: "Clientes a la Vista", promesa: "", plan: { etiqueta: "completo", contenido_md: "# M\n", created_at: FECHA } }]}
        modoCamino="ritmo"
        modos={{ marketing: "ritmo" }}
        onModoCambiado={noop}
        onRecargarChecklist={noop}
        onVerAnalisis={noop}
        onVerDocumentos={noop}
        onRealizada={noop}
        onMundoCerrado={noop}
        entrevistaAbierta={false}
        onVolverEntrevista={noop}
        onItemActualizado={noop}
        onSeguimientoIniciado={noop}
        onReplanteamientoListo={noop}
        onMundoIniciado={noop}
        onComprarPlanMundo={noop}
        onRegenerarPlanMundo={noop}
        soloDominio={soloDominio}
      />
    </IdiomaProvider>,
  );
}

const enlaceCreditos = /<a[^>]*href="\/creditos#historial"[^>]*>/;

describe("Tus créditos en el menú de herramientas", () => {
  it.each(["core", "marketing"])("en el espacio %s: la tarjeta lleva a /creditos, con su título y su descripción", (dominio) => {
    const html = pintar(dominio);
    expect(html).toMatch(enlaceCreditos);
    expect(html).toContain(esc(t.tarjetas.creditosTitulo));
    expect(html).toContain(esc(t.tarjetas.creditosDesc));
  });

  it.each([...ACTIVE_LOCALES])("%s: sus textos existen", (idioma) => {
    const tt = MANOS_A_LA_OBRA[idioma].tarjetas;
    expect(tt.creditosTitulo, idioma).toBeTruthy();
    expect(tt.creditosDesc, idioma).toBeTruthy();
    expect(pintar("core", idioma)).toContain(esc(tt.creditosTitulo));
  });
});
