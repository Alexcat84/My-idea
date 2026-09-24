# -*- coding: utf-8 -*-
"""Despues de las pasadas: cruza ids con la clave ciega y mide.

  python recall.py <intento>            recall, tasa de marcado, contrarios, costes
  python recall.py <intento> registrar  escribe docs/fidelidad/VEREDICTOS_PASOS.jsonl
"""
import json, os, sys, collections
import comun as C
import busqueda as B

def cargar(intento):
    clave = json.load(open(os.path.join(C.PRU, "CLAVE_CIEGA.json"), encoding="utf-8"))["clave"]
    r1 = json.load(open(os.path.join(C.PIL, f"pasada1_i{intento}.json"), encoding="utf-8"))
    p2 = os.path.join(C.PIL, f"pasada2_i{intento}.json")
    r2 = json.load(open(p2, encoding="utf-8")) if os.path.exists(p2) else {}
    return clave, r1, r2

def costes(etapa):
    fil = [json.loads(l) for l in open(C.LOG_COSTES, encoding="utf-8")]
    fil = [f for f in fil if f["etapa"] == etapa]
    return {"llamadas": len(fil), "usd": round(sum(f["usd"] for f in fil), 4),
            "turnos": sum(f["turnos"] or 0 for f in fil), "segundos_api": round(sum(f["duracion_s"] for f in fil), 1),
            "tokens_in": sum(f["tokens_in"] for f in fil), "tokens_out": sum(f["tokens_out"] for f in fil)}

def medir(intento):
    clave, r1, r2 = cargar(intento)
    sint = sorted((i for i, o in clave.items() if o["tipo"] == "sintetico"), key=lambda i: clave[i]["sid"])
    con = [i for i, o in clave.items() if o["tipo"] == "real" and o["nodo"] == "prevalencia_omisiones" and o["paso_idx"] == 1]
    reales = [i for i, o in clave.items() if o["tipo"] == "real"]
    fila = lambda i: {"sid": clave[i].get("sid", "conocido"), "id": i, "p1_clase": r1[i]["clase"], "p1_marca": r1[i]["marca"],
                      "p2": r2.get(i, {}).get("veredicto", "-")}
    detalle = [fila(i) for i in sint + con]
    marc_reales = [i for i in reales if r1[i]["marca"]]
    contr = [i for i in reales if r2.get(i, {}).get("veredicto") == "CONTRARIO"]
    res = {
        "intento": intento,
        "recall_pasada1_sinteticos": f"{sum(r1[i]['marca'] for i in sint)}/{len(sint)}",
        "recall_pasada1_conocido": f"{sum(r1[i]['marca'] for i in con)}/{len(con)}",
        "recall_final_sinteticos": f"{sum(r2.get(i, {}).get('veredicto') == 'CONTRARIO' for i in sint)}/{len(sint)}",
        "recall_final_conocido": f"{sum(r2.get(i, {}).get('veredicto') == 'CONTRARIO' for i in con)}/{len(con)}",
        "reales": len(reales), "reales_marcados_p1": len(marc_reales),
        "tasa_marcado_reales": round(len(marc_reales) / len(reales), 3),
        "clases_p1_reales": collections.Counter(r1[i]["clase"] for i in reales),
        "veredictos_p2_reales": collections.Counter(r2[i]["veredicto"] for i in marc_reales if i in r2),
        "contrarios_reales": [{"nodo": clave[i]["nodo"], "paso": clave[i]["paso_idx"] + 1, "id": i} for i in contr],
        "detalle_vara": detalle,
        "coste_pasada1": costes(f"pasada1_i{intento}"), "coste_pasada2": costes(f"pasada2_i{intento}"),
    }
    C.escribe_json(os.path.join(C.PIL, f"RECALL_i{intento}.json"), res)
    print(json.dumps(res, ensure_ascii=False, indent=1))

def registrar(intento):
    clave, r1, r2 = cargar(intento)
    items = {it["id"]: it for it in B._items()}
    filas = []
    for i, o in clave.items():
        if o["tipo"] != "real":
            continue
        a = r1[i]
        if a["marca"]:
            b = r2[i]
            v = {"veredicto": b["veredicto"], "cita": {"lineas": b.get("lineas", []), "texto": b.get("cita", "")},
                 "razon": b.get("razon", ""), "pasada": 2}
            if b["veredicto"] == "CONTRARIO":
                v["paso_fiel"] = b.get("paso_fiel", "")
        else:
            v = {"veredicto": a["clase"], "cita": {"lineas": a.get("lineas", []), "texto": ""},
                 "razon": a.get("razon", ""), "pasada": 1}
        filas.append(dict(nodo=o["nodo"], paso=o["paso_idx"] + 1, texto_paso=items[i]["paso"],
                          libro=C.FUENTE, id_ciego=i, intento=int(intento), modelo=C.MODELO, **v))
    filas.sort(key=lambda r: (r["nodo"], r["paso"]))
    C.escribe_jsonl(os.path.join(C.FID, "VEREDICTOS_PASOS.jsonl"), filas)
    print(len(filas), "pasos registrados", collections.Counter(f["veredicto"] for f in filas))

if __name__ == "__main__":
    if len(sys.argv) > 2 and sys.argv[2] == "registrar":
        registrar(sys.argv[1])
    else:
        medir(sys.argv[1])
