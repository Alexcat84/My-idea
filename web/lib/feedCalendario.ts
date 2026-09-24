/**
 * feedCalendario — el token del feed de calendario suscribible (Nivel 1
 * UNIVERSAL, opción B). La suscripción a un calendario no puede mandar cabeceras
 * de auth, así que la URL lleva un token FIRMADO: `base64url(userId).firma`,
 * donde firma = HMAC-SHA256(userId) con una clave del servidor. El feed es de
 * SOLO LECTURA (las fechas del propio usuario), así que el token es de bajo
 * riesgo; verificarlo evita que alguien forje el de otro usuario.
 *
 * La clave HMAC reusa `SUPABASE_SERVICE_ROLE_KEY` (alta entropía, ya presente en
 * el entorno, nunca expuesta): sin variable nueva. Rotarla invalida todos los
 * feeds (revocación global); la per-usuario no hace falta para un feed público.
 * SOLO server-side (node:crypto).
 */
import { createHmac, timingSafeEqual } from "node:crypto";

function claveHmac(): string {
  const s = process.env.SUPABASE_SERVICE_ROLE_KEY;
  if (!s) throw new Error("falta SUPABASE_SERVICE_ROLE_KEY para el feed de calendario");
  return s;
}

function firmar(userId: string): string {
  return createHmac("sha256", claveHmac()).update(userId).digest("base64url");
}

/** token = base64url(userId).firma */
export function tokenDeUsuario(userId: string): string {
  return `${Buffer.from(userId).toString("base64url")}.${firmar(userId)}`;
}

/** Verifica el token y devuelve el userId; null si no cuadra (comparación en
 * tiempo constante para no filtrar por temporización). */
export function usuarioDeToken(token: string): string | null {
  const punto = token.indexOf(".");
  if (punto <= 0) return null;
  const uidB64 = token.slice(0, punto);
  const firma = token.slice(punto + 1);
  let userId: string;
  try {
    userId = Buffer.from(uidB64, "base64url").toString("utf8");
  } catch {
    return null;
  }
  if (!userId) return null;
  const esperada = Buffer.from(firmar(userId));
  const recibida = Buffer.from(firma);
  if (esperada.length !== recibida.length) return null;
  return timingSafeEqual(esperada, recibida) ? userId : null;
}

// ─── AUD-09 H11: qué avisa el calendario suscrito ───────────────────────────

export interface ItemFeed {
  id: string;
  plan_id: string | null;
  dominio: string | null;
  estado: string;
  texto: string | null;
  etapa: number;
  fecha_base: string | null;
}

export interface PlanFeed {
  id: string;
  dominio: string | null;
  created_at: string;
  etiqueta: string;
}

const ETIQUETAS_DE_PLAN = ["inicial", "completo", "seguimiento"];
const dominioDe = (d: string | null | undefined) => (!d ? "core" : d);

/**
 * El teléfono solo recibe recordatorios de lo que el usuario sigue queriendo
 * con fechas: el plan VIGENTE de cada espacio (el último; los reemplazados ya
 * no avisan), nunca un espacio en modo "a mi ritmo" (BANCO §5: sin fechas no
 * hay recordatorios), nunca un mundo completado, y silencio entero para una
 * idea realizada. De lo que queda, solo lo pendiente con fecha. Pura.
 */
export function itemsQueAvisan(opts: {
  realizada: boolean;
  items: ItemFeed[];
  planes: PlanFeed[];
  modos: Record<string, "ritmo" | "fechas">;
  mundosCompletados: string[];
}): ItemFeed[] {
  if (opts.realizada) return [];
  const vigente: Record<string, PlanFeed> = {};
  for (const p of opts.planes) {
    if (!ETIQUETAS_DE_PLAN.includes(p.etiqueta)) continue;
    const d = dominioDe(p.dominio);
    if (!vigente[d] || new Date(p.created_at).getTime() > new Date(vigente[d].created_at).getTime()) vigente[d] = p;
  }
  return opts.items.filter((i) => {
    const d = dominioDe(i.dominio);
    if (!i.fecha_base || i.estado === "hecho" || i.estado === "no_aplica") return false;
    if (!vigente[d] || i.plan_id !== vigente[d].id) return false;
    if (opts.modos[d] === "ritmo") return false;
    if (d !== "core" && opts.mundosCompletados.includes(d)) return false;
    return true;
  });
}
