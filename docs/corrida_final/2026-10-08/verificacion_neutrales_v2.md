# Verificación de las neutrales, segunda vuelta (semilla 20261009)

**Resultado: NO PASA.** 16 de 200 sostenidos por el árbitro (8 %); tope 10 (1 de cada 20). Primera vuelta: 49 de 200 (24,5 %).

## Lo que se hizo

- Generador corregido con los cuatro patrones (sin segunda petición, contexto propio, masculino genérico, personas en condicional), la regla única en masculino genérico, y rechazo al generar de los cuatro patrones (commits 503af3379, 57d90d6fa, d8344b684, 37f509f02).
- Regeneración de las 3.417: Haiku 5.5 en cinco pasadas (3.332; USD 0,524 + 0,110 + 0,072 + 0,049 + 0,043) y Sonnet 5.5 de respaldo para las 85 restantes (USD 0,18; declaradas en `neutrales_respaldo_sonnet.json`).
- Guarda del 100 % (`guarda_neutrales_v2.md`): 0 sin neutral; 0 con género, 0 con más preguntas que su base, 0 personas sin condicional, 0 contexto perdido; 24 avisos de la heurística vieja de papeles, revisados: falsos positivos.
- Muestra ciega: 200 pares reales (10 de entrada) y 10 trampas, semilla 20261009 escrita antes en el acta, 10 jueces aparte; las instrucciones del juez añadieron el género (más estrictas).
- Trampas cazadas: 10 de 10. Marcados: 33. Sostenidos por el árbitro: **16** (no_fiel 10, papel_supuesto 6, género 0).

## El patrón (cola variada, sin un defecto dominante)

1. **Reescribe bases que no suponían ningún papel** y pierde su foco ("tu idea" pasa a "algo que te importa"; una decisión del proyecto, a "cualquier decisión en tu vida"): 4.
2. **Franquicias:** "vender franquicias" pasa a "vender tu negocio" (vender la empresa): 2.
3. **Papeles residuales sin condicional:** "quienes deciden el presupuesto", "alguien que trabaja contigo", plurales ("trabajan", "sabríais ambos"): 6.
4. Otros cambios de foco sueltos: 4.

## Los sostenidos

| par | nodo | tipo | motivo del árbitro |
|---|---|---|---|
| n01-04 | `habito_energetico_vs_mecanico` | no_fiel | La base no supone ningún papel y aun así la neutral cambia 'tu idea' por 'algo que te importa', con lo que la pregunta se suelta del proyecto y admite respuestas sobre cualquier cosa. |
| n02-04 | `linking_environmental_performance_budgeting` | papel_supuesto | Lleva los costos a 'tu propio presupuesto' pero sigue preguntando cómo recompensar a 'las personas que logren reducir', lo que da por hecho, sin condicional, que hay gente a cargo. |
| n02-08 | `consignment` | no_fiel | 'Te pidiera pagarle' invierte el flujo del dinero (ahora pagas tú) y choca con 'antes de que recibas el dinero', así que se pregunta por otra situación. |
| n03-14 | `mitigar_falling_asleep_wheel` | no_fiel | La base pregunta cómo harán los usuarios de la idea para no fiarse a ciegas de la IA (lo que no supone ningún papel) y la neutral lo cambia por el criterio de la propia persona. |
| n04-03 | `calibra_tu_propio_ojo` | no_fiel | La base pide una decisión tomada para el proyecto y no supone ningún papel; la neutral la abre a cualquier decisión 'en tu vida' y pierde ese foco. |
| n04-11 | `confidencialidad_nda_adquisicion` | papel_supuesto | Conserva 'cómo sabríais ambos', que no es tuteo neutro y trata a la persona como si fueran dos, como con un socio. |
| n04-17 | `nist_privacy_framework_introduccion` | papel_supuesto | Fuera del paréntesis condicional cierra con 'la forma en que trabajan', en plural, y así da por hecho un grupo aunque la persona trabaje sola. |
| n05-09 | `desafios_implementacion_ia` | no_fiel | Pone 'si trabajas con otras personas' delante de una pregunta que no trata de otros, así que quien trabaja solo se queda sin la segunda pregunta. |
| n05-14 | `estandarizacion_industrial_voluntaria` | no_fiel | El paréntesis convierte la coordinación con otros que enfrentan los mismos desafíos (la idea de los estándares compartidos) en coordinarse primero con los propios colaboradores, y cambia la tercera opción. |
| n05-21 | `proteccion_propiedad_intelectual_franq` | no_fiel | 'Vender tu negocio' significa vender la empresa, no vender franquicias; el ejemplo entre paréntesis no corrige el cambio de sentido. |
| n07-06 | `evaluacion_mercados_objetivo` | no_fiel | Añade una segunda pregunta sobre cómo y con quién decides, un foco que la base no tiene. |
| n08-01 | `requisitos_sistema_retroalimentacion` | no_fiel | La base pregunta por la información, el poder y los incentivos de las personas que participan en la idea; la neutral lo reduce a cómo te enteras tú y qué ganas tú, y pierde el diseño del sistema. |
| n09-12 | `conducir_reuniones_salto_nivel_diez_reglas` | papel_supuesto | Da por hecho, sin condicional, que alguien trabaja con la persona o depende de ella y que ese alguien tiene un equipo propio. |
| n09-14 | `voces_externas_credibles` | papel_supuesto | Copia la base tal cual con 'quienes deciden el presupuesto', que supone por encima de la persona una instancia que decide y que puede no existir. |
| n10-15 | `ppc_para_venta_de_franquicias` | no_fiel | Añade 'vender tu negocio', que significa vender la empresa, un foco que la base (vender franquicias) no tiene. |
| n10-16 | `eliminacion_gestion_por_objetivos_y_numeros` | papel_supuesto | 'Alguien que trabaja contigo' sigue dando por hecho, sin condicional, que hay colaboradores. |

## Los descartados por el árbitro

| par | motivo |
|---|---|
| n01-03 | Cambiar 'tu idea' por 'tu trabajo' no altera lo que se averigua: la elección entre alinear la forma de trabajar o buscar reconocimiento externo sigue intacta. |
| n01-12 | Mantiene la disyuntiva entre público interno y externo y pone en condicional al equipo; 'áreas' es un matiz menor que no cambia lo que se busca. |
| n01-19 | Conserva el foco central (qué información falta para que cada uno sepa cómo hace su trabajo) y pone el papel en condicional; quitar el marco de las reuniones solo simplifica. |
| n02-13 | Cambiar 'proyecto' por 'negocio' no supone jefe, equipo ni socios y no cambia la preocupación financiera que se averigua. |
| n03-02 | Es una de tres opciones a elegir que la base ya traía con 'tu equipo cercano'; la neutral la suaviza y quien trabaja solo puede no elegirla. |
| n04-10 | Lo que se averigua es en qué paso está la persona (entender los riesgos o decidir cómo atacarlos), y eso no cambia por decir 'para tu salud'. |
| n04-13 | Quitar la condición del país de origen es neutralizar un supuesto; las tres opciones sobre lo que frena una venta al extranjero quedan iguales. |
| n05-02 | 'Tus clientes' se entiende como el público al que vendes y no cambia lo que se averigua: si los planes se ajustan a la demanda y si se replantean. |
| n05-03 | 'En el camino' es ambiguo y 'en el proceso' también abarca el envío; se averigua lo mismo (cómo sellas y qué problemas has visto). |
| n05-04 | En el habla común 'vas a fabricar' incluye mandarlo a hacer, y las dos opciones de la pregunta quedan iguales. |
| n06-09 | 'Con qué cuentas cuentas' es torpe pero se sigue entendiendo como los recursos de los que dispones; las dos opciones no cambian. |
| n06-17 | 'Tus proveedores' puede referirse a proveedores futuros y no supone un papel interno; lo que se averigua (si ya negocia o lo hará pronto) es igual. |
| n07-12 | Cambiar 'infraestructura' por 'negocio' simplifica sin cambiar la disyuntiva entre qué proteger, cuánto invertir y qué sistemas son críticos, que sigue nombrando sistemas. |
| n08-07 | Al quitar la organización supuesta conserva el foco central: si sabes qué oye y qué se lleva la mayoría del fondo. |
| n08-19 | Lo que se averigua es si prefieres ver el momento puntual o la cadena causal, y eso no cambia; los ejemplos en primera persona no cambian las opciones. |
| n09-21 | Mantiene la disyuntiva entre culpar a la persona y mirar las condiciones; usar 'tu atención' y dar ejemplos ilustrativos no cambia lo que se averigua. |
| n10-12 | Quitar 'en tu idea' (que sugería gente dentro del proyecto) no cambia lo que se busca: qué señales te dicen que tu retroalimentación llega. |
