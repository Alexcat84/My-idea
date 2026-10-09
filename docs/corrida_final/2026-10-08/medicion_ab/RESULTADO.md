# Medición barata: A (solo reglas) contra B (reglas + verificador)

Decisión del fundador (8 oct 2026): volver a redactar los 14 planes del vuelo desde las entrevistas guardadas, sin
guardar nada, y pasarlos por el mismo juez de fidelidad (trampas sin marca, árbitro, umbral 0), en dos versiones:
**A** = solo las reglas del día (moneda desde lo que dijo la persona, datos del negocio como pregunta, "lo que este
plan aún no cubre" contra las etapas reales, costo total con tiempo nunca como costo de materiales);
**B** = A + el verificador (Sonnet 5.5, solo quita o convierte en pregunta, tope del 20 %), sin desplegar
(`VERIFICADOR_PLAN` apagado en producción). Tope de gasto: 2 USD de API.

Regla de cierre fijada de antemano: si B pasa con 0 contrarios, 0 invenciones y 0 procedencias se despliega el
verificador; **si B no pasa, se para y se reporta con la evidencia, sin arreglar.**

## Veredicto: B NO PASA (y A tampoco)

| | A (solo reglas) | B (reglas + verificador) | Umbral |
|---|---:|---:|---:|
| Hallazgos sostenidos por el árbitro | **14** (11 invenciones, 3 contrarios, 0 procedencias) | **10** (7 invenciones, 3 contrarios, 0 procedencias) | 0 |
| Planes con al menos un sostenido | 7 de 14 | 8 de 14 | 0 |
| Hallazgos brutos del juez (antes del árbitro) | 26 | 21 | n/a |
| Descartados por el árbitro | 12 | 11 | n/a |
| Trampas sin marca cazadas | 3 de 3 | 3 de 3 (una solo en la relectura de f014) | todas |
| Semilla de las trampas (escrita antes) | 20261012 | 20261013 | n/a |

Referencia: el tramo C del vuelo original (sin los arreglos de hoy) dio 11 sostenidos en 7 de 14 planes
(9 invenciones, 2 contrarios).

## Lectura honesta de la comparación

- **A y B salen del MISMO borrador** de cada plan: B es A con las ediciones del verificador (solo quita o convierte en
  pregunta; no puede añadir). Por eso A contra B aísla el efecto del verificador, y lo que difiere entre ambos en un
  mismo plan es lo que el verificador tocó más el ruido del juez y del árbitro (ver abajo).
- **El verificador no cierra la brecha.** Baja los sostenidos de 14 a 10, pero B sigue lejos del umbral 0 y afecta a 8
  planes de 14 (A, 7). Es una sola pasada del juez y del árbitro por versión.
- **Las reglas solas (A) no bajaron el nivel del vuelo original** (11 antes, 14 ahora, con planes redactados de nuevo).
- **El verificador aplicó 85 de 88 propuestas, ninguna a revisión** (el tope del 20 % no se tocó). Lo que deja pasar
  son sobre todo (a) inventos de negocio plausibles que el propio verificador no ve como inventos (empleados que tocan
  el canal de ventas, polvo y cemento sin protección, "porque el correo recupera las demás cuentas"), y (b) errores de
  cálculo u orden que no son "frases sin respaldo" sino contrarios al nodo (restar abandono menos nuevos, meta de
  piezas defectuosas aceptadas por lote, «los números del plan anterior siguen vigentes» cuando nadie los había calculado). Un verificador que solo quita o pregunta no
  corrige un contrario.
- **Ruido del juez y del árbitro, declarado:** como A y B comparten borrador, una frase que sobrevivió en las dos tuvo
  veredicto distinto según la versión: B f006 marca como invención «el correo es lo primero porque con él se
  recuperan las demás cuentas» en un plan donde el juez de A no la marcó, y frases idénticas se resolvieron distinto
  (p. ej. «y ya decidiste empezar esta semana» y «el margen con el cemento nuevo aún no está recalculado»: SOSTENIDAS en
  A f002, DESCARTADAS en B f015). Con ese margen, el umbral 0 es muy sensible a un solo caso límite.

## Coste

| Pieza | USD |
|---|---:|
| Redactor, 14 planes (un borrador por plan, compartido por A y B) | 1.1161 |
| Verificador (Sonnet 5.5), 14 planes | 0.7502 |
| **Total de API de la medición** | **1.8664** (tope 2,00) |

Los jueces y árbitros corrieron como subagentes del entorno de desarrollo (no pasan por la API del producto ni por la
consola del fundador). Verificador por plan: media 0.0536 USD (mín 0.0307, máx 0.0893).

## Version A, por plan

| Paquete | Plan | Espacio | Hallazgos del juez | Sostenidos por el árbitro | Descartados |
|---|---|---|---:|---|---:|
| f001 | b4a01dea | core (plan_nucleo) | 1 | 0 | 1 |
| f002 | deb138a3 | quality (plan_mundo) | 3 | invencion, invencion | 1 |
| f003 | ff010188 | risk_management (plan_mundo) | 4 | contrario, invencion, invencion | 1 |
| f004 | 8b7764c4 | primer_equipo (plan_mundo) | 5 | invencion, invencion, invencion, invencion | 1 |
| f005 | 9909f451 | core (plan_nucleo) | 0 | 0 | 0 |
| f006 | ee6de956 | core (plan_nucleo) | 1 | contrario | 0 |
| f007 | aad2749d | core (plan_nucleo) | 0 | 0 | 0 |
| f008 | fb027af0 | core (plan_nucleo) | 2 | 0 | 2 |
| f010 | 31ebf0ea | core (plan_nucleo) | 3 | 0 | 3 |
| f011 | 85248377 | health_safety (plan_mundo) | 2 | 0 | 2 |
| f012 | 0e481ad8 | health_safety (plan_mundo) | 0 | 0 | 0 |
| f014 | f14f36e7 | seguridad_digital (plan_mundo) | 1 | invencion | 0 |
| f015 | 265e4486 | quality (plan_mundo) | 2 | invencion, invencion | 0 |
| f016 | c73e86f8 | core (plan_nucleo) | 2 | contrario | 1 |

### Sostenidos de A

- **f002** (quality, invencion): «y ya decidiste empezar esta semana»
  - Evidencia: contexto.lo_que_conto (health_safety): a '¿Con qué te sentirías más cómodo para empezar esta semana...?' respondió 'Con eso me basta por ahora.'; lo único dicho es 'Quiero proteger mi salud sin frenar la produccion.' La frase 'Ya elegiste por dónde empezar' es de una pregunta de la IA, no de la persona.
  - Razón: Atribuye a la persona una decisión (empezar esta semana) que ella nunca declaró; su respuesta es una evasiva, no una elección.
- **f002** (quality, invencion): «El proveedor nuevo baja el cemento un veinte por ciento y todavía no lo metes en la cuenta.»
  - Evidencia: contexto.lo_que_conto (core): la persona dijo solo 'el proveedor nuevo me baja el cemento un 20%'; la IA preguntó '¿ya recalculaste... o todavía no lo has metido en la cuenta?' y ella respondió otra cosa (lotes de 10 vs por pedido). Ningún nodo ni dato lo afirma.
  - Razón: Que no haya recalculado es un hecho que nadie dio (la pregunta quedó sin contestar); es plausible, pero se presenta como dato de la persona (y se repite en la intro).
- **f003** (risk_management, contrario): «Tu mayor riesgo declarado es proteger la cuenta de Instagram»
  - Evidencia: contexto.lo_que_conto (risk_management): 'Mi mayor riesgo es que dependo de un solo proveedor de resina... Quiero aprender a verlo venir a tiempo.' y contexto.perfil_sesion: 'Dijo que su mayor riesgo es depender de un solo proveedor de resina'; la respuesta sobre Instagram fue 'Con eso me basta por ahora'
  - Razón: Lo que la persona declaró como su mayor riesgo es el proveedor de resina; Instagram es su prioridad de protección, no su mayor riesgo declarado. La salida invierte el orden, y relega el riesgo que ella nombró a un 'se suman'.
- **f003** (risk_management, invencion): «trabajar sin protección con cemento y polvo»
  - Evidencia: Ningún nodo ni el contexto (idea, lo_que_conto, ficha, perfil_sesion) menciona seguridad física, equipo de protección, cemento o polvo como riesgo de la persona.
  - Razón: Es un hecho del negocio que nadie dio, presentado como un riesgo que ella tiene; es plausible pero inventado.
- **f003** (risk_management, invencion): «Marca los que minimizaste porque no quieres enfrentarlos, por ejemplo el respaldo de tus contactos o el cemento y polvo sin protección»
  - Evidencia: Nodo evalua_la_gravedad_sin_autoengano solo da el paso genérico 'Marca los riesgos donde notas que minimizaste algo que no quieres enfrentar'; el respaldo de contactos sí lo contó ella ('No tengo copias de seguridad'), pero 'cemento y polvo sin protección' no aparece en ningún nodo ni en el contexto.
  - Razón: El ejemplo del respaldo está sostenido, pero el ejemplo 'cemento y polvo sin protección' repite el hecho inventado y lo pone como algo que ella minimiza; esa parte no se sostiene.
- **f004** (primer_equipo, invencion): «Hoy no hay escrito qué se espera de cada uno»
  - Evidencia: contexto.lo_que_conto primer_equipo: a '¿cuánto tienes ya por escrito...?' y '¿tienes escrito qué resultados concretos esperas...?' respondió 'no sé dirigirlos...' y 'Nunca he tenido reuniones a solas con ellos'; ninguna respuesta dice que no haya nada escrito.
  - Razón: Es un hecho del negocio que la persona esquivó y nunca declaró; se infiere de su silencio y se afirma como dado. Plausible, pero nadie lo dijo.
- **f004** (primer_equipo, invencion): «Un puesto bien definido te quita de encima el trabajo que terminas haciendo tú.»
  - Evidencia: crear_tarjeta_puntuacion_puesto y definir_resultados_tarjeta_puntuacion: la tarjeta fija misión, resultados y competencias y da claridad a quien llega ('Esa claridad libera a quien llega'); ningún nodo promete que libere al dueño de su propio trabajo.
  - Razón: Promete un resultado (dejar de hacer el trabajo él mismo) que ningún nodo respalda; el nodo habla de claridad para el empleado y alineación con la estrategia.
- **f004** (primer_equipo, invencion): «Con dos personas nuevas en el taller empiezan a surgir cuestiones de convivencia.»
  - Evidencia: debatir_decidir_asuntos_cultura_evitar_delegar describe asuntos de cultura que tientan a delegar, no que ya estén surgiendo; en contexto la persona no menciona ningún problema de convivencia (solo entrega tardía y falta de reconocimiento).
  - Razón: Afirma como hecho presente del taller un fenómeno que ni la persona ni los nodos dicen; es una causa/situación inventada para justificar la etapa.
- **f004** (primer_equipo, invencion): «tus empleados van a tocar el canal de ventas»
  - Evidencia: contexto: los contrató 'para el taller'; el Instagram es su canal, con prioridad declarada de protegerlo; nada dice que los empleados vayan a tener acceso. El propio paso 2 de la etapa lo trata como condicional ('Si algún empleado va a tener acceso').
  - Razón: Se afirma como hecho futuro algo que la persona no contó y que el mismo plan trata después como hipótesis; es un hecho del negocio inventado para conectar la prioridad de Instagram.
- **f006** (core, contrario): «Resta lo segundo de lo primero para ver tu velocidad real de crecimiento.»
  - Evidencia: motor_crecimiento_pegajoso, paso 3: 'Calcular la tasa de crecimiento compuesto (adquisición - churn)'; resumen: 'restar la tasa de churn a la tasa de crecimiento natural'. Salida, Etapa 4 paso 2: 'cuántos clientes abandonan por periodo y cuántos nuevos entran' (primero = abandono, segundo = nuevos).
  - Razón: 'Restar lo segundo de lo primero' es abandono menos nuevos, el signo opuesto al del nodo (nuevos menos abandono). La lectura literal es inequívoca y el orden del paso 2 de la salida invirtió el del nodo.
- **f014** (seguridad_digital, invencion): «o si pierdes Instagram, pierdes pedidos y contactos, y hoy no tienes forma de escribirle a tus compradores fuera de esa cuenta»
  - Evidencia: contexto.lo_que_conto (seguridad_digital): las cuatro preguntas sobre si tiene otra forma de avisar a sus clientes o tiene los pedidos/datos fuera de Instagram se responden solo con 'Con eso me basta por ahora.'; lo unico que contó es 'No tengo copias de seguridad; si pierdo el celular pierdo los pedidos y los contactos' y 'Hoy guardo los datos de mis clientes en un Excel sin clave y en el celular'. Ningun nodo lo dice.
  - Razón: La parte del celular está contada por la persona, pero que perder Instagram signifique perder pedidos y contactos y que hoy no tenga ninguna forma de escribirles fuera de la cuenta es un hecho que nunca dio: lo eludió, y sus datos en Excel/celular apuntan más bien a lo contrario. La propia Etapa 3 admite que esa pregunta 'quedó sin contestar', así que afirmarlo como hecho es invención.
- **f015** (quality, invencion): «Etapa 6: Anota qué lleva cada kit de huerto»
  - Evidencia: 'kit'/'huerto' solo en la salida; ni nodos ni contexto lo mencionan; la persona solo hace macetas de cemento.
  - Razón: La etapa entera presupone un producto que nadie dio.
- **f015** (quality, invencion): «Te preocupa que el sustrato de tus kits salga dispar, y no tienes escrito qué lleva cada uno.»
  - Evidencia: Las quejas contadas son burbujas y acabados irregulares entre lotes; ningún nodo menciona sustrato.
  - Razón: Atribuye a la persona una preocupación y un hecho que no contó.
- **f016** (core, contrario): «Los números de costo, canal y punto de equilibrio del plan anterior siguen vigentes y no se repiten aquí.»
  - Evidencia: contexto.estado_vivo: 'sin que aún se haya medido nada con sus cifras' y 'Quedan por resolver cuántas macetas necesita vender al mes... cómo compara el margen entre tienda e Instagram'; mensaje_entrada: 0 de 33 acciones hechas. plan_anterior solo tiene el costo 130 como cifra; margen por canal y punto de equilibrio estaban como pasos por hacer.
  - Razón: No existen números de canal ni de punto de equilibrio vigentes (nada se midió, 0/33), y el costo de 130 la propia salida lo declara obsoleto por el cemento; además las etapas 1 y 5 sí repiten esos cálculos, así que la frase afirma lo opuesto al estado real.

## Version B, por plan

| Paquete | Plan | Espacio | Hallazgos del juez | Sostenidos por el árbitro | Descartados |
|---|---|---|---:|---|---:|
| f001 | 0e481ad8 | health_safety (plan_mundo) | 0 | 0 | 0 |
| f002 | aad2749d | core (plan_nucleo) | 0 | 0 | 0 |
| f003 | 9909f451 | core (plan_nucleo) | 0 | 0 | 0 |
| f004 | c73e86f8 | core (plan_nucleo) | 1 | contrario | 0 |
| f005 | 8b7764c4 | primer_equipo (plan_mundo) | 2 | invencion, invencion | 0 |
| f006 | 31ebf0ea | core (plan_nucleo) | 2 | invencion | 1 |
| f007 | b4a01dea | core (plan_nucleo) | 2 | 0 | 2 |
| f008 | f14f36e7 | seguridad_digital (plan_mundo) | 1 | invencion | 0 |
| f009 | ff010188 | risk_management (plan_mundo) | 2 | invencion | 1 |
| f010 | 85248377 | health_safety (plan_mundo) | 3 | invencion | 2 |
| f012 | ee6de956 | core (plan_nucleo) | 1 | contrario | 0 |
| f013 | 265e4486 | quality (plan_mundo) | 3 | invencion, contrario | 1 |
| f015 | deb138a3 | quality (plan_mundo) | 2 | 0 | 2 |
| f016 | fb027af0 | core (plan_nucleo) | 2 | 0 | 2 |

### Sostenidos de B

- **f004** (core, contrario): «Los números de costo, canal y punto de equilibrio del plan anterior siguen vigentes y no se repiten aquí.»
  - Evidencia: contexto.estado_vivo: 'Quedan por resolver cuántas macetas necesita vender al mes para cubrir gastos... cómo compara el margen entre tienda e Instagram'; mensaje_entrada: 0 de 33 acciones hechas. plan_anterior: etapas 2 y 4 solo dan pasos para calcular margen por canal y punto de equilibrio, no cifras. La propia salida los repite en Etapa 5 (margen por canal, punto de equilibrio) y Etapa 7.
  - Razón: La frase presenta como ya existentes y vigentes unos números de canal y punto de equilibrio que nadie ha calculado (el estado vivo los da por pendientes), y dice que no se repiten cuando las etapas 5 y 7 sí los retoman. Solo el costo de 130 es un dato real de la persona.
- **f005** (primer_equipo, invencion): «tus empleados van a tocar el canal de ventas, y de ti depende que sepan cómo cuidarlo»
  - Evidencia: contexto.ficha.dijo_textual: los empleados fueron contratados 'para el taller'; la prioridad es 'proteger la cuenta de Instagram, su canal principal de ventas'; ningún dato ni nodo dice que los empleados accederán a Instagram o al canal de ventas (el nodo recorrer_rueda_conscientemente_cultura_equipo y los demás tratan solo de contratar, dirigir y cultura).
  - Razón: Une la prioridad real de la persona con un hecho del negocio que nadie dio (que los empleados manejarán el canal de ventas). Es un hecho inventado, no consejo operativo.
- **f005** (primer_equipo, invencion): «una regla clara de quién accede a las cuentas del taller»
  - Evidencia: Los pasos de la Etapa 7 (1, 3, 5: conversación regular, reconocer, revisar el ciclo) no producen ninguna regla de acceso; ningún nodo la enseña. La persona habló de quién puede entrar a sus cuentas (contexto, 'me preocupan las contrasenas y quien puede entrar a mis cuentas') pero nunca vinculó a los empleados con ellas.
  - Razón: El entregable promete algo que ningún paso ni nodo produce y que descansa sobre la premisa inventada de que los empleados tocan las cuentas. Es la misma invención de la primera frase.
- **f006** (core, invencion): «El correo es lo primero porque con él se recuperan las demás cuentas.»
  - Evidencia: Ningún nodo del paquete (redes sociales, referidos, SEO, apalancamiento, soporte, unidad individual) trata de cuentas o recuperación. La persona solo contó: 'Uso la misma contrasena para el correo, Instagram y el banco, y no tengo verificacion en dos pasos' y 'Me preocupa que me roben la cuenta de Instagram'. La idea de que el correo recupera la cuenta aparece solo en una PREGUNTA del sistema (seguridad_digital: 'el correo es lo que te recuperaría la cuenta si algo falla'), no en una respuesta suya.
  - Razón: Cambiar primero el correo es consejo operativo, pero la frase añade una causa presentada como hecho que ningún nodo dice y la persona no dio; lo que el sistema afirmó en su propia pregunta no la sostiene. Es plausible, pero por la rúbrica una causa que nadie dio es invención.
- **f008** (seguridad_digital, invencion): «porque quien controla tu correo puede recuperar todo lo demás»
  - Evidencia: csf_funcion_protect solo dice 'MFA en todas las cuentas que lo permitan, comenzando por las más sensibles (banca, cuentas de correo, gestores de contraseñas)', sin dar el motivo. En contexto.lo_que_conto la frase 'el correo es lo que te recuperaría la cuenta si algo falla' es de la pregunta del sistema, no de la persona (su respuesta fue 'No tengo copias de seguridad...'). Ningún otro nodo (identificacion_autenticacion_mfa, gestion_contrasenas_cui, csf_funcion_identify) da esa causa.
  - Razón: Es una causa (el correo como llave de recuperación de todas las demás cuentas) que ningún nodo dice y la persona no contó; plausible y de bajo impacto, pero la rúbrica cuenta como invención una causa que nadie dio. El orden 'correo y banco primero' sí está respaldado, solo el 'porque' no.
- **f009** (risk_management, invencion): «A eso se suman depender de un solo proveedor de resina, el defecto de burbujas entre lotes y trabajar sin protección con cemento y polvo.»
  - Evidencia: El contexto (mensaje_entrada, perfil_sesion, lo_que_conto, ficha) no menciona protección, polvo ni salud en el taller; la persona contó resina (risk_management), burbujas (quality) y contraseñas/copias (seguridad_digital). Ningún nodo habla de equipo de protección o polvo; haz_tu_lista_de_lo_que_puede_fallar solo da ejemplos genéricos (depender de ti, perder un cliente, quedarte sin dinero). Se repite en Etapa 3: 'el cemento y polvo sin protección'.
  - Razón: Afirma como hecho de su negocio una condición de trabajo que la persona nunca contó y ningún nodo dice; es un dato inventado presentado como riesgo suyo, no un consejo operativo.
- **f010** (health_safety, invencion): «se integra en cada etapa sin sumar más trabajo»
  - Evidencia: Contexto: "Quiere proteger su salud sin frenar la produccion" (no pide ni nadie dice "sin sumar trabajo"). Ningun nodo (p. ej. implementacion_controles, prevencion_control_peligros) promete que un control no suma trabajo. La salida misma dedica la Etapa 3 completa, con pasos nuevos, al polvo y al cemento.
  - Razón: Promete un resultado (proteccion sin trabajo extra, repartida en cada etapa) que ni la persona ni ningun nodo respaldan; la persona pidio no frenar el ritmo, que no es lo mismo, y el plan contradice la promesa con sus propios pasos.
- **f012** (core, contrario): «Resta lo segundo de lo primero para ver tu velocidad real de crecimiento.»
  - Evidencia: motor_crecimiento_pegajoso, paso 3: 'Calcular la tasa de crecimiento compuesto (adquisición - churn)'; resumen: 'resulta de restar la tasa de churn a la tasa de crecimiento natural'. En la salida, el paso 2 de la Etapa 4 fija el orden: 'Calcula cuántos clientes abandonan por periodo [lo primero] y cuántos nuevos entran en el mismo periodo [lo segundo]'.
  - Razón: 'Restar lo segundo de lo primero' da abandono menos nuevos, que es el signo opuesto a la fórmula del nodo (adquisición menos abandono). Además deja incoherente la frase siguiente ('si es baja aunque entren muchos clientes nuevos'), porque con ese orden la cifra sale baja precisamente cuando el negocio va bien.
- **f013** (quality, invencion): «Etapa 6: Anota qué lleva cada kit de huerto»
  - Evidencia: La palabra 'kit'/'huerto' aparece solo en la salida; ningun nodo ni el contexto (idea, lo_que_conto, ficha, dijo_textual) la menciona. La persona solo hace macetas de cemento chicas y medianas.
  - Razón: La etapa entera (titulo, pasos y primera accion 'Arma el proximo kit') presupone un producto que nadie dio; el '¿Vendes kits?' no lo salva porque el titulo y el entregable ya lo afirman.
- **f013** (quality, contrario): «Fija una meta visible, por ejemplo cuántas piezas con defecto aceptas por cada lote»
  - Evidencia: cero_defectos, paso: 'Eliminar el lenguaje que normaliza niveles aceptables de error (AQL)'; programa_cero_defectos: 'los defectos no son algo que simplemente hay que aceptar'.
  - Razón: Aunque medicion_calidad pide 'metas de mejora visibles', el ejemplo propuesto es una cuota de defectos aceptados por lote, que es justo el nivel aceptable de error (AQL) que el nodo manda eliminar.

## Archivos

`A/` y `B/`: los 14 planes redactados de nuevo (nunca guardados en la base). `veredictos_A/` y `veredictos_B/`: hallazgos
del juez (`fNNN.json`), relectura de la trampa de B (`f014_relectura.json`) y árbitro (`arbitro_fNNN.json`; el de A f015
está transcrito del informe del árbitro, que no escribió su archivo). `claves_A.json` y `claves_B.json`: qué paquete es
trampa y de cuál plan sale cada paquete real. `costes.json` y `redaccion.log`: costes por plan y por pieza y lo que
propuso y aplicó el verificador, frase por frase. Guiones: `web/scripts/corrida_final_redactar_planes.ts` y
`web/scripts/corrida_final_paquetes_ab.ts`.

## Estado y qué NO se hizo

- El verificador **no se desplegó** (la regla de cierre lo impide). Sigue apagado por defecto.
- No se arregló nada de lo hallado. Lo que queda es decisión del fundador.
- `.env` raíz: se queda hasta la decisión; la cifra final de la consola sigue pendiente de anotar.
