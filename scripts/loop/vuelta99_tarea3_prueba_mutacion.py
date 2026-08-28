# -*- coding: utf-8 -*-
r"""vuelta99_tarea3_prueba_mutacion.py . VUELTA 99, TAREA 3: PRUEBA DE MUTACION
DE LAS GUARDAS DEL ESCRITOR DEL CUARTO TRAMO (EJECUTOR.md regla 1, EL CASO ROJO
SE PRUEBA POR MUTACION).

  C1  control: las 33 filas reales                         espera VERDE
  M1  una clase que no es A, B, C ni D                     espera ROJO
  M2  una razon vacia                                      espera ROJO
  M3  una razon sin ninguna cita del banco                  espera ROJO
  M4  un puesto fuera del rango 151 a 183                  espera ROJO
  M5  un puesto repetido dentro del tramo                  espera ROJO
  M6  una direccion con un id ajeno al par                 espera ROJO
  M7  una direccion sin la forma 'a -> b'                   espera ROJO

DECLARADO Y NO FABRICADO: la CLASE y la DIRECCION de cada una de las 33 filas
son lectura a mano contra el grafo, y no hay en el repo una segunda fuente
independiente contra la que contrastarlas; su control es la relectura ciega
del auditor. Estas mutaciones prueban EL ESCRITOR (que ninguna fila mal
formada pueda colarse), no las 33 lecturas en si.

USO:
  python scripts/loop/vuelta99_tarea3_prueba_mutacion.py
"""
import copy
import importlib.util
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOOP = os.path.join(RAIZ, "scripts", "loop")
sys.path.insert(0, LOOP)


def cargar(nombre):
    ruta = os.path.join(LOOP, nombre + ".py")
    spec = importlib.util.spec_from_file_location(nombre, ruta)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[nombre] = mod
    spec.loader.exec_module(mod)
    return mod


RESULTADOS = []


def caso(nombre, desc, esperado, fallos):
    obtenido = "ROJO" if fallos else "VERDE"
    ok = (esperado == obtenido)
    RESULTADOS.append((nombre, desc, esperado, obtenido, ok))
    print("  %-4s %-52s espera %-6s obtiene %-6s (%d fallo/s) %s"
          % (nombre, desc, esperado, obtenido, len(fallos), "OK" if ok else "FALLA"))


def main():
    esc = cargar("vuelta99_tarea3_escribir_tramo4")
    base = esc.FILAS
    p = 0  # indice de la primera fila (puesto 151)

    print("=" * 112)
    print("PRUEBA DE MUTACION, VUELTA 99 TAREA 3 (guardas del escritor del cuarto tramo)")
    print("=" * 112)
    print("FILAS DE PARTIDA: %d. NADA SE ESCRIBE: las mutaciones van sobre copias en memoria.")
    print()

    _, fallos = esc.construir(base)
    caso("C1", "control: las 33 filas reales", "VERDE", fallos)

    m = copy.deepcopy(base); m[p]["clase"] = "Z"
    _, fallos = esc.construir(m)
    caso("M1", "clase 'Z', que no es A, B, C ni D", "ROJO", fallos)

    m = copy.deepcopy(base); m[p]["razon"] = ""
    _, fallos = esc.construir(m)
    caso("M2", "razon vacia", "ROJO", fallos)

    m = copy.deepcopy(base)
    m[p]["razon"] = "Una razon larga sin una sola cita de ninguna regla del banco."
    _, fallos = esc.construir(m)
    caso("M3", "razon sin ninguna cita del banco", "ROJO", fallos)

    m = copy.deepcopy(base); m[p]["n"] = 999
    _, fallos = esc.construir(m)
    caso("M4", "puesto 999, fuera del rango 151 a 183", "ROJO", fallos)

    m = copy.deepcopy(base); m[p]["n"] = m[p + 1]["n"]
    _, fallos = esc.construir(m)
    caso("M5", "puesto repetido dentro del tramo", "ROJO", fallos)

    m = copy.deepcopy(base)
    ajeno = m[p + 1]["hijo"]
    m[p]["dir"] = "%s -> %s" % (m[p]["madre"], ajeno)
    _, fallos = esc.construir(m)
    caso("M6", "direccion con un id ajeno al par (la guarda clave)", "ROJO", fallos)

    m = copy.deepcopy(base); m[p]["dir"] = m[p]["madre"]
    _, fallos = esc.construir(m)
    caso("M7", "direccion sin la forma 'a -> b'", "ROJO", fallos)

    print()
    fallan = [r for r in RESULTADOS if not r[4]]
    mut = [r for r in RESULTADOS if r[0].startswith("M")]
    con = [r for r in RESULTADOS if r[0].startswith("C")]
    print("RECUENTO: casos totales %d, controles %d (verdes %d), mutaciones %d (caen %d), "
          "casos que FALLAN %d"
          % (len(RESULTADOS), len(con), sum(1 for r in con if r[4]),
             len(mut), sum(1 for r in mut if r[4]), len(fallan)))
    print()
    print("DECLARADO Y NO FABRICADO: la CLASE y la DIRECCION de cada una de las 33 filas son")
    print("lectura a mano contra el grafo y NO TIENEN CASO ROJO AUTOMATICO. Su control es la")
    print("relectura ciega del auditor. Estas mutaciones prueban EL ESCRITOR, no las lecturas.")
    if fallan:
        print("ROJO: %d caso(s) no se comportan como se espera." % len(fallan))
        return 1
    print("VERDE: el control pasa y las %d mutaciones caen." % len(mut))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
