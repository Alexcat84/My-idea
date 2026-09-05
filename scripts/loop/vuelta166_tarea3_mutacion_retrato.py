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
import vuelta170_tarea1b_medir_tachadas_por_commit as M   # noqa: E402


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
    # (2.a) RE ANCLADO EN LA VUELTA 169, adjudicacion 6.2 del acta 168.
    # LA PALABRA ESPERADA SALE DEL COMPUTO, igual que `cuantas`, y NO de una
    # constante tecleada. Antes decia, literal: despues_p, "TRECE VECES", y
    # ~~el 4 sep 2026 la vuelta 167 anadio una tachada por el carril del 9.10:~~
    # ~~el computo paso a CATORCE, la constante se quedo en TRECE y el caso~~
    # ~~empezo a fallar por su valor esperado y no por su sujeto.~~ EL FILO NO SE
    # AFLOJA: despues_p sigue saliendo de T.cuadrar_contador y el esperado
    # de T.CARDINAL leido con `cuantas`, que son DOS caminos distintos; si
    # cuadrar_contador volviera a leer la palabra escrita en vez de contar
    # la cadena, este caso CAE.
    #
    # CORRECCION FECHADA Y ADOSADA (4 sep 2026, vuelta 170, TAREA 1.b, por el
    # carril del banco 9.10 y la adjudicacion 6.2 del acta 169). LAS TRES LINEAS
    # DE ARRIBA QUEDAN ENTERAS Y TACHADAS, NO SE BORRAN: taparlas impediria
    # auditar que se dijeron. LO QUE DICEN ES FALSO EN SU MITAD CENTRAL, y la
    # caida es de las gordas porque vive en el texto de una guarda (CUARTA SEDE)
    # y por tanto cuenta como CIFRA PUBLICADA.
    #
    # QUIEN ANADIO LA DECIMOTERCERA TACHADA: LA VUELTA 166, en el commit
    # 33fe1380, que es el MISMO COMMIT QUE CREO ESTE ARNES. No fue la 167. La
    # propia vuelta 169 ya lo habia escrito bien antes, en su commit 1eec382f,
    # al pie del reporte de la 168 ("el arnes NACIO ROJO en su PROPIO commit
    # 33fe1380, de la vuelta 166, y la 167 NO movio esa fila"), y unas horas
    # despues escribio aqui lo contrario: la vuelta se contradijo a si misma en
    # la misma sesion.
    #
    # LA TABLA, MEDIDA EN LA VUELTA 170 Y NO COPIADA DEL ACTA, con
    # scripts/loop/vuelta170_tarea1b_medir_tachadas_por_commit.py, que recorre
    # los 38 commits que tocan docs/plan/RECOMPUTO_3388.md, lee el BLOB de cada
    # uno y cuenta la cadena con el localizador y el contador del PROPIO
    # instrumento del retrato (T.localizar_filas y T.anatomia), no con un grep.
    # Salida: docs/loop/SALIDA_V170_T1B_TACHADAS_POR_COMMIT.txt.
    #
    #     commit     vuelta  fecha        tachadas
    #     7f4ec6d9   11      2026-08-13   0    (la primera de la serie)
    #     3ffc2091   58      2026-08-20   12
    #     33fe1380   166     2026-09-04   13   LA DECIMOTERCERA ENTRA AQUI
    #     c6ac70f6   167     2026-09-04   13   (ultimo commit que toca el fichero)
    #     el arbol de trabajo de hoy:      13
    #
    # La vuelta de esos dos commits NO se supone: su asunto no la nombra, asi
    # que se COMPUTA por el invariante de la casa (los commits posteriores al
    # ACTA DE LA VUELTA N son de la vuelta N mas 1). El ultimo acta anterior a
    # 33fe1380 es 00cfe6e0, ACTA DE LA VUELTA 165; luego 33fe1380 es de la 166.
    #
    # Y AQUI VA LA PRECISION QUE LA RELECTURA AL DOBLE OBLIGO A ANADIR, porque
    # la primera version de esta misma tabla puso a c6ac70f6 en la 166 y esta en
    # la 167: LA VUELTA 167 SI TOCO EL FICHERO, en c6ac70f6 ("TAREA 4: el rotulo
    # ancho dice ahora de que poblacion habla, y el 4 no se toca"), PERO NO TOCO
    # ESTA FILA. Comparadas las cuatro filas del PASO 1 entre el blob de
    # 33fe1380 y el de c6ac70f6: `colapsos` IGUAL, `crudas` IGUAL, `distintos`
    # IGUAL, y solo `multiples` DISTINTA, que es el rotulo que esa TAREA 4
    # arreglaba. Por eso el reporte de la 168 acerto al decir "la 167 NO movio
    # esa fila", y por eso lo unico falso es "anadio una tachada".
    #
    # Y POR QUE EL COMPUTO DICE CATORCE, que es la otra mitad que faltaba: NO
    # porque nadie anadiera nada en la 167, sino porque TRECE TACHADAS HACEN QUE
    # LA SIGUIENTE CORRECCION SEA LA DECIMOCUARTA. `siguiente = T.CARDINAL[
    # cuantas + 1]` con cuantas = 13 da "CATORCE VECES". La constante tecleada
    # "TRECE VECES" no se quedo atras porque la tabla creciera despues de ella:
    # se quedo atras porque nacio mal, contando la cadena en vez de contar la
    # cadena mas uno, en el mismo commit que creo el arnes.
    #
    # EL REMEDIO ESTA EN EL CASO `B_la_decimotercera_nace_en_el_commit_medido`
    # (vuelta 170, TAREA 1.c): esta historia deja de vivir SOLO en este
    # comentario y pasa a estar ANCLADA POR MEDICION contra git. Un comentario
    # se pudre; un caso cae.
    siguiente = T.CARDINAL[cuantas + 1]
    casos.append(("B_con_%d_tachadas_el_siguiente_es_%s"
                  % (cuantas, siguiente.split()[0]), despues_p, siguiente))
    # (2.b) RE ANCLADO EN LA VUELTA 169, adjudicacion 6.2 del acta 168.
    # LA MUTACION DEJA DE ESTAR CLAVADA AL TEXTO VIVO. Antes decia, literal:
    # t.replace("DOCE VECES,", "DOS VECES,", 1), y el dia que la fila crecio
    # ese literal dejo de existir: el replace no encontraba nada, la fila no se
    # mutaba y el caso que espera que la guarda CAIGA recibia CUADRA. Ahora se
    # muta LA PALABRA QUE EL PROPIO INSTRUMENTO ACABA DE LEER, y la palabra
    # falsa sale de T.CARDINAL eligiendo una DISTINTA de la viva.
    m_viva = T.PAT_CONTADOR.search(t.split("|")[2])
    palabra_viva = "%s %s" % (m_viva.group(2), m_viva.group(3))
    palabra_falsa = T.CARDINAL[2] if palabra_viva != T.CARDINAL[2] else T.CARDINAL[3]
    mutada = t.replace(palabra_viva + ",", palabra_falsa + ",", 1)
    # Y LA GUARDA QUE FALTABA, que es la que dejaba muda a la de abajo:
    # si el replace no cambia NADA, este caso CAE y el arnes sale en rojo, en
    # vez de seguir corriendo sobre una fila sin mutar.
    casos.append(("B_la_mutacion_MUERDE_el_texto_vivo", mutada != t, True))
    tm, vm, cm = T.anatomia(mutada)
    _c2, antes2, despues2 = T.cuadrar_contador(mutada.split("|")[2], cm)
    print("   se MUTA la palabra viva %r a %r sin tocar la cadena"
          % (palabra_viva, palabra_falsa))
    print("   la palabra escrita pasa a %r y el computo sigue dando %r"
          % (antes2, despues2))
    # (2.a, segundo caso) MISMO RE ANCLAJE. Antes decia, literal:
    # despues2, "TRECE VECES". El esperado sale de `cm`, que es la cadena
    # contada SOBRE LA FILA YA MUTADA: si la mutacion de la palabra tocara la
    # cadena sin querer, `cm` cambiaria y este caso CAE.
    casos.append(("B_mutar_la_palabra_no_mueve_el_computo",
                  despues2, T.CARDINAL[cm + 1]))
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
    # RETOQUE DE ROTULO DECLARADO EN LA VUELTA 169 (no encargado por nombre,
    # declarado en el reporte): el rotulo tecleaba DOCE y su propia cifra sale
    # de len(tach), que hoy vale 13. Ninguna comprobacion cambia.
    casos.append(("C_las_%d_tachadas_viejas_sobreviven" % len(tach),
                  sobreviven, len(tach)))
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

    print("F) EL NACIMIENTO DE LA DECIMOTERCERA TACHADA, ANCLADO POR MEDICION")
    print("   CONTRA GIT (vuelta 170, TAREA 1.c, adjudicacion 6.3 del acta 169)")
    print("")
    print("   POR QUE ESTE CASO EXISTE. La caida 4.1 del acta 169 fue una HISTORIA")
    print("   FALSA escrita en el comentario de arriba: decia que la vuelta 167")
    print("   anadio una tachada. Una historia escrita en un comentario se pudre")
    print("   porque nada la comprueba; una anclada en un caso CAE. Aqui la misma")
    print("   afirmacion deja de ser prosa y se lee de git en cada corrida.")
    print("   LAS FUNCIONES SE IMPORTAN, NO SE COPIAN: una sola fuente.")
    tabla_git = M.serie_medida()
    nac = M.nacimiento_de_la_tachada(13, tabla_git)
    print("   CIFRA commits de la serie: %d" % len(tabla_git))
    casos.append(("F_la_serie_de_git_no_esta_vacia", len(tabla_git) > 0, True))
    if nac is None:
        print("   ROJO PREVIO: ningun commit de la serie llega a 13 tachadas.")
        return 1
    vuelta_nac = M.vuelta_computada_de(nac[0])
    print("   el primer commit cuya fila llega a 13 tachadas: %s" % nac[0][:8])
    print("   su vuelta, COMPUTADA de las actas: %s" % vuelta_nac)
    casos.append(("F_la_13a_nace_en_33fe1380", nac[0][:8], "33fe1380"))
    casos.append(("F_y_su_vuelta_computada_es_166", vuelta_nac, 166))
    anteriores_git = [f for f in tabla_git if f[3] < 13]
    print("   el commit inmediatamente anterior: %s con %d tachadas"
          % (anteriores_git[-1][0][:8], anteriores_git[-1][3]))
    casos.append(("F_el_commit_anterior_es_3ffc2091",
                  anteriores_git[-1][0][:8], "3ffc2091"))
    casos.append(("F_y_traia_DOCE_tachadas", anteriores_git[-1][3], 12))

    # LA MITAD NEGATIVA, que es la que la caida 4.1 dijo al reves. Se BUSCA en
    # vez de suponerse: una busqueda negativa no se puede citar (EJECUTOR.md 9).
    saltos_git = [(tabla_git[i - 1], tabla_git[i])
                  for i in range(1, len(tabla_git))
                  if tabla_git[i][3] != tabla_git[i - 1][3]]
    de_167 = [b for _a, b in saltos_git if M.vuelta_computada_de(b[0]) == 167]
    print("   CIFRA commits que SUBEN el conteo y son de la vuelta 167: %d"
          % len(de_167))
    casos.append(("F_la_167_no_sube_el_conteo_ni_una_vez", len(de_167), 0))

    # Y LA PRECISION QUE LA MEDICION OBLIGO A ESCRIBIR: la 167 SI toco el
    # fichero, en c6ac70f6, pero NO esta fila. Se comprueba con el conteo de la
    # fila entre los dos blobs, no fiandose del asunto del commit.
    ultimo = tabla_git[-1]
    print("   ultimo commit que toca el fichero: %s, vuelta computada %s"
          % (ultimo[0][:8], M.vuelta_computada_de(ultimo[0])))
    casos.append(("F_el_ultimo_que_toca_el_fichero_es_c6ac70f6",
                  ultimo[0][:8], "c6ac70f6"))
    casos.append(("F_y_ES_de_la_vuelta_167",
                  M.vuelta_computada_de(ultimo[0]), 167))
    casos.append(("F_pero_NO_movio_esta_fila", ultimo[3], nac[3]))
    print("   tachadas en el nacimiento: %d | en el ultimo: %d | hoy en disco: %d"
          % (nac[3], ultimo[3], M.tachadas_de_hoy()))
    casos.append(("F_y_hoy_en_disco_siguen_siendo_las_mismas",
                  M.tachadas_de_hoy(), nac[3]))

    # Y LA OTRA MITAD DE LA CORRECCION, tambien anclada: por que el computo dice
    # CATORCE. No porque nadie anadiera nada, sino porque trece mas uno.
    casos.append(("F_trece_tachadas_hacen_que_la_siguiente_sea_CATORCE",
                  T.CARDINAL[M.tachadas_de_hoy() + 1], "CATORCE VECES"))
    print("")

    print("G) PASADA 1, LOS CASOS TAL CUAL")
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

    print("H) PASADA 2, SE MUTA EL VALOR ESPERADO Y CADA CASO TIENE QUE CAER")
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

    print("I) Y SE COMPRUEBA QUE ESTA PRUEBA NO ESCRIBIO NADA")
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
