# Sesion 3: quality / inicial

- id: 481f709c-c25a-451f-be18-1528dbd32ad4
- creada: 2026-09-27T21:19:05.122182+00:00
- cerrada: 2026-09-27T21:21:22.231+00:00
- puerta de entrada: Cumple los Catorce Pasos (`programa_mejora_calidad_14_pasos`)
- coste USD: 0.175
- desglose: {"plan": 0.0854373, "turnos": 0.04321595, "estado_vivo": 0.004346, "juez_sesion": 0.004062, "estimacion_banda": 0.03788999999999999}
- fase final del recorrido: cerrada
- prioridad declarada: {"texto": "resolver defectos de calidad (burbujas y acabados irregulares en resina)", "conteo": 2}

## Mensaje de entrada

Exploración del mundo "Calidad y Confianza" (Que tu cliente confíe, vuelva y te recomiende.) para mi idea. Contexto actual: El negocio alcanzó viabilidad financiera al recalcular costos incluyendo el valor real del trabajo del fundador ($50/hora) y subir precio a $250, logrando margen de $120 por unidad que cubre ampliamente los $200 mensuales en costos fijos. Las quince ventas en dos meses ya superan el punto de equilibrio. Sin embargo, la verdadera naturaleza del problema cambió: no es supervivencia sino comprensión del cliente y escala inteligente. Aunque las ventas persistieron tras el aumento de precio, falta validar si está vendiendo por precio bajo o por atributos específicos del producto que justifiquen margen mayor. El canal de Instagram funciona pero opera sin feedback directo sobre motivaciones de compra, lo cual limita toda decisión futura sobre posicionamiento o segmentación. La feria de agosto representa la primera oportunidad concreta para conversar con clientes reales mientras compran, observar qué atributos comunican valor y qué preguntas hacen. El trabajo inmediato debe girar en torno a tres frentes que se retroalimentan: identificar cuáles de sus quince clientes existentes son más valiosos y accesibles para entrevistas sobre qué les atrajo realmente, construir un embudo de ventas donde la conversación presencial reemplace la pasividad de Instagram, y usar la feria para probar si el posicionamiento actual funciona o requiere ajuste. La pregunta central ahora no es viabilidad sino direccionalidad: ¿está vendiendo macetas básicas a sensibles al precio bajo, o creando objetos con valor percibido diferenciado? Esa respuesta determinará si puede crecer con márgenes sostenibles o si debe replantear el segmento objetivo.

## Recorrido (etiqueta del riel, id, modo)

1. Cumple los Catorce Pasos (`programa_mejora_calidad_14_pasos`, conversado)
2. Establece Niveles de Acción Correctiva (`accion_correctiva_sistematica`, conversado)
3. Previene el Error en su Origen (`poka_yoke_a_prueba_de_errores`, salto)
4. Distingue Fallas Esporádicas y Crónicas (`accion_correctiva`, conversado)

## Ultimas preguntas

- Para atacar las burbujas y acabados irregulares, lo primero es saber exactamente cuándo y dónde ocurren: ¿podrías empezar a anotar en cada lote qué fecha hiciste, qué variables cambiaste (temperatura, tiempo de curado, técnica de vertido) y cuáles piezas salieron con defectos?
- Antes de hornear, ¿hay algo en tu proceso de mezcla o vertido donde podrías ver de inmediato si algo no está bien (por ejemplo, si la mezcla tiene aire atrapado, si la temperatura es muy baja, o si quedó demasiado espesa)?
- Cuando identificas que algo no está funcionando como debería en tu proyecto, ¿cómo te enteras normalmente y qué haces primero para entender qué pasó?

## Decisiones por turno (caja de vidrio)

```json
{
 "tipo": "decision_turno",
 "decision": {
  "accion": "repreguntar",
  "camino": [],
  "es_salto": false
 },
 "nodo_actual": "programa_mejora_calidad_14_pasos",
 "razonamiento": "La respuesta pivota desde 'qué te preocupa del programa de calidad' a un problema concreto y técnico de defectos de material/proceso. El nodo actual y sus sucesores locales tratan de programas formales de mejora continua, estructura organizacional y cultura de prevención (temas demasiado amplios para una persona sola). Antes de avanzar en esa cadena, necesito desambiguar si el problema es esporádico (requiere acción correctiva puntual) o crónico/sistemático (requiere rediseño del proceso). Esa distinción determinará cuál sucesor es relevante. Ninguno de los saltos_posibles atiende específicamente defectos de resina y acabados; 'pruebas_inadecuadas_prototipos' es genérico y trata validación de prototipo pre-producción, no defectos en producción actual. La decisión correcta es repreguntar en el contexto local.",
 "saltos_posibles": [
  {
   "id": "definiciones_operacionales",
   "titulo": "Definiciones Operacionales de Calidad Aceptable",
   "afinidad": 0.522,
   "fase_proyecto": "ejecucion",
   "condiciones_activacion": [
    "Cuando existe alta variabilidad en la aceptación de productos entre inspectores o turnos.",
    "Cuando el porcentaje de defectos es estable pero elevado y no se ha intentado clarificar criterios."
   ]
  },
  {
   "id": "identificacion_del_verdadero_cliente",
   "titulo": "Identificación del Verdadero Cliente (Quién Decide la Calidad)",
   "afinidad": 0.497,
   "fase_proyecto": "ideacion",
   "condiciones_activacion": [
    "Cuando existen intermediarios técnicos o comerciales entre el fabricante y el usuario final"
   ]
  },
  {
   "id": "eliminar_trabajo_a_destajo",
   "titulo": "Eliminación del Trabajo a Destajo (Piece Work)",
   "afinidad": 0.495,
   "fase_proyecto": "ejecucion",
   "condiciones_activacion": [
    "Cuando la organización utiliza pago por pieza como esquema de compensación principal",
    "Cuando los operadores reportan presión de producción que compromete la calidad"
   ]
  },
  {
   "id": "mejora_del_sistema_responsabilidad_gerencial",
   "titulo": "La Mejora del Sistema es Tu Responsabilidad",
   "afinidad": 0.493,
   "fase_proyecto": "ejecucion",
   "condiciones_activacion": [
    "Cuando un proceso esta en control estadistico pero la tasa de defectos sigue siendo inaceptable",
    "Cuando varias personas o maquinas presentan el mismo problema"
   ]
  },
  {
   "id": "pruebas_inadecuadas_prototipos",
   "titulo": "Pruebas inadecuadas de prototipos",
   "afinidad": 0.488,
   "fase_proyecto": "validacion",
   "condiciones_activacion": [
    "Antes de aprobar el paso de un prototipo a producción en volumen"
   ]
  },
  {
   "id": "quejas_llegan_tarde",
   "titulo": "Las Quejas Llegan Demasiado Tarde: Riesgo del Cliente Silencioso",
   "afinidad": 0.483,
   "fase_proyecto": "ejecucion",
   "condiciones_activacion": [
    "Cuando la empresa mide calidad solo por número de quejas recibidas",
    "Al analizar pérdida de clientes sin explicación aparente"
   ]
  },
  {
   "id": "rediseno_procesos_negocio_cx",
   "titulo": "Rediseño de Procesos de Negocio Centrado en el Cliente",
   "afinidad": 0.483,
   "fase_proyecto": "ejecucion",
   "condiciones_activacion": [
    "Cuando descubres que la causa del mal servicio está en cómo tú mismo organizaste tu negocio",
    "Cuando necesitas un cambio profundo en cómo trabajas, no solo un arreglo cosmético"
   ]
  },
  {
   "id": "limites_control_estadistico_vs_tolerancias",
   "titulo": "Cuando tu proceso se sale de control pero tu producto sigue cumpliendo (límites de control vs. tolerancias de calidad)",
   "afinidad": 0.479,
   "fase_proyecto": "ejecucion",
   "condiciones_activacion": [
    "Cuando ves puntos fuera de los límites de control pero tu producto sigue cumpliendo las especificaciones",
    "Si tú o quien trabaja contigo no tienen claro cuándo hay que actuar frente a una señal estadística"
   ]
  }
 ],
 "respuesta_usuario": "Mis clientes se quejan de piezas con burbujas y acabados irregulares entre lotes.",
 "candidatos_locales": [
  "cero_defectos",
  "consejo_de_calidad",
  "eliminacion_causas_error_4",
  "accion_correctiva_sistematica",
  "consejo_de_calidad_3",
  "accion_correctiva"
 ],
 "prioridad_declarada": {
  "texto": "resolver defectos de calidad (burbujas y acabados irregulares en resina)",
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
   "accion_correctiva_sistematica"
  ],
  "es_salto": false
 },
 "nodo_actual": "programa_mejora_calidad_14_pasos",
 "razonamiento": "El usuario revela que no tiene VISIBILIDAD sobre sus defectos (no registra qué falla ni cuándo), lo cual es el primer paso de cualquier acción correctiva sistemática. Aunque saltos_posibles incluye 'analisis_causa_raiz_defectos' (más específico al defecto en sí), ese nodo requiere que YA tengas claridad sobre el patrón, aquí el usuario ni siquiera registra. El sucesor 'accion_correctiva_sistematica' es el punto de entrada correcto: bifurca entre 'establecer estándar de trabajo' o 'auditar proveedores', pero el verdadero primer paso que el contexto revela que falta es la MEDICIÓN/REGISTRO del defecto. La pregunta_adaptada atiende eso sin desviar la prioridad (conteo=2): reconoce el problema como frente legítimo y propone el complemento inmediato (datos) que permite atacarlo.",
 "saltos_posibles": [
  {
   "id": "reporte_gerencial_diagnostico_calidad",
   "titulo": "Diagnostico de fallas en el sistema de calidad",
   "afinidad": 0.438,
   "fase_proyecto": "ejecucion",
   "condiciones_activacion": [
    "Cuando tu negocio tiene niveles constantes de defectos y tu única explicación es que falta maquinaria nueva",
    "Cuando tienes datos de auditoria de calidad que nunca has analizado para mejorar algo"
   ]
  },
  {
   "id": "analisis_causa_raiz_defectos",
   "titulo": "Análisis y Clasificación Precisa de Causas de Defectos",
   "afinidad": 0.431,
   "fase_proyecto": "ejecucion",
   "condiciones_activacion": [
    "Cuando existe una alta tasa de retrabajo o rechazo sin causa clara identificada",
    "Cuando diferentes departamentos se culpan mutuamente por los mismos defectos"
   ]
  },
  {
   "id": "aceptar_la_imperfeccion_del_diseno",
   "titulo": "Aceptar la Imperfección: Todo se Rompe",
   "afinidad": 0.408,
   "fase_proyecto": "planificacion",
   "condiciones_activacion": [
    "Cuando el equipo asume que su diseño es una solución perfecta y definitiva",
    "En etapas de planificación de productos con impacto social o ambiental a largo plazo"
   ]
  },
  {
   "id": "change_log",
   "titulo": "Registro de Cambios (Change Log)",
   "afinidad": 0.4,
   "fase_proyecto": "ejecucion",
   "condiciones_activacion": [
    "Si se necesita trazabilidad histórica de todos los cambios solicitados en el proyecto"
   ]
  },
  {
   "id": "carryover_fallas_producto",
   "titulo": "Eliminación del Carryover de Características Propensas a Fallas",
   "afinidad": 0.399,
   "fase_proyecto": "ejecucion",
   "condiciones_activacion": [
    "Cuando tu producto o servicio arrastra las mismas fallas de una versión a otra"
   ]
  },
  {
   "id": "regla_todo_o_nada_inspeccion_2",
   "titulo": "Regla de Inspección Todo-o-Nada (All-or-None Rules)",
   "afinidad": 0.396,
   "fase_proyecto": "ejecucion",
   "condiciones_activacion": [
    "Cuando tienes una regla fija para rechazar lotes que no está basada en costos reales",
    "Cuando necesitas tener claro, con números, si conviene pasar de revisar una muestra a inspeccionar todo o nada"
   ]
  },
  {
   "id": "probabilidad_falla_ensamblaje_multiple",
   "titulo": "Probabilidad de Falla en Ensamblajes con Múltiples Partes",
   "afinidad": 0.392,
   "fase_proyecto": "planificacion",
   "condiciones_activacion": [
    "Cuando el producto final está compuesto por múltiples partes o componentes ensamblados",
    "Cuando existe exposición repetida al mismo tipo de defecto (ej. múltiples soldaduras o uniones)"
   ]
  },
  {
   "id": "aceptacion_de_fallas_como_inevitables",
   "titulo": "Aceptar la falla como parte necesaria del sistema",
   "afinidad": 0.39,
   "fase_proyecto": "ejecucion",
   "condiciones_activacion": [
    "Cuando buscas eliminar el riesgo por completo sin pensar en el costo.",
    "Cuando hace mucho no ves fallas y sospechas que se están escondiendo."
   ]
  }
 ],
 "respuesta_usuario": "Reviso cada pieza al final, pero no tengo un registro de que falla ni cuando.",
 "candidatos_locales": [
  "cero_defectos",
  "consejo_de_calidad",
  "eliminacion_causas_error_4",
  "accion_correctiva_sistematica",
  "consejo_de_calidad_3",
  "accion_correctiva"
 ],
 "prioridad_declarada": {
  "texto": "resolver defectos de calidad (burbujas y acabados irregulares en resina)",
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
   "poka_yoke_a_prueba_de_errores"
  ],
  "es_salto": true
 },
 "nodo_actual": "accion_correctiva_sistematica",
 "razonamiento": "El usuario declara un tema concreto y nuevo que no trata ninguno de los sucesores locales de accion_correctiva_sistematica: detectar burbujas ANTES de hornear, es decir, prevención de errores en tiempo real, no registro post-defecto ni auditoría de proveedores. Entre saltos_posibles, 'poka_yoke_a_prueba_de_errores' (afinidad 0.496) es claramente el más específico: trata exactamente de 'defectos recurrentes causados por error humano' y 'cuando la inspección posterior no es suficiente' (aquí el usuario descubre defectos tras hornear, demasiado tarde). El nodo dedicado ofrece desarrollo teórico sobre dispositivos/sistemas a prueba de errores, no un arreglo local improvisado. Salto obligado.",
 "saltos_posibles": [
  {
   "id": "deteccion_defectos_raros_control_estadistico",
   "titulo": "Detección de Defectos Extremadamente Raros mediante Cartas de Control",
   "afinidad": 0.507,
   "fase_proyecto": "ejecucion",
   "condiciones_activacion": [
    "Cuando la fracción defectuosa de tu proceso es tan baja que inspeccionar el producto terminado resulta estadísticamente poco confiable.",
    "Cuando tienes requisitos extremos de confiabilidad (por ejemplo menos de 1 falla en 10^9 unidades)."
   ]
  },
  {
   "id": "reporte_gerencial_diagnostico_calidad",
   "titulo": "Diagnostico de fallas en el sistema de calidad",
   "afinidad": 0.504,
   "fase_proyecto": "ejecucion",
   "condiciones_activacion": [
    "Cuando tu negocio tiene niveles constantes de defectos y tu única explicación es que falta maquinaria nueva",
    "Cuando tienes datos de auditoria de calidad que nunca has analizado para mejorar algo"
   ]
  },
  {
   "id": "planificacion_de_la_inspeccion",
   "titulo": "Planificación de la Inspección",
   "afinidad": 0.5,
   "fase_proyecto": "planificacion",
   "condiciones_activacion": [
    "Cuando se diseña un nuevo proceso de manufactura",
    "Cuando se requiere formalizar los puntos de control de calidad en producción"
   ]
  },
  {
   "id": "poka_yoke_a_prueba_de_errores",
   "titulo": "Poka-Yoke (A Prueba de Errores)",
   "afinidad": 0.496,
   "fase_proyecto": "ejecucion",
   "condiciones_activacion": [
    "Cuando se detectan defectos recurrentes causados por error humano",
    "Cuando la inspección posterior no es suficiente para garantizar calidad"
   ]
  },
  {
   "id": "pruebas_destructivas",
   "titulo": "Manejo de Pruebas Destructivas mediante Control Estadístico",
   "afinidad": 0.491,
   "fase_proyecto": "planificacion",
   "condiciones_activacion": [
    "Cuando el atributo de calidad a probar destruye la muestra o unidad probada"
   ]
  },
  {
   "id": "accion_correctiva_2",
   "titulo": "Acción Correctiva (De la Detección a la Prevención)",
   "afinidad": 0.486,
   "fase_proyecto": "ejecucion",
   "condiciones_activacion": [
    "Cuando se detectan defectos o no conformidades recurrentes"
   ]
  },
  {
   "id": "validacion_sistema_medicion_2",
   "titulo": "Validación del Sistema de Medición (Bajo Six Sigma)",
   "afinidad": 0.484,
   "fase_proyecto": "ejecucion",
   "condiciones_activacion": [
    "Cuando se requieren tolerancias muy estrictas (Six Sigma)",
    "Cuando existen discrepancias entre clasificación de producto bueno/malo"
   ]
  },
  {
   "id": "analisis_causa_raiz_defectos",
   "titulo": "Análisis y Clasificación Precisa de Causas de Defectos",
   "afinidad": 0.482,
   "fase_proyecto": "ejecucion",
   "condiciones_activacion": [
    "Cuando existe una alta tasa de retrabajo o rechazo sin causa clara identificada",
    "Cuando diferentes departamentos se culpan mutuamente por los mismos defectos"
   ]
  }
 ],
 "respuesta_usuario": "Me interesa un proceso simple para detectar el defecto antes de hornear la pieza.",
 "candidatos_locales": [
  "planificacion_cero_defectos",
  "auditoria_calidad_proveedores",
  "cero_defectos",
  "consejo_de_calidad",
  "eliminacion_causas_error_4"
 ],
 "prioridad_declarada": {
  "texto": "resolver defectos de calidad (burbujas y acabados irregulares en resina)",
  "conteo": 2
 }
}
```
```json
{
 "tipo": "puerta_reelegida",
 "motivo": "el nodo no tiene sucesores en este mundo",
 "dominio": "quality",
 "es_semilla": true,
 "puerta_nueva": "accion_correctiva",
 "puerta_descartada": "poka_yoke_a_prueba_de_errores",
 "candidatas_restantes": 6
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
 "nodo_actual": "accion_correctiva",
 "razonamiento": "El usuario declara explícitamente 'con eso me basta por ahora', señal clara de que quiere su plan. Ha cubierto el ciclo necesario: viabilidad financiera confirmada ($120 de margen por unidad, 15 ventas superan punto de equilibrio), problema central identificado (defectos de calidad: burbujas y acabados irregulares entre lotes), y frentes de acción mapeados (detección temprana antes de hornear, poka-yoke, registro de variables). El usuario tiene suficiente para construir un plan operativo. Generar plan ahora.",
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
   "afinidad": 0.307,
   "fase_proyecto": "ideacion",
   "condiciones_activacion": [
    "Cuando estás evaluando una idea nueva o arriesgada en sus primeras etapas y todavía no tienes datos firmes"
   ]
  },
  {
   "id": "resolucion_problemas_niveles_supervision",
   "titulo": "Resolución de Problemas por Alcance (Regla 85-13-2)",
   "afinidad": 0.302,
   "fase_proyecto": "ejecucion",
   "condiciones_activacion": [
    "Cuando conviertes en un asunto grande algo que podrías resolver tú mismo en el momento",
    "Cuando no tienes claro qué problemas puedes resolver solo y cuáles necesitan ayuda externa"
   ]
  },
  {
   "id": "principio_enough_is_enough",
   "titulo": "Principio 'Enough is Enough' en Fidelidad de Prototipos",
   "afinidad": 0.301,
   "fase_proyecto": "validacion",
   "condiciones_activacion": [
    "Cuando el equipo tiende a sobre-invertir tiempo y recursos en prototipos tempranos",
    "Cuando se necesita decidir el nivel de detalle adecuado para una etapa del proyecto"
   ]
  }
 ],
 "respuesta_usuario": "Con eso me basta por ahora.",
 "candidatos_locales": [
  "comite_cero_defectos",
  "eliminacion_causas_error_4",
  "manejo_problemas",
  "planificacion_calidad_crosby",
  "sistema_informacion_calidad"
 ],
 "prioridad_declarada": {
  "texto": "resolver defectos de calidad (burbujas y acabados irregulares en resina)",
  "conteo": 2
 }
}
```
```json
{
 "ruta": 4,
 "tipo": "cobertura_conceptos",
 "total": 29,
 "cosecha": 25
}
```
```json
{
 "tipo": "estimacion_banda",
 "total": 27,
 "con_banda": 27
}
```

## Juez de sesion (calidad)

```json
{
 "comentario": "Sesión coherente con buen diagnóstico de defectos específicos de proceso (resina/moldeo); el salto a Poka-Yoke fue justificado pero los nodos visitados nunca profundizaron en causas raíz de burbujas (aire atrapado, temperatura, presión, material) ni en métodos de detección pre-hornear (inspección visual, técnicas no destructivas).",
 "repeticion_detectada": false,
 "pertinencia_transiciones": 4,
 "señales_fuera_de_material": [
  "burbujas y acabados irregulares entre lotes",
  "antes de hornear la pieza"
 ]
}
```
