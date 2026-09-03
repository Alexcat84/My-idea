# Aditividad del registro entre la apertura de la vuelta 161 y HEAD, medida por mi.
import json, subprocess
def leer(ref):
    out = subprocess.run(['git','show','%s:docs/plan/REGISTRO_DE_CITAS_OPC05.jsonl'%ref],
                         capture_output=True)
    return [json.loads(l) for l in out.stdout.decode('utf-8').splitlines() if l.strip()]
A = leer('d3482b11'); B = leer('HEAD')
ka = {r['cita'].split(',')[0].strip(): r for r in A}
kb = {r['cita'].split(',')[0].strip(): r for r in B}
print('filas antes %d  filas ahora %d' % (len(A), len(B)))
print('pares desaparecidos: %d  pares nuevos: %d' % (len(set(ka)-set(kb)), len(set(kb)-set(ka))))
esq_a = set(tuple(sorted(r.keys())) for r in A); esq_b = set(tuple(sorted(r.keys())) for r in B)
print('esquemas antes %d  ahora %d  identicos: %s' % (len(esq_a), len(esq_b), esq_a==esq_b))
movidas = [(k, ka[k]['clase'], kb[k]['clase']) for k in ka if k in kb and ka[k]['clase']!=kb[k]['clase']]
print('CLASES MOVIDAS: %d %s' % (len(movidas), movidas))
prefijo_roto = [k for k in ka if k in kb and not kb[k]['razon'].startswith(ka[k]['razon'])]
print('RAZONES CON PREFIJO ROTO: %d %s' % (len(prefijo_roto), prefijo_roto[:5]))
ampliadas = [k for k in ka if k in kb and len(kb[k]['razon'])>len(ka[k]['razon'])]
print('RAZONES AMPLIADAS: %d' % len(ampliadas))
print('   nomina: %s' % ', '.join(sorted(x.replace('LD-OPC05-','') for x in ampliadas)))
citas_cambiadas = [k for k in ka if k in kb and ka[k]['cita']!=kb[k]['cita']]
print('CITAS CAMBIADAS: %d %s' % (len(citas_cambiadas), citas_cambiadas[:6]))
pares_movidos = [k for k in ka if k in kb and ka[k]['par']!=kb[k]['par']]
print('PARES MOVIDOS: %d' % len(pares_movidos))
a_A = [k for k in kb if kb[k]['clase']=='A']
print('CLASES QUE SE MUEVEN A A: %d' % len(a_A))
