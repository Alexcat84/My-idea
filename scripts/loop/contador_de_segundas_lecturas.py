# -*- coding: utf-8 -*-
r"""contador_de_segundas_lecturas.py . EL CONTADOR DE `P.5.2`, CON NOMBRE
ESTABLE Y POR REMISION.

Nombre estable y SIN numero de vuelta, como `tallar_cabecera_reporte.py`,
`verificar_apertura_sellada.py` y `serie_de_registros.py`: se invoca cada vez
que haya que recomputar la cifra de `P.5.2` y no se clona por vuelta.

--- POR QUE NACE (vuelta 163, TAREA 5.a; adjudicacion 6.11 del acta 162) ---

LA DEUDA, CON SU NOMBRE. La cifra vigente de `P.5.2` la produce
`scripts/loop/vuelta161_tarea1c_segunda_lectura.py`, que lleva el numero de OTRA
vuelta en el nombre. Reusarlo fue lo correcto (es la ley de una sola fuente y
asi lo adjudico el acta 162), pero **un instrumento de nombre fechado que
produce la cifra vigente envejece mal**: es exactamente la deuda que
`serie_de_registros.py` vino a curar cuando el numero de la serie estaba
tecleado.

**ES REMISION, NO COPIA, Y ESA ES TODA LA GRACIA.** Aqui no se reimplementa ni
una linea de la definicion: se IMPORTA el modulo viejo y se reexporta lo suyo.
El viejo NO SE BORRA y NO SE RENOMBRA, para que las citas de las actas (que lo
nombran por su nombre fechado) sigan resolviendo. Si alguien cambia la
definicion, la cambia en un solo sitio y las dos puertas dicen lo mismo, porque
son la misma puerta.

**LA VARA DE ACEPTACION, MEDIDA Y NO ALEGADA** (`docs/loop/SALIDA_V163_T5A_*`):
la cifra sale IDENTICA antes y despues, y no "parecida": la salida de este
fichero se coteja BYTE A BYTE contra la del modulo viejo COPIADO ANTES DE TOCAR
NADA (`scripts/loop/_v163_contador_viejo_copia.py`), salvo la primera linea de
titulo, que es lo unico que cambia a proposito.

QUE SE PUEDE IMPORTAR DE AQUI:
  - `actos_de_relectura(razon)`: los actos contables de una razon, `(tipo,
    vuelta)`, con la regla 3 de `P.5.2` ya aplicada;
  - `FORMAS_QUE_CUENTAN`, `FORMAS_QUE_NO_CUENTAN`, `REGISTRO`, `RAIZ`.

USO:
  python scripts/loop/contador_de_segundas_lecturas.py
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import vuelta161_tarea1c_segunda_lectura as VIEJO   # noqa: E402

# LA REMISION, EXPLICITA. No hay copia de la definicion en este fichero.
FUENTE = "scripts/loop/vuelta161_tarea1c_segunda_lectura.py"
actos_de_relectura = VIEJO.actos_de_relectura
FORMAS_QUE_CUENTAN = VIEJO.FORMAS_QUE_CUENTAN
FORMAS_QUE_NO_CUENTAN = VIEJO.FORMAS_QUE_NO_CUENTAN
REGISTRO = VIEJO.REGISTRO
RAIZ = VIEJO.RAIZ
linea_del_acta = VIEJO.linea_del_acta


def main():
    print("CONTADOR DE SEGUNDAS LECTURAS (P.5.2), NOMBRE ESTABLE POR REMISION A %s"
          % FUENTE)
    return VIEJO.main()


if __name__ == "__main__":
    raise SystemExit(main())
