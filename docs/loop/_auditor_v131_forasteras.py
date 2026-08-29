# AUDITOR v131: los CUATRO de la BOLSA 2, se reconstruye su titulo completo
# desde docs/ (fuera del dataset)? El reporte afirma en su discutible 2 que los
# dos titulos 'solo viven en esa prosa de commit, ningun fichero de la campana
# los usa'. Esto lo mide. Salida: docs/loop/_auditor_v131_forasteras.txt
import os, re
SONDAS = {
  "Juran's Quality Handbook_ The C - Joseph A. Defeo": "Juran's Quality Handbook",
  'The Green to Gold Business Play - Daniel C. Esty': 'Green to Gold Business Play',
  'Managing the Risks of Organizat - Reason, J. T_': 'Managing the Risks of Organizat',
  'Co-Intelligence_ Living and Wor - Ethan Mollick': 'Co-Intelligence',
}
BS = chr(92)
COLA = '[^' + chr(92) + 'n|"]{0,60}'   # hasta 60 chars sin salto, sin pipe y sin comilla
for grafia, sonda in SONDAS.items():
    hits = {}
    for dp, _, fns in os.walk('docs'):
        for fn in fns:
            p = os.path.join(dp, fn)
            try:
                t = open(p, encoding='utf-8', errors='replace').read()
            except Exception:
                continue
            for m in re.finditer(re.escape(sonda) + COLA, t):
                s = m.group(0).strip()
                if len(s) > len(sonda):
                    hits.setdefault(s, set()).add(p)
    print('=== ' + repr(grafia))
    print('    sonda ' + repr(sonda) + ': %d continuaciones distintas en docs/' % len(hits))
    for s, ps in sorted(hits.items(), key=lambda kv: -len(kv[1]))[:5]:
        fuera = [p for p in ps if 'loop' not in p.replace(BS, '/').split('/')]
        print('      [%3d fich, %d fuera de docs/loop] %r' % (len(ps), len(fuera), s))
        if fuera:
            print('           ej: ' + fuera[0])
    print()
