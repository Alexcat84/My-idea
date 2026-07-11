"use client";

/**
 * PlanDocumento — el plan como documento acordeón (brief 2.6): título e
 * intro abiertos; cada "## " sección (etapas, sostenibilidad, lo no
 * cubierto) como acordeón; "Esta semana" destacado con el acento dentro
 * de su etapa; la etiqueta (inicial/completo/seguimiento) como chip
 * discreto; descarga .md. El parser respeta el markdown REAL del motor:
 * no inventa estructura, solo pliega la que viene.
 */
import { Markdown } from "./Markdown";

interface Seccion {
  titulo: string;
  contenido: string;
}

interface PlanParseado {
  etiqueta: string | null;
  titulo: string | null;
  intro: string;
  secciones: Seccion[];
  pie: string | null;
}

function parsearPlan(md: string): PlanParseado {
  const lineas = md.split("\n");
  let etiqueta: string | null = null;
  let titulo: string | null = null;
  let pie: string | null = null;

  const cuerpo: string[] = [];
  for (const linea of lineas) {
    const l = linea.trim();
    if (!etiqueta && /^_Plan (completo|inicial)_$/.test(l)) {
      etiqueta = l.replaceAll("_", "");
      continue;
    }
    if (!pie && /^_Este plan se aliment/.test(l)) {
      pie = l.replaceAll("_", "");
      continue;
    }
    cuerpo.push(linea);
  }

  const secciones: Seccion[] = [];
  let intro: string[] = [];
  let actual: Seccion | null = null;
  for (const linea of cuerpo) {
    if (linea.startsWith("# ") && !titulo) {
      titulo = linea.slice(2).trim();
      continue;
    }
    const h2 = linea.match(/^##\s+(.+)$/);
    if (h2) {
      actual = { titulo: h2[1].trim(), contenido: "" };
      secciones.push(actual);
      continue;
    }
    if (actual) actual.contenido += linea + "\n";
    else intro.push(linea);
  }
  // separadores --- sueltos al final de secciones: ruido visual fuera
  for (const s of secciones) s.contenido = s.contenido.replace(/\n---\s*$/g, "\n").trim();
  intro = intro.join("\n").replace(/\n---\s*$/g, "").trim().split("\n");

  return { etiqueta, titulo, intro: intro.join("\n").trim(), secciones, pie };
}

/** Separa el bloque "**Esta semana:** …" (hasta la línea en blanco) del
 * resto del contenido de una etapa, para destacarlo con el acento. */
function separarEstaSemana(contenido: string): { resto: string; estaSemana: string | null } {
  const m = contenido.match(/^\*\*Esta semana:?\*\*[\s\S]*?(?=\n\s*\n|$)/m);
  if (!m) return { resto: contenido, estaSemana: null };
  const estaSemana = m[0].trim();
  const resto = (contenido.slice(0, m.index) + contenido.slice((m.index ?? 0) + m[0].length)).trim();
  return { resto, estaSemana };
}

function descargarMd(md: string, nombre: string) {
  const blob = new Blob([md], { type: "text/markdown;charset=utf-8" });
  const url = URL.createObjectURL(blob);
  const a = document.createElement("a");
  a.href = url;
  a.download = `${nombre.replace(/[^\p{L}\p{N} _-]/gu, "").trim().slice(0, 60) || "plan"}.md`;
  a.click();
  URL.revokeObjectURL(url);
}

function CajaEstaSemana({
  contenido,
  grande,
  onEmpezar,
}: {
  contenido: string;
  grande?: boolean;
  onEmpezar?: () => void;
}) {
  return (
    <div
      className={
        "rounded-panel bg-surface " + (grande ? "px-7 py-[26px]" : "mt-4 px-5 py-4")
      }
      style={{ border: "1px solid rgba(63,185,80,0.35)" }}
    >
      <p className="mb-3 flex items-center gap-2.5 text-[11px] font-bold uppercase tracking-[1.4px] text-done">
        <span className="anima-green-pulse h-[9px] w-[9px] rounded-full bg-done" />
        Esta semana
      </p>
      <div className={grande ? "text-[17px] font-semibold leading-normal [text-wrap:pretty] sm:text-[19px]" : ""}>
        <Markdown>{contenido.replace(/^\*\*Esta semana:?\*\*\s*/i, "")}</Markdown>
      </div>
      {grande && onEmpezar && (
        <button
          onClick={onEmpezar}
          className="mt-[18px] rounded-[10px] bg-done px-[22px] py-2.5 text-[13.5px] font-bold text-[#04120A] hover:opacity-90"
        >
          Empezar con esto
        </button>
      )}
    </div>
  );
}

export function PlanDocumento({
  md,
  nombreIdea,
  onEmpezar,
}: {
  md: string;
  nombreIdea: string;
  /** CTA verde del canon 05 en la caja grande: lleva a Manos a la Obra. */
  onEmpezar?: () => void;
}) {
  const plan = parsearPlan(md);

  // Canon 05: la primera acción concreta se eleva a la caja grande bajo
  // la intro; su etapa conserva el resto del contenido.
  const secciones = plan.secciones.map((s) => ({ titulo: s.titulo, ...separarEstaSemana(s.contenido) }));
  const idxElevada = secciones.findIndex((s) => s.estaSemana);
  const primeraSemana = idxElevada >= 0 ? secciones[idxElevada].estaSemana : null;

  return (
    <section className="flex flex-col">
      {/* encabezado del documento (canon 05): chip + título 32 + intro */}
      <div className="anima-plan-in flex items-start justify-between gap-3" style={{ animationDelay: "0.1s" }}>
        <div className="mb-4 flex items-center gap-2">
          <span aria-hidden className="h-1.5 w-1.5 rounded-full bg-accent" />
          <span className="text-[11px] font-semibold uppercase tracking-[1.2px] text-dim">
            Generado de tu recorrido{plan.etiqueta ? ` · ${plan.etiqueta}` : ""}
          </span>
        </div>
        <button
          onClick={() => descargarMd(md, nombreIdea)}
          className="shrink-0 text-sm text-dim hover:text-ink"
        >
          Descargar .md
        </button>
      </div>
      {plan.titulo && (
        <h2 className="anima-plan-in text-[26px] font-bold leading-[1.25] tracking-[-0.02em] [text-wrap:balance] sm:text-[32px]" style={{ animationDelay: "0.1s" }}>
          {plan.titulo}
        </h2>
      )}
      {plan.intro && (
        <div className="anima-plan-in mt-3.5 max-w-[560px] text-[15.5px] leading-[1.7] text-dim [text-wrap:pretty]" style={{ animationDelay: "0.2s" }}>
          <Markdown>{plan.intro}</Markdown>
        </div>
      )}

      {/* la caja verde grande: la primera acción sobre el mundo real */}
      {primeraSemana && (
        <div className="anima-plan-in mt-9" style={{ animationDelay: "0.35s" }}>
          <CajaEstaSemana contenido={primeraSemana} grande onEmpezar={onEmpezar} />
        </div>
      )}

      {/* etapas como tarjetas numeradas (canon 05), sin acordeones */}
      <div className="mt-9 flex flex-col gap-3.5">
        {secciones.map((s, i) => {
          const numero = s.titulo.match(/^Etapa\s+(\d+)/i)?.[1];
          const esLaElevada = i === idxElevada;
          return (
            <article
              key={i}
              className="anima-plan-in rounded-[14px] border border-hairline bg-surface px-6 py-[22px]"
              style={{ animationDelay: `${0.55 + i * 0.12}s` }}
            >
              <div className="flex items-baseline gap-3.5">
                {numero && (
                  <span className="shrink-0 text-[13px] font-bold text-accent">
                    {numero.padStart(2, "0")}
                  </span>
                )}
                <div className="min-w-0 flex-1">
                  <h3 className="text-[17px] font-semibold leading-snug">
                    {s.titulo.replace(/^Etapa\s+\d+\s*[:.·-]?\s*/i, "")}
                  </h3>
                  <div className="mt-2 text-sm leading-[1.65]">
                    <Markdown>{s.resto}</Markdown>
                  </div>
                  {/* la caja elevada no se repite en su etapa */}
                  {s.estaSemana && !esLaElevada && <CajaEstaSemana contenido={s.estaSemana} />}
                </div>
              </div>
            </article>
          );
        })}
      </div>

      {plan.pie && <p className="mt-4 text-[13px] text-dim">{plan.pie}</p>}
    </section>
  );
}
