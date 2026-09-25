"use client";

import { useRouter } from "next/navigation";
import { elegir } from "@/lib/i18n/config";
import { useIdioma } from "@/lib/i18n/IdiomaProvider";
import { SESION } from "@/lib/i18n/mensajes/sesion";
import { createClient } from "@/lib/supabase/client";

export function BotonSalir() {
  const t = elegir(SESION, useIdioma());
  const router = useRouter();
  return (
    <button
      onClick={async () => {
        await createClient().auth.signOut();
        // A la landing pública: es la puerta de la casa desde Fase 3.4.
        router.push("/");
        router.refresh();
      }}
      className="text-sm text-dim hover:text-ink"
    >
      {t.salir}
    </button>
  );
}
