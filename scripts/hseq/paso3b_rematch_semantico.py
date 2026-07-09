#!/usr/bin/env python3
"""Paso 3b: re-match SEMANTICO de las referencias podadas por el paso 3.

Las 254 referencias que el paso 3 podo no son basura: son referencias con
el nombre equivocado. La generacion por chunks sin estado hizo que el
modelo nombrara conceptos vecinos plausibles (ej. 'cartas_de_control') en
vez de referenciar node_ids que vio nacer; si en el lote existe un nodo
que ES ese concepto pero se titulo distinto, la arista es legitima y solo
fallo el matching de cadenas (fuzzy 0.90 no ve equivalencia semantica).

Bandas por score del mejor match (mismo modelo del paso 6):
  >= 0.70          redirigir automatico
  0.55 - 0.70      cola de revision humana/agente (aprobar/rechazar por
                   significado, leyendo el contenido del candidato)
  <  0.55          poda definitiva (fantasma genuino: concepto que nunca
                   se chunkeo como nodo propio)

Guardas: jamas auto-referencias, jamas cruzar dominios. Toda decision
queda en metadata/aristas_resemantizadas.json.

Uso:
  python scripts/hseq/paso3b_rematch_semantico.py            # analiza + aplica banda auto + deja cola de revision
  python scripts/hseq/paso3b_rematch_semantico.py --aplicar-revision   # aplica los 'aprobado_revision' ya vereditados
"""
import json
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from lib_dominio import CATEGORIAS, cargar_dominio, dir_metadata, escribir_json, guardar_nodo

UMBRAL_AUTO = 0.70
UMBRAL_REVISION = 0.55
MODELO = "paraphrase-multilingual-MiniLM-L12-v2"
TOP_K = 3


def humanizar(nid: str) -> str:
    return nid.replace("_", " ")


def texto_nodo(d: dict) -> str:
    return f"{d.get('titulo_concepto', '')}. {(d.get('resumen_teorico') or '')[:200]}"


def aplicar_redirecciones(cat: str, nodos: dict, podadas: list, resolucion: dict) -> dict:
    """resolucion: {fantasma: destino}. Re-agrega la arista podada con el
    destino resuelto, en cada nodo que referenciaba al fantasma. Devuelve
    {fantasma: [{en, campo}, ...]} con lo realmente aplicado."""
    aplicado: dict[str, list] = {}
    for p in podadas:
        destino = resolucion.get(p["ref"])
        if not destino:
            continue
        en = p["en"]
        if en not in nodos:
            continue
        if destino == en:
            continue  # guarda: jamas auto-referencias
        lista = nodos[en].setdefault(p["campo"], [])
        if destino not in lista:
            lista.append(destino)
            guardar_nodo(cat, en, nodos[en])
        aplicado.setdefault(p["ref"], []).append({"en": en, "campo": p["campo"]})
    return aplicado


def analizar():
    from sentence_transformers import SentenceTransformer, util
    modelo = SentenceTransformer(MODELO)
    resumen_global = {}
    for cat in CATEGORIAS:
        nodos = cargar_dominio(cat)
        log = json.load(open(dir_metadata(cat) / "aristas_reparadas.json", encoding="utf-8"))
        podadas = log["podadas"]
        fantasmas = sorted({p["ref"] for p in podadas})
        if not fantasmas:
            print(f"{cat}: 0 fantasmas, nada que analizar")
            continue
        ids = sorted(nodos)
        emb_nodos = modelo.encode([texto_nodo(nodos[i]) for i in ids],
                                  normalize_embeddings=True, show_progress_bar=False)
        emb_fantasmas = modelo.encode([humanizar(f) for f in fantasmas],
                                      normalize_embeddings=True, show_progress_bar=False)
        sim = util.cos_sim(emb_fantasmas, emb_nodos)  # [F, N]

        entradas = []
        resolucion_auto = {}
        import torch
        for fi, fantasma in enumerate(fantasmas):
            fila = sim[fi]
            vals, idxs = torch.topk(fila, min(TOP_K, len(ids)))
            candidatos = [
                {"id": ids[int(ix)], "score": round(float(v), 4),
                 "titulo": nodos[ids[int(ix)]].get("titulo_concepto", "")}
                for v, ix in zip(vals.tolist(), idxs.tolist())
            ]
            score = candidatos[0]["score"]
            destino = candidatos[0]["id"]
            if score >= UMBRAL_AUTO:
                banda, veredicto = "auto", "aprobado_auto"
                resolucion_auto[fantasma] = destino
            elif score >= UMBRAL_REVISION:
                banda, veredicto = "revision", None  # pendiente de veredicto humano/agente
            else:
                banda, veredicto = "poda", "poda_definitiva"
            entradas.append({
                "fantasma": fantasma, "destino": destino, "score": score,
                "banda": banda, "veredicto": veredicto, "candidatos": candidatos,
                "referenciado_desde": [{"en": p["en"], "campo": p["campo"]}
                                        for p in podadas if p["ref"] == fantasma],
            })

        aplicado = aplicar_redirecciones(cat, nodos, podadas, resolucion_auto)
        for e in entradas:
            if e["banda"] == "auto":
                e["aplicado_en"] = aplicado.get(e["fantasma"], [])

        escribir_json(dir_metadata(cat) / "aristas_resemantizadas.json", entradas)
        conteo = {"auto": 0, "revision": 0, "poda": 0}
        for e in entradas:
            conteo[e["banda"]] += 1
        resumen_global[cat] = conteo
        print(f"{cat}: {len(fantasmas)} fantasmas unicos -> auto={conteo['auto']} "
              f"revision={conteo['revision']} poda={conteo['poda']}")
    print("\nSIGUIENTE: revisar las entradas banda='revision' (veredicto null) en "
          "metadata/aristas_resemantizadas.json, poner veredicto 'aprobado_revision' "
          "(ajustando 'destino' a otro candidato si el contenido lo justifica) o "
          "'rechazado_revision', y correr con --aplicar-revision.")


def aplicar_revision():
    for cat in CATEGORIAS:
        ruta = dir_metadata(cat) / "aristas_resemantizadas.json"
        if not ruta.exists():
            continue
        entradas = json.load(open(ruta, encoding="utf-8"))
        nodos = cargar_dominio(cat)
        log = json.load(open(dir_metadata(cat) / "aristas_reparadas.json", encoding="utf-8"))
        podadas = log["podadas"]
        resolucion = {e["fantasma"]: e["destino"] for e in entradas
                      if e["banda"] == "revision" and e.get("veredicto") == "aprobado_revision"}
        if not resolucion:
            print(f"{cat}: 0 aprobados en revision")
            continue
        aplicado = aplicar_redirecciones(cat, nodos, podadas, resolucion)
        for e in entradas:
            if e["fantasma"] in resolucion:
                e["aplicado_en"] = aplicado.get(e["fantasma"], [])
        escribir_json(ruta, entradas)
        print(f"{cat}: {len(resolucion)} fantasmas de revision aplicados")


if __name__ == "__main__":
    if "--aplicar-revision" in sys.argv:
        aplicar_revision()
    else:
        analizar()
