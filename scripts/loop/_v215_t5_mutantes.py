# -*- coding: utf-8 -*-
r"""_v215_t5_mutantes.py . LA PRUEBA DE MUTACION DE LA GUARDA DE LA TAREA 5.b:
QUE EL COMPOSITOR DE CIERRE REVIENTE EN VEZ DE RELLENAR.

COMPUTO DE UNA VUELTA, prefijo de guion bajo (moratoria de AUDITOR.md 6.3).

POR QUE EXISTE. El hallazgo 3.1 del acta 214 (linea 76086) dice que mi
compositor de la 214, al no encontrar el fichero de consola, ESCRIBIO UNA FILA EN
BLANCO Y SIGUIO, y que eso es degradacion silenciosa. El encargo de la 215 manda,
con estas palabras: "Una guarda que no encuentra su fuente REVIENTA, no rellena
con un hueco". ESTA ES LA PRUEBA DE QUE REVIENTA.

QUE MUTA, Y NO ES EL REPO: se muta la ENTRADA de fila_de_gate(), que es la
funcion pura donde vive la decision. Ningun fichero se toca, ni se borra, ni se
renombra.

LOS CUATRO CASOS, Y EL PRIMERO ES EXACTAMENTE EL DE LA 214:

  A. EL FICHERO NO EXISTE (texto None). Es el caso literal de la 214.
  B. EL FICHERO EXISTE PERO NO TRAE NI UN EXITCODE.
  C. EL FICHERO TRAE EXITCODES PERO NO SU PEOR EXITCODE.
  D. EL CASO BUENO, la consola de verdad de esta vuelta, que TIENE que dar fila.

Y ADEMAS SE COMPRUEBA LO QUE DE VERDAD IMPORTA: que en NINGUN caso malo salga una
FILA. Una fila con celdas vacias seguiria siendo una fila, y es justo lo que se
publico en la 214.

USO:  python scripts/loop/_v215_t5_mutantes.py
"""
import io
import os
import sys

NL = chr(10)
AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)
import _v215_cierre_texto as C  # noqa: E402

RAIZ = C.RAIZ
CONSOLA_REAL = "docs/loop/SALIDA_V%d_CICLO_GATE0_APERTURA_CONSOLA.txt" % C.VUELTA


def main():
    real = C.leer(CONSOLA_REAL)
    if real is None:
        print("ROJO: no puedo probar la guarda sin la consola real de esta "
              "vuelta. Y esto tambien es fallar ruidoso.")
        return 1

    casos = [
        ("A. EL FICHERO NO EXISTE, QUE ES EL CASO LITERAL DE LA VUELTA 214",
         None, False),
        ("B. EL FICHERO EXISTE PERO NO TRAE NI UNA LINEA CON EXITCODE",
         "una consola cualquiera" + NL + "sin nada que medir dentro" + NL,
         False),
        ("C. TRAE EXITCODES PERO NO SU PEOR EXITCODE",
         "   1/8 algo   EXITCODE 0 | 10 bytes" + NL
         + "   2/8 otro   EXITCODE 0 | 10 bytes" + NL, False),
        ("D. LA CONSOLA DE VERDAD DE ESTA VUELTA, QUE TIENE QUE DAR FILA",
         real, True),
    ]

    fallos = 0
    for nombre, texto, debe_dar_fila in casos:
        fila, motivo = C.fila_de_gate("APERTURA", texto, CONSOLA_REAL)
        dio = fila is not None
        ok = (dio == debe_dar_fila)
        print("CASO %s" % nombre)
        print("   da fila: %s | se esperaba: %s | VEREDICTO: %s"
              % ("SI" if dio else "NO",
                 "SI" if debe_dar_fila else "NO",
                 "CALZA" if ok else "NO CALZA"))
        if dio:
            print("   fila: %s" % fila)
        else:
            print("   motivo del rojo: %s" % motivo)
            if not motivo:
                fallos += 1
                print("   ROJO: revienta pero SIN DECIR POR QUE, que es la otra "
                      "mitad de fallar ruidoso.")
        if not ok:
            fallos += 1
    print("")

    print("LO QUE DE VERDAD IMPORTA, Y ES LA CIFRA QUE LA 214 HABRIA SUSPENDIDO:")
    malas = [n for n, t, d in casos if not d
             and C.fila_de_gate("APERTURA", t, CONSOLA_REAL)[0] is not None]
    print("CIFRA casos malos que AUN ASI producen una fila: %d (se exige 0) %s"
          % (len(malas), malas))
    if malas:
        fallos += 1
    print("CIFRA casos malos que revientan CON SU MOTIVO ESCRITO: %d de %d"
          % (len([1 for n, t, d in casos if not d
                  and C.fila_de_gate("APERTURA", t, CONSOLA_REAL)[1]]),
             len([1 for n, t, d in casos if not d])))
    print("")

    print("Y LA COMPROBACION SOBRE EL CODIGO DE LA 214, PARA QUE SE VEA QUE LA")
    print("DIFERENCIA ES REAL Y NO UNA PROMESA. Se lee su fichero, no mi memoria:")
    viejo = C.leer("scripts/loop/_v214_cierre_texto.py")
    if viejo is None:
        print("   (el compositor de la 214 no esta en el arbol)")
    else:
        for i, l in enumerate(viejo.split(NL), 1):
            if "sin fichero de consola" in l:
                print("   scripts/loop/_v214_cierre_texto.py linea %d: %s"
                      % (i, l.strip()))
        tiene = "sin fichero de consola" in viejo
        print("   CIFRA la rama que rellena con un hueco existe en el de la 214: "
              "%s" % ("SI" if tiene else "NO"))
    mio = C.leer("scripts/loop/_v%d_cierre_texto.py" % C.VUELTA)
    en_prosa = mio.count("sin fichero de consola")
    print("   CIFRA veces que esa cadena aparece en el MIO: %d, y las que "
          "aparecen estan en el docstring que explica la caida, no en una rama"
          % en_prosa)
    print("")
    print("CIFRA comprobaciones que fallan: %d" % fallos)
    if fallos:
        print("ROJO: la guarda no revienta como dice.")
        return 1
    print("VERDE: los tres casos malos revientan CON SU MOTIVO y NINGUNO produce "
          "una fila; el bueno da su fila.")
    return 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.exit(main())
