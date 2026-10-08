// LAS OPINIONES DE LOS USUARIOS (decisión del fundador, 8 oct 2026): la pregunta de un clic en los momentos clave.
// - Tarjeta discreta DENTRO de la pantalla, nunca un modal; con botón de cerrar sin responder.
// - Malo, Bueno, Excelente; si elige Malo, opciones rápidas (no es correcto, no aplica a mi caso, es confuso, otro) y
//   un texto opcional.
// - En los once idiomas; y cableada donde llega cada plan, en el seguimiento y en la cuenta.
// Prueba en rojo primero.
import { readFileSync } from "node:fs";
import path from "node:path";
import { renderToStaticMarkup } from "react-dom/server";
import { describe, expect, it } from "vitest";
import { ACTIVE_LOCALES } from "@/lib/i18n/config";
import { IdiomaProvider } from "@/lib/i18n/IdiomaProvider";
import { OPINIONES } from "@/lib/i18n/mensajes/opiniones";
import { TarjetaOpinion, type FaseTarjeta } from "./PreguntaOpinion";
import { FormularioComentarios } from "./ComentariosSugerencias";

const t = OPINIONES.es.tarjeta;
const noop = () => {};
const esc = (s: string) => s.replace(/&/g, "&amp;").replace(/'/g, "&#x27;").replace(/"/g, "&quot;");
const leer = (rel: string) => readFileSync(path.join(__dirname, "..", "..", rel), "utf8");

function pintar(fase: FaseTarjeta, extra: Partial<Parameters<typeof TarjetaOpinion>[0]> = {}, idioma: (typeof ACTIVE_LOCALES)[number] = "es") {
  return renderToStaticMarkup(
    <IdiomaProvider idioma={idioma}>
      <TarjetaOpinion
        tipo="plan"
        fase={fase}
        motivo={null}
        texto=""
        ocupado={false}
        error={null}
        onValorar={noop}
        onCerrar={noop}
        onMotivo={noop}
        onTexto={noop}
        onEnviarDetalle={noop}
        {...extra}
      />
    </IdiomaProvider>,
  );
}
const botones = (html: string) => html.match(/<button[^>]*>[\s\S]*?<\/button>/g) ?? [];

describe("la pregunta", () => {
  const html = pintar("preguntar");
  it("dice la pregunta y ofrece Malo, Bueno y Excelente", () => {
    expect(html).toContain(esc(t.pregunta.plan));
    for (const v of [t.valoracion.malo, t.valoracion.bueno, t.valoracion.excelente]) expect(html).toContain(`>${v}</button>`);
  });
  it("tiene su botón de cerrar sin responder", () => {
    expect(html).toContain(`aria-label="${esc(t.cerrar)}"`);
  });
  it("nunca es un modal: ni dialog, ni capa fija, ni fondo que tape", () => {
    expect(html).not.toMatch(/role="dialog"|aria-modal|class="[^"]*\bfixed\b/);
    expect(html).toMatch(/^<section[^>]*aria-label="/);
  });
  it("cada momento tiene su pregunta", () => {
    for (const tipo of ["plan_mundo", "profundizacion", "replanteamiento", "seguimiento"] as const) {
      expect(pintar("preguntar", { tipo })).toContain(esc(t.pregunta[tipo]));
    }
  });
  it("en los once idiomas", () => {
    for (const idioma of ACTIVE_LOCALES) {
      const h = pintar("preguntar", {}, idioma);
      expect(h).toContain(esc(OPINIONES[idioma].tarjeta.pregunta.plan));
      expect(h).toContain(`>${esc(OPINIONES[idioma].tarjeta.valoracion.excelente)}</button>`);
    }
  });
});

describe("si elige Malo", () => {
  const html = pintar("malo", { motivo: "confuso" });
  it("pregunta qué falló, con las cuatro opciones rápidas y la elegida marcada", () => {
    expect(html).toContain(esc(t.queFallo));
    for (const m of Object.values(t.motivo)) expect(html).toContain(esc(m));
    const elegida = botones(html).find((b) => b.includes(`>${t.motivo.confuso}<`))!;
    expect(elegida).toContain('aria-pressed="true"');
    const otra = botones(html).find((b) => b.includes(`>${t.motivo.otro}<`))!;
    expect(otra).toContain('aria-pressed="false"');
  });
  it("con un texto opcional y su botón de enviar", () => {
    expect(html).toContain(esc(t.textoOpcional));
    expect(html).toContain(`>${t.enviar}</button>`);
  });
  it("y se puede cerrar igual", () => {
    expect(html).toContain(`aria-label="${esc(t.cerrar)}"`);
  });
});

describe("después", () => {
  it("da las gracias, sin más botones", () => {
    const html = pintar("gracias");
    expect(html).toContain(esc(t.gracias));
    expect(html).toContain('role="status"');
    expect(botones(html)).toHaveLength(0);
  });
  it("si no se pudo guardar, lo dice (fallar ruidoso)", () => {
    expect(pintar("preguntar", { error: t.noGuardada })).toContain(esc(t.noGuardada));
  });
});

describe("Comentarios y sugerencias de la cuenta", () => {
  const c = OPINIONES.es.cuenta;
  const pintarForm = (enviado = false) =>
    renderToStaticMarkup(
      <IdiomaProvider idioma="es">
        <FormularioComentarios texto="" valoracion={null} enviado={enviado} ocupado={false} error={null} onTexto={noop} onValoracion={noop} onEnviar={noop} onOtro={noop} />
      </IdiomaProvider>,
    );
  it("un espacio para escribir, valoración opcional y enviar (desactivado sin texto)", () => {
    const html = pintarForm();
    expect(html).toContain(esc(c.descripcion));
    expect(html).toContain(esc(c.valoracionOpcional));
    expect(html).toContain(esc(c.placeholder));
    const enviar = botones(html).find((b) => b.includes(`>${c.enviar}<`))!;
    expect(enviar).toContain('disabled=""');
  });
  it("enviado: da las gracias y ofrece escribir otro", () => {
    const html = pintarForm(true);
    expect(html).toContain(esc(c.enviado));
    expect(html).toContain(`>${c.otro}</button>`);
  });
});

describe("cableada donde toca", () => {
  it("al recibir el plan del núcleo (y su profundización o replanteamiento), bajo el documento", () => {
    expect(leer("app/idea/[id]/IdeaView.tsx")).toMatch(/<PreguntaOpinion sesionId=\{planSesionId\}/);
  });
  it("en el plan de cada mundo, por la sesión de ese plan", () => {
    const manos = leer("app/ui/ManosALaObra.tsx");
    expect(manos.match(/<PreguntaOpinion sesionId=\{mundo\.plan\.session_id\}/g)?.length).toBeGreaterThanOrEqual(2);
  });
  it("de vez en cuando en el seguimiento del núcleo", () => {
    expect(leer("app/ui/ManosALaObra.tsx")).toMatch(/<PreguntaOpinion seguimiento=\{projectId\}/);
  });
  it("Comentarios y sugerencias en la cuenta", () => {
    expect(leer("app/ui/CuentaCliente.tsx")).toMatch(/<ComentariosSugerencias \/>/);
  });
});
