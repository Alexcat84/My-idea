/**
 * ics.ts — generador de archivos .ics (iCalendar, RFC 5545) para el "Nivel 0"
 * del calendario: sin backend. El usuario descarga el .ics de sus tareas con
 * fecha y su teléfono (Apple/Google/Outlook) pone el RECORDATORIO nativo.
 *
 * Cada tarea pendiente con fecha_base se vuelve un evento a las 09:00 (hora
 * local flotante, sin zona: el teléfono la interpreta en la del usuario) con
 * una alarma al inicio. El UID es estable por tarea: volver a añadir ACTUALIZA
 * el evento en vez de duplicarlo. Es puro (sin DOM, sin red): fácil de testear.
 */
export interface TareaIcs {
  id: string;
  texto: string;
  etapa: number;
  /** ISO de la fecha prevista (fecha_base) */
  fechaBase: string;
}

/** Escapa los caracteres especiales de un valor de texto iCalendar. */
function escapar(s: string): string {
  return s
    .replace(/\\/g, "\\\\")
    .replace(/;/g, "\\;")
    .replace(/,/g, "\\,")
    .replace(/\r?\n/g, "\\n");
}

/** Plegado de líneas a ≤73 caracteres (RFC 5545 §3.1): las continuaciones
 * empiezan con un espacio. Conservador con acentos (cuenta caracteres). */
function plegar(linea: string): string {
  if (linea.length <= 73) return linea;
  let out = linea.slice(0, 73);
  let resto = linea.slice(73);
  while (resto.length > 72) {
    out += `\r\n ${resto.slice(0, 72)}`;
    resto = resto.slice(72);
  }
  return `${out}\r\n ${resto}`;
}

const dosDig = (n: number) => String(n).padStart(2, "0");

/** yyyymmddThhmmss LOCAL flotante (sin Z) a las 09:00, desde una fecha ISO. */
function inicioLocal(iso: string): string {
  const d = new Date(iso);
  return `${d.getFullYear()}${dosDig(d.getMonth() + 1)}${dosDig(d.getDate())}T090000`;
}

/** yyyymmddThhmmssZ (UTC) para DTSTAMP. */
function selloUtc(d: Date): string {
  return `${d.getUTCFullYear()}${dosDig(d.getUTCMonth() + 1)}${dosDig(d.getUTCDate())}T${dosDig(
    d.getUTCHours()
  )}${dosDig(d.getUTCMinutes())}${dosDig(d.getUTCSeconds())}Z`;
}

/** Devuelve el texto de un archivo .ics con un evento por tarea. */
export function generarIcs({
  nombreIdea,
  tareas,
  ahora = new Date(),
}: {
  nombreIdea: string;
  tareas: TareaIcs[];
  ahora?: Date;
}): string {
  const stamp = selloUtc(ahora);
  const l: string[] = [
    "BEGIN:VCALENDAR",
    "VERSION:2.0",
    "PRODID:-//My Idea//Calendario//ES",
    "CALSCALE:GREGORIAN",
    "METHOD:PUBLISH",
  ];
  for (const t of tareas) {
    const inicio = inicioLocal(t.fechaBase);
    const fin = `${inicio.slice(0, 9)}093000`;
    l.push(
      "BEGIN:VEVENT",
      `UID:${t.id}@myideaproject.com`,
      `DTSTAMP:${stamp}`,
      `DTSTART:${inicio}`,
      `DTEND:${fin}`,
      `SUMMARY:${escapar(t.texto)}`,
      `DESCRIPTION:${escapar(`Etapa ${t.etapa} · ${nombreIdea}`)}`,
      "BEGIN:VALARM",
      "ACTION:DISPLAY",
      `DESCRIPTION:${escapar(t.texto)}`,
      "TRIGGER:-PT0M",
      "END:VALARM",
      "END:VEVENT"
    );
  }
  l.push("END:VCALENDAR");
  return l.map(plegar).join("\r\n");
}
