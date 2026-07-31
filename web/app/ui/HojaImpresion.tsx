"use client";

/**
 * HojaImpresion — el ANDAMIO único de impresión (Fase 4.6.1, arreglo del pie).
 *
 * Antes cada documento de papel (cuerpo, resumen, bitácora) traía su PROPIO
 * `<div data-plan-print>` con `position:absolute; top:0` y su PROPIO `<tfoot>`.
 * Al componer el Expediente (los tres juntos) se rompía por dos motivos:
 *   1. tres bloques absolutos en top:0 se ENCIMABAN (el contenido se mezclaba).
 *   2. tres `<tfoot>` distintos → dos pies en una misma página.
 *
 * La cura: UN solo `data-plan-print` (una capa), UNA tabla con UN `<tfoot>` que
 * el navegador repite y cuyo alto RESERVA por página, y las secciones como
 * FILAS del `<tbody>` que fluyen una tras otra (con salto de página opcional).
 * Así el pie es único y siempre al fondo, sin encimados ni duplicados.
 */
import type { ReactNode } from "react";

export function HojaImpresion({
  nombreIdea,
  pieTitulo,
  oculto,
  children,
}: {
  nombreIdea: string;
  /** el rótulo del pie: "Tu Plan", "Expediente", "Mi bitácora", … */
  pieTitulo: string;
  /** montado solo para imprimir: invisible en pantalla, vivo en papel */
  oculto?: boolean;
  /** una o más <FilaPapel> */
  children: ReactNode;
}) {
  return (
    <div
      data-plan-print
      {...(oculto ? { "data-solo-impresion": "" } : {})}
      style={oculto ? { display: "none" } : undefined}
      className={oculto ? undefined : "min-w-0 flex-1"}
    >
      <table data-print-tabla className="w-full border-collapse">
        <tfoot data-print-pie className="hidden">
          <tr>
            <td className="p-0">
              <div className="pie-fila">
                <span>
                  {nombreIdea} · {pieTitulo}
                </span>
                <span>My Idea</span>
              </div>
            </td>
          </tr>
        </tfoot>
        <tbody>{children}</tbody>
      </table>
    </div>
  );
}

/** Una sección del documento, como fila del `<tbody>`. Con `pagina`, empieza en
 * su propia hoja (para separar el resumen y la bitácora dentro del Expediente). */
export function FilaPapel({ pagina, children }: { pagina?: boolean; children: ReactNode }) {
  return (
    <tr>
      <td className="p-0 align-top">{pagina ? <div data-print-pagina="">{children}</div> : children}</td>
    </tr>
  );
}
