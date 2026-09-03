# -*- coding: utf-8 -*-
r"""vuelta163_tarea1c_mutacion_tramo.py . ARNES DE MUTACION DE EL TRAMO AL DOBLE CONTADO DEL REGISTRO (TAREA 1.c),
CON NOMBRE DE ARNES.

POR QUE EXISTE ESTE FICHERO Y NO SOLO EL FLAG. La bateria
`scripts/loop/verificar_mutaciones_viejas.py` invoca cada arnes SIN ARGUMENTOS,
y su censo de arneses reconoce lo que se llama `vuelta<N>...mutacion...py`. Una
bateria que vive detras de un `--mutacion` de otro fichero NO la ve nadie, y esa
es exactamente la ceguera que la adjudicacion 6.8 del acta 162 vino a cerrar en
esta misma vuelta: seria absurdo abrir el agujero por el otro lado el mismo dia
que se tapa.

NO HAY COPIA DE LA BATERIA AQUI: se IMPORTA y se llama. Una sola fuente.

USO:  python scripts/loop/vuelta163_tarea1c_mutacion_tramo.py
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import vuelta163_tarea1c_tramo_al_doble as B   # noqa: E402

if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    raise SystemExit(B.prueba_de_mutacion())
