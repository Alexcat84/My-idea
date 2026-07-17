"use client";

/**
 * CierreHonesto — Fase 4.3 §2. Cuando el motor decide 'salir', la pantalla
 * JAMÁS se queda muda.
 *
 * El hallazgo que lo obligó (barrido de 380): el intérprete salía de un mundo,
 * `IdeaView` hacía `setPregunta(null)` y NADA más, y el usuario —que había
 * pagado 3 créditos por explorar ese mundo— se quedaba mirando una pantalla sin
 * pregunta, sin plan y sin explicación. Degradación silenciosa en su cara.
 *
 * Este componente es incondicional a propósito: aunque la Fase 4.3 §1 haga que
 * el motor casi nunca abandone un mundo, el día que abandone —por la razón que
 * sea— el usuario recibe una explicación y dos salidas. La regla del BANCO §9
 * ("fallar ruidoso, no mentir calladito") también aplica de cara al usuario, no
 * solo de cara al log.
 *
 * El texto NO se inventa aquí: viaja desde el servidor (`mensaje`), que es quien
 * sabe si el cierre fue de un mundo incompatible (con su reembolso) o del viaje
 * core. La UI lo pinta.
 */
export function CierreHonesto({
  mensaje,
  creditosDevueltos,
  hayPlan,
  onVolverAManos,
  onVerMundos,
}: {
  mensaje: string;
  /** Fase 4.3.2 (regla de claims): créditos DE VERDAD devueltos, respaldados por
   * un evento del ledger. null = no hubo consumo que devolver (p.ej. beta
   * gratis): NO se muestra ninguna afirmación de dinero. El hecho de que el
   * mundo quedó reabierto ya lo dice el `mensaje` del servidor. */
  creditosDevueltos?: number | null;
  /** con plan, la salida natural es Manos a la Obra; sin él, los mundos */
  hayPlan: boolean;
  onVolverAManos: () => void;
  onVerMundos: () => void;
}) {
  return (
    <section
      className="rounded-panel border border-hairline bg-surface p-6 sm:p-7"
      aria-live="polite"
      data-cierre-honesto
    >
      <p className="mb-3 text-[11px] font-semibold uppercase tracking-[1.2px] text-dim">
        Hasta aquí llega este camino
      </p>
      <p className="text-[17px] font-medium leading-relaxed [text-wrap:pretty]">{mensaje}</p>
      {typeof creditosDevueltos === "number" && creditosDevueltos > 0 && (
        <p className="mt-3 text-[13px] text-done">
          Te devolvimos {creditosDevueltos} {creditosDevueltos === 1 ? "crédito" : "créditos"} de la
          activación. Nunca pierdes créditos por algo que no te sirvió.
        </p>
      )}
      <div className="mt-5 flex flex-wrap items-center gap-3">
        {hayPlan && (
          <button
            onClick={onVolverAManos}
            className="rounded-[10px] bg-done px-5 py-2.5 text-[13.5px] font-semibold text-[#04120A] hover:opacity-90"
          >
            Volver a Manos a la Obra
          </button>
        )}
        <button
          onClick={onVerMundos}
          className={
            hayPlan
              ? "rounded-[10px] border border-white/15 px-4 py-2.5 text-[13px] text-dim hover:border-accent/60 hover:text-ink"
              : "rounded-[10px] bg-accent px-5 py-2.5 text-[13.5px] font-semibold text-white hover:opacity-90"
          }
        >
          Ver los otros mundos
        </button>
      </div>
    </section>
  );
}
