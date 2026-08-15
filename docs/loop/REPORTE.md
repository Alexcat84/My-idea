# REPORTE DE LA VUELTA 31 (ejecutor Opus 5). FASE III, rama `pasada-unica`

**`OP-F-04-COL` QUEDA ENTERA y con ella LA FASE 01 CIERRA: las siete operaciones de fuente
hechas, con la tabla del cierre recomputada al cerrar. El modo continuo avanzo a la FASE 02 y
se detuvo en su PRIMERA operacion: `OP-D-01` no se puede ejecutar tal como esta escrita, y va
como PARADA con sus tres motivos medidos, no arreglada.**

- **Hash de partida:** `ad0b30c7` (el acta de la vuelta 30 del auditor).
- **Hash final:** `35fed793`. **Cinco commits de trabajo**, todos en `origin/pasada-unica`.
- **Rutas tocadas** (`git diff --stat ad0b30c7..HEAD`, corrido hoy): **84 ficheros, 5.932
  insertadas, 365 borradas**. Por carpeta: `dataset/nodos` **35**, `docs/loop` **34**,
  `scripts/loop` **5**, `docs/plan` **4**, `web/lib` **3**, `dataset/metadata` **2**,
  `engine/node_families.json` **1**. **Cero merges.** El hook activo (`core.hooksPath =
  .githooks`) y corrido en los cinco commits.

---

## 1. EL ESTADO, APERTURA CONTRA CIERRE

**LAS DOS COLUMNAS SON DE DOS CORRIDAS DISTINTAS, la de APERTURA corrida ANTES de la primera
operacion** (`scripts/loop/vuelta30_estado.py`, salida `SALIDA_V31_APERTURA.txt`, commiteada en
`0ee5c1e8` **antes** de tocar nada) **y la de CIERRE corrida al cerrar**
(`scripts/loop/vuelta31_estado.py`, salida `SALIDA_V31_CIERRE.txt`), que es lo que los tres
renglones de la regla 1 obligan. **Ninguna cifra viene del acta 30 ni de un reporte anterior.**

> **EL INSTRUMENTO CAMBIO ENTRE LAS DOS COLUMNAS, y se dice antes de leer la tabla:** el de
> cierre es el **sucesor declarado** del de apertura, y **lo unico que cambia es el detector de
> fronteras** (TAREA 1.4). Todo lo demas mide igual, linea por linea. **La fila de fronteras es
> la unica que no es comparable entre columnas**, y por eso lleva las dos cifras con el nombre
> de su detector.

| | **APERTURA** | **CIERRE** |
|---|---:|---:|
| marcador: n / A / B / C / D | 3.388 / 583 / 89 / 7 / 2.709 | **igual** (esta vuelta no leyo pares) |
| huecos / duplicados / clases fuera de ABCD | 0 / 0 / 0 | **0 / 0 / 0** |
| grafo: ficheros / ids / vivos / deprecados | 3.848 / 3.848 / 3.534 / 314 | **3.853 / 3.853 / 3.539 / 314** |
| enlaces / claves distintas | 16.832 / 15 | **16.848 / 15** |
| familia Weinberg (vivos, fuente unica) | 72, 70 | **72, 70** |
| familia Horowitz | 93, 91 | **93, 91** |
| familia Hugos | 111, 111 | **111, 111** |
| **familia Coleman** | 83, 68 | **75, 73** |
| familia Rackham | 47, 47 | **47, 47** |
| operaciones / estados / dependencias rotas | 71, todas LISTA, 0 | **71, todas LISTA, 0** |
| inventario | 672 | **672, identico** |
| **indice rojo declarado** | **13 lineas**, 0 ausentes | **18 lineas**, 0 ausentes |
| fronteras de `OP-F-04-COL` | **13 de 15** (detector de UNA forma) | **14 de 15** (detector de DOS formas) |

**LA FAMILIA COLEMAN BAJA DE 83 A 75 VIVOS Y SUBE DE 68 A 73 UNICOS, y las dos cifras son la
firma de lo que la vuelta hizo:** **13 donantes dejaron de declarar a Coleman** porque su
bloque se fue a su destino (83 menos 13 son 70) y **nacieron 5 nodos propios** que si lo
declaran (70 mas 5 son 75). Los unicos suben porque los 13 que salieron eran multifuente y los
5 que entraron son de fuente unica (68 mas 5 son 73). **Es la contraria exacta de la firma de
`P.19` en la vuelta 30, donde las familias no se movian: aqui el material SI sale del nodo.**

**EL CENSO SE MOVIO (3.848 a 3.853), Y POR ESO EL CUARTO COMANDO DE `Gate 0` SI APLICA** esta
vuelta, al reves que en la 30. Se corrio, en su sitio: despues del 2 y antes del 3.

---

## 2. TAREA 1, LOS REGISTROS

1. **`OP-F-04-WEI`, `OP-F-04-HOR` y `OP-F-04-RAC` quedan HECHAS** en su campo `nota`
   (`scripts/loop/vuelta30_nota.py`, correccion declarada anadida al final, **texto viejo entero
   delante**). Las dos primeras citan la **adjudicacion 1 del acta 30 con sus palabras**, leida
   hoy en la **linea 6605**. **Y las tres llevan la medicion del dia al lado, re-corrida por mi
   contra el grafo**, que es lo que la regla 1 obliga: **WEI 11 mas 2 de 13, HOR 12 mas 1 de 13,
   RAC 4 de 4, cero pendientes las tres** (`SALIDA_V31_SALDO_WEI/HOR/RAC.txt`).

   > **UNA DISCREPANCIA DECLARADA EN VEZ DE RESUELTA COPIANDO, y es del propio encargo.** El
   > encargo manda declarar `RAC` HECHA *citando las actas 27 y 29, que ya la adjudicaron*.
   > **Barrido hoy el tramo entero del acta 27 (lineas 5654 a 5943): NO trae la declaracion
   > literal de HECHA para `RAC`.** Lo que trae son las dos verificaciones que la sostienen, y
   > se citan como lo que son: la **linea 5688** (el plan sellado `PLAN_V27_OPF04_RAC.json`
   > existe) y la **linea 5709** (*los casos positivos: las seis salidas, ANTES con pruebas que
   > CAEN, DESPUES con TODO PASA, para `OP-F-02`, `OP-F-03` y `OP-F-04-RAC`*). **La declaracion
   > explicita nace en el acta 29, linea 6390** (*`OP-F-04-RAC` ya era HECHA desde la 27*) **y
   > se reafirma en la 30, linea 6608.** No cambia el resultado (dos actas la declaran y la
   > tercera la verifica, y mi medicion de hoy da 4 de 4), pero **se escribe.**

2. **La `adjudicacion` del 11 ago de `OP-F-04-COL` queda corregida en su nota: son 14 de 15**,
   no 15, y `keep_customers_strategy` trae el material **EMBEBIDO**. El campo viejo se queda
   entero. **Verificado por mi con instrumento, no copiado:** `git log --follow` sobre
   `dataset/nodos/keep_customers_strategy.json` da como commit mas reciente **`33265c05`, del
   2026-08-08**. **El nodo no cambio entre el 11 ago y hoy: lo que cambio es que se volvio a
   leer.** Correccion sobre evidencia de la fase de plan, anterior al bucle.

3. **La adjudicacion 2 del acta 30 esta publicada VERBATIM en `01_FUENTES.md`**, junto al
   hallazgo de `keep_customers_strategy` (leida hoy en su **linea 6610**), **con la marca
   DISCUTIBLE al lado** y los limites escritos: si una lectura futura declara ahi un tramo AJENO
   al objeto, entra por **la segunda puerta de la cola**; separar material embebido ajeno sigue
   sin pagina y **ninguna pagina vigente lo ordena hoy**, asi que no bloquea nada.

4. **El detector de fronteras ampliado**, en `scripts/loop/vuelta31_estado.py`, **sucesor
   declarado con el cambio y su motivo dentro del script**. Reconoce la **FORMA B** que `P.20`
   estreno (**el id en un ENCABEZADO y la particion en el cuerpo de esa subseccion**, delimitada
   por el siguiente encabezado de nivel igual o superior). **No se aflojo el patron de particion
   ni se metio ninguna excepcion por nombre de nodo:** si manana otro nodo publica asi, el
   detector lo cuenta solo. **Verificado: da 14 de 15 con `keep_customers_strategy` como el
   unico NO**, y `viral_loop_marketing` reconocido por FORMA B en las lineas 797 y 802.

5. **Punto 5 del encargo, cumplido por omision y se dice:** `P.20` **no se toco** (cero
   ediciones en `BANCO_DEL_PLAN.md` esta vuelta) y **el valor `HECHA` del campo `estado` no se
   estreno**: las **71** operaciones siguen en `LISTA`, medido al cierre, y las cuatro
   declaraciones de HECHO viven en el campo `nota` citando el acta.

---

## 3. TAREA 2, `OP-F-04-COL` SEGUNDO TIEMPO

**TRECE bloques, VEINTICUATRO cortes, VEINTIUN nodos receptores, 67 pasos movidos.** La nomina
de la familia Coleman se midio **HOY y antes de decidir un solo destino** (`83 nodos vivos, 68
con fuente unica`, `SALIDA_V31_FAMILIA_COLEMAN.txt`), que es la letra de `P.18` punto 1. La
cuenta de trece la confirmo la **adjudicacion 5 del acta 30**, leida hoy en su **linea 6639**.

**LOS SUBBLOQUES.** `blueprint_de_experiencia` se partio en **SEIS** subbloques por objeto y
otros tres bloques en dos. El encargo lo autoriza y el motivo estaba publicado antes de
partirlo: **la frontera es de LIBROS y el destino es de OBJETOS**, y la propia fila de la tabla
de `01_FUENTES.md` ya declaraba que su `5 a 17` trae *la postventa, el momento del si, el ritual
de bienvenida y los cien dias*.

**LOS CINCO NODOS PROPIOS, por `P.18` punto 3**, cada uno con los candidatos descartados por
nombre dentro de su corte, y los cinco declarados en `INDICE_ROJO_DECLARADO.jsonl`:

| nodo propio | de donde | la ausencia que tapa |
|---|---|---|
| `observar_al_cliente_en_su_contexto` | `voz_del_cliente_voc` 6 a 10 | **el mas medible de los cinco:** la familia tiene el PRIMER paso del metodo IOPS (`investigar_datos_cliente`), el TERCERO (`personalizar_interacciones_cliente`) y el CUARTO (`sorprender_cliente_estrategico`) escritos como nodo, **y los tres lo declaran en su propio resumen. Falta el SEGUNDO, observar** |
| `silla_vacia_del_cliente_en_decisiones` | `cultura_de_experiencia` 12 **y** `customer_journey_mapping` 9 | un artefacto de gobierno permanente en la reunion interna. **Los DOS donantes al MISMO nodo**, por la adjudicacion 3 del acta 27: partirlos habria fabricado el gemelo |
| `incentivos_internos_alineados_a_retencion` | `diseno_estructura_recompensas_roles` 4 a 7 | la auditoria y el rediseno del esquema de compensacion. `desconexion_ventas_experiencia` usa esa desalineacion como CAUSA de un traspaso roto, no como objeto |
| `autoservicio_y_autosanacion_del_producto` | `sistema_inmune_producto` 6 a 9 | que el PRODUCTO resuelva sin humanos. `comunicacion_proactiva_puntos_estres` avisa en el estres emocional y `rediseno_procesos_negocio_cliente` arregla PROCESOS |
| `personalizacion_guiada_por_el_cliente` | `cliente_disena_producto` 5 a 8 | quien decide es EL CLIENTE. `micro_experiencias_personalizadas` captura preferencias que recoge el equipo, y `personalizar_interacciones_cliente` son mensajes que escribe la empresa |

**GUARDAS, con su cifra y su fichero:**

| guarda | resultado |
|---|---|
| simulacion previa sobre copia en memoria | **verde**, 24 cortes, 34 ficheros (`SALIDA_V31_COL_SIM.txt`) |
| guarda de texto por prefijo | **24 de 24** |
| cobertura por origen contra las trece fronteras publicadas | **exacta, sin huecos ni repetidos**, las trece |
| **caso positivo ANTES** | **24 PASAN, 48 CAEN** (`SALIDA_V31_COL_CASO_ANTES.txt`) |
| **caso positivo DESPUES** | **72 PASAN, 0 CAEN** (`SALIDA_V31_COL_CASO_DESPUES.txt`) |
| viaje verbatim de los pasos movidos | **67 de 67** |
| cero perdida contra HEAD, nodo por nodo | **13 de 13**, y el texto de los que se quedan **INTACTO** |
| auto aristas fabricadas | **0** |
| duplicadas tras resolver fabricadas | **0** (9 en HEAD, 9 ahora) |
| los cinco nodos propios | **doce campos, vivos, arista de ida y de vuelta**: 5 de 5 |

**Ciclo de `Gate 0`, entero y en su orden:** comando 1 `run_phase1.py --reaplico-curaduria`
**exit 0, `GATE 0: OK`**; comando 2 `etiquetas_de_cara.py --aplicar` **71 etiquetas**; **comando
4 `plan_readiness.py` SI aplica** (el censo se movio) y regenera `node_families.json` con
**3.853 nodos**; comando 3 `sync_assets_web.py`. **La vara del comando 3, medida DESPUES de
commitear como manda el registro de la vuelta 27: las dos copias en el blob `af8a4bc2`, byte
identicas al `HEAD` que trae el commit** (`git hash-object` contra `git rev-parse HEAD:<ruta>`,
las dos rutas). **Suites:** motor **24 de 24**, web **80 ficheros, 1.030 pasadas y 3 saltadas**,
`tsc --noEmit` **cero lineas**.

### 3.1 LAS DIECISIETE COSTURAS, y yo esperaba DOS

**Medidas con instrumento nuevo** (`scripts/loop/vuelta31_costuras_col.py`) contra el commit
`cc47af3d`, **y con un cambio de diseno que se declara: la nomina de receptores NO se escribe a
mano, se lee del plan sellado**, precisamente para no repetir la omision que el acta 28
adjudico. **21 destinos, 17 con costura, 4 sin ella**, y los cuatro sin costura dichos por su
nombre para que la cuenta cierre. Todas registradas en `08_VERIFICACION.md` con su medicion.

> **YO ESPERABA DOS** (la de `silla_vacia` y la de `rediseno_procesos_negocio_cx`) **y la
> medicion levanto DIECISIETE. La leccion se escribe donde se va a leer:** cuando el receptor y
> el donante salen **del mismo libro**, el solape deja de ser la excepcion y pasa a ser lo
> normal. Tres de ellas (`reunion_conclusion_proyecto`, `fase_admit_celebracion`,
> `incentivos_no_monetarios_advocacy`) **no son un matiz: son el mismo paso escrito dos veces**.
> **No se destejen aqui: el verbo de esta operacion es repartir**, y la lectura que las decide
> es de la fase 02.

### 3.2 EL SALDO Y EL CIERRE DE LA FASE 01

**`scripts/loop/vuelta31_saldo_col.py`, sucesor declarado con su motivo dentro**, porque el de
la vuelta 30 contaba DOS especies y `COL` tiene TRES: la tercera la ordeno la adjudicacion 2 del
acta 30 con estas palabras, *el saldo de COL lo cuenta como especie propia (EMBEBIDO LEGITIMO),
igual que WEI cuenta sus fundidos*.

| tanda | nomina | resueltos | fundidos `P.19` | embebidos legitimos | **pendientes** |
|---|---:|---:|---:|---:|---:|
| **`OP-F-04-COL`** | 15 | **13** | **1** | **1** | **0** |

**LA TABLA DEL CIERRE DE LA FASE 01, RECOMPUTADA AL CERRAR** (cada fila con el instrumento que
la midio hoy, publicada tambien en `01_FUENTES.md`):

| operacion | estado al cierre, medido hoy |
|---|---|
| `OP-F-01` | **VERDE**, no toca ningun paso por diseno |
| `OP-F-02`, `OP-F-03` | **HECHAS** (acta 29 adjudicacion 4; nota escrita en la vuelta 30) |
| `OP-F-04-RAC` | **HECHA**, 4 de 4, 0 pendientes |
| `OP-F-04-WEI` | **HECHA**, 13 de 13 (11 mas 2), 0 pendientes |
| `OP-F-04-HOR` | **HECHA**, 13 de 13 (12 mas 1), 0 pendientes |
| `OP-F-04-COL` | **HECHA**, 15 de 15 (13 mas 1 mas 1), 0 pendientes |

> **LA FASE 01 QUEDA CERRADA**, y se dice sin estirarlo: *fuente primero* esta cumplido **para
> las nominas escritas**, o sea que ningun nodo de estas tandas entra a su destejido arrastrando
> el libro que su operacion nombraba. **NO significa que estos nodos queden perfectos:** las 17
> costuras de `COL`, las 5 de `WEI` y las 4 entradas de LA COLA DEL OBJETO AJENO son trabajo de
> la fase 02, con su comprobacion fechada al cierre de esa fase. **Y hay un nodo que se sale de
> esa frase, que es la parada de la seccion 4.**

---

## 4. PARADA: `OP-D-01` NO SE PUEDE EJECUTAR TAL COMO ESTA ESCRITA

**El modo continuo entro a la FASE 02 por su orden (`OP-D-01`, orden 1) y se detuvo ahi. NO se
toco un solo nodo en esta parada: solo medicion.** Los tres motivos, medidos hoy con instrumento
propio, salida en `docs/loop/SALIDA_V31_PARADA_OPD01.txt` y `SALIDA_V31_SALDO_OPF03.txt`.

**MOTIVO 1, y es el que contradice una regla vigente.** `principio_calidad_mvp`, uno de los dos
nodos de `OP-D-01`, **sigue declarando DOS libros**: `The Lean Startup - Eric Ries | The Hard
Thing About Hard Things`, y **su bloque de Horowitz (los pasos 6 a 10) no esta en la nomina de
NINGUNA operacion de fuente.** Barrido corrido hoy sobre el grafo entero: **de los DOS nodos
vivos que declaran *Hard Thing* en segunda posicion o posterior, uno es
`decision_de_vender_startup` (dentro de `OP-F-04-HOR`) y el otro es este, el UNICO fuera.** Y
**la propia nota de `OP-D-01` manda *fuente primero***. Destejerlo hoy seria destejer un nodo
con un segundo libro sin resolver, que es exactamente lo que esa regla existe para impedir.

> **`OP-F-03` NO ESTA MAL HECHA, y se dice para que nadie lea esto como una caida suya.** Su
> nomina son *veintiun nodos que declaran Hugos JUNTO A OTRA FUENTE* y su objeto es el material
> de Hugos. Medido hoy con `git show` contra `0b151de2~1`: antes de `OP-F-03` el nodo tenia **14
> pasos y TRES libros** (Ries, Horowitz, Hugos), y `OP-F-03` **se llevo el bloque de Hugos (los
> pasos 11 a 14) y su declaracion**. Hizo lo suyo entero. **El hueco es del PLAN: el bloque de
> Horowitz de este nodo no lo reclama ninguna operacion.**

**MOTIVO 2, y es el que no alcanza para ejecutarse sin decidir.** El campo `preservar` de
`OP-D-01` pide *decidir si `principio_calidad_mvp` conserva la narracion de LA CALIDAD (pasos 1
a 5) o la del CONJUNTO MINIMO (pasos 11 a 14)*, **y esos pasos 11 a 14 ya no existen: eran el
bloque de Hugos y `OP-F-03` se los llevo.** El nodo tiene **10 pasos** hoy. **La decision que la
operacion pide no se puede tomar sobre el nodo de hoy**, y de esa decision depende la clase del
par **494**, que es el eje de la operacion entera.

**MOTIVO 3, una discrepancia de nombre en el registro.** La nota de `OP-D-01` dice
*`principio_calidad_mvp` declara **Hugos** como segunda fuente*. **El grafo de hoy dice
Horowitz**, y Hugos ya no esta. La nota era correcta cuando se escribio; se declara en vez de
copiarse.

**HALLAZGO ADICIONAL, medido y no pedido, para que el auditor lo tenga:** **el paso 1 de
`OP-D-02` YA ESTA HECHO, y lo hizo `OP-F-04-COL` en esta misma vuelta.** Su texto manda
*destejer `voz_del_cliente_voc` separando Cooper (1 a 5) de Coleman (6 a 10)* y su tabla de
preservacion nombra *el bloque 6 a 10 entero: observar una vez al mes, ponerse en el lugar del
cliente, las pepitas de oro, anotar y revisar a los dos dias, y buscar patrones*. **Medido hoy:
el nodo tiene 5 pasos y fuente unica Cooper, y ese bloque vive en
`observar_al_cliente_en_su_contexto`.** Lo que le queda a `OP-D-02` **es fusion, no destejido**,
y su estado pide readjudicacion. **No lo toque.**

> **PARA_ALEXIS.md NO SE ESCRIBE**, y no es timidez: esa pluma es del auditor (`AUDITOR.md`
> seccion 4) y la regla 4 del `EJECUTOR.md` manda escribir la parada en el reporte y no
> arreglarla, que es lo mismo que el acta 27 adjudico CORRECTO en su punto 6.

---

## 5. CORRECCIONES DECLARADAS DE ESTA VUELTA

1. **UNA GUARDA CORREGIDA DESPUES DE VERLA CAER, y el motivo esta dentro del codigo.** La
   guarda 3 de `vuelta31_guardas_col.py` media el TOTAL de duplicadas tras resolver en los nodos
   tocados y dio **9 en rojo**. **Antes de tocar una linea medi la MISMA cuenta sobre HEAD**
   (`docs/loop/_v31_duplicadas_antes.py`, salida en `SALIDA_V31_DUPLICADAS_ANTES.txt`): **las
   nueve ya estaban ahi, en los mismos nodos y los mismos campos**, y las nueve son pares de
   alias que resuelven al mismo destino. **Esa poblacion esta contada y adjudicada por escrito**
   (`00_INDICE.md`: 1.056 entradas en 802 nodos, van a `OP-S-12`, que por su atadura 2 **va al
   final**). Lo que el encargo pide de esta operacion es **no fabricar** duplicadas, que es una
   diferencia contra HEAD, y eso es lo que la guarda mide ahora. **El total se sigue imprimiendo
   con su nombre para que nadie lo confunda con un cero que no existe.**
2. **UNA HUELLA CAMBIADA Y DECLARADA.** La del corte de `estrategia_crecimiento_clientes` iba a
   ser *bajo costo marginal*, y **la guarda del sellador la paro porque esa huella YA VIVE en el
   nodo destino** (`incentivos_no_monetarios_advocacy`). **Una prueba que el destino ya pasa
   antes del corte no prueba nada**, que es la leccion de la huella insatisfacible de la vuelta
   30. Se cambio a la mecanica del paso 8 y el motivo quedo escrito dentro del plan.
3. **DIEZ HUELLAS ESCRITAS SIN ACENTOS contra un texto de pasos que SI los lleva.** Las escribi
   mal en el sellador; **el parche va en el repo como registro** (`docs/loop/_patch_huellas_v31.py`)
   en vez de corregirse en silencio.
4. **UN BARRIDO MIO MAL FILTRADO, cazado por mi mismo y re-corrido.** El primer barrido de la
   parada preguntaba si el nodo estaba *en la nomina de alguna operacion de fuente* y dio **cero
   casos**, escondiendo el unico que hay: `principio_calidad_mvp` **si** esta en una nomina
   (`OP-F-03`), pero por su bloque de **Hugos**, no por el de Horowitz. **Corregi el filtro y
   re-corri; la salida publicada es la del barrido corregido y lleva esa frase escrita dentro.**
   Si publico la primera, publico un cero falso.
5. **UN FICHERO QUE TOCO EL VALIDADOR Y NO MI CORTE, declarado para que el diff cuadre:**
   `dataset/nodos/personalizar_interacciones_cliente.json` cambio porque `Gate 0` **simetrizo la
   arista** que `observar_al_cliente_en_su_contexto` declara hacia el. **35 ficheros de
   `dataset/nodos` en el diff, 34 de mi corte y ese.**

---

## 6. PENDIENTES DE DOCTRINA

1. **El bloque de Horowitz de `principio_calidad_mvp` no tiene operacion de fuente**, y ninguna
   pagina dice quien lo reclama. Es la parada de la seccion 4. **No es doctrina nueva
   necesariamente**: puede ser una ampliacion de nomina de `OP-F-04-HOR`, o una operacion nueva,
   y esa pluma no es mia.
2. **Los siete nodos propios nacidos en esta pasada estan escritos SIN ACENTOS** mientras el
   resto del catalogo los lleva. Sigo el precedente de la vuelta 29 (`estar_listo_para_ser_publica`,
   verificado hoy: su titulo es *Estar Listo para Ser una Empresa Publica*) **para no fabricar
   dos estilos dentro de la misma pasada**, pero **es una deuda cosmetica real** y ninguna pagina
   del plan dice cual es la forma correcta.
3. **El campo `estado` sigue sin el valor `HECHA`** (adjudicado NO en el acta 30 punto 7). Se
   repite aqui porque ya son **siete** operaciones declaradas hechas viviendo solo en `nota`.

---

## 7. LOS DISCUTIBLES, MARCADOS ANTES DE SABER SI ACIERTO

| # | que | por que es discutible |
|---:|---|---|
| **d1** | **Partir `blueprint_de_experiencia` en SEIS subbloques** | el encargo autoriza partir por objeto, **pero no dice cuantos**. Seis es mi lectura: postventa, friccion, ritual, calibracion, traspaso, cien dias. La lectura contraria seria tres (los tres actos que la tabla nombra) y dejar 8, 12 y 15 dentro del que mas se les parezca |
| **d2** | **El paso 17 (responsable por punto de contacto) con los cien dias** y no con `estrategia_multicanal_bienvenida`, cuyo entregable dice *responsables asignados* | lo leo como parte del plan de los cien dias, no como un reparto por canal. Es el destino mas fino de los veinticuatro |
| **d3** | **`cliente_disena_producto` 5 a 8 a nodo propio** | sus pasos 7 y 8 (el simbolo tangible de la decision) **son casi el mismo objeto** que el paso 11 de `blueprint`, que si mande a `fase_admit_celebracion`. Los deje juntos con 5 y 6 porque ahi *la decision* es la personalizacion y no la compra. La lectura contraria parte el bloque en dos |
| **d4** | **Un nodo propio de DOS pasos que dicen lo mismo** (`silla_vacia_del_cliente_en_decisiones`) | nace con la costura dentro y con nada mas. Lo sostengo con la adjudicacion 3 del acta 27 (partirlos habria fabricado el gemelo) mas el registro de la primera puerta, **pero un nodo cuyo contenido entero es una repeticion es un resultado incomodo** |
| **d5** | **`diseno_estructura_recompensas_roles` 4 a 7 a nodo propio** en vez de a `desconexion_ventas_experiencia` | ese miembro trae *metas de retencion ligadas a la venta* en su entregable, que roza los pasos 4, 6 y 7. Lo descarte porque su objeto es el TRASPASO y los incentivos son su causa |
| **d6** | **`sistema_inmune_producto` 6 a 9 a nodo propio** | los pasos 6 y 7 caben en `comunicacion_proactiva_puntos_estres`. Los deje con 8 y 9 porque los cuatro son un arco: friccion, aviso automatico, autoservicio, cifra sin humanos |
| **d7** | **`retention_metrics` 6 a 9 entero a `persuasion_directivos_prioridad_cliente`** | los pasos 6, 7 y 8 son cuenta pura (CAC, breakeven, abandono) y solo el 9 nombra al directivo. La lectura contraria los deja en el donante como metricas |
| **d8** | **`metas_vs_proposito` a `fase_accomplish_experiencia_cliente`** y no al generico `fase_accomplish` | los dos tienen el objeto. Desempate por entregable: el generico pide *un indicador o checkpoint* y el bloque pide sistema y protocolo |
| **d9** | **`project_close_out` 6 a 11 entero a `reunion_conclusion_proyecto`**, incluido el paso 10 de testimonios | `gestion_testimonios` era candidato real para ese paso. **Y es la costura mas alta de la tanda**: tres de seis solapan |
| **d10** | **Corregir la guarda de duplicadas despues de verla caer** | lo sostengo con la medicion contra HEAD y con la pagina de `OP-S-12`, **pero cambiar una guarda que acaba de caer es el movimiento que mas hay que mirar**, y por eso va marcado |
| **d11** | **Declarar PARADA en `OP-D-01` en vez de saltar a `OP-D-02`** | el precedente del acta 27 punto 5 permite seguir con lo independiente. **No lo hice**: lo que queda de `OP-D-02` es fusion (par 724, 755, 827), y una fusion no es lo que la fase 02 me autoriza a improvisar. La lectura contraria es que `OP-D-05` y `OP-D-08` si eran independientes y ejecutables |
| **d12** | **Contar 21 destinos y 13 destinos como dos cifras distintas** | *trece* son los nodos de la nomina cuyo bloque hay que colocar, *veintiuno* los nodos que reciben. **Podria leerse como inflar la cuenta**; lo sostengo al reves: dar solo trece escondería que el reparto toco veintiun nodos |
| **d13** | **Los cinco nodos propios escritos sin acentos** | ver el pendiente de doctrina 2 |

---

## 8. PREGUNTAS

1. **`principio_calidad_mvp`: quien reclama su bloque de Horowitz?** Medido: es el unico nodo
   vivo del grafo con *Hard Thing* en segunda posicion fuera de `OP-F-04-HOR`. **Se amplia la
   nomina de `OP-F-04-HOR` a catorce, se escribe una operacion nueva, o se adjudica que ese
   bloque no es un injerto?** De la respuesta depende `OP-D-01`, que es la primera de la fase 02.
2. **`OP-D-02` queda con la mitad de su texto ya ejecutado por `OP-F-04-COL`.** Su paso 1 esta
   hecho y lo que le queda es la fusion con `enfoque_mercado_voc`. **Se readjudica su alcance
   antes de tocarla, o se ejecuta lo que queda como si nada?**
3. **Las diecisiete costuras entran todas a la fase 02 con el mismo rango?** Tres de ellas son el
   mismo paso escrito dos veces y otras son matices parciales. **La cola no distingue grados**, y
   con diecisiete de golpe esa falta de grado empieza a pesar.

---

## 9. LA RACHA DE DICTADO, dicha por mi

**El acta 30 corto la racha en cero.** Esta vuelta midio la apertura con instrumento **antes de
la primera operacion** y la commiteo antes de tocar nada (`0ee5c1e8`); midio el cierre **al
cerrar** con el sucesor declarado; y **toda cita del registro lleva su linea leida hoy** (6605,
6608, 6610, 6639, 6648, 5688, 5709, 6390). **Las cinco correcciones de la seccion 5 son mias y
estan declaradas con nombre**, y dos de ellas (el barrido mal filtrado y la huella insatisfacible)
las cazaron guardas que escribi para que cayeran. **No me corresponde decir si la racha sigue
cortada: eso lo mide el auditor.**
