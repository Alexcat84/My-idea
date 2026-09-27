/**
 * POST /api/project/[id]/world/[pack]/unlock — Fase 3.5, remodelada por la
 * 4.5 (PREVIEW_MUNDOS_PLAN): ABRIR el mundo, gratis. Ya no es una compra:
 * el cobro del mundo vive en la ENTREGA de su plan (ruta del plan, ancla
 * ETAPA 2). Esta ruta solo crea la fila para que el dominio EXISTA para el
 * motor (el muro de filtros deja pasar) y su sección aparezca en Manos a la
 * Obra; el preview en sí lo sella world/start (preview_at). Idempotente:
 * abrir dos veces responde ok sin duplicar (UNIQUE project_id+dominio).
 * creditos_pagados queda en 0 siempre: registro histórico del modelo viejo.
 */
import { NextResponse } from "next/server";
import { elegir } from "@/lib/i18n/config";
import { RUTAS } from "@/lib/i18n/mensajes/servidorRutas";
import { SERVIDOR_MUNDOS } from "@/lib/i18n/mensajes/servidorMundos";
import { idiomaDeRequest } from "@/lib/i18n/servidor";
import { PRECIOS } from "@/lib/precios";
import catalogo from "@/lib/assets/packs_catalog.json";
import { nombreDeMundo } from "@/lib/catalogoMundos";
import { obtenerPlanCoreVigente, obtenerProyecto } from "@/lib/db";
import { murallaSinPlan } from "@/lib/espacios";
import { avisoLogin, esInvitadoInvisible } from "@/lib/identidad";
import { PACK_CLICKS_PACK } from "@/lib/dbContract";
import { createClient } from "@/lib/supabase/server";

export const runtime = "nodejs";

export async function POST(request: Request, { params }: { params: Promise<{ id: string; pack: string }> }) {
  const { id: projectId, pack } = await params;
  const idioma = idiomaDeRequest(request);
  const r = elegir(RUTAS, idioma);
  const t = elegir(SERVIDOR_MUNDOS, idioma).unlock;

  const entrada = (catalogo.packs as Array<{ clave: string; nombre: string }>).find(
    (p) => p.clave === pack
  );
  if (!entrada || !(PACK_CLICKS_PACK as readonly string[]).includes(pack)) {
    return NextResponse.json({ error: r.mundoNoExiste }, { status: 404 });
  }

  const supabase = await createClient();
  const {
    data: { user },
  } = await supabase.auth.getUser();
  if (!user) {
    return NextResponse.json({ error: r.noAutenticado }, { status: 401 });
  }
  // AUD-09 B12: las mismas puertas que el arranque del mundo (world/start):
  // cuenta real y plan del núcleo. Sin ellas no se abre nada.
  if (esInvitadoInvisible(user)) {
    return NextResponse.json(avisoLogin(idioma), { status: 401 });
  }
  const proyecto = await obtenerProyecto(supabase, projectId);
  if (!proyecto) {
    return NextResponse.json({ error: r.ideaNoEncontrada }, { status: 404 });
  }
  if (!(await obtenerPlanCoreVigente(supabase, projectId))) {
    return NextResponse.json({ error: murallaSinPlan(nombreDeMundo(entrada.clave, idioma), idioma) }, { status: 409 });
  }

  const { error } = await supabase.from("project_unlocks").insert({
    project_id: projectId,
    dominio: pack,
    // Fase 4.5: abrir es gratis; el cobro vive en la entrega del plan.
    creditos_pagados: 0,
  });
  if (error) {
    // 23505 = ya estaba activo: idempotente, no es un error para el usuario.
    if (error.code === "23505") {
      return NextResponse.json({ ok: true, dominio: pack, ya_estaba_activo: true });
    }
    return NextResponse.json({ error: t.noPudimosActivar }, { status: 500 });
  }
  // El precio sale de precios.ts, no del catalogo: el catalogo lo llevaba y
  // decia 3 cuando se cobraban 5. Abrir el mundo es GRATIS; este numero es lo
  // que costara su plan, y tiene que ser el mismo que pinta la tarjeta.
  return NextResponse.json({ ok: true, dominio: pack, creditos: PRECIOS.mundo_activar });
}
