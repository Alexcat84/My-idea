/**
 * AUD-09 M39: el "Cómo te fue" del Expediente habla con los datos. Antes decía
 * siempre "Vas por buen camino" y, sin replanificaciones, "Mantuviste tu ritmo
 * cerca de tu plan", también a mi ritmo (sin fechas) o con todo tardío. Pura.
 */
export function resumenCaminoExpediente(d: {
  cerrada: boolean;
  modo: "ritmo" | "fechas" | null;
  cumplimiento: {
    aTiempo: number;
    adelantadas: number;
    tardias: number;
    totalConFecha: number;
    replanificaciones: number;
    desviacionVsInicialDias: number;
  } | null;
}): { intro: string; loQueMovio: string } {
  const intro = d.cerrada
    ? "Empezaste con una idea y llegaste hasta el cierre. Esto es lo que dejó el camino."
    : "Esto es lo que llevas hasta aquí.";
  const c = d.cumplimiento;
  let loQueMovio: string;
  if (c && c.replanificaciones > 0) {
    const signo = c.desviacionVsInicialDias >= 0 ? "+" : "";
    loQueMovio = `Frente a tu plan inicial te moviste ${signo}${c.desviacionVsInicialDias.toFixed(1)} días de media a lo largo de ${c.replanificaciones} ${c.replanificaciones === 1 ? "replanificación" : "replanificaciones"}. Ajustar el mapa fue parte del método.`;
  } else if (c && c.totalConFecha > 0) {
    loQueMovio = `De tus ${c.totalConFecha} acciones con fecha, ${c.aTiempo} salieron a tiempo, ${c.adelantadas} antes y ${c.tardias} después de lo planeado.`;
  } else if (d.modo === "ritmo") {
    loQueMovio = "Avanzaste a tu ritmo, sin fechas contra las cuales medirte.";
  } else {
    loQueMovio = "Aún no sellaste tus fechas, así que no hay un plan contra el cual medir tu ritmo.";
  }
  return { intro, loQueMovio };
}
