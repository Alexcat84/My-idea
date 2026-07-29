"use client";

/**
 * BitacoraPapel — la bitácora ("La secuencia de tu viaje") impresa, calibrada
 * por Claude Design. Antes se imprimía como markdown vía DocumentoPapel, y los
 * encabezados de día CORTABAN la espina del timeline (bug). Aquí se dibuja como
 * un timeline ESTRUCTURADO con espina CONTINUA que atraviesa el centro de cada
 * punto y termina exactamente en el último (nunca lo sobrepasa), en tokens de
 * papel. El pie va en un <tfoot> (se repite por página y no tapa el texto).
 *
 * Misma verdad que el .md: sale de las mismas `entradas`. El .md descargable
 * sigue siendo texto (bitacoraMarkdown); esto es solo su vestido en papel.
 */
import { fechaHumanaConAno, fechaInputLocal } from "@/lib/fechas";
import type { EntradaBitacora } from "@/lib/bitacoraCliente";

const AZUL = "#3B6BE8";
const AZUL_CLARO = "#7FA0DE";
const VERDE = "#1F8A34";
const RETIRADO = "#9A9DA4";
const TINTA = "#16171A";
const TERCIARIA = "#6B6E75";

function hora(iso: string): string {
  const d = new Date(iso);
  return `${String(d.getHours()).padStart(2, "0")}:${String(d.getMinutes()).padStart(2, "0")}`;
}

type Fila =
  | { tipo: "dia"; fecha: string; cierre: boolean }
  | { tipo: "entrada"; entrada: EntradaBitacora; conHora: boolean };

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
  for (const e of entradas) {
    const dia = fechaInputLocal(new Date(e.fecha));
    if (dia !== diaAnterior) {
      filas.push({ tipo: "dia", fecha: e.fecha, cierre: cierreEnDia.has(dia) });
      diaAnterior = dia;
    }
    filas.push({ tipo: "entrada", entrada: e, conHora: (conteo.get(dia) ?? 1) >= 2 });
  }
  return filas;
}

/** Colorea la cita del motivo (": «…»") en el color dado. */
function conMotivo(texto: string, color: string) {
  const m = texto.match(/^([\s\S]*?): («[\s\S]*»)$/);
  if (!m) return texto;
  return (
    <>
      {m[1]}: <span style={{ color }}>{m[2]}</span>
    </>
  );
}

export function BitacoraPapel({
  entradas,
  nombreIdea,
  oculto,
}: {
  entradas: EntradaBitacora[];
  nombreIdea: string;
  oculto?: boolean;
}) {
  const filas = aFilas(entradas);
  const cerrada = entradas.some((e) => e.peso === "cierre");
  const rango =
    entradas.length > 0
      ? `Del ${fechaHumanaConAno(entradas[0].fecha)} al ${fechaHumanaConAno(entradas[entradas.length - 1].fecha)}, día por día, tal como quedó registrado. Si moviste una fecha, la original sigue aquí: nada se reescribe.`
      : "";

  return (
    <div
      data-plan-print
      {...(oculto ? { "data-solo-impresion": "" } : {})}
      style={oculto ? { display: "none" } : undefined}
    >
      <table data-print-tabla className="w-full border-collapse">
        <tfoot data-print-pie className="hidden">
          <tr>
            <td className="p-0">
              <div className="pie-fila">
                <span>{nombreIdea} · Mi bitácora</span>
                <span>My Idea</span>
              </div>
            </td>
          </tr>
        </tfoot>
        <tbody>
          <tr>
            <td className="p-0 align-top">
              <div data-cuerpo-papel>
                <p style={{ margin: 0, fontSize: 11, fontWeight: 700, letterSpacing: "1.6px", textTransform: "uppercase", color: AZUL }}>
                  La secuencia de tu viaje
                </p>
                <h3 style={{ margin: "22px 0 0", fontFamily: "Georgia, 'Times New Roman', serif", fontSize: 27, fontWeight: 700, letterSpacing: "-0.3px", color: TINTA }}>
                  La secuencia de tu viaje
                </h3>
                {rango && <p style={{ margin: "12px 0 0", fontSize: 14.5, lineHeight: 1.7, color: "#4B4E55" }}>{rango}</p>}

                <div style={{ position: "relative", marginTop: 28 }}>
                  {filas.map((f, i) => {
                    const esPrimera = i === 0;
                    const esUltima = i === filas.length - 1;
                    const finDeDia = filas[i + 1]?.tipo === "dia";
                    // centro del punto desde el borde superior de la fila
                    const centro = f.tipo === "dia" ? 8 : 10;
                    const verde = cerrada && (f.tipo === "dia" ? f.cierre : f.entrada.peso === "cierre");
                    const tramo = (
                      <span
                        aria-hidden
                        style={{
                          position: "absolute",
                          left: 7,
                          width: 1,
                          transform: "translateX(-50%)",
                          background: verde ? VERDE : AZUL,
                          top: esPrimera ? centro : 0,
                          ...(esUltima ? { height: centro } : { bottom: 0 }),
                        }}
                      />
                    );
                    if (f.tipo === "dia") {
                      return (
                        <div key={`d-${i}`} style={{ position: "relative", paddingLeft: 30, paddingBottom: 7, breakInside: "avoid" }}>
                          {tramo}
                          <span style={{ position: "absolute", left: 7, top: 5, transform: "translateX(-50%)", width: 7, height: 7, borderRadius: "50%", background: f.cierre ? VERDE : AZUL }} />
                          <div style={{ fontSize: 15, fontWeight: 700, color: f.cierre ? VERDE : TINTA }}>{fechaHumanaConAno(f.fecha)}</div>
                        </div>
                      );
                    }
                    const e = f.entrada;
                    const esHito = e.peso === "hito" || e.peso === "cierre";
                    const color = e.peso === "retirada" ? RETIRADO : e.peso === "cierre" ? VERDE : TINTA;
                    const puntoColor = e.peso === "retirada" ? RETIRADO : e.peso === "cierre" ? VERDE : AZUL_CLARO;
                    return (
                      <div key={`e-${i}`} style={{ position: "relative", paddingLeft: 30, paddingBottom: finDeDia || esUltima ? 16 : 6 }}>
                        {tramo}
                        <span style={{ position: "absolute", left: 7, top: 7, transform: "translateX(-50%)", width: 6, height: 6, borderRadius: "50%", background: puntoColor }} />
                        <div style={{ fontSize: 13.5, lineHeight: 1.6, fontWeight: esHito ? 700 : 400, color }}>
                          {f.conHora && (
                            <span style={{ color: TERCIARIA, fontVariantNumeric: "tabular-nums", marginRight: 8 }}>{hora(e.fecha)}</span>
                          )}
                          {conMotivo(e.texto, e.peso === "cierre" ? VERDE : e.peso === "retirada" ? "#6B6E75" : color)}
                        </div>
                      </div>
                    );
                  })}
                </div>

                <p style={{ margin: "26px 0 0", fontSize: 12.5, lineHeight: 1.6, color: TERCIARIA }}>
                  Esta es tu historia tal como quedó registrada, día por día. Puedes descargarla aparte cuando quieras.
                </p>
              </div>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  );
}
