# -*- coding: utf-8 -*-
"""_auditor_v97_ciega.py . INSTRUMENTO PROPIO DEL AUDITOR DE LA VUELTA 97.

Imprime CIEGO el material de los pares que yo elija: titulo, fuente y PASOS de
la madre y del hijo, mas el titulo_ratio de la bolsa. NO imprime ni la clase ni
la direccion ni la razon que el ejecutor escribio. El destape va en otro
fichero (_auditor_v97_destape.py) y se corre DESPUES de adjudicar.

  python docs/loop/_auditor_v97_ciega.py 41 55 62 ... > _auditor_v97_ciega.txt
"""
import io, json, os, sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
nodos = json.load(io.open(os.path.join(RAIZ, "dataset/metadata/master_graph.json"),
                          encoding="utf-8"))["nodos"]
alias = {a: k for k, v in nodos.items() for a in (v.get("ids_alias") or [])}


def res(x):
    seen = set()
    while x in alias and x not in seen:
        seen.add(x)
        x = alias[x]
    return x


def pasos(nid):
    n = nodos[res(nid)]
    out = []
    for k in ("pasos", "pasos_accionables", "acciones", "pasos_clave"):
        v = n.get(k)
        if isinstance(v, list) and v:
            for i, p in enumerate(v, 1):
                if isinstance(p, dict):
                    p = p.get("texto") or p.get("descripcion") or json.dumps(p, ensure_ascii=False)
                out.append("      %d. %s" % (i, p))
            return k, out
    return None, ["      (sin lista de pasos; claves: %s)" % sorted(n.keys())]


TRAMO = {1: ("docs/plan/DIFERENCIA_CONTRA_COLA.jsonl", 0)}
bolsa = [json.loads(l) for l in io.open(os.path.join(RAIZ, "docs/plan/DIFERENCIA_CONTRA_COLA.jsonl"),
                                        encoding="utf-8") if l.strip()]

for arg in sys.argv[1:]:
    i = int(arg)
    r = bolsa[i - 1]
    print("=" * 100)
    print("PAR %d  (dominio %s, titulo_ratio %.1f, contencion %s)"
          % (i, r["dominio"], r["titulo_ratio"] or 0.0, r.get("contencion")))
    print("=" * 100)
    m, h = res(r["madre"]), res(r["hijo"])
    print("  PASO CASADO DEL BARRIDO: paso %s de la madre" % r.get("paso"))
    print("      texto: %s" % r.get("texto_paso"))
    print()
    for rol, nid in (("MADRE (etiquetada asi por el barrido)", m),
                     ("HIJO  (etiquetado asi por el barrido)", h)):
        n = nodos[nid]
        print("  %s: %s" % (rol, nid))
        print("      titulo : %s" % n.get("titulo_concepto"))
        print("      fuente : %s" % n.get("fuente"))
        print("      que_es : %s" % (n.get("que_es") or n.get("descripcion") or "")[:400])
        k, ps = pasos(nid)
        print("      PASOS (%s):" % k)
        for p in ps:
            print(p)
        print()
