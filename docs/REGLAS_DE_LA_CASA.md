# Reglas de la casa

**Índice único de todas las reglas del producto:** de contenido, de producto y de método. Encargo del fundador del
28 sep 2026 (auditoría final, punto 4).
- Cada regla lleva su origen (quién la decidió o qué incidente la trajo), su fecha y dónde se cumple: una guarda o una
  prueba que muerde, un script, un documento, o "lectura" si no la hace cumplir nada automático.
- El desarrollo de las reglas del 28 sep 2026 (las numeradas R1 a R6) sigue más abajo, íntegro.
- Los detalles de proceso siguen en `AGENTS.md`, la voz y el copy en `docs/BANCO_DE_TEXTOS.md` y el protocolo del
  auditor en `docs/loop/AUDITOR.md`: este índice los cita, no los sustituye.

**Fechas:** la de una decisión es la de su commit (`docs/PENDIENTES.md:6-17`). Las decisiones que el texto fecha el
"25 sep", el "26 sep" y el "27 sep" se tomaron con el reloj marcando el 24 sep; aquí se citan como están escritas.

**Las guardas de contenido, como datos:** `dataset/metadata/guardas_contenido.json`, con versión. Se genera desde
`web/lib/guardasContenido.ts` y `guardasContenido.test.ts` impide que diverjan. La forja lo copia para limpiar un pack
con la misma vara que el catálogo.

## Reglas duras (fundador, 30 sep 2026): mandan sobre todas las demás

| # | Regla | Origen | Fecha | Se cumple en |
|---|---|---|---|---|
| D1 | **JAMÁS un usuario debe saber, ni poder intuir, de dónde provienen las respuestas de la app.** Todo origen es control interno: ni títulos, ni autores, ni estudios, investigaciones o expertos como respaldo, ni etiquetas de procedencia, ni el año de una fuente. Las fusiones producen textos que no aparecen literalmente en ninguna fuente, y es correcto: el sistema toma lo mejor de todo y lo convierte en accionable | Fundador, tras el informe de la auditoría final | 30 sep 2026 | `web/lib/procedencia.test.ts` (guarda única de procedencia, once idiomas), `REGLA_SIN_FUENTES` en toda llamada a la IA, el aplicador de correcciones rechaza un prefijo de procedencia |
| D2 | **NINGUNA COPIA FIEL:** los libros se convierten en NODOS DE CONOCIMIENTO; ningún texto de nodo es una copia ni una traducción palabra por palabra de un pasaje de un libro | Fundador | 30 sep 2026 | la política de corrección (C32, R8: devolver es devolver el sentido, no el pasaje); la comprobación de copias de la auditoría final (umbral 0) y la medida 2 |
| D3 | **NINGÚN nodo vivo y funcional se retira** | Fundador | 30 sep 2026 | lectura: ningún remedio retira un nodo vivo; un problema de un nodo se corrige en su texto |
| D4 | **TODO lo que presenta la app es consejo de My Idea**, aunque se apoye en fuentes. Ningún texto lleva "Sugerencia de My Idea" ni otra marca de origen; las fuentes y su registro son solo control interno. Un consejo práctico que no está en el libro **no es un defecto**: es consejo de la casa. Sigue siendo defecto la **invención dura**: un hecho, una cifra, una causa, un plazo, una norma o un resultado prometido que no está respaldado | Fundador | 1 oct 2026 | R7 (sin la clase "paso sin marca"); el aplicador rechaza un prefijo de procedencia; la medida final mide contrarios, invenciones duras y procedencia |
| D5 | **Procedencia de los métodos:** los métodos se nombran y se explican (los cinco porqués, el ciclo PDCA, el diagrama de Ishikawa): son conocimiento común y válidos. **Nunca se atribuyen:** ni "según Deming", ni "de acuerdo con", ni "como propone tal autor", ni títulos de libros. Si un método tiene nombre neutro, se usa ese ("ciclo PDCA" en vez de "ciclo de Deming"). "Los estudios muestran" y similares se reescriben diciendo el consejo directamente | Fundador | 1 oct 2026 | `web/lib/procedencia.test.ts` (secciones 6 y 7: atribuciones genéricas y métodos con persona), `REGLA_SIN_FUENTES` |

## A. Contenido (el dataset y el texto de los nodos)

| # | Regla | Origen | Fecha | Se cumple en |
|---|---|---|---|---|
| C1 | Ni libros ni autores ante el cliente; las fuentes son metadato interno (el método se nombra y se explica, nunca se atribuye, y con su nombre neutro si lo tiene: D5, 1 oct 2026) | Fundador, "regla estricta", tras un aviso "Según [libro]" publicado (AGENTS.md) | 26 sep 2026; ampliada el 27 sep (nada interno al navegador) | `web/lib/procedencia.test.ts` (guarda única de procedencia, 30 sep 2026), `engine/test_fuentes_internas.py` |
| C2 | Sin voz de libro ni de exposición ("el libro", "el texto", "el autor", "como se ilustra en el caso", "a la fecha de la fuente") | Extensión de C1 por el fundador; auditoría final | 28 sep 2026 | `vozDeLibro` en `web/lib/i18n/frasesProhibidas.ts`, `web/lib/vozDeCliente.test.ts`, `web/scripts/saneamiento/vozDelPack.ts` |
| C3 | Nada interno en el texto de cara: ni rutas, ni números de línea, ni marcas de auditoría (tampoco "Puntero jurisdiccional"); `notas_extraccion` es interno | Fundador (integración del mundo 11); auditoría final | 28 sep 2026 | `marcasInternas`, `web/lib/vozDeCliente.test.ts`, `engine/test_notas_extraccion_internas.py` |
| C4 | La persona ve la `etiqueta_arbol`, nunca el `titulo_concepto`, que no se pinta ni se modifica | La primera idea beta mostraba "MVP" y "Earlyvangelists" (BANCO) | jul 2026; reafirmada el 26 sep | `web/lib/etiquetasCara.test.ts`, `etiquetaArbol` en `web/lib/engine/graph.ts` |
| C5 | Diccionario de la casa: la jerga se traduce por función; el nombre de una metodología vive en el nodo, no en la etiqueta; lista corta de siglas exentas | Curaduría del auditor (BANCO) | jul 2026 | `web/lib/etiquetasCara.test.ts` |
| C6 | Cero guiones largos o medios | BANCO §3 | sin fecha | `raya` en frasesProhibidas, `web/lib/voz.test.ts`, el aplicador de correcciones los rechaza |
| C7 | Ortografía y tildes correctas siempre; "…" como carácter; ¿ y ¡ solo en español | BANCO; convenciones de i18n F3 | 24 sep 2026 | `puntosSuspensivos`, `signosInvertidos`, `web/lib/i18n/ortografiaEs.test.ts`, `web/scripts/chequeo_acentos_canon.ts`; en los nodos, lectura (la auditoría final midió 19,5 % con faltas) |
| C8 | La moneda son créditos, jamás "tokens" | BANCO | sin fecha | `monedaTokens` |
| C9 | Tuteo a una sola persona; plural solo si declara equipo; nunca usted, vosotros ni voseo | BANCO; R3 | sin fecha; voseo cancelado el 28 sep | `tuteoSingular`; el adaptador de preguntas (R1) |
| C10 | Cero jerga de manual cruda (MVP, pivot, earlyvangelists, stakeholder…) | BANCO | sin fecha | `jergaCruda`, `web/lib/etiquetasCara.test.ts` |
| C11 | Espejo, jamás regaño: ni "vas tarde" ni "no cumpliste"; lo tardío en ámbar | BANCO; AUD-09 M38 | sin fecha | `reproche` |
| C12 | Estados de tarea con su vocabulario (sin empezar, apenas empezada, en proceso, hecha, no aplica); nunca "a medias" | BANCO | jul 2026 | `aMedias` |
| C13 | Glosario: un concepto, un nombre, en español neutro ("a tu cargo", "director general"; fuera "coger", "coche", "móvil"…) | Orquestador del mundo 11; la auditoría final lo aplica a todo el catálogo | 28 sep 2026 | `docs/saneamiento/resultados/M11/glosario/DECISIONES.md`, en `guardas_contenido.json`; lectura |
| C14 | Fidelidad: nunca lo contrario de la fuente; los añadidos de cifra, plazo o norma salen; lo práctico útil de la casa se queda (desde el 30 sep 2026 sin prefijo visible: su constancia va al registro interno, D1) | Mandato del fundador (campaña de fidelidad) | 24 sep 2026 | `scripts/fidelidad/aplicar_correcciones.py`, `engine/test_aplicar_correcciones_fidelidad.py`; la muestra ciega de la auditoría final |
| C15 | Corrección declarada, nunca borrado: el texto viejo queda en `correcciones` con su veredicto y su cita | Regla 8 del ejecutor; M11 | ago 2026; 24 y 28 sep | `scripts/fidelidad/aplicar_correcciones.py`, `scripts/saneamiento/aplicar_aristas.py`, `engine/test_correcciones_mundo11.py` |
| C16 | Cero invención: ni pasos ni cifras nuevos; una reescritura de voz no alarga | M11; taller de re-voz | ago 2026; 28 sep | `engine/test_cifras.py`; lectura ciega |
| C17 | Marco contra país: clases A, B y C declaradas; toda entrada de jurisdicción con país y clase | Texto ratificado por el fundador (`docs/POLITICA_MARCO_PAIS.md`) | 26 sep 2026 | `engine/test_jurisdiccion.py`, `scripts/auditoria_final/navegacion.py` |
| C18 | Regla de la cifra: la de mercado sale; la que es norma se queda en su nodo-frontera | `docs/POLITICA_MARCO_PAIS.md` | 26 sep 2026 | lectura |
| C19 | Regla del empleo: contratar, pagar y despedir se enseñan como método, nunca como norma de un país | `docs/POLITICA_MARCO_PAIS.md` | 26 sep 2026 | lectura |
| C20 | Preguntas base intocables; la neutral, en campo aparte; el generador solo añade | R3 | 28 sep 2026 | `engine/test_generador_neutrales.py`, `web/lib/engine/cacheNeutrales.test.ts` |
| C21 | Ningún nodo se quita ni se salta por el papel de la persona | R3 | 28 sep 2026 | lectura |
| C22 | La adaptación cambia la forma, nunca el fondo; sin roles supuestos; la salida segura es neutral, nunca la base cruda | R1 | 28 sep 2026 | `web/lib/engine/adaptadorPregunta.test.ts`, `web/lib/engine/adaptadorEnTurno.test.ts`, `engine/test_question_cache_roles.py`, `web/lib/engine/preguntasEmprendedor.test.ts` |
| C23 | Se nombra el mundo, nunca su clave técnica | BANCO | Fase 4.2 | lectura |
| C24 | Severidad en palabras, jamás en puntajes | BANCO | ago 2026 | `web/lib/registroProteccion.test.ts` |
| C25 | Murallas de dominio: ninguna arista entre dos mundos; un mundo solo toca el núcleo, por sus puentes; ley del ancla (2 puentes por ancla y mundo) | AUD-08; AUD-09 M16; auditoría final | 25 y 28 sep 2026 | `scripts/auditoria_final/navegacion.py`, `engine/test_puentes_tejidos.py` |
| C26 | Alcanzabilidad: todo nodo vivo se alcanza desde las puertas de su mundo (o las semillas del núcleo) | Auditoría final | 28 sep 2026 | `scripts/auditoria_final/navegacion.py`, Gate 0 (`scripts/run_phase1.py`) |
| C27 | Puerta legítima: una situación que la persona cuenta y que ningún nodo produce; los aparcados no se borran | Fundador (mundo 11) | 28 sep 2026 | `engine/test_importar_forja_aparcados.py` |
| C28 | El catálogo no se borra; los datos personales sí (borrar la cuenta borra de verdad) | Fundador | 26 sep 2026 | `web/app/api/cuenta/eliminar/borradoCompleto.test.ts` |
| C29 | Frontera OPERATIVO / INVENCIÓN: lo operativo concreta el cómo sin afirmar nada nuevo y se queda. Desde el 30 sep, lo que no es operativo se clasifica en cuatro clases con su umbral: contrario (0), invención dura (0) y certeza endurecida (cuenta como matiz; 0,2 por nodo). La clase "paso práctico sin marca" se eliminó el 1 oct 2026 (D4): un consejo práctico de la casa no es defecto | Fundador, tras la auditoría final (dos pasos que la campaña dio por OPERATIVOS y el árbitro por invención); clases nuevas tras la muestra de parada de la etapa 1 | 28 sep 2026; clases el 30 sep | lectura ciega con árbitro (etapa 1 del remedio); detalle en R6 y R7 |
| C30 | Las etiquetas llevan mayúscula de rótulo en las palabras con peso ("Traza tu Plan de Exportación"): es estilo de la casa, no falta de ortografía | Fundador (3.541 de 3.634 etiquetas ya lo usaban, sin regla escrita) | 28 sep 2026 | lectura; los lectores de ortografía no lo cuentan como falta |
| C31 | Cada puerta de un mundo entra con su pregunta de ENTRADA propia (`pregunta_entrada`, campo aparte), que parte del concepto de la puerta y de la situación que la persona cuenta; la base no se toca; se verifica a ciegas con trampa sin marca | Fundador, tras la auditoría final (las bases miraban al siguiente concepto) | 28 sep 2026 | `web/lib/engine/puertasMundo.test.ts`, `web/lib/engine/preguntaEntrada.test.ts` |
| C32 | Una corrección prefiere QUITAR lo que sobra o DEVOLVER el SENTIDO y el TÉRMINO PRECISO del libro (un "puede", una condición, un plazo), nunca copiar ni traducir un pasaje palabra por palabra (D2); solo redacta frase nueva cuando no hay otra forma, y esa frase se verifica a ciegas contra el libro antes de aplicarse | Fundador, tras la muestra de parada de la etapa 1 (15 de 39 invenciones estaban en textos ya corregidos) | 30 sep 2026 | el árbitro declara el `modo` de cada corrección; verificador ciego y `tanda_e1b.py` en las claves del remedio; detalle en R8 |

## B. Producto (lo que la app hace, promete y cobra)

| # | Regla | Origen | Fecha | Se cumple en |
|---|---|---|---|---|
| P1 | Los precios viven solo en `precios.ts`; todo lo demás los refleja | Una tabla de Design decía "Seguimiento: Gratis" (AGENTS.md) | 17 jul 2026 | `web/lib/preciosViejos.test.ts`, `conceptoDelPlan` en `web/lib/precios.ts` |
| P2 | El crédito paga el trabajo del motor; lo determinista y el registro de avance son gratis | Palabra del fundador | 17 jul 2026 | lectura (`docs/FLUJO_TRACKING.md` §5) |
| P3 | Catálogo congruente: plan 10; seguimiento, mundo y replanteamiento 5; Tus Números incluido | Fundador (catálogo congruente) | jul 2026; replanteamiento el 27 sep | `web/lib/precios.ts`, `web/lib/creditos.test.ts` |
| P4 | Solo se cobra lo entregado: se aparta al empezar, se cobra al entregar, se libera si falla; un plan sin IA no se cobra | Fundador (AUD-09) | 25 sep 2026 | `creditosReserva.test.ts`, `avisoPlanBasico.test.ts`, `regenerarPlanBasico.test.ts` |
| P5 | Ninguna afirmación de dinero sin su evento en el libro de créditos | Fase 4.3.2 | Fase 4.3.2 | `web/lib/apiSesion.ts` (`creditos_devueltos`) |
| P6 | Registro de claims: ni "cero alucinación" recortado, ni "reemplaza a un consultor", ni cifras de mercado; "gratis" solo para Claridad y diagnósticos | BANCO | sin fecha | `claimsNoUsar`, `reemplazaConsultor` |
| P7 | El precio se dice al generar; todo botón que cobra dice su precio | BANCO | ago 2026 | `lenguajeMuerto`, `contratoUniforme.test.ts` |
| P8 | Fronteras de alcance: no es asesoría legal, fiscal, contable ni técnica; no certifica | BANCO §4 | sin fecha | lectura; `reemplazaConsultor` |
| P9 | El texto no promete una función que falta | Fundador | 25 sep 2026 | `promesasDeCopy.test.ts`, `expedienteDiceLoQueIncluye.test.ts` |
| P10 | Nada se borra jamás en el producto: un sello de compra, un cierre o un diagnóstico no se pierden | AUD-09 H04 | 25 sep 2026 | `web/lib/apiSesion.test.ts` |
| P11 | La historia no se reescribe: la fecha original se conserva; un ciclo nuevo no borra el anterior | BANCO; AUD-09 M04 y M34 | jul y 25 sep 2026 | `actaCierre.test.ts`, `historiaCiclos.test.ts` |
| P12 | El cierre es soberano: nunca exige el 100 % y lo pendiente es testigo, no deuda | BANCO; FLUJO_TRACKING §8 | Fase 4.0 y 4.2 | `CierreHonesto.test.ts` |
| P13 | El usuario decide qué corre: "no aplica" sale del denominador | BANCO | jul 2026 | `cuentaHonesta.test.ts` |
| P14 | Todo separado: cada espacio se mide solo; la única vista global es el Expediente | Veredicto del fundador | 4 ago 2026 | `espacioSinContagio.test.ts`, `analisisPapelSinMezcla.test.ts` |
| P15 | Una sesión de mundo no cruza a otro mundo (sí pasa por el núcleo) | AUD-09 M16 | 25 sep 2026 | `dominiosDelRecorrido` en `web/lib/engine/recorrido.ts` |
| P16 | El enlace jamás es fusión: un mundo lee el núcleo y nunca lo escribe | BANCO | ago 2026 | `snapshotProyecto.test.ts` |
| P17 | Memoria de contexto de principio a fin | R2 | 28 sep 2026 | `memoria.test.ts`, `redactorPlan.test.ts`, `textoTarea.test.ts` |
| P18 | El caché de la IA tiene un orden fijo | R4 | 28 sep 2026 | `costmeter.cache.test.ts`, `idiomaSalida.test.ts` |
| P19 | La prioridad declarada manda, en código | Fundador (contexto de la entrevista) | 28 sep 2026 | `interpretePrioridad.test.ts`, `prioridadPuertas.test.ts` |
| P20 | Fallar ruidoso, jamás mentir calladito: ninguna degradación silenciosa, ningún stream mudo | BANCO §9; AUD-09 | 25 sep 2026 | `degradacionesMudas.test.ts`, `rastroDeEscrituras.test.ts` |
| P21 | Si cae el contador de ritmo, la app falla cerrada: no cobra y suelta la reserva | Fundador | 25 sep 2026 | `upstashCaido.test.ts` |
| P22 | Confidencialidad de la mecánica: nunca conteos, nodos ni grafo ante el usuario | BANCO | jul 2026 | lectura |
| P23 | Ninguna llamada a la API real hasta la corrida final; la coherencia y el vuelo se corren una vez, juntos | Fundador | 28 sep 2026 | `docs/producto/CORRIDA_FINAL.md` |

## C. Método (pruebas, commits, auditorías y lectura)

| # | Regla | Origen | Fecha | Se cumple en |
|---|---|---|---|---|
| M1 | El cálculo canónico se escribe a mano antes del assert | Hotfix v2.1.1 (AGENTS.md) | v2.1.1 | convención en las cabeceras de las pruebas; lectura |
| M2 | Ningún test cambia de veredicto por los secretos del entorno | Hotfix v2.2.2 (AGENTS.md) | v2.2.2 | lectura |
| M3 | Ningún commit con una suite en rojo, ni con tsc en rojo | AGENTS.md; AUD-09 | ago y 25 sep 2026 | `.githooks/pre-commit`, `engine/run_all_tests.py` |
| M4 | Ninguna credencial versionada; la filtrada se rota el mismo día | Fase 3.2 (AGENTS.md) | Fase 3.2 | lectura |
| M5 | El proyecto del bridge se llama `i-have-an-idea` | AGENTS.md | sin fecha | lectura |
| M6 | Prueba en rojo primero, y prueba por la entrada real en toda capa que consume | AUD-09 | 4 sep 2026 | `analyticsEntrada.test.ts`; lectura |
| M7 | Un verde que no ejercita el escenario es peor que un rojo; todo patrón nace con dos fixtures | BANCO §9 | Fase 4.2 | `engine/test_fixtures_de_patrones.py` |
| M8 | La prueba de rumbos acompaña toda regeneración del índice semántico | Fundador | ago 2026 | `engine/test_prueba_rumbos.py` |
| M9 | Toda cifra lleva su fecha de corte y sale de una corrida del instrumento, no de memoria | BANCO 9.10, 9.17 y 9.21; `docs/loop/AUDITOR.md` | ago y sep 2026 | lectura |
| M10 | Nada se borra en los documentos de gobierno: lo viejo se tacha o se corrige por declaración | `docs/loop/AUDITOR.md` | sep 2026 | lectura |
| M11 | El merge a main es del fundador, con su visto | `docs/loop/AUDITOR.md` | ago 2026 | lectura |
| M12 | Trampas sin marca, bajo ids reales, plantadas antes de generar cualquier contexto de lectura; la clave, fuera de lo que leen los agentes | Fallos de método del mundo 11 | 28 sep 2026 | `docs/auditoria_final/` y `docs/saneamiento/resultados/M11/`; lectura |
| M13 | El umbral y la semilla se escriben antes de medir, y no se cambian después | Fundador (mundo 11 y auditoría final) | 28 sep 2026 | `docs/ACTA_SANEAMIENTO_FINAL.md` (commit 800736a7, antes de medir) |
| M14 | Lectura ciega, árbitro independiente y, si un lector no caza su trampa, segunda lectura del lote | Mundo 11; auditoría final | 28 sep 2026 | `docs/auditoria_final/INSTRUCCIONES_*.md` |
| M15 | Toda rúbrica que juzga preguntas mira papeles y contexto | R5 | 28 sep 2026 | `desajustes_de_papel` en `web/lib/engine/juezSesion.ts` |
| M16 | La fecha de una decisión es la de su commit | `docs/PENDIENTES.md:6-17` | 24 sep 2026 | lectura |
| M17 | Un libro nuevo entra a `fuentes_canonicas.json` antes que su primer nodo; toda fusión corre `fuentes_internas.py` | AGENTS.md | 26 y 27 sep 2026 | `engine/test_fuentes_internas.py` |
| M18 | Las migraciones las aplica el fundador; aplicada, va a main sola (solo SQL) con su verificador | Fundador | sep 2026 | `supabase/migrations/my_idea_check_migraciones.sql` |

**Choques y huecos que este índice deja a la vista, sin resolver aquí:**
- ~~**El BANCO contradice C1:** varias secciones siguen diciendo que el plan cita libro y capítulo (§3, §5, §6, §7.1),
  y eso choca con C1 y AGENTS.md. Hay que actualizar el BANCO.~~ **Resuelto el 28 sep 2026** (decisión del fundador):
  los seis pasajes del BANCO quedan tachados con su corrección declarada y el claim "cada plan cita su fuente" pasa a
  PROHIBIDO en §6. Se comprobó que ningún prompt pide citar libro, capítulo ni autor (`prompts.json`: `SYSTEM_PLAN`
  dice "sin autores" y prohíbe "fuentes nuevas que no esten en el material").
- **Reglas sin guarda automática:** C18, C19, C21, C23, P2, P8, P22, M2, M4, M5, M9 a M11 y M16 se cumplen solo por
  lectura.
- **Reglas que la auditoría final mide y no cumplen hoy:** C7 (ortografía) y C14 (fidelidad) en los 10 espacios que no
  pasaron el método del mundo 11 (`docs/ACTA_SANEAMIENTO_FINAL.md`, sección 6).

---

# Desarrollo de las reglas del 28 sep 2026 (R1 a R5)

## R1. Las preguntas de la caché son PREGUNTAS BASE, no ley

**Decisión del fundador con el auditor, 28 sep 2026.**

Las preguntas guardadas en `preguntas_cache.json` son preguntas base: dicen QUÉ hay que averiguar en ese punto del
camino para elegir el siguiente paso. No son el texto que la persona tiene que leer.

- **La adaptación cambia la FORMA, nunca el FONDO.** Se ajustan el papel (dueña, empleado, directivo), el contexto
  (tamaño del equipo, sector, etapa) y las palabras de la persona. La pregunta adaptada tiene que buscar lo mismo que
  la base: si una respuesta a la adaptada no serviría para elegir entre los mismos siguientes pasos, la adaptación está
  mal.
- **Nunca se suponen roles ni estructuras que la persona no mencionó.** Si la base supone un jefe, un departamento de
  recursos humanos o varios niveles de mando y la persona es dueña de su negocio, se adapta a quien cumple ese papel en
  su caso o se pregunta en condicional.
- **La salida segura, si la adaptación falla, es una versión NEUTRAL sin roles supuestos, nunca la base cruda.** Una
  pregunta que le habla de "tu propio jefe" a una persona que no lo tiene rompe la conversación más que una pregunta
  sencilla.

**Por qué:** en el vuelo del 27 sep 2026 la entrevista del mundo 11 le preguntó a un dueño de taller por su propio
jefe y por recursos humanos. El fallo no era del dataset ni del mundo: era de los prompts y de la secuencia, y afecta
a todos los mundos. El diagnóstico está en `docs/producto/CONTEXTO_ENTREVISTA.md`.

**Dónde vive:** el adaptador (`web/lib/engine/adaptadorPregunta.ts`), la versión neutral en el campo aparte
`pregunta_neutral` de la caché (`engine/build_question_cache.py --neutrales`) y la regla única que viaja en toda
llamada a la IA (`web/lib/reglaContextoUsuario.ts`).

## R2. Memoria de contexto de principio a fin

**Principio 1 del fundador, 28 sep 2026.**

El contexto completo de la persona viaja siempre: en cada turno, en cada llamada a la IA, al pasar de una sesión a otra
y al abrir cada mundo, que recibe todo lo del núcleo y de los mundos anteriores. Se guarda en la base del proyecto y se
actualiza en cada turno.

- **La ficha de contexto** (papel, si tiene jefe, equipo, sector, etapa, prioridad declarada y frases textuales) la
  actualiza el intérprete en la misma llamada de cada turno. Un dato desconocido nunca pisa uno conocido; las frases
  solo se añaden.
- **El hilo** guarda cada pregunta y cada respuesta de todas las sesiones, en orden, solo añadiendo.
- **Al abrir una sesión** se fija la foto del proyecto (idea, estado vivo, ficha e hilo), y la ficha de ese momento
  viaja aparte en cada turno. La prioridad declarada también pasa de una sesión a la siguiente.
- **Ninguna salida de la IA se guarda cortada:** toda llamada mira si se quedó sin tokens, reintenta con más o falla
  con aviso. Las tareas del checklist se guardan completas y solo se acortan al mostrarlas.

**Por qué:** en el vuelo del 27 sep 2026 el intérprete perdía la idea y el perfil desde el segundo turno, y un mundo
nuevo no sabía nada de lo que la persona había contado en el núcleo.

**Dónde vive:** `projects.memoria` (migración 049), `web/lib/engine/memoria.ts`, `anotarEnMemoria` en `web/lib/db.ts`.

## R3. Nada se elimina ni se cambia

**Principio 2 del fundador, 28 sep 2026.**

- **Ningún nodo se quita ni se salta por el papel de la persona:** todos se adaptan.
- **Las preguntas base de la caché se quedan EXACTAMENTE como están.** Las versiones neutrales van en un campo aparte.
  Nada regenera una base: el generador solo añade (`--faltantes`, `--neutrales`) y `--patch` ya no pisa una base.
- **Los nodos con siguientes y sin pregunta** reciben una nueva, que se AÑADE.
- **Queda cancelada la regeneración de las preguntas en voseo:** el adaptador las dice en tuteo neutro al momento, y
  su versión neutral también.

**Por qué:** una pregunta base guarda una intención que costó construir. Si se regenera, se pierde; si se adapta al
decirla, se conserva y además le habla a la persona real.

## R4. El caché de la IA tiene un orden fijo

**Principio 3 del fundador, 28 sep 2026.**

Toda llamada va en el mismo orden: primero lo fijo (el prompt, la regla sin fuentes y la regla única), después el
contexto del proyecto (la foto y la ficha), después el turno. El historial crece solo por el final.

- **Lo fijo y el contexto del proyecto, con caché de 1 hora. El resto, con caché de 5 minutos.**
- **Por qué 1 hora ahí:** escribir en el caché de 1 hora cuesta 2 veces la entrada normal; en el de 5 minutos, 1,25
  veces; leer cuesta 0,1. Una sesión tiene entre 4 y 13 turnos (vuelo del 27 sep 2026), y entre turno y turno la
  persona piensa y escribe. Con 5 minutos, cada pausa más larga obliga a reescribir el prefijo (1,25 veces cada vez).
  Con 1 hora se paga 0,75 de más una sola vez. Basta una pausa larga en la sesión para que la hora salga más barata, y
  el prefijo se reutiliza en todos los turnos.
- **Por qué 5 minutos en el historial:** su final cambia en cada turno, así que se vuelve a escribir en cada turno de
  todas formas. Pagar el doble por una escritura que el turno siguiente ya deja atrás no compra nada.
- **Cada llamada deja registro** de sus tokens leídos del caché y escritos en él (1 hora y 5 minutos), y `costo_usd`
  los cobra con su tarifa.

**Dónde vive:** `web/lib/costmeter.ts` (`CACHE_1H`, `registrarUso`, `costoLlamadaUsd`) y
`web/lib/i18n/idiomaSalida.ts` (`bloquesDeSistema`).

## R5. Toda rúbrica que juzga preguntas mira papeles y contexto

**Decisión del fundador, 28 sep 2026.**

Toda verificación de preguntas, sea un juez automático o una lectura ciega, mira además si la pregunta supone un papel
o una estructura que la persona no tiene: un jefe a quien es dueña de su negocio, recursos humanos, directivos, varios
departamentos, un equipo a quien trabaja sola. Una pregunta así es un fallo aunque parta bien del nodo y sirva para
elegir el siguiente paso.

**Por qué:** la verificación ciega de las preguntas de puerta del mundo 11 dio por buena la pregunta de "tu propio
jefe": miraba si partía de la situación del nodo y si servía para elegir, pero no los papeles.

**Dónde vive:** el juez de sesión (`desajustes_de_papel` en `SYSTEM_JUEZ_SESION`) y el juez de la prueba de coherencia.
Toda rúbrica nueva que juzgue preguntas lo lleva desde el primer día.

## R6. La frontera entre lo operativo y la invención

**Decisión del fundador, 28 sep 2026**, tras la medida 1 de la auditoría final: la campaña de fidelidad dio dos pasos
por OPERATIVOS con dos lecturas y el árbitro de la auditoría los dio por invención. Desde hoy la frontera está escrita
y la usa toda la etapa 1 del remedio.

- **OPERATIVO:** concreta el CÓMO (el orden, el formato, una herramienta común) sin afirmar nada nuevo. **Se queda.**
- **INVENCIÓN:** añade un QUÉ, un POR QUÉ o un CUÁNTO que el libro no dice (un hecho, una causa, una cifra, un plazo,
  un resultado prometido), o **endurece** lo que el libro dice con cautela. **Sale**, o se queda como paso de la casa
  si es un consejo práctico útil. Desde el 30 sep 2026 (D1) el paso de la casa no lleva prefijo visible: su constancia
  va al registro interno de correcciones (veredicto CASA).

**Los dos casos que la fijaron** (tanda `final-frontera`):
- "esas pepitas de oro que valen más que cualquier encuesta": la comparación con las encuestas es un QUÉ nuevo. Sale.
- "materiales reciclados o recuperados como insumo principal": "principal" endurece un consejo que el libro da con
  cautela. Sale.


## R7. Las clases de defecto contra el libro y sus umbrales

**Decisión del fundador, 30 sep 2026**, tras la muestra de parada de la etapa 1: la clase "invención" mezclaba un
hecho inventado con un consejo práctico sin marca y con un "puede" del libro dado por seguro. Desde hoy son cuatro
clases, cada una con su umbral, y corrigen la frontera de R6 en lo que no es operativo:

| Clase | Qué es | Qué se hace | Umbral en una muestra |
|---|---|---|---|
| **Contrario** | el nodo dice lo opuesto al libro | se corrige | 0 |
| **Invención dura** | un hecho, una cifra, una causa, un plazo, una norma o un resultado prometido que el libro no dice | sale | 0 |
| **Certeza endurecida** | un "puede", "suele" o "a menudo" del libro convertido en afirmación | vuelve al grado del libro; **cuenta como matiz** | 0,2 por nodo, junto con los matices |

Lo operativo (concreta el cómo sin afirmar nada nuevo) sigue sin ser defecto.

**Corrección del fundador, 1 oct 2026 (D4):** se elimina la clase "paso práctico sin marca". Un consejo práctico que el
libro no da es consejo de la casa y no es defecto: no se marca, no se cuenta y no tiene barrido. Las constancias CASA
que ya están en el registro interno se quedan como historia y no tienen efecto.

## R8. La política de corrección: quitar o devolver antes que redactar

**Decisión del fundador, 30 sep 2026.** En la muestra de parada de la etapa 1, 15 de las 39 invenciones estaban en
textos que la propia etapa había corregido: corregir redactando estaba creando defectos nuevos.

- **Orden de preferencia:**
  1. QUITAR lo que sobra.
  2. DEVOLVER el SENTIDO y el TÉRMINO PRECISO del libro: su "puede", su condición, su plazo, sin añadir nada.
     **Nunca** copiar ni traducir un pasaje palabra por palabra (D2, aclaración del fundador del 30 sep 2026): el
     nodo dice lo mismo que el libro con palabras de la casa.
  3. Solo si no hay otra forma, REDACTAR una frase nueva.
- **Verificación:** toda corrección que redacta, o que trae palabras que no estaban en el texto, la lee un verificador
  ciego contra el libro antes de aplicarse. El verificador no ve el razonamiento del árbitro. Si no la sostiene, la
  corrección no entra.
- **Ningún prefijo visible:** un paso práctico útil que el libro no da se queda con su texto, sin prefijo ni marca: es
  consejo de la casa y no es defecto (D4, 1 oct 2026). El aplicador rechaza cualquier texto nuevo con un prefijo de
  procedencia (D1).
- **Dónde vive:** el árbitro declara el `modo` de cada corrección (`quitar`, `devolver` o `redactar`). El verificador
  y el filtro de la tanda viven en las claves del remedio (`tanda_e1b.py`).
