# Spike de estimación — Fase 0 del Scheduler Inteligente (modo: items)

Unidad = **cada acción granular** (paso_accionable), con el concepto como contexto. **Es la granularidad que ve el usuario y que estimará F1.**

Modelo: `claude-sonnet-4-6` · 36 unidades × 3 corridas · costo real: **$0.1416**

## Concordancia inter-corrida
- **Exacta** (las 3 corridas, misma banda): 34/36 (94.4%)
- **Adyacente** (a lo sumo 1 banda de distancia): 1/36 (2.8%)
- **Discordante** (2+ bandas de distancia): 1/36 (2.8%)
- **espera_externa concorde** (las 3 corridas iguales): 35/36 (97.2%)

**Distribución de bandas** (moda por unidad): S=9 · M=23 · L=1 · XL=3

## PUERTA — exacta-o-adyacente = **97.2%** → ✅ **ABRE F1** (>80%)

## Matriz de DISCORDANTES (para el juicio del fundador — PM certificado = estándar de oro)

| Unidad | Dominio / Fase | Corrida 1 | Corrida 2 | Corrida 3 |
|---|---|---|---|---|
| Contratar una firma de PR especializada en franquicias cuando el pr… | franquicias / ejecucion | XL | M | M |

## Todas las unidades (referencia)

| Unidad | Dominio | Bandas (3 corridas) | Clase | Espera concorde |
|---|---|---|---|---|
| Identificar pagos adelantados (renta, seguros, campañas) que benefi… | core | M/M/M | exacta | sí |
| Designar un vocero o líder que asuma la comunicación pública durant… | core | S/S/S | exacta | sí |
| Calcular variaciones e índices de desempeño (SV, CV, SPI, CPI) | core | S/S/S | exacta | sí |
| Preguntar sobre problemas actuales sin abusar de estas preguntas | core | M/M/M | exacta | sí |
| Implementar políticas de precios estables ('everyday low price') pa… | core | XL/XL/XL | exacta | sí |
| Documentar buenas prácticas identificadas | core | M/M/M | exacta | sí |
| Negociar cuidadosamente cuántos asientos de junta se otorgan a cada… | core | XL/XL/XL | exacta | sí |
| Identificar los segmentos de clientes relevantes para la innovación | core | M/M/M | exacta | sí |
| Estar dispuesto a descartar ideas que no superen la evaluación crítica | core | S/S/S | exacta | sí |
| Compara tu diseño con sistemas naturales o comunitarios que ya dist… | core | M/M/M | exacta | sí |
| Negociar si el asiento del fundador-CEO es un 'founder seat' (perma… | core | M/M/M | exacta | sí |
| Identificar qué datos propios tiene el negocio disponibles para ent… | core | M/M/M | exacta | sí |
| Calcular escenarios de retorno bajo cada tipo de participación usan… | core | M/M/M | exacta | sí |
| Exigir compromiso personal del banquero senior en todas las reunion… | core | M/S/M | adyacente | no |
| Mide la tasa de conversión de quienes ven la oferta vs. quienes eje… | core | S/S/S | exacta | sí |
| En fase I, envía un flujo pequeño y constante de clientes para dete… | core | XL/XL/XL | exacta | sí |
| Cuando los datos contradicen una hipótesis, decidir si es una itera… | core | M/M/M | exacta | sí |
| Añadir diagramas de apoyo: mapa de flujo de trabajo del cliente, ma… | core | L/L/L | exacta | sí |
| Definir qué datos se necesitan para comunicación externa con stakeh… | environmental | M/M/M | exacta | sí |
| Identificar los mayores focos de impacto ambiental y costo en la ca… | environmental | M/M/M | exacta | sí |
| Decidir entre sight draft (pago contra documentos) o time draft (pa… | exportacion | M/M/M | exacta | sí |
| Presentar la solicitud internacional bajo el Protocolo de Madrid | exportacion | M/M/M | exacta | sí |
| Contratar una firma de PR especializada en franquicias cuando el pr… | franquicias | XL/M/M | discordante | sí |
| Establecer el proceso interno para presentar el FDD al menos 14 día… | franquicias | M/M/M | exacta | sí |
| Aplicar el enfoque 'lo peor primero' cuando los recursos son limitados | health_safety | M/M/M | exacta | sí |
| Comunicar peligros existentes y los que el trabajo contratado pueda… | health_safety | M/M/M | exacta | sí |
| Revisar si las mejoras de seguridad implementadas han sido aprovech… | health_safety | M/M/M | exacta | sí |
| Obtener el certificado de conformidad y registrar la organización p… | quality | S/S/S | exacta | sí |
| Calcular la media y desviación estándar de la población o muestra | quality | S/S/S | exacta | sí |
| Definir condiciones de inspección: distancia de visión, tiempo, ilu… | quality | S/S/S | exacta | sí |
| Registrar y analizar quejas recurrentes del personal antes de atrib… | quality | M/M/M | exacta | sí |
| Establecer y participar personalmente en un consejo de calidad | quality | M/M/M | exacta | sí |
| Determinar si los datos son de tipo variable (continuo) o atributo … | quality | S/S/S | exacta | sí |
| Establecer reglas básicas de negociación estructurada entre cliente… | quality | M/M/M | exacta | sí |
| Hacer firmar un compromiso (pledge) entre supervisor y empleado | quality | M/M/M | exacta | sí |
| Reserva algo de tu capacidad para perseguir la oportunidad más prom… | risk_management | S/S/S | exacta | sí |
