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
  {"id", "node_id", "campo" (pasos_accionables | condiciones_activacion | resumen_teorico |
   entregable_esperado), "indice" (solo en los campos lista, pasos y condiciones, desde 0), "veredicto" (CONTRARIO | ANADIDO), "texto_anterior",
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
CAMPOS = {"pasos_accionables", "condiciones_activacion", "resumen_teorico", "entregable_esperado"}
# Los campos lista se corrigen elemento a elemento, por indice. Las condiciones de
# activacion entraron el 27 sep 2026: la pasada contra la fuente sobre los campos
# que no son pasos (docs/fidelidad/CAMPOS_QUE_LLEGAN.md) llegan a la IA.
LISTAS = {"pasos_accionables", "condiciones_activacion"}
PROHIBIDOS = (chr(0x2014), chr(0x2013))


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
    if c.get("campo") in LISTAS:
        lista = nodo.get(c["campo"], [])
        i = c.get("indice")
        if not isinstance(i, int) or not 0 <= i < len(lista):
            fallas.append("indice fuera de rango: %r" % i)
        elif lista[i] != c["texto_anterior"]:
            fallas.append("el texto anterior no es el vigente de %s[%d]" % (c["campo"], i))
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
            if c["campo"] in LISTAS:
                nodo[c["campo"]][c["indice"]] = c["texto_nuevo"]
            else:
                nodo[c["campo"]] = c["texto_nuevo"]
            registro = {k: c[k] for k in ("id", "fecha", "campo", "veredicto", "texto_anterior", "texto_nuevo", "cita", "decision")}
            if c["campo"] in LISTAS:
                registro["indice"] = c["indice"]
            if c.get("auditoria"):
                registro["auditoria"] = c["auditoria"]
            nodo.setdefault("correcciones", []).append(registro)
    # LAS BARANDAS DE LA CASA (scripts/censo_duplicacion.py): una correccion no
    # puede dejar en el nodo una baranda que antes no tenia (por ejemplo, una sigla
    # como FDA u OSHA sin la formula de localizacion). Nace de la tanda fidelidad-t1,
    # que salio a produccion con una sigla sin localizar porque nadie la miraba.
    if not fallas:
        sys.path.insert(0, str(BASE / "scripts"))
        try:
            import censo_duplicacion
        except ImportError:
            censo_duplicacion = None
        if censo_duplicacion is not None:
            for nid, nodo in nodos.items():
                ruta = NODOS / ("%s.json" % nid)
                antes = censo_duplicacion.revisar_barandas(json.loads(ruta.read_text(encoding="utf-8")))
                ya = {(b["baranda"], b.get("cita")) for b in antes}
                for b in censo_duplicacion.revisar_barandas(nodo):
                    if (b["baranda"], b.get("cita")) not in ya:
                        fallas.append("%s: la correccion deja la baranda %s: %s" % (nid, b["baranda"], b.get("cita")))
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
