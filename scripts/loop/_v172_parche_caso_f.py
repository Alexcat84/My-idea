# -*- coding: utf-8 -*-
r"""_v172_parche_caso_f.py . ANDAMIO DE UN SOLO USO DE LA VUELTA 172, TAREA 4.a.

REFUNDA EL CASO `F` DE `scripts/loop/vuelta171_tarea5a_mutacion_enchufe.py` SOBRE
SUJETO CONGELADO (adjudicacion 6.4 del acta 171).

EL HECHO MEDIDO: el caso `F_el_reporte_170_del_repo_esta_archivado_y_calza`
llamaba a la guarda **contra el arbol vivo** y esperaba `True`. Eso solo fue
cierto durante los minutos que van del archivado de la 170 al momento en que el
esqueleto piso `REPORTE.md`. **Hoy es falso y lo sera para siempre**, y por eso
el arnes daba EXIT 1 con 9 de 10 casos pasando.

CONTRA QUE REGLA IBA: la condicion de la vuelta 148, SUJETO CONGELADO, que la
6.10 del acta 170 confirmo con esas palabras. Los otros nueve casos fabrican su
sujeto en un temporal; **el decimo no tenia sujeto propio, tenia el repo**.

QUE SE PONE EN SU SITIO, Y NO ES UN CASO DE ADORNO: el `F` cubria una dimension
que los otros nueve no cubren, que es **un sujeto con forma de reporte de
verdad** y no una cadena de tres lineas. Se conserva esa dimension y se le anade
la que faltaba:

  F.1  el caso VERDE sobre un sujeto GRANDE y con forma de reporte de verdad
       (cabecera, secciones 0 a 9, tablas, miles de bytes), fabricado en el
       temporal. La guarda tiene que dejar escribir.
  F.2  UN BYTE CAMBIADO EN MEDIO del texto, no al final. El caso `E` ya prueba un
       byte de mas AL FINAL; este prueba que la guarda tampoco se traga un cambio
       enterrado en mitad de un fichero grande, que es como se pierde texto de
       verdad.
  F.3  EL MISMO TEXTO CON FIN DE LINEA DE WINDOWS. La guarda normaliza CRLF antes
       de computar el sha256, y eso es una decision suya que conviene tener
       PROBADA en vez de supuesta: en este repo `git` convierte finales de linea
       al tocar los ficheros, asi que si la guarda no normalizara, saltaria en
       rojo cada vez que alguien abriera el reporte con un editor de Windows.

LA CIFRA QUE EL REPORTE DE LA 171 PUBLICO ("10 casos, 10 pasan, 10 caen") ERA
CIERTA CUANDO SE CORRIO y no se retira: lo que no se sostenia era el arnes.

USO:  python scripts/loop/_v172_parche_caso_f.py
"""
import io
import os
import py_compile

NL = chr(10)
RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
RUTA = os.path.join(RAIZ, "scripts", "loop", "vuelta171_tarea5a_mutacion_enchufe.py")

VIEJO = [
    '        print("F) EL REPO DE VERDAD, EN MODO SOLO COMPROBACION (cero escrituras)")',
    '        ok, inf = PASO0.exigir_archivado(170, ejecutar_archivador=False)',
    '        print("   ok=%r motivos=%s" % (ok, _motivos(inf)))',
    '        for l in inf:',
    '            print("   " + l)',
    '        casos.append(("F_el_reporte_170_del_repo_esta_archivado_y_calza", ok, True))',
    '        print("")',
]

NUEVO = [
    '        print("F) EL CASO VERDE SOBRE UN SUJETO GRANDE Y CON FORMA DE REPORTE DE")',
    '        print("   VERDAD, FABRICADO EN EL TEMPORAL. REFUNDADO EN LA VUELTA 172,")',
    '        print("   TAREA 4.a: antes miraba EL ARBOL VIVO y por eso caducaba solo.")',
    '        grande = _reporte_grande(170)',
    '        print("   sujeto fabricado: %d bytes, %d saltos de linea"',
    '              % (len(grande.encode("utf-8")), grande.count(chr(10))))',
    '        _escribir(os.path.join(arch, "REPORTE_V170.md"), grande)',
    '        _escribir(vivo, grande)',
    '        ok, inf = PASO0.exigir_archivado(170, ruta_reporte=vivo, dir_archivo=arch,',
    '                                         ejecutar_archivador=False)',
    '        print("   F.1 los dos identicos -> ok=%r motivos=%s" % (ok, _motivos(inf)))',
    '        casos.append(("F1_sujeto_grande_identico_deja_escribir", ok, True))',
    '        casos.append(("F1_y_no_hay_ningun_motivo", _motivos(inf), []))',
    '',
    '        medio = len(grande) // 2',
    '        picado = grande[:medio] + ("X" if grande[medio] != "X" else "Y") + grande[medio + 1:]',
    '        _escribir(vivo, picado)',
    '        ok, inf = PASO0.exigir_archivado(170, ruta_reporte=vivo, dir_archivo=arch,',
    '                                         ejecutar_archivador=False)',
    '        print("   F.2 un byte cambiado EN MEDIO (posicion %d de %d) -> ok=%r motivos=%s"',
    '              % (medio, len(grande), ok, _motivos(inf)))',
    '        casos.append(("F2_un_byte_en_medio_tambien_la_tumba", ok, False))',
    '        casos.append(("F2_y_el_motivo_es_la_d", _motivos(inf), ["d"]))',
    '        casos.append(("F2_el_picado_mide_lo_mismo_que_el_bueno",',
    '                      len(picado) == len(grande), True))',
    '',
    '        _escribir(vivo, grande.replace(chr(10), chr(13) + chr(10)))',
    '        ok, inf = PASO0.exigir_archivado(170, ruta_reporte=vivo, dir_archivo=arch,',
    '                                         ejecutar_archivador=False)',
    '        print("   F.3 el mismo texto con fin de linea de Windows -> ok=%r motivos=%s"',
    '              % (ok, _motivos(inf)))',
    '        casos.append(("F3_el_CRLF_no_la_tumba_porque_la_guarda_normaliza", ok, True))',
    '        print("")',
]

FABRICADOR = '''def _reporte_grande(vuelta):
    """UN SUJETO CON FORMA DE REPORTE DE VERDAD, FABRICADO EN MEMORIA (vuelta
    172, TAREA 4.a).

    POR QUE HACE FALTA: los casos A a E usan una cadena de tres lineas, y el
    caso `F` cubria, sin decirlo, la dimension de un fichero GRANDE y con
    estructura. Al refundar `F` sobre sujeto congelado esa dimension se conserva
    aqui en vez de perderse.

    ES DETERMINISTA Y NO LEE NADA: mismo texto en cada corrida, hoy y dentro de
    diez vueltas."""
    L = ["# REPORTE DE LA VUELTA %d (de mentira, fabricado por la prueba de "
         "mutacion). Rama `de-mentira`." % vuelta, ""]
    L.append("**EL VEREDICTO DE UNA LINEA: fabricado.**")
    L.append("")
    for k in range(10):
        L.append("## %d. SECCION FABRICADA NUMERO %d" % (k, k))
        L.append("")
        L.append("| celda | de donde sale | valor |")
        L.append("|---|---|---:|")
        for j in range(12):
            L.append("| fila %02d de la seccion %d | fabricada | %d |" % (j, k, j * k))
        L.append("")
        for j in range(6):
            L.append("Parrafo %d de la seccion %d, con texto suficiente para que el "
                     "fichero pase de los pocos bytes de los casos A a E y se parezca "
                     "a un reporte de verdad." % (j, k))
        L.append("")
    return chr(10).join(L)


'''


def main():
    t = io.open(RUTA, encoding="utf-8").read().replace(chr(13) + NL, NL)

    viejo, nuevo = NL.join(VIEJO), NL.join(NUEVO)
    assert t.count(viejo) == 1, "el caso F viejo no calza"
    t = t.replace(viejo, nuevo)

    ancla = "def _motivos(informe):"
    assert t.count(ancla) == 1
    t = t.replace(ancla, FABRICADOR + ancla)

    # La cifra del rotulo del docstring, si la hubiera, y la nota de la refundacion.
    ancla_doc = 'def prueba_de_mutacion():'
    assert t.count(ancla_doc) == 1
    nota = (
        '# --------------------------------------------------------------------------\n'
        '# EL CASO `F` SE REFUNDO EN LA VUELTA 172, TAREA 4.a (adjudicacion 6.4 del acta\n'
        '# 171). ANTES ERA: `F_el_reporte_170_del_repo_esta_archivado_y_calza`, que\n'
        '# llamaba a `PASO0.exigir_archivado(170, ejecutar_archivador=False)` CONTRA EL\n'
        '# ARBOL VIVO y esperaba True. Eso solo fue cierto durante los minutos entre\n'
        '# archivar la 170 y pisar REPORTE.md con el esqueleto de la 171; despues es\n'
        '# falso para siempre, y el arnes salia EXIT 1 con 9 de 10.\n'
        '#\n'
        '# CONTRA QUE REGLA IBA: la condicion de la vuelta 148, SUJETO CONGELADO, que la\n'
        '# 6.10 del acta 170 confirmo con esas palabras. LA FRASE VIEJA NO SE BORRA DE LA\n'
        '# HISTORIA: queda escrita aqui, que es donde se puede auditar.\n'
        '#\n'
        '# LA CIFRA QUE EL REPORTE DE LA 171 PUBLICO ("10 casos, 10 pasan, 10 caen") ERA\n'
        '# CIERTA CUANDO SE CORRIO y no se retira. Lo que no se sostenia era el arnes.\n'
        '# --------------------------------------------------------------------------\n')
    t = t.replace(ancla_doc, nota + ancla_doc)

    io.open(RUTA, "w", encoding="utf-8", newline=NL).write(t)
    py_compile.compile(RUTA, doraise=True)
    print("REFUNDADO: scripts/loop/vuelta171_tarea5a_mutacion_enchufe.py")
    print("COMPILA: OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
