# -*- coding: utf-8 -*-
"""Criba LEXICA de solo lectura para el diagnostico de saneamiento (mandato del fundador, 26 sep 2026).
No decide nada: marca candidatos para que los agentes los lean. Sirve para dimensionar y para
medir despues cuanto se le escapa (muestra ciega de los no marcados).
Uso: python criba_lexica.py <repo_my_idea> <forja> <salida.json>"""
import collections
import glob
import io
import json
import os
import re
import sys

REPO, FORJA, SALIDA = sys.argv[1], sys.argv[2], sys.argv[3]

PAISES = {
    'EEUU': r'EE\.?\s?UU\.?|Estados Unidos|estadounidense|norteamerican|\bUSA\b|\bU\.S\.|\bUS\b(?=[\s,.)])|federal(?:es)?\b|IRS\b|OSHA\b|FDA\b|EPA\b|FTC\b|SEC\b|\bSBA\b|NIOSH|USPTO|\bCPSC\b|\bEEOC\b|\bDOL\b|\bNLRB\b|\bUSDA\b|Delaware|California|Texas|Nueva York|New York',
    'Mexico': r'M[eé]xico|mexican|\bSAT\b|IMSS|PROFECO|COFEPRIS|STPS\b|SEMARNAT',
    'Espana': r'Espa[nñ]a|español(?:a|es)? (?:de )?ley|\bAEAT\b|Seguridad Social espa',
    'UE': r'Uni[oó]n Europea|\bUE\b|\bEU\b|europe[oa] (?:directiva|reglamento)|\bRGPD\b|\bGDPR\b|\bREACH\b|marcado CE',
    'Reino_Unido': r'Reino Unido|brit[aá]nic|\bUK\b|\bHSE\b',
    'Canada': r'Canad[aá]|canadiense',
    'Colombia': r'Colombia|colombian|\bDIAN\b',
    'Argentina': r'Argentina|argentin|\bAFIP\b',
    'Chile': r'\bChile\b|chilen|\bSII\b',
    'Peru': r'Per[uú]\b|peruan|SUNAT',
    'China': r'\bChina\b|chin[oa]s?\b',
    'Japon': r'Jap[oó]n|japon[eé]s',
    'Alemania': r'Alemania|alem[aá]n',
    'India': r'\bIndia\b',
    'Australia': r'Australia',
    'Brasil': r'Brasil|brasile',
}
MARCA_B = r'en tu (?:pa[ií]s|mercado|jurisdicci[oó]n)|equivalente (?:en|de) tu|autoridad equivalente|organismo equivalente|averigua (?:qu[eé]|cu[aá]l|el|la|los|las)[^.]{0,60}(?:tu pa[ií]s|tu mercado)|pregunta[^.]{0,40}tu mercado'
MARCA_C = r'(?:[Ss]i|[Ss]olo si)[^.]{0,80}(?:Estados Unidos|EE\.?\s?UU)'
VIGENCIA = {
    'norma': r'\bley(?:es)?\b|\bnorma(?:s|tiva)?\b|\breglamento|\bregulaci[oó]n|\bdecreto|\bISO\s?\d|\bNOM-|\bdirectiva\b|\bc[oó]digo (?:de|federal)|\bCFR\b|\bestatuto|\bobligatori',
    'plazo_legal': r'\b\d+\s*(?:d[ií]as|horas|meses|a[nñ]os|semanas)\b[^.]{0,60}(?:plazo|ley|legal|obliga|debes|reportar|notificar|antes de)|\bplazo (?:legal|de ley|m[aá]ximo)',
    'cifra_datada': r'\b(?:19[5-9]\d|20[0-3]\d)\b',
    'importe': r'US\$|\$\s?\d|\bUSD\b|\bd[oó]lares\b|\beuros?\b|\bpesos\b',
    'institucion': r'\b(?:[A-Z]{3,6})\b(?<!ISO)(?<!ONU)',
    'enlace': r'https?://|www\.|\.gov\b|\.org\b|\.com\b',
}


def texto_de(n, forja=False):
    campos = ['titulo', 'resumen_teorico', 'entregable_esperado'] if forja else ['titulo_concepto', 'resumen_teorico', 'entregable_esperado']
    partes = [str(n.get(c) or '') for c in campos]
    partes += [str(p) for p in (n.get('pasos_accionables') or [])]
    ca = n.get('condiciones_activacion') or []
    partes += ca if isinstance(ca, list) else [str(ca)]
    return '\n'.join(partes)


def condiciones_de(n):
    ca = n.get('condiciones_activacion') or []
    return ' '.join(ca) if isinstance(ca, list) else str(ca)


def criba(idn, n, mundo, forja=False):
    t = texto_de(n, forja)
    paises = sorted(p for p, rx in PAISES.items() if re.search(rx, t))
    vig = {k: sorted(set(m.group(0) for m in re.finditer(rx, t)))[:6] for k, rx in VIGENCIA.items()}
    vig = {k: v for k, v in vig.items() if v}
    if 'institucion' in vig:
        vig['institucion'] = [x for x in vig['institucion'] if x not in ('IA', 'KPI', 'CRM', 'ROI', 'SOP', 'FAQ', 'PDCA', 'DMAIC', 'SIPOC', 'FODA', 'SWOT', 'MVP', 'CEO', 'CFO', 'COO', 'CTO', 'RRHH', 'PYME', 'PYMES', 'SMART', 'OKR', 'OKRS', 'NPS', 'VOC', 'QFD', 'FMEA', 'AMEF', 'HACCP', 'SPC', 'TQM', 'JIT', 'ERP', 'CPA', 'LTV', 'CAC', 'API', 'URL', 'PDF', 'EBITDA', 'IVA', 'TIR', 'VAN', 'NDA', 'LLC', 'PVF', 'PCT', 'MRP', 'OEE', 'ABC', 'RACI', 'SLA', 'SEO', 'SEM', 'CPC', 'CTA', 'UX', 'UI', 'B2B', 'B2C', 'PYM', 'SKU', 'EPP', 'MSDS', 'SDS', 'GHS', 'LOTO')]
        if not vig['institucion']:
            del vig['institucion']
    cond = condiciones_de(n)
    return {'id': idn, 'mundo': mundo, 'paises': paises, 'vigencia': vig,
            'marca_B': bool(re.search(MARCA_B, t)), 'marca_C': bool(re.search(MARCA_C, t)),
            'marca_C_en_condicion': bool(re.search(MARCA_C, cond)),
            'corregido': bool(n.get('correcciones'))}


filas = []
for p in sorted(glob.glob(os.path.join(REPO, 'dataset', 'nodos', '*.json'))):
    n = json.load(io.open(p, encoding='utf-8'))
    if n.get('deprecado'):
        continue
    filas.append(criba(n['node_id'], n, n['dominio']))
for l in io.open(os.path.join(FORJA, 'dataset', 'nodos.jsonl'), encoding='utf-8'):
    if l.strip():
        n = json.loads(l)
        filas.append(criba(n['id'], n, 'mundo11', True))
for p in sorted(glob.glob(os.path.join(FORJA, 'cuarentena', 'marquet_turn_the_ship', '*.json'))):
    n = json.load(io.open(p, encoding='utf-8'))
    filas.append(criba(n.get('id') or os.path.basename(p)[:-5], n, 'mundo11_bandeja', True))
json.dump(filas, io.open(SALIDA, 'w', encoding='utf-8'), ensure_ascii=False)

por_mundo = collections.defaultdict(collections.Counter)
for f in filas:
    c = por_mundo[f['mundo']]
    c['nodos'] += 1
    if f['paises']:
        c['con_pais'] += 1
        if not f['marca_B'] and not f['marca_C']:
            c['pais_sin_marca_B_ni_C'] += 1
    for k in f['vigencia']:
        c['vig_' + k] += 1
    if f['vigencia'] or f['paises']:
        c['candidato_J'] += 1
tot = collections.Counter()
for m, c in sorted(por_mundo.items()):
    tot.update(c)
    print('%-18s %s' % (m, dict(c)))
print('%-18s %s' % ('TOTAL', dict(tot)))
pp = collections.Counter(p for f in filas for p in f['paises'])
print('por pais (nodos):', dict(pp.most_common()))
print('corregidos por fidelidad con pais:', sum(1 for f in filas if f['corregido'] and f['paises']))
