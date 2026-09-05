# -*- coding: utf-8 -*-
r"""vuelta179_tarea3_mutacion_triangulos.py . EL CASO POSITIVO POR MUTACION DE
LA CIFRA PARTIDA POR SU FUENTE (vuelta 179, TAREA 3).

QUE PRUEBA. Las cuatro funciones PURAS que la vuelta 179 anade a
`vuelta178_tarea3_anotar_triangulos.py`: `lados_de_fuera_del_archivo()`,
`recomputable_entero_del_archivo()`, `el_lado_de_fuera_es_el_D()` y
`reparto_por_fuente()`.

NADA SALE DEL REPO. Los triangulos de este arnes son FABRICADOS: no se lee
`docs/INTRA_DOMINIO_VEREDICTOS.jsonl`, ni `docs/plan/OP_L_03_TRIANGULOS.jsonl`,
ni `docs/plan/OP_L_03_LECTURAS.jsonl`, ni el grafo. El modulo se importa por su
nombre y sus funciones puras se llaman con diccionarios de mentira.

EL CASO QUE LO DECIDE TODO, Y ES EL QUE EL ENCARGO NOMBRA: un triangulo con sus
TRES lados en el archivo y otro con el `D` FUERA tienen que caer en CASILLAS
DISTINTAS, y mutar el esperado tiene que tumbar el caso.

LA MUTACION (`EJECUTOR.md` 1, EL CASO ROJO SE PRUEBA POR MUTACION): de cada caso
se mueve EL VALOR ESPERADO y se comprueba que el caso CAE. Un `assert` que
compara un literal consigo mismo no puede fallar nunca.

USO:
  python scripts/loop/vuelta179_tarea3_mutacion_triangulos.py
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import importlib   # noqa: E402

T3 = importlib.import_module("vuelta178_tarea3_anotar_triangulos")

ARCHIVO = "docs/INTRA_DOMINIO_VEREDICTOS.jsonl"
REGISTRO = "docs/plan/OP_L_03_LECTURAS.jsonl (vuelta 177)"


def lado(x, y, clase, fuente):
    return {"lado": [x, y], "clase": clase, "fuente_de_la_clase": fuente}


# ---------------------------------------------------------------- LOS SUJETOS
# ENTERO: los tres lados del archivo. Es el que tiene que salir recomputable.
ENTERO = {"acto": "acto_entero", "terna": ["a", "b", "c"], "lados": [
    lado("a", "b", "A", ARCHIVO),
    lado("a", "c", "A", ARCHIVO),
    lado("b", "c", "D", ARCHIVO),
]}

# CON EL D FUERA: los dos `A` estan en el archivo y el `D`, que es el lado que
# hace que el triangulo sea un triangulo, viene del registro de la 177.
CON_D_FUERA = {"acto": "acto_con_d_fuera", "terna": ["d", "e", "f"], "lados": [
    lado("d", "e", "A", ARCHIVO),
    lado("d", "f", "A", ARCHIVO),
    lado("e", "f", "D", REGISTRO),
]}

# CON UN `A` FUERA: se apoya en un lado de fuera, pero NO es el `D`. Tiene que
# caer en una casilla distinta de la anterior, que es la mitad del encargo que
# se olvida cuando solo se prueba el caso llamativo.
CON_A_FUERA = {"acto": "acto_con_a_fuera", "terna": ["g", "h", "i"], "lados": [
    lado("g", "h", "A", REGISTRO),
    lado("g", "i", "A", ARCHIVO),
    lado("h", "i", "D", ARCHIVO),
]}

# CON LOS TRES FUERA: el caso extremo, para que la cuenta de lados por fuente no
# se apoye en que siempre haya al menos uno del archivo.
TODO_FUERA = {"acto": "acto_todo_fuera", "terna": ["j", "k", "l"], "lados": [
    lado("j", "k", "A", REGISTRO),
    lado("j", "l", "A", REGISTRO),
    lado("k", "l", "D", REGISTRO),
]}

TODOS = [ENTERO, CON_D_FUERA, CON_A_FUERA, TODO_FUERA]


CASOS = [
    # EL CASO QUE LO DECIDE TODO: casillas distintas.
    ("A_el_entero_ES_recomputable",
     lambda: T3.recomputable_entero_del_archivo(ENTERO), True),
    ("A_el_del_D_fuera_NO_es_recomputable",
     lambda: T3.recomputable_entero_del_archivo(CON_D_FUERA), False),
    ("A_Y_CAEN_EN_CASILLAS_DISTINTAS",
     lambda: (T3.recomputable_entero_del_archivo(ENTERO),
              T3.recomputable_entero_del_archivo(CON_D_FUERA)), (True, False)),
    ("B_el_del_D_fuera_tiene_el_D_fuera",
     lambda: T3.el_lado_de_fuera_es_el_D(CON_D_FUERA), True),
    ("B_el_del_A_fuera_NO_tiene_el_D_fuera",
     lambda: T3.el_lado_de_fuera_es_el_D(CON_A_FUERA), False),
    ("B_Y_LOS_DOS_APOYADOS_CAEN_EN_CASILLAS_DISTINTAS",
     lambda: (T3.el_lado_de_fuera_es_el_D(CON_D_FUERA),
              T3.el_lado_de_fuera_es_el_D(CON_A_FUERA)), (True, False)),
    ("C_el_entero_no_tiene_ningun_lado_de_fuera",
     lambda: len(T3.lados_de_fuera_del_archivo(ENTERO)), 0),
    ("C_el_del_D_fuera_tiene_UNO",
     lambda: len(T3.lados_de_fuera_del_archivo(CON_D_FUERA)), 1),
    ("C_el_de_todo_fuera_tiene_TRES",
     lambda: len(T3.lados_de_fuera_del_archivo(TODO_FUERA)), 3),
    ("C_y_el_lado_de_fuera_se_nombra_con_su_clase",
     lambda: T3.lados_de_fuera_del_archivo(CON_D_FUERA)[0][1], "D"),
    ("D_el_reparto_cuenta_el_total",
     lambda: T3.reparto_por_fuente(TODOS)["total"], 4),
    ("D_el_reparto_cuenta_los_enteros",
     lambda: len(T3.reparto_por_fuente(TODOS)["enteros"]), 1),
    ("D_el_reparto_cuenta_los_apoyados",
     lambda: len(T3.reparto_por_fuente(TODOS)["apoyados"]), 3),
    ("D_el_reparto_cuenta_los_del_D_fuera",
     lambda: len(T3.reparto_por_fuente(TODOS)["con_d_fuera"]), 2),
    ("D_LA_RESTA_CIERRA_enteros_mas_apoyados_es_el_total",
     lambda: (len(T3.reparto_por_fuente(TODOS)["enteros"])
              + len(T3.reparto_por_fuente(TODOS)["apoyados"])
              == T3.reparto_por_fuente(TODOS)["total"]), True),
    ("E_los_lados_del_archivo_se_cuentan",
     lambda: T3.reparto_por_fuente(TODOS)["lados_por_fuente"][ARCHIVO], 7),
    ("E_los_lados_del_registro_177_se_cuentan",
     lambda: T3.reparto_por_fuente(TODOS)["lados_por_fuente"][REGISTRO], 5),
    ("E_y_los_dos_suman_los_lados_de_los_cuatro_triangulos",
     lambda: sum(T3.reparto_por_fuente(TODOS)["lados_por_fuente"].values()), 12),
    ("F_un_lado_SIN_fuente_no_cuenta_como_del_archivo",
     lambda: T3.recomputable_entero_del_archivo(
         {"acto": "x", "terna": ["m", "n", "o"], "lados": [
             lado("m", "n", "A", ARCHIVO), lado("m", "o", "A", ARCHIVO),
             {"lado": ["n", "o"], "clase": "D"}]}), False),
    ("G_una_lista_vacia_de_triangulos_no_revienta",
     lambda: T3.reparto_por_fuente([])["total"], 0),
]


def main():
    print("=" * 78)
    print("CASO POSITIVO POR MUTACION: LA CIFRA PARTIDA POR SU FUENTE (179, T3)")
    print("=" * 78)
    print("")
    print("NADA SALE DEL REPO: los cuatro triangulos son fabricados y las funciones")
    print("juzgadas son PURAS. No se lee el archivo de veredictos, ni el registro de")
    print("OP-L-03, ni el registro de triangulos, ni el grafo.")
    print("")

    print("A) LOS CASOS, CORRIDOS")
    fallan = 0
    for nombre, fn, esperado in CASOS:
        try:
            visto = fn()
        except Exception as e:
            visto = "EXCEPCION %r" % (e,)
        ok = visto == esperado
        if not ok:
            fallan += 1
        print("   %-54s %s  visto=%r esperado=%r"
              % (nombre[:54], "pasa " if ok else "FALLA", visto, esperado))
    print("   CIFRA casos: %d | pasan: %d | fallan: %d"
          % (len(CASOS), len(CASOS) - fallan, fallan))
    print("")

    print("B) LA MUTACION: A CADA CASO SE LE MUEVE EL VALOR ESPERADO Y TIENE QUE CAER")
    caen = 0
    for nombre, fn, esperado in CASOS:
        if isinstance(esperado, bool):
            mutado = not esperado
        elif isinstance(esperado, int):
            mutado = esperado + 1
        elif isinstance(esperado, tuple):
            mutado = tuple(list(esperado)[::-1])
        else:
            mutado = str(esperado) + "_MUTADO"
        try:
            visto = fn()
        except Exception as e:
            visto = "EXCEPCION %r" % (e,)
        cae = visto != mutado
        if cae:
            caen += 1
        print("   %-54s %s" % (nombre[:54], "CAE" if cae else "NO CAE, Y ESO ES ROJO"))
    print("   CIFRA casos que CAEN: %d de %d" % (caen, len(CASOS)))
    print("")

    if fallan or caen != len(CASOS):
        print("ROJO DE LA MUTACION: %d caso(s) fallan y %d de %d caen."
              % (fallan, caen, len(CASOS)))
        return 1
    print("VERDE DE LA MUTACION: %d casos, los %d pasan y los %d CAEN al mutarles "
          "el valor esperado. Un triangulo con sus tres lados en el archivo y otro "
          "con el `D` fuera caen en casillas distintas; los dos apoyados, el del "
          "`D` fuera y el de un `A` fuera, tambien caen en casillas distintas; la "
          "resta de enteros mas apoyados cierra contra el total; los lados se "
          "cuentan por fuente; y un lado sin fuente NO cuenta como del archivo."
          % (len(CASOS), len(CASOS), len(CASOS)))
    return 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.exit(main())
