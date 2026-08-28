# -*- coding: utf-8 -*-
r"""vuelta110_tarea2_prueba_mutacion.py . PRUEBA DE MUTACION de la TAREA 2
(vuelta 110): el volteo en su sitio de verificar_vuelco_de_veredicto.py.

Corre `verificar(overrides=...)` sustituyendo, SOLO para la lectura de HOY,
docs/loop/SALIDA_V108_TAREA5_2_TRAMO2_TRES_VIAS.md por una de las dos copias
del auditor (docs/loop/_auditor_v109_mut/tramo2_sin_decl_87.md o
tramo2_sin_decl_91.md, ver acta de la vuelta 109, TAREA 2.4 y 2.5 del
encargo de la 110). La historia en git que lee `vuelcos_en_sitio()` SIGUE
siendo la del fichero real (los overrides no tocan git, solo el texto de
HOY que usan `leer_ficheros` y el contexto de declaracion).

USO:
  python scripts/loop/vuelta110_tarea2_prueba_mutacion.py 87
  python scripts/loop/vuelta110_tarea2_prueba_mutacion.py 91
"""
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOOP = os.path.join(RAIZ, "docs", "loop")
sys.path.insert(0, os.path.join(RAIZ, "scripts", "loop"))
import verificar_vuelco_de_veredicto as vvv  # noqa: E402


def main():
    caso = sys.argv[1] if len(sys.argv) > 1 else "87"
    nombre_mutado = "tramo2_sin_decl_%s.md" % caso
    ruta_mutada = os.path.join(LOOP, "_auditor_v109_mut", nombre_mutado)
    if not os.path.exists(ruta_mutada):
        print("ROJO: no existe %s" % ruta_mutada)
        return 1

    overrides = {"SALIDA_V108_TAREA5_2_TRAMO2_TRES_VIAS.md": ruta_mutada}
    fallos, vuelcos = vvv.verificar(overrides=overrides)
    if fallos:
        print("ROJO, %d cosa(s) no cuadran, NO SE CUENTA NADA:" % len(fallos))
        for x in fallos:
            print("   %s" % x)
        return 1

    print("MUTACION: SALIDA_V108_TAREA5_2_TRAMO2_TRES_VIAS.md sustituido por %s" % ruta_mutada)
    print("VUELCOS DE VEREDICTO HALLADOS: %d" % len(vuelcos))
    etiqueta_tipo = {"cruce": "CRUCE", "en_sitio": "EN SITIO", "oscilacion": "OSCILACION"}
    mudos = []
    for v in vuelcos:
        estado = "DECLARADO" if v["declarado"] else "MUDO"
        print("   %d [%s]: %s -> %s (%s) -- %s"
              % (v["puesto"], etiqueta_tipo[v["tipo"]], v["veredicto_viejo"], v["veredicto_nuevo"],
                 v["nombre_nuevo"], estado))
        if not v["declarado"]:
            mudos.append("%d[%s]" % (v["puesto"], v["tipo"]))

    if mudos:
        print("\nROJO: %d vuelco(s) MUDO(s), nombrados: %s" % (len(mudos), ", ".join(mudos)))
        return 1

    print("\nVERDE: todos los vuelcos hallados estan declarados.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
