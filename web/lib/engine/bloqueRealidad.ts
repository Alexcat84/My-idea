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
import type { Analytics, AnalyticsMundo } from "../analytics";

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

/**
 * Fase 4.2: el bloque de realidad de UN MUNDO. Un mundo es un subproyecto
 * completo y su seguimiento merece su propio espejo — pero SOLO el suyo.
 *
 * La regla que este bloque existe para cumplir: jamás presentarle al motor las
 * tardanzas del core como si fueran del mundo. Todo lo medido aquí sale de
 * `aMundo` (sus ítems, contra SUS fechas, desde que el usuario lo activó); del
 * proyecto entra UNA sola línea, y va rotulada como lo que es: contexto, no su
 * historia. Sin esa línea el motor planificaría el mundo como si el resto de la
 * vida del usuario no existiera; con más de una, volvería a confundirlos.
 */
export function construirBloqueRealidadMundo(
  aMundo: AnalyticsMundo,
  aProyecto: Analytics,
  nombreMundo: string
): string | null {
  const u = aMundo.universal;
  if (!u.planVigenteAt && u.accionesHechas === 0) return null;

  const L: string[] = [
    `Mi realidad medida en «${nombreMundo}» (registrada por el sistema, no por mi memoria):`,
  ];

  L.push(
    `- Ciclo ${u.ciclosDePlan} de este mundo` +
      (u.planVigenteAt ? `; su plan vigente lleva ${PLURAL(u.diasDeVidaPlanVigente, "día", "días")}.` : ".")
  );

  const ritmo = [
    `${u.accionesVigente.hechas} de ${u.accionesVigente.total} acciones de este mundo hechas en su ciclo`,
    `${u.ritmoAccionesPorSemana} acciones por semana desde que lo activé`,
  ];
  if (u.diasSinAvance !== null) ritmo.push(`${PLURAL(u.diasSinAvance, "día", "días")} desde mi último avance aquí`);
  else ritmo.push("aún sin ningún avance registrado en este mundo");
  L.push(`- Ritmo en este mundo: ${ritmo.join("; ")}.`);

  if (u.duracionPorEtapa.length > 0) {
    const porEtapa = u.duracionPorEtapa.map((e) => `etapa ${e.etapa}: ${PLURAL(e.dias, "día", "días")}`);
    L.push(`- Duración real por etapa de este mundo: ${porEtapa.join("; ")}.`);
  }

  // Cumplimiento: el del MUNDO, contra las fechas de SUS ítems. Misma regla del
  // modo que el core — sin fechas no se juzga contra un calendario.
  const c = aMundo.cumplimiento;
  if (aProyecto.modoCamino === "fechas" && c && c.total > 0) {
    L.push(
      `- Cumplimiento de este mundo contra las fechas que acepté: ${c.aTiempo} a tiempo, ` +
        `${c.adelantadas} adelantadas, ${c.tardias} tardías (de ${c.total} con fecha); desviación media de ` +
        `${c.desviacionMediaDias > 0 ? "+" : ""}${c.desviacionMediaDias} días.`
    );
    if (c.tardiasTop.length > 0) {
      const donde = c.tardiasTop.map(
        (t) => `"${corto(t.texto)}" (etapa ${t.etapa}, ${PLURAL(t.diasRetraso, "día", "días")} tarde)`
      );
      L.push(`- Donde se me atoró el tiempo en este mundo: ${donde.join("; ")}.`);
    }
    if (c.replanificados.length > 0) {
      const cuales = c.replanificados.map((r) => `"${corto(r.texto)}" (etapa ${r.etapa})`);
      L.push(
        `- Moví la fecha de ${PLURAL(c.replanificados.length, "acción", "acciones")} de este mundo: ${cuales.join("; ")}.`
      );
    }
  } else if (aProyecto.modoCamino === "ritmo") {
    L.push("- Elegí llevar esto a mi ritmo, sin fechas: no hay nada que medir contra un calendario.");
  }

  // La ÚNICA línea del proyecto entero, rotulada para que no se confunda con lo
  // de arriba: el mundo no vive en el vacío, pero su historia no es esta.
  const p = aProyecto.universal;
  const contexto = [
    `mi viaje principal va ${p.accionesVigente.hechas} de ${p.accionesVigente.total} acciones en su ciclo ${p.ciclosDePlan}`,
  ];
  if (p.diasSinAvance !== null) contexto.push(`${PLURAL(p.diasSinAvance, "día", "días")} desde mi último avance allí`);
  L.push(`- Contexto de mi proyecto (NO de este mundo): ${contexto.join("; ")}.`);

  return L.join("\n");
}
