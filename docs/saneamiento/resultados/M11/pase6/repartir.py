# -*- coding: utf-8 -*-
"""Sexto pase de la limpieza M11, DOBLE LECTURA (decision del fundador, 28 sep 2026): reparte los 471 nodos (copia/ con
las dieciseis tandas) en 16 lotes con la semilla escrita antes de repartir (../m11-claves/umbral_y_semilla_auditoria.json,
sexto_pase). Cada lote tiene dos entradas, A y B, para dos auditores independientes, cada una con sus propias trampas SIN
MARCA en ids reales (1 o 2 por entrada, en nodos distintos de las de la otra lectura). Sin listas de clausulas: la
entrada solo lleva el texto del nodo y su evidencia.

    python pase6/repartir.py
"""
import glob
import json
import os
import random
import re
from pathlib import Path

AQUI = Path(__file__).resolve().parent
TRABAJO = AQUI.parent
SEM = json.loads((TRABAJO.parent / "m11-claves" / "umbral_y_semilla_auditoria.json").read_text(encoding="utf-8"))["sexto_pase"]["semilla_reparto_pase6"]
NLOTES = 16
CAUSAS = [", porque así se evita la mayoría de los conflictos del equipo.", ", que es lo que hacen las empresas con menos rotación.",
          ", y con ello la persona gana confianza en pocas semanas.", ", porque la gente valora más la rapidez que la calidad."]


def plantar(rnd, nodos, usados, lote, lector, clave):
    for _ in range(rnd.choice([1, 2])):
        tipo = rnd.choice(["invencion", "invencion", "contrario"])
        for intento in range(300):
            nd = rnd.choice(nodos)
            if nd["node_id"] in usados:
                continue
            i = rnd.randrange(len(nd["pasos_accionables"]))
            p = nd["pasos_accionables"][i]
            otros = [nd["titulo_concepto"], nd["resumen_teorico"], nd["entregable_esperado"]] + \
                    [q for j, q in enumerate(nd["pasos_accionables"]) if j != i] + nd["condiciones_activacion"]
            if any(p in t for t in otros):
                continue  # el texto original sigue visible en otro campo del nodo y delataria la trampa
            if tipo == "invencion":
                nuevo = p.rstrip(".") + rnd.choice(CAUSAS)
            else:
                m = re.search(r"\bno (?=\w)", p)
                if not m:
                    continue
                nuevo = p[:m.start()] + p[m.end():]
                nuevo = nuevo[0].upper() + nuevo[1:]
            if nuevo == p:
                continue
            nd["pasos_accionables"][i] = nuevo
            usados.add(nd["node_id"])
            clave["%s%s|%s" % (lote, lector, nd["node_id"])] = {"lote": lote, "lector": lector, "node_id": nd["node_id"],
                                                                "campo": "pasos_accionables[%d]" % i, "tipo": tipo, "original": p, "plantado": nuevo}
            break


def main():
    rnd = random.Random(SEM)
    ev = {c["node_id"]: c["cita"]["evidencia"] for c in json.loads((TRABAJO / "tanda_m11_limpieza.json").read_text(encoding="utf-8")) if c["veredicto"] == "RESUMEN"}
    ids = sorted(os.path.basename(p)[:-5] for p in glob.glob(str(TRABAJO / "copia" / "primer_equipo" / "nodos" / "*.json")))
    rnd.shuffle(ids)
    lotes = [ids[i::NLOTES] for i in range(NLOTES)]
    clave = {}
    for k, lote in enumerate(lotes, 1):
        nn = "%02d" % k
        usados = set()
        for lector in ("A", "B"):
            nodos = []
            for nid in lote:
                n = json.loads((TRABAJO / "copia" / "primer_equipo" / "nodos" / ("%s.json" % nid)).read_text(encoding="utf-8"))
                nodos.append({"node_id": nid, "titulo_concepto": n["titulo_concepto"], "resumen_teorico": n["resumen_teorico"],
                              "pasos_accionables": list(n["pasos_accionables"]), "entregable_esperado": n["entregable_esperado"],
                              "condiciones_activacion": list(n["condiciones_activacion"]), "evidencia": ev[nid]})
            plantar(rnd, nodos, usados, nn, lector, clave)
            (AQUI / ("entrada_%s%s.json" % (nn, lector))).write_text(json.dumps({"lote": nn + lector, "nodos": nodos}, ensure_ascii=False, indent=1), encoding="utf-8")
    (TRABAJO.parent / "m11-claves" / "pase6.json").write_text(json.dumps({"semilla": SEM, "trampas": clave}, ensure_ascii=False, indent=1), encoding="utf-8")
    print("%d lotes x 2 lectores, %d nodos, %d trampas sin marca" % (len(lotes), sum(map(len, lotes)), len(clave)))


if __name__ == "__main__":
    main()
