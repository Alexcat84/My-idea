// Ciclo de replanteamiento, Fase 2 (decisiones del fundador, 27 sep 2026):
// cada ciclo con SU línea en la bitácora ("Profundizaste tu plan" /
// "Replanteaste tu camino"), numerado por tipo, con lo que la persona escribió
// o dictó citado en su voz; y la tarea que un replanteamiento trae hecha no se
// narra dos veces. Lo esperado sale del catálogo (BITACORA), no se reteclea.
import { describe, expect, it } from "vitest";
import { construirBitacora, type DatosBitacora } from "./bitacoraCliente";
import { interpolar } from "./i18n/interpolar";
import { BITACORA } from "./i18n/mensajes/bitacora";

const t = BITACORA.es.historia;
const datos: DatosBitacora = {
  nombreIdea: "Pan",
  creadaAt: "2026-09-01T09:00:00Z",
  realizadaAt: null,
  sesiones: [],
  planes: [
    { id: "p0", etiqueta: "completo", created_at: "2026-09-02T10:00:00Z", dominio: "core", baseline_confirmada_at: null },
    { id: "p1", etiqueta: "seguimiento", created_at: "2026-09-08T10:00:00Z", dominio: "core", baseline_confirmada_at: null },
    { id: "p2", etiqueta: "replanteamiento", created_at: "2026-09-14T10:00:00Z", dominio: "core", baseline_confirmada_at: null },
    { id: "p3", etiqueta: "seguimiento", created_at: "2026-09-15T10:00:00Z", dominio: "core", baseline_confirmada_at: null },
    { id: "m1", etiqueta: "replanteamiento", created_at: "2026-09-16T10:00:00Z", dominio: "quality", baseline_confirmada_at: null },
  ],
  items: [
    { id: "t1", texto: "Hablar con 5 panaderías", completed_at: "2026-09-05T15:00:00Z", dominio: "core" },
    { id: "t9", texto: "Hablar con 5 panaderías", completed_at: "2026-09-05T15:00:00Z", dominio: "core", heredado_de: "t1" },
  ],
  eventos: [
    { tipo: "ciclo_profundizado", payload: { dominio: "core", plan_id: "p1", relato: "Vendí 10 panes." }, created_at: "2026-09-08T10:00:01Z" },
    { tipo: "ciclo_replanteado", payload: { dominio: "core", plan_id: "p2", relato: "Se cayó el local." }, created_at: "2026-09-14T10:00:01Z" },
    { tipo: "ciclo_replanteado", payload: { dominio: "quality", plan_id: "m1", relato: "Cambió la norma." }, created_at: "2026-09-16T10:00:01Z" },
  ],
  nombreMundo: (d) => (d === "quality" ? "Calidad" : d),
  generadoAt: "2026-09-20T00:00:00Z",
};

describe("la bitácora de los dos ciclos", () => {
  const entradas = construirBitacora(datos, "es");
  const de = (fecha: string) => entradas.find((e) => e.fecha === fecha);

  it("cada ciclo con su nombre, numerado por tipo, y con lo que la persona contó", () => {
    expect(de("2026-09-08T10:00:00Z")).toMatchObject({
      texto: `${t.profundizaste} ${interpolar(t.contaste, { relato: "Vendí 10 panes." })}`,
      titulo: interpolar(t.profundizasteTitulo, { n: 1 }),
      peso: "hito",
    });
    expect(de("2026-09-14T10:00:00Z")).toMatchObject({
      texto: `${t.replanteaste} ${interpolar(t.contaste, { relato: "Se cayó el local." })}`,
      titulo: interpolar(t.replanteasteTitulo, { n: 1 }),
    });
    // Segunda profundización, sin relato registrado: solo su nombre, número 2.
    expect(de("2026-09-15T10:00:00Z")).toMatchObject({ texto: t.profundizaste, titulo: interpolar(t.profundizasteTitulo, { n: 2 }) });
  });

  it("un ciclo de mundo dice cuál fue, en su espacio, con su relato", () => {
    expect(de("2026-09-16T10:00:00Z")).toMatchObject({
      texto: `${interpolar(t.replanteasteMundo, { mundo: "Calidad" })} ${interpolar(t.contaste, { relato: "Cambió la norma." })}`,
      dominio: "quality",
    });
  });

  it("la tarea heredada no se narra dos veces", () => {
    const hechas = entradas.filter((e) => e.texto === interpolar(t.marcasteHechaCita, { texto: "Hablar con 5 panaderías" }));
    expect(hechas).toHaveLength(1);
  });

  it("los eventos ciclo_* no salen como líneas sueltas (van dentro de la de su plan)", () => {
    expect(entradas.filter((e) => e.fecha.endsWith(":01Z"))).toHaveLength(0);
  });
});
