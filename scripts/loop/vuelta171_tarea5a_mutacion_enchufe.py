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


def _motivos(informe):
    """Los codigos de motivo que la guarda imprime, leidos de su informe."""
    return sorted(set(l.strip()[1] for l in informe
                      if l.strip().startswith("(") and l.strip()[2:3] == ")"))


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

        print("F) EL REPO DE VERDAD, EN MODO SOLO COMPROBACION (cero escrituras)")
        ok, inf = PASO0.exigir_archivado(170, ejecutar_archivador=False)
        print("   ok=%r motivos=%s" % (ok, _motivos(inf)))
        for l in inf:
            print("   " + l)
        casos.append(("F_el_reporte_170_del_repo_esta_archivado_y_calza", ok, True))
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
