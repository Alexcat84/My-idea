# AUD-06 — Motor v2.2: tipo de oferta, guardián GIGO, coherencia mecánica del plan

**Estado: cerrado. Tag `motor-v2.2`.**

---

## 1. Cómo se encontró

Auditoría de Fable sobre la transcripción de la primera sesión en vivo del
propio fundador (`examples/hotfix_v2_1_2_sesion_en_vivo.txt` y, en esta
ronda, `para fable 5.txt` — la re-corrida post hotfix v2.1.3, idea real:
una app de I Ching ya publicada en Play Store). La entrevista y el plan
resultante fueron certificados como el producto que el motor promete:
en el turno 10, el sistema detectó por sí solo que el anuncio de Facebook
del fundador llevaba a la página de Facebook y no a la APK — el bug real
de adquisición, encontrado con preguntas, no con opinión. Pero la lectura
detallada encontró tres bugs reales en `--reporte`, todos con la misma
causa raíz: **el sistema reconstruía en vez de registrar** lo que el
usuario realmente dijo.

## 2. Los tres bugs

1. **El plan contradijo evidencia declarada.** El usuario dijo "unos
   amigos que son una familia de China" y "su cultura es estricta, usan
   la parte física, ignoran cualquier app, eso es inútil" — un descarte
   explícito de ese segmento como canal. El plan igual propuso "tu propia
   familia y su red" como canal de adquisición, y además convirtió
   "amigos" en "familia" (alucinación de relación). El `perfil_sesion`
   nunca registró el descarte como restricción; el redactor no tenía
   forma de saber que no debía proponerlo.
2. **Incoherencia etiqueta/contenido, tercera reincidencia** (después de
   Fase 2.5 y Fase 2.8). El plan traía una sección "¿Puede sostenerse tu
   idea?" con contenido real (línea base de $175/mes, ejercicio de CAC) y
   tres líneas después declaraba "aún no cubre: viabilidad económica". La
   autodeclaración de la regla 11 de `SYSTEM_PLAN` (Fase 2.8) no bastó —
   el modelo puede seguir desincronizando su propia autodeclaración del
   contenido real que escribió.
3. **`--reporte` produjo conclusiones financieras peligrosamente falsas.**
   La mini-entrevista (molde único, "producto físico") le preguntó al
   fundador "materiales por pieza" y "horas por pieza" para una oferta
   digital. Tomó su presupuesto mensual ($200) como costo de materiales
   por pieza, sus 4 meses de desarrollo como 4 horas por unidad, y narró
   con confianza: margen -2976.9%, "no existe punto de equilibrio
   posible". La realidad de su modelo, con las unidades correctas: $200
   fijos ÷ $13 por pack ≈ 16 packs/mes de equilibrio. Un usuario de pago
   recibiendo ese reporte tomaría una decisión de abandono sobre
   matemática ficticia — esto convirtió la mejora en *blocker*, no en
   nice-to-have.

Hallazgo colateral (no un bug): el "misterio del caché" quedó resuelto —
Haiku sí mostraba `cache_read` funcionando en la entrevista; los ceros de
Sonnet son esperados (una sola llamada del redactor no tiene una segunda
que lea el prefijo, y el reporte es corto — no alcanza el mínimo
cacheable). Sin regresión.

## 3. El fix, ítem por ítem del prompt v2.2

1. **Tipo de oferta y unidad de venta**: el intérprete de turno extrae y
   persiste `tipo_oferta` (`producto_fisico`/`servicio`/`digital`/`mixto`)
   y `unidad_venta` (la palabra literal del usuario), nunca inferidos.
   Migración `my_idea_007_tipo_oferta.sql` (el prompt original decía
   "migración 006"; ese número ya lo había tomado el fix de seguridad del
   linter de Supabase del hotfix v2.1.3 — ver
   [AUD-05](AUD-05-Hotfix_v2_1_3_UnicodeDecodeError.md)).
2. **Mini-entrevista por tipo**: tres plantillas parametrizadas con
   `unidad_venta` (`_preguntas_por_tipo`). Físico y servicio comparten los
   6 campos de Motor v2.1 (retrocompatible); digital usa solo 4 (costos
   fijos, costo variable, precio, meta de usuarios/ventas) — sin pedir
   horas/valor_hora, que no aplican.
3. **Guardián GIGO**: (a) cada campo capturado guarda la unidad que la
   propia pregunta estableció (`_unidad_declarada_campo` — antes, todo
   campo de la mini-entrevista quedaba con `unidad=null`, aunque el
   esquema lo soportaba desde Motor v2.1); (b) `_detectar_no_aplica` +
   contador: al segundo "no funciona así"/"no aplica", aborta el molde,
   pregunta "¿Qué vendes exactamente y cómo se cobra?", reclasifica con
   `_clasificar_oferta` (Haiku barato), y continúa con el molde correcto;
   (c) `calculadora.detectar_inconsistencia_gigo`: si el margen es menor a
   -100% o el precio es menor al 5% del costo, el reporte NO narra
   conclusiones — `_reporte_gigo_inconsistente` (100% determinista, ni
   siquiera llama al LLM) muestra los datos crudos, señala la
   inconsistencia, y pide la corrección puntual.
4. **Calculadora generalizada**: `costo_unitario_total`/`margen_unitario`/
   `punto_equilibrio_unidades_mes` aceptan `tipo_oferta` — la rama digital
   omite horas/valor_hora como insumos (no como faltantes: no aplican).
   `escenarios_adopcion` (nueva): tres niveles de adopción (50/100/200%
   de una meta declarada) en vez de capacidad/sobredemanda. **Cambio
   adicional, más allá del prompt**: `punto_equilibrio_unidades_mes` ahora
   redondea hacia ARRIBA (`math.ceil`), no al decimal más cercano — no se
   pueden vender fracciones de unidad, y 15.4 unidades redondeadas "al más
   cercano" (15) todavía no cubre los costos fijos. Verificado contra las
   dos pruebas mandatadas (8a: 200÷13→16; 8c: 200÷4.5→45) — ninguna pasa
   sin este cambio.
5. **Evidencia negativa en el perfil**: nueva regla en
   `SYSTEM_INTERPRETE_MULTI` — un descarte con evidencia se registra como
   restricción explícita ("Descarta X como canal/segmento: [evidencia]"),
   nunca se omite. Nueva regla en `SYSTEM_INTERPRETE_MULTI` también para
   relaciones declaradas (usar la palabra exacta del usuario, nunca
   "family-ficar" una relación). Regla 12 nueva en `SYSTEM_PLAN`: prohibido
   proponer como canal/activo/segmento algo descartado con evidencia;
   prohibido alterar relaciones declaradas.
6. **Post-validador de coherencia mecánico**: `_corregir_coherencia_cobertura`
   — si el material ya traía contenido de viabilidad económica Y la
   sección fija "¿Puede sostenerse tu idea?" está presente en el markdown
   generado, `viabilidad_economica` NUNCA puede aparecer en "no cubre",
   sin importar lo que el redactor autodeclaró. Determinístico, en código,
   no depende de que el modelo lo declare bien — la solución que el
   prompt pidió explícitamente tras la tercera reincidencia.
7. **Telemetría**: sin cambios de código; documentado que los ceros de
   `cache_read`/`cache_write` de Sonnet en llamadas únicas son esperados,
   no una regresión.
8. **Pruebas** (las 4 mandatadas, más una quinta de regresión):
   - (a) `--reporte` regenerado sobre el proyecto real del fundador
     (`05868ec6`): preguntas de rama digital, cero vocabulario de piezas
     (`grep -ic pieza` → 0), equilibrio "16 unidades al mes" narrado
     correctamente. Verificado en vivo contra Supabase real.
   - (b) Suite de macetas (`test_calculadora.py::test_escenario_macetas`,
     rama física): intacta, sin cambios de comportamiento.
   - (c) Caso SaaS sintético (fijos $200, variable $0.50, precio $5,
     meta 100) → equilibrio 45 usuarios, calculado a mano antes del
     assert (`test_digital_saas_sintetico`).
   - (d) Guardián de molde: `test_reporte_tipo_oferta.py` — responder el
     molde físico con datos de una app de suscripciones aborta al segundo
     "no aplica", reclasifica a digital, y captura los 4 campos correctos
     sin rastro del molde abandonado.
9. **Limpieza de datos contaminados** (agregado por Fable tras ver la
   confirmación, antes de pasar el prompt a Claude Code): la mini-entrevista
   fallida ya había persistido en Supabase, para el proyecto real del
   fundador, `costo_materiales_unidad=200` (era presupuesto mensual),
   `horas_por_unidad=4` (eran meses de desarrollo), ambos sin unidad
   declarada. `scripts/hotfix_v2_2_limpiar_datos_contaminados.py` movió
   esos dos campos (más `valor_hora`, que solo tenía sentido junto a
   `horas_por_unidad`) a `numeros_descartados` con el motivo, y confirmó
   que `precio_tentativo` ($13/pack) y `costos_fijos_mensuales` ($200) SÍ
   eran correctos y se conservaron. Sin esta limpieza, la prueba (a)
   habría pasado por la razón equivocada: el reporte habría leído los
   $200-como-materiales del inventario ya persistido y narrado el mismo
   disparate con las plantillas nuevas.

## 4. Verificación final

- Regresión completa: 9/9 (`T01-T07`, `T15-T16` en
  [TST-01](../05_TESTING/TST-01-Registro_de_Pruebas.md)).
- `scripts/run_phase1.py` (Gate 0): verde, 1266/1266 nodos, 100% de
  alcanzabilidad — sin tocar el dataset en esta ronda.
- Reporte regenerado en vivo sobre `05868ec6` con costo real $0.02,
  guardado en `engine/salidas/reporte_20260707_2326.md` (no versionado,
  salida de usuario real).

## 5. Veredicto de Fable (verbatim, resumido)

"La entrevista y el plan quedan certificados por su usuario cero...; el
reporte queda en NO-GO hasta la v2.2, porque un producto de pago que
convierte '$13 el pack' en 'pierdes $387 por venta' no sale al mundo.
Cuando la v2.2 pase mi auditoría con el reporte de tu propio proyecto
mostrando los 16 packs de equilibrio, el motor completo queda cerrado, y
la Fase 3 deja de ser la siguiente fase para convertirse en la única que
queda." — la prueba (a) de esta ronda produce exactamente esa cifra.
