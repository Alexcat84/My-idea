# La familia OSHA de Seguridad y Personas, para tu poda

**51 nodos** salen de dos guías de OSHA que cubren el MISMO marco: **OSHA 3885** (24)
y **OSHA 3886** (27). El censo las señaló duplicando el 45,8% y el 33,3% de su contenido.

De esos 51, **20 ya caen** en los 27 clusters del índice de fusión.
Los otros **31 no**: el umbral de 0,90 no los agrupó, igual que pasó con la familia COQ.

Aquí van los **82 pares CRUZADOS entre las dos guías** a coseno ≥ 0,75, que es donde
vive la duplicación de esta familia: el mismo tema contado por dos publicaciones.

**Borra las líneas de lo que NO debe fundirse.** `sim` = coseno. `visto/cos` = telemetría real.

| sim | de OSHA 3885 | de OSHA 3886 | visto | ¿en cluster? |
|---:|---|---|---|:-:|
| 0.947 | **Establecer Coordinación Efectiva entre Emplead** `establecer_coordinacion_efectiva_hostempleador` | **Establecimiento de Coordinación Efectiva entre** `establecer_coordinacion_efectiva_contratistas` | 0/0 | **NO** |
| 0.941 | **Caracterización y Priorización de Peligros** `priorizacion_caracterizacion_peligros` | **Caracterización y Priorización de Peligros (Ev** `caracterizacion_priorizacion_peligros` | 2/2 | sí |
| 0.934 | **Prevención y Control de Peligros (Jerarquía de** `prevencion_control_peligros` | **Prevención y Control de Peligros mediante Jera** `prevencion_control_peligros_2` | 4/3 | sí |
| 0.934 | **Recopilación y Revisión de Información sobre P** `identificacion_recopilacion_informacion_peligros` | **Recopilación de Información Existente sobre Pe** `recopilacion_informacion_peligros` | 3/0 | sí |
| 0.925 | **Seguimiento de la Efectividad de los Controles** `seguimiento_efectividad_controles` | **Seguimiento de la Efectividad de los Controles** `seguimiento_efectividad_controles_2` | 3/2 | sí |
| 0.925 | **Comunicación y Coordinación Multiempleador (In** `comunicacion_coordinacion_multiempleador` | **Comunicación y Coordinación Multiempleador (Co** `comunicacion_coordinacion_multiempleador_2` | 0/0 | **NO** |
| 0.922 | **Inspección del Lugar de Trabajo para Identific** `inspeccion_lugar_trabajo_peligros` | **Inspección Regular del Sitio de Trabajo para I** `inspeccion_sitio_peligros` | 2/0 | sí |
| 0.921 | **Coordinación Multiempleador (Agencias de Perso** `coordinacion_multiempleador` | **Coordinación y Comunicación en Sitios Multiemp** `coordinacion_sitios_multiempleador` | 0/3 | **NO** |
| 0.916 | **Evaluación Periódica del Programa de Seguridad** `evaluacion_periodica_programa_seguridad` | **Evaluación y Mejora del Programa de Seguridad ** `evaluacion_mejora_programa_3` | 0/0 | sí |
| 0.915 | **Comunicación y Coordinación Multiempleador (In** `comunicacion_coordinacion_multiempleador` | **Coordinación y Comunicación en Sitios Multiemp** `coordinacion_sitios_multiempleador` | 0/3 | **NO** |
| 0.915 | **Investigación de Incidentes y Casi Accidentes** `investigacion_incidentes` | **Investigación de Incidentes y Cuasi-Accidentes** `investigacion_incidentes_2` | 2/0 | sí |
| 0.910 | **Comunicación y Coordinación para Empleadores M** `coordinacion_empleadores_multiples` | **Coordinación y Comunicación en Sitios Multiemp** `coordinacion_sitios_multiempleador` | 0/3 | **NO** |
| 0.907 | **Establecer Comunicación Efectiva entre Emplead** `establecer_comunicacion_efectiva_hostempleador` | **Establecimiento de Comunicación Efectiva entre** `establecer_comunicacion_efectiva_contratistas` | 0/0 | sí |
| 0.905 | **Implementación de Controles en el Lugar de Tra** `implementacion_controles` | **Implementación de Controles Seleccionados en e** `implementacion_controles_2` | 3/3 | sí |
| 0.901 | **Coordinación Multiempleador (Agencias de Perso** `coordinacion_multiempleador` | **Establecimiento de Coordinación Efectiva entre** `establecer_coordinacion_efectiva_contratistas` | 0/0 | **NO** |
| 0.901 | **Evaluación y Mejora del Programa de Seguridad ** `evaluacion_mejora_programa` | **Evaluación y Mejora del Programa de Seguridad ** `evaluacion_mejora_programa_3` | 3/0 | sí |
| 0.898 | **Participación de los Trabajadores en el Progra** `participacion_trabajadores` | **Participación Activa de los Trabajadores** `participacion_trabajadores_2` | 4/3 | **NO** |
| 0.896 | **Identificación de Peligros para la Salud (Indu** `identificacion_peligros_salud` | **Identificación de Peligros para la Salud (Cons** `identificacion_peligros_salud_2` | 4/0 | **NO** |
| 0.889 | **Coordinación Multiempleador (Agencias de Perso** `coordinacion_multiempleador` | **Comunicación y Coordinación Multiempleador (Co** `comunicacion_coordinacion_multiempleador_2` | 0/0 | **NO** |
| 0.885 | **Evaluación Periódica del Programa de Seguridad** `evaluacion_periodica_programa_seguridad` | **Verificación de la Implementación y Operación ** `verificacion_implementacion_programa_sst` | 0/0 | sí |
| 0.883 | **Identificación de Peligros en Situaciones de E** `peligros_emergencias_no_rutinarias` | **Identificación de Peligros en Emergencias y Ta** `peligros_emergencias_no_rutinarias_2` | 2/0 | **NO** |
| 0.879 | **Comunicación y Coordinación para Empleadores M** `coordinacion_empleadores_multiples` | **Establecimiento de Coordinación Efectiva entre** `establecer_coordinacion_efectiva_contratistas` | 0/0 | **NO** |
| 0.878 | **Capacitación de Conciencia del Programa de Seg** `capacitacion_conciencia_programa` | **Educación y Entrenamiento en Seguridad** `educacion_entrenamiento_seguridad` | 0/2 | **NO** |
| 0.873 | **Liderazgo Gerencial en Seguridad y Salud** `liderazgo_gerencial_seguridad` | **Liderazgo y Compromiso de la Gerencia en Segur** `compromiso_gerencial_seguridad` | 3/0 | **NO** |
| 0.870 | **Evaluación y Mejora del Programa de Seguridad ** `evaluacion_mejora_programa` | **Verificación de la Implementación y Operación ** `verificacion_implementacion_programa_sst` | 3/0 | sí |
| 0.867 | **Prevención y Control de Peligros (Jerarquía de** `prevencion_control_peligros` | **Jerarquía de Controles de Peligros** `jerarquia_controles` | 4/2 | sí |
| 0.866 | **Comunicación y Coordinación Multiempleador (In** `comunicacion_coordinacion_multiempleador` | **Establecimiento de Coordinación Efectiva entre** `establecer_coordinacion_efectiva_contratistas` | 0/0 | **NO** |
| 0.865 | **Identificación y Evaluación de Peligros (Indus** `identificacion_evaluacion_peligros` | **Identificación y Evaluación de Peligros (Const** `identificacion_evaluacion_peligros_2` | 4/1 | **NO** |
| 0.865 | **Establecer Coordinación Efectiva entre Emplead** `establecer_coordinacion_efectiva_hostempleador` | **Coordinación y Comunicación en Sitios Multiemp** `coordinacion_sitios_multiempleador` | 0/3 | **NO** |
| 0.859 | **Identificación de Peligros en Situaciones de E** `peligros_emergencias_no_rutinarias` | **Controles para Tareas No Rutinarias y Emergenc** `controles_no_rutinarias_emergencias` | 2/3 | **NO** |
| 0.856 | **Comunicación y Coordinación para Empleadores M** `coordinacion_empleadores_multiples` | **Comunicación y Coordinación Multiempleador (Co** `comunicacion_coordinacion_multiempleador_2` | 0/0 | **NO** |
| 0.854 | **10 Acciones Iniciales para Arrancar un Program** `diez_pasos_iniciales_programa` | **Nueve Pasos Simples para Iniciar un Programa d** `nueve_pasos_iniciar_programa` | 0/3 | **NO** |
| 0.848 | **Evaluación Periódica del Programa de Seguridad** `evaluacion_periodica_programa_seguridad` | **Corrección de Deficiencias y Mejora Continua d** `correccion_deficiencias_programa_sst` | 0/0 | sí |
| 0.848 | **Evaluación y Mejora del Programa de Seguridad ** `evaluacion_mejora_programa` | **Corrección de Deficiencias y Mejora Continua d** `correccion_deficiencias_programa_sst` | 3/0 | sí |
| 0.840 | **Evaluación y Mejora del Programa de Seguridad ** `evaluacion_mejora_programa` | **Evaluación y Mejora del Programa de Seguridad ** `evaluacion_mejora_programa_2` | 3/1 | sí |
| 0.838 | **Capacitación de Trabajadores en Identificación** `capacitacion_identificacion_peligros` | **Educación y Capacitación en Seguridad y Salud ** `capacitacion_educacion_seguridad` | 0/2 | **NO** |
| 0.836 | **Seguimiento de la Efectividad de los Controles** `seguimiento_efectividad_controles` | **Verificación de la Implementación y Operación ** `verificacion_implementacion_programa_sst` | 3/0 | sí |
| 0.835 | **Establecer Coordinación Efectiva entre Emplead** `establecer_coordinacion_efectiva_hostempleador` | **Comunicación y Coordinación Multiempleador (Co** `comunicacion_coordinacion_multiempleador_2` | 0/0 | **NO** |
| 0.825 | **Identificación y Evaluación de Peligros (Indus** `identificacion_evaluacion_peligros` | **Inspección Regular del Sitio de Trabajo para I** `inspeccion_sitio_peligros` | 4/0 | sí |
| 0.821 | **Inspección del Lugar de Trabajo para Identific** `inspeccion_lugar_trabajo_peligros` | **Identificación y Evaluación de Peligros (Const** `identificacion_evaluacion_peligros_2` | 2/1 | sí |

## Los 31 que no están en ningún cluster

Estos no los toca la fusión propuesta: son otra decisión.

| título | guía | visto | cos |
|---|---|---:|---:|
| Enfoque Proactivo 'Find and Fix' `enfoque_find_and_fix` | OSHA3886 | 4 | 4 |
| Identificación y Evaluación de Peligros (Industria Gener `identificacion_evaluacion_peligros` | OSHA3885 | 4 | 1 |
| Identificación de Peligros para la Salud (Industria Gene `identificacion_peligros_salud` | OSHA3885 | 4 | 4 |
| Participación de los Trabajadores en el Programa de Segu `participacion_trabajadores` | OSHA3885 | 4 | 4 |
| Controles para Tareas No Rutinarias y Emergencias `controles_no_rutinarias_emergencias` | OSHA3886 | 3 | 3 |
| Coordinación y Comunicación en Sitios Multiempleador `coordinacion_sitios_multiempleador` | OSHA3886 | 3 | 3 |
| Liderazgo Gerencial en Seguridad y Salud `liderazgo_gerencial_seguridad` | OSHA3885 | 3 | 3 |
| Nueve Pasos Simples para Iniciar un Programa de Segurida `nueve_pasos_iniciar_programa` | OSHA3886 | 3 | 3 |
| Participación Activa de los Trabajadores `participacion_trabajadores_2` | OSHA3886 | 3 | 3 |
| Plan de Control de Peligros `plan_control_peligros` | OSHA3886 | 3 | 1 |
| Educación y Capacitación en Seguridad y Salud Ocupaciona `capacitacion_educacion_seguridad` | OSHA3886 | 2 | 2 |
| Educación y Entrenamiento en Seguridad `educacion_entrenamiento_seguridad` | OSHA3886 | 2 | 2 |
| Jerarquía de Controles de Peligros `jerarquia_controles` | OSHA3886 | 2 | 0 |
| Identificación de Peligros en Situaciones de Emergencia  `peligros_emergencias_no_rutinarias` | OSHA3885 | 2 | 2 |
| Evaluación y Mejora del Programa de Seguridad (Elemento  `evaluacion_mejora_programa_2` | OSHA3886 | 1 | 1 |
| Identificación y Evaluación de Peligros (Construcción) `identificacion_evaluacion_peligros_2` | OSHA3886 | 1 | 1 |
| Capacitación de Conciencia del Programa de Seguridad y S `capacitacion_conciencia_programa` | OSHA3885 | 0 | 0 |
| Capacitación de Trabajadores en Identificación y Control `capacitacion_identificacion_peligros` | OSHA3885 | 0 | 0 |
| Capacitación de Empleadores, Gerentes y Supervisores en  `capacitacion_roles_gerencia` | OSHA3885 | 0 | 0 |
| Liderazgo y Compromiso de la Gerencia en Seguridad `compromiso_gerencial_seguridad` | OSHA3886 | 0 | 0 |
| Comunicación y Coordinación Multiempleador (Industria Ge `comunicacion_coordinacion_multiempleador` | OSHA3885 | 0 | 0 |
| Comunicación y Coordinación Multiempleador (Construcción `comunicacion_coordinacion_multiempleador_2` | OSHA3886 | 0 | 0 |
| Comunicación y Coordinación para Empleadores Múltiples ( `coordinacion_empleadores_multiples` | OSHA3885 | 0 | 0 |
| Coordinación Multiempleador (Agencias de Personal y Empl `coordinacion_multiempleador` | OSHA3885 | 0 | 0 |
| Corrección de Deficiencias y Mejora Continua del Program `correccion_deficiencias_programa_sst` | OSHA3886 | 0 | 0 |
| 10 Acciones Iniciales para Arrancar un Programa de Segur `diez_pasos_iniciales_programa` | OSHA3885 | 0 | 0 |
| Establecimiento de Coordinación Efectiva entre Empleador `establecer_coordinacion_efectiva_contratistas` | OSHA3886 | 0 | 0 |
| Establecer Coordinación Efectiva entre Empleadores en Si `establecer_coordinacion_efectiva_hostempleador` | OSHA3885 | 0 | 0 |
| Identificación de Peligros para la Salud (Construcción) `identificacion_peligros_salud_2` | OSHA3886 | 0 | 0 |
| Identificación de Peligros en Emergencias y Tareas No Ru `peligros_emergencias_no_rutinarias_2` | OSHA3886 | 0 | 0 |
| Verificación de la Implementación y Operación del Progra `verificacion_implementacion_programa_sst` | OSHA3886 | 0 | 0 |