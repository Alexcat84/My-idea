/**
 * /ideas: "Mis ideas" — el home de cintas (canon 3.6, mockup 01): barra
 * con el logo y Potenciadores, saludo con captura rápida (La Chispa
 * embebida), y una cinta por idea con su mini-stepper de 5 puntos, su
 * chip de estado y su pista. Server Component: lee directo de Supabase
 * con la sesión del usuario (proxy.ts ya garantizó que hay usuario).
 *
 * REGLA DE ORO: el mini-stepper y los chips solo muestran verdad
 * persistida del motor (lib/ideas.ts las deriva; aquí solo se pintan).
 * Al visitante nuevo (cero ideas) se le lleva directo a la captura.
 * "Salir" solo aparece para cuentas con email.
 */
import Link from "next/link";
import { redirect } from "next/navigation";
import { listarIdeasConEstado, type ChipCinta } from "@/lib/ideas";
import { createClient } from "@/lib/supabase/server";
import { BotonSalir } from "../ui/BotonSalir";
import { Saludo } from "../ui/Saludo";
import { StepperMini } from "../ui/Stepper";

export const dynamic = "force-dynamic";

function Chip({ chip }: { chip: ChipCinta }) {
  const tono =
    chip.tono === "verde"
      ? "border-done/45 text-done"
      : chip.tono === "azul"
        ? "border-accent/45 text-accent"
        : "border-white/20 text-ink";
  return (
    <span className={`inline-flex items-center rounded-full border px-3.5 py-1.5 text-[12.5px] font-bold ${tono}`}>
      {chip.texto}
    </span>
  );
}

export default async function MisIdeas() {
  const supabase = await createClient();
  const [ideas, { data: auth }] = await Promise.all([
    listarIdeasConEstado(supabase),
    supabase.auth.getUser(),
  ]);
  // Anónimo de Supabase o invitado bootstrapeado por el proxy: para
  // ambos, "Salir" les dejaría las ideas huérfanas — no se muestra.
  const esAnonimo = (auth.user?.is_anonymous ?? true) || auth.user?.user_metadata?.invitado === true;

  // ETAPA 2: el saldo del chip (canon 07), leído con RLS own-select. Solo
  // para cuentas reales: la identidad invisible no tiene ledger.
  let saldo: number | null = null;
  if (!esAnonimo) {
    const { data: cuenta } = await supabase.from("credit_accounts").select("creditos_total").maybeSingle();
    saldo = (cuenta as { creditos_total: number } | null)?.creditos_total ?? 0;
  }

  if (ideas.length === 0) redirect("/nueva");

  // Fase 3.8: las realizadas reposan al final, bajo su propio encabezado.
  const activas = ideas.filter((i) => !i.realizada);
  const realizadas = ideas.filter((i) => i.realizada);

  return (
    <div className="flex min-h-full flex-1 flex-col">
      <header className="flex h-[58px] items-center gap-5 border-b border-hairline px-5 sm:px-6">
        <Link href="/ideas" className="text-base font-extrabold tracking-tight">
          My <span className="text-accent">idea</span>
        </Link>
        <span className="flex-1" />
        {saldo !== null && (
          <Link
            href="/potenciadores"
            className={`inline-flex shrink-0 items-center rounded-full border px-3 py-1 text-[12px] font-semibold ${saldo === 0 ? "border-hairline text-dim hover:border-white/25" : "border-accent/40 text-accent hover:border-accent/70"}`}
            title="Tus créditos"
          >
            {saldo} {saldo === 1 ? "crédito" : "créditos"}
          </Link>
        )}
        <Link href="/potenciadores" className="text-[13.5px] text-dim hover:text-ink">
          Potenciadores
        </Link>
        {!esAnonimo && (
          <Link href="/cuenta" className="text-[13.5px] text-dim hover:text-ink">
            Cuenta
          </Link>
        )}
        {!esAnonimo && <BotonSalir />}
      </header>

      <main className="mx-auto w-full max-w-3xl flex-1 px-4 py-10 sm:px-6">
        <h1 className="anima-plan-in text-2xl font-bold tracking-tight">
          <Saludo />
        </h1>

        {/* Captura rápida: La Chispa embebida — el campo real vive en /nueva */}
        <Link
          href="/nueva"
          className="anima-plan-in mt-4 flex items-center gap-3.5 rounded-[14px] border border-accent/30 bg-surface px-5 py-4 hover:border-accent/55"
          style={{ animationDelay: "0.1s" }}
        >
          <span className="flex-1 text-[15px] text-dim">Cuéntame una idea nueva, o en qué punto estás con ella…</span>
          <span className="flex h-9 w-9 shrink-0 items-center justify-center rounded-full border-[1.5px] border-accent/55">
            <svg width="15" height="15" viewBox="0 0 16 16" fill="none" aria-hidden>
              <rect x="6" y="1.5" width="4" height="7.5" rx="2" fill="var(--accent)" />
              <path d="M3.5 8a4.5 4.5 0 0 0 9 0" stroke="var(--accent)" strokeWidth="1.4" fill="none" />
              <line x1="8" y1="12.6" x2="8" y2="14.5" stroke="var(--accent)" strokeWidth="1.4" />
            </svg>
          </span>
        </Link>

        <p
          className="anima-plan-in mb-4 mt-10 text-[11px] font-semibold uppercase tracking-[1.2px] text-dim"
          style={{ animationDelay: "0.2s" }}
        >
          Tus ideas · {activas.length}
        </p>

        <ul className="flex flex-col gap-3.5">
          {activas.map((idea, i) => (
            <li key={idea.id} className="anima-plan-in" style={{ animationDelay: `${0.3 + i * 0.1}s` }}>
              <Link
                // C0: una idea ya en Manos a la Obra entra directo a la
                // etapa 5 (checklist + mundos), no al documento del plan.
                href={idea.etapa === 5 ? `/idea/${idea.id}?vista=manos` : `/idea/${idea.id}`}
                className={
                  "block rounded-panel border bg-surface px-5 py-5 sm:px-6 " +
                  (idea.etapa === 5
                    ? "border-done/30 hover:border-done/60"
                    : "border-hairline hover:border-accent/55")
                }
                data-transiciona
              >
                {/* canon 01 mobile: título · stepper+chips · pista, apilados;
                    en desktop el bloque de chips pasa a la derecha */}
                <div className="flex items-center gap-3">
                  <p className="min-w-0 flex-1 text-[15px] font-semibold leading-snug sm:text-[17px]">
                    {idea.nombre}
                  </p>
                  <svg width="13" height="13" viewBox="0 0 12 12" aria-hidden className="shrink-0">
                    <path d="M4 2l4 4-4 4" stroke="var(--text-dim)" strokeWidth="1.5" fill="none" />
                  </svg>
                </div>
                <div className="mt-3 flex flex-wrap items-center gap-x-4 gap-y-2">
                  <StepperMini etapa={idea.etapa} pensando={idea.pensando} />
                  <span className="flex flex-1 flex-wrap justify-end gap-1.5">
                    {idea.chips.map((chip) => (
                      <Chip key={chip.texto} chip={chip} />
                    ))}
                  </span>
                </div>
                <p className="mt-2 text-xs text-dim">{idea.pista}</p>
              </Link>
            </li>
          ))}
        </ul>

        {/* Fase 3.8 §5 — Realizadas: más serenas, sin stepper ni pulso, con
            el distintivo "Proyecto" de forma. Reposan al final. */}
        {realizadas.length > 0 && (
          <>
            <p className="mb-4 mt-12 text-[11px] font-semibold uppercase tracking-[1.2px] text-dim">
              Realizadas · {realizadas.length}
            </p>
            <ul className="flex flex-col gap-3.5">
              {realizadas.map((idea) => (
                <li key={idea.id}>
                  <Link
                    href={`/idea/${idea.id}?vista=celebracion`}
                    className="block rounded-panel border border-hairline bg-surface/60 px-5 py-4 opacity-90 hover:border-done/50 hover:opacity-100 sm:px-6"
                  >
                    <div className="flex items-center justify-between gap-3">
                      <p className="min-w-0 flex-1 truncate text-[15px] font-semibold sm:text-[16px]">{idea.nombre}</p>
                      <span className="inline-flex shrink-0 items-center gap-1 rounded-full border border-done/45 px-2.5 py-1 text-[11px] font-bold text-done">
                        <svg width="9" height="9" viewBox="0 0 12 12" aria-hidden>
                          <path d="M2.5 6.5l2.5 2.5 4.5-5.5" stroke="var(--done)" strokeWidth="2" fill="none" />
                        </svg>
                        Proyecto
                      </span>
                    </div>
                    {idea.resumenRealizada && <p className="mt-1.5 text-xs text-dim">{idea.resumenRealizada}</p>}
                  </Link>
                </li>
              ))}
            </ul>
          </>
        )}
      </main>
    </div>
  );
}
