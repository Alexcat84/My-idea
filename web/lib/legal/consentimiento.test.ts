// CONSENTIMIENTO LEGAL VERSIONADO, corrección del fundador del 7 oct 2026 (manda sobre el modal de cbf087fe):
// - Navegar es libre: el modal que tapaba la página se retira y nada tapa nada.
// - La aceptación se pide en el PRIMER ENVÍO DE DATOS (escribir la idea y generar la evaluación gratuita), con una
//   línea junto al botón y el botón "Aceptar y generar", antes de mandar nada a la IA.
// - Sin cuenta también: se guarda en la identidad invisible y pasa a la cuenta con la adopción.
// - Si los textos cambian, se vuelve a pedir en el siguiente envío o al entrar con la cuenta, nunca al cargar.
// Prueba en rojo primero: escrita antes de retirar el modal y de mover la aceptación al envío.
import { existsSync, readFileSync } from "node:fs";
import path from "node:path";
import { describe, expect, it } from "vitest";
import { LOCALES } from "@/lib/i18n/config";
import { CONSENTIMIENTO } from "@/lib/i18n/mensajes/consentimiento";
import { estadoConsentimiento, HUELLA_LEGAL, idiomaTextoLegal, VERSION_LEGAL } from "./consentimiento";

const RAIZ = path.resolve(__dirname, "..", "..", "..");
const leer = (rel: string) => readFileSync(path.join(RAIZ, rel), "utf-8");
const leerSiExiste = (rel: string) => (existsSync(path.join(RAIZ, rel)) ? leer(rel) : "");

describe("estadoConsentimiento: a toda identidad que envía datos, invitada o con cuenta", () => {
  it("sin ninguna aceptación: la primera", () => {
    expect(estadoConsentimiento(null)).toEqual({ requiere: true, motivo: "primera_aceptacion" });
  });

  it("con una versión anterior: la nueva", () => {
    expect(estadoConsentimiento("2000-01-01")).toEqual({ requiere: true, motivo: "nueva_version" });
  });

  it("al día: nada", () => {
    expect(estadoConsentimiento(VERSION_LEGAL)).toEqual({ requiere: false, motivo: null });
  });
});

describe("navegar es libre: el modal se retira y nada tapa la página", () => {
  it("el layout raíz ya no monta ningún modal de consentimiento", () => {
    expect(leer("web/app/layout.tsx")).not.toContain("ConsentimientoLegal");
    expect(existsSync(path.join(RAIZ, "web/app/ui/ConsentimientoLegal.tsx"))).toBe(false);
  });

  it("la línea del consentimiento no es un diálogo ni flota sobre la página", () => {
    const linea = leerSiExiste("web/app/ui/LineaConsentimiento.tsx");
    expect(linea).not.toBe("");
    expect(linea).not.toMatch(/aria-modal|role="dialog"|fixed inset-0/);
  });
});

describe("el primer envío de datos: la línea junto al botón y 'Aceptar y generar'", () => {
  it("/nueva pinta la línea, cambia el botón y guarda la aceptación ANTES de llamar al organizador", () => {
    const nueva = leer("web/app/nueva/page.tsx");
    expect(nueva).toContain("<LineaConsentimiento");
    expect(nueva).toContain("aceptarYGenerar");
    const iAceptar = nueva.indexOf("consentimiento.aceptar(");
    const iOrganizador = nueva.indexOf('fetch("/api/organizer/stream"');
    expect(iAceptar).toBeGreaterThan(-1);
    expect(iOrganizador).toBeGreaterThan(iAceptar);
  });

  it("La Exploración (la idea ya existe): si el servidor pide aceptar, la vista pinta la línea, no un error mudo", () => {
    const vista = leer("web/app/idea/[id]/IdeaView.tsx");
    expect(vista).toContain('r.tipo === "consentimiento"');
    expect(vista).toContain("<LineaConsentimiento");
    expect(vista).toContain("aceptarYSeguir");
  });

  it("la línea enlaza a /terminos y a /privacidad (en otra pestaña: la idea escrita no se pierde)", () => {
    const linea = leerSiExiste("web/app/ui/LineaConsentimiento.tsx");
    expect(linea).toContain('href="/terminos"');
    expect(linea).toContain('href="/privacidad"');
    expect(linea).toContain('target="_blank"');
  });

  it("los textos existen en los once idiomas, y la línea nombra los dos documentos con sus enlaces", () => {
    for (const l of LOCALES) {
      const t = CONSENTIMIENTO[l] as unknown as Record<string, Record<string, string> | undefined>;
      expect(t, l).toBeDefined();
      const claves: Array<[string, string]> = [
        ["envio", "linea"], ["envio", "lineaNueva"], ["envio", "aceptarYGenerar"], ["envio", "aceptarYSeguir"],
        ["envio", "guardando"], ["envio", "errorGuardar"], ["envio", "versionCambio"], ["login", "enlaces"],
        ["login", "linea"], ["servidor", "requerida"], ["servidor", "requeridaNueva"], ["servidor", "noLeido"],
        ["cookies", "aviso"],
      ];
      for (const [grupo, clave] of claves) {
        expect((t[grupo]?.[clave] ?? "").trim().length, `${l} ${grupo}.${clave}`).toBeGreaterThan(0);
      }
      for (const [grupo, clave] of [["envio", "linea"], ["envio", "lineaNueva"], ["login", "linea"]]) {
        const v = t[grupo]?.[clave] ?? "";
        expect(v, `${l} ${grupo}.${clave}`).toMatch(/<terminos>.+<\/terminos>/);
        expect(v, `${l} ${grupo}.${clave}`).toMatch(/<privacidad>.+<\/privacidad>/);
      }
    }
  });

  it("en español, las palabras del fundador", () => {
    const es = CONSENTIMIENTO.es as unknown as { envio?: { linea: string; aceptarYGenerar: string } };
    expect(es.envio?.linea).toBe(
      "Al continuar, aceptas los <terminos>Términos</terminos> y la <privacidad>Política de Privacidad</privacidad>"
    );
    expect(es.envio?.aceptarYGenerar).toBe("Aceptar y generar");
  });
});

describe("al entrar con la cuenta: una línea en el flujo de entrada, no un modal", () => {
  it("/login enlaza a /terminos y a /privacidad, pinta la línea junto al botón y manda la aceptación", () => {
    const fuente = leer("web/app/login/page.tsx");
    expect(fuente).toContain('href="/terminos"');
    expect(fuente).toContain('href="/privacidad"');
    expect(fuente).toContain(".linea");
    expect(fuente).toContain("acepta_legal");
  });
});

describe("las cookies: solo necesarias, un aviso pequeño abajo que no tapa nada", () => {
  it("el layout monta el aviso, en el flujo de la página (no flotante) y con enlace a /cookies", () => {
    expect(leer("web/app/layout.tsx")).toContain("<AvisoCookies");
    const aviso = leerSiExiste("web/app/ui/AvisoCookies.tsx");
    expect(aviso).toContain('href="/cookies"');
    expect(aviso).not.toMatch(/\bfixed\b|aria-modal|role="dialog"/);
  });
});

describe("la versión tiene una sola fuente: docs/legal/version.json", () => {
  it("la app lee la vigente y su huella, publicadas por scripts/sync_legal_web.py", () => {
    const reg = JSON.parse(leer("docs/legal/version.json")) as {
      vigente: string;
      versiones: { version: string; huella: string }[];
    };
    expect(VERSION_LEGAL).toBe(reg.vigente);
    expect(HUELLA_LEGAL).toBe(reg.versiones.find((v) => v.version === reg.vigente)?.huella);
  });

  it("los textos legales existen en español y francés: cualquier otro idioma lee el español", () => {
    expect(idiomaTextoLegal("fr")).toBe("fr");
    expect(idiomaTextoLegal("es")).toBe("es");
    expect(idiomaTextoLegal("ja")).toBe("es");
  });
});

describe("el registro: se borra con la cuenta y la Privacidad dice cuándo se pide", () => {
  it("aceptaciones_legales cuelga de auth.users con ON DELETE CASCADE", () => {
    const sql = leer("supabase/migrations/my_idea_050_consentimiento_legal.sql");
    expect(sql).toMatch(/user_id\s+uuid NOT NULL REFERENCES auth\.users \(id\) ON DELETE CASCADE/);
  });

  it("la ruta de borrado no lo anonimiza ni lo conserva aparte", () => {
    expect(leer("web/app/api/cuenta/eliminar/route.ts")).not.toContain("aceptaciones_legales");
  });

  it("la Privacidad (es y fr) y el inventario: se pide al enviar tu idea, también sin cuenta, y pasa a tu cuenta", () => {
    const es = leer("docs/legal/PRIVACIDAD.md");
    const fr = leer("docs/legal/fr/CONFIDENTIALITE.md");
    const inv = leer("docs/legal/INVENTARIO_DATOS.md");
    expect(es).toContain("el registro de tus aceptaciones");
    expect(es).toContain("la primera vez que envías tu idea");
    expect(es).toContain("también sin cuenta");
    expect(es).toContain("pasa a tu cuenta");
    expect(es).not.toContain("cuando entras con tu cuenta te pedimos que los");
    expect(fr).toContain("registre de vos acceptations");
    expect(fr).toContain("la première fois que vous envoyez votre idée");
    expect(fr).toContain("même sans compte");
    expect(fr).toContain("est transféré à votre compte");
    expect(inv).toContain("aceptaciones_legales");
    expect(inv).toContain("también la identidad invisible");
  });
});
