# AUD-04 — Motor v2.1 (Reporte de Sostenibilidad) y hotfixes v2.1.1 / v2.1.2

**Estado: cerrado. Tag `motor-v2.1`** (los dos hotfixes son fixes sobre esa
misma versión, sin tag nuevo propio). Commits: `f035429` (Motor v2.1),
`32e2d06` (Hotfix v2.1.1), `8da516c` + `08c6af0` (Hotfix v2.1.2), `8858e0e`
(documentación), `02e84b2` (fix de seguridad Supabase, ver sección 4).

---

## 1. Motor v2.1 — Reporte de Sostenibilidad (`f035429`)

Motor v2.0 quedó cerrado como "solo recibe fixes de bugs". Motor v2.1 es
un módulo **aditivo** explícitamente autorizado: memoria numérica del
proyecto entre sesiones, pensada como el producto recurrente ideal porque
es el único entregable del motor que mejora solo con el tiempo (cada
sesión deja números nuevos, el reporte del mes 3 es mejor que el del mes 1
sin que el usuario haga nada extra).

**Piezas nuevas**:
- **Memoria numérica** (`projects.numeros_proyecto`, migración
  `supabase/migrations/my_idea_003_numeros.sql`): el intérprete de turno
  extrae, solo cuando el usuario lo declara explícitamente (nunca
  inferido), 8 campos fijos (costo de materiales, horas por unidad, valor
  de la hora, precio, capacidad semanal, costos fijos mensuales, unidades
  vendidas, precio pagado real).
- **`engine/calculadora.py`**: módulo puro, cero llamadas a LLM. Costo
  unitario, margen, punto de equilibrio, techo de ingreso por capacidad,
  tres escenarios (pesimista/base/sobredemanda), ciclo de conversión de
  efectivo. Maneja rangos con aritmética de intervalos correcta (la resta
  usa min-precio menos max-costo para el peor caso, no un min-con-min
  ingenuo). Cada función declara qué insumos usó y cuáles faltan — nunca
  inventa un número.
- **`--reporte PROJECT_ID`**: inventario de lo ya conocido, mini-entrevista
  determinista (sin brújula, sin nodos, sin LLM) por hasta 6 campos
  esenciales faltantes, acepta "no sé" sin insistir, `calculadora.py`
  calcula todo lo posible, y UNA llamada Sonnet narra los resultados YA
  CALCULADOS (prohibido generar cifras nuevas). Estructura fija: "Tus
  números hoy / Qué significan / Escenarios / Los números que te faltan",
  más disclaimer final fijo agregado por código. Presupuesto propio: $0.10.
- **Dataset v1.2** (`punto_equilibrio_unidades`, dataset a 1266 nodos):
  nodo nuevo de margen de contribución y punto de equilibrio, extraído de
  *Financial Intelligence for Entrepreneurs*.

**Verificado en vivo** (escenario mandatado de macetas: resina $8/pieza, 4
horas/pieza, valor_hora $15, precio $85, capacidad 5/semana, sin costos
fijos declarados): costo unitario $68, margen $17 (20%), techo de
capacidad 20 u/mes → $1.700 de ingreso / $340 de margen, punto de
equilibrio correctamente "pendiente" por falta de `costos_fijos_
mensuales`. Criterio más estricto verificado programáticamente: cada
número del reporte narrado se rastreó contra la salida cruda de
`calcular_reporte()` — cero huérfanos. Evidencia:
`examples/motor_v2_1_transcript.txt`, `examples/motor_v2_1_reporte_macetas.md`.

## 2. Hotfix v2.1.1 (`32e2d06`) — semántica de sobredemanda + campo dominio

Encontrado por auditoría externa (Fable), no por Claude: en
`escenarios_capacidad`, el campo `ingreso_perdido_estimado` del escenario
de sobredemanda multiplicaba unidades no atendidas por el **margen** ($17)
en vez del **precio** ($85) — subestimaba el costo de oportunidad real 5x
(reportaba "$170 en ventas perdidas" cuando la cifra real es $850).

**Causa raíz de proceso, más importante que el bug en sí**: el assert
original (`ingreso_perdido_estimado == 170`) se escribió leyendo la salida
de la función, no calculando el escenario de forma independiente —
verificaba la implementación, no la intención. Esto motivó una regla nueva
de proceso, fijada en `AGENTS.md`: todo escenario canónico de un test
numérico de `calculadora.py` se calcula A MANO en un comentario antes de
escribir el assert; el valor del assert sale de ese cálculo manual, nunca
de correr la función y copiar lo que imprimió.

**Fix**: campo separado en dos, con semántica y nombre distintos —
`ingreso_perdido_estimado = unidades_no_atendidas × precio` (ventas que no
se facturan, $850) y `margen_perdido_estimado = unidades_no_atendidas ×
margen_u` (ganancia que no llega, $170). `engine/test_calculadora.py`
reescrito con las constantes derivadas del cálculo manual, más un assert
de guardia (`ingreso_perdido_estimado != margen_perdido_estimado`) que
atrapa una regresión a la misma fórmula.

**Groundwork de dominios** (cero cambio de comportamiento el día que se
hizo): campo `dominio` agregado a los 1266 nodos (todos `"core"` por
ahora), Gate 0 lo valida, filtro por dominios desbloqueados instalado en
router/brújula/cosecha — con el default `{"core"}`, el filtro es un no-op
hasta que exista un segundo dominio.

## 3. Hotfix v2.1.2 (`8da516c` + `08c6af0`) — bugs de una sesión en vivo sin guion

A diferencia de todo lo anterior (escenarios mandatados o guionizados),
esta ronda fue la primera sesión genuinamente sin guion: una idea
inventada en el momento (tienda de barrio + entregas a domicilio por
WhatsApp), cero respuestas escritas de antemano, llamadas reales a la API,
cada respuesta decidida solo después de leer la pregunta real impresa por
el motor. Transcripción completa:
`examples/hotfix_v2_1_2_sesion_en_vivo.txt` (T14 en
[TST-01](../05_TESTING/TST-01-Registro_de_Pruebas.md)).

Encontró tres bugs reales, ninguno visible en pruebas anteriores porque
todas corrían con mocks o en modo offline/JSON local:

1. **`--continuar` perdía la pregunta pendiente**: al resumir una sesión
   interrumpida, el intérprete arrancaba con `respuesta_usuario=None` sin
   memoria de qué se había preguntado — indistinguible del arranque de
   una sesión nueva. En el mejor caso, la siguiente respuesta del usuario
   se aplicaba a una pregunta distinta (recuperable con una repregunta).
   En el peor caso, reproducido en vivo, el modelo decidió
   `accion='salir'` ("Hasta pronto") sin que el usuario dijera nada
   parecido a querer irse — su línea nunca se leyó, descartada en
   silencio. **Fix**: `guardar_sesion()` ahora persiste la pregunta
   literal antes de cada `leer_entrada()` (ramas `avanzar` y
   `repreguntar`); `--continuar` la recupera y la re-presenta, leyendo una
   respuesta real antes de entrar al bucle principal. Verificado en vivo
   (pregunta repetida palabra por palabra, respuesta bien aplicada) y con
   test nuevo (`engine/test_resume_pregunta_pendiente.py`, sin llamadas
   reales).
2. **`sessions.tipo` no aceptaba `'reporte'`**: Motor v2.1 agregó ese valor
   pero nunca actualizó el `CHECK constraint` de la columna. Contra
   Supabase real, `--reporte` generaba y guardaba el reporte en disco
   correctamente y luego crasheaba con `postgrest.exceptions.APIError` al
   intentar registrar la sesión. **Fix**: migración
   `supabase/migrations/my_idea_004_reporte_tipo.sql`.
3. **`plans.etiqueta` no aceptaba `'reporte_numeros'`**: mismo patrón, una
   columna después. Tras aplicar la migración 004, `--reporte` avanzó un
   paso más y crasheó en el siguiente `insert`. **Fix**: migración
   `supabase/migrations/my_idea_005_reporte_etiqueta.sql`.

**Re-verificado de punta a punta contra Supabase real** una vez aplicadas
las tres migraciones: sesión `b6eb05d0...` cerrada con costo exacto
$0.0153 (coincide con lo impreso en pantalla), plan `reporte_numeros`
guardado (2744 caracteres). La fila de sesión huérfana del intento que
crasheó antes de aplicar la migración 005 se confirmó sin filas
dependientes y se borró de Supabase.

## 4. Fix de seguridad Supabase (`02e84b2`) — no forma parte del hotfix v2.1.2, pero se hizo en la misma ronda

El linter de seguridad de Supabase marcó `public.rls_auto_enable()` como
alcanzable vía RPC por los roles `anon` y `authenticated`. Investigación:
esta función no la creó ninguna migración de este repo ni la llama el
código en ningún lado; al invocarla, Postgres devolvió "cannot display a
value of type event_trigger" — confirma que existe para dispararse sola en
eventos DDL (probablemente forzar RLS en tablas nuevas), no para ser
llamada directamente. **Fix**: migración
`supabase/migrations/my_idea_006_revoke_rls_auto_enable.sql` — revoca
`EXECUTE` de `PUBLIC`/`anon`/`authenticated`, sin tocar el mecanismo de
event trigger en sí. Un tercer hallazgo del mismo linter
(`auth_leaked_password_protection`, protección contra contraseñas
filtradas) requiere el plan Pro de Supabase — pendiente hasta que el
proyecto entre a producción real, según decisión explícita del usuario.

## 5. Estado al cierre de esta ronda

- Regresión completa (`engine/test_*.py`, 7 archivos): verde.
- `scripts/run_phase1.py` (Gate 0): verde, 1266/1266 nodos, 100% de
  alcanzabilidad.
- Las 6 migraciones (`001` a `006`) aplicadas por el usuario.
- Próximo paso, explícitamente NO iniciado por Claude: una sesión en vivo
  del propio usuario, con una idea real, sin guion — la última validación
  antes de la Fase 3 (el porte web).
