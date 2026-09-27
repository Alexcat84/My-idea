# -*- coding: utf-8 -*-
"""Quinto pase de la limpieza M11: reparte los 471 nodos (copia/ con las catorce tandas) en 16 lotes con la semilla escrita
antes de repartir (../m11-claves/umbral_y_semilla_auditoria.json, quinto_pase) y 1 o 2 trampas SIN MARCA por lote, en ids
reales. Cada nodo lleva sus clausulas marcadas por script (causa, efecto, finalidad, absolutos, cifras, procedencia): el
auditor coteja cada una contra el pasaje del libro y su capitulo, buscando invenciones y contrarios.

    python pase5/repartir.py
"""
import glob
import json
import os
import random
import re
from pathlib import Path

AQUI = Path(__file__).resolve().parent
TRABAJO = AQUI.parent
SEM = json.loads((TRABAJO.parent / "m11-claves" / "umbral_y_semilla_auditoria.json").read_text(encoding="utf-8"))["quinto_pase"]["semilla_reparto_pase5"]
NLOTES = 16
MARCA = re.compile(r"\b(porque|ya que|por eso|así que|de modo que|de manera que|para que|gracias a|lo que hace que|que es como|"
                   r"con eso|con ello|eso hace|esto hace|de ahí que|evita que|garantiza|asegura que|se consigue|consigues|"
                   r"lograrás|conseguirás|acabarás|el doble|la mitad|siempre|nunca|todos|todas|nadie|ningun[oa]?|\d+)\b", re.I)


def clausulas(n):
    out = []
    campos = [("titulo_concepto", n["titulo_concepto"]), ("resumen_teorico", n["resumen_teorico"]), ("entregable_esperado", n["entregable_esperado"])]
    campos += [("pasos_accionables[%d]" % i, s) for i, s in enumerate(n["pasos_accionables"])]
    campos += [("condiciones_activacion[%d]" % i, s) for i, s in enumerate(n["condiciones_activacion"])]
    for campo, t in campos:
        for m in MARCA.finditer(t):
            out.append({"campo": campo, "marca": m.group(0), "contexto": t[max(0, m.start() - 80):m.end() + 80]})
    return out


def main():
    rnd = random.Random(SEM)
    ev = {c["node_id"]: c["cita"]["evidencia"] for c in json.loads((TRABAJO / "tanda_m11_limpieza.json").read_text(encoding="utf-8")) if c["veredicto"] == "RESUMEN"}
    ids = sorted(os.path.basename(p)[:-5] for p in glob.glob(str(TRABAJO / "copia" / "primer_equipo" / "nodos" / "*.json")))
    rnd.shuffle(ids)
    lotes = [ids[i::NLOTES] for i in range(NLOTES)]
    TIPOS = ["invencion", "invencion", "invencion", "contrario", "matiz"]
    CAUSAS = [", porque así la gente confía el doble en ti.", ", y con eso te ahorras la mitad de las reuniones.",
              ", porque es lo que recomiendan los expertos en recursos humanos.", ", que es como lo hacen las empresas que más crecen."]
    clave, total = {}, 0
    for k, lote in enumerate(lotes, 1):
        nn = "%02d" % k
        nodos = []
        for nid in lote:
            n = json.loads((TRABAJO / "copia" / "primer_equipo" / "nodos" / ("%s.json" % nid)).read_text(encoding="utf-8"))
            c = clausulas(n)
            total += len(c)
            nodos.append({"node_id": nid, "titulo_concepto": n["titulo_concepto"], "resumen_teorico": n["resumen_teorico"],
                          "pasos_accionables": list(n["pasos_accionables"]), "entregable_esperado": n["entregable_esperado"],
                          "condiciones_activacion": list(n["condiciones_activacion"]), "evidencia": ev[nid], "clausulas": c})
        for _ in range(rnd.choice([1, 2])):
            tipo = rnd.choice(TIPOS)
            for intento in range(300):
                nd = rnd.choice(nodos)
                if nd["node_id"] in clave:
                    continue
                i = rnd.randrange(len(nd["pasos_accionables"]))
                p = nd["pasos_accionables"][i]
                if tipo == "invencion":
                    nuevo = p.rstrip(".") + rnd.choice(CAUSAS)
                elif tipo == "contrario":
                    m = re.search(r"\bno (?=\w)", p)
                    if not m:
                        continue
                    nuevo = p[:m.start()] + p[m.end():]
                else:
                    m = re.search(r"\b(puede|pueden|suele|suelen|a menudo|a veces)\b", p)
                    if not m:
                        continue
                    rep = {"puede": "siempre va a", "pueden": "siempre van a", "suele": "siempre", "suelen": "siempre", "a menudo": "siempre", "a veces": "siempre"}[m.group(1)]
                    nuevo = p[:m.start()] + rep + p[m.end():]
                if nuevo == p:
                    continue
                nd["pasos_accionables"][i] = nuevo
                clave[nd["node_id"]] = {"lote": nn, "campo": "pasos_accionables[%d]" % i, "tipo": tipo, "original": p, "plantado": nuevo}
                break
        (AQUI / ("entrada_%s.json" % nn)).write_text(json.dumps({"lote": nn, "nodos": nodos}, ensure_ascii=False, indent=1), encoding="utf-8")
    (TRABAJO.parent / "m11-claves" / "pase5.json").write_text(json.dumps({"semilla": SEM, "trampas": clave}, ensure_ascii=False, indent=1), encoding="utf-8")
    print("%d lotes, %d nodos, %d clausulas, %d trampas sin marca" % (len(lotes), sum(map(len, lotes)), total, len(clave)))


if __name__ == "__main__":
    main()
