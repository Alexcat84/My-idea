# -*- coding: utf-8 -*-
"""CORRECCION DECLARADA DE LAS PREGUNTAS BASE (decision del fundador, cuarta vuelta de la corrida final, 8 oct 2026).

El voseo, el ingles y las formas rotas son defectos que se corrigen tambien en las bases (REGLAS_DE_LA_CASA C34):
  1. --leer: un LECTOR (Sonnet 5.5, en tandas de 20) marca en las bases las frases en ingles y las formas rotas, con
     su fragmento exacto. El voseo lo detecta la regla general (build_question_cache.voseo_en), sin modelo.
     Guarda docs/corrida_final/2026-10-08/lector_bases.json.
  2. --corregir: cada base con algun problema pasa por engine/neutral_niveles.corregir_base: edicion minima (solo el
     fragmento del problema), comprobaciones automaticas y juez independiente. Si duda, la base NO se toca y queda en
     el residuo. Cada correccion se declara en engine/correcciones_preguntas.json (antes, despues, clases, cambios,
     fecha) y la neutral de esa base se marca para rehacer.

Uso (con ANTHROPIC_API_KEY):  python scripts/corrida_final/corregir_bases.py --leer --yes
                              python scripts/corrida_final/corregir_bases.py --corregir --yes
"""
import json
import sys
from collections import Counter
from datetime import date
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(BASE / "engine"))
import build_question_cache as bqc  # noqa: E402
import neutral_niveles as nn  # noqa: E402

LECTURA = BASE / "docs" / "corrida_final" / "2026-10-08" / "lector_bases.json"
REGISTRO = BASE / "engine" / "correcciones_preguntas.json"
TANDA = 20

SYSTEM_LECTOR = (
    "Eres un corrector de espanol neutro. Recibes una lista de preguntas de una entrevista de emprendimiento, cada una "
    "con su id. Marca SOLO las que tienen (a) una palabra o frase en INGLES que no sea un termino de uso comun en el "
    "oficio, o (b) una FORMA ROTA: concordancia de numero, genero o persona equivocada, un verbo que no concuerda con su "
    "sujeto, una palabra que sobra o falta, o una frase que no se entiende tal como esta escrita. NO marques estilo, "
    "preguntas largas, voseo, tuteo ni terminos del oficio aceptados. Para cada marcada da el fragmento EXACTO mas corto "
    "que contiene el error, copiado tal cual. Responde SOLO un JSON: "
    "{\"marcadas\": [{\"id\": str, \"clase\": \"ingles\" o \"forma_rota\", \"fragmento\": str, \"motivo\": str}]}."
)


def bases_vivas(cache, graph):
    return [(nid, e["pregunta"]) for nid, e in cache.items()
            if e.get("pregunta") and nid in graph and not graph[nid].get("deprecado")]


def leer(client, cache, graph):
    vivas = bases_vivas(cache, graph)
    marcadas, tok = [], Counter()
    for i in range(0, len(vivas), TANDA):
        lote = vivas[i:i + TANDA]
        msg = client.messages.create(
            model=nn.MODELO_JUEZ, **nn.PARAMETROS_JUEZ, max_tokens=1500,
            system=[{"type": "text", "text": SYSTEM_LECTOR}],
            messages=[{"role": "user", "content": json.dumps([{"id": n, "pregunta": t} for n, t in lote], ensure_ascii=False)}])
        tok["juez_in"] += msg.usage.input_tokens
        tok["juez_out"] += msg.usage.output_tokens
        try:
            res = bqc._json_de(nn._texto_de(msg)).get("marcadas") or []
        except ValueError:
            res = []
        ids = {n for n, _ in lote}
        for m in res:
            if isinstance(m, dict) and m.get("id") in ids and m.get("clase") in ("ingles", "forma_rota") and m.get("fragmento"):
                marcadas.append(m)
        if (i // TANDA) % 20 == 0:
            print(f"  leidas {min(i + TANDA, len(vivas))}/{len(vivas)} | marcadas {len(marcadas)}", flush=True)
    costo = (tok["juez_in"] * nn.PRECIO_JUEZ["in"] + tok["juez_out"] * nn.PRECIO_JUEZ["out"]) / 1_000_000
    LECTURA.write_text(json.dumps({"marcadas": marcadas, "costo_usd": round(costo, 4), "leidas": len(vivas)},
                                  ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"lector: {len(vivas)} bases leidas, {len(marcadas)} marcadas | costo real ${costo:.4f}")


def corregir(client, cache, graph):
    lectura = json.loads(LECTURA.read_text(encoding="utf-8"))["marcadas"] if LECTURA.exists() else []
    extras = {}
    for m in lectura:
        extras.setdefault(m["id"], []).append({"clase": m["clase"], "fragmento": m["fragmento"]})
    registro = json.loads(REGISTRO.read_text(encoding="utf-8")) if REGISTRO.exists() else []
    tot, clases, residuo = Counter(), Counter(), []
    hechas = 0
    for nid, base in bases_vivas(cache, graph):
        if not bqc.voseo_en(base) and nid not in extras:
            continue
        r = nn.corregir_base(client, client, nid, base, graph, extras.get(nid, []))
        for k in ("tokens_in", "tokens_out", "cache_read", "cache_write", "juez_in", "juez_out", "juez_read", "juez_write"):
            tot[k] += r[k]
        if r["corregida"] is None:
            if r["motivo"] != "sin_problemas_de_base":
                residuo.append({"nid": nid, "pregunta": base, "motivo": r["motivo"], "extras": extras.get(nid, [])})
            continue
        registro.append({"nid": nid, "campo": "pregunta", "antes": base, "despues": r["corregida"], "clases": r["clases"],
                         "cambios": r["cambios"], "fecha": date.today().isoformat(),
                         "verificacion": "edicion minima + comprobaciones automaticas + juez independiente (Sonnet 5.5)",
                         "decision": "fundador, cuarta vuelta de la corrida final (REGLAS C34)"})
        e = {k: v for k, v in cache[nid].items() if k not in ("pregunta_neutral", "pregunta_neutral_nivel")}
        e["pregunta"] = r["corregida"]
        cache[nid] = e
        hechas += 1
        for c in r["clases"]:
            clases[c] += 1
    bqc.CACHE_PATH.write_text(json.dumps(cache, ensure_ascii=False, indent=2), encoding="utf-8")
    REGISTRO.write_text(json.dumps(registro, ensure_ascii=False, indent=2), encoding="utf-8")
    (BASE / "docs" / "corrida_final" / "2026-10-08" / "residuo_correccion_bases.json").write_text(
        json.dumps(residuo, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"corregidas {hechas} bases ({dict(clases)}) | residuo sin tocar {len(residuo)} | costo real ${nn.costo_usd(tot):.4f}")


def solo_voseo(client, cache, graph):
    """El voseo que quede, solo el voseo, en toda base viva (sin las marcas del lector)."""
    registro = json.loads(REGISTRO.read_text(encoding="utf-8")) if REGISTRO.exists() else []
    tot, hechas, quedan = Counter(), 0, []
    for nid, base in bases_vivas(cache, graph):
        if not bqc.voseo_en(base):
            continue
        r = nn.corregir_base(client, client, nid, base, graph, [])
        for k in ("tokens_in", "tokens_out", "cache_read", "cache_write", "juez_in", "juez_out", "juez_read", "juez_write"):
            tot[k] += r[k]
        if not r["corregida"]:
            quedan.append((nid, r["motivo"]))
            continue
        registro.append({"nid": nid, "campo": "pregunta", "antes": base, "despues": r["corregida"], "clases": r["clases"],
                         "cambios": r["cambios"], "fecha": date.today().isoformat(),
                         "verificacion": "edicion minima + comprobaciones automaticas + juez independiente (Sonnet 5.5)",
                         "decision": "fundador, cuarta vuelta de la corrida final (REGLAS C34), voseo"})
        e = {k: v for k, v in cache[nid].items() if k not in ("pregunta_neutral", "pregunta_neutral_nivel")}
        e["pregunta"] = r["corregida"]
        cache[nid] = e
        hechas += 1
    bqc.CACHE_PATH.write_text(json.dumps(cache, ensure_ascii=False, indent=2), encoding="utf-8")
    REGISTRO.write_text(json.dumps(registro, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"voseo: corregidas {hechas} | quedan {len(quedan)} {quedan} | costo real ${nn.costo_usd(tot):.4f}")


def segunda_pasada(client, cache, graph):
    """El residuo de la primera: (1) el voseo SOLO, sin las marcas del lector, en toda base que aun lo tenga; (2) las
    formas rotas e ingles del residuo con fragmentos de hasta 12 palabras. Mismas comprobaciones y juez."""
    residuo_previo = json.loads((BASE / "docs" / "corrida_final" / "2026-10-08" / "residuo_correccion_bases.json")
                                .read_text(encoding="utf-8"))
    extras = {x["nid"]: x.get("extras", []) for x in residuo_previo}
    registro = json.loads(REGISTRO.read_text(encoding="utf-8")) if REGISTRO.exists() else []
    tot, clases, residuo = Counter(), Counter(), []
    hechas = 0

    def aplica(nid, r):
        nonlocal hechas
        registro.append({"nid": nid, "campo": "pregunta", "antes": cache[nid]["pregunta"], "despues": r["corregida"],
                         "clases": r["clases"], "cambios": r["cambios"], "fecha": date.today().isoformat(),
                         "verificacion": "edicion minima + comprobaciones automaticas + juez independiente (Sonnet 5.5)",
                         "decision": "fundador, cuarta vuelta de la corrida final (REGLAS C34), segunda pasada"})
        e = {k: v for k, v in cache[nid].items() if k not in ("pregunta_neutral", "pregunta_neutral_nivel")}
        e["pregunta"] = r["corregida"]
        cache[nid] = e
        hechas += 1
        for c in r["clases"]:
            clases[c] += 1

    def suma(r):
        for k in ("tokens_in", "tokens_out", "cache_read", "cache_write", "juez_in", "juez_out", "juez_read", "juez_write"):
            tot[k] += r[k]

    for nid, base in bases_vivas(cache, graph):
        motivo = None
        if bqc.voseo_en(base):
            r = nn.corregir_base(client, client, nid, base, graph, [])
            suma(r)
            if r["corregida"]:
                aplica(nid, r)
            else:
                motivo = "voseo:" + str(r["motivo"])
        if nid in extras:
            actual = cache[nid]["pregunta"]
            vivos = [x for x in extras[nid] if x.get("fragmento") and actual.count(x["fragmento"]) == 1]
            if vivos:
                r = nn.corregir_base(client, client, nid, actual, graph, vivos, max_frag=12)
                suma(r)
                if r["corregida"]:
                    aplica(nid, r)
                elif r["motivo"] != "sin_problemas_de_base":
                    motivo = (motivo + "; " if motivo else "") + "lector:" + str(r["motivo"])
        if motivo:
            residuo.append({"nid": nid, "pregunta": cache[nid]["pregunta"], "motivo": motivo, "extras": extras.get(nid, [])})
    bqc.CACHE_PATH.write_text(json.dumps(cache, ensure_ascii=False, indent=2), encoding="utf-8")
    REGISTRO.write_text(json.dumps(registro, ensure_ascii=False, indent=2), encoding="utf-8")
    (BASE / "docs" / "corrida_final" / "2026-10-08" / "residuo_correccion_bases.json").write_text(
        json.dumps(residuo, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"segunda pasada: corregidas {hechas} ({dict(clases)}) | residuo {len(residuo)} | costo real ${nn.costo_usd(tot):.4f}")


def main():
    if "--yes" not in sys.argv:
        print("Gasta API: pasa --yes.")
        return 1
    import anthropic
    client = anthropic.Anthropic()
    graph = bqc.cargar_grafo()
    cache = json.loads(bqc.CACHE_PATH.read_text(encoding="utf-8"))
    if "--leer" in sys.argv:
        leer(client, cache, graph)
    if "--corregir" in sys.argv:
        corregir(client, cache, graph)
    if "--voseo" in sys.argv:
        solo_voseo(client, cache, graph)
    if "--segunda-pasada" in sys.argv:
        segunda_pasada(client, cache, graph)
    return 0


if __name__ == "__main__":
    sys.exit(main())
