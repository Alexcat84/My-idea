/**
 * Pruebas de la logica pura de la masa: ciclo, encuadre, niveles y
 * figuras. Cada valor esperado sale del calculo a mano del comentario,
 * no de correr la funcion (AGENTS.md).
 */
import { describe, expect, it } from "vitest";
import { MedidorFps, nivelInicial, siguienteNivel, type PistasEquipo } from "./calidad";
import { DURACION_CICLO, estadoEn, estadoEnCiclo, FASES, figuraEn, MOMENTOS, suavizar } from "./ciclo";
import {
  distanciaCamara,
  ENVOLTURA_PIEL,
  FOV_GRADOS,
  pixelesPorUnidad,
  RADIO_LIMITE,
  RADIO_MASA,
  TAMANO_FIGURA,
} from "./encuadre";
import { azarSembrado, normalizarPuntos } from "./figuras";

describe("ciclo", () => {
  it("dura 9.8 s: 3.4 reposo + 1.9 disgrega + 2.6 forma + 1.9 regresa", () => {
    // 3.4 + 1.9 + 2.6 + 1.9 = 9.8
    expect(DURACION_CICLO).toBeCloseTo(9.8, 10);
  });

  it("en reposo: masa completa y ninguna particula fuera", () => {
    expect(estadoEnCiclo(1.7)).toEqual({ liquido: 1, mezcla: 0 });
  });

  it("a mitad de la disgregacion: la masa a medias y la mitad del viaje", () => {
    // b = 0.5; liquido = 1 - suavizar(0.55); suavizar(0.55) = 0.55^2 * (3 - 1.1)
    //   = 0.3025 * 1.9 = 0.57475  ->  liquido = 0.42525
    // mezcla = suavizar(0.5) = 0.25 * 2 = 0.5
    const e = estadoEnCiclo(MOMENTOS.mitadDisgregacion);
    expect(e.liquido).toBeCloseTo(0.42525, 5);
    expect(e.mezcla).toBeCloseTo(0.5, 5);
  });

  it("con la figura formada: sin masa y todas las particulas en la figura", () => {
    expect(estadoEnCiclo(MOMENTOS.figuraFormada)).toEqual({ liquido: 0, mezcla: 1 });
  });

  it("es continuo en cada cambio de fase y al cerrar el ciclo (sin cortes)", () => {
    const bordes = [
      FASES.reposo,
      FASES.reposo + FASES.disgrega,
      FASES.reposo + FASES.disgrega + FASES.forma,
      DURACION_CICLO,
    ];
    for (const b of bordes) {
      const antes = estadoEn(b - 1e-6);
      const despues = estadoEn(b + 1e-6);
      expect(Math.abs(antes.liquido - despues.liquido)).toBeLessThan(1e-3);
      expect(Math.abs(antes.mezcla - despues.mezcla)).toBeLessThan(1e-3);
    }
  });

  it("forma las cinco figuras en su orden y vuelve a empezar", () => {
    // ciclo k = floor(t / 9.8); figura = k mod 5
    expect(figuraEn(0)).toBe(0); // foco
    expect(figuraEn(9.8 * 1.5)).toBe(1); // lente
    expect(figuraEn(9.8 * 2.5)).toBe(2); // brujula
    expect(figuraEn(9.8 * 3.5)).toBe(3); // escalera
    expect(figuraEn(9.8 * 4.5)).toBe(4); // casa
    expect(figuraEn(9.8 * 5.5)).toBe(0); // foco otra vez
  });

  it("suavizar recorta fuera de [0, 1]", () => {
    expect(suavizar(-2)).toBe(0);
    expect(suavizar(3)).toBe(1);
  });
});

describe("encuadre: centrada y al 80 % del lado menor", () => {
  it("escritorio 1440 x 836: la figura mide 0.8 x 836 = 668.8 px", () => {
    // tan(15 grados) = 0.267949; d = 3 / (0.8 * 2 * 0.267949) = 6.99760
    // px por unidad = 836 / (2 * 6.99760 * 0.267949) = 836 / 3.75 = 222.93
    // 3.0 unidades * 222.93 = 668.8 = 0.8 * 836
    expect(FOV_GRADOS).toBe(30);
    expect(distanciaCamara(1440, 836)).toBeCloseTo(6.9976, 3);
    expect(TAMANO_FIGURA * pixelesPorUnidad(1440, 836)).toBeCloseTo(668.8, 1);
  });

  it("movil vertical 390 x 780: la figura mide 0.8 x 390 = 312 px", () => {
    // aspecto 0.5; d = 3 / (0.8 * 2 * 0.267949 * 0.5) = 13.9952
    // px por unidad = 780 / (2 * 13.9952 * 0.267949) = 780 / 7.5 = 104
    // 3.0 * 104 = 312 = 0.8 * 390
    expect(distanciaCamara(390, 780)).toBeCloseTo(13.9952, 3);
    expect(TAMANO_FIGURA * pixelesPorUnidad(390, 780)).toBeCloseTo(312, 1);
  });

  it("nada se recorta: el limite es 96 % del lado menor y la piel cabe dentro aun en perspectiva", () => {
    // RADIO_LIMITE = 0.48 / 0.8 * 3.0 = 1.8 -> diametro 3.6 -> 3.6 / 3.0 * 0.8 = 0.96 del lado menor
    expect(RADIO_LIMITE).toBeCloseTo(1.8, 10);
    // piel maxima 1.36 + 0.30 = 1.66; su silueta vista a distancia d se agranda
    // r * d / sqrt(d^2 - r^2). Escritorio (d = 6.9976): 1.66 * 6.9976 / 6.7979 = 1.7088 < 1.8
    const r = RADIO_MASA + ENVOLTURA_PIEL;
    for (const [w, h] of [[1440, 836], [768, 1024], [390, 780]] as const) {
      const d = distanciaCamara(w, h);
      const silueta = (r * d) / Math.sqrt(d * d - r * r);
      expect(silueta).toBeLessThan(RADIO_LIMITE);
      expect(2 * silueta * pixelesPorUnidad(w, h)).toBeLessThan(Math.min(w, h));
    }
  });
});

describe("niveles de calidad", () => {
  const base: PistasEquipo = { webgl: true, webgl2: true, movil: false, nucleos: 8, memoriaGb: 8 };

  it("escritorio arranca en alto y movil en medio", () => {
    expect(nivelInicial(base)).toBe("alto");
    expect(nivelInicial({ ...base, movil: true })).toBe("medio");
  });

  it("sin WebGL2 o por software: particulas; sin WebGL: imagen fija", () => {
    expect(nivelInicial({ ...base, webgl2: false })).toBe("particulas");
    expect(nivelInicial({ ...base, software: true })).toBe("particulas");
    expect(nivelInicial({ ...base, webgl: false, webgl2: false })).toBe("fija");
  });

  it("equipo debil o ahorro de datos: un escalon abajo", () => {
    expect(nivelInicial({ ...base, nucleos: 2 })).toBe("bajo");
    expect(nivelInicial({ ...base, movil: true, memoriaGb: 2 })).toBe("particulas");
    expect(nivelInicial({ ...base, ahorroDatos: true })).toBe("bajo");
  });

  it("la cadena de caida termina en la imagen fija", () => {
    expect(siguienteNivel("alto")).toBe("medio");
    expect(siguienteNivel("medio")).toBe("bajo");
    expect(siguienteNivel("bajo")).toBe("particulas");
    expect(siguienteNivel("particulas")).toBe("fija");
    expect(siguienteNivel("fija")).toBe("fija");
  });

  it("el medidor: 60 fps sostiene un minimo de 45", () => {
    // calentamiento 700 ms + ventana 2600 ms = 3300 ms; a 16.67 ms son 198 fotogramas
    const m = new MedidorFps(45);
    let v = m.registrar(16.67);
    for (let i = 0; i < 250; i++) v = m.registrar(16.67);
    expect(v).toBe("sostiene");
    expect(m.fpsMediana()).toBeCloseTo(60, 0);
  });

  it("el medidor: 30 fps no sostienen un minimo de 45, y lo dice tras ~3.3 s", () => {
    const m = new MedidorFps(45);
    let v = m.registrar(33.3);
    let transcurrido = 33.3;
    while (v === "midiendo") {
      v = m.registrar(33.3);
      transcurrido += 33.3;
    }
    expect(v).toBe("no-sostiene");
    // 700 + 2600 = 3300 ms, mas a lo sumo un fotograma
    expect(transcurrido).toBeGreaterThanOrEqual(3300);
    expect(transcurrido).toBeLessThan(3300 + 34);
  });

  it("el medidor ignora el calentamiento y las pausas largas", () => {
    const m = new MedidorFps(45);
    // calentamiento lento (compilacion): no cuenta
    for (let i = 0; i < 10; i++) m.registrar(60);
    // una pausa de pestaña oculta: no cuenta
    m.registrar(5000);
    let v = m.registrar(16.67);
    for (let i = 0; i < 250; i++) v = m.registrar(16.67);
    expect(v).toBe("sostiene");
  });
});

describe("figuras", () => {
  it("el azar sembrado repite la misma secuencia", () => {
    const a = azarSembrado(42);
    const b = azarSembrado(42);
    for (let i = 0; i < 5; i++) expect(a()).toBe(b());
  });

  it("centra la figura por su caja y escala su lado mayor a TAMANO_FIGURA", () => {
    // Rectangulo de pixeles x 10..29 (20 px) por y 20..59 (40 px).
    // Centro = ((10 + 29 + 1) / 2, (20 + 59 + 1) / 2) = (20, 40).
    // Escala = 3.0 / max(20, 40) = 0.075 -> x en [-0.75, 0.75], y en [-1.5, 1.5].
    const pixeles: number[] = [];
    for (let y = 20; y < 60; y++) for (let x = 10; x < 30; x++) pixeles.push(x, y);
    const puntos = normalizarPuntos(pixeles, 4000, azarSembrado(3), 0);
    let minX = Infinity, maxX = -Infinity, minY = Infinity, maxY = -Infinity, sx = 0, sy = 0;
    for (let i = 0; i < 4000; i++) {
      const x = puntos[i * 3];
      const y = puntos[i * 3 + 1];
      minX = Math.min(minX, x); maxX = Math.max(maxX, x);
      minY = Math.min(minY, y); maxY = Math.max(maxY, y);
      sx += x; sy += y;
    }
    expect(minX).toBeGreaterThanOrEqual(-0.75);
    expect(maxX).toBeLessThanOrEqual(0.75);
    expect(minY).toBeGreaterThanOrEqual(-1.5);
    expect(maxY).toBeLessThanOrEqual(1.5);
    // llega a los bordes (a menos de un pixel = 0.075)
    expect(maxY - minY).toBeGreaterThan(3.0 - 0.15);
    // centrada: la media de un rectangulo lleno cae en el centro
    expect(Math.abs(sx / 4000)).toBeLessThan(0.02);
    expect(Math.abs(sy / 4000)).toBeLessThan(0.03);
  });
});
