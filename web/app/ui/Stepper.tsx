/**
 * Stepper — el viaje como una LÍNEA CONTINUA con los puntos al ras (no puntos
 * sueltos con huecos entre la línea y el círculo, el reclamo histórico): un
 * riel de fondo, el tramo recorrido relleno encima, y los puntos sentados
 * SOBRE la línea, cubriéndola donde están.
 *
 * Seis hitos: La Chispa → Claridad → La Exploración → Tu Plan → Manos a la Obra
 * → Realizado. El último ("Realizado") es la CELEBRACIÓN: el verde de
 * "terminado" solo llega ahí. Mientras el usuario trabaja en Manos a la Obra,
 * el nodo Realizado queda GRIS: el viaje aún no terminó (decisión del fundador).
 *
 * REGLA DE ORO intacta: solo pinta el estado que recibe; la etapa sale de la
 * verdad del motor, nunca de teatro. Los estados se distinguen por FORMA (lleno
 * / hueco / anillo), no solo por color. EL AZUL PIENSA (1-4), EL VERDE EJECUTA
 * (Manos a la Obra) Y CELEBRA (Realizado).
 */

export const ETAPAS_CANON = [
  "La Chispa",
  "Claridad",
  "La Exploración",
  "Tu Plan",
  "Manos a la Obra",
  "Realizado",
] as const;

const N = ETAPAS_CANON.length;

export interface EstadoStepper {
  /** 1-5: etapa alcanzada según la verdad del motor (Realizado es el 6.º). */
  etapa: number;
  /** el motor está trabajando la etapa actual: anillo girando */
  pensando?: boolean;
  /** texto junto al riel ("Tu Plan · listo", "Manos a la Obra · 4/12") */
  etiqueta?: string;
  /** la idea se marcó realizada: solo entonces se enciende "Realizado" (verde). */
  realizada?: boolean;
}

type EstadoNodo = "hecha" | "actual" | "pensando" | "hechoVerde" | "futura";

function estadoNodo(i: number, etapa: number, pensando: boolean, realizada: boolean): EstadoNodo {
  const n = i + 1;
  // Realizado (último): VERDE solo en la celebración; gris mientras tanto. El
  // verde de "terminado" NO aparece en ninguna otra etapa (regla del fundador).
  if (n === N) return realizada ? "hechoVerde" : "futura";
  if (n < etapa) return "hecha";
  if (n === etapa) {
    if (realizada) return "hechoVerde";
    if (pensando) return "pensando";
    // El punto EN CAMINO (etapa actual, cualquiera): azul con HALO pulsante —
    // la punta viva del recorrido. Antes Manos a la Obra era verde y parecía
    // terminado; ahora el verde se guarda para Realizado.
    return "actual";
  }
  return "futura";
}

/** Un punto SOBRE la línea. Los estados rellenos cubren el riel; el hueco y el
 * anillo llevan el color de fondo para tapar la línea (así se ve "sentado"). */
function Punto({ estado, tam, fondo, titulo }: { estado: EstadoNodo; tam: number; fondo: string; titulo: string }) {
  const s = { width: `${tam}px`, height: `${tam}px` } as const;
  if (estado === "pensando") {
    return (
      <span title={titulo} className="relative shrink-0 rounded-full" style={{ ...s, background: fondo }}>
        <span
          className="anima-spin-ring absolute -inset-[3px] box-border rounded-full border-2"
          style={{ borderColor: "rgba(77,124,254,0.2)", borderTopColor: "var(--accent)" }}
        />
      </span>
    );
  }
  const base = "relative shrink-0 rounded-full";
  if (estado === "hecha") return <span title={titulo} className={base + " bg-accent"} style={s} />;
  // actual: la punta viva del recorrido — azul, con un ANILLO estático (para que
  // "dónde vas" se distinga siempre, no solo por la animación) y el halo pulsante.
  if (estado === "actual")
    return (
      <span title={titulo} className="relative shrink-0" style={s}>
        <span className="anima-idea-pulse absolute inset-0 rounded-full bg-accent" />
        <span className="absolute rounded-full border-2 border-accent/40" style={{ inset: "-4px" }} />
      </span>
    );
  // hechoVerde: verde sólido — SOLO Realizado (la celebración).
  if (estado === "hechoVerde") return <span title={titulo} className={base + " bg-done"} style={s} />;
  // futura: hueco relleno del color de fondo (tapa la línea) con borde tenue.
  return (
    <span
      title={titulo}
      className={base + " box-border border-[1.5px] border-white/25"}
      style={{ ...s, background: fondo }}
    />
  );
}

/** El riel: línea de fondo + tramo recorrido + puntos al ras, repartidos. */
function Riel({
  etapa,
  pensando,
  realizada,
  tam,
  ancho,
  fondo,
}: {
  etapa: number;
  pensando: boolean;
  realizada: boolean;
  tam: number;
  ancho: number;
  fondo: string;
}) {
  const alcanzado = realizada ? N : Math.min(Math.max(etapa, 1), N);
  const frac = (alcanzado - 1) / (N - 1);
  return (
    <div className="relative flex shrink-0 items-center" style={{ width: `${ancho}px` }}>
      {/* riel de fondo, del centro del primer punto al del último */}
      <div
        className="absolute top-1/2 h-[2px] -translate-y-1/2 rounded-full bg-white/15"
        style={{ left: `${tam / 2}px`, right: `${tam / 2}px` }}
      />
      {/* tramo recorrido: azul mientras piensa/ejecuta, verde al realizar */}
      <div
        className="absolute top-1/2 h-[2px] -translate-y-1/2 rounded-full transition-[width]"
        style={{ left: `${tam / 2}px`, width: `calc((100% - ${tam}px) * ${frac})`, background: realizada ? "var(--done)" : "var(--accent)" }}
      />
      {/* puntos, al ras sobre la línea */}
      <div className="relative flex w-full items-center justify-between">
        {ETAPAS_CANON.map((titulo, i) => (
          <Punto key={titulo} estado={estadoNodo(i, etapa, pensando, realizada)} tam={tam} fondo={fondo} titulo={titulo} />
        ))}
      </div>
    </div>
  );
}

/** Variante de header (58px): riel + etiqueta del hito actual al lado. */
export function Stepper({ etapa, pensando, etiqueta, realizada }: EstadoStepper) {
  // La etiqueta sigue el color de su punto (azul mientras se avanza), con la
  // excepción documentada por Design: "Manos a la Obra · N/M" (etapa 5) se
  // mantiene en VERDE porque nombra la ejecución EN CURSO, no el final del
  // viaje — aunque su punto ya sea la punta viva azul. Y verde también al
  // realizar (la celebración).
  const enVerde = Boolean(realizada) || etapa === 5;
  return (
    <div aria-label={`Etapa ${etapa} de ${N}: ${ETAPAS_CANON[Math.min(etapa, N) - 1]}`} className="flex items-center gap-3">
      <Riel etapa={etapa} pensando={Boolean(pensando)} realizada={Boolean(realizada)} tam={11} ancho={150} fondo="var(--bg)" />
      {etiqueta && (
        <span className={"whitespace-nowrap text-[12.5px] font-semibold " + (enVerde ? "text-done" : "text-accent")}>
          {etiqueta}
        </span>
      )}
    </div>
  );
}

/** Variante mini para las cintas del home: riel más corto, sin etiqueta. El
 * fondo de los huecos es el de la cinta (surface), no el del lienzo. */
export function StepperMini({ etapa, pensando, realizada }: EstadoStepper) {
  return (
    <div aria-label={`Etapa ${etapa} de ${N}: ${ETAPAS_CANON[Math.min(etapa, N) - 1]}`}>
      <Riel etapa={etapa} pensando={Boolean(pensando)} realizada={Boolean(realizada)} tam={9} ancho={116} fondo="var(--surface)" />
    </div>
  );
}
