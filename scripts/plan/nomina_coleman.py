# -*- coding: utf-8 -*-
"""LA SERIE DE COLEMAN, con los DOS instrumentos del estandar (banco 9.20).
   CONTADOR: levanta por la FUENTE declarada. BARRIDO: levanta por el ARCHIVO.
   Reparto por FASE, y marca de SEGUNDA CASA, PROGRAMA y MEDIOS. Nada se toca."""
import json, io, sys, re, collections, itertools
sys.stdout.reconfigure(encoding="utf-8")
G = json.load(io.open("dataset/metadata/master_graph.json", encoding="utf-8"))["nodos"]
VIV = {k: v for k, v in G.items() if not v.get("deprecado")}
V = [json.loads(l) for l in io.open("docs/INTRA_DOMINIO_VEREDICTOS.jsonl", encoding="utf-8") if l.strip()]
P = [json.loads(l) for l in io.open("docs/INTRA_DOMINIO_PARES.jsonl", encoding="utf-8") if l.strip()]
leido = {frozenset((r["nodo_a"], r["nodo_b"])): r for r in V}
encola = {frozenset((p["nodo_a"], p["nodo_b"])) for p in P}
COL = re.compile(r"never\s+lose\s+a\s+customer|coleman", re.I)

def fuentes(v):
    f = v.get("fuente")
    if isinstance(f, list): return f
    return re.split(r"\s*[;|]\s*|\s+/\s+", f or "")

prim, seg = [], []
for k, v in sorted(VIV.items()):
    fs = [x for x in fuentes(v) if x.strip()]
    if not fs: continue
    if COL.search(fs[0]): prim.append(k)
    elif any(COL.search(x) for x in fs[1:]): seg.append(k)
print("1. CONTADOR POR LA FUENTE: primera o unica %d | SEGUNDA CASA %d | total %d" % (len(prim), len(seg), len(prim)+len(seg)))
print()
# CRITERIO DE PERTENENCIA A LA SERIE, declarado y ESTRECHO a proposito:
# PROGRAMA = un nodo cuyo id o titulo nombra una de las OCHO FASES por su nombre
#            propio (assess, admit, affirm, activate, acclimate, accomplish, adopt,
#            advocate), o que enumera las ocho.
# La palabra suelta "fase" NO basta: metia project_close_out, que es de gestion de
# proyectos y solo tiene a Coleman de segunda casa.
RXF = re.compile(r"assess|admit|affirm|activate|acclimate|accomplish|adopt|advoca"
                 r"|ocho_fases|ocho fases|8_fases|ocho etapas", re.I)
# CORREGIDO el 11 ago 2026: la lista vieja no tenia MEDIO ni CANAL, y dejaba fuera
# a seis_medios_comunicacion_cliente, que es LA CABEZA de la serie de medios.
# Lo levanto el veredicto 948, no el contador: por eso los dos instrumentos.
MED = re.compile(r"correo|email|video|regalo|gift|carta|postal|llamada|telefon|sms|mensaje"
                 r"|evento|herramienta|medios_comunicacion|seis_medios|canales_comunicacion"
                 r"|multicanal|sorprender", re.I)
serie = []
for k in prim + seg:
    v = VIV[k]; t = v.get("titulo_concepto") or ""
    esfase = bool(RXF.search(k) or RXF.search(t))
    esmedio = bool(MED.search(k) or MED.search(t))
    if esfase or esmedio: serie.append((k, t, esfase, esmedio, k in seg))
print("2. LA SERIE (fases del programa + medios): %d nodos" % len(serie))
print()
print("| id | titulo | papel | casa |")
for k, t, ef, em, s2 in sorted(serie, key=lambda x: (not x[2], x[0])):
    papel = "PROGRAMA" if ef and not em else ("MEDIOS" if em and not ef else ("PROGRAMA+MEDIOS" if ef and em else "?"))
    print("| %-44s | %-52s | %-15s | %s |" % (k, t[:52], papel, "SEGUNDA CASA" if s2 else "primera"))
nom = {k for k, _, _, _, _ in serie}
pos = len(nom)*(len(nom)-1)//2
ley = [p for p in itertools.combinations(sorted(nom),2) if frozenset(p) in leido]
col = [p for p in itertools.combinations(sorted(nom),2) if frozenset(p) in encola and frozenset(p) not in leido]
cl = collections.Counter(leido[frozenset(p)]["clase"] for p in ley)
forma = "PURO" if cl.get("A",0)==len(ley)==pos else ("SUB-PURO" if len(ley) and cl.get("A",0)==len(ley) else ("MEZCLADO" if len(ley) else "SIN LEER"))
print()
print("3. BARRIDO DE LAS A: miembros %d | posibles %d | leidos %d %s | en cola %d | fuera de cola %d | FORMA %s"
      % (len(nom), pos, len(ley), dict(cl), len(col), pos-len(ley)-len(col), forma))
for a,b in ley: print("      [%s] %s | %s  (puesto %d)"%(leido[frozenset((a,b))]["clase"],a,b,leido[frozenset((a,b))]["puesto_intra"]))
print()
print("4. LOS DE COLEMAN QUE NO ENTRAN A LA SERIE: %d" % (len(prim)+len(seg)-len(serie)))
for k in sorted(set(prim+seg) - nom)[:40]: print("   -", k)
