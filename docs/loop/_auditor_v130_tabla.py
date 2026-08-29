import glob, os, json, collections
viv=[json.load(open(p,encoding='utf-8')) for p in sorted(glob.glob('dataset/nodos/*.json'))]
viv=[d for d in viv if not (d.get('deprecated') or d.get('deprecado'))]
gr={(d.get('fuente') or '').split('|')[0].strip() for d in viv if (d.get('fuente') or '').strip()}
gr={g for g in gr if len(g)>18}
print('grafias largas usadas como sonda:', len(gr))
hits=collections.Counter()
for p in glob.glob('docs/**/*', recursive=True):
    if not os.path.isfile(p): continue
    q=p.replace(os.sep,'/')
    if 'OP_S_11_MAPEO_PROPUESTO' in q or 'SALIDA_V130_3B' in q or '_auditor_v130' in q: continue
    try: t=open(p,encoding='utf-8',errors='ignore').read()
    except Exception: continue
    n=sum(1 for g in gr if g in t)
    if n>=5: hits[q]=n
print('FICHEROS de docs/ con 5+ grafias literales (excluidos los nacidos hoy):')
for p,n in hits.most_common(15): print(f'  {n:3d}  {p}')
print('total:', len(hits))
