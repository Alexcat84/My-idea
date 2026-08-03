"use client";

/**
 * BitacoraEspacio — campaña "Espacios", Fase 3 (tanda 3). La bitácora de UN
 * espacio dentro de su cara "Tu avance". REUSA la línea de tiempo de la página
 * global (LineaBitacora) y el papel de impresión (BitacoraPapel); las entradas
 * llegan ya filtradas del servidor con `bitacoraDeEspacio` (una fuente, muchas
 * lecturas). Las no-derivables (solo-globales) nunca llegan aquí.
 *
 * Descarga scopeada: .md desde el MISMO texto del servidor (bitacoraMarkdown,
 * titulado "Bitácora de {espacio}") y PDF por impresión del papel filtrado.
 */
import { useEffect, useState } from "react";
import type { EntradaBitacora } from "@/lib/bitacoraCliente";
import { BitacoraPapel } from "./BitacoraPapel";
import { LineaBitacora } from "./Bitacora";

function descargarMd(markdown: string, archivo: string) {
  const blob = new Blob([markdown], { type: "text/markdown;charset=utf-8" });
  const url = URL.createObjectURL(blob);
  const a = document.createElement("a");
  a.href = url;
  a.download = `${archivo}.md`;
  document.body.appendChild(a);
  a.click();
  a.remove();
  URL.revokeObjectURL(url);
}

type Datos = { nombre: string; entradas: EntradaBitacora[]; markdown: string };

export function BitacoraEspacio({ projectId, dominio }: { projectId: string; dominio: string }) {
  const [datos, setDatos] = useState<Datos | null>(null);
  const [error, setError] = useState(false);
  const [imprimir, setImprimir] = useState(false);

  useEffect(() => {
    let vivo = true;
    fetch(`/api/project/${projectId}/bitacora?dominio=${encodeURIComponent(dominio)}`)
      .then((r) => (r.ok ? r.json() : Promise.reject(new Error(String(r.status)))))
      .then((d: Datos) => vivo && setDatos(d))
      .catch(() => vivo && setError(true));
    return () => {
      vivo = false;
    };
  }, [projectId, dominio]);

  // Impresión: el papel se monta oculto y se manda a PDF; se limpia al cerrar.
  useEffect(() => {
    if (!imprimir) return;
    const limpiar = () => setImprimir(false);
    window.addEventListener("afterprint", limpiar);
    window.print();
    return () => window.removeEventListener("afterprint", limpiar);
  }, [imprimir]);

  if (error) return <p className="mt-8 text-[13px] text-warn">No pudimos cargar la bitácora de este espacio.</p>;
  if (!datos) return <p className="mt-8 text-[13px] text-dim">Cargando la bitácora de este espacio…</p>;

  const { nombre, entradas, markdown } = datos;

  return (
    <div className="mt-8">
      <div className="flex flex-wrap items-center justify-between gap-3" data-no-print>
        <p className="text-[11px] font-semibold uppercase tracking-[1.2px] text-dim">Tu bitácora</p>
        {entradas.length > 0 && (
          <div className="flex items-center gap-2">
            <button
              type="button"
              onClick={() => descargarMd(markdown, `Bitácora de ${nombre}`)}
              className="rounded-[9px] border border-hairline px-3 py-1.5 text-[12px] font-semibold text-dim hover:text-ink"
            >
              .md
            </button>
            <button
              type="button"
              onClick={() => setImprimir(true)}
              className="rounded-[9px] border border-hairline px-3 py-1.5 text-[12px] font-semibold text-dim hover:text-ink"
            >
              PDF
            </button>
          </div>
        )}
      </div>

      {entradas.length === 0 ? (
        <p className="mt-3 text-[13px] leading-relaxed text-dim [text-wrap:pretty]">
          Este espacio aún no tiene bitácora. En cuanto registres algo aquí (un estado, una fecha, una nota), su historia
          empezará a quedar guardada.
        </p>
      ) : (
        <LineaBitacora entradas={entradas} />
      )}

      {imprimir && <BitacoraPapel oculto nombreIdea={nombre} entradas={entradas} />}
    </div>
  );
}
