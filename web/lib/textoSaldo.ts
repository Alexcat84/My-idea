/**
 * AUD-09 M31 (decisión del fundador, 25 sep 2026): el texto del saldo que se
 * puede gastar. Una sola fuente para el chip del encabezado (cliente) y la
 * barra de /creditos (servidor). Pura.
 */
export function textoChipSaldo(disponible: number, reservados: number): { principal: string; reservados: string | null } {
  return {
    principal: `${disponible} ${disponible === 1 ? "crédito" : "créditos"}`,
    reservados:
      reservados > 0
        ? `${reservados} ${reservados === 1 ? "reservado" : "reservados"} para tu sesión en curso`
        : null,
  };
}
