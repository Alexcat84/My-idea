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
                      "_origen": {"tipo": "sintetico", "sid": s["sid"], "lineas": s["lineas"], "fragmento": s["fragmento"]}})
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
    C.escribe_jsonl(os.path.join(C.PIL, "items_mezclados.jsonl"), salida)
    C.escribe_json(os.path.join(C.PRU, "CLAVE_CIEGA.json"), {"_aviso": "Clave de la mezcla a ciegas. Ningun prompt la lee; solo recall.py.", "clave": clave})
    print(len(salida), "items;", sum(1 for v in clave.values() if v["tipo"] == "sintetico"), "sinteticos")

if __name__ == "__main__":
    main()
