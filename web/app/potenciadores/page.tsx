/**
 * /potenciadores — Potenciadores y Créditos (canon 07). Tres bloques: el
 * centro de créditos, la fila de potenciadores y "Tus Números por dentro"
 * con el único uso del ámbar, el guardián de datos.
 *
 * ETAPA 2 (beta viva): los precios son VIVOS y se pagan con la cortesía (20
 * al primer login). El preview de un mundo es gratis (4.5); su PLAN cuesta
 * su precio de catálogo, LEYENDO de precios.ts, jamás hardcodeado. El saldo
 * del panel es el real (RLS own-select). La moneda se llama créditos.
 *
 * El catálogo de BUNDLES de compra (cuántos créditos por pack, a qué precio en
 * dinero) es una DECISIÓN PENDIENTE DEL FUNDADOR para la ETAPA 2: precios.ts no
 * define bundles, así que aquí el precio en dinero va como "$ —" deshabilitado
 * y con su nota. Ver docs/MATRIZ_DELTAS_CANON_2.0.md ("Decisiones pendientes").
 */
import Link from "next/link";
import catalogo from "@/lib/assets/packs_catalog.json";
import { esInvitadoInvisible } from "@/lib/identidad";
import { PRECIOS } from "@/lib/precios";
import { createClient } from "@/lib/supabase/server";

const MUNDOS = (catalogo.packs as Array<{ clave: string; nombre: string; promesa: string }>).map((p) => ({
  nombre: p.nombre,
  promesa: p.promesa,
}));

// Tamaños de bundle provisionales: NO son un precio decidido. El fundador fija
// el catálogo (tamaños y dinero) en la ETAPA 2; aquí van sin precio en dinero.
const PACKS_PROVISIONALES = [
  { creditos: 10, destacado: false },
  { creditos: 30, destacado: true },
  { creditos: 75, destacado: false },
];

const PUNTO_MUNDO = "#3A9B8F"; // matiz de los mundos (ni azul ni verde)

export default async function Potenciadores() {
  // ETAPA 2: el saldo real del ledger (RLS: cada quien ve solo lo suyo). La
  // identidad invisible no tiene ledger: sus créditos nacen con su cuenta.
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
        <span className="text-[14.5px] font-semibold">Potenciadores y créditos</span>
      </header>

      <main className="mx-auto flex w-full max-w-4xl flex-1 flex-col gap-10 px-4 py-10 sm:px-6">
        {/* ── CENTRO DE CRÉDITOS ─────────────────────────────────────────── */}
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
              <p className="mt-3 text-[12.5px] leading-relaxed text-dim">
                Se verifica tu saldo al inicio de cada acción y se descuenta a la entrega. Si algo falla a mitad, no se cobra
                nada.
              </p>
            </div>

            <div className="grid gap-3.5 sm:grid-cols-3">
              {PACKS_PROVISIONALES.map((pack) => (
                <div
                  key={pack.creditos}
                  className={
                    "relative flex flex-col gap-1.5 rounded-panel border bg-surface p-5 " +
                    (pack.destacado ? "border-accent/45 bg-accent/[0.05]" : "border-hairline")
                  }
                >
                  <span className="text-[26px] font-extrabold leading-none">{pack.creditos}</span>
                  <span className="text-[13px] text-dim">créditos</span>
                  <span className="mt-2 text-2xl font-bold text-dim">$ —</span>
                  <span className="text-[12px] text-dim">{pack.destacado ? "por definir · el más elegido" : "por definir"}</span>
                </div>
              ))}
            </div>
          </div>

          <p className="mt-4 rounded-cinta border border-hairline bg-surface-2 px-4 py-3 text-[12.5px] leading-relaxed text-dim">
            <strong className="text-ink">Catálogo de packs por definir.</strong> Cuántos créditos trae cada pack y a qué
            precio en dinero es una decisión pendiente del fundador para la siguiente etapa. Los tamaños de arriba son
            provisionales; la compra con dinero aún no está activa.
          </p>
        </section>

        {/* ── FILA DE POTENCIADORES ──────────────────────────────────────── */}
        <section className="anima-plan-in" style={{ animationDelay: "0.1s" }}>
          <p className="text-[11px] font-semibold uppercase tracking-[1.2px] text-dim">Potencia tu idea</p>
          <div className="mt-4 grid gap-3.5 sm:grid-cols-2 lg:grid-cols-4">
            {/* Tus Números (azul, se paga por uso) */}
            <div className="flex flex-col gap-2.5 rounded-panel border border-accent/35 bg-surface p-[22px]">
              <div className="flex items-center justify-between">
                <svg
                  className="h-[18px] w-[18px] stroke-accent"
                  viewBox="0 0 24 24"
                  fill="none"
                  strokeWidth="2"
                  aria-hidden
                >
                  <line x1="6" y1="20" x2="6" y2="14" />
                  <line x1="12" y1="20" x2="12" y2="4" />
                  <line x1="18" y1="20" x2="18" y2="10" />
                </svg>
                <span className="rounded-full border border-accent/40 px-2.5 py-1 text-[11.5px] font-semibold text-accent">
                  {PRECIOS.tus_numeros} créditos
                </span>
              </div>
              <span className="text-[15px] font-semibold">Tus Números</span>
              <p className="text-[12.5px] leading-relaxed text-dim">
                Tus cifras reales convertidas en margen, punto de equilibrio y escenarios.
              </p>
              <span className="mt-auto pt-1 text-[12.5px] text-dim">Se paga por uso</span>
            </div>

            {/* Los 7 mundos: el preview es gratis (4.5); el PLAN se compra. */}
            {MUNDOS.map((m) => (
              <div key={m.nombre} className="flex flex-col gap-2.5 rounded-panel border border-hairline bg-surface p-[22px]">
                <div className="flex items-center justify-between">
                  <span className="h-2.5 w-2.5 rounded-full" style={{ background: PUNTO_MUNDO }} aria-hidden />
                  <span className="rounded-full border border-accent/40 px-2.5 py-1 text-[11.5px] font-semibold text-accent">
                    Preview gratis
                  </span>
                </div>
                <span className="text-[15px] font-semibold">{m.nombre}</span>
                <p className="text-[12.5px] leading-relaxed text-dim [text-wrap:pretty]">{m.promesa}</p>
                <span className="mt-auto pt-1 text-[12.5px] text-dim">Su plan: {PRECIOS.mundo_activar} créditos</span>
              </div>
            ))}
          </div>
        </section>

        {/* ── TUS NÚMEROS POR DENTRO + GUARDIÁN ÁMBAR ─────────────────────── */}
        <section className="anima-plan-in rounded-panel border border-hairline bg-surface p-7 sm:p-8" style={{ animationDelay: "0.2s" }}>
          <h2 className="text-lg font-bold">Tus Números, por dentro</h2>
          <p className="mt-2 max-w-2xl text-[14px] leading-relaxed text-dim">
            Los números los calcula código, no la IA: una calculadora determinística sobre las cifras que tú declaras. Punto
            de equilibrio, margen y tres escenarios, sin adivinar nada.
          </p>
          <div className="mt-5 grid gap-3.5 sm:grid-cols-3">
            {[
              { num: "170", etq: "margen por unidad, con tu costo de 180 y tu precio de 350" },
              { num: "8", etq: "unidades al mes para cubrir tus 1.200 de gasto fijo declarado" },
              { num: "3", etq: "escenarios: prudente, esperado y optimista, sobre tus mismas cifras" },
            ].map((c) => (
              <div key={c.etq} className="rounded-cinta border border-hairline px-5 py-4">
                <div className="text-[26px] font-extrabold tracking-tight">{c.num}</div>
                <div className="mt-1.5 text-[12.5px] leading-snug text-dim">{c.etq}</div>
              </div>
            ))}
          </div>
          <div className="mt-5 flex gap-3.5 rounded-cinta border border-warn/30 bg-warn/[0.06] px-5 py-4">
            <svg
              className="mt-0.5 h-[22px] w-[22px] flex-none stroke-warn"
              viewBox="0 0 24 24"
              fill="none"
              strokeWidth="2"
              strokeLinecap="round"
              strokeLinejoin="round"
              aria-hidden
            >
              <path d="M12 9v4" />
              <path d="M12 17h.01" />
              <path d="M10.3 3.9 1.8 18a2 2 0 0 0 1.7 3h17a2 2 0 0 0 1.7-3L13.7 3.9a2 2 0 0 0-3.4 0z" />
            </svg>
            <p className="text-[13.5px] leading-relaxed text-warn/90">
              <strong className="font-semibold text-warn">Guardián de datos.</strong> Estos números valen exactamente lo que
              valen las cifras que metiste. Si tu costo real cambia o tu gasto fijo está incompleto, el resultado cambia
              contigo. No sustituyen contabilidad formal ni asesoría fiscal.
            </p>
          </div>
        </section>
      </main>
    </div>
  );
}
