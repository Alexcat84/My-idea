// Ciclo de replanteamiento, Fase 2 (decisiones del fundador del 27 sep 2026):
// DOS ENTRADAS SEPARADAS en Manos a la Obra, cada una con su etiqueta.
//  a. "Replantear mi camino": 1) tu historia, OBLIGATORIA; 2) lo que ya
//     construiste, cada hecha "me sigue sirviendo" o "ya no aplica"; 3) caminos
//     posibles; 4) confirmar y generar, con resumen, precio y promesa de cobro.
//  b. "Profundizar mi plan": el ciclo de hoy, con su paso 1 renombrado "Tu
//     avance" (el checklist deja de llamarse historia).
//  LO HECHO NO SE PIERDE: la Historia muestra el relato y las hechas de cada
//  plan anterior; una tarea traída del plan anterior lleva su chip.
// Todo lo esperado sale del catálogo (MANOS_A_LA_OBRA) y de PRECIOS.
import { readFileSync } from "node:fs";
import path from "node:path";
import { renderToStaticMarkup } from "react-dom/server";
import { describe, expect, it } from "vitest";
import { IdiomaProvider } from "@/lib/i18n/IdiomaProvider";
import { interpolar } from "@/lib/i18n/interpolar";
import { MANOS_A_LA_OBRA } from "@/lib/i18n/mensajes/manosALaObra";
import { PRECIOS } from "@/lib/precios";
import { ManosALaObra, RitualContinuar, type ChecklistData, type ItemChecklistUI, type PlanHistorial } from "./ManosALaObra";
import { PasoCaminos, PasoConfirmar, PasoConstruido, RitualReplantear } from "./RitualReplantear";

const t = MANOS_A_LA_OBRA.es;
const FECHA = "2026-09-01T10:00:00.000Z";

/** El escape de texto de React (renderToStaticMarkup). */
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

const ITEMS_CORE = [
  item({ id: "c1", texto: "Hablar con tres panaderías del barrio", estado: "hecho", completed_at: FECHA }),
  item({ id: "c2", texto: "Probar la receta con masa madre", estado: "pendiente", orden: 2 }),
  item({ id: "c3", texto: "Registrar la marca", estado: "hecho", completed_at: FECHA, orden: 3, heredado_de: "item-viejo-9" }),
];

function checklistCon(items: ItemChecklistUI[], mundo?: { dominio: string; items: ItemChecklistUI[] }): ChecklistData {
  const planes: ChecklistData["planes"] = [{ plan_id: "plan-2", dominio: "core", etapas: [{ etapa: 1, items }] }];
  if (mundo) planes.push({ plan_id: "plan-m", dominio: mundo.dominio, etapas: [{ etapa: 1, items: mundo.items }] });
  return { planes, resumen: {} };
}

const noop = () => {};

function pintarManos(over: Partial<Parameters<typeof ManosALaObra>[0]> = {}) {
  return renderToStaticMarkup(
    <IdiomaProvider idioma="es">
      <ManosALaObra
        projectId="p1"
        planMd={"# Pan de barrio\n\n## Etapa 1: Valida\n"}
        planCreatedAt={FECHA}
        checklist={checklistCon(ITEMS_CORE)}
        historial={[]}
        mundos={[]}
        modoCamino="ritmo"
        modos={{}}
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
        {...over}
      />
    </IdiomaProvider>
  );
}

const cuenta = (html: string, aguja: string) => html.split(aguja).length - 1;

describe("dos entradas en Manos a la Obra", () => {
  it("el núcleo ofrece Profundizar mi plan y Replantear mi camino (móvil y escritorio), con descripciones distintas", () => {
    const html = pintarManos({ soloDominio: "core" });
    expect(cuenta(html, esc(t.tarjetas.profundizarTitulo))).toBe(2);
    expect(cuenta(html, esc(t.tarjetas.replantearTitulo))).toBe(2);
    expect(html).toContain(esc(t.tarjetas.profundizarDesc));
    expect(html).toContain(esc(t.tarjetas.replantearDesc));
    expect(t.tarjetas.profundizarDesc).not.toBe(t.tarjetas.replantearDesc);
  });

  it("con la idea realizada, ninguna de las dos aparece", () => {
    const html = pintarManos({ soloDominio: "core", realizadaAt: FECHA });
    expect(html).not.toContain(esc(t.tarjetas.profundizarTitulo));
    expect(html).not.toContain(esc(t.tarjetas.replantearTitulo));
  });

  it("cada mundo abierto tiene sus dos entradas, con su nombre en la descripción; cerrado, ninguna", () => {
    const mundoItems = [item({ id: "m1", dominio: "marketing", plan_id: "plan-m", estado: "hecho", completed_at: FECHA })];
    const mundo = {
      dominio: "marketing",
      nombre: "Clientes a la Vista",
      promesa: "",
      plan: { etiqueta: "completo", contenido_md: "# Mundo\n", created_at: FECHA },
    };
    const base = { checklist: checklistCon(ITEMS_CORE, { dominio: "marketing", items: mundoItems }), soloDominio: "marketing" };
    const abierto = pintarManos({ ...base, mundos: [mundo] });
    expect(abierto).toContain(esc(t.tarjetas.profundizarTitulo));
    expect(abierto).toContain(esc(t.tarjetas.replantearTitulo));
    expect(abierto).toContain(esc(interpolar(t.mundo.profundizarDesc, { mundo: mundo.nombre })));
    expect(abierto).toContain(esc(interpolar(t.mundo.replantearDesc, { mundo: mundo.nombre })));
    const cerrado = pintarManos({ ...base, mundos: [{ ...mundo, completadoAt: FECHA }] });
    expect(cerrado).not.toContain(esc(t.tarjetas.replantearTitulo));
    expect(cerrado).not.toContain(esc(t.tarjetas.profundizarTitulo));
  });
});

describe("Profundizar mi plan: el paso 1 es Tu avance", () => {
  const html = renderToStaticMarkup(
    <IdiomaProvider idioma="es">
      <RitualContinuar resumen={{ hechos: 2, total: 5 }} enviando={false} error={null} onEnviar={noop} onCerrar={noop} />
    </IdiomaProvider>
  );
  it("dice Tu avance y ya no llama historia al checklist", () => {
    expect(t.ritual.tuAvance).toMatch(/^Tu avance/);
    expect(html).toContain(esc(t.ritual.tuAvance));
    expect(html).not.toContain("es tu historia");
  });
  it("el encabezado dice que es profundizar", () => {
    expect(t.ritual.encabezado).toMatch(/Profundizar/);
    expect(html).toContain(esc(interpolar(t.ritual.encabezado, { paso: 1 })));
  });
});

describe("Replantear mi camino", () => {
  it("paso 1: la historia es obligatoria (Seguir desactivado sin texto) y trae las preguntas de ayuda", () => {
    const html = renderToStaticMarkup(
      <IdiomaProvider idioma="es">
        <RitualReplantear projectId="p1" dominio="core" items={ITEMS_CORE} onListo={noop} onCerrar={noop} />
      </IdiomaProvider>
    );
    expect(html).toContain(esc(interpolar(t.replantear.encabezado, { paso: 1 })));
    expect(html).toMatch(new RegExp(`<button[^>]*disabled=""[^>]*>${esc(t.ritual.seguir)}</button>`));
    expect(t.replantear.ayudas.length).toBeGreaterThanOrEqual(3);
    for (const a of t.replantear.ayudas) expect(html).toContain(esc(a));
  });

  it("paso 2: lista solo las tareas hechas, cada una con sus dos opciones", () => {
    const html = renderToStaticMarkup(
      <IdiomaProvider idioma="es">
        <PasoConstruido items={ITEMS_CORE} sueltas={new Set(["c3"])} onAlternar={noop} onSeguir={noop} onAtras={noop} />
      </IdiomaProvider>
    );
    expect(html).toContain(esc("Hablar con tres panaderías del barrio"));
    expect(html).toContain(esc("Registrar la marca"));
    expect(html).not.toContain(esc("Probar la receta con masa madre"));
    expect(cuenta(html, esc(t.replantear.meSirve))).toBe(2);
    expect(cuenta(html, esc(t.replantear.yaNoAplica))).toBe(2);
    // ninguna hecha: una línea amable, y se puede seguir
    const vacio = renderToStaticMarkup(
      <IdiomaProvider idioma="es">
        <PasoConstruido items={[ITEMS_CORE[1]]} sueltas={new Set()} onAlternar={noop} onSeguir={noop} onAtras={noop} />
      </IdiomaProvider>
    );
    expect(vacio).toContain(esc(t.replantear.sinHechas));
  });

  it("paso 3: mientras piensa lo dice, y luego ofrece los caminos para elegir uno", () => {
    const pensando = renderToStaticMarkup(
      <IdiomaProvider idioma="es">
        <PasoCaminos caminos={null} cargando error={null} elegido={null} onElegir={noop} onReintentar={noop} onSeguir={noop} onAtras={noop} />
      </IdiomaProvider>
    );
    expect(pensando).toContain(esc(t.replantear.caminosPensando));
    const caminos = [
      { id: "a", titulo: "Vender al por mayor", descripcion: "Cafeterías del barrio" },
      { id: "b", titulo: "Pan por suscripción", descripcion: "Entrega semanal" },
    ];
    const listos = renderToStaticMarkup(
      <IdiomaProvider idioma="es">
        <PasoCaminos caminos={caminos} cargando={false} error={null} elegido="b" onElegir={noop} onReintentar={noop} onSeguir={noop} onAtras={noop} />
      </IdiomaProvider>
    );
    expect(cuenta(listos, 'type="radio"')).toBe(2);
    expect(listos).toContain("Pan por suscripción");
    expect(listos).toContain("Entrega semanal");
  });

  it("paso 4: el precio sale de PRECIOS.replanteamiento (núcleo) y mundo_replanteamiento (mundo), con la promesa de cobro", () => {
    const pintar = (dominio: string) =>
      renderToStaticMarkup(
        <IdiomaProvider idioma="es">
          <PasoConfirmar
            dominio={dominio}
            historia="Se fue mi socio y el local cerró."
            conservas={2}
            sueltas={1}
            camino={{ id: "a", titulo: "Vender al por mayor", descripcion: "" }}
            enviando={false}
            onGenerar={noop}
            onAtras={noop}
          />
        </IdiomaProvider>
      );
    const core = pintar("core");
    expect(core).toContain(esc(interpolar(t.replantear.generar, { n: PRECIOS.replanteamiento })));
    expect(core).toContain(esc(t.ritual.garantiaCobro));
    expect(core).toContain("Vender al por mayor");
    expect(core).toContain(esc(interpolar(t.replantear.resumenConservas, { n: 2 })));
    expect(core).toContain(esc(interpolar(t.replantear.resumenSueltas, { n: 1 })));
    expect(pintar("marketing")).toContain(esc(interpolar(t.replantear.generar, { n: PRECIOS.mundo_replanteamiento })));
  });

  it("contrato: pregunta el saldo a GET replantear antes de abrir, y el POST lleva historia, suelta, dominio y la sesión previa", () => {
    const manos = readFileSync(path.join(__dirname, "ManosALaObra.tsx"), "utf8");
    const ritual = readFileSync(path.join(__dirname, "RitualReplantear.tsx"), "utf8");
    expect(manos).toContain("fetch(`/api/project/${projectId}/replantear?dominio=${encodeURIComponent(dominio)}`)");
    expect(ritual).toContain("fetch(`/api/project/${projectId}/replantear`");
    expect(ritual).toContain("JSON.stringify({ historia: historiaLimpia, suelta, dominio, session_previa: previa })");
    expect(ritual).toContain("MAX_LARGO_TEXTO_USUARIO");
  });
});

describe("lo hecho no se pierde", () => {
  const historial: PlanHistorial[] = [
    { etiqueta: "completo", created_at: FECHA, contenido_md: "# Primer plan\n", hechas: [], relato: null },
    {
      etiqueta: "replanteamiento",
      created_at: FECHA,
      contenido_md: "# Segundo plan\n",
      hechas: [{ texto: "Conseguir el primer cliente mayorista", completed_at: FECHA }],
      relato: "El local cerró y me quedé sin horno.",
    },
    { etiqueta: "seguimiento", created_at: FECHA, contenido_md: "# Tercer plan\n" },
  ];

  it("la Historia del núcleo nombra cada ciclo por su tipo y pinta el relato y las hechas", () => {
    const html = pintarManos({ soloDominio: "core", historial });
    expect(html).toContain(esc(t.nucleo.histPrimerPlan));
    expect(html).toContain(esc(t.nucleo.histReplanteaste));
    expect(html).toContain(esc(t.nucleo.histProfundizaste));
    expect(html).toContain(esc("El local cerró y me quedé sin horno."));
    expect(html).toContain(esc("Conseguir el primer cliente mayorista"));
    expect(html).not.toContain("Plan replanteamiento");
  });

  it("un mundo con historial la muestra en su hub", () => {
    const mundoItems = [item({ id: "m1", dominio: "marketing", plan_id: "plan-m" })];
    const html = pintarManos({
      soloDominio: "marketing",
      checklist: checklistCon(ITEMS_CORE, { dominio: "marketing", items: mundoItems }),
      mundos: [
        {
          dominio: "marketing",
          nombre: "Clientes a la Vista",
          promesa: "",
          plan: { etiqueta: "seguimiento", contenido_md: "# Mundo\n", created_at: FECHA },
          historial: [historial[1]],
        },
      ],
    });
    expect(html).toContain(esc(interpolar(t.nucleo.historia, { n: 1 })));
    expect(html).toContain(esc("El local cerró y me quedé sin horno."));
  });

  it("una tarea traída del plan anterior lleva el chip De tu plan anterior, y solo esa", () => {
    const html = pintarManos({ soloDominio: "core" });
    expect(cuenta(html, esc(t.fila.heredada))).toBe(1);
  });
});
