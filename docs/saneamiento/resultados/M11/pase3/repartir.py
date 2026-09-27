# -*- coding: utf-8 -*-
"""Tercer pase de la limpieza M11: reparte los 471 nodos (copia/ con las nueve tandas) en 24 lotes con la semilla escrita
antes de repartir (../m11-claves/umbral_y_semilla_auditoria.json, tercer_pase) y 1 o 2 trampas SIN MARCA por lote, en
ids reales. Cada nodo lleva la lista de frases con matiz de su pasaje (las lineas de su evidencia, con dos de margen) y
los avisos mecanicos (resumen fuera de 400 a 600, "y" ante sonido i).

    python pase3/repartir.py
"""
import glob
import json
import os
import random
import re
from pathlib import Path

AQUI = Path(__file__).resolve().parent
TRABAJO = AQUI.parent
LIBROS = Path(r"C:\Users\AlexDesk\Documents\forja-lectura")
SEM = json.loads((TRABAJO.parent / "m11-claves" / "umbral_y_semilla_auditoria.json").read_text(encoding="utf-8"))["tercer_pase"]["semilla_reparto_pase3"]
NLOTES = 24
MATIZ = re.compile(r"\b(can|can't|cannot|could|may|might|often|usually|typically|generally|most|many|some|sometimes|probably|"
                   r"likely|unlikely|tends?|tended|possible|possibly|perhaps|maybe|rarely|seldom|almost|nearly|virtually|"
                   r"frequently|occasionally|seems?|seemed|I've found|I find|I found|in my experience|I see|I saw|I think|"
                   r"I believe|I'd say|for me|my own|I've seen|I've learned|I learned|one of|a few|several|at times|"
                   r"in some|in many|as a rule|more often)\b", re.I)


def frases_con_matiz(ev):
    lineas = open(LIBROS / ev["fichero"], encoding="utf-8").read().splitlines()
    a, _, b = ev["lineas"].partition("-")
    a, b = int(a), int(b or a)
    out = []
    for n in range(max(1, a - 2), min(len(lineas), b + 2) + 1):
        for f in re.split(r"(?<=[.!?])\s+", lineas[n - 1].strip()):
            if MATIZ.search(f):
                out.append({"linea": n, "frase": f})
    return out


def avisos(n):
    a = []
    L = len(n["resumen_teorico"])
    if not 400 <= L <= 600:
        a.append("el resumen_teorico mide %d caracteres (van de 400 a 600)" % L)
    textos = [n["titulo_concepto"], n["resumen_teorico"], n["entregable_esperado"]] + n["pasos_accionables"] + n["condiciones_activacion"]
    for t in textos:
        for m in re.finditer(r"\by (?=h?i[^aeiouáéó])", t, re.I):
            a.append("\"y\" ante sonido i: \"%s\"" % t[max(0, m.start() - 20):m.end() + 12])
    return a


def main():
    rnd = random.Random(SEM)
    ev = {c["node_id"]: c["cita"]["evidencia"] for c in json.loads((TRABAJO / "tanda_m11_limpieza.json").read_text(encoding="utf-8")) if c["veredicto"] == "RESUMEN"}
    ids = sorted(os.path.basename(p)[:-5] for p in glob.glob(str(TRABAJO / "copia" / "primer_equipo" / "nodos" / "*.json")))
    rnd.shuffle(ids)
    lotes = [ids[i::NLOTES] for i in range(NLOTES)]
    TIPOS = ["matiz", "matiz", "matiz", "calco", "coherencia"]
    CALCOS = [("Revisa", "Chequea"), ("Pregunta", "Haz un check de"), ("reunión", "meeting"), ("cuenta", "account")]
    clave, total_frases = {}, 0
    for k, lote in enumerate(lotes, 1):
        nn = "%02d" % k
        nodos = []
        for nid in lote:
            n = json.loads((TRABAJO / "copia" / "primer_equipo" / "nodos" / ("%s.json" % nid)).read_text(encoding="utf-8"))
            fr = frases_con_matiz(ev[nid])
            total_frases += len(fr)
            nodos.append({"node_id": nid, "titulo_concepto": n["titulo_concepto"], "resumen_teorico": n["resumen_teorico"],
                          "pasos_accionables": list(n["pasos_accionables"]), "entregable_esperado": n["entregable_esperado"],
                          "condiciones_activacion": list(n["condiciones_activacion"]), "evidencia": ev[nid],
                          "frases_con_matiz": fr, "avisos": avisos(n)})
        for _ in range(rnd.choice([1, 2])):
            tipo = rnd.choice(TIPOS)
            for intento in range(200):
                nd = rnd.choice(nodos)
                if nd["node_id"] in clave:
                    continue
                i = rnd.randrange(len(nd["pasos_accionables"]))
                p = nd["pasos_accionables"][i]
                if tipo == "matiz":
                    m = re.search(r"\b(puede|pueden|suele|suelen|a menudo|a veces|probablemente|casi siempre|muchas veces|quizá|tal vez)\b", p)
                    if not m:
                        continue
                    rep = {"puede": "va a", "pueden": "van a", "suele": "", "suelen": "", "a menudo": "siempre", "a veces": "siempre",
                           "probablemente": "seguro que", "casi siempre": "siempre", "muchas veces": "siempre", "quizá": "", "tal vez": ""}[m.group(1)]
                    nuevo = re.sub(r"\s{2,}", " ", p[:m.start()] + rep + p[m.end():]).strip()
                    nuevo = nuevo[0].upper() + nuevo[1:]
                elif tipo == "calco":
                    a, b = rnd.choice(CALCOS)
                    if a not in p:
                        continue
                    nuevo = p.replace(a, b, 1)
                else:
                    nuevo = p.rstrip(".") + ", como en el tercer punto de la lista anterior."
                if nuevo == p:
                    continue
                nd["pasos_accionables"][i] = nuevo
                clave[nd["node_id"]] = {"lote": nn, "campo": "pasos_accionables[%d]" % i, "tipo": tipo, "original": p, "plantado": nuevo}
                break
        (AQUI / ("entrada_%s.json" % nn)).write_text(json.dumps({"lote": nn, "nodos": nodos}, ensure_ascii=False, indent=1), encoding="utf-8")
    (TRABAJO.parent / "m11-claves" / "pase3.json").write_text(json.dumps({"semilla": SEM, "trampas": clave}, ensure_ascii=False, indent=1), encoding="utf-8")
    print("%d lotes, %d nodos, %d frases con matiz, %d trampas sin marca" % (len(lotes), sum(map(len, lotes)), total_frases, len(clave)))


if __name__ == "__main__":
    main()
