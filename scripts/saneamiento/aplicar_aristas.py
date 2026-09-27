# -*- coding: utf-8 -*-
"""Aplica una tanda de correcciones de ARISTAS, cada una DECLARADA en los dos nodos que toca.

Saneamiento del dataset, TANDA 2 (decision del fundador del 26 sep 2026), puntos 7 y 9. Las aristas son simetricas:
a -> b vive en `nodos_siguientes` de a y en `nodos_previos` de b, y el paso 5 de scripts/run_phase1.py completa la
vista que falte a partir de cualquier nodo VIVO que la declare. Por eso cada operacion toca las dos vistas.

Uso:
  python scripts/saneamiento/aplicar_aristas.py <tanda.json> [--comprobar]

<tanda.json> es una lista de operaciones:
  {"id", "operacion": QUITAR | TEJER | RECABLEAR, "desde", "hacia", "hacia_nuevo" (solo RECABLEAR),
   "motivo", "evidencia", "decision", "fecha"}
  - QUITAR: la arista desde -> hacia sale de las dos vistas. Tiene que existir en alguna.
  - TEJER: la arista desde -> hacia entra en las dos vistas. Los dos extremos, vivos; no puede existir.
  - RECABLEAR: `hacia` es un nodo deprecado; la referencia pasa a `hacia_nuevo`, su superviviente vivo. Si
    desde -> hacia_nuevo ya existe, o hacia_nuevo es el propio desde, la referencia al deprecado solo sale.
    Vale igual con `desde` deprecado (la referencia del vivo `hacia` a su previo muerto).
El registro va al campo `correcciones` de cada nodo vivo que cambia: campo "aristas", veredicto ARISTA_QUITADA,
ARISTA_TEJIDA o ARISTA_RECABLEADA, texto_anterior y texto_nuevo como "desde -> hacia", y la evidencia.

Se niega (exit 1, sin escribir nada) si una operacion no se puede aplicar tal cual, o si su id ya esta en el nodo.
Con --comprobar solo valida.
"""
import json
import sys
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent.parent
NODOS = BASE / "dataset" / "nodos"
VEREDICTO = {"QUITAR": "ARISTA_QUITADA", "TEJER": "ARISTA_TEJIDA", "RECABLEAR": "ARISTA_RECABLEADA"}
PROHIBIDOS = (chr(0x2014), chr(0x2013))


def cargar(ids, nodos):
    for i in ids:
        if i and i not in nodos:
            ruta = NODOS / ("%s.json" % i)
            nodos[i] = json.loads(ruta.read_text(encoding="utf-8")) if ruta.exists() else None


def tiene(nodos, a, b):
    na, nb = nodos.get(a), nodos.get(b)
    return bool((na and b in (na.get("nodos_siguientes") or [])) or (nb and a in (nb.get("nodos_previos") or [])))


def quitar(nodos, a, b):
    tocados = []
    if nodos.get(a) and b in (nodos[a].get("nodos_siguientes") or []):
        nodos[a]["nodos_siguientes"] = [x for x in nodos[a]["nodos_siguientes"] if x != b]
        tocados.append(a)
    if nodos.get(b) and a in (nodos[b].get("nodos_previos") or []):
        nodos[b]["nodos_previos"] = [x for x in nodos[b]["nodos_previos"] if x != a]
        tocados.append(b)
    return tocados


def tejer(nodos, a, b):
    tocados = []
    if b not in (nodos[a].get("nodos_siguientes") or []):
        nodos[a].setdefault("nodos_siguientes", []).append(b)
        tocados.append(a)
    if a not in (nodos[b].get("nodos_previos") or []):
        nodos[b].setdefault("nodos_previos", []).append(a)
        tocados.append(b)
    return tocados


def vivo(nodos, i):
    return nodos.get(i) is not None and not nodos[i].get("deprecado")


def aplicar(op, nodos):
    """Devuelve (fallas, {nodo vivo tocado: (anterior, nuevo)})."""
    a, b, c = op.get("desde"), op.get("hacia"), op.get("hacia_nuevo")
    o = op.get("operacion")
    cargar([a, b, c], nodos)
    fallas = []
    for k in ("id", "operacion", "desde", "hacia", "motivo", "evidencia", "decision", "fecha"):
        if not op.get(k):
            fallas.append("falta %s" % k)
    if o not in VEREDICTO:
        return fallas + ["operacion no admitida: %r" % o], {}
    if any(p in str(op.get("motivo", "")) for p in PROHIBIDOS):
        fallas.append("el motivo trae guion largo o medio")
    if fallas:
        return fallas, {}
    anterior = "%s -> %s" % (a, b)
    if o == "QUITAR":
        if not tiene(nodos, a, b):
            return ["la arista %s no existe" % anterior], {}
        return [], {n: (anterior, "") for n in quitar(nodos, a, b) if vivo(nodos, n)}
    if o == "TEJER":
        if not (vivo(nodos, a) and vivo(nodos, b)):
            return ["TEJER exige dos extremos vivos: %s" % anterior], {}
        if tiene(nodos, a, b):
            return ["la arista %s ya existe" % anterior], {}
        return [], {n: ("", anterior) for n in tejer(nodos, a, b)}
    # RECABLEAR: el extremo muerto es `hacia` (una arista de un vivo a un deprecado) o `desde` (un vivo con un
    # previo deprecado); el vivo es el otro.
    if not c or not vivo(nodos, c):
        return ["RECABLEAR exige hacia_nuevo vivo: %r" % c], {}
    if not tiene(nodos, a, b):
        return ["la arista %s no existe" % anterior], {}
    if vivo(nodos, a) and not vivo(nodos, b):
        par_nuevo = (a, c)
    elif vivo(nodos, b) and not vivo(nodos, a):
        par_nuevo = (c, b)
    else:
        return ["RECABLEAR exige exactamente un extremo deprecado: %s" % anterior], {}
    tocados = {n for n in quitar(nodos, a, b) if vivo(nodos, n)}
    x, y = par_nuevo
    nuevo = ""
    if x != y and not tiene(nodos, x, y):
        nuevo = "%s -> %s" % (x, y)
        tocados |= set(tejer(nodos, x, y))
    return [], {n: (anterior, nuevo) for n in tocados}


def main(argv):
    tanda = json.loads(Path(argv[0]).read_text(encoding="utf-8"))
    comprobar = "--comprobar" in argv
    nodos, fallas, cambiados = {}, [], set()
    for op in tanda:
        f, tocados = aplicar(op, nodos)
        for x in f:
            fallas.append("%s: %s" % (op.get("id"), x))
        for n, (antes, despues) in tocados.items():
            if any(r.get("id") == op["id"] for r in nodos[n].get("correcciones", [])):
                fallas.append("%s: ya esta aplicada en %s" % (op["id"], n))
                continue
            nodos[n].setdefault("correcciones", []).append({
                "id": op["id"], "fecha": op["fecha"], "campo": "aristas", "veredicto": VEREDICTO[op["operacion"]],
                "texto_anterior": antes, "texto_nuevo": despues,
                "cita": {"instrumento": op["evidencia"], "motivo": op["motivo"]}, "decision": op["decision"]})
            cambiados.add(n)
    if fallas:
        print("TANDA RECHAZADA, no se escribio nada:")
        for f in fallas[:60]:
            print("  " + f)
        return 1
    if comprobar:
        print("TANDA VALIDA: %d operaciones, %d nodos vivos cambian (sin escribir)" % (len(tanda), len(cambiados)))
        return 0
    for n in sorted(cambiados):
        (NODOS / ("%s.json" % n)).write_text(json.dumps(nodos[n], ensure_ascii=False, indent=2), encoding="utf-8")
    print("TANDA APLICADA: %d operaciones, %d nodos vivos cambiados" % (len(tanda), len(cambiados)))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
