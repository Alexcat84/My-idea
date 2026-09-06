# -*- coding: utf-8 -*-
r"""vuelta165_tarea7_escribir_reporte.py . ESCRIBE docs/loop/REPORTE.md DE LA
VUELTA 165.

LA CABECERA NO SE TECLEA: SE LEE (`EJECUTOR.md` 1, "LA CABECERA DEL REPORTE SE
TALLA, NO SE TECLEA"). El cuerpo del reporte vive en
`docs/loop/_v165_cuerpo_reporte.md` con el marcador literal `<<<CABECERA>>>`, y
este script lo sustituye por la tabla que
`scripts/loop/tallar_cabecera_reporte.py --fase04 --vuelta 165` imprimio en
`docs/loop/SALIDA_V165_T7_CABECERA.txt`. **Si esa salida no existe o no trae la
tabla, esto PARA y no escribe nada.**

Y COMPRUEBA LO QUE ESCRIBIO, en vez de fiarse: tras escribir corre
`tallar_cabecera_reporte.py --comparar docs/loop/REPORTE.md` y publica su
veredicto.

USO:  python scripts/loop/vuelta165_tarea7_escribir_reporte.py
"""
import io
import os
import re
import subprocess
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
CABECERA = os.path.join(RAIZ, "docs", "loop", "SALIDA_V165_T7_CABECERA.txt")
CUERPO = os.path.join(RAIZ, "docs", "loop", "_v165_cuerpo_reporte.md")
REPORTE = os.path.join(RAIZ, "docs", "loop", "REPORTE.md")
MARCA = "<<<CABECERA>>>"


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    print("=" * 78)
    print("VUELTA 165, TAREA 7: EL REPORTE, CON SU CABECERA LEIDA Y NO TECLEADA")
    print("=" * 78)
    print("")

    if not os.path.exists(CABECERA):
        print("PARADA: no existe %s. La cabecera no se teclea." % CABECERA)
        return 1
    texto = io.open(CABECERA, encoding="utf-8").read()
    m = re.search(r"(\| \| \*\*apertura\*\*.+?)\n\nFIN", texto, re.S)
    if not m:
        print("PARADA: la salida del tallador no trae la tabla. No se escribe nada.")
        return 1
    tabla = m.group(1).strip()
    filas = [l for l in tabla.split("\n") if l.startswith("|")]
    print("A) LA CABECERA, LEIDA DEL TALLADOR")
    print("   fichero: docs/loop/SALIDA_V165_T7_CABECERA.txt")
    print("   CIFRA filas leidas: %d" % len(filas))
    print("")

    if not os.path.exists(CUERPO):
        print("PARADA: no existe el cuerpo %s." % CUERPO)
        return 1
    cuerpo = io.open(CUERPO, encoding="utf-8").read()
    print("B) EL CUERPO")
    print("   fichero: docs/loop/_v165_cuerpo_reporte.md")
    print("   CIFRA veces que aparece la marca %s: %d"
          % (MARCA, cuerpo.count(MARCA)))
    if cuerpo.count(MARCA) != 1:
        print("   PARADA: la marca tiene que aparecer EXACTAMENTE una vez.")
        return 1
    print("")

    final = cuerpo.replace(MARCA, tabla)
    # CERO GUIONES LARGOS Y CERO GUIONES MEDIOS (EJECUTOR.md 10), comprobado
    # aqui y no confiado al hook.
    largos = final.count(chr(8212))
    medios = final.count(chr(8211))
    print("C) LA REGLA DE LOS GUIONES, COMPROBADA ANTES DE ESCRIBIR")
    print("   CIFRA guiones largos: %d" % largos)
    print("   CIFRA guiones medios: %d" % medios)
    if largos or medios:
        print("   PARADA: el reporte trae guiones prohibidos.")
        return 1
    print("")

    with io.open(REPORTE, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(final)
    print("D) ESCRITO")
    print("   docs/loop/REPORTE.md, %d lineas por count(NL), que calza con wc -l, y %d por len(split(NL)), %d bytes"
          % (final.count("\n"), len(final.split("\n")),
             len(final.encode("utf-8"))))
    print("")

    print("E) LA COMPROBACION, QUE NO SE FIA DE LO QUE ACABA DE ESCRIBIR")
    r = subprocess.run([sys.executable,
                        "scripts/loop/tallar_cabecera_reporte.py", "--fase04",
                        "--vuelta", "165", "--comparar", "docs/loop/REPORTE.md"],
                       cwd=RAIZ, capture_output=True)
    salida = (r.stdout.decode("utf-8", errors="replace")
              + r.stderr.decode("utf-8", errors="replace"))
    for l in salida.split("\n"):
        if l.strip():
            print("   %s" % l.rstrip())
    print("   EXITCODE del comparador: %d" % r.returncode)
    return r.returncode


if __name__ == "__main__":
    raise SystemExit(main())
