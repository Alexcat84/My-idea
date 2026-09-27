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
import { idiomaDeDocumentos } from "@/lib/i18n/idiomaDocumento";
import { interpolar } from "@/lib/i18n/interpolar";
import { RUTAS } from "@/lib/i18n/mensajes/servidorRutas";
import { SERVIDOR_PROYECTO } from "@/lib/i18n/mensajes/servidorProyecto";
import { BITACORA } from "@/lib/i18n/mensajes/bitacora";
import { idiomaDeRequest } from "@/lib/i18n/servidor";
import { bitacoraDeEspacio, bitacoraMarkdown } from "@/lib/bitacoraCliente";
import { nombreDeMundo } from "@/lib/catalogoMundos";
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

  const supabase = await createClient();
  const {
    data: { user },
  } = await supabase.auth.getUser();
  if (!user) return NextResponse.json({ error: r.noAutenticado }, { status: 401 });
  const proyecto = await obtenerProyecto(supabase, projectId);
  if (!proyecto) return NextResponse.json({ error: r.ideaNoEncontrada }, { status: 404 });

  const nombre = nombreDeIdea(proyecto.titulo, proyecto.entrada_original);
  const todas = await cargarEntradasBitacora(supabase, projectId, proyecto, nombre, idioma);

  // Global (sin dominio): la historia entera, como siempre.
  if (!dominio) return NextResponse.json({ nombre, entradas: todas });

  // Por espacio: un filtro de la fuente única. Core = el nombre de la idea; un
  // mundo = su nombre de cara (jamás la clave técnica).
  const entradas = bitacoraDeEspacio(todas, dominio);
  // i18n F6 (D2): el documento (el .md, el papel del PDF y su archivo) va en el
  // idioma del proyecto (lib/i18n/idiomaDocumento.ts); la pantalla, en el de la
  // interfaz.
  const idiomaDoc = idiomaDeDocumentos(proyecto, idioma);
  const nombreEspacio = esEspacioCore(dominio) ? nombre : nombreDeMundo(dominio, idiomaDoc);
  const nombrePantalla = esEspacioCore(dominio) ? nombre : nombreDeMundo(dominio, idioma);
  const entradasDoc =
    idiomaDoc === idioma
      ? entradas
      : bitacoraDeEspacio(await cargarEntradasBitacora(supabase, projectId, proyecto, nombre, idiomaDoc), dominio);
  const tDoc = elegir(SERVIDOR_PROYECTO, idiomaDoc).bitacora;
  const tituloDoc = interpolar(tDoc.tituloEspacio, { espacio: nombreEspacio });
  const markdown = bitacoraMarkdown(nombreEspacio, entradasDoc, new Date().toISOString(), tituloDoc, undefined, idiomaDoc);
  return NextResponse.json({
    nombre: nombrePantalla,
    entradas,
    markdown,
    // El papel y el nombre del archivo, en el idioma del documento.
    idioma: idiomaDoc,
    papel: { entradas: entradasDoc, nombre: nombreEspacio },
    archivo: interpolar(elegir(BITACORA, idiomaDoc).espacio.archivo, { nombre: nombreEspacio }),
  });
}
