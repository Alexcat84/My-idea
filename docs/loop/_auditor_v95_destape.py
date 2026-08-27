# -*- coding: utf-8 -*-
"""_auditor_v95_destape.py . EL DESTAPE de la relectura ciega de la vuelta 95:
las razones escritas y la direccion escrita de los 16 pares que
_auditor_v95_ciega_pasos.py volco SIN razon, mas los cuatro caidos de la
operacion y el 1191, que son las varas.

Se corre DESPUES de haber adjudicado a ciegas, nunca antes:

    python docs/loop/_auditor_v95_destape.py > docs/loop/_auditor_v95_destape.txt
"""
import io
import json
import os

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LEIDOS = [886, 890, 947, 1844, 896, 909, 910, 940, 983, 993, 1020, 1057, 1086, 1196, 1220, 1083]
VARAS = [1098, 1009, 1281, 1992, 1191]


def cargar(ruta):
    with io.open(ruta, encoding="utf-8") as f:
        return [json.loads(l) for l in f if l.strip()]


ver = {int(v["puesto_intra"]): v for v in cargar(os.path.join(RAIZ, "docs", "INTRA_DOMINIO_VEREDICTOS.jsonl"))}
dirs = {f["puesto"]: f for f in cargar(os.path.join(RAIZ, "docs", "plan", "OP_E_07_DIRECCION_V94.jsonl"))}

print("=" * 90)
print("DESTAPE 1: LOS 16 DE LA CIEGA (razon escrita y direccion escrita)")
print("=" * 90)
for p in LEIDOS:
    d = dirs.get(p, {})
    print("PUESTO %d | madre escrita: %s | hijo: %s" % (p, d.get("madre"), d.get("hijo")))
    print("  RAZON: %s" % ver[p]["razon"])
    print()

print("=" * 90)
print("DESTAPE 2: LAS VARAS (los cuatro caidos de OP-E-07 y el 1191)")
print("=" * 90)
for p in VARAS:
    v = ver[p]
    print("PUESTO %d (%s / %s) | en la bolsa vigente: %s" % (p, v["nodo_a"], v["nodo_b"], p in dirs))
    print("  RAZON: %s" % v["razon"])
    print()
