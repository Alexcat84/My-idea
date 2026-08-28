# -*- coding: utf-8 -*-
r"""vuelta110_tarea4_caso_construccion.py . CASO POSITIVO POR CONSTRUCCION de
la TAREA 4 (vuelta 110): la rama muda de verificar_vuelco_de_veredicto.py
(el "primero y el ultimo coinciden pero algo intermedio distinto") deja de
hacer `continue` en silencio y pasa a imprimirse como 'oscilacion', con la
misma exigencia de declaracion que un vuelco normal.

Hoy esa rama no es alcanzable con los ficheros reales (cero puestos
aparecen en tres o mas ficheros de FICHEROS_VEREDICTO): se fabrica la
situacion sobre TRES COPIAS de ficheros reales
(docs/loop/_v110_tarea4_construccion/{v105,v106,v107_tramo3}_con_9001.*),
cada una con un bloque o fila anadida para un puesto que NO EXISTE en el
grafo (9001), con veredictos A (OBJETO, V105), B (SATELITE, V106), A
(OBJETO, V107 tramo3, HOY): el patron A, B, A que la rama muda existe para
cazar.

USO:
  python scripts/loop/vuelta110_tarea4_caso_construccion.py
"""
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOOP = os.path.join(RAIZ, "docs", "loop")
CONSTRUCCION = os.path.join(LOOP, "_v110_tarea4_construccion")
sys.path.insert(0, os.path.join(RAIZ, "scripts", "loop"))
import verificar_vuelco_de_veredicto as vvv  # noqa: E402


def main():
    overrides = {
        "SALIDA_V105_TAREA4_3_RE_BARRIDO.txt": os.path.join(CONSTRUCCION, "v105_con_9001.txt"),
        "SALIDA_V106_TAREA4_3_TRES_VIAS.txt": os.path.join(CONSTRUCCION, "v106_con_9001.txt"),
        "SALIDA_V107_TAREA4_3_TRAMO3_TRES_VIAS.md": os.path.join(CONSTRUCCION, "v107_tramo3_con_9001.md"),
    }
    fallos, vuelcos = vvv.verificar(overrides=overrides)
    if fallos:
        print("ROJO, %d cosa(s) no cuadran:" % len(fallos))
        for x in fallos:
            print("   %s" % x)
        return 1

    print("MUTACION: tres ficheros sustituidos por copias con el puesto 9001 fabricado "
          "(OBJETO en V105, SATELITE en V106, OBJETO en V107-tramo3=HOY).")
    oscilaciones = [v for v in vuelcos if v["tipo"] == "oscilacion"]
    print("VUELCOS TOTALES: %d, de los cuales OSCILACION: %d" % (len(vuelcos), len(oscilaciones)))
    for v in vuelcos:
        estado = "DECLARADO" if v["declarado"] else "MUDO"
        print("   %d [%s]: %s (%s) -> %s (%s) -- %s"
              % (v["puesto"], v["tipo"].upper(), v["veredicto_viejo"], v["nombre_viejo"],
                 v["veredicto_nuevo"], v["nombre_nuevo"], estado))

    ok_9001 = any(v["puesto"] == 9001 and v["tipo"] == "oscilacion" for v in vuelcos)
    if not ok_9001:
        print("\nROJO: el puesto 9001 fabricado NO aparece como oscilacion: la rama sigue muda.")
        return 1
    print("\nVERDE: la rama OSCILACION se disparo e imprimio el puesto 9001, con declaracion exigida.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
