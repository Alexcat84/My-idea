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

const MESES_CORTO = ["ene", "feb", "mar", "abr", "may", "jun", "jul", "ago", "sep", "oct", "nov", "dic"] as const;

/**
 * Sello de tiempo del historial (Fase 4.3.1): un timestamp que ANCLA la idea en
 * el calendario, en vez de solo "hace X". El "hace 3 meses / hace 4 meses" no
 * ayuda a ordenar ni a ubicar; una fecha real sí. Patrón heredado de cómo el I
 * Ching guarda los chats: hora para lo de hoy, fecha para lo anterior, y el año
 * solo cuando no es el actual (para no repetirlo en cada línea).
 *
 * Local a propósito (getHours/getDate): es la fecha del reloj del usuario, no un
 * instante UTC. `ahora` es inyectable para tests deterministas.
 */
export function fechaSello(iso: string, ahora: Date = new Date()): string {
  const d = new Date(iso);
  const hh = String(d.getHours()).padStart(2, "0");
  const mm = String(d.getMinutes()).padStart(2, "0");
  if (d.toDateString() === ahora.toDateString()) return `hoy ${hh}:${mm}`;
  const ayer = new Date(ahora);
  ayer.setDate(ahora.getDate() - 1);
  if (d.toDateString() === ayer.toDateString()) return `ayer ${hh}:${mm}`;
  const base = `${d.getDate()} ${MESES_CORTO[d.getMonth()]}`;
  return d.getFullYear() === ahora.getFullYear() ? base : `${base} ${d.getFullYear()}`;
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
