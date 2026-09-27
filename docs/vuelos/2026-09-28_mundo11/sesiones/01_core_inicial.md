# Sesion 1: core / inicial

- id: f4f51e46-e24f-4b1e-8501-687180ec07d1
- creada: 2026-09-27T21:13:13.246046+00:00
- cerrada: 2026-09-27T21:16:32.026+00:00
- puerta de entrada: None (`None`)
- coste USD: 0.3024
- desglose: {"plan": 0.11282175, "turnos": 0.1352039, "estado_vivo": 0.0039050000000000005, "juez_sesion": 0.007699, "clasificacion": 0.002957, "estimacion_banda": 0.039816}
- fase final del recorrido: cerrada
- prioridad declarada: {"texto": "no saber si el precio que cobra de verdad le deja ganancia una vez que cuenta su tiempo", "conteo": 2}

## Mensaje de entrada

Hago y vendo macetas de cemento decorativas, ya tengo ventas reales por Instagram, pero no se si el precio que cobro de verdad me deja ganancia.

## Recorrido (etiqueta del riel, id, modo)

1. Cuestiona los Supuestos Contables (`arte_de_las_finanzas`, conversado)
2. Separa tus Costos y Gastos (`distincion_cogs_gastos_operativos`, silencioso)
3. Calcula tu Margen Bruto (`margen_bruto`, conversado)
4. Estima tus Costos con Precisión (`hoja_estimacion_costos`, salto)
5. Comprueba tu Hipótesis de Ingresos (`validacion_hipotesis_ingresos`, salto)
6. Revisa tus Hipótesis en Conjunto (`sintesis_hipotesis_modelo_negocio`, conversado)
7. Diseña Pruebas Simples y Claras (`diseno_experimentos_pass_fail`, conversado)
8. Calcula tu Punto de Equilibrio (`punto_equilibrio_unidades`, salto)
9. Retrata a tu Cliente Real (`arquetipos_de_cliente`, salto)
10. Usa Eventos para Atraer Clientes (`eventos_offline_como_canal_traccion`, salto)

## Ultimas preguntas

- Ahora el cuadro es completo y es más grave de lo que parecía. Tienes $200 de costos fijos al mes, pierdes $17 por cada maceta que vendes, y solo vendes 7 o 8 al mes. Eso significa que estás perdiendo dinero cada mes: entre los costos fijos y la pérdida por unidad, ¿cuánto crees que estás perdiendo mensualmente en este momento?
- Aqui esta el punto: estás perdiendo dinero cada mes sin saber por qué la gente compra ni si pagaria más. Antes de subir precio o cambiar algo, necesitas hablar con tus clientes de Instagram de verdad. Toma los tres ultimos que compraron: ¿quien son, que hacen, y por que eligieron tu maceta en lugar de otra que encontraron en Instagram?
- Bien, los mercados de fin de semana es un test real. Pero antes de ir, necesitas saber qué validar exactamente: ¿irás solo a ver si se venden a ese precio de 85, o también probarás si la gente pagaría más si la maceta tiene algo diferente o especial?

## Decisiones por turno (caja de vidrio)

```json
{
 "tipo": "decision_turno",
 "decision": {
  "accion": "avanzar",
  "camino": [
   "distincion_cogs_gastos_operativos",
   "margen_bruto"
  ],
  "es_salto": false
 },
 "nodo_actual": "arte_de_las_finanzas",
 "razonamiento": "El usuario tiene ventas reales pero desconoce su estructura de costos y márgenes. El camino va directamente a distinguir costos de producción (COGS) de gastos operativos, y luego a calcular margen bruto, que es el siguiente paso lógico para responder su pregunta central sobre rentabilidad por unidad.",
 "saltos_posibles": [
  {
   "id": "validacion_hipotesis_ingresos",
   "titulo": "Comprobar si tus ingresos aguantan el negocio",
   "afinidad": 0.526,
   "fase_proyecto": "validacion",
   "condiciones_activacion": [
    "Cuando ya definiste cómo vas a cobrar y necesitas decidir si el negocio vale la pena antes de crecer"
   ]
  },
  {
   "id": "customer_validation_sell_phase",
   "titulo": "Sal a vender de verdad: valida con clientes reales",
   "afinidad": 0.471,
   "fase_proyecto": "validacion",
   "condiciones_activacion": [
    "Cuando ya tienes tu producto listo (tu primera versión o MVP) y necesitas comprobar con ventas reales si tu negocio funciona"
   ]
  },
  {
   "id": "get_out_building_test_sell",
   "titulo": "Vender de verdad para probar tu modelo de negocio (test selling)",
   "afinidad": 0.453,
   "fase_proyecto": "validacion",
   "condiciones_activacion": [
    "Cuando ya terminaste de hablar con clientes para entender el problema y ya identificaste a tus primeros clientes convencidos",
    "Si necesitas validar, todavia no escalar, tu modelo de negocio con pruebas reales de venta"
   ]
  },
  {
   "id": "verificar_modelo_ingresos",
   "titulo": "Verificar si se Puede Generar Ingresos y Crecer (Revenue Model Data)",
   "afinidad": 0.446,
   "fase_proyecto": "validacion",
   "condiciones_activacion": [
    "Cuando necesitas decidir si tu modelo de negocio es financieramente viable antes de escalar",
    "Cuando inversionistas o tú mismo requieren evidencia numérica de rentabilidad potencial"
   ]
  },
  {
   "id": "plantea_oferta_como_rango_o_cifra_precisa",
   "titulo": "Plantea tu oferta como un rango o con una cifra precisa, no redonda",
   "afinidad": 0.445,
   "fase_proyecto": "ejecucion",
   "condiciones_activacion": [
    "Te van a preguntar tu precio antes de conocer el de la otra parte.",
    "No conoces con certeza el valor de mercado de lo que estás vendiendo o comprando."
   ]
  },
  {
   "id": "demand_curve_pricing",
   "titulo": "Curva de Demanda y Estrategia de Precios",
   "afinidad": 0.433,
   "fase_proyecto": "planificacion",
   "condiciones_activacion": [
    "Cuando el modelo de negocio depende de un producto físico con costos de manufactura variables según escala",
    "Si hay dudas sobre si el precio actual es sostenible a largo plazo"
   ]
  },
  {
   "id": "owner_earnings",
   "titulo": "Ganancias del propietario (Owner Earnings)",
   "afinidad": 0.433,
   "fase_proyecto": "ejecucion",
   "condiciones_activacion": [
    "Cuando necesitas saber cuánto efectivo te deja realmente tu negocio y cuánto podrías retirar sin dañarlo"
   ]
  },
  {
   "id": "diferencia_ganancia_flujo_caja",
   "titulo": "Ganar dinero no es lo mismo que tener dinero: por qué un negocio rentable se puede quedar sin efectivo",
   "afinidad": 0.432,
   "fase_proyecto": "ejecucion",
   "condiciones_activacion": [
    "Si tu negocio está creciendo rápido en ventas pero no has revisado tu flujo de caja",
    "Si tu negocio muestra ganancias en los reportes pero te cuesta pagar tus facturas"
   ]
  }
 ],
 "respuesta_usuario": null,
 "candidatos_locales": [
  "reconocimiento_de_ingresos",
  "distincion_cogs_gastos_operativos",
  "depreciacion_y_amortizacion",
  "metodos_de_valuacion"
 ],
 "prioridad_declarada": {
  "texto": "entender si el precio actual genera ganancia real o si deja dinero sobre la mesa",
  "conteo": 1
 }
}
```
```json
{
 "tipo": "decision_turno",
 "decision": {
  "accion": "repreguntar",
  "camino": [],
  "es_salto": false
 },
 "nodo_actual": "margen_bruto",
 "razonamiento": "La respuesta describe los canales de venta pero no contesta la pregunta específica sobre costos unitarios ni precio de venta. Necesito esos números concretos para avanzar en el cálculo de margen bruto.",
 "saltos_posibles": [
  {
   "id": "cliente_disena_producto",
   "titulo": "Deja que tu cliente diseñe el producto (co-creación digital)",
   "afinidad": 0.357,
   "fase_proyecto": "ideacion",
   "condiciones_activacion": [
    "Tu producto no requiere conocimiento técnico o científico avanzado (por ejemplo, no aplica si vendes algo farmacéutico o aeroespacial)",
    "Tienes una base de usuarios entusiastas dispuestos a co-crear contigo"
   ]
  },
  {
   "id": "prototipar_con_medios_no_convencionales",
   "titulo": "Use Unconventional Mediums: Prototipar con Materiales Inesperados",
   "afinidad": 0.341,
   "fase_proyecto": "ideacion",
   "condiciones_activacion": [
    "Cuando estás estancado usando siempre el mismo tipo de prototipo o formato",
    "Cuando necesitas hacer tangible una tecnología abstracta o invisible como algoritmos o datos"
   ]
  },
  {
   "id": "indice_de_reparabilidad",
   "titulo": "Diseñar un puntaje de qué tan fácil es arreglar tu producto (índice de reparabilidad)",
   "afinidad": 0.338,
   "fase_proyecto": "planificacion",
   "condiciones_activacion": [
    "Si vendes en Francia productos electrónicos, donde desde 2021 debes puntuar su reparabilidad, o si tu producto es físico y dura mucho tiempo, como electrodomésticos, dispositivos o muebles.",
    "Si tu producto se puede romper o está pensado para volverse obsoleto."
   ]
  },
  {
   "id": "publicidad_no_convencional_stunts",
   "titulo": "Acciones de impacto para llamar la atención (publicity stunts)",
   "afinidad": 0.337,
   "fase_proyecto": "ejecucion",
   "condiciones_activacion": [
    "Cuando tienes poco presupuesto de marketing pero buscas visibilidad rápida",
    "Cuando necesitas diferenciarte de competidores con presupuestos publicitarios mucho más grandes"
   ]
  },
  {
   "id": "diseno_para_sostenibilidad_cradle_to_cradle",
   "titulo": "Diseño sin basura: de la cuna a la cuna (Cradle to Cradle)",
   "afinidad": 0.336,
   "fase_proyecto": "ideacion",
   "condiciones_activacion": [
    "Cuando quieres reducir el impacto ambiental de un producto fisico",
    "Si tu negocio tiene valores centrales de sostenibilidad que quieres hacer crecer sin traicionarlos"
   ]
  },
  {
   "id": "biomimicry_conexiones_naturales",
   "titulo": "Conexiones naturales para innovar (biomimética)",
   "afinidad": 0.333,
   "fase_proyecto": "ideacion",
   "condiciones_activacion": [
    "Si buscas soluciones sostenibles o eficientes.",
    "Si estás estancado en las soluciones típicas de tu sector y no encuentras salida."
   ]
  },
  {
   "id": "arquetipos_de_cliente",
   "titulo": "El retrato de tu cliente (arquetipo de cliente)",
   "afinidad": 0.322,
   "fase_proyecto": "validacion",
   "condiciones_activacion": [
    "Cuando ya explorastes a tus clientes pero todavia no tienes claro el perfil al que apuntas",
    "Si necesitas ordenar las prioridades de lo que vas a construir"
   ]
  },
  {
   "id": "eventos_offline_como_canal_traccion",
   "titulo": "Eventos presenciales para conseguir tus primeros clientes (canal de tracción)",
   "afinidad": 0.32,
   "fase_proyecto": "ejecucion",
   "condiciones_activacion": [
    "Si vendes a otras empresas o a un grupo de personas fácil de identificar",
    "Si otros canales digitales, como anuncios o buscadores, ya no te dan resultado"
   ]
  }
 ],
 "respuesta_usuario": "Hago macetas de cemento decorativas, chicas y medianas, las vendo a tiendas de plantas y directo por Instagram.",
 "candidatos_locales": [
  "margen_operativo",
  "punto_equilibrio_unidades"
 ],
 "prioridad_declarada": {
  "texto": "entender si el precio actual genera ganancia real o si deja dinero sobre la mesa",
  "conteo": 1
 }
}
```
```json
{
 "tipo": "decision_turno",
 "decision": {
  "accion": "avanzar",
  "camino": [
   "hoja_estimacion_costos"
  ],
  "es_salto": true
 },
 "nodo_actual": "margen_bruto",
 "razonamiento": "El usuario respondió que no ha calculado costos de materiales ni tiempo. saltos_posibles incluye 'Hoja de Trabajo de Estimación de Costos' (afinidad 0.439) que es más específico y dedicado a este dato nuevo que cualquiera de los sucesores locales de margen_bruto. Salta ahí para que tenga una metodología clara para hacer la cuenta.",
 "saltos_posibles": [
  {
   "id": "hoja_estimacion_costos",
   "titulo": "Hoja de Trabajo de Estimación de Costos",
   "afinidad": 0.439,
   "fase_proyecto": "planificacion",
   "condiciones_activacion": [
    "Cuando se requiere detalle metodológico para justificar una estimación de costos"
   ]
  },
  {
   "id": "estimate_at_completion_eac",
   "titulo": "Cuánto te va a costar terminar (Estimación al Completar o EAC)",
   "afinidad": 0.422,
   "fase_proyecto": "ejecucion",
   "condiciones_activacion": [
    "Cuando tu proyecto está en marcha y necesitas saber cuánto vas a gastar al final",
    "Cuando hay diferencias en costos o tiempos que necesitas proyectar hacia adelante"
   ]
  },
  {
   "id": "estimacion_costos_actividad",
   "titulo": "Estimación de Costos de Actividad",
   "afinidad": 0.407,
   "fase_proyecto": "planificacion",
   "condiciones_activacion": [
    "Cuando se necesita calcular el presupuesto detallado del proyecto"
   ]
  },
  {
   "id": "validacion_hipotesis_ingresos",
   "titulo": "Comprobar si tus ingresos aguantan el negocio",
   "afinidad": 0.403,
   "fase_proyecto": "validacion",
   "condiciones_activacion": [
    "Cuando ya definiste cómo vas a cobrar y necesitas decidir si el negocio vale la pena antes de crecer"
   ]
  },
  {
   "id": "gates_tempranos_flexibles",
   "titulo": "No exijas números exactos demasiado pronto",
   "afinidad": 0.367,
   "fase_proyecto": "ideacion",
   "condiciones_activacion": [
    "Cuando estás evaluando una idea nueva o arriesgada en sus primeras etapas y todavía no tienes datos firmes"
   ]
  },
  {
   "id": "plantea_oferta_como_rango_o_cifra_precisa",
   "titulo": "Plantea tu oferta como un rango o con una cifra precisa, no redonda",
   "afinidad": 0.346,
   "fase_proyecto": "ejecucion",
   "condiciones_activacion": [
    "Te van a preguntar tu precio antes de conocer el de la otra parte.",
    "No conoces con certeza el valor de mercado de lo que estás vendiendo o comprando."
   ]
  },
  {
   "id": "ecuacion_de_valor_cliente",
   "titulo": "Ecuación de Valor del Cliente",
   "afinidad": 0.342,
   "fase_proyecto": "ejecucion",
   "condiciones_activacion": [
    "Cuando el precio o costo de la solución es alto en relación al problema percibido por el cliente",
    "Cuando se recibe la objeción 'es demasiado caro' o 'no vale la pena el esfuerzo de cambiar'"
   ]
  },
  {
   "id": "definicion_producto_proyecto",
   "titulo": "Define tu producto y tu proyecto desde el principio, con datos reales",
   "afinidad": 0.336,
   "fase_proyecto": "planificacion",
   "condiciones_activacion": [
    "Antes de pasar a la etapa de construir el producto",
    "Cuando notas que el proyecto crece sin control o las especificaciones cambian todo el tiempo"
   ]
  }
 ],
 "respuesta_usuario": "Cobro por pieza pero no he calculado bien cuanto me cuesta en minutos y materiales hacer cada maceta.",
 "candidatos_locales": [
  "margen_operativo",
  "punto_equilibrio_unidades"
 ],
 "prioridad_declarada": {
  "texto": "entender si el precio actual genera ganancia real o si deja dinero sobre la mesa",
  "conteo": 1
 }
}
```
```json
{
 "tipo": "decision_turno",
 "decision": {
  "accion": "repreguntar",
  "camino": [],
  "es_salto": false
 },
 "nodo_actual": "hoja_estimacion_costos",
 "razonamiento": "El usuario evitó nuevamente responder números concretos (precio de venta, costo de materiales) y en su lugar dio contexto sobre volumen y tiempo. Necesito repreguntar de forma más directa y concreta, enfocándome en datos específicos de esas 15 ventas reales que ya pasaron.",
 "saltos_posibles": [
  {
   "id": "customer_validation_sell_phase",
   "titulo": "Sal a vender de verdad: valida con clientes reales",
   "afinidad": 0.473,
   "fase_proyecto": "validacion",
   "condiciones_activacion": [
    "Cuando ya tienes tu producto listo (tu primera versión o MVP) y necesitas comprobar con ventas reales si tu negocio funciona"
   ]
  },
  {
   "id": "channels_hypothesis_web_mobile",
   "titulo": "Cómo va a llegar tu producto al cliente (canal de venta digital)",
   "afinidad": 0.445,
   "fase_proyecto": "planificacion",
   "condiciones_activacion": [
    "Si tu producto es una aplicación web o móvil",
    "Cuando necesitas decidir cómo va a llegar tu producto al cliente por medios digitales"
   ]
  },
  {
   "id": "validacion_hipotesis_ingresos",
   "titulo": "Comprobar si tus ingresos aguantan el negocio",
   "afinidad": 0.433,
   "fase_proyecto": "validacion",
   "condiciones_activacion": [
    "Cuando ya definiste cómo vas a cobrar y necesitas decidir si el negocio vale la pena antes de crecer"
   ]
  },
  {
   "id": "get_out_building_test_sell",
   "titulo": "Vender de verdad para probar tu modelo de negocio (test selling)",
   "afinidad": 0.421,
   "fase_proyecto": "validacion",
   "condiciones_activacion": [
    "Cuando ya terminaste de hablar con clientes para entender el problema y ya identificaste a tus primeros clientes convencidos",
    "Si necesitas validar, todavia no escalar, tu modelo de negocio con pruebas reales de venta"
   ]
  },
  {
   "id": "prueba_solucion_con_cliente",
   "titulo": "Prueba de la Solución con el Cliente",
   "afinidad": 0.416,
   "fase_proyecto": "validacion",
   "condiciones_activacion": [
    "Cuando ya tienes una presentación de tu solución validada y necesitas evidencia de que la gente pagaría por ella",
    "Cuando vendes a través de un socio o distribuidor y necesitas entender cómo funciona su negocio"
   ]
  },
  {
   "id": "validar_canal_distribucion",
   "titulo": "Validar Socios de Canal de Distribución (Channel Partners)",
   "afinidad": 0.397,
   "fase_proyecto": "validacion",
   "condiciones_activacion": [
    "Si el modelo de negocio depende de canales de distribución indirectos como retail, mayoristas o representantes",
    "Cuando ya cuentas con evidencia de demanda real de clientes finales"
   ]
  },
  {
   "id": "earned_vs_paid_media",
   "titulo": "Prensa gratis vs publicidad pagada para conseguir clientes",
   "afinidad": 0.385,
   "fase_proyecto": "validacion",
   "condiciones_activacion": [
    "Cuando tienes que decidir cómo repartir tu presupuesto de marketing entre medios gratuitos y pagados"
   ]
  },
  {
   "id": "verificar_modelo_ingresos",
   "titulo": "Verificar si se Puede Generar Ingresos y Crecer (Revenue Model Data)",
   "afinidad": 0.385,
   "fase_proyecto": "validacion",
   "condiciones_activacion": [
    "Cuando necesitas decidir si tu modelo de negocio es financieramente viable antes de escalar",
    "Cuando inversionistas o tú mismo requieren evidencia numérica de rentabilidad potencial"
   ]
  }
 ],
 "respuesta_usuario": "Llevo dos meses vendiendo, ya tengo unas 15 ventas reales, sobre todo por Instagram y una tienda de plantas que me las revende.",
 "candidatos_locales": [
  "linea_base_costos"
 ],
 "prioridad_declarada": {
  "texto": "entender si el precio actual genera ganancia real o si deja dinero sobre la mesa",
  "conteo": 1
 }
}
```
```json
{
 "tipo": "decision_turno",
 "decision": {
  "accion": "avanzar",
  "camino": [
   "validacion_hipotesis_ingresos"
  ],
  "es_salto": true
 },
 "nodo_actual": "hoja_estimacion_costos",
 "razonamiento": "El usuario reafirmó su prioridad central (conteo ahora=2): necesita validar si sus ingresos reales aguantan el negocio cuando incluye su tiempo. saltos_posibles incluye 'Comprobar si tus ingresos aguantan el negocio' (afinidad 0.577, la más alta) que es más específico que sucesores locales sobre línea base de costos. Salta ahí, donde se valida directamente si el modelo de ingresos es viable.",
 "saltos_posibles": [
  {
   "id": "validacion_hipotesis_ingresos",
   "titulo": "Comprobar si tus ingresos aguantan el negocio",
   "afinidad": 0.577,
   "fase_proyecto": "validacion",
   "condiciones_activacion": [
    "Cuando ya definiste cómo vas a cobrar y necesitas decidir si el negocio vale la pena antes de crecer"
   ]
  },
  {
   "id": "verificar_modelo_ingresos",
   "titulo": "Verificar si se Puede Generar Ingresos y Crecer (Revenue Model Data)",
   "afinidad": 0.461,
   "fase_proyecto": "validacion",
   "condiciones_activacion": [
    "Cuando necesitas decidir si tu modelo de negocio es financieramente viable antes de escalar",
    "Cuando inversionistas o tú mismo requieren evidencia numérica de rentabilidad potencial"
   ]
  },
  {
   "id": "diferencia_ganancia_flujo_caja",
   "titulo": "Ganar dinero no es lo mismo que tener dinero: por qué un negocio rentable se puede quedar sin efectivo",
   "afinidad": 0.461,
   "fase_proyecto": "ejecucion",
   "condiciones_activacion": [
    "Si tu negocio está creciendo rápido en ventas pero no has revisado tu flujo de caja",
    "Si tu negocio muestra ganancias en los reportes pero te cuesta pagar tus facturas"
   ]
  },
  {
   "id": "plantea_oferta_como_rango_o_cifra_precisa",
   "titulo": "Plantea tu oferta como un rango o con una cifra precisa, no redonda",
   "afinidad": 0.456,
   "fase_proyecto": "ejecucion",
   "condiciones_activacion": [
    "Te van a preguntar tu precio antes de conocer el de la otra parte.",
    "No conoces con certeza el valor de mercado de lo que estás vendiendo o comprando."
   ]
  },
  {
   "id": "factores_valoracion_startup",
   "titulo": "Qué determina cuánto vale tu empresa para un inversionista",
   "afinidad": 0.456,
   "fase_proyecto": "planificacion",
   "condiciones_activacion": [
    "Cuando estás preparando o negociando una ronda de inversión",
    "Cuando no te pones de acuerdo con un inversionista sobre cuánto vale tu empresa"
   ]
  },
  {
   "id": "compensacion_fundadores_cash_vs_equity",
   "titulo": "Cuánto sueldo dejas de cobrar a cambio de participación",
   "afinidad": 0.455,
   "fase_proyecto": "planificacion",
   "condiciones_activacion": [
    "Si tú y tus cofundadores están definiendo los sueldos en las primeras etapas del negocio",
    "Si después de recibir inversión los nuevos inversores empiezan a opinar sobre tu sueldo"
   ]
  },
  {
   "id": "ecuacion_de_valor_cliente",
   "titulo": "Ecuación de Valor del Cliente",
   "afinidad": 0.447,
   "fase_proyecto": "ejecucion",
   "condiciones_activacion": [
    "Cuando el precio o costo de la solución es alto en relación al problema percibido por el cliente",
    "Cuando se recibe la objeción 'es demasiado caro' o 'no vale la pena el esfuerzo de cambiar'"
   ]
  },
  {
   "id": "seleccion_estrategia_pricing",
   "titulo": "Selección de Estrategia de Pricing",
   "afinidad": 0.441,
   "fase_proyecto": "planificacion",
   "condiciones_activacion": [
    "Cuando necesitas definir cómo vas a cobrar por tu producto o servicio",
    "Si tienes dudas sobre qué modelo de precio maximiza rentabilidad y adopción"
   ]
  }
 ],
 "respuesta_usuario": "Lo que mas me preocupa es no saber si el precio que cobro de verdad me deja ganancia una vez que cuento mi tiempo.",
 "candidatos_locales": [
  "linea_base_costos"
 ],
 "prioridad_declarada": {
  "texto": "no saber si el precio que cobra de verdad le deja ganancia una vez que cuenta su tiempo",
  "conteo": 2
 }
}
```
```json
{
 "tipo": "decision_turno",
 "decision": {
  "accion": "repreguntar",
  "camino": [],
  "es_salto": false
 },
 "nodo_actual": "validacion_hipotesis_ingresos",
 "razonamiento": "El usuario finalmente dio números concretos de costo de materiales y tiempo. Falta aún el precio de venta, que es crucial para calcular si hay ganancia. Repregunta enfocada en ese dato faltante, considerando que mencionó dos canales (tienda y venta directa) que podrían tener precios distintos.",
 "saltos_posibles": [
  {
   "id": "prototipar_con_medios_no_convencionales",
   "titulo": "Use Unconventional Mediums: Prototipar con Materiales Inesperados",
   "afinidad": 0.379,
   "fase_proyecto": "ideacion",
   "condiciones_activacion": [
    "Cuando estás estancado usando siempre el mismo tipo de prototipo o formato",
    "Cuando necesitas hacer tangible una tecnología abstracta o invisible como algoritmos o datos"
   ]
  },
  {
   "id": "amar_las_restricciones",
   "titulo": "Aprender a Amar las Restricciones",
   "afinidad": 0.365,
   "fase_proyecto": "ideacion",
   "condiciones_activacion": [
    "Cuando estés tentado a eliminar todas las limitaciones en lugar de diseñar con ellas.",
    "Cuando estés definiendo un producto o servicio desde cero."
   ]
  },
  {
   "id": "manufactura_aditiva_bajo_demanda",
   "titulo": "Manufactura Aditiva (Impresión 3D) para Producción Bajo Demanda",
   "afinidad": 0.341,
   "fase_proyecto": "planificacion",
   "condiciones_activacion": [
    "Cuando la empresa enfrenta altos costos de inventario por gran variedad de productos de baja rotación",
    "Si se busca mejorar el nivel de servicio evitando quiebres de stock"
   ]
  },
  {
   "id": "estimacion_costos_actividad",
   "titulo": "Estimación de Costos de Actividad",
   "afinidad": 0.34,
   "fase_proyecto": "planificacion",
   "condiciones_activacion": [
    "Cuando se necesita calcular el presupuesto detallado del proyecto"
   ]
  },
  {
   "id": "falacia_del_disenador_affordances",
   "titulo": "El error de creer que tú controlas cómo usarán tu diseño (y las pistas que el objeto mismo da)",
   "afinidad": 0.336,
   "fase_proyecto": "ideacion",
   "condiciones_activacion": [
    "Si estás dando por hecho que la gente va a usar tu producto exactamente como lo pensaste.",
    "Si estás definiendo cómo será tu producto sin considerar usos que puedan surgir por su cuenta."
   ]
  },
  {
   "id": "estrategia_circular_y_mecanismo_de_retorno",
   "titulo": "Elección de Estrategia Circular y Diseño del Mecanismo de Retorno",
   "afinidad": 0.313,
   "fase_proyecto": "planificacion",
   "condiciones_activacion": [
    "Cuando ya decidiste que tu modelo de negocio será circular y hay que elegir por cuál de las cinco estrategias empezar",
    "Antes de simular o dimensionar la cadena, porque la simulación necesita una estrategia y un mecanismo ya elegidos para comparar"
   ]
  },
  {
   "id": "decision_intensidad_capital",
   "titulo": "Cuánto dinero necesita tu negocio y qué partes haces tú mismo",
   "afinidad": 0.307,
   "fase_proyecto": "planificacion",
   "condiciones_activacion": [
    "Cuando tengas que decidir entre construir capacidades tú mismo o contratar afuera",
    "Cuando estés evaluando crecer por franquicia para expandirte sin buscar inversión externa"
   ]
  },
  {
   "id": "alfabetizacion_en_materiales_maliciosos",
   "titulo": "Alfabetización en Materiales Traviesos (Mischievous Materials)",
   "afinidad": 0.303,
   "fase_proyecto": "ideacion",
   "condiciones_activacion": [
    "Cuando tu proyecto involucra tecnologías emergentes complejas, como inteligencia artificial, blockchain o biotecnología.",
    "Si necesitas explicarle la tecnología a alguien que te ayuda pero no tiene formación técnica."
   ]
  }
 ],
 "respuesta_usuario": "Cada maceta me cuesta como 68 en materiales -- cemento, moldes, pintura -- y le dedico un par de horas entre mezclar, moldear y pulir.",
 "candidatos_locales": [
  "sintesis_hipotesis_modelo_negocio",
  "estrategia_ferias_comerciales"
 ],
 "prioridad_declarada": {
  "texto": "no saber si el precio que cobra de verdad le deja ganancia una vez que cuenta su tiempo",
  "conteo": 2
 }
}
```
```json
{
 "tipo": "decision_turno",
 "decision": {
  "accion": "avanzar",
  "camino": [
   "sintesis_hipotesis_modelo_negocio"
  ],
  "es_salto": false
 },
 "nodo_actual": "validacion_hipotesis_ingresos",
 "razonamiento": "El usuario está a un paso de responder su propia pregunta central: tiene costos (materiales + tiempo valuado), pero falta el precio de venta para calcular ganancia real. Síntesis de hipótesis es el nodo correcto: revisa todas las piezas juntas, y esta pregunta directa cierra el dato faltante antes de cualquier otra validación.",
 "saltos_posibles": [],
 "respuesta_usuario": "Valoro mi hora de trabajo en unos 17, aunque nunca lo habia puesto en numeros asi.",
 "candidatos_locales": [
  "sintesis_hipotesis_modelo_negocio",
  "estrategia_ferias_comerciales"
 ],
 "prioridad_declarada": {
  "texto": "no saber si el precio que cobra de verdad le deja ganancia una vez que cuenta su tiempo",
  "conteo": 2
 }
}
```
```json
{
 "tipo": "decision_turno",
 "decision": {
  "accion": "avanzar",
  "camino": [
   "diseno_experimentos_pass_fail"
  ],
  "es_salto": false
 },
 "nodo_actual": "sintesis_hipotesis_modelo_negocio",
 "razonamiento": "El usuario finalmente reveló el precio de venta ($85) y ahora tenemos el cuadro completo: cuesta $102, vende a $85, pierde $17 por unidad. Su prioridad declarada (conteo=2) acaba de ser resuelta con evidencia clara. El siguiente paso no es teoría financiera sino decisión y validación: necesita elegir entre aumentar precio, reducir costos o probar que el mercado pagaria mas. El nodo 'diseno_experimentos_pass_fail' es donde decide cual hipótesis validar primero.",
 "saltos_posibles": [
  {
   "id": "demand_curve_pricing",
   "titulo": "Curva de Demanda y Estrategia de Precios",
   "afinidad": 0.391,
   "fase_proyecto": "planificacion",
   "condiciones_activacion": [
    "Cuando el modelo de negocio depende de un producto físico con costos de manufactura variables según escala",
    "Si hay dudas sobre si el precio actual es sostenible a largo plazo"
   ]
  },
  {
   "id": "seleccion_canal_fisico",
   "titulo": "Selección de Canal de Distribución Física",
   "afinidad": 0.375,
   "fase_proyecto": "planificacion",
   "condiciones_activacion": [
    "Si el producto es físico y requiere intermediarios para llegar al consumidor final"
   ]
  },
  {
   "id": "long_tail_pattern",
   "titulo": "Patrón de la Larga Cola (Long Tail)",
   "afinidad": 0.361,
   "fase_proyecto": "ideacion",
   "condiciones_activacion": [
    "Si el negocio puede beneficiarse de ofrecer variedad en vez de concentrarse solo en productos de alta demanda.",
    "Si existen bajos costos marginales de producción/distribución digital."
   ]
  },
  {
   "id": "plantea_oferta_como_rango_o_cifra_precisa",
   "titulo": "Plantea tu oferta como un rango o con una cifra precisa, no redonda",
   "afinidad": 0.343,
   "fase_proyecto": "ejecucion",
   "condiciones_activacion": [
    "Te van a preguntar tu precio antes de conocer el de la otra parte.",
    "No conoces con certeza el valor de mercado de lo que estás vendiendo o comprando."
   ]
  },
  {
   "id": "publicidad_remanente_remnant_ads",
   "titulo": "Publicidad Remanente (Remnant Advertising)",
   "afinidad": 0.339,
   "fase_proyecto": "ejecucion",
   "condiciones_activacion": [
    "Cuando el presupuesto es limitado y el producto es masivo, sin necesidad de targeting fino de tiempo o lugar"
   ]
  },
  {
   "id": "ecuacion_de_valor",
   "titulo": "La Ecuación de Valor",
   "afinidad": 0.327,
   "fase_proyecto": "validacion",
   "condiciones_activacion": [
    "Cuando el usuario enfrenta resistencia de precio o percibe que el cliente no ve suficiente urgencia para comprar una solución costosa"
   ]
  },
  {
   "id": "get_out_building_test_sell",
   "titulo": "Vender de verdad para probar tu modelo de negocio (test selling)",
   "afinidad": 0.323,
   "fase_proyecto": "validacion",
   "condiciones_activacion": [
    "Cuando ya terminaste de hablar con clientes para entender el problema y ya identificaste a tus primeros clientes convencidos",
    "Si necesitas validar, todavia no escalar, tu modelo de negocio con pruebas reales de venta"
   ]
  },
  {
   "id": "embudo_atricion_nuevos_productos",
   "titulo": "El Embudo de Atrición de Nuevos Productos (Odds 7 a 1)",
   "afinidad": 0.323,
   "fase_proyecto": "ejecucion",
   "condiciones_activacion": [
    "Cuando se necesita justificar la cantidad de ideas necesarias para lograr un éxito comercial",
    "Si la empresa no mide sus tasas de fracaso"
   ]
  }
 ],
 "respuesta_usuario": "Las vendo en 85 cada una, mas o menos, dependiendo del tamano.",
 "candidatos_locales": [
  "diseno_experimentos_pass_fail",
  "customer_discovery",
  "aprendizaje_validado",
  "metricas_de_adquisicion_activacion",
  "disenar_tests_pass_fail",
  "hablar_con_clientes_desmontar_supuestos"
 ],
 "prioridad_declarada": {
  "texto": "no saber si el precio que cobra de verdad le deja ganancia una vez que cuenta su tiempo",
  "conteo": 2
 }
}
```
```json
{
 "tipo": "decision_turno",
 "decision": {
  "accion": "repreguntar",
  "camino": [],
  "es_salto": false
 },
 "nodo_actual": "diseno_experimentos_pass_fail",
 "razonamiento": "El usuario respondió con su capacidad de producción, no con una decisión sobre precio o costos. Tiene espacio para crecer en volumen (produce 10/semana pero vende ~7.5/semana). Antes de preguntarle si sube precio o baja costos, necesito entender si el problema es demanda o estructura de costos. Una repregunta enfocada en validación con clientes ajenos (no amigos, no su círculo) es el siguiente paso lógico para decidir si el precio es el obstáculo o si simplemente no ha probado la propuesta con audiencia real.",
 "saltos_posibles": [
  {
   "id": "gestion_equilibrio_familia_startup",
   "titulo": "Cómo equilibrar tu negocio y tu familia",
   "afinidad": 0.412,
   "fase_proyecto": "planificacion",
   "condiciones_activacion": [
    "Cuando mencionas preocupaciones familiares o de pareja como freno para emprender",
    "Cuando identificas el factor personal como desfavorable dentro del marco de las tres preguntas"
   ]
  },
  {
   "id": "decision_factory_mentality",
   "titulo": "Haz menos proyectos, pero hazlos bien",
   "afinidad": 0.375,
   "fase_proyecto": "planificacion",
   "condiciones_activacion": [
    "Cuando tienes demasiados proyectos a la vez y no das abasto para atenderlos",
    "Si el tiempo que tardas en lanzar se ha vuelto demasiado largo, o directamente no logras lanzar nada"
   ]
  },
  {
   "id": "founders_activities_clause",
   "titulo": "La cláusula que te exige dedicar todo tu tiempo a tu empresa (Founders' Activities)",
   "afinidad": 0.333,
   "fase_proyecto": "ejecucion",
   "condiciones_activacion": [
    "Tienes otros proyectos o compromisos profesionales activos",
    "El inversor te pide explícitamente esta cláusula por antecedentes de desconfianza"
   ]
  }
 ],
 "respuesta_usuario": "Puedo hacer unas 10 a la semana trabajando en mis ratos libres, sin descuidar mi otro trabajo.",
 "candidatos_locales": [
  "preparar_contacto_clientes",
  "customer_discovery",
  "customer_discovery_phase2_problem_test",
  "global_vs_local_maximum"
 ],
 "prioridad_declarada": {
  "texto": "no saber si el precio que cobra de verdad le deja ganancia una vez que cuenta su tiempo",
  "conteo": 2
 }
}
```
```json
{
 "tipo": "decision_turno",
 "decision": {
  "accion": "avanzar",
  "camino": [
   "punto_equilibrio_unidades"
  ],
  "es_salto": true
 },
 "nodo_actual": "diseno_experimentos_pass_fail",
 "razonamiento": "El usuario acaba de revelar costos fijos ($200/mes) que completan el cuadro financiero. Su prioridad declarada ya fue resuelta con evidencia: está perdiendo dinero activamente. El siguiente nodo crucial es 'Punto de Equilibrio' (Break-Even) para que vea cuántas unidades DEBE vender cada mes solo para no perder dinero, y eso lo enfrentará con la realidad de si subir precio, bajar costos o cambiar la estrategia de demanda es urgente. Este es un nodo de salto porque es más específico que los sucesores locales (que tratan validación general de cliente discovery) al problema financiero concreto que acaba de expresar.",
 "saltos_posibles": [
  {
   "id": "cash_burn_calculation",
   "titulo": "Cuánto dinero quemas cada trimestre (Cash Burn)",
   "afinidad": 0.364,
   "fase_proyecto": "planificacion",
   "condiciones_activacion": [
    "Cuando necesitas saber cuánto tiempo puedes operar antes de quedarte sin capital",
    "Antes de decidir si escalas el negocio o buscas más financiamiento"
   ]
  },
  {
   "id": "decision_intensidad_capital",
   "titulo": "Cuánto dinero necesita tu negocio y qué partes haces tú mismo",
   "afinidad": 0.359,
   "fase_proyecto": "planificacion",
   "condiciones_activacion": [
    "Cuando tengas que decidir entre construir capacidades tú mismo o contratar afuera",
    "Cuando estés evaluando crecer por franquicia para expandirte sin buscar inversión externa"
   ]
  },
  {
   "id": "punto_equilibrio_unidades",
   "titulo": "Punto de Equilibrio y Margen de Contribución (Break-Even Point & Contribution Margin)",
   "afinidad": 0.352,
   "fase_proyecto": "planificacion",
   "condiciones_activacion": [
    "Cuando el usuario necesita saber cuántas unidades debe vender al mes para no perder dinero",
    "Si el usuario tiene costos fijos y variables identificados pero no sabe combinarlos en una meta de ventas concreta"
   ]
  },
  {
   "id": "diferencia_ganancia_flujo_caja",
   "titulo": "Ganar dinero no es lo mismo que tener dinero: por qué un negocio rentable se puede quedar sin efectivo",
   "afinidad": 0.348,
   "fase_proyecto": "ejecucion",
   "condiciones_activacion": [
    "Si tu negocio está creciendo rápido en ventas pero no has revisado tu flujo de caja",
    "Si tu negocio muestra ganancias en los reportes pero te cuesta pagar tus facturas"
   ]
  },
  {
   "id": "burn_rate_por_etapa",
   "titulo": "Cómo manejar tu ritmo de gasto (burn rate) según la etapa de tu negocio",
   "afinidad": 0.343,
   "fase_proyecto": "validacion",
   "condiciones_activacion": [
    "En cualquier etapa de tu negocio donde necesites controlar el gasto de efectivo"
   ]
  },
  {
   "id": "verificar_modelo_ingresos",
   "titulo": "Verificar si se Puede Generar Ingresos y Crecer (Revenue Model Data)",
   "afinidad": 0.343,
   "fase_proyecto": "validacion",
   "condiciones_activacion": [
    "Cuando necesitas decidir si tu modelo de negocio es financieramente viable antes de escalar",
    "Cuando inversionistas o tú mismo requieren evidencia numérica de rentabilidad potencial"
   ]
  },
  {
   "id": "estimacion_costos_actividad",
   "titulo": "Estimación de Costos de Actividad",
   "afinidad": 0.339,
   "fase_proyecto": "planificacion",
   "condiciones_activacion": [
    "Cuando se necesita calcular el presupuesto detallado del proyecto"
   ]
  },
  {
   "id": "calculo_roi",
   "titulo": "Cálculo del Retorno sobre la Inversión (ROI)",
   "afinidad": 0.334,
   "fase_proyecto": "ejecucion",
   "condiciones_activacion": [
    "Si el emprendedor está considerando comprar equipo, maquinaria o tecnología nueva",
    "Antes de comprometer capital significativo en cualquier activo de largo plazo"
   ]
  }
 ],
 "respuesta_usuario": "Tengo costos fijos como de 200 al mes: renta de un rincon del taller de un amigo y las herramientas que voy comprando.",
 "candidatos_locales": [
  "preparar_contacto_clientes",
  "customer_discovery",
  "customer_discovery_phase2_problem_test",
  "global_vs_local_maximum"
 ],
 "prioridad_declarada": {
  "texto": "no saber si el precio que cobra de verdad le deja ganancia una vez que cuenta su tiempo",
  "conteo": 2
 }
}
```
```json
{
 "tipo": "decision_turno",
 "decision": {
  "accion": "avanzar",
  "camino": [
   "arquetipos_de_cliente"
  ],
  "es_salto": true
 },
 "nodo_actual": "punto_equilibrio_unidades",
 "razonamiento": "El usuario respondió que no ha hablado con clientes de forma organizada. Su siguiente paso no es calcular break-even (eso ya está claro: pierde dinero), sino entender quiénes compran y por qué. 'Arquetipos de Cliente' (afinidad 0.457) es más específico y urgente que los sucesores locales (decision_pivotar_o_proceder, customer_discovery genérico) porque trata exactamente de describir quién es el cliente que ya compra, paso previo a cualquier decisión sobre precio, demanda o pivote.",
 "saltos_posibles": [
  {
   "id": "social_ads_indirect_response",
   "titulo": "Publicidad en redes sociales con respuesta indirecta (Indirect Response)",
   "afinidad": 0.493,
   "fase_proyecto": "ejecucion",
   "condiciones_activacion": [
    "Cuando tu producto necesita que la gente lo entienda o confíe en ti antes de comprar",
    "Cuando ya tienes optimizada tu publicidad en buscadores y quieres ampliar por dónde te llegan clientes"
   ]
  },
  {
   "id": "eventos_offline_como_canal_traccion",
   "titulo": "Eventos presenciales para conseguir tus primeros clientes (canal de tracción)",
   "afinidad": 0.47,
   "fase_proyecto": "ejecucion",
   "condiciones_activacion": [
    "Si vendes a otras empresas o a un grupo de personas fácil de identificar",
    "Si otros canales digitales, como anuncios o buscadores, ya no te dan resultado"
   ]
  },
  {
   "id": "seleccion_plataforma_social_ads",
   "titulo": "Selección de Plataforma Social Según Audiencia y Objetivo",
   "afinidad": 0.463,
   "fase_proyecto": "ejecucion",
   "condiciones_activacion": [
    "Cuando el equipo debe decidir en qué red social invertir su presupuesto de ads"
   ]
  },
  {
   "id": "arquetipos_de_cliente",
   "titulo": "El retrato de tu cliente (arquetipo de cliente)",
   "afinidad": 0.457,
   "fase_proyecto": "validacion",
   "condiciones_activacion": [
    "Cuando ya explorastes a tus clientes pero todavia no tienes claro el perfil al que apuntas",
    "Si necesitas ordenar las prioridades de lo que vas a construir"
   ]
  },
  {
   "id": "enfoque_en_superfans",
   "titulo": "Enfócate en tu uno por ciento (los superfans)",
   "afinidad": 0.455,
   "fase_proyecto": "ejecucion",
   "condiciones_activacion": [
    "Cuando ya tienes una base de clientes y quieres que hablen más de ti",
    "Si tu presupuesto de marketing es limitado y necesitas decidir dónde poner primero tu esfuerzo"
   ]
  },
  {
   "id": "segmentos_de_clientes_problema_necesidad",
   "titulo": "Segmentos de Clientes: Problema, Necesidad o Pasión",
   "afinidad": 0.449,
   "fase_proyecto": "ideacion",
   "condiciones_activacion": [
    "Cuando no tienes claro quien toma la decisión de compra dentro del negocio de tu cliente",
    "Al definir la historia de usuario (user story) y la urgencia del problema que quieres resolver"
   ]
  },
  {
   "id": "herramientas_online_canal_fisico",
   "titulo": "Herramientas Online para Canales de Distribución Física",
   "afinidad": 0.447,
   "fase_proyecto": "ejecucion",
   "condiciones_activacion": [
    "Cuando el modelo de negocio depende principalmente de distribución física pero los clientes investigan online antes de comprar"
   ]
  },
  {
   "id": "scorecard_descubrimiento_cliente",
   "titulo": "Scorecard de Descubrimiento de Clientes",
   "afinidad": 0.443,
   "fase_proyecto": "validacion",
   "condiciones_activacion": [
    "Cuando necesitas distinguir entre los clientes entrevistados que muestran entusiasmo real y los que solo sienten curiosidad",
    "Cuando has completado múltiples entrevistas de descubrimiento y necesitas decidir sistemáticamente en qué clientes enfocar tus recursos"
   ]
  }
 ],
 "respuesta_usuario": "No he hablado con clientes de forma organizada, solo veo que la gente compra por Instagram, nunca les he preguntado directamente por que.",
 "candidatos_locales": [
  "decision_pivotar_o_proceder"
 ],
 "prioridad_declarada": {
  "texto": "no saber si el precio que cobra de verdad le deja ganancia una vez que cuenta su tiempo",
  "conteo": 2
 }
}
```
```json
{
 "tipo": "decision_turno",
 "decision": {
  "accion": "avanzar",
  "camino": [
   "eventos_offline_como_canal_traccion"
  ],
  "es_salto": true
 },
 "nodo_actual": "arquetipos_de_cliente",
 "razonamiento": "El usuario acaba de declarar su plan de acción concreto: ir a mercados presenciales para validar demanda. 'Eventos presenciales para conseguir tus primeros clientes' (afinidad 0.411 en saltos_posibles) es más específico que los sucesores locales porque trata exactamente cómo estructurar, ejecutar y aprender de un evento presencial, que es lo que está a punto de hacer. Este nodo tiene su propio marco metodológico sobre qué medir, cómo prepararse y cómo convertir la prueba en datos.",
 "saltos_posibles": [
  {
   "id": "publicidad_offline_pruebas_locales",
   "titulo": "Pruebas locales de publicidad fuera de internet",
   "afinidad": 0.477,
   "fase_proyecto": "ejecucion",
   "condiciones_activacion": [
    "Cuando tu producto apunta a mucha gente y lo offline tiene sentido para ti (por ejemplo, productos de consumo)",
    "Cuando los canales digitales ya no te alcanzan o están saturados"
   ]
  },
  {
   "id": "experimentacion_iterativa_mercado_fisico",
   "titulo": "Experimentación Iterativa en Mercados Físicos/Informales",
   "afinidad": 0.446,
   "fase_proyecto": "validacion",
   "condiciones_activacion": [
    "Cuando el negocio opera en mercados informales o físicos donde no aplican metodologías digitales estándar",
    "Cuando se busca validar demanda real de un servicio nuevo con mínima inversión"
   ]
  },
  {
   "id": "customer_discovery_get_out_of_building",
   "titulo": "Sal a Hablar con Clientes de Verdad (Customer Discovery)",
   "afinidad": 0.44,
   "fase_proyecto": "validacion",
   "condiciones_activacion": [
    "Cuando tienes un plan de negocio basado solo en tus propias suposiciones, sin validar",
    "Si todavia no has hablado con clientes reales"
   ]
  },
  {
   "id": "customer_validation_sell_phase",
   "titulo": "Sal a vender de verdad: valida con clientes reales",
   "afinidad": 0.429,
   "fase_proyecto": "validacion",
   "condiciones_activacion": [
    "Cuando ya tienes tu producto listo (tu primera versión o MVP) y necesitas comprobar con ventas reales si tu negocio funciona"
   ]
  },
  {
   "id": "meetups_bootstrapping_comunidad",
   "titulo": "Meetups para crecer con recursos mínimos (bootstrapping)",
   "afinidad": 0.414,
   "fase_proyecto": "ejecucion",
   "condiciones_activacion": [
    "Si tienes muy poco presupuesto para marketing",
    "Si quieres validar si hay interés en el mercado antes de crecer"
   ]
  },
  {
   "id": "eventos_offline_como_canal_traccion",
   "titulo": "Eventos presenciales para conseguir tus primeros clientes (canal de tracción)",
   "afinidad": 0.411,
   "fase_proyecto": "ejecucion",
   "condiciones_activacion": [
    "Si vendes a otras empresas o a un grupo de personas fácil de identificar",
    "Si otros canales digitales, como anuncios o buscadores, ya no te dan resultado"
   ]
  },
  {
   "id": "estrategia_ferias_comerciales",
   "titulo": "Estrategia de Ferias Comerciales (Trade Show Strategy)",
   "afinidad": 0.393,
   "fase_proyecto": "ejecucion",
   "condiciones_activacion": [
    "Cuando tu producto se dirige a un nicho industrial que se concentra en eventos presenciales.",
    "Cuando buscas acelerar acuerdos de distribución, prensa o alianzas estratégicas."
   ]
  },
  {
   "id": "get_out_building_test_sell",
   "titulo": "Vender de verdad para probar tu modelo de negocio (test selling)",
   "afinidad": 0.392,
   "fase_proyecto": "validacion",
   "condiciones_activacion": [
    "Cuando ya terminaste de hablar con clientes para entender el problema y ya identificaste a tus primeros clientes convencidos",
    "Si necesitas validar, todavia no escalar, tu modelo de negocio con pruebas reales de venta"
   ]
  }
 ],
 "respuesta_usuario": "Mi plan es ir a mercados locales de fin de semana para validar si la gente las compra en persona, no solo en redes.",
 "candidatos_locales": [
  "producto_minimo_viable",
  "dia_en_la_vida_del_cliente",
  "advocacy_customer_journey",
  "atributos_mercado_chopra_meindl",
  "community_building_estrategia",
  "construccion_tribu_de_marca"
 ],
 "prioridad_declarada": {
  "texto": "no saber si el precio que cobra de verdad le deja ganancia una vez que cuenta su tiempo",
  "conteo": 2
 }
}
```
```json
{
 "tipo": "decision_turno",
 "decision": {
  "accion": "generar_plan",
  "camino": [],
  "es_salto": false
 },
 "nodo_actual": "eventos_offline_como_canal_traccion",
 "razonamiento": "El usuario expresó 'sigamos con lo que sigue', indicando que quiere su plan final. Ha acumulado suficiente contexto y datos a lo largo de la sesión para que un plan sea viable y fundamentado.",
 "saltos_posibles": [
  {
   "id": "reset_total_de_expectativas",
   "titulo": "Si vas a comer mierda, no la mordisquees (Reset Total de Expectativas)",
   "afinidad": 0.381,
   "fase_proyecto": "ejecucion",
   "condiciones_activacion": [
    "Cuando tienes que revisar a la baja tus proyecciones ante quienes invirtieron en ti o ante el mercado",
    "Cuando hay riesgo de que tengas que hacer varios ajustes negativos seguidos"
   ]
  },
  {
   "id": "diamante_decision_tres_partes",
   "titulo": "Las tres partes de la reunión para decidir si tu proyecto sigue adelante (gate)",
   "afinidad": 0.362,
   "fase_proyecto": "ejecucion",
   "condiciones_activacion": [
    "Si sientes que te castigan injustamente por una decisión de prioridad.",
    "Si mezclas la calidad del trabajo con la decisión de negocio en la misma conversación."
   ]
  },
  {
   "id": "planificacion_consecuencias_no_intencionadas",
   "titulo": "Anticipar Consecuencias No Intencionadas en Sistemas Complejos",
   "afinidad": 0.36,
   "fase_proyecto": "planificacion",
   "condiciones_activacion": [
    "Si tu proyecto interviene en sistemas complejos, vivos o ecológicos.",
    "Si estás por escalar una solución tecnológica sin haber probado sus efectos colaterales."
   ]
  },
  {
   "id": "rendicion_de_cuentas_del_equipo",
   "titulo": "Responsabilidad y continuidad de tu proyecto de principio a fin (end to end)",
   "afinidad": 0.35,
   "fase_proyecto": "ejecucion",
   "condiciones_activacion": [
    "Cuando abandonas el proyecto apenas lo lanzas, sin darle seguimiento",
    "Cuando tus proyecciones iniciales suelen estar infladas para conseguir aprobacion"
   ]
  },
  {
   "id": "separar_hechos_de_percepcion",
   "titulo": "Separar los Hechos de la Percepción Buscando Otros Puntos de Vista",
   "afinidad": 0.34,
   "fase_proyecto": "ejecucion",
   "condiciones_activacion": [
    "Cuando tú o tu equipo interpretan una situación como catastrófica sin explorar alternativas",
    "Cuando los datos que tienes parecen apuntar a un único desenlace negativo"
   ]
  },
  {
   "id": "aceleracion_de_gates",
   "titulo": "Formas de Acelerar las Decisiones de Avanzar o Frenar (Gate)",
   "afinidad": 0.339,
   "fase_proyecto": "ejecucion",
   "condiciones_activacion": [
    "Si la espera entre etapas está retrasando la llegada de tu producto al mercado.",
    "Si trabajas con personas en distintos lugares y necesitas coordinarte a distancia."
   ]
  },
  {
   "id": "rediseno_tras_fracaso_proyecto",
   "titulo": "No Repetir el Mismo Enfoque tras un Fracaso de Proyecto",
   "afinidad": 0.335,
   "fase_proyecto": "ejecucion",
   "condiciones_activacion": [
    "Cuando un proyecto de sistema ha fracasado previamente y se plantea reiniciarlo"
   ]
  },
  {
   "id": "decision_consciente_de_crecimiento",
   "titulo": "El crecimiento como decisión consciente",
   "afinidad": 0.332,
   "fase_proyecto": "planificacion",
   "condiciones_activacion": [
    "Cuando tu negocio ya es rentable y estás pensando en expandirte",
    "Si todavía no has calculado los costos ocultos de contratar más gente"
   ]
  }
 ],
 "respuesta_usuario": "Si, tiene sentido, sigamos con lo que sigue.",
 "candidatos_locales": [
  "speaking_engagements_estrategia",
  "community_building_estrategia",
  "meetups_bootstrapping_comunidad",
  "canales_distribucion",
  "customer_retention_tactics"
 ],
 "prioridad_declarada": {
  "texto": "no saber si el precio que cobra de verdad le deja ganancia una vez que cuenta su tiempo",
  "conteo": 2
 }
}
```
```json
{
 "tipo": "numero_huerfano",
 "valor": "$130",
 "contexto": "u costo variable. Si vendes a $130 y produces a $102, ese margen"
}
```
```json
{
 "ruta": 10,
 "tipo": "cobertura_conceptos",
 "total": 35,
 "cosecha": 25
}
```
```json
{
 "tipo": "estimacion_banda",
 "total": 28,
 "con_banda": 28
}
```

## Juez de sesion (calidad)

```json
{
 "comentario": "La sesión avanzó de forma coherente desde estimación de costos hasta validación de demanda con datos reales; los saltos fueron justificados y el usuario llegó a su propia conclusión de que pierde dinero unitariamente, pero falta claridad sobre si probará aumentar precio o reducir costos antes de invertir en eventos presenciales.",
 "repeticion_detectada": false,
 "pertinencia_transiciones": 4,
 "señales_fuera_de_material": [
  "renta de un rincon del taller de un amigo",
  "voy comprando herramientas",
  "tengo otro trabajo"
 ]
}
```
