"use client";

/**
 * IdeaView — la vista de idea (canon 3.6, mockups 03-08): breadcrumb
 * "Mis ideas / <nombre>" + stepper de 5 etapas canónicas en el header,
 * layout de riel (árbol punteado) + panel, y la vista Manos a la Obra
 * (checklist + ritual + mundos) detrás de ?vista=manos.
 *
 * REGLA DE ORO: el árbol y el stepper SOLO se alimentan de eventos
 * reales: nodos de la ruta que devuelve /turn, etapas del SSE del plan,
 * filas persistidas del checklist. La entrevista es una tarjeta a la
 * vez; el "recorrido" es un acordeón para releer, no un chat.
 * EL AZUL PIENSA (explorar, planear), EL VERDE EJECUTA (etapa 5).
 */
import Link from "next/link";
import { useRouter, useSearchParams } from "next/navigation";
import { useCallback, useEffect, useRef, useState } from "react";
import { Acordeon } from "../../ui/Acordeon";
import { AnalisisProyecto } from "../../ui/AnalisisProyecto";
import { Celebracion } from "../../ui/Celebracion";
import { CampoConVoz } from "../../ui/CampoConVoz";
import { ArbolPensante, type NodoArbol } from "../../ui/ArbolPensante";
import { ManosALaObra, grupoVigente, titulosDeEtapas, type ChecklistData, type PlanHistorial } from "../../ui/ManosALaObra";
import { Claridad } from "../../ui/Claridad";
import { PlanDocumento } from "../../ui/PlanDocumento";
import { CierreHonesto } from "../../ui/CierreHonesto";
import { PotenciaTuIdea } from "../../ui/PotenciaTuIdea";
import { ReporteCard } from "../../ui/ReporteCard";
import { Stepper } from "../../ui/Stepper";
import { TarjetaPregunta } from "../../ui/TarjetaPregunta";
import catalogo from "@/lib/assets/packs_catalog.json";
import type { ChecklistEstado } from "@/lib/dbContract";
import { consumirSSE } from "@/lib/sseCliente";

const NOTA_SILENCIOSO = "cubierto por lo que contaste";
const ERROR_GENERICO = "algo se atoró de nuestro lado; intenta de nuevo en un momento";
/** Fase 4.3 §2: el servidor SIEMPRE manda el mensaje del cierre. Esto es la red
 * por si una respuesta vieja (o un despliegue a mitad) llega sin él: aun así, la
 * pantalla habla. Jamás muda. */
const MENSAJE_CIERRE_RESPALDO =
  "Hasta aquí puedo acompañarte por este camino. Tu idea queda guardada tal como está.";

interface DetalleIdea {
  idea: {
    id: string;
    nombre: string;
    entrada_original: string;
    modo_camino?: "ritmo" | "fechas" | null;
    realizada_at?: string | null;
  };
  organizador: { contenido_md: string } | null;
  plan: { etiqueta: string; contenido_md: string; created_at: string } | null;
  reporte: { contenido_md: string; created_at: string } | null;
  reporte_en_curso: { pregunta: string } | null;
  entrevista: {
    session_id: string;
    pregunta: string | null;
    listo_para_plan: boolean;
    dominio?: string;
    ruta: Array<{ id: string; titulo: string; etiqueta?: string; modo: string }>;
  } | null;
  /** recorrido que construyó el plan vigente (canon 05: sidebar de nodos). */
  recorrido?: Array<{ id: string; titulo: string; etiqueta?: string; modo: string }>;
  unlocks?: string[];
  mundos?: Array<{
    dominio: string;
    /** Fase 4.2: el mundo se dio por completado (migración 026). null = abierto. */
    completado_at?: string | null;
    cierre_motivo?: string | null;
    plan: { etiqueta: string; contenido_md: string; created_at: string } | null;
  }>;
  historial?: PlanHistorial[];
}

interface NodoNuevo {
  id: string;
  titulo: string;
  /** Fase 3.9: etiqueta_arbol para riel/cintillo; titulo respalda en detalle. */
  etiqueta?: string;
  modo: string;
}

interface RespuestaTurno {
  session_id: string;
  tipo: "pregunta" | "listo_para_plan" | "salio" | "error_temporal";
  pregunta?: string;
  nodos_nuevos?: NodoNuevo[];
  temas_pendientes?: string[];
  error?: string;
  /** Fase 4.3 §2: todo 'salio' viaja con su mensaje en palabras de persona. */
  mensaje?: string;
  /** el mundo era incompatible y su activación se devolvió (§1) */
  unlock_revertido?: boolean;
  /** Fase 4.3.2: creditos DE VERDAD devueltos (evento del ledger). null en beta. */
  creditos_devueltos?: number | null;
}

interface QA {
  pregunta: string;
  respuesta: string;
}

function nodoArbolDesdeRuta(n: { id: string; titulo: string; etiqueta?: string; modo: string }, idx: number): NodoArbol {
  return {
    id: `${idx}-${n.id}`,
    // Fase 3.9: la etiqueta_arbol enamora en el riel; el título solo respalda.
    label: n.etiqueta ?? n.titulo,
    titulo: n.titulo,
    atenuado: n.modo === "silencioso",
    salto: n.modo === "salto",
    nota: n.modo === "silencioso" ? NOTA_SILENCIOSO : undefined,
  };
}

const NOMBRE_MUNDO = Object.fromEntries(
  (catalogo as { packs: Array<{ clave: string; nombre: string; promesa: string }> }).packs.map((p) => [
    p.clave,
    { nombre: p.nombre, promesa: p.promesa },
  ])
);

export function IdeaView({ projectId }: { projectId: string }) {
  const router = useRouter();
  const searchParams = useSearchParams();
  const quiereEntrevista = searchParams.get("entrevista") === "1";
  const quiereManos = searchParams.get("vista") === "manos";
  const quiereAnalisis = searchParams.get("vista") === "analisis";
  const quiereCelebracion = searchParams.get("vista") === "celebracion";

  const [detalle, setDetalle] = useState<DetalleIdea | null>(null);
  const [cargando, setCargando] = useState(true);
  const [error, setError] = useState<string | null>(null);

  // --- entrevista ---
  const [sessionId, setSessionId] = useState<string | null>(null);
  const [pregunta, setPregunta] = useState<string | null>(null);
  const [cintillo, setCintillo] = useState<string | null>(null);
  const [enviando, setEnviando] = useState(false);
  const [listoParaPlan, setListoParaPlan] = useState(false);
  /** Fase 4.3 §2: el cierre honesto en pantalla (null = no hubo cierre). */
  const [cierre, setCierre] = useState<{ mensaje: string; creditosDevueltos: number | null } | null>(null);
  // Phase 3.7.2 (la oferta honesta): temas sobre la mesa cuando el motor
  // OFRECE el plan (null = cierre sin vuelta: CTA unico) y la tarjeta
  // intermedia de contexto final.
  const [temasPendientes, setTemasPendientes] = useState<string[] | null>(null);
  const [tarjetaContextoFinal, setTarjetaContextoFinal] = useState(false);
  const [contextoFinal, setContextoFinal] = useState("");
  const [recorrido, setRecorrido] = useState<QA[]>([]);
  const [nodos, setNodos] = useState<NodoArbol[]>([]);
  const contadorNodos = useRef(0);
  const [dominioEntrevista, setDominioEntrevista] = useState<string>("core");

  // --- plan ---
  const [generandoPlan, setGenerandoPlan] = useState(false);
  const [etiquetaEtapa, setEtiquetaEtapa] = useState<string | undefined>();
  const [planMd, setPlanMd] = useState<string | null>(null);
  // Fix (retry del stream del plan): si la redaccion muere tras los reintentos
  // del servidor, se guarda con que reintentarla. La sesion y el recorrido YA
  // estan persistidos: reintentar re-lanza SOLO la redaccion, nunca la entrevista.
  const [planFallido, setPlanFallido] = useState<{ sid: string; contexto?: string } | null>(null);
  const arrancoRef = useRef(false);
  // true desde que el usuario pide el plan de la sesion actual: los turnos
  // tardios de esa sesion ya no reabren la entrevista (carrera C0 bis).
  const planPedidoRef = useRef(false);

  // --- Manos a la Obra (Fase 3.6) ---
  const [vistaManos, setVistaManos] = useState(quiereManos);
  const [checklist, setChecklist] = useState<ChecklistData | null>(null);
  // Fase 3.8: el modo del camino ('ritmo'|'fechas'|null hasta elegir).
  const [modoCamino, setModoCamino] = useState<"ritmo" | "fechas" | null>(null);
  const [vistaAnalisis, setVistaAnalisis] = useState(quiereAnalisis);
  const [vistaCelebracion, setVistaCelebracion] = useState(quiereCelebracion);
  const [realizadaAt, setRealizadaAt] = useState<string | null>(null);

  const cargarChecklist = useCallback(async () => {
    try {
      const res = await fetch(`/api/project/${projectId}/checklist`);
      if (res.ok) setChecklist((await res.json()) as ChecklistData);
    } catch {
      /* el checklist es progresivo: sin él, la vista Manos avisa sola */
    }
  }, [projectId]);

  function agregarNodos(nuevos: NodoNuevo[] | undefined) {
    if (!nuevos?.length) return;
    setNodos((prev) => [
      ...prev,
      ...nuevos.map((n) => nodoArbolDesdeRuta(n, contadorNodos.current++)),
    ]);
    const conversado = [...nuevos].reverse().find((n) => n.modo !== "silencioso");
    if (conversado) setCintillo(conversado.etiqueta ?? conversado.titulo);
  }

  function procesarTurno(data: RespuestaTurno) {
    // C0 bis (cazado por el gate instrumentado): si el usuario pidió el
    // plan con un turno aún en vuelo, la respuesta tardía de ese turno
    // llegaba DESPUÉS de que generarPlan limpiara la pregunta y la
    // resucitaba — el plan terminaba pero la vista creía que la
    // entrevista seguía (sin CTA, sin fila de mundos). El plan manda: un
    // turno tardío de la misma sesión ya no reabre la entrevista.
    if (planPedidoRef.current) return;
    setSessionId(data.session_id);
    agregarNodos(data.nodos_nuevos);
    if (data.tipo === "pregunta" && data.pregunta) {
      setPregunta(data.pregunta);
    } else if (data.tipo === "listo_para_plan") {
      setPregunta(null);
      setListoParaPlan(true);
      setTemasPendientes(data.temas_pendientes ?? null);
    } else if (data.tipo === "salio") {
      // Fase 4.3 §2: antes esto era SOLO setPregunta(null) -- la pantalla se
      // quedaba muda y el usuario, que pudo haber pagado por este mundo, no
      // recibia ni una palabra. Un cierre sin explicacion es degradacion
      // silenciosa en su cara.
      setPregunta(null);
      setCierre({
        mensaje: data.mensaje ?? MENSAJE_CIERRE_RESPALDO,
        creditosDevueltos: data.creditos_devueltos ?? null,
      });
    }
  }

  /** Una sesión NUEVA (seguimiento o mundo) reinicia el riel y entra a la entrevista. */
  function entrarASesionNueva(data: RespuestaTurno, dominio: string) {
    setCierre(null);
    setNodos([]);
    contadorNodos.current = 0;
    setRecorrido([]);
    setListoParaPlan(false);
    setTemasPendientes(null);
    setTarjetaContextoFinal(false);
    setContextoFinal("");
    setPlanMd(null);
    setVistaManos(false);
    setDominioEntrevista(dominio);
    planPedidoRef.current = false;
    procesarTurno(data);
  }

  const generarPlan = useCallback(
    async (sid: string, contextoExtra?: string) => {
      if (generandoPlan) return;
      planPedidoRef.current = true;
      setGenerandoPlan(true);
      setPregunta(null);
      // C0 (la puerta que falta): sin esto, llegar al plan desde
      // "Suficiente para avanzar" dejaba entrevistaActiva=true para
      // siempre y escondía el CTA "Pasar a Manos a la Obra" y la fila
      // "Potencia tu idea" — el fundador terminaba su plan sin ninguna
      // puerta visible hacia la etapa 5 ni hacia los 6 mundos.
      setListoParaPlan(false);
      setError(null);
      setPlanFallido(null);
      try {
        // Phase 3.7.2: el contexto final opcional viaja al redactor.
        const res = await fetch(`/api/session/${sid}/plan`, {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify(contextoExtra ? { contexto_final: contextoExtra } : {}),
        });
        if (!res.ok || !res.body) {
          setError(ERROR_GENERICO);
          setGenerandoPlan(false);
          planPedidoRef.current = false;
          return;
        }
        // Árbol de etapas: cada encabezado "## " que llega por el stream
        // REAL enciende un punto (regla de oro: cero teatro).
        let crudo = "";
        const etapasVistas = new Set<string>();
        await consumirSSE(res, ({ evento, data }) => {
          if (evento === "reinicio") {
            // Un intento del redactor murió a mitad y el servidor va a reintentar.
            // Lo que ese intento alcanzó a pintar NO corresponde al texto nuevo:
            // se descarta para no mezclar dos redacciones en el mismo árbol.
            crudo = "";
            etapasVistas.clear();
            setNodos((prev) => prev.filter((n) => !n.id.startsWith("etapa-")));
            setEtiquetaEtapa(undefined);
          } else if (evento === "delta") {
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
            // El plan nuevo derivó SU checklist al persistirse (3.3): refrescar.
            void cargarChecklist();
          } else if (evento === "error") {
            setError(
              "no pudimos terminar de escribir tu plan; lo que contaste está guardado, así que no hay que repetir nada"
            );
            setPlanFallido({ sid, contexto: contextoExtra });
            planPedidoRef.current = false;
          }
        });
      } catch {
        setError("la conexión se cortó mientras armábamos tu plan; tu recorrido quedó guardado");
        setPlanFallido({ sid, contexto: contextoExtra });
        planPedidoRef.current = false;
      } finally {
        setGenerandoPlan(false);
        setEtiquetaEtapa(undefined);
      }
    },
    [generandoPlan, cargarChecklist]
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
        setModoCamino(d.idea.modo_camino ?? null);
        setRealizadaAt(d.idea.realizada_at ?? null);
        // Una idea ya realizada abre en su Celebración (salvo que la URL
        // pida otra vista explícita).
        if (d.idea.realizada_at && !quiereManos && !quiereAnalisis) setVistaCelebracion(true);
        if (d.plan) {
          setPlanMd(d.plan.contenido_md);
          void cargarChecklist();
        }
        if (d.entrevista) {
          setSessionId(d.entrevista.session_id);
          setPregunta(d.entrevista.pregunta);
          setListoParaPlan(d.entrevista.listo_para_plan);
          setDominioEntrevista(d.entrevista.dominio ?? "core");
          setNodos(d.entrevista.ruta.map(nodoArbolDesdeRuta));
          contadorNodos.current = d.entrevista.ruta.length;
          const conversado = [...d.entrevista.ruta].reverse().find((n) => n.modo !== "silencioso");
          if (conversado) setCintillo(conversado.etiqueta ?? conversado.titulo);
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

  /** Phase 3.7.2: "Seguimos explorando" es un click, no una frase — viaja
   * como sentinela y el motor lo entiende sin gastar en clasificarlo. */
  async function seguirExplorando() {
    if (!sessionId || enviando) return;
    setEnviando(true);
    setError(null);
    setListoParaPlan(false);
    setTemasPendientes(null);
    try {
      const res = await fetch(`/api/session/${sessionId}/turn`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ respuesta: "__seguimos_explorando__" }),
      });
      if (!res.ok) {
        setError(ERROR_GENERICO);
        setListoParaPlan(true);
        return;
      }
      procesarTurno((await res.json()) as RespuestaTurno);
    } catch {
      setError("no pudimos continuar; revisa tu internet e intenta de nuevo");
      setListoParaPlan(true);
    } finally {
      setEnviando(false);
    }
  }

  function irAManos() {
    setVistaManos(true);
    router.replace(`/idea/${projectId}?vista=manos`, { scroll: false });
  }

  function volverAlViaje() {
    setVistaManos(false);
    setVistaAnalisis(false);
    setVistaCelebracion(false);
    router.replace(`/idea/${projectId}`, { scroll: false });
  }

  function irAAnalisis() {
    setVistaAnalisis(true);
    setVistaCelebracion(false);
    router.replace(`/idea/${projectId}?vista=analisis`, { scroll: false });
  }

  function volverAManos() {
    setVistaAnalisis(false);
    setVistaCelebracion(false);
    setVistaManos(true);
    router.replace(`/idea/${projectId}?vista=manos`, { scroll: false });
  }

  function irACelebracion() {
    setRealizadaAt(new Date().toISOString());
    setVistaManos(false);
    setVistaAnalisis(false);
    setVistaCelebracion(true);
    router.replace(`/idea/${projectId}?vista=celebracion`, { scroll: false });
  }

  if (cargando) {
    return <p className="px-6 py-12 text-dim">Cargando tu idea…</p>;
  }
  if (!detalle) {
    return (
      <div className="px-6 py-12">
        <p className="text-warn">{error ?? ERROR_GENERICO}</p>
        <Link href="/ideas" className="mt-4 inline-block text-accent">
          Volver a mis ideas
        </Link>
      </div>
    );
  }

  const entrevistaActiva = Boolean(pregunta) || enviando || listoParaPlan;
  const mostrarArbol = nodos.length > 0 && (entrevistaActiva || generandoPlan);
  const puedeGenerarPlan = Boolean(sessionId) && !generandoPlan && !planMd;

  // Progreso real del checklist (para stepper, chips y fila de potenciadores).
  const coreVigente = checklist ? grupoVigente(checklist, "core") : null;
  const itemsCore = coreVigente?.etapas.flatMap((e) => e.items) ?? [];
  const hechosCore = itemsCore.filter((i) => i.estado === "hecho").length;
  const enObra = itemsCore.some((i) => i.estado !== "pendiente") || detalle.plan?.etiqueta === "seguimiento";
  const unlocks = detalle.unlocks ?? [];
  const progresoMundos: Record<string, { hechos: number; total: number } | null> = {};
  for (const u of unlocks) {
    const g = checklist ? grupoVigente(checklist, u) : null;
    const items = g?.etapas.flatMap((e) => e.items) ?? [];
    progresoMundos[u] = g
      ? { hechos: items.filter((i) => i.estado === "hecho").length, total: items.length }
      : null;
  }

  // Etapa canónica para el stepper: solo verdad del motor.
  let etapaStepper: number;
  let pensandoStepper = false;
  let etiquetaStepper: string | undefined;
  if (generandoPlan) {
    etapaStepper = 4;
    pensandoStepper = true;
    etiquetaStepper = "Tu Plan · en camino…";
  } else if (entrevistaActiva) {
    etapaStepper = 3;
    pensandoStepper = Boolean(pregunta) || enviando;
    etiquetaStepper =
      dominioEntrevista !== "core"
        ? `${NOMBRE_MUNDO[dominioEntrevista]?.nombre ?? dominioEntrevista} · en curso…`
        : "La Exploración · en curso…";
  } else if (vistaManos || enObra) {
    etapaStepper = 5;
    etiquetaStepper = itemsCore.length > 0 ? `Manos a la Obra · ${hechosCore}/${itemsCore.length}` : "Manos a la Obra";
  } else if (planMd) {
    etapaStepper = 4;
    etiquetaStepper = "Tu Plan · listo";
  } else {
    etapaStepper = 2;
    etiquetaStepper = detalle.organizador ? "Claridad · lista" : undefined;
  }

  const arbol = (
    <ArbolPensante
      nodos={nodos}
      generando={enviando || generandoPlan}
      etiquetaGenerando={generandoPlan ? etiquetaEtapa : cintillo ?? undefined}
    />
  );

  // Canon 05 "Construido con tu recorrido": los conceptos del recorrido (no
  // los silenciosos ni las etapas del plan). De la API si el plan está hecho;
  // del riel vivo si acabamos de generarlo. Fase 3.9: la etiqueta_arbol también
  // aquí (superficie de navegación), consistente entre vivo y recarga.
  const nodosFuente =
    detalle.recorrido && detalle.recorrido.length > 0
      ? detalle.recorrido.filter((n) => n.modo !== "silencioso").map((n) => n.etiqueta ?? n.titulo)
      : nodos.filter((n) => !n.atenuado && !n.id.startsWith("etapa-")).map((n) => n.label);

  const mundosParaObra = unlocks.map((dominio) => {
    const m = detalle.mundos?.find((x) => x.dominio === dominio);
    return {
      dominio,
      nombre: NOMBRE_MUNDO[dominio]?.nombre ?? dominio,
      promesa: NOMBRE_MUNDO[dominio]?.promesa ?? "",
      plan: m?.plan ?? null,
      completadoAt: m?.completado_at ?? null,
    };
  });

  return (
    <div className="flex min-h-full flex-1 flex-col">
      {/* header canon: breadcrumb + stepper de 5 etapas */}
      <header className="flex h-[58px] items-center gap-5 border-b border-hairline px-5 sm:px-6">
        <div className="flex min-w-0 items-center gap-2.5">
          <Link href="/ideas" className="shrink-0 text-[13px] text-dim hover:text-ink">
            Mis ideas /
          </Link>
          <span className="truncate text-[14.5px] font-semibold">{detalle.idea.nombre}</span>
          {realizadaAt && (
            <span className="inline-flex shrink-0 items-center gap-1 rounded-full border border-done/50 px-2 py-0.5 text-[11px] font-bold text-done">
              <svg width="9" height="9" viewBox="0 0 12 12" aria-hidden>
                <path d="M2.5 6.5l2.5 2.5 4.5-5.5" stroke="var(--done)" strokeWidth="2" fill="none" />
              </svg>
              Proyecto
            </span>
          )}
        </div>
        <span className="flex-1" />
        <div className="hidden md:block">
          <Stepper etapa={etapaStepper} pensando={pensandoStepper} etiqueta={etiquetaStepper} />
        </div>
        <span
          className={
            "md:hidden whitespace-nowrap text-[12px] font-semibold " +
            (etapaStepper === 5 ? "text-done" : "text-accent")
          }
        >
          {etiquetaStepper}
        </span>
      </header>

      <main className="mx-auto w-full max-w-5xl flex-1 px-4 py-8 sm:px-6">
        {error && (
          <div className="mb-4 flex flex-wrap items-center gap-x-4 gap-y-2">
            <p className="text-sm text-warn">{error}</p>
            {/* Reintenta SOLO la redaccion sobre la misma sesion: la entrevista
                ya esta persistida y no se repite. */}
            {planFallido && !generandoPlan && (
              <button
                onClick={() => generarPlan(planFallido.sid, planFallido.contexto)}
                className="rounded-[8px] border border-accent/50 px-3.5 py-1.5 text-[13px] font-semibold text-accent hover:bg-accent/10"
              >
                Intentar de nuevo
              </button>
            )}
          </div>
        )}

        {vistaCelebracion ? (
          <Celebracion
            projectId={projectId}
            onVerAnalisis={irAAnalisis}
            onVolverIdeas={() => router.push("/ideas")}
            onReabierto={() => {
              setRealizadaAt(null);
              volverAManos();
            }}
          />
        ) : vistaAnalisis && planMd && checklist ? (
          <AnalisisProyecto projectId={projectId} titulos={titulosDeEtapas(planMd)} onVolver={volverAManos} />
        ) : vistaManos && planMd && checklist ? (
          <>
            <button onClick={volverAlViaje} className="mb-5 text-sm text-dim hover:text-ink">
              ← Ver el plan
            </button>
            <ManosALaObra
              projectId={projectId}
              planMd={planMd}
              planCreatedAt={detalle.plan?.created_at ?? itemsCore[0]?.created_at ?? new Date().toISOString()}
              checklist={checklist}
              historial={detalle.historial ?? []}
              mundos={mundosParaObra}
              modoCamino={modoCamino}
              onModoCambiado={setModoCamino}
              onRecargarChecklist={cargarChecklist}
              onVerAnalisis={irAAnalisis}
              onRealizada={irACelebracion}
              onMundoCerrado={(dominio, completadoAt) =>
                // Fase 4.2 §3: cerrar un mundo NO cierra la idea — aquí no se
                // toca realizada_at ni se abre la Celebración. Solo su chip.
                setDetalle((prev) =>
                  prev
                    ? {
                        ...prev,
                        mundos: prev.mundos?.map((m) =>
                          m.dominio === dominio ? { ...m, completado_at: completadoAt } : m
                        ),
                      }
                    : prev
                )
              }
              entrevistaAbierta={Boolean(pregunta)}
              onVolverEntrevista={volverAlViaje}
              onItemActualizado={({ id, estado, completed_at, nota, fecha_base, fecha_base_original, fecha_base_origen }) => {
                setChecklist((prev) =>
                  prev
                    ? {
                        ...prev,
                        planes: prev.planes.map((p) => ({
                          ...p,
                          etapas: p.etapas.map((e) => ({
                            ...e,
                            items: e.items.map((i) =>
                              i.id === id
                                ? {
                                    ...i,
                                    ...(estado !== undefined ? { estado: estado as ChecklistEstado } : {}),
                                    ...(completed_at !== undefined ? { completed_at } : {}),
                                    ...(nota !== undefined ? { nota } : {}),
                                    ...(fecha_base !== undefined ? { fecha_base } : {}),
                                    ...(fecha_base_original !== undefined ? { fecha_base_original } : {}),
                                    ...(fecha_base_origen !== undefined ? { fecha_base_origen } : {}),
                                    updated_at: new Date().toISOString(),
                                  }
                                : i
                            ),
                          })),
                        })),
                      }
                    : prev
                );
              }}
              onSeguimientoIniciado={(data) => entrarASesionNueva(data as RespuestaTurno, "core")}
              onMundoIniciado={(data, dominio) => entrarASesionNueva(data as RespuestaTurno, dominio)}
            />
          </>
        ) : (
          <div className="flex flex-col gap-6 sm:grid sm:grid-cols-[190px_1fr] sm:gap-8">
            {/* Riel izquierdo: el árbol (en móvil, acordeón arriba) */}
            {mostrarArbol && (
              <>
                <div className="hidden sm:block">
                  <p className="mb-4 text-[11px] font-semibold uppercase tracking-[1.2px] text-dim">
                    Recorrido de la idea
                  </p>
                  {arbol}
                </div>
                <div className="sm:hidden">
                  <Acordeon titulo="Recorrido de la idea" abierto={generandoPlan}>
                    {arbol}
                  </Acordeon>
                </div>
              </>
            )}

            <div className={"flex min-w-0 flex-col gap-4" + (mostrarArbol ? "" : " sm:col-span-2")}>
              {/* Fase 4.3 §2 — EL CIERRE HONESTO. Va antes que todo lo demas:
                  si el motor salio, esto es lo que el usuario tiene que ver, y
                  no una pantalla en blanco. */}
              {cierre && (
                <CierreHonesto
                  mensaje={cierre.mensaje}
                  creditosDevueltos={cierre.creditosDevueltos}
                  hayPlan={Boolean(planMd)}
                  onVolverAManos={() => {
                    setCierre(null);
                    irAManos();
                  }}
                  onVerMundos={() => {
                    setCierre(null);
                    document.getElementById("tus-numeros")?.scrollIntoView({ behavior: "smooth" });
                  }}
                />
              )}
              {/* Tarjeta de pregunta (una a la vez) */}
              {pregunta && !tarjetaContextoFinal && (
                <TarjetaPregunta
                  cintillo={cintillo}
                  pregunta={pregunta}
                  enviando={enviando}
                  onEnviar={responder}
                  textoBoton="Enviar"
                />
              )}
              {!pregunta && enviando && (
                <p className="text-sm text-dim">Pensando la siguiente pregunta…</p>
              )}

              {/* Phase 3.7.2 — tarjeta intermedia (canon 04): contexto final
                  opcional antes de armar el plan. */}
              {tarjetaContextoFinal && !generandoPlan && !planMd && (
                <div className="rounded-panel border border-hairline bg-surface p-6 sm:p-7">
                  <p className="text-[19px] font-semibold leading-normal [text-wrap:pretty]">
                    ¿Algo más que quieras que tu plan tome en cuenta?
                  </p>
                  <div className="mt-5">
                    <CampoConVoz
                      id="contexto-final"
                      valor={contextoFinal}
                      onCambio={setContextoFinal}
                      filas={3}
                      placeholder="Opcional: escríbelo o díctalo…"
                    />
                  </div>
                  <button
                    onClick={() => {
                      if (!sessionId) return;
                      setTarjetaContextoFinal(false);
                      generarPlan(sessionId, contextoFinal.trim() || undefined);
                    }}
                    className="mt-5 w-full rounded-[10px] bg-accent px-5 py-3 text-sm font-semibold text-white hover:opacity-90"
                  >
                    Armar mi plan
                  </button>
                </div>
              )}

              {/* Phase 3.7.2 — LA OFERTA HONESTA (canon 04): con temas sobre
                  la mesa = pills + doble CTA de peso igual; ruta completa =
                  honestidad inversa; cierre sin vuelta (presupuesto,
                  profundidad) = CTA único. */}
              {listoParaPlan && !tarjetaContextoFinal && !generandoPlan && !planMd && (
                <div className="rounded-panel border border-hairline bg-surface p-6 sm:p-7">
                  <p className="mb-3.5 flex items-center gap-2 text-[11px] font-semibold uppercase tracking-[1.2px] text-dim">
                    <span aria-hidden className="h-1.5 w-1.5 rounded-full bg-accent" />
                    {temasPendientes === null ? "Suficiente para avanzar" : "Tu recorrido hasta aquí"}
                  </p>
                  <p className="text-[19px] font-semibold leading-normal [text-wrap:pretty]">
                    {temasPendientes === null
                      ? "Con lo que me contaste alcanza: vamos a tu plan."
                      : "Con lo que me contaste puedo armar tu plan."}
                  </p>
                  {temasPendientes !== null && temasPendientes.length > 0 && (
                    <>
                      <p className="mt-3.5 text-[13.5px] text-dim">Si quieres, seguimos explorando:</p>
                      <div className="mt-2.5 flex flex-wrap gap-2">
                        {temasPendientes.map((tema) => (
                          <span
                            key={tema}
                            className="rounded-full px-3.5 py-1.5 text-[12.5px] font-medium"
                            style={{ border: "1px solid rgba(77,124,254,0.4)" }}
                          >
                            {tema}
                          </span>
                        ))}
                      </div>
                    </>
                  )}
                  {temasPendientes !== null && temasPendientes.length === 0 && (
                    <p className="mt-3.5 text-[13.5px] text-dim">Cubrimos lo esencial de punta a punta.</p>
                  )}
                  {temasPendientes === null ? (
                    <button
                      onClick={() => setTarjetaContextoFinal(true)}
                      className="mt-6 w-full rounded-[10px] bg-accent px-5 py-3 text-sm font-semibold text-white hover:opacity-90"
                    >
                      Generar mi plan
                    </button>
                  ) : (
                    <div className="mt-6 flex gap-3">
                      <button
                        onClick={seguirExplorando}
                        disabled={enviando}
                        className="flex-1 rounded-[10px] px-3 py-3 text-sm font-semibold hover:bg-accent/10 disabled:opacity-50"
                        style={{ border: "1px solid rgba(77,124,254,0.5)" }}
                      >
                        Seguimos explorando
                      </button>
                      <button
                        onClick={() => setTarjetaContextoFinal(true)}
                        disabled={enviando}
                        className="flex-1 rounded-[10px] px-3 py-3 text-sm font-semibold hover:bg-accent/10 disabled:opacity-50"
                        style={{ border: "1px solid rgba(77,124,254,0.5)" }}
                      >
                        Generar mi plan
                      </button>
                    </div>
                  )}
                  <p className="mt-4 text-center text-xs text-dim opacity-80">
                    Tu plan puede profundizarse después con el seguimiento.
                  </p>
                </div>
              )}

              {puedeGenerarPlan && pregunta && !tarjetaContextoFinal && (
                <button
                  onClick={() => setTarjetaContextoFinal(true)}
                  className="self-start text-sm text-dim hover:text-ink"
                >
                  Generar mi plan con lo que ya conté
                </button>
              )}

              {/* C5 (canon 04→05): la espera del plan es una tarjeta con el
                  anillo pensando y la etapa que va llegando por SSE — el
                  riel de la izquierda enciende cada etapa real. */}
              {generandoPlan && (
                <div className="anima-plan-in rounded-panel border border-hairline bg-surface p-6">
                  <p className="flex items-center gap-2.5 text-[11px] font-semibold uppercase tracking-[1.2px] text-accent">
                    <span className="relative inline-block h-3 w-3">
                      <span
                        className="anima-spin-ring absolute inset-0 box-border rounded-full border-2"
                        style={{ borderColor: "rgba(77,124,254,0.2)", borderTopColor: "var(--accent)" }}
                      />
                    </span>
                    Tu Plan · en camino
                  </p>
                  <p className="mt-3 text-[17px] font-medium leading-relaxed">
                    {etiquetaEtapa ? `Escribiendo: ${etiquetaEtapa}` : "Armando tu plan por etapas."}
                  </p>
                  <p className="mt-1.5 text-sm text-dim">
                    Cada etapa se enciende en el recorrido cuando queda escrita de verdad.
                  </p>
                </div>
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

              {/* Plan como documento (canon 05) */}
              {planMd && (
                <PlanDocumento
                  md={planMd}
                  nombreIdea={detalle.idea.nombre}
                  onEmpezar={() => irAManos()}
                  nodosFuente={nodosFuente}
                />
              )}

              {/* CTA canon 05: el verde ejecuta espera en la etapa 5.
                  Fase 4.0 (regla de UNA sola puerta, docs/FLUJO_TRACKING.md §2):
                  esta pantalla es un DOCUMENTO, no una puerta. El antiguo
                  "Ajustar el plan" abría aquí el ritual de seguimiento —
                  prematuro (disparaba el follow con cero avance: "llevas 0 de
                  28") y duplicado: la única puerta al ritual es Manos a la Obra
                  → "Contar qué pasó". Ajustar sin haber ejecutado es regenerar,
                  y regenerar no es el producto. */}
              {planMd && !generandoPlan && !entrevistaActiva && (
                <div className="flex flex-wrap items-center gap-3">
                  <button
                    onClick={() => irAManos()}
                    className="rounded-[10px] bg-accent px-6 py-3 text-sm font-semibold text-white hover:opacity-90"
                  >
                    Pasar a Manos a la Obra
                  </button>
                </div>
              )}

              {/* Bajo el plan: Tus Números (canon 05/07, 2 créditos) */}
              {planMd && !generandoPlan && (
                <div id="tus-numeros">
                  <ReporteCard
                    projectId={projectId}
                    contenidoInicial={detalle.reporte?.contenido_md ?? null}
                    preguntaPendiente={detalle.reporte_en_curso?.pregunta ?? null}
                  />
                </div>
              )}

              {/* Claridad persistida (canon 03) cuando no hay nada más activo */}
              {!entrevistaActiva && !planMd && !generandoPlan && detalle.organizador && (
                <>
                  <Claridad md={detalle.organizador.contenido_md} />
                  <div className="flex flex-wrap items-center gap-3">
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
                      className="rounded-[10px] bg-accent px-5 py-3 font-medium text-white hover:opacity-90"
                    >
                      Explorar estas suposiciones
                    </button>
                  </div>
                  <p className="text-xs text-dim">
                    La Exploración usa 5 créditos. Tu Claridad es gratis y queda guardada para siempre.
                  </p>
                </>
              )}

              {/* Fila de potenciadores (canon 07 B): visible desde Claridad */}
              {!entrevistaActiva && !generandoPlan && (planMd || detalle.organizador) && (
                <PotenciaTuIdea
                  projectId={projectId}
                  unlocks={unlocks}
                  progresoMundos={progresoMundos}
                  mundosCompletados={mundosParaObra.filter((m) => m.completadoAt).map((m) => m.dominio)}
                  conPlan={Boolean(planMd)}
                  onVerMundo={() => irAManos()}
                  onActivarMundo={(dominio) => {
                    // Beta: el mundo quedó activado (unlock gratis). Se añade a
                    // la lista local para que su tarjeta pase a "Activo" y su
                    // sección aparezca en Manos a la Obra, y se entra ahí para
                    // que el usuario lo explore de inmediato.
                    setDetalle((prev) =>
                      prev
                        ? { ...prev, unlocks: [...new Set([...(prev.unlocks ?? []), dominio])] }
                        : prev
                    );
                    irAManos();
                  }}
                  onTusNumeros={() =>
                    document.getElementById("tus-numeros")?.scrollIntoView({ behavior: "smooth" })
                  }
                />
              )}
            </div>
          </div>
        )}
      </main>
    </div>
  );
}
