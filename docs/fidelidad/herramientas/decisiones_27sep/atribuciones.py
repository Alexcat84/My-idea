# -*- coding: utf-8 -*-
"""Punto 2 (27 sep): textos vivos del catalogo que atribuyen un paso o un nodo a su autor o a su libro.
Uso: python atribuciones.py <repo> <salida.tsv>. Busca en los nodos vivos 'el libro', 'el autor', 'segun X'
y los apellidos de los autores tomados del campo fuente."""
import glob, io, json, re, sys

R, OUT = sys.argv[1:3]
nodos = {}
fuentes = set()
for f in glob.glob(R + '/dataset/nodos/*.json'):
    d = json.load(io.open(f, encoding='utf-8'))
    if d.get('deprecado') is True:
        continue
    nodos[f.replace('\\', '/')[len(R) + 1:]] = d
    fuentes.add(d.get('fuente') or '')
ap = set()
NO = {'unknown', 'guide', 'press', 'staff', 'team', 'edition', 'harvard', 'business', 'review', 'osha', 'dhl', 'ups'}
for s in fuentes:
    if ' - ' in s:
        for a in re.split(r'[;&]| and ', s.split(' - ', 1)[1]):
            w = a.strip().split(',')[0].strip().split(' ')[-1] if ',' not in a else a.strip().split(',')[0].strip()
            if len(w) >= 4 and w[0].isupper() and w.lower() not in NO:
                ap.add(w)
ap.discard('Primer')
ap |= {'Juran','Defeo','Esty','Winston','Siebert','Blank','Dorf','Deming','Cooper','Feld','Mendelson','Wasserman','Dekker','Hugos','Reason','Horowitz','Crosby','Berman','Tim Brown','Ries','Doorley','Snyder','Stackpole','Coleman','Weinberg','Braungart','McDonough','Osterwalder','Pigneur','Mollick','Wallas','Rackham','Lindstrom','Voss','Rushton','Croucher','DeMarco','Lister','Hubbard','Cullinane','Muller','Komisar','Out of the Crisis','Crossing the Chasm','Tragic Design','IDEO'}
ape = '|'.join(map(re.escape, sorted(ap)))
pat = re.compile(r'\b(el libro|del libro|al libro|los autores|el autor|la autora|del autor|seg[uú]n (?:el )?(?:libro|autor)|seg[uú]n [A-Z][a-z]+|(?:propuest|cread|desarrollad|acuñad|formulad)[oa]s? por|basad[oa] en el libro|en su libro|' + ape + r')\b')
filas = []
for f, d in sorted(nodos.items()):
    lines = io.open(R + '/' + f, encoding='utf-8').read().split('\n')
    for campo in ('titulo_concepto', 'resumen_teorico', 'pasos_accionables', 'entregable_esperado'):
        vals = d.get(campo)
        vals = vals if isinstance(vals, list) else [vals or '']
        for i, v in enumerate(vals):
            m = pat.search(v)
            if not m:
                continue
            clave = json.dumps(v[:50], ensure_ascii=False)[1:-1]
            ln = next((k + 1 for k, l in enumerate(lines) if clave in l), 0)
            filas.append((f, ln, campo + ('[%d]' % i if campo == 'pasos_accionables' else ''), m.group(0), v.replace('\t', ' ')))
with io.open(OUT, 'w', encoding='utf-8', newline='\n') as o:
    o.write('fichero\tlinea\tcampo\tcoincidencia\ttexto\n')
    for x in filas:
        o.write('%s\t%d\t%s\t%s\t%s\n' % x)
print(len(filas), 'textos;', len({x[0] for x in filas}), 'nodos; apellidos buscados', len(ap))
