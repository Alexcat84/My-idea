/**
 * Motor de la masa con three.js (niveles alto, medio y bajo).
 *
 * Una sola materia: la masa liquida y las figuras son la misma superficie.
 * El shader interpola entre la piel de la masa y el campo de distancia de
 * la figura del ciclo (uMorf), asi el liquido fluye, se estira y se vuelve
 * foco, lente, brujula, escalera o casa, y despues regresa a masa.
 *
 * Por fotograma:
 *  1. la materia se calcula por raymarching en un render target a
 *     resolucion reducida (AJUSTES[nivel].escalaLiquido);
 *  2. se compone sobre el fondo del hero;
 *  3. postprocesado: bloom suave (alto y medio) y acabado con vinieta y
 *     grano que no levantan el negro.
 *
 * No toca el DOM: recibe el lienzo (HTMLCanvasElement u OffscreenCanvas) y
 * el tamano, asi corre igual en un worker (masa/trabajador.ts, lo normal)
 * que en el hilo principal (masa/anfitrion.ts, cuando no hay
 * OffscreenCanvas con WebGL2). three.js nunca entra en el bundle inicial.
 */
import {
  ClampToEdgeWrapping,
  DataTexture,
  DataUtils,
  Euler,
  HalfFloatType,
  LinearFilter,
  LinearSRGBColorSpace,
  Matrix3,
  Matrix4,
  Mesh,
  NoBlending,
  NoToneMapping,
  OrthographicCamera,
  PlaneGeometry,
  RedFormat,
  Scene,
  ShaderMaterial,
  UnsignedByteType,
  Vector2,
  WebGLRenderTarget,
  WebGLRenderer,
  type IUniform,
} from "three";
import { EffectComposer } from "three/examples/jsm/postprocessing/EffectComposer.js";
import { RenderPass } from "three/examples/jsm/postprocessing/RenderPass.js";
import { ShaderPass } from "three/examples/jsm/postprocessing/ShaderPass.js";
import { UnrealBloomPass } from "three/examples/jsm/postprocessing/UnrealBloomPass.js";
import { AJUSTES, MedidorFps, type NivelLiquido } from "./calidad";
import { estadoEn, figuraEn, giroEn, MOMENTOS } from "./ciclo";
import type { Aviso, ControlMotor, OpcionesMotor } from "./control";
import { distanciaCamara, FOV_GRADOS, RADIO_MASA } from "./encuadre";
import { calcularCampos, LADO_CAMPO } from "./figuras";
import {
  FRAGMENTO_ACABADO,
  FRAGMENTO_COMPOSICION,
  fragmentoLiquido,
  UNIFORMES_ACABADO,
  UNIFORMES_COMPOSICION,
  UNIFORMES_LIQUIDO,
  VELOCIDAD_MATERIA,
  VERTICE_PANTALLA,
} from "./glsl";

type Uniformes<L extends readonly string[]> = Record<L[number], IUniform>;

const VERTICE_PASADA = /* glsl */ `
varying vec2 vUv;
void main() {
  vUv = uv;
  gl_Position = projectionMatrix * modelViewMatrix * vec4(position, 1.0);
}
`;

/** Campo en media precision: se filtra linealmente en todo WebGL2. */
function aMediaPrecision(campo: Float32Array): Uint16Array {
  const salida = new Uint16Array(campo.length);
  for (let i = 0; i < campo.length; i++) salida[i] = DataUtils.toHalfFloat(campo[i]);
  return salida;
}

export async function montarMotor(nivel: NivelLiquido, o: OpcionesMotor): Promise<ControlMotor> {
  const ajustes = AJUSTES[nivel];
  const lienzo = o.lienzo;
  let fallo = false;
  const renderer = new WebGLRenderer({
    canvas: lienzo,
    context: o.contexto,
    antialias: false,
    alpha: false,
    depth: false,
    stencil: false,
    powerPreference: "high-performance",
  });
  renderer.outputColorSpace = LinearSRGBColorSpace;
  renderer.toneMapping = NoToneMapping;
  renderer.setClearColor(0x000000, 1);
  renderer.debug.onShaderError = (gl, _programa, vertice, fragmento) => {
    fallo = true;
    console.error(
      "[portada] un shader no compila:\n",
      gl.getShaderInfoLog(vertice) ?? "",
      gl.getShaderInfoLog(fragmento) ?? "",
    );
  };

  const flotante =
    renderer.extensions.has("EXT_color_buffer_float") || renderer.extensions.has("EXT_color_buffer_half_float");
  const tipoRt = flotante ? HalfFloatType : UnsignedByteType;

  /* ---------- la figura: su campo de distancia en una textura ---------- */
  const campo = new DataTexture(
    new Uint16Array(LADO_CAMPO * LADO_CAMPO).fill(DataUtils.toHalfFloat(10)),
    LADO_CAMPO,
    LADO_CAMPO,
    RedFormat,
    HalfFloatType,
  );
  campo.minFilter = LinearFilter;
  campo.magFilter = LinearFilter;
  campo.wrapS = ClampToEdgeWrapping;
  campo.wrapT = ClampToEdgeWrapping;
  campo.needsUpdate = true;

  /* ---------- 1. la materia ---------- */
  const uLiquido: Uniformes<typeof UNIFORMES_LIQUIDO> = {
    uTiempo: { value: 0 },
    uMorf: { value: 0 },
    uRadio: { value: RADIO_MASA },
    uAspecto: { value: 1 },
    uTanMedio: { value: Math.tan((FOV_GRADOS * Math.PI) / 360) },
    uCamZ: { value: 10 },
    uRotInv: { value: new Matrix3() },
    uPixelMundo: { value: 0.001 },
    uFigura: { value: campo },
  };
  const materialLiquido = new ShaderMaterial({
    vertexShader: VERTICE_PANTALLA,
    fragmentShader: fragmentoLiquido(ajustes),
    uniforms: uLiquido,
    depthTest: false,
    depthWrite: false,
    blending: NoBlending,
  });
  const planoGeo = new PlaneGeometry(2, 2);
  const planoLiquido = new Mesh(planoGeo, materialLiquido);
  planoLiquido.frustumCulled = false;
  const escenaLiquido = new Scene();
  escenaLiquido.add(planoLiquido);
  const camaraPlano = new OrthographicCamera(-1, 1, 1, -1, 0, 1);
  const rtLiquido = new WebGLRenderTarget(1, 1, {
    type: tipoRt,
    depthBuffer: false,
    minFilter: LinearFilter,
    magFilter: LinearFilter,
  });

  /* ---------- 2. composicion sobre el fondo del hero ---------- */
  const escena = new Scene();
  const uComposicion: Uniformes<typeof UNIFORMES_COMPOSICION> = {
    uLiquidoTex: { value: rtLiquido.texture },
    uTexelLiquido: { value: new Vector2(1, 1) },
    uLienzo: { value: new Vector2(1, 1) },
  };
  const materialComposicion = new ShaderMaterial({
    vertexShader: VERTICE_PANTALLA,
    fragmentShader: FRAGMENTO_COMPOSICION,
    uniforms: uComposicion,
    depthTest: false,
    depthWrite: false,
    blending: NoBlending,
  });
  const planoComposicion = new Mesh(planoGeo, materialComposicion);
  planoComposicion.frustumCulled = false;
  escena.add(planoComposicion);

  /* ---------- 3. postprocesado ---------- */
  const composer = new EffectComposer(renderer, new WebGLRenderTarget(1, 1, { type: tipoRt, depthBuffer: false }));
  composer.addPass(new RenderPass(escena, camaraPlano));
  const bloom = ajustes.bloom ? new UnrealBloomPass(new Vector2(256, 256), 0.38, 0.45, 0.62) : null;
  if (bloom) composer.addPass(bloom);
  const uAcabado: Uniformes<typeof UNIFORMES_ACABADO> = {
    tDiffuse: { value: null },
    uTiempo: { value: 0 },
    uLienzo: { value: new Vector2(1, 1) },
    uGrano: { value: 0.045 },
    uVineta: { value: 0.35 },
  };
  const acabado = new ShaderPass({ uniforms: uAcabado, vertexShader: VERTICE_PASADA, fragmentShader: FRAGMENTO_ACABADO });
  composer.addPass(acabado);

  /* ---------- tamano y encuadre ---------- */
  const tamano = { ancho: o.ancho, alto: o.alto, dpr: o.dpr };
  const ajustar = () => {
    const ancho = Math.max(1, tamano.ancho);
    const alto = Math.max(1, tamano.alto);
    const dpr = Math.min(tamano.dpr || 1, ajustes.dprMaximo);
    renderer.setPixelRatio(dpr);
    renderer.setSize(ancho, alto, false);
    composer.setPixelRatio(dpr);
    composer.setSize(ancho, alto);
    rtLiquido.setSize(
      Math.max(1, Math.round(ancho * dpr * ajustes.escalaLiquido)),
      Math.max(1, Math.round(alto * dpr * ajustes.escalaLiquido)),
    );
    uLiquido.uAspecto.value = ancho / alto;
    uLiquido.uCamZ.value = distanciaCamara(ancho, alto);
    uLiquido.uPixelMundo.value = (2 * uLiquido.uTanMedio.value) / rtLiquido.height;
    uComposicion.uTexelLiquido.value = new Vector2(1 / rtLiquido.width, 1 / rtLiquido.height);
    const lienzoPx = new Vector2(ancho * dpr, alto * dpr);
    uComposicion.uLienzo.value = lienzoPx;
    acabado.uniforms.uLienzo.value = lienzoPx;
  };
  ajustar();

  /* ---------- figuras ---------- */
  const figuras: Array<Uint16Array | null> = [null, null, null, null, null];
  let figuraCargada = -1;
  let destruido = false;
  const ponerFigura = (indice: number) => {
    const datos = figuras[indice];
    if (!datos || indice === figuraCargada) return;
    (campo.image.data as Uint16Array).set(datos);
    campo.needsUpdate = true;
    figuraCargada = indice;
  };
  // El medidor espera a que esten los cinco campos: se calculan en el mismo
  // hilo y no son del costo del nivel que se esta midiendo.
  let figurasListas = false;
  const camposListos = calcularCampos((i, c) => {
    figuras[i] = aMediaPrecision(c);
  }, () => destruido).then(() => {
    figurasListas = true;
  });

  /* ---------- puntero: leve paralaje ---------- */
  const puntero = { x: 0, y: 0, sx: 0, sy: 0 };

  /* ---------- pintar un instante ---------- */
  const giro = new Euler();
  const matrizGiro = new Matrix4();
  const rotInv = new Matrix3();
  const pintar = (t: number) => {
    const e = estadoEn(t);
    ponerFigura(figuraEn(t));
    puntero.sx += (puntero.x - puntero.sx) * 0.05;
    puntero.sy += (puntero.y - puntero.sy) * 0.05;
    // La masa da una vuelta completa por ciclo y se balancea; la vuelta
    // cierra justo al transformarse, asi la figura formada mira de frente.
    const libre = 1 - e.mezcla;
    const tg = t * VELOCIDAD_MATERIA;
    giro.set(
      Math.cos(tg * 0.3) * 0.32 * libre + puntero.sy * 0.18,
      giroEn(t) + Math.sin(tg * 0.37) * 0.25 * libre + puntero.sx * 0.25,
      Math.sin(tg * 0.23) * 0.22 * libre,
    );
    matrizGiro.makeRotationFromEuler(giro);
    rotInv.setFromMatrix4(matrizGiro).transpose();
    uLiquido.uRotInv.value = rotInv;
    uLiquido.uTiempo.value = t;
    uLiquido.uMorf.value = e.mezcla;
    acabado.uniforms.uTiempo.value = t;

    renderer.setRenderTarget(rtLiquido);
    renderer.render(escenaLiquido, camaraPlano);
    renderer.setRenderTarget(null);
    composer.render();
  };

  /* ---------- estado del bucle ---------- */
  let tiempoCiclo = o.tiempoFijo ?? o.tiempoInicial;
  let raf = 0;
  let pausado = false;
  let ultimo = 0;
  let avisado = false;
  let primerFotograma = false;
  const medidor = new MedidorFps(ajustes.fpsMinimo);

  const avisar = (aviso: Aviso, fps: number) => {
    if (avisado || destruido) return;
    avisado = true;
    o.alAviso(aviso, fps, tiempoCiclo);
  };
  const alPerderContexto = (ev: Event) => {
    ev.preventDefault();
    avisar("fallo", 0);
  };
  const eventos = lienzo as EventTarget;
  eventos.addEventListener("webglcontextlost", alPerderContexto);

  const liberar = () => {
    destruido = true;
    cancelAnimationFrame(raf);
    eventos.removeEventListener("webglcontextlost", alPerderContexto);
    planoGeo.dispose();
    materialLiquido.dispose();
    materialComposicion.dispose();
    campo.dispose();
    rtLiquido.dispose();
    bloom?.dispose();
    acabado.dispose();
    composer.dispose();
    renderer.dispose();
    renderer.forceContextLoss();
  };

  const mostrar = () => {
    if (primerFotograma) return;
    primerFotograma = true;
    o.alPrimerFotograma();
  };
  let cuadros = 0;

  const cuadro = (ahora: number) => {
    if (pausado || destruido) return;
    raf = requestAnimationFrame(cuadro);
    const dt = ultimo ? ahora - ultimo : 16.7;
    ultimo = ahora;
    if (o.tiempoFijo === null) tiempoCiclo += Math.min(dt, 100) / 1000;
    pintar(tiempoCiclo);
    mostrar();
    if (fallo) {
      avisar("fallo", 0);
      return;
    }
    if (o.adaptativo && figurasListas && medidor.registrar(dt) === "no-sostiene") avisar("no-sostiene", medidor.fpsMediana());
    const fps = medidor.fpsMediana();
    if (fps > 0 && ++cuadros % 30 === 0) o.alFps(fps, tiempoCiclo);
  };

  function pintarQuieto() {
    pintar(o.tiempoFijo ?? MOMENTOS.reposo);
    mostrar();
    if (fallo) avisar("fallo", 0);
  }

  /* ---------- compilar sin bloquear el hilo ---------- */
  // compileAsync usa KHR_parallel_shader_compile, pero en ANGLE/D3D el
  // trabajo pesado del shader termina en el primer dibujo, y la consulta
  // sincrona que three hace al primer uso del programa SIGUIENTE espera a
  // la GPU (medido: 0.5 a 1.1 s de hilo bloqueado). Por eso: se precompila
  // todo (tambien las pasadas del postprocesado), y el primer dibujo de cada
  // grupo se hace con el lienzo aun invisible, esperando entre uno y otro a
  // una valla de GPU que se consulta sin bloquear.
  const contextoGl = renderer.getContext();
  const esperarGpu = () =>
    new Promise<void>((listo) => {
      if (!(contextoGl instanceof WebGL2RenderingContext)) return listo();
      const valla = contextoGl.fenceSync(contextoGl.SYNC_GPU_COMMANDS_COMPLETE, 0);
      contextoGl.flush();
      const mirar = () => {
        if (!valla || destruido || contextoGl.getSyncParameter(valla, contextoGl.SYNC_STATUS) === contextoGl.SIGNALED) {
          if (valla) contextoGl.deleteSync(valla);
          listo();
        } else {
          setTimeout(mirar, 16);
        }
      };
      setTimeout(mirar, 16);
    });
  const escenaPasadas = new Scene();
  const materialesPasadas = [acabado.material];
  if (bloom) {
    materialesPasadas.push(bloom.materialHighPassFilter, ...bloom.separableBlurMaterials, bloom.compositeMaterial, bloom.blendMaterial);
  }
  for (const m of materialesPasadas) {
    const quad = new Mesh(planoGeo, m);
    quad.frustumCulled = false;
    escenaPasadas.add(quad);
  }
  try {
    await renderer.compileAsync(escenaLiquido, camaraPlano);
    await renderer.compileAsync(escena, camaraPlano);
    await renderer.compileAsync(escenaPasadas, camaraPlano);
    // Con movimiento reducido, o con el ciclo congelado en una figura, esa
    // figura tiene que estar lista antes del primer fotograma.
    if (o.reducido || o.tiempoFijo !== null) await camposListos;
    renderer.setRenderTarget(rtLiquido);
    renderer.render(escenaLiquido, camaraPlano);
    renderer.setRenderTarget(null);
    await esperarGpu();
    if (!destruido) renderer.render(escena, camaraPlano);
    await esperarGpu();
    if (!destruido) composer.render();
    await esperarGpu();
    if (destruido) throw new Error("destruido");
  } catch (error) {
    liberar();
    throw error;
  }
  if (fallo) {
    liberar();
    throw new Error("shader");
  }

  if (o.reducido) {
    pintarQuieto();
  } else {
    raf = requestAnimationFrame(cuadro);
  }

  return {
    pausar() {
      if (pausado || o.reducido) return;
      pausado = true;
      cancelAnimationFrame(raf);
    },
    reanudar() {
      if (!pausado || destruido) return;
      pausado = false;
      ultimo = 0;
      raf = requestAnimationFrame(cuadro);
    },
    destruir() {
      if (!destruido) liberar();
    },
    tiempo: () => tiempoCiclo,
    redimensionar(ancho, alto, dpr) {
      if (destruido) return;
      tamano.ancho = ancho;
      tamano.alto = alto;
      tamano.dpr = dpr;
      ajustar();
      if (o.reducido && primerFotograma) pintarQuieto();
    },
    puntero(x, y) {
      puntero.x = x;
      puntero.y = y;
    },
  };
}
