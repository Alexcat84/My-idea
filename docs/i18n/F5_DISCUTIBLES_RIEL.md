# i18n F5: etiquetas del riel, lo discutible por idioma (para el fundador)

Anexo de `F5_INFORME.md`. Cada idioma lo tradujo un modelo y lo revisó un segundo modelo; lo evidente ya está aplicado en `web/lib/i18n/etiquetas/<idioma>.json`. Esto es lo que el revisor dejó para tu decisión, tal cual lo escribió (las notas **[aplicado]** las agregó la sesión de la nube).

## DECISIÓN DEL FUNDADOR (25 sep 2026)

Aprobadas las cuatro decisiones de la nube (riel por la interfaz, lo interno en español, documentos
en F6, "État" con mayúscula). Para lo discutible: **se aplica la versión del revisor salvo que choque
con el glosario aprobado**. Aplicado el 25 sep 2026 con `scripts/i18n/etiquetasRiel.ts aplicar`
(valida cada etiqueta), 19 etiquetas:

- **en** (1): `descomponer_tiempo_ciclo_pedido` "Time Each Step of Your Order" → "Time Each Stage of
  Your Order" (el glosario fija etapa = stage).
- **fr** (0 nuevas): los casos 1 a 4 y 10 ya los había aplicado la nube; 5 y 6 (el "?" de las
  preguntas) el revisor los deja como están, "se lee natural", y no propone otra versión; 7 a 9
  ("État") quedan con mayúscula por la decisión del fundador.
- **pt** (3): `plan_de_contingencia_b`, `autoresponders_drip_campaigns` (acompanhamento, como fija el
  glosario para Seguimiento) y `framework_excelencia_operacional`.
- **de** (5): `framework_good_bad_product_manager` y los cuatro ciclos en infinitivo pasan al
  imperativo du (`build_measure_learn`, `ciclo_crear_medir_aprender`, `desarrollo_en_espiral`,
  `design_test_repeat`). El par del crédito de exportación queda como está (el revisor lo ve
  intencional).
- **it** (2): `autoservicio_y_autosanacion_del_producto` ("senza che") y
  `ten_un_checklist_de_clausulas_de_contrato` (la versión del revisor, con "lista di controllo").
- **ja** (1): `diez_derechos_servicio_cliente` → 配送の10の権利.
- **ko** (5): las tres de margen pasan a 마진, que es el término fijo del glosario; y las dos más
  largas, acortadas.
- **ar** (1): `evaluar_proceso_completo_no_cada_metrica` (حاصل ضرب, sin el doble sentido de اضربوا).
- **hi** (1): `establecer_proyecto_y_metas_diseno` (la versión inequívoca, con coma).
- **Sin cambio:** en `company_building` (el revisor no propone otra versión); it
  `modelos_negocio_mas_alla_del_lucro` y las dudas del grafo (`valor_presente_franquicia_pvf`,
  `warrants_financiamiento`, `modelos_negocio_mas_alla_del_lucro`): las corrige la sesión dueña del
  dataset; cuando lleguen a `main` se traen a `i18n` y se vuelve a derivar esa etiqueta en los diez
  idiomas.

---

## Discutibles — revisión de naturalidad (en)

Revisé las 3169 etiquetas de `en_01.json`…`en_04.json` contra sus traducciones en
`en_01.out.json`…`en_04.out.json`. La calidad general es muy alta y consistente
(glosario respetado, jerga de negocios evitada de forma sistemática — "MVP",
"pivot", "leverage", "synergy", "stakeholder" no aparecen ni una vez en las 3169
traducciones). Solo encontré 4 casos que valen la decisión del fundador, no un
arreglo evidente:

1. **`valor_presente_franquicia_pvf`** — ES: "Calcula el Valor Futuro" | EN actual:
   "Calculate a Franchise's Present Value" — El error está en el ESPAÑOL: el
   `titulo` dice "Valor Presente de una Franquicia (PVF)" y el id es "pvf", pero
   la `etiqueta` española dice "Futuro" en vez de "Presente" (contradice su propio
   título). El traductor tradujo el concepto correcto (Presente), no el texto
   literal español (que tiene el bug). Propongo dejar el inglés como está y
   corregir el bug en la etiqueta española fuente ("Calcula el Valor Presente"),
   no tocar el inglés — pero es una decisión de fondo, no una corrección de
   traducción.

2. **`warrants_financiamiento`** **[aplicado por la nube: el inglés invertía el sentido del nodo; ahora "Know How Warrants Lower Your Valuation"]** — ES: "Usa Opciones para Bajar la Valoración" |
   EN actual: "Use Warrants to Protect Your Valuation" — posible inversión de
   sentido ("bajar" vs "protect"): en financiamientos de etapas tardías, los
   warrants pueden ser una forma de dar valor a los inversionistas SIN bajar
   formalmente la valoración del encabezado (lo que encajaría con "Protect"), o
   la etiqueta española puede referirse literalmente a bajar la valoración
   efectiva. Requiere criterio de quien conoce la mecánica financiera exacta que
   se quiso enseñar en este nodo; no lo cambié por no tener certeza del sentido
   correcto en ninguno de los dos idiomas.

3. **`company_building`** — ES: "Construye Tu Empresa Formal" | EN actual: "Build
   Your Company for Real" — matiz: "formal" en español apunta a una empresa
   formalmente constituida (aspecto legal/estructural); "for real" en inglés
   suena más a "en serio, de verdad" (actitud) que a formalidad legal. Ambas
   lecturas son razonables dado el título ("Construir la empresa"); no es un
   error claro, pero cambia ligeramente el énfasis.

4. **`descomponer_tiempo_ciclo_pedido`** — ES: "Mide cada etapa de tu pedido" |
   EN actual: "Time Each Step of Your Order" — en el resto del corpus "etapa" se
   traduce consistentemente como "stage" (siete casos: `aceleracion_de_gates`,
   `burn_rate_por_etapa`, `criterios_de_exito_gate`, etc.). Aquí se usó "Step".
   No es necesariamente un error (esta "etapa" es una fase genérica de un
   proceso de pedido, no la "Etapa" canónica del recorrido del glosario), pero
   rompe la coherencia interna de término si el fundador prefiere uniformidad
   estricta.

No hay más casos discutibles de peso: no encontré pérdida de sentido, jerga de
negocios, anglicismos crudos, errores ortográficos ni de mayúsculas fuera de
estos cuatro matices.

---

## Discutibles — revisión de naturalidad fr (i18n F5, D3)

Revisé las 3169 etiquetas de `fr_01.out.json` … `fr_04.out.json` contra el español y el título de
apoyo. La calidad es muy alta: no encontré ninguna corrección **evidente** (ningún sentido
equivocado, anglicismo crudo, error de ortografía/mayúsculas, "vous" en vez de "tu", ni etiqueta
que exceda el largo permitido). `fr_revision.json` queda vacío (`{}`) a propósito — no es que no
revisé, es que no hubo nada que un nativo no dudaría en corregir.

Sí encontré cuatro decisiones de estilo/coherencia que el fundador debería ver:

1. **`capacitacion_educacion_seguridad`** **[aplicado: choca con el término fijo de los mundos / pierde "indirect"]** | ES: "Capacita en Seguridad Laboral" | FR actual:
   "Forme ton monde en santé et sécurité" | Propuesta: "Forme ton équipe en santé et sécurité" |
   Por qué: "mon monde" es un quebequismo válido para "mi gente/mi equipo", pero "Monde" es también
   el término fijo del glosario para el concepto propio "Mundos" (los nueve mundos de la app);
   usarlo aquí como sinónimo coloquial de "equipo" puede leerse como una referencia a ese concepto
   en la misma superficie de navegación.
2. **`educacion_calidad`** **[aplicado: choca con el término fijo de los mundos / pierde "indirect"]** | ES: "Educa a tu Gente en Calidad" | FR actual: "Forme ton monde à la
   qualité" | Propuesta: "Forme ton équipe à la qualité" | Por qué: mismo choque con "Mondes" que el
   caso anterior.
3. **`manejo_empleados_en_adquisicion`** **[aplicado: choca con el término fijo de los mundos / pierde "indirect"]** | ES: "Cuida a tu Gente al Vender" | FR actual: "Prends
   soin de ton monde en vendant" | Propuesta: "Prends soin de tes employés en vendant" | Por qué:
   mismo choque; aquí además "empleados" (del título) es más preciso que el coloquial "monde".
4. **`diagnostico_motivacion_para_contrataciones_inversores`** **[aplicado: choca con el término fijo de los mundos / pierde "indirect"]** | ES: "Alinea Motivaciones Antes de
   Sumar" | FR actual: "Aligne les motivations avant d'ajouter du monde" | Propuesta: "Aligne les
   motivations avant de recruter" | Por qué: mismo choque, y "ajouter du monde" es además más
   informal que el resto del lote.
5. **`cual_es_tu_mayor_riesgo`** | ES: "Cuál Es tu Mayor Riesgo" (sin "¿…?") | FR actual: "Quel est
   ton plus grand risque?" | Por qué es discutible: el español eligió NO puntuarla como pregunta
   (a diferencia de otras tres etiquetas de riesgo que sí llevan "¿…?"); el traductor la volvió
   pregunta en francés. No está mal —se lee natural— pero es una decisión de estilo que no viene
   del español: ¿toda etiqueta que suene a pregunta debe llevar "?" en francés aunque el español no
   la puntúe así, o se debe respetar la puntuación (o falta de ella) del español etiqueta por
   etiqueta?
6. **`cuan_probable_y_cuanto_doleria`** | ES: "Cuán Probable y Cuánto Dolería" (sin "¿…?") | FR
   actual: "Quelle probabilité et quel impact?" | Mismo caso que el anterior: mismo par de
   etiquetas de "riesgo" con esta ambigüedad, mismo criterio a decidir.
7. **`planes_estatales_osha`** **[no aplicado en 7 a 9: "État" con mayúscula es correcto para un estado federado, como "l'État de New York"]** | ES: "Conoce tus Planes Estatales" | FR actual: "Connais les
   régimes de ton État" (con mayúscula) | Propuesta: "ton état" (minúscula) | Por qué: en francés
   "État" con mayúscula se reserva para el Estado como poder/institución o dentro de un nombre
   propio ("l'État du Texas", "États-Unis"); aquí es un sustantivo genérico (un estado de EE. UU.
   cualquiera), que va en minúscula.
8. **`cumplir_leyes_estatales_franquicia`** | ES: "Cumple las Leyes Estatales" | FR actual:
   "Respecte les lois des États" | Propuesta: "des états" (minúscula) | Por qué: mismo caso que el
   anterior, uso genérico y plural.
9. **`registro_estatal_franquicia`** | ES: "Cumple los Registros Estatales" | FR actual: "Respecte
   les enregistrements des États" | Propuesta: "des états" (minúscula) | Por qué: mismo caso.
10. **`metodos_exportacion_directa_indirecta_2`** **[aplicado: choca con el término fijo de los mundos / pierde "indirect"]** | ES: "Decide Vender Directo o Indirecto" | FR
    actual: "Choisis de vendre en direct ou non" | Propuesta: "Choisis de vendre en direct ou en
    indirect" | Por qué: el español nombra las dos alternativas ("directo" e "indirecto"); "ou non"
    generaliza a un simple sí/no y pierde el término "indirecto" que el resto del lote (canales,
    intermediarios) usa con cuidado.

Nada más se acerca a discutible: el resto del lote usa consistentemente el tuteo, evita "vous",
usa "courriel" y nunca "mail", respeta el glosario (marge, seuil de rentabilité, client, équipe,
idée, risque…), sin rayas ni comillas decorativas, y ninguna etiqueta pasa de 70 caracteres.

---

## Discutibles — revisión pt (portugués de Brasil)

Revisé las 3.169 etiquetas de `pt_01..04.out.json` contra `pt_01..04.json`. No encontré
correcciones evidentes (ninguna que un nativo no dudara en hacer): el traductor mantuvo el
sentido, el registro "você", el glosario, la coherencia de términos y las reglas de formato
(sin rayas, sin ¿¡, sin punto final, sin marcadores rotos). Estos tres casos son decisiones de
matiz que le subo al fundador, no errores:

- `plan_de_contingencia_b` — ES: "Pregúntate: Ya Pasó lo Peor" — PT actual: "Pergunte-se: o pior
  já passou?" — Propuesta: "Pergunte-se: e se o pior já tivesse passado" (o similar en forma de
  premisa, no de pregunta de sí/no) — Por qué: el título de apoyo es "Pregunta Inversa": la técnica
  pide asumir que lo peor ya ocurrió y planear desde ahí, no preguntar si ya ocurrió; la versión
  actual convierte la premisa en una pregunta literal y cambia ligeramente la técnica.

- `autoresponders_drip_campaigns` — ES: "Automatiza tus Mensajes de Seguimiento" — PT actual:
  "Automatize suas mensagens de retorno" — Propuesta: "Automatize suas mensagens de
  acompanhamento" — Por qué: "mensagens de retorno" suena a mensajes de respuesta/vuelta, no a la
  secuencia de seguimiento proactivo (drip campaign) que describe el título; además es el único
  lugar donde "seguimiento" no se resuelve con la familia "acompanhar" que usa el resto del lote
  (p. ej. `gestion_seguimiento_prospectos`: "Acompanhe sem pressionar").

- `framework_excelencia_operacional` — ES: "Pregúntate por tu Excelencia Operativa" — PT actual:
  "Questione sua excelência operacional" — Propuesta: "Reflita sobre sua excelência operacional"
  (o "Avalie sua excelência operacional") — Por qué: "questionar" en portugués suena a poner en
  duda o desafiar algo, no a "hacerte preguntas sobre" algo como invita el español y confirma el
  título ("Framework de Preguntas..."); cambia el matiz de reflexión a uno de escepticismo.

No hay más casos que me parezca necesario subir: el resto del lote (anglicismos, jerga, mayúsculas,
longitud, coherencia de glosario, falsos amigos español-portugués) pasó limpio.

---

## Discutibles — revisión de naturalidad (alemán)

Revisé las 3169 etiquetas de `de_01..04.out.json` contra `de_01..04.json` (etiqueta española +
título como contexto). La calidad general es muy alta y consistente. Solo una corrección fue
evidente (ver `de_revision.json`). Lo que sigue son seis casos discutibles, para que el fundador
decida; ninguno es un error claro de un nativo.

1. **`framework_good_bad_product_manager`** — es: "Sé un Gran Gerente de Producto" · de actual:
   "Werde eine großartige Produktverantwortliche Person" · propuesta: "Werde großartig im
   Produktmanagement" (o "Sei eine großartige Führungskraft für dein Produkt") · por qué: el
   traductor evita el género de "Produktmanager" (patrón que también usa en `chief_sustainability_officer`
   → "eine Person für Nachhaltigkeit" y en `un_dueno_para_cada_riesgo` → "eine verantwortliche
   Person"), pero aquí "Produktverantwortliche Person" suena redundante y calcado ("responsable de
   producto" + "persona"), no como el título corto de una app.

2. **`build_measure_learn`** — es: "Construye, Mide y Aprende" · de actual: "Bauen, messen und
   lernen" · propuesta: "Baue, miss und lerne" (si se prioriza el registro imperativo parejo con
   el resto del lote) · por qué: es de las cuatro únicas etiquetas de las 3169 que usan infinitivos
   en vez del imperativo "du" que pide `INSTRUCCIONES.md`; es defendible como convención alemana
   real para nombrar un ciclo de método ("Bauen, Messen, Lernen" aparece así en literatura de Lean
   Startup en alemán), pero rompe la regla de registro.

3. **`ciclo_crear_medir_aprender`** — es: "Crea, Mide y Aprende" · de actual: "Bauen, messen und
   dazulernen" · propuesta: "Erschaffe, miss und lerne" (imperativo) o, si se mantiene el
   infinitivo, unificarlo con el de `build_measure_learn` ("Bauen, Messen, Lernen") ya que ambos
   nombran el mismo ciclo · por qué: mismo caso que el anterior, y además con una variante de
   verbo distinta ("dazulernen" vs "lernen") para el mismo concepto.

4. **`desarrollo_en_espiral`** — es: "Construye, Prueba y Ajusta" · de actual: "Bauen, testen und
   nachjustieren" · propuesta: "Baue, teste und justiere nach" (imperativo) · por qué: mismo patrón
   de infinitivo que los dos casos anteriores.

5. **`design_test_repeat`** — es: "Diseña, Prueba y Repite" · de actual: "Gestalten, testen,
   wiederholen" · propuesta: "Gestalte, teste, wiederhole" (imperativo) · por qué: mismo patrón;
   estos cuatro son los únicos casos de los 3169 que se apartan del "du" imperativo, así que la
   decisión debería tomarse una sola vez para los cuatro.

6. **`programas_ex_im_bank` / `seguro_de_credito_a_la_exportacion`** — misma etiqueta española
   ("Asegura tu Crédito de Exportación") para dos nodos distintos, con traducciones ligeramente
   distintas: "Sichere deinen Exportkredit ab" (programas de financiamiento) vs "Sichere deinen
   Exportkredit" (seguro de crédito) · por qué: el título de cada nodo es distinto (financiamiento
   vs. seguro), así que la diferencia parece intencional para distinguir los dos conceptos con
   "absichern" (asegurar/cubrir) solo en el de seguro; lo marco solo porque es el único par de
   etiquetas españolas idénticas que salió con alemán distinto en las 3169.

No hay más discutibles: el resto de divergencias que revisé (préstamos como "Team", "Business
Angels", "Marketing", "Coach", el uso de "KI" por IA, las formas plurales "ihr/eure" en los pocos
casos que hablan de "entre todos" o de reunirse) son natural alemán estándar y coherentes con el
glosario de `F3_CONVENCIONES.md` y `DISENO.md §6`.

---

## Discutibles — revisión de naturalidad IT (riel)

Revisé las 3169 etiquetas de `it_01..04.out.json` contra `it_01..04.json`. La calidad general
es muy alta (registro imperativo "tu" consistente, sin anglicismos crudos, sin rayas ni ¿¡,
todas por debajo de 70 caracteres, glosario respetado). Solo encontré 3 casos discutibles,
ninguno grave:

1. **`modelos_negocio_mas_alla_del_lucro`** — ES etiqueta: "Diseña tu Modelo sin Lucro" | IT
   actual: "Progetta il tuo modello oltre il profitto" | Mi propuesta: mantener la actual.
   Por qué: la etiqueta española dice literalmente "sin Lucro" (sin ánimo de lucro), pero el
   título ("Modelos de Negocio Más Allá del Lucro") deja claro que el concepto real es
   "más allá del lucro", no "sin lucro" (que sería un modelo sin fines de lucro, una idea
   distinta). El traductor siguió el sentido del título en vez de la palabra literal de la
   etiqueta; creo que acertó, pero como la etiqueta española misma parece tener una compresión
   imprecisa, lo subo para que el fundador confirme que el concepto es "más allá del lucro" y
   no "sin fines de lucro".

2. **`autoservicio_y_autosanacion_del_producto`** — ES: "Resuelve sin que te Llamen" | IT
   actual: "Risolvi prima che ti chiamino" | Mi propuesta: "Risolvi senza che ti chiamino".
   Por qué: la etiqueta española es "sin que te llamen" (sin necesidad de que llamen), y la
   traducción actual dice "antes de que llamen" (temporal, antes de que ocurra la llamada). Son
   matices distintos: uno es ausencia de la llamada, el otro es anticipación a ella. Mi
   propuesta usa la misma estructura de ausencia ("senza che") que el español, más fiel al
   sentido original de autoservicio (el producto se autosana sin generar ningún contacto).

3. **Coherencia de "checklist"** — `auditoria_de_proceso` (ES "Verifica tu Proceso con
   Checklist") tradujo "checklist" como "una lista di controllo" (evitando el anglicismo, bien),
   pero `ten_un_checklist_de_clausulas_de_contrato` (ES "Checklist de clausulas del contrato")
   se apartó del concepto "checklist" y tradujo el contenido del título en cambio: "Le clausole
   che ogni contratto deve avere" (las cláusulas que todo contrato debe tener), perdiendo la
   idea de lista de verificación que sí está en la etiqueta española. No es grave ni tiene una
   solución obviamente mejor (la etiqueta española original ya es rara, no imperativa, no en
   segunda persona), así que lo subo en vez de corregirlo yo: ¿debería seguir la forma literal
   de "checklist" ("Usa una lista di controllo delle clausole del contratto") o mantener la
   traducción actual, más legible como título de app?

No hay más casos discutibles de peso; el resto de las 3169 etiquetas está bien.

---

## Discutibles — revisión de naturalidad ja (riel)

Revisé las 3169 etiquetas (ja_01..04.out.json contra ja_01..04.json, con el título
como contexto), más los chequeos automáticos de largo, puntuación prohibida,
espacios, mayúsculas/romanización, coherencia terminológica y consistencia
ortográfica de los verbos recurrentes. El lote es de calidad excepcionalmente alta
y consistente: no encontré ninguna corrección evidente que un nativo no dudaría en
hacer (por eso `ja_revision.json` queda vacío, `{}`). Solo hay un caso realmente
discutible, y es una decisión de matiz, no un error:

1. **`diez_derechos_servicio_cliente`** — español: "Los diez derechos de tu
   entrega" — traducción actual: **配送の10の基本** ("los 10 fundamentos de la
   entrega") — propuesta: **配送の10の権利** ("los 10 derechos de la entrega") —
   por qué: el español usa deliberadamente "derechos" (el marco clásico de un
   "decálogo de derechos del cliente"); "基本" (fundamentos/lo básico) es una
   traducción natural y válida, pero cambia el encuadre de "derecho que se te debe"
   a "cosa básica que se hace bien". Ambas suenan naturales en japonés; es una
   elección de énfasis, no un error, así que la subo en vez de aplicarla como
   evidente.

No hay más casos que merezcan subir al fundador. Cosas que verifiqué específicamente
y que NO son discutibles (las menciono para que quede constancia del criterio
usado, no como hallazgo):
- Los préstamos del inglés que aparecen (AI, ISO, SNS, IT, GDP, CO2, cm) son términos
  de uso corriente en japonés de negocios, no jerga cruda; se dejan tal cual en todo
  el lote de forma consistente.
- "Etapa" del español se traduce como ステージ cuando el tema es la metodología
  stage-gate (término de industria) y como 段階 cuando es un paso genérico (proceso
  creativo, llamada de ventas, ronda de inversión…); es una distinción correcta, no
  una inconsistencia.
- No hay ninguna etiqueta con あなた, con です/ます, con rayas, ¿¡, comillas
  decorativas, emojis, punto final, ni espacios entre palabras.

---

## Discutibles — revisión de naturalidad zh (riel)

No hay casos discutibles que subir al fundador.

Revisé las 3169 etiquetas de `zh_01.out.json` a `zh_04.out.json` contra el español y el
glosario (`F3_CONVENCIONES.md`, `DISENO.md §6`). El lote es de una calidad muy alta y
consistente: sentido correcto, registro natural de segundo modelo en chino (verbo + objeto,
imperativo implícito, sin sujeto "你" explícito salvo donde ayuda), sin anglicismos ni jerga
de manual, puntuación de ancho completo (，。：？) y comillas “” correctas donde se cita un
término, sin rayas, ¿¡, comillas decorativas fuera de lugar, saltos de línea, marcas `{{ }}`
o `< >`, ni punto final. Ningún carácter tradicional se coló (todo en simplificado). Ningún
id sobra o falta frente al español.

La única corrección que hice fue evidente (ya está en `zh_revision.json`, no discutible):
`busqueda_ceo_sucesor_externo` usaba "首席执行官" (la única vez en las 3169 que se deletreaba
así) cuando las otras 7 etiquetas con CEO usan siempre la sigla "CEO" — es una simple
inconsistencia de un solo caso, no una decisión de términos.

Dos usos que sí revisé con cuidado por si eran inconsistencia y NO lo son, por si el
fundador quiere confirmarlo:
- "特许经营" vs "加盟" para "franquicia": el traductor los usa con criterio, no al azar —
  "特许经营" para el concepto legal/de modelo de negocio (definición, regulación, estructura)
  y "加盟" para la perspectiva del franquiciado (unirse, abrir, franquicia existente). Es la
  distinción natural que hace el chino de negocios, no una inconsistencia a corregir.
- Los acrónimos en latín (AI, CEO, ISO, IT, GDP, 3D, 5S) se dejan tal cual en casi todas las
  etiquetas donde aparecen en español: es el uso estándar en escritura de negocios en chino
  simplificado, no el anglicismo crudo que prohíbe `INSTRUCCIONES.md` (ese prohíbe jerga como
  "leverage"/"MVP"/"pivot", no siglas técnicas de uso común).

Si el fundador quiere una opinión sobre esos dos puntos igual, con gusto los subo como
discutibles reales; por ahora los resolví como "evidentes, sin cambio" porque un nativo no
dudaría frente a ninguno de los dos.

---

## Discutibles — revisión de naturalidad ko (i18n F5, D3)

Revisé las 3169 etiquetas de `ko_01..04.out.json` contra `ko_01..04.json` (español) y el
glosario (`F3_CONVENCIONES.md`, `DISENO.md §6`). Casi todo el lote es natural, coherente y
respeta el registro 해요체 pedido. Lo evidente (un swap de traducciones entre dos ids y un
registro no imperativo donde el español sí lo es) ya está en `ko_revision.json`. Lo que sigue
es discutible: decisiones de términos o de estilo que conviene que el fundador vea.

1. **`margen_bruto`** — es: "Calcula tu Margen Bruto" — actual: "매출 총이익률을 계산하세요" —
   propuesta: "매출 총마진을 계산하세요" — por qué: el glosario (`F3_CONVENCIONES.md`) fija
   "margen" = 마진 para toda la app, pero esta etiqueta (y las dos siguientes) usan "이익률"
   (término contable más preciso y también natural); es una divergencia real del término fijo,
   pero cambiarla a 마진 suena algo más informal/comercial que "이익률" para un ratio financiero
   con nombre propio. Decisión de términos, no un error de sentido.
2. **`margen_neto`** — es: "Calcula tu Margen Neto" — actual: "순이익률을 계산하세요" —
   propuesta: "순마진을 계산하세요" — por qué: mismo caso que `margen_bruto`: coherencia con el
   glosario vs. precisión contable estándar en coreano.
3. **`margen_operativo`** — es: "Calcula tu Margen Operativo" — actual: "영업 이익률을 계산하세요"
   — propuesta: "영업 마진을 계산하세요" — por qué: mismo caso; las tres etiquetas de margen
   están internamente coherentes entre sí (todas usan 이익률), solo divergen del término de
   catálogo. Si el fundador prefiere la precisión contable, dejarlas así; si prefiere coherencia
   estricta con "margen = 마진", corregir las tres a la vez.
4. **`seleccion_fuente_unica_multiple`** — es: "Elige Uno o Varios Proveedores" — actual:
   "공급업체를 하나로 할지 여럿으로 할지 고르세요" (25 caracteres, la más larga de las 3169) —
   propuesta: "단일 또는 복수 공급업체를 고르세요" (16 caracteres) — por qué: el sentido es
   correcto y natural, pero es notablemente más larga que el resto del lote (mediana: 14
   caracteres) para un riel de navegación.
5. **`rediseno_procesos_negocio_cx`** — es: "Rediseña Procesos Pensando en el Cliente" — actual:
   "고객을 생각하며 프로세스를 다시 설계하세요" (23 caracteres) — propuesta: "고객 중심으로
   프로세스를 재설계하세요" (17 caracteres) — por qué: acorta sin perder sentido. Hay unas 55
   etiquetas del lote (de 3169) por encima de 19 caracteres que valdría la pena pasar por el
   mismo criterio si el riel resulta angosto en la práctica; elegí estas dos como muestra de las
   más largas, no como lista exhaustiva.

Nada más resultó discutible: los términos fijos del glosario (idea, etapa, cliente, mundo,
Seguimiento, créditos, IA→AI, CEO, ISO, etc.) se usan de forma coherente en todo el lote, el
registro 해요체 es consistente (incluidas las etiquetas no imperativas, que reflejan
correctamente fuentes en español que tampoco son imperativas), no hay anglicismos crudos,
jerga de manual, rayas, ¿ ¡, comillas decorativas, emojis, saltos de línea ni puntos finales.

---

## ar — discutibles (revisión de naturalidad, segundo modelo)

Revisé las 3169 etiquetas (ar_01..04.out.json contra ar_01..04.json). La traducción es de muy
alta calidad: consistentemente traduce el sentido (no palabra por palabra), usa siempre el
registro pedido (imperativo plural de cortesía en ـوا y posesivo plural ـكم, nunca el masculino
singular), respeta longitud y prohibiciones de la voz, y distingue bien términos ambiguos del
español ("equipo" = equipo físico vs. equipo humano) según el contexto de cada nodo. No encontré
ninguna corrección evidente que hacer (ver ar_revision.json, vacío).

Solo hay un caso discutible, que además es el que el encargo pidió mirar con especial atención:

1. **`evaluar_proceso_completo_no_cada_metrica`** — ES: «Multiplica tus métricas, no las sumes»
   — AR actual: «اضربوا المقاييس ببعضها ولا تجمعوها» — Propuesta: «احسبوا حاصل ضرب مقاييسكم لا
   مجموعها» — Por qué: la traducción actual es correcta y un nativo la entiende bien porque el
   contraste con «ولا تجمعوها» (جمع = suma) activa de inmediato la lectura matemática de «اضربوا»
   (ضرب = multiplicar); no es un error. Pero «اضربوا» fuera de ese contexto inmediato es también
   el verbo común para «golpear/pegar», y en una etiqueta de riel —una frase corta, aislada, sin
   el título de apoyo a la vista— ese doble sentido es un riesgo real de primera lectura. La
   propuesta usa «حاصل ضرب» (el sustantivo «producto» matemático) en vez del verbo «اضربوا»,
   con lo que el registro matemático queda fijado desde la primera palabra («احسبوا» = calculen)
   y desaparece cualquier lectura violenta, sin perder el contraste multiplicar-vs-sumar que es
   el punto de la etiqueta.

Sobre `stage5_launch` (el otro caso que el encargo pidió mirar): ES «Instala y Opera tu Equipo» —
AR «ركّبوا معدّاتكم وشغّلوها». Está bien traducido: «Equipo» aquí es equipo físico (maquinaria,
título de apoyo «Etapa 5: Lanzamiento»), y el traductor usó correctamente «معدّاتكم» (vuestro
equipo/maquinaria), no «فريقكم» (vuestro equipo humano). No es discutible, lo confirmo como
correcto.

---

## Discutibles — revisión hi (hindi)

Solo 3 puntos suben al fundador. El resto de las ~3169 etiquetas se leyó natural,
fiel al español y dentro del registro pedido (आप, imperativo de cortesía); las
correcciones evidentes (51 casos, todas de un mismo patrón) ya están aplicadas en
`hi_revision.json` y se documentan aquí solo para que el fundador confirme el criterio.

1. **Decisión de término ya aplicada — काम (`kaam`) usado para "proyecto" en vez de परियोजना
   (`pariyojna`), el término fijo del glosario.** El traductor usó काम casi cada vez que la
   etiqueta española decía "Proyecto" (51 de 3169 casos, ids: `activity_list`,
   `carta_proyecto_calidad`, `cronograma_proyecto`, `project_scope_statement`, etc. — lista
   completa en `hi_revision.json`). El problema no es solo que काम no sea el término del
   glosario: काम **ya está asignado a "tarea"** en la misma tabla de términos fijos
   (`acción/tarea → कदम/काम`, `F3_CONVENCIONES.md`) y el propio traductor lo usa así en otras
   etiquetas (p. ej. `division_trabajo_humano_ia` → "...के बीच काम बाँटें", "reparte tareas").
   Es decir, काम terminaría significando "tarea" y "proyecto" a la vez en el riel, dos
   conceptos que la app distingue. Corregí los 51 casos a परियोजना (con los ajustes de
   género/concordancia que exige, परियोजना es femenino y काम es masculino). Vale la pena que
   el fundador lo confirme porque परियोजना es más formal/sánscrito que काम, que suena más
   cálido y cotidiano — es la típica tensión "la etiqueta enamora" vs. coherencia de glosario;
   con el glosario fijando el término, la resolví a favor del glosario.

2. **`valor_presente_franquicia_pvf` — la etiqueta española se contradice con su título, y el
   hindi (como la mitad de los otros idiomas) siguió el título, no la etiqueta.** Etiqueta:
   "Calcula el Valor Futuro"; título: "Valor Presente de una Franquicia (PVF)". Traducción
   actual: "फ्रैंचाइज़ी का मौजूदा मूल्य निकालें" ("calcula el valor **actual/presente** de tu
   franquicia") — sigue el título (Presente), no la etiqueta dada (Futuro). Al revisar los otros idiomas confirmé que esto no es un problema de hindi:
   en/fr/ja/ar también siguieron el título (presente/actual), mientras pt/de/it/zh/ko siguieron
   la etiqueta literal (futuro) — el lote se partió a la mitad porque la etiqueta española
   misma está mal (el concepto PVF es de valor presente, no futuro). No toqué esto en
   `hi_revision.json` porque no es un problema de la traducción hindi sino de la etiqueta
   española de origen: se debería corregir `es_04.json` (o el `.json` que corresponda) a
   "Calcula el Valor Presente" y luego re-derivar los 10 idiomas para ese id, o decidir cuál
   de las dos palabras es la correcta y unificar.

3. **`establecer_proyecto_y_metas_diseno` — ambigüedad de estructura que sobrevive a la
   corrección de término.** Etiqueta española: "Define Proyecto y Metas de Diseño" (dos cosas:
   el Proyecto, y las Metas de Diseño). Traducción corregida: "परियोजना और डिज़ाइन के लक्ष्य तय
   करें" — un hablante nativo puede leerlo como "define las metas de {proyecto y diseño}" en
   vez de "define el {proyecto}, y las metas de {diseño}", porque "के लक्ष्य" (los objetivos
   de) queda pegado solo al final de la cadena. Es ambigüedad menor y común en títulos cortos
   hindi, así que no la marco como evidente, pero si el fundador quiere que quede inequívoca,
   una alternativa más larga sería "परियोजना तय करें, डिज़ाइन के लक्ष्य भी" (más larga, pero más
   explícita, con la coma que ya se usa en otras etiquetas del lote).

Nada más llegó al nivel de discutible: el resto de las casi 3169 etiquetas (siglas como AI,
CEO, ISO, IT, HR, OSHA — todas de uso corriente en hindi técnico/de negocios y usadas con
coherencia — números, comas de separación de frases coordinadas, términos de glosario como
विचार/चरण/ग्राहक/मार्जिन/ब्रेक-ईवन बिंदु/दुनिया/टीम/जोखिम/गुणवत्ता/व्यवसाय) se aplicaron con
consistencia y sin errores de sentido, registro o mayúsculas detectables.
