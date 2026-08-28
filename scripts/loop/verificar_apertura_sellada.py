# -*- coding: utf-8 -*-
r"""verificar_apertura_sellada.py . LA GUARDA DE LA APERTURA (TAREA 1.2 de la
vuelta 101, acta de la vuelta 100, seccion "SEGUNDA CAIDA, DE INCUMPLIMIENTO
DE ENCARGO"). Nombre estable, SIN numero de vuelta (como
tallar_cabecera_reporte.py y contar_cierre_efectivo.py): se invoca con
--vuelta N y no se clona cada vuelta.

POR QUE NACE. EJECUTOR.md 1 dice, desde el 14 ago 2026, "LA APERTURA SE MIDE
ANTES DE LA PRIMERA OPERACION". La vuelta 99 ya habia caido en esto una vez
(acta 99). La vuelta 100 volvio a caer, y peor: SALIDA_V100_HEAD_APERTURA.txt
SI nacio en el primer commit de la vuelta (300802d1, hijo directo de
c8827ef7, el acta de la vuelta 99), pero los OCHO ficheros
SALIDA_V100_*_APERTURA.txt restantes (GATE0_CMD1, CONTEO, DESFASE_CALIBRADO,
ETIQUETAS, MOTOR, SYNC, TSC, WEB) nacieron TODOS en 592cf8bc, el ULTIMO
commit de la vuelta, junto con el reporte final. Nadie lo habia comprobado
con una guarda: el auditor tuvo que medirlo a mano con `git log
--diff-filter=A` sobre cada fichero. Esta guarda automatiza esa medicion.

QUE COMPRUEBA. La vara la da git, no se inventa (EJECUTOR.md, "LA IDENTIDAD
SE LEE DE GIT"): el COMMIT DE NACIMIENTO de cada
`docs/loop/SALIDA_V<vuelta>_*_APERTURA.txt` (el commit que lo ANADE, via
`git log --diff-filter=A`) tiene que ser el PRIMER commit de la vuelta, es
decir, el HIJO DIRECTO del commit del acta de la vuelta anterior (el commit
cuyo mensaje empieza por "ACTA DE LA VUELTA <vuelta-1> DEL AUDITOR", el mismo
patron que ya usa `tallar_cabecera_reporte.py`). Cae en ROJO si:
  - no hay ningun commit "ACTA DE LA VUELTA <vuelta-1> DEL AUDITOR" en la
    rama, o hay mas de uno (ambiguo);
  - algun `SALIDA_V<vuelta>_*_APERTURA.txt` no existe en el arbol de trabajo;
  - algun fichero de apertura no tiene EXACTAMENTE un commit que lo anada
    (cero o mas de uno: ambiguo o no versionado);
  - el PADRE del commit que anade un fichero de apertura NO es el commit del
    acta (nacio despues del primer commit, a mitad o al final de la vuelta).

Nunca inventa un hash ni asume una fecha: todo se lee de `git log` de la rama
actual (`git rev-parse --abbrev-ref HEAD`).

USO:
  python scripts/loop/verificar_apertura_sellada.py --vuelta 101
  python scripts/loop/verificar_apertura_sellada.py --vuelta 100

PRUEBA DE MUTACION (con su salida commiteada,
docs/loop/SALIDA_V101_TAREA1_2_MUTACION_APERTURA.txt): (a) VERDE sobre la
vuelta 101 (bien sellada, con TODOS sus `*_APERTURA.txt` en el primer commit
de la vuelta); (b) ROJO sobre la vuelta 100, el caso negativo real, sin
inventar nada: nombra los ocho ficheros que nacieron en 592cf8bc en vez de en
300802d1.
"""
import argparse
import glob
import os
import re
import subprocess

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOOP = os.path.join(RAIZ, "docs", "loop")


def _git(args, fallos, contexto):
    try:
        r = subprocess.run(["git"] + args, cwd=RAIZ, capture_output=True, text=True, check=True)
        return r.stdout
    except Exception as e:
        fallos.append("no se pudo correr git %s (%s): %s" % (" ".join(args), contexto, e))
        return None


def rama_actual(fallos):
    out = _git(["rev-parse", "--abbrev-ref", "HEAD"], fallos, "rama actual")
    return out.strip() if out is not None else None


def commit_acta(vuelta, rama, fallos):
    """Commit cuyo mensaje empieza por 'ACTA DE LA VUELTA <vuelta-1> DEL
    AUDITOR', igual que tallar_cabecera_reporte.py:commit_apertura_desde_git."""
    out = _git(["log", rama, "--pretty=format:%H\x01%s"], fallos, "git log de la rama")
    if out is None:
        return None
    patron = re.compile(r"^ACTA DE LA VUELTA %d DEL AUDITOR\b" % (vuelta - 1))
    hallados = []
    for linea in out.splitlines():
        if "\x01" not in linea:
            continue
        h, s = linea.split("\x01", 1)
        if patron.match(s):
            hallados.append(h)
    if not hallados:
        fallos.append("git log de la rama %s no trae ningun commit 'ACTA DE LA VUELTA %d "
                      "DEL AUDITOR': no se puede fijar el commit de referencia" % (rama, vuelta - 1))
        return None
    if len(hallados) > 1:
        fallos.append("git log de la rama %s trae %d commits 'ACTA DE LA VUELTA %d DEL "
                      "AUDITOR' (%s): ambiguo" % (rama, len(hallados), vuelta - 1,
                                                    ", ".join(h[:8] for h in hallados)))
        return None
    return hallados[0]


def ficheros_apertura(vuelta):
    patron = os.path.join(LOOP, "SALIDA_V%d_*_APERTURA.txt" % vuelta)
    return sorted(os.path.basename(p) for p in glob.glob(patron))


def commit_de_nacimiento(nombre, rama, fallos):
    rel = "docs/loop/%s" % nombre
    out = _git(["log", rama, "--diff-filter=A", "--pretty=format:%H", "--", rel],
               fallos, "nacimiento de %s" % nombre)
    if out is None:
        return None
    hallados = [h for h in out.splitlines() if h.strip()]
    if not hallados:
        fallos.append("%s: ningun commit lo anade (no versionado)" % nombre)
        return None
    if len(hallados) > 1:
        fallos.append("%s: %d commits lo anaden (%s): ambiguo" %
                      (nombre, len(hallados), ", ".join(h[:8] for h in hallados)))
        return None
    return hallados[0]


def verificar(vuelta):
    fallos = []
    rama = rama_actual(fallos)
    if rama is None:
        return fallos, []
    acta = commit_acta(vuelta, rama, fallos)
    if acta is None:
        return fallos, []

    nombres = ficheros_apertura(vuelta)
    if not nombres:
        fallos.append("no existe ningun docs/loop/SALIDA_V%d_*_APERTURA.txt en el arbol de trabajo" % vuelta)
        return fallos, []

    detalle = []
    for nombre in nombres:
        nacido_en = commit_de_nacimiento(nombre, rama, fallos)
        if nacido_en is None:
            continue
        padre_out = _git(["rev-parse", "%s^" % nacido_en], fallos, "padre de %s" % nacido_en)
        padre = padre_out.strip() if padre_out is not None else None
        if padre is None:
            continue
        if padre != acta:
            fallos.append("%s nacio en %s, cuyo padre es %s (no el commit del acta %s): "
                          "no se sello antes de la 1.a operacion" %
                          (nombre, nacido_en[:8], padre[:8], acta[:8]))
        detalle.append((nombre, nacido_en[:8], padre[:8] if padre else "?", padre == acta))
    return fallos, detalle


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--vuelta", type=int, required=True)
    a = ap.parse_args()

    fallos, detalle = verificar(a.vuelta)
    if fallos:
        print("ROJO, apertura de la vuelta %d NO sellada antes de la 1.a operacion "
              "(%d cosa(s) no cuadran):" % (a.vuelta, len(fallos)))
        for x in fallos:
            print("   %s" % x)
        return 1

    print("VERDE: los %d ficheros SALIDA_V%d_*_APERTURA.txt nacieron todos en el "
          "primer commit de la vuelta (hijo directo del acta):" % (len(detalle), a.vuelta))
    for nombre, nacido_en, padre, ok in detalle:
        print("   %s -- nacido en %s, padre %s" % (nombre, nacido_en, padre))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
