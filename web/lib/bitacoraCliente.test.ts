import { describe, expect, it } from "vitest";
import { bitacoraDeEspacio, bitacoraMarkdown, construirBitacora, type DatosBitacora } from "./bitacoraCliente";

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
    { id: "a1", texto: "Publica el video de tu producto", completed_at: "2026-01-10T15:00:00Z", dominio: "core" },
    { id: "a2", texto: "Habla con cinco personas", completed_at: null, dominio: "core" },
    { id: "m1", texto: "Define tu estándar de calidad", completed_at: "2026-01-19T15:00:00Z", dominio: "quality" },
  ],
  eventos: [
    { tipo: "modo_camino", payload: { de: null, a: "fechas" }, created_at: "2026-01-06T11:00:00Z" },
    { tipo: "item_estado", payload: { item: "m1", de: "pendiente", a: "empezado" }, created_at: "2026-01-16T12:00:00Z" },
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

  it("etiqueta las actividades de un MUNDO con su mundo (mapa de lecciones); las del core no", () => {
    const texto = construirBitacora(datos()).map((x) => x.texto).join("\n");
    // hecha y cambio de estado de un ítem de mundo llevan su mundo…
    expect(texto).toContain("Marcaste hecha «Define tu estándar de calidad» · en Calidad Impecable.");
    expect(texto).toContain("Empezaste «Define tu estándar de calidad» · en Calidad Impecable.");
    // …y las del viaje principal NO llevan sufijo de mundo.
    expect(texto).toContain("Marcaste hecha «Publica el video de tu producto».");
    expect(texto).toContain("Empezaste «Publica el video de tu producto».");
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

describe("bitacoraDeEspacio (Fase 3): partición exacta, sin inventar pertenencia", () => {
  it("cada entrada derivable cae en EXACTAMENTE un espacio (unión = global, sin solapes)", () => {
    const e = construirBitacora(datos());
    const core = bitacoraDeEspacio(e, "core");
    const quality = bitacoraDeEspacio(e, "quality");
    const noDerivables = e.filter((x) => x.dominio === null);
    // el dataset base no tiene ítems borrados → nada no-derivable
    expect(noDerivables).toHaveLength(0);
    // fórmula: unión de específicas = global − {no-derivables}
    expect(core.length + quality.length).toBe(e.length - noDerivables.length);
    // sin solapes: cada slice solo trae su espacio
    expect(core.every((x) => x.dominio === "core")).toBe(true);
    expect(quality.every((x) => x.dominio === "quality")).toBe(true);
    // lo del mundo NO aparece en el core (y viceversa)
    expect(core.some((x) => x.texto.includes("Calidad Impecable"))).toBe(false);
    expect(quality.some((x) => x.titulo === "La Chispa")).toBe(false);
    // el core conserva la chispa y la realización; el mundo, su diagnóstico/plan
    expect(core.some((x) => x.titulo === "La Chispa")).toBe(true);
    expect(core.some((x) => x.texto.includes("realizada"))).toBe(true);
    expect(quality.some((x) => x.texto.includes("Calidad Impecable"))).toBe(true);
  });

  it("borde no-derivable: evento de ítem borrado y sin estampa → dominio null, SOLO en la global", () => {
    const e = construirBitacora(
      datos({
        eventos: [{ tipo: "item_estado", payload: { item: "borrado-x", de: "pendiente", a: "empezado" }, created_at: "2026-01-14T10:00:00Z" }],
      }),
    );
    const fantasma = e.find((x) => x.texto === "Empezaste «una actividad».")!;
    expect(fantasma).toBeDefined();
    expect(fantasma.dominio).toBeNull();
    // etiqueta neutra: sin mundo inventado
    expect(fantasma.texto).not.toContain(" · en ");
    // presente en la global, AUSENTE de todas las específicas
    expect(e).toContain(fantasma);
    expect(bitacoraDeEspacio(e, "core")).not.toContain(fantasma);
    expect(bitacoraDeEspacio(e, "quality")).not.toContain(fantasma);
    // la fórmula se sostiene con la no-derivable listada explícita
    const noDerivables = e.filter((x) => x.dominio === null);
    expect(noDerivables).toContain(fantasma);
    expect(bitacoraDeEspacio(e, "core").length + bitacoraDeEspacio(e, "quality").length).toBe(e.length - noDerivables.length);
  });

  it("estampa: un evento con payload.dominio se atribuye por la estampa aunque el ítem ya no exista (borde solo arqueológico)", () => {
    const e = construirBitacora(
      datos({
        eventos: [{ tipo: "nota_escrita", payload: { item: "borrado-y", dominio: "quality" }, created_at: "2026-01-14T10:00:00Z" }],
      }),
    );
    const nota = e.find((x) => x.texto.startsWith("Anotaste"))!;
    expect(nota.dominio).toBe("quality");
    expect(bitacoraDeEspacio(e, "quality")).toContain(nota);
    expect(e.filter((x) => x.dominio === null)).toHaveLength(0);
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
