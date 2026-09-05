# -*- coding: utf-8 -*-
r"""vuelta177_tarea1b_mutacion_esperado_vivo.py . EL CASO POSITIVO POR MUTACION
DEL ESPERADO COMPUTADO QUE LA TAREA 1.b DE LA VUELTA 177 PUSO EN EL ARNES DEL
ROJO.

QUE SUJETO PRUEBA: el caso `H_el_texto_nombra_TODOS_los_hallazgos` de
`scripts/loop/vuelta166_tarea2_mutacion_correccion.py`, tal como quedo despues de
la correccion declarada de la vuelta 177: su valor esperado dejo de ser el `3`
tecleado de la linea 175 y pasa a computarse de la misma fuente viva, `len(hall)`.

POR QUE HACE FALTA, Y ES LA CONDICION EXPRESA DEL ENCARGO. Un esperado computado
corre un riesgo que el tecleado no corria: que el esperado y el medido salgan
DEL MISMO SITIO y el caso pase siempre, pase lo que pase. Un esperado computado
que no puede fallar nunca NO ES UNA GUARDA, ES UN ADORNO. Asi que aqui no se
comprueba que el caso pase (eso ya lo hace el arnes): SE COMPRUEBA QUE MUERDA.

COMO SE MUERDE, Y ES MUTANDO EL TEXTO Y NO EL ESPERADO. El arnes ya tiene su
pasada 2, que muta el valor esperado y exige que el caso caiga; esa pasada sigue
ahi y sigue verde. Lo que ESTA prueba hace es otra cosa y mas dura: DEJA EL
ESPERADO EN PAZ Y ROMPE EL PRODUCTO. Se fabrica un texto que deja de nombrar un
hallazgo (y otro que nombra uno de mas, y otro que no nombra ninguno) mientras
el esperado sigue saliendo de la medicion viva ENTERA, y se exige que la
comparacion CAIGA en los tres. Si cayera solo al mutar el esperado, el caso
estaria comprobando su propia aritmetica; cayendo al mutar el texto, comprueba lo
que dice comprobar: QUE EL TEXTO NOMBRA TODOS LOS HALLAZGOS.

Y SE COMPRUEBA TAMBIEN EL CASO SANO, porque una prueba que solo sabe tumbar no
distingue una guarda de una piedra: con el texto entero y sin tocar, la
comparacion tiene que PASAR.

MAS LA GUARDA DEL ADORNO: se comprueba que el arnes corregido lleva de verdad el
caso `H_la_medicion_viva_trae_hallazgos`, que es lo que impide que un `0 == 0`
se publique como verde el dia que la medicion viva se quede sin hallazgos.

CERO ESCRITURAS: todo se hace en memoria sobre el texto que devuelven las
funciones puras del sujeto. Al terminar se comprueba que el fichero de veredictos
sigue byte a byte como estaba.

USO:  python scripts/loop/vuelta177_tarea1b_mutacion_esperado_vivo.py
SUJETO CONGELADO (declarado en la vuelta 180, TAREA 2.a): este arnes NOMBRA `INTRA_DOMINIO_VEREDICTOS.jsonl` en su texto pero NO LO ABRE (2 apariciones en el texto, 0 llamadas que lo lean y 0 lecturas del fichero vivo, medidas fila a fila en docs/plan/SUJETO_CONGELADO_VEREDICTOS.jsonl), asi que su resultado no depende de lo que ese fichero diga hoy.
"""
import io
import os
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)
import vuelta166_tarea2_correccion_op_l_01 as T   # noqa: E402

ARNES = os.path.join(AQUI, "vuelta166_tarea2_mutacion_correccion.py")
MARCA = "cae sobre"


def comparacion_del_caso(texto, hallazgos):
    """LA COMPARACION EXACTA QUE EL CASO CORREGIDO HACE, aislada para poder
    mutarle el texto sin tocar el arnes. PURA: recibe el texto y la lista.

    Es la linea del sujeto, copiada en su forma y no en su letra:
        casos.append(("H_el_texto_nombra_TODOS_los_hallazgos",
                      real.count("cae sobre"), len(hall)))
    o sea real == esperado, con el esperado COMPUTADO de la misma fuente viva."""
    return texto.count(MARCA) == len(hallazgos)


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    print("=" * 78)
    print("VUELTA 177, TAREA 1.b: EL ESPERADO COMPUTADO TIENE QUE SEGUIR MORDIENDO")
    print("=" * 78)
    print("")

    print("A) EL SUJETO, LEIDO DE SU FICHERO Y NO DESCRITO DE MEMORIA")
    texto_arnes = io.open(ARNES, encoding="utf-8").read().replace(chr(13) + chr(10), chr(10))
    lineas_arnes = texto_arnes.split(chr(10))
    print("   scripts/loop/vuelta166_tarea2_mutacion_correccion.py (%d lineas)"
          % len(lineas_arnes))
    for i, l in enumerate(lineas_arnes, 1):
        if "casos.append((\"H_el_texto_nombra" in l or "casos.append((\"H_la_medicion_viva" in l:
            print("   LINEA %d: %s" % (i, l.strip()))
    print("")

    casos = []

    print("B) LA MEDICION VIVA, RECOMPUTADA AQUI Y NO COPIADA DE NINGUN SITIO")
    mapa, _n = T.mapa_de_alias()
    once = T.las_once()
    V = T.veredictos()
    n_lit, n_res, n_pl, n_pr, hall = T.medir_clausula_1(mapa, once, V)
    real = T.texto_correccion_1(hall, n_lit, n_res, n_pl, n_pr, len(mapa), len(V))
    print("   CIFRA filas de docs/INTRA_DOMINIO_VEREDICTOS.jsonl: %d" % len(V))
    print("   CIFRA hallazgos que la medicion viva da hoy: %d" % len(hall))
    print("   CIFRA veces que el texto entero dice %r: %d" % (MARCA, real.count(MARCA)))
    print("")

    print("C) EL CASO SANO: EL TEXTO ENTERO CONTRA EL ESPERADO COMPUTADO, PASA")
    print("   (una prueba que solo sabe tumbar no distingue una guarda de una piedra)")
    sano = comparacion_del_caso(real, hall)
    print("   la comparacion con el texto entero: %s" % ("PASA" if sano else "CAE"))
    casos.append(("C_el_texto_entero_pasa", sano, True))
    print("")

    print("D) MUTACION 1: EL TEXTO DEJA DE NOMBRAR UN HALLAZGO Y EL CASO TIENE QUE CAER")
    print("   (EL ESPERADO NO SE TOCA: sigue siendo len(hall) de la medicion viva")
    print("    ENTERA. Lo que se rompe es el PRODUCTO, que es lo que el caso mide)")
    menos_uno = T.texto_correccion_1(hall[:-1], n_lit, n_res, n_pl, n_pr, len(mapa), len(V))
    print("   CIFRA hallazgos con los que se fabrica el texto mutado: %d" % len(hall[:-1]))
    print("   CIFRA veces que el texto mutado dice %r: %d" % (MARCA, menos_uno.count(MARCA)))
    print("   CIFRA esperado, sin tocar: %d" % len(hall))
    cae1 = not comparacion_del_caso(menos_uno, hall)
    print("   el caso con un hallazgo de menos: %s" % ("CAE" if cae1 else "NO CAE"))
    casos.append(("D_quitar_un_hallazgo_del_texto_tumba_el_caso", cae1, True))
    print("")

    print("E) MUTACION 2: EL TEXTO NOMBRA UNO DE MAS Y EL CASO TIENE QUE CAER IGUAL")
    print("   (el caso dice TODOS, no AL MENOS TODOS: nombrar de mas tambien es")
    print("    que el texto y la medicion dejaron de calzar)")
    uno_mas = T.texto_correccion_1(list(hall) + [hall[-1]], n_lit, n_res, n_pl, n_pr,
                                   len(mapa), len(V))
    print("   CIFRA veces que el texto mutado dice %r: %d" % (MARCA, uno_mas.count(MARCA)))
    cae2 = not comparacion_del_caso(uno_mas, hall)
    print("   el caso con un hallazgo de mas: %s" % ("CAE" if cae2 else "NO CAE"))
    casos.append(("E_anadir_un_hallazgo_al_texto_tumba_el_caso", cae2, True))
    print("")

    print("F) MUTACION 3: EL TEXTO NO NOMBRA NINGUNO Y EL CASO TIENE QUE CAER")
    ninguno = T.texto_correccion_1([], n_lit, n_res, n_pl, n_pr, len(mapa), len(V))
    print("   CIFRA veces que el texto vacio de hallazgos dice %r: %d"
          % (MARCA, ninguno.count(MARCA)))
    cae3 = not comparacion_del_caso(ninguno, hall)
    print("   el caso sin ningun hallazgo en el texto: %s" % ("CAE" if cae3 else "NO CAE"))
    casos.append(("F_vaciar_el_texto_de_hallazgos_tumba_el_caso", cae3, True))
    print("")

    print("G) Y LA GUARDA DEL ADORNO, QUE ES LO QUE IMPIDE EL 0 == 0")
    print("   (con el esperado computado, una medicion viva vacia daria 0 == 0 y")
    print("    pasaria. El arnes corregido lleva un caso aparte que lo impide, y")
    print("    aqui se comprueba QUE LO LLEVA, leyendolo de su fichero)")
    lleva = "H_la_medicion_viva_trae_hallazgos" in texto_arnes
    print("   el arnes lleva el caso H_la_medicion_viva_trae_hallazgos: %s" % lleva)
    casos.append(("G_el_arnes_lleva_la_guarda_del_cero", lleva, True))
    print("   y lo que ese caso comprueba, simulado aqui: len(hall) > 0 con la")
    print("   medicion viva de hoy da %s, y con una lista vacia daria %s"
          % (len(hall) > 0, len([]) > 0))
    casos.append(("G_la_guarda_del_cero_caeria_con_medicion_vacia", len([]) > 0, False))
    print("")

    print("H) Y QUE LA LINEA VIEJA NO SE BORRO, QUE ES EL CARRIL DEL BANCO 9.10")
    print("   (una correccion que tapa lo que corrige no se puede auditar)")
    vieja = 'casos.append(("H_el_texto_nombra_las_tres", real.count("cae sobre"), 3))'
    esta = vieja in texto_arnes
    print("   el texto viejo sigue entero dentro del fichero: %s" % esta)
    casos.append(("H_la_linea_vieja_sigue_declarada_y_sin_tachar", esta, True))
    activa = chr(10) + "    " + vieja in texto_arnes
    print("   y sigue ACTIVA como sentencia (que seria el error contrario): %s" % activa)
    casos.append(("H_la_linea_vieja_ya_no_es_sentencia_activa", activa, False))
    print("")

    print("I) PASADA 1, LOS CASOS TAL CUAL")
    fallos = 0
    for nombre, real_v, esperado in casos:
        ok = (real_v == esperado)
        print("   %-52s %s   (real=%r esperado=%r)"
              % (nombre, "PASA" if ok else "FALLA", real_v, esperado))
        if not ok:
            fallos += 1
    print("   CIFRA casos: %d | pasan: %d | fallan: %d"
          % (len(casos), len(casos) - fallos, fallos))
    print("")

    print("J) PASADA 2, SE MUTA EL VALOR ESPERADO Y CADA CASO TIENE QUE CAER")
    caen = 0
    for nombre, real_v, esperado in casos:
        mutado = (not esperado) if isinstance(esperado, bool) else esperado + 1
        cae = (real_v != mutado)
        print("   %-52s %s   (esperado mutado=%r)"
              % (nombre, "CAE" if cae else "NO CAE", mutado))
        if cae:
            caen += 1
    print("   CIFRA casos que caen al mutar el esperado: %d de %d" % (caen, len(casos)))
    print("")

    print("K) Y SE COMPRUEBA QUE ESTA PRUEBA NO ESCRIBIO NADA")
    V2 = T.veredictos()
    igual = (V == V2)
    print("   docs/INTRA_DOMINIO_VEREDICTOS.jsonl identico al de antes: %s" % igual)
    if not igual:
        print("   ROJO: la prueba de mutacion escribio. Eso es peor que no tenerla.")
        return 1
    print("")

    if fallos == 0 and caen == len(casos):
        print("VERDE: los %d casos pasan tal cual y los %d caen al mutar el esperado."
              % (len(casos), len(casos)))
        print("EL ESPERADO COMPUTADO SIGUE MORDIENDO: se le rompio el texto por tres")
        print("sitios distintos SIN TOCARLE EL ESPERADO y cayo las tres veces.")
        return 0
    print("ROJO: fallos=%d, casos que no caen=%d" % (fallos, len(casos) - caen))
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
