# -*- coding: utf-8 -*-
"""vuelta42_senal_antes_despues.py - QUE LE HACE UNA FUSION A LA SENAL DE BLOQUE
DEL INSTRUMENTO DE COSTURAS, medido en vez de sostenido, PARA UN ACTO CUALQUIERA.

ESTRICTAMENTE DE SOLO LECTURA. Lee nodos de git y del disco. No escribe nada.

SUCESOR DECLARADO de scripts/loop/vuelta40_senal_antes_despues.py, al que NO
reemplaza y cuyo codigo de medicion se reusa TAL CUAL (las mismas senales crudas
privadas de scripts/costuras_internas.py, el mismo umbral vigente y sin tocar).

LO UNICO QUE CAMBIA, y va dicho porque tocar un instrumento sellado sin motivo
escrito es peor que no tocarlo: aquel trae los CASOS TECLEADOS en una lista
(los dos de OP-D-04 y el de OP-D-05, que eran tres fusiones en total). OP-D-06
son OCHO fusiones, y anadir ocho entradas a mano a una lista tecleada es
exactamente la especie de caida que la regla 1 del EJECUTOR.md cierra en su
cuarto renglon. Aqui el caso se PASA POR ARGUMENTO y no se teclea.

QUE CONTESTA, la misma pregunta del hermano mayor: la cita del instrumento sobre
un nodo recien fundido, es una costura nueva, o la senal de bloque SUBE POR
CONSTRUCCION cuando se funde? Fundir mete el vocabulario de dos nodos en menos
pasos y mas densos, y la senal mide solape de tokens entre bloques de la lista.

Uso:
  python scripts/loop/vuelta42_senal_antes_despues.py \
      --nodo producto_unico_superior --commit b563e7a5 --nombre "OP-D-06 acto 285"
"""
import argparse
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


def pasos_en(commit, nid):
    ruta = "dataset/nodos/%s.json" % nid
    bruto = subprocess.check_output(["git", "show", "%s:%s" % (commit, ruta)],
                                    cwd=RAIZ)
    return (json.loads(bruto.decode("utf-8")).get("pasos_accionables") or [])


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
    ap = argparse.ArgumentParser()
    ap.add_argument("--nodo", required=True)
    ap.add_argument("--commit", required=True,
                    help="el commit ANTERIOR a la fusion de este acto")
    ap.add_argument("--nombre", default="(sin nombre)")
    args = ap.parse_args()

    from rapidfuzz.fuzz import token_sort_ratio as ratio

    print("LA SENAL DE BLOQUE ANTES Y DESPUES DE LA FUSION")
    print("Medida con las senales CRUDAS de scripts/costuras_internas.py.")
    print("Umbral de bloque vigente y no tocado: %d" % UMBRAL_BLOQUE)
    print("")
    antes = mide(ratio, pasos_en(args.commit, args.nodo))
    despues = mide(ratio, pasos_hoy(args.nodo))
    print("%s: %s" % (args.nombre, args.nodo))
    print("  ANTES, leido de git %s:" % args.commit)
    print(linea("antes", antes))
    print("  DESPUES, leido del fichero de hoy:")
    print(linea("despues", despues))
    if antes[2] is None or despues[2] is None:
        print("  MOVIMIENTO: no comparable, la senal NO APLICABA en un extremo")
        return 0
    d = despues[2] - antes[2]
    print("  MOVIMIENTO DE LA SENAL: %+.1f puntos" % d)
    ea = "DENTRO" if antes[2] >= UMBRAL_BLOQUE else "fuera"
    ed = "DENTRO" if despues[2] >= UMBRAL_BLOQUE else "fuera"
    print("  LA COLA: %s antes -> %s despues" % (ea, ed))
    print("")
    print("=" * 78)
    if ea == "fuera" and ed == "DENTRO":
        print("LA FUSION ENCENDIO LA SENAL: estaba FUERA de la cola y quedo DENTRO.")
        print("Hay que decirlo antes que ninguna otra cosa, como el acta 40 mando.")
    elif ea == "DENTRO" and ed == "DENTRO":
        print("LA FUSION NO ENCENDIO LA SENAL: el nodo YA ESTABA DENTRO de la cola")
        print("antes de fundirse, y sigue dentro. La cita no es nueva.")
    elif ea == "DENTRO" and ed == "fuera":
        print("LA FUSION APAGO LA SENAL: estaba DENTRO y quedo FUERA.")
    else:
        print("LA SENAL NO SE ENCENDIO: fuera antes y fuera despues.")
    print("=" * 78)
    print("Y LO QUE LA CIFRA SOSTIENE Y NADA MAS: con el umbral quieto en %d, la"
          % UMBRAL_BLOQUE)
    print("fusion puede SUBIR O BAJAR la senal de bloque, y NO HAY LEY que diga")
    print("cual de las dos. Las cuatro mediciones de la vuelta 43, selladas en")
    print("docs/loop/SALIDA_V43_ACTO{331,341,344,361}_SENAL.txt: el 331 quieto en")
    print("+0.0, el 341 en -0.7, el 344 en +1.7 y el 361 en -9.4, este ultimo")
    print("APAGANDO la senal. Lo que la mueve es MECANICO y no semantico: la")
    print("senal mide solape de tokens entre los dos bloques, asi que SUBE si las")
    print("piezas que entran REPARTEN vocabulario entre los dos bloques y BAJA si")
    print("lo CONCENTRAN en uno solo. UNA CITA SOBRE UN NODO RECIEN FUNDIDO ES,")
    print("POR CONSTRUCCION, MENOS INFORMATIVA QUE LA MISMA CITA SOBRE UN NODO")
    print("QUE NADIE TOCO. Cita y no juzga: quien decide es la lectura del texto.")
    return 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    raise SystemExit(main())
