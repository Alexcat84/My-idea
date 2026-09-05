# -*- coding: utf-8 -*-
r"""_v178_arneses_que_faltan_viejo_copia.py . LA VERSION VIEJA DE
`arneses_que_faltan()`, CONGELADA AQUI PARA PODER CORRERLA EN ROJO.

NO ES CODIGO VIVO Y NO ENTRA EN NINGUNA NOMINA. Empieza por guion bajo a
proposito: `PATRON_ARNES` de `scripts/loop/verificar_mutaciones_viejas.py` exige
que el nombre empiece por `vuelta<N>`, asi que este fichero NO lo ve el censo y
NO tiene que entrar en `VIEJAS`. Es el mismo patron de casa que
`_v156_tallador_viejo_copia.py` y `_v163_contador_viejo_copia.py`.

POR QUE EXISTE. El encargo de la vuelta 178, TAREA 1.b, pide publicar LAS DOS
CORRIDAS del mismo caso, la vieja en ROJO y la nueva en VERDE. Sin una copia
congelada de la funcion vieja no hay nada que correr en rojo: el fichero vivo ya
esta arreglado, y un caso rojo que no se puede correr no es una prueba
(`EJECUTOR.md` 1, "EL CASO ROJO SE PRUEBA POR MUTACION").

EL CUERPO ES BYTE A BYTE EL DE ANTES DE LA VUELTA 178, y lo unico que se le
quita es el docstring de la funcion, que aqui se sustituye por esta nota. La
version viva de la que se copio esta en git: `verificar_mutaciones_viejas.py` en
el commit de apertura de la 178. El cotejo se puede rehacer con
`git show <apertura>:scripts/loop/verificar_mutaciones_viejas.py`.

EL FILTRO VIEJO, QUE ES LO QUE ESTE FICHERO CONSERVA PARA QUE SE PUEDA VER:

    fuera = [n for n in arneses_del_directorio(directorio)
             if n not in dentro and (vuelta_de(n) or 0) > ultima]

Ese `>` es la ceguera entera: un arnes de LA MISMA VUELTA que la ultima de la
nomina no puede aparecer nunca, dijera lo que dijera el censo.

USO: se importa desde `scripts/loop/vuelta178_tarea1b_mutacion_hermano.py`.
"""
import os
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)
import verificar_mutaciones_viejas as V   # noqa: E402


def arneses_que_faltan_viejo(nomina=None, directorio=None):
    """LA VERSION ANTERIOR A LA VUELTA 178. Congelada. No se arregla aqui: este
    fichero existe para que se la pueda ver fallar."""
    nombres = [s for s, _admite in (nomina if nomina is not None else V.VIEJAS)]
    vueltas = [v for v in (V.vuelta_de(n) for n in nombres) if v is not None]
    if not vueltas:
        return None, []
    ultima = max(vueltas)
    dentro = set(nombres)
    fuera = [n for n in V.arneses_del_directorio(directorio)
             if n not in dentro and (V.vuelta_de(n) or 0) > ultima]
    return ultima, sorted(fuera)
