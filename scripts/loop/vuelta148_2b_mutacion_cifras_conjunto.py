# -*- coding: utf-8 -*-
"""vuelta148_2b_mutacion_cifras_conjunto.py . PRUEBA DE MUTACION del CAMINO POR
CONJUNTO de la guarda de cifras (TAREA 2.2 de la vuelta 148, sobre la caida
4.4.b del acta 147).

EL AGUJERO. El camino debil recorria las candidatas y aceptaba LA PRIMERA CUYO
VALOR COINCIDIERA con el numero escrito. Dos etiquetas que comparten casi todas
sus palabras empatan en la puntuacion, la prosa no las distingue, y entonces EL
NUMERO DE UNA VALIDABA LA FRASE DE LA OTRA. El verde salia de que el numero
existiera en algun sitio del fichero, no de que fuera el de la etiqueta de la
que se hablaba.

EL SUJETO NO SE INVENTA: son las DOS PAREJAS REALES de
`docs/loop/SALIDA_V147_3A_TRUNCACION_DOS_UNIDADES.txt`, leidas del fichero
commiteado, que se diferencian solo en las palabras "vivas y canonicas" y que
valen distinto (10 contra 7, y 9 contra 6). Son exactamente las dos que el
reparto de la vuelta 147 marcaba `POR CONJUNTO`.

LOS CASOS:
  A. LA PAREJA REAL, LEIDA DEL FICHERO. Se comprueba que de verdad empatan por
     palabras y que sus valores DIFIEREN, o si no la prueba no mide nada.
  B. EL AGUJERO, CON LA REGLA VIEJA. Se reimplementa AQUI la regla vieja (y solo
     aqui, para poder ensenar lo que hacia) y se ve que ACEPTA el valor de la
     vecina.
  C. LA REGLA DE HOY sobre la MISMA entrada: NO acepta, devuelve AMBIGUO.
  D. LA SALIDA QUE SI EXISTE, que es la que el mensaje de error pide: una frase
     que NOMBRA la etiqueta de la que habla vuelve al camino FUERTE y coteja
     estricto contra ella. Una sola palabra compartida por las dos NO basta, y
     eso tambien queda ensenado en el comentario del caso.
  E. LA MUTACION SOBRE VARIABLE COMPUTADA: a la MISMA pareja se le iguala el
     valor en una copia. Igualados, POR CONJUNTO vuelve a ser inofensivo y
     pasa; distintos, no. Lo unico que cambia es un numero computado del
     fichero real.
  F. NO SE ROMPE LO QUE FUNCIONABA: una unidad con UNA sola linea CIFRA sigue
     cotejando POR ETIQUETA.

USO:
  python scripts/loop/vuelta148_2b_mutacion_cifras_conjunto.py
"""
import io
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(RAIZ, "scripts", "loop"))

import verificar_cifras_del_reporte as G

FICHERO = "SALIDA_V147_3A_TRUNCACION_DOS_UNIDADES.txt"


def regla_vieja(candidatas, frase, numero):
    """LA REGLA DE ANTES, reimplementada SOLO aqui y solo para ensenar lo que
    hacia. Es la unica copia legitima de un criterio: la que existe para
    demostrar que el criterio viejo estaba mal."""
    if not candidatas:
        return None
    if len(candidatas) == 1:
        return candidatas[0][1], candidatas[0][0], "ETIQUETA"
    pal_frase = G._palabras(frase)
    puntuadas = [(len(G._palabras(et) & pal_frase), et, val) for et, val in candidatas]
    mejor = max(p for p, _e, _v in puntuadas)
    empatadas = [(et, val) for p, et, val in puntuadas if p == mejor]
    if mejor > 0 and len(empatadas) == 1:
        return empatadas[0][1], empatadas[0][0], "ETIQUETA"
    for et, val in candidatas:
        if val == numero:
            return val, et, "CONJUNTO"
    return candidatas[0][1], candidatas[0][0], "CONJUNTO"


def main():
    fallos = []
    ruta = os.path.join(RAIZ, "docs", "loop", FICHERO)
    if not os.path.exists(ruta):
        print("ARNES ROTO: no existe %s" % FICHERO)
        return 1
    contenido = io.open(ruta, encoding="utf-8").read()

    candidatas = G.cifras_etiquetadas(contenido, "grafias")
    print("CANDIDATAS DE LA UNIDAD 'grafias' EN %s, LEIDAS DEL FICHERO:" % FICHERO)
    for et, val in candidatas:
        print("   '%s' = %d" % (et, val))
    if len(candidatas) < 2:
        print("ARNES ROTO: hacen falta al menos dos candidatas")
        return 1

    # --------- CASO A: empatan de verdad y valen distinto ---------
    # La frase es la del reporte de la vuelta 147: habla de la truncacion sin
    # decir si cuenta las vivas y canonicas o todas.
    frase = ("la truncacion a 31 caracteres deja 10 grafias en el arbol de trabajo, "
             "medidas por la sola longitud")
    numero = 10
    pal = G._palabras(frase)
    puntuadas = [(len(G._palabras(et) & pal), et, val) for et, val in candidatas]
    mejor = max(p for p, _e, _v in puntuadas)
    empatadas = [(et, val) for p, et, val in puntuadas if p == mejor]
    print("")
    print("CASO A: puntuacion mayor=%d, empatadas=%d, valores=%s"
          % (mejor, len(empatadas), sorted(set(v for _e, v in empatadas))))
    if len(empatadas) < 2:
        fallos.append("CASO A: no hay empate, asi que esta prueba no mide el camino debil")
    if len(set(v for _e, v in empatadas)) < 2:
        fallos.append("CASO A: las empatadas valen lo mismo, asi que no hay vecina contra la "
                      "que cuadrar y la prueba no mide nada")

    # --------- CASO B: la regla vieja acepta la vecina ---------
    vieja = regla_vieja(candidatas, frase, numero)
    print("")
    print("CASO B (regla VIEJA): acepta -> valor=%r etiqueta=%r modo=%r"
          % (vieja[0], vieja[1], vieja[2]))
    if vieja[2] != "CONJUNTO":
        fallos.append("CASO B: la regla vieja no llego al camino debil; el caso no reproduce "
                      "el agujero")
    if vieja[0] != numero:
        fallos.append("CASO B: la regla vieja no acepto el numero escrito; el agujero no "
                      "queda ensenado")

    # --------- CASO C: la regla de hoy NO acepta ---------
    hoy = G.elegir_cifra_etiquetada(candidatas, frase, numero)
    print("CASO C (regla de HOY): modo=%r, empatadas nombradas=%d"
          % (hoy[2], len(hoy[3])))
    if hoy[2] != "AMBIGUO":
        fallos.append("CASO C: la regla de hoy sigue aceptando (modo=%s): el camino por "
                      "conjunto NO esta cerrado" % hoy[2])
    if hoy[0] is not None:
        fallos.append("CASO C: AMBIGUO deberia venir sin valor y trae %r" % (hoy[0],))

    # --------- CASO D: la salida que si existe ---------
    # Una palabra que SOLO aparece en una de las dos etiquetas.
    # LAS DISCRIMINANTES SE CALCULAN SOBRE LAS EMPATADAS, que son las que hay
    # que separar, y no sobre las nueve candidatas del fichero.
    disc = G._discriminantes(empatadas)
    print("")
    print("PALABRAS QUE DISTINGUEN A LAS EMPATADAS ENTRE SI (propias de una y de ninguna otra):")
    for et, ps in sorted(disc.items()):
        print("   '%s' -> %s" % (et, sorted(ps) or "NINGUNA"))
    etiqueta_larga = max(empatadas, key=lambda c: len(G._palabras(c[0])))
    palabras_propias = sorted(disc[etiqueta_larga[0]])
    palabra = palabras_propias[0] if palabras_propias else None
    if palabra is None:
        fallos.append("CASO D: no hay ninguna palabra discriminante; no se puede probar la "
                      "salida")
    else:
        # LA FRASE DE LA SALIDA SE ESCRIBE COMO SE LE PIDE AL REPORTE: nombrando
        # la etiqueta de la que se habla. Se usan TODAS sus palabras propias mas
        # las comunes, que es exactamente lo que hace una prosa que si distingue.
        # PRIMER INTENTO MIO, Y NO LO BORRO PORQUE ENSENA ALGO: puse solo UNA
        # palabra propia ('canonicas') y el caso salio AMBIGUO CON RAZON, porque
        # esa palabra la comparten las DOS etiquetas de "vivas y canonicas" (la
        # de longitud, 7, y la del detector, 6). La guarda tenia razon y el
        # equivocado era mi caso.
        frase_d = "de esas %d %s segun el barrido" % (etiqueta_larga[1], etiqueta_larga[0])
        elegida_d = G.elegir_cifra_etiquetada(candidatas, frase_d, etiqueta_larga[1])
        print("")
        print("CASO D (frase con la palabra discriminante %r): modo=%r etiqueta=%r valor=%r"
              % (palabra, elegida_d[2], elegida_d[1], elegida_d[0]))
        if elegida_d[2] != "ETIQUETA":
            fallos.append("CASO D: con palabra discriminante deberia volver al camino FUERTE "
                          "y dio %s" % elegida_d[2])
        if elegida_d[1] != etiqueta_larga[0]:
            fallos.append("CASO D: eligio la etiqueta equivocada (%r en vez de %r)"
                          % (elegida_d[1], etiqueta_larga[0]))

    # --------- CASO E: la mutacion sobre variable computada ---------
    # MISMAS etiquetas, y lo unico que cambia es un valor computado del fichero.
    valor_comun = candidatas[0][1]
    igualadas = [(et, valor_comun) for et, _v in candidatas]
    elegida_e = G.elegir_cifra_etiquetada(igualadas, frase, valor_comun)
    print("")
    print("CASO E (mismas etiquetas, valores IGUALADOS a %d): modo=%r valor=%r"
          % (valor_comun, elegida_e[2], elegida_e[0]))
    if elegida_e[2] != "CONJUNTO":
        fallos.append("CASO E: con todas las empatadas valiendo lo mismo deberia pasar POR "
                      "CONJUNTO y dio %s" % elegida_e[2])
    if elegida_e[0] != valor_comun:
        fallos.append("CASO E: el valor devuelto no es el comun")

    # --------- CASO F: no se rompe lo que funcionaba ---------
    una_sola = [candidatas[0]]
    elegida_f = G.elegir_cifra_etiquetada(una_sola, "una frase cualquiera", candidatas[0][1])
    print("CASO F (una sola candidata): modo=%r" % elegida_f[2])
    if elegida_f[2] != "ETIQUETA":
        fallos.append("CASO F: con una sola candidata deberia ser ETIQUETA y dio %s"
                      % elegida_f[2])

    print("")
    if fallos:
        print("ROJO, el camino por conjunto NO esta cerrado (%d):" % len(fallos))
        for f in fallos:
            print("   %s" % f)
        return 1
    print("VERDE: los seis casos se comportan. Sobre la pareja REAL que solo se diferencia en")
    print("'vivas y canonicas', la regla VIEJA aceptaba el valor de la vecina y la de HOY")
    print("devuelve AMBIGUO; una palabra que distinga devuelve el cotejo al camino FUERTE;")
    print("igualados los valores vuelve a ser inofensivo; y una sola candidata sigue igual.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
