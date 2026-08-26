"""VUELTA 75, OP-E-01, PASO 3: lee el contenido completo de la madre y del
hijo candidato para los primeros N pares sin arista de PASO_NODO_CALIBRADO.jsonl,
para la lectura par a par (vara 9.6.1 / 9.6.2 / 9.6.3 del banco). Solo lee."""
import json
import sys

N = int(sys.argv[1]) if len(sys.argv) > 1 else 25

with open('docs/plan/PASO_NODO_CALIBRADO.jsonl', encoding='utf-8') as f:
    lines = [json.loads(l) for l in f if l.strip()]
sin_arista = [l for l in lines if l['arista'] is False]

def cargar(node_id):
    try:
        with open(f'dataset/nodos/{node_id}.json', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return None

for i, l in enumerate(sin_arista[:N]):
    print('='*100)
    print(f"PAR {i} | dominio {l['dominio']}")
    madre = cargar(l['madre'])
    hijo = cargar(l['hijo'])
    print(f"MADRE {l['madre']} ({len(madre['pasos_accionables'])} pasos) | siguientes ya escritos: {madre.get('nodos_siguientes')}")
    print(f"  paso {l['paso']}: {l['texto_paso']}")
    print(f"HIJO candidato {l['hijo']} | titulo: {hijo['titulo_concepto']}")
    print(f"  resumen: {hijo.get('resumen_teorico','')[:300]}")
    print(f"  pasos ({len(hijo['pasos_accionables'])}):")
    for j, p in enumerate(hijo['pasos_accionables']):
        print(f"    {j+1}. {p}")
    print(f"  hijo.nodos_previos ya escritos: {hijo.get('nodos_previos')}")
    print()
