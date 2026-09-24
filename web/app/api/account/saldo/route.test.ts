// AUD-09 M31 + decisión del fundador (25 sep 2026), tanda 7B (confianza): el
// saldo del encabezado muestra lo DISPONIBLE (saldo menos lo reservado por una
// sesión en curso, M25) y, si hay reserva activa, lo dice. Antes mostraba el
// saldo entero aunque parte estuviera apartada: un número que no se podía gastar.
import { beforeEach, describe, expect, it, vi } from "vitest";

let usuario: { id: string; email: string; is_anonymous?: boolean } | null = { id: "u1", email: "a@b.c" };
vi.mock("@/lib/supabase/server", () => ({
  createClient: vi.fn(async () => ({ auth: { getUser: async () => ({ data: { user: usuario } }) } })),
}));
let saldo: number | null = 25;
vi.mock("@/lib/saldo", () => ({ leerSaldo: async () => saldo }));
let apartado: number | Error = 10;
vi.mock("@/lib/creditos", async (importOriginal) => ({
  ...(await importOriginal<typeof import("@/lib/creditos")>()),
  apartadoDe: async () => {
    if (apartado instanceof Error) throw apartado;
    return apartado;
  },
}));
vi.mock("@/lib/identidad", async (importOriginal) => ({
  ...(await importOriginal<typeof import("@/lib/identidad")>()),
  esInvitadoInvisible: () => false,
}));

import { GET } from "./route";

describe("GET /api/account/saldo: lo disponible y lo reservado (AUD-09 M31)", () => {
  beforeEach(() => {
    usuario = { id: "u1", email: "a@b.c" };
    saldo = 25;
    apartado = 10;
  });

  it("devuelve lo disponible y lo reservado", async () => {
    const d = await (await GET()).json();
    // A MANO: saldo 25, reservados 10 -> disponible 25 - 10 = 15.
    expect(d).toMatchObject({ saldo: 25, reservados: 10, disponible: 15 });
  });

  it("sin reservas, lo disponible es el saldo entero", async () => {
    apartado = 0;
    expect(await (await GET()).json()).toMatchObject({ saldo: 25, reservados: 0, disponible: 25 });
  });

  it("si no se pueden leer las reservas, no inventa un disponible", async () => {
    const log = vi.spyOn(console, "error").mockImplementation(() => {});
    apartado = new Error("timeout");
    const d = await (await GET()).json();
    expect(d.disponible).toBeNull();
    log.mockRestore();
  });
});
