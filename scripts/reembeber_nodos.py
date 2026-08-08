#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""reembeber_nodos.py - Re-embebe SOLO los nodos que cambiaron.

El indice completo son 3.746 vectores y ~590.000 tokens. Re-generarlo entero
tras cada tanda de 40 seria pagar cien veces por cambiar cuarenta. Esto toca
solo lo que cambio, con el MISMO texto y el MISMO input_type que usa el
constructor del indice (build_semantic_index_voyage), para que el vector nuevo
viva en el mismo espacio que los viejos.

Tambien parchea el contenido del nodo en las dos copias del grafo, porque el
indice se arma del grafo y no de dataset/nodos/.

Uso:
  python scripts/reembeber_nodos.py --ids a b c
  python scripts/reembeber_nodos.py --desde packs/quality/poda/_revoz_hechos.json
"""
import argparse
import json
import os
import sys
import time
import urllib.request
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent
NODOS = BASE / "dataset" / "nodos"
GRAFOS = [BASE / "dataset" / "metadata" / "master_graph.json",
          BASE / "web" / "lib" / "assets" / "master_graph.json"]
INDICE = BASE / "web" / "lib" / "assets" / "semantic_index.json"
VOYAGE_URL = "https://api.voyageai.com/v1/embeddings"
MODELO = "voyage-4-lite"
LOTE = 100

CAMPOS = ("titulo_concepto", "resumen_teorico", "pasos_accionables",
          "entregable_esperado", "condiciones_activacion")


def texto_nodo(n):
    """EL MISMO que build_semantic_index_voyage. Si alli cambia, aqui tambien."""
    partes = [n.get("titulo_concepto", ""), n.get("resumen_teorico", ""),
              " ".join(n.get("condiciones_activacion", []) or [])]
    return " ".join(p for p in partes if p).strip()


def embeber(textos, dim, clave):
    for intento in range(4):
        try:
            cuerpo = json.dumps({"input": textos, "model": MODELO,
                                 "input_type": "document",
                                 "output_dimension": dim}).encode()
            req = urllib.request.Request(VOYAGE_URL, data=cuerpo, headers={
                "Authorization": f"Bearer {clave}", "Content-Type": "application/json"})
            with urllib.request.urlopen(req, timeout=180) as r:
                d = json.loads(r.read())
            return [x["embedding"] for x in d["data"]], d.get("usage", {}).get("total_tokens", 0)
        except Exception as e:
            if intento == 3:
                raise
            print(f"    reintento {intento + 1}: {e}")
            time.sleep(5 * (intento + 1))


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--ids", nargs="*", default=[])
    ap.add_argument("--desde", help="json cuyas CLAVES son los node_id tocados")
    args = ap.parse_args()

    ids = list(args.ids)
    if args.desde:
        ids += list(json.loads(Path(args.desde).read_text(encoding="utf-8")).keys())
    ids = sorted(set(ids))
    if not ids:
        print("  nada que re-embeber")
        return

    from dotenv import load_dotenv
    load_dotenv(BASE / ".env")
    clave = os.getenv("VOYAGE_API_KEY", "").strip()
    if not clave:
        print("ERROR: falta VOYAGE_API_KEY")
        sys.exit(2)

    # 1. el contenido nuevo llega a las dos copias del grafo
    nodos = {}
    for nid in ids:
        ruta = NODOS / f"{nid}.json"
        if not ruta.exists():
            print(f"  AVISO: {nid} no existe en dataset/nodos")
            continue
        nodos[nid] = json.loads(ruta.read_text(encoding="utf-8"))
    for gp in GRAFOS:
        g = json.loads(gp.read_text(encoding="utf-8"))
        for nid, n in nodos.items():
            if nid in g["nodos"]:
                g["nodos"][nid].update({k: n[k] for k in CAMPOS if k in n})
        gp.write_text(json.dumps(g, ensure_ascii=False, indent=2), encoding="utf-8")

    # 2. el vector nuevo, solo de esos
    idx = json.loads(INDICE.read_text(encoding="utf-8"))
    pos = {n: i for i, n in enumerate(idx["ids"])}
    presentes = [n for n in nodos if n in pos]
    ausentes = [n for n in nodos if n not in pos]
    tokens = 0
    for i in range(0, len(presentes), LOTE):
        trozo = presentes[i:i + LOTE]
        vecs, t = embeber([texto_nodo(nodos[n]) for n in trozo], idx["dimension"], clave)
        tokens += t
        for nid, v in zip(trozo, vecs):
            idx["embeddings"][pos[nid]] = v
        print(f"  re-embebidos {min(i + LOTE, len(presentes))}/{len(presentes)}")
    INDICE.write_text(json.dumps(idx, ensure_ascii=False), encoding="utf-8")

    print(f"  {len(presentes)} nodos re-embebidos, {tokens} tokens")
    if ausentes:
        print(f"  {len(ausentes)} no estaban en el indice (deprecados, seguramente): {ausentes[:5]}")


if __name__ == "__main__":
    main()
