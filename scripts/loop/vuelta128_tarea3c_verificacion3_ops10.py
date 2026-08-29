# -*- coding: utf-8 -*-
"""vuelta128_tarea3c_verificacion3_ops10.py . MEDICION DE LA VERIFICACION 3
DE OP-S-10, que nadie habia medido (TAREA 3.c de la vuelta 128): "los items
numerados del FDD (Item 8, 19, 23) quedan dentro de la condicion de pais, no
fuera".

QUE HACE. Sobre el grafo de HOY, recorre los 31 ids de la nomina de OP-S-10
y busca, en TODOS los campos de texto del nodo (titulo_concepto,
resumen_teorico, pasos_accionables, entregable_esperado,
condiciones_activacion), menciones literales a "Item 8", "Item 19" o
"Item 23" (insensible a mayusculas). Para cada nodo que mencione alguno,
comprueba si el nodo queda CUBIERTO por una condicion de pais en
condiciones_activacion (misma deteccion de nombra_pais que el resto de la
operacion: "estados unidos", "ee. uu", "eeuu", "ee.uu").

NO cierra la operacion, NO toca ningun nodo: solo mide y publica.

Uso:
  python scripts/loop/vuelta128_tarea3c_verificacion3_ops10.py
"""
import json
import os
import re

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

ITEMS = ["item 8", "item 19", "item 23"]


def nombra_pais(txt):
    t = (txt or "").lower()
    return "estados unidos" in t or "ee. uu" in t or "eeuu" in t or "ee.uu" in t


def campos_texto(n):
    partes = [n.get("titulo_concepto") or "", n.get("resumen_teorico") or "",
              n.get("entregable_esperado") or ""]
    partes.extend(n.get("pasos_accionables") or [])
    partes.extend(n.get("condiciones_activacion") or [])
    return partes


def main():
    ops = [json.loads(l) for l in open(os.path.join(RAIZ, "docs", "plan", "OPERACIONES.jsonl"), encoding="utf-8") if l.strip()]
    op = [o for o in ops if o.get("id_op") == "OP-S-10"][0]
    nomina = op["nodos"]
    hoy = json.load(open(os.path.join(RAIZ, "dataset", "metadata", "master_graph.json"), encoding="utf-8"))["nodos"]

    print("nomina OP-S-10: %d ids" % len(nomina))
    encontrados = []
    for nid in sorted(nomina):
        n = hoy.get(nid)
        if n is None:
            print("  %-52s NO EXISTE EN EL GRAFO DE HOY" % nid)
            continue
        texto = " || ".join(campos_texto(n)).lower()
        items_hallados = [it for it in ITEMS if it in texto]
        if not items_hallados:
            continue
        cubierto = any(nombra_pais(c) for c in (n.get("condiciones_activacion") or []))
        encontrados.append((nid, items_hallados, cubierto, n.get("deprecado", False)))

    print()
    print("NODOS DE LA NOMINA QUE NOMBRAN Item 8, Item 19 o Item 23 EN ALGUN CAMPO: %d" % len(encontrados))
    fuera = []
    for nid, items_hallados, cubierto, deprecado in encontrados:
        estado = "DEPRECADO" if deprecado else ("CUBIERTO por condicion de pais" if cubierto else "NO CUBIERTO")
        print("  %-52s %-40s %s" % (nid, ",".join(items_hallados), estado))
        if not deprecado and not cubierto:
            fuera.append(nid)

    print()
    if fuera:
        print("VERIFICACION 3 EN ROJO: %d nodo(s) vivo(s) nombran un item del FDD FUERA de la condicion de pais: %s"
              % (len(fuera), fuera))
    else:
        print("VERIFICACION 3 EN VERDE: todo nodo vivo de la nomina que nombra Item 8/19/23 queda cubierto por la "
              "condicion de pais.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
