import { describe, expect, it } from "vitest";
import { bitacoraMarkdown, construirBitacora, type DatosBitacora } from "./bitacoraCliente";

const nombreMundo = (d: string) => (d === "quality" ? "Calidad Impecable" : d);

const datos = (extra: Partial<DatosBitacora> = {}): DatosBitacora => ({
  nombreIdea: "Kits de huerto urbano",
  creadaAt: "2026-01-01T09:00:00Z",
  realizadaAt: null,
  sesiones: [{ created_at: "2026-01-03T10:00:00Z", tipo: "inicial", dominio: "core" }],
  planes: [
    { etiqueta: "organizador", created_at: "2026-01-02T10:00:00Z", dominio: "core", baseline_confirmada_at: null },
    { etiqueta: "completo", created_at: "2026-01-05T10:00:00Z", dominio: "core", baseline_confirmada_at: "2026-01-06T10:00:00Z" },
    { etiqueta: "reporte_numeros", created_at: "2026-01-07T10:00:00Z", dominio: "core", baseline_confirmada_at: null },
    { etiqueta: "completo", created_at: "2026-01-18T10:00:00Z", dominio: "quality", baseline_confirmada_at: null },
  ],
  items: [
    { id: "a1", texto: "Publica el video de tu producto", completed_at: "2026-01-10T15:00:00Z" },
    { id: "a2", texto: "Habla con cinco personas", completed_at: null },
  ],
  eventos: [
    { tipo: "modo_camino", payload: { de: null, a: "fechas" }, created_at: "2026-01-06T11:00:00Z" },
    { tipo: "cobro_carrera", payload: { monto: 12 }, created_at: "2026-01-08T10:00:00Z" }, // INTERNO
    { tipo: "mundo_incompatible", payload: { mundo: "quality" }, created_at: "2026-01-09T10:00:00Z" }, // INTERNO
    { tipo: "item_estado", payload: { item: "a1", de: "pendiente", a: "empezado" }, created_at: "2026-01-08T12:00:00Z" },
    { tipo: "item_estado", payload: { item: "a1", de: "empezado", a: "en_proceso" }, created_at: "2026-01-09T12:00:00Z" },
    { tipo: "fecha_hecho_movida", payload: { item: "a1", de: "2026-01-10T00:00:00Z", a: "2026-01-11T00:00:00Z" }, created_at: "2026-01-11T12:00:00Z" },
    { tipo: "nota_escrita", payload: { item: "a2" }, created_at: "2026-01-11T13:00:00Z" },
    { tipo: "fecha_movida", payload: { item: "a2", delta_dias: 7, cascada: 3 }, created_at: "2026-01-12T10:00:00Z" },
    { tipo: "item_no_aplica", payload: { item: "a2", motivo: "mi negocio es 100% online" }, created_at: "2026-01-13T10:00:00Z" },
    { tipo: "preview_iniciado", payload: { mundo: "quality" }, created_at: "2026-01-15T10:00:00Z" },
    { tipo: "mundo_completado", payload: { mundo: "quality", accion: "completar", motivo: "quedó redondo" }, created_at: "2026-01-20T10:00:00Z" },
    { tipo: "realizada", payload: { accion: "realizar", motivo: "ya es un negocio real" }, created_at: "2026-01-25T10:00:00Z" },
  ],
  nombreMundo,
  generadoAt: "2026-02-01T10:00:00Z",
  ...extra,
});

describe("construirBitacora", () => {
  it("ordena TODO cronológicamente ascendente (verificado a mano)", () => {
    const e = construirBitacora(datos());
    const fechas = e.map((x) => x.fecha);
    const ordenado = [...fechas].sort((a, b) => a.localeCompare(b));
    expect(fechas).toEqual(ordenado);
    // Primera entrada = la chispa; última = realizada.
    expect(e[0].texto).toContain("Encendiste la chispa");
    expect(e[e.length - 1].texto).toContain("realizada");
  });

  it("lista BLANCA: los eventos internos jamás aparecen", () => {
    const texto = construirBitacora(datos()).map((x) => x.texto).join("\n");
    expect(texto).not.toMatch(/cobro|carrera|incompatible|monto/i);
  });

  it("narra la cascada con su N y su delta", () => {
    const e = construirBitacora(datos());
    const mov = e.find((x) => x.texto.startsWith("Moviste la fecha"))!;
    expect(mov.texto).toContain("Habla con cinco personas");
    expect(mov.texto).toContain("las 3 siguientes, 7 días después");
  });

  it("registra cada decisión: cambios de estado, ajuste de fecha hecha y notas", () => {
    const texto = construirBitacora(datos()).map((x) => x.texto).join("\n");
    expect(texto).toContain("Empezaste «Publica el video de tu producto».");
    expect(texto).toContain("Pusiste «Publica el video de tu producto» en proceso.");
    expect(texto).toContain("Ajustaste la fecha en que hiciste «Publica el video de tu producto».");
    expect(texto).toContain("Anotaste algo en «Habla con cinco personas».");
  });

  it("cita los motivos del usuario entre comillas", () => {
    const texto = construirBitacora(datos()).map((x) => x.texto).join("\n");
    expect(texto).toContain("«mi negocio es 100% online»");
    expect(texto).toContain("«quedó redondo»");
    expect(texto).toContain("«ya es un negocio real»");
  });

  it("usa el nombre de CARA del mundo, nunca la clave técnica", () => {
    const texto = construirBitacora(datos()).map((x) => x.texto).join("\n");
    expect(texto).toContain("Calidad Impecable");
    expect(texto).not.toContain("quality");
  });

  it("deriva la realización de un proyecto viejo sin evento en bitácora", () => {
    const e = construirBitacora(datos({ realizadaAt: "2026-01-30T10:00:00Z", eventos: [] }));
    expect(e.some((x) => x.texto === "Marcaste tu idea como realizada.")).toBe(true);
  });

  it("no duplica la realización cuando ya hay evento en bitácora", () => {
    const reals = construirBitacora(datos({ realizadaAt: "2026-01-25T10:00:00Z" })).filter((x) => x.texto.includes("realizada"));
    expect(reals).toHaveLength(1);
  });
});

describe("bitacoraMarkdown", () => {
  it("abre con la historia de la idea y su rango de fechas", () => {
    const md = bitacoraMarkdown("Kits de huerto urbano", construirBitacora(datos()), "2026-02-01T10:00:00Z");
    expect(md).toContain("# La historia de Kits de huerto urbano");
    expect(md).toMatch(/> Del .* al /);
  });

  it("sin guiones largos en el texto generado (copy visible)", () => {
    const md = bitacoraMarkdown("Idea", construirBitacora(datos()), "2026-02-01T10:00:00Z");
    expect(md).not.toMatch(/[—–]/);
  });

  it("vacía con gracia si aún no hay historia", () => {
    const md = bitacoraMarkdown("Idea", [], "2026-02-01T10:00:00Z");
    expect(md).toContain("Tu historia apenas empieza");
  });
});
