"use client";

/**
 * TusNumeros.tsx - FASE B (canon 14): la pantalla de Tus Numeros, replica
 * financiera del Analisis. Veredicto de una frase con su color (ambar =
 * perdida, jamas rojo: espejo sin regano; verde = sano; azul = faltan datos),
 * tiles, la barra de la verdad, las tres palancas con su numero ya calculado,
 * escenarios, faltantes y el guardian. TODOS los numeros vienen del tablero
 * determinista (GET /api/project/[id]/numeros); la pantalla solo los pinta.
 */
import Link from "next/link";
import { useEffect, useState } from "react";
import type { ValorNumerico } from "@/lib/calculadora";
import type { Palanca, Palancas } from "@/lib/palancas";
import type { Tablero } from "@/lib/tableroNumeros";
import { fraseCicloCaja, type Veredicto } from "@/lib/numerosVivo";
import { fechaSello, momentoAbsoluto, selloVersion } from "@/lib/fechas";
import { CorregirCifras } from "@/app/ui/CorregirCifras";

interface VersionResumen {
  id: string;
  fecha: string;
  tono: Veredicto["tono"] | null;
  margen: ValorNumerico | null;
  vigente: boolean;
}

interface RespuestaNumeros {
  titulo: string | null;
  unidad: string | null;
  tablero: Tablero;
  veredicto: Veredicto;
  numeros_declarados: Record<string, number | { min: number; max: number }>;
  narracion: string | null;
  cifras_fecha: string | null;
  activado: boolean;
  historial?: VersionResumen[];
  /** ETAPA 2: sin activación no hay tablero; el GET devuelve la compuerta. */
  compuerta?: boolean;
  costo?: number;
  creditos_restantes?: number | null;
}

/** El payload de VISITAR una version pasada (GET ?version): modo lectura. */
interface VistaHistorica {
  titulo: string | null;
  unidad: string | null;
  tablero: Tablero;
  veredicto: Veredicto;
  cifras_fecha: string;
}

// ── formato ──────────────────────────────────────────────────────────────
function money(n: number): string {
  const neg = n < 0;
  const r = Math.round(Math.abs(n));
  const s = String(r).replace(/\B(?=(\d{3})+(?!\d))/g, ".");
  return (neg ? "-$" : "$") + s;
}
function fmt(v: ValorNumerico | null | undefined): string {
  if (v === null || v === undefined) return "—";
  if (typeof v === "object") return `${money(v.min)} a ${money(v.max)}`;
  return money(v);
}
function medio(v: ValorNumerico | null | undefined): number | null {
  if (v === null || v === undefined) return null;
  return typeof v === "object" ? (v.min + v.max) / 2 : v;
}

const ETIQUETAS_FALTANTES: Record<string, { texto: string; porque: string }> = {
  costo_materiales_unidad: { texto: "Costo de materiales por unidad", porque: "es la base para saber cuánto te cuesta cada una" },
  horas_por_unidad: { texto: "Tu tiempo por unidad, valorado en dinero", porque: "si te pagaras el rato que tardas, el costo real sube" },
  valor_hora: { texto: "Cuánto vale tu hora de trabajo", porque: "sin ella no se puede poner precio a tu tiempo" },
  precio_tentativo: { texto: "El precio al que vendes", porque: "sin precio no hay margen que calcular" },
  capacidad_semanal: { texto: "Cuántas puedes hacer en una semana", porque: "marca el techo real de lo que alcanzas a producir" },
  costos_fijos_mensuales: { texto: "Tu gasto fijo mensual", porque: "es lo que pagas cada mes vendas o no" },
  unidades_vendidas: { texto: "Cuántas vendes al mes, o tu meta", porque: "sin ella no hay escenarios de venta" },
  precio_pagado_real: { texto: "Lo que de verdad te han pagado", porque: "el precio real puede diferir del que pusiste" },
  dias_inventario: { texto: "Días que tu dinero pasa en inventario", porque: "afecta cuándo vuelve la plata a tu bolsillo" },
  dias_cobro_clientes: { texto: "Días que tardas en cobrar", porque: "cobrar tarde aprieta tu caja" },
  dias_pago_proveedores: { texto: "Días que tardas en pagar a proveedores", porque: "pagar más tarde alivia tu caja" },
};

const TONO: Record<Veredicto["tono"], { punto: string; acento: string; borde: string; fondo: string }> = {
  perdida: { punto: "bg-warn", acento: "text-warn", borde: "border-warn/35", fondo: "bg-warn/[0.06]" },
  ajuste: { punto: "bg-done", acento: "text-done", borde: "border-done/30", fondo: "bg-done/[0.06]" },
  sano: { punto: "bg-done", acento: "text-done", borde: "border-done/30", fondo: "bg-done/[0.06]" },
  datos: { punto: "bg-accent", acento: "text-accent", borde: "border-accent/30", fondo: "bg-accent/[0.06]" },
};

function TituloSeccion({ children }: { children: React.ReactNode }) {
  return <div className="mt-10 mb-4 text-[12px] font-semibold uppercase tracking-[1.4px] text-dim">{children}</div>;
}

function FraseConAcento({ frase, acento, clase }: { frase: string; acento: string | null; clase: string }) {
  if (!acento || !frase.includes(acento)) return <>{frase}</>;
  const [antes, despues] = frase.split(acento);
  return (
    <>
      {antes}
      <span className={clase}>{acento}</span>
      {despues}
    </>
  );
}

// ── tiles ────────────────────────────────────────────────────────────────
function Tiles({ t, u }: { t: Tablero; u: string }) {
  const margen = medio(t.margen);
  const claseMargen = margen === null ? "" : margen < 0 ? "text-warn" : "text-done";
  const equi = t.puntoEquilibrio;
  return (
    <div className="grid grid-cols-2 gap-3.5 sm:grid-cols-4">
      <Tile num={fmt(t.costoUnitario)} etq={`te cuesta cada ${u}`} />
      <Tile num={fmt(t.precio)} etq={`precio al que la vendes hoy`} />
      <Tile num={margen !== null && margen >= 0 ? `+${fmt(t.margen)}` : fmt(t.margen)} etq="margen por pieza" clase={claseMargen} />
      <Tile
        num={equi === null ? "No hay" : String(equi)}
        etq="punto de equilibrio"
        clase={equi === null ? "text-warn" : "text-done"}
      />
    </div>
  );
}
function Tile({ num, etq, clase = "" }: { num: string; etq: string; clase?: string }) {
  return (
    <div className="rounded-panel border border-hairline px-6 py-5">
      <div className={`text-[32px] font-extrabold tracking-tight ${clase}`}>{num}</div>
      <div className="mt-2 text-[12.5px] leading-snug text-dim">{etq}</div>
    </div>
  );
}

// ── barra de la verdad ─────────────────────────────────────────────────────
function BarraVerdad({ t }: { t: Tablero }) {
  const costo = fmt(t.costoUnitario);
  const precio = fmt(t.precio);
  const enPerdida = t.barra.enPerdida;
  const filaCosto = (
    <Fila clave="Te cuesta" pct={t.barra.costoPct} texto={costo} clase={enPerdida ? "bg-warn text-black" : "bg-dim/40 text-ink"} />
  );
  const filaPrecio = <Fila clave="Cobras" pct={t.barra.precioPct} texto={precio} clase="bg-done text-black" />;
  return (
    <div className="rounded-panel border border-hairline px-7 py-6">
      {enPerdida ? filaCosto : filaPrecio}
      {enPerdida ? filaPrecio : filaCosto}
      <p className="mt-5 border-t border-hairline pt-4 text-[13px] leading-relaxed text-dim">
        {enPerdida ? (
          <>
            La barra de lo que te cuesta es más larga que la de lo que cobras. Ese pedazo que sobresale es{" "}
            <strong className="font-semibold text-warn">la pérdida que pones de tu bolsillo en cada venta</strong>. Mientras se vea así, vender más
            solo agranda el hueco.
          </>
        ) : (
          <>
            La barra de lo que cobras es la larga, y la de lo que te cuesta no la alcanza. Ese espacio de sobra es{" "}
            <strong className="font-semibold text-done">tu margen</strong>. Aquí, vender más sí te acerca a tu meta.
          </>
        )}
      </p>
    </div>
  );
}
function Fila({ clave, pct, texto, clase }: { clave: string; pct: number | null; texto: string; clase: string }) {
  return (
    <div className="mb-4 grid grid-cols-[76px_1fr] items-center gap-4 last:mb-0">
      <span className="text-right text-[13.5px] text-dim">{clave}</span>
      <div className="relative h-[34px]">
        <div className={`flex h-full items-center rounded-lg px-3.5 text-sm font-bold ${clase}`} style={{ width: `${pct ?? 0}%` }}>
          {texto}
        </div>
      </div>
    </div>
  );
}

// ── palancas ───────────────────────────────────────────────────────────────
function textoPalanca(p: Palanca, u: string): string {
  const margen = p.margenResultante ? fmt(p.margenResultante.valor) : "—";
  const margenPos = p.margenResultante && medio(p.margenResultante.valor) !== null ? `+${margen}` : margen;
  if (p.clave === "volumen") {
    if (p.bloqueada) return p.razonBloqueo ?? "";
    const g = p.gananciaResultante != null ? money(p.gananciaResultante) : "—";
    return `A ${p.meta} ${u}s al mes, tras cubrir tus fijos, te quedan ${g} de ganancia. Es tu palanca más fuerte porque el margen ya es sano.`;
  }
  if (p.clave === "precio") {
    if (p.modo === "test")
      return `Prueba subiendo a ${fmt(p.meta)} (un 10% más): tu margen sube a ${margenPos} por ${u}. Pruébalo con un lote antes de subirlo a todos.`;
    const ventas = p.ventasParaCubrirFijos != null ? `, y cubres tus fijos con unas ${p.ventasParaCubrirFijos} ventas` : "";
    return `A ${fmt(p.meta)} tu margen pasa a ${margenPos} por ${u}${ventas}.`;
  }
  // costo
  if (p.modo === "test")
    return `Prueba bajando el costo a ${fmt(p.meta)} (un 10% menos): te deja ${margenPos} por ${u}, sin tocar el precio.`;
  return `Bajar el costo a ${fmt(p.meta)} te deja ${margenPos} por ${u}, sin tocar el precio.`;
}

function TarjetaPalanca({ p, idx, u }: { p: Palanca; idx: number; u: string }) {
  const nombre = p.clave === "precio" ? "Sube el precio a" : p.clave === "costo" ? "Baja el costo a" : "Vende al mes";
  const desde =
    p.clave === "precio" && p.actual != null
      ? `hoy cobras ${fmt(p.actual)}`
      : p.clave === "costo" && p.actual != null
        ? `hoy te cuesta ${fmt(p.actual)}`
        : null;
  const badge = p.recomendada ? (p.clave === "volumen" ? "tu meta" : "la mas directa") : null;
  if (p.bloqueada) {
    return (
      <div className="flex flex-col gap-3.5 rounded-panel border border-dashed border-hairline p-6">
        <div className="flex h-6 w-6 items-center justify-center rounded-md bg-surface-2 text-[13px] font-bold text-warn">{idx}</div>
        <div className="text-[15px] font-bold leading-snug">Vender mas, por ahora, no</div>
        <p className="text-[13px] leading-relaxed text-dim">
          <strong className="text-warn">Con el margen en rojo, el volumen agranda la pérdida.</strong>{" "}
          Primero arregla el margen con la palanca 1 o 2; cuando esté en verde, aquí te diré cuántas necesitas para tu meta.
        </p>
      </div>
    );
  }
  return (
    <div className={`flex flex-col gap-3.5 rounded-panel border p-6 ${p.recomendada ? "border-accent/40" : "border-hairline"}`}>
      <div className="flex items-center justify-between">
        <div className="flex h-6 w-6 items-center justify-center rounded-md bg-surface-2 text-[13px] font-bold text-accent">{idx}</div>
        {badge && (
          <span className="rounded-full border border-accent/40 px-2.5 py-1 text-[11px] font-semibold text-accent">{badge}</span>
        )}
      </div>
      <div className="text-[15px] font-bold leading-snug">{nombre}</div>
      <div className="text-[32px] font-extrabold tracking-tight">
        {p.clave === "volumen" ? (medio(p.meta) ?? "—") : fmt(p.meta)}{" "}
        <span className="text-[15px] font-semibold text-dim">{p.clave === "volumen" ? u + "s" : `por ${u}`}</span>
      </div>
      {desde && <div className="text-[12.5px] text-dim">{desde}</div>}
      <p className="text-[13px] leading-relaxed">
        <FraseConAcento
          frase={textoPalanca(p, u)}
          acento={
            p.margenResultante && medio(p.margenResultante.valor) !== null && medio(p.margenResultante.valor)! >= 0
              ? `+${fmt(p.margenResultante.valor)} por ${u}`
              : p.gananciaResultante != null
                ? `${money(p.gananciaResultante)} de ganancia`
                : null
          }
          clase="font-bold text-done"
        />
      </p>
    </div>
  );
}

function Palancasseccion({ pal, u }: { pal: Palancas; u: string }) {
  // Orden: recomendada primero (canon: la de la izquierda es la protagonista).
  const orden: Palanca[] = [pal.precio, pal.costo, pal.volumen];
  const titulo =
    pal.estado === "sano" ? "Tres caminos para exprimir estos numeros" : "Tres caminos para que estos numeros funcionen";
  return (
    <>
      <TituloSeccion>{titulo}</TituloSeccion>
      <div className="grid gap-3.5 sm:grid-cols-3">
        {orden.map((p, i) => (
          <TarjetaPalanca key={p.clave} p={p} idx={i + 1} u={u} />
        ))}
      </div>
    </>
  );
}

// ── escenarios ─────────────────────────────────────────────────────────────
function Escenarios({ t }: { t: Tablero }) {
  const filas = t.escenariosFilas;
  if (filas.length === 0) return null;
  return (
    <div className="overflow-hidden rounded-panel border border-hairline">
      <div className="grid grid-cols-[1fr_120px] gap-4 bg-surface px-6 py-3 text-[11.5px] font-semibold uppercase tracking-wider text-dim">
        <span>Escenario</span>
        <span className="text-right">Ganancia</span>
      </div>
      {filas.map((f) => (
        <div key={f.nombre} className="grid grid-cols-[1fr_120px] items-center gap-4 border-t border-hairline px-6 py-4">
          <div className="text-sm font-semibold">
            {f.nombre}
            <span className="block text-[12px] font-normal text-dim">{f.sub}</span>
          </div>
          <div className={`text-right text-[15px] font-bold ${f.ganancia != null && f.ganancia < 0 ? "text-warn" : f.ganancia != null && f.ganancia > 0 ? "text-done" : ""}`}>
            {f.ganancia != null ? money(f.ganancia) : "—"}
          </div>
        </div>
      ))}
    </div>
  );
}

// ── faltantes ────────────────────────────────────────────────────────────
// En el PRESENTE cada item es la PUERTA: un boton que abre el recolector en su
// campo. En una version HISTORICA (soloLectura, onCorregir ausente) son display
// plano: el pasado se visita, no se edita.
function Faltantes({ t, onCorregir }: { t: Tablero; onCorregir?: (campo: string) => void }) {
  return (
    <div className="rounded-panel border border-hairline px-6 py-5">
      {t.faltantes.map((campo) => {
        const e = ETIQUETAS_FALTANTES[campo] ?? { texto: campo, porque: "" };
        const cuerpo = (
          <>
            <span
              className={
                "mt-0.5 flex h-5 w-5 flex-none items-center justify-center rounded-md border-[1.5px] text-[14px] leading-none " +
                (onCorregir ? "border-accent/55 text-accent transition group-hover:border-accent group-hover:bg-accent/10" : "border-hairline text-transparent")
              }
            >
              +
            </span>
            <div className="min-w-0">
              <div className={"text-sm leading-snug" + (onCorregir ? " transition group-hover:text-accent" : "")}>{e.texto}</div>
              {e.porque && <div className="mt-0.5 text-[12.5px] leading-snug text-dim">{e.porque}</div>}
            </div>
            {onCorregir && (
              <span className="ml-auto self-center whitespace-nowrap text-[12px] text-accent opacity-0 transition group-hover:opacity-100">
                Añadir →
              </span>
            )}
          </>
        );
        return onCorregir ? (
          <button key={campo} onClick={() => onCorregir(campo)} className="group flex w-full items-start gap-3.5 border-b border-hairline py-3 text-left last:border-b-0">
            {cuerpo}
          </button>
        ) : (
          <div key={campo} className="flex items-start gap-3.5 border-b border-hairline py-3 last:border-b-0">
            {cuerpo}
          </div>
        );
      })}
      {t.faltantes.length === 0 && <div className="py-2 text-sm text-dim">Tienes todo lo esencial. Buen trabajo.</div>}
      {/* La ley del fundador, en pantalla (solo en el presente: en el pasado no se edita). */}
      {onCorregir && (
        <p className="mt-3 border-t border-hairline pt-3 text-[12px] leading-relaxed text-dim">
          Añadir o corregir cifras es gratis, siempre: tu tablero se recalcula al momento.
        </p>
      )}
    </div>
  );
}

// ── piezas compartidas entre el PRESENTE y una version HISTORICA ─────────────
function VeredictoBloque({ v }: { v: Veredicto }) {
  const tono = TONO[v.tono];
  return (
    <div className={`mt-5 flex items-start gap-3.5 rounded-panel border px-6 py-5 ${tono.borde} ${tono.fondo}`}>
      <span className={`mt-1.5 h-2.5 w-2.5 flex-none rounded-full ${tono.punto}`} />
      <p className="text-[17px] font-semibold leading-normal">
        <FraseConAcento frase={v.frase} acento={v.acento} clase={tono.acento} />
      </p>
    </div>
  );
}

/** El cuerpo del tablero (tiles -> guardian). En el presente los faltantes son
 * la puerta (onCorregir); en una version historica, display plano. */
function RestoTablero({ t, u, onCorregir }: { t: Tablero; u: string; onCorregir?: (campo: string) => void }) {
  return (
    <>
      <TituloSeccion>De un vistazo</TituloSeccion>
      <Tiles t={t} u={u} />
      <TituloSeccion>La barra de la verdad</TituloSeccion>
      <BarraVerdad t={t} />
      <Palancasseccion pal={t.palancas} u={u} />
      <div className="mt-10 grid gap-3.5 lg:grid-cols-[1.3fr_1fr]">
        <div>
          <TituloSeccion>Escenarios, a tu precio de hoy</TituloSeccion>
          <Escenarios t={t} />
        </div>
        <div>
          <TituloSeccion>Los números que te faltan</TituloSeccion>
          <Faltantes t={t} onCorregir={onCorregir} />
        </div>
      </div>
      {t.cicloDias !== null && (
        <>
          <TituloSeccion>Tu ciclo de caja</TituloSeccion>
          <div className="rounded-panel border border-hairline bg-surface px-6 py-5">
            <div className="text-[28px] font-extrabold tracking-tight">
              {t.cicloDias} <span className="text-[15px] font-semibold text-dim">días</span>
            </div>
            <p className="mt-2 text-[14px] leading-relaxed text-dim [text-wrap:pretty]">{fraseCicloCaja(t.cicloDias)}</p>
          </div>
        </>
      )}
      <div className="mt-4 flex gap-3.5 rounded-panel border border-warn/30 bg-warn/[0.06] px-6 py-5">
        <span className="mt-0.5 flex-none text-warn" aria-hidden>
          ⚠
        </span>
        <p className="text-[13.5px] leading-relaxed text-warn/90">
          <strong className="font-semibold text-warn">Guardián de datos.</strong>{" "}
          {t.gigo.inconsistente
            ? t.gigo.motivo
            : "Estos números valen exactamente lo que valen las cifras que metiste. Cuando agregues las que faltan, el número real puede cambiar. No sustituye contabilidad formal ni asesoría fiscal."}
        </p>
      </div>
    </>
  );
}

const ETIQUETA_TONO: Record<Veredicto["tono"], string> = {
  perdida: "pérdida",
  ajuste: "margen delgado",
  sano: "sano",
  datos: "faltan datos",
};

function margenLista(v: ValorNumerico | null): { texto: string; clase: string } {
  const m = medio(v);
  if (m === null) return { texto: "—", clase: "text-dim" };
  return { texto: m >= 0 ? `+${fmt(v)}` : fmt(v), clase: m < 0 ? "text-warn" : "text-done" };
}

/** "Versiones anteriores": SOLO las pasadas (la vigente vive arriba). El
 * diferenciador de la fila es el contenido (veredicto + margen); la hora solo
 * aparece para desambiguar gemelas del mismo día. El pasado se visita. */
function VersionesAnteriores({ versiones, onVer }: { versiones: VersionResumen[]; onVer: (id: string) => void }) {
  const pasadas = versiones.filter((v) => !v.vigente);
  if (pasadas.length === 0) return null;
  const ahora = new Date();
  const clave = (iso: string) => new Date(iso).toDateString();
  const porDia = new Map<string, number>();
  for (const v of versiones) porDia.set(clave(v.fecha), (porDia.get(clave(v.fecha)) ?? 0) + 1);
  return (
    <>
      <TituloSeccion>Versiones anteriores</TituloSeccion>
      <div className="rounded-panel border border-hairline">
        {pasadas.map((v) => {
          const conHora = (porDia.get(clave(v.fecha)) ?? 0) > 1;
          const mg = margenLista(v.margen);
          const punto = v.tono ? TONO[v.tono].punto : "bg-dim";
          return (
            <button
              key={v.id}
              onClick={() => onVer(v.id)}
              className="group flex w-full items-center gap-4 border-b border-hairline px-6 py-4 text-left last:border-b-0 hover:bg-surface-2"
            >
              <span className="text-[14px] font-semibold group-hover:text-accent">{selloVersion(v.fecha, ahora, conHora)}</span>
              <span className={`h-2 w-2 flex-none rounded-full ${punto}`} aria-hidden />
              <span className="text-[13px] text-dim">{v.tono ? ETIQUETA_TONO[v.tono] : "—"}</span>
              <span className={`ml-auto text-[14px] font-semibold ${mg.clase}`}>{mg.texto}</span>
              <span className="whitespace-nowrap text-[12px] text-accent opacity-0 transition group-hover:opacity-100">Ver →</span>
            </button>
          );
        })}
      </div>
    </>
  );
}

// ── pantalla ───────────────────────────────────────────────────────────────
export function TusNumeros({ projectId }: { projectId: string }) {
  const [data, setData] = useState<RespuestaNumeros | null>(null);
  const [error, setError] = useState<string | null>(null);
  const [editando, setEditando] = useState(false);
  /** ETAPA 2: la compuerta de activación (2 créditos, una vez por idea). */
  const [activando, setActivando] = useState(false);
  const [errorCompuerta, setErrorCompuerta] = useState<string | null>(null);
  /** La puerta de un faltante: abre el recolector con foco en ese campo. */
  const [campoInicial, setCampoInicial] = useState<string | null>(null);
  /** Una version PASADA que se esta visitando en modo lectura (null = el presente). */
  const [historico, setHistorico] = useState<VistaHistorica | null>(null);
  const abrirRecolector = (campo: string | null = null) => {
    setCampoInicial(campo);
    setEditando(true);
  };

  useEffect(() => {
    let vivo = true;
    fetch(`/api/project/${projectId}/numeros`)
      .then((r) => (r.ok ? r.json() : Promise.reject(new Error("no pudimos cargar tus numeros"))))
      .then((d: RespuestaNumeros) => vivo && setData(d))
      .catch((e) => vivo && setError(e.message));
    return () => {
      vivo = false;
    };
  }, [projectId]);

  async function verVersion(id: string) {
    const r = await fetch(`/api/project/${projectId}/numeros?version=${id}`);
    if (r.ok) {
      setHistorico((await r.json()) as VistaHistorica);
      if (typeof window !== "undefined") window.scrollTo({ top: 0, behavior: "smooth" });
    }
  }
  const volverAHoy = () => {
    setHistorico(null);
    if (typeof window !== "undefined") window.scrollTo({ top: 0, behavior: "smooth" });
  };

  if (error) return <div className="mx-auto max-w-2xl px-6 py-16 text-dim">{error}</div>;
  if (!data) return <div className="mx-auto max-w-2xl px-6 py-16 text-dim">Calculando tus números…</div>;

  // ETAPA 2 — LA COMPUERTA (canon 07): sin activación no hay tablero. Activar
  // cuesta 2 créditos, UNA vez por idea; después todo recálculo es gratis.
  if (data.compuerta) {
    return (
      <div className="min-h-full">
        <nav className="flex items-center justify-between gap-6 border-b border-hairline px-8 py-4">
          <div className="flex min-w-0 items-baseline gap-3">
            <Link href="/ideas" className="flex-none text-sm text-dim hover:text-accent">
              Mis ideas /
            </Link>
            <span className="truncate text-[15px] font-bold">{data.titulo ?? "Tu idea"}</span>
          </div>
        </nav>
        <div className="mx-auto w-full max-w-xl px-6 py-16">
          <Link href={`/idea/${projectId}`} className="mb-6 inline-block text-sm text-dim hover:text-accent">
            ← Volver al plan
          </Link>
          <div className="rounded-panel border border-accent/35 bg-surface p-8">
            <p className="text-[11px] font-semibold uppercase tracking-[1.3px] text-accent">Tus Números</p>
            <h1 className="mt-2 text-2xl font-bold tracking-tight">Tus cifras reales, convertidas en decisiones</h1>
            <p className="mt-3 text-[14.5px] leading-relaxed text-dim">
              Margen, punto de equilibrio, tres palancas calculadas y escenarios, sobre las cifras que tú declares. Se
              activa una vez por idea; después, corregir cifras y recalcular es gratis, siempre.
            </p>
            <button
              onClick={async () => {
                setError(null);
                setActivando(true);
                try {
                  const r = await fetch(`/api/project/${projectId}/numeros`, {
                    method: "POST",
                    headers: { "Content-Type": "application/json" },
                    body: JSON.stringify({ activar: true }),
                  });
                  const payload = (await r.json()) as RespuestaNumeros & { error?: string; login_requerido?: boolean };
                  if (r.status === 401 && payload.login_requerido) {
                    window.location.assign("/login");
                    return;
                  }
                  if (!r.ok) {
                    setErrorCompuerta(payload.error ?? "no pudimos activar Tus Números; intenta de nuevo");
                    return;
                  }
                  setData(payload);
                } catch {
                  setErrorCompuerta("no pudimos conectar; revisa tu internet e intenta de nuevo");
                } finally {
                  setActivando(false);
                }
              }}
              disabled={activando}
              className="mt-6 rounded-[10px] bg-accent px-6 py-3 text-sm font-semibold text-white hover:opacity-90 disabled:opacity-50"
            >
              {activando ? "Activando…" : `Sacar mis números · ${data.costo ?? 2} créditos`}
            </button>
            {errorCompuerta && <p className="mt-3 text-[13px] text-warn">{errorCompuerta}</p>}
          </div>
        </div>
      </div>
    );
  }

  const u = (historico ?? data).unidad || "unidad";
  const titulo = (historico ?? data).titulo;

  const cabecera = (
    <nav className="flex items-center justify-between gap-6 border-b border-hairline px-8 py-4">
      <div className="flex min-w-0 items-baseline gap-3">
        <Link href="/ideas" className="flex-none text-sm text-dim hover:text-accent">
          Mis ideas /
        </Link>
        <span className="truncate text-[15px] font-bold">{titulo ?? "Tu idea"}</span>
      </div>
      <span className="flex-none rounded-full border border-accent/40 px-3 py-1.5 text-[12.5px] font-semibold text-accent">
        Tus Números · 2 créditos
      </span>
    </nav>
  );

  // ── MODO LECTURA: visitar una version pasada. El pasado se visita, no se
  //    edita: sin "Corregir", sin faltantes tocables, con la banda que dice
  //    el momento absoluto (el acta consta en absoluto). ──
  if (historico) {
    return (
      <div className="min-h-full">
        {cabecera}
        <div className="mx-auto w-full max-w-[1060px] px-10 pb-16 pt-8">
          <div className="mb-6 flex flex-wrap items-center justify-between gap-3 rounded-panel border border-accent/40 bg-accent/[0.06] px-6 py-4">
            <p className="text-[14px] font-semibold text-accent">
              Estás viendo tus números del {momentoAbsoluto(historico.cifras_fecha)}
            </p>
            <button
              onClick={volverAHoy}
              className="rounded-cinta bg-accent px-4 py-2 text-[13px] font-medium text-white hover:opacity-90"
            >
              Volver a hoy
            </button>
          </div>
          <h1 className="text-[32px] font-bold leading-tight tracking-tight">
            Los números de {titulo ? titulo.toLowerCase() : "tu idea"}
          </h1>
          <VeredictoBloque v={historico.veredicto} />
          <RestoTablero t={historico.tablero} u={u} />
        </div>
      </div>
    );
  }

  // ── EL PRESENTE: se habita. Aqui se corrige y se recalcula. ──
  const t = data.tablero;
  const v = data.veredicto;
  const reciente = data.cifras_fecha ? new Date().getTime() - new Date(data.cifras_fecha).getTime() < 120_000 : false;
  const selloHoy = data.cifras_fecha ? (reciente ? "recién actualizado" : fechaSello(data.cifras_fecha)) : null;

  return (
    <div className="min-h-full">
      {cabecera}

      <div className="mx-auto w-full max-w-[1060px] px-10 pb-16 pt-8" data-screen-label="Tus Numeros vista">
        <Link href={`/idea/${projectId}`} className="mb-6 inline-block text-sm text-dim hover:text-accent">
          ← Volver al plan
        </Link>

        <div className="mb-3.5 flex items-center gap-2 text-[12px] font-semibold uppercase tracking-[1.3px] text-dim">
          Calculado por código, sobre tus cifras
        </div>
        <h1 className="text-[32px] font-bold leading-tight tracking-tight">
          Los números de {titulo ? titulo.toLowerCase() : "tu idea"}
        </h1>

        <VeredictoBloque v={v} />

        <div className="mt-4 flex flex-wrap items-center gap-x-2 gap-y-1 text-[13px] text-dim">
          <span className="font-semibold text-ink">Tus números de HOY</span>
          {selloHoy && <span>· calculado con tus cifras del {selloHoy}</span>}
          {!editando && (
            <button onClick={() => abrirRecolector(null)} className="ml-1 font-medium text-accent hover:underline">
              Corregir mis cifras · gratis
            </button>
          )}
        </div>

        {editando && (
          <div className="mt-4">
            <CorregirCifras
              projectId={projectId}
              unidad={u}
              declaradas={data.numeros_declarados}
              campoInicial={campoInicial}
              onGuardado={(payload) => {
                setData(payload as RespuestaNumeros);
                setEditando(false);
                setCampoInicial(null);
              }}
              onCancelar={() => {
                setEditando(false);
                setCampoInicial(null);
              }}
            />
          </div>
        )}

        <RestoTablero t={t} u={u} onCorregir={(campo) => abrirRecolector(campo)} />

        <VersionesAnteriores versiones={data.historial ?? []} onVer={verVersion} />
      </div>
    </div>
  );
}
