# -*- coding: utf-8 -*-
"""Aplica una tanda de correcciones de FIDELIDAD a dataset/nodos, cada una DECLARADA en el nodo.

Mandato del fundador (campania de fidelidad total, sep 2026): nunca le diremos a un
cliente lo contrario de lo que dice su fuente. Cada cambio es una correccion
declarada: el texto viejo NO se borra, queda en el campo `correcciones` del propio
nodo, con la cita literal del libro que motiva el cambio ("una correccion que tapa
lo que corrige no se puede auditar", docs/loop/EJECUTOR.md regla 8).

Uso:
  python scripts/fidelidad/aplicar_correcciones.py <tanda.json> [--comprobar]

<tanda.json> es una lista de correcciones:
  {"id", "node_id", "campo" (pasos_accionables | resumen_teorico | entregable_esperado),
   "indice" (solo pasos, desde 0), "veredicto" (CONTRARIO | ANADIDO), "texto_anterior",
   "texto_nuevo", "cita": {"libro", "fichero", "lineas", "frase"}, "decision", "auditoria"}

Se niega (exit 1, sin escribir nada) si el texto anterior no es EXACTAMENTE el
vigente, si el nuevo trae guiones largos o medios, si falta la cita, o si el id
de la correccion ya esta aplicado en el nodo. Con --comprobar solo valida.
"""
import json
import sys
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent.parent
NODOS = BASE / "dataset" / "nodos"
CAMPOS = {"pasos_accionables", "resumen_teorico", "entregable_esperado"}
PROHIBIDOS = ("—", "–")


def validar(c, nodo):
    fallas = []
    for k in ("id", "node_id", "campo", "veredicto", "texto_anterior", "texto_nuevo", "cita", "decision", "fecha"):
        if not c.get(k):
            fallas.append("falta %s" % k)
    if c.get("campo") not in CAMPOS:
        fallas.append("campo no admitido: %r" % c.get("campo"))
    cita = c.get("cita") or {}
    for k in ("libro", "lineas", "frase"):
        if not cita.get(k):
            fallas.append("cita sin %s" % k)
    if any(p in c.get("texto_nuevo", "") for p in PROHIBIDOS):
        fallas.append("el texto nuevo trae guion largo o medio")
    if c.get("texto_nuevo") == c.get("texto_anterior"):
        fallas.append("el texto nuevo es igual al anterior")
    if nodo is None:
        return fallas + ["el nodo no existe"]
    if any(x.get("id") == c.get("id") for x in nodo.get("correcciones", [])):
        fallas.append("la correccion %s ya esta aplicada" % c.get("id"))
    if c.get("campo") == "pasos_accionables":
        pasos = nodo.get("pasos_accionables", [])
        i = c.get("indice")
        if not isinstance(i, int) or not 0 <= i < len(pasos):
            fallas.append("indice fuera de rango: %r" % i)
        elif pasos[i] != c["texto_anterior"]:
            fallas.append("el texto anterior no es el vigente del paso %d" % i)
    elif nodo.get(c.get("campo")) != c.get("texto_anterior"):
        fallas.append("el texto anterior no es el vigente de %s" % c.get("campo"))
    return fallas


def main(argv):
    tanda = json.loads(Path(argv[0]).read_text(encoding="utf-8"))
    comprobar = "--comprobar" in argv
    nodos, fallas = {}, []
    for c in tanda:
        ruta = NODOS / ("%s.json" % c.get("node_id"))
        if c.get("node_id") not in nodos:
            nodos[c.get("node_id")] = json.loads(ruta.read_text(encoding="utf-8")) if ruta.exists() else None
        for f in validar(c, nodos[c.get("node_id")]):
            fallas.append("%s (%s): %s" % (c.get("id"), c.get("node_id"), f))
        if not fallas and nodos[c.get("node_id")] is not None:
            nodo = nodos[c["node_id"]]
            if c["campo"] == "pasos_accionables":
                nodo["pasos_accionables"][c["indice"]] = c["texto_nuevo"]
            else:
                nodo[c["campo"]] = c["texto_nuevo"]
            registro = {k: c[k] for k in ("id", "fecha", "campo", "veredicto", "texto_anterior", "texto_nuevo", "cita", "decision")}
            if c["campo"] == "pasos_accionables":
                registro["indice"] = c["indice"]
            if c.get("auditoria"):
                registro["auditoria"] = c["auditoria"]
            nodo.setdefault("correcciones", []).append(registro)
    if fallas:
        print("TANDA RECHAZADA, no se escribio nada:")
        for f in fallas:
            print("  " + f)
        return 1
    if comprobar:
        print("TANDA VALIDA: %d correcciones en %d nodos (sin escribir)" % (len(tanda), len(nodos)))
        return 0
    for nid, nodo in nodos.items():
        (NODOS / ("%s.json" % nid)).write_text(json.dumps(nodo, ensure_ascii=False, indent=2), encoding="utf-8")
    print("TANDA APLICADA: %d correcciones en %d nodos" % (len(tanda), len(nodos)))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
