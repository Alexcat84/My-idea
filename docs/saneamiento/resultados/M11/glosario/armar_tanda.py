# -*- coding: utf-8 -*-
"""Arma la tanda m11-glosario (correcciones declaradas) con lo verificado del pase de glosario.

    python glosario/armar_tanda.py

Texto final de cada cambio: el de propuestas_todas.json si el verificador dijo OK; el de glosario/arbitro_salida.json
si dijo FALLA (el arbitro decide). Se aplica DESPUES de la tanda m11-limpieza: texto_anterior es el texto limpio.
"""
import json
from pathlib import Path

AQUI = Path(__file__).resolve().parent
REGLA = ("pase de glosario de la limpieza M11: un concepto, un nombre, en espanol llano y neutro "
         "(glosario/DECISIONES.md, 28 sep 2026; docs/saneamiento/instrumentos/M11_LIMPIEZA.md)")


def clave(c):
    return "%s|%s%s" % (c["node_id"], c["campo"], "" if c.get("indice") is None else "[%d]" % c["indice"])


def main():
    cambios = json.loads((AQUI / "propuestas_todas.json").read_text(encoding="utf-8"))["cambios"]
    ver = {x["item"]: x for x in json.loads((AQUI / "verificador_salida.json").read_text(encoding="utf-8"))["items"]}
    arb_p = AQUI / "arbitro_salida.json"
    arb = {x["item"]: x for x in json.loads(arb_p.read_text(encoding="utf-8"))["casos"]} if arb_p.exists() else {}
    tanda, faltan = [], []
    for c in cambios:
        k = clave(c)
        v = ver.get(k)
        if v is None:
            faltan.append("%s sin veredicto" % k)
            continue
        texto, decision = c["texto_nuevo"], "verificador OK"
        if v["veredicto"] == "FALLA":
            a = arb.get(k)
            if a is None:
                faltan.append("%s: FALLA sin arbitro" % k)
                continue
            texto, decision = a["texto_final"], "arbitro (%s): %s" % (a["decision"], a.get("motivo", ""))
        if texto == c["texto_anterior"]:
            continue
        frags = [f for f in c.get("fragmentos") or [] if f and f in c["texto_anterior"] and f not in texto]
        corr = {"id": "m11-glosario-%s-%s" % (c["node_id"], c["campo"] if c.get("indice") is None else "%s-%d" % (c["campo"], c["indice"])),
                "fecha": "2026-09-28", "node_id": c["node_id"], "campo": c["campo"], "veredicto": "VOZ",
                "texto_anterior": c["texto_anterior"], "texto_nuevo": texto,
                "decision": "pase de glosario (%s): %s" % (c.get("termino", ""), decision),
                "auditoria": "docs/saneamiento/resultados/M11/glosario/", "motivos": c.get("motivos") or ["voz_de_la_casa"],
                "cita": {"regla": REGLA, "fragmentos": frags or ["(termino unificado: %s)" % c.get("termino", "")]}}
        if c.get("indice") is not None:
            corr["indice"] = c["indice"]
        tanda.append(corr)
    if faltan:
        print("TANDA INCOMPLETA:", *faltan[:30], sep="\n  ")
        return 1
    (AQUI.parent / "tanda_m11_glosario.json").write_text(json.dumps(tanda, ensure_ascii=False, indent=1), encoding="utf-8")
    print("tanda m11-glosario: %d correcciones en %d nodos" % (len(tanda), len({c["node_id"] for c in tanda})))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
