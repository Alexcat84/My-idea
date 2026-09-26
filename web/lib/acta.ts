/**
 * acta.ts: el acta de cierre como FOTO (AUD-09 M04, decisión del fundador del
 * 25 sep 2026; migración 040, tabla project_actas).
 *
 * Al cerrar (el proyecto o un mundo) se guarda una instantánea de lo que el
 * acta muestra. Volver a cerrar tras reabrir guarda OTRA fila al lado, sin
 * pisar la primera. El acta se pinta desde la instantánea; lo que se calcula en
 * vivo se llama "estado actual" y ya no se presenta como acta.
 */
import type { SupabaseClient } from "@supabase/supabase-js";
import type { Analytics } from "./analytics";
import { elegir, LOCALE_BASE, type Locale } from "./i18n/config";
import { interpolarEn } from "./i18n/elision";
import { interpolar } from "./i18n/interpolar";
import { ACTA } from "./i18n/mensajes/acta";

export interface InstantaneaActa {
  acciones: { hechas: number; total: number };
  retiradas: number;
  ciclos: number;
  /** Solo en el acta del proyecto: cada mundo como estaba al cerrar. */
  mundos: Array<{ dominio: string; hechas: number; total: number; completado_at: string | null }>;
}

export interface ActaCierre {
  dominio: string;
  cerrada_at: string;
  cierre_motivo: string | null;
  instantanea: InstantaneaActa;
}

/** La instantánea del cierre de un espacio, tomada de sus analytics. Pura. */
export function instantaneaDeActa(a: Analytics, dominio: string): InstantaneaActa {
  if (dominio === "core") {
    const u = a.universal;
    return {
      acciones: { ...u.accionesVigente },
      retiradas: u.retiradas.length,
      ciclos: u.ciclosDePlan,
      // AUD-09 M37: solo los mundos con su plan (abrir uno no lo activa).
      mundos: a.mundos.filter((m) => m.universal.ciclosDePlan > 0).map((m) => ({
        dominio: m.dominio,
        hechas: m.universal.accionesVigente.hechas,
        total: m.universal.accionesVigente.total,
        completado_at: m.completadoAt,
      })),
    };
  }
  const m = a.mundos.find((x) => x.dominio === dominio);
  const u = m?.universal;
  return {
    acciones: u ? { ...u.accionesVigente } : { hechas: 0, total: 0 },
    retiradas: u ? u.retiradas.length : 0,
    ciclos: u ? u.ciclosDePlan : 0,
    mundos: [],
  };
}

/** Guarda el acta de un cierre. Devuelve false (con rastro) si no se pudo. */
export async function guardarActa(supabase: SupabaseClient, projectId: string, acta: ActaCierre): Promise<boolean> {
  const { error } = await supabase.from("project_actas").insert({
    project_id: projectId,
    dominio: acta.dominio,
    cerrada_at: acta.cerrada_at,
    cierre_motivo: acta.cierre_motivo,
    instantanea: acta.instantanea,
  });
  if (error) {
    console.error(`[acta] no se pudo guardar el acta de ${projectId} (${acta.dominio}) (¿falta la migracion 040?):`, error);
    return false;
  }
  return true;
}

/** El acta más reciente de cada espacio del proyecto (dominio -> acta). */
export async function actasVigentes(supabase: SupabaseClient, projectId: string): Promise<Record<string, ActaCierre>> {
  const { data, error } = await supabase
    .from("project_actas")
    .select("dominio, cerrada_at, cierre_motivo, instantanea, created_at")
    .eq("project_id", projectId)
    .order("created_at", { ascending: true });
  if (error) {
    console.error(`[acta] no se pudieron leer las actas de ${projectId} (¿falta la migracion 040?):`, error);
    return {};
  }
  const out: Record<string, ActaCierre> = {};
  for (const f of (data ?? []) as Array<ActaCierre & { created_at: string }>) {
    out[f.dominio] = { dominio: f.dominio, cerrada_at: f.cerrada_at, cierre_motivo: f.cierre_motivo, instantanea: f.instantanea };
  }
  return out;
}

const pct = (h: number, t: number) => (t > 0 ? ` (${Math.round((h / t) * 100)}%)` : "");

/** Las líneas del acta (la foto) para el informe en markdown. */
export function actaMarkdown(
  acta: ActaCierre,
  nombreMundo: (dominio: string) => string,
  idioma: Locale = LOCALE_BASE
): string[] {
  const t = elegir(ACTA, idioma);
  const i = acta.instantanea;
  const l: string[] = [];
  l.push(t.titulo);
  l.push(interpolarEn(idioma, t.cerradaEl, { fecha: acta.cerrada_at.slice(0, 10) }));
  l.push(
    interpolar(t.accionesAlCerrar, {
      hechas: i.acciones.hechas,
      total: i.acciones.total,
      pct: pct(i.acciones.hechas, i.acciones.total),
    })
  );
  for (const m of i.mundos) {
    const estado = m.completado_at ? interpolarEn(idioma, t.completadoEl, { fecha: m.completado_at.slice(0, 10) }) : t.abierto;
    l.push(
      interpolar(t.mundo, { mundo: nombreMundo(m.dominio), hechas: m.hechas, total: m.total, pct: pct(m.hechas, m.total), estado })
    );
  }
  if (acta.cierre_motivo) {
    l.push("");
    l.push(t.tituloPorQue);
    l.push(`> ${acta.cierre_motivo.replace(/\s+/g, " ").trim()}`);
  }
  l.push("");
  return l;
}
