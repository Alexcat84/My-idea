/** El saldo de créditos: lib/textoSaldo.ts (chip del encabezado y barra de /creditos) y ui/ChipSaldo.tsx. */
import type { PorIdioma } from "../config";

const es = {
  creditos: { one: "{{n}} crédito", other: "{{n}} créditos" },
  reservados: { one: "{{n}} reservado para tu sesión en curso", other: "{{n}} reservados para tu sesión en curso" },
  tituloConReserva: "{{saldo}} disponibles · {{reservados}}",
  tituloChip: "Tus créditos",
};

export const SALDO: PorIdioma<typeof es> = { es };
