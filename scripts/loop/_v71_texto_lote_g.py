# -*- coding: utf-8 -*-
"""_v71_texto_lote_g.py . EL TEXTO EDITORIAL DEL REGISTRO DEL LOTE G.

NO ES UN INSTRUMENTO: es el texto. La maquina que lo arma, lo coteja y lo adosa
es scripts/loop/vuelta71_registro_lote_g.py, que lo importa. Mismo reparto que
_v67_texto..., _v68_texto_lote_d.py, _v69_texto_lote_e.py y _v70_texto_lote_f.py.

NI UNA CIFRA TECLEADA Y NI UN NUMERO DE LINEA TECLEADO: las cifras entran como
%(clave)s y salen de una salida de esta vuelta leida por expresion regular; las
citas de linea entran como [[CLAVE]] y salen de buscar su aguja de contenido.
Las tablas entran armadas del PLAN SELLADO o recortadas de la salida del
tallador.
"""

TEXTO = """

---

## `OP-U-02, TRAMO UNICO: EL REGISTRO DEL LOTE G` (2026-08-26, vuelta 71)

**Se cuelga de la cabecera de tramo que la vuelta 65 adoso** (linea **[[PAG_TRAMO_CABECERA]]**,
derivada hoy por aguja) **y se adosa al final del documento sin reescribir ni una linea de arriba.**
El lote `D` esta en la **[[PAG_LOTE_D]]**, el `E` en la **[[PAG_LOTE_E]]** y el `F` en la
**[[PAG_LOTE_F]]**.

**EL LOTE ABRE EN EL `ACTO 38`, QUE ES EL PRIMERO DEL TRAMO SIN DUENO MEDIDO, Y LOS DOS SALTOS VAN
DECLARADOS CON SU CITA**, que es lo que la adjudicacion 2 del acta 69 manda (registrada en esta misma
pagina, linea **[[PAG_ADJ_ACTO31]]**): el `acto 31` **TIENE DUENO MEDIDO** (`OP-F-04-WEI` y
`OP-S-04`) y el `acto 37` tambien (`OP-S-07`), **ninguno de los dos es una fusion de `OP-U-02`**, asi
que **no estan en la cola de fusiones de esta operacion** y saltarlos **no rompe el prefijo sin
saltos**. Su destino queda **con sus duenos en sus fases**.

**SE DECLARARON CINCO ACTOS Y 15 NODOS, Y SE ENTREGARON LOS CINCO.** **LOS CINCO CIERRAN FUNDIDOS Y
NINGUNO CIERRA `DECLARADO Y NO FUNDIDO`**, que es el segundo lote seguido del tramo sin ningun
declarado.

| acto | miembros | cierra | **FORMA medida** | superviviente |
|---:|---:|---|---|---|
| **38** | 3 | **FUNDIDO** | `UNA SOLA VARA` | `segmentos_de_clientes_problema_necesidad` |
| **39** | 3 | **FUNDIDO** | `UNA SOLA VARA` | `defensas_en_profundidad_3` |
| **40** | 3 | **FUNDIDO** | `UNA SOLA VARA` | `traction_goal` |
| **41** | 3 | **FUNDIDO** | `TODAS DE ACUERDO` | `design_for_six_sigma_dfss` |
| **42** | 3 | **FUNDIDO** | `UNA SOLA VARA` | `equipo_multifuncional_real` |

**EL TOPE DEL PREFIJO NO ES ESTRUCTURAL SINO DE LOTE, Y SE DICE EN VEZ DE DEJARLO COMO UN NUMERO
ELEGIDO:** el siguiente es el **`acto %(siguiente)s`**, **que TIENE DUENO** y por eso vuelve a
saltarse cuando el prefijo se reabra; el primero **sin dueno y sin puerta** de lo que queda es el
**`acto 43`**, y el tope de este lote cae antes de el **porque el encargo fija CINCO actos**, no
porque el `43` tenga nada que lo impida.

**LOS CUATRO MOTIVOS SELLADOS DEL `DECLARADO Y NO FUNDIDO`, RECORRIDOS UNO A UNO SOBRE ESTE LOTE**,
porque un motivo que no se usa se cuenta como usado si nadie lo dice:

| motivo sellado | sobre este lote |
|---|---|
| el triangulo de `P.10` (linea **[[PAG_ACTO1_P10]]**) | **SIN SUJETO**: **%(actos_sin_puente)s de %(actos_mirados)s** actos de lo que queda del tramo sin ningun nodo puente, medido en esta vuelta |
| la guarda `1B` con DOS o mas puertas (linea **[[PAG_GUARDA_1B]]**) | **PASA POR VACIO en los cinco**: **CERO** puertas dentro de cada acto, medido contra el universo protegido de **256** ids |
| la respuesta *DOS FAMILIAS* de `P.5` (linea **[[PAG_P5_MOTIVO]]**) | **NO SE USO**: los cinco contestaron **UNA familia**, y en el `acto 39` la contesta una decision aprobada y no una lectura del ejecutor |
| el `D` directo interno (linea **[[PAG_CUARTO_MOTIVO]]**) | **SIN SUJETO**: **CERO** pares `D` internos en los cinco y en los **%(quedan_actos)s** que quedan, medido |

> **Y LA CUENTA DE LOS MOTIVOS POSIBLES YA NO ES CUATRO SINO DOS EN LO QUE RESTA DEL TRAMO**, por la
> adjudicacion 4 del acta 70 registrada en esta misma pagina (linea **[[PAG_ADJ_PUERTAS]]**): quedan
> **la guarda `1B`** (con el `acto 44` como sujeto medido, que trae DOS puertas) y **la respuesta
> *DOS FAMILIAS* de `P.5`**. **`P.10` y el cuarto motivo estan sin sujeto y se dice.**

### a) **EL `ACTO 38`: LA ESCALA DEL PROBLEMA DEL CLIENTE, Y EL CHOQUE MAS ANCHO DEL LOTE ENTRE EL CONTENIDO Y EL CABLEADO**

**Tres miembros del mismo libro** (*The Startup Owner's Manual*, de Blank), **dos pares internos con
veredicto y los dos en `A`** (**547** y **1216**), **cero `D`, cero puentes, cero triangulos y cero
puertas.** El **1216** se titula *la escala del problema contada dos veces* y cierra midiendo que
**la misma escala de cuatro niveles aparece ya en TRES etiquetados distintos en esta zona**.

**LA FORMA ES `UNA SOLA VARA`:** la de **pasos** apunta al superviviente (5 contra 4 y 4) y la de
**condiciones** empata en 2 a tres bandas. **UNA SOLA VARA DE CONTENIDO NO EMPATADA BASTA** (acta 53,
pregunta 4), **y las DOS razones escritas apuntan al mismo nodo**.

> **EL CABLEADO APUNTA AL OTRO LADO Y CON EL MARGEN MAS ANCHO DEL LOTE POR ESTA VIA: 12 contra 5 y
> 4**, a `customer_segments_hypothesis`. **La cifra sale de la columna `cab` del instrumento de
> varas**, que es la unica fuente de cifra de cableado desde la adjudicacion 3 del acta 70 (linea
> **[[PAG_ADJ_CABLEADO]]**). **`P.8` es regla de PRELACION y el cableado solo habla a contenido
> empatado**, y aqui el contenido no empata. **Va marcado discutible en el reporte y el costo se paga
> en redirecciones.**

**El nodo crece de %(p38a)s pasos a %(p38b)s y de %(c38a)s condiciones a %(c38b)s.**

**LOS DOS `INCISO` VAN A PASOS DISTINTOS Y NINGUNO SE APILA** (acta 64): al **paso 2**, el cuarto
nivel de la escala que el superviviente no tiene (*aun no existe y tu le muestras una vision*), que
es la perdida que el **1216** sella con las palabras *el cuarto nivel es distinto*; y al **paso 3**,
*la intensidad del dolor que causa el problema*, que es el parametro del gesto de decidir si el
producto es indispensable.

%(rep38)s

%(abs38)s

%(per38)s

### b) **EL `ACTO 39`: EL RACIMO DE LAS DEFENSAS EN PROFUNDIDAD, DOS RAZONES QUE CORONAN DISTINTO Y UNA FAMILIA APROBADA POR LA MESA**

**Tres miembros del mismo libro** (*Managing the Risks of Organizational Accidents*, de Reason),
**dos pares internos con veredicto y los dos en `A`** (**2236** y **2283**), **cero `D`, cero puentes,
cero triangulos y cero puertas.** El **2283** cierra declarando **racimo de las defensas en
profundidad, tres miembros y sin una sola arista**.

> **LA PREGUNTA DE `P.5` NO LA CONTESTA UNA LECTURA DEL EJECUTOR, Y ESO ES LO PRIMERO QUE SE DICE:**
> `INVENTARIO.jsonl` trae una entrada de tipo `familia_de_ids` llamada `defensas_en_profundidad` con
> **LOS TRES miembros del acto** y con esta nota, leida hoy: *DECISION 4 de la mesa de racimos,
> aprobada el 9 ago 2026: familia unica, fusion con alias*. **UNA familia, y lo dice el archivo con
> visto del fundador.**

**LAS DOS RAZONES CORONAN SUPERVIVIENTES DISTINTOS, Y VA DICHO ENTERO:** el **2236** cierra con
*sobrevive `defensas_en_profundidad`* y el **2283** con *sobrevive `defensas_en_profundidad_3`*. **Las
dos coronaciones son sobre SU propio par y las dos matan al mismo nodo**, `defensas_en_profundidad_2`;
**el par que falta, el unico sin veredicto del acto, es exactamente el que enfrentaria a los dos
coronados.** **Es la misma forma que el `acto 34` del lote `F`**, que el acta 70 adjudico `A FAVOR` en
su `D6`. **Ninguna razon escrita se desmiente** al fundir a favor de `defensas_en_profundidad_3`,
porque el **2236** dice que `defensas_en_profundidad` gana **a `defensas_en_profundidad_2`** y no dice
nada sobre el tercero.

**LA FORMA ES `UNA SOLA VARA`:** la de **pasos** apunta al superviviente (4 contra 3 y 3) y la de
**condiciones** empata en 2. **Y HAY CONTENIDO ADEMAS DE LA CUENTA:** el **2283** declara una **FIGURA
NUEVA** con nombre propio, *el hermano que corrige al hermano*, y la mide: el paso 2 del superviviente
(*evaluar si existen dependencias ocultas entre capas que se asumen independientes*) es **exactamente
lo contrario** de evaluar cada capa *de forma independiente*, y su paso 4 (la complacencia operativa)
es **el reverso** del principio de redundancia que el otro predica.

> **EL CABLEADO APUNTA AL OTRO LADO Y CON EL MARGEN MAS ANCHO DEL TRAMO: 11 contra 3 y 2**, a
> `defensas_en_profundidad`, que tiene **nueve previos y cuatro siguientes**. La cifra sale de la
> columna `cab` del instrumento. **La letra manda igual**, y el propio banco lo tiene ejemplificado
> con *diez contra cinco, y pierde*. **Es el discutible mas fuerte del lote y va marcado.**

**El nodo crece de %(p39a)s pasos a %(p39b)s y de %(c39a)s condiciones a %(c39b)s. Es el acto que mas
crece del lote, junto con el 42, y va marcado por eso tambien.**

**EL UNICO `INCISO` VA AL PASO 1** y es la pieza que el **2236** nombra como el instrumento propio del
absorbido: *clasificandolas en las siete funciones defensivas*, que es lo que, con sus palabras,
*convierte la clasificacion en un procedimiento con casillas y no en una intencion*.

> **UNA CONSECUENCIA PUBLICADA PARA QUE `OP-S-09` NO SE LA ENCUENTRE:** tras esta fusion la familia
> `defensas_en_profundidad` queda con **UN solo id vivo**, y es `defensas_en_profundidad_3`, **el que
> lleva el sufijo numerico**. La verificacion de `OP-S-09` exige que ningun id vivo lleve sufijo
> numerico de duplicado: **le queda un renombre con alias, que es exactamente su tipo**. Esta
> operacion **no lo hace y no lo estorba**. **Y la frontera se declara en vez de estirarse:** la
> adjudicacion 2 del acta 70 (linea **[[PAG_ADJ_DUENO]]**) resolvio el caso de una entrada
> `familia_de_ids` sobre **PARTE** de la nomina; **esta cubre la nomina ENTERA**, y ese caso su letra
> **no lo dice**. **Se funde por el principio que esa misma letra enuncia, que es de TIPO y no de
> cobertura, y va como pregunta al auditor.**

%(rep39)s

%(abs39)s

%(per39)s

### c) **EL `ACTO 40`: LA META DE TRACCION, Y EL UNICO ACTO DEL LOTE DONDE EL CABLEADO NI SIQUIERA PODRIA DESEMPATAR**

**Tres miembros del mismo libro** (*Traction*, de Weinberg), **dos pares internos con veredicto y los
dos en `A`** (**627** y **824**), **cero `D`, cero puentes, cero triangulos y cero puertas.** El
**824** cierra midiendo que **la familia de la meta de traccion llega a TRES nodos y dos pares
leidos**, y anade *tres nodos para una sola idea, y ninguno enlaza a otro*.

**LA FORMA ES `UNA SOLA VARA`:** la de **pasos** apunta al superviviente (5 contra 4 y 3), la de
**condiciones** empata en 2 a tres bandas **y el cableado tambien empata, 3 a tres bandas**. **Es el
unico acto del lote en el que el cableado no podria desempatar ni aunque le tocara**, y se dice en vez
de dejarlo como un dato que nadie miro.

**NINGUNA RAZON CORONA A NADIE EN ESTE ACTO, Y ESO SE DICE EN VEZ DE FABRICARLE UNA CORONACION.** Lo
que si hay es una frase que apunta: el **627** cierra con que **el calendario con fechas y las fases
numeradas son lo mas concreto del par y es lo que se perderia**, y esas son las piezas del
superviviente.

**El nodo crece de %(p40a)s pasos a %(p40b)s y de %(c40a)s condiciones a %(c40b)s.**

**EL UNICO `INCISO` VA AL PASO 1** y es el parametro que las dos razones ponen en el centro: los
numeros concretos, *cantidad de clientes y tasa de crecimiento mensual*. **Los dos `APPEND` son los
dos gestos que las razones nombran como propios de cada absorbido**: la regla de descarte (*evaluar
cada actividad de marketing preguntando si mueve la aguja*) y el calculo previo por canal (*antes de
invertir en un canal, calcula si el volumen potencial puede acercarte realmente a tu meta*).

%(rep40)s

%(abs40)s

%(per40)s

### d) **EL `ACTO 41`: EL DESIGN FOR SIX SIGMA DE JURAN, EL ACTO MAS LIMPIO DEL LOTE Y EL UNICO QUE NO HACE CRECER A SU SUPERVIVIENTE**

**Tres miembros del mismo libro** (*Juran's Quality Handbook*, de Defeo), **dos pares internos con
veredicto y los dos en `A`** (**2465** y **2547**), **cero `D`, cero puentes, cero triangulos y cero
puertas.**

**EL SUPERVIVIENTE ESTA DECLARADO VERBATIM EN LAS DOS RAZONES:** el **2465** y el **2547** cierran los
dos con *sobrevive `design_for_six_sigma_dfss`*, y el **2547** anade que **ningun par leido lo ha hecho
perder** y lo llama **tercera candidata a ganador por derecho del dominio**. **La forma es `TODAS DE
ACUERDO`** y las tres cuentas apuntan al mismo sitio: pasos 6 contra 5 y 5, condiciones 4 contra 2 y 3,
cableado 12 contra 3 y 3, leido de la columna `cab` del instrumento.

**EL NODO NO CRECE NI UN PASO NI UNA CONDICION: se queda en %(p41b)s pasos y %(c41b)s condiciones**, y
**es el unico acto del lote asi**. **La razon esta medida y no es pereza:** las **diez** piezas de paso
de los dos absorbidos son las cinco letras de `DMADV` contadas dos veces, y las dos razones dicen que
estan **todas** dentro de los seis pasos del superviviente. **Y los cero `INCISO` tambien tienen su
razon medida, y es la puntuacion** (carril del `D5` del acta 66): **los SEIS pasos del superviviente
terminan en punto**, los seis, comprobado leyendolos, asi que cualquier `INCISO` con nexo de coma
caeria en la guarda de la **JUNTURA ROTA**. **No se forzo ninguno.**

> **AQUI LA CIFRA ALTA DE PERDIDAS NO ES DESCUIDO SINO LO CONTRARIO:** donde no hay `APPEND` ni
> `INCISO`, **todo lo que el absorbido tenia de propio se cubre o se pierde, y lo que se pierde se
> NOMBRA**. **La mas pesada va con el motivo que su propio autor le puso:** el **2547** sella *perdida
> nombrada, motivo alcance* sobre **descubrir las necesidades ocultas del cliente**, y explica que *no
> es lo mismo que traducir las necesidades declaradas y es de donde sale la caracteristica
> innovadora*. **Esta operacion no la repone y no finge reponerla.**
>
> **Y NO HAY PERDIDA DE NOMBRE, Y LO COMPRUEBA LA RAZON Y NO EL EJECUTOR:** el **2465** cierra con que
> el titulo del superviviente dice *DFSS y metodologia DMADV*, **asi que la denominacion por la que se
> busca sigue en el texto**.
>
> **LA SEGUNDA ENTRADA DE INVENTARIO DEL LOTE, CITADA CON SU CONSECUENCIA:** hay una `familia_de_ids`
> llamada `design_for_six_sigma_dmadv` con `OP-S-09` en `operaciones` y con **DOS de los tres**
> miembros. **Es exactamente el caso que la adjudicacion 2 del acta 70 resolvio** (linea
> **[[PAG_ADJ_DUENO]]**), y se funde por ella. **La consecuencia se publica:** esa familia queda con
> **CERO ids vivos**, porque sus dos miembros son los dos absorbidos; su estado declarado era
> *pendiente, se resuelve por continua o repite*, y **esta fusion la resuelve por REPITE**, que es una
> de las dos salidas escritas. **No le estorba: le cierra el caso.**

%(rep41)s

%(abs41)s

%(per41)s

### e) **EL `ACTO 42`: EL EQUIPO MULTIFUNCIONAL DE COOPER, Y EL UNICO ACTO DEL TRAMO DONDE DECIDE LA VARA DE CONDICIONES SOBRE UN EMPATE DE PASOS**

**Tres miembros del mismo libro** (*Winning at New Products*, de Cooper), **dos pares internos con
veredicto y los dos en `A`** (**476** y **672**), **cero `D`, cero puentes, cero triangulos y cero
puertas.** El **672** los llama **gemelos del mismo libro sobre el mismo problema, sin arista entre
ellos**, y resume el acto en una linea: **el eje es el mismo, el lider de verdad y el equipo de
verdad**.

**LA FORMA ES `UNA SOLA VARA`, Y LA VARA QUE HABLA NO ES LA DE PASOS:** la de **pasos EMPATA en 5**
entre los otros dos miembros y **no apunta a nadie**; la de **condiciones apunta al superviviente** (3
contra 2 y 2). **UNA SOLA VARA DE CONTENIDO NO EMPATADA BASTA**, y la de condiciones es vara de
contenido igual que la de pasos.

> **VA DICHO LO INCOMODO EN VEZ DE MEDIO: EL SUPERVIVIENTE ES EL MIEMBRO MAS PEQUENO DEL ACTO**, por
> pasos (4 contra 5 y 5) **y por cableado** (2 contra 5 y 4, leido de la columna `cab`). **Gana por la
> unica vara de contenido que no empata**, y el cableado no habla porque el contenido no empata. **Va
> marcado discutible.**
>
> **LO QUE LO SOSTIENE ADEMAS DE LA CUENTA ES CONTENIDO DECLARADO POR EL ARCHIVO:** el **672** dice
> con todas sus letras que **lo que se perderia si se fusiona mal son las dos condiciones materiales
> del segundo, liberar tiempo y recompensar por equipo, que son las unicas que convierten el aviso en
> algo ejecutable**. **Ese segundo es el superviviente y esas dos piezas son sus pasos 2 y 3.** Elegir
> a cualquiera de los otros dos obligaria a repescar por `APPEND` exactamente las dos piezas que la
> razon llama las unicas ejecutables.

**El nodo crece de %(p42a)s pasos a %(p42b)s y de %(c42a)s condiciones a %(c42b)s.**

**DOS PIEZAS VAN A UNA CONDICION DEL SUPERVIVIENTE Y NO A UN PASO, Y ESO SE DICE PORQUE ES UNA LECTURA
Y NO UN ATAJO:** los pasos 1 de los dos absorbidos describen **la composicion multiarea del equipo**,
y el superviviente la nombra en su **condicion 1** y **nunca como paso**: da la composicion por
supuesta y empieza por el lider. **Las dos van marcadas contra esa condicion y las dos sellan su
perdida.**

%(rep42)s

%(abs42)s

%(per42)s

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
| **el reanclaje, corrido ENTRE la fusion y `run_phase1`** | **%(reanclaje)s**, y no es un cero: el fundidor ya habia redirigido **%(redirecciones)s** referencias vivas y **quedaba una fuera del grafo** |
| **el diff de duplicadas, por instrumento** | **GRUPOS FABRICADOS DE VERDAD: %(dup_fab)s**, renombrados **%(dup_ren)s**, y los grupos pasan de **%(dup_antes)s** a **%(dup_despues)s** |
| **Gate 0 con su ciclo de TRES** | **`OK`**: **%(gate_activos)s** activos y **%(gate_deprecados)s** deprecados |

**EN CIFRAS DEL INSTRUMENTO:** **%(mueren)s nodos mueren** (**%(antes_vivos)s** vivos a
**%(despues_vivos)s**), **%(tocados)s ficheros tocados**, **%(piezas)s piezas repartidas**
(**%(enteras)s** enteras y **%(yadichas)s** ya dichas) y **%(per_total)s perdidas selladas en campo
propio**.

**LOS GRUPOS DE DUPLICADAS QUE DESAPARECEN ESTAN EXPLICADOS Y NO SON UN CERO MUDO:** son **siete**, y
los siete son de la misma especie: **un vivo que apuntaba a DOS miembros del mismo acto en el mismo
campo**, y que tras la fusion **hereda el destino una sola vez**. **`P.16` los limpio en la misma
corrida** y el diff por instrumento mide **CERO fabricados** y **CERO renombrados**.

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
| **`CALZA`** | **`%(col_calza)s`** |
| auto-pares, medidos al cierre | **%(autopares)s** |

> **LA LINEA BASE QUE ESTE LOTE USO ES `%(col_base)s`, Y ENTRO POR EL DEFECTO DEL INSTRUMENTO**, por
> la adjudicacion 1 del acta 70 y la correccion declarada que esta vuelta aplico en su `TAREA 1`
> (linea **[[PAG_ACTA70_BASE]]**). **No hizo falta pasarla a mano, y la guarda la MIDIO sobre el arbol
> antes de usarla:** si el censo de antes no calzara con la base declarada, el instrumento caeria en
> `ROJO` y diria *la base se mide, no se supone*. **Las dos colisiones de la mesa `OP-M-03` y las
> CINCO de `OP-U-02` ya publicadas siguen vigentes con su duena y no se tocan.**

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
practica que sale de la caida de reporte del acta 70: de los **%(quedan_actos)s** que quedan, **CUATRO
traen puerta** y van nombrados uno a uno. El **`31`** una (y ademas tiene dueno), el **`44` DOS**, el
**`46`** una y el **`51`** una. **El `44` cerrara `DECLARADO` por la guarda `1B` cuando el prefijo lo
alcance, y el `46` y el `51` funden con su puerta sobreviviendo** (acta 54, pregunta 1), **por la
adjudicacion 4 del acta 70** (linea **[[PAG_ADJ_PUERTAS]]**).

### i) **LO QUE ESTE REGISTRO NO HACE**

**NO toca ni una cifra publicada arriba**, **NO deshace ninguna fusion**, **NO re-lee ni un veredicto
de las siete colisiones vigentes**, **NO toca la mesa `OP-M-03` ni sus dos colisiones**, **NO toca las
CINCO colisiones de `OP-U-02` ya publicadas**, **NO ejecuta ninguna de las cinco fichas `OP-M-02`
consumidas** (lo consumado no se ejecuta ni se rehace), **NO funde ningun acto con dueno** (el `31` y
el `37` quedan con los suyos), **NO toca el `acto 44` ni sus dos puertas**, **NO mueve la linea base
del censo** (la mueve el auditor y esta vuelta solo aplico la correccion encargada) y **NO anade ni
una fila ni una columna a ninguna tabla de registrador**, que es la adjudicacion 3 del acta 69
aplicada sobre el instrumento que la registra.
"""
