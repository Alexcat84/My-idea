/**
 * EL RITUAL DE FECHAS NO SE ROMPE CON UNA TAREA HECHA O RETIRADA (ficha
 * ritual-fechas-sin-fecha de docs/PENDIENTES.md, hallada en i18n F2; decisión del
 * fundador, 25 sep 2026: arreglarla con su prueba en rojo).
 *
 * El defecto: el ritual (RitualFechas en ManosALaObra) listaba en la primera
 * corrida TODAS las tareas, y en el recálculo quitaba solo las hechas. Pero el
 * repartidor (calcularFechasRitual, AUD-09 M07) solo le da fecha a lo PENDIENTE:
 * una tarea hecha o retirada ("no aplica") llegaba a la pantalla sin fecha, y
 * fechaHumana(isoDesdeInputLocal(undefined)) lanzaba "RangeError: Invalid time
 * value": la pantalla se rompía. Guardar tenía el mismo problema.
 *
 * La regla del arreglo: el ritual lista exactamente lo que el repartidor fecha.
 */
import { describe, expect, it } from "vitest";
import { CAPACIDAD_DEFAULT } from "@/lib/empaquetado";
import { fechaHumana, isoDesdeInputLocal } from "@/lib/fechas";
import { calcularFechasRitual, tramosDelRitual } from "./ManosALaObra";
import type { GrupoRitual, ItemChecklistUI } from "./ManosALaObra";

const ANCLA = "2026-08-03T10:00:00";

function item(over: Partial<ItemChecklistUI> & { id: string; etapa: number }): ItemChecklistUI {
  return {
    plan_id: "plan-1",
    dominio: "core",
    orden: 1,
    texto: "una tarea",
    destacado: false,
    estado: "pendiente",
    nota: null,
    completed_at: null,
    no_aplica_motivo: null,
    fecha_base: null,
    fecha_base_origen: null,
    fecha_base_original: null,
    banda: null,
    espera_externa: null,
    created_at: ANCLA,
    updated_at: ANCLA,
    ...over,
  };
}

// Un plan con una pendiente, una empezada, una hecha y una retirada.
const grupos: GrupoRitual[] = [
  {
    dominio: "core",
    nombre: "Tu viaje principal",
    planCreatedAt: ANCLA,
    titulos: {},
    items: [
      item({ id: "pendiente", etapa: 1 }),
      item({ id: "empezada", etapa: 1, estado: "empezado" }),
      item({ id: "hecha", etapa: 1, estado: "hecho", completed_at: ANCLA }),
      item({ id: "retirada", etapa: 2, estado: "no_aplica", no_aplica_motivo: "ya no aplica" }),
    ],
  },
];

describe("el ritual lista exactamente lo que recibe fecha", () => {
  it("el mecanismo del defecto: una fecha que falta rompe la pantalla", () => {
    expect(() => fechaHumana(isoDesdeInputLocal(undefined as unknown as string))).toThrow(RangeError);
  });

  it.each([false, true])("soloPendientes=%s: ni la hecha ni la retirada entran al ritual", (soloPendientes) => {
    const ids = tramosDelRitual(grupos, soloPendientes).flatMap((g) => g.items.map((i) => i.id));
    expect(ids).toEqual(["pendiente", "empezada"]);
  });

  it.each([false, true])("soloPendientes=%s: cada tarea que el ritual muestra tiene su fecha (nada se rompe al pintar ni al guardar)", (soloPendientes) => {
    const tramos = tramosDelRitual(grupos, soloPendientes);
    const { fechas } = calcularFechasRitual(tramos, {
      diaPreferido: null,
      capacidad: CAPACIDAD_DEFAULT,
      empaquetable: false,
      hoy: ANCLA,
    });
    for (const it of tramos.flatMap((g) => g.items)) {
      expect(fechas[it.id], it.id).toMatch(/^\d{4}-\d{2}-\d{2}$/);
      expect(() => fechaHumana(isoDesdeInputLocal(fechas[it.id]))).not.toThrow();
    }
  });

  it("un tramo que se queda sin nada pendiente no aparece", () => {
    const todoHecho: GrupoRitual[] = [{ ...grupos[0], items: [item({ id: "h", etapa: 1, estado: "hecho" })] }];
    expect(tramosDelRitual(todoHecho, false)).toEqual([]);
  });
});
