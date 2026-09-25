"use client";

/**
 * BorrarIdeaCinta — borrar una idea DESDE el área de ideas (regla del
 * fundador: ideas se gestionan en ideas, no en opciones). Papelera discreta
 * en la esquina de cada cinta, con confirmación en el sitio ("no hay
 * papelera"). DELETE /api/project/[id] (RLS: solo la tuya) + refresco.
 */
import { useState } from "react";
import { useRouter } from "next/navigation";
import { elegir } from "@/lib/i18n/config";
import { useIdioma } from "@/lib/i18n/IdiomaProvider";
import { interpolar } from "@/lib/i18n/interpolar";
import { BORRAR_IDEA } from "@/lib/i18n/mensajes/borrarIdea";

export function BorrarIdeaCinta({ id, nombre }: { id: string; nombre: string }) {
  const t = elegir(BORRAR_IDEA, useIdioma());
  const router = useRouter();
  const [confirmando, setConfirmando] = useState(false);
  const [ocupado, setOcupado] = useState(false);

  async function borrar() {
    if (ocupado) return;
    setOcupado(true);
    try {
      const res = await fetch(`/api/project/${id}`, { method: "DELETE" });
      if (res.ok) router.refresh();
    } finally {
      setOcupado(false);
    }
  }

  if (confirmando) {
    return (
      <span className="absolute right-3 top-3 z-10 flex items-center gap-2 rounded-cinta border border-warn/40 bg-surface px-2.5 py-1.5 shadow-lg">
        <span className="text-[11px] text-warn">{t.borrarla}</span>
        <button onClick={borrar} disabled={ocupado} className="text-[11px] font-semibold text-warn hover:underline disabled:opacity-50">
          {t.si}
        </button>
        <button onClick={() => setConfirmando(false)} className="text-[11px] text-dim hover:text-ink">
          {t.no}
        </button>
      </span>
    );
  }

  return (
    <button
      onClick={() => setConfirmando(true)}
      aria-label={interpolar(t.ariaBorrar, { nombre })}
      title={t.tituloBorrar}
      className="absolute right-3 top-3 z-10 flex h-7 w-7 items-center justify-center rounded-full text-dim/70 hover:bg-warn/10 hover:text-warn"
    >
      <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.8" strokeLinecap="round" strokeLinejoin="round" aria-hidden>
        <path d="M3 6h18" />
        <path d="M8 6V4a1 1 0 0 1 1-1h6a1 1 0 0 1 1 1v2" />
        <path d="M6 6v14a1 1 0 0 0 1 1h10a1 1 0 0 0 1-1V6" />
        <line x1="10" y1="11" x2="10" y2="17" />
        <line x1="14" y1="11" x2="14" y2="17" />
      </svg>
    </button>
  );
}
