# Vuelo del 27-28 sep 2026 (integracion del mundo 11), lo que genero la corrida

Corrida real del vuelo (`web/scripts/vuelo.ts`, rama puente-forja, commit 733ee641) contra la API real (Haiku y Sonnet)
y la base real, con el dev user. Empezo a las 21:12:53 UTC del 27 sep. Todo lo de aqui salio de esa corrida: la
transcripcion literal del vuelo y lo que quedo guardado en Supabase para sus proyectos.

## Resultado

- Pasaron todas las fases hasta la 2k, incluida la **2g-quater, Primer Equipo (mundo 11)**: unlock gratis con la
  migracion 048, entrada por una puerta del mundo, 6 turnos, plan con dominio `primer_equipo`, sin rayas ni titulos
  ni autores de libros, 29 items en su checklist (ver `sesiones/08_primer_equipo_inicial.md` y
  `planes/08_primer_equipo_inicial.md`).
- **Cae en la fase 2L** (el mundo como subproyecto): el bloque de realidad del seguimiento de `health_safety` sale en
  su redaccion de ritmo, sin la linea de cumplimiento. Causa: desde AUD-09 M10 (commit c531e175, 23 sep) ese bloque
  lee el modo DEL MUNDO (`project_modos`), y la fase 2L del vuelo solo pone en 'fechas' el modo del nucleo. El vuelo
  no se habia corrido completo desde el 9 sep, antes de ese cambio. No toca al mundo 11.

## Donde mirar la calidad de las respuestas

- `transcripcion_vuelo.txt`: cada pregunta que hizo la app y la respuesta que dio el vuelo, fase por fase.
- `sesiones/NN_*.md`: por sesion, la puerta, el recorrido por el riel (con su etiqueta), las decisiones de cada turno
  con su razonamiento, y el veredicto del **juez de sesion** (pertinencia de transiciones, senales fuera de material).
- `planes/NN_*.md`: cada plan entregado, completo, tal como lo lee el usuario.
- `checklist.md`: las acciones que nacieron de cada plan, agrupadas por mundo y plan.
- `proyecto.md`: la entrada original y el estado vivo final del proyecto.
- `creditos.md`: lo que costo cada entrega en creditos.

## Indice de ficheros


- `organizador_1/proyecto.md`: proyecto 1: entrada y estado vivo final
- `organizador_1/sesion_01.md`: sesion 1 del proyecto 1: core / gratuito, puerta None
- `organizador_1/planes/01_core_organizador.md`: plan de la sesion 1: core / organizador
- `organizador_2/proyecto.md`: proyecto 2: entrada y estado vivo final
- `organizador_2/sesion_01.md`: sesion 1 del proyecto 2: core / gratuito, puerta None
- `organizador_2/planes/01_core_organizador.md`: plan de la sesion 1: core / organizador
- `proyecto.md`: proyecto 3: entrada y estado vivo final
- `sesiones/01_core_inicial.md`: sesion 1 del proyecto 3: core / inicial, puerta None
- `planes/01_core_completo.md`: plan de la sesion 1: core / completo
- `sesiones/02_core_seguimiento.md`: sesion 2 del proyecto 3: core / seguimiento, puerta None
- `planes/02_core_seguimiento.md`: plan de la sesion 2: core / seguimiento
- `sesiones/03_quality_inicial.md`: sesion 3 del proyecto 3: quality / inicial, puerta programa_mejora_calidad_14_pasos
- `planes/03_quality_completo.md`: plan de la sesion 3: quality / completo
- `sesiones/04_exportacion_inicial.md`: sesion 4 del proyecto 3: exportacion / inicial, puerta elementos_plan_exportacion_ejemplo
- `sesiones/05_franquicias_inicial.md`: sesion 5 del proyecto 3: franquicias / inicial, puerta propuesta_valor_franquicia
- `sesiones/06_seguridad_digital_inicial.md`: sesion 6 del proyecto 3: seguridad_digital / inicial, puerta getting_started_planning
- `planes/06_seguridad_digital_inicial.md`: plan de la sesion 6: seguridad_digital / inicial
- `sesiones/07_risk_management_inicial.md`: sesion 7 del proyecto 3: risk_management / inicial, puerta cuatro_caminos_ante_un_riesgo
- `planes/07_risk_management_inicial.md`: plan de la sesion 7: risk_management / inicial
- `sesiones/08_primer_equipo_inicial.md`: sesion 8 del proyecto 3: primer_equipo / inicial, puerta crear_tarjeta_puntuacion_puesto
- `planes/08_primer_equipo_inicial.md`: plan de la sesion 8: primer_equipo / inicial
- `sesiones/09_core_seguimiento.md`: sesion 9 del proyecto 3: core / seguimiento, puerta None
- `planes/09_core_seguimiento.md`: plan de la sesion 9: core / seguimiento
- `sesiones/10_core_seguimiento.md`: sesion 10 del proyecto 3: core / seguimiento, puerta None
- `planes/10_core_seguimiento.md`: plan de la sesion 10: core / seguimiento
- `sesiones/11_health_safety_inicial.md`: sesion 11 del proyecto 3: health_safety / inicial, puerta prevencion_control_peligros
- `planes/11_health_safety_inicial.md`: plan de la sesion 11: health_safety / inicial
- `sesiones/12_core_seguimiento.md`: sesion 12 del proyecto 3: core / seguimiento, puerta None
- `sesiones/13_health_safety_seguimiento.md`: sesion 13 del proyecto 3: health_safety / seguimiento, puerta None
- `checklist.md`: checklist del proyecto 3 (239 items)
- `bitacora.json`: bitacora del proyecto 3
- `creditos.md`: creditos consumidos por la corrida
