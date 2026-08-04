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
import { useEffect, useState } from "react";
import { etiquetaEspacio, proyectoTieneMundos, type EntradaBitacora } from "@/lib/bitacoraCliente";
import catalogo from "@/lib/assets/packs_catalog.json";
import { fechaHumanaConAno, fechaInputLocal } from "@/lib/fechas";

/** dominio (clave) → nombre de cara del mundo; "core" lo resuelve etiquetaEspacio. */
const NOMBRE_MUNDO: Record<string, string> = Object.fromEntries(
  (catalogo as { packs: Array<{ clave: string; nombre: string }> }).packs.map((p) => [p.clave, p.nombre]),
);
const nombreMundo = (d: string) => NOMBRE_MUNDO[d] ?? d;

const AZUL = "#4D7CFE";
const CELESTE = "#8FB3F5";
const VERDE = "#3FB950";
const PALABRA_NUM = ["", "un", "dos", "tres", "cuatro", "cinco", "seis", "siete", "ocho", "nueve", "diez"];

function hora(iso: string): string {
  const d = new Date(iso);
  return `${String(d.getHours()).padStart(2, "0")}:${String(d.getMinutes()).padStart(2, "0")}`;
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

/**
 * La LÍNEA DE TIEMPO en sí (sin encabezado ni descarga). Reutilizable: la usa la
 * página global "Mi bitácora" y la bitácora POR ESPACIO de la cara "Tu avance"
 * (Fase 3), que le pasa las entradas ya filtradas con `bitacoraDeEspacio`. La
 * espina dibuja su tramo por fila y termina justo en el centro del último punto.
 */
export function LineaBitacora({
  entradas,
  etiquetar,
}: {
  entradas: EntradaBitacora[];
  /** Fase 3 (tanda 4): la ETIQUETA DE ESPACIO por entrada (nombre de cara), solo
   * en la vista GLOBAL y con ruido cero. La vista por-espacio no la pasa. */
  etiquetar?: (e: EntradaBitacora) => string | null;
}) {
  const filas = aFilas(entradas);
  const cerrada = entradas.some((e) => e.peso === "cierre");
  return (
    <div className="relative mt-9 pb-1">
      {filas.map((f, i) => {
        const esPrimera = i === 0;
        const esUltima = i === filas.length - 1;
        // centro del punto de esta fila, desde el borde superior de la fila
        const centro = f.tipo === "dia" ? 12 : f.entrada.peso === "cierre" ? 13 : 11;
        const verde = cerrada && (f.tipo === "dia" ? f.cierre : f.entrada.peso === "cierre");
        const tramo = (
          <span
            aria-hidden
            style={{
              position: "absolute",
              left: 13,
              width: 2,
              transform: "translateX(-50%)",
              background: verde ? "rgba(63,185,80,0.9)" : "rgba(77,124,254,0.85)",
              top: esPrimera ? centro : 0,
              ...(esUltima ? { height: centro } : { bottom: 0 }),
            }}
          />
        );
        return f.tipo === "dia" ? (
          <div key={`d-${i}`} className="relative" style={{ paddingLeft: 44, paddingBottom: 10, paddingTop: esPrimera ? 2 : 8 }}>
            {tramo}
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
            style={{ paddingLeft: 44, paddingBottom: esUltima ? 0 : f.entrada.peso === "hito" ? 14 : 20 }}
          >
            {tramo}
            <PuntoEntrada peso={f.entrada.peso} />
            {(() => {
              const etq = etiquetar?.(f.entrada);
              return etq ? (
                <div className="mb-1">
                  <span className="inline-flex items-center rounded-full border border-hairline bg-surface-3 px-2 py-0.5 text-[10px] font-semibold uppercase tracking-[0.6px] text-dim">
                    {etq}
                  </span>
                </div>
              ) : null;
            })()}
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
        );
      })}
    </div>
  );
}

export function Bitacora({
  projectId,
  onVolver,
  dominio,
  nombreEspacio,
}: {
  projectId: string;
  onVolver: () => void;
  /** "Todo separado" (T4): scopeada a un mundo → su bitácora (filtro de servidor
   * de la Fase 3, ?dominio=X); sin dominio, la historia entera del proyecto. */
  dominio?: string;
  nombreEspacio?: string;
}) {
  const [datos, setDatos] = useState<{ nombre: string; entradas: EntradaBitacora[] } | null>(null);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    let vivo = true;
    // El filtro por espacio vive en el SERVIDOR (Fase 3): aquí solo se pide.
    const url = dominio
      ? `/api/project/${projectId}/bitacora?dominio=${dominio}`
      : `/api/project/${projectId}/bitacora`;
    fetch(url)
      .then((r) => (r.ok ? r.json() : Promise.reject(new Error(String(r.status)))))
      .then((d: { nombre: string; entradas: EntradaBitacora[] }) => vivo && setDatos(d))
      .catch(() => vivo && setError("No pudimos cargar tu bitácora. Vuelve a intentarlo en un momento."));
    return () => {
      vivo = false;
    };
  }, [projectId, dominio]);

  if (error) return <p className="text-sm text-warn">{error}</p>;
  if (!datos) return <p className="text-dim">Cargando tu bitácora…</p>;

  const { entradas } = datos;
  const rango =
    entradas.length > 0
      ? `del ${fechaHumanaConAno(entradas[0].fecha)} al ${fechaHumanaConAno(entradas[entradas.length - 1].fecha)}`
      : null;

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
              {dominio ? `Bitácora de ${nombreEspacio ?? "este mundo"}` : "Mi bitácora de mi viaje"}
            </h2>
            <p className="mt-3 text-[15px] text-dim">
              <span className="font-semibold text-ink">«{datos.nombre}»</span>
              {rango ? ` · ${rango}` : ""}
            </p>
            {/* Sin botones de descarga aquí: bajar la bitácora en .md o PDF vive
                en "Tus documentos" (centralizado). Esta página es la vista viva. */}
          </div>
        </div>

        {entradas.length === 0 ? (
          <p className="mt-8 text-[14px] leading-relaxed text-dim">
            Tu historia apenas empieza. Cada paso que des irá quedando aquí: cada estado que cambies, cada fecha que
            muevas, cada nota.
          </p>
        ) : (
          <>
            {/* La bitácora es un REGISTRO completo (todo, día por día), no un
                resumen: el resumen y el mapa de hitos viven en el Análisis del
                proyecto, que es donde tienen sentido. Aquí, solo la línea de
                tiempo. */}

            {/* ── Línea de tiempo completa (componente reutilizable) ─────── */}
            {/* Vista GLOBAL: etiqueta cada entrada con su espacio (nombre de
                cara), con RUIDO CERO — un proyecto solo-core no etiqueta nada. La
                vista POR ESPACIO (T4) ya es de un solo espacio: no etiqueta. */}
            <LineaBitacora
              entradas={entradas}
              etiquetar={dominio ? undefined : (e) => etiquetaEspacio(e.dominio, proyectoTieneMundos(entradas), nombreMundo)}
            />

            <p className="mt-9 border-t border-hairline pt-5 text-[12.5px] leading-relaxed text-dim">
              Esta es tu historia tal como quedó registrada, día por día. Nada se reescribe: si moviste una fecha, la
              original sigue aquí.
            </p>
          </>
        )}
      </div>

    </section>
  );
}
