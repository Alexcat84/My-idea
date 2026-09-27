/**
 * Encuadre: la masa y las figuras centradas en los dos ejes y ocupando
 * cerca del 80 por ciento del LADO MENOR del hero, en escritorio y en
 * movil vertical, sin recortarse nunca en el borde.
 *
 * Todo el contenido vive en un espacio de mundo centrado en el origen:
 *  - TAMANO_FIGURA es el lado mayor de cada figura formada (80 %);
 *  - la masa en reposo tiene un diametro medio parecido (RADIO_MASA);
 *  - nada pasa de RADIO_LIMITE (96 % del lado menor): ni la piel agitada
 *    ni la materia en plena transformacion.
 */

export const FOV_GRADOS = 30;
export const FRACCION_LADO_MENOR = 0.8;
export const TAMANO_FIGURA = 3.0;
export const RADIO_MASA = 1.22;
/** Desplazamiento maximo de la piel sobre RADIO_MASA (ver glsl.ts). */
export const ENVOLTURA_PIEL = 0.52;
export const RADIO_LIMITE = (0.48 / FRACCION_LADO_MENOR) * TAMANO_FIGURA;

/**
 * Distancia de la camara (en el eje z, mirando al origen) para que
 * TAMANO_FIGURA ocupe FRACCION_LADO_MENOR del lado menor del lienzo.
 * El FOV de three.js es vertical: en retrato el lado menor es el ancho.
 */
export function distanciaCamara(ancho: number, alto: number, fovGrados = FOV_GRADOS): number {
  const aspecto = ancho / Math.max(alto, 1);
  const tanMedio = Math.tan((fovGrados * Math.PI) / 360);
  return TAMANO_FIGURA / (FRACCION_LADO_MENOR * 2 * tanMedio * Math.min(1, aspecto));
}

/** Pixeles de pantalla por unidad de mundo en el plano z = 0. */
export function pixelesPorUnidad(ancho: number, alto: number, fovGrados = FOV_GRADOS): number {
  const d = distanciaCamara(ancho, alto, fovGrados);
  const tanMedio = Math.tan((fovGrados * Math.PI) / 360);
  return alto / (2 * d * tanMedio);
}
