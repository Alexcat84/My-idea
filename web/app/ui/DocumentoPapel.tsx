"use client";

/**
 * DocumentoPapel — cualquier documento del usuario (un ciclo del plan o el
 * expediente completo) renderizado con el lenguaje visual de la casa para que
 * el PDF se parezca a la pantalla: el azul que piensa marca la estructura, el
 * verde que ejecuta marca lo hecho, y las listas mantienen sus puntos de
 * conexión con su línea.
 *
 * Vive dentro de `[data-plan-print]`, así que hereda la hoja de impresión de
 * globals.css (tokens de papel, pie propio, acordeones abiertos). En pantalla
 * puede ir oculto: el panel de Descargas lo monta solo para mandarlo a papel.
 */
import ReactMarkdown, { type Components } from "react-markdown";
import remarkGfm from "remark-gfm";
import { HojaImpresion, FilaPapel } from "./HojaImpresion";

/** El riel del timeline: una ESPINA vertical continua y los puntos de cada ítem
 * centrados EXACTAMENTE sobre ella (el fundador la quiere ATRAVESANDO su centro).
 *
 * La espina va como BACKGROUND (clase `.papel-espina` de globals.css), NO como
 * un `::before` absoluto: en impresión un `::before` posicionado sobre el <ul>
 * abarca TODA la altura de la lista y, si la lista cruza un salto de página,
 * baja a través de la banda del pie y lo CRUZA (bug del fundador, jul 2026). El
 * fondo se recorta por página y jamás cruza el pie.
 *
 * Geometría (todo relativo al <ul>/<ol>, con pl-6 = 24px de canal):
 *  - espina: background en x=8..10 (2px)  → su centro cae en x=9.
 *  - punto:  el <li> arranca en x=24; con left:-20px y 10px de ancho, su centro
 *    cae en 24-20+5 = 9. Mismo eje que la espina → la línea pasa por el centro.
 * La comparten viñetas (ul) y pasos de etapa (ol). */
const RIEL_CLASES =
  "relative pl-6 papel-espina " +
  "[&>li]:relative " +
  "[&>li]:before:absolute [&>li]:before:content-[''] [&>li]:before:-left-[20px] [&>li]:before:top-[6px] " +
  "[&>li]:before:h-2.5 [&>li]:before:w-2.5 [&>li]:before:rounded-full [&>li]:before:bg-accent";

const COMPONENTES: Components = {
  h1: ({ children }) => (
    <h1 className="mb-4 text-[26px] font-bold leading-[1.2] tracking-[-0.02em] [text-wrap:balance] sm:text-[30px]">
      {children}
    </h1>
  ),
  // Sección mayor: hairline arriba y punto azul, como las barras del plan.
  h2: ({ children }) => (
    <h2 className="mt-10 flex items-baseline gap-2.5 border-t border-hairline pt-7 text-[19px] font-semibold leading-snug [text-wrap:balance]">
      <span aria-hidden className="h-1.5 w-1.5 shrink-0 translate-y-[-3px] rounded-full bg-accent" />
      {children}
    </h2>
  ),
  // Un documento incrustado (un plan) entra en h3, y sus etapas en h4: los dos
  // tienen que leerse como títulos de verdad, no como etiquetas menudas.
  h3: ({ children }) => (
    <h3 className="mt-8 text-[18px] font-semibold leading-snug text-accent [text-wrap:balance]">{children}</h3>
  ),
  h4: ({ children }) => (
    <h4 className="mt-6 text-[15px] font-semibold leading-snug [text-wrap:balance]">{children}</h4>
  ),
  h5: ({ children }) => <h5 className="mt-5 text-[13.5px] font-semibold">{children}</h5>,
  h6: ({ children }) => (
    <h6 className="mt-4 text-[11px] font-semibold uppercase tracking-[1px] text-dim">{children}</h6>
  ),
  p: ({ children }) => (
    <p className="my-3 text-[14.5px] leading-[1.7] [text-wrap:pretty]">{children}</p>
  ),
  ul: ({ children, className }) => {
    // Las listas de tareas llevan su propia marca (check verde / círculo), así
    // que no necesitan el riel de puntos: sería ruido sobre ruido.
    const tareas = typeof className === "string" && className.includes("contains-task-list");
    return tareas ? (
      <ul className="my-3 flex flex-col gap-2.5">{children}</ul>
    ) : (
      <ul className={"my-3 flex flex-col gap-2.5 " + RIEL_CLASES}>{children}</ul>
    );
  },
  // Los pasos de cada Etapa del plan (lista numerada) usan el MISMO riel de
  // puntos que las viñetas: la espina + los puntos encima. Sin el número decimal
  // (el riel es el que ordena, como en "¿Puede sostenerse tu idea?").
  ol: ({ children }) => <ol className={"my-3 flex list-none flex-col gap-2.5 " + RIEL_CLASES}>{children}</ol>,
  li: ({ children, className }) => {
    const tarea = typeof className === "string" && className.includes("task-list-item");
    return (
      <li
        className={
          "text-[14px] leading-[1.65] [text-wrap:pretty] [&_p]:!my-0 " +
          (tarea ? "flex items-start gap-2.5" : "")
        }
      >
        {children}
      </li>
    );
  },
  // El check de una lista de tareas: verde ejecuta cuando está hecho, aro
  // vacío cuando sigue pendiente. Nunca rojo (regla de color de la casa).
  input: ({ checked }) =>
    checked ? (
      <span
        aria-hidden
        className="mt-[3px] inline-flex h-[15px] w-[15px] shrink-0 items-center justify-center rounded-full bg-done-soft"
        style={{ border: "1.5px solid var(--done)" }}
      >
        <svg width="9" height="9" viewBox="0 0 12 12">
          <path d="M2.5 6.5l2.5 2.5 4.5-5.5" stroke="var(--done)" strokeWidth="2" fill="none" />
        </svg>
      </span>
    ) : (
      <span
        aria-hidden
        className="mt-[3px] inline-block h-[15px] w-[15px] shrink-0 rounded-full"
        style={{ border: "1.5px solid var(--border)" }}
      />
    ),
  blockquote: ({ children }) => (
    <blockquote
      className="my-4 rounded-[10px] bg-surface-2 px-4 py-3 text-[14px] leading-[1.65] text-dim [&_p]:!my-0"
      style={{ borderLeft: "2px solid var(--accent)" }}
    >
      {children}
    </blockquote>
  ),
  strong: ({ children }) => <strong className="font-semibold text-ink">{children}</strong>,
  em: ({ children }) => <em className="text-dim">{children}</em>,
  hr: () => <hr className="my-7 border-hairline" />,
  a: ({ children, href }) => {
    // Enlaces-centinela de fecha (los pone expediente.ts): no son enlaces, son
    // fechas coloreadas. Verde = cumplimiento (hecho), azul = planificación
    // (previsto). El retraso no se castiga: nunca rojo.
    if (href === "#f-hecho") return <span className="font-semibold text-done">{children}</span>;
    if (href === "#f-prev") return <span className="font-semibold text-accent">{children}</span>;
    return (
      <a href={href} className="text-accent underline underline-offset-2">
        {children}
      </a>
    );
  },
  code: ({ children }) => (
    <code className="rounded-[5px] bg-surface-2 px-1.5 py-0.5 text-[13px]">{children}</code>
  ),
  // Una tabla ancha nunca debe empujar la página de lado: rueda en su caja.
  table: ({ children }) => (
    <div className="my-4 overflow-x-auto">
      <table className="w-full border-collapse text-[13.5px]">{children}</table>
    </div>
  ),
  th: ({ children }) => (
    <th className="border-b border-hairline bg-surface-2 px-3 py-2 text-left font-semibold">{children}</th>
  ),
  td: ({ children }) => <td className="border-b border-hairline px-3 py-2 align-top">{children}</td>,
};

/** El CONTENIDO del documento (sin el andamio de tabla/pie), para poder
 * componerlo como una fila más del Expediente o como documento suelto. */
export function ContenidoDocumento({ markdown, titulo }: { markdown: string; titulo: string }) {
  return (
    // data-cuerpo-papel: la hoja de impresión limita la columna de lectura a
    // 600px (Design), aunque la hoja tenga más ancho útil.
    <div data-cuerpo-papel>
      <div className="mb-3 flex items-center gap-2">
        <span aria-hidden className="h-1.5 w-1.5 rounded-full bg-accent" />
        <span className="text-[11px] font-semibold uppercase tracking-[1.2px] text-dim">{titulo}</span>
      </div>
      {/* Sin data-prosa-plan a propósito: ese marcador fuerza tinta plana (prosa
          gris de PANTALLA) y aquí borraría el azul de los títulos y los puntos. */}
      <ReactMarkdown remarkPlugins={[remarkGfm]} components={COMPONENTES}>
        {markdown}
      </ReactMarkdown>
    </div>
  );
}

export function DocumentoPapel({
  markdown,
  nombreIdea,
  titulo,
  oculto,
}: {
  markdown: string;
  nombreIdea: string;
  /** "Tu Plan", "Seguimiento 1", "Expediente completo" */
  titulo: string;
  /** montado solo para imprimir: invisible en pantalla, vivo en papel */
  oculto?: boolean;
}) {
  return (
    <HojaImpresion nombreIdea={nombreIdea} pieTitulo={titulo} oculto={oculto}>
      <FilaPapel>
        <ContenidoDocumento markdown={markdown} titulo={titulo} />
      </FilaPapel>
    </HojaImpresion>
  );
}
