# Spike de estimación — Fase 0 del Scheduler Inteligente

Modelo: `claude-sonnet-4-6` · 36 tareas × 3 corridas · costo real: **$0.1712**

## Concordancia inter-corrida
- **Exacta** (las 3 corridas, misma banda): 35/36 (97.2%)
- **Adyacente** (a lo sumo 1 banda de distancia): 0/36 (0.0%)
- **Discordante** (2+ bandas de distancia): 1/36 (2.8%)
- **espera_externa concorde** (las 3 corridas iguales): 34/36 (94.4%)

## PUERTA — exacta-o-adyacente = **97.2%** → ✅ **ABRE F1** (>80%)

## Matriz de DISCORDANTES (para el juicio del fundador — PM certificado = estándar de oro)

| Tarea | Dominio / Fase | Corrida 1 | Corrida 2 | Corrida 3 |
|---|---|---|---|---|
| Perfil de Compañía Internacional (ICP) | exportacion / validacion | M | XL | XL |

## Todas las tareas (referencia)

| Tarea | Dominio | Bandas (3 corridas) | Clase | Espera concorde |
|---|---|---|---|---|
| Accruals (Devengos) y Activos Prepagados | core | M/M/M | exacta | sí |
| Liderazgo Frontal Frente a la Prensa y Ataques Competitivos | core | XL/XL/XL | exacta | sí |
| Email Marketing para Captación de Clientes | core | XL/XL/XL | exacta | sí |
| Generalistas vs. Especialistas: Valor de Opción vs. Profundidad | core | M/M/M | exacta | sí |
| Navegar la Política Organizacional de Nuevas Ideas | core | XL/XL/XL | exacta | sí |
| Rediseño de Procesos de Negocio para Eliminar Fricciones Autoinfligidas | core | XL/XL/XL | exacta | sí |
| Timing Correcto para Solicitar Referencias | core | L/L/L | exacta | sí |
| Determinar el Tipo de Mercado | core | M/M/M | exacta | sí |
| Identificar Brechas (Mind the Gaps) | core | M/M/M | exacta | sí |
| Superioridad del Producto Basada en Beneficios | core | XL/XL/XL | exacta | sí |
| Costo de Oportunidad | core | M/M/M | exacta | sí |
| Fase de Movilización: Equipo Multifuncional | core | XL/XL/XL | exacta | sí |
| Plan de Gestión de las Comunicaciones | core | M/M/M | exacta | sí |
| Sistema Triple A (Adaptativo, Ágil, Acelerado) | core | XL/XL/XL | exacta | no |
| Crowdfunding de Producto (Kickstarter/Indiegogo) | core | XL/XL/XL | exacta | sí |
| Hipótesis de Relación con Clientes (Get, Keep, Grow) para Web/Mobile | core | XL/XL/XL | exacta | sí |
| Métricas de Retención | core | XL/XL/XL | exacta | sí |
| Expandir el Trabajo a través de la Cadena de Valor (Co-creación) | environmental | XL/XL/XL | exacta | sí |
| Eco-efectividad vs. Eco-eficiencia | environmental | L/L/L | exacta | sí |
| Responsabilidad extendida del productor y stewardship de producto | environmental | XL/XL/XL | exacta | sí |
| Negociación del Acuerdo con el Representante Extranjero | exportacion | XL/XL/XL | exacta | sí |
| Perfil de Compañía Internacional (ICP) | exportacion | M/XL/XL | discordante | sí |
| Facilidad de Supervisión del Franquiciante | franquicias | XL/XL/XL | exacta | sí |
| Comprender la Definición Legal Federal de Franquicia (FTC Rule 436) | franquicias | L/L/L | exacta | sí |
| Maintenance Error Decision Aid (MEDA) | health_safety | L/L/L | exacta | sí |
| Defensas en Profundidad (Las Siete Funciones) | health_safety | L/L/L | exacta | sí |
| Patrones Disfuncionales de Cultura Organizacional | health_safety | XL/XL/XL | exacta | sí |
| Ciclo Adaptativo de Inteligencia Organizacional | quality | XL/XL/XL | exacta | sí |
| DMAIC - Fase Measure (Medición del Proceso) | quality | XL/XL/XL | exacta | no |
| Fase Launch del Roadmap de Transformación | quality | XL/XL/XL | exacta | sí |
| Secuencia Universal de Juran para el Breakthrough (Mejora Radical) | quality | XL/XL/XL | exacta | sí |
| Adaptación de los 14 Puntos de Deming al Servicio Médico | quality | XL/XL/XL | exacta | sí |
| Enfoque en la Mejora Continua en Operaciones | quality | XL/XL/XL | exacta | sí |
| Plan de Acción para la Transformación (Punto 14) | quality | XL/XL/XL | exacta | sí |
| Auditoría de Calidad (Examen Planeado de Conformidad) | quality | XL/XL/XL | exacta | sí |
| Empezar con Métodos Simples y Probados | risk_management | M/M/M | exacta | sí |
