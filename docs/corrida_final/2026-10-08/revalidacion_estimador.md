# Re-validación del estimador de bandas antes de cambiarle el modelo

Fecha: 2026-10-08T01:26:26.340Z · casos originales 36, recuperados 24 · coste real: $0.0629

Camino de producción: SYSTEM_ESTIMACION_BANDA, el lote entero en una llamada, 3 corridas por modelo.
Control: `claude-sonnet-4-6` (el de hoy). Candidato: `claude-sonnet-5-5`.

| Vara | Control | Candidato |
|---|---|---|
| Puerta original: concordancia entre corridas, exacta-o-adyacente (> 80 %) | 24/24 (100.0 %) | 24/24 (100.0 %) |
| Mayoría igual a la banda del spike original | 13/24 (54.2 %) | 11/24 (45.8 %) |
| Mayoría a una banda o menos de la del spike original | 21/24 (87.5 %) | 22/24 (91.7 %) |

Candidato frente al control de hoy, tarea por tarea: igual 17/24 (70.8 %); a una banda o menos 24/24 (100.0 %).
espera_externa concorde en las 3 corridas del candidato: 22/24 (91.7 %).

**Puerta del candidato:** PASA (> 80 %). El cambio de modelo espera el visto del fundador.

## Casos que ya no están en el grafo de hoy (no se inventan)
- Compara tu diseño con sistemas naturales o comunitarios que ya dist… (core; banda original M)
- Negociar si el asiento del fundador-CEO es un 'founder seat' (perma… (core; banda original M)
- Identificar qué datos propios tiene el negocio disponibles para ent… (core; banda original M)
- Mide la tasa de conversión de quienes ven la oferta vs. quienes eje… (core; banda original S)
- Cuando los datos contradicen una hipótesis, decidir si es una itera… (core; banda original M)
- Definir qué datos se necesitan para comunicación externa con stakeh… (environmental; banda original M)
- Contratar una firma de PR especializada en franquicias cuando el pr… (franquicias; banda original M)
- Establecer el proceso interno para presentar el FDD al menos 14 día… (franquicias; banda original M)
- Aplicar el enfoque 'lo peor primero' cuando los recursos son limitados (health_safety; banda original M)
- Registrar y analizar quejas recurrentes del personal antes de atrib… (quality; banda original M)
- Establecer y participar personalmente en un consejo de calidad (quality; banda original M)
- Hacer firmar un compromiso (pledge) entre supervisor y empleado (quality; banda original M)

## Caso por caso

| Tarea | Spike original | Control (3 corridas) | Candidato (3 corridas) |
|---|---|---|---|
| Identificar pagos adelantados (renta, seguros, campañas) que benefi… | M/M/M | M/M/M | S/S/S |
| Designar un vocero o líder que asuma la comunicación pública durant… | S/S/S | M/M/M | S/S/S |
| Calcular variaciones e índices de desempeño (SV, CV, SPI, CPI) | S/S/S | L/L/L | L/L/L |
| Preguntar sobre problemas actuales sin abusar de estas preguntas | M/M/M | S/S/S | S/S/S |
| Implementar políticas de precios estables ('everyday low price') pa… | XL/XL/XL | L/M/M | L/L/L |
| Documentar buenas prácticas identificadas | M/M/M | M/M/L | M/M/M |
| Negociar cuidadosamente cuántos asientos de junta se otorgan a cada… | XL/XL/XL | L/L/L | L/L/M |
| Identificar los segmentos de clientes relevantes para la innovación | M/M/M | M/M/M | M/M/M |
| Estar dispuesto a descartar ideas que no superen la evaluación crítica | S/S/S | S/S/S | S/S/S |
| Calcular escenarios de retorno bajo cada tipo de participación usan… | M/M/M | M/M/M | M/M/M |
| Exigir compromiso personal del banquero senior en todas las reunion… | M/S/M | S/S/S | M/S/S |
| En fase I, envía un flujo pequeño y constante de clientes para dete… | XL/XL/XL | L/L/L | L/L/L |
| Añadir diagramas de apoyo: mapa de flujo de trabajo del cliente, ma… | L/L/L | L/L/L | L/L/L |
| Identificar los mayores focos de impacto ambiental y costo en la ca… | M/M/M | M/M/M | L/L/L |
| Decidir entre sight draft (pago contra documentos) o time draft (pa… | M/M/M | M/M/M | S/S/S |
| Presentar la solicitud internacional bajo el Protocolo de Madrid | M/M/M | L/L/L | L/L/L |
| Comunicar peligros existentes y los que el trabajo contratado pueda… | M/M/M | M/S/S | S/M/S |
| Revisar si las mejoras de seguridad implementadas han sido aprovech… | M/M/M | M/M/M | M/M/M |
| Obtener el certificado de conformidad y registrar la organización p… | S/S/S | XL/XL/XL | XL/XL/XL |
| Calcular la media y desviación estándar de la población o muestra | S/S/S | M/S/M | S/S/S |
| Definir condiciones de inspección: distancia de visión, tiempo, ilu… | S/S/S | S/S/S | M/M/M |
| Determinar si los datos son de tipo variable (continuo) o atributo … | S/S/S | S/S/S | S/S/S |
| Establecer reglas básicas de negociación estructurada entre cliente… | M/M/M | M/M/M | M/M/M |
| Reserva algo de tu capacidad para perseguir la oportunidad más prom… | S/S/S | S/S/S | S/S/S |
