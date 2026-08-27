"""Auditor v81: vuelca los campos de lectura de un nodo (pasos primero)."""
import io, json, os, sys
RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import sys as _s
_s.stdout.reconfigure(encoding="utf-8")
def ruta(nid):
    for d, _, fs in os.walk(os.path.join(RAIZ, "dataset", "nodos")):
        if nid + ".json" in fs:
            return os.path.join(d, nid + ".json")
    return None
for nid in sys.argv[1:]:
    r = ruta(nid)
    if not r:
        print("NO EXISTE: %s" % nid); continue
    n = json.load(io.open(r, encoding="utf-8"))
    print("=" * 78)
    print("%s   [%s]" % (nid, n.get("dominio") or n.get("domain")))
    print("TITULO: %s" % (n.get("titulo_concepto") or n.get("titulo")))
    ps = n.get("pasos") or n.get("pasos_accionables") or []
    print("PASOS (%d):" % len(ps))
    for i, p in enumerate(ps, 1):
        print("  %d. %s" % (i, p if isinstance(p, str) else json.dumps(p, ensure_ascii=False)))
    for k in ("entregable_esperado", "resumen", "descripcion", "familia_de_ids", "acto", "racimo"):
        if n.get(k):
            v = n[k]
            print("%s: %s" % (k.upper(), v if isinstance(v, str) else json.dumps(v, ensure_ascii=False)))
    print("SIGUIENTES (%d): %s" % (len(n.get("nodos_siguientes") or []), n.get("nodos_siguientes")))
    print("PREVIOS (%d): %s" % (len(n.get("nodos_previos") or []), n.get("nodos_previos")))
