"use client";
/**
 * "Comentarios y sugerencias" de la cuenta (decisión del fundador, 8 oct 2026): un espacio para escribir lo que la
 * persona piensa de la app, con valoración opcional. Se guarda como opinión 'general' por /api/opiniones, con su tope
 * diario. FormularioComentarios es lo visual (probado en estático: preguntaOpinion.test.tsx).
 */
import { useState } from "react";
import { elegir } from "@/lib/i18n/config";
import { interpolar } from "@/lib/i18n/interpolar";
import { useIdioma } from "@/lib/i18n/IdiomaProvider";
import { OPINIONES } from "@/lib/i18n/mensajes/opiniones";
import type { OpinionValoracion } from "@/lib/dbContract";
import { TEXTO_MAX } from "@/lib/opiniones";
import { CampoConVoz } from "./CampoConVoz";

const VALORACIONES: OpinionValoracion[] = ["malo", "bueno", "excelente"];

export function FormularioComentarios({
  texto,
  valoracion,
  enviado,
  ocupado,
  error,
  onTexto,
  onValoracion,
  onEnviar,
  onOtro,
}: {
  texto: string;
  valoracion: OpinionValoracion | null;
  enviado: boolean;
  ocupado: boolean;
  error: string | null;
  onTexto: (t: string) => void;
  onValoracion: (v: OpinionValoracion | null) => void;
  onEnviar: () => void;
  onOtro: () => void;
}) {
  const idioma = useIdioma();
  const o = elegir(OPINIONES, idioma);
  const c = o.cuenta;

  if (enviado) {
    return (
      <div className="flex flex-wrap items-center gap-3">
        <p role="status" className="text-sm text-dim">
          {c.enviado}
        </p>
        <button type="button" onClick={onOtro} className="text-[13px] text-accent hover:underline">{c.otro}</button>
      </div>
    );
  }

  return (
    <div className="flex flex-col gap-3">
      <p className="text-sm text-dim">{c.descripcion}</p>
      <div>
        <p className="mb-2 text-[12.5px] text-dim">{c.valoracionOpcional}</p>
        <div className="flex flex-wrap gap-2">
          {VALORACIONES.map((v) => (
            <button
              key={v}
              type="button"
              aria-pressed={valoracion === v}
              onClick={() => onValoracion(valoracion === v ? null : v)}
              disabled={ocupado}
              className={
                "rounded-cinta border px-4 py-1.5 text-[13px] disabled:opacity-50 " +
                (valoracion === v ? "border-accent/60 bg-accent/10 text-accent" : "border-hairline text-ink hover:border-accent/50")
              }
            >{o.tarjeta.valoracion[v]}</button>
          ))}
        </div>
      </div>
      <CampoConVoz id="comentarios-sugerencias" valor={texto} onCambio={(v) => onTexto(v.slice(0, TEXTO_MAX))} filas={4} placeholder={c.placeholder} deshabilitado={ocupado} />
      <div className="flex items-center gap-3">
        <button
          type="button"
          onClick={onEnviar}
          disabled={ocupado || !texto.trim()}
          className="rounded-cinta border border-accent/40 bg-accent/10 px-5 py-2 text-sm font-medium text-accent hover:bg-accent/20 disabled:opacity-50"
        >{c.enviar}</button>
        <span className="ms-auto text-[12px] tabular-nums text-dim">{interpolar(c.contador, { n: texto.length, max: TEXTO_MAX })}</span>
      </div>
      {error && (
        <p role="alert" className="text-[12.5px] text-warn">
          {error}
        </p>
      )}
    </div>
  );
}

export function ComentariosSugerencias() {
  const c = elegir(OPINIONES, useIdioma()).cuenta;
  const [texto, setTexto] = useState("");
  const [valoracion, setValoracion] = useState<OpinionValoracion | null>(null);
  const [enviado, setEnviado] = useState(false);
  const [ocupado, setOcupado] = useState(false);
  const [error, setError] = useState<string | null>(null);

  async function enviar() {
    setOcupado(true);
    setError(null);
    try {
      const r = await fetch("/api/opiniones", {
        method: "POST",
        headers: { "content-type": "application/json" },
        body: JSON.stringify({ general: true, texto: texto.trim(), valoracion }),
      });
      if (!r.ok) {
        const d = (await r.json().catch(() => ({}))) as { error?: string };
        setError(r.status === 429 && d.error ? d.error : c.noEnviado);
        return;
      }
      setEnviado(true);
      setTexto("");
      setValoracion(null);
    } catch {
      setError(c.noEnviado);
    } finally {
      setOcupado(false);
    }
  }

  return (
    <FormularioComentarios
      texto={texto}
      valoracion={valoracion}
      enviado={enviado}
      ocupado={ocupado}
      error={error}
      onTexto={setTexto}
      onValoracion={setValoracion}
      onEnviar={() => void enviar()}
      onOtro={() => setEnviado(false)}
    />
  );
}
