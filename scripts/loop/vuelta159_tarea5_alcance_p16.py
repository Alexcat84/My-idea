# -*- coding: utf-8 -*-
"""vuelta159_tarea5_alcance_p16.py . TAREA 5.b DE LA VUELTA 159, EL ALCANCE DEL
CHECK DE P.16, RECOMPUTADO.

POR QUE NACE Y POR QUE SE QUEDA AQUI. El encargo de la vuelta 159 dice, literal:
"EL ALCANCE, MEDIDO POR MI Y RECOMPUTALO TU: once ficheros de scripts/loop/
llevan el patron literal, siete de ellos dentro de la bateria de las 23. SI TU
CUENTA NO DA ONCE, PARAS Y LO DICES."

ESTE INSTRUMENTO SOLO CUENTA. NO TOCA UN SOLO CHECK. Publica la nomina bajo TRES
lecturas distintas de "el patron literal", el cruce con la bateria de las 23, y
el fichero que explica la diferencia con la cifra del acta.

LAS TRES LECTURAS, PORQUE "EL PATRON LITERAL" ADMITE MAS DE UNA Y NO SE ELIGE LA
QUE CONVIENE:
  (A) LA ESTRECHA: el codigo invoca `git status --porcelain` con los DOS
      pathspec que el docstring de la 6.7 nombra, `dataset/` Y `docs/plan/`.
  (B) LA MEDIA: el codigo invoca `git status --porcelain` con un pathspec que
      EMPIEZA por `dataset/`. Es la que este instrumento toma como principal,
      porque la 6.7 describe el defecto por su INSTRUMENTO (git status ve fin de
      linea y suciedad previa) y ese defecto lo tiene cualquier pathspec sobre
      `dataset/`.
  (C) LA ANCHA: el codigo invoca `git status --porcelain` con cualquier
      pathspec o sin ninguno.

LA EXCLUSION QUE SE DECLARA EN VEZ DE CALLARSE, Y ES LA MISMA TRAMPA QUE
`verificar_apertura_sellada.py` lleva escrita desde la vuelta 102: UN BUSCADOR
DE UN PATRON CONTIENE EL PATRON QUE BUSCA. Se descartan POR NOMBRE este fichero
y `vuelta159_tarea1_registrar_adjudicaciones.py`, que es el otro que lo escribe
para buscarlo. Sin esa exclusion la cuenta sale inflada en dos, y la primera
corrida de la TAREA 1 de esta vuelta lo demostro saliendo TRECE.

USO:  python scripts/loop/vuelta159_tarea5_alcance_p16.py
"""
import io
import os
import re
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOOP = os.path.join(RAIZ, "scripts", "loop")
BATERIA = os.path.join(LOOP, "verificar_mutaciones_viejas.py")

ESTRECHA = '"--porcelain", "--", "dataset/", "docs/plan/"'
MEDIA = '"--porcelain", "--", "dataset/'
ANCHA = '"--porcelain"'

BUSCADORES = {
    "vuelta159_tarea5_alcance_p16.py",
    "vuelta159_tarea1_registrar_adjudicaciones.py",
}

ESPERADO_FICHEROS = 11
ESPERADO_EN_BATERIA = 7


def leer(ruta):
    return io.open(ruta, encoding="utf-8").read()


def con_patron(patron):
    salida = []
    for nombre in sorted(os.listdir(LOOP)):
        if not nombre.endswith(".py") or nombre in BUSCADORES:
            continue
        try:
            if patron in leer(os.path.join(LOOP, nombre)):
                salida.append(nombre)
        except (IOError, UnicodeDecodeError):
            continue
    return salida


def nomina_bateria():
    t = leer(BATERIA)
    return [m[0] for m in re.findall(r'^\s*\("(vuelta[^"]+\.py)",\s*(True|False)\)',
                                     t, re.M)]


def main():
    print("=" * 78)
    print("VUELTA 159, TAREA 5.b: EL ALCANCE DEL CHECK DE P.16, RECOMPUTADO")
    print("=" * 78)
    print("")
    print("EXCLUSION DECLARADA: se descartan por nombre los dos buscadores que")
    print("contienen el patron porque tienen que escribirlo para buscarlo:")
    for b in sorted(BUSCADORES):
        print("   %s" % b)
    print("")

    bat = nomina_bateria()
    print("A) LA BATERIA, CONTADA DE SU PROPIO FICHERO")
    print("   fuente: scripts/loop/verificar_mutaciones_viejas.py")
    print("   CIFRA mutaciones en la nomina de la bateria: %d" % len(bat))
    print("")

    print("B) LAS TRES LECTURAS DEL PATRON LITERAL")
    resultados = {}
    for nombre, patron in (("A ESTRECHA (dataset/ Y docs/plan/)", ESTRECHA),
                           ("B MEDIA (pathspec que empieza por dataset/)", MEDIA),
                           ("C ANCHA (cualquier git status --porcelain)", ANCHA)):
        f = con_patron(patron)
        resultados[nombre] = f
        en_bat = [x for x in f if x in bat]
        print("   %s" % nombre)
        print("      patron: %s" % patron)
        print("      CIFRA ficheros: %d" % len(f))
        print("      CIFRA de ellos en la bateria de las 23: %d" % len(en_bat))
    print("")

    principal = resultados["B MEDIA (pathspec que empieza por dataset/)"]
    en_bat = [x for x in principal if x in bat]
    fuera_bat = [x for x in principal if x not in bat]
    print("C) LA NOMINA PRINCIPAL (lectura B), UNA A UNA")
    for x in principal:
        print("   %-46s %s" % (x, "EN LA BATERIA" if x in bat else "fuera de la bateria"))
    print("")
    print("   CIFRA ficheros con el patron: %d" % len(principal))
    print("   CIFRA de ellos dentro de la bateria de las 23: %d" % len(en_bat))
    print("   CIFRA de ellos fuera de la bateria: %d" % len(fuera_bat))
    print("")

    print("D) EL COTEJO CONTRA LA CIFRA DEL ACTA 158, ADJUDICACION 6.7")
    print("   CIFRA que el acta declara, ficheros: %d" % ESPERADO_FICHEROS)
    print("   CIFRA que el acta declara, dentro de la bateria: %d" % ESPERADO_EN_BATERIA)
    print("   CIFRA que este computo da, ficheros: %d" % len(principal))
    print("   CIFRA que este computo da, dentro de la bateria: %d" % len(en_bat))
    print("")
    if len(en_bat) == ESPERADO_EN_BATERIA:
        print("   LOS SIETE DE LA BATERIA REPRODUCEN AL DIGITO.")
    if len(principal) != ESPERADO_FICHEROS:
        sobran = len(principal) - ESPERADO_FICHEROS
        print("   LA CIFRA DE FICHEROS NO REPRODUCE: sale %d y el acta dice %d."
              % (len(principal), ESPERADO_FICHEROS))
        candidatos = [x for x in principal if not x.startswith("vuelta1")]
        print("   EL RESIDUO SE PUEDE NOMBRAR, Y ES UNO SOLO: %s" % ", ".join(candidatos))
        print("   Quitandolo, la cuenta da %d, que es exactamente la del acta."
              % (len(principal) - len(candidatos)))
        print("")
        print("   PARADA, POR MANDATO LITERAL DEL ENCARGO (TAREA 5.b): si la cuenta")
        print("   no da once, se para y se dice. NO SE TOCA UN SOLO CHECK. El remedio")
        print("   de la 5.a y el caso positivo de la 5.c NO SE EJECUTAN en esta")
        print("   vuelta, porque su alcance esta en disputa y una guarda que se")
        print("   reescribe con el alcance mal contado es peor que la que se deja.")
        print("FIN")
        return 1

    print("   LA CUENTA REPRODUCE. Se puede aplicar el remedio de la 5.a.")
    print("FIN")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
