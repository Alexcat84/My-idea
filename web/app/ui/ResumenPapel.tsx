"use client";

/**
 * ResumenPapel — la página "Cómo te fue" / "Tu progreso hasta aquí" del
 * Expediente, calibrada por Claude Design (resumen_816). Render de papel
 * ESTRUCTURADO (no markdown): tres cifras grandes entre dos hilos, el mapa de
 * hitos del viaje, la caja de cierre (verde si ya cerró, gris si sigue) y dos
 * columnas de texto. Todo de datos deterministas de analytics; cero LLM.
 *
 * El verde solo se enciende con el cierre (ley de color). Pie en <tfoot> para
 * que no tape el texto. Se monta oculto y la hoja de impresión lo enciende.
 */
const AZUL = "#3B6BE8";
const VERDE = "#1F8A34";
const TINTA = "#16171A";
const SEC = "#4B4E55";
const TER = "#6B6E75";
const HILO = "#DFE1E6";
const MESES = ["ene", "feb", "mar", "abr", "may", "jun", "jul", "ago", "sep", "oct", "nov", "dic"];

function fechaMapa(iso: string): string {
  const d = new Date(iso);
  return `${d.getUTCDate()} ${MESES[d.getUTCMonth()]}`;
}

export interface HitoResumen {
  fecha: string;
  nombre: string;
}

export function ResumenPapel({
  nombreIdea,
  cerrada,
  cierreMotivo,
  intro,
  dias,
  accionesCumplidas,
  hitos,
  loQueMovio,
  loQuePendiente,
  oculto,
}: {
  nombreIdea: string;
  cerrada: boolean;
  cierreMotivo: string | null;
  intro: string;
  dias: number;
  accionesCumplidas: number;
  hitos: HitoResumen[];
  loQueMovio: string;
  loQuePendiente: string;
  oculto?: boolean;
}) {
  const titulo = cerrada ? "Cómo te fue" : "Tu progreso hasta aquí";
  const N = hitos.length;
  const inset = N > 1 ? 100 / (2 * N) : 50;

  const cifra = (valor: number, etiqueta: string, color?: string) => (
    <div style={{ flex: 1, padding: "22px 0" }}>
      <div style={{ fontSize: 40, fontWeight: 800, letterSpacing: "-1.4px", fontVariantNumeric: "tabular-nums", color: color ?? TINTA }}>{valor}</div>
      <div style={{ fontSize: 12.5, color: TER, marginTop: 4 }}>{etiqueta}</div>
    </div>
  );

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
                <span>{nombreIdea} · Expediente</span>
                <span>My Idea</span>
              </div>
            </td>
          </tr>
        </tfoot>
        <tbody>
          <tr>
            <td className="p-0 align-top">
              <div data-cuerpo-papel>
                <div style={{ display: "flex", alignItems: "baseline", justifyContent: "space-between", gap: 20, paddingBottom: 14, borderBottom: `1px solid ${HILO}` }}>
                  <span style={{ fontSize: 11, fontWeight: 700, letterSpacing: "1.6px", textTransform: "uppercase", color: AZUL }}>{titulo}</span>
                  <span style={{ fontSize: 11, color: TER }}>{nombreIdea}</span>
                </div>

                <h3 style={{ margin: "30px 0 0", fontFamily: "Georgia, 'Times New Roman', serif", fontSize: 29, fontWeight: 700, letterSpacing: "-0.4px", color: TINTA }}>{titulo}</h3>
                {intro && <p style={{ margin: "12px 0 0", fontSize: 14.5, lineHeight: 1.7, color: SEC }}>{intro}</p>}

                {/* tres cifras entre dos hilos */}
                <div style={{ display: "flex", marginTop: 28, borderTop: `1px solid ${HILO}`, borderBottom: `1px solid ${HILO}` }}>
                  {cifra(dias, "días de camino")}
                  {cifra(accionesCumplidas, "acciones cumplidas")}
                  {cifra(N, "hitos alcanzados", cerrada ? VERDE : undefined)}
                </div>

                {/* mapa de hitos del viaje */}
                {N > 0 && (
                  <div style={{ marginTop: 30 }}>
                    <div style={{ fontSize: 10.5, fontWeight: 700, letterSpacing: "1.5px", textTransform: "uppercase", color: TER, marginBottom: 20 }}>Tu viaje completo</div>
                    <div style={{ position: "relative", height: 14, display: "flex", alignItems: "center" }}>
                      <div
                        style={{
                          position: "absolute",
                          left: `${inset}%`,
                          right: `${inset}%`,
                          height: 1.5,
                          background: cerrada ? `linear-gradient(to right, ${AZUL} 0%, ${AZUL} 78%, ${VERDE} 100%)` : AZUL,
                        }}
                      />
                      <div style={{ position: "relative", display: "grid", gridTemplateColumns: `repeat(${N}, 1fr)`, width: "100%", alignItems: "center" }}>
                        {hitos.map((h, i) => {
                          const esUltimo = i === N - 1;
                          const verde = cerrada && esUltimo;
                          return (
                            <div key={i} style={{ display: "flex", justifyContent: "center" }}>
                              <span style={{ width: verde ? 13 : 9, height: verde ? 13 : 9, borderRadius: "50%", background: verde ? VERDE : AZUL }} />
                            </div>
                          );
                        })}
                      </div>
                    </div>
                    <div style={{ display: "grid", gridTemplateColumns: `repeat(${N}, 1fr)`, gap: 8, marginTop: 12 }}>
                      {hitos.map((h, i) => {
                        const verde = cerrada && i === N - 1;
                        return (
                          <div key={i} style={{ textAlign: "center" }}>
                            <div style={{ fontSize: 11.5, color: TER, fontVariantNumeric: "tabular-nums" }}>{fechaMapa(h.fecha)}</div>
                            <div style={{ fontSize: 12.5, fontWeight: verde ? 700 : 600, marginTop: 2, lineHeight: 1.35, color: verde ? VERDE : TINTA }}>{h.nombre}</div>
                          </div>
                        );
                      })}
                    </div>
                  </div>
                )}

                {/* caja de cierre: verde si cerró (con el motivo), gris si sigue */}
                {cerrada ? (
                  <div style={{ marginTop: 28, borderRadius: 8, border: `1px solid #BFE3C6`, background: "#F1F9F3", padding: "18px 22px" }}>
                    <div style={{ fontSize: 10.5, fontWeight: 700, letterSpacing: "1.5px", textTransform: "uppercase", color: VERDE, marginBottom: 8 }}>Aquí acaba tu idea y nace tu proyecto</div>
                    {cierreMotivo && (
                      <div style={{ fontSize: 15, lineHeight: 1.6, fontFamily: "Georgia, serif", color: TINTA }}>«{cierreMotivo}»</div>
                    )}
                  </div>
                ) : (
                  <div style={{ marginTop: 28, borderRadius: 8, border: `1px solid ${HILO}`, background: "#F4F6F9", padding: "18px 22px" }}>
                    <div style={{ fontSize: 14, lineHeight: 1.6, color: SEC }}>Tu idea sigue en marcha. Cuando la des por realizada, aquí quedará tu cierre con tus propias palabras.</div>
                  </div>
                )}

                {/* dos columnas de texto */}
                {(loQueMovio || loQuePendiente) && (
                  <div style={{ marginTop: 30, display: "grid", gridTemplateColumns: "1fr 1fr", gap: 26 }}>
                    <div>
                      <div style={{ fontSize: 10.5, fontWeight: 700, letterSpacing: "1.5px", textTransform: "uppercase", color: TER, marginBottom: 10 }}>Lo que más te movió el camino</div>
                      <div style={{ fontSize: 14, lineHeight: 1.65, color: TINTA }}>{loQueMovio}</div>
                    </div>
                    <div>
                      <div style={{ fontSize: 10.5, fontWeight: 700, letterSpacing: "1.5px", textTransform: "uppercase", color: TER, marginBottom: 10 }}>Lo que quedó pendiente</div>
                      <div style={{ fontSize: 14, lineHeight: 1.65, color: TINTA }}>{loQuePendiente}</div>
                    </div>
                  </div>
                )}
              </div>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  );
}
