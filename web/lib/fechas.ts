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
