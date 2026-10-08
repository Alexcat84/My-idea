# -*- coding: utf-8 -*-
"""Neutrales de RESPALDO con Sonnet 5.5 para las que Haiku 5.5 no logra (corrida final, 8 oct 2026).

Tras regenerar las 3.417 neutrales con el generador corregido (cuatro reglas de fidelidad), cinco pasadas de Haiku 5.5
dejaron 85 sin neutral: el modelo volvia a cerrar con una pregunta anadida o a perder el tema concreto. Un diagnostico
con Sonnet 5.5 resolvio 8 de 10 al primer intento. Este script genera SOLO las que faltan, con las MISMAS
instrucciones (SYSTEM_NEUTRAL) y los MISMOS rechazos (comprobar_neutral), y declara cada nodo que hizo en
docs/corrida_final/2026-10-08/neutrales_respaldo_sonnet.json. La base no se toca.

Uso (con ANTHROPIC_API_KEY en el entorno):  python scripts/corrida_final/neutrales_respaldo.py --yes
"""
import json
import sys
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(BASE / "engine"))
import build_question_cache as bqc  # noqa: E402

MODELO = "claude-sonnet-5-5"
# Por millon: entrada 2, salida 10; lectura de cache al 5 % de la entrada, escritura al 125 %.
PRECIO = {"in": 2.0, "out": 10.0, "read": 0.10, "write": 2.50}
REGISTRO = BASE / "docs" / "corrida_final" / "2026-10-08" / "neutrales_respaldo_sonnet.json"
INTENTOS = 4


def generar(client, nid, base, candidatos, graph):
    n = graph[nid]
    ctx = {
        "pregunta_base": base,
        "concepto": {"etiqueta": n.get("etiqueta_arbol") or n["titulo_concepto"], "resumen": n.get("resumen_teorico", "")[:400]},
        "temas_siguientes": [graph[c].get("etiqueta_arbol") or graph[c]["titulo_concepto"] for c in candidatos if c in graph][:6],
    }
    msg = client.messages.create(
        model=MODELO,
        thinking={"type": "between_tools"},  # Sonnet 5.5 razona por defecto y rechaza "disabled"
        max_tokens=600,
        system=[{"type": "text", "text": bqc.SYSTEM_NEUTRAL, "cache_control": {"type": "ephemeral"}}],
        messages=[{"role": "user", "content": json.dumps(ctx, ensure_ascii=False)}],
    )
    raw = "".join(b.text for b in msg.content if b.type == "text")
    texto = ""
    if msg.stop_reason != "max_tokens":
        try:
            texto = str(bqc._json_de(raw).get("pregunta_neutral", "")).strip()
        except ValueError:
            texto = ""
    return texto, msg.usage


def main():
    if "--yes" not in sys.argv:
        print("Gasta API: pasa --yes.")
        return 1
    import anthropic
    client = anthropic.Anthropic()
    graph = bqc.cargar_grafo()
    cache = json.loads(bqc.CACHE_PATH.read_text(encoding="utf-8"))
    trabajo = [(nid, "pregunta", "pregunta_neutral") for nid in bqc.objetivos_neutrales(cache, graph)]
    trabajo += [(nid, "pregunta_entrada", "pregunta_entrada_neutral")
                for nid in bqc.objetivos_neutrales(cache, graph, "pregunta_entrada", "pregunta_entrada_neutral")]
    registro = json.loads(REGISTRO.read_text(encoding="utf-8")) if REGISTRO.exists() else []
    tok = {"in": 0, "out": 0, "read": 0, "write": 0}
    fallidas = []
    for nid, origen, destino in trabajo:
        base = cache[nid][origen]
        ultimo = None
        for _ in range(INTENTOS):
            texto, u = generar(client, nid, base, cache[nid].get("candidatos", []), graph)
            r, w = bqc._cache_de(u)
            tok["in"] += u.input_tokens
            tok["out"] += u.output_tokens
            tok["read"] += r
            tok["write"] += w
            ultimo = bqc.comprobar_neutral(base, texto) if texto else "sin_texto"
            if ultimo is None:
                cache[nid] = {**cache[nid], destino: texto}
                assert cache[nid][origen] == base
                registro.append({"nid": nid, "campo": destino, "modelo": MODELO})
                break
        if ultimo is not None:
            fallidas.append((nid, destino, ultimo))
            print(f"  FALLO {nid} ({destino}): {ultimo}")
    bqc.CACHE_PATH.write_text(json.dumps(cache, ensure_ascii=False, indent=2), encoding="utf-8")
    REGISTRO.write_text(json.dumps(registro, ensure_ascii=False, indent=2), encoding="utf-8")
    costo = sum(tok[k] * PRECIO[k] for k in tok) / 1_000_000
    print(f"respaldo Sonnet 5.5: hechas {len(trabajo) - len(fallidas)} de {len(trabajo)}, fallidas {len(fallidas)} | "
          f"tokens {tok['in']} in / {tok['out']} out / cache {tok['read']} leidos, {tok['write']} escritos | "
          f"costo real: ${costo:.4f}")
    return 0 if not fallidas else 1


if __name__ == "__main__":
    sys.exit(main())
