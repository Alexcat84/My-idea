# -*- coding: utf-8 -*-
"""Mezcla a ciegas: los 403 pasos reales de Reason y los sinteticos de
pruebas/ reciben ids opacos y un orden barajado. La clave (id -> origen)
vive SOLO en pruebas/CLAVE_CIEGA.json, que ningun prompt lee.
"""
import json, os, random, secrets
import comun as C

def main():
    nodos = C.nodos_reason()
    items, clave = [], {}
    for nid, n in nodos.items():
        pasos = n.get("pasos_accionables") or []
        for i, p in enumerate(pasos):
            items.append({"nodo": nid, "paso": p, "otros_pasos": [q for j, q in enumerate(pasos) if j != i],
                          "_origen": {"tipo": "real", "nodo": nid, "paso_idx": i}})
    sint = [d for d in C.lee_jsonl(os.path.join(C.PRU, "SINTETICOS_REASON.jsonl")) if d.get("sintetico")]
    for s in sint:
        host = nodos[s["nodo_huesped"]]["pasos_accionables"]
        items.append({"nodo": s["nodo_huesped"], "paso": s["paso"], "otros_pasos": list(host),
                      "_origen": {"tipo": "sintetico", "clase": s.get("clase_sintetica", "CONTRARIO"), "sid": s["sid"],
                                  "lineas": s["lineas"], "fragmento": s["fragmento"]}})
    random.Random(secrets.randbits(64)).shuffle(items)
    usados = set()
    salida = []
    for it in items:
        while True:
            oid = "P" + secrets.token_hex(3).upper()
            if oid not in usados: break
        usados.add(oid)
        clave[oid] = it.pop("_origen")
        n = nodos[it["nodo"]]
        salida.append({"id": oid, "nodo": it["nodo"], "titulo": n["titulo_concepto"], "resumen": n["resumen_teorico"],
                       "entregable": n.get("entregable_esperado", ""), "paso": it["paso"], "otros_pasos": it["otros_pasos"]})
    C.escribe_jsonl(os.path.join(C.PIL, f"items_mezclados_i{C.INTENTO}.jsonl"), salida)
    C.escribe_json(os.path.join(C.PRU, f"CLAVE_CIEGA_i{C.INTENTO}.json"), {"_aviso": "Clave de la mezcla a ciegas. Ningun prompt la lee; solo recall.py.", "clave": clave})
    remapear(salida)
    print(len(salida), "items;", sum(1 for v in clave.values() if v["tipo"] == "sintetico"), "sinteticos")

def remapear(salida):
    """Las consultas traducidas y el oro dependen solo del texto (nodo, paso): se
    heredan del intento 1 por texto, bajo los ids nuevos. Lo que no tenga
    consultas (los anadidos sinteticos nuevos) se traduce aparte, con el mismo prompt."""
    por_texto_c, por_texto_o = {}, {}
    for prev in [str(n) for n in range(1, int(C.INTENTO))]:
        viejos = {it["id"]: (it["nodo"], it["paso"]) for it in C.lee_jsonl(os.path.join(C.PIL, f"items_mezclados_i{prev}.jsonl"))}
        cons1 = json.load(open(os.path.join(C.PIL, f"consultas_traducidas_i{prev}.json"), encoding="utf-8"))
        oro1 = json.load(open(os.path.join(C.PIL, f"oro_busqueda_i{prev}.json"), encoding="utf-8"))
        por_texto_c.update({viejos[i]: v for i, v in cons1.items()})
        por_texto_o.update({viejos[i]: v for i, v in oro1.items()})
    cons, oro = {}, {}
    for it in salida:
        t = (it["nodo"], it["paso"])
        if t in por_texto_c: cons[it["id"]] = dict(por_texto_c[t], id=it["id"])
        if t in por_texto_o: oro[it["id"]] = por_texto_o[t]
    C.escribe_json(os.path.join(C.PIL, f"consultas_traducidas_i{C.INTENTO}.json"), cons)
    C.escribe_json(os.path.join(C.PIL, f"oro_busqueda_i{C.INTENTO}.json"), oro)
    print("heredadas", len(cons), "consultas y", len(oro), "oros")

if __name__ == "__main__":
    main()
