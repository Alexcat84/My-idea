/**
 * Las figuras de la masa: ideas hechas realidad (decision del fundador, 8 oct
 * 2026; el catalogo vive en catalogo.ts). Cada figura llega PRECALCULADA: el
 * horno (scripts/portada/hornear_figuras.ts) la dibuja, calcula aqui su campo de
 * distancia con signo (campoDesdeMascara) y lo guarda cuantizado a 16 bits en
 * public/portada/figuras/<nombre>.bin. El navegador no dibuja ni calcula: baja
 * el campo de la figura que va a formar (cargarFigura) y lo usa tal cual:
 *  - el motor three.js lo sube como textura y la masa se transforma en ella;
 *  - el respaldo de particulas saca de el puntos dentro del trazo (puntosDeCampo).
 *
 * Cada figura se centra por su caja y se escala para que su lado mayor mida
 * TAMANO_FIGURA: todas quedan centradas y al mismo 80 % del lado menor.
 */
import { RADIO_LIMITE, TAMANO_FIGURA } from "./encuadre";

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

/** Lado del lienzo con que el horno dibuja cada figura. */
export const LADO_RASTER_CAMPO = 384;
/** Lado (en texeles) del campo precalculado que se sube a la GPU. */
export const LADO_CAMPO = 128;
/** El campo cubre el cuadrado de mundo [-EXTENSION_CAMPO, EXTENSION_CAMPO]^2. */
export const EXTENSION_CAMPO = RADIO_LIMITE;
/** El campo guardado se recorta a [-RANGO_CAMPO, RANGO_CAMPO] (unidades de mundo):
 * cubre la diagonal del cuadrado (1.8 * raiz de 2 = 2.55). */
export const RANGO_CAMPO = 2.6;

/**
 * Campo de distancia con signo de una figura ya dibujada (`mascara`, 1 donde
 * hay trazo, en un lienzo de `r` x `r`), en unidades de mundo, sobre una grilla
 * `lado` x `lado` que cubre [-EXTENSION_CAMPO, +]^2. Fila 0 = y minima (como lee
 * la textura en WebGL). Centrada por su caja y con el lado mayor en
 * TAMANO_FIGURA: la figura queda al 80 % del lado menor. Lo usa el horno.
 */
export function campoDesdeMascara(mascara: Uint8Array, r: number, lado = LADO_CAMPO): Float32Array {
  const campo = new Float32Array(lado * lado);
  const encendidos: number[] = [];
  for (let y = 0; y < r; y++) for (let x = 0; x < r; x++) if (mascara[y * r + x]) encendidos.push(x, y);
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
  const paso = (2 * EXTENSION_CAMPO) / lado;
  for (let j = 0; j < lado; j++) {
    const yMundo = -EXTENSION_CAMPO + (j + 0.5) * paso;
    for (let i = 0; i < lado; i++) {
      const xMundo = -EXTENSION_CAMPO + (i + 0.5) * paso;
      campo[j * lado + i] = muestra(xMundo / escala + cx, -yMundo / escala + cy) * escala;
    }
  }
  // La mascara binaria deja escalones de medio pixel en las curvas; una pasada
  // de un filtro binomial [1 2 1] los alisa sin mover el trazo.
  suavizar(campo, lado);
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

/** Campo -> 16 bits: [-RANGO_CAMPO, RANGO_CAMPO] lineal sobre [0, 65535]. */
export function codificarCampo(campo: Float32Array): Uint16Array {
  const salida = new Uint16Array(campo.length);
  for (let i = 0; i < campo.length; i++) {
    const d = Math.min(Math.max(campo[i], -RANGO_CAMPO), RANGO_CAMPO);
    salida[i] = Math.round((d / RANGO_CAMPO / 2 + 0.5) * 65535);
  }
  return salida;
}

/** 16 bits -> campo, el inverso de codificarCampo. */
export function decodificarCampo(datos: Uint16Array): Float32Array {
  const campo = new Float32Array(datos.length);
  for (let i = 0; i < datos.length; i++) campo[i] = ((datos[i] / 65535) * 2 - 1) * RANGO_CAMPO;
  return campo;
}

/**
 * `n` puntos de mundo DENTRO del trazo (campo < 0), para el respaldo de
 * particulas: se recorre una permutacion de los texeles del trazo (sin grumos
 * ni huecos por azar), cada punto con un temblor dentro de su texel.
 */
export function puntosDeCampo(campo: Float32Array, lado: number, n: number, azar: () => number, grosorZ = 0.05): Float32Array {
  const salida = new Float32Array(n * 3);
  const dentro: number[] = [];
  for (let k = 0; k < lado * lado; k++) if (campo[k] < 0) dentro.push(k);
  if (dentro.length === 0) return salida;
  for (let i = dentro.length - 1; i > 0; i--) {
    const j = Math.floor(azar() * (i + 1));
    const tmp = dentro[i];
    dentro[i] = dentro[j];
    dentro[j] = tmp;
  }
  const paso = (2 * EXTENSION_CAMPO) / lado;
  for (let p = 0; p < n; p++) {
    const k = dentro[p % dentro.length];
    const i = k % lado;
    const j = Math.floor(k / lado);
    salida[p * 3] = -EXTENSION_CAMPO + (i + azar()) * paso;
    salida[p * 3 + 1] = -EXTENSION_CAMPO + (j + azar()) * paso;
    salida[p * 3 + 2] = (azar() - 0.5) * grosorZ;
  }
  return salida;
}

/** Donde se sirven los campos precalculados. */
export const RUTA_FIGURAS = "/portada/figuras";

const cargas = new Map<string, Promise<Float32Array>>();

/**
 * Baja (una sola vez por visita) el campo precalculado de una figura. Un fallo
 * de red no se recuerda: el siguiente pedido lo intenta de nuevo.
 */
export function cargarFigura(nombre: string): Promise<Float32Array> {
  const previa = cargas.get(nombre);
  if (previa) return previa;
  const carga = fetch(`${RUTA_FIGURAS}/${nombre}.bin`)
    .then((res) => {
      if (!res.ok) throw new Error(`figura ${nombre}: ${res.status}`);
      return res.arrayBuffer();
    })
    .then((b) => {
      if (b.byteLength !== LADO_CAMPO * LADO_CAMPO * 2) throw new Error(`figura ${nombre}: tamano ${b.byteLength}`);
      return decodificarCampo(new Uint16Array(b));
    });
  cargas.set(nombre, carga);
  carga.catch(() => cargas.delete(nombre));
  return carga;
}
