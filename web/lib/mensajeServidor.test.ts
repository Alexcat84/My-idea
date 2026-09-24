// AUD-09 H03: la pantalla se tragaba los mensajes honestos del servidor
// (saldo, doble factor, idea demasiado larga, fusible, los 409 del
// seguimiento) y decía "algo se atoró de nuestro lado". La regla: el genérico
// solo cuando el servidor no dio razón.
import { readFileSync } from "node:fs";
import path from "node:path";
import { describe, expect, it } from "vitest";
import { ERROR_GENERICO, leerRechazo } from "./mensajeServidor";
import { MAX_LARGO_TEXTO_USUARIO, MENSAJE_TEXTO_LARGO } from "./constants";

function respuesta(status: number, cuerpo: unknown) {
  return new Response(cuerpo === undefined ? "" : JSON.stringify(cuerpo), { status });
}

describe("leerRechazo: el mensaje del servidor llega a la pantalla", () => {
  it("402 sin saldo: su mensaje, tal cual", async () => {
    const r = await leerRechazo(respuesta(402, { error: "Te quedan 0 créditos; esto cuesta 10." }));
    expect(r).toEqual({ tipo: "mensaje", mensaje: "Te quedan 0 créditos; esto cuesta 10." });
  });
  it("403 del doble factor: pide el desafío", async () => {
    const r = await leerRechazo(respuesta(403, { segundo_factor_requerido: true, error: "Confirma tu segundo factor." }));
    expect(r).toEqual({ tipo: "segundo_factor", mensaje: "Confirma tu segundo factor." });
  });
  it("409, 429 y 503: su mensaje", async () => {
    for (const status of [409, 429, 503]) {
      const r = await leerRechazo(respuesta(status, { error: "razón en palabras de persona" }));
      expect(r.mensaje).toBe("razón en palabras de persona");
    }
  });
  it("400 por texto demasiado largo: el mensaje con su límite", async () => {
    const r = await leerRechazo(respuesta(400, { error: MENSAJE_TEXTO_LARGO, limite: MAX_LARGO_TEXTO_USUARIO }));
    expect(r.mensaje).toBe(MENSAJE_TEXTO_LARGO);
    expect(r.mensaje).toContain(String(MAX_LARGO_TEXTO_USUARIO));
  });
  it("sin razón (500 sin cuerpo, 400 técnico): el genérico", async () => {
    expect((await leerRechazo(respuesta(500, undefined))).mensaje).toBe(ERROR_GENERICO);
    expect((await leerRechazo(respuesta(400, { error: "cuerpo invalido" }))).mensaje).toBe(ERROR_GENERICO);
  });
});

const leer = (rel: string) => readFileSync(path.join(__dirname, "..", "app", rel), "utf8");

describe("ninguna pantalla convierte un rechazo con razón en el genérico", () => {
  it("IdeaView: arranque, turno y plan leen el rechazo del servidor", () => {
    const f = leer("idea/[id]/IdeaView.tsx");
    expect(f).not.toMatch(/else if \(!inicio\.ok\) setError\(ERROR_GENERICO\)/);
    expect(f).not.toMatch(/if \(!res\.ok \|\| !res\.body\) \{\s*setError\(ERROR_GENERICO\)/);
    expect(f).not.toMatch(/if \(!res\.ok\) \{\s*setError\(ERROR_GENERICO\)/);
  });
  it("/nueva: el organizador lee el rechazo del servidor", () => {
    expect(leer("nueva/page.tsx")).not.toMatch(/if \(!res\.ok \|\| !res\.body\) \{\s*setEstado\(\{ fase: "captura", error: "algo se atoró/);
  });
  it("Manos a la Obra: el seguimiento y el cierre de mundo leen el rechazo del servidor", () => {
    const f = leer("ui/ManosALaObra.tsx");
    expect(f).not.toMatch(/res\.status === 429 \|\| res\.status === 402 \? String\(data\.error\) : ERROR_GENERICO/);
  });
});
