# Sonda del auditor v72: delta de la cola de costuras nodo a nodo (antes por
# git show sobre c4c38956, el commit del plan) y conteo grupos/nodos de las
# duplicadas en la apertura (1dd2cccd) y al cierre. Solo lee.
import json, subprocess


def leer_jsonl(texto):
    return [json.loads(l) for l in texto.splitlines() if l.strip()]


def git_show(ref):
    r = subprocess.run(['git', 'show', ref], capture_output=True, text=True, encoding='utf-8')
    if r.returncode:
        raise SystemExit('git show fallo: %s' % ref)
    return r.stdout


cola_antes = {c['node_id'] for c in leer_jsonl(git_show('c4c38956:docs/COSTURAS_INTERNAS.jsonl'))}
cola_ahora = {c['node_id'] for c in leer_jsonl(open('docs/COSTURAS_INTERNAS.jsonl', encoding='utf-8').read())}
print('cola antes (c4c38956):', len(cola_antes))
print('cola despues (hoy)   :', len(cola_ahora))
print('ENTRAN (%d):' % len(cola_ahora - cola_antes))
for n in sorted(cola_ahora - cola_antes):
    print('   ', n)
print('SALEN (%d):' % len(cola_antes - cola_ahora))
for n in sorted(cola_antes - cola_ahora):
    print('   ', n)

for etiqueta, ref in [('apertura 1dd2cccd', '1dd2cccd:docs/plan/ARISTAS_DUPLICADAS.jsonl'), ('cierre hoy', None)]:
    filas = leer_jsonl(git_show(ref)) if ref else leer_jsonl(open('docs/plan/ARISTAS_DUPLICADAS.jsonl', encoding='utf-8').read())
    grupos = {(f['nodo'], f['campo'], f['destino']) for f in filas}
    nodos = {f['nodo'] for f in filas}
    print('\nduplicadas %s: grupos %d | nodos %d' % (etiqueta, len(grupos), len(nodos)))

# y la cola en la apertura de la vuelta (1dd2cccd), que la TAREA 1 no debio mover
cola_1dd = {c['node_id'] for c in leer_jsonl(git_show('1dd2cccd:docs/COSTURAS_INTERNAS.jsonl'))}
print('\ncola en 1dd2cccd:', len(cola_1dd), '| identica a c4c38956:', cola_1dd == cola_antes)
