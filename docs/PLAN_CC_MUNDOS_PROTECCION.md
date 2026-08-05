# Plan de ejecución (CC) — Campaña "MUNDOS DE PROTECCIÓN"

Contra la spec del fundador `docs/PLAN_MUNDOS_PROTECCION.md`. **Cero código
escrito.** Este documento es la entrega de calibración: qué verifiqué contra el
código real, cómo propongo ejecutar cada tanda, y las **dudas numeradas** que el
fundador y el auditor tienen que resolver antes de que se escriba nada.

Base verificada: **main `3fe83c0`** (cierre del scheduler, tag `web-v2.3.0-beta`).

---

## A. Lo que verifiqué contra el código (no contra el recuerdo)

Ocho anclajes. Tres cambian el plan de forma importante y están marcados.

1. **La muralla del sin-plan YA EXISTE.**
   `app/api/project/[id]/world/[pack]/start/route.ts:69-87` tiene el "candado de
   secuencia": busca el último plan `dominio='core'` con etiqueta
   `inicial|completo|seguimiento` y, si no hay, responde **409** con
   *"Primero genera el plan de tu idea. El mundo se construye sobre él."*
   `app/ui/PotenciaTuIdea.tsx:240` ya pinta esa frase.
   **CONSECUENCIA:** la muralla de §1 no es maquinaria nueva. Es **elevar el copy**
   al que la spec pide ("primero tu plan; tu mundo de Riesgos se aplicará sobre
   él") y decidir si ese copy es distinto para los mundos de protección. Reduce P1
   a la mitad.

2. **El plan se genera por STREAMING DE PROSA.**
   `app/api/session/[id]/plan/route.ts:91-109` usa `client.messages.stream()` con
   `SYSTEM_PLAN`; el usuario ve el texto aparecer. Después `finalizarPlan()` lo
   post-valida y `derivarChecklist()` (`lib/engine/checklist.ts:30`) parsea la
   prosa a ítems con un parser de markdown (`## Etapa N:`, `1. …`,
   `**Esta semana:**`).
   **CONSECUENCIA (la decisión central de la campaña):** la "salida estructurada
   detección → actividad → respuesta" **no puede salir de esa misma llamada** sin
   o bien ensuciar la prosa que el usuario está mirando, o bien meterle al parser
   una gramática nueva. Ver **Duda 1** y la propuesta del enlazador.

3. **El Gantt del núcleo es POR ETAPA, no por actividad.**
   `app/ui/GanttCumplimiento.tsx:189` recibe `porEtapa: EtapaGantt[]`, y
   `EtapaGantt` es `{etapa, baseInicio, baseFin, realInicio, realFin}`: una barra
   por etapa, no una por ítem.
   **CONSECUENCIA:** el "carril bajo las barras del núcleo" de §4 no puede alinear
   una respuesta con **su** actividad, porque la actividad no tiene barra propia.
   Ver **Duda 5**.

4. **El precedente de `protege_item` sin PATCH ya está probado dos veces.**
   `espera_externa` (F1) y `banda` viven en `checklist_items`; la ruta
   `app/api/project/[id]/checklist/route.ts` acepta `banda` en el PATCH y **no**
   `espera_externa`, exactamente por el criterio que la spec §3 invoca. Copiar ese
   patrón para `protege_item`/`deteccion` es mecánico y sin riesgo.

5. **La estimación corre en TODO plan nuevo por ruta única.**
   `app/api/session/[id]/plan/route.ts:305` (F1) estima antes de insertar el
   checklist, sin mirar el dominio. **Los planes de protección nacerán con banda
   y `espera_externa` sin tocar nada**, y el empaquetado de §5 compone sobre F2-F4.
   El vuelo ya custodia que el replan nazca estimado.

6. **El tamaño del snapshot es barato, con una salvedad.**
   Un plan real del dossier del auditor tiene **5 etapas y 31 ítems**. A ~15-20
   tokens por actividad (título + etapa + estado + fecha + banda) son **~600
   tokens**. La salvedad: "vigentes" no está definido y con varios ciclos el
   checklist acumula (3 ciclos ≈ 90 ítems). Ver **Duda 3**.

7. **El diagnóstico del preview es una llamada aparte, con su presupuesto.**
   `lib/engine/diagnosticoMundo.ts`: `materialDiagnostico()` arma el material
   (etiquetas de árbol + `perfilSesion`) y `PRESUPUESTO_DIAGNOSTICO_USD = 0.1`,
   con **ley de calidad plena (Sonnet siempre, jamás degradar)**. Meter el
   snapshot ahí es añadir un campo al material: encaja sin cirugía.

8. **El armador de la entrevista de mundo entra por `world/[pack]/start`.**
   Nace la sesión con `dominio=pack` y `estadoInicial()`; el contexto de la
   entrevista viaja en el estado del recorrido. El snapshot tiene que engancharse
   aquí para que llegue a los turnos, no solo al diagnóstico.

---

## B0. Estado final (cierre de contenido, ago 2026)

**TODAS las tandas ejecutadas y en producción**, cada una auditada y con visto:
P0+P1 (`ca67af4`, con la corrección del snapshot ilegible que falla honesto) →
P2 el enlace (`2c8fac5`; migración 034) → P2b la pregunta anclada (`c818d06`) →
P3 el registro completo (`d0ebf48`; migración 035, el camino como dato) →
P4 carril y chips (`6cdb68f`) → P5 anclas (`39f0c3f`). El **cierre** (vuelo 2P +
doctrina al BANCO + encargo Design + este estado) queda en staging esperando la
corrida única del fundador y su "visto, mergea y etiqueta" (tag propuesto:
`web-v2.4.0-beta`). Instrucciones de corrida: PENDIENTES §3.

## B. Tandas propuestas (el plan original, ejecutado)

Sigo el orden de la spec §6 (P0..P5 + cierre). Cambios respecto de ella,
declarados: **P1 encoge** (la muralla existe) y **P2 crece** (el enlazador es la
pieza dura). Cada tanda cierra con checkpoint (tsc + suite + lint + build) y
merge solo con visto.

### P0 — Gobierno (sin código de producto)
- BANCO §7.1: **las dos familias** (mejora/expansión vs protección), el
  **enlace jamás fusión** (un mundo nunca escribe el núcleo) y la **regla
  anti-matriz-teatral**, citando que el antídoto lo trae el propio grafo.
- `PENDIENTES`: la ficha ya está promovida y apunta a la spec (hecho, `4af224e`).
- Entregable: dos ediciones de doc. Sin riesgo.

### P1 — El snapshot + la muralla (sin migración)
- **`lib/engine/snapshotProyecto.ts`** puro y testeado: lee las actividades
  vigentes del núcleo y devuelve `{actividades:[{id, titulo, etapa, estado,
  fecha_base, banda}], estado_vivo}`. **Lectura pura**: no escribe nada, y un
  test de contrato lo prueba (ninguna llamada de escritura en el módulo).
- Se enchufa en dos sitios: el **material del diagnóstico** (ancla 7) y el
  **arranque de la entrevista** del mundo (ancla 8), **solo para los tres mundos
  de protección** (una constante `MUNDOS_PROTECCION` en `lib/espacios.ts`, que ya
  es la fuente única de los espacios).
- **La muralla:** subir el copy del 409 al que pide la spec y decidir si cambia
  por familia (**Duda 2**).
- Tests: el armador con un proyecto sembrado; que un mundo de mejora **no** reciba
  snapshot; el corte de "vigentes" (**Duda 3**).

### P2 — El enlace (la única migración) — **la tanda dura**
- **Migración 034**: `checklist_items.protege_item uuid NULL REFERENCES
  checklist_items(id)` + `deteccion text NULL`, con su bloque en el verificador y
  su entrada en `dbContract` si lleva CHECK. **`ON DELETE SET NULL`** para que
  borrar un ítem del núcleo no cascade a las respuestas del mundo (**Duda 4**).
- **El enlazador** (ver **Duda 1** para la elección de forma): una llamada de
  salida estructurada **después** del plan, hermana de la estimación de F1, que
  recibe `(plan del mundo recién escrito, snapshot del núcleo)` y devuelve
  `[{item_orden, deteccion, protege_item|null}]`. Se persiste en el mismo insert
  del checklist. **Si falla: todos los enlaces null y el plan no se bloquea**, con
  síntoma en `sessions.decisiones` (doctrina de F1, ya probada).
- Tests: todo enlace apunta a un ítem real del núcleo **o** es NULL declarado;
  ningún enlace cruza a otro mundo; el fallback; el PATCH que **rechaza**
  `protege_item`.

### P3 — El registro visible
- La herramienta canónica instanciada en el hub del mundo: el registro con sus
  filas (detección · severidad en palabras · camino elegido · respuesta enlazada).
- Documento descargable del espacio (.md/PDF) con el patrón de T7
  (`particionDocumentos` ya separa global y del espacio).
- Test de voz: **cero puntajes numéricos** en el registro (mismo patrón que el
  test que vigila que el copy del colchón no derive al reproche).

### P4 — El carril y los chips

**Restricción de diseño del fundador (ago 2026, incorporada antes de arrancar):**
el carril de protección nace **DENTRO de la jerarquía visual de fase** del Gantt
(anidado bajo la banda de su etapa), para que la calibración de fases visuales
que hará CD (ficha en PENDIENTES §2) lo vista sin deshacerlo.
- Los **chips bidireccionales** en el detalle: baratos y de alto valor, con los
  datos que P2 ya persistió.
- El **carril del Gantt**: depende de **Duda 5**. Si la respuesta es "bajo la
  barra de su etapa", es una fila extra en `GanttCumplimiento` y no toca el
  cálculo del núcleo. Garantía irrenunciable: el carril **no entra en ninguna
  medida** (avance, cumplimiento, conteos). Lo prueba un test de no-doble-conteo,
  igual que el de la campaña Espacios.
- Par de gate dedicado.

### P5 — Las anclas
- `empaquetarFechas` gana **anclas de precedencia**: una respuesta enlazada
  entrega **antes** de lo que protege. Fórmula de la spec: `min(fecha normal por
  capacidad, ancla − margen)`; el **margen** no está definido (**Duda 6**).
- **El aviso de no-llego**, que es la regla que más me importa: si la capacidad no
  alcanza, **se dice** y **jamás se miente la fecha**. Propongo que el resultado
  del empaquetado lleve un campo declarado (`noLlegaAlAncla: true`) y que la
  pantalla lo diga en persona; el silencio aquí sería exactamente la degradación
  callada que el BANCO §9 prohíbe.
- Las sistémicas (`protege_item NULL`) se empaquetan normal.
- Tests con **aritmética a mano** (regla de la casa): el ancla que adelanta, la
  capacidad que no alcanza y se dice, la sistémica normal.

### CIERRE
Vuelo del ciclo completo (preview → snapshot → plan enlazado → registro → carril
→ anclas), gate, encargo a Design (carril, registro, chips), doctrina al BANCO y
tag menor.

---

## C. Dudas numeradas — **TODAS ADJUDICADAS** (fundador + auditor, 5 ago 2026)

Veredicto de cada una, arriba de su enunciado original. Lo adjudicado manda.

1. **Enlazador = (a) segunda llamada**, hermana de la estimación de F1, con su
   fallback declarado. **(c) rechazada con nombre:** la coincidencia de texto es
   adivinación.
2. **Copy de muralla ÚNICO e interpolado:** *"Primero genera el plan de tu idea:
   tu mundo de {nombre} se construirá sobre él."*
3. **Vigentes = el ciclo vigente del núcleo, INCLUYENDO las hechas** (con su
   estado marcado en el snapshot) y **excluyendo las retiradas**.
4. **Mi propuesta aprobada entera** (`SET NULL`; `no_aplica` no rompe el enlace)
   **+ regla anti-silencio:** el chip de la respuesta renderiza **siempre** su
   detección, y si lo protegido se retiró, **lo dice** ("la actividad que
   protegía fue retirada").
5. **Carril = (a) bajo la barra de su etapa.** El Gantt no se reconstruye; la
   precisión ítem a ítem vive en los chips y en el registro. Revocable por el ojo
   del fundador en el gate de P4.
6. **`MARGEN_ANCLA_SEMANAS = 1`**, constante nombrada con su porqué, hermana de
   `LEAD_ESPERA_SEMANAS`. **Por banda: rechazado** (el colchón es post-entrega; la
   duración ya la empaqueta F2). Revisable con telemetría.
7. **La severidad la emite el enlazador** en el mismo JSON, contra **vocabulario
   cerrado** del nodo canónico: `probabilidad: poco_probable|probable|muy_probable`
   y `dolor: poco|bastante|mucho`. **Fuera del enum → null** (no se aproxima).
8. **Costo ABSORBIDO**, y **reportado MEDIDO en los checkpoints**.
   **CORREGIDO por el fundador (5 ago 2026), y esto es lo que manda:** el umbral
   de $0.25 venía del catálogo VIEJO (mundo a 3). Con el catálogo vigente (plan
   10, todo lo demás 5, fijado con análisis de mercado precisamente para
   financiar más calidad por entrega), el peor caso de la tubería completa de
   protección queda lejísimos del precio. **El umbral MUERE como puerta**; la
   medición **vive como telemetría de margen** (el costo por entrega ya se
   persiste en el evento de sesión) y se reporta **informativa, sin condición
   asociada**. Única alarma residual, de sentido común y no de umbral: si una
   entrega individual se acercara a un orden de magnitud del precio (**$0.50+**),
   se menciona. **Jamás se frena nada por centavos.**

### Enunciados originales (para que se lea el porqué de cada veredicto)

**1. La forma de la salida estructurada del enlazador.** El plan es prosa en
streaming (ancla 2). Tres caminos:
   - **(a) Segunda llamada "enlazador"** después del plan, con el plan y el
     snapshot, que devuelve JSON estricto. **Es mi recomendación:** es el patrón
     exacto de la estimación de F1 (probado, con fallback declarado), no toca la
     prosa que el usuario mira, y se puede validar contra el snapshot.
     Cuesta una llamada extra por plan de protección.
   - **(b) `SYSTEM_PLAN` de protección emite un bloque estructurado** al final que
     `derivarChecklist` lee. Sin llamada extra, pero mete gramática nueva en el
     parser que sostiene TODOS los planes, y ensucia lo que el usuario ve.
   - **(c) Enlace determinístico** por coincidencia de texto contra el snapshot.
     Gratis y sin IA, pero adivina: rompería "cero invención".
   **¿Cuál?**

**2. El copy de la muralla.** Ya existe *"Primero genera el plan de tu idea. El
mundo se construye sobre él."* La spec pide *"primero tu plan; tu mundo de Riesgos
se aplicará sobre él"*. ¿Cambio el copy **solo** para los tres mundos de
protección (más preciso, dos textos que mantener) o **uno solo** para todos
(más simple, menos específico)?

**3. Qué es "actividades vigentes" en el snapshot.** Tres lecturas posibles:
solo el ciclo vigente del núcleo (~31 ítems, lo más barato y lo que veo como
intención); todo lo no-hecho de cualquier ciclo; o todo. Cambia el costo y, más
importante, **el significado**: ¿protege lo que el usuario tiene por delante, o
también lo ya cerrado? Mi lectura es la primera, pero es una decisión de producto.

**4. Qué pasa con un enlace cuando su actividad del núcleo desaparece o se
retira.** Propongo `ON DELETE SET NULL` (la respuesta sobrevive como sistémica) y
que **`no_aplica` NO rompa el enlace** (la actividad retirada sigue existiendo).
¿De acuerdo? El riesgo de la otra opción es que retirar una tarea del núcleo
silencie una protección sin decirlo.

**5. El carril, con un Gantt que dibuja ETAPAS.** (Ancla 3.) Opciones: **(a)** la
respuesta se dibuja bajo la barra de la **etapa** de lo que protege (funciona ya,
menos preciso); **(b)** el carril es una **lista cronológica** paralela, no barras
alineadas; **(c)** el Gantt del núcleo pasa a tener barras por actividad, que es
un cambio grande en una pieza que Design ya calibró. ¿Cuál?

**6. El "margen" del ancla.** `min(fecha normal, ancla − margen)`: la spec no lo
define. Propongo **una semana**, con constante nombrada y el porqué escrito, igual
que `LEAD_ESPERA_SEMANAS`. ¿Se acepta, o el margen debe depender de la banda de la
respuesta (una XL necesita más colchón que una S)?

**7. Severidad sin puntajes: ¿de dónde sale?** La regla es clara (palabras, jamás
números). Lo que no está dicho es **quién** la produce: ¿la escribe el enlazador
como parte de su salida (probable/dolería mucho), o se deriva de algo que ya
existe? Si la escribe el modelo, entra en el mismo JSON de la Duda 1 y hay que
validarla contra un vocabulario cerrado para que no invente escalas.

**8. Costo y créditos.** El plan del mundo ya es una entrega pagada. El enlazador
(si es (a)) y el snapshot añaden coste real. ¿Se absorbe en el precio actual del
plan de mundo, o el fundador quiere verlo medido antes de decidir?

---

## D. Lo que NO haré sin que se diga (declarado)

Cruce mundo↔mundo; re-anclaje automático ante movimientos del núcleo; puntajes
numéricos; tocar los mundos de mejora; y **escribir una sola línea de código de
producto antes de que estas dudas estén resueltas**.
