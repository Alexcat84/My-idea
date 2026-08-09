#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""gradiente_pares.py - EMPAREJA nodos de mundo con su nodo base del nucleo.

ESTRICTAMENTE DE SOLO LECTURA. No toca ni un nodo, no toca el motor, no toca la
web. Lo unico que escribe son sus dos salidas en docs/.

ESTE INSTRUMENTO EMPAREJA, NO JUZGA. El veredicto de cada par es lectura textual
del auditor con visto del fundador. Un par en la cola es UNA CITA PARA LEER, no
una violacion. La vara esta en docs/GRADIENTE_NUCLEO_MUNDO.md.

DOS SENALES INDEPENDIENTES, y basta con que dispare CUALQUIERA:

  1. TITULO: token_sort_ratio de rapidfuzz, umbral 80. Caza los pares que se
     llaman casi igual aunque el texto haya divergido.
  2. SEMANTICA: coseno entre los vectores de web/lib/assets/semantic_index.json,
     umbral inicial 0.75. Caza los pares que hablan de lo mismo con otras
     palabras, que es donde el titulo no llega.

Se reportan LAS DOS por par, siempre, aunque solo una haya disparado: el auditor
necesita ver por que entro cada uno.

POR QUE LOS CONTEOS DE PASOS ESTAN EN LA SALIDA Y NO EN EL CRITERIO: la doctrina
lo dice y aqui se respeta. La profundidad se adjudica leyendo, jamas contando.
Los conteos SOLO ordenan la cola de lectura.

Uso:
  python scripts/gradiente_pares.py
  python scripts/gradiente_pares.py --umbral-semantico 0.70
"""
import argparse
import collections
import json
import statistics
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent
GRAFO = BASE / "dataset" / "metadata" / "master_graph.json"
INDICE = BASE / "web" / "lib" / "assets" / "semantic_index.json"
SALIDA = BASE / "docs" / "GRADIENTE_PARES.jsonl"
RESUMEN = BASE / "docs" / "GRADIENTE_PARES_RESUMEN.md"

UMBRAL_TITULO = 80
UMBRAL_SEMANTICO = 0.75

# La calibracion conocida: este par TIENE que aparecer en la cola. Si el
# instrumento no lo caza, esta mal calibrado y hay que decirlo antes de entregar.
PAR_DE_CALIBRACION = ("plan_gestion_calidad", "sistema_gestion_calidad")


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--umbral-titulo", type=int, default=UMBRAL_TITULO)
    ap.add_argument("--umbral-semantico", type=float, default=UMBRAL_SEMANTICO)
    args = ap.parse_args()

    import numpy as np
    from rapidfuzz.fuzz import token_sort_ratio

    grafo = json.loads(GRAFO.read_text(encoding="utf-8"))["nodos"]
    idx = json.loads(INDICE.read_text(encoding="utf-8"))
    pos = {n: i for i, n in enumerate(idx["ids"])}
    E = np.array(idx["embeddings"], dtype=np.float32)
    E /= np.linalg.norm(E, axis=1, keepdims=True)

    activos = {k: v for k, v in grafo.items() if not v.get("deprecado")}
    nucleo = [k for k, v in activos.items() if (v.get("dominio") or "core") == "core"]
    mundos = collections.defaultdict(list)
    for k, v in activos.items():
        d = v.get("dominio") or "core"
        if d != "core":
            mundos[d].append(k)

    # Solo los que tienen vector: el Gate ya garantiza que son todos los activos,
    # pero se comprueba en vez de suponerlo.
    nucleo = [k for k in nucleo if k in pos]
    N = E[[pos[k] for k in nucleo]]
    titulo = {k: (activos[k].get("titulo_concepto") or "") for k in activos}
    pasos = {k: len(activos[k].get("pasos_accionables") or []) for k in activos}

    pares, todas_sem = [], []
    for dom in sorted(mundos):
        ids_m = [k for k in mundos[dom] if k in pos]
        if not ids_m:
            continue
        S = E[[pos[k] for k in ids_m]] @ N.T
        for i, nm in enumerate(ids_m):
            fila = S[i]
            todas_sem.extend(float(x) for x in fila)
            # candidatos por semantica
            cand = {nucleo[j] for j in np.where(fila >= args.umbral_semantico)[0]}
            # candidatos por titulo, contra TODO el nucleo (barato con rapidfuzz)
            tm = titulo[nm]
            for j, nc in enumerate(nucleo):
                if token_sort_ratio(tm, titulo[nc]) >= args.umbral_titulo:
                    cand.add(nc)
            for nc in cand:
                j = nucleo.index(nc)
                pares.append({
                    "mundo": dom,
                    "nodo_mundo": nm, "titulo_mundo": tm,
                    "nodo_nucleo": nc, "titulo_nucleo": titulo[nc],
                    "sim_titulo": round(float(token_sort_ratio(tm, titulo[nc])), 1),
                    "sim_semantica": round(float(fila[j]), 4),
                    "disparo_titulo": bool(token_sort_ratio(tm, titulo[nc]) >= args.umbral_titulo),
                    "disparo_semantica": bool(fila[j] >= args.umbral_semantico),
                    "pasos_mundo": pasos[nm], "pasos_nucleo": pasos[nc],
                })

    pares.sort(key=lambda p: -max(p["sim_semantica"], p["sim_titulo"] / 100))
    with open(SALIDA, "w", encoding="utf-8") as fh:
        for p in pares:
            fh.write(json.dumps(p, ensure_ascii=False) + "\n")

    # LA CALIBRACION CONOCIDA
    a, b = PAR_DE_CALIBRACION
    calibra = [p for p in pares if p["nodo_nucleo"] == a and p["nodo_mundo"] == b]
    if not calibra:
        calibra = [p for p in pares if {p["nodo_nucleo"], p["nodo_mundo"]} == {a, b}]

    por_mundo = collections.Counter(p["mundo"] for p in pares)
    sem = sorted(todas_sem)

    L = []
    A = L.append
    A("# Cola de pares nucleo-mundo para leer")
    A("")
    A("**ESTE INSTRUMENTO EMPAREJA, NO JUZGA.** El veredicto de cada par es **lectura "
      "textual** del auditor con visto del fundador. **Un par en esta lista es una cita "
      "para leer, no una violacion.**")
    A("")
    A("La vara esta en `docs/GRADIENTE_NUCLEO_MUNDO.md`: el nucleo es suficiente, el mundo "
      "es exponencial respecto de esa base, y una violacion **jamas** se arregla "
      "empobreciendo el nucleo.")
    A("")
    A("Los conteos de pasos que aparecen en la salida **solo ordenan la cola**. La "
      "profundidad se adjudica leyendo `pasos_accionables` y `entregable_esperado`, jamas "
      "contando.")
    A("")
    A("## Como se emparejo")
    A("")
    A(f"Dos senales independientes, y basta con que dispare **cualquiera**:")
    A("")
    A(f"- **titulo**: `token_sort_ratio` de rapidfuzz, umbral **{args.umbral_titulo}**")
    A(f"- **semantica**: coseno sobre `semantic_index.json`, umbral **{args.umbral_semantico}**")
    A("")
    A("Cada par reporta **las dos**, aunque solo una haya disparado.")
    A("")
    A("## La calibracion conocida")
    A("")
    if calibra:
        c = calibra[0]
        A(f"**CAZADO.** El par `{a}` (nucleo) contra `{b}` (quality) esta en la cola: "
          f"similitud de titulo **{c['sim_titulo']}**, semantica **{c['sim_semantica']}** "
          f"(disparo por titulo: {c['disparo_titulo']}, por semantica: {c['disparo_semantica']}).")
    else:
        A(f"**NO CAZADO. EL INSTRUMENTO ESTA MAL CALIBRADO.** El par `{a}` contra `{b}` "
          f"deberia estar en la cola y no esta. No uses esta salida sin revisar los "
          f"umbrales.")
    A("")
    A("## Conteos")
    A("")
    A(f"**{len(pares)} pares** en la cola, sobre {len(nucleo)} nodos de nucleo y "
      f"{sum(len(v) for v in mundos.values())} de mundo.")
    A("")
    A("| mundo | pares |")
    A("|---|---:|")
    for dom, c in por_mundo.most_common():
        A(f"| {dom} | {c} |")
    A("")
    A("## Distribucion de la similitud semantica")
    A("")
    A(f"Sobre **{len(sem)}** comparaciones mundo-contra-nucleo:")
    A("")
    A("| percentil | coseno |")
    A("|---|---:|")
    for pc in (50, 75, 90, 95, 99, 99.9):
        A(f"| p{pc} | {sem[min(len(sem) - 1, int(len(sem) * pc / 100))]:.4f} |")
    A(f"| maximo | {sem[-1]:.4f} |")
    A("")
    A(f"Media {statistics.mean(sem):.4f}. **Por encima del umbral "
      f"{args.umbral_semantico}: {sum(1 for x in sem if x >= args.umbral_semantico)} "
      f"comparaciones.**")
    A("")
    A(f"**Lectura de esta distribucion para calibrar**: el umbral {args.umbral_semantico} "
      f"esta muy por encima del p99.9 "
      f"({sem[min(len(sem) - 1, int(len(sem) * 0.999))]:.4f}), asi que la senal semantica "
      f"solo caza la cola extrema. Es deliberadamente selectiva: la cola es para LEER, y "
      f"una cola de miles de pares no se lee. Si el auditor quiere mas cobertura, bajar a "
      f"0.70 o 0.65 la ensancha; el instrumento acepta `--umbral-semantico`.")
    A("")
    A("## Los veinte pares de similitud mas alta del catalogo entero")
    A("")
    A("Ordenados por la senal MAS FUERTE de las dos, normalizando el titulo a 0-1. Por eso "
      "hay filas con semantica baja y titulo alto: entraron por el titulo, y se ven las dos "
      "columnas para que quede claro por cual.")
    A("")
    A("| # | mundo | nodo del mundo | nodo del nucleo | titulo | semantica | pasos M/N |")
    A("|---:|---|---|---|---|---:|---:|")
    for i, p in enumerate(pares[:20], 1):
        A(f"| {i} | {p['mundo']} | `{p['nodo_mundo']}` | `{p['nodo_nucleo']}` | "
          f"{p['sim_titulo']} | {p['sim_semantica']} | {p['pasos_mundo']}/{p['pasos_nucleo']} |")
    A("")
    A(f"La cola completa, con los titulos de los dos lados, en `{SALIDA.name}`.")
    RESUMEN.write_text("\n".join(L) + "\n", encoding="utf-8")

    print(f"  pares: {len(pares)} | escrito {SALIDA.name} y {RESUMEN.name}")
    print(f"  calibracion {a} vs {b}: {'CAZADO' if calibra else 'NO CAZADO (mal calibrado)'}")
    return 0 if calibra else 1


if __name__ == "__main__":
    raise SystemExit(main())
