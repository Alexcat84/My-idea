"use client";

/**
 * ChipSaldo — ETAPA 2 (canon 07): el saldo de créditos, discreto, en el
 * header. Solo aparece con cuenta real (la identidad invisible no tiene
 * ledger).
 *
 * AUD-09 M31 (decisión del fundador, 25 sep 2026): muestra lo DISPONIBLE (el
 * saldo menos lo reservado por una sesión en curso) y, si hay reserva activa,
 * lo dice. Se vuelve a pedir cada vez que la página sube `version` (al empezar
 * una sesión, al entregarse un plan): antes se quedaba con el número de la
 * carga y, tras cobrar un plan, seguía mostrando el saldo previo.
 */
import { useEffect, useState } from "react";
import Link from "next/link";
import { elegir } from "@/lib/i18n/config";
import { useIdioma } from "@/lib/i18n/IdiomaProvider";
import { interpolar } from "@/lib/i18n/interpolar";
import { SALDO } from "@/lib/i18n/mensajes/saldo";
import { textoChipSaldo } from "@/lib/textoSaldo";

export { textoChipSaldo };

export function ChipSaldo({ version = 0 }: { version?: number }) {
  const idioma = useIdioma();
  const t = elegir(SALDO, idioma);
  const [estado, setEstado] = useState<{ disponible: number; reservados: number } | null>(null);

  useEffect(() => {
    let vivo = true;
    fetch("/api/account/saldo")
      .then((r) => (r.ok ? r.json() : null))
      .then((d: { invisible?: boolean; disponible?: number | null; reservados?: number | null } | null) => {
        if (!vivo || !d || d.invisible) return;
        // Sin un disponible cierto no se pinta un número (AUD-09 M21).
        if (typeof d.disponible === "number") setEstado({ disponible: d.disponible, reservados: d.reservados ?? 0 });
        else setEstado(null);
      })
      .catch(() => {});
    return () => {
      vivo = false;
    };
  }, [version]);

  if (estado === null) return null;
  const texto = textoChipSaldo(estado.disponible, estado.reservados, idioma);
  // Canon 20 (lote 3): el cero va en GRIS, no en azul: informa sin presionar
  // ni alarmar; la puerta al frente es /creditos (el saldo es dinero, no
  // potenciadores: no mezclar procesos).
  const claseTono =
    estado.disponible === 0 ? "border-hairline text-dim hover:border-white/25" : "border-accent/40 text-accent hover:border-accent/70";
  return (
    <Link
      href="/creditos"
      className={`inline-flex shrink-0 items-center gap-1.5 rounded-full border px-3 py-1 text-[12px] font-semibold ${claseTono}`}
      title={texto.reservados ? interpolar(t.tituloConReserva, { saldo: texto.principal, reservados: texto.reservados }) : t.tituloChip}
    >
      {texto.principal}
      {texto.reservados && <span className="font-normal text-dim">· {texto.reservados}</span>}
    </Link>
  );
}
