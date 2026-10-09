# Costes de la corrida final (la app)

Ventana: 2026-10-08T13:02:00Z a 2026-10-08T13:31:30Z. Sesiones: 33.

**Total de la app (suma de sessions.costo_usd): $2.7189**

## Por espacio (núcleo y cada mundo)

| Espacio | USD |
|---|---|
| Riesgos Bajo Control | $1.1644 |
| Seguridad Digital | $0.5081 |
| Tu viaje (núcleo) | $0.3260 |
| Seguridad y Personas | $0.3168 |
| Primer Equipo | $0.0969 |
| Del Taller a sus Manos | $0.0695 |
| Tu Compra Correcta | $0.0617 |
| Vender al Mundo | $0.0576 |
| Calidad y Confianza | $0.0509 |
| Multiplica tu Negocio | $0.0349 |
| Ambiente y Futuro | $0.0321 |

## Por sesión

| Proyecto | Espacio | Tipo | USD | Llamadas | Caché leída | Caché escrita |
|---|---|---|---|---|---|---|
| Pasteles por encargo: comprueba si tu ca | Tu viaje (núcleo) | inicial | $0.1465 | 20 | 659976 | 73235 |
| Pasteles por encargo: comprueba si tu ca | Calidad y Confianza | inicial | $0.0173 | 13 | 524854 | 71261 |
| Pasteles por encargo: comprueba si tu ca | Seguridad y Personas | inicial | $0.1583 | 27 | 672976 | 83290 |
| Pasteles por encargo: comprueba si tu ca | Ambiente y Futuro | inicial | $0.0079 | 5 | 118314 | 36825 |
| Pasteles por encargo: comprueba si tu ca | Seguridad Digital | inicial | $0.1992 | 26 | 687156 | 94914 |
| Pasteles por encargo: comprueba si tu ca | Vender al Mundo | inicial | $0.0230 | 15 | 641171 | 82330 |
| Pasteles por encargo: comprueba si tu ca | Multiplica tu Negocio | inicial | $0.0159 | 9 | 348458 | 68133 |
| Pasteles por encargo: comprueba si tu ca | Riesgos Bajo Control | inicial | $0.3479 | 20 | 540452 | 138453 |
| Pasteles por encargo: comprueba si tu ca | Tu Compra Correcta | inicial | $0.0262 | 14 | 612931 | 103466 |
| Pasteles por encargo: comprueba si tu ca | Del Taller a sus Manos | inicial | $0.0285 | 15 | 699708 | 112564 |
| Pasteles por encargo: comprueba si tu ca | Primer Equipo | inicial | $0.0366 | 19 | 986588 | 133135 |
| De ejecutar a dirigir: cómo hacer que tu | Tu viaje (núcleo) | inicial | $0.0801 | 8 | 31746 | 9592 |
| De ejecutar a dirigir: cómo hacer que tu | Calidad y Confianza | inicial | $0.0124 | 13 | 341990 | 47712 |
| De ejecutar a dirigir: cómo hacer que tu | Seguridad y Personas | inicial | $0.0845 | 18 | 322183 | 52964 |
| De ejecutar a dirigir: cómo hacer que tu | Ambiente y Futuro | inicial | $0.0174 | 16 | 413649 | 56945 |
| De ejecutar a dirigir: cómo hacer que tu | Seguridad Digital | inicial | $0.1506 | 26 | 534095 | 82528 |
| De ejecutar a dirigir: cómo hacer que tu | Vender al Mundo | inicial | $0.0115 | 6 | 187425 | 54815 |
| De ejecutar a dirigir: cómo hacer que tu | Multiplica tu Negocio | inicial | $0.0118 | 7 | 193878 | 48644 |
| De ejecutar a dirigir: cómo hacer que tu | Riesgos Bajo Control | inicial | $0.6308 | 29 | 675994 | 241422 |
| De ejecutar a dirigir: cómo hacer que tu | Tu Compra Correcta | inicial | $0.0176 | 8 | 219892 | 74486 |
| De ejecutar a dirigir: cómo hacer que tu | Del Taller a sus Manos | inicial | $0.0296 | 19 | 797215 | 107944 |
| De ejecutar a dirigir: cómo hacer que tu | Primer Equipo | inicial | $0.0374 | 19 | 791323 | 131809 |
| Propuesta de entregas el mismo día desde | Tu viaje (núcleo) | inicial | $0.0994 | 14 | 158246 | 23986 |
| Propuesta de entregas el mismo día desde | Calidad y Confianza | inicial | $0.0212 | 16 | 635861 | 73335 |
| Propuesta de entregas el mismo día desde | Seguridad y Personas | inicial | $0.0740 | 12 | 181774 | 41321 |
| Propuesta de entregas el mismo día desde | Ambiente y Futuro | inicial | $0.0068 | 5 | 105795 | 31018 |
| Propuesta de entregas el mismo día desde | Seguridad Digital | inicial | $0.1583 | 29 | 651496 | 91886 |
| Propuesta de entregas el mismo día desde | Vender al Mundo | inicial | $0.0231 | 15 | 591715 | 88829 |
| Propuesta de entregas el mismo día desde | Multiplica tu Negocio | inicial | $0.0072 | 3 | 46958 | 34112 |
| Propuesta de entregas el mismo día desde | Riesgos Bajo Control | inicial | $0.1857 | 18 | 453266 | 94609 |
| Propuesta de entregas el mismo día desde | Tu Compra Correcta | inicial | $0.0179 | 9 | 283386 | 77467 |
| Propuesta de entregas el mismo día desde | Del Taller a sus Manos | inicial | $0.0114 | 5 | 137201 | 52296 |
| Propuesta de entregas el mismo día desde | Primer Equipo | inicial | $0.0229 | 13 | 441257 | 97369 |

## Por modelo (del registro llamada por llamada)

| Modelo | Llamadas | USD |
|---|---|---|
| claude-haiku-5-5 | 384 | $0.5950 |
| claude-sonnet-5-5 | 107 | $2.1240 |

## La consulta para cuadrar con la medición del fundador (SQL Editor)

```sql
SELECT count(*) AS sesiones, round(sum(costo_usd)::numeric, 4) AS usd
FROM sessions
WHERE user_id = (SELECT id FROM auth.users WHERE email = '[correo del dev user]')
  AND created_at >= '2026-10-08T13:02:00Z' AND created_at < '2026-10-08T13:31:30Z';
```
