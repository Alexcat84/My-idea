# REPORTE DE LA VUELTA 50 (19 ago 2026, ejecutor Opus 5)

**LA TAREA 1 ENTERA, y con ella el instrumento del barrido REPARADO: perseguia una averia
que el mismo tenia. DE LA TAREA 2, UN ACTO DE VEINTISEIS, y lo que lo frena no es la
cuerda sino un hallazgo: LA RECETA DE `P.12` DEL ENCARGO NO ESTA DEFINIDA PARA LA FORMA
QUE TIENEN 24 DE LOS 26 MIXTOS. Medido antes de tocar un nodo, generalizado desde el
unico acto ya resuelto, y comprobado que NINGUN acto se queda sin superviviente posible,
asi que no hay parada.**

| | |
|---|---|
| **rama** | `pasada-unica` |
| **hash de apertura** | `b8d1083a` (el acta de la vuelta 49), **arbol limpio y todo pusheado** |
| **commits de la vuelta** | **2**: `d485284a` (TAREA 1) mas el del cierre |
| **arbol al cierre** | limpio tras el commit del cierre |

---

## 0. LA APERTURA, MEDIDA ANTES DE LA PRIMERA OPERACION (regla 1)

**Corrida ANTES de tocar nada**, con `python scripts/loop/vuelta31_estado.py APERTURA_V50`
([`SALIDA_V50_APERTURA.txt`](SALIDA_V50_APERTURA.txt)). **El arbol estaba limpio y todo
pusheado en `b8d1083a`, asi que la regla 3 se cumplio por vacio, y se dice asi en vez de
darla por cumplida.**

| | **apertura**, antes de la 1.ª operacion | **cierre, RECOMPUTADO al cierre** |
|---|---:|---:|
| marcador `A` / `B` / `C` / `D` | 573 / 77 / 8 / 2.730 | **571 / 77 / 8 / 2.732** |
| `n`, huecos, duplicados | 3.388 / 0 / 0 | **3.388 / 0 / 0** |
| tasa de `A` | 16,9 | **16,9** |
| grafo: ficheros / vivos / deprecados / enlaces | 3.853 / 3.499 / 354 / 16.984 | **3.853 / 3.498 / 355 / 16.986** |
| retrato: `A` crudas / colapsos / pares distintos | 573 / 48 / 525 | **571 / 49 / 522** |
| operaciones, estados, dependencias rotas | 71, todas `LISTA`, 0 | **71, todas `LISTA`, 0** |
| entradas del inventario | 672 | **672** |
| actos `CERRADOS` / `ABIERTOS` | 252 / 53 | **251 / 53** |
| nodos en `CERRADOS` / `ABIERTOS` | 536 / 240 | **532 / 240** |
| cola de costuras | 1.491 | **1.491** |
| duplicadas tras resolver / auto-aristas | 1.002 / 0 | **1.002 / 0** |
| colisiones de clase vigentes | 0 | **0** |

**El cierre esta RECOMPUTADO al cierre** ([`SALIDA_V50_CIERRE.txt`](SALIDA_V50_CIERRE.txt),
[`SALIDA_V50_MARCADOR_CIERRE.txt`](SALIDA_V50_MARCADOR_CIERRE.txt),
[`SALIDA_V50_RECOMPUTO_CIERRE.txt`](SALIDA_V50_RECOMPUTO_CIERRE.txt),
[`SALIDA_V50_COLA.txt`](SALIDA_V50_COLA.txt)), **no copiado de la apertura.**

**Las cinco familias de libro no se mueven** (Weinberg 68/66, Horowitz 91/89, Hugos
111/111, Coleman 74/72, Rackham 46/46): el unico nodo que muere hoy es de `health_safety`.

---

## 1. TAREA 1.1: LAS TABLAS SIN BARRER, Y EL BARRIDO QUE NO SABIA BUSCAR

**Siete celdas corregidas con tachado, fecha y motivo, y TODAS las cifras de instrumento
corrido HOY** ([`SALIDA_V50_CORRECCIONES_910.txt`](SALIDA_V50_CORRECCIONES_910.txt)):

| la celda | decia | **medido hoy** |
|---|---:|---:|
| informe **100.1**, fila `A` / fila `D` | 574 / 2.729 | **573 / 2.730** |
| `RECOMPUTO_3388.md` **246** (`A` crudas) | 574 | **573** |
| **247** (colapsos a auto-arista) | 41 | **48** |
| **248** (pares distintos) | 533 | **525** |
| **1079** (total de `A`) | 574 | **573** |
| checkpoint **ii** de la **528** | 533 igual a 533 | **525 igual a 525, sigue OK** |

**Y el 41 no era un error de lectura**: era el corte de la TAREA 1.3 de la vuelta 49,
tomado ANTES de las tres fusiones de su propia TAREA 2. **Los siete que faltaban son la
huella de esas tres fusiones, que es lo que la propia fila ya explicaba de las 41.**

**Mas una CUARTA correccion declarada de la fila `core`**, que la cadena no tenia: el
dominio vigente es **334** y sin ella la unica cifra legible como reciente era la del 18 ago.

### EL HALLAZGO DEL TRAMO: EL INSTRUMENTO DEL BARRIDO TENIA LA AVERIA QUE PERSEGUIA

**Medido antes de escribir una linea del sucesor**
([`SALIDA_V50_BARRIDO_910_INSTRUMENTO_VIEJO.txt`](SALIDA_V50_BARRIDO_910_INSTRUMENTO_VIEJO.txt)):
`vuelta49_barrido_910.py` **acepta `--viejo` pero NO LO USA PARA BUSCAR**. Sus dos
expresiones regulares estan clavadas a `583` y `2709`, las cifras de la vuelta 14, y
`--viejo` solo cambia la cabecera que imprime. Corrido con `--viejo 574,77,8,2729`
devuelve 22 candidatos, **y los devuelve porque esas celdas arrastran el 583 en su cadena
de tachados, no porque sepa buscar el 574**. **Una celda nueva escrita hoy con la cifra
vigente y sin cadena de tachados le seria INVISIBLE.**

**El sucesor `scripts/loop/vuelta50_barrido_910.py`** busca de verdad lo que se le pide,
conserva la familia legado y anade **la familia del RETRATO**, que ningun barrido anterior
miraba. **Con el, las siete celdas salen solas**, y al cierre saco tambien las que esta
misma vuelta habia escrito (seccion 5).

---

## 2. TAREA 1.2: EL CONTADOR LD, TERCER NIVEL, Y UNA RAZON MAS FUERTE QUE LA DEL NIVEL

**Tercera correccion declarada sobre el mismo instrumento, con el texto viejo del criterio
delante y sin borrar.** Excluidos los **REGISTROS DEL ARNES** por patron
`docs/loop/ultimo_*.json` (hoy `ultimo_ejecutor.json` y `ultimo_auditor.json`;
`loop.log` ya quedaba fuera por extension, y se dice en vez de darlo por supuesto).

> **Y LA RAZON QUE DE VERDAD LOS CONDENA NO ES EL NIVEL: ES QUE SU CONTENIDO NO ES
> REPRODUCIBLE.** Mi corrida previa dio **2** y no los **4** del auditor
> ([`SALIDA_V50_CONTAR_LD_ANTES.txt`](SALIDA_V50_CONTAR_LD_ANTES.txt)), **porque
> `ultimo_ejecutor.json` estaba en CERO BYTES**: el arnes lo vacia al abrir la sesion y lo
> reescribe al cerrarla. **El mismo instrumento, mismo repo, mismo dia, devuelve una cifra
> distinta segun EN QUE MINUTO de la sesion se corra.** Una celda publicada no puede colgar
> de eso. **La discrepancia con el auditor se declara y no se resuelve copiando** (regla 2).

**CASO POSITIVO CORRIDO, y es lo que cierra el argumento**
([`SALIDA_V50_CONTAR_LD_CASO_POSITIVO.txt`](SALIDA_V50_CONTAR_LD_CASO_POSITIVO.txt)): con
una sonda que repone la cita en el fichero del arnes, **el instrumento VIEJO da 4, y son
exactamente los `LD-12` y `LD-27` que el auditor midio**; el corregido da **2**. Arnes
restaurado a cero bytes, que es como estaba.

| | cifra vieja (corte 12 ago) | **medida hoy, tras la correccion** |
|---|---:|---|
| lecturas dirigidas **hechas** | 65 | **81** |
| nombrados **sin seccion propia** | | **2**: `LD-71` y `LD-99`, los dos ya adjudicados como NO pendientes |
| **encargadas sin hacer** (la celda publicada) | CERO | **CERO, y la celda aguanta** |

**LAS DOS CELDAS DEL `00_INDICE` SE REPRODUCEN: 81 y CERO. Ninguna parada.**

---

## 3. TAREA 1.3: EL ALIAS `modelo_spin_2`, CON UN FILO MAS QUE LA OBSERVACION DEL ACTA

**Una linea en el registro del tramo y cero datos tocados**, que es lo que el encargo
manda. Medido hoy ([`SALIDA_V50_ALIAS_DURMIENTE.txt`](SALIDA_V50_ALIAS_DURMIENTE.txt)):

| | |
|---|---|
| quien lo declara | `modelo_spin`, **que esta DEPRECADO** |
| **por el resolutor de la casa** (`P.1`, mapa de alias solo de vivos) | **NO RESUELVE EN ABSOLUTO** |
| por la cadena ancha | `modelo_spin_2` a `modelo_spin` **[DEP]** a `modelo_spin_preguntas` |
| referencias en aristas / en veredictos | **CERO** / **CERO** |

**El acta decia que resuelve por cadena; medido con la vara de la casa, para todo conteo
publicado ese id se queda DONDE ESTA.** Pasivo de `OP-S-12`, nombrado y no reparado.

> **CORRECCION DECLARADA SOBRE MI PROPIO INSTRUMENTO NUEVO, en la vuelta en que nacio:** la
> primera version leia los campos `id` y `alias` en vez de `node_id` e `ids_alias`, y
> **imprimio un resultado que POR CASUALIDAD se parecia al hallazgo verdadero**. Eso es lo
> que la hacia peligrosa: una medicion que sale bien por el motivo equivocado no es una
> medicion. **Corregida antes de publicar cifra alguna.**

---

## 4. TAREA 2: LO QUE FRENO EL TRAMO NO FUE LA CUERDA

### 4.1 EL TRAMO 1, RE-IDENTIFICADO POR MIEMBROS Y NO POR NUMERO

**Lo manda el encargo y era necesario**: el numero de acto baila con cada fusion.
Instrumento nuevo `vuelta50_tramo_por_miembros.py`, que resuelve por `P.1` y casa
conjuntos ([`SALIDA_V50_TRAMO1_POR_MIEMBROS.txt`](SALIDA_V50_TRAMO1_POR_MIEMBROS.txt)).

| de los 50 actos del tramo | al abrir | **al cerrar** |
|---|---:|---:|
| **CONSUMIDOS** (ya fundidos) | 18 | **18** |
| **VIVOS** en la nomina | 31 | **30** |
| **PARTIDOS** (no calzan enteros hoy) | 1 | **2** |
| de los vivos: **MIXTOS** pendientes de `P.12` | **26** | **25** |
| de los vivos: **DECLARADOS** | 5 | **5** |

> **LA CIFRA DEL ENCARGO NO CUADRA CON LA MEDICION Y SE DECLARA EN VEZ DE COPIARSE**
> (regla 2): **el encargo pide *las veinticinco lecturas `P.12` pendientes*, y al abrir esta
> vuelta eran VEINTISEIS.** El 25 viene de una fila del registro de la vuelta 49 que en la
> misma pagina convive con un **26 de 26**. La vuelta 48 dejo **27** y la 49 resolvio **uno**.

### 4.2 LA RECETA DEL ENCARGO NO ESTA DEFINIDA PARA 24 DE LOS 26. **ESTE ES EL HALLAZGO**

**El encargo dice: elige el superviviente de la PARTE A y lee el MIXTO contra el.** Eso
presupone la forma del unico acto ya resuelto (el del SPIN): **una clique `A` mas UN nodo
colgando.** **El primer acto que abri no la tiene**, y por eso lo primero fue medir las 26
([`SALIDA_V50_FORMA_MIXTOS.txt`](SALIDA_V50_FORMA_MIXTOS.txt)):

| forma del subgrafo `A` | actos |
|---|---:|
| **CLIQUE MAS COLGANTE**, donde la receta se aplica sola | **2** |
| **ESTRELLA**: un centro que repite contra cada punta, y puntas que no se parecen entre si | **24** |

**No es una rareza: es la figura `9.23` del banco**, y **el propio archivo la nombra** (el
puesto **1201** dice, con esa palabra, *este par cierra una ESTRELLA*). Lo que `9.23` no
dice es **quien sobrevive cuando el centro repite contra varios nodos que son `D` entre si**.

**LA DEFINICION OPERATIVA, sacada del acto ya resuelto y NO inventada:** en el SPIN la
parte A fueron los nodos **con arista `A` contra el superviviente**, y el mixto el unico
**sin** arista `A` contra el. Generalizado, mas una comprobacion que es aritmetica y no
criterio: un superviviente es **VIABLE** si su parte A es clique `A` (si no, fundirla
juntaria dos nodos que el archivo declaro `D`, que es lo que `P.12` prohibe) y si deja al
menos un mixto fuera
([`SALIDA_V50_SUPERVIVIENTES_VIABLES.txt`](SALIDA_V50_SUPERVIVIENTES_VIABLES.txt)).

| | actos |
|---|---:|
| **VARIOS VIABLES**, y el CONTENIDO decide, que es la regla de la pagina | **26 de 26** |
| **NINGUNO VIABLE**, que habria sido parada | **CERO** |

> **NINGUN ACTO SE QUEDA SIN SUPERVIVIENTE POSIBLE: NO HAY CONDICION DE PARADA.** Lo que
> hay es que **en la estrella el CENTRO casi nunca es viable.**

**Y UN CHOQUE MEDIDO: CINCO veredictos en CUATRO actos** (hoy el **3**, que trae dos, el
**27**, el **28** y el **29**) **cierran con *Sobrevive X* apuntando a un `X` que NO es
viable** por la estructura de su acto. **Se mide, se nombra y se trae.**

### 4.3 EL ACTO 1 EJECUTADO ENTERO: EL RACIMO DE LA DERIVA

| | |
|---|---|
| **superviviente** | `normalizacion_de_la_desviacion`, por **CONTENIDO** sin empate (6 pasos contra 4, 4 condiciones contra 2, resumen de 711 contra 574/466/458), **y el propio 2237 cierra con *Sobrevive normalizacion_de_la_desviacion*** |
| absorbe | `drift_hacia_el_fallo_2` |
| **guarda de las puertas (`1B`)** | **por vacio**: el acto no esta entre los 30 SALVABLES ni entre los 2 IMPOSIBLES ([`SALIDA_V50_PUERTAS_EN_EL_LOTE.txt`](SALIDA_V50_PUERTAS_EN_EL_LOTE.txt)) |
| **las dos lecturas `P.12`** | `deriva_hacia_el_fallo` y `drift_hacia_el_fallo`, **las dos `CONTINUA`**, con los puestos 2275 y 2394 citados |
| aristas declaradas (`P.9`, sin ejecutar) | **2**, con su poda de solape anotada para la fase 04 |
| **las ocho guardas del instrumento** | **todas OK**, incluido el reparto sin olvidos (6 piezas: 4 viajan, 1 ya estaba, **1 de INCISO**) |
| censo | 3.499 a **3.498** vivos, delta deprecados **+1 sobre +1 esperado** |

**LAS DOS COLISIONES QUE FABRICO, LIMPIADAS EN EL MISMO ACTO (`P.16`)**, con la razon vieja
pegada por maquina: **2222 y 2226, de `A` a `D`**. **LA CUENTA CALZA CON LA QUE EL ENCARGO
EXIGE: dos `CONTINUA`, dos colisiones, cero por `ENTRA`**
([`SALIDA_V50_CENSO_COLISIONES_ACTO1.txt`](SALIDA_V50_CENSO_COLISIONES_ACTO1.txt)). **Censo
tras la limpieza: CERO colisiones vigentes.**

---

## 5. EL BARRIDO DEL CIERRE, QUE ES LA REGLA DEL AVISO, Y SE CORRIO SOBRE MI PROPIA VUELTA

**La TAREA 1.1 corrigio siete celdas con el marcador de ESE momento. Despues la TAREA 2 lo
movio otra vez.** Dejarlas asi habria sido repetir, **dentro de la misma vuelta**, la caida
que esta vuelta vino a corregir. **El barrido se corrio DESPUES del ultimo movimiento**
([`SALIDA_V50_BARRIDO_910_CIERRE.txt`](SALIDA_V50_BARRIDO_910_CIERRE.txt)) **y saco DIEZ
correcciones mas** ([`SALIDA_V50_CORRECCIONES_910_CIERRE.txt`](SALIDA_V50_CORRECCIONES_910_CIERRE.txt)):
las filas 246, 247, 248, 528 y 1079, el apendice 100.1 entero, y **el encabezado de mi
propia tabla de la TAREA 1.1**, que decia *hoy, medido en esta vuelta* y por tanto se
presentaba como vigente. **Su cifra NO se toco** (fue exacta al escribirse; reescribirla
fabricaria una corrida que nunca existio): **se corrigio el titulo.**

**Y UNA AFIRMACION HEREDADA QUE ESTA VUELTA DESMIENTE, dicha en vez de dejada correr:** las
cuatro correcciones declaradas anteriores de la tabla por dominio decian, cada una, que **el
unico dominio que se mueve es `core`**. Hoy no: **los dos volteos de `P.16` son de
`health_safety`**, que baja de `A 45` a `A 43` (23,4 a 22,4 por ciento) mientras `core` se
queda quieto en 334. **Queda escrita como quinta correccion declarada.**

**Re-barrido de comprobacion tras corregir: ninguna celda vigente conserva la cifra vieja**
([`SALIDA_V50_BARRIDO_910_TRAS.txt`](SALIDA_V50_BARRIDO_910_TRAS.txt)). **Y los tres
contadores de correccion (*CORREGIDA N VECES*) se cuadraron con su cadena de tachados: 7, 4
y 7**, que es una incoherencia que las propias correcciones habrian dejado dentro.

---

## 6. GATE 0 Y LAS SUITES

**Corridos tras la TAREA 1 y otra vez al cierre. Todos exit 0.**

| que | como salio |
|---|---|
| **Gate 0**, ciclo de **TRES** comandos | `run_phase1 --reaplico-curaduria` con **`GATE 0: OK`**; `etiquetas_de_cara --aplicar` con **71** etiquetas; `sync_assets_web` con **6** assets |
| **suite del motor** | **25 de 25** |
| **suite web** | **80** ficheros, **1.030** pasadas y **3** saltadas |
| `tsc --noEmit` | **CERO** lineas |
| duplicadas tras resolver / auto-aristas **NUEVAS** | **CERO** y **CERO** (1.002 y 0 en la base, 1.002 y 0 despues) |
| las cuatro comprobaciones de `08_VERIFICACION` | **TODAS OK** |
| **hook guardian** | verde en todos los commits |

---

## 7. CORRECCIONES DECLARADAS SOBRE MI PROPIO TRABAJO

1. **EL INSTRUMENTO DEL BARRIDO `9.10` NO BUSCABA LO QUE SE LE PEDIA**, y por eso el
   barrido de la vuelta 49 tranquilizaba sin mirar. **Sucesor escrito con el motivo medido
   delante.**
2. **MI CONTADOR LD SE LEIA A SI MISMO UN TERCER NIVEL MAS ARRIBA**, y la razon de fondo
   es peor que el nivel: **su fuente no es reproducible dentro de una misma sesion.**
3. **MI INSTRUMENTO DE ALIAS NACIO LEYENDO LOS CAMPOS EQUIVOCADOS** y dio un resultado que
   se parecia al bueno. **Declarado en su propio docstring.**
4. **LA TABLA QUE ESCRIBI EN LA TAREA 1.1 ENVEJECIO DENTRO DE MI PROPIA VUELTA**, y la
   destapo mi propio barrido del cierre. **Corregido el encabezado, no la cifra.**
5. **Ficheros tocados que el encargo no nombraba, declarados:** `docs/COSTURAS_INTERNAS.jsonl`
   y `docs/COSTURAS_INTERNAS_RESUMEN.md`, que `scripts/costuras_internas.py` reescribe al
   correrse. **Mismo alcance que las vueltas 48 y 49, y se vuelve a declarar.**
6. **UNA CIFRA MIA QUE CONVIVE CON OTRA Y SE EXPLICA EN VEZ DE ESCONDERSE:** el recomputo
   cuenta **49 veredictos `A` que colapsan a auto-arista** y mi censo propio cuenta **32
   auto-pares**. **No es discrepancia: son dos universos**, uno cuenta veredictos y el otro
   pares resueltos distintos (varios veredictos colapsan al mismo nodo).

---

## 8. LOS DISCUTIBLES MARCADOS, para la relectura ciega

**Marcados ANTES de saber si acierto. Son OCHO.**

| # | el discutible | por que lo marco |
|---:|---|---|
| **D1** | **Hice 1 de las 26 lecturas `P.12` y NO abri el tramo 2. Es el discutible mayor y es de alcance.** | Entregue **un acto de veintiseis**. Lo que consumio la vuelta no fue la TAREA 1 sino **medir que la receta no estaba definida** para 24 de los 26 y generalizarla desde el unico precedente. **Si el auditor lee que la generalizacion era obvia y que habia que fundir sin medirla, esto es una caida de reparto y la marco yo** |
| **D2** | **Generalice la definicion de PARTE A y de MIXTO, que el encargo daba por sabida.** | La saque del acto del SPIN por induccion de UN caso, no de una regla escrita. **Es la pieza mas discutible de la vuelta**: si el auditor lee que "parte A" significaba otra cosa, las dos lecturas del acto 1 y sus dos volteos estan mal fundados |
| **D3** | **Elegi `normalizacion_de_la_desviacion` sobre dos candidatos que los otros veredictos `A` nombran.** | Los tres `A` del acto nombran **tres supervivientes distintos**, y el 2237 dice con esas palabras que **cual sobrevive se resuelve en el racimo, no par a par**. **Elegi por CONTENIDO como manda la pagina y cite el 2237 a mi favor, pero el mismo veredicto declara la cuestion abierta.** Un lector puede decir que este acto era DECLARADO, no fundible |
| **D4** | **Marque el paso 3 del que muere como INCISO y no como `CUBIERTO`.** | El 2237 lo llama **un EJEMPLO** del paso 3 del superviviente. **Un ejemplo puede leerse como ya cubierto**, y entonces el inciso anade texto que nadie pidio. Elegi la figura del INCISO porque el ejemplar concreto es lo unico que vuelve palpable la relajacion de criterios |
| **D5** | **Marque el paso 2 del que muere como `APPEND` teniendo el paso 5 del superviviente cerca.** | El paso 5 ya manda *evaluar si estas ignorando tus propias senales de alerta*. **Lo que anade el 2 es que la senal EXISTIO Y NO SE REPORTO**, que es mecanismo de organizacion y no de atencion propia. **El veredicto lo cuenta como linea propia y le hice caso, pero el solape es real y lo digo** |
| **D6** | **Corregi el ENCABEZADO de una tabla que yo mismo habia escrito seis horas antes, en vez de declararla y encargarla.** | Es alcance sobre trabajo de la propia vuelta. **La alternativa era dejar viva una columna titulada *hoy* con una cifra que ya no era la de hoy**, que es exactamente la especie de la caida de la vuelta 49 |
| **D7** | **Cuadre los contadores *CORREGIDA N VECES* de tres filas.** | **Nadie me lo pidio.** Los deje coherentes con su cadena de tachados porque una fila que dice SEIS con siete tachados es una cifra publicada mal. **Si el auditor lee que el contador cuenta otra cosa (por ejemplo, actos de correccion y no cifras), tres de mis ediciones sobran** |
| **D8** | **Declare que el encargo pide 25 lecturas cuando yo mido 26, en vez de aceptar el 25.** | La regla 2 manda declarar la discrepancia. **Pero el 25 viene del acta y del encargo, o sea de mi auditor**, y estoy contradiciendo su cifra con la mia. **Si mi universo esta mal definido, el equivocado soy yo y la declaracion es ruido** |

---

## 9. PENDIENTES DE DOCTRINA

1. **LA ESTRELLA CON PUNTAS `D` NO TIENE REGLA DE SUPERVIVIENTE.** El banco `9.23` define
   la figura y su coste (*el centro contra cada periferico, por separado*), pero **no dice
   que hacer cuando el centro repite contra `N` nodos que son `D` entre si**: el centro solo
   puede morir una vez. **Afecta a 24 de los 26 mixtos pendientes.** Mi salida (elegir por
   CONTENIDO entre los viables y leer los demas por `P.12`) **es una lectura mia y merece
   adjudicacion.**
2. **UN VEREDICTO `A` QUE NOMBRA UN SUPERVIVIENTE NO VIABLE.** Medido en **cinco
   veredictos de cuatro actos**. La letra del veredicto y la aritmetica del acto apuntan a
   sitios distintos, **y ninguna regla dice cual manda.**
3. **HEREDADOS Y SIN CAMBIO HOY**: el INCISO para condiciones **sigue sin existir** en el
   instrumento (el acta 49 lo dejo como extension citable, a fabricar cuando un caso real lo
   pida; esta vuelta no lo pidio); el esquema de `OPERACIONES.jsonl` **sigue sin distinguir
   ejecutada de pendiente** (71 en `LISTA`, medido hoy); y el campo `orden` de la fase 03
   **sigue sin ser su criterio de orden**.

---

## 10. LO QUE ESTA VUELTA NO HIZO, DICHO EN VEZ DE CALLADO

1. **NO hizo 25 de las 26 lecturas `P.12`.** Solo el acto 1, con sus dos lecturas. **Es el
   incumplimiento mayor de la vuelta**, y no lo tapo la TAREA 1.
2. **NO abrio el tramo 2** de 50 actos.
3. **NO toco los cinco declarados**, identificados hoy **por sus miembros** y no por su
   numero. Ninguno se funde y los cinco quedan escritos con su motivo en el registro.
4. **NO ejecuto las dos aristas** de los `CONTINUA` del acto 1 ni la poda de sus solapes:
   son de la fase 04 y quedan **declaradas** con id resuelto (`P.9`).
5. **NO resolvio las 1.002 duplicadas** ni el alias durmiente `modelo_spin_2`: son de
   `OP-S-12`.
6. **NO corrigio todos los candidatos del barrido**, solo las celdas adjudicadas como
   tablas vigentes envejecidas. **La vara de separacion va escrita en el instrumento** y es
   de lectura, asi que se puede discutir sitio por sitio.

---

## 11. LAS PREGUNTAS PARA EL AUDITOR

1. **La generalizacion de PARTE A y MIXTO: vale?** (**D2**.) Es la pieza sobre la que se
   apoya todo el resto del tramo. **Afecta a los 25 que quedan.**
2. **La estrella con puntas `D`: se funde eligiendo por contenido entre los viables, o es
   DECLARADO?** (**D3**, pendiente 1.) El propio 2237 dice que se resuelve *en el racimo, no
   par a par*, **y yo lo resolvi par a par.**
3. **Un veredicto `A` que nombra un superviviente no viable: manda la letra o la
   aritmetica?** (Pendiente 2, cinco casos medidos.)
4. **Las 26 contra las 25: cual universo es el bueno?** (**D8**.)
5. **Una tabla que la propia vuelta envejece a media vuelta: se corrige el encabezado, se
   corrige la cifra, o se declara y se encarga?** (**D6**.) **Lo hice del primer modo y es
   la decision que menos precedente tiene.**
