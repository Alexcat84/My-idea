# TST-01 — Registro de Pruebas

Registro maestro de toda la suite de pruebas del motor (`engine/`). Dos
familias, con propósito y costo distintos — no confundirlas:

- **Automatizadas** (`engine/test_*.py`): mocks de `llamar_claude` /
  `leer_entrada` / `buscar_afines`, cero llamadas reales a la API, cero
  costo, deterministas. Son la red de seguridad de regresión — correrlas
  después de cualquier cambio en `prototipo_motor.py` o `calculadora.py`.
- **En vivo** (`engine/live_tests/test_*.py`): llamadas reales a Sonnet/Haiku
  (y en algunos casos a los embeddings locales), persistencia forzada a
  JSON local para no tocar Supabase real. Cuestan dinero real (céntimos de
  dólar por corrida) y ya cumplieron su propósito — generaron la evidencia
  que vive en `examples/`. No hace falta re-correrlas salvo que se quiera
  reproducir o auditar el resultado original.

Comandos de operación día a día (probar todo lo demás, sesiones reales,
`--reporte`, etc.) están en
[PRO-02-Manual_de_Comandos_CLI](../04_PROCESSES/PRO-02-Manual_de_Comandos_CLI.md).

---

## Suite automatizada (regresión, costo $0, correr después de cada cambio)

| ID | Archivo | Qué verifica | Se agregó en |
|---|---|---|---|
| T01 | [engine/test_calculadora.py](../../engine/test_calculadora.py) | `calculadora.py`: costo unitario, margen, punto de equilibrio, techo de capacidad, 3 escenarios (incluyendo el par `ingreso_perdido_estimado`/`margen_perdido_estimado` corregido en el hotfix v2.1.1), rangos con aritmética de intervalos, cero datos inventados cuando faltan insumos. Constantes derivadas a mano por regla de `AGENTS.md`. | Motor v2.1 / Hotfix v2.1.1 |
| T02 | [engine/test_resume_pregunta_pendiente.py](../../engine/test_resume_pregunta_pendiente.py) | `guardar_sesion()` persiste la pregunta literal pendiente ANTES de leer la respuesta; `cargar_sesion()` la recupera intacta para que `--continuar` la re-presente. | Hotfix v2.1.2 |
| T03 | [engine/test_autocorreccion.py](../../engine/test_autocorreccion.py) | Auto-corrección invisible: si el modelo inventa un `id` inexistente dos veces seguidas, el sistema reintenta con `error_previo`+`ids_validos`, y si vuelve a fallar, autoselecciona en silencio por afinidad semántica (nunca `None`, evento `fallback_auto` registrado). | Fase 2.9 |
| T04 | [engine/test_pregunta_adaptada.py](../../engine/test_pregunta_adaptada.py) | Si `pregunta_necesaria=true` pero falta `pregunta_adaptada`, se trata como respuesta inválida y dispara reintento; el reintento exitoso se usa tal cual (nunca la pregunta cruda del caché). | Fase 2.6 |
| T05 | [engine/test_conversacion_incremental.py](../../engine/test_conversacion_incremental.py) | Mecánica de `llamar_claude_conversacion`: el marcador `cache_control` vive solo en el último bloque enviado (se mueve turno a turno), y una llamada fallida deja `historial_mensajes` intacto (sin turno huérfano). | Fase 2.7 |
| T06 | [engine/test_salto_semantico.py](../../engine/test_salto_semantico.py) | Validación de `salto_semantico` (brújula): un salto ofrecido se acepta al primer intento; uno inventado (fuera de lo ofrecido) se rechaza, dispara un reintento, y cae al respaldo local de afinidad si vuelve a fallar. | Fase 2.8 |
| T07 | [engine/test_sigamos_salida.py](../../engine/test_sigamos_salida.py) | `extender_sigamos_dirigido` corta de inmediato en cuanto detecta "dame mi plan" a mitad de la extensión dirigida, sin forzar las preguntas restantes. | Fase 2.9 |
| T15 | [engine/test_leer_entrada_decode_error.py](../../engine/test_leer_entrada_decode_error.py) | `leer_entrada()` convierte un `UnicodeDecodeError` (encontrado en vivo pegando texto con emojis en una consola de Windows) en cierre elegante (`SesionInterrumpida`), igual que EOF/Ctrl+C, en vez de propagar un traceback crudo. | Hotfix v2.1.3 |

**Correr toda la suite de una vez:**
```bash
cd "engine"
for t in test_calculadora.py test_resume_pregunta_pendiente.py test_leer_entrada_decode_error.py test_autocorreccion.py test_pregunta_adaptada.py test_conversacion_incremental.py test_salto_semantico.py test_sigamos_salida.py; do
  echo "=== $t ==="; python "$t" || echo "FALLO: $t"
done
```
Todos terminan con una línea `TODO OK: ...` (o, en `test_calculadora.py`,
`TODOS LOS TESTS DE calculadora.py PASARON`). Cualquier `AssertionError` o
`FALLO` interrumpe la cadena — investigar antes de continuar.

---

## Suite en vivo (API real, costo real, ya ejecutada — evidencia en `examples/`)

| ID | Archivo | Qué verifica | Evidencia generada | Costo aprox. |
|---|---|---|---|---|
| T08 | [engine/live_tests/test_macetas_comparativa.py](../../engine/live_tests/test_macetas_comparativa.py) | Fase 2.6 contra el escenario real de macetas (preguntas adaptadas por turno + prompt caching). | `examples/fase2_6_macetas_con_cache.txt` | ~$0.14 |
| T09 | [engine/live_tests/test_macetas_fase27.py](../../engine/live_tests/test_macetas_fase27.py) | Fase 2.7: escucha activa (`prioridad_declarada`), cobertura del bloqueo declarado, anti-plantillas x3, caching incremental. | `examples/fase2_7_macetas_escucha_activa.txt`, `examples/fase2_7_plan_macetas.md` | ~$0.10-0.15 |
| T10 | [engine/live_tests/test_macetas_fase28.py](../../engine/live_tests/test_macetas_fase28.py) | Fase 2.8: brújula semántica (navegación libre), "sigamos" dirigido, coherencia por autodeclaración. | `examples/fase2_8_macetas_navegacion_libre.txt`, `examples/fase2_8_plan_macetas.md` | ~$0.10-0.15 |
| T11 | [engine/live_tests/test_macetas_fase29.py](../../engine/live_tests/test_macetas_fase29.py) | Fase 2.9: cierre del motor (tag `motor-v2.0`) sobre el mismo escenario de macetas. | `examples/fase2_9_macetas_cierre_motor.txt`, `examples/fase2_9_plan_macetas.md` | ~$0.10-0.15 |
| T12 | [engine/live_tests/test_reporte_macetas.py](../../engine/live_tests/test_reporte_macetas.py) | Motor v2.1: extracción de `numeros_proyecto` en conversación real + `--reporte` (mini-entrevista, cálculo puro, narración sin cifras inventadas). Escenario mandatado del hotfix v2.1.1 (`ingreso_perdido_estimado`=850 / `margen_perdido_estimado`=170). | `examples/motor_v2_1_transcript.txt`, `examples/motor_v2_1_reporte_macetas.md` | ~$0.10-0.20 |
| T13 | [engine/live_tests/test_sigamos_salida_real.py](../../engine/live_tests/test_sigamos_salida_real.py) | Igual que T07 pero con el clasificador REAL (`SYSTEM_PROFUNDIZAR`, no mockeado) reconociendo "dame mi plan" a mitad de la extensión. | Verificado inline (asserts), sin transcript propio en `examples/`. | ~$0.01 (2-3 llamadas Haiku) |

La sesión en vivo sin guion que encontró los 3 bugs del hotfix v2.1.2
(`--continuar` perdía la pregunta pendiente, `sessions.tipo` y
`plans.etiqueta` sin los valores de Motor v2.1) no tiene script propio —
fue interactiva, turno a turno, contra Supabase real, no un script de un
solo disparo. Su transcripción completa: **[T14]**
[examples/hotfix_v2_1_2_sesion_en_vivo.txt](../../examples/hotfix_v2_1_2_sesion_en_vivo.txt).

La primera sesión en vivo del propio usuario (idea real: app de I Ching,
proyecto `e3bc08a3...`) encontró el bug de `UnicodeDecodeError` (T15,
hotfix v2.1.3) al pegar el texto de un anuncio de Facebook con emojis y
saltos de línea. El plan igual se generó completo y coherente
(`engine/salidas/plan_20260707_2038.md`, no versionado por ser salida de
usuario real), pero la sesión de Supabase quedó sin cerrar tras el
traceback — corregido junto con el bug de fondo.

---

## Estado

Última corrida completa de la suite automatizada (T01-T07): **7/7 verde**,
verificada junto con el commit `8858e0e` (documentación del hotfix
v2.1.2). Ver también `scripts/run_phase1.py` (Gate 0) para la validación
del dataset, registrado aparte porque no es una prueba del motor sino del
grafo de conocimiento — cubierto en
[AUD-01](../audits/AUD-01-Fase1_Cierre_y_Auditoria.md) y las auditorías de
fase (AUD-02 a AUD-04).
