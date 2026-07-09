/**
 * rateLimit.ts — Fase 3.2 (item del plan original de Fase 3.0): límite
 * de beta de 5 arranques al día por usuario (ideas nuevas + entrevistas),
 * patrón Upstash del proyecto I Ching. Ventana fija por día UTC via
 * INCR + EXPIRE sobre el REST API de Upstash (sin SDK: dos fetch).
 *
 * Solo se cobra el ARRANQUE de trabajo caro (organizador, inicio de
 * entrevista); los turnos siguientes de una entrevista ya arrancada no
 * cuentan — cortar a alguien a mitad de entrevista sería castigarlo por
 * habernos respondido.
 *
 * Si las credenciales no están en el entorno (dev local sin .env
 * completo), el límite se desactiva con un aviso en consola: nunca debe
 * romper el flujo por configuración faltante.
 */

const LIMITE_DIARIO = 5;

interface ResultadoLimite {
  permitido: boolean;
  usados: number;
  limite: number;
}

export async function verificarLimiteDiario(userId: string, email?: string | null): Promise<ResultadoLimite> {
  // El dev user de los arneses de prueba (vuelo.ts/probar.ts, ver
  // scripts/setup_dev_user.py) queda exento: una corrida completa del
  // vuelo hace 4 arranques y dos corridas el mismo dia reventarian el
  // limite -- castigar a la verificacion seria castigar la disciplina.
  if (email === "dev@my-idea.local") {
    return { permitido: true, usados: 0, limite: LIMITE_DIARIO };
  }
  const url = process.env.UPSTASH_REDIS_REST_URL;
  const token = process.env.UPSTASH_REDIS_REST_TOKEN;
  if (!url || !token) {
    console.warn("rateLimit: UPSTASH_REDIS_REST_URL/TOKEN ausentes; limite desactivado");
    return { permitido: true, usados: 0, limite: LIMITE_DIARIO };
  }

  const dia = new Date().toISOString().slice(0, 10); // YYYY-MM-DD (UTC)
  const clave = `myidea:rl:${userId}:${dia}`;
  const headers = { Authorization: `Bearer ${token}` };

  const resIncr = await fetch(`${url}/incr/${encodeURIComponent(clave)}`, { headers });
  if (!resIncr.ok) {
    // Upstash caído no debe tumbar el producto: se permite y se registra.
    console.warn(`rateLimit: INCR fallo (${resIncr.status}); se permite la solicitud`);
    return { permitido: true, usados: 0, limite: LIMITE_DIARIO };
  }
  const usados = Number(((await resIncr.json()) as { result: number }).result);

  if (usados === 1) {
    // Primera del día: la clave expira sola a las 24h (ventana fija).
    await fetch(`${url}/expire/${encodeURIComponent(clave)}/86400`, { headers }).catch(() => {});
  }

  return { permitido: usados <= LIMITE_DIARIO, usados, limite: LIMITE_DIARIO };
}

/** Mensaje en palabras de persona para el 429 (el usuario web nunca ve
 * maquinaria). */
export const MENSAJE_LIMITE =
  "Por hoy alcanzaste el límite de la beta (5 arranques al día). " +
  "Tus ideas quedan guardadas — vuelve mañana y seguimos donde quedamos.";
