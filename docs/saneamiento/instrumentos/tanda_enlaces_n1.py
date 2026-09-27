# -*- coding: utf-8 -*-
"""Nivel 1, criterio 10 (decision del fundador del 27 sep 2026): los enlaces que el comprobador dio por rotos o sin
respuesta, revisados a mano el 27 sep 2026 con un navegador (curl con agente de navegador, DNS y el archivo de Internet):
  - Half.com: no es un enlace, es un ejemplo historico de truco de prensa (renombrar un pueblo); se queda.
  - dominio.com: no es un enlace, es el marcador del operador de busqueda "site:"; se queda.
  - NIST.gov/CyberFramework: responde 200 (el fallo era del certificado local); se queda.
  - www.fas.usda.gov: vivo; solo rechaza a los robots (403 en la red de su CDN), el DNS resuelve y el archivo de Internet
    lo captura con 200 en 2026; se queda.
  - TrafficEstimate.com: el dominio es hoy de otro sitio sin relacion; SALE del paso.
  - ecertify.com: redirige a otra empresa (esscert.com); SALE la marca, queda "un proveedor privado".
  - bis.doc.gov: se mudo a bis.gov; se ACTUALIZA.
  - otexa.ita.doc.gov: ya no resuelve; OTEXA vive en www.trade.gov/otexa (200); se ACTUALIZA.
Uso: python tanda_enlaces_n1.py <repo>"""
import io
import json
import os
import sys

os.chdir(sys.argv[1])
EV = 'Comprobador de enlaces (docs/saneamiento/ENLACES.md) y revision a mano del 27 sep 2026: '
CAMBIOS = [
    ('medicion_resultados_marketing_franquicia', 'pasos_accionables', 2, 'TrafficEstimate.com, ', '', 'TrafficEstimate.com es hoy un dominio de otro sitio sin relacion.'),
    ('reglas_origen_sectoriales', 'pasos_accionables', 1, 'otexa.ita.doc.gov', 'www.trade.gov/otexa', 'otexa.ita.doc.gov ya no resuelve; OTEXA esta en www.trade.gov/otexa (responde 200).'),
    ('licencia_exportacion_regulaciones', 'pasos_accionables', 0, 'bis.doc.gov', 'bis.gov', 'bis.doc.gov redirige a bis.gov.'),
    ('licencia_exportacion_regulaciones', 'pasos_accionables', 2, 'bis.doc.gov', 'bis.gov', 'bis.doc.gov redirige a bis.gov.'),
    ('certificados_genericos_de_origen', 'resumen_teorico', None, 'proveedores privados como ecertify.com', 'proveedores privados', 'ecertify.com redirige a otra empresa (esscert.com).'),
    ('certificados_genericos_de_origen', 'pasos_accionables', 1, 'un proveedor privado (ej. ecertify.com)', 'un proveedor privado', 'ecertify.com redirige a otra empresa (esscert.com).'),
]
tanda = []
for nid, campo, i, viejo, nuevo, evid in CAMBIOS:
    n = json.load(io.open('dataset/nodos/%s.json' % nid, encoding='utf-8'))
    antes = n[campo][i] if i is not None else n[campo]
    assert viejo in antes, (nid, campo, viejo)
    despues = antes.replace(viejo, nuevo)
    c = {'id': 'n1-enlace-%d' % (len(tanda) + 1), 'node_id': nid, 'campo': campo, 'veredicto': 'VIGENCIA', 'texto_anterior': antes,
         'texto_nuevo': despues, 'cita': {'instrumento': 'Comprobador de enlaces del saneamiento', 'evidencia': EV + evid},
         'decision': 'Saneamiento del dataset, nivel 1 (decision del fundador del 27 sep 2026), criterio 10: los enlaces rotos, corregidos o retirados.',
         'fecha': '2026-09-27'}
    if i is not None:
        c['indice'] = i
    tanda.append(c)
json.dump(tanda, io.open('docs/saneamiento/tandas/saneamiento-n1-enlaces.json', 'w', encoding='utf-8', newline='\n'), ensure_ascii=False, indent=1)
print('correcciones', len(tanda))
