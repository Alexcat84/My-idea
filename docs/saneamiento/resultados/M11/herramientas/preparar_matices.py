# -*- coding: utf-8 -*-
"""PASE DE MATICES de la limpieza M11: relee cada resumen FINAL contra sus lineas buscando un solo tipo de fallo,
el matiz perdido (el libro dice some, most, often, might, may, can, tend to... y el resumen lo afirma como regla).

    python preparar_matices.py            arma matices/entrada_NN.json (lotes de 30 resumenes) desde tanda_m11_limpieza.json

Solo entran los resumenes de los lotes 01 a 31: desde el lote 32 el verificador ciego ya buscaba el matiz perdido y la
anecdota vuelta regla (instruccion endurecida el 28 sep 2026), y sus hallazgos pasaron por el arbitro.

Nace del arbitro de los lotes 19, 26, 29 y 30 (28 sep 2026): en 6 de 7 casos encontro endurecimientos que el
verificador ciego no habia marcado. Se plantan trampas (semilla escrita aqui, antes de sortear): un resumen real
al que se le quita un matiz. Su clave va a la carpeta del orquestador.
"""
import json
import random
import re
from pathlib import Path

SEMILLA = 20260930
AQUI = Path(__file__).resolve().parent
LIBROS = Path(r"C:\Users\AlexDesk\Documents\forja-lectura")
CLAVE = Path(r"C:\Users\AlexDesk\AppData\Local\Temp\claude\c--Users-AlexDesk-Documents-I-have-an-idea\35709856-d3a7-4f79-ad7e-c0e77323cd47\scratchpad\clave_trampas_matices.json")
POR_LOTE = 30
# endurecimientos plantados: (patron, reemplazo)
ENDURECER = [(r"\ba menudo ", ""), (r"\bsuele ", ""), (r"\bpuede ", "va a "), (r"\bpueden ", "van a "),
             (r"\balgunos ", "todos los "), (r"\balgunas ", "todas las "), (r"\bmuchas veces ", "siempre "),
             (r"\bla mayoría de ", "todos ")]


def lineas_del_libro(fichero, lineas):
    ruta = LIBROS / fichero
    if not ruta.exists():
        return "(no se encontro %s)" % fichero
    todas = ruta.read_text(encoding="utf-8").splitlines()
    nums = [int(x) for x in re.findall(r"\d+", lineas or "")]
    if not nums:
        return "(sin lineas)"
    a, b = max(1, min(nums) - 1), min(len(todas), max(nums) + 1)
    if b - a > 80:
        b = a + 80
    return "\n".join("%d: %s" % (i, todas[i - 1]) for i in range(a, b + 1))


def main():
    tanda = json.loads((AQUI / "tanda_m11_limpieza.json").read_text(encoding="utf-8"))
    viejos = set()
    for n in range(1, 32):
        s = json.loads((AQUI / "redactor" / ("lote_%02d.json" % n)).read_text(encoding="utf-8"))
        viejos |= {x["node_id"] for x in s["nodos"]}
    items = []
    for c in tanda:
        if c["veredicto"] != "RESUMEN" or c["node_id"] not in viejos:
            continue
        ev = c["cita"]["evidencia"]
        nodo = json.loads((AQUI / "primer_equipo" / "nodos" / ("%s.json" % c["node_id"])).read_text(encoding="utf-8"))
        items.append({"item": c["node_id"], "resumen": c["texto_nuevo"], "evidencia": ev,
                      "pasos_del_nodo": nodo["pasos_accionables"], "lineas_del_libro": lineas_del_libro(ev["fichero"], ev["lineas"])})
    # textos de cara cuyo texto VIEJO contaba la experiencia del autor o la autora: el redactor tendia a volverla regla
    # general (hallado por el verificador endurecido en los lotes 34, 35 y 39)
    evid = {c["node_id"]: c["cita"]["evidencia"] for c in tanda if c["veredicto"] == "RESUMEN"}
    PERSONAL = re.compile(r"(?:autora?|autores)|ella (?:cuenta|dice|hizo|admite|reconoce|recuerda)|su (?:propia )?experiencia|le paso", re.I)
    for c in tanda:
        if c["veredicto"] == "RESUMEN" or c["node_id"] not in viejos or not PERSONAL.search(c["texto_anterior"]):
            continue
        ev = evid.get(c["node_id"]) or {}
        items.append({"item": "%s|%s%s" % (c["node_id"], c["campo"], "" if c.get("indice") is None else "[%d]" % c["indice"]),
                      "viejo": c["texto_anterior"], "nuevo": c["texto_nuevo"], "evidencia_del_nodo": ev})
    rnd = random.Random(SEMILLA)
    rnd.shuffle(items)
    lotes = [items[i:i + POR_LOTE] for i in range(0, len(items), POR_LOTE)]
    clave = {"semilla": SEMILLA, "trampas": {}}
    (AQUI / "matices").mkdir(exist_ok=True)
    for k, lote in enumerate(lotes, 1):
        nn = "%02d" % k
        candidatos = [(it, p, r) for it in lote if "resumen" in it for p, r in ENDURECER if re.search(p, it["resumen"])]
        if candidatos:
            it, p, r = rnd.choice(candidatos)
            t = json.loads(json.dumps(it))
            t["resumen"] = re.sub(p, r, it["resumen"], count=1)
            t["resumen"] = t["resumen"][0].upper() + t["resumen"][1:]
            t["item"] = "mtrampa_%s" % nn
            lote.insert(rnd.randrange(len(lote) + 1), t)
            clave["trampas"][t["item"]] = {"copia_de": it["item"], "patron": p, "reemplazo": r}
        (AQUI / "matices" / ("entrada_%s.json" % nn)).write_text(json.dumps({"lote": nn, "items": lote}, ensure_ascii=False, indent=1), encoding="utf-8")
    CLAVE.write_text(json.dumps(clave, ensure_ascii=False, indent=1), encoding="utf-8")
    print("%d resumenes en %d lotes, %d trampas" % (len(items), len(lotes), len(clave["trampas"])))


if __name__ == "__main__":
    main()
