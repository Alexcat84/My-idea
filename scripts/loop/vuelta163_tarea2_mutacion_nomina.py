# -*- coding: utf-8 -*-
r"""vuelta163_tarea2_mutacion_nomina.py . ARNES DE MUTACION DE LA MIRADA DE LA
NOMINA SOBRE SI MISMA (vuelta 163, TAREA 2; adjudicacion 6.8 del acta 162).

POR QUE EXISTE ESTE FICHERO Y NO SOLO EL FLAG `--mutar-nomina`: la bateria
invoca cada arnes SIN ARGUMENTOS y su censo reconoce lo que se llama
`vuelta<N>...mutacion...py`. Una bateria que vive detras del flag de otro
fichero no la ve nadie, que es la ceguera que esta misma vuelta viene a cerrar.

NO HAY COPIA DE LA BATERIA AQUI: se IMPORTA y se llama. Una sola fuente.

Y SE DICE LO QUE TIENE DE RARO, PORQUE ES RARO: este arnes prueba la guarda que
LO CONTIENE, y por eso su caso (E) corre sobre el repo de verdad y exige que HOY
no falte ninguno. El dia que alguien escriba un arnes nuevo y no lo meta en la
nomina, este arnes CAE, y con el cae la bateria entera.

USO:  python scripts/loop/vuelta163_tarea2_mutacion_nomina.py
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import verificar_mutaciones_viejas as B   # noqa: E402

if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    raise SystemExit(B.prueba_de_la_nomina())
