# -*- coding: utf-8 -*-
"""Vara PROPIA del auditor v92: el DISCRIMINADOR que el acta 91 seccion 3.1
establecio, aplicado a las 87 que se quedan.

  formula MADRE/HIJO : "trae el procedimiento DE ESA LINEA / de su paso N /
                       de esa competencia / de la SEGUNDA..."  -> nombra la
                       linea de la madre que el hijo despliega.
  formula de la D    : "trae un procedimiento QUE EL OTRO NO TIENE / que esa
                       fase no tiene / que el otro no tiene en ninguna forma"
                       -> cada uno trae lo suyo. NO es jerarquia.

El 1098 cayo por usar la segunda y haberse leido como la primera."""
import io, json, os, re
RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
V = {int(v["puesto_intra"]): v for v in (json.loads(l) for l in io.open(os.path.join(RAIZ,"docs","INTRA_DOMINIO_VEREDICTOS.jsonl"),encoding="utf-8") if l.strip())}
filas = [json.loads(l) for l in io.open(os.path.join(RAIZ,"docs","plan","OP_E_07_DIRECCION_V92.jsonl"),encoding="utf-8") if l.strip()]

# la formula de la D: "trae/tiene UN procedimiento ... que ... NO tiene"
D_NO_TIENE = re.compile(r"trae\s+(?:un|su)\s+[^.]{0,120}?\bno\s+(?:lo\s+)?tiene", re.IGNORECASE)
# la formula madre/hijo: "trae el procedimiento de esa/su/la ... linea/paso/etapa/..."
MH_DE_ESA = re.compile(r"trae\s+(?:el|la|los|las)\s+[^.]{0,140}?\bde\s+(?:esa|ese|esas|esos|su|sus|la|el|las|los)\b", re.IGNORECASE)

d_sola, mh, ambas, ninguna = [], [], [], []
for f in sorted(filas, key=lambda x: x["puesto"]):
    p = f["puesto"]; r = V[p]["razon"]
    a = bool(D_NO_TIENE.search(r)); b = bool(MH_DE_ESA.search(r))
    if a and not b: d_sola.append(p)
    elif b and not a: mh.append(p)
    elif a and b: ambas.append(p)
    else: ninguna.append(p)
print("de las 87 que SE QUEDAN:")
print("  formula MADRE/HIJO ('trae el procedimiento de esa/su ...'), sin la de la D : %d" % len(mh))
print("  LAS DOS formulas en la misma razon                                        : %d %s" % (len(ambas), ambas))
print("  SOLO la formula de la D ('trae un procedimiento que ... no tiene')         : %d %s" % (len(d_sola), d_sola))
print("  NINGUNA de las dos                                                        : %d %s" % (len(ninguna), ninguna))
print()
for p in d_sola:
    m = D_NO_TIENE.search(V[p]["razon"])
    print("  puesto %-5s D: ...%s..." % (p, m.group(0)))
