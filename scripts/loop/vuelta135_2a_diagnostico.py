# -*- coding: utf-8 -*-
"""vuelta135_2a_diagnostico.py . TAREA 2.a de la vuelta 135: mide el TAMANO
DE LA PUERTA DE SERVICIO que la exencion (iii) de verificar_cifras_del_reporte.py
deja abierta hoy, ANTES de tocar una linea de ese fichero (acta 134, 4.1).

Contra docs/loop/REPORTE.md TAL COMO ESTA EN EL ARBOL AL ABRIR esta vuelta
(el reporte real de la vuelta 134, sin reescribir), escribe:
  (1) la linea COBERTURA tal cual la imprime la guarda hoy;
  (2) la lista de las exentas por "(sin instrumento)", una por una;
  (3) por cada una de esas exentas, si en su ventana de tres frases HAY o NO
      HAY citado un SALIDA_V134_*.txt (regex PATRON_CITA_SALIDA de la propia
      guarda, sin filtrar por existencia en disco: lo que importa aqui es si
      el TEXTO cita un fichero, que es lo que decide la exencion (iii)
      vigente), con el nombre del fichero cuando lo haya.

No modifica verificar_cifras_del_reporte.py: reusa sus funciones internas
(EJECUTOR.md 2, "el instrumento manda").

USO:
  python scripts/loop/vuelta135_2a_diagnostico.py
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import verificar_cifras_del_reporte as v  # noqa: E402


def diagnosticar(ruta_reporte):
    fallos, cotejados, exentas, total_cifras = v.verificar(ruta_reporte)
    cobertura = "COBERTURA: %d cotejadas / %d exentas / %d cifras" % (
        len(cotejados), len(exentas), total_cifras)

    texto_completo = v.leer(ruta_reporte)
    texto = v.quitar_bloques_cubiertos(texto_completo)
    frases = v.dividir_frases(texto)

    detalle = []
    for numero, unidad, frase_exenta in exentas:
        # localizar el indice de la frase exacta para poder tomar su ventana
        idx = None
        for i, fr in enumerate(frases):
            if fr.strip() == frase_exenta:
                idx = i
                break
        if idx is None:
            # busqueda por contencion, por si dividir_frases normalizo espacios
            for i, fr in enumerate(frases):
                if frase_exenta[:40] in fr:
                    idx = i
                    break
        ventana = frases[idx:idx + 3] if idx is not None else [frase_exenta]
        ventana_txt = " ".join(ventana)
        citas = sorted(set(v.PATRON_CITA_SALIDA.findall(ventana_txt)))
        detalle.append((numero, unidad, frase_exenta, citas))
    return cobertura, detalle, fallos


def main():
    ruta = v.RUTA_REPORTE
    cobertura, detalle, fallos = diagnosticar(ruta)

    print("DIAGNOSTICO 2.a contra %s (REPORTE de la vuelta 134, arbol al abrir la 135):" % ruta)
    print(cobertura)
    print("")
    print("exentas por (sin instrumento), una por una (%d):" % len(detalle))
    for numero, unidad, frase, citas in detalle:
        if citas:
            print("  %d %s: SI hay SALIDA_V134_*.txt citado en su ventana: %s" %
                  (numero, unidad, ", ".join(citas)))
        else:
            print("  %d %s: NO hay ningun SALIDA_V134_*.txt citado en su ventana" %
                  (numero, unidad))
        print("    frase: %r" % frase)
    print("")
    print("EXITCODE: 0")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
