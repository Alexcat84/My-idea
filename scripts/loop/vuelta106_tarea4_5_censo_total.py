import json, io, re
CORREC_RE = re.compile(r'^correccion_v(\d+)$')
def cargar(ruta):
    with io.open(ruta, encoding='utf-8') as f:
        return [json.loads(l) for l in f if l.strip()]
def correcciones_ordenadas(fila):
    claves = [(int(m.group(1)), k) for k in fila for m in [CORREC_RE.match(k)] if m]
    claves.sort()
    return [fila[k] for _, k in claves]
def valor_efectivo(fila, campo):
    valor = fila.get(campo)
    for c in correcciones_ordenadas(fila):
        if c.get('campo_corregido') == campo:
            valor = c.get('valor_nuevo')
    return valor
tramos = ['docs/plan/OP_E_03_LECTURA_TRAMO1_V96.jsonl','docs/plan/OP_E_03_LECTURA_TRAMO2_V97.jsonl','docs/plan/OP_E_03_LECTURA_TRAMO3_V98.jsonl','docs/plan/OP_E_03_LECTURA_TRAMO4_V99.jsonl']
censo = {json.loads(l)['puesto_tramo']: json.loads(l) for l in open('docs/loop/CENSO_RELECTURAS_OP_E_03.jsonl', encoding='utf-8')}
total_resuelta=0
sin_tocar=[]
for ruta in tramos:
    for f in cargar(ruta):
        p=f['puesto_tramo']
        dir_ef = valor_efectivo(f,'direccion_leida')
        if not dir_ef: continue
        total_resuelta+=1
        c=censo.get(p)
        releido = c['veces_releido'] if c else None
        tiene_corr = len(correcciones_ordenadas(f))>0
        if releido==0 and not tiene_corr:
            sin_tocar.append(p)
print('TOTAL RESUELTA (todos los tramos):', total_resuelta)
print('SIN relectura NI correccion (todos los tramos), antes de la TAREA 4:', len(sin_tocar), sin_tocar)
