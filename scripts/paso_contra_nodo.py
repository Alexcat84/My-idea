#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""paso_contra_nodo.py - mide cada PASO de un nodo contra los NODOS de su dominio.

ESTRICTAMENTE DE SOLO LECTURA. No toca ni un nodo, no toca el motor, no toca la
web. Lo unico que escribe es su salida en docs/.

EL EJE QUE NADIE HABIA MIRADO. Los dos instrumentos existentes miden NODO contra
NODO: `intra_dominio.py` empareja nodos del mismo dominio, y
`costuras_internas.py` mide los pasos de un nodo contra los pasos de ESE MISMO
nodo. Ninguno mira el eje cruzado: **un PASO de la madre contra un NODO ENTERO
que lo desarrolla**.

POR QUE ESE EJE IMPORTA. El cribado intra encontro esa figura una y otra vez, y
siempre a mano: una madre enumera un paso en UNA LINEA y otro nodo trae el
procedimiento entero de esa linea. En el tramo 901 a 928 fueron SIETE de
veintiocho pares. La figura tiene dos destinos posibles y los dos estan en el
plan:

  - **ARISTA QUE FALTA** (banco 9.6) cuando la jerarquia es sana: la madre nombra,
    el hijo desarrolla, y solo falta el enlace.
  - **PODA** cuando la madre re-desarrolla lo que el hijo ya cuenta.

ESTE INSTRUMENTO NO ADJUDICA CUAL DE LOS DOS. Empareja. La lista es una cita para
leer, igual que la del intra.

LAS DOS SENALES, y tienen que disparar LAS DOS (Y logico, no O):

  1. TITULO: `token_set_ratio` del paso contra el TITULO del hijo candidato.
     Se usa `token_set_ratio` y no `token_sort_ratio` porque los largos son muy
     distintos: un titulo de cinco palabras dentro de un paso de veinte. El
     `set` ignora esa asimetria; el `sort` la castiga.
  2. CONTENCION: que proporcion de las palabras de contenido del paso aparece en
     la IDENTIDAD del hijo (titulo mas resumen mas entregable).

POR QUE LAS DOS Y NO CUALQUIERA. Es la leccion del umbral 0,80 del intra: dentro
de un dominio la vecindad tematica es la norma. Cualquiera de las dos senales
sola llena la lista de vecinos legitimos. La conjuncion pide que el paso NOMBRE
al hijo (senal 1) y ademas que su vocabulario VIVA dentro del hijo (senal 2).

UMBRALES DECLARADOS, y el motivo de cada uno:
  --umbral-titulo 72   el titulo del hijo reconocible dentro del paso
  --umbral-contencion 0.45   casi la mitad del vocabulario del paso, dentro del hijo
  --min-tokens 4   pasos de menos de cuatro palabras de contenido no se miden:
                   "iterar rapido" se parece a demasiadas cosas

EXCLUSIONES: nodos deprecados de los dos lados, el propio nodo, y los pares de
distinto dominio (el nucleo cuenta como dominio).

Uso:
  python scripts/paso_contra_nodo.py
  python scripts/paso_contra_nodo.py --dominio core --umbral-titulo 78
"""
import argparse
import collections
import json
import re
import unicodedata
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
GRAFO = RAIZ / "dataset" / "metadata" / "master_graph.json"
SALIDA = RAIZ / "docs" / "PASO_NODO_CANDIDATOS.jsonl"

# Palabras que en este catalogo no distinguen nada: aparecen en casi todo paso.
VACIAS = {
    "a", "al", "ante", "con", "contra", "de", "del", "desde", "en", "entre",
    "hacia", "hasta", "la", "las", "lo", "los", "para", "por", "segun", "sin",
    "sobre", "tras", "un", "una", "unos", "unas", "el", "y", "o", "u", "e",
    "que", "se", "su", "sus", "tu", "tus", "te", "le", "les", "es", "son",
    "si", "no", "mas", "menos", "ya", "cada", "todo", "toda", "todos", "todas",
    "este", "esta", "estos", "estas", "ese", "esa", "esos", "esas", "cual",
    "cuales", "como", "cuando", "donde", "porque", "pero", "aunque", "ni",
    "definir", "define", "hacer", "haz", "usar", "usa", "crear", "crea",
    "identificar", "identifica", "establecer", "establece", "evaluar", "evalua",
    "revisar", "revisa", "determinar", "determina", "realizar", "realiza",
    "tener", "ten", "ser", "estar", "poder", "puede", "debe", "deben",
    "tuyo", "tuya", "propio", "propia", "mismo", "misma", "otro", "otra",
}


def norm(s):
    """Minusculas, sin acentos, sin puntuacion."""
    s = unicodedata.normalize("NFD", (s or "").lower())
    s = "".join(c for c in s if unicodedata.category(c) != "Mn")
    return re.sub(r"[^a-z0-9ñ]+", " ", s).strip()


def contenido(s):
    """Palabras de contenido: normalizadas, sin vacias, de tres letras o mas."""
    return {w for w in norm(s).split() if len(w) >= 3 and w not in VACIAS}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--umbral-titulo", type=float, default=72.0)
    ap.add_argument("--umbral-contencion", type=float, default=0.45)
    ap.add_argument("--min-tokens", type=int, default=4)
    ap.add_argument("--dominio", default=None)
    ap.add_argument("--top", type=int, default=10)
    args = ap.parse_args()

    from rapidfuzz.fuzz import token_set_ratio

    G = json.load(open(GRAFO, encoding="utf-8"))["nodos"]
    DEP = {k for k, v in G.items() if v.get("deprecado")}
    ALIAS = {a: k for k, v in G.items() for a in (v.get("ids_alias") or [])}

    def vivo(x):
        if x in G and x not in DEP:
            return x
        y = ALIAS.get(x)
        return y if y in G and y not in DEP else None

    def vecinos(n):
        out = set()
        for campo in ("nodos_siguientes", "nodos_previos"):
            for y in (G[n].get(campo) or []):
                r = vivo(y)
                if r and r != n:
                    out.add(r)
        return out

    vivos = [k for k in G if k not in DEP]
    if args.dominio:
        vivos = [k for k in vivos if G[k].get("dominio") == args.dominio]

    por_dominio = collections.defaultdict(list)
    for k in vivos:
        por_dominio[G[k].get("dominio") or "?"].append(k)

    # Identidad de cada hijo candidato: titulo mas resumen mas entregable.
    ident = {}
    for k in vivos:
        g = G[k]
        ident[k] = contenido(" ".join([
            g.get("titulo_concepto") or "",
            g.get("resumen_teorico") or "",
            g.get("entregable_esperado") or "",
        ]))

    # Indice invertido token -> hijos cuya identidad lo contiene. Sin el, el
    # barrido es cuadratico sobre 1.500 nodos por cinco pasos y no termina.
    indice = collections.defaultdict(set)
    for k in vivos:
        for w in ident[k]:
            indice[w].add(k)
    titulo_norm = {k: norm(G[k].get("titulo_concepto") or "") for k in vivos}

    filas = []
    for dom, nodos in por_dominio.items():
        set_dom = set(nodos)
        for madre in nodos:
            pasos = G[madre].get("pasos_accionables") or []
            vec_m = vecinos(madre)
            for i, paso in enumerate(pasos, 1):
                toks = contenido(paso)
                if len(toks) < args.min_tokens:
                    continue
                paso_norm = norm(paso)
                # LA CONTENCION PRIMERO, porque es de conjuntos y es barata; el
                # ratio de titulo solo se calcula sobre lo que ya paso el filtro.
                golpes = collections.Counter()
                for w in toks:
                    for k in indice.get(w, ()):
                        golpes[k] += 1
                minimo = args.umbral_contencion * len(toks)
                for hijo, n_comunes in golpes.items():
                    if hijo == madre or hijo not in set_dom or n_comunes < minimo:
                        continue
                    c = n_comunes / len(toks)
                    t = token_set_ratio(paso_norm, titulo_norm[hijo])
                    if t < args.umbral_titulo:
                        continue
                    filas.append({
                        "dominio": dom,
                        "madre": madre,
                        "paso": i,
                        "pasos_madre": len(pasos),
                        "texto_paso": paso,
                        "hijo": hijo,
                        "pasos_hijo": len(G[hijo].get("pasos_accionables") or []),
                        "titulo_ratio": round(t, 1),
                        "contencion": round(c, 3),
                        "puntaje": round(t / 100 * c, 4),
                        "arista": hijo in vec_m or madre in vecinos(hijo),
                    })

    filas.sort(key=lambda f: -f["puntaje"])
    with open(SALIDA, "w", encoding="utf-8", newline="\n") as f:
        for fila in filas:
            f.write(json.dumps(fila, ensure_ascii=False) + "\n")

    print("UMBRALES: titulo %.0f | contencion %.2f | min tokens %d"
          % (args.umbral_titulo, args.umbral_contencion, args.min_tokens))
    print("nodos vivos mirados: %d | candidatos: %d" % (len(vivos), len(filas)))
    print()
    print("VOLUMEN POR DOMINIO")
    cnt = collections.Counter(f["dominio"] for f in filas)
    tot = collections.Counter(G[k].get("dominio") or "?" for k in vivos)
    con_ar = collections.Counter(f["dominio"] for f in filas if f["arista"])
    print("  %-16s %8s %10s %10s %10s" % ("dominio", "nodos", "candidatos", "con arista", "sin arista"))
    for d in sorted(tot, key=lambda x: -cnt.get(x, 0)):
        print("  %-16s %8d %10d %10d %10d"
              % (d, tot[d], cnt.get(d, 0), con_ar.get(d, 0), cnt.get(d, 0) - con_ar.get(d, 0)))
    print()
    print("LOS %d CANDIDATOS MAS FUERTES" % args.top)
    for f in filas[:args.top]:
        print("  %.3f  t%.0f c%.2f  %s [paso %d de %d] -> %s (%d pasos) arista=%s"
              % (f["puntaje"], f["titulo_ratio"], f["contencion"], f["madre"],
                 f["paso"], f["pasos_madre"], f["hijo"], f["pasos_hijo"],
                 "SI" if f["arista"] else "NO"))
    print()
    print("ESTE INSTRUMENTO EMPAREJA, NO JUZGA. Cada fila es una cita para leer.")


if __name__ == "__main__":
    main()
