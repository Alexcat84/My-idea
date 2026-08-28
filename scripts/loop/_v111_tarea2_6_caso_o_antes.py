# -*- coding: utf-8 -*-
"""_v111_tarea2_6_caso_o_antes.py . TAREA 2.6 de la vuelta 111: paga la deuda
de la 1.2 (acta de la vuelta 110) midiendo de verdad el "antes" del caso O.

Corre verificar_vuelco_de_veredicto.py EN SU VERSION DE 55a48875 (la que
tenia el defecto de cruce, antes del arreglo de la vuelta 110) con
docs/loop/_auditor_v109_mut/tramo2_sin_decl_91.md puesto EN EL LUGAR de
SALIDA_V108_TAREA5_2_TRAMO2_TRES_VIAS.md (via overrides=), igual mecanica que
scripts/loop/vuelta109_tarea2_4_prueba_mutacion.py.

USO: python scripts/loop/_v111_tarea2_6_caso_o_antes.py
"""
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(RAIZ, "scripts", "loop"))
import _v111_verificar_vuelco_de_veredicto_55a48875 as m  # noqa: E402

RUTA_FIXTURE = os.path.join(RAIZ, "docs", "loop", "_auditor_v109_mut", "tramo2_sin_decl_91.md")


def main():
    overrides = {"SALIDA_V108_TAREA5_2_TRAMO2_TRES_VIAS.md": RUTA_FIXTURE}
    fallos, vuelcos = m.verificar(overrides=overrides)
    print("FALLOS:", fallos)
    print("VUELCOS DE VEREDICTO HALLADOS: %d" % len(vuelcos))
    for v in vuelcos:
        print("   %s: %s (%s, vuelta %s) -> %s (%s, vuelta %s) -- %s" % (
            v["puesto"], v["veredicto_viejo"], v["nombre_viejo"], v["vuelta_vieja"],
            v["veredicto_nuevo"], v["nombre_nuevo"], v["vuelta_nueva"],
            "DECLARADO" if v.get("declarado") else "MUDO"))
    mudos = [v for v in vuelcos if not v.get("declarado")]
    if mudos:
        print("\nROJO EXIT 1: %d vuelco(s) MUDO(s): %s" % (len(mudos), [v["puesto"] for v in mudos]))
        return 1
    print("\nVERDE: todos los vuelcos hallados estan declarados.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
