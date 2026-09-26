// i18n F6 (D9): un buscador que sigue un hreflang llega a `/?lang=xx` sin
// cookie y casi siempre sin Accept-Language. proxy.ts debe servirle ESE idioma
// (en la petición, para que el layout ya lo lea, y en la cookie de la
// respuesta), y en la portada no debe acuñar identidad invisible. Se corre el
// proxy de verdad con Supabase simulado (ninguna clave hace falta).
import { NextRequest } from "next/server";
import { beforeEach, describe, expect, it, vi } from "vitest";

const signInAnonymously = vi.fn(async () => ({ error: null }));
vi.mock("@supabase/ssr", () => ({
  createServerClient: () => ({
    auth: {
      getUser: async () => ({ data: { user: null } }),
      signInAnonymously,
      signInWithPassword: vi.fn(),
    },
  }),
}));
vi.mock("@/lib/supabase/admin", () => ({ createAdminClient: vi.fn() }));

const { proxy } = await import("@/proxy");

const GOOGLEBOT = "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)";
const pedir = (url: string, cabeceras: Record<string, string> = {}) =>
  new NextRequest(url, { headers: { "user-agent": GOOGLEBOT, ...cabeceras } });

describe("proxy.ts honra ?lang= para los buscadores (D9)", () => {
  beforeEach(() => signInAnonymously.mockClear());

  it("/?lang=fr sin cookie ni Accept-Language: la visita va en francés y la cookie lo guarda", async () => {
    const res = await proxy(pedir("https://www.myideaproject.com/?lang=fr"));
    // la petición reescrita que lee el layout lleva la cookie en fr
    expect(res.headers.get("x-middleware-request-cookie") ?? "").toContain("myidea_idioma=fr");
    expect(res.cookies.get("myidea_idioma")?.value).toBe("fr");
  });

  it("?lang= manda sobre el Accept-Language del rastreador", async () => {
    const res = await proxy(pedir("https://www.myideaproject.com/?lang=zh", { "accept-language": "en-US" }));
    expect(res.cookies.get("myidea_idioma")?.value).toBe("zh");
  });

  it("?lang= manda sobre una cookie anterior", async () => {
    const res = await proxy(pedir("https://www.myideaproject.com/?lang=ar", { cookie: "myidea_idioma=en" }));
    expect(res.cookies.get("myidea_idioma")?.value).toBe("ar");
  });

  it("la URL sin parámetro (x-default) y sin nada más cae al español", async () => {
    const res = await proxy(pedir("https://www.myideaproject.com/"));
    expect(res.cookies.get("myidea_idioma")?.value).toBe("es");
  });

  it("un ?lang= que no se sirve no manda: cae a la negociación normal", async () => {
    const res = await proxy(pedir("https://www.myideaproject.com/?lang=zz", { "accept-language": "de-DE" }));
    expect(res.cookies.get("myidea_idioma")?.value).toBe("de");
  });

  it("en la portada el rastreador no acuña identidad invisible", async () => {
    await proxy(pedir("https://www.myideaproject.com/?lang=ja"));
    expect(signInAnonymously).not.toHaveBeenCalled();
  });

  it("robots.txt y sitemap.xml tampoco acuñan identidad (todo rastreador los pide)", async () => {
    await proxy(pedir("https://www.myideaproject.com/robots.txt", { "user-agent": GOOGLEBOT }));
    await proxy(pedir("https://www.myideaproject.com/sitemap.xml", { "user-agent": GOOGLEBOT }));
    expect(signInAnonymously).not.toHaveBeenCalled();
  });
});
