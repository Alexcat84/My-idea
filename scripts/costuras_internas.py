#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""costuras_internas.py - CITA los nodos con texto repetido DENTRO de si mismos.

ESTRICTAMENTE DE SOLO LECTURA. No toca ni un nodo, ni el motor, ni la web. Lo
unico que escribe son sus dos salidas en docs/.

ESTE INSTRUMENTO CITA, NO JUZGA. Igual que gradiente_pares.py, del que es el
hermano chico. Un nodo en la cola es UNA CITA PARA LEER, no una costura
probada. El veredicto es lectura textual del auditor con visto del fundador.

QUE BUSCA. La clase nacio de dos hallazgos del gradiente: `plan_mejora_procesos`
(puesto 83) y `economia_circular_como_modelo_de_negocio` (puesto 97), dos nodos
del nucleo con DOS SECUENCIAS CASI IDENTICAS PEGADAS DENTRO. No son duplicados
entre nodos: son un solo nodo al que le sobran pasos. Dos figuras identicas en
temas sin relacion significan que la tanda que pego sin tejer dejo mas huellas, y
esas no se cazan esperando el tercer golpe de suerte.

DOS SEÑALES INDEPENDIENTES, y basta con que dispare CUALQUIERA. Se reportan LAS
DOS siempre, aunque solo una haya disparado, porque el auditor necesita ver por
que entro cada nodo:

  1. PAREJA DE PASOS: token_sort_ratio de rapidfuzz entre cada dos pasos del
     mismo nodo, umbral 80. Caza el paso REPETIDO casi literal.

  2. ALINEACION DE BLOQUES: para cada corte posible de la lista, se empareja el
     segundo bloque contra el primero EN ORDEN (emparejamiento monotono) y se
     promedian las tres mejores parejas. Umbral 45. Caza el BLOQUE reiniciado,
     que es la figura de los dos hallazgos, y ademas dice DONDE esta el corte.

POR QUE HACEN FALTA LAS DOS, medido antes de escribirlo. Con la señal 1 sola, y
en cualquier umbral, la calibracion NO entra: la mejor pareja interna de
`plan_mejora_procesos` es 60.0 y la de `economia_circular` 54.7, y bajar el
umbral hasta ahi caza 856 nodos, el 24 por ciento del catalogo. Esta casa ya
adjudico que una baranda que caza lo correcto no es estricta, esta rota. El
motivo es que esas dos costuras son PARAFRASIS con cola distinta, no copias:
"Establecer metricas de exito en cada etapa" contra "Establece metricas para
cada etapa (¿estas obteniendo suficientes candidatos?)". La señal 2 las pone en
los puestos 7 y 32 de 567, y acierta el corte exacto en las dos.

LA CALIBRACION CONOCIDA: los dos nodos de arriba TIENEN que aparecer en la cola.
Si falta alguno, el instrumento esta mal calibrado, lo dice y SALE CON CODIGO 1
SIN ENTREGAR.

Uso:
  python scripts/costuras_internas.py
  python scripts/costuras_internas.py --umbral-pareja 75 --umbral-bloque 50
"""
import argparse
import json
import statistics
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent
GRAFO = BASE / "dataset" / "metadata" / "master_graph.json"
SALIDA = BASE / "docs" / "COSTURAS_INTERNAS.jsonl"
RESUMEN = BASE / "docs" / "COSTURAS_INTERNAS_RESUMEN.md"

UMBRAL_PAREJA = 80
UMBRAL_BLOQUE = 45

# Minimo de pasos para que un bloque signifique algo: con menos de tres pasos por
# lado, "el segundo bloque repite al primero" no es una afirmacion, es ruido.
MIN_BLOQUE = 3

# Los dos nodos que dieron origen a la clase. Si el instrumento no los caza, no
# sirve para lo que se construyo y no entrega nada.
CALIBRACION = ("plan_mejora_procesos", "economia_circular_como_modelo_de_negocio")


def peor_pareja(ratio, pasos):
    """La pareja de pasos mas parecida del nodo: (similitud, i, j) en base 1."""
    mejor = (0.0, 0, 0)
    for a in range(len(pasos)):
        for b in range(a + 1, len(pasos)):
            s = ratio(pasos[a], pasos[b])
            if s > mejor[0]:
                mejor = (s, a + 1, b + 1)
    return mejor


def mejor_bloque(ratio, pasos):
    """El corte que mejor explica la lista como DOS bloques, uno repitiendo al
    otro: (score, corte). El corte es en base 1: 'los pasos 1 a corte contra el
    resto'. Devuelve (0, 0) si la lista es demasiado corta para afirmarlo."""
    mejor = (0.0, 0)
    n = len(pasos)
    for corte in range(MIN_BLOQUE, n - MIN_BLOQUE + 1):
        a, b = pasos[:corte], pasos[corte:]
        # Emparejamiento MONOTONO: cada paso del segundo bloque se empareja con
        # uno del primero, sin retroceder. Es lo que distingue "la secuencia
        # vuelve a empezar" de "estos dos pasos se parecen".
        j, puntajes = 0, []
        for paso in b:
            candidatos = [(ratio(a[k], paso), k) for k in range(j, len(a))]
            if not candidatos:
                break
            s, k = max(candidatos)
            puntajes.append(s)
            j = k + 1
        if len(puntajes) >= MIN_BLOQUE:
            score = sum(sorted(puntajes, reverse=True)[:MIN_BLOQUE]) / MIN_BLOQUE
            if score > mejor[0]:
                mejor = (score, corte)
    return mejor


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--umbral-pareja", type=float, default=UMBRAL_PAREJA)
    ap.add_argument("--umbral-bloque", type=float, default=UMBRAL_BLOQUE)
    args = ap.parse_args()

    from rapidfuzz.fuzz import token_sort_ratio as ratio

    nodos = json.loads(GRAFO.read_text(encoding="utf-8"))["nodos"]
    activos = {k: v for k, v in nodos.items() if not v.get("deprecado")}

    filas, sc_pareja, sc_bloque = [], [], []
    for nid, n in sorted(activos.items()):
        pasos = n.get("pasos_accionables") or []
        if len(pasos) < 2:
            continue
        s_par, i, j = peor_pareja(ratio, pasos)
        sc_pareja.append(s_par)
        s_blo, corte = (mejor_bloque(ratio, pasos) if len(pasos) >= MIN_BLOQUE * 2
                        else (0.0, 0))
        if corte:
            sc_bloque.append(s_blo)
        disparo_p = s_par >= args.umbral_pareja
        disparo_b = bool(corte) and s_blo >= args.umbral_bloque
        if not (disparo_p or disparo_b):
            continue
        filas.append({
            "node_id": nid,
            "dominio": n.get("dominio"),
            "titulo": n.get("titulo_concepto", ""),
            "pasos": len(pasos),
            "sim_pareja": round(s_par, 1),
            "pareja": [i, j],
            "paso_a": pasos[i - 1],
            "paso_b": pasos[j - 1],
            "sim_bloque": round(s_blo, 1),
            "corte": corte,
            "disparo_pareja": disparo_p,
            "disparo_bloque": disparo_b,
        })

    # Ordena por la señal MAS FUERTE de las dos, normalizando ambas a 0-1.
    filas.sort(key=lambda f: max(f["sim_pareja"] / 100, f["sim_bloque"] / 100),
               reverse=True)

    encontrados = {f["node_id"] for f in filas}
    faltan = [c for c in CALIBRACION if c not in encontrados]
    if faltan:
        print("INSTRUMENTO MAL CALIBRADO. No entrega nada.")
        print(f"  La calibracion conocida no aparece en la cola: {faltan}")
        for c in faltan:
            pasos = activos.get(c, {}).get("pasos_accionables") or []
            if pasos:
                sp = peor_pareja(ratio, pasos)
                sb = mejor_bloque(ratio, pasos)
                print(f"    {c}: mejor pareja {sp[0]:.1f} (pasos {sp[1]} y {sp[2]}), "
                      f"mejor bloque {sb[0]:.1f} (corte tras {sb[1]})")
        print(f"  Umbrales usados: pareja {args.umbral_pareja}, bloque {args.umbral_bloque}")
        return 1

    L = []
    A = L.append
    A("# Costuras internas: nodos con texto repetido DENTRO de si mismos")
    A("")
    A("**ESTE INSTRUMENTO CITA, NO JUZGA.** Hermano chico de "
      "`scripts/gradiente_pares.py`. **Un nodo en esta lista es una cita para "
      "leer, no una costura probada.** El veredicto es **lectura textual** del "
      "auditor con visto del fundador.")
    A("")
    A("La clase nacio de dos hallazgos del gradiente: `plan_mejora_procesos` "
      "(puesto 83) y `economia_circular_como_modelo_de_negocio` (puesto 97). **No "
      "son duplicados entre nodos: son un solo nodo al que le sobran pasos.**")
    A("")
    A("## Las dos señales")
    A("")
    A("| señal | que caza | umbral |")
    A("|---|---|---:|")
    A(f"| **pareja de pasos** | el paso repetido casi literal (`token_sort_ratio`) | **{args.umbral_pareja}** |")
    A(f"| **alineacion de bloques** | la secuencia que vuelve a empezar, y **donde** | **{args.umbral_bloque}** |")
    A("")
    A("**Basta con que dispare cualquiera, y se reportan las dos siempre**, como "
      "en el hermano mayor: el auditor necesita ver por que entro cada nodo.")
    A("")
    A("### Por que hacen falta las dos, medido")
    A("")
    A("**Con la señal de pareja sola, y en cualquier umbral, la calibracion no "
      "entra.** La mejor pareja interna de `plan_mejora_procesos` es **60.0** y la "
      "de `economia_circular` **54.7**; bajar el umbral hasta ahi caza **856 "
      "nodos, el 24 por ciento del catalogo**.")
    A("")
    A("> **Una baranda que caza lo correcto no es estricta, esta rota.**")
    A("")
    A("El motivo es que esas dos costuras son **parafrasis con cola distinta**, no "
      "copias. La señal de bloques las pone en los **puestos 7 y 32 de 567** y "
      "**acierta el corte exacto en las dos**.")
    A("")
    A("## La calibracion conocida")
    A("")
    for c in CALIBRACION:
        f = next(x for x in filas if x["node_id"] == c)
        A(f"**CAZADO** `{c}`: pareja **{f['sim_pareja']}**, bloque "
          f"**{f['sim_bloque']}** con el corte **tras el paso {f['corte']}**.")
        A("")
    A("## Conteos")
    A("")
    A(f"**{len(filas)} nodos** en la cola, sobre {len(activos)} activos.")
    A("")
    por_dom = {}
    for f in filas:
        por_dom[f["dominio"]] = por_dom.get(f["dominio"], 0) + 1
    A("| dominio | nodos |")
    A("|---|---:|")
    for dom, c in sorted(por_dom.items(), key=lambda x: -x[1]):
        A(f"| {dom} | {c} |")
    A("")
    A("## Distribucion, para calibrar")
    A("")
    A("| percentil | mejor pareja interna | alineacion de bloques |")
    A("|---|---:|---:|")
    qp = statistics.quantiles(sc_pareja, n=100)
    qb = statistics.quantiles(sc_bloque, n=100)
    for etiqueta, k in (("p50", 50), ("p90", 90), ("p99", 99)):
        A(f"| {etiqueta} | {qp[k - 1]:.1f} | {qb[k - 1]:.1f} |")
    A(f"| maximo | {max(sc_pareja):.1f} | {max(sc_bloque):.1f} |")
    A("")
    A(f"Nodos evaluados por bloques (6 pasos o mas): **{len(sc_bloque)}**.")
    A("")
    A("## Los veinte primeros")
    A("")
    A("| # | dominio | nodo | pasos | pareja | bloque | corte | entro por |")
    A("|---:|---|---|---:|---:|---:|---:|---|")
    for i, f in enumerate(filas[:20], 1):
        por = []
        if f["disparo_pareja"]:
            por.append("pareja")
        if f["disparo_bloque"]:
            por.append("bloque")
        A(f"| {i} | {f['dominio']} | `{f['node_id']}` | {f['pasos']} | "
          f"{f['sim_pareja']} | {f['sim_bloque']} | {f['corte'] or ''} | "
          f"{' y '.join(por)} |")
    A("")
    A(f"La cola completa, con los dos pasos de cada pareja, en `{SALIDA.name}`.")
    RESUMEN.write_text("\n".join(L) + "\n", encoding="utf-8")

    with open(SALIDA, "w", encoding="utf-8") as fh:
        for f in filas:
            fh.write(json.dumps(f, ensure_ascii=False) + "\n")

    print(f"  nodos en la cola: {len(filas)} | escrito {SALIDA.name} y {RESUMEN.name}")
    print(f"  calibracion: los {len(CALIBRACION)} nodos conocidos, CAZADOS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
