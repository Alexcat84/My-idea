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
import { esInvitadoInvisible } from "@/lib/identidad";
import { PACKS, PRECIOS } from "@/lib/precios";
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
function Costo({ cifra }: { cifra: number }) {
  return (
    <span className="inline-flex flex-none items-center gap-1.5 rounded-full border border-accent/35 bg-accent/[0.22] px-2.5 py-1">
      <strong className="text-[14px] font-extrabold tabular-nums text-ink">{cifra}</strong>
      <span className="text-[11.5px] font-semibold text-[#BFD0F5]">créditos</span>
    </span>
  );
}

// Una línea de "lo que incluye": prefijo en negrita + resto.
function Incluye({ items }: { items: [string, string][] }) {
  return (
    <div className="flex flex-col gap-2.5 pt-1">
      {items.map(([fuerte, resto]) => (
        <div key={fuerte} className="flex items-start gap-2.5">
          <Paloma />
          <span className="text-[13px] leading-relaxed text-[#E2E6F0] [text-wrap:pretty]">
            <strong className="font-semibold text-ink">{fuerte}</strong> {resto}
          </span>
        </div>
      ))}
    </div>
  );
}

const INCLUYE_PLAN: [string, string][] = [
  ["El plan:", "tus etapas, con sus entregables, tus tareas y tus fechas de un vistazo."],
  ["Manos a la obra:", "ejecuta tu plan. Marca lo hecho, añade tus notas y ve tu avance en tiempo real. Incluido, siempre."],
  ["Tus Números:", "el tablero de tu idea (margen, punto de equilibrio, escenarios). Corrige cifras y recalcula cuando quieras."],
  ["Tus documentos:", "tu plan y cada resumen, en archivo y PDF, para leer o guardar."],
  ["Tu bitácora:", "la historia de tu viaje, cada decisión, guardada en orden."],
];

const INCLUYE_MUNDO: [string, string][] = [
  ["Su plan y su Manos a la obra:", "las etapas, tareas y fechas de ese frente, listas para ejecutar igual que tu viaje."],
  ["Todo lo del mundo, por separado:", "su avance, sus documentos y su bitácora, solo de ese frente."],
  ["Y suma al general:", "cada mundo se refleja también en la vista completa de tu proyecto. Ves el frente solo, o el panorama entero."],
  ["Un mismo proyecto:", "no es otra cuenta ni otra idea."],
];

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
  const supabase = await createClient();
  const {
    data: { user },
  } = await supabase.auth.getUser();
  const cuentaReal = Boolean(user && !esInvitadoInvisible(user));
  let saldo = 0;
  if (cuentaReal) {
    const { data: cuenta } = await supabase.from("credit_accounts").select("creditos_total").maybeSingle();
    saldo = (cuenta as { creditos_total: number } | null)?.creditos_total ?? 0;
  }

  return (
    <div className="flex min-h-full flex-1 flex-col">
      {/* Barra: dónde estoy y cuánto tengo */}
      <header className="sticky top-0 z-30 flex h-[58px] items-center gap-3 border-b border-hairline px-5 sm:px-6" style={{ background: "rgba(0,0,0,0.82)", backdropFilter: "blur(14px)", WebkitBackdropFilter: "blur(14px)" }}>
        <Link href="/ideas" className="text-[13px] text-dim hover:text-ink">
          Mis ideas /
        </Link>
        <span className="text-[14.5px] font-semibold">Créditos</span>
        <span className="flex-1" />
        <div className="flex items-center gap-2 rounded-full border border-accent/35 bg-accent/[0.08] px-3 py-1.5">
          <span className="h-1.5 w-1.5 rounded-full bg-accent" />
          <span className="text-[12.5px] font-semibold tabular-nums text-[#DCE7FF]">{saldo} créditos</span>
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
            <div className="text-[11px] font-bold uppercase tracking-[1.6px] text-[#8FB0FF]">Tu saldo</div>
            <div className="flex items-baseline gap-3">
              <span className="text-[84px] font-extrabold leading-[0.85] tracking-[-0.04em] tabular-nums sm:text-[96px]">
                {saldo}
              </span>
              <span className="text-[18px] text-dim">créditos</span>
            </div>
          </div>
          <p className="mt-4 max-w-md text-center text-[12.5px] leading-relaxed text-dim">
            {cuentaReal
              ? "Se verifica tu saldo al inicio de cada acción y se descuenta a la entrega. Si algo falla a mitad, no se cobra nada."
              : "Tus créditos viven en tu cuenta. Entra o crea la tuya para sumar y usar créditos."}
          </p>
        </section>

        {/* ── SUMAR CRÉDITOS: las cuatro recargas (provisional) ───────────── */}
        <section className="anima-plan-in flex flex-col items-center gap-6" style={{ animationDelay: "0.05s" }}>
          <h2 className="text-center text-[22px] font-bold tracking-tight">Sumar créditos</h2>
          <div className="grid w-full grid-cols-1 gap-4 sm:grid-cols-2 lg:grid-cols-4">
            {PACKS.map((pack, i) => {
              const s = estiloRecarga(i, Boolean(pack.destacado));
              return (
                <article
                  key={pack.nombre}
                  className={`flex flex-col items-center gap-4 rounded-panel border p-6 text-center ${s.caja}`}
                  style={{ background: s.fondo }}
                >
                  {pack.destacado && (
                    <span className="absolute -top-2.5 left-1/2 flex h-[22px] -translate-x-1/2 items-center rounded-full bg-accent px-3 text-[11px] font-extrabold text-[#04102C]">
                      El más elegido
                    </span>
                  )}
                  <span
                    className={`flex h-[54px] w-[54px] items-center justify-center rounded-full border text-[20px] font-extrabold tabular-nums ${s.ficha}`}
                  >
                    {pack.creditos}
                  </span>
                  <span className="flex flex-col gap-1">
                    <span className="text-[15px] font-semibold">{pack.nombre}</span>
                    <span className={`text-[12.5px] ${s.cantidad}`}>{pack.creditos} créditos</span>
                  </span>
                  <span className="text-[30px] font-extrabold leading-none tracking-[-0.025em] tabular-nums">
                    ${pack.usd}
                  </span>
                  <button
                    type="button"
                    disabled
                    className="mt-1 flex w-full cursor-not-allowed items-center justify-center rounded-[11px] border border-hairline py-2.5 text-[12.5px] font-semibold text-dim/70"
                  >
                    La compra se abre pronto
                  </button>
                </article>
              );
            })}
          </div>
        </section>

        {/* ── USA TUS CRÉDITOS: lo gratis, luego los tres planes ──────────── */}
        <section className="anima-plan-in flex flex-col items-center gap-6 border-t border-hairline pt-10" style={{ animationDelay: "0.1s" }}>
          <h2 className="text-center text-[22px] font-bold tracking-tight">Usa tus créditos según lo que necesites</h2>

          <p className="max-w-3xl text-center text-[13.5px] leading-relaxed text-dim [text-wrap:pretty]">
            <strong className="text-ink">La Claridad</strong> es <strong className="text-done">gratis</strong>: tu idea
            ordenada, la frase, lo que tienes y lo que asumes. El <strong className="text-ink">diagnóstico de un mundo</strong>{" "}
            también es <strong className="text-done">gratis</strong>: el primer vistazo de ese frente.
          </p>

          <div className="grid w-full grid-cols-1 items-start gap-4 lg:grid-cols-3">
            {/* Columna 1: el proyecto entero */}
            <article
              className="flex flex-col gap-5 rounded-panel border border-accent/30 p-6"
              style={{ background: "linear-gradient(180deg, rgba(77,124,254,0.09) 0%, rgba(77,124,254,0.02) 100%)" }}
            >
              <span className="inline-flex self-start items-center rounded-full bg-accent/20 px-2.5 py-1 text-[11px] font-bold text-[#DCE7FF]">
                Tu proyecto
              </span>

              <div className="flex flex-col gap-3">
                <div className="flex items-center justify-between gap-3">
                  <span className="text-[16px] font-bold">Tu Plan</span>
                  <Costo cifra={PRECIOS.plan_completo} />
                </div>
                <span className="text-[13px] leading-relaxed text-dim [text-wrap:pretty]">
                  Tu viaje completo, de la idea a hacerla realidad: el plan y todo para llevarlo a cabo.
                </span>
                <Incluye items={INCLUYE_PLAN} />
              </div>

              <div className="flex flex-col gap-3 border-t border-hairline pt-4">
                <div className="flex items-center justify-between gap-3">
                  <span className="text-[16px] font-bold">Un cambio de rumbo</span>
                  <Costo cifra={PRECIOS.seguimiento} />
                </div>
                <span className="text-[13px] leading-relaxed text-dim [text-wrap:pretty]">
                  Cuando la realidad te mueve el plan y necesitas replantear sin empezar de cero: cuentas qué pasó, se
                  conserva lo que ya lograste y tu viaje se rehace desde ahí.
                </span>
              </div>
            </article>

            {/* Columna 2: un frente del negocio */}
            <article
              className="flex flex-col gap-5 rounded-panel border border-accent/30 p-6"
              style={{ background: "linear-gradient(180deg, rgba(77,124,254,0.09) 0%, rgba(77,124,254,0.02) 100%)" }}
            >
              <span className="inline-flex self-start items-center rounded-full bg-accent/20 px-2.5 py-1 text-[11px] font-bold text-[#DCE7FF]">
                Un mundo
              </span>

              <div className="flex flex-col gap-3">
                <div className="flex items-center justify-between gap-3">
                  <span className="text-[16px] font-bold">El plan de un mundo</span>
                  <Costo cifra={PRECIOS.mundo_activar} />
                </div>
                <span className="text-[13px] leading-relaxed text-dim [text-wrap:pretty]">
                  Un frente entero de tu negocio (calidad, riesgos, seguridad…), con su propio espacio dentro de tu mismo
                  proyecto.
                </span>
                <Incluye items={INCLUYE_MUNDO} />
              </div>

              <div className="flex flex-col gap-3 border-t border-hairline pt-4">
                <div className="flex items-center justify-between gap-3">
                  <span className="text-[16px] font-bold">Un cambio de rumbo en un mundo</span>
                  <Costo cifra={PRECIOS.mundo_seguimiento} />
                </div>
                <span className="text-[13px] leading-relaxed text-dim [text-wrap:pretty]">
                  Lo mismo dentro de ese frente, cuando ahí necesitas replantear el rumbo.
                </span>
              </div>
            </article>

            {/* Columna 3: el catálogo de mundos */}
            <article
              className="flex flex-col gap-5 rounded-panel border border-accent/30 p-6"
              style={{ background: "linear-gradient(180deg, rgba(77,124,254,0.09) 0%, rgba(77,124,254,0.02) 100%)" }}
            >
              <span className="inline-flex self-start items-center rounded-full bg-accent/20 px-2.5 py-1 text-[11px] font-bold text-[#DCE7FF]">
                Los mundos que puedes desbloquear
              </span>

              <div className="flex flex-col gap-3.5">
                {mundosVisibles().map((mundo) => (
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
