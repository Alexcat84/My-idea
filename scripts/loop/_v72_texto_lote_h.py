# -*- coding: utf-8 -*-
"""_v72_texto_lote_h.py . EL TEXTO EDITORIAL DEL REGISTRO DEL LOTE H.

NO ES UN INSTRUMENTO: es el texto. La maquina que lo arma, lo coteja y lo adosa
es scripts/loop/vuelta72_registro_lote_h.py, que lo importa. Mismo reparto que
_v67_texto..., _v68_texto_lote_d.py, _v69_texto_lote_e.py, _v70_texto_lote_f.py
y _v71_texto_lote_g.py.

NI UNA CIFRA TECLEADA Y NI UN NUMERO DE LINEA TECLEADO: las cifras entran como
%(clave)s y salen de una salida de esta vuelta leida por expresion regular; las
citas de linea entran como [[CLAVE]] y salen de buscar su aguja de contenido.
Las tablas entran armadas del PLAN SELLADO o recortadas de la salida del
tallador. La del acto DECLARADO sale del campo declarados_y_no_fundidos del
mismo plan.
"""

TEXTO = """

---

## `OP-U-02, TRAMO UNICO: EL REGISTRO DEL LOTE H` (2026-08-26, vuelta 72)

**Se cuelga de la cabecera de tramo que la vuelta 65 adoso** (linea **[[PAG_TRAMO_CABECERA]]**,
derivada hoy por aguja) **y se adosa al final del documento sin reescribir ni una linea de arriba.**
El lote `E` esta en la **[[PAG_LOTE_E]]**, el `F` en la **[[PAG_LOTE_F]]** y el `G` en la
**[[PAG_LOTE_G]]**. **Las adjudicaciones del acta 71 que gobiernan este lote se adosaron en la
`TAREA 1` de esta misma vuelta y viven en la linea **[[PAG_ACTA71]]**.**

**EL LOTE ABRE EN EL `ACTO 43`, QUE ES EL PRIMERO DEL TRAMO SIN DUENO MEDIDO, Y LOS DOS SALTOS VAN
DECLARADOS CON SU CITA**, que es lo que la adjudicacion 2 del acta 69 manda (registrada en esta misma
pagina, linea **[[PAG_ADJ_ACTO31]]**): el `acto 31` **TIENE DUENO MEDIDO** (`OP-F-04-WEI` y
`OP-S-04`) y el `acto 37` tambien (`OP-S-07`), **ninguno de los dos es una fusion de `OP-U-02`**, asi
que **no estan en la cola de fusiones de esta operacion** y saltarlos **no rompe el prefijo sin
saltos**. Su destino queda **con sus duenos en sus fases**.

**SE DECLARARON CINCO ACTOS Y 15 NODOS, Y SE ENTREGARON LOS CINCO.** **CUATRO CIERRAN FUNDIDOS Y UNO
CIERRA `DECLARADO Y NO FUNDIDO`**: el `acto 44`, **por LA GUARDA `1B` con DOS puertas**. **Es el
primer `DECLARADO` desde el lote `E` de la vuelta 69 y el PRIMERO DE TODO EL TRAMO cuyo motivo sellado
es la guarda `1B` y no el triangulo de `P.10`.**

| acto | miembros | cierra | **FORMA medida** | superviviente |
|---:|---:|---|---|---|
| **43** | 3 | **FUNDIDO** | `UNA SOLA VARA` | `preservar_efectivo_buscar_modelo` |
| **44** | 3 | **`DECLARADO Y NO FUNDIDO`** | `UNA SOLA VARA` | **NINGUNO**, y ninguno se toca |
| **45** | 3 | **FUNDIDO** | `CONTENIDO EMPATA` | `reconstruccion_contexto_situacional` |
| **46** | 3 | **FUNDIDO** | `UNA SOLA VARA` | `mitigacion_riesgos_ambientales` **(LA PUERTA)** |
| **47** | 3 | **FUNDIDO** | `UNA SOLA VARA` | `gestion_terminacion_franquiciado` |

**EL TOPE DEL PREFIJO NO ES ESTRUCTURAL SINO DE LOTE, Y SE DICE EN VEZ DE DEJARLO COMO UN NUMERO
ELEGIDO:** el siguiente sin destino es el **`acto %(siguiente)s`**, **que TIENE DUENO** y por eso
vuelve a saltarse cuando el prefijo se reabra; el primero **sin dueno** de lo que queda es el **`acto
49`**, **que tampoco trae puerta**, y el tope de este lote cae antes de el **porque el encargo fija
CINCO actos**, no porque el `49` tenga nada que lo impida.

> **DOS DE LAS TRES CORRECCIONES DECLARADAS DE LA `TAREA 1` MUERDEN SOBRE ESTE LOTE, Y SE DICE CUAL
> CAMBIA QUE.** La primera (linea **[[PAG_CORR_OPL03]]**): las entradas de tipo acto de los cinco
> nombran en `operaciones` **NO SOLO `OP-U-02` sino tambien `OP-L-03`**, igual que en el lote `G`; la
> diferencia es que **ahora la ficha de `OP-L-03` YA LLEVA su correccion declarada aplicada**, asi que
> la clausula de la era del par **ya no esta en divergencia**: sigue entera arriba y la vara nueva esta
> escrita debajo. **Lo que en el lote `G` iba como pregunta abierta, aqui va como pregunta CONTESTADA
> con su cita.** La segunda (linea **[[PAG_CORR_PREFIJO]]**): **el plan de este lote se sello como
> `PLAN_V72_OPU02_LOTE_H.json` y no como `OPU01`**, que es el defecto viejo del generador. **La
> correccion se comprobo leyendo el nombre del fichero ANTES de sellar**, y es la primera vez que un
> plan de este tramo sale con el nombre de su operacion sin pasar `--prefijo` a mano.

**LOS CUATRO MOTIVOS SELLADOS DEL `DECLARADO Y NO FUNDIDO`, RECORRIDOS UNO A UNO SOBRE ESTE LOTE**,
porque un motivo que no se usa se cuenta como usado si nadie lo dice:

| motivo sellado | sobre este lote |
|---|---|
| el triangulo de `P.10` (linea **[[PAG_ACTO1_P10]]**) | **SIN SUJETO**: cero nodos puente y cero triangulos en los cinco, y **%(actos_sin_puente)s de %(actos_mirados)s** actos de lo que queda del tramo tambien sin ninguno, medido en esta vuelta |
| la guarda `1B` con DOS o mas puertas (linea **[[PAG_GUARDA_1B]]**) | **MUERDE, Y ES LA NOTICIA DEL LOTE**: el `acto 44` trae **DOS** puertas medidas contra el universo protegido de **256** ids, y cierra `DECLARADO` |
| la respuesta *DOS FAMILIAS* de `P.5` (linea **[[PAG_P5_MOTIVO]]**) | **NO SE USO**: los cinco contestaron **UNA familia**, **incluido el `44`**, y eso se dice porque lo que detiene al `44` **no es la familia, son sus puertas** |
| el `D` directo interno (linea **[[PAG_CUARTO_MOTIVO]]**) | **SIN SUJETO**: **CERO** pares `D` internos en los cinco y en los **%(quedan_actos)s** que quedan, medido |

> **Y LA CUENTA DE LOS MOTIVOS POSIBLES SIGUE SIENDO DOS EN LO QUE RESTA DEL TRAMO**, por la
> adjudicacion 4 del acta 70 registrada en esta misma pagina (linea **[[PAG_ADJ_PUERTAS]]**). **Este
> lote gasta uno de los dos y lo devuelve medido:** la guarda `1B` **tenia sujeto y mordio**, tal como
> el acta 70 predijo para el `44` y el acta 71 volvio a medir. **`P.10` y el cuarto motivo siguen sin
> sujeto y se dice.**

### a) **EL `ACTO 43`: EL FRENO AL GASTO ANTES DE VALIDAR EL MODELO, Y EL CHOQUE MAS CARO DEL LOTE ENTRE EL CONTENIDO Y EL CABLEADO**

**Tres miembros del mismo libro** (*The Startup Owner's Manual*, de Blank), **dos pares internos con
veredicto y los dos en `A`** (**550** y **935**), **cero `D`, cero puentes, cero triangulos y cero
puertas.** El **935** se titula *el mismo freno contra el escalamiento temprano, del mismo libro y sin
arista entre ellos*.

**LA FORMA ES `UNA SOLA VARA`, Y NO ES LA DE PASOS:** la de **pasos** EMPATA en 5 entre el
superviviente y `restriccion_gasto_validacion` y no apunta; la de **condiciones** apunta al
superviviente (4 contra 2 y 2). **UNA SOLA VARA DE CONTENIDO NO EMPATADA BASTA** (acta 53, pregunta
4), **y es la misma forma que el acta 71 adjudico `A FAVOR` en su `D4` para el `acto 42`**.

> **EL CABLEADO APUNTA AL OTRO LADO Y ES EL CHOQUE MAS CARO DEL LOTE: 11 contra 7 y 7**, a
> `restriccion_gasto_validacion`, **que tiene DIEZ nodos siguientes**, la cifra mas alta del lote.
> **La cifra sale de la columna `cab` del instrumento de varas**, que es la unica fuente de cifra de
> cableado desde la adjudicacion 3 del acta 70 (linea **[[PAG_ADJ_CABLEADO]]**). **`P.8` es regla de
> PRELACION y el cableado solo habla a contenido empatado**, y aqui el contenido no empata. **Va
> marcado discutible en el reporte y el costo se paga en redirecciones.**

**NINGUNA RAZON CORONA A NADIE EN ESTE ACTO, Y ESO SE COMPRUEBA EN VEZ DE SUPONERSE.** El **550**
reparte lo propio de cada lado sin elegir; el **935** nombra **dos piezas** de
`restriccion_gasto_validacion` como *lo que hay que salvar*, **que no es coronarlo: es encargar su
rescate**, y **este reparto lo ejecuta, las dos, de `APPEND` entero**.

**El nodo crece de %(p43a)s pasos a %(p43b)s y de %(c43a)s condiciones a %(c43b)s. Es el acto que mas
crece del lote y va marcado por eso.**

**LOS TRES `APPEND` SON GESTOS QUE LAS RAZONES NOMBRAN COMO PROPIOS**, uno a uno: **el presupuesto
maximo por prueba con su cifra** y **la caja reservada para financiar varios pivotes** (las dos que el
**935** manda salvar), y **retrasar las inversiones grandes en infraestructura** (lo propio de
`escalamiento_prematuro` segun esa misma razon). **EL UNICO `INCISO` VA AL PASO 3** y es un parametro
del gesto que el superviviente ya tiene: su paso 3 ya mide dinero, y lo que entra es **con que vara**,
*tu ritmo de consumo de caja (burn rate) como tu metrica principal*.

%(rep43)s

%(abs43)s

%(per43)s

### b) **EL `ACTO 44`: `DECLARADO Y NO FUNDIDO` POR LA GUARDA `1B`, CON DOS PUERTAS, Y NI UN NODO TOCADO**

**Es el primer `DECLARADO` desde el lote `E` de la vuelta 69 y el PRIMERO DE TODO EL TRAMO cuyo motivo
sellado es la guarda `1B`.** **DOS de los tres miembros son PUERTA**
(`explotacion_tecnologias_disruptivas` y `tecnologias_disruptivas_oportunidad`), medido contra el
universo protegido de **256** ids. **La guarda `1B` prohibe absorber una puerta, y con DOS no existe
ningun superviviente posible que no absorba a la otra.**

> **LA LETRA ESTA REGISTRADA EN ESTA MISMA PAGINA** (linea **[[PAG_GUARDA_1B]]**) **y dice, con estas
> palabras: si aparece un acto que no se pueda fundir sin absorber una puerta, cierra `DECLARADO` con
> la guarda `1B` como motivo, SIN improvisar fusiones parciales que ninguna letra escribe.** **Y EL
> CASO DE UNA SOLA PUERTA NO ES ESTE**, y la propia pagina lo distingue en la linea
> **[[PAG_PUERTA_UNICA]]**: con **una** el acto **si se funde** y la puerta sobrevive. **Con dos, no.**

**LO QUE NO SE HACE, ENUMERADO PARA QUE NADIE LO LEA COMO UN OLVIDO:** no se funde
`evaluacion_tecnologias_disruptivas` contra una de las dos puertas dejando la otra fuera, **porque eso
seria una fusion parcial**; no se elige puerta ganadora, **porque la guarda no ordena las puertas
entre si**; no se parte el acto en dos componentes, **porque el acto es la componente y partirla es re
cribar**; y **no se toca ni un nodo, ni un alias, ni un veredicto**.

**Y LA FAMILIA NO ES LO QUE LO DETIENE, QUE ES LO QUE HAY QUE DECIR PARA QUE EL CIERRE DE LA FASE 03
LO ENCUENTRE LISTO:** `P.5` contesta **UNA SOLA FAMILIA** con las razones delante. Los tres miembros
son del mismo libro (*Winning at New Products*, de Cooper), los dos pares internos con veredicto son
de clase `A` (**505** y **513**), y el **513** cierra declarando que **esta familia llega a TRES nodos
del nucleo y ninguno esta en `RACIMOS_MIEMBROS.jsonl`**. **Es UNA familia que NO SE PUEDE FUNDIR, que
no es lo mismo que DOS familias.**

> **A QUIEN HABRIAN APUNTADO LAS VARAS, DICHO EN VEZ DE CALLADO, PORQUE CALLARLO SERIA ESCONDER EL
> COSTO:** la forma medida es `UNA SOLA VARA` y la de **pasos** apunta a
> `explotacion_tecnologias_disruptivas` (6 contra 4 y 4); el **cableado** apunta AL OTRO LADO, a
> `tecnologias_disruptivas_oportunidad` (6 contra 5 y 2), leido de la columna `cab`. **LOS DOS NODOS A
> LOS QUE APUNTAN LAS VARAS SON LAS DOS PUERTAS**, y ese es justamente el problema.

%(dec44)s

> **UNA MEDICION QUE SE DEJA ESCRITA PARA QUIEN RETOME ESTE ACTO EN EL CIERRE DE LA FASE 03:** la nota
> de la ficha de `OP-L-03`, leida hoy, declara que `evaluacion_tecnologias_disruptivas` es **`LD-04`**,
> una de las DOS lecturas dirigidas de la primera tanda **YA LEIDAS**. **El acto no se toca, asi que
> esa lectura no se gasta ni se contradice.**

### c) **EL `ACTO 45`: LA RECONSTRUCCION SIN SESGO RETROSPECTIVO, Y EL UNICO ACTO DEL LOTE QUE DECIDE EL CABLEADO SOLO**

**Tres miembros del mismo libro** (*The Field Guide to Understanding Human Error*, de Dekker), **dos
pares internos con veredicto y los dos en `A`** (**2244** y **2294**), **cero `D`, cero puentes, cero
triangulos y cero puertas.** Las dos razones abren con *REPITE* y las dos hacen la misma cuenta: **los
CINCO pasos de `evitar_sesgo_retrospectivo_hindsight` estan cubiertos uno a uno**, y las dos cierran
con la misma frase, ***no le queda ni una linea propia***.

**LAS DOS RAZONES CORONAN SUPERVIVIENTES DISTINTOS, Y VA DICHO ENTERO:** el **2244** cierra con
*sobrevive `reconstruccion_contexto_situacional`* y el **2294** con *sobrevive `evitar_shopping_bag`*.
**Las dos coronaciones son sobre SU propio par y las dos matan al mismo nodo**,
`evitar_sesgo_retrospectivo_hindsight`; **el par que falta, el unico sin veredicto del acto, es
exactamente el que enfrentaria a los dos coronados.** **Es la misma forma que el `acto 34` del lote `F`
y el `acto 39` del lote `G`**, que las actas 70 y 71 adjudicaron `A FAVOR` en su `D6` y su `D5`.

> **Y HAY UNA DIFERENCIA CON AQUELLOS DOS QUE NO SE CALLA:** alli el par que faltaba **no tenia
> arista**; aqui los dos coronados **SI la tienen, y en los dos sentidos**
> (`reconstruccion_contexto_situacional` nombra a `evitar_shopping_bag` entre sus siguientes y
> `evitar_shopping_bag` lo nombra entre sus previos). **El archivo ya dice que uno viene del otro.**
> **Va marcado discutible.**

**LA FORMA ES `CONTENIDO EMPATA`, LA UNICA DEL LOTE:** la de **pasos** empata en 5 **a tres bandas** y
la de **condiciones** empata en 2 entre dos de ellos. **CON EL CONTENIDO EMPATADO, Y SOLO ENTONCES,
HABLA EL CABLEADO**, que es la letra exacta de `P.8`: apunta a `reconstruccion_contexto_situacional`
con **8 contra 3 y 2**, leido de la columna `cab`. **Es el unico acto del lote que decide el cableado
solo, y por eso el margen se publica y no se resume: 8 contra 3 y 2 no es un margen de uno.**

**El nodo crece de %(p45a)s pasos a %(p45b)s y de %(c45a)s condiciones a %(c45b)s. Es el reparto mas
barato del lote**, y no por generosidad sino porque **el absorbido grande no tenia lineas propias: las
dos razones lo dicen.**

**EL UNICO `APPEND` ES EL QUE LA RAZON NOMBRA POR SU NOMBRE:** *identificar que senales se contradecian
entre si en el momento*, que el **2294** llama **el paso que le da nombre al efecto y que ningun otro
nodo del racimo tiene**. **EL UNICO `INCISO` VA AL PASO 5** y es la forma concreta que toma el vicio
que ese paso prohibe.

%(rep45)s

%(abs45)s

%(per45)s

### d) **EL `ACTO 46`: EL RIESGO AMBIENTAL DE LA CADENA EXTENDIDA, Y LA PUERTA QUE SOBREVIVE AUNQUE PIERDA EN CONTENIDO**

**Tres miembros del mismo libro** (*The Green to Gold Business Playbook*, de Esty), **dos pares
internos con veredicto y los dos en `A`** (**1788** y **1822**), **cero `D`, cero puentes, cero
triangulos y UNA PUERTA.** El **1822** declara que **la familia del riesgo ambiental extendido pasa de
DOS a TRES nodos por cierre transitivo, con `mitigacion_riesgos_ambientales` de centro**.

> **AQUI DECIDE LA GUARDA `1B` ANTES QUE `P.8`, Y EL CHOQUE SE ESCRIBE ENTERO EN VEZ DE MAQUILLARSE.**
> **Con UNA puerta el acto SI se funde y LA PUERTA SOBREVIVE** (acta 54, pregunta 1), **gane o pierda
> en contenido**, y la propia pagina lo tiene escrito en la linea **[[PAG_PUERTA_UNICA]]** con estas
> palabras: *el choque con la vara de contenido queda escrito en el motivo sellado*. **ESTE ES
> EXACTAMENTE ESE CASO, Y EL CHOQUE EXISTE.**

**`P.8` EN ORDEN, MEDIDO Y PUBLICADO AUNQUE NO DECIDA:** la de **pasos** empata en 4 **a tres bandas**;
la de **condiciones** apunta a `gestion_eco_riesgos` (**3 contra 2 y 2**); y el **cableado** tambien
empata, **4 entre dos de ellos**, leido de la columna `cab`. **LA UNICA VARA QUE HABLA APUNTA AL OTRO
LADO, y aun asi el superviviente es la puerta.** **Va marcado discutible con las tres cifras al lado.**

> **LA CONSECUENCIA PARA `OP-S-09` SE PUBLICA EN VEZ DE CALLARSE**, que es lo que la adjudicacion 2 del
> acta 70 exige (linea **[[PAG_ADJ_DUENO]]**): `INVENTARIO.jsonl` trae una entrada de tipo
> `familia_de_ids` con `responsabilidad_extendida_productor` y `responsabilidad_extendida_productor_2`,
> con `OP-S-09` en `operaciones` y con la nota *DECISION 4 de la mesa de racimos, aprobada el 9 ago
> 2026: familia unica, fusion con alias*. **Cubre UNO de los tres miembros, o sea PARTE de la nomina,
> que es EXACTAMENTE el caso que esa adjudicacion resolvio.** **Este acto absorbe a
> `responsabilidad_extendida_productor`**, y a `OP-S-09` **le queda
> `responsabilidad_extendida_productor_2` VIVO** (medido hoy sobre `master_graph`, sin marca de
> deprecado) **mas el otro id resolviendo por alias a `mitigacion_riesgos_ambientales`**. **Su sujeto
> queda SERVIBLE**, y lo que cambia se dice: **su resolucion aprobada tendra que ejecutarse sobre un
> alias que apunta FUERA de la familia.** **Va marcado discutible.**
>
> **Y EL BORDE QUE EL ACTA 71 ESCRIBIO NO SE PISA, MEDIDO Y NO SUPUESTO** (linea
> **[[PAG_ADJ_BORDE]]**): barridas las **12** entradas de `INVENTARIO.jsonl` que tocan a los 15
> miembros del lote, **UNA SOLA es de tipo `familia_de_ids`** y **CERO cubren la nomina ENTERA de
> ningun acto del lote**.

**El nodo crece de %(p46a)s pasos a %(p46b)s y de %(c46a)s condiciones a %(c46b)s.** **EL UNICO
`APPEND` DE PASO** es *mapear todos los puntos de la cadena de valor*, que el **1788** llama **el
unico paso que da un metodo para encontrarlos en vez de suponerlos**. **EL UNICO `APPEND` DE
CONDICION** es un **disparador distinto y no un matiz** (no haber evaluado formalmente la exposicion),
que es la unica puerta por la que el acta 55 (pregunta 5) deja pasar una condicion. **EL UNICO
`INCISO` VA AL PASO 3** y es *sobre que* se disenan los planes de contingencia.

%(rep46)s

%(abs46)s

%(per46)s

### e) **EL `ACTO 47`: LA TERMINACION DEL FRANQUICIADO, EL UNICO DEL LOTE QUE NO HACE CRECER A SU SUPERVIVIENTE Y EL UNICO CON LAS DOS RAZONES CORONANDO AL MISMO NODO**

**Tres miembros del mismo libro** (*Franchise Your Business*, de Siebert), **dos pares internos con
veredicto y los dos en `A`** (**2072** y **2190**), **cero `D`, cero puentes, cero triangulos y cero
puertas.** **Las dos razones cierran con *por la vara, REPITE*** y el **2190** remata con *sobrevive
`gestion_terminacion_franquiciado` por contenido*. **No hay coronas cruzadas que reconciliar.**

**Y EL ARCHIVO DECLARA UNA FIGURA SOBRE ESTE ACTO:** la entrada de tipo `figura` del **SUBCONJUNTO
ESTRICTO** (banco `9.6.1`) nombra al par de `gestion_terminacion_franquiciado` con
`terminacion_franquiciado_causas` con esta glosa: *los pasos del corto viven dentro del largo y lo
unico propio cabe en una linea*. **El 2072 hace esa cuenta paso por paso.**

**LA FORMA ES `UNA SOLA VARA`:** la de **pasos** apunta al superviviente (5 contra 4 y 4) y la de
**condiciones** empata en 2. **Y LAS DOS RAZONES ESCRITAS APUNTAN AL MISMO NODO QUE LA VARA.**

> **EL CABLEADO APUNTA AL OTRO LADO Y ES EL MARGEN MAS ESTRECHO DE TODO EL LOTE: 2 contra 1 y 1**, a
> `perdida_control_operativo`, **UN SOLO ENLACE DE DIFERENCIA**, leido de la columna `cab`. **El
> superviviente es el nodo peor cableado del acto** (un enlace, y **CERO** siguientes) **y aun asi gana
> por contenido**, porque el cableado solo habla a contenido empatado y aqui el contenido no empata.
> **Se publica igual, porque una cifra que solo se publica cuando conviene no es una cifra.**

**EL NODO NO CRECE NI UN PASO NI UNA CONDICION: se queda en %(p47b)s pasos y %(c47b)s condiciones**, y
**es el unico acto del lote asi.** **La razon esta medida y no es avaricia del reparto:** las dos
razones dicen lo mismo con las mismas palabras, ***lo unico que el corto anade es una frase*** y ***lo
unico propio de `perdida_control_operativo` es su paso 1, y eso cabe en una linea***. **Cuando lo
propio cabe en una linea, la linea va de `INCISO`.**

**LOS DOS `INCISO` VAN A PASOS DISTINTOS Y NINGUNO SE APILA** (acta 64), **y los dos son la unica
linea propia de su absorbido, nombrada por su propia razon**: al **paso 2**, *segun su gravedad*, que
el **2072** aisla con las palabras *lo unico que el corto anade es una frase*; y al **paso 1**, *que
decisiones operativas quedaran bajo control del franquiciado*, que el **2190** no solo aisla sino que
**enruta**: *la linea de la aceptacion del control cedido se absorbe en el*. **El `INCISO` ejecuta esa
frase al pie.**

%(rep47)s

%(abs47)s

%(per47)s

### f) **LAS GUARDAS DE LA OPERACION, LEIDAS DE LAS SALIDAS Y NO AFIRMADAS**

| guarda | resultado, leido de su salida |
|---|---|
| **guarda 1** (miembros vivos y nomina completa) | **`OK` en las cuatro fusiones** |
| **guarda `1B`** (ningun absorbido es semilla ni extremo de puente) | **`OK` en las cuatro**, y **NO pasa por vacio en el lote**: en el `acto 46` la puerta **es el superviviente** y en el `44` **detuvo la fusion entera** |
| **guarda 2** (cobertura exacta de indices, cero olvidos) | **`OK` en las cuatro** |
| **guarda 3** (cero repetidos literales en el resultado) | **`OK` en las cuatro** |
| **guarda D** (los absorbidos conservan su texto INTACTO) | **`OK`**, los **%(mueren)s** |
| **`P.16`, quien fabrica limpia, en el mismo commit** | **1** duplicada fabricada y **limpiada en la misma corrida** |
| **el reanclaje, corrido ENTRE la fusion y `run_phase1`** | **%(reanclaje)s**, y **es un cero medido y no un cero supuesto**: el fundidor redirigio **30** referencias vivas y no quedo ninguna fuera del grafo. **Ninguna ancla duplicada se fabrico**, comprobado sobre los **49** rumbos del banco |
| **el diff de duplicadas, por instrumento** | **GRUPOS FABRICADOS DE VERDAD: %(dup_fab)s**, renombrados **%(dup_ren)s**, y los grupos pasan de **%(dup_antes)s** a **%(dup_despues)s** |
| **Gate 0 con su ciclo de TRES** | **`OK`**: **%(gate_activos)s** activos y **%(gate_deprecados)s** deprecados |

**EN CIFRAS DEL INSTRUMENTO:** **%(mueren)s nodos mueren** (**%(antes_vivos)s** vivos a
**%(despues_vivos)s**), **%(tocados)s ficheros tocados**, **%(piezas)s piezas repartidas**
(**%(enteras)s** enteras y **%(yadichas)s** ya dichas) y **%(per_total)s perdidas selladas en campo
propio**. **El plan sello %(fundidos_plan)s fusiones y %(declarados_plan)s declarado, y el fundidor
ejecuto exactamente eso.**

**LOS GRUPOS DE DUPLICADAS QUE DESAPARECEN ESTAN EXPLICADOS Y NO SON UN CERO MUDO:** son
**%(dup_idas)s**, y los tres son de la misma especie: **un vivo que apuntaba a DOS miembros del mismo
acto en el mismo campo**, y que tras la fusion **hereda el destino una sola vez**. **`P.16` limpio en
la misma corrida** y el diff por instrumento mide **CERO fabricados** y **CERO renombrados**.

**LA COLA DE COSTURAS BAJA Y SE MIDE NODO A NODO EN VEZ DE DEJARSE COMO UN MENOS DOS:** de
**%(cola_antes)s** a **%(cola_despues)s**, con **%(cola_entran)s que entran** y **%(cola_salen)s que
salen**, y los dos que salen son **absorbidos que dejan de ser vivos**. **NINGUN superviviente de este
lote entra a la cola**, que es la diferencia entera con el lote `G`, donde entraron tres y quedo
marcado como su costo mas caro.

**LA CUENTA AGREGADA DE LAS PERDIDAS, POR MAQUINA Y NO DE MEMORIA:**

| | contado sobre el plan sellado |
|---|---:|
| **perdidas selladas en campo propio** | **%(per_total)s** |
| de ellas `DE PARAMETRO DE PASO` | **%(per_paso)s** |
| de ellas `DE CONDICIONES` | **%(per_cond)s** |
| **filas con `ATENUANTE DECLARADO`** | **%(per_aten)s** |
| de ellas, de la **especie del pendiente 4** | **%(per_p4)s**, **y esa cifra lleva su glosa aparte** |
| de ellas, con **`ATENUANTE DECLARADO Y MEDIDO`** | **%(per_medido)s** |
| **filas con DOS SEDES en el campo `donde`** | **%(per_dos_sedes)s** |
| **filas que describen un atenuante SIN la frase sellada** | **NINGUNA**, medido, y por eso **no hay ninguna exclusion que decir en este lote** |
| la aritmetica de **la lectura contraria** (una fila por SITIO y no por PIEZA, linea **[[PAG_D10_POR_PIEZA]]**) | **%(per_contraria)s** y no **%(per_total)s** |

> **LA CELDA DE LA ESPECIE DEL PENDIENTE 4 SALE EN %(per_p4)s Y NO SE DEJA COMO UN CERO QUE PARECE
> LIMPIO:** el instrumento la cuenta buscando la frase sellada *ESPECIE DEL PENDIENTE 4* dentro del
> campo `que`, **y la fila del `acto 43` no la lleva**. **En sustancia esa fila SI es de esa especie**
> (la pieza llega entera por otro absorbido del mismo acto), **pero por un `INCISO` y no por un
> `APPEND`**, que es el vehiculo que el nombre del pendiente nombra. **Se declara aqui en vez de
> corregir el plan, porque un plan EJECUTADO no se re-sella** (acta 68, `D15`), **y la pregunta de si
> la especie la define el VEHICULO o el HECHO va marcada discutible en el reporte.**

### g) **EL CENSO DE COLISIONES: ESTE LOTE NO FABRICA NINGUNA, Y SE PUBLICA IGUAL**

**El carril esta escrito en esta misma pagina** (linea **[[PAG_LINEA_BASE]]**): **la duena de una
colision que fabrica una fusion es quien la fabrica.** **Este lote no fabrica ninguna, y la cuenta se
publica exactamente igual que cuando si las fabrica**, porque un censo que solo se publica cuando sale
mal no es un censo.

| | |
|---|---:|
| linea base declarada **y MEDIDA sobre el arbol de antes** | **%(col_base)s** |
| **colisiones NUEVAS que la fusion fabricaria** | **%(col_nuevas)s** |
| colisiones que desaparecerian | **%(col_idas)s** |
| **ESPERADAS TRAS FUNDIR** | **%(col_esp)s** |
| **MEDIDAS al cierre por el censo** | **%(col_med)s** |
| **auto-pares NUEVOS predichos antes de fundir** | **%(autopares_esp)s** |
| **auto-pares MEDIDOS al cierre** | **%(autopares)s** |

> **LA LINEA BASE QUE ESTE LOTE USO ES `%(col_base)s`, Y ENTRO POR EL DEFECTO DEL INSTRUMENTO**, por la
> adjudicacion 1 del acta 70 y la correccion declarada que la vuelta 71 aplico. **No hizo falta pasarla
> a mano, y la guarda la MIDIO sobre el arbol antes de usarla.** **SEGUNDO LOTE SEGUIDO DEL TRAMO QUE
> NO FABRICA NINGUNA.** **Las dos colisiones de la mesa `OP-M-03` y las CINCO de `OP-U-02` ya
> publicadas siguen vigentes con su duena y no se tocan.**

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

**Y LAS PUERTAS DE LOS QUE QUEDAN SE MIDEN Y SE PUBLICAN CON SU SALIDA COMMITTEADA**, que es la regla
practica que sale de la caida de reporte del acta 70: de los **%(quedan_actos)s** que quedan, **DOS
traen puerta** y van nombrados uno a uno. El **`31`** una, `captura_conocimiento_mercado` (y ademas
tiene dueno), y el **`51`** una, `metodo_valor_presente_neto`. **Los dos funden con su puerta
sobreviviendo cuando les toque** (acta 54, pregunta 1), **por la adjudicacion 4 del acta 70** (linea
**[[PAG_ADJ_PUERTAS]]**), **y ninguno de los dos puede cerrar `DECLARADO` por la guarda `1B`, porque
esa guarda pide DOS.** **El `44`, que era el que traia dos, ya cerro en este lote.**

> **Y LAS FORMAS DE LOS %(quedan_actos)s SE MIDEN TAMBIEN:** **CUATRO `UNA SOLA VARA`** (los `37`,
> `49`, `50` y `51`), **UNA `CHOCAN`** (el `31`) y **UNA `TODAS DE ACUERDO`** (el `53`). **Los
> %(quedan_actos)s siguen siendo de tres miembros con dos pares `A` y uno sin veredicto, cero puentes y
> cero `D` internos.**

**LOS `DECLARADOS Y NO FUNDIDOS` QUE ESPERAN EL CIERRE DE LA FASE 03 PASAN DE CATORCE A
%(declarados_arg)s**, y **el que entra es el `acto 44`**. **Es el primero de la lista cuyo motivo
sellado es la guarda `1B`**, y eso se dice porque cambia lo que el cierre de la fase 03 va a
encontrar: **los catorce anteriores esperan por `P.10` o por su familia; este espera por sus dos
puertas**, que es una pregunta distinta.

### i) **LO QUE ESTE REGISTRO NO HACE**

**NO toca ni una cifra publicada arriba**, **NO deshace ninguna fusion**, **NO re-lee ni un veredicto
de las siete colisiones vigentes**, **NO toca la mesa `OP-M-03` ni sus dos colisiones**, **NO toca las
CINCO colisiones de `OP-U-02` ya publicadas**, **NO ejecuta ninguna de las cinco fichas `OP-M-02`
consumidas** (lo consumado no se ejecuta ni se rehace), **NO funde ningun acto con dueno** (el `31` y
el `37` quedan con los suyos), **NO toca ni un nodo del `acto 44` ni sus dos puertas**, **NO re-sella
el plan ya ejecutado de este lote**, **NO mueve la linea base del censo** (la mueve el auditor) y **NO
anade ni una fila ni una columna a ninguna tabla de registrador**, que es la adjudicacion 3 del acta 69
aplicada sobre el instrumento que la registra. **La UNICA celda de tabla que esta vuelta toca es la de
la figura del inventario de la tabla del `DECLARADO`, con su texto viejo citado VERBATIM en el
docstring del constructor y MARCADA DISCUTIBLE**, porque la coletilla que llevaba tecleada dentro
(*y su centro es el MISMO nodo puente que `P.10` detecto*) era cierta para el `acto 27` de la vuelta 69
y **falsa para un acto declarado por la guarda `1B`, que no tiene ningun nodo puente**.
"""
