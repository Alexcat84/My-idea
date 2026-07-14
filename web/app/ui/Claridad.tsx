"use client";

/**
 * Claridad — el organizador del API como el canon 03: chip "Esto entendí de
 * tu idea", la idea en una frase (título grande), y dos columnas — "Lo que
 * ya tienes" (puntos azules llenos) y "Lo que estás asumiendo" (rombos
 * azules) con su nota al pie. Azul piensa. El parser respeta el markdown
 * REAL del organizador; si no reconoce la estructura, cae al markdown plano.
 */
import { Markdown } from "./Markdown";

interface Claridad {
  frase: string | null;
  tienes: string[];
  asumes: string[];
}

function parsear(md: string): Claridad {
  let frase: string | null = null;
  const tienes: string[] = [];
  const asumes: string[] = [];
  let seccion: "tienes" | "asumes" | null = null;
  for (const linea of md.split("\n")) {
    const l = linea.trim();
    const mFrase = l.match(/^\*\*En una frase:?\*\*\s*(.+)$/i);
    if (mFrase) {
      frase = mFrase[1].trim();
      continue;
    }
    if (/^##\s+lo que ya tienes/i.test(l)) {
      seccion = "tienes";
      continue;
    }
    if (/^##\s+lo que est[áa]s asumiendo/i.test(l)) {
      seccion = "asumes";
      continue;
    }
    if (/^#{1,2}\s/.test(l)) {
      seccion = null;
      continue;
    }
    const item = l.match(/^[-*]\s+(.+)$/);
    if (item) {
      if (seccion === "tienes") tienes.push(item[1].trim());
      else if (seccion === "asumes") asumes.push(item[1].trim());
    }
  }
  return { frase, tienes, asumes };
}

function PuntoLleno() {
  return (
    <span
      aria-hidden
      className="mt-0.5 flex h-4 w-4 shrink-0 items-center justify-center rounded-full bg-black"
    >
      <span className="h-2 w-2 rounded-full bg-accent" />
    </span>
  );
}

function Rombo() {
  return (
    <span aria-hidden className="mt-0.5 flex h-4 w-4 shrink-0 items-center justify-center bg-black">
      <span className="h-2 w-2 rotate-45 border-[1.5px] border-accent" />
    </span>
  );
}

export function Claridad({ md }: { md: string }) {
  const { frase, tienes, asumes } = parsear(md);

  // Sin estructura reconocible: no rompemos: markdown plano.
  if (!frase && tienes.length === 0 && asumes.length === 0) {
    return (
      <section className="rounded-panel border border-hairline bg-surface p-5 sm:p-6">
        <Markdown>{md}</Markdown>
      </section>
    );
  }

  return (
    <section className="flex flex-col">
      <p className="anima-plan-in mb-4 flex items-center gap-2 text-[11px] font-semibold uppercase tracking-[1.2px] text-dim" style={{ animationDelay: "0.1s" }}>
        <span aria-hidden className="h-1.5 w-1.5 rounded-full bg-accent" />
        Esto entendí de tu idea
      </p>
      {frase && (
        <h2 className="anima-plan-in text-[22px] font-bold leading-[1.35] tracking-[-0.01em] [text-wrap:balance] sm:text-[30px]" style={{ animationDelay: "0.1s" }}>
          {frase}
        </h2>
      )}

      <div className="mt-8 grid grid-cols-1 gap-3.5 sm:grid-cols-2 sm:gap-5">
        {tienes.length > 0 && (
          <div className="anima-plan-in rounded-panel border border-hairline bg-surface p-6 sm:p-7" style={{ animationDelay: "0.35s" }}>
            <p className="mb-5 text-[11px] font-semibold uppercase tracking-[1.2px] text-dim">Lo que ya tienes</p>
            <ul className="flex flex-col gap-4">
              {tienes.map((t, i) => (
                <li key={i} className="flex items-start gap-3">
                  <PuntoLleno />
                  <span className="text-[14.5px] leading-[1.6] [text-wrap:pretty]">{t}</span>
                </li>
              ))}
            </ul>
          </div>
        )}
        {asumes.length > 0 && (
          <div
            className="anima-plan-in rounded-panel bg-surface p-6 sm:p-7"
            style={{ animationDelay: "0.5s", border: "1px solid rgba(77,124,254,0.3)" }}
          >
            <p className="mb-5 text-[11px] font-semibold uppercase tracking-[1.2px] text-accent">Lo que estás asumiendo</p>
            <ul className="flex flex-col gap-4">
              {asumes.map((a, i) => (
                <li key={i} className="flex items-start gap-3">
                  <Rombo />
                  <span className="text-[14.5px] leading-[1.6] [text-wrap:pretty]">{a}</span>
                </li>
              ))}
            </ul>
            <p className="mt-5 border-t border-hairline pt-[18px] text-[13px] leading-[1.6] text-dim [text-wrap:pretty]">
              Estas suposiciones son exactamente lo que La Exploración pone a prueba, pregunta a pregunta.
            </p>
          </div>
        )}
      </div>
    </section>
  );
}
