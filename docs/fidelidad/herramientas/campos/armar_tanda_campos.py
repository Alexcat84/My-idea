# -*- coding: utf-8 -*-
"""Tanda de la pasada sobre los campos que no son pasos: de cada hallazgo se aplica SOLO el cambio que cae sobre
su fragmento (el texto_fiel del agente reescribe el campo entero; lo que cambie fuera del fragmento se descarta).
Varios hallazgos del mismo campo se combinan. Las rayas que ya traia el texto vigente se cambian por comas (la
regla de la casa las prohibe y el aplicador rechaza un texto nuevo con ellas); se declara.

Uso (desde my-idea-correcciones): python armar_tanda_campos.py <hallazgos.json> <W> <tanda_id> <salida.json> <ajustes.json>
Imprime lo que no pudo armar (fragmento no localizado, parches que se pisan) para revisarlo a mano.
"""
import collections
import difflib
import io
import json
import re
import sys

HALL, W, TID, SAL, AJ = sys.argv[1:6]
AJUSTES = json.load(io.open(AJ, encoding='utf-8'))
CAMPO = {'resumen': 'resumen_teorico', 'entregable': 'entregable_esperado', 'condiciones': 'condiciones_activacion',
         'etiqueta': 'etiqueta_arbol', 'titulo': 'titulo_concepto'}
RAYA = (chr(0x2014), chr(0x2013))


def n(s):
    for a, b in ((chr(0x2019), "'"), (chr(0x2018), "'"), (chr(0x201c), '"'), (chr(0x201d), '"')):
        s = s.replace(a, b)
    return ' '.join(s.split())


def localizar(texto, frag):
    """Posicion (ini, fin) del fragmento en el texto; tolera espacios y la barra que el mezclador puso por '|'."""
    i = texto.find(frag)
    if i >= 0:
        return i, i + len(frag)
    patron = r'\s+'.join(re.escape(w).replace('/', '[/|]') for w in frag.split())
    m = re.search(patron, texto)
    return (m.start(), m.end()) if m else None


def parches(orig, fiel, ini, fin):
    """Cambios de orig->fiel, PALABRA A PALABRA (nunca parte una palabra), que tocan [ini, fin): lista de
    (a0, a1, texto_nuevo) en posiciones de caracter de orig."""
    ta, tb = re.findall(r'\s+|\S+', orig), re.findall(r'\s+|\S+', fiel)
    pos, p = [], 0
    for t in ta:
        pos.append(p)
        p += len(t)
    pos.append(p)
    out = []
    for op, a0, a1, b0, b1 in difflib.SequenceMatcher(None, ta, tb, autojunk=False).get_opcodes():
        if op == 'equal':
            continue
        c0, c1 = pos[a0], pos[a1]
        if (c0 < fin and c1 > ini) or (c0 == c1 and ini <= c0 <= fin):
            out.append((c0, c1, ''.join(tb[b0:b1])))
    return out


def rayas(s):
    s = re.sub(r'\s*[%s]\s*' % ''.join(RAYA), ', ', s)
    return re.sub(r',\s*,', ',', s)


H = json.load(io.open(HALL, encoding='utf-8'))
grupos = collections.OrderedDict()
for h in sorted(H, key=lambda h: (h['veredicto'] != 'CONTRARIO', h['node_id'], h['campo'], h['indice'])):
    grupos.setdefault((h['node_id'], h['campo'], h['indice'] if h['campo'] == 'condiciones' else 0), []).append(h)
T, problemas, i = [], [], 0
for (nid, campo, idx), hs in grupos.items():
    d = json.load(io.open('dataset/nodos/%s.json' % nid, encoding='utf-8'))
    c = CAMPO[campo]
    vigente = d[c][idx] if campo == 'condiciones' else d.get(c, '')
    clave = '%s|%s|%d' % (nid, campo, idx)
    if clave in AJUSTES:
        nuevo = AJUSTES[clave]['texto']
        nota_ajuste = ' ' + AJUSTES[clave]['nota']
    else:
        todos = []
        for h in hs:
            pos = localizar(vigente, h['fragmento'])
            if not pos:
                problemas.append((clave, h['id'], 'fragmento no localizado: ' + h['fragmento'][:120]))
                continue
            todos += parches(vigente, h['texto_fiel'], *pos)
        todos.sort()
        if any(todos[k][1] > todos[k + 1][0] for k in range(len(todos) - 1)):
            problemas.append((clave, hs[0]['id'], 'parches que se pisan'))
            continue
        nuevo = vigente
        for a0, a1, txt in reversed(todos):
            nuevo = nuevo[:a0] + txt + nuevo[a1:]
        nota_ajuste = ''
    if nuevo == vigente:
        problemas.append((clave, hs[0]['id'], 'sin cambio tras recortar al fragmento'))
        continue
    nota_raya = ''
    if any(r in nuevo for r in RAYA):
        nuevo = rayas(nuevo)
        nota_raya = ' El texto vigente traia rayas; la sesion las cambia por comas (regla de la casa), sin tocar el sentido.'
    h0 = hs[0]
    lote = h0['id'].split('-')[0]
    reales = json.load(io.open('%s/c2/claves/reales_%s.json' % (W, lote), encoding='utf-8'))
    fich = next(r['ficheros'] for r in reales if r['node_id'] == nid)
    trozo = n(h0['frase_clave'].split('...')[0])[:60]
    fi = next((f for f in fich if trozo in n(io.open(f, encoding='utf-8', errors='replace').read())), fich[0])
    ver = 'CONTRARIO' if any(h['veredicto'] == 'CONTRARIO' for h in hs) else 'ANADIDO'
    if ver == 'CONTRARIO':
        dec = 'Mandato del fundador, regla B, CONTRARIO: version fiel del verificador o del arbitro, con su cita. '
    else:
        dec = 'Mandato del fundador, regla B, ANADIDO de cifra, plazo o norma: quitado o sustituido por lo que dice el libro. '
    dec += ('Decision del fundador (recogida el 24 sep 2026): pasada contra la fuente sobre los campos que llegan a la IA o a la '
            'pantalla (docs/fidelidad/CAMPOS_QUE_LLEGAN.md), solo CONTRARIOS y ANADIDOS de cifra, plazo o norma. ')
    dec += ' / '.join('%s (%s, %s): %s' % (h['id'], h['veredicto'], h['decidido_por'], h['razon']) for h in hs)
    dec += (' La sesion aplica solo el cambio que cae sobre el fragmento senalado; lo que el texto propuesto cambiara fuera de el '
            'se descarta.' if not nota_ajuste else '') + nota_ajuste + nota_raya
    i += 1
    e = {'node_id': nid, 'campo': c, 'veredicto': ver, 'texto_anterior': vigente, 'texto_nuevo': nuevo,
         'cita': {'libro': h0['libro'], 'fichero': fi.replace(chr(92), '/').split('Documents/', 1)[1],
                  'lineas': ', '.join(sorted({h['lineas'] for h in hs})),
                  'frase': ' / '.join(dict.fromkeys(h['frase_clave'] for h in hs))},
         'decision': dec,
         'auditoria': 'rama fidelidad-total, docs/fidelidad/campania/campos/VEREDICTOS_CAMPOS.jsonl, ids ' + ', '.join(h['id'] for h in hs),
         'id': '%s-%02d' % (TID, i), 'fecha': '2026-09-25'}
    if campo == 'condiciones':
        e['indice'] = idx
    T.append(e)
json.dump(T, io.open(SAL, 'w', encoding='utf-8', newline='\n'), ensure_ascii=False, indent=1)
print(len(T), 'correcciones de', len(H), 'hallazgos |', collections.Counter(t['campo'] for t in T), '| problemas', len(problemas))
for p in problemas:
    print('  PROBLEMA', p)
