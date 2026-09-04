# -*- coding: utf-8 -*-
r"""vuelta167_tarea5_estado_de_op_c_01.py . QUE DICE LA FICHA DE `OP-C-01` Y QUE
DICE EL CODIGO, MEDIDO ANTES DE EJECUTAR NADA (TAREA 5 de la vuelta 167;
adjudicacion 6.9 del acta 166).

POR QUE NACE. El encargo manda ejecutar `OP-C-01` TAL COMO SU FICHA ESTA
ESCRITA, y su verificacion trae una letra que manda sobre las demas: *"ninguna
prueba nueva pasa verde ANTES del arreglo: si pasa, no prueba nada"*. Lo primero
que hay que medir, entonces, NO es el arreglo: es SI EL ARREGLO YA ESTA PUESTO,
porque si lo esta, esa letra no se puede cumplir y no hay caso positivo posible.

QUE MIDE, TODO DE GIT Y DEL ARBOL, NADA TECLEADO:
  (1) EL ESTADO DE LA FICHA hoy en `docs/plan/OPERACIONES.jsonl`, y su historia:
      en que commit nacio la fila y si su `estado` se movio alguna vez.
  (2) LOS TRES PUNTOS DEL ARREGLO que la propia `nota` de la ficha enumera, uno
      por uno, buscados en los cuatro ficheros que la `nota` nombra.
  (3) LAS TRES PRUEBAS de la lista `verificacion`, buscadas en la suite.
  (4) EL COMMIT que introdujo cada marca, leido con `git log -S`.

CERO ESCRITURAS: solo imprime.

USO:  python scripts/loop/vuelta167_tarea5_estado_de_op_c_01.py
"""
import io
import json
import os
import subprocess
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
OPS = os.path.join(RAIZ, "docs", "plan", "OPERACIONES.jsonl")


def git(*args):
    r = subprocess.run(["git"] + list(args), cwd=RAIZ, capture_output=True)
    return r.stdout.decode("utf-8", "replace").strip()


MARCAS = [
    ("1. resolver nid al entrar en aMaterial",
     "web/lib/engine/planRedactor.ts",
     "OP-C-01 de la pasada unica: RESUELVE AL ENTRAR"),
    ("2a. cargarEntrySeeds(graph) en organizer",
     "web/app/api/organizer/route.ts",
     "cargarEntrySeeds(graph)"),
    ("2b. cargarEntrySeeds(graph) en organizer/stream",
     "web/app/api/organizer/stream/route.ts",
     "cargarEntrySeeds(graph)"),
    ("3. resolver antes de puntuar en compass",
     "web/lib/compass.ts",
     "OP-C-01: RESOLVER ANTES DE PUNTUAR"),
]

PRUEBAS = [
    ("aMaterial con id deprecado de alias vivo",
     "web/lib/engine/accesosResueltos.test.ts",
     "OP-C-01 - aMaterial: el material del plan se arma tras resolver"),
    ("organizer con seed deprecado",
     "web/lib/engine/accesosResueltos.test.ts",
     "OP-C-01 - las semillas del organizador pasan por la puerta unica"),
    ("compass con id que ya no es nodo",
     "web/lib/engine/accesosResueltos.test.ts",
     "OP-C-01 - el indice semantico no ofrece lo que ya no es nodo"),
]


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    print("=" * 78)
    print("VUELTA 167, TAREA 5: EL ESTADO REAL DE OP-C-01, ANTES DE EJECUTAR NADA")
    print("=" * 78)
    print("")

    print("A) LA FICHA, LEIDA HOY DEL REGISTRO")
    fila = None
    n_linea = 0
    for i, l in enumerate(io.open(OPS, encoding="utf-8"), 1):
        if not l.strip():
            continue
        d = json.loads(l)
        if d.get("id_op") == "OP-C-01":
            fila, n_linea = d, i
    if fila is None:
        print("   PARADA: OP-C-01 no esta en docs/plan/OPERACIONES.jsonl.")
        return 1
    print("   docs/plan/OPERACIONES.jsonl:%d" % n_linea)
    print("   estado          : %s" % fila["estado"])
    print("   fase            : %s   orden: %s" % (fila["fase"], fila["orden"]))
    print("   depende_de      : %s" % fila["depende_de"])
    print("   bloquea_a       : %s" % fila["bloquea_a"])
    print("   fecha_corte     : %s" % fila["fecha_corte"])
    print("   CIFRA clausulas de verificacion: %d" % len(fila["verificacion"]))
    for k, v in enumerate(fila["verificacion"], 1):
        print("      V%d %s" % (k, v))
    print("")

    print("B) LOS TRES PUNTOS DEL ARREGLO, BUSCADOS EN EL ARBOL DE HOY")
    puestos = 0
    for etiqueta, ruta, marca in MARCAS:
        p = os.path.join(RAIZ, ruta.replace("/", os.sep))
        texto = io.open(p, encoding="utf-8").read() if os.path.exists(p) else ""
        hay = marca in texto
        puestos += 1 if hay else 0
        print("   %-46s %s   (%s)"
              % (etiqueta, "PUESTO" if hay else "NO PUESTO", ruta))
    print("   CIFRA puntos del arreglo ya puestos: %d de %d" % (puestos, len(MARCAS)))
    print("")

    print("C) LAS TRES PRUEBAS DE LA VERIFICACION, BUSCADAS EN LA SUITE")
    escritas = 0
    for etiqueta, ruta, marca in PRUEBAS:
        p = os.path.join(RAIZ, ruta.replace("/", os.sep))
        texto = io.open(p, encoding="utf-8").read() if os.path.exists(p) else ""
        hay = marca in texto
        escritas += 1 if hay else 0
        print("   %-46s %s   (%s)"
              % (etiqueta, "ESCRITA" if hay else "NO ESCRITA", ruta))
    print("   CIFRA pruebas ya escritas: %d de %d" % (escritas, len(PRUEBAS)))
    print("")

    print("D) EL COMMIT DE CADA MARCA, LEIDO DE GIT Y NO SUPUESTO")
    commits = set()
    for etiqueta, ruta, marca in MARCAS + PRUEBAS:
        out = git("log", "--oneline", "-S", marca, "--", ruta)
        primera = out.split("\n")[0] if out else "(ninguno)"
        if out:
            commits.add(primera.split()[0])
        print("   %-46s %s" % (etiqueta, primera[:90]))
    print("   CIFRA commits distintos que introdujeron las marcas: %d" % len(commits))
    for c in sorted(commits):
        print("      %s  %s" % (c, git("log", "-1", "--format=%ad  %s",
                                       "--date=short", c)[:100]))
    print("")

    print("E) LA HISTORIA DE LA FILA EN EL REGISTRO, LEIDA DE GIT")
    nac = git("log", "--diff-filter=A", "--format=%h %ad %s", "--date=short",
              "--", "docs/plan/OPERACIONES.jsonl")
    print("   commit que anadio el fichero: %s" % (nac.split("\n")[-1][:100] if nac else "(ninguno)"))
    hist = git("log", "--format=%h %ad", "--date=short", "-S", '"id_op": "OP-C-01"',
               "--", "docs/plan/OPERACIONES.jsonl")
    print("   commits que tocaron el texto del id de la ficha:")
    for l in (hist.split("\n") if hist else []):
        print("      %s" % l)
    est = git("log", "--format=%h %ad", "--date=short", "-S",
              '"OP-S-01",\n    "OP-S-09"', "--", "docs/plan/OPERACIONES.jsonl")
    print("")

    print("F) EL VEREDICTO DE ESTA MEDICION, SIN ADORNO")
    print("   la ficha dice estado %s." % fila["estado"])
    print("   el arreglo esta puesto en %d de %d sitios." % (puestos, len(MARCAS)))
    print("   las pruebas estan escritas en %d de %d." % (escritas, len(PRUEBAS)))
    if puestos == len(MARCAS) and escritas == len(PRUEBAS):
        print("   O SEA: EL ARREGLO YA ESTA HECHO Y LAS PRUEBAS YA ESTAN ESCRITAS,")
        print("   Y LA FICHA SIGUE EN %s. La clausula V5 de la propia ficha"
              % fila["estado"])
        print("   ('ninguna prueba nueva pasa verde ANTES del arreglo') NO SE PUEDE")
        print("   CUMPLIR HOY: no hay codigo sin arreglar sobre el que estrenarlas.")
    else:
        print("   O SEA: queda arreglo por poner y la ficha se puede ejecutar.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
