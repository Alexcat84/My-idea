# -*- coding: utf-8 -*-
r"""vuelta166_tarea3_mutacion_retrato.py . CASO POSITIVO POR MUTACION DEL
RECOMPUTO DEL RETRATO DE LAS A (TAREA 3 de la vuelta 166), CON NOMBRE DE ARNES
para que la bateria lo vea (invoca cada arnes SIN ARGUMENTOS).

QUE PRUEBA, Y POR QUE ES ESTO. Lo que esta TAREA promete es que la correccion
entra por el carril del banco 9.10: contador CUADRADO en el mismo acto, nota
fechada ADOSADA, ninguna cifra vieja borrada y ninguna nota vieja reescrita.
Y la mitad mas fragil de esa promesa es el CONTADOR: la caida historica de esta
tabla (vueltas 51 y 52) fue exactamente que la cadena crecio y el contador no.
Por eso el contador se COMPUTA de la cadena y NO se lee de la palabra escrita, y
por eso el caso central de esta prueba es: si alguien desincroniza la palabra, el
computo tiene que seguir a la CADENA y la guarda tiene que CAER.

CERO ESCRITURAS: todo se hace en memoria sobre copias de las lineas leidas, y al
final se comprueba que el documento sigue byte a byte como estaba.

USO:  python scripts/loop/vuelta166_tarea3_mutacion_retrato.py
"""
import io
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import vuelta166_tarea3_retrato_de_las_a as T   # noqa: E402


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    print("=" * 78)
    print("VUELTA 166, TAREA 3: CASO POSITIVO POR MUTACION DEL CARRIL DEL 9.10")
    print("=" * 78)
    print("")

    antes = io.open(T.DOC, encoding="utf-8").read()
    lineas = antes.split("\n")
    filas, errores = T.localizar_filas(lineas)
    casos = []

    print("A) EL SUJETO, LEIDO DEL DOCUMENTO DE VERDAD")
    print("   docs/plan/RECOMPUTO_3388.md, %d lineas" % len(lineas))
    print("   CIFRA filas del PASO 1 localizadas: %d | errores: %d"
          % (len(filas), len(errores)))
    casos.append(("A_las_cuatro_filas_se_localizan", len(filas), 4))
    casos.append(("A_sin_errores_de_localizacion", len(errores), 0))
    por_clave = {c: (n, t) for c, n, t in filas}
    print("")

    print("B) EL CONTADOR SE COMPUTA DE LA CADENA Y NO DE LA PALABRA ESCRITA")
    n, t = por_clave["colapsos"]
    tach, viva, cuantas = T.anatomia(t)
    print("   la fila de los colapsos trae %d tachadas y la palabra %s"
          % (cuantas, T.PAT_CONTADOR.search(t.split("|")[2]).group(2)))
    _c, antes_p, despues_p = T.cuadrar_contador(t.split("|")[2], cuantas)
    casos.append(("B_con_%d_tachadas_el_siguiente_es_TRECE" % cuantas,
                  despues_p, "TRECE VECES"))
    mutada = t.replace("DOCE VECES,", "DOS VECES,", 1)
    tm, vm, cm = T.anatomia(mutada)
    _c2, antes2, despues2 = T.cuadrar_contador(mutada.split("|")[2], cm)
    print("   se MUTA la palabra a DOS VECES sin tocar la cadena")
    print("   la palabra escrita pasa a %r y el computo sigue dando %r"
          % (antes2, despues2))
    casos.append(("B_mutar_la_palabra_no_mueve_el_computo", despues2, "TRECE VECES"))
    casos.append(("B_la_cadena_sigue_teniendo_las_mismas_tachadas", cm, cuantas))
    lm = list(lineas)
    lm[n - 1] = mutada
    print("   y la guarda de que todos cuadran, sobre el documento MUTADO:")
    print("      %s" % ("CUADRA" if T.todos_cuadran(lm) else "CAE"))
    casos.append(("B_la_guarda_CAE_con_el_contador_desincronizado",
                  T.todos_cuadran(lm), False))
    casos.append(("B_y_PASA_sobre_el_documento_sin_mutar",
                  T.todos_cuadran(lineas), True))
    print("")

    print("C) LA CIFRA VIEJA NO SE BORRA: SE TACHA Y SE QUEDA")
    nota = T.nota_de_la_fila("colapsos", viva, 398, cuantas, [],
                             {"crudas": 551, "colapsos": 398})
    nueva_fila, a0, a1 = T.fila_corregida(t, viva, 398, cuantas, nota)
    print("   cifra viva antes: %s" % viva)
    print("   la fila nueva contiene ~~**%s**~~: %s"
          % (viva, ("~~**%s**~~" % viva) in nueva_fila))
    casos.append(("C_la_vieja_queda_tachada_y_entera",
                  ("~~**%s**~~" % viva) in nueva_fila, True))
    casos.append(("C_la_nueva_esta_viva", "**398**" in nueva_fila, True))
    sobreviven = sum(1 for x in tach if ("~~**%s**~~" % x) in nueva_fila)
    print("   de las %d tachadas viejas sobreviven %d" % (len(tach), sobreviven))
    casos.append(("C_las_doce_tachadas_viejas_sobreviven", sobreviven, len(tach)))
    casos.append(("C_la_fila_solo_crece", len(nueva_fila) > len(t), True))
    print("")
    print("D) LA CELDA QUE NO SALE DE UN INSTRUMENTO NO SE ESCRIBE")
    bueno = ("A crudas en el archivo (clase == 'A'): 551\n"
             "de esas, colapsan a auto-arista tras resolver (mismo nodo vivo en los "
             "dos lados): 398\n"
             "PARES DISTINTOS EN EL RETRATO (tras resolver y deduplicar): 149\n"
             "de esos, con mas de un veredicto crudo apuntando al mismo par "
             "resuelto: 4\n")
    d, faltan, pares = T.leer_paso_1(bueno)
    print("   salida completa -> %d cifras, %d faltan" % (len(d), len(faltan)))
    casos.append(("D_la_salida_completa_da_las_cuatro", len(faltan), 0))
    casos.append(("D_y_las_lee_bien", [d[k] for _p, k in T.FILAS], [551, 398, 149, 4]))
    for quitar, etiqueta in ((0, "crudas"), (2, "distintos"), (3, "multiples")):
        roto = "\n".join(l for i, l in enumerate(bueno.strip().split("\n"))
                         if i != quitar) + "\n"
        _d2, f2, _p2 = T.leer_paso_1(roto)
        print("   sin la linea de %-10s -> faltan %d (%s)"
              % (etiqueta, len(f2), ", ".join(f2)))
        casos.append(("D_sin_%s_el_lector_lo_dice" % etiqueta, f2, [etiqueta]))
    print("")

    print("E) EL TEXTO DE LA NOTA SIGUE A LA MEDICION Y NO A UNA CONSTANTE")
    n1 = T.nota_de_la_fila("colapsos", "207", 398, 12, [],
                           {"crudas": 551, "colapsos": 398})
    n2 = T.nota_de_la_fila("colapsos", "207", 300, 12, [],
                           {"crudas": 551, "colapsos": 300})
    print("   con 398 la nota dice 'de 207 a 398': %s" % ("de 207 a 398" in n1))
    print("   con 300 la nota dice 'de 207 a 300': %s" % ("de 207 a 300" in n2))
    casos.append(("E_la_nota_lleva_la_cifra_medida", "de 207 a 398" in n1, True))
    casos.append(("E_y_cambia_si_la_medicion_cambia", n1 == n2, False))
    casos.append(("E_el_ordinal_sale_del_conteo",
                  "DECIMOTERCERA CORRECCION" in n1, True))
    n3 = T.nota_de_la_fila("colapsos", "207", 398, 5, [],
                           {"crudas": 551, "colapsos": 398})
    casos.append(("E_con_cinco_tachadas_el_ordinal_es_SEXTA",
                  "SEXTA CORRECCION" in n3, True))
    pares_reales = [("['a', 'b']", "[1, 2]"), ("['c', 'd']", "[3, 4]")]
    n4 = T.nota_de_la_fila("multiples", "0", 2, 0, pares_reales,
                           {"crudas": 551, "colapsos": 398})
    print("   la nota de los multiples nombra los pares uno por uno: %s"
          % all(p in n4 for p, _q in pares_reales))
    casos.append(("E_la_nota_de_multiples_nombra_sus_pares",
                  sum(1 for p, _q in pares_reales if p in n4), 2))
    casos.append(("E_y_dice_que_no_adjudica_clase",
                  "NO ADJUDICA CLASE" in n4, True))
    n5 = T.nota_de_la_fila("distintos", "344", 149, 15, [],
                           {"crudas": 551, "colapsos": 398})
    casos.append(("E_la_nota_de_distintos_avisa_de_la_resta_rota",
                  "ya NO es la resta exacta" in n5, True))
    print("")

    print("F) PASADA 1, LOS CASOS TAL CUAL")
    fallos = 0
    for nombre, real, esperado in casos:
        ok = (real == esperado)
        print("   %-52s %s   (real=%r esperado=%r)"
              % (nombre, "PASA" if ok else "FALLA", real, esperado))
        if not ok:
            fallos += 1
    print("   CIFRA casos: %d | pasan: %d | fallan: %d"
          % (len(casos), len(casos) - fallos, fallos))
    print("")

    print("G) PASADA 2, SE MUTA EL VALOR ESPERADO Y CADA CASO TIENE QUE CAER")
    caen = 0
    for nombre, real, esperado in casos:
        if isinstance(esperado, bool):
            mutado = not esperado
        elif isinstance(esperado, int):
            mutado = esperado + 1
        elif isinstance(esperado, list):
            mutado = esperado + ["_mutado"]
        else:
            mutado = str(esperado) + "_mutado"
        cae = (real != mutado)
        print("   %-52s %s   (esperado mutado=%r)"
              % (nombre, "CAE" if cae else "NO CAE", mutado))
        if cae:
            caen += 1
    print("   CIFRA casos que caen al mutar el esperado: %d de %d" % (caen, len(casos)))
    print("")

    print("H) Y SE COMPRUEBA QUE ESTA PRUEBA NO ESCRIBIO NADA")
    despues = io.open(T.DOC, encoding="utf-8").read()
    print("   el documento es identico byte a byte al de antes: %s"
          % (antes == despues))
    if antes != despues:
        print("   ROJO: la prueba de mutacion escribio.")
        return 1
    print("")

    if fallos == 0 and caen == len(casos):
        print("VERDE: los %d casos pasan tal cual y los %d caen al mutar el esperado."
              % (len(casos), len(casos)))
        return 0
    print("ROJO: fallos=%d, casos que no caen=%d" % (fallos, len(casos) - caen))
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
