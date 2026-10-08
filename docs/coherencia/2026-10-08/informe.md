# Prueba de coherencia, 2026-10-08T13:02:06.782Z

**Dictamen:** NO CUMPLE
- continuidad: sola, de core a quality: el primer mundo abrio con la ficha en papel 'desconocido', el retrato 'dueno'
- continuidad: dos_empleados, de core a quality: el primer mundo abrio con la ficha en papel 'desconocido', el retrato 'dueno'
- ficha: sola, tras core: la ficha dice papel 'desconocido', el retrato 'dueno'
- ficha: sola, tras core: la ficha dice tiene_jefe null, el retrato false
- ficha: sola, tras quality: la ficha dice papel 'desconocido', el retrato 'dueno'
- ficha: sola, tras quality: la ficha dice tiene_jefe null, el retrato false
- ficha: sola, tras health_safety: la ficha dice papel 'desconocido', el retrato 'dueno'
- ficha: sola, tras health_safety: la ficha dice tiene_jefe null, el retrato false
- ficha: sola, tras environmental: la ficha dice papel 'desconocido', el retrato 'dueno'
- ficha: sola, tras environmental: la ficha dice tiene_jefe null, el retrato false
- ficha: sola, tras seguridad_digital: la ficha dice papel 'desconocido', el retrato 'dueno'
- ficha: sola, tras seguridad_digital: la ficha dice tiene_jefe null, el retrato false
- ficha: sola, tras risk_management: la ficha dice tiene_jefe true, el retrato false
- ficha: sola, tras compras: la ficha dice tiene_jefe true, el retrato false
- ficha: sola, tras entrega: la ficha dice tiene_jefe true, el retrato false
- ficha: sola, tras primer_equipo: la ficha dice tiene_jefe true, el retrato false
- ficha: dos_empleados, tras core: la ficha dice papel 'desconocido', el retrato 'dueno'
- ficha: dos_empleados, tras core: la ficha dice tiene_jefe null, el retrato false
- ficha: dos_empleados, tras quality: la ficha dice papel 'desconocido', el retrato 'dueno'
- ficha: dos_empleados, tras quality: la ficha dice tiene_jefe null, el retrato false
- ficha: dos_empleados, tras health_safety: la ficha dice papel 'desconocido', el retrato 'dueno'
- ficha: dos_empleados, tras health_safety: la ficha dice tiene_jefe null, el retrato false

| Condicion | Cumple |
|---|---|
| Juez ciego (umbral del fundador) | si |
| Continuidad desde el nucleo, con todas las respuestas | no |
| Ficha con el papel y el jefe del retrato | no |
| Hilo: las respuestas dadas, en orden, creciendo al final | si |
| Contexto en cada llamada (491 de 491; lista blanca: organizadores) | si |
| Cache (ahorro, lecturas, escritura de 1 h por persona, turno mas barato) | si |

Ventana: 2026-10-08T13:02:06.782Z a 2026-10-08T13:31:00.261Z

| Persona | Preguntas | Papel | Contexto | Adaptadas fieles | Trampas |
|---|---|---|---|---|---|
| sola | 112 | 0 | 1 | 12 de 12 | 4 de 4 |
| dos_empleados | 89 | 0 | 1 | 18 de 18 | 4 de 4 |
| empleado_mediana | 86 | 0 | 0 | 14 de 14 | 4 de 4 |

## Coste

- Dentro de la app (sessions.costo_usd): 2.7189 USD
- El arnes (actor y juez): 0.2414 USD
- Cache: con cache 2.7190 USD, sin cache 4.6549 USD, ahorro 1.9358 USD
- Turno del interprete: antes 0.0104 USD, ahora 0.0015 USD

| Persona | Espacio | Turnos | USD |
|---|---|---|---|
| sola | core | 12 | 0.1465 |
| sola | quality | 12 | 0.0173 |
| sola | health_safety | 12 | 0.1583 |
| sola | environmental | 4 | 0.0079 |
| sola | seguridad_digital | 12 | 0.1992 |
| sola | exportacion | 6 | 0.0230 |
| sola | franquicias | 8 | 0.0159 |
| sola | risk_management | 10 | 0.3479 |
| sola | compras | 12 | 0.0262 |
| sola | entrega | 12 | 0.0285 |
| sola | primer_equipo | 8 | 0.0366 |
| dos_empleados | core | 1 | 0.0801 |
| dos_empleados | quality | 11 | 0.0124 |
| dos_empleados | health_safety | 9 | 0.0845 |
| dos_empleados | environmental | 11 | 0.0174 |
| dos_empleados | seguridad_digital | 12 | 0.1506 |
| dos_empleados | exportacion | 5 | 0.0115 |
| dos_empleados | franquicias | 5 | 0.0118 |
| dos_empleados | risk_management | 12 | 0.6308 |
| dos_empleados | compras | 5 | 0.0176 |
| dos_empleados | entrega | 5 | 0.0296 |
| dos_empleados | primer_equipo | 12 | 0.0374 |
| empleado_mediana | core | 4 | 0.0994 |
| empleado_mediana | quality | 12 | 0.0212 |
| empleado_mediana | health_safety | 5 | 0.0740 |
| empleado_mediana | environmental | 4 | 0.0068 |
| empleado_mediana | seguridad_digital | 12 | 0.1583 |
| empleado_mediana | exportacion | 12 | 0.0231 |
| empleado_mediana | franquicias | 2 | 0.0072 |
| empleado_mediana | risk_management | 9 | 0.1857 |
| empleado_mediana | compras | 6 | 0.0179 |
| empleado_mediana | entrega | 4 | 0.0114 |
| empleado_mediana | primer_equipo | 12 | 0.0229 |
