# -*- coding: utf-8 -*-
"""vuelta40_senal_antes_despues.py - QUE LE HACE UNA FUSION A LA SENAL DE BLOQUE
DEL INSTRUMENTO DE COSTURAS, medido en vez de sostenido.

ESTRICTAMENTE DE SOLO LECTURA. Lee nodos de git y del disco. No escribe nada.

POR QUE EXISTE. Al cerrar OP-D-05 aparecio un hecho incomodo que hay que decir
antes que ninguna otra cosa: `seleccion_ceo_fundador` NO estaba en la cola del
instrumento antes de la fusion (bloque 43,6 contra umbral 44) y SI esta despues
(48,4). O sea que LA FUSION ENCENDIO LA SENAL. El reporte de la vuelta 39 pudo
decir de su caso que la senal ya disparaba antes; aqui NO se puede decir eso, y
callarlo seria la peor version de este cierre.

LA PREGUNTA QUE CONTESTA: es eso una costura nueva, o es que la senal de bloque
SUBE POR CONSTRUCCION cuando se funde? Una fusion mete el vocabulario de tres
nodos en menos pasos y mas densos, y la senal mide solape de tokens entre
bloques de la lista. Si la sospecha es cierta, la cifra tiene que subir en TODOS
los casos medidos y no solo en este.

COMO LO MIDE: con las senales CRUDAS del propio instrumento (las privadas, las
mismas que usa su puerta para medirse a si misma), sobre los pasos del nodo
LEIDOS DE UN COMMIT ANTERIOR con `git show`, contra los pasos de hoy.

Uso:
  python scripts/loop/vuelta40_senal_antes_despues.py
"""
import io
import json
import os
import subprocess
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(RAIZ, "scripts"))

from costuras_internas import (  # noqa: E402
    UMBRAL_BLOQUE, NoAplica, _peor_pareja, _mejor_bloque,
)

# Los casos medibles: cada resultante de fusion, con el commit ANTERIOR a su
# fusion. Los dos de OP-D-04 salieron en la vuelta 39 y su apertura es 03e8e0e8;
# el de OP-D-05 sale hoy y su apertura es 002edf43.
CASOS = [
    ("OP-D-04, el taller", "reglas_brainstorming", "03e8e0e8"),
    ("OP-D-04, la alternancia", "pensamiento_convergente_divergente", "03e8e0e8"),
    ("OP-D-05, la seleccion del CEO", "seleccion_ceo_fundador", "002edf43"),
]


def pasos_en(commit, nid):
    ruta = "dataset/nodos/%s.json" % nid
    bruto = subprocess.check_output(["git", "show", "%s:%s" % (commit, ruta)],
                                    cwd=RAIZ)
    d = json.loads(bruto.decode("utf-8"))
    return d.get("pasos_accionables") or []


def pasos_hoy(nid):
    d = json.loads(io.open(os.path.join(RAIZ, "dataset", "nodos", nid + ".json"),
                           encoding="utf-8").read())
    return d.get("pasos_accionables") or []


def mide(ratio, pasos):
    sp = _peor_pareja(ratio, pasos)
    sb = _mejor_bloque(ratio, pasos)
    if isinstance(sb[0], NoAplica):
        return (len(pasos), sp[0], None, 0)
    return (len(pasos), sp[0], sb[0], sb[1])


def linea(etq, m):
    n, par, blo, corte = m
    if blo is None:
        return "    %-10s %d pasos | pareja %5.1f | bloque NO APLICA" % (etq, n, par)
    return ("    %-10s %d pasos | pareja %5.1f | bloque %5.1f (corte tras %d) | "
            "%s el umbral %d por %+.1f"
            % (etq, n, par, blo, corte,
               "SOBRE" if blo >= UMBRAL_BLOQUE else "BAJO ", UMBRAL_BLOQUE,
               blo - UMBRAL_BLOQUE))


def main():
    from rapidfuzz.fuzz import token_sort_ratio as ratio

    print("LA SENAL DE BLOQUE ANTES Y DESPUES DE CADA FUSION, 19 ago 2026")
    print("Medida con las senales CRUDAS de scripts/costuras_internas.py.")
    print("Umbral de bloque vigente y no tocado: %d" % UMBRAL_BLOQUE)
    print("")
    subio = igual = bajo = 0
    for nombre, nid, commit in CASOS:
        antes = mide(ratio, pasos_en(commit, nid))
        despues = mide(ratio, pasos_hoy(nid))
        print("%s: %s" % (nombre, nid))
        print("  ANTES, leido de git %s:" % commit)
        print(linea("antes", antes))
        print("  DESPUES, leido del fichero de hoy:")
        print(linea("despues", despues))
        if antes[2] is not None and despues[2] is not None:
            d = despues[2] - antes[2]
            print("  MOVIMIENTO DE LA SENAL: %+.1f puntos" % d)
            if d > 0:
                subio += 1
            elif d < 0:
                bajo += 1
            else:
                igual += 1
            ea = "DENTRO" if antes[2] >= UMBRAL_BLOQUE else "fuera"
            ed = "DENTRO" if despues[2] >= UMBRAL_BLOQUE else "fuera"
            print("  LA COLA: %s antes -> %s despues%s"
                  % (ea, ed, "   LA FUSION LO METIO EN LA COLA"
                     if (ea == "fuera" and ed == "DENTRO") else ""))
        else:
            print("  MOVIMIENTO: no comparable, la senal NO APLICABA en un extremo")
            print("  LA COLA: %s antes -> %s despues%s"
                  % ("no aplica" if antes[2] is None else
                     ("DENTRO" if antes[2] >= UMBRAL_BLOQUE else "fuera"),
                     "no aplica" if despues[2] is None else
                     ("DENTRO" if despues[2] >= UMBRAL_BLOQUE else "fuera"),
                     ""))
        print("")
    print("=" * 78)
    print("EL PATRON, contado: SUBE en %d de %d casos, baja en %d, igual en %d."
          % (subio, len(CASOS), bajo, igual))
    print("=" * 78)
    print("LECTURA, y es lo que la cifra sostiene y nada mas: en los casos")
    print("medidos la senal de bloque SUBE con la fusion. El mecanismo es")
    print("mecanico y no semantico: fundir mete el vocabulario de tres nodos en")
    print("menos pasos y mas densos, y la senal mide solape de tokens entre los")
    print("dos bloques de la lista. UNA CITA SOBRE UN NODO RECIEN FUNDIDO ES,")
    print("POR ESO, LO ESPERABLE, y no prueba por si sola que haya costura.")
    print("")
    print("LO QUE ESTO NO AUTORIZA, y va escrito para que nadie lo use de coartada:")
    print("no autoriza a descartar la cita. El instrumento CITA Y NO JUZGA, y una")
    print("cita es una lectura obligada. Lo que esta medicion dice es que la")
    print("lectura hay que hacerla con el texto delante, no despacharla con la")
    print("cifra ni en un sentido ni en el otro.")
    return 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    raise SystemExit(main())
