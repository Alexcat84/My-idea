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
            Créditos consumibles: sin suscripción y sin cargos recurrentes. Tu plan cuesta {PRECIOS.plan_completo} créditos
            e incluye Tus Números; los seguimientos y los mundos, {PRECIOS.seguimiento} cada uno. La Claridad y los
            diagnósticos de mundos son gratis.
          </p>

          <div className="mt-6 rounded-panel border border-hairline bg-surface p-6 sm:max-w-sm">
            <div className="text-[40px] font-extrabold leading-none tracking-tight tabular-nums">{saldo}</div>
            <div className="mt-1.5 text-[13px] text-dim">
              {cuentaReal ? "créditos disponibles" : "tus créditos viven en tu cuenta"}
            </div>
            <p className="mt-3 text-[12.5px] leading-relaxed text-dim">
              Se verifica tu saldo al inicio de cada acción y se descuenta a la entrega. Si algo falla a mitad, no se cobra
              nada.
            </p>
          </div>

          <div className="mt-4 grid grid-cols-1 gap-3.5 sm:grid-cols-2 lg:grid-cols-4">
            {PACKS.map((pack) => (
              <div
                key={pack.nombre}
                className={
                  "relative flex flex-col gap-1.5 rounded-panel border bg-surface p-5 " +
                  (pack.destacado ? "border-accent/45 bg-accent/[0.05]" : "border-hairline")
                }
              >
                {pack.destacado && (
                  <span className="absolute right-4 top-4 rounded-full bg-accent/15 px-2 py-0.5 text-[10.5px] font-semibold text-accent">
                    El más elegido
                  </span>
                )}
                <span className="text-[13px] font-semibold">{pack.nombre}</span>
                <span className="mt-1 text-[26px] font-extrabold leading-none tabular-nums">
                  {pack.creditos} <span className="text-[13px] font-medium text-dim">créditos</span>
                </span>
                <span className="text-2xl font-bold tabular-nums">${pack.usd}</span>
                <span className="min-h-[32px] text-[12px] leading-snug text-dim">Alcanza para {pack.alcanza}.</span>
                <button
                  type="button"
                  disabled
                  className="mt-1 w-full cursor-not-allowed rounded-[10px] border border-hairline py-2 text-[12.5px] font-semibold text-dim/70"
                >
                  La compra se abre pronto
                </button>
              </div>
            ))}
          </div>
        </section>

        {/* ── LO QUE CUESTA CADA COSA (números de precios.ts, jamás hardcodeados) */}
        <section className="anima-plan-in" style={{ animationDelay: "0.05s" }}>
          <p className="text-[11px] font-semibold uppercase tracking-[1.2px] text-dim">Lo que cuesta cada cosa</p>
          <div className="mt-4 overflow-hidden rounded-panel border border-hairline bg-surface">
            {[
              { que: "La Claridad", detalle: "tu idea ordenada: la frase, lo que tienes, lo que asumes", etiqueta: "Gratis", tono: "gratis" },
              { que: "El diagnóstico de un mundo", detalle: "el escaparate del mundo: su entrevista y su diagnóstico", etiqueta: "Gratis", tono: "gratis" },
              { que: "Tu Plan", detalle: "La Exploración, tu plan completo y Tus Números, todo dentro", etiqueta: `${PRECIOS.plan_completo} créditos`, tono: "precio" },
              { que: "El plan de un mundo", detalle: "el plan del dominio; su diagnóstico ya fue gratis", etiqueta: `${PRECIOS.mundo_activar} créditos`, tono: "precio" },
              { que: "Seguimiento del viaje principal", detalle: "contar qué pasó y recalcular tu plan desde donde estás", etiqueta: `${PRECIOS.seguimiento} créditos`, tono: "precio" },
              { que: "Seguimiento de un mundo", detalle: "contar qué pasó en su checklist", etiqueta: `${PRECIOS.mundo_seguimiento} créditos`, tono: "precio" },
              { que: "Tus Números", detalle: "el tablero de sostenibilidad de tu idea; corregir cifras y recalcular, cuando quieras", etiqueta: "Incluido con tu plan", tono: "incluido" },
              { que: "Registrar tu avance", detalle: "marcar hecho, notas, tus documentos y tu bitácora", etiqueta: "Incluido con tu paquete", tono: "incluido" },
            ].map((fila, i) => (
              <div
                key={fila.que}
                className={`flex flex-wrap items-baseline gap-x-4 gap-y-1 px-5 py-3.5 sm:flex-nowrap ${i > 0 ? "border-t border-hairline" : ""}`}
              >
                <span className="text-[13.5px] font-semibold">{fila.que}</span>
                <span className="min-w-0 flex-1 text-[12.5px] text-dim">{fila.detalle}</span>
                <span
                  className={`shrink-0 text-[12.5px] font-semibold ${
                    fila.tono === "gratis" ? "text-done" : fila.tono === "incluido" ? "text-ink" : "text-accent"
                  }`}
                >
                  {fila.etiqueta}
                </span>
              </div>
            ))}
          </div>
          <p className="mt-3 text-[12px] leading-relaxed text-dim">
            Al comprar tu plan, Tus Números vienen dentro. Registrar tu avance, tus documentos y tu bitácora van incluidos
            con lo que ya compraste: nunca se cobran aparte.
          </p>
        </section>
      </main>
    </div>
  );
}
