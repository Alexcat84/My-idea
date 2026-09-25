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
import { loginConNext } from "@/lib/nextSeguro";
import { fraseCicloCaja, type Veredicto } from "@/lib/numerosVivo";
import { fechaSello, momentoAbsoluto, selloVersion } from "@/lib/fechas";
import { CorregirCifras } from "@/app/ui/CorregirCifras";
import { elegir, LOCALE_BASE, type Locale } from "@/lib/i18n/config";
import { useIdioma } from "@/lib/i18n/IdiomaProvider";
import { interpolar } from "@/lib/i18n/interpolar";
import { rico } from "@/lib/i18n/rico";
import { dinero } from "@/lib/i18n/formato";
import { TUS_NUMEROS } from "@/lib/i18n/mensajes/tusNumeros";

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
// El dinero sale de formato.ts (idéntico en español al money() de antes).
function fmt(v: ValorNumerico | null | undefined, idioma: Locale): string {
  if (v === null || v === undefined) return "—";
  if (typeof v === "object")
    return interpolar(elegir(TUS_NUMEROS, idioma).rango, { min: dinero(idioma, v.min), max: dinero(idioma, v.max) });
  return dinero(idioma, v);
}
function medio(v: ValorNumerico | null | undefined): number | null {
  if (v === null || v === undefined) return null;
  return typeof v === "object" ? (v.min + v.max) / 2 : v;
}

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
  const idioma = useIdioma();
  const tx = elegir(TUS_NUMEROS, idioma).tiles;
  const margen = medio(t.margen);
  const claseMargen = margen === null ? "" : margen < 0 ? "text-warn" : "text-done";
  const equi = t.puntoEquilibrio;
  return (
    <div className="grid grid-cols-2 gap-3.5 sm:grid-cols-4">
      <Tile num={fmt(t.costoUnitario, idioma)} etq={interpolar(tx.teCuestaCada, { u })} />
      <Tile num={fmt(t.precio, idioma)} etq={tx.precioHoy} />
      <Tile
        num={margen !== null && margen >= 0 ? `+${fmt(t.margen, idioma)}` : fmt(t.margen, idioma)}
        etq={tx.margenPorPieza}
        clase={claseMargen}
      />
      <Tile
        num={equi === null ? tx.noHay : String(equi)}
        etq={tx.puntoEquilibrio}
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
  const idioma = useIdioma();
  const tx = elegir(TUS_NUMEROS, idioma).barra;
  const costo = fmt(t.costoUnitario, idioma);
  const precio = fmt(t.precio, idioma);
  const enPerdida = t.barra.enPerdida;
  const filaCosto = (
    <Fila clave={tx.teCuesta} pct={t.barra.costoPct} texto={costo} clase={enPerdida ? "bg-warn text-black" : "bg-dim/40 text-ink"} />
  );
  const filaPrecio = <Fila clave={tx.cobras} pct={t.barra.precioPct} texto={precio} clase="bg-done text-black" />;
  return (
    <div className="rounded-panel border border-hairline px-7 py-6">
      {enPerdida ? filaCosto : filaPrecio}
      {enPerdida ? filaPrecio : filaCosto}
      <p className="mt-5 border-t border-hairline pt-4 text-[13px] leading-relaxed text-dim">
        {enPerdida
          ? rico(tx.enPerdida, { b: (c) => <strong className="font-semibold text-warn">{c}</strong> })
          : rico(tx.conMargen, { b: (c) => <strong className="font-semibold text-done">{c}</strong> })}
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
/** Plural de la unidad de venta en el idioma de la frase. Español (AUD-09 H12):
 * vocal + s, z -> ces, consonante + es; en una unidad de varias palabras ("kit de velas")
 * se pluraliza la primera. i18n F3: inglés, portugués, francés e
 * italiano con su regla regular; alemán, japonés, chino, coreano, árabe e hindi
 * dejan la unidad tal cual (sin plural regular: mejor sin plural que inventado). */
export function pluralDe(unidad: string, idioma: Locale = LOCALE_BASE): string {
  const palabras = unidad.trim().split(" ");
  if (!palabras[0]) return unidad;
  const regla = REGLA_PLURAL[idioma];
  if (!regla) return unidad;
  // En inglés el núcleo es la última palabra ("candle kit"), salvo con "of"
  // ("cup of coffee"); en las lenguas romances, la primera ("caja de velas").
  const i = idioma === "en" && !palabras.includes("of") ? palabras.length - 1 : 0;
  palabras[i] = regla(palabras[i]);
  return palabras.join(" ");
}

const REGLA_PLURAL: Record<Locale, ((p: string) => string) | null> = {
  es: (p) => (/[aeiouáéíóú]$/i.test(p) ? `${p}s` : /z$/i.test(p) ? `${p.slice(0, -1)}ces` : /s$/i.test(p) ? p : `${p}es`),
  en: (p) =>
    /(ss|x|z|ch|sh)$/i.test(p) ? `${p}es` : /[^aeiou]y$/i.test(p) ? `${p.slice(0, -1)}ies` : /s$/i.test(p) ? p : `${p}s`,
  pt: (p) =>
    /ão$/i.test(p)
      ? `${p.slice(0, -2)}ões`
      : /m$/i.test(p)
        ? `${p.slice(0, -1)}ns`
        : /[aeou]l$/i.test(p)
          ? `${p.slice(0, -1)}is`
          : /[rz]$/i.test(p)
            ? `${p}es`
            : /s$/i.test(p)
              ? p
              : `${p}s`,
  fr: (p) => (/[sxz]$/i.test(p) ? p : /(eau|au|eu)$/i.test(p) ? `${p}x` : /al$/i.test(p) ? `${p.slice(0, -2)}aux` : `${p}s`),
  it: (p) =>
    /[cg]a$/i.test(p)
      ? `${p.slice(0, -1)}he`
      : /a$/i.test(p)
        ? `${p.slice(0, -1)}e`
        : /[oe]$/i.test(p)
          ? `${p.slice(0, -1)}i`
          : p,
  de: null,
  ja: null,
  zh: null,
  ko: null,
  ar: null,
  hi: null,
};

export function textoPalanca(p: Palanca, u: string, idioma: Locale = LOCALE_BASE): string {
  const tx = elegir(TUS_NUMEROS, idioma).palanca;
  const margen = p.margenResultante ? fmt(p.margenResultante.valor, idioma) : "—";
  const margenPos = p.margenResultante && medio(p.margenResultante.valor) !== null ? `+${margen}` : margen;
  if (p.clave === "volumen") {
    if (p.bloqueada) return p.razonBloqueo ?? "";
    // AUD-09 H12: una cifra que no existe no se escribe ("A null", "— de
    // ganancia"), y el plural es español ("unidades", no "unidads").
    const cierre = tx.cierreVolumen;
    if (p.meta == null) {
      return interpolar(tx.volumenSinMeta, { cierre });
    }
    const unidades = `${p.meta} ${pluralDe(u, idioma)}`;
    if (p.gananciaResultante == null) {
      return interpolar(tx.volumenSinGanancia, { unidades, cierre });
    }
    return interpolar(tx.volumenConGanancia, { unidades, ganancia: dinero(idioma, p.gananciaResultante), cierre });
  }
  const meta = fmt(p.meta, idioma);
  if (p.clave === "precio") {
    if (p.modo === "test") return interpolar(tx.precioTest, { meta, margen: margenPos, u });
    const ventas = p.ventasParaCubrirFijos != null ? interpolar(tx.precioVentas, { n: p.ventasParaCubrirFijos }) : "";
    return interpolar(tx.precioArreglo, { meta, margen: margenPos, u, ventas });
  }
  // costo
  if (p.modo === "test") return interpolar(tx.costoTest, { meta, margen: margenPos, u });
  return interpolar(tx.costoArreglo, { meta, margen: margenPos, u });
}

function TarjetaPalanca({ p, idx, u }: { p: Palanca; idx: number; u: string }) {
  const idioma = useIdioma();
  const tx = elegir(TUS_NUMEROS, idioma).palanca;
  const nombre = p.clave === "precio" ? tx.nombrePrecio : p.clave === "costo" ? tx.nombreCosto : tx.nombreVolumen;
  const desde =
    p.clave === "precio" && p.actual != null
      ? interpolar(tx.hoyCobras, { v: fmt(p.actual, idioma) })
      : p.clave === "costo" && p.actual != null
        ? interpolar(tx.hoyTeCuesta, { v: fmt(p.actual, idioma) })
        : null;
  const badge = p.recomendada ? (p.clave === "volumen" ? tx.badgeMeta : tx.badgeDirecta) : null;
  if (p.bloqueada) {
    return (
      <div className="flex flex-col gap-3.5 rounded-panel border border-dashed border-hairline p-6">
        <div className="flex h-6 w-6 items-center justify-center rounded-md bg-surface-2 text-[13px] font-bold text-warn">{idx}</div>
        <div className="text-[15px] font-bold leading-snug">{tx.bloqueadaTitulo}</div>
        <p className="text-[13px] leading-relaxed text-dim">
          {rico(tx.bloqueadaTexto, { b: (c) => <strong className="text-warn">{c}</strong> })}
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
        {p.clave === "volumen" ? (medio(p.meta) ?? "—") : fmt(p.meta, idioma)}{" "}
        <span className="text-[15px] font-semibold text-dim">
          {p.clave === "volumen" ? interpolar(tx.unidadesSufijo, { u }) : interpolar(tx.porUnidad, { u })}
        </span>
      </div>
      {desde && <div className="text-[12.5px] text-dim">{desde}</div>}
      <p className="text-[13px] leading-relaxed">
        <FraseConAcento
          frase={textoPalanca(p, u, idioma)}
          acento={
            p.margenResultante && medio(p.margenResultante.valor) !== null && medio(p.margenResultante.valor)! >= 0
              ? interpolar(tx.acentoMargen, { margen: `+${fmt(p.margenResultante.valor, idioma)}`, u })
              : p.gananciaResultante != null
                ? interpolar(tx.acentoGanancia, { ganancia: dinero(idioma, p.gananciaResultante) })
                : null
          }
          clase="font-bold text-done"
        />
      </p>
    </div>
  );
}

function Palancasseccion({ pal, u }: { pal: Palancas; u: string }) {
  const tx = elegir(TUS_NUMEROS, useIdioma()).palanca;
  // Orden: recomendada primero (canon: la de la izquierda es la protagonista).
  const orden: Palanca[] = [pal.precio, pal.costo, pal.volumen];
  const titulo = pal.estado === "sano" ? tx.tituloSano : tx.tituloArreglo;
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
  const idioma = useIdioma();
  const tx = elegir(TUS_NUMEROS, idioma).escenarios;
  const filas = t.escenariosFilas;
  if (filas.length === 0) return null;
  return (
    <div className="overflow-hidden rounded-panel border border-hairline">
      <div className="grid grid-cols-[1fr_120px] gap-4 bg-surface px-6 py-3 text-[11.5px] font-semibold uppercase tracking-wider text-dim">
        <span>{tx.escenario}</span>
        <span className="text-right">{tx.ganancia}</span>
      </div>
      {filas.map((f) => (
        <div key={f.nombre} className="grid grid-cols-[1fr_120px] items-center gap-4 border-t border-hairline px-6 py-4">
          <div className="text-sm font-semibold">
            {f.nombre}
            <span className="block text-[12px] font-normal text-dim">{f.sub}</span>
          </div>
          <div className={`text-right text-[15px] font-bold ${f.ganancia != null && f.ganancia < 0 ? "text-warn" : f.ganancia != null && f.ganancia > 0 ? "text-done" : ""}`}>
            {f.ganancia != null ? (
              dinero(idioma, f.ganancia)
            ) : f.sinCifra ? (
              // AUD-09 M43: sin fijos no hay ganancia neta: se dice qué falta.
              <span className="text-[12px] font-normal text-dim">{f.sinCifra}</span>
            ) : (
              "—"
            )}
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
  const tx = elegir(TUS_NUMEROS, useIdioma());
  const etiquetas: Record<string, { texto: string; porque: string }> = tx.faltantes;
  return (
    <div className="rounded-panel border border-hairline px-6 py-5">
      {t.faltantes.map((campo) => {
        const e = etiquetas[campo] ?? { texto: campo, porque: "" };
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
                {tx.anadir}
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
      {t.faltantes.length === 0 && <div className="py-2 text-sm text-dim">{tx.todoLoEsencial}</div>}
      {/* La ley del fundador, en pantalla (solo en el presente: en el pasado no se edita). */}
      {onCorregir && (
        <p className="mt-3 border-t border-hairline pt-3 text-[12px] leading-relaxed text-dim">{tx.leyGratis}</p>
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
  const idioma = useIdioma();
  const tx = elegir(TUS_NUMEROS, idioma);
  return (
    <>
      <TituloSeccion>{tx.secciones.deUnVistazo}</TituloSeccion>
      <Tiles t={t} u={u} />
      <TituloSeccion>{tx.secciones.barraDeLaVerdad}</TituloSeccion>
      <BarraVerdad t={t} />
      <Palancasseccion pal={t.palancas} u={u} />
      <div className="mt-10 grid gap-3.5 lg:grid-cols-[1.3fr_1fr]">
        <div>
          <TituloSeccion>{tx.secciones.escenarios}</TituloSeccion>
          <Escenarios t={t} />
        </div>
        <div>
          <TituloSeccion>{tx.secciones.faltantes}</TituloSeccion>
          <Faltantes t={t} onCorregir={onCorregir} />
        </div>
      </div>
      {t.cicloDias !== null && (
        <>
          <TituloSeccion>{tx.secciones.cicloDeCaja}</TituloSeccion>
          <div className="rounded-panel border border-hairline bg-surface px-6 py-5">
            <div className="text-[28px] font-extrabold tracking-tight">
              {t.cicloDias} <span className="text-[15px] font-semibold text-dim">{tx.dias}</span>
            </div>
            <p className="mt-2 text-[14px] leading-relaxed text-dim [text-wrap:pretty]">{fraseCicloCaja(t.cicloDias, idioma)}</p>
          </div>
        </>
      )}
      <div className="mt-4 flex gap-3.5 rounded-panel border border-warn/30 bg-warn/[0.06] px-6 py-5">
        <span className="mt-0.5 flex-none text-warn" aria-hidden>
          ⚠
        </span>
        <p className="text-[13.5px] leading-relaxed text-warn/90">
          <strong className="font-semibold text-warn">{tx.guardianTitulo}</strong>{" "}
          {t.gigo.inconsistente ? t.gigo.motivo : tx.guardianTexto}
        </p>
      </div>
    </>
  );
}

function margenLista(v: ValorNumerico | null, idioma: Locale): { texto: string; clase: string } {
  const m = medio(v);
  if (m === null) return { texto: "—", clase: "text-dim" };
  return { texto: m >= 0 ? `+${fmt(v, idioma)}` : fmt(v, idioma), clase: m < 0 ? "text-warn" : "text-done" };
}

/** "Versiones anteriores": SOLO las pasadas (la vigente vive arriba). El
 * diferenciador de la fila es el contenido (veredicto + margen); la hora solo
 * aparece para desambiguar gemelas del mismo día. El pasado se visita. */
function VersionesAnteriores({ versiones, onVer }: { versiones: VersionResumen[]; onVer: (id: string) => void }) {
  const idioma = useIdioma();
  const tx = elegir(TUS_NUMEROS, idioma);
  const pasadas = versiones.filter((v) => !v.vigente);
  if (pasadas.length === 0) return null;
  const ahora = new Date();
  const clave = (iso: string) => new Date(iso).toDateString();
  const porDia = new Map<string, number>();
  for (const v of versiones) porDia.set(clave(v.fecha), (porDia.get(clave(v.fecha)) ?? 0) + 1);
  return (
    <>
      <TituloSeccion>{tx.secciones.versionesAnteriores}</TituloSeccion>
      <div className="rounded-panel border border-hairline">
        {pasadas.map((v) => {
          const conHora = (porDia.get(clave(v.fecha)) ?? 0) > 1;
          const mg = margenLista(v.margen, idioma);
          const punto = v.tono ? TONO[v.tono].punto : "bg-dim";
          return (
            <button
              key={v.id}
              onClick={() => onVer(v.id)}
              className="group flex w-full items-center gap-4 border-b border-hairline px-6 py-4 text-left last:border-b-0 hover:bg-surface-2"
            >
              <span className="text-[14px] font-semibold group-hover:text-accent">{selloVersion(v.fecha, ahora, conHora, idioma)}</span>
              <span className={`h-2 w-2 flex-none rounded-full ${punto}`} aria-hidden />
              <span className="text-[13px] text-dim">{v.tono ? tx.tonos[v.tono] : "—"}</span>
              <span className={`ml-auto text-[14px] font-semibold ${mg.clase}`}>{mg.texto}</span>
              <span className="whitespace-nowrap text-[12px] text-accent opacity-0 transition group-hover:opacity-100">{tx.ver}</span>
            </button>
          );
        })}
      </div>
    </>
  );
}

// ── pantalla ───────────────────────────────────────────────────────────────
export function TusNumeros({ projectId }: { projectId: string }) {
  const idioma = useIdioma();
  const tx = elegir(TUS_NUMEROS, idioma);
  const [data, setData] = useState<RespuestaNumeros | null>(null);
  const [error, setError] = useState<string | null>(null);
  const [editando, setEditando] = useState(false);
  /** La compuerta de activación (incluida con el plan, una vez por idea). */
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
      .then((r) => (r.ok ? r.json() : Promise.reject(new Error(tx.errorCargar))))
      .then((d: RespuestaNumeros) => vivo && setData(d))
      .catch((e) => vivo && setError(e.message));
    return () => {
      vivo = false;
    };
  }, [projectId, tx.errorCargar]);

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
  if (!data) return <div className="mx-auto max-w-2xl px-6 py-16 text-dim">{tx.calculando}</div>;

  // Catálogo congruente (§4): sin activación no hay tablero. Tus Números va
  // INCLUIDO en el plan: activar no cuesta, pero sigue siendo UNA vez por idea
  // (ancla activado_at). Si `data.costo` llegara > 0, el botón vuelve a mostrar
  // el precio; con 0 muestra "incluido con tu plan".
  if (data.compuerta) {
    return (
      <div className="min-h-full">
        <nav className="flex items-center justify-between gap-6 border-b border-hairline px-8 py-4">
          <div className="flex min-w-0 items-baseline gap-3">
            <Link href="/ideas" className="flex-none text-sm text-dim hover:text-accent">
              {tx.misIdeas}
            </Link>
            <span className="truncate text-[15px] font-bold">{data.titulo ?? tx.tuIdea}</span>
          </div>
        </nav>
        <div className="mx-auto w-full max-w-xl px-6 py-16">
          <Link href={`/idea/${projectId}`} className="mb-6 inline-block text-sm text-dim hover:text-accent">
            {tx.volverAlPlan}
          </Link>
          <div className="rounded-panel border border-accent/35 bg-surface p-8">
            <p className="text-[11px] font-semibold uppercase tracking-[1.3px] text-accent">{tx.compuerta.eyebrow}</p>
            <h1 className="mt-2 text-2xl font-bold tracking-tight">{tx.compuerta.titulo}</h1>
            <p className="mt-3 text-[14.5px] leading-relaxed text-dim">{tx.compuerta.texto}</p>
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
                    // Al volver, reanuda en Manos (donde vive Tus Números).
                    window.location.assign(loginConNext(`/idea/${projectId}?vista=manos`));
                    return;
                  }
                  if (!r.ok) {
                    setErrorCompuerta(payload.error ?? tx.compuerta.errorActivar);
                    return;
                  }
                  setData(payload);
                } catch {
                  setErrorCompuerta(tx.compuerta.errorConectar);
                } finally {
                  setActivando(false);
                }
              }}
              disabled={activando}
              className="mt-6 rounded-[10px] border border-accent/40 bg-accent/10 px-6 py-3 text-sm font-semibold text-accent hover:bg-accent/20 disabled:opacity-50"
            >
              {activando
                ? tx.compuerta.activando
                : (data.costo ?? 0) > 0
                  ? interpolar(tx.compuerta.sacarConCosto, { n: String(data.costo) })
                  : tx.compuerta.activarIncluido}
            </button>
            {errorCompuerta && <p className="mt-3 text-[13px] text-warn">{errorCompuerta}</p>}
          </div>
        </div>
      </div>
    );
  }

  const u = (historico ?? data).unidad || tx.unidadPorDefecto;
  const titulo = (historico ?? data).titulo;

  const cabecera = (
    <nav className="flex items-center justify-between gap-6 border-b border-hairline px-8 py-4">
      <div className="flex min-w-0 items-baseline gap-3">
        <Link href="/ideas" className="flex-none text-sm text-dim hover:text-accent">
          {tx.misIdeas}
        </Link>
        <span className="truncate text-[15px] font-bold">{titulo ?? tx.tuIdea}</span>
      </div>
      <span className="flex-none rounded-full border border-accent/40 px-3 py-1.5 text-[12.5px] font-semibold text-accent">
        {tx.insigniaIncluido}
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
              {interpolar(tx.historico.viendo, { momento: momentoAbsoluto(historico.cifras_fecha, undefined, idioma) })}
            </p>
            <button
              onClick={volverAHoy}
              className="rounded-cinta border border-accent/40 bg-accent/10 px-4 py-2 text-[13px] font-medium text-accent hover:bg-accent/20"
            >
              {tx.historico.volverAHoy}
            </button>
          </div>
          <h1 className="text-[32px] font-bold leading-tight tracking-tight">
            {interpolar(tx.losNumerosDe, { titulo: titulo ? titulo.toLowerCase() : tx.tuIdeaMinuscula })}
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
  const selloHoy = data.cifras_fecha ? (reciente ? tx.recienActualizado : fechaSello(data.cifras_fecha, undefined, idioma)) : null;

  return (
    <div className="min-h-full">
      {cabecera}

      <div className="mx-auto w-full max-w-[1060px] px-10 pb-16 pt-8" data-screen-label="Tus Numeros vista">
        <Link href={`/idea/${projectId}`} className="mb-6 inline-block text-sm text-dim hover:text-accent">
          {tx.volverAlPlan}
        </Link>

        <div className="mb-3.5 flex items-center gap-2 text-[12px] font-semibold uppercase tracking-[1.3px] text-dim">
          {tx.calculadoPorCodigo}
        </div>
        <h1 className="text-[32px] font-bold leading-tight tracking-tight">
          {interpolar(tx.losNumerosDe, { titulo: titulo ? titulo.toLowerCase() : tx.tuIdeaMinuscula })}
        </h1>

        <VeredictoBloque v={v} />

        <div className="mt-4 flex flex-wrap items-center gap-x-2 gap-y-1 text-[13px] text-dim">
          <span className="font-semibold text-ink">{tx.tusNumerosDeHoy}</span>
          {selloHoy && <span>{interpolar(tx.calculadoConCifrasDel, { sello: selloHoy })}</span>}
          {!editando && (
            <button onClick={() => abrirRecolector(null)} className="ml-1 font-medium text-accent hover:underline">
              {tx.corregirGratis}
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
