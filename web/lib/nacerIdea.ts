/**
 * Crear una idea nueva (i18n F5): nace con el idioma de SU texto
 * (DISENO §3.3; D2) y ese idioma suma uno al conteo anónimo (046). Las tres
 * puertas de entrada (session/start, organizer, organizer/stream) crean la idea
 * por aquí, para que ninguna se salte la detección ni el conteo.
 */
import type { SupabaseClient } from "@supabase/supabase-js";
import type { ActiveLocale } from "@/lib/i18n/config";
import { crearProyecto } from "@/lib/db";
import { detectarIdioma } from "@/lib/i18n/detectarIdioma";
import { contarIdiomaDeIdea } from "@/lib/i18n/conteoIdiomas";

export async function nacerIdea(
  supabase: SupabaseClient,
  userId: string,
  texto: string,
  interfaz: ActiveLocale
): Promise<{ projectId: string; idioma: string }> {
  const { codigo } = detectarIdioma(texto, interfaz);
  const projectId = await crearProyecto(supabase, userId, texto, codigo);
  await contarIdiomaDeIdea(codigo, interfaz);
  return { projectId, idioma: codigo };
}
