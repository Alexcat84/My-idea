/**
 * /creditos — el área de CRÉDITOS, separada de Potenciadores (regla del
 * fundador: no mezclar procesos). Aquí vive todo lo del dinero: tu saldo,
 * los packs de recarga y lo que cuesta cada cosa en créditos. Los
 * potenciadores (Tus Números, los mundos) son add-ons de las ideas y viven
 * en /potenciadores; el desarrollo de Tus Números vive dentro de cada idea.
 *
 * Recargas DECIDIDAS por el fundador (2026-07-19): 1 crédito = 1 USD (ancla
 * invariable, sin descuento por volumen), packs por entregable (5/15/30 a
 * $4.99/$14.99/$29.99), LEYENDO de precios.ts (PACKS), jamás hardcodeado. La
 * compra con dinero sigue dormida hasta que despierten las pasarelas.
 */
import Link from "next/link";
import { esInvitadoInvisible } from "@/lib/identidad";
import { PACKS, PRECIOS } from "@/lib/precios";
import { createClient } from "@/lib/supabase/server";

export const dynamic = "force-dynamic";

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
      <header className="flex h-[58px] items-center gap-3 border-b border-hairline px-5 sm:px-6">
        <Link href="/ideas" className="text-[13px] text-dim hover:text-ink">
          Mis ideas /
        </Link>
        <span className="text-[14.5px] font-semibold">Créditos</span>
      </header>

      <main className="mx-auto flex w-full max-w-4xl flex-1 flex-col gap-10 px-4 py-10 sm:px-6">
        {/* ── SALDO + RECARGAS ────────────────────────────────────────────── */}
        <section className="anima-plan-in">
          <h1 className="text-2xl font-bold tracking-tight">Tus créditos</h1>
          <p className="mt-2 max-w-2xl text-[15px] leading-relaxed text-dim">
            Los créditos son consumibles: sin suscripción, sin cargos recurrentes. Nunca pierdes créditos por un fallo del
            sistema, y registrar tu avance es gratis para siempre.
          </p>

          <div className="mt-6 grid gap-4 sm:grid-cols-[280px_1fr]">
            <div className="rounded-panel border border-hairline bg-surface p-6">
              <div className="text-[40px] font-extrabold leading-none tracking-tight">{saldo}</div>
              <div className="mt-1.5 text-[13px] text-dim">
                {cuentaReal ? "créditos disponibles" : "tus créditos nacen con tu cuenta"}
              </div>
              {cuentaReal && (
                <span className="mt-2 inline-flex items-center rounded-full border border-done/40 px-2.5 py-1 text-[11.5px] font-semibold text-done">
                  cortesía de bienvenida
                </span>
              )}
              <p className="mt-3 text-[12.5px] leading-relaxed text-dim">
                Se verifica tu saldo al inicio de cada acción y se descuenta a la entrega. Si algo falla a mitad, no se cobra
                nada.
              </p>
            </div>

            <div className="grid gap-3.5 sm:grid-cols-3">
              {PACKS.map((pack) => (
                <div
                  key={pack.creditos}
                  className={
                    "relative flex flex-col gap-1.5 rounded-panel border bg-surface p-5 " +
                    (pack.destacado ? "border-accent/45 bg-accent/[0.05]" : "border-hairline")
                  }
                >
                  <span className="text-[26px] font-extrabold leading-none">{pack.creditos}</span>
                  <span className="text-[13px] text-dim">créditos</span>
                  <span className="mt-2 text-2xl font-bold">${pack.usd}</span>
                  <span className="text-[12px] text-dim">
                    {pack.sentido}
                    {pack.destacado ? " · el más elegido" : ""}
                  </span>
                </div>
              ))}
            </div>
          </div>

          <p className="mt-4 rounded-cinta border border-hairline bg-surface-2 px-4 py-3 text-[12.5px] leading-relaxed text-dim">
            <strong className="text-ink">Un crédito es un dólar, siempre.</strong> Los packs no esconden descuentos: se
            dimensionan por lo que compras con ellos. La compra con dinero se abre muy pronto; durante la beta trabajas
            con tu cortesía de bienvenida.
          </p>
        </section>

        {/* ── LO QUE CUESTA CADA COSA (números de precios.ts, jamás hardcodeados) */}
        <section className="anima-plan-in" style={{ animationDelay: "0.05s" }}>
          <p className="text-[11px] font-semibold uppercase tracking-[1.2px] text-dim">Lo que cuesta cada cosa</p>
          <div className="mt-4 overflow-hidden rounded-panel border border-hairline bg-surface">
            {[
              { que: "El organizador (Claridad)", detalle: "tu idea ordenada: frase, lo que tienes, lo que asumes", precio: null },
              { que: "La Exploración", detalle: "la entrevista y tu plan completo", precio: PRECIOS.plan_completo },
              { que: "El plan de un mundo", detalle: "el preview (entrevista + diagnóstico) es gratis", precio: PRECIOS.mundo_activar },
              { que: "Seguimiento del viaje principal", detalle: "contar qué pasó y recalcular tu plan desde donde estás", precio: PRECIOS.seguimiento },
              { que: "Seguimiento de un mundo", detalle: "contar qué pasó en su checklist", precio: PRECIOS.mundo_seguimiento },
              { que: "Tus Números", detalle: "una vez por idea; corregir cifras y recalcular es gratis, siempre", precio: PRECIOS.tus_numeros },
              { que: "Registrar tu avance", detalle: "marcar hecho, notas, progreso", precio: null },
            ].map((fila, i) => (
              <div
                key={fila.que}
                className={`flex flex-wrap items-baseline gap-x-4 gap-y-1 px-5 py-3.5 sm:flex-nowrap ${i > 0 ? "border-t border-hairline" : ""}`}
              >
                <span className="text-[13.5px] font-semibold">{fila.que}</span>
                <span className="min-w-0 flex-1 text-[12.5px] text-dim">{fila.detalle}</span>
                <span className={`shrink-0 text-[12.5px] font-semibold ${fila.precio === null ? "text-done" : "text-accent"}`}>
                  {fila.precio === null ? "Gratis, siempre" : `${fila.precio} créditos`}
                </span>
              </div>
            ))}
          </div>
        </section>
      </main>
    </div>
  );
}
