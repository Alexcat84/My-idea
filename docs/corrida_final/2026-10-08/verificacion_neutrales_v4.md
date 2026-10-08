# Verificación de las neutrales, cuarta vuelta (semilla 20261011)

**Resultado: falla SOLO en defectos menores.** 0 cambios de sentido o contrarios (umbral 0: **cumple**); 16 con otro defecto (tope 10: no cumple). Trampas de cambio de sentido sin marca: **10 de 10 cazadas**.

**Regla de cierre del fundador (fijada antes de la muestra):** si falla solo en defectos menores, se corrige lo hallado, se declara el residuo en el acta y se sigue con la sincronización, el despliegue y la coherencia. Lo único que detiene la corrida es un cambio de sentido o un contrario. **Se sigue.**

## Lo que se hizo antes de la muestra

- **Corrección declarada de bases (C34):** 382 correcciones en `engine/correcciones_preguntas.json` (formas rotas 213, voseo 170, inglés 14), cada una por edición mínima, comprobaciones automáticas y juez independiente; residuo sin tocar en `residuo_correccion_bases.json`.
- **Nivel 1 ampliado:** papeles implícitos y plurales de grupo ya no pasan tal cual.
- **Regeneración de las 423 neutrales afectadas** (USD 0,308).

## La muestra

200 pares reales (175 de nivel 1, 25 de nivel 2) y 10 trampas de cambio de sentido sin marca; 10 jueces aparte y un árbitro. Marcados: 34; sostenidos: 16 (13 papel supuesto, 3 otro); descartados: 18.

## Lo hallado y su corrección (regla de cierre)

- Las **16 neutrales sostenidas pasan a nivel 3** (plantilla segura): `cierre_cuarta_muestra.json`.
- Las **dos bases con defecto de lengua se corrigen** por corrección declarada verificada: "te detenes" → "te detienes" (un voseo sin tilde que la regla general no veía) y "qué tan cómodos te sientes" → "qué tan cómodo te sientes".

## Residuo declarado

- Defectos menores fuera de la muestra: con 16 de 200 (8 %) en la muestra, se estiman en torno a 250 neutrales de nivel 1 o 2 con un defecto menor, casi todos **bases copiadas tal cual que suponen un grupo de forma implícita** (plurales de ustedes como "identificaron", "creen"; "la dirección a la que convencer"; "el equipo de liderazgo"). Ninguno cambia el sentido: en cuatro muestras ciegas con trampas, desde que existe el sistema por niveles, 0 cambios de sentido en pares reales.
- Voseo sin tilde ("detenes"): la regla general exige la tilde; formas sin tilde pueden quedar en otras bases. Queda anotado para una pasada posterior.
- 1 base con voseo que el juez no aprobó (`trabajo_como_imaginado_vs_trabajo_como_hecho`): su neutral no sale tal cual.

## Estado final de los niveles

Bases: {1: 2661, 2: 388, 3: 282}. Entradas: {1: 83, 3: 3}.

## Los sostenidos

- n03-16 `validacion_con_franquiciados` (base, nivel 1): otro: 'Qué tan cómodos te sientes' no concuerda: pone el adjetivo en plural con el tuteo singular.
- n04-02 `matriz_de_seleccion` (base, nivel 1): papel_supuesto: Trata a la persona de ustedes ('hayan elegido', 'tienen') y da por hecho un grupo que decide y reparte responsabilidades.
- n04-19 `formulacion_teorias_causa` (base, nivel 1): papel_supuesto: Todo va en plural ('identificaron', 'creen', 'podrían'), dando por hecho un grupo en vez de tutear a una persona.
- n05-02 `hacer_remarcable_lo_requerido` (base, nivel 1): papel_supuesto: Da por hecha una organización con áreas y otras partes del proyecto que presionan, que quien emprende solo no tiene.
- n05-06 `pruning_portafolio` (base, nivel 1): papel_supuesto: Dos de las tres opciones suponen sin condición una organización con dirección a la que hay que convencer.
- n05-13 `sostener_cambio_contexto_continuo` (base, nivel 1): otro: 'Te detenes' es voseo; el tuteo neutro pide 'te detienes'.
- n06-13 `comunicacion_a_toda_la_empresa` (base, nivel 1): papel_supuesto: Da por hecho un 'equipo de liderazgo' sin condicional, estructura que la persona puede no tener.
- n07-03 `automatizacion_software_gestion_innovacion` (base, nivel 2): papel_supuesto: 'Lo que aprueban' supone un grupo que aprueba, y el condicional 'tienes equipo, si lo tienes' queda circular.
- n07-09 `monitoreo_continuo` (base, nivel 2): papel_supuesto: 'Cómo van a organizarse' sigue dando por hecho un grupo aunque el equipo quede condicional al final.
- n07-13 `educacion_estadistica_para_la_calidad` (base, nivel 1): papel_supuesto: Las dos opciones suponen una organización con un área especializada y otras personas que hacen el trabajo.
- n07-18 `buyer_rating_system` (base, nivel 1): papel_supuesto: Da por hecho que existe una dirección a la que hay que convencer, y el nodo no trata de eso.
- n08-15 `seleccion_relaciones_cofundadores` (base, nivel 2): otro: El 'si los tienes' choca con 'quiénes podrían ser tus cofundadores' y deja una frase incoherente.
- n09-02 `evaluacion_alternativas_solucion` (base, nivel 1): papel_supuesto: Se mantiene el plural de ustedes ('consideraron', 'decidieron', 'creen'), que da por hecho un grupo.
- n09-14 `requisitos_sistema_retroalimentacion` (base, nivel 1): papel_supuesto: Da por hecho un grupo de personas con jerarquía y permisos dentro de la idea, sin condicional y sin que el tema lo pida.
- n09-17 `organizacion_independiente_de_calidad` (base, nivel 1): papel_supuesto: Una de las opciones supone sin condición 'los equipos' que se comunican y trabajan juntos.
- n10-10 `gestion_efectiva_benchmarking` (base, nivel 1): papel_supuesto: 'Qué apoyo necesitas de arriba' y 'dónde están parados' dan por hecha una jerarquía y un grupo.

## Los descartados por el árbitro

| par | motivo |
|---|---|
| n01-06 | 'Todos' puede ser clientes o terceros y 'a quién corregir o qué cambiar' deja abierta la opción de cambiar algo sin personas a cargo. |
| n01-10 | Todo va dentro del hipotético 'si pudieras reunir', así que no da por hecho que ese grupo ya exista. |
| n01-20 | 'Las personas en ese momento' pueden ser la propia persona, clientes o proveedores; no supone ninguna estructura. |
| n02-07 | 'Qué te llevas a analizar' es una construcción válida (llevarse algo para analizarlo), rara pero no rota. |
| n02-12 | El tema del nodo es cuidar a tu equipo y el 'cuando trabajas con alguien a tu cargo' funciona como condición. |
| n02-14 | El subjuntivo 'que se unan' ya es hipotético y compensar a quien se sume es el tema mismo del nodo. |
| n02-16 | El equipo ya es condicional y 'involucrar a más personas' se responde bien aunque hoy no haya nadie. |
| n03-01 | El tema del nodo es planear el crecimiento de tu equipo, así que hablar del plan con cada persona y de quién asciende es inherente. |
| n04-18 | 'Tú o alguien más' admite que ese alguien sea un cliente, así que ponerse de acuerdo sobre la calidad no exige tener equipo. |
| n05-01 | Habla de definir roles a futuro para la gente que encaje, no supone que hoy ya haya varias personas. |
| n05-10 | 'Tus almacenes' es una cosa física dentro de una opción, no un papel ni una estructura de personas. |
| n05-17 | Dentro de un 'cuando' condicional, las personas a quienes se enseña el método son parte del tema de validar ese método. |
| n08-12 | El nodo trata de defender al cliente ante quien decide, así que llevar la idea a los líderes es el tema mismo. |
| n09-04 | El nodo trata de dejar decidir a los más cercanos a los hechos; que haya gente que trae opiniones es inherente al tema. |
| n09-11 | La pregunta entera queda bajo 'tus empleados, si los tienes', y el tema del nodo es capacitar a ese equipo. |
| n10-11 | Preguntar quiénes deben estar en la conversación admite 'solo yo' o asesores externos; no supone ninguna estructura. |
| n10-13 | 'En tu proyecto o equipo' es una alternativa con 'o' y no exige tener equipo. |
| n10-19 | El nodo trata de decidir cuándo despedir, así que la persona a despedir es el tema mismo. |
