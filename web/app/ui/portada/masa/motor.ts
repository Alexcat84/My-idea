/**
 * Motor de la masa con three.js (niveles alto, medio y bajo).
 *
 * Por fotograma:
 *  1. el liquido se calcula por raymarching en un render target a
 *     resolucion reducida (AJUSTES[nivel].escalaLiquido);
 *  2. la escena principal compone fondo + liquido escalado y encima las
 *     particulas (quads instanciados con estela) a resolucion completa;
 *  3. postprocesado: bloom suave (alto y medio) y acabado con vinieta y
 *     grano que no levantan el negro.
 *
 * No toca el DOM: recibe el lienzo (HTMLCanvasElement u OffscreenCanvas) y
 * el tamano, asi corre igual en un worker (masa/trabajador.ts, lo normal)
 * que en el hilo principal (masa/anfitrion.ts, cuando no hay
 * OffscreenCanvas con WebGL2). three.js nunca entra en el bundle inicial.
 */
import {
  Group,
  HalfFloatType,
  InstancedBufferAttribute,
  InstancedBufferGeometry,
  BufferAttribute,
  LinearFilter,
  LinearSRGBColorSpace,
  Matrix3,
  Mesh,
  NoBlending,
  NoToneMapping,
  OrthographicCamera,
  PerspectiveCamera,
  PlaneGeometry,
  Scene,
  ShaderMaterial,
  UnsignedByteType,
  Vector2,
  Vector3,
  WebGLRenderTarget,
  WebGLRenderer,
  type IUniform,
} from "three";
import { EffectComposer } from "three/examples/jsm/postprocessing/EffectComposer.js";
import { RenderPass } from "three/examples/jsm/postprocessing/RenderPass.js";
import { ShaderPass } from "three/examples/jsm/postprocessing/ShaderPass.js";
import { UnrealBloomPass } from "three/examples/jsm/postprocessing/UnrealBloomPass.js";
import { AJUSTES, MedidorFps, type NivelLiquido } from "./calidad";
import { estadoEn, figuraEn, MOMENTOS } from "./ciclo";
import type { Aviso, ControlMotor, OpcionesMotor } from "./control";
import { distanciaCamara, FOV_GRADOS, RADIO_MASA } from "./encuadre";
import { azarSembrado, muestrearTodas } from "./figuras";
import {
  FRAGMENTO_ACABADO,
  FRAGMENTO_COMPOSICION,
  FRAGMENTO_PARTICULAS,
  fragmentoLiquido,
  UNIFORMES_ACABADO,
  UNIFORMES_COMPOSICION,
  UNIFORMES_LIQUIDO,
  UNIFORMES_PARTICULAS,
  VERTICE_PANTALLA,
  verticeParticulas,
} from "./glsl";

type Uniformes<L extends readonly string[]> = Record<L[number], IUniform>;

/** Segundos hacia atras de donde nace la estela de cada particula. */
const ESTELA = 0.045;
/** Radio del grano (px de dispositivo) como fraccion del lado menor. */
const GRANO_RELATIVO = 0.0021;

const VERTICE_PASADA = /* glsl */ `
varying vec2 vUv;
void main() {
  vUv = uv;
  gl_Position = projectionMatrix * modelViewMatrix * vec4(position, 1.0);
}
`;

/** Direcciones repartidas por igual sobre la esfera (espiral de Fibonacci). */
function direccionesFibonacci(n: number): Float32Array {
  const salida = new Float32Array(n * 3);
  const oro = Math.PI * (3 - Math.sqrt(5));
  for (let i = 0; i < n; i++) {
    const y = 1 - (2 * (i + 0.5)) / n;
    const r = Math.sqrt(1 - y * y);
    const ang = i * oro;
    salida[i * 3] = Math.cos(ang) * r;
    salida[i * 3 + 1] = y;
    salida[i * 3 + 2] = Math.sin(ang) * r;
  }
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

  /* ---------- 1. liquido ---------- */
  const uLiquido: Uniformes<typeof UNIFORMES_LIQUIDO> = {
    uTiempo: { value: 0 },
    uLiquido: { value: 1 },
    uRadio: { value: RADIO_MASA },
    uAspecto: { value: 1 },
    uTanMedio: { value: Math.tan((FOV_GRADOS * Math.PI) / 360) },
    uCamZ: { value: 10 },
    uRotInv: { value: new Matrix3() },
    uPixelMundo: { value: 0.001 },
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

  /* ---------- 2. escena principal: composicion + particulas ---------- */
  const escena = new Scene();
  const camara = new PerspectiveCamera(FOV_GRADOS, 1, 0.1, 100);

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
  planoComposicion.renderOrder = 0;
  escena.add(planoComposicion);

  const n = ajustes.particulas;
  const azar = azarSembrado(7);
  const azares = new Float32Array(n * 2);
  for (let i = 0; i < n * 2; i++) azares[i] = azar();
  const direcciones = direccionesFibonacci(n);
  const destino = new InstancedBufferAttribute(new Float32Array(n * 3), 3);
  for (let i = 0; i < n * 3; i++) destino.array[i] = direcciones[i] * RADIO_MASA;

  const geoParticulas = new InstancedBufferGeometry();
  // position.x: 0 en la cola, 1 en la cabeza; position.y: lado de la estela.
  geoParticulas.setAttribute("position", new BufferAttribute(new Float32Array([0, -1, 0, 1, -1, 0, 0, 1, 0, 1, 1, 0]), 3));
  geoParticulas.setIndex([0, 1, 2, 2, 1, 3]);
  geoParticulas.setAttribute("aDir", new InstancedBufferAttribute(direcciones, 3));
  geoParticulas.setAttribute("aDestino", destino);
  geoParticulas.setAttribute("aAzar", new InstancedBufferAttribute(azares, 2));
  geoParticulas.instanceCount = n;

  const uParticulas: Uniformes<typeof UNIFORMES_PARTICULAS> = {
    uTiempo: { value: 0 },
    uTiempoPrevio: { value: 0 },
    uMezcla: { value: 0 },
    uMezclaPrevia: { value: 0 },
    uLiquido: { value: 1 },
    uLiquidoPrevio: { value: 1 },
    uRadio: { value: RADIO_MASA },
    uVis: { value: 1 },
    uTamPx: { value: 2 },
    uLienzo: { value: new Vector2(1, 1) },
    uCamara: { value: new Vector3(0, 0, 10) },
  };
  const materialParticulas = new ShaderMaterial({
    vertexShader: verticeParticulas(ajustes.pasosRizo),
    fragmentShader: FRAGMENTO_PARTICULAS,
    uniforms: uParticulas,
    transparent: true,
    depthTest: false,
    depthWrite: false,
  });
  const particulas = new Mesh(geoParticulas, materialParticulas);
  particulas.frustumCulled = false;
  particulas.renderOrder = 1;
  const nube = new Group();
  nube.add(particulas);
  escena.add(nube);

  /* ---------- 3. postprocesado ---------- */
  const composer = new EffectComposer(renderer, new WebGLRenderTarget(1, 1, { type: tipoRt, depthBuffer: false }));
  composer.addPass(new RenderPass(escena, camara));
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
    const d = distanciaCamara(ancho, alto);
    camara.aspect = ancho / alto;
    camara.position.set(0, 0, d);
    camara.updateProjectionMatrix();
    uLiquido.uAspecto.value = ancho / alto;
    uLiquido.uCamZ.value = d;
    uComposicion.uTexelLiquido.value = new Vector2(1 / rtLiquido.width, 1 / rtLiquido.height);
    uLiquido.uPixelMundo.value = (2 * uLiquido.uTanMedio.value) / rtLiquido.height;
    const lienzoPx = new Vector2(ancho * dpr, alto * dpr);
    uComposicion.uLienzo.value = lienzoPx;
    uParticulas.uLienzo.value = lienzoPx;
    acabado.uniforms.uLienzo.value = lienzoPx;
    uParticulas.uCamara.value = camara.position.clone();
    uParticulas.uTamPx.value = Math.max(GRANO_RELATIVO * Math.min(ancho, alto) * dpr, 0.9 * dpr);
  };
  ajustar();

  /* ---------- figuras ---------- */
  const figuras: Array<Float32Array | null> = [null, null, null, null, null];
  let figuraCargada = -1;
  let destruido = false;
  const ponerFigura = (indice: number) => {
    const puntos = figuras[indice];
    if (!puntos || indice === figuraCargada) return;
    (destino.array as Float32Array).set(puntos);
    destino.needsUpdate = true;
    figuraCargada = indice;
  };
  // El medidor espera a que esten las cinco figuras: su muestreo corre en
  // el mismo hilo y no es del costo del nivel que se esta midiendo.
  let figurasListas = false;
  void muestrearTodas(n, (i, puntos) => {
    figuras[i] = puntos;
  }, () => destruido).then(() => {
    figurasListas = true;
  });

  /* ---------- puntero: leve paralaje ---------- */
  const puntero = { x: 0, y: 0, sx: 0, sy: 0 };

  /* ---------- pintar un instante ---------- */
  const rotInv = new Matrix3();
  const pintar = (t: number) => {
    const e = estadoEn(t);
    const previo = estadoEn(t - ESTELA);
    ponerFigura(figuraEn(t));
    puntero.sx += (puntero.x - puntero.sx) * 0.05;
    puntero.sy += (puntero.y - puntero.sy) * 0.05;
    const libre = 1 - e.mezcla;
    nube.rotation.set(
      Math.cos(t * 0.13) * 0.3 * libre + puntero.sy * 0.18,
      Math.sin(t * 0.17) * 0.8 * libre + puntero.sx * 0.25,
      Math.sin(t * 0.09) * 0.2 * libre,
    );
    nube.updateMatrixWorld();
    rotInv.setFromMatrix4(nube.matrixWorld).transpose();
    uLiquido.uRotInv.value = rotInv;
    uLiquido.uTiempo.value = t;
    uLiquido.uLiquido.value = e.liquido;
    uParticulas.uTiempo.value = t;
    uParticulas.uTiempoPrevio.value = t - ESTELA;
    uParticulas.uMezcla.value = e.mezcla;
    uParticulas.uMezclaPrevia.value = previo.mezcla;
    uParticulas.uLiquido.value = e.liquido;
    uParticulas.uLiquidoPrevio.value = previo.liquido;
    acabado.uniforms.uTiempo.value = t;

    renderer.setRenderTarget(rtLiquido);
    renderer.clear();
    if (e.liquido > 0.004) renderer.render(escenaLiquido, camaraPlano);
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
    geoParticulas.dispose();
    materialLiquido.dispose();
    materialComposicion.dispose();
    materialParticulas.dispose();
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

  /* ---------- compilar sin bloquear el hilo principal ---------- */
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
    await renderer.compileAsync(escena, camara);
    await renderer.compileAsync(escenaPasadas, camaraPlano);
    renderer.setRenderTarget(rtLiquido);
    renderer.render(escenaLiquido, camaraPlano);
    renderer.setRenderTarget(null);
    await esperarGpu();
    if (!destruido) renderer.render(escena, camara);
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
