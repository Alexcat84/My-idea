/** Atributos con que se crea el contexto WebGL2 del motor (los que pide three.js). */
export const ATRIBUTOS_CONTEXTO: WebGLContextAttributes = {
  alpha: false,
  depth: false,
  stencil: false,
  antialias: false,
  premultipliedAlpha: true,
  preserveDrawingBuffer: false,
  powerPreference: "high-performance",
  failIfMajorPerformanceCaveat: false,
};

/** true si el nombre de la GPU delata un rasterizador por software. */
export function esSoftware(renderizador: string): boolean {
  return /swiftshader|llvmpipe|software|basic render/i.test(renderizador);
}

/** Nombre real de la GPU (Chrome enmascara RENDERER como "WebKit WebGL"). */
export function nombreGpu(gl: WebGLRenderingContext | WebGL2RenderingContext): string {
  const info = gl.getExtension("WEBGL_debug_renderer_info");
  return String(gl.getParameter(info ? info.UNMASKED_RENDERER_WEBGL : gl.RENDERER) ?? "");
}
