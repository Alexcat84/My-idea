# Fase 3.6 — Convergencia frontend (canon visual) + integración de packs

Fecha: 2026-07-10 · Rama: `staging` · Tag: `web-v0.5.0`

## A. Línea de ensamblaje (integrar_packs.py) — ejecutada

Hallazgos reales al encenderla (todos corregidos en el mismo commit):

1. **Envoltorio de bridges_aprobados.json**: los archivos aprobados llegan
   como `{nota, aprobados: [...]}`; el script esperaba lista plana. Se adaptó
   `validar_prerequisitos()` para aceptar ambas formas conservando la nota
   en el archivo. 36 puentes (12+12+12) sobre 27 nodos core.
2. **Colisión de node_id**: `analisis_competitivo` existía en core Y en el
   pack quality (conceptos distintos). El nodo del pack se renombró a
   `analisis_competitivo_calidad` con sus 3 vecinos actualizados.
3. **Título duplicado**: `auditoria_calidad` (pack, Crosby) vs `quality_audit`
   (core) compartían "Auditoría de Calidad". El del pack pasó a
   "Auditoría de Calidad (Examen Planeado de Conformidad)" (registrado en
   `titulos_diferenciados.json`, la convención del saneamiento).
4. **Typos de datos en 7+ nodos de packs**: `resumen_keorico`,
   `resumen_theorico`, `resumen_hteorico` y 5 variantes más (97 archivos
   entre packs y sus copias) — normalizados a `resumen_teorico` con barrido
   completo; 0 nodos sin resumen tras el fix. Rompían el caché de preguntas.
5. **Dominios ampliados**: `DOMINIOS_PERMITIDOS` de run_phase1 ahora acepta
   `core|quality|health_safety|environmental`.
6. **Alcanzabilidad**: el validador une las semillas de packs
   (`packs/*/metadata/entry_seeds.json`, 21) a las 20 core SOLO para el
   chequeo — `dataset/metadata/entry_seeds.json` (el que rutea al usuario
   en el motor) NO se toca: los mundos siguen detrás de flags.
7. **Orden b/e corregido** en integrar_packs.py: plan_readiness lee
   master_graph.json, que recompila run_phase1 — familias ahora se etiquetan
   sobre el grafo ampliado (2805), no el viejo (1266).
8. **`--patch-file` en build_question_cache.py**: 1566 ids exceden el límite
   de línea de comandos de Windows; ahora la lista viaja en archivo, con
   guardado incremental cada 50 (una falla a mitad no pierde lo pagado) y
   costo total reportado.

Gate 0 tras los fixes: **VERDE** — 2805 nodos, 1 componente, 0 rotos,
alcanzabilidad dirigida 100.0% desde 41 semillas, 0 títulos duplicados.

### Costos reales de la línea

| Paso | Costo |
|---|---|
| b. familias (clasificador por palabras clave) | $0 |
| c. caché de preguntas parcial (Haiku 4.5) | PENDIENTE |
| d. índice Voyage completo (~2805 nodos) | PENDIENTE |

## B-E. Convergencia visual (canon: 8 HTML + REGLAS_Y_TOKENS.md)

- `web/app/tokens.css` → **VARIABLES v2**: "el azul piensa, el verde
  ejecuta" (azul #4D7CFE etapas 1-4/exploración/navegación; verde #3FB950
  etapa 5/Esta semana/checklist/Marcar hecho; ámbar guardián #E0A64A);
  `--done-soft` nuevo; animaciones canon en globals.css.
- `Stepper.tsx` (header + mini): los 5 nombres canónicos; verde solo la 5.
- Home `/ideas`: cintas con mini-stepper, chips por estado (verde
  "Manos a la Obra · N/M" del plan VIGENTE, azul "En exploración"/"Con
  plan", neutro "Con claridad"), saludo + captura rápida.
- `/nueva`: La Chispa ("Cuéntame tu idea… Continuar") y Claridad ("Esto
  entendí de tu idea", CTA "Explorar estas suposiciones", nota 5 créditos).
- Vista de idea: breadcrumb + stepper en header; "Suficiente para
  avanzar" (canon 04); "Esta semana" VERDE en el plan; CTA "Pasar a Manos
  a la Obra" + "Ajustar el plan"; tarjeta Tus Números "2 créditos".
- `ManosALaObra.tsx` (canon 06/08): checklist agrupado con títulos de
  etapa del markdown REAL del plan, 4 estados de un toque (forma, no solo
  color) + "Marcar hecho", barra y contadores verdes, ritual de 3
  tarjetas → POST /follow, acordeón Historia (planes core anteriores),
  Ritmo, y mundos activos (grupo del checklist por dominio + arranque
  world/start + plan del mundo).
- `PotenciaTuIdea.tsx` (canon 07 B): Tus Números 2 créditos + mundos 3
  créditos desde precios.ts/packs_catalog (cero cifras hardcodeadas);
  candado → pack_clicks + "Disponible próximamente"; activo → chip verde.
- `/potenciadores` (canon 07): centro de créditos, packs 5/12/30, "$ —".
- API: `/api/idea/[id]` ahora expone `unlocks`, `mundos` (plan por
  dominio) e `historial`; el plan principal filtra SOLO core (un plan de
  mundo ya no tapa el viaje). GET checklist en orden cronológico (el
  grupo vigente es el último; plan_id es uuid y su orden era arbitrario).

REGLA DE ORO intacta: stepper, chips, barras y checks solo pintan filas
persistidas y eventos reales del motor.

## F. Vuelo y cierre

- FASE 2h nueva en `scripts/vuelo.ts`: contrato de la UI (unlocks +
  historial + mundos + grupo vigente cronológico).
- `scripts/capturas.ts`: PNGs desktop 1240 / mobile 380 de las 5
  pantallas, autenticado como dev user (examples/capturas/).
- Resultados: PENDIENTE (vuelo 10/10, suites, capturas, preview URL).
