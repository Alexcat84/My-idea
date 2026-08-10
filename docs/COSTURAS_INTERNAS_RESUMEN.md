# Costuras internas: nodos con texto repetido DENTRO de si mismos

**ESTE INSTRUMENTO CITA, NO JUZGA.** Hermano chico de `scripts/gradiente_pares.py`. **Un nodo en esta lista es una cita para leer, no una costura probada.** El veredicto es **lectura textual** del auditor con visto del fundador.

La clase nacio de dos hallazgos del gradiente: `plan_mejora_procesos` (puesto 83) y `economia_circular_como_modelo_de_negocio` (puesto 97). **No son duplicados entre nodos: son un solo nodo al que le sobran pasos.**

## Las dos señales

| señal | que caza | umbral |
|---|---|---:|
| **pareja de pasos** | el paso repetido casi literal (`token_sort_ratio`) | **80** |
| **alineacion de bloques** | la secuencia que vuelve a empezar, y **donde** | **44** |

**Basta con que dispare cualquiera, y se reportan las dos siempre**, como en el hermano mayor: el auditor necesita ver por que entro cada nodo.

### Por que hacen falta las dos, medido

**Con la señal de pareja sola, y en cualquier umbral, la calibracion no entra.** La mejor pareja interna de `plan_mejora_procesos` es **60.0** y la de `economia_circular` **54.7**; bajar el umbral hasta ahi caza **856 nodos, el 24 por ciento del catalogo**.

> **Una baranda que caza lo correcto no es estricta, esta rota.**

El motivo es que esas dos costuras son **parafrasis con cola distinta**, no copias. La señal de bloques las pone en los **puestos 7 y 32 de 567** y **acierta el corte exacto en las dos**.

## La calibracion conocida

**CAZADO** `plan_mejora_procesos`: pareja **60.0**, bloque **56.7** con el corte **tras el paso 10**.

**CAZADO** `economia_circular_como_modelo_de_negocio`: pareja **54.7**, bloque **49.7** con el corte **tras el paso 5**.

## Conteos

**128 nodos** en la cola, sobre 3521 activos.

| dominio | nodos |
|---|---:|
| core | 78 |
| quality | 26 |
| exportacion | 9 |
| seguridad_digital | 5 |
| franquicias | 4 |
| health_safety | 4 |
| environmental | 2 |

## Distribucion, para calibrar

| percentil | mejor pareja interna | alineacion de bloques |
|---|---:|---:|
| p50 | 50.5 | 45.9 |
| p90 | 57.6 | 50.3 |
| p99 | 66.6 | 76.1 |
| maximo | 92.8 | 80.2 |

Nodos evaluados por bloques (6 pasos o mas): **173**.

## La franja 44 a 45: lo que el umbral viejo dejaba fuera

**18 citas** entraron al bajar el umbral de bloque de 45 a 44. **Van juntas aqui a proposito**, para que la lectura del auditor las encuentre sin rastrearlas por la cola.

| # | dominio | nodo | pasos | bloque | corte |
|---:|---|---|---:|---:|---:|
| 1 | core | `preferencia_de_liquidacion` | 8 | 45.0 | 3 |
| 2 | exportacion | `certificado_de_origen_coo` | 6 | 45.0 | 3 |
| 3 | quality | `presentaciones_alta_direccion` | 6 | 45.0 | 3 |
| 4 | core | `brainstorming_divergente` | 8 | 44.8 | 5 |
| 5 | core | `portfolio_management` | 6 | 44.7 | 3 |
| 6 | core | `internal_idea_capture` | 7 | 44.7 | 4 |
| 7 | core | `captura_conocimiento_mercado` | 7 | 44.7 | 4 |
| 8 | core | `lectura_balance_general` | 6 | 44.6 | 3 |
| 9 | exportacion | `evaluacion_preparacion_empresa_exportar` | 6 | 44.6 | 3 |
| 10 | quality | `planificacion_cero_defectos` | 7 | 44.5 | 4 |
| 11 | exportacion | `negociacion_acuerdo_representante_extranjero` | 8 | 44.4 | 4 |
| 12 | core | `sem_estrategia_ejecucion` | 8 | 44.3 | 5 |
| 13 | core | `product_market_fit` | 6 | 44.2 | 3 |
| 14 | core | `producto_unico_superior` | 8 | 44.2 | 3 |
| 15 | franquicias | `ferias_comerciales_franquicia` | 6 | 44.2 | 3 |
| 16 | core | `revisiones_regulares_desempeno_ceo` | 10 | 44.2 | 5 |
| 17 | core | `propuesta_gasto_capital` | 12 | 44.1 | 5 |
| 18 | core | `optimizacion_embudo_get_customers` | 10 | 44.1 | 6 |

**El motivo del cambio fue un FALSO NEGATIVO medido**: `nucleo/propuesta_gasto_capital`, con costura confirmada por lectura, quedaba fuera por **0,9 puntos** (bloque 44,1). **La señal si lo habia visto**: su corte propuesto es tras el paso 5, exactamente donde la lectura encontro la costura.

## EL LIMITE DECLARADO, que bajar el umbral NO cierra

**Bajar el umbral recupera a ESE falso negativo. No cierra el mecanismo que lo produjo.**

> **Un comparador de tokens no ve equivalencias semanticas, a ningun umbral.** En el nodo recuperado, el paso 3 dice *"calcular NPV usando el hurdle rate"* y el 11 dice *"calcular el valor presente neto (VPN)"*. **Son la misma cosa con la sigla en dos idiomas, y para este instrumento se parecen un 46,2.**

**Las redes que quedan debajo, y por eso el limite se declara en vez de taparse:**

| red | que caza que este instrumento no |
|---|---|
| **(a) los rebotes del gradiente** | ya cazaron **cuatro** costuras sin buscarlas, leyendo pares por otra razon |
| **(b) el barrido semantico intra-dominio** del final | los embeddings **si** ven que `NPV` y `VPN` viven juntos |
| **(c) la pasada unica** | relee **entero** cada nodo que toca antes de destejerlo |

> **Ninguna cola sustituye a leer el nodo.** Este instrumento ordena la lectura; no la reemplaza.

## Los veinte primeros

| # | dominio | nodo | pasos | pareja | bloque | corte | entro por |
|---:|---|---|---:|---:|---:|---:|---|
| 1 | core | `coeficiente_viral` | 16 | 92.8 | 74.7 | 11 | pareja y bloque |
| 2 | core | `viral_loop_marketing` | 30 | 89.9 | 65.9 | 17 | pareja y bloque |
| 3 | quality | `diseno_de_procesos_por_caracteristicas` | 5 | 86.6 | 0.0 |  | pareja |
| 4 | core | `ratios_eficiencia_inventario` | 8 | 85.1 | 48.3 | 4 | pareja y bloque |
| 5 | core | `producto_minimo_viable` | 22 | 85.0 | 80.2 | 18 | pareja y bloque |
| 6 | quality | `tipos_innovacion_i_ii` | 6 | 84.1 | 0.0 |  | pareja |
| 7 | core | `dso_dpo_gestion_capital_trabajo` | 4 | 81.5 | 0.0 |  | pareja |
| 8 | quality | `control_estadistico_metodo_medicion` | 6 | 80.9 | 0.0 |  | pareja |
| 9 | core | `decision_de_vender_startup` | 34 | 79.2 | 69.3 | 30 | bloque |
| 10 | core | `transicion_producto_a_experiencia` | 12 | 71.0 | 60.1 | 7 | bloque |
| 11 | core | `lienzo_modelo_negocio` | 17 | 66.0 | 59.2 | 13 | bloque |
| 12 | core | `cultura_de_experiencia` | 12 | 65.8 | 50.2 | 5 | bloque |
| 13 | quality | `estratificacion_datos` | 7 | 63.6 | 48.2 | 4 | bloque |
| 14 | quality | `viaje_diagnostico_remedial` | 8 | 63.5 | 46.7 | 4 | bloque |
| 15 | quality | `planificacion_recoleccion_datos` | 16 | 63.4 | 52.3 | 11 | bloque |
| 16 | core | `gestion_libro_abierto_obm` | 10 | 63.2 | 45.1 | 4 | bloque |
| 17 | core | `portfolio_management` | 6 | 62.1 | 44.7 | 3 | bloque |
| 18 | seguridad_digital | `csf_funcion_govern` | 7 | 62.0 | 48.5 | 3 | bloque |
| 19 | core | `analisis_tco_roi_b2b` | 9 | 61.9 | 48.9 | 6 | bloque |
| 20 | core | `plan_gestion_riesgos` | 6 | 61.9 | 50.3 | 3 | bloque |

La cola completa, con los dos pasos de cada pareja, en `COSTURAS_INTERNAS.jsonl`.

---

<!-- MANUAL -->

# INFORME DE CIERRE DEL INSTRUMENTO

**TODO LO QUE SIGUE A LA MARCA `<!-- MANUAL -->` LO CONSERVA EL SCRIPT.**
`scripts/costuras_internas.py` regenera lo de arriba y **copia esta cola tal cual**
en cada regeneracion. La marca y el codigo que la respeta se anadieron el 11 ago
2026, la misma solucion que ya lleva `scripts/intra_dominio.py`.

**Cerrado el 11 ago 2026. Toda cifra de este informe esta RECOMPUTADA del archivo**
cruzando `docs/COSTURAS_INTERNAS.jsonl` con los veredictos escritos en
`docs/FICHA_SUBFUSION_GRADIENTE.md`.

> **LA COLA CIERRA: 128 citas, 128 veredictos propios.** Ninguno heredado de otro
> informe, ninguno pendiente. **Veintidos tandas.**

---

## 1. LAS CIFRAS FINALES

| | |
|---|---:|
| citas del instrumento | **128** |
| **costuras CONFIRMADAS** | **46** |
| citas FALSAS | **82** |
| **precision de la cola** | **36%** |

**La serie de la precision, tanda a tanda**: 73% con 22 leidas, 68% con 28, 65%
con 34, 65% con 40, 61% con 46, 56% con 52, 53% con 58, 53% con 64, 54% con 70,
57% con 76, 55% con 82, 51% con 88, 48% con 94, 48% con 95, 46% con 101, 45% con
102, 43% con 108, 40% con 114, 38% con 121 y **36% con 128**.

> **La precision baja de forma monotona desde la tanda 3 y eso NO es que el
> instrumento se degrade: es el orden de lectura.** La cola se leyo de mayor a
> menor senal, asi que lo bueno salio primero. **Un instrumento que ordena bien
> tiene que terminar con la precision cayendo.**

### Las 46 confirmadas, por forma

| forma | ejemplares | que le pasa al nodo |
|---|---:|---|
| **LA FORMA QUE PARTE** | **8** | un nodo lleva **dos temas**; la cirugia **separa** en dos nodos |
| **LA FORMA REPARTIDA** | **1** | un tema vive **partido en dos nodos**; la cirugia **reune** |
| **el resto** | **37** | **narraciones repetidas del mismo tema**; la cirugia **poda** |

> **La forma repartida es el espejo de la que parte, y nacio de una correccion
> mia**: el encargo daba por repetido el Bullseye en dos nodos y al verificarlo
> contra el grafo **cada nodo llevaba una mitad distinta**. **Cambiar el verbo,
> de podar a reunir, cambia la operacion entera.**

### Las 82 falsas, por clase

| clase | citas | por que no es costura |
|---|---:|---|
| **FALSO POSITIVO DE SECUENCIA LEGITIMA** | **74** | un procedimiento largo **que no se puede acortar ni reordenar**: cada paso necesita al anterior |
| **LARGO LEGITIMO** | **7** | checklists que el estandar de 3 a 6 pasos no contempla, y que **no estan repetidos: estan completos** |
| **DUO LEGITIMO** | **1** | **dos fuentes en secuencia temporal que no se solapan** |

> **LOS SIETE DEL LARGO LEGITIMO NO SE ARREGLAN UNO A UNO: son DECISION DE
> FUENTE.** Cuatro de los siete son formatos-lista del *Basic Guide*; el resto
> sale del mismo molde. **No se decide nodo por nodo si el checklist se parte: se
> decide una vez por libro y se aplica a todos sus nodos.**

---

## 2. LA HERENCIA PRINCIPAL: EL PREDICTOR DE FUENTES

**Es lo mas util que deja esta campana, y llego por un camino que no era el
previsto.**

| | citas leidas | confirmadas | tasa |
|---|---:|---:|---:|
| **nodos de DOS o mas libros** | **47** | **43** | **91%** |
| **nodos de UN solo libro** | **81** | **3** | **4%** |
| | **128** | **46** | 36% |

> **Veintitres veces mas probable.** Un nodo que declara dos libros confirma nueve
> de cada diez veces; uno que declara uno solo, cuatro de cada cien.
>
> **Y el reparto de la cola no explica el resultado**: 47 contra 81 no es un
> efecto de muestra pequena en ninguno de los dos lados.

**La racha final lo dice sin estadistica: CUARENTA Y CINCO citas de un solo libro
leidas seguidas, de la tanda 15 a la 22, sin UNA SOLA costura.** Las tres
confirmadas de un solo libro son todas anteriores a la tanda 15.

> **EL INSTRUMENTO SE CONSTRUYO SOBRE DOS SENALES DE TEXTO, el bloque y la
> pareja, y las dos resultaron ruidosas. La senal que si separa no estaba en el
> texto: estaba en el campo `fuente`, que nadie habia mirado.**

### LA SALVEDAD, y sin ella el predictor se usa mal

> **El campo `fuente` tiene ruido medido, y esta medido en otra ficha**
> (`campos-sucios-dataset`, en `docs/PENDIENTES.md`): **1.314 nodos del catalogo,
> el 34,3%, declaran una fuente que no es el titulo de la obra** sino un nombre de
> archivo truncado o un codigo de documento. **Y once obras aparecen con dos o
> tres grafias distintas.**
>
> Ademas hay ruido de contenido: **`gestion_libro_abierto_obm` declara un libro
> cuyo material no aparece en ningun paso.**
>
> **El predictor es bueno y su base NO esta auditada.** Auditarla es del barrido.

### LA REGLA DE USO, que es la que impide el mal uso

> **EL PREDICTOR ORDENA LA LECTURA. NO DICTA EL VEREDICTO.**
>
> **Probado en los dos sentidos dentro de esta misma campana**:
> `manejo_empleados_en_adquisicion` declara dos libros, entro alto en la cola por
> eso, **y salio FALSA**. La senal acerto al ponerlo arriba; **el veredicto siguio
> siendo de la lectura**, como en las 128.
>
> **Lo que el predictor sirve para hacer**: decidir por donde empezar cuando hay
> mas cola que tiempo. **Lo que no sirve para hacer**: cerrar un nodo sin abrirlo.

### EL PUNTO CIEGO DEL INSTRUMENTO, declarado el 11 ago 2026

**Se anade a la herencia y NO toca ninguna cifra: las 128 siguen siendo 128 y el
cierre sigue cerrado.** Lo que se declara es **un limite del instrumento**, que
es informacion sobre lo que midio, no una medicion nueva.

> **LAS DOS SENALES MIDEN REPETICION. Un nodo que lleva DOS TEMAS PEGADOS SIN
> REPETIR NADA no dispara ninguna de las dos.**

**El ejemplar es `core/retention_metrics`**, hallado **despues del cierre** y por
el otro eje, en el puesto 522 del cribado intra-dominio. **Nueve pasos, dos
fuentes**, y el corte se ve en el vocabulario: del 1 al 5 se mide **lo que el
cliente hace**, del 6 al 9 **lo que el cliente cuesta**, con su propia jerga de
CAC, punto de equilibrio e impacto financiero. **Ninguno de los nueve pasos
repite a otro**, y por eso la cola no lo tenia.

> **Es LA FORMA QUE PARTE en estado puro.** Los ocho ejemplares que si entraron
> disparaban porque **ademas** repetian algo. **Esta es la forma sin su
> acompanamiento, y es invisible para este instrumento.**
>
> **LA RED QUE LO CUBRE ES EL EJE INTRA-DOMINIO, y lo cubre DE REBOTE**: un nodo
> con dos temas **se parece a los vecinos de cada uno de los dos**, asi que entra
> en la cola del otro eje por partida doble aunque no repita nada por dentro.
>
> **Los dos instrumentos no se solapan: se tapan los agujeros.** El de costuras
> mira dentro del nodo; el intra mira entre nodos; **y la forma que parte pura
> solo se ve desde fuera.**

**Lo que aparezca por esta via se anota en `COSTURAS FUERA DE COLA`**, en
`docs/FICHA_SUBFUSION_GRADIENTE.md`, **no aqui**: este informe dice lo que el
instrumento vio.

---

## 3. LAS REGLAS DE CORTE, con sus cifras finales

**El `corte` es donde el instrumento cree que empieza la segunda narracion. Se
midio si predice, y la respuesta es que no.**

| regla | cifra final | veredicto |
|---|---|---|
| **el corte 3 NO es evidencia** | **53 citas de corte 3, 4 confirmadas** | Cuarenta y nueve cayeron al abrir los pasos. **Un corte bajo es lo normal en un procedimiento corto.** |
| **la pareja como senal UNICA no cazo nada** | **4 citas de solo pareja, 0 confirmadas** | El eje de pareja sin el de bloque **no encontro ni una costura en toda la campana** |
| **corte 8 o mas predice costura, SALVO formato lista** | se cumple con la salvedad | La rompio `elementos_plan_exportacion_ejemplo`, corte 10 y FALSA, que es un formato lista |
| **mirar la pareja dentro del corte 3 no ayuda** | la pareja mas alta de ese grupo es de una FALSA | **La regla que se quiso escribir no se sostuvo con los datos** |

> **LO QUE EL EJE DE PAREJA SI ENSENA, y salio en la ultima tanda**: sus tres
> citas mas altas que no son copia **son las tres SIMETRIA DELIBERADA**, la
> comprobacion en los dos sentidos, los dos polos de una tecnica, el cruce
> completo de un estudio de medicion. **En su extremo superior, el eje de pareja
> caza al que escribe bien.**

> **PRECISION SOBRE EL CAMPO `pareja`, verificada en las 128 entradas**: son **dos
> indices de pasos DEL MISMO NODO**, no dos nodos. **Las dos senales del
> instrumento son internas las dos**, y por eso el cribado intra-dominio es otro
> eje y no un solapamiento.

---

## 4. LA ASIMETRIA NUCLEO-MUNDOS, final

| | |
|---|---:|
| confirmadas en nodos del **NUCLEO** | **45** |
| confirmadas en nodos de **MUNDO** | **1** |
| | **46** |

**La unica excepcion es `quality/planificacion_recoleccion_datos`.**

> **Cuarenta y cinco de cuarenta y seis.** La costura interna es **un fenomeno del
> nucleo**, y eso encaja con la vara del gradiente: **el nucleo se escribio
> primero, con mas fuentes y mas pasadas, y ahi es donde se apilaron las
> narraciones.**

---

## 5. LOS RACIMOS COSTURADOS TRANSVERSALES

**Dos racimos donde la costura interna y la duplicacion entre nodos son el mismo
problema, y por eso se destejen juntos.**

### Numero 1: la familia de la EXPERIENCIA del cliente

**Cinco vertices: tres costurados y dos sanos que son DESTINO del material que
sobra.** El destejido de los tres reparte hacia los dos, en vez de podar y tirar.

> **Y tiene un quinto vertice que hay que fabricar**: el destejido conjunto tiene
> que mirar a `fase_affirm_buyers_remorse` como destino aunque hoy no exista con
> ese contenido.

### Numero 2: el BULLSEYE partido en dos

**Es el ejemplar unico de LA FORMA REPARTIDA**, y su regla no es *decidir cual es
la copia* sino **decidir donde vive el original**.

---

## 6. LOS PATRONES DE FUENTE

**Tres decisiones de fuente en la pasada unica, en vez de dieciocho arreglos de
nodo. Es la misma economia de la mesa de racimos.**

| patron | como se manifiesta | nodos |
|---|---|---:|
| **los formatos lista del `Basic Guide` y de Juran** | checklists largos que el estandar de 3 a 6 pasos no contempla, y que salen **FALSOS** | 4 de los 7 LARGO LEGITIMO |
| **la tanda de Mollick** | el metodo de taller rehecho con IA como segundo bloque, **CONFIRMADO** las tres veces | 3 |
| **el pegado de Hugos** | material de cadena de suministro adosado a nodos de otro tema, **CONFIRMADO** | 11 de las 46 |

> **El de Mollick sale mas raro de lo que parece, y la medicion lo agrava**: **51
> nodos declaran a Mollick y 48 son de tema IA por su propio id.** O sea que la
> tanda entro **dos veces y de dos maneras**: como familia propia de 48 nodos, que
> es lo correcto, **y ademas como injerto en 3 nodos de taller que ya existian**.
> **El material de IA ya tenia adonde ir: los injertos no se hicieron por falta de
> sitio.**

---

## 7. EL ESTADO, dicho sin adorno

> **NADA ESTA REPARADO. NINGUN NODO SE TOCO EN TODA LA CAMPANA.**
>
> **Las 46 costuras confirmadas, las 8 de la forma que parte, la repartida, los
> dos racimos transversales y los tres patrones de fuente PASAN ENTEROS AL PLAN DE
> LA PASADA UNICA.** Este instrumento **citaba y medía**; **no arregla.**

**Lo que el plan de la pasada unica recibe de aqui, en orden de coste:**

1. **Tres decisiones de fuente** que cubren dieciocho nodos.
2. **Dos racimos transversales** que se destejen juntos, con reparto en vez de poda.
3. **Nueve cirugias de forma**: ocho que parten, una que reune.
4. **Treinta y siete podas** de narracion repetida, la primera de ellas
   `producto_minimo_viable`, elegida **no por ser la mayor sino por ser la mas
   barata**: su material sobrante ya esta localizado paso por paso, asi que el
   destejido deja de ser un juicio y pasa a ser una lista de borrados.

> **Y la deuda que este informe deja abierta y no cierra**: **auditar el campo
> `fuente`** antes de fiarse del predictor para nada que no sea ordenar una cola.
