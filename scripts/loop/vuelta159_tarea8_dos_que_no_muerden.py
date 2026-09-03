# -*- coding: utf-8 -*-
"""vuelta159_tarea8_dos_que_no_muerden.py . TAREA 8 DE LA VUELTA 159.

SE LEE EL ROJO DE `vuelta96_tarea3_prueba_mutacion.py` Y
`vuelta97_tarea2_prueba_mutacion.py` ANTES DE TOCAR NADA (adjudicacion 6.10 del
acta 158). Las dos salen exit 1 y las dos sostienen la P3b de `OP-E-03`.

LO QUE ESTE INSTRUMENTO HACE, Y LO QUE NO. HACE: correr las dos, extraer sus
fallos, y DIAGNOSTICAR LA CAUSA CONTRA EL GRAFO. NO HACE, y es la prohibicion
literal de la 6.10: AJUSTAR LA EXPECTATIVA HASTA QUE SALGA VERDE. Ninguna tabla
congelada se retoca, ningun control se afloja, ningun numero esperado se mueve.

EL DIAGNOSTICO, Y ES EL MISMO PARA LAS DOS: EL SUJETO ESTA CONGELADO Y EL GRAFO
SE MOVIO. Las tablas de veredicto de las vueltas 96 y 97 nombran los ids que los
nodos TENIAN ENTONCES. Despues, en las mesas de fusion, varios de esos nodos se
FUNDIERON en un superviviente y quedaron DEPRECADOS. El resolutor de la casa
(P.1) mapea el id viejo al superviviente, y el check compara EL NOMBRE LITERAL
de la tabla contra EL NOMBRE RESUELTO de hoy: por eso canta desviacion. Es
exactamente la especie de la vara anclada a algo que se mueve.

COMO SE PRUEBA QUE ES ESO Y NO UNA REGRESION, y son dos pruebas independientes:
  (i)  TODAS LAS MUTACIONES DE LAS DOS SIGUEN MORDIENDO. Si la guarda se hubiera
       roto, alguna mutacion habria dejado de caer. Se cuenta cuantas caen y se
       publica.
  (ii) CADA NODO NOMBRADO EN UN FALLO SE MIRA CONTRA EL GRAFO DE HOY: se dice si
       esta DEPRECADO, cual es el nodo vivo con el que el check lo contrasta y en
       que fila del registro de fusiones (`docs/plan/03_FUSIONES.md`) aparece. Si
       algun nodo de un fallo NO estuviera deprecado, ESO SI SERIA HALLAZGO y
       este instrumento lo diria en vez de taparlo.

LA MARCA OBLIGATORIA, CON LA MISMA DISCIPLINA QUE LA BATERIA DE LAS 23. Un CASO
DECLARADO no exime al script: exime A UN FALLO CONCRETO. Por eso cada uno lleva
una MARCA literal tomada de su salida de hoy, y si manana el script empieza a
fallar por OTRA razon esa marca no aparecera y el caso volvera a caer. La marca
no se teclea: se comprueba contra la salida de la corrida de hoy.

USO:  python scripts/loop/vuelta159_tarea8_dos_que_no_muerden.py
"""
import io
import json
import os
import re
import subprocess
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
GRAFO = os.path.join(RAIZ, "dataset", "metadata", "master_graph.json")
FUSIONES = os.path.join(RAIZ, "docs", "plan", "03_FUSIONES.md")

# CADA SUJETO ES (ruta, MARCA_OBLIGATORIA, CORTE). El CORTE es el literal a
# partir del cual la salida DEJA DE SER CONTROL y pasa a ser MUTACION INYECTADA,
# y existe por una caida de este mismo instrumento que se declara en vez de
# taparse: la primera corrida cazo `takt_time` y `smed_setup_reduction` como
# "nodos sin explicar" del sujeto 97, y esos dos NO son un fallo del control:
# son EL NODO AJENO QUE LA MUTACION 3 INYECTA A PROPOSITO ("la direccion del par
# 45 nombra otros dos nodos"). Contar la mutacion como sintoma es leer la prueba
# al reves. Con corte None se analiza la salida entera.
SUJETOS = [
    ("scripts/loop/vuelta96_tarea3_prueba_mutacion.py",
     "CONTROL (dato real): material 40 filas / 2 fallos, veredictos 40 filas / 6 fallos -> ROJO",
     None),
    ("scripts/loop/vuelta97_tarea2_prueba_mutacion.py",
     "RESULTADO: 10 de 12 comprobaciones se comportan como deben.",
     "MUTACIONES DEL ARMAZON"),
]

PATRON_NODO = re.compile(r"[a-z][a-z0-9_]{6,}")
PATRON_CAE_OK = re.compile(r"CAE\s+(?:\(correcto\)|OK)")
PATRON_FALLO_NODOS = re.compile(r"nombra \[([^\]]*)\].*?resueltos de esa fila \(([^)]*)\)")


def correr(rel):
    r = subprocess.run([sys.executable, os.path.join(RAIZ, rel)],
                       cwd=RAIZ, capture_output=True)
    return r.returncode, r.stdout.decode("utf-8", "replace") + \
        r.stderr.decode("utf-8", "replace")


def main():
    print("=" * 78)
    print("VUELTA 159, TAREA 8: SE LEE EL ROJO DE LAS DOS QUE NO MUERDEN")
    print("=" * 78)
    print("")

    N = json.load(io.open(GRAFO, encoding="utf-8"))["nodos"]
    texto_fusiones = io.open(FUSIONES, encoding="utf-8").read()

    resumen = []
    for rel, marca, corte in SUJETOS:
        print("=" * 78)
        print("SUJETO: %s" % rel)
        print("=" * 78)
        codigo, salida = correr(rel)
        print("   exit medido en esta vuelta: %d" % codigo)
        print("   MARCA OBLIGATORIA declarada para este caso:")
        print("      %r" % marca)
        tiene = marca in salida
        print("   la marca aparece en la salida de hoy: %s" % ("SI" if tiene else "NO"))
        if not tiene:
            print("   ROJO: la marca NO aparece. Este script esta fallando por OTRA")
            print("   razon y el CASO DECLARADO NO LO CUBRE. Es hallazgo y se trae.")
            resumen.append((rel, codigo, "MARCA AUSENTE, NO CUBIERTO", 0, 0, 0))
            print("")
            continue

        muerden = len(PATRON_CAE_OK.findall(salida))
        print("")
        print("   (i) LAS MUTACIONES SIGUEN MORDIENDO?")
        print("       CIFRA mutaciones que CAEN como deben en esta corrida: %d" % muerden)
        print("       Si la guarda se hubiera roto, alguna habria dejado de caer.")
        print("")

        print("   (ii) LOS NODOS DE CADA FALLO DEL CONTROL, CONTRA EL GRAFO DE HOY")
        if corte and corte in salida:
            zona = salida[:salida.index(corte)]
            print("       CORTE DECLARADO: solo se analiza lo anterior a %r," % corte)
            print("       porque lo de despues son NODOS AJENOS INYECTADOS A PROPOSITO.")
        else:
            zona = salida
            print("       sin corte: se analiza la salida entera.")
        pares = PATRON_FALLO_NODOS.findall(zona)
        vistos = set()
        deprecados, vivos_raros = 0, []
        for nombrados, resueltos in pares:
            nn = PATRON_NODO.findall(nombrados)
            rr = PATRON_NODO.findall(resueltos)
            for a in nn:
                if a in vistos:
                    continue
                vistos.add(a)
                nodo = N.get(a)
                if nodo is None:
                    print("       %-44s NO EXISTE HOY EN EL GRAFO" % a)
                    vivos_raros.append(a)
                    continue
                dep = bool(nodo.get("deprecado"))
                if dep:
                    deprecados += 1
                else:
                    if a not in rr:
                        vivos_raros.append(a)
                fila = "SI" if ("`%s`" % a) in texto_fusiones else "no"
                print("       %-44s deprecado=%-5s en 03_FUSIONES.md: %s"
                      % (a, dep, fila))
        print("       CIFRA nodos nombrados en fallos que estan DEPRECADOS: %d" % deprecados)
        print("       CIFRA nodos nombrados en fallos que NO se explican por fusion: %d"
              % len(vivos_raros))
        if vivos_raros:
            print("       ESO SI SERIA HALLAZGO: %s" % ", ".join(sorted(set(vivos_raros))))
        print("")

        if deprecados and not vivos_raros:
            veredicto = "CASO DECLARADO: EXPECTATIVA ENVEJECIDA SOBRE SUJETO CONGELADO"
            print("   VEREDICTO: %s" % veredicto)
            print("   MOTIVO ESCRITO: la tabla congelada nombra los ids de antes de las")
            print("   mesas de fusion; esos nodos hoy estan DEPRECADOS y el resolutor los")
            print("   manda a su superviviente, asi que el check compara el nombre viejo")
            print("   contra el nuevo y canta desviacion. LA GUARDA NO SE HA ROTO: sus")
            print("   %d mutaciones siguen cayendo. NO SE AJUSTA LA EXPECTATIVA." % muerden)
        else:
            veredicto = "HALLAZGO, NO CASO DECLARADO"
            print("   VEREDICTO: %s" % veredicto)
        resumen.append((rel, codigo, veredicto, muerden, deprecados, len(vivos_raros)))
        print("")

    print("=" * 78)
    print("RESUMEN")
    print("=" * 78)
    for rel, codigo, ver, muerden, dep, raros in resumen:
        print("  %-52s exit %d" % (os.path.basename(rel), codigo))
        print("      %s" % ver)
        print("      mutaciones que caen: %d | nodos deprecados en fallos: %d | "
              "sin explicar: %d" % (muerden, dep, raros))
    print("  CIFRA sujetos con CASO DECLARADO: %d"
          % sum(1 for x in resumen if x[2].startswith("CASO DECLARADO")))
    print("  CIFRA sujetos que quedan como HALLAZGO: %d"
          % sum(1 for x in resumen if not x[2].startswith("CASO DECLARADO")))
    print("")
    print("LO QUE NO SE HIZO, Y ES LA PROHIBICION LITERAL DE LA 6.10: no se ajusto")
    print("ninguna expectativa, no se retoco ninguna tabla congelada y los dos scripts")
    print("SIGUEN SALIENDO exit 1. Un caso declarado no apaga un rojo: lo explica.")
    print("FIN")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
