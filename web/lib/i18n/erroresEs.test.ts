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

// Hallados al traducir a los otros idiomas (F3): el español concordaba mal con
// lo que entra por el marcador. A mano:
//   saldo = "1 crédito" -> "1 crédito disponibles" (mal); se nombra antes: "Disponible: 1 crédito".
//   sello = "hace 21 min" -> "tus cifras del hace 21 min" (mal); entre paréntesis.
describe("concordancia con lo que entra por el marcador (F3)", () => {
  it("el saldo con reserva no fuerza un plural", async () => {
    const { SALDO } = await import("./mensajes/saldo");
    expect(interpolar(SALDO.es.tituloConReserva, { saldo: "1 crédito", reservados: "2 apartados" })).toBe(
      "Disponible: 1 crédito · 2 apartados"
    );
  });
  it("el sello de las cifras no va tras 'del'", async () => {
    const { TUS_NUMEROS } = await import("./mensajes/tusNumeros");
    expect(interpolar(TUS_NUMEROS.es.calculadoConCifrasDel, { sello: "hace 21 min" })).toBe(
      "· calculado con tus cifras (hace 21 min)"
    );
  });
});

// Segunda tanda de errores del español, hallados al traducir a los otros
// nueve idiomas (F3). Ninguno cambia los marcadores (las traducciones ya los
// sortearon). Escritos a mano:
//   - "¿Cuántas veces de {{u}}…?" / "¿Cuántas de {{u}}…?": agramatical y supone
//     unidad femenina; se cuenta "por {{u}}".
//   - "Mi bitácora de mi viaje": "mi" repetido.
//   - "Tu bitacora" (nombre del archivo): sin tilde.
//   - "Tu viaje core": anglicismo en pantalla (BANCO §3); ya existe "Tu viaje principal".
//   - "planificado · adelantada": concuerda con la acción, femenino.
//   - "el cómo te fue de este mundo": "cómo te fue en este mundo".
//   - "si te pagaras…, el costo real sube": condicional, "subiría".
describe("segunda tanda de errores del español (F3)", () => {
  it("las preguntas por la unidad de venta", async () => {
    const { REPORTE } = await import("./mensajes/reporte");
    const p = REPORTE.es.preguntas as unknown as Record<string, Record<string, string>>;
    expect(interpolar(p.servicio.capacidad_semanal, { u: "sesión" })).toBe(
      "En una semana normal, ¿cuántas veces puedes atender? Cuenta cada sesión como una vez."
    );
    expect(interpolar(p.productoFisico.capacidad_semanal, { u: "pieza" })).toBe(
      "En una semana normal, ¿cuánto puedes producir, contando por pieza?"
    );
    expect(interpolar(p.digital.unidades_vendidas, { u: "licencia" })).toBe(
      "Contando por licencia, ¿cuánto tienes hoy, o cuál sería una meta mensual realista?"
    );
  });
  it("los demás", async () => {
    const { BITACORA } = await import("./mensajes/bitacora");
    const { DOCUMENTOS_RUTA } = await import("./mensajes/documentosRuta");
    const { MANOS_A_LA_OBRA } = await import("./mensajes/manosALaObra");
    const { ANALYTICS_INFORME } = await import("./mensajes/analyticsInforme");
    const { EXPEDIENTE } = await import("./mensajes/expediente");
    const { TUS_NUMEROS } = await import("./mensajes/tusNumeros");
    expect(BITACORA.es.pagina.miBitacora).toBe("La bitácora de mi viaje");
    expect(DOCUMENTOS_RUTA.es.archivoBitacora).toBe("Tu bitácora");
    expect(MANOS_A_LA_OBRA.es.nucleo.tuViajeCore).toBe("Tu viaje principal · <b>{{hechos}}/{{total}}</b>");
    expect(ANALYTICS_INFORME.es.hitos.cumplimiento).toEqual({
      a_tiempo: "planificada · a tiempo",
      adelantada: "planificada · adelantada",
      tardia: "planificada · tardía",
    });
    expect(EXPEDIENTE.es.indice.reporteSubtitulo).toBe("El plan, el avance y cómo te fue en este mundo");
    expect(TUS_NUMEROS.es.faltantes.horas_por_unidad.porque).toBe("si te pagaras el rato que tardas, el costo real subiría");
  });
});
