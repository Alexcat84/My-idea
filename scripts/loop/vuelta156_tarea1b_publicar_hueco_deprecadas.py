# -*- coding: utf-8 -*-
"""vuelta156_tarea1b_publicar_hueco_deprecadas.py . TAREA 1 DE LA VUELTA 156,
SEGUNDA MITAD DE LA ADJUDICACION 6.9 DEL ACTA 155.

QUE HACE. La 6.9 tiene dos mitades. La primera ("los tres pares de fuente
deprecada NO SE LEEN y se quedan NOMBRADOS dentro de la guarda") ya estaba
cumplida y su registro por adicion lo escribe
scripts/loop/vuelta156_tarea1_registrar_adjudicaciones.py. LA SEGUNDA es esta:
"y SU CUENTA (157 menos 154) SE PUBLICA CADA VEZ QUE LA GUARDA HABLE". Un
comentario no habla cada vez: habla la LINEA DE DETALLE del check. Este script
la anade.

TODO POR ADICION. No se borra ni se reescribe una sola linea de la guarda: se
insertan lineas nuevas antes del `checks.append` y una linea nueva DENTRO de la
expresion del detalle, delante de la que ya estaba. La aditividad se mide con
`git diff --numstat` y se exige BORRADOS 0.

LA CIFRA SE COMPUTA, NO SE TECLEA: el hueco se cuenta con EL MISMO recorrido de
la guarda pero SIN exigir que el nodo de partida este vivo (vara 4 de la tabla
del acta 153, seccion 4.1). Los dos EXTREMOS siguen teniendo que resolver a
nodos VIVOS. Ningun 157 ni ningun 3 va escrito a mano en el codigo.

ES IDEMPOTENTE: si la marca ya esta, no duplica nada.

USO:  python scripts/loop/vuelta156_tarea1b_publicar_hueco_deprecadas.py
"""
import io
import os
import subprocess

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
RUTA_REL = "scripts/run_phase1.py"
RUTA = os.path.join(RAIZ, RUTA_REL)

MARCA = "_fuera_por_fuente_deprecada"

ANCLA_COMPUTO = "    _sin_cita = [f\"{_a} <-> {_b}\" for _a, _b in _bidireccionales\n"

BLOQUE_COMPUTO = '''    # ADJUDICACION 6.9 DEL ACTA 155 (2026-09-03, vuelta 156): EL HUECO DE LA
    # VARA SE CUENTA Y SE PUBLICA CADA VEZ QUE ESTA GUARDA HABLE. Mismo
    # recorrido que el de arriba, con UNA sola diferencia: no se exige que el
    # nodo de PARTIDA este vivo. Los dos EXTREMOS siguen teniendo que resolver a
    # nodos vivos, asi que lo unico que se afloja es QUIEN declara la arista.
    # Es la vara 4 de la tabla del acta 153, seccion 4.1. NINGUNA CIFRA VA
    # TECLEADA: el 157 y el 3 salen de este computo, no de una constante.
    _dirigidas_con_deprecadas = set()
    for _nid in sorted(nodos_todos):
        for _campo in ("nodos_siguientes", "nodos_previos"):
            for _dest in nodos_todos[_nid].get(_campo) or []:
                if _dest not in nodos_todos:
                    continue
                _a, _b = _resolver(_nid), _resolver(_dest)
                if (_a and _b and _a != _b
                        and _a in activos and _b in activos):
                    if _campo == "nodos_previos":
                        _dirigidas_con_deprecadas.add((_b, _a))
                    else:
                        _dirigidas_con_deprecadas.add((_a, _b))
    _bidi_con_deprecadas = sorted({tuple(sorted(_p)) for _p in _dirigidas_con_deprecadas
                                   if (_p[1], _p[0]) in _dirigidas_con_deprecadas})
    _fuera_por_fuente_deprecada = sorted(set(_bidi_con_deprecadas) - set(_bidireccionales))
'''

ANCLA_DETALLE = '         + (f": {_sin_cita[:5]}" if _sin_cita else "")),\n'

BLOQUE_DETALLE = ('         + (f" [FUERA DE ESTA VARA, decision del fundador del 14 ago 2026, '
                  'camino A: {len(_fuera_por_fuente_deprecada)} par(es) mas que solo existen '
                  'si se admite como declarante a un nodo DEPRECADO, o sea '
                  '{len(_bidi_con_deprecadas)} con ellos: '
                  '{[f\'{_x} <-> {_y}\' for _x, _y in _fuera_por_fuente_deprecada]}]"'
                  ' if _fuera_por_fuente_deprecada else "")\n')


def numstat(ruta_rel):
    r = subprocess.run(["git", "diff", "--numstat", "--", ruta_rel],
                       cwd=RAIZ, capture_output=True)
    linea = r.stdout.decode("utf-8", "replace").strip()
    if not linea:
        return 0, 0
    campos = linea.split("\t")
    return int(campos[0]), int(campos[1])


def main():
    print("=" * 78)
    print("VUELTA 156, TAREA 1.b: LA SEGUNDA MITAD DE LA ADJUDICACION 6.9.")
    print("LA CUENTA DEL HUECO SE PUBLICA CADA VEZ QUE LA GUARDA HABLE.")
    print("=" * 78)
    print("")

    texto = io.open(RUTA, encoding="utf-8").read()
    if MARCA in texto:
        print("YA ESTABA: la marca %s ya vive en %s. No se duplica nada." % (MARCA, RUTA_REL))
        return

    lineas_antes = len(texto.splitlines())
    assert texto.count(ANCLA_COMPUTO) == 1, "el ancla del computo no es unica"
    assert texto.count(ANCLA_DETALLE) == 1, "el ancla del detalle no es unica"

    texto = texto.replace(ANCLA_COMPUTO, BLOQUE_COMPUTO + ANCLA_COMPUTO)
    texto = texto.replace(ANCLA_DETALLE, BLOQUE_DETALLE + ANCLA_DETALLE)

    with io.open(RUTA, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(texto)

    lineas_despues = len(texto.splitlines())
    print("LINEAS DE %s: antes %d, despues %d, ANADIDAS %d"
          % (RUTA_REL, lineas_antes, lineas_despues, lineas_despues - lineas_antes))

    mas, menos = numstat(RUTA_REL)
    print("ADITIVIDAD MEDIDA CON git diff --numstat: +%d -%d" % (mas, menos))
    assert menos == 0, "la escritura NO fue aditiva: %d borrado(s)" % menos
    print("")
    print("CIFRA lineas anadidas a la guarda: %d linea(s)" % (lineas_despues - lineas_antes))
    print("NADA SE BORRA: las dos inserciones van DELANTE de su ancla, y el ancla queda")
    print("intacta detras.")


main()
