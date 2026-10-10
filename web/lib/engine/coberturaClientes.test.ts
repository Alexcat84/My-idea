/**
 * "Lo que este plan aún no cubre: validar con clientes reales" solo cuando las ETAPAS de verdad no validan con clientes
 * (decision del fundador, 9 oct 2026). Segunda medicion A/B: la frase fija salio en 11 de 14 planes y el arbitro la
 * sostuvo como contrario en planes cuyas etapas mandan hablar con clientes, entregar una primera version a los primeros
 * usuarios o probar el precio con compradores. coberturaContraEtapas solo miraba los nodos autodeclarados por etapa y los
 * encabezados; ahora mira tambien las acciones de las etapas. Casos reales (extractos de los planes de la medicion,
 * docs/corrida_final/2026-10-08/medicion_ab2/A/).
 */
import { describe, expect, it } from "vitest";
import { coberturaContraEtapas, validaConClientesEnEtapas } from "./planRedactor";
import { textosFamiliaFaltante } from "./constants";

const FRASE = textosFamiliaFaltante("es").accion_clientes;
const ECON = textosFamiliaFaltante("es").viabilidad_economica;

const sinAccion = {
  es_completa: false,
  tiene_accion_clientes: false,
  tiene_viabilidad_economica: true,
  familias_faltantes: [FRASE],
};

function faltantesCon(cuerpo: string): string[] {
  return coberturaContraEtapas(sinAccion, { familias_tratadas: [], etapas: {} } as never, new Set(), {}, cuerpo, "es").familias_faltantes;
}

// Plan ee6de956 (núcleo, app de gastos): sostenido como contrario por el árbitro.
const EE6DE956 = `# Tu app de registro de gastos: descubre si alguien pagará cada mes y se quedará

Tienes una app de suscripción mensual para llevar el registro de gastos personales y todavía ningún cliente ha pagado.

## Etapa 1: Pon por escrito lo que das por cierto sin haberlo comprobado

1. Escribe las suposiciones que sostienen tu idea.

## Etapa 2: Sal a hablar con personas que podrían usarla

1. Toma las suposiciones más riesgosas de la etapa 1 y conviértelas en preguntas para clientes potenciales.
2. Habla con personas que llevan o intentan llevar el control de sus gastos personales.

## Etapa 4: Lanza a un grupo pequeño y mide lo que hacen, no lo que dicen

1. Lanza tu primera versión, funcional o simulada, a unos pocos usuarios dispuestos a probar cosas nuevas.

## ¿Puede sostenerse tu idea? Los números en simple

- **Costo:** lo que te cuesta cada mes.`;

// Plan 9909f451 (núcleo): sostenido como contrario por el árbitro.
const P9909F451 = `# Plan para validar tu app de suscripción de gastos personales

Todavía no has hablado con usuarios reales, así que este plan empieza por comprobar que el problema existe.

## Etapa 1: Descubre cómo registra gastos la gente hoy

2. Sal a hablar con personas que llevan o intentan llevar sus gastos, de forma repetida durante varias semanas, y pregúntales qué hacen hoy y qué otras soluciones usan.

## Etapa 4: Prueba una versión mínima con tus primeros usuarios

3. Entrégala a tus primeros usuarios, los del grupo visionario de la etapa 2, no a un público masivo.`;

// Plan aad2749d (núcleo, macetas, ya vende): sostenido como contrario por el árbitro.
const AAD2749D = `# Tu precio de 250 con costo real de 130: de comprobar el margen a decidir tu rumbo

## Etapa 1: Cierra tu costo real y tu ganancia por maceta

1. Suma lo que gastas en materiales por pieza.

## Etapa 4: Confirma que el precio de 250 se sostiene y mide el canal de la tienda

1. Escribe de antemano qué resultado te bastaría para quedarte con el precio de 250 (por ejemplo, cuántos compradores de un grupo pequeño lo aceptan).
2. Revisa si tus compradores por Instagram siguen comprando a 250 y registra no solo si compran, sino lo que dicen sobre el precio.
5. Mira si la feria local de agosto te sirve para probar el precio con compradores nuevos, cambiando solo eso.`;

// Plan 85248377 (Salud y Seguridad): habla con sus EMPLEADOS, no con clientes. La frase es verdad y se queda.
const P85248377 = `# Protege tu salud y la de tu taller de macetas sin frenar la producción

Trabajas todos los días con cemento y polvo sin mascarilla ni guantes adecuados.

## Etapa 3: Controla cada peligro empezando por lo más efectivo

1. Para cada peligro prioritario, pregúntate en este orden: ¿puedo eliminarlo?, ¿puedo cambiar el material?

## Etapa 4: Habla con tus dos empleados sobre la protección

3. Pregúntales qué les incomoda del equipo de protección y qué ajuste les ayudaría a trabajar con él sin perder ritmo.`;

// Solo la introducción habla de clientes; ninguna etapa los toca: la frase se queda.
const SOLO_INTRO = `# Ordena tu taller

Tus clientes te piden más rapidez y quieres hablar con tus compradores más adelante.

## Etapa 1: Ordena tus herramientas

1. Pon cada herramienta en su sitio.

## Lo que este plan aún no cubre

- validar con clientes reales (conversaciones, una primera versión sencilla de tu producto, pruebas con usuarios, una venta o preventa real)`;

describe("la frase de validar con clientes solo sale si las etapas de verdad no validan con clientes", () => {
  it.each([
    ["ee6de956 (habla con personas que llevan sus gastos; lanza la primera versión a usuarios)", EE6DE956],
    ["9909f451 (pregúntales a las personas; entrégala a tus primeros usuarios)", P9909F451],
    ["aad2749d (probar el precio con compradores nuevos)", AAD2749D],
  ])("caso real %s: las etapas validan con clientes y la frase NO sale", (_caso, cuerpo) => {
    expect(validaConClientesEnEtapas(cuerpo)).toBe(true);
    expect(faltantesCon(cuerpo)).not.toContain(FRASE);
  });

  it("caso real 85248377: habla con sus empleados, no con clientes, y la frase SE QUEDA", () => {
    expect(validaConClientesEnEtapas(P85248377)).toBe(false);
    expect(faltantesCon(P85248377)).toContain(FRASE);
  });

  it("los clientes solo en la introducción no cuentan: la frase SE QUEDA", () => {
    expect(validaConClientesEnEtapas(SOLO_INTRO)).toBe(false);
    expect(faltantesCon(SOLO_INTRO)).toContain(FRASE);
  });

  it("nunca toca la otra familia: si falta la viabilidad económica, sigue faltando", () => {
    const r = coberturaContraEtapas(
      { es_completa: false, tiene_accion_clientes: false, tiene_viabilidad_economica: false, familias_faltantes: [FRASE, ECON] },
      { familias_tratadas: [], etapas: {} } as never,
      new Set(),
      {},
      EE6DE956.replace(/## ¿Puede sostenerse[\s\S]*$/, ""),
      "es"
    );
    expect(r.familias_faltantes).toEqual([ECON]);
    expect(r.tiene_accion_clientes).toBe(true);
    expect(r.es_completa).toBe(false);
  });
});
