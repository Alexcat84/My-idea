# AUDITOR VUELTA 160: aditividad del registro contra el commit del acta 159.
import json, subprocess, collections
def leer(ref):
    t = subprocess.run(["git","show",f"{ref}:docs/plan/REGISTRO_DE_CITAS_OPC05.jsonl"],
                       capture_output=True, text=True, encoding="utf-8").stdout
    return {tuple(json.loads(l)["par"]): json.loads(l) for l in t.splitlines() if l.strip()}
A = leer("13cf21be"); B = leer("HEAD")
print("CIFRA filas ANTES:", len(A), " DESPUES:", len(B))
print("CIFRA pares desaparecidos:", len(set(A)-set(B)))
print("CIFRA pares nuevos:", len(set(B)-set(A)))
ka = set(); kb = set()
for v in A.values(): ka |= set(v)
for v in B.values(): kb |= set(v)
print("ESQUEMA identico:", sorted(ka)==sorted(kb), sorted(kb))
movidas = [(p, A[p]["clase"], B[p]["clase"]) for p in A if p in B and A[p]["clase"]!=B[p]["clase"]]
print("CIFRA clases movidas:", len(movidas))
for p,x,y in movidas:
    print(f"   {B[p]['cita'].split(',')[0]:<16} {x} -> {y}   {p[0]} <-> {p[1]}")
print("CIFRA que se mueven a A:", len([1 for _,_,y in movidas if y=="A"]))
rotos = [p for p in A if p in B and not B[p]["razon"].startswith(A[p]["razon"])]
ampl  = [p for p in A if p in B and B[p]["razon"]!=A[p]["razon"]]
print("CIFRA razones ampliadas:", len(ampl), " de ellas con PREFIJO ROTO:", len(rotos))
for p in rotos[:5]: print("   ROTO:", B[p]["cita"][:50])
citas = [p for p in A if p in B and A[p]["cita"]!=B[p]["cita"]]
print("CIFRA citas cambiadas:", len(citas))
