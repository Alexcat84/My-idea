"use client";

/**
 * CambiadorEspacios — campaña "Espacios". Los espacios del proyecto como
 * PESTAÑAS-FICHERO (folders): cada mundo es un expediente del mismo proyecto, y
 * el core ("Tu viaje") otro. Cada pestaña lleva su ICONO y su NOMBRE de cara; la
 * activa se "levanta" (fondo de superficie, borde superior en acento, icono y
 * texto en azul) y se conecta con el contenido de abajo. El "+" abre otro mundo
 * (lleva a la fila). Scroll horizontal a 380; nunca comprime las pestañas.
 *
 * Tema oscuro de la casa (adaptación del patrón de tabs-fichero que pidió el
 * fundador). El icono sale del mismo juego que la fila de potenciadores.
 */
import { Icono } from "./PotenciaTuIdea";

export function CambiadorEspacios({
  activo,
  mundos,
  onIrIdea,
  onIrCore,
  onIrMundo,
  onMas,
}: {
  /** el espacio actual: "idea" (el nivel general), "core" o el dominio del mundo */
  activo: string;
  /** los mundos ACTIVOS (con su nombre de cara), en orden de la fila */
  mundos: { dominio: string; nombre: string }[];
  /** Frente "La idea completa": el nivel GENERAL. Se muestra como entrada
   * distinguida AL FRENTE (aparece solo con >=1 mundo, que es cuando este
   * cambiador existe). null = sin nivel general (no debería pasar aquí). */
  onIrIdea?: () => void;
  onIrCore: () => void;
  onIrMundo: (dominio: string) => void;
  onMas: () => void;
}) {
  const claseTab = (activa: boolean) =>
    "group relative flex min-w-[86px] shrink-0 flex-col items-center gap-1.5 rounded-t-[12px] border border-b-0 px-5 pt-2.5 pb-3 transition-[background,border-color] duration-150 " +
    (activa
      ? "-mb-px border-hairline border-t-2 border-t-accent bg-surface"
      : "border-transparent hover:bg-surface-2/50");

  const claseNombre = (activa: boolean) =>
    "text-[12.5px] font-semibold whitespace-nowrap " +
    (activa ? "text-accent" : "text-dim group-hover:text-ink");

  return (
    <div
      role="tablist"
      aria-label="Los espacios de tu proyecto"
      className="mb-6 flex items-stretch gap-1 overflow-x-auto border-b border-hairline [scrollbar-width:none] [&::-webkit-scrollbar]:hidden"
    >
      {/* El nivel GENERAL: distinguido (verde del agregado), NO un espacio. Va al
          frente y jamás es un tercer riel: es una entrada más del mismo cambiador. */}
      {onIrIdea && (
        <button
          role="tab"
          aria-selected={activo === "idea"}
          onClick={onIrIdea}
          className={
            "group relative flex min-w-[92px] shrink-0 flex-col items-center gap-1.5 rounded-t-[12px] border border-b-0 px-5 pt-2.5 pb-3 transition-[background,border-color] duration-150 " +
            (activo === "idea" ? "-mb-px border-hairline border-t-2 border-t-done bg-surface" : "border-transparent hover:bg-surface-2/50")
          }
        >
          <span aria-hidden className={"text-[15px] leading-none " + (activo === "idea" ? "text-done" : "text-dim group-hover:text-ink")}>◎</span>
          <span className={"text-[12.5px] font-semibold whitespace-nowrap " + (activo === "idea" ? "text-done" : "text-dim group-hover:text-ink")}>
            La idea completa
          </span>
        </button>
      )}

      <button role="tab" aria-selected={activo === "core"} onClick={onIrCore} className={claseTab(activo === "core")}>
        <Icono clave="core" activo={activo === "core"} />
        <span className={claseNombre(activo === "core")}>Tu viaje</span>
      </button>

      {mundos.map((m) => {
        const activa = activo === m.dominio;
        return (
          <button
            key={m.dominio}
            role="tab"
            aria-selected={activa}
            onClick={() => onIrMundo(m.dominio)}
            className={claseTab(activa)}
          >
            <Icono clave={m.dominio} activo={activa} />
            <span className={claseNombre(activa)}>{m.nombre}</span>
          </button>
        );
      })}

      <button
        onClick={onMas}
        aria-label="Añadir un mundo"
        title="Añadir un mundo"
        className="group flex min-w-[72px] shrink-0 flex-col items-center justify-center gap-1.5 rounded-t-[12px] border border-b-0 border-transparent px-4 pt-2.5 pb-3 text-dim transition-colors hover:bg-surface-2/50 hover:text-ink"
      >
        <span className="text-2xl leading-none">+</span>
        <span className="text-[12.5px] font-semibold">Mundo</span>
      </button>
    </div>
  );
}
