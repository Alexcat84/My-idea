/**
 * cicloApertura.ts — Ciclo de replanteamiento, Fase 2 (decisiones del
 * fundador, 27 sep 2026). Las PUERTAS de un ciclo posterior, las mismas para
 * "Profundizar mi plan" (POST /follow) y "Replantear mi camino" (POST
 * /replantear): una sola fuente, para que las dos entradas no diverjan en quién
 * puede abrir un ciclo ni en cuándo se aparta o se suelta el precio.
 *
 * En orden (AUD-09, el de siempre del follow): cuenta real y doble factor, la
 * idea existe, la idea realizada o el mundo cerrado no se replanifican, el
 * mundo existe y está activado; luego el saldo, la RESERVA con la clave del
 * cobro de la sesión que va a nacer, y al final el fusible y el límite diario
 * (un rechazo por saldo no gasta el arranque del día). Todo rechazo posterior a
 * la reserva la suelta.
 */
import type { SupabaseClient, User } from "@supabase/supabase-js";
import { NextResponse } from "next/server";
import catalogo from "@/lib/assets/packs_catalog.json";
import { nombreDeMundo } from "@/lib/catalogoMundos";
import { mensajeSaldoInsuficiente, reservarCreditos, resolverReserva, verificarSaldo } from "@/lib/creditos";
import { analyticsDeMundo, calcularAnalytics } from "@/lib/analytics";
import { cargarEntradaAnalytics } from "@/lib/analyticsEntrada";
import { obtenerModosPorEspacio, obtenerProyecto, type Proyecto } from "@/lib/db";
import { construirBloqueRealidad, construirBloqueRealidadMundo } from "@/lib/engine/bloqueRealidad";
import { elegir, type Locale } from "@/lib/i18n/config";
import { interpolar } from "@/lib/i18n/interpolar";
import { RUTAS } from "@/lib/i18n/mensajes/servidorRutas";
import { SERVIDOR_PROYECTO } from "@/lib/i18n/mensajes/servidorProyecto";
import { avisoLogin, esInvitadoInvisible } from "@/lib/identidad";
import { conceptoDelPlan, PRECIOS } from "@/lib/precios";
import {
  identidadLimite,
  mensajeFusible,
  mensajeLimite,
  mensajeServicioNoDisponible,
  verificarFusibleGlobal,
  verificarLimiteDiario,
} from "@/lib/rateLimit";
import { aviso2FA, faltaSegundoFactor } from "@/lib/seguridad";

export type TipoCiclo = "profundizar" | "replantear";

/** El precio de un ciclo en un espacio, de precios.ts (la única fuente). */
export function precioDelCiclo(tipo: TipoCiclo, dominio: string): number {
  return PRECIOS[conceptoDelPlan(dominio, true, tipo === "replantear")];
}

export interface CicloAbierto {
  user: User;
  proyecto: Proyecto;
  /** "" en el núcleo; el nombre de catálogo del mundo en un mundo. */
  nombreMundo: string;
  /** El id de la sesión que va a nacer: la reserva ya lleva su clave. */
  sessionIdNueva: string;
  monto: number;
  soltarReserva: () => Promise<unknown>;
}

/**
 * Abre un ciclo: o devuelve el contexto (con el precio ya apartado y el límite
 * del día ya contado) o la respuesta de rechazo lista para devolver.
 */
export async function abrirCiclo(params: {
  request: Request;
  supabase: SupabaseClient;
  projectId: string;
  dominio: string;
  tipo: TipoCiclo;
  idioma: Locale;
}): Promise<{ ok: true; ciclo: CicloAbierto } | { ok: false; respuesta: NextResponse }> {
  const { request, supabase, projectId, dominio, tipo, idioma } = params;
  const r = elegir(RUTAS, idioma);
  const t = elegir(SERVIDOR_PROYECTO, idioma).follow;
  const rechazo = (cuerpo: unknown, status: number) => ({ ok: false as const, respuesta: NextResponse.json(cuerpo, { status }) });

  const {
    data: { user },
  } = await supabase.auth.getUser();
  if (!user) return rechazo({ error: r.noAutenticado }, 401);
  // ETAPA 2 (la frontera): un ciclo es motor pagado; cuenta real.
  if (esInvitadoInvisible(user)) return rechazo(avisoLogin(idioma), 401);
  if (await faltaSegundoFactor()) return rechazo(aviso2FA(idioma), 403);
  const proyecto = await obtenerProyecto(supabase, projectId);
  if (!proyecto) return rechazo({ error: r.ideaNoEncontrada }, 404);
  // AUD-09 (tanda 5): con la idea REALIZADA no se paga un ciclo del núcleo.
  // Cerrar es reversible de un toque. Va antes del saldo: nadie gasta nada.
  if (dominio === "core" && proyecto.realizada_at) return rechazo({ error: t.ideaRealizada }, 409);

  // Fase 4.2: el mundo debe existir, estar activado y estar ABIERTO, antes de
  // cobrar el arranque: nadie quema una consulta en un 403.
  let nombreMundo = "";
  if (dominio !== "core") {
    const entrada = (catalogo.packs as Array<{ clave: string; nombre: string }>).find((p) => p.clave === dominio);
    if (!entrada) return rechazo({ error: r.mundoNoExiste }, 404);
    nombreMundo = entrada.nombre;
    const { data: unlock } = await supabase
      .from("project_unlocks")
      .select("id, completado_at")
      .eq("project_id", projectId)
      .eq("dominio", dominio)
      .limit(1);
    if (!unlock || unlock.length === 0) {
      return rechazo({ error: interpolar(r.mundoNoActivado, { mundo: nombreDeMundo(dominio, idioma) }) }, 403);
    }
    if ((unlock[0] as { completado_at?: string | null }).completado_at) {
      return rechazo({ error: interpolar(t.mundoCompletado, { mundo: nombreDeMundo(dominio, idioma) }) }, 409);
    }
  }

  // ETAPA 2: VERIFICAR al inicio; el descuento ocurre a la entrega del plan.
  const monto = precioDelCiclo(tipo, dominio);
  const saldo = await verificarSaldo(user.id, monto);
  if (!saldo.alcanza) {
    return rechazo({ error: mensajeSaldoInsuficiente(saldo.creditos, monto, 0, idioma), saldo: saldo.creditos }, 402);
  }

  // AUD-09 M25: RESERVA al empezar, con la clave del cobro de la sesión que va
  // a nacer. Si otra sesión ya apartó el saldo, 402 antes de crear nada.
  const sessionIdNueva = crypto.randomUUID();
  const claveReserva = `plan:${sessionIdNueva}`;
  const reserva = await reservarCreditos(user.id, claveReserva, conceptoDelPlan(dominio, true, tipo === "replantear"), monto);
  if (!reserva.reservado) {
    const ahora = await verificarSaldo(user.id, monto, claveReserva);
    return rechazo({ error: mensajeSaldoInsuficiente(ahora.creditos, monto, ahora.apartados, idioma), saldo: ahora.creditos }, 402);
  }
  const soltarReserva = () => resolverReserva(claveReserva, "liberada");

  // AUD-09 (tanda 2): fusible y límite diario DESPUÉS del saldo y antes de la API.
  const fusible = await verificarFusibleGlobal(user.email);
  if (!fusible.permitido) {
    await soltarReserva();
    return rechazo({ error: fusible.caido ? mensajeServicioNoDisponible(idioma) : mensajeFusible(idioma) }, 503);
  }
  const limite = await verificarLimiteDiario(identidadLimite(user.id, request), user.email);
  if (!limite.permitido) {
    await soltarReserva();
    return rechazo(
      { error: limite.caido ? mensajeServicioNoDisponible(idioma) : mensajeLimite(limite.limite, idioma) },
      limite.caido ? 503 : 429
    );
  }

  return { ok: true, ciclo: { user, proyecto, nombreMundo, sessionIdNueva, monto, soltarReserva } };
}

/**
 * AUD-09 M22: ¿alcanza el saldo para abrir el ciclo? Solo mira: no gasta el
 * límite del día ni aparta créditos. Lo usan los GET de las dos entradas, que
 * la pantalla consulta ANTES de que la persona escriba nada.
 */
export async function consultarSaldoCiclo(params: {
  supabase: SupabaseClient;
  projectId: string;
  dominio: string;
  tipo: TipoCiclo;
  idioma: Locale;
}): Promise<NextResponse> {
  const { supabase, projectId, dominio, tipo, idioma } = params;
  const r = elegir(RUTAS, idioma);
  const {
    data: { user },
  } = await supabase.auth.getUser();
  if (!user) return NextResponse.json({ error: r.noAutenticado }, { status: 401 });
  if (esInvitadoInvisible(user)) return NextResponse.json(avisoLogin(idioma), { status: 401 });
  const proyecto = await obtenerProyecto(supabase, projectId);
  if (!proyecto) return NextResponse.json({ error: r.ideaNoEncontrada }, { status: 404 });
  const costo = precioDelCiclo(tipo, dominio);
  const saldo = await verificarSaldo(user.id, costo);
  if (!saldo.alcanza) {
    return NextResponse.json(
      { error: mensajeSaldoInsuficiente(saldo.creditos, costo, saldo.apartados, idioma), saldo: saldo.creditos },
      { status: 402 }
    );
  }
  return NextResponse.json({ alcanza: true, costo });
}

/**
 * Fase 4.0 §3 (docs/FLUJO_TRACKING.md): el BLOQUE DE REALIDAD de un ciclo, el
 * mismo para las dos entradas. Lee el mismo analytics.ts que el Análisis:
 * cumplimiento, dónde se atora, replanificaciones y ritmo real. Un MUNDO se
 * mide con la misma vara pero con SUS datos, y del proyecto solo lleva una
 * línea de contexto rotulada. AUD-09 M18: una lectura fallida LANZA
 * LecturaFallidaError (quien llama dice 503), no se pinta en cero.
 */
export async function realidadDelCiclo(
  supabase: SupabaseClient,
  projectId: string,
  proyecto: Proyecto,
  dominio: string,
  nombreMundo: string
): Promise<string | null> {
  const entrada = await cargarEntradaAnalytics(supabase, projectId, proyecto);
  const analytics = calcularAnalytics(entrada);
  if (dominio === "core") return construirBloqueRealidad(analytics);
  const aMundo = analyticsDeMundo(entrada, dominio);
  // AUD-09 M10: el modo del MUNDO (project_modos), no el del núcleo.
  const modoMundo = (await obtenerModosPorEspacio(supabase, projectId))[dominio] ?? null;
  return aMundo ? construirBloqueRealidadMundo(aMundo, analytics, nombreMundo, modoMundo) : null;
}
