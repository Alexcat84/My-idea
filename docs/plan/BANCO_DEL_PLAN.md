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
