# -*- coding: utf-8 -*-
r"""vuelta176_tarea1c_mutacion_tramos.py . EL CASO POSITIVO POR MUTACION DEL
REPARTO DE LA BATERIA EN TRAMOS (vuelta 176, TAREA 1.c).

QUE SUJETO PRUEBA: `reparto_en_tramos()` de
`scripts/loop/verificar_mutaciones_viejas.py`, que nace en esta vuelta para que
la bateria se pueda correr a bocados sin dejar de correrse entera.

LO QUE HAY QUE PROTEGER, DICHO ANTES DE PROBARLO. Partir la bateria SOLO es
legitimo si la union de los tramos es la nomina ENTERA, en su mismo orden, SIN
PERDER NI REPETIR NI UNA ENTRADA. Si el reparto se comiera una entrada, la
composicion de los tramos daria un verde que no cubre lo que dice, y esa es
exactamente la especie de caida que esta campana lleva cazando desde la vuelta
74: una frase que promete mas de lo que su instrumento mide.

POR QUE ESTE ARNES ENTRA EN LA NOMINA EN SU MISMA VUELTA Y NO EN LA SIGUIENTE:
por la letra que el propio `verificar_mutaciones_viejas.py` lleva escrita desde
la vuelta 148 (TAREA 2.5, adjudicacion 3.5 del acta 147): "LO QUE ESTA REGLA
EXIGE ES SUJETO CONGELADO. EL PLAZO DE UNA VUELTA ERA EL MEDIO, NO EL FIN". Este
arnes no tiene ancla sobre ningun fichero vivo: llama a una funcion PURA con
nominas FABRICADAS aqui dentro, asi que su sujeto no se le puede mover debajo, y
esperar una vuelta no lo haria mas seguro, solo mas tarde. Y si NO entrara hoy,
`arneses_que_faltan()` lo veria como un arnes posterior a la nomina y pondria la
bateria en ROJO, con razon.

NINGUN VEREDICTO ES UNA CONSTANTE LITERAL (`EJECUTOR.md` 1, 29 ago 2026). La
comprobacion de verdad es el INVARIANTE `lo_que_rompe()`, y para demostrar que
ese invariante no es vacio se le pasan TRES REPARTOS ROTOS A PROPOSITO, escritos
aqui al lado: uno que PIERDE entradas, uno que las REPITE y uno que las
DESORDENA. Si el invariante no cazara los tres, este arnes cae. Un invariante
que aprueba todo lo que le echan no prueba nada.

P.16, QUIEN FABRICA LIMPIA: no escribe nada, ni en disco ni en `docs/loop/`. Sus
sujetos son listas en memoria.

USO:
  python scripts/loop/vuelta176_tarea1c_mutacion_tramos.py
"""
import os
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)
import verificar_mutaciones_viejas as B   # noqa: E402


def nomina_fabricada(n):
    """UNA NOMINA DE MENTIRA con la forma de la de verdad: (nombre, admite).
    Los nombres llevan su indice dentro, para que perder o repetir uno se vea."""
    return [("vuelta%03d_arnes_mutacion_de_mentira.py" % i, i % 3 == 0)
            for i in range(n)]


def lo_que_rompe(nomina, tramos):
    """EL INVARIANTE. Devuelve la lista de motivos por los que un reparto NO
    sirve; vacia si el reparto es legitimo. PURA.

    LAS CUATRO COSAS, y las cuatro tienen que darse a la vez:
      (a) la union de los tramos, CONCATENADA EN ORDEN, es la nomina entera;
      (b) no falta ninguna entrada;
      (c) no se repite ninguna entrada;
      (d) ningun tramo esta vacio."""
    motivos = []
    plano = [x for t in tramos for x in t]
    if plano != list(nomina):
        motivos.append("(a) la concatenacion de los tramos NO es la nomina en su "
                       "orden: %d entradas concatenadas contra %d de la nomina"
                       % (len(plano), len(nomina)))
    nombres_plano = [s for s, _a in plano]
    nombres_nomina = [s for s, _a in nomina]
    faltan = [n for n in nombres_nomina if n not in set(nombres_plano)]
    if faltan:
        motivos.append("(b) el reparto PIERDE %d entrada(s): %s"
                       % (len(faltan), ", ".join(faltan[:4])))
    repes = sorted({n for n in nombres_plano if nombres_plano.count(n) > 1})
    if repes:
        motivos.append("(c) el reparto REPITE %d entrada(s): %s"
                       % (len(repes), ", ".join(repes[:4])))
    vacios = [i for i, t in enumerate(tramos) if not t]
    if vacios:
        motivos.append("(d) hay %d tramo(s) VACIOS, en las posiciones %s"
                       % (len(vacios), vacios))
    return motivos


# ---------------------------------------------------------------- LOS ROTOS
# TRES REPARTOS ROTOS A PROPOSITO. Existen para demostrar que `lo_que_rompe()`
# NO es un invariante vacio: si aprobara cualquiera de estos tres, este arnes
# cae en rojo y con razon.

def reparto_que_pierde(nomina, tamano):
    """Avanza de tamano+1 en tamano+1 pero corta de tamano en tamano: se come
    una entrada por tramo. Es el fallo mas facil de escribir sin darse cuenta."""
    return [list(nomina[i:i + tamano])
            for i in range(0, len(nomina), tamano + 1)]


def reparto_que_repite(nomina, tamano):
    """Solapa los tramos en una entrada: la ultima de cada tramo vuelve a ser la
    primera del siguiente. Correria de mas y el verde diria de mas."""
    out = []
    i = 0
    while i < len(nomina):
        out.append(list(nomina[i:i + tamano]))
        i += max(tamano - 1, 1)
    return out


def reparto_que_desordena(nomina, tamano):
    """Reparte bien pero devuelve los tramos del reves. No pierde ni repite
    nada, y por eso es el que distingue un invariante que mira el ORDEN de uno
    que solo cuenta cabezas."""
    return list(reversed(B.reparto_en_tramos(nomina, tamano)))


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    print("=" * 78)
    print("PRUEBA DE MUTACION DEL REPARTO EN TRAMOS (vuelta 176, TAREA 1.c)")
    print("=" * 78)
    print("Sujeto: reparto_en_tramos() de verificar_mutaciones_viejas.py")
    print("Todo sobre nominas FABRICADAS en memoria. No se escribe nada.")
    print("")

    fallos = []

    # ------------------------------------------------- (a) LOS CASOS BUENOS
    print("(a) EL REPARTO DE VERDAD, SOBRE NOMINAS FABRICADAS DE VARIOS TAMANOS")
    print("    Ninguna cifra esperada se teclea: todas se computan de la nomina.")
    casos = []
    for n in (1, 2, 7, 10, 87, 88, 100):
        for tamano in (1, 3, 10, 25, 200):
            casos.append((n, tamano))
    for n, tamano in casos:
        nomina = nomina_fabricada(n)
        tramos = B.reparto_en_tramos(nomina, tamano)
        motivos = lo_que_rompe(nomina, tramos)
        # LA CIFRA ESPERADA DE TRAMOS SE COMPUTA, NO SE TECLEA.
        esperados = (n + tamano - 1) // tamano
        if len(tramos) != esperados:
            motivos.append("el reparto da %d tramos y la cuenta de techo dice %d"
                           % (len(tramos), esperados))
        if max((len(t) for t in tramos), default=0) > tamano:
            motivos.append("hay un tramo mas grande que el tamano pedido")
        if motivos:
            fallos.append("CASO BUENO n=%d tamano=%d: %s" % (n, tamano, "; ".join(motivos)))
    print("    CIFRA casos buenos corridos: %d" % len(casos))
    print("    CIFRA casos buenos que fallan: %d"
          % len([f for f in fallos if f.startswith("CASO BUENO")]))
    print("")

    # LA NOMINA DE VERDAD, la que la bateria va a repartir hoy. NO se teclea su
    # tamano: se lee del modulo.
    print("(b) LA NOMINA DE VERDAD, LEIDA DEL MODULO Y NO TECLEADA")
    real = list(B.VIEJAS)
    print("    CIFRA entradas de la nomina real: %d" % len(real))
    for tamano in (5, 10, 15, 20):
        tramos = B.reparto_en_tramos(real, tamano)
        motivos = lo_que_rompe(real, tramos)
        print("    tamano %3d -> %2d tramos, el ultimo con %2d entradas, invariante: %s"
              % (tamano, len(tramos), len(tramos[-1]),
                 "INTACTO" if not motivos else "ROTO"))
        if motivos:
            fallos.append("NOMINA REAL tamano=%d: %s" % (tamano, "; ".join(motivos)))
    print("")

    # ------------------------------------------- (c) LA MUTACION DE VERDAD
    print("(c) LOS TRES REPARTOS ROTOS. EL INVARIANTE TIENE QUE CAZAR LOS TRES.")
    print("    Si aprobara uno solo, `lo_que_rompe()` seria un invariante vacio")
    print("    y los casos de arriba no probarian nada.")
    rotos = (("PIERDE entradas", reparto_que_pierde),
             ("REPITE entradas", reparto_que_repite),
             ("DESORDENA los tramos", reparto_que_desordena))
    for etiqueta, funcion in rotos:
        cazado_en = []
        for n, tamano in ((87, 10), (88, 10), (100, 25), (10, 3)):
            nomina = nomina_fabricada(n)
            motivos = lo_que_rompe(nomina, funcion(nomina, tamano))
            if motivos:
                cazado_en.append((n, tamano, motivos[0]))
        print("    reparto que %-22s cazado en %d de 4 escenarios"
              % (etiqueta, len(cazado_en)))
        if cazado_en:
            print("        primer motivo: %s" % cazado_en[0][2][:96])
        if len(cazado_en) != 4:
            fallos.append("EL INVARIANTE NO CAZA el reparto que %s: solo lo pillo en "
                          "%d de 4 escenarios" % (etiqueta, len(cazado_en)))
    print("")

    # ------------------------------------------------- (d) EL TAMANO ILEGAL
    print("(d) UN TAMANO DE TRAMO ILEGAL SE NIEGA, NO SE APANA")
    for tamano in (0, -1):
        try:
            B.reparto_en_tramos(nomina_fabricada(10), tamano)
        except ValueError as e:
            print("    tamano %2d -> ValueError, como tiene que ser: %s" % (tamano, e))
        else:
            fallos.append("EL TAMANO %d NO se nego: el reparto lo acepto y devolvio "
                          "algo" % tamano)
    print("")

    print("=" * 78)
    if fallos:
        print("ROJO, %d fallo(s):" % len(fallos))
        for f in fallos:
            print("   " + f)
        return 1
    print("VERDE: el reparto conserva la nomina entera, en su orden, sin perder ni")
    print("repetir ni una entrada, en los %d casos fabricados y en la nomina real;"
          % len(casos))
    print("se niega a repartir con un tamano ilegal; y el invariante que lo dice")
    print("CAZA los tres repartos rotos, o sea que no es un invariante vacio.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
