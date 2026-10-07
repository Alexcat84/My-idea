# Auditoría de prompts: instrucciones que empujan a inventar (1 oct 2026)

Añadido del fundador del 1 oct 2026, punto 2. Es solo lectura: **nada se cambia hasta el visto del fundador**.

La regla es cero contrarios y cero invenciones duras. Una invención dura es una cifra, una norma o ley, un plazo, una
causa o un resultado prometido que ningún nodo dice y la persona no dijo.

Dónde viven los prompts:
- Los SYSTEM_* del motor: `engine/prototipo_motor.py` ("motor:N"), copiados a `web/lib/assets/prompts.json`.
- Los nacidos en TS: `web/lib/prompts.ts`.
- Los bloques fijos de toda llamada: `reglaSinFuentes.ts`, `reglaContextoUsuario.ts` e `i18n/idiomaSalida.ts`.
- Un cambio en el motor exige correr `scripts/sync_assets_web.py`, y la caché del prompt se invalida una vez.

**Resumen:**
- 18 llamadas revisadas: 13 SYSTEM_* del motor y 5 prompts nacidos en TS, más los 3 bloques fijos.
- **24 hallazgos: 6 altos, 10 medios y 8 bajos.**

## A. Severidad alta

**APLICADOS los 6 (decisión del fundador, 1 oct 2026)** en `engine/prototipo_motor.py`, sincronizados a `prompts.json`, con las suites en verde. El ejemplo de las velas ya no lleva ninguna cifra. Los 18 medios y bajos siguen pendientes (`docs/PROXIMOS_PASOS.md`).

| # | Prompt (dónde) | Instrucción | Por qué empuja a inventar | Ajuste propuesto |
|---|---|---|---|---|
| A1 | SYSTEM_PLAN, ejemplo de las velas (motor:1118-1131) | "cada vela te cuesta $3 … a $8 … 10 velas al mes, eso son $50" | El perfil del ejemplo dice "No ha calculado costos" (motor:1083) y su material no trae cifras, pero el prompt afirma que "$3 y $8 salen directamente del material". El ejemplo más largo enseña a inventar cifras, volumen y un juicio | Un ejemplo sin cifras: "Todavía no sabes cuánto te cuesta cada vela… **Costo por unidad:** suma lo que gastas en una tanda y divide entre las velas que salen. **Primera acción:** anota lo que gastaste en tu última tanda". Borrar "la cifra de $3 y $8 salen directamente del material" |
| A2 | SYSTEM_PLAN, regla 1 (motor:881-885) | "tarea concreta con verbo, sujeto y criterio de exito. Ejemplo: 'Entrevista a 5 personas'" | El "5" no viene de ningún lado. Pedir un criterio de éxito en cada tarea invita a umbrales inventados | "…una tarea con verbo, sujeto y qué debe quedar anotado al terminar. Pon cantidades o umbrales solo si vienen en el material o los dijo la persona." |
| A3 | SYSTEM_PLAN, regla 9 (motor:974-991) | "DEBE darle tratamiento explicito y accionable … criterio de exito medible" | Obliga a dar pasos sobre el bloqueo aunque el material no lo cubra. Choca con la regla 16 (confesar el hueco) | "…con pasos que salgan del material. Si no trae cómo atacarlo, aplica la regla 16. El criterio de éxito lo fija la persona; no inventes umbrales." |
| A4 | SYSTEM_ESTADO_VIVO (motor:1190-1194) | "los titulos de los conceptos nuevos que se cubrieron … que se ha validado o decidido" | Haber hablado de un tema no es haberlo hecho, y el estado vivo vuelve como contexto de la persona en todas las llamadas. La regla 8 del plan escribe "ya validaste…": se fabrica un logro | "Lo validado o decidido entra solo si la persona lo dijo. Los conceptos cubiertos son temas que se conversaron: 'se habló de…'. No añadas cifras, causas ni logros." |
| A5 | SYSTEM_DIAGNOSTICO_MUNDO (motor:1353-1354) | "como promesa concreta y verificable" | Recibe solo etiquetas, no el contenido de los nodos. En mundos normativos invita a prometer certificaciones, normas o resultados | "…qué temas de los recorridos trabajaría el plan, con tus palabras. No prometas resultados, certificaciones, normas, plazos ni documentos que no estén en lo que recibes." |
| A6 | SYSTEM_DIAGNOSTICO_MUNDO (motor:1343-1345) | "Si te nace un paso, conviertelo en promesa" | Legitima convertir cualquier ocurrencia en promesa comercial | "Si te nace un paso que corresponde a uno de los temas recorridos, nómbralo como tema; si no corresponde a ninguno, descártalo." |

## B. Severidad media

| # | Prompt (dónde) | Instrucción | Ajuste propuesto |
|---|---|---|---|
| B1 | SYSTEM_PLAN, regla 6 (motor:922-924) | "con lo que va a lograr con este plan concreto" (promete un resultado) | "…con lo que este plan le ayuda a averiguar o decidir, sin prometer resultados." |
| B2 | SYSTEM_PLAN, regla 4-bis (motor:913-919) | "Un item por cada numero que la persona debe calcular", con un ejemplo de cuatro columnas de un caso digital que el modelo copia | "Un ítem por cada número que nombran los conceptos con es_viabilidad_economica; no añadas métricas que el material no nombre." |
| B3 | SYSTEM_PLAN, velas, paso 2 (motor:1104-1107) | "es mas rapido confirmar interes ahi…" (causa añadida) | "Prueba venderlas primero en un mercado local o grupo de redes sociales de tu zona antes de pensar en una tienda propia." |
| B4 | SYSTEM_PLAN, regla 15 y cierre (motor:1047-1052, 1073-1075) | Buena protección, pero incompleta: no cubre normas, plazos, precios de referencia ni resultados | Añadir al cierre: "Tampoco inventes leyes, normas, trámites, plazos, precios o porcentajes de referencia, tasas de éxito, resultados prometidos ni nombres de herramientas o empresas que no estén en el material o en lo que dijo la persona." |
| B5 | SYSTEM_INTERPRETE_MULTI, perfil_update (motor:647-649) | "resumela en 1 o 2 frases" (resumir invita a deducir, y lo deducido pasa a hecho) | "…con lo que la persona dijo, en sus palabras; no deduzcas causas, cifras ni logros." |
| B6 | SYSTEM_REPORTE (motor:1290-1292) | "¿es sano el margen?" (exige una referencia de la industria) | "…comparándolos solo entre sí o con una meta que la persona declaró; no califiques contra referencias externas." |
| B7 | SYSTEM_CAMINOS (motor:1161, 1173-1178) | "Eres el estratega", "que harias distinto", ejemplo "Vender por encargo sin local" | "…qué trabajarías distinto usando solo lo que dicen los candidatos y lo que contó la persona; sin canales, modelos de venta, cifras ni plazos nuevos." Ejemplo neutro: "Probar primero con quienes ya te compran" |
| B8 | SYSTEM_ENLACE_PROTECCION (prompts.ts:186-187) | "LA DETECCIÓN que la originó" (riesgo inferido que se ve en pantalla) | "…solo si el texto la nombra o se lee en ella sin suponer nada; si no, cadena vacía." |
| B9 | SYSTEM_ENLACE_PROTECCION (prompts.ts:190-192) | La severidad (probabilidad y dolor): un juicio sin respaldo que se muestra | "…solo si el plan o la persona dan base; si no, null." El validador ya acepta null |
| B10 | SYSTEM_ORGANIZADOR (motor:1252-1256) | "areas_que_cubriria_tu_plan_completo", "lo_que_estas_asumiendo_sin_saberlo" | "Las áreas son nombres de temas de la lista de puertas. Lo que asumes son preguntas abiertas, nunca afirmaciones de mercado, normas o cifras." |

## C. Severidad baja

| # | Prompt (dónde) | Ajuste propuesto |
|---|---|---|
| C1 | SYSTEM_PLAN, ejemplo de la regla 15 (motor:1053-1055): "busca en el registro oficial de tu pais" | "busca cuántos auditores certificados hay en tu zona; ese número te dirá si hay espacio" |
| C2 | SYSTEM_PLAN, ejemplo de la regla 8 (motor:933-935): "ya validaste el interes de dos instituciones" | Añadir "usa solo avances que estado_vivo_previo diga con esas palabras" |
| C3 | SYSTEM_PLAN, regla 3 (motor:900-901): "para 3 piezas y divide entre 3" | Opcional: "para una tanda y divide entre las piezas que salieron" |
| C4 | SYSTEM_PLAN, regla 16 (motor:1069-1070): "case studies y un criterio pass/fail" | "…y luego ofrece solo lo que el material sí trae alrededor de esa prioridad" |
| C5 | SYSTEM_INTERPRETE_MULTI (motor:498-507, 529): beneficios prometidos en los ejemplos; "lo adyacente que SÍ cubres" | "…lo adyacente que trae alguno de los nodos que recibes", y quitar los beneficios de los ejemplos |
| C6 | SYSTEM_REPORTE (motor:1286, 1303, 1316): "(y cómo conseguirlos)" y el ejemplo de $850/$170 | "…que lo puede medir o anotar ella misma; no nombres fuentes externas". Marcar el ejemplo como cifras ficticias de forma |
| C7 | REGLA_SIN_FUENTES (reglaSinFuentes.ts): pone ejemplos de métodos con nombre en toda llamada | "Un método se nombra solo si viene en el material que recibes, y se explica sin atribuirlo a nadie; si tiene nombre neutro, usa ese." Sin los ejemplos |
| C8 | REGLA_CONTEXTO_USUARIO (reglaContextoUsuario.ts:12-13): "su contador o abogado" (roles supuestos) | "adáptalo a quien la persona dijo que lo cumple; si no lo dijo, habla de ella misma o pregúntalo en condicional" |

Menores, sin hallazgo formal:
- SYSTEM_CLASIFICAR_OFERTA (motor:3323): "la palabra que el usuario usaria" pasaría a "la que usó; si no la dijo, 'unidad'".
- `seguimientoComposer.ts:121`: riesgo mínimo.

## D. Protecciones que ya existen (conservar)

- **SYSTEM_REPORTE:** su regla dura, ninguna cifra que no venga de la calculadora o de lo declarado (motor:1275). Es
  la mejor protección del sistema.
- **SYSTEM_PLAN:** las reglas 4, 15, 16, 12 y 11, el cierre "Todo debe salir del material recibido" y "la honestidad
  sobre lo que aún no se sabe vale más que un número inventado".
- **SYSTEM_INTERPRETE_MULTI:** la memoria numérica ("nunca uno que tú infieras"), la ficha ("Nunca inventes un dato"),
  la unidad de venta, la confesión de dominio y los ids nunca inventados.
- **SYSTEM_CAMINOS:** "Sin cifras que no estén en lo que recibiste".
- **SYSTEM_DIAGNOSTICO_MUNDO:** "citando su realidad" y "No agregues … precios".
- **Enlazador y estimador:** prohíben puntajes, porcentajes y horas.
- **Reformulador y adaptador:** "la forma, nunca el fondo".
- **SYSTEM_ORGANIZADOR:** "PROHIBIDO instruir".
- **REGLA_CONTEXTO_USUARIO:** "Nunca des por hecho lo que la persona no dijo".

## E. Prompts revisados

| Prompt | Dónde | Resultado |
|---|---|---|
| SYSTEM_CLASIFICACION | motor:317 | ok |
| SYSTEM_PUERTA_AVANZADA | motor:329 | ok |
| SYSTEM_INTERPRETE_MULTI | motor:351 | B5, C5 |
| SYSTEM_PROFUNDIZAR | motor:840 | ok |
| SYSTEM_PREGUNTA_DIRIGIDA | motor:847 | ok |
| SYSTEM_PLAN | motor:865 | A1, A2, A3, B1-B4, C1-C4 |
| SYSTEM_CAMINOS | motor:1159 | B7 |
| SYSTEM_ESTADO_VIVO | motor:1187 | A4 |
| SYSTEM_JUEZ_SESION | motor:1201 | ok (interno) |
| SYSTEM_ORGANIZADOR | motor:1243 | B10 |
| SYSTEM_REPORTE | motor:1261 | B6, C6 |
| SYSTEM_DIAGNOSTICO_MUNDO | motor:1329 | A5, A6 |
| SYSTEM_CLASIFICAR_OFERTA | motor:3315 | ok (menor) |
| SYSTEM_REFORMULADOR_PROTECCION | prompts.ts:96 | ok |
| SYSTEM_ADAPTAR_PREGUNTA | prompts.ts:125 | ok |
| SYSTEM_CONSULTA_AL_ESPANOL | prompts.ts:158 | ok |
| SYSTEM_ENLACE_PROTECCION | prompts.ts:176 | B8, B9 |
| SYSTEM_ESTIMACION_BANDA | prompts.ts:212 | ok |
| REGLA_SIN_FUENTES | reglaSinFuentes.ts | C7 |
| REGLA_CONTEXTO_USUARIO | reglaContextoUsuario.ts | C8 |
| bloquesDeSistema | i18n/idiomaSalida.ts | ok |

**Orden sugerido:**
1. A1-A3 y B4 (SYSTEM_PLAN).
2. A4 (estado vivo), porque contamina el contexto de todas las llamadas siguientes.
3. A5-A6 (diagnóstico de mundo).
4. Los medios, y después los bajos.

## F. Los 18 medios y bajos: estado tras el encargo del 6 oct 2026 (punto 7a)

Encargo: aplicar los ajustes que solo QUITAN y dejar los demás listados para el visto del fundador. Se aplicó solo lo
que se puede quitar sin poner palabras nuevas. La parte que añade texto de cada ajuste queda aquí para el visto.

**Aplicados (solo quitan):**

| # | Qué se quitó | Dónde |
|---|---|---|
| B1 | "con lo que va a lograr con este plan concreto" (prometía un resultado) | SYSTEM_PLAN, regla 6 |
| B2, parte | el ejemplo de las cuatro columnas de un caso digital, que el modelo copiaba | SYSTEM_PLAN, regla 4-bis |
| B3 | la causa añadida del paso 2 de las velas (ya había salido con A1) | SYSTEM_PLAN, ejemplo |
| B6 | "¿es sano el margen?" (pedía una referencia externa); queda "¿el techo de ingreso alcanza lo que busca?" | SYSTEM_REPORTE |
| C4 | "con case studies y un criterio pass/fail" | SYSTEM_PLAN, regla 16 |
| C5, parte | los beneficios prometidos de los ejemplos ("te protege de invertir de más", "evita que inviertas semanas…") | SYSTEM_INTERPRETE_MULTI |
| C8, parte | "su contador o abogado" (roles supuestos) | REGLA_CONTEXTO_USUARIO (TS y su copia en `build_question_cache.py`) |

**Para el visto del fundador (añaden texto, o quitar solo no basta):**

- **B2, resto:** limitar los números a los que nombran los conceptos de viabilidad.
- **B4:** ampliar el cierre del plan a leyes, normas, trámites, plazos, precios de referencia, tasas de éxito,
  resultados y nombres de herramientas o empresas.
- **B5:** el resumen del perfil, con las palabras de la persona y sin deducir.
- **B7:** "Eres el estratega" y "qué harías distinto" se reescriben. Quitar el ejemplo "Vender por encargo sin local"
  dejaba el título sin modelo, así que se cambia por un ejemplo neutro, que es texto nuevo.
- **B8 y B9:** la detección y la severidad del enlazador, solo con base en el texto.
- **B10:** las áreas y los supuestos del organizador.
- **C1:** el ejemplo del registro oficial. Quitar solo el paréntesis deja el ejemplo sin la instrucción de buscar.
- **C2:** el ejemplo "ya validaste el interés de dos instituciones".
- **C3:** "3 piezas", opcional.
- **C5, resto:** "lo adyacente que trae alguno de los nodos".
- **C6:** "(y cómo conseguirlos)" es un título fijo que también usa el código del reporte, y el ejemplo de $850/$170.
- **C7:** quitar los ejemplos de métodos de `REGLA_SIN_FUENTES` rompe la guarda `lib/procedencia.test.ts`, que fija la
  regla D5 del fundador (el método se nombra con su nombre neutro, por ejemplo "el ciclo PDCA"). No se toca sin su visto.
