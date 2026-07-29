"use client";

/**
 * Bitacora — Fase 4.8: la bitácora del cliente como PÁGINA en vivo. El usuario
 * la ve antes de imprimirla: "Mi bitácora de mi viaje". Es una LÍNEA DE TIEMPO
 * con una barra vertical y un punto por cada timestamp/actividad; cada día
 * abre su encabezado. Cero motor: solo lee lo que ya pasó.
 *
 * El .md y el PDF salen del MISMO texto (bitacoraMarkdown, la misma verdad que
 * el documento del panel).
 */
import { useCallback, useEffect, useState } from "react";
import { bitacoraMarkdown, type EntradaBitacora } from "@/lib/bitacoraCliente";
import { fechaHumanaConAno, fechaInputLocal } from "@/lib/fechas";
import { DocumentoPapel } from "./DocumentoPapel";

function hora(iso: string): string {
  const d = new Date(iso);
  return `${String(d.getHours()).padStart(2, "0")}:${String(d.getMinutes()).padStart(2, "0")}`;
}

type Fila =
  | { tipo: "dia"; fecha: string; clave: string }
  | { tipo: "entrada"; fecha: string; texto: string; conHora: boolean };

/** Aplana las entradas en filas con encabezado por día; la hora solo en los
 * días con 2+ entradas (regla del historial, igual que el documento). */
function aFilas(entradas: EntradaBitacora[]): Fila[] {
  const porDia = new Map<string, number>();
  for (const e of entradas) {
    const k = fechaInputLocal(new Date(e.fecha));
    porDia.set(k, (porDia.get(k) ?? 0) + 1);
  }
  const filas: Fila[] = [];
  let diaAnterior = "";
  for (const e of entradas) {
    const dia = fechaInputLocal(new Date(e.fecha));
    if (dia !== diaAnterior) {
      filas.push({ tipo: "dia", fecha: e.fecha, clave: dia });
      diaAnterior = dia;
    }
    filas.push({ tipo: "entrada", fecha: e.fecha, texto: e.texto, conHora: (porDia.get(dia) ?? 0) >= 2 });
  }
  return filas;
}

function descargarMd(markdown: string, archivo: string) {
  const blob = new Blob([markdown], { type: "text/markdown;charset=utf-8" });
  const url = URL.createObjectURL(blob);
  const a = document.createElement("a");
  a.href = url;
  a.download = `${archivo}.md`;
  a.click();
  URL.revokeObjectURL(url);
}

export function Bitacora({ projectId, onVolver }: { projectId: string; onVolver: () => void }) {
  const [datos, setDatos] = useState<{ nombre: string; entradas: EntradaBitacora[] } | null>(null);
  const [error, setError] = useState<string | null>(null);
  const [imprimir, setImprimir] = useState<string | null>(null);

  useEffect(() => {
    let vivo = true;
    fetch(`/api/project/${projectId}/bitacora`)
      .then((r) => (r.ok ? r.json() : Promise.reject(new Error(String(r.status)))))
      .then((d: { nombre: string; entradas: EntradaBitacora[] }) => vivo && setDatos(d))
      .catch(() => vivo && setError("No pudimos cargar tu bitácora. Vuelve a intentarlo en un momento."));
    return () => {
      vivo = false;
    };
  }, [projectId]);

  useEffect(() => {
    if (!imprimir) return;
    const limpiar = () => setImprimir(null);
    window.addEventListener("afterprint", limpiar);
    window.print();
    return () => window.removeEventListener("afterprint", limpiar);
  }, [imprimir]);

  const markdown = useCallback(
    () => (datos ? bitacoraMarkdown(datos.nombre, datos.entradas, new Date().toISOString()) : ""),
    [datos]
  );

  if (error) return <p className="text-sm text-warn">{error}</p>;
  if (!datos) return <p className="text-dim">Cargando tu bitácora…</p>;

  const filas = aFilas(datos.entradas);
  const rango =
    datos.entradas.length > 0
      ? `del ${fechaHumanaConAno(datos.entradas[0].fecha)} al ${fechaHumanaConAno(datos.entradas[datos.entradas.length - 1].fecha)}`
      : null;

  return (
    <section className="mx-auto w-full max-w-[720px]">
      <button onClick={onVolver} className="mb-5 text-sm text-dim hover:text-ink" data-no-print>
        ← Volver
      </button>

      <div data-no-print>
        <p className="mb-2 flex items-center gap-2 text-[11px] font-semibold uppercase tracking-[1.2px] text-accent">
          <span aria-hidden className="h-1.5 w-1.5 rounded-full bg-accent" />
          Tu historia
        </p>
        <h2 className="text-[24px] font-bold leading-tight tracking-[-0.02em] [text-wrap:balance] sm:text-[28px]">
          Mi bitácora de mi viaje
        </h2>
        <p className="mt-1.5 text-[15px] text-dim">
          <span className="font-semibold text-ink">«{datos.nombre}»</span>
          {rango ? ` · ${rango}` : ""}
        </p>

        <div className="mt-4 flex flex-wrap gap-2.5">
          <button
            onClick={() => descargarMd(markdown(), `bitacora-${datos.nombre.replace(/[^\p{L}\p{N}]+/gu, "-").slice(0, 40) || "mi-viaje"}`)}
            className="rounded-[9px] border border-hairline px-3.5 py-2 text-[12.5px] font-semibold text-dim hover:border-accent/60 hover:text-ink"
          >
            Descargar .md
          </button>
          <button
            onClick={() => setImprimir(markdown())}
            className="rounded-[9px] border border-accent/45 bg-accent/10 px-3.5 py-2 text-[12.5px] font-semibold text-accent hover:bg-accent/20"
          >
            Imprimir / PDF
          </button>
        </div>

        {datos.entradas.length === 0 ? (
          <p className="mt-8 text-[14px] leading-relaxed text-dim">
            Tu historia apenas empieza. Cada paso que des irá quedando aquí: cada estado que cambies, cada fecha que
            muevas, cada nota.
          </p>
        ) : (
          // LÍNEA DE TIEMPO: una barra vertical con un punto por cada timestamp.
          // La barra pasa por el CENTRO de los puntos (espina continua).
          <div className="relative mt-8">
            <span
              aria-hidden
              className="absolute left-[7px] top-1 bottom-1 w-[2px] rounded-full bg-accent/25"
            />
            <ol className="flex flex-col gap-3.5">
              {filas.map((f, i) =>
                f.tipo === "dia" ? (
                  <li key={`d-${f.clave}`} className={"relative pl-8 " + (i === 0 ? "" : "mt-2")}>
                    {/* nodo de día: aro hueco sobre la barra */}
                    <span
                      aria-hidden
                      className="absolute left-[1px] top-[1px] h-3.5 w-3.5 rounded-full border-2 border-accent bg-bg"
                    />
                    <p className="text-[13px] font-semibold text-accent">{fechaHumanaConAno(f.fecha)}</p>
                  </li>
                ) : (
                  <li key={`e-${i}`} className="relative pl-8">
                    {/* punto lleno sobre la barra */}
                    <span aria-hidden className="absolute left-[3px] top-[5px] h-2.5 w-2.5 rounded-full bg-accent" />
                    <p className="text-[14.5px] leading-relaxed [text-wrap:pretty]">
                      {f.conHora && <span className="mr-2 font-semibold tabular-nums text-dim">{hora(f.fecha)}</span>}
                      {f.texto}
                    </p>
                  </li>
                )
              )}
            </ol>
          </div>
        )}
      </div>

      {/* Invisible en pantalla; la hoja de impresión lo enciende en papel. */}
      {imprimir && <DocumentoPapel oculto markdown={imprimir} nombreIdea={datos.nombre} titulo="Mi bitácora" />}
    </section>
  );
}
