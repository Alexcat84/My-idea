# Plan de ejecución — EXPANSIÓN v1.3 (cumplimiento del RUNBOOK)

Fecha: 2026-07-11 · Rama: `staging` · Ejecutor: Claude Code (autónomo hasta los
gates humanos §7). Fuente de verdad: `RUNBOOK_EXPANSION_v1_3.md` de Fable +
verificación contra código real (correcciones abajo).

## Estado de partida (extracción cruda YA hecha, una pasada, Sonnet 5)

| Grupo | Nodos crudos | Costo | Destino runbook |
|---|---|---|---|
| books/General (7 libros, 6 temas) | 580 (incl. 1 recuperado tras clobber case-insensitive) | $6.2904 | OLA 1 → core |
| books/seguridad_digital (5 docs NIST/FTC) | 56 | $0.4507 | OLA 2 → packs/seguridad_digital |
| books/exportacion (Basic Guide 11ª) | 169 | $1.6587 | OLA 3 → packs/exportacion |
| books/franquicias (Siebert) | 219 | $1.9392 | OLA 4 → packs/franquicias |

Divergencias asumidas y su cura (aprobadas por el usuario el 2026-07-11:
"la extracción de conocimientos es el mismo... encárgate de todo lo que falta"):
extracción fue en paralelo y en una pasada con aristas-como-ids → se cura con
dedup por contenido + rematch semántico con bandas (paso3b HSEQ), no se re-extrae.

## Correcciones al runbook verificadas contra código (no cambiar)

1. Esquema vigente de los 2805: `node_id, fase_proyecto, dominio,
   titulo_concepto, fuente, resumen_teorico, pasos_accionables,
   entregable_esperado, nodos_previos, nodos_siguientes, condiciones_activacion`.
   El validador usa ESTA lista blanca (no "titulo"/"pasos_practicos").
2. `familia` NO es campo del nodo: la asigna engine/plan_readiness.py
   (engine/node_families.json) post-integración.
3. `etiqueta_arbol` no existe aún: se construye `scripts/generar_etiquetas_arbol.py`
   (parametrizado; reglas de voz: 4-5 palabras, segunda persona, cero
   anglicismos ni autores) y se genera SOLO para nodos nuevos como campo
   adicional inofensivo (nada lo consume todavía; la UI podrá usarlo luego).

## Gates humanos (NO ejecutar sin el usuario — §7)

- G2: familias nuevas (probable "canales" por Traction) → PROPONER al final.
- G3: semillas de cada pack (5-8) → PROPONER con recomendación curada.
- G4: puentes de cada pack → PROPONER en lápiz con curaduría.
- G5: bautizo del pack franquicias ("Seguridad Digital" y "Vender al Mundo" ya
  aprobados como nombres de catálogo).
- Merge a main: solo con autorización explícita (regla de memoria).

## FASES (ejecutar en orden; checkpoint en disco tras cada una)

### F1. Herramientas base (sin API)
- `scripts/expansion/validar_esquema.py`: lista blanca de campos del esquema
  vigente (+ `etiqueta_arbol` opcional), obligatorios no vacíos, ids ascii
  minúscula. Corre sobre books/*/nodos y packs nuevos. Reporta y NO auto-arregla
  (arreglos con script dedicado y registro).
- `scripts/expansion/censo_colisiones.py`: cada id nuevo vs censo completo
  (dataset/nodos 2805 + packs existentes + los otros grupos nuevos). Colisión →
  renombrar con sufijo de dominio (patrón analisis_competitivo_calidad),
  actualizando refs internas del grupo. Registro en <grupo>/metadata/.
- Mover books/<pack>/nodos → packs/<pack>/nodos para los 3 packs (runbook §4)
  y extender scripts/hseq/lib_dominio.py CATEGORIAS con
  {franquicias, exportacion, seguridad_digital}. General se queda en
  books/General/nodos hasta su integración (es core, no pack).

### F2. Saneamiento de packs (OLAS 2-4, patrón HSEQ con scripts/hseq/*)
Por dominio (orden: seguridad_digital, exportacion, franquicias):
paso0 anomalías → paso1 ascii → paso2 dedup por CONTENIDO (registro de
decisiones commiteado ANTES de fusionar; fusiones conservan historia en
merged_originals/) → paso3_4 aristas (resolver refs, fantasmas) → paso3b
rematch semántico con bandas (auto ≥0.70; 0.50-0.70 queda REGISTRADO para
revisión, sin auto-conectar; <0.50 poda) → paso7 huérfanos (cirugía SCC con
mejor vecino temático, registrada) → run_phase1_dominio Gate 0 por dominio
(0 rotas, simetría, títulos únicos, alcanzabilidad desde semillas provisionales).
- Auditoría copyright exportación: detectar y podar nodos derivados de
  success stories / material de terceros; agregar puntero jurisdiccional
  ("verifica el acuerdo vigente") a nodos de tratados/aranceles/regulación.
  Registro en packs/exportacion/metadata/auditoria_copyright.json.
- paso5_6: candidatas a semillas (5-8) y puentes en lápiz → SOLO PROPUESTA.

### F3. OLA 1 — enriquecer-vs-crear contra el core (books/General)
- Embeddings Voyage (voyage-4-lite, dim 512, mismo modelo del índice) de los
  nodos nuevos; comparación coseno contra web/lib/assets/semantic_index.json
  (2805) + match léxico (norm_titulo / ids).
- Bandas: score ≥0.80 y mismo concepto → ENRIQUECER (fuente pasa a lista,
  mejores pasos_accionables si aplica; el nodo core conserva id e historia);
  0.60-0.80 → juez Sonnet 5 con el criterio §2 ("¿el ángulo cambia la acción
  del emprendedor?") → enriquecer o crear; <0.60 → CREAR.
- Registro: dataset/metadata/enriquecimientos_v13.json (id, libro, qué aportó,
  score, decisión). Meta: 60-140 nuevos por libro (Traction hasta 180) —
  verificar densidad, no forzar.
- Auditoría Co-Intelligence: pasos herramienta-agnósticos (pasada de revisión).
- FTC garantías: puntero jurisdiccional (ley EE.UU.) en sus nodos.
- Dedup interno de General + aristas + rematch como en F2 (mismas bandas).

### F4. etiqueta_arbol (script nuevo, parametrizado)
- `scripts/generar_etiquetas_arbol.py --carpeta <dir>`: Sonnet 5 en lotes,
  reglas de voz (4-5 palabras, segunda persona, sin anglicismos/autores),
  valida longitud y ascii, reintenta las que fallen. Genera para TODOS los
  nodos nuevos (General post-dedup + 3 packs post-saneamiento).

### F5. Integración OLA 1 al core (libro a libro, orden runbook)
Orden: Traction → SPIN → Coleman(+FTC) → Hugos → Horowitz → Co-Intelligence.
Por libro: copiar sus nodos (los CREAR) a dataset/nodos + aplicar
enriquecimientos a nodos core existentes + tejer (≥1 predecesor y ≥1 sucesor
dentro del core real, sin islas) + run_phase1 Gate 0 VERDE antes del
siguiente libro. Familias del catálogo vigente vía plan_readiness (si un
libro exige familia nueva → detener ese punto y PROPONER, gate G2).
Semillas core NO cambian.
- Tras el último libro: caché parcial de preguntas (nodos nuevos + cores con
  sucesores cambiados, --patch-file), plan_readiness, índice Voyage completo,
  sync_assets_web, suites web+python, 3 casos de calibración de brújula
  (hoja_estimacion_costos pasa / alfabetizacion_materiales fuera / + 1 caso
  nuevo por libro grande), vuelo vivo, clon limpio.
- Tag: dataset-v1.3.0. Commits "Expansion v1.3:". Push staging (autopush).

### F6. Cierre y reporte
- Conteos A MANO antes de los asserts (regla AGENTS.md).
- Tags pack-digital-v1, pack-export-v1, pack-franq-v1 (packs saneados,
  pendientes de integración hasta gates G3-G5).
- Reporte final: nodos por destino, enriquecimientos, podas de copyright,
  costos reales por fase, y la lista de decisiones del usuario (G2-G5).

## Estado de ejecución (actualizar aquí al completar cada fase)
- [x] F1 herramientas + movida a packs/ (esquema 0 fallas, colisiones: 2 packs + 1 general renombradas)
- [x] F2 seguridad_digital saneado — Gate 0 VERDE (55 nodos)
- [x] F2 exportacion saneado — Gate 0 VERDE (158) + copyright (3 scrubs, 54 punteros)
- [x] F2 franquicias saneado — Gate 0 VERDE (214); etiquetas packs 426/427 ($0.65)
- [ ] F3 enriquecer-vs-crear General
- [ ] F4 etiquetas de árbol
- [ ] F5 integración OLA 1 (6 libros, Gate 0 entre libros) + línea completa + tag
- [ ] F6 reporte
