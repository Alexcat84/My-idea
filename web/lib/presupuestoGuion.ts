/**
 * TOPES DE LOS GUIONES (decision del fundador, 10 oct 2026): cada llamada a la API reserva su coste maximo ANTES de
 * lanzarse y, al terminar, la reserva se cambia por el coste real. Una llamada que no cabe con lo gastado mas lo
 * reservado no se lanza. Asi el tope se cumple aunque haya llamadas en paralelo (antes, las que ya estaban en curso
 * terminaban despues del tope). Lo usan los guiones de la API; el gemelo en Python vive en
 * auditoria-final-claves/copia/api_copia.py.
 */
export class TopeAlcanzado extends Error {}

export class Presupuesto {
  gastado = 0;
  reservado = 0;

  constructor(readonly tope: number) {}

  /** Reserva el coste maximo de una llamada o lanza TopeAlcanzado sin reservar nada. Devuelve lo reservado. */
  reservar(usd: number): number {
    if (this.gastado + this.reservado + usd > this.tope + 1e-12) {
      throw new TopeAlcanzado(
        `tope de ${this.tope.toFixed(2)} USD: gastado ${this.gastado.toFixed(4)}, reservado ${this.reservado.toFixed(4)}, la llamada pide ${usd.toFixed(4)}`
      );
    }
    this.reservado += usd;
    return usd;
  }

  /** Cambia la reserva por el coste real de la llamada. */
  cerrar(reserva: number, real: number): void {
    this.reservado = Math.max(0, this.reservado - reserva);
    this.gastado += real;
  }

  /** La llamada fallo sin coste: suelta la reserva. */
  liberar(reserva: number): void {
    this.reservado = Math.max(0, this.reservado - reserva);
  }
}

/** El peor caso de una llamada: la entrada estimada por lo alto (2,5 caracteres por token, sin descuento de cache) y
 * todo el tope de salida, al precio del modelo [entrada, salida] por millon de tokens. */
export function reservaDeLlamada(caracteresDeEntrada: number, maxTokensSalida: number, precio: [number, number]): number {
  return ((caracteresDeEntrada / 2.5) * precio[0] + maxTokensSalida * precio[1]) / 1e6;
}
