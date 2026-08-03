# Plan — Restructuración "TODO SEPARADO"

Estado: **propuesta, pendiente del visto del fundador y del auditor.** 0 líneas de
código hasta la aprobación. (Redactado 2026-08-03. Anula parcialmente el frente
"La idea completa" (tag `web-v2.1.0-beta`) y la Opción A de la Fase 3.)

Todo verificado en código (no de memoria); las rutas son `file:line` reales.

## 0. El modelo final

El **proyecto principal** ("Tu viaje" / Mi idea) ES el centro visual y conceptual,
desde su pantalla actual (que no se toca en esencia). Los **mundos** son adiciones,
cada uno **espejo** de esa misma configuración con su etiqueta. **NO existe nivel
centralizado por encima.** Todo registro, medida y documento es **POR ESPACIO**, con
**UNA excepción global: el Expediente completo.**

**Principio de gobierno:** gobernanza separada por espacio, **cero mezcla de medidas**.
Cada espacio se mide solo, con sus indicadores. La única vista global es el Expediente.

## 1. Qué ya sirve / qué falta (verificado)

**Ya sirve:**
- El filtro de bitácora por espacio (Fase 3): `bitacoraDeEspacio` + ruta `?dominio` +
  `BitacoraEspacio` — **se queda** y es la base del acceso "Mi bitácora" del mundo.
- `analyticsDeMundo(entrada, dominio)` → `AnalyticsMundo.universal` tiene **la misma
  forma** que `analytics.universal` del core (`analytics.ts:458` vs `:539`): las Capas
  1 y 2 del Análisis se reusan verbatim con los datos del mundo.
- El Expediente ya lista principal-primero + una sección por mundo con **plan +
  acciones + cómo te fue** (`expediente.ts:333-356`, tanda 5). Sin mundos, solo el
  principal (`expediente.test.ts:210-218`).
- El "Reporte de {mundo}" ya se sirve (`route.ts:162-197`) con su campo `espacio`.
- Las dos acciones del mundo ya existen (cerrar con acta + seguimiento), scopeadas al
  dominio en backend (`ManosALaObra.tsx:1743-1763`, `enviarFollow(...,mundo.dominio)`).

**Falta / hay que cambiar:**
- Los 4 accesos (bitácora, calendario, análisis, documentos) viven **solo en el core**
  (aside gated por `mostrarCore`, `ManosALaObra.tsx:1799-1971`). El mundo **no los tiene**.
- No hay componente compartido de "tarjeta de acceso": son 4 `<div>` ad-hoc idénticos.
  Las 2 tarjetas de acción tienen **formatos distintos** entre sí y de los accesos.
- El Análisis (`AnalisisProyecto.tsx`) no recibe `dominio`: es del core (+ "Tu proyecto
  completo" y barras cross-mundo). Falta un análisis **por mundo** a pantalla completa.
- El Calendario (in-app y .ics) es **CORE-ONLY** (`Calendario.tsx:96`, `feed/route.ts:40`):
  no recoge ítems de mundo ni etiqueta por espacio.
- El Expediente **no lleva etiqueta "Global"**; los docs core no llevan su etiqueta de
  espacio (`DocumentoIndice.espacio` solo está en los reportes de mundo).

## 2. Las tandas (commits "Todo separado:")

### Tanda 0 — Gobierno (el banco lidera)
- **Re-enmienda BANCO §7.1** con la historia completa: (a) "Tu avance" vuelve a **"hitos
  reales del espacio, nada más"**; (b) **"no existe análisis global: cada espacio se
  mide solo, con sus indicadores; la única vista global es el Expediente completo"**;
  (c) la decisión del **calendario etiquetado por espacio**; (d) el porqué del fundador.
- **Matriz (PENDIENTES)**: refleja la eliminación del nivel general; las varas de Design
  pierden el nivel general y ganan el calendario etiquetado y las **seis tarjetas
  hermanas**.

### Tanda 1 — Eliminar el nivel general (borrado limpio)
Muere: `agregadoDeIdea`+`AgregadoIdea` (`analytics.ts:467-526`) y su describe
(`analytics.test.ts:599-660`); `IdeaCompleta.tsx` (archivo entero); `?vista=idea` +
`vistaIdea`/`irAIdeaCompleta`/origen "idea"/rama de despacho/`onIrIdea`
(`IdeaView.tsx`, ~12 puntos); la entrada "La idea completa" del cambiador
(`CambiadorEspacios.tsx:52-69` + prop `onIrIdea`); el campo `agregado` de `/analisis`
(`route.ts:53-56`); y la sección **"Tu proyecto completo"** + `NivelFila`
(`AnalisisProyecto.tsx:65-83, 163-198`). Gate: quitar capturas `?vista=idea` y el texto
"Tu proyecto completo" (`gate_beta.ts:199-210`) + el proyecto `pidSolo` que ya no aplica.

- **BORDE CRÍTICO (verificado, corrige un mapeo erróneo):** **NO borrar
  `ETIQUETAS_CICLO_PLAN`** (`analytics.ts:465`). Aunque el agregado lo usaba,
  `analyticsDeMundo` **también** lo usa (`analytics.ts:445`); borrarlo rompe el análisis
  por mundo de la tanda 3.
- `/analisis` **se queda** (4 consumidores: AnalisisProyecto, Celebracion, ManosALaObra,
  vuelo.ts); solo se quita el campo `agregado`. El tipo `Analytics.mundos` **se queda**
  (lo usa `CumplimientoPorMundoBarras`).

### Tanda 2 — "Tu avance" vuelve a solo hitos
- Quitar `EstadisticasEspacio` y `BitacoraEspacio` de la cara "Tu avance" en los dos
  seams (`ManosALaObra.tsx:1366,1368` core; `:1589,1593` mundo). "Tu avance" = **solo
  `LineaAvance`** (los hitos del espacio, únicos y propios).
- Esos dos componentes NO se borran: **se reubican** — las estadísticas pasan al acceso
  "Análisis de {espacio}" (tanda 4); `BitacoraEspacio`/su filtro pasan al acceso "Mi
  bitácora de {espacio}" (tanda 4).

### Tanda 3 — Las vistas SCOPEABLES por espacio (los destinos)
Hacer que las 4 vistas acepten un espacio, reusando lo existente:
- **Análisis por mundo (a pantalla completa, misma vara):** `/analisis?dominio=X` →
  devuelve un `Respuesta` armado desde `analyticsDeMundo`: `universal = m.universal`
  (Capas 1-2 verbatim), un **`cumplimiento` sintetizado** desde `CumplimientoDominio`
  (derivar pct; `porEtapa=[]`, `porDominio=[]`), `realizada_at←m.completadoAt`,
  `cierre_motivo←m.cierreMotivo`, `titulos` del plan del mundo, `nombre="…de {mundo}"`.
  `AnalisisProyecto` gana un prop `dominio?` y lo pasa al fetch; las piezas core-only
  (**Gantt** `c.porEtapa`, **MapaHitos** `a.hitos`, **barras cross-mundo**
  `c.porDominio.length>1`) se **auto-ocultan** por sus gates existentes. Etiqueta
  "Análisis de {espacio}".
- **Bitácora por espacio:** ya scopeada (`BitacoraEspacio` + ruta `?dominio`); solo
  cablear el acceso y la etiqueta.
- **Calendario por espacio:** el componente recoge el grupo del espacio (o todos, con
  filtro) — ver tanda 5.
- **Documentos por espacio:** ver tanda 6.
- **Navegación:** cada `ir*` gana un `dominio` opcional; deep-link `?vista=analisis&dominio=X`,
  etc.; "Volver" coherente por espacio (patrón del `?cara=`).

### Tanda 4 — Los 6 accesos/acciones UNIFORMES por espacio
- **Extraer `TarjetaAcceso`** (componente nuevo): icono + título + descripción + botón,
  un solo formato. Reemplaza los 4 `<div>` ad-hoc.
- **El aside existe en CADA espacio** (core y hub de mundo): hoy está gated por
  `mostrarCore`; se generaliza a "el espacio actual", con los conteos/gates **del
  espacio** (bitácora: hay entradas; calendario: modo fechas + hay fechas del espacio;
  análisis: hay acciones del espacio).
- **Seis tarjetas hermanas** (mismo patrón): Mi bitácora · Tu calendario · Análisis ·
  Tus documentos · (la de cierre) · (la de ciclo). Etiquetadas con el nombre del espacio.
- **Las 2 tarjetas de acción por espacio** adoptan el formato de `TarjetaAcceso`:
  - core: "Tu idea ya es un proyecto · Marcar como realizada" y "¿La realidad te cambió
    el plan? · Contar qué pasó".
  - mundo: sus equivalentes (cerrar el mundo con acta; el seguimiento del mundo). **Copy
    del mundo (paridad):** el seguimiento del mundo hoy es un botón pelado sin promesa;
    gana su línea propia scopeada — p.ej. *"¿La realidad cambió {mundo}? Cuéntame qué
    pasó y lo recalculo desde donde estás"* — **jamás "todo"** (el backend ya recalcula
    solo ese mundo: `enviarFollow(...,dominio)`; se hace explícito en el copy).

### Tanda 5 — Calendario ETIQUETADO por espacio (lo nuevo importante)
- **Incluir ítems de mundo** (relajar el filtro `esCore`) en los 3 generadores: el
  Calendario in-app (`Calendario.tsx:96`, recoger todos los grupos), las descargas
  (`ManosALaObra.tsx:1077`), y el **feed webcal** (`feed/route.ts:40`).
- **Etiqueta visible:** añadir `nombreEspacio?` a `TareaIcs` y **prefijar el SUMMARY en
  UN solo sitio** (`ics.ts:86`): `[Calidad y Confianza] {texto}`. Poblar el nombre de
  cara (catálogo) en cada llamador.
- **La vista in-app filtra/etiqueta por espacio** (cada actividad muestra su etiqueta;
  el calendario de un mundo muestra lo suyo).
- **Cuidando el Nivel 1 (Google Calendar):** el `UID` por ítem (`ics.ts:83`) **no se
  toca** → los suscriptores **actualizan** el evento (ganan el prefijo), no se duplica.
  El prefijo va en un solo lugar (idempotente). El feed sigue siendo por-usuario; ahora
  incluye los mundos, cada uno etiquetado.

### Tanda 6 — Documentos etiquetados (Global / específico)
- **Etiqueta explícita:** el **Expediente = "Global"** (único global); los específicos
  con el nombre de su espacio ("Bitácora de Quality", "Análisis de Quality", "Tu Plan"
  del núcleo con su etiqueta). Requiere: `DocumentoIndice` gana una etiqueta de espacio
  para el expediente y los docs core (hoy `espacio` solo está en reportes de mundo), y
  `Descargas.tsx` renderiza el chip **también** para el global (hoy solo con `doc.espacio`).
- **El panel por espacio:** el acceso "Tus documentos" de un espacio muestra SUS
  documentos; el Expediente (Global) se muestra desde el núcleo. (Ver DUDA 4.)
- **Verificar el Expediente:** ya lista principal-primero + por mundo (tanda 5). **BORDE
  de orden:** el **resumen** (`informeMd`) y la **secuencia** (bitácora global) del
  principal hoy van **DESPUÉS** de los mundos (`expediente.ts:358,372`), así que el
  principal no queda 100% contiguo. Decisión en DUDA 5.

### Cierre — verificación
- **Tests que MUEREN:** el describe de `agregadoDeIdea` (`analytics.test.ts:599-660`).
- **Tests que se ACTUALIZAN:** ninguno de "Tu avance" (era UI sin tests); revisar que
  nada más dependa de lo borrado (verificado: solo ese describe).
- **Tests NUEVOS (puros, a mano):** la **síntesis** de `CapaCumplimiento` desde
  `CumplimientoDominio` (pct, vacíos); el **prefijo del ICS** por espacio (idempotente,
  UID intacto); el **índice** con etiqueta Global/específico (expediente="Global", docs
  core con su etiqueta); el calendario recogiendo ítems de mundo.
- **Gate re-capturado** (`gate_beta.ts`): quitar `?vista=idea`/"Tu proyecto completo";
  añadir por-espacio los 4 accesos + las 2 acciones (core y un mundo), el análisis de un
  mundo, el calendario etiquetado, y los documentos con etiqueta Global/específico. Dos
  viewports. **No corrido en vivo** (lo corre el fundador/auditor).
- **Tag:** `web-v2.2.0-beta` ("todo separado"). Merge a main solo con visto, por tanda.

## 3. PROBLEMAS, BORDES Y DUDAS (para calibrar antes de codificar)

**Bordes ya resueltos en el plan:**
- **B1.** `ETIQUETAS_CICLO_PLAN` NO es huérfano (lo usa `analyticsDeMundo`): no borrar.
- **B2.** `/analisis` y `Analytics.mundos` se quedan (4+1 consumidores). Solo muere `agregado`.
- **B3.** El `UID` del ICS es estable: el prefijo del SUMMARY no duplica eventos (Nivel 1 sano).

**Dudas que necesito que decidan (fundador + auditor):**
- **D1 — Barras cross-mundo en el Análisis del núcleo.** `CumplimientoPorMundoBarras`
  (`AnalisisProyecto.tsx:340-351`) muestra el cumplimiento de core + mundos en un solo
  gráfico. ¿Es "composición global" que también debe morir (para que el análisis del
  núcleo sea 100% core), o se queda? *Recomiendo quitarla* (coherente con "cada espacio
  se mide solo"); el desglose por mundo ya vive en el análisis de cada mundo.
- **D2 — El Análisis de un mundo es más ligero.** No tendrá **Gantt** (no hay `porEtapa`
  por mundo) ni **MapaHitos** (no hay `hitos` por mundo; sus hitos viven en "Tu avance").
  Tendrá: avance, ritmo, esfuerzo, y el cumplimiento (a tiempo/adelantadas/tardías) sin
  el Gantt. ¿Aceptable? *Recomiendo sí* (misma vara de tiles; lo que falta no existe por
  mundo).
- **D3 — Calendario: el feed webcal es por-usuario (todas las ideas).** Etiquetar por
  espacio es correcto, pero el feed **crece** (ahora incluye los mundos). Los suscriptores
  verán aparecer los eventos de mundo y los títulos ganar el prefijo. ¿Confirmado que es
  el comportamiento deseado del Nivel 1? (La vista in-app sí se scopea por espacio; el
  feed es uno por usuario, todo etiquetado.)
- **D4 — El panel "Tus documentos" por espacio.** ¿El acceso de un mundo muestra solo su
  "Reporte de {mundo}" (que ya empaqueta su plan+seguimientos+avance+cómo te fue), o
  además sus ciclos sueltos (Tu Plan/Seguimiento del mundo) como documentos separados? Y
  el **Expediente (Global)**: ¿se muestra solo desde el núcleo, o también aparece
  (etiquetado "Global") en cada espacio? *Recomiendo: mundo = su Reporte; Expediente
  (Global) desde el núcleo.*
- **D5 — Orden del Expediente.** ¿Reordenar para que el proyecto principal quede 100%
  contiguo (idea→números→**resumen→secuencia**), y LUEGO los mundos? ¿O el resumen/
  secuencia globales cierran el documento (como hoy), porque son la lectura del proyecto
  entero? *Recomiendo dejarlo* (el resumen+secuencia son el cierre global del único doc
  global); solo lo señalo por si tu modelo asume contigüidad estricta.
- **D6 — Las 2 tarjetas de acción como `TarjetaAcceso`.** Hoy la de "realizada" y el
  ritual **expanden su flujo en la propia tarjeta**. Uniformar a "6 hermanas" implica que
  la tarjeta es la ENTRADA y el flujo (confirmación/ritual) se abre al pulsar (overlay o
  expansión). ¿De acuerdo con ese patrón? (Preserva los flujos; cambia solo la envoltura.)

## 4. Riesgos de ejecución
- **Navegación vista×espacio.** Multiplica el estado (cada `?vista=` gana `&dominio=`).
  Riesgo de "Volver" incoherente entre espacios; se mitiga con el patrón del `?cara=` ya
  probado y pruebas de deep-link en el gate.
- **UI no unit-testeable** (vitest = node, sin testing-library): los accesos por espacio,
  el aside y las tarjetas se verifican en el **gate** (capturas), no en tests. Lo puro
  (síntesis de cumplimiento, prefijo ICS, índice etiquetado) sí lleva tests a mano.
- **Alcance.** Es la restructuración más grande desde la Fase 3: 7 tandas. Propongo
  checkpoint por tanda y merge con tu visto, como en Fase 3.
