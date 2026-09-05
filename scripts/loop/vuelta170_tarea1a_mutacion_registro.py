# -*- coding: utf-8 -*-
r"""vuelta170_tarea1a_mutacion_registro.py . ARNES DE MUTACION DEL REGISTRADOR
DEL ACTA 169 (TAREA 1.a de la vuelta 170), CON NOMBRE DE ARNES.

POR QUE EXISTE ESTE FICHERO Y NO SOLO EL FLAG `--mutar`. La bateria
`scripts/loop/verificar_mutaciones_viejas.py` invoca cada arnes SIN ARGUMENTOS.
Una prueba que vive detras de un `--mutar` de otro fichero no la corre nadie
desde la bateria. Es el mismo motivo por el que existe
`vuelta168_tarea1_mutacion_registro.py`, del que este es clon declarado.

Y POR QUE VUELVE A EXISTIR, QUE ES LO QUE HAY QUE DECIR: LA VUELTA 169 NO
ESCRIBIO EL SUYO. Su registrador (`vuelta169_tarea1_registrar_acta168.py`) se
quedo sin `prueba_de_mutacion`, y aun asi la entrada `R.38` que escribio afirma
que "el arnes hermano lo prueba por mutacion". Medido en esta vuelta con
`ls scripts/loop/ | grep mutacion_registro`: existen los de las vueltas 164,
165, 166, 167 y 168, y NO existe el de la 169. La entrada `R.39` de esta vuelta
repite esa misma frase, asi que este fichero es lo que la hace cierta. La
observacion sobre el `R.38` se trae como HALLAZGO en el reporte, no se corrige
aqui: no es mia y el encargo no me manda tocarla.

NO HAY COPIA DE LA PRUEBA AQUI: se IMPORTA y se llama. Una sola fuente.

SUJETO: fabricado EN MEMORIA (actas de mentira como listas de lineas) mas el
acta real leida hoy. CERO escrituras.

SUJETO CONGELADO, que es la condicion de entrada a la bateria desde la vuelta
148 (TAREA 2.5, adjudicacion 3.5 del acta 147): las actas de mentira son
literales de este proceso, y el acta 169 ya esta cerrada y firmada. Cuando el
auditor escriba el acta 170, el acotado de este instrumento seguira delimitando
la 169 por su cabecera siguiente, y sus dos conteos (12 y 3) no se mueven.

USO:  python scripts/loop/vuelta170_tarea1a_mutacion_registro.py
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import vuelta170_tarea1_registrar_acta169 as R   # noqa: E402

if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    raise SystemExit(R.prueba_de_mutacion())
