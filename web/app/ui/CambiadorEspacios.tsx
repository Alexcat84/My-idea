"use client";

/**
 * CambiadorEspacios — campaña "Espacios". La barra de tabs que salta entre los
 * espacios del proyecto en un clic: "Tu viaje" (el core) · cada mundo activo por
 * su NOMBRE DE CARA · "+". El "+" lleva a la fila de potenciadores (a activar
 * otro mundo). Scroll horizontal a 380 (nunca comprime los tabs); el tab activo
 * es evidente (acento pleno). Sin la barra, un mundo y el core se sienten
 * pantallas sueltas; con ella, salas de un mismo proyecto.
 */

export function CambiadorEspacios({
  activo,
  mundos,
  onIrCore,
  onIrMundo,
  onMas,
}: {
  /** el espacio actual: "core" o el dominio del mundo abierto */
  activo: string;
  /** los mundos ACTIVOS (con su nombre de cara), en orden de la fila */
  mundos: { dominio: string; nombre: string }[];
  onIrCore: () => void;
  onIrMundo: (dominio: string) => void;
  onMas: () => void;
}) {
  const base =
    "shrink-0 rounded-full px-3.5 py-1.5 text-[13px] font-semibold whitespace-nowrap transition-[background,color,border-color] duration-150";
  const claseTab = (activa: boolean) =>
    base +
    (activa
      ? " border border-accent bg-accent/15 text-accent"
      : " border border-hairline text-dim hover:text-ink");

  return (
    <div
      role="tablist"
      aria-label="Espacios de tu proyecto"
      className="mb-5 flex items-center gap-1.5 overflow-x-auto pb-1 [scrollbar-width:none] [&::-webkit-scrollbar]:hidden"
    >
      <button
        role="tab"
        aria-selected={activo === "core"}
        onClick={onIrCore}
        className={claseTab(activo === "core")}
      >
        Tu viaje
      </button>
      {mundos.map((m) => (
        <button
          key={m.dominio}
          role="tab"
          aria-selected={activo === m.dominio}
          onClick={() => onIrMundo(m.dominio)}
          className={claseTab(activo === m.dominio)}
        >
          {m.nombre}
        </button>
      ))}
      <button
        onClick={onMas}
        aria-label="Añadir un mundo"
        title="Añadir un mundo"
        className="shrink-0 rounded-full border border-hairline px-3 py-1.5 text-[13px] font-semibold text-dim transition-colors hover:text-ink"
      >
        +
      </button>
    </div>
  );
}
