#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""consolidar_pack.py - Ejecuta la fusion podada de un pack.

Solo corre sobre el archivo de poda YA APROBADO por el fundador. Sin el, no
arranca: ningun nodo se funde sin visto.

QUE HACE, por cluster:
  1. El SUPERVIVIENTE (elegido por la regla ya adoptada: mas historia; sin
     historia, el propuesto) hereda las mejores piezas de sus absorbidos. Lo
     redacta el modelo con los nodos del cluster delante y la orden de no
     inventar: lo que no este en alguno de ellos, no se escribe.
  2. Los ABSORBIDOS se marcan `deprecado: true`. NO se borran. Conservan
     archivo, id, titulo, resumen y aristas: la historia queda intacta y
     resuelve. Lo unico que pierden es la elegibilidad, y de eso se encarga la
     puerta unica (esOfrecible).
  3. El superviviente recoge `ids_alias` y `merged_originals` con la
     procedencia, y HEREDA las aristas de los absorbidos: si un camino activo
     pasaba por un absorbido, ahora pasa por el superviviente. Sin esa herencia,
     lo que colgaba detras de un absorbido quedaria fuera del universo activo.

LA BARANDA ANTI-INVENCION, comprobable sin criterio: toda CIFRA del texto
resultante tiene que aparecer en alguno de los nodos del cluster. Es donde el
modelo inventa primero cuando funde (un porcentaje, un plazo, un umbral), y es
lo unico de "cero invencion" que se puede verificar a maquina. Lo demas lo
sostiene el prompt y el muestreo del fundador.

Uso:
  python scripts/consolidar_pack.py --pack quality --dry-run
  python scripts/consolidar_pack.py --pack quality
"""
import argparse
import json
import os
import re
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import libro_mayor  # noqa: E402

BASE = Path(__file__).resolve().parent.parent
NODOS = BASE / "dataset" / "nodos"
MODEL = "claude-sonnet-5"
TECHOS = (16000, 32000, 64000)
PRECIO_IN, PRECIO_OUT = 2.00, 10.00
PALABRAS = (80, 150)

SYSTEM = """Eres el editor de un grafo de conocimiento para emprendedores.

Recibes un CLUSTER de nodos que describen el mismo concepto con distintos
nombres y matices, y cual de ellos SOBREVIVE. Tu trabajo es escribir el
contenido del superviviente heredando lo mejor de todos.

REGLAS QUE NO SE NEGOCIAN:
1. CERO INVENCION. Todo lo que escribas tiene que estar en alguno de los nodos
   del cluster. No agregues datos, cifras, plazos ni ejemplos nuevos. Si una
   cifra no aparece en ninguno, NO la escribas: el nodo se rechaza por eso.
2. El titulo del superviviente se CONSERVA tal cual. No lo mejores.
3. resumen_teorico: entre 80 y 150 palabras. Recoge los matices que aportaban
   los absorbidos y que el superviviente no tenia. Si dos dicen lo mismo, una
   vez basta.
4. pasos_accionables: de 3 a 6, imperativos y concretos. Une los de todos sin
   repetir. Si sobran, quedate con los que cambian lo que la persona hace.
5. condiciones_activacion: de 2 a 4, situaciones del emprendedor.
6. entregable_esperado: una frase, el artefacto que queda en la mano.
7. PROHIBIDOS los guiones largos y medios.
8. El tono le habla a UNA persona sola, con un telefono. Si el texto original
   asume equipos, comites o direccion, tradúcelo, pero SIN inventar.

Devuelve EXCLUSIVAMENTE un objeto JSON, sin markdown, con estos campos y
ninguno mas:
{"resumen_teorico": "...", "pasos_accionables": ["..."],
 "entregable_esperado": "...", "condiciones_activacion": ["..."]}"""


def _texto(r):
    for b in r.content:
        if getattr(b, "type", "") == "text":
            return b.text
    return ""


def _objeto(t):
    t = t.strip()
    for v in ("```json", "```"):
        if t.startswith(v):
            t = t[len(v):]
    if t.endswith("```"):
        t = t[:-3]
    i, j = t.find("{"), t.rfind("}")
    return t[i:j + 1] if i != -1 and j > i else t


def llamar(cli, prompt, uso):
    ultimo = None
    for techo in TECHOS:
        for intento in range(3):
            try:
                with cli.messages.stream(model=MODEL, max_tokens=techo, system=SYSTEM,
                                         messages=[{"role": "user", "content": prompt}]) as s:
                    r = s.get_final_message()
                uso["in"] += r.usage.input_tokens
                uso["out"] += r.usage.output_tokens
                if r.stop_reason == "max_tokens":
                    ultimo = "cortada"
                    break
                return json.loads(_objeto(_texto(r))), None
            except json.JSONDecodeError as e:
                ultimo = f"JSON invalido: {e}"
            except Exception as e:
                ultimo = str(e)
                time.sleep(5 * (intento + 1))
    return None, ultimo or "fallo"


RE_CIFRA = re.compile(r"\d+(?:[.,]\d+)?")


def cifras_inventadas(nuevo, fuentes):
    """Cifras del texto nuevo que no aparecen en ninguno de los nodos fuente."""
    en_fuente = set()
    for f in fuentes:
        en_fuente |= set(RE_CIFRA.findall(f))
    return sorted({c for c in RE_CIFRA.findall(nuevo) if c not in en_fuente})


def texto_de(n):
    return " ".join([n.get("titulo_concepto", ""), n.get("resumen_teorico", ""),
                     " ".join(n.get("pasos_accionables") or []),
                     " ".join(n.get("condiciones_activacion") or []),
                     n.get("entregable_esperado", "") or ""])


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--pack", required=True)
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    poda = json.loads((BASE / "packs" / args.pack / "poda" /
                       f"_poda_{args.pack}.json").read_text(encoding="utf-8"))
    clusters = poda["clusters"]
    absorbidos_total = sum(len(c["nodos"]) - 1 for c in clusters)
    print(f"  {len(clusters)} clusters, {absorbidos_total} absorbidos")
    if args.dry_run:
        return

    from dotenv import load_dotenv
    import anthropic
    load_dotenv(BASE / ".env")
    cli = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
    uso = {"in": 0, "out": 0}
    hechos, rechazos, muestra, absorbidos_hechos = 0, [], [], 0

    for c in clusters:
        gana = c["sobrevive"]
        otros = [n for n in c["nodos"] if n != gana]
        rutas = {n: NODOS / f"{n}.json" for n in c["nodos"]}
        if not all(p.exists() for p in rutas.values()):
            rechazos.append({"cluster": c["orden"], "motivo": "falta algun archivo"})
            continue
        nodos = {n: json.loads(p.read_text(encoding="utf-8")) for n, p in rutas.items()}

        bloque = [f"SOBREVIVE: {nodos[gana].get('titulo_concepto')}", ""]
        for n in c["nodos"]:
            d = nodos[n]
            bloque.append(f"--- {'SUPERVIVIENTE' if n == gana else 'ABSORBIDO'}: {d.get('titulo_concepto')}")
            bloque.append(f"resumen: {d.get('resumen_teorico','')}")
            bloque.append(f"pasos: {json.dumps(d.get('pasos_accionables') or [], ensure_ascii=False)}")
            bloque.append(f"condiciones: {json.dumps(d.get('condiciones_activacion') or [], ensure_ascii=False)}")
            bloque.append(f"entregable: {d.get('entregable_esperado','')}")
        nuevo, err = llamar(cli, "\n".join(bloque), uso)
        if err or not isinstance(nuevo, dict):
            rechazos.append({"cluster": c["orden"], "motivo": err or "respuesta no es objeto"})
            continue

        fuentes = [texto_de(nodos[n]) for n in c["nodos"]]
        todo = " ".join([nuevo.get("resumen_teorico", ""),
                         " ".join(nuevo.get("pasos_accionables") or []),
                         " ".join(nuevo.get("condiciones_activacion") or []),
                         nuevo.get("entregable_esperado", "") or ""])
        inventadas = cifras_inventadas(todo, fuentes)
        palabras = len((nuevo.get("resumen_teorico") or "").split())
        problemas = []
        if inventadas:
            problemas.append(f"cifras que no estan en ningun nodo del cluster: {inventadas}")
        if not (PALABRAS[0] <= palabras <= PALABRAS[1]):
            problemas.append(f"resumen de {palabras} palabras")
        if any(g in todo for g in ("—", "–")):
            problemas.append("guion largo")
        if problemas:
            rechazos.append({"cluster": c["orden"], "superviviente": gana, "motivo": problemas})
            continue

        # --- el superviviente hereda ---
        d = nodos[gana]
        antes_resumen = d.get("resumen_teorico", "")
        for k in ("resumen_teorico", "pasos_accionables", "entregable_esperado",
                  "condiciones_activacion"):
            if nuevo.get(k):
                d[k] = nuevo[k]
        alias = list(d.get("ids_alias") or [])
        merged = list(d.get("merged_originals") or [])
        for n in otros:
            if n not in alias:
                alias.append(n)
            merged.append({"node_id": n, "titulo": nodos[n].get("titulo_concepto", ""),
                           "fuente": nodos[n].get("fuente", "")})
            # HEREDA las aristas: sin esto, lo que colgaba detras de un
            # absorbido saldria del universo activo al deprecarlo.
            for campo in ("nodos_previos", "nodos_siguientes"):
                for r in nodos[n].get(campo) or []:
                    if r != gana and r not in (d.get(campo) or []) and r not in otros:
                        d.setdefault(campo, []).append(r)
        d["ids_alias"] = alias
        d["merged_originals"] = merged
        rutas[gana].write_text(json.dumps(d, ensure_ascii=False, indent=2), encoding="utf-8")

        # --- los absorbidos se deprecan, NO se borran ---
        for n in otros:
            nodos[n]["deprecado"] = True
            rutas[n].write_text(json.dumps(nodos[n], ensure_ascii=False, indent=2), encoding="utf-8")

        hechos += 1
        absorbidos_hechos += len(otros)
        if len(muestra) < 5:
            muestra.append({"cluster": c["orden"], "superviviente": gana,
                            "titulo": d.get("titulo_concepto"),
                            "absorbio": [nodos[n].get("titulo_concepto") for n in otros],
                            "resumen_antes": antes_resumen, "resumen_despues": d["resumen_teorico"]})
        print(f"  [{c['orden']:>2}/{len(clusters)}] {gana}: absorbe {len(otros)}")

    salida = BASE / "packs" / args.pack / "poda"
    (salida / "_consolidacion.json").write_text(json.dumps({
        "clusters_hechos": hechos, "rechazos": rechazos, "muestra": muestra,
        "costo_usd": round(uso["in"] / 1e6 * PRECIO_IN + uso["out"] / 1e6 * PRECIO_OUT, 2),
        "tokens": uso,
    }, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"\n  Fundidos {hechos}/{len(clusters)}. Rechazados {len(rechazos)}.")
    costo = uso["in"] / 1e6 * PRECIO_IN + uso["out"] / 1e6 * PRECIO_OUT
    libro_mayor.anotar(args.pack, "consolidacion", costo,
                       clusters=hechos, absorbidos=absorbidos_hechos, tokens=uso)
    print(f"  Costo: ${costo:.2f}")
    if rechazos:
        print(f"  Los rechazos, con motivo, en {salida / '_consolidacion.json'}")


if __name__ == "__main__":
    main()
