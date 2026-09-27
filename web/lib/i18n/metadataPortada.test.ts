// i18n F6 (DISENO §3.6): los metadatos de la portada salen en el idioma de la
// visita, con los hreflang de los once más x-default y la canónica de la
// variante pedida. Se llama al generateMetadata de verdad con el idioma de la
// cookie simulado (lo que proxy.ts dejaría tras un ?lang=fr). El francés lleva
// espacio duro antes de ":" (F3_CONVENCIONES).
import { describe, expect, it, vi } from "vitest";

vi.mock("@/lib/i18n/servidor", () => ({ idiomaDeCookies: async () => "fr" }));
vi.mock("@/lib/supabase/server", () => ({ createClient: vi.fn() }));
vi.mock("@/app/ui/Landing", () => ({ Landing: () => null }));
vi.mock("@/lib/i18n/IdiomaProvider", () => ({ IdiomaProvider: () => null }));
vi.mock("./globals.css", () => ({}));
vi.mock("next/font/google", () => {
  const fuente = () => ({ variable: "--x" });
  return { Inter: fuente, Noto_Sans_Arabic: fuente, Noto_Sans_Devanagari: fuente, Noto_Sans_JP: fuente, Noto_Sans_KR: fuente, Noto_Sans_SC: fuente };
});

const { generateMetadata } = await import("@/app/page");
const { generateMetadata: metadataLayout } = await import("@/app/layout");

describe("metadatos de la portada por idioma", () => {
  it("?lang=fr: título y descripción del catálogo en francés, canónica ?lang=fr, doce alternos", async () => {
    const m = await generateMetadata({ searchParams: Promise.resolve({ lang: "fr" }) });
    expect(m.title).toBe("My Idea : mets ta créativité en action");
    expect(m.alternates?.canonical).toBe("https://www.myideaproject.com/?lang=fr");
    const alternos = m.alternates?.languages as Record<string, string>;
    expect(Object.keys(alternos)).toHaveLength(12);
    expect(alternos["zh-Hans"]).toBe("https://www.myideaproject.com/?lang=zh");
    expect(alternos["x-default"]).toBe("https://www.myideaproject.com/");
    expect((m.openGraph as { locale?: string }).locale).toBe("fr_CA");
  });

  it("sin ?lang=: la canónica es la URL sin parámetro", async () => {
    const m = await generateMetadata({ searchParams: Promise.resolve({}) });
    expect(m.alternates?.canonical).toBe("https://www.myideaproject.com/");
  });

  it("el layout fija la base de las URL absolutas y la descripción en el idioma de la visita", async () => {
    const m = await metadataLayout();
    expect(String(m.metadataBase)).toBe("https://www.myideaproject.com/");
    expect(m.description).toBe("L'espace où tes idées prennent forme.");
  });
});
