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

**CABECERA PENDIENTE DE TALLAR AL CIERRE.** Se pega entera al final de esta
vuelta, con `python scripts/loop/tallar_cabecera_reporte.py --fase04 --vuelta 83`,
tras la ultima operacion de codigo (regla `EJECUTOR.md`: "el estado al
cierre se mide al cierre").

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
`nodos_siguientes` de su propio hijo. Este instrumento es
`scripts/loop/vuelta83_hornear_decididas.py` en su modo de verificacion
(la misma funcion `arista_presente_hoy`, reusada) mas la tabla que la
TAREA 3 arma con esos datos; su salida citable es
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
