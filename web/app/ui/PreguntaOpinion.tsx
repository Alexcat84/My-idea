"use client";
/**
 * La pregunta de un clic en los momentos clave (decisión del fundador, 8 oct 2026): "¿Qué tal salió tu plan?" al
 * recibir un plan, un plan de mundo, una profundización o un replanteamiento, y "¿Qué tal va tu idea?" de vez en
 * cuando en el seguimiento.
 *
 * Una tarjeta discreta DENTRO de la pantalla, nunca un modal. Quien decide si aparece es el servidor
 * (/api/opiniones, lib/opiniones.ts): solo cuentas reales, una sola vez por plan, con tope de frecuencia. Cerrar sin
 * responder también se guarda, para no volver a preguntar. Si elige "Malo", la opinión se guarda al instante y luego
 * se le ofrecen las opciones rápidas y un texto opcional, que la completan.
 *
 * TarjetaOpinion es lo visual (una fase a la vez, probado en estático: preguntaOpinion.test.tsx); PreguntaOpinion
 * habla con la ruta.
 */
import { useEffect, useState } from "react";
import { elegir } from "@/lib/i18n/config";
import { useIdioma } from "@/lib/i18n/IdiomaProvider";
import { OPINIONES } from "@/lib/i18n/mensajes/opiniones";
import { OPINIONES_MOTIVO, type OpinionMotivo, type OpinionValoracion } from "@/lib/dbContract";
import { TEXTO_MAX } from "@/lib/opiniones";
import { CampoConVoz } from "./CampoConVoz";

export type FaseTarjeta = "preguntar" | "malo" | "gracias";
export type TipoTarjeta = "plan" | "plan_mundo" | "profundizacion" | "replanteamiento" | "seguimiento";

const VALORACIONES: OpinionValoracion[] = ["malo", "bueno", "excelente"];

function Cerrar({ etiqueta, onClick, deshabilitado }: { etiqueta: string; onClick: () => void; deshabilitado: boolean }) {
  return (
    <button
      type="button"
      onClick={onClick}
      disabled={deshabilitado}
      aria-label={etiqueta}
      title={etiqueta}
      className="-me-1 -mt-1 grid h-7 w-7 shrink-0 place-items-center rounded-full text-dim hover:bg-white/5 hover:text-ink disabled:opacity-50"
    >
      <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2.4" strokeLinecap="round" aria-hidden>
        <path d="M6 6l12 12M18 6L6 18" />
      </svg>
    </button>
  );
}

export function TarjetaOpinion({
  tipo,
  fase,
  motivo,
  texto,
  ocupado,
  error,
  onValorar,
  onCerrar,
  onMotivo,
  onTexto,
  onEnviarDetalle,
}: {
  tipo: TipoTarjeta;
  fase: FaseTarjeta;
  motivo: OpinionMotivo | null;
  texto: string;
  ocupado: boolean;
  error: string | null;
  onValorar: (v: OpinionValoracion) => void;
  onCerrar: () => void;
  onMotivo: (m: OpinionMotivo) => void;
  onTexto: (t: string) => void;
  onEnviarDetalle: () => void;
}) {
  const t = elegir(OPINIONES, useIdioma()).tarjeta;
  const pregunta = t.pregunta[tipo];

  if (fase === "gracias") {
    return (
      <section aria-label={pregunta} className="rounded-panel border border-hairline bg-surface px-4 py-3">
        <p role="status" className="text-[13px] text-dim">
          {t.gracias}
        </p>
      </section>
    );
  }

  return (
    <section aria-label={pregunta} className="rounded-panel border border-hairline bg-surface px-4 py-3.5">
      <div className="flex items-start gap-3">
        <p className="flex-1 text-[14px] font-medium leading-snug">{fase === "malo" ? t.queFallo : pregunta}</p>
        <Cerrar etiqueta={t.cerrar} onClick={onCerrar} deshabilitado={ocupado} />
      </div>

      {fase === "preguntar" && (
        <div className="mt-3 flex flex-wrap gap-2">
          {VALORACIONES.map((v) => (
            <button
              key={v}
              type="button"
              onClick={() => onValorar(v)}
              disabled={ocupado}
              className="rounded-cinta border border-hairline px-4 py-1.5 text-[13px] text-ink hover:border-accent/50 hover:text-accent disabled:opacity-50"
            >{t.valoracion[v]}</button>
          ))}
        </div>
      )}

      {fase === "malo" && (
        <div className="mt-3 flex flex-col gap-3">
          <div className="flex flex-wrap gap-2">
            {OPINIONES_MOTIVO.map((m) => (
              <button
                key={m}
                type="button"
                aria-pressed={motivo === m}
                onClick={() => onMotivo(m)}
                disabled={ocupado}
                className={
                  "rounded-cinta border px-3.5 py-1.5 text-[13px] disabled:opacity-50 " +
                  (motivo === m ? "border-accent/60 bg-accent/10 text-accent" : "border-hairline text-ink hover:border-accent/50")
                }
              >{t.motivo[m]}</button>
            ))}
          </div>
          <CampoConVoz id={`opinion-${tipo}`} valor={texto} onCambio={(v) => onTexto(v.slice(0, TEXTO_MAX))} filas={2} placeholder={t.textoOpcional} deshabilitado={ocupado} />
          <div>
            <button
              type="button"
              onClick={onEnviarDetalle}
              disabled={ocupado || (!motivo && !texto.trim())}
              className="rounded-[9px] border border-accent/40 bg-accent/10 px-4 py-1.5 text-[13px] font-semibold text-accent hover:bg-accent/20 disabled:opacity-50"
            >{t.enviar}</button>
          </div>
        </div>
      )}

      {error && (
        <p role="alert" className="mt-2 text-[12.5px] text-warn">
          {error}
        </p>
      )}
    </section>
  );
}

/** La tarjeta viva: pregunta al servidor si toca y guarda lo que la persona elige. Sin tarjeta, no pinta nada. */
export function PreguntaOpinion(props: { sesionId?: string | null; seguimiento?: string | null; className?: string }) {
  const t = elegir(OPINIONES, useIdioma()).tarjeta;
  const objetivo = props.sesionId ? { sesion: props.sesionId } : props.seguimiento ? { seguimiento: props.seguimiento } : null;
  const clave = objetivo ? Object.entries(objetivo)[0].join("=") : null;
  const [tipo, setTipo] = useState<TipoTarjeta | null>(null);
  const [fase, setFase] = useState<FaseTarjeta | "oculta">("oculta");
  const [motivo, setMotivo] = useState<OpinionMotivo | null>(null);
  const [texto, setTexto] = useState("");
  const [idOpinion, setIdOpinion] = useState<string | null>(null);
  const [ocupado, setOcupado] = useState(false);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    if (!clave) return;
    let vivo = true;
    setFase("oculta");
    fetch(`/api/opiniones?${clave}`)
      .then((r) => (r.ok ? r.json() : { preguntar: false }))
      .then((d: { preguntar?: boolean; tipo?: TipoTarjeta }) => {
        if (vivo && d.preguntar && d.tipo) {
          setTipo(d.tipo);
          setFase("preguntar");
        }
      })
      .catch(() => {});
    return () => {
      vivo = false;
    };
  }, [clave]);

  if (!objetivo || !tipo || fase === "oculta") return null;

  async function enviar(metodo: "POST" | "PATCH", cuerpo: Record<string, unknown>): Promise<{ id?: string } | null> {
    setOcupado(true);
    setError(null);
    try {
      const r = await fetch("/api/opiniones", { method: metodo, headers: { "content-type": "application/json" }, body: JSON.stringify(cuerpo) });
      if (!r.ok) throw new Error(String(r.status));
      return (await r.json()) as { id?: string };
    } catch {
      setError(t.noGuardada);
      return null;
    } finally {
      setOcupado(false);
    }
  }

  return (
    <div className={props.className}>
      <TarjetaOpinion
        tipo={tipo}
        fase={fase}
        motivo={motivo}
        texto={texto}
        ocupado={ocupado}
        error={error}
        onValorar={async (v) => {
          const r = await enviar("POST", { ...objetivo, valoracion: v });
          if (!r) return;
          if (v === "malo") {
            setIdOpinion(r.id ?? null);
            setFase("malo");
          } else setFase("gracias");
        }}
        onCerrar={async () => {
          // En "Malo" la opinión ya está guardada: cerrar solo cierra. En la pregunta, se guarda el cierre.
          if (fase === "preguntar" && !(await enviar("POST", objetivo))) return;
          setFase("oculta");
        }}
        onMotivo={(m) => setMotivo(motivo === m ? null : m)}
        onTexto={setTexto}
        onEnviarDetalle={async () => {
          if (idOpinion && !(await enviar("PATCH", { id: idOpinion, motivo, texto: texto.trim() || null }))) return;
          setFase("gracias");
        }}
      />
    </div>
  );
}
