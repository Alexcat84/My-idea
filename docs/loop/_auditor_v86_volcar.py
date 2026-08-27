# -*- coding: utf-8 -*-
"""AUDITOR, vuelta 86. Vuelca las 60 fichas (30 madres y 30 hijos) del tramo 11
desde dataset/nodos/, con los pares LEIDOS del fichero del filtro (ninguno
tecleado). Para la relectura ciega: NO imprime ninguna decision ni razon del
ejecutor.

  set PYTHONIOENCODING=utf-8
  python docs/loop/_auditor_v86_volcar.py A > docs/loop/_auditor_v86_volcado_a.txt
  python docs/loop/_auditor_v86_volcar.py B > docs/loop/_auditor_v86_volcado_b.txt
"""
import json
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
F86 = RAIZ / "docs" / "plan" / "PASO_NODO_CALIBRADO_FILTRADO_V86.jsonl"
NODOS = RAIZ / "dataset" / "nodos"


def filas(ruta):
    return [json.loads(l) for l in open(ruta, encoding="utf-8") if l.strip()]


def ficha(nid):
    p = NODOS / ("%s.json" % nid)
    if not p.exists():
        return None
    return json.load(open(p, encoding="utf-8"))


def pinta(rol, nid, marcar_paso=None):
    d = ficha(nid)
    print("  [%s] %s" % (rol, nid))
    if d is None:
        print("     (SIN FICHA)")
        return
    print("     titulo: %s" % d.get("titulo_concepto"))
    print("     dominio/fase: %s / %s" % (d.get("dominio"), d.get("fase_proyecto")))
    r = (d.get("resumen_teorico") or "").strip()
    print("     resumen: %s" % r)
    print("     pasos:")
    for i, p in enumerate(d.get("pasos_accionables") or [], 1):
        if isinstance(p, dict):
            txt = "%s | %s" % (p.get("titulo_paso"), p.get("descripcion_paso"))
        else:
            txt = str(p)
        marca = "  <<< EL PASO QUE LA UNIDAD TRAE" if marcar_paso == i else ""
        print("       %d. %s%s" % (i, txt, marca))
    print("     entregable: %s" % (d.get("entregable_esperado") or ""))
    print("     nodos_siguientes (%d): %s" % (len(d.get("nodos_siguientes") or []),
                                              d.get("nodos_siguientes")))
    print("     nodos_previos (%d): %s" % (len(d.get("nodos_previos") or []),
                                           d.get("nodos_previos")))


def main():
    mitad = sys.argv[1] if len(sys.argv) > 1 else "A"
    B = filas(F86)
    rango = range(95, 110) if mitad == "A" else range(110, 125)
    for i in rango:
        f = B[i]
        print("=" * 78)
        print("UNIDAD %d | %s -> %s | paso %s | dominio %s | titulo_ratio %s | contencion %s"
              % (i, f["madre"], f["hijo"], f["paso"], f["dominio"],
                 f.get("titulo_ratio"), f.get("contencion")))
        print("TEXTO DEL PASO QUE LA UNIDAD TRAE: %s" % f.get("texto_paso"))
        print("=" * 78)
        try:
            pinta("MADRE", f["madre"], marcar_paso=int(f["paso"]))
        except (TypeError, ValueError):
            pinta("MADRE", f["madre"])
        print()
        pinta("HIJO", f["hijo"])
        print()


if __name__ == "__main__":
    main()
