/**
 * /creditos — el CENTRO DE CRÉDITOS. Área del dinero, separada de Potenciadores
 * (regla del fundador: no mezclar procesos). Aquí vive tu saldo, los packs de
 * recarga y para qué alcanza cada crédito.
 *
 * Calco del diseño de Claude Design (_entrega-claude-design/credits/
 * 10_centro_de_creditos_1240.html) con los tokens de la casa. Estructura:
 *  1. Héroe: el saldo, en grande.
 *  2. Sumar créditos: las cuatro recargas (PACKS de precios.ts).
 *  3. Usa tus créditos: lo gratis primero, luego los tres planes (Tu proyecto,
 *     Un mundo, y el catálogo de mundos por desbloquear).
 *
 * Números SIEMPRE de precios.ts, jamás hardcodeados ni copiados al catálogo
 * (que los llevaba y envejecieron diciendo 3 cuando se cobraban 5). La
 * compra con dinero sigue dormida hasta que despierten las pasarelas: el botón
 * lo dice honesto ("La compra se abre pronto"), no finge cobrar.
 *
 * NOTA (2026-08): la sección de precios (las recargas) es provisional; el
 * fundador la va a recalibrar con opciones más visuales. Todo lo demás es canon.
 */
import Link from "next/link";
import { mundosVisibles } from "@/lib/catalogoMundos";
import { elegir } from "@/lib/i18n/config";
import { interpolar } from "@/lib/i18n/interpolar";
import { CREDITOS } from "@/lib/i18n/mensajes/creditos";
import { PACKS_RECARGA } from "@/lib/i18n/mensajes/packsRecarga";
import { rico } from "@/lib/i18n/rico";
import { idiomaDeCookies } from "@/lib/i18n/servidor";
import { esInvitadoInvisible } from "@/lib/identidad";
import { PACKS, PRECIOS } from "@/lib/precios";
import { apartadoDe } from "@/lib/creditos";
import { leerSaldo } from "@/lib/saldo";
import { textoChipSaldo } from "@/lib/textoSaldo";
import { createClient } from "@/lib/supabase/server";

export const dynamic = "force-dynamic";

// Paloma azul del canon (la lista de "lo que incluye").
function Paloma() {
  return (
    <svg className="mt-0.5 shrink-0" width="15" height="15" viewBox="0 0 16 16" fill="none" aria-hidden="true">
      <path d="m3.5 8.4 3 3 6-6.6" stroke="#8FB0FF" strokeWidth="1.6" strokeLinecap="round" strokeLinejoin="round" />
    </svg>
  );
}

// El costo, siempre a la derecha del nombre (píldora azul).
function Costo({ cifra, etiqueta }: { cifra: number; etiqueta: string }) {
  return (
    <span className="inline-flex flex-none items-center gap-1.5 rounded-full border border-accent/35 bg-accent/[0.22] px-2.5 py-1">
      <strong className="text-[14px] font-extrabold tabular-nums text-ink">{cifra}</strong>
      <span className="text-[11.5px] font-semibold text-[#BFD0F5]">{etiqueta}</span>
    </span>
  );
}

// Una línea de "lo que incluye": prefijo en negrita (<b> del catálogo) + resto.
function Incluye({ items }: { items: string[] }) {
  return (
    <div className="flex flex-col gap-2.5 pt-1">
      {items.map((item) => (
        <div key={item} className="flex items-start gap-2.5">
          <Paloma />
          <span className="text-[13px] leading-relaxed text-[#E2E6F0] [text-wrap:pretty]">
            {rico(item, { b: (c) => <strong className="font-semibold text-ink">{c}</strong> })}
          </span>
        </div>
      ))}
    </div>
  );
}

// Lo que incluye cada plan vive en el catálogo (CREDITOS.incluyePlan e
// incluyeMundo). AUD-09 M47: la vista global que se prometía en el del mundo
// ya no existe (BANCO §7.1); la única lectura de la idea entera es el Expediente.

// Estilo de cada escalón de recarga (calco de los cuatro del diseño).
function estiloRecarga(i: number, destacado: boolean) {
  if (destacado) {
    return {
      caja: "relative border-accent/60 shadow-[0_0_0_1px_rgba(77,124,254,0.16),0_18px_44px_rgba(0,0,0,0.55)]",
      fondo: "linear-gradient(180deg, rgba(77,124,254,0.20) 0%, rgba(77,124,254,0.05) 50%, rgba(77,124,254,0.02) 100%)",
      ficha: "border-transparent bg-accent text-[#04102C]",
      cantidad: "text-[#8FB0FF]",
    };
  }
  if (i === 1) {
    return {
      caja: "border-accent/[0.22]",
      fondo: "linear-gradient(180deg, rgba(77,124,254,0.05) 0%, #101013 70%)",
      ficha: "border-accent/40 bg-accent/[0.12] text-[#A9C4FF]",
      cantidad: "text-dim",
    };
  }
  if (i === 3) {
    return {
      caja: "border-accent/[0.34]",
      fondo: "linear-gradient(180deg, rgba(77,124,254,0.08) 0%, #0c0c10 70%)",
      ficha: "border-accent/[0.55] bg-accent/[0.18] text-[#DCE7FF]",
      cantidad: "text-dim",
    };
  }
  return {
    caja: "border-hairline",
    fondo: "#101013",
    ficha: "border-accent/25 bg-accent/[0.07] text-[#8FB0FF]",
    cantidad: "text-dim",
  };
}

export default async function Creditos() {
  const idioma = await idiomaDeCookies();
  const t = elegir(CREDITOS, idioma);
  const tPacks = elegir(PACKS_RECARGA, idioma);
  const supabase = await createClient();
  const {
    data: { user },
  } = await supabase.auth.getUser();
  const cuentaReal = Boolean(user && !esInvitadoInvisible(user));
  // AUD-09 M21: lectura única; si falla, null y se dice (nunca un 0 falso).
  let saldo: number | null = 0;
  if (cuentaReal) saldo = await leerSaldo(supabase);
  // AUD-09 M31: lo reservado por una sesión en curso (M25). La barra dice lo
  // disponible; el héroe, el saldo y cuánto está reservado. Si las reservas no
  // se leen, no se inventa un disponible.
  let reservados: number | null = 0;
  if (cuentaReal && user && saldo !== null) {
    try {
      reservados = await apartadoDe(user.id);
    } catch (e) {
      console.error("[creditos] no se pudieron leer las reservas:", e);
      reservados = null;
    }
  }
  const textoSaldo = saldo !== null && reservados !== null ? textoChipSaldo(Math.max(0, saldo - reservados), reservados, idioma) : null;

  return (
    <div className="flex min-h-full flex-1 flex-col">
      {/* Barra: dónde estoy y cuánto tengo */}
      <header className="sticky top-0 z-30 flex h-[58px] items-center gap-3 border-b border-hairline px-5 sm:px-6" style={{ background: "rgba(0,0,0,0.82)", backdropFilter: "blur(14px)", WebkitBackdropFilter: "blur(14px)" }}>
        <Link href="/ideas" className="text-[13px] text-dim hover:text-ink">
          {t.misIdeas}
        </Link>
        <span className="text-[14.5px] font-semibold">{t.titulo}</span>
        <span className="flex-1" />
        <div className="flex items-center gap-2 rounded-full border border-accent/35 bg-accent/[0.08] px-3 py-1.5">
          <span className="h-1.5 w-1.5 rounded-full bg-accent" />
          <span className="text-[12.5px] font-semibold tabular-nums text-[#DCE7FF]">
            {textoSaldo ? interpolar(t.disponibles, { saldo: textoSaldo.principal }) : t.saldoNoDisponible}
          </span>
        </div>
      </header>

      <main className="mx-auto flex w-full max-w-[1180px] flex-1 flex-col gap-12 px-4 py-10 sm:px-8">
        {/* ── HÉROE: el saldo ─────────────────────────────────────────────── */}
        <section className="anima-plan-in flex flex-col items-center">
          <div
            className="flex flex-col items-center gap-3 rounded-[20px] border border-accent/25 px-12 py-9 text-center shadow-[0_24px_60px_rgba(0,0,0,0.55)] sm:px-20"
            style={{
              background:
                "linear-gradient(135deg, rgba(77,124,254,0.14) 0%, rgba(77,124,254,0.03) 55%, rgba(255,255,255,0.01) 100%)",
            }}
          >
            <div className="text-[11px] font-bold uppercase tracking-[1.6px] text-[#8FB0FF]">{t.heroe.tuSaldo}</div>
            {saldo === null ? (
              <p className="max-w-xs text-[15px] text-warn">{t.heroe.noPudeLeer}</p>
            ) : (
              <div className="flex items-baseline gap-3">
                <span className="text-[84px] font-extrabold leading-[0.85] tracking-[-0.04em] tabular-nums sm:text-[96px]">
                  {saldo}
                </span>
                <span className="text-[18px] text-dim">{t.creditos}</span>
              </div>
            )}
            {textoSaldo?.reservados && <p className="text-[13px] text-dim">{textoSaldo.reservados}</p>}
          </div>
          <p className="mt-4 max-w-md text-center text-[12.5px] leading-relaxed text-dim">
            {cuentaReal
              ? t.heroe.garantiaCuenta
              : t.heroe.sinCuenta}
          </p>
        </section>

        {/* ── SUMAR CRÉDITOS: las cuatro recargas (provisional) ───────────── */}
        <section className="anima-plan-in flex flex-col items-center gap-6" style={{ animationDelay: "0.05s" }}>
          <h2 className="text-center text-[22px] font-bold tracking-tight">{t.sumar.titulo}</h2>
          <div className="grid w-full grid-cols-1 gap-4 sm:grid-cols-2 lg:grid-cols-4">
            {PACKS.map((pack, i) => {
              const s = estiloRecarga(i, Boolean(pack.destacado));
              return (
                <article
                  key={pack.clave}
                  className={`flex flex-col items-center gap-4 rounded-panel border p-6 text-center ${s.caja}`}
                  style={{ background: s.fondo }}
                >
                  {/* AUD-09 B03a: sin la chapa de "más elegido" (ningún dato la respalda). */}
                  <span
                    className={`flex h-[54px] w-[54px] items-center justify-center rounded-full border text-[20px] font-extrabold tabular-nums ${s.ficha}`}
                  >
                    {pack.creditos}
                  </span>
                  <span className="flex flex-col gap-1">
                    <span className="text-[15px] font-semibold">{tPacks[pack.clave].nombre}</span>
                    <span className={`text-[12.5px] ${s.cantidad}`}>{interpolar(t.sumar.nCreditos, { n: pack.creditos })}</span>
                  </span>
                  <span className="text-[30px] font-extrabold leading-none tracking-[-0.025em] tabular-nums">
                    ${pack.usd}
                  </span>
                  <button
                    type="button"
                    disabled
                    className="mt-1 flex w-full cursor-not-allowed items-center justify-center rounded-[11px] border border-hairline py-2.5 text-[12.5px] font-semibold text-dim/70"
                  >
                    {t.sumar.compraPronto}
                  </button>
                </article>
              );
            })}
          </div>
        </section>

        {/* ── USA TUS CRÉDITOS: lo gratis, luego los tres planes ──────────── */}
        <section className="anima-plan-in flex flex-col items-center gap-6 border-t border-hairline pt-10" style={{ animationDelay: "0.1s" }}>
          <h2 className="text-center text-[22px] font-bold tracking-tight">{t.usar.titulo}</h2>

          <p className="max-w-3xl text-center text-[13.5px] leading-relaxed text-dim [text-wrap:pretty]">
            {rico(t.usar.gratis, {
              b: (c) => <strong className="text-ink">{c}</strong>,
              g: (c) => <strong className="text-done">{c}</strong>,
            })}
          </p>

          <div className="grid w-full grid-cols-1 items-start gap-4 lg:grid-cols-3">
            {/* Columna 1: el proyecto entero */}
            <article
              className="flex flex-col gap-5 rounded-panel border border-accent/30 p-6"
              style={{ background: "linear-gradient(180deg, rgba(77,124,254,0.09) 0%, rgba(77,124,254,0.02) 100%)" }}
            >
              <span className="inline-flex self-start items-center rounded-full bg-accent/20 px-2.5 py-1 text-[11px] font-bold text-[#DCE7FF]">
                {t.proyecto.etiqueta}
              </span>

              <div className="flex flex-col gap-3">
                <div className="flex items-center justify-between gap-3">
                  <span className="text-[16px] font-bold">{t.proyecto.plan}</span>
                  <Costo cifra={PRECIOS.plan_completo} etiqueta={t.creditos} />
                </div>
                <span className="text-[13px] leading-relaxed text-dim [text-wrap:pretty]">
                  {t.proyecto.planTexto}
                </span>
                <Incluye items={t.incluyePlan} />
              </div>

              <div className="flex flex-col gap-3 border-t border-hairline pt-4">
                <div className="flex items-center justify-between gap-3">
                  <span className="text-[16px] font-bold">{t.proyecto.cambioRumbo}</span>
                  <Costo cifra={PRECIOS.seguimiento} etiqueta={t.creditos} />
                </div>
                <span className="text-[13px] leading-relaxed text-dim [text-wrap:pretty]">
                  {t.proyecto.cambioRumboTexto}
                </span>
              </div>
            </article>

            {/* Columna 2: un frente del negocio */}
            <article
              className="flex flex-col gap-5 rounded-panel border border-accent/30 p-6"
              style={{ background: "linear-gradient(180deg, rgba(77,124,254,0.09) 0%, rgba(77,124,254,0.02) 100%)" }}
            >
              <span className="inline-flex self-start items-center rounded-full bg-accent/20 px-2.5 py-1 text-[11px] font-bold text-[#DCE7FF]">
                {t.mundo.etiqueta}
              </span>

              <div className="flex flex-col gap-3">
                <div className="flex items-center justify-between gap-3">
                  <span className="text-[16px] font-bold">{t.mundo.plan}</span>
                  <Costo cifra={PRECIOS.mundo_activar} etiqueta={t.creditos} />
                </div>
                <span className="text-[13px] leading-relaxed text-dim [text-wrap:pretty]">
                  {t.mundo.planTexto}
                </span>
                <Incluye items={t.incluyeMundo} />
              </div>

              <div className="flex flex-col gap-3 border-t border-hairline pt-4">
                <div className="flex items-center justify-between gap-3">
                  <span className="text-[16px] font-bold">{t.mundo.cambioRumbo}</span>
                  <Costo cifra={PRECIOS.mundo_seguimiento} etiqueta={t.creditos} />
                </div>
                <span className="text-[13px] leading-relaxed text-dim [text-wrap:pretty]">
                  {t.mundo.cambioRumboTexto}
                </span>
              </div>
            </article>

            {/* Columna 3: el catálogo de mundos */}
            <article
              className="flex flex-col gap-5 rounded-panel border border-accent/30 p-6"
              style={{ background: "linear-gradient(180deg, rgba(77,124,254,0.09) 0%, rgba(77,124,254,0.02) 100%)" }}
            >
              <span className="inline-flex self-start items-center rounded-full bg-accent/20 px-2.5 py-1 text-[11px] font-bold text-[#DCE7FF]">
                {t.mundosPorDesbloquear}
              </span>

              <div className="flex flex-col gap-3.5">
                {mundosVisibles(false, idioma).map((mundo) => (
                  <div key={mundo.clave} className="flex flex-col gap-0.5">
                    <span className="text-[13.5px] font-bold text-ink">{mundo.nombre}</span>
                    <span className="text-[12.5px] leading-snug text-dim [text-wrap:pretty]">{mundo.promesa}</span>
                  </div>
                ))}
              </div>
            </article>
          </div>
        </section>
      </main>
    </div>
  );
}
