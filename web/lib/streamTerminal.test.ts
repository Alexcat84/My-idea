/**
 * streamTerminal.test.ts . la garantia de que NINGUN stream del plan termina
 * en silencio (4 sep 2026).
 *
 * El defecto que la trajo: la corrida I del vuelo cayo con "el plan de
 * seguimiento no devolvio markdown". El cliente no recibio `done` NI `error`,
 * el servidor respondio 200 y no escribio una sola linea `[plan]`. Un final
 * mudo es indistinguible de un transitorio, y por eso no se podia clasificar.
 */
import { describe, expect, it } from "vitest";
import { readFileSync } from "node:fs";
import { join } from "node:path";
import { garantizarTerminal, MOTIVO_CIERRE_SIN_TERMINAL } from "./streamTerminal";

function arnes(over: Partial<Parameters<typeof garantizarTerminal>[0]> = {}) {
  const enviados: Array<{ evento: string; data: unknown }> = [];
  const logs: Array<{ mensaje: string; detalle: unknown }> = [];
  const base = {
    terminalEmitido: null as string | null,
    emitidos: ["contexto_final_usuario"],
    causa: new Error("enqueue on closed controller"),
    sessionId: "sid-1",
    projectId: "pid-1",
    enviar: (evento: string, data: unknown) => { enviados.push({ evento, data }); },
    log: (mensaje: string, detalle: unknown) => { logs.push({ mensaje, detalle }); },
  };
  return { enviados, logs, args: { ...base, ...over } };
}

describe("ningun stream del plan termina en silencio", () => {
  it("un stream que se cierra SIN terminal produce error con motivo 'cierre sin terminal'", () => {
    const { enviados, logs, args } = arnes();
    expect(garantizarTerminal(args)).toBe(true);

    // grita por el canal
    expect(enviados).toHaveLength(1);
    expect(enviados[0].evento).toBe("error");
    const d = enviados[0].data as Record<string, unknown>;
    expect(d.motivo).toBe(MOTIVO_CIERRE_SIN_TERMINAL);
    expect(d.session_id).toBe("sid-1");
    expect(d.emitidos).toEqual(["contexto_final_usuario"]);
    expect(d.causa).toBe("enqueue on closed controller");

    // y grita por el log del servidor, que es la prueba cuando el canal murio
    expect(logs).toHaveLength(1);
    expect(logs[0].mensaje).toBe("[plan] cierre sin terminal");
  });

  it("si YA salio un terminal, no toca nada", () => {
    for (const t of ["done", "error"]) {
      const { enviados, logs, args } = arnes({ terminalEmitido: t });
      expect(garantizarTerminal(args)).toBe(false);
      expect(enviados).toHaveLength(0);
      expect(logs).toHaveLength(0);
    }
  });

  it("si el canal esta roto, el fallo del emit NO se propaga y el log sigue siendo la prueba", () => {
    const { logs, args } = arnes({
      enviar: () => { throw new Error("controller cerrado"); },
    });
    // una garantia que revienta al garantizar no garantiza nada
    expect(() => garantizarTerminal(args)).not.toThrow();
    expect(logs).toHaveLength(1);
    expect(logs[0].mensaje).toBe("[plan] cierre sin terminal");
  });

  it("CASO POR MUTACION: la ruta llama a la garantia DESDE SU finally", () => {
    // Sin esta comprobacion, quitar la llamada del finally dejaria la prueba de
    // arriba en verde y el defecto vivo: el helper funcionaria y nadie lo
    // llamaria. Es el mismo patron que engine/test_aviso_curaduria.py usa.
    const ruta = join(process.cwd(), "app/api/session/[id]/plan/route.ts");
    const cuerpo = readFileSync(ruta, "utf-8");
    expect(cuerpo, "la ruta no importa la garantia").toContain(
      'import { garantizarTerminal } from "@/lib/streamTerminal"'
    );
    const finallyIdx = cuerpo.indexOf("} finally {");
    expect(finallyIdx, "no hay finally en la ruta").toBeGreaterThan(-1);
    const bloqueFinally = cuerpo.slice(finallyIdx, cuerpo.indexOf("controller.close()", finallyIdx));
    expect(bloqueFinally, "el finally NO llama a garantizarTerminal").toContain("garantizarTerminal({");
  });
});
