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
  const [saldo, setSaldo] = useState<number | null>(saldoProp ?? null);

  useEffect(() => {
    if (typeof saldoProp === "number") {
      setSaldo(saldoProp);
      return;
    }
    let vivo = true;
    fetch("/api/account/saldo")
      .then((r) => (r.ok ? r.json() : null))
      .then((d: { invisible?: boolean; saldo?: number | null } | null) => {
        if (vivo && d && !d.invisible && typeof d.saldo === "number") setSaldo(d.saldo);
      })
      .catch(() => {});
    return () => {
      vivo = false;
    };
  }, [saldoProp]);

  if (saldo === null) return null;
  return (
    <Link
      href="/potenciadores"
      className="inline-flex shrink-0 items-center gap-1.5 rounded-full border border-accent/40 px-3 py-1 text-[12px] font-semibold text-accent hover:border-accent/70"
      title="Tus créditos"
    >
      {saldo} {saldo === 1 ? "crédito" : "créditos"}
    </Link>
  );
}
