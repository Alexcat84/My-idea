// i18n F2, el hilo del idioma: donde el código YA tiene el idioma de la
// interfaz a mano (useIdioma en el cliente, idiomaDeRequest en una ruta,
// idiomaDeCookies en una página del servidor), el texto se elige por ese
// idioma, nunca por la constante del idioma base. Así F3 solo agrega
// catálogos. Lo que se guarda o forma un documento sigue en el base hasta F5
// (D2: el idioma del proyecto) y no entra en este contrato.
import { readdirSync, readFileSync, statSync } from "node:fs";
import path from "node:path";
import { describe, expect, it } from "vitest";
import { MENSAJE_LECTURA_FALLIDA, mensajeLecturaFallida } from "../analyticsEntrada";
import {
  MENSAJE_ADOPCION_PENDIENTE,
  MENSAJE_IDEA_LARGA,
  MENSAJE_TEXTO_LARGO,
  mensajeAdopcionPendiente,
  mensajeIdeaLarga,
  mensajeTextoLargo,
} from "../constants";
import { PREGUNTA_TIPO_OFERTA, preguntaTipoOferta } from "../engine/constants";
import { SECCIONES_ORGANIZADOR, seccionesOrganizador } from "../engine/organizador";
import { AVISO_VERSION_BASICA, avisoVersionBasica } from "../engine/planRedactor";
import { ERROR_SNAPSHOT_ILEGIBLE, errorSnapshotIlegible } from "../engine/snapshotProyecto";
import { ERROR_GENERICO, errorGenerico } from "../mensajeServidor";
import { MENSAJE_TOPE_RENARRACION, mensajeTopeRenarracion } from "../numerosVivo";
import { MENSAJE_FUSIBLE, mensajeFusible } from "../rateLimit";

const RAIZ_APP = path.join(__dirname, "..", "..", "app");

function archivos(dir: string, filtro: (f: string) => boolean): string[] {
  const out: string[] = [];
  for (const nombre of readdirSync(dir)) {
    const p = path.join(dir, nombre);
    if (statSync(p).isDirectory()) out.push(...archivos(p, filtro));
    else if (filtro(p) && !/\.test\.[tj]sx?$/.test(p)) out.push(p);
  }
  return out;
}

/** El código sin las líneas de import ni los comentarios de línea. */
function cuerpo(p: string): string {
  return readFileSync(p, "utf8")
    .replace(/^import[\s\S]*?;\s*$/gm, "")
    .replace(/^\s*(\/\/|\*|\/\*).*$/gm, "");
}

const rel = (p: string) => path.relative(RAIZ_APP, p).replace(/\\/g, "/");

describe("el hilo del idioma", () => {
  it("cada texto por idioma es, en español, idéntico a su constante base (nada visible cambia)", () => {
    expect(mensajeFusible("es")).toBe(MENSAJE_FUSIBLE);
    expect(mensajeTextoLargo("es")).toBe(MENSAJE_TEXTO_LARGO);
    expect(mensajeIdeaLarga("es")).toBe(MENSAJE_IDEA_LARGA);
    expect(mensajeAdopcionPendiente("es")).toBe(MENSAJE_ADOPCION_PENDIENTE);
    expect(errorGenerico("es")).toBe(ERROR_GENERICO);
    expect(mensajeLecturaFallida("es")).toBe(MENSAJE_LECTURA_FALLIDA);
    expect(mensajeTopeRenarracion("es")).toBe(MENSAJE_TOPE_RENARRACION);
    expect(errorSnapshotIlegible("es")).toBe(ERROR_SNAPSHOT_ILEGIBLE);
    expect(avisoVersionBasica("es")).toBe(AVISO_VERSION_BASICA);
    expect(preguntaTipoOferta("es")).toBe(PREGUNTA_TIPO_OFERTA);
    expect(seccionesOrganizador("es")).toEqual(SECCIONES_ORGANIZADOR);
  });

  it("ninguna ruta ni pantalla muestra una constante del idioma base", () => {
    const BASE = [
      "MENSAJE_FUSIBLE",
      "MENSAJE_TEXTO_LARGO",
      "MENSAJE_IDEA_LARGA",
      "MENSAJE_ADOPCION_PENDIENTE",
      "ERROR_GENERICO",
      "MENSAJE_LECTURA_FALLIDA",
      "MENSAJE_TOPE_RENARRACION",
      "ERROR_SNAPSHOT_ILEGIBLE",
      "AVISO_VERSION_BASICA",
      "PREGUNTA_TIPO_OFERTA",
      "SECCIONES_ORGANIZADOR",
      "ETIQUETA_ESTADO",
      "REGISTRO_VACIO",
      "PALABRA_CAMINO",
      "PALABRA_PROBABILIDAD",
      "PALABRA_DOLOR",
      "AVISO_LOGIN",
      "AVISO_2FA",
      "AVISO_PRECIO_EXPLORACION",
    ];
    const patron = new RegExp(`\\b(${BASE.join("|")})\\b`);
    const culpables = archivos(RAIZ_APP, (f) => /\.(ts|tsx)$/.test(f))
      .filter((p) => !p.endsWith(path.join("ui", "SelectorEstado.tsx"))) // la define
      .filter((p) => patron.test(cuerpo(p)))
      .map(rel);
    expect(culpables).toEqual([]);
  });

  it("toda pantalla lee los rechazos del servidor en su idioma", () => {
    const culpables = archivos(RAIZ_APP, (f) => f.endsWith(".tsx"))
      .filter((p) => /leerRechazo\(res\)/.test(cuerpo(p)))
      .map(rel);
    expect(culpables).toEqual([]);
  });

  it("las rutas del recorrido pasan su idioma al motor (la pregunta que se pinta)", () => {
    for (const r of ["api/session/start/route.ts", "api/session/[id]/turn/route.ts", "api/project/[id]/follow/route.ts"]) {
      const src = readFileSync(path.join(RAIZ_APP, r), "utf8");
      const llamada = src.match(/avanzarTurno\(\{[\s\S]*?\}\);/)?.[0] ?? "";
      expect(llamada, r).toMatch(/\bidioma,/);
    }
    const start = readFileSync(path.join(RAIZ_APP, "api/project/[id]/world/[pack]/start/route.ts"), "utf8");
    // i18n F5: la pregunta sale en el idioma de las plantillas de la IDEA
    // (el suyo si es de los once; si no, el de la interfaz).
    expect(start).toMatch(/obtenerPregunta\(semillaId, graph\[semillaId\], preguntasCache, idiomaDePlantilla\(idiomaIdea, idioma\)\)/);
  });
});
