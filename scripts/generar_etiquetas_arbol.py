# -*- coding: utf-8 -*-
"""Expansión v1.3 — etiqueta_arbol (estándar nuevo del RUNBOOK §1).

Genera para cada nodo una etiqueta de árbol: el nombre amable que el riel
de la UI muestra al usuario (el canon 04 lo llama "título original" vs el
nombre del riel: 'Hoja de Estimación de Costos' -> 'Piensa tus Costos
Reales'). Reglas de voz: 4-5 palabras, segunda persona, cero anglicismos
ni autores. Campo adicional `etiqueta_arbol` en el JSON del nodo (la UI
lo consumirá cuando se cablee; hoy es inofensivo).

Parametrizado y reanudable: salta nodos que ya tienen etiqueta valida.

Uso:
  python scripts/generar_etiquetas_arbol.py <carpeta_nodos> [...carpetas]
"""
import json
import os
import re
import sys
import time
from pathlib import Path

from dotenv import load_dotenv

BASE = Path(__file__).resolve().parent.parent
load_dotenv(BASE / ".env")

MODEL = "claude-sonnet-5"
LOTE = 40
PRICE_IN, PRICE_OUT = 2.00, 10.00  # intro hasta 2026-08-31

SYSTEM = """Eres el redactor de la interfaz de "My Idea", una app en español que acompaña a emprendedores.
Para cada concepto recibirás su id, título formal y un resumen. Devuelve una ETIQUETA DE ÁRBOL: el nombre corto y humano con el que la app mostrará ese paso en el riel del recorrido.

REGLAS DE VOZ (obligatorias):
- 4 a 5 palabras (nunca más de 6, nunca menos de 3).
- Segunda persona o imperativo cercano ("Piensa tus Costos Reales", "Atiende a Mano, Primero", "Tu Apuesta Más Grande").
- Español común: CERO anglicismos, CERO siglas salvo universales (ROI no, IVA sí), CERO nombres de autores, libros o marcas.
- Debe capturar la ACCIÓN o decisión del concepto, no su taxonomía.
- Mayúsculas de título en español (primera letra de palabras significativas).

Responde SOLO un objeto JSON: {"<id>": "<etiqueta>", ...} con TODOS los ids recibidos. Sin markdown."""


def extraer_json(texto):
    i = texto.find("{")
    if i == -1:
        return texto
    depth = 0
    in_s = False
    esc = False
    for j in range(i, len(texto)):
        ch = texto[j]
        if in_s:
            if esc:
                esc = False
            elif ch == "\\":
                esc = True
            elif ch == '"':
                in_s = False
            continue
        if ch == '"':
            in_s = True
        elif ch == "{":
            depth += 1
        elif ch == "}":
            depth -= 1
            if depth == 0:
                return texto[i:j + 1]
    return texto[i:]


def valida(etiqueta: str) -> bool:
    if not isinstance(etiqueta, str):
        return False
    palabras = [p for p in re.split(r"\s+", etiqueta.strip()) if p]
    return 3 <= len(palabras) <= 6


def procesar_carpeta(client, carpeta: Path, uso):
    archivos = [f for f in sorted(carpeta.glob("*.json")) if not f.name.startswith("_")]
    pendientes = []
    for f in archivos:
        d = json.loads(f.read_text(encoding="utf-8"))
        if valida(d.get("etiqueta_arbol", "")):
            continue
        pendientes.append((f, d))
    print(f"\n== {carpeta}: {len(archivos)} nodos, {len(pendientes)} sin etiqueta")

    fallidas = []
    for i in range(0, len(pendientes), LOTE):
        lote = pendientes[i:i + LOTE]
        entrada = [{"id": d["node_id"], "titulo": d["titulo_concepto"],
                    "resumen": d["resumen_teorico"][:220]} for _, d in lote]
        for intento in range(3):
            try:
                r = client.messages.create(
                    model=MODEL, max_tokens=8000, system=SYSTEM,
                    messages=[{"role": "user", "content": json.dumps(entrada, ensure_ascii=False)}])
                uso["in"] += r.usage.input_tokens
                uso["out"] += r.usage.output_tokens
                texto = next((b.text for b in r.content if getattr(b, "type", "") == "text"), "")
                mapa = json.loads(extraer_json(texto))
                break
            except Exception as e:
                print(f"  [reintento {intento+1}] {e}")
                time.sleep(5 * (intento + 1))
        else:
            fallidas.extend(d["node_id"] for _, d in lote)
            continue
        ok = 0
        for f, d in lote:
            et = mapa.get(d["node_id"])
            if valida(et):
                d["etiqueta_arbol"] = et.strip()
                f.write_text(json.dumps(d, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
                ok += 1
            else:
                fallidas.append(d["node_id"])
        print(f"  lote {i // LOTE + 1}: {ok}/{len(lote)} etiquetadas")
    if fallidas:
        print(f"  PENDIENTES tras la corrida (reintenta el script): {len(fallidas)}")
    return len(pendientes) - len(fallidas)


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(2)
    import anthropic
    client = anthropic.Anthropic()
    uso = {"in": 0, "out": 0}
    total = 0
    for arg in sys.argv[1:]:
        total += procesar_carpeta(client, Path(arg), uso)
    costo = uso["in"] / 1e6 * PRICE_IN + uso["out"] / 1e6 * PRICE_OUT
    print(f"\nEtiquetadas: {total} | Tokens: {uso['in']} in / {uso['out']} out | Costo: ${costo:.4f}")


if __name__ == "__main__":
    main()
