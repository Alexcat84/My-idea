# -*- coding: utf-8 -*-
r"""vuelta168_tarea4_mutacion_op_v_01.py . ARNES DE MUTACION DE LA PRUEBA POR CITA DE OP-V-01
(vuelta 168), CON NOMBRE DE ARNES.

POR QUE EXISTE ESTE FICHERO Y NO SOLO EL FLAG `--mutar`. La bateria
`scripts/loop/verificar_mutaciones_viejas.py` invoca cada arnes SIN ARGUMENTOS.
Una prueba que vive detras de un `--mutar` de otro fichero no la corre nadie
desde la bateria, y entonces no es una guarda: es una intencion.

NO HAY COPIA DE LA PRUEBA AQUI: se IMPORTA y se llama. Una sola fuente.

SUJETO: fabricado EN MEMORIA mas commits FIJOS de la historia. CERO escrituras.

USO:  python scripts/loop/vuelta168_tarea4_mutacion_op_v_01.py
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import vuelta168_tarea4_op_v_01 as R   # noqa: E402

if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    raise SystemExit(R.prueba_de_mutacion())
