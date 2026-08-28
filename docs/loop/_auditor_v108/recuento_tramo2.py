import json, sys, os
sys.path.insert(0, os.path.join('scripts','loop'))
import contar_cierre_efectivo as cce
f='docs/plan/OP_E_03_LECTURA_TRAMO2_V97.jsonl'
d,fallos = cce.cifras([os.path.join(os.path.dirname(os.path.dirname(os.path.abspath('scripts'))),'')] ) if False else (None,None)
# recuento propio, aplicando correccion_vNN en orden ascendente sobre direccion_leida
vivas=[]; anuladas=[]
for ln in open(f,encoding='utf-8'):
    ln=ln.strip()
    if not ln: continue
    o=json.loads(ln)
    dirl=o.get('direccion_leida')
    for k in sorted([k for k in o if k.startswith('correccion_v')], key=lambda x:int(x.split('_v')[1])):
        c=o[k]
        if c.get('campo_corregido')=='direccion_leida':
            dirl=c.get('valor_nuevo')
    if dirl: vivas.append(o['puesto_tramo'])
    else: anuladas.append(o['puesto_tramo'])
print('tramo2 filas:', len(vivas)+len(anuladas))
print('RESUELTA vivas:', len(vivas))
print('anuladas / NO RESUELTA:', len(anuladas))
print('lista vivas:', vivas)
