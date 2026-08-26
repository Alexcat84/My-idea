# -*- coding: utf-8 -*-
"""_v68_texto_acta67.py . EL TEXTO EDITORIAL DEL REGISTRO DEL ACTA 67.

NO ES UN INSTRUMENTO: es el texto. La maquina que lo coteja y lo adosa es
scripts/loop/vuelta68_registrar_acta67.py, que lo importa. Vive aparte por la
misma razon por la que el contenido de un lote vive aparte del generador: para
que el fichero que MIDE y el fichero que DICE no se confundan. Es el mismo
reparto que las vueltas 66 y 67 usaron con _v66_texto_acta65.py y
_v67_texto_acta66.py.

LA DIFERENCIA CON SUS DOS ANTECESORES, y es la correccion de la vuelta 68: AQUI
NO HAY NI UN NUMERO DE LINEA TECLEADO. Cada cita va como marca [[CLAVE]] y el
registrador la sustituye por el numero que le devuelve BUSCAR la aguja de esa
clave en su fichero. Un numero de linea escrito a mano en este fichero es
exactamente la especie que cayo en la vuelta 67.
"""

TEXTO = """

---

## LAS ADJUDICACIONES DEL ACTA DE LA VUELTA 67, REGISTRADAS AQUI PARA QUE EL REGISTRO NO DEPENDA DEL ACTA (26 ago 2026, vuelta 68, TAREA 1 del encargo)

**Se adosan al final del documento y NO reescriben ni una linea de las secciones de arriba**, que es
la via que esta pagina ya uso **OCHO** veces, la ultima de ellas la del acta 66 en la linea
**[[PAG_ACTA66]]** y la anterior la del acta 65 en la **[[PAG_ACTA65]]**, **las dos cotejadas HOY
abriendo el fichero**. **Ninguna cifra publicada de arriba se toca.**

**Y AQUI CAMBIA EL PROCEDIMIENTO DE LA CITA, porque la vuelta pasada lo pago:** **ninguna de las
citas de linea de esta seccion esta TECLEADA**. Cada una es una marca que el registrador sustituye
por el numero que le devuelve **buscar su aguja de contenido** en el fichero, y **antes de escribir
una sola letra el instrumento vuelve a barrer el texto ya sustituido y exige que TODO numero de
linea que aparezca en el salga de una aguja**; si uno solo no sale, cae en `ROJO` y **no escribe
nada**. El ensanche esta enumerado en el docstring de
[`../../scripts/loop/vuelta68_registrar_acta67.py`](../../scripts/loop/vuelta68_registrar_acta67.py)
y **va marcado discutible** en el reporte de esta vuelta. **El acta de la vuelta 67 abre en la linea
**[[A67_ABRE]]** de [`../loop/ACTA_AUDITOR.md`](../loop/ACTA_AUDITOR.md)**, su verificacion por
corrida propia en la **[[A67_VERIF]]**, su relectura ciega en la **[[A67_CIEGA]]**, sus caidas en la
**[[A67_CAIDAS]]**, sus quince adjudicaciones en la **[[A67_QUINCE]]**, sus pendientes en la
**[[A67_PEND]]**, su metrica de credito en la **[[A67_METRICA]]** y sus condiciones de parada en la
**[[A67_PARADAS]]**.

### a) **LA CAIDA DE CIFRA PUBLICADA DEL EJECUTOR, CON SU NOMBRE Y SU MEDICION: LA RACHA SE ROMPE EN LA DUODECIMA Y EL CONTADOR DE PARADA QUEDA EN UNO**

**Se registra aqui, y no solo en el acta, porque la cifra equivocada vive en ESTA pagina**, y una
caida que solo vive en un acta se olvida.

| | lo que el acta 67 mide, copiado de su linea | linea |
|---|---|---:|
| **la caida** | **el registro del acta 66 de esta pagina dice que la frase envejecida *cuya linea base sigue en `2`* vive en la linea `4055`, y lo medido es que vive en otras tres**; **es una cifra que vive en `docs/plan/`, o sea CAIDA DE CIFRA PUBLICADA**, y **esta FUERA de los quince discutibles marcados** | **[[A67_CAIDA_MEDICION]]** |
| **por que la guarda no la cazo** | **la guarda de citas del registrador cotejo esa linea contra OTRA afirmacion** (que ahi esta la cabecera del apartado e, y ahi esta) **y la afirmacion de la PROSA no estaba en su lista de agujas**; una guarda que coteja las citas de una lista y no las citas del TEXTO deja pasar exactamente esta especie | **[[A67_GUARDA_NO_CAZO]]** |
| **lo que NO cae** | **la declaracion de ENVEJECIDA es correcta**: la frase existe, esta envejecida por la adjudicacion de la base `4` y no se tacha; **lo equivocado es el puntero**, y el dato adjudicado no se movio | **[[A67_SUSTANCIA]]** |
| **el efecto en el credito** | **la relectura al doble se ejecuto** (47 citas de linea de los dos adosados, **46 calzan, UNA mala**) y **la racha CLASE O CIFRA EN CERO se rompe en la duodecima tanda** | **[[A67_EFECTO_CREDITO]]** |
| **la especie reporte** | **CERO**, porque la afirmacion equivocada no vive solo en `REPORTE.md`: **cuenta una sola vez y en la especie mas grave**. **TERCERA tanda seguida con reporte en cero** | **[[A67_REPORTE_CERO]]** |
| **las rachas al cierre de la 67** | **REPORTE EN CERO** (tercera seguida); **CLASE O CIFRA: ROTA** en la duodecima | **[[A67_RACHAS]]** |

> **EL CONTADOR DE PARADA QUEDA EN UNO, y se escribe con estas letras porque manda sobre la vuelta
> siguiente:** **UNA tanda con caida de clase o de cifra publicada**. La regla del credito pide **DOS
> SEGUIDAS** para parar el bucle. **Si la tanda 68 trae otra caida de clase o de cifra publicada, es
> `PARADA`**, y el auditor la ejecuta. La metrica acumulada al cierre de la 67 esta en la linea
> **[[A67_ACUMULADO]]**: **463 relecturas, 786 puestos, 7 caidas de clase, 27 de reporte del
> ejecutor, 14 de cifra publicada del ejecutor, 3 de cifra del auditor, 7 de acta del auditor y 4 de
> procedimiento del auditor**.

### b) **LA CORRECCION DECLARADA DE LA CITA, POR EL CARRIL DEL BANCO 9.10: EL TEXTO VIEJO VERBATIM, SIN TACHAR NADA, Y LA MEDICION AL LADO**

**Va por el mismo carril que la regla de la ficha envejecida de esta pagina** (linea
**[[PAG_FICHA_ENVEJECIDA]]**): **una correccion que tapa lo que corrige no se puede auditar**, asi
que **el texto viejo se cita entero y se queda donde esta**.

**LO QUE LA LINEA [[PAG_CITA_MALA]] DE ESTA PAGINA DICE HOY, COPIADO DEL FICHERO Y NO DE MEMORIA**
(las tres lineas del parrafo, leidas por el registrador en la corrida que escribe esta seccion):

[[VERBATIM:PAG_CITA_MALA:3]]

**LO MEDIDO, Y ES LO QUE MANDA:**

| | medicion |
|---|---|
| **donde vive de verdad la frase** | en las lineas **[[PAG_FRASE_1]]** a **[[PAG_FRASE_3]]** de esta pagina, dentro del apartado *LO QUE ESTA SECCION NO HACE* del registro del acta 65; **el fragmento *linea base sigue* esta en la linea [[PAG_FRASE_2]]** |
| **que hay de verdad en la linea [[PAG_E_ACTA65]]** | **la cabecera del apartado e) del registro del acta 65**, *LOS PENDIENTES 2 Y 4, NOMBRADOS CON SU DESTINO: EL CIERRE DE LA FASE 03*. **NUNCA vivio ahi la frase**, y el registrador lo comprueba con una aguja NEGATIVA antes de escribir |
| **que se corrige** | **solo el puntero**. **La declaracion de ENVEJECIDA sigue en pie**: la frase se lee con su corte del 20 ago 2026 y **manda la linea base `4`** que el acta 66 adjudico y que esta pagina registro en el apartado c) del registro del acta 66 |
| **que NO se corrige** | **nada de la aritmetica del censo**: las colisiones vigentes siguen siendo **4**, las dos de la mesa `OP-M-03` con su carril en la linea **[[PAG_CARRIL_COLISIONES]]** y las dos de `OP-U-02` con su duena |
| **que NO se tacha** | **ni una letra**. El parrafo viejo se queda tal cual, y esta correccion se lee al lado |

### c) **LOS QUINCE DISCUTIBLES, ADJUDICADOS: LOS QUINCE `A FAVOR`, Y EL `D1` POR EXTENSION CITABLE**

La columna de la vara **no es una glosa: es la regla citable con la que el auditor lo adjudico**.
**La cifra de cabecera y el detalle coinciden** (linea **[[A67_QUINCE]]**, *ADJUDICACION DE LOS
QUINCE DISCUTIBLES*): **quince marcados, quince adjudicados, cero sin contestar**.

| | lo discutible, tal como el ejecutor lo marco | **la vara que lo sostiene** | linea |
|---|---|---|---:|
| **`D1`** | declarar el `ACTO 12` por un `D` DIRECTO sin triangulo, con un motivo fuera de los tres sellados | **`A FAVOR` POR EXTENSION CITABLE**, y es la adjudicacion de mas peso de la tanda: la lista de motivos es **enumeracion, no estatuto**; `P.12` manda que los veredictos DIRECTOS gobiernen; la ultima linea de `P.10` no esta condicionada al triangulo | **[[A67_D1]]** |
| **`D2`** | declarar el `ACTO 14` por `P.5` cuando el quinto tiene una `A` con un miembro del puro | **`A FAVOR`**: el veredicto de clase y la membresia de familia **son dos cosas**, y el propio puesto 878 las separa en su texto; **`P.5` pregunta por familias, no por clases** | **[[A67_D2]]** |
| **`D3`** | estrenar la guarda `1B` como motivo unico en dos actos el mismo dia | **`A FAVOR`**: el carril esta escrito y registrado; **un carril escrito no necesita estreno previo para valer**, y usarlo dos veces el mismo dia es frecuencia, no doctrina | **[[A67_D3]]** |
| **`D4`** | en el `ACTO 15` las tres varas apuntan a una puerta y aun asi declara | **`A FAVOR`**: el carril del acta 54 resuelve el CHOQUE (vara a un miembro, puerta OTRO); aqui vara y puerta son **el mismo nodo** y lo que detiene es **la SEGUNDA puerta** | **[[A67_D4]]** |
| **`D5`** | una sola fusion sobre seis actos | **`A FAVOR`**: el contrato es **prefijo con tope, no minimo** (acta 61, `D1`); la cifra va publicada en vez de maquillada | **[[A67_D5]]** |
| **`D6`** | declarar seis teniendo cinco declarados baratos | **`A FAVOR`**: el lote se declara al abrirlo y se entrega lo declarado; **alargarlo al ver que sale barato es justo lo que el contrato del prefijo evita** | **[[A67_D6]]** |
| **`D7`** | el superviviente del `ACTO 16` contra el cableado 8 a 3 | **`A FAVOR`**: `P.8` es regla de **PRELACION** y el contenido dice algo (5 pasos contra 4); **el cableado no habla** | **[[A67_D7]]** |
| **`D8`** | cinco `APPEND` y el nodo duplica su tamano | **`A FAVOR`**, carril del `D9` del acta 65 y el `D7` del acta 66: **catalogo mas rico con solapes declarados** sobre `CUBIERTO` que calla texto vivo; el nodo entro a la cola de costuras | **[[A67_D8]]** |
| **`D9`** | los dos `APPEND` que se solapan (la brujula y el titular) | **`A FAVOR`**: el puesto 1319 llama al titular *su unico gesto propio*; **callar uno con `CUBIERTO` habria perdido texto vivo que el archivo distingue** | **[[A67_D9]]** |
| **`D10`** | una perdida con dos sitios en un solo campo `donde` | **`A FAVOR`, y el criterio queda adjudicado para que no oscile: LA FILA DEL CONTRATO ES POR PIEZA QUE SE PIERDE, NO POR SITIO DONDE VIVIA** | **[[A67_D10]]** |
| **`D11`** | tres perdidas con atenuante declarado | **`A FAVOR`**, carril del `D8` del acta 63 y el `D10` del acta 65: **sobre-sellar declarando es mas auditable que callar** | **[[A67_D11]]** |
| **`D12`** | corregir el defecto de `--base` sin encargo | **`A FAVOR`**: un instrumento committeado afirmando una cifra superada, **a sabiendas**, es la especie que esta campana persigue; la guarda sigue midiendo | **[[A67_D12]]** |
| **`D13`** | re-codificar dos salidas en vez de re-correr | **`A FAVOR`**, verificado **al byte** por el auditor: `cp1252` a `utf-8` **sin tocar una letra ni una cifra**; re-correr el reanclaje habria dado cero re-anclajes y esa salida ya no seria la de la operacion | **[[A67_D13]]** |
| **`D14`** | no contestar la pregunta de `P.5` en el `ACTO 15` | **`A FAVOR` con la letra delante**: `P.5` existe para decidir ANTES de fundir y **este acto no se funde**; **una pregunta cuya respuesta no tuviera consecuencia seria un rito** | **[[A67_D14]]** |
| **`D15`** | ensanchar la aguja del comprobador y corregir su rotulo sin encargo | **`A FAVOR`**: **una guarda que pasa en verde sobre nada es peor que una que falla** (acta 64, pregunta 6); el barrido previo esta medido y **no hay regresion** | **[[A67_D15]]** |

### d) **EL CUARTO MOTIVO SELLADO DEL `DECLARADO Y NO FUNDIDO`: UN VEREDICTO `D` DIRECTO INTERNO QUE LA FUSION ENTERA DESMENTIRIA (adjudicado por extension, con sus cuatro letras)**

**LA PREGUNTA CONCRETA DEL EJECUTOR SE CONTESTA PRIMERO, y la respuesta manda sobre todos los lotes
que quedan:** **LA LISTA DE MOTIVOS SELLABLES NO ES CERRADA, ES LA ENUMERACION DE LO ADJUDICADO
HASTA SU FECHA** (linea **[[A67_P1_LISTA_NO_CERRADA]]**). **La prueba esta en su propia historia**:
nacio con uno (`P.10`, registrado en la linea **[[PAG_ACTO1_P10]]** de esta pagina), **el acta 65
anadio la guarda `1B`** (linea **[[PAG_GUARDA_1B]]**) y **el acta 66 anadio `P.5`** (linea
**[[PAG_P5_MOTIVO]]**) diciendo con todas sus letras que anadir un motivo por adjudicacion es la
misma extension y **no doctrina nueva**. **Un encargo que enumera el estado del dia no convierte la
enumeracion en frontera.**

**EL CUARTO MOTIVO QUEDA ADJUDICADO** (linea **[[A67_P1]]**), **y sus cuatro letras van copiadas de
sus lineas**:

| | la letra, copiada de su linea | linea |
|---|---|---:|
| **PRIMERA** | **`P.12` parte 2 manda que con el acto convocado gobiernen los veredictos DIRECTOS** (una lectura hecha vale por si misma), y el **1374** es un `D` directo leido: **fundir los cinco deprecaria sus dos extremos al mismo vivo y sellaria que repiten entre si**, que es lo que esa lectura niega | **[[A67_P1_PRIMERA]]** |
| **SEGUNDA** | **la ultima linea de `P.10`** (*lo que NUNCA es salida es fundir la componente entera porque el cierre transitivo la junta*) **no esta condicionada a que exista triangulo**, y aqui **lo unico que junta a los dos nodos del `D` es el camino transitivo**: la unica lectura directa entre ellos es el `D` | **[[A67_P1_SEGUNDA]]** |
| **TERCERA** | **las tres salidas de `P.10` estan cerradas por letra vigente**: leer los pares que faltan es cribado que la fase no tiene (banco 9.21), releer contra el superviviente **presupone la fusion que se esta negando**, y el subconjunto cerrado exige todas las lecturas hechas **y ademas la fusion parcial la prohibe el encargo** | **[[A67_P1_TERCERA]]** |
| **CUARTA** | **el precedente del acto 5 de la vuelta 66 cerro `DECLARADO` por identidades que NADIE leyo**; aqui **la identidad esta leida y NEGADA**: el caso es mas fuerte | **[[A67_P1_CUARTA]]** |

> **EL CATALOGO DE MOTIVOS SELLADOS QUEDA EN CUATRO** (linea **[[A67_P1_CATALOGO]]**): **el
> triangulo de `P.10`**, **la guarda `1B`**, **la respuesta de `P.5` (no es una familia)** y **el `D`
> directo interno que la fusion entera desmentiria**. **El `ACTO 12` cierra `DECLARADO Y NO FUNDIDO`
> por ese cuarto motivo**, y su ficha en esta pagina, escrita cuando el motivo aun no tenia letra,
> esta en la linea **[[PAG_ACTO12]]** del registro del lote C.
>
> **Y LA LISTA SIGUE SIN SER ESTATUTO:** si un acto no cabe en ninguno de los cuatro, **va como
> `PENDIENTE DE DOCTRINA` con lo mejor sostenido registrado**, que es exactamente lo que la vuelta 67
> hizo con el 12.

### e) **EL TRANSITO DEL ACTO CON FORMA `EMPATE SIN VARA`: NI SE DECLARA NI DETIENE EL LOTE**

**Adjudicado en la linea **[[A67_P2]]**, y `P.8` ya decia a quien se trae (al auditor); lo que
faltaba era el estado mientras tanto.** **Queda asi, y es carril nuevo de procedimiento sobre letra
vieja:**

1. **EL ACTO NI SE DECLARA NI DETIENE EL LOTE** (linea **[[A67_P2_NI_NI]]**). **Se procesa entero
   como cualquier otro**: dossier, `P.5` sobre el texto estable, puertas, puentes y colisiones.
2. **Si una guarda o un motivo sellado lo detiene, cierra `DECLARADO` por ese motivo** y **el empate
   ya no importa**.
3. **Si nada lo detiene, el ejecutor NO elige superviviente** (linea **[[A67_P2_CASO]]**): **escribe
   el caso entero en el reporte** (la respuesta de `P.5`, las tres cuentas y el cableado, y **las
   piezas propias que el archivo nombra por cada miembro**, que es lo que `P.8` llama contenido:
   piezas propias, rol declarado, alcance) y **lo marca discutible**.
4. **El acto queda `ABIERTO EN TRANSITO` dentro del tramo, FUERA de la cuenta de cerrados del lote**
   (linea **[[A67_P2_TRANSITO]]**).
5. **El auditor adjudica el superviviente en su acta siguiente**, con el caso delante, y **el lote
   siguiente ejecuta esa fusion adjudicada como su primera operacion**.

> **`DECLARADO Y NO FUNDIDO` QUEDA RESERVADO A MOTIVOS SELLADOS** (linea
> **[[A67_P2_RESERVADO]]**): **el auditor aun no contesta no es un motivo, es una pregunta en
> viaje**. **El `ACTO 18` del prefijo viene MEDIDO en `EMPATE SIN VARA`** (pasos 4 a cuatro bandas,
> condiciones 2 a cuatro bandas, cableado empatado) **y entra al lote D por este carril**.

### f) **LA NOTA DE DICTADO DEL PUESTO 1030: LA SUSTANCIA MEDIDA, LA ATRIBUCION SUELTA, Y SIN CAIDA**

**Se registra porque una nota que solo vive en un acta se olvida, y porque distingue dos cosas que
conviene no confundir** (linea **[[A67_NOTA1030]]**).

| | lo que el acta 67 dice |
|---|---|
| **lo que el reporte 67 escribio** | que el puesto **1030** *enumera la familia con sus cuatro nombres* |
| **lo que el auditor midio** | la razon del **1030** nombra **el PAR** y **el rotulo de la familia** (la competencia entre inversores) **con su cuenta de cuatro miembros y seis pares**; **los cuatro nombres juntos los da el conjunto de los seis pares**, no ese puesto solo |
| **la sustancia** | **CALZA y esta medida**: los seis pares entre los cuatro miembros (787, 394, 334, 413, 257 y 1030) **leidos y los SEIS en `A`**, contados por el auditor contra el archivo |
| **el veredicto** | **la atribucion literal es un pelo suelta y queda dicha**, **sin contarse como caida**: el mismo carril del 1306 y el 1330 en el acta 66 |

### g) **LOS PENDIENTES 3 A 6, NOMBRADOS CON SU DESTINO**

**Se registran porque mandan sobre lo que viene aunque no encarguen trabajo hoy**, y **los cuatro
quedan NOMBRADOS, ninguno abierto en doctrina nueva**.

| pendiente | lo que el acta 67 fija, copiado de su linea | destino | linea |
|---|---|---|---:|
| **3. el subconjunto cerrado de un acto con puente** (heredado) | sigue **NOMBRADO**, ahora con **NUEVE actos esperandolo** (el **1**, **5**, **10**, **11**, **12**, **13**, **14**, **15** y **17**) | **el CIERRE DE LA FASE 03**, donde **la parada de `AUDITOR.md` garantiza que el fundador lo ve antes del tramo mecanico** | **[[A67_P3]]** |
| **4. la marca para *ya lo dice el `APPEND` de un hermano*** (heredado) | sigue **NOMBRADO**: **el carril vigente alcanza**, y la vuelta 67 **lo pago tres veces con atenuante declarado**; la cuenta crece y se publica | **anotado, no encargado** (el mismo trato que el `INCISO` de condiciones, acta 55 pregunta 5) | **[[A67_P4]]** |
| **5. el `INCISO` de condiciones** (heredado) | sigue en su carril, con **cinco piezas `DE CONDICIONES` mas** de la vuelta 67 | **la fase 04** (acta 55, pregunta 5) | **[[A67_P5]]** |
| **6. el esquema de `OPERACIONES.jsonl`** (heredado) | sigue **pendiente**; la vuelta 67 **no toco ninguna ficha y no estreno ninguna clave** (`OPERACIONES.jsonl` sin cambios, verificado por `numstat`) | **anotado, sin clave nueva** | **[[A67_P6]]** |

> **LOS DOS PRIMEROS PENDIENTES NO ESTAN EN ESTA TABLA PORQUE YA NO SON PENDIENTES:** el **1** quedo
> **ADJUDICADO** como el cuarto motivo sellado del apartado d) y el **2** quedo **ADJUDICADO** como
> el transito del apartado e). **Se dice para que la ausencia no parezca omision.**

### h) **LO QUE ESTA SECCION NO HACE, dicho para que nadie se lo atribuya**

**NO toca ni una cifra publicada arriba**, **NO tacha ni una letra del texto que corrige**, **NO
elige ningun superviviente**, **NO funde nada**, **NO deshace ninguna fusion**, **NO re-lee ni un
veredicto de las cuatro colisiones vigentes** (cuya **linea base es `4`** y cuyas duenas son la mesa
`OP-M-03` y `OP-U-02`), **NO toca la mesa `OP-M-03`**, **NO ejecuta ninguna de las cinco fichas
`OP-M-02` consumidas** y **NO reabre el registro del lote C** (linea **[[PAG_LOTE_C]]**), cuyos
apartados sobre los actos **13** y **15** (linea **[[PAG_ACTO13_15]]**), el **14** (linea
**[[PAG_ACTO14]]**) y el **17** (linea **[[PAG_ACTO17]]**) **quedan tal como se escribieron**.
Registra adjudicaciones y una correccion declarada.
"""
