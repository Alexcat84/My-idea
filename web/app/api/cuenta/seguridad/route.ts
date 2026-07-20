/**
 * GET /api/cuenta/seguridad — el estado 2FA de la cuenta para la UI (centro
 * de cuenta y paso de desafío del login). Nunca expone secretos: solo
 * habilitado/método y si ESTA sesión ya superó el desafío.
 */
import { NextResponse } from "next/server";
import { desafioSuperadoEnSesion, estadoSeguridad, sesionRealDeCookies } from "@/lib/seguridad";

export async function GET() {
  const sesion = await sesionRealDeCookies();
  if (!sesion) return NextResponse.json({ invisible: true });
  const estado = await estadoSeguridad(sesion.user.id);
  return NextResponse.json({
    invisible: false,
    email: sesion.user.email ?? null,
    habilitado: estado.habilitado,
    metodo: estado.metodo,
    desafioSuperado: estado.habilitado
      ? await desafioSuperadoEnSesion(sesion.user.id, sesion.sessionId)
      : true,
  });
}
