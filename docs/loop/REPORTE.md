# REPORTE DE LA VUELTA 39, 19 ago 2026. Ejecutor: Opus 5. Rama `pasada-unica`

**LO QUE ESTA VUELTA HIZO EN UNA LINEA: `OP-D-04` CERRADA CON SUS DOS FUSIONES EJECUTADAS Y EL
RESTO ENLAZADO, y `OP-D-05` abierta y medida.** Cuatro nodos absorbidos, cero borrados, todo verde,
**y tres cosas que salieron mal que van escritas antes que las que salieron bien.**

---

## 0. LA APERTURA, MEDIDA ANTES DE LA PRIMERA OPERACION (regla 1)

**Corrida:** `python scripts/loop/vuelta31_estado.py`, salida entera en
`docs/loop/SALIDA_V39_APERTURA.txt`, **commiteada sola en `03e8e0e8` antes de tocar nada.**

| | apertura (antes de la primera operacion) |
|---|---:|
| marcador | `n 3.388`, A **575**, B **83**, C **8**, D **2.722**, tasa **17,0** |
| grafo | **3.853** ficheros, **3.538** vivos, **315** deprecados, **16.849** enlaces |
| operaciones | **71**, todas `LISTA`, **0** dependencias rotas |
| inventario | **672** entradas |

**Identica al cierre de la vuelta 38, que es exactamente lo que tenia que dar: aquella vuelta no
toco ni un nodo.** La comparacion se hace contra `docs/loop/SALIDA_V38_CIERRE.txt`, leida hoy.

---

## 1. LA CORRECCION QUE EL ACTA DE LA VUELTA 38 DEJO ENCARGADA

**El acta declaro UNA caida de reporte con nombre, y aqui va corregida sin borrar nada.** El
reporte de la vuelta 38 publico que el diff `f734ab67..1b2f3dd5` traia **4.043 insertadas**. El
auditor lo re-corrio y le dio **4.044**.

> **LA CIFRA BUENA ES 4.044. LA QUE YO PUBLIQUE, 4.043, ESTABA MAL POR UNA LINEA.** Las 26 rutas y
> las 366 borradas si reproducian. **El texto viejo no se toca**: vive en el acta, que es donde la
> caida quedo registrada con su nombre (`ACTA_AUDITOR.md`, seccion 1, leida hoy).

---

## 2. LA GUARDA PREVIA: LAS DOS SIMULACIONES SELLADAS, `BYTE IGUAL`

**Antes de escribir una sola letra**, las dos simulaciones de la vuelta 38 se re-corrieron con el
mismo instrumento y con el acto entero en el parametro del acto:

```
python scripts/plan/simular_fusion.py \
  --fusion reglas_brainstorming:brainstorming_divergente \
  --fusion reglas_brainstorming:brainstorming_efectivo \
  --acto brainstorming_divergente,brainstorming_efectivo,reglas_brainstorming,generar_multiples_opciones,pensamiento_convergente_divergente,design_attitude_vs_decision_attitude,construir_sobre_ideas_ajenas,brainstorming
```

| | contra | resultado |
|---|---|---|
| el taller | `SALIDA_V38_SIM_TALLER.txt` | **BYTE IGUAL**, `md5 e3a3c927ac9a442a1d70aaa90609d2ce` |
| la alternancia | `SALIDA_V38_SIM_ALTERNANCIA.txt` | **BYTE IGUAL**, `md5 ff1158100310dec30e34fc53cf2bcced` |

**Nada del grafo se habia movido desde el sellado, y eso se comprobo en vez de suponerse.** Copias
de esta vuelta en `SALIDA_V39_SIM_TALLER.txt` y `SALIDA_V39_SIM_ALTERNANCIA.txt`.

---

## 3. LAS TRES COSAS QUE SALIERON MAL, Y VAN PRIMERO

### 3.1 `GATE 0` CAYO EN ROJO A LA PRIMERA: el plan sellado no enumeraba los puentes

Ejecutada la fusion del taller, el ciclo devolvio:

```
[FALLO] Ningun puente aprobado apunta a un nodo deprecado (valor: 1 rotos: ['quality:brainstorming_efectivo'])
GATE 0: FALLIDO
```

**El plan enumeraba las 17 referencias de NODO y ninguna del registro de puentes**
(`packs/quality/metadata/bridges_aprobados.json`). **La simulacion de `P.7` tampoco lo ve: mira el
grafo, y un puente no vive en el grafo.**

**Se resolvio con el instrumento de la casa**, `scripts/reanclar_por_resolutor.py`, **que mueve
REFERENCIAS y jamas nodos** y va **por el resolutor** (`P.1`, regla 9 del `EJECUTOR`):

```
  [puente] quality: brainstorming_efectivo -> reglas_brainstorming  (Reglas de Brainstorming Efectivo)
  1 referencias re-ancladas.
```

El ancla queda en `reglas_brainstorming` con **`ancla_original: brainstorming_efectivo`**. **No es
una decision recalculada: es la misma redireccion que la fusion ya hace, sobre un registro que el
plan no listo.** El precedente esta **medido tres veces en git y no recordado**: `a2902995` (*Los
tres redirigidos a su superviviente*), `06dd2922` (*EL GATE 0 VOLVIO A CAZAR UN PUENTE a un recien
deprecado... Redirigido a su superviviente*) y `33265c05`, que es el commit **que creo el
instrumento** justamente para no cazar el mismo pez cuatro veces. **VA COMO DISCUTIBLE 1.**

### 3.2 MI PROPIO INSTRUMENTO CAYO DOS VECES ANTES DE ACERTAR

**Las dos correcciones van escritas DENTRO del codigo, no solo aqui.**

| | que hacia mal | como se corrigio, y por que NO se aflojo |
|---|---|---|
| **guarda 1**, la fuente | leia `fuente_esperada` como si fuera **la de los tres nodos**. Cayo en rojo contra los dos absorbidos del taller | los dos actos de `OP-D-04` son **DE FUENTE MIXTA**, medido: `divergente` es *Change by Design, Revised*, `efectivo` es *Change by Design*, el superviviente es *Osterwalder*. La guarda ahora exige la fuente **del superviviente** y **IMPRIME LAS TRES**, y exige que la de cada absorbido **viaje verbatim a `merged_originals`** |
| **guardas 6 y 7**, `preservar` y `rastros` | heredaron de `vuelta33_fundir.py` un cuerpo hecho **solo de pasos**. Cayeron en rojo contra la alternancia por `3-5 alternativas`, `convergencia` e `iteraciones` | **fui a mirar y las tres SI sobreviven**, en el entregable y en el resumen. **Lo roto era la vara, no el plan.** La vara corregida coteja **los CUATRO campos de texto** que la fusion escribe **y ademas imprime EN CUAL sobrevive cada pieza**, para que la sede no se pueda esconder |

> **Las dos cayeron haciendo su trabajo.** Una guarda que no cae nunca no es una guarda.

### 3.3 UN INSTRUMENTO DE LA CASA NO ENTREGA, Y NO SE LE TOCO EL UMBRAL

`scripts/costuras_internas.py` se niega en **su propia puerta de calibracion**:

```
INSTRUMENTO MAL CALIBRADO. No entrega nada.
  La calibracion conocida no aparece en la cola: ['plan_mejora_procesos']
    plan_mejora_procesos: 5 pasos, mejor pareja 47.1, mejor bloque 43.1 (corte tras 2)
  Umbrales usados: pareja 80, bloque 44
```

**Su fixture ya no dispara: 43,1 contra un umbral de 44.** La averia es **ANTERIOR a esta vuelta y
ajena a ella** (esta vuelta no toco ese nodo). **NO SE AFLOJO EL UMBRAL para que entregara**, que
seria arreglar la vara en vez de la pieza. **VA COMO PENDIENTE 1 al fundador.**

---

## 4. `OP-D-04`: LAS DOS FUSIONES EJECUTADAS

**Se ejecutaron TAL COMO estaban selladas, sin recalcular ni una decision**, en el orden del
encargo: primero el taller, despues la alternancia. **Instrumento nuevo**,
`scripts/loop/vuelta39_fundir.py`, **sucesor declarado** de `vuelta33_fundir.py` (que solo sabe de
UN absorbido y de otro esquema de plan).

### LAS TRECE GUARDAS, escritas para caer, por operacion

| guarda | el taller | la alternancia |
|---|---|---|
| 1, fuente del superviviente y vida de los tres | OK, **con las tres fuentes impresas** | OK, idem |
| 2, conteos contra el plan | OK, 3 de 3 nodos | OK, 3 de 3 |
| 3, **VERBATIM** contra `dataset/nodos` | **19 de 19**, 0 sobrantes | **16 de 16**, 0 sobrantes |
| 4, cobertura exacta de origenes | **13 pasos** y **6 condiciones**, 0 repetidos, 0 faltan, 0 sobran | **11 pasos** y **5 condiciones**, idem |
| 5, los finales derivados de los grupos | OK | OK |
| 6, `preservar_literal` con su sede impresa | **5 de 5** | **5 de 5** |
| 7, `rastros` con su sede impresa | **5 de 5** | **5 de 5** |
| 8, redirecciones contra el plan | **17 de 17** | **5 de 5** |
| 8b, deprecados que nombran y NO se tocan | **0**, como el plan dice | **1**, `fase_entender_modelo_negocio` |
| 9, **`P.16`**, duplicadas fabricadas | **1**, `prototipado_rapido.nodos_previos` | **1**, `analisis_y_sintesis.nodos_siguientes` |
| 10, cero auto arista tras resolver | **0** | **0** |
| 11, cero duplicada tras resolver | **0** | **0** |
| 12, **`a6`**, titulo y etiqueta sin tocar | OK | OK |
| 13, el censo | 3.853 = 3.853, vivos **menos 2** | 3.853 = 3.853, vivos **menos 2** |

**`P.16`, QUIEN FABRICA LIMPIA: la duplicada de cada fusion se midio ANTES de limpiarla, se cotejo
contra el plan, y se resolvio EN LA MISMA OPERACION.** Cero duplicadas y cero auto aristas al
salir.

### LA GUARDA DE SIMETRIZACION, EXACTA Y RELEIDA EN EL FICHERO

`scripts/loop/vuelta39_guarda_simetrizacion.py`, contra `dataset/metadata/phase1_run_log.json`:

| | entradas en el log | para el superviviente | de otros nodos | el plan esperaba | faltan | sobran |
|---|---:|---:|---:|---:|---:|---:|
| `reglas_brainstorming` | **16** | **16** | **0** | **16** | **0** | **0** |
| `pensamiento_convergente_divergente` | **4** | **4** | **0** | **4** | **0** | **0** |

**Cotejadas UNA A UNA contra `simetrizacion_esperada`, y ademas RELEIDAS en `dataset/nodos`**: 16
de 16 y 4 de 4 presentes en el fichero. **Un log dice lo que el paso 5 cree que hizo; el fichero
dice lo que paso.**

### EL ENLACE DEL CUARTO MIEMBRO LLEGO SOLO, tal como el plan predijo

```
    reglas_brainstorming    nombra a brainstorming            en ['nodos_siguientes']
    brainstorming           nombra a reglas_brainstorming     en ['nodos_previos']
  GUARDA 3, la arista esta en los dos ficheros y en campos opuestos: OK
```

**Nadie la escribio: la trajo la redireccion de la entrada que nombraba a `brainstorming_efectivo`.**

### EL CASO POSITIVO, con el MISMO instrumento las dos veces

| | ANTES (tiene que CAER) | DESPUES (tiene que PASAR) | conservacion |
|---|---|---|---|
| el taller | **15 pasan, 33 caen** | **50 pasan, 0 caen** | 5 de 5 |
| la alternancia | **15 pasan, 21 caen** | **38 pasan, 0 caen** | 5 de 5 |

### EL CENSO, tramo a tramo, y **recontado al cierre**

| momento | ficheros | vivos | deprecados |
|---|---:|---:|---:|
| apertura | 3.853 | 3.538 | 315 |
| tras el taller | 3.853 | 3.536 | 317 |
| tras la alternancia | 3.853 | 3.534 | 319 |
| **recontado al cierre** | **3.853** | **3.534** | **319** |

**Exactamente dos vivos menos por fusion y dos deprecados mas, como el encargo exige. Nadie
borrado: los cuatro absorbidos conservan su texto entero.**

---

## 5. `P.10`, TERCERA SALIDA COMPLETA: EL RESTO ENLAZADO

**De los tres pares entre los tres vivos, DOS llegaron solos** (redireccion mas simetrizacion) **y
UNO se escribio**: `reglas_brainstorming` con `construir_sobre_ideas_ajenas`.

**`P.9` cumplido en sus tres obligaciones:** el enlace corre **despues** de las fusiones (las dos ya
commiteadas); los dos extremos **se pasaron por el resolutor antes de escribir** y los dos resuelven
a si mismos, o sea **ninguno nace por alias**; y **se escribieron los DOS extremos de una vez**.

> **LA PRUEBA DE QUE NO SE APOYA EN NADIE: el ciclo posterior trajo `symmetrize_added` VACIO.** Si
> hubiera escrito un solo lado, el paso 5 habria tenido algo que anadir.

**La direccion no se invento.** El motivo del grupo 3 del plan sellado dice que el procedimiento no
se injerta *porque vive en `construir_sobre_ideas_ajenas`, que queda VIVO y enlazado por `P.10`*, y
la condicion de activacion del destino lo cierra: *Durante sesiones de brainstorming o co-creacion
en equipo*. **De la sesion se va a la tecnica.**

---

## 6. `OP-D-04` CERRADA

**El campo `superviviente` QUEDA EN `null`** por la adjudicacion **`a4`**: la operacion produce
**DOS** supervivientes y el esquema tiene **UN** campo. **Es el mismo `null` que `OP-D-03` pero por
el motivo contrario**, y por eso se dice. La nota gana **4.440 caracteres** nombrando los dos
supervivientes con sus dos planes sellados. **Seis guardas verdes**, entre ellas que **el texto
viejo sobrevive LITERAL** y que **se movio UNA sola linea de 71**.

### LA VERIFICACION DE LA PROPIA OPERACION, punto por punto

| punto | como quedo |
|---|---|
| **1**, `Gate 0 verde` | **`GATE 0: OK`, exit 0**, las tres veces. 3.853 compilados, 3.534 activos, 319 deprecados, alcanzabilidad **100 por ciento** |
| **2**, sin congelados que liberar | no aplica, y ya lo decia la propia operacion |
| **3**, dentro del estandar o de la excepcion de clase | **DISCUTIBLE 2, abajo** |
| **4**, recomputo del cierre transitivo (`9.21`) | **CORRIDO**, con el movimiento medido |
| **5**, cada perdida en su bloque | **CORRIDO**: 5 tablas, 31 filas, **0 discrepancias**, varas 1 y 2 CORRIDAS |
| **6**, el acto leido ENTERO | hecho en la vuelta 37, **21 de 21** |

**EL RECOMPUTO, antes contra despues** (`scripts/plan/recomputo_3388.py`):

| | vuelta 37 (antes) | vuelta 39 (despues) |
|---|---:|---:|
| actos | 333 | **333** |
| ABIERTOS | 54 sobre **247** nodos | 54 sobre **243** nodos |
| ABIERTOS por tamano | `7: 2`, `3: 25` | **`7: 1`, `3: 26`** |
| nodos en actos | 845 | **841** |
| `A` vigentes resueltas | 574 | **569** |
| las cuatro comprobaciones | OK | **OK las cuatro** |

> **El acto de siete dejo de existir y en su sitio hay uno de tres**, que son los tres vivos. **Es
> la fusion leida desde el otro lado del instrumento.**

---

## 7. LOS DISCUTIBLES MARCADOS, antes de saber si acierto

**DISCUTIBLE 1. EL RE-ANCLAJE DEL PUENTE.** Sostengo que redirigir el ancla del puente de `quality`
**no es recalcular una decision** sino completar la redireccion que la fusion ya hace, y que hacerlo
con el instrumento de la casa por el resolutor es lo que el precedente triple manda. **Lo discutible
es que el encargo decia *sin recalcular ninguna decision* y el plan sellado no listaba ese
registro.** La alternativa era **PARAR con `Gate 0` en rojo**. Elegi seguir. **Que se me discuta.**

**DISCUTIBLE 2. LOS SIETE PASOS Y LA SENAL QUE DISPARA.** Los dos resultantes quedan en **siete
pasos**, uno por encima del estandar de 3 a 6, y entran por **la excepcion de clase de `OP-F-01`**
(criterio escrito: superar el estandar **sin narracion repetida dentro**), con precedente en
`02_DESTEJIDOS` linea 294 leida hoy. **PERO el instrumento no entrega y UNA senal dispara:**

| nodo | pasos | peor pareja (u. 80) | mejor bloque (u. 44) | dispara |
|---|---:|---:|---:|---|
| `reglas_brainstorming` **antes** | 5 | 54,3 | **47,7** | **BLOQUE** |
| `reglas_brainstorming` **despues** | 7 | 54,3 | **50,6** | **BLOQUE** |
| `pensamiento_convergente_divergente` antes | 4 | 46,2 | 0,0 | ninguna |
| `pensamiento_convergente_divergente` despues | 7 | 48,1 | **43,8** | ninguna |

**Sostengo que la clase cubre a los dos**, porque **la fusion NO enciende la senal: ya disparaba
antes** con 47,7 sobre los cinco pasos viejos (medido contra `git 03e8e0e8`), **la sube y no la
crea**, el corte es el mismo (tras el paso 2), y **el propio instrumento declara que CITA y NO
JUZGA**. **Lo discutible es que un 50,6 sobre umbral 44 se quede sin lectura textual.** **Y el
margen del otro se dice igual: 43,8 contra 44, por dos decimas.**

**DISCUTIBLE 3. LA DIRECCION DE LA ARISTA DE `P.10`.** La escribi `reglas_brainstorming` hacia
`construir_sobre_ideas_ajenas` por el motivo del plan mas la condicion de activacion del destino.
**Lo discutible: los otros dos pares corren al reves** (`construir` hacia `pensamiento`, y
`pensamiento` hacia `reglas`), asi que **mi arista cierra un ciclo dirigido de tres**. No encontre
regla escrita que lo prohiba y `Gate 0` no protesta. **Si la casa prefiere no cerrar ciclos, esta es
la arista que sobra.**

**DISCUTIBLE 4. RE-HICE EL TALLER DESDE CERO PARA NO CITAR UN LOG PISADO.** La primera corrida
necesito **dos** pasadas de `run_phase1` (la segunda tras re-anclar el puente), y **la segunda vacio
`symmetrize_added`**, que es justo lo que la guarda tenia que citar. **Restaure `dataset/`, `packs/`
y `web/lib/assets/` a `HEAD` con `git checkout --` y repeti la fusion en el orden correcto (fundir,
re-anclar, ciclo UNA vez)**, para que el log citado fuera el de verdad y no una reconstruccion. **Lo
discutible es haber descartado escrituras ya hechas.** El estado final es identico y el arbol quedo
limpio; **pero se dice, porque un `git checkout --` sobre `dataset/` no se oculta.**

---

## 8. `OP-D-05` ABIERTA: el acto medido, y sale limpio

**Instrumento nuevo y PARAMETRIZADO**, `scripts/loop/vuelta39_acto.py`, sucesor declarado de
`vuelta37_acto_opd04.py`: aquel traia los siete nodos y las trece dirigidas **dentro del codigo**;
**este lee la nomina de `OPERACIONES.jsonl` por el id** y **aborta si un par se queda sin clase**.

| | `OP-D-05`, medido hoy |
|---|---|
| nodos | **3**, los tres **VIVOS** y **los tres de la misma fuente** (*The Founder's Dilemmas*): **NO es de fuente mixta** |
| pares | **3 de 3 con clase, los tres del ARCHIVO** (puestos **492**, **673**, **833**), **cero lecturas dirigidas** |
| reparto | **A 3, y nada mas** |
| nodos puente (`P.10`) | **CERO** |
| subconjuntos cerrados | **1, y es el acto entero**: UNA familia, no dos |
| aristas cojas | **CERO en los tres**: elegir superviviente **no cuesta ni una arista** |
| `9.3.1` sobre pares A | de 3 pares A, **UNO** nombra ganador (el 673). **No hay GANADOR POR DERECHO**: la especie es **POR ELEGIR**, y la elige `P.8` |
| cableado | `seleccion_ceo_fundador` 4 pasos y **LO NOMBRAN 9**; los otros dos 5 pasos y **LO NOMBRAN 4** cada uno |

**LO QUE FALTA, y por que no se hizo hoy:** la nota de la operacion dice que `P.5` manda leer el
acto entero **DESPUES DE SU DESTEJIDO** y antes de su fusion, **y el destejido no se ha corrido**.
**La lectura de hoy es PREVIA al destejido y se declara como tal: sirve para saber la forma del
acto, NO para autorizar la fusion.** El destejido tiene a quien mirar:
`errores_comunes_asignacion_roles` **dispara la senal de bloque, 45,5 contra 44**, y **la razon del
par 673 ya habla de *la costura del largo***. Los otros dos no disparan (43,6 y 40,6). **Misma
advertencia que en 3.3: esas cifras son senales calculadas aparte, INDICIO y no veredicto.**

---

## 9. EL ESTADO AL CIERRE, RECOMPUTADO AL CIERRE (regla 1)

**Corrida:** `python scripts/loop/vuelta31_estado.py`, salida en `docs/loop/SALIDA_V39_CIERRE.txt`.

| | apertura | **cierre** | movio |
|---|---:|---:|---|
| `n` | 3.388 | **3.388** | no, y no tenia que moverse: esta vuelta **no emitio ni un veredicto** |
| A / B / C / D | 575 / 83 / 8 / 2.722 | **575 / 83 / 8 / 2.722** | no |
| tasa | 17,0 | **17,0** | no |
| ficheros | 3.853 | **3.853** | no, **nadie borrado** |
| vivos | 3.538 | **3.534** | **si, menos 4**: los cuatro absorbidos |
| deprecados | 315 | **319** | **si, mas 4** |
| enlaces | 16.849 | **16.869** | **si, mas 20**, y la aritmetica cuadra sola |
| operaciones | 71 `LISTA`, 0 rotas | **71 `LISTA`, 0 rotas** | no |
| inventario | 672 | **672** | no |

**LA ARITMETICA DE LOS ENLACES, comprobada y no publicada a ojo:** mas 16 de simetrizacion del
taller, mas 4 de la alternancia, mas 2 por la arista de `P.10` escrita en sus dos extremos, menos 1
por la duplicada del taller resuelta y menos 1 por la de la alternancia. **16 mas 4 mas 2 menos 1
menos 1 igual 20, y 16.869 menos 16.849 igual 20.**

**LA TASA POR DOMINIO AL CIERRE** (`scripts/loop/vuelta35_tasa_dominio.py`,
`SALIDA_V39_TASA_DOMINIO.txt`), **impresa y no tecleada**:

```
dominio                   n      A     tasa      B      C      D
core                   1445    336    23.3%     81      8   1020
quality                 844    126    14.9%      0      0    718
health_safety           192     45    23.4%      0      0    147
entrega                 171      2     1.2%      0      0    169
environmental           170     29    17.1%      0      0    141
compras                 155      1     0.6%      2      0    152
franquicias             148     18    12.2%      0      0    130
exportacion             130     15    11.5%      0      0    115
risk_management         106      0     0.0%      0      0    106
seguridad_digital        27      3    11.1%      0      0     24
```

**FIGURAS Y FAMILIAS AL DIA**, del inventario recontado al cierre: **672 entradas**, por tipo
dominio 10, acto 556, racimo 13, familia_de_ids 54, **figura 20**, defecto 19. **Familias de
libro**: Weinberg **72 / 70**, Horowitz **93 / 91**, Hugos **111 / 111**, Coleman **75 / 73**,
Rackham **47 / 47**. **Ninguna se movio, y ninguna tenia que moverse.**

**VARA POR TRAMO:** esta vuelta **no es de cribado y no emitio veredictos**, asi que no hay vara de
tramo que publicar. **Se dice en vez de rellenar la casilla.**

---

## 10. LAS SUITES Y EL CICLO, POR CORRIDA PROPIA

| | tras el taller | tras la alternancia |
|---|---|---|
| `run_phase1 --reaplico-curaduria` | exit 0, **`GATE 0: OK`** | exit 0, **`GATE 0: OK`** |
| `etiquetas_de_cara --aplicar` | **71 etiquetas** | **71 etiquetas** |
| `sync_assets_web` | **seis assets** | **seis assets** |
| motor (`engine/run_all_tests.py`) | **25 de 25**, exit 0 | **25 de 25**, exit 0 |
| web (`pnpm test`) | **80 ficheros, 1.030 pasadas, 3 saltadas**, exit 0 | **80, 1.030, 3**, exit 0 |
| `tsc --noEmit` | **cero lineas**, exit 0 | **cero lineas**, exit 0 |

**Un tercer ciclo** corrio tras el enlace de `P.10`: **`GATE 0: OK`** y **`symmetrize_added` vacio**.

---

## 11. RUTAS TOCADAS Y COMMITS

`git diff --numstat 29a1acf1..HEAD` corrido hoy: **81 ficheros, 5.116 insertadas, 151 borradas.**

| carpeta | ficheros |
|---|---:|
| `docs/loop` | 42 |
| `dataset/nodos` | 25 |
| `scripts/loop` | 7 |
| `docs/plan` | 3 |
| `web/lib/assets` | 2 |
| `packs/quality/metadata` | 1 |
| `dataset/metadata` | 1 |

**Los commits de la vuelta, en orden:** `03e8e0e8` (apertura), `7cb10c63` (tarea 1 y la guarda
previa), `4fd51e4a` (el taller), `d406059c` (la alternancia), `e5f7bdbd` (`OP-D-04` cerrada),
`fc7b0d08` (`OP-D-05` abierta) y **`f070617c`** (este reporte). **El hash de este reporte se
anade DESPUES de commitear, medido con `git log` y no anticipado, que es la unica forma de
citarlo sin inventarlo.**

---

## 12. INSTRUMENTOS NUEVOS, todos con su sucesion declarada dentro del codigo

| instrumento | sucede a | que anade |
|---|---|---|
| `vuelta39_fundir.py` | `vuelta33_fundir.py` | DOS absorbidos, guarda VERBATIM en vez de por prefijo, finales derivados de los grupos, `P.16` medida antes de limpiar, `a6` |
| `vuelta39_caso_positivo.py` | `vuelta33_caso_positivo.py` | dos absorbidos, fuente mixta con la ficha exigida, `preservar` sobre el nodo entero con su sede, etiqueta del arbol, cuarto miembro |
| `vuelta39_guarda_simetrizacion.py` | nuevo | la guarda que el plan de la vuelta 38 dejo escrita, mas la relectura en el fichero |
| `vuelta39_enlazar_p10.py` | nuevo | la tercera salida de `P.10` con `P.9` comprobado antes de escribir |
| `vuelta39_cerrar_opd04.py` | `vuelta36_cerrar_opd03.py` | cierre con DOS supervivientes y `null` por sobra, no por falta |
| `vuelta39_tabla_cierre.py` | nuevo | las cuatro tablas del cierre, impresas y no tecleadas (regla 1) |
| `vuelta39_acto.py` | `vuelta37_acto_opd04.py` | nomina leida de `OPERACIONES.jsonl` en vez de escrita en el codigo |

---

## 13. PENDIENTES DE DOCTRINA Y PENDIENTES

**PENDIENTE DE DOCTRINA 1, NUEVO: NINGUNA REGLA DICE QUE UNA FUSION TENGA QUE MIRAR LOS REGISTROS
QUE NO SON EL GRAFO.** `P.7` simula sobre el grafo; el plan enumero referencias de nodo; el puente
lo cazo `Gate 0` **despues** de escribir. **Lo mejor sostenido y ejecutado hoy: correr
`reanclar_por_resolutor.py` como parte del ciclo de toda fusion, antes de `run_phase1`.** No lo
elevo a regla: **lo registro y sigo**, conforme a la regla 5.

**PENDIENTE 1, NUEVO: `costuras_internas.py` no entrega.** Su fixture `plan_mejora_procesos` da
43,1 contra umbral 44. **No lo arreglo yo** (regla 4: cero reparaciones fuera de encargo) **y no
aflojo el umbral.** Mientras siga asi, **el punto 3 de la verificacion de toda operacion que deje un
nodo por encima del estandar no se puede cerrar con el instrumento de la casa.**

**PENDIENTES HEREDADOS, vivos y ninguno bloquea:** el recomputo no ve las dirigidas; el estado
`HECHA` que no existe en el esquema; el acto que se parte en dos; **el esquema de
`OPERACIONES.jsonl` frente a operaciones con dos supervivientes** (recomendacion del acta, `a4`);
**el titulo del nodo del taller** (recomendacion del acta, `a6`); una linea general de prelacion
para el choque de `a3`; y los pendientes 5 a 9 de la vuelta 36.

---

## 14. PREGUNTAS, lo que no esta escrito y no pude medir

1. **La direccion de la arista de `P.10`, y el ciclo dirigido que cierra.** No hay pagina que diga
   si un ciclo dirigido de tres entre nodos vivos es defecto o es normal. **No lo adivino: lo
   pregunto.**
2. **`OP-D-05` y el orden `destejido` antes de `P.5`.** Su nota lo manda, y su destejido tiene una
   sola cita medida (`errores_comunes_asignacion_roles`, bloque 45,5). **Pregunta: con el
   instrumento de costuras caido, vale la senal calculada aparte como base para destejer, o el
   destejido espera a que el instrumento vuelva?** De la respuesta depende si `OP-D-05` avanza en la
   vuelta 40 o se queda medida.
3. **El re-anclaje de puentes, dentro o fuera del plan sellado.** Si entra en el ciclo, el plan de
   toda fusion futura deberia enumerar tambien los registros que no son el grafo. **Es decision de
   la casa.**
