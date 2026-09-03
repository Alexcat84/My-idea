# -*- coding: utf-8 -*-
r"""vuelta164_tarea5_medir_pre148.py . TAREA 5 de la vuelta 164.

LOS ARNESES DE MUTACION ANTERIORES A LA VUELTA 148 QUE ESTAN FUERA DE LA NOMINA:
SE MIDEN Y SE PARA AHI. Adjudicacion 6.9 del acta 163, arrastrada de la 5.b de
la 163 y de la 6.9 del acta 162.

ES UNA MEDICION, NO UNA OPERACION, Y ESO MANDA SOBRE TODO LO DEMAS:
  - NINGUNO ENTRA EN `VIEJAS`. Este instrumento NO toca
    `scripts/loop/verificar_mutaciones_viejas.py` y no propone entradas.
  - NO SE AFIRMA QUE LA REGLA LES ALCANCE. La regla "una mutacion entra en la
    bateria en la vuelta siguiente a la que nace" nace en la vuelta 144 y NO
    dice si es retroactiva. Con la cifra delante se decide, que es lo que la 6.7
    del acta 156 hizo con las nueve salidas de la P3b.
  - NINGUNO SE ARREGLA. Un rojo aqui se publica con su primera linea util y su
    nombre, y se queda ahi.

QUE HACE, EXACTAMENTE:
  (a) computa la nomina a medir SIN TECLEAR NI UN NOMBRE, importando el censo de
      la propia bateria (`arneses_del_directorio`, `vuelta_de` y `VIEJAS`): son
      los que casan el patron de arnes, NO estan en la nomina y nacieron ANTES
      de la vuelta 148;
  (b) los corre UNA VEZ cada uno (la bateria los correria DOS por el cotejo de
      reproducibilidad; aqui no se cotejan salidas selladas porque no se esta
      juzgando si valen, se esta contando cuantos siquiera corren);
  (c) cronometra cada uno y el total, como la bateria desde la 6.8;
  (d) clasifica igual que la bateria (`clasificar`), para que la cifra sea
      comparable con la suya y no una escala nueva;
  (e) mide el arbol ANTES y DESPUES y publica CON SU NOMBRE todo fichero de
      `docs/loop/` que aparezca o cambie durante la corrida. Correr 41 scripts
      viejos puede ensuciar el arbol, y callarlo seria lo contrario del banco 9.

USO:  python scripts/loop/vuelta164_tarea5_medir_pre148.py
"""
import os
import subprocess
import sys
import time

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)
RAIZ = os.path.dirname(os.path.dirname(AQUI))

import verificar_mutaciones_viejas as V   # noqa: E402

CORTE = 148


def nomina():
    """LOS QUE SE MIDEN, COMPUTADOS Y NO TECLEADOS."""
    dentro = {s for s, _admite in V.VIEJAS}
    return sorted(n for n in V.arneses_del_directorio()
                  if n not in dentro and (V.vuelta_de(n) or 0) < CORTE)


def estado_git():
    r = subprocess.run(["git", "status", "--porcelain", "--", "docs/", "scripts/",
                        "dataset/", "web/", "engine/"],
                       cwd=RAIZ, capture_output=True, text=True,
                       encoding="utf-8", errors="replace")
    return sorted(l.strip() for l in (r.stdout or "").splitlines() if l.strip())


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    print("=" * 78)
    print("VUELTA 164, TAREA 5: LOS ARNESES PRE %d QUE ESTAN FUERA DE LA NOMINA" % CORTE)
    print("=" * 78)
    print("")
    print("ES UNA MEDICION, NO UNA OPERACION. NINGUNO ENTRA EN LA BATERIA, NINGUNO")
    print("SE ARREGLA, Y NO SE AFIRMA QUE LA REGLA DE LA VUELTA 144 LES ALCANCE:")
    print("esa regla no dice si es retroactiva. Con la cifra delante se decide.")
    print("")

    lista = nomina()
    print("A) LA NOMINA A MEDIR, COMPUTADA Y NO TECLEADA")
    print("   CIFRA arneses de mutacion en scripts/loop/: %d"
          % len(V.arneses_del_directorio()))
    print("   CIFRA entradas en la nomina de la bateria: %d" % len(V.VIEJAS))
    print("   CIFRA fuera de la nomina y ANTERIORES a la vuelta %d: %d"
          % (CORTE, len(lista)))
    for n in lista:
        print("      %-52s vuelta %s" % (n, V.vuelta_de(n)))
    print("")

    antes = estado_git()
    print("B) EL ARBOL ANTES DE CORRER NADA")
    print("   CIFRA lineas de git status --porcelain: %d" % len(antes))
    for l in antes:
        print("      %s" % l)
    print("")

    print("C) LA CORRIDA, UNO A UNO Y CON SU CRONOMETRO")
    filas = []
    reloj = {}
    t0 = time.perf_counter()
    for nombre in lista:
        t = time.perf_counter()
        codigo, salida = V.correr(nombre)
        reloj[nombre] = time.perf_counter() - t
        estado = V.clasificar(codigo, salida)
        filas.append((nombre, codigo, estado, V.primera_linea_util(salida)))
        print("   %-52s exit %-4d %-16s %7.1fs"
              % (nombre, codigo, estado, reloj[nombre]))
        if estado != "OK":
            print("        %s" % filas[-1][3])
    total = time.perf_counter() - t0
    print("")

    print("D) EL VEREDICTO CONTADO, Y SOLO CONTADO")
    verdes = [n for n, c, _e, _p in filas if c == 0]
    rojos = [n for n, c, _e, _p in filas if c != 0]
    print("   CIFRA medidos: %d" % len(filas))
    print("   CIFRA que dan exit 0: %d" % len(verdes))
    print("   CIFRA que dan ROJO (exit distinto de 0): %d" % len(rojos))
    reparto = {}
    for _n, _c, e, _p in filas:
        reparto[e] = reparto.get(e, 0) + 1
    for e in sorted(reparto):
        print("   CIFRA con estado %-16s %d" % (e + ":", reparto[e]))
    print("")
    print("   LOS QUE DAN exit 0, CON SU NOMBRE:")
    for n in verdes:
        print("      %s" % n)
    print("   LOS QUE DAN ROJO, CON SU NOMBRE Y SU PRIMERA LINEA UTIL:")
    if not rojos:
        print("      (ninguno)")
    for n, c, e, p in filas:
        if c != 0:
            print("      %-52s exit %d  %s" % (n, c, e))
            print("           %s" % p)
    print("")

    print("E) EL CRONOMETRO")
    print("   CIFRA TIEMPO TOTAL de la medicion, en segundos: %.1f" % total)
    print("   CIFRA TIEMPO TOTAL de la medicion, en minutos: %.1f" % (total / 60.0))
    orden = sorted(reloj.items(), key=lambda kv: -kv[1])
    if orden:
        print("   CIFRA arnes MAS LENTO: %s con %.1fs" % (orden[0][0], orden[0][1]))
        print("   CIFRA arnes MAS RAPIDO: %s con %.1fs" % (orden[-1][0], orden[-1][1]))
        print("   CIFRA mediana por arnes, en segundos: %.1f"
              % sorted(reloj.values())[len(reloj) // 2])
        print("   LOS DIEZ MAS LENTOS, DE MAS A MENOS:")
        for nombre, seg in orden[:10]:
            print("      %-52s %7.1fs" % (nombre, seg))
    print("   AVISO DE RELOJ: aqui cada arnes se corre UNA VEZ. La bateria los")
    print("   correria DOS, asi que si algun dia se decidiera meterlos, el coste")
    print("   sobre el ciclo de cierre seria del orden del DOBLE de este total.")
    print("")

    despues = estado_git()
    nuevas = [l for l in despues if l not in antes]
    idas = [l for l in antes if l not in despues]
    print("F) EL ARBOL DESPUES, Y LO QUE LA CORRIDA MOVIO, CON SU NOMBRE")
    print("   CIFRA lineas de git status --porcelain: %d" % len(despues))
    print("   CIFRA lineas NUEVAS respecto de antes: %d" % len(nuevas))
    for l in nuevas:
        print("      APARECE O CAMBIA: %s" % l)
    print("   CIFRA lineas que DESAPARECEN respecto de antes: %d" % len(idas))
    for l in idas:
        print("      DESAPARECE: %s" % l)
    if not nuevas and not idas:
        print("      (el arbol queda como estaba)")
    print("")

    print("G) LO QUE ESTA MEDICION NO HACE, DICHO OTRA VEZ AL CIERRE")
    print("   NINGUNO de los %d entra en la nomina de la bateria." % len(lista))
    print("   NINGUNO se arregla en esta vuelta.")
    print("   NO se afirma que la regla de la vuelta 144 les alcance.")
    print("   La decision de que hacer con esta cifra NO es del ejecutor.")
    print("")
    print("FIN")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
