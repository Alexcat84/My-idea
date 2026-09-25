// i18n F3, decisión del fundador (24 sep 2026): la tanda de errores del español
// de F2_INFORME.md que no son tildes (esas las vigila ortografiaEs.test.ts):
// plurales mal armados e inconsistencias. Cada texto esperado está escrito a
// mano, con la regla que lo corrige al lado.
import { describe, expect, it } from "vitest";
import { formaPlural, interpolar } from "./interpolar";
import { LOGIN, CLAVE_NUEVA } from "./mensajes/acceso";
import { CALENDARIO } from "./mensajes/calendario";
import { CREDITOS } from "./mensajes/creditos";
import { DESCARGAS } from "./mensajes/descargas";
import { DOCUMENTOS_RUTA } from "./mensajes/documentosRuta";
import { MIS_IDEAS } from "./mensajes/misIdeas";
import { PORTADA } from "./mensajes/portada";
import { LARGO_MINIMO } from "../password";

describe("plurales del español (tanda de F2)", () => {
  it("'Quedan 1 acciones' -> 'Queda 1 acción … sigue'; con 3, como antes", () => {
    const t = DOCUMENTOS_RUTA.es;
    expect(interpolar(formaPlural("es", 1, t.loQuePendiente), { n: 1 })).toBe(
      "Queda 1 acción por delante. Nada se borró: sigue en tu expediente."
    );
    expect(interpolar(formaPlural("es", 3, t.loQuePendiente), { n: 3 })).toBe(
      "Quedan 3 acciones por delante. Nada se borró: siguen en tu expediente."
    );
    // con retiradas siempre hay al menos dos cosas guardadas: "siguen"
    expect(interpolar(formaPlural("es", 1, t.loQuePendienteConRetiradas), { n: 1, retiradas: 2 })).toBe(
      "Queda 1 acción por delante y 2 que retiraste con su motivo. Nada se borró: siguen en tu expediente."
    );
  });
  it("'1 días de la chispa' -> '1 día'", () => {
    const t = MIS_IDEAS.es.cintas.resumenRealizada;
    expect(interpolar(formaPlural("es", 1, t), { fecha: "hoy", dias: 1 })).toBe("realizada hoy · 1 día de la chispa al proyecto");
    expect(interpolar(formaPlural("es", 12, t), { fecha: "hoy", dias: 12 })).toBe("realizada hoy · 12 días de la chispa al proyecto");
  });
  it("'Una fecha ya pasó… Puedes moverlas' -> 'moverla'", () => {
    expect(CALENDARIO.es.bandaVencidas.one).toBe("Una fecha ya pasó y sigue abierta. Puedes moverla al día que te sirva.");
  });
});

describe("inconsistencias del español (tanda de F2)", () => {
  it("puntos suspensivos con el carácter de la casa", () => {
    expect(DESCARGAS.es.preparando).toBe("Preparando…");
    expect(DESCARGAS.es.cargando).toBe("Cargando…");
  });
  it("el título de la portada va en minúscula tras los dos puntos, igual que el h1", () => {
    expect(PORTADA.es.meta.titulo).toBe("My Idea: transforma tu creatividad en acción");
    expect(PORTADA.es.meta.titulo).toBe(PORTADA.es.tituloOculto);
  });
  it("el largo mínimo de la contraseña sale de la regla (password.ts), no de un 8 escrito a mano", () => {
    for (const texto of [LOGIN.es.reglasContrasena, CLAVE_NUEVA.es.reglas]) {
      expect(texto).not.toMatch(/\d/);
      expect(interpolar(texto, { n: LARGO_MINIMO })).toBe("Al menos 8 caracteres, una mayúscula y un número.");
    }
  });
  it("una sola redacción del enlace vencido (cambia solo a dónde ir a pedir otro)", () => {
    expect(LOGIN.es.enlaceVencido.startsWith("Ese enlace ya venció o ya se usó.")).toBe(true);
    expect(CLAVE_NUEVA.es.enlaceVencido.startsWith("Ese enlace ya venció o ya se usó.")).toBe(true);
  });
  it("'No pude leer tu saldo' -> 'No pudimos' (la casa habla en plural)", () => {
    expect(CREDITOS.es.heroe.noPudeLeer.startsWith("No pudimos leer tu saldo")).toBe(true);
  });
  it("el aviso de beta privada sin la frase forzada", () => {
    expect(LOGIN.es.noInvitado.texto).toBe(
      "Ese correo aún no está en la lista de invitados (es la misma lista para entrar con contraseña o con Google). Si alguien te invitó, pídele que confirme el correo que registró."
    );
  });
  it("el año del pie no está fijo", () => {
    expect(PORTADA.es.pie.derechos).toBe("© {{ano}} My Idea");
  });
});
