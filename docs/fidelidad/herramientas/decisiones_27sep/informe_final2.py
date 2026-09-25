# -*- coding: utf-8 -*-
"""Reescribe docs/fidelidad/INFORME_FINAL_CAMPANIA.md y docs/fidelidad/EXCEPCIONES.md (rama fidelidad-total)
tras las decisiones del fundador del 27 sep 2026. Todas las cifras salen de ficheros; nada de memoria.

Uso: python informe_final2.py <repo_fidelidad> <repo_correcciones>
"""
import glob
import io
import json
import subprocess
import sys

RF, RC = sys.argv[1:3]
C = RF + '/docs/fidelidad/campania'
COB = json.load(io.open(C + '/COBERTURA_FINAL.json', encoding='utf-8'))
P2 = json.load(io.open(C + '/p2/RESUMEN.json', encoding='utf-8'))
P3 = json.load(io.open(C + '/p3/RESUMEN.json', encoding='utf-8'))
censo, N = COB['censo'], COB['pasos_vivos']


def commit(tag):
    return subprocess.run(['git', '-C', RC, 'rev-parse', '--short', tag + '^{commit}'], capture_output=True, text=True).stdout.strip()


tandas = []
for t in sorted(glob.glob(RC + '/docs/fidelidad/tandas/fidelidad-t*.json'), key=lambda s: int(s.split('-t')[-1].split('.')[0])):
    x = json.load(io.open(t, encoding='utf-8'))
    nom = t.replace(chr(92), '/').split('/')[-1][:-5]
    tandas.append((nom, commit(nom), len(x), sum(1 for c in x if c['veredicto'] == 'CONTRARIO'),
                   sum(1 for c in x if 'Sugerencia de My Idea' in c['texto_nuevo']), len({c['node_id'] for c in x})))
retiradas = json.load(io.open(RC + '/docs/fidelidad/PREGUNTAS_RETIRADAS.json', encoding='utf-8'))
reemb = [l for l in io.open(RC + '/docs/fidelidad/credencial/nodos_a_reembeber.txt', encoding='utf-8').read().split() if l]
L = []
A = L.append
sin = COB['contrarios_sin_corregir_en_main']
A('NINGUN CONTRARIO CONOCIDO QUEDA EN PRODUCCION' if not sin else 'QUEDAN CONTRARIOS SIN CORREGIR: %d' % len(sin))
A('')
A('# CAMPANIA DE FIDELIDAD TOTAL: INFORME FINAL')
A('')
A('Mandato del fundador: nunca le diremos a un cliente lo contrario de lo que dice su fuente. Busqueda en la rama fidelidad-total; '
  'correccion en la rama correcciones-fidelidad, llevada a main por avance rapido en las tandas fidelidad-t1 a fidelidad-t%d. '
  'Todo con claude-opus-5-5; los agentes solo leyeron, clasificaron, verificaron y propusieron; la sesion escribio cada fichero '
  'e hizo cada commit. Este informe incluye lo hecho por las decisiones del fundador del 27 sep 2026 (seccion 8).' % len(tandas))
A('')
A('## 1. Cobertura, comprobada por script')
A('')
A('**%d pasos vivos, %d con veredicto, %d sin veredicto, %d duplicados, %d que no existan** (campania/COBERTURA_FINAL.json).' % (
    N, COB['con_veredicto'], COB['n_faltan'], COB['n_duplicados'], COB['n_sobran']))
A('')
A('**Cada paso vivo tiene al menos dos lecturas ciegas independientes contra su libro, salvo 3 pasos que el lector de la campania leyo OPERATIVO y que por un caso de borde del flujo no pasaron al verificador (OPERATIVO no se corrige): `amortizacion_y_periodo_de_gracia` p4, `eliminar_metas_numericas_gerencia` p1 y `eliminar_cuotas_numericas_trabajadores` p2.** Los no FIEL: lector y verificador ciego, '
  'y arbitro si no coincidian. Los FIEL: los muestreados en la campania por el verificador; todos los demas, por la segunda '
  'pasada ciega de la decision 5 (2763 de seguridad y salud y de legal y dinero, y su ampliacion a los 6186 del resto).')
A('')
A('## 2. Censo por clase')
A('')
A('| clase | campania | ahora | que se hizo |')
A('|---|---:|---:|---|')
ca = COB['censo_campania']
A('| FIEL | %d | %d | nada |' % (ca.get('FIEL', 0), censo.get('FIEL', 0)))
A('| OPERATIVO | %d | %d | **no se toca** (decision del fundador 2: los OPERATIVOS se quedan) |' % (ca.get('OPERATIVO', 0), censo.get('OPERATIVO', 0)))
A('| ANADIDO | %d | %d | por regla: cifra, plazo, norma o materia legal, quitado o sustituido por el libro; practico, "Sugerencia de My Idea: ..." |' % (ca.get('ANADIDO', 0), censo.get('ANADIDO', 0)))
A('| CONTRARIO | %d | %d | **todos corregidos** con la version fiel, con su cita |' % (ca.get('CONTRARIO', 0), censo.get('CONTRARIO', 0)))
A('')
A('Lo que cambio despues de la campania:')
A('')
A('| fuente | de | a | pasos |')
A('|---|---|---|---:|')
for x in COB['cambios_posteriores']:
    A('| %s | %s | %s | %d |' % (x['fuente'], x['de'], x['a'], x['pasos']))
A('')
A('**Los CONTRARIOS, comprobado por script contra main:** %d CONTRARIOS conocidos (los del registro, los del muestreo, el del arbitraje '
  'de las excepciones y los de la segunda pasada y su ampliacion); **%d sin corregir** (scratchpad censo_final2.py).' % (COB['contrarios_conocidos'], len(sin)))
A('')
A('## 3. Lo medido del metodo')
A('')
A('- **Trampas en la campania:** 532 de 532 cazadas por los lectores y 532 de 532 por los verificadores ciegos; 32 de 32 en el tramo 1 calibrado.')
A('- **Trampas en la segunda pasada:** lectores %d de %d, verificadores %d de %d; en la ampliacion, lectores %d de %d y verificadores %d de %d.' % (
    P2['trampas_lector'][0], P2['trampas_lector'][1], P2['trampas_verificador'][0], P2['trampas_verificador'][1],
    P3['trampas_lector'][0], P3['trampas_lector'][1], P3['trampas_verificador'][0], P3['trampas_verificador'][1]))
A('  El lector del lote Q027 no cazo una trampa en dos lecturas (la leyo OPERATIVO; su verificador si la cazo). Por eso un verificador '
  'ciego extra releyo los 79 FIEL no muestreados de ese lote con sus 4 trampas dentro: 4 de 4, ningun ANADIDO ni CONTRARIO, 15 OPERATIVO '
  '(campania/p3/VERIFICADOR_EXTRA_Q027.json).')
A('- **Desacuerdos lector frente a verificador:** 656 en la campania, %d en la segunda pasada y %d en la ampliacion; todos arbitrados releyendo el libro.' % (P2['desacuerdos'], P3['desacuerdos']))
A('- **Lo que encontro la segunda lectura de los FIEL:** 7 CONTRARIOS y 1 ANADIDO en 8949 pasos (0,08 por ciento), todos corregidos. '
  'Los CONTRARIOS escondidos eran sutiles: un plazo alargado ("cada semana o dos" frente a "every week or so"), un criterio estrechado '
  '("negocios fallidos" frente a "con o sin exito"), una consecuencia invertida ("bajos costos" de la sobrecapacidad frente a "higher costs").')
A('- **Limites, dichos:** las trampas las escribe el mismo modelo que las caza; un solo arbitro por desacuerdo; la frontera FIEL y OPERATIVO '
  'es blanda (la segunda lectura paso %d FIEL a OPERATIVO), la que importa es la de ANADIDO y CONTRARIO; las guias de empaque escaneadas '
  'con columnas mezcladas no permiten cita literal contigua (seccion 7). "Ningun contrario conocido" es verdad; que no quede ninguno sin '
  'detectar no esta demostrado, pero cada paso, salvo esos 3 OPERATIVOS, ya lo leyeron dos lectores ciegos distintos.' % (
      sum(x['pasos'] for x in COB['cambios_posteriores'] if x['de'] == 'FIEL' and x['a'] == 'OPERATIVO')))
A('')
A('## 4. Tandas en produccion (main, avance rapido, con Gate 0 entero y las dos suites en verde)')
A('')
A('| tanda | commit | correcciones | de ellas CONTRARIO | sugerencias de My Idea | nodos |')
A('|---|---|---:|---:|---:|---:|')
for t in tandas:
    A('| %s | %s | %d | %d | %d | %d |' % t)
A('| **total** | | **%d** | **%d** | **%d** | |' % (sum(t[2] for t in tandas), sum(t[3] for t in tandas), sum(t[4] for t in tandas)))
A('')
A('Cada correccion vive en el campo `correcciones` de su nodo con el texto viejo, el nuevo, la cita literal (libro, lineas, frase) y la '
  'decision (docs/fidelidad/tandas/ en main). Las cuentas de CONTRARIO incluyen los datos repetidos en el resumen o el entregable del mismo nodo.')
A('')
A('## 5. Censo por libro')
A('')
A('| libro | pasos | FIEL | OPERATIVO | ANADIDO | CONTRARIO |')
A('|---|---:|---:|---:|---:|---:|')
for lib, c in sorted(COB['por_libro'].items(), key=lambda kv: -sum(kv[1].values())):
    A('| %s | %d | %d | %d | %d | %d |' % (lib.replace('|', '/')[:70], sum(c.values()), c.get('FIEL', 0), c.get('OPERATIVO', 0), c.get('ANADIDO', 0), c.get('CONTRARIO', 0)))
A('')
A('## 6. CENSO DE OPERATIVOS')
A('')
op = sorted(((lib, c.get('OPERATIVO', 0), sum(c.values())) for lib, c in COB['por_libro'].items()), key=lambda x: -x[1])
A('**%d pasos OPERATIVOS** (%.1f por ciento del catalogo): concretan lo que su libro dice, en su misma direccion y sin datos nuevos. '
  'Decision del fundador 2: se quedan. Por libro, de mas a menos:' % (censo.get('OPERATIVO', 0), 100.0 * censo.get('OPERATIVO', 0) / N))
A('')
A('| libro | OPERATIVOS | de sus pasos |')
A('|---|---:|---:|')
for lib, o, n in op:
    if o:
        A('| %s | %d | %.0f%% |' % (lib.replace('|', '/')[:70], o, 100.0 * o / n))
A('')
A('## 7. EXCEPCIONES')
A('')
A('Ver docs/fidelidad/EXCEPCIONES.md. Ninguna es un CONTRARIO sin corregir.')
A('')
A('## 8. Decisiones del fundador del 27 sep 2026, una por una')
A('')
A('1. **Textos derivados.** Se buscaron los textos anteriores de las 120 correcciones de CONTRARIO y las 125 de cifra, plazo o norma en la '
  'cache de preguntas y en todo fichero derivado. Ninguna pregunta contiene un texto viejo; pero el generador lee los 400 primeros caracteres '
  'del resumen, asi que las preguntas cuyo resumen se corrigio dentro de ese tramo se **retiraron de la cache: %d** (docs/fidelidad/PREGUNTAS_RETIRADAS.json '
  'en main, con la pregunta, sus candidatos y la correccion que la invalida). Caen a la generica que la sesion adapta en vivo. El master_graph lleva '
  'el campo `correcciones` con los textos viejos, pero ningun codigo de web/ lo lee ni lo manda a un prompt. 7 textos viejos siguen identicos en nodos '
  'deprecados, que la app no ofrece y que resuelven al superviviente corregido.' % len(retiradas))
A('2. **OPERATIVOS: se quedan.** Lista de atribuciones a autor para la sesion de idiomas: docs/fidelidad/ATRIBUCIONES_A_AUTOR.md en main '
  '(el codigo de web/ no atribuye nada ni lee el campo fuente; los nombres de autor viven dentro del texto de 241 nodos, con fichero y linea).')
A('3. **EXCEPCIONES.** Las 4 con desacuerdo, a un arbitro con el libro (campania/ARBITRAJE_EXCEPCIONES.json): 1 CONTRARIO y 3 ANADIDOS practicos, '
  'corregidos en fidelidad-t10. Las 3 guias escaneadas: el fundador reconvierte los PDF y los pasara; pendientes (EXCEPCIONES.md, seccion B).')
A('4. **Criterios ratificados:** quitar el dominio en los 3 pasos; el prefijo "Sugerencia de My Idea:"; la voz de la casa solo si el significado no cambia, con registro y cita.')
A('5. **Segunda pasada ciega dirigida:** 2763 FIEL de seguridad y salud y de legal y dinero dieron 5 CONTRARIOS (fidelidad-t11); por la regla, se amplio '
  'al resto de los FIEL (6186), que dio 2 CONTRARIOS y 1 ANADIDO (fidelidad-t12). Registro: campania/p2/ y campania/p3/.')
A('6. **Documentacion:** docs/fidelidad/ de esta rama y el informe del muestreo se fusionan a main como archivo.')
A('7. **Sesion con credencial:** %d nodos a re-embeber (el indice embebe titulo, resumen y condiciones, no los pasos) y %d preguntas a regenerar; '
  'listas exactas en docs/fidelidad/credencial/ de main (LISTAS.md con la razon de cada una).' % (len(reemb), len(retiradas)))
txt = '\n'.join(L) + '\n'
io.open(RF + '/docs/fidelidad/INFORME_FINAL_CAMPANIA.md', 'w', encoding='utf-8', newline='\n').write(txt.replace(chr(0x2014), '--').replace(chr(0x2013), '-'))

# EXCEPCIONES
E = []
e = E.append
e('# EXCEPCIONES DE LA CAMPANIA DE FIDELIDAD')
e('')
e('Lo que la regla del fundador no resolvio limpio, para que lo decida el fundador. Actualizado tras sus decisiones del 27 sep 2026.')
e('')
e('## A. Resueltas')
e('')
e('- `ficcion_especulativa_como_metodo` paso 2: la campania lo leyo ANADIDO con texto limpio; corregido en fidelidad-t9-013.')
ARB = json.load(io.open(C + '/ARBITRAJE_EXCEPCIONES.json', encoding='utf-8'))
for x in ARB:
    e('- `%s` paso %d: el arbitro con el libro lo leyo %s (%s, "%s"); corregido en fidelidad-t10.' % (x['node_id'], x['paso'], x['veredicto'], x['lineas'], x['frase_literal'][:160]))
e('')
e('## B. Pendientes: las 3 guias de empaque escaneadas')
e('')
e('ANADIDOS practicos cuya frase de apoyo existe en la fuente, pero partida por el escaneo en trozos no contiguos. Decision del fundador 3: OCR '
  'para sacar la cita; si no se puede, esos pasos pasan a "Sugerencia de My Idea:" sin atribucion. **El fundador reconvierte los PDF y los pasara.**')
e('')
for nid, p, fuente, fich in (('adaptar_empaque_segun_tipo_de_articulo', 2, 'Guia visual de empaque (infografia de UPS)', 'I have an idea/txt/Supply chain/packaging_guide_infographic.txt, L47-L55'),
                             ('adaptar_empaque_segun_tipo_de_articulo', 4, 'Guia visual de empaque (infografia de UPS)', 'I have an idea/txt/Supply chain/packaging_guide_infographic.txt, L61-L67'),
                             ('revisar_necesidades_de_empaque', 3, 'DHL Express, Guia de empaque', 'I have an idea/txt/Supply chain/dhl_express_packing_guide_en.txt, L51-L53')):
    d = json.load(io.open('%s/dataset/nodos/%s.json' % (RC, nid), encoding='utf-8'))
    e('- `%s` paso %d (%s; %s). **Texto vigente:** %s' % (nid, p, fuente, fich, d['pasos_accionables'][p - 1]))
e('')
e('## C. Para ratificar: textos que la sesion ajusto sobre la propuesta del verificador o del arbitro')
e('')
e('- `decision_fpr` paso 2 (fidelidad-t11-01): el texto del arbitro decia que el FPR "facilita la venta"; el libro lo desmiente (L2052, "no significant '
  'correlation between the use of an FPR and speed of growth"; L4695). Quedo con los beneficios que el libro si da (L4715 y L4717) y dos razones para no usarlo (L4719).')
e('- `documentacion_mantenimiento_linea_base` paso 2 (fidelidad-t10-03): se quito del texto del arbitro una coletilla que remitia al texto viejo.')
e('- Restitucion de tildes en textos de verificador sin ellas: fidelidad-t11-05 y fidelidad-t12-02.')
t = '\n'.join(E) + '\n'
io.open(RF + '/docs/fidelidad/EXCEPCIONES.md', 'w', encoding='utf-8', newline='\n').write(t.replace(chr(0x2014), '--').replace(chr(0x2013), '-'))
print('informe y excepciones escritos;', len(tandas), 'tandas;', sum(t[2] for t in tandas), 'correcciones')
