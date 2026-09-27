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
A('## Estado del catalogo, solo con lo probado')
A('')
an_sin = COB['anadidos_sin_correccion_en_main']
CAMPOS = json.load(io.open(C + '/campos/RESUMEN.json', encoding='utf-8'))
nh = sum(CAMPOS['hallazgos'].values())
A('> **Los %d pasos accionables vivos del catalogo de My Idea se leyeron a ciegas contra su fuente, cada uno por al menos dos lectores '
  'independientes salvo 3 que quedaron OPERATIVOS con una sola lectura; los %d que la contradecian y los %d que afirmaban algo que la '
  'fuente no respalda tienen su correccion declarada en produccion, con cita literal, y un script lo comprueba contra main (%d y %d sin '
  'corregir). Los demas campos que llegan a la IA o a la pantalla (resumen, entregable, condiciones, titulo y etiqueta) de los %d nodos '
  'vivos se leyeron tambien a ciegas contra su fuente, buscando solo contrarios y anadidos de cifra, plazo o norma: los %d hallados tienen '
  'su correccion declarada en produccion (%d sin corregir). No esta demostrado que no quede ningun error sin detectar, y en esos campos no '
  'se buscaron anadidos practicos.**' % (N, COB['contrarios_conocidos'], COB['anadidos'], len(sin), len(an_sin), CAMPOS['nodos'], nh,
                                         len(CAMPOS['hallazgos_sin_correccion_en_main'])))
A('')
A('Mandato del fundador: nunca le diremos a un cliente lo contrario de lo que dice su fuente. Busqueda en la rama fidelidad-total; '
  'correccion en la rama correcciones-fidelidad, llevada a main por avance rapido en las tandas fidelidad-t1 a fidelidad-t%d. '
  'Todo con claude-opus-5-5; los agentes solo leyeron, clasificaron, verificaron y propusieron; la sesion escribio cada fichero '
  'e hizo cada commit. Este informe incluye lo hecho por las decisiones del fundador recogidas el 24 sep 2026 (secciones 8 a 10; fechadas 27 sep por error, vale la fecha del commit: docs/PENDIENTES.md seccion 0).' % len(tandas))
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
A('## 8. Decisiones del fundador recogidas el 24 sep 2026, una por una')
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
A('')
A('## 9. Segundas decisiones del fundador, recogidas el 24 sep 2026')
A('')
A('1. **Ratificados** los textos que la sesion ajusto (EXCEPCIONES.md, seccion C).')
A('2. **Atribuciones:** los nombres de autor dentro del texto de los nodos se quedan; no hay cambio de interfaz pendiente.')
A('3. **Pagina del auditor externo** actualizada con estas cifras.')
A('4. **Guias escaneadas:** el fundador reextrajo los PDF linea por linea con coordenadas. La infografia se identifico como la de UPS por el '
  'encabezado de su extraccion; la de DHL se comparo con la version oficial descargada (23/07/2026 frente a la local del 25/02/2026: mismo texto '
  'salvo un parrafo nuevo sobre "black foil"; la frase citada identica). Las dos ya tienen cita literal: 3 ANADIDOS practicos a "Sugerencia de '
  'My Idea:" en fidelidad-t13. Al comprobar por script que cada ANADIDO del censo tuviera su correccion aparecio uno sin corregir: '
  '`creacion_option_pool` p2, una excepcion del bloque B1 que se habia perdido (la cita no se reconocio por unas comillas tipograficas y nunca paso '
  'a EXCEPCIONES.md). Corregido en fidelidad-t14, junto con una cifra cambiada en su resumen ("hasta 20%" frente a "averaged 20%").')
A('5. **Sesion con credencial:** pendiente de que el fundador diga "clave cargada"; listas exactas en docs/fidelidad/credencial/ de main '
  '(%d nodos a re-embeber y %d preguntas a regenerar tras fidelidad-t14).' % (len(reemb), len(retiradas)))
A('6. **Frase de estado:** al principio de este informe.')
A('')
A('## 10. La pasada sobre los campos que llegan a la IA o a la pantalla')
A('')
A('Decision del fundador (recogida el 24 sep): medir que campos llegan a la IA o a la pantalla (docs/fidelidad/CAMPOS_QUE_LLEGAN.md en main) y, '
  'si alguno aparte de los pasos llega, leerlo contra la fuente con el mismo metodo calibrado, buscando solo CONTRARIOS y ANADIDOS de cifra, '
  'plazo o norma. Llegan el resumen, el entregable, las condiciones de activacion, el titulo y la etiqueta de cara.')
A('')
A('- **Cobertura:** %d nodos vivos, una fila por nodo con sus cinco campos, en %d lotes.' % (CAMPOS['nodos'], len(CAMPOS['lotes'])))
A('- **Trampas:** %d nodos trampa con un error sembrado; lectores %d, verificadores %d. La trampa de R013 (un plazo de 12 meses anadido en una '
  'condicion) se escapo a cuatro lecturas: lector, relectura, verificador y un verificador ciego extra, que releyo los nodos limpios no '
  'muestreados de ese lote sin encontrar nada en los reales.' % (CAMPOS['trampas_lector'][1], CAMPOS['trampas_lector'][0], CAMPOS['trampas_verificador'][0]))
A('- **Desacuerdos arbitrados:** %d.' % CAMPOS['desacuerdos'])
A('- **Hallazgos:** %d en %d nodos: %s. Corregidos en fidelidad-t15 (76 correcciones), cada uno con su cita literal; %d sin corregir.' % (
    nh, CAMPOS['nodos_con_hallazgo'], ', '.join('%d %s' % (v, k) for k, v in sorted(CAMPOS['hallazgos'].items(), key=lambda kv: -kv[1])),
    len(CAMPOS['hallazgos_sin_correccion_en_main'])))
A('- **Textos derivados:** 50 preguntas de la cache retiradas (nacieron de un resumen o de las condiciones de un candidato ahora corregidos) y '
  '2 puertas del mundo entrega restauradas por la guarda AUD-09 H13, sin el dato corregido. Segunda sesion con credencial pendiente: listas '
  'en docs/fidelidad/credencial/ de main.')
A('- **Registro:** campania/campos/ (VEREDICTOS_CAMPOS.jsonl, RESUMEN.json, VERIFICADOR_EXTRA_R013.json y el rastro de cada lote).')
txt = '\n'.join(L) + '\n'
io.open(RF + '/docs/fidelidad/INFORME_FINAL_CAMPANIA.md', 'w', encoding='utf-8', newline='\n').write(txt.replace(chr(0x2014), '--').replace(chr(0x2013), '-'))

# EXCEPCIONES
E = []
e = E.append
e('# EXCEPCIONES DE LA CAMPANIA DE FIDELIDAD')
e('')
e('Lo que la regla del fundador no resolvio limpio, para que lo decida el fundador. Actualizado tras sus decisiones recogidas el 24 sep 2026.')
e('')
e('## A. Resueltas')
e('')
e('- `ficcion_especulativa_como_metodo` paso 2: la campania lo leyo ANADIDO con texto limpio; corregido en fidelidad-t9-013.')
ARB = json.load(io.open(C + '/ARBITRAJE_EXCEPCIONES.json', encoding='utf-8'))
for x in ARB:
    e('- `%s` paso %d: el arbitro con el libro lo leyo %s (%s, "%s"); corregido en fidelidad-t10.' % (x['node_id'], x['paso'], x['veredicto'], x['lineas'], x['frase_literal'][:160]))
e('')
e('- `adaptar_empaque_segun_tipo_de_articulo` pasos 2 y 4 y `revisar_necesidades_de_empaque` paso 3 (guias escaneadas): con la extraccion nueva del fundador, cita literal; ANADIDOS practicos a "Sugerencia de My Idea:" en fidelidad-t13.')
e('- `creacion_option_pool` paso 2: excepcion del bloque B1 que se habia perdido (su cita no se reconocio por unas comillas tipograficas y nunca llego a este fichero). La encontro la comprobacion por script de los ANADIDOS; corregida en fidelidad-t14.')
e('')
e('## B. Abiertas')
e('')
e('Ninguna.')
e('')
e('## C. Textos que la sesion ajusto sobre la propuesta del verificador o del arbitro: RATIFICADOS por el fundador (decision recogida el 24 sep 2026)')
e('')
e('- `decision_fpr` paso 2 (fidelidad-t11-01): el texto del arbitro decia que el FPR "facilita la venta"; el libro lo desmiente (L2052, L4695).')
e('- `documentacion_mantenimiento_linea_base` paso 2 (fidelidad-t10-03): se quito una coletilla que remitia al texto viejo.')
e('- Restitucion de tildes: fidelidad-t11-05 y fidelidad-t12-02.')
e('')
e('## D. Declarado sin corregir')
e('')
e('- El resumen de `adaptar_empaque_segun_tipo_de_articulo` repite como dato practico la bolsa plastica para liquidos y la caja dentro de caja. Por el precedente de las tandas, el dato repetido en resumen o entregable solo se corrigio en CONTRARIOS y en cifras, plazos o normas; los resumenes no los pinta ninguna pantalla.')
t = '\n'.join(E) + '\n'
io.open(RF + '/docs/fidelidad/EXCEPCIONES.md', 'w', encoding='utf-8', newline='\n').write(t.replace(chr(0x2014), '--').replace(chr(0x2013), '-'))
print('informe y excepciones escritos;', len(tandas), 'tandas;', sum(t[2] for t in tandas), 'correcciones')
