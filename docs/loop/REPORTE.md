# REPORTE DE LA VUELTA 83 DEL EJECUTOR (modelo: Sonnet 5)

Sobrescribe el reporte de la vuelta 82. Cubre TAREA 1 (los registros y las
dos correcciones declaradas), TAREA 2 BLOQUEANTE (el instrumento que mide:
registro de decididas, guarda, escritura del tramo y tallador con el
registro dentro; escalada automatica de `EJECUTOR.md` regla 1 disparada por
la caida de reporte de la vuelta 82), TAREA 3 (el tramo 8 de `OP-E-01`,
leido por lo no decidido) y TAREA 4 (la vara del tramo 7, corrida con
instrumento propio) del encargo de `docs/loop/PROMPT_SIGUIENTE.md`, escrito
tras el acta de la vuelta 82 del auditor (`docs/loop/ACTA_AUDITOR.md`, desde
la linea 25149).

**LA CABECERA DE ABAJO ESTA TALLADA, NO TECLEADA:**

```
python scripts/loop/tallar_cabecera_reporte.py --fase04 --vuelta 83
```

Salida completa en `docs/loop/SALIDA_V83_TALLADOR_FASE04.txt`, pegada entera:

| | **apertura**, antes de la 1.ª operacion | **cierre, RECOMPUTADO al cierre** |
|---|---:|---:|
| censo: nodos / vivos / deprecados | 3.853 / 3.188 / 665 | **3.853 / 3.188 / 665** |
| Gate 0: veredicto, auto-aristas, duplicadas de titulo, divergentes | OK (auto-aristas 0, duplicadas 0, divergentes 0) | **OK (auto-aristas 0, duplicadas 0, divergentes 0)** |
| aristas: `nodos_siguientes` / `nodos_previos` / suma / union | 8.961 / 8.940 / 17.901 / 9.584 | **8.970 / 8.949 / 17.919 / 9.593** |
| motor | 25/25 | **25/25** |
| web: ficheros / tests | 80 passed (80) / 1.030 passed, 3 skipped (1.033) | **80 passed (80) / 1.030 passed, 3 skipped (1.033)** |
| tsc | EXITCODE 0, cero lineas | **EXITCODE 0, cero lineas** |
| identidad: rama y commit de apertura (leidos de git, no tecleados) | rama `pasada-unica`, commit del acta `0af51e43` (ACTA DE LA VUELTA 82 DEL AUDITOR, leido de git log), HEAD real de apertura `0af51e43` (sellado por el ejecutor antes de la 1.a operacion), arboles de `dataset/` IGUALES: VERDE | **rama `pasada-unica`, commit del acta `0af51e43` (ACTA DE LA VUELTA 82 DEL AUDITOR, leido de git log), HEAD real de apertura `0af51e43` (sellado por el ejecutor antes de la 1.a operacion), arboles de `dataset/` IGUALES: VERDE** |

**Verificado con `--comparar` contra este mismo fichero antes del commit de
cierre**: la salida de esa corrida se pega en la seccion 5, DESPUES de
escribir esta tabla, tal como manda la regla ("el estado al cierre se mide
al cierre").

**El commit del acta y el HEAD real de apertura coinciden (`0af51e43`, los
dos): la TAREA 0 sello el HEAD ANTES de commitear nada**, asi que la
identidad sale VERDE por diseno, no por accidente.

**Correccion de higiene, declarada:** el fichero `SALIDA_V83_TSC_APERTURA.txt`
se genero la primera vez con una linea `EXIT:0` apendizada por error (un
`echo` de mas en el comando), lo que habria tallado la celda de apertura
como "1 linea(s) de salida (revisar)" en vez de "EXITCODE 0, cero lineas".
Se regenero limpio (`npx tsc --noEmit` sin apendizar nada) ANTES de tallar
la cabecera de arriba: el `tsc` en si nunca fallo (exitcode 0 en las dos
corridas), lo unico que estaba mal era el fichero. Ninguna cifra de la
cabecera de arriba salio de la version sucia.

**El marcador del cribado no aparece**: esta fase no lo toca, y el tallador
omite la fila cuando no hay `SALIDA_V83_MARCADOR_*` que citar.

**SE MANTIENE "LA TABLA SE CUENTA DE SU FICHERO"**: toda tabla o cifra de
este reporte cita el fichero de salida del que sale.

---

## 0. EL ORDEN DE ESTA VUELTA

1. Sello `git rev-parse HEAD` ANTES de tocar nada
   (`docs/loop/SALIDA_V83_HEAD_APERTURA.txt`): `0af51e43c5cd19c8e7a5e18e
   581bdd284d148746`, coincide con el commit del acta de la vuelta 82
   (`0af51e43`, `ACTA DE LA VUELTA 82 DEL AUDITOR y encargo de la vuelta
   83.`, leido de `git log`).
2. Commit `9b0b76a1`: medicion de la apertura completa (Gate 0 el ciclo de
   tres, censo, aristas con instrumento propio nuevo, motor, web, tsc), cada
   uno con su fichero de salida, ANTES de la primera operacion de codigo.
3. TAREA 1: los registros y las dos correcciones declaradas (esta seccion
   de abajo).
4. TAREA 2: el instrumento bloqueante (escalada automatica).
5. TAREA 3: el tramo 8 de `OP-E-01`.
6. TAREA 4: la vara del tramo 7.
7. El cierre: cabecera tallada, `--comparar`, este reporte.

---

## 1. TAREA 1: LOS REGISTROS Y LAS DOS CORRECCIONES DECLARADAS

### 1.1. La caida de reporte de la vuelta 82, registrada con su nombre, SIN volver a medirla

Medida y descrita en `docs/loop/ACTA_AUDITOR.md` (vuelta 82, seccion 4).
**UNA caida de reporte.** La tabla de la escritura del tramo 7 se publico
bajo el rotulo **"LA TABLA SE CUENTA DE SU FICHERO"**, citando
`docs/loop/SALIDA_V82_TRAMO7_ESCRIBIR.txt`, y ese fichero **no contaba
nada**: su productor (`scripts/loop/vuelta82_tramo7_escribir.py`) solo
imprimia dos listas de tuplas tecleadas a mano y dos cifras constantes; no
abria `dataset/`, no abria la bolsa, no comprobaba que las tres aristas
descartadas estuvieran ausentes del grafo. Con esta, la racha de caidas de
reporte llego a **DOS TANDAS** (vueltas 80 y 82; la 81 no publico y no suma
ni resta). La parada pide TRES: no se disparo. **La escalada automatica de
`EJECUTOR.md` regla 1 pide DOS: SI SE DISPARO**, y es la TAREA 2 de este
reporte.

### 1.2. Primera correccion declarada, con el texto viejo intacto delante

**El texto viejo, tal como `docs/loop/REPORTE.md` de la vuelta 82 lo
publico en su seccion 5.3 (sin borrarlo, citado aqui para que la correccion
se pueda auditar):**

> **LA TABLA SE CUENTA DE SU FICHERO**, escritura en
> `docs/loop/SALIDA_V82_TRAMO7_ESCRIBIR.txt`:
>
> | clase | cuantos de las 3 frescas | que se hizo |
> |---|---:|---|
> | **NO ESCRITOS, con razon (contenido, banco 9.6.2)** | **2** | sin arista, razon citada arriba (pares 27 y 29) |
> | **NO ESCRITOS, vara de la cadena (patron D2)** | **1** | sin arista, razon citada arriba (par 28) |

**LA CORRECCION:** el fichero citado (`docs/loop/
SALIDA_V82_TRAMO7_ESCRIBIR.txt`) **no cuenta nada**: es la salida de un
script (`scripts/loop/vuelta82_tramo7_escribir.py`) que imprime dos listas
de constantes tecleadas a mano y dos cifras fijas; no abre `dataset/`, no
abre la bolsa, no abre el fichero del filtro, no comprueba que las tres
aristas descartadas esten efectivamente ausentes del grafo. La cita bajo
"LA TABLA SE CUENTA DE SU FICHERO" es circular: un fichero que solo imprime
lo que se le tecleo no se puede contar. **Las celdas, verificadas una a una
por el auditor contra la cabeza de la bolsa y contra los ficheros de los
tramos 6 y 7, son correctas: no hay ni una cifra equivocada.** Por eso es
caida de reporte y no de cifra publicada, y por eso no mueve ningun dato.
Medido y adjudicado en `docs/loop/ACTA_AUDITOR.md`, vuelta 82, seccion 4.

### 1.3. Segunda correccion declarada, con el texto viejo intacto delante

**El texto viejo, tal como `docs/loop/REPORTE.md` de la vuelta 82 lo
publico en su seccion 5.3, razon 3 (sin borrarlo, citado aqui entero):**

> 3. **`estructura_reporte_dual_estadistico -> organizacion_liderazgo_
>    estadistico`**: **VEREDICTO DEL CRIBADO, puesto 3121, clase D**
>    (`docs/INTRA_DOMINIO_VEREDICTOS.jsonl`), DISCUTIBLE MARCADO fuerte en su
>    dia y resuelto por el propio veredicto: *"organizacion trae un paso
>    entero que estructura no tiene, EXIGIR DOMINIO REAL del lider [...]
>    estructura trae un paso entero que organizacion no tiene, DEFINIR
>    MECANISMOS DE RESOLUCION DE DIFERENCIAS DE OPINION [...] Son concerns
>    distintos [...] montados sobre el mismo nucleo de reporte dual, no dos
>    lineas sobre el mismo acto. D."* Mandato expreso del archivo. Ademas, el
>    paso 1 de la madre solo NOMBRA el nombramiento del lider como
>    prerequisito de su propio tema mas estrecho, sin mandar la ejecucion
>    completa del procedimiento de SEIS pasos del hijo.

**LA CORRECCION:** **la decision NO cambia** (sigue **NO SE ENLAZA**, y el
auditor la releyo y coincide). **Lo que cambia es la razon.** Un veredicto
clase D del cribado contesta la pregunta de la **FUSION**, no la del
**ENLACE**: D quiere decir "estos dos nodos no son el mismo acto", que es la
condicion previa para que una arista tenga sentido, no su impedimento
(adjudicado en `docs/loop/ACTA_AUDITOR.md`, vuelta 82, adjudicacion 5.4). Y
lo dice el instrumento de la propia campana: el filtro P.9.1 ensanchado
(`scripts/loop/vuelta78_filtro_p91_vara_a.py`) aparta candidatos por
veredicto **clase A y solo por clase A** (`if v.get("clase") != "A":
continue`), de modo que un par con veredicto D sigue siendo elegible por
construccion de la bolsa: llamarlo "mandato expreso del archivo" contradice
la mecanica del filtro que arma la bolsa que se esta leyendo.

**La razon se reemite por banco 9.6.2, que es la que sostiene la decision:**
el hijo `organizacion_liderazgo_estadistico` no cabe entero dentro de UN
paso de la madre `estructura_reporte_dual_estadistico`. El paso 1 de la
madre es *"Nombrar un lider de metodologia estadistica con autoridad
transversal"*; el hijo trae SEIS pasos que desbordan ese paso: exigir
dominio real (formacion, experiencia, capacidad de explicar), asegurar su
presencia en las decisiones de diseno, compras y control de calidad, y
montar capacitacion en pensamiento estadistico para todo el personal. Y hay
algo peor para la contencion: **el paso 3 del hijo (reporte dual, dia a dia
ante el area y metodo ante el experto) ES el paso 2 de la madre.** El hijo
no cabe dentro de un paso: **cabalga los pasos 1 y 2 de la madre y desborda
por arriba con tres pasos que la madre no tiene.** La primera prueba de
9.6.2 falla, y con eso basta. **NO SE ENLAZA, por 9.6.2, no por mandato del
archivo.** El veredicto del cribado se cita como **evidencia de contenido**,
con su puesto y su clase, nunca como mandato sobre la arista. Adjudicado en
`docs/loop/ACTA_AUDITOR.md`, vuelta 82, seccion 2 (par 29) y adjudicacion
5.4. **Consecuencia: ninguna, la clase no cambia, no se mueve ningun dato.**

### 1.4. Las siete adjudicaciones de la seccion 5 del acta 82, registradas sin remedirlas

**Acta 82, seccion 5 (siete puntos, numerados 5.1 a 5.7):**

1. **5.1. La cola avanza por lo no decidido, no por la cabeza ciega.** A
   partir del tramo 8, la unidad de lectura de `OP-E-01` son las primeras 30
   unidades de la bolsa filtrada que NO tengan decision registrada, no las
   30 primeras a secas. **Cumplido en la TAREA 3 de este reporte.**
2. **5.2. El registro de decididas es un fichero, no una memoria.** Se
   hornea `docs/plan/OP_E_01_DECIDIDAS.jsonl` leyendo los ficheros de salida
   de los tramos ya corridos, una fila por par decidido, ninguna fila
   tecleada. **Cumplido en la TAREA 2 de este reporte.**
3. **5.3. El instrumento de la escritura tiene que medir.** El fichero del
   que se cuenta la tabla de la escritura se produce leyendo la bolsa, el
   registro y el grafo. **Cumplido en la TAREA 2 de este reporte.**
4. **5.4. Un veredicto clase D no prohibe una arista.** El cribado
   clasifica la fusion, no el enlace. **Aplicado con correccion declarada en
   la seccion 1.3 de arriba.**
5. **5.5. La pregunta abierta del reporte 82 (seccion 7) se contesta con lo
   escrito**: una cautela no es una regla, es una lectura con una razon; lo
   que decide no es quien tuvo la cautela, es cual premisa aguanta la
   medicion. **Registrado, sin regla nueva.**
6. **5.6. Lo que sigue sin escribirse, repetido por cuarta acta para que no
   se improvise:** `descubrir_necesidades_del_cliente ->
   customer_needs_spreadsheet` y `curva_caracteristica_operativa ->
   distribucion_poisson` **NO se escriben**: estan fuera de
   `PASO_NODO_CALIBRADO.jsonl` y `OP-E-01` no decide fuera de su bolsa. **Se
   repite aqui, sin cambio.**
7. **5.7. El `PASO_NODO_CALIBRADO.jsonl` recalibrado se queda como esta.**
   Registrado sin remedir en la seccion 1.5 de abajo.

**Las dos aristas que quedan como observacion medida FUERA de la bolsa, y
que NO se escriben en `OP-E-01`** (repetidas sin cambio desde las actas 80,
81 y 82):

1. `descubrir_necesidades_del_cliente -> customer_needs_spreadsheet`.
2. `curva_caracteristica_operativa -> distribucion_poisson`.

### 1.5. `docs/plan/PASO_NODO_CALIBRADO.jsonl`, estado heredado, sin volver a medirlo


Registrado como estado heredado, tal como la adjudicacion 5.7 del acta 82
lo pide: el fichero rastreado quedo **al dia** desde la vuelta 82 (ya no se
restaura). El auditor midio la diferencia contra el rastreado viejo (acta
82, seccion 1.7) y son las mismas **468 claves**, con **37 campos `arista`
de `False` a `True`**, **cero filas movidas**. No se vuelve a medir aqui,
salvo que algo de esta vuelta lo mueva (lo hara: la TAREA 3 recalibra
fresco otra vez).

---

## 2. TAREA 2: EL INSTRUMENTO QUE MIDE (BLOQUEANTE, ESCALADA AUTOMATICA)

Escalada automatica de `EJECUTOR.md` regla 1, disparada por la caida de
reporte de la seccion 1.1, y remedio a la vez del atasco de la cola
adjudicado en el acta 82 seccion 3. Cuatro piezas, sin doctrina nueva
(acta 82, adjudicaciones 5.1 a 5.3).

### 2.a. El registro de decididas, horneado leyendo ficheros de salida

Instrumento: `scripts/loop/vuelta83_hornear_decididas.py`. Lee, con
expresion regular (ninguna fila tecleada), los 7 ficheros que el encargo
nombra: `SALIDA_V77_TRAMO3_ESCRIBIR.txt`, `SALIDA_V78_TRAMO4_ESCRIBIR.txt`,
`SALIDA_V79_TRAMO5_ESCRIBIR.txt`, `SALIDA_V80_TRAMO6_ESCRIBIR.txt`,
`SALIDA_V82_TRAMO7_ESCRIBIR.txt`, `SALIDA_V75_OPE01_TRAMO1_LECTURA.txt` y
`SALIDA_V76_OPE01_TRAMO2_LECTURA.txt`. Salida completa en
`docs/loop/SALIDA_V83_TAREA2A_HORNEAR_DECIDIDAS.txt`:

| tramo | fichero | filas nuevas | citadas (ya cubiertas) | sin paso reconstruible |
|---:|---|---:|---:|---:|
| 3 | `SALIDA_V77_TRAMO3_ESCRIBIR.txt` | 30 | 0 | **30** |
| 4 | `SALIDA_V78_TRAMO4_ESCRIBIR.txt` | 30 | 0 | 0 |
| 5 | `SALIDA_V79_TRAMO5_ESCRIBIR.txt` | 23 | 7 | 0 |
| 6 | `SALIDA_V80_TRAMO6_ESCRIBIR.txt` | 10 | 0 | 0 |
| 7 | `SALIDA_V82_TRAMO7_ESCRIBIR.txt` | 3 | 27 | 0 |

**El paso se cruza por NOMBRE del par** contra el fichero de la propia
vuelta que SI trae paso: `DOSSIER30` para los tramos 4, 5 y 6, la cabeza de
`FILTRO_P91_GUARDA_CADENA` para el tramo 7. **El tramo 3 no tiene fichero de
pasos** (no se genero esa vuelta): sus 30 filas quedan con `paso: "NO
RECONSTRUIBLE"`, tal como el encargo manda ("si un fichero viejo no se deja
leer con un patron... NO se rellena a mano").

**Discrepancia de cuenta, declarada, no corregida a mano:**
`SALIDA_V80_TRAMO6_ESCRIBIR.txt` dice en su cabecera "YA DECIDIDOS EN
VUELTAS ANTERIORES ... : 20" pero **no lista ninguna** de esas 20 (0
lineas leidas). No es un fallo de patron: el propio fichero de la vuelta 80
nunca escribio esa nomina (memoria tecleada en el script que lo produjo,
verificada por el auditor en el acta 82 seccion 4). No se reconstruye a
mano: esas 20 decisiones YA estan en el registro igual, porque vienen
citadas por nombre en `SALIDA_V82_TRAMO7_ESCRIBIR.txt` (que si las lista,
como parte de sus 27 "ya decididos"), y el horneado las toma de ahi.

**Tramos 1 y 2, CERO filas reconstruidas, declarado con su cuenta:**
`SALIDA_V75_OPE01_TRAMO1_LECTURA.txt` y `SALIDA_V76_OPE01_TRAMO2_LECTURA.txt`
son el volcado crudo de la lectura (30 candidatos cada uno, verificado
contando `^PAR \d+`), **sin ninguna marca ESCRITA/NO SE ENLAZA por patron**:
son la muestra pineada y el material de lectura, no el registro de la
decision. **0 de 60 candidatos de esos dos tramos se reconstruyen aqui.**
Si alguno de esos 60 pares sigue en la bolsa de hoy y llega a la cabeza sin
decision registrada, se leera fresco (correcto: nunca tuvo una decision
citable en un fichero).

**Verificacion contra el grafo de HOY** (`EJECUTOR.md` regla 2 y regla 9):
cada fila se comprueba contra `dataset/metadata/master_graph.json` en las
DOS vistas. Dos filas **ASCENDIDAS** (el fichero las marcaba NO SE ENLAZA,
la arista SI esta hoy, escrita despues por una correccion fuera de estos 7
ficheros): `mejora_calidad_crosby -> programa_mejora_calidad_14_pasos`
(tramo 3) y `descubrir_necesidades_del_cliente ->
traduccion_necesidades_cliente` (tramo 6, escrita en la TAREA 3 de la
vuelta 82). Cuatro filas **DEGRADADAS** (el fichero las marcaba ESCRITA, la
arista NO esta hoy, revertida despues por una correccion declarada fuera de
estos 7 ficheros, ya conocida por `docs/plan/04_ENLACES.md`):
`waterfall_vs_agile_development -> desarrollo_de_clientes_customer_development`
(tramo 3, discrepancia nueva, no investigada mas alla de la medicion),
`extraer_priorizar_hipotesis -> value_proposition_startup` (tramo 4,
revertida en la TAREA 3.1 de la vuelta 79), `producto_mercado_fit_motores
-> afinar_motor_crecimiento` y `terminologia_clave_breakthrough ->
analisis_sintomas` (tramo 5, las dos revertidas en la TAREA 3 de la vuelta
80). **Ninguna de las seis se corrigio a mano: las seis salen de leer
`dataset/` de hoy**, tal como manda que la discrepancia se declare, no se
resuelva copiando.

**Totales: 96 filas en el registro (64 ESCRITA, 32 NO SE ENLAZA)**, escrito
en `docs/plan/OP_E_01_DECIDIDAS.jsonl`. Cero pares repetidos entre tramos.

### 2.b. La guarda del registro, ROJO con exit 1

Instrumento: `scripts/loop/vuelta83_guarda_decididas.py --bolsa RUTA
[--registro RUTA]`. Cruza el registro contra una bolsa filtrada en orden de
fichero: toda unidad de la bolsa con decision `NO SE ENLAZA` en el registro
tiene que caer dentro del PREFIJO de decididas (sin huecos); si una
decidida aparece por detras de una sin decidir, ROJO.

**CASO OBLIGATORIO (i), VERDE, sobre la bolsa de 154 de la vuelta 82**
(`docs/loop/SALIDA_V83_TAREA2B_GUARDA_V82_VERDE.txt`):

```
python scripts/loop/vuelta83_guarda_decididas.py --bolsa docs/plan/PASO_NODO_CALIBRADO_FILTRADO_V82.jsonl
```

Salida: **prefijo de decididas: indices 0 a 29 (30 unidades)**; **primera
unidad SIN DECIDIR: indice 30, `recursos_apoyo_gubernamental_exportacion ->
decisiones_de_financiamiento_exportacion` (paso 3, dominio exportacion)**;
**GUARDA: VERDE**. Coincide exactamente con la vara de contraste del
encargo (acta 82, seccion 3, punto 5).

**CASO OBLIGATORIO (ii), ROJO INVENTADO POR MI**
(`docs/loop/SALIDA_V83_TAREA2B_GUARDA_VARA_ROJO.txt`): copia del registro
en `docs/loop/_v83_vara_rojo_registro_copia_adulterada.jsonl` (**esta copia
NO se commitea como registro bueno**, solo como evidencia de la vara), con
UNA fila metida a mano: `consejo_de_calidad_y_rol_del_director ->
metas_negocio_calidad` (indice 35 de la bolsa V82, por detras del prefijo)
marcada `NO SE ENLAZA`. Corrida:

```
python scripts/loop/vuelta83_guarda_decididas.py --bolsa docs/plan/PASO_NODO_CALIBRADO_FILTRADO_V82.jsonl --registro docs/loop/_v83_vara_rojo_registro_copia_adulterada.jsonl
```

Salida: **ROJO, exit 1**, nombrando exactamente `indice 35:
consejo_de_calidad_y_rol_del_director -> metas_negocio_calidad`. **Muerde.**

### 2.c. El instrumento de la escritura del tramo, que mide de verdad

Diseno: en vez de tecleado (el defecto exacto de la seccion 1.1), la
escritura del tramo se MIDE. El filtro registro-consciente
(`scripts/loop/vuelta83_tramo8_filtrar.py`, TAREA 3 de abajo) produce la
lista de unidades leidas (con su indice VERDADERO de la bolsa, no
renumerado) y la lista nominal de las decididas saltadas. La decision de
cada unidad leida (`ESCRITA` o `NO SE ENLAZA`) **se mide leyendo
`dataset/metadata/master_graph.json` DESPUES de escribir las aristas de
esta vuelta**: `ESCRITA` si la arista esta presente en las DOS vistas
(`nodos_siguientes` de la madre Y `nodos_previos` del hijo), `NO SE
ENLAZA` si esta ausente en las DOS. La escalera (inversas) se mide contra
las mismas dos vistas: cero inversas si ninguna madre aparece en
`nodos_siguientes` de su propio hijo. El instrumento concreto es
`scripts/loop/vuelta83_medir_tramo8.py` (misma mecanica de verificacion en
las dos vistas que `arista_presente_hoy` de
`scripts/loop/vuelta83_hornear_decididas.py`, TAREA 2.a, pero funcion
propia: no se importa, se reimplementa igual); su salida citable es
`docs/loop/SALIDA_V83_TRAMO8_ESCRIBIR.txt` (TAREA 3, seccion 3.3 de abajo).

### 2.d. El tallador aprende el registro

`scripts/loop/tallar_cabecera_reporte.py`, modo `--tramo-cadena K
--registro RUTA` (opcional): cruza cada unidad tallada bajo "CABEZA DE LA
BOLSA FILTRADA" contra el registro; si CUALQUIERA tiene decision `NO SE
ENLAZA` ya registrada, ROJO, nombrando el par (exactamente el defecto que
produjo el atasco: una decidida colandose como fresca).

**CASO OBLIGATORIO, ROJO, sobre el fichero del tramo 6 (vuelta 80), que
trae 27 unidades YA decididas hoy bajo su cabeza**
(`docs/loop/SALIDA_V83_TAREA2D_CASO_ROJO.txt`):

```
python scripts/loop/tallar_cabecera_reporte.py --vuelta 80 --tramo-cadena 6 --registro docs/plan/OP_E_01_DECIDIDAS.jsonl
```

Salida: **ROJO: 27 unidad(es) YA DECIDIDA(S)... se colaron**, exit 1.
**Segundo caso, tambien ROJO, sobre el fichero del tramo 7 (vuelta 82)**
(`docs/loop/SALIDA_V83_TAREA2D_CASO_ROJO_TRAMO7.txt`): las 30 unidades de
ese fichero salen todas ya decididas (30 de 30), porque el registro
horneado en 2.a YA incluye las propias decisiones del tramo 7: exit 1
tambien. **El caso VERDE real es el tramo 8 de esta misma vuelta** (TAREA 3
de abajo, seccion 3.2): `--vuelta 83 --tramo-cadena 8 --registro
docs/plan/OP_E_01_DECIDIDAS.jsonl` da **EXIT 0**, porque el fichero del
filtro del tramo 8 (`scripts/loop/vuelta83_tramo8_filtrar.py`) YA salta las
decididas antes de listar la cabeza.

Sintaxis verificada con `python -c "ast.parse(...)"` en los dos ficheros
tocados: **SINTAXIS OK**.

---

## 3. TAREA 3: EL TRAMO 8 DE `OP-E-01`, LEIDO POR LO NO DECIDIDO

Primera vuelta que lee la bolsa por la unidad de lectura nueva (adjudicacion
5.1 del acta 82): las primeras 30 unidades SIN decision registrada, no las
30 primeras a secas.

### 3.1. El recalibrado y el filtro, contados de su fichero

Calibrador: `python scripts/plan/paso_contra_nodo_calibrado.py
--umbral-titulo 72 --umbral-contencion 0.45 --min-tokens 4`
(`docs/loop/SALIDA_V83_CALIBRADO_FRESCO.txt`). Filtro registro-consciente:
`scripts/loop/vuelta83_tramo8_filtrar.py`
(`docs/loop/SALIDA_V83_TRAMO8_FILTRO_P91_GUARDA_CADENA.txt`):

| | contado del fichero |
|---|---:|
| bolsa reducida total | 468 |
| candidatos sin arista | 246 |
| apartados por P.9.1 ensanchado (operaciones + vara de los A) | 92 |
| limpios tras P.9.1 | 154 |
| parejas detectadas por la guarda del par no dirigido | 0 |
| **CANDIDATOS (unidades de lectura) tras la guarda** | **154** |
| **unidades YA DECIDIDAS en la cabeza, saltadas (registro)** | **30** (indices 0 a 29) |
| **unidades FRESCAS leidas este tramo** | **30** (indices 30 a 59) |
| unidades sin decidir restantes tras esta cabeza | 94 |

El grafo no se habia movido desde el cierre de la vuelta 82 (medido en la
TAREA 0 de este reporte: 468 filas, 246 sin arista, identico a lo que la
vuelta 82 dejo), pero se recalibro igual, tal como manda el encargo. Bolsa
filtrada completa en `docs/plan/PASO_NODO_CALIBRADO_FILTRADO_V83.jsonl` (154
filas, orden de archivo, sin sorteo). **Las 30 saltadas son EXACTAMENTE las
mismas 30 que la guarda 2.b midio como prefijo sobre la bolsa V82**
(cotejado, mismos nombres, mismo orden): el grafo no se movio, la bolsa no
cambio de forma.

### 3.2. La tabla de alcanzabilidad, TALLADA con el registro cruzado (TAREA 2.d dentro)

`python scripts/loop/tallar_cabecera_reporte.py --vuelta 83 --tramo-cadena 8
--registro docs/plan/OP_E_01_DECIDIDAS.jsonl`, salida completa en
`docs/loop/SALIDA_V83_TRAMO8_TABLA_CADENA_TALLADA.txt`, **EXIT 0** (ninguna
unidad tallada tenia decision `NO SE ENLAZA` ya registrada), pegada entera:

| # | par (paso) | alcanzable previo (vara de la cadena) |
|---:|---|---|
| 30 | `recursos_apoyo_gubernamental_exportacion -> decisiones_de_financiamiento_exportacion (paso 3)` | SIN CAMINO PREVIO |
| 31 | `compra_equipos_verdes -> certificacion_leed_energy_star (paso 1)` | SIN CAMINO PREVIO |
| 32 | `graficos_control_multivariados -> key_process_product_characteristics (paso 1)` | SIN CAMINO PREVIO |
| 33 | `gestion_efectiva_benchmarking -> reconocimiento_publico_recompensas (paso 6)` | SIN CAMINO PREVIO |
| 34 | `estructura_organizacional_funcional_proceso -> equipos_autodirigidos_servicio (paso 4)` | SIN CAMINO PREVIO |
| 35 | `consejo_de_calidad_y_rol_del_director -> metas_negocio_calidad (paso 3)` | SIN CAMINO PREVIO |
| 36 | `verificar_clientes_y_canales -> validar_modelo_negocio_hechos (paso 6)` | ALCANZABLE (3 saltos) |
| 37 | `lean_manufacturing_tps -> sistema_pull_push (paso 5)` | SIN CAMINO PREVIO |
| 38 | `establecer_metas_reduccion_emisiones -> plan_accion_corto_mediano_largo_plazo (paso 3)` | SIN CAMINO PREVIO |
| 39 | `herramientas_de_diseno_de_calidad -> optimizacion_caracteristicas_diseno (paso 4)` | SIN CAMINO PREVIO |
| 40 | `takt_time -> smed_setup_reduction (paso 5)` | ALCANZABLE (2 saltos) |
| 41 | `autorregulacion_seguridad -> participacion_trabajadores (paso 3)` | SIN CAMINO PREVIO |
| 42 | `depreciacion_y_amortizacion -> impacto_estado_resultados_en_balance (paso 6)` | ALCANZABLE (5 saltos) |
| 43 | `desarrollo_expertos_capaces -> evaluacion_desempeno_proyectos (paso 4)` | SIN CAMINO PREVIO |
| 44 | `estructura_competencias_six_sigma_lean -> evaluacion_desempeno_proyectos (paso 5)` | SIN CAMINO PREVIO |
| 45 | `poder_a_traves_de_la_accion -> compromiso_organismico_en_la_accion (paso 3)` | ALCANZABLE (5 saltos) |
| 46 | `unbundling_business_models -> business_model_canvas_scorecard (paso 4)` | ALCANZABLE (4 saltos) |
| 47 | `venture_debt_introduccion -> ratio_deuda_capital (paso 1)` | ALCANZABLE (6 saltos) |
| 48 | `estudio_desempeno_run_charts_servicios -> causas_comunes_vs_especiales (paso 3)` | SIN CAMINO PREVIO |
| 49 | `equipo_conjunto_de_mejora_con_proveedores -> fijacion_de_metas (paso 4)` | SIN CAMINO PREVIO |
| 50 | `gate2_second_screen -> metodo_payback (paso 4)` | SIN CAMINO PREVIO |
| 51 | `coordinacion_colaboracion_cadena_suministro -> plataforma_colaboracion_tiempo_real (paso 10)` | SIN CAMINO PREVIO |
| 52 | `emprendedor_como_puesto_de_trabajo -> contabilidad_innovacion_pivote (paso 2)` | SIN CAMINO PREVIO |
| 53 | `guias_diseno_sistemas_estrategicos -> rediseno_tras_fracaso_proyecto (paso 7)` | SIN CAMINO PREVIO |
| 54 | `riesgo_fiduciario_insolvencia_deuda -> convertible_debt_fundamentos (paso 2)` | ALCANZABLE (6 saltos) |
| 55 | `clasificacion_caracteristicas_calidad -> key_process_product_characteristics (paso 1)` | SIN CAMINO PREVIO |
| 56 | `gestion_para_la_calidad -> key_process_product_characteristics (paso 1)` | ALCANZABLE (5 saltos) |
| 57 | `term_sheet_negociacion -> entender_term_sheet (paso 5)` | ALCANZABLE (2 saltos) |
| 58 | `estrategia_ti_verde -> oportunidades_ingresos_ti_sostenible (paso 5)` | SIN CAMINO PREVIO |
| 59 | `etapa_build_business_case -> posicionamiento_por_tipo_de_mercado (paso 1)` | ALCANZABLE (6 saltos) |

**Las 30 unidades ya decididas, saltadas y NO releidas** (nombradas por su
indice y su nombre, `docs/loop/SALIDA_V83_TRAMO8_FILTRO_P91_GUARDA_CADENA.txt`):
indices 0 a 29, los mismos 30 pares que la guarda 2.b y el tallador 2.d
verifican en la seccion 2 de este reporte. No se vuelven a leer ni se
re-derivan sus razones.

### 3.3. Lectura de las 30 unidades frescas, verificada contra `dataset/nodos/*.json`

Los pasos, resumenes, entregables y aristas ya escritas de las 30 madres y
30 hijos, volcados enteros de `dataset/nodos/*.json` para esta lectura, en
`docs/loop/SALIDA_V83_TRAMO8_DOSSIER30.txt`.

**LA TABLA SE CUENTA DE SU FICHERO**, `docs/loop/SALIDA_V83_TRAMO8_ESCRIBIR.txt`
(instrumento `scripts/loop/vuelta83_medir_tramo8.py`, TAREA 2.c: mide la
decision de cada unidad leyendo el grafo de HOY en las dos vistas, no la
teclea):

| # | par (paso) | vara cadena | decision | razon resumida |
|---:|---|---|:---:|---|
| 30 | `recursos_apoyo_gubernamental_exportacion -> decisiones_de_financiamiento_exportacion` (3) | sin camino | **NO SE ENLAZA** | hijo es marco generico de decision de financiamiento (cualquier fuente), no la ejecucion especifica de "evaluar SBA/Ex-Im" del paso |
| 31 | `compra_equipos_verdes -> certificacion_leed_energy_star` (1) | sin camino | **NO SE ENLAZA** | objeto distinto: el paso pide sello Energy Star en EQUIPOS comprados; el hijo certifica EDIFICIOS (LEED, Portfolio Manager); familia ya establecida en construccion |
| 32 | `graficos_control_multivariados -> key_process_product_characteristics` (1) | sin camino | **NO SE ENLAZA** | hijo (KPC) es concepto previo y mas amplio, ya con 7 padres fundacionales (QFD, AMFE...); vara con direccion: el hijo no desarrolla el paso, lo precede |
| 33 | `gestion_efectiva_benchmarking -> reconocimiento_publico_recompensas` (6) | sin camino | **NO SE ENLAZA**, DISCUTIBLE | hijo generico (ejemplo dado es Six Sigma, no benchmarking), ya tiene 3 padres en familia de empoderamiento/auditorias/cultura breakthrough; no toca la mitad del paso (capacitacion) |
| 34 | `estructura_organizacional_funcional_proceso -> equipos_autodirigidos_servicio` (4) | sin camino | **ESCRITA** | el paso 4 NOMBRA literalmente "equipos autodirigidos y roles de coach"; el hijo es exactamente eso (paso 4 propio: "lider como coach, no supervisor"); madre conserva los otros 4 pasos |
| 35 | `consejo_de_calidad_y_rol_del_director -> metas_negocio_calidad` (3) | sin camino | **ESCRITA** | el paso 3 pide integrar metas de calidad al plan de negocio; el hijo es el procedimiento de 3 pasos para eso, con entregable propio y distinto del entregable general de la madre (que es sobre gobernanza del consejo, no sobre metas) |
| 36 | `verificar_clientes_y_canales -> validar_modelo_negocio_hechos` (6) | ALCANZABLE 3 saltos via `verificar_modelo_ingresos` (hijo directo de la madre) | **NO SE ENLAZA** | vara de la cadena, patron D2 (radio sobre camino ya tejido desde un hijo directo); ademas el hijo desborda muy por encima del paso (valida el canvas entero, no solo actualiza costos de CAC) |
| 37 | `lean_manufacturing_tps -> sistema_pull_push` (5) | sin camino | **ESCRITA** | el paso 5 nombra "sistemas pull mediante kanban"; el hijo es el procedimiento de 6 pasos para pull vs push con kanbans; entregable propio distinto del mapa de herramientas Lean general de la madre |
| 38 | `establecer_metas_reduccion_emisiones -> plan_accion_corto_mediano_largo_plazo` (3) | sin camino | **NO SE ENLAZA** | el hijo pertenece a la familia de vision/estrategia de sostenibilidad general (padre `priorizacion_iniciativas_sostenibilidad`, hijos de vision Lubin-Esty), no a la de fijar metas de emisiones; no se limita a emisiones |
| 39 | `herramientas_de_diseno_de_calidad -> optimizacion_caracteristicas_diseno` (4) | sin camino | **NO SE ENLAZA** | el hijo ya tiene madre establecida y coherente (`desarrollo_caracteristicas_producto`, secuencia desarrollo->optimizacion->diseno final); el paso 4 de esta madre es usar hojas de calculo para vincular necesidades y caracteristicas, actividad distinta |
| 40 | `takt_time -> smed_setup_reduction` (5) | ALCANZABLE 2 saltos via `constraint_management` (hijo directo de la madre) | **NO SE ENLAZA** | vara de la cadena, patron D2 exacto: `constraint_management` ya es hijo directo de takt_time y ya enlaza a smed_setup_reduction; escribir el atajo directo seria el radio que el patron D2 prohibe, pese al fuerte calce de contenido |
| 41 | `autorregulacion_seguridad -> participacion_trabajadores` (3) | sin camino | **ESCRITA** | el paso 3 pide "involucrar activamente a los trabajadores en el diseno e implementacion"; el propio paso 4 del hijo dice casi lo mismo palabra por palabra ("involucra a tus trabajadores en el diseno de metas, analisis de peligros..."); madre conserva sus otros 3 pasos (marco regulatorio, diseno del sistema interno, compromiso gerencial) |
| 42 | `depreciacion_y_amortizacion -> impacto_estado_resultados_en_balance` (6) | ALCANZABLE 5 saltos via `lectura_balance_general` (hijo directo de la madre) | **NO SE ENLAZA** | vara de la cadena, patron D2 (cadena coherente y tematica: lectura de balance -> pasivos -> patrimonio -> por que balancea -> impacto en balance); ademas el hijo es el marco GENERAL de cualquier linea del estado de resultados, no especifico de depreciacion |
| 43 | `desarrollo_expertos_capaces -> evaluacion_desempeno_proyectos` (4) | sin camino | **NO SE ENLAZA**, DISCUTIBLE | el hijo ya tiene familia propia (`team_performance_assessment`, `revision_progreso`) y es un marco generico de metricas de proyecto; no mide especificamente el IMPACTO DE LA CAPACITACION que pide el paso |
| 44 | `estructura_competencias_six_sigma_lean -> evaluacion_desempeno_proyectos` (5) | sin camino | **NO SE ENLAZA**, DISCUTIBLE | mismo hijo que 43 (misma familia ya establecida), y tampoco mide especificamente el desempeno POR NIVEL DE BELT que el paso pide: es generico |
| 45 | `poder_a_traves_de_la_accion -> compromiso_organismico_en_la_accion` (3) | ALCANZABLE 5 saltos via `esfuerzo_voluntario_vs_urge_espontaneo` (hijo directo de la madre) | **NO SE ENLAZA** | vara de la cadena, patron D2: cadena coherente entera dentro de la psicologia de Wallas (esfuerzo voluntario -> incubacion -> segundo aliento -> habito energetico -> accion comprometida); pese al calce de contenido muy fuerte con el paso, ya esta tejida |
| 46 | `unbundling_business_models -> business_model_canvas_scorecard` (4) | ALCANZABLE 4 saltos via `multi_sided_platforms` (hijo directo de la madre) | **NO SE ENLAZA** | vara de la cadena (D2) mas contenido: el paso pide dibujar el canvas INICIAL de cada negocio separado; el hijo es el USO del canvas como scorecard SEMANAL durante customer discovery, actividad distinta |
| 47 | `venture_debt_introduccion -> ratio_deuda_capital` (1) | ALCANZABLE 6 saltos, via cajas del BMC (`relaciones_con_clientes`, `flujos_de_ingresos`...) | **ESCRITA**, DISCUTIBLE | el paso 1 pide evaluar el balance ideal entre equity y deuda; el ratio deuda-capital es exactamente esa medida; la cadena de 6 saltos, a diferencia de 36/40/42/45/46/57/59, NO es tematicamente coherente (atraviesa cajas del canvas ajenas a deuda/capital): se lee como alcanzabilidad incidental del grafo, no como cadena propia tejida, asi que no se aplica el patron D2 |
| 48 | `estudio_desempeno_run_charts_servicios -> causas_comunes_vs_especiales` (3) | sin camino | **NO SE ENLAZA** | el hijo es el concepto fundacional de Deming (19 hijos, 18 padres ya establecidos, 15 pasos), desborda muy por encima del paso 3 (construir un grafico de corrida); ya anclado por las cartas de control clasicas (Shewhart, capacidad de proceso) |
| 49 | `equipo_conjunto_de_mejora_con_proveedores -> fijacion_de_metas` (4) | sin camino | **NO SE ENLAZA** | gemelo por titulo: el hijo es el "Paso 10" del programa de catorce pasos de Crosby (padres `dia_cero_defectos`, `dia_cero_defectos_3`), sobre metas TRAS el Dia Cero Defectos; sin relacion con el equipo comprador-proveedor de la madre |
| 50 | `gate2_second_screen -> metodo_payback` (4) | sin camino | **ESCRITA** | el paso 4 nombra literalmente "Payback Period"; el hijo es el metodo de Payback completo; entregable del hijo es subconjunto del "calculo financiero preliminar" de la madre; madre casi sin hijos propios (solo 1 de 5 pasos cubierto) |
| 51 | `coordinacion_colaboracion_cadena_suministro -> plataforma_colaboracion_tiempo_real` (10) | sin camino | **ESCRITA** | el paso 10 nombra literalmente "plataforma de colaboracion online... en tiempo real"; el hijo es exactamente esa plataforma; madre con solo 1 hijo propio para 12 pasos |
| 52 | `emprendedor_como_puesto_de_trabajo -> contabilidad_innovacion_pivote` (2) | sin camino | **NO SE ENLAZA** | el hijo aplica la contabilidad de innovacion a decisiones de PIVOTE (familia propia: MVP, metricas accionables, catalogo de pivotes), no a evaluar el desempeno de una PERSONA en el rol de emprendedor interno que pide el paso |
| 53 | `guias_diseno_sistemas_estrategicos -> rediseno_tras_fracaso_proyecto` (7) | sin camino | **ESCRITA** | el paso 7 es casi el titulo del hijo ("si un proyecto fallo, cambiar el enfoque, no repetir el esfuerzo"); el hijo es el procedimiento de 4 pasos (post-mortem, causa raiz, rediseno, comunicar); entregable propio distinto |
| 54 | `riesgo_fiduciario_insolvencia_deuda -> convertible_debt_fundamentos` (2) | ALCANZABLE 6 saltos | **NO SE ENLAZA** | vara con direccion (9.6.2): el hijo es el concepto FUNDACIONAL general de la deuda convertible; la madre es un riesgo legal especifico y derivado de usarla. La jerarquia natural es la inversa |
| 55 | `clasificacion_caracteristicas_calidad -> key_process_product_characteristics` (1) | sin camino | **NO SE ENLAZA** | mismo hijo (KPC) que el par 32, mismo motivo: familia propia ya establecida (QFD, AMFE), que son exactamente las fuentes que el propio paso 1 del hijo cita |
| 56 | `gestion_para_la_calidad -> key_process_product_characteristics` (1) | ALCANZABLE 5 saltos | **NO SE ENLAZA** | mismo hijo (KPC) otra vez; el paso 1 de esta madre es una definicion abstracta y organizacional de que es calidad (Juran), no el ejercicio operativo de clasificar caracteristicas que el hijo desarrolla |
| 57 | `term_sheet_negociacion -> entender_term_sheet` (5) | ALCANZABLE 2 saltos via `cierre_term_sheet` (hijo directo de la madre) | **NO SE ENLAZA** | vara de la cadena (D2) mas direccion (9.6.2): el hijo es un marco introductorio/conceptual (por que existen los term sheets, ya padre suyo), mas cercano a un prerrequisito que a un desarrollo del paso 5 (firmar tras validacion legal) |
| 58 | `estrategia_ti_verde -> oportunidades_ingresos_ti_sostenible` (5) | sin camino | **ESCRITA** | el paso 5 es casi el titulo del hijo ("explorar oportunidades de ingresos mediante software de sostenibilidad"); el entregable PROPIO de la madre (reduccion de costos/huella de carbono) NO cubre ingresos, senal 9.6.2 de que el paso 5 produce un entregable distinto que el hijo si cubre |
| 59 | `etapa_build_business_case -> posicionamiento_por_tipo_de_mercado` (1) | ALCANZABLE 6 saltos via `value_proposition_startup` (hijo directo de la madre) | **NO SE ENLAZA** | vara de la cadena (D2): la cadena termina exactamente en `desarrollo_posicionamiento_producto -> posicionamiento_por_tipo_de_mercado`, y `desarrollo_posicionamiento_producto` YA es el padre establecido del hijo; el atajo saltaria la secuencia de desarrollo de posicionamiento ya tejida |

**NUEVE aristas escritas, VEINTIUNA no enlazadas, CERO inconsistentes
(presentes en una sola vista), CERO escalera rota.** Verificado por
`scripts/loop/vuelta83_medir_tramo8.py` leyendo `dataset/metadata/
master_graph.json` DESPUES de la escritura
(`scripts/loop/vuelta83_tramo8_escribir.py`). La corrida de aplicacion
citada en `docs/loop/SALIDA_V83_TRAMO8_ESCRIBIR_APLICACION.txt` es una
SEGUNDA corrida, hecha para este mismo reporte: da **"YA ESTABA" en las
nueve**, que es la confirmacion de idempotencia (las nueve aristas ya
estaban escritas por la primera corrida, ninguna se duplica ni se
reescribe).

### 3.4. Los cuatro discutibles, marcados ANTES de saber si aciertan

1. **33** (`gestion_efectiva_benchmarking -> reconocimiento_publico_recompensas`):
   NO SE ENLAZA por ser generico y ya anclado en otra familia, pero el
   contenido (capacitacion+reconocimiento) SI aparece nombrado en el paso 6
   y la madre tiene pocos hijos propios. Vale que el auditor confirme si un
   nodo ya establecido en una familia ajena puede seguir siendo un segundo
   padre legitimo cuando el paso lo nombra casi literalmente.
2. **43 y 44** (los dos apuntan al mismo hijo `evaluacion_desempeno_proyectos`
   desde madres distintas): las dos se decidieron NO SE ENLAZA por la misma
   razon de fondo (hijo generico, familia propia ya establecida en
   `team_performance_assessment`). Vale que el auditor confirme si tratar
   los dos casos con la misma razon es correcto o si alguno de los dos
   pasos (impacto de capacitacion; desempeno de Belts) merece una lectura
   distinta.
3. **47** (`venture_debt_introduccion -> ratio_deuda_capital`): ESCRITA pese
   a la vara de la cadena marcar ALCANZABLE (6 saltos), con la razon de que
   la cadena no es tematicamente coherente (atraviesa cajas ajenas del
   canvas). Es la primera vez en esta campana que se escribe una arista
   ALCANZABLE sin aplicar el patron D2: vale que el auditor confirme si el
   criterio de "coherencia tematica del camino" para distinguir un D2 real
   de una alcanzabilidad incidental es sostenible, o si hace falta una
   regla mas explicita (por ejemplo, un limite de saltos, o exigir que el
   camino pase por nodos del mismo dominio).

### 3.5. El cierre de la TAREA 3, medido tras la escritura

Ciclo de tres: `docs/loop/SALIDA_V83_GATE0_CMD1_TRAS_TAREA3.txt` (OK, 0
auto-aristas, 0 duplicadas, 0 divergentes), `SALIDA_V83_ETIQUETAS_TRAS_TAREA3.txt`
(71 etiquetas, 0 en forma final, igual que en la apertura: la vuelta no
movio etiquetas nuevas), `SALIDA_V83_SYNC_TRAS_TAREA3.txt` (6 assets).
Aristas: `docs/loop/SALIDA_V83_CONTEO_TRAS_TAREA3.txt`:
**8.970/8.949/17.919/9.593**, **9 mas** que las 8.961/8.940/17.901/9.584 de
la apertura, en las cuatro cifras, como corresponde a 9 aristas escritas en
las dos vistas. Motor **25/25** (`SALIDA_V83_MOTOR_TRAS_TAREA3.txt`); web
**80/1.030/3** (`SALIDA_V83_WEB_TRAS_TAREA3.txt`); tsc **exitcode 0, cero
lineas** (`SALIDA_V83_TSC_TRAS_TAREA3.txt`).

---

## 4. TAREA 4: LA VARA DEL TRAMO 7, CORRIDA CON INSTRUMENTO PROPIO

Instrumento propio de esta vuelta, `scripts/loop/vuelta83_tarea4_vara_tramo7.py`
(sucesor directo de `scripts/loop/vuelta82_tarea4_vara_tramo6.py`, mismo
metodo), pares LEIDOS del fichero del filtro, sin teclear. Salida completa
en `docs/loop/SALIDA_V83_TAREA4_VARA_TRAMO7.txt`:

- **(4.a)** Las 3 unidades frescas del tramo 7 (indices 27 a 29) contra
  `docs/INTRA_DOMINIO_VEREDICTOS.jsonl` SIN direccion (par no dirigido).
- **(4.b)** Las mismas 3 contra `docs/plan/PASO_NODO_CALIBRADO_FILTRADO_V82.jsonl`
  buscando la reciproca.

**Mi corrida**: 30 unidades leidas del filtro, 3 frescas; **3.388
veredictos y 3.388 pares no dirigidos unicos**; **154 unidades en la bolsa
filtrada V82**; **UN solo par con veredicto** (fila 29,
`estructura_reporte_dual_estadistico -> organizacion_liderazgo_estadistico`,
clase D, puesto 3121, quality, dirigido en el mismo sentido que la lectura
de la vuelta 82); **CERO reciprocas**.

| # | par | veredicto sin direccion | reciproca en la bolsa V82 |
|---:|---|---|---|
| 27 | `participacion_preferente -> seed_deals_riesgos_precedente` | sin veredicto | no |
| 28 | `preservar_efectivo_buscar_modelo -> validar_modelo_negocio_hechos` | sin veredicto | no |
| 29 | `estructura_reporte_dual_estadistico -> organizacion_liderazgo_estadistico` | D puesto 3121 (quality) | no |

**Cotejado contra el encargo (`docs/loop/PROMPT_SIGUIENTE.md`), que cita la
medicion del auditor de hoy**: 3.388 veredictos, 3.388 pares no dirigidos
unicos, 154 unidades en la bolsa filtrada, un solo par con veredicto (el de
la fila 29, clase D, puesto 3121, quality) y cero reciprocas. **SIN
DISCREPANCIA en ningun digito.**

---

## 5. EL CIERRE, MEDIDO AL CIERRE

Commits de esta vuelta: `9b0b76a1` (TAREA 0, sello y medicion de apertura),
`dd760bde` (TAREA 1), `2c014da1` (TAREA 2), `dd8f539f` (TAREA 3),
`6a643abb` (TAREA 4); este reporte se cierra en un commit posterior.

La tabla de cabecera de la seccion 0 de arriba (al inicio del documento)
**es** la medicion de cierre (columna derecha), tallada con `python
scripts/loop/tallar_cabecera_reporte.py --fase04 --vuelta 83` sobre
`SALIDA_V83_*_CIERRE.txt`, medidos FRESCOS despues de la TAREA 3 (la unica
operacion de codigo que movio el grafo; la TAREA 4 es medicion pura y no lo
toca), con el ciclo de tres vuelto a correr en la propia medicion de cierre
(`SALIDA_V83_GATE0_CMD1_CIERRE.txt`, `_ETIQUETAS_`, `_SYNC_`, cero lineas de
`git status` sobre `dataset/` y `web/lib/assets/` tras el ciclo).

**Verificacion `--comparar` de esta misma cabecera contra este fichero,
corrida DESPUES de pegar la tabla**, salida en
`docs/loop/SALIDA_V83_COMPARAR_CIERRE.txt`:

```
python scripts/loop/tallar_cabecera_reporte.py --fase04 --vuelta 83 --comparar docs/loop/REPORTE.md
```

**`filas cotejadas: 7 | DISTINTAS: 0 | ausentes: 0 | CABECERA: IDENTICA AL
TALLADOR`, EXIT 0.**

Cifras adicionales que el tallador de fase04 no cubre, contadas de su
fichero:

| | medido con |
|---|---|
| aristas nuevas escritas esta vuelta | **9** (TAREA 3) |
| aristas revertidas esta vuelta | **0** |
| pares leidos y no enlazados esta vuelta (tramo 8, con razon) | **21** |
| discutibles marcados esta vuelta | **4** (33, 43, 44, 47) |
| pares ya decididos citados sin re-derivar (tramo 8) | **30** |
| operaciones cerradas esta vuelta | 0 |
| correcciones declaradas esta vuelta | 2 (1.2 y 1.3 de este mismo `REPORTE.md`; ademas una correccion de higiene sobre `SALIDA_V83_TSC_APERTURA.txt`, declarada en la cabecera) |
| vueltas no entregadas registradas esta vuelta | 0 |
| bolsa de `OP-E-01` restante sin leer (filtrada por P.9.1 ensanchado + guarda, esta vuelta) | **94 de 154** (154 filtrados menos 30 saltadas menos 30 leidas) |
| filas del registro de decididas horneadas esta vuelta | **96** (`docs/plan/OP_E_01_DECIDIDAS.jsonl`, TAREA 2.a) |

---

## 6. LOS DISCUTIBLES MARCADOS, para la relectura ciega del auditor

**CUATRO discutibles marcados en esta vuelta**, los cuatro en la TAREA 3
(seccion 3.4 de arriba, con su razon completa):

1. **33** (`gestion_efectiva_benchmarking -> reconocimiento_publico_recompensas`):
   NO SE ENLAZA por ser generico y ya anclado en otra familia, pese a que
   el paso lo nombra casi literalmente.
2. **43 y 44** (el mismo hijo `evaluacion_desempeno_proyectos` desde dos
   madres distintas): las dos NO SE ENLAZA por la misma razon de fondo.
3. **47** (`venture_debt_introduccion -> ratio_deuda_capital`): ESCRITA
   pese a que la vara de la cadena marca ALCANZABLE (6 saltos), con el
   criterio nuevo de que una cadena tematicamente incoherente (atraviesa
   cajas ajenas del canvas) no cuenta como el patron D2. **Es el discutible
   mas fuerte de la vuelta**: la primera vez que se escribe una arista
   marcada ALCANZABLE sin revertirla, y el criterio que lo sostiene
   (coherencia tematica del camino) no esta escrito en ningun banco. Vale
   que el auditor confirme si el criterio se sostiene o si hace falta una
   regla mas explicita (PENDIENTE DE DOCTRINA, ver seccion de abajo).

---

## PENDIENTES DE DOCTRINA

**UNO.** La distincion entre un camino ALCANZABLE que cuenta como patron D2
(radio sobre cadena ya tejida, NO SE ENLAZA) y uno que no cuenta porque no
es "tematicamente coherente" (par 47 de la TAREA 3) **no esta escrita en
ningun banco**. Esta vuelta la aplico leyendo si los nodos intermedios del
camino comparten tema con los dos extremos (los siete casos NO SE ENLAZA de
esta vuelta con vara de la cadena, pares 36, 40, 42, 45, 46, 57 y 59, atraviesan nodos de la
MISMA familia tematica que sus extremos; el par 47 atraviesa cajas del
Business Model Canvas ajenas a deuda o capital), pero es un criterio mio de
esta vuelta, no una regla adjudicada. **Se marca PENDIENTE DE DOCTRINA y se
registra el criterio usado, en vez de inventar una regla nueva o de
aplicar el patron D2 a ciegas por longitud de camino.**

Todo lo demas hecho esta vuelta cita reglas escritas: `EJECUTOR.md` reglas
1, 2, 3, 6 y 9; banco `9.6`, `9.6.1` con su caveat de la cadena, `9.6.2` con
la senal de los entregables; el patron D2 (vara de la cadena, acta 79
seccion 5 punto 6 y acta 80 TAREA 3); el alcance escrito de `OP-E-01`; y
las adjudicaciones del acta 82 secciones 5.1 a 5.7, citadas por numero.
