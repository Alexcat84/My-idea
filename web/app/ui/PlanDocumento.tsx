"use client";

/**
 * PlanDocumento — el plan como documento acordeón (brief 2.6): título e
 * intro abiertos; cada "## " sección (etapas, sostenibilidad, lo no
 * cubierto) como acordeón; "Esta semana" destacado con el acento dentro
 * de su etapa; la etiqueta (inicial/completo/seguimiento) como chip
 * discreto; descarga .md. El parser respeta el markdown REAL del motor:
 * no inventa estructura, solo pliega la que viene.
 */
import { Acordeon } from "./Acordeon";
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

export function PlanDocumento({ md, nombreIdea }: { md: string; nombreIdea: string }) {
  const plan = parsearPlan(md);

  return (
    <section className="flex flex-col gap-3">
      <div className="flex items-center justify-between gap-3">
        <div className="flex items-center gap-3">
          {plan.etiqueta && (
            <span className="rounded-full border border-hairline px-2.5 py-0.5 text-xs text-dim">
              {plan.etiqueta}
            </span>
          )}
        </div>
        <button
          onClick={() => descargarMd(md, nombreIdea)}
          className="text-sm text-dim hover:text-ink"
        >
          Descargar .md
        </button>
      </div>

      <div className="rounded-panel border border-hairline bg-surface p-5 sm:p-6">
        {plan.titulo && <h2 className="text-xl font-semibold leading-snug">{plan.titulo}</h2>}
        {plan.intro && (
          <div className="mt-3">
            <Markdown>{plan.intro}</Markdown>
          </div>
        )}
      </div>

      {plan.secciones.map((s, i) => {
        const { resto, estaSemana } = separarEstaSemana(s.contenido);
        return (
          <Acordeon key={i} titulo={s.titulo}>
            <Markdown>{resto}</Markdown>
            {estaSemana && (
              <div className="mt-4 rounded-cinta border border-hairline bg-accent-soft px-4 py-3">
                <Markdown>{estaSemana}</Markdown>
              </div>
            )}
          </Acordeon>
        );
      })}

      {plan.pie && <p className="mt-1 text-xs text-dim">{plan.pie}</p>}
    </section>
  );
}
