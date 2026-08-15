# REPORTE DE LA VUELTA 29 (ejecutor Opus 5). FASE III, EJECUCION. Rama `pasada-unica`

**El muro cayo y la fase 01 avanzo casi entera: `OP-F-02` cerrada, `OP-F-03` cerrada,
`OP-F-04-WEI` y `OP-F-04-HOR` ejecutadas en casi todo, TRECE nodos propios nacidos y
declarados. Y PARADA por TRES bloques de TOQUE UNICO cuyo texto no alcanza para
ejecutarse sin decidir. `OP-F-04-COL` no se ejecuto, y el motivo se mide aqui.**

---

## 0. CABECERA, con su medicion

| | |
|---|---|
| **HEAD de partida** | `dc8ef3a2` (la decision del fundador: paridad de censo, cuarto comando, estado al cierre) |
| **HEAD al escribir esto** | el commit de este reporte, sobre `2bd8dd76` |
| **commits de trabajo** | **SEIS**, todos empujados a `origin/pasada-unica` |
| **rutas tocadas** (`git diff --name-only dc8ef3a2..HEAD`) | `docs/loop/` **68**, `dataset/nodos/` **55**, `scripts/loop/` **7**, `web/lib/` **3**, `docs/plan/` **3**, `engine/node_families.json` **1**, `dataset/metadata/` **1** |
| **`dataset/nodos/`** | **55 ficheros, 510 insertadas, 236 borradas**; **13 ficheros NUEVOS** (`git diff --name-status`, contados hoy) |
| **salidas de instrumento** | **63 ficheros `SALIDA_V29_*`** |
| **cortes ejecutados** | **TREINTA**: 3 de `OP-F-02`, 1 de la relectura, 5 de `OP-F-03`, 8 de `OP-F-04-WEI`, 13 de `OP-F-04-HOR` |

**LOS SEIS COMMITS:**

| hash | que |
|---|---|
| `f4ad6d45` | TAREA 1: las cinco costuras de WEI a la cola, medidas |
| `2d96e3d3` | `OP-F-02` entera: los tres nodo propio de Mollick |
| `7521f039` | la correccion 1 de la relectura conjunta: el nodo de economia circular |
| `9d4a8eb1` | `OP-F-03` CERRADA: los cinco bloques con destino nodo propio |
| `1eef1c6b` | `OP-F-04-WEI` segunda tanda: ocho cortes, el anillo interior |
| `2bd8dd76` | `OP-F-04-HOR`: doce nodos en trece cortes |

---

## 1. TAREA 1: LOS REGISTROS

### 1.1 Las costuras de `OP-F-04-WEI`, declaradas: son CINCO, no tres

**Instrumento propio corrido en esta vuelta:** `scripts/loop/vuelta29_costuras.py`, salida con
los pasos impresos uno a uno en `docs/loop/SALIDA_V29_COSTURAS.txt`. Los pasos de HOY salen
del arbol; **los de ANTES del reparto salen del commit `4e6349ea`**, el ultimo anterior a
`f69f4819`, que es el que ejecuto los cinco cortes de la vuelta 28. Todas en la MISMA tabla de
`docs/plan/08_VERIFICACION.md`, seccion `LA COLA DE RELECTURA POST FUSION`, con el formato de
la primera costura. **La fila de la vuelta 28 se quedo entera.**

| miembro | medido hoy | veredicto |
|---|---|---|
| `fases_traccion_producto` | **7 pasos contra 4** | los tres que entraron repiten sus pasos 1, 2 y 4 |
| `clasificacion_leads_abc` | **10 contra 5** | tres de los cinco repiten (categorias, 66 a 75 por ciento, pase de los C) |
| `bullseye_framework` | **11 contra 6** | cuatro de los cinco repiten (los 19 canales, la prueba barata, medir, comparar) |
| `publicidad_offline_pruebas_locales` | **9 contra 5** | **SOLAPE PARCIAL, uno de cuatro.** El acta lo sospechaba y la cifra lo confirma |
| `compromiso_linea_tiempo_cliente` | **6 contra 5** | **QUINTA costura, que el acta no nombro.** El unico paso que entro repite sus pasos 2 y 3 |

**LO QUE EL INSTRUMENTO LEVANTO Y EL ENCARGO NO PEDIA, declarado y no arreglado:** la quinta
costura. El acta nombro tres y mando revisar una cuarta; **medi los CINCO receptores del
reparto y este tambien repite.** La regla de esa puerta es mecanica (*una repeticion que un
reparto de la fase 01 crea dentro de un miembro entra a la nomina de la fase 02*), y el propio
acta de la vuelta 28 ya habia leido esa repeticion al sostener el destino en su discutible 9.
**Callarla porque el encargo no la nombraba habria sido la misma omision que esta correccion
viene a reparar.**

### 1.2 Las tres correcciones del commit del fundador, citadas con su linea (no reescritas)

**Leidas hoy contra los ficheros, no recordadas:**

| correccion | donde vive | linea leida hoy |
|---|---|---|
| **paridad de censo contra `total_nodos`** | `web/lib/engine/graph.test.ts` | **linea 15**: *carga TODOS los nodos reales, paridad contra total_nodos (decision del fundador, 14 ago 2026)*. Su registro con el caso positivo en las dos direcciones esta en `docs/plan/08_VERIFICACION.md` **linea 250** |
| **el cuarto comando condicional del ciclo** | `docs/plan/08_VERIFICACION.md` | **linea 55** (la fila del comando 4: `python engine/plan_readiness.py`, *corrido DESPUES del 2 y ANTES del 3, SOLO cuando la operacion cambia el CENSO*) y su registro completo en **linea 99** |
| **`EL ESTADO AL CIERRE SE MIDE AL CIERRE`** | `docs/loop/EJECUTOR.md` | **linea 15** |

**LA PRIMERA TIENE SU PRIMER EJEMPLAR EN EL HISTORIAL EN ESTA VUELTA:** el censo se movio de
**3.835 a 3.848** en cinco operaciones, y `graph.test.ts` **quedo verde las cinco veces sin
tocarse una sola linea**. La regla que el fundador escribio hizo exactamente lo que decia.

---

## 2. TAREA 2: LOS PLANES SELLADOS QUE EL MURO TENIA PRESOS

### 2.1 `OP-F-02` EJECUTADA ENTERA

Aplicada desde `docs/loop/PLAN_V27_OPF02.json` **sin reescribir una linea del sello de la
vuelta 27**.

| origen | pasos | nodo propio nuevo |
|---|---|---|
| `future_scenarios_planning` | **13 a 5**, con destejido declarado de 8 a 6 y su mapa | `escenarios_de_evolucion_de_la_ia` |
| `gut_check` | **9 a 4** | `critica_del_plan_con_ia` |
| `brainstorming_divergente` | **8 a 4** | `ideacion_con_ia_en_la_sesion` |

**Caso positivo: 6 CAEN antes, 6 PASAN despues.**

### 2.2 La correccion 1 de la relectura conjunta, APLICADA

`estrategia_circular_y_mecanismo_de_retorno` nace de `modelo_simulacion_cadena_suministro_circular`
(**9 pasos a 5**), con `economia_circular_como_modelo_de_negocio` como procedencia y previo.
**Caso positivo: 2 de 3 CAEN antes, 3 de 3 PASAN despues.**

> **REBANADA DECLARADA, y hace falta decirlo:** el plan sellado trae DOS mudanzas y la segunda
> (`diferencia_ventaja_beneficio` a `framework_caracteristicas_ventajas_beneficios`) **ya estaba
> en el arbol desde la vuelta 28**. Su guarda de conteo paro en rojo, **como debe**. Se ejecuto
> `docs/loop/PLAN_V29_RELECTURA_D1.json`, la rebanada con la mudanza pendiente, **copiada del
> sello POR INSTRUMENTO y verificada identica al dict original** (`LA MUDANZA ES IDENTICA AL
> SELLO: True`): no se reescribio una sola linea de lo sellado.

### 2.3 CORRECCION DECLARADA: la cita del encargo sobre `OP-F-03` no calza con lo medido

**El encargo dice:** *los cinco bloques nodo propio de `OP-F-03` (`PLAN_V27_OPF03_SISTEMAS.json`
y lo que falte de `PLAN_V27_OPF03_CADENA.json`)*. **Medido hoy con instrumento propio**
(`scripts/loop/vuelta29_estado_planes.py`, salida en `docs/loop/SALIDA_V29_ESTADO_PLANES.txt`):

| plan | cortes | con destino nodo propio | pendientes |
|---|---:|---:|---:|
| `PLAN_V27_OPF03_SISTEMAS.json` | 7 | **0** | **0** |
| `PLAN_V27_OPF03_CADENA.json` | 9 | **0** | **0** |

**Los dos planes estan APLICADOS ENTEROS desde la vuelta 27, y ninguno de sus dieciseis cortes
tiene destino nodo propio.** La discrepancia **se declara en vez de resolverse copiando**
(regla 2 del ejecutor), y **se ejecuto sobre lo que el registro SI dice**: los cinco bloques
estan nombrados en `docs/plan/01_FUENTES.md`, en la tabla `LOS CUATRO QUE NO SE PUDIERON
EJECUTAR` (vuelta 27) mas el de la relectura (vuelta 28). **La cifra CINCO del encargo es
correcta; lo que no calza son los dos ficheros citados.**

### 2.4 `OP-F-03` CERRADA: los cinco bloques ejecutados

| origen | frontera | destino |
|---|---|---|
| `economia_circular_...` (via `modelo_simulacion_...`) | 6 a 9 | nodo propio `estrategia_circular_y_mecanismo_de_retorno` |
| `analisis_tco_roi_b2b` | 5 a 9 | nodo propio `seleccion_de_proveedores_por_costo_total` |
| `criterios_seleccion_proveedores` | 7 a 10 | **EL MISMO nodo** (adjudicacion 3 del acta 27) |
| `gestion_inventario` | 6 a 9 | nodo propio `driver_de_inventario` |
| `transicion_producto_a_experiencia` | **5 a 8 y 9 a 12** | nodo propio `producto_como_servicio_de_acceso`, **los dos a UNO** |

**La cuenta que la vuelta 28 dejo escrita (*catorce de diecinueve bloques en el arbol, cinco
pendientes*) queda en DIECINUEVE de diecinueve. Caso positivo: 10 CAEN antes, 15 PASAN
despues.**

**LO QUE ESTA VUELTA ANADIO A LA LECTURA PUBLICADA, dicho sin adornos:** el **cuerpo** de los
tres nodos propios (titulo, resumen, entregable, condiciones, etiqueta) y **el `node_id` de
uno de ellos**: la tabla de la vuelta 27 publicaba `seleccion_de_proveedores_por_costo_total` y
`driver_de_inventario` con su id escrito, **pero la de `transicion_producto_a_experiencia`
decia solo *nodo propio*, sin nombre.** `producto_como_servicio_de_acceso` es un nombre de esta
vuelta, **y va marcado como discutible 1**.

### 2.5 AMPLIACION DECLARADA DEL INSTRUMENTO

`scripts/loop/vuelta27_cortar.py`: el destino de tipo `miembro` vale ahora **si existe en disco
O si este mismo plan acaba de crearlo como nodo propio en un corte anterior**. **Sin eso, la
adjudicacion 3 del acta 27 no se podia ejecutar**: el segundo corte chocaba con la guarda de
*ya existe*, y la unica salida habria sido **fabricar el par que la campana existe para
deshacer**. **Ninguna guarda se ablanda:** si el destino no esta ni en disco ni en memoria,
sigue siendo rojo. Se uso en tres sitios (`seleccion_de_proveedores_por_costo_total`,
`producto_como_servicio_de_acceso`, `anillo_interior_explotar_el_canal_nucleo`,
`formalizar_un_proceso_ad_hoc`).

---

## 3. TAREA 3: `OP-F-04`

### 3.1 `OP-F-04-WEI`, segunda tanda: ocho cortes sobre siete nodos

**Nomina de la familia MEDIDA HOY, no copiada: 76 nodos vivos declaran `Traction` y 67 con
fuente UNICA** (`SALIDA_V29_FAMILIA_WEINBERG.txt`). **Coincide con la medicion de CIERRE del
auditor en el acta 28 y NO con la de apertura (80 y 67), que es la caida de reporte que esa
acta nombro.** Las fronteras son las publicadas en la vuelta 28: **no se rehicieron.**

| origen | frontera | destino por `P.18` |
|---|---|---|
| `enfoque_motor_unico_crecimiento` | 5 a 9 | **nodo propio** `anillo_interior_explotar_el_canal_nucleo` |
| `optimizacion_embudo_get_customers` | 6 a 10 | **el mismo** |
| `ab_testing_optimizacion` | 11 a 15 | **el mismo** |
| `analisis_trafico_competitivo` | 5 a 8 | **nodo propio** `inteligencia_de_anuncios_de_la_competencia` |
| `decision_pivote_perseverar` | 5 a 9 | **nodo propio** `puntos_brillantes_antes_del_pivote` |
| `key_partners_hypothesis` | **6 a 10** | miembro `alineacion_bd_metricas_core` |
| `key_partners_hypothesis` | **11 a 14** | miembro `pipeline_alianzas_bd` |
| `metricas_de_adquisicion_activacion` | 6 a 9 | miembro `sem_estrategia_ejecucion` |

> **LA AUSENCIA QUE DECIDE LOS TRES PRIMEROS, medida sobre los 76: LA DIANA NO TIENE ANILLO
> INTERIOR.** `canales_de_traccion_19` es el exterior, `middle_ring_testing` el medio,
> `bullseye_framework` la diana entera, **y ningun miembro dice que se hace con el canal
> DESPUES de que gana.** Los tres bloques son ese mismo acto. Fundidos en UNO por la
> adjudicacion 3.

**`key_partners_hypothesis` da DOS cortes**, resolviendo lo que el acta 28 dejo SOSTENIDO en su
discutible 11: **leidos hoy, los dos sub bloques se distinguen.** El de 6 a 10 filtra alianzas
**por la metrica**; el de 11 a 14 **clasifica por TIPO** segun el cuello de botella.

**LA GUARDA DE HUELLA PARO CINCO VECES** y obligo a cambiar el trozo elegido: `MixRank` ya
vivia en `retargeting_display`, `Critical Path` **en el propio destino**
`alineacion_bd_metricas_core`, `valores at` en `medidas_tendencia_dispersion`, `cuello de
botella` en dos nodos mas y `joint venture` en cuatro. **Una huella que ya vive fuera del
origen no prueba nada, y la guarda lo cazo antes de sellar.** *(El caso de `Critical Path` es
evidencia a favor del destino, no en contra.)*

**Caso positivo: 16 CAEN de 24 antes, 24 de 24 PASAN despues.**

### 3.2 `OP-F-04-HOR`: doce nodos en trece cortes, DESBLOQUEADA POR CITA

**La cita, leida hoy:** acta de la vuelta 28, **adjudicacion 3**, que cito el REGISTRO del
fundador en la nota de `OP-F-04-HOR` de `OPERACIONES.jsonl`. *Familia propia* es **la familia
del propio libro**, en paralelo exacto con *se reune con SPIN*, *con el Bullseye* y *con los
100 dias*. **HOR se ejecuta como WEI.** El parrafo de la vuelta 28 que preveia el choque con el
muro **se quedo entero**: era la lectura de ese dia.

**Nomina MEDIDA HOY: 102 vivos declaran el trozo `Hard Thing`, 88 con fuente UNICA.** Las
fronteras son las publicadas en la vuelta 20: **no se rehicieron.**

| origen | frontera | destino por `P.18` |
|---|---|---|
| `actualizacion_posiciones_existentes` | 5 a 19 | miembro `evaluacion_balanceada_de_ejecutivos` |
| `background_startup_vs_corporativo` | 5 a 9 | miembro `contratar_ambicion_correcta` |
| `contratacion_experiencia_vs_potencial` | 5 a 10 | miembro `contratar_por_fortaleza` |
| `decision_de_salir_a_bolsa` | 6 a 10 | **nodo propio** `estar_listo_para_ser_publica` |
| `estrategia_de_innovacion_producto` | 4 a 7 | miembro `coraje_en_decisiones_dificiles` |
| `manejo_empleados_en_adquisicion` | 5 a 9 | miembro `comunicacion_honesta_en_crisis_al_equipo` |
| `metas_vs_proposito` | 5 a 9 | miembro `diseno_metricas_lideres_rezagados` |
| `organizacion_adaptativa` | 5 a 8 | miembro `contratacion_acelerada_hipercrecimiento` |
| `plan_mejora_procesos` | **6 a 10 y 11 a 15** | **nodo propio** `formalizar_un_proceso_ad_hoc`, **los dos a UNO** |
| `posicionamiento_de_empresa` | 6 a 9 | **nodo propio** `la_historia_de_la_empresa` |
| `revisiones_regulares_desempeno_ceo` | 5 a 10 | miembro `framework_excelencia_operacional` |
| `seleccion_ceo_fundador` | 5 a 12 | miembro `planificacion_sucesion_ceo` |

> **`plan_mejora_procesos` ES EL SEGUNDO EJEMPLAR MEDIDO DE LA AVERIA DE `OP-S-11`:** declara a
> Horowitz **dos veces con dos grafias** (*Hard Things* y *Hard Thing*), y sus dos bloques dicen
> lo mismo **cuatro veces de cinco**. Van a UN nodo por la adjudicacion 3.

**Caso positivo: 26 CAEN de 39 antes, 39 de 39 PASAN despues.**

### 3.3 `OP-F-04-COL` NO SE EJECUTO, y el motivo se mide

| | medido hoy |
|---|---|
| nomina | **15 nodos, los 15 vivos** |
| familia de destino | **83 vivos declaran a Coleman, 68 con fuente UNICA** |
| **fronteras publicadas** | **2 de 15**, barrido corrido hoy (`SALIDA_V29_FRONTERAS_COL.txt`): solo `voz_del_cliente_voc` y `metas_vs_proposito`. **Los otros trece no aparecen con frontera en ninguna linea de `01_FUENTES.md`** |

**Esa es la diferencia entera con `WEI` y con `HOR`:** en las dos, las fronteras estaban
publicadas y esta vuelta solo tuvo que anadir el destino. **En `COL` habria que leer TRECE
fronteras nuevas ademas de quince destinos**, que es exactamente el motivo que las vueltas 27 y
28 dieron para no tocarla (*lectura y no mecanica*). **Leer trece fronteras al final de una
vuelta que ya ejecuto treinta cortes seria adivinar, y la regla 11 lo prohibe.**

**Y hay una segunda razon, de dependencia y no de alcance:** `viral_loop_marketing` esta
**DENTRO de los 15 de COL**, y es uno de los tres bloques de la PARADA. **`OP-F-04-COL` no se
puede declarar ENTERA mientras ese nodo espere adjudicacion, ejecute quien ejecute el resto.**

### 3.4 LA FASE 01 NO CIERRA, y por eso no se paso a las fases siguientes

El punto 4 del encargo (seguir en modo continuo a las fases siguientes del `00_INDICE`) tiene
como condicion escrita *con las cuatro `OP-F-04` hechas*. **Hoy son dos hechas (`RAC`, y `HOR`
salvo un nodo), una parcial (`WEI`, por dos) y una sin ejecutar (`COL`).** No se avanzo a la
fase 02.

---

## 4. PARADA: TRES BLOQUES DE TOQUE UNICO CUYO TEXTO NO ALCANZA

**El encargo lo dice con esas palabras: *cualquier operacion cuyo texto no alcance para
ejecutarse sin decidir, te detiene a ti y convoca al auditor*. Son estos tres, los tres
declarados en `01_FUENTES.md` como `LOS TRES CASOS QUE NO SON UN SIMPLE APENDICE`, los tres
con TOQUE UNICO. Leidos hoy paso por paso, y NO ejecutados.**

### 4.1 `coeficiente_viral` (16 pasos, `OP-F-04-WEI`)

**Lo leido hoy:** 1 a 5 son de Blank (contar usuarios y referidos, calcular el coeficiente,
testear incentivos, monitorear). **6 a 11 y 12 a 16 son el bloque de Weinberg DOS VECES**: los
dos miden invitaciones por usuario, conversion y K; el primero anade el tiempo de ciclo viral y
como reducirlo.

**LO QUE NO ALCANZA:** el destino esta declarado **PENDIENTE de leer la nomina** en la tabla de
la vuelta 28, y leida hoy la nomina, **el unico nodo del catalogo cuyo objeto es descomponer K
en sus variables es el propio donante**, que **SALE de la familia** al quedarse con Blank como
fuente unica. Los vecinos no coinciden: `tiempo_ciclo_viral` tiene por objeto el TIEMPO del
ciclo (solo dos pasos del bloque), `identificacion_bolsas_virales` mide K **por segmento**, y
`seeding_canal_viral` es el seeding.

> **Y AQUI ESTA LA CONTRADICCION QUE ME DETIENE, y por eso no elijo:** si el bloque va a **nodo
> propio**, la campana **fabrica un nodo que es gemelo evidente de su propio donante el dia de
> su creacion**, que es literalmente lo que la ratio de la adjudicacion 3 del acta 27 prohibe
> (*fabricar el par que la campana existe para deshacer*). Si va a un **miembro**, se fuerza un
> encaje que la lectura no sostiene, que es lo que `P.18` punto 3 prohibe. **Las dos salidas
> chocan con una regla vigente, asi que no es una lectura dificil: es una decision que no me
> toca.**

### 4.2 `viral_loop_marketing` (30 pasos, TRES libros, en `OP-F-04-WEI` **y** en `OP-F-04-COL`)

**Lo leido hoy:** no son dos bloques sino **seis tramos** de tres libros entrelazados: 1 a 3
(Blank, mecanismo de referidos), 4 a 8 (momento e incentivo del referido), 9 a 13 (identificar
promotores espontaneos, agradecer, reconocimiento VIP), 14 a 17 (programa de referidos,
embajadores, contenido compartible), 18 a 21 (senales de promotor, herramientas, reconocimiento,
progresion Adopt a Advocate), 22 a 25 (que valoran mas alla del dinero, segmentar, oferta
escasa), 26 a 30 (tipos de viralidad, mecanismos de invitacion, simplificar el registro).

**LO QUE NO ALCANZA, y son tres cosas a la vez:**

1. **La frontera NO esta publicada.** Lo unico escrito es que *los pasos 14 a 17 y 18 a 21
   dicen lo mismo con otras palabras*, que es una nota sobre una repeticion, **no un corte
   entre tres libros.**
2. **El nodo pertenece a DOS operaciones** (`OP-F-04-COL` y `OP-F-04-WEI`, verificado hoy en el
   campo `nodos` de las dos), y ninguna pagina dice cual corta primero ni como se reparte entre
   las dos.
3. **La repeticion cruza libros**: los tramos que se repiten son de Coleman, y el TOQUE UNICO
   manda destejer en el mismo acto, **pero destejer entre bloques de autores distintos no es lo
   que ese verbo describe en ninguna pagina.**

### 4.3 `decision_de_vender_startup` (34 pasos, `OP-F-04-HOR`)

**Frontera publicada: 1 a 10 / 11 a 34.** Declara a Horowitz **dos veces con dos grafias** y su
material esta repetido **TRES veces** (11 a 15, 16 a 20, 21 a 25), como esa misma pagina dice.

**LO QUE NO ALCANZA:** el TOQUE UNICO manda separar y destejer en el mismo acto, **y con 24
pasos y tres repeticiones el destejido no es mecanico**: hay que decidir cual de las tres
versiones sobrevive y que se hace con los pasos 26 a 34, que **ninguna pagina describe**. **La
adjudicacion 3 cubre dos bloques que caen en el mismo destino; no cubre tres versiones del
mismo material dentro de un solo bloque.**

> **NO ESCRIBO `docs/loop/PARA_ALEXIS.md`**, por el precedente triple que el acta 28 ratifico en
> su adjudicacion 8 (actas 26, 27 y 28): **esa pluma es del auditor.**

---

## 5. EL ESTADO AL CIERRE, RECOMPUTADO AL CIERRE

**Regla 1, segundo renglon, aplicada al pie: toda cifra de esta seccion se remidio DESPUES del
ultimo corte, no al abrir la vuelta.** Instrumento: `scripts/loop/vuelta26_estado.py` y
`scripts/loop/vuelta27_medir.py familia`, corridos hoy sobre `2bd8dd76`. Salidas en
`SALIDA_V29_ESTADO_FINAL.txt` y `SALIDA_V29_FAMILIAS_CIERRE.txt`.

### 5.1 El marcador: NO SE MOVIO, y era lo esperado

**n 3.388; A 583 (17,2), B 89 (2,6), C 7 (0,2), D 2.709 (80,0); puestos 1 a 3.388; cero huecos,
cero duplicados, cero clases fuera de ABCD.** **Esta vuelta no leyo un solo par**, asi que el
marcador y la tasa por dominio (diez filas, recomputadas) **quedan identicos a los del acta 28**.
**Vara por tramo: NO APLICA**, no hubo cribado.

### 5.2 El grafo, y el censo que se movio

| | apertura (acta 28) | **cierre, medido hoy** |
|---|---:|---:|
| nodos en disco | 3.835 | **3.848** |
| vivos | 3.521 | **3.534** |
| deprecados | 314 | **314** |
| enlaces | 16.800 | **16.832** |
| claves distintas | 15 | **15** |

**Trece nodos nuevos, cero deprecados: el censo subio en exactamente los trece que se crearon.**

### 5.3 Las familias AL DIA, medidas al cierre, con la resta de donantes declarada

**Esta es la tabla que la vuelta 28 publico con la medicion de apertura, y por eso lleva aqui
su aritmetica al lado:**

| familia | apertura de esta vuelta | **cierre, medido hoy** | la aritmetica |
|---|---|---|---|
| **Weinberg** (`Traction`) | 76 vivos, 67 unica | **72 vivos, 70 unica** | **menos 7 donantes** que perdieron su segunda fuente y salieron de la familia, **mas 3 nodos nuevos**: 76 menos 7 mas 3 igual 72. Unica: 67 mas 3 igual 70 |
| **Horowitz** (`Hard Thing`) | 102 vivos, 88 unica | **93 vivos, 91 unica** | **menos 12 donantes, mas 3 nuevos**: 102 menos 12 mas 3 igual 93. Unica: 88 mas 3 igual 91 |
| **Hugos** | 111 vivos, 107 unica | **111 vivos, 111 unica** | **menos 4 donantes, mas 4 nuevos**: 111 menos 4 mas 4 igual 111. **Unica sube a 111 porque los 4 que salieron eran MULTIFUENTE y los 4 que entraron tienen fuente unica** |
| **Coleman** | 83 vivos, 68 unica | **83 vivos, 68 unica** | **sin mover**: `COL` no se ejecuto, y `metas_vs_proposito` sigue MULTI tras perder a Horowitz |
| **Rackham** | 47 vivos, 47 unica | **47 vivos, 47 unica** | **sin mover** |

### 5.4 Inventario, operaciones e indice rojo

- **Inventario: 672 entradas** (dominio 10, acto 556, racimo 13, familia_de_ids 54, figura 20,
  defecto 19). **Sin mover**: esta vuelta no anadio entradas.
- **Operaciones: 71, 71 ids unicos, cero dependencias rotas, las 71 en LISTA.**
- **`docs/plan/INDICE_ROJO_DECLARADO.jsonl`: de 3 lineas a 13**, contadas hoy. **Los trece ids
  nuevos estan declarados uno a uno con su operacion y su fecha**, y las sedes los imprimen:
  **0 activos sin vector, 13 en ROJO DECLARADO.**

### 5.5 Las guardas, corridas enteras tras CADA una de las cinco operaciones

| guarda | resultado |
|---|---|
| **ciclo de `GATE 0`, los CUATRO comandos** (1, 2, **4**, 3) | **exit 0 y `GATE 0: OK` las cinco veces.** El cuarto corrio siempre porque **las cinco cambian el censo** |
| **comando 2, etiquetas** | **71 etiquetas, cero ya en forma final, las cinco veces. CERO ENCOGIMIENTO** |
| **comando 4, `plan_readiness.py`** | `node_families.json` regenerado: 3838, 3839, 3842, 3845, **3848** |
| **comando 3, las dos copias** | **byte identicas a HEAD por las dos rutas**, blob **`e1a584c6`** al cierre (medido con `git hash-object` contra `git rev-parse HEAD:<ruta>` **despues** de commitear, que es la vara escrita) |
| **suite del motor** | **24 de 24, exit 0**, las cinco veces |
| **suite web** | **80 ficheros, 1.030 pasadas y 3 saltadas, exit 0**, las cinco veces |
| **`tsc --noEmit`** | **cero lineas, exit 0**, las cinco veces |
| **simulacion previa** | verde en las cinco, sobre copia en memoria, cero escrituras |
| **guarda de huella** | **paro 5 veces en WEI** y obligo a cambiar el trozo |
| **guarda de conteo** | **paro 1 vez** (la mudanza ya aplicada del plan sellado de la vuelta 28) |
| **el guardian de commit** | corrio en los **seis** commits: *verde. Commit permitido.* |

---

## 6. PENDIENTES DE DOCTRINA (regla 5: no paro por esto, lo registro y sigo)

1. **El paso bien copiado que quedo en el nodo equivocado no tiene puerta.** Los pasos 7 y 8 de
   `producto_como_servicio_de_acceso` (las tres interfaces de usuario, que `01_FUENTES.md` ya
   senalaba en la vuelta 27 como material de SISTEMAS; y la mirada de economia circular) **no
   repiten nada y tampoco son del objeto del nodo**. La cola de relectura tiene disparador para
   **la repeticion**, y no lo tiene para esto. **No se destejio: el verbo de la operacion que
   los movio es repartir.**
2. **La costura dentro de un nodo RECIEN CREADO.** El registro dice *una repeticion que un
   reparto crea dentro de un MIEMBRO*. Dos de las costuras nuevas
   (`producto_como_servicio_de_acceso`, `anillo_interior_explotar_el_canal_nucleo`) caen dentro
   de nodos que la propia operacion acaba de crear. **La extension me parece natural (el
   disparador es la repeticion, no el domicilio) y por eso las declare, pero es extension y va
   marcada.**

---

## 7. CORRECCIONES DECLARADAS DE ESTA VUELTA

1. **La cita del encargo sobre los planes de `OP-F-03`** (seccion 2.3). Los dos ficheros
   citados estan aplicados enteros y tienen cero destinos nodo propio; los cinco bloques viven
   en `01_FUENTES.md`. **La cifra cinco es correcta.**
2. **Las familias al cierre, con la resta de donantes** (seccion 5.3). **Es la leccion de la
   caida de reporte que el acta 28 me puso con nombre**, aplicada por adelantado a mi propia
   tanda: la medicion de apertura de una familia **deja de ser el estado al dia en cuanto el
   reparto le quita donantes.**
3. **`OP-F-04-WEI` pasa de nueve bloques pendientes a DOS**, y sigue PARCIAL.
4. **La ampliacion del instrumento** (seccion 2.5), declarada con su motivo dentro del codigo.

---

## 8. LOS DISCUTIBLES, MARCADOS ANTES DE SABER SI ACIERTO

**Ordenados del mas debil al mas firme dentro de cada bloque. Los cinco primeros son los que yo
mismo releeria primero.**

### Los mas debiles, y digo por que

| # | discutible | por que dudo |
|---:|---|---|
| **1** | **`actualizacion_posiciones_existentes` 5 a 19 entero a `evaluacion_balanceada_de_ejecutivos`** | **es el mas debil de los treinta.** Sus quince pasos traen **tres objetos distintos**: la conversacion de la degradacion (5 a 10), la evaluacion del ejecutivo que no escala (11 a 15) y la revision trimestral (16 a 19). **Solo los ultimos dos calzan con el miembro.** Ejecute sobre la frontera publicada, que es UNA, porque el encargo prohibe rehacer lecturas publicadas; **si el auditor lee que ahi habia dos o tres cortes y no uno, tiene razon y yo no** |
| **2** | **`producto_como_servicio_de_acceso` es un NOMBRE DE ESTA VUELTA** | la tabla de la vuelta 27 publicaba *nodo propio* sin id, a diferencia de los otros dos. El nombre, el cuerpo y la fase son mios |
| **3** | **fundir TRES bloques de TRES donantes distintos en `anillo_interior_explotar_el_canal_nucleo`** | la adjudicacion 3 habla de **DOS** bloques. Extendi a tres por la misma ratio. **Y el nodo nace con 15 pasos y una costura grande dentro** |
| **4** | **`analisis_trafico_competitivo` 5 a 8 a nodo propio** | `seleccion_plataforma_social_ads` tambien elige donde anunciarse por audiencia. Lo descarte porque el bloque parte de los anuncios **AJENOS** y no de la audiencia propia, **pero es un pelo** |
| **5** | **`decision_pivote_perseverar` 5 a 9 a nodo propio** | `identificacion_bolsas_virales` usa el mismo metodo (segmentar para encontrar el bolson). Lo descarte por objeto (viralidad contra decision de pivote), **no por metodo** |

### Los demas, marcados igual

| # | discutible |
|---:|---|
| **6** | **el CUERPO de los 13 nodos nuevos** (titulo, resumen, entregable, condiciones, etiqueta, fase, dominio) es texto de esta vuelta. El precedente es la adjudicacion 9 del acta 28 (*el fondo se relee el dia que el plan se aplique*): **ese dia es hoy, para los cuatro que venian sellados y para los nueve que sella esta vuelta** |
| **7** | **`key_partners_hypothesis` 11 a 14 a `pipeline_alianzas_bd`**: el eje de coincidencia es la **categorizacion**, que es una columna del entregable del miembro y no su acto entero |
| **8** | **`metricas_de_adquisicion_activacion` 6 a 9 a `sem_estrategia_ejecucion`**: tres de los cuatro pasos son metrica de campana en general; **solo el ultimo nombra el canal de busqueda** |
| **9** | **`organizacion_adaptativa` 5 a 8 a `contratacion_acelerada_hipercrecimiento`**: el bloque decide **cuando meter estructura**, y el miembro es de **contratacion** en hipercrecimiento. Comparten el umbral, no el sujeto |
| **10** | **`background_startup_vs_corporativo` 5 a 9 a `contratar_ambicion_correcta`** y no a `screening_ambicion_organizacional`: los dos son de ambicion, y elegi el del **TIPO** de ambicion |
| **11** | **`contratacion_experiencia_vs_potencial` 5 a 10 a `contratar_por_fortaleza`**: el paso 5 calza exacto, **pero los pasos 6 a 8 (promover adentro contra traer de afuera) no tienen miembro y viajan de arrimados** |
| **12** | **los tres nodos propios de HOR**: la ausencia se midio leyendo **titulos y entregables** de los 102, no los pasos de los 102 uno a uno. **Es un barrido mas barato que el de Hugos de la vuelta 28** |
| **13** | **declarar `compromiso_linea_tiempo_cliente` como quinta costura** que el acta no nombro |
| **14** | **declarar en la cola las costuras que caen dentro de nodos recien creados** (pendiente de doctrina 2) |
| **15** | **la ampliacion de `vuelta27_cortar.py`**: toco un instrumento que vueltas anteriores usaron |
| **16** | **ejecutar la rebanada `PLAN_V29_RELECTURA_D1.json`** en vez del plan sellado entero |
| **17** | **no ejecutar `OP-F-04-COL`** pese a que el encargo la pedia entera |
| **18** | **declarar los tres TOQUE UNICO como PARADA** en vez de ejecutarlos |
| **19** | **seguir trabajando despues de detectar la PARADA** en vez de parar en seco: los tres bloques no bloqueaban a `HOR` ni al resto de `WEI`, y la regla 5 manda no parar lo que se sostiene. **Si el auditor lee que *te detiene a ti* significaba parar la vuelta entera ahi, entonces las secciones 3.2 y siguientes sobran** |
| **20** | **no escribir `PARA_ALEXIS.md`** (precedente triple, adjudicacion 8 del acta 28) |

---

## 9. PREGUNTAS (regla 11: lo que no puedo medir, lo traigo)

1. **`OP-F-04-COL`**: la vuelta siguiente, la lee entera (trece fronteras mas quince destinos en
   una tanda), o **se parte en dos**: una vuelta que publica las trece fronteras como registro y
   otra que decide los destinos? **La segunda es la forma que `WEI` y `HOR` acabaron teniendo, y
   funciono.**
2. **Los tres TOQUE UNICO**: cuando el destejido deja **una sola version** de un material
   repetido dos o tres veces, **que se hace con la version que no sobrevive**? `P.3` prohibe
   podar. **Y para `coeficiente_viral`, cual de las dos reglas cede: la que prohibe fabricar un
   gemelo o la que prohibe forzar el encaje?**
3. **`viral_loop_marketing` esta en DOS operaciones**: cual corta primero, y el segundo corte se
   lee contra los pasos originales o contra los ya recortados? (El instrumento lee siempre
   contra los originales, por la leccion de la vuelta 27, **pero eso es dentro de un plan, no
   entre dos operaciones**.)
4. **El paso bien copiado en el nodo equivocado** (pendiente de doctrina 1): entra a la cola de
   la fase 02 por extension, o eso es doctrina nueva?
5. **`OP-F-03` se declara HECHA?** Sus diecinueve bloques estan en el arbol y su caso positivo
   pasa. La vuelta 28 la dejo PARCIAL por los cinco que faltaban, **y ya no faltan.** Lo digo
   como medicion, no como adjudicacion: **la pluma de declarar HECHA una operacion es del
   auditor.**
