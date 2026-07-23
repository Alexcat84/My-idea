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

import { parsearPlan, type BloquePasos, type Seccion } from "@/lib/planParser";


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
            {/* El punto va al centro óptico de la PRIMERA línea del texto:
                13.5px x 1.6 de interlineado = 21.6px de caja, punto de 6px ->
                (21.6-6)/2 ~= 8px. Antes iba a 5px y ademas el <p> del Markdown
                empujaba el texto 10px hacia abajo: de ahi el desalineo. */}
            <span className="mt-2 block h-1.5 w-1.5 rounded-full bg-accent" />
            {i < pasos.length - 1 && (
              // del borde inferior de este punto al borde superior del siguiente
              <span
                className="absolute left-[2.5px] top-4 w-px"
                style={{ bottom: "-8px", background: "rgba(77,124,254,0.28)" }}
              />
            )}
          </span>
          {/* [&_p]:!my-0 neutraliza el margen del parrafo del Markdown, que es
              lo que descuadraba el punto contra el texto. */}
          <span className="min-w-0 flex-1 text-[13.5px] leading-[1.6] text-dim [text-wrap:pretty] [&_p]:!my-0">
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
          {/* CONFIDENCIAL: jamás exponer la maquinaria (conteo de nodos,
              grafo, conceptos). El usuario solo ve que su plan salió de SU
              recorrido. */}
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
