// La tarea de limpieza de ideas de invitado está programada en Vercel.
import { readFileSync } from "node:fs";
import path from "node:path";
import { describe, expect, it } from "vitest";

describe("la limpieza de invitados está programada", () => {
  it("vercel.json la corre a diario", () => {
    const v = JSON.parse(readFileSync(path.join(__dirname, "..", "..", "..", "vercel.json"), "utf8"));
    expect(v.crons).toContainEqual({ path: "/api/cron/limpiar-invitados", schedule: "0 8 * * *" });
  });
});
