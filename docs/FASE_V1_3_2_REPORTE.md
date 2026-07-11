# Fase v1.3.2 — tres mundos nuevos: reporte de cierre

Fecha: 2026-07-11 · Rama: `staging` · Commits: `834809c` (curaduría),
`0c68aed` (integración) · Tag: `web-v0.6.0` (al cerrar el vuelo).
Merge a main: **queda para después de la auditoría** (palabra del usuario).

## Resultado en una línea

**Los 3 packs saneados de la Expansión v1.3 (seguridad_digital 55,
exportacion 158, franquicias 214) están integrados al universo recorrible
— master 3,687 nodos, Gate 0 VERDE, 35 puentes curados a mano — y la web
conoce 6 mundos (contrato, catálogo, brecha, murallas), con la migración
017 lista para pegar.**

## 1. Semillas (patch del usuario, verbatim)

`packs/<pack>/metadata/entry_seeds.json`: 6/7/7 semillas aprobadas.
Verificación previa: las 20 existen como nodos de su pack; Gate 0 por
dominio re-corrido VERDE con las definitivas.

## 2. Curaduría de puentes (la parte que va con lupa)

**Hallazgo estructural**: 37/55 propuestas de `bridges_propuestos.json`
tenían el ancla en OTRO pack (quality/health_safety), no en core —
seguridad_digital 15/15, exportacion 14/20, franquicias 8/20. Un puente
pack→pack queda muerto tras las murallas de dominio (el ancla se filtra si
ese otro mundo no está desbloqueado); el patrón de la Fase 3.5 es
core↔dominio. Se rechazaron en bloque y se regeneraron candidatos con el
mismo método (embeddings multilingual-MiniLM sobre título+resumen)
restringido a anclas `dominio=core` — que ahora incluye los 455 de OLA 1,
mejores anclas que las de 2805 (p.ej. Traction, SPIN, Hugos anclan
naturalmente a los mundos nuevos).

Curaduría sobre los candidatos core-only (30 por pack + profundidad extra
en seguridad_digital), leyendo `resumen_teorico` en los pares ambiguos:

| Pack | Aprobados | Rechazos con nota | Trampas típicas rechazadas |
|---|---|---|---|
| seguridad_digital | 12 | 20 | homónimos riesgo/monitoreo/sistema/evaluación (métricas de retención ≠ postura de seguridad; Mollick "sistemas sabios" ≠ authorization boundary) |
| exportacion | 10 | 20 | homónimos investigación/cultura (SPIN research ≠ estudio de mercado; cultura interna ≠ interculturalidad); dirección invertida (proveedores vs compradores) |
| franquicias | 13 | 17 | ancla-imán `gestion_contratos_desempeno` (score 0.876, el máximo del pool, par absurdo); homónimo exit/venta (salida de fundadores ≠ vender franquicias) |

Reglas aplicadas: máx 2-3 por ancla core (tope real usado: 2), cero
redundantes (un destino no acumula puentes que enseñan lo mismo). Registro
completo con motivo por rechazo en `packs/<pack>/metadata/bridges_curaduria.json`,
commiteado ANTES de fusionar (regla del runbook). Total tejido: **35 puentes
bidireccionales sobre 29 anclas core**.

## 3. Línea de ensamblaje (integrar_packs.py GENERALIZADO)

`scripts/integrar_packs.py` ya no hardcodea packs: descubre `packs/*/nodos`
y separa integrados (todos sus nodos ya viven en `dataset/nodos/` — los
HSEQ, congelados) de pendientes; estado parcial = error. También se curó
la trampa Windows de `pnpm` en subprocess (`shutil.which`).
`run_phase1.py`: `DOMINIOS_PERMITIDOS` ampliado a 7 (core + 6 packs).

Corrida real: 427 nodos copiados + 35 puentes → master **3,687**
(1,721 core + 896 quality + 332 health_safety + 311 environmental +
214 franquicias + 158 exportacion + 55 seguridad_digital) → Gate 0 VERDE →
familias (gratis) → caché parcial 456 nodos (401 parchados, 55 hojas sin
sucesores, **$0.3826**) → índice Voyage completo 3,687 (~561K tokens,
calibración de brújula intacta: hoja_estimacion 0.3514 pasa /
alfabetización 0.2583 fuera, umbral 0.30) → sync con checksums.

## 4. Cableado web a 6 mundos

- **Migración 017** (`my_idea_017_mundos_nuevos.sql`): los 4 CHECK de
  dominio a 6 packs. Nombres verificados dos veces: contra las migraciones
  fuente (016 nombra `sessions/plans_dominio_check`; los inline de 014/016
  generan `pack_clicks_pack_check`/`project_unlocks_dominio_check`) y
  contra la base viva (un insert de sonda devolvió 23514 nombrando
  `pack_clicks_pack_check`). DROP/ADD van como sentencias separadas para
  que `dbContract.test.ts` parsee el CHECK vigente. Bloque 017 añadido a
  `my_idea_check_migraciones.sql` (paste-and-run).
- **dbContract.ts**: `PACK_CLICKS_PACK` a 6 → `DOMINIOS` a 7; el test del
  contrato pasa contra la 017.
- **packs_catalog.json**: 6 mundos, bautizos y promesas del usuario
  verbatim ("Seguridad Digital", "Vender al Mundo", "Multiplica tu
  Negocio").
- **packs_entry_seeds.json**: semillas de los 3 packs horneadas
  (id/título/fase/condiciones desde los nodos reales).
- **brecha_semillas.json** (asset nuevo): el mapeo determinístico
  fase→semilla del usuario, verbatim, con una corrección documentada: el
  patch usaba fases `construccion/operacion/crecimiento` que no existen en
  el canon (ideacion/validacion/planificacion/ejecucion). Se añadieron
  alias `planificacion`/`ejecucion` con el mismo valor — verificado contra
  la fase real de los nodos: los de "construccion" son planificacion y los
  de "operacion" son ejecucion. `crecimiento` queda para el futuro.
  `evaluacionBrecha` consulta el mapa primero (los HSEQ no están en él y
  conservan el puntaje dinámico); si la semilla mapeada ya está cubierta,
  cae al puntaje clásico. Tests nuevos cubren las decisiones de producto
  (exportación ideación=validación por mercados objetivo; franquicias
  validación por "prueba que UNA funciona").
- **ideas.ts / graph.test.ts**: nombres de mundo y muralla probada para
  los 6 dominios.

## 5. Vuelo v1.3.2 (fase 2g-bis de vuelo.ts)

Murallas negativas de exportacion/franquicias (403 sin unlock) + ciclo
positivo completo de seguridad_digital (unlock → start con semilla del
mapeo → turnos → plan dominio=seguridad_digital → checklist agrupado) +
captura de la fila de 6 potenciadores (capturas.ts, /potenciadores).
**Prerrequisito**: migración 017 aplicada — el sondeo confirmó que aún no
lo está. Resultado del vuelo: ver addendum al cierre.

## 6. Costos reales de la fase

| Concepto | Costo |
|---|---|
| Caché parcial de preguntas (456 nodos, haiku) | $0.3826 |
| Índice Voyage 3,687 (~561K tokens) | ≈$0.01 |
| Vuelo vivo (addendum al cierre) | pendiente |

## 7. Suites

Web 220/220 (28 archivos; +2 tests de brecha, muralla ×6, grafo 3,687) ·
python 13/13 · clon limpio: ver addendum al cierre.
