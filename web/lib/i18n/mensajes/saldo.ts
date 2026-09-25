/** El saldo de créditos: lib/textoSaldo.ts (chip del encabezado y barra de /creditos) y ui/ChipSaldo.tsx. */
import type { PorIdioma } from "../config";

const es = {
  creditos: { one: "{{n}} crédito", other: "{{n}} créditos" },
  reservados: { one: "{{n}} reservado para tu sesión en curso", other: "{{n}} reservados para tu sesión en curso" },
  tituloConReserva: "{{saldo}} disponibles · {{reservados}}",
  tituloChip: "Tus créditos",
};

const en: typeof es = {
  creditos: { one: "{{n}} credit", other: "{{n}} credits" },
  reservados: { one: "{{n}} reserved for your current session", other: "{{n}} reserved for your current session" },
  tituloConReserva: "{{saldo}} available · {{reservados}}",
  tituloChip: "Your credits",
};

export const SALDO: PorIdioma<typeof es> = { es, en };
