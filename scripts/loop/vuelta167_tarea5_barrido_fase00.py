# -*- coding: utf-8 -*-
r"""vuelta167_tarea5_barrido_fase00.py . LA FASE 00_CODIGO ENTERA CONTRA SU
HISTORIA EN GIT (TAREA 5 de la vuelta 167).

POR QUE NACE. Al medir `OP-C-01` antes de ejecutarla resulto que su arreglo YA
ESTABA PUESTO en el arbol desde el commit `8b2ba536`, con sus pruebas escritas y
su rojo previo sellado, y su ficha sigue en `LISTA`. Una desviacion asi no se
publica sobre UNA fila sin mirar si sus hermanas estan igual: si la especie es
general, el orden de la campana entero se apoya en estados que no describen el
arbol. `EJECUTOR.md` 9 lo dice para las perdidas y vale igual aqui: una
afirmacion sobre el registro se re verifica contra la realidad.

QUE MIDE, TODO DE GIT Y DEL REGISTRO:
  para CADA operacion de la fase `00_CODIGO`, su estado escrito y si existe en
  la rama un commit cuyo asunto la nombre junto a la palabra `EJECUTADA`.

CERO ESCRITURAS: solo imprime.

USO:  python scripts/loop/vuelta167_tarea5_barrido_fase00.py
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


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    filas = [json.loads(l) for l in io.open(OPS, encoding="utf-8") if l.strip()]
    fase = [f for f in filas if f.get("fase") == "00_CODIGO"]
    fase.sort(key=lambda f: (f.get("orden") or 0))

    print("=" * 78)
    print("VUELTA 167, TAREA 5: LA FASE 00_CODIGO CONTRA SU HISTORIA EN GIT")
    print("=" * 78)
    print("")
    print("A) EL CENSO DE LA FASE, CONTADO DEL FICHERO")
    print("   CIFRA filas del registro entero: %d" % len(filas))
    print("   CIFRA filas de la fase 00_CODIGO: %d" % len(fase))
    reparto = {}
    for f in fase:
        reparto[f["estado"]] = reparto.get(f["estado"], 0) + 1
    print("   reparto por estado: %s" % dict(sorted(reparto.items())))
    print("")

    print("B) CADA UNA CONTRA GIT: hay commit que la nombre con EJECUTADA?")
    print("")
    print("   %-10s %-6s %-8s %s" % ("id_op", "orden", "estado", "commit que la declara EJECUTADA"))
    desvios = []
    for f in fase:
        out = git("log", "--oneline", "--all", "--grep", "%s EJECUTADA" % f["id_op"])
        primera = out.split("\n")[0] if out else ""
        print("   %-10s %-6s %-8s %s"
              % (f["id_op"], f.get("orden"), f["estado"],
                 primera[:70] if primera else "(ninguno)"))
        if primera and f["estado"] != "HECHA":
            desvios.append((f["id_op"], f["estado"], primera.split()[0]))
    print("")

    print("C) LOS DESVIOS, SI LOS HAY: estado del registro contra historia del arbol")
    print("   CIFRA operaciones de la fase con commit de EJECUTADA y estado distinto")
    print("   de HECHA: %d" % len(desvios))
    for idop, est, sha in desvios:
        print("      %s: registro dice %s, y %s dice ejecutada el %s"
              % (idop, est, sha, git("log", "-1", "--format=%ad", "--date=short", sha)))
    print("")
    print("D) EL PRECEDENTE ESCRITO, BUSCADO ANTES DE LLAMARLO HALLAZGO NUEVO")
    print("   `EJECUTOR.md` 9: una afirmacion sobre el registro se re verifica, y")
    print("   una busqueda negativa no se puede citar. Asi que antes de publicar")
    print("   esto como novedad, se busca si YA ESTA DECLARADO en la casa.")
    pend = os.path.join(RAIZ, "docs", "PENDIENTES.md")
    lineas = io.open(pend, encoding="utf-8").read().split("\n")
    aguja = "FASE 0, OP-X EJECUTADA"
    hits = [i for i, l in enumerate(lineas, 1) if aguja in l]
    print("   CIFRA lineas de docs/PENDIENTES.md que citan la sede del commit: %d"
          % len(hits))
    for i in hits:
        for j in range(max(1, i - 6), min(len(lineas), i + 3) + 1):
            print("      PENDIENTES.md:%d| %s" % (j, lineas[j - 1]))
    print("")

    print("E) LO QUE ESTA MEDICION NO HACE")
    print("   NO mueve ni un estado, NO edita el registro y NO adjudica nada.")
    print("   Solo pone el registro y el arbol uno al lado del otro.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
