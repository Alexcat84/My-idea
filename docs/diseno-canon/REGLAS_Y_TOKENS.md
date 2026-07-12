# My Idea · Reglas y tokens del paquete visual

Referencia de handoff que viaja junto a los mockups. Todo lo que diga este archivo manda sobre cualquier residuo visual.

## 1. Paleta y regla de color: EL AZUL PIENSA, EL VERDE EJECUTA

| Token | Valor | Uso |
|---|---|---|
| Azul primario | #4D7CFE | Todo lo que es exploracion, planeacion y posibilidad: etapas 1 a 4 del stepper, mini viajes de mundos en Exploracion y Plan, chips informativos, focus, acciones de navegacion, anillo "pensando" |
| Verde ejecucion | #3FB950 | Todo lo que es accion sobre el mundo real: etapa 5 del stepper, cajas "Esta semana" (core y mundos), progreso del checklist (contadores X/N, barras, items hechos, botones "Marcar hecho"), estados "Manos a la Obra · N/M" |
| Ambar guardian | #E0A64A | Solo el guardian de datos (GIGO) de Tus Numeros, tono acompanante |
| Fondo base | #0A0A0C / #000000 | Lienzo y frames |
| Superficie 1 | #101013 | Tarjetas |
| Superficie 2 | #17171B / #141419 | Campos, hover de tarjetas |
| Texto | #F5F6F8 | Principal |
| Texto dim | #A6A7AD | Secundario |
| Hairline | rgba(255,255,255,0.08) | Bordes |

Los estados completados se distinguen tambien por FORMA (check lleno, texto tachado), nunca solo por color.

## 2. Los 5 nombres canonicos de etapa

1. La Chispa
2. Claridad
3. La Exploracion
4. Tu Plan
5. Manos a la Obra

"Manos a la Obra" es el unico nombre valido de la etapa 5 en todas las superficies (stepper, mini viajes de mundos, estados de cinta, textos). No existe "En marcha".

## 3. Tabla de creditos (la moneda se llama "creditos", jamas "tokens")

| Item | Costo |
|---|---|
| El organizador (Claridad) | Gratis, siempre |
| La Exploracion (entrevista + plan) | 5 creditos |
| Activar un mundo (Seguridad y Personas / Ambiente y Futuro / Calidad y Confianza) | 3 creditos |
| Seguimiento | 2 creditos |
| Tus Numeros | 2 creditos |

Precios en dinero y tamanos de pack: por definir (los packs del centro de creditos son estructura, no precio).

## 4. Pantallas incluidas

1. 01 Home - Mis Ideas (cintas por idea, captura rapida, chips de estado)
2. 02 Etapa 1 - La Chispa (captura de la idea, momento sagrado)
3. 03 Etapa 2 - Claridad (organizador del API: frase, lo que tienes, lo que asumes)
4. 04 Etapa 3 - La Exploracion (riel animado, tarjeta de pregunta, estados especiales, bottom sheet mobile)
5. 05 Etapa 4 - Tu Plan (documento con Esta semana, trazabilidad por nodo, tarjeta Tus Numeros)
6. 06 Etapa 5 - Manos a la Obra (checklist verde, ciclo de profundizacion, ritmo)
7. 07 Potenciadores y Creditos (compuerta, centro de creditos, fila de potenciadores, Tus Numeros por dentro, guardian ambar)
8. 08 Mundos Activos (idea con Calidad y Confianza activo: checklist maestro agrupado, seccion del mundo, cinta con chips)
9. 09 La Celebracion (marcar idea como realizada: timeline vertical animado del viaje, pulso verde + pill "Proyecto", estadisticas reales, linea de cumplimiento solo con baseline, "Reabrir esta idea")
10. 10 Modo y Fechas (vista A: eleccion "A mi ritmo" vs "Con fechas y recordatorios"; vista B: ritual de linea base con fechas sugeridas deterministicas, "Aceptar estas fechas", edicion por item, "mover esta etapa una semana")
11. 11 Analisis del Proyecto (capa universal siempre + capa de cumplimiento solo con baseline, tono espejo con tardias en ambar, barras gemelas base-vs-real, "Descargar mi informe .md")

Cada pantalla incluye desktop 1240 y mobile 380. Los archivos HTML son autocontenidos: abren sin servidor.

## 5. Fase 3.8 — El sentido del tiempo (pantallas 09-11)

Reglas nuevas que mandan sobre estas tres pantallas:

- CERO LLM / cero costo por render: la Celebracion y el Analisis se construyen solo de lo persistido (projects.created_at, planes, checklist_items.completed_at, project_unlocks, plans.baseline_confirmada_at, checklist_items.fecha_base). Ningun texto de estas pantallas sale de un modelo.
- Tardias en AMBAR (#E0A64A, el tono guardian), jamas en rojo. El tono es espejo, nunca regano.
- La capa de cumplimiento (a tiempo / adelantadas / tardias, desviacion, barras gemelas) solo aparece si hubo baseline confirmada. Sin baseline: solo la capa universal.
- Umbral "a tiempo": |completed_at - fecha_base| <= 1 dia. Adelantada: completed_at < fecha_base - 1 dia. Tardia: completed_at > fecha_base + 1 dia.
- Animacion de la Celebracion: duracion FIJA 6-8s sin importar el largo del viaje, saltable con un toque, prefers-reduced-motion -> estado estatico directo.
- Las fechas sugeridas son deterministicas (sin hora): etapa N -> plan.created_at + N semanas (viernes); items "Esta semana" -> inicio de su semana. El usuario las ve en lenguaje humano ("viernes 20 de marzo").
