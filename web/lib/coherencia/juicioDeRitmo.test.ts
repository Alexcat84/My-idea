// CONTROL DEL MODO "A MI RITMO" (FLUJO_TRACKING §3; decision del fundador, corrida final, 8 oct 2026).
// En "a mi ritmo" esta PROHIBIDO juzgar la puntualidad del propio usuario frente a su plan ("vas atrasado", "no
// llegaste a tiempo", "vas por delante"). Esta PERMITIDO "a tiempo" como consejo de negocio (entregar a tiempo a los
// clientes, pagar a tiempo a los proveedores).
// Origen: el vuelo del 8 oct paro en 2j porque el control buscaba la expresion suelta "a tiempo" y el plan decia
// "...para detectar el defecto a tiempo" (consejo de calidad, inocente). El control debe cazar el JUICIO sobre el ritmo
// del usuario, no la expresion.
import { describe, expect, it } from "vitest";
import { juiciosDeRitmo } from "./juicioDeRitmo";

describe("inocente: 'a tiempo' y los retrasos como consejo de negocio no son juicio", () => {
  it.each([
    // la frase real del plan del vuelo (8 oct 2026, plan 738cba1f)
    "Decide qué paso de tu proceso revisarías antes de hornear para detectar el defecto a tiempo.",
    "Entrega a tiempo a tus clientes los pedidos de diciembre.",
    "Págale a tiempo a tu proveedor de cemento para no perder el descuento.",
    "Eso toma tiempo, y está bien.",
    "Compara cuál te deja más margen contando el riesgo de atrasos.",
    "También pesan los rechazos, los retrasos y el material que no sale bien.",
    "Suma al precio lo que te cuesta usarlo: piezas que salen mal, retrasos de entrega.",
    "Este plan parte de eso y asume que avanzas a tu ritmo, sin fechas.",
    "Pídele que te confirme desde qué fecha aplica el precio nuevo.",
    "Llevas tarde en el horno las piezas grandes: déjalas enfriar.",
  ])("%s", (frase) => {
    expect(juiciosDeRitmo(frase)).toEqual([]);
  });
});

describe("violacion: juzgar la puntualidad del usuario frente a su plan", () => {
  it.each([
    "Vas atrasado con las tareas de la etapa 2.",
    "No llegaste a tiempo con el cálculo de costos.",
    "Vas por delante de tu plan: sigue así.",
    "Llevas cinco días de retraso.",
    "Retoma tus tareas atrasadas antes de empezar otras.",
    "Terminaste tarde la etapa de precios.",
    "Estás adelantada respecto a lo que te propusiste.",
    "Cumpliste a tiempo dos de tus tres acciones.",
    "Tu puntualidad ha mejorado este mes.",
    "Tuviste una desviación de tres días contra tus fechas.",
    "Una de tus acciones quedó tardía.",
  ])("%s", (frase) => {
    expect(juiciosDeRitmo(frase).length).toBeGreaterThan(0);
  });
});
