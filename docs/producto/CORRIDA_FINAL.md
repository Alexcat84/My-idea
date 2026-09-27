# Corrida final: prueba de coherencia y vuelo completo

**Regla del fundador (28 sep 2026):** ninguna llamada a la API real hasta esta corrida. La prueba de coherencia y el
vuelo completo de todos los mundos se corren UNA sola vez, juntos, cuando todo esté arriba y auditado, con el fundador
midiendo el saldo de la API al inicio y al final. Este documento dice qué se ejecuta, cuántos planes y mundos genera,
cuánto cuesta y cómo se compara con su medición.

## Antes de empezar (nada de esto gasta)

1. **Fundidas en main y desplegadas:** `puente-forja` (mundo 11, Primer Equipo) y `contexto-entrevista`, cada una con su
   visto.
2. **Migración 049 aplicada** por el fundador (`projects.memoria`), con su chequeo en OK. Sin ella no hay memoria y el
   arnés se niega a correr.
3. **Créditos del dev user:** hacen falta 90 (ver abajo). Se siembran 120.
4. **Límites de ritmo, subidos solo durante la ventana** (Vercel, producción). El dev user no está exento en producción:
   - `LIMITE_ARRANQUES_DIA`: por defecto 5 al día. La corrida abre unas 50 sesiones: subirlo a 80.
   - `FUSIBLE_SESIONES_DIA`: fusible global, por defecto 30 al día. Subirlo a 100.
   - Al terminar, se devuelven a su valor.
5. **Entorno de la máquina que corre** (el `.env` raíz, que el fundador repone para la corrida y retira después):
   `ANTHROPIC_API_KEY`, `VUELO_DEV_PASSWORD`, `SUPABASE_SERVICE_ROLE_KEY`, `SUPABASE_URL`, `SUPABASE_ANON_KEY`. Y en el
   shell, no en el `.env`: `VUELO_BASE_URL` con la URL de producción.
6. **El fundador anota el saldo de la API** y la hora de inicio (UTC).

## Lo que se ejecuta, en este orden

### Paso A. Completar la caché (local, antes de desplegar)

La salida segura del adaptador y las preguntas nuevas viven en la caché, que va dentro del despliegue. Por eso van
primero.

| # | Comando | Llamadas | Qué hace |
|---|---|---|---|
| A1 | `python engine/build_question_cache.py --faltantes --yes` | 40 (Haiku) | La pregunta de los 40 nodos con siguientes y sin pregunta. No pisa ninguna base. |
| A2 | `python engine/build_question_cache.py --neutrales --yes` | 2.940, más reintentos (Haiku) | La versión neutral de cada base viva, en `pregunta_neutral`. La base no se toca. |
| A3 | `python scripts/sync_assets_web.py` | 0 | Copia la caché a la web. |

Después: los dos topes de `web/lib/engine/cacheNeutrales.test.ts` pasan a 0. Luego las suites, el commit, el visto y
el despliegue. Si A1 o A2 dejan fallidas, salen con código distinto de 0 y la lista de cada una. Se vuelven a correr
(son reanudables: lo hecho no se paga dos veces). Cada comando imprime sus tokens y su coste real al terminar.

### Paso B. Prueba de coherencia

`npx tsx scripts/coherencia.ts --confirmo-gasto` (desde `web/`). Sin la bandera dice lo que haría y no gasta nada.
Compruébalo primero.

- **Tres personas sintéticas**, cada una en su proyecto nuevo:
  - una fundadora que trabaja sola;
  - un dueño con dos empleados recién contratados;
  - un empleado de una empresa mediana, con jefe y recursos humanos.
- **Cada una recorre el núcleo hasta su plan**, porque sin plan no se abre ningún mundo. Después recorre los 10 mundos
  del catálogo, uno tras otro, hasta la oferta del plan del mundo, sin comprarlo.
- **Responde por ellas un actor (Haiku)** fiel a su retrato.
- **Un juez ciego (Sonnet)** lee cada pregunta mostrada. Si la pregunta salió del adaptador, lee también su base. Las
  preguntas van mezcladas con 12 trampas sin marca, escritas antes de la corrida en `web/lib/coherencia/nucleo.ts`.
- **El umbral, fijado por el fundador antes de medir:**
  - 0 desajustes de papel;
  - como mucho 1 desajuste de contexto por cada 10 preguntas;
  - al menos el 95 % de las adaptadas fieles a su base;
  - todas las trampas cazadas.
- **Mundo tras mundo:** el contexto con que abre cada mundo tiene que traer lo que la persona contó en el anterior.
- **Informe:** `docs/coherencia/<fecha>/informe.md` y `datos.json`. Incluye el coste por sesión, el coste por turno
  antes y ahora, y el ahorro del caché calculado llamada por llamada.

**Corrección declarada a la propuesta E:** decía "el núcleo y los 11 mundos, 36 recorridos". El catálogo tiene 10
mundos contando Primer Equipo: el mundo 11 es el undécimo espacio si se cuenta el núcleo. Son **3 × 11 = 33
recorridos**. El umbral no cambia.

### Paso C. Vuelo completo

`pnpm vuelo` (desde `web/`): todas las fases, incluida la 2g-quater del mundo 11 y de la 2L en adelante, que no
corren enteras desde el 9 de septiembre.

- **Aserción vieja, ya corregida:** si la entrevista de Seguridad digital cierra por incompatible, la fase 2g-bis
  exigía `unlock_revertido` verdadero. Desde AUD-09 H04 (nada se borra jamás) la respuesta dice `false`, y el vuelo
  habría caído por su propio arnés. Ahora exige `false`.

## Cuántos planes y mundos genera

| | Planes | Mundos | Créditos |
|---|---|---|---|
| Coherencia | 3 del núcleo | 30 entrevistas de mundo sin plan (3 personas × 10 mundos) | 3 × 10 = 30 |
| Vuelo | 11: 4 del núcleo (1 inicial y 3 seguimientos) y 7 de mundo | Calidad, Seguridad digital, Riesgos, Primer Equipo y Seguridad y salud, con su seguimiento; Calidad reabierto; Exportación y Franquicias solo se abren | 10 + 3 × 5 + 7 × 5 = 60 |
| **Total** | **14 planes** | | **90**; se siembran **120**, porque las fases 3 y 4 del vuelo apartan 10 cada una al arrancar aunque no generen plan |

Además, el vuelo genera 2 organizadores y 2 reportes, que no cobran créditos.

## Coste estimado (API de Anthropic)

Con las cifras medidas en el vuelo del 27 sep 2026:
- una sesión del núcleo con 13 turnos y su plan: 0,30 USD;
- un turno del intérprete: 0,0104 USD;
- un mundo con su plan: entre 0,18 y 0,29 USD.

| Paso | Base de la cuenta | USD |
|---|---|---|
| A1, preguntas nuevas | 40 × ~0,002 | 0,1 |
| A2, versiones neutrales | 2.940 × 0,0008 a 0,0015, con reintentos | 2,4 a 4,4 |
| B, en la app | 3 núcleos con plan × ~0,33, más 30 mundos × ~5 turnos × ~0,012 | ~2,8 |
| B, el arnés | actor ~200 turnos × 0,002, más juez 3 × ~0,1 | ~0,7 |
| C, vuelo | 1,76 medidos hasta la 2L, más la 2L, la 2M, los reportes y el adaptador | 2,3 a 3 |
| **Total** | | **unos 8 a 11 USD** |

Voyage (la brújula y la prioridad) es otro proveedor y no entra en el saldo de Anthropic: menos de 0,01 USD.

## Cómo se compara con la medición del fundador

**Saldo inicial − saldo final ≈ lo de la app (consulta de abajo) + lo del arnés (informe de coherencia, "El arnés")
+ lo del generador (lo que imprimen A1 y A2).**

La app no guarda las llamadas del arnés ni las del generador, porque se hacen desde la máquina local. Por eso esas dos
cifras las imprime cada script.

La consulta, para pegar y correr en el SQL Editor. Sustituye las dos fechas por la hora de inicio y de fin en UTC:

```sql
-- Corrida final: lo que la app gasto en la IA dentro de la ventana, sesion por sesion (sessions.costo_usd)
SELECT 'TOTAL' AS componente,
       count(*) AS sesiones,
       round(sum(costo_usd)::numeric, 4) AS usd
FROM sessions
WHERE user_id = (SELECT id FROM auth.users WHERE email = 'dev@my-idea.local')
  AND created_at >= '2026-10-01 00:00:00+00'
  AND created_at <  '2026-10-01 23:59:59+00'
UNION ALL
SELECT d.key AS componente,
       count(DISTINCT s.id) AS sesiones,
       round(sum(d.value::numeric), 4) AS usd
FROM sessions s, jsonb_each_text(s.costo_desglose) AS d
WHERE s.user_id = (SELECT id FROM auth.users WHERE email = 'dev@my-idea.local')
  AND s.created_at >= '2026-10-01 00:00:00+00'
  AND s.created_at <  '2026-10-01 23:59:59+00'
GROUP BY d.key
ORDER BY usd DESC;
```

**Diferencias esperables, y por qué:**
- Cada sesión redondea su coste a 4 decimales.
- Las tarifas de `web/lib/costmeter.ts` son las publicadas. Si Anthropic factura distinto, la diferencia aparece aquí
  y se anota.
- La app también cobra el caché (lecturas al 10 %, escrituras de 5 minutos al 125 % y de 1 hora al 200 %), así que ya
  no hay escrituras de caché fuera de la cuenta.

## Al terminar

1. Devolver `LIMITE_ARRANQUES_DIA` y `FUSIBLE_SESIONES_DIA` a su valor.
2. Retirar el `.env`.
3. Anotar el saldo final y comparar con la suma de arriba.
4. Pasar al auditor el informe de coherencia y la exportación del vuelo.
