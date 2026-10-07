// La puerta del mini-gate comprueba quién eres (encargo del fundador del 6 oct 2026, punto 7c; la auditoría de
// promesas públicas encontró que ?ver=ocultos no lo comprobaba: cualquiera con el enlace abría un mundo sin publicar).
// Ahora la URL solo pide; el servidor decide: los mundos ocultos se ven y se abren solo con una cuenta real cuyo
// correo está en FUNDADOR_EMAILS (variable de entorno, nunca en el código).
import { readFileSync } from "node:fs";
import { join } from "node:path";
import { afterEach, describe, expect, it } from "vitest";
import { mundoAlcanzable, puedeVerOcultos } from "./fundador";
import { MUNDOS } from "./catalogoMundos";

const leer = (ruta: string) => readFileSync(join(__dirname, "..", ruta), "utf-8");
const ORIGINAL = process.env.FUNDADOR_EMAILS;
afterEach(() => {
  if (ORIGINAL === undefined) delete process.env.FUNDADOR_EMAILS;
  else process.env.FUNDADOR_EMAILS = ORIGINAL;
});

describe("puedeVerOcultos", () => {
  it("sin usuario, invitado invisible o sin la variable: nadie", () => {
    process.env.FUNDADOR_EMAILS = "dueno@ejemplo.com";
    expect(puedeVerOcultos(null)).toBe(false);
    expect(puedeVerOcultos({ is_anonymous: true, email: "dueno@ejemplo.com" })).toBe(false);
    expect(puedeVerOcultos({ is_anonymous: false, email: "x@invitado.my-idea.local" })).toBe(false);
    delete process.env.FUNDADOR_EMAILS;
    expect(puedeVerOcultos({ is_anonymous: false, email: "dueno@ejemplo.com" })).toBe(false);
  });

  it("una cuenta real en la lista, sin importar mayúsculas ni espacios", () => {
    process.env.FUNDADOR_EMAILS = " otra@ejemplo.com , Dueno@Ejemplo.com";
    expect(puedeVerOcultos({ is_anonymous: false, email: "dueno@ejemplo.com" })).toBe(true);
    expect(puedeVerOcultos({ is_anonymous: false, email: "alguien@ejemplo.com" })).toBe(false);
  });
});

describe("mundoAlcanzable", () => {
  it("un mundo publicado lo alcanza cualquiera; uno oculto, solo quien puede verlo", () => {
    process.env.FUNDADOR_EMAILS = "dueno@ejemplo.com";
    const publicado = MUNDOS.find((m) => !m.oculto)!;
    const oculto = MUNDOS.find((m) => m.oculto);
    const nadie = { is_anonymous: false, email: "alguien@ejemplo.com" };
    const dueno = { is_anonymous: false, email: "dueno@ejemplo.com" };
    expect(mundoAlcanzable(publicado.clave, nadie)).toBe(true);
    expect(mundoAlcanzable("no_existe", dueno)).toBe(false);
    if (oculto) {
      expect(mundoAlcanzable(oculto.clave, nadie)).toBe(false);
      expect(mundoAlcanzable(oculto.clave, dueno)).toBe(true);
    }
  });
});

describe("la puerta se cumple en el servidor", () => {
  it("las tres rutas que abren un mundo rechazan uno oculto a quien no puede verlo", () => {
    for (const r of ["diagnostico", "start", "unlock"]) {
      expect(leer(`app/api/project/[id]/world/[pack]/${r}/route.ts`), r).toContain("mundoAlcanzable(pack, user)");
    }
  });

  it("la vista solo enciende la puerta si el servidor dice que puedes", () => {
    expect(leer("app/api/idea/[id]/route.ts")).toContain("puedeVerOcultos(user)");
    expect(leer("app/idea/[id]/IdeaView.tsx")).toContain("detalle?.puedeVerOcultos === true");
  });
});
