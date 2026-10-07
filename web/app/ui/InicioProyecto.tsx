"use client";

/**
 * InicioProyecto — el día en que nació el proyecto, para los selectores de
 * "cuándo lo hiciste" (decisión del fundador, 8 oct 2026): no ofrecen días
 * anteriores. El servidor aplica la misma regla (lib/inicioProyecto.ts), así
 * que esto es comodidad, no la guarda.
 */
import { createContext, useContext, type ReactNode } from "react";
import { fechaInputLocal } from "@/lib/fechas";

const Ctx = createContext<string | null>(null);

export function InicioProyectoProvider({ creadoAt, children }: { creadoAt: string | null | undefined; children?: ReactNode }) {
  const dia = creadoAt && !Number.isNaN(Date.parse(creadoAt)) ? fechaInputLocal(new Date(creadoAt)) : null;
  return <Ctx.Provider value={dia}>{children}</Ctx.Provider>;
}

/** "YYYY-MM-DD" (local) del día de inicio, o undefined si no se conoce. */
export function useMinFechaHecho(): string | undefined {
  return useContext(Ctx) ?? undefined;
}
