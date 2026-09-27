// PRINCIPIO 1, memoria de contexto de principio a fin (decision del fundador, 28 sep
// 2026): el contexto completo del usuario viaja SIEMPRE y se GUARDA EN LA BASE del
// proyecto (projects.memoria), actualizado cada turno. Nada se pierde dentro de una
// sesion ni entre sesiones. Aqui las funciones puras de esa memoria.
import { describe, expect, it } from "vitest";
import {
  agregarAlHilo,
  aperturaDeSesion,
  fichaVacia,
  fusionarFicha,
  memoriaDe,
  textoContextoProyecto,
  textoFichaActual,
  type MemoriaProyecto,
} from "./memoria";

describe("la ficha de contexto se fusiona sin perder nada", () => {
  it("un dato nuevo entra; un desconocido o vacio nunca pisa uno conocido", () => {
    const a = fusionarFicha(fichaVacia(), {
      papel: "dueno",
      tiene_jefe: false,
      equipo: { personas: 2, descripcion: "dos empleados recien contratados" },
      sector: "taller de macetas de cemento",
    });
    const b = fusionarFicha(a, { papel: "desconocido", tiene_jefe: null, sector: "", etapa: "ejecucion" });
    expect(b.papel).toBe("dueno");
    expect(b.tiene_jefe).toBe(false);
    expect(b.sector).toBe("taller de macetas de cemento");
    expect(b.equipo).toEqual({ personas: 2, descripcion: "dos empleados recien contratados" });
    expect(b.etapa).toBe("ejecucion");
  });

  it("las frases textuales solo se AÑADEN, sin repetir", () => {
    const a = fusionarFicha(fichaVacia(), { dijo_textual: ["termino haciendo yo el trabajo"] });
    const b = fusionarFicha(a, { dijo_textual: ["termino haciendo yo el trabajo", "les hablo solo cuando hay un problema", "  "] });
    expect(b.dijo_textual).toEqual(["termino haciendo yo el trabajo", "les hablo solo cuando hay un problema"]);
  });

  it("la prioridad declarada se reemplaza solo cuando llega una", () => {
    const a = fusionarFicha(fichaVacia(), { prioridad_declarada: { texto: "dirigir a mis dos empleados", conteo: 1 } });
    expect(fusionarFicha(a, { prioridad_declarada: null }).prioridad_declarada).toEqual({ texto: "dirigir a mis dos empleados", conteo: 1 });
    expect(fusionarFicha(a, { prioridad_declarada: { texto: "dirigir a mis dos empleados", conteo: 2 } }).prioridad_declarada?.conteo).toBe(2);
  });
});

describe("la memoria del proyecto", () => {
  it("una memoria vacia o de antes de la 049 ({} en la base) se lee como memoria vacia", () => {
    expect(memoriaDe({})).toEqual({ version: 1, ficha: fichaVacia(), hilo: [] });
    expect(memoriaDe(null)).toEqual({ version: 1, ficha: fichaVacia(), hilo: [] });
  });

  it("el hilo solo crece por el final", () => {
    const m0 = memoriaDe({});
    const e1 = { sesion: "s1", dominio: "core", nodo: "n1", pregunta: "¿Que vendes?", respuesta: "Macetas", en: "2026-09-28T10:00:00Z" };
    const e2 = { sesion: "s1", dominio: "core", nodo: "n2", pregunta: "¿A quien?", respuesta: "A viveros", en: "2026-09-28T10:02:00Z" };
    const m2 = agregarAlHilo(agregarAlHilo(m0, e1), e2);
    expect(m2.hilo).toEqual([e1, e2]);
    expect(m0.hilo).toEqual([]); // no muta
  });
});

describe("el texto del contexto que viaja a la IA", () => {
  const m: MemoriaProyecto = {
    version: 1,
    ficha: fusionarFicha(fichaVacia(), { papel: "dueno", tiene_jefe: false, equipo: { personas: 2, descripcion: null } }),
    hilo: [{ sesion: "s0", dominio: "core", nodo: "n1", pregunta: "¿Que vendes?", respuesta: "Macetas de cemento", en: "2026-09-27T10:00:00Z" }],
  };

  it("lleva la idea, el estado vivo, la ficha y todo lo contado antes, en ese orden", () => {
    const t = textoContextoProyecto(m, { entradaOriginal: "Quiero vender macetas", estadoVivo: "Taller con dos empleados." });
    const orden = ["Quiero vender macetas", "Taller con dos empleados.", '"papel": "dueno"', "Macetas de cemento"].map((x) => t.indexOf(x));
    expect(orden.every((i) => i >= 0)).toBe(true);
    expect([...orden].sort((a, b) => a - b)).toEqual(orden);
  });

  it("es determinista: la misma memoria da el mismo texto (de eso depende el cache)", () => {
    const a = textoContextoProyecto(m, { entradaOriginal: "X", estadoVivo: null });
    const b = textoContextoProyecto(memoriaDe(JSON.parse(JSON.stringify(m))), { entradaOriginal: "X", estadoVivo: null });
    expect(a).toBe(b);
  });

  it("la ficha actual se presenta como la que manda", () => {
    expect(textoFichaActual(m.ficha)).toMatch(/^FICHA DE CONTEXTO ACTUAL/);
    expect(textoFichaActual(m.ficha)).toContain('"tiene_jefe": false');
  });
});

describe("aperturaDeSesion", () => {
  it("da la foto del proyecto (con lo contado en el nucleo) y la ficha guardada", () => {
    const a = aperturaDeSesion({
      entrada_original: "Quiero vender macetas",
      estado_vivo: "Taller con dos empleados.",
      memoria: { ficha: { papel: "dueno" }, hilo: [{ sesion: "s0", dominio: "core", nodo: "n1", pregunta: "¿Que vendes?", respuesta: "Macetas", en: "t" }] },
    });
    expect(a.ficha.papel).toBe("dueno");
    expect(a.contextoProyecto).toContain("Quiero vender macetas");
    expect(a.contextoProyecto).toContain("[core] P: ¿Que vendes? R: Macetas");
  });
});
