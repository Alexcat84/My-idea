# -*- coding: utf-8 -*-
r"""_v215_verificar_cierre.py . LAS GUARDAS DEL CIERRE, RE CORRIDAS SOBRE EL
REPORTE YA ESCRITO Y CORREGIDO.

COMPUTO DE UNA VUELTA, prefijo de guion bajo (moratoria de AUDITOR.md 6.3).

POR QUE EXISTE, Y NO ES PARA DARME UN VERDE. cerrar_reporte.py escribio el
reporte y SALIO EN ROJO, con razon: su guarda de las dos convenciones conto
CUATRO cifras de bytes publicadas sin su pareja. Las cuatro se corrigieron por
sustitucion declarada y medida. PERO ESE INSTRUMENTO NO SE PUEDE VOLVER A
CORRER: su paso A exige que el reporte siga sin cerrar, y ya esta cerrado. Si me
quedara ahi, el reporte se publicaria con un ROJO sellado y sin nada que diga si
la causa de ese rojo sigue viva.

QUE HACE: IMPORTA las MISMAS funciones de cerrar_reporte.py, no las clona
(acta 206, adjudicacion 6.5), y las corre sobre el texto final. NO AFLOJA
NINGUNA: si alguna cae, esto sale en rojo.

USO:  python scripts/loop/_v215_verificar_cierre.py
"""
import io
import os
import re
import sys

NL = chr(10)
AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(os.path.dirname(AQUI))
REPORTE = os.path.join(RAIZ, "docs", "loop", "REPORTE.md")
VUELTA = int(re.search(r"_v(\d+)_", os.path.basename(os.path.abspath(__file__))).group(1))

sys.path.insert(0, AQUI)
import cerrar_reporte as C  # noqa: E402


def main():
    texto = io.open(REPORTE, encoding="utf-8").read().replace(chr(13) + NL, NL)
    fallos = 0
    print("=" * 78)
    print("LAS GUARDAS DEL CIERRE, RE CORRIDAS SOBRE EL REPORTE FINAL DE LA %d"
          % VUELTA)
    print("=" * 78)
    print("docs/loop/REPORTE.md: %d bytes, %d lineas"
          % (len(texto.encode("utf-8")), texto.count(NL)))
    print("")

    tall = io.open(os.path.join(RAIZ, "docs", "loop",
                                "SALIDA_V%d_TALLADOR_CABECERA.txt" % VUELTA),
                   encoding="utf-8").read().replace(chr(13) + NL, NL)
    filas_tall = [l for l in tall.split(NL) if l.strip().startswith("|")]
    bat = io.open(os.path.join(RAIZ, "docs", "loop", "SALIDA_V183_BATERIA.txt"),
                  encoding="utf-8").read().replace(chr(13) + NL, NL)
    lineas_bat = [l for l in bat.split(NL) if l.strip()]
    # LA EVIDENCIA SE COMPUTA COMO LA COMPUTA main(), CON LA VUELTA DEL FICHERO
    # (la 183, que es la que el lanzador pone en el nombre) Y NO CON LA MIA, y
    # se queda con los tramos cuyo asunto de commit dice ESTA vuelta.
    reparto = C.tramos_por_vuelta(183)
    sellados = sorted(n for n, v in reparto.items() if v == VUELTA)
    print("CIFRA tramos de la bateria con fichero en disco: %d" % len(reparto))
    print("CIFRA tramos sellados EN LA VUELTA %d: %d %s"
          % (VUELTA, len(sellados), sellados))
    for n in sorted(reparto):
        print("   tramo %-3d -> vuelta %s" % (n, reparto[n]))
    print("")

    print("(A) LAS CUATRO PIEZAS, CON piezas_que_faltan() DE cerrar_reporte.py")
    faltan = C.piezas_que_faltan(texto, filas_tall, lineas_bat, VUELTA,
                                 "docs/loop/SALIDA_V183_BATERIA.txt", sellados)
    print("CIFRA piezas que faltan: %d" % len(faltan))
    for f in faltan:
        print("   FALTA> %s" % f)
    if faltan:
        fallos += 1
    print("")

    print("(B) LAS CIFRAS SIN PAREJA, CON cifras_sin_pareja() DE cerrar_reporte.py")
    huerfanas = C.cifras_sin_pareja(texto)
    print("CIFRA cifras publicadas sin su pareja: %d (se exigen 0)"
          % len(huerfanas))
    for n, especie, muestra, linea in huerfanas:
        print("   HUERFANA> linea %d, %s, %s: %s" % (n, especie, muestra, linea))
    if huerfanas:
        fallos += 1
    print("")

    print("(C) LAS SECCIONES, CON secciones_del_reporte() DE cerrar_reporte.py")
    sec = C.secciones_del_reporte(texto)
    ausentes = [k for k in range(3, 10) if k not in sec]
    dup = sorted(k for k, v in sec.items() if len(v) > 1)
    desorden = C.secciones_fuera_de_orden(sec)
    print("CIFRA secciones halladas: %d %s" % (len(sec), sorted(sec)))
    print("CIFRA secciones de la 3 a la 9 AUSENTES: %d %s" % (len(ausentes), ausentes))
    print("CIFRA secciones DUPLICADAS: %d %s" % (len(dup), dup))
    print("CIFRA secciones FUERA DE ORDEN: %d" % len(desorden))
    if ausentes or dup or desorden:
        fallos += 1
    print("")

    print("(D) LOS GUIONES Y EL VEREDICTO")
    print("CIFRA guiones largos: %d | CIFRA guiones medios: %d"
          % (texto.count(chr(8212)), texto.count(chr(8211))))
    if texto.count(chr(8212)) or texto.count(chr(8211)):
        fallos += 1
    sin_escribir = C.VEREDICTO_VIEJO in texto
    print("CIFRA el reporte AUN dice SIN ESCRIBIR TODAVIA: %s (se exige NO)"
          % ("SI" if sin_escribir else "NO"))
    if sin_escribir:
        fallos += 1
    hueco = C.HUECO_CABECERA in texto
    print("CIFRA el hueco de la cabecera sigue sin rellenar: %s (se exige NO)"
          % ("SI" if hueco else "NO"))
    if hueco:
        fallos += 1
    print("")

    print("CIFRA comprobaciones que fallan: %d" % fallos)
    if fallos:
        print("ROJO: el reporte NO cierra limpio.")
        return 1
    print("VERDE: las cuatro piezas estan, no queda ni una cifra sin su pareja, "
          "las secciones 3 a 9 estan unicas y en orden, y el veredicto esta "
          "escrito.")
    return 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.exit(main())
