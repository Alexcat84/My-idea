// AUD-09 M17 (tanda 5, fallas silenciosas): el clasificador, el juez de sesión y
// el compresor del estado vivo caían a un respaldo sin evento ni log. La
// entrevista arrancaba genérica (primera puerta, perfil vacío) y nadie lo sabía.
import { readFileSync } from "node:fs";
import path from "node:path";
import { describe, expect, it, vi } from "vitest";
import type Anthropic from "@anthropic-ai/sdk";
import { usoVacio } from "../costmeter";
import { cargarGrafo } from "./graph";
import { clasificarEntrada } from "./clasificar";
import { evaluarCalidadSesion } from "./juezSesion";
import { comprimirEstadoVivo } from "./planRedactor";

const caido = { messages: { create: async () => { throw new Error("sin red"); } } } as unknown as Anthropic;
const graph = cargarGrafo();

describe("los respaldos dicen que lo son (AUD-09 M17)", () => {
  it("el clasificador caído marca su respaldo y deja rastro", async () => {
    const errores = vi.spyOn(console, "error").mockImplementation(() => {});
    const semilla = Object.keys(graph)[0];
    const r = await clasificarEntrada(caido, "quiero vender macetas", [semilla], graph, usoVacio());
    expect(r.puertaId).toBe(semilla);
    expect(r.fallback).toMatch(/clasificaci/);
    expect(errores).toHaveBeenCalled();
    errores.mockRestore();
  });

  it("el juez caído deja rastro", async () => {
    const errores = vi.spyOn(console, "error").mockImplementation(() => {});
    const turno = {
      tipo: "decision_turno",
      nodo_actual: null,
      decision: { camino: [], es_salto: false },
      candidatos_locales: [],
      saltos_posibles: [],
      razonamiento: "",
    } as never;
    const r = await evaluarCalidadSesion(caido, [turno], graph, usoVacio(), 1);
    expect(r.calidad).toBeNull();
    expect(errores).toHaveBeenCalled();
    errores.mockRestore();
  });

  it("el compresor caído deja rastro", async () => {
    const errores = vi.spyOn(console, "error").mockImplementation(() => {});
    await comprimirEstadoVivo(caido, "antes", "ahora", [], usoVacio());
    expect(errores).toHaveBeenCalled();
    errores.mockRestore();
  });

  it("el arranque de la entrevista registra el respaldo del clasificador como evento", () => {
    const ruta = readFileSync(path.join(__dirname, "..", "..", "app", "api", "session", "start", "route.ts"), "utf8");
    expect(ruta).toMatch(/clasificacion\.fallback/);
  });
});
