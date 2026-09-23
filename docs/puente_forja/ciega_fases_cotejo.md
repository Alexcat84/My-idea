COTEJO DE LA CIEGA DE FASES (semilla 20260923). Todas las filas.

| clave | node_id | declarada a ciegas | registro | veredicto |
|---|---|---|---|---|
| C01 | `examinar_trabajo_pasado_candidato` | ejecucion | ejecucion | COINCIDE |
| C02 | `desplegar_plan_orden_operaciones_franqueza_radical` | planificacion | planificacion | COINCIDE |
| C03 | `elegir_pregunta_recurrente_pedir_critica` | planificacion | planificacion | COINCIDE |
| C04 | `frenar_incoherencias_entrevista` | ejecucion | ejecucion | COINCIDE |
| C05 | `desplegar_marco_franqueza_radical` | ejecucion | ejecucion | COINCIDE |
| C06 | `manejar_contacto_fisico_regla_platino` | ejecucion | ejecucion | COINCIDE |
| C07 | `planificar_cinco_olas_venta` | planificacion | planificacion | COINCIDE |
| C08 | `dar_opinion_especifica_tarea` | ejecucion | ejecucion | COINCIDE |
| C09 | `ajustar_franqueza_oido_oyente` | ejecucion | ejecucion | COINCIDE |
| C10 | `vender_cambio_trabajo_familia` | ejecucion | ejecucion | COINCIDE |
| C11 | `alinear_equipo_proposito_comun` | ejecucion | ejecucion | COINCIDE |
| C12 | `probar_gestion_antes_decidir` | validacion | validacion | COINCIDE |
| C13 | `decidir_contratacion_final` | ejecucion | ejecucion | COINCIDE |
| C14 | `probar_banquillo_vacaciones_largas` | validacion | validacion | COINCIDE |
| C15 | `resolver_dudas_frecuentes_reuniones_salto_nivel` | ejecucion | ejecucion | COINCIDE |
| C16 | `auditar_calendario_reuniones_semana` | validacion | planificacion | DISCREPA |
| C17 | `pedir_referencias_empleados` | planificacion | ejecucion | DISCREPA |
| C18 | `vivir_primero_valor_declarado` | ejecucion | ejecucion | COINCIDE |
| C19 | `cambiar_formato_reunion_favorecer_participacion` | ejecucion | ejecucion | COINCIDE |
| C20 | `ayudar_personas_jugar_fortalezas` | ejecucion | ejecucion | COINCIDE |

CIFRA cotejados: 20 | COINCIDEN: 18 | DISCREPAN: 2

**Las dos discrepancias, adjudicadas.** Las dos son de frontera entre fases vecinas, y las dos se resuelven a favor de la lectura ciega, que aplica la vara mas al pie de la letra: `auditar_calendario_reuniones_semana` pasa de planificacion a validacion (su nucleo es medir una semana antes de purgar) y `pedir_referencias_empleados` pasa de ejecucion a planificacion (monta un sistema con resultado e incentivo en la tarjeta de cada persona). Las dos lineas del registro llevan su `correccion_declarada` y su `fase_anterior`.

**Lo que esta ciega mide y lo que no, dicho entero:** la lectora del registro y la de la ciega son la misma sesion, asi que el 18 de 20 mide la ESTABILIDAD de la vara (dos lecturas separadas del mismo texto caen en la misma fase), no la independencia de dos lectores. Una ciega con otro lector es la prueba mas fuerte y queda para la revision del fundador.
