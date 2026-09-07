# -*- coding: utf-8 -*-
r"""_gen_v202_esqueleto_piezas.py . LAS TRES PIEZAS QUE CAMBIAN DEL ESQUELETO DE
LA VUELTA 202 RESPECTO AL DE LA 201.

Fichero de computo con PREFIJO DE GUION BAJO: fuera del censo y fuera de la
nomina. No es un arnes ni una guarda ni un lector: es el molde del que sale
`scripts/loop/vuelta202_esqueleto_reporte.py`, que se genera de la 201 copiando
todo lo demas BYTE A BYTE.
"""
NL = chr(10)

DOCSTRING = r'''r"""vuelta202_esqueleto_reporte.py . EL ESQUELETO DEL REPORTE DE LA VUELTA 202,
TALLADO EN LA APERTURA Y EN SU PROPIO COMMIT PARA QUE UNA VUELTA CORTADA DEJE
REPORTE PARCIAL Y NO VACIO.

CLON DECLARADO de scripts/loop/vuelta201_esqueleto_reporte.py, generado de el
programaticamente con `scripts/loop/_gen_v202_esqueleto.py`. Cambia el numero de
vuelta, la lista TAREAS, este docstring y el bloque de prosa del encabezado. EL
CODIGO DE LAS FUNCIONES VA IGUAL, byte a byte, porque se copio y no se re
escribio.

POR QUE CUATRO TAREAS, Y LA CIFRA NO SE TECLEA: la racha de cierres, contada del
instrumento en el bloque `E` del sello de apertura de ESTA vuelta, vale 3, con
las vueltas 199, 200 y 201. `AUDITOR.md` 6.2 apaga el regimen temporal de dos
sub-tareas cuando DOS VUELTAS SEGUIDAS cierran su propio reporte con
`cerrar_reporte.py`, y con racha 3 SE APAGA y vuelve el tope de CINCO. El encargo
trae CUATRO. LA CIFRA SE LEE DEL SELLO, con `racha_del_sello()`, y si el sello no
la trae este esqueleto CAE EN ROJO y no escribe nada.

Y ESTA NO ES VUELTA DE BATERIA: la 200 lo fue y cerro entera, y por la cadencia
de `AUDITOR.md` 6.1 le toca a la 205. La seccion 9 cierra con el HUECO DECLARADO
Y MEDIDO por el carril de `cerrar_reporte.py`. El trabajo de esta vuelta es EL
PLAN, que es lo que la moratoria 6.3 manda.

EL DESFASE DE `PATRONES_ACTA` NO APARECE EN ESTA VUELTA, Y ESO SE MIDE EN VEZ DE
SUPONERSE: `PATRONES_ACTA` pide el acta de `VUELTA - 1`, o sea la 201, y el acta
que ORDENA esta vuelta ES la 201 (la 202 no existe todavia, y el bloque `H.2` del
sello de apertura lo cuenta: 1 acierto para la 201 y 0 para la 202). El literal
`DESFASE DECLARADO` se sigue CONTANDO de los reportes archivados, con su fecha de
corte, porque esa cifra es de inventario y envejece sola.

LA FUNCION PURA VA CLONADA A PROPOSITO, Y SE DECLARA:
vuelta_del_reporte_del_arbol esta copiada de vuelta174_esqueleto_reporte.py en
vez de importada, y la guarda que CAE EN ROJO si esa fuente desaparece la
escribio la TAREA 4.b de la vuelta 180: corre aqui como PASO 0.0.

USO:
  python scripts/loop/vuelta202_esqueleto_reporte.py
"""'''

TAREAS_TXT = '''TAREAS = [
    ('1', 'LA CORRECCION DECLARADA DE LA `evidencia` DE `OP-L-03`, EN SU SEDE, adjudicada por el acta 201 en su `4.3`. **EL CARRIL ES EL DE `OP-I-01` DE LA VUELTA 201**: banco `9.10`, **POR ADICION**, como **un elemento mas de la misma lista `evidencia`**, **sin clave nueva de esquema** y **sin tocar ni tachar el texto viejo**, que es la via de la gemela `OP-L-01` en la vuelta 166 que el **acta 71, seccion 6, adjudicacion 3** adjudico con las palabras **NO ES PARADA**. Tiene que decir **TRES cosas**: que el documento que la `evidencia` nombra trae **0** veces `reparto por acto` y **0** menciones de `OP-L-03`, **medidas aqui**; que el reparto por acto vive en `docs/plan/OP_L_03_LECTURAS.jsonl` y `docs/plan/OP_L_03_TRIANGULOS.jsonl`, **nombrados los dos** y con **sus bytes exactos** (`P.2`); y **la cobertura real con su fecha de corte**, porque la evidencia promete **55 pares en 29 actos** y el fichero trae otra cifra. **GUARDA OBLIGATORIA Y CORRIDA DOS VECES**, la misma que la 201 uso para `OP-I-01`. **NINGUN campo `estado` se mueve**'),
    ('2', '`OP-L-02` CONTRA EL CRITERIO DE HECHO, ahora que su clausula 1 esta medida por el acta 201 en su `4.1`. **LO PRIMERO Y SIN CLONAR NADA**: se **importan** y se corren `scripts/loop/vuelta169_tarea5_cobertura_op_l_02.py` y `scripts/loop/vuelta170_tarea5b_veredicto_op_l_02.py`, comprobado ANTES que **ninguno escribe ficheros**, y **ninguno se toca**. Las tres clausulas se miden contra el criterio de hecho de `docs/plan/08_VERIFICACION.md` **citado por linea**, y se citan por **linea 42 mas indice**. **LA CLAUSULA 2 TRAE UNA TRAMPA YA MEDIDA** (acta 201, `4.2`): el instrumento la da `NO CUMPLIDA` porque diffea contra `46208790`, un HEAD de la vuelta 170. **Se remide contra el HEAD de apertura de ESTA vuelta**, leido del sello, y **se publican las dos lecturas juntas** con la discrepancia declarada. **NO SE ARREGLA EL INSTRUMENTO: LA MORATORIA LO PROHIBE.** Si las tres quedan cumplidas, **SE PROPONE Y NO SE CIERRA**'),
    ('3', '`OP-L-01` CONTRA EL CRITERIO DE HECHO, Y EL HUECO DE LA VIGENCIA, adjudicada por el acta 201 en su `4.8`. Sus **cuatro pruebas de cobertura** estan cubiertas y el auditor las reprodujo las cuatro, pero **eso es PRESENCIA y no CALIDAD**. Se mide contra el criterio de hecho de `docs/plan/08_VERIFICACION.md` **citado por linea**, con su `verificacion` citada por **linea 41 mas indice**. **Y SE MIDE EL HUECO QUE LA 201 NOMBRO Y NADIE HA MEDIDO**: la **TABLA VIVA DE LOS PUROS** de `docs/BANCO_DE_TEXTOS.md` (linea **938**) declara `vigente al puesto 1157` y el marcador de hoy vale otra cosa; **las dos cifras se recuentan aqui**, y se mide **cuantas filas de esa tabla siguen en pie al corte de hoy y cuantas no**, con el **resolutor delante por `P.1`** si el conteo toca ids. **SI EL HUECO PIDE MOVER UNA CLASE, NO SE MUEVE**: mover una clase es del RECOMPUTO, se nombra y se para ahi. **PROPONE, NO CIERRA**'),
    ('4', 'LOS REGISTROS. `R.63` Y `R.64`, LAS DOS MAS VIEJAS DE LA DEUDA, adjudicada por el acta 201 en su `4.9`: la deuda son **8 actas seguidas, las 173 a 180**, y se pagan **DE LA MAS VIEJA A LA MAS NUEVA, DOS POR VUELTA**. Va **DETRAS** del trabajo de plan y nunca delante. `R.63` para el **acta 173** y `R.64` para el **acta 174**, en `docs/PENDIENTES.md`. **NINGUN LECTOR NUEVO**: los que el computo necesita **se importan**, como hizo la 201. **Cada acta se acota EN ESTA VUELTA** por linea de inicio y fin, con su reparto de adjudicaciones, hallazgos, preguntas, caidas del auditor y caidas del ejecutor. **SI EL REPORTE ARCHIVADO NO EXISTE, NO SE FABRICA**: se declara la ausencia medida con `os.path.isfile` y `os.path.getsize`, y se usa la vara que el acta 201 dejo escrita en su `4.7`. **Cierra con la serie medida**: entradas, colisiones, huecos y siguiente libre'),
]'''

PROSA = '''> **ESTE REPORTE SE ABRIO AL EMPEZAR LA VUELTA Y CRECE POR ANEXION** (`EJECUTOR.md`
> 1, "EL REPORTE ABRE CON LA VUELTA"). El esqueleto lo tallo
> `scripts/loop/vuelta%(v)d_esqueleto_reporte.py`; cada tarea ANEXA SU FILA AL
> CERRARSE; y el cierre lo talla entero `scripts/loop/cerrar_reporte.py`. **Si esta
> vuelta se corta, las filas que sigan diciendo ABIERTA, SIN CERRAR son las que no
> se hicieron.**
>
> **ESTA NO ES VUELTA DE BATERIA, Y ESO NO ES UNA OMISION SINO LA CADENCIA.** La
> 200 lo fue y cerro entera; `AUDITOR.md` 6.1 dice que la bateria corre **cada
> cinco vueltas**, en vuelta propia, y por esa cadencia **le toca a la 205**. Aqui
> la **seccion 9 cierra igual**, con el **HUECO DECLARADO Y MEDIDO** por el carril
> de `cerrar_reporte.py`, que lleva **su nombre, sus bytes medidos y su atribucion,
> las tres juntas, o no vale**. El bloque `I` del sello de apertura ya lo midio:
> **0 ficheros `SALIDA_V%(v)d_BATERIA_TRAMO_N.txt`** y
> **`docs/loop/SALIDA_V%(v)d_BATERIA.txt` NO EXISTE**.
>
> **Y RIGE LA MORATORIA DE MAQUINARIA** (`AUDITOR.md` 6.3, decision del fundador
> del 7 sep 2026): **no se fabrican arneses, guardas ni lectores nuevos**, y **esta
> vuelta NO TIENE NINGUNA EXCEPCION**. Lo que hace falta **se importa**, y los dos
> instrumentos de `OP-L-02` se corren **sin clonarlos y sin tocarlos**. **La nomina
> queda CONGELADA EN 135**, y el bloque `F` del sello de apertura la midio contra
> ese congelado sin tocarla. **EL TRABAJO ES EL PLAN**, que es para lo que el bucle
> existe.
>
> **EL TOPE DE SUB-TAREAS ES CINCO, Y LA CIFRA QUE LO MANDA NO SE TECLEA.**
> El bloque `E` del sello de apertura de esta vuelta corrio el instrumento de la
> racha sobre el inventario ENTERO y **la racha de cierres vale %(racha)s**, con las
> vueltas **%(cuales)s**. `AUDITOR.md` 6.2 apaga el regimen temporal de dos
> sub-tareas cuando **DOS vueltas seguidas** cierran su propio reporte con
> `cerrar_reporte.py`, y con **%(racha)s** **SE APAGA**. **Este encargo trae CUATRO,
> y cabe.**
>
> **EL BLOQUE DE APERTURA CORRIO EL CICLO COMPLETO, `tsc` Y `pnpm test`
> INCLUIDOS**, y **escribio el mismo los dos literales que la guarda `D.1` de
> `cerrar_reporte.py` busca en la seccion 4**. **El desfase de calibrado se midio
> DENTRO del bloque de apertura y ANTES de la primera operacion.** Y su bloque `F`
> publica la cifra de arneses del censo fuera de la nomina **con su vara al lado y
> las dos medidas**: con vara **%(vara)s** salen **%(conv)s** y sin vara salen
> **%(sinv)s**. **Esas son las cifras de HOY.**
>
> **LO QUE EL ACTA 201 ADJUDICO NO SE VUELVE A LEVANTAR AQUI.** Su `4.1` disuelve
> la unica parada que la 201 levanto: `OP-L-02` **si se puede medir sin decidir**,
> porque sus seis nominas viven **por id** en la constante `NOMINAS_OP_L_02`. Su
> `4.2` declara **FALSO ROJO** el `NO CUMPLIDA` de la clausula 2, porque el
> instrumento diffea contra un HEAD sellado en la vuelta 170. Y su `4.4` fija la
> convencion: **la coordenada de una ficha JSONL es LINEA MAS INDICE**, y aqui se
> usa **publicando las dos numeraciones del indice** para que ninguna cita quede
> ambigua.
>
> **LO QUE NO ENTRA:** ni cribado, ni recomputo, ni **podar la nomina**, ni **mover
> un solo campo `estado`** (la vara del trabajo pendiente es
> `scripts/loop/vuelta150_3_relectura_expediente.py`, nunca el campo, por el
> recuadro de `AUDITOR.md` 0), ni **cerrar ninguna ficha por cuenta del ejecutor**:
> lo que estas tareas producen es **lectura medida**, y si de ella sale que una
> ficha esta cumplida, **se propone con su evidencia y lo adjudica el auditor**. **Y
> siguen fuera, nombradas para que la 203 no las redescubra:** la **reparacion del
> HEAD envejecido** de `vuelta170_tarea5b_veredicto_op_l_02.py`; el **cierre del
> turno del auditor que se reabre despues de declarar las clases**; los **dos
> arneses que el censo ve y la nomina congelada no tiene**
> (`vuelta197_tarea2_mutacion_orden_del_turno.py` y
> `vuelta199_tarea1_mutacion_guardas_revividas.py`); **las dos paradas que levanto
> la 200**; y **QUE HACER CON LAS FILAS `B` DEL ARCHIVO**. **Las tres primeras son
> de codigo y van a la auditoria integral: la moratoria las prohibe hoy.**
>
> **NO SE MUEVE NINGUNA CLASE Y NINGUN VEREDICTO:** el `sha256` LF de
> `docs/INTRA_DOMINIO_VEREDICTOS.jsonl` abre y tiene que cerrar en el mismo valor,
> y **las dos convenciones se publican**. **Y no se toca `dataset/` a mano**: el
> `numstat` de `dataset/`, `web/`, `engine/` y `docs/plan/` se mide al entrar y al
> salir y **las dos cifras se publican**.'''
