#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""El PUESTO de cada nodo blanco en el ranking completo, no solo si entro al top-K.

POR QUE (encargo del auditor, Fase 3): un ambar dice "no entro al top-10" y se
queda callado sobre lo demas. Un blanco que salta del puesto 30 al 12 sin entrar
dice "la voz mueve y falta dosis", que es informacion DISTINTA de un ambar
inmovil. Es el mismo metodo del experimento de las tildes (14 -> 15), que ya
demostro su valor: sin el puesto, aquella conclusion habria sido "no paso nada".

Tambien reporta QUIEN le sigue ganando al blanco, y si ese ganador esta en el
lote que se esta tocando: si el que gana tambien se re-voza, la comparacion de
la siguiente corrida no es limpia y hay que decirlo.

Uso:
  python scripts/rumbos/puesto_de_blancos.py --etiqueta antes
  python scripts/rumbos/puesto_de_blancos.py --etiqueta despues --contra antes
"""
import argparse
import json
import os
import sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
BASE = AQUI.parent.parent
sys.path.insert(0, str(BASE / "scripts"))

BLANCOS = {
    "nucleo_validar_antes_de_gastar": ["customer_discovery_get_out_of_building",
                                       "diseno_experimentos_hipotesis"],
    "nucleo_dicen_que_si_pero_no_compran": ["get_out_building_test_sell"],
    "nucleo_le_sirve_a_todo_el_mundo": ["customer_segments_hypothesis",
                                        "segmentos_de_clientes_problema_necesidad"],
    "nucleo_por_que_me_comprarian_a_mi": ["value_proposition_startup"],
    "nucleo_sacar_algo_pequeno_primero": ["construir_mvp_baja_fidelidad", "concierge_mvp"],
}


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--etiqueta", required=True, help="nombre de esta foto (antes/despues)")
    ap.add_argument("--contra", help="etiqueta de una foto anterior para comparar")
    ap.add_argument("--lote", help="json con `sobrevivientes`: marca a los que estan en el lote")
    args = ap.parse_args()

    from dotenv import load_dotenv
    load_dotenv(BASE / ".env")
    import numpy as np
    from prueba_rumbos import embeber, puerta, K  # misma puerta que el motor

    banco = json.loads((AQUI / "banco_rumbos.json").read_text(encoding="utf-8"))["rumbos"]
    idx = json.loads((BASE / "web" / "lib" / "assets" / "semantic_index.json").read_text(encoding="utf-8"))
    grafo = json.loads((BASE / "web" / "lib" / "assets" / "master_graph.json").read_text(encoding="utf-8"))["nodos"]
    ids = idx["ids"]
    E = np.array(idx["embeddings"], dtype=np.float32)
    E /= np.linalg.norm(E, axis=1, keepdims=True)

    en_lote = set()
    if args.lote:
        en_lote = set(json.loads(Path(args.lote).read_text(encoding="utf-8"))["sobrevivientes"])

    rumbos = [r for r in banco if r["id"] in BLANCOS]
    vecs, uso = embeber([r["consulta"] for r in rumbos], idx["dimension"])
    Q = np.array(vecs, dtype=np.float32)
    Q /= np.linalg.norm(Q, axis=1, keepdims=True)

    foto = {}
    for r, q in zip(rumbos, Q):
        dominios = set(r["dominios"]) | {"core"}
        s = E @ q
        # el ranking COMPLETO de lo que la puerta deja ofrecer
        orden = [ids[i] for i in np.argsort(-s) if puerta(ids[i], grafo, dominios)]
        puesto = {n: orden.index(n) + 1 for n in BLANCOS[r["id"]] if n in orden}
        mejor = min(puesto.values()) if puesto else None
        ganadores = orden[:K]
        foto[r["id"]] = {
            "puestos": puesto,
            "mejor_puesto": mejor,
            "en_top_k": bool(mejor and mejor <= K),
            "le_ganan": [{"id": n, "puesto": i + 1, "en_el_lote": n in en_lote,
                          "titulo": grafo[n]["titulo_concepto"]}
                         for i, n in enumerate(ganadores) if n not in puesto][:5],
        }
    salida = AQUI / f"_puestos_{args.etiqueta}.json"
    salida.write_text(json.dumps({"K": K, "foto": foto}, ensure_ascii=False, indent=2),
                      encoding="utf-8")

    antes = None
    if args.contra:
        p = AQUI / f"_puestos_{args.contra}.json"
        if p.exists():
            antes = json.loads(p.read_text(encoding="utf-8"))["foto"]

    print(f"\n  PUESTO DEL BLANCO en el ranking completo (K={K})\n")
    for rid, d in foto.items():
        linea = f"  {rid}"
        if antes and rid in antes:
            a, b = antes[rid]["mejor_puesto"], d["mejor_puesto"]
            flecha = "->"
            if a and b:
                flecha = f"{a} {'SUBE' if b < a else ('BAJA' if b > a else '=')} {b}"
            linea += f"    {flecha}"
        else:
            linea += f"    puesto {d['mejor_puesto']}"
        print(linea + ("   [EN TOP-K]" if d["en_top_k"] else ""))
        for n, p_ in d["puestos"].items():
            extra = ""
            if antes and rid in antes:
                pa = antes[rid]["puestos"].get(n)
                if pa:
                    extra = f"  (antes {pa})"
            print(f"      {p_:>5}  {n}{extra}")
        for w in d["le_ganan"][:3]:
            marca = " *EN EL LOTE*" if w["en_el_lote"] else ""
            print(f"        le gana #{w['puesto']}: {w['titulo'][:52]}{marca}")
    print(f"\n  ({uso.get('total_tokens', 0)} tokens de consulta) -> {salida.name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
