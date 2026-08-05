# PLAN MAESTRO — MUNDOS DE PROTECCIÓN SOBRE LO EXISTENTE
Campaña post-scheduler. Decisión del fundador (5 ago 2026): Riesgos, HSEQ y
Seguridad Digital se aplican SOBRE las actividades reales del proyecto, con
sus herramientas canónicas (que YA viven en el grafo) enlazadas visualmente:
"estos son tus riesgos y aquí sus mitigaciones". Los mundos de mejora y
expansión (Calidad, Internacionalización, Multiplica, Sostenibilidad) quedan
como están: contexto narrativo. Este documento es la spec; se ejecuta por
fases con plan-de-CC-primero, al cerrar la campaña del scheduler.

## 0. LAS DOS FAMILIAS (la doctrina que abre el banco)
- **Mejora/expansión**: construyen SU plan desde el contexto del negocio
  (estado_vivo + su entrevista). Como hoy. NO se tocan.
- **Protección** (risk_management, health_safety, seguridad_digital): su
  evaluación, su entrevista y su plan se aplican SOBRE el snapshot de las
  actividades vigentes. Su forma natural es "registro → detección →
  respuesta enlazada".

## 1. EL SNAPSHOT (insumo obligatorio, lectura pura)
Al abrir la entrevista/diagnóstico de un mundo de protección, el motor
arma el snapshot del proyecto: las actividades vigentes del NÚCLEO
(título, etapa, estado, fecha vigente, banda si existe) + el estado_vivo.
- Es LECTURA: nada se muda ni se copia; el núcleo jamás es escrito por un
  mundo. El snapshot viaja como contexto (tokens: barato) y muere con la
  sesión; lo único persistente son los ENLACES (§3).
- v1: núcleo-solo. Las actividades de OTROS mundos activos quedan como
  evolución declarada (un plan de Calidad también carga riesgos, pero
  cruzar mundos entre sí multiplica murallas: se decide con telemetría).
- La actualización natural: cada seguimiento del mundo de protección
  re-lee el snapshot fresco ("¿qué cambió en tu proyecto?").
- MURALLA NUEVA (pregunta 4 de la ficha, resuelta): un mundo de protección
  SIN plan de núcleo no puede evaluar sobre nada → su preview lo dice en
  persona y ofrece el camino ("primero tu plan; tu mundo de Riesgos se
  aplicará sobre él") en vez de generar un plan genérico: fallar honesto,
  jamás plantilla.

## 2. LAS HERRAMIENTAS CANÓNICAS (minadas del grafo real, verificado)
Cada mundo de protección tiene en sus nodos su herramienta madre; el plan
del mundo la INSTANCIA sobre las actividades reales:
- **Riesgos** (pack risk_management, ~55 nodos verificados): el REGISTRO DE
  RIESGOS como artefacto central (nodos "busca el riesgo antes de que te
  busque", "cuán probable y cuánto dolería" = probabilidad×impacto en
  palabras de persona, "cuatro caminos ante un riesgo" = evitar/mitigar/
  transferir/aceptar, "cuando el riesgo se vuelve realidad" = contingencia,
  "amenaza y oportunidad"). Instanciado: cada riesgo detectado apunta a su
  actividad (o al negocio entero), con su cuán-probable/cuánto-dolería, su
  camino elegido y su respuesta como actividad del plan del mundo.
- **HSEQ** (pack health_safety): el registro de peligros + la respuesta a
  incidentes (nodos "plan de acción de emergencia", "registro y reporte de
  lesiones", "investigación de incidentes", "aprendizaje desde
  incidentes"). Instanciado sobre las actividades físicas/operativas del
  plan (las que tocan producción, personas, materiales).
- **Seguridad Digital** (pack seguridad_digital): el inventario de activos
  digitales + amenazas (nodos "plan de desastre y recuperación",
  "estrategia de gestión de riesgo/tolerancia", la advertencia canónica
  "la matriz de colores te engaña": el grafo ya trae el antídoto contra el
  teatro de matrices). Instanciado sobre las actividades que tocan datos,
  cuentas, pagos, presencia digital.
- REGLA DE HONESTIDAD HEREDADA DEL PROPIO GRAFO: el nodo "la matriz de
  colores te engaña" manda: la severidad se muestra en palabras y rangos
  ("probable y dolería mucho"), jamás como puntaje numérico teatral.

## 3. EL ENLACE (la única migración de la campaña)
`checklist_items.protege_item uuid NULL` (referencia a un ítem del núcleo;
NULL = sistémico, "el negocio entero") + `deteccion text NULL` (la
detección que originó la respuesta, en una frase: "depende de un solo
proveedor"). Nace al generarse el plan del mundo de protección (el motor
enlaza cada respuesta a su actividad detectada); jamás editable por PATCH
(estructura del plan, no percepción del usuario: mismo criterio que
espera_externa).

## 4. LAS VISTAS (la barra paralela del fundador, como lectura)
- **El carril de protección en el Gantt del núcleo**: toggle "Ver
  protección" que dibuja, bajo las barras del núcleo, las actividades
  enlazadas de los mundos de protección activos (etiquetadas con su mundo,
  solo-lectura, JAMÁS contando en las medidas del núcleo). Una fuente,
  muchas lecturas.
- **El chip en el detalle**: la tarea del núcleo protegida muestra
  "Protegida por: [respuesta] · [mundo]" con enlace al hub; la tarea del
  mundo muestra "Protege: [actividad del núcleo]" con su detección.
- **La vista del registro** en el hub del mundo: la herramienta canónica
  instanciada (el registro de riesgos/peligros/activos con sus enlaces),
  descargable como documento del espacio (.md/PDF, el patrón de T7).

## 5. EL SCHEDULER DE PROTECCIÓN (las anclas de precedencia)
El empaquetado del mundo de protección recibe las fechas vigentes de las
actividades protegidas como ANCLAS: una respuesta enlazada debe ENTREGARSE
ANTES de la fecha de lo que protege (asegurar el proveedor alterno antes
de la compra, no después). Regla: su fecha empaquetada = min(fecha normal
por capacidad, ancla − margen); si la capacidad no alcanza para llegar
antes del ancla, se DICE ("esta protección no llega antes de [actividad]:
muévela o acepta el riesgo"): jamás se miente la fecha. Las sistémicas
(protege_item NULL) se empaquetan normal. Los movimientos de fechas del
núcleo NO arrastran al mundo automáticamente (murallas): el seguimiento
del mundo detecta el desfase y lo re-ancla (se dice, no se hace a
espaldas).

## 6. LAS FASES (cada una con checkpoint, plan-de-CC-primero)
- **P0 Gobierno**: las dos familias + el enlace-jamás-fusión + la regla
  anti-matriz-teatral al BANCO §7.1; la ficha del backlog se promueve a
  campaña.
- **P1 El snapshot + la muralla**: el armador del snapshot (puro,
  testeado); las entrevistas/diagnósticos de los tres mundos lo reciben;
  la muralla del sin-plan-de-núcleo con su copy honesto. Sin migración.
- **P2 El enlace**: migración (protege_item + deteccion); el motor de plan
  de protección genera enlazado (prompt con salida estructurada:
  detección → actividad → respuesta); tests de que todo enlace apunta a un
  ítem real o a NULL declarado.
- **P3 El registro visible**: la vista de la herramienta canónica en el
  hub + su documento descargable (patrón T7).
- **P4 El carril y los chips**: el toggle del Gantt + los chips
  bidireccionales del detalle. La pieza más visual: par de gate dedicado.
- **P5 Las anclas**: el empaquetado de protección con precedencias y su
  aviso honesto de no-llego. Tests con aritmética a mano (el ancla que
  adelanta, la capacidad que no alcanza y se dice, la sistémica normal).
- **CIERRE**: vuelo del ciclo de protección completo (preview → snapshot
  → plan enlazado → registro → carril → anclas), gate, encargo de Design
  (el carril, el registro, los chips), tag.

## 7. LO QUE NO ENTRA (declarado)
Cruce mundo↔mundo (Calidad cargando riesgos): evolución con telemetría.
Re-anclaje automático ante movimientos del núcleo: jamás (se dice en el
seguimiento). Puntajes numéricos de riesgo: prohibidos por el propio
grafo. Los mundos de mejora: intactos.
