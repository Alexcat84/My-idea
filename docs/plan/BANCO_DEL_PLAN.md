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
