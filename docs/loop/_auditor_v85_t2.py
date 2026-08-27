# -*- coding: utf-8 -*-
"""AUDITOR, vuelta 85. Las tres aristas de la TAREA 2 en las dos vistas, con
los pares LEIDOS del fichero de salida del ejecutor (ninguno tecleado), y el
campo `arista` de esos tres pares en el PASO_NODO_CALIBRADO.jsonl de la
vuelta 84 (para medir si "ya habian salido de sin arista" era cierto).

  python docs/loop/_auditor_v85_t2.py > docs/loop/_auditor_v85_t2.txt
"""
import json
import re
import subprocess

GRAFO = "dataset/metadata/master_graph.json"
SAL = "docs/loop/SALIDA_V85_TAREA2_ESCRIBIR.txt"
CAL = "docs/plan/PASO_NODO_CALIBRADO.jsonl"

pares = []
for linea in open(SAL, encoding="utf-8"):
    m = re.match(r"ARISTA ESCRITA \([^)]*\): (\S+) -> (\S+)", linea.strip())
    if m:
        pares.append((m.group(1), m.group(2)))

nodos = json.load(open(GRAFO, encoding="utf-8"))["nodos"]
print("pares leidos del fichero: %d" % len(pares))
for a, b in pares:
    s = b in (nodos.get(a, {}).get("nodos_siguientes") or [])
    p = a in (nodos.get(b, {}).get("nodos_previos") or [])
    invs = a in (nodos.get(b, {}).get("nodos_siguientes") or [])
    invp = b in (nodos.get(a, {}).get("nodos_previos") or [])
    print("  %s -> %s | en_sig_madre %s en_prev_hijo %s | INVERSAS %s/%s"
          % (a, b, s, p, invs, invp))

print()
print("--- el campo `arista` de los tres pares de la TAREA 3 de la vuelta 84,")
print("    en el PASO_NODO_CALIBRADO.jsonl COMMITEADO por la vuelta 84 ---")
crudo = subprocess.run(["git", "show", "2d75140e:%s" % CAL], capture_output=True)
cal84 = [json.loads(l) for l in crudo.stdout.decode("utf-8").splitlines() if l.strip()]
print("    filas del CAL de la vuelta 84: %d | sin arista: %d | con arista: %d"
      % (len(cal84), sum(1 for r in cal84 if not r.get("arista")),
         sum(1 for r in cal84 if r.get("arista"))))
V84_T3 = [("gate5_go_to_launch", "plan_de_lanzamiento_al_mercado"),
          ("descubrir_necesidades_del_cliente", "necesidades_psicologicas_cliente"),
          ("mix_medios_marketing_franquicia", "presupuesto_marketing_franquicia")]
idx84 = {(r["madre"], r["hijo"]): r for r in cal84}
for par in V84_T3 + pares:
    r = idx84.get(par)
    print("    %-100s arista=%s" % ("%s -> %s" % par,
                                    None if r is None else r.get("arista")))

print()
print("--- los mismos pares en el PASO_NODO_CALIBRADO.jsonl de HOY (vuelta 85) ---")
cal85 = [json.loads(l) for l in open(CAL, encoding="utf-8") if l.strip()]
idx85 = {(r["madre"], r["hijo"]): r for r in cal85}
for par in V84_T3 + pares:
    r = idx85.get(par)
    print("    %-100s arista=%s" % ("%s -> %s" % par,
                                    None if r is None else r.get("arista")))
