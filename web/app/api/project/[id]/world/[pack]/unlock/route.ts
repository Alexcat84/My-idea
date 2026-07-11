/**
 * POST /api/project/[id]/world/[pack]/unlock — Fase 3.5, stub de créditos
 * (Stripe llega en fase posterior): valida el pack contra el catálogo,
 * inserta el unlock con los créditos del catálogo (creditos_pagados) y
 * desde ese momento el dominio EXISTE para el motor (el muro de filtros
 * deja pasar). Idempotente: activar dos veces responde ok sin duplicar
 * (UNIQUE project_id+dominio).
 */
import { NextResponse } from "next/server";
import catalogo from "@/lib/assets/packs_catalog.json";
import { obtenerProyecto } from "@/lib/db";
import { PACK_CLICKS_PACK } from "@/lib/dbContract";
import { createClient } from "@/lib/supabase/server";

export const runtime = "nodejs";

export async function POST(_request: Request, { params }: { params: Promise<{ id: string; pack: string }> }) {
  const { id: projectId, pack } = await params;

  const entrada = (catalogo.packs as Array<{ clave: string; nombre: string; creditos_activar: number }>).find(
    (p) => p.clave === pack
  );
  if (!entrada || !(PACK_CLICKS_PACK as readonly string[]).includes(pack)) {
    return NextResponse.json({ error: "ese mundo no existe" }, { status: 404 });
  }

  const supabase = await createClient();
  const {
    data: { user },
  } = await supabase.auth.getUser();
  if (!user) {
    return NextResponse.json({ error: "no autenticado" }, { status: 401 });
  }
  const proyecto = await obtenerProyecto(supabase, projectId);
  if (!proyecto) {
    return NextResponse.json({ error: "idea no encontrada" }, { status: 404 });
  }

  const { error } = await supabase.from("project_unlocks").insert({
    project_id: projectId,
    dominio: pack,
    creditos_pagados: entrada.creditos_activar,
  });
  if (error) {
    // 23505 = ya estaba activo: idempotente, no es un error para el usuario.
    if (error.code === "23505") {
      return NextResponse.json({ ok: true, dominio: pack, ya_estaba_activo: true });
    }
    return NextResponse.json({ error: "no pudimos activar el mundo, intenta de nuevo" }, { status: 500 });
  }
  return NextResponse.json({ ok: true, dominio: pack, creditos: entrada.creditos_activar });
}
