# -*- coding: utf-8 -*-
"""_v70_texto_lote_f.py . EL TEXTO EDITORIAL DEL REGISTRO DEL LOTE F.

NO ES UN INSTRUMENTO: es el texto. La maquina que lo arma, lo coteja y lo adosa
es scripts/loop/vuelta70_registro_lote_f.py, que lo importa. Mismo reparto que
_v66_texto..., _v67_texto..., _v68_texto_lote_d.py y _v69_texto_lote_e.py.

NI UNA CIFRA TECLEADA Y NI UN NUMERO DE LINEA TECLEADO: las cifras entran como
%(clave)s y salen de una salida de esta vuelta leida por expresion regular; las
citas de linea entran como [[CLAVE]] y salen de buscar su aguja de contenido.
Las tablas entran armadas del PLAN SELLADO o recortadas de la salida del
tallador.
"""

TEXTO = """

---

## `OP-U-02, TRAMO UNICO: EL REGISTRO DEL LOTE F` (2026-08-26, vuelta 70)

**Se cuelga de la cabecera de tramo que la vuelta 65 adoso** (linea **[[PAG_TRAMO_CABECERA]]**,
derivada hoy por aguja) **y se adosa al final del documento sin reescribir ni una linea de arriba.**
El lote `C` esta en la **[[PAG_LOTE_C]]**, el `D` en la **[[PAG_LOTE_D]]** y el `E` en la
**[[PAG_LOTE_E]]**.

**EL LOTE ABRE EN EL `ACTO 32` Y EL SALTO DEL `31` VA DECLARADO CON SU CITA**, que es lo que la
adjudicacion 2 del acta 69 manda (registrada en esta misma pagina, linea **[[PAG_ADJ_ACTO31]]**): el
`acto 31` **TIENE DUENO MEDIDO** (`OP-F-04-WEI` y `OP-S-04`) y **NO es una fusion de `OP-U-02`**, asi
que **no esta en la cola de fusiones de esta operacion** y saltarlo **no rompe el prefijo sin
saltos**. Su destino queda **con sus duenos en sus fases**.

**SE DECLARARON CINCO ACTOS Y 15 NODOS, Y SE ENTREGARON LOS CINCO.** **LOS CINCO CIERRAN FUNDIDOS Y
NINGUNO CIERRA `DECLARADO Y NO FUNDIDO`: ES EL PRIMER LOTE DEL TRAMO SIN NINGUN DECLARADO**, y no es
una sorpresa sino lo que la adjudicacion 4 del acta 69 anticipo (linea **[[PAG_ADJ_SIN_PUENTES]]**).

| acto | miembros | cierra | **FORMA medida** | superviviente |
|---:|---:|---|---|---|
| **32** | 3 | **FUNDIDO** | `CONTENIDO EMPATA` | `atacar_mercados_establecidos_con_problema` |
| **33** | 3 | **FUNDIDO** | `UNA SOLA VARA` | `wallas_intimacion_fringe_consciousness` |
| **34** | 3 | **FUNDIDO** | `TODAS DE ACUERDO` | `ciclo_de_culpa_2` |
| **35** | 3 | **FUNDIDO** | `CHOCAN` | `construccion_tribu_de_marca` |
| **36** | 3 | **FUNDIDO** | `CHOCAN` | `plan_de_control` |

**EL TOPE DEL PREFIJO ES ESTRUCTURAL Y SE DICE:** el siguiente es el **`acto 37`**, que **TIENE
DUENO** (`OP-S-07`), y sobre el la misma adjudicacion 2 dice con todas sus letras que vale lo mismo
que para el `31`. **El `acto 37` se leyo entero igual** (esta en el dossier y en las varas de esta
vuelta), por el carril del `D16` del acta 68: **la letra prohibe FUNDIR un acto con dueno, no
leerlo**.

**LOS CUATRO MOTIVOS SELLADOS DEL `DECLARADO Y NO FUNDIDO`, RECORRIDOS UNO A UNO SOBRE ESTE LOTE**,
porque un motivo que no se usa se cuenta como usado si nadie lo dice:

| motivo sellado | sobre este lote |
|---|---|
| el triangulo de `P.10` (linea **[[PAG_ACTO1_P10]]**) | **SIN SUJETO**: **%(actos_sin_puente)s de %(actos_mirados)s** actos del resto del tramo sin ningun nodo puente, medido |
| la guarda `1B` con DOS o mas puertas (linea **[[PAG_GUARDA_1B]]**) | **PASA POR VACIO en los cinco**: **CERO** puertas dentro de cada acto, medido contra el universo protegido de **256** ids |
| la respuesta *DOS FAMILIAS* de `P.5` (linea **[[PAG_P5_MOTIVO]]**) | **NO SE USO**: los cinco contestaron **UNA familia** |
| el `D` directo interno (linea **[[PAG_CUARTO_MOTIVO]]**) | **SIN SUJETO**: **CERO** pares `D` internos en los cinco y en todo lo que queda del tramo, medido |

### a) **EL `ACTO 32`: LA BUSQUEDA DE PROBLEMAS GRANDES, Y LA PRIMERA VEZ DEL TRAMO QUE EL CABLEADO DECIDE SOLO CON MARGEN DE UNO**

**Tres miembros del mismo libro** (*Winning at New Products*, de Cooper), **dos pares internos con
veredicto y los dos en `A`** (**908** y **1507**), **cero `D`, cero puentes, cero triangulos y cero
puertas.** El **1507** declara que **la familia pasa a TRES nodos por cierre transitivo**, con
cobertura de 2 de 3.

**LA FORMA ES `CONTENIDO EMPATA`** (los tres empatan en 4 pasos y en 2 condiciones), **asi que EL
CABLEADO DECIDE SOLO**, que es el unico supuesto en que `P.8` le da la palabra. **Apunta a
`atacar_mercados_establecidos_con_problema` con 3 contra 2 y 2: MARGEN DE UNO, el mas estrecho con el
que este tramo ha elegido superviviente por cableado.** Va marcado discutible en el reporte.

**El nodo crece de %(p32a)s pasos a %(p32b)s y de %(c32a)s condiciones a %(c32b)s.**

**EL `INCISO` AL PASO 1 ES LA PIEZA QUE LA RAZON MANDA SALVAR**, y esto no es lectura del ejecutor: el
**908** dice que la unica diferencia entre los dos nodos es **donde mirar**, que esa diferencia **no
es contradiccion sino cobertura**, y que **es justo lo que hay que salvar en la fusion**, o sea que
**el nodo superviviente tiene que decir que la busqueda vale en los dos sitios**. **Un `APPEND` lo
habria puesto de paso 5**, despues de la validacion economica; **el `INCISO` lo deja dentro del paso
donde se elige el coto.**

**EL REPARTO, PIEZA POR PIEZA, GENERADO DEL PLAN SELLADO:**

%(rep32)s

**LAS PIEZAS POR ABSORBIDO:**

%(abs32)s

**LAS PERDIDAS SELLADAS EN CAMPO PROPIO, recortadas de la salida del tallador:**

%(per32)s

### b) **EL `ACTO 33`: LA CONCIENCIA PERIFERICA, Y EL CHOQUE MAS ANCHO DEL LOTE ENTRE EL CONTENIDO Y EL CABLEADO**

**Tres miembros del mismo libro** (*The Art of Thought*, de Wallas), **dos pares internos con
veredicto y los dos en `A`** (**403** y **1510**), **cero `D`, cero puentes, cero triangulos y cero
puertas.**

**EL SUPERVIVIENTE LO DECLARA UNA RAZON, Y ESO ES LO PRIMERO QUE MANDA.** El **403** trae una linea
rotulada *DATO QUE DECIDE CUAL SOBREVIVE*, verificada contra el grafo por su autor y anticipada en el
puesto **279**: **la madre `wallas_etapa_iluminacion` tiene arista con
`wallas_intimacion_fringe_consciousness` y NO la tiene con `intimation_illumination`**, y el que no la
tiene **es el gemelo sin casa**.

**LA VARA DE CONTENIDO DICE LO MISMO QUE LA RAZON:** la forma es `UNA SOLA VARA`, la de **pasos**
apunta al superviviente (4 contra 3 y 3) y la de condiciones empata. **UNA SOLA VARA DE CONTENIDO NO
EMPATADA BASTA** (acta 53, pregunta 4).

> **Y EL CHOQUE VA ENTERO EN VEZ DE MEDIO, PORQUE ES EL MAS FUERTE DEL LOTE: EL CABLEADO APUNTA AL
> OTRO LADO CON 9 CONTRA 4 Y 3.** `intimation_illumination` tiene **seis siguientes y tres previos**,
> asi que fundirlo obliga a redirigir nueve referencias. **La letra de `P.8` es explicita en que el
> cableado solo habla A CONTENIDO EMPATADO**, y aqui el contenido no empata. **Va marcado discutible
> en el reporte con su cifra al lado.**

**El nodo crece de %(p33a)s pasos a %(p33b)s y de %(c33a)s condiciones a %(c33b)s**, y es el unico
acto del lote que triplica sus condiciones: entraba con **UNA**.

**CERO `INCISO` EN ESTE ACTO, Y ES POR LA PUNTUACION** (carril del `D5` del acta 66): **los cuatro
pasos del superviviente terminan en punto**, asi que cualquier `INCISO` con nexo de coma caeria en la
guarda de la **JUNTURA ROTA**. **No se forzo ninguno.**

**EL UNICO `APPEND` DE PASO ES EL QUE LA RAZON MANDA CONSERVAR Y ADEMAS EXPLICAR:** *practicar la
inhibicion de la tendencia natural a enfocar de inmediato cualquier estimulo interesante*. El **1510**
la llama **la unica instruccion del catalogo que pide NO prestar atencion a proposito**, y avisa de
que esta **EN TENSION** con los pasos 2 y 3 del superviviente, que piden lo contrario. **La razon pide
conservar las dos y decir cual es el disparador de cada una: las dos quedan conservadas, y REDACTAR
el disparador de cada una queda enrutado a la fase 04**, porque redactar no es repartir.

%(rep33)s

%(abs33)s

%(per33)s

### c) **EL `ACTO 34`: EL CICLO DE CULPA, DOS RAZONES QUE CORONAN SUPERVIVIENTES DISTINTOS, Y UNA ENTRADA DE INVENTARIO QUE SE DECLARA EN VEZ DE CALLARSE**

**Es el acto mas discutible del lote y por eso su ficha es la mas larga.** Tres miembros del mismo
libro (*Managing the Risks of Organizational Accidents*, de Reason), **dos pares internos con
veredicto y los dos en `A`** (**2233** y **2272**), **cero `D`, cero puentes, cero triangulos y cero
puertas.**

**EL NUCLEO COMPARTIDO ESTA DECLARADO POR LAS DOS RAZONES:** los **cuatro** pasos de `ciclo_de_culpa`
estan **dentro** de los otros dos, uno por uno y con el paso receptor nombrado en cada caso. **Un nodo
que cabe entero dentro de los otros dos es la bisagra que hace de esto UNA familia.**

> **LO QUE HACE DE ESTE ACTO EL MAS DISCUTIBLE, DICHO ENTERO: LAS DOS RAZONES CORONAN SUPERVIVIENTES
> DISTINTOS.** El **2233** cierra con *sobrevive `dysfunctional_organizational_culture_patterns`* y el
> **2272** con *sobrevive `ciclo_de_culpa_2`*. **Las dos coronaciones son sobre SU PROPIO PAR y las
> dos matan al mismo nodo**, `ciclo_de_culpa`; **el par que falta, el unico sin veredicto del acto, es
> exactamente el que enfrentaria a los dos coronados.** **NINGUNA RAZON ESCRITA SE DESMIENTE** al
> fundir a favor de `ciclo_de_culpa_2`, porque el **2233** dice que `dysfunctional` gana **a
> `ciclo_de_culpa`** y no dice nada sobre el otro. **Lo que decide es `P.8`**, y la forma es `TODAS DE
> ACUERDO`: pasos (5 contra 4 y 4) y condiciones (3 contra 2 y 2) apuntan al mismo nodo. **El cableado
> apunta a `ciclo_de_culpa`, que es el nodo que LAS DOS razones matan**, y solo habla a contenido
> empatado.

> **LA ENTRADA DE INVENTARIO, MEDIDA Y DECLARADA, PORQUE TOCA LA FRONTERA DEL DUENO** (linea
> **[[PAG_DUENO_MEDIDO]]**): `INVENTARIO.jsonl` trae una entrada de tipo `familia_de_ids` llamada
> `ciclo_de_culpa`, con miembros `ciclo_de_culpa` y `ciclo_de_culpa_2`, forma *ids que difieren por
> sufijo*, estado *pendiente* y **`OP-S-09` en su campo `operaciones`**. **Leida al pie de la letra, la
> frontera diria que eso es dueno y que el acto no se funde.**
>
> **LA PRACTICA MEDIDA DE LA CAMPANA DICE LO CONTRARIO, Y ES PRECEDENTE Y NO OPINION:** el **`acto
> 3`** (fundido por el lote `A`) y el **`acto 7`** (fundido por el lote `B`) tenian **cada uno** una
> entrada `familia_de_ids` con `OP-S-09` cubriendo **PARTE** de su nomina, **3 de 10** y **2 de 6**, y
> **los dos se fundieron**; medido hoy sobre el grafo les queda **1 miembro vivo de 10** y **1 de 6**.
> **La frontera del acta 68 se escribio sobre un RACIMO que cubria la NOMINA ENTERA de su acto y que
> tenia `operaciones` VACIO**; esta entrada es de otra especie y cubre **2 de 3**. **Se funde por ese
> precedente, la lectura contraria va marcada discutible y la pregunta va al auditor.**
>
> **Y UNA CONSECUENCIA MEDIDA QUE SE PUBLICA PARA QUE `OP-S-09` NO SE LA ENCUENTRE:** tras esta fusion
> esa familia de ids queda con **UN solo id vivo**, y ese id es **`ciclo_de_culpa_2`**, o sea **el que
> lleva el sufijo numerico**. La verificacion de `OP-S-09` exige que **ningun id vivo lleve sufijo
> numerico de duplicado**, asi que **`OP-S-09` sigue teniendo trabajo sobre este id: un renombre con
> alias, que es exactamente su tipo**. Esta operacion **no lo hace y no lo estorba**, y lo deja
> escrito.

**El nodo crece de %(p34a)s pasos a %(p34b)s y de %(c34a)s condiciones a %(c34b)s.** **Los tres
`APPEND` son piezas que el 2233 nombra como propias del absorbido y que el superviviente NO TIENE:**
la **indefension aprendida** como sintoma medible, **los rituales repetidos sin evidencia de
efectividad**, y **sustituir las reacciones de evitacion de ansiedad por analisis genuino de causas
raiz**, que es la unica pieza del acto que nombra la causa raiz.

**EL UNICO `INCISO` VA AL PASO 2 Y REPONE LA FRASE QUE DA NOMBRE AL PATRON:** *culpar y entrenar*. El
**2272** declara ese paso `CUBIERTO`, y lo esta **en el gesto**, pero el superviviente **no dice esas
palabras**, que son las que vuelven buscable el patron.

%(rep34)s

%(abs34)s

%(per34)s

### d) **EL `ACTO 35`: LA TRIBU DE MARCA, UN `CHOCAN` QUE LA PIEZA DECLARADA RESUELVE SIN RESIDUO**

**Tres miembros del mismo libro** (*Never Lose a Customer Again*, de Coleman), **dos pares internos
con veredicto y los dos en `A`** (**178** y **880**), **cero `D`, cero puentes, cero triangulos y cero
puertas.**

**LA FORMA ES `CHOCAN`:** la vara de **pasos** apunta a `comunidad_tribu_marca` (6 contra 5 y 5) y la
de **condiciones** a `construccion_tribu_de_marca` (2 contra 1 y 1). **Cuando dos varas de contenido
CHOCAN decide LA PIEZA DECLARADA** (acta 53, pregunta 3), **y aqui esta escrita:** el **880** cierra
diciendo que **lo que hay que salvar es el ethos y la transformacion de identidad**, y esas dos piezas
son **exactamente** los pasos 1 y 2 de `construccion_tribu_de_marca`.

**Y NO ESTA SOLA:** ese nodo es ademas **el HUB del acto**, el unico miembro que aparece en **los dos**
pares con veredicto, **y el cableado apunta al mismo sitio** (4 contra 2 y 2). **De las cuatro cuentas
del acto, TRES apuntan al superviviente y una al otro. Este `CHOCAN` no deja residuo.** **La vara de
pasos se pierde por UNO y va marcada discutible.**

**El nodo crece de %(p35a)s pasos a %(p35b)s y se queda en %(c35b)s condiciones.** **CERO `APPEND` DE
CONDICION, y se dice en vez de callarlo:** las dos condiciones de los dos absorbidos dicen lo mismo
que las dos del superviviente, leidas una a una; **ninguna es un DISPARADOR DISTINTO**, que es la
unica puerta del acta 55 (pregunta 5).

**UNA ARISTA INTERNA MEDIDA Y DECLARADA:** los **dos absorbidos estaban cableados entre si**
(`marcador_visual_marca` tenia a `comunidad_tribu_marca` en sus siguientes y este a aquel en sus
previos). **Al fundir, esa arista habria quedado apuntando al superviviente desde el superviviente**, y
**el fundidor la retira**: la cuenta de auto-aristas retiradas del lote es **%(autoaristas)s**, y el
superviviente **no se cita a si mismo** en ninguno de sus dos campos, comprobado nodo a nodo.

%(rep35)s

%(abs35)s

%(per35)s

### e) **EL `ACTO 36`: EL PLAN DE CONTROL DE JURAN, EL ACTO MEJOR DECLARADO DEL LOTE Y EL NODO MAS GRANDE DE LA CAMPANA**

**Tres miembros del mismo libro** (*Juran's Quality Handbook*, de Defeo), **dos pares internos con
veredicto y los dos en `A`** (**2562** y **2639**), **cero `D`, cero puentes, cero triangulos y cero
puertas.**

**EL SUPERVIVIENTE ESTA DECLARADO VERBATIM EN LAS DOS RAZONES:** el **2562** cierra con *sobrevive
`plan_de_control`* y el **2639** con *sobrevive `plan_de_control`, el bucle completo de ocho pasos*, y
ademas lo llama **el hub** del acto. **La forma es `CHOCAN`** (pasos al superviviente, condiciones a
`matriz_de_control_de_proceso`) **y la pieza declarada no hay que interpretarla: esta escrita dos veces
con el nombre del nodo.**

**ESTE ACTO TRAE UN DISCUTIBLE HEREDADO DE SU PROPIO AUTOR Y NO SE ESCONDE:** el **2639** cierra con
*DISCUTIBLE MARCADO: quien lea capacitar duenos y auditar efectividad como pasos enteros propios dira
fusion mutua, por elegir*. **El reparto responde a ese aviso de la unica forma que lo desactiva: LOS
DOS pasos entran de `APPEND` y NINGUNO se sella como perdida**, o sea que **lo que la lectura contraria
querria conservar queda vivo dentro del superviviente**.

> **EL NODO CRECE DE %(p36a)s PASOS A %(p36b)s, Y ESO SE DICE CON ESA PALABRA: ES EL NODO MAS GRANDE
> QUE LA CAMPANA HA PRODUCIDO.** El anterior mayor fueron NUEVE. **La razon esta medida:** el
> superviviente **entra** con ocho porque el **2562** lo describe como **el nodo mas granulado** de los
> tres, y los dos que se le adosan son **los dos que el 2639 nombra como lineas a reponer**. **Y NO ES
> UNA PUERTA**: ningun miembro del acto lo es, medido. **Va marcado discutible.**

**LOS DOS `INCISO` VAN A PASOS DISTINTOS Y NINGUNO SE APILA** (acta 64): al **paso 3**, la
especificacion de *unidad de medida, sensor, frecuencia y tamano de muestra*, que es lo que vuelve
ejecutable *definir como se medira*; y al **paso 8**, la revision por *cobertura de variables criticas
y velocidad de respuesta*, que es **exactamente** la linea que el **2562** sella como *una linea a
reponer en la operacion de fusion*.

**Y POR ESO ESTE ACTO SELLA POCAS PERDIDAS, Y SE DICE PARA QUE LA CIFRA BAJA NO SE LEA COMO DESCUIDO:**
las piezas que las razones mandaban reponer **estan REPUESTAS** (una por `INCISO` y las dos del 2639
por `APPEND`), asi que **no se sellan como perdidas**: una perdida sellada que en realidad no se pierde
**infla la cuenta**.

%(rep36)s

%(abs36)s

%(per36)s

### f) **LAS GUARDAS DE LA OPERACION, LEIDAS DE LAS SALIDAS Y NO AFIRMADAS**

| guarda | resultado, leido de su salida |
|---|---|
| **guarda 1** (miembros vivos y nomina completa) | **`OK` en las cinco** |
| **guarda `1B`** (ningun absorbido es semilla ni extremo de puente) | **`OK` en las cinco**, y **pasa POR VACIO**: cero puertas dentro de los cinco actos |
| **guarda 2** (cobertura exacta de indices, cero olvidos) | **`OK` en las cinco** |
| **guarda 3** (cero repetidos literales en el resultado) | **`OK` en las cinco** |
| **guarda A** (cero auto-aristas nuevas) | **`OK`**, **%(autoaristas)s** retiradas |
| **guarda B** (cero duplicadas nuevas tras resolver) | **`OK`**, pasivo propio de la guarda **%(pasivo_antes)s** antes y **%(pasivo_despues)s** despues |
| **guarda C** (los campos que esta operacion NO redacta, intactos) | **%(campos_intactos)s** |
| **guarda D** (los absorbidos conservan su texto INTACTO) | **`OK`**, los **%(mueren)s** |
| **`P.16`, quien fabrica limpia, en el mismo commit** | **%(p16)s** duplicadas fabricadas y **limpiadas en la misma corrida** |
| **el reanclaje, corrido ENTRE la fusion y `run_phase1`** | **%(reanclaje)s**, y se dice por que: el fundidor ya habia redirigido **%(redirecciones)s** referencias vivas |
| **el diff de duplicadas, por instrumento** | **GRUPOS FABRICADOS DE VERDAD: %(dup_fab)s**, renombrados **%(dup_ren)s**, y los grupos pasan de **%(dup_antes)s** a **%(dup_despues)s** |
| **Gate 0 con su ciclo de TRES** | **`OK`**: **%(gate_activos)s** activos y **%(gate_deprecados)s** deprecados |

**EN CIFRAS DEL INSTRUMENTO:** **%(mueren)s nodos mueren** (**%(antes_vivos)s** vivos a
**%(despues_vivos)s**), **%(tocados)s ficheros tocados**, **%(piezas)s piezas repartidas**
(**%(enteras)s** enteras y **%(yadichas)s** ya dichas) y **%(per_total)s perdidas selladas en campo
propio**.

**EL GRUPO DE DUPLICADAS QUE DESAPARECE ESTA EXPLICADO Y NO ES UN CERO MUDO:** era el de
`control_mantener_ganancias` en `nodos_siguientes`, que traia **`ciclo_pdsa` y `ciclo_shewhart_pdsa`**
a la vez y que el propio censo clasificaba como *el id nuevo mas su alias*. Ese nodo **es ahora un
absorbido y sale del censo de vivos**, y el superviviente **hereda el destino una sola vez**.

**LA CUENTA AGREGADA DE LAS PERDIDAS, POR MAQUINA Y NO DE MEMORIA** (la regla del acta 68, linea
**[[PAG_CUENTA_AGREGADA]]**):

| | contado sobre el plan sellado |
|---|---:|
| **perdidas selladas en campo propio** | **%(per_total)s** |
| de ellas `DE PARAMETRO DE PASO` | **%(per_paso)s** |
| de ellas `DE CONDICIONES` | **%(per_cond)s** |
| **filas con `ATENUANTE DECLARADO`** | **%(per_aten)s** |
| de ellas, de la **especie del pendiente 4** | **%(per_p4)s** |
| de ellas, con **`ATENUANTE DECLARADO Y MEDIDO`** | **%(per_medido)s** |
| **filas con DOS SEDES en el campo `donde`** | **%(per_dos_sedes)s** |
| **filas que describen un atenuante SIN la frase sellada** | **NINGUNA**, medido, y por eso **no hay ninguna exclusion que decir en este lote** |
| la aritmetica de **la lectura contraria** (una fila por SITIO y no por PIEZA, linea **[[PAG_D10_POR_PIEZA]]**) | **%(per_contraria)s** y no **%(per_total)s** |

### g) **LA COLISION DE CLASE QUE ESTA VUELTA FABRICA, PREDICHA ANTES DE TOCAR UN NODO Y PUBLICADA EN ROJO CON SU DUENA**

**El carril esta escrito en esta misma pagina** (linea **[[PAG_LINEA_BASE]]**): **la duena de una
colision que fabrica una fusion es quien la fabrica.** **Duena: `OP-U-02`.**

| | |
|---|---:|
| linea base declarada **y MEDIDA sobre el arbol de antes** | **%(col_base)s** |
| **colisiones NUEVAS que la fusion fabricaria** | **%(col_nuevas)s** |
| colisiones que desaparecerian | **%(col_idas)s** |
| **ESPERADAS TRAS FUNDIR** | **%(col_esp)s** |
| **MEDIDAS al cierre por el censo** | **%(col_med)s** |
| **`CALZA`** | **`%(col_calza)s`** |
| auto-pares, predichos y medidos | **%(autopares)s** |

**LA NUEVA, NOMBRADA CON SUS PUESTOS:** `cuatro_etapas_del_pensamiento_creativo` contra
`wallas_intimacion_fringe_consciousness`, **`B` contra `D`**, de la fusion del **`acto 33`**. Sale del
puesto **279** (`B`, y su propio autor la titula *DUDOSO* y cierra con *no lo decido*) contra el
absorbido `intimation_illumination`, y del puesto **721** (`D`, *EL HIJO CON CASA PROPIA*, con la
arista verificada en los dos sentidos) contra el superviviente.

> **ES LA MISMA ESPECIE QUE LAS DOS DE LA VUELTA 69, y decirlo la explica: NO es una lectura nueva ni
> una lectura movida, es UNA LECTURA VIEJA QUE CAMBIA DE VECINO.** La madre `wallas_etapa_iluminacion`
> tenia una lectura `B` **dudosa** contra el gemelo sin casa y una lectura `D` **firme** contra el
> hijo con casa propia; la fusion junta los dos lados en un solo par resuelto y **el choque se vuelve
> visible**. **Y hay una simetria que conviene dejar escrita: el mismo dato de arista que el puesto
> 403 uso para ELEGIR al superviviente es el que hace que la colision aparezca.**
>
> **LA LINEA BASE QUE ESTE LOTE USO YA ES `6`**, por la adjudicacion 1 del acta 69 y la correccion
> declarada que esta vuelta aplico sobre el instrumento (linea **[[PAG_ACTA69_BASE]]**). **Con esta,
> la base operativa pasaria a `7`**, y **el ejecutor NO la mueve**: va como pregunta al auditor, igual
> que la vuelta 69 hizo con la suya.

### h) **LO QUE QUEDA DEL TRAMO AL CIERRE DE ESTE LOTE, MEDIDO Y NO ARRASTRADO**

| | |
|---|---:|
| actos del tramo unico | **47** |
| actos **FUNDIDOS**, medido sobre el grafo | **%(fundidos_medidos)s** |
| actos **`DECLARADOS Y NO FUNDIDOS`** | **%(declarados_arg)s** |
| **quedan sin destino** | **%(quedan_actos)s actos y %(quedan_nodos)s nodos** |
| **el siguiente del prefijo** | el acto **%(siguiente)s**, **con dueno** |
| de los que quedan, **con dueno medido** | **%(con_dueno)s** |
| de los que quedan, **con nodo puente** | **%(quedan_puente)s** |
| de los que quedan, **con par `D` interno** | **%(quedan_d)s** |
| componentes `ABIERTOS` del recomputo | **%(abiertos)s** sobre **%(abiertos_n)s** nodos |

**LA MEDICION SALE DE UN INSTRUMENTO DE NOMBRE ESTABLE QUE NACE EN ESTA VUELTA**,
[`../../scripts/loop/tramo_al_cierre.py`](../../scripts/loop/tramo_al_cierre.py), **y va dicho por
que**: esta tabla se venia publicando desde una sonda escrita dentro de la vuelta que **no quedaba en
el arbol**, y una cifra que se publica en cada vuelta y cuyo instrumento no se puede re-correr contra
otro corte es justo lo que la regla 2 del ejecutor prohibe. **El reparto por lotes y la lista de
declarados entran por argumento y el instrumento lo dice**, porque **no se pueden medir sobre el
grafo**: un acto declarado tiene todos sus miembros vivos igual que uno sin tocar.

### i) **LO QUE ESTE REGISTRO NO HACE**

**NO toca ni una cifra publicada arriba**, **NO deshace ninguna fusion**, **NO re-lee ni un veredicto
de las colisiones vigentes**, **NO toca la mesa `OP-M-03` ni sus dos colisiones**, **NO toca las
CUATRO colisiones de `OP-U-02` ya publicadas**, **NO ejecuta ninguna de las cinco fichas `OP-M-02`
consumidas** (lo consumado no se ejecuta ni se rehace), **NO funde ningun acto con dueno** (el `31` y
el `37` quedan con los suyos), **NO mueve la linea base del censo** (la sube como pregunta) y **NO
anade ni una fila ni una columna a ninguna tabla de registrador**, que es la adjudicacion 3 del acta
69 aplicada sobre el instrumento que la registra.
"""
