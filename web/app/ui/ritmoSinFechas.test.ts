// AUD-09 M38 (tanda 7B, confianza): a quien eligió avanzar a su ritmo se le
// seguía hablando de fechas: "para el …" en la fila, "Tardía · N días" y la
// sección FECHA en el detalle, sin mirar el modo (contra BANCO §3: sin fechas no
// hay plazos ni atrasos). "Hecho el …" se queda: es un dato de lo que pasó.
import { readFileSync } from "node:fs";
import path from "node:path";
import { describe, expect, it } from "vitest";

const manos = readFileSync(path.join(__dirname, "ManosALaObra.tsx"), "utf8");
const detalle = readFileSync(path.join(__dirname, "DetalleActividad.tsx"), "utf8");
const calendario = readFileSync(path.join(__dirname, "Calendario.tsx"), "utf8");

describe("a mi ritmo no se habla de plazos (AUD-09 M38)", () => {
  it("la fila solo dice 'para el …' fuera del modo a mi ritmo", () => {
    expect(manos).toMatch(/!hecho && !retirada && item\.fecha_base && modo !== "ritmo" && \(/);
  });

  it("el detalle recibe el modo y calla el chip y la fecha a mi ritmo", () => {
    expect(detalle).toMatch(/modo\?: ModoCamino \| null;/);
    expect(detalle).toMatch(/const conFechas = modo !== "ritmo";/);
    // i18n F2: el chip recibe además el idioma de la interfaz (sus textos salen del catálogo).
    expect(detalle).toMatch(/const chip = conFechas \? chipCumplimiento\(item, idioma\) : null;/);
    expect(detalle).toMatch(/\{conFechas && item\.fecha_base && \(/);
  });

  it("quien abre el detalle le pasa el modo de su espacio", () => {
    expect(manos).toMatch(/<DetalleActividad[\s\S]{0,120}modo=\{esEspacioCore\(vivo\.dominio\) \? modoCamino : modoDeMundo\(vivo\.dominio\)\}/);
    expect(calendario).toMatch(/<DetalleActividad[\s\S]{0,80}modo="fechas"/);
  });
});
