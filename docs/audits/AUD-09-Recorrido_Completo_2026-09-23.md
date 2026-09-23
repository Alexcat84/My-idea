# AUD-09. Auditoría del recorrido completo, de la idea al cierre

**Fecha:** 23 sep 2026. **Commit auditado:** `13183d93` (main = staging = producción en myideaproject.com).
**Modo:** solo lectura. Ningún archivo de código tocado, ninguna API real llamada, ningún secreto leído.
**Método:** seis auditores en paralelo, uno por tramo, cada hallazgo con evidencia `archivo:línea` de los dos lados y cotejado contra `docs/PENDIENTES.md`. Los hallazgos de gravedad ALTA los re-verifiqué a mano en el código (marca **[V]**); el resto lleva la verificación del auditor de su tramo.

| tramo | alcance |
|---|---|
| A | portada, /nueva (tecleo y dictado), organizador, entrevista, redacción del plan, primera vista |
| B | proyecto vivo: tablero, stepper, estados, modo y fechas, scheduler, calendario, Tus Números, espacios, bitácora |
| C | seguimiento, avance cero, análisis, documentos, acta de cierre y celebración |
| D | mundos: vitrina, preview, compra, diagnóstico, plan, seguimiento, protección, cierre |
| E | transversal: censo de rutas y cobros, identidad y autorización, 2FA, voz y copy |
| F | continuidad de los nodos del núcleo y de los 9 mundos integrados (sin el mundo 11) |

Gravedad: **ALTA** = el usuario pierde dinero o datos, queda atascado, se le miente, o hay hueco de seguridad. **MEDIA** = incoherencia o contrato roto sin daño inmediato. **BAJA** = copy, comentario o documento desalineado.
Salvo que se diga lo contrario, todo hallazgo es NUEVO (no descrito en PENDIENTES).

---

## 1. ALTA

### Dinero y promesas

**H01. El seguimiento anuncia 10 créditos y cobra 5, en el núcleo y en los mundos. [V]** (C1, D2, E3)
`IdeaView.tsx:1034` entra a toda sesión de seguimiento con dominio `"core"`, así que los botones de `:1138`, `:1187` y `:1209` pintan `PRECIOS.plan_completo` (10). El servidor cobra `montoDelPlan(dominio, esSeguimiento)`, es decir 5 (`plan/route.ts:197`, `creditos.ts:116`). El ritual ya había dicho "Continuar mi idea · 5 créditos" (`ManosALaObra.tsx:653`). Quien tiene entre 5 y 9 créditos cree que no le alcanza.
Agravante en el mundo: si se recarga a mitad del seguimiento de un mundo, `IdeaView.tsx:512` toma el dominio real y el botón pasa a "Ver mi diagnóstico · gratis"; `diagnostico/route.ts:81-83` no distingue preview de seguimiento y `:117` sobrescribe `resumen_md` y `preview_session_id` del preview con la sesión del ciclo, que se cierra sin plan.

**H02. Un plan ensamblado sin IA se cobra a precio completo y el aviso nunca llega a la pantalla. [V]** (A2, C2)
Con el presupuesto de sesión agotado (0,35 USD, `costmeter.ts:41-48`), `plan/route.ts:87-88` arma el plan "sin narrar"; también cuando el redactor falla (`:119-121`). Se emite el evento `aviso` (`:247`) pero `IdeaView.tsx:437-465` solo atiende reinicio, delta, done y error. Luego se cobra igual (`:429-441`). La pantalla prometía "Si algo falla, no se cobra nada" (`IdeaView.tsx:1219`). El plan offline (`planRedactor.ts:474-490`) sale con "# Tu plan de accion" sin tilde, etapas con `titulo_concepto` (que pasan al checklist) y el perfil interno. Viola BANCO §5 y §9.
Antesala del mismo caso: con el presupuesto agotado cada turno responde `error_temporal` con `opciones` (`recorrido.ts:496-502`); la web las ignora y muestra el error genérico en bucle (`IdeaView.tsx:562-564`), mientras Python ofrece un menú de emergencia (`prototipo_motor.py:1936`). Y `presupuesto_excedido` nunca se marca, aunque el comentario de `costmeter.ts:139-146` diga que sí.

**H03. La pantalla se traga los mensajes honestos del servidor y dice "algo se atoró de nuestro lado". [V]** (A1, A3, C10, D4, D12, E2)
Solo 401 y 429 se distinguen en `IdeaView.tsx:318-325`, `:529-537`, `:1326-1334` (arranque) y `:427-431` (plan); `nueva/page.tsx:41-48` igual; `ManosALaObra.tsx:1904-1908` y `:1930-1932` muestran solo 429 y 402. Lo que se pierde:
- **402 sin saldo** ("Te quedan 0 créditos; esto cuesta 10"). La beta no tiene cortesía (`creditos.ts:21-33`): un usuario nuevo sin siembra que pulsa "Explorar estas suposiciones" lee que el problema es nuestro. Si el 402 llega al pedir el plan, reaparece la Claridad y "Explorar" abre una sesión nueva que oculta la entrevista completa (`api/idea/[id]/route.ts:152-182`). En la compra de un mundo, además, ya se había hecho `setPlanMd(null)` (`IdeaView.tsx:379-384`).
- **403 de 2FA**: quien no superó el desafío (por ejemplo tras recuperar la contraseña) recibe el genérico en toda acción pagada y ninguna pantalla le abre el desafío (solo `CuentaCliente.tsx:164` lo atiende).
- **400 por idea de más de 4000 caracteres** (`organizer/stream/route.ts:58-62`, `turn/route.ts:35-39`): un dictado largo falla siempre, el textarea no tiene tope ni contador (`CampoConVoz.tsx:50-62`) y reintentar no sirve.
- **409 del seguimiento** ("Ya recorriste todas las puertas", "Primero explora...", "Diste X por completado") y **503 del fusible** (`MENSAJE_FUSIBLE`).

### Pérdida de datos

**H04. Un seguimiento de mundo que termina en "cierre honesto" borra el mundo ya pagado. [V]** (C3, D1, E12)
`recorrido.ts:525-589` devuelve `cierreMundo` en cualquier sesión de mundo, sin mirar `esSeguimiento`; `apiSesion.ts:129` borra la fila de `project_unlocks` sin mirar `plan_pagado_at`. Se pierden `plan_pagado_at`, `completado_at`, `cierre_motivo` y el diagnóstico; el mundo sale de las pestañas, del análisis y del Expediente, su checklist queda huérfano, y volver exige preview y compra otra vez. El texto dice "Activé y exploré este mundo... puedes volver a entrar" (`apiSesion.ts:48-58`). Los comentarios de `apiSesion.ts:111-121` ("no hay ledger") y `recorrido.ts:535` ("con reembolso") son falsos hoy. En un seguimiento las puertas ya cubiertas están descartadas, así que agotarlas es más probable que en el preview.

**H05. Comprar un mundo después de un ciclo del núcleo usa el perfil congelado del preview y pisa el estado vivo del proyecto. [V]** (D5)
`PREVIEW_MUNDOS_PLAN.md §4`: el plan se genera con el estado vivo ACTUAL. El código usa `perfilSesion` y `textoOriginal` congelados al hacer el preview (`start/route.ts:192, 242`); `prepararPlan` solo inyecta `estado_vivo_previo` en seguimientos (`planRedactor.ts:217-220`). Después `plan/route.ts:411-416` escribe `estado_vivo` y `fase_actual` del proyecto sin condición: lo aprendido en el ciclo del núcleo se pierde para el motor, y la fase del proyecto pasa a ser la del último nodo del mundo (esto último, SOSPECHA de efecto).

**H06. El diagnóstico de un mundo puede quedar bloqueado para siempre. [V]** (D3)
`diagnosticoMundo.ts:17-19` promete un presupuesto propio "independiente del de sesión", pero `:77-81` pasa el tope de 0,10 USD junto con el acumulado de TODA la entrevista (`diagnostico/route.ts:99-101`). Si la entrevista costó 0,10 o más, `costmeter.ts:156` lanza antes de llamar y cada reintento da el mismo 502. `scripts/vuelo_preview.ts:21` estima entrevista, diagnóstico y plan en 0,15 a 0,25 USD; el vuelo no lo ve porque corta la entrevista pronto. Frecuencia: SOSPECHA; mecanismo: HALLAZGO.

**H07. La idea del invitado se queda sin dueño en tres caminos.** (A5, E5b)
- Confirmar el correo desde otro navegador: `auth/callback/route.ts:49-53` toma el id anónimo solo de la cookie del propio request; `registrar/route.ts:77-89` guarda el destino en una cookie de 30 minutos. El usuario ve /ideas vacío.
- Recuperar la contraseña en el mismo navegador: el ramal `type=recovery` (`callback/route.ts:66-68`) retorna antes de `bienvenidaTrasLogin`; el `anonId` capturado en `:53` no se usa.
- Si la adopción falla, solo queda en el log (`cuentas.ts:78-83`) y el usuario lee "esa idea no existe o no es tuya".
Contradice `AVISO_LOGIN` ("seguimos justo donde quedaste"). Solo se rescata con el script del fundador.

### Atascos sin salida

**H08. /nueva puede quedarse para siempre en "Organizando tu idea...".** (A4)
`nueva/page.tsx:71-73` solo detecta el cierre mudo si todavía no llegó `inicio`. Si llegó y el stream muere sin `done` ni `error` (timeout de la función), el estado no sale de "generando". La ruta del organizador no usa `garantizarTerminal` (finally de `stream/route.ts:217-220`), a diferencia de la del plan (`plan/route.ts:486-498`), que se creó justo por ese síntoma.

**H09. "Cargando tu espacio..." eterno.** (B-A3)
`IdeaView.tsx:951` exige `planMd && checklist`; si falta, `:1045-1050` pinta el mensaje sin salida, y `:250-254` se traga el fallo de `/checklist`. Camino reproducible: invitado en Claridad, Tus Números (visible sin plan, `PotenciaTuIdea.tsx:177`), "Activar", 401, login, vuelve a `?vista=manos` sin plan (`TusNumeros.tsx:535`), carga infinita.

### Fechas y avisos

**H10. "Recalcular pendientes" propone fechas ya vencidas. [V]** (B-A1)
El ancla del empaquetado es siempre la creación del plan (`ManosALaObra.tsx:795`, `:816`; `planCreatedAt` desde `IdeaView.tsx:973`), nunca hoy; al recalcular solo se quitan las hechas (`:871`). Contradice `empaquetado.ts:272-276` ("ninguna fecha del ritual puede nacer vencida"). Un plan de agosto recalculado en septiembre nace entero en ámbar. Lo mismo al pasar de "a mi ritmo" a "con fechas" tras meses. Ningún test cubre recalcular desde hoy.

**H11. El calendario suscrito sigue avisando lo que el usuario pausó, cerró o reemplazó. [V]** (B-A2, D10)
`calendar/feed/[token]/route.ts:32` lee todos los proyectos sin mirar `realizada_at`; `:37-41` lee los ítems de TODOS los planes, sin mirar `project_modos` ni `completado_at` del mundo; `:50` solo filtra hechas y retiradas; `ics.ts:96-100` pone una alarma por tarea. Contradice BANCO §5 ("sin fechas no hay recordatorios", "silencio para ideas cerradas"), `NOTAS_DE_DECISIONES.md:163-169` y "A mi ritmo: sin fechas ni presiones". El calendario de la app sí usa el plan vigente (`Calendario.tsx:117-120`): dos fuentes para lo mismo.

### Tus Números

**H12. Dos cifras de dinero distintas para lo mismo en la misma pantalla.** (B-A4)
`palancas.ts:217-222` redondea la meta hacia arriba (`:68-71`) y promete más unidades que la capacidad; la fila "A capacidad plena" de `tableroNumeros.ts:84-88` no. Ejemplo verificado: costo 180, precio 350, fijos 1200, 11 por semana: la palanca dice "45 al mes, te quedan $6.450" y la tabla "44 al mes, $6.300". En la misma frase (`TusNumeros.tsx:185`) pueden salir "A null ..." y "unidads" (deducido del código).

### Nodos

**H13. Cuatro puertas de mundo abren a un nodo sin pregunta y tres de ellas no tienen salida. [V]** (F1)
Sin entrada en `preguntas_cache.json`: `franquicias:principio_apalancamiento_numero_magico`, `compras:ten_un_checklist_de_clausulas_de_contrato`, `entrega:reconocer_mercancia_peligrosa_disfrazada`, `entrega:calcular_peso_dimensional_antes_cotizar`. La primera pregunta de un mundo sale de la caché (`world/[pack]/start/route.ts:261`); si falta, `graph.ts:264` escribe `Pensando en "<titulo_concepto>", cuentame...`: el título del libro en crudo y sin tildes. Las tres de compras y entrega tienen 0 sucesores: tras una respuesta la sesión pasa a `listo_para_plan` (`recorrido.ts:457`) y la entrevista del mundo dura una pregunta. Caso determinista: todo proyecto de franquicias en validación entra por la primera (`brecha_semillas.json:25`).

### Seguridad

**H14. Open redirect después del login. [V]** (E1)
`nextSeguro.ts:9-13` solo rechaza `//` y `/\` en la segunda posición. Un carácter de control en esa posición pasa el filtro y el parser de URL lo descarta, quedando `//otro-dominio` (comprobado con `new URL` de Node: resuelve a un dominio ajeno). Se usa en `auth/callback/route.ts:37-39`, alimentado por `api/auth/google/route.ts:32` y `api/auth/registrar/route.ts:28`, y en `login/page.tsx:41,106,216`. `nextSeguro.test.ts` no cubre caracteres de control. Cura corta: validar con `new URL(raw, origin)` y exigir el mismo origen.

**H15. La recuperación de contraseña se salta la allowlist de la beta. [V]** (E5)
`auth/callback/route.ts:66-68` retorna ante `type=recovery` antes de la allowlist (`:79-109`); `type` es un parámetro de la query. Un code válido de un correo no invitado (por ejemplo de Google) abre sesión real. Contradice `entrar/route.ts:29-30`. SOSPECHA adicional: la allowlist vive solo en rutas de la app (la migración 008 no tiene trigger ni hook); no pude ver el panel de Supabase.

**H16. Borrar la cuenta falla abierto sin 2FA si la lectura de seguridad falla. [V]** (E4)
`cuenta/eliminar/route.ts:40-47`: si `estadoSeguridad` o `desafioSuperadoEnSesion` lanzan, se registra en el log y el borrado irreversible sigue. Las rutas pagadas fallan cerradas. Latente: un atacante no lo provoca a voluntad.

---

## 2. MEDIA

### Conteos que no cuadran entre vistas
- **M01.** Header del stepper, chips de mundo y /ideas cuentan las tareas retiradas en el total (`IdeaView.tsx:761-771`, `:791`; `ideas.ts:86-88`, `:136-139`); Manos, el servidor y BANCO §5 cuentan activas (`ManosALaObra.tsx:249-256`, `checklist/route.ts:147-156`). Resultado: "3/10" frente a "3/9". (B-M1, C8)
- **M02.** Expediente y Reporte de mundo suman las acciones de todos los ciclos (`documentos/route.ts:70-89`, `:339`, `:370`, `:425`; `expediente.ts:249-257`; `analytics.ts:771`): con un seguimiento hecho, el tablero dice 3 de 25 y el Expediente "Completaste 22 de 53" y "22 de 25". Pariente de PENDIENTES:510, caso distinto. (C4)
- **M03.** El documento "Registro de X" de protección lee todos los ciclos (`documentos/route.ts:210-214`); la pantalla, el vigente. (D9)
- **M04.** El acta no es una foto: "Acciones al cerrar" se recalcula en vivo (`analytics.ts:754-758`, `AnalisisProyecto.tsx:143-148`) y la bitácora no guarda conteos (`realizar/route.ts:65`). (C6)
- **M05.** El PDF "Análisis del proyecto" conserva el "Cumplimiento por mundo" que D1 de PLAN_TODO_SEPARADO mató en pantalla (`analytics.ts:608`, `documentos/route.ts:303`, `AnalisisPapel.tsx:459-461`). (D11)
- **M06.** La cascada de "mover fecha" arrastra tareas de planes reemplazados (`mover-fecha/route.ts:80-84`, `:101-111`): desde Manos "5 que siguen", desde el calendario "3"; el servidor mueve 5. (B-M9)
- **M07.** El ritual reparte fechas a tareas hechas y retiradas y les descuenta capacidad (`ManosALaObra.tsx:871`, `:983-991`; `empaquetado.ts:303`); las hechas quedan como "Adelantadas". (B-M3)

### El cierre no cierra
- **M08.** Con la idea realizada se puede pagar un seguimiento y volver a cerrar reescribe la fecha: `follow/route.ts` no mira `realizada_at` (sí lo hace para un mundo, `:129-136`); Manos sigue mostrando el ciclo y "¿Tu idea ya es un proyecto?" (`ManosALaObra.tsx:2561-2586`); `realizar/route.ts:58-64` re-sella. Contradice §9.2 y "la historia no se reescribe". (C5)
- **M09.** `?vista=celebracion` abre la Celebración aunque la idea no esté cerrada, y "Reabrir" escribe una reapertura falsa (`IdeaView.tsx:162`, `:236`). Al revés, una idea realizada con un mundo abierto abre la Celebración al recargar el hub del mundo (`:503`, `:915`). (C17, B-M14)

### Fugas entre núcleo y mundo (contra TODO SEPARADO)
- **M10.** El bloque de realidad de un mundo usa el modo del núcleo (`bloqueRealidad.ts:141`, `:159`; `analyticsEntrada.ts:128-132`): el motor recibe "a mi ritmo" para un mundo con fechas, o al revés. (C7)
- **M11.** El ritual del mundo usa la cadencia del núcleo (`ManosALaObra.tsx:1556-1573`, `:2253`). (B-M16)
- **M12.** Una sola instancia de `ManosALaObra` sin `key` para los dos espacios: "Ponerlas después", "Recalcular" y "cambiar modo" se contagian entre núcleo y mundo (`IdeaView.tsx:970`; `ManosALaObra.tsx:1507`, `:1575-1576`). (B-M4)
- **M13.** Tras comprar o cerrar un plan de mundo, la vista del núcleo muestra ese plan como "Tu Plan", con su título en Manos y sus etapas en el Análisis, hasta recargar (`IdeaView.tsx:460`, `:336`, `:934`). (C16, D7)
- **M14.** "Mi bitácora" del núcleo es global y mezcla mundos (`ManosALaObra.tsx:2531`, `bitacora/route.ts:38-39`), contra BANCO §7.1. El calendario del núcleo en la app también es global y el canon se contradice (D3 de PLAN_TODO_SEPARADO frente a BANCO §7.1). (B-M8)
- **M15.** En protección, cada ciclo nuevo del núcleo rompe el registro y las anclas: `protege_item` apunta a ids del ciclo viejo (`plan/route.ts:351-379`); todo pasa a "la actividad que protegía ya no está en tu plan" (`registroProteccion.ts:125`) y las anclas P5 desaparecen sin aviso (`ManosALaObra.tsx:1638`). (D8)
- **M16.** La sesión de un mundo no está confinada a su mundo: `sucesoresNivel` usa el núcleo más todo mundo previsualizado (`db.ts:516`, `recorrido.ts:456`), y hay aristas vivas de mundo a núcleo (quality 38, environmental 13, health_safety 4) y de mundo a mundo (unas 22). SOSPECHA de efecto. (F5)

### Degradaciones silenciosas (contra BANCO §9)
- **M17.** `clasificar.ts:53-55` toma la primera puerta con perfil vacío si la clasificación falla; igual `juezSesion.ts:76-78`, `planRedactor.ts:628-631` y el respaldo de temas pendientes (`recorrido.ts:~222`). (A11)
- **M18.** `analyticsEntrada.ts:21-30`, `:68-75`, `:111-126` y `documentos/route.ts:78-87`, `:115-128`, `:341-354` ignoran errores de lectura: un fallo transitorio produce un Análisis, una Celebración o un bloque de realidad en cero presentado como verdad. (C11)
- **M19.** `registrarBitacora` (`db.ts:368-379`) envuelve en try/catch un insert de Supabase que nunca lanza: el error se pierde sin rastro, incluido el registro `cobro_carrera`. `mover-fecha/route.ts:115-119` y `baseline/route.ts:225` responden ok sin mirar el error del update. (B-M10, C11)
- **M20.** La narración de Tus Números cae a `reporteOffline` con `catch {}` (`reporte.ts:216-218`), se guarda como narración y cuenta contra el tope diario (`numeros/route.ts:315-334`). (E8)
- **M21.** El saldo cae a 0 si la consulta falla (`account/saldo/route.ts:26`, `creditos/page.tsx:121`, `ideas/page.tsx:51`). (E21, baja)

### Límites, puertas y cobros laterales
- **M22.** El fusible y el límite diario se gastan antes de verificar saldo y en los fallos (`session/start/route.ts:76-94`, `follow/route.ts:154-172`, reintentos de `stream/route.ts:74-81`): cinco clics sin saldo agotan el día. El canon §5 pide además rechazar antes de que el usuario escriba su "qué pasó"; el ritual se abre sin consultar saldo. (A8, C9)
- **M23.** `/api/project/[id]/report` invoca Sonnet sin cobro, sin fusible, sin límite y sin 2FA; ninguna pantalla lo llama, solo `vuelo.ts` y `probar.ts`. Cualquier cuenta puede repetirlo sin tope. (C13, E6)
- **M24.** Tus Números dice "Incluido con tu plan" pero `numeros/route.ts:204-320` no exige plan: activación y narración con IA quedan gratis sin plan. (E7)
- **M25.** La "carrera rara" del cobro dura toda la generación del plan: varias sesiones en paralelo con saldo para una se entregan todas y se cobra una. El comportamiento está anotado en `BETA_CUENTAS_README.md:44-45`; es NUEVO que la ventana no es rara. (E9)
- **M26.** Si algo falla después de `cerrarSesion` el reintento recibe 409 y el genérico; si falla entre `guardarPlan` y `cerrarSesion`, el reintento puede crear un segundo plan y checklist (SOSPECHA) (`plan/route.ts:305-416`). (A10, E15)

### La entrevista
- **M27.** Si el turno falla, la respuesta escrita se borra (`TarjetaPregunta.tsx:243-246`, `IdeaView.tsx:562-570`). (A7)
- **M28.** El organizador crea el proyecto antes de llamar a la IA (`stream/route.ts:96-97`): cada fallo deja un proyecto huérfano que /ideas presenta "Con claridad" y que abre una página vacía sin CTA (`IdeaView.tsx:1312`, `:1353`). (A6)
- **M29.** Dos definiciones de "entrevista abierta" (`ideas.ts:102` frente a `api/idea/[id]/route.ts:158-162`): "Una pregunta te espera" queda para siempre tras un diagnóstico de mundo no comprado o un `listo_para_plan`. (A14, B-M2)
- **M30.** `?entrevista=1` nunca se quita de la URL: recargar tras un cierre honesto arranca otra exploración y gasta un arranque (`IdeaView.tsx:520-541`). (A15)
- **M31.** El saldo del encabezado no se actualiza tras el cobro: `<ChipSaldo />` sin prop e `creditos_restantes` del `done` ignorado (`IdeaView.tsx:869`, `:458-462`). (A9)
- **M32.** El canon 03 define un aviso de precio antes de explorar y la app no lo muestra (`nueva/page.tsx:166-179`, `IdeaView.tsx:1312-1348`). (A12)
- **M33.** El plan cierra con "continua la conversacion en esta misma sesion" (sin tildes), cuando la sesión ya está cerrada y FLUJO §2 define una sola puerta; la lista incluye "MVP" (`planRedactor.ts:600-603`, `engine/constants.ts:15-18`). (A13)

### Bitácora e historia
- **M34.** La bitácora reescribe la historia: "Marcaste hecha" sale del `completed_at` vivo y deshacer lo borra; cada recálculo pisa `baseline_confirmada_at` (`bitacoraCliente.ts:159-186`, `checklist/route.ts:228-229`, `baseline/route.ts:229-232`), contra "Nada se reescribe" (`Bitacora.tsx:297-298`). (B-M6)
- **M35.** Tus Números no existe para la bitácora ni el Expediente: el tablero vivo escribe en `project_numeros_versiones`, y bitácora y documentos leen planes `reporte_numeros`, que solo crea `/report`. (B-M7)
- **M36.** Cada plan de seguimiento de un mundo se registra como `preview_a_compra` ("Sumaste el plan completo de X") e infla el dato comercial (`plan/route.ts:445-452`). (D6)
- **M37.** Un clic en la tarjeta de un mundo cuenta como "Mundo activado" en la Celebración y en el acta ("0 de 0, abierta") (`unlock/route.ts:42-47`, `analytics.ts:671`, `:759`). (D16, baja)

### Fechas y modo
- **M38.** A quien eligió su ritmo se le sigue hablando de fechas: "para el ..." y "Tardía · N días" sin mirar el modo (`ManosALaObra.tsx:421`, `DetalleActividad.tsx:31-43`, `:383`), contra BANCO §3. (B-M5)
- **M39.** El resumen del Expediente en PDF dice siempre "Vas por buen camino" y "Mantuviste tu ritmo cerca de tu plan" (`documentos/route.ts:421-432`), también en modo ritmo o con todo tardío. (C12)
- **M40.** La capacidad por defecto (5 a 10 horas) no se guarda si no se toca el chip (`ManosALaObra.tsx:882`, `:924-947`). (B-M15)
- **M41.** `mover-fecha` acepta tareas hechas y las pasa a "A tiempo" (`mover-fecha/route.ts:85-89`). (B-M17)
- **M42.** "Última acción" de /ideas usa `projects.updated_at`, que ni checklist ni fechas actualizan (`ideas.ts:154-156`). (B-M11)

### Tus Números y paridad
- **M43.** "Ganancia del mes" no descuenta fijos cuando faltan (`tableroNumeros.ts:75`). (B-M12)
- **M44.** El redondeo TS/Python difiere (`calculadora.ts:64-68` con `Math.round` frente a `round` al par de `calculadora.py:54-55`): margen 31,2% frente a 31,3% con costo 11 y precio 16. Contradice "paridad probada" de BANCO §6; `engine/test_calculadora.py:123-124` compara contra la misma expresión (regla del cálculo a mano de AGENTS.md). (B-M13)
- **M45.** La prueba de paridad de prompts es circular: nada compara contra `prototipo_motor.py`. Hoy la paridad real está bien (12 de 12 por AST). (A17)

### Mundos
- **M46.** Los documentos del mundo no alcanzan D4 (plan, seguimientos sueltos, bitácora y análisis): solo "Reporte de X" empaquetado; `?doc=ciclo:` solo resuelve ciclos del núcleo. PENDIENTES:189 da T7 por hecha. (D13)
- **M47.** `/creditos` promete antes de pagar que "cada mundo se refleja en la vista completa de tu proyecto", vista que BANCO §7.1 eliminó (`creditos/page.tsx:75`). (D14)
- **M48.** Si el enlace de protección falla al entregar el plan, no hay reintento y el registro sigue diciendo "se llenará con el plan de este mundo" (`plan/route.ts:351-379`, `ManosALaObra.tsx:1166-1169`). (D15)

### 2FA
- **M49.** El texto promete "un segundo paso al entrar protege tu cuenta" (`CuentaCliente.tsx:311`) pero el candado solo cubre cobros y borrados (`seguridad.ts:170-181`). (E10)
- **M50.** Re-enrolar TOTP con 2FA por correo activo cambia el método antes de verificar (`2fa/enroll/route.ts:93-99`): si se abandona el QR, solo se entra con código de rescate. (E11)

### Continuidad de nodos
- **M51.** Los 22 puentes "re-anclados al núcleo" solo cambiaron en `bridges_aprobados.json`; en el grafo servido siguen anclados en otros mundos (compras 13 aprobados y 8 reales, entrega 15 y 9, riesgos 13 y 2). El puente correctivo `matriz_probabilidad_impacto -> evalua_la_gravedad_sin_autoengano` no existe en el grafo. PENDIENTES:2590 lo da por CERRADA, y los guardianes leen el archivo, no las aristas. (F2)
- **M52.** La brecha de ejecución de compras y entrega apunta a nodos que no son semilla y se ignora en silencio (`evaluacionBrecha.ts:53-54`); `semillasDePack.test.ts:56` se titula "cada destino es una semilla real" y su cuerpo no lo prueba. (F3)
- **M53.** La ley del ancla se viola (`reglas_gestion_riesgo_gambling` ancla 3 puentes de riesgos) y `integrar_packs.py:198` tolera hasta 3; hay 61 aristas núcleo a mundo fuera de todo `bridges_aprobados`. (F4)
- **M54.** 50 nodos vivos del núcleo no se alcanzan caminando solo por el núcleo (28 solo tienen predecesores en mundos); el Gate da 100% porque ignora dominios. (F6)
- **M55.** 233 nodos vivos sin sucesor ofrecible, 37 en ideación o validación (ejemplos `ideacion_con_ia_en_la_sesion`, `critica_del_plan_con_ia`); al llegar, el recorrido corta en `listo_para_plan`. (F7)

---

## 3. BAJA

- **B01. Precios fuera de `precios.ts` (10/5/5/5/0).** Todos los tramos lo encontraron; AGENTS.md lo trata como bug.
  Documentos: `FLUJO_TRACKING.md` §4, §5 (5/2/3/2, Tus Números 2) y §9.4 (2/2 y "descuento en la entrega del primer turno", falso); `REGLAS_Y_TOKENS.md` §3 (packs 5/15/30, cortesía 20) y §4 (centro en /potenciadores, código por correo); `CUENTAS_DISENO.md:83-101`; `PREVIEW_MUNDOS_PLAN.md` (3 y 2, "Explóralo gratis"); `ANALISIS_PRECIOS.md:21` ("7 dominios"); BANCO §9 ("pagará 5 créditos"); mockups 03, 05, 07, 17, 18 y 20.
  Comentarios: `creditos.ts:14`, `:104-110`; `session/start/route.ts:86`; `plan/route.ts:13-15`, `:72`, `:128`, `:191-194`; `follow/route.ts:139-151`, `:163`, `:328-332`; `numeros/route.ts:230-232`, `:249-250`; `IdeaView.tsx:377-378`; `follow/route.test.ts:4`; `start/route.ts:152` y `recorrido.ts:528` ("pagó por explorar", el preview es gratis); `/dev/cierre` ("te devolvimos 3 créditos", público en producción).
- **B02. `FLUJO_TRACKING.md §7` obsoleta:** "Ajustar el plan", bloque de realidad, avance cero, sugeridor que aprende, cobro del follow y acta ya existen; "Contar qué pasó" hoy es "Ciclo de profundización".
- **B03. Copy contra BANCO:** "gratis" fuera de su frontera (`DetalleActividad.tsx:494`, `TusNumeros.tsx:337`, `:640`, `CorregirCifras.tsx:143`); "checklist" visible (`ManosALaObra.tsx:585`, `:604`, `:2115`, `:2418`, `:2641`); "línea base" (YA ANOTADO en parte, PENDIENTES:355-363); "Análisis del proyecto" antes del cierre; guion largo en el 409 de `follow/route.ts:205`; el guion largo como relleno visible de celdas vacías (`TusNumeros.tsx:62`, `:180`, `:184`, `Calendario.tsx:727`, `GanttCumplimiento.tsx:183`); cintillo de la portada "Calidad y Diseño en el MVP" (`Landing.tsx:303`); "El más elegido" sin respaldo (`creditos/page.tsx:179`); "te recuerda el día antes" frente a `TRIGGER:-PT0M` del mismo día (`SuscripcionCalendario.tsx:64-65`, `ics.ts:99`); "Yo te recuerdo" sin sistema de recordatorios; "Realizado" frente a "Realizada"; "Manos a la obra" frente a "Manos a la Obra"; píldora "Tus numeros de verdad" sin tilde; "Etapa detectada" y "Áreas de tu plan completo" anunciadas y retiradas; barra del plan "Vuelve a la entrevista cuando quieras".
- **B04. Canon de copy desalineado:** BANCO §2 dice 7 mundos (hay 9) y 5 etapas (hay 6 hitos).
- **B05. Pantalla de límite en /nueva:** "Ver planes" manda a la portada; el texto "5 arranques" está fijo aunque el número sale de `LIMITE_ARRANQUES_DIA` (`rateLimit.ts:125-134`).
- **B06. Claridad pintada en dos lugares con estilos divergentes** (`nueva/page.tsx:131-165` frente a `Claridad.tsx`): el arreglo del fundador se aplicó a una sola copia.
- **B07. Ruta JSON del organizador** (la que prueban los arneses) distinta de la real: sin reintentos, devuelve `data` sin limpiar y filtra `e.message`.
- **B08. Íconos:** compras y entrega caen al escudo de Calidad (`PotenciaTuIdea.tsx:58-122`, `CambiadorEspacios.tsx:62`).
- **B09. `catalogoMundos` se declara "la única puerta" y 17 archivos importan `packs_catalog.json` directo.**
- **B10. Nombres y etapas:** /ideas y el header calculan la etapa distinto en un seguimiento abierto; "Tu Plan" en "Tu avance" y en la bitácora toman fechas distintas; Tus Números muestra siempre "Tu idea" porque usa `titulo` crudo.
- **B11. Duplicados de una sola fuente que hoy coinciden:** vocabulario de estados (3 copias), clasificador de cumplimiento (2, redondeo distinto), `ORDEN_FASES` (4 copias), tres criterios para "hay mundos" en la etiqueta [Espacio].
- **B12. Validación laxa:** `PATCH /modo` acepta cualquier dominio y `project_modos.dominio` no tiene CHECK; `unlock` no revisa invitado ni plan del núcleo.
- **B13. Comentarios obsoletos:** "stepper de 5 etapas", "los 4 estados", `proxy.ts:6-8` ("el login llegará en una fase futura"), `rateLimit.ts:18-22` ("la credencial vive en el repo"), cortesía en `entrar` y `registrar`, cabeceras "NO APLICAR" de 020 y 021, evento de bitácora prometido en `checklist/route.ts:312-314` que no existe.
- **B14. Sospechas menores:** el micrófono se apaga en silencio si se niega el permiso; el texto provisional del dictado no entra si se pulsa Continuar mientras se dicta; "ya" como subcadena en `detectarDecisionPlan` ("playa" cuenta como "generar ya"); el feed usa la hora UTC del servidor; `world/start` permite re-arrancar un mundo comprado sin checklist.
- **B15. Nodos, cosmético:** 27 aristas de vivo a deprecado sin cablear al superviviente; huecos de semillas por fase no declarados (quality, environmental y franquicias sin ideación ni validación, entre otros) y mapas de brecha que apuntan a otra fase; etiquetas repetidas ("Asegura tu crédito de exportación" dos veces en exportación; tres pares núcleo y mundo); 44 etiquetas por encima del tope del SOP y 7 con anglicismo; títulos desactualizados en `packs_entry_seeds.json`; 31 de 47 nodos de entrega y 13 de 46 de compras con palabras sin tilde (PENDIENTES:2473 decía uno).
- **B16. Tests ausentes** donde viven H04 a H06: sin tests de `unlock`, `start`, `diagnostico`, ni del seguimiento de mundo hasta su plan, ni de `cierreMundo` en un seguimiento.

---

## 4. Revisado y sano

- **Cobro del plan:** verificación al inicio, descuento a la entrega con clave idempotente `plan:{sessionId}`, reembolso si revienta antes del `done`, carrera registrada sin castigar. `precios.ts` es la única fuente de montos en rutas y botones; `packs_catalog.json` ya no lleva precios; el único cobro vivo está en la ruta del plan.
- **SQL de créditos (020 a 024, 038):** deducción atómica con guard de saldo, idempotencia con índice único, REVOKE a anon y authenticated, sin montos negativos, CHECK de saldo no negativo.
- **Autorización:** toda ruta `/api/project/[id]/*` usa el cliente RLS del usuario con políticas por dueño; el cliente admin solo aparece donde el usuario sale del JWT. La adopción no puede tomar ideas ajenas.
- **2FA:** candado de intentos, anti-replay de TOTP, código por correo con hash y pimienta, rescate de un solo uso. Feed del calendario con HMAC en tiempo constante.
- **Motor:** 12 de 12 prompts idénticos entre Python y web; constantes con paridad (la diferencia de `MIN_SCORE_SALTO` está documentada); `etiquetaArbol` en riel, cintillo, diagnóstico y puertas; recarga a mitad de entrevista la reanuda; botones protegidos contra doble envío.
- **Tramo B:** CHECK de estados igual a `CHECKLIST_ESTADO`; modo y capacidad por espacio; aritmética del empaquetado probada a mano; fórmulas, umbrales GIGO e `ingreso_perdido_estimado` idénticos entre TS y Python; ninguna ruta de registro cobra.
- **Seguimiento y cierre:** una sola puerta al ritual; muros del follow de mundo correctos; caso avance cero como dice el canon; acta con motivo opcional que no se pisa; completar un mundo no toca `realizada_at`; `sinProcedencia` en todas las descargas.
- **Nodos:** 0 referencias rotas en todo el grafo; dataset, master del dataset y master de la web idénticos (3853); ningún nodo vivo sin vector, sin familia ni sin `etiqueta_arbol`; semillas vivas y de su dominio; dentro de cada mundo el 100% de sus nodos se alcanza desde sus semillas; los 10 dominios (núcleo y 9 mundos) coinciden en todos los lugares donde se definen; ningún ciclo atasca el recorrido.
