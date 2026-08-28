# -*- coding: utf-8 -*-
"""Auditor v110: recuento propio del lote preposicional y de los veredictos
registrados, SIN leer la clasificacion del ejecutor."""
import io, os, re, sys, json
RAIZ = os.getcwd()
sys.path.insert(0, os.path.join(RAIZ, "scripts", "loop"))
from verificar_cobertura_bolsa_tres_vias import FICHEROS_VEREDICTO
import contar_cierre_efectivo as cce

LOOP = os.path.join(RAIZ, "docs", "loop")
RE_B = re.compile(r"^--- PUESTO (\d+) ---")
RE_BV = re.compile(r"VEREDICTO:\s*(OBJETO|SATELITE|NO_OBJETO)\b")
RE_T = re.compile(r"^(\d+)\s*\|.*\|\s*(OBJETO|SATELITE|NO_OBJETO)\b")

def bloque(t):
    out={}; p=None
    for l in t.splitlines():
        m=RE_B.match(l)
        if m: p=int(m.group(1)); continue
        if l.strip()=="": p=None; continue
        if p is not None:
            mv=RE_BV.search(l)
            if mv: out[p]=mv.group(1); p=None
    return out
def tabla(t):
    out={}
    for l in t.splitlines():
        m=RE_T.match(l)
        if m: out[int(m.group(1))]=m.group(2)
    return out

ver={}
for nombre,fmt in FICHEROS_VEREDICTO:
    t=io.open(os.path.join(LOOP,nombre),encoding="utf-8").read()
    d = bloque(t) if fmt=="bloque" else tabla(t)
    for k,v in d.items(): ver[k]=v   # el ultimo fichero manda (orden cronologico)
print("puestos con veredicto en los seis ficheros:", len(ver))
c=cce.cifras() if hasattr(cce,"cifras") else None
print("cifras() disponible:", c is not None)
