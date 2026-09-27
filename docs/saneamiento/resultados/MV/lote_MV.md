# Pasada MV: nodos que salen del nucleo a su mundo

## A: aristas del nucleo a un mundo. PUENTE o RETIRAR, con fuerza 1 a 3 (0 si RETIRAR)

### MV-A01
- NODO DEL NUCLEO [alineacion_incentivos_desempeno]
    titulo: Alineación de Incentivos de Desempeño en la Cadena de Suministro | mundo: core
    resumen: Los incentivos de ventas por cuotas mensuales o trimestrales generan compras forzadas al final de cada periodo, empujando producto sin demanda real hacia la cadena. Del mismo modo, incentivos internos en conflicto (ej. minimizar costos de transporte a costa del servicio al cliente) generan ineficiencias sistémicas.
- NODO DEL MUNDO "logistica y entrega" [drum_buffer_rope]
    titulo: Modelo Drum-Buffer-Rope para Sincronizar la Cadena de Suministro | mundo: entrega
    resumen: Modelo que sincroniza toda la cadena de suministro como una sola entidad, alineada al ritmo real de la demanda del mercado (el 'tambor'). Cada empresa gestiona la incertidumbre mediante buffers de inventario o capacidad productiva, y comparten datos de demanda (la 'cuerda') que los mantiene sincronizados, minimizando el efecto látigo (bullwhip effect).

### MV-A02
- NODO DEL NUCLEO [alineacion_ti_negocio]
    titulo: Alinear la tecnología con tu modelo de negocio | mundo: core
    resumen: Cuando tus sistemas y herramientas tecnológicas están alineados con tu modelo de negocio, tienes más chances de que funcione. El lienzo de modelo de negocio (Business Model Canvas) te ayuda a entender rápido cómo funciona tu negocio sin perderte en detalles operativos, y sirve de puente entre tu visión de negocio, las aplicaciones que usas y la tecnología detrás (arquitectura empresarial). Usa el Canvas para definir primero tu visión de negocio y después alinea tus aplicaciones e infraestructura tecnológica en función de eso.
- NODO DEL MUNDO "logistica y entrega" [simulacion_de_operaciones_supply_chain]
    titulo: Modelado de Simulación para Decisiones de Supply Chain | mundo: entrega
    resumen: La simulación permite crear un prototipo digital de una fábrica, almacén o red de suministro completa para probar diferentes condiciones antes de implementar cambios reales. Se aplica en tres horizontes: estratégico (1-5 años, ej. dónde construir una planta), táctico (1 mes-1 año, ej. gestión de incertidumbre de demanda) y operativo (1 día-1 mes, ej. layout de almacén). Permite detectar problemas de diseño antes de invertir, reducir stock de seguridad manteniendo el nivel de servicio, y evitar inversiones innecesarias mediante pruebas virtuales.

### MV-A03
- NODO DEL NUCLEO [ciclo_virtuoso_datos_electronicos]
    titulo: Ciclo Virtuoso de Conexiones Electrónicas de Datos | mundo: core
    resumen: La estrategia efectiva de cadena de suministro comienza con mejorar la precisión y flujo de datos entre empresas. Las conexiones electrónicas simples de datos (vs. EDI/XML costosos y complejos) son la base de un ciclo virtuoso de mejora continua, especialmente relevante para las empresas tier 2/3 que aún dependen de email, fax y hojas de cálculo. Sistemas simples con datos buenos superan a sistemas complejos con datos malos ('garbage in, garbage out').
- NODO DEL MUNDO "logistica y entrega" [estandarizacion_codigos_producto_epc]
    titulo: Estandarización de Datos de Producto (EPC y GDSN) | mundo: entrega
    resumen: El uso de números de parte internos distintos entre empresas genera errores costosos de traducción, facturación y pronóstico. El Electronic Product Code (EPC) y redes como el Global Data Synchronization Network (GDSN) permiten un identificador único compartido entre socios comerciales, eliminando traducciones manuales y mejorando la precisión de los datos de ventas e inventario.

### MV-A04
- NODO DEL NUCLEO [ciclo_virtuoso_datos_electronicos]
    titulo: Ciclo Virtuoso de Conexiones Electrónicas de Datos | mundo: core
    resumen: La estrategia efectiva de cadena de suministro comienza con mejorar la precisión y flujo de datos entre empresas. Las conexiones electrónicas simples de datos (vs. EDI/XML costosos y complejos) son la base de un ciclo virtuoso de mejora continua, especialmente relevante para las empresas tier 2/3 que aún dependen de email, fax y hojas de cálculo. Sistemas simples con datos buenos superan a sistemas complejos con datos malos ('garbage in, garbage out').
- NODO DEL MUNDO "logistica y entrega" [scorecard_desempeno_cadena_suministro]
    titulo: Scorecard de Desempeño y Bucle de Retroalimentación Autocorrectivo | mundo: entrega
    resumen: Cuando los datos fluyen continuamente entre empresas, es posible generar scorecards actualizados que muestren el desempeño de toda la cadena y de cada empresa individual. La transparencia total (todos ven el desempeño de todos) crea un bucle de retroalimentación autocorrectivo: las empresas corrigen sus propios problemas rápidamente sin esperar instrucciones, porque saben que su desempeño es visible para todos. Esto eleva el desempeño colectivo de la cadena por encima de lo que lograría cada empresa operando de forma aislada.

### MV-A05
- NODO DEL NUCLEO [cinco_pasos_enfoque_restricciones]
    titulo: Los Cinco Pasos de Enfoque para Gestionar Restricciones | mundo: core
    resumen: Metodología práctica derivada de la Teoría de Restricciones para identificar y gestionar los cuellos de botella de un sistema (fábrica o cadena de suministro) de forma iterativa: identificar, explotar, subordinar, elevar y repetir el ciclo cuando la restricción se traslada.
- NODO DEL MUNDO "logistica y entrega" [drum_buffer_rope]
    titulo: Modelo Drum-Buffer-Rope para Sincronizar la Cadena de Suministro | mundo: entrega
    resumen: Modelo que sincroniza toda la cadena de suministro como una sola entidad, alineada al ritmo real de la demanda del mercado (el 'tambor'). Cada empresa gestiona la incertidumbre mediante buffers de inventario o capacidad productiva, y comparten datos de demanda (la 'cuerda') que los mantiene sincronizados, minimizando el efecto látigo (bullwhip effect).

### MV-A06
- NODO DEL NUCLEO [combinacion_humano_ia_decision]
    titulo: Combinación Óptima de Personas y Tecnología (Humano + IA) | mundo: core
    resumen: Basado en el estudio de Brynjolfsson y McAfee sobre torneos de ajedrez, se demuestra que equipos de personas con habilidades moderadas usando IA simple y simulaciones superan tanto a expertos humanos sin tecnología como a sistemas de IA complejos sin intervención humana. La clave del éxito está en dejar que las personas hagan el pensamiento creativo y la resolución de problemas, mientras la tecnología realiza los cálculos masivos y valida ideas rápidamente, especialmente bajo presión de tiempo.
- NODO DEL MUNDO "logistica y entrega" [plataforma_colaboracion_tiempo_real]
    titulo: Plataforma de Colaboración en Tiempo Real para Cadena de Suministro | mundo: entrega
    resumen: Una plataforma basada en la nube que ofrece visibilidad casi en tiempo real a todos los actores de la cadena de suministro (fabricantes, logística, distribuidores, retailers) permite que cada parte identifique problemas y actúe sin esperar instrucciones de una autoridad central. Se combina con sesiones de 'colaboración masiva' (crowdsourcing) donde múltiples empresas ajustan en vivo el diseño de la cadena, corren simulaciones, y llegan a consenso sobre el plan operativo, generando compromiso genuino de todas las partes.

### MV-A07
- NODO DEL NUCLEO [contractor_status_report]
    titulo: Informe de Estado del Contratista | mundo: core
    resumen: El Informe de Estado del Contratista es completado por el contratista y presentado periódicamente al director de proyecto. Rastrea el desempeño del periodo actual (alcance, calidad, cronograma, costo) y proporciona pronósticos para periodos futuros. También recopila información sobre nuevos riesgos, disputas y problemas, alimentando el Informe de Desempeño del Proyecto general.
- NODO DEL MUNDO "compras y proveedores" [contract_close_out]
    titulo: Cierre de Contrato | mundo: compras
    resumen: El Cierre de Contrato documenta el desempeño del proveedor para evaluaciones futuras, asegurando que todas las disputas se resuelvan, el producto sea aceptado y los pagos finales realizados antes de cerrar formalmente el contrato. Incluye análisis de desempeño del proveedor, registro de cambios contractuales y disputas, así como la fecha de finalización, firma y pago final.

### MV-A08
- NODO DEL NUCLEO [contractor_status_report]
    titulo: Informe de Estado del Contratista | mundo: core
    resumen: El Informe de Estado del Contratista es completado por el contratista y presentado periódicamente al director de proyecto. Rastrea el desempeño del periodo actual (alcance, calidad, cronograma, costo) y proporciona pronósticos para periodos futuros. También recopila información sobre nuevos riesgos, disputas y problemas, alimentando el Informe de Desempeño del Proyecto general.
- NODO DEL MUNDO "compras y proveedores" [procurement_audit]
    titulo: Auditoría de Adquisiciones | mundo: compras
    resumen: La Auditoría de Adquisiciones es una revisión de los contratos y procesos de contratación para verificar su completitud, precisión y efectividad. Evalúa el desempeño del proveedor (alcance, calidad, cronograma, costo, facilidad de trabajo) y el proceso de gestión de adquisiciones en sí, generando información útil para mejorar contratos futuros y alimentar las Lecciones Aprendidas.

### MV-A09
- NODO DEL NUCLEO [coordinacion_colaboracion_cadena_suministro]
    titulo: Coordinación y Colaboración como Ventaja Competitiva | mundo: core
    resumen: En economías de alto cambio, la coordinación entre empresas de una cadena de suministro es más poderosa que el control unilateral. Las ganancias vienen de conectarse a redes de cadena de suministro y desarrollar reputación de buen servicio y buenos productos a precios razonables (no necesariamente los más bajos). Sistemas diseñados para dar control excesivo a grandes empresas sobre proveedores (bajo el disfraz de 'eficiencia') desmotivan a los proveedores y destruyen la innovación colectiva, dejando a toda la cadena vulnerable cuando el mercado cambia (ejemplo iPhone: ecosistema colaborativo vs. control unilateral).
- NODO DEL MUNDO "compras y proveedores" [collaboration_enablers]
    titulo: Habilitadores Clave para la Colaboración en Supply Chain | mundo: compras
    resumen: Para que las iniciativas colaborativas tengan éxito se requieren habilitadores humanos y tecnológicos: interés común, apertura, reconocimiento de prioridades, expectativas claras, liderazgo, cooperación (no castigo), confianza, reparto de beneficios y TI avanzada. Sin estos elementos, la colaboración fracasa ante los obstáculos naturales del negocio tradicional.

### MV-A10
- NODO DEL NUCLEO [coordinacion_colaboracion_cadena_suministro]
    titulo: Coordinación y Colaboración como Ventaja Competitiva | mundo: core
    resumen: En economías de alto cambio, la coordinación entre empresas de una cadena de suministro es más poderosa que el control unilateral. Las ganancias vienen de conectarse a redes de cadena de suministro y desarrollar reputación de buen servicio y buenos productos a precios razonables (no necesariamente los más bajos). Sistemas diseñados para dar control excesivo a grandes empresas sobre proveedores (bajo el disfraz de 'eficiencia') desmotivan a los proveedores y destruyen la innovación colectiva, dejando a toda la cadena vulnerable cuando el mercado cambia (ejemplo iPhone: ecosistema colaborativo vs. control unilateral).
- NODO DEL MUNDO "logistica y entrega" [plataforma_colaboracion_tiempo_real]
    titulo: Plataforma de Colaboración en Tiempo Real para Cadena de Suministro | mundo: entrega
    resumen: Una plataforma basada en la nube que ofrece visibilidad casi en tiempo real a todos los actores de la cadena de suministro (fabricantes, logística, distribuidores, retailers) permite que cada parte identifique problemas y actúe sin esperar instrucciones de una autoridad central. Se combina con sesiones de 'colaboración masiva' (crowdsourcing) donde múltiples empresas ajustan en vivo el diseño de la cadena, corren simulaciones, y llegan a consenso sobre el plan operativo, generando compromiso genuino de todas las partes.

### MV-A11
- NODO DEL NUCLEO [cost_management_plan]
    titulo: Cost Management Plan | mundo: core
    resumen: Es la parte de tu plan de proyecto que define cómo vas a estimar, estructurar, monitorear y controlar los costos a lo largo de todo el ciclo de vida del proyecto. Incluye el nivel de precisión que necesitas en tus estimaciones, las unidades de medida y la moneda que usarás, los umbrales de varianza para detectar desviaciones del presupuesto, y las reglas de medición de desempeño, como el valor ganado. También cubre las técnicas de estimación que aplicarás y el proceso para desarrollar el presupuesto por fases, así como quién tiene autoridad para asignar partidas presupuestarias. Este documento te da el marco de referencia para tomar decisiones financieras consistentes durante toda la ejecución del proyecto.
- NODO DEL MUNDO "gestion de riesgos" [risk_audit]
    titulo: Auditoría de Riesgos | mundo: risk_management
    resumen: La Auditoría de Riesgos evalúa la efectividad del proceso de identificación de riesgos, las respuestas implementadas y el proceso general de gestión de riesgos. Se revisan los eventos de riesgo ocurridos, sus causas, las respuestas aplicadas y su éxito, así como el cumplimiento del proceso de gestión de riesgos y las herramientas utilizadas, identificando buenas prácticas y áreas de mejora.

### MV-A12
- NODO DEL NUCLEO [creacion_data_warehouse]
    titulo: Crea un repositorio central de datos para tu cadena de suministro (data warehouse) | mundo: core
    resumen: Un repositorio central de datos (data warehouse) junta la información de los distintos sistemas que usas para operar y llevar las cuentas de tu negocio, capturándola automáticamente desde la fuente para que no tengas que ingresarla a mano. Combina una base de datos con herramientas de reportes ya armados, gráficos y consultas que puedes hacer tú mismo. Conviene que empieces con algo simple y lo vayas ampliando a medida que le agarras la mano a usar los datos todos los días.
- NODO DEL MUNDO "compras y proveedores" [compartir_datos_cadena_suministro]
    titulo: Compartición de Datos entre Empresas de la Cadena de Suministro | mundo: compras
    resumen: Compartir datos de demanda, decisiones y métricas de desempeño entre las empresas de una cadena de suministro mejora la toma de decisiones colectiva y reduce distorsiones como el efecto látigo (bullwhip effect). Aunque existe reticencia por temor a filtrar información confidencial a competidores, las cadenas que colaboran eficientemente ganan cuota de mercado frente a las que no lo hacen, ya que la competencia se traslada de empresa-contra-empresa a cadena-de-suministro-contra-cadena-de-suministro.

### MV-A13
- NODO DEL NUCLEO [definicion_alineacion_cadena_suministro]
    titulo: Definición y Alineación de la Cadena de Suministro con la Estrategia | mundo: core
    resumen: Una cadena de suministro es la red de empresas y actividades necesarias para diseñar, fabricar, entregar y usar un producto o servicio. Toda empresa participa en una o más cadenas de suministro y debe entender el rol que juega en ellas. La gestión de la cadena de suministro (SCM) es la coordinación sistémica de producción, inventario, ubicación y transporte entre los participantes para lograr el mejor balance entre capacidad de respuesta y eficiencia según el mercado servido. La estrategia de la empresa (competir por precio vs. por servicio/conveniencia) debe determinar el diseño de su cadena de suministro.
- NODO DEL MUNDO "compras y proveedores" [gestion_procurement_consumo]
    titulo: Cuánto y qué compras en tu negocio (procurement) | mundo: compras
    resumen: Antes de negociar con tus proveedores, necesitas entender cuánto y qué compras en todo tu negocio. Define cuánto esperas consumir de cada categoría de producto y en cada lugar donde operas, y compara eso regularmente con lo que realmente consumes para detectar desviaciones que te avisen de problemas u oportunidades.

### MV-A14
- NODO DEL NUCLEO [definicion_alineacion_cadena_suministro]
    titulo: Definición y Alineación de la Cadena de Suministro con la Estrategia | mundo: core
    resumen: Una cadena de suministro es la red de empresas y actividades necesarias para diseñar, fabricar, entregar y usar un producto o servicio. Toda empresa participa en una o más cadenas de suministro y debe entender el rol que juega en ellas. La gestión de la cadena de suministro (SCM) es la coordinación sistémica de producción, inventario, ubicación y transporte entre los participantes para lograr el mejor balance entre capacidad de respuesta y eficiencia según el mercado servido. La estrategia de la empresa (competir por precio vs. por servicio/conveniencia) debe determinar el diseño de su cadena de suministro.
- NODO DEL MUNDO "gestion de riesgos" [gestion_riesgo_cadena_suministro]
    titulo: Cómo manejar el riesgo natural y operativo en tu cadena de suministro | mundo: risk_management
    resumen: Manejar el riesgo en tu cadena de suministro es un equilibrio constante entre lograr buen desempeño a bajo costo y cuidarte de eventos que puedan interrumpir tu operación. Si eliminas proveedores duplicados, instalaciones extra o stock de seguridad, bajas costos pero subes el riesgo ante una disrupción. Evalúa el riesgo natural (desastres) y operativo (calidad, mano de obra, tipo de cambio, impuestos, infraestructura, robo, terrorismo) de cada país o ubicación donde trabajas, para decidir cuánto stock de seguridad necesitas según cuánto riesgo estás dispuesto a asumir.

### MV-A15
- NODO DEL NUCLEO [definicion_alineacion_cadena_suministro]
    titulo: Definición y Alineación de la Cadena de Suministro con la Estrategia | mundo: core
    resumen: Una cadena de suministro es la red de empresas y actividades necesarias para diseñar, fabricar, entregar y usar un producto o servicio. Toda empresa participa en una o más cadenas de suministro y debe entender el rol que juega en ellas. La gestión de la cadena de suministro (SCM) es la coordinación sistémica de producción, inventario, ubicación y transporte entre los participantes para lograr el mejor balance entre capacidad de respuesta y eficiencia según el mercado servido. La estrategia de la empresa (competir por precio vs. por servicio/conveniencia) debe determinar el diseño de su cadena de suministro.
- NODO DEL MUNDO "logistica y entrega" [ia_en_supply_chain]
    titulo: Inteligencia Artificial Aplicada a la Cadena de Suministro | mundo: entrega
    resumen: La IA, potenciada por machine learning y modelos de lenguaje grandes (LLMs), te permite encontrar patrones en grandes volúmenes de datos y convertirlos en decisiones accionables en tiempo real. Transforma tres áreas clave: pronóstico de demanda (analizando históricos, tendencias de mercado y factores externos como clima o eventos sociales), optimización de rutas (con datos de tráfico en tiempo real para rutas dinámicas) y operaciones de almacén (automatización y visión computacional para manipular productos de formas variables). El objetivo no es reemplazar tu juicio sino complementarlo: la IA procesa el volumen de datos que a ti te resulta inmanejable desde el teléfono, y tú decides qué hacer con esas señales para ganar ventaja competitiva frente a métodos tradicionales que ya no alcanzan.

### MV-A16
- NODO DEL NUCLEO [definicion_alineacion_cadena_suministro]
    titulo: Definición y Alineación de la Cadena de Suministro con la Estrategia | mundo: core
    resumen: Una cadena de suministro es la red de empresas y actividades necesarias para diseñar, fabricar, entregar y usar un producto o servicio. Toda empresa participa en una o más cadenas de suministro y debe entender el rol que juega en ellas. La gestión de la cadena de suministro (SCM) es la coordinación sistémica de producción, inventario, ubicación y transporte entre los participantes para lograr el mejor balance entre capacidad de respuesta y eficiencia según el mercado servido. La estrategia de la empresa (competir por precio vs. por servicio/conveniencia) debe determinar el diseño de su cadena de suministro.
- NODO DEL MUNDO "logistica y entrega" [simulacion_de_operaciones_supply_chain]
    titulo: Modelado de Simulación para Decisiones de Supply Chain | mundo: entrega
    resumen: La simulación permite crear un prototipo digital de una fábrica, almacén o red de suministro completa para probar diferentes condiciones antes de implementar cambios reales. Se aplica en tres horizontes: estratégico (1-5 años, ej. dónde construir una planta), táctico (1 mes-1 año, ej. gestión de incertidumbre de demanda) y operativo (1 día-1 mes, ej. layout de almacén). Permite detectar problemas de diseño antes de invertir, reducir stock de seguridad manteniendo el nivel de servicio, y evitar inversiones innecesarias mediante pruebas virtuales.

### MV-A17
- NODO DEL NUCLEO [definicion_alineacion_cadena_suministro]
    titulo: Definición y Alineación de la Cadena de Suministro con la Estrategia | mundo: core
    resumen: Una cadena de suministro es la red de empresas y actividades necesarias para diseñar, fabricar, entregar y usar un producto o servicio. Toda empresa participa en una o más cadenas de suministro y debe entender el rol que juega en ellas. La gestión de la cadena de suministro (SCM) es la coordinación sistémica de producción, inventario, ubicación y transporte entre los participantes para lograr el mejor balance entre capacidad de respuesta y eficiencia según el mercado servido. La estrategia de la empresa (competir por precio vs. por servicio/conveniencia) debe determinar el diseño de su cadena de suministro.
- NODO DEL MUNDO "logistica y entrega" [sistema_visibilidad_cadena_suministro_low_cost]
    titulo: Sistema de Visibilidad End-to-End con Componentes IT Simples | mundo: entrega
    resumen: Ante restricciones de tiempo y presupuesto, es posible construir un sistema de visibilidad de cadena de suministro combinando componentes IT básicos y accesibles (hojas de cálculo, archivos de texto, email, páginas web, bases de datos relacionales, scripts simples) en vez de comprar software costoso y complejo. La clave es identificar el patrón subyacente simple detrás de la aparente complejidad del problema (siguiendo la lógica de Sun Tzu: pocas notas, infinitas combinaciones) y usar esos componentes para crear una vista actualizada constantemente de inventario, producción y demanda, visible para todos los actores de la cadena.

### MV-A18
- NODO DEL NUCLEO [definicion_metas_engagement]
    titulo: Define tus metas y decisiones sobre el compromiso de tu equipo (engagement) | mundo: core
    resumen: Después de evaluar las actitudes de tu equipo, tienes que definir objetivos claros y tomar decisiones clave: qué le vas a pedir a las personas, si la participación será opcional u obligatoria, quién toma las decisiones y cómo vas a medir y evaluar el progreso con datos cuantitativos y cualitativos.
- NODO DEL MUNDO "gestion ambiental" [construccion_capacidad_empleados]
    titulo: Construcción de Capacidad mediante Entrenamiento en Sostenibilidad | mundo: environmental
    resumen: Las empresas exitosas desarrollan programas de entrenamiento formal, educación informal (brown-bag lunches, seminarios) y aprendizaje práctico ('learning by doing', como los Treasure Hunts de GE) para profundizar el conocimiento y la capacidad de acción de los empleados en sostenibilidad, adaptando el nivel de formación según el rol (todos los empleados, especialistas, líderes).

### MV-A19
- NODO DEL NUCLEO [definicion_metas_engagement]
    titulo: Define tus metas y decisiones sobre el compromiso de tu equipo (engagement) | mundo: core
    resumen: Después de evaluar las actitudes de tu equipo, tienes que definir objetivos claros y tomar decisiones clave: qué le vas a pedir a las personas, si la participación será opcional u obligatoria, quién toma las decisiones y cómo vas a medir y evaluar el progreso con datos cuantitativos y cualitativos.
- NODO DEL MUNDO "gestion ambiental" [programa_do_one_thing]
    titulo: Programa 'Haz Una Cosa' (Personal Sustainability Project) | mundo: environmental
    resumen: Un primer paso efectivo para involucrar empleados es pedirles que tomen una acción simple en su trabajo o en casa, como el Personal Sustainability Project (PSP) de Walmart, que en 2007 pidió a sus 1.3 millones de asociados en Estados Unidos que eligieran una acción personal de sostenibilidad. Estos programas generan beneficios intangibles como mejora de moral y también resultados de negocio concretos.

### MV-A20
- NODO DEL NUCLEO [driver_ubicacion]
    titulo: Driver de Ubicación: Centralización vs Descentralización de Instalaciones | mundo: core
    resumen: La ubicación se refiere al sitio geográfico de las instalaciones de producción y almacenamiento, y a qué actividades se realizan en cada una. El trade-off central es centralizar (economías de escala y eficiencia) vs. descentralizar (mayor cercanía a clientes/proveedores y capacidad de respuesta). Las decisiones de ubicación son altamente estratégicas porque comprometen inversiones de largo plazo y determinan las rutas posibles de flujo de producto hacia el cliente final.
- NODO DEL MUNDO "logistica y entrega" [driver_transporte]
    titulo: Driver de Transporte: Selección de Modo según Valor del Producto | mundo: entrega
    resumen: El transporte mueve materiales y productos entre instalaciones. Existen seis modos básicos: barco y ferrocarril (bajo costo, lento), tuberías (eficiente pero limitado a líquidos/gases), camiones (flexible, costo variable), avión (rápido y costoso) y transporte electrónico (instantáneo pero limitado a datos/energía). Como regla general, productos de alto valor deben usar redes de transporte que prioricen capacidad de respuesta, y productos de bajo valor (commodities) deben usar redes que prioricen eficiencia. El transporte puede representar hasta un tercio del costo operativo de la cadena de suministro.

### MV-A21
- NODO DEL NUCLEO [embudo_get_keep_grow]
    titulo: Embudo Get, Keep, Grow Customers | mundo: core
    resumen: El embudo Get, Keep, Grow resume la misión de toda startup en tres frases: construir grandes productos, conseguir, mantener y hacer crecer clientes, y ganar dinero de ellos. Aplica tanto a canales físicos como a web o mobile y describe el ciclo de vida completo de la relación con el cliente: adquisición y activación (Get), retención e interacción (Keep), y crecimiento vía up-sell, cross-sell y referidos (Grow). Es una de las hipótesis más críticas de cualquier startup porque sin clientes la empresa muere. Además, adquirir clientes suele ser la parte más costosa del negocio, por lo que conviene priorizar recursos entre las tres fases según su impacto real en el crecimiento sostenible.
- NODO DEL MUNDO "gestion de la calidad" [metricas_calidad]
    titulo: Métricas de Calidad | mundo: quality
    resumen: Proporcionan mediciones específicas y detalladas sobre un atributo del proyecto, producto o servicio, y cómo debe medirse. Se consultan en el proceso de aseguramiento de calidad y se comparan contra los resultados reales en el proceso de control de calidad para determinar si se requiere acción correctiva.

### MV-A22
- NODO DEL NUCLEO [erp_systems]
    titulo: Sistemas ERP (Enterprise Resource Planning) | mundo: core
    resumen: Los sistemas ERP recopilan datos de múltiples funciones de la empresa (finanzas, procura, manufactura, cumplimiento de órdenes, RRHH, logística) y ofrecen una vista orientada a procesos que atraviesa departamentos funcionales. Se enfocan principalmente en ejecutar y monitorear transacciones diarias, careciendo a menudo de capacidades analíticas avanzadas.
- NODO DEL MUNDO "logistica y entrega" [warehouse_management_system]
    titulo: Sistema de Gestión de Almacén (WMS) | mundo: entrega
    resumen: Los WMS soportan las operaciones diarias de almacén, gestionando niveles de inventario, ubicaciones de almacenamiento, y las actividades de picking, packing y envío para cumplir con las órdenes de los clientes de manera eficiente.

### MV-A23
- NODO DEL NUCLEO [estimate_at_completion_eac]
    titulo: Cuánto te va a costar terminar (Estimación al Completar o EAC) | mundo: core
    resumen: La Estimación al Completar (EAC) te dice cuánto vas a gastar en total cuando termines el proyecto, según cómo vas con los costos y el tiempo hasta ahora. Hay varias fórmulas según lo que asumas: si crees que tu ritmo de gasto actual (CPI) se va a mantener igual, usas EAC = BAC/CPI; si crees que tanto tu ritmo de gasto como tu ritmo de avance (SPI) van a afectar lo que falta, usas EAC = AC + [(BAC-EV)/(CPI×SPI)]. Además, el TCPI te muestra qué tan eficiente tienes que ser con el trabajo que te queda para no salirte del presupuesto.
- NODO DEL MUNDO "gestion de riesgos" [risk_audit]
    titulo: Auditoría de Riesgos | mundo: risk_management
    resumen: La Auditoría de Riesgos evalúa la efectividad del proceso de identificación de riesgos, las respuestas implementadas y el proceso general de gestión de riesgos. Se revisan los eventos de riesgo ocurridos, sus causas, las respuestas aplicadas y su éxito, así como el cumplimiento del proceso de gestión de riesgos y las herramientas utilizadas, identificando buenas prácticas y áreas de mejora.

### MV-A24
- NODO DEL NUCLEO [estrategia_circular_y_mecanismo_de_retorno]
    titulo: Elección de Estrategia Circular y Diseño del Mecanismo de Retorno | mundo: core
    resumen: Decidir que tu negocio será circular no dice todavía por dónde empieza. Antes de simular nada y antes de invertir, hay un acto propio: mirar el ciclo de vida que tu producto tiene HOY, compararlo con las cinco estrategias circulares y elegir en cuál de ellas tu negocio tiene más potencial real. Elegida la estrategia, hay que diseñar el mecanismo que la hace posible, el retorno del producto o su remanufactura, y recién entonces poner números: cuánto mejora la sostenibilidad y cuánto mueve tus costos de materiales y de logística. La elección y el mecanismo son el insumo de la simulación, no su resultado.
- NODO DEL MUNDO "logistica y entrega" [modelo_simulacion_cadena_suministro_circular]
    titulo: Simulación de Cadenas de Suministro Circulares y Sostenibles | mundo: entrega
    resumen: Antes de implementar una cadena de suministro física, es posible construir un modelo de simulación compuesto por entidades clave (productos, instalaciones, vehículos, rutas) para probar diferentes escenarios de oferta, demanda, costos y ubicaciones. Esto permite generar reportes de P&L y KPIs que sirven de base objetiva para comparar diseños alternativos antes de invertir capital, especialmente relevante en cadenas de suministro circulares (como recolección de aceite usado para biodiesel) donde el impacto ambiental y la eficiencia económica deben equilibrarse.

### MV-A25
- NODO DEL NUCLEO [estructura_de_costos]
    titulo: Bloque de Estructura de Costos | mundo: core
    resumen: Describe todos los costos incurridos para operar el modelo de negocio. Se distingue entre modelos dirigidos por costo (cost-driven, minimizando gastos) y dirigidos por valor (value-driven, priorizando la propuesta premium). También se clasifican en costos fijos, variables, economías de escala y economías de alcance.
- NODO DEL MUNDO "logistica y entrega" [modelado_simulacion_cadena_suministro]
    titulo: Modelado y Simulación de Cadena de Suministro con Cuatro Entidades | mundo: entrega
    resumen: Cualquier cadena de suministro puede modelarse definiendo cuatro tipos de entidades: Productos (costo, peso, volumen), Instalaciones (ubicación, costos operativos, tasas de producción/demanda), Vehículos (velocidad, capacidad, costos, rutas) y Rutas (destinos, distancias, frecuencias). Usando mapas digitales (Google Maps, etc.) estas entidades se colocan geográficamente y se simulan interacciones para detectar problemas de desempeño antes de implementarlos en la realidad, reduciendo riesgo y costo de errores.

### MV-A26
- NODO DEL NUCLEO [evaluacion_preparacion_tecnologica]
    titulo: Revisa si tu tecnología está lista para vender en línea (evaluación IT) | mundo: core
    resumen: Antes de lanzar tus operaciones en línea, evalúa tus necesidades y capacidades de tecnología (IT): tus sistemas actuales, qué partes de tu negocio conviene migrar, si conviene invertir en tecnología nueva según costo y beneficio, y qué medidas de seguridad necesitas frente a ataques informáticos.
- NODO DEL MUNDO "exportacion" [seleccion_dominio_web]
    titulo: Selección de Dirección Web (Dominio) para Mercados Internacionales | mundo: exportacion
    resumen: La elección del dominio web (URL) es clave para la presencia internacional: debe ser corto, simple y memorable. Se puede optar por dominios de código de país (ccTLD) localizados o por nombres de dominio internacionalizados (IDN) en el alfabeto o script del mercado objetivo, lo cual mejora reconocimiento de marca y posicionamiento en buscadores locales.

### MV-A27
- NODO DEL NUCLEO [formal_acceptance]
    titulo: Aceptación Formal de Entregables | mundo: core
    resumen: La Aceptación Formal documenta la aceptación de un entregable por parte del cliente u otro stakeholder, ya sea de forma periódica o al final del proyecto. Involucra dos etapas: verificar la corrección del entregable (Control de Calidad) y validar que cumple los criterios de aceptación acordados (Validar Alcance). Los entregables aceptados se firman formalmente y se remiten al proceso de Cierre del Proyecto o Fase.
- NODO DEL MUNDO "compras y proveedores" [contract_close_out]
    titulo: Cierre de Contrato | mundo: compras
    resumen: El Cierre de Contrato documenta el desempeño del proveedor para evaluaciones futuras, asegurando que todas las disputas se resuelvan, el producto sea aceptado y los pagos finales realizados antes de cerrar formalmente el contrato. Incluye análisis de desempeño del proveedor, registro de cambios contractuales y disputas, así como la fecha de finalización, firma y pago final.

### MV-A28
- NODO DEL NUCLEO [gestion_inventario]
    titulo: Gestión Eficiente de Inventario | mundo: core
    resumen: El inventario representa efectivo congelado que la empresa no puede usar para otros fines. El reto es minimizar el inventario sin generar quiebres de stock que insatisfagan a los clientes. Múltiples áreas de la empresa (ventas, ingeniería, producción) afectan los niveles de inventario a través de decisiones sobre personalización de productos, versiones y eficiencia de planta.
- NODO DEL MUNDO "logistica y entrega" [programacion_entregas_delivery_scheduling]
    titulo: Programación de Entregas: Directas vs. Milk Run | mundo: entrega
    resumen: Existen dos métodos principales de entrega: las entregas directas (de un origen a un destino, simples pero eficientes solo cuando el EOQ del receptor coincide con la carga de transporte completa) y las entregas milk run (de un origen a múltiples destinos o viceversa, más complejas de programar pero más eficientes en el uso del transporte y menor costo de recepción cuando las cantidades individuales son menores a una carga completa). La elección depende de la relación entre el EOQ de cada ubicación receptora y la capacidad del modo de transporte.

### MV-A29
- NODO DEL NUCLEO [gestion_pedidos_order_management]
    titulo: Gestión de Pedidos (Order Management) | mundo: core
    resumen: Proceso de transmitir información de pedidos desde clientes hacia atrás en la cadena de suministro (minoristas, distribuidores, proveedores de servicios, productores) y devolver información de fechas de entrega, sustituciones y pedidos pendientes. Se rige por cuatro principios: ingresar los datos del pedido una sola vez y capturarlos electrónicamente en la fuente original; automatizar el manejo de pedidos rutinarios y reservar la intervención humana para excepciones; hacer visible el estado del pedido a clientes y agentes de servicio; e integrar los sistemas de gestión de pedidos con otros sistemas relacionados (inventario, precios, facturación) para mantener la integridad de los datos.
- NODO DEL MUNDO "logistica y entrega" [programacion_entregas_delivery_scheduling]
    titulo: Programación de Entregas: Directas vs. Milk Run | mundo: entrega
    resumen: Existen dos métodos principales de entrega: las entregas directas (de un origen a un destino, simples pero eficientes solo cuando el EOQ del receptor coincide con la carga de transporte completa) y las entregas milk run (de un origen a múltiples destinos o viceversa, más complejas de programar pero más eficientes en el uso del transporte y menor costo de recepción cuando las cantidades individuales son menores a una carga completa). La elección depende de la relación entre el EOQ de cada ubicación receptora y la capacidad del modo de transporte.

### MV-A30
- NODO DEL NUCLEO [impacto_estado_resultados_en_balance]
    titulo: Cómo el Estado de Resultados Impacta el Balance General | mundo: core
    resumen: Todo cambio en el estado de resultados repercute en el balance: las ventas generan efectivo o cuentas por cobrar, los gastos reducen efectivo o aumentan pasivos acumulados, y la utilidad neta incrementa el patrimonio (vía utilidades retenidas) mientras una pérdida lo reduce. Decisiones operativas aparentemente simples (comprar inventario, atender nuevos clientes, adquirir equipo) tienen efectos complejos y a veces contradictorios sobre activos, pasivos y liquidez que deben analizarse integralmente.
- NODO DEL MUNDO "compras y proveedores" [efecto_bullwhip]
    titulo: Detectar y calcular el costo del efecto látigo en tu cadena de suministro | mundo: compras
    resumen: El efecto látigo (bullwhip) pasa cuando un cambio pequeño en lo que pide el cliente final se va agrandando a medida que sube por tu cadena de proveedores, y cada eslabón termina con una idea distinta de cuánta demanda real hay. Primero te quedas corto de inventario, después te sobra. Antes de gastar en resolverlo, tienes que medir qué tan grande es el efecto en tu caso y calcular cuánto te cuesta en producción, transporte, inventario y ventas que pierdes por no tener producto.

### MV-A31
- NODO DEL NUCLEO [industrial_robots_automation]
    titulo: Automatización con Robots Industriales | mundo: core
    resumen: Los robots industriales son manipuladores diseñados para mover materiales, partes y herramientas, y realizar tareas programadas en manufactura y producción. Su sofisticación y asequibilidad crecientes permiten que empresas de todos los tamaños los adopten para tareas peligrosas o repetitivas en fábricas y almacenes.
- NODO DEL MUNDO "logistica y entrega" [ia_en_supply_chain]
    titulo: Inteligencia Artificial Aplicada a la Cadena de Suministro | mundo: entrega
    resumen: La IA, potenciada por machine learning y modelos de lenguaje grandes (LLMs), te permite encontrar patrones en grandes volúmenes de datos y convertirlos en decisiones accionables en tiempo real. Transforma tres áreas clave: pronóstico de demanda (analizando históricos, tendencias de mercado y factores externos como clima o eventos sociales), optimización de rutas (con datos de tráfico en tiempo real para rutas dinámicas) y operaciones de almacén (automatización y visión computacional para manipular productos de formas variables). El objetivo no es reemplazar tu juicio sino complementarlo: la IA procesa el volumen de datos que a ti te resulta inmanejable desde el teléfono, y tú decides qué hacer con esas señales para ganar ventaja competitiva frente a métodos tradicionales que ya no alcanzan.

### MV-A32
- NODO DEL NUCLEO [information_driver_supply_chain]
    titulo: El Rol de la Información como Driver de la Cadena de Suministro | mundo: core
    resumen: La información es el conector entre todas las actividades de tu cadena de suministro y la base para tomar decisiones sobre los otros drivers: producción, inventario, ubicación y transporte. Cuanto más precisa, oportuna y completa sea la información que compartes con proveedores y clientes, mejores decisiones podrás tomar, maximizando la rentabilidad conjunta. La información cumple dos funciones: coordinar actividades diarias, como la programación de producción, los niveles de inventario y las rutas de transporte, y sustentar pronósticos de demanda, tanto a nivel táctico (cronogramas mensuales o trimestrales) como estratégico (decisiones de expansión o entrada y salida de mercados).
- NODO DEL MUNDO "logistica y entrega" [iot_big_data_supply_chain]
    titulo: IoT y Big Data para Trazabilidad de Supply Chain | mundo: entrega
    resumen: El Internet de las Cosas (IoT) conecta dispositivos embebidos en productos y equipos para enviar y recibir datos en tiempo real, generando volúmenes masivos de 'big data' que alimentan el análisis de patrones y tendencias en la cadena de suministro. Esta evolución va desde códigos de barras, pasando por RFID, hasta microchips embebidos en cualquier producto, permitiendo un seguimiento continuo y granular del movimiento de mercancías.

### MV-A33
- NODO DEL NUCLEO [innovacion_tipo_ii]
    titulo: Innovación Tipo II (Más grande/Más pequeño/Combinación) | mundo: core
    resumen: Técnica de generación de ideas basada en tres categorías simples: hacer algo más grande, más pequeño, o combinarlo con otra cosa. Es una habilidad que se puede aprender y mejorar con práctica, útil en sesiones de brainstorming para innovar productos, servicios o estrategias sin necesidad de ser un genio creativo nato.
- NODO DEL MUNDO "gestion de la calidad" [design_for_six_sigma_dfss]
    titulo: Design for Six Sigma (DFSS) y Metodología DMADV | mundo: quality
    resumen: DFSS es un enfoque sistemático para crear, al mismo tiempo, un producto nuevo y su proceso de producción con niveles de calidad cercanos a Six Sigma, minimizando fallas desde el inicio en lugar de corregirlas después. A diferencia de DMAIC, que mejora procesos existentes, DMADV (Definir, Medir, Analizar, Diseñar, Verificar) se usa cuando no hay un proceso previo que mejorar sino que debe crearse desde cero. Parte siempre de escuchar la voz del cliente y traducir sus necesidades en CTQs (Critical to Quality) medibles, evalúa varios conceptos de diseño con métodos estadísticos, detalla el diseño ganador y verifica que cumpla tanto las necesidades del negocio como del cliente antes de pasar a producción a escala completa.

### MV-A34
- NODO DEL NUCLEO [innovacion_tipo_ii]
    titulo: Innovación Tipo II (Más grande/Más pequeño/Combinación) | mundo: core
    resumen: Técnica de generación de ideas basada en tres categorías simples: hacer algo más grande, más pequeño, o combinarlo con otra cosa. Es una habilidad que se puede aprender y mejorar con práctica, útil en sesiones de brainstorming para innovar productos, servicios o estrategias sin necesidad de ser un genio creativo nato.
- NODO DEL MUNDO "gestion de la calidad" [juran_quality_by_design]
    titulo: Modelo Juran de Calidad por Diseño (Quality by Design) | mundo: quality
    resumen: Este modelo es el primer proceso de la Trilogía de Juran, vigente desde 1986, y te sirve para diseñar un producto, servicio o proceso nuevo de forma simple y económica, sin necesidad de herramientas estadísticas complejas. Cubre tu doble responsabilidad como emprendedor: definir las características que satisfacen a tu cliente y asegurar que el proceso para producirlas sea viable y no genere desperdicio. Antes de empezar, decide si lo usarás como una práctica continua en tu negocio o para un proyecto puntual. Consta de seis pasos secuenciales, desde establecer metas hasta transferir el diseño a operaciones, y cada paso debe dejar una salida documentada antes de avanzar al siguiente.

### MV-A35
- NODO DEL NUCLEO [manufactura_aditiva_bajo_demanda]
    titulo: Manufactura Aditiva (Impresión 3D) para Producción Bajo Demanda | mundo: core
    resumen: La impresión 3D o manufactura aditiva permite crear productos por capas a partir de materia prima común (plástico, polvo metálico), fabricando bajo demanda en lugar de predecir y almacenar inventario de múltiples variantes. Esto reduce costos de inventario y mejora el nivel de servicio al cliente al minimizar quiebres de stock.
- NODO DEL MUNDO "logistica y entrega" [simulacion_de_operaciones_supply_chain]
    titulo: Modelado de Simulación para Decisiones de Supply Chain | mundo: entrega
    resumen: La simulación permite crear un prototipo digital de una fábrica, almacén o red de suministro completa para probar diferentes condiciones antes de implementar cambios reales. Se aplica en tres horizontes: estratégico (1-5 años, ej. dónde construir una planta), táctico (1 mes-1 año, ej. gestión de incertidumbre de demanda) y operativo (1 día-1 mes, ej. layout de almacén). Permite detectar problemas de diseño antes de invertir, reducir stock de seguridad manteniendo el nivel de servicio, y evitar inversiones innecesarias mediante pruebas virtuales.

### MV-A36
- NODO DEL NUCLEO [marco_analisis_mercado_cadena_suministro]
    titulo: Cómo entender tu mercado para encontrar oportunidades en tu cadena de suministro | mundo: core
    resumen: Antes de decidir dónde enfocar tus esfuerzos, necesitas entender en qué tipo de mercado te mueves: uno maduro, uno en desarrollo o uno estable. Cada tipo te exige destacar en algo distinto: atención al cliente, eficiencia interna, capacidad de adaptarte a la demanda o desarrollo de producto. Tu tarea es identificar en cuál de estas áreas necesitas ser mejor que tu competencia.
- NODO DEL MUNDO "compras y proveedores" [compartir_datos_cadena_suministro]
    titulo: Compartición de Datos entre Empresas de la Cadena de Suministro | mundo: compras
    resumen: Compartir datos de demanda, decisiones y métricas de desempeño entre las empresas de una cadena de suministro mejora la toma de decisiones colectiva y reduce distorsiones como el efecto látigo (bullwhip effect). Aunque existe reticencia por temor a filtrar información confidencial a competidores, las cadenas que colaboran eficientemente ganan cuota de mercado frente a las que no lo hacen, ya que la competencia se traslada de empresa-contra-empresa a cadena-de-suministro-contra-cadena-de-suministro.

### MV-A37
- NODO DEL NUCLEO [mecanismo_resolucion_disputas]
    titulo: Establecer Mecanismo Informal de Resolución de Disputas de Garantía | mundo: core
    resumen: Esta es una figura del derecho estadounidense (Magnuson-Moss Warranty Act) sobre garantías de productos. Antes de que un cliente te demande por incumplir la garantía, puedes ofrecerle un mecanismo informal para resolver el reclamo, como conciliación, mediación o arbitraje, gestionado por un tercero imparcial (por ejemplo, el Better Business Bureau) o por alguien de tu propio negocio dedicado a esto. Si decides exigir que el cliente use este mecanismo antes de poder demandarte, la ley te obliga a cumplir reglas de la FTC (Dispute Resolution Rule): debe ser gratuito para el cliente, imparcial, con procedimientos escritos, resolver en 40 días y someterse a auditoría anual. Los conceptos son útiles en cualquier país, pero confirma la norma vigente donde vendes.
- NODO DEL MUNDO "compras y proveedores" [contract_close_out]
    titulo: Cierre de Contrato | mundo: compras
    resumen: El Cierre de Contrato documenta el desempeño del proveedor para evaluaciones futuras, asegurando que todas las disputas se resuelvan, el producto sea aceptado y los pagos finales realizados antes de cerrar formalmente el contrato. Incluye análisis de desempeño del proveedor, registro de cambios contractuales y disputas, así como la fecha de finalización, firma y pago final.

### MV-A38
- NODO DEL NUCLEO [plan_gestion_adquisiciones]
    titulo: Plan para comprar y contratar lo que necesitas de afuera (Plan de Gestión de Adquisiciones) | mundo: core
    resumen: Define cómo vas a conseguir afuera lo que tu proyecto necesita comprar o contratar: qué tipo de contrato usarás, quién decide qué, con qué criterios eliges a un proveedor, cómo se conecta esa compra con tu cronograma y tu plan de tareas (WBS), y cómo vas a medir si el proveedor cumple.
- NODO DEL MUNDO "compras y proveedores" [procurement_audit]
    titulo: Auditoría de Adquisiciones | mundo: compras
    resumen: La Auditoría de Adquisiciones es una revisión de los contratos y procesos de contratación para verificar su completitud, precisión y efectividad. Evalúa el desempeño del proveedor (alcance, calidad, cronograma, costo, facilidad de trabajo) y el proceso de gestión de adquisiciones en sí, generando información útil para mejorar contratos futuros y alimentar las Lecciones Aprendidas.

### MV-A39
- NODO DEL NUCLEO [plan_gestion_calidad]
    titulo: Plan de Gestión de Calidad | mundo: core
    resumen: Componente del plan de gestión del proyecto que describe cómo se cumplirán los requisitos de calidad. Incluye roles y responsabilidades, y enfoques de aseguramiento, control y mejora de calidad, así como herramientas, procesos y políticas relacionadas.
- NODO DEL MUNDO "gestion de la calidad" [metricas_calidad]
    titulo: Métricas de Calidad | mundo: quality
    resumen: Proporcionan mediciones específicas y detalladas sobre un atributo del proyecto, producto o servicio, y cómo debe medirse. Se consultan en el proceso de aseguramiento de calidad y se comparan contra los resultados reales en el proceso de control de calidad para determinar si se requiere acción correctiva.

### MV-A40
- NODO DEL NUCLEO [plan_gestion_calidad]
    titulo: Plan de Gestión de Calidad | mundo: core
    resumen: Componente del plan de gestión del proyecto que describe cómo se cumplirán los requisitos de calidad. Incluye roles y responsabilidades, y enfoques de aseguramiento, control y mejora de calidad, así como herramientas, procesos y políticas relacionadas.
- NODO DEL MUNDO "gestion de la calidad" [quality_audit]
    titulo: Auditoría de Calidad | mundo: quality
    resumen: Revisión estructurada e independiente de procesos, documentos o productos del proyecto para verificar cumplimiento de políticas y plan de calidad, identificando buenas prácticas y áreas de mejora.

### MV-A41
- NODO DEL NUCLEO [planificacion_gobierno_organizaciones_familiares]
    titulo: Cómo organizar el mando y la sucesión en un negocio familiar (gobierno corporativo) | mundo: core
    resumen: Si tu negocio es familiar, como más del 70% de las organizaciones registradas en el mundo, necesitas pensar el mando de otra manera, sobre todo cuando te acercas al momento de dejar el timón. Busca ayuda externa de alguien que conozca el tema para armar un plan maestro que incluya un consejo familiar, una junta directiva profesional y la entrada gradual de familiares, gerentes clave y directores externos independientes con la formación necesaria.
- NODO DEL MUNDO "gestion de la calidad" [evaluacion_desempeno_junta_directiva]
    titulo: Evaluación del Desempeño de la Junta Directiva Basada en Resultados | mundo: quality
    resumen: Método para evaluar cómo la junta o el consejo que te asesora contribuye a los resultados de tu negocio. Se usa una escala de cuatro niveles (Entendimiento, Primeros pasos, Implementación, Liderazgo) para calificar ocho puntos clave: resultados financieros, acceso a capital, indicadores de desempeño, valor de marca, capital intelectual, gestión de riesgos, evaluación de las personas con interés en el negocio y percepción de la comunidad. Esta forma de mejorar tomando conciencia te ayuda a ver en qué áreas conviene fortalecer el gobierno de tu negocio.

### MV-A42
- NODO DEL NUCLEO [planificacion_gobierno_organizaciones_familiares]
    titulo: Cómo organizar el mando y la sucesión en un negocio familiar (gobierno corporativo) | mundo: core
    resumen: Si tu negocio es familiar, como más del 70% de las organizaciones registradas en el mundo, necesitas pensar el mando de otra manera, sobre todo cuando te acercas al momento de dejar el timón. Busca ayuda externa de alguien que conozca el tema para armar un plan maestro que incluya un consejo familiar, una junta directiva profesional y la entrada gradual de familiares, gerentes clave y directores externos independientes con la formación necesaria.
- NODO DEL MUNDO "gestion de la calidad" [familia_normas_iso_9000]
    titulo: Familia de Normas ISO 9000 | mundo: quality
    resumen: ISO 9000 es una familia de normas internacionales de gestion de calidad, creada por el Comite Tecnico 176 de ISO, aplicable a cualquier producto, servicio o negocio sin importar su tamano o sector. Son normas no prescriptivas: definen que debe existir en el sistema de gestion, no como implementarlo, y combinan estandares de producto (especificaciones tecnicas) con estandares de sistema de gestion. La version ISO 9001:2015 incorporo un enfoque basado en riesgos, nuevas exigencias sobre el contexto de tu negocio y las partes interesadas, y mayor peso al liderazgo y a la gestion de relaciones mas alla del cliente tradicional.

### MV-A43
- NODO DEL NUCLEO [posicionamiento_est]
    titulo: Elige en qué vas a ser el mejor (y renuncia al resto) | mundo: core
    resumen: Según un estudio de McMillan Doolittle, tienes que ser el mejor en al menos una de cinco cosas: el que tiene más variedad, el más barato, el más fácil de usar, el más rápido o el más de moda. Si intentas destacar en más de dos a la vez, terminas siendo mediocre en todas. Elegir en qué destacar significa aceptar que vas a sacrificar otras cosas a propósito.
- NODO DEL MUNDO "franquicias" [calificacion_prospectos_marketing]
    titulo: Diseñar el Mensaje para Calificar y Descalificar Prospectos | mundo: franquicias
    resumen: Los compradores de franquicia buscan activamente razones para eliminar opciones de su lista corta (solo consideran entre 6 y 12 franquiciadores). El mensaje de marketing debe comunicar claramente los requisitos de inversión y perfil para autodescalificar a los no calificados antes de la llamada telefónica, ahorrando tiempo a ambas partes.

### MV-A44
- NODO DEL NUCLEO [posicionamiento_est]
    titulo: Elige en qué vas a ser el mejor (y renuncia al resto) | mundo: core
    resumen: Según un estudio de McMillan Doolittle, tienes que ser el mejor en al menos una de cinco cosas: el que tiene más variedad, el más barato, el más fácil de usar, el más rápido o el más de moda. Si intentas destacar en más de dos a la vez, terminas siendo mediocre en todas. Elegir en qué destacar significa aceptar que vas a sacrificar otras cosas a propósito.
- NODO DEL MUNDO "franquicias" [propuesta_valor_franquicia]
    titulo: Desarrollar la Propuesta de Valor Integral del Sistema de Franquicia | mundo: franquicias
    resumen: Lo que realmente compra un franquiciado no es la receta o el producto, sino el sistema completo: selección de sitios, negociación de arrendamiento, publicidad, servicio al cliente, branding, compras, precios, contratación, capacitación y control de calidad. La propuesta de valor debe combinar factores diferenciadores (inversión, mercado objetivo, territorio, soporte, estructura de tarifas) en un paquete coherente que justifique el pago de regalías.

### MV-A45
- NODO DEL NUCLEO [precios_todos_los_dias_bajos]
    titulo: Estrategia de Precios Estables (Everyday Low Prices) | mundo: core
    resumen: Las fluctuaciones de precio (promociones, descuentos) generan compras anticipadas (forward buying) y oleadas de demanda difíciles de gestionar. Mantener precios estables y predecibles hace que los clientes compren según necesidad real, facilitando el pronóstico de demanda y la eficiencia de la cadena.
- NODO DEL MUNDO "logistica y entrega" [drum_buffer_rope]
    titulo: Modelo Drum-Buffer-Rope para Sincronizar la Cadena de Suministro | mundo: entrega
    resumen: Modelo que sincroniza toda la cadena de suministro como una sola entidad, alineada al ritmo real de la demanda del mercado (el 'tambor'). Cada empresa gestiona la incertidumbre mediante buffers de inventario o capacidad productiva, y comparten datos de demanda (la 'cuerda') que los mantiene sincronizados, minimizando el efecto látigo (bullwhip effect).

### MV-A46
- NODO DEL NUCLEO [principio_humano_en_el_loop]
    titulo: Principio 2: Sé tú quien decide, no la IA (mantente en el ciclo) | mundo: core
    resumen: La IA generativa no sabe nada en realidad: adivina la palabra más probable que sigue, y muchas veces prioriza sonar convincente antes que ser exacta. Por eso a veces te da respuestas incorrectas dichas con total seguridad (alucinaciones). No le entregues decisiones importantes sin revisarlas tú mismo: verifica y cuestiona lo que te devuelve, sobre todo en lo que más te puede costar si sale mal, como plata, temas legales, salud o el trato con tus clientes.
- NODO DEL MUNDO "seguridad digital" [gestion_riesgo_seguridad_ia]
    titulo: Gestión de Riesgos de Seguridad en IA (Prompt Injection y Jailbreaking) | mundo: seguridad_digital
    resumen: Los sistemas de IA pueden ser manipulados mediante técnicas como 'prompt injection' (instrucciones ocultas en contenido web o documentos que la IA lee) y 'jailbreaking' (convencer a la IA de romper sus reglas mediante escenarios ficticios o roleplay). Esto representa un riesgo real para cualquier negocio que integre IA con acceso a datos externos, atención al cliente automatizada o generación de contenido, ya que actores malintencionados pueden explotar estas vulnerabilidades para phishing, desinformación o fraude.

### MV-A47
- NODO DEL NUCLEO [prompting_cadena_de_pensamiento]
    titulo: Prompting en Cadena de Pensamiento (Chain-of-Thought) | mundo: core
    resumen: Técnica que consiste en pedir a la IA que razone paso a paso, dividiendo una tarea compleja en subpasos secuenciales (listar opciones, criticarlas, compararlas en una tabla, elegir la mejor). Esto mejora significativamente la calidad y precisión de las respuestas frente a preguntas directas de una sola vez, permitiendo además revisar y refinar cada etapa del proceso.
- NODO DEL MUNDO "logistica y entrega" [ia_en_supply_chain]
    titulo: Inteligencia Artificial Aplicada a la Cadena de Suministro | mundo: entrega
    resumen: La IA, potenciada por machine learning y modelos de lenguaje grandes (LLMs), te permite encontrar patrones en grandes volúmenes de datos y convertirlos en decisiones accionables en tiempo real. Transforma tres áreas clave: pronóstico de demanda (analizando históricos, tendencias de mercado y factores externos como clima o eventos sociales), optimización de rutas (con datos de tráfico en tiempo real para rutas dinámicas) y operaciones de almacén (automatización y visión computacional para manipular productos de formas variables). El objetivo no es reemplazar tu juicio sino complementarlo: la IA procesa el volumen de datos que a ti te resulta inmanejable desde el teléfono, y tú decides qué hacer con esas señales para ganar ventaja competitiva frente a métodos tradicionales que ya no alcanzan.

### MV-A48
- NODO DEL NUCLEO [pronostico_de_demanda_variables]
    titulo: Pronóstico de Demanda: Cuatro Variables Clave | mundo: core
    resumen: Todo pronóstico de demanda depende de cuatro variables: Oferta (número de proveedores y lead times), Demanda (crecimiento, estacionalidad, madurez del mercado), Características del producto (si es sustituible, complementario, nuevo o maduro) y Entorno competitivo (participación de mercado, promociones, guerras de precios). Cuanta más incertidumbre haya en estas variables, más difícil y menos preciso será el pronóstico.
- NODO DEL MUNDO "logistica y entrega" [gestion_rationing_shortage_gaming]
    titulo: Gestión del Racionamiento y Shortage Gaming | mundo: entrega
    resumen: Cuando la demanda supera la oferta, los fabricantes racionan producto según pedidos recibidos, lo que incentiva a distribuidores a inflar artificialmente sus órdenes para recibir más asignación (shortage gaming). Esto distorsiona la demanda real percibida en toda la cadena de suministro.

### MV-A49
- NODO DEL NUCLEO [reglas_gestion_riesgo_gambling]
    titulo: Las Cinco Reglas de Gestión de Riesgo (Gambling Rules) | mundo: core
    resumen: Basado en la teoría de apuestas, la gestión de nuevos productos es esencialmente gestión de riesgo, entendido como la combinación de monto en juego e incertidumbre. Cinco reglas la guían: mantener bajas las apuestas cuando la incertidumbre es alta, incrementar el monto invertido solo cuando la incertidumbre baja, dividir el proceso en etapas comprando opciones en vez de jugar todo o nada, pagar por información que reduzca la incertidumbre antes de aumentar el gasto, y prever puntos de salida (gates) donde puedas abandonar el proyecto a tiempo. Estas reglas te permiten calibrar cuánto arriesgar en cada momento del proyecto según lo que realmente sabes, en vez de comprometer recursos grandes sobre supuestos no verificados.
- NODO DEL MUNDO "logistica y entrega" [cadena_suministro_respuesta_desastres]
    titulo: Cadenas de Suministro para Respuesta a Desastres | mundo: entrega
    resumen: Las cadenas de suministro de respuesta a desastres (DR) enfrentan alta imprevisibilidad y organización ad hoc, sin autoridad centralizada clara. A diferencia de las cadenas comerciales, requieren mayores niveles de inventario de contingencia (surge capacity), planificación pre-desastre, y entrenamiento colaborativo entre organizaciones diversas (gobierno, ONG, militares, empresas) que normalmente no trabajan juntas.

### MV-A50
- NODO DEL NUCLEO [sales_operations_planning]
    titulo: Planificación de Ventas y Operaciones (S&OP) | mundo: core
    resumen: El S&OP es un proceso de negocio cross-funcional (ventas, operaciones, finanzas, desarrollo de producto) que se ejecuta mensualmente para mantener el balance entre oferta y demanda a nivel agregado. Toma un enfoque 'outside-in', considerando primero factores externos (clientes, competidores) antes de ajustar planes internos, y vincula el plan estratégico con la ejecución diaria.
- NODO DEL MUNDO "compras y proveedores" [colaboracion_cadena_suministro]
    titulo: Iniciar la Colaboración en la Cadena de Suministro | mundo: compras
    resumen: El primer paso para reducir el efecto látigo es medirlo dentro de la propia empresa, comparando el volumen y frecuencia de pedidos recibidos de clientes contra los pedidos realizados a proveedores. Compartir datos de inventario y demanda con socios comerciales (como hacen Walmart, Dell y P&G) permite decisiones más eficientes en toda la cadena, en lugar de que cada empresa optimice de forma aislada.

### MV-A51
- NODO DEL NUCLEO [seleccion_de_proveedores_por_costo_total]
    titulo: Seleccion de Proveedores por Costo Total Ponderado | mundo: core
    resumen: Elegir proveedor por el precio unitario mas bajo es decidir con la mitad de la informacion. Lo que de verdad cuesta trabajar con un proveedor incluye la calidad que entrega, su cumplimiento y el control que tiene sobre sus procesos, y esos criterios no pesan igual en todos los negocios. El acto propio es armar la comparacion antes de firmar: definir que criterios cualitativos importan, repartir el peso entre el costo monetario y esos criterios, calcular el costo total ponderado de cada proveedor y compararlos con esa cifra en vez de con el precio de lista. Y hay una decision que va con la misma logica: concentrar el volumen en menos proveedores da poder de negociacion, asi que la lista de preferidos se arma a proposito y no por acumulacion.
- NODO DEL MUNDO "compras y proveedores" [negociacion_contratos_proveedores]
    titulo: Negociación de Contratos con Proveedores | mundo: compras
    resumen: La negociación de contratos con proveedores debe equilibrar precio unitario con otros servicios de valor agregado como conexiones electrónicas, entregas frecuentes y precisión en pedidos. Deben especificarse metas de desempeño, penalizaciones y formas de pago (mayor margen en precio, pagos separados o combinación). Entender la cultura y etiqueta de negocios del proveedor es clave para negociaciones interculturales efectivas.

### MV-A52
- NODO DEL NUCLEO [sop_colaborativo]
    titulo: Proceso Colaborativo S&OP (Sales and Operations Planning) en 5 Pasos | mundo: core
    resumen: Un proceso simplificado de S&OP guiado por simulaciones, ejecutado en ciclos (ej. cada 30 días): (1) Pronóstico de demanda y precios, (2) Plan de demanda por instalación, (3) Plan de suministro (producción/rutas), (4) Modelado y simulación para detectar discrepancias entre demanda y suministro, y (5) Ajuste y consenso del plan operativo final. Este proceso convierte datos en un plan operativo compartido y revisado continuamente por todos los actores de la cadena.
- NODO DEL MUNDO "logistica y entrega" [plataforma_colaboracion_tiempo_real]
    titulo: Plataforma de Colaboración en Tiempo Real para Cadena de Suministro | mundo: entrega
    resumen: Una plataforma basada en la nube que ofrece visibilidad casi en tiempo real a todos los actores de la cadena de suministro (fabricantes, logística, distribuidores, retailers) permite que cada parte identifique problemas y actúe sin esperar instrucciones de una autoridad central. Se combina con sesiones de 'colaboración masiva' (crowdsourcing) donde múltiples empresas ajustan en vivo el diseño de la cadena, corren simulaciones, y llegan a consenso sobre el plan operativo, generando compromiso genuino de todas las partes.

### MV-A53
- NODO DEL NUCLEO [stakeholder_register]
    titulo: Lista de las personas que le importan a tu proyecto (Stakeholder Register) | mundo: core
    resumen: Es un documento vivo donde anotas quiénes se ven afectados por tu proyecto o negocio, tanto dentro como fuera. Para cada uno registras su rol, qué necesita, qué espera de ti, cuánta influencia tiene y cómo lo clasificas. Te sirve para saber a quién hablarle, cuándo y de qué manera, durante todo el recorrido.
- NODO DEL MUNDO "gestion de riesgos" [risk_audit]
    titulo: Auditoría de Riesgos | mundo: risk_management
    resumen: La Auditoría de Riesgos evalúa la efectividad del proceso de identificación de riesgos, las respuestas implementadas y el proceso general de gestión de riesgos. Se revisan los eventos de riesgo ocurridos, sus causas, las respuestas aplicadas y su éxito, así como el cumplimiento del proceso de gestión de riesgos y las herramientas utilizadas, identificando buenas prácticas y áreas de mejora.

### MV-A54
- NODO DEL NUCLEO [supply_chain_management_systems]
    titulo: Sistemas de Gestión de Cadena de Suministro (SCM) | mundo: core
    resumen: Los sistemas SCM son suites de aplicaciones integradas (planificación avanzada, planificación de transporte, planificación de demanda, gestión de inventario) que dependen de datos de sistemas ERP y ofrecen capacidades analíticas para la toma de decisiones estratégicas y tácticas en la cadena de suministro.
- NODO DEL MUNDO "logistica y entrega" [ia_en_supply_chain]
    titulo: Inteligencia Artificial Aplicada a la Cadena de Suministro | mundo: entrega
    resumen: La IA, potenciada por machine learning y modelos de lenguaje grandes (LLMs), te permite encontrar patrones en grandes volúmenes de datos y convertirlos en decisiones accionables en tiempo real. Transforma tres áreas clave: pronóstico de demanda (analizando históricos, tendencias de mercado y factores externos como clima o eventos sociales), optimización de rutas (con datos de tráfico en tiempo real para rutas dinámicas) y operaciones de almacén (automatización y visión computacional para manipular productos de formas variables). El objetivo no es reemplazar tu juicio sino complementarlo: la IA procesa el volumen de datos que a ti te resulta inmanejable desde el teléfono, y tú decides qué hacer con esas señales para ganar ventaja competitiva frente a métodos tradicionales que ya no alcanzan.

### MV-A55
- NODO DEL NUCLEO [teoria_de_restricciones]
    titulo: Teoría de Restricciones (Theory of Constraints) | mundo: core
    resumen: Desarrollada por Eliyahu Goldratt, sostiene que todo sistema tiene al menos una restricción (cuello de botella) que determina su rendimiento total. En vez de intentar eliminar constantemente nuevas restricciones, es mejor identificarlas y gestionarlas deliberadamente. El objetivo es 'aumentar el throughput mientras se reduce simultáneamente inventario y gastos operativos'.
- NODO DEL MUNDO "logistica y entrega" [drum_buffer_rope]
    titulo: Modelo Drum-Buffer-Rope para Sincronizar la Cadena de Suministro | mundo: entrega
    resumen: Modelo que sincroniza toda la cadena de suministro como una sola entidad, alineada al ritmo real de la demanda del mercado (el 'tambor'). Cada empresa gestiona la incertidumbre mediante buffers de inventario o capacidad productiva, y comparten datos de demanda (la 'cuerda') que los mantiene sincronizados, minimizando el efecto látigo (bullwhip effect).

### MV-A56
- NODO DEL NUCLEO [trade_off_responsividad_eficiencia]
    titulo: Balance entre Capacidad de Respuesta y Eficiencia | mundo: core
    resumen: Cada decisión en la cadena de suministro (producción, inventario, ubicación, transporte, información) implica un trade-off entre ser más responsivo (rápido, flexible, capaz de atender picos de demanda) o más eficiente (bajo costo, alta utilización de activos). El mercado que se sirve determina qué extremo priorizar: mercados masivos sensibles al precio requieren eficiencia; mercados que valoran servicio y conveniencia requieren capacidad de respuesta.
- NODO DEL MUNDO "logistica y entrega" [driver_transporte]
    titulo: Driver de Transporte: Selección de Modo según Valor del Producto | mundo: entrega
    resumen: El transporte mueve materiales y productos entre instalaciones. Existen seis modos básicos: barco y ferrocarril (bajo costo, lento), tuberías (eficiente pero limitado a líquidos/gases), camiones (flexible, costo variable), avión (rápido y costoso) y transporte electrónico (instantáneo pero limitado a datos/energía). Como regla general, productos de alto valor deben usar redes de transporte que prioricen capacidad de respuesta, y productos de bajo valor (commodities) deben usar redes que prioricen eficiencia. El transporte puede representar hasta un tercio del costo operativo de la cadena de suministro.

### MV-A57
- NODO DEL NUCLEO [vehiculos_autonomos_drones_supply_chain]
    titulo: Drones y Vehículos Autónomos en la Cadena de Suministro | mundo: core
    resumen: Un dron es cualquier vehículo sin conductor que opera de forma remota o autónoma, ya sea volando, caminando, conduciendo, flotando o nadando. Puedes usarlo para mover productos en distintos tramos de tu cadena de suministro: camiones autónomos entre fábricas y almacenes, o drones aéreos y furgonetas autónomas para la entrega final al cliente. Todos se pueden conectar a un sistema central que programa y coordina sus rutas. Bien aplicada, esta tecnología te ayuda a reducir costos y tiempos de entrega en tramos con alto volumen repetitivo.
- NODO DEL MUNDO "logistica y entrega" [ia_en_supply_chain]
    titulo: Inteligencia Artificial Aplicada a la Cadena de Suministro | mundo: entrega
    resumen: La IA, potenciada por machine learning y modelos de lenguaje grandes (LLMs), te permite encontrar patrones en grandes volúmenes de datos y convertirlos en decisiones accionables en tiempo real. Transforma tres áreas clave: pronóstico de demanda (analizando históricos, tendencias de mercado y factores externos como clima o eventos sociales), optimización de rutas (con datos de tráfico en tiempo real para rutas dinámicas) y operaciones de almacén (automatización y visión computacional para manipular productos de formas variables). El objetivo no es reemplazar tu juicio sino complementarlo: la IA procesa el volumen de datos que a ti te resulta inmanejable desde el teléfono, y tú decides qué hacer con esas señales para ganar ventaja competitiva frente a métodos tradicionales que ya no alcanzan.

### MV-A58
- NODO DEL NUCLEO [vehiculos_autonomos_drones_supply_chain]
    titulo: Drones y Vehículos Autónomos en la Cadena de Suministro | mundo: core
    resumen: Un dron es cualquier vehículo sin conductor que opera de forma remota o autónoma, ya sea volando, caminando, conduciendo, flotando o nadando. Puedes usarlo para mover productos en distintos tramos de tu cadena de suministro: camiones autónomos entre fábricas y almacenes, o drones aéreos y furgonetas autónomas para la entrega final al cliente. Todos se pueden conectar a un sistema central que programa y coordina sus rutas. Bien aplicada, esta tecnología te ayuda a reducir costos y tiempos de entrega en tramos con alto volumen repetitivo.
- NODO DEL MUNDO "logistica y entrega" [simulacion_de_operaciones_supply_chain]
    titulo: Modelado de Simulación para Decisiones de Supply Chain | mundo: entrega
    resumen: La simulación permite crear un prototipo digital de una fábrica, almacén o red de suministro completa para probar diferentes condiciones antes de implementar cambios reales. Se aplica en tres horizontes: estratégico (1-5 años, ej. dónde construir una planta), táctico (1 mes-1 año, ej. gestión de incertidumbre de demanda) y operativo (1 día-1 mes, ej. layout de almacén). Permite detectar problemas de diseño antes de invertir, reducir stock de seguridad manteniendo el nivel de servicio, y evitar inversiones innecesarias mediante pruebas virtuales.

## B: puentes aprobados cuya ancla sale del nucleo. Elige un ANCLA DEL NUCLEO nueva

### MV-B01
- NODO DEL MUNDO "gestion ambiental" QUE NECESITA UNA PUERTA DESDE EL NUCLEO [optimizacion_tecnologia_cadena_suministro]
    titulo: Optimización de la Cadena de Suministro con Tecnología | mundo: environmental
    resumen: Las nuevas tecnologías permiten a las empresas tener una visión integrada de los impactos de la cadena de suministro. El software de análisis de ciclo de vida y los dashboards permiten comparar el desempeño de proveedores a lo largo del tiempo sin necesidad de recolectar información directamente. Aberdeen Group identifica cuatro áreas clave: dashboards verdes basados en roles, activos sostenibles/eficientes, seguimiento de residuos y transporte/logística sostenible.
- CANDIDATOS A ANCLA (nucleo)
  1. [supply_chain_management_systems]
    titulo: Sistemas de Gestión de Cadena de Suministro (SCM) | mundo: core
    resumen: Los sistemas SCM son suites de aplicaciones integradas (planificación avanzada, planificación de transporte, planificación de demanda, gestión de inventario) que dependen de datos de sistemas ERP y ofrecen capacidades analíticas para la toma de decisiones estratégicas y tácticas en la cadena de suministro.
  2. [scor_model_operaciones]
    titulo: Modelo SCOR: Marco de Operaciones de Cadena de Suministro | mundo: core
    resumen: El modelo SCOR (Supply Chain Operations Reference) es un marco estandarizado y reconocido mundialmente para analizar y mejorar el desempeño de la cadena de suministro. Organiza las operaciones en seis procesos de alto nivel: Planificar, Abastecer, Fabricar, Entregar, Devolver y Habilitar. Provee un lenguaje común, métricas estándar (KPIs de confiabilidad, capacidad de respuesta, agilidad, costo y gestión de activos) y permite benchmarking entre empresas. La versión más reciente, SCOR DS, incorpora resiliencia, sostenibilidad y procesos digitales.
  3. [information_driver_supply_chain]
    titulo: El Rol de la Información como Driver de la Cadena de Suministro | mundo: core
    resumen: La información es el conector entre todas las actividades de tu cadena de suministro y la base para tomar decisiones sobre los otros drivers: producción, inventario, ubicación y transporte. Cuanto más precisa, oportuna y completa sea la información que compartes con proveedores y clientes, mejores decisiones podrás tomar, maximizando la rentabilidad conjunta. La información cumple dos funciones: coordinar actividades diarias, como la programación de producción, los niveles de inventario y las rutas de transporte, y sustentar pronósticos de demanda, tanto a nivel táctico (cronogramas mensuales o trimestrales) como estratégico (decisiones de expansión o entrada y salida de mercados).
  4. [tecnologia_como_medio_no_fin]
    titulo: La tecnología es un medio, no un fin | mundo: core
    resumen: La tecnología en tu cadena de suministro solo vale si te permite entregar el servicio y los precios que tus clientes valoran. No inviertas en tecnología porque sea sofisticada o nueva. Evalúa cada inversión tecnológica según su capacidad real de mejorar el servicio a tus clientes y bajar tus costos de forma rentable.
  5. [ejecucion_incremental_transicion_tecnologica]
    titulo: Transición Tecnológica mediante Pasos Incrementales | mundo: core
    resumen: La tecnología es un medio, no un fin: solo importa en la medida en que permite entregar servicio de valor a los clientes de forma rentable. Las transiciones exitosas hacia nuevas capacidades de cadena de suministro casi siempre involucran una serie de pasos incrementales, comenzando con la reutilización de equipos existentes, en lugar de intentar un 'gran salto' arriesgado.
  6. [analisis_cadena_de_valor]
    titulo: Análisis de Cadena de Valor | mundo: core
    resumen: Consiste en examinar la cadena de valor completa, tanto aguas arriba (proveedores) como aguas abajo (clientes de los clientes, usuarios finales), para identificar roles cambiantes, posibles desintermediaciones y oportunidades de negocio donde la empresa podría capturar valor que actualmente otros players se llevan.
  7. [diseno_producto_cadena_suministro]
    titulo: Diseño de Producto Orientado a la Cadena de Suministro | mundo: core
    resumen: El diseño del producto determina la forma de la cadena de suministro necesaria para fabricarlo, impactando fuertemente en costo y disponibilidad. Diseñar productos con menos partes, diseños simples y construcción modular a partir de subensambles genéricos permite trabajar con menos proveedores, reducir inventarios de producto terminado y responder más rápido a la demanda. Equipos multifuncionales (diseño, procurement, manufactura) deben coordinar para lograr productos exitosos y rentables.
  8. [definicion_alineacion_cadena_suministro]
    titulo: Definición y Alineación de la Cadena de Suministro con la Estrategia | mundo: core
    resumen: Una cadena de suministro es la red de empresas y actividades necesarias para diseñar, fabricar, entregar y usar un producto o servicio. Toda empresa participa en una o más cadenas de suministro y debe entender el rol que juega en ellas. La gestión de la cadena de suministro (SCM) es la coordinación sistémica de producción, inventario, ubicación y transporte entre los participantes para lograr el mejor balance entre capacidad de respuesta y eficiencia según el mercado servido. La estrategia de la empresa (competir por precio vs. por servicio/conveniencia) debe determinar el diseño de su cadena de suministro.

### MV-B02
- NODO DEL MUNDO "gestion ambiental" QUE NECESITA UNA PUERTA DESDE EL NUCLEO [optimizacion_tecnologia_cadena_suministro]
    titulo: Optimización de la Cadena de Suministro con Tecnología | mundo: environmental
    resumen: Las nuevas tecnologías permiten a las empresas tener una visión integrada de los impactos de la cadena de suministro. El software de análisis de ciclo de vida y los dashboards permiten comparar el desempeño de proveedores a lo largo del tiempo sin necesidad de recolectar información directamente. Aberdeen Group identifica cuatro áreas clave: dashboards verdes basados en roles, activos sostenibles/eficientes, seguimiento de residuos y transporte/logística sostenible.
- CANDIDATOS A ANCLA (nucleo)
  1. [supply_chain_management_systems]
    titulo: Sistemas de Gestión de Cadena de Suministro (SCM) | mundo: core
    resumen: Los sistemas SCM son suites de aplicaciones integradas (planificación avanzada, planificación de transporte, planificación de demanda, gestión de inventario) que dependen de datos de sistemas ERP y ofrecen capacidades analíticas para la toma de decisiones estratégicas y tácticas en la cadena de suministro.
  2. [scor_model_operaciones]
    titulo: Modelo SCOR: Marco de Operaciones de Cadena de Suministro | mundo: core
    resumen: El modelo SCOR (Supply Chain Operations Reference) es un marco estandarizado y reconocido mundialmente para analizar y mejorar el desempeño de la cadena de suministro. Organiza las operaciones en seis procesos de alto nivel: Planificar, Abastecer, Fabricar, Entregar, Devolver y Habilitar. Provee un lenguaje común, métricas estándar (KPIs de confiabilidad, capacidad de respuesta, agilidad, costo y gestión de activos) y permite benchmarking entre empresas. La versión más reciente, SCOR DS, incorpora resiliencia, sostenibilidad y procesos digitales.
  3. [information_driver_supply_chain]
    titulo: El Rol de la Información como Driver de la Cadena de Suministro | mundo: core
    resumen: La información es el conector entre todas las actividades de tu cadena de suministro y la base para tomar decisiones sobre los otros drivers: producción, inventario, ubicación y transporte. Cuanto más precisa, oportuna y completa sea la información que compartes con proveedores y clientes, mejores decisiones podrás tomar, maximizando la rentabilidad conjunta. La información cumple dos funciones: coordinar actividades diarias, como la programación de producción, los niveles de inventario y las rutas de transporte, y sustentar pronósticos de demanda, tanto a nivel táctico (cronogramas mensuales o trimestrales) como estratégico (decisiones de expansión o entrada y salida de mercados).
  4. [tecnologia_como_medio_no_fin]
    titulo: La tecnología es un medio, no un fin | mundo: core
    resumen: La tecnología en tu cadena de suministro solo vale si te permite entregar el servicio y los precios que tus clientes valoran. No inviertas en tecnología porque sea sofisticada o nueva. Evalúa cada inversión tecnológica según su capacidad real de mejorar el servicio a tus clientes y bajar tus costos de forma rentable.
  5. [ejecucion_incremental_transicion_tecnologica]
    titulo: Transición Tecnológica mediante Pasos Incrementales | mundo: core
    resumen: La tecnología es un medio, no un fin: solo importa en la medida en que permite entregar servicio de valor a los clientes de forma rentable. Las transiciones exitosas hacia nuevas capacidades de cadena de suministro casi siempre involucran una serie de pasos incrementales, comenzando con la reutilización de equipos existentes, en lugar de intentar un 'gran salto' arriesgado.
  6. [analisis_cadena_de_valor]
    titulo: Análisis de Cadena de Valor | mundo: core
    resumen: Consiste en examinar la cadena de valor completa, tanto aguas arriba (proveedores) como aguas abajo (clientes de los clientes, usuarios finales), para identificar roles cambiantes, posibles desintermediaciones y oportunidades de negocio donde la empresa podría capturar valor que actualmente otros players se llevan.
  7. [diseno_producto_cadena_suministro]
    titulo: Diseño de Producto Orientado a la Cadena de Suministro | mundo: core
    resumen: El diseño del producto determina la forma de la cadena de suministro necesaria para fabricarlo, impactando fuertemente en costo y disponibilidad. Diseñar productos con menos partes, diseños simples y construcción modular a partir de subensambles genéricos permite trabajar con menos proveedores, reducir inventarios de producto terminado y responder más rápido a la demanda. Equipos multifuncionales (diseño, procurement, manufactura) deben coordinar para lograr productos exitosos y rentables.
  8. [definicion_alineacion_cadena_suministro]
    titulo: Definición y Alineación de la Cadena de Suministro con la Estrategia | mundo: core
    resumen: Una cadena de suministro es la red de empresas y actividades necesarias para diseñar, fabricar, entregar y usar un producto o servicio. Toda empresa participa en una o más cadenas de suministro y debe entender el rol que juega en ellas. La gestión de la cadena de suministro (SCM) es la coordinación sistémica de producción, inventario, ubicación y transporte entre los participantes para lograr el mejor balance entre capacidad de respuesta y eficiencia según el mercado servido. La estrategia de la empresa (competir por precio vs. por servicio/conveniencia) debe determinar el diseño de su cadena de suministro.

### MV-B03
- NODO DEL MUNDO "gestion ambiental" QUE NECESITA UNA PUERTA DESDE EL NUCLEO [alcance_profundo_cadena_suministro]
    titulo: Alcance Profundo en la Cadena de Suministro (Tier 2/3) | mundo: environmental
    resumen: Cuando gestionas proveedores de forma avanzada, tu responsabilidad no termina en quien te vende directamente (tier 1). También debes preocuparte por los proveedores de tus proveedores (tier 2 y 3), porque ahí pueden esconderse riesgos ambientales, de materiales peligrosos o reputacionales que tú no ves a simple vista. Logras este alcance incluyendo requisitos en los contratos con tus proveedores directos, exigiéndoles que trasladen tu código de conducta a quienes ellos les compran. Algunas empresas llegan a rastrear hasta el 4to o 5to nivel para verificar fórmulas químicas en los materiales que usan. Esto solo tiene sentido si ya tienes un programa maduro de gestión de proveedores y sospechas que el riesgo real está en niveles profundos de tu cadena.
- CANDIDATOS A ANCLA (nucleo)
  1. [information_driver_supply_chain]
    titulo: El Rol de la Información como Driver de la Cadena de Suministro | mundo: core
    resumen: La información es el conector entre todas las actividades de tu cadena de suministro y la base para tomar decisiones sobre los otros drivers: producción, inventario, ubicación y transporte. Cuanto más precisa, oportuna y completa sea la información que compartes con proveedores y clientes, mejores decisiones podrás tomar, maximizando la rentabilidad conjunta. La información cumple dos funciones: coordinar actividades diarias, como la programación de producción, los niveles de inventario y las rutas de transporte, y sustentar pronósticos de demanda, tanto a nivel táctico (cronogramas mensuales o trimestrales) como estratégico (decisiones de expansión o entrada y salida de mercados).
  2. [supply_chain_management_systems]
    titulo: Sistemas de Gestión de Cadena de Suministro (SCM) | mundo: core
    resumen: Los sistemas SCM son suites de aplicaciones integradas (planificación avanzada, planificación de transporte, planificación de demanda, gestión de inventario) que dependen de datos de sistemas ERP y ofrecen capacidades analíticas para la toma de decisiones estratégicas y tácticas en la cadena de suministro.
  3. [seleccion_de_proveedores_por_costo_total]
    titulo: Seleccion de Proveedores por Costo Total Ponderado | mundo: core
    resumen: Elegir proveedor por el precio unitario mas bajo es decidir con la mitad de la informacion. Lo que de verdad cuesta trabajar con un proveedor incluye la calidad que entrega, su cumplimiento y el control que tiene sobre sus procesos, y esos criterios no pesan igual en todos los negocios. El acto propio es armar la comparacion antes de firmar: definir que criterios cualitativos importan, repartir el peso entre el costo monetario y esos criterios, calcular el costo total ponderado de cada proveedor y compararlos con esa cifra en vez de con el precio de lista. Y hay una decision que va con la misma logica: concentrar el volumen en menos proveedores da poder de negociacion, asi que la lista de preferidos se arma a proposito y no por acumulacion.
  4. [definicion_alineacion_cadena_suministro]
    titulo: Definición y Alineación de la Cadena de Suministro con la Estrategia | mundo: core
    resumen: Una cadena de suministro es la red de empresas y actividades necesarias para diseñar, fabricar, entregar y usar un producto o servicio. Toda empresa participa en una o más cadenas de suministro y debe entender el rol que juega en ellas. La gestión de la cadena de suministro (SCM) es la coordinación sistémica de producción, inventario, ubicación y transporte entre los participantes para lograr el mejor balance entre capacidad de respuesta y eficiencia según el mercado servido. La estrategia de la empresa (competir por precio vs. por servicio/conveniencia) debe determinar el diseño de su cadena de suministro.
  5. [diseno_producto_cadena_suministro]
    titulo: Diseño de Producto Orientado a la Cadena de Suministro | mundo: core
    resumen: El diseño del producto determina la forma de la cadena de suministro necesaria para fabricarlo, impactando fuertemente en costo y disponibilidad. Diseñar productos con menos partes, diseños simples y construcción modular a partir de subensambles genéricos permite trabajar con menos proveedores, reducir inventarios de producto terminado y responder más rápido a la demanda. Equipos multifuncionales (diseño, procurement, manufactura) deben coordinar para lograr productos exitosos y rentables.
  6. [driver_de_inventario]
    titulo: Driver de Inventario: Ciclico, de Seguridad y Estacional | mundo: core
    resumen: El inventario es uno de los drivers de la cadena de suministro, y se dimensiona en tres partes que responden a preguntas distintas. El inventario ciclico sale de balancear lo que cuesta ordenar contra lo que cuesta mantener: pedir mas seguido encarece las ordenes y pedir de mas encarece el almacen. El inventario de seguridad no depende del promedio de la demanda sino de su variabilidad y de lo que te cuesta quedarte sin stock. Y el estacional obliga a una eleccion de fondo: acumular antes del pico o invertir en flexibilidad de produccion para no acumular. Las tres se sostienen sobre los puntos de reorden, y esos se ajustan con datos reales de demanda, no con los del plan original.
  7. [tecnologia_como_medio_no_fin]
    titulo: La tecnología es un medio, no un fin | mundo: core
    resumen: La tecnología en tu cadena de suministro solo vale si te permite entregar el servicio y los precios que tus clientes valoran. No inviertas en tecnología porque sea sofisticada o nueva. Evalúa cada inversión tecnológica según su capacidad real de mejorar el servicio a tus clientes y bajar tus costos de forma rentable.
  8. [ciclo_virtuoso_datos_electronicos]
    titulo: Ciclo Virtuoso de Conexiones Electrónicas de Datos | mundo: core
    resumen: La estrategia efectiva de cadena de suministro comienza con mejorar la precisión y flujo de datos entre empresas. Las conexiones electrónicas simples de datos (vs. EDI/XML costosos y complejos) son la base de un ciclo virtuoso de mejora continua, especialmente relevante para las empresas tier 2/3 que aún dependen de email, fax y hojas de cálculo. Sistemas simples con datos buenos superan a sistemas complejos con datos malos ('garbage in, garbage out').

### MV-B04
- NODO DEL MUNDO "gestion de la calidad" QUE NECESITA UNA PUERTA DESDE EL NUCLEO [equipo_conjunto_de_mejora_con_proveedores]
    titulo: Equipo Conjunto Comprador-Proveedor para Mejora de Cadena de Suministro | mundo: quality
    resumen: Enfoque de cinco niveles progresivos para la mejora de la cadena de suministro: crear un equipo conjunto para alinear metas y trabajar en problemas crónicos, enfocarse en reducción de costos, evaluar el valor agregado de cada eslabón, intercambiar información rutinariamente, y finalmente operar la cadena como un proceso único colaborativo. Requiere liderazgo de la alta gerencia en ambas organizaciones.
- CANDIDATOS A ANCLA (nucleo)
  1. [coordinacion_colaboracion_cadena_suministro]
    titulo: Coordinación y Colaboración como Ventaja Competitiva | mundo: core
    resumen: En economías de alto cambio, la coordinación entre empresas de una cadena de suministro es más poderosa que el control unilateral. Las ganancias vienen de conectarse a redes de cadena de suministro y desarrollar reputación de buen servicio y buenos productos a precios razonables (no necesariamente los más bajos). Sistemas diseñados para dar control excesivo a grandes empresas sobre proveedores (bajo el disfraz de 'eficiencia') desmotivan a los proveedores y destruyen la innovación colectiva, dejando a toda la cadena vulnerable cuando el mercado cambia (ejemplo iPhone: ecosistema colaborativo vs. control unilateral).
  2. [seleccion_de_proveedores_por_costo_total]
    titulo: Seleccion de Proveedores por Costo Total Ponderado | mundo: core
    resumen: Elegir proveedor por el precio unitario mas bajo es decidir con la mitad de la informacion. Lo que de verdad cuesta trabajar con un proveedor incluye la calidad que entrega, su cumplimiento y el control que tiene sobre sus procesos, y esos criterios no pesan igual en todos los negocios. El acto propio es armar la comparacion antes de firmar: definir que criterios cualitativos importan, repartir el peso entre el costo monetario y esos criterios, calcular el costo total ponderado de cada proveedor y compararlos con esa cifra en vez de con el precio de lista. Y hay una decision que va con la misma logica: concentrar el volumen en menos proveedores da poder de negociacion, asi que la lista de preferidos se arma a proposito y no por acumulacion.
  3. [definicion_alineacion_cadena_suministro]
    titulo: Definición y Alineación de la Cadena de Suministro con la Estrategia | mundo: core
    resumen: Una cadena de suministro es la red de empresas y actividades necesarias para diseñar, fabricar, entregar y usar un producto o servicio. Toda empresa participa en una o más cadenas de suministro y debe entender el rol que juega en ellas. La gestión de la cadena de suministro (SCM) es la coordinación sistémica de producción, inventario, ubicación y transporte entre los participantes para lograr el mejor balance entre capacidad de respuesta y eficiencia según el mercado servido. La estrategia de la empresa (competir por precio vs. por servicio/conveniencia) debe determinar el diseño de su cadena de suministro.
  4. [diseno_producto_cadena_suministro]
    titulo: Diseño de Producto Orientado a la Cadena de Suministro | mundo: core
    resumen: El diseño del producto determina la forma de la cadena de suministro necesaria para fabricarlo, impactando fuertemente en costo y disponibilidad. Diseñar productos con menos partes, diseños simples y construcción modular a partir de subensambles genéricos permite trabajar con menos proveedores, reducir inventarios de producto terminado y responder más rápido a la demanda. Equipos multifuncionales (diseño, procurement, manufactura) deben coordinar para lograr productos exitosos y rentables.
  5. [information_driver_supply_chain]
    titulo: El Rol de la Información como Driver de la Cadena de Suministro | mundo: core
    resumen: La información es el conector entre todas las actividades de tu cadena de suministro y la base para tomar decisiones sobre los otros drivers: producción, inventario, ubicación y transporte. Cuanto más precisa, oportuna y completa sea la información que compartes con proveedores y clientes, mejores decisiones podrás tomar, maximizando la rentabilidad conjunta. La información cumple dos funciones: coordinar actividades diarias, como la programación de producción, los niveles de inventario y las rutas de transporte, y sustentar pronósticos de demanda, tanto a nivel táctico (cronogramas mensuales o trimestrales) como estratégico (decisiones de expansión o entrada y salida de mercados).
  6. [trade_off_responsividad_eficiencia]
    titulo: Balance entre Capacidad de Respuesta y Eficiencia | mundo: core
    resumen: Cada decisión en la cadena de suministro (producción, inventario, ubicación, transporte, información) implica un trade-off entre ser más responsivo (rápido, flexible, capaz de atender picos de demanda) o más eficiente (bajo costo, alta utilización de activos). El mercado que se sirve determina qué extremo priorizar: mercados masivos sensibles al precio requieren eficiencia; mercados que valoran servicio y conveniencia requieren capacidad de respuesta.
  7. [scor_model_operaciones]
    titulo: Modelo SCOR: Marco de Operaciones de Cadena de Suministro | mundo: core
    resumen: El modelo SCOR (Supply Chain Operations Reference) es un marco estandarizado y reconocido mundialmente para analizar y mejorar el desempeño de la cadena de suministro. Organiza las operaciones en seis procesos de alto nivel: Planificar, Abastecer, Fabricar, Entregar, Devolver y Habilitar. Provee un lenguaje común, métricas estándar (KPIs de confiabilidad, capacidad de respuesta, agilidad, costo y gestión de activos) y permite benchmarking entre empresas. La versión más reciente, SCOR DS, incorpora resiliencia, sostenibilidad y procesos digitales.
  8. [proceso_sop_mop]
    titulo: Planeación Colaborativa S&OP / M&OP (Sales & Operations / Mission & Operations Planning) | mundo: core
    resumen: El S&OP (Sales & Operations Planning) es una práctica empresarial de planeación colaborativa cíclica (cada 15-30 días) que se puede adaptar como M&OP (Mission & Operations Planning) para respuesta a desastres. Consta de cinco pasos: (1) órdenes de misión/CONOPS, (2) planeación de demanda, (3) planeación de oferta, (4) conciliación de planes mediante modelado y simulación en mapas digitales, y (5) implementación y monitoreo continuo. Permite que múltiples organizaciones con agendas distintas lleguen a consenso rápido usando datos visuales compartidos.

### MV-B05
- NODO DEL MUNDO "seguridad digital" QUE NECESITA UNA PUERTA DESDE EL NUCLEO [estrategia_gestion_riesgo_tolerancia]
    titulo: Estrategia de Gestión de Riesgo y Tolerancia al Riesgo | mundo: seguridad_digital
    resumen: La estrategia de gestión de riesgo guía las decisiones sobre cómo se enmarca, evalúa, responde y monitorea el riesgo, haciendo explícitas las percepciones de riesgo usadas en decisiones de inversión y operación. Define la tolerancia al riesgo, es decir, el nivel de riesgo o incertidumbre aceptable para la organización, el cual no tiene un valor 'correcto' universal sino que depende de la cultura organizacional y puede variar según el tipo de pérdida.
- CANDIDATOS A ANCLA (nucleo)
  1. [matriz_probabilidad_impacto]
    titulo: Prioriza tus riesgos según qué tan probable y qué tan grave es cada uno | mundo: core
    resumen: Se trata de cruzar dos cosas de cada riesgo: qué tan probable es que pase y qué tanto te afectaría si pasa. Con eso puedes ordenar tus riesgos por prioridad y ver de un vistazo qué tan expuesto está tu proyecto en general. Qué tanto riesgo consideras alto o bajo depende de cuánto estés dispuesto a aceptar tú.
  2. [reglas_gestion_riesgo_gambling]
    titulo: Las Cinco Reglas de Gestión de Riesgo (Gambling Rules) | mundo: core
    resumen: Basado en la teoría de apuestas, la gestión de nuevos productos es esencialmente gestión de riesgo, entendido como la combinación de monto en juego e incertidumbre. Cinco reglas la guían: mantener bajas las apuestas cuando la incertidumbre es alta, incrementar el monto invertido solo cuando la incertidumbre baja, dividir el proceso en etapas comprando opciones en vez de jugar todo o nada, pagar por información que reduzca la incertidumbre antes de aumentar el gasto, y prever puntos de salida (gates) donde puedas abandonar el proyecto a tiempo. Estas reglas te permiten calibrar cuánto arriesgar en cada momento del proyecto según lo que realmente sabes, en vez de comprometer recursos grandes sobre supuestos no verificados.
  3. [gestion_incertidumbre_contratos]
    titulo: Gestión de Incertidumbre en Contratos: Knowns, Known-Unknowns y Unknown-Unknowns | mundo: core
    resumen: Los acuerdos de equity deben abordar tres tipos de incertidumbre: 'knowns' (hechos ya conocidos, resueltos con términos contractuales estándar), 'known-unknowns' (escenarios anticipables cuyo resultado es incierto, resueltos con cláusulas contingentes) y 'unknown-unknowns' (sorpresas totales, manejadas mediante la confianza mutua del equipo). El objetivo es convertir la mayor cantidad posible de unknown-unknowns en known-unknowns mediante discusión proactiva de escenarios futuros.
  4. [analisis_de_sensibilidad_riesgo]
    titulo: Análisis de Sensibilidad y Ratio Riesgo-Retorno | mundo: core
    resumen: Técnica para identificar riesgos clave de un proyecto probando cómo cambian los resultados financieros al variar supuestos críticos (ej. ventas al 75%, costos +10%, retraso de lanzamiento). También se calcula el ratio riesgo-retorno dividiendo la máxima pérdida acumulada posible entre el NPV del proyecto, para cuantificar el riesgo relativo.
  5. [gestion_de_portafolio_arriesgado]
    titulo: Gestión Estratégica de Portafolio y Buckets (Vector II) | mundo: core
    resumen: Las empresas tienden a gravitar hacia portafolios conservadores y de bajo riesgo, usando erróneamente herramientas financieras tradicionales (NPV, ROI) diseñadas para proyectos pequeños. Esto mata los proyectos audaces. La solución es una gestión de portafolio deliberada, asignando recursos en 'cubetas estratégicas' (strategic buckets), reservando explícitamente una porción del presupuesto para proyectos de alto riesgo y alto rendimiento potencial.
  6. [gestion_riesgo_credito]
    titulo: Gestión Inteligente del Riesgo de Crédito | mundo: core
    resumen: La función de crédito debe ayudar a la empresa a tomar riesgos inteligentes que apoyen su plan de negocio. Una decisión de crédito aparentemente mala desde una perspectiva puede ser una buena decisión de negocio desde otra (por ejemplo, ganar cuota de mercado). Se pueden crear programas de crédito adaptados a segmentos específicos (startups, contratistas, clientes extranjeros) usando seguros de crédito, garantías y avales gubernamentales.
  7. [modelo_contingencia_riesgo]
    titulo: Modelo de Contingencia Basado en Riesgo | mundo: core
    resumen: En vez de seguir una lista fija de actividades tipo SOP (procedimiento operativo estándar), el equipo del proyecto parte de un lienzo en blanco, identifica las incertidumbres clave, señala los supuestos críticos con consecuencias económicas, y determina qué información se necesita para validarlos. Esto define las actividades y entregables específicos de cada proyecto, evitando trabajo innecesario.
  8. [riesgo_recompensa_ideas_audaces]
    titulo: Perfil Riesgo/Recompensa para Ideas Audaces | mundo: core
    resumen: Herramienta para defender ideas de modelo de negocio audaces en organizaciones establecidas sin que sean 'domesticadas' o diluidas. Consiste en mapear el potencial de ganancia/pérdida, conflictos con unidades existentes, impacto en marca y reacción de clientes actuales, para clarificar las incertidumbres y decidir qué prototipar y testear en mercado.

### MV-B06
- NODO DEL MUNDO "seguridad digital" QUE NECESITA UNA PUERTA DESDE EL NUCLEO [fundamentos_gestion_riesgo]
    titulo: Fundamentos de la Gestión de Riesgo (Frame, Assess, Respond, Monitor) | mundo: seguridad_digital
    resumen: La gestión de riesgo es un proceso integral compuesto por cuatro actividades continuas: enmarcar el riesgo (establecer contexto, tolerancia, estrategia), evaluar el riesgo (identificar y priorizar impactos), responder al riesgo (aceptar, evitar, mitigar, compartir o transferir) y monitorear el riesgo (verificar la efectividad de las respuestas de forma continua). Estas actividades forman la base conceptual sobre la cual se construye el Risk Management Framework (RMF) de NIST.
- CANDIDATOS A ANCLA (nucleo)
  1. [matriz_probabilidad_impacto]
    titulo: Prioriza tus riesgos según qué tan probable y qué tan grave es cada uno | mundo: core
    resumen: Se trata de cruzar dos cosas de cada riesgo: qué tan probable es que pase y qué tanto te afectaría si pasa. Con eso puedes ordenar tus riesgos por prioridad y ver de un vistazo qué tan expuesto está tu proyecto en general. Qué tanto riesgo consideras alto o bajo depende de cuánto estés dispuesto a aceptar tú.
  2. [modelo_contingencia_riesgo]
    titulo: Modelo de Contingencia Basado en Riesgo | mundo: core
    resumen: En vez de seguir una lista fija de actividades tipo SOP (procedimiento operativo estándar), el equipo del proyecto parte de un lienzo en blanco, identifica las incertidumbres clave, señala los supuestos críticos con consecuencias económicas, y determina qué información se necesita para validarlos. Esto define las actividades y entregables específicos de cada proyecto, evitando trabajo innecesario.
  3. [project_management_plan]
    titulo: Plan de Gestión del Proyecto | mundo: core
    resumen: Documento integrador que describe cómo se ejecutará, monitoreará, controlará y cerrará el proyecto. Combina todos los planes subsidiarios (alcance, cronograma, costo, calidad, RRHH, comunicaciones, riesgos, adquisiciones, stakeholders) y las líneas base en un enfoque cohesivo para gestionar el proyecto de principio a fin.
  4. [analisis_de_sensibilidad_riesgo]
    titulo: Análisis de Sensibilidad y Ratio Riesgo-Retorno | mundo: core
    resumen: Técnica para identificar riesgos clave de un proyecto probando cómo cambian los resultados financieros al variar supuestos críticos (ej. ventas al 75%, costos +10%, retraso de lanzamiento). También se calcula el ratio riesgo-retorno dividiendo la máxima pérdida acumulada posible entre el NPV del proyecto, para cuantificar el riesgo relativo.
  5. [plan_gestion_calidad]
    titulo: Plan de Gestión de Calidad | mundo: core
    resumen: Componente del plan de gestión del proyecto que describe cómo se cumplirán los requisitos de calidad. Incluye roles y responsabilidades, y enfoques de aseguramiento, control y mejora de calidad, así como herramientas, procesos y políticas relacionadas.
  6. [gestion_incertidumbre_contratos]
    titulo: Gestión de Incertidumbre en Contratos: Knowns, Known-Unknowns y Unknown-Unknowns | mundo: core
    resumen: Los acuerdos de equity deben abordar tres tipos de incertidumbre: 'knowns' (hechos ya conocidos, resueltos con términos contractuales estándar), 'known-unknowns' (escenarios anticipables cuyo resultado es incierto, resueltos con cláusulas contingentes) y 'unknown-unknowns' (sorpresas totales, manejadas mediante la confianza mutua del equipo). El objetivo es convertir la mayor cantidad posible de unknown-unknowns en known-unknowns mediante discusión proactiva de escenarios futuros.
  7. [cinco_porques_master]
    titulo: Designar un Maestro de los Cinco Porqués | mundo: core
    resumen: Rol de facilitador senior, pero no tan alto que no pueda asistir a las sesiones, encargado de moderar las reuniones de Cinco Porqués, decidir las inversiones de prevención y asignar el trabajo de seguimiento. Este maestro actúa como punto de responsabilidad y agente de cambio, evaluando si las inversiones realizadas están dando resultado. Es clave iniciar con un área de problema acotada y específica antes de expandir el proceso a temas de mayor envergadura.
  8. [convertir_unknown_unknowns_en_known_unknowns]
    titulo: Anticipar Escenarios de Riesgo entre Cofundadores | mundo: core
    resumen: En el alto nivel de incertidumbre de una startup, muchos riesgos son 'incógnitas desconocidas' (unknown-unknowns). El primer paso para manejarlos es discutir proactivamente con el equipo fundador qué pasaría si ocurren eventos disruptivos (enfermedad, visa denegada, cambio de prioridades personales), convirtiendo así incógnitas desconocidas en incógnitas conocidas (known-unknowns) sobre las cuales sí se puede planificar y acordar contingencias.

### MV-B07
- NODO DEL MUNDO "seguridad digital" QUE NECESITA UNA PUERTA DESDE EL NUCLEO [getting_started_supply_chain_risk_management]
    titulo: Gestión de Riesgo de la Cadena de Suministro (SCRM) | mundo: seguridad_digital
    resumen: Proceso sistemático para gestionar exposiciones al riesgo cibernético, amenazas y vulnerabilidades en toda la cadena de suministro, desarrollando estrategias de respuesta ante riesgos presentados por proveedores, productos o servicios suministrados.
- CANDIDATOS A ANCLA (nucleo)
  1. [definicion_alineacion_cadena_suministro]
    titulo: Definición y Alineación de la Cadena de Suministro con la Estrategia | mundo: core
    resumen: Una cadena de suministro es la red de empresas y actividades necesarias para diseñar, fabricar, entregar y usar un producto o servicio. Toda empresa participa en una o más cadenas de suministro y debe entender el rol que juega en ellas. La gestión de la cadena de suministro (SCM) es la coordinación sistémica de producción, inventario, ubicación y transporte entre los participantes para lograr el mejor balance entre capacidad de respuesta y eficiencia según el mercado servido. La estrategia de la empresa (competir por precio vs. por servicio/conveniencia) debe determinar el diseño de su cadena de suministro.
  2. [scor_model_operaciones]
    titulo: Modelo SCOR: Marco de Operaciones de Cadena de Suministro | mundo: core
    resumen: El modelo SCOR (Supply Chain Operations Reference) es un marco estandarizado y reconocido mundialmente para analizar y mejorar el desempeño de la cadena de suministro. Organiza las operaciones en seis procesos de alto nivel: Planificar, Abastecer, Fabricar, Entregar, Devolver y Habilitar. Provee un lenguaje común, métricas estándar (KPIs de confiabilidad, capacidad de respuesta, agilidad, costo y gestión de activos) y permite benchmarking entre empresas. La versión más reciente, SCOR DS, incorpora resiliencia, sostenibilidad y procesos digitales.
  3. [gestion_pedidos_order_management]
    titulo: Gestión de Pedidos (Order Management) | mundo: core
    resumen: Proceso de transmitir información de pedidos desde clientes hacia atrás en la cadena de suministro (minoristas, distribuidores, proveedores de servicios, productores) y devolver información de fechas de entrega, sustituciones y pedidos pendientes. Se rige por cuatro principios: ingresar los datos del pedido una sola vez y capturarlos electrónicamente en la fuente original; automatizar el manejo de pedidos rutinarios y reservar la intervención humana para excepciones; hacer visible el estado del pedido a clientes y agentes de servicio; e integrar los sistemas de gestión de pedidos con otros sistemas relacionados (inventario, precios, facturación) para mantener la integridad de los datos.
  4. [bucle_retroalimentacion_autoajustable]
    titulo: Bucle de Retroalimentación Autoajustable en la Cadena de Suministro | mundo: core
    resumen: Un mecanismo donde el sistema compara continuamente su estado actual con el objetivo deseado y toma acciones correctivas para minimizar la diferencia, como un termostato o el control de crucero de un auto. Aplicado a cadenas de suministro, permite que empresas y sus socios ajusten su comportamiento en tiempo real (hora a hora) para mantenerse alineados con metas de desempeño, controlando efectos como el 'bullwhip effect' y generando eficiencias acumulativas similares al interés compuesto.
  5. [information_driver_supply_chain]
    titulo: El Rol de la Información como Driver de la Cadena de Suministro | mundo: core
    resumen: La información es el conector entre todas las actividades de tu cadena de suministro y la base para tomar decisiones sobre los otros drivers: producción, inventario, ubicación y transporte. Cuanto más precisa, oportuna y completa sea la información que compartes con proveedores y clientes, mejores decisiones podrás tomar, maximizando la rentabilidad conjunta. La información cumple dos funciones: coordinar actividades diarias, como la programación de producción, los niveles de inventario y las rutas de transporte, y sustentar pronósticos de demanda, tanto a nivel táctico (cronogramas mensuales o trimestrales) como estratégico (decisiones de expansión o entrada y salida de mercados).
  6. [driver_de_inventario]
    titulo: Driver de Inventario: Ciclico, de Seguridad y Estacional | mundo: core
    resumen: El inventario es uno de los drivers de la cadena de suministro, y se dimensiona en tres partes que responden a preguntas distintas. El inventario ciclico sale de balancear lo que cuesta ordenar contra lo que cuesta mantener: pedir mas seguido encarece las ordenes y pedir de mas encarece el almacen. El inventario de seguridad no depende del promedio de la demanda sino de su variabilidad y de lo que te cuesta quedarte sin stock. Y el estacional obliga a una eleccion de fondo: acumular antes del pico o invertir en flexibilidad de produccion para no acumular. Las tres se sostienen sobre los puntos de reorden, y esos se ajustan con datos reales de demanda, no con los del plan original.
  7. [dependency_analysis]
    titulo: Análisis de Dependencias | mundo: core
    resumen: Responde a la pregunta: '¿Qué debe suceder, fuera de nuestro control, para vender nuestro producto a gran volumen?'. Identifica cambios tecnológicos, de comportamiento del consumidor, regulatorios o económicos externos necesarios para el éxito del negocio, junto con planes de contingencia si no ocurren.
  8. [tecnologia_como_medio_no_fin]
    titulo: La tecnología es un medio, no un fin | mundo: core
    resumen: La tecnología en tu cadena de suministro solo vale si te permite entregar el servicio y los precios que tus clientes valoran. No inviertas en tecnología porque sea sofisticada o nueva. Evalúa cada inversión tecnológica según su capacidad real de mejorar el servicio a tus clientes y bajar tus costos de forma rentable.

## C: nodos del nucleo que se quedan sin camino por el nucleo. Elige un PREDECESOR DEL NUCLEO

### MV-C01
- NODO DEL NUCLEO SIN CAMINO [big_data_ia_cadena_suministro]
    titulo: Big Data e IA Predictiva en la Cadena de Suministro | mundo: core
    resumen: Basado en el caso de Microsoft, este concepto describe cómo centralizar datos en la nube (data lake), aplicar machine learning y visualizar resultados en dashboards permite pasar de una gestión reactiva a una predictiva. Esto habilita anticipar devoluciones de productos, mantenimiento predictivo en fábricas, y mayor capacidad de respuesta ante disrupciones. Requiere un cambio cultural hacia una organización basada en datos ('learn it all') y equipos de ciencia de datos que trabajen junto a expertos de dominio.
- CANDIDATOS A PREDECESOR (nucleo)
  1. [creacion_data_warehouse]
    titulo: Crea un repositorio central de datos para tu cadena de suministro (data warehouse) | mundo: core
    resumen: Un repositorio central de datos (data warehouse) junta la información de los distintos sistemas que usas para operar y llevar las cuentas de tu negocio, capturándola automáticamente desde la fuente para que no tengas que ingresarla a mano. Combina una base de datos con herramientas de reportes ya armados, gráficos y consultas que puedes hacer tú mismo. Conviene que empieces con algo simple y lo vayas ampliando a medida que le agarras la mano a usar los datos todos los días.
  2. [evaluar_ia_predictiva_vs_generativa_para_negocio]
    titulo: ¿Predecir o generar? Elige el tipo de IA correcto (IA predictiva vs IA generativa) | mundo: core
    resumen: Existen dos grandes tipos de inteligencia artificial y cada uno resuelve problemas distintos en tu negocio. La IA predictiva (aprende de datos ya etiquetados) te sirve para prever la demanda, optimizar el inventario y mejorar la logística; es el caso de Amazon, que usa IA para manejar toda su cadena de suministro, desde el pronóstico hasta los robots Kiva en sus almacenes. La IA generativa (los LLMs) te sirve para crear contenido, analizar texto y simular conversaciones. Antes de elegir una herramienta, identifica qué tipo de problema tienes: ¿necesitas predecir un número o generar contenido y lenguaje?
  3. [information_driver_supply_chain]
    titulo: El Rol de la Información como Driver de la Cadena de Suministro | mundo: core
    resumen: La información es el conector entre todas las actividades de tu cadena de suministro y la base para tomar decisiones sobre los otros drivers: producción, inventario, ubicación y transporte. Cuanto más precisa, oportuna y completa sea la información que compartes con proveedores y clientes, mejores decisiones podrás tomar, maximizando la rentabilidad conjunta. La información cumple dos funciones: coordinar actividades diarias, como la programación de producción, los niveles de inventario y las rutas de transporte, y sustentar pronósticos de demanda, tanto a nivel táctico (cronogramas mensuales o trimestrales) como estratégico (decisiones de expansión o entrada y salida de mercados).
  4. [jerarquia_datos_scor]
    titulo: Los tres niveles de datos de tu negocio: estratégicos, operativos y tácticos (modelo SCOR) | mundo: core
    resumen: El modelo SCOR (Supply Chain Operations Reference) clasifica los datos de tu negocio en tres niveles según para qué los usas: los datos estratégicos te sirven a ti para ver el desempeño global en atención al cliente, eficiencia interna, capacidad de responder a cambios en la demanda y desarrollo de producto; los datos operativos los necesita quien coordina el trabajo día a día en cada sucursal para planificar; y los datos tácticos los usa quien resuelve los problemas del terreno. Esta estructura evita que te ahogues en información y permite que cada persona vea solo el nivel de detalle que necesita para su trabajo.
  5. [bpm_gestion_excepciones]
    titulo: Gestión de Excepciones con Business Process Management (BPM) | mundo: core
    resumen: El uso de software BPM interfaced con los sistemas transaccionales permite definir reglas de negocio y detectar automáticamente excepciones (errores en pedidos, retrasos, facturación) para alertar al personal correspondiente, permitiendo una atención al cliente proactiva en vez de reactiva.
  6. [supply_chain_management_systems]
    titulo: Sistemas de Gestión de Cadena de Suministro (SCM) | mundo: core
    resumen: Los sistemas SCM son suites de aplicaciones integradas (planificación avanzada, planificación de transporte, planificación de demanda, gestión de inventario) que dependen de datos de sistemas ERP y ofrecen capacidades analíticas para la toma de decisiones estratégicas y tácticas en la cadena de suministro.
  7. [gestion_pedidos_order_management]
    titulo: Gestión de Pedidos (Order Management) | mundo: core
    resumen: Proceso de transmitir información de pedidos desde clientes hacia atrás en la cadena de suministro (minoristas, distribuidores, proveedores de servicios, productores) y devolver información de fechas de entrega, sustituciones y pedidos pendientes. Se rige por cuatro principios: ingresar los datos del pedido una sola vez y capturarlos electrónicamente en la fuente original; automatizar el manejo de pedidos rutinarios y reservar la intervención humana para excepciones; hacer visible el estado del pedido a clientes y agentes de servicio; e integrar los sistemas de gestión de pedidos con otros sistemas relacionados (inventario, precios, facturación) para mantener la integridad de los datos.
  8. [gestion_visual_del_pipeline_de_desarrollo]
    titulo: Gestión Visual del Pipeline de Desarrollo (Portfolio Visibility) | mundo: core
    resumen: Agile-Stage-Gate genera gran visibilidad visual del progreso de tareas dentro y entre proyectos mediante tableros visuales (físicos o virtuales). Esto permite al dueño del portafolio pasar de una gestión reactiva (basada en revisiones mensuales) a una proactiva, interviniendo en tiempo real cuando se detectan problemas o tendencias negativas.

### MV-C02
- NODO DEL NUCLEO SIN CAMINO [collaboration_roadblocks]
    titulo: Obstáculos a la Colaboración en la Cadena de Suministro | mundo: core
    resumen: Existen obstáculos recurrentes que dificultan la colaboración exitosa: falta de confianza y control sobre la propiedad intelectual compartida, riesgo de fuga de información propietaria a competidores, cuestiones éticas no resueltas, dificultades de integración de sistemas, complejidad de la colaboración global, dificultad para medir beneficios totales, y falta de estructuras/estándares establecidos.
- CANDIDATOS A PREDECESOR (nucleo)
  1. [coordinacion_colaboracion_cadena_suministro]
    titulo: Coordinación y Colaboración como Ventaja Competitiva | mundo: core
    resumen: En economías de alto cambio, la coordinación entre empresas de una cadena de suministro es más poderosa que el control unilateral. Las ganancias vienen de conectarse a redes de cadena de suministro y desarrollar reputación de buen servicio y buenos productos a precios razonables (no necesariamente los más bajos). Sistemas diseñados para dar control excesivo a grandes empresas sobre proveedores (bajo el disfraz de 'eficiencia') desmotivan a los proveedores y destruyen la innovación colectiva, dejando a toda la cadena vulnerable cuando el mercado cambia (ejemplo iPhone: ecosistema colaborativo vs. control unilateral).
  2. [prueba_antes_de_comprometerse]
    titulo: Probar la Compatibilidad Antes de Cofundar ('Try Before You Buy') | mundo: core
    resumen: Antes de comprometerse a largo plazo como cofundadores, es recomendable colaborar en tareas concretas y acotadas (proyectos, competencias de planes de negocio, trabajo previo) para evaluar la compatibilidad real de trabajo, valores, tolerancia al riesgo y estilo de compromiso, evitando así asumir que la afinidad social o académica garantiza una buena sociedad profesional.
  3. [confianza_mutua_fundadores]
    titulo: Construcción y Mantenimiento de la Confianza entre Cofundadores | mundo: core
    resumen: La confianza entre cofundadores es el 'cable' que evita que el equipo colapse ante sorpresas y tensiones. Negociaciones difíciles (como el reparto de equity) pueden fortalecer o destruir esta confianza dependiendo de cómo se manejen. Comunicación abierta y disposición a ajustar acuerdos según las necesidades de todos fortalece la confianza; negociar de forma egoísta buscando maximizar el propio beneficio a corto plazo la destruye.
  4. [confidencialidad_nda_adquisicion]
    titulo: Acuerdo de Confidencialidad (NDA) en Procesos de Adquisición | mundo: core
    resumen: A diferencia de las rondas de inversión, en procesos de M&A los NDAs son prácticamente obligatorios, ya que ambas partes comparten información sensible durante el due diligence. Un NDA débil o unilateral puede ser señal de que el comprador busca información competitiva más que cerrar un trato genuino.
  5. [anticipacion_riesgos_fundacionales]
    titulo: Anticipa los riesgos de fundar tu negocio antes de que te pasen | mundo: core
    resumen: Muchos de los problemas que vas a enfrentar al fundar tu negocio (cofundar con amigos o familia, repartir la participación de forma fija desde el inicio, aceptar dinero de inversionistas que suelen reemplazar al fundador que dirige) son predecibles. Si los anticipas, puedes poner protecciones (acuerdos claros con familiares, cláusulas para recomprar la participación de quien se va, investigar antes a tus inversionistas) que reducen el daño.
  6. [obstaculos_innovacion_modelo_negocio]
    titulo: Obstáculos Organizacionales a la Innovación de Modelos de Negocio | mundo: core
    resumen: La innovación de modelos de negocio enfrenta barreras humanas y organizacionales recurrentes: falta de lenguaje común para hablar de modelos de negocio, resistencia al cambio hasta que aparecen crisis, miedo a canibalizar el negocio actual, métricas de éxito que premian la eficiencia sobre la exploración, y estructuras de compensación desalineadas con la innovación. El éxito actual de una empresa suele ser el mayor obstáculo para cuestionar su propio modelo.
  7. [pipeline_alianzas_bd]
    titulo: Construcción de un Pipeline de Alianzas | mundo: core
    resumen: Dado que la mayoría de los acuerdos de BD no se concretan, es esencial mantener una lista extensa y organizada de socios potenciales, categorizados por tipo, tamaño, relevancia y prioridad. Esto permite trabajar múltiples oportunidades en paralelo y no depender de un solo prospecto.
  8. [cuantos_cofundadores_agregar]
    titulo: Determinar el Número Óptimo de Cofundadores | mundo: core
    resumen: Cada cofundador que suma añade también costo de coordinación, más complejidad de comunicación y más riesgo de choques por roles. Sueles subestimar esos costos y sobreestimar el valor de alguien que repite lo que ya tienes. La regla es simple: cada nuevo cofundador tiene que aportar algo claro (cubrir una carencia de capital o quitarte carga real) que pese más que la complejidad que añade.

### MV-C03
- NODO DEL NUCLEO SIN CAMINO [combinacion_humano_ia_decision]
    titulo: Combinación Óptima de Personas y Tecnología (Humano + IA) | mundo: core
    resumen: Basado en el estudio de Brynjolfsson y McAfee sobre torneos de ajedrez, se demuestra que equipos de personas con habilidades moderadas usando IA simple y simulaciones superan tanto a expertos humanos sin tecnología como a sistemas de IA complejos sin intervención humana. La clave del éxito está en dejar que las personas hagan el pensamiento creativo y la resolución de problemas, mientras la tecnología realiza los cálculos masivos y valida ideas rápidamente, especialmente bajo presión de tiempo.
- CANDIDATOS A PREDECESOR (nucleo)
  1. [ideacion_con_ia_en_la_sesion]
    titulo: Ideación con IA dentro de la Sesión | mundo: core
    resumen: La IA entra en la sesión de ideas como un participante más, no como sustituto del equipo. Su ventaja es el volumen y la variedad: produce lotes grandes y adopta estilos o puntos de vista que la sala no tiene. Su límite es el criterio, que sigue siendo humano: el lote se filtra después, y las ideas que sobreviven se cruzan entre sí para forzar híbridos que ninguna de las dos partes habría propuesto sola.
  2. [centaur_cyborg_ia]
    titulo: Modelos de Colaboración Centauro y Cyborg con IA | mundo: core
    resumen: Existen dos formas principales de integrar IA en el trabajo humano: el modelo Centauro, donde hay una división clara de tareas entre persona y máquina (cada uno hace lo que mejor sabe), y el modelo Cyborg, donde humano e IA se entrelazan profundamente en la misma tarea (por ejemplo, completando frases o iterando ideas juntos). Elegir el modelo correcto según la tarea permite maximizar productividad y calidad sin perder control ni criterio humano.
  3. [habilidad_prompting_como_experticia]
    titulo: La Habilidad de Trabajar con IA como Nueva Experticia Competitiva | mundo: core
    resumen: Surge un nuevo tipo de ventaja competitiva: personas o equipos que son excepcionalmente hábiles trabajando con sistemas de IA (adoptando prácticas 'Cyborg', diseñando prompts efectivos, iterando con la IA) logran mejoras de rendimiento órdenes de magnitud mayores que el usuario promedio. Esta habilidad, aunque difícil de definir con precisión, puede convertirse en un diferenciador clave para founders y equipos que buscan maximizar el retorno de sus herramientas de IA.
  4. [division_trabajo_humano_ia]
    titulo: División del Trabajo entre Humanos e IA | mundo: core
    resumen: Principio estratégico que establece que las computadoras y la IA deben automatizar las tareas repetitivas, rutinarias y de monitoreo (donde no fallan ni se cansan), mientras que las personas deben enfocarse en actividades creativas, de resolución de problemas y colaboración, donde no hay respuestas correctas claras y se requiere juicio humano.
  5. [ai_como_coach_personalizado]
    titulo: IA como Coach o Tutor Personalizado para el Equipo | mundo: core
    resumen: Los tutores de IA pueden personalizar el aprendizaje según el desempeño de cada persona, ajustando el contenido y detectando patrones de dificultad para ofrecer ayuda más profunda. Aplicado a un equipo de startup, esto permite acelerar la capacitación de nuevos colaboradores, liberando tiempo del líder para interacciones de mayor valor y aprendizaje activo (resolución de problemas reales, discusión, mentoring directo).
  6. [comprension_capacidades_limitaciones_ia]
    titulo: Comprensión de las Capacidades y Limitaciones Impredecibles de la IA | mundo: core
    resumen: Las IA modernas muestran capacidades que ni sus propios creadores anticiparon del todo: pueden sobresalir en tareas complejas, como escribir código funcional, y al mismo tiempo fallar en tareas aparentemente simples, como jugar tic-tac-toe correctamente. Esto significa que lo que es fácil para ti puede ser difícil para la IA, y al revés. Antes de confiar en ella para algo importante de tu negocio, prueba tú mismo qué tan bien resuelve tu caso concreto, en lugar de asumir que funciona bien solo porque el modelo tiene buena fama.
  7. [ia_generacion_ideas_negocio]
    titulo: IA como Motor de Generación de Ideas (Recombinación) | mundo: core
    resumen: La innovación surge frecuentemente de la recombinación de ideas existentes de campos distintos (como los hermanos Wright combinando mecánica de bicicletas y observación de aves). Los LLMs son 'máquinas de conexión' entrenadas para encontrar relaciones entre conceptos aparentemente no relacionados, lo que las hace herramientas poderosas para generar ideas de negocio novedosas. En estudios controlados (ej. Wharton), un modelo de IA avanzado superó a 200 estudiantes de MBA generando ideas de producto: 35 de las 40 mejores ideas evaluadas por jueces humanos vinieron de la IA. Sin embargo, la mayoría de ideas generadas serán mediocres; el valor está en generar volumen y luego filtrar humanamente.
  8. [adoptar_co_inteligencia_ia]
    titulo: Co-Inteligencia: IA como Socio de Trabajo | mundo: core
    resumen: A diferencia de tecnologías anteriores que automatizan tareas mecánicas repetitivas, la IA generativa actúa como una 'co-inteligencia': un colaborador que puede pensar junto a los humanos, generar ideas, redactar planes de negocio, simular escenarios de negociación y actuar como un cofundador virtual. El caso de un estudiante que creó un demo funcional para su proyecto de emprendimiento en menos de la mitad de tiempo usando IA, obteniendo interés de inversionistas de capital de riesgo al día siguiente, ilustra el potencial de usar la IA como socio activo en el proceso emprendedor, no solo como herramienta pasiva.

### MV-C04
- NODO DEL NUCLEO SIN CAMINO [definicion_metas_engagement]
    titulo: Define tus metas y decisiones sobre el compromiso de tu equipo (engagement) | mundo: core
    resumen: Después de evaluar las actitudes de tu equipo, tienes que definir objetivos claros y tomar decisiones clave: qué le vas a pedir a las personas, si la participación será opcional u obligatoria, quién toma las decisiones y cómo vas a medir y evaluar el progreso con datos cuantitativos y cualitativos.
- CANDIDATOS A PREDECESOR (nucleo)
  1. [diseno_metricas_lideres_rezagados]
    titulo: Cómo diseñar tus métricas: señales tempranas y resultados finales | mundo: core
    resumen: Cuando diseñas tus métricas, tienes que combinar señales tempranas (indicadores líderes, que te avisan hacia dónde vas antes de llegar) con resultados finales (indicadores rezagados, que miden lo que ya pasó). Si mides solo una cosa, por ejemplo la velocidad, sin vigilar también la calidad, puedes terminar empujando a tu equipo hacia comportamientos que te perjudican.
  2. [reunion_pivotar_o_perseverar]
    titulo: La reunión para decidir si cambias de rumbo o sigues igual (pivotar o perseverar) | mundo: core
    resumen: Decidir si cambias de rumbo es una decisión cargada de emoción, así que conviene convertirla en un hábito: programa estas reuniones con una cadencia regular, ni muy seguida ni muy espaciada, para que cuando llegue el momento tengas datos de sobra y el peso emocional pese menos. Reúne a quien construye el producto y a quien lleva el negocio, e invita si puedes a alguien externo que te dé una mirada objetiva. Lleva un reporte completo de los resultados de tus experimentos a lo largo del tiempo comparados con lo que esperabas al inicio, no solo del último periodo, y súmale lo que has escuchado en conversaciones con clientes actuales y potenciales. Antes de decidir, investiga otras líneas posibles, como nuevos segmentos o necesidades que nadie está atendiendo.
  3. [team_performance_assessment]
    titulo: Evaluación de Desempeño del Equipo | mundo: core
    resumen: Evalúa el desempeño técnico e interpersonal del equipo como conjunto, incluyendo moral y cohesión, para identificar áreas de mejora que ayuden a lograr los objetivos del proyecto.
  4. [plan_gestion_interesados]
    titulo: Plan para relacionarte con las personas interesadas en tu proyecto | mundo: core
    resumen: Aquí defines cómo te vas a relacionar con cada persona que tiene algo que ver con tu proyecto: en qué nivel de compromiso está ahora, en qué nivel te gustaría que estuviera, qué necesita saber de ti y cómo la vas acercando al nivel que buscas.
  5. [diamante_decision_tres_partes]
    titulo: Las tres partes de la reunión para decidir si tu proyecto sigue adelante (gate) | mundo: core
    resumen: Cuando revises si un proyecto tuyo sigue adelante, separa la conversación en tres partes claras. Primero, revisa si lo que entregaste está completo y con la calidad esperada: si falta algo, lo corriges, no lo cancelas. Segundo, evalúa si el proyecto sigue siendo una buena inversión, mirando los números y los criterios que ya definiste; si no lo es, ahí sí lo cierras. Tercero, compara ese proyecto con tus otras iniciativas para decidir a cuál le dedicas tiempo y recursos ahora. Mantener estas tres preguntas separadas evita que sientas que te penalizan por un buen trabajo cuando en realidad el proyecto solo perdió prioridad frente a otro.
  6. [protocolo_reuniones_gate]
    titulo: Reglas claras para tus reuniones de decisión (gate) | mundo: core
    resumen: Cuando te reúnes para decidir si un proyecto sigue adelante, necesitas reglas que hagan la reunión justa, transparente, efectiva y rápida. Antes de sentarte a decidir, define reglas claras: todos los que deciden asisten, todos leen los entregables con anticipación, nadie pide información extra que no se haya pedido antes, nadie ataca a quien presenta, las decisiones se toman con criterios y hechos, no con política ni emociones, y la decisión se cierra ese mismo día. Te conviene que alguien modere la reunión como árbitro imparcial.
  7. [plan_gestion_recursos_humanos]
    titulo: Plan de Gestión del Equipo del Proyecto | mundo: core
    resumen: Describe cómo abordarás todos los aspectos de gestión del equipo del proyecto, compuesto por roles y responsabilidades, organigramas del proyecto y el plan de gestión de personal (adquisición, liberación, calendarios, capacitación, reconocimiento y seguridad).
  8. [criterios_de_exito_gate]
    titulo: Criterios de Éxito para Evaluar tu Proyecto por Etapas (Gates) | mundo: core
    resumen: Como alternativa a evaluar solo con números financieros, puedes definir criterios de éxito claros para cada etapa (gate) de tu proyecto, por ejemplo ventas del primer año, margen de utilidad o fecha de lanzamiento. Este método, que usan compañías como P&G, te sirve para revisar tu avance en cada etapa sucesiva y también en la revisión posterior al lanzamiento, ayudándote a mantenerte responsable de los resultados que prometiste.

### MV-C05
- NODO DEL NUCLEO SIN CAMINO [evaluacion_preparacion_tecnologica]
    titulo: Revisa si tu tecnología está lista para vender en línea (evaluación IT) | mundo: core
    resumen: Antes de lanzar tus operaciones en línea, evalúa tus necesidades y capacidades de tecnología (IT): tus sistemas actuales, qué partes de tu negocio conviene migrar, si conviene invertir en tecnología nueva según costo y beneficio, y qué medidas de seguridad necesitas frente a ataques informáticos.
- CANDIDATOS A PREDECESOR (nucleo)
  1. [channels_hypothesis_web_mobile]
    titulo: Cómo va a llegar tu producto al cliente (canal de venta digital) | mundo: core
    resumen: Define cómo tu producto va a llegar de tus manos a las de tu cliente en un entorno digital. Tienes varias opciones para elegir (tienda online propia, distribución en dos pasos, agregadores, plataformas de aplicaciones, venta a través de redes sociales, ventas relámpago, empezar gratis y cobrar después), y cada una tiene sus fortalezas, sus debilidades y sus costos. Tienes que elegir un canal principal buscando el mejor balance entre lo que ofreces, cuánto te cuesta, cómo generas ingresos y qué prefiere tu cliente.
  2. [tecnologia_como_medio_no_fin]
    titulo: La tecnología es un medio, no un fin | mundo: core
    resumen: La tecnología en tu cadena de suministro solo vale si te permite entregar el servicio y los precios que tus clientes valoran. No inviertas en tecnología porque sea sofisticada o nueva. Evalúa cada inversión tecnológica según su capacidad real de mejorar el servicio a tus clientes y bajar tus costos de forma rentable.
  3. [validacion_hipotesis_ingresos]
    titulo: Comprobar si tus ingresos aguantan el negocio | mundo: core
    resumen: Antes de crecer, haz un cálculo aproximado, a mano y sin ser contador, para ver si lo que vas a ganar cubre tus costos, si eso mejora con el tiempo y si te conviene más entre más grande te pones. También revisa cómo el canal por el que vendes afecta cuánto ingreso te queda realmente, y ten en cuenta cuánto vale un cliente durante todo el tiempo que te compra (su valor de vida, o Customer Lifetime Value) porque eso debería guiar tu precio.
  4. [evaluacion_ventana_mercado]
    titulo: Evaluación de la Ventana de Oportunidad de Mercado | mundo: core
    resumen: Antes de lanzar tu idea, evalúa con honestidad si el momento es el correcto (la ventana de oportunidad de mercado). Mira el tamaño y el crecimiento del mercado, si puedes llegar a todo el país o solo a tu zona, cuánta competencia hay y en qué etapa está esa industria. Pregúntate si hay un reloj corriendo, como una tecnología que cambia rápido, que te obligue a moverte ya. Si tu idea es disruptiva, necesitará más tiempo que una que mejora algo que ya existe.
  5. [identificacion_brechas_funcionales]
    titulo: Identifica lo que no sabes hacer en tu negocio | mundo: core
    resumen: Cuando arrancas un negocio tienes que cubrir todas las funciones: producto, marketing, ventas, finanzas, gente. Si te faltan habilidades en alguna de esas áreas, un problema justo ahí te puede tomar por sorpresa y provocarte retrasos serios y decisiones tomadas a ciegas. Por ejemplo, si vienes del área comercial pero no tienes experiencia técnica para desarrollar software, ese hueco te puede complicar.
  6. [alineacion_ti_negocio]
    titulo: Alinear la tecnología con tu modelo de negocio | mundo: core
    resumen: Cuando tus sistemas y herramientas tecnológicas están alineados con tu modelo de negocio, tienes más chances de que funcione. El lienzo de modelo de negocio (Business Model Canvas) te ayuda a entender rápido cómo funciona tu negocio sin perderte en detalles operativos, y sirve de puente entre tu visión de negocio, las aplicaciones que usas y la tecnología detrás (arquitectura empresarial). Usa el Canvas para definir primero tu visión de negocio y después alinea tus aplicaciones e infraestructura tecnológica en función de eso.
  7. [seleccion_canal_distribucion]
    titulo: Selección de Canal de Distribución | mundo: core
    resumen: Elegir el canal de ventas adecuado (físico, web/mobile o híbrido) es crítico y debe alinearse con el precio del producto, los hábitos de compra existentes y los costos asociados. Un error común de las startups es intentar lanzar por múltiples canales simultáneamente antes de validar cuál funciona mejor.
  8. [customer_validation_sell_phase]
    titulo: Sal a vender de verdad: valida con clientes reales | mundo: core
    resumen: Después de prepararte para vender, tienes que intentar vender el producto de verdad, o atraer usuarios y pagadores, usando pruebas simples que pasan o no pasan sobre lo que crees de tu negocio. El objetivo no es hacer crecer los ingresos todavía, sino comprobar que hay un negocio real ahí: que los clientes valoran lo que ofreces, que el precio es el correcto, que el proceso de compra funciona y que hay suficiente mercado para sostenerte.

### MV-C06
- NODO DEL NUCLEO SIN CAMINO [industrial_robots_automation]
    titulo: Automatización con Robots Industriales | mundo: core
    resumen: Los robots industriales son manipuladores diseñados para mover materiales, partes y herramientas, y realizar tareas programadas en manufactura y producción. Su sofisticación y asequibilidad crecientes permiten que empresas de todos los tamaños los adopten para tareas peligrosas o repetitivas en fábricas y almacenes.
- CANDIDATOS A PREDECESOR (nucleo)
  1. [division_trabajo_humano_ia]
    titulo: División del Trabajo entre Humanos e IA | mundo: core
    resumen: Principio estratégico que establece que las computadoras y la IA deben automatizar las tareas repetitivas, rutinarias y de monitoreo (donde no fallan ni se cansan), mientras que las personas deben enfocarse en actividades creativas, de resolución de problemas y colaboración, donde no hay respuestas correctas claras y se requiere juicio humano.
  2. [manufactura_aditiva_bajo_demanda]
    titulo: Manufactura Aditiva (Impresión 3D) para Producción Bajo Demanda | mundo: core
    resumen: La impresión 3D o manufactura aditiva permite crear productos por capas a partir de materia prima común (plástico, polvo metálico), fabricando bajo demanda en lugar de predecir y almacenar inventario de múltiples variantes. Esto reduce costos de inventario y mejora el nivel de servicio al cliente al minimizar quiebres de stock.
  3. [driver_produccion]
    titulo: Driver de Producción: Enfoque de Producto vs Funcional | mundo: core
    resumen: La producción se refiere a la capacidad de fabricar y almacenar productos. Las fábricas pueden diseñarse con enfoque de producto (realizan todas las operaciones para una línea de producto, generando expertise en ese producto) o enfoque funcional (se especializan en pocas operaciones aplicables a múltiples productos, generando expertise funcional). Además, los almacenes pueden organizarse mediante almacenamiento por SKU, por lote de trabajo (job lot) o crossdocking (sin almacenar, solo redistribuyendo rápidamente).
  4. [sistemas_organizacionales_ia]
    titulo: De Tareas a Sistemas: Rediseño Organizacional con IA | mundo: core
    resumen: Los sistemas de trabajo (organigramas, líneas de producción, metodologías ágiles) son artefactos históricos moldeados por la tecnología de su época. La IA plantea la necesidad de repensar estos sistemas desde cero, no solo automatizar tareas individuales, sino rediseñar cómo se coordina y estructura el trabajo mismo.
  5. [automatizacion_software_gestion_innovacion]
    titulo: Automatización mediante Software de Gestión de Innovación | mundo: core
    resumen: Usa herramientas de software para acelerar y ordenar tu proceso de decisión por etapas (conocido como Stage-Gate): plantillas ya armadas, reportes de estado que se generan solos, paneles (dashboards) para ver tus proyectos, y gestión de recursos e ideas. Te quita carga administrativa y te da consistencia al ejecutar el proceso, para que puedas ver el avance de un proyecto o de todos los que tienes en marcha.
  6. [evaluar_ia_predictiva_vs_generativa_para_negocio]
    titulo: ¿Predecir o generar? Elige el tipo de IA correcto (IA predictiva vs IA generativa) | mundo: core
    resumen: Existen dos grandes tipos de inteligencia artificial y cada uno resuelve problemas distintos en tu negocio. La IA predictiva (aprende de datos ya etiquetados) te sirve para prever la demanda, optimizar el inventario y mejorar la logística; es el caso de Amazon, que usa IA para manejar toda su cadena de suministro, desde el pronóstico hasta los robots Kiva en sus almacenes. La IA generativa (los LLMs) te sirve para crear contenido, analizar texto y simular conversaciones. Antes de elegir una herramienta, identifica qué tipo de problema tienes: ¿necesitas predecir un número o generar contenido y lenguaje?
  7. [gestion_inventario]
    titulo: Gestión Eficiente de Inventario | mundo: core
    resumen: El inventario representa efectivo congelado que la empresa no puede usar para otros fines. El reto es minimizar el inventario sin generar quiebres de stock que insatisfagan a los clientes. Múltiples áreas de la empresa (ventas, ingeniería, producción) afectan los niveles de inventario a través de decisiones sobre personalización de productos, versiones y eficiencia de planta.
  8. [erp_systems]
    titulo: Sistemas ERP (Enterprise Resource Planning) | mundo: core
    resumen: Los sistemas ERP recopilan datos de múltiples funciones de la empresa (finanzas, procura, manufactura, cumplimiento de órdenes, RRHH, logística) y ofrecen una vista orientada a procesos que atraviesa departamentos funcionales. Se enfocan principalmente en ejecutar y monitorear transacciones diarias, careciendo a menudo de capacidades analíticas avanzadas.

### MV-C07
- NODO DEL NUCLEO SIN CAMINO [innovacion_tipo_ii]
    titulo: Innovación Tipo II (Más grande/Más pequeño/Combinación) | mundo: core
    resumen: Técnica de generación de ideas basada en tres categorías simples: hacer algo más grande, más pequeño, o combinarlo con otra cosa. Es una habilidad que se puede aprender y mejorar con práctica, útil en sesiones de brainstorming para innovar productos, servicios o estrategias sin necesidad de ser un genio creativo nato.
- CANDIDATOS A PREDECESOR (nucleo)
  1. [innovacion_abierta]
    titulo: Innovación Abierta (Open Innovation) | mundo: core
    resumen: Estrategia para generar ideas de nuevos productos aprovechando fuentes externas a la organización, superando el síndrome NIH ('not invented here'). Incluye seis métodos: socios/proveedores, comunidad técnica externa, pequeñas empresas y startups, diseños externos de producto (crowdsourcing), envío externo de ideas, y concursos externos de ideas. El método más popular y efectivo es trabajar con socios y proveedores.
  2. [mash_ups]
    titulo: Mash-Ups (Combinación de Conceptos) | mundo: core
    resumen: Ejercicio de pensamiento que combina dos marcas o conceptos existentes para explorar ideas nuevas de forma acelerada. Consiste en aislar una cualidad deseada (ej. eficiencia, exclusividad) y preguntarse qué marca o servicio real encarna esa cualidad, para luego aplicar esa lógica al reto de diseño propio (ej. '¿Cuál sería la versión Facebook de una cuenta de ahorros?').
  3. [portafolio_innovacion_diversificado]
    titulo: Portafolio Diversificado de Innovación (Silver Buckshot) | mundo: core
    resumen: No existe una bala de plata para la innovación; se necesita 'munición de plata' (silver buckshot). Es necesario gestionar un portafolio diversificado que abarque desde ideas incrementales de corto plazo (mejorar el producto actual) hasta ideas revolucionarias de largo plazo, aceptando que la mayoría del esfuerzo estará en lo incremental, pero sin dejar de invertir en lo disruptivo para evitar ser sorprendidos por la competencia.
  4. [bundle_ideas]
    titulo: Agrupa tus ideas en un solo sistema (bundle ideas) | mundo: core
    resumen: Es la manera de pasar de tener varias ideas sueltas a construir una solución completa: tomas los mejores elementos de distintas ideas y los combinas para que funcionen juntos como un sistema. En vez de quedarte con una sola idea ganadora, buscas combinaciones que resuelvan más partes del reto que tienes entre manos, descartando lo que no encaje y completando con ideas nuevas los huecos que queden en la logística.
  5. [estrategia_de_innovacion_y_tecnologia]
    titulo: Estrategia de Innovación y Tecnología de Producto (Arenas Estratégicas) | mundo: core
    resumen: Un prerrequisito para la generación efectiva de ideas es contar con una estrategia de innovación de producto que defina 'arenas estratégicas' - focos de esfuerzo de I+D donde se buscarán ideas. Estas arenas deben ser atractivas (mercados grandes, en crecimiento, competencia débil) y alineadas con las competencias core de la empresa. Delimitar estos campos de búsqueda hace la búsqueda de ideas más enfocada y efectiva.
  6. [reglas_brainstorming]
    titulo: Reglas de Brainstorming Efectivo | mundo: core
    resumen: Conjunto de reglas para maximizar la generación de ideas útiles en sesiones de lluvia de ideas: mantener el foco en un problema bien definido (idealmente centrado en la necesidad del cliente), diferir el juicio crítico, mantener una sola conversación a la vez, priorizar cantidad, pensar visualmente (Post-it) y fomentar ideas alocadas. Incluye un ejercicio de calentamiento ('Silly Cow') para desbloquear la creatividad. Las reglas no son decorado: sin ellas la sesión degenera en reunión ordenada o en caos improductivo. La sesión pertenece a la fase divergente: abre el espectro de opciones y su cosecha se filtra después, en la fase de convergencia.
  7. [starting_points_innovacion]
    titulo: Puntos de Partida para la Innovación (Push vs Pull) | mundo: core
    resumen: Las nuevas propuestas de valor no siempre parten del cliente, pero siempre deben terminar abordando jobs, pains o gains que le importan. Existen dos enfoques: Technology Push (partir de una tecnología/invención y buscar el problema que resuelve) y Market Pull (partir de un job/pain/gain manifiesto y buscar la solución/tecnología necesaria).
  8. [seis_formas_innovar_perfil_cliente]
    titulo: Seis Formas de Innovar a partir del Perfil del Cliente | mundo: core
    resumen: Una vez mapeado el customer profile, existen seis palancas para innovar: abordar más jobs, cambiar a un job más importante, ir más allá de jobs funcionales (emocionales/sociales), ayudar a más clientes a lograr el job, mejorar incrementalmente el job, o lograr una mejora radical del job (creación de nuevo mercado).

### MV-C08
- NODO DEL NUCLEO SIN CAMINO [mitigacion_efecto_latigo]
    titulo: Mitigación del Efecto Látigo: Cinco Factores Causales | mundo: core
    resumen: Existen cinco factores que generan el efecto látigo y sus respectivas estrategias de mitigación: (1) pronóstico de demanda basado en pedidos en lugar de datos de punto de venta reales; (2) agrupamiento de pedidos (order batching) por costos de procesamiento/transporte; (3) racionamiento de producto que induce 'shortage gaming'; (4) fluctuación de precios que genera compras anticipadas; y (5) incentivos de desempeño desalineados (ej. cuotas de fin de mes). Cada factor requiere una intervención específica: compartir datos POS, reducir costos de pedido, basar el racionamiento en históricos, aplicar precios estables ('everyday low prices'), y alinear incentivos con costeo basado en actividades (ABC).
- CANDIDATOS A PREDECESOR (nucleo)
  1. [trade_off_responsividad_eficiencia]
    titulo: Balance entre Capacidad de Respuesta y Eficiencia | mundo: core
    resumen: Cada decisión en la cadena de suministro (producción, inventario, ubicación, transporte, información) implica un trade-off entre ser más responsivo (rápido, flexible, capaz de atender picos de demanda) o más eficiente (bajo costo, alta utilización de activos). El mercado que se sirve determina qué extremo priorizar: mercados masivos sensibles al precio requieren eficiencia; mercados que valoran servicio y conveniencia requieren capacidad de respuesta.
  2. [pronostico_de_demanda_variables]
    titulo: Pronóstico de Demanda: Cuatro Variables Clave | mundo: core
    resumen: Todo pronóstico de demanda depende de cuatro variables: Oferta (número de proveedores y lead times), Demanda (crecimiento, estacionalidad, madurez del mercado), Características del producto (si es sustituible, complementario, nuevo o maduro) y Entorno competitivo (participación de mercado, promociones, guerras de precios). Cuanta más incertidumbre haya en estas variables, más difícil y menos preciso será el pronóstico.
  3. [driver_de_inventario]
    titulo: Driver de Inventario: Ciclico, de Seguridad y Estacional | mundo: core
    resumen: El inventario es uno de los drivers de la cadena de suministro, y se dimensiona en tres partes que responden a preguntas distintas. El inventario ciclico sale de balancear lo que cuesta ordenar contra lo que cuesta mantener: pedir mas seguido encarece las ordenes y pedir de mas encarece el almacen. El inventario de seguridad no depende del promedio de la demanda sino de su variabilidad y de lo que te cuesta quedarte sin stock. Y el estacional obliga a una eleccion de fondo: acumular antes del pico o invertir en flexibilidad de produccion para no acumular. Las tres se sostienen sobre los puntos de reorden, y esos se ajustan con datos reales de demanda, no con los del plan original.
  4. [metricas_servicio_cliente_bts_bto]
    titulo: Métricas de Servicio al Cliente: Build-to-Stock vs Build-to-Order | mundo: core
    resumen: Existen dos modelos operativos con métricas de servicio distintas. Build-to-Stock (BTS) aplica a productos commodity que deben estar disponibles de inmediato (medido por fill rate de orden completa y de línea de producto). Build-to-Order (BTO) aplica a productos personalizados por pedido (medido por tiempo de respuesta cotizado y tasa de cumplimiento a tiempo). Elegir y medir el modelo correcto es esencial para alinear expectativas del cliente con la operación.
  5. [metodos_de_pronostico]
    titulo: Métodos de Pronóstico: Cualitativo, Causal, Series de Tiempo y Simulación | mundo: core
    resumen: Existen cuatro métodos básicos de pronóstico que suelen combinarse: (1) Cualitativo, basado en intuición y comparación con productos similares, útil cuando hay poca data histórica; (2) Causal, que asume relación fuerte entre demanda y factores externos como precio o tasas de interés; (3) Series de tiempo, el más común, que usa patrones históricos (promedios móviles, suavizado exponencial) y funciona mejor en mercados estables; (4) Simulación, que combina métodos causales y de series de tiempo para modelar escenarios hipotéticos. Los pronósticos de corto plazo y agregados son más precisos que los de largo plazo o muy segmentados, y siempre existe un margen de error que debe planificarse.
  6. [demand_curve_pricing]
    titulo: Curva de Demanda y Estrategia de Precios | mundo: core
    resumen: La curva de demanda busca la intersección óptima entre volumen de ventas y beneficio neto. Un precio muy bajo puede generar demanda masiva pero ser insostenible si el costo de producción no escala; hay que considerar precio unitario, múltiplos, suscripciones, descuentos por volumen y cómo el precio puede usarse para atraer más usuarios o aumentar la frecuencia de compra.
  7. [seleccion_de_proveedores_por_costo_total]
    titulo: Seleccion de Proveedores por Costo Total Ponderado | mundo: core
    resumen: Elegir proveedor por el precio unitario mas bajo es decidir con la mitad de la informacion. Lo que de verdad cuesta trabajar con un proveedor incluye la calidad que entrega, su cumplimiento y el control que tiene sobre sus procesos, y esos criterios no pesan igual en todos los negocios. El acto propio es armar la comparacion antes de firmar: definir que criterios cualitativos importan, repartir el peso entre el costo monetario y esos criterios, calcular el costo total ponderado de cada proveedor y compararlos con esa cifra en vez de con el precio de lista. Y hay una decision que va con la misma logica: concentrar el volumen en menos proveedores da poder de negociacion, asi que la lista de preferidos se arma a proposito y no por acumulacion.
  8. [gestion_inventario]
    titulo: Gestión Eficiente de Inventario | mundo: core
    resumen: El inventario representa efectivo congelado que la empresa no puede usar para otros fines. El reto es minimizar el inventario sin generar quiebres de stock que insatisfagan a los clientes. Múltiples áreas de la empresa (ventas, ingeniería, producción) afectan los niveles de inventario a través de decisiones sobre personalización de productos, versiones y eficiencia de planta.

### MV-C09
- NODO DEL NUCLEO SIN CAMINO [planificacion_gobierno_organizaciones_familiares]
    titulo: Cómo organizar el mando y la sucesión en un negocio familiar (gobierno corporativo) | mundo: core
    resumen: Si tu negocio es familiar, como más del 70% de las organizaciones registradas en el mundo, necesitas pensar el mando de otra manera, sobre todo cuando te acercas al momento de dejar el timón. Busca ayuda externa de alguien que conozca el tema para armar un plan maestro que incluya un consejo familiar, una junta directiva profesional y la entrada gradual de familiares, gerentes clave y directores externos independientes con la formación necesaria.
- CANDIDATOS A PREDECESOR (nucleo)
  1. [framework_tres_rs_sucesion]
    titulo: Los Tres Rs para Gestionar la Sucesión del Fundador | mundo: core
    resumen: Marco para que un nuevo CEO gane el apoyo del fundador que reemplaza, basado en tres pilares: Relaciones (construir confianza mutua antes de asumir el cargo), Roles (redefinir gradualmente las funciones del fundador, alejándolo de tareas operativas hacia decisiones estratégicas o proyectos especiales) y Recompensas (asegurar beneficios financieros tangibles, como un buyout parcial o bonos de transición, que compensen la pérdida de control).
  2. [identificacion_necesidad_sucesion_ceo]
    titulo: Cuándo tu negocio necesita cambiar de líder al mando (sucesión del CEO fundador) | mundo: core
    resumen: Tu negocio pasa por etapas de crecimiento, desde el arranque veloz inicial (speedboat) hasta convertirse en una empresa grande y estable (oil tanker), y cada etapa pide capacidades de liderazgo distintas. Tienes que revisar todo el tiempo si quien dirige tiene las habilidades que la etapa actual exige, aplicando primero acompañamiento y solo después, si no mejora, un reemplazo.
  3. [founder_ceo_succession_process]
    titulo: El reemplazo del fundador como director general (CEO) | mundo: core
    resumen: A medida que tu negocio crece, es probable que dejes de ser tú quien dirige la empresa: más de la mitad de los fundadores son reemplazados en ese puesto, típicamente hacia la tercera ronda de inversión. Esto puede pasar porque decides dar un paso al costado, porque los resultados no llegan (lo que aumenta mucho la probabilidad de que la junta busque a alguien externo), o incluso por éxito: lograste desarrollar el producto y conseguir fondos, pero te faltan las habilidades que pide la siguiente etapa, como ventas, marketing o coordinar varias áreas a la vez. Quien dispara el cambio importa: la junta inicia el 73% de estas sucesiones, y solo el 27% las inicia el propio fundador. Si te reemplazan, puedes seguir en la empresa como ejecutivo o miembro de la junta, y que la transición funcione depende de quién te sucede y de cómo se maneje el cambio.
  4. [transicion_jerarquia_startup]
    titulo: De repartir todo por igual a tener un líder claro | mundo: core
    resumen: Cuando arrancas, decidir todo entre todos funciona. Pero a medida que tu negocio crece, ese modo de trabajar se vuelve lento y empieza a costarte oportunidades: necesitas una estructura más clara, con alguien al mando. Esta transición suele doler porque tú y tus socios ya se acostumbraron a decidirlo todo juntos, y ceder control específico genera roces. Muchas veces son los inversionistas externos quienes te obligan a dar este paso, porque no invierten si no ven a alguien claramente a cargo.
  5. [transicion_post_sucesion]
    titulo: Cómo manejar tu rol después de que alguien más toma el mando | mundo: core
    resumen: A diferencia de las grandes empresas, donde si te reemplazan como líder principal sueles irte del todo, en las startups es más común que te quedes trabajando en el negocio y en el consejo, sobre todo si fuiste tú quien impulsó el cambio. Esto trae riesgos: resistencia oculta y confusión entre tu equipo sobre a quién debe hacerle caso. También trae beneficios: se conserva lo que tú sabes del negocio y las relaciones que tienes con tus clientes.
  6. [revisiones_regulares_desempeno_ceo]
    titulo: Revisiones Regulares y Escritas del Desempeño del Fundador-CEO | mundo: core
    resumen: Para reducir el riesgo de sorpresas desagradables y facilitar futuras transiciones, el consejo debe realizar evaluaciones periódicas, honestas y documentadas del desempeño del fundador-CEO. Esto construye confianza, provee retroalimentación de desarrollo continua, y sienta las bases para una sucesión más fluida cuando sea necesaria.
  7. [sucesion_iniciada_por_fundador]
    titulo: Sucesión Iniciada por el Fundador vs. por la Junta | mundo: core
    resumen: Distingue dos formas de gatillar el reemplazo del CEO fundador: cuando el fundador mismo reconoce la necesidad de cambio y lo inicia ('adelantarse a la junta'), versus cuando la junta directiva lo impone. Los datos muestran que cuando el fundador inicia el proceso, tiene mayor probabilidad de permanecer en un rol senior, participar en la elección del sucesor y seguir en el consejo directivo, en lugar de ser expulsado abruptamente.
  8. [planificacion_sucesion_ceo]
    titulo: El Dilema de la Sucesión del CEO: Interno vs. Externo | mundo: core
    resumen: La sucesión de un CEO es una de las decisiones más difíciles de una organización. Los candidatos internos suelen superar a los externos por su conocimiento profundo de tecnología, cultura y personas, pero surge el dilema de si promover a alguien del equipo ejecutivo (probablemente un 'Two') o buscar profundo en la organización a un 'One' con visión estratégica, arriesgando la rotación masiva del equipo actual (como hizo GE con Jack Welch). No existe una fórmula perfecta: promover un Two puede ralentizar decisiones estratégicas futuras, mientras promover un One no reconocido puede causar fricción y salida de talento.

### MV-C10
- NODO DEL NUCLEO SIN CAMINO [plantea_oferta_como_rango_o_cifra_precisa]
    titulo: Plantea tu oferta como un rango o con una cifra precisa, no redonda | mundo: core
    resumen: En lugar de dar una cifra fija y redonda cuando te preguntan tu precio, plantea un rango donde el número más bajo sea justo el que en realidad esperas recibir, o da una cifra exacta y no redonda. Ambas formas transmiten que hiciste un cálculo cuidadoso, en vez de improvisar un número al azar, y dejan menos margen para que te empujen hacia abajo. Un rango bien pensado amplía la referencia de la otra parte hacia arriba sin que parezca una posición extrema. Una cifra exacta, en lugar de un número redondeado, transmite que hiciste cálculos reales. Esto importa especialmente cuando no conoces con certeza el valor de mercado de lo que negocias.
- CANDIDATOS A PREDECESOR (nucleo)
  1. [orden_negociacion_puntos]
    titulo: En qué orden negociar los puntos de tu acuerdo (term sheet) | mundo: core
    resumen: El orden en que hablas de cada punto del acuerdo cambia el resultado. Si tienes poca experiencia negociando, conviene empezar por lo fácil de acordar para generar buena onda, dejar la valuación para el final porque suele necesitar más vueltas de conversación, y evitar entrar tema por tema sin ver el panorama completo cuando es la otra parte quien controla el proceso.
  2. [factores_valoracion_startup]
    titulo: Qué determina cuánto vale tu empresa para un inversionista | mundo: core
    resumen: Cuánto te ofrece un inversionista no es una ciencia exacta. Se mezcla lo medible con lo que no lo es: en qué etapa estás, cuánta competencia hay entre quienes quieren financiarte, la experiencia de tu equipo, el tamaño y la tendencia de tu mercado, el momento en que entra cada inversionista, tus números (ingresos, ganancia operativa, cuánto dinero quemas al mes) y el clima económico general. Concéntrate en lo que sí puedes controlar: generar competencia real entre los interesados.
  3. [tipos_adquisiciones_tecnologia]
    titulo: Tipos de compra de tu empresa (adquisiciones) | mundo: core
    resumen: Cuando alguien quiere comprarte, hay tres lógicas distintas de valor: (1) te compran por el equipo o la tecnología (precio en tu mercado); (2) te compran el producto para venderlo con su propia fuerza comercial (precio mayor que el anterior); (3) te compran el negocio completo, con sus ingresos y ganancias, valorado por métricas financieras. Entender cuál de las tres te están ofreciendo es clave para negociar bien.
  4. [contrarrestar_argumento_mercado]
    titulo: Responde al Argumento de 'Así es el Mercado' | mundo: core
    resumen: Los inversionistas y abogados con experiencia a veces usan la frase 'es lo que marca el mercado' (en inglés, 'es market') para justificar condiciones sin darte razones de fondo. Es una táctica de negociación floja. Tienes que preguntar por qué esa condición aplica justo a tu caso, en lugar de aceptarla sin cuestionarla.
  5. [negociacion_con_plazos_artificiales]
    titulo: Fechas Límite Artificiales para Forzar Decisiones en una Negociación | mundo: core
    resumen: Cuando estás vendiendo un activo, negociando una fusión o una compra, y el tiempo juega en tu contra, te conviene poner fechas límite artificiales y avisarlas a varios compradores potenciales al mismo tiempo. Eso genera urgencia, evita que el proceso se alargue sin fin y aprovecha que hay varios interesados compitiendo entre sí para cerrar el trato antes y en mejores condiciones para ti.
  6. [disciplina_rigurosa_proceso_ventas]
    titulo: Ten disciplina rigurosa en tu proceso de ventas | mundo: core
    resumen: Un pronostico de ventas (forecast) optimista basado en supuestos sin verificar, como pensar que la persona que te apoya adentro (champion) ya te aseguro todo, es peligroso. Antes de dar por segura una oportunidad, habla directamente con todas las personas que deciden, no solo con tu contacto principal, incluyendo sus pares y jefes. Revisa cada negociacion en voz alta frente a tu equipo de ventas para mantener el estándar alto y evitar la comodidad.
  7. [estructura_de_la_venta]
    titulo: Cómo estructurar la venta: cobrar todo de una vez (cash-only) o cobrar por metas cumplidas (earn-out) | mundo: core
    resumen: Cuando negocias la venta de tu negocio, tienes que elegir (o negociar) entre dos formas de cobrar: todo en efectivo de una vez por tus acciones, o en pagos futuros que dependen de que el negocio cumpla ciertas metas después de la venta (earn-out). Si confías en el futuro del negocio, el earn-out te puede convenir: te permite pedir más dinero y le muestra al comprador que crees en lo que construiste. Pero tiene riesgos: puedes perder el control sobre decisiones que afectan si esas metas se cumplen, y puedes quedarte sin ese dinero por cosas que no dependen de ti, como cambios del mercado o que el comprador cambie de prioridades.
  8. [gates_tempranos_flexibles]
    titulo: No exijas números exactos demasiado pronto | mundo: core
    resumen: Al principio de una idea nueva no estás decidiendo todo o nada: estás pagando un poco para ver si vale la pena seguir explorando, como quien compra una opción. Si le pides a una idea recién nacida un cálculo financiero detallado (retorno esperado, ganancia proyectada), cuando los datos todavía son puras suposiciones, la puedes matar antes de tiempo.

### MV-C11
- NODO DEL NUCLEO SIN CAMINO [posicionamiento_est]
    titulo: Elige en qué vas a ser el mejor (y renuncia al resto) | mundo: core
    resumen: Según un estudio de McMillan Doolittle, tienes que ser el mejor en al menos una de cinco cosas: el que tiene más variedad, el más barato, el más fácil de usar, el más rápido o el más de moda. Si intentas destacar en más de dos a la vez, terminas siendo mediocre en todas. Elegir en qué destacar significa aceptar que vas a sacrificar otras cosas a propósito.
- CANDIDATOS A PREDECESOR (nucleo)
  1. [producto_unico_superior]
    titulo: Tener un Producto Único y Superior: El Factor Número Uno de Rentabilidad | mundo: core
    resumen: Lo que más determina si tu producto nuevo tiene éxito es que sea diferente y le ofrezca al cliente beneficios únicos con una propuesta de valor convincente. Si logras un producto superior, tienes 5 veces más probabilidad de éxito, 4 veces más participación de mercado y 4 veces más rentabilidad. Define esa superioridad desde la mirada de tu cliente, no desde lo técnico: las características (features) te cuestan dinero a ti, y los beneficios (benefits) son lo que tu cliente realmente compra y por lo que está dispuesto a pagar. Piensa en tu producto como un conjunto de beneficios para quien lo usa, no como una lista de funciones técnicas. Evita caer en copiar lo que ya existe sin diferenciarte, y evita también desarrollar una solución técnica que después sale a buscar un mercado que la quiera.
  2. [brief_competitivo]
    titulo: Escribe tu análisis de la competencia (brief competitivo) | mundo: core
    resumen: Una vez que tienes claro qué tipo de mercado es el tuyo, escribe un análisis que explique por qué y cómo tu producto es mejor que las alternativas que ya existen. Incluso en un mercado nuevo, donde la 'competencia' es la forma actual, ineficiente o inexistente, en que la gente resuelve el problema. Lo que buscas entender no es una lista de características, sino por qué compra la gente.
  3. [ventaja_competitiva_producto]
    titulo: Construye una ventaja competitiva real y una propuesta de valor que convenza | mundo: core
    resumen: Uno de los mayores impulsores de rentabilidad en un producto nuevo es que sea realmente superior: con beneficios diferenciados y una propuesta de valor que convenza a quien la escucha. Es fácil caer en la trampa de repetir lo que ya haces y terminar con un producto calcado a los que ya existen. Antes de avanzar en cada revisión de tu proyecto (gate), exígete evidencia de que tu producto es superior, preguntándote: ¿tiene ese factor sorpresa? ¿resuelve un problema importante para tu cliente? ¿ofrece una ventaja clara frente a lo que ya hay en el mercado?
  4. [enfoque_motor_unico_crecimiento]
    titulo: Enfócate en un Solo Motor de Crecimiento | mundo: core
    resumen: Es posible que tu negocio tenga más de un motor de crecimiento en marcha (viral, de retención o pegajoso, y de pago), pero la experiencia muestra que los negocios que despegan de verdad se concentran en uno solo a la vez. Si intentas vigilar los tres motores al mismo tiempo, terminas confundido sobre qué mirar y qué mover. Conviene perseguir un motor a fondo antes de pensar en cambiar hacia otro.
  5. [desarrollar_posicionamiento_empresa]
    titulo: Desarrollo del Posicionamiento de Empresa | mundo: core
    resumen: A diferencia del posicionamiento de producto (atributos específicos), el posicionamiento de empresa responde a '¿qué hace esta empresa por mí?', '¿por qué querría hacer negocios con ellos?' y '¿por qué existe esta empresa y en qué es diferente?'. Debe ser simple, centrado en el cliente y evitar superlativos no sustentables como 'el mejor' o 'el más fácil', prefiriendo afirmaciones demostrables como 'el más rápido'.
  6. [marco_analisis_mercado_cadena_suministro]
    titulo: Cómo entender tu mercado para encontrar oportunidades en tu cadena de suministro | mundo: core
    resumen: Antes de decidir dónde enfocar tus esfuerzos, necesitas entender en qué tipo de mercado te mueves: uno maduro, uno en desarrollo o uno estable. Cada tipo te exige destacar en algo distinto: atención al cliente, eficiencia interna, capacidad de adaptarte a la demanda o desarrollo de producto. Tu tarea es identificar en cuál de estas áreas necesitas ser mejor que tu competencia.
  7. [checklist_mejores_apuestas_modelo_negocio]
    titulo: Tu última revisión antes de apostar todo (best bets) | mundo: core
    resumen: Antes de comprometerte a ejecutar, revisa con método si elegiste la mejor propuesta de valor, el momento óptimo para entregarla, y el modelo de ingresos y costos más eficiente. Busca cambios de juego (game changers) o patrones de negocio poco obvios, como convertir una venta basada en funciones en una experiencia de marca, o pasar de vender unidades sueltas a un modelo con efectos de red.
  8. [analisis_competitivo]
    titulo: Análisis Competitivo para Identificar Oportunidades | mundo: core
    resumen: No se trata de copiar a los competidores, sino de analizar sus éxitos y fracasos (directos e indirectos) para obtener insights sobre qué se necesita hacer a continuación. Una estrategia de 'fast-follower' bien ejecutada, basada en identificar debilidades de los competidores líderes, puede ser muy exitosa.

### MV-C12
- NODO DEL NUCLEO SIN CAMINO [sales_operations_planning]
    titulo: Planificación de Ventas y Operaciones (S&OP) | mundo: core
    resumen: El S&OP es un proceso de negocio cross-funcional (ventas, operaciones, finanzas, desarrollo de producto) que se ejecuta mensualmente para mantener el balance entre oferta y demanda a nivel agregado. Toma un enfoque 'outside-in', considerando primero factores externos (clientes, competidores) antes de ajustar planes internos, y vincula el plan estratégico con la ejecución diaria.
- CANDIDATOS A PREDECESOR (nucleo)
  1. [proceso_sop_mop]
    titulo: Planeación Colaborativa S&OP / M&OP (Sales & Operations / Mission & Operations Planning) | mundo: core
    resumen: El S&OP (Sales & Operations Planning) es una práctica empresarial de planeación colaborativa cíclica (cada 15-30 días) que se puede adaptar como M&OP (Mission & Operations Planning) para respuesta a desastres. Consta de cinco pasos: (1) órdenes de misión/CONOPS, (2) planeación de demanda, (3) planeación de oferta, (4) conciliación de planes mediante modelado y simulación en mapas digitales, y (5) implementación y monitoreo continuo. Permite que múltiples organizaciones con agendas distintas lleguen a consenso rápido usando datos visuales compartidos.
  2. [roadmap_proyectos_operacionales_12_meses]
    titulo: Plan de proyectos para mejorar tus operaciones en 12 meses (roadmap) | mundo: core
    resumen: Para convertir tu estrategia de capacidades de mercado en acciones concretas, identifica las operaciones específicas de tu negocio (pronóstico de demanda, gestión de inventario, gestión de pedidos, programación de entregas, procesamiento de devoluciones) y define proyectos priorizados con un cronograma. Cada proyecto debe conectarse directamente con un requerimiento de desempeño que puedas medir.
  3. [produccion_scheduling_balance_objetivos]
    titulo: Programación de Producción: Balance entre Objetivos Competitivos | mundo: core
    resumen: La programación de producción asigna la capacidad disponible (equipo, mano de obra, instalaciones) al trabajo que debe realizarse, buscando el equilibrio óptimo entre tres objetivos que compiten entre sí: altas tasas de utilización (economías de escala mediante corridas largas), bajos niveles de inventario (corridas cortas y entrega justo a tiempo) y altos niveles de servicio al cliente (evitar quiebres de stock). No es posible maximizar los tres simultáneamente, por lo que la gestión de operaciones consiste en encontrar el balance adecuado según la estrategia del negocio.
  4. [trade_off_responsividad_eficiencia]
    titulo: Balance entre Capacidad de Respuesta y Eficiencia | mundo: core
    resumen: Cada decisión en la cadena de suministro (producción, inventario, ubicación, transporte, información) implica un trade-off entre ser más responsivo (rápido, flexible, capaz de atender picos de demanda) o más eficiente (bajo costo, alta utilización de activos). El mercado que se sirve determina qué extremo priorizar: mercados masivos sensibles al precio requieren eficiencia; mercados que valoran servicio y conveniencia requieren capacidad de respuesta.
  5. [pronostico_de_demanda_variables]
    titulo: Pronóstico de Demanda: Cuatro Variables Clave | mundo: core
    resumen: Todo pronóstico de demanda depende de cuatro variables: Oferta (número de proveedores y lead times), Demanda (crecimiento, estacionalidad, madurez del mercado), Características del producto (si es sustituible, complementario, nuevo o maduro) y Entorno competitivo (participación de mercado, promociones, guerras de precios). Cuanta más incertidumbre haya en estas variables, más difícil y menos preciso será el pronóstico.
  6. [dependency_analysis]
    titulo: Análisis de Dependencias | mundo: core
    resumen: Responde a la pregunta: '¿Qué debe suceder, fuera de nuestro control, para vender nuestro producto a gran volumen?'. Identifica cambios tecnológicos, de comportamiento del consumidor, regulatorios o económicos externos necesarios para el éxito del negocio, junto con planes de contingencia si no ocurren.
  7. [scor_model_operaciones]
    titulo: Modelo SCOR: Marco de Operaciones de Cadena de Suministro | mundo: core
    resumen: El modelo SCOR (Supply Chain Operations Reference) es un marco estandarizado y reconocido mundialmente para analizar y mejorar el desempeño de la cadena de suministro. Organiza las operaciones en seis procesos de alto nivel: Planificar, Abastecer, Fabricar, Entregar, Devolver y Habilitar. Provee un lenguaje común, métricas estándar (KPIs de confiabilidad, capacidad de respuesta, agilidad, costo y gestión de activos) y permite benchmarking entre empresas. La versión más reciente, SCOR DS, incorpora resiliencia, sostenibilidad y procesos digitales.
  8. [portfolio_management]
    titulo: Gestión de Portafolio de Proyectos (Portfolio Management) | mundo: core
    resumen: La gestión de portafolio es un proceso dinámico de decisión mediante el cual se evalúan, seleccionan, priorizan y reasignan recursos entre los proyectos activos de desarrollo de nuevos productos de una empresa. Busca balance entre riesgo/retorno, corto/largo plazo y mantenimiento/crecimiento, asegurando que los recursos escasos se inviertan en los proyectos correctos.

### MV-C13
- NODO DEL NUCLEO SIN CAMINO [sop_colaborativo]
    titulo: Proceso Colaborativo S&OP (Sales and Operations Planning) en 5 Pasos | mundo: core
    resumen: Un proceso simplificado de S&OP guiado por simulaciones, ejecutado en ciclos (ej. cada 30 días): (1) Pronóstico de demanda y precios, (2) Plan de demanda por instalación, (3) Plan de suministro (producción/rutas), (4) Modelado y simulación para detectar discrepancias entre demanda y suministro, y (5) Ajuste y consenso del plan operativo final. Este proceso convierte datos en un plan operativo compartido y revisado continuamente por todos los actores de la cadena.
- CANDIDATOS A PREDECESOR (nucleo)
  1. [proceso_sop_mop]
    titulo: Planeación Colaborativa S&OP / M&OP (Sales & Operations / Mission & Operations Planning) | mundo: core
    resumen: El S&OP (Sales & Operations Planning) es una práctica empresarial de planeación colaborativa cíclica (cada 15-30 días) que se puede adaptar como M&OP (Mission & Operations Planning) para respuesta a desastres. Consta de cinco pasos: (1) órdenes de misión/CONOPS, (2) planeación de demanda, (3) planeación de oferta, (4) conciliación de planes mediante modelado y simulación en mapas digitales, y (5) implementación y monitoreo continuo. Permite que múltiples organizaciones con agendas distintas lleguen a consenso rápido usando datos visuales compartidos.
  2. [information_driver_supply_chain]
    titulo: El Rol de la Información como Driver de la Cadena de Suministro | mundo: core
    resumen: La información es el conector entre todas las actividades de tu cadena de suministro y la base para tomar decisiones sobre los otros drivers: producción, inventario, ubicación y transporte. Cuanto más precisa, oportuna y completa sea la información que compartes con proveedores y clientes, mejores decisiones podrás tomar, maximizando la rentabilidad conjunta. La información cumple dos funciones: coordinar actividades diarias, como la programación de producción, los niveles de inventario y las rutas de transporte, y sustentar pronósticos de demanda, tanto a nivel táctico (cronogramas mensuales o trimestrales) como estratégico (decisiones de expansión o entrada y salida de mercados).
  3. [scor_model_operaciones]
    titulo: Modelo SCOR: Marco de Operaciones de Cadena de Suministro | mundo: core
    resumen: El modelo SCOR (Supply Chain Operations Reference) es un marco estandarizado y reconocido mundialmente para analizar y mejorar el desempeño de la cadena de suministro. Organiza las operaciones en seis procesos de alto nivel: Planificar, Abastecer, Fabricar, Entregar, Devolver y Habilitar. Provee un lenguaje común, métricas estándar (KPIs de confiabilidad, capacidad de respuesta, agilidad, costo y gestión de activos) y permite benchmarking entre empresas. La versión más reciente, SCOR DS, incorpora resiliencia, sostenibilidad y procesos digitales.
  4. [definicion_alineacion_cadena_suministro]
    titulo: Definición y Alineación de la Cadena de Suministro con la Estrategia | mundo: core
    resumen: Una cadena de suministro es la red de empresas y actividades necesarias para diseñar, fabricar, entregar y usar un producto o servicio. Toda empresa participa en una o más cadenas de suministro y debe entender el rol que juega en ellas. La gestión de la cadena de suministro (SCM) es la coordinación sistémica de producción, inventario, ubicación y transporte entre los participantes para lograr el mejor balance entre capacidad de respuesta y eficiencia según el mercado servido. La estrategia de la empresa (competir por precio vs. por servicio/conveniencia) debe determinar el diseño de su cadena de suministro.
  5. [supply_chain_management_systems]
    titulo: Sistemas de Gestión de Cadena de Suministro (SCM) | mundo: core
    resumen: Los sistemas SCM son suites de aplicaciones integradas (planificación avanzada, planificación de transporte, planificación de demanda, gestión de inventario) que dependen de datos de sistemas ERP y ofrecen capacidades analíticas para la toma de decisiones estratégicas y tácticas en la cadena de suministro.
  6. [gestion_pedidos_order_management]
    titulo: Gestión de Pedidos (Order Management) | mundo: core
    resumen: Proceso de transmitir información de pedidos desde clientes hacia atrás en la cadena de suministro (minoristas, distribuidores, proveedores de servicios, productores) y devolver información de fechas de entrega, sustituciones y pedidos pendientes. Se rige por cuatro principios: ingresar los datos del pedido una sola vez y capturarlos electrónicamente en la fuente original; automatizar el manejo de pedidos rutinarios y reservar la intervención humana para excepciones; hacer visible el estado del pedido a clientes y agentes de servicio; e integrar los sistemas de gestión de pedidos con otros sistemas relacionados (inventario, precios, facturación) para mantener la integridad de los datos.
  7. [trade_off_responsividad_eficiencia]
    titulo: Balance entre Capacidad de Respuesta y Eficiencia | mundo: core
    resumen: Cada decisión en la cadena de suministro (producción, inventario, ubicación, transporte, información) implica un trade-off entre ser más responsivo (rápido, flexible, capaz de atender picos de demanda) o más eficiente (bajo costo, alta utilización de activos). El mercado que se sirve determina qué extremo priorizar: mercados masivos sensibles al precio requieren eficiencia; mercados que valoran servicio y conveniencia requieren capacidad de respuesta.
  8. [cinco_pasos_enfoque_restricciones]
    titulo: Los Cinco Pasos de Enfoque para Gestionar Restricciones | mundo: core
    resumen: Metodología práctica derivada de la Teoría de Restricciones para identificar y gestionar los cuellos de botella de un sistema (fábrica o cadena de suministro) de forma iterativa: identificar, explotar, subordinar, elevar y repetir el ciclo cuando la restricción se traslada.
