// Scheduler F1 — la PERSISTENCIA de la estimación: insertarChecklist escribe la
// banda y espera_externa junto al ítem al nacer el plan. El caso que importa de
// verdad es el FALLBACK: un plan cuyos ítems no traen estimación se inserta
// igual, con banda null, en vez de romper el nacimiento del plan.
import { describe, expect, it } from "vitest";
import { crearSupabaseFalso, estadoFalsoVacio } from "./testUtils/fakeSupabase";
import { insertarChecklist } from "./db";
import type { SupabaseClient } from "@supabase/supabase-js";

function falso() {
  const estado = estadoFalsoVacio();
  return { estado, client: crearSupabaseFalso(estado) as unknown as SupabaseClient };
}

describe("insertarChecklist: persiste la banda estimada (Scheduler F1)", () => {
  it("guarda banda y espera_externa por ítem", async () => {
    const { estado, client } = falso();
    await insertarChecklist(
      client,
      "p1",
      "plan-1",
      [
        { etapa: 1, orden: 1, texto: "Redacta el perfil", destacado: false, banda: "M", espera_externa: false },
        { etapa: 1, orden: 2, texto: "Escribe y espera respuesta", destacado: true, banda: "S", espera_externa: true },
      ],
      "core"
    );
    expect(estado.checklistItems).toHaveLength(2);
    expect(estado.checklistItems[0]).toMatchObject({ texto: "Redacta el perfil", banda: "M", espera_externa: false });
    expect(estado.checklistItems[1]).toMatchObject({ banda: "S", espera_externa: true });
  });

  it("FALLBACK: sin estimación, el ítem se inserta con banda null (el plan no se bloquea)", async () => {
    const { estado, client } = falso();
    await insertarChecklist(client, "p1", "plan-1", [{ etapa: 1, orden: 1, texto: "Compra dos termos", destacado: false }]);
    expect(estado.checklistItems).toHaveLength(1);
    expect(estado.checklistItems[0]).toMatchObject({ banda: null, espera_externa: null });
  });

  it("estimación PARCIAL: los ítems que el lote no cubrió quedan sin banda, los demás con la suya", async () => {
    const { estado, client } = falso();
    await insertarChecklist(client, "p1", "plan-1", [
      { etapa: 1, orden: 1, texto: "Con banda", destacado: false, banda: "L", espera_externa: false },
      { etapa: 1, orden: 2, texto: "Sin banda", destacado: false, banda: null, espera_externa: null },
    ]);
    expect(estado.checklistItems[0].banda).toBe("L");
    expect(estado.checklistItems[1].banda).toBeNull();
  });

  it("el dominio del plan viaja con cada ítem (core o mundo)", async () => {
    const { estado, client } = falso();
    await insertarChecklist(
      client,
      "p1",
      "plan-m",
      [{ etapa: 1, orden: 1, texto: "Tarea del mundo", destacado: false, banda: "XL", espera_externa: false }],
      "quality"
    );
    expect(estado.checklistItems[0]).toMatchObject({ dominio: "quality", banda: "XL" });
  });

  it("lista vacía: no escribe nada", async () => {
    const { estado, client } = falso();
    await insertarChecklist(client, "p1", "plan-1", []);
    expect(estado.checklistItems).toHaveLength(0);
  });
});
