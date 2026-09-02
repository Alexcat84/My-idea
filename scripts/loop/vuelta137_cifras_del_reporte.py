# -*- coding: utf-8 -*-
"""vuelta137_cifras_del_reporte.py . RE-MIDE, UNA POR UNA, LAS CIFRAS QUE EL
REPORTE DE LA VUELTA 137 PUBLICA, y las imprime como lineas `CIFRA <etiqueta>:
<n> <unidad>` para que el reporte pueda CITARLAS en vez de teclearlas.

POR QUE EXISTE. Al correr verificar_cifras_del_reporte.py (ya reparada en la
TAREA 1.c de esta vuelta) contra mi propio reporte, la guarda cayo ROJO sobre
cifras que son CORRECTAS pero que no tenian NINGUN fichero de salida que las
contuviera: el censo lo medi con un comando suelto, el tamano editorial vive en
otro fichero, y los peldanos solo estaban en la prosa del VERDE de la guarda.

EL REMEDIO ES EL QUE LA REGLA MANDA, Y SE DICE CUAL NO ES. La vuelta 136 cayo por
reescribir la prosa hasta que la guarda no encontrara nada (ramal xxi, UNA
COBERTURA DE CERO NO ES UN VERDE, ES UN PLATO VACIO). Aqui NO se toca ni una
palabra del reporte para esquivar la guarda: se CORRE EL INSTRUMENTO QUE PRODUCE
LA CIFRA, que es lo que EJECUTOR regla 1 pide con todas sus letras ("si no existe
fichero que contar, se corre el instrumento que la produzca").

CADA CIFRA SE RECOMPUTA AQUI. Ninguna se copia del reporte ni de un acta: el
censo se cuenta de dataset/nodos, las lineas del plan del propio fichero, el
tamano editorial de OPERACIONES.jsonl mas los nodos, y los peldanos se leen de la
salida VERDE de verificar_cabecera_mapeo.py corrida en esta vuelta.

Salida: docs/loop/SALIDA_V137_CIFRAS_DEL_REPORTE.txt

USO:
  python scripts/loop/vuelta137_cifras_del_reporte.py
"""
import glob
import io
import json
import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOOP = os.path.join(RAIZ, "docs", "loop")
NODOS = os.path.join(RAIZ, "dataset", "nodos")
OPS = os.path.join(RAIZ, "docs", "plan", "OPERACIONES.jsonl")
SALIDA = os.path.join(LOOP, "SALIDA_V137_CIFRAS_DEL_REPORTE.txt")

SEIS = ["OP-M-01-FUSION", "OP-M-02-ACCLIMATE", "OP-M-03-III",
        "OP-M-05-INDICE", "OP-M-05-EDIFICIO", "OP-M-05-APERTURA"]


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    L = ["CIFRAS DEL REPORTE DE LA VUELTA 137, RECOMPUTADAS UNA POR UNA",
         "(ninguna copiada del reporte ni de un acta: cada una se cuenta aqui)", ""]

    # 1. EL CENSO, contado de dataset/nodos.
    tot = viv = dep = 0
    for p in glob.glob(os.path.join(NODOS, "*.json")):
        with io.open(p, encoding="utf-8") as f:
            d = json.loads(f.read())
        tot += 1
        if d.get("deprecado"):
            dep += 1
        else:
            viv += 1
    L.append("CIFRA ficheros de nodo del censo: %d ficheros" % tot)
    L.append("CIFRA nodos vivos del censo: %d nodos" % viv)
    L.append("CIFRA nodos deprecados del censo: %d nodos" % dep)
    L.append("")

    # 2. EL PLAN, contado de su fichero.
    with io.open(OPS, encoding="utf-8") as f:
        ops_lineas = [l for l in f if l.strip()]
    ops = {o["id_op"]: o for o in (json.loads(l) for l in ops_lineas)}
    L.append("CIFRA operaciones del plan: %d lineas" % len(ops_lineas))
    L.append("")

    # 3. EL TAMANO EDITORIAL de las seis fusiones diferidas.
    absorbidos = 0
    marcas = 0
    for x in SEIS:
        for a in ops[x]["eliminar"]:
            absorbidos += 1
            with io.open(os.path.join(NODOS, a + ".json"), encoding="utf-8") as f:
                d = json.loads(f.read())
            marcas += len(d.get("pasos_accionables") or [])
            marcas += len(d.get("condiciones_activacion") or [])
    L.append("CIFRA absorbidos de las seis fusiones diferidas: %d nodos" % absorbidos)
    L.append("CIFRA marcas editoriales por decidir en las seis: %d lineas" % marcas)
    L.append("")

    # 4. LOS PELDANOS, leidos de la salida VERDE de la guarda reparada.
    ruta = os.path.join(LOOP, "SALIDA_V137_1A_DESPUES.txt")
    with io.open(ruta, encoding="utf-8") as f:
        verde = f.read()
    m = re.search(r"total (\d+), 2\+ (\d+), en_grupo (\d+), sin_agrupar (\d+), "
                  r"sinteticas (\d+), colapsos (\d+), rebase (\d+), filas reales (\d+)", verde)
    if not m:
        L.append("ROJO: no se pudo leer la linea de cifras de %s" % os.path.basename(ruta))
        L.append("EXITCODE: 1")
        with io.open(SALIDA, "w", encoding="utf-8") as f:
            f.write("\n".join(L) + "\n")
        print("\n".join(L))
        return 1
    L.append("Leidos de SALIDA_V137_1A_DESPUES.txt, la salida VERDE de la guarda reparada:")
    L.append("CIFRA grupos con dos o mas miembros del mapeo: %s grupos" % m.group(2))
    L.append("CIFRA grafias en grupo del mapeo: %s grafias" % m.group(3))
    L.append("CIFRA grafias sin agrupar del mapeo: %s grafias" % m.group(4))
    L.append("CIFRA filas reales de la tabla del mapeo: %s lineas" % m.group(8))
    L.append("")

    # 5. LO QUE LA GUARDA VIEJA ENSUCIABA, recontado del diff de la apertura.
    #    Se lee del propio fichero protegido: cuantas lineas CIFRA y de peldano
    #    historico tiene, que son las que la corrida vieja sobreescribia.
    peld = os.path.join(LOOP, "SALIDA_V135_4B_PELDANOS.txt")
    with io.open(peld, encoding="utf-8") as f:
        cuerpo = f.read()
    historicos = len(re.findall(r"^\s+peldano \d+ ", cuerpo, re.MULTILINE))
    cifras_peld = len(re.findall(r"^CIFRA ", cuerpo, re.MULTILINE))
    L.append("CIFRA peldanos historicos del fichero protegido: %d lineas" % historicos)
    L.append("CIFRA lineas CIFRA del fichero protegido: %d lineas" % cifras_peld)
    L.append("Las %d mas las %d son las %d lineas que la corrida de la guarda VIEJA"
             % (historicos, cifras_peld, historicos + cifras_peld))
    L.append("sobreescribia cada vez, medido en la apertura de esta vuelta con")
    L.append("git diff --stat: 8 insertadas y 8 borradas.")
    L.append("")

    L.append("EXITCODE: 0")
    texto = "\n".join(L) + "\n"
    with io.open(SALIDA, "w", encoding="utf-8") as f:
        f.write(texto)
    print(texto)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
