# Reporte fix_spiderweb (Fase 1.2)

- Nodos reales: 953
- Enlaces totales: 2402, rotos: 608 (25.3%)
- Fantasmas unicos: 376

## Resolucion por capas
- Capa A (auto, score >= 90): 161 fantasmas, recuperan 305 enlaces
- Capa B (revision, 72-90): 140 fantasmas, afectan 209 enlaces
- Capa C (sin match, < 72): 75 fantasmas, afectan 94 enlaces

## Resultado tras aplicar Capa A (dataset_clean/)
- Enlaces corregidos: 305
- Rotos: 608 -> 303 (12.6%)
- Nodos sin enlaces entrantes: 413 -> 396
