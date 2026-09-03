# -*- coding: utf-8 -*-
r"""vuelta163_tarea6_orden_y_muro.py . TAREA 6 de la vuelta 163.

SIGUE EL ORDEN ESCRITO EN MODO CONTINUO HASTA EL MURO CONOCIDO Y YA ADJUDICADO
(acta 149, seccion 3.10). NO CIERRA NINGUNA FASE Y NO TOCA NINGUN NODO.

POR QUE UN INSTRUMENTO NUEVO Y NO EL DE LA VUELTA 162, Y SE DICE EN VEZ DE
CALLARSE. El de la 162 (`vuelta162_tarea5_orden_y_muro.py`) ya arreglo la
seccion D de su antecesor computandola en vez de teclearla, y sus secciones A, B
y D siguen siendo correctas: POR ESO SE IMPORTAN Y NO SE COPIAN. Lo que quedo
rancio esta vez es SU SECCION C, que lleva ESCRITO A MANO *"la 161 publico 47
sin cumplir, 44 sin vara escrita y TRES con vara que muerde"*. Es la misma
especie de deuda, un escalon mas arriba: la comparacion con la vuelta anterior
se teclea cada vez.

EL REMEDIO, Y ES EL DE LA CASA: LA COMPARACION SE LEE DE LA SALIDA SELLADA DE LA
VUELTA ANTERIOR (`docs/loop/SALIDA_V162_T5_ORDEN_Y_MURO.txt`), parseando sus
propias lineas `CIFRA`, y no de la memoria de nadie. Si ese fichero no esta o no
trae sus cifras, esto lo DICE y sigue sin comparar, en vez de inventar el
contraste.

USO:  python scripts/loop/vuelta163_tarea6_orden_y_muro.py
"""
import io
import os
import re
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import vuelta161_tarea3_orden_y_muro as V161   # noqa: E402

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

RAIZ = V161.RAIZ
ACTA = V161.ACTA
LINEA_ACTA_149 = V161.LINEA_ACTA_149

# LA SALIDA SELLADA DE LA VUELTA ANTERIOR, que es de donde sale el contraste.
ANTERIOR = os.path.join(RAIZ, "docs", "loop", "SALIDA_V162_T5_ORDEN_Y_MURO.txt")

CIFRAS_DEL_CONTRASTE = [
    ("sin_cumplir", r"CIFRA sin cumplir en total: (\d+)"),
    ("sin_vara", r"CIFRA de ellas SIN VARA ESCRITA \(no computables\): (\d+)"),
    ("con_vara", r"CIFRA de ellas SIN CUMPLIR CON VARA QUE MIDE: (\d+)"),
    ("catalogo", r"CIFRA operaciones del plan entero: (\d+)"),
]


def contraste_de_la_anterior():
    """Las cifras de la vuelta anterior, PARSEADAS de su salida sellada. Devuelve
    (dict, ruta_relativa) o (None, ruta) si no se puede leer."""
    rel = os.path.relpath(ANTERIOR, RAIZ).replace("\\", "/")
    if not os.path.exists(ANTERIOR):
        return None, rel
    texto = io.open(ANTERIOR, encoding="utf-8", errors="replace").read()
    out = {}
    for nombre, patron in CIFRAS_DEL_CONTRASTE:
        m = re.search(patron, texto)
        if m is None:
            return None, rel
        out[nombre] = int(m.group(1))
    return out, rel


def main():
    print("=" * 78)
    print("VUELTA 163, TAREA 6: EL ORDEN ESCRITO, RECORRIDO HASTA EL MURO")
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
        d["con_vara"] = d["sin_cumplir"] - d["sin_vara"]
        tabla[f] = d
        print("   | %s | %d | %d | %d | %d | %d | %s |"
              % (f, d["catalogo"], d["cumplidas"], d["sin_cumplir"], d["sin_vara"],
                 d["con_vara"], d["nombres"]))
    print("")

    catalogo = sum(d["catalogo"] for d in tabla.values())
    cumplidas = sum(d["cumplidas"] for d in tabla.values())
    sin_cumplir = sum(d["sin_cumplir"] for d in tabla.values())
    sin_vara = sum(d["sin_vara"] for d in tabla.values())
    con_vara = sum(d["con_vara"] for d in tabla.values())
    print("   CIFRA fases medidas: %d" % len(tabla))
    print("   CIFRA fases sin NINGUNA sin cumplir: %d"
          % len([d for d in tabla.values() if d["sin_cumplir"] == 0]))
    print("   CIFRA fases sin ninguna sin cumplir CON VARA QUE MIDE: %d"
          % len([d for d in tabla.values() if d["con_vara"] == 0]))
    print("   CIFRA operaciones del plan entero: %d" % catalogo)
    print("   CIFRA cumplidas en total: %d" % cumplidas)
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

    print("C) EL CONTRASTE CON LA VUELTA ANTERIOR, LEIDO DE SU SALIDA SELLADA")
    print("   Y NO TECLEADO (que es lo que quedo rancio en el instrumento de la 162)")
    antes, rel = contraste_de_la_anterior()
    print("   fuente del contraste: %s" % rel)
    if antes is None:
        print("   NO SE PUDO LEER EL CONTRASTE: el fichero no esta o no trae sus lineas")
        print("   CIFRA. NO se inventa la comparacion y NO se cita de memoria: se dice.")
    else:
        hoy = {"catalogo": catalogo, "sin_cumplir": sin_cumplir,
               "sin_vara": sin_vara, "con_vara": con_vara}
        print("   | cifra | vuelta 162 (leida de su fichero) | vuelta 163 (medida hoy) | "
              "delta |")
        print("   |---|---:|---:|---:|")
        for nombre, _p in CIFRAS_DEL_CONTRASTE:
            print("   | %s | %d | %d | %+d |"
                  % (nombre, antes[nombre], hoy[nombre], hoy[nombre] - antes[nombre]))
        movidas = [n for n, _p in CIFRAS_DEL_CONTRASTE if antes[n] != hoy[n]]
        print("   CIFRA cifras que se movieron respecto de la vuelta anterior: %d (%s)"
              % (len(movidas), ", ".join(movidas) or "ninguna"))
        if not movidas:
            print("   NINGUNA SE MOVIO, y era lo esperado: esta vuelta NO toca el grafo,")
            print("   NO cierra ninguna operacion y NO mueve ninguna clase.")
    print("")

    print("D) LAS QUE SIGUEN SIN CUMPLIR CON VARA QUE MIDE, COMPUTADAS Y NO TECLEADAS")
    print("   CIFRA fases con algo sin cumplir CON VARA QUE MIDE: %d" % len(primeras))
    for f in primeras:
        print("      %s: %d con vara que mide, dentro de las %d sin cumplir (%s)"
              % (f, tabla[f]["con_vara"], tabla[f]["sin_cumplir"], tabla[f]["nombres"]))
    if not primeras:
        print("      (ninguna)")
    print("")

    print("E) EL MURO, MEDIDO HOY Y NO CITADO DE MEMORIA")
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

    print("F) DONDE TERMINA LO QUE UN BUCLE PUEDE HACER SOLO")
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
