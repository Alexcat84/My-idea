# -*- coding: utf-8 -*-
r"""vuelta171_tarea5a_mutacion_enchufe.py . CASO POSITIVO POR MUTACION DEL PASO 0
DEL ESQUELETO (el archivador enchufado), TAREA 5.a DE LA VUELTA 171.

POR QUE EXISTE ESTE FICHERO Y NO SOLO UN FLAG: la bateria
`scripts/loop/verificar_mutaciones_viejas.py` invoca cada arnes SIN ARGUMENTOS.
Una prueba que vive detras de un `--mutar` de otro fichero no la corre nadie
desde la bateria.

QUE PRUEBA (adjudicacion 6.6 del acta 170: "el esqueleto se niega a escribir si
el reporte anterior no esta archivado ... con su caso positivo por mutacion"):
que la guarda CAE en los cuatro modos por los que puede caer, y que PASA cuando
y solo cuando lo que se va a pisar ya esta guardado.

  (a) el archivador no sale verde        -> no se ejercita aqui: se ejercita en
      la corrida real, y la (d) lo cubre.
  (b) no existe el archivo del reporte anterior
  (c) el archivo existe pero lleva el reporte de OTRA vuelta
  (d) el archivo existe y es de la vuelta buena PERO NO ES lo que se va a pisar

SUJETO: fabricado EN MEMORIA y en un directorio temporal del sistema, NUNCA en
el repo. CERO escrituras bajo `docs/` y bajo `scripts/`. El caso VERDE se corre
ademas contra el repo REAL en modo solo comprobacion, que tampoco escribe.

SUJETO CONGELADO, que es la condicion de entrada a la bateria desde la vuelta
148 (TAREA 2.5, adjudicacion 3.5 del acta 147): los reportes de mentira son
literales de este proceso, y el unico sujeto de repo que se lee es
`docs/loop/reportes/REPORTE_V170.md`, que es un reporte de una vuelta ya
cerrada y firmada.

NINGUN VEREDICTO ES UNA CONSTANTE LITERAL: cada caso sale de llamar a la funcion
real `PASO0.exigir_archivado` sobre un sujeto distinto, y la segunda pasada muta
cada valor esperado y exige que el caso CAIGA.

USO:  python scripts/loop/vuelta171_tarea5a_mutacion_enchufe.py
"""
import io
import os
import shutil
import sys
import tempfile

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import paso0_archivar_anterior as PASO0   # noqa: E402

RAIZ = PASO0.RAIZ


def _escribir(ruta, texto):
    d = os.path.dirname(ruta)
    if not os.path.isdir(d):
        os.makedirs(d)
    io.open(ruta, "w", encoding="utf-8", newline="\n").write(texto)


def _reporte_falso(vuelta, cola=""):
    return ("# REPORTE DE LA VUELTA %d (de mentira, fabricado por la prueba de "
            "mutacion). Rama `de-mentira`.\n\ncuerpo cualquiera\n%s" % (vuelta, cola))


def _reporte_grande(vuelta):
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


def _motivos(informe):
    """Los codigos de motivo que la guarda imprime, leidos de su informe."""
    return sorted(set(l.strip()[1] for l in informe
                      if l.strip().startswith("(") and l.strip()[2:3] == ")"))


# --------------------------------------------------------------------------
# EL CASO `F` SE REFUNDO EN LA VUELTA 172, TAREA 4.a (adjudicacion 6.4 del acta
# 171). ANTES ERA: `F_el_reporte_170_del_repo_esta_archivado_y_calza`, que
# llamaba a `PASO0.exigir_archivado(170, ejecutar_archivador=False)` CONTRA EL
# ARBOL VIVO y esperaba True. Eso solo fue cierto durante los minutos entre
# archivar la 170 y pisar REPORTE.md con el esqueleto de la 171; despues es
# falso para siempre, y el arnes salia EXIT 1 con 9 de 10.
#
# CONTRA QUE REGLA IBA: la condicion de la vuelta 148, SUJETO CONGELADO, que la
# 6.10 del acta 170 confirmo con esas palabras. LA FRASE VIEJA NO SE BORRA DE LA
# HISTORIA: queda escrita aqui, que es donde se puede auditar.
#
# LA CIFRA QUE EL REPORTE DE LA 171 PUBLICO ("10 casos, 10 pasan, 10 caen") ERA
# CIERTA CUANDO SE CORRIO y no se retira. Lo que no se sostenia era el arnes.
# --------------------------------------------------------------------------
def prueba_de_mutacion():
    sys.stdout.reconfigure(encoding="utf-8")
    print("=" * 78)
    print("VUELTA 171, TAREA 5.a: CASO POSITIVO POR MUTACION DEL PASO 0 DEL ESQUELETO")
    print("=" * 78)
    print("")
    casos = []
    tmp = tempfile.mkdtemp(prefix="v171_paso0_")
    try:
        arch = os.path.join(tmp, "reportes")
        vivo = os.path.join(tmp, "REPORTE.md")

        print("A) (b) SIN ARCHIVO DEL REPORTE ANTERIOR, LA GUARDA TIENE QUE CAER")
        _escribir(vivo, _reporte_falso(170))
        ok, inf = PASO0.exigir_archivado(170, ruta_reporte=vivo, dir_archivo=arch,
                                         ejecutar_archivador=False)
        print("   ok=%r motivos=%s" % (ok, _motivos(inf)))
        casos.append(("A_sin_archivo_la_guarda_NO_deja_escribir", ok, False))
        casos.append(("A_y_el_motivo_es_la_b", _motivos(inf), ["b"]))
        print("")

        print("B) (c) EL ARCHIVO EXISTE PERO ES DE OTRA VUELTA: TIENE QUE CAER")
        _escribir(os.path.join(arch, "REPORTE_V170.md"), _reporte_falso(168))
        ok, inf = PASO0.exigir_archivado(170, ruta_reporte=vivo, dir_archivo=arch,
                                         ejecutar_archivador=False)
        print("   ok=%r motivos=%s" % (ok, _motivos(inf)))
        casos.append(("B_archivo_de_otra_vuelta_NO_deja_escribir", ok, False))
        casos.append(("B_y_los_motivos_son_c_y_d", _motivos(inf), ["c", "d"]))
        print("")

        print("C) (d) LA CLAUSULA QUE DE VERDAD MIRA LO QUE SE VA A DESTRUIR.")
        print("   El archivo es de la vuelta BUENA, pero al arbol le han crecido")
        print("   lineas despues de archivarlo: eso es texto que se perderia.")
        _escribir(os.path.join(arch, "REPORTE_V170.md"), _reporte_falso(170))
        _escribir(vivo, _reporte_falso(170, cola="\n## 9. LA SECCION QUE SE PERDERIA\n"))
        ok, inf = PASO0.exigir_archivado(170, ruta_reporte=vivo, dir_archivo=arch,
                                         ejecutar_archivador=False)
        print("   ok=%r motivos=%s" % (ok, _motivos(inf)))
        casos.append(("C_arbol_con_texto_sin_archivar_NO_deja_escribir", ok, False))
        casos.append(("C_y_el_motivo_es_la_d", _motivos(inf), ["d"]))
        print("")

        print("D) EL CASO VERDE: LOS DOS CALZAN Y LA GUARDA DEJA ESCRIBIR")
        _escribir(vivo, _reporte_falso(170))
        ok, inf = PASO0.exigir_archivado(170, ruta_reporte=vivo, dir_archivo=arch,
                                         ejecutar_archivador=False)
        print("   ok=%r motivos=%s" % (ok, _motivos(inf)))
        casos.append(("D_cuando_calzan_la_guarda_deja_escribir", ok, True))
        casos.append(("D_y_no_hay_ningun_motivo", _motivos(inf), []))
        print("")

        print("E) UN BYTE DE DIFERENCIA BASTA: LA GUARDA NO ES UN 'PARECIDO'")
        _escribir(vivo, _reporte_falso(170) + " ")
        ok, inf = PASO0.exigir_archivado(170, ruta_reporte=vivo, dir_archivo=arch,
                                         ejecutar_archivador=False)
        print("   ok=%r motivos=%s (un solo byte de mas en el arbol)"
              % (ok, _motivos(inf)))
        casos.append(("E_un_byte_de_mas_ya_la_tumba", ok, False))
        print("")

        print("F) EL CASO VERDE SOBRE UN SUJETO GRANDE Y CON FORMA DE REPORTE DE")
        print("   VERDAD, FABRICADO EN EL TEMPORAL. REFUNDADO EN LA VUELTA 172,")
        print("   TAREA 4.a: antes miraba EL ARBOL VIVO y por eso caducaba solo.")
        grande = _reporte_grande(170)
        print("   sujeto fabricado: %d bytes, %d saltos de linea"
              % (len(grande.encode("utf-8")), grande.count(chr(10))))
        _escribir(os.path.join(arch, "REPORTE_V170.md"), grande)
        _escribir(vivo, grande)
        ok, inf = PASO0.exigir_archivado(170, ruta_reporte=vivo, dir_archivo=arch,
                                         ejecutar_archivador=False)
        print("   F.1 los dos identicos -> ok=%r motivos=%s" % (ok, _motivos(inf)))
        casos.append(("F1_sujeto_grande_identico_deja_escribir", ok, True))
        casos.append(("F1_y_no_hay_ningun_motivo", _motivos(inf), []))

        medio = len(grande) // 2
        picado = grande[:medio] + ("X" if grande[medio] != "X" else "Y") + grande[medio + 1:]
        _escribir(vivo, picado)
        ok, inf = PASO0.exigir_archivado(170, ruta_reporte=vivo, dir_archivo=arch,
                                         ejecutar_archivador=False)
        print("   F.2 un byte cambiado EN MEDIO (posicion %d de %d) -> ok=%r motivos=%s"
              % (medio, len(grande), ok, _motivos(inf)))
        casos.append(("F2_un_byte_en_medio_tambien_la_tumba", ok, False))
        casos.append(("F2_y_el_motivo_es_la_d", _motivos(inf), ["d"]))
        casos.append(("F2_el_picado_mide_lo_mismo_que_el_bueno",
                      len(picado) == len(grande), True))

        _escribir(vivo, grande.replace(chr(10), chr(13) + chr(10)))
        ok, inf = PASO0.exigir_archivado(170, ruta_reporte=vivo, dir_archivo=arch,
                                         ejecutar_archivador=False)
        print("   F.3 el mismo texto con fin de linea de Windows -> ok=%r motivos=%s"
              % (ok, _motivos(inf)))
        casos.append(("F3_el_CRLF_no_la_tumba_porque_la_guarda_normaliza", ok, True))
        print("")
    finally:
        shutil.rmtree(tmp, ignore_errors=True)

    print("G) PASADA 1, LOS CASOS TAL CUAL")
    fallos = 0
    for nombre, real, esperado in casos:
        bien = (real == esperado)
        print("   %-52s %s   (real=%r esperado=%r)"
              % (nombre, "PASA" if bien else "FALLA", real, esperado))
        if not bien:
            fallos += 1
    print("   CIFRA casos: %d | pasan: %d | fallan: %d"
          % (len(casos), len(casos) - fallos, fallos))
    print("")

    print("H) PASADA 2, SE MUTA EL VALOR ESPERADO Y CADA CASO TIENE QUE CAER")
    caen = 0
    for nombre, real, esperado in casos:
        if isinstance(esperado, bool):
            mutado = not esperado
        elif isinstance(esperado, list):
            mutado = esperado + ["mutado"]
        else:
            mutado = str(esperado) + "_mutado"
        cae = (real != mutado)
        print("   %-52s %s   (esperado mutado=%r)"
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
    sys.exit(prueba_de_mutacion())
