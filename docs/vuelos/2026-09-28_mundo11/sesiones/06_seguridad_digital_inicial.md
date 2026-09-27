# Sesion 6: seguridad_digital / inicial

- id: 8d8f5a43-18ef-4e16-985e-b924264c0aa9
- creada: 2026-09-27T21:21:26.330805+00:00
- cerrada: 2026-09-27T21:23:54.32+00:00
- puerta de entrada: Redacta tu Plan de Seguridad (`getting_started_planning`)
- coste USD: 0.2012
- desglose: {"plan": 0.0511083, "turnos": 0.03203735, "estado_vivo": 0.00411, "juez_sesion": 0.004128, "estimacion_banda": 0.031206, "enlace_proteccion": 0.03414, "anclaje_proteccion": 0.044502}
- fase final del recorrido: cerrada
- prioridad declarada: {"texto": "ordenar contraseñas y quién puede entrar a las cuentas, proteger datos de clientes, especialmente Instagram", "conteo": 4}

## Mensaje de entrada

Exploración del mundo "Seguridad Digital" (Blinda tus datos, tus cuentas y la confianza de tus clientes.) para mi idea. Contexto actual: El negocio tiene viabilidad financiera confirmada con margen de $120 por unidad y quince ventas que ya cubren costos fijos, pero la pregunta central sigue siendo qué lo diferencia: si vende macetas básicas sensibles al precio o productos con valor percibido que justifiquen márgenes mayores. La feria de agosto es la oportunidad para validar esto mediante conversación directa con clientes mientras compran.

Paralelo a esa incertidumbre comercial, emergió un problema técnico concreto que erosiona ambas posibilidades: burbujas y acabados irregulares en el producto. Los clientes lo reportan y varía entre lotes, lo que sugiere causas en mezcla, curado o proceso, no en capacidad. El obstáculo inmediato es que carece de registro sistemático de defectos: revisa cada pieza al final pero no documenta variables ni pauta cuándo ocurre cada falla. Sin esos datos no puede aislar la causa raíz.

El fundador pivotó correctamente hacia prevención temprana: detectar el defecto antes de hornear, no después. Esto requiere primero un sistema mínimo de captura de datos durante cada paso del proceso que le permita correlacionar burbujas con variables como temperatura ambiente, tiempo de mezcla, o descanso del material. Hasta entonces cualquier corrección es a ciegas. El costo de esta mala calidad es doble: clientes decepcionados que no recompran y unidades rechazadas que no generan ingresos.

Resolver esto es prerequisito antes de escalar: no puede crecer con un proceso que falla sin aviso. La feria sirve tanto para entender qué valoran los clientes como para confrontar directamente si aceptan estos defectos o no, información que completará el diagnóstico del negocio real.

## Recorrido (etiqueta del riel, id, modo)

1. Redacta tu Plan de Seguridad (`getting_started_planning`, conversado)
2. Protege tus Contraseñas Correctamente (`gestion_contrasenas_cui`, salto)
3. Protege tus Medios de Almacenamiento (`getting_started_media_protection`, salto)

## Ultimas preguntas

- Entiendo que quieres ordenar tus números y tomar decisiones sobre cada parte del negocio. Cuando dices que quieres empezar ya, por donde prefieres arrancar: con los costos y el margen actualizado en la Etapa 1, o primero con el análisis de tus canales de venta en la Etapa 4?
- Sin copias de seguridad, perder el celular significa perder todo: pedidos, contactos, datos de tus 15 clientes. Ese riesgo es real y urgente. Lo que propongo es resolver esto en paralelo a ordenar las contraseñas: primero, ¿dónde guardas ahora mismo esos datos del celular, solo en el teléfono, o hay algo en la nube, aunque sea accidental?
- Si mañana perdieras acceso a tu cuenta de Instagram y con ella todo el historial que necesitas revisar en la actividad #6 para clasificar las 15 ventas por canal de origen, ¿tienes esos datos de esos clientes guardados en otro lugar (correo, papel, nube), o en este momento solo existen dentro de los mensajes de Instagram?

## Decisiones por turno (caja de vidrio)

```json
{
 "a": "Cuando la revisión bimestral de la actividad #27 te lleve a incorporar un proveedor nuevo, una plataforma diferente o algún colaborador externo para manejar tus datos de ventas, costos o conversaciones con clientes, ¿cómo vas a asegurarte de que ese nuevo elemento cumpla con los mismos criterios de seguridad y privacidad que ya tienes definidos para tu operación actual?",
 "de": "A medida que tu idea crece y necesites incorporar nuevas herramientas, plataformas o colaboradores externos para manejar información sensible, ¿cómo estás pensando en asegurar que esos nuevos sistemas o servicios cumplan con los mismos estándares de protección que ya has establecido?",
 "tipo": "anclaje_proteccion"
}
```
```json
{
 "tipo": "decision_turno",
 "decision": {
  "accion": "avanzar",
  "camino": [
   "gestion_contrasenas_cui"
  ],
  "es_salto": true
 },
 "nodo_actual": "getting_started_planning",
 "razonamiento": "El usuario declara una prioridad inmediata concreta (contraseñas y acceso) que no es del dominio del nodo actual (SP 800-171 para contratistas federales). Su situación real (Excel sin clave, datos en celular, sin estructura formal) es ajena a ese contexto regulatorio. Salto a gestión de contraseñas porque aborda su preocupación específica de forma más directa y contextualizada.",
 "saltos_posibles": [
  {
   "id": "gestion_contrasenas_cui",
   "titulo": "Gestión Segura de Contraseñas",
   "afinidad": 0.606,
   "fase_proyecto": "ejecucion",
   "condiciones_activacion": [
    "Cuando tu empresa maneja CUI por un contrato con el gobierno federal de Estados Unidos y necesita reglas para crear, compartir y renovar contraseñas de forma segura"
   ]
  },
  {
   "id": "csf_funcion_protect",
   "titulo": "Función Protect del NIST CSF 2.0",
   "afinidad": 0.537,
   "fase_proyecto": "ejecucion",
   "condiciones_activacion": [
    "Cuando ya se identificaron los activos críticos y se necesita implementar salvaguardas concretas",
    "Si el negocio no usa autenticación multifactor en sus cuentas críticas"
   ]
  },
  {
   "id": "getting_started_personnel_security",
   "titulo": "Seguridad del Personal",
   "afinidad": 0.511,
   "fase_proyecto": "ejecucion",
   "condiciones_activacion": [
    "Cuando operas o vendes en Estados Unidos como contratista del gobierno federal y contratas, despides o transfieres empleados con acceso a sistemas que procesan CUI."
   ]
  },
  {
   "id": "concientizacion_entrenamiento_cui",
   "titulo": "Concientización y Entrenamiento en Seguridad para Personal",
   "afinidad": 0.481,
   "fase_proyecto": "ejecucion",
   "condiciones_activacion": [
    "Cuando trabajas como contratista o proveedor del gobierno de Estados Unidos, manejas informacion controlada no clasificada (CUI) y debes cumplir la familia Awareness and Training de SP 800-171"
   ]
  },
  {
   "id": "funcion_protect_politica_seguridad",
   "titulo": "Función Proteger: Política de Ciberseguridad y Controles",
   "afinidad": 0.478,
   "fase_proyecto": "ejecucion",
   "condiciones_activacion": [
    "Cuando ya existe un inventario de activos",
    "Cuando la empresa carece de políticas formales de seguridad"
   ]
  },
  {
   "id": "identificacion_autenticacion_mfa",
   "titulo": "Identificación, Autenticación y Autenticación Multifactor (MFA)",
   "afinidad": 0.475,
   "fase_proyecto": "ejecucion",
   "condiciones_activacion": [
    "Cuando operas o vendes en Estados Unidos como proveedor del gobierno federal y debes cumplir los requisitos de identificación y autenticación de SP 800-171",
    "Si la organización aún depende solo de contraseñas para el acceso"
   ]
  },
  {
   "id": "monitoreo_continuo",
   "titulo": "Vigilancia Continua de tu Seguridad y Privacidad (postura de seguridad)",
   "afinidad": 0.475,
   "fase_proyecto": "ejecucion",
   "condiciones_activacion": [
    "Una vez que autorizaste tu sistema, para mantener su nivel de riesgo aceptable con el paso del tiempo.",
    "Cuando ocurren cambios importantes en tu sistema, en las personas involucradas o en el entorno donde operas."
   ]
  },
  {
   "id": "identify_mapeo_datos",
   "titulo": "Mapea tus datos y evalúa el riesgo de privacidad (Identify)",
   "afinidad": 0.467,
   "fase_proyecto": "planificacion",
   "condiciones_activacion": [
    "Cuando empiezas a construir tu manejo de privacidad desde cero",
    "Si no tienes claro qué datos personales manejas en tu negocio"
   ]
  }
 ],
 "respuesta_usuario": "Me preocupan sobre todo las contrasenas y quien puede entrar a mis cuentas, quiero ordenar eso ya. Hoy guardo los datos de mis clientes en un Excel sin clave y en el celular.",
 "candidatos_locales": [
  "getting_started_system_services_acquisition"
 ],
 "prioridad_declarada": {
  "texto": "ordenar contraseñas y quién puede entrar a las cuentas, proteger datos de clientes",
  "conteo": 1
 }
}
```
```json
{
 "a": "Empecemos por lo que te urge en este momento: en tu actividad #6, cuando abras el historial de mensajes de Instagram para rastrear el origen de tus 15 ventas, ¿cuántos datos de clientes tienes ya guardados ahi y desde hace cuánto los estás almacenando de esa forma?",
 "de": "Empecemos por lo que te urge: ese Excel con datos de clientes sin clave y en el celular. ¿cuántos clientes tienes ya registrados ahi y hace cuanto que guardas los datos asi?",
 "tipo": "anclaje_proteccion"
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
 "nodo_actual": "gestion_contrasenas_cui",
 "razonamiento": "La respuesta revela un riesgo concreto (contraseña única, sin MFA) pero no discrimina entre dos caminos posibles del nodo actual: fortaleza de contraseñas vs. respuesta ante incidentes. Repreguntar para identificar cuál es el punto de partida que el usuario necesita resolver primero. Prioridad llega a conteo=2 y debe ser reconocida sin deflexión.",
 "saltos_posibles": [
  {
   "id": "identificacion_autenticacion_mfa",
   "titulo": "Identificación, Autenticación y Autenticación Multifactor (MFA)",
   "afinidad": 0.491,
   "fase_proyecto": "ejecucion",
   "condiciones_activacion": [
    "Cuando operas o vendes en Estados Unidos como proveedor del gobierno federal y debes cumplir los requisitos de identificación y autenticación de SP 800-171",
    "Si la organización aún depende solo de contraseñas para el acceso"
   ]
  },
  {
   "id": "csf_funcion_protect",
   "titulo": "Función Protect del NIST CSF 2.0",
   "afinidad": 0.424,
   "fase_proyecto": "ejecucion",
   "condiciones_activacion": [
    "Cuando ya se identificaron los activos críticos y se necesita implementar salvaguardas concretas",
    "Si el negocio no usa autenticación multifactor en sus cuentas críticas"
   ]
  },
  {
   "id": "monitoreo_continuo",
   "titulo": "Vigilancia Continua de tu Seguridad y Privacidad (postura de seguridad)",
   "afinidad": 0.338,
   "fase_proyecto": "ejecucion",
   "condiciones_activacion": [
    "Una vez que autorizaste tu sistema, para mantener su nivel de riesgo aceptable con el paso del tiempo.",
    "Cuando ocurren cambios importantes en tu sistema, en las personas involucradas o en el entorno donde operas."
   ]
  },
  {
   "id": "implementar_controles",
   "titulo": "Implementación de Controles de Seguridad y Privacidad",
   "afinidad": 0.337,
   "fase_proyecto": "ejecucion",
   "condiciones_activacion": [
    "Cuando ya se han seleccionado los controles y se procede a su despliegue técnico u organizacional.",
    "Al descubrir que un control planificado no puede implementarse tal como se diseñó."
   ]
  },
  {
   "id": "rmf_paso_categorizar",
   "titulo": "Paso Categorizar: Clasificación de Sistemas por Impacto",
   "afinidad": 0.334,
   "fase_proyecto": "planificacion",
   "condiciones_activacion": [
    "Cuando la organización tiene múltiples sistemas con diferentes niveles de criticidad.",
    "Antes de decidir qué controles de seguridad implementar."
   ]
  },
  {
   "id": "funcion_protect_politica_seguridad",
   "titulo": "Función Proteger: Política de Ciberseguridad y Controles",
   "afinidad": 0.32,
   "fase_proyecto": "ejecucion",
   "condiciones_activacion": [
    "Cuando ya existe un inventario de activos",
    "Cuando la empresa carece de políticas formales de seguridad"
   ]
  },
  {
   "id": "gates_sin_dientes_problema",
   "titulo": "Diagnóstico: Compuertas sin Dientes (Gates with No Teeth)",
   "afinidad": 0.32,
   "fase_proyecto": "ejecucion",
   "condiciones_activacion": [
    "Si tienes demasiados proyectos activos sin claridad de cuál es prioridad",
    "Si no has cancelado ningún proyecto en el último año a pesar de tener un proceso de etapas y filtros"
   ]
  },
  {
   "id": "estructura_sp800171",
   "titulo": "Estructura de SP 800-171: 17 Familias de Requisitos de Seguridad",
   "afinidad": 0.316,
   "fase_proyecto": "planificacion",
   "condiciones_activacion": [
    "Cuando tu negocio tiene un contrato con el gobierno federal de Estados Unidos y debe implementar controles de seguridad para proteger CUI"
   ]
  }
 ],
 "respuesta_usuario": "Uso la misma contrasena para el correo, Instagram y el banco, y no tengo verificacion en dos pasos.",
 "candidatos_locales": [
  "respuesta_incidentes_cui",
  "mantenimiento_sistema_cui"
 ],
 "prioridad_declarada": {
  "texto": "ordenar contraseñas y quién puede entrar a las cuentas, proteger datos de clientes",
  "conteo": 2
 }
}
```
```json
{
 "a": "Entiendo que quieres ordenar tus números y tomar decisiones sobre cada parte del negocio. Cuando dices que quieres empezar ya, por donde prefieres arrancar: con los costos y el margen actualizado en la Etapa 1, o primero con el análisis de tus canales de venta en la Etapa 4?",
 "de": "Entiendo: misma contraseña en tres lugares críticos y sin verificación en dos pasos es un riesgo real. Cuando dices que quieres ordenar esto ya, ¿por dónde prefieres empezar: cambiar esas contraseñas a unas distintas y fuertes, o primero activar la verificación en dos pasos en el banco y el correo?",
 "tipo": "anclaje_proteccion"
}
```
```json
{
 "tipo": "decision_turno",
 "decision": {
  "accion": "avanzar",
  "camino": [
   "getting_started_media_protection"
  ],
  "es_salto": true
 },
 "nodo_actual": "gestion_contrasenas_cui",
 "razonamiento": "El usuario reafirma su prioridad con una evidencia concreta nueva: no tiene copias de seguridad. Eso es protección de medios (dispositivo único, sin respaldo) más que gestión de contraseñas. Salto a Media Protection porque aborda directamente el riesgo de pérdida total de datos. La pregunta reconoce la prioridad (conteo=3) sin deflexionar y avanza sobre ella.",
 "saltos_posibles": [
  {
   "id": "getting_started_media_protection",
   "titulo": "Protección de Medios (Media Protection)",
   "afinidad": 0.474,
   "fase_proyecto": "ejecucion",
   "condiciones_activacion": [
    "Cuando operas o vendes en Estados Unidos como contratista del gobierno federal y manejas dispositivos de almacenamiento removibles o documentos físicos con CUI."
   ]
  },
  {
   "id": "getting_started_personnel_security",
   "titulo": "Seguridad del Personal",
   "afinidad": 0.448,
   "fase_proyecto": "ejecucion",
   "condiciones_activacion": [
    "Cuando operas o vendes en Estados Unidos como contratista del gobierno federal y contratas, despides o transfieres empleados con acceso a sistemas que procesan CUI."
   ]
  },
  {
   "id": "regla_disponibilidad_previa_venta",
   "titulo": "Disponibilidad de la Garantia Antes de la Venta (Pre-Sale Availability Rule)",
   "afinidad": 0.398,
   "fase_proyecto": "ejecucion",
   "condiciones_activacion": [
    "Si vendes, o piensas vender, productos a clientes en Estados Unidos.",
    "Cuando ofreces una garantia escrita sobre lo que vendes, sin importar el canal."
   ]
  },
  {
   "id": "indice_de_reparabilidad",
   "titulo": "Diseñar un puntaje de qué tan fácil es arreglar tu producto (índice de reparabilidad)",
   "afinidad": 0.398,
   "fase_proyecto": "planificacion",
   "condiciones_activacion": [
    "Si vendes en Francia productos electrónicos, donde desde 2021 debes puntuar su reparabilidad, o si tu producto es físico y dura mucho tiempo, como electrodomésticos, dispositivos o muebles.",
    "Si tu producto se puede romper o está pensado para volverse obsoleto."
   ]
  },
  {
   "id": "desconexion_ventas_experiencia",
   "titulo": "La desconexion entre vender y cumplir lo prometido después",
   "afinidad": 0.393,
   "fase_proyecto": "ejecucion",
   "condiciones_activacion": [
    "Cuando recibes quejas frecuentes de clientes nuevos porque no se cumplio lo que se les prometio",
    "Si quien vende y quien atiende o entrega funcionan como mundos separados"
   ]
  },
  {
   "id": "investigar_datos_cliente",
   "titulo": "Investigar a tu cliente: reúne sus datos de forma ordenada",
   "afinidad": 0.393,
   "fase_proyecto": "ejecucion",
   "condiciones_activacion": [
    "Ya tienes clientes activos pero te falta conocerlos a fondo",
    "Quieres mejorar la retención construyendo relaciones más personales"
   ]
  },
  {
   "id": "identify_mapeo_datos",
   "titulo": "Mapea tus datos y evalúa el riesgo de privacidad (Identify)",
   "afinidad": 0.393,
   "fase_proyecto": "planificacion",
   "condiciones_activacion": [
    "Cuando empiezas a construir tu manejo de privacidad desde cero",
    "Si no tienes claro qué datos personales manejas en tu negocio"
   ]
  },
  {
   "id": "getting_started_system_communication_protection",
   "titulo": "Protección de Comunicaciones y Límites del Sistema",
   "afinidad": 0.392,
   "fase_proyecto": "ejecucion",
   "condiciones_activacion": [
    "Cuando operas o vendes en Estados Unidos como contratista del gobierno federal y tus comunicaciones de red transmiten CUI."
   ]
  }
 ],
 "respuesta_usuario": "No tengo copias de seguridad; si pierdo el celular pierdo los pedidos y los contactos.",
 "candidatos_locales": [
  "respuesta_incidentes_cui",
  "mantenimiento_sistema_cui"
 ],
 "prioridad_declarada": {
  "texto": "ordenar contraseñas y quién puede entrar a las cuentas, proteger datos de clientes",
  "conteo": 3
 }
}
```
```json
{
 "a": "Sin copias de seguridad, perder el celular significa perder todo: pedidos, contactos, datos de tus 15 clientes. Ese riesgo es real y urgente. Lo que propongo es resolver esto en paralelo a ordenar las contraseñas: primero, ¿dónde guardas ahora mismo esos datos del celular, solo en el teléfono, o hay algo en la nube, aunque sea accidental?",
 "de": "Sin copias de seguridad, perder el celular significa perder todo: pedidos, contactos, datos de tus 15 clientes. Ese riesgo es real y urgente. Lo que propongo es resolver esto en paralelo a ordenar las contraseñas: primero, ¿dónde guardas ahora mismo esos datos del celular, solo en el teléfono, o hay algo en la nube, aunque sea accidental?",
 "tipo": "anclaje_proteccion",
 "motivo": "la reformulación no tenía forma de pregunta"
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
 "nodo_actual": "getting_started_media_protection",
 "razonamiento": "La respuesta introduce una nueva dimensión (robo de cuenta de Instagram) pero sigue siendo parte del mismo frente: protección de acceso. Repreguntar para saber si hay respaldo de contactos fuera de Instagram, porque eso discrimina entre dos caminos: (1) solo ordenar contraseña y MFA de Instagram, o (2) primero exportar/respaldar la lista de clientes como acción inmediata antes de cambiar contraseña. Sin saber si existe ese respaldo, no puedo elegir camino.",
 "saltos_posibles": [
  {
   "id": "monitoreo_continuo",
   "titulo": "Vigilancia Continua de tu Seguridad y Privacidad (postura de seguridad)",
   "afinidad": 0.386,
   "fase_proyecto": "ejecucion",
   "condiciones_activacion": [
    "Una vez que autorizaste tu sistema, para mantener su nivel de riesgo aceptable con el paso del tiempo.",
    "Cuando ocurren cambios importantes en tu sistema, en las personas involucradas o en el entorno donde operas."
   ]
  },
  {
   "id": "enfoque_en_superfans",
   "titulo": "Enfócate en tu uno por ciento (los superfans)",
   "afinidad": 0.379,
   "fase_proyecto": "ejecucion",
   "condiciones_activacion": [
    "Cuando ya tienes una base de clientes y quieres que hablen más de ti",
    "Si tu presupuesto de marketing es limitado y necesitas decidir dónde poner primero tu esfuerzo"
   ]
  },
  {
   "id": "evaluacion_preparacion_tecnologica",
   "titulo": "Revisa si tu tecnología está lista para vender en línea (evaluación IT)",
   "afinidad": 0.361,
   "fase_proyecto": "planificacion",
   "condiciones_activacion": [
    "Si no cuentas con la infraestructura tecnológica adecuada para vender en línea"
   ]
  },
  {
   "id": "creacion_contenido_compartible",
   "titulo": "Creación de Contenido Compartible para Amplificar con Publicidad Pagada",
   "afinidad": 0.361,
   "fase_proyecto": "ejecucion",
   "condiciones_activacion": [
    "Cuando se cuenta con contenido de marca y se busca maximizar su alcance con bajo presupuesto"
   ]
  },
  {
   "id": "gestion_riesgo_seguridad_ia",
   "titulo": "Gestión de Riesgos de Seguridad en IA (Prompt Injection y Jailbreaking)",
   "afinidad": 0.353,
   "fase_proyecto": "planificacion",
   "condiciones_activacion": [
    "Cuando el producto integra IA con capacidad de leer contenido externo o ejecutar acciones automáticas",
    "Antes del lanzamiento público de una funcionalidad basada en IA generativa"
   ]
  },
  {
   "id": "email_marketing_para_captacion",
   "titulo": "Email Marketing para Captación de Clientes",
   "afinidad": 0.35,
   "fase_proyecto": "ejecucion",
   "condiciones_activacion": [
    "Si necesitas acompañar a alguien antes de que te compre",
    "Si ya te llega gente por otros canales (buscadores, tu blog) y quieres convertirla en contactos tuyos"
   ]
  },
  {
   "id": "publicidad_no_convencional_stunts",
   "titulo": "Acciones de impacto para llamar la atención (publicity stunts)",
   "afinidad": 0.343,
   "fase_proyecto": "ejecucion",
   "condiciones_activacion": [
    "Cuando tienes poco presupuesto de marketing pero buscas visibilidad rápida",
    "Cuando necesitas diferenciarte de competidores con presupuestos publicitarios mucho más grandes"
   ]
  },
  {
   "id": "diferencia_ganancia_flujo_caja",
   "titulo": "Ganar dinero no es lo mismo que tener dinero: por qué un negocio rentable se puede quedar sin efectivo",
   "afinidad": 0.34,
   "fase_proyecto": "ejecucion",
   "condiciones_activacion": [
    "Si tu negocio está creciendo rápido en ventas pero no has revisado tu flujo de caja",
    "Si tu negocio muestra ganancias en los reportes pero te cuesta pagar tus facturas"
   ]
  }
 ],
 "respuesta_usuario": "Me preocupa que me roben la cuenta de Instagram porque es mi canal principal de ventas.",
 "candidatos_locales": [
  "getting_started_personnel_security"
 ],
 "prioridad_declarada": {
  "texto": "ordenar contraseñas y quién puede entrar a las cuentas, proteger datos de clientes, especialmente Instagram",
  "conteo": 4
 }
}
```
```json
{
 "a": "Si mañana perdieras acceso a tu cuenta de Instagram y con ella todo el historial que necesitas revisar en la actividad #6 para clasificar las 15 ventas por canal de origen, ¿tienes esos datos de esos clientes guardados en otro lugar (correo, papel, nube), o en este momento solo existen dentro de los mensajes de Instagram?",
 "de": "Instagram es tu 100% de ventas ahora mismo. Si te roban esa cuenta, pierdes acceso a tus clientes y al historial de pedidos al mismo tiempo. ¿ya tienes una lista de esos 15 clientes en otro lugar (correo, papel, nube), o están solo en los mensajes de Instagram?",
 "tipo": "anclaje_proteccion"
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
 "nodo_actual": "getting_started_media_protection",
 "razonamiento": "El usuario declara 'con eso me basta por ahora', señal clara de que quiere su plan. Aunque la respuesta anterior no fue explícita sobre dónde están los datos de clientes, el usuario ha indicado suficientemente su intención de terminar la sesión de preguntas y generar el plan con lo acumulado.",
 "saltos_posibles": [
  {
   "id": "reset_total_de_expectativas",
   "titulo": "Si vas a comer mierda, no la mordisquees (Reset Total de Expectativas)",
   "afinidad": 0.316,
   "fase_proyecto": "ejecucion",
   "condiciones_activacion": [
    "Cuando tienes que revisar a la baja tus proyecciones ante quienes invirtieron en ti o ante el mercado",
    "Cuando hay riesgo de que tengas que hacer varios ajustes negativos seguidos"
   ]
  },
  {
   "id": "gates_tempranos_flexibles",
   "titulo": "No exijas números exactos demasiado pronto",
   "afinidad": 0.308,
   "fase_proyecto": "ideacion",
   "condiciones_activacion": [
    "Cuando estás evaluando una idea nueva o arriesgada en sus primeras etapas y todavía no tienes datos firmes"
   ]
  },
  {
   "id": "principio_enough_is_enough",
   "titulo": "Principio 'Enough is Enough' en Fidelidad de Prototipos",
   "afinidad": 0.302,
   "fase_proyecto": "validacion",
   "condiciones_activacion": [
    "Cuando el equipo tiende a sobre-invertir tiempo y recursos en prototipos tempranos",
    "Cuando se necesita decidir el nivel de detalle adecuado para una etapa del proyecto"
   ]
  }
 ],
 "respuesta_usuario": "Con eso me basta por ahora.",
 "candidatos_locales": [
  "getting_started_personnel_security"
 ],
 "prioridad_declarada": {
  "texto": "ordenar contraseñas y quién puede entrar a las cuentas, proteger datos de clientes, especialmente Instagram",
  "conteo": 4
 }
}
```
```json
{
 "ruta": 3,
 "tipo": "cobertura_conceptos",
 "total": 11,
 "cosecha": 8
}
```
```json
{
 "tipo": "estimacion_banda",
 "total": 22,
 "con_banda": 22
}
```
```json
{
 "tipo": "enlace_proteccion",
 "mundo": "seguridad_digital",
 "total": 22,
 "costo_usd": 0.0341,
 "enlazados": 0,
 "descartados": 0
}
```

## Juez de sesion (calidad)

```json
{
 "comentario": "La sesión repregunta dos veces sobre el mismo nodo (Gestión Segura de Contraseñas) sin avanzar; el salto a Protección de Medios es pertinente pero luego vuelve al mismo nodo, y los saltos_posibles ofrecidos en los últimos dos turnos tienen afinidades muy bajas (0.316-0.386) y contenidos desconectados (Email Marketing, publicity stunts, flujo de efectivo), señal de que el grafo carece de cobertura clara para el caso concreto del usuario: gestión de acceso a cuentas críticas para negocios (Instagram, banco) con MFA.",
 "repeticion_detectada": true,
 "pertinencia_transiciones": 2,
 "señales_fuera_de_material": [
  "uso la misma contraseña para el correo, Instagram y el banco",
  "no tengo verificación en dos pasos",
  "Instagram porque es mi canal principal de ventas"
 ]
}
```
