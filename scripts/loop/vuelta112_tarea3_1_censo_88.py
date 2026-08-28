# -*- coding: utf-8 -*-
r"""vuelta112_tarea3_1_censo_88.py . TAREA 3.1 de la vuelta 112 (encargo del
auditor, acta de la vuelta 111, seccion final "DONDE VA LA LECTURA").

RECUENTA, ANTES DE LEER NINGUN PAR: de las NO RESUELTA de hoy
(`contar_cierre_efectivo.cifras()`, campo `sin_dir`), cuantas traen YA una
`correccion_vNN` declarada sobre su fila (cualquier campo: alguien ya las
reabrio a proposito) y cuantas NO tienen ninguna correccion, o sea siguen
NO RESUELTA desde la lectura original y nadie las ha vuelto a abrir nunca.
De esas ultimas, reparto por dominio.

CIFRA DE CONTROL DEL ENCARGO (para contrastar, no para copiar): 109 NO
RESUELTA; 21 con correccion_vNN; 88 sin ninguna, repartidas quality 39,
core 32, environmental 8, franquicias 3, exportacion 3, health_safety 1,
risk_management 1, entrega 1.

USO: python scripts/loop/vuelta112_tarea3_1_censo_88.py
"""
import collections
import io
import json
import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(RAIZ, "scripts", "loop"))
import contar_cierre_efectivo as cce  # noqa: E402

CORREC_RE = re.compile(r"^correccion_v(\d+)$")


def cargar_filas_por_puesto(rutas):
    filas = {}
    for ruta in rutas:
        with io.open(ruta, encoding="utf-8") as f:
            for linea in f:
                if linea.strip():
                    d = json.loads(linea)
                    filas[d["puesto_tramo"]] = d
    return filas


def main():
    d, fallos = cce.cifras(cce.TRAMOS_OP_E_03_POR_DEFECTO)
    if fallos:
        print("ROJO:", fallos)
        return 1

    no_resuelta = sorted(d["sin_dir"])
    print("NO RESUELTA de hoy (contar_cierre_efectivo.cifras, sin_dir): %d" % len(no_resuelta))

    filas = cargar_filas_por_puesto(cce.TRAMOS_OP_E_03_POR_DEFECTO)

    con_correccion = []
    sin_correccion = []
    for p in no_resuelta:
        fila = filas[p]
        tiene = any(CORREC_RE.match(k) for k in fila)
        (con_correccion if tiene else sin_correccion).append(p)

    print("de esas, CON correccion_vNN declarada sobre su fila (reabiertas a proposito): %d -- %s"
          % (len(con_correccion), con_correccion))
    print("de esas, SIN ninguna correccion (NO RESUELTA desde la lectura original): %d"
          % len(sin_correccion))

    reparto = collections.Counter(filas[p]["dominio"] for p in sin_correccion)
    print()
    print("REPARTO POR DOMINIO de las %d sin reabrir:" % len(sin_correccion))
    for dominio, n in sorted(reparto.items(), key=lambda x: -x[1]):
        print("   %s %d" % (dominio, n))

    print()
    print("PUESTOS sin reabrir, ordenados: %s" % sin_correccion)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
