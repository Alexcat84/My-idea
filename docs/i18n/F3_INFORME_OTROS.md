# i18n F3, grupo 2: los otros nueve idiomas (pendiente del visto del fundador)

Rama `i18n`. Decisión del fundador (25 sep 2026): el inglés queda aprobado con condición hasta el
merge, y se sigue con todos los demás hasta terminar. Convenciones y términos fijos de cada idioma:
`F3_CONVENCIONES.md`. Informe del inglés: `F3_INFORME_EN.md`.

## Qué quedó hecho
- **`ACTIVE_LOCALES` = los once idiomas.** Cada uno de los 56 catálogos tiene fr, pt, de, it, ja,
  zh, ko, ar e hi, unos 1.540 textos por idioma. El compilador y el auditor (mismas claves,
  marcadores y etiquetas, nada vacío, "My Idea" intacto) están en verde.
- **Cómo se tradujo:** 27 traductores (tres por idioma) sobre JSON, sin tocar los .ts, validados con
  `scripts/i18n/traducir.ts` (la misma comparación del auditor, más la voz: sin rayas ni ¿¡) e
  integrados con esa misma herramienta. Así ningún archivo tuvo dos manos a la vez.
- **Revisión de naturalidad por un segundo modelo** en los nueve (la regla D1 del glosario, pedida
  para los ocho; se hizo también para el francés). El revisor leyó cada idioma completo contra el
  español. Buscó sobre todo los términos que los tres traductores de un mismo idioma habían
  resuelto distinto, el sentido, la gramática y el género de quien usa la app. **Lo evidente está
  aplicado; lo discutible no, y va abajo para tu decisión.**

| idioma | evidentes aplicados | discutibles para ti |
|---|---|---|
| francés | 43 | 5 |
| portugués (Brasil) | 58 | 2 |
| alemán | 48 | 5 |
| italiano | 33 | 4 |
| japonés | 77 | 5 |
| chino simplificado | 71 | 3 |
| coreano | 81 | 4 |
| árabe | 60 | 1 |
| hindi | 83 | 6 |

- **Palabra de borrado** en cada idioma (SUPPRIMER, EXCLUIR, LÖSCHEN, ELIMINA, 削除, 删除, 삭제, حذف,
  हटाएँ); el servidor acepta además siempre "ELIMINAR".
- **Revisado en el navegador** (compilado local, sin base de datos): portada, /login, /nueva y
  /creditos en los nueve idiomas, con `<html lang dir>` correcto (`zh-Hans`, árabe `rtl`).

## Arreglos de código que salieron al traducir
- En alemán, los sustantivos conservan su mayúscula: la etiqueta de horas de Manos a la Obra y el
  título de la idea en Tus Números se pasaban a minúscula.
- El nombre de los archivos descargados borraba los signos vocálicos del devanagari (y de
  cualquier escritura con marcas): "विचार" quedaba "वचर".
- Español: dos tandas de errores corregidas con prueba en rojo (ver `F3_INFORME_EN.md` y los
  commits), la última con lo que encontraron los nueve traductores: las preguntas "¿Cuántas veces de
  {{u}}…?", "Mi bitácora de mi viaje", "Tu bitacora", "Tu viaje core", "planificado · adelantada",
  "el cómo te fue de", "subiría" y tres textos que forzaban un plural con lo que entra por el
  marcador ("1 crédito disponibles", "tus cifras del hace 21 min").

## Pendiente para F4 (antes del merge conviene tenerlo presente)
- **Árabe de derecha a izquierda:** la página ya se pone en `rtl`, pero las 69 clases físicas de
  dirección (DISENO §3.5) siguen sin pasar a las lógicas: algunos márgenes y el selector fijo arriba
  a la derecha no se reflejan. Es F4.
- **Tipografías CJK y devanagari** con `next/font`: hoy salen con la fuente del sistema (se ven bien
  en los navegadores comunes). Es F4.
- **Italiano:** "il 8 marzo" en vez de "l'8 marzo" cuando la fecha va tras un artículo. Se arregla en
  el código de fechas, no en el catálogo.

## Lo que sigue en español dentro de los otros idiomas (a propósito, hasta F5)
Igual que en inglés: todo lo que escribe la IA (entrevista, Claridad, plan), las etiquetas del riel y
las preguntas del grafo (D3), los documentos y sus títulos, el plan básico sin IA y el `.ics`.

## Errores o dudas del español que quedan para ti (no se tocaron)
- "Realizada" en los hitos, frente a "Realizado" en el glosario (parece concordancia con "idea").
- Regionalismos: "algo se atoró", "la plata", "No corre para esta idea".
- "cuando tu proyecto crezca" (servidorSesion y devCierre) y "proyecto vivo" en la portada, frente a
  la regla de voz de que "proyecto" solo se gana al final.
- "Ya pasó y sigue abierto" (grupo del calendario), en masculino junto a textos en femenino.
- "Duración: {{n}} días" y "Racha más larga: {{n}} días" dicen "1 días" cuando n es 1.
- En Tus Números, "Cada {{u}} te deja {{acento}}", donde el acento ya lleva "por {{u}}", repite la
  unidad; y "precio al que la vendes" supone unidad femenina.
- "Tu idea pasa de 12.000 caracteres": el número está escrito a mano y no sale de la constante.
- El glosario tiene en árabe "ضاعف عملك" (Multiplica tu Negocio) en masculino singular; es el único
  que no pasó al plural neutro de D7 (ver discutibles del árabe).

## Los discutibles de cada idioma (para tu decisión; no aplicados)
### Francés (fr): 43 evidentes aplicados, 5 discutibles
- `analyticsInforme.ts` ANALYTICS_INFORME.hitos.conLineaBase: «avec son point de départ fixé» → «avec son plan de référence». Tercera traducción de "línea base"; alinearla con "plan de référence" da coherencia pero repite "plan" bajo "Ton plan · cycle 1".
- `mundos.ts` MUNDOS_I18N.franquicias.promesa: «Transforme ton entreprise qui a fait ses preuves en plusieurs qui fonctionnent de la même façon.» → «Transforme ton entreprise éprouvée en un réseau qui fonctionne partout pareil.». La promesa del mundo es larga y pesada frente a las otras ocho; "réseau" es más corto pero añade una idea (red) que el español no dice.
- `cierreHonesto.ts` CIERRE_HONESTO.unAltoHonesto: «Un arrêt honnête» → «Une halte honnête». "halte" traduce mejor "un alto" (parar para seguir después); "arrêt" suena a final definitivo. Es cuestión de tono.
- `manosALaObra.ts` MANOS_A_LA_OBRA.mundo.siTerminado: «Oui, je le considère comme terminé» → «Oui, c'est terminé». Botón largo (34 caracteres); la versión corta cabe mejor, aunque pierde el matiz de "lo doy por" (decisión del usuario).
- `expediente.ts` EXPEDIENTE.acciones.retiradasExplicacion: «Des tâches dont tu as décidé qu'elles ne s'appliquent pas à cette idée. Ce ne sont ni des oublis ni des échecs : elles font partie de ton discernement.» → «Des tâches dont tu as décidé qu'elles ne s'appliquent pas à cette idée. Ce ne sont ni des tâches en suspens ni des échecs : elles font partie de ton discernement.». El español dice "no son pendientes"; "oublis" (olvidos) cambia el matiz, aunque se lee con naturalidad.

### Portugués (pt): 58 evidentes aplicados, 2 discutibles
- `manosALaObra.ts` MANOS_A_LA_OBRA.ritual.asiVaSigamos: «É assim que está, vamos seguir» → «É isso, vamos seguir». 'É assim que está' es literal y pesado para un botón; 'É isso' es lo que diría un brasileño
- `mundos.ts` MUNDOS_I18N.risk_management.promesa: «Veja chegar o que pode dar errado e decida antes que isso decida por você.» → «Preveja o que pode dar errado e decida antes que isso decida por você.». Promesa de mundo: 'Veja chegar' suena forzado; 'Preveja' es más natural (toca texto de marca de un mundo)

### Alemán (de): 48 evidentes aplicados, 5 discutibles
- `documentosPapel.ts` DOCUMENTOS_PAPEL.resumen.meses[2]: «Mär» → «März». fecha corta: hitos.ts escribe "3. März/Juni/Juli" y aquí "3. Mär/Jun/Jul"; unificar con hitos (lo usual en alemán)
- `documentosPapel.ts` DOCUMENTOS_PAPEL.resumen.meses[5]: «Jun» → «Juni». ídem
- `documentosPapel.ts` DOCUMENTOS_PAPEL.resumen.meses[6]: «Jul» → «Juli». ídem
- `reporte.ts` REPORTE.preguntas.servicio.capacidad_semanal: «Wie viele kannst du in einer normalen Woche übernehmen (gezählt pro {{u}})?» → «Wie viele Einheiten ({{u}}) kannst du in einer normalen Woche übernehmen?». "(gezählt pro {{u}})" es rebuscado; esta forma evita el plural de {{u}} pero repite "Einheit" si {{u}} es la unidad por omisión
- `expediente.ts` EXPEDIENTE.expediente.estadoEnMarcha: «**Status** Im Gange» → «**Status** Läuft». "Im Gange" es correcto pero algo libresco; "Läuft" es lo que se ve en apps (y es el "en curso" del resto)

### Italiano (it): 33 evidentes aplicados, 4 discutibles
- `acceso.ts` LOGIN.olvide: «Ho dimenticato la password» → «Password dimenticata?». Fórmula estándar de las apps en italiano; si se aplica, cambiar también la cita en CLAVE_NUEVA.enlaceVencido
- `acceso.ts` CLAVE_NUEVA.enlaceVencido: «Questo link è scaduto o è già stato usato. Chiedine uno nuovo da 'Ho dimenticato la password'.» → «Questo link è scaduto o è già stato usato. Chiedine uno nuovo da 'Password dimenticata?'.». Solo junto con LOGIN.olvide: la cita debe coincidir con el enlace
- `portada.ts` PORTADA.meta.descripcion: «Agli imprenditori non mancano le idee. Manca un interlocutore serio. Racconta la tua, ricevi il tuo piano e mettilo in pratica.» → «Agli imprenditori non mancano le idee. Manca loro un interlocutore serio. Racconta la tua, ricevi il tuo piano e mettilo in pratica.». 'Manca loro' mantiene el sujeto del español ('les falta'); sin él la frase queda como afirmación general. Más formal
- `portada.ts` PORTADA.acerca.titulo: «Agli imprenditori non mancano le idee. Manca un interlocutore serio» → «Agli imprenditori non mancano le idee. Manca loro un interlocutore serio». Igual que meta.descripcion; aplicar ambos o ninguno

### Japonés (ja): 77 evidentes aplicados, 5 discutibles
- `portada.ts` PORTADA.meta.titulo: «My Idea：あなたの創造力を、行動に変える» → «My Idea：創造力を、行動に変える». quitar あなた del lema; en publicidad japonesa あなた se tolera, decide el fundador
- `portada.ts` PORTADA.tituloOculto: «My Idea：あなたの創造力を、行動に変える» → «My Idea：創造力を、行動に変える». igual que meta.titulo
- `reporte.ts` REPORTE.tusNumerosHoy: «## 今のあなたの数字» → «## 今日時点の数字». igual que tusNumeros 'Tus números de HOY'; hoy mezcla la marca あなたの数字 con un título genérico
- `tusNumeros.ts` TUS_NUMEROS.secciones.barraDeLaVerdad: «真実のバー» → «ありのままを映すバー». '真実のバー' suena a calco; la alternativa es más natural pero pierde el golpe de la frase
- `detalleActividad.ts` DETALLE_ACTIVIDAD.chip.tardia.one: «遅れ · {{n}}日» → «予定より後 · {{n}}日». voz espejo: 遅れ ('retraso') juzga un poco; si el fundador lo prefiere, cambiar 遅れ por 予定より後 en todo el producto (analisis, celebracion, analyticsInforme, detalleActividad)

### Chino (zh): 71 evidentes aplicados, 3 discutibles
- `mundos.ts` MUNDOS_I18N.health_safety.promesa: «保护你的人和你的生意，挺过最糟糕的那一天。» → «护住你的团队和生意，远离最糟糕的那一天。». '挺过' = sobrevivirlo; el español es protegerlos DE ese día (prevenir). 你的人 → 你的团队. Promesa de marca
- `tusNumeros.ts` TUS_NUMEROS.guardianTitulo: «数据守护。» → «数据把关。». '数据守护' suena a compuesto artificial; 把关 es la palabra común para 'revisar que cuadre'
- `servidorProyecto.ts` SERVIDOR_PROYECTO.numeros.noNarroInconsistente: «这些数据我没法给出结论：请查看数据守护的提示，修正对不上的数字。» → «这些数据我没法给出结论：请查看“数据把关”的提示，修正对不上的数字。». acompaña al cambio de guardianTitulo (solo si se aprueba ese)

### Coreano (ko): 81 evidentes aplicados, 4 discutibles
- `analisis.ts` ANALISIS.comun.repartoTitulo: «날짜를 지킨 방식» → «날짜 준수 현황». "날짜를 지킨 방식" suena a "la manera de cumplir"; el gráfico reparte a tiempo/adelantadas/tardías y "일정 준수" ya es el término de analyticsInforme
- `tusNumeros.ts` TUS_NUMEROS.barra.conMargen: «받는 가격 막대가 더 길고, 드는 비용 막대는 거기에 못 미쳐요. 남는 그 공간이 <b>나의 마진</b>이에요. 이럴 때는 더 많이 팔수록 목표에 정말 가까워져요.» → «받는 가격 막대가 더 길고, 드는 비용 막대는 거기에 못 미쳐요. 남는 그 공간이 <b>마진</b>이에요. 이럴 때는 더 많이 팔수록 목표에 정말 가까워져요.». "나의 마진" en una frase que la app dirige al usuario; el estilo "나의/내" en primera persona del usuario es válido en apps coreanas, pero aquí sobra
- `tusNumeros.ts` TUS_NUMEROS.compuerta.texto: «마진, 손익분기점, 계산된 세 가지 방법과 시나리오를 내가 입력한 수치로 보여 줘요. 계획에 포함되어 있어요. 아이디어마다 한 번 활성화하면, 수치 수정과 재계산은 언제든 할 수 있어요.» → «마진, 손익분기점, 계산된 세 가지 방법과 시나리오를 직접 입력한 수치로 보여 줘요. 계획에 포함되어 있어요. 아이디어마다 한 번 활성화하면, 수치 수정과 재계산은 언제든 할 수 있어요.». "내가 입력한" (voz del usuario) dentro de una frase de la app; "직접 입력한" es neutro. Es cuestión de estilo (el estilo "내" es común en apps coreanas)
- `cierreHonesto.ts` CIERRE_HONESTO.notaMundo: «메인 여정은 그대로예요. 이 월드를 닫아도 아이디어에는 영향이 없어요.» → «주 여정은 그대로예요. 이 월드를 닫아도 아이디어에는 영향이 없어요.». "메인" es anglicismo (aunque muy usado en coreano); "주 여정" o "기본 여정" evitaría el préstamo. Aplicaría igual a nucleo.tuViajePrincipal/tuViajeCore y descargas.sinDocumentosViaje

### Árabe (ar): 60 evidentes aplicados, 1 discutibles
- `mundos.ts` MUNDOS_I18N.franquicias.nombre: «ضاعف عملك» → «ضاعفوا عملكم». Término del glosario (§6) en masculino singular; es el único que quedó así tras pasar el resto del glosario al plural neutro (D7). Alternativa neutra: "ضاعفوا عملكم". Decide el fundador; no se aplica

### Hindi (hi): 83 evidentes aplicados, 6 discutibles
- `motor.ts` MOTOR.preguntaTipoOferta: «आप ठीक-ठीक क्या बेचते हैं, और उसका पैसा कैसे लेते हैं?» → «आपका प्रोडक्ट या सेवा ठीक-ठीक क्या है, और उसका पैसा कैसे मिलता है?». 'बेचते/लेते हैं' son masculinos; la forma neutra obliga a reformular la pregunta (el original es más directo)
- `documentosPapel.ts` DOCUMENTOS_PAPEL.resumen.loQueMasTeMovio: «आपके सफ़र को सबसे ज़्यादा किसने आगे बढ़ाया» → «आपका रास्ता कैसे बदला». el texto debajo habla de cuánto se movieron tus fechas/ritmo, no de qué te impulsó; igual que analisis comun.comoSeMovio. (El inglés también lo leyó como 'impulsó')
- `tusNumeros.ts` TUS_NUMEROS.secciones.escenarios: «अलग-अलग स्थितियाँ, आपकी आज की कीमत पर» → «अलग-अलग परिदृश्य, आपकी आज की कीमत पर». 'escenarios' es परिदृश्य en creditos y potenciaTuIdea pero स्थिति aquí; स्थिति además es 'estado' de una tarea. Unificar a परिदृश्य (o al revés)
- `tusNumeros.ts` TUS_NUMEROS.escenarios.escenario: «स्थिति» → «परिदृश्य». misma unificación de 'escenario'
- `motorNumeros.ts` MOTOR_NUMEROS.escenarios.pesimista: «निराशावादी» → «कमज़ोर हालात». 'निराशावादी' describe a una persona y suena sánscrito; como etiqueta de escenario 'कमज़ोर हालात' se lee más natural
- `analisis.ts` ANALISIS.comun.semanaCorta: «ह{{n}}» → «हफ़्ता {{n}}». 'ह{{n}}' no es una abreviatura reconocible en hindi; más largo pero claro (verificar espacio en el eje del gráfico)

