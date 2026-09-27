// AUD-09 M25 (tanda 7A, dinero; decisión del fundador 25 sep 2026): RESERVA
// DE CRÉDITOS al empezar la sesión, cobro al entregar, liberación si la IA
// falla. Antes la verificación del inicio no apartaba nada: con saldo para UNA
// entrega se abrían varias sesiones en paralelo, todas se entregaban y solo la
// primera se cobraba. Esta prueba fija la capa fina sobre la migración 042.
import { beforeEach, describe, expect, it, vi } from "vitest";

type Fila = Record<string, unknown>;
let tablas: Record<string, Fila[]> = {};
let rpcRespuesta: Record<string, { data: unknown; error: unknown }> = {};
const rpcLlamadas: Array<{ nombre: string; args: Record<string, unknown> }> = [];

/** Cliente admin falso: select con filtros eq/gt/neq y rpc programable. */
function adminFalso() {
  return {
    from(tabla: string) {
      const filtros: Array<(f: Fila) => boolean> = [];
      const q = {
        select: () => q,
        eq: (c: string, v: unknown) => (filtros.push((f) => f[c] === v), q),
        neq: (c: string, v: unknown) => (filtros.push((f) => f[c] !== v), q),
        gt: (c: string, v: string) => (filtros.push((f) => String(f[c]) > v), q),
        maybeSingle: async () => ({ data: (tablas[tabla] ?? []).filter((f) => filtros.every((p) => p(f)))[0] ?? null, error: null }),
        then: (r: (v: { data: Fila[]; error: null }) => unknown) =>
          r({ data: (tablas[tabla] ?? []).filter((f) => filtros.every((p) => p(f))), error: null }),
      };
      return q;
    },
    rpc: async (nombre: string, args: Record<string, unknown>) => {
      rpcLlamadas.push({ nombre, args });
      return rpcRespuesta[nombre] ?? { data: null, error: null };
    },
  };
}
vi.mock("./supabase/admin", () => ({ createAdminClient: () => adminFalso() }));

import {
  MINUTOS_RESERVA,
  mensajeSaldoInsuficiente,
  reservarCreditos,
  resolverReserva,
  verificarSaldo,
} from "./creditos";

const U = "u1";
const futuro = new Date(Date.now() + 3600_000).toISOString();
const pasado = new Date(Date.now() - 3600_000).toISOString();

beforeEach(() => {
  tablas = { credit_accounts: [{ user_id: U, creditos_total: 10 }], credit_reservas: [] };
  rpcRespuesta = {};
  rpcLlamadas.length = 0;
});

describe("el disponible descuenta lo apartado (AUD-09 M25)", () => {
  // A MANO: saldo 10. Reservas: una activa de 10 que vence en una hora (cuenta),
  // una activa de 5 ya vencida (no cuenta), una liberada de 5 (no cuenta).
  // Apartado = 10. Disponible = 10 - 10 = 0: no alcanza para otro plan de 10.
  beforeEach(() => {
    tablas.credit_reservas = [
      { user_id: U, clave: "plan:s1", monto: 10, estado: "activa", expira_at: futuro },
      { user_id: U, clave: "plan:s0", monto: 5, estado: "activa", expira_at: pasado },
      { user_id: U, clave: "plan:sx", monto: 5, estado: "liberada", expira_at: futuro },
    ];
  });

  it("con 10 de saldo y 10 apartados, otra sesión de 10 no alcanza", async () => {
    expect(await verificarSaldo(U, 10)).toEqual({ alcanza: false, creditos: 10, apartados: 10 });
  });

  it("la propia reserva no se cuenta contra sí misma", async () => {
    expect(await verificarSaldo(U, 10, "plan:s1")).toEqual({ alcanza: true, creditos: 10, apartados: 0 });
  });

  it("el 402 dice cuánto hay apartado, sin cambiar la promesa del precio", () => {
    expect(mensajeSaldoInsuficiente(10, 10, 10)).toBe(
      "Tienes 10 créditos y 10 ya están apartados para un plan que tienes en curso; esto cuesta 10. Tu trabajo queda guardado tal como está."
    );
    // Sin nada apartado, el mensaje de siempre.
    expect(mensajeSaldoInsuficiente(3, 10)).toBe("Te quedan 3 créditos; esto cuesta 10. Tu trabajo queda guardado tal como está.");
  });
});

describe("reservar y resolver (AUD-09 M25)", () => {
  it("reserva con la clave del cobro y el vencimiento de la casa", async () => {
    rpcRespuesta.reservar_creditos = { data: 0, error: null };
    expect(await reservarCreditos(U, "plan:s2", "plan_completo", 10)).toEqual({ reservado: true, disponible: 0 });
    expect(rpcLlamadas[0]).toEqual({
      nombre: "reservar_creditos",
      args: { p_user_id: U, p_clave: "plan:s2", p_concepto: "plan_completo", p_monto: 10, p_minutos: MINUTOS_RESERVA },
    });
  });

  it("-1 de la base es 'no alcanza'", async () => {
    rpcRespuesta.reservar_creditos = { data: -1, error: null };
    expect((await reservarCreditos(U, "plan:s2", "plan_completo", 10)).reservado).toBe(false);
  });

  it("sin la migración 042 degrada a la verificación de antes, con el síntoma en el log", async () => {
    const log = vi.spyOn(console, "error").mockImplementation(() => {});
    rpcRespuesta.reservar_creditos = {
      data: null,
      error: { code: "PGRST202", message: "Could not find the function public.reservar_creditos" },
    };
    expect(await reservarCreditos(U, "plan:s2", "plan_completo", 10)).toEqual({ reservado: true, disponible: 10 });
    expect(log).toHaveBeenCalled();
    log.mockRestore();
  });

  it("cualquier otro error de la base se propaga", async () => {
    rpcRespuesta.reservar_creditos = { data: null, error: { code: "57014", message: "timeout" } };
    await expect(reservarCreditos(U, "plan:s2", "plan_completo", 10)).rejects.toMatchObject({ code: "57014" });
  });

  it("resolver marca la reserva, y si falla no rompe la entrega (el vencimiento la suelta)", async () => {
    await resolverReserva("plan:s2", "cobrada");
    expect(rpcLlamadas.at(-1)).toEqual({ nombre: "resolver_reserva", args: { p_clave: "plan:s2", p_estado: "cobrada" } });
    const log = vi.spyOn(console, "error").mockImplementation(() => {});
    rpcRespuesta.resolver_reserva = { data: null, error: { code: "XX000", message: "boom" } };
    await expect(resolverReserva("plan:s2", "liberada")).resolves.toBeUndefined();
    expect(log).toHaveBeenCalled();
    log.mockRestore();
  });
});
