/**
 * "/" — la landing pública (Fase 3.4): el diseño canónico del fundador,
 * portado 1:1 en ui/Landing.tsx. Ruta pública: proxy.ts NO crea sesión
 * aquí (los bots/crawlers no acuñan usuarios); la identidad invisible
 * nace cuando el visitante entra a /nueva con el CTA. "Mis ideas" vive
 * ahora en /ideas.
 */
import { redirect } from "next/navigation";
import { Landing } from "./ui/Landing";
import { esInvitadoInvisible } from "@/lib/identidad";
import { createClient } from "@/lib/supabase/server";

export const metadata = {
  title: "My Idea — Transforma tu creatividad en acción",
  description:
    "A los emprendedores no les faltan ideas. Les falta un interlocutor serio. Cuéntala, recibe tu plan y ejecútalo.",
};

export default async function PaginaPublica({
  searchParams,
}: {
  searchParams: Promise<Record<string, string | string[] | undefined>>;
}) {
  const sp = await searchParams;

  // RED DE SEGURIDAD del login: si un flujo de auth (Google, confirmación de
  // registro, recuperación) devolvió el ?code= a la HOME en vez de a
  // /auth/callback —Supabase cae al Site URL cuando el redirect_to no casa la
  // allowlist, p.ej. entrar por el dominio apex sin su /auth/callback— lo
  // reenviamos al callback para que canjee la sesión. Sin esto, el código
  // queda tirado en la portada y el login "no hace nada".
  const code = typeof sp.code === "string" ? sp.code : null;
  if (code) {
    const params = new URLSearchParams({ code });
    if (typeof sp.type === "string") params.set("type", sp.type);
    redirect(`/auth/callback?${params.toString()}`);
  }

  // ETAPA 2 (§6 navegación): con sesión real, el nav ofrece "Mis ideas".
  // Leer la sesión aquí NO acuña identidad (eso sigue siendo cosa de /nueva).
  const supabase = await createClient();
  const {
    data: { user },
  } = await supabase.auth.getUser();
  const sesionActiva = Boolean(user && !esInvitadoInvisible(user));
  return <Landing sesionActiva={sesionActiva} />;
}
