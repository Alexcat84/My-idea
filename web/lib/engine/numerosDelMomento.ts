/**
 * Las cifras que la persona tenia dadas EN EL MOMENTO de un plan (decision del fundador, 10 oct 2026), para que el guion
 * de medicion entregue al redactor lo mismo que produccion en ese momento. Cada cifra del proyecto lleva su fecha
 * (updated_at): entran las anteriores al plan; las de la propia sesion entran siempre y mandan. Una cifra del proyecto
 * sin fecha no se puede situar: no entra y se avisa. Limite declarado: si una cifra se cambio despues del plan, su valor
 * de ese momento no se conoce y no entra.
 */
type Campos = Record<string, { updated_at?: unknown } & Record<string, unknown>>;

export function numerosDelMomento(
  numerosProyecto: unknown,
  numerosSesion: unknown,
  momento: string
): { numeros: Record<string, unknown>; fuera: string[]; sinFecha: string[] } {
  const proyecto = (numerosProyecto && typeof numerosProyecto === "object" ? numerosProyecto : {}) as Campos;
  const sesion = (numerosSesion && typeof numerosSesion === "object" ? numerosSesion : {}) as Record<string, unknown>;
  const limite = Date.parse(momento);
  const numeros: Record<string, unknown> = {};
  const fuera: string[] = [];
  const sinFecha: string[] = [];
  for (const [campo, v] of Object.entries(proyecto)) {
    const f = typeof v?.updated_at === "string" ? Date.parse(v.updated_at) : NaN;
    if (Number.isNaN(f)) sinFecha.push(campo);
    else if (f <= limite) numeros[campo] = v;
    else fuera.push(campo);
  }
  return { numeros: { ...numeros, ...sesion }, fuera, sinFecha };
}
