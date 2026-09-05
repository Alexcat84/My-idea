# -*- coding: utf-8 -*-
"""vuelta148_2d_mutacion_exencion.py . PRUEBA DE MUTACION de la EXENCION
DECLARADA de la guarda de ausencias (TAREA 2.4 de la vuelta 148, sobre la caida
4.2 del acta 147 y su punto 3.15).

LO QUE HAY QUE PROBAR ES QUE NO ES UN INTERRUPTOR. Una exencion que escribe el
auditado no vale nada si el auditado decide solo cuando aplica (leccion de la
vuelta 135). Aqui la guarda la verifica ella misma, y estos casos ensenan que
la verificacion muerde.

  A. LA FRASE QUE DISPARA, SIN EXENCION: ROJO. Si no cayera, el resto de la
     prueba no mediria nada.
  B. LA MISMA FRASE, ENVUELTA EN UNA EXENCION LEGITIMA (no nombra el repo):
     pasa, Y LA EXENCION SE IMPRIME con su motivo.
  C. LA MUTACION QUE IMPORTA, SOBRE VARIABLE COMPUTADA: a la MISMA frase eximida
     se le anade UNA ruta del repositorio. La exencion tiene que ser RECHAZADA
     nombrando lo que aparecio. Lo unico que cambia entre B y C es ese texto.
  D. EXENCION SIN MOTIVO: rechazada, porque una exencion sin motivo es un
     interruptor.
  E. MARCA SUELTA: un cierre sin apertura es ROJO, como manda la regla de las
     tres marcas de la casa.
  F. LA EXENCION NO TAPA AL VECINO: una frase que dispara FUERA del bloque
     sigue cayendo aunque haya una exencion legitima en la misma pagina.

El sujeto no se teclea: la frase que dispara se construye con una formula
LEIDA del vocabulario vivo de la guarda.

USO:
  python scripts/loop/vuelta148_2d_mutacion_exencion.py
SUJETO CONGELADO (declarado en la vuelta 180, TAREA 2.a): este arnes NOMBRA `REPORTE.md` en su texto pero NO LO ABRE (1 apariciones en el texto, 0 llamadas que lo lean y 0 lecturas del fichero vivo, medidas fila a fila en docs/plan/SUJETO_CONGELADO_VEREDICTOS.jsonl), asi que su resultado no depende de lo que ese fichero diga hoy.
"""
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(RAIZ, "scripts", "loop"))

import verificar_ausencias_del_reporte as G


def main():
    fallos = []

    # LA FORMULA SE LEE DEL VOCABULARIO VIVO, no se teclea.
    formula = sorted(G.VOCABULARIO_ACTIVO)[0]
    print("VOCABULARIO VIVO: %d formulas. Elegida por orden: %r"
          % (len(G.VOCABULARIO_ACTIVO), formula))
    frase = "En toda la campana %s parecido, y lo digo de memoria." % formula

    # --------- CASO A: sin exencion, cae ---------
    fa, va, ra, ea = G.verificar(frase)
    print("")
    print("CASO A (frase suelta, sin exencion): fallos=%d vistas=%d exenciones=%d"
          % (len(fa), len(va), len(ea)))
    if not fa:
        fallos.append("CASO A: la frase no disparo; la prueba no mide nada")

    # --------- CASO B: exencion legitima ---------
    motivo = "prosa de la campana, no afirma nada sobre el repositorio"
    envuelta = ("<!-- EXENCION DECLARADA: %s -->\n%s\n<!-- FIN EXENCION DECLARADA -->\n"
                % (motivo, frase))
    fb, vb, rb, eb = G.verificar(envuelta)
    print("CASO B (misma frase, exencion legitima): fallos=%d vistas=%d exenciones=%d"
          % (len(fb), len(vb), len(eb)))
    for m, cuerpo in eb:
        print("   | motivo: %s" % m)
    if fb:
        fallos.append("CASO B: la exencion legitima no paso: %s" % fb)
    if len(eb) != 1:
        fallos.append("CASO B: la exencion no quedo registrada para imprimirse")

    # --------- CASO C: LA MUTACION. la misma frase, apuntando al repo ---------
    frase_con_repo = frase + " Ver docs/loop/REPORTE.md."
    envuelta_c = ("<!-- EXENCION DECLARADA: %s -->\n%s\n<!-- FIN EXENCION DECLARADA -->\n"
                  % (motivo, frase_con_repo))
    fc, vc, rc, ec = G.verificar(envuelta_c)
    print("CASO C (MUTACION: la misma frase mas UNA ruta del repo): fallos=%d exenciones=%d"
          % (len(fc), len(ec)))
    for f in fc:
        print("   | %s" % f[:170])
    if not fc:
        fallos.append("CASO C: la exencion se trago una frase que SI apunta al repositorio: "
                      "es un interruptor")
    if ec:
        fallos.append("CASO C: la exencion rechazada se conto como aceptada")
    if not any("RECHAZADA" in f for f in fc):
        fallos.append("CASO C: el fallo no dice que la exencion queda RECHAZADA")

    # --------- CASO D: sin motivo ---------
    sin_motivo = ("<!-- EXENCION DECLARADA:  -->\n%s\n<!-- FIN EXENCION DECLARADA -->\n"
                  % frase)
    fd, vd, rd, ed = G.verificar(sin_motivo)
    print("CASO D (exencion sin motivo): fallos=%d" % len(fd))
    if not fd:
        fallos.append("CASO D: una exencion sin motivo paso; eso es un interruptor")

    # --------- CASO E: marca suelta ---------
    suelta = "%s\n<!-- FIN EXENCION DECLARADA -->\n" % frase
    fe, ve, re_, ee = G.verificar(suelta)
    print("CASO E (cierre sin apertura): fallos=%d" % len(fe))
    if not any("sin su apertura" in f for f in fe):
        fallos.append("CASO E: un cierre suelto no se canto")

    # --------- CASO F: la exencion no tapa al vecino ---------
    vecina = ("<!-- EXENCION DECLARADA: %s -->\n%s\n<!-- FIN EXENCION DECLARADA -->\n\n"
              "Y ademas, %s en el arbol de hoy.\n" % (motivo, frase, formula))
    ff, vf, rf, ef = G.verificar(vecina)
    print("CASO F (una exenta y una suelta en la misma pagina): fallos=%d exenciones=%d"
          % (len(ff), len(ef)))
    if not ff:
        fallos.append("CASO F: la frase de FUERA del bloque no cayo: la exencion tapo a su "
                      "vecina")
    if len(ef) != 1:
        fallos.append("CASO F: la exencion legitima dejo de contarse")

    print("")
    if fallos:
        print("ROJO, la exencion declarada NO se sostiene (%d):" % len(fallos))
        for f in fallos:
            print("   %s" % f)
        return 1
    print("VERDE: los seis casos se comportan. La exencion NO es un interruptor: solo se")
    print("acepta si lo eximido de verdad no apunta al repositorio, se rechaza nombrando la")
    print("ruta en cuanto aparece una, exige motivo escrito, canta la marca suelta, y no")
    print("tapa a la frase vecina.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
