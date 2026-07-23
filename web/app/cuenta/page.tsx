/**
 * /cuenta: el centro de cuenta = SOLO opciones de cuenta (regla del fundador:
 * no mezclar procesos). Identidad, seguridad en dos pasos (TOTP + correo) y
 * borrar la cuenta. Los créditos viven en /creditos y las ideas en /ideas:
 * aquí NO aparecen. Solo cuentas reales: la identidad invisible no tiene
 * cuenta que administrar.
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

  return (
    <div className="flex min-h-full flex-1 flex-col">
      <header className="flex h-[58px] items-center gap-5 border-b border-hairline px-5 sm:px-6">
        <Link href="/ideas" className="text-base font-extrabold tracking-tight">
          My <span className="text-accent">Idea</span>
        </Link>
        <span className="flex-1" />
        <Link href="/ideas" className="text-[13.5px] text-dim hover:text-ink">
          Mis ideas
        </Link>
        <BotonSalir />
      </header>

      <main className="mx-auto w-full max-w-2xl flex-1 px-4 py-10 sm:px-6">
        <h1 className="text-2xl font-bold tracking-tight">Tu cuenta</h1>
        <CuentaCliente email={user.email ?? ""} />
      </main>
    </div>
  );
}
