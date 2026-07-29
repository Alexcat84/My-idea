"use client";

/**
 * Bitacora — Fase 4.8: la bitácora del cliente como PÁGINA en vivo, calibrada
 * por Claude Design ("Mi bitácora de mi viaje"). Un resumen y un mapa de hitos
 * arriba; debajo, la línea de tiempo completa día por día.
 *
 * La ESPINA atraviesa el centro de cada punto (nunca al lado, nunca la sobrepasa).
 * Cuatro pesos, sin iconos: día (13px azul), hito (9px celeste con halo),
 * acción diaria (7px celeste), retirada (7px gris). El cierre es el único verde.
 * La hora solo aparece en días con 2+ entradas. Cero motor: solo lee lo que pasó.
 *
 * El .md y el PDF salen del MISMO texto (bitacoraMarkdown), la misma verdad que
 * el documento del panel.
 */
import { useCallback, useEffect, useState } from "react";
import { bitacoraMarkdown, type EntradaBitacora } from "@/lib/bitacoraCliente";
import { fechaHumanaConAno, fechaInputLocal } from "@/lib/fechas";
import { DocumentoPapel } from "./DocumentoPapel";

const AZUL = "#4D7CFE";
const CELESTE = "#8FB3F5";
const VERDE = "#3FB950";
const MESES_CORTOS = ["ene", "feb", "mar", "abr", "may", "jun", "jul", "ago", "sep", "oct", "nov", "dic"];
const PALABRA_NUM = ["", "un", "dos", "tres", "cuatro", "cinco", "seis", "siete", "ocho", "nueve", "diez"];

function hora(iso: string): string {
  const d = new Date(iso);
  return `${String(d.getHours()).padStart(2, "0")}:${String(d.getMinutes()).padStart(2, "0")}`;
}
/** "1 jun" — día + mes abreviado, para el mapa de hitos. */
function fechaMapa(iso: string): string {
  const d = new Date(iso);
  return `${d.getDate()} ${MESES_CORTOS[d.getMonth()]}`;
}
function numeroPalabra(n: number): string {
  return n <= 10 ? PALABRA_NUM[n] : String(n);
}

type Fila =
  | { tipo: "dia"; fecha: string; sub: string | null; cierre: boolean }
  | { tipo: "entrada"; entrada: EntradaBitacora; conHora: boolean; ultima: boolean };

/** Aplana las entradas en filas con encabezado por día; la hora solo en los
 * días con 2+ entradas (regla del historial, igual que el documento). */
function aFilas(entradas: EntradaBitacora[]): Fila[] {
  const conteo = new Map<string, number>();
  const cierreEnDia = new Set<string>();
  for (const e of entradas) {
    const k = fechaInputLocal(new Date(e.fecha));
    conteo.set(k, (conteo.get(k) ?? 0) + 1);
    if (e.peso === "cierre") cierreEnDia.add(k);
  }
  const filas: Fila[] = [];
  let diaAnterior = "";
  entradas.forEach((e, i) => {
    const dia = fechaInputLocal(new Date(e.fecha));
    const n = conteo.get(dia) ?? 1;
    if (dia !== diaAnterior) {
      const sub = i === 0 ? "el día en que empezó todo" : n >= 3 ? `${numeroPalabra(n)} momentos este día` : null;
      filas.push({ tipo: "dia", fecha: e.fecha, sub, cierre: cierreEnDia.has(dia) });
      diaAnterior = dia;
    }
    filas.push({ tipo: "entrada", entrada: e, conHora: n >= 2, ultima: i === entradas.length - 1 });
  });
  return filas;
}

function descargarMd(markdown: string, archivo: string) {
  const blob = new Blob([markdown], { type: "text/markdown;charset=utf-8" });
  const url = URL.createObjectURL(blob);
  const a = document.createElement("a");
  a.href = url;
  a.download = `${archivo}.md`;
  a.click();
  URL.revokeObjectURL(url);
}

/** El punto de una fila de entrada, según su peso. */
function PuntoEntrada({ peso }: { peso: EntradaBitacora["peso"] }) {
  const base = { position: "absolute" as const, left: 13, transform: "translateX(-50%)", borderRadius: "50%" };
  if (peso === "cierre")
    return <span aria-hidden style={{ ...base, top: 8, width: 11, height: 11, background: VERDE, boxShadow: `0 0 0 3px rgba(63,185,80,0.2)` }} />;
  if (peso === "retirada")
    return <span aria-hidden style={{ ...base, top: 7, width: 7, height: 7, background: "#5A5B62" }} />;
  if (peso === "hito")
    return <span aria-hidden style={{ ...base, top: 7, width: 9, height: 9, background: CELESTE, boxShadow: `0 0 0 3px rgba(143,179,245,0.16)` }} />;
  return <span aria-hidden style={{ ...base, top: 7, width: 7, height: 7, background: CELESTE }} />;
}

/** El texto de una entrada, con su peso: hito pleno, acción tenue, retirada gris,
 * cierre en grande. Los motivos ya vienen entre «» del builder; aquí solo se
 * colorea el que sigue a la retirada/cierre. */
function TextoEntrada({ e }: { e: EntradaBitacora }) {
  if (e.peso === "cierre")
    return (
      <>
        <div style={{ fontSize: 17, fontWeight: 700, lineHeight: 1.45, color: "#F5F6F8" }}>{coloreaMotivo(e.texto, VERDE)}</div>
        <div style={{ fontSize: 13, color: "#6F7076", marginTop: 6 }}>Aquí acaba tu idea y nace tu proyecto.</div>
      </>
    );
  if (e.peso === "retirada")
    return <span style={{ fontSize: 14.5, lineHeight: 1.55, color: "#8A8B92" }}>{coloreaMotivo(e.texto, "#A6A7AD")}</span>;
  if (e.peso === "hito") return <span style={{ fontSize: 15, fontWeight: 600, lineHeight: 1.5, color: "#F5F6F8" }}>{e.texto}</span>;
  return <span style={{ fontSize: 14.5, lineHeight: 1.55, color: "#DDDEE3" }}>{e.texto}</span>;
}

/** Si el texto trae un motivo citado tras dos puntos (": «…»"), colorea la cita. */
function coloreaMotivo(texto: string, color: string) {
  const m = texto.match(/^([\s\S]*?): («[\s\S]*»)$/);
  if (!m) return texto;
  return (
    <>
      {m[1]}: <span style={{ color }}>{m[2]}</span>
    </>
  );
}

export function Bitacora({ projectId, onVolver }: { projectId: string; onVolver: () => void }) {
  const [datos, setDatos] = useState<{ nombre: string; entradas: EntradaBitacora[] } | null>(null);
  const [error, setError] = useState<string | null>(null);
  const [imprimir, setImprimir] = useState<string | null>(null);

  useEffect(() => {
    let vivo = true;
    fetch(`/api/project/${projectId}/bitacora`)
      .then((r) => (r.ok ? r.json() : Promise.reject(new Error(String(r.status)))))
      .then((d: { nombre: string; entradas: EntradaBitacora[] }) => vivo && setDatos(d))
      .catch(() => vivo && setError("No pudimos cargar tu bitácora. Vuelve a intentarlo en un momento."));
    return () => {
      vivo = false;
    };
  }, [projectId]);

  useEffect(() => {
    if (!imprimir) return;
    const limpiar = () => setImprimir(null);
    window.addEventListener("afterprint", limpiar);
    window.print();
    return () => window.removeEventListener("afterprint", limpiar);
  }, [imprimir]);

  const markdown = useCallback(
    () => (datos ? bitacoraMarkdown(datos.nombre, datos.entradas, new Date().toISOString()) : ""),
    [datos]
  );

  if (error) return <p className="text-sm text-warn">{error}</p>;
  if (!datos) return <p className="text-dim">Cargando tu bitácora…</p>;

  const { entradas } = datos;
  const filas = aFilas(entradas);
  const rango =
    entradas.length > 0
      ? `del ${fechaHumanaConAno(entradas[0].fecha)} al ${fechaHumanaConAno(entradas[entradas.length - 1].fecha)}`
      : null;

  // Resumen: cifras de lo persistido (el mismo criterio del análisis).
  const hitos = entradas.filter((e) => e.peso === "hito" || e.peso === "cierre");
  const cerrada = entradas.some((e) => e.peso === "cierre");
  const diasDeViaje =
    entradas.length > 0
      ? Math.max(
          1,
          Math.round((new Date(entradas[entradas.length - 1].fecha).getTime() - new Date(entradas[0].fecha).getTime()) / 86_400_000) + 1
        )
      : 0;
  const N = hitos.length;
  const inset = N > 1 ? 100 / (2 * N) : 50;
  const spineBottom = cerrada ? 40 : 16;

  return (
    <section className="mx-auto w-full max-w-[880px]">
      <button onClick={onVolver} className="mb-5 text-sm text-dim hover:text-ink" data-no-print>
        ← Volver
      </button>

      <div data-no-print>
        <div className="flex flex-wrap items-start justify-between gap-6">
          <div className="min-w-0">
            <p className="mb-3 flex items-center gap-2.5 text-[12px] font-semibold uppercase tracking-[1.5px]" style={{ color: AZUL }}>
              <span aria-hidden className="h-[7px] w-[7px] rounded-full" style={{ background: CELESTE }} />
              Tu historia
            </p>
            <h2 className="text-[28px] font-bold leading-[1.15] tracking-[-0.02em] [text-wrap:balance] sm:text-[34px]">
              Mi bitácora de mi viaje
            </h2>
            <p className="mt-3 text-[15px] text-dim">
              <span className="font-semibold text-ink">«{datos.nombre}»</span>
              {rango ? ` · ${rango}` : ""}
            </p>
          </div>
          <div className="flex flex-none gap-2.5 pt-1">
            <button
              onClick={() => descargarMd(markdown(), `bitacora-${datos.nombre.replace(/[^\p{L}\p{N}]+/gu, "-").slice(0, 40) || "mi-viaje"}`)}
              className="rounded-full border border-hairline px-4 py-2.5 text-[13.5px] font-semibold text-ink hover:border-accent/60"
            >
              Descargar .md
            </button>
            <button
              onClick={() => setImprimir(markdown())}
              className="rounded-full border border-accent/50 bg-accent/15 px-4 py-2.5 text-[13.5px] font-semibold text-accent hover:bg-accent/25"
            >
              Imprimir / PDF
            </button>
          </div>
        </div>

        {entradas.length === 0 ? (
          <p className="mt-8 text-[14px] leading-relaxed text-dim">
            Tu historia apenas empieza. Cada paso que des irá quedando aquí: cada estado que cambies, cada fecha que
            muevas, cada nota.
          </p>
        ) : (
          <>
            {/* ── Resumen + mapa de hitos ──────────────────────────────── */}
            <div className="mt-7 rounded-[16px] border border-hairline p-6 sm:p-7" style={{ background: "#0C0C10" }}>
              <div className="grid grid-cols-2 gap-3 sm:grid-cols-4 sm:gap-3.5">
                <Cifra valor={diasDeViaje} etiqueta="días de viaje" borde />
                <Cifra valor={entradas.length} etiqueta="momentos registrados" borde />
                <Cifra valor={N} etiqueta="hitos de tu camino" color={AZUL} borde />
                <Cifra valor={cerrada ? 1 : 0} etiqueta={cerrada ? "cierre: ya es proyecto" : "aún en marcha"} color={cerrada ? VERDE : undefined} />
              </div>

              {N > 0 && (
                <div className="mt-2 border-t border-hairline pt-6">
                  <div className="mb-5 text-[11.5px] font-semibold uppercase tracking-[1.3px] text-dim">Tus hitos, de un vistazo</div>
                  <div className="relative overflow-x-auto">
                    <div className="relative" style={{ minWidth: N > 6 ? N * 96 : undefined }}>
                      <div
                        aria-hidden
                        style={{
                          position: "absolute",
                          left: `${inset}%`,
                          right: `${inset}%`,
                          top: 8,
                          height: 2,
                          background: cerrada
                            ? `linear-gradient(to right, rgba(77,124,254,0.85) 0%, rgba(77,124,254,0.85) 82%, rgba(63,185,80,0.9) 100%)`
                            : `rgba(77,124,254,0.85)`,
                        }}
                      />
                      <div className="relative grid items-start" style={{ gridTemplateColumns: `repeat(${N}, 1fr)` }}>
                        {hitos.map((h, i) => {
                          const esCierre = h.peso === "cierre";
                          const viva = !cerrada && i === N - 1;
                          return (
                            <div key={i} className="flex flex-col items-center gap-0 px-1 text-center">
                              <div className="flex h-[18px] items-center justify-center">
                                <span
                                  className={viva ? "anima-idea-pulse" : undefined}
                                  style={{
                                    width: esCierre ? 13 : 11,
                                    height: esCierre ? 13 : 11,
                                    borderRadius: "50%",
                                    background: esCierre ? VERDE : AZUL,
                                    boxShadow: esCierre ? `0 0 0 4px rgba(63,185,80,0.18)` : undefined,
                                  }}
                                />
                              </div>
                              <div className="mt-2.5 text-[11.5px] tabular-nums text-dim">{fechaMapa(h.fecha)}</div>
                              <div className="mt-1 text-[12.5px] font-semibold leading-[1.35]" style={{ color: esCierre ? VERDE : "#F5F6F8" }}>
                                {h.titulo ?? h.texto}
                              </div>
                            </div>
                          );
                        })}
                      </div>
                    </div>
                  </div>
                  <div className="mt-4 text-[11.5px] text-dim">
                    Un paso por hito, en el orden en que ocurrieron. Las distancias reales entre fechas viven en la línea de abajo.
                  </div>
                </div>
              )}
            </div>

            {/* ── Línea de tiempo completa ─────────────────────────────── */}
            <div className="relative mt-9 pb-1">
              <div
                aria-hidden
                style={{
                  position: "absolute",
                  left: 13,
                  top: 12,
                  bottom: spineBottom,
                  width: 2,
                  transform: "translateX(-50%)",
                  background: cerrada
                    ? `linear-gradient(to bottom, rgba(77,124,254,0.85) 0%, rgba(77,124,254,0.85) 92%, rgba(63,185,80,0.9) 100%)`
                    : `rgba(77,124,254,0.85)`,
                }}
              />
              {filas.map((f, i) =>
                f.tipo === "dia" ? (
                  <div key={`d-${i}`} className="relative" style={{ paddingLeft: 44, paddingBottom: 10, paddingTop: i === 0 ? 2 : 8 }}>
                    <span
                      aria-hidden
                      style={{
                        position: "absolute",
                        left: 13,
                        top: 6,
                        transform: "translateX(-50%)",
                        width: 13,
                        height: 13,
                        borderRadius: "50%",
                        background: f.cierre ? VERDE : AZUL,
                        boxShadow: `0 0 0 4px ${f.cierre ? "rgba(63,185,80,0.16)" : "rgba(77,124,254,0.16)"}`,
                      }}
                    />
                    <div className="text-[15px] font-bold" style={{ color: f.cierre ? VERDE : "#F5F6F8" }}>
                      {fechaHumanaConAno(f.fecha)}
                    </div>
                    {f.sub && <div className="mt-[3px] text-[12px] text-dim">{f.sub}</div>}
                  </div>
                ) : (
                  <div
                    key={`e-${i}`}
                    className="relative"
                    style={{ paddingLeft: 44, paddingBottom: f.ultima ? 0 : f.entrada.peso === "hito" ? 14 : 20 }}
                  >
                    <PuntoEntrada peso={f.entrada.peso} />
                    {f.conHora ? (
                      <div className="flex items-baseline gap-3">
                        <span className="flex-none text-[12px] tabular-nums text-dim" style={{ minWidth: 38 }}>
                          {hora(f.entrada.fecha)}
                        </span>
                        <span className="[text-wrap:pretty]">
                          <TextoEntrada e={f.entrada} />
                        </span>
                      </div>
                    ) : (
                      <span className="[text-wrap:pretty]">
                        <TextoEntrada e={f.entrada} />
                      </span>
                    )}
                  </div>
                )
              )}
            </div>

            <p className="mt-9 border-t border-hairline pt-5 text-[12.5px] leading-relaxed text-dim">
              Esta es tu historia tal como quedó registrada, día por día. Nada se reescribe: si moviste una fecha, la
              original sigue aquí.
            </p>
          </>
        )}
      </div>

      {/* Invisible en pantalla; la hoja de impresión lo enciende en papel. */}
      {imprimir && <DocumentoPapel oculto markdown={imprimir} nombreIdea={datos.nombre} titulo="Mi bitácora" />}
    </section>
  );
}

function Cifra({ valor, etiqueta, color, borde }: { valor: number; etiqueta: string; color?: string; borde?: boolean }) {
  return (
    <div className={"px-2.5 py-3.5 text-center" + (borde ? " sm:border-r sm:border-hairline" : "")}>
      <div className="text-[30px] font-extrabold tracking-[-0.5px] tabular-nums" style={color ? { color } : undefined}>
        {valor}
      </div>
      <div className="mt-1.5 text-[12.5px] text-dim">{etiqueta}</div>
    </div>
  );
}
