/**
 * fechas.ts — Fase 3.8: fechas en palabras de persona, español, sin
 * librerías. La copia del canon 10 es "viernes 20 de marzo"; el timeline
 * real (§2) y la línea base (§4) leen de aquí. Todo local (getDay/getDate):
 * la "fecha del calendario" que el usuario ve, no un instante UTC.
 */
import { elegir, LOCALE_BASE, type Locale } from "./i18n/config";
import { interpolar } from "./i18n/interpolar";
import { FECHAS } from "./i18n/mensajes/fechas";

/** El número del día como se escribe en el idioma. El primero del mes es
 * ordinal en italiano, "1º" (se lee "primo": "il 1º marzo"), y en francés,
 * "1er" (se lee "premier": "1er mars"); los demás días, cardinales, también el
 * 21 ("21 mars", "vingt et un"). i18n F6; la elisión "l'8 marzo" vive en
 * lib/i18n/elision.ts. */
const PRIMERO: Record<string, string> = { it: "1º", fr: "1er" };

export function numeroDeDia(dia: number, idioma: Locale): string {
  return (dia === 1 && PRIMERO[idioma]) || String(dia);
}

/** "20 de marzo" (con el año solo si `conAno`), en el idioma pedido. */
function diaDeMes(d: Date, idioma: Locale, conAno = false): string {
  const t = elegir(FECHAS, idioma);
  const mes = t.meses[d.getMonth()];
  const dia = numeroDeDia(d.getDate(), idioma);
  return conAno ? interpolar(t.diaDeMesAno, { d: dia, mes, ano: d.getFullYear() }) : interpolar(t.diaDeMes, { d: dia, mes });
}

/**
 * Sello de tiempo del historial (Fase 4.3.1; formato híbrido desde 4.3.2): la
 * marca de tiempo de la UI VIVA. Decisión del fundador: "la UI respira, las
 * actas constan" — aquí, relativo para lo reciente ("hace 21 min", "hace 3
 * días") y absoluto como ancla ("hoy 08:14", "ayer 21:26", "12 de marzo", con
 * el año solo cuando no es el actual). Es el patrón del canon de Claude Design.
 *
 * IMPORTANTE: esta función es SOLO para la UI. Los DOCUMENTOS DE REGISTRO —el
 * acta de cierre, el informe .md, el análisis exportado— van SIEMPRE en
 * absoluto y NO la usan: leen `fechaHumana`/`fechaHumanaCorta`/ISO. Un registro
 * que diga "hace 3 días" deja de constar en cuanto pasa el tiempo.
 *
 * Local a propósito (getHours/getDate): la fecha del reloj del usuario, no un
 * instante UTC. `ahora` es inyectable para tests deterministas.
 */
export function fechaSello(iso: string, ahora: Date = new Date(), idioma: Locale = LOCALE_BASE): string {
  const t = elegir(FECHAS, idioma);
  const d = new Date(iso);
  const min = Math.floor((ahora.getTime() - d.getTime()) / 60_000);
  if (min < 2) return t.haceUnMomento;
  if (min < 60) return interpolar(t.haceMin, { n: min });
  const hh = String(d.getHours()).padStart(2, "0");
  const mm = String(d.getMinutes()).padStart(2, "0");
  if (d.toDateString() === ahora.toDateString()) return interpolar(t.hoyHora, { hora: `${hh}:${mm}` });
  const ayer = new Date(ahora);
  ayer.setDate(ahora.getDate() - 1);
  if (d.toDateString() === ayer.toDateString()) return interpolar(t.ayerHora, { hora: `${hh}:${mm}` });
  // Diferencia en días DE CALENDARIO (no ventanas de 24h): 2..6 días => relativo.
  const soloFecha = (x: Date) => new Date(x.getFullYear(), x.getMonth(), x.getDate()).getTime();
  const dias = Math.round((soloFecha(ahora) - soloFecha(d)) / 86_400_000);
  if (dias < 7) return interpolar(t.haceDias, { n: dias });
  return diaDeMes(d, idioma, d.getFullYear() !== ahora.getFullYear());
}

/**
 * Sello de una VERSIÓN del historial de Tus Números. Igual espíritu que
 * fechaSello (relativo lo reciente, absoluto lo viejo), pero la HORA es un
 * DESAMBIGUADOR: se muestra solo cuando hay dos o más versiones del mismo día
 * (conHora=true). Con hora, la parte de fecha va absoluta ("12 de julio 14:32")
 * para no chocar con un "hace N días 14:32". El diferenciador de la fila es el
 * contenido (veredicto, margen), no el reloj; la hora solo separa gemelas.
 */
export function selloVersion(iso: string, ahora: Date = new Date(), conHora = false, idioma: Locale = LOCALE_BASE): string {
  const t = elegir(FECHAS, idioma);
  const d = new Date(iso);
  const ayer = new Date(ahora);
  ayer.setDate(ahora.getDate() - 1);
  let fecha: string;
  if (d.toDateString() === ahora.toDateString()) fecha = t.hoy;
  else if (d.toDateString() === ayer.toDateString()) fecha = t.ayer;
  else {
    const soloFecha = (x: Date) => new Date(x.getFullYear(), x.getMonth(), x.getDate()).getTime();
    const dias = Math.round((soloFecha(ahora) - soloFecha(d)) / 86_400_000);
    const abs = diaDeMes(d, idioma, d.getFullYear() !== ahora.getFullYear());
    fecha = !conHora && dias >= 2 && dias < 7 ? interpolar(t.haceDias, { n: dias }) : abs;
  }
  if (!conHora) return fecha;
  const hh = String(d.getHours()).padStart(2, "0");
  const mm = String(d.getMinutes()).padStart(2, "0");
  return `${fecha} ${hh}:${mm}`;
}

/**
 * El MOMENTO ABSOLUTO de un acta: "18 de julio, 14:32" (con el año solo cuando
 * no es el actual). Es lo que dice la banda de una versión histórica abierta:
 * dentro del documento del pasado, el registro consta en absoluto, no relativo.
 */
export function momentoAbsoluto(iso: string, ahora: Date = new Date(), idioma: Locale = LOCALE_BASE): string {
  const d = new Date(iso);
  const hh = String(d.getHours()).padStart(2, "0");
  const mm = String(d.getMinutes()).padStart(2, "0");
  const fecha = diaDeMes(d, idioma, d.getFullYear() !== ahora.getFullYear());
  return interpolar(elegir(FECHAS, idioma).momento, { fecha, hora: `${hh}:${mm}` });
}

/** "viernes 20 de marzo" — la fecha en palabras del canon 10. */
export function fechaHumana(iso: string, idioma: Locale = LOCALE_BASE): string {
  const t = elegir(FECHAS, idioma);
  const d = new Date(iso);
  return interpolar(t.diaSemanaDeMes, { dia: t.dias[d.getDay()], d: numeroDeDia(d.getDate(), idioma), mes: t.meses[d.getMonth()] });
}

/** "20 de marzo" — versión corta, sin día de la semana. */
export function fechaHumanaCorta(iso: string, idioma: Locale = LOCALE_BASE): string {
  return diaDeMes(new Date(iso), idioma);
}

/** "20 de marzo de 2026" — con año, para documentos que se guardan y se
 * releen fuera de la app (el expediente, los planes descargados): ahí "20 de
 * marzo" a secas no dice de qué año se está hablando. */
export function fechaHumanaConAno(iso: string, idioma: Locale = LOCALE_BASE): string {
  return diaDeMes(new Date(iso), idioma, true);
}

/** "septiembre de 2026" — el mes con su año, sin día: el encabezado de mes de
 * la bitácora en pantalla (decisión del fundador, 26 sep 2026). Local. */
export function mesConAno(iso: string, idioma: Locale = LOCALE_BASE): string {
  const t = elegir(FECHAS, idioma);
  const d = new Date(iso);
  return interpolar(t.mesAno, { mes: t.meses[d.getMonth()], ano: d.getFullYear() });
}

/**
 * ¿La fecha cae en la MISMA semana ISO (lunes–domingo) que `ahora`? Local
 * (getDay/getDate): la semana del calendario del usuario, no una ventana UTC.
 * Vacío/inválido → false. `ahora` inyectable para tests deterministas. La usa la
 * chapa "esta semana" honesta del modo fechas (§4).
 */
export function esEstaSemana(fechaIso: string | null | undefined, ahora: Date = new Date()): boolean {
  if (!fechaIso) return false;
  const f = new Date(fechaIso);
  if (Number.isNaN(f.getTime())) return false;
  const lunesDe = (d: Date) => {
    const desdeLunes = (d.getDay() + 6) % 7; // 0=lunes .. 6=domingo
    return new Date(d.getFullYear(), d.getMonth(), d.getDate() - desdeLunes).getTime();
  };
  return lunesDe(f) === lunesDe(ahora);
}

/** yyyy-mm-dd LOCAL para el value/max de un <input type="date">. */
export function fechaInputLocal(d: Date): string {
  const y = d.getFullYear();
  const m = String(d.getMonth() + 1).padStart(2, "0");
  const day = String(d.getDate()).padStart(2, "0");
  return `${y}-${m}-${day}`;
}

/** "2026-03-20" (de un date input) → ISO del mediodía local, para que el
 * día del calendario no se corra al persistir/leer en otra zona horaria. */
export function isoDesdeInputLocal(fecha: string): string {
  return new Date(`${fecha}T12:00:00`).toISOString();
}
