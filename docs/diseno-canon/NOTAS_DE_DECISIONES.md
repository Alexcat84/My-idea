# NOTAS DE DECISIONES, refresco del canon web de My Idea

Esta nota vale tanto como los frames: es lo que evita que la implementación
reinterprete el criterio de diseño. Aquí queda, pantalla por pantalla, qué se
refrescó de la app actual y por qué, qué se colapsó o se mandó a un segundo
nivel en móvil, y qué se recortó.

Alcance: este es el canon WEB (la app renderiza esta web en un teléfono). El
caparazón nativo de la APK es un encargo aparte y no se decide aquí.

## Convenciones de entrega (para el instrumento que lee esto)

- Un archivo `.html` autocontenido por pantalla, abre por doble clic sin
  servidor, sin CDNs ni frameworks. CSS y JS inline; tokens en `:root`; clases
  semánticas en español; indentación de 2 espacios; comentarios de sección.
- Cada archivo trae, al inicio, un comentario índice con TODOS sus
  `data-screen-label`. Los labels son únicos y disjuntos: ninguno es prefijo de
  otro (el sufijo de viewport queda al final, pero el estado va ANTES del
  viewport, no después, justo para no cruzar el par). Ejemplo:
  `Exploracion movil 380` y `Exploracion recorrido abierto movil 380` difieren
  desde el carácter 13, no al final.
- Todos los frames vienen en sus dos viewports: 1240 (desktop) y 380 (móvil).
  Ni un frame sin su 380.
- Texto de prueba largo y feo, el que genera el producto real (ítems de dos y
  tres líneas, títulos de idea que truncan). Cero ejemplos cortos y bonitos.
- Cero guiones largos o medios en el copy visible. La regla de color se respeta
  en todas partes: el azul piensa, el verde ejecuta, el ámbar es el guardián, y
  los mundos tienen su matiz propio.

## Regla transversal aplicada en todo el canon

El color es de SIGNIFICADO, no de decoración. Azul en exploración, planeación,
navegación y en cualquier acción que dispara al motor a pensar (incluido
"Contar qué pasó", que regenera el plan). Verde en la ejecución sobre el mundo
real: etapa 5, progreso, contadores, "esta semana", "marcar hecho", "marcar
como realizada". Ámbar solo en el guardián de datos y en las tardías (espejo,
nunca rojo, nunca regaño). Matiz de los mundos (`#3A9B8F`) en la identidad de un
mundo y en su hito de la Celebración. Los estados completados se distinguen
también por FORMA (check lleno, texto tachado), jamás solo por color.

## 01, Home / Mis ideas

- Refrescado: la cinta por idea ahora lleva su sello de fecha de última acción
  ("ayer 21:26", "hace 21 min", "hoy 08:14") junto al estado, tal como pide el
  producto de hoy.
- Refrescado: las ideas realizadas reposan al final de la lista con su
  distintivo Proyecto (chip verde) y su riel terminado en verde, separadas de
  las que siguen en curso.
- Móvil: el riel sube arriba del pie y el chip baja junto a la fecha, para que
  la fila respire a 380 sin encoger el título por debajo de dos líneas.

## 02, La Chispa

- Se conserva el momento sagrado: un solo campo que escucha, el micrófono como
  protagonista, cero plantillas. El borde azul del campo comunica "estoy
  escuchando".
- Texto de prueba: una idea dictada larga y desordenada (reparación de
  bicicletas a domicilio con dudas de cobro y de tiempo), no una frase pulida.

## 03, Claridad

- La frase reformulada es larga a propósito (tres líneas): así se ve si el
  bloque aguanta el ancho real.
- Distinción por forma: lo que YA tienes lleva punto lleno; lo que ASUMES lleva
  rombo. La columna de suposiciones cierra con la nota de que eso es justo lo
  que La Exploración pone a prueba.
- Móvil: las dos columnas se apilan (tienes, luego asumes), sin perder la nota.

## 04, La Exploracion

- Refrescado: el riel del árbol (la línea desciende y toca cada punto), con
  nodos "cubierto por lo que contaste" cuando el motor ya dio por respondido un
  nodo con lo que el usuario contó antes.
- Incluye la oferta honesta ("Con lo que me contaste puedo armar tu plan", con
  chips de potenciadores y dos salidas) y la tarjeta intermedia mientras el plan
  se escribe ("Escribiendo: Etapa 1...", con el nodo generándose en el riel).
- Móvil, replanteo: el riel no cabe como columna a 380, así que se manda a un
  segundo nivel como hoja inferior ("Recorrido"), y se entrega su estado abierto
  como frame propio (`Exploracion recorrido abierto movil 380`) para que el
  instrumento lo mire sin cruzar el par cerrado.

## 05, Tu Plan

- El plan es un DOCUMENTO, no una puerta: se lee, se descarga (.md), se navega
  hacia Manos a la Obra. No se puso ningún botón de "ajustar el plan" aquí:
  ajustar sin haber ejecutado es regenerar, y regenerar no es el producto (esa
  puerta duplicada se elimina del canon).
- Color con intención: "Tu primera acción" y cada bloque "esta semana" van en
  verde (ejecución); la estructura del plan, la procedencia y la navegación en
  azul.
- Refrescado: los potenciadores muestran "Activar · beta" con el precio de
  catálogo tachado ("3 creditos" tachado, "gratis en beta"). El candado se
  retiró.
- Recorte en móvil: se muestran las etapas 01 a 03 (01 abierta) en lugar de las
  cinco expandibles, y el rail derecho "construido con tu recorrido" se omite a
  380 por ser contexto secundario. Es una muestra fiel del patrón, no el volcado
  completo.

## 06, Manos a la Obra (la que más creció)

- Problema medido en la app actual: a 380 son cerca de 3.100px de scroll, con la
  columna lateral entera cayendo al fondo. Replanteo del canon:
  - El checklist se agrupa por etapas plegables (una abierta, el resto
    colapsadas con su contador). Los completados se distinguen por forma: check
    verde lleno y texto tachado.
  - En móvil, la columna lateral (análisis, cerrar como realizada, ritmo) NO se
    vuelca al fondo: se agrupa. La acción que dispara al motor ("Contar qué
    pasó") sube arriba con jerarquía; el resto queda como tarjetas plegables
    ("Ver análisis", "Ritmo del proyecto") y una sola tarjeta de cierre visible.
- Se decidió mostrar el estado ACTIVO (modo ya elegido, con progreso 7/30) en
  vez del estado recién llegado con el selector de modo. Razón: es el estado
  común, y demuestra el color de ejecución y la forma de completado. El selector
  de modo vive completo en la pantalla 10, y desde aquí se llega con "cambiar".
- "Contar qué pasó" es azul a propósito: es la única puerta al ritual y dispara
  al motor a repensar. "Marcar como realizada" es verde: es un acto de
  ejecución del usuario.

## 07, Potenciadores y Creditos

- Refrescado, lo central: el candado se retiró. Durante la beta cada potenciador
  es "Activar · beta", gratis, con su precio de catálogo tachado.
- La moneda se nombra créditos, jamás tokens. El centro de créditos muestra
  saldo y packs como ESTRUCTURA (10, 30, 75), con el precio en dinero por
  definir: son estructura, no precio.
- "Tus Números por dentro" trae el único uso del ámbar: el guardián de datos
  (GIGO), que recuerda que los números valen lo que valen las cifras que se
  metieron, y que no sustituyen contabilidad ni asesoría fiscal.

## 08, Mundos Activos

- Refrescado a la decisión nueva: un mundo es un SUBPROYECTO completo, no una
  versión recortada del viaje. Su sección trae su propio mini viaje (Exploración,
  Plan, Manos a la Obra con su contador), su checklist por etapas, su ritual
  ("Contar qué pasó", azul) y su cierre ("Marcar este mundo como completado",
  verde).
- Nuevo estado dibujado: el acta de cierre del mundo (el acta en miniatura). No
  exige el 100%, el porqué es opcional (campo de texto o voz), el espejo dice "X
  de N acciones de este mundo", y deja claro que cerrar el mundo no cierra la
  idea. Los pendientes quedan como testigos, no como deuda.
- El matiz de los mundos aparece en la identidad (el punto junto al nombre y el
  borde de la sección); la ejecución del mundo sigue en verde, igual que el core.

## 09, La Celebracion

- El momento emocional. El timeline vertical se dibuja solo y va de azul (el
  pensar del viaje: La Chispa, Claridad, Tu Plan) a verde (las acciones
  ejecutadas), con el hito de mundo en el matiz de los mundos ("Mundo activado:
  Calidad y Confianza").
- Dos variantes entregadas: con cumplimiento (modo fechas, con la fila a tiempo,
  adelantadas, tardías) y a mi ritmo (sin lenguaje de calendario, porque a quien
  eligió no tener fechas no se le juzga contra fechas). Ambas en sus dos
  viewports.
- El motivo del cierre (del acta soberana) aparece discreto bajo REALIZADA, en
  la voz del usuario.
- Accesibilidad: con `prefers-reduced-motion` el timeline abre directo a su
  estado final, sin animación de dibujado.
- Móvil: el timeline pasa de alternar lados a un solo lado (línea a la
  izquierda), que es lo único que aguanta 380 sin romper el texto largo.

## 10, Modo y Fechas

- Vista A, la elección: a mi ritmo (sin fechas ni presiones, con la honestidad
  "sin fechas no habrá recordatorios") o con fechas y recordatorios. El modo es
  reversible siempre.
- Vista B, el ritual de la línea base: fechas propuestas en lenguaje humano que
  se pueden ajustar, "mover esta etapa una semana" por etapa, y el interruptor
  de recordatorios (opt in, máximo uno al día, tono sin culpa, silencio para
  ideas cerradas).
- Se dice de frente: sin fechas no hay recordatorios, y si se replanifica una
  fecha, la original se preserva.

## 11, Analisis del Proyecto

- Refrescado con la fila NUEVA "Cumplimiento por mundo", que muestra la
  jerarquía honesta: un mundo puede quedar abierto aunque la idea se cierre
  ("Seguridad y Personas: 3 de 5, 60%, abierta"), y un mundo completado se
  marca como tal. Con el matiz de los mundos.
- La capa universal siempre está (duración, ritmo, racha, ciclos y mundos, más
  hitos). La capa de cumplimiento aparece solo en modo fechas: a tiempo en
  verde, adelantadas en azul, tardías en ámbar (espejo, jamás rojo).
- Variante entregada aparte: análisis solo universal (modo a mi ritmo), sin capa
  de cumplimiento, con la razón dicha en pantalla ("no se juzga contra fechas
  que decidiste no tener").
- Todo se lee de una sola fuente (analytics); nada se recalcula aparte.

## 12, El cierre honesto (NUEVO, diseñado desde cero)

- Cuando el motor decide que un camino no lleva a ningún lado, o que un mundo no
  es para esta idea, la pantalla JAMÁS queda muda: dice el porqué en palabras de
  persona y ofrece dos salidas. La confesión no es disculpa, es la credencial.
- Dos casos dibujados, cada uno en sus dos viewports:
  - Camino sin salida (core): "Por aquí no encuentro un plan que valga tu
    tiempo", con el porqué y dos salidas (volver a Manos a la Obra, explorar
    otro ángulo). Nada se pierde: recorrido y Claridad quedan guardados.
  - Mundo que no encaja: dice que no es para esta idea todavía, y devuelve la
    activación con su chip ("Activación devuelta · 3 creditos") y su nota (el
    usuario nunca pierde créditos por algo que no le sirvió). Cerrar el mundo no
    toca la idea.
- Es un momento de decisión del motor, por eso el acento es azul, no verde.

## 13, Explorar actividad (detalle de item, NUEVO, diseñado desde cero)

- Hoy cada acción del checklist es una fila con "marcar hecho" y nada más. Se
  diseñó abrir la actividad para ver y ajustar sus cosas DENTRO: su texto
  completo, su estado, su fecha (con "mover fecha" y la historia preservada), su
  nota libre editable, su historia de replanificaciones, y marcarla hecha.
- Cómo se abre: tocando la fila del checklist. Cómo se ve: en desktop es un
  cajón lateral sobre el checklist atenuado; en móvil, una hoja inferior. Cómo
  se cierra: con la X o tocando fuera (el velo).
- Se respeta el canon: registrar avance y notas es gratis, siempre; la tardía se
  muestra en ámbar como espejo, no como regaño; y al mover una fecha, la
  original se conserva (la historia no se reescribe).

## Lo que NO se hizo, a propósito

- No se calcó la app actual: donde era torpe (Manos a la Obra a 380), el canon
  lo resolvió mejor, y esa diferencia es el trabajo de implementación que sigue.
- No se cambiaron los cinco nombres de etapa ni los nombres de los mundos.
- No se rompió la regla del azul y el verde para que algo "se viera mejor".
- No se metió nada que dependa de la red: sin fuentes remotas ni imágenes
  externas, todo abre offline. La tipografía es un stack de sistema (Inter con
  respaldo), aceptable porque el instrumento abre por file y un enlace a Google
  Fonts no cargaría.
