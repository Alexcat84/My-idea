// AUD-09 M15 (decisión del fundador, 25 sep 2026): la protección apunta al
// NODO de la tarea, no al id de la tarea del ciclo. Hoy un ciclo nuevo del
// núcleo dejaba la protección huérfana sin aviso: las anclas de fecha, el chip
// del cajón y el registro buscaban el id viejo en el plan nuevo. Contrato de
// fuente: cada consumidor resuelve con resolverProtegido y los dos campos
// portadores viajan de la base a la pantalla.
import { readFileSync } from "node:fs";
import path from "node:path";
import { describe, expect, it } from "vitest";

const leer = (rel: string) => readFileSync(path.join(__dirname, "..", "..", rel), "utf8");
const manos = leer("app/ui/ManosALaObra.tsx");
const checklist = leer("app/api/project/[id]/checklist/route.ts");
const documentos = leer("app/api/project/[id]/documentos/route.ts");
const plan = leer("app/api/session/[id]/plan/route.ts");
const db = leer("lib/db.ts");

describe("la protección se resuelve por nodo en cada consumidor (AUD-09 M15)", () => {
  it("el checklist lee nodos_origen y protege_nodos, con degradación si falta la 041", () => {
    expect(checklist).toMatch(/const COLUMNAS =[^;]*nodos_origen, protege_nodos/);
    expect(checklist).toMatch(/COLUMNAS_NUEVAS = \[[^\]]*", nodos_origen, protege_nodos"/);
  });

  it("Manos a la Obra resuelve anclas y cajón con resolverProtegido, no por id crudo", () => {
    expect(manos).toMatch(/resolverProtegido\(/);
    expect(manos).not.toMatch(/corePorId\.get\(it\.protege_item\)/);
    expect(manos).not.toMatch(/i\.protege_item === vivo\.id/);
    expect(manos).not.toMatch(/todos\.find\(\(i\) => i\.id === vivo\.protege_item\)/);
  });

  it("el registro en pantalla y en papel recibe los ids del plan vigente", () => {
    expect(manos).toMatch(/armarRegistro\([\s\S]{0,200}?actividadesNucleo,\s*idsPlanNucleo\s*\)/);
    expect(documentos).toMatch(/protege_item, protege_nodos/);
    expect(documentos).toMatch(/armarRegistro\([^)]*actividades, idsDelPlan\)/);
  });

  it("las actividades del núcleo llevan sus nodos (lectura del plan vigente)", () => {
    expect(db).toMatch(/const columnas = "id, texto, etapa, orden, estado, fecha_base, banda, nodos_origen"/);
  });

  it("el enlace del plan de protección guarda los nodos de lo protegido", () => {
    expect(plan).toMatch(/protege_nodos: nodosDeLoProtegido\(/);
    expect(db).toMatch(/protege_nodos: i\.protege_nodos \?\? null/);
  });
});
