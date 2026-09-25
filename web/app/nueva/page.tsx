"use client";

/**
 * /nueva — el momento sagrado (brief 2.3) + organizador con árbol que
 * piensa (brief 2.4). Tres fases en una sola pantalla: captura →
 * generación (árbol alimentado SOLO por eventos reales del stream) →
 * resultado en acordeones con su CTA. Al terminar, la URL se reescribe a
 * /idea/<id> para que un refresh caiga en la vista persistida.
 */
import { useRouter } from "next/navigation";
import { useEffect, useState } from "react";
import { ArbolPensante, type NodoArbol } from "../ui/ArbolPensante";
import { CampoConVoz } from "../ui/CampoConVoz";
import { BotonHeroe } from "../ui/BotonHeroe";
import { MAX_LARGO_IDEA, MENSAJE_IDEA_LARGA } from "@/lib/constants";
import { leerRechazo } from "@/lib/mensajeServidor";
import { consumirSSE, EsperaAgotadaError } from "@/lib/sseCliente";
import type { OrganizadorData } from "@/lib/engine/organizador";
import { AVISO_PRECIO_EXPLORACION } from "@/lib/avisoExploracion";
import { CODIGO_CIERRE_SIN_TERMINAL } from "@/lib/streamTerminal";

type Fase =
  | { fase: "captura"; error?: string }
  | { fase: "generando" }
  | { fase: "resultado"; projectId: string; data: OrganizadorData }
  | { fase: "limite"; mensaje: string };

export default function NuevaIdea() {
  const router = useRouter();
  const [texto, setTexto] = useState("");
  const [estado, setEstado] = useState<Fase>({ fase: "captura" });
  const [nodos, setNodos] = useState<NodoArbol[]>([]);
  const [etiqueta, setEtiqueta] = useState<string | undefined>();
  // AUD-09 M28: /nueva?idea=<id> ordena una idea que ya existe y quedó sin su
  // Claridad (el organizador falló). Se trae su texto y se reusa la misma idea.
  const [ideaAReordenar, setIdeaAReordenar] = useState<string | null>(null);
  useEffect(() => {
    const id = new URLSearchParams(window.location.search).get("idea");
    if (!id) return;
    fetch(`/api/idea/${id}`)
      .then((r) => (r.ok ? r.json() : null))
      .then((d: { idea?: { entrada_original?: string } } | null) => {
        if (!d?.idea?.entrada_original) return;
        setTexto(d.idea.entrada_original);
        setIdeaAReordenar(id);
      })
      .catch(() => {});
  }, []);

  async function enviar() {
    if (!texto.trim()) return;
    // AUD-09 H03: el límite se dice antes de enviar, con su número, y el texto
    // se queda en el campo para recortarlo.
    if (texto.length > MAX_LARGO_IDEA) {
      setEstado({ fase: "captura", error: MENSAJE_IDEA_LARGA });
      return;
    }
    setEstado({ fase: "generando" });
    setNodos([]);
    try {
      const res = await fetch("/api/organizer/stream", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(ideaAReordenar ? { texto, project_id: ideaAReordenar } : { texto }),
      });
      if (res.status === 429) {
        const data = await res.json();
        setEstado({ fase: "limite", mensaje: data.error });
        return;
      }
      if (!res.ok || !res.body) {
        // AUD-09 H03: el rechazo con razón (fusible, texto largo) se dice tal cual.
        setEstado({ fase: "captura", error: (await leerRechazo(res)).mensaje });
        return;
      }
      // AUD-09 H08: la espera termina SIEMPRE con salida. Lo que decide es si
      // llegó el evento final (done o error), no si llegó "inicio".
      let terminal = false;
      await consumirSSE(res, ({ evento, data }) => {
        if (evento === "seccion") {
          const s = data as { clave: string; label: string };
          setEtiqueta(s.label);
          setNodos((prev) => [...prev, { id: s.clave, label: s.label }]);
        } else if (evento === "done") {
          terminal = true;
          const d = data as { project_id: string; data: OrganizadorData };
          window.history.replaceState(null, "", `/idea/${d.project_id}`);
          setEstado({ fase: "resultado", projectId: d.project_id, data: d.data });
        } else if (evento === "error") {
          terminal = true;
          // AUD-09: un cierre mudo llega como código + identificador (la causa
          // interna se queda en el servidor): aquí se dice en palabras de persona.
          const d = data as { error?: string; codigo?: string; id?: string };
          setEstado({
            fase: "captura",
            error:
              d?.codigo === CODIGO_CIERRE_SIN_TERMINAL
                ? `La conexión se cortó antes de terminar. Tu texto sigue aquí; intenta de nuevo (referencia ${d.id ?? "sin id"}).`
                : String(d?.error ?? "algo se atoró; intenta de nuevo"),
          });
        }
      });
      if (!terminal) {
        setEstado({ fase: "captura", error: "la conexión se cortó a medio camino; tu texto sigue aquí, intenta de nuevo" });
      }
    } catch (e) {
      setEstado({
        fase: "captura",
        error:
          e instanceof EsperaAgotadaError
            ? "esto está tardando más de lo normal; tu texto sigue aquí, intenta de nuevo"
            : "no pudimos conectar; revisa tu internet e intenta de nuevo",
      });
    }
  }

  if (estado.fase === "limite") {
    return (
      <main className="mx-auto flex w-full max-w-xl flex-1 flex-col items-center justify-center px-4 py-12 text-center">
        <p className="text-lg">{estado.mensaje}</p>
        {/* AUD-09 B05: a la portada "a ver planes" no había nada que ver; las
            ideas guardadas sí te esperan. */}
        <button
          onClick={() => router.push("/ideas")}
          className="mt-8 rounded-cinta border border-hairline bg-surface px-5 py-3 text-dim hover:text-ink"
        >
          Ir a mis ideas
        </button>
      </main>
    );
  }

  if (estado.fase === "generando") {
    return (
      <main className="mx-auto flex w-full max-w-2xl flex-1 flex-col px-4 py-10 sm:px-6">
        <h1 className="mb-8 text-xl font-semibold">Organizando tu idea…</h1>
        <ArbolPensante nodos={nodos} generando etiquetaGenerando={etiqueta} />
      </main>
    );
  }

  if (estado.fase === "resultado") {
    const d = estado.data;
    return (
      // Canon 03 (docs/diseno-canon): frase héroe + dos tarjetas (la de
      // suposiciones con borde azul y rombos) + nota interna + CTA. Sin
      // acordeones, sin "Etapa detectada", sin "Áreas del plan" y sin
      // "Corregir algo" (estaba en el canon; removido por orden del
      // fundador — la Claridad no se regenera).
      <main className="mx-auto flex w-full max-w-[840px] flex-1 flex-col px-4 py-12 sm:px-6">
        <div className="anima-plan-in" style={{ animationDelay: "0.1s" }}>
          <div className="mb-4 flex items-center gap-2">
            <span aria-hidden className="h-1.5 w-1.5 rounded-full bg-accent" />
            <span className="text-[11px] font-semibold uppercase tracking-[1.2px] text-dim">
              Esto entendí de tu idea
            </span>
          </div>
          <h1 className="text-[26px] font-bold leading-[1.35] tracking-[-0.02em] [text-wrap:balance] sm:text-[30px]">
            {d.idea_en_una_frase}
          </h1>
        </div>

        <div className="mt-10 grid gap-5 sm:grid-cols-2">
          <section
            className="anima-plan-in rounded-panel border border-hairline bg-surface p-7"
            style={{ animationDelay: "0.35s" }}
          >
            <p className="mb-5 text-[11px] font-semibold uppercase tracking-[1.2px] text-dim">
              Lo que ya tienes
            </p>
            <ul className="flex flex-col gap-4">
              {(d.lo_que_ya_tienes_claro ?? []).map((b, i) => (
                <li key={i} className="flex items-start gap-3">
                  <span
                    aria-hidden
                    className="mt-0.5 flex h-4 w-4 shrink-0 items-center justify-center rounded-full bg-black"
                  >
                    <span className="h-[9px] w-[9px] rounded-full bg-accent" />
                  </span>
                  <span className="text-[14.5px] leading-[1.6]">{b}</span>
                </li>
              ))}
            </ul>
          </section>

          <section
            className="anima-plan-in rounded-panel bg-surface p-7"
            style={{ animationDelay: "0.5s", border: "1px solid rgba(77,124,254,0.3)" }}
          >
            <p className="mb-5 text-[11px] font-semibold uppercase tracking-[1.2px] text-accent">
              Lo que estás asumiendo
            </p>
            <ul className="flex flex-col gap-4">
              {(d.lo_que_estas_asumiendo_sin_saberlo ?? []).map((b, i) => (
                <li key={i} className="flex items-start gap-3">
                  <span
                    aria-hidden
                    className="mt-0.5 flex h-4 w-4 shrink-0 items-center justify-center bg-black"
                  >
                    <span className="box-border h-2 w-2 rotate-45 border-[1.5px] border-accent" />
                  </span>
                  <span className="text-[14.5px] leading-[1.6]">{b}</span>
                </li>
              ))}
            </ul>
            <p className="mt-5 border-t border-hairline pt-[18px] text-[13px] leading-[1.6] text-dim [text-wrap:pretty]">
              Estas suposiciones son exactamente lo que La Exploración pone a prueba, pregunta a
              pregunta.
            </p>
          </section>
        </div>

        <div className="anima-plan-in mt-9" style={{ animationDelay: "0.65s" }}>
          <BotonHeroe
            onClick={() => router.push(`/idea/${estado.projectId}?entrevista=1`)}
            className="rounded-[10px] px-[26px] py-3 text-sm font-semibold"
          >
            Explorar estas suposiciones
          </BotonHeroe>
          {/* AUD-09 M32: el aviso de precio del canon 03, antes de empezar. */}
          <p className="mt-3 text-[12.5px] leading-[1.6] text-dim [text-wrap:pretty]">{AVISO_PRECIO_EXPLORACION}</p>
        </div>
      </main>
    );
  }

  return (
    <main className="mx-auto flex w-full max-w-2xl flex-1 flex-col justify-center px-4 py-10 sm:px-6">
      {/* Canon 02 (La Chispa): el momento sagrado — un campo grande y nada más */}
      <p className="mb-2 text-[11px] font-semibold uppercase tracking-[1.2px] text-accent">
        Nueva idea · La Chispa
      </p>
      <label htmlFor="idea" className="mb-2 block text-2xl font-bold leading-snug tracking-tight">
        Cuéntame tu idea
      </label>
      <p className="mb-4 text-[15px] text-dim">
        Escríbela o díctala tal como la tienes en mente. Ese es todo el requisito.
      </p>
      <CampoConVoz
        id="idea"
        valor={texto}
        onCambio={setTexto}
        filas={7}
        autoFocus
        placeholder="Quiero vender café de especialidad a domicilio en mi barrio…"
      />
      {estado.error && (
        <div className="mt-3 flex flex-wrap items-center gap-x-4 gap-y-2">
          <p className="text-sm text-warn">{estado.error}</p>
          {/* tu texto sigue en el campo: reintentar es un clic, sin re-teclear */}
          <button
            onClick={enviar}
            disabled={!texto.trim()}
            className="rounded-[8px] border border-accent/50 px-3.5 py-1.5 text-[13px] font-semibold text-accent hover:bg-accent/10 disabled:opacity-40"
          >
            Intentar de nuevo
          </button>
        </div>
      )}
      <div className="mt-5 flex items-center justify-between gap-4">
        <p className="text-xs text-dim">Sin plantillas ni formularios. Solo tu idea, en tus palabras.</p>
        <button
          onClick={enviar}
          disabled={!texto.trim()}
          className="rounded-[10px] border border-accent/40 bg-accent/10 px-6 py-3 font-medium text-accent hover:bg-accent/20 disabled:opacity-40"
        >
          Continuar
        </button>
      </div>
    </main>
  );
}
