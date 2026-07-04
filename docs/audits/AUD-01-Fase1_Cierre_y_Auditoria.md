# Auditoría de Cierre — Fase 1: Saneamiento del Grafo de Conocimiento

**Estado: Fase 1 cerrada oficialmente. Auditoría Fase 1.6: APROBADA.**

Este documento registra el trabajo de saneamiento del dataset (`dataset/nodos/`) realizado en la rama `staging`, y la auditoría independiente que lo verificó. Dos partes trabajaron en esto: **Claude (Sonnet 5)** ejecutó el diagnóstico, el pipeline y las fusiones semánticas; **Fable** auditó de forma independiente cada entrega, incluyendo un detector de strings propio para revisar la calidad de la síntesis.

---

## 1. El viaje completo

| | Antes | Después |
|---|---|---|
| Nodos | 953 (con inconsistencias entre disco y `master_graph.json`) | **908** |
| Enlaces rotos | 608 (~25%) | **0** |
| Islas / componentes desconectados | 40 | **1** (100% navegable) |
| Nodos inalcanzables | 413 | **0** |
| Duplicados fósiles / semánticos | ~70 | **0** |
| Nombres de archivo no-ASCII | 12 | **0** |
| Pipeline | scripts sueltos, rutas absolutas de Windows, no reproducibles | `scripts/run_phase1.py` único, idempotente, rutas relativas, validador con `exit code` |

Las cifras de la fila "Antes" corresponden a la auditoría externa de cierre (Fable) sobre el estado original completo del dataset. La primera auditoría propia (Claude), hecha sobre el estado del repositorio al inicio de este trabajo, midió 415 enlaces rotos y 12 archivos no-ASCII sobre 958/953 nodos — un punto de partida distinto porque ya reflejaba una corrida parcial y con errores de un pipeline anterior (`phase1_1_ascii.py`, `phase1_5_merge.py`, etc.). Ambas mediciones describen el mismo problema de fondo desde dos observaciones en el tiempo; se documentan las dos para no perder trazabilidad.

---

## 2. Trabajo de Claude (Sonnet 5) — qué se hizo y en qué commits

### 2.1 Gate 0 — enlaces, nombres, compilación (`d73d75b`, `ed26296`, `5ce0c9a`)
- `scripts/run_phase1.py`: orquestador único con rutas relativas (`pathlib`), reemplazando los scripts de un solo uso (archivados en `scripts/archive/`).
- Normalización ASCII de nombres de archivo (NFKD + eliminación de marcas combinantes: `ñ` → `n`, `á` → `a`), con detección de colisiones en vez de renombrado ciego con sufijo.
- Redirección de referencias a nodos fusionados por el script histórico `phase1_5_merge.py`, que nunca había redirigido lo que fusionaba.
- Aplicación de los alias maps pendientes (capa B, capa C, auto) con resolución encadenada.
- Limpieza de referencias rotas sin resolver, con log de cada eliminación.
- Recompilación de `dataset/metadata/master_graph.json` desde disco (índice por fase, estadísticas de conectividad).
- Eliminación de una carpeta anidada `dataset/nodos/nodos/` con 958 archivos duplicados, artefacto de un commit anterior — confirmado con el usuario antes de borrar.
- Eliminación de 12 duplicados fósiles verificados programáticamente (mismo `titulo_concepto`, contenido idéntico, cero referencias entrantes/salientes únicas).
- Validador Gate 0 integrado: enlaces rotos, nombres no-ASCII, conteo de nodos, componentes conexos, cobertura del componente principal, JSON parseables, y (agregado en esta ronda) duplicados exactos de título.

### 2.2 Fase 1.6 — fusión semántica (`4c1b1bc`)
- `scripts/phase1_6_merge.py`: clustering por título exacto o similitud (`rapidfuzz.ratio >= 92`), generando `dataset/metadata/merge_clusters.json` para revisión.
- 35 clusters (73 nodos) leídos en su totalidad y fusionados a mano en `dataset/metadata/merge_decisions.json`: una sola voz por concepto, sin atribución a autores, jerga explicada en la misma frase, `pasos_accionables`/`condiciones_activacion` unidos con deduplicación semántica (sin perder ningún paso único), `fuente` conservada como metadato interno con `fuentes_adicionales` cuando el cluster mezclaba libros.
- Enlaces (`nodos_previos`/`nodos_siguientes`) recalculados automáticamente por el script (unión de los miembros del cluster, sin auto-referencias) — no a mano, para evitar errores aritméticos en 35 clusters.
- Los 40 archivos perdedores preservados (no borrados) en `dataset/metadata/merged_originals/`.
- Validador actualizado: falla dura si queda algún grupo con `titulo_concepto` exactamente duplicado; warning informativo (no bloqueante) para pares de título con similitud ≥ 95.

**Resultado final del validador (`python scripts/run_phase1.py`):**
```
--- Resumen Gate 0 ---
  [OK] Enlaces rotos en dataset == 0 (valor: 0)
  [OK] Archivos con nombre no-ASCII == 0 (valor: 0)
  [OK] Nodos en master_graph.json == archivos en disco (valor: 908 vs 908)
  [OK] Componentes conexos <= 2 (valor: 1)
  [OK] Cobertura del componente principal >= 99% (valor: 100.0)
  [OK] Todos los JSON parsean sin error (valor: 0)
  [OK] Cero grupos con titulo_concepto exacto duplicado (valor: 0)

--- Estadisticas del grafo ---
{
  "componentes_conexos": 1,
  "tamano_componente_principal": 908,
  "cobertura_componente_principal_pct": 100.0,
  "nodos_sin_enlaces_entrantes": 0,
  "enlaces_rotos_en_grafo": 0
}

--- Warning informativo: pares de titulo con similitud >= 95 (0) ---
  Ninguno.

GATE 0: OK
```

---

## 3. Auditoría de Fable — verificación independiente

**Veredicto: APROBADA.**

- **Métricas duras**: 908 nodos, 0 rotos, 1 componente, 100% cobertura, 0 nodos sin entrantes, 0 títulos duplicados — coincide exactamente con el validador de Claude.
- **Trazabilidad**: cuadra exacto. 73 miembros en 35 clusters; 33 canónicos conservaron su id original y 2 recibieron un id nuevo (`emprendimiento_como_disciplina_de_gestion`, `estrategia_crecimiento_clientes`); 40 perdedores, y los 40 están archivados en `merged_originals/` — coincidencia 1:1. Aritmética verificada: 946 − 38 = 908.
- **Integridad de alcance**: cero nodos fuera de los clusters con algún campo alterado. La regla dura (no tocar contenido teórico fuera de la Fase 1.6) se respetó.
- **Calidad de síntesis**: el detector de strings de Fable marcó 107 pasos accionables "sin eco" (sin coincidencia literal con el texto original), pero la inspección manual confirmó que eran reescritura legítima, no pérdida de contenido. Ejemplo señalado — el cluster más difícil de verificar (Agile-Stage-Gate, 3 nodos, 16 pasos originales) quedó en 9 pasos que conservan todo lo sustantivo y traducen jerga a lenguaje común: *"daily scrums de ~20 min liderados por scrum master"* se convirtió en *"reuniones diarias breves lideradas por un facilitador de equipo"*. Fable señala que esto cumple exactamente el estándar del principio de producto (fuentes como combustible interno, no como contenido de cara al usuario).
- **Voz unificada**: `definicion_startup` fusiona las dos definiciones fundacionales (institución humana bajo incertidumbre extrema + organización temporal que busca un modelo repetible y escalable) en un solo párrafo sin rastro de autores, con las fuentes correctamente relegadas a metadato interno (`fuente` + `fuentes_adicionales`). Cero menciones de autor en los 35 nodos fusionados, verificado por Fable con una búsqueda por expresiones regulares sobre todo el contenido.

---

## 4. Estado del repositorio

- Rama: `staging`, pusheada a `origin/staging`.
- Commits relevantes: `d73d75b`, `ed26296`, `5ce0c9a`, `4c1b1bc`.
- `main` no fue tocada en ningún momento de este trabajo.
- Etiqueta de congelamiento del dataset: `dataset-v1.0.0` (ver [CHANGELOG](#5-changelog) más abajo).

## 5. Changelog

- **2026-07-04** — Fase 1 cerrada. Tag `dataset-v1.0.0`: "Knowledge graph frozen: 908 nodes, 0 broken links, 1 component, 100% coverage".
