/**
 * /potenciadores — el centro de créditos (canon 3.6, mockup 07): la
 * estructura comercial real con precios en dinero por definir ("$ —",
 * stub hasta Stripe). Los costos en créditos vienen de precios.ts —
 * ninguna cifra hardcodeada. La moneda se llama "créditos", jamás
 * "tokens" (REGLAS_Y_TOKENS.md §3).
 */
import Link from "next/link";
import { PRECIOS } from "@/lib/precios";

const PACKS_CREDITOS = [
  { creditos: 5, para: "Para la idea que tienes entre manos", destacado: false },
  { creditos: 12, para: "Para quien tiene más de una idea rondando", destacado: true },
  { creditos: 30, para: "Para emprendedores en serie y mentores", destacado: false },
];

export default function Potenciadores() {
  return (
    <div className="flex min-h-full flex-1 flex-col">
      <header className="flex h-[58px] items-center gap-3 border-b border-hairline px-5 sm:px-6">
        <Link href="/ideas" className="text-[13px] text-dim hover:text-ink">
          Mis ideas /
        </Link>
        <span className="text-[14.5px] font-semibold">Potenciadores y créditos</span>
      </header>

      <main className="mx-auto w-full max-w-3xl flex-1 px-4 py-10 sm:px-6">
        <section className="anima-plan-in">
          <p className="text-[11px] font-semibold uppercase tracking-[1.2px] text-accent">
            Centro de créditos
          </p>
          <h1 className="mt-2 text-2xl font-bold tracking-tight">Tienes 0 créditos</h1>
          <p className="mt-3 max-w-xl text-[15px] leading-relaxed text-dim">
            Explorar una idea usa {PRECIOS.plan_completo} créditos · activar un mundo{" "}
            {PRECIOS.mundo_activar} · el seguimiento {PRECIOS.seguimiento} · Tus Números{" "}
            {PRECIOS.tus_numeros}. El organizador siempre es gratis.
          </p>
        </section>

        <div className="mt-8 grid gap-4 sm:grid-cols-3">
          {PACKS_CREDITOS.map((pack, i) => (
            <div
              key={pack.creditos}
              className={
                "anima-plan-in relative flex flex-col gap-2 rounded-panel border bg-surface p-6 " +
                (pack.destacado ? "border-accent/45" : "border-hairline")
              }
              style={{ animationDelay: `${0.15 + i * 0.1}s` }}
            >
              {pack.destacado && (
                <span className="absolute -top-3 left-5 rounded-full border border-accent/45 bg-bg px-3 py-1 text-[11px] font-bold text-accent">
                  Más elegido
                </span>
              )}
              <p className="text-xl font-bold">{pack.creditos} créditos</p>
              <p className="text-sm leading-relaxed text-dim">{pack.para}</p>
              <p className="mt-auto pt-3 text-2xl font-bold text-dim">$ —</p>
            </div>
          ))}
        </div>

        <p className="anima-plan-in mt-6 text-xs leading-relaxed text-dim" style={{ animationDelay: "0.5s" }}>
          Los potenciadores se activan con créditos dentro de cada idea. Precios y tamaños de pack por
          definir: esta estructura es la del catálogo real.
        </p>
      </main>
    </div>
  );
}
