# Auditor v162: la nomina de verificar_mutaciones_viejas.py contra los arneses que existen.
import re, os, subprocess
RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
src = open(os.path.join(RAIZ,'scripts','loop','verificar_mutaciones_viejas.py'),encoding='utf-8').read()
i = src.index('VIEJAS = [') if 'VIEJAS = [' in src else src.index('[\n    ("vuelta133')
# la nomina son las tuplas ("fichero.py", bool)
nomina = re.findall(r'\("(vuelta\d+[^"]*\.py)",\s*(?:True|False)\)', src)
nomina = sorted(set(nomina))
print('NOMINA DE LA BATERIA: %d' % len(nomina))
d = os.path.join(RAIZ,'scripts','loop')
arneses = sorted(f for f in os.listdir(d) if re.match(r'vuelta\d+.*mutacion', f) and f.endswith('.py'))
print('ARNESES DE MUTACION EN scripts/loop: %d' % len(arneses))
def vuelta(f):
    return int(re.match(r'vuelta(\d+)', f).group(1))
fuera = [f for f in arneses if f not in nomina]
print('ARNESES DE MUTACION FUERA DE LA NOMINA: %d' % len(fuera))
ult = max(vuelta(f) for f in nomina)
print('ULTIMA VUELTA REPRESENTADA EN LA NOMINA: %d' % ult)
post = [f for f in fuera if vuelta(f) > ult]
print('DE ESOS, NACIDOS DESPUES DE LA ULTIMA VUELTA DE LA NOMINA: %d' % len(post))
for f in post: print('   vuelta %-4d %s' % (vuelta(f), f))
pre = [f for f in fuera if vuelta(f) <= ult]
print('Y NACIDOS ANTES O EN ESA VUELTA Y AUN ASI FUERA: %d' % len(pre))
for f in pre: print('   vuelta %-4d %s' % (vuelta(f), f))
