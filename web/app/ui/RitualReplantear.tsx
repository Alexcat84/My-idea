"use client";

/**
 * RitualReplantear: "Replantear mi camino" (ciclo de replanteamiento, Fase 2;
 * docs/producto/CICLO_REPLANTEAMIENTO.md). La entrada hermana de "Profundizar
 * mi plan" para cuando algo cambió o se rompió. Cuatro pasos y SIN entrevista:
 *   1. Tu historia, OBLIGATORIA, con texto y dictado y preguntas de ayuda.
 *   2. Lo que ya construiste: cada hecha del plan vigente, "Me sigue sirviendo"
 *      (por omisión) o "Ya no aplica".
 *   3. Caminos posibles: POST /api/project/{id}/replantear, que aparta el precio,
 *      crea la sesión y devuelve dos o tres caminos. Se elige uno.
 *   4. Confirmar y generar: resumen, precio (montoDelPlan, la regla del cobro) y
 *      la promesa de cobro. El plan lo genera el padre (onListo) por la ruta de
 *      siempre, con el camino elegido.
 * Sirve al núcleo y a cada mundo (`mundo` es su nombre, `dominio` su clave),
 * igual que RitualContinuar.
 *
 * Los pasos se exportan sueltos porque son pantallas puras: las pruebas los
 * pintan uno por uno sin simular clics.
 */
import { useState } from "react";
import { CampoConVoz } from "./CampoConVoz";
import type { ItemChecklistUI } from "./ManosALaObra";
import { MAX_LARGO_TEXTO_USUARIO } from "@/lib/constants";
import { errorGenerico, irAlDesafio, leerRechazo } from "@/lib/mensajeServidor";
import { loginConNext } from "@/lib/nextSeguro";
import { montoDelPlan } from "@/lib/precios";
import { elegir } from "@/lib/i18n/config";
import { useIdioma } from "@/lib/i18n/IdiomaProvider";
import { interpolar } from "@/lib/i18n/interpolar";
import { MANOS_A_LA_OBRA } from "@/lib/i18n/mensajes/manosALaObra";

export interface CaminoPosible {
  id: string;
  titulo: string;
  descripcion: string;
}

const BOTON =
  "rounded-[10px] border border-accent/40 bg-accent/10 px-5 py-2.5 font-medium text-accent hover:bg-accent/20 disabled:opacity-50";
const ENLACE = "text-sm text-dim hover:text-ink";

/** Las tareas que cuentan como "lo que ya construiste": las hechas del plan. */
export function hechasDe(items: ItemChecklistUI[]): ItemChecklistUI[] {
  return items.filter((i) => i.estado === "hecho");
}

/** Recorta la historia para el resumen del paso 4 (se ve entera en el paso 1). */
function recortar(texto: string, max = 220): string {
  return texto.length <= max ? texto : texto.slice(0, max).trimEnd() + "…";
}

/** Paso 1: tu historia. Obligatoria y con tope de largo. */
export function PasoHistoria({
  mundo,
  historia,
  onCambio,
  onSeguir,
}: {
  mundo?: string;
  historia: string;
  onCambio: (v: string) => void;
  onSeguir: () => void;
}) {
  const t = elegir(MANOS_A_LA_OBRA, useIdioma());
  const larga = historia.trim().length > MAX_LARGO_TEXTO_USUARIO;
  const vacia = historia.trim().length === 0;
  return (
    <>
      <p className="text-[17px] font-medium leading-relaxed">{t.replantear.historiaTitulo}</p>
      <p className="mt-2 text-sm text-dim">
        {mundo ? interpolar(t.replantear.historiaDescMundo, { mundo }) : t.replantear.historiaDesc}
      </p>
      {/* Las preguntas de ayuda son una pista suave, no un formulario: se leen
          y la persona cuenta lo suyo como quiera. */}
      <div className="mt-3 rounded-[10px] border border-dashed border-accent/30 bg-accent/5 px-4 py-3">
        <p className="text-[12.5px] text-dim">{t.replantear.ayudaTitulo}</p>
        <ul className="mt-1.5 flex flex-col gap-1">
          {t.replantear.ayudas.map((a) => (
            <li key={a} className="flex items-start gap-2 text-[13px] text-ink/85">
              <span aria-hidden className="mt-[8px] h-1.5 w-1.5 shrink-0 rounded-full bg-accent/60" />
              {a}
            </li>
          ))}
        </ul>
      </div>
      <div className="mt-3">
        <CampoConVoz id="replantear-historia" valor={historia} onCambio={onCambio} filas={5} placeholder={t.replantear.placeholderHistoria} />
      </div>
      {larga && (
        <p className="mt-2 text-sm text-warn">{interpolar(t.replantear.historiaLarga, { max: MAX_LARGO_TEXTO_USUARIO })}</p>
      )}
      <div className="mt-3 flex items-center gap-3">
        <button onClick={onSeguir} disabled={vacia || larga} className={BOTON}>
          {t.ritual.seguir}
        </button>
      </div>
    </>
  );
}

/** Paso 2: lo que ya construiste. Solo las hechas del plan vigente del espacio. */
export function PasoConstruido({
  items,
  sueltas,
  dominio = "core",
  onAlternar,
  onSeguir,
  onAtras,
}: {
  items: ItemChecklistUI[];
  /** ids de las hechas marcadas "Ya no aplica" (las demás se conservan) */
  sueltas: ReadonlySet<string>;
  dominio?: string;
  onAlternar: (id: string, suelta: boolean) => void;
  onSeguir: () => void;
  onAtras: () => void;
}) {
  const t = elegir(MANOS_A_LA_OBRA, useIdioma());
  const hechas = hechasDe(items);
  const opcion = (activa: boolean) =>
    "rounded-full border px-3 py-1 text-[12px] font-semibold " +
    (activa ? "border-accent/60 bg-accent/15 text-accent" : "border-white/15 text-dim hover:border-white/30 hover:text-ink");
  return (
    <>
      <p className="text-[17px] font-medium leading-relaxed">{t.replantear.construidoTitulo}</p>
      {hechas.length === 0 ? (
        <p className="mt-2 text-sm text-dim">{t.replantear.sinHechas}</p>
      ) : (
        <>
          <p className="mt-2 text-sm text-dim">{t.replantear.construidoDesc}</p>
          <ul className="mt-3 flex flex-col gap-2">
            {hechas.map((i) => {
              const suelta = sueltas.has(i.id);
              return (
                <li key={i.id} className="rounded-cinta border border-hairline bg-surface-2/40 px-4 py-3">
                  <p className={"text-[14px] " + (suelta ? "text-dim line-through" : "text-ink")}>{i.texto}</p>
                  <div className="mt-2 flex flex-wrap gap-2" role="group" aria-label={i.texto}>
                    <button type="button" aria-pressed={!suelta} onClick={() => onAlternar(i.id, false)} className={opcion(!suelta)}>
                      {t.replantear.meSirve}
                    </button>
                    <button type="button" aria-pressed={suelta} onClick={() => onAlternar(i.id, true)} className={opcion(suelta)}>
                      {t.replantear.yaNoAplica}
                    </button>
                  </div>
                </li>
              );
            })}
          </ul>
        </>
      )}
      {/* Al seguir nace la sesión y se aparta el precio: se dice ANTES. */}
      <p className="mt-3 text-xs text-dim opacity-80">
        {interpolar(t.replantear.apartado, { n: montoDelPlan(dominio, true, true) })}
      </p>
      <div className="mt-3 flex items-center gap-3">
        <button onClick={onSeguir} className={BOTON}>
          {t.ritual.seguir}
        </button>
        <button onClick={onAtras} className={ENLACE}>
          {t.ritual.atras}
        </button>
      </div>
    </>
  );
}

/** Paso 3: caminos posibles. Una sola elección (radio). */
export function PasoCaminos({
  caminos,
  cargando,
  error,
  elegido,
  onElegir,
  onReintentar,
  onSeguir,
  onAtras,
}: {
  caminos: CaminoPosible[] | null;
  cargando: boolean;
  error: string | null;
  elegido: string | null;
  onElegir: (id: string) => void;
  onReintentar: () => void;
  onSeguir: () => void;
  onAtras: () => void;
}) {
  const t = elegir(MANOS_A_LA_OBRA, useIdioma());
  return (
    <>
      <p className="text-[17px] font-medium leading-relaxed">{t.replantear.caminosTitulo}</p>
      {cargando && (
        <p className="mt-3 flex items-center gap-2 text-sm text-accent" role="status">
          <span aria-hidden className="h-2 w-2 animate-pulse rounded-full bg-accent" />
          {t.replantear.caminosPensando}
        </p>
      )}
      {!cargando && error && (
        <div className="mt-3">
          <p className="text-sm text-warn">{error}</p>
          <button onClick={onReintentar} className={"mt-3 " + BOTON}>
            {t.replantear.reintentar}
          </button>
        </div>
      )}
      {!cargando && !error && caminos && (
        <>
          <p className="mt-2 text-sm text-dim">{t.replantear.caminosDesc}</p>
          <fieldset className="mt-3 flex flex-col gap-2.5">
            <legend className="sr-only">{t.replantear.caminosTitulo}</legend>
            {caminos.map((c) => {
              const activo = elegido === c.id;
              return (
                <label
                  key={c.id}
                  className={
                    "flex cursor-pointer items-start gap-3 rounded-panel border px-4 py-3.5 " +
                    (activo ? "border-accent/60 bg-accent/10" : "border-hairline bg-surface hover:border-accent/35")
                  }
                >
                  <input
                    type="radio"
                    name="camino-replanteo"
                    value={c.id}
                    checked={activo}
                    onChange={() => onElegir(c.id)}
                    className="mt-1 accent-[var(--accent)]"
                  />
                  <span className="min-w-0">
                    <span className="block text-[15px] font-semibold text-ink">{c.titulo}</span>
                    {c.descripcion && <span className="mt-1 block text-[13px] leading-relaxed text-dim">{c.descripcion}</span>}
                  </span>
                </label>
              );
            })}
          </fieldset>
        </>
      )}
      <div className="mt-3 flex items-center gap-3">
        {!cargando && !error && caminos && (
          <button onClick={onSeguir} disabled={!elegido} className={BOTON}>
            {t.ritual.seguir}
          </button>
        )}
        <button onClick={onAtras} disabled={cargando} className={ENLACE + " disabled:opacity-50"}>
          {t.ritual.atras}
        </button>
      </div>
    </>
  );
}

/** Paso 4: confirmar y generar. El precio sale de la regla del cobro. */
export function PasoConfirmar({
  dominio,
  historia,
  conservas,
  sueltas,
  camino,
  enviando,
  onGenerar,
  onAtras,
}: {
  dominio: string;
  historia: string;
  conservas: number;
  sueltas: number;
  camino: CaminoPosible;
  enviando: boolean;
  onGenerar: () => void;
  onAtras: () => void;
}) {
  const t = elegir(MANOS_A_LA_OBRA, useIdioma());
  const precio = montoDelPlan(dominio, true, true);
  return (
    <>
      <p className="text-[17px] font-medium leading-relaxed">{t.replantear.confirmarTitulo}</p>
      <div className="mt-3 flex flex-col gap-3 rounded-[12px] border border-hairline bg-surface-2/40 px-4 py-3.5 text-[13.5px]">
        <div>
          <p className="text-[11px] font-semibold uppercase tracking-[1px] text-dim">{t.replantear.resumenHistoria}</p>
          <p className="mt-1 whitespace-pre-line text-ink/90">{recortar(historia)}</p>
        </div>
        <div className="flex flex-col gap-0.5 text-dim">
          <span>{interpolar(t.replantear.resumenConservas, { n: conservas })}</span>
          <span>{interpolar(t.replantear.resumenSueltas, { n: sueltas })}</span>
        </div>
        <div>
          <p className="text-[11px] font-semibold uppercase tracking-[1px] text-dim">{t.replantear.resumenCamino}</p>
          <p className="mt-1 font-semibold text-ink">{camino.titulo}</p>
        </div>
      </div>
      <div className="mt-3 flex flex-wrap items-center gap-3">
        <button onClick={onGenerar} disabled={enviando} className={BOTON}>
          {enviando ? t.ritual.pensando : interpolar(t.replantear.generar, { n: precio })}
        </button>
        <button onClick={onAtras} disabled={enviando} className={ENLACE + " disabled:opacity-50"}>
          {t.ritual.atras}
        </button>
      </div>
      {/* La garantía del cobro, en el momento de decidir (la misma del ritual). */}
      <p className="mt-3 text-xs text-dim opacity-80">{t.ritual.garantiaCobro}</p>
    </>
  );
}

export function RitualReplantear({
  projectId,
  dominio,
  mundo,
  items,
  onListo,
  onCerrar,
}: {
  projectId: string;
  /** "core" o el dominio del mundo: viaja al servidor y decide el precio. */
  dominio: string;
  /** el nombre del mundo (sin él, es el núcleo) */
  mundo?: string;
  /** las tareas del plan VIGENTE del espacio (el paso 2 toma las hechas) */
  items: ItemChecklistUI[];
  /** la sesión nació y hay camino elegido: el padre genera el plan */
  onListo: (sessionId: string, caminoId: string) => void;
  onCerrar: () => void;
}) {
  const idioma = useIdioma();
  const t = elegir(MANOS_A_LA_OBRA, idioma);
  const [paso, setPaso] = useState<1 | 2 | 3 | 4>(1);
  const [historia, setHistoria] = useState("");
  const [sueltas, setSueltas] = useState<Set<string>>(() => new Set());
  const [caminos, setCaminos] = useState<CaminoPosible[] | null>(null);
  const [sessionId, setSessionId] = useState<string | null>(null);
  // Con qué historia y qué sueltas se pidieron los caminos: si la persona vuelve
  // atrás y cambia algo, los caminos ya no le corresponden y se piden de nuevo.
  const [claveCaminos, setClaveCaminos] = useState<string | null>(null);
  const [elegido, setElegido] = useState<string | null>(null);
  const [cargando, setCargando] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [enviando, setEnviando] = useState(false);

  const hechas = hechasDe(items);
  const idsHechas = new Set(hechas.map((i) => i.id));
  const nSueltas = [...sueltas].filter((id) => idsHechas.has(id)).length;

  function alternar(id: string, suelta: boolean) {
    setSueltas((prev) => {
      const nuevo = new Set(prev);
      if (suelta) nuevo.add(id);
      else nuevo.delete(id);
      return nuevo;
    });
  }

  async function pedirCaminos(forzar = false) {
    const historiaLimpia = historia.trim();
    const suelta = [...sueltas].filter((id) => idsHechas.has(id)).sort();
    const clave = JSON.stringify([historiaLimpia, suelta]);
    setPaso(3);
    if (!forzar && clave === claveCaminos && caminos) return;
    // La sesión de los caminos anteriores (si los hubo): el servidor suelta su
    // precio apartado antes de apartar el de esta vuelta.
    const previa = sessionId;
    // Si el servidor dice que se llegó al tope de vueltas, la vuelta anterior
    // sigue viva (sus caminos y su precio apartado): se restaura para elegir.
    const anterior = { caminos, sessionId, claveCaminos, elegido };
    setCargando(true);
    setError(null);
    setCaminos(null);
    setElegido(null);
    setSessionId(null);
    try {
      const res = await fetch(`/api/project/${projectId}/replantear`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ historia: historiaLimpia, suelta, dominio, session_previa: previa }),
      });
      if (res.status === 401) {
        window.location.assign(loginConNext(`/idea/${projectId}?vista=manos`));
        return;
      }
      if (!res.ok) {
        const cuerpo = (await res.clone().json().catch(() => null)) as { tope?: unknown; error?: unknown } | null;
        if (cuerpo?.tope === true) {
          setCaminos(anterior.caminos);
          setSessionId(anterior.sessionId);
          setClaveCaminos(anterior.claveCaminos);
          setElegido(anterior.elegido);
          // Y la historia y las sueltas CON las que se pidió esa vuelta: el
          // resumen del paso 4 no puede mostrar un texto que el plan no usará.
          if (anterior.claveCaminos) {
            const [h, sueltasPrevias] = JSON.parse(anterior.claveCaminos) as [string, string[]];
            setHistoria(h);
            setSueltas(new Set(sueltasPrevias));
          }
          setError(typeof cuerpo.error === "string" ? cuerpo.error : errorGenerico(idioma));
          return;
        }
        // Igual que el follow: todo rechazo con razón (saldo, límite, fusible,
        // muros del mundo, doble factor, texto largo) se muestra tal cual.
        const r = await leerRechazo(res, idioma);
        setError(r.mensaje);
        if (r.tipo === "segundo_factor") void irAlDesafio(`/idea/${projectId}?vista=manos`);
        return;
      }
      const data = (await res.json()) as { session_id?: unknown; caminos?: unknown };
      const lista = Array.isArray(data.caminos)
        ? (data.caminos as CaminoPosible[]).filter((c) => c && typeof c.id === "string" && typeof c.titulo === "string")
        : [];
      if (typeof data.session_id !== "string" || lista.length === 0) {
        setError(errorGenerico(idioma));
        return;
      }
      setSessionId(data.session_id);
      setCaminos(lista.map((c) => ({ ...c, descripcion: typeof c.descripcion === "string" ? c.descripcion : "" })));
      setClaveCaminos(clave);
    } catch {
      setError(t.errores.conectar);
    } finally {
      setCargando(false);
    }
  }

  function generar() {
    if (!sessionId || !elegido || enviando) return;
    setEnviando(true);
    onListo(sessionId, elegido);
  }

  const camino = caminos?.find((c) => c.id === elegido) ?? null;

  return (
    <div className="rounded-panel border border-accent/40 bg-surface p-5 sm:p-6">
      <div className="mb-3 flex items-center justify-between">
        <p className="text-[11px] font-semibold uppercase tracking-[1.2px] text-accent">
          {mundo ? interpolar(t.replantear.encabezadoMundo, { mundo, paso }) : interpolar(t.replantear.encabezado, { paso })}
        </p>
        <button onClick={onCerrar} className={ENLACE}>
          {t.ritual.cerrar}
        </button>
      </div>

      {paso === 1 && <PasoHistoria mundo={mundo} historia={historia} onCambio={setHistoria} onSeguir={() => setPaso(2)} />}
      {paso === 2 && (
        <PasoConstruido
          items={items}
          sueltas={sueltas}
          dominio={dominio}
          onAlternar={alternar}
          onSeguir={() => void pedirCaminos()}
          onAtras={() => setPaso(1)}
        />
      )}
      {paso === 3 && (
        <PasoCaminos
          caminos={caminos}
          cargando={cargando}
          error={error}
          elegido={elegido}
          onElegir={setElegido}
          onReintentar={() => void pedirCaminos(true)}
          onSeguir={() => setPaso(4)}
          onAtras={() => setPaso(2)}
        />
      )}
      {paso === 4 && camino && (
        <PasoConfirmar
          dominio={dominio}
          historia={historia.trim()}
          conservas={hechas.length - nSueltas}
          sueltas={nSueltas}
          camino={camino}
          enviando={enviando}
          onGenerar={generar}
          onAtras={() => setPaso(3)}
        />
      )}
    </div>
  );
}
