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

/** Fase 3.9 C8: un bloque de pasos con su sub-encabezado (o null si la lista
 * venía suelta). Varios por etapa: "Pasos para construir", "Pasos para
 * atacarlo", etc. — todos con el MISMO tratamiento visual de puntos + línea. */
interface BloquePasos {
  label: string | null;
  pasos: string[];
}

interface Seccion {
  titulo: string;
  numero: string | null;
  tipo: TipoSeccion;
  descripcion: string;
  bloquesPasos: BloquePasos[];
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

  // 1) La acción concreta del tramo (va al final): "Esta semana" o su
  //    equivalente en la sección de números ("El lunes que viene").
  const RE_SEMANA = /\*\*(?:Esta semana|El lunes(?: que viene)?):?\*\*[\s\S]*?(?=\n\s*\n|$)/i;
  const es = recortarBloque(cuerpo, RE_SEMANA);
  cuerpo = es.resto;
  const estaSemana = es.valor
    ? es.valor.replace(/^\*\*(?:Esta semana|El lunes(?: que viene)?):?\*\*\s*/i, "").trim()
    : null;

  // 2) "Entregable" — el artefacto que queda.
  const ent = recortarBloque(cuerpo, /\*\*Entregable:?\*\*[\s\S]*?(?=\n\s*\n|$)/);
  cuerpo = ent.resto;
  const entregable = ent.valor ? ent.valor.replace(/^\*\*Entregable:?\*\*\s*/i, "").trim() : null;

  // 3) Pasos (C8): CUALQUIER "**...Pasos...:**" abre un bloque; una lista suelta
  //    cae en un bloque sin label. Todo lo demás (incluidas notas en negrita
  //    como "**Nota crítica:**") es descripción/prosa. Así los pasos reciben el
  //    mismo punto+línea vengan numerados, con viñetas, o en varios sub-bloques.
  const bloquesPasos: BloquePasos[] = [];
  const descripLineas: string[] = [];
  let bloque: BloquePasos | null = null;
  const esItem = (l: string) => /^\s*(?:\d+[.)]|[-*])\s+/.test(l);
  for (const linea of cuerpo.split("\n")) {
    const lab = linea.match(/^\s*\*\*\s*([^*]*[Pp]asos[^*]*?)\s*:?\s*\*\*\s*(.*)$/);
    if (lab) {
      bloque = { label: lab[1].trim(), pasos: [] };
      bloquesPasos.push(bloque);
      if (lab[2]?.trim()) bloque.pasos.push(lab[2].trim());
      continue;
    }
    if (esItem(linea)) {
      if (!bloque) {
        bloque = { label: null, pasos: [] };
        bloquesPasos.push(bloque);
      }
      bloque.pasos.push(linea.replace(/^\s*(?:\d+[.)]|[-*])\s+/, "").trim());
      continue;
    }
    bloque = null; // una línea no-lista cierra el bloque de pasos
    if (linea.trim()) descripLineas.push(linea);
  }
  for (const b of bloquesPasos) b.pasos = b.pasos.filter(Boolean);

  return {
    titulo,
    numero,
    tipo: numero ? "etapa" : esCierre ? "cierre" : "otro",
    descripcion: descripLineas.join("\n").trim(),
    bloquesPasos: bloquesPasos.filter((b) => b.pasos.length > 0),
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
  etiqueta = "Esta semana",
}: {
  contenido: string;
  grande?: boolean;
  onEmpezar?: () => void;
  etiqueta?: string;
}) {
  return (
    <div
      className={"rounded-[12px] bg-surface " + (grande ? "px-7 py-[26px]" : "px-4 py-4")}
      style={{ border: "1px solid rgba(63,185,80,0.35)" }}
    >
      <p className="mb-2 flex items-center gap-2.5 text-[11px] font-bold uppercase tracking-[1.4px] text-done">
        <span className="anima-green-pulse h-[9px] w-[9px] rounded-full bg-done" />
        {etiqueta}
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
function BarraTopic({ s, abierta }: { s: Seccion; abierta?: boolean }) {
  return (
    <details
      {...(abierta ? { open: true } : {})}
      className="group overflow-hidden rounded-[14px] border border-hairline bg-surface transition-colors open:border-[color:rgba(77,124,254,0.35)]"
    >
      <summary className="flex cursor-pointer list-none items-start gap-3.5 px-6 py-[18px] [&::-webkit-details-marker]:hidden">
        {s.numero ? (
          <span className="mt-px shrink-0 text-[13px] font-bold text-accent">{s.numero}</span>
        ) : (
          <span aria-hidden className="mt-2 h-1.5 w-1.5 shrink-0 rounded-full bg-accent" />
        )}
        <span className="min-w-0 flex-1">
          <span className="block text-[15.5px] font-semibold leading-snug">{s.titulo}</span>
          {/* Entregable como subtítulo de la barra colapsada: saber de qué va
              sin expandir. Se oculta al abrir (dentro va la caja completa). */}
          {s.entregable && (
            <span className="mt-1 line-clamp-2 block text-[12.5px] leading-[1.5] text-dim [text-wrap:pretty] group-open:hidden">
              {s.entregable}
            </span>
          )}
        </span>
        <svg
          aria-hidden
          width="14"
          height="14"
          viewBox="0 0 12 12"
          className="mt-1 shrink-0 text-dim transition-transform duration-200 group-open:rotate-180"
        >
          <path d="M2 4l4 4 4-4" stroke="currentColor" strokeWidth="1.4" fill="none" />
        </svg>
      </summary>
      <div className="flex flex-col gap-4 px-6 pb-[22px] pt-1">
        {s.descripcion && (
          // C7: prosa justificada con partición (lang="es" en el layout); C10:
          // cuerpo legible (gris claro, no el dim tenue), jerarquía por tamaño.
          <div className="text-[14.5px] leading-[1.7] text-[#C7C8CD] [text-align:justify] [hyphens:auto] [text-wrap:pretty]">
            <Markdown>{s.descripcion}</Markdown>
          </div>
        )}
        {s.bloquesPasos.map((b, bi) => (
          <div key={bi}>
            <p className="text-[11px] font-semibold uppercase tracking-[1px] text-dim">{b.label ?? "Pasos"}</p>
            <PasosLista pasos={b.pasos} />
          </div>
        ))}
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
  nodosFuente,
}: {
  md: string;
  nombreIdea: string;
  /** CTA verde: lleva a Manos a la Obra (bloque "Tu primera acción"). */
  onEmpezar?: () => void;
  /** canon 05: nodos del recorrido → sidebar "Construido con tu recorrido". */
  nodosFuente?: string[];
}) {
  const plan = parsearPlan(md);
  const etapas = plan.secciones.filter((s) => s.tipo === "etapa");
  // La acción de la etapa 1 (el corazón del producto): SIEMPRE visible arriba,
  // fuera de los acordeones. Su copia también vive al final de su tramo.
  const primeraAccion =
    etapas.find((s) => s.estaSemana)?.estaSemana ?? plan.secciones.find((s) => s.estaSemana)?.estaSemana ?? null;

  const documento = (
    <div className="min-w-0 flex-1">
      {/* encabezado del documento (canon 05) */}
      <div className="anima-plan-in flex items-start justify-between gap-3" style={{ animationDelay: "0.1s" }}>
        <div className="mb-3 flex items-center gap-2">
          <span aria-hidden className="h-1.5 w-1.5 rounded-full bg-accent" />
          <span className="text-[11px] font-semibold uppercase tracking-[1.2px] text-dim">
            Generado de tu recorrido
            {nodosFuente && nodosFuente.length > 0
              ? ` · ${nodosFuente.length} ${nodosFuente.length === 1 ? "nodo" : "nodos"}`
              : plan.etiqueta
                ? ` · ${plan.etiqueta}`
                : ""}
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
        <div className="anima-plan-in mt-3.5 max-w-[640px] text-[15.5px] leading-[1.7] text-[#C7C8CD] [text-align:justify] [hyphens:auto] [text-wrap:pretty]" style={{ animationDelay: "0.2s" }}>
          <Markdown>{plan.intro}</Markdown>
        </div>
      )}
      {etapas.length > 0 && (
        <p className="anima-plan-in mt-3 text-[13px] text-dim" style={{ animationDelay: "0.25s" }}>
          {etapas.length} {etapas.length === 1 ? "etapa" : "etapas"} · cada barra muestra su entregable; despliégala para los pasos y la acción
        </p>
      )}

      {/* TU PRIMERA ACCIÓN: el corazón del producto, siempre visible arriba */}
      {primeraAccion && (
        <div className="anima-plan-in mt-8" style={{ animationDelay: "0.3s" }}>
          <CajaEstaSemana contenido={primeraAccion} grande onEmpezar={onEmpezar} etiqueta="Tu primera acción" />
        </div>
      )}

      {/* barras-topic (acordeones): los topics primero, primera abierta */}
      <div className="mt-6 flex flex-col gap-3">
        {plan.secciones.map((s, i) => (
          <div key={i} className="anima-plan-in" style={{ animationDelay: `${0.4 + i * 0.08}s` }}>
            <BarraTopic s={s} abierta={i === 0} />
          </div>
        ))}
      </div>

      {plan.pie && <p className="mt-5 text-[13px] text-dim">{plan.pie}</p>}
    </div>
  );

  // Sin nodos fuente (plan de mundo / historial): una sola columna.
  if (!nodosFuente || nodosFuente.length === 0) {
    return <section className="flex flex-col">{documento}</section>;
  }

  // Canon 05: documento + sidebar "Construido con tu recorrido".
  return (
    <section className="flex flex-col gap-8 lg:flex-row lg:items-start">
      {documento}
      <aside
        className="anima-plan-in lg:w-[300px] lg:shrink-0 lg:border-l lg:border-hairline lg:pl-7"
        style={{ animationDelay: "0.5s" }}
      >
        <p className="mb-5 text-[11px] font-semibold uppercase tracking-[1.2px] text-dim">Construido con tu recorrido</p>
        <ul className="flex flex-col gap-4">
          {nodosFuente.map((n, i) => (
            <li key={i} className="flex items-start gap-3">
              <span
                aria-hidden
                className="mt-0.5 flex h-3.5 w-3.5 shrink-0 items-center justify-center rounded-full border-[1.5px] border-white/15 bg-black"
              >
                <span className="h-[7px] w-[7px] rounded-full bg-accent" />
              </span>
              <span className="text-[13px] leading-[1.5] text-dim">{n}</span>
            </li>
          ))}
        </ul>
        {/* Canon 05: la nota de recálculo bajo una hairline — el plan no es
            una lápida, se vuelve a la entrevista cuando el mundo cambia. */}
        <p className="mt-6 border-t border-hairline pt-5 text-[12.5px] leading-[1.6] text-dim [text-wrap:pretty]">
          ¿Cambia algo en el mundo real? Vuelve a la entrevista cuando quieras: el plan se recalcula desde donde estés.
        </p>
      </aside>
    </section>
  );
}
