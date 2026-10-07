/**
 * Los dibujos de la masa de la portada (decisión del fundador, 8 oct 2026): la
 * masa deja de alternar las cinco etapas y forma IDEAS HECHAS REALIDAD, objetos
 * reconocibles de negocios y proyectos reales. Ninguno es un logotipo, una marca
 * ni un personaje conocido: son trazos genéricos de línea.
 *
 * Este módulo NO viaja al navegador. Lo lee el horno
 * (scripts/portada/hornear_figuras.ts), que dibuja cada figura en un lienzo de
 * Chromium, calcula su campo de distancia y lo guarda precalculado en
 * public/portada/figuras/. El navegador solo baja el campo de la figura que va a
 * formar.
 *
 * Convenciones (las mismas de las cinco figuras de antes): lienzo de 512 px,
 * trazo base de 16 px con puntas y uniones redondas, y la figura ocupa una caja
 * de unos 400 px (el horno la centra por su caja y la escala a TAMANO_FIGURA, así
 * que una caja mucho menor engorda los trazos). Cada dibujo es autosuficiente:
 * solo usa `g` (el pincel 2D), `h` (las ayudas de abajo) y Math, porque el horno
 * lo pasa al navegador como texto.
 */

type Pincel = CanvasRenderingContext2D | OffscreenCanvasRenderingContext2D;

export interface Ayudas {
  /** Grosor del trazo en px (16 es el de base). */
  ancho(px: number): void;
  linea(x0: number, y0: number, x1: number, y1: number): void;
  /** Polilínea por pares x, y; `cerrar` la cierra. */
  poli(puntos: number[], cerrar?: boolean): void;
  circulo(x: number, y: number, r: number, relleno?: boolean): void;
  /** Rectángulo de esquinas redondeadas (radio `r`). */
  caja(x: number, y: number, w: number, alto: number, r?: number): void;
  arco(x: number, y: number, r: number, a0: number, a1: number): void;
}

export type Dibujo = (g: Pincel, h: Ayudas) => void;

/** Las ayudas, también autosuficientes (el horno las pasa como texto). */
export function crearAyudas(g: Pincel): Ayudas {
  return {
    ancho(px) {
      g.lineWidth = px;
    },
    linea(x0, y0, x1, y1) {
      g.beginPath();
      g.moveTo(x0, y0);
      g.lineTo(x1, y1);
      g.stroke();
    },
    poli(p, cerrar) {
      g.beginPath();
      g.moveTo(p[0], p[1]);
      for (let i = 2; i < p.length; i += 2) g.lineTo(p[i], p[i + 1]);
      if (cerrar) g.closePath();
      g.stroke();
    },
    circulo(x, y, r, relleno) {
      g.beginPath();
      g.arc(x, y, r, 0, Math.PI * 2);
      if (relleno) g.fill();
      else g.stroke();
    },
    caja(x, y, w, alto, r = 0) {
      g.beginPath();
      g.moveTo(x + r, y);
      g.lineTo(x + w - r, y);
      g.arcTo(x + w, y, x + w, y + r, r);
      g.lineTo(x + w, y + alto - r);
      g.arcTo(x + w, y + alto, x + w - r, y + alto, r);
      g.lineTo(x + r, y + alto);
      g.arcTo(x, y + alto, x, y + alto - r, r);
      g.lineTo(x, y + r);
      g.arcTo(x, y, x + r, y, r);
      g.closePath();
      g.stroke();
    },
    arco(x, y, r, a0, a1) {
      g.beginPath();
      g.arc(x, y, r, a0, a1);
      g.stroke();
    },
  };
}

export const DIBUJOS: Record<string, Dibujo> = {
  /** Una cafetería: la taza con su plato y el vapor. */
  cafeteria(g, h) {
    g.beginPath();
    g.moveTo(112, 214); g.lineTo(368, 214); g.lineTo(350, 360);
    g.quadraticCurveTo(342, 404, 300, 404); g.lineTo(180, 404);
    g.quadraticCurveTo(138, 404, 130, 360); g.closePath(); g.stroke();
    h.arco(372, 284, 44, -Math.PI * 0.45, Math.PI * 0.45);
    g.beginPath(); g.moveTo(80, 440); g.quadraticCurveTo(256, 476, 432, 440); g.stroke();
    h.ancho(12);
    for (const x of [190, 246, 302]) {
      g.beginPath(); g.moveTo(x, 182); g.bezierCurveTo(x - 26, 150, x + 26, 124, x, 88); g.stroke();
    }
  },
  /** Un taller de bicicletas. */
  bicicleta(g, h) {
    h.ancho(14);
    h.circulo(146, 330, 88);
    h.circulo(366, 330, 88);
    h.ancho(16);
    h.poli([146, 330, 252, 330, 224, 212, 146, 330]);
    h.poli([224, 212, 334, 212, 252, 330]);
    h.linea(334, 212, 366, 330);
    h.poli([334, 212, 318, 172, 360, 166]);
    h.linea(198, 204, 248, 204);
    h.ancho(12);
    h.linea(252, 330, 276, 360);
  },
  /** Un vivero: la planta en su maceta. */
  maceta(g, h) {
    h.poli([162, 334, 350, 334, 328, 452, 184, 452], true);
    h.ancho(20);
    h.linea(146, 316, 366, 316);
    h.ancho(16);
    h.linea(256, 316, 256, 168);
    g.beginPath(); g.moveTo(256, 256); g.quadraticCurveTo(168, 256, 146, 176); g.quadraticCurveTo(232, 184, 256, 256); g.stroke();
    g.beginPath(); g.moveTo(256, 214); g.quadraticCurveTo(344, 214, 366, 134); g.quadraticCurveTo(280, 142, 256, 214); g.stroke();
    g.beginPath(); g.moveTo(256, 168); g.quadraticCurveTo(216, 110, 256, 56); g.quadraticCurveTo(296, 110, 256, 168); g.stroke();
  },
  /** Una panadería: la hogaza con sus cortes, recién salida. */
  panaderia(g, h) {
    g.beginPath();
    g.moveTo(72, 366); g.bezierCurveTo(72, 196, 440, 196, 440, 366);
    g.quadraticCurveTo(440, 400, 406, 400); g.lineTo(106, 400);
    g.quadraticCurveTo(72, 400, 72, 366); g.stroke();
    h.ancho(14);
    h.linea(164, 312, 206, 256);
    h.linea(236, 312, 278, 250);
    h.linea(308, 314, 350, 258);
    h.ancho(12);
    for (const x of [200, 312]) {
      g.beginPath(); g.moveTo(x, 196); g.bezierCurveTo(x - 22, 168, x + 22, 146, x, 116); g.stroke();
    }
  },
  /** Una app: la laptop con su aplicación en pantalla. */
  laptop(g, h) {
    h.caja(116, 104, 280, 198, 14);
    h.poli([84, 318, 428, 318, 456, 362, 56, 362], true);
    h.ancho(10);
    h.linea(226, 340, 286, 340);
    h.linea(150, 144, 230, 144);
    h.linea(150, 172, 206, 172);
    h.caja(248, 136, 118, 68, 8);
    h.linea(150, 236, 366, 236);
    h.linea(150, 264, 300, 264);
  },
  /** Un food truck con su ventanilla y su toldo. */
  foodtruck(g, h) {
    h.poli([60, 352, 60, 160, 340, 160, 340, 352]);
    h.poli([340, 222, 404, 222, 450, 288, 450, 352, 52, 352]);
    h.ancho(10);
    h.poli([356, 238, 398, 238, 428, 282, 356, 282], true);
    h.ancho(12);
    h.caja(100, 204, 184, 72, 6);
    h.linea(88, 290, 296, 290);
    h.ancho(10);
    for (let i = 0; i < 5; i++) h.arco(120 + i * 36, 200, 18, 0, Math.PI);
    h.ancho(16);
    h.circulo(132, 364, 36);
    h.circulo(392, 364, 36);
    h.circulo(132, 364, 10, true);
    h.circulo(392, 364, 10, true);
  },
  /** Una tienda de barrio: la vitrina con su toldo de rayas. */
  tienda(g, h) {
    h.poli([100, 230, 100, 440]);
    h.poli([412, 230, 412, 440]);
    h.linea(78, 440, 434, 440);
    h.ancho(14);
    h.linea(80, 152, 432, 152);
    h.linea(80, 152, 80, 220);
    h.linea(432, 152, 432, 220);
    for (let i = 0; i < 6; i++) h.arco(109.3 + i * 58.7, 220, 29.3, 0, Math.PI);
    h.ancho(10);
    for (let i = 1; i < 6; i++) h.linea(80 + i * 58.7, 152, 80 + i * 58.7, 220);
    h.ancho(14);
    h.poli([224, 440, 224, 318, 288, 318, 288, 440]);
    h.caja(126, 296, 70, 70, 6);
    h.caja(316, 296, 70, 70, 6);
    h.ancho(12);
    h.caja(176, 82, 160, 46, 10);
  },
  /** Una startup que despega: el cohete. */
  cohete(g, h) {
    g.beginPath();
    g.moveTo(256, 52); g.bezierCurveTo(332, 108, 332, 262, 310, 352);
    g.lineTo(202, 352); g.bezierCurveTo(180, 262, 180, 108, 256, 52); g.closePath(); g.stroke();
    h.ancho(14);
    h.circulo(256, 188, 32);
    h.ancho(16);
    h.poli([204, 280, 148, 352, 148, 402, 202, 354]);
    h.poli([308, 280, 364, 352, 364, 402, 310, 354]);
    h.ancho(14);
    g.beginPath(); g.moveTo(224, 370); g.quadraticCurveTo(256, 466, 288, 370); g.stroke();
    h.ancho(10);
    g.beginPath(); g.moveTo(244, 374); g.quadraticCurveTo(256, 422, 268, 374); g.stroke();
  },
  /** Una escuela de música: la guitarra acústica. */
  guitarra(g, h) {
    g.beginPath();
    g.moveTo(256, 236); g.bezierCurveTo(204, 236, 194, 274, 210, 298);
    g.bezierCurveTo(146, 314, 146, 444, 256, 456);
    g.bezierCurveTo(366, 444, 366, 314, 302, 298);
    g.bezierCurveTo(318, 274, 308, 236, 256, 236); g.closePath(); g.stroke();
    h.ancho(12);
    h.circulo(256, 350, 26);
    h.ancho(14);
    h.linea(226, 414, 286, 414);
    g.fillRect(243, 96, 26, 142);
    h.ancho(12);
    h.caja(234, 50, 44, 52, 10);
    h.ancho(10);
    h.linea(220, 64, 234, 64); h.linea(220, 88, 234, 88);
    h.linea(278, 64, 292, 64); h.linea(278, 88, 292, 88);
  },
  /** Turismo en el mar: el velero. */
  velero(g, h) {
    h.poli([86, 336, 426, 336, 372, 398, 140, 398], true);
    h.linea(250, 336, 250, 70);
    h.ancho(14);
    h.poli([266, 86, 266, 314, 414, 314], true);
    h.poli([234, 112, 234, 314, 118, 314], true);
    g.beginPath(); g.moveTo(250, 70); g.lineTo(292, 84); g.lineTo(250, 98); g.closePath(); g.fill();
    h.ancho(12);
    g.beginPath(); g.moveTo(66, 440);
    for (let i = 0; i < 8; i++) g.quadraticCurveTo(66 + i * 47.5 + 23.75, 420, 66 + (i + 1) * 47.5, 440);
    g.stroke();
  },
  /** Un estudio de fotografía: la cámara. */
  camara(g, h) {
    h.caja(68, 160, 376, 240, 28);
    h.poli([168, 160, 194, 114, 290, 114, 316, 160]);
    h.circulo(256, 284, 84);
    h.ancho(12);
    h.circulo(256, 284, 44);
    h.ancho(10);
    h.caja(362, 184, 46, 28, 6);
    h.ancho(14);
    h.linea(102, 140, 138, 140);
  },
  /** Una casa con su huerto. */
  casahuerto(g, h) {
    h.poli([96, 220, 220, 108, 344, 220]);
    h.linea(122, 198, 122, 330);
    h.linea(318, 198, 318, 330);
    h.linea(84, 330, 440, 330);
    h.poli([198, 330, 198, 262, 242, 262, 242, 330]);
    h.linea(394, 330, 394, 266);
    h.circulo(394, 226, 44);
    // el huerto: una fila de brotes grandes sobre su surco
    h.ancho(14);
    h.linea(80, 438, 432, 438);
    for (const x of [124, 210, 296, 382]) {
      h.linea(x, 438, x, 396);
      g.beginPath(); g.moveTo(x, 404); g.quadraticCurveTo(x - 30, 402, x - 34, 372); g.quadraticCurveTo(x - 6, 376, x, 404); g.stroke();
      g.beginPath(); g.moveTo(x, 404); g.quadraticCurveTo(x + 30, 402, x + 34, 372); g.quadraticCurveTo(x + 6, 376, x, 404); g.stroke();
    }
  },
  /** Una librería o una editorial: el libro abierto. */
  libro(g, h) {
    g.beginPath(); g.moveTo(256, 160); g.quadraticCurveTo(170, 108, 70, 140); g.lineTo(70, 386);
    g.quadraticCurveTo(170, 354, 256, 406); g.stroke();
    g.beginPath(); g.moveTo(256, 160); g.quadraticCurveTo(342, 108, 442, 140); g.lineTo(442, 386);
    g.quadraticCurveTo(342, 354, 256, 406); g.stroke();
    h.linea(256, 160, 256, 406);
    h.ancho(9);
    for (const y of [206, 250, 294]) {
      h.linea(104, y, 222, y - 4);
      h.linea(290, y - 4, 408, y);
    }
  },
  /** Una peluquería: las tijeras. */
  tijeras(g, h) {
    h.circulo(192, 382, 50);
    h.circulo(320, 382, 50);
    h.ancho(18);
    h.linea(222, 340, 326, 70);
    h.linea(290, 340, 186, 70);
    h.circulo(256, 252, 10, true);
  },
  /** Una marca de ropa: la camiseta. */
  camiseta(g, h) {
    g.beginPath();
    g.moveTo(198, 94); g.quadraticCurveTo(256, 146, 314, 94);
    g.lineTo(418, 138); g.lineTo(456, 234); g.lineTo(386, 262); g.lineTo(376, 226);
    g.lineTo(376, 432); g.lineTo(136, 432); g.lineTo(136, 226); g.lineTo(126, 262);
    g.lineTo(56, 234); g.lineTo(94, 138); g.closePath(); g.stroke();
    h.ancho(10);
    h.caja(292, 188, 48, 42, 6);
  },
  /** Una repostería: el pastel con sus velas. */
  pastel(g, h) {
    h.linea(68, 432, 444, 432);
    h.poli([100, 432, 100, 322, 412, 322, 412, 432]);
    h.poli([160, 322, 160, 232, 352, 232, 352, 322]);
    h.ancho(10);
    g.beginPath(); g.moveTo(100, 350);
    for (let i = 0; i < 6; i++) g.quadraticCurveTo(100 + i * 52 + 26, 374, 100 + (i + 1) * 52, 350);
    g.stroke();
    g.beginPath(); g.moveTo(160, 258);
    for (let i = 0; i < 4; i++) g.quadraticCurveTo(160 + i * 48 + 24, 280, 160 + (i + 1) * 48, 258);
    g.stroke();
    h.ancho(12);
    for (const x of [208, 256, 304]) {
      h.linea(x, 232, x, 184);
      g.beginPath(); g.moveTo(x, 168); g.quadraticCurveTo(x + 13, 154, x, 132); g.quadraticCurveTo(x - 13, 154, x, 168); g.fill();
    }
  },
  /** Una pizzería: la porción. */
  pizza(g, h) {
    g.beginPath(); g.moveTo(256, 452); g.lineTo(106, 132); g.quadraticCurveTo(256, 66, 406, 132); g.closePath(); g.stroke();
    h.ancho(12);
    g.beginPath(); g.moveTo(124, 170); g.quadraticCurveTo(256, 112, 388, 170); g.stroke();
    h.ancho(10);
    h.circulo(226, 230, 22);
    h.circulo(296, 252, 20);
    h.circulo(252, 326, 18);
  },
  /** Una heladería: el cono con dos bolas. */
  helado(g, h) {
    h.poli([182, 272, 256, 458, 330, 272]);
    h.linea(172, 272, 340, 272);
    h.ancho(8);
    h.linea(193, 300, 287, 380);
    h.linea(209, 340, 271, 420);
    h.linea(319, 300, 225, 380);
    h.linea(303, 340, 241, 420);
    h.ancho(16);
    h.arco(256, 236, 80, Math.PI * 0.95, Math.PI * 2.05);
    g.beginPath(); g.moveTo(176, 252);
    for (let i = 0; i < 4; i++) g.quadraticCurveTo(176 + i * 40 + 20, 270, 176 + (i + 1) * 40, 252);
    g.stroke();
    h.arco(256, 146, 62, Math.PI * 0.88, Math.PI * 2.12);
    h.circulo(256, 70, 14, true);
    h.ancho(8);
    g.beginPath(); g.moveTo(256, 62); g.quadraticCurveTo(266, 44, 284, 40); g.stroke();
  },
  /** Fotografía aérea o reparto: el dron. */
  dron(g, h) {
    h.ancho(14);
    h.caja(206, 226, 100, 60, 18);
    h.ancho(16);
    h.linea(206, 238, 126, 174);
    h.linea(306, 238, 386, 174);
    h.linea(206, 274, 126, 338);
    h.linea(306, 274, 386, 338);
    h.ancho(10);
    for (const [x, y] of [[120, 168], [392, 168], [120, 344], [392, 344]]) {
      h.circulo(x, y, 52);
      h.circulo(x, y, 10, true);
    }
    h.circulo(256, 256, 12, true);
  },
  /** Jardinería: la regadera. */
  regadera(g, h) {
    h.poli([150, 222, 330, 222, 320, 400, 160, 400], true);
    g.beginPath(); g.moveTo(182, 222); g.bezierCurveTo(182, 132, 298, 132, 298, 222); g.stroke();
    h.ancho(14);
    g.beginPath(); g.moveTo(150, 252); g.quadraticCurveTo(96, 252, 96, 302); g.quadraticCurveTo(96, 352, 152, 352); g.stroke();
    h.ancho(16);
    h.linea(322, 332, 420, 214);
    h.ancho(20);
    h.linea(404, 194, 444, 230);
    h.ancho(8);
    h.linea(452, 252, 460, 274);
    h.linea(434, 264, 440, 288);
    h.linea(466, 238, 476, 258);
  },
  /** Paseo o veterinaria: la cara de un perro de orejas caídas. */
  perro(g, h) {
    // La cara se dibuja a 1.3x sobre su centro (su caja quedaba en 309 px) y el
    // trazo se compensa, para que mida lo mismo que en las demás figuras.
    g.translate(256, 262);
    g.scale(1.3, 1.3);
    g.translate(-256, -262);
    h.ancho(16 / 1.3);
    g.beginPath();
    g.moveTo(178, 178); g.quadraticCurveTo(256, 120, 334, 178);
    g.quadraticCurveTo(370, 262, 330, 342); g.quadraticCurveTo(256, 398, 182, 342);
    g.quadraticCurveTo(142, 262, 178, 178); g.stroke();
    g.beginPath(); g.moveTo(174, 176); g.quadraticCurveTo(96, 204, 112, 326); g.quadraticCurveTo(168, 312, 184, 230); g.stroke();
    g.beginPath(); g.moveTo(338, 176); g.quadraticCurveTo(416, 204, 400, 326); g.quadraticCurveTo(344, 312, 328, 230); g.stroke();
    h.circulo(220, 244, 13, true);
    h.circulo(292, 244, 13, true);
    g.beginPath(); g.moveTo(232, 286); g.lineTo(280, 286); g.lineTo(256, 312); g.closePath(); g.fill();
    h.ancho(12 / 1.3);
    g.beginPath(); g.moveTo(256, 310); g.quadraticCurveTo(256, 340, 226, 342); g.stroke();
    g.beginPath(); g.moveTo(256, 310); g.quadraticCurveTo(256, 340, 286, 342); g.stroke();
  },
  /** Una pescadería o un criadero: el pez. */
  pez(g, h) {
    g.beginPath(); g.moveTo(92, 256); g.bezierCurveTo(166, 128, 326, 128, 378, 256);
    g.bezierCurveTo(326, 384, 166, 384, 92, 256); g.closePath(); g.stroke();
    h.poli([372, 256, 452, 186, 452, 326], true);
    h.circulo(156, 238, 12, true);
    h.ancho(12);
    g.beginPath(); g.moveTo(198, 204); g.quadraticCurveTo(226, 256, 198, 308); g.stroke();
    g.beginPath(); g.moveTo(218, 166); g.quadraticCurveTo(262, 116, 304, 160); g.stroke();
    h.ancho(9);
    h.arco(262, 236, 22, -Math.PI * 0.5, Math.PI * 0.5);
    h.arco(304, 278, 22, -Math.PI * 0.5, Math.PI * 0.5);
  },
  /** Una zapatería: la zapatilla. */
  zapato(g, h) {
    g.beginPath(); g.moveTo(62, 358); g.lineTo(450, 358); g.quadraticCurveTo(458, 400, 420, 400);
    g.lineTo(92, 400); g.quadraticCurveTo(58, 400, 62, 358); g.stroke();
    g.beginPath(); g.moveTo(70, 358); g.lineTo(78, 214); g.quadraticCurveTo(82, 196, 104, 198);
    g.lineTo(176, 206); g.quadraticCurveTo(196, 246, 240, 236); g.lineTo(276, 226);
    g.lineTo(362, 290); g.quadraticCurveTo(440, 300, 446, 358); g.stroke();
    h.ancho(10);
    h.linea(258, 244, 280, 272);
    h.linea(290, 254, 310, 282);
    h.linea(322, 268, 338, 292);
  },
  /** Una óptica: los anteojos. */
  anteojos(g, h) {
    h.caja(78, 208, 152, 112, 42);
    h.caja(282, 208, 152, 112, 42);
    g.beginPath(); g.moveTo(230, 240); g.quadraticCurveTo(256, 212, 282, 240); g.stroke();
    h.linea(78, 236, 50, 198);
    h.linea(434, 236, 462, 198);
  },
  /** Un pódcast: el micrófono de estudio. */
  microfono(g, h) {
    h.caja(196, 66, 120, 172, 60);
    h.ancho(8);
    h.linea(210, 118, 302, 118);
    h.linea(206, 158, 306, 158);
    h.linea(210, 198, 302, 198);
    h.ancho(14);
    g.beginPath(); g.moveTo(168, 176); g.lineTo(168, 206); g.bezierCurveTo(168, 300, 344, 300, 344, 206); g.lineTo(344, 176); g.stroke();
    h.linea(256, 280, 256, 420);
    h.ancho(18);
    h.linea(184, 424, 328, 424);
  },
  /** Un estudio de grabación: los audífonos. */
  audifonos(g, h) {
    h.ancho(18);
    h.arco(256, 262, 150, Math.PI, Math.PI * 2);
    h.ancho(16);
    h.caja(88, 252, 72, 136, 26);
    h.caja(352, 252, 72, 136, 26);
    h.ancho(10);
    h.linea(162, 276, 162, 364);
    h.linea(350, 276, 350, 364);
  },
  /** Un taller de arte: la paleta del pintor. */
  paleta(g, h) {
    g.beginPath(); g.moveTo(256, 100);
    g.bezierCurveTo(392, 100, 452, 202, 422, 292);
    g.bezierCurveTo(402, 352, 332, 330, 322, 372);
    g.bezierCurveTo(312, 422, 250, 432, 198, 422);
    g.bezierCurveTo(96, 402, 66, 300, 88, 220);
    g.bezierCurveTo(110, 140, 180, 100, 256, 100); g.closePath(); g.stroke();
    h.ancho(12);
    h.circulo(250, 340, 26);
    for (const [x, y] of [[168, 196], [244, 164], [324, 174], [382, 236], [148, 282]]) h.circulo(x, y, 20, true);
  },
  /** Un taller de costura: la máquina de coser. */
  costura(g, h) {
    g.beginPath(); g.moveTo(112, 380); g.lineTo(112, 150); g.quadraticCurveTo(112, 120, 142, 120);
    g.lineTo(390, 120); g.quadraticCurveTo(420, 120, 420, 150); g.lineTo(420, 244); g.lineTo(368, 244);
    g.lineTo(368, 190); g.lineTo(182, 190); g.lineTo(182, 380); g.stroke();
    h.caja(62, 380, 388, 42, 8);
    h.ancho(10);
    h.linea(394, 244, 394, 300);
    h.linea(376, 300, 412, 300);
    h.linea(262, 120, 262, 98);
    h.caja(244, 74, 36, 24, 6);
  },
  /** Turismo de montaña: la carpa y el pino. */
  carpa(g, h) {
    h.poli([70, 420, 220, 160, 370, 420], true);
    h.ancho(12);
    h.linea(220, 300, 182, 420);
    h.linea(220, 300, 258, 420);
    h.ancho(16);
    h.linea(48, 420, 466, 420);
    h.poli([410, 130, 458, 240, 362, 240], true);
    h.poli([410, 190, 466, 320, 354, 320], true);
    h.linea(410, 320, 410, 412);
  },
  /** Una tienda en línea: el carrito. */
  carrito(g, h) {
    h.poli([58, 108, 110, 108, 170, 332, 404, 332]);
    h.poli([124, 160, 442, 160, 410, 282, 156, 282], true);
    h.ancho(8);
    h.linea(210, 160, 220, 282);
    h.linea(290, 160, 290, 282);
    h.linea(370, 160, 360, 282);
    h.linea(140, 220, 426, 220);
    h.ancho(14);
    h.circulo(196, 392, 28);
    h.circulo(372, 392, 28);
  },
  /** Envíos: la caja con su cinta. */
  paquete(g, h) {
    h.poli([256, 88, 432, 170, 256, 252, 80, 170], true);
    h.poli([80, 170, 80, 350, 256, 432, 432, 350, 432, 170]);
    h.linea(256, 252, 256, 432);
    h.ancho(22);
    h.linea(168, 129, 344, 211);
    h.linea(344, 211, 344, 296);
  },
  /** Reparto a domicilio: el camión con su flecha. */
  camion(g, h) {
    h.poli([60, 340, 60, 150, 322, 150, 322, 340]);
    h.poli([322, 200, 402, 200, 452, 270, 452, 340, 50, 340]);
    h.ancho(10);
    h.poli([338, 216, 394, 216, 430, 266, 338, 266], true);
    h.ancho(14);
    h.linea(114, 245, 262, 245);
    h.poli([230, 213, 262, 245, 230, 277]);
    h.ancho(16);
    h.circulo(132, 354, 38);
    h.circulo(392, 354, 38);
    h.circulo(132, 354, 10, true);
    h.circulo(392, 354, 10, true);
  },
  /** Energía limpia: el aerogenerador. */
  aerogenerador(g, h) {
    h.ancho(14);
    h.linea(236, 452, 250, 206);
    h.linea(276, 452, 262, 206);
    h.ancho(16);
    h.linea(196, 452, 316, 452);
    const cx = 256, cy = 192, largo = 160, lado = 24;
    for (const grados of [-90, 30, 150]) {
      const a = (grados * Math.PI) / 180;
      const ux = Math.cos(a), uy = Math.sin(a);
      const px = -uy, py = ux;
      const tx = cx + ux * largo, ty = cy + uy * largo;
      const mx = cx + ux * largo * 0.35, my = cy + uy * largo * 0.35;
      g.beginPath(); g.moveTo(cx, cy);
      g.quadraticCurveTo(mx + px * lado, my + py * lado, tx, ty);
      g.quadraticCurveTo(mx - px * lado * 0.3, my - py * lado * 0.3, cx, cy);
      g.closePath(); g.fill();
    }
    h.circulo(cx, cy, 20, true);
  },
  /** Energía solar: el panel bajo el sol. */
  panelsolar(g, h) {
    h.poli([170, 236, 420, 236, 456, 396, 134, 396], true);
    h.ancho(10);
    h.linea(253, 236, 241, 396);
    h.linea(337, 236, 349, 396);
    h.linea(152, 316, 438, 316);
    h.ancho(16);
    h.linea(296, 396, 296, 448);
    h.linea(244, 452, 348, 452);
    h.ancho(14);
    h.circulo(118, 120, 38);
    h.ancho(10);
    for (let i = 0; i < 8; i++) {
      const a = (i * Math.PI) / 4;
      h.linea(118 + Math.cos(a) * 58, 120 + Math.sin(a) * 58, 118 + Math.cos(a) * 80, 120 + Math.sin(a) * 80);
    }
  },
  /** Un restaurante o comida casera: la olla humeante. */
  olla(g, h) {
    g.beginPath(); g.moveTo(110, 232); g.lineTo(110, 380); g.quadraticCurveTo(110, 420, 150, 420);
    g.lineTo(362, 420); g.quadraticCurveTo(402, 420, 402, 380); g.lineTo(402, 232); g.stroke();
    h.linea(94, 224, 418, 224);
    g.beginPath(); g.moveTo(98, 224); g.quadraticCurveTo(256, 148, 414, 224); g.stroke();
    h.circulo(256, 172, 14, true);
    h.ancho(14);
    h.poli([110, 266, 70, 266, 70, 300, 110, 300]);
    h.poli([402, 266, 442, 266, 442, 300, 402, 300]);
    h.ancho(12);
    for (const x of [200, 312]) {
      g.beginPath(); g.moveTo(x, 132); g.bezierCurveTo(x - 22, 104, x + 22, 82, x, 52); g.stroke();
    }
  },
  /** Una casa de té: la tetera. */
  tetera(g, h) {
    g.beginPath(); g.moveTo(140, 250); g.bezierCurveTo(118, 440, 394, 440, 372, 250); g.closePath(); g.stroke();
    g.beginPath(); g.moveTo(180, 250); g.quadraticCurveTo(256, 188, 332, 250); g.stroke();
    h.circulo(256, 206, 13, true);
    g.beginPath(); g.moveTo(146, 312); g.bezierCurveTo(98, 312, 88, 250, 60, 218); g.stroke();
    g.beginPath(); g.moveTo(370, 282); g.bezierCurveTo(446, 270, 446, 376, 360, 372); g.stroke();
  },
  /** Apicultura: el frasco de miel. */
  miel(g, h) {
    g.beginPath(); g.moveTo(150, 172); g.lineTo(362, 172); g.lineTo(362, 190);
    g.quadraticCurveTo(394, 220, 394, 262); g.lineTo(394, 400); g.quadraticCurveTo(394, 442, 352, 442);
    g.lineTo(160, 442); g.quadraticCurveTo(118, 442, 118, 400); g.lineTo(118, 262);
    g.quadraticCurveTo(118, 220, 150, 190); g.closePath(); g.stroke();
    h.caja(138, 112, 236, 52, 10);
    h.ancho(12);
    const hx = [];
    for (let i = 0; i < 6; i++) {
      const a = Math.PI / 6 + (i * Math.PI) / 3;
      hx.push(256 + Math.cos(a) * 56, 318 + Math.sin(a) * 56);
    }
    h.poli(hx, true);
    g.beginPath(); g.moveTo(300, 172); g.quadraticCurveTo(306, 202, 300, 218); g.stroke();
  },
  /** Velas artesanales: la vela encendida. */
  vela(g, h) {
    h.poli([196, 230, 196, 430]);
    h.poli([316, 230, 316, 430]);
    g.beginPath(); g.moveTo(196, 230); g.lineTo(234, 230); g.quadraticCurveTo(246, 276, 258, 230); g.lineTo(316, 230); g.stroke();
    h.ancho(12);
    h.linea(256, 216, 256, 186);
    h.ancho(14);
    g.beginPath(); g.moveTo(256, 172); g.bezierCurveTo(302, 132, 282, 80, 256, 48);
    g.bezierCurveTo(230, 80, 210, 132, 256, 172); g.closePath(); g.stroke();
    h.ancho(16);
    g.beginPath(); g.moveTo(136, 444); g.quadraticCurveTo(256, 474, 376, 444); g.stroke();
    h.linea(150, 432, 362, 432);
  },
  /** Diseño o tutorías: el lápiz sobre la regla. */
  lapizregla(g, h) {
    // regla en la diagonal ascendente
    const rx0 = 92, ry0 = 404, rx1 = 404, ry1 = 92, medio = 30;
    const largo = Math.hypot(rx1 - rx0, ry1 - ry0);
    const ux = (rx1 - rx0) / largo, uy = (ry1 - ry0) / largo;
    const px = -uy, py = ux;
    h.poli([
      rx0 + px * medio, ry0 + py * medio, rx1 + px * medio, ry1 + py * medio,
      rx1 - px * medio, ry1 - py * medio, rx0 - px * medio, ry0 - py * medio,
    ], true);
    h.ancho(9);
    for (let i = 1; i < 10; i++) {
      const bx = rx0 + ux * (largo * i) / 10 + px * medio;
      const by = ry0 + uy * (largo * i) / 10 + py * medio;
      const k = i % 2 ? 16 : 28;
      h.linea(bx, by, bx - px * k, by - py * k);
    }
    // lápiz en la otra diagonal
    const lx0 = 112, ly0 = 112, lx1 = 352, ly1 = 352, m = 22;
    h.ancho(14);
    h.poli([lx0 + m * 0.707, ly0 - m * 0.707, lx1 + m * 0.707, ly1 - m * 0.707, 430, 430, lx1 - m * 0.707, ly1 + m * 0.707, lx0 - m * 0.707, ly0 + m * 0.707], true);
    h.linea(lx0 + 30 + m * 0.707, ly0 + 30 - m * 0.707, lx0 + 30 - m * 0.707, ly0 + 30 + m * 0.707);
  },
  /** Una academia: el birrete. */
  birrete(g, h) {
    h.poli([256, 108, 456, 188, 256, 268, 56, 188], true);
    g.beginPath(); g.moveTo(140, 224); g.lineTo(140, 320); g.quadraticCurveTo(256, 380, 372, 320); g.lineTo(372, 224); g.stroke();
    h.ancho(10);
    h.poli([256, 188, 420, 206, 420, 330]);
    g.beginPath(); g.moveTo(420, 326); g.lineTo(402, 372); g.lineTo(438, 372); g.closePath(); g.fill();
  },
  /** Turismo de aventura: el globo aerostático. */
  globo(g, h) {
    g.beginPath(); g.moveTo(196, 330); g.bezierCurveTo(98, 250, 108, 58, 256, 58);
    g.bezierCurveTo(404, 58, 414, 250, 316, 330); g.closePath(); g.stroke();
    h.ancho(12);
    g.beginPath(); g.moveTo(256, 60); g.quadraticCurveTo(196, 190, 226, 330); g.stroke();
    g.beginPath(); g.moveTo(256, 60); g.quadraticCurveTo(316, 190, 286, 330); g.stroke();
    h.ancho(10);
    h.linea(206, 336, 224, 390);
    h.linea(306, 336, 288, 390);
    h.ancho(14);
    h.caja(218, 390, 76, 54, 6);
  },
  /** Astroturismo o ciencia: el telescopio. */
  telescopio(g, h) {
    const ax = 110, ay = 286, bx = 390, by = 150;
    const largo = Math.hypot(bx - ax, by - ay);
    const ux = (bx - ax) / largo, uy = (by - ay) / largo;
    const px = -uy, py = ux;
    const atras = 22, frente = 36;
    h.poli([
      ax + px * atras, ay + py * atras, bx + px * frente, by + py * frente,
      bx - px * frente, by - py * frente, ax - px * atras, ay - py * atras,
    ], true);
    h.ancho(12);
    const ox = ax - ux * 30, oy = ay - uy * 30;
    h.linea(ox + px * 14, oy + py * 14, ax + px * 14, ay + py * 14);
    h.linea(ox - px * 14, oy - py * 14, ax - px * 14, ay - py * 14);
    h.linea(ox + px * 14, oy + py * 14, ox - px * 14, oy - py * 14);
    h.ancho(16);
    const cx = 256, cy = 230;
    h.linea(cx, cy, 168, 444);
    h.linea(cx, cy, 258, 444);
    h.linea(cx, cy, 348, 444);
    h.circulo(cx, cy, 14, true);
  },
  /** Una app móvil: el teléfono con su cuadrícula. */
  telefono(g, h) {
    h.caja(164, 58, 184, 396, 32);
    h.ancho(10);
    h.linea(232, 92, 280, 92);
    h.ancho(12);
    for (let f = 0; f < 2; f++) for (let c = 0; c < 2; c++) h.caja(200 + c * 66, 136 + f * 66, 46, 46, 10);
    h.caja(200, 290, 112, 66, 12);
    h.linea(226, 412, 286, 412);
  },
  /** Un taller mecánico: el engranaje y la llave. */
  mecanica(g, h) {
    h.circulo(168, 168, 70);
    h.ancho(12);
    h.circulo(168, 168, 26);
    g.lineCap = "butt";
    h.ancho(30);
    for (let i = 0; i < 8; i++) {
      const a = (i * Math.PI) / 4 + Math.PI / 8;
      h.linea(168 + Math.cos(a) * 70, 168 + Math.sin(a) * 70, 168 + Math.cos(a) * 98, 168 + Math.sin(a) * 98);
    }
    g.lineCap = "round";
    h.ancho(30);
    h.linea(122, 418, 352, 188);
    h.ancho(18);
    h.arco(382, 158, 46, -Math.PI / 4 + 0.62, -Math.PI / 4 - 0.62 + Math.PI * 2);
    h.ancho(14);
    h.circulo(104, 436, 26);
  },
  /** Una oficina o un coworking: el edificio. */
  edificio(g, h) {
    h.poli([150, 450, 150, 70, 300, 70, 300, 450]);
    h.poli([300, 190, 410, 190, 410, 450]);
    h.linea(106, 450, 452, 450);
    h.ancho(12);
    for (let f = 0; f < 4; f++) {
      h.caja(176, 102 + f * 70, 38, 40, 6);
      h.caja(236, 102 + f * 70, 38, 40, 6);
    }
    for (let f = 0; f < 3; f++) h.caja(336, 224 + f * 70, 38, 40, 6);
    h.ancho(14);
    h.poli([206, 450, 206, 404, 244, 404, 244, 450]);
  },
  /** Turismo de costa: el faro. */
  faro(g, h) {
    h.poli([210, 430, 226, 180, 286, 180, 302, 430]);
    h.ancho(12);
    h.linea(221, 260, 291, 260);
    h.linea(216, 340, 296, 340);
    h.caja(220, 130, 72, 50, 4);
    h.poli([208, 130, 256, 88, 304, 130], true);
    h.ancho(10);
    h.linea(304, 150, 442, 112);
    h.linea(304, 162, 442, 202);
    h.linea(208, 150, 70, 112);
    h.linea(208, 162, 70, 202);
    h.ancho(12);
    g.beginPath(); g.moveTo(84, 444);
    for (let i = 0; i < 7; i++) g.quadraticCurveTo(84 + i * 49 + 24.5, 426, 84 + (i + 1) * 49, 444);
    g.stroke();
  },
  /** Una cafetería de postres: el cupcake. */
  cupcake(g, h) {
    h.poli([170, 304, 196, 442, 316, 442, 342, 304], true);
    h.ancho(8);
    h.linea(212, 304, 222, 442);
    h.linea(256, 304, 256, 442);
    h.linea(300, 304, 290, 442);
    h.ancho(16);
    g.beginPath(); g.moveTo(160, 304); g.quadraticCurveTo(126, 254, 180, 236);
    g.quadraticCurveTo(170, 176, 228, 178); g.quadraticCurveTo(256, 120, 296, 176);
    g.quadraticCurveTo(356, 176, 342, 236); g.quadraticCurveTo(390, 254, 352, 304); g.closePath(); g.stroke();
    h.circulo(262, 118, 16, true);
    h.ancho(8);
    g.beginPath(); g.moveTo(262, 104); g.quadraticCurveTo(270, 82, 292, 76); g.stroke();
  },
  /** Comida rápida: la hamburguesa. */
  hamburguesa(g, h) {
    g.beginPath(); g.moveTo(98, 246); g.bezierCurveTo(98, 114, 414, 114, 414, 246); g.closePath(); g.stroke();
    h.ancho(10);
    h.linea(188, 188, 200, 180);
    h.linea(250, 166, 264, 166);
    h.linea(312, 180, 324, 188);
    h.linea(214, 216, 226, 212);
    h.linea(288, 212, 300, 216);
    h.ancho(12);
    g.beginPath(); g.moveTo(86, 272);
    for (let i = 0; i < 8; i++) g.quadraticCurveTo(86 + i * 42.5 + 21.25, i % 2 ? 258 : 288, 86 + (i + 1) * 42.5, 272);
    g.stroke();
    h.ancho(16);
    h.caja(94, 294, 324, 42, 20);
    g.beginPath(); g.moveTo(102, 360); g.lineTo(410, 360); g.quadraticCurveTo(410, 410, 362, 410);
    g.lineTo(150, 410); g.quadraticCurveTo(102, 410, 102, 360); g.stroke();
  },
  /** Un gimnasio: la mancuerna. */
  mancuerna(g, h) {
    h.ancho(18);
    h.linea(166, 256, 346, 256);
    h.ancho(16);
    h.caja(96, 168, 38, 176, 12);
    h.caja(136, 192, 30, 128, 10);
    h.caja(378, 168, 38, 176, 12);
    h.caja(346, 192, 30, 128, 10);
    h.linea(72, 256, 96, 256);
    h.linea(416, 256, 440, 256);
  },
  /** Un taller de relojería: el reloj de pared. */
  reloj(g, h) {
    h.circulo(256, 256, 170);
    h.ancho(10);
    for (let i = 0; i < 12; i++) {
      const a = (i * Math.PI) / 6;
      const k = i % 3 ? 140 : 128;
      h.linea(256 + Math.cos(a) * k, 256 + Math.sin(a) * k, 256 + Math.cos(a) * 152, 256 + Math.sin(a) * 152);
    }
    h.ancho(14);
    h.linea(256, 256, 256, 148);
    h.linea(256, 256, 334, 296);
    h.circulo(256, 256, 12, true);
  },
  /** Diseño de interiores: la lámpara de escritorio. */
  lampara(g, h) {
    h.ancho(18);
    h.linea(114, 440, 290, 440);
    h.ancho(16);
    g.beginPath(); g.moveTo(130, 440); g.quadraticCurveTo(202, 404, 274, 440); g.stroke();
    h.poli([202, 424, 150, 282, 286, 166]);
    h.circulo(150, 282, 12, true);
    h.circulo(286, 166, 12, true);
    h.poli([268, 150, 330, 104, 432, 226, 352, 280], true);
    h.ancho(10);
    h.linea(372, 306, 392, 354);
    h.linea(414, 294, 444, 334);
  },
  /** El campo: el tractor. */
  tractor(g, h) {
    h.circulo(170, 330, 100);
    h.ancho(12);
    h.circulo(170, 330, 30);
    h.ancho(16);
    h.circulo(392, 372, 56);
    h.circulo(392, 372, 12, true);
    h.poli([120, 226, 130, 100, 262, 100, 272, 250]);
    h.poli([272, 250, 432, 250, 442, 316]);
    h.ancho(12);
    h.linea(392, 250, 392, 190);
    h.ancho(10);
    h.poli([150, 120, 244, 120, 250, 210, 144, 210], true);
  },
};
