# -*- coding: utf-8 -*-
"""Sexto pase M11 (doble lectura): puntua trampas por lector, arma la entrada del arbitro de cada lote con TODO lo que
marco cualquiera de los dos lectores (sin las trampas de cada uno) y la tanda m11-pase6.

    python pase6/consolidar.py puntuar
    python pase6/consolidar.py arbitro NN
    python pase6/consolidar.py tanda
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "auditoria"))
import consolidar as base  # noqa: E402

AQUI = Path(__file__).resolve().parent
TRABAJO = AQUI.parent
CLAVE = TRABAJO.parent / "m11-claves" / "pase6.json"
NODOS = TRABAJO / "copia" / "primer_equipo" / "nodos"


def trampas():
    return json.loads(CLAVE.read_text(encoding="utf-8"))["trampas"]


def es_trampa(t, lote, lector, nid, d):
    x = t.get("%s%s|%s" % (lote, lector, nid))
    return x is not None and x["campo"] == d["campo"] and (d.get("cita") or "") not in x["original"]


def puntuar():
    t = trampas()
    caz = 0
    for k, x in sorted(t.items()):
        s = {n["node_id"]: n for n in json.loads((AQUI / ("salida_%s%s.json" % (x["lote"], x["lector"]))).read_text(encoding="utf-8"))["nodos"]}
        if any(d["campo"] == x["campo"] for d in s.get(x["node_id"], {}).get("defectos", [])):
            caz += 1
        else:
            print("  NO cazada:", k, x["campo"], x["tipo"])
    print("TRAMPAS SIN MARCA DE LA DOBLE LECTURA: %d/%d" % (caz, len(t)))


def arbitro(nn):
    t = trampas()
    campos, marcas = {}, {"A": 0, "B": 0, "ambos": 0}
    por_lector = {}
    for lector in ("A", "B"):
        for n in json.loads((AQUI / ("salida_%s%s.json" % (nn, lector))).read_text(encoding="utf-8"))["nodos"]:
            nid = n["node_id"]
            nodo = json.loads((NODOS / ("%s.json" % nid)).read_text(encoding="utf-8"))
            for d in n.get("defectos", []):
                if es_trampa(t, nn, lector, nid, d):
                    continue
                k = (nid, d["campo"])
                por_lector.setdefault(k, set()).add(lector)
                if k not in campos:
                    campos[k] = {"node_id": nid, "campo": d["campo"], "actual": base.texto(nodo, d["campo"]), "defectos": [],
                                 "contexto": {x: nodo[x] for x in ("titulo_concepto", "resumen_teorico", "pasos_accionables", "entregable_esperado", "condiciones_activacion")}}
                campos[k]["defectos"].append(dict(d, lector=lector))
    for k, ls in por_lector.items():
        campos[k]["marcado_por"] = sorted(ls)
        marcas["ambos" if len(ls) == 2 else next(iter(ls))] += 1
    (AQUI / ("arbitro_entrada_%s.json" % nn)).write_text(json.dumps({"lote": nn, "campos": list(campos.values())}, ensure_ascii=False, indent=1), encoding="utf-8")
    print("doble lectura %s: %d campos al arbitro (solo A %d, solo B %d, ambos %d)" % (nn, len(campos), marcas["A"], marcas["B"], marcas["ambos"]))


if __name__ == "__main__":
    cmd = sys.argv[1]
    if cmd == "puntuar":
        puntuar()
    elif cmd == "arbitro":
        arbitro(sys.argv[2])
    else:
        base.NODOS = NODOS
        raise SystemExit(base.tanda(str(AQUI / "arbitro_salida_*.json"), "tanda_m11_pase6.json", "m11-pase6"))
