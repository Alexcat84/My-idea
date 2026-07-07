_Plan inicial_

# Macetas de calcita con autenticación QR: de los experimentos técnicos a las primeras ventas reales

Tu proyecto ya tiene algo que muchas ideas no tienen: personas que lo vieron, lo tocaron y reaccionaron bien. El bloqueo real no es la demanda — es que los dos problemas técnicos que te frenan (burbujas en la resina y durabilidad del QR) están acoplados: si la resina falla, el QR falla con ella. Este plan parte de ese punto concreto y te da una ruta para resolver ambos de forma sistemática, medir qué funciona, y arrancar ventas reales sin esperar a tener todo perfecto.

---

## Etapa 1: Separa lo que sabes de lo que estás asumiendo

Antes de iterar técnica o salir a vender, necesitas saber exactamente qué está confirmado y qué es todavía una apuesta. Mezclar hechos con supuestos hace que tomes decisiones costosas basadas en cosas que aún no probaste.

**Pasos:**

1. Escribe dos columnas en una hoja: "Confirmado" y "Por validar". Empieza con estas preguntas: ¿Alguien fuera de tu círculo cercano pagaría por una maceta así? ¿El QR necesita ser permanente o solo legible al momento de la compra? ¿El valor del NFT es algo que el comprador entiende y quiere, o es algo que tú valoras más que él?
2. Revisa cuáles de tus supuestos son de bajo riesgo (por ejemplo, "la calcita rosa se ve bien en resina" — ya lo sabes) y cuáles podrían matar el proyecto si están equivocados (por ejemplo, "el comprador entiende y quiere el NFT como prueba de autenticidad").
3. Marca los tres supuestos más arriesgados. Esos son los que este plan va a atacar primero.
4. Para cada supuesto marcado, escribe una pregunta concreta que podrías responder con evidencia real, no con opinión tuya. Ejemplo: en vez de "creo que les gustará el NFT", escribe "¿cuántas de las personas que recibieron el prototipo escanearon el QR por iniciativa propia sin que yo se los pidiera?"

**Entregable:** Lista de supuestos separados en hechos confirmados e hipótesis sin probar, con los tres más críticos identificados.

**Esta semana:** Contacta a las personas que recibieron prototipos y pregúntales directamente: "¿Escaneaste el código QR? ¿Qué esperabas encontrar? ¿Te importaría tener un certificado digital de autenticidad?" Anota las respuestas exactas, no tu interpretación de ellas.

---

## Etapa 2: Ataca el bloqueo técnico con experimentos de una variable a la vez

Mencionaste algo importante durante la sesión: ya tienes un plan de experimentos sistemáticos variando una variable a la vez en la mezcla de resina. Ese enfoque es correcto y este plan lo estructura para que produzcas aprendizaje real en cada intento, no solo intentos fallidos sin registro.

El nudo técnico es que los defectos en la resina y la legibilidad del QR no son independientes: una resina con burbujas distorsiona la superficie donde va el QR, lo que hace al QR ilegible. Esto significa que no puedes resolver uno y luego el otro — necesitas encontrar la combinación que resuelva ambos al mismo tiempo o que evite que el defecto en uno se propague al otro.

**Pasos:**

1. Antes de cada experimento, escribe una tarjeta con estos cuatro campos: (a) la hipótesis concreta que vas a probar ("si reduzco la temperatura de vertido en X grados, las burbujas disminuyen sin afectar la superficie del QR"), (b) la única variable que vas a cambiar en este intento, (c) la métrica que vas a medir ("número de burbujas visibles a 10 cm" y "porcentaje de celdas del QR legibles con escáner estándar"), y (d) el umbral que defines como éxito antes de ejecutar, no después.
2. Documenta los resultados con fotos y el resultado del escaneo para cada intento. Sin registro, no hay aprendizaje acumulado — solo intuición que no escala.
3. Prueba primero los experimentos más baratos y rápidos: cambios en temperatura, tiempo de curado, técnica de vertido. Antes de invertir en métodos alternativos de grabado del QR (que son más costosos), confirma si el problema es la resina o es el método de marcado.
4. Para el QR específicamente: una vez que tengas una mezcla de resina estable, prueba al menos dos métodos de fijación del QR (grabado láser, incrustación de etiqueta resistente, impresión UV sobre capa sellada) y mide la legibilidad después de simular uso real: agua, roce, exposición a luz solar directa por 48 horas.
5. Define cuántos experimentos necesitas antes de tomar una decisión: si después de 5 intentos controlados con variables distintas ninguno cumple el umbral, eso es evidencia para considerar un cambio de método, no para seguir intentando lo mismo.

**Entregable:** Serie de tarjetas de experimento completadas con hipótesis, variable modificada, métricas medidas y resultado validado o invalidado para cada intento.

**Esta semana:** Produce tres muestras de resina cambiando solo una variable en cada una (elige la que creas más probable que cause las burbujas), escanea el QR en cada una con un teléfono estándar, y anota cuál pasa y cuál no. Eso ya es tu primera iteración documentada.

---

## Etapa 3: Construye el MVP más simple posible para probar el sistema completo

No necesitas que el producto esté perfecto para probar si el sistema QR-NFT genera valor real en el comprador. Puedes probar el concepto digital antes de resolver completamente la parte física, y puedes usar eso para informar qué tan importante es realmente el NFT para quien compra.

**Pasos:**

1. Crea una página simple (puede ser una página gratuita en Notion, Carrd o similar) que simule lo que el comprador vería al escanear el QR: nombre del material, origen de la calcita, número de pieza, imagen del producto. No necesitas blockchain real todavía — estás probando si el comprador encuentra valor en esa información, no si la tecnología funciona.
2. Imprime un QR que apunte a esa página y pégalo en una maceta existente (aunque tenga defectos de resina que no afecten la lectura del código).
3. Muestra ese prototipo funcional completo a tres personas que no te conocen directamente. Observa si escanean el QR por iniciativa propia, si leen la página completa, si hacen alguna pregunta sobre la autenticidad. No les expliques el sistema antes — observa la reacción genuina.
4. Al final de la interacción, pregunta: "Si compraras esta maceta a un precio que te parezca justo, ¿cuánto pagarías? ¿El certificado digital cambia ese número para ti?"
5. Registra qué funcionalidades reclaman o preguntan que no están ahí — eso te dice qué agregar. Lo que no reclaman, no lo construyas todavía.

Esta etapa también te permite probar algo crítico: si la persona entiende el concepto de NFT como autenticación sin que tú se lo expliques. Si necesitas explicarlo en detalle cada vez, eso es una señal de que la propuesta de valor necesita simplificarse en su presentación, no necesariamente abandonarse.

**Entregable:** Registro de tres interacciones con el prototipo completo (físico + QR + página), con observaciones de comportamiento real y precio mencionado espontáneamente por cada persona.

**Esta semana:** Crea la página de autenticación simulada (sin NFT real) con los datos de una sola maceta, genera el QR, y muéstraselo a una persona que no sea familiar ni amigo cercano. Anota si escaneó sola o esperó instrucciones.

---

## Etapa 4: Mide cuánto te cuesta realmente producir una maceta

No tienes los números de costo documentados. Esto importa ahora — no después de resolver la técnica — porque si no sabes cuánto cuesta cada unidad en materiales y tiempo real, no puedes saber si el precio que el comprador menciona en la etapa anterior es viable para ti.

**Pasos:**

1. En tu próxima sesión de producción, cronometra y anota cada etapa por separado: tiempo en la mina (extracción y selección de calcita), tiempo en el tumbler (procesamiento), tiempo de preparación de resina y vertido, tiempo de desmolde y acabado, tiempo de aplicación del QR.
2. Anota el costo en materiales para esa sesión: resina, molde (amortización si es reutilizable), calcita usada (aunque la extraigas tú, tiene un costo de tiempo y traslado), código QR (si tiene costo de impresión o grabado).
3. Divide el costo total de materiales entre el número de macetas producidas en esa sesión. Ese es tu costo por unidad en materiales.
4. Multiplica las horas totales trabajadas por el valor que le asignarías a tu tiempo (aunque sea un estimado, ponle un número). Divídelo entre las macetas producidas. Eso es el costo de tu tiempo por unidad.
5. Suma ambos. Ese es tu costo real por maceta. Compáralo con el precio que las personas mencionaron en la Etapa 3.

**Entregable:** Costo real documentado por unidad (materiales + tiempo estimado) para una sesión de producción real.

**Esta semana:** En tu próxima vez que trabajes en el proyecto, anota el tiempo de inicio y fin de cada etapa y lista todos los materiales que usas. No necesitas medirlo todo perfectamente — con un registro honesto de una sola sesión ya tienes una base real.

---

## Etapa 5: Decide si perseverar, ajustar o cambiar dirección con base en lo que aprendiste

Con los datos de las etapas anteriores —reacción real al sistema QR, resultados de los experimentos de resina, y costos documentados— ya tienes suficiente para tomar decisiones informadas en lugar de seguir operando por intuición.

**Pasos:**

1. Revisa los resultados de todas las etapas anteriores juntos. Pregúntate: ¿los experimentos de resina están mostrando progreso medible, o sigo obteniendo el mismo resultado con variables distintas? ¿Las personas que vieron el prototipo con QR entendieron el valor sin que lo explicaras? ¿El precio que mencionaron cubre tu costo real?
2. Si los experimentos de resina muestran progreso pero lento: sigue en esa dirección con más iteraciones, pero considera tomar un pedido con plazo real (3-4 semanas) para crear presión de validación — el dinero en la mano te dice algo que la opinión verbal no te dice.
3. Si las personas no entienden el sistema NFT sin explicación: evalúa simplificar la propuesta digital a "certificado de autenticidad en línea" en lugar de "NFT", sin cambiar la tecnología — el nombre puede estar creando fricción innecesaria.
4. Si el costo real por unidad es mayor al precio que las personas mencionan: necesitas saber si el problema es el precio (y hay que subirlo), el costo (y hay que bajar materiales o tiempo), o el segmento (y hay que buscar compradores que paguen más por un objeto con historia verificable).
5. Programa este análisis como una reunión contigo mismo cada tres semanas: trae los datos reales, compáralos con lo que esperabas, y toma una decisión explícita: seguir igual, cambiar algo específico, o cambiar la dirección completa.

**Entregable:** Una decisión documentada (seguir, ajustar o cambiar) con los datos que la respaldan, no solo la corazonada.

**Esta semana:** Anota en un papel cuál es el resultado que, si lo ves en tres semanas, te daría confianza para tomar el primer pedido pagado. Ese número o condición es tu criterio de éxito actual. Escríbelo antes de ver los resultados, no después.

---

## ¿Puede sostenerse tu idea? Los números en simple

Esta sección no puede darte cifras reales todavía porque no las tienes documentadas — y ese es exactamente el punto.

Lo que sí se sabe: produces todo tú solo, en cada etapa (extracción, procesamiento, vertido, acabado). Eso significa que el costo más importante de tu idea no es solo la resina o la calcita — es tu tiempo, y ese tiempo tiene un límite físico que define cuántas macetas puedes producir en una semana o un mes.

El número que necesitas descubrir en la Etapa 4 es ese costo real por unidad. Una vez que lo tengas, el análisis es simple: si el precio que un comprador desconocido está dispuesto a pagar supera tu costo real (materiales más tiempo), la idea puede sostenerse. Si no lo supera, tienes tres palancas: subir el precio, bajar el costo por unidad, o producir en mayor cantidad para que el costo de tiempo se distribuya.

La parte digital (el sistema QR y el certificado) puede justificar un precio más alto que una maceta sin autenticación — pero solo si el comprador lo entiende y lo valora sin que tú se lo expliques. Eso es lo que la Etapa 3 te va a decir.

El lunes que viene: produce tres muestras de resina cambiando solo una variable en cada una, cronometra el tiempo que te toma, y escanea el QR en cada muestra con un teléfono estándar. Con esos dos datos juntos ya empiezas a construir la base de todo lo demás.

---
_Este plan se alimento de 39 conceptos: 14 de tu recorrido conversado y 25 del vecindario relacionado del grafo._

## Lo que este plan aun no cubre

- si tu idea puede sostenerse economicamente (costos, precios, punto de equilibrio)

Para profundizar, continua la sesion: `python engine/prototipo_motor.py --continuar test27fd1313`