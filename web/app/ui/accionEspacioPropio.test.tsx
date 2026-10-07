// Decisión del fundador (8 oct 2026): cada opción del menú de Manos a la Obra
// (Profundizar mi plan, Replantear mi camino, Análisis, Tus documentos y las
// demás) abre SU PROPIO ESPACIO, con su ruta y su botón de volver; ninguna se
// despliega encima de la pantalla actual. En móvil igual.
//
// Análisis, documentos, bitácora y calendario ya eran vistas propias
// (?vista=...). Lo que se desplegaba dentro del hub eran las tres acciones:
// profundizar, replantear y cerrar. Con `accionInicial` (la ruta &accion=...),
// Manos pinta SOLO esa acción, con "← Volver", y nada del hub.
import { readFileSync } from "node:fs";
import path from "node:path";
import { renderToStaticMarkup } from "react-dom/server";
import { describe, expect, it } from "vitest";
import { IdiomaProvider } from "@/lib/i18n/IdiomaProvider";
import { interpolar } from "@/lib/i18n/interpolar";
import { MANOS_A_LA_OBRA } from "@/lib/i18n/mensajes/manosALaObra";
import { ManosALaObra, type ChecklistData, type ItemChecklistUI } from "./ManosALaObra";

const t = MANOS_A_LA_OBRA.es;
const FECHA = "2026-09-01T10:00:00.000Z";
const esc = (s: string) =>
  s.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;").replace(/"/g, "&quot;").replace(/'/g, "&#x27;");

function item(over: Partial<ItemChecklistUI> & { id: string }): ItemChecklistUI {
  return {
    plan_id: "plan-2",
    dominio: "core",
    etapa: 1,
    orden: 1,
    texto: "una tarea",
    destacado: false,
    estado: "pendiente",
    nota: null,
    completed_at: null,
    no_aplica_motivo: null,
    fecha_base: null,
    fecha_base_origen: null,
    fecha_base_original: null,
    banda: null,
    espera_externa: null,
    created_at: FECHA,
    updated_at: FECHA,
    ...over,
  };
}

const TAREA_CORE = "Probar la receta con masa madre";
const TAREA_MUNDO = "Escribir a diez cafeterías";
const ITEMS_CORE = [
  item({ id: "c1", texto: "Hablar con tres panaderías", estado: "hecho", completed_at: FECHA }),
  item({ id: "c2", texto: TAREA_CORE, orden: 2 }),
];
const ITEMS_MUNDO = [item({ id: "m1", dominio: "marketing", plan_id: "plan-m", texto: TAREA_MUNDO })];
const CHECKLIST: ChecklistData = {
  planes: [
    { plan_id: "plan-2", dominio: "core", etapas: [{ etapa: 1, items: ITEMS_CORE }] },
    { plan_id: "plan-m", dominio: "marketing", etapas: [{ etapa: 1, items: ITEMS_MUNDO }] },
  ],
  resumen: {},
};
const MUNDO = {
  dominio: "marketing",
  nombre: "Clientes a la Vista",
  promesa: "",
  plan: { etiqueta: "completo", contenido_md: "# Mundo\n", created_at: FECHA },
};
const noop = () => {};

function pintar(over: Partial<Parameters<typeof ManosALaObra>[0]> = {}) {
  return renderToStaticMarkup(
    <IdiomaProvider idioma="es">
      <ManosALaObra
        projectId="p1"
        planMd={"# Pan de barrio\n\n## Etapa 1: Valida\n"}
        planCreatedAt={FECHA}
        checklist={CHECKLIST}
        historial={[]}
        mundos={[MUNDO]}
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
        soloDominio="core"
        {...over}
      />
    </IdiomaProvider>,
  );
}

/** Nada del hub: ni sus tareas, ni las tarjetas del menú, ni el avance. */
function sinHub(html: string, tarea: string) {
  expect(html).not.toContain(esc(tarea));
  expect(html).not.toContain(esc(t.tarjetas.documentosTitulo));
  expect(html).not.toContain(esc(t.tarjetas.analisisTitulo));
  expect(html).not.toContain(esc(t.nucleo.avanza));
}
const conVolver = (html: string) => expect(html).toMatch(new RegExp(`<button[^>]*>${esc(t.nucleo.volverAlEspacio)}</button>`));

describe("sin acción: el hub de siempre", () => {
  it("el núcleo pinta sus tareas y su menú, sin el botón de volver de las acciones", () => {
    const html = pintar();
    expect(html).toContain(esc(TAREA_CORE));
    expect(html).toContain(esc(t.tarjetas.documentosTitulo));
    expect(html).not.toContain(esc(t.nucleo.volverAlEspacio));
  });
});

describe("cada acción del núcleo en su propio espacio", () => {
  it("Profundizar mi plan: solo el ritual, con volver", () => {
    const html = pintar({ accionInicial: { tipo: "profundizar", dominio: "core" } });
    expect(html).toContain(esc(interpolar(t.ritual.encabezado, { paso: 1 })));
    conVolver(html);
    sinHub(html, TAREA_CORE);
  });

  it("Replantear mi camino: solo el replanteamiento, con volver", () => {
    const html = pintar({ accionInicial: { tipo: "replantear", dominio: "core" } });
    expect(html).toContain(esc(interpolar(t.replantear.encabezado, { paso: 1 })));
    conVolver(html);
    sinHub(html, TAREA_CORE);
  });

  it("Cerrar la idea: solo el acta de cierre, con volver", () => {
    const html = pintar({ accionInicial: { tipo: "cerrar", dominio: "core" } });
    expect(html).toContain(esc(t.cierre.cierraTuIdea));
    conVolver(html);
    sinHub(html, TAREA_CORE);
  });

  it("con la idea realizada la ruta no abre nada: queda el hub", () => {
    for (const tipo of ["profundizar", "replantear", "cerrar"] as const) {
      const html = pintar({ accionInicial: { tipo, dominio: "core" }, realizadaAt: FECHA });
      expect(html).not.toContain(esc(t.nucleo.volverAlEspacio));
      expect(html).toContain(esc(TAREA_CORE));
    }
  });
});

describe("cada acción de un mundo en su propio espacio", () => {
  const enMundo = { soloDominio: "marketing" };
  it("Profundizar en el mundo: su ritual con su nombre, sin el hub del mundo", () => {
    const html = pintar({ ...enMundo, accionInicial: { tipo: "profundizar", dominio: "marketing" } });
    expect(html).toContain(esc(interpolar(t.ritual.encabezadoMundo, { mundo: MUNDO.nombre, paso: 1 })));
    conVolver(html);
    expect(html).not.toContain(esc(TAREA_MUNDO));
  });

  it("Replantear en el mundo", () => {
    const html = pintar({ ...enMundo, accionInicial: { tipo: "replantear", dominio: "marketing" } });
    expect(html).toContain(esc(interpolar(t.replantear.encabezadoMundo, { mundo: MUNDO.nombre, paso: 1 })));
    conVolver(html);
    expect(html).not.toContain(esc(TAREA_MUNDO));
  });

  it("Cerrar el mundo: su acta en miniatura", () => {
    const html = pintar({ ...enMundo, accionInicial: { tipo: "cerrar", dominio: "marketing" } });
    expect(html).toContain(esc(interpolar(t.mundo.disteTerminado, { mundo: MUNDO.nombre })));
    conVolver(html);
    expect(html).not.toContain(esc(TAREA_MUNDO));
  });

  it("un mundo ya cerrado no abre sus acciones", () => {
    const html = pintar({ ...enMundo, mundos: [{ ...MUNDO, completadoAt: FECHA }], accionInicial: { tipo: "profundizar", dominio: "marketing" } });
    expect(html).not.toContain(esc(t.nucleo.volverAlEspacio));
  });
});

describe("contrato de la ruta", () => {
  const vista = readFileSync(path.join(__dirname, "..", "idea", "[id]", "IdeaView.tsx"), "utf8");
  const manos = readFileSync(path.join(__dirname, "ManosALaObra.tsx"), "utf8");

  it("IdeaView lee &accion= de la URL, se la pasa a Manos y la escribe cuando cambia", () => {
    expect(vista).toMatch(/searchParams\.get\("accion"\)/);
    expect(vista).toMatch(/accionInicial=\{/);
    expect(vista).toMatch(/onAccion=\{/);
  });

  it("en el espacio de una acción no se pintan las pestañas de espacios", () => {
    expect(vista).toMatch(/accionEnUrl \? null : mundosParaObra\.length > 0/);
  });

  it("toda vista propia arranca arriba (no se abre a media página)", () => {
    for (const fn of ["irAAnalisis", "irADocumentos", "irABitacora", "irACalendario"]) {
      const cuerpo = vista.match(new RegExp(`function ${fn}\\([\\s\\S]*?\\r?\\n  \\}\\r?\\n`))?.[0] ?? "";
      expect(cuerpo, fn).toContain("alInicio()");
    }
    expect(manos).toMatch(/window\.scrollTo\(/);
  });

  it("los rituales y las actas ya no se pintan dentro del hub", () => {
    expect(manos.match(/<RitualContinuar\b/g)?.length).toBe(1);
    expect(manos.match(/<RitualReplantear\b/g)?.length).toBe(1);
  });
});
