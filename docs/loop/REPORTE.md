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

**EL VEREDICTO DE UNA LINEA: SIN ESCRIBIR TODAVIA.** Se talla al cierre, cuando
haya de que hablar.

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
**PENDIENTE DE TALLAR AL CIERRE, Y SE DICE EN VEZ DE RELLENARLA.** La tabla sale
de `scripts/loop/tallar_cabecera_reporte.py --fase04 --vuelta 182`. **Esta
vuelta corrio el bloque de apertura entero ANTES de su primera operacion**, asi
que la mitad izquierda ya se puede leer: corrido aqui, el tallador dice **"ROJO,
19 celdas no se pudieron leer"** y de esas lineas de rojo, **0
mencionan APERTURA**. Este hueco se rellena con la tabla tallada entera cuando la
vuelta cierre.
<!-- FIN CABECERA TALLADA -->

## 1. LAS CINCO TAREAS DEL ENCARGO, Y SU ESTADO

<!-- TABLA DE TAREAS -->
| tarea | que encarga | estado | donde vive la prueba |
|---|---|---|---|
| **TAREA 1** | LOS REGISTROS Y LA DEUDA DE LECTURA. (a) El acta 181 y sus adjudicaciones entran en la serie de registros, con el numero que devuelve `scripts/loop/serie_de_registros.py` y no tecleado. (b) LOS DOS PENDIENTES DEL ACTA 180, que llevan una vuelta esperando y estan escritos en sus puntos `6.8` y `6.6`: el remedio del `E.1` sobre `scripts/loop/cerrar_reporte.py`, que es la rama que escribe la cabecera CORRIDA ENTERA Y SOLA sobre una seccion 9 cuyo cuerpo dice que nadie la corrio, y la `P.1`, el arnes `vuelta172_tarea1c_guarda_que_mordio.py`, que cae con exit 1 fallando 1 de 6 y esta fuera del censo: primero el esperado y despues el nombre, en ese orden, que es parte de la adjudicacion. (c) LA RELECTURA AL DOBLE del tramo de la ciega que el acta 181 encarga en su `7.2` por `AUDITOR.md` 1.2, sobre los 30 puestos que su seccion 8 lista | **CERRADA** | `SALIDA_V182_T1A_REGISTRO_ACTA_181.txt`, `_T1A_REGISTRO_R43.txt`, `_T1A_MUTACION_REGISTRO.txt`, `_T1B_REMEDIO_E1.txt`, `_T1B_ARNES_RAMA_SECCION9.txt`, `_T1B_REMEDIO_P1.txt`, `_T1B_REMEDIO_P1_MITAD_C.txt`, `_T1B_DECLARAR_CONGELADO_P1.txt`, `_T1C_RELECTURA_AL_DOBLE.txt` |
| **TAREA 2** | LA APERTURA DEL AUDITOR COMO CODIGO (decision del fundador del 5 sep 2026, PREGUNTA 3, opcion c, la mitad que quita el problema de raiz; la otra mitad, que ROMPER UN REMEDIO ESCRITO ACUMULE, ya esta escrita en `AUDITOR.md`). Fichero GEMELO del bloque de apertura del ejecutor: corre `scripts/loop/aislador_de_ciega.py` y SELLA SU SALIDA ANTES de que el turno pueda tocar `git log`, `git status` o `docs/loop/REPORTE.md`. Con CASO POR MUTACION SOBRE VARIABLE COMPUTADA, no sobre constante literal (`EJECUTOR.md` 1, EL CASO ROJO SE PRUEBA POR MUTACION): si el sello se intenta DESPUES de tocar cualquiera de los tres, TIENE QUE CAER, y la prueba se corre cambiando el valor esperado para comprobar que el caso cae de verdad | **ABIERTA, SIN CERRAR** | (la fila se anexa al cerrarse la tarea) |
| **TAREA 3** | EL INSTRUMENTO DEL DIFERENCIADOR MOVIDO (decision del fundador del 5 sep 2026, PREGUNTA 1, la `b`). Cruza LA RAZON ESCRITA de cada `D` contra LOS PASOS DE HOY del otro nodo, y SOLO las `D` con la lesion exacta vuelven a la cola. CASO POSITIVO OBLIGATORIO: EL PUESTO 2.464 TIENE QUE SALIR NOMBRADO; si no sale, el instrumento no sirve y se dice. Y EL CENSO POR ESTADO DE LAS `A` en el mismo instrumento: ejecutadas contra pendientes, con LAS PENDIENTES DE TEXTO MOVIDO MARCADAS RANCIAS POR `P.5`. Las `A` NO ganan cola nueva: la ejecutada es cosa consumada y la pendiente ya la cubre `P.5` | **CERRADA** | `SALIDA_V182_T3_DIFERENCIADOR.txt`, `SALIDA_V182_T3_COLA.json`, `SALIDA_V182_T3_MUTACION.txt`, `SALIDA_V182_T3_DIFERENCIADOR_FECHADO_MALO.txt` |
| **TAREA 4** | LAS `D` QUE EL INSTRUMENTO NOMBRE ENTRAN A LA COLA de relectura post fusion de `docs/plan/08_VERIFICACION.md`, y se releen POR TRAMOS en las vueltas siguientes. En esta vuelta SE ENTRA A LA COLA Y SE DECLARA EL TRAMO; no se releen 543 pares, que es justo lo que la decision del fundador evita al conceder la `b` y no la `c` | **CERRADA** | `SALIDA_V182_T4_COLA.txt`, y la seccion nueva en `docs/plan/08_VERIFICACION.md` |
| **TAREA 5** | LA VUELTA DE BATERIA VA EN LA 183, POR TRAMOS RESUMIBLES (decision del fundador del 5 sep 2026, PREGUNTA 4, opcion `a`, con el precedente de los nueve tramos de la vuelta 176). Aqui SOLO se deja preparada y declarada: nueve tramos, cada uno se commitea CON SU SALIDA SELLADA al terminar, una vuelta cortada RETOMA EN EL TRAMO SIGUIENTE, y la bateria se declara corrida cuando LOS NUEVE tienen salida sellada DEL MISMO CALIBRE. En esta vuelta la seccion 9 del reporte cierra con su HUECO DECLARADO Y MEDIDO, como el regimen `6.1` manda | **ABIERTA, SIN CERRAR** | (la fila se anexa al cerrarse la tarea) |
<!-- FIN TABLA DE TAREAS -->

## 2. LAS TAREAS, UNA POR UNA (cada seccion se ANEXA al cerrarse su tarea)

<!-- ANEXO DE TAREAS -->

### TAREA 1. LOS REGISTROS Y LA DEUDA DE LECTURA

**1.a. EL ACTA 181, CITADA CON SU LINEA.** Instrumento
`scripts/loop/vuelta182_tarea1_registros.py`, salida
`docs/loop/SALIDA_V182_T1A_REGISTRO_ACTA_181.txt` (**8.504 bytes**). Cabecera del
acta 181 en la **62907** y la del acta 180 en la **62449**, las dos localizadas y
no tecleadas. **42 agujas buscadas, 42 halladas, 0 no halladas**, contadas de ese
fichero.

**R.43 ESCRITO**, con el numero que devuelve `serie_de_registros.siguiente_libre()`
y no tecleado. Instrumento `scripts/loop/vuelta182_tarea1a_registrar_acta181.py`,
salida `docs/loop/SALIDA_V182_T1A_REGISTRO_R43.txt` (**2.910 bytes**). Titulo con
sus tres numerales contados del acta acotada (lineas 62907 a 63249): **5
adjudicaciones `7.n`**, **1 caida propia del auditor** (`C.1`, linea 62932) y **1
del ejecutor** (`E.2`, linea 63078). `docs/PENDIENTES.md` pasa de **843.961** a
**850.711 bytes**. Caso por mutacion **VERDE**
(`docs/loop/SALIDA_V182_T1A_MUTACION_REGISTRO.txt`, **1.531 bytes**): 4 actas
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

**EL `E.1`**, sobre `scripts/loop/cerrar_reporte.py` (**38.947 a 43.563 bytes**).
Tres causas medidas y **cuatro piezas** de remedio: el patron no casaba con
`SALIDA_V180_HUECO_BATERIA` y daba `None`; con `None` la guarda de vuelta ajena se
saltaba en silencio; la rama se elegia solo por si el fichero traia lineas; y **una
corrida no es cualquier fichero con lineas, tiene que llamarse como una corrida**.
La decision sale de `main()` y pasa a ser `rama_de_la_seccion9()`, pura y con arnes
propio: **9 casos, 9 calzan, 4 en que la logica vieja y la viva difieren**, y las
dos mutaciones **CAEN**
(`docs/loop/SALIDA_V182_T1B_ARNES_RAMA_SECCION9.txt`, **5.802 bytes**).

> **EL ARNES CAZO QUE MI PRIMER REMEDIO ERA INCOMPLETO.** Con solo tres piezas
> salia VERDE en sus nueve casos **y su propia seccion C publicaba que el caso real
> de la 180 seguia saliendo `CORRIDA`**. Esa salida queda entera en
> `docs/loop/SALIDA_V182_T1B_ARNES_REMEDIO_INCOMPLETO.txt` (**5.293 bytes**) y el
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
`SALIDA_V182_T1B_REMEDIO_P1.txt` (**2.337 bytes**),
`SALIDA_V182_T1B_REMEDIO_P1_MITAD_C.txt` (**1.395 bytes**) y
`SALIDA_V182_T1B_DECLARAR_CONGELADO_P1.txt` (**1.897 bytes**).

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
`docs/loop/SALIDA_V182_T1C_RELECTURA_AL_DOBLE.txt` (**9.452 bytes**). El tramo son
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
`docs/loop/SALIDA_V182_T3_DIFERENCIADOR.txt` (**8.313 bytes**) y la lista en crudo
en `docs/loop/SALIDA_V182_T3_COLA.json` (**1.074 bytes**). Decision del fundador
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
   `docs/loop/SALIDA_V182_T3_DIFERENCIADOR_FECHADO_MALO.txt` (**7.894 bytes**).

**EL CENSO POR ESTADO DE LAS `A`, en el mismo instrumento:** **551** `A`, de ellas
**0 ejecutadas**, **551 pendientes** y **0 no decidibles**; la suma calza con 551.
De las pendientes, **8** tienen hoy su diferenciador declarado en el otro nodo y
quedan **marcadas RANCIAS por `P.5`**: **978, 2230, 2255, 2272, 2414, 2420, 2498 y
2509**. **No se encolan**, por la PREGUNTA 2 de la misma decision.

Caso positivo por mutacion **VERDE** con material fabricado
(`docs/loop/SALIDA_V182_T3_MUTACION.txt`, **1.607 bytes**): **5 casos, 5 calzan**,
el esperado mutado **CAE** y con la vara imposible la lesion **desaparece**. Ni el
archivo ni `dataset/` se leen en la mutacion.

> **ESTE INSTRUMENTO NO CAMBIA NINGUN VEREDICTO, no toca el marcador y no toca
> `docs/plan/`.** Solo mide y nombra. Encolar es la TAREA 4.

### TAREA 4. LA ENTRADA A LA COLA, Y EL TRAMO DECLARADO

Instrumento `scripts/loop/vuelta182_tarea4_entrar_a_la_cola.py`, salida
`docs/loop/SALIDA_V182_T4_COLA.txt` (**1.054 bytes**). Escribe en
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

<!-- FIN ANEXO DE TAREAS -->
