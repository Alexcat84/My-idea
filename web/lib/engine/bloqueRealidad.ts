/**
 * bloqueRealidad.ts — Fase 4.0 §3 (docs/FLUJO_TRACKING.md): el espejo para EL
 * MOTOR. El Análisis le muestra al humano que la etapa 2 tardó tres semanas de
 * más; este bloque le dice LO MISMO al motor que regenera el plan. Ambos beben
 * de analytics.ts: aquí NO se recalcula nada, solo se redacta.
 *
 * Determinístico y compacto (cero LLM). Se adjunta al mensaje del follow y
 * queda auditable en la bitácora de la sesión.
 *
 * Regla del modo: si el usuario eligió "a mi ritmo", el bloque lleva SOLO
 * duraciones y ritmo — jamás lenguaje de cumplimiento. No se juzga contra
 * fechas que el usuario eligió no tener.
 */
import type { Analytics } from "../analytics";

/** Recorta un texto de ítem para que el bloque no se infle. */
function corto(texto: string, max = 70): string {
  const t = (texto ?? "").replace(/\s+/g, " ").trim();
  return t.length > max ? `${t.slice(0, max)}…` : t;
}

const PLURAL = (n: number, sing: string, plur: string) => `${n} ${n === 1 ? sing : plur}`;

/**
 * El bloque de realidad, o null si no hay nada medido que contar (proyecto
 * recién nacido sin plan vigente ni avances).
 */
export function construirBloqueRealidad(a: Analytics): string | null {
  const u = a.universal;
  if (!u.planVigenteAt && u.accionesHechas === 0) return null;

  const L: string[] = ["Mi realidad medida (registrada por el sistema, no por mi memoria):"];

  // Ciclo: numero, y cuanto lleva vivo el plan vigente.
  const ciclo = `- Ciclo ${u.ciclosDePlan}` + (u.planVigenteAt ? `; el plan vigente lleva ${PLURAL(u.diasDeVidaPlanVigente, "día", "días")}.` : ".");
  L.push(ciclo);

  // Ritmo real: siempre, en cualquier modo.
  const ritmo = [
    `${u.accionesVigente.hechas} de ${u.accionesVigente.total} acciones hechas en este ciclo`,
    `${u.ritmoAccionesPorSemana} acciones por semana`,
    `racha más larga de ${PLURAL(u.rachaMasLargaDias, "día", "días")}`,
  ];
  if (u.diasSinAvance !== null) ritmo.push(`${PLURAL(u.diasSinAvance, "día", "días")} desde mi último avance`);
  else ritmo.push("aún sin ningún avance registrado");
  L.push(`- Ritmo: ${ritmo.join("; ")}.`);

  // Duracion real por etapa: el dato honesto que existe en los dos modos.
  if (u.duracionPorEtapa.length > 0) {
    const porEtapa = u.duracionPorEtapa.map((e) => `etapa ${e.etapa}: ${PLURAL(e.dias, "día", "días")}`);
    L.push(`- Duración real por etapa: ${porEtapa.join("; ")}.`);
  }

  // Cumplimiento: SOLO en modo fechas y con baseline confirmada.
  const conFechas = a.modoCamino === "fechas" && a.cumplimiento !== null;
  if (conFechas) {
    const c = a.cumplimiento!;
    L.push(
      `- Cumplimiento contra las fechas que acepté: ${c.aTiempo} a tiempo, ${c.adelantadas} adelantadas, ` +
        `${c.tardias} tardías (de ${c.totalConFecha} con fecha); desviación media de ` +
        `${c.desviacionMediaDias > 0 ? "+" : ""}${c.desviacionMediaDias} días.`
    );
    if (c.tardiasTop.length > 0) {
      const donde = c.tardiasTop.map((t) => `"${corto(t.texto)}" (etapa ${t.etapa}, ${PLURAL(t.diasRetraso, "día", "días")} tarde)`);
      L.push(`- Donde se me atoró el tiempo: ${donde.join("; ")}.`);
    }
    if (c.replanificados.length > 0) {
      const cuales = c.replanificados.map((r) => `"${corto(r.texto)}" (etapa ${r.etapa})`);
      L.push(`- Moví la fecha de ${PLURAL(c.replanificados.length, "acción", "acciones")}: ${cuales.join("; ")}.`);
    }
  } else if (a.modoCamino === "ritmo") {
    L.push("- Elegí llevar esto a mi ritmo, sin fechas: no hay nada que medir contra un calendario.");
  }

  return L.join("\n");
}
