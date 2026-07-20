"use client";

/**
 * ChipSaldo — ETAPA 2 (canon 07): el saldo de créditos, discreto, en el
 * header. Solo aparece con cuenta real (la identidad invisible no tiene
 * ledger). Se refresca al montarse y cuando la página lo pide vía la prop
 * `saldo` (las entregas devuelven creditos_restantes).
 */
import { useEffect, useState } from "react";
import Link from "next/link";

export function ChipSaldo({ saldo: saldoProp }: { saldo?: number | null }) {
  const [saldoFetch, setSaldoFetch] = useState<number | null>(null);

  useEffect(() => {
    if (typeof saldoProp === "number") return; // el padre manda el saldo
    let vivo = true;
    fetch("/api/account/saldo")
      .then((r) => (r.ok ? r.json() : null))
      .then((d: { invisible?: boolean; saldo?: number | null } | null) => {
        if (vivo && d && !d.invisible && typeof d.saldo === "number") setSaldoFetch(d.saldo);
      })
      .catch(() => {});
    return () => {
      vivo = false;
    };
  }, [saldoProp]);

  // El prop (si viene) manda; si no, lo que trajo el fetch.
  const saldo = typeof saldoProp === "number" ? saldoProp : saldoFetch;

  if (saldo === null) return null;
  // Canon 20 (lote 3): el cero va en GRIS, no en azul: informa sin presionar
  // ni alarmar; la puerta al frente sigue siendo /potenciadores.
  const claseTono = saldo === 0 ? "border-hairline text-dim hover:border-white/25" : "border-accent/40 text-accent hover:border-accent/70";
  return (
    <Link
      href="/potenciadores"
      className={`inline-flex shrink-0 items-center gap-1.5 rounded-full border px-3 py-1 text-[12px] font-semibold ${claseTono}`}
      title="Tus créditos"
    >
      {saldo} {saldo === 1 ? "crédito" : "créditos"}
    </Link>
  );
}
