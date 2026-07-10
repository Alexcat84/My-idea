"use client";

import { useRouter } from "next/navigation";
import { createClient } from "@/lib/supabase/client";

export function BotonSalir() {
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
      Salir
    </button>
  );
}
