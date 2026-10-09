# Costes de la corrida final (la app)

Ventana: 2026-10-08T22:58:00Z a 2026-10-08T23:39:00Z. Sesiones: 22.

**Total de la app (suma de sessions.costo_usd): $2.4866**

## Por espacio (núcleo y cada mundo)

| Espacio | USD |
|---|---|
| Tu viaje (núcleo) | $0.9390 |
| Seguridad y Personas | $0.5503 |
| Calidad y Confianza | $0.3251 |
| Seguridad Digital | $0.2570 |
| Riesgos Bajo Control | $0.2413 |
| Primer Equipo | $0.1730 |
| Vender al Mundo | $0.0008 |
| Multiplica tu Negocio | $0.0001 |

## Por sesión

| Proyecto | Espacio | Tipo | USD | Llamadas | Caché leída | Caché escrita |
|---|---|---|---|---|---|---|
| Tengo una idea de una app que ayuda a pe | Tu viaje (núcleo) | gratuito | $0.0009 | 0 | 0 | 0 |
| Quisiera crear un auditor HSEQ virtual,  | Tu viaje (núcleo) | gratuito | $0.0007 | 0 | 0 | 0 |
| Macetas de cemento: descubre si tu preci | Tu viaje (núcleo) | inicial | $0.1510 | 17 | 256289 | 70468 |
| Macetas de cemento: descubre si tu preci | Tu viaje (núcleo) | seguimiento | $0.1258 | 11 | 109420 | 34661 |
| Macetas de cemento: descubre si tu preci | Calidad y Confianza | inicial | $0.1229 | 13 | 137445 | 48673 |
| Macetas de cemento: descubre si tu preci | Vender al Mundo | inicial | $0.0008 | 1 | 1513 | 3587 |
| Macetas de cemento: descubre si tu preci | Multiplica tu Negocio | inicial | $0.0001 | 1 | 5100 | 0 |
| Macetas de cemento: descubre si tu preci | Seguridad Digital | inicial | $0.2570 | 33 | 575512 | 80689 |
| Macetas de cemento: descubre si tu preci | Riesgos Bajo Control | inicial | $0.2413 | 22 | 206017 | 70220 |
| Macetas de cemento: descubre si tu preci | Primer Equipo | inicial | $0.1730 | 15 | 186506 | 67988 |
| Macetas de cemento: descubre si tu preci | Tu viaje (núcleo) | seguimiento | $0.1587 | 12 | 104124 | 55419 |
| Macetas de cemento: descubre si tu preci | Tu viaje (núcleo) | seguimiento | $0.1537 | 10 | 82609 | 53950 |
| Macetas de cemento: descubre si tu preci | Seguridad y Personas | inicial | $0.3284 | 30 | 644956 | 125878 |
| Macetas de cemento: descubre si tu preci | Tu viaje (núcleo) | seguimiento | $0.0068 | 3 | 39181 | 22430 |
| Macetas de cemento: descubre si tu preci | Seguridad y Personas | seguimiento | $0.2219 | 11 | 91040 | 72734 |
| Macetas de cemento: descubre si tu preci | Calidad y Confianza | inicial | $0.2022 | 28 | 627787 | 126237 |
| Tu app de gastos personales: de la idea  | Tu viaje (núcleo) | inicial | $0.0928 | 8 | 32325 | 8585 |
| Tu app de gastos personales: de la idea  | Tu viaje (núcleo) | reporte | $0.0249 | 0 | 0 | 0 |
| Valida si registrar gastos es un problem | Tu viaje (núcleo) | inicial | $0.1094 | 8 | 34340 | 7309 |
| Valida si registrar gastos es un problem | Tu viaje (núcleo) | reporte | $0.0148 | 0 | 0 | 0 |
| Tu pieza hecha a mano: comprueba que alg | Tu viaje (núcleo) | inicial | $0.0995 | 8 | 32417 | 9675 |
| Tu pieza hecha a mano: comprueba que alg | Tu viaje (núcleo) | reporte | $0.0000 | 0 | 0 | 0 |

## Por modelo (del registro llamada por llamada)

| Modelo | Llamadas | USD |
|---|---|---|
| claude-haiku-5-5 | 148 | $0.1977 |
| claude-sonnet-5-5 | 83 | $2.2476 |

## La consulta para cuadrar con la medición del fundador (SQL Editor)

```sql
SELECT count(*) AS sesiones, round(sum(costo_usd)::numeric, 4) AS usd
FROM sessions
WHERE user_id = (SELECT id FROM auth.users WHERE email = '[correo del dev user]')
  AND created_at >= '2026-10-08T22:58:00Z' AND created_at < '2026-10-08T23:39:00Z';
```
