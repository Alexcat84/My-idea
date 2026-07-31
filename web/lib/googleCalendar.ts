/**
 * googleCalendar — el cliente de Google Calendar (Nivel 1, una vía). Sin SDK:
 * solo `fetch` a los endpoints REST de OAuth y de la Calendar API. Scope MÍNIMO
 * `calendar.app.created`: la app solo ve/gestiona los calendarios que ELLA crea
 * (el "My Idea"), nunca el resto del calendario del usuario.
 *
 * SOLO server-side (lo llaman las rutas /api/calendar/google/* con el token del
 * usuario, ya descifrado). Los errores se lanzan para que el llamador decida
 * (fallar ruidoso en logs, jamás romper la acción del usuario).
 */
const AUTH = "https://accounts.google.com/o/oauth2/v2/auth";
const TOKEN = "https://oauth2.googleapis.com/token";
const CAL = "https://www.googleapis.com/calendar/v3";

/** El único scope que pedimos, además de la identidad para saber el correo. */
export const SCOPE_CALENDARIO = "https://www.googleapis.com/auth/calendar.app.created";
export const SCOPES = `openid email ${SCOPE_CALENDARIO}`;

/** La URL de consentimiento de Google. `access_type=offline` + `prompt=consent`
 * garantizan un refresh_token (para actuar en su calendario más adelante). */
export function urlConsentimiento({ clientId, redirectUri, state }: { clientId: string; redirectUri: string; state: string }): string {
  const p = new URLSearchParams({
    client_id: clientId,
    redirect_uri: redirectUri,
    response_type: "code",
    scope: SCOPES,
    access_type: "offline",
    prompt: "consent",
    include_granted_scopes: "true",
    state,
  });
  return `${AUTH}?${p.toString()}`;
}

/** Decodifica el `email` del id_token (JWT) sin verificar firma (viene directo
 * de Google por TLS en el intercambio del código; solo lo usamos para mostrar). */
function emailDeIdToken(idToken: string | undefined): string | null {
  if (!idToken) return null;
  try {
    const payload = idToken.split(".")[1];
    const json = JSON.parse(Buffer.from(payload, "base64").toString("utf8"));
    return typeof json.email === "string" ? json.email : null;
  } catch {
    return null;
  }
}

export interface Tokens {
  accessToken: string;
  refreshToken: string | null;
  expiresIn: number;
  email: string | null;
}

export async function canjearCodigo({
  code,
  clientId,
  clientSecret,
  redirectUri,
}: {
  code: string;
  clientId: string;
  clientSecret: string;
  redirectUri: string;
}): Promise<Tokens> {
  const res = await fetch(TOKEN, {
    method: "POST",
    headers: { "Content-Type": "application/x-www-form-urlencoded" },
    body: new URLSearchParams({ code, client_id: clientId, client_secret: clientSecret, redirect_uri: redirectUri, grant_type: "authorization_code" }),
  });
  if (!res.ok) throw new Error(`google token ${res.status}: ${await res.text()}`);
  const j = (await res.json()) as { access_token: string; refresh_token?: string; expires_in: number; id_token?: string };
  return { accessToken: j.access_token, refreshToken: j.refresh_token ?? null, expiresIn: j.expires_in, email: emailDeIdToken(j.id_token) };
}

export async function refrescarAccessToken({ refreshToken, clientId, clientSecret }: { refreshToken: string; clientId: string; clientSecret: string }): Promise<string> {
  const res = await fetch(TOKEN, {
    method: "POST",
    headers: { "Content-Type": "application/x-www-form-urlencoded" },
    body: new URLSearchParams({ refresh_token: refreshToken, client_id: clientId, client_secret: clientSecret, grant_type: "refresh_token" }),
  });
  if (!res.ok) throw new Error(`google refresh ${res.status}: ${await res.text()}`);
  return ((await res.json()) as { access_token: string }).access_token;
}

async function cal(accessToken: string, ruta: string, init?: RequestInit): Promise<Response> {
  return fetch(`${CAL}${ruta}`, {
    ...init,
    headers: { Authorization: `Bearer ${accessToken}`, "Content-Type": "application/json", ...(init?.headers ?? {}) },
  });
}

/** Crea el calendario secundario dedicado y devuelve su id. */
export async function crearCalendario(accessToken: string, resumen: string): Promise<string> {
  const res = await cal(accessToken, "/calendars", {
    method: "POST",
    body: JSON.stringify({ summary: resumen, description: "Las fechas de tus ideas en My Idea. Este calendario lo creó y lo gestiona la app; puedes quitarlo cuando quieras." }),
  });
  if (!res.ok) throw new Error(`google crearCalendario ${res.status}: ${await res.text()}`);
  return ((await res.json()) as { id: string }).id;
}

/** Borra el calendario dedicado entero (se lleva todos sus eventos de un tirón). */
export async function borrarCalendario(accessToken: string, calendarId: string): Promise<void> {
  const res = await cal(accessToken, `/calendars/${encodeURIComponent(calendarId)}`, { method: "DELETE" });
  if (!res.ok && res.status !== 404 && res.status !== 410) throw new Error(`google borrarCalendario ${res.status}: ${await res.text()}`);
}

export interface EventoGoogle {
  summary: string;
  description: string;
  start: { date: string };
  end: { date: string };
  reminders: { useDefault: false; overrides: Array<{ method: "popup" | "email"; minutes: number }> };
  extendedProperties?: { private?: Record<string, string> };
}

export async function crearEvento(accessToken: string, calendarId: string, evento: EventoGoogle): Promise<string> {
  const res = await cal(accessToken, `/calendars/${encodeURIComponent(calendarId)}/events`, { method: "POST", body: JSON.stringify(evento) });
  if (!res.ok) throw new Error(`google crearEvento ${res.status}: ${await res.text()}`);
  return ((await res.json()) as { id: string }).id;
}

export async function actualizarEvento(accessToken: string, calendarId: string, eventId: string, evento: EventoGoogle): Promise<void> {
  const res = await cal(accessToken, `/calendars/${encodeURIComponent(calendarId)}/events/${encodeURIComponent(eventId)}`, { method: "PATCH", body: JSON.stringify(evento) });
  if (!res.ok) throw new Error(`google actualizarEvento ${res.status}: ${await res.text()}`);
}

export async function borrarEvento(accessToken: string, calendarId: string, eventId: string): Promise<void> {
  const res = await cal(accessToken, `/calendars/${encodeURIComponent(calendarId)}/events/${encodeURIComponent(eventId)}`, { method: "DELETE" });
  // 404/410: ya no existe (lo borró el usuario o una sync previa): idempotente.
  if (!res.ok && res.status !== 404 && res.status !== 410) throw new Error(`google borrarEvento ${res.status}: ${await res.text()}`);
}
