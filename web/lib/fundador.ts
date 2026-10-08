/**
 * La puerta del mini-gate comprueba quién eres (encargo del fundador del 6 oct 2026, punto 7c).
 *
 * `?ver=ocultos` solo PIDE ver los mundos sin publicar; quien decide es el servidor. Un mundo oculto se lista y se
 * abre solo para una cuenta real cuyo correo está en FUNDADOR_EMAILS (variable de entorno, separada por comas; vacía
 * o ausente = nadie). Así el enlace deja de ser una llave: copiado a otra cuenta, no abre nada.
 * Prueba: lib/fundador.test.ts.
 */
import type { User } from "@supabase/supabase-js";
import { mundo } from "./catalogoMundos";
import { esInvitadoInvisible } from "./identidad";

function correosFundador(): Set<string> {
  return new Set(
    (process.env.FUNDADOR_EMAILS ?? "")
      .split(",")
      .map((c) => c.trim().toLowerCase())
      .filter(Boolean),
  );
}

/** ¿Es la cuenta del fundador? Una cuenta real cuyo correo está en FUNDADOR_EMAILS. Abre los mundos sin publicar y
 * el panel de opiniones (app/fundador/opiniones, decisión del 8 oct 2026). */
export function esFundador(user: Pick<User, "is_anonymous" | "email"> | null | undefined): boolean {
  if (!user || esInvitadoInvisible(user)) return false;
  return correosFundador().has((user.email ?? "").trim().toLowerCase());
}

/** ¿Esta cuenta puede ver y caminar los mundos sin publicar? */
export function puedeVerOcultos(user: Pick<User, "is_anonymous" | "email"> | null | undefined): boolean {
  return esFundador(user);
}

/** ¿Esta cuenta puede abrir este mundo? Publicado: cualquiera. Oculto: solo quien puede verlo. Inexistente: nadie. */
export function mundoAlcanzable(clave: string, user: Pick<User, "is_anonymous" | "email"> | null | undefined): boolean {
  const m = mundo(clave);
  if (!m) return false;
  return !m.oculto || puedeVerOcultos(user);
}
