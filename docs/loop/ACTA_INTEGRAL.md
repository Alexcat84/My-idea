# ACTA INTEGRAL DE CIERRE DE CAMPAÑA (9 sep 2026)

**Auditor integral, con el fundador delante.** Se escribe POR ANEXION conforme
avanza, no al final. Toda cifra sale de un instrumento corrido en esta sesion;
toda cita lleva su linea. Mapa de herencias: `docs/loop/PARA_ALEXIS.md`
(248 lineas, cierre del bucle del 9 sep 2026).

**Estado de partida, medido:** rama `pasada-unica`, HEAD `6dbfb9c0`, arbol
limpio, `origin` sin diferencia.

---

## PASO 0. HIGIENE: EL TURNO RESIDUAL DEL CORTE, CERRADO

`python scripts/loop/apertura_del_auditor.py --cerrar-turno --vuelta "220-cola"`
corrido en esta sesion. Salida literal: *vuelta registrada en cerrados: 220-cola;
el fichero del turno NO se borra; un turno NUEVO lo cargara como CERRADO y
empezara limpio SIN borrar nada*. Vueltas cerradas en el fichero tras el acto:
`206 ... 220, 220-cola`.

**Un matiz que se dice en vez de callarlo:** `--estado` sigue diciendo
`TURNO VIVO ABIERTO: SI` despues del cierre. Es el diseño declarado por el propio
instrumento (el fichero no se borra; el turno nuevo lo carga como cerrado), no un
fallo del cierre. Arbol limpio antes y despues.

---

## PASO 1. LAS DECISIONES DEL FUNDADOR, Y LO MEDIDO ANTES DE APLICARLAS

### 1.a LAS CLAUSULAS A MEDIAS: DOS LIBROS DISTINTOS, MEDIDOS

**El lector de las 17 clausulas** (`docs/loop/SALIDA_V220_T1_RECORRIDA_DEL_LECTOR.txt`,
lineas 238 a 254, filas 0 CODIGO a 07 ADUANA) deja **tres** en A MEDIAS:

| fila | fase | idx | clausula |
|---:|---|---:|---|
| 6 | `03 FUSIONES` | 0 | un superviviente por acto, el resto DEPRECADO CON ALIAS |
| 11 | `05 SANEO` | 1 | los tres de Incoterms con su version |
| 17 | `07 ADUANA` | 0 | los cuatro controles mecanicos corriendo en Gate 0 |

**Y la ficha `OP-I-01` tiene su propio libro de cuatro puntos** (leidos de
`docs/plan/OPERACIONES.jsonl`): idx 0 fecha_corte, idx 1 PROVISIONAL, idx 2
*todo hueco NOMBRADO, nunca rellenado*, idx 3 *el inventario se recomputa entero
con el disparador*. La correccion de la vuelta 214 (misma ficha, campo
`evidencia`) los re-midio: **2 en CUBRE, 2 en A MEDIAS (idx 2 y idx 3)**. El idx 3
es **la vista humana** (`docs/plan/10_INVENTARIO.md`), que en su linea 19 declara
*LA TABLA NO SE REGENERA AQUI, A PROPOSITO*. Desde la vuelta 214 la pagina 08
tiene filas 08, 09 y 10, y la fila 10 son esos cuatro puntos.

**LA CIFRA DE 03 FUSIONES idx 0, donde se midio por primera vez:** acta 217,
linea 77344: *71 actos sin fundir de 335 del corte vigente (19 nodos en las SEIS
fusiones que la remision de la fase 03 dejo enrutadas)*.

**LA CIFRA DE 07 ADUANA idx 0, medida en esta sesion y no citada:** la ficha
`OP-A-02` v4 nombra CINCO controles mecanicos. Cotejados contra las 26
comprobaciones de Gate 0 (`docs/loop/SALIDA_V220_GATE0_CMD1_CIERRE.txt`):

| control de OP-A-02 v4 | comprobacion de Gate 0 que lo corre |
|---|---|
| auto-arista con resolucion | `Ningun nodo VIVO se cita a si mismo tras RESOLVER` |
| lista blanca de claves | `Ninguna clave de nodo fuera de la lista blanca del esquema` |
| control posicional del campo fuente | `OP-A-01: todo nodo VIVO con MAS DE UNA fuente pasa la comprobacion posicional` |
| campo fuente canonico | `OP-A-01 / OP-A-02 (A2.4): el campo fuente resuelve contra la lista CANONICA` |
| **revision de nomina por dominio** | **NINGUNA por ese nombre** (la mas cercana, *la nomina adjudicada de la aduana no se movio sin declararse*, no es por dominio) |

**El quinto control es la revision de nomina por dominio.** Y la fila 07 de la
pagina 08 (linea 30) dice CUATRO donde la ficha dice CINCO: es la divergencia que
la cola de siete lleva como entrada 2.

**PENDIENTE DE PREGUNTA AL FUNDADOR (se para aqui, por su orden):** su letra
nombra `05 SANEO idx 1` y `OP-I-01 idx 3` como dos de *las tres*; el lector de las
17 tiene otras dos ademas (`03 FUSIONES idx 0`, `07 ADUANA idx 0`) y `OP-I-01`
tiene ademas su idx 2. Son **cinco** items a medias en dos libros, no tres. Se
pide alcance antes de escribir nada en el plan.

### 1.b LA BATERIA: LA NOMINA Y LOS NUEVE ARNESES, MEDIDOS

`scripts/loop/verificar_mutaciones_viejas.py` trae **154** entradas literales
`vuelta*.py` en su texto (contadas con regex en esta sesion); la nomina corrida
en la 220 fue de **135** exactamente una vez, 270 corridas. Los **siete que no
muerden**, con su tramo, leidos de `docs/loop/SALIDA_V220_T2_BATERIA.txt` lineas
112 a 120:

| tramo | arnes | lineas |
|---:|---|---:|
| 3 | `vuelta160_tarea6b_mutacion_puerta.py` | 303 |
| 5 | `vuelta165_tarea6_mutacion_op_l_01.py` | 174 |
| 5 | `vuelta166_tarea2_mutacion_correccion.py` | 267 |
| 5 | `vuelta168_tarea1_mutacion_nota.py` | 24 |
| 6 | `vuelta168_tarea2_mutacion_reconstructor.py` | 24 |
| 6 | `vuelta171_mutacion_busqueda_acta.py` | 172 |
| 9 | `vuelta185_tarea1c_mutacion_bateria_continuada.py` | 264 |

Los **dos fuera de la nomina** (lineas 122 a 125 de la misma salida):
`vuelta197_tarea2_mutacion_orden_del_turno.py` (423 lineas) y
`vuelta199_tarea1_mutacion_guardas_revividas.py` (442 lineas). Su medicion uno a
uno se anexa en cuanto corran.

### 1.b (continuacion) LOS NUEVE, CORRIDOS UNO A UNO, Y LO QUE SE HIZO CON CADA UNO

**Los dos fuera de la nomina, corridos tal cual en esta sesion:**

| arnes | exitcode | veredicto impreso |
|---|---:|---|
| `vuelta197_tarea2_mutacion_orden_del_turno.py` | 0 | VEREDICTO: VERDE |
| `vuelta199_tarea1_mutacion_guardas_revividas.py` | 0 | VEREDICTO DEL ARNES: VERDE |

Legitimos los dos (cada uno prueba una pieza viva de `apertura_del_auditor.py`
y trae su mutacion), **ENTRAN en la nomina**: `VIEJAS` pasa de 135 a 137,
`arneses_que_faltan()` devuelve vacio e `nomina_invisible_al_censo()` devuelve
vacio, medidos importando el fichero tras el parche.

**Los siete que no muerden, corridos uno a uno ANTES de tocar nada** (los siete
exitcode 1) **y diagnosticados leyendo su codigo y git, no su rotulo.** El rojo
de un arnes de mutacion puede ser dos cosas opuestas: la guarda que no muerde
(el mutante no cae) o el sujeto que se movio (el arnes ya no puede probar lo que
probaba). **Los siete eran sujeto movido**, en tres especies:

| arnes | lo que imprimia | causa medida | reparacion |
|---|---|---|---|
| `vuelta160_tarea6b_mutacion_puerta.py` | `no se hallo el acta 159 en la rama` | busca el asunto en `git log -n 500`; el acta 159 (`13cf21be`) esta a **641** commits de HEAD | se lee la rama entera |
| `vuelta168_tarea1_mutacion_nota.py` | `commits que empiezan por 'ACTA DE LA VUELTA 167': 0` | ventana `-400` en `vuelta168_tarea1_adosar_nota_r36.py`; el acta 167 (`e3152a9c`) esta a **541** | se lee la rama entera |
| `vuelta168_tarea2_mutacion_reconstructor.py` | `... 'ACTA DE LA VUELTA 165': 0` | ventana `-400` en `vuelta168_tarea2_reconstruir_166_167.py`; el acta 165 (`00cfe6e0`) esta a **556** | se lee la rama entera |
| `vuelta171_mutacion_busqueda_acta.py` | `F_y_es_el_commit_d7b18370 FALLA (real='')` | ventana `-400`; `d7b18370` esta a **513** | se lee la rama entera |
| `vuelta165_tarea6_mutacion_op_l_01.py` | `C_tiene_seis_clausulas FALLA (real=7)`, `C_tres... (real=4)`, `C_sigue_en_LISTA (real='HECHA')` | la ficha paso a 7 clausulas y 4 declaradas en la vuelta 203 (`169a2ff6`) y a HECHA en la 209 (`1a3d6d54`), trazado con `git log` sobre `OPERACIONES.jsonl` | tercer re anclaje, con el motivo escrito y los dos anteriores intactos; el caso sigue siendo igualdad exacta |
| `vuelta166_tarea2_mutacion_correccion.py` | `F_mover_el_estado_tumba_el_invariante_4 FALLA (real=True)` | la mutacion escribia `HECHA` sobre una ficha que ya esta en HECHA: no era mutacion | el estado se mueve siempre a un valor distinto del que tiene hoy |
| `vuelta185_tarea1c_mutacion_bateria_continuada.py` | bloque F: los once tramos dan `vuelta 220`, reparto 4 y 5 `NO` | `tramos_por_vuelta(183)` lee el ultimo commit de cada fichero en HEAD y la 220 los volvio a sellar todos | `cerrar_reporte.tramos_por_vuelta` gana `ref=None` (con `None`, conducta identica); el arnes clava el commit del tramo 9 de la 184 leido de git por su asunto (`3500db9d`, exactamente uno) y lee el reparto EN ese commit |

Los cuatro primeros son **una sola caida en cuatro cuerpos**: una ventana
contada sobre git que la propia rama dejo atras. Y las profundidades dicen
cuando empezo a fallar cada uno: el de la 171 al pasar de 400 commits desde
`d7b18370`, mucho antes de la 220.

**Las siete reparaciones, corridas una a una despues del parche:**

| arnes | exitcode | segunda pasada (el esperado mutado cae) |
|---|---:|---|
| `vuelta160_tarea6b_mutacion_puerta.py` | 0 | VERDE: los 4 se comportan |
| `vuelta165_tarea6_mutacion_op_l_01.py` | 0 | 16 pasan, 16 caen al mutar |
| `vuelta166_tarea2_mutacion_correccion.py` | 0 | 20 pasan, 20 caen al mutar |
| `vuelta168_tarea1_mutacion_nota.py` | 0 | 14 pasan, 14 caen al mutar |
| `vuelta168_tarea2_mutacion_reconstructor.py` | 0 | 17 pasan, 17 caen al mutar |
| `vuelta171_mutacion_busqueda_acta.py` | 0 | 16 pasan, 16 caen al mutar |
| `vuelta185_tarea1c_mutacion_bateria_continuada.py` | 0 | reparto 4 y 5 sobre nueve SI; mutados (5 y 4) CAE, (nueve por la 183) CAE; CIFRA fallos: 0 |

**Ninguno se retira.** Los siete se repararon barato y con su mutacion probada
por la segunda pasada de cada arnes. Una caida propia de esta sesion, declarada:
el primer parche de `cerrar_reporte.py` dejo un parentesis sin cerrar
(`SyntaxError` en la linea 389 al importar); se cerro y el arnes 185 se volvio a
correr desde cero. El fichero sellado
`docs/loop/SALIDA_V185_T1C_MUTACION_BATERIA_CONTINUADA.txt` queda con la corrida
reparada (el arnes escribe en esa ruta fija); los sellos de 197 y 199 se
restauraron a HEAD porque sus arneses ya la habian escrito igual en su vuelta.

**Doctrina escrita:** `docs/loop/AUDITOR.md` 6.3 lleva la congelacion en 135
tachada con su correccion declarada (9 sep 2026), y nace **6.4 REGIMEN POST
BUCLE DE LA BATERIA** (nomina abierta que llena el censo, cuando corre, las dos
especies del rojo, reparar barato o retirar con motivo, ninguna ventana contada
sobre git, la salida sellada con el nombre de la sesion). La entrada de la
nomina en `verificar_mutaciones_viejas.py` dice lo mismo en su sitio.

**La bateria entera con la nomina de 137** se corre en el PASO 2.b con su
sello `_integral_`; aqui solo se midieron los nueve uno a uno.

### 1.d LA COLA DE SIETE, LEIDA DEL ACTA 219

Seccion 6, lineas 78024 a 78066, las siete con su numero. Se resuelven o se
remiten con ficha en el apartado correspondiente de esta acta; ninguna queda sin
linea.

### 1.a (continuacion) LA DECISION DE ALCANCE Y LOS CINCO ITEMS, RESUELTOS

**La respuesta del fundador** esta verbatim en
`docs/loop/paradas/2026-09-09-alcance-integral-1a-DECISION.md`: los CINCO
entran, con el criterio de firma, fabricacion barata o remision declarada con
ficha. Las cinco celdas de `docs/plan/08_VERIFICACION.md` llevan el texto viejo
tachado y el nuevo al lado, y el bloque de correccion declarada de la integral
va debajo del de la vuelta 214; la tabla sigue armando **11 filas y 30
clausulas** con el mismo reparto (medido con el mismo partidor del lector, el
punto y coma).

| item | destino | la cifra, corrida en esta sesion |
|---|---|---|
| 1. `03 FUSIONES` idx 0 | REESCRITA a los tres destinos y medida | `scripts/loop/_integral_1a_destino_de_los_actos.py`, salida `docs/loop/SALIDA_integral_1A_DESTINO_ACTOS.txt`: **335 de 335 con destino** (SUPERVIVIENTE 264, DECLARACION SELLADA 42, DISOLUCION MEDIDA 29, SIN DESTINO 0); por estado, ABIERTO 17 y 7 y 31, CERRADO 25 y 22 y 233 |
| 2. `05 SANEO` idx 1 | FIRMADA | adjudicacion 4.5 del acta 219 (`ACTA_AUDITOR.md:77935`) escrita debajo de la tabla, con la decision del 9 sep 2026 citada |
| 3. `07 ADUANA` idx 0 | FABRICADO | `scripts/loop/verificar_nomina_por_dominio.py` cableado a Gate 0 (`run_phase1.py`, comprobacion `OP-A-02 (quinto control)`): 32 racimos, 171 miembros, 0 fuera de su dominio; arnes `vuelta221_integral_mutacion_nomina_por_dominio.py` VERDE (cuatro mutaciones caen, cero escrituras) |
| 4. `OP-I-01` idx 2 | REMITIDA CON FICHA | `docs/PENDIENTES.md`, ficha `relleno-de-huecos-del-inventario`, con la nomina de los cinco huecos que el archivo nombra (cuatro dominios sin cribar y el puente de la mesa unida) |
| 5. `OP-I-01` idx 3 | FABRICADO | `scripts/loop/vista_del_inventario.py` (`--escribir`, `--comprobar`): bloque de 165 lineas al final de `10_INVENTARIO.md`; arnes `vuelta221_integral_mutacion_vista_inventario.py` VERDE (cinco casos caen) |

**Lo que el instrumento del item 1 encontro y como se resolvio, dicho entero.**
Con el grafo y los 81 planes sellados solos, **7 de los 335 quedaban SIN
DESTINO** (`obtencion_compromiso`, `influence_map_organizacional`,
`crowdfunding_legal_exemptions_jobs_act`, `analisis_trafico_competitivo`,
`cultura_climatica_innovacion`, `hr_calidad_gestion`, `fit_problema_solucion`).
Se buscaron uno a uno en el expediente y **los siete tienen su declaracion
sellada en los registros de cierre de `docs/plan/03_FUSIONES.md`, no en un plan
JSON**: colision de clase medida (lineas 909 y 913), pregunta de politica de
catalogo congelada en una B (1431), conteos de contenido que chocan (1663),
pregunta de politica que pide mesa (1927) y los dos actos con dueño FUERA de la
fase, el 31 y el 37 del `orden_universo` (9272). El instrumento gano una cuarta
fuente, la pagina, y con ella 335 de 335. **Un matiz que se dice:** cinco de
esos siete se declararon *se acumula para LA MESA* y `docs/plan/06_MESAS.md`
no los nombra (medido con grep: cero lineas); su destino es la declaracion con
motivo, reabrible solo por la cola ordinaria post campaña (decision 2 del cierre
de la fase 03, `03_FUSIONES.md:9284`). No se paro porque ninguno carece de los
tres destinos; si el fundador lee esos cinco como trabajo real, son cinco actos
de dos y tres miembros con su linea citada.

**El quinto control, medido antes de fabricarlo:** el censo trae etiquetas de
dominio en vocabulario libre (`NUCLEO`, `environmental + nucleo`, `nucleo (3) +
quality (1)`) y 41 miembros deprecados. Leyendo `NUCLEO` como `core`, `a + b`
como declaracion transversal (que es lo que `04_ENLACES.md:1045` ya reconoce) y
resolviendo por alias, quedan **0 fuera de su dominio**; sin normalizar salian
66. No exigio decision de contenido.

**Una caida propia, cazada por el arnes y declarada:** la primera version de la
vista clasificaba CERRADO y ABIERTO por la palabra que aparecia, y un estado
corregido que dice *CERRADO (...). El texto viejo: ABIERTO* salia ABIERTO; el
caso B del arnes no cayo, se reparo (gana la primera palabra) y la vista dice
281 CERRADOS y 54 ABIERTOS, que es lo que el instrumento del item 1 tambien
cuenta.

### 1.c LAS 71 FICHAS, RECONCILIADAS UNA VEZ COMO ACTO DE ARCHIVO

**La vara antes de tocar nada** (`vuelta150_3_relectura_expediente.py --corte
f5689f9a`, sellada en `docs/loop/SALIDA_integral_1C_VARA.txt`): 71 fichas, 31
calzan, 40 no calzan (24 congeladas declaradas, 12 en silencio, **4 HECHA sin
ninguna prueba**: `OP-V-01`, `OP-L-01`, `OP-L-02`, `OP-L-03`; 3 LISTA sin
prueba, de las que 2 CONSUMIDAS y 1 trabajo real, `OP-I-01`, resuelto en 1.a).
Las rutas de prueba de las 71 se computaron con las funciones de la propia
vara (P1 grafo, P2 codigo, P3a git con reloj en el corte, P3b caso positivo, P4
documental).

**El acto de archivo, aplicado a `docs/plan/OPERACIONES.jsonl` con
`scratchpad/parche_1c_archivo.py`** (71 lineas reescritas con el serializador
que reproduce byte a byte las 71 originales, medido antes):

| estado nuevo | fichas | de donde venian |
|---|---:|---|
| **HECHA** | 66 | 32 ya HECHA (28 con prueba de grafo, codigo o git; 4 con prueba documental) y 34 LISTA con prueba (congeladas por el registro HECHA no se estrena) |
| **CONSUMIDA** | 5 | `OP-M-02-MEDIOS`, `OP-M-02-ASSESS`, `OP-M-02-ADMIT`, `OP-M-02-ACTIVATE`, `OP-M-02-ACCOMPLISH`: sus nodos resuelven por P.1 al vivo, consumidas por `OP-U-01` (`docs/loop/SALIDA_V64_CONSUMIDAS.txt`) |
| **REMITIDA** | 0 | ninguna ficha entera; la unica remision es la clausula idx 2 de `OP-I-01`, que va en su ficha |

Cada nota lleva *ARCHIVO DE CAMPAÑA (...) de X a Y. PRUEBA: ruta*. **Las cuatro
que afirmaban mas que el repo** llevan el tachado con su motivo: `~~HECHA sin
ninguna prueba de grafo, codigo ni git~~ HECHA con prueba DOCUMENTAL`, con la
ruta y los bytes del documento (`docs/AUDITORIA_MOTOR.md` y
`scripts/rumbos/prueba_rumbos.py`; `docs/plan/LECTURAS_DIRIGIDAS.md`;
`docs/plan/LD_SALES_ROADMAP.md`; `docs/plan/OP_L_03_LECTURAS.jsonl` y
`OP_L_03_TRIANGULOS.jsonl`), y el motivo: una mesa de lecturas produce
documentos y no huella en el grafo.

### 1.d LA COLA DE SIETE, CADA UNA CON SU LINEA

| entrada (acta 219, seccion 6) | destino |
|---|---|
| 1. familia `C.1` en nueve, con tres opciones | **RESUELTA POR DECLARACION** en `docs/loop/AUDITOR.md` (correccion declarada bajo el orden de apertura): la familia se cierra con el bucle, sin turnos no hay orden que romper; ninguna de las tres opciones se elige porque su sujeto ya no existe; la letra queda como historia |
| 2. dos divergencias de la pagina 08 (lineas 28 y 30) | **RESUELTAS** en 1.a: la 28 lleva la firma y la 30 pasa de cuatro a cinco por tachado |
| 3. `--siguiente` del lanzador no distingue la vuelta | **REPARADA BARATO**: `vuelta183_bateria_por_tramos.py` gana `--rotulo <texto>` (las tres salidas y `--siguiente` llevan el rotulo); medido: `--siguiente --rotulo integral` dice 11 tramos que faltan, y sin rotulo sigue diciendo 0 sobre las de la 183 |
| 4. `vuelta150_4_tabla_por_fase.py` en rojo por once filas | **REPARADA BARATO**: la vara mide las ocho filas de 0 CODIGO a 07 ADUANA y dice cuales quedan fuera; corrida con `--corte f5689f9a`: exitcode 0, 8 filas, 0 en NO CUMPLE |
| 5. la ciega no acierta lo que se decide por barrido de familia | **REMITIDA CON FICHA**: `docs/PENDIENTES.md`, `ciega-por-familia`, con la cifra del acta (nueve de catorce fallos) y su condicion de cierre |
| 6. las dos clausulas que quedaban | **RESUELTAS** en 1.a (items 1 y 3) |
| 7. el remedio de dictado de la `C.4` | **ESCRITO** en `docs/loop/EJECUTOR.md`, junto a la regla de la ruta que promete prueba, en las palabras del propio ejecutor: la pareja de bytes es una regla de cifras, venga de una ruta o de un campo |
