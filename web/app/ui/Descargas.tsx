"use client";

/**
 * Descargas — Fase 4.6: lo que el usuario se lleva, una descarga por fase del
 * viaje (Tu Plan, cada Seguimiento) más el expediente con todo el desarrollo.
 * Cada documento sale en .md (para editar y compartir) o en PDF (para leer e
 * imprimir).
 *
 * El PDF se hace con el motor de impresión del navegador: se monta el
 * documento OCULTO en pantalla, la hoja de impresión de globals.css lo
 * enciende en papel, y el usuario elige "Guardar como PDF". Por eso el .md y
 * el PDF salen del MISMO markdown del servidor: dos formatos, un solo texto.
 */
import { useCallback, useEffect, useState } from "react";
import { DocumentoPapel } from "./DocumentoPapel";

import { fechaHumanaConAno } from "@/lib/fechas";
import type { DocumentoIndice } from "@/lib/expediente";

type Formato = "md" | "pdf";

function descargarMd(markdown: string, archivo: string) {
  const blob = new Blob([markdown], { type: "text/markdown;charset=utf-8" });
  const url = URL.createObjectURL(blob);
  const a = document.createElement("a");
  a.href = url;
  a.download = `${archivo}.md`;
  a.click();
  URL.revokeObjectURL(url);
}

function BotonFormato({
  children,
  onClick,
  ocupado,
  destacado,
}: {
  children: React.ReactNode;
  onClick: () => void;
  ocupado: boolean;
  destacado?: boolean;
}) {
  return (
    <button
      onClick={onClick}
      disabled={ocupado}
      className={
        "rounded-[9px] px-3.5 py-2 text-[12.5px] font-semibold disabled:opacity-50 " +
        (destacado
          ? "bg-accent text-white hover:opacity-90"
          : "border border-hairline text-dim hover:border-accent/60 hover:text-ink")
      }
    >
      {ocupado ? "Preparando..." : children}
    </button>
  );
}

/** Una hoja: cada fase del camino deja su documento. */
function IconoHoja() {
  return (
    <svg width="20" height="20" viewBox="0 0 24 24" fill="none" aria-hidden>
      <path
        d="M14 3H7a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2V8l-5-5Z"
        stroke="currentColor"
        strokeWidth="1.6"
        strokeLinejoin="round"
      />
      <path d="M14 3v5h5M8.5 13h7M8.5 16.5h5" stroke="currentColor" strokeWidth="1.6" strokeLinecap="round" strokeLinejoin="round" />
    </svg>
  );
}

/** Hojas apiladas: el expediente es la compilación de todo el camino. */
function IconoExpediente() {
  return (
    <svg width="20" height="20" viewBox="0 0 24 24" fill="none" aria-hidden>
      <path d="M8 7V5a2 2 0 0 1 2-2h5l4 4v9a2 2 0 0 1-2 2h-2" stroke="currentColor" strokeWidth="1.6" strokeLinejoin="round" />
      <path d="M15 3v5h4" stroke="currentColor" strokeWidth="1.6" strokeLinejoin="round" />
      <rect x="3" y="8" width="11" height="13" rx="2" stroke="currentColor" strokeWidth="1.6" />
      <path d="M6 12.5h5M6 16h3.5" stroke="currentColor" strokeWidth="1.6" strokeLinecap="round" />
    </svg>
  );
}

export function Descargas({
  projectId,
  nombreIdea,
  onVolver,
}: {
  projectId: string;
  nombreIdea: string;
  onVolver: () => void;
}) {
  const [documentos, setDocumentos] = useState<DocumentoIndice[] | null>(null);
  const [error, setError] = useState<string | null>(null);
  const [ocupado, setOcupado] = useState<string | null>(null);
  const [paraImprimir, setParaImprimir] = useState<{ titulo: string; markdown: string } | null>(null);

  useEffect(() => {
    let vivo = true;
    fetch(`/api/project/${projectId}/documentos`)
      .then((r) => (r.ok ? r.json() : Promise.reject(new Error(String(r.status)))))
      .then((d: { documentos: DocumentoIndice[] }) => {
        if (vivo) setDocumentos(d.documentos);
      })
      .catch(() => {
        if (vivo) setError("No pudimos cargar tus documentos. Vuelve a intentarlo en un momento.");
      });
    return () => {
      vivo = false;
    };
  }, [projectId]);

  // El documento ya está montado cuando corre este efecto, así que la vista de
  // impresión lo encuentra. Se desmonta al cerrar el diálogo (afterprint).
  useEffect(() => {
    if (!paraImprimir) return;
    const limpiar = () => setParaImprimir(null);
    window.addEventListener("afterprint", limpiar);
    window.print();
    return () => window.removeEventListener("afterprint", limpiar);
  }, [paraImprimir]);

  const pedir = useCallback(
    async (doc: DocumentoIndice, formato: Formato) => {
      setError(null);
      setOcupado(`${doc.clave}:${formato}`);
      try {
        const r = await fetch(`/api/project/${projectId}/documentos?doc=${encodeURIComponent(doc.clave)}`);
        if (!r.ok) throw new Error(String(r.status));
        const d = (await r.json()) as { titulo: string; archivo: string; markdown: string };
        if (formato === "md") descargarMd(d.markdown, d.archivo);
        else setParaImprimir({ titulo: d.titulo, markdown: d.markdown });
      } catch {
        setError("No pudimos preparar ese documento. Vuelve a intentarlo en un momento.");
      } finally {
        setOcupado(null);
      }
    },
    [projectId]
  );

  return (
    <section className="mx-auto w-full max-w-[720px]">
      <button onClick={onVolver} className="mb-5 text-sm text-dim hover:text-ink" data-no-print>
        ← Volver
      </button>

      <div data-no-print>
        <h2 className="text-[24px] font-bold leading-tight tracking-[-0.02em] [text-wrap:balance] sm:text-[28px]">
          Tus documentos
        </h2>
        <p className="mt-2.5 max-w-[560px] text-[14.5px] leading-[1.65] text-dim [text-wrap:pretty]">
          Cada fase de tu camino deja su propio documento. Llévatelos en .md para editarlos o en PDF para leerlos e
          imprimirlos.
        </p>

        {error && <p className="mt-5 text-sm text-warn">{error}</p>}

        {documentos === null && !error && <p className="mt-6 text-sm text-dim">Cargando...</p>}

        {documentos?.length === 0 && (
          <p className="mt-6 text-[14px] leading-relaxed text-dim">
            Todavía no hay nada que descargar. Cuando tengas tu plan, aparecerá aquí.
          </p>
        )}

        <div className="mt-7 flex flex-col gap-3">
          {documentos?.map((doc) => {
            const esExpediente = doc.tipo === "expediente";
            return (
              <div
                key={doc.clave}
                className={
                  "flex flex-wrap items-center gap-x-4 gap-y-3 rounded-panel bg-surface px-5 py-4 transition-colors " +
                  (esExpediente
                    ? "border border-accent/40 hover:border-accent/60"
                    : "border border-hairline hover:border-white/20")
                }
              >
                {/* Icono de documento: una hoja para cada fase; el expediente
                    lleva hojas apiladas (es la compilación de todo). Tinte azul
                    en el expediente, neutro en los ciclos. */}
                <span
                  className={
                    "grid h-11 w-11 shrink-0 place-items-center rounded-[10px] " +
                    (esExpediente ? "bg-accent/10 text-accent" : "bg-surface-2 text-dim")
                  }
                  aria-hidden
                >
                  {esExpediente ? <IconoExpediente /> : <IconoHoja />}
                </span>
                <div className="min-w-[180px] flex-1">
                  <p className="text-[15px] font-semibold leading-snug">{doc.titulo}</p>
                  <p className="mt-0.5 text-[12.5px] leading-[1.5] text-dim [text-wrap:pretty]">{doc.subtitulo}</p>
                  {doc.fecha && (
                    <p className="mt-1.5 text-[12px] text-dim">
                      {esExpediente ? "Cerrado el " : ""}
                      {fechaHumanaConAno(doc.fecha)}
                    </p>
                  )}
                </div>
                <div className="flex shrink-0 gap-2.5">
                  <BotonFormato onClick={() => pedir(doc, "md")} ocupado={ocupado === `${doc.clave}:md`}>
                    .md
                  </BotonFormato>
                  <BotonFormato
                    onClick={() => pedir(doc, "pdf")}
                    ocupado={ocupado === `${doc.clave}:pdf`}
                    destacado={esExpediente}
                  >
                    PDF
                  </BotonFormato>
                </div>
              </div>
            );
          })}
        </div>
      </div>

      {/* Invisible en pantalla; la hoja de impresión lo enciende en papel. */}
      {paraImprimir && (
        <DocumentoPapel
          oculto
          markdown={paraImprimir.markdown}
          nombreIdea={nombreIdea}
          titulo={paraImprimir.titulo}
        />
      )}
    </section>
  );
}
