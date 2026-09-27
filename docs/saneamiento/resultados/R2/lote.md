# Pasada R2: nodos sin entrada tras mover nodos del nucleo a su mundo

### R2-01
- NODO SIN ENTRADA [cadena_suministro_respuesta_desastres]
    titulo: Cadenas de Suministro para Respuesta a Desastres | mundo: entrega
    resumen: Las cadenas de suministro de respuesta a desastres (DR) enfrentan alta imprevisibilidad y organización ad hoc, sin autoridad centralizada clara. A diferencia de las cadenas comerciales, requieren mayores niveles de inventario de contingencia (surge capacity), planificación pre-desastre, y entrenamiento colaborativo entre organizaciones diversas (gobierno, ONG, militares, empresas) que normalmente no trabajan juntas.
- CANDIDATOS A PREDECESOR (su mismo mundo)
  1. [plataforma_colaboracion_tiempo_real]
    titulo: Plataforma de Colaboración en Tiempo Real para Cadena de Suministro | mundo: entrega
    resumen: Una plataforma basada en la nube que ofrece visibilidad casi en tiempo real a todos los actores de la cadena de suministro (fabricantes, logística, distribuidores, retailers) permite que cada parte identifique problemas y actúe sin esperar instrucciones de una autoridad central. Se combina con sesiones de 'colaboración masiva' (crowdsourcing) donde múltiples empresas ajustan en vivo el diseño de la cadena, corren simulaciones, y llegan a consenso sobre el plan operativo, generando compromiso genuino de todas las partes.
  2. [crossdocking]
    titulo: Crossdocking en Centros de Distribución | mundo: entrega
    resumen: El crossdocking es una técnica logística en la que los envíos de carga completa llegan a un centro de distribución y se descargan, y al mismo tiempo se fragmentan y combinan con otros productos para cargarse directamente en camiones de salida, minimizando el almacenamiento. Reduce el tiempo de flujo del producto y los costos de manipulación, pero requiere alta coordinación entre entradas y salidas y volúmenes predecibles.
  3. [drum_buffer_rope]
    titulo: Modelo Drum-Buffer-Rope para Sincronizar la Cadena de Suministro | mundo: entrega
    resumen: Modelo que sincroniza toda la cadena de suministro como una sola entidad, alineada al ritmo real de la demanda del mercado (el 'tambor'). Cada empresa gestiona la incertidumbre mediante buffers de inventario o capacidad productiva, y comparten datos de demanda (la 'cuerda') que los mantiene sincronizados, minimizando el efecto látigo (bullwhip effect).
  4. [sistema_visibilidad_cadena_suministro_low_cost]
    titulo: Sistema de Visibilidad End-to-End con Componentes IT Simples | mundo: entrega
    resumen: Ante restricciones de tiempo y presupuesto, es posible construir un sistema de visibilidad de cadena de suministro combinando componentes IT básicos y accesibles (hojas de cálculo, archivos de texto, email, páginas web, bases de datos relacionales, scripts simples) en vez de comprar software costoso y complejo. La clave es identificar el patrón subyacente simple detrás de la aparente complejidad del problema (siguiendo la lógica de Sun Tzu: pocas notas, infinitas combinaciones) y usar esos componentes para crear una vista actualizada constantemente de inventario, producción y demanda, visible para todos los actores de la cadena.
  5. [simulacion_de_operaciones_supply_chain]
    titulo: Modelado de Simulación para Decisiones de Supply Chain | mundo: entrega
    resumen: La simulación permite crear un prototipo digital de una fábrica, almacén o red de suministro completa para probar diferentes condiciones antes de implementar cambios reales. Se aplica en tres horizontes: estratégico (1-5 años, ej. dónde construir una planta), táctico (1 mes-1 año, ej. gestión de incertidumbre de demanda) y operativo (1 día-1 mes, ej. layout de almacén). Permite detectar problemas de diseño antes de invertir, reducir stock de seguridad manteniendo el nivel de servicio, y evitar inversiones innecesarias mediante pruebas virtuales.
  6. [warehouse_management_system]
    titulo: Sistema de Gestión de Almacén (WMS) | mundo: entrega
    resumen: Los WMS soportan las operaciones diarias de almacén, gestionando niveles de inventario, ubicaciones de almacenamiento, y las actividades de picking, packing y envío para cumplir con las órdenes de los clientes de manera eficiente.
  7. [driver_transporte]
    titulo: Driver de Transporte: Selección de Modo según Valor del Producto | mundo: entrega
    resumen: El transporte mueve materiales y productos entre instalaciones. Existen seis modos básicos: barco y ferrocarril (bajo costo, lento), tuberías (eficiente pero limitado a líquidos/gases), camiones (flexible, costo variable), avión (rápido y costoso) y transporte electrónico (instantáneo pero limitado a datos/energía). Como regla general, productos de alto valor deben usar redes de transporte que prioricen capacidad de respuesta, y productos de bajo valor (commodities) deben usar redes que prioricen eficiencia. El transporte puede representar hasta un tercio del costo operativo de la cadena de suministro.
  8. [gestion_rationing_shortage_gaming]
    titulo: Gestión del Racionamiento y Shortage Gaming | mundo: entrega
    resumen: Cuando la demanda supera la oferta, los fabricantes racionan producto según pedidos recibidos, lo que incentiva a distribuidores a inflar artificialmente sus órdenes para recibir más asignación (shortage gaming). Esto distorsiona la demanda real percibida en toda la cadena de suministro.

### R2-02
- NODO SIN ENTRADA [calificacion_prospectos_marketing]
    titulo: Diseñar el Mensaje para Calificar y Descalificar Prospectos | mundo: franquicias
    resumen: Los compradores de franquicia buscan activamente razones para eliminar opciones de su lista corta (solo consideran entre 6 y 12 franquiciadores). El mensaje de marketing debe comunicar claramente los requisitos de inversión y perfil para autodescalificar a los no calificados antes de la llamada telefónica, ahorrando tiempo a ambas partes.
- CANDIDATOS A PREDECESOR (su mismo mundo)
  1. [segmentacion_perfil_franquiciado]
    titulo: Estrechamiento del Perfil de Comprador de Franquicia | mundo: franquicias
    resumen: Una de las formas más efectivas de mejorar el marketing de franquicias es reducir y precisar el perfil del prospecto objetivo. Un público objetivo demasiado amplio obliga a usar mensajes genéricos y a competir en medios saturados con muchas otras oportunidades de franquicia. Al narrowear el perfil, el mensaje se vuelve más específico y se pueden elegir medios menos saturados, mejorando la efectividad de la inversión en marketing. La investigación primaria (hablar con franquiciados de marcas similares, asociaciones de la industria, otros franquiciadores) complementa la intuición para definir este perfil.
  2. [mensaje_marketing_franquicia]
    titulo: Diseño del Mensaje de Marketing de Franquicia (Contenido y Emoción) | mundo: franquicias
    resumen: El mensaje de marketing de franquicia debe hablar a múltiples 'compradores' influyentes (el prospecto, su abogado, prestamista, contador, familia, buscadores web y reguladores estatales), no solo al interesado directo. Al mismo tiempo, la decisión de comprar una franquicia es altamente emocional, ligada a la identidad y el bienestar financiero del comprador, por lo que el mensaje debe combinar contenido racional de la oferta (propuesta de valor) con impacto emocional (aspiración, identidad, estilo de vida). Un error común es usar imágenes pensadas para atraer al consumidor final que en realidad asustan al franquiciado, como mostrar una tienda vacía sin clientes. Por eso los materiales deben revisarse desde la óptica del comprador de la franquicia y cuidar su calidad para transmitir seriedad.
  3. [rechazo_gentil_prospecto]
    titulo: Rechazar Prospectos No Calificados con Delicadeza | mundo: franquicias
    resumen: Cuando un prospecto no cumple los requisitos financieros u otros criterios, tu le comunicas el rechazo de forma profesional y empatica, poniendo por delante el exito de la persona como franquiciado, y le ofreces alternativas cuando existan, como buscar un inversionista o esperar y ahorrar mas.
  4. [proceso_llamada_inicial_venta]
    titulo: Proceso de la Primera Llamada de Ventas | mundo: franquicias
    resumen: La venta de franquicias es un cortejo, no una venta rápida. Los mejores vendedores escuchan más de lo que hablan en la primera llamada, evitando abrumar al prospecto con información. La llamada inicial sigue una agenda estructurada: obtener datos de contacto, calificar financieramente, calificar por otros criterios, determinar urgencia y motivos, entender el proceso de compra del candidato y posicionar frente a competidores, dar una visión general, explicar próximos pasos y pedir un avance (advance).
  5. [estrategia_marca_segun_tamano]
    titulo: Adaptar la Estrategia de Mensaje Según el Tamaño y Reconocimiento de la Marca | mundo: franquicias
    resumen: No todos los prospectos buscan marcas reconocidas; algunos prefieren oportunidades de 'planta baja'. Un franquiciador pequeño no debe intentar aparentar ser grande, sino destacar su naturaleza emprendedora y de oportunidad temprana si eso es lo que atrae a su público.
  6. [las_cuatro_ventas_franquicia]
    titulo: Las Cuatro Ventas de la Franquicia | mundo: franquicias
    resumen: Al vender una franquicia, el vendedor debe lograr cuatro ventas separadas en la mente del prospecto: (1) decidir emprender un negocio propio, (2) decidir entrar en esa industria específica, (3) decidir franquiciar en vez de hacerlo solo, y (4) decidir comprar esta franquicia en particular (vs. la competencia). Cada venta requiere un mensaje distinto y debe entenderse para diseñar materiales de marketing efectivos.
  7. [motivaciones_reales_franquiciado]
    titulo: Comprender las Motivaciones Reales del Franquiciado | mundo: franquicias
    resumen: Contrario a la creencia común, los compradores de franquicia no están motivados principalmente por el retorno financiero, sino por independencia, ser su propio jefe, flexibilidad y control de su destino. Entender estas motivaciones (evitando sesgos al encuestar solo a franquiciados actuales) permite crear mensajes más efectivos.
  8. [presupuesto_marketing_leads_franquicia]
    titulo: Presupuesto de marketing para atraer candidatos a franquicia (leads) | mundo: franquicias
    resumen: Conseguir contactos interesados (leads) calificados es esencial y cuesta dinero: pregunta en tu mercado cuánto necesitas presupuestar por cada franquicia que quieras vender en el año. Como el proceso de venta de una franquicia toma entre 12 y 14 semanas, y las ventas no llegan de forma pareja sino que se concentran hacia la mitad del período (como una curva de campana), tienes que dejar preparado el flujo de caja para varios meses de publicidad antes de recuperar las cuotas de entrada.

### R2-03
- NODO SIN ENTRADA [efecto_bullwhip]
    titulo: Detectar y calcular el costo del efecto látigo en tu cadena de suministro | mundo: compras
    resumen: El efecto látigo (bullwhip) pasa cuando un cambio pequeño en lo que pide el cliente final se va agrandando a medida que sube por tu cadena de proveedores, y cada eslabón termina con una idea distinta de cuánta demanda real hay. Primero te quedas corto de inventario, después te sobra. Antes de gastar en resolverlo, tienes que medir qué tan grande es el efecto en tu caso y calcular cuánto te cuesta en producción, transporte, inventario y ventas que pierdes por no tener producto.
- CANDIDATOS A PREDECESOR (su mismo mundo)
  1. [diagnostico_efecto_latigo]
    titulo: Diagnóstico del Efecto Látigo (Bullwhip Effect) | mundo: compras
    resumen: El efecto látigo describe cómo pequeños cambios en la demanda del consumidor final se amplifican en oscilaciones cada vez mayores conforme se transmiten hacia atrás en la cadena de suministro (minorista, distribuidor, fabricante), generando ciclos de escasez y luego exceso de inventario. Fue ilustrado con el 'beer game' del MIT y documentado por Peter Senge. Provoca sobrecostos en producción, inventario, transporte y mano de obra, además de pérdida de ventas.
  2. [colaboracion_cadena_suministro]
    titulo: Iniciar la Colaboración en la Cadena de Suministro | mundo: compras
    resumen: El primer paso para reducir el efecto látigo es medirlo dentro de la propia empresa, comparando el volumen y frecuencia de pedidos recibidos de clientes contra los pedidos realizados a proveedores. Compartir datos de inventario y demanda con socios comerciales (como hacen Walmart, Dell y P&G) permite decisiones más eficientes en toda la cadena, en lugar de que cada empresa optimice de forma aislada.
  3. [compartir_datos_cadena_suministro]
    titulo: Compartición de Datos entre Empresas de la Cadena de Suministro | mundo: compras
    resumen: Compartir datos de demanda, decisiones y métricas de desempeño entre las empresas de una cadena de suministro mejora la toma de decisiones colectiva y reduce distorsiones como el efecto látigo (bullwhip effect). Aunque existe reticencia por temor a filtrar información confidencial a competidores, las cadenas que colaboran eficientemente ganan cuota de mercado frente a las que no lo hacen, ya que la competencia se traslada de empresa-contra-empresa a cadena-de-suministro-contra-cadena-de-suministro.
  4. [calcula_costo_de_mantener_contra_costo_de_reponer]
    titulo: Calcula cuánto te cuesta guardar stock contra cuánto te cuesta reponerlo | mundo: compras
    resumen: Cada producto guardado te cuesta dinero solo por estar ahi: espacio, seguro, deterioro y el efectivo que tienes inmovilizado en el. A esto se le llama costo de mantener. Cada pedido que haces tambien te cuesta tiempo y esfuerzo en armarlo, negociarlo y recibirlo: es el costo de reponer. Si compras poco y muy seguido, el costo de reponer se dispara. Si compras mucho de una vez, el costo de mantener se dispara. El punto optimo esta en el equilibrio entre ambos: ni tanto stock que se te muera en la bodega, ni tan poco que compres todos los dias. Calcula cuanto te cuesta cada peso de inventario guardado por año y usa ese numero para decidir cuanto pedir cada vez que reabastezcas.
  5. [conoce_insumos_vitales]
    titulo: Conoce tus insumos vitales | mundo: compras
    resumen: No todos los insumos que compras pesan igual. Algunos representan mucho dinero invertido pero se consiguen facilmente en cualquier lado. Otros cuestan poco pero si faltan, tu negocio se detiene por completo porque no hay sustituto rapido ni proveedor alterno cercano. Confundir estas dos cosas lleva a errores comunes: vigilar de cerca un insumo barato y facil de reponer, mientras un insumo critico y economico se queda sin control hasta que un dia falta y detiene tu operacion. Distinguir lo que representa mayor gasto de lo que realmente te deja parado si no lo tienes te permite decidir a que insumos ponerles mas atencion, mas stock de seguridad, o mas de un proveedor disponible por si el habitual te falla.
  6. [define_punto_maximo_de_stock]
    titulo: Define tu punto máximo de stock y cada cuánto lo revisas | mundo: compras
    resumen: Para no quedarte sin producto ni acumular de más, conviene fijar un punto de reorden: la cantidad mínima con la que todavía puedes esperar a que llegue el próximo pedido sin quedarte a cero. Ese punto se calcula combinando cuánto vendes por semana, cuánto tarda tu proveedor en entregar, y un colchón extra por si hay retrasos o defectos. A partir de ahí también puedes fijar un máximo: cuánto quieres tener en total antes de dejar de pedir más. Estos números no son fijos para siempre: cambian si tu ritmo de ventas cambia o si tu proveedor modifica sus tiempos de entrega, así que conviene revisarlos cada vez que eso ocurra.
  7. [gestion_procurement_consumo]
    titulo: Cuánto y qué compras en tu negocio (procurement) | mundo: compras
    resumen: Antes de negociar con tus proveedores, necesitas entender cuánto y qué compras en todo tu negocio. Define cuánto esperas consumir de cada categoría de producto y en cada lugar donde operas, y compara eso regularmente con lo que realmente consumes para detectar desviaciones que te avisen de problemas u oportunidades.
  8. [clasifica_tu_inventario]
    titulo: Clasifica tu inventario y define qué meta persigues | mundo: compras
    resumen: No todo lo que tienes guardado sirve para lo mismo. Hay mercaderia lista para vender, insumos para producir, piezas de repuesto para reparar algo que ya vendiste, consumibles de operacion diaria, y reserva de seguridad para cubrir imprevistos. Mezclar estas categorias sin distincion hace que sea imposible saber si tu inventario esta bien dimensionado o si es dinero inmovilizado sin motivo. Antes de decidir cuanto comprar o cuando reponer, separa lo que tienes segun su funcion real y define una meta concreta para ti mismo: cuantos dias de stock quieres mantener, cuantas veces al ano quieres rotar el inventario, o que nivel de disponibilidad le quieres garantizar a tus clientes. Sin esa meta escrita, cualquier decision de compra es a ciegas.

### R2-04
- NODO SIN ENTRADA [modelado_simulacion_cadena_suministro]
    titulo: Modelado y Simulación de Cadena de Suministro con Cuatro Entidades | mundo: entrega
    resumen: Cualquier cadena de suministro puede modelarse definiendo cuatro tipos de entidades: Productos (costo, peso, volumen), Instalaciones (ubicación, costos operativos, tasas de producción/demanda), Vehículos (velocidad, capacidad, costos, rutas) y Rutas (destinos, distancias, frecuencias). Usando mapas digitales (Google Maps, etc.) estas entidades se colocan geográficamente y se simulan interacciones para detectar problemas de desempeño antes de implementarlos en la realidad, reduciendo riesgo y costo de errores.
- CANDIDATOS A PREDECESOR (su mismo mundo)
  1. [simulacion_de_operaciones_supply_chain]
    titulo: Modelado de Simulación para Decisiones de Supply Chain | mundo: entrega
    resumen: La simulación permite crear un prototipo digital de una fábrica, almacén o red de suministro completa para probar diferentes condiciones antes de implementar cambios reales. Se aplica en tres horizontes: estratégico (1-5 años, ej. dónde construir una planta), táctico (1 mes-1 año, ej. gestión de incertidumbre de demanda) y operativo (1 día-1 mes, ej. layout de almacén). Permite detectar problemas de diseño antes de invertir, reducir stock de seguridad manteniendo el nivel de servicio, y evitar inversiones innecesarias mediante pruebas virtuales.
  2. [modelo_simulacion_cadena_suministro_circular]
    titulo: Simulación de Cadenas de Suministro Circulares y Sostenibles | mundo: entrega
    resumen: Antes de implementar una cadena de suministro física, es posible construir un modelo de simulación compuesto por entidades clave (productos, instalaciones, vehículos, rutas) para probar diferentes escenarios de oferta, demanda, costos y ubicaciones. Esto permite generar reportes de P&L y KPIs que sirven de base objetiva para comparar diseños alternativos antes de invertir capital, especialmente relevante en cadenas de suministro circulares (como recolección de aceite usado para biodiesel) donde el impacto ambiental y la eficiencia económica deben equilibrarse.
  3. [driver_transporte]
    titulo: Driver de Transporte: Selección de Modo según Valor del Producto | mundo: entrega
    resumen: El transporte mueve materiales y productos entre instalaciones. Existen seis modos básicos: barco y ferrocarril (bajo costo, lento), tuberías (eficiente pero limitado a líquidos/gases), camiones (flexible, costo variable), avión (rápido y costoso) y transporte electrónico (instantáneo pero limitado a datos/energía). Como regla general, productos de alto valor deben usar redes de transporte que prioricen capacidad de respuesta, y productos de bajo valor (commodities) deben usar redes que prioricen eficiencia. El transporte puede representar hasta un tercio del costo operativo de la cadena de suministro.
  4. [drum_buffer_rope]
    titulo: Modelo Drum-Buffer-Rope para Sincronizar la Cadena de Suministro | mundo: entrega
    resumen: Modelo que sincroniza toda la cadena de suministro como una sola entidad, alineada al ritmo real de la demanda del mercado (el 'tambor'). Cada empresa gestiona la incertidumbre mediante buffers de inventario o capacidad productiva, y comparten datos de demanda (la 'cuerda') que los mantiene sincronizados, minimizando el efecto látigo (bullwhip effect).
  5. [programacion_entregas_delivery_scheduling]
    titulo: Programación de Entregas: Directas vs. Milk Run | mundo: entrega
    resumen: Existen dos métodos principales de entrega: las entregas directas (de un origen a un destino, simples pero eficientes solo cuando el EOQ del receptor coincide con la carga de transporte completa) y las entregas milk run (de un origen a múltiples destinos o viceversa, más complejas de programar pero más eficientes en el uso del transporte y menor costo de recepción cuando las cantidades individuales son menores a una carga completa). La elección depende de la relación entre el EOQ de cada ubicación receptora y la capacidad del modo de transporte.
  6. [tecnologias_emergentes_cadena_suministro]
    titulo: Combinación de Tecnologías Emergentes para Cadenas Ágiles | mundo: entrega
    resumen: El verdadero potencial de tecnologías como robots industriales, manufactura aditiva (impresión 3D), vehículos autónomos, drones e IoT se logra cuando se combinan entre sí, no usándolas aisladamente. Empresas como Walmart y Amazon lograron ventajas competitivas dominantes al combinar prácticas logísticas complementarias. La combinación de estas tecnologías permite fábricas flexibles que ajustan rápidamente su producción, almacenes automatizados y entregas más precisas y rápidas.
  7. [ia_en_supply_chain]
    titulo: Inteligencia Artificial Aplicada a la Cadena de Suministro | mundo: entrega
    resumen: La IA, potenciada por machine learning y modelos de lenguaje grandes (LLMs), te permite encontrar patrones en grandes volúmenes de datos y convertirlos en decisiones accionables en tiempo real. Transforma tres áreas clave: pronóstico de demanda (analizando históricos, tendencias de mercado y factores externos como clima o eventos sociales), optimización de rutas (con datos de tráfico en tiempo real para rutas dinámicas) y operaciones de almacén (automatización y visión computacional para manipular productos de formas variables). El objetivo no es reemplazar tu juicio sino complementarlo: la IA procesa el volumen de datos que a ti te resulta inmanejable desde el teléfono, y tú decides qué hacer con esas señales para ganar ventaja competitiva frente a métodos tradicionales que ya no alcanzan.
  8. [iot_big_data_supply_chain]
    titulo: IoT y Big Data para Trazabilidad de Supply Chain | mundo: entrega
    resumen: El Internet de las Cosas (IoT) conecta dispositivos embebidos en productos y equipos para enviar y recibir datos en tiempo real, generando volúmenes masivos de 'big data' que alimentan el análisis de patrones y tendencias en la cadena de suministro. Esta evolución va desde códigos de barras, pasando por RFID, hasta microchips embebidos en cualquier producto, permitiendo un seguimiento continuo y granular del movimiento de mercancías.

### R2-05
- NODO SIN ENTRADA [risk_audit]
    titulo: Auditoría de Riesgos | mundo: risk_management
    resumen: La Auditoría de Riesgos evalúa la efectividad del proceso de identificación de riesgos, las respuestas implementadas y el proceso general de gestión de riesgos. Se revisan los eventos de riesgo ocurridos, sus causas, las respuestas aplicadas y su éxito, así como el cumplimiento del proceso de gestión de riesgos y las herramientas utilizadas, identificando buenas prácticas y áreas de mejora.
- CANDIDATOS A PREDECESOR (su mismo mundo)
  1. [evaluacion_gestion_riesgos]
    titulo: Evaluación y Gestión de Riesgos | mundo: risk_management
    resumen: Proceso estructurado para identificar riesgos potenciales, evaluar su severidad y probabilidad, y definir acciones concretas para minimizarlos o eliminarlos. Incluye el análisis de consecuencias de actuar o no actuar, el impacto futuro de las decisiones, y el balance costo/beneficio. El objetivo final no es solo evaluar sino generar una lista de acciones ejecutables con responsables y fechas.
  2. [identificacion_de_riesgos]
    titulo: Identificación de Riesgos | mundo: risk_management
    resumen: Un riesgo es cualquier cosa que puede salir mal y resultar en una pérdida. Antes de gestionar o mitigar riesgos es indispensable identificarlos de forma sistemática, porque suelen permanecer invisibles mientras las condiciones son favorables y solo se manifiestan bajo condiciones adversas. El primer paso es reunir conocimiento amplio sobre tu negocio, sus sistemas, personas y procesos, y examinar de forma crítica qué puede fallar en cada uno. Usa el sombrero negro de los Seis Sombreros de pensar para cuestionar cada respuesta y evitar quedarte solo con lo obvio. Revisar fallas pasadas ayuda a completar la lista. El resultado debe documentarse por completo antes de pasar a evaluar la probabilidad o el impacto de cada riesgo.
  3. [revisa_tus_riesgos_con_un_ritmo]
    titulo: Procedimientos de Monitoreo del Riesgo | mundo: risk_management
    resumen: Vigilar tus riesgos no puede ser algo que haces cuando te sobra tiempo: necesita un ritmo fijo. La frecuencia sana depende de la gravedad y del movimiento del proyecto: los riesgos graves o los momentos intensos piden revisión frecuente, hasta semanal o diaria; los tranquilos, una mirada mensual basta. La idea no es reunirte a contemplar la lista, sino detectar a tiempo cualquier desviación de lo normal y decidir si actúas. Para el emprendedor solo, poner en la agenda un momento fijo de revisión, con una frecuencia acorde a lo que está en juego, es lo que convierte la gestión de riesgo de una buena intención en un hábito real.
  4. [evaluacion_de_factores_de_riesgo]
    titulo: Evaluación de Factores de Riesgo (Severidad, Probabilidad y más) | mundo: risk_management
    resumen: Cuando identificas varios riesgos, conviene ordenarlos para saber cuál atacar primero. Para eso, revisas cada uno según su gravedad, qué tan probable es que ocurra, qué tan rápido golpearía, cuánto indignaría a tus clientes, su complejidad, su alcance y cuánta incertidumbre tiene. Combinando estos factores obtienes una lista clara de prioridades para enfocar tu esfuerzo de prevención.
  5. [manten_viva_tu_lista_de_riesgos]
    titulo: El Registro de Riesgos como Documento Vivo | mundo: risk_management
    resumen: Tu lista de riesgos no vale por lo que escribiste al inicio, sino por si sigue reflejando lo que de verdad puede pasarte. Un riesgo se cierra cuando ya no puede afectarte, no cuando te cansaste de mirarlo o el plazo que le pusiste venció. Mientras el proyecto avanza, algunos riesgos que anotaste como pequeños crecen sin que te des cuenta, y aparecen otros que ni existían cuando armaste la lista por primera vez. Una lista congelada te da la sensación de que tienes todo bajo control, y eso es más peligroso que no tener lista: te confías justo donde deberías estar mirando con más atención.
  6. [tu_gestion_de_riesgo_funciona]
    titulo: Auditar y Mejorar el Método de Riesgo | mundo: risk_management
    resumen: Tu forma de manejar el riesgo también hay que auditarla y mejorarla, o se vuelve un rito que da calma sin servir. Auditar es preguntar sin piedad: mi método reduce las sorpresas de verdad, o solo produce papeles y tranquilidad. La única forma seria de saberlo es comparar lo que predijiste con lo que pasó, a lo largo del tiempo. Y mejorar es ajustar el método ciclo a ciclo: soltar lo que no atinó, reforzar lo que sí, calibrar mejor tu juicio. Ningún método nace perfecto; el bueno es el que aprende de su propio historial. Para el emprendedor, mirar su gestión de riesgo con el mismo ojo crítico con que mira su negocio es lo que la mantiene honesta y afilada, en vez de convertirse en una superstición reconfortante.
  7. [haz_tu_lista_de_lo_que_puede_fallar]
    titulo: El Censo de Riesgos | mundo: risk_management
    resumen: Ya sabes cómo se registra un riesgo: con su identificador, su descripción, su causa y su efecto, su probabilidad y gravedad, su respuesta y su responsable. Lo que falta es cómo se llena esa lista la primera vez sin quedarte corto. Se hace con una sesión honesta donde nombras, sin filtro, todo lo que podría hundir o frenar tu proyecto, incluso lo que te da vergüenza decir en voz alta. Después viene el criterio: no todo lo que nombraste merece una respuesta activa. Algunos riesgos los vas a trabajar ya, otros los vas a soltar por ahora porque son improbables o su efecto es menor. El valor no está en la lista que sale de esa primera sesión, sino en aprender a distinguir qué entra al registro y qué se queda fuera sin culpa.
  8. [vuelve_a_medir_despues_del_susto]
    titulo: Reevaluación del Riesgo Tratado | mundo: risk_management
    resumen: Después de actuar sobre un riesgo, o después de que un susto lo cambió, hay que volver a medirlo: la foto vieja ya no sirve. Cuando aplicaste una respuesta, la pregunta es si de verdad funcionó, es decir, si el riesgo quedó tan bajo como querías o si sigue igual de peligroso y hace falta más. Y cuando un riesgo se materializó o el entorno cambió, su probabilidad y su impacto ya no son los de antes. Reevaluar cierra el ciclo: comparas el riesgo tratado contra tu criterio y decides si lo das por controlado o le das otra vuelta. Para el emprendedor solo, este paso evita dos errores: creer que un riesgo está resuelto cuando tu respuesta no sirvió, y seguir temiendo un riesgo que en realidad ya bajó.
