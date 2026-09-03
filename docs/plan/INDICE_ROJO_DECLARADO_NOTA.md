# NOTA DE `INDICE_ROJO_DECLARADO.jsonl`: LA LISTA QUEDA VACIA (3 sep 2026)

**CORRECCION DECLARADA POR ADICION. Nada del texto anterior se borra: la lista vieja
queda entera aqui abajo, tachada.**

## POR QUE LA NOTA VIVE AQUI Y NO DENTRO DEL `.jsonl`

Porque el lector no lo permite, y esta medido, no supuesto.
`indice_rojo_declarado()` en `scripts/run_phase1.py` (lineas 731 a 751) salta
**solo las lineas vacias** y hace `json.loads` de **toda** linea no vacia. Una linea
de comentario o una nota en prosa dentro del `.jsonl` **tumbaria Gate 0 con un error
de parseo**. Asi que el `.jsonl` queda **vacio de verdad** y el registro vive en este
fichero hermano, con su nombre, al lado.

## LA LETRA QUE MANDA VACIARLA

El docstring del propio lector lo dice, y es la vara de este acto:

> *"Al cierre de la FASE III esta lista tiene que quedar VACIA, con el reindexado
> hecho y Gate 0 entero en verde (`docs/plan/08_VERIFICACION.md`)."*

Y la decision del fundador que la funda, del **14 ago 2026, opcion B extendida**:
el rojo declarado vale **exclusivamente para los ids que la pasada acaba de crear**, y
**cualquier otro id en rojo en el chequeo del indice es PARADA**.

## LO MEDIDO EL 3 SEP 2026, EN LA SESION CON CREDENCIAL

**Los DIECIOCHO ids de la lista tienen hoy su vector.** Medido contra
`web/lib/assets/semantic_index.json` recien reconstruido: **18 de 18 con vector, 0 sin
vector**, y **los 18 siguen vivos en el grafo**. El reindexado del paso 2 de esta
sesion metio los 18 y saco los 370 deprecados en la misma pasada, como el acta 149
seccion 3.11 adjudico.

**Por eso la lista se vacia: ya no queda un solo id que declarar.** No se vacia por
conveniencia ni para que una guarda pase; se vacia porque **su motivo se consumio**.

## LA LISTA VIEJA, ENTERA Y TACHADA (18 entradas, 14 ago 2026)

~~`escenarios_de_evolucion_de_la_ia`, `OP-F-02`, 2026-08-14~~
~~`critica_del_plan_con_ia`, `OP-F-02`, 2026-08-14~~
~~`ideacion_con_ia_en_la_sesion`, `OP-F-02`, 2026-08-14~~
~~`estrategia_circular_y_mecanismo_de_retorno`, `OP-F-03`, 2026-08-14~~
~~`seleccion_de_proveedores_por_costo_total`, `OP-F-03`, 2026-08-14~~
~~`driver_de_inventario`, `OP-F-03`, 2026-08-14~~
~~`producto_como_servicio_de_acceso`, `OP-F-03`, 2026-08-14~~
~~`anillo_interior_explotar_el_canal_nucleo`, `OP-F-04-WEI`, 2026-08-14~~
~~`inteligencia_de_anuncios_de_la_competencia`, `OP-F-04-WEI`, 2026-08-14~~
~~`puntos_brillantes_antes_del_pivote`, `OP-F-04-WEI`, 2026-08-14~~
~~`estar_listo_para_ser_publica`, `OP-F-04-HOR`, 2026-08-14~~
~~`formalizar_un_proceso_ad_hoc`, `OP-F-04-HOR`, 2026-08-14~~
~~`la_historia_de_la_empresa`, `OP-F-04-HOR`, 2026-08-14~~
~~`personalizacion_guiada_por_el_cliente`, `OP-F-04-COL`, 2026-08-14~~
~~`silla_vacia_del_cliente_en_decisiones`, `OP-F-04-COL`, 2026-08-14~~
~~`incentivos_internos_alineados_a_retencion`, `OP-F-04-COL`, 2026-08-14~~
~~`autoservicio_y_autosanacion_del_producto`, `OP-F-04-COL`, 2026-08-14~~
~~`observar_al_cliente_en_su_contexto`, `OP-F-04-COL`, 2026-08-14~~

**LO QUE NO CAMBIA:** el mecanismo sigue vivo y con dientes. Si una pasada futura crea
un nodo, vuelve a escribir su linea aqui, y **cualquier id sin vector que NO este
declarado sigue siendo rojo que para**. Vaciar la lista no afloja la guarda: la deja
sin nada que restar.
