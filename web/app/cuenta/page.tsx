/**
 * /cuenta: el centro de cuenta (réplica del panel de opciones del I Ching,
 * en pantalla propia): identidad, seguridad en dos pasos (TOTP + correo),
 * créditos (saldo + puerta a /potenciadores, decisión del fundador: el
 * centro de créditos sigue siendo /potenciadores), borrar ideas concretas
 * y borrar la cuenta completa. Solo cuentas reales: la identidad invisible
 * no tiene cuenta que administrar.
 */
import Link from "next/link";
import { redirect } from "next/navigation";
import { esInvitadoInvisible } from "@/lib/identidad";
import { createClient } from "@/lib/supabase/server";
import { BotonSalir } from "../ui/BotonSalir";
import { CuentaCliente } from "../ui/CuentaCliente";

export const dynamic = "force-dynamic";

export default async function Cuenta() {
  const supabase = await createClient();
  const {
    data: { user },
  } = await supabase.auth.getUser();
  if (!user || esInvitadoInvisible(user)) redirect("/login");

  const [{ data: cuenta }, { data: proyectos }] = await Promise.all([
    supabase.from("credit_accounts").select("creditos_total").maybeSingle(),
    supabase.from("projects").select("id, titulo, entrada_original, created_at").order("created_at", { ascending: false }),
  ]);
  const saldo = (cuenta as { creditos_total: number } | null)?.creditos_total ?? 0;
  const ideas = (
    (proyectos ?? []) as Array<{ id: string; titulo: string | null; entrada_original: string; created_at: string }>
  ).map(
    (p) => ({
      id: p.id,
      nombre: (p.titulo ?? p.entrada_original ?? "Idea sin título").slice(0, 90),
      fecha: new Date(p.created_at).toLocaleDateString("es", { day: "numeric", month: "short", year: "numeric" }),
    })
  );

  // Métodos con los que esta cuenta puede entrar (Supabase los vincula por
  // email verificado).
  const proveedores = ((user.app_metadata?.providers as string[] | undefined) ?? [])
    .map((p) => (p === "google" ? "Google" : p === "email" ? "Código por correo" : p))
    .filter((v, i, a) => a.indexOf(v) === i);

  return (
    <div className="flex min-h-full flex-1 flex-col">
      <header className="flex h-[58px] items-center gap-5 border-b border-hairline px-5 sm:px-6">
        <Link href="/ideas" className="text-base font-extrabold tracking-tight">
          My <span className="text-accent">Idea</span>
        </Link>
        <span className="flex-1" />
        <Link
          href="/potenciadores"
          className={`inline-flex shrink-0 items-center rounded-full border px-3 py-1 text-[12px] font-semibold ${saldo === 0 ? "border-hairline text-dim hover:border-white/25" : "border-accent/40 text-accent hover:border-accent/70"}`}
          title="Tus créditos"
        >
          {saldo} {saldo === 1 ? "crédito" : "créditos"}
        </Link>
        <Link href="/ideas" className="text-[13.5px] text-dim hover:text-ink">
          Mis ideas
        </Link>
        <BotonSalir />
      </header>

      <main className="mx-auto w-full max-w-2xl flex-1 px-4 py-10 sm:px-6">
        <h1 className="text-2xl font-bold tracking-tight">Tu cuenta</h1>
        <CuentaCliente email={user.email ?? ""} proveedores={proveedores} saldo={saldo} ideas={ideas} />
      </main>
    </div>
  );
}
