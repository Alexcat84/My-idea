# -*- coding: utf-8 -*-
r"""vuelta171_tarea1a_mutacion_registro.py . ARNES DE MUTACION DEL REGISTRADOR
DEL ACTA 170 (TAREA 1.a de la vuelta 171), CON NOMBRE DE ARNES.

POR QUE EXISTE ESTE FICHERO Y NO SOLO EL FLAG `--mutar`. La bateria
`scripts/loop/verificar_mutaciones_viejas.py` invoca cada arnes SIN ARGUMENTOS.
Una prueba que vive detras de un `--mutar` de otro fichero no la corre nadie
desde la bateria. Es el mismo motivo por el que existe
`vuelta170_tarea1a_mutacion_registro.py`, del que este es clon declarado.

Y SIGUE A LA 170, NO A LA 169: la vuelta 169 no escribio el suyo y aun asi su
entrada `R.38` afirmaba que "el arnes hermano lo prueba por mutacion". La 170 si
lo escribio; esta lo escribe igual, y ademas ESTA VUELTA CORRIGE AQUELLA
AFIRMACION FALSA en la TAREA 4.a, por el carril del banco 9.10.

NO HAY COPIA DE LA PRUEBA AQUI: se IMPORTA y se llama. Una sola fuente.

SUJETO: fabricado EN MEMORIA (actas de mentira como listas de lineas) mas el
acta real leida hoy. CERO escrituras.

SUJETO CONGELADO, que es la condicion de entrada a la bateria desde la vuelta
148 (TAREA 2.5, adjudicacion 3.5 del acta 147): las actas de mentira son
literales de este proceso, y el acta 170 ya esta cerrada y firmada. Cuando el
auditor escriba el acta 171, el acotado de este instrumento seguira delimitando
la 170 por su cabecera siguiente, y sus dos conteos (12 y 4) no se mueven.

USO:  python scripts/loop/vuelta171_tarea1a_mutacion_registro.py
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import vuelta171_tarea1_registrar_acta170 as R   # noqa: E402

if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    raise SystemExit(R.prueba_de_mutacion())
