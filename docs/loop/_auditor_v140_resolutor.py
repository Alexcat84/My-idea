import json, os, glob
D='dataset/nodos'
nodos={}
for f in glob.glob(os.path.join(D,'*.json')):
    d=json.load(open(f,encoding='utf-8'))
    nid=d.get('node_id') or os.path.basename(f)[:-5]
    nodos[nid]=d
alias={}
for n,d in nodos.items():
    for a in (d.get('ids_alias') or []):
        alias[a]=n
def res(x, seen=None):
    seen=seen or set()
    while x in alias and x not in seen:
        seen.add(x); x=alias[x]
    return x
sig=set(); prev=set()
for n,d in nodos.items():
    rn=res(n)
    for x in (d.get('nodos_siguientes') or []): sig.add((rn,res(x)))
    for x in (d.get('nodos_previos') or []): prev.add((res(x),rn))
def vivo(x):
    d=nodos.get(x)
    return d is not None and not d.get('deprecado')
def chk(a,b,label=''):
    ra,rb=res(a),res(b)
    print("%-14s %s -> %s | resueltos: %s -> %s | vivos %s/%s | IDA sig=%s prev=%s | VUELTA sig=%s prev=%s"%(
        label,a,b,ra,rb,vivo(ra),vivo(rb),(ra,rb) in sig,(ra,rb) in prev,(rb,ra) in sig,(rb,ra) in prev))
    return (ra,rb)
print("### OP-M-01-ESLABONES")
chk('sistema_stage_gate','sistema_gates_go_kill','LD-56')
chk('sistema_gates_go_kill','asignacion_recursos_en_gates','LD-57')
print("### OP-E-04")
pares=[('gestion_portafolio_dos_niveles','estructura_gates','LD-35'),
('requisitos_gates_con_dientes','portfolio_management','LD-40'),
('requisitos_gates_con_dientes','revision_portafolio_periodica','LD-42'),
('requisitos_gates_con_dientes','gestion_portafolio_foco','LD-45'),
('portfolio_management','gates_go_kill_decision_points','LD-48'),
('gestion_portafolio_formal','gates_go_kill_decision_points','LD-49'),
('gestion_portafolio_dos_niveles','gates_go_kill_decision_points','LD-51'),
('gestion_portafolio_foco','gates_go_kill_decision_points','LD-53'),
('decision_factory_mentality','gates_go_kill_decision_points','LD-55')]
rs=[]
for a,b,l in pares: rs.append(chk(a,b,l))
print("pares dirigidos distintos tras resolver:", len(set(rs)), "de", len(rs))
print("### OP-E-05")
chk('requisitos_gates_con_dientes','gestion_portafolio_formal','LD-41')
chk('requisitos_gates_con_dientes','gestion_portafolio_dos_niveles','LD-43')
print("### OP-M-03-ENLACES")
chk('pivotar_o_perseverar','pivote_estrategico','a')
chk('pivote_o_proceder','pivote_estrategico','b')
print("### OP-M-01-SEXTO")
chk('gestion_de_portafolio_gates_go_kill','sistema_gates_go_kill','x')
