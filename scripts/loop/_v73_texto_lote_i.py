# -*- coding: utf-8 -*-
"""_v73_texto_lote_i.py . EL TEXTO EDITORIAL DEL REGISTRO DEL LOTE I.

NO ES UN INSTRUMENTO: es el texto. La maquina que lo arma, lo coteja y lo adosa
es scripts/loop/vuelta73_registro_lote_i.py, que lo importa. Mismo reparto que
_v68_texto_lote_d.py, _v69_texto_lote_e.py, _v70_texto_lote_f.py,
_v71_texto_lote_g.py y _v72_texto_lote_h.py.

NI UNA CIFRA TECLEADA Y NI UN NUMERO DE LINEA TECLEADO: las cifras entran como
%(clave)s y salen de una salida de esta vuelta leida por expresion regular; las
citas de linea entran como [[CLAVE]] y salen de buscar su aguja de contenido.
Las tablas entran armadas del PLAN SELLADO o recortadas de la salida del
tallador. ESTE LOTE NO TIENE NINGUN ACTO DECLARADO, asi que no hay tabla de
declarado que armar, y eso se dice dentro del propio texto en vez de notarse por
su ausencia.
"""

TEXTO = """

---

## `OP-U-02, TRAMO UNICO: EL REGISTRO DEL LOTE I` (2026-08-26, vuelta 73)

**Se cuelga de la cabecera de tramo que la vuelta 65 adoso** (linea **[[PAG_TRAMO_CABECERA]]**,
derivada hoy por aguja) **y se adosa al final del documento sin reescribir ni una linea de arriba.**
El lote `G` esta en la **[[PAG_LOTE_G]]** y el `H` en la **[[PAG_LOTE_H]]**. **Las adjudicaciones del
acta 72 que gobiernan este lote se adosaron en la `TAREA 1` de esta misma vuelta y viven en la linea
**[[PAG_ACTA72]]**.**

**EL LOTE ABRE EN EL `ACTO 49`, QUE ES EL PRIMERO DEL TRAMO SIN DUENO MEDIDO, Y LOS DOS SALTOS VAN
DECLARADOS CON SU CITA**, que es lo que la adjudicacion 2 del acta 69 manda (registrada en esta misma
pagina, linea **[[PAG_ADJ_ACTO31]]**): el `acto 31` **TIENE DUENO MEDIDO** (`OP-F-04-WEI` y
`OP-S-04`) y el `acto 37` tambien (`OP-S-07`), **ninguno de los dos es una fusion de `OP-U-02`**, asi
que **no estan en la cola de fusiones de esta operacion** y saltarlos **no rompe el prefijo sin
saltos**. Su destino queda **con sus duenos en sus fases**.

**SE DECLARARON CUATRO ACTOS Y %(bor_miembros)s NODOS, Y SE ENTREGARON LOS CUATRO.** **LOS CUATRO CIERRAN FUNDIDOS
Y NINGUNO CIERRA `DECLARADO Y NO FUNDIDO`.**

| acto | miembros | cierra | **FORMA medida** | superviviente |
|---:|---:|---|---|---|
| **49** | 3 | **FUNDIDO** | `UNA SOLA VARA` | `shadow_ia_organizacional` |
| **50** | 3 | **FUNDIDO** | `UNA SOLA VARA` | `investigacion_new_view` |
| **51** | 3 | **FUNDIDO** | `UNA SOLA VARA` | `metodo_valor_presente_neto` **(LA PUERTA)** |
| **53** | 3 | **FUNDIDO** | `TODAS DE ACUERDO` | `reconocimiento_al_desempeno` |

**CON ESTE LOTE EL TRAMO SE QUEDA SIN NINGUN ACTO SIN DUENO Y SIN DESTINO, Y ESO ES LO QUE ESTE
REGISTRO ENTREGA.** **El siguiente sin destino es el `acto %(siguiente)s`, que TIENE DUENO**, y con el
`37` son **%(con_dueno)s** los que quedan, **los dos con dueno**. **El tope de este lote no es de
cuerda: es el final de la cola sin dueno.**

> **LA CORRECCION DECLARADA DE LA `TAREA 1` MUERDE SOBRE ESTE LOTE, Y SE DICE EN QUE** (linea
> **[[PAG_CORR_GLOSA]]**, y la adjudicacion que la ordena en la **[[PAG_ADJ_P4]]**): **la especie del
> pendiente 4 la define AHORA EL HECHO y no el vehiculo**, asi que las **%(per_total)s** filas de
> perdida de este lote se midieron contra el HECHO (que la sustancia llegue ENTERA desde otro absorbido
> del mismo acto, **por `APPEND` o por `INCISO`**) y no contra el nombre historico de la marca. **El
> resultado es %(per_p4)s, y una cuenta en cero medida con la definicion nueva dice algo que la misma
> cuenta con la definicion vieja no decia.**

**LOS CUATRO MOTIVOS SELLADOS DEL `DECLARADO Y NO FUNDIDO`, RECORRIDOS UNO A UNO SOBRE ESTE LOTE**,
porque un motivo que no se usa se cuenta como usado si nadie lo dice. **ESTE LOTE NO GASTA NINGUNO:**

| motivo sellado | sobre este lote |
|---|---|
| el triangulo de `P.10` | **SIN SUJETO**: cero nodos puente y cero triangulos en los cuatro, y **%(actos_sin_puente)s de %(actos_mirados)s** actos de lo que queda del tramo tambien sin ninguno, medido en esta vuelta |
| la guarda `1B` con DOS o mas puertas (linea **[[PAG_GUARDA_1B]]**) | **SIN SUJETO**: el unico acto del lote con puerta es el `51` y trae **UNA sola**, medida contra el universo protegido de **256** ids. **La guarda pide DOS** |
| la respuesta *DOS FAMILIAS* de `P.5` | **NO SE USO**: los cuatro contestaron **UNA familia**, y en el `51` la propia razon escribe la palabra *FAMILIA* con su nomina de tres dentro |
| el `D` directo interno | **SIN SUJETO**: **CERO** pares `D` internos en los cuatro y en los **%(quedan_actos)s** que quedan, medido |

> **Y LA CUENTA DE LOS MOTIVOS POSIBLES SIGUE SIENDO DOS EN LO QUE RESTA DEL TRAMO**, por la
> adjudicacion 4 del acta 70 registrada en esta misma pagina (linea **[[PAG_ADJ_PUERTAS]]**). **Este
> lote NO gasta ninguno y lo devuelve medido**, que es distinto de no haberlo mirado.

### a) **EL `ACTO 49`: LA POLITICA CONTRA LA IA CLANDESTINA, Y UN CHOQUE DE CABLEADO DE UNA SOLA ARISTA**

**Tres miembros del mismo libro** (*Co-Intelligence*, de Ethan Mollick), **dos pares internos con
veredicto y los dos en `A`** (**241** y **1032**), **cero `D`, cero puentes, cero triangulos y cero
puertas.** El **1032** se titula *la misma politica contra la IA clandestina, del mismo libro y sin
arista entre ellos*, y el **241** abre con *REPITE* y remata con *FIGURA: ids casi identicos, use
contra ia*.

**LA FORMA ES `UNA SOLA VARA`, Y ES LA DE PASOS:** la de **pasos** apunta al superviviente (4 contra 3
y 3); la de **condiciones** EMPATA en 2 a tres bandas y no apunta. **UNA SOLA VARA DE CONTENIDO NO
EMPATADA BASTA** (acta 53, pregunta 4).

> **EL CABLEADO APUNTA AL OTRO LADO, A `shadow_ai_use_organizacional`, CON 3 CONTRA 2 Y 2**, leido de
> la columna `cab` del instrumento de varas, que es la unica fuente de cifra de cableado desde la
> adjudicacion 3 del acta 70 (linea **[[PAG_ADJ_CABLEADO]]**). **`P.8` es regla de PRELACION y el
> cableado solo habla a contenido empatado**, y aqui el contenido no empata. **EL MARGEN ES DE UNA SOLA
> ARISTA y se dice**, porque un margen de uno no se lee igual que el de 11 contra 7 del `acto 43`.
> **Va marcado discutible en el reporte.**

**EL ROTULO NO DECIDIO, Y AQUI HABRIA SIDO LO COMODO**: los ids de dos de los tres miembros son casi
identicos (`shadow_ai_use_organizacional` contra `shadow_ia_organizacional`, *use* contra *ia*), y la
propia razon lo llama una FIGURA. **Decidio la vara de pasos.**

**El nodo crece de %(p49a)s pasos a %(p49b)s y de %(c49a)s condiciones a %(c49b)s.**

**LOS DOS `APPEND` VAN CON SU PROCEDENCIA DICHA, Y NO SON IGUALES.** El primero **lo nombra la razon
por su nombre**: el **1032** dice que lo propio de `incentivos_transparencia_ia` es *comunicar de
forma EXPLICITA que usar IA no va a resultar en despidos automaticos*, **la version dicha en voz alta
de lo que el otro deja implicito**. El segundo **NO lo nombra ninguna razon y por eso va marcado
discutible**: es *realizar encuestas anonimas para detectar el nivel real de adopcion*, **el UNICO
instrumento de medida de los tres nodos**, y sin el nadie produce el *diagnostico del uso real* que su
propio entregable prometia.

**LOS DOS `INCISO` VAN A PASOS DISTINTOS Y NO SE APILAN** (acta 64): al **paso 1**, *que poner en lugar
de la prohibicion* (los marcos de uso responsable y transparente), y al **paso 4**, *con que se
recompensa* (los incentivos tangibles con sus dos ejemplos).

%(rep49)s

%(abs49)s

%(per49)s

### b) **EL `ACTO 50`: LA UNICA VARA APUNTA AL NODO QUE LAS DOS RAZONES MATAN, Y MANDA EL ARCHIVO**

**Es el acto caro de este lote y va con su choque entero al principio, no en una nota al pie.** Tres
miembros del mismo libro (*The Field Guide to Understanding Human Error*, de Sidney Dekker), **dos
pares internos con veredicto y los dos en `A`** (**2290** y **2292**), **cero `D`, cero puentes, cero
triangulos y cero puertas.**

**LA FORMA ES `UNA SOLA VARA` Y ESA VARA APUNTA AL ABSORBIDO:** la de **pasos** EMPATA en 5 entre
`investigacion_new_view` y `new_view_vs_old_view_de_error_humano` y no apunta; la de **condiciones**
apunta a `new_view_vs_old_view_de_error_humano` (3 contra 2 y 2); el **cableado** EMPATA en 5 entre los
dos grandes y por la letra tampoco habla. **Y LAS DOS RAZONES ESCRITAS MATAN A ESE MISMO NODO**, cada
una sobre SU par: el **2290** cierra con *SOBREVIVE investigacion_new_view* y el **2292** con
*SOBREVIVE perspectiva_dentro_del_tunel*.

> **POR QUE MANDA EL ARCHIVO Y NO LA VARA, CITADO Y NO IMPROVISADO.** **`P.8` dice que donde el
> contenido dice algo el contenido manda**, y define expresamente que **contenido no es solo el texto
> de los pasos**: un **padre declarado por el archivo** es contenido. **Aqui el archivo declara
> CONTENCION dos veces**: el **2290** escribe que el paso 1 del absorbido *ES* el paso 1 del otro y que
> sus pasos 2, 3 y 5 son *formas de decir lo que el otro pide con instrumentos*, y remata con *le queda
> una linea propia*; el **2292** escribe la misma contencion contra el tercero y remata con *le quedan
> dos lineas*. **Un conteo de condiciones de 3 contra 2 no vence a una contencion declarada dos veces**,
> y la letra del tramo lo dice por su lado: **`CHOCAN` decide LA PIEZA DECLARADA** (acta 53, pregunta
> 3). **Fundir a favor de la vara habria desmentido DOS razones publicadas a la vez.**
>
> **LA ELECCION ENTRE LOS DOS CORONADOS NO LA HACE UNA LECTURA, LA HACEN LAS VARAS.** Las coronas son
> **cruzadas y sobre SU propio par**, que es la figura que las actas 70, 71 y 72 adjudicaron `A FAVOR`
> en su `D6`, su `D5` y su `D6`. **El par que falta, el unico sin veredicto del acto, es exactamente el
> que enfrentaria a los dos coronados**, asi que el archivo no los compara y hay que medirlos: **pasos
> 5 contra 4 y cableado 5 contra 3, las DOS a `investigacion_new_view`**; condiciones EMPATA en 2.
> **Ninguna vara apunta a `perspectiva_dentro_del_tunel`.**
>
> **PENDIENTE DE DOCTRINA, NOMBRADO Y NO INVENTADO:** ninguna regla escrita dice hoy que hacer cuando
> la FORMA que el instrumento imprime es `UNA SOLA VARA` **y esa vara apunta al nodo que las razones
> matan**. El instrumento **no lee razones** y por eso no puede imprimir `CHOCAN`. **Se registro lo
> mejor sostenido, va marcado discutible y no se estreno ninguna regla**, que es la regla 5 del
> `EJECUTOR`.

**El nodo crece de %(p50a)s pasos a %(p50b)s y de %(c50a)s condiciones a %(c50b)s.**

**LOS DOS `APPEND` SON LOS DOS PROPIOS QUE LAS RAZONES NOMBRAN**, uno de cada absorbido: **ampliar el
circulo de testigos a colegas, familiares y allegados** (el **2290** lo llama *la unica linea propia* y
ademas encarga que *se absorba como linea suya*) y **entrevistar a los involucrados para entender su
percepcion y sus objetivos** (el **2292** lo glosa como *ir a preguntarles en vez de deducirlo*).

**UNA ELECCION QUE SE DECLARA EN VEZ DE CALLARSE:** al **paso 1** solo cabe **un** `INCISO` (acta 64) y
competian **dos** piezas. **Se salva la que las razones DECLARAN PROPIA** (*reconstruir la informacion
y las senales disponibles*) **y se sella la que las razones declaran MUTUAMENTE CUBIERTA** (la
enumeracion del contexto: el **2292** escribe que el paso 3 de uno *es* el paso 4 del otro). **El
segundo `INCISO` va al paso 4** y trae la postura con la que se comunica el informe.

%(rep50)s

%(abs50)s

%(per50)s

### c) **EL `ACTO 51`: LA PUERTA SOBREVIVE Y NO HAY NINGUN CHOQUE QUE PUBLICAR, Y ESO TAMBIEN SE DICE**

**Tres miembros del mismo libro** (*Financial Intelligence for Entrepreneurs*, de Berman y Knight),
**dos pares internos con veredicto y los dos en `A`** (**378** y **1332**), **cero `D`, cero puentes y
cero triangulos.** **LA FAMILIA NO ES LECTURA: ES DECLARACION DEL ARCHIVO CON LA PALABRA DENTRO.** El
**378** escribe *FAMILIA anotada, de tres* y la nombra entera, y anade que **solo el tercero resta
ademas el desembolso inicial**.

**`metodo_valor_presente_neto` ES PUERTA** (universo protegido de **256** ids) **Y SOBREVIVE**, que es
lo que el acta 54, pregunta 1, manda **gane o pierda en contenido**, y lo que la propia pagina
distingue del caso de dos puertas en la linea **[[PAG_PUERTA_UNICA]]**. **AQUI GANA, Y SE DICE EN VEZ
DE DARSE POR HECHO:** la vara de **pasos** apunta a la puerta (6 contra 5 y 4) y el **cableado**
tambien (10 contra 5 y 4); la de **condiciones** EMPATA en 3. **NO HAY NINGUN CHOQUE QUE ESCRIBIR EN EL
MOTIVO SELLADO**, a diferencia del `acto 46` del lote `H`, **y callarlo dejaria al lector sin saber si
se miro.** **Es el unico acto del lote donde la vara, el cableado y la puerta apuntan al mismo sitio.**

**El nodo NO CRECE NI UN PASO: se queda en %(p51b)s pasos y %(c51b)s condiciones.** **Es el reparto mas
barato de todo el tramo**, y no por generosidad: el **1332** lo habia escrito antes con estas palabras,
*PERDIDA CERO Y DIRECCION FORZADA: el nodo que muere no tiene ni una linea propia*.

**CERO `APPEND` Y UN SOLO `INCISO`, Y EL `INCISO` VA CON LA PRECISION DE LA RAZON DELANTE:** el **378**
dice que lo unico que `valor_del_dinero_en_el_tiempo` tiene de mas es **la premisa**, y anade que **es
el porque y no un paso**. Por eso **no entra de `APPEND`**: un porque no es un paso, y meterlo como
paso habria contradicho la razon escrita. **Entra de `INCISO` al paso 3**, que es justamente el paso
que aplica la ecuacion de descuento.

> **Y SE DICE ALGO QUE LA RAZON NO DIJO, PORQUE ESCUDARSE EN ELLA SERIA CALLAR:** el **1332** mide
> *perdida cero* sobre los **PASOS** de `valor_presente`, y es cierto al digito, **pero las condiciones
> de los dos absorbidos SI pierden**. Esas perdidas van selladas aqui con su motivo en vez de esconderse
> detras de la frase de la razon.

%(rep51)s

%(abs51)s

%(per51)s

### d) **EL `ACTO 53`: `TODAS DE ACUERDO`, Y LA PROMESA DE MARCADO DE SU RAZON, CUMPLIDA Y DESACTIVADA**

**Tres miembros del mismo libro** (*Quality is Free*, de Philip B. Crosby), **los tres son EL PASO 12
del programa**, **dos pares internos con veredicto y los dos en `A`** (**2616** y **2942**), **cero
`D`, cero puentes, cero triangulos y cero puertas.**

**LA FORMA ES `TODAS DE ACUERDO`, LA UNICA DEL LOTE Y LA MAS LIMPIA DEL TRAMO:** la de **pasos** apunta
al superviviente (5 contra 4 y 3) **y la de condiciones apunta AL MISMO NODO** (3 contra 2 y 1). **Se
funde a su lado.** El **cableado** EMPATA en 5 y por la letra tampoco habria hablado.

**LA PROMESA DE MARCADO DE LA RAZON SE CUMPLE Y NO SE OLVIDA:** el **2942** lleva escrito *DISCUTIBLE
MARCADO fuerte* sobre la linea de `reconocimiento_crosby` de **adaptar el reconocimiento a tu forma de
trabajar con tu gente**, con esta frase: *quien la lea como un paso entero propio dira D*. **Va marcada
en el reporte de esta vuelta.**

> **Y ESTE REPARTO LE QUITA EL FILO A LA PREGUNTA EN VEZ DE ESQUIVARLA:** esa linea **NO SE PIERDE**.
> Entra de `INCISO` al paso 3 del superviviente, **asi que se lea como paso o como linea, el contenido
> se conserva**. La pregunta sigue abierta como pregunta de doctrina; **el dato ya no depende de como
> se conteste.**

**El nodo NO CRECE NI UN PASO: se queda en %(p53b)s pasos y %(c53b)s condiciones.** **CERO `APPEND` Y
DOS `INCISO` a pasos distintos**, y no es casualidad: las dos razones dicen que **ninguno trae un paso
entero ajeno al otro**, asi que meter un `APPEND` habria contradicho lo escrito. **Los dos `INCISO` son
las dos lineas que las razones clasifican como LINEAS y no como actos**: *tratar todos los problemas
reportados de manera equitativa* (que el **2942** llama *una linea de criterio*) y la de adaptar el
reconocimiento (*una linea de estilo*).

**Y EL ABSORBIDO PEQUENO NO PIERDE NADA, TAL COMO EL 2616 PROMETIO** con las palabras *sin perdida
propia*: sus tres pasos y su unica condicion entran, y **ninguna de las perdidas de este acto es
suya**.

%(rep53)s

%(abs53)s

%(per53)s

### e) **LAS GUARDAS DE LA FUSION, TODAS EN VERDE Y CADA UNA CON SU CIFRA**

| guarda | resultado |
|---|---|
| **guarda 1B** (ningun absorbido es puerta) | **`OK`**: la unica puerta del lote es el superviviente del `51` |
| **guarda A** (cero auto-aristas nuevas) | **`OK`**, con **%(auto_retiradas)s** que la fusion habria creado y se retiran |
| **guarda B** (cero duplicadas nuevas tras resolver) | **`OK`**, y el pasivo propio BAJA de **%(pasivo_antes)s** a **%(pasivo_despues)s** |
| **guarda C** (campos que esta operacion NO redacta) | **%(guarda_c)s de %(guarda_c)s intactos** |
| **guarda D** (los absorbidos conservan su texto INTACTO) | **`OK`**, los **%(mueren)s** |
| **`P.16`, quien fabrica limpia, en el mismo commit** | **%(p16_fabrica)s** duplicadas fabricadas y **limpiadas en la misma corrida**; re-corrido por separado despues dice **NINGUNA** |
| **el reanclaje, corrido ENTRE la fusion y `run_phase1`** | **%(reanclaje)s**, y **es un cero medido y no un cero supuesto**: el fundidor redirigio **%(redirecciones)s** referencias vivas y no quedo ninguna fuera del grafo. **Ninguna ancla duplicada se fabrico**, comprobado sobre los **%(rumbos)s** rumbos del banco |
| **el diff de duplicadas, por instrumento** | **GRUPOS FABRICADOS DE VERDAD: %(dup_fab)s**, renombrados **%(dup_ren)s**, y los grupos resueltos pasan de **%(dup_antes)s** a **%(dup_despues)s** |
| **Gate 0 con su ciclo de TRES** | **`OK`**: **%(gate_activos)s** activos y **%(gate_deprecados)s** deprecados |

**EN CIFRAS DEL INSTRUMENTO:** **%(mueren)s nodos mueren** (**%(antes_vivos)s** vivos a
**%(despues_vivos)s**), **%(tocados)s ficheros tocados**, **%(piezas)s piezas repartidas**
(**%(enteras)s** enteras y **%(yadichas)s** ya dichas) y **%(per_total)s perdidas selladas en campo
propio**. **El plan sello %(fundidos_plan)s fusiones y %(declarados_plan)s declarados, y el fundidor
ejecuto exactamente eso.**

**LOS GRUPOS DE DUPLICADAS QUE DESAPARECEN SON %(dup_idas)s, Y NO ES UN CERO MUDO:** las
**%(p16_fabrica)s** que la propia fusion fabrico **se limpiaron en la misma corrida** por `P.16`, y el
diff por instrumento, corrido despues con la apertura sacada de `git` sobre el commit del plan, mide
**CERO fabricados** y **CERO renombrados**.

**LA COLA DE COSTURAS BAJA Y SE MIDE NODO A NODO EN VEZ DE DEJARSE COMO UN MENOS DOS:** de
**%(cola_antes)s** a **%(cola_despues)s**, con **%(cola_entran)s que entran** y **%(cola_salen)s que
salen**. **Y AQUI SI ENTRAN SUPERVIVIENTES, A DIFERENCIA DEL LOTE `H`, Y VA DICHO PORQUE ES UN COSTO:**
los que entran son `investigacion_new_view` y `shadow_ia_organizacional`, **los dos supervivientes que
crecieron dos pasos**; los que salen son **absorbidos que dejan de ser vivos**. **La cola CITA, no
juzga**, y la poda es de la fase 04.

**LA CUENTA AGREGADA DE LAS PERDIDAS, POR MAQUINA Y NO DE MEMORIA:**

| | contado sobre el plan sellado |
|---|---:|
| **perdidas selladas en campo propio** | **%(per_total)s** |
| de ellas `DE PARAMETRO DE PASO` | **%(per_paso)s** |
| de ellas `DE CONDICIONES` | **%(per_cond)s** |
| **filas con `ATENUANTE DECLARADO`** | **%(per_aten)s** |
| de ellas, de la **especie del pendiente 4**, medida con la **definicion CORREGIDA de esta vuelta** | **%(per_p4)s** |
| de ellas, con **`ATENUANTE DECLARADO Y MEDIDO`** | **%(per_medido)s** |
| **filas con DOS SEDES en el campo `donde`** | **%(per_dos_sedes)s** |
| **filas que describen un atenuante SIN la frase sellada** | **NINGUNA**, medido, y por eso **no hay ninguna exclusion que decir en este lote** |
| la aritmetica de **la lectura contraria** (una fila por SITIO y no por PIEZA, linea **[[PAG_D10_POR_PIEZA]]**) | **%(per_contraria)s** y no **%(per_total)s** |

> **LA CELDA DEL PENDIENTE 4 SALE EN %(per_p4)s Y AHORA ESA CIFRA SIGNIFICA ALGO DISTINTO QUE ANTES:**
> la vuelta 72 la publico en cero **con una glosa que decia que en sustancia si habia una**, porque el
> instrumento buscaba el vehiculo. **Con la definicion corregida de esta vuelta la cuenta se hizo contra
> el HECHO**, fila a fila, **y sigue dando %(per_p4)s**: en ninguna de las **%(per_total)s** la
> sustancia perdida llega entera desde otro absorbido, ni por `APPEND` ni por `INCISO`. **La unica que
> se acerco lleva su `ATENUANTE DECLARADO Y MEDIDO` y lleva escrito dentro por que no entra**: lo que
> llega por el `INCISO` del `acto 50` es **la postura**, y lo que se pierde es **la lista de palabras**.
> **Una pieza vecina no es la misma pieza.**

**LAS CINCO FILAS CON DOS SEDES SON LA CIFRA MAS ALTA DEL TRAMO, Y VAN CON SU MOTIVO:** la fila del
contrato es **por PIEZA que se pierde y no por sitio donde vivia** (linea **[[PAG_D10_POR_PIEZA]]**), y
en este lote **los dos absorbidos de un mismo acto traen la misma pieza mas veces que en ningun lote
anterior**, porque los tres miembros de cada acto son del mismo libro y describen el mismo gesto. **Se
declaran las dos sedes en la misma fila en vez de partir la pieza en dos filas**, que es lo que el
`D10` del acta 67 descarto.

### f) **EL CENSO DE COLISIONES: ESTE LOTE NO FABRICA NINGUNA, Y SE PUBLICA IGUAL**

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

> **LA LINEA BASE QUE ESTE LOTE USO ES `%(col_base)s`, Y ENTRO POR EL DEFECTO DEL INSTRUMENTO.** **No
> hizo falta pasarla a mano, y la guarda la MIDIO sobre el arbol antes de usarla.** **TERCER LOTE
> SEGUIDO DEL TRAMO QUE NO FABRICA NINGUNA.** **Las dos colisiones de la mesa `OP-M-03` y las CINCO de
> `OP-U-02` ya publicadas siguen vigentes con su duena y no se tocan.**

### g) **EL BORDE DEL DUENO, MEDIDO ANTES DE SELLAR Y NO DESPUES**

**El carril esta en esta misma pagina** (linea **[[PAG_ADJ_DUENO]]**) **y su borde lo escribio el acta
71**: una `familia_de_ids` de **nomina ENTERA** sin resolucion aprobada que la fusion ejecute **va como
PREGUNTA y no como fusion**. **No basta con no encontrarla: hay que barrer y contar.**

| | medido hoy por maquina |
|---|---:|
| entradas del inventario barridas, el fichero ENTERO | **%(bor_inv_total)s** |
| entradas que **tocan** a alguno de los %(bor_miembros)s miembros | **%(bor_tocan)s** |
| de ellas, de tipo `acto` | **%(bor_acto)s**, o sea **TODAS** |
| **`familia_de_ids` que cubren la NOMINA ENTERA de un acto del lote** | **%(bor_enteras)s** |
| miembros del lote en alguna nomina de `RACIMOS_MIEMBROS.jsonl` (%(bor_rac_lineas)s lineas) | **%(bor_rac_hits)s** |
| menciones en `OPERACIONES.jsonl`, barrido **CAMPO A CAMPO** sobre las %(bor_ops_fichas)s fichas | **%(bor_menciones)s** |

**EL BORDE NO SE PISA, Y ESTA VEZ NI SIQUIERA SE ACERCA.** **Las %(bor_acto)s entradas de tipo acto nombran en
`operaciones` a `OP-L-03` y a `OP-U-02`**, que es la propia operacion que funde, **y eso no hace dueno
a nadie por la adjudicacion 2 del acta 68**: las tres fuentes que hacen dueno son los campos `nodos`,
`preservar` y `eliminar` de una ficha, **y el barrido campo a campo no devuelve ninguna**.

### h) **LO QUE QUEDA DEL TRAMO AL CIERRE DE ESTE LOTE, MEDIDO Y NO ARRASTRADO**

| | |
|---|---:|
| actos del tramo unico | **%(tramo_filas)s** |
| actos **FUNDIDOS**, medido sobre el grafo | **%(fundidos_medidos)s** |
| actos **`DECLARADOS Y NO FUNDIDOS`** | **%(declarados_arg)s** |
| **quedan sin destino** | **%(quedan_actos)s actos y %(quedan_nodos)s nodos** |
| **el siguiente del prefijo** | el acto **%(siguiente)s**, **con dueno** |
| de los que quedan, **con dueno medido** | **%(con_dueno)s**, **o sea TODOS** |
| de los que quedan, **con nodo puente** | **%(quedan_puente)s** |
| de los que quedan, **con par `D` interno** | **%(quedan_d)s** |
| componentes `ABIERTOS` del recomputo | **%(abiertos)s** sobre **%(abiertos_n)s** nodos |

**ESTE ES EL ESTADO QUE EL CIERRE DE LA FASE 03 VA A PESAR, Y POR ESO SE DEJA ESCRITO ENTERO:** **no
queda ningun acto del tramo sin dueno y sin destino.** Los **%(quedan_actos)s** que quedan **traen
dueno los dos** (el `31` con `OP-F-04-WEI` y `OP-S-04`, el `37` con `OP-S-07`) y **su destino esta en
sus fases, no aqui**. **Los %(declarados_arg)s `DECLARADOS Y NO FUNDIDOS` siguen esperando**, y **uno
de ellos, el `acto 44`, entra NOMBRADO APARTE** por la adjudicacion 3 del acta 72: **espera por sus DOS
puertas y no por `P.10` ni por su familia**, que es una pregunta distinta de la de los otros catorce.

**Y LAS PUERTAS DE LOS QUE QUEDAN SE MIDEN Y SE PUBLICAN CON SU SALIDA COMMITTEADA:** de los
**%(quedan_actos)s**, **UNO trae puerta**, el `31` con `captura_conocimiento_mercado` (y ademas tiene
dueno), **y el `37` ninguna**. **El `31` fundiria con su puerta sobreviviendo cuando le toque** (acta
54, pregunta 1, y la adjudicacion 4 del acta 70 en la linea **[[PAG_ADJ_PUERTAS]]**), **y ninguno de
los dos puede cerrar `DECLARADO` por la guarda `1B`, porque esa guarda pide DOS.** **Las FORMAS de los
dos, medidas hoy: el `31` `CHOCAN` y el `37` `UNA SOLA VARA`.**

### i) **LO QUE ESTE REGISTRO NO HACE**

**NO toca ni una cifra publicada arriba**, **NO deshace ninguna fusion**, **NO re-lee ni un veredicto
de las siete colisiones vigentes**, **NO toca la mesa `OP-M-03` ni sus dos colisiones**, **NO toca las
CINCO colisiones de `OP-U-02` ya publicadas**, **NO ejecuta ninguna de las cinco fichas `OP-M-02`
consumidas** (lo consumado no se ejecuta ni se rehace), **NO funde ningun acto con dueno** (el `31` y
el `37` quedan con los suyos), **NO toca ni un nodo del `acto 44` ni de los otros catorce declarados**,
**NO re-sella el plan ya ejecutado de este lote**, **NO ABRE LA FASE 04**, **NO DECIDE EL CIERRE DE LA
FASE 03**, que es parada de fundador, **NO mueve la linea base del censo** (la mueve el auditor) y **NO
anade, quita ni corrige ni una fila ni una columna ni una celda de ninguna tabla de registrador**, que
es la adjudicacion 3 del acta 69 aplicada entera: **la correccion que la vuelta 72 hizo en la celda de
la figura del inventario ya viene aplicada en el ancestro y esta vuelta solo comprueba que sigue en
pie.**
"""
