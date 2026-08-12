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
