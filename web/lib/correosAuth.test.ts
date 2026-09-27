// i18n F6 (D4): los correos de Supabase Auth por el Send Email Hook. Cada caso
// está calculado a mano ANTES del assert (AGENTS.md): la firma con el vector de
// prueba publicado por Standard Webhooks, los enlaces con el formato que
// documenta Supabase y los destinatarios con su tabla del cambio de correo.
import { readFileSync } from "node:fs";
import path from "node:path";
import { describe, expect, it } from "vitest";
import { CORREOS_AUTH } from "./i18n/mensajes/correosAuth";
import {
  armarCorreos,
  enlaceDeAccion,
  idiomaDelUsuario,
  verificarFirmaHook,
  type PayloadHook,
} from "./correosAuth";

// Vector de prueba de la especificación Standard Webhooks (el mismo que usan
// sus librerías oficiales): secreto, id, marca de tiempo, cuerpo y firma
// esperada. No sale de esta implementación: es un dato externo.
const VECTOR = {
  secreto: "whsec_MfKQ9r8GKYqrTwjUPD8ILPZIo2LaLaSw",
  id: "msg_p5jXN8AQM9LWM0D4loKWxJek",
  timestamp: "1614265330",
  cuerpo: '{"test": 2432232314}',
  firma: "v1,g0hM9SsE+OTPJTGt/tmIKtSyZlE3uFJELVlNIOLJ1OE=",
};
const AHORA_VECTOR = 1614265330 * 1000;

function cabeceras(extra: Partial<Record<"webhook-id" | "webhook-timestamp" | "webhook-signature", string>> = {}) {
  return new Headers({
    "webhook-id": VECTOR.id,
    "webhook-timestamp": VECTOR.timestamp,
    "webhook-signature": VECTOR.firma,
    ...extra,
  });
}

describe("la firma del hook (Standard Webhooks)", () => {
  it("acepta el vector publicado, con el secreto tal como lo da Supabase (v1,whsec_…)", () => {
    expect(verificarFirmaHook(VECTOR.cuerpo, cabeceras(), `v1,${VECTOR.secreto}`, AHORA_VECTOR)).toBe(true);
  });

  it("acepta también el secreto sin el prefijo v1,", () => {
    expect(verificarFirmaHook(VECTOR.cuerpo, cabeceras(), VECTOR.secreto, AHORA_VECTOR)).toBe(true);
  });

  it("acepta si una de varias firmas separadas por espacio es la buena", () => {
    const h = cabeceras({ "webhook-signature": `v1,AAAA ${VECTOR.firma}` });
    expect(verificarFirmaHook(VECTOR.cuerpo, h, VECTOR.secreto, AHORA_VECTOR)).toBe(true);
  });

  it("rechaza un cuerpo alterado", () => {
    expect(verificarFirmaHook('{"test": 2432232315}', cabeceras(), VECTOR.secreto, AHORA_VECTOR)).toBe(false);
  });

  it("rechaza otro secreto", () => {
    expect(verificarFirmaHook(VECTOR.cuerpo, cabeceras(), "whsec_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA", AHORA_VECTOR)).toBe(false);
  });

  it("rechaza sin cabeceras de firma", () => {
    expect(verificarFirmaHook(VECTOR.cuerpo, new Headers(), VECTOR.secreto, AHORA_VECTOR)).toBe(false);
    expect(verificarFirmaHook(VECTOR.cuerpo, cabeceras({ "webhook-signature": "" }), VECTOR.secreto, AHORA_VECTOR)).toBe(false);
  });

  it("rechaza una marca de tiempo fuera de los 5 minutos (repetición)", () => {
    // 1614265330 + 301 s: pasa la tolerancia de 300 s.
    expect(verificarFirmaHook(VECTOR.cuerpo, cabeceras(), VECTOR.secreto, (1614265330 + 301) * 1000)).toBe(false);
    // 299 s: dentro.
    expect(verificarFirmaHook(VECTOR.cuerpo, cabeceras(), VECTOR.secreto, (1614265330 + 299) * 1000)).toBe(true);
  });

  it("rechaza un secreto vacío (falla cerrada)", () => {
    expect(verificarFirmaHook(VECTOR.cuerpo, cabeceras(), "", AHORA_VECTOR)).toBe(false);
  });
});

describe("el idioma del correo", () => {
  it("la preferencia guardada en user_metadata.idioma", () => {
    expect(idiomaDelUsuario({ user_metadata: { idioma: "ko" } })).toBe("ko");
    expect(idiomaDelUsuario({ user_metadata: { idioma: "ar" } })).toBe("ar");
  });
  it("sin preferencia o con una desconocida, español", () => {
    expect(idiomaDelUsuario({ user_metadata: { idioma: "xx" } })).toBe("es");
    expect(idiomaDelUsuario({ user_metadata: {} })).toBe("es");
    expect(idiomaDelUsuario({})).toBe("es");
  });
});

describe("el enlace de cada acción", () => {
  it("signup: {SUPABASE_URL}/auth/v1/verify?token=…&type=signup&redirect_to=… (URLSearchParams)", () => {
    // A mano: ":" → %3A y "/" → %2F dentro de redirect_to.
    expect(
      enlaceDeAccion({
        supabaseUrl: "https://abc.supabase.co/",
        tokenHash: "pkce_123",
        tipo: "signup",
        redirectTo: "https://www.myideaproject.com/auth/callback",
        siteUrl: "https://www.myideaproject.com",
      })
    ).toBe(
      "https://abc.supabase.co/auth/v1/verify?token=pkce_123&type=signup&redirect_to=https%3A%2F%2Fwww.myideaproject.com%2Fauth%2Fcallback"
    );
  });

  it("recovery conserva el ?type=recovery del redirect (? → %3F, = → %3D)", () => {
    expect(
      enlaceDeAccion({
        supabaseUrl: "https://abc.supabase.co",
        tokenHash: "h",
        tipo: "recovery",
        redirectTo: "https://www.myideaproject.com/auth/callback?type=recovery",
        siteUrl: "https://www.myideaproject.com",
      })
    ).toBe(
      "https://abc.supabase.co/auth/v1/verify?token=h&type=recovery&redirect_to=https%3A%2F%2Fwww.myideaproject.com%2Fauth%2Fcallback%3Ftype%3Drecovery"
    );
  });

  it("sin redirect_to, vuelve al site_url", () => {
    expect(
      enlaceDeAccion({ supabaseUrl: "https://abc.supabase.co", tokenHash: "h", tipo: "magiclink", redirectTo: "", siteUrl: "https://www.myideaproject.com" })
    ).toBe("https://abc.supabase.co/auth/v1/verify?token=h&type=magiclink&redirect_to=https%3A%2F%2Fwww.myideaproject.com");
  });
});

function payload(tipo: string, extra: Partial<PayloadHook["email_data"]> = {}, user: Partial<PayloadHook["user"]> = {}): PayloadHook {
  return {
    user: { id: "u1", email: "ana@example.com", user_metadata: { idioma: "ko" }, ...user },
    email_data: {
      token: "305805",
      token_hash: "hash_a",
      redirect_to: "https://www.myideaproject.com/auth/callback",
      email_action_type: tipo,
      site_url: "https://www.myideaproject.com",
      token_new: "",
      token_hash_new: "",
      old_email: "",
      ...extra,
    },
  };
}
const SB = "https://abc.supabase.co";

describe("los correos que arma el hook", () => {
  it("signup en coreano: asunto del catálogo, enlace en el html con & escapado, lang=ko", () => {
    const [c, ...resto] = armarCorreos(payload("signup"), SB);
    expect(resto).toEqual([]);
    expect(c.para).toBe("ana@example.com");
    expect(c.asunto).toBe(CORREOS_AUTH.ko.registro.asunto);
    const enlace = `${SB}/auth/v1/verify?token=hash_a&type=signup&redirect_to=https%3A%2F%2Fwww.myideaproject.com%2Fauth%2Fcallback`;
    expect(c.texto).toContain(enlace);
    expect(c.texto).toContain(CORREOS_AUTH.ko.registro.cuerpo);
    expect(c.html).toContain(enlace.replaceAll("&", "&amp;"));
    expect(c.html).toContain('lang="ko"');
    expect(c.html).toContain('dir="ltr"');
    // signup no lleva el código de 6 cifras (la plantilla de hoy es solo el enlace)
    expect(c.texto).not.toContain("305805");
  });

  it("en árabe el html va de derecha a izquierda", () => {
    const [c] = armarCorreos(payload("recovery", {}, { user_metadata: { idioma: "ar" } }), SB);
    expect(c.asunto).toBe(CORREOS_AUTH.ar.recuperar.asunto);
    expect(c.html).toContain('dir="rtl"');
    expect(c.html).toContain('lang="ar"');
  });

  it("sin idioma guardado, el correo sale en español", () => {
    const [c] = armarCorreos(payload("signup", {}, { user_metadata: {} }), SB);
    expect(c.asunto).toBe("Confirma tu correo en My Idea");
  });

  it("invite y magiclink usan su plantilla y su type", () => {
    const [i] = armarCorreos(payload("invite"), SB);
    expect(i.asunto).toBe(CORREOS_AUTH.ko.invitacion.asunto);
    expect(i.texto).toContain("type=invite");
    const [m] = armarCorreos(payload("magiclink"), SB);
    expect(m.asunto).toBe(CORREOS_AUTH.ko.enlaceEntrar.asunto);
    expect(m.texto).toContain("type=magiclink");
    // el enlace para entrar lleva también el código: 305805
    expect(m.texto).toContain("305805");
  });

  it("cambio de correo seguro: dos correos, token_hash_new al actual y token_hash al nuevo (la tabla de Supabase)", () => {
    const correos = armarCorreos(
      payload("email_change", { token_hash: "H_NUEVO", token_hash_new: "H_ACTUAL", token_new: "111111" }, { new_email: "ana.nueva@example.com" }),
      SB
    );
    expect(correos.map((c) => c.para)).toEqual(["ana@example.com", "ana.nueva@example.com"]);
    expect(correos[0].texto).toContain("token=H_ACTUAL&type=email_change");
    expect(correos[0].asunto).toBe(CORREOS_AUTH.ko.cambioCorreoActual.asunto);
    expect(correos[0].texto).toContain("ana.nueva@example.com");
    expect(correos[1].texto).toContain("token=H_NUEVO&type=email_change");
    expect(correos[1].asunto).toBe(CORREOS_AUTH.ko.cambioCorreoNuevo.asunto);
  });

  it("cambio de correo sin la opción segura: un solo correo, al nuevo, con token_hash", () => {
    const correos = armarCorreos(payload("email_change", { token_hash: "H" }, { new_email: "b@example.com" }), SB);
    expect(correos.map((c) => c.para)).toEqual(["b@example.com"]);
    expect(correos[0].texto).toContain("token=H&type=email_change");
  });

  it("reautenticación: el código de 6 cifras, sin enlace", () => {
    const [c] = armarCorreos(payload("reauthentication", { token: "424242", token_hash: "" }), SB);
    expect(c.asunto).toBe(CORREOS_AUTH.ko.reautenticacion.asunto);
    expect(c.texto).toContain("424242");
    expect(c.html).toContain("424242");
    expect(c.texto).not.toContain("/auth/v1/verify");
  });

  it("el aviso de correo cambiado va al correo anterior", () => {
    const [c] = armarCorreos(payload("email_changed_notification", { old_email: "vieja@example.com" }), SB);
    expect(c.para).toBe("vieja@example.com");
    expect(c.asunto).toBe(CORREOS_AUTH.ko.avisos.correoCambiado.asunto);
    expect(c.texto).toContain(CORREOS_AUTH.ko.avisos.notaSeguridad);
  });

  it("cada aviso de seguridad tiene su plantilla", () => {
    const tabla: [string, string][] = [
      ["password_changed_notification", CORREOS_AUTH.es.avisos.contrasenaCambiada.asunto],
      ["phone_changed_notification", CORREOS_AUTH.es.avisos.telefonoCambiado.asunto],
      ["identity_linked_notification", CORREOS_AUTH.es.avisos.accesoVinculado.asunto],
      ["identity_unlinked_notification", CORREOS_AUTH.es.avisos.accesoDesvinculado.asunto],
      ["mfa_factor_enrolled_notification", CORREOS_AUTH.es.avisos.verificacionAgregada.asunto],
      ["mfa_factor_unenrolled_notification", CORREOS_AUTH.es.avisos.verificacionQuitada.asunto],
    ];
    for (const [tipo, asunto] of tabla) {
      const [c] = armarCorreos(payload(tipo, {}, { user_metadata: {} }), SB);
      expect(c.asunto).toBe(asunto);
    }
  });

  it("un tipo desconocido lanza (fallar ruidoso, nunca un correo vacío)", () => {
    expect(() => armarCorreos(payload("algo_nuevo"), SB)).toThrow(/algo_nuevo/);
  });

  it("sin destinatario lanza", () => {
    expect(() => armarCorreos(payload("signup", {}, { email: "" }), SB)).toThrow();
  });

  it("escapa lo que viene del payload en el html", () => {
    const [c] = armarCorreos(
      payload("email_change", { token_hash_new: "X" }, { email: "a<b>@example.com", new_email: 'n"@example.com' }),
      SB
    );
    expect(c.html).not.toContain("a<b>");
    expect(c.html).toContain("a&lt;b&gt;@example.com");
  });
});

describe("ningún secreto en el código", () => {
  it("el hook lee el secreto del entorno y no trae ninguno escrito", () => {
    const raiz = path.join(__dirname, "..");
    for (const archivo of ["lib/correosAuth.ts", "app/api/auth/hook-correo/route.ts"]) {
      const fuente = readFileSync(path.join(raiz, archivo), "utf8");
      expect(fuente).not.toMatch(/whsec_[A-Za-z0-9+/=]{8,}/);
      expect(fuente).not.toMatch(/re_[A-Za-z0-9]{16,}/);
    }
    const ruta = readFileSync(path.join(raiz, "app/api/auth/hook-correo/route.ts"), "utf8");
    expect(ruta).toContain("process.env.SEND_EMAIL_HOOK_SECRET");
  });
});
