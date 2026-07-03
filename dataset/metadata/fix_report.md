# Reporte fix_spiderweb (Fase 1.2)

- Nodos reales: 958
- Enlaces totales: 3223, rotos: 415 (12.9%)
- Fantasmas unicos: 229

## Resolucion por capas
- Capa A (auto, score >= 90): 13 fantasmas, recuperan 86 enlaces
- Capa B (revision, 72-90): 141 fantasmas, afectan 235 enlaces
- Capa C (sin match, < 72): 75 fantasmas, afectan 94 enlaces

## Resultado tras aplicar Capa A (dataset_clean/)
- Enlaces corregidos: 86
- Rotos: 415 -> 329 (10.2%)
- Nodos sin enlaces entrantes: 12 -> 12
