/**
 * Shaders de la masa. Cada shader publica la lista EXACTA de uniformes
 * que declara (UNIFORMES_*): el motor construye sus uniformes tipados por
 * esa lista (TypeScript exige que esten todos) y glsl.test.ts verifica que
 * el GLSL declare esos y ningun otro, sin nombres repetidos ni nombres que
 * ya reservan GLSL o el prefijo que three.js antepone.
 *
 * Los colores se escriben en espacio de pantalla (sin conversion de
 * salida): asi el negro del nucleo es el negro que se ve.
 */
import { ENVOLTURA_PIEL, RADIO_LIMITE } from "./encuadre";

/**
 * Ruido simplex 3D de webgl-noise (Ashima Arts / Stefan Gustavson,
 * licencia MIT, github.com/ashima/webgl-noise).
 */
export const RUIDO = /* glsl */ `
vec3 mod289(vec3 x) { return x - floor(x * (1.0 / 289.0)) * 289.0; }
vec4 mod289(vec4 x) { return x - floor(x * (1.0 / 289.0)) * 289.0; }
vec4 permute(vec4 x) { return mod289(((x * 34.0) + 10.0) * x); }
vec4 taylorInvSqrt(vec4 r) { return 1.79284291400159 - 0.85373472095314 * r; }
float snoise(vec3 v) {
  const vec2 C = vec2(1.0 / 6.0, 1.0 / 3.0);
  const vec4 D = vec4(0.0, 0.5, 1.0, 2.0);
  vec3 i = floor(v + dot(v, C.yyy));
  vec3 x0 = v - i + dot(i, C.xxx);
  vec3 g = step(x0.yzx, x0.xyz);
  vec3 l = 1.0 - g;
  vec3 i1 = min(g.xyz, l.zxy);
  vec3 i2 = max(g.xyz, l.zxy);
  vec3 x1 = x0 - i1 + C.xxx;
  vec3 x2 = x0 - i2 + C.yyy;
  vec3 x3 = x0 - D.yyy;
  i = mod289(i);
  vec4 p = permute(permute(permute(
    i.z + vec4(0.0, i1.z, i2.z, 1.0)) +
    i.y + vec4(0.0, i1.y, i2.y, 1.0)) +
    i.x + vec4(0.0, i1.x, i2.x, 1.0));
  float n_ = 0.142857142857;
  vec3 ns = n_ * D.wyz - D.xzx;
  vec4 j = p - 49.0 * floor(p * ns.z * ns.z);
  vec4 x_ = floor(j * ns.z);
  vec4 y_ = floor(j - 7.0 * x_);
  vec4 x = x_ * ns.x + ns.yyyy;
  vec4 y = y_ * ns.x + ns.yyyy;
  vec4 h = 1.0 - abs(x) - abs(y);
  vec4 b0 = vec4(x.xy, y.xy);
  vec4 b1 = vec4(x.zw, y.zw);
  vec4 s0 = floor(b0) * 2.0 + 1.0;
  vec4 s1 = floor(b1) * 2.0 + 1.0;
  vec4 sh = -step(h, vec4(0.0));
  vec4 a0 = b0.xzyw + s0.xzyw * sh.xxyy;
  vec4 a1 = b1.xzyw + s1.xzyw * sh.zzww;
  vec3 p0 = vec3(a0.xy, h.x);
  vec3 p1 = vec3(a0.zw, h.y);
  vec3 p2 = vec3(a1.xy, h.z);
  vec3 p3 = vec3(a1.zw, h.w);
  vec4 norm = taylorInvSqrt(vec4(dot(p0, p0), dot(p1, p1), dot(p2, p2), dot(p3, p3)));
  p0 *= norm.x; p1 *= norm.y; p2 *= norm.z; p3 *= norm.w;
  vec4 m = max(0.5 - vec4(dot(x0, x0), dot(x1, x1), dot(x2, x2), dot(x3, x3)), 0.0);
  m = m * m;
  return 105.0 * dot(m * m, vec4(dot(p0, x0), dot(p1, x1), dot(p2, x2), dot(p3, x3)));
}
`;

const decimal = (x: number) => (Number.isInteger(x) ? x.toFixed(1) : String(x));

/* ------------------------------------------------------------------ */
/* 1. El liquido: raymarching de una piel con ruido sobre un quad.     */
/* ------------------------------------------------------------------ */

export const UNIFORMES_LIQUIDO = [
  "uTiempo", "uLiquido", "uRadio", "uAspecto", "uTanMedio", "uCamZ", "uRotInv", "uPixelMundo",
] as const;

export interface OpcionesLiquido {
  pasos: number;
  octavas: number;
  deformacionCompleta: boolean;
  muestrasAo: number;
}

export const VERTICE_PANTALLA = /* glsl */ `
varying vec2 vUv;
void main() {
  vUv = uv;
  gl_Position = vec4(position.xy, 0.0, 1.0);
}
`;

export function fragmentoLiquido(o: OpcionesLiquido): string {
  return /* glsl */ `
#define PASOS ${o.pasos}
#define OCTAVAS ${o.octavas}
#define MUESTRAS_AO ${o.muestrasAo}
#define DEFORMACION_COMPLETA ${o.deformacionCompleta ? 1 : 0}
#define ENVOLTURA ${decimal(ENVOLTURA_PIEL)}

uniform float uTiempo;
uniform float uLiquido;
uniform float uRadio;
uniform float uAspecto;
uniform float uTanMedio;
uniform float uCamZ;
uniform mat3 uRotInv;
// Tamano de un pixel del render target a distancia 1 (antialias del borde).
uniform float uPixelMundo;
varying vec2 vUv;
${RUIDO}

float fbm(vec3 q) {
  float suma = 0.0;
  float peso = 0.62;
  for (int i = 0; i < OCTAVAS; i++) {
    suma += peso * snoise(q);
    q = q * 1.93 + vec3(1.7, -9.2, 3.1);
    peso *= 0.3;
  }
  return suma;
}

// Deformacion de dominio: un campo lento y grande que tuerce las coordenadas.
vec3 deformacion(vec3 q, float t) {
  vec3 k = q * 0.45 + vec3(0.0, t * 0.04, t * 0.06);
#if DEFORMACION_COMPLETA
  return vec3(snoise(k), snoise(k + vec3(31.4, 7.7, -2.9)), snoise(k + vec3(-5.1, 19.3, 11.7)));
#else
  float s = snoise(k);
  return vec3(s, -0.6 * s, 0.35 * s);
#endif
}

// La piel en dos escalas: ondulacion lenta y grande + temblor fino y rapido.
float piel(vec3 q, float t) {
  vec3 w = deformacion(q, t);
  float lenta = fbm(q * 0.58 + w * 0.5 + vec3(0.0, 0.0, t * 0.09));
  float fina = snoise(q * 3.4 + w * 0.25 + vec3(t * 0.9, -t * 0.7, t * 0.5));
  return lenta * 0.30 + fina * 0.012;
}

float radioActual() { return uRadio * (0.12 + 0.88 * uLiquido); }
// La gota chica tiembla en proporcion a su tamano.
float agitacion() { return (0.35 + 0.65 * uLiquido) * (radioActual() / uRadio); }

float mapa(vec3 pw) {
  vec3 q = uRotInv * pw;
  float rf = radioActual();
  float amp = agitacion();
  float base = length(q) - rf;
  float margen = ENVOLTURA * amp;
  // Lejos de la piel basta la esfera envolvente (cota inferior segura).
  if (base > margen + 0.05) return base - margen;
  return base - piel(q * (uRadio / rf), uTiempo) * amp;
}

vec3 normalPiel(vec3 q) {
  const vec2 e = vec2(1.0, -1.0) * 0.0035;
  return normalize(
    e.xyy * mapa(q + e.xyy) + e.yyx * mapa(q + e.yyx) +
    e.yxy * mapa(q + e.yxy) + e.xxx * mapa(q + e.xxx));
}

// Oclusion ambiental por SDF: cuanto se hunde la piel alrededor del punto.
float oclusion(vec3 q, vec3 n) {
#if MUESTRAS_AO > 0
  float o = 0.0;
  float peso = 1.0;
  for (int i = 1; i <= MUESTRAS_AO; i++) {
    float h = 0.03 + 0.14 * float(i) / float(MUESTRAS_AO);
    o += (h - mapa(q + n * h)) * peso;
    peso *= 0.7;
  }
  return clamp(1.0 - 2.4 * o, 0.0, 1.0);
#else
  return 1.0;
#endif
}

// Entorno procedural oscuro: el estudio negro que la piel refleja. Delante
// (hacia la camara) casi nada; detras, un contraluz ceniza amplio y una
// franja violeta: eso es lo que enciende el borde por fresnel.
vec3 entorno(vec3 d) {
  vec3 c = mix(vec3(0.008, 0.007, 0.014), vec3(0.030, 0.030, 0.042), smoothstep(-0.4, 0.9, d.y));
  float caja = dot(d, normalize(vec3(-0.70, 0.70, 0.15)));
  c += vec3(0.80, 0.82, 0.90) * smoothstep(0.80, 0.97, caja) * 0.55;
  float detras = smoothstep(0.05, -0.85, d.z);
  c += vec3(0.56, 0.57, 0.66) * detras * (0.30 + 0.25 * smoothstep(-0.6, 0.8, d.y));
  float franja = dot(d, normalize(vec3(0.80, -0.40, -0.45)));
  c += vec3(0.50, 0.36, 0.90) * smoothstep(0.35, 0.95, franja) * 0.55;
  return c;
}

void main() {
  if (uLiquido < 0.004) { gl_FragColor = vec4(0.0); return; }
  vec2 ndc = vUv * 2.0 - 1.0;
  vec3 ro = vec3(0.0, 0.0, uCamZ);
  vec3 rd = normalize(vec3(ndc.x * uAspecto * uTanMedio, ndc.y * uTanMedio, -1.0));

  float rf = radioActual();
  float limite = rf + ENVOLTURA * agitacion() + 0.45 * (rf / uRadio);
  float b = dot(ro, rd);
  float c = dot(ro, ro) - limite * limite;
  float h = b * b - c;
  if (h < 0.0) { gl_FragColor = vec4(0.0); return; }
  float sq = sqrt(h);
  float t = max(-b - sq, 0.0);
  float tFin = -b + sq;

  bool toca = false;
  vec3 pos = ro;
  float dMin = 1e5;
  float tMin = t;
  for (int i = 0; i < PASOS; i++) {
    pos = ro + rd * t;
    float d = mapa(pos);
    if (d < dMin) { dMin = d; tMin = t; }
    if (d < 0.0008 * t) { toca = true; break; }
    t += d * 0.65;
    if (t > tFin) break;
  }

  float cobertura = smoothstep(0.0, 0.25, uLiquido);
  if (!toca) {
    // Aura: la masa ilumina levemente el aire que la rodea. Se mide desde la
    // distancia del rayo al centro (suave, sin escalones) y se apaga antes
    // del borde de la esfera envolvente.
    float cerca = length(cross(ro, rd)) - rf;
    float g = exp(-max(cerca, 0.0) * 4.2) * 0.30 * cobertura;
    g *= 1.0 - smoothstep(limite - rf - 0.2, limite - rf, cerca);
    // Antialias de la silueta: el rayo que roza la piel sin tocarla se
    // lleva una fraccion del borde luminoso, en vez de un escalon.
    float roce = (1.0 - smoothstep(0.0, 2.5 * tMin * uPixelMundo, dMin)) * cobertura;
    vec3 aura = vec3(0.42, 0.38, 0.72) * g;
    gl_FragColor = vec4(mix(aura, vec3(0.30, 0.28, 0.42), roce), max(g * 0.4, roce));
    return;
  }

  vec3 n = normalPiel(pos);
  vec3 v = -rd;
  float ndv = clamp(dot(n, v), 0.0, 1.0);
  vec3 r = reflect(rd, n);
  float ao = oclusion(pos, n);

  // Fresnel de Schlick con dispersion: cada canal abre a su ritmo y el
  // reflejo se toma con el rayo apenas desviado por canal.
  float fr = 1.0 - ndv;
  vec3 fres = 0.04 + 0.96 * vec3(pow(fr, 4.2), pow(fr, 4.6), pow(fr, 5.0));
  vec3 refl = vec3(
    entorno(normalize(r + n * 0.07)).r,
    entorno(r).g,
    entorno(normalize(r - n * 0.07)).b);

  // Dos luces: clave ceniza arriba a la izquierda, contraluz violeta abajo a la derecha.
  vec3 l1 = normalize(vec3(-0.75, 0.80, 0.20));
  vec3 l2 = normalize(vec3(0.75, -0.35, -0.45));
  float esp1 = pow(max(dot(n, normalize(l1 + v)), 0.0), 90.0) * 1.1;
  float esp2 = pow(max(dot(n, normalize(l2 + v)), 0.0), 40.0) * 0.5;
  float dif1 = max(dot(n, l1), 0.0);
  float contraluz = fr * fr * clamp(dot(n, l2) * 0.5 + 0.5, 0.0, 1.0);

  // Brillo interior que respira: tenue y de frente, sin aclarar el nucleo.
  float respiro = 0.5 + 0.5 * sin(uTiempo * 0.85);
  float venas = 0.5 + 0.5 * snoise(uRotInv * pos * 1.6 + vec3(0.0, uTiempo * 0.15, 0.0));
  vec3 interior = vec3(0.13, 0.08, 0.24) * pow(ndv, 3.0) * (0.25 + 0.75 * respiro) * venas * 0.16;

  vec3 col = vec3(0.010, 0.009, 0.016) * (0.25 + dif1 * 0.9);
  col += interior;
  col += fres * refl * 1.7 * ao;
  col += vec3(0.86, 0.88, 0.96) * esp1 * ao;
  col += vec3(0.50, 0.38, 0.86) * (esp2 + contraluz * 0.55) * ao;
  // Borde luminoso: ceniza arriba y a la izquierda, violeta hacia la contraluz.
  float lado = smoothstep(0.35, 0.85, dot(n, l2) * 0.5 + 0.5);
  col += mix(vec3(0.60, 0.61, 0.70), vec3(0.56, 0.42, 0.98), lado) * pow(fr, 3.0) * 0.45 * ao;
  gl_FragColor = vec4(col * cobertura, cobertura);
}
`;
}

/* ------------------------------------------------------------------ */
/* 2. Composicion: fondo del hero + liquido escalado.                  */
/* ------------------------------------------------------------------ */

export const UNIFORMES_COMPOSICION = ["uLiquidoTex", "uTexelLiquido", "uLienzo"] as const;

/** Mismo degradado que el fondo CSS del hero (landing.css, .portada-hero). */
export const FONDO_CSS = "radial-gradient(circle at 50% 50%, #0b0a14 0%, #050409 38%, #000000 72%)";

export const FRAGMENTO_COMPOSICION = /* glsl */ `
uniform sampler2D uLiquidoTex;
uniform vec2 uTexelLiquido;
uniform vec2 uLienzo;
varying vec2 vUv;

vec3 fondo(vec2 px) {
  float r = length(px - 0.5 * uLienzo) / length(0.5 * uLienzo);
  vec3 c0 = vec3(11.0, 10.0, 20.0) / 255.0;
  vec3 c1 = vec3(5.0, 4.0, 9.0) / 255.0;
  if (r < 0.38) return mix(c0, c1, r / 0.38);
  return mix(c1, vec3(0.0), clamp((r - 0.38) / 0.34, 0.0, 1.0));
}

void main() {
  // El liquido llega a resolucion reducida: cinco muestras en tienda
  // suavizan la silueta al escalarlo, sin escalones ni contorno punteado.
  vec2 k = uTexelLiquido * 0.75;
  vec4 l = texture2D(uLiquidoTex, vUv) * 0.36
    + (texture2D(uLiquidoTex, vUv + vec2(k.x, k.y)) + texture2D(uLiquidoTex, vUv + vec2(-k.x, k.y))
     + texture2D(uLiquidoTex, vUv + vec2(k.x, -k.y)) + texture2D(uLiquidoTex, vUv + vec2(-k.x, -k.y))) * 0.16;
  gl_FragColor = vec4(l.rgb + fondo(gl_FragCoord.xy) * (1.0 - l.a), 1.0);
}
`;

/* ------------------------------------------------------------------ */
/* 3. Particulas: nacen en la piel, vuelan con rizo, forman la figura. */
/* ------------------------------------------------------------------ */

export const UNIFORMES_PARTICULAS = [
  "uTiempo", "uTiempoPrevio", "uMezcla", "uMezclaPrevia", "uLiquido", "uLiquidoPrevio",
  "uRadio", "uVis", "uTamPx", "uLienzo", "uCamara",
] as const;

export function verticeParticulas(pasosRizo: number): string {
  return /* glsl */ `
#define PASOS_RIZO ${pasosRizo}
#define RADIO_LIMITE ${decimal(RADIO_LIMITE)}

attribute vec3 aDir;
attribute vec3 aDestino;
attribute vec2 aAzar;
uniform float uTiempo;
uniform float uTiempoPrevio;
uniform float uMezcla;
uniform float uMezclaPrevia;
uniform float uLiquido;
uniform float uLiquidoPrevio;
uniform float uRadio;
uniform float uVis;
uniform float uTamPx;
uniform vec2 uLienzo;
uniform vec3 uCamara;
varying vec2 vLocal;
varying float vLargo;
varying float vRadioPx;
varying float vLuz;
varying float vAlfa;
${RUIDO}

vec3 potencial(vec3 q) {
  return vec3(snoise(q), snoise(q + vec3(31.416, -47.853, 12.793)), snoise(q + vec3(-233.145, -113.408, -185.31)));
}

// Ruido de rizo: rotacional de un potencial, un flujo sin fuentes ni sumideros.
vec3 rizo(vec3 q) {
  const float e = 0.08;
  vec3 p0 = potencial(q);
  vec3 px = potencial(q + vec3(e, 0.0, 0.0));
  vec3 py = potencial(q + vec3(0.0, e, 0.0));
  vec3 pz = potencial(q + vec3(0.0, 0.0, e));
  return vec3(
    (py.z - p0.z) - (pz.y - p0.y),
    (pz.x - p0.x) - (px.z - p0.z),
    (px.y - p0.y) - (py.x - p0.x)) / e;
}

float avance(float mezcla) { return clamp(mezcla * 1.6 - aAzar.x * 0.6, 0.0, 1.0); }

vec3 enLaPiel(float liquido, float t) {
  float rf = uRadio * (0.12 + 0.88 * liquido);
  float amp = (0.35 + 0.65 * liquido) * (rf / uRadio);
  return aDir * (rf + snoise(aDir * 0.85 + vec3(0.0, 0.0, t * 0.11)) * 0.16 * amp);
}

vec3 lugar(float m, float liquido, float t) {
  float e = m * m * (3.0 - 2.0 * m);
  vec3 p = mix(enLaPiel(liquido, t), aDestino, e);
  float vuelo = 4.0 * m * (1.0 - m);
  if (vuelo > 0.001) {
    // Integracion del rizo desenrollada (un bucle de una vuelta hace protestar al compilador D3D).
    vec3 semilla = vec3(aAzar.y * 5.0, t * 0.12, -t * 0.05);
    float paso = (0.16 / float(PASOS_RIZO)) * vuelo;
    p += rizo(p * 0.55 + semilla) * paso;
#if PASOS_RIZO >= 2
    p += rizo(p * 0.55 + semilla) * paso;
#endif
  }
  // Temblor minimo de la figura sostenida.
  p += vec3(sin(t * 1.3 + aAzar.y * 40.0), cos(t * 1.1 + aAzar.x * 30.0), 0.0) * 0.004 * e;
  return p * min(1.0, RADIO_LIMITE / max(length(p), 1e-4));
}

// 1 si el punto (mundo) queda detras de la masa vista desde la camara.
float detrasDeLaMasa(vec3 mundo) {
  if (uLiquido < 0.02) return 0.0;
  vec3 rd = mundo - uCamara;
  float dist = length(rd);
  rd /= dist;
  float ro = uRadio * (0.12 + 0.88 * uLiquido) * 0.97;
  float b = dot(uCamara, rd);
  float c = dot(uCamara, uCamara) - ro * ro;
  float h = b * b - c;
  if (h <= 0.0) return 0.0;
  float entrada = -b - sqrt(h);
  return smoothstep(0.0, 0.06, dist - entrada);
}

void main() {
  float mAhora = avance(uMezcla);
  float alfa = smoothstep(0.0, 0.10, mAhora) * uVis;
  vLocal = vec2(0.0);
  vLargo = 0.0;
  vRadioPx = 1.0;
  vLuz = 0.0;
  vAlfa = 0.0;
  if (alfa < 0.002) {
    // Fuera del recorte: sin costo de fragmentos.
    gl_Position = vec4(2.0, 2.0, 2.0, 1.0);
    return;
  }
  float e = mAhora * mAhora * (3.0 - 2.0 * mAhora);
  vec3 cabeza = lugar(mAhora, uLiquido, uTiempo);
  vec3 cola = lugar(avance(uMezclaPrevia), uLiquidoPrevio, uTiempoPrevio);
  vec4 mundoCabeza = modelMatrix * vec4(cabeza, 1.0);
  vec4 clipCabeza = projectionMatrix * viewMatrix * mundoCabeza;
  vec4 clipCola = projectionMatrix * viewMatrix * modelMatrix * vec4(cola, 1.0);

  vec2 pxCabeza = clipCabeza.xy / clipCabeza.w * 0.5 * uLienzo;
  vec2 pxCola = clipCola.xy / clipCola.w * 0.5 * uLienzo;
  vec2 delta = pxCabeza - pxCola;
  float largo = length(delta);
  vec2 eje = largo > 0.001 ? delta / largo : vec2(1.0, 0.0);
  vec2 perp = vec2(-eje.y, eje.x);
  float radio = max(uTamPx * (0.55 + aAzar.x * 0.9) * (uCamara.z / clipCabeza.w), 0.75);
  // Estelas cortas: nunca mas largas que unas pocas veces el grano.
  largo = min(largo, radio * 5.0);

  float a = mix(-radio, largo + radio, position.x);
  vec2 px = pxCabeza - eje * largo + eje * a + perp * position.y * radio;
  gl_Position = vec4(px / (0.5 * uLienzo) * clipCabeza.w, clipCabeza.z, clipCabeza.w);

  vLocal = vec2(a, position.y * radio);
  vLargo = largo;
  vRadioPx = radio;
  vLuz = mix(0.35, 0.86, e);
  vAlfa = alfa * (1.0 - detrasDeLaMasa(mundoCabeza.xyz)) * mix(0.75, 0.8, e);
}
`;
}

export const FRAGMENTO_PARTICULAS = /* glsl */ `
varying vec2 vLocal;
varying float vLargo;
varying float vRadioPx;
varying float vLuz;
varying float vAlfa;

void main() {
  if (vAlfa <= 0.0) discard;
  // Cabeza: un grano redondo de borde nitido en el extremo delantero.
  float cabeza = 1.0 - smoothstep(vRadioPx * 0.5, vRadioPx, length(vec2(vLocal.x - vLargo, vLocal.y)));
  // Estela: la capsula hasta la cola, mas fina y apagandose hacia atras.
  float dx = vLocal.x - clamp(vLocal.x, 0.0, vLargo);
  float cuerpo = 1.0 - smoothstep(vRadioPx * 0.2, vRadioPx * 0.7, length(vec2(dx, vLocal.y)));
  float estela = cuerpo * (0.06 + 0.5 * clamp(vLocal.x / max(vLargo, 1e-3), 0.0, 1.0));
  float a = max(cabeza, estela);
  if (a <= 0.0) discard;
  vec3 col = mix(vec3(0.03, 0.03, 0.05), vec3(0.82, 0.84, 0.92), vLuz);
  gl_FragColor = vec4(col, a * vAlfa);
}
`;

/* ------------------------------------------------------------------ */
/* 4. Acabado: vinieta leve y grano fino que no lavan el negro.        */
/* ------------------------------------------------------------------ */

export const UNIFORMES_ACABADO = ["tDiffuse", "uTiempo", "uLienzo", "uGrano", "uVineta"] as const;

export const FRAGMENTO_ACABADO = /* glsl */ `
uniform sampler2D tDiffuse;
uniform float uTiempo;
uniform vec2 uLienzo;
uniform float uGrano;
uniform float uVineta;
varying vec2 vUv;

float azar(vec2 q) { return fract(sin(dot(q, vec2(12.9898, 78.233))) * 43758.5453); }

void main() {
  vec3 c = texture2D(tDiffuse, vUv).rgb;
  vec2 q = vUv - 0.5;
  q.x *= uLienzo.x / uLienzo.y;
  // Vinieta: solo oscurece hacia los bordes.
  c *= 1.0 - uVineta * smoothstep(0.45, 1.25, length(q) * 1.6);
  // Hombro suave: comprime altas luces, deja el negro en cero.
  c = c / (1.0 + c * 0.18) * 1.12;
  // Grano proporcional a la luz: donde hay negro puro, sigue negro.
  float l = dot(c, vec3(0.299, 0.587, 0.114));
  float g = azar(gl_FragCoord.xy + fract(uTiempo * 7.13) * vec2(97.0, 57.0)) - 0.5;
  c += g * uGrano * smoothstep(0.0, 0.10, l) * (0.35 + l);
  // Tramado de medio escalon para que los degradados oscuros no hagan bandas.
  c += (azar(gl_FragCoord.xy * 1.37 + 3.1) - 0.5) / 255.0;
  gl_FragColor = vec4(max(c, 0.0), 1.0);
}
`;

/* ------------------------------------------------------------------ */
/* 5. Respaldo: solo particulas, WebGL1 crudo (sin three.js).          */
/* ------------------------------------------------------------------ */

export const UNIFORMES_RESPALDO = ["uProyeccion", "uModeloVista", "uTiempo", "uMezcla", "uTamPx"] as const;

export const VERTICE_RESPALDO = /* glsl */ `
precision highp float;
attribute vec3 aBlob;
attribute vec3 aDestino;
attribute float aAzar;
uniform mat4 uProyeccion;
uniform mat4 uModeloVista;
uniform float uTiempo;
uniform float uMezcla;
uniform float uTamPx;
varying float vLuz;
varying float vAlfa;
${RUIDO}

void main() {
  float t = uTiempo * 0.22;
  vec3 q = aBlob * 1.15;
  vec3 d = vec3(snoise(q + vec3(t, 0.0, 0.0)), snoise(q + vec3(0.0, t + 17.1, 0.0)), snoise(q + vec3(0.0, 0.0, t + 31.7)));
  float pulso = snoise(aBlob * 0.7 + vec3(t * 0.6));
  vec3 masa = aBlob + d * 0.62 + normalize(aBlob + 1e-5) * pulso * 0.42;
  float m = clamp(uMezcla * 1.65 - aAzar * 0.65, 0.0, 1.0);
  m = m * m * (3.0 - 2.0 * m);
  vec3 pos = mix(masa * 0.8, aDestino + d * 0.03, m);
  vec4 mv = uModeloVista * vec4(pos, 1.0);
  gl_Position = uProyeccion * mv;
  gl_PointSize = uTamPx * (0.55 + aAzar * 0.9) / (-mv.z);
  float borde = smoothstep(0.55, 1.75, length(masa));
  vLuz = mix(borde * borde, 0.92, m);
  vAlfa = mix(0.55 + borde * 0.4, 0.85, m);
}
`;

export const FRAGMENTO_RESPALDO = /* glsl */ `
precision mediump float;
varying float vLuz;
varying float vAlfa;

void main() {
  vec2 c = gl_PointCoord - 0.5;
  float r = length(c);
  if (r > 0.5) discard;
  float a = smoothstep(0.5, 0.05, r);
  gl_FragColor = vec4(mix(vec3(0.012, 0.011, 0.02), vec3(0.80, 0.82, 0.90), vLuz) * a * vAlfa, a * vAlfa);
}
`;
