# Redactor con respaldo (propuesta)

**Estado:** propuesta, sin código y sin API. Espera el visto del fundador (decisión del 9 oct 2026: las reglas en
el prompt llegaron a su límite y no se mide más hasta cambiar el diseño del redactor).

**Evidencia:** las tres mediciones de la corrida final, en `docs/corrida_final/2026-10-08/`:

| Medición | Carpeta |
|---|---|
| M1 | `medicion_ab/` |
| M2 | `medicion_ab2/` |
| M3, la última, por el camino de producción y con dos jueces | `medicion_final/` |

Cada hallazgo se nombra con su id, `M<medición><versión>-<paquete>-<n>`. El anexo trae los 70 hallazgos sostenidos
por el árbitro, con su plan, su clase, el lugar del plan donde están y el punto que lo quitaría.

## Lo que dicen las tres mediciones

- **70 hallazgos sostenidos en total. 17 ya están resueltos y no reaparecieron:**
  - 3 eran del guion de la primera medición;
  - 5 eran la frase fija de «aún no cubre» (0 en M3);
  - 9 eran premisas de preguntas de la IA y contrarios de cálculo: «ya decidiste empezar», el correo que recupera las
    cuentas, la resta al revés, la cuota de defectos, «siguen vigentes».
- **Quedan 53 abiertos.** Todos los escribe el redactor por su cuenta.
- **Dónde viven:** 41 de los 70 están en prosa narrativa (11 en la introducción del plan, 30 en los párrafos de las
  etapas) y 18 en pasos numerados. La prosa narrativa es solo el **18 % del texto** de un plan (medido en M3) pero
  junta el **59 % de los hallazgos**.
- **Los 17 de M3, por punto:** cada uno cae en alguno de los cinco.

  | Punto | Hallazgos de M3 |
  |---|---:|
  | 1 | 2 |
  | 2 | 4 |
  | 3 | 5 |
  | 4 | 5 |
  | 5 | 1 |

## Resumen

| Punto | Abiertos que quitaría (de 53) | De la última (de 17) | Cómo lo garantiza | Coste por plan | Esfuerzo |
|---|---:|---:|---|---:|---|
| 1. «Material» | 2 | 2 | por código (filtro) | 0 | 0,5 a 1 día |
| 2. Números por código | 8 (+3 en parte) | 4 | lo reduce: la IA recibe el dato hecho, pero puede seguir leyéndolo mal | +0,001 USD | 2 a 3 días |
| 3. Citar o callar | 20 | 5 | por código, que la referencia exista; no que respalde | +0,004 a 0,006 USD | 4 a 6 días |
| 4. Menos prosa de enlace | 18 (+20 que viven en prosa) | 5 (+7 en prosa) | por construcción, lo que no se escribe no se inventa | −0,003 a −0,005 USD | 1 a 2 días, más Design |
| 5. Plan anterior | 2 | 1 | por código, el texto no viaja | −0,001 USD | 0,5 días |
| Ninguno de los cinco | 3 | 0 | n/a | n/a | n/a |

Base: el redactor cuesta hoy 0,0793 USD por plan (media de M3, Sonnet 5.5). Con los cinco, el coste queda casi igual:
lo que el punto 3 añade de salida lo ahorra el punto 4. No hay segundo modelo.

**Una corrección al punto 5, comprobada en el código:** al seguimiento y al replanteamiento NO les llega hoy el texto
del plan anterior.
- `planAnteriorParaIA` (`web/lib/engine/replanteamiento.ts`) solo manda los títulos de las etapas y las tareas con su
  estado y la nota de la persona.
- Lo que sí viaja es el **texto de cada tarea**, que es una frase del plan anterior. Por ahí se arrastró «la feria
  local de agosto».
- El punto 5 queda como «tampoco el texto de las tareas».

## 1. «Material»: nombre neutro y filtro en el código

**Qué cambia:**
- **El payload.** Hoy el payload del redactor llama a los nodos `material_principal` y `material_de_apoyo`, y el
  prompt (`SYSTEM_PLAN`, en `engine/prototipo_motor.py`, sincronizado a la web) dice «material» en cada regla. El
  redactor lo copia como si fuera una fuente.
- **El nombre nuevo.** Pasa a ser un nombre que no suena a fuente: `temas_del_recorrido` y `temas_vecinos`. El prompt
  dice expresamente que la persona nunca ve esa lista.
- **El filtro.** En `finalizarPlan`, un filtro determinista sobre las frases que citan el payload como fuente: un
  sujeto de fuente («el material», «este contenido», «el método base», «los temas de este plan»…) seguido de un verbo
  de fuente («enseña», «dice», «recomienda», «indica», «no cubre»…).
- **Qué hace el filtro con cada frase.** «El material enseña que X» se reescribe como «X»; la que solo habla de la
  fuente («El material de este plan no cubre…») se quita.
- **En los once idiomas**, con una lista por idioma, como la de `validacionClientes.ts`.
- **La guarda.** El patrón entra a la guarda única de procedencia (`web/lib/procedencia.test.ts`) y a
  `REGLA_SIN_FUENTES`.

**Lo que quitaría:** M3A-f003-3 («El material de este plan no cubre seguridad informática en detalle») y M3A-f015-1
(«El material enseña que la seguridad funciona cuando la gente participa»).

**Riesgos:**
- **Falsos positivos con el material físico:** en un taller de macetas, «el material se agrieta» es un dato real. Por
  eso el filtro exige el verbo de fuente, y lleva casos reales en la prueba.
- **Otro sustantivo:** la IA podría citar otro («la guía dice…»). La lista se amplía con lo que aparezca, y la guarda
  lo vigila.

**Coste por plan:** 0. **Esfuerzo:** 0,5 a 1 día, con prueba en rojo en los once idiomas.

## 2. Números por código: las cifras llegan calculadas y etiquetadas

**Qué cambia:**
- **Hoy.** Las cifras de la persona le llegan al redactor dentro de la prosa del perfil y del contexto
  («Vendo unas 12 macetas al mes por Instagram»), y la IA deduce qué son. `numeros_proyecto` (con su `texto_original`)
  solo se usa después, para el aviso de números huérfanos.
- **Un bloque nuevo en el payload,** `numeros_de_la_persona`. Una fila por cifra:
  - valor y unidad;
  - **qué es** y **qué no es**, en texto llano armado por código;
  - de qué respuesta sale.

  Ejemplos:
  - «12 macetas al mes: lo que vende por Instagram. No es su venta total.»
  - «130 por maceta: costo con su hora incluida, igual para los dos tamaños. No es solo materiales; no distingue
    tamaños.»
  - «Precio en la tienda: no lo dio.»
- **Para el «qué no es», el intérprete guarda el alcance de cada número** (canal, tamaño, período, si incluye el
  tiempo de la persona). Ya lo hace en parte desde c6e51feec, con el costo que incluye tiempo. No hace falta
  migración: es el mismo JSON.
- **Lo que ya calcula el código entra hecho:**
  - `calculadora.ts`: margen y punto de equilibrio, con su estado («calculado» o «pendiente: falta X»);
  - la realidad del cronograma: «de 5 anotaciones, 3 tarde, 1 antes, 1 a tiempo».
- **La regla del redactor** pasa a ser una sola: «Las cifras son las del bloque; no deduzcas ni combines otras».

**Lo que quitaría:**
- las 12 macetas tratadas como total: M2A-f006-1, M2B-f002-2, M3A-f014-1;
- «tus cinco anotaciones tomaron más de lo previsto»: M3A-f012-1;
- el 130 leído mal: M3A-f003-1 «ahí se esconde un gasto»; M2A-f007-1 y M2B-f012-1 «chicas y medianas llevan distinto
  material»; M3A-f002-1 «no cuestan lo mismo».

**Ayudaría en** M3A-f003-2, M3A-f007-1 y M3A-f007-2 (canales que «no pagan lo mismo»), porque el bloque diría
«precio en la tienda: no lo dio». Esos los cierra el punto 3.

**Riesgos:**
- Un alcance mal etiquetado por el intérprete llega al plan con autoridad de dato. Por eso cada fila lleva la frase
  textual de la persona, y la prueba usa los casos reales.
- Más «no lo dio» puede volver el plan más preguntón. Es lo que el fundador ya decidió para los datos del negocio
  (bfbd1fddc).

**Coste por plan:** unos 400 tokens de entrada, +0,001 USD; en el intérprete, unos campos más por número detectado
(Haiku, despreciable). **Esfuerzo:** 2 a 3 días (intérprete, bloque, regla, pruebas en rojo con los cuatro casos).

## 3. Citar o callar: cada afirmación sobre el negocio lleva su respaldo

**Qué cambia:**
- **El redactor recibe numeradas las respuestas de la persona** (R1, R2… del hilo de la memoria y de la sesión, hasta
  ese momento) y los temas con su id.
- **Toda frase que afirme algo del negocio o de la situación de la persona termina con su respaldo:**
  - `⟦R7⟧`: una respuesta suya;
  - `⟦N:node_id⟧`: lo que enseña un tema.
- **Si no tiene respaldo, la escribe como pregunta**, con `⟦?⟧`.
- **Puede dejar una pregunta de reserva,** `⟦R7|¿…?⟧`: si la referencia no vale, el código usa esa pregunta en lugar
  de inventar una.
- **El código, en `finalizarPlan`, sin un segundo modelo:**
  - valida que cada R exista y que cada N sea del material entregado;
  - exige que las cifras de la frase estén en la respuesta citada o en el bloque del punto 2, y que la frase comparta
    al menos una palabra con contenido con la respuesta citada (comprobación barata, declarada como heurística);
  - quita la frase o la cambia por su pregunta de reserva cuando la referencia no vale;
  - quita las marcas antes de guardar y antes de cada trozo del streaming.
- **Las frases que no son afirmación** (las acciones en imperativo: «anota», «pregúntale a tres clientes») no necesitan
  marca. Las afirmaciones sin marca fuera de los pasos se quitan.

**Lo que quitaría** (hechos del negocio que nadie dio):
- «la tienda y Instagram no pagan lo mismo» y el margen «distinto en la tienda, en Instagram y en la feria»:
  M3A-f003-2, M3A-f007-1, M3A-f007-2;
- «quienes siguieron comprando ya te conocían»: M3A-f017-1;
- «el lote puede dejarte piezas paradas»: M3A-f014-2;
- «hecho a mano»: M2B-f009-1;
- «esa claridad solo existe en tu cabeza»: M2A-f012-1, M2B-f004-1;
- el cemento y el polvo sin protección: M1A-f003-2, M1A-f003-3, M1B-f009-1;
- los empleados que tocarán el canal de ventas: M1A-f004-4, M1B-f005-1, M1B-f005-2;
- «empiezan a surgir cuestiones de convivencia»: M1A-f004-3;
- «hoy no hay escrito qué se espera de cada uno»: M1A-f004-1;
- perder Instagram es perder pedidos y contactos: M1A-f014-1;
- «Si Instagram pesa mucho, eso confirma…»: M2A-f006-3.

Además, dos lecturas al revés de lo que dijo la persona: «tu mayor riesgo declarado es Instagram» (M1A-f003-1) y «aún
no has nombrado un riesgo concreto» (M2B-f002-1). En estas dos, el código solo comprueba que la cita exista: si la IA
cita la respuesta correcta pero la lee al revés, pasa. Las quita mejor el punto 4, porque están en la introducción.

**Riesgos:**
- **El código comprueba que el respaldo exista, no que respalde.** Una cita a una respuesta que no dice eso pasa si
  comparte una palabra. Es el límite de no usar un segundo modelo.
- **La IA puede no cumplir el protocolo de marcas.** Se vería en el evento de frases quitadas; si pasa del umbral, el
  plan sale igual, con aviso en el registro.
- **Marcas que se cuelan a la pantalla en el streaming en vivo.** Hay que limpiarlas por trozos, con prueba propia.
- **Un plan más corto y más genérico** si la IA calla mucho: «callar» también quita lo bueno que no sabe citar.
- **Un texto más entrecortado.**
- **Alcance:** primero, el redactor de planes (núcleo, mundo, seguimiento, replanteo). La Claridad no se ha medido.

**Coste por plan:** el índice de respuestas suma unos 300 a 600 tokens de entrada (las respuestas ya viajan en el
contexto; solo se numeran) y las marcas, un 10 a 15 % de salida: +0,004 a 0,006 USD. **Esfuerzo:** 4 a 6 días
(protocolo en el prompt, validador, limpieza en streaming, preguntas de reserva, pruebas en rojo con los casos reales
de arriba).

## 4. Menos prosa de enlace

**Qué cambia:** la estructura del plan en `SYSTEM_PLAN` y su lectura en `planParser.ts`.
- **La introducción del plan** deja de ser prosa libre: son dos frases como mucho, con lo que la persona contó (con su
  respaldo, punto 3) y lo que el plan va a hacer.
- **Cada etapa** pierde el párrafo narrativo. Queda:
  - el título;
  - una línea de **por qué**, que dice qué enseña el tema (con su `⟦N:…⟧`) o qué contó la persona (con su `⟦R…⟧`);
  - los pasos, el entregable y la primera acción.
- **Los pasos son acciones.** Las colas causales sin respaldo («…, porque no cuestan lo mismo», «…, que además suele
  cuidar el ritmo», «eso confirma…») se quitan por código: la cláusula tras «porque», «así que», «ya que» o «eso
  confirma» sin marca de respaldo.
- **Se quitan los cierres de etapa** del tipo «Esta etapa es la que hace que…».

**Lo que quitaría** (las causas y los resultados prometidos en las bisagras):
- «suele cuidar el ritmo de la producción», «Predicar con el ejemplo quita el aire de reproche», «sin que te quite
  tiempo»: M2A-f008-1, M2A-f008-2, M2A-f008-3, M2B-f015-1, M2B-f015-2, M2B-f015-3;
- «se integra en cada etapa sin sumar más trabajo»: M1B-f010-1;
- «las quejas llegan porque lo aceptable vive solo en tu cabeza», «el cuidado de cada pieza es lo que sostiene ese
  precio»: M2A-f003-1, M2A-f003-2, M2B-f013-1, M2B-f013-2;
- «por eso tus lotes no salen parejos»: M3A-f016-1;
- «Este es el paso que más te ayuda a dejar de apagar incendios», «Quien va bien y nunca lo oye…», «Contratar con
  método evita repetir lo que hoy te cuesta»: M3A-f001-1, M3A-f001-2, M3A-f001-3;
- «Un puesto bien definido te quita de encima el trabajo»: M1A-f004-2;
- «lo más barato y rápido es observar y escuchar»: M2B-f005-1;
- «tu tiempo es el recurso más escaso»: M3A-f011-1.

Además, 20 de los hallazgos de los puntos 2, 3 y 5 viven en la introducción o en la prosa de etapa (marcados «y 4» en
el anexo). Al no escribirse esa prosa, desaparecen también.

**Riesgos:**
- **Pierde calidez y motivo.** El párrafo de cada etapa es donde el plan le habla a la persona; la voz canónica del
  BANCO lo pide. La línea de por qué tiene que conservar el motivo, pero con respaldo.
- **La IA puede mover las mismas afirmaciones a los pasos.** El punto 3 y el corte de colas causales lo cubren.
- **Pantalla y documentos:** la tarjeta, el Expediente y el PDF leen las secciones del plan, y el canon visual de
  Design puede apoyarse en el párrafo de etapa. Hay que coordinarlo con Design antes de cambiar el formato.

**Coste por plan:** la prosa narrativa es el 18 % del texto; quitarla y poner una línea por etapa baja la salida un 12
a 15 %, −0,003 a 0,005 USD. **Esfuerzo:** 1 a 2 días (prompt, parser, corte de colas, pruebas), más la revisión de
Design.

## 5. Plan anterior: solo las etapas y su estado

**Qué cambia:**
- **Lo que viaja hoy:** título de cada etapa y cada tarea con su texto, su estado y la nota de la persona.
- **Lo que viajaría:** por etapa, el título, cuántas tareas hay en cada estado y los temas que trabajó (ids, los que
  ya guarda la migración 037), más las **notas de la persona**, que sí son dato suyo.
- **Lo que deja de viajar:** el texto de las tareas pendientes. Las que la persona marcó como hechas, en proceso o que
  no aplican, viajan como «tarea N: hecha», sin su frase.
- **La regla 8-ter del prompt** se ajusta a esa forma.

**Lo que quitaría:** «la feria local de agosto», M2A-f007-2 y M3A-f003-4: era una tarea del plan anterior, inventada
allí, que el seguimiento volvió a dar por cierta.

**Riesgos:**
- **El seguimiento pierde la textura de lo pendiente** y podría repetir o contradecir una tarea que no ve. Por eso
  recibe los temas de cada etapa y el conteo de estados.
- **Queda otro camino:** la persona repite en una respuesta la lista del plan (en el vuelo, el guion de la persona lo
  hace), y eso entra como dato suyo. Se puede anotar en el contexto como «repite el plan» si se quiere cerrar también.

**Coste por plan:** menos entrada, −0,001 USD. **Esfuerzo:** 0,5 días.

## Lo que ninguno de los cinco quita

Tres contrarios de **enseñanza del nodo** dentro de los pasos. La IA aplica el tema al revés:
- «busca un segundo proveedor» como forma de evitar, cuando el tema lo llama reducir: M2A-f006-2;
- «llama a las referencias que ella misma te facilite», cuando el tema dice que las eliges tú: M2A-f012-2 y
  M2B-f004-2.

El punto 3 no lo ve, porque la cita al tema existe y es la correcta. Una idea para después, no propuesta aquí: que los
pasos salgan de los pasos del tema adaptados (no reescritos) y que el código compare cada paso con su origen.

## Orden sugerido y cómo medir después

1. **Puntos 1 y 5:** baratos, por código y sin riesgo de calidad.
2. **Punto 4:** con Design, porque toca el formato.
3. **Punto 2:** toca el intérprete.
4. **Punto 3:** el más grande; se apoya en el 2 y en el 4.

Después, una sola medición con la misma regla de cierre (acta, fila 17: dos jueces, 0 contrarios, como mucho 2
invenciones, 0 procedencias) y el mismo camino de producción. Costó 9,29 USD en M3.

## Anexo: los 70 hallazgos sostenidos de las tres mediciones

«Dónde» es el lugar del plan. «Lo quitaría» es el punto principal; entre paréntesis, otro punto que también lo quita.

| Id | Plan | Clase | Dónde | Afirmación | Lo quitaría |
|---|---|---|---|---|---|
| M1A-f002-1 | deb138a3 quality | invencion | prosa de etapa | «y ya decidiste empezar esta semana» | ya resuelto (contexto y reglas, 0 en las dos siguientes) |
| M1A-f002-2 | deb138a3 quality | invencion | prosa de etapa | «El proveedor nuevo baja el cemento un veinte por ciento y todavía no lo metes en la cuenta.» | ya resuelto (contexto y reglas, 0 en las dos siguientes) |
| M1A-f003-1 | ff010188 risk_management | contrario | introducción | «Tu mayor riesgo declarado es proteger la cuenta de Instagram» | punto 3 (y 4) |
| M1A-f003-2 | ff010188 risk_management | invencion | introducción | «trabajar sin protección con cemento y polvo» | punto 3 (y 4) |
| M1A-f003-3 | ff010188 risk_management | invencion | paso | «Marca los que minimizaste porque no quieres enfrentarlos, por ejemplo el respaldo de tus contactos o el cem…» | punto 3 |
| M1A-f004-1 | 8b7764c4 primer_equipo | invencion | prosa de etapa | «Hoy no hay escrito qué se espera de cada uno» | punto 3 (y 4) |
| M1A-f004-2 | 8b7764c4 primer_equipo | invencion | prosa de etapa | «Un puesto bien definido te quita de encima el trabajo que terminas haciendo tú.» | punto 4 |
| M1A-f004-3 | 8b7764c4 primer_equipo | invencion | prosa de etapa | «Con dos personas nuevas en el taller empiezan a surgir cuestiones de convivencia.» | punto 3 (y 4) |
| M1A-f004-4 | 8b7764c4 primer_equipo | invencion | prosa de etapa | «tus empleados van a tocar el canal de ventas» | punto 3 (y 4) |
| M1A-f006-1 | ee6de956 core | contrario | paso | «Resta lo segundo de lo primero para ver tu velocidad real de crecimiento.» | ya resuelto (contexto y reglas, 0 en las dos siguientes) |
| M1A-f014-1 | f14f36e7 seguridad_digital | invencion | prosa de etapa | «o si pierdes Instagram, pierdes pedidos y contactos, y hoy no tienes forma de escribirle a tus compradores …» | punto 3 (y 4) |
| M1A-f015-1 | 265e4486 quality | invencion | título de etapa | «Etapa 6: Anota qué lleva cada kit de huerto» | ya resuelto (defecto del guion de la 1.ª medición) |
| M1A-f015-2 | 265e4486 quality | invencion | prosa de etapa | «Te preocupa que el sustrato de tus kits salga dispar, y no tienes escrito qué lleva cada uno.» | ya resuelto (defecto del guion de la 1.ª medición) |
| M1A-f016-1 | c73e86f8 core | contrario | introducción | «Los números de costo, canal y punto de equilibrio del plan anterior siguen vigentes y no se repiten aquí.» | ya resuelto (contexto y reglas, 0 en las dos siguientes) |
| M1B-f004-1 | c73e86f8 core | contrario | introducción | «Los números de costo, canal y punto de equilibrio del plan anterior siguen vigentes y no se repiten aquí.» | ya resuelto (contexto y reglas, 0 en las dos siguientes) |
| M1B-f005-1 | 8b7764c4 primer_equipo | invencion | prosa de etapa | «tus empleados van a tocar el canal de ventas, y de ti depende que sepan cómo cuidarlo» | punto 3 (y 4) |
| M1B-f005-2 | 8b7764c4 primer_equipo | invencion | entregable / primera acción | «una regla clara de quién accede a las cuentas del taller» | punto 3 |
| M1B-f006-1 | 31ebf0ea core | invencion | paso | «El correo es lo primero porque con él se recuperan las demás cuentas.» | ya resuelto (contexto y reglas, 0 en las dos siguientes) |
| M1B-f008-1 | f14f36e7 seguridad_digital | invencion | paso | «porque quien controla tu correo puede recuperar todo lo demás» | ya resuelto (contexto y reglas, 0 en las dos siguientes) |
| M1B-f009-1 | ff010188 risk_management | invencion | introducción | «A eso se suman depender de un solo proveedor de resina, el defecto de burbujas entre lotes y trabajar sin p…» | punto 3 (y 4) |
| M1B-f010-1 | 85248377 health_safety | invencion | introducción | «se integra en cada etapa sin sumar más trabajo» | punto 4 |
| M1B-f012-1 | ee6de956 core | contrario | paso | «Resta lo segundo de lo primero para ver tu velocidad real de crecimiento.» | ya resuelto (contexto y reglas, 0 en las dos siguientes) |
| M1B-f013-1 | 265e4486 quality | invencion | título de etapa | «Etapa 6: Anota qué lleva cada kit de huerto» | ya resuelto (defecto del guion de la 1.ª medición) |
| M1B-f013-2 | 265e4486 quality | contrario | paso | «Fija una meta visible, por ejemplo cuántas piezas con defecto aceptas por cada lote» | ya resuelto (contexto y reglas, 0 en las dos siguientes) |
| M2A-f003-1 | 265e4486 quality | invencion | prosa de etapa | «Hoy las quejas llegan porque lo "aceptable" vive solo en tu cabeza.» | punto 4 |
| M2A-f003-2 | 265e4486 quality | invencion | introducción | «Ahora el cuidado de cada pieza es lo que sostiene ese precio.» | punto 4 |
| M2A-f004-1 | aad2749d core | contrario | «aún no cubre» | «validar con clientes reales (conversaciones, una primera versión sencilla de tu producto, pruebas con usuar…» | ya resuelto (frase fija, 0 en la última) |
| M2A-f006-1 | ff010188 risk_management | contrario | paso | «cuántas de tus 12 macetas al mes vendes por Instagram» | punto 2 |
| M2A-f006-2 | ff010188 risk_management | contrario | paso | «Considera primero si puedes evitarlo cambiando de rumbo. Ejemplo: si dependes de un solo proveedor, busca u…» | ninguno de los cinco |
| M2A-f006-3 | ff010188 risk_management | invencion | paso | «Si Instagram pesa mucho, eso confirma que conviene tener otra vía para llegar a tus clientes.» | punto 3 |
| M2A-f007-1 | 31ebf0ea core | invencion | prosa de etapa | «Chicas y medianas llevan distinto material y distinto tiempo» | punto 2 (y 4) |
| M2A-f007-2 | 31ebf0ea core | invencion | paso | «Anota si la feria local de agosto te sirve para probar el precio con gente que no te conoce.» | punto 5 |
| M2A-f008-1 | 85248377 health_safety | invencion | prosa de etapa | «Antes conviene mirar si el peligro se puede quitar o reducir en el origen, que además suele cuidar el ritmo…» | punto 4 |
| M2A-f008-2 | 85248377 health_safety | invencion | paso | «Predicar con el ejemplo quita el aire de reproche.» | punto 4 |
| M2A-f008-3 | 85248377 health_safety | invencion | prosa de etapa | «Esta etapa es la que hace que el cuidado dure sin que te quite tiempo.» | punto 4 |
| M2A-f012-1 | 8b7764c4 primer_equipo | invencion | prosa de etapa | «Hoy esa claridad solo existe en tu cabeza, y por eso acabas haciendo el trabajo tú.» | punto 3 (y 4) |
| M2A-f012-2 | 8b7764c4 primer_equipo | contrario | paso | «llama a las referencias que ella misma te facilite» | ninguno de los cinco |
| M2A-f013-1 | 9909f451 core | contrario | «aún no cubre» | «validar con clientes reales (conversaciones, una primera versión sencilla de tu producto, pruebas con usuar…» | ya resuelto (frase fija, 0 en la última) |
| M2B-f002-1 | ff010188 risk_management | contrario | introducción | «aunque todavía no hayas nombrado un riesgo concreto sobre ella» | punto 3 (y 4) |
| M2B-f002-2 | ff010188 risk_management | contrario | paso | «cuántas de tus 12 macetas al mes vendes por Instagram» | punto 2 |
| M2B-f004-1 | 8b7764c4 primer_equipo | invencion | prosa de etapa | «Hoy esa claridad solo existe en tu cabeza, y por eso acabas haciendo el trabajo tú.» | punto 3 (y 4) |
| M2B-f004-2 | 8b7764c4 primer_equipo | contrario | paso | «llama a las referencias que ella misma te facilite» | ninguno de los cinco |
| M2B-f005-1 | ee6de956 core | invencion | prosa de etapa | «lo más barato y rápido es observar y escuchar a personas reales antes de tocar el producto» | punto 4 |
| M2B-f005-2 | ee6de956 core | contrario | «aún no cubre» | «validar con clientes reales (conversaciones, una primera versión sencilla de tu producto, pruebas con usuar…» | ya resuelto (frase fija, 0 en la última) |
| M2B-f009-1 | b4a01dea core | invencion | título | «Tu producto hecho a mano, pieza a pieza» | punto 3 |
| M2B-f010-1 | aad2749d core | contrario | «aún no cubre» | «validar con clientes reales (conversaciones, una primera versión sencilla de tu producto, pruebas con usuar…» | ya resuelto (frase fija, 0 en la última) |
| M2B-f012-1 | 31ebf0ea core | invencion | prosa de etapa | «Tu costo de 130 es un promedio. Chicas y medianas llevan distinto material y distinto tiempo» | punto 2 (y 4) |
| M2B-f013-1 | 265e4486 quality | invencion | introducción | «Ahora el cuidado de cada pieza es lo que sostiene ese precio.» | punto 4 |
| M2B-f013-2 | 265e4486 quality | invencion | prosa de etapa | «Hoy las quejas llegan porque lo "aceptable" vive solo en tu cabeza.» | punto 4 |
| M2B-f015-1 | 85248377 health_safety | invencion | prosa de etapa | «Antes conviene mirar si el peligro se puede quitar o reducir en el origen, que además suele cuidar el ritmo…» | punto 4 |
| M2B-f015-2 | 85248377 health_safety | invencion | prosa de etapa | «Esta etapa es la que hace que el cuidado dure sin que te quite tiempo.» | punto 4 |
| M2B-f015-3 | 85248377 health_safety | invencion | paso | «Predicar con el ejemplo quita el aire de reproche.» | punto 4 |
| M2B-f017-1 | 9909f451 core | contrario | «aún no cubre» | «Lo que este plan aún no cubre: validar con clientes reales (conversaciones, una primera versión sencilla de…» | ya resuelto (frase fija, 0 en la última) |
| M3A-f001-1 | 8b7764c4 primer_equipo | invencion | prosa de etapa | «Este es el paso que más te ayuda a dejar de apagar incendios.» | punto 4 |
| M3A-f001-2 | 8b7764c4 primer_equipo | invencion | prosa de etapa | «Quien va bien y nunca lo oye queda sin referencia de qué repetir.» | punto 4 |
| M3A-f001-3 | 8b7764c4 primer_equipo | invencion | prosa de etapa | «Con dos empleados ya sabes lo que cuesta acertar o fallar. Contratar con método evita repetir lo que hoy te…» | punto 4 |
| M3A-f002-1 | fb027af0 core | invencion | paso | «Haz el cálculo por separado para el tamaño chico y para el mediano, porque no cuestan lo mismo.» | punto 2 |
| M3A-f003-1 | 31ebf0ea core | invencion | prosa de etapa | «Si la cuenta de una tanda no coincide con ese 130, ahí se esconde un gasto que aún no estás viendo.» | punto 2 (y 4) |
| M3A-f003-2 | 31ebf0ea core | invencion | prosa de etapa | «la tienda de plantas y Instagram no pagan lo mismo» | punto 3 (y 4, 2) |
| M3A-f003-3 | 31ebf0ea core | procedencia | prosa de etapa | «El material de este plan no cubre seguridad informática en detalle» | punto 1 (y 4) |
| M3A-f003-4 | 31ebf0ea core | invencion | paso | «Anota si la feria local de agosto te sirve para probar el precio con gente que no te conoce» | punto 5 |
| M3A-f007-1 | aad2749d core | invencion | prosa de etapa | «porque la tienda y Instagram no te pagan lo mismo» | punto 3 (y 4, 2) |
| M3A-f007-2 | aad2749d core | invencion | sección de números | «lo que te queda de cada maceta después de ese costo, distinto en la tienda, en Instagram y en la feria» | punto 3 (y 2) |
| M3A-f011-1 | b4a01dea core | invencion | introducción | «así que tu tiempo es el recurso más escaso» | punto 4 |
| M3A-f012-1 | 0e481ad8 health_safety | contrario | introducción | «tus cinco anotaciones tomaron más de lo previsto» | punto 2 (y 4) |
| M3A-f014-1 | ff010188 risk_management | contrario | entregable / primera acción | «anota cuántas macetas de tus 12 al mes pasan por ese canal» | punto 2 |
| M3A-f014-2 | ff010188 risk_management | invencion | paso | «el lote te da descuento en materiales, pero puede dejarte piezas paradas» | punto 3 |
| M3A-f015-1 | 85248377 health_safety | procedencia | prosa de etapa | «El material enseña que la seguridad funciona cuando la gente participa, no cuando se le impone.» | punto 1 (y 4) |
| M3A-f016-1 | 265e4486 quality | invencion | prosa de etapa | «Sin un criterio claro, "burbujas" o "acabado irregular" significan algo distinto cada día, y por eso tus lo…» | punto 4 |
| M3A-f017-1 | c73e86f8 core | invencion | prosa de etapa | «Que no hayan bajado las ventas con gente que ya te conocía no prueba que el precio aguante con desconocidos.» | punto 3 (y 4) |
