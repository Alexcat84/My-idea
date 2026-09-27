# -*- coding: utf-8 -*-
"""COMPROBADOR DE ENLACES del catalogo (decision del fundador, 26 sep 2026, saneamiento tanda 1, punto 4).

Saca de los nodos VIVOS (titulo, resumen, pasos, entregable, condiciones) cada URL o dominio citado como recurso,
lo pide por HTTP (HEAD y, si el servidor no lo admite, GET; siguiendo redirecciones, 20 s de espera) y escribe su
informe. Solo lee el dataset; no corrige nada.

    python scripts/saneamiento/comprobar_enlaces.py            # escribe docs/saneamiento/ENLACES.md y .json

Estados: VIVO (2xx), REDIRIGE (acaba en otro dominio), ROTO (4xx o 5xx), NO_RESPONDE (sin respuesta o error de red).
"""
import datetime
import glob
import io
import json
import os
import re
import ssl
import sys
import urllib.error
import urllib.request
from urllib.parse import urlparse

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SALIDA_MD = os.path.join(RAIZ, 'docs', 'saneamiento', 'ENLACES.md')
SALIDA_JSON = os.path.join(RAIZ, 'docs', 'saneamiento', 'ENLACES.json')
RX = re.compile(r'(?:https?://)?(?:www\.)?(?:[a-z0-9-]+\.)+(?:gov|org|com|int|net|edu|mx|es|co|eu|io|uk|ca)(?:/[^\s),;"\']*)?', re.I)
NO_SON = {'e.g', 'i.e'}


def enlaces_de(texto):
    salida = []
    for m in RX.finditer(texto):
        e = m.group(0).rstrip('.')
        if e.lower() in NO_SON or '@' in texto[max(0, m.start() - 1):m.start()]:
            continue
        salida.append(e)
    return salida


def pedir(url):
    if not url.lower().startswith('http'):
        url = 'https://' + url
    ctx = ssl.create_default_context()
    cabeceras = {'User-Agent': 'Mozilla/5.0 (My-idea comprobador de enlaces)'}
    for metodo in ('HEAD', 'GET'):
        try:
            req = urllib.request.Request(url, method=metodo, headers=cabeceras)
            with urllib.request.urlopen(req, timeout=20, context=ctx) as r:
                return r.status, r.geturl()
        except urllib.error.HTTPError as e:
            if metodo == 'HEAD' and e.code in (403, 405, 400, 501):
                continue
            return e.code, url
        except Exception as e:  # red, certificado, tiempo
            if metodo == 'HEAD':
                continue
            return None, str(e)[:120]
    return None, 'sin respuesta'


def main():
    usos = {}
    for p in sorted(glob.glob(os.path.join(RAIZ, 'dataset', 'nodos', '*.json'))):
        n = json.load(io.open(p, encoding='utf-8'))
        if n.get('deprecado'):
            continue
        campos = [n.get('titulo_concepto', ''), n.get('resumen_teorico', ''), n.get('entregable_esperado', '')]
        campos += n.get('pasos_accionables') or []
        campos += n.get('condiciones_activacion') or []
        for e in enlaces_de('\n'.join(campos)):
            usos.setdefault(e, set()).add(n['node_id'])
    filas = []
    for e in sorted(usos):
        codigo, final = pedir(e)
        origen = urlparse(e if e.lower().startswith('http') else 'https://' + e).netloc.lower().replace('www.', '')
        destino = urlparse(final).netloc.lower().replace('www.', '') if final.startswith('http') else ''
        if codigo is None:
            estado = 'NO_RESPONDE'
        elif codigo >= 400:
            estado = 'ROTO'
        elif destino and destino != origen and not destino.endswith('.' + origen):
            estado = 'REDIRIGE'
        else:
            estado = 'VIVO'
        filas.append({'enlace': e, 'estado': estado, 'codigo': codigo, 'final': final, 'nodos': sorted(usos[e])})
        print('%-12s %-4s %s' % (estado, codigo or '-', e), flush=True)
    hoy = datetime.date.today().isoformat()
    json.dump({'fecha': hoy, 'enlaces': filas}, io.open(SALIDA_JSON, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    cuenta = {}
    for f in filas:
        cuenta[f['estado']] = cuenta.get(f['estado'], 0) + 1
    lineas = ['# ENLACES DEL CATALOGO: INFORME DEL COMPROBADOR (%s)' % hoy, '',
              '*Generado por `scripts/saneamiento/comprobar_enlaces.py` (decision del fundador, 26 sep 2026). Solo lee el '
              'dataset; los enlaces rotos se corrigen aparte, por correccion declarada.*', '',
              '**%d enlaces distintos** en los nodos vivos: %s.' % (len(filas), ', '.join('%s %d' % (k, v) for k, v in sorted(cuenta.items()))), '',
              '| estado | codigo | enlace | acaba en | nodos |', '|---|---|---|---|---|']
    for f in filas:
        lineas.append('| %s | %s | `%s` | %s | %s |' % (f['estado'], f['codigo'] or '-', f['enlace'],
                                                     f['final'] if f['estado'] != 'VIVO' else '', ', '.join('`%s`' % x for x in f['nodos'])))
    io.open(SALIDA_MD, 'w', encoding='utf-8', newline='\n').write('\n'.join(lineas) + '\n')
    print('informe:', os.path.relpath(SALIDA_MD, RAIZ), cuenta)
    return 0


if __name__ == '__main__':
    sys.exit(main())
