# -*- coding: utf-8 -*-
r"""vuelta165_tarea6_mutacion_op_l_01.py . CASO POSITIVO POR MUTACION DE LA
VERIFICACION DE `OP-L-01` (TAREA 6 de la vuelta 165).

QUE PRUEBA, Y ES LO QUE SOSTIENE EL HALLAZGO DE LA TAREA 6: que la comparacion
LITERAL y la RESUELTA dan cosas distintas, y que la resuelta es la que `P.1`
manda. Sobre un mapa de alias y unos veredictos FABRICADOS, un par que solo
aparece via alias tiene que salir NO en literal y SI en resuelta. Si el
resolutor dejara de resolver, los dos casos CAEN.

Y PRUEBA TAMBIEN LA PARADA: que la clausula del marcador no se puede leer de las
dos maneras a la vez, con las dos cifras computadas.

NINGUN VEREDICTO ES UNA CONSTANTE LITERAL: todos salen de correr `resolver()` y
las funciones reales del instrumento sobre sujetos fabricados, y la segunda
pasada muta cada esperado y exige que el caso CAIGA.

SUJETO: mapas y filas fabricados en memoria, mas la ficha real de `OP-L-01`
leida hoy. CERO escrituras.

USO:  python scripts/loop/vuelta165_tarea6_mutacion_op_l_01.py
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import vuelta165_tarea6_op_l_01 as T   # noqa: E402


def prueba():
    print("=" * 78)
    print("VUELTA 165, TAREA 6: CASO POSITIVO POR MUTACION DE LA VERIFICACION")
    print("=" * 78)
    print("")
    casos = []

    print("A) EL RESOLUTOR, SOBRE UN MAPA FABRICADO")
    mapa = {"alias_de_a": "nodo_a", "alias_de_alias": "alias_de_a",
            "alias_de_b": "nodo_b"}
    for x, esperado in (("alias_de_a", "nodo_a"),
                        ("alias_de_alias", "nodo_a"),
                        ("nodo_a", "nodo_a"),
                        ("desconocido", "desconocido")):
        real = T.resolver(mapa, x)
        print("   resolver(%-16s) = %s" % (x, real))
        casos.append(("A_resolver_%s" % x, real, esperado))
    ciclo = {"x": "y", "y": "x"}
    print("   y un ciclo no cuelga: resolver(x) = %s" % T.resolver(ciclo, "x"))
    casos.append(("A_un_ciclo_no_cuelga", T.resolver(ciclo, "x") in ("x", "y"), True))
    print("")

    print("B) LO QUE LA COMPARACION LITERAL NO VE Y LA RESUELTA SI")
    filas = [("alias_de_a", "alias_de_b"), ("otro_1", "otro_2")]
    literal = set(frozenset(p) for p in filas)
    resuelto = set(frozenset((T.resolver(mapa, a), T.resolver(mapa, b)))
                   for a, b in filas)
    par = frozenset(("nodo_a", "nodo_b"))
    print("   veredictos fabricados: %s" % filas)
    print("   el par buscado: nodo_a contra nodo_b")
    print("   aparece en la comparacion LITERAL:  %s" % (par in literal))
    print("   aparece en la comparacion RESUELTA: %s" % (par in resuelto))
    casos.append(("B_la_literal_NO_lo_ve", par in literal, False))
    casos.append(("B_la_resuelta_SI_lo_ve", par in resuelto, True))
    print("   ESTA ES LA ESPECIE QUE P.1 TIENE ESCRITA: una comparacion literal")
    print("   INVENTA SALUD, hace desaparecer un problema real.")
    print("")

    print("C) LA FICHA REAL DE OP-L-01, LEIDA HOY")
    linea, d = T.ficha("OP-L-01")
    print("   docs/plan/OPERACIONES.jsonl:%d" % linea)
    escribiria = sum(len(d.get(k) or []) for k in
                     ("nodos", "preservar", "eliminar", "aristas_nuevas"))
    print("   CIFRA elementos declarados para escribir: %d" % escribiria)
    print("   CIFRA clausulas de verificacion: %d" % len(d.get("verificacion") or []))
    print("   estado: %s | fecha_corte: %s" % (d.get("estado"), d.get("fecha_corte")))
    casos.append(("C_la_ficha_no_escribe_nada", escribiria, 0))
    # RE ANCLADO EN LA VUELTA 168 (TAREA 3.b; hallazgo 4.5 del acta 167).
    # CORRECCION DECLARADA, Y EL MOTIVO NO SE BORRA: este caso esperaba TRES
    # clausulas y hoy la ficha trae CINCO. NO es que la guarda se haya roto ni
    # que se le afloje la vara para llegar al verde: LA CAMPANA MOVIO EL SUJETO
    # A PROPOSITO. La vuelta 166, en su TAREA 2, anadio a `OP-L-01` las
    # clausulas `V4` y `V5` POR ADICION, por el carril del banco 9.10 y con el
    # texto viejo entero encima; el acta 166 lo verifico y lo adjudico bien en
    # su 6.8. Este arnes se quedo anclado al numero de antes porque la bateria
    # no se corrio ni en la 166 ni en la 167, asi que nadie lo vio hasta que el
    # acta 167 lo midio (real 5, esperado 3).
    # EL CASO NO SE AFLOJA AL RE ANCLARLO, Y ESO ES LO QUE IMPORTA: sigue siendo
    # una IGUALDAD EXACTA contra el conteo real de la ficha de hoy, asi que
    # vuelve a caer en rojo en cuanto alguien anada o quite una clausula sin
    # declararlo. Lo que cambia es el numero, no el filo.
    # Y SE ANADE EL INVARIANTE QUE EL NUMERO SOLO NO DA: las dos clausulas
    # nuevas son CORRECCIONES DECLARADAS, y eso se comprueba, no se supone. Si
    # alguien reescribiera la ficha borrando el texto viejo en vez de anadir,
    # este caso caeria aunque el conteo siguiera dando cinco.
    casos.append(("C_tiene_cinco_clausulas", len(d.get("verificacion") or []), 5))
    declaradas = [c for c in (d.get("verificacion") or [])
                  if c.startswith("CORRECCION DECLARADA")]
    print("   CIFRA clausulas que son CORRECCION DECLARADA: %d" % len(declaradas))
    casos.append(("C_dos_de_las_cinco_son_correccion_declarada", len(declaradas), 2))
    casos.append(("C_las_tres_viejas_siguen_enteras",
                  len([c for c in (d.get("verificacion") or [])
                       if not c.startswith("CORRECCION DECLARADA")]), 3))
    casos.append(("C_sigue_en_LISTA", d.get("estado"), "LISTA"))
    casos.append(("C_su_corte_es_del_11_ago", d.get("fecha_corte"), "2026-08-11"))
    print("")

    print("D) LA PARADA, CON SUS DOS CIFRAS COMPUTADAS")
    clausula = (d.get("verificacion") or ["", "", ""])[1]
    print("   la clausula: %r" % clausula)
    hoy = len(T.veredictos())
    print("   CIFRA marcador HOY, contada del fichero: %d" % hoy)
    print("   CIFRA que la clausula escribe: 2117")
    casos.append(("D_la_clausula_trae_el_numeral", "2.117" in clausula, True))
    casos.append(("D_el_marcador_de_hoy_no_es_ese", hoy == 2117, False))
    casos.append(("D_y_la_diferencia_no_es_cero", hoy - 2117 != 0, True))
    print("   LAS DOS LECTURAS NO PUEDEN SER CIERTAS A LA VEZ, y por eso es")
    print("   PARADA y no eleccion del ejecutor.")
    print("")

    print("E) PASADA 1, LOS CASOS TAL CUAL")
    fallos = 0
    for nombre, real, esperado in casos:
        ok = (real == esperado)
        print("   %-46s %s   (real=%r esperado=%r)"
              % (nombre, "PASA" if ok else "FALLA", real, esperado))
        if not ok:
            fallos += 1
    print("   CIFRA casos: %d | pasan: %d | fallan: %d"
          % (len(casos), len(casos) - fallos, fallos))
    print("")

    print("F) PASADA 2, SE MUTA EL VALOR ESPERADO Y CADA CASO TIENE QUE CAER")
    caen = 0
    for nombre, real, esperado in casos:
        if isinstance(esperado, bool):
            mutado = not esperado
        elif isinstance(esperado, int):
            mutado = esperado + 1
        else:
            mutado = str(esperado) + "_MUTADO"
        cae = (real != mutado)
        print("   %-46s %s   (esperado mutado=%r)"
              % (nombre, "CAE" if cae else "NO CAE", mutado))
        if cae:
            caen += 1
    print("   CIFRA casos que caen al mutar el esperado: %d de %d" % (caen, len(casos)))
    print("")

    if fallos == 0 and caen == len(casos):
        print("VERDE: los %d casos pasan tal cual y los %d caen al mutar el esperado."
              % (len(casos), len(casos)))
        return 0
    print("ROJO: fallos=%d, casos que no caen=%d" % (fallos, len(casos) - caen))
    return 1


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    raise SystemExit(prueba())
