# Sesion 8: primer_equipo / inicial

- id: efa3658e-be7a-4c37-ab51-94f6a305ecbd
- creada: 2026-09-27T21:27:24.411153+00:00
- cerrada: 2026-09-27T21:29:31.332+00:00
- puerta de entrada: Define la Tarjeta de Puntuación (`crear_tarjeta_puntuacion_puesto`)
- coste USD: 0.1828
- desglose: {"plan": 0.0962733, "turnos": 0.038459099999999996, "estado_vivo": 0.004606000000000001, "juez_sesion": 0.003981, "estimacion_banda": 0.039525000000000005}
- fase final del recorrido: cerrada
- prioridad declarada: {"texto": "Quiere aprender a dar opinión clara y a repartir el trabajo para dejar de apagar incendios", "conteo": 2}

## Mensaje de entrada

Exploración del mundo "Primer Equipo" (Contrata bien, dirige mejor y haz crecer a tu gente.) para mi idea. Contexto actual: El negocio mantiene viabilidad financiera con margen de $120 por unidad confirmado, pero la diferenciación sigue sin resolver: no está claro si competirá como maceta básica sensible al precio o si logrará posicionamiento con valor percibido superior. La feria de agosto permanece como escenario de validación mediante conversación directa con clientes.

El problema técnico de burbujas y acabados irregulares persiste porque falta documentación sistemática del proceso de producción que correlacione defectos con variables de temperatura, mezcla y descanso del material. El fundador orientó correctamente hacia detección preventiva antes del horneado, pero esto requiere primero registrar lo que sucede actualmente paso a paso.

La sesión identificó tres puntos críticos de fallo sin respaldo que ahora dominan la prioridad operativa inmediata. Primero, la seguridad de datos: utiliza contraseña única para correo, Instagram y banco sin autenticación multifactor, datos de clientes en Excel sin protección dentro de un celular sin copias de seguridad, lo que genera exposición financiera y reputacional. Segundo, la dependencia de un único proveedor de resina sin alternativas conocidas ni colchón financiero, que paraliza producción si hay desabasto o alza de precio. Tercero, la concentración total de ventas y acceso a clientes en Instagram, donde perder la cuenta significa perder el historial de pedidos y contactos sin otra forma de recuperarlos.

El negocio gestiona crisis de forma reactiva sin registro documentado de riesgos. Transitó de la reacción a la anticipación identificando estos tres riesgos nucleares y reconociendo que el fundador es punto único de falla operativo. Necesita urgentemente redundancia en proveedores, respaldos de datos en almacenamiento seguro externo, protección de credenciales con multifactor, y un flujo de clientes que no dependa únicamente de Instagram. La capacidad de respuesta actual es frágil y cualquier shock operativo colapsa el negocio inmediatamente.

## Recorrido (etiqueta del riel, id, modo)

1. Define la Tarjeta de Puntuación (`crear_tarjeta_puntuacion_puesto`, conversado)
2. Equilibra Microgestión y Ausencia (`equilibrar_microdireccion_ausencia`, salto)
3. Entrega tus Problemas Difíciles (`entregar_problema_dificil_reporte`, conversado)
4. Sigue los Cuatro Pasos al Contratar (`aplicar_metodo_ghsmart_contratacion`, conversado)
5. Haz tu Opinión Accionable (`hacer_opinion_accionable`, salto)
6. Escucha el Primer Aviso de Renuncia (`responder_primer_aviso_renuncia_subordinado`, conversado)

## Ultimas preguntas

- Cuando piensas en la próxima persona que necesitas traer a tu equipo, ¿qué es lo que más te preocupa en este momento: tener claro exactamente qué resultados esperas que logre, encontrar a los candidatos adecuados, elegir bien entre quienes ya tienes identificados, o hacer que la persona que escojas realmente quiera venir a trabajar contigo?
- Cuando les dices a tus dos empleados que algo salió mal, ¿qué información les das: solo el error que viste, o también qué esperabas que hicieran distinto y por qué te importa?
- Cuando alguien valioso en tu proyecto te dice que se quiere ir, y tu escuchas de verdad hasta encontrar la razón real detrás de esa decisión, ¿qué tan lejos estás dispuesto a llegar para retenerlo: hablarías con tu propio jefe, buscarías cambiarle el rol, conseguirías presupuesto para mejorar su situación, o ya sabes que hay cosas en tu alcance que podrías mover?

## Decisiones por turno (caja de vidrio)

```json
{
 "tipo": "decision_turno",
 "decision": {
  "accion": "avanzar",
  "camino": [
   "equilibrar_microdireccion_ausencia"
  ],
  "es_salto": true
 },
 "nodo_actual": "crear_tarjeta_puntuacion_puesto",
 "razonamiento": "Respuesta revela un problema concreto nuevo (no sabe dirigir a los empleados) distinto del tema de 'crear tarjeta de puntuacion'. Saltos_posibles incluye nodos dedicados a direccion y delegacion con afinidad 0.58+. 'Equilibrar microdireccion y ausencia' es el mas especifico al dilema declarado: se mete o confía, pero termina meterse. Este tema merece nodo dedicado, no pregunta local improvisada.",
 "saltos_posibles": [
  {
   "id": "reemplazarse_trabajo_propio",
   "titulo": "Buscar constantemente quién te reemplace en lo que haces hoy",
   "afinidad": 0.608,
   "fase_proyecto": "ejecucion",
   "condiciones_activacion": [
    "De forma continua, y con más motivo cuando te notes apegado a una tarea porque te da sensación de pericia, de control o de identidad."
   ]
  },
  {
   "id": "entregar_problema_dificil_reporte",
   "titulo": "Entregar un problema difícil a alguien de tu equipo y declararlo dueño en público",
   "afinidad": 0.602,
   "fase_proyecto": "ejecucion",
   "condiciones_activacion": [
    "Cuando aparece un problema difícil y tu primer impulso es cargar con él para ahorrárselo a tu equipo."
   ]
  },
  {
   "id": "admitir_pronto_mal_desempenio_cuatro_razones",
   "titulo": "Admitir pronto que alguien de tu equipo empieza a rendir por debajo, con cuatro razones para no esperar",
   "afinidad": 0.596,
   "fase_proyecto": "ejecucion",
   "condiciones_activacion": [
    "Cuando alguien de tu equipo empieza a rendir por debajo y todavía no lo has admitido, ni ante ti mismo ni ante tu jefe ni ante recursos humanos."
   ]
  },
  {
   "id": "decidir_directivo_no_encaja_papel",
   "titulo": "Decidir qué hacer cuando un directivo de tu equipo no da la talla del papel",
   "afinidad": 0.591,
   "fase_proyecto": "ejecucion",
   "condiciones_activacion": [
    "Cuando uno de los directivos de tu equipo no está cumpliendo las expectativas de su papel, y tu primer impulso es apoyarle y ayudarle a superarlo."
   ]
  },
  {
   "id": "mover_rapido_persona_papel_equivocado",
   "titulo": "Mover rápido a quien no está preparado para tener éxito en su papel",
   "afinidad": 0.586,
   "fase_proyecto": "ejecucion",
   "condiciones_activacion": [
    "Cuando alguien de tu equipo lleva tiempo sin hacer trabajo de calidad, sin ser productivo o bajando la moral, y llevas meses volcando esfuerzo en arreglarlo sin que cambie nada."
   ]
  },
  {
   "id": "equilibrar_microdireccion_ausencia",
   "titulo": "Equilibrar la microdirección y la ausencia al delegar",
   "afinidad": 0.586,
   "fase_proyecto": "ejecucion",
   "condiciones_activacion": [
    "Siempre que tengas que decidir si te metes tú o das un paso atrás y confías en otro."
   ]
  },
  {
   "id": "ceder_autoridad_unilateral_equipo",
   "titulo": "Soltar la autoridad unilateral sobre tu equipo para que se sientan libres en el trabajo, sin caer en la abdicación",
   "afinidad": 0.583,
   "fase_proyecto": "ejecucion",
   "condiciones_activacion": [
    "Cuando quieres que la gente a tu cargo se sienta libre en el trabajo y eres tú quien tiene sobre ellos las palancas tradicionales de control de un jefe."
   ]
  },
  {
   "id": "planificar_reduccion_trabajo_individual",
   "titulo": "Planificar la reducción de tu trabajo individual cuando el equipo crece",
   "afinidad": 0.578,
   "fase_proyecto": "planificacion",
   "condiciones_activacion": [
    "Cuando eres directivo nuevo, ya sea porque te tocó dirigir dentro de un equipo que crece o porque fuiste el primero en un trabajo que ahora se vuelve de equipo, y sigues llevando responsabilidades de trabajo individual además de las de gestión. El momento de actuar es cuando tu equipo llega a cuatro o cinco personas."
   ]
  }
 ],
 "respuesta_usuario": "Acabo de contratar a mis dos primeros empleados para el taller y no se dirigirlos: termino haciendo yo el trabajo porque me cuesta delegar y decirles cuando algo sale mal.",
 "candidatos_locales": [
  "alinear_comunicar_tarjeta_puntuacion",
  "definir_resultados_tarjeta_puntuacion",
  "identificar_competencias_tarjeta_puntuacion",
  "redactar_mision_tarjeta_puntuacion",
  "respetar_cautelas_legales_contratacion"
 ],
 "prioridad_declarada": {
  "texto": "No sabe cómo dirigir a los dos empleados recién contratados: le cuesta delegar y dar retroalimentación sobre trabajo deficiente",
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
   "entregar_problema_dificil_reporte"
  ],
  "es_salto": false
 },
 "nodo_actual": "equilibrar_microdireccion_ausencia",
 "razonamiento": "La respuesta revela el patrón raiz: no hay diálogo estructurado con los empleados, solo reacción a crisis. El nodo local (entregar_problema_dificil_reporte) atiende exactamente esto: cómo traspasar propiedad del problema. No es necesario saltar a reuniones 1:1 todavía; primero hay que entender su impulso de control (¿miedo al colapso o a la incompetencia de ellos?) para diseñar cómo delegar de verdad.",
 "saltos_posibles": [
  {
   "id": "montar_reuniones_solas_mentalidad_frecuencia",
   "titulo": "Montar tus reuniones a solas con cada persona a tu cargo: la mentalidad, la frecuencia, presentarte siempre y la agenda puesta por esa persona",
   "afinidad": 0.487,
   "fase_proyecto": "planificacion",
   "condiciones_activacion": [
    "Cuando vas a montar o a arreglar las reuniones a solas con las personas a tu cargo, y quieres que sean lo que pueden ser: tu mejor oportunidad de escuchar de verdad."
   ]
  },
  {
   "id": "leer_seniales_fallo_jefe_reunion_solas",
   "titulo": "Leer en tus reuniones a solas las cinco señales de que estás fallando como jefe",
   "afinidad": 0.457,
   "fase_proyecto": "validacion",
   "condiciones_activacion": [
    "Cuando quieres las señales tempranas de que estás fallando como jefe, y las buscas donde aparecen primero: en tus propias reuniones a solas."
   ]
  },
  {
   "id": "reuniones_uno_a_uno",
   "titulo": "Las reuniones uno a uno (1:1)",
   "afinidad": 0.456,
   "fase_proyecto": "ejecucion",
   "condiciones_activacion": [
    "Cuando tu equipo crece y la comunicación informal deja de ser suficiente"
   ]
  },
  {
   "id": "escribir_apuntes_sala_estudio_equipo",
   "titulo": "Escribir y leer los apuntes de la semana dentro de la propia reunión, como sala de estudio, en vez de contarlos en voz alta o dejarlos a que cada cual los ponga por su cuenta",
   "afinidad": 0.453,
   "fase_proyecto": "ejecucion",
   "condiciones_activacion": [
    "Cuando quieres que todo el mundo sepa en qué anda todo el mundo para poder señalar solapes y motivos de preocupación, y ni te vale una reunión de horas ni te funciona que cada cual escriba sus apuntes por su cuenta."
   ]
  },
  {
   "id": "auditar_formacion_premios_ultima_fila",
   "titulo": "Auditar la reunión general y su entrega de premios desde la última fila, donde está la mayor parte de la gente",
   "afinidad": 0.441,
   "fase_proyecto": "validacion",
   "condiciones_activacion": [
    "Cuando tu organización ya tiene una reunión general periódica con anuncios o entrega de premios y quieres saber qué llega de ella a la gente que está al fondo."
   ]
  },
  {
   "id": "cubrir_indicadores_problemas_reunion_individual",
   "titulo": "Cubrir en la reunión individual los indicadores del subordinado, lo ocurrido desde la anterior y el problema potencial, con el criterio de que sean los asuntos que le preocupan",
   "afinidad": 0.439,
   "fase_proyecto": "ejecucion",
   "condiciones_activacion": [
    "Cuando estás dentro de la reunión individual, o preparando su guion, y hay que decidir qué asuntos se tratan en ella."
   ]
  },
  {
   "id": "avisar_organizador_reunion_prescindible",
   "titulo": "Avisar a quien organiza cuando una reunión periódica no parece valer para nadie",
   "afinidad": 0.435,
   "fase_proyecto": "ejecucion",
   "condiciones_activacion": [
    "Cuando te encuentras en una reunión periódica de valor cuestionable, que no parece valiosa para nadie y no solo para ti."
   ]
  },
  {
   "id": "recoger_opinion_360_grados",
   "titulo": "Recoger opinión de trescientos sesenta grados para la máxima objetividad",
   "afinidad": 0.434,
   "fase_proyecto": "ejecucion",
   "condiciones_activacion": [
    "Cuando te falta contexto profundo del día a día de la persona a tu cargo, cuando toca su revisión anual de desempeño, o cuando sospechas que tu mensaje no está calando y necesitas que le llegue desde varias voces."
   ]
  }
 ],
 "respuesta_usuario": "Nunca he tenido reuniones a solas con ellos; les hablo solo cuando hay un problema y a las carreras.",
 "candidatos_locales": [
  "entregar_problema_dificil_reporte"
 ],
 "prioridad_declarada": {
  "texto": "No sabe cómo dirigir a los dos empleados recién contratados: le cuesta delegar y dar retroalimentación sobre trabajo deficiente",
  "conteo": 1
 }
}
```
```json
{
 "tipo": "puerta_reelegida",
 "motivo": "el nodo no tiene sucesores en este mundo",
 "dominio": "primer_equipo",
 "es_semilla": true,
 "puerta_nueva": "aplicar_metodo_ghsmart_contratacion",
 "puerta_descartada": "entregar_problema_dificil_reporte",
 "candidatas_restantes": 18
}
```
```json
{
 "tipo": "decision_turno",
 "decision": {
  "accion": "avanzar",
  "camino": [
   "hacer_opinion_accionable"
  ],
  "es_salto": true
 },
 "nodo_actual": "aplicar_metodo_ghsmart_contratacion",
 "razonamiento": "Respuesta nueva declara prioridad distinta y más específica: no es solo delegación, sino capacidad de comunicar opinión de forma que otros puedan actuar sin depender de él. Saltos_posibles incluye 'Hacer que tu opinión se pueda convertir en acción' (afinidad 0.58) que es exactamente esto. Este nodo es más dedicado y especializado que cualquier sucesor local de 'aplicar_metodo_ghsmart', que trata contratación, no comunicación de retroalimentación. Salta ahí.",
 "saltos_posibles": [
  {
   "id": "repartir_decision_cercanos_hechos",
   "titulo": "Repartir las decisiones entre los más cercanos a los hechos en vez de tomarlas tú por ser el jefe",
   "afinidad": 0.594,
   "fase_proyecto": "ejecucion",
   "condiciones_activacion": [
    "Cuando en tu equipo las decisiones las estás tomando tú, o las toma el más veterano de la sala, y no quien tiene delante los hechos."
   ]
  },
  {
   "id": "hacer_opinion_accionable",
   "titulo": "Hacer que tu opinión se pueda convertir en acción, con tres consejos",
   "afinidad": 0.58,
   "fase_proyecto": "ejecucion",
   "condiciones_activacion": [
    "Cuando alguien ha oído tu opinión y aun así no cambia nada, porque no ve el problema que le describes o no sabe qué hacer con lo que le has dicho."
   ]
  },
  {
   "id": "debatir_decidir_asuntos_cultura_evitar_delegar",
   "titulo": "Debatir y decidir tú los asuntos de cultura que te tienta delegar en recursos humanos, para que no los decidan sin tu influencia humanizadora ni se queden sin decidir",
   "afinidad": 0.568,
   "fase_proyecto": "ejecucion",
   "condiciones_activacion": [
    "Cuando tienes delante uno de esos asuntos de cultura en los que preferirías no gastar neuronas y te tienta pasárselo a recursos humanos o simplemente dejarlo pasar."
   ]
  },
  {
   "id": "declarar_intencion_reemplazar_peticion_permiso",
   "titulo": "Reemplazar las frases que piden permiso por frases que declaran intención, y responder con una aprobación simple",
   "afinidad": 0.566,
   "fase_proyecto": "ejecucion",
   "condiciones_activacion": [
    "Cuando vas a proponer una acción a quien tiene la autoridad de aprobarla, en vez de pedirle permiso o pedirle que decida por ti."
   ]
  },
  {
   "id": "transmitir_objetivos_prioridades_preferencias",
   "titulo": "Transmitir objetivos, prioridades y preferencias, y no solo hechos, para que el subordinado pueda decidir solo",
   "afinidad": 0.563,
   "fase_proyecto": "ejecucion",
   "condiciones_activacion": [
    "Cuando tus subordinados te traen a ti decisiones que podrían tomar ellos, o toman solos decisiones que a ti no te valen, y al mirar qué les has dado ves que les has dado hechos y nada más."
   ]
  },
  {
   "id": "definir_quien_responde_cada_cosa",
   "titulo": "Definir quién responde de cada cosa antes de que la conversación termine",
   "afinidad": 0.56,
   "fase_proyecto": "ejecucion",
   "condiciones_activacion": [
    "Al final de cualquier conversación de la que tenga que salir trabajo, y también cada vez que escribes a más de una persona sobre un asunto que pide seguimiento."
   ]
  },
  {
   "id": "empujar_persona_reunion_direccion_preferida",
   "titulo": "Empujar a una persona o a una reunión hacia la dirección que prefieres, sabiendo que un empujón no es una orden",
   "afinidad": 0.555,
   "fase_proyecto": "ejecucion",
   "condiciones_activacion": [
    "Cuando quieres que un asunto vaya en una dirección sin dar una instrucción ni una orden, y limitarte a transmitir información se queda corto."
   ]
  },
  {
   "id": "ser_honesto_transparente_desempenio",
   "titulo": "Ser honesto y transparente sobre el desempeño de la persona a tu cargo",
   "afinidad": 0.552,
   "fase_proyecto": "ejecucion",
   "condiciones_activacion": [
    "Siempre que tengas a alguien a tu cargo, y con más urgencia cuando notes que a menudo se está preguntando qué piensas de ella."
   ]
  }
 ],
 "respuesta_usuario": "Quiero aprender a dar opinion clara y a repartir el trabajo para dejar de apagar incendios.",
 "candidatos_locales": [
  "abastecer_flujo_candidatos",
  "seleccionar_jugador_cuatro_entrevistas",
  "vender_puesto_jugador",
  "instalar_metodo_contratacion_empresa"
 ],
 "prioridad_declarada": {
  "texto": "Quiere aprender a dar opinión clara y a repartir el trabajo para dejar de apagar incendios",
  "conteo": 2
 }
}
```
```json
{
 "tipo": "puerta_reelegida",
 "motivo": "el nodo no tiene sucesores en este mundo",
 "dominio": "primer_equipo",
 "es_semilla": true,
 "puerta_nueva": "responder_primer_aviso_renuncia_subordinado",
 "puerta_descartada": "hacer_opinion_accionable",
 "candidatas_restantes": 17
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
 "nodo_actual": "responder_primer_aviso_renuncia_subordinado",
 "razonamiento": "Usuario declara explícitamente que tiene suficiente con lo tratado hasta ahora ('Con eso me basta por ahora'). Aunque no use comando literal 'dame mi plan', la intención es clara: quiere pasar a generación del plan de acción. Acción correcta es generar_plan.",
 "saltos_posibles": [
  {
   "id": "decir_no_trabajo_excede_capacidad",
   "titulo": "Decir que no de salida al trabajo que excede tu capacidad, antes y no después, usando tu propia idea del tiempo que cada cosa te lleva",
   "afinidad": 0.343,
   "fase_proyecto": "ejecucion",
   "condiciones_activacion": [
    "Cuando te llega trabajo por encima de lo que puedes atender y lo aceptas porque no sabes medir tu propia capacidad."
   ]
  },
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
   "id": "atender_modo_supervivencia_equipo",
   "titulo": "Atender el modo supervivencia antes de invertir en el largo plazo",
   "afinidad": 0.307,
   "fase_proyecto": "ejecucion",
   "condiciones_activacion": [
    "Cuando vas a invertir tiempo y energía en el propósito, las personas y el proceso de tu equipo, que es lo que da fruto a la larga, y antes tienes que saber si tu organización se puede permitir esperar a la larga."
   ]
  },
  {
   "id": "encargar_meta_especifica_dejar_libre_metodo",
   "titulo": "Encargar una meta específica sin decir cómo se cumple, y dejar los recursos como estaban",
   "afinidad": 0.305,
   "fase_proyecto": "ejecucion",
   "condiciones_activacion": [
    "Cuando le encargas a alguien que deje lista una organización o un equipo y tienes que decidir cuánto le dices sobre cómo hacerlo."
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
  "gestionar_retencion_subordinado_valioso_renuncia"
 ],
 "prioridad_declarada": {
  "texto": "Quiere aprender a dar opinión clara y a repartir el trabajo para dejar de apagar incendios",
  "conteo": 2
 }
}
```
```json
{
 "ruta": 6,
 "tipo": "cobertura_conceptos",
 "total": 23,
 "cosecha": 17
}
```
```json
{
 "tipo": "estimacion_banda",
 "total": 29,
 "con_banda": 29
}
```

## Juez de sesion (calidad)

```json
{
 "comentario": "El salto del turno 2 al 3 rompe la secuencia: se abandona 'Equilibrar microdirección y ausencia' sin explorar sus sucesores locales (reuniones 1:1, que el usuario necesitaba), saltando a contratación después de que el usuario ya había reconocido que el problema es la dirección cotidiana, no la selección de personal.",
 "repeticion_detectada": false,
 "pertinencia_transiciones": 3,
 "señales_fuera_de_material": [
  "termino haciendo yo el trabajo porque me cuesta delegar",
  "les hablo solo cuando hay un problema y a las carreras",
  "dejar de apagar incendios"
 ]
}
```
