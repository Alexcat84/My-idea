/**
 * El CONTEO ANÓNIMO de los idiomas en que se escriben las ideas (i18n F5,
 * añadido del fundador del 25 sep 2026; migración 046). Sirve para decidir qué
 * idiomas vienen después. Solo viajan dos códigos (el de la idea y el de la
 * interfaz): la base suma uno al mes en curso, sin persona ni idea.
 *
 * Usa el cliente de service_role (la función no la puede llamar nadie más).
 * Nunca lanza: el conteo no puede tumbar la creación de una idea.
 */
import type { SupabaseClient } from "@supabase/supabase-js";
import { createAdminClient } from "@/lib/supabase/admin";

export async function contarIdiomaDeIdea(idiomaIdea: string, idiomaInterfaz: string, admin?: SupabaseClient): Promise<void> {
  try {
    const { error } = await (admin ?? createAdminClient()).rpc("contar_idioma_de_idea", { p_idioma_idea: idiomaIdea, p_idioma_interfaz: idiomaInterfaz });
    if (error) console.error("[contarIdiomaDeIdea] no se contó (¿falta la migración 046?):", error.message);
  } catch (e) {
    console.error("[contarIdiomaDeIdea] no se contó:", e instanceof Error ? e.message : e);
  }
}
