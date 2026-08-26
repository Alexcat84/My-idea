# Sonda del auditor de la vuelta 71: textos pre fusion del lote G (sin razones)
# y comprobacion verbatim de los cinco trozos de INCISO. Solo lee; escribe su
# salida en docs/loop/_auditor_v71/.
import json, subprocess, io

raw = subprocess.run(['git', 'show', 'c1859ed5:dataset/metadata/master_graph.json'],
                     capture_output=True, text=True, encoding='utf-8').stdout
g = json.loads(raw)['nodos']

actos = {
    38: ['segmentos_de_clientes_problema_necesidad', 'customer_segments_hypothesis', 'problem_recognition_scale'],
    39: ['defensas_en_profundidad_3', 'defensas_en_profundidad', 'defensas_en_profundidad_2'],
    40: ['traction_goal', 'definir_meta_de_traccion', 'moving_the_needle'],
    41: ['design_for_six_sigma_dfss', 'design_for_six_sigma_dmadv', 'design_for_six_sigma_dmadv_2'],
    42: ['equipo_multifuncional_real', 'diseno_organizacional_equipos_innovacion', 'equipo_multifuncional'],
}

out = io.StringIO()
for a, miembros in actos.items():
    out.write('\n===== ACTO %d =====\n' % a)
    for m in miembros:
        n = g[m]
        out.write('\n--- %s (dominio %s, fase %s) ---\n' % (m, n.get('dominio'), n.get('fase')))
        out.write('TITULO: %s\n' % n.get('titulo'))
        out.write('RESUMEN: %s\n' % (n.get('resumen') or n.get('descripcion') or '')[:700])
        for i, p in enumerate(n.get('pasos_accionables') or [], 1):
            out.write('  paso %d: %s\n' % (i, p))
        for i, c in enumerate(n.get('condiciones_activacion') or [], 1):
            out.write('  cond %d: %s\n' % (i, c))

open('docs/loop/_auditor_v71/TEXTOS_PRE_FUSION_LOTE_G.txt', 'w', encoding='utf-8').write(out.getvalue())
print('escrito', len(out.getvalue()), 'caracteres')

trozos = [
    ('38', 'y también cuando aún no existe y tú le muestras una visión'),
    ('38', 'determinando la intensidad del dolor que causa el problema'),
    ('39', 'clasificándolas en las siete funciones defensivas'),
    ('40', 'en números concretos como cantidad de clientes y tasa de crecimiento mensual'),
    ('42', 'y elígelo con espíritu emprendedor'),
]
absorbidos = ['customer_segments_hypothesis', 'problem_recognition_scale',
              'defensas_en_profundidad', 'defensas_en_profundidad_2',
              'definir_meta_de_traccion', 'moving_the_needle',
              'design_for_six_sigma_dmadv', 'design_for_six_sigma_dmadv_2',
              'diseno_organizacional_equipos_innovacion', 'equipo_multifuncional']
for acto, t in trozos:
    hallado = [m for m in absorbidos if t in json.dumps(g[m], ensure_ascii=False)]
    print('TROZO acto', acto, repr(t[:45]), '->', hallado if hallado else 'NO HALLADO')

# Y los cinco pasos resultantes presentes en el grafo de HOY
hoy = json.load(open('dataset/metadata/master_graph.json', encoding='utf-8'))['nodos']
resultantes = [
    ('segmentos_de_clientes_problema_necesidad', 'y también cuando aún no existe y tú le muestras una visión'),
    ('segmentos_de_clientes_problema_necesidad', 'determinando la intensidad del dolor que causa el problema'),
    ('defensas_en_profundidad_3', 'clasificándolas en las siete funciones defensivas'),
    ('traction_goal', 'en números concretos como cantidad de clientes y tasa de crecimiento mensual'),
    ('equipo_multifuncional_real', 'y elígelo con espíritu emprendedor'),
]
for nid, t in resultantes:
    ok = any(t in p for p in hoy[nid].get('pasos_accionables') or [])
    print('RESULTANTE', nid, '->', 'PRESENTE' if ok else 'AUSENTE')
