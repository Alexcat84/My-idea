/**
 * AUD-09 M39: el "Cómo te fue" del Expediente habla con los datos. Antes decía
 * siempre "Vas por buen camino" y, sin replanificaciones, "Mantuviste tu ritmo
 * cerca de tu plan", también a mi ritmo (sin fechas) o con todo tardío. Pura.
 */
import { elegir, LOCALE_BASE, type Locale } from "./i18n/config";
import { decimal } from "./i18n/formato";
import { interpolar, plural } from "./i18n/interpolar";
import { EXPEDIENTE } from "./i18n/mensajes/expediente";

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
}, idioma: Locale = LOCALE_BASE): { intro: string; loQueMovio: string } {
  const t = elegir(EXPEDIENTE, idioma).resumenCamino;
  const intro = d.cerrada ? t.introCerrada : t.introEnMarcha;
  const c = d.cumplimiento;
  let loQueMovio: string;
  if (c && c.replanificaciones > 0) {
    const signo = c.desviacionVsInicialDias >= 0 ? "+" : "";
    loQueMovio = interpolar(t.movioReplanificando, {
      desviacion: `${signo}${decimal(idioma, c.desviacionVsInicialDias, 1)}`,
      replanificaciones: plural(idioma, c.replanificaciones, t.replanificaciones),
    });
  } else if (c && c.totalConFecha > 0) {
    loQueMovio = interpolar(t.movioConFechas, {
      total: c.totalConFecha,
      aTiempo: c.aTiempo,
      adelantadas: c.adelantadas,
      tardias: c.tardias,
    });
  } else if (d.modo === "ritmo") {
    loQueMovio = t.movioARitmo;
  } else {
    loQueMovio = t.movioSinFechas;
  }
  return { intro, loQueMovio };
}
