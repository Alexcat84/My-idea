# -*- coding: utf-8 -*-
"""Procesa el resultado de un bloque de lectura de la campania (solo la sesion escribe).

Uso: python procesar_bloque.py <W> <salida_workflow_lectura.output> <repo_fidelidad> <repo_correcciones> <bloque>

Escribe en <repo_fidelidad>/docs/fidelidad/campania/c2/:
  resultados/<lote>.json        el resultado final de cada lote (con node_id y paso)
  VEREDICTOS_CAMPANIA.jsonl     una linea por paso real (se reescribe entera con todos los lotes procesados)
  fichas/<bloque>.json          fichas de los no FIEL, con el pasaje literal sacado del libro por script
  bloques/<bloque>.json         recall, cuentas y comprobaciones del bloque
Y en <W>/c2/decision/<bloque>.json las correcciones candidatas por regla B y las excepciones.
"""
import glob
import io
import json
import os
import re
import sys
import unicodedata

W, SALIDA, RF, RC, BLOQUE = sys.argv[1:6]
C2 = W + '/c2'
BASE = RF + '/docs/fidelidad/campania/c2'
for d in ('resultados', 'fichas', 'bloques'):
    os.makedirs('%s/%s' % (BASE, d), exist_ok=True)
os.makedirs(C2 + '/decision', exist_ok=True)
RAYA, MEDIO = chr(0x2014), chr(0x2013)


def sin_rayas(s):
    return (s or '').replace(RAYA, '--').replace(MEDIO, '-')


def norm(s):
    s = unicodedata.normalize('NFKC', s or '')
    for a, b in ((chr(0x2019), "'"), (chr(0x2018), "'"), (chr(0x201c), '"'), (chr(0x201d), '"'), (RAYA, '--'), (MEDIO, '-'), (chr(0x2011), '-'), (chr(0x2010), '-')):
        s = s.replace(a, b)
    s = re.sub(r'(?<=[a-z\.])\d{1,2}(?= [A-Z])', '', s)
    return ' '.join(s.split()).lower()


libros = {}


def texto_libro(f):
    if f not in libros:
        libros[f] = io.open(f, encoding='utf-8', errors='replace').read().splitlines()
    return libros[f]


def rango(lineas):
    nums = [int(n) for n in re.findall(r'L(\d+)', lineas or '')]
    return (min(nums), max(nums)) if nums else None


o = json.load(io.open(SALIDA, encoding='utf-8'))
res = o['result'] if isinstance(o, dict) else o
fichas, decision, excepciones, stats = [], [], [], {'lotes': {}, 'errores': []}
for r in res:
    lote = r['lote']
    mapa = json.load(io.open('%s/claves/mapa_%s.json' % (C2, lote), encoding='utf-8'))
    reales = {i for i, m in mapa.items() if m['real']}
    final = {x['id']: x for x in r['final']}
    faltan = sorted(reales - set(final))
    if faltan:
        stats['errores'].append('%s: %d pasos reales sin veredicto: %s' % (lote, len(faltan), faltan[:5]))
    salida_lote = []
    for ident in sorted(final):
        if ident not in reales:
            continue
        m, x = mapa[ident], final[ident]
        nodo = json.load(io.open('%s/dataset/nodos/%s.json' % (RC, m['node_id']), encoding='utf-8'))
        actual = nodo['pasos_accionables'][m['paso'] - 1]
        reales_lote = json.load(io.open('%s/claves/reales_%s.json' % (C2, lote), encoding='utf-8'))
        leido = next((it for it in reales_lote if it['node_id'] == m['node_id'] and it['paso'] == m['paso']), {})
        ficheros = leido.get('ficheros', [])
        ya_corregido = leido.get('texto') is not None and leido.get('texto') != actual
        fila = dict(x, node_id=m['node_id'], paso=m['paso'], libro=m['libro'], texto_actual=actual, ficheros=ficheros,
                    texto_leido=leido.get('texto'), ya_corregido_antes=ya_corregido)
        salida_lote.append(fila)
        if x['veredicto'] == 'FIEL':
            continue
        # pasaje literal por script, en el primer fichero del libro que contenga la frase clave
        pasaje, fichero_ok, literal = '', ficheros[0] if ficheros else '', False
        trozos = [t.strip(' "') for t in re.split(r'\.\.\.|' + chr(0x2026) + r'| / ', re.sub(r'\(L\d+[^)]*\)', ' ', x.get('frase_clave', ''))) if len(t.strip(' "')) > 8]
        for f in ficheros:
            t = texto_libro(f)
            if trozos and all(norm(tr) in norm('\n'.join(t)) for tr in trozos):
                fichero_ok, literal = f, True
                break
        rg = rango(x.get('lineas'))
        if rg and fichero_ok:
            t = texto_libro(fichero_ok)
            if rg[1] <= len(t):
                pasaje = '\n'.join('L%d: %s' % (k, sin_rayas(t[k - 1])) for k in range(rg[0], rg[1] + 1) if t[k - 1].strip())
        if not literal:
            stats['errores'].append('%s: frase clave no literal en el libro' % ident)
        ficha = {'id': ident, 'lote': lote, 'node_id': m['node_id'], 'fichero_nodo': 'dataset/nodos/%s.json' % m['node_id'],
                 'paso_desde_0': m['paso'] - 1, 'paso_desde_1': m['paso'], 'libro': m['libro'], 'fichero_libro': fichero_ok,
                 'veredicto': x['veredicto'], 'decidido_por': x.get('decidido_por', ''), 'lector': x.get('lector', ''),
                 'verificador': x.get('verificador', ''), 'texto_actual': sin_rayas(actual), 'lineas': x.get('lineas', ''),
                 'frase_clave': sin_rayas(x.get('frase_clave', '')), 'frase_literal_en_libro': literal,
                 'dato': sin_rayas(x.get('dato', '')), 'tipo_anadido': x.get('tipo_anadido', ''),
                 'texto_fiel': sin_rayas(x.get('texto_fiel', '')), 'texto_sugerencia': sin_rayas(x.get('texto_sugerencia', '')),
                 'razon': sin_rayas(x.get('razon', '')), 'pasaje': pasaje}
        fichas.append(ficha)
        # REGLA B
        if x['veredicto'] == 'OPERATIVO':
            continue
        if ya_corregido:
            # el paso ya lo cambio una tanda anterior (t1 a t3): el veredicto es sobre el texto viejo
            ficha['nota'] = 'ya corregido antes de esta lectura; el veredicto es sobre el texto viejo'
            continue
        nuevo, regla = '', ''
        if x['veredicto'] == 'CONTRARIO':
            nuevo, regla = ficha['texto_fiel'], 'regla B, CONTRARIO: version fiel escrita por el verificador (o el arbitro si hubo desacuerdo), con su cita'
        elif x.get('tipo_anadido') == 'LEGAL_CIFRA':
            nuevo, regla = ficha['texto_fiel'], 'regla B, ANADIDO de cifra, plazo, norma o materia legal: se quita o se reemplaza por lo que dice el libro'
        elif x.get('tipo_anadido') == 'PRACTICO':
            nuevo, regla = ficha['texto_sugerencia'], 'regla B, ANADIDO practico: se reescribe como sugerencia de My Idea, sin atribuirlo al autor'
            if not nuevo.startswith('Sugerencia de My Idea: '):
                nuevo = ''
        motivo = ''
        if not nuevo:
            motivo = 'la regla no tiene texto limpio que aplicar (veredicto %s, tipo %r)' % (x['veredicto'], x.get('tipo_anadido'))
        elif not literal:
            motivo = 'la frase clave de la cita no esta literal en el libro'
        elif any(c in nuevo for c in (RAYA, MEDIO)):
            motivo = 'el texto propuesto trae guiones largos o medios'
        if motivo:
            excepciones.append({'id': ident, 'node_id': m['node_id'], 'paso': m['paso'], 'veredicto': x['veredicto'],
                                'texto_actual': actual, 'motivo': motivo, 'ficha': ficha})
            continue
        rel = fichero_ok.replace('\\', '/')
        rel = rel.split('Documents/', 1)[1] if 'Documents/' in rel else rel
        decision.append({'ficha_id': ident, 'node_id': m['node_id'], 'campo': 'pasos_accionables', 'indice': m['paso'] - 1,
                         'veredicto': x['veredicto'], 'texto_anterior': actual, 'texto_nuevo': nuevo,
                         'cita': {'libro': m['libro'], 'fichero': rel, 'lineas': x.get('lineas', ''), 'frase': ficha['frase_clave']},
                         'decision': 'Mandato del fundador, %s. %s' % (regla, ficha['razon']),
                         'auditoria': 'rama fidelidad-total, docs/fidelidad/campania/c2/fichas/%s.json, ficha %s' % (BLOQUE, ident),
                         'dato': ficha['dato']})
    json.dump(salida_lote, io.open('%s/resultados/%s.json' % (BASE, lote), 'w', encoding='utf-8', newline='\n'), ensure_ascii=False, indent=1)
    h = r['historial'][-1]
    stats['lotes'][lote] = {'cuenta': r['cuenta'], 'lecturas': len(r['historial']), 'trampas_lector': h['recall'],
                            'trampas_verificador': r['recallVerificador'], 'desacuerdos': r['desacuerdos'],
                            'fiel_muestreados': r['fielMuestreados'], 'fiel_cambiados': r['fielCambiados']}
# registro por paso, con todos los lotes procesados hasta ahora
filas = []
for f in sorted(glob.glob(BASE + '/resultados/*.json')):
    for x in json.load(io.open(f, encoding='utf-8')):
        filas.append({'id': x['id'], 'node_id': x['node_id'], 'paso': x['paso'], 'libro': x['libro'], 'veredicto': x['veredicto'],
                      'lineas': x.get('lineas', ''), 'frase_clave': sin_rayas(x.get('frase_clave', '')), 'decidido_por': x.get('decidido_por', '')})
with io.open(BASE + '/VEREDICTOS_CAMPANIA.jsonl', 'w', encoding='utf-8', newline='\n') as fh:
    for x in filas:
        fh.write(json.dumps(x, ensure_ascii=False) + '\n')
orden = {'CONTRARIO': 0, 'ANADIDO': 1, 'OPERATIVO': 2}
fichas.sort(key=lambda f: (orden[f['veredicto']], f['id']))
decision.sort(key=lambda d: (orden[d['veredicto']], d['ficha_id']))
json.dump(fichas, io.open('%s/fichas/%s.json' % (BASE, BLOQUE), 'w', encoding='utf-8', newline='\n'), ensure_ascii=False, indent=1)
json.dump(stats, io.open('%s/bloques/%s.json' % (BASE, BLOQUE), 'w', encoding='utf-8', newline='\n'), ensure_ascii=False, indent=1)
json.dump({'correcciones': decision, 'excepciones': excepciones}, io.open('%s/decision/%s.json' % (C2, BLOQUE), 'w', encoding='utf-8', newline='\n'), ensure_ascii=False, indent=1)
cuenta = {}
for f in filas:
    cuenta[f['veredicto']] = cuenta.get(f['veredicto'], 0) + 1
det = sum(v['trampas_lector']['detectadas'] for v in stats['lotes'].values())
tot = sum(v['trampas_lector']['total'] for v in stats['lotes'].values())
print('bloque %s: %d lotes | pasos acumulados %d %s | trampas del lector %d/%d | correcciones candidatas %d (CONTRARIO %d) | excepciones %d | errores %d'
      % (BLOQUE, len(stats['lotes']), len(filas), cuenta, det, tot, len(decision), sum(1 for d in decision if d['veredicto'] == 'CONTRARIO'), len(excepciones), len(stats['errores'])))
for e in stats['errores'][:20]:
    print('  ', e)
