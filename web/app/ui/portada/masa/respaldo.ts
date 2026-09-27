/**
 * Respaldo para equipos debiles: solo particulas (la muestra
 * particula-my-idea.html), en WebGL1 crudo y sin three.js, para que un
 * equipo que no sostiene el liquido tampoco pague la descarga de three.js.
 * Mismo ciclo, mismas figuras y mismo encuadre que el motor principal.
 */
import { FPS_MINIMO_PARTICULAS, MedidorFps, PARTICULAS_RESPALDO } from "./calidad";
import { estadoEn, figuraEn, MOMENTOS } from "./ciclo";
import type { ControlMasa, OpcionesMontaje } from "./control";
import { distanciaCamara, FOV_GRADOS } from "./encuadre";
import { azarSembrado, muestrearTodas } from "./figuras";
import { FRAGMENTO_RESPALDO, UNIFORMES_RESPALDO, VERTICE_RESPALDO } from "./glsl";

type Mat4 = Float32Array;

function perspectiva(fovGrados: number, aspecto: number, cerca: number, lejos: number): Mat4 {
  const f = 1 / Math.tan((fovGrados * Math.PI) / 360);
  const m = new Float32Array(16);
  m[0] = f / aspecto;
  m[5] = f;
  m[10] = (lejos + cerca) / (cerca - lejos);
  m[11] = -1;
  m[14] = (2 * lejos * cerca) / (cerca - lejos);
  return m;
}

/** Camara en z = d mirando al origen, por la rotacion de Euler 'XYZ' de three.js. */
function modeloVista(rx: number, ry: number, rz: number, d: number): Mat4 {
  const [cx, sx, cy, sy, cz, sz] = [Math.cos(rx), Math.sin(rx), Math.cos(ry), Math.sin(ry), Math.cos(rz), Math.sin(rz)];
  // R = Rx * Ry * Rz (mismo orden de Euler 'XYZ' que three.js)
  const r00 = cy * cz, r01 = -cy * sz, r02 = sy;
  const r10 = cx * sz + sx * sy * cz, r11 = cx * cz - sx * sy * sz, r12 = -sx * cy;
  const r20 = sx * sz - cx * sy * cz, r21 = sx * cz + cx * sy * sz, r22 = cx * cy;
  // columna mayor
  return new Float32Array([r00, r10, r20, 0, r01, r11, r21, 0, r02, r12, r22, 0, 0, 0, -d, 1]);
}

function compilar(gl: WebGLRenderingContext, tipo: number, fuente: string): WebGLShader {
  const s = gl.createShader(tipo);
  if (!s) throw new Error("shader");
  gl.shaderSource(s, fuente);
  gl.compileShader(s);
  if (!gl.getShaderParameter(s, gl.COMPILE_STATUS)) {
    const registro = gl.getShaderInfoLog(s) ?? "";
    console.error("[portada] el shader del respaldo no compila:\n", registro);
    throw new Error("shader");
  }
  return s;
}

export async function montarRespaldo(o: OpcionesMontaje): Promise<ControlMasa> {
  const lienzo = document.createElement("canvas");
  lienzo.className = "portada-masa-lienzo";
  lienzo.setAttribute("aria-hidden", "true");
  const gl = lienzo.getContext("webgl", { alpha: true, antialias: false, premultipliedAlpha: true });
  if (!gl) throw new Error("webgl");
  o.contenedor.appendChild(lienzo);

  let programa: WebGLProgram;
  try {
    const p = gl.createProgram();
    if (!p) throw new Error("programa");
    gl.attachShader(p, compilar(gl, gl.VERTEX_SHADER, VERTICE_RESPALDO));
    gl.attachShader(p, compilar(gl, gl.FRAGMENT_SHADER, FRAGMENTO_RESPALDO));
    gl.linkProgram(p);
    if (!gl.getProgramParameter(p, gl.LINK_STATUS)) {
      console.error("[portada] el programa del respaldo no enlaza:\n", gl.getProgramInfoLog(p) ?? "");
      throw new Error("programa");
    }
    programa = p;
  } catch (error) {
    lienzo.remove();
    throw error;
  }
  gl.useProgram(programa);

  const ubicaciones = {} as Record<(typeof UNIFORMES_RESPALDO)[number], WebGLUniformLocation | null>;
  for (const nombre of UNIFORMES_RESPALDO) ubicaciones[nombre] = gl.getUniformLocation(programa, nombre);

  const movil = Math.min(window.innerWidth, window.innerHeight) < 700;
  const n = movil ? PARTICULAS_RESPALDO.movil : PARTICULAS_RESPALDO.escritorio;
  const azar = azarSembrado(11);
  const blob = new Float32Array(n * 3);
  const azares = new Float32Array(n);
  for (let i = 0; i < n; i++) {
    const th = 2 * Math.PI * azar();
    const ph = Math.acos(2 * azar() - 1);
    const r = 1.25 * Math.pow(azar(), 0.42);
    blob[i * 3] = r * Math.sin(ph) * Math.cos(th);
    blob[i * 3 + 1] = r * Math.sin(ph) * Math.sin(th);
    blob[i * 3 + 2] = r * Math.cos(ph);
    azares[i] = azar();
  }
  const destino = new Float32Array(blob);

  const buffers: WebGLBuffer[] = [];
  const atributo = (nombre: string, datos: Float32Array, tam: number, dinamico = false): WebGLBuffer | null => {
    const loc = gl.getAttribLocation(programa, nombre);
    const b = gl.createBuffer();
    if (!b || loc < 0) return null;
    buffers.push(b);
    gl.bindBuffer(gl.ARRAY_BUFFER, b);
    gl.bufferData(gl.ARRAY_BUFFER, datos, dinamico ? gl.DYNAMIC_DRAW : gl.STATIC_DRAW);
    gl.enableVertexAttribArray(loc);
    gl.vertexAttribPointer(loc, tam, gl.FLOAT, false, 0, 0);
    return b;
  };
  atributo("aBlob", blob, 3);
  atributo("aAzar", azares, 1);
  const bufferDestino = atributo("aDestino", destino, 3, true);

  gl.enable(gl.BLEND);
  gl.blendFunc(gl.ONE, gl.ONE_MINUS_SRC_ALPHA);
  gl.clearColor(0, 0, 0, 0);

  const figuras: Array<Float32Array | null> = [null, null, null, null, null];
  let figuraCargada = -1;
  let destruido = false;
  // El medidor espera a que esten las cinco figuras: su muestreo corre en
  // el hilo principal y no es del costo del nivel que se esta midiendo.
  let figurasListas = false;
  void muestrearTodas(n, (i, puntos) => {
    figuras[i] = puntos;
  }, () => destruido).then(() => {
    figurasListas = true;
  });

  let distancia = 10;
  let ancho = 1;
  let alto = 1;
  const ajustar = () => {
    ancho = Math.max(1, o.contenedor.clientWidth);
    alto = Math.max(1, o.contenedor.clientHeight);
    const dpr = Math.min(window.devicePixelRatio || 1, movil ? 1.5 : 2);
    lienzo.width = Math.round(ancho * dpr);
    lienzo.height = Math.round(alto * dpr);
    gl.viewport(0, 0, lienzo.width, lienzo.height);
    distancia = distanciaCamara(ancho, alto);
    gl.uniformMatrix4fv(ubicaciones.uProyeccion, false, perspectiva(FOV_GRADOS, ancho / alto, 0.1, 100));
    // Tamano de punto: fraccion del lado menor, escalado por la distancia.
    gl.uniform1f(ubicaciones.uTamPx, Math.max(0.0055 * Math.min(ancho, alto) * dpr, 1.6 * dpr) * distancia);
  };
  ajustar();

  const pintar = (t: number) => {
    const indice = figuraEn(t);
    const puntos = figuras[indice];
    if (puntos && indice !== figuraCargada && bufferDestino) {
      gl.bindBuffer(gl.ARRAY_BUFFER, bufferDestino);
      gl.bufferSubData(gl.ARRAY_BUFFER, 0, puntos);
      figuraCargada = indice;
    }
    const e = estadoEn(t);
    const libre = 1 - e.mezcla;
    gl.uniformMatrix4fv(
      ubicaciones.uModeloVista,
      false,
      modeloVista(Math.cos(t * 0.13) * 0.35 * libre, Math.sin(t * 0.17) * 0.9 * libre, Math.sin(t * 0.09) * 0.2 * libre, distancia),
    );
    gl.uniform1f(ubicaciones.uTiempo, t);
    gl.uniform1f(ubicaciones.uMezcla, e.mezcla);
    gl.clear(gl.COLOR_BUFFER_BIT);
    gl.drawArrays(gl.POINTS, 0, n);
  };

  let tiempoCiclo = o.tiempoFijo ?? o.tiempoInicial;
  let raf = 0;
  let pausado = false;
  let ultimo = 0;
  let avisado = false;
  let visible = false;
  const medidor = new MedidorFps(FPS_MINIMO_PARTICULAS);
  const mostrar = () => {
    if (visible) return;
    visible = true;
    lienzo.style.opacity = "1";
    o.alPrimerFotograma();
  };
  const avisar = (aviso: "no-sostiene" | "fallo", fps: number) => {
    if (avisado || destruido) return;
    avisado = true;
    o.alAviso(aviso, fps);
  };

  const cuadro = (ahora: number) => {
    if (pausado || destruido) return;
    raf = requestAnimationFrame(cuadro);
    const dt = ultimo ? ahora - ultimo : 16.7;
    ultimo = ahora;
    if (o.tiempoFijo === null) tiempoCiclo += Math.min(dt, 100) / 1000;
    pintar(tiempoCiclo);
    mostrar();
    if (o.adaptativo && figurasListas && medidor.registrar(dt) === "no-sostiene") avisar("no-sostiene", medidor.fpsMediana());
    const fps = medidor.fpsMediana();
    if (fps > 0) o.contenedor.dataset.fps = fps.toFixed(0);
  };

  const pintarQuieto = () => {
    pintar(o.tiempoFijo ?? MOMENTOS.reposo);
    mostrar();
  };

  const observador = new ResizeObserver(() => {
    ajustar();
    if (o.reducido) pintarQuieto();
  });
  observador.observe(o.contenedor);
  const alPerderContexto = (ev: Event) => {
    ev.preventDefault();
    avisar("fallo", 0);
  };
  lienzo.addEventListener("webglcontextlost", alPerderContexto);

  if (o.reducido) pintarQuieto();
  else raf = requestAnimationFrame(cuadro);

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
      if (destruido) return;
      destruido = true;
      cancelAnimationFrame(raf);
      observador.disconnect();
      lienzo.removeEventListener("webglcontextlost", alPerderContexto);
      for (const b of buffers) gl.deleteBuffer(b);
      gl.deleteProgram(programa);
      gl.getExtension("WEBGL_lose_context")?.loseContext();
      lienzo.remove();
    },
    tiempo: () => tiempoCiclo,
  };
}
