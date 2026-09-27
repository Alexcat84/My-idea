# -*- coding: utf-8 -*-
"""Auditoria completa M11: puntua trampas, arma entradas del arbitro y la tanda m11-auditoria.

    python auditoria/consolidar.py puntuar
    python auditoria/consolidar.py arbitro NN
    python auditoria/consolidar.py tanda
"""
import glob
import json
import re
import sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
TRABAJO = AQUI.parent
CLAVE = TRABAJO.parent / "m11-claves" / "auditoria.json"
NODOS = TRABAJO / "copia" / "primer_equipo" / "nodos"
INSTR = "auditoria completa de la limpieza M11: auditor ciego por nodo con trampas sin marca y arbitro contra el libro (docs/saneamiento/resultados/M11/auditoria/)"
REGLA = "voz de la casa y espanol llano: sin calcos, regionalismos ni voz de libro (docs/saneamiento/instrumentos/M11_LIMPIEZA.md; decisiones del fundador, 28 sep 2026)"


def trampas():
    return json.loads(CLAVE.read_text(encoding="utf-8"))["trampas"]


def puntuar():
    t = trampas()
    caz, tot = 0, 0
    for nid, x in sorted(t.items()):
        p = AQUI / ("salida_%s.json" % x["lote"])
        if not p.exists():
            continue
        tot += 1
        s = {n["node_id"]: n for n in json.loads(p.read_text(encoding="utf-8"))["nodos"]}
        if any(d["campo"] == x["campo"] for d in s.get(nid, {}).get("defectos", [])):
            caz += 1
        else:
            print("  NO cazada:", x["lote"], nid, x["campo"], x["tipo"])
    print("TRAMPAS SIN MARCA DE LA AUDITORIA (cazadas / plantadas en lotes terminados): %d/%d" % (caz, tot))


def texto(n, campo):
    m = re.match(r"(\w+)(?:\[(\d+)\])?$", campo)
    v = n[m.group(1)]
    return v if m.group(2) is None else v[int(m.group(2))]


def arbitro(nn):
    t = trampas()
    s = json.loads((AQUI / ("salida_%s.json" % nn)).read_text(encoding="utf-8"))
    campos = {}
    for n in s["nodos"]:
        nid = n["node_id"]
        nodo = json.loads((NODOS / ("%s.json" % nid)).read_text(encoding="utf-8"))
        for d in n.get("defectos", []):
            if nid in t and t[nid]["campo"] == d["campo"] and (d.get("cita") or "") not in t[nid]["original"]:
                continue  # la trampa: lo que cita solo existe por lo plantado; un defecto real del mismo campo SI pasa
            k = (nid, d["campo"])
            if k not in campos:
                campos[k] = {"node_id": nid, "campo": d["campo"], "actual": texto(nodo, d["campo"]), "defectos": [],
                             "contexto": {"titulo_concepto": nodo["titulo_concepto"], "resumen_teorico": nodo["resumen_teorico"],
                                          "pasos_accionables": nodo["pasos_accionables"], "entregable_esperado": nodo["entregable_esperado"],
                                          "condiciones_activacion": nodo["condiciones_activacion"]}}
            campos[k]["defectos"].append(d)
    (AQUI / ("arbitro_entrada_%s.json" % nn)).write_text(json.dumps({"lote": nn, "campos": list(campos.values())}, ensure_ascii=False, indent=1), encoding="utf-8")
    print("auditoria %s: %d campos al arbitro (%d defectos)" % (nn, len(campos), sum(len(c["defectos"]) for c in campos.values())))


def tanda():
    out, faltan = [], []
    for p in sorted(glob.glob(str(AQUI / "arbitro_salida_*.json"))):
        for c in json.loads(Path(p).read_text(encoding="utf-8"))["campos"]:
            if c["decision"] != "corregido":
                continue
            nodo = json.loads((NODOS / ("%s.json" % c["node_id"])).read_text(encoding="utf-8"))
            ant = texto(nodo, c["campo"])
            if c["texto_final"] == ant:
                continue
            m = re.match(r"(\w+)(?:\[(\d+)\])?$", c["campo"])
            campo, i = m.group(1), (None if m.group(2) is None else int(m.group(2)))
            v = c.get("veredicto")
            corr = {"id": "m11-auditoria-%s-%s" % (c["node_id"], campo if i is None else "%s-%d" % (campo, i)), "fecha": "2026-09-28",
                    "node_id": c["node_id"], "campo": campo, "veredicto": v, "texto_anterior": ant, "texto_nuevo": c["texto_final"],
                    "decision": "auditoria completa M11 (%s): %s" % (", ".join(c.get("tipos") or []), (c.get("motivo") or "")[:700]),
                    "auditoria": "docs/saneamiento/resultados/M11/auditoria/", "motivos": c.get("tipos") or []}
            if i is not None:
                corr["indice"] = i
            if v in ("CONTRARIO", "ANADIDO"):
                if not (c.get("fichero") and c.get("lineas") and c.get("frase")):
                    faltan.append("%s %s: %s sin fichero, lineas o frase" % (c["node_id"], c["campo"], v))
                    continue
                corr["cita"] = {"libro": nodo["fuente"], "lineas": "%s %s" % (c["fichero"], c["lineas"]), "frase": c["frase"]}
            elif v == "VOZ":
                fr = [f for f in c.get("fragmentos") or [] if f and f in ant and f not in c["texto_final"]]
                corr["cita"] = {"regla": REGLA, "fragmentos": fr or ["(texto reescrito: %s)" % ", ".join(c.get("tipos") or [])]}
            elif v in ("COHERENCIA", "ORTOGRAFIA"):
                corr["cita"] = {"instrumento": INSTR, "evidencia": (c.get("motivo") or "auditoria")[:400]}
            else:
                faltan.append("%s %s: veredicto %r" % (c["node_id"], c["campo"], v))
                continue
            out.append(corr)
    if faltan:
        print("TANDA INCOMPLETA:", *faltan[:40], sep="\n  ")
        return 1
    (TRABAJO / "tanda_m11_auditoria.json").write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
    print("tanda m11-auditoria: %d correcciones en %d nodos" % (len(out), len({c["node_id"] for c in out})))
    return 0


if __name__ == "__main__":
    cmd = sys.argv[1]
    if cmd == "puntuar":
        puntuar()
    elif cmd == "arbitro":
        arbitro(sys.argv[2])
    else:
        raise SystemExit(tanda())
