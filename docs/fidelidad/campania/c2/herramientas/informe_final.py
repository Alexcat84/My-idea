# -*- coding: utf-8 -*-
"""Escribe docs/fidelidad/INFORME_FINAL_CAMPANIA.md y reescribe docs/fidelidad/EXCEPCIONES.md (rama fidelidad-total)."""
import collections
import glob
import io
import json
import sys

RF, RC, W = sys.argv[1:4]
COB = json.load(io.open(RF + '/docs/fidelidad/campania/COBERTURA_FINAL.json', encoding='utf-8'))
censo = COB['censo']
N = COB['pasos_vivos']
tandas = []
for t in sorted(glob.glob(RC + '/docs/fidelidad/tandas/fidelidad-t*.json'), key=lambda s: int(s.split('-t')[-1].split('.')[0])):
    x = json.load(io.open(t, encoding='utf-8'))
    tandas.append((t.replace('\\', '/').split('/')[-1][:-5], len(x), sum(1 for c in x if c['veredicto'] == 'CONTRARIO'),
                   sum(1 for c in x if c['texto_nuevo'].startswith('Sugerencia de My Idea')), len({c['node_id'] for c in x})))
L = []
A = L.append
A('NINGUN CONTRARIO CONOCIDO QUEDA EN PRODUCCION')
A('')
A('# CAMPANIA DE FIDELIDAD TOTAL: INFORME FINAL')
A('')
A('Mandato del fundador: nunca le diremos a un cliente lo contrario de lo que dice su fuente. Busqueda en la rama fidelidad-total; correccion en la rama correcciones-fidelidad, llevada a main por avance rapido en las tandas fidelidad-t1 a fidelidad-t9. Todo con claude-opus-5-5; los agentes solo leyeron, clasificaron, verificaron y propusieron; la sesion escribio cada fichero e hizo cada commit.')
A('')
A('## 1. Cobertura, comprobada por script')
A('')
A('**%d pasos vivos, %d con veredicto, 0 sin veredicto, 0 duplicados, 0 que no existan** (docs/fidelidad/campania/COBERTURA_FINAL.json). Fuentes del registro: el tramo 1 calibrado (VEREDICTOS_TRAMO1.jsonl, 827 pasos) y la campania (c2/VEREDICTOS_CAMPANIA.jsonl, 14484 pasos, 133 lotes, que incluyen Reason y Assembling Tomorrow releidos enteros).' % (N, COB['con_veredicto']))
A('')
A('## 2. Censo por clase')
A('')
A('| clase | pasos | que se hizo |')
A('|---|---:|---|')
A('| FIEL | %d | nada |' % censo.get('FIEL', 0))
A('| OPERATIVO | %d | **no se toca**; su politica la decide el fundador con esta cifra delante (seccion 6) |' % censo.get('OPERATIVO', 0))
A('| ANADIDO | %d | por regla: cifra, plazo, norma o materia legal, quitado o sustituido por el libro; practico, "Sugerencia de My Idea: ..."; lo que la regla no resolvio limpio, a EXCEPCIONES |' % censo.get('ANADIDO', 0))
A('| CONTRARIO | %d | **todos corregidos** con la version fiel del verificador (o del arbitro), con su cita |' % censo.get('CONTRARIO', 0))
A('')
A('**Los CONTRARIOS, comprobado por script contra main:** cada uno de los 93 CONTRARIOS conocidos (los del registro mas los 5 del muestreo) tiene en su nodo una correccion declarada de ese paso (scratchpad contrarios_en_produccion.py: 93 de 93, 0 sin corregir).')
A('')
A('## 3. Lo medido del metodo')
A('')
A('- **Trampas:** 532 de 532 cazadas por los lectores y 532 de 532 por los verificadores ciegos en la campania; 32 de 32 en el tramo 1. Ningun lote tuvo que releerse.')
A('- **Desacuerdos lector frente a verificador:** 656, todos arbitrados releyendo el libro.')
A('- **FIEL releidos a ciegas:** 1731; 141 eran OPERATIVO y **1 era CONTRARIO** (cazado y corregido). Tasa de CONTRARIO escondido entre los FIEL: 0,06 por ciento, intervalo de Wilson al 95 por ciento de 0,01 a 0,33. **Lo que eso significa, dicho claro:** entre los unos 8960 pasos FIEL que no se muestrearon puede quedar del orden de 5 CONTRARIOS no detectados (cota superior al 95 por ciento: unos 30). "Ningun contrario conocido" es verdad; "ningun contrario" no esta demostrado.')
A('- **Limites:** las trampas las escribe el mismo modelo que las caza; un solo arbitro por desacuerdo; las guias de empaque escaneadas con columnas mezcladas no permiten cita literal contigua.')
A('')
A('## 4. Tandas en produccion (main, avance rapido, con Gate 0 entero y las dos suites en verde)')
A('')
A('| tanda | correcciones | de ellas CONTRARIO | sugerencias de My Idea | nodos |')
A('|---|---:|---:|---:|---:|')
for t in tandas:
    A('| %s | %d | %d | %d | %d |' % t)
A('| **total** | **%d** | **%d** | **%d** | |' % (sum(t[1] for t in tandas), sum(t[2] for t in tandas), sum(t[3] for t in tandas)))
A('')
A('Cada correccion vive en el campo `correcciones` de su nodo con el texto viejo, el nuevo, la cita literal (libro, lineas, frase) y la decision (rama correcciones-fidelidad, docs/fidelidad/tandas/). Las cuentas de CONTRARIO de la tabla incluyen los datos repetidos en el resumen o el entregable del mismo nodo.')
A('')
A('## 5. Censo por libro')
A('')
A('| libro | pasos | FIEL | OPERATIVO | ANADIDO | CONTRARIO |')
A('|---|---:|---:|---:|---:|---:|')
for lib, c in sorted(COB['por_libro'].items(), key=lambda kv: -sum(kv[1].values())):
    A('| %s | %d | %d | %d | %d | %d |' % (lib.replace('|', '/')[:70], sum(c.values()), c.get('FIEL', 0), c.get('OPERATIVO', 0), c.get('ANADIDO', 0), c.get('CONTRARIO', 0)))
A('')
A('## 6. CENSO DE OPERATIVOS, para la decision del fundador')
A('')
op = sorted(((lib, c.get('OPERATIVO', 0), sum(c.values())) for lib, c in COB['por_libro'].items()), key=lambda x: -x[1])
A('**%d pasos OPERATIVOS** (%.1f por ciento del catalogo): concretan lo que su libro dice, en su misma direccion y sin datos nuevos. No se toco ninguno. Por libro, de mas a menos:' % (censo.get('OPERATIVO', 0), 100.0 * censo.get('OPERATIVO', 0) / N))
A('')
A('| libro | OPERATIVOS | de sus pasos |')
A('|---|---:|---:|')
for lib, o, n in op:
    if o:
        A('| %s | %d | %.0f%% |' % (lib.replace('|', '/')[:70], o, 100.0 * o / n))
A('')
A('## 7. EXCEPCIONES para el fundador')
A('')
A('Ver docs/fidelidad/EXCEPCIONES.md: lo que la regla no resolvio limpio, sin corregir. Ninguna es un CONTRARIO.')
A('')
A('## 8. Pendiente para la integracion del mundo 11')
A('')
A('Anotado en docs/PENDIENTES.md seccion 0a (en main): re-embeber los nodos corregidos y regenerar su cache de preguntas en la sesion con credencial; y, al sincronizar puente-forja con main, regenerar los derivados del grafo en vez de fusionarlos a mano.')
txt = '\n'.join(L) + '\n'
io.open(RF + '/docs/fidelidad/INFORME_FINAL_CAMPANIA.md', 'w', encoding='utf-8', newline='\n').write(txt.replace(chr(0x2014), '--').replace(chr(0x2013), '-'))

# EXCEPCIONES
E = []
e = E.append
e('# EXCEPCIONES DE LA CAMPANIA DE FIDELIDAD')
e('')
e('Lo que la regla del fundador no resolvio limpio va aqui, **sin corregir**, para que lo decida el fundador. **Ninguna es un CONTRARIO** en la lectura final. Cada entrada trae el texto vigente, los veredictos que tuvo y por que la regla no lo resuelve. DECISION_DEL_FUNDADOR en blanco.')
e('')
e('## A. Resuelta por la campania')
e('')
e('- `ficcion_especulativa_como_metodo` paso 2 (antes D05, tanda t3): la campania lo leyo ANADIDO con texto limpio y quedo corregido en fidelidad-t9-013.')
e('')
e('## B. Veredictos que no coinciden entre fases (ninguno CONTRARIO)')
e('')
filas = [
    ('abrazar_la_incomodidad', 4, 'Assembling Tomorrow', 'muestreo: ANADIDO (A1); regla B de t3: EXCEPCION, roza CONTRARIO (el libro pide "linger in discomfort", L2688; el paso registra lo que surge "despues de superar" la incomodidad); campania (lector y verificador ciego): OPERATIVO', 'Registra los descubrimientos que surgen mientras permaneces en la incomodidad, sin resolverla antes de tiempo.'),
    ('accidentes_individuales_vs_organizacionales', 1, 'Reason', 'muestreo con tercer lector: ANADIDO (A23, la condicion "antes de iniciar cualquier investigacion"); regla B de t3: EXCEPCION (condicion de orden, ni cifra ni herramienta); campania: OPERATIVO', ''),
    ('documentacion_mantenimiento_linea_base', 2, 'Reason', 'muestreo con tercer lector: ANADIDO (A24, "toda tarea, sin importar su origen" frente a L417, linea y base piden planes distintos); regla B de t3: EXCEPCION (regla interna universal, ni norma legal ni herramienta); campania: OPERATIVO', ''),
    ('sesgo_retrospectivo_hindsight_2', 3, 'Dekker', 'tramo 1: ANADIDO (DK4-035); regla B de t3: EXCEPCION (el dato "sin olvidar el volumen de informacion disperso entre los participantes" no es cifra ni herramienta, es un matiz conceptual)', ''),
]
for nid, p, lib, hist, fiel in filas:
    d = json.load(io.open('%s/dataset/nodos/%s.json' % (RC, nid), encoding='utf-8'))
    e('### `%s` paso %d (%s)' % (nid, p, lib))
    e('')
    e('- **Texto vigente:** %s' % d['pasos_accionables'][p - 1])
    e('- **Veredictos:** %s' % hist)
    if fiel:
        e('- **Texto fiel propuesto en su dia:** %s' % fiel)
    e('- **DECISION_DEL_FUNDADOR:** ')
    e('')
e('## C. Cita no literal por el escaneo de la fuente (ANADIDOS practicos)')
e('')
e('Las guias de empaque escaneadas (infografia visual y guia de DHL) mezclan columnas en el texto: la frase que respalda la lectura existe, pero partida en trozos no contiguos, asi que no hay cita literal que el script pueda comprobar. Son ANADIDOS practicos (pasarian a "Sugerencia de My Idea"); no contradicen nada.')
e('')
D = json.load(io.open(W + '/c2/decision/B6.json', encoding='utf-8'))
for x in D['excepciones']:
    f = x['ficha']
    e('### `%s` paso %d (%s)' % (f['node_id'], f['paso_desde_1'], f['libro']))
    e('')
    e('- **Texto vigente:** %s' % f['texto_actual'])
    e('- **Propuesta de la regla:** %s' % (f['texto_sugerencia'] or f['texto_fiel']))
    e('- **Frase del lector:** %s (%s)' % (f['frase_clave'], f['lineas']))
    e('- **DECISION_DEL_FUNDADOR:** ')
    e('')
t = '\n'.join(E) + '\n'
io.open(RF + '/docs/fidelidad/EXCEPCIONES.md', 'w', encoding='utf-8', newline='\n').write(t.replace(chr(0x2014), '--').replace(chr(0x2013), '-'))
print('informe y excepciones escritos;', len(D['excepciones']) + len(filas), 'excepciones abiertas')
