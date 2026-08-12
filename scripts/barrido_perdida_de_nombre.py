#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""barrido_perdida_de_nombre.py . busca A donde muere el nombre por el que se busca.

SOLO LECTURA. No adjudica: LISTA.

LA CLASE. Hay veredictos A donde lo que se pierde no es un paso ni una linea, sino
LA PALABRA POR LA QUE EL LECTOR LLEGA: un apellido (Taguchi, Pareto, Ishikawa) o el
nombre propio de un instrumento (Poka-Yoke, DMAIC, Baldridge). El alias del grafo
cubre el ID, no cubre la BUSQUEDA del lector.

CRITERIO DEL BARRIDO, escrito antes de correrlo:
  se marca el par si un marcador de nombre propio aparece en el ID o el TITULO del
  nodo que MUERE y NO aparece en ningun sitio del texto del que SOBREVIVE (id,
  titulo, pasos, entregable).

La lista de marcadores es curada y esta escrita abajo: es una lista de apellidos y
de instrumentos con nombre propio, no una heuristica de mayusculas, porque los
titulos del catalogo capitalizan casi todo.
"""
import json, io, sys, re, unicodedata, argparse

ap = argparse.ArgumentParser()
ap.add_argument("--listar", action="store_true")
a = ap.parse_args()
sys.stdout.reconfigure(encoding="utf-8")


def sinac(s):
    return "".join(c for c in unicodedata.normalize("NFD", s or "")
                   if unicodedata.category(c) != "Mn").lower()


MARCADORES = [
    # apellidos
    "taguchi", "pareto", "ishikawa", "shewhart", "deming", "juran", "crosby", "kano",
    "heinrich", "reason", "dekker", "amalberti", "maslow", "porter", "kotler", "moore",
    "christensen", "ansoff", "drucker", "herzberg", "mcgregor", "rackham", "cialdini",
    "kahneman", "osterwalder", "blank", "ries", "coleman", "siebert", "gerber",
    # instrumentos con nombre propio
    "poka", "yoke", "kaizen", "kanban", "muda", "gemba", "hoshin", "andon", "jidoka",
    "baldridge", "baldrige", "efqm", "iso", "dmaic", "dmadv", "six sigma", "sigma",
    "swiss cheese", "queso suizo", "tripod", "heart", "hazop", "fmea", "amef",
    "qfd", "spc", "copq", "smed", "5s", "takt", "scrum", "pdca", "shingo",
]


def hay(m, z):
    """Coincidencia por PALABRA COMPLETA. Sin esto, 'ries' casa dentro de 'riesgo'
    y 'iso' dentro de 'decision': el primer barrido dio ese falso positivo."""
    return re.search(r"(?<![a-z0-9])" + re.escape(m) + r"(?![a-z0-9])", z) is not None


def marcadores_en(txt):
    z = sinac(txt)
    return sorted({m for m in MARCADORES if hay(m, z)})


G = json.load(io.open("dataset/metadata/master_graph.json", encoding="utf-8"))["nodos"]
V = [json.loads(l) for l in io.open("docs/INTRA_DOMINIO_VEREDICTOS.jsonl", encoding="utf-8") if l.strip()]

SURV = [r"[Ss]obrevive\s+`?([a-z0-9_]+)", r"[Ss]uperviviente[^a-z0-9_]{0,12}`?([a-z0-9_]+)",
        r"[Gg]ana\s+`?([a-z0-9_]+)"]


def surviviente(r):
    for pat in SURV:
        m = re.search(pat, r["razon"])
        if m and m.group(1) in (r["nodo_a"], r["nodo_b"]):
            return m.group(1)
    return None


def texto(k):
    n = G.get(k) or {}
    return " ".join([k, n.get("titulo_concepto") or "", n.get("entregable_esperado") or ""] +
                    (n.get("pasos_accionables") or []))


A = [r for r in V if r["clase"] == "A"]
condir = [r for r in A if surviviente(r)]
hallados = []
for r in condir:
    surv = surviviente(r)
    muere = r["nodo_a"] if r["nodo_b"] == surv else r["nodo_b"]
    nm = G.get(muere) or {}
    # marcadores en el ID o el TITULO del que muere
    ms = marcadores_en(muere + " " + (nm.get("titulo_concepto") or ""))
    if not ms:
        continue
    tv = sinac(texto(surv))
    perdidos = [m for m in ms if not hay(m, tv)]
    if perdidos:
        hallados.append((r["puesto_intra"], r["dominio"], muere, surv, perdidos))

print("A del archivo: %d | A que eligen direccion: %d" % (len(A), len(condir)))
print("A con PERDIDA DE NOMBRE (marcador en el que muere, ausente en el que sobrevive): %d"
      % len(hallados))
print()
if hallados:
    print("| puesto | dominio | muere | sobrevive | el nombre que se pierde |")
    print("|---:|---|---|---|---|")
    for p, d, m, s, per in sorted(hallados):
        print("| **%d** | `%s` | `%s` | `%s` | **%s** |" % (p, d, m, s, ", ".join(per)))
