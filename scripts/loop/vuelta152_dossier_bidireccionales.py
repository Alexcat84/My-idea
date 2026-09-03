# -*- coding: utf-8 -*-
"""VUELTA 152, TAREA 6.b: EL DOSSIER DE LECTURA DE LOS PARES BIDIRECCIONALES
SIN VEREDICTO.

IMPRIME, PARA CADA PAR, LO QUE LA VARA DEL BANCO 9.22 NECESITA Y NADA MAS: el
titulo y los pasos accionables de los dos nodos, mas EN QUE LISTA vive cada
direccion. No adjudica: la adjudicacion es lectura y se escribe a mano en
docs/plan/LECTURAS_DIRIGIDAS.md.

LA VARA, CITADA Y NO PARAFRASEADA (banco 9.22, LOS DOS POLOS):
  PROCEDIMIENTO en los DOS sentidos sobre DOS LINEAS DISTINTAS -> clase C,
    ENLACE MUTUO: las dos aristas se quedan.
  LINEA en los DOS sentidos -> clase A, FUSION.
  Procedimiento en UN solo sentido -> el par CONTINUA, no es esta figura.
Y la comprobacion que la separa de la duplicacion: si las dos direcciones
apuntan A LA MISMA LINEA, no es enlace mutuo, es un solape.

USO:
  python scripts/loop/vuelta152_dossier_bidireccionales.py --desde 0 --hasta 40
"""
import argparse
import io
import json
import os
import subprocess

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
GRAFO = os.path.join(RAIZ, "dataset", "metadata", "master_graph.json")

sub = subprocess.run(["python", os.path.join("scripts", "loop",
                                             "vuelta152_registro_de_citas_opc05.py")],
                     capture_output=True, cwd=RAIZ)
salida = sub.stdout.decode("utf-8", "replace")
pares = []
dentro = False
for linea in salida.splitlines():
    if linea.startswith("LOS PARES SIN VEREDICTO"):
        dentro = True
        continue
    if dentro and linea.startswith("="):
        continue
    if dentro and " <-> " in linea:
        izq, der = linea.split(" <-> ", 1)
        pares.append((izq.strip(), der.split("  [")[0].strip()))

N = json.load(io.open(GRAFO, encoding="utf-8"))["nodos"]

ap = argparse.ArgumentParser()
ap.add_argument("--desde", type=int, default=0)
ap.add_argument("--hasta", type=int, default=40)
args = ap.parse_args()

print("PARES SIN VEREDICTO EN TOTAL: %d. ESTE DOSSIER CUBRE [%d, %d)."
      % (len(pares), args.desde, args.hasta))
print("")


def pinta(nid, otro):
    n = N.get(nid) or {}
    pasos = n.get("pasos_accionables") or []
    print("  %s" % nid)
    print("    titulo: %s" % (n.get("titulo_concepto") or "(sin titulo)"))
    print("    dominio: %s | pasos: %d" % (n.get("dominio"), len(pasos)))
    en_sig = otro in (n.get("nodos_siguientes") or [])
    en_prev = otro in (n.get("nodos_previos") or [])
    print("    cablea a %s en: %s%s" % (otro, "nodos_siguientes " if en_sig else "",
                                        "nodos_previos" if en_prev else ""))
    for i, p in enumerate(pasos, 1):
        t = p if isinstance(p, str) else json.dumps(p, ensure_ascii=False)
        print("      %2d. %s" % (i, t[:300]))


for k in range(args.desde, min(args.hasta, len(pares))):
    a, b = pares[k]
    print("=" * 96)
    print("PAR %d de %d:  %s  <->  %s" % (k + 1, len(pares), a, b))
    print("=" * 96)
    pinta(a, b)
    print("")
    pinta(b, a)
    print("")
