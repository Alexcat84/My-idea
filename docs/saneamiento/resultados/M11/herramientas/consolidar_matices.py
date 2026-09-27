# -*- coding: utf-8 -*-
"""Cierra el PASE DE MATICES de la limpieza M11.

    python consolidar_matices.py puntuar         trampas cazadas por los lectores de matices
    python consolidar_matices.py arbitro NN      arma matices/arbitro_entrada_NN.json con los FALLA reales del lote NN
    python consolidar_matices.py ajustes         pasa las decisiones del arbitro a ajustes_orquestador.json

Cada FALLA real va al arbitro con el texto actual, la objecion del lector, su propuesta y la evidencia. El texto que
decide el arbitro entra como AJUSTE del orquestador sobre el texto final de la tanda m11-limpieza (consolidar.py tanda
lo recoge), con su motivo: "pase de matices: <tipo>: <motivo del arbitro>".
"""
import glob
import json
import sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
M = AQUI / "matices"
CLAVE = Path(r"C:\Users\AlexDesk\AppData\Local\Temp\claude\c--Users-AlexDesk-Documents-I-have-an-idea\35709856-d3a7-4f79-ad7e-c0e77323cd47\scratchpad\clave_trampas_matices.json")


def clave_item(it):
    # los resumenes van por node_id; los demas ya traen "nid|campo[i]"
    return it if "|" in it else "%s|resumen_teorico" % it


def puntuar():
    clave = json.loads(CLAVE.read_text(encoding="utf-8"))
    cazadas, total = 0, 0
    for item in sorted(clave["trampas"]):
        nn = item.split("_")[1]
        p = M / ("salida_%s.json" % nn)
        if not p.exists():
            continue
        total += 1
        r = next((x for x in json.loads(p.read_text(encoding="utf-8"))["items"] if x["item"] == item), None)
        if r and r["veredicto"] == "FALLA":
            cazadas += 1
        else:
            print("  el lector NO cazo", item)
    print("TRAMPAS DEL PASE DE MATICES (cazadas / plantadas): %d/%d" % (cazadas, total))


def arbitro(nn):
    e = {i["item"]: i for i in json.loads((M / ("entrada_%s.json" % nn)).read_text(encoding="utf-8"))["items"]}
    s = json.loads((M / ("salida_%s.json" % nn)).read_text(encoding="utf-8"))
    casos = []
    for r in s["items"]:
        if r["veredicto"] != "FALLA" or r["item"].startswith("mtrampa_"):
            continue
        casos.append(dict(e[r["item"]], tipo=r.get("tipo"), objecion=r.get("motivo"), propuesta_lector=r.get("propuesta")))
    (M / ("arbitro_entrada_%s.json" % nn)).write_text(json.dumps({"lote": nn, "casos": casos}, ensure_ascii=False, indent=1), encoding="utf-8")
    print("matices %s: %d casos al arbitro" % (nn, len(casos)))


def ajustes():
    p = AQUI / "ajustes_orquestador.json"
    aj = json.loads(p.read_text(encoding="utf-8"))
    por = {a["item"]: a for a in aj["ajustes"]}
    n = 0
    for f in sorted(glob.glob(str(M / "arbitro_salida_*.json"))):
        for c in json.loads(Path(f).read_text(encoding="utf-8"))["casos"]:
            if c["decision"] == "actual":
                continue
            k = clave_item(c["item"])
            motivo = "pase de matices (%s): %s" % (c.get("tipo") or "", c.get("motivo", ""))
            if k in por:
                por[k]["texto_final"] = c["texto_final"]
                por[k]["motivo"] += "; " + motivo
            else:
                por[k] = {"item": k, "texto_final": c["texto_final"], "motivo": motivo}
                aj["ajustes"].append(por[k])
            n += 1
    p.write_text(json.dumps(aj, ensure_ascii=False, indent=1), encoding="utf-8")
    print("ajustes del pase de matices: %d (total de ajustes: %d)" % (n, len(aj["ajustes"])))


if __name__ == "__main__":
    cmd = sys.argv[1]
    if cmd == "puntuar":
        puntuar()
    elif cmd == "arbitro":
        arbitro(sys.argv[2])
    elif cmd == "ajustes":
        ajustes()
