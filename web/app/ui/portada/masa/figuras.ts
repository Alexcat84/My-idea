/**
 * Las cinco figuras del ciclo (foco, lente, brujula, escalera, casa),
 * dibujadas con los mismos trazos de las muestras aprobadas y muestreadas
 * en puntos para las particulas.
 *
 * Diferencia con las muestras: cada figura se centra por su caja y se
 * escala para que su lado mayor mida TAMANO_FIGURA, asi todas quedan
 * centradas exactas y al mismo 80 % del lado menor.
 */
import { FIGURAS, type NombreFigura } from "./ciclo";
import { TAMANO_FIGURA } from "./encuadre";

type Pincel = CanvasRenderingContext2D | OffscreenCanvasRenderingContext2D;

const LADO = 512;

const TRAZOS: Record<NombreFigura, (g: Pincel) => void> = {
  foco(g) {
    g.beginPath(); g.arc(256, 200, 108, Math.PI * 0.78, Math.PI * 2.22); g.stroke();
    g.beginPath(); g.moveTo(190, 283); g.quadraticCurveTo(210, 318, 212, 350);
    g.moveTo(322, 283); g.quadraticCurveTo(302, 318, 300, 350); g.stroke();
    g.beginPath(); g.moveTo(212, 362); g.lineTo(300, 362);
    g.moveTo(218, 392); g.lineTo(294, 392); g.moveTo(232, 420); g.lineTo(280, 420); g.stroke();
    g.lineWidth = 10;
    g.beginPath(); g.moveTo(228, 300); g.lineTo(240, 230); g.lineTo(256, 262); g.lineTo(272, 230); g.lineTo(284, 300); g.stroke();
    g.lineWidth = 12;
    const rayos: ReadonlyArray<readonly [number, number, number, number]> = [
      [256, 58, 256, 30], [150, 100, 128, 78], [362, 100, 384, 78], [110, 200, 80, 200], [402, 200, 432, 200],
    ];
    for (const [x0, y0, x1, y1] of rayos) {
      g.beginPath(); g.moveTo(x0, y0); g.lineTo(x1, y1); g.stroke();
    }
  },
  lente(g) {
    g.lineWidth = 18; g.beginPath(); g.arc(222, 214, 118, 0, Math.PI * 2); g.stroke();
    g.lineWidth = 10; g.beginPath(); g.arc(222, 214, 78, Math.PI * 1.1, Math.PI * 1.45); g.stroke();
    g.lineWidth = 34; g.beginPath(); g.moveTo(312, 304); g.lineTo(416, 408); g.stroke();
  },
  brujula(g) {
    g.lineWidth = 16; g.beginPath(); g.arc(256, 256, 170, 0, Math.PI * 2); g.stroke();
    g.lineWidth = 10;
    for (let a = 0; a < 8; a++) {
      const ang = (a * Math.PI) / 4;
      const r1 = a % 2 ? 150 : 138;
      g.beginPath(); g.moveTo(256 + Math.cos(ang) * r1, 256 + Math.sin(ang) * r1);
      g.lineTo(256 + Math.cos(ang) * 160, 256 + Math.sin(ang) * 160); g.stroke();
    }
    g.beginPath(); g.moveTo(256, 118); g.lineTo(288, 256); g.lineTo(224, 256); g.closePath(); g.fill();
    g.lineWidth = 12;
    g.beginPath(); g.moveTo(256, 394); g.lineTo(288, 256); g.moveTo(256, 394); g.lineTo(224, 256); g.stroke();
    g.beginPath(); g.arc(256, 256, 12, 0, Math.PI * 2); g.fill();
  },
  escalera(g) {
    g.lineWidth = 16; g.beginPath();
    g.moveTo(92, 420); g.lineTo(92, 356); g.lineTo(176, 356); g.lineTo(176, 288);
    g.lineTo(260, 288); g.lineTo(260, 220); g.lineTo(344, 220); g.lineTo(344, 152); g.lineTo(424, 152);
    g.stroke();
    g.beginPath(); g.moveTo(80, 430); g.lineTo(432, 430); g.stroke();
    g.lineWidth = 10; g.beginPath(); g.moveTo(410, 150); g.lineTo(410, 70); g.stroke();
    g.beginPath(); g.moveTo(410, 72); g.lineTo(462, 90); g.lineTo(410, 108); g.closePath(); g.fill();
  },
  casa(g) {
    g.lineWidth = 16;
    g.beginPath(); g.moveTo(118, 262); g.lineTo(256, 128); g.lineTo(394, 262); g.stroke();
    g.beginPath(); g.moveTo(152, 236); g.lineTo(152, 420); g.lineTo(360, 420); g.lineTo(360, 236); g.stroke();
    g.beginPath(); g.moveTo(228, 420); g.lineTo(228, 330); g.lineTo(284, 330); g.lineTo(284, 420); g.stroke();
    g.lineWidth = 10; g.beginPath(); g.rect(304, 278, 36, 36); g.stroke();
    g.lineWidth = 14; g.beginPath(); g.moveTo(322, 200); g.lineTo(322, 150); g.lineTo(350, 150); g.lineTo(350, 226); g.stroke();
  },
};

/** PRNG sembrado (mulberry32): la misma figura sale igual en cada visita. */
export function azarSembrado(semilla: number): () => number {
  let s = semilla >>> 0;
  return () => {
    s = (s + 0x6d2b79f5) >>> 0;
    let z = s;
    z = Math.imul(z ^ (z >>> 15), z | 1);
    z ^= z + Math.imul(z ^ (z >>> 7), z | 61);
    return ((z ^ (z >>> 14)) >>> 0) / 4294967296;
  };
}

/**
 * Convierte pixeles encendidos (x, y en el lienzo de LADO) en `n` puntos
 * de mundo: centrados por la caja y con el lado mayor = TAMANO_FIGURA.
 * Separado del dibujo para poder probarlo sin canvas.
 */
export function normalizarPuntos(pixeles: ArrayLike<number>, n: number, azar: () => number, grosorZ = 0.05): Float32Array {
  const total = pixeles.length / 2;
  const salida = new Float32Array(n * 3);
  if (total === 0) return salida;
  let minX = Infinity, minY = Infinity, maxX = -Infinity, maxY = -Infinity;
  for (let i = 0; i < total; i++) {
    const x = pixeles[i * 2];
    const y = pixeles[i * 2 + 1];
    if (x < minX) minX = x;
    if (x > maxX) maxX = x;
    if (y < minY) minY = y;
    if (y > maxY) maxY = y;
  }
  // +1: cada pixel ocupa su celda completa
  const cx = (minX + maxX + 1) / 2;
  const cy = (minY + maxY + 1) / 2;
  const escala = TAMANO_FIGURA / Math.max(maxX - minX + 1, maxY - minY + 1);
  // Reparto estratificado: se recorre una permutacion de los pixeles y se
  // repite solo si faltan, asi no hay grumos ni huecos por azar.
  const orden = new Uint32Array(total);
  for (let i = 0; i < total; i++) orden[i] = i;
  for (let i = total - 1; i > 0; i--) {
    const j = Math.floor(azar() * (i + 1));
    const tmp = orden[i];
    orden[i] = orden[j];
    orden[j] = tmp;
  }
  for (let i = 0; i < n; i++) {
    const k = orden[i % total];
    const x = pixeles[k * 2] + azar();
    const y = pixeles[k * 2 + 1] + azar();
    salida[i * 3] = (x - cx) * escala;
    salida[i * 3 + 1] = -(y - cy) * escala;
    salida[i * 3 + 2] = (azar() - 0.5) * grosorZ;
  }
  return salida;
}

/** Dibuja la figura y devuelve `n` puntos de mundo sobre sus trazos. */
export function muestrearFigura(nombre: NombreFigura, n: number, semilla: number): Float32Array {
  // En un worker no hay document: OffscreenCanvas cuando existe.
  let g: Pincel | null;
  if (typeof OffscreenCanvas !== "undefined") {
    g = new OffscreenCanvas(LADO, LADO).getContext("2d", { willReadFrequently: true });
  } else {
    const lienzo = document.createElement("canvas");
    lienzo.width = LADO;
    lienzo.height = LADO;
    g = lienzo.getContext("2d", { willReadFrequently: true });
  }
  if (!g) return new Float32Array(n * 3);
  g.strokeStyle = "#fff";
  g.fillStyle = "#fff";
  g.lineCap = "round";
  g.lineJoin = "round";
  g.lineWidth = 16;
  TRAZOS[nombre](g);
  const datos = g.getImageData(0, 0, LADO, LADO).data;
  const encendidos: number[] = [];
  for (let y = 0; y < LADO; y++) {
    for (let x = 0; x < LADO; x++) {
      if (datos[(y * LADO + x) * 4 + 3] > 128) encendidos.push(x, y);
    }
  }
  return normalizarPuntos(encendidos, n, azarSembrado(semilla));
}

/**
 * Muestrea las cinco figuras cediendo el hilo entre una y otra, para no
 * crear una tarea larga en el arranque. La primera llega en cuanto esta.
 */
export async function muestrearTodas(
  n: number,
  alListo: (indice: number, puntos: Float32Array) => void,
  cancelado: () => boolean,
): Promise<void> {
  for (let i = 0; i < FIGURAS.length; i++) {
    if (cancelado()) return;
    alListo(i, muestrearFigura(FIGURAS[i], n, 1000 + i));
    await new Promise<void>((resolver) => setTimeout(resolver, 0));
  }
}
