# REPORTE DE LA VUELTA 182 (ejecutor). FASE III, EJECUCION. Rama `pasada-unica`.

> **ESTE REPORTE SE ABRIO AL EMPEZAR LA VUELTA Y CRECE POR ANEXION** (`EJECUTOR.md`
> 1, "EL REPORTE ABRE CON LA VUELTA"). El esqueleto lo tallo
> `scripts/loop/vuelta182_esqueleto_reporte.py`; cada tarea ANEXA SU FILA AL
> CERRARSE, no al final; y el cierre lo talla entero `scripts/loop/cerrar_reporte.py`.
> **Si esta vuelta se corta, lo que quede aqui es lo que de verdad se hizo, y las
> filas que sigan diciendo ABIERTA, SIN CERRAR son las que no se hicieron.**
>
> **ESTA VUELTA NO ES DE BATERIA, Y ESO TAMBIEN ES LETRA.** `AUDITOR.md` 6.1: la
> bateria corre CADA CINCO, en VUELTA PROPIA. **La 181 era la suya y se corto
> antes de lanzarla**, y su acta lo registra en el punto 7.5 sin contarlo como
> caida de reporte, porque el esqueleto por anexion dejo la fila diciendo ABIERTA,
> SIN CERRAR y no publico ninguna cifra de una corrida que no hubo. La decision
> del fundador del **5 sep 2026** (PREGUNTA 4 de
> `docs/loop/paradas/2026-09-05-cola-post-fusion-DECISION.md`) manda que corra
> **POR TRAMOS RESUMIBLES**, y la **TAREA 5** de este encargo la deja preparada y
> declarada para la **183**. **La seccion 9 de este reporte cierra con su HUECO
> DECLARADO Y MEDIDO**, que es lo que el regimen 6.1 manda para las vueltas
> intermedias: un hueco declarado no es un hueco escondido.
>
> **EL TOPE DE ESTA VUELTA ES CINCO SUB-TAREAS, Y TAMPOCO ES UNA GANA.** La
> adjudicacion **6.8 del acta 180** bajo el tope a DOS en la 181 porque era vuelta
> de bateria, y en la misma frase escribio: *"El tope vuelve a cinco en la 182"*.
> El encargo de esta vuelta trae **CINCO** y dice *"que es el tope. Ni una mas"*.
>
> **LO QUE NO ENTRA EN ESTA VUELTA, DICHO PARA QUE NO SE CUELE:** no se relee
> ninguno de los 543 pares que la TAREA 4 mete en la cola (eso es justo lo que la
> decision del fundador evita al conceder la `b` y no la `c`), no se toca el
> marcador, no se cambia ningun veredicto del archivo, y **las `A` no ganan cola
> nueva** por la PREGUNTA 2 de la misma decision. **Y no se corre la bateria**: se
> prepara.
>
> **Y ESTA VUELTA MIDE SU DESFASE DE CALIBRADO EN LA APERTURA, DENTRO DEL BLOQUE
> DE APERTURA Y ANTES DE LA PRIMERA OPERACION.** El remedio se cableo en
> `vuelta177_apertura.py`, la 178 lo estreno, la 179 y la 180 lo repitieron y aqui
> vuelve a correr en su sitio. **Desde la 178, una columna de apertura medida al
> cierre es caida que ACUMULA.**
>
> **Y EL PASO 0 DE ESTE ESQUELETO PREGUNTA POR EL REPORTE QUE VA A PISAR, NO POR
> LA VUELTA ANTERIOR.** Esta vez las dos preguntas vuelven a coincidir, porque la
> 181 escribio su reporte, lo cerro y lo archivo EN SU MISMA VUELTA; el
> fichero corre LAS DOS igualmente y publica lo que salga de cada una, porque una
> guarda que solo se mira cuando difiere no se puede auditar el dia que difiera.

**EL VEREDICTO DE UNA LINEA: LAS CINCO TAREAS CERRARON, EL 2.464 ENTRA A LA COLA COMO UNICA D CON LESION EXACTA CONFIRMADA, Y LAS SEIS CAIDAS QUE COMETI VAN CON SU NOMBRE Y SU SALIDA VIEJA GUARDADA.**
## 0. LA IDENTIDAD Y LA CABECERA, TALLADAS Y NO TECLEADAS

**LA IDENTIDAD, LEIDA DE GIT EN ESTA VUELTA** por
`scripts/loop/vuelta182_esqueleto_reporte.py`, con
`git rev-parse --abbrev-ref HEAD`, `git log` y `git log --diff-filter=A`, y CAE
EN ROJO si algo no se encuentra o es ambiguo:

- rama: `pasada-unica`
- commit del acta de la vuelta 181: `b931019f`, asunto real leido de git log:
  'ACTA DEL AUDITOR, VUELTA 181, Y PARADA: UNA FUSION LE MOVIO LA EVIDENCIA A UN VEREDICTO CERRADO Y LA COLA QUE DEBIA RELEERLO EXCLUYE SU CLASE.'
- HEAD real de apertura, sellado ANTES de la primera operacion en
  `docs/loop/SALIDA_V182_HEAD_APERTURA.txt`: `326d7dc9`
- commit de nacimiento del bloque de apertura, leido con
  `git log --diff-filter=A`: `c85f0c4d`
- reporte que este esqueleto pisa, leido de la cabecera de ese mismo fichero:
  la vuelta **181**, ya archivada byte a byte antes de escribir aqui
- commit de cierre: se talla al cierre. **Un reporte no puede nombrar el commit
  que lo lleva**, porque ese commit se crea despues de escribirlo.

<!-- CABECERA TALLADA -->
**LA TABLA, PEGADA ENTERA DEL FICHERO QUE LA LLEVA Y NO TECLEADA.** Salio
de `scripts/loop/tallar_cabecera_reporte.py --fase04 --vuelta 182`, y su salida
cruda vive en `docs/loop/SALIDA_V182_TALLADOR_CABECERA.txt` (2397 bytes en disco y 2377 normalizado a LF, 11 filas de
tabla,
contadas por `scripts/loop/cerrar_reporte.py`). **LA CELDA QUE NO SALGA DE UN
INSTRUMENTO NO SE ESCRIBE.**

| | **apertura**, antes de la 1.ª operacion | **cierre, RECOMPUTADO al cierre** |
|---|---:|---:|
| censo: nodos / vivos / deprecados | 3.853 / 3.169 / 684 | **3.853 / 3.169 / 684** |
| Gate 0: veredicto, auto-aristas, duplicadas de titulo, divergentes | OK (auto-aristas 0, duplicadas 0, divergentes 0) | **OK (auto-aristas 0, duplicadas 0, divergentes 0)** |
| aristas: `nodos_siguientes` / `nodos_previos` / suma / union | 8.780 / 8.740 / 17.520 / 9.914 | **8.780 / 8.740 / 17.520 / 9.914** |
| motor | 25/25 | **25/25** |
| web: ficheros / tests | 82 passed (82) / 1.040 passed (1.040) | **82 passed (82) / 1.040 passed (1.040)** |
| tsc | EXITCODE 0, cero lineas | **EXITCODE 0, cero lineas** |
| aristas movidas en la vuelta (cierre menos apertura): `nodos_siguientes` / `nodos_previos` / suma / union | (no aplica: la celda de cierre es la resta contra esta apertura) | **+0 / +0 / +0 / +0** |
| desfase del calibrado rastreado (`PASO_NODO_CALIBRADO.jsonl` distinto del grafo) | 4 fila(s): `dia_cero_defectos_2 -> eliminacion_causas_error_4`, `customer_validation -> establecer_linea_base_mvp`, `dia_cero_defectos_3 -> eliminacion_causas_error_4`, `ganar_comprension_del_cliente -> dia_en_la_vida_del_cliente` | **4 fila(s): `dia_cero_defectos_2 -> eliminacion_causas_error_4`, `customer_validation -> establecer_linea_base_mvp`, `dia_cero_defectos_3 -> eliminacion_causas_error_4`, `ganar_comprension_del_cliente -> dia_en_la_vida_del_cliente`** |
| identidad: rama y commit de apertura (leidos de git, no tecleados) | rama `pasada-unica`, commit del acta `b931019f` (asunto real leido de git log: 'ACTA DEL AUDITOR, VUELTA 181, Y PARADA: UNA FUSION LE MOVIO LA EVIDENCIA A UN VEREDICTO CERRADO Y LA COLA QUE DEBIA RELEERLO EXCLUYE SU CLASE.'), HEAD real de apertura `326d7dc9` (sellado antes de la 1.a operacion, leido de git log --diff-filter=A), arboles de `dataset/` IGUALES: VERDE | **rama `pasada-unica`, HEAD de cierre `9357417d` (leido de `SALIDA_V182_HEAD_CIERRE.txt`, sellado tras la ultima operacion)** |

<!-- FIN CABECERA TALLADA -->

## 1. LAS CINCO TAREAS DEL ENCARGO, Y SU ESTADO

<!-- TABLA DE TAREAS -->
| tarea | que encarga | estado | donde vive la prueba |
|---|---|---|---|
| **TAREA 1** | LOS REGISTROS Y LA DEUDA DE LECTURA. (a) El acta 181 y sus adjudicaciones entran en la serie de registros, con el numero que devuelve `scripts/loop/serie_de_registros.py` y no tecleado. (b) LOS DOS PENDIENTES DEL ACTA 180, que llevan una vuelta esperando y estan escritos en sus puntos `6.8` y `6.6`: el remedio del `E.1` sobre `scripts/loop/cerrar_reporte.py`, que es la rama que escribe la cabecera CORRIDA ENTERA Y SOLA sobre una seccion 9 cuyo cuerpo dice que nadie la corrio, y la `P.1`, el arnes `vuelta172_tarea1c_guarda_que_mordio.py`, que cae con exit 1 fallando 1 de 6 y esta fuera del censo: primero el esperado y despues el nombre, en ese orden, que es parte de la adjudicacion. (c) LA RELECTURA AL DOBLE del tramo de la ciega que el acta 181 encarga en su `7.2` por `AUDITOR.md` 1.2, sobre los 30 puestos que su seccion 8 lista | **CERRADA** | `SALIDA_V182_T1A_REGISTRO_ACTA_181.txt`, `_T1A_REGISTRO_R43.txt`, `_T1A_MUTACION_REGISTRO.txt`, `_T1B_REMEDIO_E1.txt`, `_T1B_ARNES_RAMA_SECCION9.txt`, `_T1B_REMEDIO_P1.txt`, `_T1B_REMEDIO_P1_MITAD_C.txt`, `_T1B_DECLARAR_CONGELADO_P1.txt`, `_T1C_RELECTURA_AL_DOBLE.txt` |
| **TAREA 2** | LA APERTURA DEL AUDITOR COMO CODIGO (decision del fundador del 5 sep 2026, PREGUNTA 3, opcion c, la mitad que quita el problema de raiz; la otra mitad, que ROMPER UN REMEDIO ESCRITO ACUMULE, ya esta escrita en `AUDITOR.md`). Fichero GEMELO del bloque de apertura del ejecutor: corre `scripts/loop/aislador_de_ciega.py` y SELLA SU SALIDA ANTES de que el turno pueda tocar `git log`, `git status` o `docs/loop/REPORTE.md`. Con CASO POR MUTACION SOBRE VARIABLE COMPUTADA, no sobre constante literal (`EJECUTOR.md` 1, EL CASO ROJO SE PRUEBA POR MUTACION): si el sello se intenta DESPUES de tocar cualquiera de los tres, TIENE QUE CAER, y la prueba se corre cambiando el valor esperado para comprobar que el caso cae de verdad | **CERRADA** | `scripts/loop/apertura_del_auditor.py`, `SALIDA_V182_T2_MUTACION_APERTURA_AUDITOR.txt`, y el parrafo nuevo de `docs/loop/AUDITOR.md` |
| **TAREA 3** | EL INSTRUMENTO DEL DIFERENCIADOR MOVIDO (decision del fundador del 5 sep 2026, PREGUNTA 1, la `b`). Cruza LA RAZON ESCRITA de cada `D` contra LOS PASOS DE HOY del otro nodo, y SOLO las `D` con la lesion exacta vuelven a la cola. CASO POSITIVO OBLIGATORIO: EL PUESTO 2.464 TIENE QUE SALIR NOMBRADO; si no sale, el instrumento no sirve y se dice. Y EL CENSO POR ESTADO DE LAS `A` en el mismo instrumento: ejecutadas contra pendientes, con LAS PENDIENTES DE TEXTO MOVIDO MARCADAS RANCIAS POR `P.5`. Las `A` NO ganan cola nueva: la ejecutada es cosa consumada y la pendiente ya la cubre `P.5` | **CERRADA** | `SALIDA_V182_T3_DIFERENCIADOR.txt`, `SALIDA_V182_T3_COLA.json`, `SALIDA_V182_T3_MUTACION.txt`, `SALIDA_V182_T3_DIFERENCIADOR_FECHADO_MALO.txt` |
| **TAREA 4** | LAS `D` QUE EL INSTRUMENTO NOMBRE ENTRAN A LA COLA de relectura post fusion de `docs/plan/08_VERIFICACION.md`, y se releen POR TRAMOS en las vueltas siguientes. En esta vuelta SE ENTRA A LA COLA Y SE DECLARA EL TRAMO; no se releen 543 pares, que es justo lo que la decision del fundador evita al conceder la `b` y no la `c` | **CERRADA** | `SALIDA_V182_T4_COLA.txt`, y la seccion nueva en `docs/plan/08_VERIFICACION.md` |
| **TAREA 5** | LA VUELTA DE BATERIA VA EN LA 183, POR TRAMOS RESUMIBLES (decision del fundador del 5 sep 2026, PREGUNTA 4, opcion `a`, con el precedente de los nueve tramos de la vuelta 176). Aqui SOLO se deja preparada y declarada: nueve tramos, cada uno se commitea CON SU SALIDA SELLADA al terminar, una vuelta cortada RETOMA EN EL TRAMO SIGUIENTE, y la bateria se declara corrida cuando LOS NUEVE tienen salida sellada DEL MISMO CALIBRE. En esta vuelta la seccion 9 del reporte cierra con su HUECO DECLARADO Y MEDIDO, como el regimen `6.1` manda | **CERRADA. PREPARADA Y DECLARADA, NO CORRIDA** | `scripts/loop/vuelta183_bateria_por_tramos.py`, `SALIDA_V182_T5_PLAN_BATERIA_183.txt`, `SALIDA_V182_T5_SIGUIENTE_TRAMO.txt`, `SALIDA_V182_T5_COTEJO_CLON_BATERIA.txt` |
<!-- FIN TABLA DE TAREAS -->

## 2. LAS TAREAS, UNA POR UNA (cada seccion se ANEXA al cerrarse su tarea)

<!-- ANEXO DE TAREAS -->

### TAREA 1. LOS REGISTROS Y LA DEUDA DE LECTURA

**1.a. EL ACTA 181, CITADA CON SU LINEA.** Instrumento
`scripts/loop/vuelta182_tarea1_registros.py`, salida
`docs/loop/SALIDA_V182_T1A_REGISTRO_ACTA_181.txt` (**8.504 bytes en disco y 8.504 normalizados a LF**). Cabecera del
acta 181 en la **62907** y la del acta 180 en la **62449**, las dos localizadas y
no tecleadas. **42 agujas buscadas, 42 halladas, 0 no halladas**, contadas de ese
fichero.

**R.43 ESCRITO**, con el numero que devuelve `serie_de_registros.siguiente_libre()`
y no tecleado. Instrumento `scripts/loop/vuelta182_tarea1a_registrar_acta181.py`,
salida `docs/loop/SALIDA_V182_T1A_REGISTRO_R43.txt` (**2.910 bytes en disco y 2.910 normalizados a LF**). Titulo con
sus tres numerales contados del acta acotada (lineas 62907 a 63249): **5
adjudicaciones `7.n`**, **1 caida propia del auditor** (`C.1`, linea 62932) y **1
del ejecutor** (`E.2`, linea 63078). `docs/PENDIENTES.md` pasa de **843.961** a
**850.711 bytes en disco y 850.711 normalizados a LF**. Caso por mutacion **VERDE**
(`docs/loop/SALIDA_V182_T1A_MUTACION_REGISTRO.txt`, **1.531 bytes en disco y 1.531 normalizados a LF**): 4 actas
fabricadas, el esperado mutado **CAE**, y el prefijo viejo `6.` sobre un acta que
numera `7.n` da **CERO**.

> **CAIDA MIA, Y VA DELANTE.** En el docstring del bloque de apertura, en el del
> esqueleto y en dos mensajes de commit escribi que la adjudicacion `6.8` del acta
> 180 dice, con esas palabras, *"El tope vuelve a cinco en la 182"*. **NO ESTA EN
> EL ACTA:** esa frase literal es del **reporte de la 181**
> (`docs/loop/reportes/REPORTE_V181.md:21`), o sea prosa mia. Lo que el acta 180
> escribe esta en su punto 10, **linea 62893**: *"EL TOPE: DOS SUB-TAREAS EN LA
> 181, POR MI ADJUDICACION 6.8, y vuelve a cinco en la 182"*. **La sustancia
> coincide; la atribucion y el literal no.** El texto viejo no se borra: vive en
> los commits `c85f0c4d` y `afa8ecc5`.

> **DEUDA MEDIDA Y NO CALLADA.** La ultima entrada de la serie antes de esta
> registraba el acta de la vuelta **172** (`R.42`). **Las actas 173 a 180 no
> tienen entrada propia.** Se cuenta en la seccion G de la salida y **no se
> inventan ocho registros que nadie encargo**.

**1.b. LOS DOS PENDIENTES DEL ACTA 180.**

**EL `E.1`**, sobre `scripts/loop/cerrar_reporte.py` (**38.947 a 43.563 bytes en disco y 43.563 normalizados a LF**).
Tres causas medidas y **cuatro piezas** de remedio: el patron no casaba con
`SALIDA_V180_HUECO_BATERIA` y daba `None`; con `None` la guarda de vuelta ajena se
saltaba en silencio; la rama se elegia solo por si el fichero traia lineas; y **una
corrida no es cualquier fichero con lineas, tiene que llamarse como una corrida**.
La decision sale de `main()` y pasa a ser `rama_de_la_seccion9()`, pura y con arnes
propio: **9 casos, 9 calzan, 4 en que la logica vieja y la viva difieren**, y las
dos mutaciones **CAEN**
(`docs/loop/SALIDA_V182_T1B_ARNES_RAMA_SECCION9.txt`, **5.802 bytes en disco y 5.802 normalizados a LF**).

> **EL ARNES CAZO QUE MI PRIMER REMEDIO ERA INCOMPLETO.** Con solo tres piezas
> salia VERDE en sus nueve casos **y su propia seccion C publicaba que el caso real
> de la 180 seguia saliendo `CORRIDA`**. Esa salida queda entera en
> `docs/loop/SALIDA_V182_T1B_ARNES_REMEDIO_INCOMPLETO.txt` (**5.293 bytes en disco y 5.293 normalizados a LF**) y el
> parche a medias en `SALIDA_V182_T1B_REMEDIO_E1_PRIMERA_PASADA.txt` (**867
> bytes**). De ahi salio la pieza (d). **Hoy el caso de la 180 sale `HUECO` y
> `hueco_declarado_que_falta()` SI corre.**

**LA `P.1`**, primero el esperado y despues el nombre, que es parte de la
adjudicacion `6.6` (acta 180, **linea 62818**). Caia con **exit 1 fallando 1 de
6**; hoy sale **exit 0 con 7 de 7**. **Tres mitades**, y solo la primera estaba
encargada: el escenario historico se reconstruye de `git ls-tree` y `git show` en
vez de copiar `docs/loop/reportes/` **de hoy**; la comprobacion deja de preguntar
por el repo de hoy; y el bloque E deja de correr contra el arbol vivo y pasa a ser
**conducta sobre dos escenarios fabricados** (muerde cuando falta el archivo, deja
de morder cuando esta). **La segunda y la tercera aparecieron al medir y son la
misma especie que el `6.6` adjudica.** Salidas:
`SALIDA_V182_T1B_REMEDIO_P1.txt` (**2.337 bytes en disco y 2.337 normalizados a LF**),
`SALIDA_V182_T1B_REMEDIO_P1_MITAD_C.txt` (**1.395 bytes en disco y 1.395 normalizados a LF**) y
`SALIDA_V182_T1B_DECLARAR_CONGELADO_P1.txt` (**1.897 bytes en disco y 1.897 normalizados a LF**).

Renombrado con `git mv` a
`scripts/loop/vuelta172_tarea1c_caso_positivo_guarda_que_mordio.py`. **Censo 168 a
169**, **nomina 108 a 109**. Entra en la nomina porque **la regla de entrada es el
SUJETO CONGELADO y no el plazo de una vuelta**, y eso lo dice el propio fichero de
la bateria desde la 148. `anclaje_de()` lo dejaba en **NO DECIDIBLE** por cinco
apariciones de `REPORTE.md` en la maquina; cuatro eran prosa de `print` y el nombre
de un temporal y **se quitaron**, y la que queda es un `git show` de un blob
clavado, **declarada con su motivo y nombrando su linea**. Hoy: **CONGELADO**,
`guarda_del_sujeto_congelado()` **0**, `arneses_que_faltan()` **0**,
`nomina_invisible_al_censo()` **0**.

**1.c. LA RELECTURA AL DOBLE**, encargada por la `7.2` del acta 181
(`ACTA_AUDITOR.md:63171`) por `AUDITOR.md:57`. Instrumento
`scripts/loop/vuelta182_tarea1c_relectura_al_doble.py`, salida
`docs/loop/SALIDA_V182_T1C_RELECTURA_AL_DOBLE.txt` (**9.452 bytes en disco y 9.452 normalizados a LF**). El tramo son
los **30 puestos** que la seccion 8 del acta lista, leidos del acta en su
**linea 63210**; el doble son **30 vecinos deterministas** (el siguiente puesto
libre de cada uno), **solape con el tramo 0**, **60 releidos en total**. De los 60:
**3 declaran diferenciador**, **1 tiene lesion exacta** (el **2.464**) y **0 tienen
un nodo muerto**. La maquina **se importa** del instrumento de la TAREA 3.

> **LO QUE ESTA RELECTURA NO ES, Y SE DICE PARA NO VENDERLA DE MAS:** no vuelve a
> decidir la clase de ningun par. **Es la relectura MECANICA del tramo con la vara
> nueva de esta vuelta**, que es la unica que se puede correr sobre 60 pares sin
> inventarse nada. Lo que la vara no ve, esta salida **no lo afirma**.

### TAREA 3. EL INSTRUMENTO DEL DIFERENCIADOR MOVIDO

Instrumento `scripts/loop/vuelta182_tarea3_diferenciador_movido.py`, salida
`docs/loop/SALIDA_V182_T3_DIFERENCIADOR.txt` (**8.313 bytes en disco y 8.313 normalizados a LF**) y la lista en crudo
en `docs/loop/SALIDA_V182_T3_COLA.json` (**1.074 bytes en disco y 1.074 normalizados a LF**). Decision del fundador
del 5 sep 2026, PREGUNTA 1, opcion `b`.

**LA CRIBA, CONTADA DE ESE FICHERO Y NO TECLEADA:**

| condicion | cuantas `D` la pasan |
|---|---:|
| todas las `D` del archivo | **2.760** |
| 1. su razon **declara** un diferenciador | **99** |
| 2. y hoy el otro nodo **si lo tiene** | **6** |
| 3. y el paso **entra despues** del veredicto | **1** |

**EL CASO POSITIVO OBLIGATORIO SALE NOMBRADO: EL PUESTO 2.464.** Carece
`cero_defectos`; su **paso 7** de hoy cubre **3 palabras** del diferenciador
declarado con **cobertura 0.50**; veredicto del **2026-08-12** y el paso entra el
**2026-08-20**. **El acta 181 lo fecha a mano en `02384c6a`, 20 ago 2026, y
calzan**, sin que este instrumento le copie ninguna cifra.

**LAS VARAS NO SE ELIGEN A OJO.** El instrumento imprime el barrido entero de las
dos (`abs` 2 a 5 por cobertura 0.30 a 0.70) con cuantas `D` selecciona cada celda,
y la elegida (**abs 3, cobertura 0.45**) es **la celda mas estrecha que sigue
nombrando el 2.464**. La tabla va dentro de la salida para que la eleccion se
pueda discutir.

**DOS CORRECCIONES MIAS, LAS DOS CON SU SALIDA VIEJA GUARDADA:**

1. El contenido declarado se juzgaba **en bloque** y el 2.464 daba cobertura
   **0.19** y no salia. La razon enumera **dos cosas** separadas por punto y coma:
   **un diferenciador enumerado en dos se ha movido si se mueve uno.** Con el corte
   por punto y coma la primera da **0.50**.
2. El fechado buscaba el texto del paso **en el blob entero** del grafo y fechaba
   el paso del AQL el **2026-07-10**, contra el 20 ago que el acta 181 fecha a
   mano. **Ese texto vivia en otro nodo antes de la fusion.** Ahora se busca
   **dentro de su nodo**, parseando cada uno de los **165 commits** del grafo una
   sola vez para los seis pares. La salida equivocada queda entera en
   `docs/loop/SALIDA_V182_T3_DIFERENCIADOR_FECHADO_MALO.txt` (**7.894 bytes en disco y 7.894 normalizados a LF**).

**EL CENSO POR ESTADO DE LAS `A`, en el mismo instrumento:** **551** `A`, de ellas
**0 ejecutadas**, **551 pendientes** y **0 no decidibles**; la suma calza con 551.
De las pendientes, **8** tienen hoy su diferenciador declarado en el otro nodo y
quedan **marcadas RANCIAS por `P.5`**: **978, 2230, 2255, 2272, 2414, 2420, 2498 y
2509**. **No se encolan**, por la PREGUNTA 2 de la misma decision.

Caso positivo por mutacion **VERDE** con material fabricado
(`docs/loop/SALIDA_V182_T3_MUTACION.txt`, **1.607 bytes en disco y 1.607 normalizados a LF**): **5 casos, 5 calzan**,
el esperado mutado **CAE** y con la vara imposible la lesion **desaparece**. Ni el
archivo ni `dataset/` se leen en la mutacion.

> **ESTE INSTRUMENTO NO CAMBIA NINGUN VEREDICTO, no toca el marcador y no toca
> `docs/plan/`.** Solo mide y nombra. Encolar es la TAREA 4.

### TAREA 4. LA ENTRADA A LA COLA, Y EL TRAMO DECLARADO

Instrumento `scripts/loop/vuelta182_tarea4_entrar_a_la_cola.py`, salida
`docs/loop/SALIDA_V182_T4_COLA.txt` (**1.054 bytes en disco y 1.054 normalizados a LF**). Escribe en
`docs/plan/08_VERIFICACION.md` la seccion **LA ENTRADA POR EL DIFERENCIADOR
MOVIDO (5 sep 2026, vuelta 182)**, generada **leyendo el JSON de la TAREA 3** y no
tecleada.

**LA SEDE, MEDIDA ANTES Y DESPUES:** `docs/plan/08_VERIFICACION.md` pasa de
**64.355** a **67.121 bytes** y de **833** a **882 lineas**; **crece 2.766 bytes** y
**lineas que desaparecen: 0**. La lista del 12 ago 2026 sigue entera y el ancla
tambien, las dos comprobadas releyendo el fichero del disco.

**LO QUE ENTRA A LA COLA: el puesto 2.464, y nada mas.** Es la unica `D` que pasa
las tres condiciones. **El tramo queda declarado aqui y no se improvisa despues:**
**TRAMO 1 y unico con lo medido hoy, el unico par de arriba**, y se relee **entero
o no cuenta**; si el instrumento volviera a nombrar mas, cada grupo nuevo abre **su
propio tramo con su fecha**.

> **EN ESTA VUELTA NO SE RELEE NINGUN PAR**, que es literalmente lo que el encargo
> manda: *"se entra a la cola y se declara el tramo; no se releen 543 pares, que es
> justo lo que la decision evita"*. Ninguna clase cambia y el archivo de veredictos
> no se toca.

> **SOBRE `verificar_mapas_destejido.py`:** `EJECUTOR.md` 1 lo exige para **toda
> tabla de particion** (fila = destino, origenes, motivo). **La tabla de esta cola
> no es de particion**: sus filas son `par | clase | que le pasa | tras que
> operacion`, no hay destino ni origenes y no reparte nada. **Se dice, en vez de
> correr un instrumento sobre una tabla que no es la suya y publicar un verde que
> no significa nada.**

### TAREA 2. LA APERTURA DEL AUDITOR COMO CODIGO

**`scripts/loop/apertura_del_auditor.py`** (**11.444 bytes en disco y 11.444 normalizados a LF en disco**), con nombre
estable y sin numero de vuelta, como `aislador_de_ciega.py` y `cerrar_reporte.py`,
y **no se clona**. Decision del fundador del 5 sep 2026, PREGUNTA 3, opcion `c`,
la mitad que quita el problema de raiz; la otra mitad, que romper un remedio
escrito ACUMULE, ya estaba escrita en `AUDITOR.md`.

**COMO LO IMPIDE, Y ES LO UNICO QUE HACE.** Lleva una **bitacora de toques**: las
tres cosas prohibidas solo se hacen llamando a `git_log()`, `git_status()` y
`leer_reporte()`, y cada una **apunta su toque antes de hacerlo**. `sellar()`
**cae en rojo si la bitacora ya trae alguno de los tres, y no escribe nada**: no
avisa ni recomienda, **no sella**. La decision vive en `puede_sellar()`, separada
a proposito, para que el arnes la pueda tumbar **sin escribir un solo fichero**.

**EL CASO POR MUTACION, SOBRE VARIABLE COMPUTADA Y NO SOBRE CONSTANTE LITERAL**
(`EJECUTOR.md` 1, letra del 29 ago 2026). Instrumento
`scripts/loop/vuelta182_tarea2_mutacion_apertura_auditor.py`, salida
`docs/loop/SALIDA_V182_T2_MUTACION_APERTURA_AUDITOR.txt` (**5.078 bytes en disco y 5.078 normalizados a LF**).
**VERDE, 0 fallos**, con todo el material fabricado en un temporal que se borra:

- **6 escenarios** de `puede_sellar()`, los tres prohibidos uno a uno, los tres
  juntos, la bitacora limpia y un toque **no** prohibido. Los seis calzan.
- **Los tres prohibidos por su funcion de verdad**, no apuntados a mano:
  `puede_sellar()` pasa de `True` a `False` en los tres.
- **`sellar()` tras tocar: devuelve `False` y escribe CERO ficheros en el
  temporal.** No es que avise: es que no hay sello.
- **Y con la bitacora limpia SI sella**, con su ciega, su destape y su sello,
  para que se vea que no esta simplemente roto: *un guardia que no deja pasar a
  nadie no es un guardia, es una pared*.
- **LA MUTACION:** el veredicto computado tras `git_log()` es `False`; con el
  esperado `False` **PASA** y con el esperado `True` **CAE**. Y la segunda
  mutacion quita `git log` de la constante de prohibidos y el mismo escenario
  **cambia a `True`**, con la constante devuelta a su sitio despues.

`docs/loop/AUDITOR.md` gana el parrafo que nombra el fichero y **escribe el orden
obligatorio del turno como una linea de codigo y no como un recuerdo**.

> **LO QUE ESTE FICHERO NO PUEDE HACER, Y SE DICE EN VEZ DE VENDERLO DE MAS:** no
> puede impedir que alguien corra `git status` en su terminal por su cuenta.
> **Ninguna guarda de este repo puede.** Lo que si hace es que **el sello, que es
> lo que el acta cita como prueba, no se pueda escribir despues**; y con eso
> saltarse el remedio deja de ser un descuido y pasa a ser **una decision a
> sabiendas y sin sello**.

### TAREA 5. LA BATERIA DE LA 183, PREPARADA Y DECLARADA, Y NO CORRIDA

**`scripts/loop/vuelta183_bateria_por_tramos.py`** (**23.847 bytes en disco y 23.847 normalizados a LF en disco**),
**clon declarado** de `scripts/loop/vuelta176_bateria_por_tramos.py`, que es **el
precedente que la propia decision del fundador cita**. Cotejo del clon en
`docs/loop/SALIDA_V182_T5_COTEJO_CLON_BATERIA.txt` (**7.017 bytes en disco y 6.891 normalizados a LF**): **52
sentencias de codigo y 4 literales de texto**. **No sale vacio y no se dice que
salga**: el docstring entero cambia, el `TAMANO` cambia y el carril `--siguiente`
es nuevo.

**EL REPARTO, COMPUTADO Y NO TECLEADO** (`--plan`, salida en
`docs/loop/SALIDA_V182_T5_PLAN_BATERIA_183.txt`, **5.820 bytes en disco y 5.685 normalizados a LF**): **109 entradas
de nomina**, **tramo de 13**, **9 tramos**, y **la suma de las entradas de todos
los tramos es 109**, o sea que no se cae ni se repite ninguna. **Los nueve no son
un numero elegido: son los del precedente de la 176**, y el `TAMANO` es lo que se
ajusta para que salgan nueve, no al reves.

**LA ESTIMACION DEL RELOJ, DICHA COMO ESTIMACION Y NO COMO MEDICION**, con las
cifras del propio archivo: **entre 4,3 y 5,6 minutos por tramo** y **entre 36,0 y
46,9 minutos la nomina entera**. **La medicion de verdad la da cada tramo al
cerrarse.**

**EL CARRIL NUEVO `--siguiente` ES LA MITAD EN CODIGO DE "RETOMA EN EL TRAMO
SIGUIENTE".** El lanzador de la 176 ya era resumible de hecho, porque cada tramo
se corre con `--tramo N`; pero **saber cual tocaba era cosa de acordarse**, y
acordarse es lo que esta casa lleva vueltas demostrando que no funciona. Corrido
hoy (`docs/loop/SALIDA_V182_T5_SIGUIENTE_TRAMO.txt`, **1.178 bytes en disco y 1.154 normalizados a LF**): **9 tramos
del reparto, 0 con salida sellada, 9 faltan, EL SIGUIENTE ES EL TRAMO 1.**

> **Y UNA SALIDA SELLADA QUE MIDE CERO BYTES NO CUENTA COMO HECHA.** No es
> severidad: la bateria del ejecutor salio en **cero bytes tres vueltas seguidas**
> (171, 172 y 173) y esa es media causa del regimen entero de `AUDITOR.md` 6.1.
> Por la letra del 5 sep 2026, **una ruta que promete prueba y mide cero bytes es
> caida de cifra**.

**LO QUE ESTA VUELTA NO HACE CON ESTO, Y ES LO QUE SU ENCARGO MANDA:** *"Aqui solo
se deja preparada y declarada"*. Lo unico que se corrio de este fichero es
`--plan` y `--siguiente`, que **no tocan la nomina, no corren ningun arnes y no
escriben ninguna salida de bateria**. **No hay ninguna corrida de bateria en esta
vuelta**, y por eso la seccion 9 de este reporte cierra con su **hueco declarado y
medido**, que es lo que el regimen 6.1 manda para las vueltas intermedias.

**Y LA NOMINA CRECIO DENTRO DE ESTA MISMA VUELTA, con su corte al lado:** de
**108** a **109** entradas, por el arnes de la `P.1` que la TAREA 1.b remedio y
renombro. **La cifra de 109 es la de esta corrida de `--plan`, tomada al cierre y
no en la apertura**, porque la propia vuelta la movio.

<!-- FIN ANEXO DE TAREAS -->

## 3. EL CIERRE, CON SU IDENTIDAD LEIDA DE GIT

**LAS CINCO TAREAS DEL ENCARGO CERRARON, Y NINGUNA SE QUEDO ABIERTA.** El tope era
cinco y son cinco: ni una mas, como el propio encargo manda.

- rama, leida con `git rev-parse --abbrev-ref HEAD`: `pasada-unica`
- HEAD de apertura, sellado **antes de la primera operacion** en
  `docs/loop/SALIDA_V182_HEAD_APERTURA.txt`: **`326d7dc9`**
- HEAD de cierre, sellado **tras la ultima operacion** en
  `docs/loop/SALIDA_V182_HEAD_CIERRE.txt`: **`9357417d`**
- commit del acta 181, localizado en `git log` y no tecleado: **`b931019f`**
- commit de nacimiento del bloque de apertura, `git log --diff-filter=A`:
  **`c85f0c4d`**

**GATE 0 VERDE ENTERO EN SU CICLO, EN LA APERTURA Y OTRA VEZ AL CIERRE**, y las dos
columnas de la cabecera salen del tallador, no de mis dedos. **La vuelta no movio
ni una arista**: `+0 / +0 / +0 / +0`.

**EL BLOQUE DE APERTURA SE CORRIO TRES VECES Y LAS TRES SALIDAS QUEDAN**, sin
borrar ninguna: `SALIDA_V182_APERTURA_PRIMERA_CORRIDA.txt` (**33.313 bytes en disco y 33.313 normalizados a LF**),
`SALIDA_V182_APERTURA_SEGUNDA_CORRIDA.txt` (**35.299 bytes en disco y 35.299 normalizados a LF**) y la buena,
`SALIDA_V182_APERTURA.txt` (**36.679 bytes en disco y 36.679 normalizados a LF**). Las tres correcciones que lo
obligaron van en la seccion 8, que es donde vive lo que hice mal.

**LA CABECERA NO SE TECLEO Y SE COMPROBO QUE NO SE TECLEO**
(`EJECUTOR.md` 1, LA CABECERA DEL REPORTE SE TALLA, NO SE TECLEA). Corrido
`scripts/loop/tallar_cabecera_reporte.py --fase04 --vuelta 182 --comparar
docs/loop/REPORTE.md`, salida en `docs/loop/SALIDA_V182_TALLADOR_COMPARAR.txt`:
**filas cotejadas 9, DISTINTAS 0, ausentes 0, CABECERA IDENTICA AL TALLADOR**.

## 4. LA GUARDA DEL COMMIT DE `dataset/`, CORRIDA EL DIA QUE SERVIA

`scripts/loop/guarda_commit_dataset.py`, salida
`docs/loop/SALIDA_V182_GUARDA_COMMIT.txt` (**1.121 bytes en disco y 1.099 normalizados a LF**). `git status` daba
`M dataset/metadata/master_graph.json` **al abrir la vuelta y sigue dandolo al
cerrarla**, que es justo la firma que deja una bateria muerta a medias. **Se midio
antes de creerlo:** `git diff --numstat -- dataset/` da **cero filas**, y el blob
del arbol y el de `HEAD` son **el mismo, `cb33552aedddab4d`**. **Es artefacto de
fin de linea, no contenido. Ninguna perdida de catalogo que declarar**, y el
fichero **no se commitea**.

## 5. LOS DISCUTIBLES, MARCADOS ANTES DE SABER SI ACIERTO

**`D.1`. LA VARA DEL SOLAPE LEXICO ES MIA Y NO SALE DE NINGUNA DOCTRINA.**
`abs 3, cobertura 0.45` decide que `D` tienen lesion exacta. **La elegi de un
barrido que publico entero**, y el criterio fue *"la celda mas estrecha que sigue
nombrando el 2.464"*. **Es defendible y es discutible**: el caso positivo
obligatorio esta puesto por el fundador, asi que calibrar contra el no es hacer
trampas, **pero tampoco es una vara independiente**. Con `abs 2, cobertura 0.30`
saldrian **19** en vez de **6**. **Lo marco antes de saber si el auditor lo
concede.**

**`D.2`. LAS CLAUSULAS DE CARENCIA SON SEIS LITERALES Y NO UN ANALISIS.** De las
**2.760** `D`, solo **99** declaran su diferenciador de una forma que mi lista
reconoce. **No afirmo que las otras 2.661 no declaren ninguno: afirmo que mi lista
no lo ve**, que es otra cosa. Si el auditor cree que hay familias de redaccion
fuera de esas seis, la cifra de 99 sube y la de 6 puede subir con ella.

**`D.3`. EL CORTE DEL CONTENIDO POR PUNTO Y COMA Y POR LA ORACION DE RELATIVO.**
Sin el, el 2.464 da cobertura **0.19** y no sale; con el, da **0.50**. **Lo escribi
despues de ver que el caso obligatorio se caia**, y eso hay que decirlo tal cual.
Mi justificacion es que *"un diferenciador que la razon enumera en dos se ha movido
si se mueve uno"*, y me parece cierta; **pero el orden en que llegue a ella es el
que es.**

**`D.4`. METI EL ARNES DE LA `P.1` EN LA NOMINA EN ESTA MISMA VUELTA.** La letra
que cito para hacerlo (la regla de entrada es el sujeto congelado, no el plazo)
esta escrita en el propio fichero de la bateria desde la 148 y la lei hoy. **Pero
la costumbre de la casa es que un arnes entra a la vuelta siguiente**, y elegi la
letra sobre la costumbre **porque si no lo metia, la bateria de la 183 abriria en
rojo con `arneses_que_faltan()` en 1** por un motivo que no es una guarda rota.
**Puede que el auditor prefiera el rojo declarado.**

**`D.5`. LA DECLARACION DE SUJETO CONGELADO DEL ARNES DE LA `P.1`.** Sin ella el
anclaje queda en **NO DECIDIBLE** y la bateria entera sale roja. La escribi **solo
despues** de quitar cuatro de las cinco huellas de sujeto vivo y de comprobar que
la que queda es un `git show` de un blob clavado. **Sigue siendo una declaracion
del ejecutor sobre su propio arnes**, que es exactamente la figura que conviene
mirar dos veces.

**`D.6`. `--siguiente` CUENTA UNA SALIDA DE CERO BYTES COMO NO HECHA.** Lo
justifico con la letra del 5 sep 2026 sobre las rutas que prometen prueba, y con
las tres baterias de cero bytes de las vueltas 171, 172 y 173. **Nadie me encargo
esa regla para los tramos**, y la aplique por extension.

**`D.7`. LA SECCION QUE ESCRIBI EN `docs/plan/08_VERIFICACION.md` DICE "TRAMO 1 Y
UNICO".** Con un solo par en la cola, llamar a eso un tramo es casi un formalismo.
**Lo escribi asi porque la decision del fundador pide tramos y porque el numero
puede crecer**, pero admito que un tramo de uno es una palabra grande para una
lista corta.

## 6. LAS PREGUNTAS

1. **LA DEUDA DE REGISTROS DE OCHO ACTAS.** La serie `R.N` llega hasta el acta
   **172** (`R.42`) y esta vuelta escribe la del acta **181** (`R.43`). **Las
   actas 173 a 180 no tienen entrada propia**, medido hoy. **No las escribi porque
   nadie las encargo y serian ocho registros de golpe.** Pregunto si se recuperan,
   en que orden, y si el salto que ahora queda entre la 172 y la 181 se documenta
   como tal o se rellena.
2. **LAS SEIS `D` CON LESION EXACTA Y SOLO UNA CONFIRMADA.** Cinco tienen su
   diferenciador hoy en el otro nodo **pero el paso ya estaba el dia del
   veredicto**. Por mi lectura de la decision, **eso no es lesion: es un veredicto
   discutible**, que es otra cosa y no es de esta cola. **Pregunto si el fundador
   quiere que esas cinco vayan a algun sitio** o si se quedan donde estan.
3. **LAS OCHO `A` RANCIAS POR `P.5`.** Estan marcadas y contadas, y la decision
   dice que **no ganan cola**. Pero *"su vigencia se comprueba antes de ejecutar"*
   **no tiene hoy ningun instrumento que lo haga**. Pregunto si esa comprobacion
   se cablea o se deja al criterio de quien ejecute.

## 7. PENDIENTES DE DOCTRINA

**`PD.1`. NO HAY REGLA ESCRITA SOBRE QUE HACER CON UNA `D` CUYO DIFERENCIADOR
DECLARADO YA ESTABA EN EL OTRO NODO EL DIA DEL VEREDICTO.** Son las cinco de la
pregunta 2. La cola de relectura post fusion es para lo que **se movio despues**;
esto es un veredicto que pudo nacer discutible. **No lo resuelvo yo y no invento
una etiqueta:** se registra como pendiente y las cinco quedan nombradas en
`docs/loop/SALIDA_V182_T3_DIFERENCIADOR.txt`, seccion E.

**`PD.2`. LA CONVENCION DE BYTES SIGUE SIN FIJAR**, novena vuelta que sube. El
fundador decidio el 5 sep 2026 que **los tamanos van en bytes exactos y nunca
redondeados, con los KB solo entre parentesis**, y esta vuelta lo cumple: **no hay
ni un KB en este reporte**. Lo que sigue sin decidirse es **cual de las dos
convenciones de conteo manda**, disco o LF, y por eso la apertura las publica las
dos.

**`PD.3`. NINGUNA ETIQUETA DE VIA DICE "SUPERADA POR DECISION DEL FUNDADOR".** El
`R.43` vuelve a usar `EJECUTADA` y `SIN TOCAR NADA` porque son las que hay. Ya se
levanto en el `R.42` y sigue sin resolverse.

## 8. MIS CAIDAS PROPIAS, CON SU NOMBRE Y NINGUNA TAPADA

**`C.1`. CITE COMO PALABRAS DEL ACTA 180 UNA FRASE QUE ES MIA.** Escribi, en el
docstring del bloque de apertura, en el del esqueleto y en dos mensajes de commit,
que la adjudicacion `6.8` dice *"El tope vuelve a cinco en la 182"*. **Esa frase
literal no esta en el acta:** es del **reporte de la 181**
(`docs/loop/reportes/REPORTE_V181.md:21`), o sea prosa mia. El acta lo dice en su
punto 10, **linea 62893**, con otras palabras. **La sustancia coincide; la cita
no.** La cazo mi propio instrumento de la TAREA 1.a, que no encontro la aguja. **El
texto viejo no se borra: vive en `c85f0c4d` y `afa8ecc5`.**

**`C.2`. EL BLOQUE DE APERTURA HEREDO DEL CLON TRES LINEAS FALSAS.** Decia *"VUELTA
DE BATERIA, Y NO LLEVA NADA MAS"* y *"DOS sub-tareas"*, que eran verdad de la 181 y
falsas de la 182. **Es la especie exacta que `EJECUTOR.md` 1 persigue:** una frase
tecleada que sobrevive a un clon porque ningun instrumento la mide. La primera
corrida entera queda guardada.

**`C.3`. ADIVINE DOS CLAVES DEL GRAFO.** `G.get("nodes")` cuando el fichero las
guarda en `nodos`, y `pasos` o `steps` cuando se llaman `pasos_accionables`. **Las
dos publicaron cifras falsas** (*"CIFRA nodos del grafo: 0"* y *"cero_defectos con
0 pasos"*) en la primera y la segunda corrida de la apertura, **las dos
guardadas**. `EJECUTOR.md` 11 dice **NO ADIVINES**. La reparacion no teclea la
clave buena: **lista las claves y trabaja sobre la que exista.**

**`C.4`. EL FECHADO DE LA TAREA 3 BUSCABA EL PASO EN EL BLOB ENTERO.** Fechaba el
paso del AQL el **2026-07-10** contra el **20 ago 2026** que el acta 181 mide a
mano, **y con esa cifra el 2.464 NO entraba a la cola**: la corrida entera decia
*"LAS QUE ENTRAN A LA COLA: (ninguna)"*. **Lo cazo la contradiccion con el acta, no
un instrumento mio.** La salida equivocada queda entera en
`docs/loop/SALIDA_V182_T3_DIFERENCIADOR_FECHADO_MALO.txt` (**7.894 bytes en disco y 7.894 normalizados a LF**).

**`C.5`. PUBLIQUE DOS CIFRAS DE BYTES QUE NO CONTE DE SU FICHERO.** La seccion de
la TAREA 1 decia **1.607** y **5.573**; contados hoy de su fichero miden **1.531**
y **5.802**. **Los corregi en el reporte antes de publicarlo y lo digo aqui**,
porque es literalmente la caida que `EJECUTOR.md` 1 lleva desde el 26 ago
persiguiendo: **toda cifra se reconstruye contando su fichero antes de
publicarla.**

**`C.6`. MI PRIMER REMEDIO DEL `E.1` ERA INCOMPLETO Y LO DIJO SU PROPIO ARNES.** Lo
registro a favor del arnes y en contra mia: **escribi el arnes antes de aplicar el
remedio, y por eso se vio.** Las dos salidas del estado a medias quedan guardadas.

**`C.7`. PUBLIQUE 27 CIFRAS DE BYTES SIN SU PAREJA.** `cerrar_reporte.py` cierra el
reporte y despues corre `cifras_sin_pareja()`, y sobre este reporte recien cerrado
dio **27**; el acta 180 punto 6.7 midio **0** sobre el reporte de la 180. **La
diferencia es mia**: publique un solo numero por fichero, el de disco, y la casa
publica los dos mientras la convencion del fundador no este fijada. Lo arregle con
`scripts/loop/vuelta182_emparejar_cifras.py`, que **no cambia ningun numero**: mide
cada fichero por las dos convenciones y reescribe la frase. Salida en
`docs/loop/SALIDA_V182_EMPAREJAR_CIFRAS.txt`
(**2.844 bytes en disco y 2.844 normalizados a LF**): **27 lineas emparejadas,
0 que no se pudieron emparejar, y
`cifras_sin_pareja()` releida del disco da 0**. **Y cuatro ficheros tienen las dos
cifras DISTINTAS**, lo cual es justamente el motivo de que la casa publique las
dos.

> **NINGUNA DE LAS SIETE SE TAPA Y NINGUNA MOVIO UNA CIFRA PUBLICADA A ESPALDAS DE
> NADIE.** La `C.4` es la mas grave, porque **habria dejado la cola vacia** y con
> ella el encargo entero sin efecto; lo que la salvo fue **cotejar contra el acta
> en vez de creerle a mi instrumento**, que es `EJECUTOR.md` 2 al pie de la letra.

## 9. LA BATERIA DE MUTACIONES: HUECO DECLARADO Y MEDIDO

**HUECO DECLARADO Y MEDIDO. LA BATERIA DE LA VUELTA 182 NO CORRIO, Y EL HUECO SE DECLARA EN VEZ
DE RELLENARSE CON OTRA COSA.**

**EL NOMBRE DEL FICHERO:** `docs/loop/SALIDA_V182_BATERIA.txt`.
**SUS BYTES, MEDIDOS EN ESTA CORRIDA** con `os.path.getsize` por
`scripts/loop/cerrar_reporte.py`, no tecleados, y POR LAS DOS
CONVENCIONES mientras la del fundador no este fijada:
**0 bytes en disco y 0 bytes normalizados a LF**.

ATRIBUCION: NADIE LA CORRIO EN LA VUELTA 182, Y NO TENIA QUE CORRERLA: AUDITOR.md 6.1 la manda CADA CINCO en vuelta propia, la 181 era la suya y se corto antes de lanzarla, y la decision del fundador del 5 sep 2026 (PREGUNTA 4) la manda a la 183 POR TRAMOS RESUMIBLES. Su lanzador ya esta escrito y sin correr en scripts/loop/vuelta183_bateria_por_tramos.py, con nueve tramos computados de la nomina, y --siguiente dice hoy que el siguiente es el TRAMO 1.

**POR QUE ESTO CIERRA Y UNA AUSENCIA MUDA NO.** La pieza (4) de este
instrumento admite el hueco declarado desde la vuelta 173, TAREA 1.b
(adjudicacion 6.2 del acta del auditor de la vuelta 172), y la letra es
estrecha: **el nombre, los bytes medidos y la atribucion, LAS TRES JUNTAS**.
Faltando cualquiera de las tres, este instrumento sigue cayendo en ROJO, y
**una corrida de otra vuelta pegada aqui tampoco vale**.
