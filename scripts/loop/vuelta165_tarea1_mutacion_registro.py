# -*- coding: utf-8 -*-
r"""vuelta165_tarea1_mutacion_registro.py . ARNES DE MUTACION DEL REGISTRADOR
DEL ACTA 164 (TAREA 1 de la vuelta 165), CON NOMBRE DE ARNES.

POR QUE EXISTE ESTE FICHERO Y NO SOLO EL FLAG `--mutar`. La bateria
`scripts/loop/verificar_mutaciones_viejas.py` invoca cada arnes SIN ARGUMENTOS.
Una prueba que vive detras de un `--mutar` de otro fichero no la corre nadie
desde la bateria.

NO HAY COPIA DE LA PRUEBA AQUI: se IMPORTA y se llama. Una sola fuente.

SUJETO: fabricado EN MEMORIA (actas de mentira como listas de lineas) mas el
acta real leida hoy. CERO escrituras.

USO:  python scripts/loop/vuelta165_tarea1_mutacion_registro.py
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import vuelta165_tarea1_registrar_acta164 as R   # noqa: E402

if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    raise SystemExit(R.prueba_de_mutacion())
