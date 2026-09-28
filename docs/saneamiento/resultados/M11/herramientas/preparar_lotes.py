# -*- coding: utf-8 -*-
"""Arma los lotes del REDACTOR de la limpieza M11 (docs/saneamiento/instrumentos/M11_LIMPIEZA.md).

Los nodos del pack (../m11-trabajo/primer_equipo/nodos) se ordenan por libro y capitulo y se parten en lotes de 12.
En cada lote entra UNA trampa: la copia de un nodo de OTRO lote, con id trampa_NN y tres cosas plantadas que el
redactor tiene que sacar (una voz de libro que la guarda no conoce, una cifra de mercado y un autor). La semilla se
escribe aqui, antes de sortear. La clave de las trampas se guarda FUERA del alcance de los agentes
(clave_trampas_redactor.json en esta carpeta de trabajo, que ellos no leen) hasta puntuar.
"""
import glob
import json
import random
import re
from pathlib import Path

SEMILLA = 20260928
TAM = 12
AQUI = Path(__file__).resolve().parent
NODOS = AQUI / "primer_equipo" / "nodos"
ENTRADA = AQUI / "entrada"
LIBRO = {"Kim Scott": "scott_radical_candor", "Julie Zhuo": "zhuo_manager", "Geoff Smart": "smart_who",
         "Andrew S. Grove": "grove_high_output", "Michael E. Gerber": "gerber_emyth", "L. David Marquet": "marquet_turn_the_ship"}
RF = re.compile(r"fuentes/([a-z_]+)/(cap_\d+[a-z_]*\.md)")
RL = re.compile(r"[Ll][ií]neas? (\d+)(?: a (\d+))?")
PLANTADOS = {
    "voz": "Como cuenta la obra original, esto se aprende haciendolo.",
    "cifra": "Calcula unos 20.000 dolares al anio para esto.",
    "autor": "Como recomienda Andy Grove, ",
}


def libro_de(fuente):
    for k, v in LIBRO.items():
        if k in fuente:
            return v
    raise SystemExit("fuente sin libro: " + fuente)


def entrada(n):
    nota = n["notas_extraccion"]
    f, l = RF.search(nota), RL.search(nota)
    return {
        "node_id": n["node_id"],
        "libro": "fuentes/" + libro_de(n["fuente"]),
        "pista_evidencia": {"fichero": "fuentes/%s/%s" % f.groups() if f else None,
                            "lineas": ("%s-%s" % (l.group(1), l.group(2) or l.group(1))) if l else None},
        "notas_extraccion": nota,
        "titulo_concepto": n["titulo_concepto"],
        "pasos_accionables": n["pasos_accionables"],
        "entregable_esperado": n["entregable_esperado"],
        "condiciones_activacion": n["condiciones_activacion"],
    }


def main():
    nodos = [json.loads(Path(p).read_text(encoding="utf-8")) for p in sorted(glob.glob(str(NODOS / "*.json")))]
    items = [entrada(n) for n in nodos]
    items.sort(key=lambda e: (e["libro"], e["pista_evidencia"]["fichero"] or "zz", e["node_id"]))
    lotes = [items[i:i + TAM] for i in range(0, len(items), TAM)]
    rnd = random.Random(SEMILLA)
    clave = {"semilla": SEMILLA, "plantados": PLANTADOS, "trampas": {}}
    ENTRADA.mkdir(exist_ok=True)
    for i, lote in enumerate(lotes, 1):
        otro = rnd.choice([j for j in range(len(lotes)) if j != i - 1])
        base = rnd.choice(lotes[otro])
        t = json.loads(json.dumps(base))
        tid = "trampa_%02d" % i
        t["node_id"] = tid
        pasos = t["pasos_accionables"]
        k1, k2 = rnd.sample(range(len(pasos)), 2) if len(pasos) > 1 else (0, 0)
        pasos[k1] = pasos[k1] + " " + PLANTADOS["voz"]
        pasos[k2] = pasos[k2] + " " + PLANTADOS["cifra"]
        t["entregable_esperado"] = PLANTADOS["autor"] + t["entregable_esperado"][0].lower() + t["entregable_esperado"][1:]
        pos = rnd.randrange(len(lote) + 1)
        con = lote[:pos] + [t] + lote[pos:]
        clave["trampas"][tid] = {"lote": "%02d" % i, "copia_de": base["node_id"], "paso_voz": k1, "paso_cifra": k2}
        (ENTRADA / ("lote_%02d.json" % i)).write_text(json.dumps({"lote": "%02d" % i, "nodos": con}, ensure_ascii=False, indent=1), encoding="utf-8")
    (AQUI / "clave_trampas_redactor.json").write_text(json.dumps(clave, ensure_ascii=False, indent=1), encoding="utf-8")
    print("%d nodos en %d lotes de hasta %d, mas una trampa por lote (semilla %d)" % (len(items), len(lotes), TAM, SEMILLA))


if __name__ == "__main__":
    main()
