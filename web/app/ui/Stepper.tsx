/**
 * Stepper — el viaje de 5 etapas canónicas (REGLAS_Y_TOKENS.md §2):
 * La Chispa → Claridad → La Exploración → Tu Plan → Manos a la Obra.
 * Regla de color: EL AZUL PIENSA (etapas 1-4), EL VERDE EJECUTA (etapa 5).
 * REGLA DE ORO intacta: este componente solo pinta el estado que recibe;
 * la etapa se deriva de la verdad persistida del motor, nunca de teatro.
 *
 * Los estados completados se distinguen también por FORMA (punto lleno
 * vs hueco), nunca solo por color.
 */

export const ETAPAS_CANON = [
  "La Chispa",
  "Claridad",
  "La Exploración",
  "Tu Plan",
  "Manos a la Obra",
] as const;

export interface EstadoStepper {
  /** 1-5: etapa alcanzada según la verdad del motor */
  etapa: number;
  /** el motor está trabajando la etapa actual: anillo girando */
  pensando?: boolean;
  /** texto junto al punto actual ("Tu Plan · listo", "Manos a la Obra · 4/12") */
  etiqueta?: string;
}

function Punto({ estado, titulo, tamano }: { estado: "hecha" | "actual" | "pensando" | "verde" | "futura"; titulo: string; tamano: number }) {
  const px = `${tamano}px`;
  if (estado === "pensando") {
    return (
      <span title={titulo} className="relative shrink-0" style={{ width: px, height: px }}>
        <span
          className="anima-spin-ring absolute -inset-0.5 box-border rounded-full border-2"
          style={{ borderColor: "rgba(77,124,254,0.2)", borderTopColor: "var(--accent)" }}
        />
      </span>
    );
  }
  const base = "shrink-0 rounded-full";
  if (estado === "hecha") {
    return <span title={titulo} className={base + " bg-accent"} style={{ width: px, height: px }} />;
  }
  if (estado === "actual") {
    return <span title={titulo} className={base + " anima-idea-pulse bg-accent"} style={{ width: px, height: px }} />;
  }
  if (estado === "verde") {
    return <span title={titulo} className={base + " anima-green-pulse bg-done"} style={{ width: px, height: px }} />;
  }
  return (
    <span
      title={titulo}
      className={base + " box-border border-[1.5px] border-dim"}
      style={{ width: px, height: px }}
    />
  );
}

function Guion({ ancho }: { ancho: number }) {
  return (
    <span
      aria-hidden
      className="shrink-0 border-t-2 border-dashed"
      style={{ width: `${ancho}px`, borderColor: "rgba(255,255,255,0.18)" }}
    />
  );
}

/** Variante de header (58px): puntos de 12px, etiqueta junto al actual. */
export function Stepper({ etapa, pensando, etiqueta }: EstadoStepper) {
  return (
    <div aria-label={`Etapa ${etapa} de 5: ${ETAPAS_CANON[etapa - 1]}`} className="flex items-center gap-2.5">
      {ETAPAS_CANON.map((titulo, i) => {
        const n = i + 1;
        const esVerde = n === 5;
        let estado: "hecha" | "actual" | "pensando" | "verde" | "futura";
        if (n < etapa) estado = "hecha";
        else if (n === etapa) estado = pensando ? "pensando" : esVerde ? "verde" : "actual";
        else estado = "futura";
        const mostrarEtiqueta = n === etapa && etiqueta;
        return (
          <span key={titulo} className="flex items-center gap-2.5">
            {i > 0 && <Guion ancho={30} />}
            {mostrarEtiqueta ? (
              <span className="flex items-center gap-2">
                <Punto estado={estado} titulo={titulo} tamano={12} />
                <span
                  className={
                    "whitespace-nowrap text-[12.5px] font-semibold " + (esVerde ? "text-done" : "text-accent")
                  }
                >
                  {etiqueta}
                </span>
              </span>
            ) : (
              <Punto estado={estado} titulo={titulo} tamano={12} />
            )}
          </span>
        );
      })}
    </div>
  );
}

/** Variante mini para las cintas del home: puntos de 9px, sin etiqueta. */
export function StepperMini({ etapa, pensando }: EstadoStepper) {
  return (
    <div aria-label={`Etapa ${etapa} de 5: ${ETAPAS_CANON[etapa - 1]}`} className="flex items-center gap-2">
      {ETAPAS_CANON.map((titulo, i) => {
        const n = i + 1;
        let estado: "hecha" | "actual" | "pensando" | "verde" | "futura";
        if (n < etapa) estado = "hecha";
        else if (n === etapa) estado = pensando ? "pensando" : n === 5 ? "verde" : "actual";
        else estado = "futura";
        return (
          <span key={titulo} className="flex items-center gap-2">
            {i > 0 && <Guion ancho={14} />}
            <Punto estado={estado} titulo={titulo} tamano={9} />
          </span>
        );
      })}
    </div>
  );
}
