# -*- coding: utf-8 -*-
"""_v67_texto_lote_c.py . EL TEXTO EDITORIAL DEL REGISTRO DEL LOTE C.

NO ES UN INSTRUMENTO: es el texto. La maquina que lo coteja, le mete las tablas
generadas del plan sellado y lo adosa es scripts/loop/vuelta67_registro_lote_c.py.
Vive aparte por la misma razon por la que el contenido de un lote vive aparte del
generador: para que el fichero que MIDE y el fichero que DICE no se confundan.

LAS MARCAS DE FORMATO SON LAS CELDAS QUE NO SE TECLEAN. Ni un porcentaje literal
puede entrar aqui sin doblarse, porque este texto se pasa por el operador de
formato; por eso no se usa ninguno.
"""

TEXTO = """

---

## `OP-U-02, TRAMO UNICO: EL REGISTRO DEL LOTE C` (2026-08-25, vuelta 67)

**Bajo la cabecera de tramo que la vuelta 65 adoso** (linea **3732** de esta pagina, cotejada hoy) y
**adosado al final sin reescribir ni una linea de arriba**. **EL LOTE SE DECLARO AL ABRIRLO Y ES
PREFIJO SIN SALTOS** del `orden_universo` de lo que quedaba (el lote A cerro los actos **1** y **3**,
el lote B cerro los actos **5**, **7**, **8**, **9**, **10** y **11**): **los actos 12, 13, 14, 15,
16 y 17, SEIS actos y 30 nodos, los seis cerrados ENTEROS.**

| acto | miembros | cierra | superviviente |
|---:|---:|---|---|
| **12** | 5 | **`DECLARADO Y NO FUNDIDO`**, y su motivo NO tiene letra: **PENDIENTE DE DOCTRINA** | ninguno se elige |
| **13** | 5 | **`DECLARADO Y NO FUNDIDO` por la guarda `1B`** | ninguno se elige |
| **14** | 5 | **`DECLARADO Y NO FUNDIDO` por `P.5`** | ninguno se elige |
| **15** | 5 | **`DECLARADO Y NO FUNDIDO` por la guarda `1B`** | ninguno se elige |
| **16** | 5 | **FUNDIDO** | `encuadre_desafio_diseno` |
| **17** | 5 | **`DECLARADO Y NO FUNDIDO` por `P.10`** | ninguno se elige |

> **UN LOTE CON UNA SOLA FUSION Y CINCO DECLARADOS, Y LA CIFRA SE PUBLICA EN VEZ DE MAQUILLARSE.** El
> contrato del lote es **PREFIJO CON TOPE, NO MINIMO** (acta 61, `D1` y pregunta 1), y **lo que la
> lectura da es lo que se entrega**. **Ninguno de los cinco declarados se declara por comodidad**:
> **dos por una guarda que prohibe la fusion**, **uno por la respuesta de `P.5`**, **uno por el
> triangulo de `P.10`** y **uno por una situacion que ninguna letra cubre y que va nombrada como
> tal**.

### a) **EL `ACTO 16`: LA FAMILIA DEL ENCUADRE DEL PROBLEMA (`HOW MIGHT WE`), Y LA PRIMERA VEZ QUE EL CABLEADO APUNTA AL OTRO LADO Y NO DECIDE**

| | |
|---|---|
| **superviviente** | `encuadre_desafio_diseno` |
| **absorbidos** | **4** |
| **nodos implicados / nodos que MUEREN** | 5 / %(mueren)s |
| **plan sellado** | [`../loop/PLAN_V67_OPU02_LOTE_C.json`](../loop/PLAN_V67_OPU02_LOTE_C.json), contrato **`CAMPO PROPIO v1`** |
| **vivos antes / despues** | %(antes_vivos)s / **%(despues_vivos)s** |

**LA PREGUNTA DE `P.5`, UNA FAMILIA O DOS, CONTESTADA CON MEDICION Y CON LAS RAZONES DELANTE:** los
**cinco** miembros tienen **CUATRO pares internos con veredicto escrito y los CUATRO son de clase
`A`**, hay **CERO pares `D` internos**, **CERO nodos puente** y **CERO triangulos**. **`P.10` solo
detiene una componente cuando aparece un triangulo `A` mas `A` mas `D`, y aqui no hay ninguno.**

**Y LAS CUATRO `A` ENCADENAN A LOS CINCO SIN UNA SOLA CONTRADICCION**, que es lo que separa una
familia leida de un cierre transitivo que solo cuenta: el puesto **525** encadena
`encuadre_desafio_diseno` con `how_might_we_framing`, el **264** encadena `how_might_we_framing` con
`how_might_we_hmw`, el **1319** encadena `how_might_we_hmw` con `how_might_we_briefs`, y el **236**
encadena `how_might_we_briefs` con `how_might_we_brief_social`.

> **EL PUESTO 1319 DECLARA LA UNION CON TODAS SUS LETRAS Y SE CITA EN VEZ DE RESUMIRSE:** *hasta hoy
> la familia HMW eran DOS componentes separadas*, y esa `A` *las UNE: por el cierre transitivo del
> banco 9.24 son ahora UNA SOLA de CINCO NODOS*. **El mismo veredicto nombra el gesto comun de los
> cinco**: *tomar el problema central, reformularlo con la formula de como podriamos, y CALIBRAR SU
> ALTURA para que no quede ni tan amplio que sea imposible de abordar ni tan estrecho que no deje
> espacio a soluciones*.

**EL SUPERVIVIENTE LO ELIGE EL CONTENIDO, Y AQUI EL CABLEADO APUNTA AL OTRO LADO:** la **FORMA
medida** es **`UNA SOLA VARA`**, la de **PASOS**, y apunta a `encuadre_desafio_diseno` con **5 contra
un maximo de 4**; la de **CONDICIONES empata en 2**. **El cableado apunta a `how_might_we_briefs`
con 8 contra 3, Y NO HABLA**, porque **`P.8` es regla de PRELACION**: *el desempate por cableado solo
habla a contenido empatado*, y **aqui el contenido dice algo**. **UNA SOLA VARA BASTA** (acta 53,
pregunta 4). **NI EL ROTULO SOLO NI LA CANTIDAD DECIDEN**: decide que `encuadre_desafio_diseno` es el
unico del acto que **ademas de formular la pregunta** define el impacto que se busca, documenta
contexto y restricciones, y manda revisar y ajustar la pregunta con lo aprendido. **NINGUN MIEMBRO DE
ESTE ACTO ES PUERTA**, medido al sellar.

#### EL REPARTO POR ABSORBIDO, TALLADO DEL PLAN SELLADO

%(abs16)s

#### EL REPARTO, PIEZA A PIEZA, TALLADO DEL PLAN SELLADO

%(rep16)s

> **LOS DOS `INCISO` DEL ACTO, Y POR QUE SON DOS Y NO MAS.** El superviviente viene del *field guide*
> de IDEO y **NO NOMBRA LA FORMULA** que le da nombre a la familia. **La formula viaja de `INCISO`
> adosado al paso 1, EXTRAIDA VERBATIM del paso 2 de `how_might_we_hmw`**, y el paso resultante se
> lee limpio porque **el paso 1 del superviviente no termina en punto**. **El segundo `INCISO` va al
> paso 5**, extraido VERBATIM del paso 3 de `how_might_we_framing`, y mete en el paso de revisar **lo
> unico que le faltaba: con quien se itera y cual es el criterio de parada**. **NO SE APILA MAS DE UN
> `INCISO` SOBRE EL MISMO PASO** (acta 64, registrada en esta pagina): los otros dos pasos que traen
> la formula, **el 1 de `how_might_we_framing` y el 2 de `how_might_we_briefs`**, van **`CUBIERTO`
> por el paso 1 y SIN perdida**, porque **el `INCISO` ya la trae**.

**EL SUPERVIVIENTE PASA DE %(p16a)s A %(p16b)s PASOS Y DE %(c16a)s A %(c16b)s CONDICIONES**, leido de
la salida de la ejecucion. **Piezas repartidas: %(piezas)s (%(enteras)s viajan enteras, %(yadichas)s
ya estaban dichas).**

#### LAS PERDIDAS, SELLADAS EN CAMPO PROPIO (`CAMPO PROPIO v1`), RECORTADAS DE LA SALIDA DEL TALLADOR

%(per16)s

> **UNA PERDIDA SE SELLA UNA SOLA VEZ CON SUS DOS SITIOS NOMBRADOS, Y VA MARCADO DISCUTIBLE.** El
> disparador de **PROYECTO DE INNOVACION** lo traen la condicion 1 de `how_might_we_framing` **y** la
> condicion 1 de `how_might_we_hmw`, y **es LA MISMA perdida vista desde dos nodos**. Lo mismo con la
> verificacion de la **FLEXIBILIDAD**, que traen el paso 3 de `how_might_we_brief_social` y el paso 3
> de `how_might_we_briefs`. **Se sellan UNA vez con los DOS sitios escritos en el campo `donde`**, en
> vez de dos, porque **inflar la cuenta de perdidas duplicando una sola tambien falsea el campo**.

#### LAS GUARDAS Y LOS CENSOS, LEIDOS DE LA SALIDA DE LA EJECUCION

| guarda | resultado |
|---|---|
| **guarda 1** (miembros vivos y nomina completa) | **OK** |
| **guarda `1B`** (ningun absorbido es semilla ni extremo de puente) | **OK** |
| **guarda 2** (cobertura exacta de indices, cero olvidos) | **OK** |
| **guarda 3** (cero repetidos literales en el resultado) | **OK** |
| **`P.16`**, duplicadas que la propia fusion fabrica y limpia **en el mismo commit** | **%(p16)s**, limpiadas en la misma corrida |
| **guarda A** (cero auto-aristas nuevas) y **guarda B** (cero duplicadas nuevas tras resolver) | **OK** las dos |
| **guarda C** (los campos que esta operacion NO redacta, intactos) y **guarda D** (los absorbidos conservan su texto INTACTO) | **OK** las dos |
| **pasivo historico del censo propio de la guarda** | **%(pasivo_antes)s a %(pasivo_despues)s** |
| **ficheros tocados** | **%(tocados)s** |

**EL DIFF DE DUPLICADAS, POR INSTRUMENTO Y CON LA APERTURA SACADA DE `git`**
([`../loop/SALIDA_V67_DIFF_DUPLICADAS.txt`](../loop/SALIDA_V67_DIFF_DUPLICADAS.txt)): **GRUPOS
FABRICADOS DE VERDAD: %(dup_fab)s**, renombrados **%(dup_ren)s**, y el censo de `OP-S-12` pasa de
**%(dup_antes)s a %(dup_despues)s** grupos.

**EL CENSO DE COLISIONES, CON LAS ESPERADAS MEDIDAS ANTES DE FUNDIR SOBRE LA LINEA BASE QUE EL ACTA
66 ADJUDICO** (registrada en la linea **4542** de esta pagina):

| | |
|---|---:|
| linea base declarada **y MEDIDA sobre el arbol de antes** | **%(col_base)s** |
| colisiones NUEVAS que la fusion fabricaria | **%(col_nuevas)s** |
| **ESPERADAS TRAS FUNDIR** | **%(col_esp)s** |
| **MEDIDAS al cierre por el censo** | **%(col_med)s** |
| **CALZA** | **%(col_calza)s** |

**`reanclar_por_resolutor.py` corrido ENTRE la fusion y `run_phase1`**: **%(reanclajes)s referencia
re-anclada**, y esta vez **no fue por vacio**: el rumbo `nucleo_quiero_algo_propio_sin_idea` apuntaba
a `how_might_we_hmw` y pasa a apuntar al superviviente. **Se corre siempre y se dice, en vez de darlo
por bueno.**

> **UNA CONSECUENCIA MEDIDA QUE SE DICE EN VEZ DE CALLARSE: LA COLA DE COSTURAS SUBE UNO.** De
> **1.447** a **1.448**, y **el que entra es `encuadre_desafio_diseno`**, el propio superviviente,
> **medido por diff contra la cola de la apertura sacada de `git`** y no supuesto. **Un nodo de 10
> pasos entrando a la cola de costuras internas es la consecuencia esperada de una fusion de cinco
> miembros**, y **queda enrutado a la fase 04 como el resto de la cola**.

### b) **EL `ACTO 12`: `DECLARADO Y NO FUNDIDO` POR ALGO QUE NINGUNA LETRA CUBRE, Y SE DICE ASI EN VEZ DE DISFRAZARLO DE MOTIVO CONOCIDO**

%(dec12)s

**LO PRIMERO QUE SE DICE ES QUE `P.10` NO SE DISPARA, medido y no supuesto:** **CERO nodos puente y
CERO triangulos**. **Y NINGUN MIEMBRO ES PUERTA**: la guarda `1B` pasa por vacio. **Con `P.10` sola y
con la guarda `1B` sola, este acto se fundiria**, y la FORMA habria apuntado a
`metrics_that_matter_framework`.

**LO QUE LO DETIENE ES EL PUESTO 1374, UN VEREDICTO `D` DIRECTO ENTRE DOS MIEMBROS:**
`cash_burn_calculation` contra `validacion_hipotesis_ingresos`, y su razon dice que los dos parten
del mismo dato, el ingreso neto de canal, y **salen por puertas distintas**: *uno responde cuanto
tiempo queda, el otro cuanto se puede gastar en traer al siguiente cliente*. **Una fusion de los
CINCO a un superviviente unico deprecaria a los dos contra el mismo vivo y SELLARIA QUE REPITEN ENTRE
SI**, que es exactamente lo que ese veredicto niega.

**LA FAMILIA ES UNA Y AUN ASI NO SE FUNDE, Y LAS DOS COSAS SE DICEN JUNTAS PORQUE NO SE
CONTRADICEN:** la pregunta de `P.5` se contesta **UNA**, y esta escrita con nombres propios en el
puesto **451**, que enumera **los CINCO** sobre el mismo modelo financiero del fin de la validacion,
sostenida por el **404** y el **807**. **Pero una familia con un `D` dentro es una familia
MEZCLADA**, que es el mismo nombre que el archivo usa en el puesto **863** para la familia de la
estrategia de innovacion cuando le entra su primer `D`. **FAMILIA NO ES FUSION:** la fusion exige
que **todos** los absorbidos REPITAN al superviviente.

**LAS CUATRO LETRAS QUE SOSTIENEN EL DECLARADO, cada una citable:**

| | la letra | |
|---|---|---|
| **PRIMERA** | **`P.10`** cierra con que **LO QUE NUNCA ES SALIDA ES FUNDIR LA COMPONENTE ENTERA PORQUE EL CIERRE TRANSITIVO LA JUNTA** | y aqui los dos nodos del `D` **solo coinciden en la componente por el camino** `cash_burn`, `metrics`, `verificar`, `validacion`: **la unica lectura DIRECTA entre ellos es el `D`** |
| **SEGUNDA** | **`P.12`** manda que el cierre transitivo convoque y **LA LECTURA DECIDA** | y la lectura decide **`D`** |
| **TERCERA** | el **acto 5 de la vuelta 66** (linea **4365** de esta pagina) se declaro porque fundir sellaria identidades **QUE NADIE LEYO** | y **aqui el caso es mas fuerte y no mas debil: alguien las leyo y dijo que no** |
| **CUARTA** | las **alternativas estan prohibidas por letra vigente** | leer los **4** pares que faltan es **cribado que esta fase no tiene** (banco 9.21), y fundir solo el subconjunto cerrado es una **FUSION PARCIAL** que el encargo prohibe con todas sus letras |

> **POR QUE NO ES PARADA Y SI ES PENDIENTE DE DOCTRINA:** **nada se toca, ningun nodo se depreca, es
> reversible entero y no desmiente ninguna lectura escrita**. La **regla 5** manda registrar lo mejor
> sostenido y seguir. **LO DISCUTIBLE, DICHO ANTES DE SABER SI ACIERTA:** el encargo de esta vuelta
> **enumera TRES motivos sellables** (el triangulo de `P.10`, la guarda `1B` y la respuesta *DOS
> FAMILIAS* de `P.5`) **y esa lista se puede leer como CERRADA**, y **leida asi este acto tenia que
> fundirse**.

### c) **LOS `ACTOS 13` Y `15`: LAS DOS PRIMERAS VECES DE LA CAMPANA EN QUE LA GUARDA `1B` ES EL MOTIVO UNICO**

**El carril lo escribio el acta 65 y esta pagina lo registro en la linea 4023:** *si aparece un acto
que no se pueda fundir sin absorber una puerta, cierra `DECLARADO` con la guarda `1B` como motivo,
SIN improvisar fusiones parciales que ninguna letra escribe*. **Hasta hoy ese carril existia y nadie
lo habia estrenado como motivo UNICO**: el acto 1 de la vuelta 65 tenia dos puertas, pero **su
motivo sellado fue `P.10`** y las puertas eran la segunda razon.

**El `acto 13`, la familia de la seleccion de canal de distribucion:**

%(dec13)s

> **LA PREGUNTA DE `P.5` SE CONTESTA IGUAL Y SE DEJA ESCRITA, porque el acto se lee entero aunque no
> se funda: ES UNA FAMILIA, y no es lectura de esta vuelta sino declaracion del archivo.** El puesto
> **609** dice **FAMILIA DECLARADA** y nombra el racimo *LA SELECCION DE CANAL* de seis miembros, el
> **762** lo repite, y el **1488** cierra que el racimo **NO crece**, sigue en **SEIS** miembros, su
> cobertura pasa a **8 de 15** con los ocho en `A`, y **sigue siendo SUB-PURO**.
>
> **Y UNA COSA MAS QUE SE DICE EN VEZ DE CALLARSE:** el puesto **537** declara un **CHOQUE CON LA
> DIRECCION DE FUSION DE LA RELECTURA `R1`** y avisa con todas sus letras de que **la direccion de
> fusion NO se puede cerrar par por par**, porque *fisico y digital son especializaciones que el nodo
> general NO lleva*. **No es el motivo sellado, pero apunta al mismo sitio que la guarda.**

**El `acto 15`, la familia de la ecuacion de valor de Rackham:**

%(dec15)s

> **Y SE DICE PRIMERO LO QUE ESTE ACTO NO ES, PORQUE SE PARECE Y NO LO ES: NO ES UN CHOQUE DE
> PUERTA.** En el choque, **la vara de contenido apunta a un miembro y la puerta es OTRO**, y el
> carril escrito manda **fundir A LA PUERTA y registrar el choque** (acta 54, pregunta 1, con el acto
> 9 de la vuelta 66 de precedente nuevo). **Aqui LAS TRES VARAS APUNTAN A LA PUERTA**
> (`prevencion_objeciones_vs_manejo`, con 6 pasos contra 4, 3 condiciones contra 2 y cableado 9
> contra 4), **o sea que no hay nada que chocar**. **Lo que hay es una SEGUNDA puerta dentro**,
> `ecuacion_de_valor`, **que cualquier fusion tendria que absorber**.
>
> **LA PREGUNTA DE `P.5` SE DEJA MEDIDA Y SIN CONTESTAR, Y ESO TAMBIEN SE DICE:** hay un nucleo de la
> ecuacion de valor de **cuatro** miembros que el archivo declara (puesto **217**, racimo nuevo de
> tres, y puesto **950**, que lo lleva a cuatro y **lo DEGRADA a SUB-PURO** con dos lecturas por
> hacer), y el quinto entra por el puesto **1146**, cuya razon avisa de que **no es un par de madre e
> hijo sino dos nodos laterales**. **Con la guarda `1B` deteniendo la fusion, la pregunta de si el
> quinto es de la misma familia NO HACE FALTA CONTESTARLA HOY y no se contesta**: se deja medida y
> escrita para quien la necesite.

### d) **EL `ACTO 14`: `DECLARADO Y NO FUNDIDO` POR `P.5`, Y ES EL SEGUNDO USO DEL CARRIL QUE EL ACTA 66 ADJUDICO**

%(dec14)s

**El precedente es el acto 5 de la vuelta 66** (linea **4365**) y **la letra esta registrada en la
linea 4518 de esta pagina**. **`P.10` NO se dispara** (cero `D`, cero puentes, cero triangulos) y
**ningun miembro es puerta**: con las dos solas, este acto se fundiria.

**LA PREGUNTA DE `P.5` SE CONTESTA SOBRE EL TEXTO ESTABLE Y LA RESPUESTA ES `NO ES UNA`: HAY UN PURO
DE CUATRO Y UN QUINTO QUE LA LECTURA DEJA FUERA CON TODAS SUS LETRAS.**

| | lo que el archivo dice, leido del dossier |
|---|---|
| **el PURO de CUATRO** | el puesto **1030** declara que *CON ESTE PAR NACE EL PRIMER PURO DE CUATRO* y **enumera la familia**: `construccion_de_leverage`, `leverage_en_negociacion_con_vcs`, `gestion_multiples_term_sheets` y `estrategia_competencia_vcs`, **CUATRO miembros, SEIS pares posibles, LOS SEIS LEIDOS Y LOS SEIS EN `A`**, y anade que es el **PRIMER PURO DE CUATRO MIEMBROS del archivo**. **Cuatro, no cinco** |
| **el quinto, y no esta fuera por olvido** | el puesto **878** lo levanta por el **BARRIDO DE LAS `A`** del banco 9.15, **lo mira y decide**, y su razon dice que **LA LECTURA LO DEJA FUERA PORQUE SU OBJETO ES COMO NEGOCIAR TERMINOS Y NO COMO GENERAR COMPETENCIA ENTRE INVERSORES**. El mismo puesto llama a `tecnica_anclaje_negociacion` **el paso cuatro contado como nodo**, sin procedimiento propio |

> **LA VARA APUNTA AL NODO EXCLUIDO, Y ESO NO ES UN DETALLE.** La FORMA medida es `CONTENIDO EMPATA`
> (pasos empatan en 5 a dos bandas y condiciones en 2 a dos bandas), asi que por `P.8` decidiria **el
> cableado solo**, y el cableado apunta a `tecnica_anclaje_negociacion` con **7 contra un maximo de
> 6**. **Fundir el acto entero pondria de superviviente al mismo nodo que la lectura saco de la
> familia**, y **sellaria que el PURO DE CUATRO repite a un nodo que el archivo declara de otro
> objeto**. **`P.12` manda que los veredictos DIRECTOS gobiernen**, y el directo aqui dice que **el
> objeto es otro**.

**LAS ALTERNATIVAS, RECORRIDAS EN VEZ DE ELEGIR LA COMODA:** leer los **3** pares que faltan es
cribado que esta fase no tiene; **fundir solo el PURO DE CUATRO y dejar fuera al quinto es una FUSION
PARCIAL**, que el encargo prohibe con todas sus letras; y **fundir entero desmiente la lectura del
878**. **ASI QUE NO SE FUNDE NADA Y SE DECLARA.**

### e) **EL `ACTO 17`: `DECLARADO Y NO FUNDIDO` POR `P.10`, CON SU TRIANGULO MEDIDO, Y CON UNA SEGUNDA RAZON INDEPENDIENTE**

%(dec17)s

**Es el PRIMERO de los seis actos con puente que el acta 66 dejo contados al cierre** (los actos 17,
20, 21, 23, 24 y 27). **El puente es `estrategia_de_innovacion_arenas`**, que tiene `A` con
`estrategia_de_innovacion_de_producto` y `A` con `estrategia_de_innovacion_y_tecnologia` siendo esos
dos `D` entre si (puesto **530**), y `A` con `estrategia_de_innovacion_y_tecnologia` y `A` con
`estrategia_innovacion_producto` siendo esos dos `D` entre si (puesto **863**).

> **LOS DOS `D` SON DE UNA PIEZA Y NO UN ACCIDENTE, Y LOS DOS HABLAN DEL MISMO NODO:** el **863** dice
> *LA MADRE Y SU PIEZA DE ARENAS* y declara que `estrategia_de_innovacion_y_tecnologia` **desarrolla
> con un procedimiento propio la UNA LINEA que la madre despacha**, con el metodo de seleccion, la
> frontera del alcance y el uso como filtro de gate que **no estan en ningun paso de la madre**. El
> **530** es una **CORRECCION DECLARADA del 13 ago 2026 por relectura conjunta encargada por el
> auditor**: era `A`, se midio paso por paso contra el grafo, **la afirmacion resulto FALSA** y paso
> a `D` por la vara del banco 9.6.1. **Una fusion entera desmentiria las dos.**

**Y HAY UNA SEGUNDA RAZON INDEPENDIENTE, QUE SE DICE EN VEZ DE CALLARSE:**
`estrategia_de_innovacion_y_tecnologia` **ES PUERTA**, y **no es el miembro al que apunta la vara**
(que es `seleccion_arenas_estrategicas`), asi que **cualquier fusion tendria que absorberla y la
guarda `1B` lo prohibe**. **Este acto tiene DOS motivos independientes, como el acto 1 de la vuelta
65, y no uno.**

> **UNA CITA QUE SE TRAE COMO CONTRASTE Y NO COMO FUENTE, Y LA DISCREPANCIA SE DECLARA EN VEZ DE
> RESOLVERSE COPIANDO** (regla 2): el puesto **460** dice que *esta familia ya esta declarada como
> racimo nuevo de SEIS nodos y se decide en mesa, no aqui*. **MEDIDO HOY CONTRA EL FICHERO DEL
> TRAMO**, este acto **NO tiene dueno en mesa ni en destejido** (el campo `duenos_mesa_o_destejido`
> esta vacio), que es **el criterio con el que `OP-U-02` abrio su universo en la vuelta 63**. **La
> razon habla de una mesa que ninguna operacion escrita nombra**, y **el acto cierra `DECLARADO`
> igual**, asi que **ninguna de las dos lecturas mueve un nodo**.

### f) **LO QUE QUEDA DEL TRAMO AL CIERRE DE ESTE LOTE, MEDIDO Y NO ARRASTRADO**

| | |
|---|---:|
| actos del tramo unico | **47** |
| cerrados por el lote A (vuelta 65) | **2** |
| cerrados por el lote B (vuelta 66) | **6** |
| **cerrados por el lote C (esta vuelta)** | **6** (1 fundido, 5 declarados) |
| **quedan** | **33 actos** |
| **nodos que quedan** | **109** |
| de los que quedan, con nodo puente | **5** (actos 20, 21, 23, 24 y 27) |
| actos `ABIERTOS` del recomputo al cierre | **%(abiertos)s** sobre **%(abiertos_n)s** nodos |

### g) **LO QUE ESTE REGISTRO NO HACE**

**NO toca ni una cifra publicada arriba, NO deshace ninguna fusion, NO re-lee ni un veredicto de las
cuatro colisiones vigentes, NO funde ningun acto con dueno, NO toca la mesa `OP-M-03` ni sus dos
colisiones, NO toca las dos colisiones de `OP-U-02` (que siguen vigentes y publicadas con su duena) y
NO ejecuta ninguna de las cinco fichas `OP-M-02` consumidas.**
"""
