import json, os, subprocess
exec(open(os.path.join(os.path.dirname(os.path.abspath(__file__)),"_auditor_v127_historia.py")).read().split("refs=sys.argv")[0])
a = en("cbc6ce51"); b = en("WORK")
print("baseline %d, hoy %d" % (len(a), len(b)))
print("DESAPARECIDAS desde el baseline (%d):" % len(a-b))
for p in sorted(a-b): print("   %s -> %s" % p)
print("NUEVAS desde el baseline (%d):" % len(b-a))
for p in sorted(b-a): print("   %s -> %s" % p)
