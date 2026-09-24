# AUD-09. Acta de cierre de la campaña de arreglos

**Informe:** `docs/audits/AUD-09-Recorrido_Completo_2026-09-23.md` (commit `f35d2878`).
**Rama:** `arreglos-aud09`, de `main` en `13183d93`. **Cierre:** tanda 6, 25 sep 2026.
**Regla de cada arreglo:** primero una prueba que reproduce el fallo y cae en rojo; luego el
arreglo. Tras cada tanda: tsc, lint, build y las dos suites (web y motor) en verde, rama y
staging, y el paso a `main` por la mano del fundador tras su visto en la vista previa.

## Entregas

| tanda | contenido | en producción |
|---|---|---|
| 1 | seguridad y fugas: H14, H15, H16, /report | `48558d08`, tag `web-v2.6.1` |
| 2 | promesas de dinero: H01, H02, H03, límite diario | `48558d08`, tag `web-v2.6.1` |
| 3 | pérdida de datos: H04, H05, H06, H07 | `5150b93e`, tag `web-v2.6.2` |
| 4 | atascos, fechas y números: H08 a H13 | `5150b93e`, tag `web-v2.6.2` |
| 5 | medias por tema y barrido de precios | `046076c5`, tag `web-v2.6.3` |
| 6 | gobierno (`8b295aad`), acta como foto (M04), protección por nodo (M15), esta acta | `1ba09965`, tag `web-v2.6.4` |

**Migraciones de la campaña:** 039 (`plan_basico_at`), 040 (`project_actas`) y 041
(`protege_nodos`), las tres aplicadas por el fundador; su bloque está en
`my_idea_check_migraciones.sql`.

## Estados

- **CERRADO:** arreglado con su prueba y en producción.
- **PARCIAL:** una parte cerrada, el resto abierto y nombrado.
- **EN PENDIENTES:** es dato del grafo o de Design, y no código de esta campaña; vive en su ficha.
- **ABIERTO:** quedó fuera del alcance de las tandas que fijó el fundador. Ningún abierto se
  da por resuelto: todos viven en la ficha `aud09-remanentes` de `docs/PENDIENTES.md`.

## 1. ALTA (16 de 16 cerrados)

| hallazgo | qué | commit | estado |
|---|---|---|---|
| H01 | el seguimiento anunciaba 10 y cobraba 5 | `c97fb14e` | CERRADO |
| H02 | plan sin IA cobrado a precio completo | `b9141f65`, `48558d08` (regenerar y sello solo si hubo pago; migración 039) | CERRADO |
| H03 | la pantalla se tragaba los mensajes del servidor | `92d40003` | CERRADO |
| H04 | el cierre honesto de un mundo borraba el mundo pagado | `f4892fed` | CERRADO |
| H05 | comprar un mundo pisaba el estado vivo | `d31f0f7d` | CERRADO |
| H06 | el diagnóstico de un mundo podía quedar bloqueado | `648e1975` | CERRADO |
| H07 | la idea del invitado se quedaba sin dueño | `1658241e` | CERRADO |
| H08 | /nueva colgada en "Organizando tu idea..." | `578bd20b` | CERRADO |
| H09 | "Cargando tu espacio..." eterno | `2ad330df` | CERRADO |
| H10 | recalcular proponía fechas vencidas | `369c0e2f` | CERRADO |
| H11 | el calendario avisaba lo pausado, cerrado o reemplazado | `a75bc3d3` | CERRADO |
| H12 | dos cifras de dinero para lo mismo en Tus Números | `8b761473` | CERRADO |
| H13 | cuatro puertas sin pregunta y entrevistas de mundo sin salida | `5150b93e` (por código; el dataset no se tocó) | CERRADO |
| H14 | redirect abierto después del login | `4b350e3b` | CERRADO |
| H15 | la recuperación se saltaba la lista de la beta | `b87c0a1b` | CERRADO |
| H16 | borrar la cuenta fallaba abierto sin doble factor | `09decc95` | CERRADO |

## 2. MEDIA (22 cerrados, 1 parcial, 3 en pendientes, 29 abiertos)

| hallazgo | qué | commit | estado |
|---|---|---|---|
| M01 | las retiradas contaban en el total | `37ceaa43` | CERRADO |
| M02 | Expediente y Reporte sumaban todos los ciclos | `1e6b3f5c` | CERRADO |
| M03 | el Registro de protección leía todos los ciclos | `1e6b3f5c` | CERRADO |
| M04 | el acta de cierre se recalculaba en vivo | `215bb40d` (foto en `project_actas`, migración 040; la vista en vivo se llama "Estado actual") | CERRADO |
| M05 | el PDF conservaba el "Cumplimiento por mundo" | `040d9d48` | CERRADO |
| M06 | la cascada de mover fecha arrastraba planes reemplazados | `041d75d7` | CERRADO |
| M07 | el ritual repartía fechas a hechas y retiradas | `041d75d7` | CERRADO |
| M08 | seguimiento pagable con la idea realizada; volver a cerrar reescribía la fecha | `25545207` | CERRADO |
| M09 | `?vista=celebracion` abre la Celebración sin cierre | | ABIERTO |
| M10 | el bloque de realidad del mundo usaba el modo del núcleo | `c531e175` | CERRADO |
| M11 | el ritual del mundo usaba la cadencia del núcleo | `d4ec9ec8` | CERRADO |
| M12 | una sola instancia de Manos a la Obra para los dos espacios | `1b96d5a4` | CERRADO |
| M13 | el plan de un mundo ocupaba "Tu Plan" | `17e0bd28` | CERRADO |
| M14 | "Mi bitácora" del núcleo mezclaba mundos | `e775ff09` | CERRADO |
| M15 | un ciclo nuevo del núcleo dejaba la protección huérfana | `d28ffe0e` (la protección apunta al nodo; migración 041), `059945cf` (la escritura tolera la 041 ausente) | CERRADO |
| M16 | la sesión de un mundo cruzaba a otro mundo | `736796a0`; decisión del fundador en `8b295aad` (puede pasar por el núcleo, el corte es entre mundos) | CERRADO |
| M17 | los respaldos del motor callaban | `31c30162` | CERRADO |
| M18 | una lectura fallida se pintaba en cero | `aa3c3402` | CERRADO |
| M19 | escrituras fallidas sin rastro | `567f7b3a` | CERRADO |
| M20 | la narración de Tus Números caía a offline en silencio | `d89836e4` | CERRADO |
| M21 | un saldo ilegible se mostraba como 0 | `0e7b62ea` | CERRADO |
| M22 | fusible y límite gastados antes del saldo | `d0a3ea22` cierra el orden (saldo primero). Abierto: rechazar sin saldo antes de que el usuario escriba su "qué pasó" (el ritual se abre sin consultar saldo) | PARCIAL |
| M23 | /report sin cobro, fusible, límite ni doble factor | `7a2bbf7e` | CERRADO |
| M24 | Tus Números no exige plan | /report sí lo exige (`7a2bbf7e`); `numeros/route.ts` todavía no | ABIERTO |
| M25 | la carrera del cobro dura toda la generación | | ABIERTO |
| M26 | reintento tras fallar entre guardar plan y cerrar sesión (sospecha) | | ABIERTO |
| M27 | si el turno falla, la respuesta escrita se borra | | ABIERTO |
| M28 | el organizador crea el proyecto antes de la IA | | ABIERTO |
| M29 | dos definiciones de "entrevista abierta" | | ABIERTO |
| M30 | `?entrevista=1` nunca sale de la URL | | ABIERTO |
| M31 | el saldo del encabezado no se refresca tras el cobro | | ABIERTO |
| M32 | falta el aviso de precio antes de explorar del canon 03 | | ABIERTO |
| M33 | el plan cierra con "continúa la conversación" y dice "MVP" | | ABIERTO |
| M34 | la bitácora reescribe la historia | | ABIERTO |
| M35 | Tus Números no existe para bitácora ni Expediente | | ABIERTO |
| M36 | cada seguimiento de mundo contaba como compra | `48558d08` (arreglado de paso con el sello de H02) | CERRADO |
| M37 | un clic en la tarjeta cuenta como "Mundo activado" | | ABIERTO |
| M38 | a quien eligió su ritmo se le habla de fechas | | ABIERTO |
| M39 | el Expediente dice siempre "Vas por buen camino" | | ABIERTO |
| M40 | la capacidad por defecto no se guarda | | ABIERTO |
| M41 | mover-fecha acepta tareas hechas | | ABIERTO |
| M42 | "Última acción" de /ideas usa `updated_at` | | ABIERTO |
| M43 | "Ganancia del mes" sin fijos | | ABIERTO |
| M44 | redondeo distinto entre TS y Python | | ABIERTO |
| M45 | la prueba de paridad de prompts es circular | | ABIERTO |
| M46 | los documentos del mundo no alcanzan D4 | | ABIERTO |
| M47 | /creditos promete una vista que ya no existe | | ABIERTO |
| M48 | el enlace de protección fallido no se reintenta | | ABIERTO |
| M49 | el texto del doble factor promete más de lo que cubre | | ABIERTO |
| M50 | re-enrolar TOTP cambia el método antes de verificar | | ABIERTO |
| M51 | los 22 puentes re-anclados solo en el archivo | ficha `puentes-reanclados-sin-tejer` (`f44c1a4a`); es dato del grafo, toca a la sesión de integración | EN PENDIENTES |
| M52 | la brecha de compras y entrega apunta a no semillas | | ABIERTO |
| M53 | ley del ancla violada y 61 aristas no declaradas | hermano de M51 en la misma ficha (`f44c1a4a`) | EN PENDIENTES |
| M54 | 50 nodos del núcleo no se alcanzan por el núcleo | | ABIERTO |
| M55 | 233 nodos sin sucesor ofrecible | el motor ya da salida en los mundos (`5150b93e`); el censo vive en la ficha `callejones-del-grafo`, con la decisión del fundador de que el callejón del núcleo se queda (`f44c1a4a`) | EN PENDIENTES |

## 3. BAJA (2 cerrados, 1 parcial, 13 abiertos)

| hallazgo | qué | commit | estado |
|---|---|---|---|
| B01 | precios fuera de `precios.ts` | `046076c5` (documentos y comentarios, guardiana `preciosViejos.test.ts`); los mockups, a la ficha `mockups-con-precios-viejos` (`8b295aad`) para la próxima entrega de Design | CERRADO |
| B02 | `FLUJO_TRACKING.md §7` obsoleta | | ABIERTO |
| B03 | copy contra BANCO | | ABIERTO |
| B04 | BANCO §2 con 7 mundos y 5 etapas | `046076c5` (9 mundos, 6 hitos con Realizado) | CERRADO |
| B05 | pantalla de límite en /nueva | | ABIERTO |
| B06 | Claridad pintada en dos lugares | | ABIERTO |
| B07 | ruta JSON del organizador distinta de la real | | ABIERTO |
| B08 | íconos de compras y entrega | | ABIERTO |
| B09 | `catalogoMundos` no es la única puerta | | ABIERTO |
| B10 | nombres y etapas calculados distinto | | ABIERTO |
| B11 | duplicados de una sola fuente | | ABIERTO |
| B12 | validación laxa en `/modo` y `unlock` | | ABIERTO |
| B13 | comentarios obsoletos | | ABIERTO |
| B14 | sospechas menores | | ABIERTO |
| B15 | nodos, cosmético | | ABIERTO |
| B16 | tests ausentes donde vivían H04 a H06 | tanda 3 dejó pruebas del diagnóstico (`648e1975`), del cierre de mundo (`f4892fed`) y de la compra (`d31f0f7d`); siguen sin pruebas `unlock` y `start` | PARCIAL |

## Decisiones del fundador tomadas en la campaña

- Política de cobro: se verifica al empezar y se cobra al final, solo si se entregó lo
  prometido; un plan armado sin IA no se cobra y se puede regenerar (`ANALISIS_PRECIOS.md §4`).
- /report pasa por los mismos controles que toda llamada a la IA.
- Nada se borra jamás: un sello de compra, un cierre o un diagnóstico no se pierden por ningún flujo.
- H13 va por el código y el dataset no se toca.
- El callejón del núcleo se queda: ofrecer el plan con "Seguimos explorando" es su paso natural.
- M16: una entrevista de mundo puede pasar por el núcleo; el corte es solo entre mundos.
- M04: el acta de cierre es una foto; volver a cerrar guarda otra al lado.
- M15: la protección apunta al nodo de la tarea. Límite declarado: `nodos_origen` se guarda
  por etapa (migración 037), así que en un ciclo nuevo la resolución es exacta a nivel de etapa.
- Los mockups con precios viejos son errata de Design, no cambio de política.

## Veredicto

**AUD-09 CERRADA** con la entrada de la tanda 6 a producción (`web-v2.6.4`). Los 16 hallazgos
de gravedad ALTA quedaron cerrados en producción, igual que las medias de dinero, fallas
silenciosas, conteos y mezcla de espacios que el fundador puso en las tandas. Lo abierto no se
da por resuelto: queda nombrado arriba y en la ficha `aud09-remanentes` de `docs/PENDIENTES.md`,
para que el fundador lo ordene en otra campaña.

## CIERRE

**AUD-09 CERRADA el 25 sep 2026.** Visto del fundador a la tanda 6 (el acta es foto del cierre y
el segundo cierre agrega otra sin pisar la primera), migraciones 040 y 041 aplicadas, `main` por
avance rápido a `1ba09965` con el tag `web-v2.6.4`, y sello en vivo de www.myideaproject.com en
`1ba0996`. Balance final: ALTA 16 de 16 cerrados; MEDIA 22 cerrados, 1 parcial, 3 con ficha propia
y 29 abiertos; BAJA 2 cerrados, 1 parcial y 13 abiertos. El límite de M15 (nodos por etapa) quedó
aceptado por el fundador, con su condición de cierre en la ficha `aud09-remanentes`, donde viven
también los remanentes para su triaje.

## TANDAS 7A Y 7B

Después del cierre, el fundador triajó los remanentes (25 sep 2026) en DINERO, DATOS, SEGURIDAD,
CONFIANZA y OTRO. Las cuatro primeras clases fueron las tandas 7A y 7B, con las mismas reglas
(prueba en rojo primero, suites en verde, sin tocar `dataset/`, visto del fundador en la vista
previa). Migraciones de la 7A: 042 (`credit_reservas`, reserva de créditos) y 043
(`totp_secret_pendiente`), aplicadas por el fundador. La 7B no tuvo migraciones.

### Tanda 7A: dinero, datos y seguridad (tag `web-v2.6.5`, `main` en `271c5187`)

| hallazgo | qué quedó | commit |
|---|---|---|
| M24 | Tus Números pide plan para activar y narrar | `60389f57` |
| M25 | reserva de créditos al empezar, cobro al entregar, liberación si no hay cobro (042); política en `ANALISIS_PRECIOS §4` | `9b280470` |
| M22 | el ritual consulta el saldo antes de abrirse (lo que quedaba del parcial) | `8a73d772` |
| M30 | `?entrevista=1` se consume al arrancar | `ede226a3` |
| M32 | aviso de precio antes de explorar, con la cifra de `precios.ts` | `45406c0f` |
| B14a | el respaldo de la decisión del plan no corta por una subcadena ("playa"); paridad Python | `66672721` |
| M09 | la Celebración solo con el cierre; sin cambio de estado no hay rastro | `2cd655aa` |
| M26 | reproducido y arreglado: la entrega del plan es idempotente por sesión | `00623953` |
| M27 | la respuesta escrita no se pierde si el turno falla | `f52a99cc` |
| M34 | la bitácora no reescribe la historia (evento `item_hecho`; primer sello de la línea base) | `72037406` |
| M41 | mover-fecha no toca lo hecho ni lo retirado | `ac8f5376` |
| B14b | el dictado provisional no se pierde | `f39a8746` |
| M49 | el texto del doble factor dice lo que protege (cobros y borrados) | `b5ad1b20` |
| M50 | re-enrolar el autenticador no desarma el candado (043); su rojo, corrido contra `b5ad1b20`, consta en la ficha | `7d8c9e3f` |
| B07a | el mensaje interno de un error no viaja al cliente | `87e7d081` |
| B12 | `/modo` valida el espacio; `unlock` pide cuenta real y plan | `e10fd538` |

Decisiones del fundador tras la 7A, también en `web-v2.6.6`: la reserva de 2 horas se queda;
`streamTerminal` manda al cliente solo un código y un identificador de correlación (`3e037783`);
el guardián de commit corre `tsc --noEmit` sobre `web/` (`1bcbf33b`), con la prueba de que un
error de tipos aborta; y la constancia del rojo de M50 (`2b35bdc3`).

### Tanda 7B: confianza (tag `web-v2.6.6`, `main` en `1adfb9d0`)

| hallazgo | qué quedó | commit |
|---|---|---|
| M31 | el saldo del encabezado muestra lo disponible y dice lo reservado para la sesión en curso; se refresca | `a42a312d` |
| M28 | la idea sin Claridad dice "Sin ordenar" y ofrece ordenarla, reusando la misma idea | `2bf59bae` |
| M29 | una sola regla de "entrevista abierta" | `24a900ab` |
| M33 | el plan no invita a una sesión cerrada; sin "MVP"; con tildes; paridad Python | `d64051f0` |
| M37 | un mundo cuenta cuando tiene su plan | `6876156f` |
| M38 | a mi ritmo no se habla de plazos | `e95686b8` |
| M39 | el "Cómo te fue" del Expediente habla con los datos | `c5c0ec60` |
| M40 | la capacidad que se ve elegida se guarda | `c97f38c1` |
| M42 | la última acción cuenta el trabajo en las tareas | `fa45f9fc` |
| M43 | sin gastos fijos no se muestra una ganancia que no es neta | `9436b833` |
| M47 | `/creditos` no promete la vista global eliminada | `f5fe191c` |
| M48 | el registro de protección vacío dice que el enlace falló | `7eefed19` |
| B03a | "el mismo día" en vez de "el día antes"; fuera "Yo te recuerdo" y "El más elegido" | `9543b64b` |
| B05 | el límite dice su número real y lleva a las ideas | `d45fdff9` |
| B10 | una etapa (`etapaDeIdea`), una fecha de "Tu Plan" y un nombre de la idea | `b55ed305` |
| B14c | el micrófono dice por qué se apagó | `8f60e5d2` |
| M35 | por texto: el Expediente dice exactamente lo que incluye | `1243c826` |

### Estado final de la campaña

**Todo lo de DINERO, DATOS, SEGURIDAD y CONFIANZA quedó CERRADO en producción** (`web-v2.6.5`
y `web-v2.6.6`), incluidos los dos parciales de su clase (M22 en la 7A; B16 es de OTRO). Lo de
OTRO (M44, M45, M46, M52, M54, B02, B03b, B06, B07b, B08, B09, B11, B13, B14d, B15 y B16) y las
funciones futuras (doble factor al entrar, volver a enlazar un registro de protección, Tus
Números dentro del Expediente, y guardar los nodos por tarea del límite de M15) quedan en la
ficha `aud09-remanentes` de `docs/PENDIENTES.md`, cada uno con su condición de cierre. La campaña
de arreglos de la AUD-09 termina aquí.
