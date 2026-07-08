# AUD-05 — Hotfix v2.1.3: `UnicodeDecodeError` al pegar texto con emojis

**Estado: cerrado. Sin tag nuevo** (fix sobre `motor-v2.1`, mismo patrón que
v2.1.1 y v2.1.2). Commit: pendiente de push al momento de escribir este
documento (ver historial de git para el hash real).

---

## 1. Cómo se encontró

Primera sesión en vivo del propio usuario, con su idea real (una app de
I Ching ya publicada en Play Store, proyecto Supabase `e3bc08a3-4484-4ede-
8b0a-3bfd28131016`) — la validación final que se venía posponiendo desde
el cierre de Fase 2.9 ("la siguiente validación real requiere una sesión
en vivo, sin guion"). La sesión iba bien, con navegación y escucha activa
funcionando (`prioridad_declarada` capturó correctamente "Identificar el
cliente específico antes de intentar adquisición nuevamente", conteo 4),
hasta que el motor preguntó qué decía un anuncio de Facebook que el
usuario había probado. El usuario pegó el texto del anuncio directamente
desde el portapapeles — con emojis y saltos de línea.

## 2. Qué pasó exactamente

Reconstruido a partir del reporte del usuario más la evidencia en disco:
cada salto de línea del texto pegado fue interpretado por la terminal como
si se hubiera presionado Enter — el motor "contestó solo" varias preguntas
seguidas, cada una con el fragmento de texto (y a veces un emoji suelto)
que le tocó en esa línea. Esto **no es un bug de `prototipo_motor.py`**:
es cómo funciona cualquier `input()` de terminal frente a una pegada
multilínea — el proceso no tiene forma de distinguir "el usuario pegó 6
líneas de una vez" de "el usuario escribió y confirmó 6 respuestas
distintas".

Lo que sí era un bug real: en algún punto de esa ráfaga, uno de los
fragmentos (probablemente una línea con solo un emoji) no pudo ser
decodificado por la consola de Windows, y `input()` lanzó
`UnicodeDecodeError` — una excepción que `leer_entrada()` **no
atrapaba** (solo capturaba `EOFError`/`KeyboardInterrupt`). El resultado:
un traceback crudo, exactamente lo que el "cierre elegante" de Motor v1.0
existe para evitar. El usuario cerró la ventana sin alcanzar a copiar el
traceback completo.

**Evidencia de que el daño fue menor de lo que pareció**: pese a la ráfaga
de respuestas fragmentadas, el `perfil_sesion` guardado localmente
(`engine/sessions/2947a1a5.json`) interpretó el contenido del anuncio con
sentido ("Intentó publicidad en Facebook con un mensaje abstracto ('Some
questions don't have Google answers') sin mencionar I Ching ni la
propuesta concreta") — nada quedó como texto basura. La conversación
incluso llegó a generar un plan completo y coherente
(`engine/salidas/plan_20260707_2038.md`, 121 líneas, con etapas y cifras
que sí corresponden a la idea real del usuario), probablemente en una
corrida posterior a la que crasheó. Lo que sí quedó incompleto: la sesión
de Supabase (`5787da98-c680-4021-a38a-fc03b1612b74`) nunca se cerró
(`closed_at=None`, `costo_usd=0.0`, cero filas en `plans`/`project_nodes`
para ese proyecto) — consistente con que el traceback cortó el proceso
en algún punto antes de que `_persistir_resultado` pudiera completar su
escritura a Supabase.

## 3. Fix

1. **`sys.stdin` reconfigurado a UTF-8 con `errors="replace"`**, igual que
   ya se hacía para `stdout`/`stderr` desde el commit de kickoff de Fase 2
   (`c54d5e1`, que resolvió el mismo problema pero de salida —
   `UnicodeEncodeError` con flechas `->` en contenido de nodos). Esto
   ataca la causa más probable de raíz.
2. **`leer_entrada()` ahora también atrapa `UnicodeDecodeError`**, tratándolo
   exactamente igual que EOF/Ctrl+C: cierre elegante, nunca un traceback.
   Esto es la red de seguridad — cubre el caso de que la consola no
   respete `sys.stdin.reconfigure()` (comportamiento observado en algunas
   versiones de Python/Windows Terminal donde la lectura de consola no
   pasa por la capa de encoding configurable de `io`).
3. **Documentado el riesgo de fondo** (no solucionable sin reescribir el
   modo de lectura de la terminal): pegar texto con saltos de línea
   siempre se va a repartir entre preguntas sucesivas. Se agregó una
   advertencia clara en `PRO-02` con el workaround (quitar saltos de línea
   antes de pegar) y la nota de que este problema desaparece en la Fase 3
   (interfaz web con un campo de texto real, donde pegar multilínea sí
   funciona como una sola respuesta).

**Decisión explícita de alcance**: no se intentó construir un sistema de
"buffer de pegado" (detectar una ráfaga de líneas y tratarlas como una
sola respuesta) porque es una limitación inherente a `input()` de
terminal, el esfuerzo de ingeniería para resolverlo bien (lectura cruda de
consola, específica por plataforma) es alto, y el problema de fondo
desaparece solo al llegar a la Fase 3. Se priorizó cerrar la fuga real (el
traceback) sobre resolver la ergonomía completa de un prototipo de
terminal que ya tiene fecha de reemplazo.

## 4. Verificación

- Test nuevo, sin llamadas reales a la API:
  [engine/test_leer_entrada_decode_error.py](../../engine/test_leer_entrada_decode_error.py)
  (T15 en [TST-01](../05_TESTING/TST-01-Registro_de_Pruebas.md)) — mockea
  `input()` para lanzar `UnicodeDecodeError` y confirma que
  `leer_entrada()` lo convierte en `SesionInterrumpida`, no en traceback.
- Regresión completa (8 archivos `engine/test_*.py`): verde.
- Smoke test manual (`--gratis --offline`): sin regresión visible tras
  reconfigurar `sys.stdin`.
- `scripts/run_phase1.py` (Gate 0): verde.

## 5. Pendiente / no accionado

La fila de sesión huérfana en Supabase (`5787da98-c680-4021-a38a-
fc03b1612b74`, proyecto real del usuario) **no se borró** — a diferencia
de las filas huérfanas de pruebas anteriores, esta pertenece a un proyecto
real del usuario, no a un test. Se deja tal cual; no afecta el uso futuro
del proyecto (`--seguir` sigue funcionando con el `project_id`), y el plan
completo ya existe en `engine/salidas/plan_20260707_2038.md` para
referencia del usuario.
