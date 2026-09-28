# -*- coding: utf-8 -*-
"""Arma la tanda m11-pase4-barrido: los restos de las decisiones del orquestador para todo el pack (cuarto pase) que
quedaron en campos que ningun arbitro tenia en su entrada ("a cargo" sin posesivo, "cien por cien", "video" con tilde,
"un computador"). Propuestas del orquestador, verificador ciego con una trampa sin marca (clave en
../m11-claves/pase4_barrido.json).

    python pase4_barrido/armar_tanda.py
"""
import json
import re
from pathlib import Path

AQUI = Path(__file__).resolve().parent
CLAVE = AQUI.parent.parent / "m11-claves" / "pase4_barrido.json"
REGLA = ("voz de la casa y espanol neutro: forma fijada 'a tu cargo' / 'a su cargo' y formas de una sola region a la "
         "neutra (decisiones del orquestador para todo el pack, cuarto pase de la limpieza M11, 28 sep 2026)")
INSTR = "barrido de restos del cuarto pase de la limpieza M11 con verificador ciego (docs/saneamiento/resultados/M11/pase4_barrido/)"


def main():
    trampa = json.loads(CLAVE.read_text(encoding="utf-8"))["trampa"]["item"]
    cambios = json.loads((AQUI / "propuestas.json").read_text(encoding="utf-8"))["cambios"]
    ver = {x["item"]: x for x in json.loads((AQUI / "verificador_salida.json").read_text(encoding="utf-8"))["items"]}
    tanda, faltan = [], []
    for c in cambios:
        k = "%s|%s" % (c["node_id"], c["campo"])
        v = ver.get(k)
        if v is None:
            faltan.append("%s sin veredicto" % k)
            continue
        if v["veredicto"] == "FALLA" and k != trampa:
            faltan.append("%s: FALLA real, decidir" % k)
            continue
        m = re.match(r"(\w+)(?:\[(\d+)\])?$", c["campo"])
        campo, i = m.group(1), (None if m.group(2) is None else int(m.group(2)))
        corr = {"id": "m11-pase4-barrido-%s-%s" % (c["node_id"], campo if i is None else "%s-%d" % (campo, i)),
                "fecha": "2026-09-28", "node_id": c["node_id"], "campo": campo, "veredicto": c["veredicto"],
                "texto_anterior": c["texto_anterior"], "texto_nuevo": c["texto_nuevo"], "decision": c["decision"],
                "auditoria": "docs/saneamiento/resultados/M11/pase4_barrido/", "motivos": [c["motivo"]]}
        if i is not None:
            corr["indice"] = i
        if c["veredicto"] == "VOZ":
            corr["cita"] = {"regla": REGLA, "fragmentos": [c["fragmento"]]}
        else:
            corr["cita"] = {"instrumento": INSTR, "evidencia": "'%s' se lee como quien manda; forma fijada 'a tu cargo' / 'a su cargo'" % c["fragmento"]}
        tanda.append(corr)
    if faltan:
        print("TANDA INCOMPLETA:", *faltan, sep="\n  ")
        return 1
    (AQUI.parent / "tanda_m11_pase4_barrido.json").write_text(json.dumps(tanda, ensure_ascii=False, indent=1), encoding="utf-8")
    print("tanda m11-pase4-barrido: %d correcciones en %d nodos" % (len(tanda), len({c["node_id"] for c in tanda})))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
