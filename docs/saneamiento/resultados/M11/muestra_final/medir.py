# -*- coding: utf-8 -*-
"""Mide la muestra ciega final contra el umbral del fundador (28 sep 2026).

    python muestra_final/medir.py arbitro     arma muestra_final/arbitro_entrada.json con los defectos reales (sin las trampas)
    python muestra_final/medir.py medir       cuenta los defectos CONFIRMADOS por el arbitro y los compara con el umbral

Cuenta solo lo que el arbitro confirma contra el libro. Umbral en 50 nodos: invencion 0, contrario 0; el resto
(matiz, calco, coherencia, regionalismo, voz, ortografia) como maximo 10.
"""
import json
import re
import sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
CLAVE = AQUI.parent.parent / "m11-claves" / "muestra_final.json"
NODOS = AQUI.parent / "copia" / "primer_equipo" / "nodos"


def texto(n, campo):
    m = re.match(r"(\w+)(?:\[(\d+)\])?$", campo)
    v = n[m.group(1)]
    return v if m.group(2) is None else v[int(m.group(2))]


def trampas():
    return json.loads(CLAVE.read_text(encoding="utf-8"))["trampas"]


def arbitro():
    t = trampas()
    campos, cazadas = {}, 0
    for lote in ("F1", "F2"):
        for n in json.loads((AQUI / ("salida_%s.json" % lote)).read_text(encoding="utf-8"))["nodos"]:
            nid = n["node_id"]
            nodo = json.loads((NODOS / ("%s.json" % nid)).read_text(encoding="utf-8"))
            for d in n.get("defectos", []):
                if nid in t and t[nid]["campo"] == d["campo"] and (d.get("cita") or "") not in t[nid]["original"]:
                    cazadas += 1
                    continue
                k = (nid, d["campo"])
                campos.setdefault(k, {"node_id": nid, "campo": d["campo"], "actual": texto(nodo, d["campo"]), "defectos": [],
                                      "contexto": {x: nodo[x] for x in ("titulo_concepto", "resumen_teorico", "pasos_accionables", "entregable_esperado", "condiciones_activacion")}})
                campos[k]["defectos"].append(d)
    (AQUI / "arbitro_entrada.json").write_text(json.dumps({"lote": "final", "campos": list(campos.values())}, ensure_ascii=False, indent=1), encoding="utf-8")
    print("trampas sin marca cazadas: %d/%d; %d campos al arbitro (%d defectos)" % (cazadas, len(t), len(campos), sum(len(c["defectos"]) for c in campos.values())))


def medir():
    s = json.loads((AQUI / "arbitro_salida.json").read_text(encoding="utf-8"))
    duros, blandos, detalle = 0, 0, []
    for c in s["campos"]:
        if c["decision"] != "corregido":
            continue
        tipos = set(c.get("tipos") or [])
        # lectura estricta: cada tipo confirmado en un campo cuenta como un defecto
        duros += len(tipos & {"invencion", "contrario"})
        blandos += len(tipos - {"invencion", "contrario"}) or (0 if tipos & {"invencion", "contrario"} else 1)
        detalle.append("%s %s %s" % (c["node_id"], c["campo"], sorted(tipos)))
    print("\n".join(detalle))
    ok = duros == 0 and blandos <= 10
    print("CONFIRMADOS: invencion+contrario %d (umbral 0); matiz+calco+coherencia+resto %d (umbral 10) -> %s" % (duros, blandos, "CUMPLE" if ok else "NO CUMPLE"))
    return 0 if ok else 1


if __name__ == "__main__":
    if sys.argv[1] == "arbitro":
        arbitro()
    else:
        raise SystemExit(medir())
