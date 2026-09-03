# -*- coding: utf-8 -*-
"""vuelta157_tarea4c_tachar_tres_filas.py . TAREA 4.c DE LA VUELTA 157.

LAS TRES FILAS YA RECLASIFICADAS EN LA VUELTA 156 (`LD-OPC05-002`,
`LD-OPC05-040` y `LD-OPC05-097`) RECIBEN SU `~~C~~ D` EN LA CELDA DE CLASE DE
`docs/plan/LECTURAS_DIRIGIDAS.md`, que es la costumbre de la casa: no tapar lo
que se corrige.

SOLO SE CORRE DESPUES DE LA 4.a Y LA 4.b, y este script lo comprueba EL MISMO en
vez de fiarse del orden: si el lector de
`scripts/loop/vuelta152_registro_de_citas_opc05.py` no trae el patron
ensanchado, sale ROJO PREVIO y no toca una linea. Tachar antes de ensanchar
tumbaria Gate 0, que es exactamente lo que la vuelta 156 evito.

QUE CAMBIA Y QUE NO. Cambia LA CELDA DE CLASE, de `D` a `~~C~~ D`. NO cambia la
clase vigente, que sigue siendo D y que el lector nuevo lee de la ULTIMA clase
escrita: lo unico que pasa es que la C vieja vuelve a estar A LA VISTA. La razon
de cada fila, que ya declaraba la correccion en prosa, no se toca.

LA COMPROBACION SE HACE CORRIENDO EL LECTOR, NO MIRANDO EL TEXTO: antes y
despues de escribir, se cuenta lo que el lector recoge y se exige MISMO NUMERO
DE PARES, MISMAS CLAVES Y MISMAS CLASES. Si el tachado moviera una sola clase,
esto sale ROJO.

ES IDEMPOTENTE: una fila que ya venga tachada se deja igual y se dice.

USO:  python scripts/loop/vuelta157_tarea4c_tachar_tres_filas.py
"""
import importlib.util
import io
import os
import subprocess
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LECTOR = os.path.join(RAIZ, "scripts", "loop", "vuelta152_registro_de_citas_opc05.py")
LD = os.path.join(RAIZ, "docs", "plan", "LECTURAS_DIRIGIDAS.md")

# fila, par, clase vieja, clase vigente
TRES = [
    ("2", "actividades_clave <-> key_resources_hypothesis", "C", "D"),
    ("40", "cost_management_plan <-> stakeholder_register", "C", "D"),
    ("97", "juran_rcca_metodo <-> viaje_diagnostico_remedial", "C", "D"),
]


def cargar_lector():
    spec = importlib.util.spec_from_file_location("lector_opc05", LECTOR)
    mod = importlib.util.module_from_spec(spec)
    argv, salida = sys.argv, sys.stdout
    sys.argv = [LECTOR]
    sys.stdout = io.StringIO()
    try:
        spec.loader.exec_module(mod)
    finally:
        sys.argv, sys.stdout = argv, salida
    return mod


def main():
    print("=" * 78)
    print("VUELTA 157, TAREA 4.c: LAS TRES FILAS RECLASIFICADAS RECIBEN SU TACHADO")
    print("=" * 78)
    print("")

    mod = cargar_lector()
    if not hasattr(mod, "PATRON_FILA_LD"):
        print("ROJO PREVIO: el lector no trae el patron ensanchado de la TAREA 4.a.")
        print("FIN")
        return 1
    N = mod.cargar("WORK")
    r = mod.hacer_resolver(N)

    texto = io.open(LD, encoding="utf-8").read()
    antes = mod.citas_de_lectura_dirigida_de_texto(texto, r)
    print("  CIFRA pares que el lector recoge ANTES del tachado: %d" % len(antes))
    print("")

    nuevo = texto
    hechas, ya = 0, 0
    for fila, par, vieja, vigente in TRES:
        limpia = "| %s | REGISTRO DE CITAS `OP-C-05` | %s | %s |" % (fila, par, vigente)
        tachada = "| %s | REGISTRO DE CITAS `OP-C-05` | %s | ~~%s~~ %s |" % (
            fila, par, vieja, vigente)
        if tachada in nuevo:
            print("  fila %-3s LD-OPC05-%03d  YA ESTABA TACHADA" % (fila, int(fila)))
            ya += 1
            continue
        if limpia not in nuevo:
            print("ROJO PREVIO: la fila %s no viene con la celda limpia esperada." % fila)
            print("FIN")
            return 1
        nuevo = nuevo.replace(limpia, tachada, 1)
        print("  fila %-3s LD-OPC05-%03d  celda %r pasa a %r"
              % (fila, int(fila), vigente, "~~%s~~ %s" % (vieja, vigente)))
        hechas += 1

    if hechas:
        with io.open(LD, "w", encoding="utf-8", newline="\n") as fh:
            fh.write(nuevo)

    despues = mod.citas_de_lectura_dirigida_de_texto(
        io.open(LD, encoding="utf-8").read(), r)
    print("")
    print("  CIFRA pares que el lector recoge DESPUES del tachado: %d" % len(despues))
    mismas_claves = set(antes) == set(despues)
    movidas = sorted(k for k in antes if k in despues
                     and antes[k]["clase"] != despues[k]["clase"])
    print("  mismas claves: %s" % mismas_claves)
    print("  CIFRA clases movidas por el tachado: %d (%s)"
          % (len(movidas), ", ".join("%s <-> %s" % k for k in movidas) or "ninguna"))

    r2 = subprocess.run(["git", "diff", "--numstat", "--", "docs/plan/LECTURAS_DIRIGIDAS.md"],
                        cwd=RAIZ, capture_output=True)
    print("  numstat de docs/plan/LECTURAS_DIRIGIDAS.md: %s"
          % (r2.stdout.decode("utf-8", "replace").strip() or "(sin cambios)"))

    print("")
    print("CIFRA filas tachadas en esta corrida: %d" % hechas)
    print("CIFRA filas que ya venian tachadas: %d" % ya)
    bien = (len(antes) == len(despues)) and mismas_claves and not movidas
    if bien:
        print("")
        print("VERDE: el tachado deja la C vieja a la vista y el lector sigue leyendo los")
        print("mismos %d pares con las mismas clases." % len(despues))
        print("FIN")
        return 0
    print("")
    print("ROJO: el tachado movio lo que el lector recoge.")
    print("FIN")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
