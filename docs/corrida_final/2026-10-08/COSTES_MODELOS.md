# Costes por modelo: la corrida final contra el vuelo del 27 de septiembre

## La cifra oficial: la consola del fundador

El coste oficial de la corrida es el que marca la consola de Anthropic del fundador, no la suma de `costo_usd`:

| | USD | Hora (UTC) |
|---|---:|---|
| Saldo inicial de referencia | 19,67 | 8 oct 2026, 01:05 |
| Saldo final | pendiente (lo anota el fundador) |  |
| Coste oficial de la corrida | pendiente | |

La consola incluye todo lo que corrió con la clave en el día (la caché de preguntas, sus jueces, las neutrales, la
coherencia, cada intento del vuelo y la medición del anclaje). `costo_usd` de la app queda solo como DESGLOSE por pieza
y por modelo, que es lo que decide qué modelo usa cada pieza.

## El desglose

De esta medición depende qué modelo usa cada pieza de la app. Todo sale de los volcados de coste de esta carpeta
(solo números, sin textos de usuario). El coste por modelo se recalcula con `costoLlamadaUsd` de `web/lib/costmeter.ts`:
los mismos precios y multiplicadores de caché que usa la app para cobrar.

Precios por millón de tokens (entrada / salida), tal como están en `PRECIOS`:

| Modelo | Entrada | Salida |
|---|---:|---:|
| claude-sonnet-5-5 | $2.00 | $10.00 |
| claude-haiku-5-5 | $0.10 | $0.50 |
| claude-sonnet-4-6 | $3.00 | $15.00 |
| claude-haiku-4-5 | $1.00 | $5.00 |

## 1. Resumen por corrida

| Corrida | Sesiones | Total | Media por sesión | p50 | p95 | Máxima |
|---|---:|---:|---:|---:|---:|---:|
| Vuelo 27 sep (Sonnet 4.6 + Haiku 4.5) | 28 | $3.5841 | $0.1280 | $0.1311 | $0.3140 | $0.3264 |
| Coherencia 8 oct (5.5, antes del arreglo del anclaje) | 33 | $2.7189 | $0.0824 | $0.0262 | $0.3479 | $0.6308 |
| Vuelo 8 oct, intento 1 (paro en 2i) | 10 | $1.2858 | $0.1286 | $0.1096 | $0.4066 | $0.4066 |
| Vuelo 8 oct, intento 2 (paro en 2j) | 12 | $1.7799 | $0.1483 | $0.1233 | $0.3898 | $0.3898 |
| Vuelo 8 oct, intento 3 (paro en 2f, sin creditos) | 3 | $0.1484 | $0.0495 | $0.0009 | $0.1468 | $0.1468 |
| Vuelo FINAL validado (intento 10 + fases 3 y 4) | 22 | $2.4866 | $0.1130 | $0.1094 | $0.2570 | $0.3284 |

Las corridas no tienen la misma mezcla de sesiones (cuántos seguimientos, qué mundos, cuántos turnos), así que el
total no se compara a ciegas: la comparación más justa es por pieza (sección 3) y por llamada (sección 4).

## 2. Por modelo

### Vuelo 27 sep (Sonnet 4.6 + Haiku 4.5)

| Modelo | Llamadas | Entrada | Salida | Caché leída | Caché escrita 5 min | Caché escrita 1 h | Coste | Coste por llamada |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| claude-haiku-4-5 | 151 | 221.878 | 65.799 | 1.918.248 | 316.151 | 0 | $1.1379 | $0.00754 |
| claude-sonnet-4-6 | 106 | 354.544 | 98.058 | 87.015 | 11.602 | 0 | $2.6041 | $0.02457 |

### Coherencia 8 oct (5.5, antes del arreglo del anclaje)

| Modelo | Llamadas | Entrada | Salida | Caché leída | Caché escrita 5 min | Caché escrita 1 h | Coste | Coste por llamada |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| claude-haiku-5-5 | 384 | 243.696 | 146.171 | 13.945.354 | 1.385.621 | 924.595 | $0.5950 | $0.00155 |
| claude-sonnet-5-5 | 107 | 278.913 | 28.192 | 743.575 | 0 | 302.479 | $2.1240 | $0.01985 |

### Vuelo 8 oct, intento 1 (paro en 2i)

| Modelo | Llamadas | Entrada | Salida | Caché leída | Caché escrita 5 min | Caché escrita 1 h | Coste | Coste por llamada |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| claude-haiku-5-5 | 96 | 207.063 | 40.951 | 1.844.581 | 214.946 | 104.645 | $0.1074 | $0.00112 |
| claude-sonnet-5-5 | 47 | 165.897 | 40.912 | 177.490 | 0 | 104.554 | $1.1769 | $0.02504 |

### Vuelo 8 oct, intento 2 (paro en 2j)

| Modelo | Llamadas | Entrada | Salida | Caché leída | Caché escrita 5 min | Caché escrita 1 h | Coste | Coste por llamada |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| claude-haiku-5-5 | 144 | 355.441 | 64.546 | 3.487.924 | 322.226 | 268.778 | $0.1967 | $0.00137 |
| claude-sonnet-5-5 | 62 | 257.582 | 52.134 | 343.690 | 0 | 127.701 | $1.5817 | $0.02551 |

### Vuelo 8 oct, intento 3 (paro en 2f, sin creditos)

| Modelo | Llamadas | Entrada | Salida | Caché leída | Caché escrita 5 min | Caché escrita 1 h | Coste | Coste por llamada |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| claude-haiku-5-5 | 12 | 9845 | 6079 | 276.586 | 40.575 | 21.208 | $0.0161 | $0.00134 |
| claude-sonnet-5-5 | 4 | 17.101 | 4878 | 4282 | 0 | 11.831 | $0.1307 | $0.03268 |

### Vuelo FINAL validado (intento 10 + fases 3 y 4)

| Modelo | Llamadas | Entrada | Salida | Caché leída | Caché escrita 5 min | Caché escrita 1 h | Coste | Coste por llamada |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| claude-haiku-5-5 | 148 | 277.788 | 64.673 | 2.732.716 | 343.544 | 336.521 | $0.1977 | $0.00134 |
| claude-sonnet-5-5 | 83 | 334.533 | 82.144 | 433.865 | 0 | 178.438 | $2.2476 | $0.02708 |

## 3. Por pieza (componente)

| Pieza | Vuelo 27 sep (Sonnet 4.6 + Haiku 4.5) | Coherencia 8 oct (5.5, antes del arreglo del anclaje) | Vuelo 8 oct, intento 1 (paro en 2i) | Vuelo 8 oct, intento 2 (paro en 2j) | Vuelo 8 oct, intento 3 (paro en 2f, sin creditos) | Vuelo FINAL validado (intento 10 + fases 3 y 4) |
|---|---:|---:|---:|---:|---:|---:|
| adaptador |  | $0.1249 (30 ses.) | $0.0100 (7 ses.) | $0.0199 (6 ses.) |  | $0.0206 (9 ses.) |
| anclaje_proteccion | $0.2258 (5 ses.) | $1.8301 (9 ses.) | $0.3132 (2 ses.) | $0.2349 (2 ses.) |  | $0.2290 (3 ses.) |
| clasificacion | $0.0547 (8 ses.) | $0.0013 (3 ses.) | $0.0023 (2 ses.) | $0.0097 (4 ses.) | $0.0007 (1 ses.) | $0.0153 (9 ses.) |
| enlace_proteccion | $0.2109 (5 ses.) |  | $0.1212 (2 ses.) | $0.0988 (2 ses.) |  | $0.2027 (4 ses.) |
| estado_vivo | $0.0699 (17 ses.) | $0.0020 (3 ses.) | $0.0103 (6 ses.) | $0.0188 (8 ses.) | $0.0009 (1 ses.) | $0.0269 (14 ses.) |
| estimacion_banda | $0.6994 (17 ses.) | $0.1074 (3 ses.) | $0.2772 (6 ses.) | $0.4790 (8 ses.) | $0.0377 (1 ses.) | $0.7374 (14 ses.) |
| juez_sesion | $0.0617 (13 ses.) | $0.0018 (3 ses.) | $0.0106 (6 ses.) | $0.0195 (8 ses.) | $0.0012 (1 ses.) | $0.0221 (14 ses.) |
| organizador | $0.0205 (4 ses.) |  | $0.0015 (2 ses.) | $0.0016 (2 ses.) | $0.0016 (2 ses.) | $0.0016 (2 ses.) |
| plan | $1.3974 (17 ses.) | $0.1865 (3 ses.) | $0.4652 (6 ses.) | $0.7690 (8 ses.) | $0.0930 (1 ses.) | $1.0785 (14 ses.) |
| reporte |  |  |  |  |  | $0.0398 (2 ses.) |
| turnos | $0.8438 (13 ses.) | $0.4649 (33 ses.) | $0.0743 (6 ses.) | $0.1288 (8 ses.) | $0.0134 (1 ses.) | $0.1127 (15 ses.) |

## 4. Por llamada (pieza × modelo)

El registro llamada por llamada existe desde la corrida con los modelos 5.5. Media por llamada:

### Coherencia 8 oct (5.5, antes del arreglo del anclaje)

| Pieza · modelo | Llamadas | Coste por llamada | Entrada media | Salida media | Caché leída media |
|---|---:|---:|---:|---:|---:|
| anclaje_proteccion · claude-sonnet-5-5 | 95 | $0.01926 | 2305 | 126 | 7397 |
| turnos · claude-haiku-5-5 | 316 | $0.00147 | 657 | 419 | 43.318 |
| plan · claude-sonnet-5-5 | 3 | $0.06218 | 13.087 | 3387 | 8909 |
| adaptador · claude-haiku-5-5 | 58 | $0.00215 | 149 | 178 | 4168 |
| estimacion_banda · claude-sonnet-5-5 | 9 | $0.01193 | 2294 | 677 | 1568 |
| estado_vivo · claude-haiku-5-5 | 4 | $0.00051 | 1482 | 604 | 1505 |
| juez_sesion · claude-haiku-5-5 | 3 | $0.00061 | 4357 | 191 | 1864 |
| clasificacion · claude-haiku-5-5 | 3 | $0.00043 | 2864 | 167 | 1159 |

### Vuelo 8 oct, intento 1 (paro en 2i)

| Pieza · modelo | Llamadas | Coste por llamada | Entrada media | Salida media | Caché leída media |
|---|---:|---:|---:|---:|---:|
| plan · claude-sonnet-5-5 | 6 | $0.07753 | 14.072 | 3480 | 8786 |
| anclaje_proteccion · claude-sonnet-5-5 | 20 | $0.01566 | 1705 | 134 | 2740 |
| estimacion_banda · claude-sonnet-5-5 | 18 | $0.01540 | 2099 | 628 | 3522 |
| enlace_proteccion · claude-sonnet-5-5 | 3 | $0.04041 | 3194 | 2017 | 2195 |
| turnos · claude-haiku-5-5 | 62 | $0.00120 | 2019 | 439 | 28.263 |
| juez_sesion · claude-haiku-5-5 | 9 | $0.00117 | 4962 | 379 | 3106 |
| estado_vivo · claude-haiku-5-5 | 10 | $0.00103 | 2223 | 725 | 3081 |
| adaptador · claude-haiku-5-5 | 13 | $0.00077 | 169 | 198 | 2499 |
| clasificacion · claude-haiku-5-5 | 2 | $0.00113 | 6398 | 243 | 518 |

### Vuelo 8 oct, intento 2 (paro en 2j)

| Pieza · modelo | Llamadas | Coste por llamada | Entrada media | Salida media | Caché leída media |
|---|---:|---:|---:|---:|---:|
| plan · claude-sonnet-5-5 | 8 | $0.09613 | 15.515 | 3565 | 7688 |
| estimacion_banda · claude-sonnet-5-5 | 24 | $0.01996 | 2224 | 669 | 5233 |
| anclaje_proteccion · claude-sonnet-5-5 | 28 | $0.00839 | 2616 | 134 | 5532 |
| turnos · claude-haiku-5-5 | 93 | $0.00138 | 2294 | 487 | 35.356 |
| enlace_proteccion · claude-sonnet-5-5 | 2 | $0.04938 | 3417 | 1903 | 845 |
| adaptador · claude-haiku-5-5 | 23 | $0.00087 | 147 | 184 | 4443 |
| juez_sesion · claude-haiku-5-5 | 11 | $0.00178 | 6444 | 369 | 3331 |
| estado_vivo · claude-haiku-5-5 | 13 | $0.00144 | 2487 | 763 | 4486 |
| clasificacion · claude-haiku-5-5 | 4 | $0.00243 | 8872 | 250 | 668 |

### Vuelo 8 oct, intento 3 (paro en 2f, sin creditos)

| Pieza · modelo | Llamadas | Coste por llamada | Entrada media | Salida media | Caché leída media |
|---|---:|---:|---:|---:|---:|
| plan · claude-sonnet-5-5 | 1 | $0.09300 | 11.293 | 3165 | 0 |
| estimacion_banda · claude-sonnet-5-5 | 3 | $0.01258 | 1936 | 571 | 1427 |
| turnos · claude-haiku-5-5 | 9 | $0.00148 | 4 | 563 | 30.732 |
| juez_sesion · claude-haiku-5-5 | 1 | $0.00122 | 5717 | 230 | 0 |
| estado_vivo · claude-haiku-5-5 | 1 | $0.00087 | 1219 | 610 | 0 |
| clasificacion · claude-haiku-5-5 | 1 | $0.00066 | 2873 | 169 | 0 |

### Vuelo FINAL validado (intento 10 + fases 3 y 4)

| Pieza · modelo | Llamadas | Coste por llamada | Entrada media | Salida media | Caché leída media |
|---|---:|---:|---:|---:|---:|
| plan · claude-sonnet-5-5 | 14 | $0.07704 | 11.942 | 3191 | 8514 |
| estimacion_banda · claude-sonnet-5-5 | 42 | $0.01756 | 2220 | 665 | 4197 |
| anclaje_proteccion · claude-sonnet-5-5 | 23 | $0.00996 | 2626 | 132 | 5798 |
| enlace_proteccion · claude-sonnet-5-5 | 4 | $0.05066 | 3428 | 1625 | 1267 |
| turnos · claude-haiku-5-5 | 81 | $0.00139 | 1301 | 447 | 31.414 |
| estado_vivo · claude-haiku-5-5 | 23 | $0.00117 | 1943 | 770 | 3805 |
| juez_sesion · claude-haiku-5-5 | 17 | $0.00130 | 3545 | 327 | 2975 |
| adaptador · claude-haiku-5-5 | 18 | $0.00115 | 165 | 185 | 2296 |
| clasificacion · claude-haiku-5-5 | 9 | $0.00170 | 7162 | 203 | 979 |

## 5. Por sesión y por espacio

### Vuelo 27 sep (Sonnet 4.6 + Haiku 4.5)

| Tipo · espacio | Sesiones | Media | Máxima |
|---|---:|---:|---:|
| gratuito · core | 4 | $0.0051 | $0.0062 |
| inicial · core | 2 | $0.3082 | $0.3140 |
| inicial · exportacion | 2 | $0.0000 | $0.0000 |
| inicial · franquicias | 2 | $0.0000 | $0.0000 |
| inicial · health_safety | 2 | $0.1181 | $0.2362 |
| inicial · primer_equipo | 2 | $0.2027 | $0.2226 |
| inicial · quality | 2 | $0.1774 | $0.1797 |
| inicial · risk_management | 2 | $0.3094 | $0.3264 |
| inicial · seguridad_digital | 2 | $0.2319 | $0.2626 |
| seguimiento · core | 7 | $0.1241 | $0.2385 |
| seguimiento · health_safety | 1 | $0.0000 | $0.0000 |

### Coherencia 8 oct (5.5, antes del arreglo del anclaje)

| Tipo · espacio | Sesiones | Media | Máxima |
|---|---:|---:|---:|
| inicial · compras | 3 | $0.0206 | $0.0262 |
| inicial · core | 3 | $0.1087 | $0.1465 |
| inicial · entrega | 3 | $0.0232 | $0.0296 |
| inicial · environmental | 3 | $0.0107 | $0.0174 |
| inicial · exportacion | 3 | $0.0192 | $0.0231 |
| inicial · franquicias | 3 | $0.0116 | $0.0159 |
| inicial · health_safety | 3 | $0.1056 | $0.1583 |
| inicial · primer_equipo | 3 | $0.0323 | $0.0374 |
| inicial · quality | 3 | $0.0170 | $0.0212 |
| inicial · risk_management | 3 | $0.3881 | $0.6308 |
| inicial · seguridad_digital | 3 | $0.1694 | $0.1992 |

### Vuelo 8 oct, intento 1 (paro en 2i)

| Tipo · espacio | Sesiones | Media | Máxima |
|---|---:|---:|---:|
| gratuito · core | 2 | $0.0008 | $0.0008 |
| inicial · core | 1 | $0.1155 | $0.1155 |
| inicial · exportacion | 1 | $0.0008 | $0.0008 |
| inicial · franquicias | 1 | $0.0002 | $0.0002 |
| inicial · primer_equipo | 1 | $0.1653 | $0.1653 |
| inicial · quality | 1 | $0.1248 | $0.1248 |
| inicial · risk_management | 1 | $0.4066 | $0.4066 |
| inicial · seguridad_digital | 1 | $0.3615 | $0.3615 |
| seguimiento · core | 1 | $0.1096 | $0.1096 |

### Vuelo 8 oct, intento 2 (paro en 2j)

| Tipo · espacio | Sesiones | Media | Máxima |
|---|---:|---:|---:|
| gratuito · core | 2 | $0.0008 | $0.0008 |
| inicial · core | 1 | $0.1389 | $0.1389 |
| inicial · exportacion | 1 | $0.0008 | $0.0008 |
| inicial · franquicias | 1 | $0.0001 | $0.0001 |
| inicial · primer_equipo | 1 | $0.2871 | $0.2871 |
| inicial · quality | 1 | $0.1233 | $0.1233 |
| inicial · risk_management | 1 | $0.3898 | $0.3898 |
| inicial · seguridad_digital | 1 | $0.3031 | $0.3031 |
| seguimiento · core | 3 | $0.1784 | $0.2115 |

### Vuelo 8 oct, intento 3 (paro en 2f, sin creditos)

| Tipo · espacio | Sesiones | Media | Máxima |
|---|---:|---:|---:|
| gratuito · core | 2 | $0.0008 | $0.0009 |
| inicial · core | 1 | $0.1468 | $0.1468 |

### Vuelo FINAL validado (intento 10 + fases 3 y 4)

| Tipo · espacio | Sesiones | Media | Máxima |
|---|---:|---:|---:|
| gratuito · core | 2 | $0.0008 | $0.0009 |
| inicial · core | 4 | $0.1132 | $0.1510 |
| inicial · exportacion | 1 | $0.0008 | $0.0008 |
| inicial · franquicias | 1 | $0.0001 | $0.0001 |
| inicial · health_safety | 1 | $0.3284 | $0.3284 |
| inicial · primer_equipo | 1 | $0.1730 | $0.1730 |
| inicial · quality | 2 | $0.1626 | $0.2022 |
| inicial · risk_management | 1 | $0.2413 | $0.2413 |
| inicial · seguridad_digital | 1 | $0.2570 | $0.2570 |
| reporte · core | 3 | $0.0132 | $0.0249 |
| seguimiento · core | 4 | $0.1112 | $0.1587 |
| seguimiento · health_safety | 1 | $0.2219 | $0.2219 |

## 6. Caché

Lo que costaría la caché leída si se pagara como entrada normal, contra lo que costó de verdad:

| Corrida | Modelo | Caché leída | Pagado por leerla | Habría costado sin caché | Ahorro |
|---|---|---:|---:|---:|---:|
| Vuelo 27 sep (Sonnet 4.6 + Haiku 4.5) | claude-haiku-4-5 | 1.918.248 | $0.1918 | $1.9182 | $1.7264 |
| Vuelo 27 sep (Sonnet 4.6 + Haiku 4.5) | claude-sonnet-4-6 | 87.015 | $0.0261 | $0.2610 | $0.2349 |
| Coherencia 8 oct (5.5, antes del arreglo del anclaje) | claude-haiku-5-5 | 13.945.354 | $0.1395 | $1.3945 | $1.2551 |
| Coherencia 8 oct (5.5, antes del arreglo del anclaje) | claude-sonnet-5-5 | 743.575 | $0.0744 | $1.4871 | $1.4128 |
| Vuelo 8 oct, intento 1 (paro en 2i) | claude-haiku-5-5 | 1.844.581 | $0.0184 | $0.1845 | $0.1660 |
| Vuelo 8 oct, intento 1 (paro en 2i) | claude-sonnet-5-5 | 177.490 | $0.0177 | $0.3550 | $0.3372 |
| Vuelo 8 oct, intento 2 (paro en 2j) | claude-haiku-5-5 | 3.487.924 | $0.0349 | $0.3488 | $0.3139 |
| Vuelo 8 oct, intento 2 (paro en 2j) | claude-sonnet-5-5 | 343.690 | $0.0344 | $0.6874 | $0.6530 |
| Vuelo 8 oct, intento 3 (paro en 2f, sin creditos) | claude-haiku-5-5 | 276.586 | $0.0028 | $0.0277 | $0.0249 |
| Vuelo 8 oct, intento 3 (paro en 2f, sin creditos) | claude-sonnet-5-5 | 4282 | $0.0004 | $0.0086 | $0.0081 |
| Vuelo FINAL validado (intento 10 + fases 3 y 4) | claude-haiku-5-5 | 2.732.716 | $0.0273 | $0.2733 | $0.2459 |
| Vuelo FINAL validado (intento 10 + fases 3 y 4) | claude-sonnet-5-5 | 433.865 | $0.0434 | $0.8677 | $0.8243 |

### El hallazgo del anclaje de protección

En la coherencia, el anclaje de los mundos de protección fue la pieza más cara: la foto del proyecto y la ficha de
cada turno viajaban juntas en el bloque con caché de 1 hora, así que el bloque se reescribía (a 2× la entrada) en
cada turno. Arreglo (main 0908caa7a): solo la parte fija va en caché; la ficha viaja aparte, sin caché. Medido con la
misma sesión real antes y después:

```
ANTES   (foto + ficha en el bloque de 1 hora): $0.4712 | por llamada $0.0590 $0.0588 $0.0586 $0.0591 $0.0590 $0.0590 $0.0589 $0.0587
  uso: {"claude-sonnet-5-5":{"in":14522,"out":1009,"cache_read":10816,"cache_write":0,"cache_write_1h":107736,"llamadas":8}}
DESPUES (foto en cache, ficha aparte):          $0.1057 | por llamada $0.0583 $0.0067 $0.0068 $0.0069 $0.0067 $0.0069 $0.0066 $0.0069
  uso: {"claude-sonnet-5-5":{"in":16386,"out":969,"cache_read":103447,"cache_write":0,"cache_write_1h":13233,"llamadas":8}}
AHORRO: $0.3654 (77.6 %) en 8 anclajes
```

## 7. El tope por sesión

Visto del fundador (8 oct 2026): USD 1,00 por defecto en el código; al alcanzarlo la entrevista se cierra ordenada y el
plan que arranca se termina entero (margen de USD 0,50). Sesiones que habrían tocado cada valor:

| Corrida | Sesiones | > 0,35 | > 1,00 | Máxima |
|---|---:|---:|---:|---:|
| Vuelo 27 sep (Sonnet 4.6 + Haiku 4.5) | 28 | 0 | 0 | $0.3264 |
| Coherencia 8 oct (5.5, antes del arreglo del anclaje) | 33 | 1 | 0 | $0.6308 |
| Vuelo 8 oct, intento 1 (paro en 2i) | 10 | 2 | 0 | $0.4066 |
| Vuelo 8 oct, intento 2 (paro en 2j) | 12 | 1 | 0 | $0.3898 |
| Vuelo 8 oct, intento 3 (paro en 2f, sin creditos) | 3 | 0 | 0 | $0.1468 |
| Vuelo FINAL validado (intento 10 + fases 3 y 4) | 22 | 0 | 0 | $0.3284 |

## 8. La consulta de costo_usd

Para repetir las cuentas en el SQL Editor de Supabase (cambia la ventana):

```sql
select tipo, dominio, count(*) as sesiones, round(sum(costo_usd)::numeric, 4) as total_usd,
       round(avg(costo_usd)::numeric, 4) as media_usd, round(max(costo_usd)::numeric, 4) as maxima_usd
from sessions
where user_id = '4a05a687-fc7e-4427-8eaf-cc1cc1644678'
  and created_at >= '2026-10-08T13:02:00Z' and created_at < '2026-10-09T00:00:00Z'
group by tipo, dominio
order by tipo, dominio;
```


## 9. La medición barata A/B (9 oct 2026)

Redactar de nuevo los 14 planes del vuelo desde sus entrevistas guardadas (sin guardar nada) y pasar cada uno por el
verificador de planes (Sonnet 5.5, sin desplegar). Cifras de `medicion_ab/costes.json`; jueces y árbitros corrieron
fuera de la API del producto.

| Pieza | USD | Por plan (media) |
|---|---:|---:|
| Redactor (un borrador por plan, compartido por A y B) | 1,1161 | 0,0797 |
| Verificador (Sonnet 5.5) | 0,7502 | 0,0536 |
| **Total** | **1,8664** | 0,1333 |

El verificador sube el coste del plan en torno a un 67 % sobre el redactor (0,0536 contra 0,0797 USD por plan; mínimo
0,0308, máximo 0,0893 en el plan de Primer Equipo). Propuso 88 correcciones y aplicó 85 (3 ignoradas), ninguna a
revisión. **Resultado de fidelidad: B NO PASA** (10 sostenidos en 8 de 14 planes contra 14 en 7 de A), así que el
coste no se despliega: ver [medicion_ab/RESULTADO.md](medicion_ab/RESULTADO.md). Esta sección es manual: si se vuelve a
generar el archivo con `corrida_final_costes_modelos.ts`, hay que volver a añadirla.

## 10. La segunda medición A/B (9 oct 2026)

Los mismos 14 planes con el contexto arreglado. Cifras de `medicion_ab2/costes.json`.

| Pieza | USD | Por plan (media) |
|---|---:|---:|
| Redactor (un borrador por plan, compartido por A y B) | 1,1126 | 0,0795 |
| Verificador (Sonnet 5.5) | 0,7725 | 0,0552 |
| **Total de redacción** | **1,8851** | 0,1347 |
| Juez, relectura y árbitro por la API (Opus 5.5, 51 llamadas; estimado a 5/25 por millón) | 9,29 | n/a |

El verificador sube el coste del plan en torno a un 69 % sobre el redactor (mínimo 0,0312, máximo 0,0805). Propuso 87
ediciones y aplicó 83, ninguna a revisión. **Resultado de fidelidad: B NO PASA** (15 sostenidos en 9 de 14 planes
contra 14 en 7 de A): ver [medicion_ab2/RESULTADO.md](medicion_ab2/RESULTADO.md). Sección manual, como la 9.

## 11. La última medición (9 oct 2026)

Los 14 planes por el camino de producción, sin verificador. Cifras de `medicion_final/costes.json` y `juez.log`.

| Pieza | Modelo | Llamadas | USD | Por plan (media) |
|---|---|---:|---:|---:|
| Redactor | Sonnet 5.5 | 14 | 1,1103 | 0,0793 |
| Dos jueces por paquete (17 paquetes) | Opus 5.5 | 34 | 6,44 | n/a |
| Árbitro en las coincidencias | Opus 5.5 | 10 | 1,74 | n/a |
| **Total** | | **58** | **9,29** | n/a |

Jueces y árbitro estimados a 5/25 USD por millón de tokens; la cifra oficial es la consola. **Resultado: NO PASA**
(ver [medicion_final/RESULTADO.md](medicion_final/RESULTADO.md)). Sección manual, como la 9 y la 10.

## 12. El cierre del 10 oct 2026: copia fiel y redactor con respaldo

Gasto estimado por los guiones de la API (la cifra oficial es la consola del fundador).

| Pieza | Modelo | USD |
|---|---|---:|
| Copia fiel, pilotos | Sonnet 5.5 | 1,59 |
| Copia fiel, parte 1 (k31b, 76 paquetes) | Sonnet 5.5 | 10,10 |
| Copia fiel, parte 2a (12 lotes V) | Sonnet 5.5 | 3,84 |
| Copia fiel, parte 2b (k32) | Sonnet 5.5 | 1,85 |
| Copia fiel, parte 3 (reescritura y verificación r3) | Sonnet 5.5 | 8,69 |
| **Copia fiel, total** | | **26,07** |
| Primera medición final del redactor | Sonnet 5.5 + Opus 5.5 | 9,63 |
| Segunda medición final del redactor | Sonnet 5.5 + Opus 5.5 | 8,22 |
| **Total del 10 oct** | | **43,92** |

Coste real frente a lo estimado: entre 1,6 y 1,9 veces, porque Sonnet 5.5 razona por defecto y esos tokens se cobran.
Desde la verificación de k31b, los guiones reservan el peor caso de cada llamada antes de lanzarla y el tope se
cumple con llamadas en paralelo. Sección manual, como la 9, la 10 y la 11.
