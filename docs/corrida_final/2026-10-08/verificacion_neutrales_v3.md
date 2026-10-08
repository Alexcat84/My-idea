# Verificación de las neutrales, tercera vuelta (seguridad máxima de sentido, semilla 20261010)

**Resultado: NO PASA.** 0 cambios de sentido o contrarios (umbral 0: **cumple**); 17 con otro defecto (tope 10: **no cumple**). Trampas de cambio de sentido sin marca: **10 de 10 cazadas**.

## El sistema por niveles

| | Nivel 1 (base tal cual) | Nivel 2 (edición mínima verificada) | Nivel 3 (plantilla segura) |
|---|---|---|---|
| Bases vivas (3.331) | 2.601 | 462 | 268 |
| Entradas (86) | 83 | 0 | 3 |

Coste de la regeneración por niveles: USD 1,691 + 0,200 (editor Haiku 5.5, juez independiente Sonnet 5.5). Guarda del 100 %: 0 en género, segunda petición, personas sin condicional y contexto perdido; 32 avisos de la heurística vieja de papeles, revisados: falsos positivos.

## La muestra

200 pares reales (10 de entrada) de las neutrales con texto (niveles 1 y 2; el nivel 3 no tiene texto: la app pone la plantilla) y 10 trampas: neutrales reales con el sentido cambiado sin marca (más/menos, un término clave, antes/después, una negación). 10 jueces aparte con instrucciones nuevas (cambio de sentido aparte de los demás defectos) y un árbitro.

Composición: 170 de nivel 1 y 30 de nivel 2. Marcados: 29; sostenidos: 17; descartados: 12.

## Lo que dice el resultado

1. **El sentido está protegido:** ningún par real cambia de sentido; las 10 trampas que lo cambiaban se cazaron.
2. **15 de los 17 defectos son de nivel 1, es decir, de la PREGUNTA BASE copiada tal cual:** la base misma supone un grupo de forma implícita ("la gente que trabaja en él", "para que todos sepan", plurales como "tienen claro", "como organización", "quien toma decisiones"), trae voseo que la lista de voseo no conocía ("sentís", "contactás", "imaginás", "descubrís", "decidís", "contás") o una forma rota ("figura out", "lo que ves que ofreces de entrega", "qué consecuencias vería eso"). Esas bases son las que la app ya muestra hoy.
3. **El nivel 2 (edición mínima) tiene 2 defectos en 30:** un condicional que deja "la organización" sin condicionar, y un "si lo tienes" que choca con una opción de la misma pregunta.

## Los sostenidos

- n01-09 `normalizacion_de_la_desviacion` (base, nivel 1): papel_supuesto: 'La gente que trabaja en él' da por hecho, sin condicional, que hay personas trabajando en el proyecto.
- n02-20 `estrategias_estimacion_costos` (base, nivel 1): papel_supuesto: 'Convencer a quien toma decisiones' supone a otra persona por encima que decide, cosa que quien emprende solo no tiene.
- n02-21 `cognisance_organizacional` (base, nivel 2): papel_supuesto: Condiciona el equipo pero deja 'la organización' que mide y celebra como algo dado.
- n03-09 `market_type_revenue_growth` (base, nivel 1): otro: Conserva la expresión en inglés 'figura out', que es una forma rota.
- n03-12 `definir_metas_smart_de_proyecto` (base, nivel 1): papel_supuesto: 'Cómo desarrollan' y 'van inventando' en plural suponen un grupo que decide en conjunto.
- n03-13 `roles_product_owner_scrum_master` (base, nivel 1): papel_supuesto: 'Para que todos sepan' da por hecho un grupo de personas a las que mantener informadas.
- n04-08 `planificar_cinco_olas_venta` (base, nivel 1): otro: Voseo ('sentís', 'contactás') en lugar de tuteo neutro.
- n04-16 `modos_de_entrada_intermediarios` (base, nivel 1): otro: Voseo ('imaginás') en lugar de tuteo neutro.
- n04-18 `programa_cero_defectos` (base, nivel 1): papel_supuesto: Da por hecho que hay 'responsables de equipos' que guían a otros, sin condicional.
- n05-06 `decision_comunicacion` (base, nivel 1): otro: Voseo ('descubrís', 'decidís', 'contás') en lugar de tuteo neutro.
- n08-13 `dmaic_fase_define` (base, nivel 1): papel_supuesto: Habla en plural ('tienen claro', 'quieren', 'sabrían') y supone un grupo en vez de tutear a la persona.
- n08-16 `lenguajes_jerarquia_organizacional` (base, nivel 1): papel_supuesto: Supone que en la idea hay otra persona que toma las decisiones finales y aprueba.
- n08-18 `ceder_control_reforzar_competencia_claridad` (base, nivel 2): otro: El 'si lo tienes' añadido choca con la alternativa de 'armar ese equipo', y 'a la que le gustaría' queda como una forma rota.
- n09-08 `detectar_prioridad_cliente_entrega` (base, nivel 1): otro: Forma rota: 'no les gusta lo que ves que ofreces de entrega', además de la discordancia entre 'alguien' y 'se arrepientan'.
- n09-09 `categorizacion_ranking_proyectos_cubetas` (base, nivel 1): papel_supuesto: 'Hacia donde quieres ir como organización' da por hecho una organización que la persona puede no tener.
- n09-12 `contacto_con_el_cliente` (base, nivel 1): papel_supuesto: Da por hecho que alguien trabaja contigo y atiende a clientes, cuando quien emprende solo puede atenderlos en persona.
- n10-13 `antidilution_carve_outs` (base, nivel 1): otro: 'Qué consecuencias vería eso' es una forma rota; los inversionistas actuales en sí son el tema del nodo.

## Los descartados por el árbitro

| par | motivo |
|---|---|
| n01-10 | El inciso 'si lo tienes' queda algo torpe pero se entiende, condiciona el equipo y conserva el sentido. |
| n03-07 | 'La gente se equivoca' es genérico (puede incluir clientes o a cualquiera que toque el proceso), no supone un equipo propio. |
| n04-07 | El tema del nodo son los franquiciados, así que nombrarlos no es un defecto. |
| n05-09 | Un edificio no es un papel ni una estructura de personas, y el tema del nodo es el consumo del edificio. |
| n06-08 | Los grupos o áreas se plantean como algo futuro, a medida que la idea crece y suma personas, no como algo que ya existe. |
| n07-10 | El tema del nodo es otorgar el título de fundador entre varios, así que nombrar a los fundadores es propio del tema. |
| n07-11 | El tema del nodo es delegar decisiones en los más cercanos a los hechos, así que nombrar a esas personas es propio del tema. |
| n08-04 | 'Cuando necesitas que otros la lleven adelante' plantea una circunstancia propia del tema (separar el debate de la decisión), no supone un equipo fijo. |
| n08-07 | El tema del nodo son los franquiciados actuales, así que nombrarlos no es un defecto. |
| n09-18 | El tema del nodo es detectar a quienes se salen del promedio, así que hablar de esa persona es propio del tema. |
| n10-01 | 'La gente aún no cree' es una referencia genérica a la gente, no a un equipo propio. |
| n10-12 | 'Lo que producen' remite al equipo ya condicionado con 'si lo tienes'; el juez exige algo que no afecta. |
