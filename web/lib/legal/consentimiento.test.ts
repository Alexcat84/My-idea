// CONSENTIMIENTO LEGAL VERSIONADO (decisión del fundador, 7 oct 2026; idea tomada de The Original I Ching,
// auth/complete-legal + user_legal_acceptances). Las cuentas REALES aceptan los Términos y la Privacidad por
// versión y la app vuelve a pedirlo cuando la versión cambia. La web sigue ABIERTA: la identidad invisible jamás ve
// el modal, y las páginas legales, el login y el centro de cuenta (desde donde se borra la cuenta) nunca lo muestran.
// Prueba en rojo primero: nació antes que lib/legal/consentimiento.ts y que el modal.
import { readFileSync } from "node:fs";
import path from "node:path";
import { describe, expect, it } from "vitest";
import { LOCALES } from "@/lib/i18n/config";
import { CONSENTIMIENTO } from "@/lib/i18n/mensajes/consentimiento";
import { estadoConsentimiento, HUELLA_LEGAL, idiomaTextoLegal, rutaSinConsentimiento, VERSION_LEGAL } from "./consentimiento";

const RAIZ = path.resolve(__dirname, "..", "..", "..");
const leer = (rel: string) => readFileSync(path.join(RAIZ, rel), "utf-8");

describe("estadoConsentimiento: a quién se le pide y por qué", () => {
  it("la identidad invisible nunca: la web es abierta, sin muro", () => {
    expect(estadoConsentimiento(false, null)).toEqual({ requiere: false, motivo: null });
    expect(estadoConsentimiento(false, "1999-01-01")).toEqual({ requiere: false, motivo: null });
  });

  it("una cuenta real sin ninguna aceptación: la primera", () => {
    expect(estadoConsentimiento(true, null)).toEqual({ requiere: true, motivo: "primera_aceptacion" });
  });

  it("una cuenta real que aceptó una versión anterior: la nueva", () => {
    expect(estadoConsentimiento(true, "2000-01-01")).toEqual({ requiere: true, motivo: "nueva_version" });
  });

  it("una cuenta real al día: nada", () => {
    expect(estadoConsentimiento(true, VERSION_LEGAL)).toEqual({ requiere: false, motivo: null });
  });
});

describe("rutaSinConsentimiento: dónde el modal no aparece nunca", () => {
  it("las páginas legales y de ayuda, el login, los regresos de auth y el centro de cuenta", () => {
    for (const r of ["/terminos", "/privacidad", "/cookies", "/login", "/auth/callback", "/auth/update-password",
      "/eliminar-cuenta", "/preguntas-frecuentes", "/cuenta"]) {
      expect(rutaSinConsentimiento(r), r).toBe(true);
    }
  });

  it("la app sí (con cuenta real y sin aceptar)", () => {
    for (const r of ["/ideas", "/idea/abc", "/nueva", "/creditos", "/potenciadores", "/", "/terminos-falsos"]) {
      expect(rutaSinConsentimiento(r), r).toBe(false);
    }
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

describe("el borrado de la cuenta se lleva el registro (coherente con la 044: borrar borra de verdad)", () => {
  it("aceptaciones_legales cuelga de auth.users con ON DELETE CASCADE", () => {
    const sql = leer("supabase/migrations/my_idea_050_consentimiento_legal.sql");
    expect(sql).toMatch(/user_id\s+uuid NOT NULL REFERENCES auth\.users \(id\) ON DELETE CASCADE/);
  });

  it("la ruta de borrado no lo anonimiza ni lo conserva aparte", () => {
    expect(leer("web/app/api/cuenta/eliminar/route.ts")).not.toContain("aceptaciones_legales");
  });

  it("la Privacidad (es y fr) y el inventario lo dicen", () => {
    expect(leer("docs/legal/PRIVACIDAD.md")).toContain("el registro de tus aceptaciones");
    expect(leer("docs/legal/fr/CONFIDENTIALITE.md")).toContain("registre de vos acceptations");
    expect(leer("docs/legal/INVENTARIO_DATOS.md")).toContain("aceptaciones_legales");
  });
});

describe("la interfaz: el login enlaza los textos y el modal vive en el layout", () => {
  it("los textos del modal y del login existen en los once idiomas", () => {
    for (const l of LOCALES) {
      const t = CONSENTIMIENTO[l];
      expect(t, l).toBeDefined();
      for (const v of [t.tituloPrimera, t.tituloNueva, t.introPrimera, t.introNueva, t.casilla, t.aceptar,
        t.salir, t.borrar, t.errorGuardar, t.errorEstado, t.versionCambio, t.login.enlaces, t.login.aviso]) {
        expect(v.trim().length, l).toBeGreaterThan(0);
      }
    }
  });

  it("/login enlaza a /terminos y a /privacidad", () => {
    const fuente = leer("web/app/login/page.tsx");
    expect(fuente).toContain('href="/terminos"');
    expect(fuente).toContain('href="/privacidad"');
  });

  it("el modal enlaza a los dos textos, guarda por la ruta del servidor y está montado en el layout raíz", () => {
    const modal = leer("web/app/ui/ConsentimientoLegal.tsx");
    expect(modal).toContain('href="/terminos"');
    expect(modal).toContain('href="/privacidad"');
    expect(modal).toContain("/api/cuenta/consentimiento");
    expect(leer("web/app/layout.tsx")).toContain("<ConsentimientoLegal");
  });
});
