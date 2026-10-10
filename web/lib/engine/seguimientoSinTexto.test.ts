/**
 * LA TERCERA RUTA (decision del fundador, 10 oct 2026). En la segunda medicion final, la feria de agosto (inventada en un
 * plan) volvio dos veces por el MENSAJE DE ENTRADA DEL SEGUIMIENTO: la app lo compone con el texto de cada tarea del plan
 * anterior ("- Anota si la feria local de agosto te sirve...") y con el texto de las tareas atrasadas en el bloque de
 * realidad. Ahora ese mensaje lleva el estado de cada tarea, la nota de la persona y el titulo de su tema, nunca el texto
 * de la tarea; el bloque de realidad nombra solo la etapa.
 */
import { describe, expect, it } from "vitest";
import { componerMensajeSeguimiento, itemsDelUltimoPlanDe, type FilaChecklist } from "./seguimientoComposer";
import { construirBloqueRealidad } from "./bloqueRealidad";

const FERIA = "Anota si la feria local de agosto te sirve para probar el precio con gente que no te conoce";

describe("el mensaje del seguimiento nunca lleva el texto de una tarea", () => {
  it("caso real (31ebf0ea, c73e86f8): la feria no viaja; viajan el estado, la nota y el tema", () => {
    const m = componerMensajeSeguimiento({
      items: [
        { etapa: 1, texto: FERIA, destacado: false, estado: "pendiente", temas: ["Valida tu Precio"] },
        { etapa: 1, texto: "Multiplica tus horas por tu valor hora", destacado: false, estado: "hecho", nota: "ya sé que es 130", temas: ["Calcula tu Costo Real"] },
        { etapa: 2, texto: "Habla con la tienda", destacado: false, estado: "no_aplica", noAplicaMotivo: "cerró la tienda", temas: ["Elige tus Canales"] },
        { etapa: 2, texto: "Otra cosa sin tema", destacado: false, estado: "en_proceso" },
      ],
    });
    expect(m).not.toContain("feria");
    expect(m).not.toContain("Multiplica tus horas");
    expect(m).not.toContain("Habla con la tienda");
    expect(m).not.toContain("Otra cosa sin tema");
    expect(m).toContain("Calcula tu Costo Real (nota: ya sé que es 130)");
    expect(m).toContain("Valida tu Precio");
    expect(m).toContain("Elige tus Canales (porque: cerró la tienda)");
    expect(m).toMatch(/HECHO \(1\)/);
    expect(m).toMatch(/una tarea de la etapa 2/);
  });

  it("itemsDelUltimoPlanDe resuelve el tema de cada tarea por sus nodos de origen", () => {
    const filas: FilaChecklist[] = [
      { plan_id: "p1", etapa: 1, texto: FERIA, destacado: false, estado: "pendiente", created_at: "2026-10-08T23:00:00Z", nodos_origen: ["precio_n"] },
    ];
    const items = itemsDelUltimoPlanDe(filas, "core", (id) => (id === "precio_n" ? "Valida tu Precio" : null));
    expect(items[0].temas).toEqual(["Valida tu Precio"]);
  });

  it("el bloque de realidad nombra la etapa, no el texto de la tarea atrasada, la movida ni la retirada", () => {
    const b = construirBloqueRealidad({
      universal: {
        planVigenteAt: "2026-10-01T00:00:00Z", accionesHechas: 1, ciclosDePlan: 1, diasDeVidaPlanVigente: 9,
        accionesVigente: { hechas: 1, total: 3 }, ritmoAccionesPorSemana: 1, rachaMasLargaDias: 1, diasSinAvance: 2,
        retiradas: [{ texto: "Habla con la tienda de plantas", etapa: 3, motivo: "cerró la tienda" }],
        duracionPorEtapa: [],
      },
      modoCamino: "fechas",
      cumplimiento: {
        aTiempo: 1, adelantadas: 0, tardias: 1, totalConFecha: 2, desviacionMediaDias: 3,
        tardiasTop: [{ texto: FERIA, etapa: 2, diasRetraso: 5 }],
        replanificados: [{ texto: "Llama a la tienda de plantas", etapa: 1 }],
      },
      duracionPorEtapa: [],
    } as never);
    expect(b ?? "").not.toContain("feria");
    expect(b ?? "").not.toContain("Llama a la tienda");
    expect(b ?? "").not.toContain("Habla con la tienda");
    expect(b ?? "").toContain("una acción de la etapa 2");
    expect(b ?? "").toContain("una tarea de la etapa 3 (cerró la tienda)");
  });
});

describe("el guion de medición pasa el mensaje guardado al formato sin texto (como lo compone hoy la app)", () => {
  // Extracto real del mensaje guardado de la sesión de 31ebf0ea (8 oct 2026).
  const GUARDADO = [
    "Desde el último plan, este es mi avance real:",
    "HECHO (1):",
    "- Suma materiales y tiempo para obtener el costo real por unidad de cada tamaño.",
    "SIN EMPEZAR (2):",
    "- Repite la cuenta por separado para las chicas y las medianas, porque el tamaño cambia tanto el material como el tiempo.",
    "- Anota si la feria local de agosto te sirve para probar el precio con gente que no te conoce, y qué resultado mínimo te haría quedarte con él.",
    "Además: El proveedor de cemento subio precios a mitad de camino.",
    "",
    "Mi realidad medida (registrada por el sistema, no por mi memoria):",
    '- Donde se me atoró el tiempo: "Suma materiales y tiempo para obtener el costo real por unidad de cada tamaño." (etapa 1, 7 días tarde).',
    '- Moví la fecha de 1 acción: "Toma la última tanda, anota cuánto gastaste en materiales" (etapa 1).',
    '- Retiré 1 tarea por no aplicar: "Habla con la tienda de plantas" (cerró la tienda).',
    "",
    "Lo que más me interesa profundizar ahora: Quiero cerrar el costo real por pieza.",
  ].join("\n");
  const FILAS = [
    { texto: "Suma materiales y tiempo para obtener el costo real por unidad de cada tamaño.", etapa: 1, nodos_origen: ["costo_n"] },
    { texto: "Repite la cuenta por separado para las chicas y las medianas, porque el tamaño cambia tanto el material como el tiempo.", etapa: 1, nodos_origen: ["costo_n"] },
    { texto: "Anota si la feria local de agosto te sirve para probar el precio con gente que no te conoce, y qué resultado mínimo te haría quedarte con él.", etapa: 4, nodos_origen: null },
  ];
  it("ni la feria, ni la causa inventada de los tamaños, ni ninguna tarea viajan; sí las notas, el enfoque y lo medido", async () => {
    const { mensajeAlFormatoSinTexto } = await import("./seguimientoComposer");
    const m = mensajeAlFormatoSinTexto(GUARDADO, FILAS, (id) => (id === "costo_n" ? "Calcula tu Costo Real" : null));
    expect(m).not.toContain("feria");
    expect(m).not.toContain("chicas y las medianas");
    expect(m).not.toContain("Toma la última tanda");
    expect(m).not.toContain("Habla con la tienda");
    expect(m).toContain("HECHO (1):\n- Calcula tu Costo Real");
    expect(m).toContain("- una tarea de la etapa 4");
    expect(m).toContain("una acción de la etapa 1 (7 días tarde)");
    expect(m).toContain("una tarea (cerró la tienda)");
    expect(m).toContain("Además: El proveedor de cemento subio precios a mitad de camino.");
    expect(m).toContain("Lo que más me interesa profundizar ahora: Quiero cerrar el costo real por pieza.");
  });
});
