/**
 * Home: "Mis ideas" (brief 2.2) — lista vertical de cintas, una por
 * idea, con nombre, última actividad y mini-estado. Server Component:
 * lee directo de Supabase con la sesión del usuario (proxy.ts ya
 * garantizó que hay usuario, anónimo si hizo falta).
 *
 * Web abierta: al visitante nuevo (cero ideas) no se le muestra una
 * lista vacía — se le lleva directo a la captura, que es la puerta de
 * la experiencia. "Salir" solo aparece para cuentas con email: a un
 * usuario anónimo cerrarle la sesión le dejaría sus ideas huérfanas.
 */
import Link from "next/link";
import { redirect } from "next/navigation";
import { haceCuanto, listarIdeasConEstado, type EstadoIdea } from "@/lib/ideas";
import { createClient } from "@/lib/supabase/server";
import { BotonSalir } from "./ui/BotonSalir";

export const dynamic = "force-dynamic";

function ChipEstado({ estado }: { estado: EstadoIdea }) {
  const activo = estado === "En entrevista";
  return (
    <span
      className={
        "rounded-full px-2.5 py-0.5 text-xs " +
        (activo ? "bg-accent-soft text-accent" : "border border-hairline text-dim")
      }
    >
      {estado}
    </span>
  );
}

export default async function Home() {
  const supabase = await createClient();
  const [ideas, { data: auth }] = await Promise.all([
    listarIdeasConEstado(supabase),
    supabase.auth.getUser(),
  ]);
  const esAnonimo = auth.user?.is_anonymous ?? true;

  if (ideas.length === 0) redirect("/nueva");

  return (
    <main className="mx-auto flex w-full max-w-2xl flex-1 flex-col px-4 py-8 sm:px-6">
      <header className="mb-8 flex items-center justify-between">
        <h1 className="text-2xl font-semibold tracking-tight">Mis ideas</h1>
        <div className="flex items-center gap-5">
          {!esAnonimo && <BotonSalir />}
          <Link
            href="/nueva"
            className="rounded-cinta bg-accent px-4 py-2 font-medium text-white hover:opacity-90"
          >
            Nueva idea
          </Link>
        </div>
      </header>

      <ul className="flex flex-col gap-3">
        {ideas.map((idea) => (
          <li key={idea.id}>
            <Link
              href={`/idea/${idea.id}`}
              className="block rounded-cinta border border-hairline bg-surface px-5 py-4 hover:bg-surface-2"
            >
              <div className="flex items-start justify-between gap-3">
                <p className="font-medium leading-snug">{idea.nombre}</p>
                <ChipEstado estado={idea.estado} />
              </div>
              <p className="mt-1.5 text-xs text-dim">{haceCuanto(idea.actualizado)}</p>
            </Link>
          </li>
        ))}
      </ul>
    </main>
  );
}
