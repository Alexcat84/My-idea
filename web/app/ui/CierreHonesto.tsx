"use client";

/**
 * CierreHonesto — FASE B (canon 12). Cuando el motor decide 'salir', la
 * pantalla JAMÁS se queda muda (ley de la Fase 4.3 §2, sigue siendo suprema).
 *
 * Dos estados: el CAMINO sin salida (core) y el MUNDO que no encaja (con su
 * reembolso). Confesión con dignidad, no disculpa.
 *
 * El texto NO se inventa aquí: título y cuerpo vienen del servidor; el
 * "porqué" es la CAJA DE VIDRIO, el motivo REAL que registró el intérprete
 * (nunca prosa genérica). Compat (amarre 1): si un payload viejo o un camino
 * no migrado entrega solo `cuerpo` sin `titulo`/`porque`, se pinta el cuerpo
 * sin estructura, y nada se rompe.
 *
 * Reembolso solo-con-ledger (Fase 4.3.2): el chip y la nota de créditos
 * devueltos aparecen SOLO si `creditosDevueltos` trae un número respaldado por
 * el ledger. En beta la activación es gratis: no hay claim de dinero.
 */
export function CierreHonesto({
  tipo,
  titulo,
  cuerpo,
  porque,
  creditosDevueltos,
  hayPlan,
  onVolverAManos,
  onVolverAIdea,
  onExplorarOtroAngulo,
  onVerMundos,
}: {
  tipo: "camino" | "mundo";
  /** null cuando el payload es el viejo/plano (compat): se pinta solo el cuerpo. */
  titulo: string | null;
  cuerpo: string;
  /** El motivo REAL del intérprete (caja de vidrio). null = no hubo: no se pinta la caja. */
  porque: string | null;
  creditosDevueltos?: number | null;
  hayPlan: boolean;
  onVolverAManos: () => void;
  onVolverAIdea: () => void;
  onExplorarOtroAngulo: () => void;
  onVerMundos: () => void;
}) {
  const esMundo = tipo === "mundo";
  const hayReembolso = typeof creditosDevueltos === "number" && creditosDevueltos > 0;
  return (
    <section
      className="rounded-panel border border-hairline bg-surface p-6 sm:p-8"
      aria-live="polite"
      data-cierre-honesto
    >
      <div className="flex flex-wrap items-center justify-between gap-3">
        <p className="text-[11px] font-semibold uppercase tracking-[1.3px] text-dim">Un alto honesto</p>
        {esMundo && hayReembolso && (
          <span className="rounded-full border border-done/45 bg-done/[0.08] px-3 py-1.5 text-[12px] font-semibold text-done">
            Activación devuelta · {creditosDevueltos} {creditosDevueltos === 1 ? "crédito" : "créditos"}
          </span>
        )}
      </div>

      {titulo ? (
        <>
          <h2 className="mt-3.5 text-[22px] font-bold leading-snug [text-wrap:pretty] sm:text-[26px]">{titulo}</h2>
          <p className="mt-3 text-[15.5px] leading-relaxed text-dim [text-wrap:pretty]">{cuerpo}</p>
        </>
      ) : (
        // Compat: sin título estructurado, el cuerpo es el mensaje principal.
        <p className="mt-3.5 text-[17px] font-medium leading-relaxed [text-wrap:pretty]">{cuerpo}</p>
      )}

      {porque && (
        <div className="mt-5 rounded-panel border border-hairline bg-surface-2 px-5 py-4">
          <div className="text-[12px] font-semibold uppercase tracking-[1.2px] text-dim">
            {esMundo ? "Por qué este mundo, no ahora" : "Lo que vi"}
          </div>
          <p className="mt-2 text-[14px] leading-relaxed [text-wrap:pretty]">{porque}</p>
        </div>
      )}

      {esMundo && hayReembolso && (
        <div className="mt-4 flex gap-3 rounded-panel border border-done/30 bg-done/[0.05] px-4 py-3.5">
          <svg
            className="mt-0.5 h-[18px] w-[18px] flex-none stroke-done"
            viewBox="0 0 24 24"
            fill="none"
            strokeWidth="2"
            strokeLinecap="round"
            strokeLinejoin="round"
            aria-hidden
          >
            <path d="M3 12a9 9 0 1 0 9-9 9.7 9.7 0 0 0-6.7 2.8L3 8" />
            <path d="M3 3v5h5" />
          </svg>
          <span className="text-[13.5px] leading-relaxed text-done/90">
            Te devolvimos {creditosDevueltos} {creditosDevueltos === 1 ? "crédito" : "créditos"} de la activación.
            Nunca pierdes créditos por algo que no te sirvió.
          </span>
        </div>
      )}

      <div className="mt-6 flex flex-wrap items-center gap-3">
        <button
          onClick={esMundo || hayPlan ? onVolverAManos : onVolverAIdea}
          className="rounded-[10px] bg-done px-5 py-2.5 text-[13.5px] font-semibold text-[#04120A] hover:opacity-90"
        >
          {esMundo || hayPlan ? "Volver a Manos a la Obra" : "Volver a mi idea"}
        </button>
        <button
          onClick={esMundo ? onVerMundos : onExplorarOtroAngulo}
          className="rounded-[10px] border border-white/15 px-4 py-2.5 text-[13px] text-dim hover:border-accent/60 hover:text-ink"
        >
          {esMundo ? "Ver los otros mundos" : "Explorar otro ángulo de la idea"}
        </button>
      </div>

      <p className="mt-5 text-[13px] leading-relaxed text-dim">
        {esMundo
          ? "Tu viaje principal sigue intacto: cerrar este mundo no toca tu idea."
          : "Nada se pierde: tu recorrido y tu Claridad quedan guardados tal como están."}
      </p>
    </section>
  );
}
