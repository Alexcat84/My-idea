/**
 * /potenciadores — los ADD-ONS de las ideas (regla del fundador: no mezclar
 * procesos, y esto NO vive en el menú principal). Se llega desde el final de
 * la lista de ideas ("Potenciar mis ideas") y el flujo es en dos pasos:
 *   1. ¿Qué idea quieres potenciar?  (solo tiene sentido con ideas ya creadas)
 *   2. ¿Qué potenciador? (Tus Números o un mundo) → se activa dentro de la
 *      idea, en Manos a la Obra, que es donde vive su desarrollo.
 *
 * Aquí NO vive el dinero (saldo, packs, tabla de costos): eso es /creditos.
 * Los precios se LEEN de precios.ts, jamás hardcodeados.
 */
import Link from "next/link";
import { redirect } from "next/navigation";
import catalogo from "@/lib/assets/packs_catalog.json";
import { esInvitadoInvisible } from "@/lib/identidad";
import { PRECIOS } from "@/lib/precios";
import { createClient } from "@/lib/supabase/server";

export const dynamic = "force-dynamic";

const MUNDOS = (catalogo.packs as Array<{ clave: string; nombre: string; promesa: string }>).map((p) => ({
  nombre: p.nombre,
  promesa: p.promesa,
}));

const PUNTO_MUNDO = "#3A9B8F"; // matiz de los mundos (ni azul ni verde)

function Cabecera({ titulo }: { titulo: string }) {
  return (
    <header className="flex h-[58px] items-center gap-3 border-b border-hairline px-5 sm:px-6">
      <Link href="/ideas" className="text-[13px] text-dim hover:text-ink">
        Mis ideas /
      </Link>
      <span className="text-[14.5px] font-semibold">{titulo}</span>
    </header>
  );
}

export default async function Potenciadores({
  searchParams,
}: {
  searchParams: Promise<Record<string, string | string[] | undefined>>;
}) {
  const sp = await searchParams;
  const ideaId = typeof sp.idea === "string" ? sp.idea : null;

  const supabase = await createClient();
  const {
    data: { user },
  } = await supabase.auth.getUser();
  if (!user || esInvitadoInvisible(user)) redirect("/login");

  // ── PASO 1: ¿qué idea quieres potenciar? ────────────────────────────────
  if (!ideaId) {
    const { data: proyectos } = await supabase
      .from("projects")
      .select("id, titulo, entrada_original")
      .order("created_at", { ascending: false });
    const ideas = ((proyectos ?? []) as Array<{ id: string; titulo: string | null; entrada_original: string }>).map(
      (p) => ({ id: p.id, nombre: (p.titulo ?? p.entrada_original ?? "Idea sin título").slice(0, 90) })
    );

    return (
      <div className="flex min-h-full flex-1 flex-col">
        <Cabecera titulo="Potenciar" />
        <main className="mx-auto w-full max-w-2xl flex-1 px-4 py-10 sm:px-6">
          <h1 className="text-2xl font-bold tracking-tight">¿Qué idea quieres potenciar?</h1>
          {ideas.length === 0 ? (
            <p className="mt-3 text-[15px] text-dim">
              Los potenciadores se suman a una idea. Cuando tengas la primera, aquí podrás elegirla.
            </p>
          ) : (
            <>
              <p className="mt-2 text-[15px] leading-relaxed text-dim">
                Elige una y después escoges el potenciador.
              </p>
              <ul className="mt-6 flex flex-col gap-3">
                {ideas.map((idea) => (
                  <li key={idea.id}>
                    <Link
                      href={`/potenciadores?idea=${idea.id}`}
                      className="flex items-center justify-between gap-3 rounded-panel border border-hairline bg-surface px-5 py-4 hover:border-accent/55"
                    >
                      <span className="min-w-0 flex-1 truncate text-[15px] font-semibold">{idea.nombre}</span>
                      <svg width="13" height="13" viewBox="0 0 12 12" aria-hidden className="shrink-0">
                        <path d="M4 2l4 4-4 4" stroke="var(--text-dim)" strokeWidth="1.5" fill="none" />
                      </svg>
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

  // ── PASO 2: ¿qué potenciador para esa idea? ─────────────────────────────
  // RLS: si la idea no es suya (o no existe), no la ve.
  const { data: proyecto } = await supabase
    .from("projects")
    .select("id, titulo, entrada_original")
    .eq("id", ideaId)
    .maybeSingle();
  if (!proyecto) redirect("/potenciadores");
  const nombreIdea = (
    (proyecto as { titulo: string | null; entrada_original: string }).titulo ??
    (proyecto as { entrada_original: string }).entrada_original ??
    "tu idea"
  ).slice(0, 90);
  const irAlaIdea = `/idea/${ideaId}?vista=manos`;

  return (
    <div className="flex min-h-full flex-1 flex-col">
      <Cabecera titulo="Potenciar" />
      <main className="mx-auto flex w-full max-w-4xl flex-1 flex-col gap-8 px-4 py-10 sm:px-6">
        <section className="anima-plan-in">
          <Link href="/potenciadores" className="text-[13px] text-dim hover:text-ink">
            ← Cambiar de idea
          </Link>
          <h1 className="mt-2 text-2xl font-bold tracking-tight">¿Qué potenciador quieres usar?</h1>
          <p className="mt-2 max-w-2xl text-[15px] leading-relaxed text-dim">
            Para <span className="font-semibold text-ink">{nombreIdea}</span>. Los mundos se exploran gratis y solo
            pagas su plan si decides activarlo.
          </p>

          <div className="mt-6 grid gap-3.5 sm:grid-cols-2 lg:grid-cols-4">
            {/* Tus Números (azul, se paga por uso) */}
            <Link
              href={irAlaIdea}
              className="flex flex-col gap-2.5 rounded-panel border border-accent/35 bg-surface p-[22px] hover:border-accent/60"
            >
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
            </Link>

            {/* Los 7 mundos: el preview es gratis (4.5); el PLAN se compra. */}
            {MUNDOS.map((m) => (
              <Link
                key={m.nombre}
                href={irAlaIdea}
                className="flex flex-col gap-2.5 rounded-panel border border-hairline bg-surface p-[22px] hover:border-accent/45"
              >
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
              </Link>
            ))}
          </div>
        </section>
      </main>
    </div>
  );
}
