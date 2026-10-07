/**
 * El redactor del plan en streaming (movido desde app/api/session/[id]/plan/route.ts, 28 sep 2026: un fichero de
 * ruta solo puede exportar sus metodos, y esta pieza necesitaba prueba propia).
 *
 * Reintento del redactor (hermano del fix del organizador). El plan se genera en el momento de MAYOR inversion
 * emocional del usuario -- acaba de terminar su entrevista -- y es un momento PAGADO (PRECIOS.plan_completo): un hipo
 * transitorio de la API no puede costarle su plan. El SDK reintenta la conexion inicial pero NO un fallo a mitad de
 * stream: eso lo cubre esta red.
 *
 * Contexto de la entrevista (28 sep 2026):
 *  - un plan CORTADO por el tope de tokens no se trata como completo: ese intento se registra (se pago), el siguiente
 *    dobla el tope, y si se agotan los intentos se falla con aviso;
 *  - el contexto del proyecto (memoria y ficha de la persona) viaja en su propio bloque con cache de 1 hora, antes
 *    del material del plan.
 */
import type Anthropic from "@anthropic-ai/sdk";
import {
  CACHE_1H,
  costoAcumuladoUsd,
  MODEL,
  PresupuestoExcedidoError,
  PRESUPUESTO_SESION_USD_DEFAULT,
  registrarUso,
  RespuestaCortadaError,
  type UsoAcumulado,
} from "../costmeter";
import { bloquesDeSistema } from "../i18n/idiomaSalida";
import { SYSTEM_PLAN } from "../prompts";
import { ROTULOS_PLAN } from "./constants";
import { filtrarDeltaAntesDeAutodeclaracion, type PreparacionPlan } from "./planRedactor";

export const BACKOFFS_PLAN_MS = [0, 1000, 3000];
const MAX_TOKENS_PLAN = 5000;

export async function generarTextoPlan(
  client: Anthropic,
  preparacion: PreparacionPlan,
  acumulado: UsoAcumulado,
  onDelta: (texto: string) => void,
  /** Un intento previo pinto etapas en el arbol de espera y murio: el cliente
   * debe DESCARTARLAS antes de que el intento nuevo pinte las suyas (el texto
   * nuevo no es el mismo). Anunciar una sola vez, la leccion del organizador. */
  onReinicio: () => void,
  /** i18n F5: el idioma de la IDEA (el plan sigue al proyecto, D2). */
  idiomaSalida: string | null = null,
  opts: { backoffsMs?: number[]; contexto?: string | null } = {}
): Promise<{ rawTexto: string | null; acumulado: UsoAcumulado; avisoFallback: string | null }> {
  if (costoAcumuladoUsd(acumulado) >= PRESUPUESTO_SESION_USD_DEFAULT) {
    return { rawTexto: null, acumulado, avisoFallback: "presupuesto de sesion ya excedido, ensamblo sin narrar" };
  }
  const backoffs = opts.backoffsMs ?? BACKOFFS_PLAN_MS;
  const material = JSON.stringify(preparacion.payload);
  const content = opts.contexto
    ? [
        { type: "text" as const, text: opts.contexto, cache_control: CACHE_1H },
        { type: "text" as const, text: material },
      ]
    : material;
  let maxTokens = MAX_TOKENS_PLAN;
  let acumuladoVivo = acumulado;
  let ultimoError: unknown = null;
  for (let intento = 0; intento < backoffs.length; intento += 1) {
    if (intento > 0) {
      if (backoffs[intento] > 0) await new Promise((r) => setTimeout(r, backoffs[intento]));
      onReinicio();
    }
    try {
      const stream = client.messages.stream({
        model: MODEL,
        max_tokens: maxTokens,
        system: bloquesDeSistema(SYSTEM_PLAN, idiomaSalida, ROTULOS_PLAN),
        messages: [{ role: "user", content }] as Anthropic.MessageParam[],
      });
      // Nunca reenviar el marcador ===JSON=== ni lo que sigue -- es la
      // autodeclaracion de cobertura interna (regla 11 de SYSTEM_PLAN), no
      // contenido para mostrar en vivo. Filtro NUEVO por intento: es con estado.
      const filtro = filtrarDeltaAntesDeAutodeclaracion(onDelta);
      stream.on("text", filtro.onChunk);
      const mensajeFinal = await stream.finalMessage();
      filtro.finalizar();
      acumuladoVivo = registrarUso(acumuladoVivo, MODEL, mensajeFinal.usage, "plan", mensajeFinal.stop_reason ?? null, Boolean(opts.contexto));
      if (mensajeFinal.stop_reason === "max_tokens") {
        ultimoError = new RespuestaCortadaError("plan", maxTokens);
        console.error(`[plan] intento ${intento + 1}/${backoffs.length} salio cortado por tope de tokens (${maxTokens})`);
        maxTokens *= 2;
        continue;
      }
      const rawTexto = mensajeFinal.content
        .filter((b): b is Anthropic.TextBlock => b.type === "text")
        .map((b) => b.text)
        .join("");
      return { rawTexto, acumulado: acumuladoVivo, avisoFallback: null };
    } catch (e) {
      // El presupuesto no es un hipo: reintentar solo quemaria mas. Es el UNICO
      // caso que sigue ensamblando offline, que para eso existe.
      if (e instanceof PresupuestoExcedidoError) {
        return { rawTexto: null, acumulado: acumuladoVivo, avisoFallback: `fallo el redactor con IA, ensamblo offline: ${e.message}` };
      }
      ultimoError = e;
      console.error(`[plan] intento ${intento + 1}/${backoffs.length} fallo:`, e);
    }
  }
  // Agotados los reintentos: LANZA. Antes se degradaba en silencio a un
  // ensamblado offline -- un plan mecanico, sin narracion, entregado como si
  // nada en el momento que mas le importa al usuario (y que pronto le cuesta 5
  // creditos). Es mejor decirlo y ofrecerle reintentar SOLO la redaccion: su
  // sesion y su recorrido ya estan persistidos, la entrevista no se repite.
  console.error("[plan] redactor agotado tras reintentos", { ultimoError });
  throw ultimoError instanceof Error ? ultimoError : new Error(String(ultimoError));
}
