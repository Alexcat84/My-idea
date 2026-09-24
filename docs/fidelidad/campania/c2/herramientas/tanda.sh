#!/usr/bin/env bash
# Uso: bash tanda.sh <bloque> <tanda_id> <repetidos.output|->
# Arma la tanda del bloque, la valida, comprueba las citas literales, la aplica y corre el ciclo de Gate 0 y las suites.
# No commitea: eso lo hace la sesion a la vista del resultado.
set -e
B="$1"; T="$2"; REP="$3"
S="$(cd "$(dirname "$0")" && pwd)"
C=/c/Users/AlexDesk/Documents/my-idea-correcciones
cd "$C"
PYTHONIOENCODING=utf-8 python "$S/armar_tanda.py" "$S/c2/decision/$B.json" "$REP" "$C" "$T" 2026-09-24 "docs/fidelidad/tandas/$T.json" "$S/c2/decision/${B}_excepciones_tanda.json"
python scripts/fidelidad/aplicar_correcciones.py "docs/fidelidad/tandas/$T.json" --comprobar
PYTHONIOENCODING=utf-8 python - "docs/fidelidad/tandas/$T.json" <<'EOF'
import json, io, re, sys, unicodedata
def norm(s):
    s = unicodedata.normalize('NFKC', s)
    for a, b in ((chr(0x2019), "'"), (chr(0x2018), "'"), (chr(0x201c), '"'), (chr(0x201d), '"'), (chr(0x2014), '--'), (chr(0x2013), '-'), (chr(0x2011), '-'), (chr(0x2010), '-')):
        s = s.replace(a, b)
    s = re.sub(r'(?<=[a-z\.])\d{1,2}(?= [A-Z])', '', s)
    s = s.replace("'", '"')
    return ' '.join(s.split()).lower()
T = json.load(io.open(sys.argv[1], encoding='utf-8')); cache = {}; mal = 0
for c in T:
    f = c['cita']['fichero'] if ':' in c['cita']['fichero'] else 'C:/Users/AlexDesk/Documents/' + c['cita']['fichero']
    if f not in cache:
        cache[f] = norm(io.open(f, encoding='utf-8', errors='replace').read())
    tr = [t.strip(' "') for t in re.split(r' / |\[\.\.\.\]|\.\.\.|' + chr(0x2026), re.sub(r'\(L\d+[^)]*\)', ' ', c['cita']['frase'])) if len(t.strip(' "')) > 8]
    if not tr or not all(norm(t) in cache[f] for t in tr):
        mal += 1; print('NO LITERAL', c['id'], c['cita']['frase'][:120])
print('%d de %d citas literales; %d sugerencias' % (len(T) - mal, len(T), sum(1 for c in T if c['texto_nuevo'].startswith('Sugerencia de My Idea'))))
sys.exit(1 if mal else 0)
EOF
python scripts/fidelidad/aplicar_correcciones.py "docs/fidelidad/tandas/$T.json"
bash /tmp/ciclo_gate.sh 2>&1 | head -3
cat "$S/c2/decision/${B}_excepciones_tanda.json" | head -20
