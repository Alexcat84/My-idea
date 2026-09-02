# -*- coding: utf-8 -*-
"""vuelta144_3b_mutacion_negativa.py . LA MUTACION NEGATIVA DE LA TAREA 3.b.

QUE PRUEBA. Que las guardas PROPIAS del sellador nuevo
(`vuelta144_3b_sellar_mesa_opm04.py`) MUERDEN, y que cuando muerden NO SE
ESCRIBE NADA: ni el plan ni un nodo.

TRES CASOS, todos EN MEMORIA, todos con `--simular` puesto para que ni en el
peor caso se toque el disco, y todos con la cifra leida de la salida real y
nunca contra un literal (EJECUTOR.md regla 1):

  (A) EL EMPAREJAMIENTO CAMBIADO. Se intercambian los absorbidos de los dos
      contenidos: el superviviente de la 367 pasa a absorber el gemelo de la 328
      y al reves. LA GUARDA 5 tiene que caer nombrando los dos repartos, el del
      contenido y el que la ficha declara. Es la guarda propia de este
      instrumento y la unica que ninguna de las del generador cubre.
  (B) LA MARCA QUE APUNTA FUERA. Se le pone a un paso una marca CUBIERTO a un
      numero mayor que los pasos del superviviente. Tiene que caer la aritmetica
      del generador, IMPORTADA y no copiada, que es justo lo que se quiere
      probar: que al no relajar ninguna guarda, las del generador siguen
      mordiendo dentro del sellador nuevo.
  (C) LA CONTRAPRUEBA. Sin mutar nada, el sellador sale VERDE. Sin ella, dos
      rojos no prueban nada.

Y AL FINAL, LA CUENTA QUE MANDA: `git status --porcelain -- dataset/ docs/loop/`
tiene que salir IGUAL que al empezar. Cero escrituras.
"""
import copy
import os
import subprocess
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOOP = os.path.join(RAIZ, "scripts", "loop")
sys.path.insert(0, LOOP)

import _v144_opm04_328 as C328  # noqa: E402
import _v144_opm04_367 as C367  # noqa: E402
import vuelta144_3b_sellar_mesa_opm04 as S  # noqa: E402


def estado():
    return subprocess.run(["git", "status", "--porcelain", "--", "dataset/", "docs/loop/"],
                          cwd=RAIZ, capture_output=True, text=True).stdout


class Capturada(object):
    def __init__(self):
        self.trozos = []

    def write(self, s):
        self.trozos.append(s)
        return len(s)

    def flush(self):
        pass

    def reconfigure(self, **kw):
        return None

    def valor(self):
        return "".join(self.trozos)


def correr(argv):
    real_argv, real_out = sys.argv, sys.stdout
    buf = Capturada()
    try:
        sys.argv = argv
        sys.stdout = buf
        try:
            codigo = S.main()
        except SystemExit as e:
            codigo = e.code if isinstance(e.code, int) else 1
    finally:
        sys.argv, sys.stdout = real_argv, real_out
    return codigo, buf.valor()


def main():
    argv = ["vuelta144_3b_sellar_mesa_opm04.py", "--simular"]
    antes = estado()
    guardadas = (copy.deepcopy(C367.FUSION), copy.deepcopy(C328.FUSION))

    print("MUTACION NEGATIVA DE LA TAREA 3.b | vuelta 144")
    print("Todo EN MEMORIA y con --simular: ni el plan ni un nodo se tocan.")
    print("=" * 78)

    resultados = []
    try:
        # ---- (C) LA CONTRAPRUEBA, primero -----------------------------------
        cod_c, sal_c = correr(argv)
        ok_c = cod_c == 0 and "SIMULACION: el plan NO se escribe" in sal_c
        print("(C) CONTRAPRUEBA, sin mutar nada: codigo %r" % cod_c)
        print("     VEREDICTO: %s" % ("OK" if ok_c else "ROJO"))
        resultados.append(("(C) contraprueba, el sellador sale VERDE", ok_c))
        print("")

        # ---- (A) EL EMPAREJAMIENTO CAMBIADO ---------------------------------
        a367, a328 = C367.FUSION["absorbidos"], C328.FUSION["absorbidos"]
        C367.FUSION["absorbidos"] = list(a328)
        C367.FUSION["pasos"] = {a328[0]: {}}
        C367.FUSION["condiciones"] = {a328[0]: {}}
        C328.FUSION["absorbidos"] = list(a367)
        C328.FUSION["pasos"] = {a367[0]: {}}
        C328.FUSION["condiciones"] = {a367[0]: {}}
        cod_a, sal_a = correr(argv)
        cae_guarda5 = "guarda 5, el emparejamiento del contenido calza con el de la ficha: ROJO" in sal_a
        nombra = "NO es el que la ficha declara" in sal_a
        no_escribe = "NO se escribe nada" in sal_a
        ok_a = cod_a != 0 and cae_guarda5 and nombra and no_escribe
        print("(A) EMPAREJAMIENTO CAMBIADO (los dos absorbidos intercambiados):")
        print("     codigo %r | la guarda 5 cae: %s | nombra los dos repartos: %s | no "
              "escribe nada: %s" % (cod_a, cae_guarda5, nombra, no_escribe))
        for ln in sal_a.splitlines():
            if "guarda 5" in ln or "NO es el que la ficha declara" in ln:
                print("     %s" % ln.strip()[:180])
        print("     VEREDICTO: %s" % ("OK" if ok_a else "ROJO"))
        resultados.append(("(A) emparejamiento cambiado, cae la guarda 5", ok_a))
        print("")

        # ---- (B) LA MARCA QUE APUNTA FUERA ----------------------------------
        C367.FUSION.update(copy.deepcopy(guardadas[0]))
        C328.FUSION.update(copy.deepcopy(guardadas[1]))
        ab = C367.FUSION["absorbidos"][0]
        fuera = 99
        C367.FUSION["pasos"] = copy.deepcopy(C367.FUSION["pasos"])
        C367.FUSION["pasos"][ab]["1"] = ["CUBIERTO", fuera]
        cod_b, sal_b = correr(argv)
        cae_aritmetica = "CUBIERTO:%d y el superviviente tiene" % fuera in sal_b
        no_escribe_b = "NO se escribe nada" in sal_b
        ok_b = cod_b != 0 and cae_aritmetica and no_escribe_b
        print("(B) MARCA CUBIERTO:%d, fuera del rango del superviviente:" % fuera)
        print("     codigo %r | cae la aritmetica IMPORTADA del generador: %s | no escribe "
              "nada: %s" % (cod_b, cae_aritmetica, no_escribe_b))
        for ln in sal_b.splitlines():
            if "CUBIERTO:%d" % fuera in ln:
                print("     %s" % ln.strip()[:180])
        print("     VEREDICTO: %s" % ("OK" if ok_b else "ROJO"))
        resultados.append(("(B) marca fuera de rango, cae la aritmetica", ok_b))
        print("")
    finally:
        C367.FUSION.clear()
        C367.FUSION.update(guardadas[0])
        C328.FUSION.clear()
        C328.FUSION.update(guardadas[1])

    despues = estado()
    igual = despues == antes
    print("=" * 78)
    buenas = sum(1 for _, ok in resultados if ok)
    for nombre, ok in resultados:
        print("  %-48s %s" % (nombre, "OK" if ok else "ROJO"))
    print("")
    print("CERO ESCRITURAS: git status -- dataset/ docs/loop/ identico al de la apertura "
          "del arnes: %s" % igual)
    print("")
    print("COMPROBACIONES QUE MUERDEN: %d de %d" % (buenas, len(resultados)))
    return 0 if buenas == len(resultados) and igual else 1


if __name__ == "__main__":
    raise SystemExit(main())
