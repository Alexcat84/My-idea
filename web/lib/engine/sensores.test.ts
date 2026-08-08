import { readFileSync } from "node:fs";
import path from "node:path";
import { describe, expect, it } from "vitest";
import { nodosPorEtapaValidados } from "./planRedactor";

const RAIZ = path.resolve(__dirname, "..", "..");
const leer = (rel: string) => readFileSync(path.join(RAIZ, rel), "utf-8");
const MIGRACION = readFileSync(
  path.resolve(RAIZ, "..", "supabase", "migrations", "my_idea_037_sensores_del_panel.sql"),
  "utf-8"
);

/**
 * LOS DOS SENSORES DEL PANEL (migración 037).
 *
 * La telemetría solo acumula desde que el sensor existe: un sensor que nace
 * después del primer tester no puede contar lo que ese tester hizo. Por eso
 * están, y por eso su contrato se custodia.
 */
describe("b1 — el ítem del checklist y su nodo de origen", () => {
  const RUTA = ["nodo_a", "nodo_b"];
  const COSECHA = ["nodo_c"];

  it("guarda los nodos que el redactor autodeclaró, por etapa", () => {
    const r = nodosPorEtapaValidados({ etapas: { "1": ["nodo_a"], "2": ["nodo_b", "nodo_c"] } },
      RUTA, COSECHA);
    expect(r).toEqual({ "1": ["nodo_a"], "2": ["nodo_b", "nodo_c"] });
  });

  it("sin autodeclaración devuelve null, JAMÁS un objeto vacío", () => {
    // El ausente tiene que distinguirse del vacío: null es "no autodeclaró" y
    // {} sería "autodeclaró nada". Con {} un plan viejo mentiría diciendo que
    // no tuvo origen, y esa mentira sería indistinguible de un plan nuevo cuyo
    // redactor omitió la autodeclaración, que es algo que ya pasa hoy.
    expect(nodosPorEtapaValidados(null, RUTA, COSECHA)).toBeNull();
    expect(nodosPorEtapaValidados({}, RUTA, COSECHA)).toBeNull();
    expect(nodosPorEtapaValidados({ etapas: {} }, RUTA, COSECHA)).toBeNull();
  });

  it("un id ALUCINADO no se persiste", () => {
    // La regla dura del sensor: puede quedarse corto, pero no puede guardar
    // procedencia falsa. Un id que nunca vino en la ruta ni en la cosecha es
    // una alucinación, y verificarProcedenciaEtapas ya la registra; aquí
    // ademas se cae del dato que se guarda.
    const r = nodosPorEtapaValidados(
      { etapas: { "1": ["nodo_a", "nodo_inventado"], "2": ["solo_inventado"] } }, RUTA, COSECHA);
    expect(r).toEqual({ "1": ["nodo_a"] });
    expect(JSON.stringify(r)).not.toContain("inventado");
  });

  it("la columna es nullable y SIN default en la migración", () => {
    expect(MIGRACION).toMatch(/ADD COLUMN nodos_origen text\[\]\s*;/);
    const linea = MIGRACION.split("\n").find((l) => l.includes("ADD COLUMN nodos_origen"))!;
    expect(linea.toUpperCase(), "un DEFAULT haría mentir a los planes viejos")
      .not.toContain("DEFAULT");
    expect(linea.toUpperCase()).not.toContain("NOT NULL");
  });
});

describe("b2 — el diario de visitas", () => {
  it("una visita es una fila: el diario NO filtra por nuevos", () => {
    // Si filtrara, no sería un diario: sería una copia del estado, y la
    // pregunta que existe para contestar (cuántas veces se vuelve a un nodo)
    // se quedaría sin respuesta.
    const db = leer("lib/db.ts");
    const bloque = db.slice(db.indexOf("const { error: errorDiario }"),
                            db.indexOf("const yaCubiertos"));
    expect(bloque).toContain("nodosConTipo.map");
    expect(bloque, "el diario está filtrando por nuevos").not.toContain("nuevos.map");
  });

  it("escribe junto al camino existente, y su fallo NO tumba el recorrido", () => {
    // Un sensor que rompe lo que mide deja de ser un sensor.
    const db = leer("lib/db.ts");
    const bloque = db.slice(db.indexOf("const { error: errorDiario }"),
                            db.indexOf("const yaCubiertos"));
    expect(bloque).toContain("console.warn");
    expect(bloque, "el diario lanza y tumbaría el insert de project_nodes")
      .not.toMatch(/throw\s/);
    // y sigue existiendo el insert de project_nodes, el ESTADO
    expect(db).toContain('from("project_nodes").insert');
  });

  it("project_nodes conserva su UNIQUE: el diario no lo reemplaza", () => {
    expect(MIGRACION).not.toMatch(/project_nodes[\s\S]{0,80}DROP CONSTRAINT/i);
    expect(MIGRACION).toContain("CREATE TABLE public.node_visits");
    // sin UNIQUE en el diario: cada visita es una fila y ese es el punto
    const tabla = MIGRACION.slice(MIGRACION.indexOf("CREATE TABLE public.node_visits"),
                                  MIGRACION.indexOf(");", MIGRACION.indexOf("CREATE TABLE public.node_visits")));
    expect(tabla.toUpperCase()).not.toContain("UNIQUE");
  });

  it("el diario tiene RLS y sus índices", () => {
    expect(MIGRACION).toContain("ALTER TABLE public.node_visits ENABLE ROW LEVEL SECURITY");
    expect(MIGRACION).toContain("CREATE POLICY node_visits_own");
    expect(MIGRACION).toContain("node_visits_node_idx");
    expect(MIGRACION).toContain("node_visits_project_idx");
  });
});
