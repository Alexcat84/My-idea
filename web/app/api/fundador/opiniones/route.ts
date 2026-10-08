/**
 * /api/fundador/opiniones — el panel del fundador lee y exporta las opiniones de todas las cuentas (decisión del
 * fundador, 8 oct 2026). Protegido con FUNDADOR_EMAILS (lib/fundador.ts, esFundador): para cualquier otra identidad
 * es 404, ni siquiera se sabe que existe.
 *
 *   GET ?tipo=&valoracion=            → { opiniones } con su contexto interno
 *   GET ?tipo=&valoracion=&formato=csv → el CSV (lib/opiniones.ts, aCsv), con BOM para que la hoja de cálculo lea
 *                                       los acentos.
 * Prueba: route.test.ts.
 */
import { NextResponse } from "next/server";
import { esFundador } from "@/lib/fundador";
import { aCsv, filtrosDe } from "@/lib/opiniones";
import { listarOpiniones } from "@/lib/opinionesServidor";
import { createClient } from "@/lib/supabase/server";

export async function GET(request: Request) {
  const supabase = await createClient();
  const {
    data: { user },
  } = await supabase.auth.getUser();
  if (!esFundador(user)) return new NextResponse(null, { status: 404 });

  const params = new URL(request.url).searchParams;
  let opiniones;
  try {
    opiniones = await listarOpiniones(filtrosDe(params));
  } catch (e) {
    console.error("[fundador/opiniones] no se pudieron leer:", e);
    return NextResponse.json({ error: String(e) }, { status: 503 });
  }
  if (params.get("formato") === "csv") {
    const fecha = new Date().toISOString().slice(0, 10);
    return new NextResponse(`﻿${aCsv(opiniones)}`, {
      headers: {
        "content-type": "text/csv; charset=utf-8",
        "content-disposition": `attachment; filename="opiniones-${fecha}.csv"`,
        "cache-control": "no-store",
      },
    });
  }
  return NextResponse.json({ opiniones }, { headers: { "cache-control": "no-store" } });
}
