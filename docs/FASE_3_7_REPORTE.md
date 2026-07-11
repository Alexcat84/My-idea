# Fase 3.7 — Fidelidad y voz: reporte de cierre

Fecha: 2026-07-11 · Rama: `staging` · Tag: `web-v0.6.1` ·
Commits: `18a5432` (paso 0), `a70bb03` (D+A+B), `4298da9` (C0-C6),
`01af02a` (gate C7). Detonante: la sesión de fundador (gate 5) encontró
"se parece pero no es" + diagnóstico del auditor con el repo abierto.

## Resultado en una línea

**El canon de Claude Design está versionado en `docs/diseno-canon/`, la
puerta que le escondía al fundador la etapa 5 y los 6 mundos está
cableada (y era un bug de una línea), la voz ya no escribe con guiones ni
asume equipos que no existen, y el gate de cierre es una sesión real por
la UI con capturas lado a lado contra el canon.**

## PASO 0 — el canon al repo

8 HTML + REGLAS_Y_TOKENS.md commiteados. La causa raíz 1 del auditor era
exacta: la "alineación al canon" de la 3.6 se hizo contra el recuerdo.
Desde ahora la vara es un archivo versionado y el gate es mecánico.

## D1 — la pregunta fuera de contexto, forense (bitácora real)

Cadena de tres eslabones en `sessions.decisiones` de la sesión del
fundador: (1) el intérprete juzgó vaga la respuesta y quiso repreguntar
**sin repreguntas disponibles**; (2) saltó `fallback_auto` ("2 respuestas
inválidas del modelo") que avanza al primer candidato y sirve su caché
**verbatim, sin intérprete**; (3) ese caché (test_sell_channel_partners,
nodo B2B) traía supuestos de libro ("ustedes", "su equipo",
"distribuidores"). No fue alucinación: fue la red de seguridad sirviendo
caché sucio de un nodo mal condicionado. Cura triple en A+B.

## D2 — sello de versión

`v·<sha7>` permanente en el pie (VERCEL_GIT_COMMIT_SHA; `v·dev` local).
Dato del incidente: producción **sí** servía el build correcto
(`9f678d6`); "Corregir algo" **sí existía** en el código (el diagnóstico
del auditor erró ahí) — y además está en el canon 03. Se removió por
orden del fundador; conviene retirarlo también del HTML canon para que
el gate lado a lado no lo acuse.

## A — voz sin guiones

- Regla anti-guiones (— –) en los 7 prompts de generación (fuente
  `prototipo_motor.py` + `build_question_cache.py`; la web hereda por
  sync con checksums).
- Filtro mecánico `limpiarGuiones` (web/lib/voz.ts) en el punto único de
  salida del modelo (`costmeter.llamarClaude*`): viñetas, rangos
  numéricos, incisos y guiones sueltos; 7 tests.
- Barrido del caché: **256 preguntas con — o – → 0**.

## B — caché sin supuestos de libro

Auditoría por patrones (ustedes / su equipo / su empresa / distribuidores
/ verbos de plural) sobre las 3,428: **97 con indicios**. Regla nueva en
el generador ("habla SIEMPRE de tú; no asumas cofundadores, equipo,
empresa, distribuidores; pregunta en condicional") → 96 regeneradas
($0.1081) + 9 reescritas a mano (reincidentes de Founder's Dilemmas y la
del incidente) → 4 residuales legítimos (condicionales reales o falso
positivo). `condiciones_activacion` con cláusula negativa explícita en
los 3 nodos B2B propensos a salir prematuros. Gate 0 OK.

## C0 — la puerta que faltaba (el hallazgo mayor, y era UNA línea)

`generarPlan` limpiaba `pregunta` pero **nunca reseteaba
`listoParaPlan`** → al llegar al plan desde "Suficiente para avanzar",
`entrevistaActiva` quedaba true para siempre y escondía el CTA "Pasar a
Manos a la Obra" y la fila "Potencia tu idea" (Tus Números no tenía esa
condición: por eso era lo único que el fundador veía). Además: la cinta
del home de una idea en etapa 5 ahora entra directo a `?vista=manos`.
Verificado en el gate: **los 6 mundos aparecen en un flujo real sin
teclear URLs**.

## C1-C6 — fidelidad contra los archivos (extraída, no reinterpretada)

- **C1 riel** (canon 04): barra 4px gradiente azul que crece, puntos
  20px con aro hairline, anillo girando en el punto pensado, relleno
  inset 4px, silenciosos al 50%, rombo "fue un salto". Animaciones solo
  de ENTRADA de eventos reales.
- **C2 stepper**: el canon (03/04/05) manda conectores PUNTEADOS — el
  stepper de 3.6 ya era fiel; sin cambios (si se quiere barra de relleno
  arriba, es cambio de canon, no de fidelidad).
- **C3**: riel contenido (max-height + scroll, actual siempre a la
  vista, historial deslizable).
- **C4 Claridad** (canon 03): frase héroe 30px + dos tarjetas
  (suposiciones con borde azul y rombos) + nota interna + CTA único.
  Fuera acordeones, "Etapa detectada" y "Áreas del plan" (no existen en
  el canon). Sin "Corregir algo".
- **C5**: espera del plan como tarjeta con anillo + etapa llegando por
  SSE (el riel enciende cada etapa real).
- **C6 plan** (canon 05): chip + título 32px + caja verde grande "Esta
  semana" con botón "Empezar con esto" (→ Manos a la Obra) + etapas como
  tarjetas numeradas 01..N.

## C7 — el gate de cierre

`web/scripts/gate_canon.ts`: Playwright vive el viaje entero por la UI
real (la idea de kits de huerto urbano: organizer real, 5 respuestas de
entrevista real, plan real por SSE, CTA a manos) y captura cada pantalla
junto al frame desktop de su HTML canon. Pares en
`web/examples/gate-canon/`. El gate es mecánico; el veredicto visual es
del fundador/auditor.

## Costos reales de la fase

| Concepto | Costo |
|---|---|
| Regeneración de 96 preguntas (haiku) | $0.1081 |
| Sesión real del gate (organizer + entrevista + plan) | ≈$0.25 |
| Total | ≈$0.36 |

## Suites

Web 238/238 (30 archivos: +voz 7, +brecha/muralla previos) · python
13/13 · tsc limpio · **clon limpio VERDE** (python 13/13; web 30/30
archivos, 235 + 3 skipped que requieren .env, ausente en el clon por diseño). Trampa Windows
documentada: los clones de prueba van en ruta CORTA (MAX_PATH corrompe
node_modules).
