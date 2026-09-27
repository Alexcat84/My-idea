/**
 * Las cinco figuras del ciclo (foco, lente, brujula, escalera, casa),
 * dibujadas con los mismos trazos de las muestras aprobadas. Dos salidas:
 *  - campoFigura: un campo de distancia con signo, para que la misma masa
 *    liquida se transforme en la figura (motor three.js);
 *  - muestrearFigura: puntos sobre los trazos, para el respaldo de particulas.
 *
 * Diferencia con las muestras: cada figura se centra por su caja y se
 * escala para que su lado mayor mida TAMANO_FIGURA, asi todas quedan
 * centradas exactas y al mismo 80 % del lado menor.
 */
import { FIGURAS, type NombreFigura } from "./ciclo";
import { RADIO_LIMITE, TAMANO_FIGURA } from "./encuadre";

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
  const { cx, cy, escala } = normalizacion(pixeles);
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

/**
 * Centro de la caja de los pixeles encendidos y escala pixel -> mundo que
 * deja el lado mayor en TAMANO_FIGURA: mundo = (pixel - centro) * escala.
 */
export function normalizacion(pixeles: ArrayLike<number>): { cx: number; cy: number; escala: number } {
  const total = pixeles.length / 2;
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
  return {
    cx: (minX + maxX + 1) / 2,
    cy: (minY + maxY + 1) / 2,
    escala: TAMANO_FIGURA / Math.max(maxX - minX + 1, maxY - minY + 1),
  };
}

/**
 * Dibuja la figura en un lienzo de `lado` px (los trazos estan pensados
 * para 512) y devuelve su mascara: 1 donde hay trazo.
 */
function rasterizar(nombre: NombreFigura, lado: number): Uint8Array {
  // En un worker no hay document: OffscreenCanvas cuando existe.
  let g: Pincel | null;
  if (typeof OffscreenCanvas !== "undefined") {
    g = new OffscreenCanvas(lado, lado).getContext("2d", { willReadFrequently: true });
  } else {
    const lienzo = document.createElement("canvas");
    lienzo.width = lado;
    lienzo.height = lado;
    g = lienzo.getContext("2d", { willReadFrequently: true });
  }
  const mascara = new Uint8Array(lado * lado);
  if (!g) return mascara;
  g.scale(lado / LADO, lado / LADO);
  g.strokeStyle = "#fff";
  g.fillStyle = "#fff";
  g.lineCap = "round";
  g.lineJoin = "round";
  g.lineWidth = 16;
  TRAZOS[nombre](g);
  const datos = g.getImageData(0, 0, lado, lado).data;
  for (let i = 0; i < lado * lado; i++) mascara[i] = datos[i * 4 + 3] > 128 ? 1 : 0;
  return mascara;
}

function encendidosDe(mascara: Uint8Array, lado: number): number[] {
  const encendidos: number[] = [];
  for (let y = 0; y < lado; y++) {
    for (let x = 0; x < lado; x++) if (mascara[y * lado + x]) encendidos.push(x, y);
  }
  return encendidos;
}

/** Dibuja la figura y devuelve `n` puntos de mundo sobre sus trazos. */
export function muestrearFigura(nombre: NombreFigura, n: number, semilla: number): Float32Array {
  return normalizarPuntos(encendidosDe(rasterizar(nombre, LADO), LADO), n, azarSembrado(semilla));
}

/**
 * Transformada de distancia euclidea exacta (Felzenszwalb y Huttenlocher),
 * al cuadrado y en pixeles: para cada pixel, la distancia al pixel mas
 * cercano donde `mascara` vale `objetivo`.
 */
export function distanciaCuadrada(mascara: Uint8Array, ancho: number, alto: number, objetivo: 0 | 1): Float64Array {
  const INF = 1e20;
  const d = new Float64Array(ancho * alto);
  for (let i = 0; i < d.length; i++) d[i] = mascara[i] === objetivo ? 0 : INF;
  const n = Math.max(ancho, alto);
  const f = new Float64Array(n);
  const salida = new Float64Array(n);
  const v = new Int32Array(n);
  const z = new Float64Array(n + 1);
  const pasada = (largo: number) => {
    let k = 0;
    v[0] = 0;
    z[0] = -INF;
    z[1] = INF;
    for (let q = 1; q < largo; q++) {
      let s = (f[q] + q * q - (f[v[k]] + v[k] * v[k])) / (2 * q - 2 * v[k]);
      while (s <= z[k]) {
        k--;
        s = (f[q] + q * q - (f[v[k]] + v[k] * v[k])) / (2 * q - 2 * v[k]);
      }
      k++;
      v[k] = q;
      z[k] = s;
      z[k + 1] = INF;
    }
    k = 0;
    for (let q = 0; q < largo; q++) {
      while (z[k + 1] < q) k++;
      salida[q] = (q - v[k]) * (q - v[k]) + f[v[k]];
    }
  };
  for (let x = 0; x < ancho; x++) {
    for (let y = 0; y < alto; y++) f[y] = d[y * ancho + x];
    pasada(alto);
    for (let y = 0; y < alto; y++) d[y * ancho + x] = salida[y];
  }
  for (let y = 0; y < alto; y++) {
    for (let x = 0; x < ancho; x++) f[x] = d[y * ancho + x];
    pasada(ancho);
    for (let x = 0; x < ancho; x++) d[y * ancho + x] = salida[x];
  }
  return d;
}

/**
 * Distancia con signo al borde del trazo, en pixeles: negativa dentro,
 * positiva fuera, medida entre centros de pixel (media celda de ajuste).
 */
export function distanciaConSigno(mascara: Uint8Array, ancho: number, alto: number): Float32Array {
  const aDentro = distanciaCuadrada(mascara, ancho, alto, 1);
  const aFuera = distanciaCuadrada(mascara, ancho, alto, 0);
  const d = new Float32Array(ancho * alto);
  for (let i = 0; i < d.length; i++) {
    d[i] = mascara[i] ? -(Math.sqrt(aFuera[i]) - 0.5) : Math.sqrt(aDentro[i]) - 0.5;
  }
  return d;
}

/** Lado del lienzo con que se calcula el campo de cada figura. */
export const LADO_RASTER_CAMPO = 384;
/** Lado (en texeles) del campo que se sube a la GPU. */
export const LADO_CAMPO = 256;
/** El campo cubre el cuadrado de mundo [-EXTENSION_CAMPO, EXTENSION_CAMPO]^2. */
export const EXTENSION_CAMPO = RADIO_LIMITE;

/**
 * Campo de distancia con signo de la figura, en unidades de mundo, sobre
 * una grilla LADO_CAMPO x LADO_CAMPO que cubre [-EXTENSION_CAMPO, +]^2.
 * Fila 0 = y minima (como lee la textura en WebGL). Mismo centrado y
 * escala que las particulas: la figura queda al 80 % del lado menor.
 */
export function campoFigura(nombre: NombreFigura): Float32Array {
  const r = LADO_RASTER_CAMPO;
  const mascara = rasterizar(nombre, r);
  const campo = new Float32Array(LADO_CAMPO * LADO_CAMPO);
  const encendidos = encendidosDe(mascara, r);
  if (encendidos.length === 0) return campo.fill(EXTENSION_CAMPO);
  const { cx, cy, escala } = normalizacion(encendidos);
  const dpx = distanciaConSigno(mascara, r, r);
  const muestra = (px: number, py: number) => {
    // bilineal entre centros de pixel; fuera del lienzo se suma lo que falta
    const x = Math.min(Math.max(px - 0.5, 0), r - 1);
    const y = Math.min(Math.max(py - 0.5, 0), r - 1);
    const x0 = Math.floor(x);
    const y0 = Math.floor(y);
    const x1 = Math.min(x0 + 1, r - 1);
    const y1 = Math.min(y0 + 1, r - 1);
    const fx = x - x0;
    const fy = y - y0;
    const a = dpx[y0 * r + x0] * (1 - fx) + dpx[y0 * r + x1] * fx;
    const b = dpx[y1 * r + x0] * (1 - fx) + dpx[y1 * r + x1] * fx;
    return a * (1 - fy) + b * fy + Math.hypot(px - 0.5 - x, py - 0.5 - y);
  };
  const paso = (2 * EXTENSION_CAMPO) / LADO_CAMPO;
  for (let j = 0; j < LADO_CAMPO; j++) {
    const yMundo = -EXTENSION_CAMPO + (j + 0.5) * paso;
    for (let i = 0; i < LADO_CAMPO; i++) {
      const xMundo = -EXTENSION_CAMPO + (i + 0.5) * paso;
      campo[j * LADO_CAMPO + i] = muestra(xMundo / escala + cx, -yMundo / escala + cy) * escala;
    }
  }
  // La mascara binaria deja escalones de medio pixel en las curvas; dos
  // pasadas de un filtro binomial [1 2 1] los alisan sin mover el trazo.
  suavizar(campo, LADO_CAMPO);
  suavizar(campo, LADO_CAMPO);
  return campo;
}

/** Filtro binomial separable [1 2 1] / 4, con bordes replicados. */
function suavizar(campo: Float32Array, lado: number): void {
  const tmp = new Float32Array(campo.length);
  for (let j = 0; j < lado; j++) {
    for (let i = 0; i < lado; i++) {
      const a = campo[j * lado + Math.max(i - 1, 0)];
      const b = campo[j * lado + i];
      const c = campo[j * lado + Math.min(i + 1, lado - 1)];
      tmp[j * lado + i] = (a + 2 * b + c) / 4;
    }
  }
  for (let j = 0; j < lado; j++) {
    for (let i = 0; i < lado; i++) {
      const a = tmp[Math.max(j - 1, 0) * lado + i];
      const b = tmp[j * lado + i];
      const c = tmp[Math.min(j + 1, lado - 1) * lado + i];
      campo[j * lado + i] = (a + 2 * b + c) / 4;
    }
  }
}

/** Calcula los cinco campos cediendo el hilo entre uno y otro. */
export async function calcularCampos(
  alListo: (indice: number, campo: Float32Array) => void,
  cancelado: () => boolean,
): Promise<void> {
  for (let i = 0; i < FIGURAS.length; i++) {
    if (cancelado()) return;
    alListo(i, campoFigura(FIGURAS[i]));
    await new Promise<void>((resolver) => setTimeout(resolver, 0));
  }
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
