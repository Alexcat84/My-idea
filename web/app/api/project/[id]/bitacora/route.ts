/**
 * GET /api/project/[id]/bitacora — Fase 4.8: las entradas de la bitácora en
 * JSON, para la PÁGINA en vivo (verla antes de imprimir). Misma fuente que el
 * documento .md/PDF: una sola historia. Cero motor, cero créditos.
 *
 * Fase 3 (Espacios): con `?dominio=X` devuelve la bitácora POR ESPACIO — un
 * FILTRO de esa misma fuente única (bitacoraDeEspacio), jamás un registro
 * paralelo — más su `markdown` titulado "Bitácora de {espacio}" (el MISMO texto
 * canónico del servidor, bitacoraMarkdown). Las entradas no-derivables (dominio
 * null) viven solo en la global: aquí nunca aparecen.
 */
import { NextResponse } from "next/server";
import { elegir } from "@/lib/i18n/config";
import { interpolar } from "@/lib/i18n/interpolar";
import { RUTAS } from "@/lib/i18n/mensajes/servidorRutas";
import { SERVIDOR_PROYECTO } from "@/lib/i18n/mensajes/servidorProyecto";
import { idiomaDeRequest } from "@/lib/i18n/servidor";
import { bitacoraDeEspacio, bitacoraMarkdown } from "@/lib/bitacoraCliente";
import catalogo from "@/lib/assets/packs_catalog.json";
import { cargarEntradasBitacora } from "@/lib/bitacoraDatos";
import { obtenerProyecto } from "@/lib/db";
import { esEspacioCore } from "@/lib/espacios";
import { nombreDeIdea } from "@/lib/ideas";
import { createClient } from "@/lib/supabase/server";

export const runtime = "nodejs";

export async function GET(request: Request, { params }: { params: Promise<{ id: string }> }) {
  const { id: projectId } = await params;
  const dominio = new URL(request.url).searchParams.get("dominio");
  const idioma = idiomaDeRequest(request);
  const r = elegir(RUTAS, idioma);
  const t = elegir(SERVIDOR_PROYECTO, idioma).bitacora;

  const supabase = await createClient();
  const {
    data: { user },
  } = await supabase.auth.getUser();
  if (!user) return NextResponse.json({ error: r.noAutenticado }, { status: 401 });
  const proyecto = await obtenerProyecto(supabase, projectId);
  if (!proyecto) return NextResponse.json({ error: r.ideaNoEncontrada }, { status: 404 });

  const nombre = nombreDeIdea(proyecto.titulo, proyecto.entrada_original);
  const todas = await cargarEntradasBitacora(supabase, projectId, proyecto, nombre);

  // Global (sin dominio): la historia entera, como siempre.
  if (!dominio) return NextResponse.json({ nombre, entradas: todas });

  // Por espacio: un filtro de la fuente única. Core = el nombre de la idea; un
  // mundo = su nombre de cara (jamás la clave técnica).
  const entradas = bitacoraDeEspacio(todas, dominio);
  const nombreEspacio = esEspacioCore(dominio)
    ? nombre
    : (catalogo as { packs: Array<{ clave: string; nombre: string }> }).packs.find((p) => p.clave === dominio)?.nombre ??
      dominio;
  const markdown = bitacoraMarkdown(nombreEspacio, entradas, new Date().toISOString(), interpolar(t.tituloEspacio, { espacio: nombreEspacio }));
  return NextResponse.json({ nombre: nombreEspacio, entradas, markdown });
}
