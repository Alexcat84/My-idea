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
import { DocumentoPapel, ContenidoDocumento } from "./DocumentoPapel";
import { ResumenPapel, ContenidoResumen } from "./ResumenPapel";
import { BitacoraPapel, ContenidoBitacora } from "./BitacoraPapel";
import { AnalisisPapel, type AnalisisPapelData } from "./AnalisisPapel";
import { HojaImpresion, FilaPapel } from "./HojaImpresion";
import type { EntradaBitacora } from "@/lib/bitacoraCliente";

/** Datos estructurados que la ruta manda para dibujar el PDF en papel (no
 * markdown): el resumen "Cómo te fue" y la secuencia. Ausente en los ciclos. */
type ResumenData = {
  cerrada: boolean;
  cierreMotivo: string | null;
  intro: string;
  dias: number;
  accionesCumplidas: number;
  hitos: Array<{ fecha: string; nombre: string }>;
  loQueMovio: string;
  loQuePendiente: string;
};
type PapelDoc = {
  bodyMarkdown?: string;
  resumen?: ResumenData | null;
  entradas?: EntradaBitacora[];
  analisis?: AnalisisPapelData | null;
};

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
  marcado,
}: {
  children: React.ReactNode;
  onClick: () => void;
  ocupado: boolean;
  /** El PDF es el botón MARCADO (contorno azul con tinte), sutil pero bien
   * visible; el .md queda como botón neutro. Igual en TODAS las cintas. */
  marcado?: boolean;
}) {
  return (
    <button
      onClick={onClick}
      disabled={ocupado}
      className={
        "rounded-[10px] border text-[12.5px] disabled:opacity-50 " +
        (marcado
          ? "border-accent/50 bg-accent/15 px-[18px] py-[9px] font-bold text-accent hover:bg-accent/25"
          : "border-white/[0.14] px-4 py-[9px] font-semibold text-dim hover:border-accent/60 hover:text-ink")
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

/** Una hoja con flecha circular: cada Seguimiento recalcula el plan. */
function IconoSeguimiento() {
  return (
    <svg width="20" height="20" viewBox="0 0 24 24" fill="none" aria-hidden>
      <path
        d="M14 3H7a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2V8l-5-5Z"
        stroke="currentColor"
        strokeWidth="1.6"
        strokeLinejoin="round"
      />
      <path d="M14 3v5h5" stroke="currentColor" strokeWidth="1.6" strokeLinejoin="round" />
      <path d="M9 15.5a3 3 0 1 0 1-2.3" stroke="currentColor" strokeWidth="1.6" strokeLinecap="round" strokeLinejoin="round" />
      <path d="M10 11v2.2h2.2" stroke="currentColor" strokeWidth="1.6" strokeLinecap="round" strokeLinejoin="round" />
    </svg>
  );
}

/** Barras: el análisis del proyecto, tu ritmo y cumplimiento de un vistazo. */
function IconoAnalisis() {
  return (
    <svg width="20" height="20" viewBox="0 0 24 24" fill="none" aria-hidden>
      <path d="M4 20V4" stroke="currentColor" strokeWidth="1.6" strokeLinecap="round" />
      <path d="M4 20h16" stroke="currentColor" strokeWidth="1.6" strokeLinecap="round" />
      <rect x="7" y="12" width="3" height="5" rx="0.6" stroke="currentColor" strokeWidth="1.6" />
      <rect x="12.5" y="8" width="3" height="9" rx="0.6" stroke="currentColor" strokeWidth="1.6" />
      <rect x="18" y="14" width="3" height="3" rx="0.6" stroke="currentColor" strokeWidth="1.6" />
    </svg>
  );
}

/** Una línea de tiempo: la bitácora cuenta la secuencia del viaje. */
function IconoBitacora() {
  return (
    <svg width="20" height="20" viewBox="0 0 24 24" fill="none" aria-hidden>
      <path d="M6 4v16" stroke="currentColor" strokeWidth="1.6" strokeLinecap="round" />
      <circle cx="6" cy="7" r="1.6" fill="currentColor" />
      <circle cx="6" cy="12.5" r="1.6" fill="currentColor" />
      <circle cx="6" cy="18" r="1.6" fill="currentColor" />
      <path d="M10 7h9M10 12.5h9M10 18h6" stroke="currentColor" strokeWidth="1.6" strokeLinecap="round" />
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
  const [paraImprimir, setParaImprimir] = useState<{ titulo: string; markdown: string; papel?: PapelDoc } | null>(null);

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
        const d = (await r.json()) as { titulo: string; archivo: string; markdown: string; papel?: PapelDoc };
        if (formato === "md") descargarMd(d.markdown, d.archivo);
        else setParaImprimir({ titulo: d.titulo, markdown: d.markdown, papel: d.papel });
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
            const esSeguimiento = /^seguimiento/i.test(doc.titulo);
            return (
              <div
                key={doc.clave}
                className={
                  "flex flex-wrap items-center gap-x-5 gap-y-3 rounded-[14px] bg-surface px-6 py-5 transition-colors hover:bg-[#141419] " +
                  (esExpediente
                    ? "border border-accent/[0.28] hover:border-accent/[0.34]"
                    : "border border-hairline hover:border-accent/[0.34]")
                }
              >
                {/* Icono por fase (trazo 1.6px) en chip azul: hoja=Tu Plan, hoja
                    con flecha=Seguimiento, línea de tiempo=bitácora, hojas
                    apiladas=Expediente. El Expediente es el único con chip azul
                    pleno y trazo oscuro, porque contiene a los demás. */}
                <span
                  className={
                    "grid h-[52px] w-[52px] shrink-0 place-items-center rounded-[12px] " +
                    (esExpediente ? "bg-accent text-[#07070A]" : "bg-accent/12 text-[#7B9DFF]")
                  }
                  aria-hidden
                >
                  {esExpediente ? (
                    <IconoExpediente />
                  ) : doc.tipo === "analisis" || doc.tipo === "reporte" ? (
                    <IconoAnalisis />
                  ) : doc.tipo === "bitacora" ? (
                    <IconoBitacora />
                  ) : esSeguimiento ? (
                    <IconoSeguimiento />
                  ) : (
                    <IconoHoja />
                  )}
                </span>
                <div className="min-w-[180px] flex-1">
                  {/* Fase 3 (tanda 5): la etiqueta de espacio de un documento por
                      mundo (solo los reportes la traen; los del viaje, no). */}
                  {doc.espacio && (
                    <span className="mb-1 inline-flex items-center rounded-full border border-hairline bg-surface-3 px-2 py-0.5 text-[10px] font-semibold uppercase tracking-[0.6px] text-dim">
                      {doc.espacio}
                    </span>
                  )}
                  <p className="text-[15px] font-semibold leading-snug">{doc.titulo}</p>
                  <p className="mt-0.5 text-[12.5px] leading-[1.5] text-dim [text-wrap:pretty]">{doc.subtitulo}</p>
                  {doc.fecha && (
                    <p className="mt-1.5 text-[12px] tabular-nums text-[#6F7076]">
                      {esExpediente ? "Cerrado el " : ""}
                      {fechaHumanaConAno(doc.fecha)}
                    </p>
                  )}
                </div>
                {/* El panel de documentos SOLO descarga (.md / PDF). "Ver" la
                    bitácora en vivo vive en las páginas de desarrollo (plan,
                    Manos, mundos), no aquí. */}
                <div className="flex shrink-0 gap-2.5">
                  <BotonFormato onClick={() => pedir(doc, "md")} ocupado={ocupado === `${doc.clave}:md`}>
                    .md
                  </BotonFormato>
                  <BotonFormato onClick={() => pedir(doc, "pdf")} ocupado={ocupado === `${doc.clave}:pdf`} marcado>
                    PDF
                  </BotonFormato>
                </div>
              </div>
            );
          })}
        </div>

        {/* Cierre de la lista (Design): recuerda que .md y PDF son el mismo
            texto, y dónde vive la bitácora en vivo. */}
        {documentos && documentos.length > 0 && (
          <p className="mt-5 text-[12.5px] leading-relaxed text-dim [text-wrap:pretty]">
            El .md y el PDF salen del mismo texto: lo que lees aquí es lo que se imprime. Tu bitácora en vivo se
            abre desde el plan, desde Manos a la Obra y desde tus mundos.
          </p>
        )}
      </div>

      {/* Invisible en pantalla; la hoja de impresión lo enciende en papel.
          El Expediente compone: cuerpo (markdown) + resumen "Cómo te fue" y
          secuencia ESTRUCTURADOS (cada uno en su hoja). La bitácora suelta va
          como timeline estructurado. Los ciclos, como markdown. */}
      {paraImprimir &&
        (() => {
          const p = paraImprimir.papel;
          if (p?.bodyMarkdown) {
            // El Expediente compone en UNA sola hoja (un solo pie que se repite
            // y reserva su alto): cuerpo + resumen + bitácora, cada uno en su
            // hoja. Antes eran tres bloques absolutos que se encimaban y traían
            // tres pies (dos por página). Ahora fluyen como filas.
            return (
              <HojaImpresion oculto nombreIdea={nombreIdea} pieTitulo="Expediente">
                <FilaPapel>
                  <ContenidoDocumento markdown={p.bodyMarkdown} titulo="Expediente completo" />
                </FilaPapel>
                {p.resumen && (
                  <FilaPapel pagina>
                    <ContenidoResumen nombreIdea={nombreIdea} {...p.resumen} />
                  </FilaPapel>
                )}
                {p.entradas && p.entradas.length > 0 && (
                  <FilaPapel pagina>
                    <ContenidoBitacora entradas={p.entradas} />
                  </FilaPapel>
                )}
              </HojaImpresion>
            );
          }
          if (p?.analisis) {
            return <AnalisisPapel oculto nombre={nombreIdea} nombreIdea={nombreIdea} datos={p.analisis} />;
          }
          if (p?.resumen) {
            return <ResumenPapel oculto nombreIdea={nombreIdea} {...p.resumen} />;
          }
          if (p?.entradas) {
            return <BitacoraPapel oculto nombreIdea={nombreIdea} entradas={p.entradas} />;
          }
          return <DocumentoPapel oculto markdown={paraImprimir.markdown} nombreIdea={nombreIdea} titulo={paraImprimir.titulo} />;
        })()}
    </section>
  );
}
