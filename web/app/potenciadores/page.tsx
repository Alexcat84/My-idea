/**
 * /potenciadores — los ADD-ONS de las ideas (regla del fundador: no mezclar
 * procesos, y esto NO vive en el menú principal). Se llega desde el final de
 * la lista de ideas ("Potenciar mis ideas") y hace UNA sola cosa: elegir la
 * idea. Con la idea elegida, muestra la pantalla enfocada de ELEGIR EL
 * POTENCIADOR, que renderiza la ÚNICA fila real (PotenciaTuIdea): aplicarlo lo
 * agrega al menú de la idea y desde ahí todo sigue igual.
 *
 * Por qué redirección y no una segunda parrilla (decisión del fundador, ago
 * 2026, no discutible): esta página tuvo su propia copia de las tarjetas y se
 * quedó DOS campañas atrás sin que nadie lo notara, mintiendo el catálogo en
 * vivo (el chip de explorar que ya había muerto, y el potenciador incluido
 * pintado como de pago). No debe haber dos versiones de lo mismo: una sola
 * fuente de verdad y el resto redirige a ella. El contrato vive en
 * page.test.ts y falla si a esta página le vuelve a crecer una parrilla.
 */
import Link from "next/link";
import { redirect } from "next/navigation";
import { ElegirPotenciador } from "./ElegirPotenciador";
import { esInvitadoInvisible } from "@/lib/identidad";
import { createClient } from "@/lib/supabase/server";

export const dynamic = "force-dynamic";

function Cabecera({ titulo }: { titulo: string }) {
  return (
    <header className="sticky top-0 z-30 flex h-[58px] items-center gap-3 border-b border-hairline px-5 sm:px-6" style={{ background: "rgba(0,0,0,0.82)", backdropFilter: "blur(14px)", WebkitBackdropFilter: "blur(14px)" }}>
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

  // Con idea elegida: la pantalla enfocada de elegir potenciador. RLS: si la
  // idea no es suya (o no existe), vuelve a elegir. La parrilla que se pinta
  // ahí es EL MISMO componente de la idea (PotenciaTuIdea), no una copia.
  if (ideaId) {
    const { data: proyecto } = await supabase.from("projects").select("id").eq("id", ideaId).maybeSingle();
    if (!proyecto) redirect("/potenciadores");
    return (
      <div className="flex min-h-full flex-1 flex-col">
        <Cabecera titulo="Potenciar" />
        <main className="mx-auto flex w-full max-w-4xl flex-1 flex-col px-4 py-10 sm:px-6">
          <ElegirPotenciador ideaId={ideaId} />
        </main>
      </div>
    );
  }

  // ── El único paso propio: ¿qué idea quieres potenciar? ──────────────────
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
              Elige una y te llevo a sus potenciadores.
            </p>
            {/* Las filas hablan el MISMO idioma visual que la lista normal de
                /ideas (mismo contenedor, mismo cuerpo, misma pista): este es un
                acceso distinto, no un menú distinto. */}
            <ul className="mt-6 flex flex-col gap-3.5">
              {ideas.map((idea) => (
                <li key={idea.id}>
                  <Link
                    href={`/potenciadores?idea=${idea.id}`}
                    className="block rounded-panel border border-hairline bg-surface px-5 py-5 hover:border-accent/55 sm:px-6"
                  >
                    <div className="flex items-center gap-3">
                      <p className="min-w-0 flex-1 text-[15px] font-semibold leading-snug sm:text-[17px]">
                        {idea.nombre}
                      </p>
                      <svg width="13" height="13" viewBox="0 0 12 12" aria-hidden className="shrink-0">
                        <path d="M4 2l4 4-4 4" stroke="var(--text-dim)" strokeWidth="1.5" fill="none" />
                      </svg>
                    </div>
                    <p className="mt-2 text-xs text-dim">Añádele un mundo o revisa sus potenciadores.</p>
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
