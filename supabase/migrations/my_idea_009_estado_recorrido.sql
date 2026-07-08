-- ============================================================================
-- MY IDEA · Migration 009_estado_recorrido
-- Fase 3.0: estado completo del bucle de entrevista (ejecutar_recorrido en
-- prototipo_motor.py), persistido entre turnos.
--
-- En el CLI, este estado vive en dos sitios: un archivo local
-- engine/sessions/{id}.json (guardar_sesion/cargar_sesion, solo para
-- --continuar) y variables en memoria del proceso (historial_mensajes,
-- ultimas_preguntas, repreguntas_usadas, numeros_detectados_sesion,
-- tipo_oferta_sesion, unidad_venta_sesion) que --continuar SIEMPRE pierde
-- (ver docstring de ejecutar_recorrido: "vive solo en memoria de esta
-- corrida, no se persiste").
--
-- La web no tiene ese lujo: cada turno es una invocacion serverless
-- separada, sin memoria compartida ni con el turno anterior de la MISMA
-- sesion. Por eso sessions.estado_recorrido debe guardar TODO lo anterior
-- en un solo JSONB, incluyendo lo que el CLI descartaba -- lo cual es una
-- mejora real, no solo paridad: la web no perdera el cache de conversacion
-- ni los numeros detectados solo porque el usuario cerro la pestaña entre
-- preguntas.
-- ============================================================================

ALTER TABLE public.sessions ADD COLUMN IF NOT EXISTS estado_recorrido JSONB;

COMMENT ON COLUMN public.sessions.estado_recorrido IS
  'Estado completo y resumible del bucle de entrevista de un turno al '
  'siguiente: ruta, modos, perfil_sesion, historial_mensajes (cache '
  'incremental), ultimas_preguntas, repreguntas_usadas, '
  'numeros_detectados_sesion, tipo_oferta_sesion, unidad_venta_sesion, '
  'prioridad_declarada, fallback_events, fase (esperando_respuesta | '
  'esperando_profundizar | extendiendo_dirigido | listo_para_plan | '
  'cerrada) y pregunta_pendiente (el texto literal mostrado al usuario, '
  'Hotfix v2.1.2). Null mientras la sesion no ha arrancado su primer turno.';
