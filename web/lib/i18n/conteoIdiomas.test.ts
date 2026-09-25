/**
 * i18n F5, añadido del fundador (25 sep 2026): el CONTEO ANÓNIMO de los
 * idiomas en que se escriben las ideas (migración 046). Solo viajan dos
 * códigos de idioma: nada de la persona ni de la idea. Y el conteo nunca tumba
 * la creación de una idea.
 */
import { describe, expect, it, vi } from "vitest";
import type { SupabaseClient } from "@supabase/supabase-js";
import { contarIdiomaDeIdea } from "./conteoIdiomas";

describe("contarIdiomaDeIdea", () => {
  it("llama a la función de la 046 solo con los dos idiomas", async () => {
    const rpc = vi.fn(async () => ({ error: null }));
    await contarIdiomaDeIdea("ru", "en", { rpc } as unknown as SupabaseClient);
    expect(rpc).toHaveBeenCalledWith("contar_idioma_de_idea", { p_idioma_idea: "ru", p_idioma_interfaz: "en" });
  });

  it("si la 046 no está aplicada (o falla), no lanza", async () => {
    const rpc = vi.fn(async () => ({ error: { code: "PGRST202", message: "Could not find the function" } }));
    const log = vi.spyOn(console, "error").mockImplementation(() => {});
    await expect(contarIdiomaDeIdea("ko", "es", { rpc } as unknown as SupabaseClient)).resolves.toBeUndefined();
    expect(log).toHaveBeenCalled();
    log.mockRestore();
  });

  it("si el cliente mismo explota, tampoco lanza", async () => {
    const rpc = vi.fn(async () => {
      throw new Error("sin red");
    });
    const log = vi.spyOn(console, "error").mockImplementation(() => {});
    await expect(contarIdiomaDeIdea("ko", "es", { rpc } as unknown as SupabaseClient)).resolves.toBeUndefined();
    log.mockRestore();
  });
});
