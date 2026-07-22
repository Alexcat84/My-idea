/**
 * /potenciadores — los ADD-ONS de las ideas, nada más (regla del fundador:
 * no mezclar procesos). Aquí viven Tus Números y los 7 mundos: lo que
 * potencia una idea, con su costo en créditos. NO vive aquí el dinero (saldo,
 * packs, "un crédito es un dólar", tabla de costos) — eso es /creditos — ni
 * el desarrollo de Tus Números (el explicador "por dentro", el guardián de
 * datos), que pertenece a la pantalla de Tus Números dentro de cada idea.
 *
 * Los precios se LEEN de precios.ts (jamás hardcodeados). El preview de un
 * mundo es gratis (4.5); su PLAN cuesta su precio de catálogo.
 */
import Link from "next/link";
import catalogo from "@/lib/assets/packs_catalog.json";
import { PRECIOS } from "@/lib/precios";

const MUNDOS = (catalogo.packs as Array<{ clave: string; nombre: string; promesa: string }>).map((p) => ({
  nombre: p.nombre,
  promesa: p.promesa,
}));

const PUNTO_MUNDO = "#3A9B8F"; // matiz de los mundos (ni azul ni verde)

export default function Potenciadores() {
  return (
    <div className="flex min-h-full flex-1 flex-col">
      <header className="flex h-[58px] items-center gap-3 border-b border-hairline px-5 sm:px-6">
        <Link href="/ideas" className="text-[13px] text-dim hover:text-ink">
          Mis ideas /
        </Link>
        <span className="text-[14.5px] font-semibold">Potenciadores</span>
      </header>

      <main className="mx-auto flex w-full max-w-4xl flex-1 flex-col gap-8 px-4 py-10 sm:px-6">
        <section className="anima-plan-in">
          <h1 className="text-2xl font-bold tracking-tight">Potencia tu idea</h1>
          <p className="mt-2 max-w-2xl text-[15px] leading-relaxed text-dim">
            Herramientas que se suman a una idea cuando la necesitas. Cada una tiene su costo en créditos; los mundos se
            exploran gratis y solo pagas su plan si decides activarlo.
          </p>

          <div className="mt-6 grid gap-3.5 sm:grid-cols-2 lg:grid-cols-4">
            {/* Tus Números (azul, se paga por uso) */}
            <div className="flex flex-col gap-2.5 rounded-panel border border-accent/35 bg-surface p-[22px]">
              <div className="flex items-center justify-between">
                <svg className="h-[18px] w-[18px] stroke-accent" viewBox="0 0 24 24" fill="none" strokeWidth="2" aria-hidden>
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
                    Explóralo gratis
                  </span>
                </div>
                <span className="text-[15px] font-semibold">{m.nombre}</span>
                <p className="text-[12.5px] leading-relaxed text-dim [text-wrap:pretty]">{m.promesa}</p>
                <span className="mt-auto pt-1 text-[12.5px] text-dim">
                  El preview es gratis · su plan: {PRECIOS.mundo_activar} créditos
                </span>
              </div>
            ))}
          </div>
        </section>
      </main>
    </div>
  );
}
