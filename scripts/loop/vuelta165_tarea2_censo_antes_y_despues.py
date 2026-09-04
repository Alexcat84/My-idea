# -*- coding: utf-8 -*-
r"""vuelta165_tarea2_censo_antes_y_despues.py . LA MEDICION DEL CENSO ANTES Y
DESPUES DEL ARREGLO (TAREA 2 de la vuelta 165), Y LA CADENA CERRADA QUE LA
TAREA 3 TIENE QUE PUBLICAR.

POR QUE ESTE FICHERO EXISTE: `EJECUTOR.md` 1, "LA TABLA SE CUENTA DE SU
FICHERO". Toda cifra del reporte cita el fichero de salida del que sale y se
reconstruye contando ese fichero. Esta es esa salida.

QUE IMPRIME:
  A) la cadena de la caida de reporte de la 164, CERRADA, con el patron VIEJO,
     que es el universo en el que esa cadena se escribio: 92 vistos por el
     censo, 53 en la nomina, 51 visibles, 41 fuera.
  B) la misma cadena con el patron NUEVO.
  C) LOS 41 PRE 148 con nombre y apellido, que es el universo de la TAREA 4.
     Se computan con el patron VIEJO A PROPOSITO: son los 41 que el acta 164
     nombra y adjudica, no un conjunto que esta vuelta se invente.
  D) la poblacion NUEVA que el ensanche del patron hace visible y que NADIE ha
     adjudicado, declarada como lo que es y no metida en la TAREA 4.

CERO ESCRITURAS Y CERO EFECTOS: solo lee el directorio y la nomina.

USO:  python scripts/loop/vuelta165_tarea2_censo_antes_y_despues.py
"""
import os
import re
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import verificar_mutaciones_viejas as B   # noqa: E402

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def censo_con(patron):
    return sorted(n for n in os.listdir(B.LOOP) if patron.match(n))


def _git(args):
    r = subprocess.run(["git"] + args, cwd=RAIZ, capture_output=True)
    if r.returncode != 0:
        raise SystemExit("ROJO: git %s fallo" % " ".join(args))
    return r.stdout.decode("utf-8", errors="replace")


def cadena_en_el_arbol(ref):
    """LA CADENA CON EL PATRON VIEJO TAL COMO ESTABA EN UN ARBOL DE GIT.

    Hace falta porque la apertura de esta vuelta y su cierre NO pueden dar lo
    mismo: la propia vuelta anade arneses a la nomina y al directorio. La cifra
    de apertura se lee del arbol, no de la memoria."""
    ficheros = [l.split("/")[-1] for l in _git(
        ["ls-tree", "--name-only", "%s:scripts/loop" % ref]).split("\n") if l.strip()]
    fuente = _git(["show", "%s:scripts/loop/verificar_mutaciones_viejas.py" % ref])
    bloque = fuente.split("VIEJAS = [", 1)[1].split("\n]", 1)[0]
    nomina = re.findall(r'\(\s*"([^"]+\.py)"\s*,\s*(?:True|False)\s*\)', bloque)
    censo = sorted(n for n in ficheros if B.PATRON_ARNES_VIEJO.match(n))
    visibles = [n for n in nomina if B.PATRON_ARNES_VIEJO.match(n)]
    fuera = [n for n in censo if n not in set(nomina)]
    return censo, nomina, visibles, fuera


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    print("=" * 78)
    print("VUELTA 165, TAREA 2: EL CENSO DE ARNESES, ANTES Y DESPUES DEL ARREGLO")
    print("=" * 78)
    print("")

    print("A0) LA CADENA EN LA APERTURA DE ESTA VUELTA, LEIDA DEL ARBOL DE GIT")
    print("    (no de la memoria y no del acta: `git ls-tree` sobre scripts/loop/ y")
    print("    la nomina sacada del fuente de ESE arbol. Hace falta porque la propia")
    print("    vuelta 165 anade arneses, asi que apertura y cierre no pueden coincidir)")
    for etiqueta, ref in (("acta 164, que es donde el auditor midio", "2c00a1c0"),
                          ("apertura de la 165, hijo directo del acta", "d6fa3df1")):
        c, nm, vi, fu = cadena_en_el_arbol(ref)
        print("    %s (%s):" % (etiqueta, ref))
        print("      vistos por el censo viejo %d | nomina %d | visibles %d | fuera %d"
              % (len(c), len(nm), len(vi), len(fu)))
        print("      la resta que cierra: %d menos %d es %d"
              % (len(c), len(vi), len(c) - len(vi)))
    print("")

    nomina = [s for s, _a in B.VIEJAS]
    viejo = censo_con(B.PATRON_ARNES_VIEJO)
    nuevo = censo_con(B.PATRON_ARNES)

    print("A) LA CADENA DE LA CAIDA DE REPORTE DE LA 164, CON EL PATRON VIEJO")
    print("   (es el universo en el que esa cadena se escribio, y es el que la")
    print("   adjudicacion 6.4 del acta 164 manda publicar entero y cerrado)")
    vis_viejo = [n for n in nomina if B.PATRON_ARNES_VIEJO.match(n)]
    fuera_viejo = [n for n in viejo if n not in set(nomina)]
    print("   CIFRA vistos por el censo VIEJO: %d" % len(viejo))
    print("   CIFRA entradas en la nomina: %d" % len(nomina))
    print("   CIFRA de esas entradas VISIBLES al censo viejo: %d" % len(vis_viejo))
    print("   CIFRA fuera de la nomina: %d" % len(fuera_viejo))
    print("   LA RESTA QUE CIERRA: %d menos %d es %d"
          % (len(viejo), len(vis_viejo), len(viejo) - len(vis_viejo)))
    print("   LA RESTA QUE NO CERRABA: %d menos %d es %d, y NO es la cifra de fuera"
          % (len(viejo), len(nomina), len(viejo) - len(nomina)))
    print("")

    print("B) LA MISMA CADENA CON EL PATRON NUEVO")
    vis_nuevo = [n for n in nomina if B.PATRON_ARNES.match(n)]
    fuera_nuevo = [n for n in nuevo if n not in set(nomina)]
    print("   CIFRA vistos por el censo NUEVO: %d" % len(nuevo))
    print("   CIFRA entradas en la nomina: %d" % len(nomina))
    print("   CIFRA de esas entradas VISIBLES al censo nuevo: %d" % len(vis_nuevo))
    print("   CIFRA entradas de la nomina INVISIBLES al censo nuevo: %d"
          % len(B.nomina_invisible_al_censo()))
    print("   CIFRA fuera de la nomina: %d" % len(fuera_nuevo))
    print("   LA RESTA QUE CIERRA: %d menos %d es %d"
          % (len(nuevo), len(vis_nuevo), len(nuevo) - len(vis_nuevo)))
    ultima, faltan = B.arneses_que_faltan()
    print("   CIFRA ultima vuelta representada en la nomina: %s" % ultima)
    print("   CIFRA arneses POSTERIORES a esa vuelta que se quedan FUERA: %d (%s)"
          % (len(faltan), ", ".join(faltan) or "ninguno"))
    print("")

    print("C) LOS PRE 148 FUERA DE LA NOMINA, CON EL PATRON VIEJO")
    print("   ESTE ES EL UNIVERSO DE LA TAREA 4, y se computa con el patron VIEJO")
    print("   A PROPOSITO: son los que el acta 164 nombra y su 6.5 adjudica, no un")
    print("   conjunto que esta vuelta se invente por haber ensanchado el patron.")
    pre148_viejo = sorted(n for n in fuera_viejo if (B.vuelta_de(n) or 0) < 148)
    post_viejo = sorted(n for n in fuera_viejo if (B.vuelta_de(n) or 0) >= 148)
    print("   CIFRA pre 148 fuera de la nomina (patron viejo): %d" % len(pre148_viejo))
    print("   CIFRA 148 o posteriores fuera de la nomina (patron viejo): %d"
          % len(post_viejo))
    for i, n in enumerate(pre148_viejo, 1):
        print("   %3d. %s" % (i, n))
    print("")

    print("D) LA POBLACION QUE EL ENSANCHE HACE VISIBLE Y QUE NADIE HA ADJUDICADO")
    print("   NO ENTRA EN LA TAREA 4 Y NO SE MIDE AQUI: se declara y se deja")
    print("   escrita para quien tenga que decidir, que es lo que la 6.5 hizo")
    print("   con los 41. Ninguna de estas es reclamada por el verde de la")
    print("   bateria, porque todas son ANTERIORES a la ultima vuelta de la")
    print("   nomina y la regla solo reclama a las posteriores.")
    nuevas = sorted(set(fuera_nuevo) - set(fuera_viejo))
    print("   CIFRA arneses que el ensanche hace visibles y estan fuera: %d" % len(nuevas))
    print("   CIFRA de esas que son posteriores a la ultima vuelta de la nomina: %d"
          % len([n for n in nuevas if (B.vuelta_de(n) or 0) > (ultima or 0)]))
    for i, n in enumerate(nuevas, 1):
        print("   %3d. %s (vuelta %s)" % (i, n, B.vuelta_de(n)))
    print("")

    print("E) LO QUE NO SE MUEVE, DICHO CON SU CIFRA")
    print("   CIFRA entradas en la nomina antes y despues del arreglo: %d" % len(nomina))
    print("   (el arreglo NO recorta ni amplia la nomina: cambia lo que el censo VE)")
    print("")
    print("FIN")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
