"use client";

/**
 * ReporteCard — la tarjeta "Reporte de números" bajo el plan (brief 2.6):
 * corre la mini-entrevista de tipo de oferta en tarjetas iguales a las de
 * la entrevista, y muestra el reporte final en acordeones. Los avisos del
 * guardián GIGO ya vienen del motor en palabras de persona.
 */
import { useState } from "react";
import { Acordeon } from "./Acordeon";
import { Markdown } from "./Markdown";
import { TarjetaPregunta } from "./TarjetaPregunta";
import { PRECIOS } from "@/lib/precios";

const ERROR_GENERICO = "algo se atoró de nuestro lado; intenta de nuevo en un momento";

interface Props {
  projectId: string;
  contenidoInicial: string | null;
  preguntaPendiente: string | null;
}

type Estado =
  | { fase: "cerrado" }
  | { fase: "preguntando"; pregunta: string }
  | { fase: "cargando" }
  | { fase: "listo"; contenido: string };

function parsearReporte(md: string): { secciones: Array<{ titulo: string; contenido: string }>; pie: string | null } {
  const secciones: Array<{ titulo: string; contenido: string }> = [];
  let pie: string | null = null;
  let actual: { titulo: string; contenido: string } | null = null;
  for (const linea of md.split("\n")) {
    const l = linea.trim();
    if (/^_Estimaciones basadas/.test(l)) {
      pie = l.replaceAll("_", "");
      continue;
    }
    const h2 = linea.match(/^##\s+(.+)$/);
    if (h2) {
      actual = { titulo: h2[1].trim(), contenido: "" };
      secciones.push(actual);
      continue;
    }
    if (actual) actual.contenido += linea + "\n";
  }
  for (const s of secciones) s.contenido = s.contenido.replace(/\n---\s*$/g, "\n").trim();
  return { secciones, pie };
}

export function ReporteCard({ projectId, contenidoInicial, preguntaPendiente }: Props) {
  const [estado, setEstado] = useState<Estado>(() =>
    contenidoInicial
      ? { fase: "listo", contenido: contenidoInicial }
      : preguntaPendiente
        ? { fase: "preguntando", pregunta: preguntaPendiente }
        : { fase: "cerrado" }
  );
  const [enviando, setEnviando] = useState(false);
  const [error, setError] = useState<string | null>(null);

  async function paso(respuesta?: string) {
    setEnviando(true);
    setError(null);
    try {
      const res = await fetch(`/api/project/${projectId}/report`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(respuesta === undefined ? {} : { respuesta }),
      });
      const data = await res.json();
      if (!res.ok) {
        setError(ERROR_GENERICO);
        return;
      }
      if (data.tipo === "pregunta") {
        setEstado({ fase: "preguntando", pregunta: String(data.pregunta) });
      } else {
        setEstado({ fase: "listo", contenido: String(data.contenido) });
      }
    } catch {
      setError("no pudimos conectar; revisa tu internet e intenta de nuevo");
    } finally {
      setEnviando(false);
    }
  }

  if (estado.fase === "listo") {
    const { secciones, pie } = parsearReporte(estado.contenido);
    return (
      <section className="flex flex-col gap-3">
        <h3 className="mt-2 text-base font-semibold">Tus Números</h3>
        {secciones.map((s, i) => (
          <Acordeon key={i} titulo={s.titulo} abierto={i === 0}>
            <Markdown>{s.contenido}</Markdown>
          </Acordeon>
        ))}
        {pie && <p className="text-xs text-dim">{pie}</p>}
        <button
          onClick={() => paso()}
          disabled={enviando}
          className="self-start text-sm text-dim hover:text-ink disabled:opacity-50"
        >
          {enviando ? "Actualizando…" : "Actualizar mis números"}
        </button>
        {error && <p className="text-sm text-warn">{error}</p>}
      </section>
    );
  }

  if (estado.fase === "preguntando") {
    return (
      <section className="flex flex-col gap-3">
        <h3 className="mt-2 text-base font-semibold">Tus Números</h3>
        <TarjetaPregunta
          cintillo="Tus números"
          pregunta={estado.pregunta}
          enviando={enviando}
          onEnviar={(r) => paso(r)}
        />
        {error && <p className="text-sm text-warn">{error}</p>}
      </section>
    );
  }

  // Canon 05/07: la tarjeta "Tus Números" bajo el plan, con su costo en
  // créditos desde precios.ts (jamás cifras hardcodeadas).
  return (
    <section className="rounded-panel border border-hairline bg-surface p-5 hover:border-accent/55" data-transiciona>
      <div className="flex items-center justify-between gap-3">
        <h3 className="text-base font-semibold">Tus Números</h3>
        <span className="inline-flex shrink-0 items-center rounded-full border border-accent/45 px-2.5 py-1 text-[11px] font-bold text-accent">
          {PRECIOS.tus_numeros} créditos
        </span>
      </div>
      <p className="mt-1.5 text-sm text-dim">
        Tus cifras reales convertidas en margen, punto de equilibrio y escenarios.
      </p>
      <button
        onClick={() => paso()}
        disabled={enviando}
        className="mt-4 rounded-cinta border border-hairline bg-surface-2 px-4 py-2.5 text-sm font-medium hover:bg-accent-soft disabled:opacity-50"
      >
        {enviando ? "Preparando…" : "Sacar mis números"}
      </button>
      {error && <p className="mt-3 text-sm text-warn">{error}</p>}
    </section>
  );
}
