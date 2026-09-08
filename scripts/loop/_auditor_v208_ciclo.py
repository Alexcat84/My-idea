# -*- coding: utf-8 -*-
r"""_auditor_v208_ciclo.py . EL CICLO ENTERO DE GATE 0, CORRIDO POR EL AUDITOR DE
LA VUELTA 208. NUNCA `run_phase1.py` A SECAS: LOS OCHO COMANDOS EN SU ORDEN.

COMPUTO DE UNA VUELTA, prefijo de guion bajo: fuera del censo, fuera de la nomina
(congelada en 135 por `AUDITOR.md` 6.3), no vigila nada y muere con la vuelta.
NO ROZA LA MORATORIA (acta 199 `4.5`, acta 203 `4.6`, acta 205 `4.1`, acta 207).

NO ES UN CLON: IMPORTA `_v205_ciclo_gate0.py`, que es el fichero que tiene los
ocho comandos en su orden, y lo unico que le cambia es DONDE ESCRIBE.
**IMPORTAR NO ES CLONAR**, adjudicado como letra general por el acta 206 `6.5`.

POR QUE HAY QUE CAMBIARLE DONDE ESCRIBE: `escribir()` del fichero importado
apunta a `SALIDA_V<vuelta>_<seg>_<lado>.txt`, que son LOS FICHEROS QUE EL
EJECUTOR YA SELLO EN ESTA MISMA VUELTA. Correrlo tal cual los PISARIA, y el
auditor destruiria la evidencia que viene a verificar (acta 206 `7.3`).

USO:  python scripts/loop/_auditor_v208_ciclo.py
"""
import io
import os
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)

import _v205_ciclo_gate0 as C   # noqa: E402

C.VUELTA = 208


def escribir_del_auditor(seg, lado, texto):
    """LA UNICA LINEA QUE LE CAMBIO AL FICHERO IMPORTADO. Misma firma que la
    suya, para que el resto de su `main()` no note nada."""
    ruta = os.path.join(C.LOOP, "SALIDA_V208_%s_%s_AUDITOR.txt" % (seg, lado))
    io.open(ruta, "w", encoding="utf-8", newline=C.NL).write(texto)
    return os.path.getsize(ruta)


C.escribir = escribir_del_auditor

if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    print("=" * 74)
    print("CICLO ENTERO DE GATE 0, CORRIDO POR EL AUDITOR DE LA VUELTA 208")
    print("=" * 74)
    print("  IMPORTADO, NO CLONADO: %s" % os.path.basename(C.__file__))
    print("  SEDE DE MIS SALIDAS: docs/loop/SALIDA_V208_<seg>_<lado>_AUDITOR.txt")
    print("  (las del ejecutor NO se tocan: por eso se le cambia `escribir`)")
    sys.argv = [sys.argv[0], "CIERRE"]
    raise SystemExit(C.main())
