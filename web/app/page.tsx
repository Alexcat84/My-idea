/**
 * "/" — la landing pública (Fase 3.4): el diseño canónico del fundador,
 * portado 1:1 en ui/Landing.tsx. Ruta pública: proxy.ts NO crea sesión
 * aquí (los bots/crawlers no acuñan usuarios); la identidad invisible
 * nace cuando el visitante entra a /nueva con el CTA. "Mis ideas" vive
 * ahora en /ideas.
 */
import { Landing } from "./ui/Landing";
import { esInvitadoInvisible } from "@/lib/identidad";
import { createClient } from "@/lib/supabase/server";

export const metadata = {
  title: "My Idea — Transforma tu creatividad en acción",
  description:
    "A los emprendedores no les faltan ideas. Les falta un interlocutor serio. Cuéntala, recibe tu plan y ejecútalo.",
};

export default async function PaginaPublica() {
  // ETAPA 2 (§6 navegación): con sesión real, el nav ofrece "Mis ideas".
  // Leer la sesión aquí NO acuña identidad (eso sigue siendo cosa de /nueva).
  const supabase = await createClient();
  const {
    data: { user },
  } = await supabase.auth.getUser();
  const sesionActiva = Boolean(user && !esInvitadoInvisible(user));
  return <Landing sesionActiva={sesionActiva} />;
}
