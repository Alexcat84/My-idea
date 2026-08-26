"""VUELTA 75, OP-E-02: control mecanico de RACIMOS_MIEMBROS.jsonl contra el
grafo vivo de HOY. Por cada racimo: cuantos de sus 32 (miembros declarados en
docs/RACIMOS_MIEMBROS.jsonl, censados el 9 ago 2026) siguen vivos, cuantos ya
murieron en una fusion de la fase 03 (y a que resuelven), y si alguno de los
vivos tiene un dominio real DISTINTO del dominio censado del racimo (la figura
RACIMO CON MIEMBRO AJENO de 04_ENLACES.md). Solo lee.
"""
import json
from pathlib import Path
from collections import Counter

RAIZ = Path(__file__).resolve().parents[2]

with open(RAIZ / "dataset/metadata/master_graph.json", encoding="utf-8") as f:
    grafo = json.load(f)
nodos = grafo["nodos"] if "nodos" in grafo else grafo

def resolver(node_id, visto=None):
    visto = visto or set()
    if node_id in visto:
        return None
    visto.add(node_id)
    if node_id in nodos and not nodos[node_id].get("deprecado"):
        return node_id
    # buscar por alias (tambien cuando node_id SI esta en nodos pero deprecado)
    for nid, data in nodos.items():
        if node_id in (data.get("ids_alias") or []):
            if data.get("deprecado"):
                return resolver(nid, visto)
            return nid
    return None

with open(RAIZ / "docs/RACIMOS_MIEMBROS.jsonl", encoding="utf-8") as f:
    racimos = [json.loads(l) for l in f if l.strip()]

print(f"racimos censados: {len(racimos)}")
print()

def dominios_permitidos(dominio_censado):
    """El catalogo gratis se declara NUCLEO en RACIMOS_MIEMBROS.jsonl y como
    dominio 'core' en el grafo (00_INDICE.md y 04_ENLACES.md usan 'core' para
    ese mismo catalogo). Se normaliza ANTES de comparar, o cada racimo de
    nucleo sale como transversal por un problema de nombre, no de dominio."""
    texto = dominio_censado.lower()
    doms = set()
    for token in ["quality", "environmental", "franquicias", "exportacion",
                  "health_safety", "entrega", "seguridad_digital",
                  "risk_management", "compras"]:
        if token in texto:
            doms.add(token)
    if "nucleo" in texto or "core" in texto:
        doms.add("core")
    return doms

total_vivos = 0
total_muertos = 0
transversales_nuevos = []

for r in racimos:
    dominio_racimo = r["dominio_censado"]
    permitidos = dominios_permitidos(dominio_racimo)
    vivos, muertos, ajenos = [], [], []
    for m in r["miembros"]:
        nid = m["node_id"]
        resuelto = resolver(nid)
        if resuelto is None:
            muertos.append((nid, "SIN RASTRO"))
            continue
        data = nodos[resuelto]
        if data.get("deprecado"):
            muertos.append((nid, f"resuelve a {resuelto} pero SIGUE deprecado"))
            continue
        vivos.append((nid, resuelto))
        dom_real = data.get("dominio")
        if dom_real not in permitidos:
            ajenos.append((nid, resuelto, dom_real))

    total_vivos += len(vivos)
    total_muertos += len(muertos)
    if ajenos:
        transversales_nuevos.append((r["racimo"], dominio_racimo, ajenos))

    if muertos or ajenos:
        print(f"--- {r['racimo']} ({dominio_racimo}, censado {r['tamano_censado']})")
        if muertos:
            print(f"    MUERTOS/fundidos desde el censo: {len(muertos)}")
            for nid, why in muertos:
                print(f"      {nid}: {why}")
        if ajenos:
            print(f"    MIEMBRO AJENO (dominio real distinto del censado): {len(ajenos)}")
            for nid, resuelto, dom in ajenos:
                print(f"      {nid} (resuelve a {resuelto}) es de {dom}, no de {dominio_racimo}")
        print()

print("="*80)
print(f"TOTAL miembros vivos hoy: {total_vivos}")
print(f"TOTAL miembros muertos/fundidos desde el censo: {total_muertos}")
print(f"Racimos con miembro ajeno HOY: {len(transversales_nuevos)}")
