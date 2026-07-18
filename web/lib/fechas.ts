/**
 * fechas.ts — Fase 3.8: fechas en palabras de persona, español, sin
 * librerías. La copia del canon 10 es "viernes 20 de marzo"; el timeline
 * real (§2) y la línea base (§4) leen de aquí. Todo local (getDay/getDate):
 * la "fecha del calendario" que el usuario ve, no un instante UTC.
 */
const MESES = [
  "enero",
  "febrero",
  "marzo",
  "abril",
  "mayo",
  "junio",
  "julio",
  "agosto",
  "septiembre",
  "octubre",
  "noviembre",
  "diciembre",
] as const;

const DIAS = ["domingo", "lunes", "martes", "miércoles", "jueves", "viernes", "sábado"] as const;

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
export function fechaSello(iso: string, ahora: Date = new Date()): string {
  const d = new Date(iso);
  const min = Math.floor((ahora.getTime() - d.getTime()) / 60_000);
  if (min < 2) return "hace un momento";
  if (min < 60) return `hace ${min} min`;
  const hh = String(d.getHours()).padStart(2, "0");
  const mm = String(d.getMinutes()).padStart(2, "0");
  if (d.toDateString() === ahora.toDateString()) return `hoy ${hh}:${mm}`;
  const ayer = new Date(ahora);
  ayer.setDate(ahora.getDate() - 1);
  if (d.toDateString() === ayer.toDateString()) return `ayer ${hh}:${mm}`;
  // Diferencia en días DE CALENDARIO (no ventanas de 24h): 2..6 días => relativo.
  const soloFecha = (x: Date) => new Date(x.getFullYear(), x.getMonth(), x.getDate()).getTime();
  const dias = Math.round((soloFecha(ahora) - soloFecha(d)) / 86_400_000);
  if (dias < 7) return `hace ${dias} días`;
  const base = `${d.getDate()} de ${MESES[d.getMonth()]}`;
  return d.getFullYear() === ahora.getFullYear() ? base : `${base} de ${d.getFullYear()}`;
}

/**
 * Sello de una VERSIÓN del historial de Tus Números. Igual espíritu que
 * fechaSello (relativo lo reciente, absoluto lo viejo), pero la HORA es un
 * DESAMBIGUADOR: se muestra solo cuando hay dos o más versiones del mismo día
 * (conHora=true). Con hora, la parte de fecha va absoluta ("12 de julio 14:32")
 * para no chocar con un "hace N días 14:32". El diferenciador de la fila es el
 * contenido (veredicto, margen), no el reloj; la hora solo separa gemelas.
 */
export function selloVersion(iso: string, ahora: Date = new Date(), conHora = false): string {
  const d = new Date(iso);
  const ayer = new Date(ahora);
  ayer.setDate(ahora.getDate() - 1);
  let fecha: string;
  if (d.toDateString() === ahora.toDateString()) fecha = "hoy";
  else if (d.toDateString() === ayer.toDateString()) fecha = "ayer";
  else {
    const soloFecha = (x: Date) => new Date(x.getFullYear(), x.getMonth(), x.getDate()).getTime();
    const dias = Math.round((soloFecha(ahora) - soloFecha(d)) / 86_400_000);
    const abs = d.getFullYear() === ahora.getFullYear() ? `${d.getDate()} de ${MESES[d.getMonth()]}` : `${d.getDate()} de ${MESES[d.getMonth()]} de ${d.getFullYear()}`;
    fecha = !conHora && dias >= 2 && dias < 7 ? `hace ${dias} días` : abs;
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
export function momentoAbsoluto(iso: string, ahora: Date = new Date()): string {
  const d = new Date(iso);
  const hh = String(d.getHours()).padStart(2, "0");
  const mm = String(d.getMinutes()).padStart(2, "0");
  const base = `${d.getDate()} de ${MESES[d.getMonth()]}`;
  const conAno = d.getFullYear() === ahora.getFullYear() ? base : `${base} de ${d.getFullYear()}`;
  return `${conAno}, ${hh}:${mm}`;
}

/** "viernes 20 de marzo" — la fecha en palabras del canon 10. */
export function fechaHumana(iso: string): string {
  const d = new Date(iso);
  return `${DIAS[d.getDay()]} ${d.getDate()} de ${MESES[d.getMonth()]}`;
}

/** "20 de marzo" — versión corta, sin día de la semana. */
export function fechaHumanaCorta(iso: string): string {
  const d = new Date(iso);
  return `${d.getDate()} de ${MESES[d.getMonth()]}`;
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
