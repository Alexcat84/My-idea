/**
 * POST /api/session/[id]/regenerar: regenerar un plan básico (AUD-09, decisión
 * del fundador del 25 sep 2026).
 *
 * El plan básico nace cuando la conversación llegó a su tope de trabajo: la
 * redacción con IA no ocurrió, el plan se armó sin narrar y se entregó gratis.
 * Regenerarlo en la MISMA sesión chocaría con el mismo tope, así que es una
 * SESIÓN NUEVA con su presupuesto completo, que parte del perfil ya capturado
 * (ruta, perfil, texto original: sin repetir la entrevista). Esta ruta solo la
 * prepara; el plan sale por POST /api/session/[nueva]/plan, la ruta de
 * siempre, que cobra el precio normal SOLO si la IA entrega y, si vuelve a
 * fallar, lo entrega otra vez gratis con el mismo aviso. El plan nuevo pasa a
 * vigente por el mecanismo de siempre (el último plan del espacio manda) y el
 * básico queda archivado con sus tareas, visible en el historial.
 *
 * Es una acción que va a invocar la IA: pasa por los mismos controles que
 * toda otra (doble factor, saldo, y fusible y límite diario DESPUÉS del saldo).
 */
import { NextResponse } from "next/server";
import { elegir } from "@/lib/i18n/config";
import { RUTAS } from "@/lib/i18n/mensajes/servidorRutas";
import { SERVIDOR_SESION } from "@/lib/i18n/mensajes/servidorSesion";
import { idiomaDeRequest } from "@/lib/i18n/servidor";
import { usoVacio } from "@/lib/costmeter";
import {
  conceptoDelPlan,
  mensajeSaldoInsuficiente,
  montoDelPlan,
  reservarCreditos,
  resolverReserva,
  verificarSaldo,
} from "@/lib/creditos";
import { crearSesion, guardarEstadoSesion, obtenerSesion, type EstadoSesionPersistido } from "@/lib/db";
import { avisoDelPlan } from "@/lib/engine/planRedactor";
import { avisoLogin, esInvitadoInvisible } from "@/lib/identidad";
import { identidadLimite, mensajeFusible, mensajeLimite, verificarFusibleGlobal, verificarLimiteDiario } from "@/lib/rateLimit";
import { aviso2FA, faltaSegundoFactor } from "@/lib/seguridad";
import { createClient } from "@/lib/supabase/server";

export async function POST(request: Request, { params }: { params: Promise<{ id: string }> }) {
  const { id: sessionBasica } = await params;
  const idioma = idiomaDeRequest(request);
  const r = elegir(RUTAS, idioma);
  const t = elegir(SERVIDOR_SESION, idioma).regenerar;

  const supabase = await createClient();
  const {
    data: { user },
  } = await supabase.auth.getUser();
  if (!user) {
    return NextResponse.json({ error: r.noAutenticado }, { status: 401 });
  }
  if (esInvitadoInvisible(user)) {
    return NextResponse.json(avisoLogin(idioma), { status: 401 });
  }
  if (await faltaSegundoFactor()) {
    return NextResponse.json(aviso2FA(idioma), { status: 403 });
  }

  const sesion = await obtenerSesion(supabase, sessionBasica);
  if (!sesion) {
    return NextResponse.json({ error: t.noEncontrePlan }, { status: 404 });
  }
  const estado = sesion.estado_recorrido as EstadoSesionPersistido | null;
  const decisiones = (sesion as { decisiones?: unknown }).decisiones;
  if (!estado || !avisoDelPlan(decisiones)) {
    return NextResponse.json({ error: t.planCompleto }, { status: 409 });
  }

  const dominio = ((sesion as { dominio?: string | null }).dominio ?? "core") as string;
  const esSeguimiento = estado.recorrido.esSeguimiento === true;
  const costo = montoDelPlan(dominio, esSeguimiento);

  // El saldo primero: un rechazo por saldo no gasta el arranque del día.
  const saldo = await verificarSaldo(user.id, costo);
  if (!saldo.alcanza) {
    return NextResponse.json(
      { error: mensajeSaldoInsuficiente(saldo.creditos, costo, 0, idioma), saldo: saldo.creditos },
      { status: 402 }
    );
  }
  // AUD-09 M25: la sesión nueva RESERVA su precio al empezar, con la clave de
  // su cobro (id generado aquí); si otra sesión ya apartó el saldo, 402 sin
  // crear nada. Un rechazo posterior suelta la reserva.
  const nuevaId = crypto.randomUUID();
  const claveReserva = `plan:${nuevaId}`;
  const reserva = await reservarCreditos(user.id, claveReserva, conceptoDelPlan(dominio, esSeguimiento), costo);
  if (!reserva.reservado) {
    const ahora = await verificarSaldo(user.id, costo, claveReserva);
    return NextResponse.json(
      { error: mensajeSaldoInsuficiente(ahora.creditos, costo, ahora.apartados, idioma), saldo: ahora.creditos },
      { status: 402 }
    );
  }
  const fusible = await verificarFusibleGlobal(user.email);
  if (!fusible.permitido) {
    await resolverReserva(claveReserva, "liberada");
    return NextResponse.json({ error: mensajeFusible(idioma) }, { status: 503 });
  }
  const limite = await verificarLimiteDiario(identidadLimite(user.id, request), user.email);
  if (!limite.permitido) {
    await resolverReserva(claveReserva, "liberada");
    return NextResponse.json({ error: mensajeLimite(limite.limite, idioma) }, { status: 429 });
  }

  const tipo = ((sesion as { tipo?: string }).tipo ?? (esSeguimiento ? "seguimiento" : "inicial")) as Parameters<
    typeof crearSesion
  >[3];
  const nueva = await crearSesion(
    supabase,
    user.id,
    sesion.project_id,
    tipo,
    "regeneracion del plan basico",
    null,
    dominio,
    { id: nuevaId }
  );
  await guardarEstadoSesion(supabase, nueva, {
    recorrido: {
      ...estado.recorrido,
      fase: "listo_para_plan",
      preguntaPendiente: null,
      fallbackEvents: [{ tipo: "regeneracion_plan_basico", desde_sesion: sessionBasica }],
    },
    // Presupuesto completo: la sesión nueva no hereda el gasto de la básica.
    acumulado: usoVacio(),
  });

  return NextResponse.json({ session_id: nueva, costo });
}
