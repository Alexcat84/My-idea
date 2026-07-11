# -*- coding: utf-8 -*-
"""Expansión v1.3 — enriquecer-vs-crear (RUNBOOK §2, la regla madre).

Para cada nodo de books/General/nodos (candidato a OLA 1), busca su gemelo
en el CORE vivo (dominio 'core' del master graph): semántica (Voyage,
mismo modelo/dimensión del índice) + léxica (título normalizado).
Bandas: score >=0.60 o match léxico -> par candidato que juzga Sonnet 5
("¿el ángulo cambia la acción del emprendedor?"); <0.60 -> CREAR directo.

ENRIQUECER: el nodo core conserva id e historia; su `fuente` suma la nueva
como string "a | b" (graph.ts tipa fuente como string: NO se vuelve lista),
y gana los pasos_accionables del libro nuevo que no estén ya cubiertos.
El nodo nuevo se mueve a books/General/nodos_absorbidos/ (trazabilidad).
Registro auditable: dataset/metadata/enriquecimientos_v13.json.

Etapas (reanudables, en orden):
  --candidatos   embeddings + matching, escribe books/General/metadata/evc_candidatos.json
  --juzgar       veredictos Sonnet para la banda de duda
  --aplicar      ejecuta enriquecimientos y deja los CREAR en su lugar
"""
import json
import os
import sys
import time
from pathlib import Path

import requests
from dotenv import load_dotenv

BASE = Path(__file__).resolve().parents[2]
load_dotenv(BASE / ".env")

GENERAL = BASE / "books" / "General"
NODOS = GENERAL / "nodos"
META = GENERAL / "metadata"
ABSORBIDOS = GENERAL / "nodos_absorbidos"
REGISTRO = BASE / "dataset" / "metadata" / "enriquecimientos_v13.json"

VOYAGE_URL = "https://api.voyageai.com/v1/embeddings"
VOYAGE_MODEL = "voyage-4-lite"
DIM = 512
VOYAGE_API_KEY = os.environ.get("VOYAGE_API_KEY", "").strip()

MODEL = "claude-sonnet-5"
UMBRAL_CANDIDATO = 0.60

import re
import unicodedata


def a_ascii(texto):
    plano = unicodedata.normalize("NFKD", texto)
    plano = "".join(c for c in plano if not unicodedata.combining(c))
    plano = re.sub(r"[^a-z0-9_]+", "_", plano.lower())
    return re.sub(r"_+", "_", plano).strip("_")


def norm_titulo(t):
    return a_ascii(re.sub(r"\([^)]*\)", " ", t or ""))


def texto_nodo(n):
    partes = [n.get("titulo_concepto", ""), n.get("resumen_teorico", ""),
              " ".join(n.get("condiciones_activacion", []) or [])]
    return " ".join(p for p in partes if p).strip()


def _embeber(textos):
    for intento in range(6):
        r = requests.post(VOYAGE_URL,
                          headers={"Authorization": f"Bearer {VOYAGE_API_KEY}",
                                   "Content-Type": "application/json"},
                          json={"input": textos, "model": VOYAGE_MODEL,
                                "input_type": "document", "output_dimension": DIM},
                          timeout=120)
        if r.status_code == 429 and intento < 5:
            time.sleep(2 ** intento * 2)
            continue
        r.raise_for_status()
        items = sorted(r.json()["data"], key=lambda d: d["index"])
        return [it["embedding"] for it in items]
    raise RuntimeError("Voyage 429 persistente")


def cargar_core():
    graph = json.loads((BASE / "dataset" / "metadata" / "master_graph.json").read_text(encoding="utf-8"))["nodos"]
    idx = json.loads((BASE / "web" / "lib" / "assets" / "semantic_index.json").read_text(encoding="utf-8"))
    core_ids = {nid for nid, d in graph.items() if (d.get("dominio") or "core") == "core"}
    pares = [(nid, emb) for nid, emb in zip(idx["ids"], idx["embeddings"]) if nid in core_ids]
    return graph, pares


def cargar_generales():
    return {f.stem: json.loads(f.read_text(encoding="utf-8"))
            for f in sorted(NODOS.glob("*.json")) if not f.name.startswith("_")}


def etapa_candidatos():
    import numpy as np
    graph, pares_core = cargar_core()
    generales = cargar_generales()
    print(f"General: {len(generales)} nodos | core: {len(pares_core)} con embedding")

    ids_g = list(generales)
    textos = [texto_nodo(generales[i]) for i in ids_g]
    embs = []
    for i in range(0, len(textos), 128):
        embs.extend(_embeber(textos[i:i + 128]))
        print(f"  embebidos {min(i+128, len(textos))}/{len(textos)}")

    core_ids = [nid for nid, _ in pares_core]
    M = np.array([e for _, e in pares_core], dtype="float32")
    M /= np.linalg.norm(M, axis=1, keepdims=True)
    G = np.array(embs, dtype="float32")
    G /= np.linalg.norm(G, axis=1, keepdims=True)
    S = G @ M.T  # similitud coseno

    titulos_core = {norm_titulo(graph[nid].get("titulo_concepto", "")): nid for nid, _ in pares_core}

    candidatos, crear_directo = [], []
    for k, gid in enumerate(ids_g):
        fila = S[k]
        top = fila.argsort()[-3:][::-1]
        mejor = float(fila[top[0]])
        lex = titulos_core.get(norm_titulo(generales[gid].get("titulo_concepto", "")))
        if mejor >= UMBRAL_CANDIDATO or lex:
            candidatos.append({
                "general_id": gid,
                "titulo_general": generales[gid]["titulo_concepto"],
                "top_core": [{"core_id": core_ids[j], "score": round(float(fila[j]), 4),
                              "titulo": graph[core_ids[j]].get("titulo_concepto", "")} for j in top],
                "lexico": lex,
                "veredicto": None,
            })
        else:
            crear_directo.append({"general_id": gid, "mejor_score": round(mejor, 4)})

    META.mkdir(exist_ok=True)
    (META / "evc_candidatos.json").write_text(json.dumps(
        {"candidatos": candidatos, "crear_directo": crear_directo},
        ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"candidatos a juicio: {len(candidatos)} | crear directo: {len(crear_directo)}")


JUEZ_SYSTEM = """Eres el curador del grafo de conocimiento de "My Idea". Decides si un concepto NUEVO (de un libro complementario) duplica un concepto EXISTENTE del core.

Regla (del runbook): si el concepto ya existe -> ENRIQUECER el existente. Si es genuinamente nuevo -> CREAR. Umbral de duda: si es "parecido pero con ángulo distinto", se crea aparte SOLO si el ángulo CAMBIA LA ACCIÓN del emprendedor; si solo cambia el vocabulario o la fuente, se enriquece.

Recibirás pares {nuevo, existente}. Responde SOLO JSON: una lista de objetos
{"general_id": ..., "decision": "enriquecer"|"crear", "core_id": <el existente elegido si enriquecer, null si crear>, "motivo": "<una frase>"}"""


def etapa_juzgar():
    import anthropic
    client = anthropic.Anthropic()
    data = json.loads((META / "evc_candidatos.json").read_text(encoding="utf-8"))
    generales = cargar_generales()
    graph = json.loads((BASE / "dataset" / "metadata" / "master_graph.json").read_text(encoding="utf-8"))["nodos"]

    pendientes = [c for c in data["candidatos"] if c.get("veredicto") is None]
    print(f"a juzgar: {len(pendientes)}")
    uso = {"in": 0, "out": 0}
    LOTE = 12
    for i in range(0, len(pendientes), LOTE):
        lote = pendientes[i:i + LOTE]
        entrada = []
        for c in lote:
            g = generales[c["general_id"]]
            mejor = c["top_core"][0]
            core = graph[mejor["core_id"]]
            entrada.append({
                "general_id": c["general_id"],
                "nuevo": {"titulo": g["titulo_concepto"], "resumen": g["resumen_teorico"][:350],
                          "pasos": g.get("pasos_accionables", [])[:3]},
                "candidatos_core": [
                    {"core_id": t["core_id"], "score": t["score"],
                     "titulo": t["titulo"],
                     "resumen": graph[t["core_id"]].get("resumen_teorico", "")[:280]}
                    for t in c["top_core"][:2]
                ],
            })
        for intento in range(3):
            try:
                r = client.messages.create(model=MODEL, max_tokens=9000, system=JUEZ_SYSTEM,
                                           messages=[{"role": "user", "content": json.dumps(entrada, ensure_ascii=False)}])
                uso["in"] += r.usage.input_tokens
                uso["out"] += r.usage.output_tokens
                txt = next((b.text for b in r.content if getattr(b, "type", "") == "text"), "").strip()
                j = txt.find("[")
                veredictos = json.loads(txt[j:txt.rfind("]") + 1])
                break
            except Exception as e:
                print(f"  [reintento {intento+1}] {e}")
                time.sleep(5 * (intento + 1))
        else:
            continue
        por_id = {v["general_id"]: v for v in veredictos if isinstance(v, dict)}
        for c in lote:
            v = por_id.get(c["general_id"])
            if v and v.get("decision") in ("enriquecer", "crear"):
                c["veredicto"] = {"decision": v["decision"],
                                  "core_id": v.get("core_id"),
                                  "motivo": v.get("motivo", "")}
        (META / "evc_candidatos.json").write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print(f"  lote {i // LOTE + 1}: {len(por_id)} veredictos")
    costo = uso["in"] / 1e6 * 2.00 + uso["out"] / 1e6 * 10.00
    print(f"Juez: {uso['in']} in / {uso['out']} out | ${costo:.4f}")


def _paso_ya_cubierto(paso, existentes):
    na = a_ascii(paso)[:60]
    return any(na and na in a_ascii(e) or a_ascii(e)[:60] in na for e in existentes if e)


def etapa_aplicar():
    data = json.loads((META / "evc_candidatos.json").read_text(encoding="utf-8"))
    generales = cargar_generales()
    ABSORBIDOS.mkdir(exist_ok=True)
    registro = []
    enriquecidos, creados = 0, 0
    sin_veredicto = 0
    for c in data["candidatos"]:
        v = c.get("veredicto")
        if not v:
            sin_veredicto += 1
            continue
        gid = c["general_id"]
        if v["decision"] == "crear" or not v.get("core_id"):
            creados += 1
            continue
        core_id = v["core_id"]
        ruta_core = BASE / "dataset" / "nodos" / f"{core_id}.json"
        if not ruta_core.exists():
            print(f"  AVISO: core {core_id} no existe; {gid} queda como crear")
            creados += 1
            continue
        core = json.loads(ruta_core.read_text(encoding="utf-8"))
        g = generales[gid]
        # fuente: string "a | b" (graph.ts tipa string; el runbook pedia lista,
        # se registra la decision en el registro)
        if g["fuente"] not in core["fuente"]:
            core["fuente"] = core["fuente"] + " | " + g["fuente"]
        aportados = []
        for paso in g.get("pasos_accionables", []):
            if not _paso_ya_cubierto(paso, core.get("pasos_accionables", [])):
                core.setdefault("pasos_accionables", []).append(paso)
                aportados.append(paso)
        ruta_core.write_text(json.dumps(core, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        # el nodo general queda absorbido (trazabilidad completa)
        origen = NODOS / f"{gid}.json"
        (ABSORBIDOS / f"{gid}.json").write_text(origen.read_text(encoding="utf-8"), encoding="utf-8")
        origen.unlink()
        registro.append({"core_id": core_id, "absorbio": gid, "libro": g["fuente"],
                         "que_aporto": {"fuente": True, "pasos_nuevos": aportados},
                         "motivo": v.get("motivo", ""), "score": c["top_core"][0]["score"]})
        enriquecidos += 1
    REGISTRO.write_text(json.dumps(registro, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"enriquecidos: {enriquecidos} | crear (tras juicio): {creados} | sin veredicto: {sin_veredicto}")
    print(f"crear directo (score<{UMBRAL_CANDIDATO}): {len(data['crear_directo'])}")
    print(f"registro: {REGISTRO}")


if __name__ == "__main__":
    if "--candidatos" in sys.argv:
        etapa_candidatos()
    elif "--juzgar" in sys.argv:
        etapa_juzgar()
    elif "--aplicar" in sys.argv:
        etapa_aplicar()
    else:
        print(__doc__)
