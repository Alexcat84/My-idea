# EL RECOMPUTO DE LA FASE II, corte 3.388

**Vuelta 11 del bucle (Sonnet 5), 13 ago 2026. Disparador cumplido: el cribado intra-dominio
llego al puesto 3.388 (banco 9.21, `OP-U-02`).** Es la unica recomputacion general del plan.

**INSTRUMENTO, de solo lectura, autorizado esta vuelta:** `scripts/plan/recomputo_3388.py`. No
escribe ni un nodo, ni un veredicto, ni una operacion. Modelado sobre `scripts/plan/nominas.py`
(el `comp()` de componentes) y sobre el `res()` de `scripts/volcar_pares.py` (el resolutor de
alias, misma semantica que `resolverId` del motor).

**REGLA P.1 DEL BANCO DEL PLAN aplicada en los cuatro pasos: todo conteo que toque ids resuelve
antes de contar.** El grafo tiene hoy 3.835 nodos, 314 deprecados, 391 entradas de alias (77
huerfanas, 314 a nodo deprecado, 0 colisiones vivas, cifras de `CORRECCIONES_A_APLICAR.md`
CORRECCION 3, sin cambio).

**LO QUE ESTE DOCUMENTO NO HACE:** no cambia el estado de ninguna operacion.
`docs/plan/OPERACIONES.jsonl` no se toco esta vuelta. `OP-U-02` sigue en DECISION PENDIENTE hasta
que el auditor verifique las cuatro comprobaciones de mas abajo.

---

## PASO 1. EL RETRATO DE LAS A

**Comando:** `python scripts/plan/recomputo_3388.py` (paso 1 de su salida).

| | |
|---|---:|
| A crudas en el archivo (`clase == 'A'`), corte 3.388 | **583** |
| de esas, colapsan a auto-arista al resolver (mismo nodo vivo en los dos lados) | **0** |
| pares distintos en el retrato tras resolver y deduplicar | **583** |
| pares con mas de un veredicto crudo apuntando al mismo par resuelto | **0** |

**Ninguna de las 583 A colapsa.** Los 391 alias vigentes hoy son historia previa a esta campana
(ninguna fusion del plan de la pasada unica se ha ejecutado contra `dataset/`: verificado que
`nafta_free_trade_agreements`, el ejemplar de `OP-S-01`, sigue sin `deprecado`), asi que resolver
no fusiona ningun par de las 583 A en si mismo. **El retrato de las A vigentes al cierre, corte
3.388, es de 583 pares distintos.**

**COMPROBACION CRUZADA con la evidencia vieja:** las A con `puesto_intra <= 2117`, resueltas y
deduplicadas, dan **401** pares, contra las **400 A vigentes al puesto 2117** citadas como
evidencia de `OP-U-01`. ~~**Diferencia de una unidad, no investigada: fuera del alcance de este
recomputo** (la evidencia vieja no publica su comando ni su lista, asi que no hay con que
diferenciar). Se deja escrita como pregunta abierta, no como discrepancia que pare la vuelta:
ninguna cifra publicada con corte se contradice, la vieja no trae instrumento reproducible con el
que comparar par por par.~~

**CORRECCION DECLARADA (vuelta 12, auditor Opus 5, verificada por el ejecutor con instrumento
propio antes de escribirse): la diferencia de una unidad ESTA RESUELTA, PAR POR PAR, Y NO ES UNA
CONTRADICCION.** El repositorio guarda el archivo al corte exacto (`git show
c16a24f5:docs/INTRA_DOMINIO_VEREDICTOS.jsonl`, 11 ago 2026, 2.117 lineas). Comparado clase a clase
contra el archivo de hoy en ese mismo tramo (2.117 primeras lineas): **cambia UNA sola clase, el
puesto 2.078** (`elaboracion_fdd` contra `preparar_fdd`, dominio `franquicias`), **D el 11 ago 2026
y A hoy por correccion posterior declarada**. El archivo viejo tiene exactamente **400 A**. **No
hay descuadre: hay una correccion declarada, y cada cifra es correcta en su corte** (banco 9.21,
"toda cifra de cruce lleva su fecha de corte"). Verificado por el ejecutor con un script propio de
comparacion linea a linea contra el blob del commit `c16a24f5`: un solo cambio de clase en las
2.117 lineas, exactamente el 2.078, exactamente D a A.

---

## PASO 2. EL BARRIDO DE CONFIRMADAS CONTRA LAS A

~~**NO CORRIDO.**

**LA BUSQUEDA, tal como pide el encargo, empezando por los dos ficheros senalados:**

- `docs/plan/01_FUENTES.md`, linea 53 (tabla de la aritmetica de los 18) y linea 62 (la nota que
  distingue los dos numeros de Hugos): **la cifra 11 aparece dos veces, siempre como CONTEO**
  ("11 son costuras confirmadas con pegado de Hugos"), nunca como nomina.
- `docs/plan/CORRECCIONES_A_APLICAR.md`, lineas 169-174 (CORRECCION 4): **misma cifra, mismo
  tratamiento**, conteo sin lista.
- Busqueda ampliada sobre `docs/` completo (`grep -rn "costuras confirmadas"`,
  `"confirmadas de rebote"`): `docs/COSTURAS_INTERNAS_RESUMEN.md` secciones 6 y 7 y
  `docs/FICHA_SUBFUSION_GRADIENTE.md` (marcador de la clase, `~3400-3430`) **repiten el total de
  46 costuras confirmadas (45 nucleo + 1 `quality`) sin nomina**. `docs/GRADIENTE_VEREDICTOS.md`
  tiene una familia con nombre parecido, **"costuras confirmadas DE REBOTE"** (6 casos, esos si
  nombrados: `ratios_eficiencia_inventario`, `plan_mejora_procesos`, `economia_circular`,
  `propuesta_gasto_capital`, y dos mas), **pero es OTRO UNIVERSO**: verificaciones post-cirugia de
  la cola del gradiente semantico, no la nomina de las 46 confirmadas del cierre de costuras
  internas que este paso 2 necesita.

**RESULTADO: la nomina de las 11 (ni la de las 46) no esta escrita como lista en ningun sitio del
repositorio.** Por la instruccion del encargo, **el paso 2 NO SE CORRE**: no se inventa ni se
reconstruye de memoria. Queda declarado como pendiente para quien tenga a mano la nomina original
del cierre de costuras (probablemente en una sesion de trabajo que no dejo el listado en disco).~~

**CORRECCION DECLARADA (vuelta 12, adjudicacion del auditor: el paso 2 se puede correr sin
inventar nomina, por la VIA ACOTADA). El paso pasa de NO CORRIDO A CORRIDO.**

**LO QUE FALTABA NO ERA LA NOMINA DE LAS 46: era el archivo de salida del propio instrumento.**
`docs/COSTURAS_INTERNAS.jsonl` existe, 128 filas con `node_id`, `dominio`, `pasos`, `corte`,
`disparo_bloque` y `disparo_pareja` (verificado: 128 filas, campos exactos). No trae el veredicto,
asi que la nomina de las confirmadas no esta ahi como dato directo; pero el paso 2 no necesita la
nomina entera, solo necesita saber que citas caen dentro del retrato de las A.

**1. Cruce de las 128 citas (resueltas por alias, P.1) contra los 854 nodos con al menos una A del
paso 1 y 3.** Comando: recorrer `docs/COSTURAS_INTERNAS.jsonl`, resolver cada `node_id` por alias,
y comparar contra el conjunto de nodos del paso 3. **Verificado por el ejecutor: la interseccion es
de TREINTA Y SEIS nodos**, exacto contra la cifra del auditor. Las 128 citas resuelven a 128 nodos
distintos (cero colisiones por alias en este universo), y de esos, 36 tienen al menos una A vigente
al corte 3.388.

**2. Para esos treinta y seis, y solo esos, el veredicto YA ESCRITO**, buscado en
`docs/FICHA_SUBFUSION_GRADIENTE.md`. **Los treinta y seis, sin excepcion, aparecen en la tabla
reconciliada de esa ficha** (lineas 3651 a 3780, "Las 128, con su fila y su veredicto", la misma que
declara "cada una de las 128 citas leidas vive en exactamente una fila"): **36 de 36 tienen
veredicto escrito, cero SIN VEREDICTO ESCRITO.** Ningun nodo se leyo de nuevo ni se adivino desde el
texto: los 36 veredictos son copia literal de esa tabla, citados linea por linea.

| clase | cuantos | nodos, con su linea en FICHA_SUBFUSION_GRADIENTE.md |
|---|---:|---|
| **CONFIRMADA** | **15** | `ab_testing_optimizacion` (3660), `blueprint_de_experiencia` (3671), `brainstorming_divergente` (3766), `customer_journey_mapping` (3693), `future_scenarios_planning` (3676), `key_partners_hypothesis` (3663), `optimizacion_embudo_get_customers` (3775), `plan_de_adquisicion_acquire` (3697), `principio_calidad_mvp` (3686), `producto_minimo_viable` (3653), `producto_unico_superior` (3773), `propuesta_gasto_capital` (3776), `seleccion_ceo_fundador` (3743), `split_testing_experimentos_ab` (3664), `voz_del_cliente_voc` (3672) |
| **FALSA** | **21** | `captura_conocimiento_mercado` (3769), `control_estadistico_de_procesos` (3717), `criterios_equity_split` (3700), `design_for_six_sigma_dfss` (3710), `dso_dpo_gestion_capital_trabajo` (3777), `evaluacion_riesgo_calidad_organizacional` (3723), `eventos_offline_como_canal_traccion` (3764), `export_administration_regulations` (3716), `ferias_comerciales_franquicia` (3740), `founder_ceo_succession_process` (3665), `funcion_protect_politica_seguridad` (3724), `getting_started_maintenance` (3720), `metricas_accionables` (3741), `mix_ubicaciones_corporativas_franquicia` (3666), `modelo_spin_preguntas` (3747), `portfolio_management` (3767), `regalos_estrategicos_sorpresa` (3756), `tipos_innovacion_i_ii` (3779), `verificar_modelo_ingresos` (3692), `vesting_acciones_fundadores` (3759), `viaje_diagnostico_remedial` (3722) |
| **SIN VEREDICTO ESCRITO** | **0** | (ninguno) |

**3. Los que salen CONFIRMADA son las CURAS ACOPLADAS** (destejido y fusion en el mismo acto, banco
9.4). **La ficha ya tiene la serie escrita** (SANO POR DENTRO, GEMELO POR FUERA, con sus ejemplares
CUARTO a DUODECIMO mas el DECIMOTERCERO Y CUARTO, lineas 2899 a 3184) **y ninguno de los 15 es
nuevo: los 15 ya estan escritos, se citan, no se reescriben:**

- **Diez tienen ejemplar numerado propio** en la serie: `optimizacion_embudo_get_customers`
  (CUARTO, linea 2940), `producto_unico_superior` (QUINTO, linea 2973),
  `propuesta_gasto_capital` (SEXTO, linea 2990), `key_partners_hypothesis` (SEPTIMO, linea 3008),
  `split_testing_experimentos_ab` (OCTAVO, linea 3029), `voz_del_cliente_voc` (NOVENO, linea 3051),
  `ab_testing_optimizacion` (UNDECIMO, linea 3091), `seleccion_ceo_fundador` (DUODECIMO, linea
  3111), `producto_minimo_viable` y `principio_calidad_mvp` (DECIMOTERCERO Y CUARTO, LA CURA
  ACOPLADA MAYOR, linea 3118).
- **Dos son el precedente citado dentro de esa misma serie**: `blueprint_de_experiencia` y
  `customer_journey_mapping` (puesto 341, "precedente exacto" nombrado en la linea 3128, con su
  propia seccion en la ficha, lineas 846 a 1260).
- **Tres estan en la tabla "TRES que el goteo no habia encontrado"** del recuento completo del 13
  ago 2026 (linea 3154 a 3163): `brainstorming_divergente` (tres gemelos, 823/834/844),
  `future_scenarios_planning` (`escenarios_futuros`, 711) y `plan_de_adquisicion_acquire`
  (`plan_acquire_activate`, 344).

**VERIFICACION CRUZADA, no pedida por el encargo pero barata y decisiva: los 15 CONFIRMADA ya
tienen operacion propia en `docs/plan/OPERACIONES.jsonl`.** Cada uno de los 15 aparece en la nomina
de `nodos` de alguna `OP-D-01` a `OP-D-06`: `OP-D-01` (producto_minimo_viable,
principio_calidad_mvp), `OP-D-02` (voz_del_cliente_voc), `OP-D-03` (ab_testing_optimizacion,
optimizacion_embudo_get_customers, split_testing_experimentos_ab), `OP-D-04`
(brainstorming_divergente), `OP-D-05` (seleccion_ceo_fundador), `OP-D-06` (todos los demas:
blueprint_de_experiencia, customer_journey_mapping, future_scenarios_planning,
key_partners_hypothesis, plan_de_adquisicion_acquire, producto_unico_superior,
propuesta_gasto_capital, mas los dos que repite con `OP-D-01`). **Cero de los 15 quedan sin dueno.**
El paso 2, corrido por la via acotada, no encuentra ninguna cura acoplada nueva que el plan no
tuviera ya contemplada: confirma que `OP-D-01` a `OP-D-06` son exhaustivas sobre el universo de los
36.

---

## PASO 3. EL CIERRE TRANSITIVO

**Calculado sobre el retrato del paso 1 (las 583 A resueltas), no sobre el archivo crudo.**

| | |
|---|---:|
| nodos con al menos una A (tras resolver) | **854** |
| componentes totales (tamano >= 2) | **335** |
| distribucion de tamanos | 2: 244 &#124; 3: 56 &#124; 4: 16 &#124; 5: 7 &#124; 6: 5 &#124; 7: 2 &#124; 8: 1 &#124; 9: 1 &#124; 10: 1 &#124; 13: 1 &#124; 15: 1 |

**Las componentes grandes nombradas por `OP-U-01`/`OP-U-02` al corte 2.117 siguen presentes hoy,
mismo tamano, identificadas por el nodo que la nota de esas operaciones cita** (verificado por
coincidencia de nombre y tamano, no por un registro historico de membresia completa que no
existe):

| tamano | nombre citado en la nota vieja | miembro que la identifica | sigue del mismo tamano hoy |
|---:|---|---|---|
| 13 | "puertas y portafolio" | `gestion_de_portafolio_gates_go_kill` | **si, 13** |
| 9 | "customer discovery" | `customer_discovery` | **si, 9** |
| 8 | "build, measure, learn" | `build_measure_learn` | **si, 8** |
| 7 | "customer validation" | `customer_validation` | **si, 7** |
| 7 | "el brainstorming" | `brainstorming_divergente` | **si, 7** |

**Ninguna de las cinco crecio ni se cerro entre el 2.117 y el 3.388.** Las dos que `OP-U-02`
declaraba con dueno en otra fase tambien se confirman presentes con su nomina completa: la de
`OP-D-03` (`ab_testing_optimizacion`, `funnel_get_customers_optimizacion`,
`optimizacion_embudo_get_customers`, `split_testing`, `split_testing_experimentos_ab`,
`test_ab_precio`, tamano 6) y la de `OP-D-04` (`brainstorming_divergente` y sus seis companeros,
tamano 7, la misma de la fila de arriba).

**La componente nueva mas grande, tamano 15, es enteramente del dominio `health_safety`**
(`cultura_de_seguridad_interpretivista_funcionalista`, `errores_como_consecuencia`,
`new_view_vs_old_view`... la familia entera de vieja-vision-contra-nueva-vision del error humano):
no existia al corte 2.117 porque el cribado de `health_safety` no habia cerrado todavia (cierra en
la seccion 80 del informe, con puesto posterior a 2.117). **La segunda componente nueva mas
grande, tamano 10, es enteramente de `quality`** (`causas_comunes_vs_especiales` y su familia de
nueve companeros): tampoco existia al corte 2.117, porque `quality` no habia abierto su cribado
(seccion 81, tambien posterior).

---

## PASO 4. LAS NOMINAS Y LOS ACTOS, con cobertura al lado

**Cada componente re-medida con banco 9.26 (cobertura al lado) y reclasificada CERRADO/ABIERTO con
el mismo criterio de `OP-U-01`: CERRADO cuando TODOS los pares posibles entre miembros estan
leidos (`fuera_de_cola == 0` y `en_cola_sin_leer == 0`); ABIERTO en cualquier otro caso.**

**AVISO METODOLOGICO QUE CAMBIA EL CALCULO RESPECTO AL 2.117: la cola intra-dominio esta AGOTADA
(verificado, `docs/INTRA_DOMINIO_PARES.jsonl` y `docs/INTRA_DOMINIO_VEREDICTOS.jsonl` tienen
EXACTAMENTE los mismos 3.388 pares, cero diferencia en ningun sentido).** Eso significa que la
segunda condicion del criterio de `OP-U-01` ("ningun miembro tiene un par pendiente en la cola sin
leer") **es hoy trivialmente cierta para todo el mundo**: no queda ni un par de la cola sin leer.
Lo unico que puede dejar abierto un acto hoy es la primera condicion: que existan pares POSIBLES
entre miembros del acto que **nunca entraron a la cola** (el universo de `OP-L-02`, "fuera de
cola"). El script lo mide exactamente asi: `fuera_de_cola` es la cuenta de esos pares.

### El marcador nuevo

| | corte 2.117 (`OP-U-01`/`OP-U-02`) | corte 3.388 (esta vuelta) | diferencia |
|---|---:|---:|---:|
| actos totales (tamano >= 2) | 221 | **335** | **+114** |
| **CERRADOS** | 173 | **280** | **+107** |
| nodos en actos CERRADOS | 371 | **600** | **+229** |
| **ABIERTOS** | 48 | **55** | **+7** |
| nodos en actos ABIERTOS | 205 | **254** | **+49** |
| nodos en actos, total | 576 | **854** | **+278** |

**CERRADOS por tamano (corte 3.388):** 2: 244, 3: 32, 4: 4. Contra el 2.117 (149 de dos, 23 de
tres, 1 de cuatro, el de SPIN): **crecieron los tres niveles**, y el de cuatro paso de 1 a 4 (SPIN
sigue siendo uno de ellos, verificado por nombre: `framework_spin_selling`,
`metodologia_spin_selling`, `modelo_spin`, `modelo_spin_preguntas`, presente en la lista de
tamano 4).

**ABIERTOS por tamano (corte 3.388):** 3: 24, 4: 12, 5: 7, 6: 5, 7: 2, 8: 1, 9: 1, 10: 1, 13: 1,
15: 1. Los de tamano >= 5 suman **19** (7+5+2+1+1+1+1+1), contra los **16** nombrados al 2.117
(1 de 13, 1 de 9, 1 de 8, 2 de 7, 4 de 6, 7 de 5). **La diferencia de +3 se explica entera:** la
fila de seis crecio de CUATRO a CINCO (+1), y aparecen las dos componentes enteramente nuevas
identificadas en el paso 3, tamano 10 (+1) y tamano 15 (+1). 4+1+1+1 no cuadra con la aritmetica
simple porque el quinto miembro de la fila de seis TAMBIEN es nuevo (arista mas vieja posterior al
2.117): 16 (viejos) + 1 (crecio la fila de 6) + 1 (el de 10) + 1 (el de 15) = 19.

### Cuantos actos son continuacion de antes del 2.117 y cuantos son enteramente nuevos

**MEDIDO POR PROXY DE EDAD DE ARISTA (la fecha, `puesto_intra`, de la A mas antigua que conecta
cada par dentro de la componente), NO POR UN MAPEO 1 A 1 CONTRA LA MEMBRESIA DE LOS 48 ANTIGUOS:
esa membresia completa nunca se escribio como lista en ningun documento del plan (solo tamanos y
un puñado de nombres, citados arriba), asi que un mapeo exacto no se puede hacer sin inventar.**
Este proxy es lo maximo que se puede medir sin adivinar:

| | actos | de ellos, ABIERTOS | de ellos, CERRADOS |
|---|---:|---:|---:|
| **TODO ANTERIOR AL 2.117** (todas sus aristas A tienen puesto <= 2.117) | 221 | 42 | 179 |
| **MIXTO** (al menos una arista <= 2.117 y al menos una > 2.117) | 1 | 1 | 0 |
| **TODO POSTERIOR AL 2.117** (todas sus aristas A tienen puesto > 2.117) | 113 | 12 | 101 |

**Lectura, con la cautela de que es un proxy:** de los 55 actos abiertos de hoy, **43 (42 + el
mixto) tienen alguna arista anterior al 2.117**, o sea que son continuacion de algo que ya existia
en alguna forma (abierto o cerrado) al corte viejo; **12 son enteramente nuevos**, formados por
completo dentro del cribado que corrio despues del 2.117. **Ninguno de los cinco actos grandes
nombrados en la tabla del paso 3 aparece entre los enteramente nuevos** (los cinco tienen su A mas
vieja anterior al 2.117, verificado). ~~**Con esa cautela declarada: no se puede decir con certeza
cuantos de los 48 antiguos cerraron**, porque un acto abierto viejo pudo haberse partido o fundido
con otro por una A nueva y el proxy de edad no distingue eso de una simple continuacion. Lo que
si se puede decir, medido: ninguno de los CINCO actos grandes identificables por nombre paso de
abierto a cerrado, y 113 actos son enteramente producto del cribado que corrio entre el 2.117 y
el 3.388 (los 1.271 pares que faltaban), de los cuales 101 nacieron ya cerrados (en su
mayoria pares de dos de `quality`, que aporta 25 de las 28 fusiones mutuas del catalogo) y 12
nacieron abiertos (entre ellos las dos componentes nuevas mas grandes, tamano 15 en
`health_safety` y tamano 10 en `quality`).~~

**CORRECCION DECLARADA (vuelta 12, auditor Opus 5, VERIFICADA POR EL EJECUTOR CON INSTRUMENTO
PROPIO, no solo transcrita): el mapeo de los 48 antiguos SI se puede hacer 1 a 1, sin proxy.** La
condicion que lo permite: **la cola `docs/INTRA_DOMINIO_PARES.jsonl` esta completa en 3.388 pares
desde el 9 ago 2026** (`c442345a`, "la cola completa, 3388 pares ordenados") **y no se ha tocado
desde entonces** (`git diff --stat c442345a -- docs/INTRA_DOMINIO_PARES.jsonl` vacio), asi que la
cola contra la que se midio `OP-U-01` el 11 ago 2026 es la misma de hoy. **Metodo:** se vuelve a
correr la medicion de `OP-U-01` sobre el mismo archivo, truncado al corte viejo (2.117 lineas) y
**excluyendo la correccion posterior del 2.078** (forzado a D, su clase el 11 ago), con el
CRITERIO ORIGINAL DE DOS CONDICIONES escrito en la nota de `OP-U-01`/`OP-U-02`: (1) todos los pares
posibles entre miembros ya leidos, y (2) **ningun miembro tiene un par pendiente en la cola sin
leer, CONTRA CUALQUIER NODO, no solo contra otro miembro del acto**. Con la condicion (2) medida en
su forma completa (no solo pares internos al acto, que es la simplificacion valida SOLO cuando la
cola esta agotada, como al corte 3.388), **el ejecutor reproduce la cifra publicada EXACTA**: 221
componentes sobre 576 nodos, **173 cerrados sobre 371** (149 de dos, 23 de tres, uno de cuatro),
**48 abiertos sobre 205**, motivos **42 por par interno mas 6 por miembro pendiente**. Con esa
membresia:

| los 48 actos abiertos del 2.117 | cuantos | verificado |
|---|---:|---|
| **CERRARON** (mismos miembros, hoy CERRADO) | **5** | si |
| siguen abiertos, identicos, sin crecer | **42** | si |
| siguen abiertos y CRECIERON | **1** | si (`gestion_terminacion_franquiciado` con `terminacion_franquiciado_causas`, de 2 a 3) |

Y por el otro lado: **114 actos de hoy no contienen ni un nodo que estuviera en un acto del 2.117**;
**102 de esos nacieron cerrados y 12 nacieron abiertos**. Las cuentas cierran: 173 + 5 + 102 =
**280**; 42 + 1 + 12 = **55**. **El proxy de edad de arista de arriba (221/1/113, con 101 nacidos
cerrados y 12 abiertos) difiere en exactamente una unidad, y la unidad es el mismo 2.078**: su
arista es anterior al 2.117, asi que el proxy lo llama continuacion, pero en el corte viejo ese
par era D y su acto no existia. Las dos mediciones son coherentes entre si una vez nombrada la
causa. **Ninguno de los cinco actos grandes identificables por nombre cerro ni cambio de
tamano**, confirmado con las dos vias.

---

## LAS CUATRO COMPROBACIONES

**Comando:** el mismo, seccion final de su salida.

| # | comprobacion | resultado |
|---:|---|---|
| **i** | nodos en actos (854) == suma de tamanos de las componentes (854) | **OK** |
| **ii** | A vigentes resueltas del retrato (583) == suma de aristas A internas de las componentes (583) | **OK** |
| **iii** | todo acto CERRADO tiene sus pares internos leidos y ningun miembro con par pendiente | **OK**, verificado sobre los 280 |
| **iv** | ningun nodo deprecado aparece dentro de una componente | **OK**, 0 encontrados |

**LAS CUATRO CUADRAN.** El recomputo esta bien hecho por su propio criterio: no hay auto-aristas
fantasma, no hay deprecados colados dentro de una componente (que habria significado que el
resolutor no resolvio), y las dos sumas de control (nodos y aristas) cierran exactas.

---

## POR QUE LA DIFERENCIA DE `OP-E-03` (387 FILAS) NO BAJO, CERRADO

**Pregunta abierta de la TAREA 3 de la vuelta 11** (`docs/loop/REPORTE.md` de esa vuelta, que se
sobreescribe por vuelta, y `docs/plan/08_VERIFICACION.md`): el encargo de esa vuelta esperaba que
la diferencia del barrido calibrado contra la cola BAJARA una vez que `risk_management`,
`seguridad_digital` y `quality` cerraran su cribado, porque el ensayo en vacio del 11 ago 2026
(387 de 477) se corrio cuando esos tres dominios (`quality` sobre todo) todavia no tenian cola.
**No bajo: sigue en 387 de 477, byte por byte identico.**

**CORRECCION DECLARADA (vuelta 12, auditor Opus 5, adjudicacion 2.c de su acta): la expectativa de
baja fue un error del auditor, no del ejecutor, y la razon decisiva se lee directo en el script.**
`scripts/plan/diferencia_contra_cola.py` compara cada candidato del barrido contra la **UNION** de
`docs/INTRA_DOMINIO_PARES.jsonl` (la cola PLANIFICADA) **mas** `docs/INTRA_DOMINIO_VEREDICTOS.jsonl`
(los pares ya leidos), y **la primera esta completa en 3.388 pares desde el 9 ago 2026** (`c442345a`,
verificado sin diferencia contra el estado de hoy). **La cola planificada no crece cuando un
dominio se criba: crece el archivo LEIDO, que ya estaba dentro de la union desde antes.** Por eso
el 387 no podia moverse pasara lo que pasara con `quality`, `risk_management` o `seguridad_digital`:
esos tres dominios ya aportaban sus pares a la union por el lado de `INTRA_DOMINIO_PARES.jsonl`
desde el 9 ago, antes incluso del ensayo en vacio del 11 ago que produjo el 387. **El ejecutor de
la vuelta 11 hizo bien en publicar la cifra sin forzar la baja**; su explicacion de entonces
(heuristicas de generacion de candidatos distintas, solape estructuralmente chico) es cierta pero
no era la razon decisiva. Queda escrita aqui la razon decisiva, para que ningun encargo futuro
vuelva a pedir una baja imposible.

---

## LO QUE ESTE RECOMPUTO NO DECIDE

~~**Ninguna operacion cambia de estado con este documento.** `OP-U-02` queda con la evidencia de
arriba, a la espera de que el auditor verifique las cuatro comprobaciones y autorice el paso a
LISTA en el encargo siguiente. `OP-U-01`, `OP-L-02`, las cinco mesas y las seis `OP-D-*` siguen con
sus cifras del corte 2.117 hasta esa misma autorizacion (banco del plan P.12: el cierre transitivo
CONVOCA, no decide; una componente medida no es una fusion aprobada).~~

**CORRECCION DECLARADA (vuelta 12): la autorizacion ya se dio.** El auditor (Opus 5, acta vuelta
11, adjudicacion 4.1) verifico las cuatro comprobaciones con instrumento propio, con la prueba
extra de identidad conjunto a conjunto de las 335 componentes, y autorizo el paso. **Esta misma
vuelta, `docs/plan/OPERACIONES.jsonl` SI se edita** (TAREA 2.A del encargo): `OP-U-02` pasa a
LISTA con `fecha_corte` 2026-08-13, y `OP-U-01`, `OP-L-02`, las cinco mesas y las seis `OP-D-*`
reescriben sus cifras con el corte 3.388 al lado del corte 2.117 (banco 9.21, la vieja no se
borra). El recomputo en si (este documento) sigue siendo lectura pura: la escritura vive en
`OPERACIONES.jsonl`, no aqui.

**El fichero de detalle, con las 335 componentes fila por fila (miembros, cobertura, clases
internas, estado, edad), vive en** `docs/plan/RECOMPUTO_3388_COMPONENTES.jsonl`, **solo lectura,
salida directa del script.**
