# -*- coding: utf-8 -*-
"""VARA PROPIA DEL AUDITOR, VUELTA 91. Adjudica la direccion de los 88 pares de
OP-E-07 con una regla DISTINTA de la del ejecutor.

La del ejecutor: segmento de texto desde la primera mencion de cada id hasta la
mencion del otro, y busca la MARCA DE HIJO ("trae" no autoreferencial, o
"desarrolla", o "RECORRE EL CAMINO") en exactamente uno de los dos segmentos.

La mia: NO segmenta ni busca marca de hijo. Parte la razon en ORACIONES, se
queda con las oraciones DESCRIPTIVAS (la que empieza nombrando un id), y puntua
cada id con dos lexicos INDEPENDIENTES, uno de MADRE (el que dice, nombra,
enumera, indexa, compara o despacha) y otro de HIJO (el que desarrolla,
detalla, dibuja, llena, monta la infraestructura o es UNO DE ESOS). Gana el id
con saldo (madre menos hijo) estrictamente mayor. Si empatan, SIN VEREDICTO y
se lee a mano.
"""
import io, json, re, os

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
VER = os.path.join(RAIZ, "docs", "INTRA_DOMINIO_VEREDICTOS.jsonl")
DIR = os.path.join(RAIZ, "docs", "plan", "OP_E_07_DIRECCION_V91.jsonl")

LEX_MADRE = [
    r"dice en su paso", r"en UNA LINEA", r"en DOS LINEAS", r"ES EL INDICE",
    r"\bENUMERA\b", r"\benumera\b", r"MONTA EL MARCO", r"describe las piezas",
    r"\bcompara los\b", r"\bdespacha\b", r"\bnombra\b", r"\blista\b",
    r"\bes el indice\b", r"\bes la lista\b", r"\bes el catalogo general\b",
    r"\bMANDA\b", r"\bindexa\b", r"\bel marco\b",
]
LEX_HIJO = [
    r"\btrae el\b", r"\btrae la\b", r"\btrae un\b", r"\btrae las\b", r"\btrae los\b",
    r"ES EL PROCEDIMIENTO", r"es el procedimiento", r"\bdesarrolla\b",
    r"RECORRE EL CAMINO", r"\bDIBUJA UNA\b", r"LLENA LA PATA",
    r"monta la infraestructura", r"\bes uno de esos\b", r"ES UNO DE ESOS",
    r"con su procedimiento", r"\bde esa linea\b", r"\bde esa\b",
    r"\bdetalla\b", r"\bel detalle\b", r"\bel catalogo de\b",
]
RE_M = [re.compile(p, re.IGNORECASE) for p in LEX_MADRE]
RE_H = [re.compile(p, re.IGNORECASE) for p in LEX_HIJO]


def oraciones(t):
    return [s for s in re.split(r"(?<=[.;])\s+", t) if s.strip()]


def saldo(razon, nid, otro):
    m = h = 0
    for s in oraciones(razon):
        if nid not in s:
            continue
        # solo el tramo de la oracion que habla de ESTE id: desde su mencion
        # hasta la mencion del otro (si el otro aparece despues) o al final
        i = s.find(nid)
        j = s.find(otro, i + len(nid))
        tramo = s[i:] if j == -1 else s[i:j]
        if re.search(r"\btrae\s+lo\s+suyo\b", tramo, re.IGNORECASE):
            tramo = re.sub(r"\btrae\s+lo\s+suyo\b", " ", tramo, flags=re.IGNORECASE)
        m += sum(1 for r in RE_M if r.search(tramo))
        h += sum(1 for r in RE_H if r.search(tramo))
    return m - h


V = {}
for l in io.open(VER, encoding="utf-8"):
    l = l.strip()
    if not l:
        continue
    d = json.loads(l)
    V[int(d["puesto_intra"])] = d

EJ = {}
for l in io.open(DIR, encoding="utf-8"):
    d = json.loads(l)
    EJ[int(d["puesto"])] = (d["madre"], d["hijo"])

coinc = disc = sin = 0
filas = []
for p in sorted(EJ):
    v = V[p]
    a, b = v["nodo_a"], v["nodo_b"]
    r = v["razon"]
    sa, sb = saldo(r, a, b), saldo(r, b, a)
    if sa > sb:
        mia = (a, b)
    elif sb > sa:
        mia = (b, a)
    else:
        mia = None
    ej = EJ[p]
    if mia is None:
        est = "SIN VEREDICTO"; sin += 1
    elif mia == ej:
        est = "COINCIDE"; coinc += 1
    else:
        est = "DISCREPA"; disc += 1
    filas.append((p, est, ej, mia, sa, sb))

for p, est, ej, mia, sa, sb in filas:
    if est != "COINCIDE":
        print("%-6s %-14s ejecutor: %s -> %s | mia: %s | saldos a=%d b=%d" %
              (p, est, ej[0], ej[1], ("%s -> %s" % mia) if mia else "(empate)", sa, sb))
print()
print("=" * 78)
print("TOTAL 88 | COINCIDEN: %d | DISCREPAN: %d | SIN VEREDICTO DE MI VARA: %d" % (coinc, disc, sin))
