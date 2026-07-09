"use client";

/**
 * IdeaView — la vista de idea (brief 2.4/2.5/2.6): layout de riel
 * (árbol punteado) + panel de contenido. El árbol SOLO se alimenta de
 * eventos reales: nodos de la ruta que devuelve /turn, etapas del SSE
 * del plan. La entrevista es una tarjeta a la vez; el "recorrido" es un
 * acordeón para releer, no un chat.
 */
import Link from "next/link";
import { useSearchParams } from "next/navigation";
import { useCallback, useEffect, useRef, useState } from "react";
import { Acordeon } from "../../ui/Acordeon";
import { ArbolPensante, type NodoArbol } from "../../ui/ArbolPensante";
import { Markdown } from "../../ui/Markdown";
import { MundosAddOn } from "../../ui/MundosAddOn";
import { PlanDocumento } from "../../ui/PlanDocumento";
import { ReporteCard } from "../../ui/ReporteCard";
import { TarjetaPregunta } from "../../ui/TarjetaPregunta";
import { consumirSSE } from "@/lib/sseCliente";

const NOTA_SILENCIOSO = "cubierto por lo que contaste";
const ERROR_GENERICO = "algo se atoró de nuestro lado; intenta de nuevo en un momento";

interface DetalleIdea {
  idea: { id: string; nombre: string; entrada_original: string };
  organizador: { contenido_md: string } | null;
  plan: { etiqueta: string; contenido_md: string; created_at: string } | null;
  reporte: { contenido_md: string; created_at: string } | null;
  reporte_en_curso: { pregunta: string } | null;
  entrevista: {
    session_id: string;
    pregunta: string | null;
    listo_para_plan: boolean;
    ruta: Array<{ id: string; titulo: string; modo: string }>;
  } | null;
}

interface NodoNuevo {
  id: string;
  titulo: string;
  modo: string;
}

interface RespuestaTurno {
  session_id: string;
  tipo: "pregunta" | "listo_para_plan" | "salio" | "error_temporal";
  pregunta?: string;
  nodos_nuevos?: NodoNuevo[];
  error?: string;
}

interface QA {
  pregunta: string;
  respuesta: string;
}

function nodoArbolDesdeRuta(n: { id: string; titulo: string; modo: string }, idx: number): NodoArbol {
  return {
    id: `${idx}-${n.id}`,
    label: n.titulo,
    atenuado: n.modo === "silencioso",
    salto: n.modo === "salto",
    nota: n.modo === "silencioso" ? NOTA_SILENCIOSO : undefined,
  };
}

export function IdeaView({ projectId }: { projectId: string }) {
  const searchParams = useSearchParams();
  const quiereEntrevista = searchParams.get("entrevista") === "1";

  const [detalle, setDetalle] = useState<DetalleIdea | null>(null);
  const [cargando, setCargando] = useState(true);
  const [error, setError] = useState<string | null>(null);

  // --- entrevista ---
  const [sessionId, setSessionId] = useState<string | null>(null);
  const [pregunta, setPregunta] = useState<string | null>(null);
  const [cintillo, setCintillo] = useState<string | null>(null);
  const [enviando, setEnviando] = useState(false);
  const [listoParaPlan, setListoParaPlan] = useState(false);
  const [recorrido, setRecorrido] = useState<QA[]>([]);
  const [nodos, setNodos] = useState<NodoArbol[]>([]);
  const contadorNodos = useRef(0);

  // --- plan ---
  const [generandoPlan, setGenerandoPlan] = useState(false);
  const [etiquetaEtapa, setEtiquetaEtapa] = useState<string | undefined>();
  const [planMd, setPlanMd] = useState<string | null>(null);
  const arrancoRef = useRef(false);

  function agregarNodos(nuevos: NodoNuevo[] | undefined) {
    if (!nuevos?.length) return;
    setNodos((prev) => [
      ...prev,
      ...nuevos.map((n) => nodoArbolDesdeRuta(n, contadorNodos.current++)),
    ]);
    const conversado = [...nuevos].reverse().find((n) => n.modo !== "silencioso");
    if (conversado) setCintillo(conversado.titulo);
  }

  function procesarTurno(data: RespuestaTurno) {
    setSessionId(data.session_id);
    agregarNodos(data.nodos_nuevos);
    if (data.tipo === "pregunta" && data.pregunta) {
      setPregunta(data.pregunta);
    } else if (data.tipo === "listo_para_plan") {
      setPregunta(null);
      setListoParaPlan(true);
    } else if (data.tipo === "salio") {
      setPregunta(null);
    }
  }

  const generarPlan = useCallback(
    async (sid: string) => {
      if (generandoPlan) return;
      setGenerandoPlan(true);
      setPregunta(null);
      setError(null);
      try {
        const res = await fetch(`/api/session/${sid}/plan`, { method: "POST" });
        if (!res.ok || !res.body) {
          setError(ERROR_GENERICO);
          setGenerandoPlan(false);
          return;
        }
        // Árbol de etapas: cada encabezado "## " que llega por el stream
        // REAL enciende un punto (regla de oro: cero teatro).
        let crudo = "";
        const etapasVistas = new Set<string>();
        await consumirSSE(res, ({ evento, data }) => {
          if (evento === "delta") {
            crudo += String((data as { texto: string }).texto);
            for (const m of crudo.matchAll(/^##\s+(.+)$/gm)) {
              const titulo = m[1].trim();
              if (etapasVistas.has(titulo)) continue;
              // solo cerrado por salto de línea posterior: encabezado completo
              const fin = (m.index ?? 0) + m[0].length;
              if (fin >= crudo.length) continue;
              etapasVistas.add(titulo);
              setEtiquetaEtapa(titulo);
              setNodos((prev) => [...prev, { id: `etapa-${prev.length}`, label: titulo }]);
            }
          } else if (evento === "done") {
            const d = data as { markdown: string };
            setPlanMd(d.markdown);
          } else if (evento === "error") {
            setError(ERROR_GENERICO);
          }
        });
      } catch {
        setError("la conexión se cortó mientras armábamos tu plan; tu recorrido quedó guardado, intenta de nuevo");
      } finally {
        setGenerandoPlan(false);
        setEtiquetaEtapa(undefined);
      }
    },
    [generandoPlan]
  );

  // Carga inicial + arranque de entrevista si venimos del organizador.
  useEffect(() => {
    if (arrancoRef.current) return;
    arrancoRef.current = true;
    (async () => {
      try {
        const res = await fetch(`/api/idea/${projectId}`);
        if (!res.ok) {
          setError(res.status === 404 ? "esa idea no existe o no es tuya" : ERROR_GENERICO);
          setCargando(false);
          return;
        }
        const d = (await res.json()) as DetalleIdea;
        setDetalle(d);
        if (d.plan) setPlanMd(d.plan.contenido_md);
        if (d.entrevista) {
          setSessionId(d.entrevista.session_id);
          setPregunta(d.entrevista.pregunta);
          setListoParaPlan(d.entrevista.listo_para_plan);
          setNodos(d.entrevista.ruta.map(nodoArbolDesdeRuta));
          contadorNodos.current = d.entrevista.ruta.length;
          const conversado = [...d.entrevista.ruta].reverse().find((n) => n.modo !== "silencioso");
          if (conversado) setCintillo(conversado.titulo);
        } else if (quiereEntrevista && !d.plan) {
          // Arranque: la entrevista sobre ESTA idea (el motor nunca
          // re-pregunta la idea inicial: se la mandamos como contexto).
          setEnviando(true);
          const inicio = await fetch("/api/session/start", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ texto: d.idea.entrada_original, project_id: projectId }),
          });
          if (inicio.status === 429) {
            setError(((await inicio.json()) as { error: string }).error);
          } else if (!inicio.ok) {
            setError(ERROR_GENERICO);
          } else {
            procesarTurno((await inicio.json()) as RespuestaTurno);
          }
          setEnviando(false);
        }
      } catch {
        setError("no pudimos cargar tu idea; revisa tu internet e intenta de nuevo");
      } finally {
        setCargando(false);
      }
    })();
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [projectId]);

  async function responder(respuesta: string) {
    if (!sessionId || !pregunta) return;
    setEnviando(true);
    setError(null);
    const preguntaActual = pregunta;
    try {
      const res = await fetch(`/api/session/${sessionId}/turn`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ respuesta }),
      });
      if (!res.ok) {
        setError(ERROR_GENERICO);
        return;
      }
      setRecorrido((prev) => [...prev, { pregunta: preguntaActual, respuesta }]);
      procesarTurno((await res.json()) as RespuestaTurno);
    } catch {
      setError("no pudimos enviar tu respuesta; revisa tu internet e intenta de nuevo");
    } finally {
      setEnviando(false);
    }
  }

  if (cargando) {
    return <p className="px-6 py-12 text-dim">Cargando tu idea…</p>;
  }
  if (!detalle) {
    return (
      <div className="px-6 py-12">
        <p className="text-warn">{error ?? ERROR_GENERICO}</p>
        <Link href="/" className="mt-4 inline-block text-accent">
          Volver a mis ideas
        </Link>
      </div>
    );
  }

  const entrevistaActiva = Boolean(pregunta) || enviando || listoParaPlan;
  const mostrarArbol = nodos.length > 0 && (entrevistaActiva || generandoPlan);
  const puedeGenerarPlan = Boolean(sessionId) && !generandoPlan && !planMd;

  const arbol = (
    <ArbolPensante
      nodos={nodos}
      generando={enviando || generandoPlan}
      etiquetaGenerando={generandoPlan ? etiquetaEtapa : cintillo ?? undefined}
    />
  );

  return (
    <main className="mx-auto w-full max-w-4xl flex-1 px-4 py-8 sm:px-6">
      <header className="mb-6 flex items-start justify-between gap-4">
        <div>
          <Link href="/" className="text-sm text-dim hover:text-ink">
            ← Mis ideas
          </Link>
          <h1 className="mt-1 text-xl font-semibold leading-snug">{detalle.idea.nombre}</h1>
        </div>
        {puedeGenerarPlan && (
          <button
            onClick={() => sessionId && generarPlan(sessionId)}
            className="shrink-0 rounded-cinta border border-hairline bg-surface px-4 py-2 text-sm font-medium hover:bg-surface-2"
          >
            Generar mi plan
          </button>
        )}
      </header>

      {error && <p className="mb-4 text-sm text-warn">{error}</p>}

      <div className="flex flex-col gap-6 sm:grid sm:grid-cols-[190px_1fr] sm:gap-8">
        {/* Riel izquierdo: el árbol (en móvil, acordeón arriba) */}
        {mostrarArbol && (
          <>
            <div className="hidden sm:block">{arbol}</div>
            <div className="sm:hidden">
              <Acordeon titulo="Recorrido del grafo" abierto={generandoPlan}>
                {arbol}
              </Acordeon>
            </div>
          </>
        )}

        <div className={"flex min-w-0 flex-col gap-4" + (mostrarArbol ? "" : " sm:col-span-2")}>
          {/* Tarjeta de pregunta (una a la vez) */}
          {pregunta && (
            <TarjetaPregunta cintillo={cintillo} pregunta={pregunta} enviando={enviando} onEnviar={responder} />
          )}
          {!pregunta && enviando && (
            <p className="text-sm text-dim">Pensando la siguiente pregunta…</p>
          )}

          {/* Acciones claras, no texto en conversación */}
          {listoParaPlan && !generandoPlan && !planMd && (
            <div className="rounded-panel border border-hairline bg-surface p-5">
              <p className="font-medium">Con lo que contaste ya alcanza para tu plan.</p>
              <button
                onClick={() => sessionId && generarPlan(sessionId)}
                className="mt-4 rounded-cinta bg-accent px-5 py-3 font-medium text-white hover:opacity-90"
              >
                Generar mi plan
              </button>
            </div>
          )}

          {generandoPlan && (
            <p className="text-sm text-dim">Armando tu plan por etapas — mira el recorrido crecer.</p>
          )}

          {/* Recorrido releíble (no chat) */}
          {recorrido.length > 0 && (
            <Acordeon titulo={`Recorrido (${recorrido.length})`}>
              <ol className="space-y-4">
                {recorrido.map((qa, i) => (
                  <li key={i} className="border-b border-hairline pb-3 last:border-0 last:pb-0">
                    <p className="text-sm text-dim">{qa.pregunta}</p>
                    <p className="mt-1">{qa.respuesta}</p>
                  </li>
                ))}
              </ol>
            </Acordeon>
          )}

          {/* Plan como documento acordeón (brief 2.6) */}
          {planMd && <PlanDocumento md={planMd} nombreIdea={detalle.idea.nombre} />}

          {/* Bajo el plan: la tarjeta "Reporte de números" */}
          {planMd && !generandoPlan && (
            <ReporteCard
              projectId={projectId}
              contenidoInicial={detalle.reporte?.contenido_md ?? null}
              preguntaPendiente={detalle.reporte_en_curso?.pregunta ?? null}
            />
          )}

          {/* Mundos HSEQ con candado (fachada de beta, brief sección 4) */}
          {!entrevistaActiva && !generandoPlan && (planMd || detalle.organizador) && (
            <MundosAddOn projectId={projectId} />
          )}

          {/* Organizador persistido (cuando no hay nada más activo) */}
          {!entrevistaActiva && !planMd && !generandoPlan && detalle.organizador && (
            <>
              <section className="rounded-panel border border-hairline bg-surface p-5 sm:p-6">
                <Markdown>{detalle.organizador.contenido_md}</Markdown>
              </section>
              <button
                onClick={async () => {
                  setEnviando(true);
                  setError(null);
                  try {
                    const inicio = await fetch("/api/session/start", {
                      method: "POST",
                      headers: { "Content-Type": "application/json" },
                      body: JSON.stringify({ texto: detalle.idea.entrada_original, project_id: projectId }),
                    });
                    if (inicio.status === 429) {
                      setError(((await inicio.json()) as { error: string }).error);
                    } else if (!inicio.ok) {
                      setError(ERROR_GENERICO);
                    } else {
                      procesarTurno((await inicio.json()) as RespuestaTurno);
                    }
                  } catch {
                    setError("no pudimos conectar; revisa tu internet e intenta de nuevo");
                  } finally {
                    setEnviando(false);
                  }
                }}
                className="self-start rounded-cinta bg-accent px-5 py-3 font-medium text-white hover:opacity-90"
              >
                Continuar el desarrollo de mi idea
              </button>
            </>
          )}
        </div>
      </div>
    </main>
  );
}
