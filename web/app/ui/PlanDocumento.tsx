"use client";

/**
 * PlanDocumento — el plan como DOCUMENTO DE ACORDEONES (canon 05 +
 * ajustes del fundador 2026-07-14):
 *   - Encabezado + intro abiertos; debajo, una línea de meta ("N etapas").
 *   - Cada "## " del motor es una BARRA-TOPIC colapsada que, al desplegarse,
 *     muestra la data estructurada en contenedores: descripción, Pasos como
 *     una mini-línea de puntos (sutil pero visual), y Entregable en su caja.
 *   - La ACCIÓN concreta ("Esta semana") va al FINAL de cada tramo, nunca al
 *     inicio; y el cierre es un CTA concreto (Empezar / Manos a la Obra).
 * El parser respeta el markdown REAL del motor: no inventa estructura, solo
 * pliega la que viene. Colores: azul piensa, verde ejecuta (REGLAS_Y_TOKENS).
 */
import { Markdown } from "./Markdown";

type TipoSeccion = "etapa" | "cierre" | "otro";

interface Seccion {
  titulo: string;
  numero: string | null;
  tipo: TipoSeccion;
  descripcion: string;
  pasos: string[];
  entregable: string | null;
  estaSemana: string | null;
}

interface PlanParseado {
  etiqueta: string | null;
  titulo: string | null;
  intro: string;
  secciones: Seccion[];
  pie: string | null;
}

/** Recorta "**Etiqueta:** …" (hasta la línea en blanco o el fin) del cuerpo. */
function recortarBloque(cuerpo: string, etiqueta: RegExp): { valor: string | null; resto: string } {
  const m = cuerpo.match(etiqueta);
  if (!m || m.index === undefined) return { valor: null, resto: cuerpo };
  const resto = (cuerpo.slice(0, m.index) + cuerpo.slice(m.index + m[0].length)).trim();
  return { valor: m[0].trim(), resto };
}

function parsearSeccion(tituloCrudo: string, contenido: string): Seccion {
  const mEtapa = tituloCrudo.match(/^Etapa\s+(\d+)\s*[:.·-]?\s*(.*)$/i);
  const numero = mEtapa ? mEtapa[1].padStart(2, "0") : null;
  const titulo = (mEtapa ? mEtapa[2].trim() : tituloCrudo) || tituloCrudo;
  const esCierre = /sosten|n[úu]meros|no cubr|qu[ée] sigue/i.test(tituloCrudo);

  let cuerpo = contenido.replace(/\n---\s*$/g, "\n").trim();

  // 1) "Esta semana" — la acción concreta del tramo (va al final).
  const es = recortarBloque(cuerpo, /\*\*Esta semana:?\*\*[\s\S]*?(?=\n\s*\n|$)/);
  cuerpo = es.resto;
  const estaSemana = es.valor ? es.valor.replace(/^\*\*Esta semana:?\*\*\s*/i, "").trim() : null;

  // 2) "Entregable" — el artefacto que queda.
  const ent = recortarBloque(cuerpo, /\*\*Entregable:?\*\*[\s\S]*?(?=\n\s*\n|$)/);
  cuerpo = ent.resto;
  const entregable = ent.valor ? ent.valor.replace(/^\*\*Entregable:?\*\*\s*/i, "").trim() : null;

  // 3) "Pasos" — tras quitar Entregable/Esta semana, lo que sigue a **Pasos:**
  //    es la lista; lo anterior es la descripción.
  let pasos: string[] = [];
  const idxPasos = cuerpo.search(/\*\*Pasos:?\*\*/i);
  let descripcion = cuerpo;
  if (idxPasos >= 0) {
    descripcion = cuerpo.slice(0, idxPasos).trim();
    const listaRaw = cuerpo.slice(idxPasos).replace(/^\*\*Pasos:?\*\*\s*/i, "");
    pasos = listaRaw
      .split(/\n/)
      .map((l) => l.replace(/^\s*(?:\d+[.)]|[-*])\s+/, "").trim())
      .filter(Boolean);
  }

  return {
    titulo,
    numero,
    tipo: numero ? "etapa" : esCierre ? "cierre" : "otro",
    descripcion: descripcion.trim(),
    pasos,
    entregable,
    estaSemana,
  };
}

function parsearPlan(md: string): PlanParseado {
  let etiqueta: string | null = null;
  let pie: string | null = null;
  const cuerpo: string[] = [];
  for (const linea of md.split("\n")) {
    const l = linea.trim();
    if (!etiqueta && /^_Plan (completo|inicial|de seguimiento|seguimiento)_$/i.test(l)) {
      etiqueta = l.replaceAll("_", "");
      continue;
    }
    if (!pie && /^_Este plan se aliment/i.test(l)) {
      pie = l.replaceAll("_", "");
      continue;
    }
    cuerpo.push(linea);
  }

  let titulo: string | null = null;
  const intro: string[] = [];
  const rawSecc: { titulo: string; contenido: string }[] = [];
  let actual: { titulo: string; contenido: string } | null = null;
  for (const linea of cuerpo) {
    // El primer encabezado (# o ##) es el TÍTULO del plan; su cuerpo, la intro.
    if (!titulo) {
      const h = linea.match(/^#{1,2}\s+(.+)$/);
      if (h) {
        titulo = h[1].trim();
        continue;
      }
      intro.push(linea);
      continue;
    }
    const h2 = linea.match(/^##\s+(.+)$/);
    if (h2) {
      actual = { titulo: h2[1].trim(), contenido: "" };
      rawSecc.push(actual);
      continue;
    }
    if (actual) actual.contenido += linea + "\n";
    else intro.push(linea);
  }

  const secciones = rawSecc.map((s) => parsearSeccion(s.titulo, s.contenido));
  const introTxt = intro.join("\n").replace(/\n---\s*$/g, "").trim();
  return { etiqueta, titulo, intro: introTxt, secciones, pie };
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

/** Pasos como mini-línea de puntos (canon 04 en pequeño): sutil pero visual. */
function PasosLista({ pasos }: { pasos: string[] }) {
  return (
    <ol className="mt-2 flex flex-col">
      {pasos.map((p, i) => (
        <li key={i} className="relative flex gap-3 pb-3 last:pb-0">
          <span aria-hidden className="relative flex-none">
            <span className="mt-[5px] block h-1.5 w-1.5 rounded-full bg-accent" />
            {i < pasos.length - 1 && (
              <span
                className="absolute left-[2.5px] top-3 w-px"
                style={{ bottom: "-4px", background: "rgba(77,124,254,0.28)" }}
              />
            )}
          </span>
          <span className="min-w-0 flex-1 text-[13.5px] leading-[1.6] text-dim [text-wrap:pretty]">
            <Markdown>{p}</Markdown>
          </span>
        </li>
      ))}
    </ol>
  );
}

/** La caja verde de acción (verde ejecuta). Al final de cada tramo, o como CTA
 * grande de cierre con el botón "Empezar con esto". */
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
      className={"rounded-[12px] bg-surface " + (grande ? "px-7 py-[26px]" : "px-4 py-4")}
      style={{ border: "1px solid rgba(63,185,80,0.35)" }}
    >
      <p className="mb-2 flex items-center gap-2.5 text-[11px] font-bold uppercase tracking-[1.4px] text-done">
        <span className="anima-green-pulse h-[9px] w-[9px] rounded-full bg-done" />
        Esta semana
      </p>
      <div className={grande ? "text-[17px] font-semibold leading-normal [text-wrap:pretty] sm:text-[19px]" : "text-[13.5px] leading-[1.6] [text-wrap:pretty]"}>
        <Markdown>{contenido}</Markdown>
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

/** Una barra-topic desplegable (acordeón nativo <details>): colapsada por
 * defecto; al abrir muestra la data estructurada y la acción al final. */
function BarraTopic({ s }: { s: Seccion }) {
  return (
    <details className="group overflow-hidden rounded-[14px] border border-hairline bg-surface transition-colors open:border-[color:rgba(77,124,254,0.35)]">
      <summary className="flex cursor-pointer list-none items-center gap-3.5 px-6 py-[18px] [&::-webkit-details-marker]:hidden">
        {s.numero ? (
          <span className="shrink-0 text-[13px] font-bold text-accent">{s.numero}</span>
        ) : (
          <span aria-hidden className="h-1.5 w-1.5 shrink-0 rounded-full bg-accent" />
        )}
        <span className="min-w-0 flex-1 text-[15.5px] font-semibold leading-snug">{s.titulo}</span>
        <svg
          aria-hidden
          width="14"
          height="14"
          viewBox="0 0 12 12"
          className="shrink-0 text-dim transition-transform duration-200 group-open:rotate-180"
        >
          <path d="M2 4l4 4 4-4" stroke="currentColor" strokeWidth="1.4" fill="none" />
        </svg>
      </summary>
      <div className="flex flex-col gap-4 px-6 pb-[22px] pt-1">
        {s.descripcion && (
          <div className="text-sm leading-[1.65] text-dim [text-wrap:pretty]">
            <Markdown>{s.descripcion}</Markdown>
          </div>
        )}
        {s.pasos.length > 0 && (
          <div>
            <p className="text-[11px] font-semibold uppercase tracking-[1px] text-dim">Pasos</p>
            <PasosLista pasos={s.pasos} />
          </div>
        )}
        {s.entregable && (
          <div className="rounded-[10px] border border-hairline px-4 py-3" style={{ background: "#141419" }}>
            <p className="mb-1 text-[11px] font-semibold uppercase tracking-[1px] text-accent">Entregable</p>
            <div className="text-[13.5px] leading-[1.55] text-ink [text-wrap:pretty]">
              <Markdown>{s.entregable}</Markdown>
            </div>
          </div>
        )}
        {/* La acción concreta, SIEMPRE al final del tramo. */}
        {s.estaSemana && <CajaEstaSemana contenido={s.estaSemana} />}
      </div>
    </details>
  );
}

export function PlanDocumento({
  md,
  nombreIdea,
  onEmpezar,
}: {
  md: string;
  nombreIdea: string;
  /** CTA verde del cierre: lleva a Manos a la Obra. */
  onEmpezar?: () => void;
}) {
  const plan = parsearPlan(md);
  const etapas = plan.secciones.filter((s) => s.tipo === "etapa");

  return (
    <section className="flex flex-col">
      {/* encabezado del documento (canon 05) */}
      <div className="anima-plan-in flex items-start justify-between gap-3" style={{ animationDelay: "0.1s" }}>
        <div className="mb-3 flex items-center gap-2">
          <span aria-hidden className="h-1.5 w-1.5 rounded-full bg-accent" />
          <span className="text-[11px] font-semibold uppercase tracking-[1.2px] text-dim">
            Generado de tu recorrido{plan.etiqueta ? ` · ${plan.etiqueta}` : ""}
          </span>
        </div>
        <button onClick={() => descargarMd(md, nombreIdea)} className="shrink-0 text-sm text-dim hover:text-ink">
          Descargar .md
        </button>
      </div>
      {plan.titulo && (
        <h2 className="anima-plan-in text-[26px] font-bold leading-[1.25] tracking-[-0.02em] [text-wrap:balance] sm:text-[32px]" style={{ animationDelay: "0.1s" }}>
          {plan.titulo}
        </h2>
      )}
      {plan.intro && (
        <div className="anima-plan-in mt-3.5 max-w-[600px] text-[15.5px] leading-[1.7] text-dim [text-wrap:pretty]" style={{ animationDelay: "0.2s" }}>
          <Markdown>{plan.intro}</Markdown>
        </div>
      )}
      {etapas.length > 0 && (
        <p className="anima-plan-in mt-3 text-[13px] text-dim" style={{ animationDelay: "0.25s" }}>
          {etapas.length} {etapas.length === 1 ? "etapa" : "etapas"} · despliega cada una para ver los pasos y tu acción concreta
        </p>
      )}

      {/* barras-topic (acordeones), colapsadas: los topics primero */}
      <div className="mt-8 flex flex-col gap-3">
        {plan.secciones.map((s, i) => (
          <div key={i} className="anima-plan-in" style={{ animationDelay: `${0.4 + i * 0.08}s` }}>
            <BarraTopic s={s} />
          </div>
        ))}
      </div>

      {/* cierre concreto: ejecutar (verde ejecuta) */}
      {onEmpezar && (
        <div className="anima-plan-in mt-8" style={{ animationDelay: "0.5s" }}>
          <CajaEstaSemana
            contenido="Ya tienes el mapa completo. El primer paso concreto te espera en Manos a la Obra — empieza por lo más pequeño que puedas hacer hoy."
            grande
            onEmpezar={onEmpezar}
          />
        </div>
      )}

      {plan.pie && <p className="mt-5 text-[13px] text-dim">{plan.pie}</p>}
    </section>
  );
}
