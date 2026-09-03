# -*- coding: utf-8 -*-
"""vuelta159_tarea8b_declarar_los_dos_casos.py . TAREA 8 DE LA VUELTA 159, LA
DECLARACION.

DEJA ESCRITO EN CADA UNO DE LOS DOS SCRIPTS SU CASO DECLARADO, con su motivo y
su MARCA OBLIGATORIA (adjudicacion 6.10 del acta 158). POR ADICION, al final del
docstring de modulo; nada se borra, y la aditividad se mide con
`git diff --numstat` exigiendo BORRADOS 0.

LO QUE ESTA DECLARACION NO HACE, Y ES LA PROHIBICION LITERAL DE LA 6.10: NO
AJUSTA NINGUNA EXPECTATIVA. Los dos scripts siguen saliendo exit 1 despues de
esto. Un caso declarado no apaga un rojo: lo explica y lo ata a una marca, para
que el dia que fallen por otra razon la marca no aparezca y el rojo vuelva a
contar.

USO:  python scripts/loop/vuelta159_tarea8b_declarar_los_dos_casos.py
"""
import io
import os
import subprocess
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

MARCA = "CASO DECLARADO (VUELTA 159, ADJUDICACION 6.10 DEL ACTA 158)"

COMUN = """
--- %s: EXPECTATIVA ENVEJECIDA SOBRE UN
SUJETO CONGELADO. EL ROJO SE EXPLICA, NO SE APAGA ---

REGISTRO POR ADICION. Nada de lo escrito arriba se borra, NINGUNA EXPECTATIVA SE
AJUSTA Y ESTE SCRIPT SIGUE SALIENDO exit 1 DESPUES DE ESTA DECLARACION. La 6.10
prohibe con esas palabras "ajustar la expectativa hasta que salga verde", que es
la caida que esta campana persigue desde el principio.

EL DIAGNOSTICO, MEDIDO CON
`scripts/loop/vuelta159_tarea8_dos_que_no_muerden.py` (salida
`docs/loop/SALIDA_V159_T8_DIAGNOSTICO.txt`): EL SUJETO ESTA CONGELADO Y EL GRAFO
SE MOVIO. La tabla de veredictos de esta vuelta nombra los ids que los nodos
TENIAN ENTONCES. Despues, en las mesas de fusion, varios de esos nodos se
FUNDIERON en un superviviente y quedaron DEPRECADOS; el resolutor de la casa
(P.1) manda el id viejo al superviviente, y el check compara EL NOMBRE LITERAL
DE LA TABLA contra EL NOMBRE RESUELTO DE HOY. Por eso canta desviacion. Es la
especie de la vara anclada a algo que se mueve.

LAS DOS PRUEBAS INDEPENDIENTES DE QUE NO ES UNA REGRESION DE LA GUARDA:
  (i)  LAS SEIS MUTACIONES DE ESTE SCRIPT SIGUEN CAYENDO, contadas en la corrida
       del 3 sep 2026. Si la guarda se hubiera roto, alguna habria dejado de
       morder.
  (ii) TODOS LOS NODOS NOMBRADOS EN LOS FALLOS DEL CONTROL ESTAN DEPRECADOS y
       aparecen en `docs/plan/03_FUSIONES.md`: CERO nodos sin explicar por
       fusion. Si alguno no lo estuviera, seria hallazgo y no caso declarado, y
       el instrumento lo diria.
%s
LA MARCA OBLIGATORIA DE ESTE CASO, con la misma disciplina que los dos CASOS
DECLARADOS de la bateria de las 23: la exencion NO es del script, es DE UN FALLO
CONCRETO, y solo vale mientras la salida traiga LITERALMENTE esta linea:

    %s

Si manana este script empieza a fallar por otra razon, esa linea no aparecera y
el caso volvera a contar como rojo sin explicar.
"""

NODOS = {
    "scripts/loop/vuelta96_tarea3_prueba_mutacion.py": (
        "CONTROL (dato real): material 40 filas / 2 fallos, veredictos 40 filas / 6 fallos -> ROJO",
        """
LOS NODOS FUNDIDOS QUE ESTE CASO TOCA, medidos contra el grafo de hoy:
  `get_out_of_the_building`              deprecado, resuelve a
                                         `customer_discovery_get_out_of_building`
  `customer_discovery_overview`          deprecado, resuelve a `customer_discovery`
  `estrategia_de_innovacion_de_producto` deprecado, resuelve a
                                         `estrategia_innovacion_producto`
Y las dos filas de material que caen por "YA ESTA EN LA COLA tras resolver" son
la misma causa vista por el otro lado: tras resolver el id viejo, el par cae
dentro de la cola del cribado, que en la vuelta 96 no lo contenia.
"""),
    "scripts/loop/vuelta97_tarea2_prueba_mutacion.py": (
        "RESULTADO: 10 de 12 comprobaciones se comportan como deben.",
        """
LOS NODOS FUNDIDOS QUE ESTE CASO TOCA, medidos contra el grafo de hoy:
  `estrategia_de_innovacion_de_producto` deprecado, resuelve a
                                         `estrategia_innovacion_producto`
  `requisitos_gates_con_dientes`         deprecado, resuelve a `sistema_gates_go_kill`
  `get_out_of_the_building`              deprecado, resuelve a
                                         `customer_discovery_get_out_of_building`
Las dos afirmaciones de la senial de esta vuelta (la mediana de los dos tramos y
la de misma fuente leida contra no resuelta) SIGUEN VERDES y sus dos mutaciones
siguen cayendo: lo que envejecio es el armazon de la tabla, no la senial.
"""),
}


def leer(ruta):
    return io.open(ruta, encoding="utf-8").read()


def numstat(rel):
    r = subprocess.run(["git", "diff", "--numstat", "--", rel],
                       cwd=RAIZ, capture_output=True)
    l = r.stdout.decode("utf-8", "replace").strip()
    if not l:
        return 0, 0
    c = l.split("\t")
    return int(c[0]), int(c[1])


def main():
    print("=" * 78)
    print("VUELTA 159, TAREA 8: LOS DOS CASOS DECLARADOS, ESCRITOS DONDE VIVEN")
    print("=" * 78)
    print("")
    total_borrados = 0
    for rel, (marca_obl, nodos) in NODOS.items():
        ruta = os.path.join(RAIZ, rel)
        texto = leer(ruta)
        if MARCA in texto:
            print("   %-52s YA ESTABA" % os.path.basename(rel))
        else:
            bloque = COMUN % (MARCA, nodos, marca_obl)
            ini = texto.index('"""')
            fin = texto.index('"""', ini + 3)
            with io.open(ruta, "w", encoding="utf-8", newline="\n") as fh:
                fh.write(texto[:fin] + bloque + texto[fin:])
            print("   %-52s ANADIDO %d lineas"
                  % (os.path.basename(rel), len(bloque.splitlines())))
        mas, menos = numstat(rel)
        total_borrados += menos
        print("      numstat: mas %d, menos %d" % (mas, menos))
    print("")
    print("   CIFRA borrados en los dos .py: %d" % total_borrados)
    assert total_borrados == 0, "SE BORRO UNA LINEA: la aditividad esta rota"
    print("   CERO BORRADOS.")
    print("")

    print("   Y LOS DOS SIGUEN SALIENDO ROJO DESPUES DE DECLARARLOS, que es el punto:")
    for rel in NODOS:
        r = subprocess.run([sys.executable, os.path.join(RAIZ, rel)],
                           cwd=RAIZ, capture_output=True)
        print("      %-52s exit %d" % (os.path.basename(rel), r.returncode))
    print("")
    print("FIN")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
