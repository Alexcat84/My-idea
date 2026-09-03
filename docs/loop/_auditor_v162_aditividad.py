# Auditor v162: aditividad del registro entre el commit de apertura y HEAD.
import json, subprocess, sys, collections
def leer(ref, path):
    out = subprocess.run(['git','show','%s:%s'%(ref,path)],capture_output=True)
    return [json.loads(l) for l in out.stdout.decode('utf-8').splitlines() if l.strip()]
P='docs/plan/REGISTRO_DE_CITAS_OPC05.jsonl'
A=leer('f7f52f91',P); B=leer('HEAD',P)
print('filas apertura %d -> cierre %d' % (len(A),len(B)))
ka=lambda r: r['cita'].split(',')[0]
da={ka(r):r for r in A}; db={ka(r):r for r in B}
print('pares desaparecidos: %d' % len(set(da)-set(db)))
print('pares nuevos: %d' % len(set(db)-set(da)))
esq=set(tuple(sorted(r.keys())) for r in B)
print('esquemas distintos en el cierre: %d' % len(esq))
print('mismo esquema que la apertura: %s' % (esq==set(tuple(sorted(r.keys())) for r in A)))
movidas=[k for k in da if k in db and da[k]['clase']!=db[k]['clase']]
print('CLASES MOVIDAS: %d %s' % (len(movidas), movidas))
aA=sum(1 for r in A if r['clase']=='A'); aB=sum(1 for r in B if r['clase']=='A')
print('clase A apertura %d cierre %d' % (aA,aB))
citas=[k for k in da if k in db and da[k]['cita']!=db[k]['cita']]
print('CITAS CAMBIADAS: %d %s' % (len(citas),citas))
via=[k for k in da if k in db and da[k]['via']!=db[k]['via']]
print('VIA CAMBIADA: %d' % len(via))
rotas=[k for k in da if k in db and not db[k]['razon'].startswith(da[k]['razon'])]
print('RAZONES CON PREFIJO ROTO (el texto viejo ya no es prefijo del nuevo): %d %s' % (len(rotas),rotas))
ampl=[k for k in da if k in db and db[k]['razon']!=da[k]['razon']]
print('RAZONES AMPLIADAS: %d -> %s' % (len(ampl), ', '.join(sorted(x.replace('LD-OPC05-','') for x in ampl))))
# orden de las filas
print('ORDEN DE LAS FILAS IDENTICO: %s' % ([ka(r) for r in A]==[ka(r) for r in B]))
