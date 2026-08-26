"""VUELTA 75, OP-E-01: lista los primeros N candidatos sin arista de
PASO_NODO_CALIBRADO.jsonl, en el orden del archivo (sin recorte a mano),
para leerlos uno a uno. Solo lee, no escribe nada."""
import json
import sys

N = int(sys.argv[1]) if len(sys.argv) > 1 else 20

with open('docs/plan/PASO_NODO_CALIBRADO.jsonl', encoding='utf-8') as f:
    lines = [json.loads(l) for l in f if l.strip()]

sin_arista = [l for l in lines if l['arista'] is False]
print('total bolsa reducida (575):', len(lines))
print('total sin arista (esperado 477):', len(sin_arista))
print()
for i, l in enumerate(sin_arista[:N]):
    print(f"--- {i} | {l['dominio']} | familia_paso={l['familia_paso']} familia_hijo={l['familia_hijo']}")
    print(f"madre: {l['madre']} paso {l['paso']}: {l['texto_paso']}")
    print(f"hijo candidato: {l['hijo']} | titulo: {l['titulo_hijo']}")
    print()
