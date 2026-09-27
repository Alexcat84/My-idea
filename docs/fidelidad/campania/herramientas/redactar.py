# -*- coding: utf-8 -*-
"""Redacta docs/fidelidad/campania/TRAMO1_SEGURIDAD_Y_SALUD.md a partir de las fichas y la comprobacion."""
import collections
import io
import json
import math
import sys

W, R = sys.argv[1], sys.argv[2]
F = json.load(io.open(W + '/fichas_tramo1.json', encoding='utf-8'))
C = json.load(io.open(W + '/comprobacion_tramo1.json', encoding='utf-8'))
RES = json.load(io.open(W + '/resultado_tramo1.json', encoding='utf-8'))


def wil(k, n):
    if not n:
        return '-'
    z = 1.96
    p = k / n
    d = 1 + z * z / n
    c = (p + z * z / (2 * n)) / d
    h = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / d
    return '%.1f%% [%.1f, %.1f]' % (100 * p, 100 * (c - h), 100 * (c + h))


def cota(n):
    z = 1.96
    d = 1 + z * z / n
    c = (z * z / (2 * n)) / d
    h = z * math.sqrt(z * z / (4 * n * n)) / d
    return 100 * (c + h)


tot = collections.Counter()
for c in C['cuenta'].values():
    tot.update(c)
N = sum(tot.values())
fm = sum(r['fielMuestreados'] for r in RES)
fd = sum(len(r['fielDiscutidos']) for r in RES)
nf = {x['id']: x['veredicto'] for r in RES for x in r['noFiel']}
fdn = sum(1 for r in RES for i in r['fielDiscutidos'] if i in nf)
des = sum(r['desacuerdos'] for r in RES)

L = []
A = L.append
A('CONTRARIOS: %d' % tot['CONTRARIO'])
A('ANADIDOS: %d' % tot['ANADIDO'])
A('FICHAS PARA DECISION DEL FUNDADOR: %d (todos los CONTRARIOS, ANADIDOS y OPERATIVOS, con DECISION_DEL_FUNDADOR vacio)' % len(F))
A('')
A('# FIDELIDAD TOTAL, TRAMO 1 (seguridad y salud): CALIBRACION DEL METODO DE ESPECIALISTAS')
A('')
A('Decision del fundador del 24 sep 2026: agentes especialistas por libro, verificados, con cobertura del 100 por ciento y cada hallazgo comprobado. Solo lectura sobre dataset/: nada se corrige aqui. Todo con claude-opus-5-5.')
A('')
A('## 1. Que se leyo')
A('')
A('Los 5 libros del tramo 1 que faltaban (Reason ya esta leido entero en el muestreo, rama muestreo-fidelidad): Dekker, SMALL_BUSINESS, OSHA3885, OSHA3886 y la guia de empaque de FedEx. **%d pasos de 179 nodos vivos, cada uno exactamente una vez**, comprobado por script contra docs/fidelidad/INVENTARIO_NODOS.jsonl y dataset/nodos.' % N)
A('')
A('## 2. El metodo, en tres capas mas un script')
A('')
A('1. **Lector especialista por lote** (8 lotes de 48 a 125 pasos): cuatro veredictos, con rango de lineas, frase clave literal y texto fiel. En cada lote iban escondidas 4 TRAMPAS (2 CONTRARIAS y 2 ANADIDAS sinteticas, escritas por otros agentes sobre pasajes reales), bajo ids opacos y barajados, sin marca. Regla: si el lector no las caza todas o se salta pasos, el lote se relee con otro lector.')
A('2. **Verificador ciego por lote**: reclasifica desde cero todo lo no FIEL mas uno de cada seis FIEL, sin ver el primer veredicto.')
A('3. **Arbitro por lote**: relee el libro en cada desacuerdo y decide.')
A('4. **Script** (no agente): cobertura, pasaje literal de cada ficha sacado del libro por su rango de lineas, y frase clave comprobada literal en el libro.')
A('')
A('El rastro completo esta en esta carpeta: lotes/ (lo que vio cada lector), trampas/ y claves/ (las trampas y el mapa de ids, que ningun lector vio), salidas/ (el fichero de cada lector, verificador y arbitro) y herramientas/.')
A('')
A('## 3. Lo medido')
A('')
A('| medida | resultado |')
A('|---|---|')
A('| trampas cazadas por los lectores | **32 de 32**, las 32 con su clase exacta, en la primera lectura; ningun lote tuvo que releerse |')
A('| trampas cazadas por los verificadores ciegos | **32 de 32** |')
A('| cobertura | %d de %d pasos, 0 repetidos, 0 sin veredicto |' % (N, N))
A('| FIEL muestreados y releidos a ciegas | %d; el verificador discutio %d y el arbitro dejo %d como OPERATIVO; **0 resultaron ANADIDO ni CONTRARIO** (cota superior al 95 por ciento de ANADIDO o CONTRARIO escondidos entre los FIEL: %.1f por ciento) |' % (fm, fd, fdn, cota(fm)))
A('| desacuerdos lector frente a verificador | %d, todos arbitrados releyendo el libro |' % des)
A('| citas | %d fichas con su pasaje sacado del libro por script; frases clave literales en el libro: %d de %d (la que falla, DK2-008, es literal en L2508 y L2626 salvo el arranque "it is now") |' % (len(F), len(F) - len(C['errores']), len(F)))
A('| coste | 29 agentes (5 de trampas y 24 de lectura, verificacion y arbitraje); 3,76 millones de tokens de subagente; unos 26 minutos de reloj |')
A('')
A('Limites, dichos: las trampas las escribe el mismo modelo que las caza, lo que puede inflar el recall; la frontera FIEL y OPERATIVO es blanda (%d de %d FIEL muestreados eran OPERATIVO), pero la frontera que importa, ANADIDO o CONTRARIO, no escondio ninguno en la muestra; un solo arbitro por desacuerdo.' % (fdn, fm))
A('')
A('## 4. Tasas por libro (Wilson al 95 por ciento, por paso)')
A('')
A('| libro | pasos | FIEL | OPERATIVO | ANADIDO | CONTRARIO |')
A('|---|---:|---|---|---|---|')
for lib, c in C['cuenta'].items():
    n = sum(c.values())
    A('| %s | %d | %s | %s | %s | %s |' % (lib, n, wil(c.get('FIEL', 0), n), wil(c.get('OPERATIVO', 0), n), wil(c.get('ANADIDO', 0), n), wil(c.get('CONTRARIO', 0), n)))
A('| **tramo 1 sin Reason** | %d | %s | %s | %s | %s |' % (N, wil(tot['FIEL'], N), wil(tot['OPERATIVO'], N), wil(tot['ANADIDO'], N), wil(tot['CONTRARIO'], N)))
A('')


def tabla(v, titulo):
    xs = [f for f in F if f['veredicto'] == v]
    A('## %s (%d)' % (titulo, len(xs)))
    A('')
    A('| id | nodo, paso | libro | dato | decidido por |')
    A('|---|---|---|---|---|')
    for f in xs:
        A('| %s | `%s` p%d | %s | %s | %s |' % (f['id'], f['node_id'], f['paso_desde_1'], f['libro'][:30], (f['dato'] or '').replace('|', '/')[:200], f['decidido_por']))
    A('')


tabla('CONTRARIO', '5. CONTRARIOS')
tabla('ANADIDO', '6. ANADIDOS')
A('## 7. FICHAS (todas: CONTRARIOS, ANADIDOS y OPERATIVOS)')
A('')
A('Formato fijo, una clave por linea. El PASAJE es el texto literal del libro en el rango citado, sacado por script (unica excepcion: la raya va como `--`). DECISION_DEL_FUNDADOR admite MANTENER, APLICAR_FIEL u OTRO.')
A('')
for f in F:
    A('### %s: %s, `%s` paso %d' % (f['id'], f['veredicto'], f['node_id'], f['paso_desde_1']))
    A('')
    A('```')
    for k in ['id', 'veredicto', 'decidido_por', 'node_id', 'fichero_nodo', 'paso_desde_0', 'paso_desde_1', 'libro', 'fichero_libro', 'lineas']:
        A('%s: %s' % (k.upper(), f[k]))
    A('TEXTO_ACTUAL: %s' % f['texto_actual'])
    A('FRASE_CLAVE: %s' % f['frase_clave'])
    if f['dato']:
        A('DATO: %s' % f['dato'])
    A('TEXTO_FIEL: %s' % (f['texto_fiel'] or '(mantener el actual)'))
    A('RAZON: %s' % f['razon'])
    A('DECISION_DEL_FUNDADOR: ')
    A('```')
    A('')
    A('PASAJE (%s):' % f['lineas'])
    A('')
    for l in f['pasaje'].split('\n'):
        A('> ' + l)
    A('')
txt = '\n'.join(L) + '\n'
txt = txt.replace('—', '--').replace('–', '-')
io.open(R + '/docs/fidelidad/campania/TRAMO1_SEGURIDAD_Y_SALUD.md', 'w', encoding='utf-8', newline='\n').write(txt)
print(len(txt), 'bytes;', txt.count('—') + txt.count('–'), 'rayas')
