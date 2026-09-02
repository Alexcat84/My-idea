# -*- coding: utf-8 -*-
"""Auditor v142, CIEGA: direcciones distintas por operacion, con parser y
resolutor PROPIOS. Se corre ANTES de abrir la CORRECCION 15 del ejecutor.
Cada fila de `aristas_nuevas` es prosa: puede llevar UNA direccion o DOS
unidas por ' Y '. Se corta en el primer parentesis o coma y se parte por '->'."""
import json, io, os, glob, re

alias, vivos, todos = {}, set(), set()
for p in glob.glob("dataset/nodos/*.json"):
    d = json.load(io.open(p, encoding="utf-8"))
    nid = d.get("node_id") or os.path.splitext(os.path.basename(p))[0]
    todos.add(nid)
    if not d.get("deprecado"):
        vivos.add(nid)
    for a in (d.get("ids_alias") or []):
        alias[a] = nid

def resolver(x):
    visto = set()
    while x in alias and x not in visto:
        visto.add(x); x = alias[x]
    return x

TOK = re.compile(r"^[a-z0-9_]+$")

def direcciones_de_fila(txt):
    fuera = []
    for trozo in re.split(r"\s+Y\s+", txt):
        cab = re.split(r"[(,:;]", trozo)[0].strip()
        if "->" not in cab:
            continue
        partes = [t.strip() for t in cab.split("->")]
        for a, b in zip(partes, partes[1:]):
            a = a.split()[-1] if a.split() else a
            b = b.split()[0] if b.split() else b
            if TOK.match(a) and TOK.match(b):
                fuera.append((resolver(a), resolver(b)))
    return fuera

ops = [json.loads(l) for l in io.open("docs/plan/OPERACIONES.jsonl", encoding="utf-8") if l.strip()]
porid = {o["id_op"]: o for o in ops}
CINCO = ["OP-M-03-ENLACES", "OP-E-04", "OP-E-05", "OP-M-01-ESLABONES", "OP-M-01-SEXTO"]
SEXTA = "OP-M-05-APERTURA"

def medir(nomina, rotulo):
    tf = td = 0
    print("--- %s ---" % rotulo)
    for i in nomina:
        o = porid[i]
        an = o.get("aristas_nuevas") or []
        dirs = []
        for fila in an:
            for d in direcciones_de_fila(fila):
                if d not in dirs:
                    dirs.append(d)
        print("  %-20s %2d filas -> %2d direcciones" % (i, len(an), len(dirs)))
        tf += len(an); td += len(dirs)
    print("  TOTAL %s: %d filas, %d DIRECCIONES\n" % (rotulo, tf, td))
    return tf, td

medir(CINCO, "LAS CINCO REMITIDAS DEL ACTA 140")
medir(CINCO + [SEXTA], "LAS SEIS DEL TRAMO (con OP-M-05-APERTURA)")
