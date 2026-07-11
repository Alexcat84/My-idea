# Expansión v1.3 — reporte de cierre

Fecha: 2026-07-11/12 · Rama: `staging` · Tags: `dataset-v1.3.0`, `pack-digital-v1`,
`pack-export-v1`, `pack-franq-v1` · Ejecución autónoma hasta los gates humanos §7.
Plan operativo: `docs/PLAN_EXPANSION_V1_3_EJECUCION.md` (runbook de Fable +
correcciones verificadas contra código).

## Resultado en una línea

**El universo creció de 2,805 a 3,260 nodos (455 nuevos + 99 core enriquecidos),
con Gate 0 VERDE tras cada libro, vuelo del motor 10/10 sobre el core expandido,
y 3 packs nuevos (427 nodos) saneados con Gate 0 por dominio, esperando los
gates del usuario para integrarse.**

## 1. Extracción (pipeline nuevo, claude-sonnet-5, costo real)

`scripts/pipeline_libros.py` — hereda el motor probado de los packs HSEQ
(reanudable por chunk, reintentos con backoff, colisiones con sufijo) y agrega:
descubrimiento recursivo (books/General tiene 6 subcarpetas temáticas),
etiquetas legibles para fuentes crudas (los NIST y la guía de exportación viajan
con su título real en `fuente`), y conteo de tokens/costo por corrida.

| Grupo | Libros | Nodos crudos | Costo |
|---|---|---|---|
| General (→ core) | Traction, SPIN, Coleman, guía FTC de garantías, Hugos, Horowitz, Co-Intelligence | 580 | $6.2904 |
| seguridad_digital | NIST SP 1300/1314/1318 + Privacy QSG + FTC ciber | 56 | $0.4507 |
| exportacion | A Basic Guide to Exporting (11ª ed.) | 169 | $1.6587 |
| franquicias | Franchise Your Business (Siebert) | 219 | $1.9392 |

## 2. Herramientas construidas (scripts/expansion/ + scripts/)

- `validar_esquema.py` — lista blanca del esquema VIGENTE (verificado contra los
  2805; el runbook citaba campos que no existen), obligatorios no vacíos, ids
  ascii. Atrapó de nacimiento 16 typos `resumen_*teorico` en 3 corridas.
- `censo_colisiones.py` — cada id nuevo contra el censo completo (dataset +
  packs + grupos nuevos); renombra con sufijo de dominio y actualiza refs.
  Colisiones reales: `proteccion_propiedad_intelectual` (×2 packs),
  `coeficiente_viral` (General).
- `enriquecer_vs_crear.py` — la regla madre (§2): embeddings Voyage del mismo
  modelo/dimensión del índice + match léxico → juez Sonnet 5 con el criterio
  "¿el ángulo cambia la acción del emprendedor?" → aplicar con registro
  (`dataset/metadata/enriquecimientos_v13.json`). Nota de diseño: `fuente` se
  mantiene string ("a | b") porque graph.ts la tipa string — el runbook pedía
  lista y eso rompería el contrato web.
- `tejer_ola1.py` — dedup interno por contenido, resolución de aristas contra
  el censo core+General con rematch por bandas (auto ≥0.70 / revisión 0.50-0.70
  juzgada con veredicto+motivo / poda <0.50), y tejido por libro: ≥1 predecesor
  y ≥1 sucesor reales (mejor vecino temático si falta, registrado) + simetría.
- `generar_etiquetas_arbol.py` — el estándar nuevo `etiqueta_arbol` (§1 del
  runbook): 4-5 palabras, segunda persona, cero anglicismos ni autores
  ("Limita Accesos al Mínimo Necesario", "Detecta Ataques a Tiempo"). Campo
  aditivo e inofensivo hoy; la UI lo consumirá cuando se cablee.
- `scripts/hseq/lib_dominio.py` ganó `HSEQ_CATEGORIAS` (env) para apuntar los
  pasos HSEQ a packs nuevos sin re-tocar los HSEQ ya integrados (congelados).

## 3. OLA 1 — el core (INTEGRADA)

Enriquecer-vs-crear sobre los 580 crudos: 549 pares juzgados uno a uno +
31 crear directo → **99 core enriquecidos** (fuente sumada, pasos nuevos no
cubiertos) y 481 a crear; dedup interno fusionó 26 duplicados de chunks
solapados (historia en `merged_originals/`) → **455 nodos nuevos**.

Aristas: 670 refs exactas/alias; 337 fantasmas → 117 auto, 208 juzgados
(114 aprobados / 94 rechazados con motivo), 12+ podados. Total: 356 aristas
redirigidas, 146 podadas.

Tejido libro a libro (orden del runbook), **Gate 0 VERDE tras cada uno**:

| Libro | Nodos tejidos | Conexiones por vecino temático |
|---|---|---|
| Traction | 68 | 17 |
| SPIN Selling | 53 | 14 |
| Never Lose a Customer (Coleman) | 72 | 25 |
| Guía FTC de garantías | 12 | 5 |
| Essentials of Supply Chain (Hugos) | 112 | 34 |
| The Hard Thing (Horowitz) | 90 | 38 |
| Co-Intelligence (Mollick) | 48 | 22 |

Línea de cierre: familias 3260 (clasificador, $0) · caché parcial de preguntas
637 nodos ($0.6473, 3,056 preguntas totales) · índice Voyage completo 3260
(dim 512) · sync con checksums · **suites web 218/218 + python 12/12, también
en clon limpio** · vuelo vivo **10/10** ($0.5569; el motor dio 4 saltos
semánticos donde antes daba 3).

Calibración de la brújula: los 2 casos históricos intactos
(hoja_estimacion_costos 0.3503 pasa / alfabetizacion_materiales 0.2583 fuera,
umbral 0.30) **+ 2 casos nuevos permanentes** (fixture + test):
"no sé qué canal de marketing probar" → `framework_bullseye` 0.58;
"mis entregas llegan tarde y el inventario se acumula" → `gestion_inventario`
0.54. La brújula VE el conocimiento nuevo.

## 4. OLAS 2-4 — packs (SANEADOS, no integrados)

Patrón HSEQ completo por dominio con Gate 0 VERDE:
**seguridad_digital 55 · exportacion 158 · franquicias 214.**
Dedup por contenido con registro commiteado ANTES de fusionar (17 fusiones;
2 rechazos con criterio: Detect≠Protect en el CSF; "velocidad como ventaja" ≠
"crecer despacio al inicio"); rematch de aristas con 29 revisiones a veredicto
y 5 rebinds justificados; cirugía de huérfanos (28 aristas con score);
12 semillas candidatas por pack (provisionales para el Gate; la aprobación
de 5-8 es del usuario) y puentes en lápiz (15/20/20).

Copyright: 3 menciones de success stories limpiadas y **54 punteros
jurisdiccionales** en exportación ("verifica el acuerdo vigente"); punteros de
ley EE.UU. en los 14 nodos FTC; 4 nodos de Co-Intelligence reformulados
herramienta-agnósticos. Registros en `packs/*/metadata/auditoria_copyright.json`
y `dataset/metadata/expansion_v13/`.

## 5. Costos reales de la expansión: ≈ $16.30

| Concepto | Costo |
|---|---|
| Extracción (4 grupos + humo) | $10.35 |
| Etiquetas de árbol (882 nodos) | $1.02 |
| Juez enriquecer-vs-crear (549 pares) | ≈$2.30 (parte de la 1ª corrida murió con la sesión, estimada por proporción) |
| Juez de aristas (208 revisiones) | $0.35 |
| Caché parcial de preguntas (637) | $0.65 |
| Índice Voyage 3260 | ≈$0.01 |
| Vuelo vivo | $0.56 |
| Recuperación de 1 nodo perdido | $0.07 |

## 6. Incidentes y lecciones (todos resueltos, en memoria del agente)

1. **Sonnet 5 trae adaptive thinking por defecto**: `content[0].text` puede ser
   un bloque de thinking y el thinking consume `max_tokens` — dos scripts
   nuevos fallaron en silencio con techos de 3-4K. Cura: extraer el bloque
   `type=="text"` y techos ≥8K (patrón ya presente en pipeline_dominio).
2. **Windows es case-insensitive**: una transliteración ASCII escribió y borró
   el mismo archivo (`coCreacion` → `cocreacion`), perdiendo un nodo. Se
   recuperó re-extrayendo su chunk de origen ($0.07).
3. **Los background mueren con la sesión**: el juez EVC se cortó a medio camino;
   como toda etapa guarda estado tras cada lote, se reanudó sin pérdida.

## 7. Correcciones al runbook (verificadas contra código)

- El esquema vigente usa `titulo_concepto` y `pasos_accionables` (no "titulo"/
  "pasos_practicos"); un validador literal del runbook rechazaría los 2805.
- `familia` no es campo del nodo (vive en `engine/node_families.json`).
- `etiqueta_arbol` no existía: se construyó el script parametrizado y hoy es
  parte del estándar para nodos nuevos.
- `fuente` como lista rompería `graph.ts`; se usa string "a | b".

## 8. Gates pendientes del usuario (§7)

1. **G2** — familia nueva "canales" para los 68 nodos de Traction (hoy en
   familia `general`).
2. **G3** — semillas: aprobar 5-8 de las 12 candidatas por pack
   (`packs/<pack>/metadata/entry_seeds_candidatas.json`).
3. **G4** — puentes: aprobar 10-15 por pack desde `bridges_propuestos.json`
   (regla anti-concentración máx 2-3 por ancla core) → `bridges_aprobados.json`
   con envoltorio `{nota, aprobados}`.
4. **G5** — bautizo del pack de franquicias.
5. Técnica: `integrar_packs.py` hardcodea los 3 packs HSEQ — extenderlo al
   aprobar G3/G4.
6. Merge a main: solo con autorización explícita.


## 9. Addendum — Hygiene v1.3.1 (post-auditoría)

**Hallazgo 1 del auditor (esquema "renegado" en los packs): REFUTADO con censo.**
Los 4,583 nodos del universo (3,260 dataset + 896 quality + 427 packs nuevos)
tienen CERO campos `titulo`; el 100% usa `titulo_concepto`, `pasos_accionables`
y `node_id` interno — uniforme desde el core original hasta los HSEQ integrados.
El chequeo de títulos del Gate 0 por dominio lee `titulo_concepto`
(run_phase1_dominio.py:46) y nunca corrió vacuo: re-corrido con evidencia
(427 títulos, 0 vacíos, 100% únicos por dominio, VERDE). La migración prescrita
a `titulo`/`pasos_practicos` habría roto graph.ts, el motor y run_phase1 —
es el mismo desfase del runbook §1 ya documentado en la sección 7.
**Núcleo válido adoptado:** `engine/test_validador_esquema.py` — garantía
permanente (nodo sintético renegado → exit 1) cableada a run_all_tests.

**Hallazgo 2 (backlog de etiqueta_arbol): LEGÍTIMO y ejecutado.**
Backfill de los 2,805 nodos pre-v1.3 con el script parametrizado: $3.3735
(+$0.0667 de diferenciación). Validación: 0 vacías, 0 >6 palabras; 74 etiquetas
duplicadas entre nodos distintos diferenciadas (72 regeneradas con prohibición
explícita + 2 a mano: "Adopta Cero Defectos como Norma", "Valida que tu
Cliente Compra") → **3,260/3,260 etiquetadas, 0 duplicadas**. Master recompilado
(la etiqueta viaja al grafo compilado), sync con checksums, suites python 13/13
y web 218/218, **clon limpio VERDE**. Commit `fa2e601` ("Hygiene v1.3.1").

Costo total actualizado de la expansión: ≈ **$19.80**.
Merge a main: listo desde el lado técnico; esperando la palabra del usuario,
igual que los gates G2-G5 (curaduría del auditor disponible en la sección 8).
