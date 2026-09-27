// Ciclo de replanteamiento, Fase 2 (decisiones del fundador, 27 sep 2026): al
// replantear, lo que "me sigue sirviendo" pasa al plan nuevo COMO HECHO, con
// `heredado_de` apuntando a la original (migración 047). La original sigue bajo
// su plan viejo, así que la copia NO puede contarse dos veces en la historia
// (acciones hechas, ritmo, hitos), pero SÍ cuenta como hecha en el plan vigente.
import { describe, expect, it } from "vitest";
import { calcularAnalytics, type EntradaAnalytics, type ItemAnalytics } from "./analytics";

const base = { destacado: false, fecha_base: null, fecha_base_original: null, dominio: "core" };
const items: ItemAnalytics[] = [
  // Plan viejo (pA): la original, hecha el 10 sep.
  { ...base, id: "t1", plan_id: "pA", etapa: 1, estado: "hecho", completed_at: "2026-09-10T15:00:00.000Z", texto: "Hablar con 5" },
  // Plan nuevo (pB): su copia heredada, hecha con la MISMA fecha, y una nueva pendiente.
  { ...base, id: "t9", plan_id: "pB", etapa: 1, estado: "hecho", completed_at: "2026-09-10T15:00:00.000Z", texto: "Hablar con 5", heredado_de: "t1" },
  { ...base, id: "t10", plan_id: "pB", etapa: 1, estado: "pendiente", completed_at: null, texto: "Vender por encargo" },
];
const entrada: EntradaAnalytics = {
  proyectoCreatedAt: "2026-09-01T00:00:00.000Z",
  ahora: "2026-09-15T00:00:00.000Z",
  planesCore: [
    { id: "pA", etiqueta: "completo", created_at: "2026-09-02T00:00:00.000Z", baseline_confirmada_at: null },
    { id: "pB", etiqueta: "replanteamiento", created_at: "2026-09-14T00:00:00.000Z", baseline_confirmada_at: null },
  ],
  items,
  mundos: [],
};

describe("las tareas heredadas no se cuentan dos veces", () => {
  it("una acción hecha en la historia (no dos), y en el plan vigente 1 de 2", () => {
    const a = calcularAnalytics(entrada);
    // A MANO: completadas sin heredadas = [t1] -> 1. Vigente pB: t9 hecha + t10 pendiente -> 1 de 2.
    expect(a.universal.accionesHechas).toBe(1);
    expect(a.universal.accionesVigente).toEqual({ hechas: 1, total: 2 });
    // Un solo día con avance (el 10 sep) y con una sola acción.
    expect(a.universal.avancePorDia).toEqual([{ fecha: "2026-09-10", hechas: 1 }]);
  });
});
