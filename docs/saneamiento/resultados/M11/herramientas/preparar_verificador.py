# -*- coding: utf-8 -*-
"""Arma la entrada del VERIFICADOR CIEGO de un lote M11 (docs/saneamiento/instrumentos/M11_LIMPIEZA.md, seccion 6).

    python preparar_verificador.py NN

Por elemento: el texto viejo, el nuevo y, para el resumen, los pasos viejos del nodo y las lineas del libro que el
redactor dio como evidencia. No lleva el razonamiento del redactor ni sus veredictos. Las trampas del redactor
(trampa_NN) no se verifican: se puntuan aparte. Se plantan DOS trampas para el verificador (semilla escrita aqui):
un resumen con una cifra o un plazo que no esta en las lineas, y un paso con el sentido invertido o con la voz de libro
devuelta. Su clave va a la carpeta del orquestador, fuera del alcance de los agentes.
"""
import json
import random
import re
import sys
from pathlib import Path

SEMILLA = 20260929
AQUI = Path(__file__).resolve().parent
LIBROS = Path(r"C:\Users\AlexDesk\Documents\forja-lectura")
CLAVE = Path(r"C:\Users\AlexDesk\AppData\Local\Temp\claude\c--Users-AlexDesk-Documents-I-have-an-idea\35709856-d3a7-4f79-ad7e-c0e77323cd47\scratchpad\clave_trampas_verificador.json")
INSERTOS_RESUMEN = [" Conviene hacerlo en un plazo de 30 días.", " Así se reduce la rotación en un 40 por ciento."]
INSERTOS_PASO = [(" como dice el libro", "voz"), ("NEGAR", "sentido")]


def lineas_del_libro(fichero, lineas):
    ruta = LIBROS / fichero
    if not ruta.exists():
        return "(no se encontro %s)" % fichero
    todas = ruta.read_text(encoding="utf-8").splitlines()
    nums = [int(x) for x in re.findall(r"\d+", lineas or "")]
    if not nums:
        return "(sin lineas)"
    a, b = max(1, min(nums) - 1), min(len(todas), max(nums) + 1)
    if b - a > 70:
        b = a + 70
    return "\n".join("%d: %s" % (i, todas[i - 1]) for i in range(a, b + 1))


def main(nn):
    entrada = {n["node_id"]: n for n in json.loads((AQUI / "entrada" / ("lote_%s.json" % nn)).read_text(encoding="utf-8"))["nodos"]}
    salida = json.loads((AQUI / "redactor" / ("lote_%s.json" % nn)).read_text(encoding="utf-8"))
    items = []
    for s in salida["nodos"]:
        nid = s["node_id"]
        if nid.startswith("trampa_"):
            continue
        n = entrada[nid]
        r = s["resumen"]
        items.append({"item": "%s|resumen_teorico" % nid, "campo": "resumen_teorico", "pasos_del_nodo": n["pasos_accionables"],
                      "nuevo": r["texto"], "evidencia": {"fichero": r["fichero"], "lineas": r["lineas"]},
                      "lineas_del_libro": lineas_del_libro(r["fichero"], r["lineas"])})
        for c in s.get("cambios") or []:
            viejo = n[c["campo"]] if c.get("indice") is None else n[c["campo"]][c["indice"]]
            clave = c["campo"] + ("" if c.get("indice") is None else "[%d]" % c["indice"])
            items.append({"item": "%s|%s" % (nid, clave), "campo": c["campo"], "viejo": viejo, "nuevo": c["texto_nuevo"]})
    rnd = random.Random(SEMILLA + int(nn))
    trampas = {}
    resumenes = [i for i in items if i["campo"] == "resumen_teorico"]
    pasos = [i for i in items if i["campo"] == "pasos_accionables" and len(i["nuevo"]) > 40]
    if resumenes:
        base = rnd.choice(resumenes)
        t = json.loads(json.dumps(base))
        ins = rnd.choice(INSERTOS_RESUMEN)
        t["nuevo"] = base["nuevo"].rstrip() + ins
        t["item"] = "vtrampa_%s_a|resumen_teorico" % nn
        items.insert(rnd.randrange(len(items) + 1), t)
        trampas[t["item"]] = {"tipo": "cifra_o_plazo_inventado", "inserto": ins, "copia_de": base["item"]}
    if pasos:
        base = rnd.choice(pasos)
        t = json.loads(json.dumps(base))
        ins, tipo = rnd.choice(INSERTOS_PASO)
        if tipo == "voz":
            t["nuevo"] = base["nuevo"].rstrip(".") + ins + "."
        else:
            # el sentido invertido: el imperativo del paso pasa a su prohibicion
            t["nuevo"] = "No " + base["nuevo"][0].lower() + base["nuevo"][1:]
        t["item"] = "vtrampa_%s_b|pasos_accionables" % nn
        items.insert(rnd.randrange(len(items) + 1), t)
        trampas[t["item"]] = {"tipo": tipo, "copia_de": base["item"], "nuevo_plantado": t["nuevo"]}
    (AQUI / "verificador").mkdir(exist_ok=True)
    (AQUI / "verificador" / ("entrada_%s.json" % nn)).write_text(json.dumps({"lote": nn, "items": items}, ensure_ascii=False, indent=1), encoding="utf-8")
    todas = json.loads(CLAVE.read_text(encoding="utf-8")) if CLAVE.exists() else {"semilla": SEMILLA, "trampas": {}}
    todas["trampas"].update(trampas)
    CLAVE.write_text(json.dumps(todas, ensure_ascii=False, indent=1), encoding="utf-8")
    print("lote %s: %d elementos a verificar (con %d trampas)" % (nn, len(items), len(trampas)))


if __name__ == "__main__":
    main(sys.argv[1])
