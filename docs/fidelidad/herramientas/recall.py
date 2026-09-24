# -*- coding: utf-8 -*-
"""Despues de las pasadas: cruza ids con la clave ciega y mide.

  python recall.py <intento>            recall, tasa de marcado, contrarios, costes
  python recall.py <intento> registrar  escribe docs/fidelidad/VEREDICTOS_PASOS.jsonl
"""
import json, os, sys, collections
import comun as C
import busqueda as B

def cargar(intento):
    clave = json.load(open(os.path.join(C.PRU, f"CLAVE_CIEGA_i{intento}.json"), encoding="utf-8"))["clave"]
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
    sint = sorted((i for i, o in clave.items() if o["tipo"] == "sintetico" and o.get("clase", "CONTRARIO") == "CONTRARIO"), key=lambda i: clave[i]["sid"])
    anad = sorted((i for i, o in clave.items() if o["tipo"] == "sintetico" and o.get("clase") == "ANADIDO"), key=lambda i: clave[i]["sid"])
    con = [i for i, o in clave.items() if o["tipo"] == "real" and o["nodo"] == "prevalencia_omisiones" and o["paso_idx"] == 1]
    reales = [i for i, o in clave.items() if o["tipo"] == "real"]
    fila = lambda i: {"sid": clave[i].get("sid", "conocido"), "id": i, "p1_clase": r1[i]["clase"], "p1_marca": r1[i]["marca"],
                      "p2": r2.get(i, {}).get("veredicto", "-"), "tambien_anadido": r2.get(i, {}).get("tambien_anadido"),
                      "datos_sin_respaldo": r2.get(i, {}).get("datos_sin_respaldo")}
    detalle = [fila(i) for i in sint + anad + con]
    marc_reales = [i for i in reales if r1[i]["marca"]]
    contr = [i for i in reales if r2.get(i, {}).get("veredicto") == "CONTRARIO"]
    anadr = [i for i in reales if r2.get(i, {}).get("veredicto") == "INFERIDO-ANADIDO"]
    marc_contra = [i for i in reales if r1[i].get("podria_contradecir") or r1[i].get("clase") in ("POSIBLE_CONTRARIO", "SIN_COBERTURA")]
    marc_dato = [i for i in reales if r1[i].get("dato_concreto")]
    res = {
        "intento": intento,
        "recall_pasada1_sinteticos": f"{sum(r1[i]['marca'] for i in sint)}/{len(sint)}",
        "recall_pasada1_conocido": f"{sum(r1[i]['marca'] for i in con)}/{len(con)}",
        "recall_final_sinteticos": f"{sum(r2.get(i, {}).get('veredicto') == 'CONTRARIO' for i in sint)}/{len(sint)}",
        "recall_final_conocido": f"{sum(r2.get(i, {}).get('veredicto') == 'CONTRARIO' for i in con)}/{len(con)}",
        "recall_pasada1_anadidos": f"{sum(r1[i]['marca'] for i in anad)}/{len(anad)}",
        "recall_final_anadidos": f"{sum(r2.get(i, {}).get('veredicto') == 'INFERIDO-ANADIDO' for i in anad)}/{len(anad)}",
        "recall_final_anadidos_con_doble_etiqueta": f"{sum(r2.get(i, {}).get('veredicto') == 'INFERIDO-ANADIDO' or (r2.get(i, {}).get('veredicto') == 'CONTRARIO' and bool(r2.get(i, {}).get('tambien_anadido'))) for i in anad)}/{len(anad)}",
        "reales": len(reales), "reales_marcados_p1": len(marc_reales),
        "tasa_marcado_reales": round(len(marc_reales) / len(reales), 3),
        "clases_p1_reales": collections.Counter(r1[i]["clase"] for i in reales),
        "veredictos_p2_reales": collections.Counter(r2[i]["veredicto"] for i in marc_reales if i in r2),
        "reales_marca_contradecir": len(marc_contra), "reales_marca_dato": len(marc_dato),
        "reales_solo_marca_dato": len(set(marc_dato) - set(marc_contra)),
        "anadidos_reales": [{"nodo": clave[i]["nodo"], "paso": clave[i]["paso_idx"] + 1, "id": i} for i in anadr],
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
            if b.get("datos_sin_respaldo"):
                v["datos_sin_respaldo"] = b["datos_sin_respaldo"]
            if b.get("tambien_anadido"):
                v["tambien_anadido"] = True
            if b["veredicto"] in ("CONTRARIO", "INFERIDO-ANADIDO"):
                v["paso_fiel"] = b.get("paso_fiel", "")
        else:
            v = {"veredicto": a["clase"], "cita": {"lineas": a.get("lineas", []), "texto": ""},
                 "razon": a.get("razon", ""), "pasada": 1}
        filas.append(dict(nodo=o["nodo"], paso=o["paso_idx"] + 1, texto_paso=items[i]["paso"],
                          libro=C.FUENTE, id_ciego=i, intento=int(intento), modelo=C.MODELO, **v))
    # El mismo paso en el intento anterior (misma prueba, otra mezcla a ciegas): para ver la variacion.
    prev = str(int(intento) - 1)
    if os.path.exists(os.path.join(C.PIL, f"pasada2_i{prev}.json")) and prev != "1":
        cp, p1p, p2p = cargar(prev)
        ant = {(o["nodo"], o["paso_idx"] + 1): (p2p[i]["veredicto"] if p1p[i]["marca"] else p1p[i]["clase"])
               for i, o in cp.items() if o["tipo"] == "real"}
        for f in filas:
            f[f"veredicto_intento{prev}"] = ant[(f["nodo"], f["paso"])]
    filas.sort(key=lambda r: (r["nodo"], r["paso"]))
    cab = {"_definiciones": {
        "CONTRARIO": "el nodo aconseja lo que su libro desaconseja o contradice (mandato del fundador, 25 sep 2026). Prioridad absoluta.",
        "INFERIDO-ANADIDO": "afirma algo concreto que el libro no respalda (una cifra, un plazo, una herramienta, un responsable, una norma, una frecuencia). SE CORRIGE en la tanda de correcciones.",
        "INFERIDO-OPERATIVO": "concreta lo que el libro dice, en su misma direccion, sin datos nuevos. SE QUEDA.",
        "FIEL": "el libro dice lo que el paso aconseja.",
        "precedencia": "CONTRARIO antes que INFERIDO-ANADIDO, y este antes que INFERIDO-OPERATIVO; tambien_anadido=true marca un CONTRARIO que ademas inventa un dato.",
        "pasada": "2 = decidido por la pasada a fondo (Opus 5.5, capitulos enteros); 1 = la pasada 1 (Opus 5.5) no lo marco: sin indicio de choque y sin dato concreto.",
        "cita": "lineas del texto del fundador: " + C.LIBRO}}
    C.escribe_jsonl(os.path.join(C.FID, "VEREDICTOS_PASOS.jsonl"), [cab] + filas)
    print(len(filas), "pasos registrados", collections.Counter(f["veredicto"] for f in filas))

def estabilidad(a, b):
    """Mismo paso real en dos intentos a ciegas: cuanto coincide el veredicto final."""
    def finales(intento):
        clave, r1, r2 = cargar(intento)
        out = {}
        for i, o in clave.items():
            if o["tipo"] == "real":
                out[(o["nodo"], o["paso_idx"])] = r2[i]["veredicto"] if r1[i]["marca"] else r1[i]["clase"]
        return out
    fa, fb = finales(a), finales(b)
    igual = sum(fa[k] == fb[k] for k in fa)
    ca = {k for k, v in fa.items() if v == "CONTRARIO"}; cb = {k for k, v in fb.items() if v == "CONTRARIO"}
    aa = {k for k, v in fa.items() if v == "INFERIDO-ANADIDO"}; ab = {k for k, v in fb.items() if v == "INFERIDO-ANADIDO"}
    res = {"pasos": len(fa), "mismo_veredicto": igual,
           "contrarios": {f"i{a}": len(ca), f"i{b}": len(cb), "en_ambos": len(ca & cb), "union": len(ca | cb),
                          "solo_i" + a: sorted(f"{n} paso {p+1}" for n, p in ca - cb), "solo_i" + b: sorted(f"{n} paso {p+1}" for n, p in cb - ca)},
           "anadidos": {f"i{a}": len(aa), f"i{b}": len(ab), "en_ambos": len(aa & ab), "union": len(aa | ab)}}
    C.escribe_json(os.path.join(C.PIL, f"ESTABILIDAD_i{a}_i{b}.json"), res)
    print(json.dumps(res, ensure_ascii=False, indent=1))

if __name__ == "__main__":
    if len(sys.argv) > 3 and sys.argv[1] == "estabilidad":
        estabilidad(sys.argv[2], sys.argv[3]); sys.exit()
    if len(sys.argv) > 2 and sys.argv[2] == "registrar":
        registrar(sys.argv[1])
    else:
        medir(sys.argv[1])
