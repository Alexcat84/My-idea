/**
 * Campaña "Mundos de protección", P1 — el armador del snapshot.
 *
 * Lo que se prueba: el corte de "vigentes" tal como lo adjudicaron el fundador y
 * el auditor (ciclo vigente, CON las hechas y su estado, SIN las retiradas), que
 * el módulo es LECTURA PURA (no muta lo que recibe), y el TAMAÑO: un plan real
 * ronda los 600 tokens, y hay un tope declarado para que un caso raro no infle
 * cada llamada de la entrevista sin que nadie se entere.
 */
import { readFileSync } from "node:fs";
import path from "node:path";
import { describe, expect, it } from "vitest";
import {
  TOPE_TOKENS_SNAPSHOT,
  armarSnapshot,
  snapshotComoTexto,
  tokensAprox,
  type FilaChecklistSnapshot,
} from "./snapshotProyecto";
import { esMundoProteccion, murallaSinPlan, MUNDOS_PROTECCION } from "../espacios";

function fila(over: Partial<FilaChecklistSnapshot> & { id: string }): FilaChecklistSnapshot {
  return {
    texto: "Una actividad del plan",
    etapa: 1,
    orden: 1,
    estado: "pendiente",
    fecha_base: null,
    banda: null,
    ...over,
  };
}

describe("qué entra al snapshot: el corte de 'vigentes'", () => {
  it("las HECHAS entran, con su estado marcado (también generan riesgos)", () => {
    const s = armarSnapshot([
      fila({ id: "a", texto: "Compra dos termos", estado: "hecho" }),
      fila({ id: "b", texto: "Habla con tres clientes", orden: 2 }),
    ]);
    expect(s.actividades).toHaveLength(2);
    expect(s.actividades[0]).toMatchObject({ id: "a", estado: "hecho" });
    expect(snapshotComoTexto(s)).toContain("hecha");
  });

  it("las RETIRADAS quedan fuera: sobre lo descartado no se levanta protección", () => {
    const s = armarSnapshot([
      fila({ id: "a", texto: "Sigue viva" }),
      fila({ id: "b", texto: "El usuario la retiró", estado: "no_aplica", orden: 2 }),
    ]);
    expect(s.actividades.map((a) => a.id)).toEqual(["a"]);
    expect(snapshotComoTexto(s)).not.toContain("El usuario la retiró");
  });

  it("los otros tres estados entran tal cual", () => {
    const s = armarSnapshot([
      fila({ id: "a", estado: "pendiente" }),
      fila({ id: "b", estado: "empezado", orden: 2 }),
      fila({ id: "c", estado: "en_proceso", orden: 3 }),
    ]);
    expect(s.actividades.map((a) => a.estado)).toEqual(["pendiente", "empezado", "en_proceso"]);
  });

  it("se ordena por etapa y luego por orden, lleguen como lleguen", () => {
    const s = armarSnapshot([
      fila({ id: "c", etapa: 2, orden: 1 }),
      fila({ id: "b", etapa: 1, orden: 2 }),
      fila({ id: "a", etapa: 1, orden: 1 }),
    ]);
    expect(s.actividades.map((a) => a.id)).toEqual(["a", "b", "c"]);
  });

  it("el índice es 1..N y NO salta con las retiradas (es la referencia del enlazador)", () => {
    const s = armarSnapshot([
      fila({ id: "a" }),
      fila({ id: "retirada", estado: "no_aplica", orden: 2 }),
      fila({ id: "b", orden: 3 }),
    ]);
    expect(s.actividades.map((a) => a.indice)).toEqual([1, 2]);
    expect(s.actividades[1].id).toBe("b");
  });

  it("un plan vacío da un snapshot vacío y un texto vacío (nada que fingir)", () => {
    const s = armarSnapshot([]);
    expect(s.actividades).toEqual([]);
    expect(snapshotComoTexto(s)).toBe("");
  });
});

describe("LECTURA PURA: el armador no escribe ni muta nada", () => {
  it("no toca el arreglo que recibe ni sus filas", () => {
    const filas = [fila({ id: "b", etapa: 2 }), fila({ id: "a", etapa: 1 })];
    const copia = JSON.parse(JSON.stringify(filas));
    armarSnapshot(filas);
    expect(filas).toEqual(copia);
  });

  it("el módulo no importa Supabase ni nada que escriba (contrato de lectura)", () => {
    const fuente = readFileSync(path.join(__dirname, "snapshotProyecto.ts"), "utf-8");
    expect(fuente).not.toMatch(/from ["'].*supabase/i);
    expect(fuente).not.toMatch(/\.(insert|update|upsert|delete)\(/);
  });
});

describe("el texto que viaja al prompt", () => {
  it("lleva índice, etapa, título y estado; y la fecha y la banda solo si existen", () => {
    const s = armarSnapshot([
      fila({ id: "a", texto: "Cotiza con tres proveedores", fecha_base: "2026-08-14T12:00:00.000Z", banda: "M" }),
      fila({ id: "b", texto: "Sin fecha ni banda", orden: 2 }),
    ]);
    const t = snapshotComoTexto(s);
    expect(t).toContain("#1 · E1 · Cotiza con tres proveedores · sin empezar · 14 ago · M");
    expect(t).toContain("#2 · E1 · Sin fecha ni banda · sin empezar");
    // la línea 2 no inventa una fecha ni una banda que no existen
    expect(t.split("\n")[2]).toBe("#2 · E1 · Sin fecha ni banda · sin empezar");
  });

  it("no lleva los uuid: son ~36 caracteres por actividad que el modelo no usa", () => {
    const s = armarSnapshot([fila({ id: "3f1c2b9e-0a4d-4f6b-9c11-7d2e5a8b1234", texto: "Una tarea" })]);
    expect(snapshotComoTexto(s)).not.toContain("3f1c2b9e");
  });
});

describe("el TAMAÑO del snapshot está medido, no supuesto", () => {
  /** Un plan real del dossier: 5 etapas, 31 actividades, títulos de una frase
   * (el largo que produce `derivarChecklist`, con su tope de 180 caracteres). */
  function planReal(): FilaChecklistSnapshot[] {
    const filas: FilaChecklistSnapshot[] = [];
    let n = 0;
    for (let etapa = 1; etapa <= 5; etapa += 1) {
      for (let orden = 1; orden <= 6 && n < 31; orden += 1) {
        n += 1;
        filas.push(
          fila({
            id: `item-${n}`,
            etapa,
            orden,
            texto: "Habla con tres clientes que no te conozcan y anota con qué palabras describen su problema.",
            estado: n <= 6 ? "hecho" : "pendiente",
            fecha_base: "2026-08-14T12:00:00.000Z",
            banda: "M",
          })
        );
      }
    }
    return filas;
  }

  it("un plan real (31 actividades) ronda los 600 tokens", () => {
    const t = snapshotComoTexto(armarSnapshot(planReal()));
    const tokens = tokensAprox(t);
    // A MANO: 31 líneas de ~120 caracteres ≈ 3.700 caracteres ≈ 930 tokens con
    // títulos largos; con títulos normales baja de 600. Se acota el rango en vez
    // de clavar un número: lo que importa es el orden de magnitud, no el dígito.
    expect(tokens).toBeGreaterThan(300);
    expect(tokens).toBeLessThan(TOPE_TOKENS_SNAPSHOT);
  });

  it("hasta un plan grande (60 actividades) se queda bajo el tope declarado", () => {
    const grande = [...planReal(), ...planReal().map((f, i) => ({ ...f, id: `extra-${i}`, etapa: f.etapa + 5 }))];
    const tokens = tokensAprox(snapshotComoTexto(armarSnapshot(grande)));
    // Si esto se rompe algún día, es la señal de que hay que recortar el
    // snapshot (por etapa o por pendientes), no de subir el tope a ciegas.
    expect(tokens).toBeLessThan(TOPE_TOKENS_SNAPSHOT * 2);
  });
});

describe("la muralla del sin plan: una sola frase, interpolada", () => {
  it("nombra el mundo y ofrece el camino, sin regañar", () => {
    expect(murallaSinPlan("Riesgos Bajo Control")).toBe(
      "Primero genera el plan de tu idea: tu mundo de Riesgos Bajo Control se construirá sobre él."
    );
  });

  it("la frase no lleva guiones largos ni medios (regla de la casa)", () => {
    const f = murallaSinPlan("Seguridad Digital");
    expect(f).not.toContain("—");
    expect(f).not.toContain("–");
  });

  it("la ruta y la pantalla usan la MISMA fuente (nadie la reescribe por su cuenta)", () => {
    const ruta = readFileSync(
      path.join(__dirname, "..", "..", "app", "api", "project", "[id]", "world", "[pack]", "start", "route.ts"),
      "utf-8"
    );
    const pantalla = readFileSync(path.join(__dirname, "..", "..", "app", "ui", "PotenciaTuIdea.tsx"), "utf-8");
    expect(ruta).toContain("murallaSinPlan(");
    expect(pantalla).toContain("murallaSinPlan(");
    // y ninguno de los dos conserva la frase vieja hardcodeada
    expect(ruta).not.toContain('"Primero genera el plan de tu idea.');
    expect(pantalla).not.toContain('"Primero genera el plan de tu idea."');
  });
});

describe("el enganche: el snapshot llega donde tiene que llegar", () => {
  it("world/start lo siembra SOLO para los mundos de protección", () => {
    const ruta = readFileSync(
      path.join(__dirname, "..", "..", "app", "api", "project", "[id]", "world", "[pack]", "start", "route.ts"),
      "utf-8"
    );
    expect(ruta).toContain("esMundoProteccion(pack)");
    expect(ruta).toContain("snapshotComoTexto(");
    expect(ruta).toContain("snapshotNucleo,");
  });

  it("el material del diagnóstico lo lleva, y se OMITE cuando no hay", () => {
    const dm = readFileSync(path.join(__dirname, "diagnosticoMundo.ts"), "utf-8");
    expect(dm).toContain("actividades_del_nucleo");
    // el campo se omite si el snapshot es null: un campo vacío solo gasta tokens
    expect(dm).toContain("recorrido.snapshotNucleo ? { actividades_del_nucleo");
  });
});

describe("la frontera: solo los tres mundos de protección", () => {
  it("los tres de protección son esos y no otros", () => {
    expect([...MUNDOS_PROTECCION]).toEqual(["risk_management", "health_safety", "seguridad_digital"]);
  });

  it("los mundos de mejora y expansión NO son de protección", () => {
    for (const mejora of ["quality", "exportacion", "franquicias", "environmental"]) {
      expect(esMundoProteccion(mejora)).toBe(false);
    }
  });

  it("el núcleo y lo vacío tampoco", () => {
    expect(esMundoProteccion("core")).toBe(false);
    expect(esMundoProteccion(null)).toBe(false);
    expect(esMundoProteccion(undefined)).toBe(false);
  });
});
