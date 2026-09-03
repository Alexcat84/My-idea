# -*- coding: utf-8 -*-
r"""vuelta164_tarea1_mutacion_registro.py . ARNES DE MUTACION DEL REGISTRADOR DEL
ACTA 163 (TAREA 1 de la vuelta 164), CON NOMBRE DE ARNES.

POR QUE EXISTE ESTE FICHERO Y NO SOLO EL FLAG `--mutar`. La bateria
`scripts/loop/verificar_mutaciones_viejas.py` invoca cada arnes SIN ARGUMENTOS y
su censo reconoce lo que se llama `vuelta<N>...mutacion...py`. Una prueba que
vive detras de un `--mutar` de otro fichero no la ve la bateria, y esa es
justamente la ceguera que la adjudicacion 6.8 del acta 162 cerro.

NO HAY COPIA DE LA PRUEBA AQUI: se IMPORTA y se llama. Una sola fuente.

SUJETO: fabricado EN MEMORIA (actas de mentira como listas de lineas, series de
mentira como listas de tuplas) mas el acta real leida hoy. CERO escrituras.

USO:  python scripts/loop/vuelta164_tarea1_mutacion_registro.py
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import vuelta164_tarea1_registrar_acta163 as R   # noqa: E402

if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    raise SystemExit(R.prueba_de_mutacion())
