# -*- coding: utf-8 -*-
r"""vuelta162_tarea5_orden_y_muro.py . TAREA 5 de la vuelta 162.

SIGUE EL ORDEN ESCRITO EN MODO CONTINUO HASTA EL MURO CONOCIDO Y YA ADJUDICADO
(acta 149, seccion 3.10). NO CIERRA NINGUNA FASE Y NO TOCA NINGUN NODO.

POR QUE UN INSTRUMENTO NUEVO Y NO EL DE LA VUELTA 161, Y SE DICE EN VEZ DE
CALLARSE: `scripts/loop/vuelta161_tarea3_orden_y_muro.py` sigue corriendo y sus
secciones A, B y C siguen siendo correctas, POR ESO SE IMPORTAN Y NO SE COPIAN
(ley de una sola fuente). Lo que ya NO es correcto es su seccion D, que lleva
ESCRITO A MANO que `OP-D-02` es la unica operacion fuera de la fase 03 sin
cumplir con vara que mide: la TAREA 2.b de esta vuelta la puso CUMPLIDA por la
adjudicacion 6.4 del acta 161, y esa prosa quedo rancia el mismo dia. Aqui la
seccion D SE COMPUTA de la tabla en vez de teclearse, que es el remedio de la
especie.

USO:  python scripts/loop/vuelta162_tarea5_orden_y_muro.py
"""
import io
import json
import os
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import vuelta161_tarea3_orden_y_muro as V161   # noqa: E402

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

RAIZ = V161.RAIZ
ACTA = V161.ACTA
LINEA_ACTA_149 = V161.LINEA_ACTA_149
OPERACIONES = V161.OPERACIONES


def main():
    print("=" * 78)
    print("VUELTA 162, TAREA 5: EL ORDEN ESCRITO, RECORRIDO HASTA EL MURO")
    print("=" * 78)
    print("")

    print("A) EL ORDEN, LEIDO DEL FICHERO Y NO TECLEADO")
    print("   fuente: docs/plan/OPERACIONES.jsonl (campo `fase`)")
    fases = V161.fases_del_fichero()
    for f in fases:
        print("   %s" % f)
    print("   CIFRA fases con operaciones: %d" % len(fases))
    print("")

    print("B) EL RECORRIDO, FASE A FASE, CON SUS CIFRAS TALLADAS")
    print("   instrumento: scripts/loop/tallar_estado_de_fase.py --fase <N>")
    print("")
    print("   | fase | catalogo | cumplidas | sin cumplir | de ellas SIN VARA ESCRITA | "
          "sin cumplir CON VARA QUE MIDE | las que faltan |")
    print("   |---|---:|---:|---:|---:|---:|---|")
    tabla = {}
    for f in fases:
        d, rc = V161.estado(f)
        if d is None:
            print("   | %s | ROJO: el tallador no publico su linea CIFRA (exit %d) |" % (f, rc))
            return 1
        con_vara = d["sin_cumplir"] - d["sin_vara"]
        d["con_vara"] = con_vara
        tabla[f] = d
        print("   | %s | %d | %d | %d | %d | %d | %s |"
              % (f, d["catalogo"], d["cumplidas"], d["sin_cumplir"], d["sin_vara"],
                 con_vara, d["nombres"]))
    print("")

    catalogo = sum(d["catalogo"] for d in tabla.values())
    sin_cumplir = sum(d["sin_cumplir"] for d in tabla.values())
    sin_vara = sum(d["sin_vara"] for d in tabla.values())
    con_vara = sum(d["con_vara"] for d in tabla.values())
    print("   CIFRA fases medidas: %d" % len(tabla))
    print("   CIFRA fases sin NINGUNA sin cumplir: %d"
          % len([d for d in tabla.values() if d["sin_cumplir"] == 0]))
    print("   CIFRA fases sin ninguna sin cumplir CON VARA QUE MIDE: %d"
          % len([d for d in tabla.values() if d["con_vara"] == 0]))
    print("   CIFRA operaciones del plan entero: %d" % catalogo)
    print("   CIFRA sin cumplir en total: %d" % sin_cumplir)
    print("   CIFRA de ellas SIN VARA ESCRITA (no computables): %d" % sin_vara)
    print("   CIFRA de ellas SIN CUMPLIR CON VARA QUE MIDE: %d" % con_vara)
    print("")
    print("   LO QUE ESTA TABLA DICE Y LO QUE NO, Y SE SEPARA A PROPOSITO:")
    print("   'sin cumplir' del tallador incluye las NO COMPUTABLES, o sea las de un tipo")
    print("   para el que NO HAY REGLA ESCRITA que mida su destino contra el grafo. Esa")
    print("   columna NO dice que la operacion este pendiente: dice que nadie ha escrito")
    print("   con que medirla. La columna que si muerde es la ultima.")
    primeras = [f for f in fases if tabla[f]["con_vara"] > 0]
    print("   LA PRIMERA DEL ORDEN CON ALGO SIN CUMPLIR Y CON VARA QUE MIDE: %s"
          % (primeras[0] if primeras else "NINGUNA"))
    print("")

    print("C) LO QUE APARECE AL RECORRER EL ORDEN, COMPUTADO Y NO TECLEADO")
    print("   CIFRA fases con algo sin cumplir CON VARA QUE MIDE: %d" % len(primeras))
    for f in primeras:
        print("      %s: %d con vara que mide, dentro de las %d sin cumplir (%s)"
              % (f, tabla[f]["con_vara"], tabla[f]["sin_cumplir"], tabla[f]["nombres"]))
    print("   Y LA COMPARACION CON LA VUELTA 161, SIN BORRAR LO QUE AQUELLA MIDIO: la 161")
    print("   publico 47 sin cumplir, 44 sin vara escrita y TRES con vara que muerde")
    print("   (OP-M-02-ADMIT, OP-M-02-MEDIOS y OP-D-02). Hoy son %d, %d y %d: la que sale"
          % (sin_cumplir, sin_vara, con_vara))
    print("   es OP-D-02, y sale por la TAREA 2.b de esta vuelta (adjudicacion 6.4 del")
    print("   acta 161), no porque se haya tocado el grafo.")
    print("")

    print("D) EL MURO, MEDIDO HOY Y NO CITADO DE MEMORIA")
    lineas = io.open(ACTA, encoding="utf-8").read().split("\n")
    print("   ACTA_AUDITOR.md:%d, leida hoy:" % LINEA_ACTA_149)
    print("      %s" % lineas[LINEA_ACTA_149 - 1].strip()[:110])
    env = os.path.join(RAIZ, ".env")
    existe = os.path.exists(env)
    gitignore = io.open(os.path.join(RAIZ, ".gitignore"), encoding="utf-8").read().split("\n")
    en_gitignore = any(l.strip() == ".env" for l in gitignore)
    print("   .env existe en el arbol de trabajo: %s" % existe)
    print("   .env esta en .gitignore: %s" % en_gitignore)
    print("")
    print("   LA PRUEBA DE RUMBOS, CORRIDA HOY (tiene que fallar VISIBLE):")
    r = subprocess.run([sys.executable, os.path.join("scripts", "rumbos", "prueba_rumbos.py")],
                       cwd=RAIZ, capture_output=True, text=True,
                       encoding="utf-8", errors="replace")
    for l in ((r.stdout or "") + (r.stderr or "")).strip().split("\n")[:6]:
        if l.strip():
            print("      %s" % l.strip())
    print("      EXITCODE de la prueba de rumbos: %d" % r.returncode)
    print("      FALLA VISIBLE: %s" % (r.returncode != 0))
    print("")

    print("E) DONDE TERMINA LO QUE UN BUCLE PUEDE HACER SOLO")
    print("   La fase 08 tiene UNA operacion, OP-V-01, y su punto 9 es la verificacion")
    print("   TRANSVERSAL: Gate 0 verde, suite verde, VUELO COMPLETO, PRUEBA DE RUMBOS y")
    print("   REINDEXADO SEMANTICO. Las tres ultimas necesitan credencial. El .env esta")
    print("   fuera del repo mientras el bucle corre Y ESO ESTA BIEN (AUDITOR.md 4).")
    print("   SE PARA Y SE DICE: no es un fallo del bucle, es su frontera.")
    print("   EL MERGE NO SE PIDE NI SE HACE.")
    print("")
    print("FIN")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
