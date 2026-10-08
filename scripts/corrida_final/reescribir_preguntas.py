# -*- coding: utf-8 -*-
"""Reescritura de preguntas nuevas tras su auditoria ciega (decision del fundador, corrida final, 8 oct 2026).

Lee docs/corrida_final/2026-10-08/reescritura_preguntas_nuevas.json (por nodo: la pregunta actual, los motivos del
juez y del arbitro, y la correccion), redacta cada pregunta de nuevo con el MISMO generador de la cache
(engine/build_question_cache.py: SYSTEM_PREGUNTA_CON_REGLA, Haiku 5.5 sin razonamiento por defecto) mas la correccion,
la guarda como pregunta del nodo y BORRA su pregunta_neutral para que --neutrales la rehaga sobre la pregunta nueva.

Solo toca los nodos del archivo, que son preguntas nacidas en esta corrida (--faltantes): ninguna base anterior.
El antes y el despues quedan en el mismo archivo (campo pregunta_nueva) para la evidencia.

Uso (con ANTHROPIC_API_KEY en el entorno):  python scripts/corrida_final/reescribir_preguntas.py --yes [--solo <nid>]
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent / "engine"))
import build_question_cache as bqc  # noqa: E402

BASE = Path(__file__).resolve().parent.parent.parent
LISTA = BASE / "docs" / "corrida_final" / "2026-10-08" / "reescritura_preguntas_nuevas.json"
ANTES = BASE / "docs" / "corrida_final" / "2026-10-08" / "preguntas_nuevas.json"

ADENDA = (
    "\n\nREESCRITURA: ademas del concepto y sus siguientes, recibes la pregunta_actual de este nodo y una correccion "
    "que dice que falla en ella. Redacta UNA pregunta nueva que cumpla todas las reglas de arriba y la correccion. "
    "Responde SOLO un JSON: {\"pregunta\": str}."
)


def main():
    if "--yes" not in sys.argv:
        print("Gasta API: pasa --yes.")
        return 1
    import anthropic
    client = anthropic.Anthropic()
    graph = bqc.cargar_grafo()
    cache = json.loads(bqc.CACHE_PATH.read_text(encoding="utf-8"))
    nacidas = set(json.loads(ANTES.read_text(encoding="utf-8")))
    lista = json.loads(LISTA.read_text(encoding="utf-8"))
    solo = sys.argv[sys.argv.index("--solo") + 1] if "--solo" in sys.argv else None
    elegibles = bqc.nodos_elegibles(graph)
    t_in = t_out = c_read = c_write = 0
    for item in lista:
        nid = item["nid"]
        if solo and nid != solo:
            continue
        assert nid in nacidas, f"{nid} no es una pregunta nacida en esta corrida: no se toca"
        actual = graph[nid]
        candidatos = elegibles[nid]
        ctx = {
            "concepto_actual": {
                "titulo": actual["titulo_concepto"],
                "resumen": actual["resumen_teorico"][:400],
                "condicion": (actual.get("condiciones_activacion") or [""])[0],
                "entregable": actual.get("entregable_esperado") or "",
            },
            "conceptos_siguientes": [
                {"titulo": graph[c]["titulo_concepto"], "condiciones_activacion": graph[c].get("condiciones_activacion", [])[:3]}
                for c in candidatos
            ],
            "pregunta_actual": item["pregunta_actual"],
            "correccion": item["correccion"],
        }
        msg = client.messages.create(
            model=bqc.MODEL,
            **bqc.PARAMETROS_MODELO,
            max_tokens=300,
            system=[{"type": "text", "text": bqc.SYSTEM_PREGUNTA_CON_REGLA + ADENDA, "cache_control": {"type": "ephemeral"}}],
            messages=[{"role": "user", "content": json.dumps(ctx, ensure_ascii=False)}],
        )
        t_in += msg.usage.input_tokens
        t_out += msg.usage.output_tokens
        r, w = bqc._cache_de(msg.usage)
        c_read += r
        c_write += w
        if msg.stop_reason == "max_tokens":
            raise SystemExit(f"{nid}: respuesta cortada")
        raw = "".join(b.text for b in msg.content if b.type == "text")
        nueva = bqc._json_de(raw)["pregunta"].strip()
        motivo = bqc.comprobar_neutral(item["pregunta_actual"], nueva)  # mismas comprobaciones de forma
        if motivo:
            raise SystemExit(f"{nid}: la pregunta nueva no pasa ({motivo}): {nueva}")
        cache[nid] = {k: v for k, v in cache[nid].items() if k != "pregunta_neutral"}
        cache[nid]["pregunta"] = nueva
        item["pregunta_nueva"] = nueva
        print(f"{nid}\n  antes: {item['pregunta_actual']}\n  ahora: {nueva}")
    bqc.CACHE_PATH.write_text(json.dumps(cache, ensure_ascii=False, indent=2), encoding="utf-8")
    LISTA.write_text(json.dumps(lista, ensure_ascii=False, indent=2), encoding="utf-8")
    costo = bqc.costo_usd({"tokens_in": t_in, "tokens_out": t_out, "cache_read": c_read, "cache_write": c_write})
    print(f"\n{len(lista)} reescritas | tokens {t_in} in / {t_out} out / cache {c_read} leidos, {c_write} escritos | "
          f"costo real: ${costo:.4f}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
