# i18n F5: la IA en el idioma de la idea (hecha, pendiente del visto)

Rama `i18n`. Diseño: `DISENO.md §3.3, §5` y las decisiones D2 y D3. Añadidos del fundador del
25 sep 2026: los **idiomas fuera de los once** y el **conteo anónimo**. Commits `ccd91a19` (1) a
`c00f3570` (7) y el de este informe.

## Lo que hace falta del fundador
1. **Aplicar la migración 046** en el SQL Editor de Supabase:
   `supabase/migrations/my_idea_046_idioma_del_proyecto.sql`. Después, `my_idea_check_migraciones.sql`
   debe decir `046 ✓ OK`. Mientras no esté aplicada, todo funciona igual: las ideas se crean sin
   su idioma (se leen como español) y el conteo no se guarda. Queda un aviso en el log.
2. **El visto en la vista previa** (https://my-idea-git-i18n-alexs-projects-e8bf95b4.vercel.app),
   con la IA real, que la nube no puede usar. La prueba de DISENO §8 es una idea en **coreano** y
   otra en **árabe**: la entrevista, el plan y la Claridad deben salir en su idioma y con los
   nodos correctos. Vale sumar una en **ruso**, fuera de los once: la IA responde en ruso y la
   interfaz queda en el idioma que elegiste.
3. **Lo discutible de las etiquetas del riel**: `F5_DISCUTIBLES_RIEL.md`, lo que cada revisor dejó
   para tu decisión. Van de 0 a 10 casos por idioma.
4. **Tres dudas del español del grafo**, que la nube no toca porque `dataset/` no se toca:
   - `valor_presente_franquicia_pvf`: la etiqueta dice "Calcula el Valor **Futuro**", pero el
     concepto (título e id) es el valor **presente**. Los traductores se partieron: en, fr, ja, ar
     e hi siguieron el concepto; pt, de, it, zh y ko, la etiqueta. Cuando corrijas el español, se
     vuelve a derivar ese id en los diez idiomas.
   - `warrants_financiamiento`: "Usa Opciones para Bajar la Valoración" le aconseja al fundador
     bajar su propia valoración. El nodo explica que son los inversionistas quienes usan los
     warrants para bajarla. ¿La etiqueta debería avisar en vez de aconsejar? En inglés quedó
     "Know How Warrants Lower Your Valuation".
   - `modelos_negocio_mas_alla_del_lucro`: la etiqueta dice "sin Lucro", pero el concepto es "más
     allá del lucro".
5. Sigue pendiente la etiqueta **`web-v2.8.0`** (F3 y F4 en `main`): el proxy de git de la nube
   rechaza empujar etiquetas. Los pasos están en `RELEVO_NUBE.md §10`.

## Qué quedó hecho

### El idioma de la idea (1)
- `lib/i18n/detectarIdioma.ts` sigue el método del I Ching:
  - primero el **alfabeto**: gana el que tiene más letras;
  - en alfabeto latino, las **palabras vacías**, más un punto por las letras propias de un idioma
    (ñ, ã, ß, ę…);
  - en empate o sin señal, el **idioma de la interfaz**.
- Reconoce los once y además estos idiomas:
  - por su alfabeto: ruso, ucraniano, griego, hebreo, tailandés, persa, urdu, bengalí, tamil,
    telugu, gujarati, panyabí, canarés, malayalam, georgiano, armenio, amárico, jemer, lao, birmano
    y cingalés;
  - por sus palabras: neerlandés, polaco, turco, vietnamita, indonesio, rumano y sueco.
- Toda idea nueva nace por `lib/nacerIdea.ts` (session/start, organizer y organizer/stream). Ahí
  se detecta su idioma, se guarda en `projects.idioma` y suma uno al conteo.
- **Conteo anónimo** (`conteo_idiomas`, 046): mes, idioma de la idea, idioma de la interfaz y
  número de ideas. No guarda persona ni idea, ni una fecha más fina que el mes. Solo lo escribe
  service_role, con `contar_idioma_de_idea`. Para leerlo:
  `select * from conteo_idiomas order by mes desc, ideas desc;`
- Una idea de antes de F5 (sin idioma) se trata como **español**: la app solo hablaba español.

### La IA escribe en el idioma de la idea (2)
- Los prompts siguen fijos y en español, porque el caché de Anthropic depende de su prefijo. El
  idioma viaja en un **segundo bloque de sistema**, después del cacheado. En español no se agrega
  nada.
- Los ocho prompts del motor que escriben para la persona terminan con la regla **IDIOMA DE
  SALIDA** (editada en `engine/prototipo_motor.py` y sincronizada): intérprete, pregunta dirigida,
  plan, estado vivo, organizador, reporte, clasificación de la oferta y diagnóstico de mundo. Los
  nativos que la llevan son el reformulador de protección y el nuevo de preguntas. Los de JSON
  interno no cambian. Una guardia lo exige.
- El idioma de la idea llega a la entrevista (en el estado de la sesión), al plan, al estado vivo,
  a la Claridad, al reporte, al diagnóstico y al anclaje de protección.
- Qué idioma sigue cada cosa:
  - Lo que escribe la IA sigue el idioma de la idea.
  - Lo que arma el código sin IA sigue el idioma de la idea si es de los once, y si no el de la
    interfaz (`idiomaDePlantilla`).
  - La interfaz, sus botones y el **riel** (que es navegación) siguen la cookie (D2).

### Los marcadores neutros (3)
- El plan se **guarda** siempre con sus rótulos de estructura en español: "## Etapa N:",
  "**Pasos:**", "**Entregable:**", "**Esta semana:**", "**El lunes que viene:**", la sección de
  números, "_Plan completo_" y "## Lo que este plan aún no cubre". Son las claves que leen el
  checklist y la pantalla. El contenido va en el idioma de la idea.
- Si la IA traduce un rótulo, `neutralizarRotulos` lo devuelve a la forma neutra antes de guardar.
  La pantalla lo **pinta** en el idioma de quien lee (`pintarRotulos`), con las palabras de los
  catálogos y los dos puntos de cada idioma.
- El detector de acentos solo mira planes en español. La red del diagnóstico reconoce "esta
  semana" y las etapas en los once idiomas.

### Las plantillas sin IA (4)
- La nota al pie y la unidad de cada número del reporte salen en el idioma de la idea.
- El "dame mi plan" del respaldo se reconoce en los once idiomas. Quedan fuera las palabras
  ambiguas entre idiomas: "pronto" y "ja".
- El plan sin IA, la Claridad y lo que falta ya salían del catálogo; ahora reciben el idioma.
- **Se quedan en español a propósito** el bloque "Mi realidad medida" y el mensaje de seguimiento.
  Son **entrada de la IA**, ninguna pantalla los lee, y la regla 8-bis del plan los nombra por su
  rótulo. La IA responde igual en el idioma de la idea.

### D3: el riel y las preguntas (5 y 7)
- **Las etiquetas del riel en los diez idiomas**: 3169 por idioma en `lib/i18n/etiquetas/`, sin
  tocar el grafo.
  - Cada idioma lo tradujo un modelo con las convenciones de F3 y lo revisó un segundo modelo.
  - Lo evidente quedó aplicado, entre otras cosas:
    - un intercambio de dos etiquetas en coreano;
    - "proyecto" en hindi vuelve a परियोजना, porque काम ya es "tarea" en el glosario;
    - "ton monde" en francés chocaba con el término de los mundos;
    - una elisión y una tilde en italiano;
    - una preposición en alemán;
    - un sentido invertido en inglés.
  - `scripts/i18n/etiquetasRiel.ts` exporta **solo las que faltan**, valida y aplica.
  - La guardia `etiquetasRiel.test.ts` exige que todo nodo vivo tenga su etiqueta en cada idioma.
    Cuando cambie el grafo, falla hasta que se traduzcan las nuevas.
- **Preguntas fuera del español**: la pregunta cacheada (en español) la expresa Haiku en el idioma
  de la idea (`SYSTEM_TRADUCIR_PREGUNTA`), y queda como pendiente. Si la IA falla, queda la
  cacheada.
- La **pregunta genérica** ahora nombra el tema por su **etiqueta** y no por el `titulo_concepto`,
  por la regla "la etiqueta enamora" (AGENTS.md).

### El remedio de F1 (6)
- En una idea escrita en otro idioma, la brújula busca con la respuesta (o el perfil) **traducida
  al español** por Haiku. Es la misma letra que se midió en F1: en inglés, de 2,80 a 7,40
  candidatos sobre el umbral.
- Si la traducción falla, se busca con el original y queda el evento `consulta_sin_traducir`.
- En español no hay llamada extra.

## Lo que queda para F6 (no es un olvido)
- **Los documentos descargables** (Expediente, bitácora, informe, acta, registro) siguen en el
  idioma base, como dice la ruta desde F2. F6 los pasa al idioma de la idea. La herramienta ya
  existe: `pintarRotulos` para el plan que va dentro.
- La elisión del italiano ("l'8 marzo"), los correos (D4), los legales (D5), el SEO y los `hreflang`
  (D9).
- Dos respaldos siguen leyendo palabras en español. Solo actúan cuando la IA falla, y en otro
  idioma degradan en silencio:
  - las palabras clave de `familiasDesdeEncabezados`, que se usan solo si falta la
    autodeclaración del plan;
  - las listas de `readiness.ts`.

## Verificación
- Se probaron en rojo primero la detección (con cada caso contado a mano), el almacenamiento con y
  sin la 046, el conteo, la regla de idioma en cada llamada, los rótulos (ida y vuelta en los diez
  idiomas), las plantillas, las preguntas y el remedio.
- Suites web y motor, tsc, lint, build y Gate 0 en verde en cada commit.
