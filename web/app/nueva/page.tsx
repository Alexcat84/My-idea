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
import { Acordeon } from "../ui/Acordeon";
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
      <main className="mx-auto flex w-full max-w-2xl flex-1 flex-col gap-3 px-4 py-10 sm:px-6">
        {/* Canon 03 (Claridad): chip de estado + "Esto entendí de tu idea" */}
        <p className="text-[11px] font-semibold uppercase tracking-[1.2px] text-dim">Claridad · lista</p>
        <h1 className="mb-3 text-xl font-semibold">Esto entendí de tu idea</h1>
        <Acordeon titulo="Tu idea en una frase" abierto>
          <p>{d.idea_en_una_frase}</p>
          {d.etapa_detectada && (
            <p className="mt-2 text-sm text-dim">Etapa detectada: {d.etapa_detectada}</p>
          )}
        </Acordeon>
        <Acordeon titulo="Lo que ya tienes" abierto>
          <ul className="list-disc space-y-1.5 pl-5">
            {(d.lo_que_ya_tienes_claro ?? []).map((b, i) => (
              <li key={i}>{b}</li>
            ))}
          </ul>
        </Acordeon>
        <Acordeon titulo="Lo que estás asumiendo" abierto>
          <ul className="list-disc space-y-1.5 pl-5">
            {(d.lo_que_estas_asumiendo_sin_saberlo ?? []).map((b, i) => (
              <li key={i}>{b}</li>
            ))}
          </ul>
        </Acordeon>
        <Acordeon titulo="Áreas que cubriría tu plan completo">
          <ul className="list-disc space-y-1.5 pl-5">
            {(d.areas_que_cubriria_tu_plan_completo ?? []).map((b, i) => (
              <li key={i}>{b}</li>
            ))}
          </ul>
        </Acordeon>
        <p className="mt-2 text-sm text-dim">
          Estas suposiciones son exactamente lo que La Exploración pone a prueba, pregunta a pregunta.
        </p>
        <div className="mt-3 flex flex-wrap items-center gap-3">
          <button
            onClick={() => router.push(`/idea/${estado.projectId}?entrevista=1`)}
            className="rounded-[10px] bg-accent px-6 py-3 font-medium text-white hover:opacity-90"
          >
            Explorar estas suposiciones
          </button>
          <button
            onClick={() => {
              setEstado({ fase: "captura" });
            }}
            className="rounded-[10px] border border-white/15 px-5 py-3 text-[13.5px] text-dim hover:border-accent/60 hover:text-ink"
          >
            Corregir algo
          </button>
        </div>
        <p className="mt-2 text-xs text-dim">
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
      {estado.error && <p className="mt-3 text-sm text-warn">{estado.error}</p>}
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
