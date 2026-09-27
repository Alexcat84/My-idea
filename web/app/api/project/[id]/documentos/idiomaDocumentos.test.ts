// i18n F6 (D2): los documentos que se descargan siguen el IDIOMA DEL PROYECTO;
// el panel que los lista y los rechazos, el de la interfaz.
//
// El idioma de un documento es el de la idea si es de los once; si no, el de
// la interfaz (idiomaDePlantilla de F5). Una idea de antes de F5 (sin idioma)
// es español. Lo esperado sale del glosario y de los catálogos de cada idioma
// (DISENO §6): "Tu Plan" = ko "나의 계획" = en "Your Plan"; la fecha coreana es
// "{{ano}}년 {{mes}} {{d}}일" con "3월" → "2026년 3월 8일"; el rótulo neutro
// "## Etapa 1:" se pinta "## 1단계:", "**Pasos:**" → "**진행 순서:**",
// "**Entregable:**" → "**결과물:**" (catálogos MOTOR_PLAN y PLAN_DOCUMENTO).
import { beforeEach, describe, expect, it, vi } from "vitest";

type Fila = Record<string, unknown>;
let tablas: Record<string, Fila[]> = {};

function consulta(nombre: string) {
  const filtros: Array<(f: Fila) => boolean> = [];
  const q = {
    select: () => q,
    eq: (c: string, v: unknown) => (filtros.push((f) => f[c] === v), q),
    in: (c: string, vs: unknown[]) => (filtros.push((f) => vs.includes(f[c])), q),
    order: () => q,
    limit: () => q,
    then: (res: (v: unknown) => unknown, rej: (e: unknown) => unknown) =>
      Promise.resolve({ data: (tablas[nombre] ?? []).filter((f) => filtros.every((p) => p(f))), error: null }).then(res, rej),
  };
  return q;
}
const supabaseFalso = {
  auth: { getUser: vi.fn(async () => ({ data: { user: { id: "u1" } } })) },
  from: (nombre: string) => consulta(nombre),
};
vi.mock("@/lib/supabase/server", () => ({ createClient: vi.fn(async () => supabaseFalso) }));

// Las llamadas se leen en mock.calls (el 5.º argumento es el idioma).
const cargarEntradasBitacora = vi.fn<(...args: unknown[]) => Promise<Fila[]>>(async () => [
  { fecha: new Date(2026, 2, 8, 12).toISOString(), texto: "첫 인터뷰", peso: "accion", dominio: "core" },
]);
vi.mock("@/lib/bitacoraDatos", () => ({ cargarEntradasBitacora: (...a: unknown[]) => cargarEntradasBitacora(...a) }));

import { GET } from "./route";

const PARAMS = { params: Promise.resolve({ id: "p1" }) };
const CREADO = new Date(2026, 2, 8, 12).toISOString();
const PLAN_NEUTRO = [
  "# Plan de pan",
  "",
  "## Etapa 1: 첫 고객 인터뷰",
  "",
  "**Pasos:**",
  "1. 다섯 명에게 전화하기",
  "",
  "**Entregable:** 인터뷰 메모",
].join("\n");

function sembrar(idioma: string | null, conMundo = false) {
  tablas = {
    projects: [{ id: "p1", titulo: "Pan de barrio", entrada_original: "idea", created_at: CREADO, idioma }],
    sessions: [{ id: "s1", project_id: "p1", created_at: CREADO, tipo: "entrevista", dominio: null }],
    plans: [
      { id: "pl1", session_id: "s1", etiqueta: "inicial", contenido_md: PLAN_NEUTRO, created_at: CREADO, dominio: null, baseline_confirmada_at: null },
      ...(conMundo
        ? [{ id: "pl2", session_id: "s1", etiqueta: "inicial", contenido_md: PLAN_NEUTRO, created_at: CREADO, dominio: "quality", baseline_confirmada_at: null }]
        : []),
    ],
  };
}

const pedir = (interfaz: string, doc?: string) =>
  GET(
    new Request(`http://x/api/project/p1/documentos${doc ? `?doc=${encodeURIComponent(doc)}` : ""}`, {
      headers: { cookie: `myidea_idioma=${interfaz}` },
    }),
    PARAMS
  );

describe("documentos en el idioma del proyecto (D2)", () => {
  beforeEach(() => cargarEntradasBitacora.mockClear());

  it("idea en coreano, interfaz en español: el plan descargado va entero en coreano", async () => {
    sembrar("ko");
    const res = await pedir("es", "ciclo:pl1");
    const d = await res.json();
    expect(d.idioma).toBe("ko");
    expect(d.titulo).toBe("나의 계획");
    expect(d.archivo).toBe("pan-de-barrio-나의-계획");
    const lineas = (d.markdown as string).split("\n");
    expect(lineas[0]).toBe("> Pan de barrio · 나의 계획 · 2026년 3월 8일");
    expect(lineas).toContain("## 1단계: 첫 고객 인터뷰");
    expect(lineas).toContain("**진행 순서:**");
    expect(lineas).toContain("**결과물:** 인터뷰 메모");
    expect(d.markdown).not.toMatch(/Etapa|Pasos|Entregable/);
  });

  it("el panel que lista los documentos sigue la interfaz", async () => {
    sembrar("ko", true);
    const d = await (await pedir("en")).json();
    expect(d.documentos[0].titulo).toBe("Your Plan");
    // El espacio del reporte de un mundo lleva su nombre de cara en la
    // interfaz (glosario: quality = "Quality & Trust"), el mismo con que la
    // pantalla parte el panel en dos recuadros.
    const reporte = d.documentos.find((x: { tipo: string }) => x.tipo === "reporte");
    expect(reporte.espacio).toBe("Quality & Trust");
    expect(reporte.titulo).toContain("Quality & Trust");
  });

  it("idea en ruso (fuera de los once), interfaz en inglés: el documento va en inglés", async () => {
    sembrar("ru");
    const d = await (await pedir("en", "ciclo:pl1")).json();
    expect(d.idioma).toBe("en");
    expect(d.titulo).toBe("Your Plan");
    expect(d.markdown.split("\n")).toContain("## Stage 1: 첫 고객 인터뷰");
  });

  it("idea de antes de F5 (sin idioma), interfaz en francés: el documento sigue en español, idéntico", async () => {
    sembrar(null);
    const d = await (await pedir("fr", "ciclo:pl1")).json();
    expect(d.idioma).toBe("es");
    expect(d.titulo).toBe("Tu Plan");
    expect(d.markdown).toBe(`> Pan de barrio · Tu Plan · 8 de marzo de 2026\n\n${PLAN_NEUTRO}\n`);
  });

  it("la bitácora se arma en el idioma del proyecto", async () => {
    sembrar("ko");
    const d = await (await pedir("es", "bitacora")).json();
    expect(cargarEntradasBitacora).toHaveBeenCalled();
    expect(cargarEntradasBitacora.mock.calls[0][4]).toBe("ko");
    expect(d.idioma).toBe("ko");
    expect(d.titulo).toBe("나의 기록장");
    expect(d.archivo).toBe("pan-de-barrio-나의-기록장");
  });

  it("un documento que no existe se rechaza en el idioma de la interfaz", async () => {
    sembrar("ko");
    const res = await pedir("en", "ciclo:nada");
    expect(res.status).toBe(404);
    const { DOCUMENTOS_RUTA } = await import("@/lib/i18n/mensajes/documentosRuta");
    expect((await res.json()).error).toBe(DOCUMENTOS_RUTA.en.noEncontrado);
  });
});
