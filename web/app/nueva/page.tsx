"use client";

/**
 * /nueva — el momento sagrado (brief 2.3) + organizador con árbol que
 * piensa (brief 2.4). Tres fases en una sola pantalla: captura →
 * generación (árbol alimentado SOLO por eventos reales del stream) →
 * resultado en acordeones con su CTA. Al terminar, la URL se reescribe a
 * /idea/<id> para que un refresh caiga en la vista persistida.
 */
import { useRouter } from "next/navigation";
import { useState } from "react";
import { ArbolPensante, type NodoArbol } from "../ui/ArbolPensante";
import { CampoConVoz } from "../ui/CampoConVoz";
import { consumirSSE } from "@/lib/sseCliente";
import type { OrganizadorData } from "@/lib/engine/organizador";

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

  async function enviar() {
    if (!texto.trim()) return;
    setEstado({ fase: "generando" });
    setNodos([]);
    try {
      const res = await fetch("/api/organizer/stream", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ texto }),
      });
      if (res.status === 429) {
        const data = await res.json();
        setEstado({ fase: "limite", mensaje: data.error });
        return;
      }
      if (!res.ok || !res.body) {
        setEstado({ fase: "captura", error: "algo se atoró de nuestro lado; intenta de nuevo en un momento" });
        return;
      }
      let projectId = "";
      let huboError = false;
      await consumirSSE(res, ({ evento, data }) => {
        if (evento === "inicio") {
          projectId = String((data as { project_id: string }).project_id);
        } else if (evento === "seccion") {
          const s = data as { clave: string; label: string };
          setEtiqueta(s.label);
          setNodos((prev) => [...prev, { id: s.clave, label: s.label }]);
        } else if (evento === "done") {
          const d = data as { project_id: string; data: OrganizadorData };
          window.history.replaceState(null, "", `/idea/${d.project_id}`);
          setEstado({ fase: "resultado", projectId: d.project_id, data: d.data });
        } else if (evento === "error") {
          huboError = true;
          setEstado({
            fase: "captura",
            error: String((data as { error?: string })?.error ?? "algo se atoró; intenta de nuevo"),
          });
        }
      });
      if (!projectId && !huboError) {
        setEstado({ fase: "captura", error: "la conexión se cortó a medio camino; intenta de nuevo" });
      }
    } catch {
      setEstado({ fase: "captura", error: "no pudimos conectar; revisa tu internet e intenta de nuevo" });
    }
  }

  if (estado.fase === "limite") {
    return (
      <main className="mx-auto flex w-full max-w-xl flex-1 flex-col items-center justify-center px-4 py-12 text-center">
        <p className="text-lg">{estado.mensaje}</p>
        <button
          onClick={() => router.push("/")}
          className="mt-8 rounded-cinta border border-hairline bg-surface px-5 py-3 text-dim hover:text-ink"
        >
          Ver planes
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
          <button
            onClick={() => router.push(`/idea/${estado.projectId}?entrevista=1`)}
            className="rounded-[10px] bg-accent px-[26px] py-3 text-sm font-semibold text-white hover:opacity-90"
          >
            Explorar estas suposiciones
          </button>
        </div>
        <p className="anima-plan-in mt-3.5 text-[13px] text-dim" style={{ animationDelay: "0.75s" }}>
          La Exploración usa 5 créditos. Tu Claridad es gratis y queda guardada para siempre.
        </p>
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
          className="rounded-[10px] bg-accent px-6 py-3 font-medium text-white hover:opacity-90 disabled:opacity-40"
        >
          Continuar
        </button>
      </div>
    </main>
  );
}
