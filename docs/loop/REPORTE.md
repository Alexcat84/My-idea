# REPORTE DE LA VUELTA 53 (20 ago 2026, ejecutor Opus 5)

**LA TAREA 1 ENTERA, sus CUATRO puntos. Y LA TAREA 2 CIERRA EL TRAMO 1: DOCE ACTOS FUNDIDOS en
tres lotes, UN ACTO MAS DECLARADO, y CERO lecturas `P.12` pendientes. EL HALLAZGO DE LA VUELTA
SALE DE CUMPLIR LA REGLA 9 (toda perdida declarada se re-verifica contra el grafo): el puesto 2488
escribe que el acronimo MBO SOLO APARECE EN EL NODO QUE CAE y el 2477 que el superviviente NO LO
NOMBRA EN NINGUN SITIO. Medido hoy campo por campo sobre los 3.489 nodos vivos, MBO VIVE EN DOS
NODOS, y el segundo es justo el MIXTO que sobrevive a ese acto. La perdida no existe.**

| | |
|---|---|
| **rama** | `pasada-unica` |
| **hash de apertura** | `d88c42bb` (el acta de la vuelta 52), **arbol limpio y todo pusheado** |
| **hash final** | `be5d152b`, **pusheado a `origin/pasada-unica`** |
| **commits de la vuelta** | **5**: `49ae6eef` (TAREA 1), `cadc9977` (lote A), `04bd56de` (lote B), `90bb930c` (lote C) y `be5d152b` (el cierre) |
| **arbol al cierre** | limpio tras el commit del cierre |

---

## 0. LA APERTURA, MEDIDA ANTES DE LA PRIMERA OPERACION (regla 1)

**Corrida ANTES de tocar nada**, con `python scripts/loop/vuelta31_estado.py APERTURA_V53`
([`SALIDA_V53_APERTURA.txt`](SALIDA_V53_APERTURA.txt)) y `python scripts/recomputar_marcador.py
3388` ([`SALIDA_V53_MARCADOR_APERTURA.txt`](SALIDA_V53_MARCADOR_APERTURA.txt)). **El arbol estaba
limpio y todo pusheado en `d88c42bb`, asi que la regla 3 se cumplio por vacio, y se dice asi en
vez de darla por cumplida.**

| | **apertura**, antes de la 1.ª operacion | **cierre, RECOMPUTADO al cierre** |
|---|---:|---:|
| marcador `A` / `B` / `C` / `D` | 563 / 75 / 7 / 2.743 | **551 / 73 / 6 / 2.758** |
| `n`, huecos, duplicados | 3.388 / 0 / 0 | **3.388 / 0 / 0** |
| tasa de `A` | 16,6 | **16,3** |
| grafo: ficheros / vivos / deprecados / enlaces | 3.853 / 3.489 / 364 / 17.011 | **3.853 / 3.477 / 376 / 17.052** |
| retrato: `A` crudas / colapsos / pares distintos | 563 / 60 / 503 | **551 / 72 / 479** |
| operaciones, estados, dependencias rotas | 71, todas `LISTA`, 0 | **71, todas `LISTA`, 0** |
| entradas del inventario | 672 | **672** |
| actos `CERRADOS` / `ABIERTOS` | 244 / 53 | **232 / 53** |
| nodos en `CERRADOS` / `ABIERTOS` | 509 / 240 | **473 / 240** |
| cola de costuras | 1.488 | **1.483** |
| colisiones de clase vigentes | 0 | **0** |
| mixtos del tramo 1 pendientes de `P.12` | 18 | **6, y los SEIS declarados o bloqueados** |
| familias de libro que se mueven | | **una sola, `Coleman`, de 73/71 a 72/70** |

**EL CIERRE ESTA RECOMPUTADO AL CIERRE**, despues del ultimo movimiento
([`SALIDA_V53_CIERRE.txt`](SALIDA_V53_CIERRE.txt),
[`SALIDA_V53_MARCADOR_CIERRE.txt`](SALIDA_V53_MARCADOR_CIERRE.txt),
[`SALIDA_V53_RECOMPUTO_CIERRE.txt`](SALIDA_V53_RECOMPUTO_CIERRE.txt),
[`SALIDA_V53_COLA_CIERRE.txt`](SALIDA_V53_COLA_CIERRE.txt)), **no copiado de la apertura.**

> **LO QUE LA COLUMNA DE APERTURA NO ES, dicho en vez de callado.** Las filas de **marcador,
> grafo, operaciones, inventario y familias** salen de las DOS corridas propias hechas antes de la
> primera operacion. **Las filas de retrato, actos, cola y tramo 1 NO se re-corrieron antes de la
> primera operacion: son las del CIERRE de la vuelta 52** y valen como apertura porque entre aquel
> cierre y mi primera operacion no se movio ningun nodo ni ningun veredicto, **comprobado por las
> dos corridas propias que si se hicieron, que reproducen el cierre de la 52 al digito**
> (563/75/7/2.743 y 3.853/3.489/364/17.011). **Va marcado (`D1`).**

**EL MOVIMIENTO DEL MARCADOR CUADRA AL DIGITO CON LOS QUINCE MOVIMIENTOS:** **menos 12 en `A`**
(los puestos 475, 1175, 559, 1865, 2075, 2090, 2181, 2488, 2551, 2613, 2742 y 1222), **menos 2 en
`B`** (el 204 y el 811), **menos 1 en `C`** (el 360) y **mas 15 en `D`**.

**CUATRO DOMINIOS SE MUEVEN Y SEIS NO:** `core` de 329 a **325**, `quality` de 123 a **119**,
`environmental` de 29 a **28** y `franquicias` de 18 a **15**, que es el que mas se mueve porque
tres de los doce actos son suyos. **Quedan identicos al digito** `health_safety` 43, `exportacion`
15, `entrega` 2, `compras` 1, `risk_management` 0 y `seguridad_digital` 3.

**EL GRAFO GANA 41 ENLACES Y NO LOS PIERDE, y se dice porque es la primera vuelta en que esa fila
se mueve:** la simetrizacion del paso 5 de `run_phase1.py` completo **45 vistas** en las tres
corridas de Gate 0 (7+6, 4+5 y 13+10) al redirigir a los supervivientes las aristas de los doce
nodos que mueren, y `P.16` retiro por su lado duplicadas y dos auto-aristas. **La resta exacta
entre 45 y 41 no la he derivado y no la invento: va como pregunta.**

---

## 1. TAREA 1: LOS CUATRO PUNTOS

**Instrumentos: `scripts/loop/vuelta53_correcciones_tarea1.py` (nueve sustituciones, todas
idempotentes al re-correrlas:
[`SALIDA_V53_CORRECCIONES_T1_IDEMPOTENCIA.txt`](SALIDA_V53_CORRECCIONES_T1_IDEMPOTENCIA.txt)) y
`scripts/loop/vuelta53_marcador_por_git.py`, sucesor declarado que anade las columnas de
porcentaje.**

| | la especie | lo que se toco |
|---|---|---|
| **1.1** | **TABLA VIGENTE MANTENIDA A MEDIAS** | las **tres** filas atrasadas de la **100.2** del `INFORME` (`core` 336, `quality` 126, `health_safety` 45) corregidas con tachado y nota fechada a **329 / 123 / 43**, leidas de mi corrida del dia. **Y LA HERMANDAD CON LA TABLA DEL `RECOMPUTO` ESCRITA EN LAS DOS SEDES** |
| **1.2** | **FOTO FECHADA QUE NO PUBLICA LA CIFRA DE SU CORRIDA** | el **583 / 89 / 7 / 2.709** restituido A LA VISTA en las dos tablas (vueltas 19 y 20) y las **cuatro** cifras del mantenimiento muerto tachadas con nota. **Los cuatro porcentajes de la tabla de la 20 eran los del 575 y se tachan con el**; los del 583 (17,2 / 2,6 / 0,2 / 80,0) salen del instrumento |
| **1.3** | **ROTULO QUE REPITE EL SINTOMA** | los **dos** rotulos del caso `c` de `vuelta48_puertas_en_el_lote.py` (docstring y parentesis del resumen), con el texto viejo delante entero |
| **1.4** | **REGISTROS DE ADJUDICACIONES** | los **tres** carriles del acta 52 escritos en el registro del tramo de `03_FUSIONES.md`: el acto de la sucesion del CEO por **empate sin vara**, el **carril GENERAL de colisiones** en tabla, y el criterio del **mixto contenido** en tabla |

**LOS OTROS SIETE DOMINIOS DE LA 100.2 MEDIAN EXACTOS EN LA APERTURA Y NO SE TOCARON EN LA TAREA
1**, comprobado en la misma salida. **La suma de la columna cuadraba con el marcador de la
apertura**: 329 mas 123 mas 43 mas 2 mas 29 mas 1 mas 18 mas 0 mas 15 mas 3 son **563**.

**LA VERIFICACION POR GIT DE 1.2, RE-CORRIDA HOY**: `python scripts/loop/vuelta53_marcador_por_git.py`
sobre los **once** commits que van del inicio de la vuelta 19 al final de la 21
([`SALIDA_V53_MARCADOR_POR_GIT.txt`](SALIDA_V53_MARCADOR_POR_GIT.txt)): **los once miden `A 583, B
89, C 7, D 2.709` y `17,2 / 2,6 / 0,2 / 80,0 por ciento`, al digito.**

**EL ROTULO REPARADO NO MUEVE LA VARA**, comprobado re-corriendo el instrumento sobre la nomina del
dia ([`SALIDA_V53_PUERTAS_APERTURA.txt`](SALIDA_V53_PUERTAS_APERTURA.txt)): **31 actos con puerta
dentro, 26 salvables, 2 imposibles por nomina, 3 por estructura y 0 sin receta**, exactamente las
mismas cifras que antes de tocarlo.

---

## 2. TAREA 2: EL TRAMO 1 QUEDA CERRADO

### LAS TRECE LECTURAS `P.12` QUE ESPERABAN, LAS TRECE HECHAS

| | |
|---|---:|
| lecturas `P.12` hechas | **13 de 13** |
| de ellas, **FUNDIDAS** | **12** |
| de ellas, **DECLARADAS** | **1** (el mapa de influencia, par mixto en `B`, politica del 604) |
| mixtos del tramo 1 que quedan pendientes de lectura | **CERO** |

**Los seis actos mixtos vivos al cierre son exactamente los que ninguna lectura puede mover**: el
del S&OP (politica del 703), el de la sucesion del CEO (empate sin vara), el del mapa de influencia
(politica del 604, declarado esta vuelta) y **los tres imposibles por puerta**.

### LA GUARDA DE COLISIONES, CUMPLIDA AL DIGITO EN LOS TRES LOTES

| lote | **predicho** antes de tocar un nodo | **medido** sobre el archivo entero tras ejecutar | tras `P.16` |
|---|---:|---:|---:|
| **A** (lienzo, prompts, warrants, huella) | **6**: 4 dentro, 2 fuera | **6, las mismas seis** | **0** |
| **B** (costos, abogado, inadvertida, objetivos) | **4**: 4 dentro, 0 fuera | **4, las mismas cuatro** | **0** |
| **C** (pareto, poka yoke, dmaic, cliente) | **4**: 4 dentro, 0 fuera | **4, las mismas cuatro** | **0** |

**Ninguna colision real fuera de la prediccion. Ninguna guarda en rojo. Ninguna condicion de
parada.**

### LOS DOCE ACTOS, con la vara que eligio al superviviente

| lote | superviviente | absorbe | mixto en `CONTINUA` (su `D` directo) | **que eligio al superviviente** |
|---|---|---|---|---|
| **A** | `value_proposition_canvas` | `customer_profile_value_map` | `customer_profile` (705) | **ALCANCE DEL ROL**: el 705 llama al superviviente EL INSTRUMENTO ENTERO y al mixto EL CIRCULO DE LA DERECHA. **El conteo apuntaba al otro** (5 pasos contra 4, 2 condiciones contra 1) |
| **A** | `ingenieria_de_prompts_efectiva` | `asignacion_persona_ia` | `prompting_por_persona_ia` (1144) | **PADRE DECLARADO**: el 1144 la declara LA ANATOMIA DEL PROMPT y al mixto EL PROCEDIMIENTO DE SU PRIMERA LINEA. Conteos EMPATADOS, cableado al otro |
| **A** | `warrant_pricing_venture_debt` | `warrants_deuda_convertible` | `warrants_financiamiento` (1448) | **ALCANCE DEL ROL**: el entregable del que muere son LOS TERMINOS YA DEFINIDOS, que es LA MECANICA DEL PRECIO y no LA DECISION DE ACEPTAR. **Las condiciones apuntaban al otro** (2 contra 1) |
| **A** | `medir_huella_carbono_corporativa` | `huella_carbono_empresarial` | `definir_limites_huella_carbono` (1855) | **LAS TRES VARAS A FAVOR y ninguna en contra**: 5 pasos contra 4, 3 condiciones contra 2, cableado 4 contra 3 |
| **B** | `estimacion_inversion_inicial_franquiciador` | `cinco_categorias_costos_franquicia` | `costos_preparacion_franquicia` (2092) | **ALCANCE DEL ROL**: el que muere es el presupuesto de las CINCO categorias y el otro viable se llama como UNA de ellas. **El cableado apuntaba al otro** |
| **B** | `eleccion_abogado_franquicias` | `contratar_abogado_especializado_franquicias` | `contratar_abogado_franquicias` (2086) | **PASOS 6 contra 5 y alcance del rol de acuerdo. EL MATERIAL PROPIO APUNTABA AL OTRO** (4 contra 3) |
| **B** | `prevenir_franquicias_inadvertidas` | `estructuras_combinadas_franquicia` | `deteccion_franquicia_inadvertida` (2073) | **TRES VARAS a favor y la cuarta empatada**: condiciones 2 contra 1, cableado 3 contra 1, material propio 3 contra 2 |
| **B** | `eliminar_metas_numericas_gerencia` | `critica_gestion_por_objetivos` | `eliminacion_gestion_por_objetivos_y_numeros` (2534) | **LA UNICA VARA QUE NO EMPATA**: condiciones 2 contra 1. Pasos, cableado y material propio EMPATAN |
| **C** | `analisis_pareto_de_proveedores` | `analisis_pareto` | `principio_pareto` (3087) | **PASOS 5 contra 3, condiciones 2 contra 1 y material propio 2 contra 1. El cableado apuntaba al otro** (4 contra 2) |
| **C** | `error_proofing_servicio` | `mistake_proofing_poka_yoke_2` | `poka_yoke_a_prueba_de_errores` (2931) | **LAS TRES VARAS QUE NO EMPATAN a favor**: 6 pasos contra 4, cableado 4 contra 1, material propio 3 contra 2 |
| **C** | `criterios_seleccion_proyectos_calidad` | `proceso_nominacion_seleccion` | `dmaic_fase_select` (2933) | **ALCANCE DEL ROL** con condiciones y cableado de acuerdo: el que muere es el proceso GENERAL y el otro viable es UNA FASE del mapa DMAIC. **Los pasos apuntaban al otro** (5 contra 4) |
| **C** | `investigar_datos_cliente` | `seguimiento_informacion_cliente` | `personalizacion_investigacion_prospecto` (811) | **EL MARGEN MAS ANCHO DE LA TANDA**: 11 pasos contra 4, cableado 4 contra 2 |

**En los doce muere el CENTRO de la estrella. En SIETE de los doce alguna vara apunta al otro
lado, y en los siete va escrito en el motivo del plan y marcado aqui:** el conteo en el lienzo, el
cableado en los prompts, en los costos de franquicia y en el pareto, las condiciones en los
warrants, el material propio en el abogado y los pasos en el dmaic select.

**Guardas, por acto y en los doce:** miembros vivos y nomina completa, cobertura exacta de indices
sin olvidos, cero repetidos literales, **cero auto-aristas y cero duplicadas NUEVAS**, los cinco
campos que la operacion no redacta intactos, y **los doce absorbidos con su texto INTACTO**. **La
guarda `1B` paso POR VACIO en once y en el doceavo (el dmaic select) NO paso por vacio sino con la
puerta DE SUPERVIVIENTE**: `criterios_seleccion_proyectos_calidad` es puerta y aqui es quien
sobrevive.

### EL CARRIL GENERAL DE COLISIONES, EN SUS DOS FORMAS

**ONCE VOLTEOS POR MAQUINA** (`A` arrastrada contra directo `D`, el unico caso mecanico): 475,
1175, 559, 1865, 2075, 2090, 2181, 2488, 2551, 2613 y 2742. **CUATRO RELECTURAS EN EL MISMO ACTO**
por veredicto del filo:

| par resuelto | del filo | contraste | veredicto de la relectura |
|---|---|---|---|
| `value_map` contra `value_proposition_canvas` | **360 `C` ARRASTRADO** | 250 `D` directo | **CONDICION DE TEXTO.** Las dos razones dicen lo mismo (NIVELES DISTINTOS, SANO contra LA PARTE CONTRA EL TODO) y tras la fusion el paso 3 del superviviente apunta al mapa de valor con MAS letra. **La figura que el `C` congelaba YA esta registrada Y RE-ENCUADRADA** en la seccion 5 del `INFORME`, verificado hoy. **Se mueve el `C`** |
| `venture_debt_terminos_economicos` contra `warrant_pricing_venture_debt` | **204 `B` DIRECTO** | 1521 `D` arrastrado | **CONDICION DE TEXTO.** Su frase EL SEGUNDO NO AGREGA DECISION NUEVA es falsa hoy: el superviviente trae TRES decisiones que el otro no tiene, y el propio contraste las llama PROCEDIMIENTO. **Se mueve el `B`** |
| `investigar_datos_cliente` contra `personalizacion_investigacion_prospecto` | **811 `B` DIRECTO** y **1222 `A` arrastrada** | uno del otro | **CONDICION DE CONTEO, DESCARGADA POR MEDICION.** **SE MUEVEN LOS DOS**, y se dice por que: dejar uno en `B` y el otro en `D` deja la colision viva. La vara la escribe el propio 1222 (*cuando lo compartido es solo por donde se entra, es sano*) |

**LAS CUATRO SALIERON CONDICION DE TEXTO O DE CONTEO Y NINGUNA PREGUNTA DE POLITICA**, y de eso
dependia que los actos se pudieran fundir.

### LOS TRES CHOQUES DE LETRA CONTRA ARITMETICA, EJECUTADOS Y REGISTRADOS

| el acto | lo que la letra nombra | los puestos | que le paso |
|---|---|---|---|
| pareto | `analisis_pareto` | **2546, 2551** | **NO ES VIABLE y MUERE ABSORBIDO** |
| poka yoke | `mistake_proofing_poka_yoke_2` | **2613** | **NO ES VIABLE y MUERE ABSORBIDO** |
| dmaic select | `proceso_nominacion_seleccion` | **2627** | **NO ES VIABLE y MUERE ABSORBIDO** |

> **LO QUE ESTOS TRES TIENEN DE NUEVO, y no es un detalle.** El acta de la vuelta 50 adjudico que
> manda la aritmetica **y escribio que *la letra se honra en lo que puede: X sigue VIVO en los
> cinco casos***. **En estos tres X NO sigue vivo: MUERE**, porque el nodo que la letra nombra es
> el CENTRO de la estrella, que es justo el que la receta no deja sobrevivir. **La adjudicacion se
> cumple en lo que si dice** (nadie funde a X en contra de su par: los pares que lo absorben son
> sus dos `A`), **pero el consuelo que escribia no aplica.** Va marcado (`D3`).

### EL REPARTO, pieza por pieza

| lote | piezas | enteras | de INCISO | ya dichas | perdidas NOMBRADAS |
|---|---:|---:|---:|---:|---:|
| **A** | 28 | 12 | 5 | 11 | **1** (la comparacion entre varias personas, viva entera en el mixto) |
| **B** | 24 | 7 | 1 | 16 | **1** (las referencias a otros franquiciantes, vivas enteras en el mixto) |
| **C** | 33 | 19 | 6 | 8 | **0** |

---

## 3. EL HALLAZGO: UNA PERDIDA QUE DOS VEREDICTOS DAN POR SEGURA Y LA MEDICION DESMIENTE

**La regla 9 del `EJECUTOR` manda re-verificar contra el grafo toda perdida de catalogo declarada,
sin importar quien la declare.** Esta vuelta la cumplio TRES veces
(`scripts/loop/vuelta53_perdidas_verificadas.py`) y una de las tres devolvio lo contrario de lo
escrito:

| busqueda | lo que el archivo decia | **lo que mide el grafo hoy** |
|---|---|---|
| **MBO** | el 2488: *el acronimo MBO solo aparece en el nodo que cae*; el 2477: *el superviviente no nombra el MBO en ningun sitio* | **VIVE EN DOS NODOS VIVOS**: el que muere **y `eliminacion_gestion_por_objetivos_y_numeros`, que es el MIXTO de ese acto y SOBREVIVE**, en su resumen teorico ([`SALIDA_V53_MBO.txt`](SALIDA_V53_MBO.txt)) |
| **PARETO** | (nada escrito) | **CINCO titulos vivos llevan la palabra**, y al morir `analisis_pareto` quedan **CUATRO**, entre ellos el del mixto que sobrevive ([`SALIDA_V53_PARETO.txt`](SALIDA_V53_PARETO.txt)) |
| **la familia Coleman del 811** | *ya lleva cuatro nodos vistos y los pares se contradicen: hay que contarla antes de decidir* | **cobertura 6 de 6, CERO pares pendientes**, y contada no hay contradiccion ([`SALIDA_V53_COLEMAN.txt`](SALIDA_V53_COLEMAN.txt)) |

**LA PERDIDA DE MBO NO EXISTE**, y es la clase **VIVE DENTRO** de `P.13`: era real contra aquel
par y es falsa contra esta nomina. **Se declara la discrepancia en vez de resolverla copiando**
(regla 2), y **las dos razones viejas no se tocan**. **Lo que si se declara como perdida de nombre
es el titulo general sin adjetivo `Analisis de Pareto`**, porque esta operacion no redacta titulos.

---

## 4. EL CASO POSITIVO: LAS CUATRO GUARDAS PUESTAS A FALLAR

**Escrito y corrido ANTES de ejecutar nada** (`scripts/loop/vuelta53_caso_positivo.py`,
[`SALIDA_V53_CASO_POSITIVO.txt`](SALIDA_V53_CASO_POSITIVO.txt)).

| guarda | la mentira que se le puso delante | resultado |
|---|---|---|
| **`1B`** | un plan cuyo absorbido es `domina_lo_que_compras`, que es puerta | **exit 1, `ROJO`, aborta sin escribir** |
| **cobertura** | un plan que se olvida del paso 3 del absorbido | **exit 1, `faltan ['3']`, aborta sin escribir** |
| **INCISO VERBATIM** (NUEVA) | un inciso que es PARAFRASIS y no trozo literal | **exit 1, `NO es trozo verbatim`, aborta sin escribir** |
| **colisiones** | el censo contra una cuenta esperada FALSA de 9 | **`MEDIDA: 0 \| CALZA: NO`** |

**LA CUARTA ES NUEVA Y SE ANADIO POR NECESIDAD**: siete de los doce actos llevan marcas `INCISO`,
y la marca solo es honesta si su primer campo es literal. **Y el caso positivo de la vuelta 52 se
tuvo que reescribir**, porque su plan de mentira usaba `split_igual_vs_desigual`, que aquella
misma vuelta depreco: habria fallado por la guarda equivocada. **Una mentira que falla por el
motivo que no es no prueba la guarda que dice probar.**

---

## 5. EL BARRIDO `9.10` DEL CIERRE, CORRIDO DESPUES DEL ULTIMO MOVIMIENTO

**Con las cifras viejas DE HOY** (`--viejo 563,75,7,2743 --retrato 60,503 --puestos` los quince,
[`SALIDA_V53_BARRIDO_910_CIERRE.txt`](SALIDA_V53_BARRIDO_910_CIERRE.txt)). **VEINTIUNA celdas
corregidas** ([`SALIDA_V53_CORRECCIONES_910.txt`](SALIDA_V53_CORRECCIONES_910.txt), idempotente al
re-correrlo):

| la celda | decia | **medido al cierre** |
|---|---:|---:|
| `RECOMPUTO_3388.md` **246**, `A` crudas **y su contador** | 563, contador NUEVE | **551, contador DIEZ** |
| **247**, colapsos **y su contador** | 60, contador SEIS | **72, contador SIETE** |
| **248**, pares distintos **y su contador** | 503, contador NUEVE | **479, contador DIEZ** |
| **528**, el checkpoint `ii` en sus dos parentesis | 503 igual a 503 | **479 igual a 479, sigue OK** |
| **1069 a 1078**, las CUATRO filas por dominio que se mueven | 329 / 123 / 29 / 18 | **325 / 119 / 28 / 15** |
| **1079**, total de la tabla por dominio | 563 (16,6 %) | **551 (16,3 %)** |
| `INTRA_DOMINIO_INFORME.md` **100.1**, las CUATRO filas | 563 / 75 / 7 / 2.743 | **551 / 73 / 6 / 2.758** |
| **100.2**, las CUATRO filas por dominio **y su nota** | 329 / 123 / 29 / 18 | **325 / 119 / 28 / 15** |

**LAS DOS TABLAS POR DOMINIO SE MOVIERON EN EL MISMO ACTO, QUE ES PARA LO QUE LA HERMANDAD SE
ESCRIBIO EN LA TAREA 1.1.** **Y LOS TRES CONTADORES SE CUADRARON EN EL MISMO ACTO**, que es el
`D7` de la vuelta 50. **La suma de la columna vuelve a cuadrar**, comprobada hoy: 325 mas 119 mas
43 mas 2 mas 28 mas 1 mas 15 mas 0 mas 15 mas 3 son **551**.

---

## 6. GATE 0 Y LAS SUITES

**Corridos tras la TAREA 1, tras cada uno de los tres lotes y otra vez al cierre. Todos exit 0.**

| que | como salio |
|---|---|
| **Gate 0**, ciclo de **TRES** comandos | `run_phase1 --reaplico-curaduria` con **`GATE 0: OK`** las cinco veces; `etiquetas_de_cara --aplicar` con **71** etiquetas; `sync_assets_web` con **6** assets |
| **suite del motor** | **25 de 25**, las cinco veces |
| **suite web** | **80** ficheros, **1.030** pasadas y **3** saltadas |
| `tsc --noEmit` | **CERO** lineas |
| duplicadas / auto-aristas **NUEVAS** | **CERO** y **CERO** en los tres lotes |
| las cuatro comprobaciones de `08_VERIFICACION` | **TODAS OK** al cierre (713 igual a 713; 479 igual a 479) |
| censo de colisiones **al cierre** | **CERO** |
| **hook guardian** | verde en todos los commits |

---

## 7. CORRECCIONES DECLARADAS SOBRE MI PROPIO TRABAJO

1. **MI PRIMERA VERSION DE LOS TRES PLANES NO LLEVABA EL CAMPO `declarados_y_no_fundidos`**, y el
   ejecutor cayo con `KeyError` al imprimir el resumen **despues de haber hecho las cuatro
   simulaciones en verde**. No escribio nada porque corria en modo simular. Corregido en el
   generador y re-simulado antes de ejecutar.
2. **CINCO DE MIS SIETE INCISOS SE LEIAN MAL EN SU PRIMERA VERSION** (*especificando en el los
   jobs*, *en el proceso proceso o producto*, un parentesis colgando detras de un punto, dos sin
   acentos). **Los cace releyendo la salida de la simulacion del generador, que imprime el paso
   resultante entero**, y los corregi antes de sellar los planes. **Es la guarda funcionando, no
   un acierto mio.**
3. **MI PRIMERA VERSION DEL PLAN DEL ACTO 17 DECLARABA UNA PERDIDA DE NOMBRE DEL ACRONIMO MBO
   copiando lo que dicen los puestos 2477 y 2488.** La regla 9 me obligo a medirlo y la medicion
   dijo lo contrario. **Corregido en el plan ANTES de sellarlo**, y la discrepancia declarada.
4. **CUATRO ANCLAS DE MIS INSTRUMENTOS DE CORRECCION APARECIAN DOS O CUATRO VECES** en su fichero
   (la fila de `health_safety` de la 100.2 es literal a la de la 99.2; la ultima fila de un
   registro de tramo es literal en los cuatro registros). **Los instrumentos salieron en ROJO y no
   escribieron nada**, que es lo que se les pide; re-anclados sobre bloques verificados unicos.
5. **Ficheros tocados que el encargo no nombraba, declarados:** `docs/COSTURAS_INTERNAS.jsonl` y
   `docs/COSTURAS_INTERNAS_RESUMEN.md`, `docs/plan/ARISTAS_DUPLICADAS.jsonl`,
   `dataset/metadata/*` y `web/lib/assets/*` (los reescriben los instrumentos y el ciclo de Gate
   0). **Mismo alcance que las vueltas 48 a 52.**

---

## 8. LOS DISCUTIBLES MARCADOS, para la relectura ciega

**Marcados ANTES de saber si acierto. Son ONCE.**

| # | el discutible | por que lo marco |
|---:|---|---|
| **D1** | **La columna de APERTURA de mi tabla mezcla dos corridas**: marcador, grafo, operaciones e inventario son mios y de antes de la primera operacion; **retrato, actos, cola y tramo 1 son del CIERRE de la vuelta 52 y no los re-corri antes de tocar nada.** | La regla 1 dice que la apertura se mide ANTES de la primera operacion. **Lo justifico con que las dos corridas propias reproducen el cierre de la 52 al digito, pero eso es un argumento, no una medicion de esas filas.** Y hay UNA cifra que NO reproduce: las duplicadas tras resolver, que la vuelta 52 publico en **1.000** al cierre y que mi instrumento de fundir midio en **999** antes de tocar un nodo. **No la explico y va aqui** |
| **D2** | **En el acto del PARETO mate `analisis_pareto`**, que es el nodo mas cargado del acto (6 pasos, cableado 9, con alias) y el unico que lleva el nombre general del instrumento, **para que sobreviva `analisis_pareto_de_proveedores`.** | Es el discutible mayor de la tanda. **La receta lo obliga** (el centro no es viable) **y el contenido eligio entre los dos viables, pero el resultado es que un titulo general muere dentro de una especializacion.** Ademas `9.3.1` del banco llama a un nodo que gano todos sus pares **GANADOR POR DERECHO** y dice que *el superviviente esta fijado, es final*: `analisis_pareto` gano 2546 y 2551 y el tercer par no lo incluye. **Lo resolvi con la adjudicacion 2 del acta 50 (la estrella con puntas D funde y el centro muere), que es posterior y especifica, pero la tension con `9.3.1` es real y la traigo** |
| **D3** | **En los tres choques el nodo que la letra nombra MUERE**, y la adjudicacion del acta 50 escribia que *X sigue VIVO en los cinco casos*. | **Ejecute los tres igual, porque la adjudicacion dice que manda la aritmetica y esa parte si aplica.** Pero el consuelo con el que la adjudicacion se sostenia no aplica aqui, y **si el auditor lee que ese consuelo era parte de la vara, los tres actos habria que haberlos declarado en vez de fundirlos** |
| **D4** | **En el acto del ABOGADO elegi `eleccion_abogado_franquicias` aunque el MATERIAL PROPIO apunta al otro** (el 2086 le cuenta CUATRO cosas propias a `contratar_abogado_franquicias` y TRES al elegido). | Me apoye en los pasos (6 contra 5), el cableado, el alias y el alcance del rol. **Pero el acta 51, pregunta 6, dice que el material propio ES el contenido hablando**, y aqui lo puse por debajo del conteo de pasos. **Es el mismo orden que la vuelta 52 uso al reves y le adjudicaron a favor** |
| **D5** | **En el acto de los WARRANTS elegi `warrant_pricing_venture_debt` aunque las CONDICIONES apuntan al otro** (2 contra 1) **y aunque esa eleccion fabrica una colision FUERA del acto que la otra no fabricaba.** | Me apoye en el alcance del rol leido del entregable del nodo que muere. **Elegir la rama que cuesta una relectura mas es defendible y tambien es alcance: un lector puede decir que preferi la lectura que me gustaba y pague el precio** |
| **D6** | **En el acto de la GESTION POR OBJETIVOS decidi con UNA SOLA vara** (condiciones 2 contra 1) **estando pasos, cableado y material propio EMPATADOS.** | **Es exactamente la forma que la vuelta 52 declaro como EMPATE SIN VARA en el acto de la sucesion del CEO**, salvo que alli el cableado tambien empataba y aqui las condiciones no. **Si el auditor lee que una sola vara de conteo no basta, este acto habria que haberlo declarado** |
| **D7** | **En el acto del POKA YOKE meti de `APPEND` el paso 5 del centro (validar el dispositivo antes de escalar) aunque el `D` directo 2931 declara *probarlo en condiciones reales* propio del MIXTO.** | Elegi `APPEND` porque la pieza es un GESTO DISTINTO y porque el solape que fabrica **no es una contradiccion** sino un solape, que es lo que la poda de la fase 04 recoge. **Pero el `D5` de la vuelta 52 se ratifico para no meter en el vivo lo que un `D` declara del otro, y un lector puede leer esto como el mismo caso** |
| **D8** | **En la colision del `811` movi LOS DOS veredictos y no uno.** | El carril dice *la relectura decide CUAL se mueve*, en singular. **Mover uno solo dejaba la colision viva** (`B` contra `D` sigue siendo colision), asi que movi los dos y lo escribi en la razon. **Pero elegir mover dos cuando el carril dice cual es lectura mia** |
| **D9** | **Trate la condicion del `811` como CONDICION DE CONTEO y no como pregunta de POLITICA**, y por eso el acto se fundio. | El carril escrito solo tiene dos casillas: **texto** (se resuelve) o **politica** (se declara). **La del 811 no es ninguna de las dos: es una condicion de COBERTURA que se descarga midiendo.** La descargue y segui. **La casilla nueva la puse yo** |
| **D10** | **Corregi las filas de `environmental` y `franquicias` de las DOS tablas por dominio, que el encargo no nombraba**, y ademas les abri cadena de tachados donde no habia ninguna. | Lo hice porque esta vuelta SI las movio y porque la hermandad que yo mismo acababa de escribir obliga a moverlas juntas. **Pero abrir cadena en una celda que nunca la tuvo es una decision de formato que nadie adjudico** |
| **D11** | **En 1.2 publique los CUATRO PORCENTAJES del 583 en la tabla de la vuelta 20**, que el encargo no pedia: solo mandaba dejar visible el 583 y tachar las cuatro cifras muertas. | Los porcentajes viejos eran los del 575 y dejarlos al lado del 583 publicaba una cifra de una corrida con los porcentajes de otra. **Para no teclearlos escribi un instrumento nuevo. Pero anadir columnas a un instrumento para poder publicar cuatro numeros que el encargo no pedia es alcance** |

---

## 9. PENDIENTES DE DOCTRINA

1. **`9.3.1` (GANADOR POR DERECHO) Y LA RECETA `P.12` SE CONTRADICEN EN LA ESTRELLA CON PUNTAS
   `D`.** El banco dice que un nodo que gano todos sus pares tiene *el superviviente fijado* y que
   *no hay lectura pendiente ni futura que pueda moverlo*; la receta dice que ese mismo nodo no es
   viable porque no deja ningun mixto fuera. **Medido tres veces esta vuelta** (pareto, poka yoke,
   dmaic select). Lo resolvi con la adjudicacion 2 del acta 50, que es posterior y especifica, y
   **lo traigo escrito**.
2. **EL CARRIL DE COLISIONES NO TIENE CASILLA PARA UNA CONDICION DE COBERTURA.** Tiene *texto* y
   *politica*. La del `811` es de CONTEO y se descarga midiendo, no leyendo ni decidiendo en la
   mesa. **Aparecio una vez y se resolvio midiendo** (`D9`).
3. **EL CARRIL DICE *CUAL* SE MUEVE Y A VECES HAY QUE MOVER LOS DOS**, porque dejar clases
   distintas sobre el mismo par resuelto deja la colision viva. **Aparecio una vez** (`D8`).
4. **QUIEN CONTESTA UNA PREGUNTA DE POLITICA DE CATALOGO.** Heredado y sin cambio, y **ahora
   afecta a DOS actos declarados** (el del S&OP por el 703 y el del mapa de influencia por el
   604), los dos con la pregunta escrita por el propio veredicto.
5. **UNA PERDIDA DECLARADA EN UNA RAZON PUBLICADA QUE LA MEDICION DESMIENTE: DONDE SE ESCRIBE.**
   La declare en el plan y en este reporte, y **las dos razones viejas no se tocan**. Ninguna
   pagina dice si ademas hay que adosar la correccion a las razones mismas.
6. **HEREDADOS Y SIN CAMBIO HOY**: el `INCISO` para condiciones **sigue sin existir** en el
   instrumento; el esquema de `OPERACIONES.jsonl` **sigue sin distinguir ejecutada de pendiente**
   (71 en `LISTA`, medido hoy); y el campo `orden` de la fase 03 **sigue sin ser su criterio de
   orden**.

---

## 10. LO QUE ESTA VUELTA NO HIZO, DICHO EN VEZ DE CALLADO

1. **NO ABRIO EL TRAMO 2**, aunque el tramo 1 quedo cerrado y la condicion del encargo se cumplio.
   **No hubo cuerda: la vuelta se fue en la TAREA 1 entera, en trece lecturas `P.12`, doce
   fusiones en tres lotes con sus guardas, cuatro relecturas del filo y el cierre completo con su
   barrido.** **Es el incumplimiento de la vuelta y va el primero.**
2. **NO REPARO LA RECETA** para que sepa que hacer cuando el `GANADOR POR DERECHO` del `9.3.1` es
   el centro no viable de una estrella: eso es doctrina y va al auditor.
3. **NO TOCO LOS CINCO DECLARADOS DE SIEMPRE.** Al cerrar son los actos **2, 8, 9, 10 y 11**,
   leidos de la salida que la celda cita.
4. **NO EJECUTO LAS DOCE ARISTAS** de los `CONTINUA` ni la poda de sus solapes: son de la fase 04
   y quedan **declaradas** con id resuelto (`P.9`).
5. **NO RESOLVIO LAS DUPLICADAS HISTORICAS** (997 grupos al cierre, medidos con
   `scripts/plan/aristas_duplicadas_tras_resolver.py`) ni el alias durmiente `modelo_spin_2`: son
   de `OP-S-12`.
6. **NO REPUSO EL TITULO GENERAL `Analisis de Pareto`**: esta operacion no redacta titulos.
7. **NO MIDIO POR SU CUENTA LAS FILAS DE RETRATO, COLA Y TRAMO 1 DE LA APERTURA** (`D1`).

---

## 11. LAS PREGUNTAS PARA EL AUDITOR

1. **`9.3.1` contra la receta: cuando el GANADOR POR DERECHO es el centro no viable de una
   estrella, quien manda?** (`D2`, pendiente 1.) Esta vuelta mato al ganador por derecho **tres
   veces**. Si la respuesta es `9.3.1`, los tres actos habria que deshacerlos.
2. **El consuelo del acta 50 (*X sigue VIVO*) era parte de la vara o una observacion?** (`D3`.) De
   la respuesta depende si un choque cuyo X MUERE se ejecuta o se declara.
3. **Entre el conteo de pasos y el material propio declarado en las razones, cual va primero?**
   (`D4`.) La vuelta 52 puso el material propio por encima del conteo y le adjudicaron a favor;
   esta vuelta lo puso por debajo en el acto del abogado.
4. **Una sola vara de conteo basta para elegir, o eso es empate sin vara?** (`D6`.) En el acto de
   la gestion por objetivos decidieron las condiciones, 2 contra 1, con todo lo demas empatado.
5. **Una condicion de COBERTURA en un veredicto del filo: que casilla del carril es?** (`D9`,
   pendiente 2.) La descargue midiendo y fundi el acto.
6. **Cuando una colision se resuelve moviendo LOS DOS veredictos, sigue siendo el carril?**
   (`D8`, pendiente 3.)
7. **Una perdida que una razon publicada declara y la medicion desmiente: se adosa la correccion a
   la razon vieja, o basta declararla fuera?** (Pendiente 5.) Hoy esta declarada en el plan y en
   este reporte, y las razones viejas siguen intactas.
8. **Los 41 enlaces que gana el grafo contra las 45 vistas que la simetrizacion completo: de donde
   sale la diferencia?** No la he derivado y no la invento.
