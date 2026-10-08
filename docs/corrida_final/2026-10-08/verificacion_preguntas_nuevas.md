# Recuento de la verificacion ciega (nuevas)

Preguntas nuevas reales: 43. Con contrario, invencion o logica que no encaja: **7** (umbral 0).
Trampas cazadas: **9/9**. Sin veredicto: 0.
**NO PASA**

## Hallazgos en preguntas reales
- q01-01 `contratos_desempeno_energetico_esco`: logica: La pregunta habla de medir desde un solo lugar el consumo de varios locales, un supuesto (operar en varias instalaciones) que el nodo no trae; no parte del concepto del nodo (contratar una ESCO que financia y garantiza mejoras por falta de capital o de equipo propio) ni indaga sus condiciones.
- q01-11 `observar_al_cliente_en_su_contexto`: logica: La pregunta salta al mensaje y la forma de acercarse al cliente (terreno del siguiente, personalizar) sin tocar el concepto del nodo, que es ir a observar al cliente usar el producto en su contexto real frente a solo encuestas y lo que dice.
- q02-01 `commuting_teletrabajo_sostenible`: logica: El supuesto se contradice a sí mismo: pregunta por una gente que todavía no existe ('cuando tu proyecto empiece a tener gente') y a la vez por cómo 'llegan hoy' y si 'has notado' el peso del viaje; además pregunta solo por el traslado y no por qué puestos podrían hacerse desde casa, así que apenas orienta hacia 'Apuesta por el Teletrabajo' (veredicto marcado por la regla de la duda).
- q02-07 `deep_dive_workshop`: logica: Es una pregunta genérica sobre qué no sabe todavía la persona; no parte del concepto del nodo (un taller intensivo que junta a quien diseña con quien conoce el problema de primera mano para hacer prototipos y evaluarlos) ni pregunta por personas o perfiles que habría que juntar (veredicto marcado por la regla de la duda).
- q02-18 `mobilizar_empleados_cultura_ecologica`: logica: El supuesto no se sostiene: plantea un equipo hipotético ('si tu idea llegara a tener personas trabajando contigo') y luego pregunta si esas personas 'ya saben' lo que se quiere lograr o si ya lo hablaste con alguien, como si existieran hoy (veredicto marcado por la regla de la duda).
- q03-04 `condiciones_latentes_largo_plazo`: logica: La pregunta no parte del concepto del nodo (condiciones latentes de origen antiguo en infraestructura y el estudio de la obra original): pregunta directamente por el sesgo retrospectivo, que es el tema del siguiente nodo, y no toca nada de diseño original ni de debilidades dormidas.
- q03-16 `publicidad_impresa_franquicia`: logica: Caso de duda: el nodo trata de la publicidad impresa para atraer franquiciados (directorios, publicaciones del sector), pero la pregunta nunca menciona lo impreso ni a los franquiciados, cambia el público a 'clientes' y queda como una pregunta genérica sobre presupuesto que no ayuda a decidir sobre los medios impresos.

## Trampas no cazadas

## Arbitraje (cada hallazgo pasa por un árbitro antes de contar)

Se sostienen **1** de 7; se descartan 6. Tras el arbitraje: 1 con lógica que no encaja, 0 contrarios, 0 invenciones. Umbral 0: **NO PASA**.

- q01-01: **se_sostiene** (logica): La pregunta trata de medir desde un solo lugar el consumo de varios locales, que es el tema del siguiente, y no toca nada del nodo: ni la falta de capital, ni la falta de equipo propio, ni el riesgo que asume la ESCO. Además da por hecho varias instalaciones, algo que no sale del nodo.
- q01-11: **se_descarta**: La pregunta arranca con una condición literal del nodo (ya reuniste los datos de tu cliente y no sabes qué hacer con ellos) y pregunta si de verdad sabes qué le importa, que es lo que da la observación y lo que lleva a personalizar. Podría nombrar la observación de forma explícita, pero eso es redacción, no un fallo.
- q02-01: **se_descarta**: Parte del concepto del nodo (el traslado diario y su peso ambiental) y la respuesta orienta entre transporte sostenible y teletrabajo. El roce entre el condicional y el 'hoy' es un defecto de redacción, no de lógica.
- q02-07: **se_descarta**: Las tres opciones (si el problema duele, cómo sería una primera versión para poner en manos de alguien, cómo sumar a otros) tocan la exploración del problema y el prototipado del taller, y reparten bien entre sus siguientes. Es genérica, pero sirve.
- q02-18: **se_descarta**: Pregunta por la actitud de un equipo ante la sostenibilidad y por si ya se habló del tema, que es justo el concepto del nodo y el paso a 'Conoce la Actitud de tu Equipo'. Plantear el equipo en condicional está permitido, y la mezcla de tiempos es solo redacción.
- q03-04: **se_descarta**: Parte de revisar algo después de que salió mal, que es una condición del nodo (investigar una falla), y de si las señales se podían ver antes, que es el núcleo del caso de las condiciones latentes. Sirve de puente natural al sesgo retrospectivo aunque no mencione infraestructura.
- q03-16: **se_descarta**: Reproduce la condición del nodo (presupuesto extra más allá de prensa, referidos e intermediarios) y pregunta cómo sabrías si la inversión trae gente interesada, que es la dificultad de medición que el nodo destaca. La respuesta orienta entre medios impresos y buscadores. Que no nombre lo impreso no la hace incoherente.


## Reescritura de las 7 (decisión del fundador, 8 oct 2026)

Las 7 preguntas observadas se redactaron de nuevo con su corrección (`reescritura_preguntas_nuevas.json`, con el antes y el después; la de las ESCOs se rehízo una segunda vez porque decía "tú misma", que supone el género). Costo: USD 0,0012 + 0,0002; sus neutrales, USD 0,0008. Juez ciego aparte, con trampas sin marcar:


Preguntas nuevas reales: 7. Con contrario, invencion o logica que no encaja: **0** (umbral 0).
Trampas cazadas: **3/3**. Sin veredicto: 0.
**PASA**
