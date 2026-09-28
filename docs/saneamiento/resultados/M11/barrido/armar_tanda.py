# -*- coding: utf-8 -*-
"""Arma la tanda m11-barrido: los calcos que la auditoria completa dejo repetidos ("a que se parece", "abastecer",
"por delante" en el sentido de "up front", "que suban la voz", "ensenar mejora"). Redactor, verificador ciego con una
trampa sin marca (clave en ../m11-claves/barrido.json) y, en los FALLA reales, la decision de barrido/arbitro.json.

    python barrido/armar_tanda.py
"""
import json
from pathlib import Path

AQUI = Path(__file__).resolve().parent
CLAVE = AQUI.parent.parent / "m11-claves" / "barrido.json"
REGLA = ("barrido final de calcos de la limpieza M11 (barrido/INSTRUCCIONES.md; espanol llano, decisiones del fundador "
         "del 28 sep 2026)")


def clave(c):
    return "%s|%s%s" % (c["node_id"], c["campo"], "" if c.get("indice") is None else "[%d]" % c["indice"])


def main():
    trampa = json.loads(CLAVE.read_text(encoding="utf-8"))["trampa"]["item"]
    cambios = json.loads((AQUI / "propuestas.json").read_text(encoding="utf-8"))["cambios"]
    ver = {x["item"]: x for x in json.loads((AQUI / "verificador_salida.json").read_text(encoding="utf-8"))["items"]}
    arb_p = AQUI / "arbitro.json"
    arb = {x["item"]: x for x in json.loads(arb_p.read_text(encoding="utf-8"))["casos"]} if arb_p.exists() else {}
    tanda, faltan = [], []
    for c in cambios:
        k = clave(c)
        v = ver.get(k)
        texto = c["texto_nuevo"]
        if v is None:
            faltan.append("%s sin veredicto" % k)
            continue
        if v["veredicto"] == "FALLA" and k != trampa:
            if k not in arb:
                faltan.append("%s: FALLA sin decision" % k)
                continue
            texto = arb[k]["texto_final"]
        if texto == c["texto_anterior"]:
            continue
        frags = [f for f in c.get("fragmentos") or [] if f and f in c["texto_anterior"] and f not in texto]
        corr = {"id": "m11-barrido-%s-%s" % (c["node_id"], c["campo"] if c.get("indice") is None else "%s-%d" % (c["campo"], c["indice"])),
                "fecha": "2026-09-28", "node_id": c["node_id"], "campo": c["campo"], "veredicto": "VOZ",
                "texto_anterior": c["texto_anterior"], "texto_nuevo": texto,
                "decision": "barrido final de calcos (%s)" % c.get("termino", ""),
                "auditoria": "docs/saneamiento/resultados/M11/barrido/", "motivos": c.get("motivos") or ["ingles"],
                "cita": {"regla": REGLA, "fragmentos": frags or ["(calco: %s)" % c.get("termino", "")]}}
        if c.get("indice") is not None:
            corr["indice"] = c["indice"]
        tanda.append(corr)
    if faltan:
        print("TANDA INCOMPLETA:", *faltan, sep="\n  ")
        return 1
    (AQUI.parent / "tanda_m11_barrido.json").write_text(json.dumps(tanda, ensure_ascii=False, indent=1), encoding="utf-8")
    print("tanda m11-barrido: %d correcciones en %d nodos" % (len(tanda), len({c["node_id"] for c in tanda})))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
