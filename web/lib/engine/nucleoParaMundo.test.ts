/**
 * EL PLAN DE MUNDO SABE QUE TAREAS DEL NUCLEO ESTAN HECHAS (decision del fundador, 10 oct 2026, noche, punto 2b). Caso
 * real de la cuarta medicion final (85248377, Salud y Seguridad): el plan de mundo propuso «Pon clave al Excel de
 * clientes» y «Guarda los contactos fuera del celular, porque hoy no tienes copias», cuando en el nucleo esas tareas ya
 * estaban hechas. El redactor del plan de mundo no recibia nada del nucleo. Ahora recibe, de cada tarea del nucleo
 * vigente que no esta pendiente, el titulo de su tema y su estado; nunca el texto de la tarea (la misma regla que el
 * plan anterior: el texto era del plan, no de la persona).
 */
import { describe, expect, it } from "vitest";
import { nucleoParaMundo } from "./nucleoParaMundo";
import { cargarFamilies } from "../readiness";
import { cargarGrafo } from "./graph";
import { prepararPlan } from "./planRedactor";
import prompts from "../assets/prompts.json";

const TITULOS: Record<string, string> = {
  proteger_datos_clientes: "Protege los Datos de tus Clientes",
  respaldo_informacion: "Respalda tu Información",
  calcular_costo: "Calcula tu Costo Real",
};
const titulo = (id: string) => TITULOS[id] ?? null;

// Las tareas del núcleo de 85248377, con su estado (el texto no viaja).
const TAREAS = [
  { etapa: 2, texto: "Pasa la lista de clientes a un Excel con contraseña", estado: "hecho" as const, completed_at: "2026-10-05T10:00:00Z", nodos_origen: ["proteger_datos_clientes"] },
  { etapa: 2, texto: "Haz una copia de los datos fuera del celular", estado: "hecho" as const, completed_at: "2026-10-06T10:00:00Z", nodos_origen: ["respaldo_informacion"] },
  { etapa: 1, texto: "Suma materiales y tiempo de una maceta", estado: "en_proceso" as const, completed_at: null, nodos_origen: ["calcular_costo"] },
  { etapa: 3, texto: "Habla con la tienda de plantas", estado: "no_aplica" as const, completed_at: null, nodos_origen: ["calcular_costo"] },
  { etapa: 3, texto: "Pregunta precios a tres proveedores", estado: "pendiente" as const, completed_at: null, nodos_origen: ["calcular_costo"] },
  { etapa: 4, texto: "Una tarea sin tema", estado: "hecho" as const, completed_at: "2026-10-01T10:00:00Z", nodos_origen: null },
];

describe("nucleoParaMundo", () => {
  it("caso real 85248377: viajan el título del tema y el estado de lo hecho, en proceso o retirado; nunca el texto", () => {
    const n = nucleoParaMundo(TAREAS, titulo);
    expect(n).toEqual([
      { temas: ["Protege los Datos de tus Clientes"], estado: "hecho" },
      { temas: ["Respalda tu Información"], estado: "hecho" },
      { temas: ["Calcula tu Costo Real"], estado: "en_proceso" },
      { temas: ["Calcula tu Costo Real"], estado: "no_aplica" },
    ]);
    const enviado = JSON.stringify(n);
    expect(enviado).not.toContain("Excel");
    expect(enviado).not.toContain("celular");
    expect(enviado).not.toContain("proveedores");
  });

  it("lo pendiente y las tareas sin tema no viajan; los repetidos (mismo tema y estado) van una vez", () => {
    const n = nucleoParaMundo([...TAREAS, { ...TAREAS[0], texto: "Otra del mismo tema" }], titulo);
    expect(n.filter((x) => x.temas[0] === "Protege los Datos de tus Clientes")).toHaveLength(1);
    expect(n.some((x) => x.estado === "pendiente")).toBe(false);
  });

  it("con fecha de corte (el guion de medición), lo hecho después del plan cuenta como pendiente y no viaja", () => {
    const n = nucleoParaMundo(TAREAS, titulo, "2026-10-05T12:00:00Z");
    expect(n.map((x) => x.temas[0] + ":" + x.estado)).toEqual([
      "Protege los Datos de tus Clientes:hecho",
      "Calcula tu Costo Real:en_proceso",
      "Calcula tu Costo Real:no_aplica",
    ]);
  });
});

describe("el plan de mundo lo recibe y la regla lo describe", () => {
  it("prepararPlan pone actividades_del_nucleo en el payload cuando llega", () => {
    const graph = cargarGrafo();
    const families = cargarFamilies();
    const nucleo = nucleoParaMundo(TAREAS, titulo);
    const prep = prepararPlan(["punto_equilibrio_unidades"], graph, families, "idea", null, null, false, null, null, { nucleo });
    expect(prep.payload.actividades_del_nucleo).toEqual(nucleo);
    const sin = prepararPlan(["punto_equilibrio_unidades"], graph, families, "idea", null, null, false, null);
    expect(sin.payload.actividades_del_nucleo).toBeUndefined();
  });

  it("SYSTEM_PLAN: lo hecho, en proceso o retirado en el núcleo no se propone como pendiente ni se dice que falta", () => {
    expect(prompts.SYSTEM_PLAN).toMatch(/actividades_del_nucleo/);
    expect(prompts.SYSTEM_PLAN).toMatch(/no lo propongas como tarea pendiente ni digas que falta/);
  });
});
