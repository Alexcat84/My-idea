# EL BANCO DEL PLAN

**Lecciones que este plan produjo y que valen mas alla de el.** No son operaciones:
son **como se mide y como se lee** en este catalogo.

> **Se escriben aqui porque una leccion que vive dentro de una operacion muere con
> ella.** Estas sobreviven a la pasada unica.

---

## P.1 REGLA DE MEDICION: EN ESTE GRAFO, TODO CONTEO QUE TOQUE IDS PASA POR EL RESOLUTOR ANTES DE CONTAR

**Adoptada el 11 ago 2026, y nace de un error propio.**

> **Un id de este grafo no es una cadena: es una referencia con historia.** Comparar
> ids **literalmente** no mide lo que parece que mide, porque **un id vivo y un
> alias suyo son el mismo nodo escritos de dos maneras**.
>
> **LA REGLA: todo instrumento que cuente, cruce o compare ids RESUELVE PRIMERO.**
> Sin excepcion, y **da igual quien haya pedido el conteo**: aplica a los
> instrumentos y a los dictados del auditor por igual.

### LOS DOS EJEMPLARES, y los dos fallan en direcciones opuestas

| ejemplar | que hace la comparacion literal | por que es peligroso |
|---|---|---|
| **las 27 auto-aristas** | da **CERO** sobre un grafo que tiene **veintisiete** | **INVENTA SALUD**: hace desaparecer un problema real |
| **las aristas a nodos deprecados** | las da por **ROTAS** | **INVENTA ENFERMEDAD**: manda a reparar lo que ya funciona |

**EL PRIMERO, medido.** Las 27 auto-aristas son **33 enlaces y NINGUNO es directo**:
el nodo no se cita a si mismo por su id, **cita un id que es su propio alias**.
`analisis_flujo_de_valor` lleva `value_stream_analysis_lean` en sus
`nodos_previos`, y ese id es su alias. **Una comparacion literal no ve ni una de
las 33.**

**EL SEGUNDO, medido el mismo dia.** De **391 alias**, **314 apuntan a un nodo
deprecado**. Un instrumento que exija que toda arista apunte a un nodo **vivo**
declararia rotas cientos de aristas sanas. **Apuntar a un deprecado ES la funcion
del alias**, y `resolverId` las camina hasta un activo.

> **Las dos averias tienen la misma raiz y remedios opuestos, y por eso hay que
> tener la regla escrita:** sin ella, el mismo instrumento que no ve las 27 se
> inventa 314.

### QUE OBLIGA, y es corto

1. **Ningun conteo de ids se publica sin decir si resolvio.** Igual que ninguna
   cifra viaja sin su corte (banco 9.21), **ninguna cifra de ids viaja sin decir
   con que semantica se midio.**
2. **Las guardas tambien resuelven.** Una guarda de Gate 0 que compare literalmente
   **es una guarda que no guarda**: pasaria verde el dia de la reparacion y
   seguiria pasando verde si manana vuelve a entrar una.
3. **Un dictado del auditor no exime.** La adjudicacion que mataba `OP-S-07` era
   correcta **dado el numero que yo di**, y el numero estaba mal. **La regla se
   aplica antes de dictar y antes de obedecer.**

### EL COSTE, para que quede dicho

**Un ciclo entero de ida y vuelta**: informe cero, el auditor adjudico sobre cero y
mato una operacion real, y hubo que devolverla. **La medicion mal hecha no se
quedo en la medicion: viajo hasta una decision.**

---

## P.2 HALLAZGO: LA FIRMA POSICIONAL DEL INJERTO

**Adoptado el 11 ago 2026, al verificar la nomina de Hugos.**

> **EL ORDEN DENTRO DEL CAMPO `fuente` LLEVA INFORMACION.** No es una lista
> desordenada de libros: **el primero es de donde salio el nodo, y lo que viene
> detras es lo que se le pego.**

### LA CIFRA, y es lo que convierte la observacion en detector

| | nodos vivos |
|---|---:|
| declaran **Hugos** en su campo `fuente` | **128** |
| lo declaran **como fuente unica o primera** | **107** |
| **lo declaran en SEGUNDO lugar, detras de otro libro** | **21** |
| de esos 21, **confirmados como injerto** | **21 de 21** |

> **Citar a Hugos no dice nada: lo hacen 128 nodos. Citarlo DETRAS de otro libro lo
> dice todo: son 21 y los 21 son los injertados.**

**LOS VEINTIUNO, todos de `core`**: `analisis_tco_roi_b2b`, `asociaciones_clave`,
`bundle_ideas`, `co_creation_session`, `criterios_seleccion_proveedores`,
`economia_circular_como_modelo_de_negocio`, `empoderamiento_de_participantes`,
`gestion_cuentas_por_cobrar`, `gestion_inventario`, `gestion_libro_abierto_obm`,
`mapa_de_canal_de_ventas`, `modelo_hibrido_agile_stage_gate`,
`principio_calidad_mvp`, `procesamiento_paralelo_con_espirales`,
`producto_unico_superior`, `propuesta_gasto_capital`, `ratios_eficiencia_inventario`,
`reduccion_tamano_de_lote_batch_size`, `schedule_management_plan`,
`seleccion_estrategia_pricing`, `transicion_producto_a_experiencia`.

### POR QUE ES UN DETECTOR Y NO UNA CURIOSIDAD

**Antes**, encontrar un injerto costaba **leer el nodo entero** y comparar su
material contra el libro que declaraba. **Con la firma posicional, el candidato
sale de una consulta al campo `fuente`**, y la lectura solo tiene que **confirmar
o descartar**.

> **Es el mismo salto que dio el barrido de las A frente al contador de nombres:**
> se cambia el goteo por una lista.

**Y tiene el mismo limite que todo detector: levanta candidatos, no adjudica.** La
firma dice **donde mirar**; el veredicto sigue siendo de la lectura. En Hugos la
tasa fue **21 de 21**, pero eso es una medicion de este libro, no una promesa.

### LO QUE ESTA FIRMA LE DEBE A UNA CORRECCION

**El numero honesto de esta ficha no es 21 contra 128: es 21 contra 107.** Los 107
que declaran Hugos **como fuente unica o primera** son el fondo sano contra el que
se recorta la firma. **Sin ese fondo, el 21 no significa nada.**

### PARA DONDE VA

| destino | que se lleva |
|---|---|
| **el mundo 11** | la firma completa con su cifra, porque es material de contenido y no de proceso: **un nodo que declara dos libros con el segundo pegado esta mal atribuido, y la atribucion es lo que el lector ve** |
| **`07_ADUANA`** | **el detector, como control de entrada permanente.** Todo nodo que entre declarando **mas de una fuente** pasa por la comprobacion: el material del segundo libro, esta en los pasos? Si no esta, **la fuente sobra**; si esta y es de otro tema, **es un injerto y se desteje** |

> **A la aduana le interesa mas que al plan.** El plan repara 21 nodos una vez; la
> aduana **impide que entre el veintidos**, y para eso le basta con mirar el orden
> del campo `fuente`, que es lo mas barato que se puede mirar.

### LA PREGUNTA QUE ESTA FIRMA ABRE, y no se contesta aqui

**Hugos es el libro que mas junturas dejo, pero la firma no es suya: es del campo
`fuente`.** Nadie ha corrido el mismo recorte con los otros libros. **Si la firma
posicional vale en general, hay una lista de injertos que nadie ha contado.**

> Se anota, **sin cifra y sin estimacion**, porque inventar un numero aqui seria
> exactamente lo que la regla P.1 acaba de prohibir.

---

## P.3 REGLA DE REMEDIO: CUANDO EL INJERTO ES DEL MISMO TEMA, NO SE PODA, SE REPARTE

**Adoptada el 11 ago 2026, al cerrar la tanda de los 43 injertos.**

> **El remedio de un injerto depende de UNA sola pregunta: el bloque pegado es del
> MISMO tema que el nodo, o de otro?**

| el bloque pegado es | que se hace | por que |
|---|---|---|
| **de OTRO tema** | **la poda es segura** | el lector distingue solo lo que sobra: ve material que no viene a cuento |
| **del MISMO tema** | **NO se poda: SE REPARTE** | **el lector no puede distinguir que vino de donde**, asi que podar es elegir por el cual mitad se queda, y esa eleccion no la hace nadie |

**LOS DOS CASOS, medidos, y por eso la regla no es teorica:**

| caso | el bloque | el remedio |
|---|---|---|
| **Hugos**, 21 nodos | **cadena de suministro** dentro de nodos de producto y de finanzas: **otro tema** | **la poda era segura**, y por eso la ficha pudo escribir *poda o reparto* sin peligro |
| **Coleman, Horowitz, Weinberg y Rackham**, 43 nodos | **el tema COINCIDE**: el bloque de Coleman habla del cliente y el nodo tambien; el de Weinberg habla de canal y el nodo tambien | **REPARTO OBLIGATORIO** |

> **POR QUE EL MISMO TEMA HACE LA PODA PELIGROSA, y no solo cara.** Cuando los dos
> bloques hablan de lo mismo, **el lector que sigue el nodo no sabe donde acaba un
> libro y empieza el otro**: para el es un procedimiento y ya. **Podar el segundo
> bloque no le quita ruido: le quita la mitad de un metodo que estaba usando
> entero.**

**LO QUE OBLIGA, aplicado a las cuatro decisiones de fuente nuevas:**

| operacion | el bloque se REPARTE a |
|---|---|
| **`OP-F-04-COL`** | la serie de los 100 dias de Coleman, que ya tiene **16 nodos de fase y dos nodos-programa** |
| **`OP-F-04-HOR`** | la familia de Horowitz, y donde no exista **se crea nodo propio**: no se borra |
| **`OP-F-04-WEI`** | el Bullseye y los canales de traccion de Weinberg |
| **`OP-F-04-RAC`** | la familia de SPIN, que ya tiene un acto CERRADO de cuatro miembros |

> **Y ninguna de las cuatro admite la salida barata.** *Podar y ya* deja de ser una
> opcion en las cuatro, **y eso encarece la fase 01 a proposito**: el reparto pide
> decidir a donde va cada bloque, y esa decision es la que evita perder material
> que el lector estaba usando.

---

## P.4 CLASE PROPIA: LA A DE BLOQUE

**Adoptada el 11 ago 2026, con `LD-06` de ejemplar.**

> **Hay repeticion, pero NO entre los dos nodos: entre el BLOQUE INJERTADO de uno
> y el OTRO NODO ENTERO.**

**COMO SE RECONOCE, y son tres senales juntas:**

1. uno de los dos nodos **declara fuente doble**
2. su **bloque apendice** repite con el otro nodo **paso por paso**
3. **su primer bloque no tiene nada que ver** con el otro nodo

**EL ARREGLO, y no admite atajo:**

> **DESTEJIDO MAS FUSION PARCIAL. Nunca fusion de enteros.**

| lo que se hace | lo que NO se hace |
|---|---|
| se **desteje** el nodo de fuente doble | **fundir los dos nodos enteros** |
| su **bloque apendice** se funde con el otro nodo | dejar el injerto donde esta porque *repite igual* |
| su **primer bloque** se queda como nodo, con su fuente corregida | podar el bloque, que perderia material vivo |

### EL EJEMPLAR: `LD-06`

`project_close_out` declara **Snyder y Coleman**. Sus **pasos 1 a 5** son el cierre
formal de proyecto: acta de constitucion, criterios de finalizacion, variaciones,
cierre de contrato, aprobaciones. Sus **pasos 6 a 11 son Coleman**, y **repiten con
`reunion_conclusion_proyecto` casi paso por paso**, incluida **la misma cifra: tres
meses de monitoreo posterior.**

> **LA ADVERTENCIA, y es el motivo de que la clase exista: fundir enteros mete una
> cosa dentro de otra que no le corresponde.** Aqui meteria **el cierre formal de
> un proyecto dentro de una reunion de conclusion con encuestas**. El superviviente
> quedaria diciendo que para cerrar una reunion de satisfaccion hay que revisar el
> acta de constitucion.

### POR QUE NO BASTA CON LLAMARLA A Y SEGUIR

**Una A normal manda fundir.** Si esta se registra como A a secas, **quien ejecute
va a fundir los nodos enteros**, porque eso es lo que una A significa en todo el
resto del archivo. **La clase existe para que el ejecutor no tenga que adivinar
que esta A es distinta.**

> **Y tiene una consecuencia de ORDEN: la A de bloque obliga a que el destejido
> vaya ANTES que la fusion, siempre.** En una A normal el orden puede discutirse;
> **en esta no hay fusion posible hasta que el bloque este separado.**

### DONDE BUSCARLAS

**La firma de P.2 las levanta**: todo nodo de fuente doble es candidato, y **son 67
en el catalogo**. La A de bloque aparece cuando **uno de esos 67 tiene un par en la
cola con un nodo del libro que lleva pegado**.

> **`LD-07` es el contraejemplo util y va al lado del ejemplar**: el MISMO bloque
> injertado, contra el OTRO nodo de Coleman, sale **D**. **Que un nodo lleve un
> injerto no significa que repita con todo su libro de origen: repite con uno, y
> hay que leer cual.**

---

## P.5 REGLA DE ORDEN: CADA ACTO QUE VAYA A FUNDIRSE SE LEE ENTERO

**Adoptada el 11 ago 2026, y saca 55 pares del backlog.**

> **CADA ACTO SE LEE ENTERO DESPUES DE SU DESTEJIDO Y ANTES DE SU FUSION.**

**LA PREGUNTA QUE CONTESTA, y no la contesta ninguna otra cosa:**

> **el acto es UNA familia o son DOS?**

**Un acto se construye por transitividad**: si A repite con B y B con C, los tres
caen en la misma componente. **Pero eso no prueba que A repita con C.** Mientras
queden pares internos sin leer, **la componente puede ser una familia o pueden ser
dos pegadas por un nodo puente.**

**POR QUE DESPUES DEL DESTEJIDO Y NO ANTES.** Un acto con costuras dentro **no
tiene texto estable**: leer un par cuyo nodo va a perder la mitad de sus pasos
**es leer algo que va a dejar de existir**. Es la misma razon por la que el cribado
CONGELA un par cuyo veredicto depende de una cirugia.

**POR QUE ANTES DE LA FUSION.** Despues ya no hay a quien preguntarle: **una vez
fundido, el acto es un nodo y la pregunta de si eran una familia o dos se vuelve
irrespondible.**

### LO QUE ESTO CAMBIA EN LA CUENTA

**Los 55 pares que estaban en el backlog como *resto sin mesa ni nomina* dejan de
ser backlog: son la lectura obligatoria de 29 actos.**

| | |
|---|---:|
| actos afectados | **29** |
| pares que se leen | **55** |
| de ellos, ya leidos como lectura dirigida | **2** (`LD-04` y `LD-08`) |
| **pendientes reales** | **53** |

> **Y no es trabajo nuevo: es trabajo que ya estaba y no tenia dueno.** Antes se
> iba a fundir sin leerlo; ahora se lee, y se lee en el unico momento en que la
> respuesta vale.

### LA REGLA VALE PARA LOS 221 ACTOS, no solo para los 29

**Los 29 son los que tienen pares fuera de cola y ninguna mesa que los recoja.**
Los demas la cumplen por otra via: **173 actos ya estan enteros** (`OP-U-01`), y
los grandes **entran por mesa o por destejido**, donde la lectura completa ya
estaba prevista.

> **El efecto neto de la regla es que NINGUN acto se funde sin haberse leido
> entero.** Eso, y no otra cosa, es lo que convierte una componente medida en una
> familia declarada.

### CORRECCION DECLARADA: **EL ALCANCE DE P.5 ES EL ACTO EN OPERACION, Y NADA MAS** (15 ago 2026, decision del fundador)

**Nace de la vuelta 35, que midio sobre `OP-D-03` algo que la regla no acotaba:** de los
seis pares `A` del acto, **CINCO se habian leido contra texto que ya no existe** porque el
destejido de la propia operacion lo cambio. La regla obliga a releerlos, y ahi aparecio la
pregunta que el texto de arriba no contestaba: **hasta donde llega ese deber de relectura.**

> **LA RELECTURA DE PARES RANCIOS Y LA LECTURA DEL ACTO ENTERO VALEN SOLO DENTRO DEL ACTO
> EN OPERACION. NINGUN PAR DE FUERA DEL ACTO SE RELEE POR ESTE CAMINO.**

**El motivo, y es de alcance, no de rigor:** el mismo criterio (un veredicto emitido contra
un texto que despues cambio) alcanzaria a pares de todo el archivo, y aplicarlo sin frontera
**abre un re cribado que ninguna operacion escribio y que nadie adjudico**. `P.5` existe
para contestar *el acto es una familia o son dos* antes de fundirlo, no para reabrir el
cribado entero.

> **DENTRO del acto en operacion, la relectura es OBLIGATORIA y no opcional**: es lo que
> hace que la fusion se decida sobre texto vivo. **FUERA del acto, un par rancio no se
> toca por esta puerta**; si alguna vez hay que abrirla, sera con su propia operacion
> escrita y su propia adjudicacion, no como efecto lateral de una fusion.

### EXCEPCION DE UNA VEZ, AUTORIZADA POR EL FUNDADOR: **EL CUARTO MIEMBRO DEL RACIMO MIXTO DE `OP-D-04`** (19 ago 2026)

**La regla de arriba se queda entera y su frontera no se mueve.** Lo que sigue es **UNA
autorizacion expresa, para UN racimo, de UNA sola vez**, y se escribe aqui precisamente
para que **no valga como precedente**.

**EL CASO:** el triangulo del taller de `OP-D-04` (`brainstorming_divergente`,
`brainstorming_efectivo`, `reglas_brainstorming`) es **tres de los cuatro miembros del
racimo mixto** *Las reglas del brainstorming*. **El cuarto, `brainstorming`, es de
`quality` y esta FUERA del acto.** Ahi chocan dos cosas escritas: `MESA_RACIMOS.md`
advierte que **podar el lado del nucleo de un racimo mixto cambia el gradiente del mundo
que lo acompana**, y el alcance de `P.5` **no da puerta para leer un par de fuera del
acto**. Y ninguna operacion de la fase 06 nombra a estos nodos: **esa mesa no esta
escrita.**

> **AUTORIZADO, POR ESTA VEZ Y SOLO PARA ESTE RACIMO: `brainstorming` se lee contra cada
> uno de los tres del taller, en TRES lecturas dirigidas (`LD-96` a `LD-98`), FUERA DEL
> ALCANCE DE `P.5`.**

| resultado | que pasa |
|---|---|
| **las tres dan `D`** | **el racimo queda decidido** y el cuarto **se ENLAZA** al superviviente del taller. La fusion sigue |
| **alguna da `A`** | **EL BUCLE PARA** con la lectura delante. Una `A` ahi mete a un nodo de `quality` dentro del acto, y eso es **alcance de campaña, no de operacion** |

> **POR QUE ES EXCEPCION Y NO REGLA NUEVA:** la puerta se abre porque **fundir a ciegas
> el lado del nucleo de un racimo mixto es peor que leer tres pares**, no porque el
> alcance de `P.5` estuviera mal. **Cualquier otro racimo mixto que aparezca vuelve a
> necesitar autorizacion**, o su mesa escrita en la fase 06.

---

## P.6 EL TEMA SE LEE, EL ACTO SE COMPUTA

**Adoptada el 11 ago 2026, y nace de una degradacion que no cerraba.**

> **LA NOMINA DE TEMA Y LA NOMINA DE ACTO SON DOS OBJETOS DISTINTOS.**
>
> **La nomina de TEMA se DECIDE LEYENDO**: quien pertenece al racimo depende de
> cual es su objeto, y eso lo dice un lector, no una cuenta.
>
> **La nomina de ACTO se COMPUTA**: es el **cierre transitivo de la relacion
> gemelo** (banco 9.24), y **NO ADMITE GUSTO**. Si hay A, el nodo esta dentro.

> **Y DE AHI LA OBLIGACION QUE ESTA REGLA IMPONE: TODA FORMA DECLARADA DICE SOBRE
> CUAL DE LAS DOS SE DECLARO.** *Puro*, *sub-puro*, *mezclado* y *partido* son
> formas de **componente**, o sea del acto. **Escribirlas sin decir sobre que
> nomina se contaron es lo que produce la contradiccion.**

### POR QUE HACEN FALTA LAS DOS, y por que no se pueden colapsar

**Ninguna de las dos sobra.** El acto contesta *que hay que hacer con estos nodos*:
si repiten, se funden o se enlazan, y eso no se puede votar. El tema contesta *de
que va este racimo*, que es lo que hace que una nomina se pueda leer, nombrar y
sentar en una mesa. **Un acto sin tema es una lista de ids; un tema sin acto es una
opinion.**

**MIENTRAS NINGUN MIEMBRO AJENO AL TEMA TENGA UNA A, LAS DOS NOMINAS COINCIDEN.**
Por eso el problema no se ve casi nunca: **aparece exactamente el dia en que un
nodo de otro tema entra por una A**, y ese dia las dos se separan **sin que nadie
lo anuncie**.

### EL EJEMPLAR, con sus dos decisiones fechadas y las dos vivas

**`tecnica_anclaje_negociacion` contra el racimo de la competencia entre
inversores.**

| | decision | fecha | sobre que objeto | resultado |
|---|---|---|---|---|
| **1** | la lectura del **puesto 878** lo deja **FUERA**, con motivo escrito: *su objeto es como negociar terminos y no como generar competencia entre inversores* | archivo, puesto 878 | **el TEMA** | nomina de tema: **cuatro** |
| **2** | el barrido del **11 ago 2026** lo mete **DENTRO** por el cierre transitivo de la A del 878, reafirmada como vigente en el puesto 1295 | 11 ago 2026 | **el ACTO** | nomina de acto: **cinco** |

> **LAS DOS SON CORRECTAS. No hay contradiccion: hay dos objetos.** Lo que estaba
> mal era **la etiqueta**, no las decisiones: se publico *PURO, cuatro miembros,
> seis pares*, que es una cuenta de **componente**, mientras la nomina de cuatro era
> de **tema**.

> **LA REGLA DE ORO QUE ESTO DEJA: si una forma y una nomina no cuadran, antes de
> discutir quien tiene razon se pregunta SOBRE CUAL DE LAS DOS NOMINAS SE CALCULO LA
> FORMA.** Casi siempre ahi se acaba la discusion.

### COMO SE ESCRIBE A PARTIR DE HOY

| se escribe asi | y no asi |
|---|---|
| *la competencia entre inversores: **acto** de 5, **tema** de 4; **SUB-PURO 7 de 10 sobre el acto*** | *la competencia entre inversores: PURO* |
| *el racimo del pivote: **acto** partido en 3, **tema** de 7; **MEZCLADO 13 de 21 sobre el tema*** | *el racimo del pivote: MEZCLADO* |

> **Y cuando las dos coinciden, se dice que coinciden.** Es informacion, no ruido:
> **una nomina donde tema y acto calzan es una nomina que ya no puede sorprender.**

---

## P.7 TODA OPERACION DE MESA SE SIMULA ANTES DE ESCRIBIRSE LISTA

**Adoptada el 12 ago 2026, y nace de que la primera simulacion del plan le corrigio
DOS cosas a la adjudicacion del auditor.**

> **NINGUNA OPERACION DE MESA PASA A LISTA SIN HABERSE SIMULADO SOBRE UNA COPIA EN
> MEMORIA DEL GRAFO.** Y **el script de la simulacion se NOMBRA dentro de la
> operacion**, para que cualquiera pueda volver a correrla.

### QUE TIENE QUE DEVOLVER LA SIMULACION

| | |
|---|---|
| **1** | el **desempate por cableado**, con los dos grados a la vista |
| **2** | los **alias resultantes** del superviviente |
| **3** | las **entradas que se redirigen**, una por una |
| **4** | las **duplicadas NUEVAS** que la fusion fabrica, y solo las nuevas |
| **5** | las **auto-aristas** que la fusion crearia |
| **6** | las **aristas internas del acto que sobreviven**, con su direccion **resuelta** |

**El instrumento es `scripts/plan/simular_fusion.py`.**

### EL EJEMPLAR, y es la razon de la regla

**La mesa de la junta asesora se adjudico con dos premisas razonables, y la
simulacion tumbo las dos:**

| la premisa | lo que midio la simulacion |
|---|---|
| *la arista entre los dos es **bidireccional** y se convierte en el enlace buscado* | **es UNA sola, dirigida**, declarada en los dos extremos. **Y apunta al reves de la escalera.** La direccion buena **no existia** |
| *la entrada de `formalize` por `customer_discovery` **se redirige** por alias* | **ya estaban las dos**: `customer_discovery` nombraba a los dos nodos. No habia que redirigir nada, y **la fusion dejaba una duplicada** |

> **NINGUNA DE LAS DOS SE VE LEYENDO. Las dos se ven simulando.** Un expediente
> completo, con los pasos, los veredictos y las aristas listadas, **no basta**:
> **una fusion es una operacion sobre el grafo, y el grafo hay que correrlo.**

### LO QUE LA REGLA IMPIDE, dicho con nombre

**Impide adjudicar sobre un grafo imaginado.** Las dos correcciones de la junta
asesora **no eran errores del auditor**: eran **detalles que solo aparecen cuando se
ejecuta**. La regla no desconfia de quien adjudica: **desconfia de la lectura como
metodo para predecir el estado final.**

> **Y trae su propio caso positivo: si la simulacion no corrige NADA, tambien vale.**
> Lo que no vale es **no haberla corrido.**

---

## P.8 EL CABLEADO DESEMPATA, NO DECIDE

**Adoptada el 12 ago 2026, y nace del primer choque entre el grafo y el archivo.**

> **EL DESEMPATE POR CABLEADO SOLO HABLA A CONTENIDO EMPATADO.** Donde el contenido
> dice algo, **el contenido manda**, aunque el margen de aristas apunte al otro lado.

### QUE CUENTA COMO CONTENIDO, y aqui esta lo que no era obvio

**Contenido no es solo el texto de los pasos.** Tambien lo son, **y con el mismo
peso**:

| | |
|---|---|
| **un PADRE DECLARADO por el archivo** | si una lectura ya dijo que A es la doctrina general y B su hijo, **eso es contenido**, no cableado |
| **el ALCANCE DEL ROL** | una cabeza que vale para las ocho fases **no puede llamarse como una sola** |

> **Y UNA ARISTA DE MARGEN NO VENCE A NINGUNA DE LAS DOS COSAS.**

### EL EJEMPLAR, con sus dos cifras

**La cabeza de la serie de medios de Coleman, par 948.**

| dice | quien gana | con que |
|---|---|---|
| el **cableado** | `estrategia_multicanal_bienvenida` | **3 contra 2**. **Margen de UNA arista** |
| el **archivo** | `seis_medios_comunicacion_cliente` | el veredicto **1012** lo llama **LA DOCTRINA GENERAL** y declara **hijo** suyo a `seis_canales_comunicacion_assess` |

**Adjudicado: sobrevive `seis_medios_comunicacion_cliente`.**

> **Y el nombre lo confirma por su lado: el id que ganaba por cableado dice
> BIENVENIDA, que es UNA fase, mientras la doctrina vale para las OCHO.** **La cabeza
> de una serie no se llama como uno de sus pasos.**

### LA SEGUNDA APLICACION, y es mas dura que la primera

**El acto II del racimo del pivote.** Ahi el cableado **no empata ni por poco**:
`pivotar_o_proceder` tiene **10** y `pivote_o_proceder` **5**. **Y aun asi sobrevive
`pivote_o_proceder`**, porque **lleva el material propio**: el mapa del cliente
tipico y el resumen en un parrafo.

> **Diez contra cinco, y pierde.** Si P.8 solo valiera para empates de una arista
> seria una regla decorativa. **Vale para esto.**

### LO QUE ESTO NO AUTORIZA

**No autoriza a ignorar el cableado cuando el contenido calla.** En la fusion 328 de
la junta asesora **el veredicto dice literalmente que los pasos coinciden**: ahi el
contenido **no tiene nada que decir**, y el cableado decide solo. **La regla es de
PRELACION, no de desprecio.**

| el contenido | quien decide |
|---|---|
| dice algo (piezas propias, rol declarado, alcance) | **el contenido** |
| **esta empatado y el veredicto lo dice** | **el cableado** |
| empatado y el cableado tambien | **se trae al auditor** |

---

## P.9 TODA ARISTA NUEVA SE ESCRIBE RESUELTA AL DIA DE SU ESCRITURA

**Adoptada el 12 ago 2026, y nace de leer el plan en orden de ejecucion en vez de en
orden de escritura.**

> **UNA ARISTA SE ESCRIBE CON EL ID QUE ESTARA VIVO EL DIA EN QUE SE ESCRIBA, no con
> el que estaba vivo el dia en que se decidio.**

### DE DONDE SALE

**`OP-E-04` tiene nueve aristas, y SEIS de sus destinos mueren el mismo dia en que
ella se ejecuta**: cinco apuntan a `gates_go_kill_decision_points` y una a
`estructura_gates`, y los dos desaparecen dentro de sus fusiones.

> **Escribirlas literales seria fabricar SEIS ARISTAS POR ALIAS el mismo dia en que
> `OP-S-12` acaba de limpiar MIL CINCUENTA Y SEIS.** **La fase que limpia y la fase
> que ensucia serian la misma tarde.**

### LO QUE LA REGLA OBLIGA, y son tres cosas

| | |
|---|---|
| **1** | **los enlaces corren DESPUES de las fusiones que tocan sus destinos**, y eso se escribe en el `depende_de`, no en una nota |
| **2** | **la arista se escribe con el id RESUELTO**, no con el que aparece en la lectura que la justifica |
| **3** | **la verificacion de cada enlace incluye que la arista NO NAZCA RESOLVIENDO POR ALIAS**: se comprueba que el id escrito es el id vivo |

### POR QUE NO BASTA CON EL RESOLUTOR

**Porque el resolutor la haria funcionar, y ese es justo el problema.** Una arista
escrita al id muerto **llega igual a su destino**, asi que **nadie la nota**: el grafo
se ve bien desde fuera. **Es exactamente la basura que `OP-S-12` mide, y se fabricaria
por descuido en la operacion que viene despues de limpiarla.**

> **LA FORMA CORTA: EL RESOLUTOR ES UNA RED DE SEGURIDAD, NO UNA LICENCIA.**

---

## P.10 LOS NODOS PUENTE, y son la mitad diagnostica de P.5

**Figura nombrada el 12 ago 2026, despues de que aparecieran TRES en dos dias.**

> **UN NODO PUENTE es el que tiene A con dos nodos que entre si son D.**
>
> **La componente que forma puede ser UNA familia o DOS pegadas por el.** Y **el
> cierre transitivo no lo distingue**: las junta igual.

### LA REGLA DE DETECCION, y es la unica que hay

> **UN NODO PUENTE SOLO SE VE MIRANDO LA COMPONENTE ENTERA.** Leyendo un par, jamas.
> **Es la mitad diagnostica de P.5**: la regla manda leer el acto entero antes de
> fundirlo, **y esto es lo que esa lectura encuentra cuando encuentra algo.**

**EN LA PRACTICA:** por cada componente, **se listan sus pares leidos y se busca un
nodo con dos A cuyos otros extremos den D entre si.** **Si aparece, la componente NO
se funde hasta que ese triangulo se cierre.**

### LOS TRES EJEMPLARES

| | el puente | sus dos A | la D que los enfrenta | como acabo |
|---:|---|---|---|---|
| **1** | `sistema_gates_go_kill` | 488 y 801 | **`LD-44`** | **`LD-58` lo cerro hacia la UNION**: los dos lados son un acto de seis, y la anomalia **se movio** al propio `LD-44` |
| **2** | `filosofia_customer_validation` | 1096 con earlyvangelists | 1185, 436 y 697 | **se resuelve releyendo contra el superviviente**, banco 9.10 |
| **3** | `customer_validation` **y** `filosofia_customer_validation` | 781 y 245 con `customer_validation_sell_phase` | **`LD-59`** | **no queda lectura que desempate**: se funde solo el triangulo cerrado y el cuarto **se enlaza** |

> **Y EL TERCERO ENSENA LO QUE LOS DOS PRIMEROS NO: UN PUENTE PUEDE SER DOBLE.** Dos
> nodos pueden hacer de puente a la vez sobre el mismo par, **y entonces la componente
> no tiene un punto debil: tiene una costura.**

### LAS TRES SALIDAS, y ninguna es fundir a ciegas

| salida | cuando |
|---|---|
| **leer el par que falta** | si queda alguno sin leer. **Es la unica que resuelve de verdad** |
| **releer contra el superviviente** | si el par existe pero uno de sus nodos va a cambiar. Banco 9.10 |
| **fundir solo el subconjunto CERRADO y enlazar el resto** | si todas las lecturas estan hechas y aun asi se contradicen. **Es la unica forma que no desmiente ninguna** |

> **LO QUE NUNCA ES SALIDA: fundir la componente entera porque el cierre transitivo la
> junta.** **El cierre transitivo no lee: cuenta.**

---

## P.11 PRECISION DE LA VARA: **UNA ADVERTENCIA ES LINEA, NO PROCEDIMIENTO**

**Ratificada por el auditor el 12 ago 2026, y la estreno `LD-58`.**

> **LAS ADVERTENCIAS CALIFICAN EL ACTO, NO LO CONSTITUYEN.**
>
> *No lo delegues*, *no dejes que avance*, *preguntate de verdad*, *no te aferres a tu
> idea*, *evita el multitasking*: **ninguna de esas frases anade un paso al
> procedimiento. Le anaden una condicion de calidad al paso que ya estaba.**

### POR QUE HACIA FALTA DECIRLO

**La regla practica de la vara ya distinguia linea de procedimiento**: es LINEA un
puntero, **una advertencia**, un criterio suelto o una accion unica; es PROCEDIMIENTO
un paso con varias decisiones dentro o que se repite en el tiempo.

**Pero un nodo entero hecho de advertencias no se ve como una linea: se ve como una
lista de cuatro pasos.** Y ahi es donde la vara se aplicaba mal.

**EL EJEMPLAR QUE LA ESTRENO: `gates_go_kill_decision_points`**, cuatro pasos.

| paso | que es de verdad |
|---:|---|
| 1. define con claridad cada punto de decision | **una accion unica** |
| 2. preguntate de verdad si sigues o paras, **no solo revises como va** | **una advertencia** |
| 3. **no dejes** que un proyecto avance sin haber decidido | **una advertencia** |
| 4. anota que decidiste, con sus cinco salidas | **una accion unica mas una taxonomia** |

> **Cuatro pasos, y ni uno es un procedimiento.** Contra
> `requisitos_gates_con_dientes`, que tiene **seis condiciones cada una con decisiones
> dentro**, la vara dice **REPITE** sin dudar. **Antes de esta precision, cuatro contra
> seis parecia una comparacion entre iguales.**

### COMO SE APLICA, en una pregunta

> **Quitale al nodo todas las frases que empiezan por NO, por EVITA o por DE VERDAD.
> Lo que queda, es un procedimiento o es una lista de punteros?**

**Si lo que queda cabe en una linea, el nodo es linea**, por muchos pasos que tenga
escritos.

### LO QUE ESTA PRECISION NO AUTORIZA

**No autoriza a borrar las advertencias.** Una advertencia **es lo mas facil de perder
en una fusion y lo mas caro de recuperar**, porque **no se nota que falta**: el
procedimiento sigue completo sin ella y simplemente **se ejecuta peor**.

> **UNA ADVERTENCIA NO DECIDE LA CLASE, PERO SIEMPRE VIAJA.** Es linea para la vara y
> es perdida nombrada para la fusion. **Las dos cosas a la vez.**

---

## P.12 EL CIERRE TRANSITIVO CONVOCA, LA LECTURA DECIDE

**Adoptada el 12 ago 2026, y resuelve la primera contradiccion del plan entre el
conteo y la lectura.**

> **EL BANCO 9.24 DEFINE EL UNIVERSO DEL ACTO, NO LA MEMBRESIA DE LA FUSION.**
>
> El cierre transitivo dice **quienes se leen y se simulan juntos**. **No dice quienes
> se funden.**

### LAS TRES PARTES DE LA REGLA

| | |
|---|---|
| **1. CONVOCA** | el cierre transitivo **junta a todos** los conectados por A, y **asi hay que leerlos y simularlos**: es el universo del acto |
| **2. DECIDE** | **con el acto leido ENTERO, mandan los veredictos DIRECTOS.** Una A que nadie leyo no existe; una A que se leyo, vale por si misma |
| **3. EL MIXTO SE JUZGA CON LA VARA** | un nodo con A y D contra la misma familia **no se decide por conteo**: se lee **contra el superviviente** |

### LA VARA CONTRA EL SUPERVIVIENTE, que es la parte operativa

> **Si el nodo mixto comparte con el superviviente LA IDEA EN LINEAS, CONTINUA:**
> enlace **mas poda del solape**.
>
> **Si comparte PROCEDIMIENTO, ENTRA.**

**NI TRANSITIVIDAD AUTOMATICA NI MAYORIA.** Contar A contra D **es la trampa
elegante**: parece objetivo y **no lee nada**. Dos A pueden ser dos veces la misma
linea, y tres D pueden ser tres veces el mismo procedimiento distinto. **El numero no
sabe cual.**

### EL EJEMPLAR: EL SEXTO DE GATES

**`gestion_de_portafolio_gates_go_kill`**, con **los quince pares de su acto leidos**:

| contra | clase |
|---|---|
| `sistema_gates_go_kill` y `gates_go_kill_decision_points` | **A** |
| `requisitos_gates_con_dientes`, `estructura_gates` y `estructura_de_gates` | **D** |

**Y EL PATRON LO EXPLICA TODO: repite con LA IDEA de puerta y no con su ANATOMIA.**
Sus dos A son contra **los dos nodos mas generales**, los que dicen *que la puerta
exista y que sea firme*. Sus tres D son contra **los tres que dicen como se monta por
dentro**: que entregables, que tipos de criterio, quien aprueba, que salidas hay.

> **Aplicada la vara contra el superviviente: lo que comparte es LA IDEA, y la idea le
> cabe en una linea, su paso 2.** **CONTINUA: enlace mas poda del solape.**

> **Y eso coincide con la frontera de los dos niveles que su propia mesa adopto**: el
> sexto es un nodo **estrategico** y los cinco son **tacticos**. **Cuando la vara y la
> frontera dicen lo mismo, no hay caso.**

### POR QUE ESTA REGLA NO DEBILITA EL 9.24

**El 9.24 sigue siendo lo que era: la unica forma de saber a quien hay que leer
junto.** Sin el, el sexto nunca se habria comparado con los otros cinco **y su
enlace no existiria**.

> **LA FORMA CORTA: EL CIERRE TRANSITIVO ES LA CITACION, NO LA SENTENCIA.**

---

## P.13 LAS PERDIDAS SE RECOMPUTAN SOBRE LA NOMINA FINAL

**Adoptada el 12 ago 2026, y la estreno `LD-61`.**

> **UNA PERDIDA SE DECLARA CONTRA UN PAR Y SE COBRA CONTRA UNA NOMINA.** Cuando la
> nomina de la fusion cambia, **toda perdida listada se vuelve a comprobar contra la
> nomina completa**, y **la que viva dentro se reclasifica con su dueno.**

**LA PERDIDA NO SE PIERDE: CAMBIA DE DUENO.**

### DE DONDE SALE

**`LD-58` dejo como perdida la taxonomia de CINCO salidas**, porque el superviviente
candidato tenia cuatro. **`LD-61` la desactivo**: `estructura_de_gates` **lleva las
cinco**, y esta **dentro de la misma fusion**.

> **La perdida era real contra aquel par y falsa contra esta nomina.** **Y una perdida
> falsa no es inofensiva: obliga a injertar en el superviviente algo que ya esta, y eso
> es como se fabrica una repeticion nueva el dia de la pasada.**

### LAS TRES CLASES QUE EL RECOMPUTO PRODUCE

| clase | que es | que se hace |
|---|---|---|
| **VIAJA** | la pieza **no esta en ningun nodo vivo de la nomina** | se injerta en el superviviente, con su texto |
| **VIVE DENTRO** | la pieza **ya esta en el superviviente o en otro que sobrevive** | **se tacha de la lista** y se anota donde vive |
| **YA NO APLICA** | la pieza era de un nodo que **dejo de entrar en la fusion** | **se retira**: ese nodo sigue vivo y se la queda |

### CUANDO SE CORRE

**Cada vez que cambia la nomina de una fusion**, y **siempre antes de pasarla a
LISTA**. Es barato: **es leer el texto del superviviente con la lista al lado.**

> **Y ES DE LA MISMA FAMILIA QUE P.9: las dos dicen que lo escrito el dia de la
> decision hay que releerlo el dia de la ejecucion.** Una lo dice de los ids, la otra
> de las perdidas.

---

## COROLARIO DE P.13: **UNA FUSION QUE CRECE RE MIDE TAMBIEN A SU SUPERVIVIENTE**

**Registrado el 12 ago 2026.**

> **P.13 dice que al cambiar la nomina se recomprueban las PERDIDAS. El corolario dice
> que tambien se recomprueba EL SUPERVIVIENTE.**

**Y no es lo mismo, porque el superviviente se elige por P.8 CONTRA LOS QUE ESTABAN.**
Meter un miembro nuevo **puede cambiar quien contiene a quien y quien aporta mas**, sin
que ninguna lectura cambie.

### EL EJEMPLAR: EL TRIO DE GATES

| | nomina | superviviente | por que |
|---|---|---|---|
| **como trio** | `requisitos_gates_con_dientes`, `estructura_gates`, `estructura_de_gates` | **`requisitos_gates_con_dientes`** | contenia a los otros dos y aportaba el puente al portafolio y la revision post lanzamiento |
| **como camarilla de cinco** | los tres mas `sistema_gates_go_kill` y `gates_go_kill_decision_points` | **`sistema_gates_go_kill`** | el veredicto 801 mide **TRES piezas propias suyas contra DOS** del otro, sobre un eje que se repite entero |

> **Ninguna lectura cambio. Cambio la nomina, y con ella el ganador.**

**LO QUE ESTO OBLIGA:** cuando una fusion absorbe a otra o gana un miembro, **se
vuelve a correr P.8 EN ORDEN sobre la nomina nueva**, contenido primero. **No se
hereda el superviviente de la operacion pequena.**

> **LA FORMA CORTA: EL SUPERVIVIENTE ES UNA PROPIEDAD DE LA NOMINA, NO DEL NODO.**

---

## FIGURA: **COBRAR UNA A SIN FUNDIR**

**Nombrada el 12 ago 2026 con el sexto de gates, y es la plantilla para todo nodo
mixto que `P.12` deje fuera de una fusion.**

> **Una A es un dato y no una orden.** Dice **que hay un bloque que repite**, no **que
> los nodos sean el mismo nodo.**

### LA PLANTILLA, en tres pasos

| | |
|---|---|
| **1. EL ENLACE** | una arista **de la madre al hijo**, **una sola direccion**, en el sentido que diga la jerarquia |
| **2. LA PODA DEL SOLAPE** | **el bloque que la A senala DEJA DE REFORMULAR** lo que el otro desarrolla, **y pasa a citar la arista** |
| **3. LO PROPIO SE QUEDA** | lo que las D senalan **no se toca**: es el motivo de que el nodo viva |

**EL EJEMPLAR:** `gestion_de_portafolio_gates_go_kill`, con **dos A y tres D** contra
la misma familia. **Sus dos A se cobran en la poda** de su paso 2, *establecer gates
formales con criterios visibles*, **que es el bloque que reformula la idea general de
la puerta**. **Sus tres D son el motivo de que viva**: el embudo, los seis criterios y
el balance del portafolio.

### POR QUE ESTO NO ES UNA FUSION A MEDIAS

**Una fusion resuelve la repeticion BORRANDO UN NODO. Esta la resuelve BORRANDO UN
BLOQUE.** El resultado en el catalogo es el mismo por el lado que importa, **la
instruccion deja de estar dos veces**, y **se conserva lo que la fusion habria
arrastrado**.

> **Y EL COSTE DE NO HACERLO ES DOBLE: el catalogo se queda con el bloque repetido Y
> sin la arista.** Es exactamente el estado en que la mesa unida encontro sus dos
> mitades: **once jerarquias sin cablear y un bloque diciendo lo mismo dos veces.**

**CUANDO SE APLICA:** siempre que `P.12` deje un nodo mixto fuera de la fusion. **No es
una excepcion: es lo que hay que hacer con el que se queda.**

---

## P.14 UN CONTROL QUE SOLO ENCUENTRA FALLOS AJENOS NO ES UN CONTROL

**Adoptada el 12 ago 2026, y la enseno el puesto 1804.**

> **TODO CONTROL REPORTA TAMBIEN LO QUE EL CONTROL FALLO.** Si una relectura de
> veinticuatro pares no encuentra ni una vez que el archivo tenia razon, **lo primero
> que hay que revisar no es el archivo: es la relectura.**

### EL EJEMPLAR

**El puesto 1804**, `gestion_centro_datos_verde` contra
`optimizacion_centro_datos_verde`. **La lectura a ciegas de hoy lo marco como
CAERIA A B**, porque **tres de los cinco pasos del nodo corto son identicos a tres del
largo**: contencion de pasillos, rango de temperatura y economizadores.

**Y la razon vieja traia un eje que la lectura de hoy no vio:**

> *Uno **ATACA EL AIRE Y EL CALOR** y el otro **ATACA LA CARGA**. **Uno enfria mejor lo
> mismo, el otro necesita enfriar menos.***

**Con ese eje nombrado, las tres lineas compartidas son incidentales**: son las medidas
que **cualquiera** de las dos estrategias usa. **El D se sostiene, y la lectura vieja
fue mejor que la de hoy.**

### POR QUE ES UNA REGLA Y NO UNA ANECDOTA

**Un relector llega con las doctrinas nuevas en la mano y con ganas de usarlas.** Eso
**aumenta la sensibilidad y baja la especificidad**: se ve deriva donde hay un eje que
no se supo nombrar.

> **LA CIFRA DEL PROPIO CONTROL LO DICE: de veinticuatro, UNO cayo por doctrina nueva y
> UNO fue error del relector. Uno a uno.** **Si el segundo no se hubiera escrito, la
> tasa publicada seria mejor de lo que es.**

### COMO SE CUMPLE

| | |
|---|---|
| **1** | la relectura se hace **A CIEGAS** y **solo despues** se destapa la razon vieja |
| **2** | **cuando la razon vieja gana, se escribe con su puesto y con el eje que el relector no vio** |
| **3** | **si el control no encuentra ninguno, se dice**, y se toma como senal de que el metodo puede estar sesgado |

---

## P.15 TODA TASA PUBLICADA LLEVA SU BANDA AL LADO

**Adoptada el 12 ago 2026.**

> **UNA TASA SIN INTERVALO NO ES UNA MEDIDA: ES UNA IMPRESION CON DECIMALES.**

**Y el plan ya tiene dos escarmientos propios:**

| | |
|---|---|
| **el cero de veinticuatro** | *cero podas en veinticuatro lecturas* se leyo como un cero **y era un techo del 11,7%**. La clase que decia no existir vale **15,2%** |
| **el 4,2% de las D** | punto en 4,2 **y banda de 0,7 a 20,2**. **Publicar solo el punto haria creer que el error de dejar pasar esta acotado, y no lo esta** |

### LO QUE OBLIGA

| | |
|---|---|
| **1** | **toda tasa del plan lleva su banda**, su **N** y su **fecha de corte**. Las tres, no dos |
| **2** | **una clase con CERO observaciones se escribe como techo**, nunca como ausencia |
| **3** | **si la banda es ancha, se dice que es ancha y por que**: casi siempre es que la muestra es chica y el evento raro, **y eso tambien es un resultado** |

> **Y LA FORMA CORTA, para cuando haya prisa: SI NO CABE LA BANDA, NO CABE LA TASA.**

---

## P.16 QUIEN FABRICA, LIMPIA

**Adoptada el 14 ago 2026, decision del fundador.**

> **TODA OPERACION DE FUSION RETIRA, EN SU MISMO COMMIT, LA ARISTA INTERNA DEL PAR
> QUE SU PROPIA SIMULACION REPORTA COMO AUTO-ARISTA NACIENTE.**

**El motivo esta escrito en `OP-S-07`: las 33 auto-aristas del grafo de hoy no
nacieron de golpe, nacieron una fusion a la vez, y ninguna se limpio en el momento
en que se fabrico.** Cada una quedo esperando a una operacion de saneo posterior
que las barriera todas juntas, y esa espera es lo que las hizo dificiles de
diagnosticar: el nodo se cita a si mismo, pero via alias, y una guarda literal no
lo ve.

**Y no es un solo fenomeno: son dos gemelos, con su operacion de saneo cada uno.**
`OP-S-07` limpia la **AUTO-ARISTA** (el nodo se cita a si mismo tras resolver).
`OP-S-12` limpia la **ARISTA DUPLICADA** (el alias fundido deja un puntero que,
tras resolver, repite el que ya tiene el superviviente). Las dos nacen del mismo
descuido: **una fusion que no retira lo que ella misma vuelve redundante.**

### LO QUE OBLIGA

| | |
|---|---|
| **1** | si `P.7` (la simulacion previa a toda operacion de mesa) reporta que el par a fusionar deja una **arista interna sin retirar**, sea AUTO-ARISTA o ARISTA DUPLICADA, **la operacion la retira en el mismo commit que ejecuta la fusion** |
| **2** | **la limpieza no se aplaza a una operacion de saneo posterior**: aplazarla es exactamente como nacieron las 33 auto-aristas y las 1.056 entradas duplicadas de hoy |
| **3** | **`OP-S-12` pasa de limpieza a VERIFICACION DE CERO**: ya no borra duplicadas acumuladas, **comprueba que no quede ninguna**, porque cada fusion desde esta fecha retira su propio sobrante al fundirse |

> **LA CONSECUENCIA PARA EL PLAN VIEJO: no se toca.** Las 33 auto-aristas y las
> 1.056 duplicadas de hoy siguen siendo trabajo de `OP-S-07` y `OP-S-12`, que ya
> estan escritas y adjudicadas. `P.16` gobierna las fusiones QUE VIENEN, no
> reescribe las que ya pasaron.

---

## P.17 LA LECTURA VENCE AL METADATO

**Adoptada el 14 ago 2026, decision del fundador.**

> **CUANDO UN NODO VIVE EN DOS OPERACIONES, LA PERTENENCIA CONFIRMADA CONTRA LOS
> PASOS CON FRONTERA ESCRITA VENCE A LA ARGUMENTADA POR METADATO (FUENTE, FORMATO,
> FAMILIA).**

**El ejemplar que la trajo: `background_startup_vs_corporativo`.** `OP-F-01` lo
clasificaba en la clase LARGO LEGITIMO por metadato: declara dos libros, y eso
rompia la exclusividad de los manuales. `OP-F-04-HOR` lo tenia LEIDO Y CONFIRMADO
como injerto de Horowitz, con su frontera de paso publicada (1 a 4 de Wasserman, 5
a 9 de Horowitz). **Las dos lecturas eran ciertas el mismo dia, y se contradicen**:
por `P.3` el bloque del mismo tema se reparte obligatoriamente, y repartir tumba la
clase; quedarse en la clase deja el injerto sin destejer.

### LO QUE OBLIGA

| | |
|---|---|
| **1** | ante la contradiccion, **gana la operacion que confirmo la pertenencia leyendo los pasos del nodo y publico una frontera**, no la que la argumento por un dato del nodo (de que libro sale, que formato tiene, a que familia pertenece) |
| **2** | **la operacion perdedora corrige su nomina y su verificacion por CORRECCION DECLARADA**, sin borrar el texto viejo: la lectura que la sostenia no era falsa, solo perdio frente a una lectura mas fuerte |
| **3** | la prosa que citaba al nodo perdedor como ejemplo **se corrige declarada en el mismo lugar**: el argumento general puede sobrevivir con otro ejemplar, y eso se dice, no se calla |

> **ALCANCE, escrito el mismo dia de la adopcion:** ademas del ejemplar que la
> trajo, `P.17` gobierna **los tres cruces ya declarados de `OP-F-03`**
> (`principio_calidad_mvp` con `OP-D-01` y `OP-D-06`, `producto_unico_superior` y
> `propuesta_gasto_capital` con `OP-D-06`), donde ya manda el orden fuente primero,
> y **cualquier cruce futuro** que el plan descubra entre una operacion de fuente y
> una de destejido o fusion.

---

## P.18 EL DESTINO SE DECIDE POR LECTURA DE OBJETO

**Adoptada el 14 ago 2026, decision del fundador.**

> **DENTRO DE LA FAMILIA QUE LA FRONTERA NOMBRA, EL BLOQUE VA AL MIEMBRO CUYO
> OBJETO COINCIDA, DECIDIDO POR LECTURA SOBRE LA NOMINA VIGENTE AL DIA. SI NINGUNO
> COINCIDE, FORMA NODO PROPIO EN ESA FAMILIA.**

**El motivo:** `P.3` resuelve la separacion de un bloque hasta el nivel de familia;
no dice a que MIEMBRO de esa familia va. Elegir el miembro es una decision de
contenido, y esa pluma no era del ejecutor ni del auditor. **Primer ejemplar:
`OP-F-02`**, donde el fundador escribio la regla el 14 ago 2026 para el racimo de
supervision de la IA antes de que `P.18` tuviera numero propio.

### LO QUE OBLIGA

| | |
|---|---|
| **1** | la lectura se hace sobre la **nomina vigente al dia en que se ejecuta la operacion**, no sobre una nomina publicada en otra fecha: si la familia crecio o se partio desde que se escribio la evidencia, se lee de nuevo |
| **2** | **el miembro elegido, o la creacion del nodo propio, se escribe como CORRECCION DECLARADA al ejecutar**, con la lectura que lo sostiene: no basta con nombrar el miembro, hay que decir POR QUE su objeto coincide |
| **3** | si ningun miembro coincide, **el bloque forma nodo propio dentro de la familia**: no se fuerza un encaje que la lectura no sostiene |

> **ALCANCE, escrito el mismo dia de la adopcion:** ademas de `OP-F-02`, `P.18`
> gobierna el destino de las cuatro `OP-F-04` (`OP-F-04-COL`, `OP-F-04-HOR`,
> `OP-F-04-WEI`, `OP-F-04-RAC`) cuando su bloque apendice va a una familia y no a
> nodo propio, y el reparto de `OP-F-03` hacia la subfamilia Hugos del nucleo y
> hacia la familia HUGOS-SISTEMAS (ver la correccion declarada en la nota de
> `OP-F-03`).

---

## P.19 LA REPETICION INTERNA SE FUNDE, NO SE DESTEJE

**Adoptada el 14 ago 2026, decision del fundador.**

> **CUANDO MATERIAL DE DOS O MAS FUENTES DENTRO DE UN NODO REPITE EL MISMO
> OBJETO, NO VA A NINGUN DESTINO: SE FUNDE EN UN SOLO PROCEDIMIENTO DENTRO DEL
> NODO.**

**El motivo:** `P.18` decide DONDE VA un bloque cuando su objeto no repite el del
nodo que lo contiene (a un miembro de la familia, o a nodo propio). Pero cuando el
bloque repite EL MISMO OBJETO que ya vive en el nodo, `P.18` no tiene pregunta que
contestar: no hay destino que buscar, porque **el objeto ya esta en casa**. Mandarlo
a nodo propio fabrica el gemelo exacto del propio donante; forzarlo a un miembro
ajeno es el encaje que `P.18` punto 3 ya prohibe. **Las dos salidas de `P.18`
chocaban porque la pregunta no era de `P.18`.**

### LO QUE OBLIGA

| | |
|---|---|
| **1** | el material repetido se funde **en un solo procedimiento dentro del nodo**, con el mapa de destejido (cada paso destino declara sus origenes, nada se poda) |
| **2** | el nodo queda **MULTIFUENTE LEGITIMO**, con la **procedencia declarada por bloque**: de que libro sale cada tramo del procedimiento fundido |
| **3** | las diferencias entre versiones (una mas completa, un paso que solo una version trae) **se reparten por la tabla de seis motivos de perdida de linea**, igual que cualquier fusion |
| **4** | el destejido con destino de `P.18` **sigue vigente para el material AJENO al objeto** del nodo: esta regla no lo reemplaza, lo complementa. Un mismo nodo puede tener un bloque que se funde (mismo objeto) y otro que se desteje a otro destino (objeto ajeno) |

**EJEMPLARES: `coeficiente_viral` y `decision_de_vender_startup`.** Los dos traian el
mismo calculo (K, el precio minimo, la disposicion del equipo) repetido varias veces
dentro del propio nodo, de mas de un libro. Ninguno tenia destino: los dos se funden.

---

## P.20 UN NODO, UN CORTE

**Adoptada el 14 ago 2026, decision del fundador.**

> **CUANDO UN NODO PERTENECE A DOS OPERACIONES DE DESTEJIDO, NO SE CORTA DOS
> VECES NI EN ORDEN: LA FRONTERA COMPLETA (TODOS LOS LIBROS) SE PUBLICA COMO
> REGISTRO UNICO, Y EL CORTE SE EJECUTA UNA VEZ, CITADO POR LAS DOS OPERACIONES
> CON CORRECCION DECLARADA.**

**El motivo:** el precedente de `fuente primero` (`01_FUENTES.md`) resuelve el orden
entre decisiones de fuente y destejidos que dependen de ellas, pero no dice que
pasa cuando el MISMO nodo tiene material de tres libros repartido entre DOS
operaciones de destejido distintas: cortar dos veces partiria el mismo bloque en
pedazos incompatibles, y cortar en orden dejaria a la segunda operacion leyendo un
nodo que la primera ya movio.

### LO QUE OBLIGA

| | |
|---|---|
| **1** | la frontera se lee **entera, los tres o mas libros a la vez**, antes de cortar nada |
| **2** | se publica **como registro unico** (en `01_FUENTES.md`, con el metodo de la tabla de los 14 de Horowitz) |
| **3** | el corte se ejecuta **UNA sola vez** |
| **4** | las dos operaciones **citan el mismo corte** con correccion declarada en su nota, en vez de cada una escribir el suyo |

**Y donde `P.19` y `P.18` entran, en el mismo corte:** lo que repite el mismo objeto
entre los libros **se funde** por `P.19`; lo que es ajeno al objeto del nodo **se
desteje con destino** por `P.18`. Un nodo de dos operaciones puede necesitar las dos
reglas a la vez, cada una sobre su propio tramo.

**EJEMPLAR: `viral_loop_marketing`** (30 pasos, tres libros, pertenece a
`OP-F-04-COL` y a `OP-F-04-WEI`). Primero se publica la frontera de los tres libros
como registro unico; en el corte, el material del promotor que repite entre 9 a 13,
14 a 17 y 18 a 21 se funde por `P.19`, y lo ajeno al objeto se desteje por `P.18`.
