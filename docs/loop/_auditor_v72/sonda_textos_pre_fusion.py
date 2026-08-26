# Sonda del auditor de la vuelta 72: textos pre fusion del lote H (SIN razones),
# para la relectura ciega. Lee el grafo en c4c38956 (el commit del plan, PRE
# fusion) y escribe titulo, resumen, pasos y condiciones de los 15 nodos.
import json, subprocess, io

raw = subprocess.run(['git', 'show', 'c4c38956:dataset/metadata/master_graph.json'],
                     capture_output=True, text=True, encoding='utf-8').stdout
g = json.loads(raw)['nodos']

actos = {
    43: ['preservar_efectivo_buscar_modelo', 'escalamiento_prematuro', 'restriccion_gasto_validacion'],
    44: ['evaluacion_tecnologias_disruptivas', 'explotacion_tecnologias_disruptivas', 'tecnologias_disruptivas_oportunidad'],
    45: ['reconstruccion_contexto_situacional', 'evitar_sesgo_retrospectivo_hindsight', 'evitar_shopping_bag'],
    46: ['mitigacion_riesgos_ambientales', 'gestion_eco_riesgos', 'responsabilidad_extendida_productor'],
    47: ['gestion_terminacion_franquiciado', 'perdida_control_operativo', 'terminacion_franquiciado_causas'],
}

out = io.StringIO()
for a, miembros in actos.items():
    out.write('\n===== ACTO %d =====\n' % a)
    for m in sorted(miembros):
        n = g[m]
        out.write('\n--- %s (dominio %s, fase %s) ---\n' % (m, n.get('dominio'), n.get('fase_proyecto')))
        out.write('TITULO: %s\n' % n.get('titulo_concepto'))
        out.write('FUENTE: %s\n' % n.get('fuente'))
        out.write('RESUMEN: %s\n' % (n.get('resumen_teorico') or '')[:700])
        for i, p in enumerate(n.get('pasos_accionables') or [], 1):
            out.write('  paso %d: %s\n' % (i, p))
        for i, c in enumerate(n.get('condiciones_activacion') or [], 1):
            out.write('  cond %d: %s\n' % (i, c))

open('docs/loop/_auditor_v72/TEXTOS_PRE_FUSION_LOTE_H.txt', 'w', encoding='utf-8').write(out.getvalue())
print('escrito', len(out.getvalue()), 'caracteres')
