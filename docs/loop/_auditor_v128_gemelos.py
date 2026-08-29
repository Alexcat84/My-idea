# Auditor v128: compara los dos master_graph con el MISMO comparador del Gate 0.
import json, sys, pathlib
sys.path.insert(0, str(pathlib.Path("scripts")))
from run_phase1 import gemelos_divergentes
a = json.load(open(sys.argv[1], encoding="utf-8"))["nodos"]
b = json.load(open(sys.argv[2], encoding="utf-8"))["nodos"]
d = gemelos_divergentes(a, b)
print(f"DIVERGENTES: {len(d)}")
for k, v in list(d.items())[:5]:
    print(f"  {k} ({v})")
