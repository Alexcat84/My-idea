# -*- coding: utf-8 -*-
"""vuelta148_0d_mutacion_corredor.py . PRUEBA DE MUTACION del CORREDOR DE LA
PARADA que la vuelta 148 le anade a verificar_apertura_sellada.py.

POR QUE EXISTE. EJECUTOR.md 1, "EL CASO ROJO SE PRUEBA POR MUTACION": ninguna
guarda se publica como prueba sin haber corrido antes su prueba de mutacion, y
la mutacion va sobre una variable QUE EL CODIGO COMPUTE, no sobre un literal.
La caida 2 de la vuelta 89 fue exactamente eso: un veredicto que era una
constante literal comparada consigo misma, o sea un caso rojo que no podia
fallar nunca.

QUE MUTA, Y ES COMPUTADO. El corredor NO se teclea: se lee de git con
`corredor_desde_git(acta, nacido_en)` sobre la vuelta 148 real de esta rama.
El veredicto de los dos casos sale de la MISMA funcion pura
`intrusos_del_corredor`, que recibe ese corredor leido. Lo unico que cambia
entre el caso verde y el rojo es UNA RUTA anadida a una copia en memoria del
corredor real. Si alguien afloja el criterio (por ejemplo metiendo dataset/ en
los papeles de parada), el caso B deja de caer y esta prueba se pone en rojo.

CASOS:
  A. VERDE. El corredor REAL de la vuelta 148 (el commit de la decision del
     fundador) no trae intrusos: sus rutas son todas papel de parada.
  B. ROJO POR MUTACION. Al MISMO corredor, en una copia, se le anade la ruta
     de un nodo del dataset. La funcion tiene que nombrarla como intrusa.
  C. ROJO POR MUTACION, LA OTRA MITAD. Una ruta que solo SE PARECE a un papel
     de parada (docs/loop/paradas_falsas/...) tampoco puede colarse: el
     prefijo es `docs/loop/paradas/` con su barra, no `docs/loop/paradas`.
  D. VERDE DE CONTROL SOBRE OTRA VUELTA. La 147 no tuvo parada en medio: su
     corredor leido de git es vacio, y un corredor vacio no trae intrusos.

--- CORRECCION DECLARADA (vuelta 163, TAREA 2; adjudicacion 6.8 del acta 162) ---

ESTE ARNES LLEVABA ROTO DESDE LA VUELTA 154 Y NADIE SE ENTERO, que es
exactamente la enfermedad que la 6.8 viene a curar. La vuelta 154 (TAREA 6, por
la adjudicacion 6.7 del acta 153) le cambio la firma a
`intrusos_del_corredor`: antes devolvia UNA lista y desde entonces devuelve DOS,
`(intrusos, admitidos_por_el_encargo)`. Este fichero seguia recibiendo el
resultado como si fuera UNA, asi que:

  - el CASO A imprimia "2 intruso(s)" SIEMPRE, porque medía `len()` de la TUPLA
    de dos listas y no de la lista de intrusos, y por eso siempre daba dos;
  - el CASO B reventaba con `ValueError: not enough values to unpack (expected
    3, got 1)` al intentar recorrer la tupla como si fuera la lista.

LO QUE SE ARREGLA ES EL SITIO DE LA LLAMADA, NO EL CRITERIO: se desempaquetan
las dos listas y se sigue midiendo sobre `intrusos`, que es lo que este arnes
siempre quiso medir. Ni un caso se afloja, ni un esperado se toca. La lista de
admitidos se IMPRIME ademas, porque una guarda que devuelve dos cosas y solo
mira una es como estaba este fichero.

NO SE BORRA NADA Y NO SE ALEGA VERDE: el rojo de hoy esta sellado en
`docs/loop/SALIDA_V163_T2_CENSO_POST147.txt` con su traza entera, y el arnes
entra en la bateria por la 6.8 DESPUES de arreglarse, no antes.

USO:
  python scripts/loop/vuelta148_0d_mutacion_corredor.py
"""
import os
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import verificar_apertura_sellada as G

RUTA_INTRUSA = "dataset/nodos/un_nodo_cualquiera.json"
RUTA_QUE_SE_PARECE = "docs/loop/paradas_falsas/2026-09-02-colada.md"


def corredor_real(vuelta):
    """El corredor de la vuelta pedida, LEIDO DE GIT y no tecleado: acta de la
    vuelta anterior y commit en que nacio SALIDA_V<vuelta>_HEAD_APERTURA.txt."""
    fallos = []
    rama = G.rama_actual(fallos)
    acta = G.commit_acta(vuelta, rama, fallos)
    nacido_en = G.commit_de_nacimiento("SALIDA_V%d_HEAD_APERTURA.txt" % vuelta, rama, fallos)
    if fallos:
        raise SystemExit("no se pudo leer el corredor real de la vuelta %d: %s" % (vuelta, fallos))
    corredor = G.corredor_desde_git(acta, nacido_en, fallos)
    if corredor is None or fallos:
        raise SystemExit("corredor no medible en la vuelta %d: %s" % (vuelta, fallos))
    return acta, nacido_en, corredor


def con_ruta_extra(corredor, ruta):
    """Copia del corredor con UNA ruta mas en su primer commit. La copia es
    profunda en la lista de rutas: mutar la del original invalidaria el caso A."""
    if not corredor:
        raise SystemExit("el corredor esta vacio: no hay commit al que anadirle la ruta")
    h, asunto, rutas = corredor[0]
    return [(h, asunto, list(rutas) + [ruta])] + list(corredor[1:])


def main():
    acta, nacido_en, real = corredor_real(148)
    print("CORREDOR REAL DE LA VUELTA 148, LEIDO DE GIT (no tecleado)")
    print("  acta de la 147: %s" % acta[:8])
    print("  apertura de la 148 nacio en: %s" % nacido_en[:8])
    for h, asunto, rutas in real:
        print("  %s '%s'" % (h[:8], asunto[:70]))
        for r in rutas:
            print("      %s   (papel de parada: %s)" % (r, G.es_papel_de_la_parada(r)))

    fallos = []

    # --- CASO A: VERDE sobre el corredor real ---
    intrusos_a, admitidos_a = G.intrusos_del_corredor(real)
    print("\nCASO A (verde, corredor real): %d intruso(s)" % len(intrusos_a))
    if intrusos_a:
        fallos.append("CASO A: el corredor real deberia estar limpio y trae %d intruso(s): %s"
                      % (len(intrusos_a), intrusos_a))

    # --- CASO B: ROJO por mutacion, ruta de dataset ---
    mutado_b = con_ruta_extra(real, RUTA_INTRUSA)
    intrusos_b, _admitidos_b = G.intrusos_del_corredor(mutado_b)
    print("CASO B (rojo por mutacion, +%s): %d intruso(s)" % (RUTA_INTRUSA, len(intrusos_b)))
    for h, asunto, ajenas in intrusos_b:
        print("      %s nombra %s" % (h[:8], ajenas))
    if len(intrusos_b) != 1 or intrusos_b[0][2] != [RUTA_INTRUSA]:
        fallos.append("CASO B: la mutacion NO cayo como debia; intrusos=%s" % (intrusos_b,))

    # --- CASO C: ROJO por mutacion, ruta que solo se parece ---
    mutado_c = con_ruta_extra(real, RUTA_QUE_SE_PARECE)
    intrusos_c, _admitidos_c = G.intrusos_del_corredor(mutado_c)
    print("CASO C (rojo por mutacion, +%s): %d intruso(s)" % (RUTA_QUE_SE_PARECE, len(intrusos_c)))
    for h, asunto, ajenas in intrusos_c:
        print("      %s nombra %s" % (h[:8], ajenas))
    if len(intrusos_c) != 1 or intrusos_c[0][2] != [RUTA_QUE_SE_PARECE]:
        fallos.append("CASO C: la ruta que se parece se colo; intrusos=%s" % (intrusos_c,))

    # --- CASO D: VERDE de control sobre la vuelta 147, sin parada en medio ---
    _, _, real_147 = corredor_real(147)
    intrusos_d, _admitidos_d = G.intrusos_del_corredor(real_147)
    print("CASO D (verde de control, vuelta 147): corredor de %d commit(s), %d intruso(s)"
          % (len(real_147), len(intrusos_d)))
    if len(real_147) != 0:
        fallos.append("CASO D: la vuelta 147 no tuvo parada en medio y su corredor deberia "
                      "estar vacio; trae %d commit(s)" % len(real_147))
    if intrusos_d:
        fallos.append("CASO D: corredor vacio con intrusos: %s" % (intrusos_d,))

    # --- EL CASO A NO SE CONTAMINO CON LA MUTACION ---
    intrusos_a2, _admitidos_a2 = G.intrusos_del_corredor(real)
    if intrusos_a2:
        fallos.append("La mutacion contamino el corredor real: A ya no esta limpio (%s)" % (intrusos_a2,))

    print("")
    if fallos:
        print("ROJO, la prueba de mutacion del corredor NO se sostiene (%d):" % len(fallos))
        for f in fallos:
            print("   %s" % f)
        return 1
    print("VERDE: los cuatro casos se comportan. El corredor real pasa, las dos mutaciones "
          "CAEN nombrando la ruta intrusa, y el corredor vacio de la 147 sigue pasando.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
