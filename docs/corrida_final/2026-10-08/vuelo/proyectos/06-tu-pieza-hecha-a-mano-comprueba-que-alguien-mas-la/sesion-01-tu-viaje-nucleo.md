# Sesión 1: Tu viaje (núcleo) (inicial)

Abrió: 2026-10-08T23:37:55.405853+00:00 · cerró: 2026-10-08T23:38:43.102+00:00 · coste: $0.0995

## La entrada

Vendo un producto fisico que fabrico yo mismo, una pieza a la vez.

## Preguntas de la app y respuestas, turno a turno

_Sin turnos en el hilo de la memoria._
## El recorrido por los nodos

1. Escucha Realmente a tus Clientes (`voz_del_cliente_voc`) · conversado
2. Sal del Edificio a Validar (`customer_discovery_get_out_of_building`) · conversado

## Las decisiones de cada turno (el motivo)

1. `{"tipo":"decision_turno","decision":{"accion":"avanzar","camino":["customer_discovery_get_out_of_building"],"es_salto":false},"pregunta":"¿ya tienes algo concreto que puedas mostrarle a alguien, una pieza terminada o una foto, o todavía estás definiendo qué vas a fabricar?","nodo_actual":"voz_del_cliente_voc","razonamiento":"Usuario describe producto físico hecho a mano sin validación; el nodo de customer discovery aplica y la respuesta no está en el contexto.","saltos_posibles":[{"id":"customer_validation_sell_phase","titulo":"Sal a vender de verdad: valida con clientes reales","afinidad":0.469,"fase_proyecto":"validacion","condiciones_activacion":["Cuando necesitas comprobar con ventas reales si tu negocio funciona"]},{"id":"indice_de_reparabilidad","titulo":"Diseñar un puntaje de qué tan fácil es arreglar tu producto (índice de reparabilidad)","afinidad":0.451,"fase_proyecto":"planificacion","condiciones_activacion":["Si fabricas productos electrónicos que se venden en Francia, donde desde 2021 los fabricantes deben puntuar su reparabilidad, o si tu producto es físico y dura mucho tiempo, como electrodomésticos, dispositivos o muebles.","Si tu producto se puede romper o está pensado para volverse obsoleto."]},{"id":"get_out_building_test_sell","titulo":"Vender de verdad para probar tu modelo de negocio (test selling)","afinidad":0.439,"fase_proyecto":"validacion","condiciones_activacion":["Cuando ya terminaste de hablar con clientes para entender el problema y ya identificaste a tus primeros clientes convencidos","Si necesitas validar, todavía no escalar, tu modelo de negocio con pruebas reales de venta"]},{"id":"diseno_producto_cadena_suministro","titulo":"Diseño de Producto Orientado a la Cadena de Suministro","afinidad":0.437,"fase_proyecto":"planificacion","condiciones_activacion":["Cuando se está diseñando un nuevo producto físico","Cuando existen múltiples proveedores para componentes críticos y se busca simplificar la cadena"]},{"id":"cliente_disena_producto","titulo":"Deja que tu cliente diseñe el producto (co-creación digital)","afinidad":0.434,"fase_proyecto":"ideacion","condiciones_activacion":["Tu producto no requiere conocimiento técnico o científico avanzado (por ejemplo, con algo farmacéutico o aeroespacial esto en general no funciona)","Tienes una base de usuarios entusiastas dispuestos a co-crear contigo"]},{"id":"manufactura_aditiva_bajo_demanda","titulo":"Manufactura Aditiva (Impresión 3D) para Producción Bajo Demanda","afinidad":0.434,"fase_proyecto":"planificacion","condiciones_activacion":["Cuando la empresa enfrenta altos costos de inventario por gran variedad de productos de baja rotación","Si se busca mejorar el nivel de servicio evitando quiebres de stock"]},{"id":"channels_hypothesis_physical","titulo":"Hipótesis de Canal de Distribución Físico","afinidad":0.426,"fase_proyecto":"validacion","condiciones_activacion":["Si el producto es físico o híbrido físico/digital","Cuando se debate entre múltiples canales de venta"]},{"id":"personalizacion_guiada_por_el_cliente","titulo":"Personalización Guiada y el Símbolo de la Decisión del Cliente","afinidad":0.423,"fase_proyecto":"ejecucion","condiciones_activacion":["Cuando tu producto admite decisiones de personalización y no sabes cuales dejar en manos de tu cliente sin abrumarlo","Cuando tu cliente elige algo importante y no recibe nada tangible que se lo recuerde"]}],"respuesta_usuario":null,"candidatos_locales":["definicion_producto_proyecto","desarrollo_en_espiral","customer_discovery_get_out_of_building","customer_journey_mapping","data_integrity_forecasting","estrategia_producto_global_glocal"],"prioridad_declarada":null}`
2. `{"ruta":2,"tipo":"cobertura_conceptos","total":27,"cosecha":25}`
3. `{"tipo":"estimacion_banda","total":33,"con_banda":33}`

## Eventos (adaptación de preguntas, respaldos, guardián)

- `{"tipo":"decision_turno","decision":{"accion":"avanzar","camino":["customer_discovery_get_out_of_building"],"es_salto":false},"pregunta":"¿ya tienes algo concreto que puedas mostrarle a alguien, una pieza terminada o una foto, o todavía estás definiendo qué vas a fabricar?","nodo_actual":"voz_del_cliente_voc","razonamiento":"Usuario describe producto físico hecho a mano sin validación; el nodo de customer discovery aplica y la respuesta no está en el contexto.","saltos_posibles":[{"id":"customer_validation_sell_phase","titulo":"Sal a vender de verdad: valida con clientes reales","afinidad":0.469,"fase_proyecto":"validacion","condiciones_activacion":["Cuando necesitas comprobar con ventas reales si tu negocio funciona"]},{"id":"indice_de_reparabilidad","titulo":"Diseñar un puntaje de qué tan fácil es arreglar tu producto (índice de reparabilidad)","afinidad":0.451,"fase_proyecto":"planificacion","condiciones_activacion":["Si fabricas productos electrónicos que se venden en Francia, donde desde 2021 los fabricantes deben puntuar su reparabilidad, o si tu producto es físico y dura mucho tiempo, como electrodomésticos, dispositivos o muebles.","Si tu producto se puede romper o está pensado para volverse obsoleto."]},{"id":"get_out_building_test_sell","titulo":"Vender de verdad para probar tu modelo de negocio (test selling)","afinidad":0.439,"fase_proyecto":"validacion","condiciones_activacion":["Cuando ya terminaste de hablar con clientes para entender el problema y ya identificaste a tus primeros clientes convencidos","Si necesitas validar, todavía no escalar, tu modelo de negocio con pruebas reales de venta"]},{"id":"diseno_producto_cadena_suministro","titulo":"Diseño de Producto Orientado a la Cadena de Suministro","afinidad":0.437,"fase_proyecto":"planificacion","condiciones_activacion":["Cuando se está diseñando un nuevo producto físico","Cuando existen múltiples proveedores para componentes críticos y se busca simplificar la cadena"]},{"id":"cliente_disena_producto","titulo":"Deja que tu cliente diseñe el producto (co-creación digital)","afinidad":0.434,"fase_proyecto":"ideacion","condiciones_activacion":["Tu producto no requiere conocimiento técnico o científico avanzado (por ejemplo, con algo farmacéutico o aeroespacial esto en general no funciona)","Tienes una base de usuarios entusiastas dispuestos a co-crear contigo"]},{"id":"manufactura_aditiva_bajo_demanda","titulo":"Manufactura Aditiva (Impresión 3D) para Producción Bajo Demanda","afinidad":0.434,"fase_proyecto":"planificacion","condiciones_activacion":["Cuando la empresa enfrenta altos costos de inventario por gran variedad de productos de baja rotación","Si se busca mejorar el nivel de servicio evitando quiebres de stock"]},{"id":"channels_hypothesis_physical","titulo":"Hipótesis de Canal de Distribución Físico","afinidad":0.426,"fase_proyecto":"validacion","condiciones_activacion":["Si el producto es físico o híbrido físico/digital","Cuando se debate entre múltiples canales de venta"]},{"id":"personalizacion_guiada_por_el_cliente","titulo":"Personalización Guiada y el Símbolo de la Decisión del Cliente","afinidad":0.423,"fase_proyecto":"ejecucion","condiciones_activacion":["Cuando tu producto admite decisiones de personalización y no sabes cuales dejar en manos de tu cliente sin abrumarlo","Cuando tu cliente elige algo importante y no recibe nada tangible que se lo recuerde"]}],"respuesta_usuario":null,"candidatos_locales":["definicion_producto_proyecto","desarrollo_en_espiral","customer_discovery_get_out_of_building","customer_journey_mapping","data_integrity_forecasting","estrategia_producto_global_glocal"],"prioridad_declarada":null}`

## Veredicto del juez de sesión

```json
{
  "comentario": "Un solo turno sin salto semántico: la pregunta sobre si ya tiene una pieza terminada es pertinente, la ficha (dueño, sin jefe, 1 persona que fabrica) es consistente con el nodo de discovery, y no hay preguntas adaptadas que auditar.",
  "desajustes_de_papel": [],
  "repeticion_detectada": false,
  "pertinencia_transiciones": 5,
  "señales_fuera_de_material": []
}
```

## Coste

Por componente: `{"plan":0.0596761,"turnos":0.0013339500000000002,"estado_vivo":0.00047190000000000003,"juez_sesion":0.00025491,"clasificacion":0.00043506,"estimacion_banda":0.037299900000000004}`

| # | componente | modelo | entrada | salida | caché leída | caché 5 min | caché 1 h | USD | fin |
|---|---|---|---|---|---|---|---|---|---|
| 1 | clasificacion | claude-haiku-5-5 | 2844 | 137 | 1036 | 0 | 359 | 0.00044 | end_turn |
| 2 | turnos | claude-haiku-5-5 | 4 | 415 | 14660 | 7474 | 226 | 0.00133 | end_turn |
| 3 | plan | claude-sonnet-5-5 | 11043 | 3506 | 9141 | 0 | 404 | 0.05968 | end_turn |
| 4 | estado_vivo | claude-haiku-5-5 | 844 | 587 | 1320 | 0 | 404 | 0.00047 | end_turn |
| 5 | estimacion_banda | claude-sonnet-5-5 | 2377 | 699 | 1237 | 0 | 404 | 0.01348 | end_turn |
| 6 | estimacion_banda | claude-sonnet-5-5 | 2377 | 699 | 1641 | 0 | 0 | 0.01191 | end_turn |
| 7 | estimacion_banda | claude-sonnet-5-5 | 2377 | 699 | 1641 | 0 | 0 | 0.01191 | end_turn |
| 8 | juez_sesion | claude-haiku-5-5 | 752 | 163 | 1741 | 0 | 404 | 0.00025 | end_turn |
