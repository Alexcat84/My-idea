// Hotfix v2.2.2: trampa sistemica para la familia de bugs de contrato
// codigo<->DB (migraciones 004, 005, 012: sessions.tipo, plans.etiqueta y
// project_nodes.tipo reventaron 23514 en vivo porque el codigo emitia un
// valor que ninguna migracion le habia permitido aun a la base de datos).
// Este test parsea los CHECK ... IN (...) vigentes directamente de
// supabase/migrations/ (aplicando las alteraciones en orden numerico) y
// los compara contra los literales que dbContract.ts centraliza -- si el
// codigo alguna vez declara un valor nuevo sin que exista la migracion que
// lo permita, este test falla ANTES de que Supabase reviente en vivo.
import { readdirSync, readFileSync } from "node:fs";
import path from "node:path";
import { describe, expect, it } from "vitest";
import { PLANS_ETIQUETA, PROJECT_NODES_TIPO, SESSIONS_TIPO } from "./dbContract";

const MIGRATIONS_DIR = path.resolve(__dirname, "..", "..", "supabase", "migrations");

function extraerLiterales(listaSql: string): string[] {
  return [...listaSql.matchAll(/'([^']*)'/g)].map((m) => m[1]);
}

function numeroMigracion(nombreArchivo: string): number {
  const m = nombreArchivo.match(/^my_idea_(\d+)_/);
  if (!m) throw new Error(`archivo de migracion sin numero: ${nombreArchivo}`);
  return Number(m[1]);
}

/** Parsea supabase/migrations/*.sql en orden numerico y devuelve, para
 * cada "tabla.columna" con un CHECK ... IN (...) vigente, el conjunto de
 * literales que la base de datos acepta HOY (la ultima migracion que
 * toco esa columna gana -- igual que aplicar las migraciones en orden
 * real contra Supabase). */
function parsearContratoDesdeMigraciones(): Map<string, Set<string>> {
  const archivos = readdirSync(MIGRATIONS_DIR)
    .filter((f) => /^my_idea_\d+_.*\.sql$/.test(f))
    .sort((a, b) => numeroMigracion(a) - numeroMigracion(b));

  const contrato = new Map<string, Set<string>>();

  for (const archivo of archivos) {
    const sql = readFileSync(path.join(MIGRATIONS_DIR, archivo), "utf-8");

    // CREATE TABLE public.<tabla> ( ... <col> TEXT ... CHECK (<col> IN (...)) ... );
    for (const bloque of sql.matchAll(/CREATE TABLE public\.(\w+)\s*\(([\s\S]*?)\n\);/g)) {
      const [, tabla, cuerpo] = bloque;
      for (const check of cuerpo.matchAll(/(\w+)\s+TEXT[^,]*CHECK\s*\(\s*\1\s+IN\s*\(([^)]*)\)\)/g)) {
        const [, columna, lista] = check;
        contrato.set(`${tabla}.${columna}`, new Set(extraerLiterales(lista)));
      }
    }

    // ALTER TABLE public.<tabla> ADD CONSTRAINT ... CHECK (<col> IN (...));
    for (const alter of sql.matchAll(
      /ALTER TABLE public\.(\w+)\s+ADD CONSTRAINT\s+\w+\s+CHECK\s*\(\s*(\w+)\s+IN\s*\(([^)]*)\)\)/g
    )) {
      const [, tabla, columna, lista] = alter;
      contrato.set(`${tabla}.${columna}`, new Set(extraerLiterales(lista)));
    }
  }

  return contrato;
}

const contrato = parsearContratoDesdeMigraciones();

function assertSubconjuntoDelContrato(claveTabla: string, valoresCodigo: readonly string[]) {
  const permitidos = contrato.get(claveTabla);
  expect(permitidos, `no se encontro ningun CHECK vigente para ${claveTabla} en supabase/migrations/`).toBeDefined();
  const noPermitidos = valoresCodigo.filter((v) => !permitidos!.has(v));
  expect(
    noPermitidos,
    `${claveTabla}: el codigo puede emitir ${JSON.stringify(noPermitidos)} pero ninguna migracion se lo permite ` +
      `a la base de datos (CHECK vigente: ${JSON.stringify([...permitidos!].sort())}) -- agrega una migracion antes de usar este valor.`
  ).toEqual([]);
}

describe("contrato codigo<->DB: todo lo que el codigo emite, Supabase lo acepta (Hotfix v2.2.2)", () => {
  it("sessions.tipo", () => {
    assertSubconjuntoDelContrato("sessions.tipo", SESSIONS_TIPO);
  });

  it("plans.etiqueta", () => {
    assertSubconjuntoDelContrato("plans.etiqueta", PLANS_ETIQUETA);
  });

  it("project_nodes.tipo", () => {
    assertSubconjuntoDelContrato("project_nodes.tipo", PROJECT_NODES_TIPO);
  });

  it("parseo de sanidad: encontro los 3 CHECK esperados con al menos un literal cada uno", () => {
    for (const clave of ["sessions.tipo", "plans.etiqueta", "project_nodes.tipo"]) {
      const permitidos = contrato.get(clave);
      expect(permitidos).toBeDefined();
      expect(permitidos!.size).toBeGreaterThan(0);
    }
  });
});
