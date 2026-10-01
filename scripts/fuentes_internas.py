# -*- coding: utf-8 -*-
"""FUENTES COMPLETAS POR NODO (decisiones del fundador del 27 sep 2026, puntos 1 y 4).

Para cada nodo vivo calcula la lista COMPLETA de sus fuentes: la suya mas las de todos los nodos que absorbio, por
cualquier fusion y en cadena, sin limite de eslabones. La guarda en el campo interno `fuentes_internas` del nodo y en
el inventario interno docs/internos/INVENTARIO_FUENTES.md. El campo `fuente` NO se toca. Es solo registro interno:
jamas se muestra al cliente (scripts/sync_assets_web.py lo quita de la vista web; guarda:
web/lib/procedencia.test.ts).

De donde sale quien absorbio a quien (absorbido -> absorbedor), por prioridad:
  1. `ids_alias` y `merged_originals` de cada nodo de dataset/nodos (la verdad de hoy: es lo que usa el resolutor);
  2. merge_decisions.json y merge_decisions_v11.json (los perdedores de cada cluster -> su canonico);
  3. los mapas de alias de la era de las capas (alias_map_auto, _capa_b, _capa_c, _capa_d_duplicates);
  4. ghost_decisions_v11.json (referencias fantasma -> el nodo real que las representa).
Cada id sigue su cadena hasta el primer nodo vivo, como el resolutor de la web.

De donde sale la fuente de cada id: su fichero en dataset/nodos, su original en dataset/metadata/merged_originals*/,
la procedencia que guarda su absorbedor (`merged_originals`), y dataset/metadata/fuentes_historicas.json (lo que solo
quedaba en el historial de git). Un id sin fuente en ninguno de esos sitios es una referencia que nunca fue nodo: el
inventario la cuenta aparte, no se pierde en silencio.

    python scripts/fuentes_internas.py              # escribe el campo en los nodos vivos y el inventario
    python scripts/fuentes_internas.py --comprobar  # solo compara (exit 1 si algun nodo no esta al dia)
"""
import json
import sys
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent
NODOS = BASE / "dataset" / "nodos"
META = BASE / "dataset" / "metadata"
INVENTARIO = BASE / "docs" / "internos" / "INVENTARIO_FUENTES.md"
MAPAS_CAPAS = ("alias_map_auto.json", "alias_map_capa_b.json", "alias_map_capa_c.json", "alias_map_capa_d_duplicates.json")


CANON = json.loads((META / "fuentes_canonicas.json").read_text(encoding="utf-8"))["fuentes"]


def partes(fuente):
    """Las fuentes de un campo `fuente`, cada una con el nombre canonico de su libro (`igual_a` en
    dataset/metadata/fuentes_canonicas.json): dos formas de escribir el mismo libro son UN libro."""
    out = []
    for p in str(fuente or "").split(" | "):
        p = p.strip()
        if p:
            p = CANON.get(p, {}).get("igual_a", p)
            if p not in out:
                out.append(p)
    return out


def cargar():
    nodos = {}
    for p in NODOS.glob("*.json"):
        n = json.loads(p.read_text(encoding="utf-8"))
        nodos[n["node_id"]] = n
    originales = {}
    for d in ("merged_originals", "merged_originals_v11"):
        for p in (META / d).glob("*.json"):
            x = json.loads(p.read_text(encoding="utf-8"))
            originales.setdefault(x.get("node_id") or p.stem, []).append(x.get("fuente"))
    decisiones = []
    for f in ("merge_decisions.json", "merge_decisions_v11.json"):
        decisiones += json.loads((META / f).read_text(encoding="utf-8"))
    capas = {}
    for f in MAPAS_CAPAS:
        capas.update(json.loads((META / f).read_text(encoding="utf-8")))
    fantasmas = json.loads((META / "ghost_decisions_v11.json").read_text(encoding="utf-8"))
    historicas = json.loads((META / "fuentes_historicas.json").read_text(encoding="utf-8"))["nodos"]
    return nodos, originales, decisiones, capas, fantasmas, historicas


def calcular(nodos, originales, decisiones, capas, fantasmas, historicas):
    """{nodo vivo: [fuentes]}, {nodo vivo: [ids absorbidos]}, [ids absorbidos sin fuente registrada]."""
    vivos = {k for k, n in nodos.items() if not n.get("deprecado")}
    absorbedor = {}

    def declarar(a, b):
        if a and b and a != b and a not in absorbedor and a not in vivos:
            absorbedor[a] = b

    for k, n in sorted(nodos.items()):
        for a in n.get("ids_alias") or []:
            declarar(a, k)
        for m in n.get("merged_originals") or []:
            declarar(m.get("node_id"), k)
    for c in decisiones:
        for a in c.get("losers") or []:
            declarar(a, c.get("canonical_id"))
    for a, b in sorted(capas.items()):
        declarar(a, b)
    for a, b in sorted(fantasmas.items()) if isinstance(fantasmas, dict) else []:
        if isinstance(b, str):
            declarar(a, b)

    fuentes_de = {}

    def sumar(i, f):
        for p in partes(f):
            fuentes_de.setdefault(i, [])
            if p not in fuentes_de[i]:
                fuentes_de[i].append(p)

    for k, n in nodos.items():
        sumar(k, n.get("fuente"))
        for m in n.get("merged_originals") or []:
            sumar(m.get("node_id"), m.get("fuente"))
    for k, fs in originales.items():
        for f in fs:
            sumar(k, f)
    for k, h in historicas.items():
        sumar(k, h.get("fuente"))

    def resolver(i):
        visto = {i}
        cur = i
        while cur not in vivos and cur in absorbedor:
            cur = absorbedor[cur]
            if cur in visto:
                return None
            visto.add(cur)
        return cur if cur in vivos else None

    absorbidos = {k: [] for k in vivos}
    for i in absorbedor:
        r = resolver(i)
        if r is not None:
            absorbidos[r].append(i)
    resultado, sin_fuente = {}, []
    for k in sorted(vivos):
        lista = list(partes(nodos[k].get("fuente")))
        for i in sorted(absorbidos[k]):
            if not fuentes_de.get(i):
                sin_fuente.append(i)
            for f in fuentes_de.get(i, []):
                if f not in lista:
                    lista.append(f)
        resultado[k] = lista
    return resultado, {k: sorted(v) for k, v in absorbidos.items() if v}, sorted(sin_fuente)


def inventario(resultado, absorbidos, sin_fuente, nodos):
    varias = {k: v for k, v in resultado.items() if len(v) > 1}
    libros = sorted({f for v in resultado.values() for f in v})
    out = [
        "# Inventario interno de fuentes por nodo",
        "",
        "INTERNO. Decisiones del fundador del 27 sep 2026, puntos 1 y 4: cada nodo vivo con la lista COMPLETA de sus "
        "fuentes, la suya mas las de todos los nodos que absorbio por cualquier fusion y en cadena, sin limite. Lo "
        "genera `python scripts/fuentes_internas.py` (no se edita a mano) y es el mismo contenido que el campo interno "
        "`fuentes_internas` de cada nodo. El campo `fuente` no se toca. Nada de esto llega al cliente: ni a la web, ni a "
        "un documento, ni a un correo, ni a una respuesta de la IA (REGLA ESTRICTA del 26 sep 2026).",
        "",
        "## Resumen",
        "",
        "- Nodos vivos: %d" % len(resultado),
        "- Con mas de un libro (fusiones entre libros distintos): %d" % len(varias),
        "- Nodos que absorbieron a otros: %d (%d ids absorbidos)" % (len(absorbidos), sum(len(v) for v in absorbidos.values())),
        "- Fuentes distintas: %d" % len(libros),
        "- Ids absorbidos sin fuente registrada en ningun sitio (referencias que nunca fueron nodo): %d" % len(sin_fuente),
        "",
        "## Nodos con mas de un libro",
        "",
        "| nodo | fuentes | absorbio |",
        "|---|---|---|",
    ]
    for k, v in sorted(varias.items()):
        out.append("| %s | %s | %s |" % (k, "<br>".join(x.replace("|", "/") for x in v), ", ".join(absorbidos.get(k, []))))
    out += ["", "## Todos los nodos vivos", "", "| nodo | n | fuentes |", "|---|---:|---|"]
    for k, v in sorted(resultado.items()):
        out.append("| %s | %d | %s |" % (k, len(v), "<br>".join(x.replace("|", "/") for x in v)))
    out += ["", "## Ids absorbidos sin fuente registrada", "",
            "Referencias de la era de la extraccion y de las capas de alias (una arista a un id que nunca fue fichero de "
            "nodo, ni en dataset/ ni en el historial de git). No traen libro propio: su absorbedor ya lista el suyo.", ""]
    out.append(", ".join(sin_fuente) if sin_fuente else "Ninguno.")
    return "\n".join(out) + "\n"


def main(argv):
    comprobar = "--comprobar" in argv
    nodos, *resto = cargar()
    resultado, absorbidos, sin_fuente = calcular(nodos, *resto)
    desfasados = [k for k, v in resultado.items() if nodos[k].get("fuentes_internas") != v]
    texto = inventario(resultado, absorbidos, sin_fuente, nodos)
    if comprobar:
        viejo = INVENTARIO.read_text(encoding="utf-8").replace("\r\n", "\n") if INVENTARIO.exists() else ""
        if desfasados or viejo != texto:
            print("DESFASADO: %d nodos sin sus fuentes_internas al dia%s; corre python scripts/fuentes_internas.py" % (
                len(desfasados), " y el inventario" if viejo != texto else ""))
            return 1
        print("AL DIA: %d nodos vivos con sus fuentes_internas" % len(resultado))
        return 0
    for k in desfasados:
        n = nodos[k]
        n["fuentes_internas"] = resultado[k]
        (NODOS / ("%s.json" % k)).write_text(json.dumps(n, ensure_ascii=False, indent=2), encoding="utf-8")
    INVENTARIO.parent.mkdir(parents=True, exist_ok=True)
    INVENTARIO.write_bytes(texto.encode("utf-8"))
    print("fuentes_internas: %d nodos vivos, %d actualizados, %d con mas de una fuente, %d ids absorbidos sin fuente" % (
        len(resultado), len(desfasados), sum(1 for v in resultado.values() if len(v) > 1), len(sin_fuente)))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
