# Verificación de las neutrales (paso 1 de la corrida final)

**Resultado: NO PASA.** Umbral: como máximo 1 de cada 20 pares con fallo de fidelidad (10 de 200).

## Lo que se hizo

- **Generación (A2):** 3.417 neutrales con Haiku 5.5 (3.331 de base y 86 de entrada), 0 fallidas, USD 0,3482, de 01:31:27 a 02:30:46 UTC.
- **Guarda automática sobre el 100 %** (`guarda_neutrales.md`): 0 bases y 0 entradas sin neutral; 20 neutrales nombran un papel sin condicional, la mayoría falsos positivos de la heurística ("equipos" como maquinaria, "socios" dentro de una lista de opciones).
- **Muestra ciega:** 200 pares reales (10 de entrada) y 10 trampas sin marcar (la neutral de otro nodo del mismo dominio), en 10 paquetes, semilla 20261008, 10 jueces aparte.
- **Trampas cazadas: 10 de 10.**

## El recuento

- Marcados por los jueces: 64. Un árbitro aparte sostuvo **49** y descartó 15.
- Sostenidos por tipo: genero 6, no_fiel 38, papel_supuesto 5.
- **49 de 200 = 24.5 %**, con un tope de 10.

## El patrón (no son casos sueltos)

1. **Añade una segunda petición** que la base no tiene ("o cómo lo harías con alguien por encima", "con quien trabajes").
2. **Pierde el contexto propio de la base** (franquicia, proveedores, seguridad) y lo vuelve genérico.
3. **Marca el género:** "tú misma, si trabajas sola". En toda la caché, 80 de 3.331 neutrales de base y 1 de 86 de entrada; en las preguntas base, 3 de 3.954 (no lo trae la base: lo introduce el generador).
4. **Mete personas sin condicional** ("las personas que te acompañan").

## Los hallazgos sostenidos

| par | nodo | tipo | motivo del árbitro |
|---|---|---|---|
| n01-07 | Revisa Que Tus Controles Funcionen | no_fiel | Añade una segunda petición (cómo lo harías con alguien por encima o un equipo) que la base no tiene. |
| n01-11 | Traza el Viaje del Cliente | genero | 'tú misma si estás sola' marca el género femenino de la persona. |
| n02-03 | Diseña Junto a tus Proveedores | no_fiel | Pierde el diseño conjunto con proveedores, centro de la base, y lo cambia por 'las personas que trabajan contigo'. |
| n02-10 | Elige y Ajusta tus Controles | no_fiel | Añade una petición nueva sobre el punto de partida con quien trabajes, un segundo foco que la base no tiene. |
| n02-15 | Equilibra Mantenimiento Preventivo y Correctivo | no_fiel | Cambia la segunda opción de accidentes y riesgos (daño a personas) por imprevistos y fallos de uso, lo que cambia lo que se averigua. |
| n02-17 | Elimina Barreras al Orgullo Laboral | genero | '(o tú misma, si trabajas sola)' marca el género femenino de la persona. |
| n02-20 | Mide Procesos, no Solo Resultados | genero | '(o tú misma)' marca el género femenino, y además 'salgan bien' pierde el foco en la seguridad. |
| n03-04 | Diseña Paneles para cada Rol | papel_supuesto | Sin ningún condicional, da por hecho que hay varias personas, cada una con su parte del trabajo, a quienes mostrar indicadores. |
| n03-05 | Diseña Controles para Sostener la Mejora | papel_supuesto | Da por hecho, sin condicional, que hay otras personas que usarán los controles y podrían resistirse. |
| n03-11 | Crea tu Folleto de Franquicia | no_fiel | Pierde el contexto de franquicia y el cumplimiento legal, y cambia el siguiente paso inmediato por una costumbre general. |
| n03-13 | Despliega tu Plan Paso a Paso | no_fiel | Da por hecho que empieza por su cuenta en vez de preguntar si tiene equipo, y añade un foco nuevo sobre la base sólida para compartir. |
| n03-18 | Pásate a la Energía Renovable | no_fiel | Convierte un hecho estructural (varios lugares frente a uno solo) en una preferencia y cambia los lugares por actividades. |
| n03-21 | Haz Transparente la Crítica Entre Pares | no_fiel | Pasa de quién debe participar en la crítica transparente que se implanta a las críticas sobre el trabajo propio, y supone compañeros. |
| n04-02 | Construye tu Estrategia con tu Equipo | papel_supuesto | Da por hecho, sin condicional, que hay 'personas que te acompañan' en la estrategia. |
| n04-04 | Anticipa lo Desconocido en Contratos | genero | 'para estar tranquila' marca el género femenino de la persona. |
| n04-10 | Anticipa Consecuencias No Intencionadas | no_fiel | Añade la condición 'incluso si todo sale bien en lo que tú controlas', que estrecha la pregunta hacia factores externos. |
| n04-12 | Usa Gráficos de Control | no_fiel | Añade una segunda pregunta sobre quién supervisa y cómo lo registran, que además introduce la figura de un supervisor. |
| n04-18 | Trabaja en Paralelo, Siempre | genero | 'a ti misma' marca el género femenino de la persona. |
| n05-01 | Fija Expectativas Desde el Inicio | no_fiel | Añade una segunda pregunta sobre qué espera de ti alguien por encima, un foco ajeno a la base que además insinúa un jefe. |
| n05-15 | Investiga a Fondo tu Entorno | no_fiel | Añade una pregunta previa que pide recontar lo descubierto, un segundo foco que la base da por hecho. |
| n06-02 | Reconoce el Estilo de tu Contraparte | no_fiel | Añade una pregunta sobre cómo suele tratar a los demás la otra parte, que la base no pide. |
| n06-03 | Da Autonomía a tus Supervisores | papel_supuesto | Da por hecho que existe alguien que coordina el trabajo y un equipo cuya forma de trabajar cambia. |
| n06-09 | Distingue Conflictos entre Socios | no_fiel | Cambia el diagnóstico de un conflicto actual por una preferencia general e hipotética sobre qué tensiones cuestan más. |
| n06-11 | Ajusta la Participación a la Urgencia | papel_supuesto | Sin condicional, da por hecho que la persona trabaja con otros a quienes propone direcciones. |
| n06-19 | Gestiona el Riesgo con Método | no_fiel | Añade una segunda petición sobre cómo se reparte el trabajo con quien te apoye. |
| n07-05 | Comparte Información en tu Cadena | no_fiel | Añade una segunda pregunta sobre compartir información con proveedores o socios. |
| n07-08 | Elige el tamaño justo de caja | no_fiel | Pierde la pregunta por la consistencia en la cantidad de relleno, la mitad del foco de la base. |
| n07-18 | Decide Qué Vas a Prototipar | no_fiel | Cambia 'cómo interactuarían con tu idea' (uso) por 'cómo reaccionarían ante la idea' (aceptación), una opción que averigua otra cosa. |
| n07-21 | Sigue el Proceso de Venta | no_fiel | Convierte el proceso de venta de la franquicia, contenido central de la base, en la venta de cualquier cosa. |
| n08-01 | Prepara tu Equipo de Crisis | no_fiel | Añade una segunda pregunta sobre cómo se reparten las decisiones con un socio o colaborador. |
| n08-04 | Aprovecha Plataformas ya Grandes | no_fiel | Pierde lo que pide la base, cuál plataforma es la más rápida o viable para empezar, y pregunta en cambio dónde pasan su tiempo. |
| n08-07 | Asegura la Calidad Siempre | no_fiel | Invierte la pregunta: de qué cambiaría si todos se comprometieran a qué cambiar para lograr ese compromiso. |
| n08-10 | Elige a tu Próximo Director General | no_fiel | Añade una pregunta sobre cómo encaja en la decisión alguien por encima o un socio. |
| n08-13 | Valida tu Ajuste Problema-Solución | no_fiel | La primera opción deja de ser la preocupación por alinear al equipo y pasa a ser si tienes con quién compartir la idea. |
| n08-15 | Observa sin Suponer Nada | no_fiel | Añade el filtro 'que casi nadie parece tomar en cuenta', que estrecha lo que se busca. |
| n08-17 | Decide si Vender tu Empresa | no_fiel | Cambia la opción de necesitar a alguien que lleve el proceso con compradores por la de ya tener un interesado, otra situación. |
| n08-21 | No Busques un Número Mágico | no_fiel | Borra la franquicia, tema de la base, y pierde el foco en unidades vendidas y pagos de los franquiciados. |
| n09-01 | Atiende lo que le Preocupa | no_fiel | Lleva las conversaciones uno a uno de trabajo a una charla de apoyo personal con un confidente, ajena al proyecto. |
| n09-04 | Genera Confianza en tu Calidad | no_fiel | Añade una segunda pregunta sobre cómo se coordinaría con un superior o un equipo. |
| n09-05 | Define tu Estructura de Regalías | no_fiel | Confunde las regalías con un porcentaje de tus propias ventas y diluye a los franquiciados, lo que cambia el sentido. |
| n09-09 | Pregunta Qué, No Quién | no_fiel | Añade una segunda pregunta sobre cómo reacciona la gente ante un error. |
| n09-12 | Arregla Fallos lo Antes Posible | no_fiel | Añade una pregunta sobre en qué momento te das cuenta y cambia el foco de dónde duele más a qué cuesta detectar a tiempo. |
| n09-19 | Decide Cuándo Sumar Ejecutivos | no_fiel | Cambia a quien está contigo desde el inicio por un vago 'alguien de tu entorno' y pierde ese dilema; además 'tú mismo' marca el género. |
| n10-03 | Diagnostica las Fallas de Calidad | no_fiel | Pierde el foco en el criterio de remuneración (cantidad frente a calidad) y pregunta solo cómo sabes si lo haces bien. |
| n10-06 | Da la Mala Noticia de Golpe | no_fiel | Abre la pregunta a cualquier cosa que importe, incluso un plan personal, y a un momento futuro, con lo que pierde el foco en la idea. |
| n10-07 | Enfoca tus Recursos Regulatorios | no_fiel | Añade una pregunta nueva sobre cómo influye tener a alguien por encima o un equipo a cargo. |
| n10-08 | Decide quién empaca tus envíos | genero | 'lo haces tú misma' marca el género femenino de la persona. |
| n10-10 | Ve el Error como Síntoma | no_fiel | Reduce 'por qué la persona actuó' a 'por qué actuaste tú' y añade una segunda pregunta sobre cómo influyen otros. |
| n10-13 | Moderniza tu Sistema de Climatización | no_fiel | Pierde el foco en la climatización y los recursos del edificio y lo cambia por el uso de energía o agua donde trabajas o vives. |

## Los descartados por el árbitro

| par | motivo |
|---|---|
| n01-19 | La base ya enumera inversionistas, fundadores y empleados; la neutral conserva las dos preocupaciones y solo cambia la forma. |
| n02-01 | La neutral va en condicional ('si pudieras') y busca lo mismo que la base, que ya suponía trabajadores. |
| n02-07 | Sigue pidiendo los números concretos que indicarían que el plan funciona; 'te gustaría ver para sentir' es solo forma. |
| n02-11 | Sin el contexto previo, preguntar qué te quita el sueño y cuánto arriesgarías averigua lo mismo; es simplificación. |
| n02-18 | Quitar 'en ese mercado' no cambia lo que se busca: cómo evaluar qué socio encaja mejor y qué comprobar antes de decidir. |
| n03-15 | 'Quienes pusieron dinero' incluye a la propia persona o a su familia y no supone más estructura que la base; la preocupación es la misma. |
| n04-16 | Mantiene el mismo dilema (autonomía sin confianza o datos insuficientes); 'por ti' es un cambio de forma que no cambia lo que se averigua. |
| n04-17 | Describir de qué tratan las historias es contexto; la pregunta (qué practicar: dar, recibir u otra cosa) es la misma. |
| n05-03 | Vuelve condicional al equipo y pone en su lugar la comodidad propia para quien trabaja solo, que es justo su trabajo. |
| n05-04 | La base ya era condicional; 'organización colectiva' entre quienes trabajan contigo averigua lo mismo que la representación de los trabajadores. |
| n05-17 | La disyuntiva 'a ti o a las personas' mantiene lo que se averigua (exposición y si se evaluó); los cambios de forma son menores. |
| n06-21 | Quitar 'de tu idea' no cambia lo que se averigua: si usa una segunda prueba al entrar. |
| n07-15 | 'Personas que están lejos' conserva la distancia y la pregunta por el tipo de apoyo posventa, que es lo que se busca. |
| n07-19 | 'Cuando alguien...' funciona como condicional genérico y busca lo mismo: quién marca las prioridades y quién cuida el oficio. |
| n07-20 | Quitar 'estés negociando términos de inversión' retira una estructura supuesta y mantiene la preocupación por lo que te tocaría. |
