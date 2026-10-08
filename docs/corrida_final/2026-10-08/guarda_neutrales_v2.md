# Guarda automatica de las neutrales (100 %): papeles supuestos y los cuatro patrones

Neutrales revisadas: 3417 (3331 de base, 86 de entrada).
Bases vivas sin neutral: 0. Entradas vivas sin neutral: 0.
Neutrales que nombran un papel sin condicional: **24**. Revisadas una por una: las 24 son falsos positivos de esa heurística ("equipos" como maquinaria, luces o servidores; "socios" o "colaboradores" como una opción dentro de una lista; "junta" en el nodo que trata de la junta directiva). Ninguna da por hecho un papel que la persona puede no tener.

- `anticipacion_riesgos_fundacionales` (base), papel «socios»: Pensando en los riesgos que pueden aparecer al crear un negocio, como buscar dinero de inversionistas, trabajar con socios cercanos o decidir cómo se reparten las participaciones, ¿hay alguno que ya estés negociando o enfrentando ahora mismo, o es algo que quieres prepararte para evitar en el futuro?
- `comparacion_metodos_inversion` (base), papel «equipos»: Para que tu idea crezca o funcione, ¿necesitarías invertir en algo concreto como equipos, tecnología, infraestructura o un proyecto grande? Si es así, ¿tienes claro cuánto dinero necesitarías y cuándo esperas que esa inversión te devuelva lo gastado?
- `cultura_de_experimentacion_continua` (base), papel «colaboradores»: De todo lo que has aprendido sobre experimentar continuamente con tu idea, ¿cómo imaginas que otras personas, ya sean clientes, colaboradores o usuarios, podrían participar activamente en mejorar lo que estás construyendo?
- `indemnification_clause` (base), papel «socios»: ¿Estás pensando en vender tu idea o proyecto en los próximos meses, o estás negociando términos importantes con personas que quieran entrar como socios o inversionistas en la dirección del negocio?
- `preparacion_due_diligence` (base), papel «socios»: ¿Ya has compartido tu idea o alguna parte del proyecto con otras personas, como amigos, posibles socios, asesores o personas que te ayuden en el desarrollo?
- `tamano_junta_directiva_vc` (base), papel «junta»: Ahora que estás pensando en cómo estructurar tu junta directiva con los inversionistas, ¿qué tan cómodo te sientes liderando personalmente todos los cambios que van a venir en los próximos años? Porque a veces los fundadores descubren que lo que los hizo brillar al principio no es exactamente lo que la idea necesita cuando crece.
- `analisis_pareto_de_proveedores` (base), papel «socios»: De los proveedores o socios que te dan más problemas, ¿hay alguno con el que te gustaría trabajar de forma más cercana y conjunta para resolverlos, o prefieres enfocarte en presionarlos para que mejoren por su cuenta?
- `arrendamiento_verde` (base), papel «equipos»: ¿Qué parte de tu forma de trabajar consume más energía o genera más residuos en tu día a día: es por el lugar donde trabajas, o por la tecnología y los equipos que usas para funcionar?
- `auditoria_energetica_sistematica` (base), papel «equipos»: Además de saber cuánta energía estás usando, ¿qué es lo que más te gustaría mejorar en tu forma de trabajar: reducir lo que se desperdicia en general, entender mejor cómo fluye tu trabajo de principio a fin, o evitar que tus equipos se dañen y dejen de funcionar?
- `auditoria_ti_verde` (base), papel «equipos»: Después de revisar qué tecnología usas ahora, ¿cuál es el mayor desperdicio que sospechas que está pasando? ¿Es en la energía que consumen tus equipos o servidores, en los aparatos que no estás aprovechando, o quizás en algo relacionado con los desplazamientos (por ejemplo, viajes que podrían resolverse con una videollamada)?
- `dialogo_stakeholders` (base), papel «colaboradores»: Ahora que has empezado a escuchar a las personas que te rodean (clientes, colaboradores, proveedores u otras partes interesadas) y a construir esas relaciones, ¿qué te gustaría que pasara después? ¿Lo ves como algo que ya hiciste una vez y ahora necesitas mantener y mejorar, o todavía estás en el proceso de hacer que esa conversación realmente funcione?
- `evaluacion_mejora_programa` (base), papel «colaboradores»: En tu idea, ¿trabajas o vas a trabajar con personas que no son directamente tuyas, como contratistas, personal de agencias o colaboradores de otros negocios en el mismo espacio?
- `feedback_supervisores_trabajadores` (base), papel «equipos»: En tu idea o proyecto, ¿hay momentos en que los equipos o recursos que usas no funcionan como deberían, o pierden capacidad con el tiempo? Si es así, ¿qué impacto tiene eso en lo que intentas lograr?
- `machinery_equipment_safety` (base), papel «equipos»: Cuando tienes que hacer mantenimiento, reparación o ajuste a tus equipos, ¿cómo te aseguras de que nadie los encienda por accidente mientras trabajas en ellos? ¿Y hay equipos en tu actividad que levanten o muevan cargas muy pesadas?
- `personal_protective_equipment` (base), papel «equipo»: Más allá del equipo de protección que ya usas, ¿hay algo en el ambiente donde trabajas que flote en el aire o que respires, como polvo, químicos o vapores, y que te preocupe o que creas que necesita protección especial? ¿O el riesgo principal viene de otro lado, como el contacto con materiales biológicos o enfermedades?
- `prevencion_control_peligros` (entrada), papel «equipos»: Frente a lo que puede lastimarte en tu trabajo o en una actividad nueva, ¿cómo te proteges hoy: quitando el peligro de raíz, cambiando equipos o formas de trabajar, o confiando sobre todo en equipo de protección?
- `adoptar_co_inteligencia_ia` (base), papel «socio»: Ahora que ves que la IA puede trabajar contigo como un socio que piensa, ¿hay alguna situación concreta de tu proyecto en la que sientas que necesitas practicar, probar o generar algo antes de llevarlo a la realidad con clientes o inversores?
- `stakeholder_mapping_wheel` (base), papel «socios»: Ahora que ya identificaste a todas las personas y organizaciones que influyen en tu idea, ¿cuál es el siguiente paso más urgente que necesitas dar: cerrar conversaciones o acuerdos con algunas de ellas, coordinar cómo se mueven los recursos o productos entre varios socios, o lograr que muchas organizaciones diferentes trabajen juntas de forma rápida y sincronizada?
- `export_administration_regulations` (base), papel «socio»: En este momento, ¿ya estás preparando el envío de tu producto al extranjero, estás planificando un viaje para negociar con clientes internacionales, o acabas de recibir una solicitud o contrato de un socio en el extranjero que tiene condiciones especiales sobre con quién puedes o no puedes trabajar?
- `investigacion_empresa_extranjera` (base), papel «socios»: Una vez que hayas identificado y validado a esos posibles compradores o socios en el extranjero, ¿qué tan importante es para ti mantener y fortalecer esas relaciones a lo largo del tiempo, o prefieres explorar constantemente nuevos contactos?
- `diseno_programa_capacitacion_franquicia` (base), papel «equipo»: Una vez que los franquiciados completen la capacitación inicial y abran sus ubicaciones, ¿qué desafíos crees que enfrentarán en el día a día que podrían requerir tu apoyo continuo, y cuál es tu preocupación más grande: que el equipo de cada franquicia rote constantemente, o que los propios franquiciados se sientan solos en la operación?
- `reporta_el_riesgo_sin_maquillaje` (base), papel «socios»: ¿Hay algún riesgo o problema en tu idea que aún no le has contado a nadie (ni a posibles socios, ni a mentores, ni a ti mismo con claridad) porque te preocupa cómo reaccionen o qué piensen?
- `usa_el_no_del_proveedor_a_tu_favor` (base), papel «socio»: ¿Hay alguna persona, cliente, proveedor o socio con la que hayas estado conversando hace un tiempo y de repente dejó de responder, o la conversación simplemente se quedó estancada sin que supieras bien por qué?
- `eficiencia_energetica_almacenes` (base), papel «equipos»: Cuéntame, ¿tu idea o proyecto implica operar algún espacio físico, como una bodega o un local con iluminación, climatización o equipos? Si es así, ¿cómo se ve hoy ese lugar en cuanto a la antigüedad de sus luces y en qué gastos de energía te estás fijando más?

## Marcan el género del lector (precisa): **0**


## Más preguntas que su base (precisa): **0**


## Personas sin condicional (heurística: revisar): **0**


## Contexto propio de la base perdido (heurística: revisar): **0**

