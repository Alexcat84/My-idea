# -*- coding: utf-8 -*-
r"""vuelta164_tarea6_orden_y_muro.py . TAREA 6 de la vuelta 164.

SIGUE EL ORDEN ESCRITO EN MODO CONTINUO HASTA EL MURO CONOCIDO Y YA ADJUDICADO
(acta 149, seccion 3.10). NO CIERRA NINGUNA FASE Y NO TOCA NINGUN NODO.

POR QUE UN INSTRUMENTO NUEVO Y NO EL DE LA VUELTA 163, Y SE DICE EN VEZ DE
CALLARSE. El de la 163 arreglo la seccion C de su antecesor leyendo el contraste
de la salida sellada de la vuelta anterior en vez de teclearlo, y ese arreglo es
correcto y SE HEREDA IMPORTANDOLO. Lo que quedo rancio un escalon mas arriba es
LA RUTA DE ESA SALIDA: `ANTERIOR` es una constante con el numero de vuelta
DENTRO (`SALIDA_V162_T5_ORDEN_Y_MURO.txt`). Cada vuelta hay que re teclearla, y
el dia que alguien la olvide el instrumento comparara contra una vuelta que no
es la anterior SIN DECIR NADA, porque el fichero existe y trae sus cifras. Es la
misma especie que la 163 curo en `160_6b`: una referencia que hay que mantener a
mano acaba apuntando a otro sitio.

EL REMEDIO, Y ES EL DE LA CASA: LA SALIDA DE CONTRASTE SE COMPUTA. Se listan
todas las `docs/loop/SALIDA_V<N>_*_ORDEN_Y_MURO.txt` que EXISTEN, se toma la del
NUMERO MAYOR que sea MENOR que esta vuelta, y se publica cual se eligio y de que
vueltas habia. Si no hay ninguna, se dice y no se compara.

Y AQUI ESO IMPORTA DE VERDAD, no es teoria: LA VUELTA 163 NO DEJO SALIDA. Su
instrumento existe y nunca se corrio (acta 163, seccion 2: *"6 orden y muro, NO
HECHA, cero salidas; existe vuelta163_tarea6_orden_y_muro.py sin correr"*). O
sea que el contraste de HOY es contra la 162 y NO contra la 163, y eso se dice
con todas sus letras en vez de dejar que parezca que se comparo con la vuelta
inmediatamente anterior.

NO SE COPIA UNA LINEA DEL RECORRIDO: se importan `vuelta161_tarea3_orden_y_muro`
(fases y estado por fase) y `vuelta163_tarea6_orden_y_muro` (el parseo del
contraste). Una sola fuente.

USO:  python scripts/loop/vuelta164_tarea6_orden_y_muro.py
"""
import io
import os
import re
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import vuelta161_tarea3_orden_y_muro as V161   # noqa: E402
import vuelta163_tarea6_orden_y_muro as V163   # noqa: E402

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

RAIZ = V161.RAIZ
ACTA = V161.ACTA
LINEA_ACTA_149 = V161.LINEA_ACTA_149
LOOP = os.path.join(RAIZ, "docs", "loop")
VUELTA = 164

PATRON_SALIDA = re.compile(r"^SALIDA_V(\d+)_.*_ORDEN_Y_MURO\.txt$")


def salidas_de_contraste():
    """(las que existen ordenadas por vuelta, la elegida). NO SE TECLEA NINGUNA
    RUTA: se computan del propio directorio, y la elegida es la de mayor numero
    de vuelta ESTRICTAMENTE MENOR que esta."""
    halladas = []
    for nombre in sorted(os.listdir(LOOP)):
        m = PATRON_SALIDA.match(nombre)
        if m:
            halladas.append((int(m.group(1)), nombre))
    halladas.sort()
    previas = [h for h in halladas if h[0] < VUELTA]
    return halladas, (previas[-1] if previas else None)


def main():
    print("=" * 78)
    print("VUELTA %d, TAREA 6: EL ORDEN ESCRITO, RECORRIDO HASTA EL MURO" % VUELTA)
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

    print("C) EL CONTRASTE, Y LA SALIDA CONTRA LA QUE SE CONTRASTA, COMPUTADA")
    halladas, elegida = salidas_de_contraste()
    print("   CIFRA salidas de orden y muro que existen en docs/loop/: %d" % len(halladas))
    for n, nombre in halladas:
        print("      vuelta %-4d %s" % (n, nombre))
    if elegida is None:
        print("   NO HAY NINGUNA ANTERIOR: no se compara y no se inventa el contraste.")
        antes, rel = None, "(ninguna)"
    else:
        n_ele, nombre_ele = elegida
        rel = "docs/loop/%s" % nombre_ele
        print("   ELEGIDA, la de mayor vuelta menor que %d: vuelta %d, %s"
              % (VUELTA, n_ele, nombre_ele))
        if n_ele != VUELTA - 1:
            print("   AVISO, Y SE DICE EN VEZ DE DEJARLO PASAR: la elegida NO es la de la")
            print("   vuelta %d, que es la inmediatamente anterior. Esa vuelta NO dejo"
                  % (VUELTA - 1))
            print("   salida de orden y muro (acta 163, seccion 2: la TAREA 6 quedo sin")
            print("   correr). El contraste de hoy es contra la vuelta %d." % n_ele)
        V163.ANTERIOR = os.path.join(LOOP, nombre_ele)
        antes, _rel_v163 = V163.contraste_de_la_anterior()
    print("   fuente del contraste: %s" % rel)
    if antes is None:
        print("   NO SE PUDO LEER EL CONTRASTE: el fichero no esta o no trae sus lineas")
        print("   CIFRA. NO se inventa la comparacion y NO se cita de memoria: se dice.")
    else:
        hoy = {"catalogo": catalogo, "sin_cumplir": sin_cumplir,
               "sin_vara": sin_vara, "con_vara": con_vara}
        print("   | cifra | vuelta %d (leida de su fichero) | vuelta %d (medida hoy) | "
              "delta |" % (elegida[0], VUELTA))
        print("   |---|---:|---:|---:|")
        for nombre, _p in V163.CIFRAS_DEL_CONTRASTE:
            print("   | %s | %d | %d | %+d |"
                  % (nombre, antes[nombre], hoy[nombre], hoy[nombre] - antes[nombre]))
        movidas = [n for n, _p in V163.CIFRAS_DEL_CONTRASTE if antes[n] != hoy[n]]
        print("   CIFRA cifras que se movieron respecto de la de contraste: %d (%s)"
              % (len(movidas), ", ".join(movidas) or "ninguna"))
        if not movidas:
            print("   NINGUNA SE MOVIO, y era lo esperado: ni la 163 ni la 164 tocan el")
            print("   grafo, ni cierran ninguna operacion. Las dos clases que esta vuelta")
            print("   toca viven en el REGISTRO DE CITAS, no en el catalogo de operaciones.")
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
    print("   SE PARA Y SE DICE: no es un fallo del bucle, es su frontera. HACE FALTA UNA")
    print("   SESION CON CREDENCIAL Y CON EL FUNDADOR DELANTE.")
    print("   EL MERGE NO SE PIDE NI SE HACE: es del fundador y solo suyo.")
    print("")
    print("FIN")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
