# -*- coding: utf-8 -*-
"""AUDITOR v146: censo propio, con ast, de pares_exceptuados_de en scripts/."""
import ast, io, os
NOMBRE = "pares_exceptuados_de"
apar, llam = set(), set()
n_llamadas = 0
detalle = []
for raiz, _d, fs in os.walk("scripts"):
    for f in sorted(fs):
        if not f.endswith(".py"): continue
        r = os.path.join(raiz, f).replace("\\", "/")
        try: txt = io.open(r, encoding="utf-8").read()
        except UnicodeDecodeError: txt = io.open(r, encoding="utf-8", errors="replace").read()
        if NOMBRE not in txt: continue
        apar.add(r)
        try: arbol = ast.parse(txt)
        except SyntaxError: detalle.append((r, 0, "NO PARSEA")); continue
        for nodo in ast.walk(arbol):
            if isinstance(nodo, ast.Call):
                fn = nodo.func
                nom = getattr(fn, "id", None) or getattr(fn, "attr", None)
                if nom == NOMBRE:
                    llam.add(r); n_llamadas += 1
                    detalle.append((r, nodo.lineno, "LLAMADA"))
            elif isinstance(nodo, (ast.FunctionDef, ast.AsyncFunctionDef)) and nodo.name == NOMBRE:
                detalle.append((r, nodo.lineno, "DEFINICION"))
for r, l, c in sorted(detalle):
    print("  %-52s %5s  %s" % (r, l, c))
print()
print("FICHEROS CON APARICION DEL NOMBRE : %d" % len(apar))
print("FICHEROS CON LLAMADA DE VERDAD    : %d" % len(llam))
print("LLAMADAS EN TOTAL                 : %d" % n_llamadas)
print("SOLO MENCION                      : %d %s" % (len(apar - llam), sorted(apar - llam)))
