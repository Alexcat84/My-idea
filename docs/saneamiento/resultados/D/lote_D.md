# Pasada D: 39 nodos, el nucleo o su mundo

### D-01
- mundo propuesto: entrega (logistica y entrega (empaque, envio, inventario, transporte, devoluciones))
- titulo: Sistema de Gestión de Almacén (WMS)
- resumen: Los WMS soportan las operaciones diarias de almacén, gestionando niveles de inventario, ubicaciones de almacenamiento, y las actividades de picking, packing y envío para cumplir con las órdenes de los clientes de manera eficiente.
- pasos:
  1. Mapear el flujo físico actual de productos en el almacén
  2. Definir ubicaciones y niveles de inventario a rastrear en el sistema
  3. Automatizar procesos de picking, packing y shipping
  4. Integrar el WMS con robots o vehículos automatizados si aplica
- entregable: WMS implementado y operando con seguimiento de inventario en tiempo real

### D-02
- mundo propuesto: entrega (logistica y entrega (empaque, envio, inventario, transporte, devoluciones))
- titulo: Modelo Drum-Buffer-Rope para Sincronizar la Cadena de Suministro
- resumen: Modelo que sincroniza toda la cadena de suministro como una sola entidad, alineada al ritmo real de la demanda del mercado (el 'tambor'). Cada empresa gestiona la incertidumbre mediante buffers de inventario o capacidad productiva, y comparten datos de demanda (la 'cuerda') que los mantiene sincronizados, minimizando el efecto látigo (bullwhip effect).
- pasos:
  1. Identificar la demanda del mercado como el 'tambor' que marca el ritmo de toda la cadena
  2. Determinar buffers de inventario o capacidad en cada eslabón según el nivel de incertidumbre
  3. Compartir datos de demanda real (ventas POS) entre los participantes de la cadena para reducir la incertidumbre
  4. Monitorear la reducción de las olas de demanda (bullwhip effect) tras la sincronización
- entregable: Diagrama de flujo de inventario sincronizado con buffers definidos y acuerdo de intercambio de datos de demanda

### D-03
- mundo propuesto: entrega (logistica y entrega (empaque, envio, inventario, transporte, devoluciones))
- titulo: Estandarización de Identificación de Producto (GTIN/EPC)
- resumen: Para que la información de productos sea utilizable globalmente, se requiere un protocolo de identificación estándar. GS1 unificó los sistemas UPC y EAN en el Global Trade Item Number (GTIN), y lo extendió con el Electronic Product Code (EPC), que añade un número de serie único a cada ítem individual, permitiendo rastrear su historial de movimiento a través de la red EPCglobal.
- pasos:
  1. Registrar la organización en GS1 para obtener un código de gestor (manager code)
  2. Etiquetar los productos con GTIN/EPC usando el esquema unificado de 14 digitos (el 'UPC de 14 digitos' en Norteamerica o el 'EAN de 13 digitos mas digito de control' en Europa)
  3. Integrar los sistemas internos con la red EPCglobal para consulta y actualización en tiempo real
  4. Mantener actualizada la base de datos de códigos EPC conforme los productos se mueven en la cadena
- entregable: Catálogo de productos codificado bajo estándar GTIN/EPC, registrado en GS1

### D-04
- mundo propuesto: entrega (logistica y entrega (empaque, envio, inventario, transporte, devoluciones))
- titulo: Elegir resistencia de caja según peso del contenido
- resumen: No toda caja de cartón aguanta lo mismo: la resistencia depende del grosor, si es de pared simple o doble, y de dos pruebas que los fabricantes imprimen en la caja, una que mide cuánta fuerza aguanta antes de romperse por un golpe y otra que mide cuánto peso soporta apilada de canto. Cuanto más pesado o delicado el contenido, más resistencia necesitas: lo liviano puede ir en pared simple, lo pesado o frágil pide pared doble o incluso triple. Usar una caja por debajo de su capacidad real termina en cajas que se aplastan o revientan en tránsito, mientras que sobredimensionar la resistencia solo cuesta dinero de más sin necesidad real. La clave es mirar el sello del fabricante en la caja y hacerlo coincidir con el peso real de lo que va adentro.
- pasos:
  1. Pesa el contenido completo, incluyendo el relleno que vas a usar.
  2. Busca el sello del fabricante en la caja: te dice su resistencia y tipo de pared.
  3. Si tu contenido pesa cerca del límite de una pared simple, sube a pared doble.
  4. Pregunta a tu proveedor de cajas cuál es el límite de peso exacto para cada tipo que vende.
  5. Nunca reutilices una caja que ya perdió rigidez, aunque el peso a enviar sea bajo.
- entregable: Una tabla propia de peso del pedido y el tipo de caja a usar, según lo que ofrece tu proveedor local.

### D-05
- mundo propuesto: risk_management (gestion de riesgos)
- titulo: Las Cuatro Etapas del Pensamiento Creativo (Wallas)
- resumen: Todo proceso de pensamiento creativo o resolución de problemas, sea científico, artístico o de negocios, atraviesa cuatro etapas que no son estrictamente lineales y pueden solaparse cuando trabajas en varios problemas a la vez. Preparación: investigas el problema en profundidad y de forma consciente, reuniendo toda la información relevante. Incubación: dejas de pensar conscientemente en el problema mientras descansas o haces otra cosa, pero el trabajo mental inconsciente sigue activo. Iluminación: aparece de golpe la idea o solución feliz, a menudo precedida por señales sutiles de que algo se está formando, llamadas intimación. Verificación: sometes la idea a un análisis lógico riguroso y a pruebas antes de implementarla. Este modelo es la base histórica de casi todos los procesos modernos de pensamiento de diseño e ideación.
- pasos:
  1. Preparación: define claramente el problema e investígalo a fondo, reuniendo toda la información relevante posible
  2. Incubación: aléjate deliberadamente del problema (duerme, camina, trabaja en otra cosa) sin forzar conscientemente una solución, creando condiciones de silencio, actividad relajada
  3. Lleva contigo una libreta o notas de voz para capturar cualquier señal sutil de que una idea se está formando, o el momento en que llega completa, como indicio de Intimación
  4. Iluminación: cuando llegue el destello de la idea, captúralo de inmediato sin filtrarlo con crítica
  5. Verificación: somete la idea capturada a un análisis lógico riguroso y a pruebas antes de implementarla
  6. Sugerencia de My Idea: anota en qué etapa se encuentra cada idea que estés trabajando, preparación, incubación, iluminación o verificación, para no perder el hilo.
- entregable: Una bitácora del proceso creativo, con notas de preparación, incubación e iluminación, y una idea validada lógicamente lista para pasar a prototipado.

### D-06
- mundo propuesto: compras (compras y proveedores (elegir, negociar y gestionar proveedores y contratos de compra))
- titulo: Auditoría de Adquisiciones
- resumen: La Auditoría de Adquisiciones es una revisión de los contratos y procesos de contratación para verificar su completitud, precisión y efectividad. Evalúa el desempeño del proveedor (alcance, calidad, cronograma, costo, facilidad de trabajo) y el proceso de gestión de adquisiciones en sí, generando información útil para mejorar contratos futuros y alimentar las Lecciones Aprendidas.
- pasos:
  1. Revisar el desempeño del proveedor en alcance, calidad, cronograma y costo
  2. Evaluar la facilidad de trabajo con el proveedor
  3. Auditar el proceso de gestión de adquisiciones y las herramientas utilizadas
  4. Documentar buenas prácticas y áreas de mejora
  5. Combinar hallazgos con el Cierre de Contrato si corresponde
- entregable: Informe de Auditoría de Adquisiciones con evaluación del proveedor y del proceso

### D-07
- mundo propuesto: entrega (logistica y entrega (empaque, envio, inventario, transporte, devoluciones))
- titulo: Driver de Transporte: Selección de Modo según Valor del Producto
- resumen: El transporte mueve materiales y productos entre instalaciones. Existen seis modos básicos: barco y ferrocarril (bajo costo, lento), tuberías (eficiente pero limitado a líquidos/gases), camiones (flexible, costo variable), avión (rápido y costoso) y transporte electrónico (instantáneo pero limitado a datos/energía). Como regla general, productos de alto valor deben usar redes de transporte que prioricen capacidad de respuesta, y productos de bajo valor (commodities) deben usar redes que prioricen eficiencia. El transporte puede representar hasta un tercio del costo operativo de la cadena de suministro.
- pasos:
  1. Clasificar los productos según su valor y su sensibilidad al tiempo de entrega.
  2. Seleccionar el modo de transporte (barco, ferrocarril, tubería, camión, avión, electrónico) según esa clasificación.
  3. Diseñar rutas y redes de transporte que conecten instalaciones de forma óptima.
  4. Revisar periódicamente el costo de transporte como porcentaje del costo operativo total.
- entregable: Matriz de decisión de modo de transporte por línea de producto, junto con el diseño de rutas y red logística.

### D-08
- mundo propuesto: entrega (logistica y entrega (empaque, envio, inventario, transporte, devoluciones))
- titulo: Programación de Entregas: Directas vs. Milk Run
- resumen: Existen dos métodos principales de entrega: las entregas directas (de un origen a un destino, simples pero eficientes solo cuando el EOQ del receptor coincide con la carga de transporte completa) y las entregas milk run (de un origen a múltiples destinos o viceversa, más complejas de programar pero más eficientes en el uso del transporte y menor costo de recepción cuando las cantidades individuales son menores a una carga completa). La elección depende de la relación entre el EOQ de cada ubicación receptora y la capacidad del modo de transporte.
- pasos:
  1. Evaluar si el EOQ de cada ubicación receptora coincide con cargas completas de transporte
  2. Si coincide, implementar entregas directas por su simplicidad
  3. Si no coincide, diseñar rutas milk run combinando pedidos
  4. Seleccionar técnica de ruteo: matriz de ahorros (savings matrix) para múltiples restricciones o técnica de asignación generalizada cuando la única restricción es capacidad del vehículo
  5. Decidir entre entregas desde ubicaciones de producto único o desde centros de distribución
  6. Diseñar la secuencia de recogidas/entregas y validar con software de ruteo
  7. Medir el ahorro en costo de transporte y recepción tras implementar la ruta consolidada
- entregable: Plan de logística de entregas con método seleccionado (directo/milk run) y rutas optimizadas

### D-09
- mundo propuesto: compras (compras y proveedores (elegir, negociar y gestionar proveedores y contratos de compra))
- titulo: Habilitadores Clave para la Colaboración en Supply Chain
- resumen: Para que las iniciativas colaborativas tengan éxito se requieren habilitadores humanos y tecnológicos: interés común, apertura, reconocimiento de prioridades, expectativas claras, liderazgo, cooperación (no castigo), confianza, reparto de beneficios y TI avanzada. Sin estos elementos, la colaboración fracasa ante los obstáculos naturales del negocio tradicional.
- pasos:
  1. Evaluar si existe un interés común genuino entre todas las partes
  2. Fomentar la apertura en el intercambio de información, respetando normas antitrust
  3. Designar un líder o champion que impulse la colaboración
  4. Establecer un sistema de reparto de beneficios (ej. scorecard compartido)
  5. Invertir en TI avanzada para habilitar transferencia de datos en tiempo real
- entregable: Checklist de habilitadores presentes/ausentes y plan de acción para fortalecer los débiles

### D-10
- mundo propuesto: compras (compras y proveedores (elegir, negociar y gestionar proveedores y contratos de compra))
- titulo: Cuánto y qué compras en tu negocio (procurement)
- resumen: Antes de negociar con tus proveedores, necesitas entender cuánto y qué compras en todo tu negocio. Define cuánto esperas consumir de cada categoría de producto y en cada lugar donde operas, y compara eso regularmente con lo que realmente consumes para detectar desviaciones que te avisen de problemas u oportunidades.
- pasos:
  1. Clasifica lo que compras en materiales estratégicos y compras indirectas (MRO)
  2. Define cuánto esperas consumir de cada producto en cada lugar donde operas
  3. Compara periódicamente lo que consumes realmente contra lo esperado
  4. Investiga las causas cuando encuentres desviaciones grandes, ya sea por encima o por debajo de lo esperado
  5. Ajusta tus expectativas o corrige el proceso según lo que encuentres
- entregable: Un reporte de tu consumo por categoría de producto y lugar de operación, con el análisis de las desviaciones.

### D-11
- mundo propuesto: entrega (logistica y entrega (empaque, envio, inventario, transporte, devoluciones))
- titulo: Scorecard de Desempeño y Bucle de Retroalimentación Autocorrectivo
- resumen: Cuando los datos fluyen continuamente entre empresas, es posible generar scorecards actualizados que muestren el desempeño de toda la cadena y de cada empresa individual. La transparencia total (todos ven el desempeño de todos) crea un bucle de retroalimentación autocorrectivo: las empresas corrigen sus propios problemas rápidamente sin esperar instrucciones, porque saben que su desempeño es visible para todos. Esto eleva el desempeño colectivo de la cadena por encima de lo que lograría cada empresa operando de forma aislada.
- pasos:
  1. Definir métricas clave de desempeño compartidas entre todos los socios de la cadena (entregas a tiempo, niveles de inventario, precisión de pronósticos)
  2. Construir un scorecard visible para todas las partes, actualizado en tiempo real o casi real
  3. Comunicar que el desempeño de cada empresa es visible para el resto de la cadena
  4. Dejar que las empresas autocorrijan su desempeño sin intervención centralizada constante
  5. Revisar el scorecard periódicamente en reuniones de coordinación (ej: conference calls)
- entregable: Scorecard funcional compartido entre los miembros de la cadena de suministro con métricas actualizadas regularmente

### D-12
- mundo propuesto: compras (compras y proveedores (elegir, negociar y gestionar proveedores y contratos de compra))
- titulo: Gestión y Seguimiento del Desempeño de Proveedores
- resumen: Una vez firmados los contratos, es necesario medir y gestionar el desempeño de los proveedores contra lo acordado. Dado que las empresas reducen su base de proveedores, cada uno se vuelve crítico. El Vendor-Managed Inventory (VMI) es un ejemplo donde el proveedor monitorea el inventario del cliente y envía productos proactivamente según niveles de uso, facturando bajo los términos del contrato.
- pasos:
  1. Establecer indicadores de desempeño (KPIs) alineados al contrato
  2. Recolectar datos de desempeño de proveedores de forma rutinaria
  3. Notificar y exigir corrección a proveedores que no cumplen niveles acordados
  4. Evaluar implementar Vendor-Managed Inventory (VMI) para proveedores estratégicos
- entregable: Sistema de seguimiento de KPIs de proveedores con reportes periódicos de cumplimiento

### D-13
- mundo propuesto: compras (compras y proveedores (elegir, negociar y gestionar proveedores y contratos de compra))
- titulo: Detectar y calcular el costo del efecto látigo en tu cadena de suministro
- resumen: El efecto látigo (bullwhip) pasa cuando un cambio pequeño en lo que pide el cliente final se va agrandando a medida que sube por tu cadena de proveedores, y cada eslabón termina con una idea distinta de cuánta demanda real hay. Primero te quedas corto de inventario, después te sobra. Antes de gastar en resolverlo, tienes que medir qué tan grande es el efecto en tu caso y calcular cuánto te cuesta en producción, transporte, inventario y ventas que pierdes por no tener producto.
- pasos:
  1. Mide qué tan grande es el efecto látigo en tu negocio comparando cómo varía la demanda en distintos puntos de tu cadena
  2. Calcula cuánto te está costando en producción y en programar tu operación
  3. Calcula cuánto te está costando en transporte, envíos y recepción de mercadería
  4. Averigua cuánto inventario necesitas para no quedarte sin producto y cuánto te cuesta mantenerlo
  5. Revisa cuánto estás perdiendo en ventas por no tener producto disponible cuando lo necesitas
  6. Usa estos números para decidir si vale la pena invertir en compartir datos o coordinarte mejor con tus proveedores
- entregable: Un cálculo claro de cuánto te cuesta el efecto látigo en tu negocio, que te sirva para decidir si conviene invertir en mejor visibilidad de datos con tus proveedores

### D-14
- mundo propuesto: compras (compras y proveedores (elegir, negociar y gestionar proveedores y contratos de compra))
- titulo: Criterios para Elegir a tus Proveedores (Source Selection Criteria)
- resumen: Es la lista de puntos que le pides a un proveedor para trabajar contigo en un contrato. Te sirve para comparar propuestas sin dejarte llevar solo por la primera impresión: le das más peso a lo que más te importa y calificas a cada proveedor en cada punto para llegar a un resultado claro.
- pasos:
  1. Decide qué vas a evaluar en cada proveedor (experiencia, precio, calidad, etc.)
  2. Reparte la importancia entre esos puntos hasta que sumen el 100%
  3. Define cómo vas a calificar cada punto
  4. Evalúa cada propuesta con esos mismos puntos
  5. Multiplica la importancia de cada punto por la calificación que le pusiste
  6. Suma los resultados y elige al proveedor con el puntaje más alto
- entregable: Una tabla donde comparas a cada proveedor con la importancia que le diste a cada punto, la calificación que le pusiste y el puntaje total que obtuvo.

### D-15
- mundo propuesto: risk_management (gestion de riesgos)
- titulo: Auditoría de Riesgos
- resumen: La Auditoría de Riesgos evalúa la efectividad del proceso de identificación de riesgos, las respuestas implementadas y el proceso general de gestión de riesgos. Se revisan los eventos de riesgo ocurridos, sus causas, las respuestas aplicadas y su éxito, así como el cumplimiento del proceso de gestión de riesgos y las herramientas utilizadas, identificando buenas prácticas y áreas de mejora.
- pasos:
  1. Revisar los eventos de riesgo ocurridos durante el proyecto y sus causas
  2. Evaluar las respuestas a riesgos implementadas y su nivel de éxito
  3. Auditar el cumplimiento del proceso de gestión de riesgos
  4. Documentar las herramientas y técnicas utilizadas
  5. Identificar buenas prácticas y áreas de mejora para futuros proyectos
- entregable: Informe de Auditoría de Riesgos con hallazgos sobre eventos, respuestas y proceso general

### D-16
- mundo propuesto: entrega (logistica y entrega (empaque, envio, inventario, transporte, devoluciones))
- titulo: Modelado y Simulación de Cadena de Suministro con Cuatro Entidades
- resumen: Cualquier cadena de suministro puede modelarse definiendo cuatro tipos de entidades: Productos (costo, peso, volumen), Instalaciones (ubicación, costos operativos, tasas de producción/demanda), Vehículos (velocidad, capacidad, costos, rutas) y Rutas (destinos, distancias, frecuencias). Usando mapas digitales (Google Maps, etc.) estas entidades se colocan geográficamente y se simulan interacciones para detectar problemas de desempeño antes de implementarlos en la realidad, reduciendo riesgo y costo de errores.
- pasos:
  1. Definir los datos clave de tus productos, instalaciones, vehículos y rutas.
  2. Usar una herramienta de mapeo o software de simulación (ej. SCM Globe) para colocar estas entidades geográficamente.
  3. Ejecutar simulaciones para detectar cuellos de botella, exceso de inventario o incumplimientos antes de operar en el mundo real.
  4. Iterar el diseño hasta lograr el balance óptimo entre costo y nivel de servicio.
- entregable: Modelo de simulación de la cadena de suministro con métricas base de desempeño (inventario, costos, tiempos).

### D-17
- mundo propuesto: entrega (logistica y entrega (empaque, envio, inventario, transporte, devoluciones))
- titulo: Simulación de Cadenas de Suministro Circulares y Sostenibles
- resumen: Antes de implementar una cadena de suministro física, es posible construir un modelo de simulación compuesto por entidades clave (productos, instalaciones, vehículos, rutas) para probar diferentes escenarios de oferta, demanda, costos y ubicaciones. Esto permite generar reportes de P&L y KPIs que sirven de base objetiva para comparar diseños alternativos antes de invertir capital, especialmente relevante en cadenas de suministro circulares (como recolección de aceite usado para biodiesel) donde el impacto ambiental y la eficiencia económica deben equilibrarse.
- pasos:
  1. Definir las entidades del modelo: productos, instalaciones, vehículos y rutas
  2. Usar el método del centro de gravedad para ubicar instalaciones de recolección/hubs
  3. Correr simulaciones de al menos 14 días con distintos supuestos de oferta y demanda
  4. Generar reportes de P&L y KPIs a partir de los datos simulados
  5. Comparar diseños alternativos de cadena de suministro antes de la inversión real
- entregable: Modelo de simulación funcional con reporte de P&L y KPIs para al menos dos escenarios de diseño de cadena de suministro

### D-18
- mundo propuesto: quality (gestion de la calidad)
- titulo: Auditoría de Calidad
- resumen: Revisión estructurada e independiente de procesos, documentos o productos del proyecto para verificar cumplimiento de políticas y plan de calidad, identificando buenas prácticas y áreas de mejora.
- pasos:
  1. Seleccionar el área o proceso a auditar
  2. Documentar buenas prácticas identificadas
  3. Registrar deficiencias con acción correctiva, responsable y fecha límite
  4. Generar Change Request si se requiere acción correctiva
- entregable: Informe de auditoría de calidad con hallazgos y acciones correctivas asignadas

### D-19
- mundo propuesto: seguridad_digital (seguridad digital)
- titulo: Gestión de Riesgos de Seguridad en IA (Prompt Injection y Jailbreaking)
- resumen: Los sistemas de IA pueden ser manipulados mediante técnicas como 'prompt injection' (instrucciones ocultas en contenido web o documentos que la IA lee) y 'jailbreaking' (convencer a la IA de romper sus reglas mediante escenarios ficticios o roleplay). Esto representa un riesgo real para cualquier negocio que integre IA con acceso a datos externos, atención al cliente automatizada o generación de contenido, ya que actores malintencionados pueden explotar estas vulnerabilidades para phishing, desinformación o fraude.
- pasos:
  1. Evaluar qué fuentes de datos externas puede leer la IA integrada en el producto (webs, documentos, emails)
  2. Sugerencia de My Idea: realizar pruebas de penetración (red teaming) intentando jailbreaks comunes antes de lanzar el producto
  3. Sugerencia de My Idea: Establecer capas de validación adicionales para instrucciones que provengan de contenido no confiable
  4. Monitorear el uso del sistema en producción para detectar patrones de abuso o manipulación
- entregable: Plan de mitigación de riesgos de seguridad para el sistema de IA del negocio

### D-20
- mundo propuesto: compras (compras y proveedores (elegir, negociar y gestionar proveedores y contratos de compra))
- titulo: Diagnóstico del Efecto Látigo (Bullwhip Effect)
- resumen: El efecto látigo describe cómo pequeños cambios en la demanda del consumidor final se amplifican en oscilaciones cada vez mayores conforme se transmiten hacia atrás en la cadena de suministro (minorista, distribuidor, fabricante), generando ciclos de escasez y luego exceso de inventario. Fue ilustrado con el 'beer game' del MIT y documentado por Peter Senge. Provoca sobrecostos en producción, inventario, transporte y mano de obra, además de pérdida de ventas.
- pasos:
  1. Comparar las órdenes recibidas en cada eslabón contra la demanda real del consumidor final
  2. Identificar si existe amplificación de la variabilidad de la demanda al subir en la cadena
  3. Simular el 'beer game' o un ejercicio similar con el equipo para visualizar la dinámica
  4. Cuantificar costos asociados a sobreproducción, exceso de inventario y rupturas de stock
- entregable: Informe de diagnóstico que evidencie la presencia y magnitud del efecto látigo en la cadena propia

### D-21
- mundo propuesto: compras (compras y proveedores (elegir, negociar y gestionar proveedores y contratos de compra))
- titulo: Iniciar la Colaboración en la Cadena de Suministro
- resumen: El primer paso para reducir el efecto látigo es medirlo dentro de la propia empresa, comparando el volumen y frecuencia de pedidos recibidos de clientes contra los pedidos realizados a proveedores. Compartir datos de inventario y demanda con socios comerciales (como hacen Walmart, Dell y P&G) permite decisiones más eficientes en toda la cadena, en lugar de que cada empresa optimice de forma aislada.
- pasos:
  1. Medir el efecto látigo comparando pedidos entrantes vs. pedidos salientes durante un periodo (trimestre o año)
  2. Graficar la divergencia entre demanda de clientes y órdenes a proveedores
  3. Determinar la posición de la empresa en la cadena (cerca o lejos del cliente final)
  4. Establecer acuerdos de intercambio de datos de inventario y ventas (POS) con socios clave
  5. Construir un sistema simple y de bajo costo de visibilidad de inventario compartido (spreadsheets, bases de datos, reportes) si no hay presupuesto para software especializado
- entregable: Gráfico de medición del efecto látigo propio y acuerdo inicial de intercambio de datos con al menos un socio clave

### D-22
- mundo propuesto: risk_management (gestion de riesgos)
- titulo: Cómo manejar el riesgo natural y operativo en tu cadena de suministro
- resumen: Manejar el riesgo en tu cadena de suministro es un equilibrio constante entre lograr buen desempeño a bajo costo y cuidarte de eventos que puedan interrumpir tu operación. Si eliminas proveedores duplicados, instalaciones extra o stock de seguridad, bajas costos pero subes el riesgo ante una disrupción. Evalúa el riesgo natural (desastres) y operativo (calidad, mano de obra, tipo de cambio, impuestos, infraestructura, robo, terrorismo) de cada país o ubicación donde trabajas, para decidir cuánto stock de seguridad necesitas según cuánto riesgo estás dispuesto a asumir.
- pasos:
  1. Define cuánto riesgo estás dispuesto a asumir hoy
  2. Cuantifica el riesgo natural de cada país o región donde operas (terremotos, huracanes, sequías, etc.)
  3. Evalúa el riesgo operativo por país (calidad, mano de obra, tipo de cambio, impuestos, infraestructura, robo, terrorismo, enfermedades)
  4. Junta a quienes se ocupan de operaciones, finanzas, compras y tecnología para mirar el riesgo desde distintos ángulos
  5. Crea un mapa, físico o digital, de tus instalaciones y rutas de suministro para tener un contexto común
  6. Corre simulaciones de escenarios que podrían interrumpir tu operación, por ejemplo un huracán, para ver qué instalaciones son más vulnerables
  7. Decide cuánto stock de seguridad necesitas según el riesgo de cada país y cuánto riesgo estás dispuesto a asumir
  8. Calcula el costo extra de cada opción de protección y compáralas antes de decidir
- entregable: Un plan de contingencia escrito con los niveles de stock de seguridad que necesitas, los proveedores duplicados donde haga falta, y un mapa de riesgo por instalación o país.

### D-23
- mundo propuesto: entrega (logistica y entrega (empaque, envio, inventario, transporte, devoluciones))
- titulo: Sistema de Visibilidad End-to-End con Componentes IT Simples
- resumen: Ante restricciones de tiempo y presupuesto, es posible construir un sistema de visibilidad de cadena de suministro combinando componentes IT básicos y accesibles (hojas de cálculo, archivos de texto, email, páginas web, bases de datos relacionales, scripts simples) en vez de comprar software costoso y complejo. La clave es identificar el patrón subyacente simple detrás de la aparente complejidad del problema (siguiendo la lógica de Sun Tzu: pocas notas, infinitas combinaciones) y usar esos componentes para crear una vista actualizada constantemente de inventario, producción y demanda, visible para todos los actores de la cadena.
- pasos:
  1. Identificar el patrón simple detrás del problema complejo (ej: rastrear uso diario, actualizar pronósticos, mover inventario, agotar stock a tiempo)
  2. Inventariar qué componentes IT básicos ya tienen acceso todas las partes de la cadena (spreadsheets, email, bases de datos)
  3. Diseñar un sistema modesto que combine estos componentes para recolectar datos de inventario en producción, almacén y pedidos
  4. Incluir datos de facturación/entregas para rastrear demanda real a nivel tienda y región
  5. Implementar llamadas de conferencia recurrentes usando el sistema para revisar números y proyectar fechas de agotamiento
  6. Iterar el sistema agregando nuevas vistas y cálculos según se necesiten
  7. Documentar aprendizajes y extender el sistema a otros productos o líneas
- entregable: Sistema funcional de bajo costo (construido en semanas, no meses) que ofrece visibilidad end-to-end de inventario y demanda entre múltiples actores de la cadena de suministro

### D-24
- mundo propuesto: compras (compras y proveedores (elegir, negociar y gestionar proveedores y contratos de compra))
- titulo: Cierre de Contrato
- resumen: El Cierre de Contrato documenta el desempeño del proveedor para evaluaciones futuras, asegurando que todas las disputas se resuelvan, el producto sea aceptado y los pagos finales realizados antes de cerrar formalmente el contrato. Incluye análisis de desempeño del proveedor, registro de cambios contractuales y disputas, así como la fecha de finalización, firma y pago final.
- pasos:
  1. Confirmar que todas las disputas contractuales estén resueltas
  2. Verificar que el producto o resultado haya sido aceptado
  3. Confirmar que se hayan realizado los pagos finales
  4. Documentar el análisis de desempeño del proveedor y registro de cambios
  5. Registrar la fecha de finalización del contrato y firma de cierre
- entregable: Informe de Cierre de Contrato con desempeño del proveedor, cambios, disputas y firma final

### D-25
- mundo propuesto: quality (gestion de la calidad)
- titulo: Métricas de Calidad
- resumen: Proporcionan mediciones específicas y detalladas sobre un atributo del proyecto, producto o servicio, y cómo debe medirse. Se consultan en el proceso de aseguramiento de calidad y se comparan contra los resultados reales en el proceso de control de calidad para determinar si se requiere acción correctiva.
- pasos:
  1. Identificar el atributo del producto o proceso a medir
  2. Definir la métrica específica (valor objetivo)
  3. Establecer el método de medición
  4. Documentar en formato estandarizado con ID único
- entregable: Tabla de métricas de calidad con atributos, valores objetivo y métodos de medición

### D-26
- mundo propuesto: entrega (logistica y entrega (empaque, envio, inventario, transporte, devoluciones))
- titulo: Decidir si empacas tú mismo o subcontratas el envío
- resumen: Antes de crecer tienes que decidir si empacas y despachas tus propios pedidos o si le pagas a un tercero que lo haga por ti. Empacar tu mismo te da control total sobre la experiencia del cliente, pero te consume tiempo y espacio que podrias usar para vender. Subcontratar libera ese tiempo, pero pone la marca de tu negocio en manos de otro: muchos compradores eligen que tienda comprar segun el courier que usa, asi que el operador que elijas se vuelve parte de tu reputacion. No es una decision de una sola vez: conviene revisarla cuando el volumen cambie, porque lo que conviene con pocos pedidos puede dejar de convenir cuando crecen.
- pasos:
  1. Calcula cuanto tiempo y espacio te toma empacar cada pedido tu mismo en una semana normal.
  2. Compara ese costo contra las tarifas de un operador logistico local.
  3. Pregunta a tus clientes que tan importante es la marca del courier en su decision de comprarte.
  4. Prueba subcontratar solo una parte de tus pedidos antes de mover todo el volumen.
  5. Decide segun quien te da mas control sobre la experiencia del cliente sin romper tu margen.
- entregable: Una decision escrita sobre fulfilment propio o tercerizado con el costo por pedido de cada opcion.

### D-27
- mundo propuesto: entrega (logistica y entrega (empaque, envio, inventario, transporte, devoluciones))
- titulo: Plataforma de Colaboración en Tiempo Real para Cadena de Suministro
- resumen: Una plataforma basada en la nube que ofrece visibilidad casi en tiempo real a todos los actores de la cadena de suministro (fabricantes, logística, distribuidores, retailers) permite que cada parte identifique problemas y actúe sin esperar instrucciones de una autoridad central. Se combina con sesiones de 'colaboración masiva' (crowdsourcing) donde múltiples empresas ajustan en vivo el diseño de la cadena, corren simulaciones, y llegan a consenso sobre el plan operativo, generando compromiso genuino de todas las partes.
- pasos:
  1. Implementar un sistema visual (mapa) compartido con datos en tiempo real de inventario, rutas y costos.
  2. Organizar sesiones de colaboración masiva con todos los socios clave de la cadena.
  3. Permitir que cada participante edite y proponga cambios visibles para todos en vivo.
  4. Correr simulaciones colectivas y ajustar el diseño hasta llegar a consenso.
  5. Usar la plataforma no solo para planificar sino para monitorear operaciones diarias y resolver problemas en tiempo real.
- entregable: Plataforma o sistema de visibilidad compartida activa entre los socios de la cadena de suministro, con métricas base y alertas de desviación.

### D-28
- mundo propuesto: entrega (logistica y entrega (empaque, envio, inventario, transporte, devoluciones))
- titulo: Estandarización de Datos de Producto (EPC y GDSN)
- resumen: El uso de números de parte internos distintos entre empresas genera errores costosos de traducción, facturación y pronóstico. El Electronic Product Code (EPC) y redes como el Global Data Synchronization Network (GDSN) permiten un identificador único compartido entre socios comerciales, eliminando traducciones manuales y mejorando la precisión de los datos de ventas e inventario.
- pasos:
  1. Evaluar los costos actuales de traducción de números de parte entre socios comerciales
  2. Adoptar códigos EPC para la comunicación externa manteniendo códigos internos si se desea
  3. Conectar la empresa a un 'data pool' del GDSN a través de GS1
  4. Clasificar los productos usando estándares como UNSPSC o GPC para análisis jerárquico
- entregable: Catálogo de productos con códigos EPC/GPC asignados y conexión activa a la red GDSN

### D-29
- mundo propuesto: entrega (logistica y entrega (empaque, envio, inventario, transporte, devoluciones))
- titulo: Gestión del Racionamiento y Shortage Gaming
- resumen: Cuando la demanda supera la oferta, los fabricantes racionan producto según pedidos recibidos, lo que incentiva a distribuidores a inflar artificialmente sus órdenes para recibir más asignación (shortage gaming). Esto distorsiona la demanda real percibida en toda la cadena de suministro.
- pasos:
  1. Basar las decisiones de racionamiento en patrones históricos de pedidos del cliente, no en el tamaño de la orden actual
  2. Comunicar con anticipación a los clientes cuando se detecte que la demanda superará la oferta
  3. Implementar sistemas de alerta temprana de escasez para evitar compras de pánico
- entregable: Política de racionamiento basada en histórico y protocolo de comunicación anticipada de escasez

### D-30
- mundo propuesto: entrega (logistica y entrega (empaque, envio, inventario, transporte, devoluciones))
- titulo: Planificación de Misión y Operaciones (M&OP)
- resumen: El M&OP es una adaptación del proceso comercial de Sales and Operations Planning (S&OP) para cadenas de suministro ad hoc como las de respuesta a desastres. Es un proceso de cinco pasos que comienza con la definición de la misión (CONOPS), sigue con planificación de demanda por instalación, planificación de transporte, modelado del supply chain y simulación para elegir el mejor plan antes de ejecutarlo en el mundo real.
- pasos:
  1. Definir el concepto de operaciones (CONOPS): origen de suministros, instalaciones y necesidades
  2. Realizar planificación de demanda por instalación según población afectada
  3. Planificar el uso de vehículos disponibles para transportar suministros
  4. Modelar la cadena de suministro propuesta con los datos de demanda y transporte
  5. Simular el modelo para detectar problemas y elegir el plan de mejor desempeño antes de ejecutarlo
- entregable: Plan de operaciones de cinco pasos (CONOPS, demanda, transporte, modelo, simulación) validado antes de su ejecución

### D-31
- mundo propuesto: entrega (logistica y entrega (empaque, envio, inventario, transporte, devoluciones))
- titulo: Cadenas de Suministro para Respuesta a Desastres
- resumen: Las cadenas de suministro de respuesta a desastres (DR) enfrentan alta imprevisibilidad y organización ad hoc, sin autoridad centralizada clara. A diferencia de las cadenas comerciales, requieren mayores niveles de inventario de contingencia (surge capacity), planificación pre-desastre, y entrenamiento colaborativo entre organizaciones diversas (gobierno, ONG, militares, empresas) que normalmente no trabajan juntas.
- pasos:
  1. Realizar pronósticos simplificados de demanda basados en riesgo geográfico y población
  2. Preposicionar inventario estratégico ('surge capacity') en ubicaciones clave
  3. Seleccionar proveedores capaces de escalar rápidamente en caso de emergencia
  4. Diseñar y ejecutar simulaciones de entrenamiento colaborativo entre organizaciones participantes
  5. Establecer una plataforma común de datos (basada en mapas) para coordinación en tiempo real
- entregable: Plan de preparación pre-desastre con inventario de contingencia, proveedores identificados y ejercicios de entrenamiento colaborativo diseñados

### D-32
- mundo propuesto: compras (compras y proveedores (elegir, negociar y gestionar proveedores y contratos de compra))
- titulo: Compartición de Datos entre Empresas de la Cadena de Suministro
- resumen: Compartir datos de demanda, decisiones y métricas de desempeño entre las empresas de una cadena de suministro mejora la toma de decisiones colectiva y reduce distorsiones como el efecto látigo (bullwhip effect). Aunque existe reticencia por temor a filtrar información confidencial a competidores, las cadenas que colaboran eficientemente ganan cuota de mercado frente a las que no lo hacen, ya que la competencia se traslada de empresa-contra-empresa a cadena-de-suministro-contra-cadena-de-suministro.
- pasos:
  1. Definir qué datos de demanda, decisiones y desempeño se pueden compartir de forma segura
  2. Establecer mecanismos electrónicos (reportes vía web) para compartir información con socios
  3. Compartir decisiones internas con impacto en demanda (ej. promociones) con proveedores clave
  4. Evaluar cuantitativamente los beneficios de la colaboración frente a los riesgos de exposición
- entregable: Acuerdo de intercambio de datos con al menos un socio clave de la cadena de suministro

### D-33
- mundo propuesto: entrega (logistica y entrega (empaque, envio, inventario, transporte, devoluciones))
- titulo: IoT y Big Data para Trazabilidad de Supply Chain
- resumen: El Internet de las Cosas (IoT) conecta dispositivos embebidos en productos y equipos para enviar y recibir datos en tiempo real, generando volúmenes masivos de 'big data' que alimentan el análisis de patrones y tendencias en la cadena de suministro. Esta evolución va desde códigos de barras, pasando por RFID, hasta microchips embebidos en cualquier producto, permitiendo un seguimiento continuo y granular del movimiento de mercancías.
- pasos:
  1. Mapear los puntos de la cadena de suministro donde se necesita visibilidad en tiempo real
  2. Seleccionar tecnología de tagging adecuada (código de barras, RFID, chips IoT) según costo y necesidad de datos
  3. Establecer una base de datos centralizada que capture y almacene los datos generados por los dispositivos IoT
  4. Definir qué patrones o KPIs se analizarán con los datos recolectados (tiempos de tránsito, quiebres de stock, etc.)
- entregable: Infraestructura de captura de datos IoT integrada con un repositorio central listo para análisis

### D-34
- mundo propuesto: compras (compras y proveedores (elegir, negociar y gestionar proveedores y contratos de compra))
- titulo: Uso de Scorecards y Criterios Visibles en Gates
- resumen: Los scorecards son herramientas que permiten evaluar proyectos con criterios cualitativos (atractivo de mercado, ventaja competitiva, apalancamiento de competencias) junto con criterios financieros, haciendo la decisión de Go/Kill más objetiva y menos emocional. El 85% de los mejores innovadores usa criterios de Go/Kill específicos, a menudo en forma de scorecard, frente a solo una cuarta parte de las empresas de peor desempeño.
- pasos:
  1. Diseñar un scorecard con criterios cualitativos y financieros ponderados
  2. Aplicar el scorecard en los gates tempranos (Gates 1, 2 y 3)
  3. Considerar la auto-evaluación del equipo de proyecto antes de la reunión de gate (evitando sesgo del gatekeeper)
  4. Comparar puntuaciones del equipo vs gatekeepers y discutir diferencias en la reunión
  5. Integrar métricas financieras (NPV, ECV, Payback Period) al scorecard
- entregable: Scorecard estandarizado y aplicado consistentemente en cada gate, con puntuaciones documentadas y criterios de corte definidos

### D-35
- mundo propuesto: compras (compras y proveedores (elegir, negociar y gestionar proveedores y contratos de compra))
- titulo: Negociación de Contratos con Proveedores
- resumen: La negociación de contratos con proveedores debe equilibrar precio unitario con otros servicios de valor agregado como conexiones electrónicas, entregas frecuentes y precisión en pedidos. Deben especificarse metas de desempeño, penalizaciones y formas de pago (mayor margen en precio, pagos separados o combinación). Entender la cultura y etiqueta de negocios del proveedor es clave para negociaciones interculturales efectivas.
- pasos:
  1. Definir requisitos de producto, precio y niveles de servicio necesarios
  2. Negociar trade-offs entre precio unitario y servicios de valor agregado
  3. Establecer metas de desempeño con penalizaciones claras
  4. Estudiar la cultura y etiqueta de negociación del proveedor si es internacional
  5. Formalizar el contrato con términos de pago, entrega y garantías
- entregable: Contrato firmado con proveedor especificando precios, términos de servicio, penalizaciones y condiciones de pago

### D-36
- mundo propuesto: entrega (logistica y entrega (empaque, envio, inventario, transporte, devoluciones))
- titulo: Crossdocking en Centros de Distribución
- resumen: El crossdocking es una técnica logística en la que los envíos de carga completa llegan a un centro de distribución y se descargan, y al mismo tiempo se fragmentan y combinan con otros productos para cargarse directamente en camiones de salida, minimizando el almacenamiento. Reduce el tiempo de flujo del producto y los costos de manipulación, pero requiere alta coordinación entre entradas y salidas y volúmenes predecibles.
- pasos:
  1. Evaluar si el volumen y la predictibilidad de la demanda justifican crossdocking
  2. Sincronizar horarios de llegada de camiones entrantes con la salida de camiones salientes
  3. Diseñar el layout del centro de distribución para minimizar tiempos de manipulación
  4. Establecer sistemas de coordinación en tiempo real entre proveedores y transportistas
  5. Medir reducción de inventario en tránsito y costos de manipulación
- entregable: Proceso documentado de crossdocking con horarios de sincronización y layout del centro de distribución

### D-37
- mundo propuesto: entrega (logistica y entrega (empaque, envio, inventario, transporte, devoluciones))
- titulo: Combinación de Tecnologías Emergentes para Cadenas Ágiles
- resumen: El verdadero potencial de tecnologías como robots industriales, manufactura aditiva (impresión 3D), vehículos autónomos, drones e IoT se logra cuando se combinan entre sí, no usándolas aisladamente. Empresas como Walmart y Amazon lograron ventajas competitivas dominantes al combinar prácticas logísticas complementarias. La combinación de estas tecnologías permite fábricas flexibles que ajustan rápidamente su producción, almacenes automatizados y entregas más precisas y rápidas.
- pasos:
  1. Mapear las tecnologías disponibles (robots, IoT, manufactura aditiva, vehículos autónomos) aplicables a cada nodo de la cadena
  2. Identificar combinaciones sinérgicas entre tecnologías, no implementaciones aisladas
  3. Priorizar inversión según impacto en flexibilidad de producción y velocidad de entrega
  4. Pilotar la combinación tecnológica en una planta o centro de distribución antes de escalar
- entregable: Un plan de implementación tecnológica combinada con al menos 2 tecnologías integradas y métricas de impacto esperado

### D-38
- mundo propuesto: entrega (logistica y entrega (empaque, envio, inventario, transporte, devoluciones))
- titulo: Inteligencia Artificial Aplicada a la Cadena de Suministro
- resumen: La IA, potenciada por machine learning y modelos de lenguaje grandes (LLMs), te permite encontrar patrones en grandes volúmenes de datos y convertirlos en decisiones accionables en tiempo real. Transforma tres áreas clave: pronóstico de demanda (analizando históricos, tendencias de mercado y factores externos como clima o eventos sociales), optimización de rutas (con datos de tráfico en tiempo real para rutas dinámicas) y operaciones de almacén (automatización y visión computacional para manipular productos de formas variables). El objetivo no es reemplazar tu juicio sino complementarlo: la IA procesa el volumen de datos que a ti te resulta inmanejable desde el teléfono, y tú decides qué hacer con esas señales para ganar ventaja competitiva frente a métodos tradicionales que ya no alcanzan.
- pasos:
  1. Auditar tus fuentes de datos actuales de demanda, rutas o almacén para evaluar su calidad y volumen
  2. Priorizar un área piloto entre forecasting, optimización de rutas u operaciones de almacén
  3. Seleccionar una herramienta de IA/ML compatible con los sistemas que ya usas
  4. Integrar esa herramienta con tus datos históricos y en tiempo real disponibles (tráfico, clima, redes sociales)
  5. Medir la mejora en precisión de pronóstico o eficiencia operativa antes de escalar a otra área
  6. Definir qué decisiones puede tomar la IA sola y cuáles necesitas revisar tú mismo
- entregable: Un plan piloto de IA implementado en un área de tu cadena de suministro, con métricas de mejora documentadas para decidir si escalarlo.

### D-39
- mundo propuesto: entrega (logistica y entrega (empaque, envio, inventario, transporte, devoluciones))
- titulo: Modelado de Simulación para Decisiones de Supply Chain
- resumen: La simulación permite crear un prototipo digital de una fábrica, almacén o red de suministro completa para probar diferentes condiciones antes de implementar cambios reales. Se aplica en tres horizontes: estratégico (1-5 años, ej. dónde construir una planta), táctico (1 mes-1 año, ej. gestión de incertidumbre de demanda) y operativo (1 día-1 mes, ej. layout de almacén). Permite detectar problemas de diseño antes de invertir, reducir stock de seguridad manteniendo el nivel de servicio, y evitar inversiones innecesarias mediante pruebas virtuales.
- pasos:
  1. Recopilar datos de ERP/SCM sobre productos, plantas, costos y restricciones de capacidad
  2. Definir el horizonte de decisión (estratégico, táctico u operativo) y la pregunta a responder
  3. Construir el modelo de simulación representando la red actual o propuesta
  4. Ejecutar el modelo bajo distintos escenarios y variables de incertidumbre (demanda, tráfico, procesos), y no solo optimizar lo existente
  5. Comparar resultados de escenarios para seleccionar el diseño con mejor relación costo-servicio
  6. Validar la solución antes de implementarla físicamente para minimizar riesgo
  7. Definir la estrategia de negocio antes de diseñar la cadena de suministro
  8. Probar combinaciones de tecnologías (robots, manufactura aditiva, vehículos autónomos) en el modelo
  9. Repetir el proceso de simulación periódicamente para adaptarse a cambios del mercado global
- entregable: Modelo de simulación validado con recomendación de diseño de red, layout o política de inventario respaldada por datos
