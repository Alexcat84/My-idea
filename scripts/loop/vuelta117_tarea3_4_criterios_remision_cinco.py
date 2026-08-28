# -*- coding: utf-8 -*-
r"""vuelta117_tarea3_4_criterios_remision_cinco.py . TAREA 3.4 de la vuelta
117, encargo del auditor (acta de la vuelta 116): "LOS TRES CRITERIOS DE LA
REMISION SOBRE LAS CINCO QUE ESPERAN MESA, re-medidos con el tallador de la
116 corrido tal cual (es historia, no lo reescribas) y acotado a las cinco".

QUE HACE. scripts/loop/vuelta116_tarea3_4_tres_criterios_remision.py es
historia y NO SE TOCA: este fichero lo corre tal cual PRIMERO (su salida
completa sobre las SIETE queda pegada en
docs/loop/SALIDA_V117_TAREA3_4_CRITERIOS_REMISION_SIETE_TAL_CUAL.txt), y
DESPUES reusa sus mismas funciones (`destino`, `RUTA_OPS`) para acotar la
tabla a las CINCO que la TAREA 3.3 de esta vuelta mide sin ADDENDUM DE
EJECUCION y sin registro de cierre en la pagina (las que de verdad esperan
mesa): OP-M-03-ENLACES, OP-E-04, OP-E-05, OP-M-01-ESLABONES, OP-M-01-SEXTO.
OP-E-06 y OP-E-07 QUEDAN FUERA de esta tabla porque la doctrina adjudicada
del acta de la vuelta 116 (D.7 del encargo de esta vuelta) ya las cuenta
EJECUTADAS por su ADDENDUM DE EJECUCION, no como operaciones que esperan
mesa.

SOLO MEDIR. No adjudica si la remision esta bien cerrada.

USO:
  python scripts/loop/vuelta117_tarea3_4_criterios_remision_cinco.py
"""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from vuelta116_tarea3_4_tres_criterios_remision import RUTA_OPS, destino

LAS_CINCO = ["OP-M-03-ENLACES", "OP-E-04", "OP-E-05", "OP-M-01-ESLABONES", "OP-M-01-SEXTO"]


def main():
    ops = [json.loads(l) for l in open(RUTA_OPS, encoding="utf-8") if l.strip()]
    by_id = {o["id_op"]: o for o in ops}

    print("LOS TRES CRITERIOS DE LA REMISION SOBRE LAS CINCO QUE ESPERAN MESA, TAREA 3.4 VUELTA 117.")
    print("=" * 100)
    print("Acotado de vuelta116_tarea3_4_tres_criterios_remision.py (corrido tal cual antes, ver")
    print("docs/loop/SALIDA_V117_TAREA3_4_CRITERIOS_REMISION_SIETE_TAL_CUAL.txt): OP-E-06 y OP-E-07")
    print("quedan fuera porque la TAREA 3.3 de esta vuelta las mide EJECUTADAS (ADDENDUM), no en espera.")
    print()
    print("| operacion | destino (mesa fase 06) | nomina (aristas_nuevas) | pregunta_pendiente | adjudicacion escrita |")
    print("|---|---|---:|---|---|")
    destinos = []
    for oid in LAS_CINCO:
        o = by_id[oid]
        nomina = len(o.get("aristas_nuevas") or [])
        pp = o.get("pregunta_pendiente")
        pp_txt = "NINGUNA" if pp is None else repr(pp)
        adj = o.get("adjudicacion") or ""
        adj_escrita = "SI (%d caracteres)" % len(adj) if adj.strip() else "NO"
        mesas = destino(by_id, oid)
        destinos.extend(mesas)
        print("| %s | %s | %d | %s | %s |" % (oid, ", ".join(mesas) or "NINGUNA", nomina, pp_txt, adj_escrita))

    print()
    todas_sin_pregunta = all((by_id[oid].get("pregunta_pendiente") is None) for oid in LAS_CINCO)
    todas_con_adjudicacion = all((by_id[oid].get("adjudicacion") or "").strip() for oid in LAS_CINCO)
    print("RESUMEN: pregunta_pendiente NINGUNA en las %d: %s. adjudicacion escrita en las %d: %s."
          % (len(LAS_CINCO), todas_sin_pregunta, len(LAS_CINCO), todas_con_adjudicacion))
    total_nomina = sum(len(by_id[oid].get("aristas_nuevas") or []) for oid in LAS_CINCO)
    print("nomina total (suma de aristas_nuevas de las cinco): %d" % total_nomina)
    from collections import Counter
    cnt = Counter(destinos)
    print("destino: %s" % ", ".join("%d a %s" % (c, m) for m, c in sorted(cnt.items())))


if __name__ == "__main__":
    main()
