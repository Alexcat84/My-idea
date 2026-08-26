"""VUELTA 77, TAREA 1.5: recomputo de la nomina de OP-S-09 desde el grafo,
aplicando el criterio ESCRITO en docs/plan/05_SANEO.md y docs/MESA_RACIMOS.md
DECISION 4 (familia unica, sufijo numerico / particulas / orden de palabras /
sinonimo puro), porque 05_SANEO.md trae el CRITERIO y las CIFRAS (53
familias, 125 nodos vivos) pero NO la lista de los 125 ids: la pagina es la
vara contra la que se comprueba este recomputo, no la fuente de la nomina.

METODO, declarado porque es el unico disponible sin releer 3.188 nodos a
mano:
1. Universo: solo nodos VIVOS (deprecado distinto de True).
2. Para cada id vivo se calcula una CLAVE NORMALIZADA:
   a. se separa en tokens por "_"
   b. se retira, SI Y SOLO SI hay mas de un token, un sufijo numerico final
      puro (tokens que son solo digitos), guardando aparte si el id tenia
      sufijo numerico
   c. se retiran las PARTICULAS (de, del, la, el, los, las, y) de la lista
      de tokens restante, guardando aparte si el id tenia alguna
   d. la CLAVE es la lista de tokens que sobran, ORDENADA alfabeticamente
      (esto agrupa tambien el orden de palabras)
3. Todo id vivo que comparte CLAVE con al menos otro id vivo forma una
   FAMILIA. Familias de tamano 1 se descartan (no son duplicado, son un id
   con un token compartido casual... NO: la clave ya exige coincidencia de
   TODOS los tokens no particulares, asi que un tamano 1 es simplemente un id
   sin gemelo).
4. CAUSA de la familia (una sola por familia, la mas fuerte primero):
   - SUFIJO NUMERICO si dos o mas miembros comparten el mismo stem (tokens
     SIN retirar particulas, EN EL MISMO ORDEN) y difieren solo en el
     sufijo numerico.
   - PARTICULAS si, tras solo retirar el sufijo numerico (sin tocar orden),
     los tokens coinciden en el MISMO ORDEN salvo por particulas insertadas
     o quitadas.
   - ORDEN DE PALABRAS si los tokens (ya sin particulas) son el MISMO
     CONJUNTO pero en ORDEN DISTINTO entre al menos dos miembros.
   - SINONIMO PURO: no detectable por este metodo lexico (exige leer
     contenido); se deja en 0 como el recomputo previo, y se declara.
5. EXCEPCIONES escritas en MESA_RACIMOS.md DECISION 4 y citadas en
   05_SANEO.md: la transdominio (`nafta_free_trade_agreements`, ya cubierta
   por OP-S-01) y el `_2` de propiedad intelectual salen del criterio
   general. Se excluyen por nombre si el barrido las encuentra.
"""
import json
import re
from pathlib import Path
from collections import defaultdict

RAIZ = Path(__file__).resolve().parents[2]
PARTICULAS = {"de", "del", "la", "el", "los", "las", "y"}
EXCEPCIONES = {"nafta_free_trade_agreements"}

with open(RAIZ / "dataset/metadata/master_graph.json", encoding="utf-8") as f:
    grafo = json.load(f)
nodos = grafo["nodos"] if "nodos" in grafo else grafo

vivos = {nid: d for nid, d in nodos.items() if not d.get("deprecado")}


def quitar_sufijo(tokens):
    if len(tokens) > 1 and tokens[-1].isdigit():
        return tokens[:-1], tokens[-1]
    return tokens, None


def quitar_particulas(tokens):
    sin = [t for t in tokens if t not in PARTICULAS]
    huboparticula = len(sin) != len(tokens)
    return sin, huboparticula


grupos = defaultdict(list)
info = {}
for nid in vivos:
    if nid in EXCEPCIONES:
        continue
    tokens = nid.split("_")
    stem, sufijo = quitar_sufijo(tokens)
    sin_particulas, hubo_particula = quitar_particulas(stem)
    clave = tuple(sorted(sin_particulas))
    if not clave:
        continue
    grupos[clave].append(nid)
    info[nid] = {
        "stem": tuple(stem),
        "sufijo": sufijo,
        "sin_particulas": tuple(sin_particulas),
        "hubo_particula": hubo_particula,
    }

familias = {clave: miembros for clave, miembros in grupos.items() if len(miembros) >= 2}


def causa_familia(miembros):
    stems = set(info[m]["stem"] for m in miembros)
    if len(stems) == 1 and any(info[m]["sufijo"] for m in miembros):
        return "SUFIJO NUMERICO"
    sin_part = set(info[m]["sin_particulas"] for m in miembros)
    if len(sin_part) == 1 and any(info[m]["hubo_particula"] for m in miembros):
        return "PARTICULAS"
    return "ORDEN DE PALABRAS"


por_causa = defaultdict(int)
nodos_por_causa = defaultdict(int)
todas = []
for clave, miembros in sorted(familias.items()):
    causa = causa_familia(miembros)
    por_causa[causa] += 1
    nodos_por_causa[causa] += len(miembros)
    todas.append((clave, sorted(miembros), causa))

total_familias = len(todas)
total_nodos = sum(len(m) for _, m, _ in todas)

print(f"FAMILIAS: {total_familias}")
print(f"NODOS VIVOS EN FAMILIA: {total_nodos}")
print()
print("POR CAUSA:")
for causa in ("SUFIJO NUMERICO", "PARTICULAS", "ORDEN DE PALABRAS"):
    print(f"  {causa}: {por_causa[causa]} familias, {nodos_por_causa[causa]} nodos")
print(f"  SINONIMO PURO: 0 familias (no detectable por metodo lexico, declarado)")
print()
print("LAS CUATRO MAYORES (por tamano, desempate alfabetico):")
mayores = sorted(todas, key=lambda t: (-len(t[1]), t[0]))[:4]
for clave, miembros, causa in mayores:
    print(f"  {'/'.join(clave)} ({causa}): {miembros}")
print()
print("NOMINA COMPLETA:")
nomina_ids = []
for clave, miembros, causa in todas:
    print(f"  [{causa}] {miembros}")
    nomina_ids.extend(miembros)
print()
print(f"NOMINA_IDS_TOTAL={len(nomina_ids)}")
print("NOMINA_IDS_JSON_START")
print(json.dumps(sorted(set(nomina_ids)), ensure_ascii=False))
print("NOMINA_IDS_JSON_END")
