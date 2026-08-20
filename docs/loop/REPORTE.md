# REPORTE DE LA VUELTA 57 (20 ago 2026, ejecutor Opus 5)

**LA TAREA 1 ENTERA Y LA TAREA 2 ENTERA. EL TRAMO 4 SE ABRE Y SE CIERRA EN LA MISMA VUELTA, CON 44
ACTOS FUNDIDOS DE 50 Y SEIS DECLARADOS.** **EL HALLAZGO DE LA TAREA 1 ES QUE LA LISTA DE LAS SANAS
CON FIGURA ESTABA ENVEJECIDA POR LOS DOS LADOS**, y el lado que nadie habia visto es el que ENTRA:
el `494` es `C` desde el 15 ago 2026 y ninguna de las dos listas lo recogio nunca. **EL HALLAZGO DE
LA TAREA 2 SALE, otra vez, DE CORRER UNA GUARDA: la simulacion del lote A cae en ROJO por una
DUPLICADA QUE SOLO SE VE POR EL RESOLUTOR**, la misma grieta que la vuelta 56 destapo con los
ajenos, en otro sitio. **Y APARECE UNA ESPECIE QUE LA CAMPANA NO HABIA VISTO: un acto cuyos DOS
miembros son PUERTA**, donde la guarda 1B no deja fundir en ninguna direccion.

| | |
|---|---|
| **rama** | `pasada-unica` |
| **hash de apertura** | `c0e8041a` (la decision del fundador), **arbol limpio y todo pusheado; la regla 3 se cumplio POR VACIO y se dice asi en vez de darla por cumplida** |
| **hash final** | `66c36215` (el cierre) mas este mismo commit, que solo escribe esta cabecera, **pusheados a `origin/pasada-unica`** |
| **commits de la vuelta** | **6**, leidos de `git log --oneline -7` al escribir esta cabecera: `27a401d3` (apertura medida y TAREA 1 entera), `75863aee` (el tramo 4 abierto), `0481113f` (lote A), `a1d7269d` (lote B), `706397c7` (lote C), `66c36215` (el cierre), **mas este**, que solo escribe esta cabecera porque el commit del cierre no podia contener su propio hash |
| **arbol al cierre** | limpio tras el commit del cierre |

---

## 0. LA APERTURA Y EL CIERRE, LA TABLA TALLADA POR INSTRUMENTO (regla 1, decision del fundador)

**ESTA TABLA NO ESTA TECLEADA Y ES LA PRIMERA VEZ QUE SE PUEDE DECIR:** sale entera de
`python scripts/loop/tallar_cabecera_reporte.py --vuelta 57`
([`SALIDA_V57_TALLAR_CABECERA.txt`](SALIDA_V57_TALLAR_CABECERA.txt)), que es el instrumento que la
decision del fundador del 20 ago 2026 (opcion b) mando estrenar aqui. **Cada celda se extrae por
expresion regular de la salida que la cita, y las dos columnas se leen de ficheros DISTINTOS**, que
es exactamente lo que la caida de la vuelta 56 no hizo.

| | **apertura**, antes de la 1.ª operacion | **cierre, RECOMPUTADO al cierre** |
|---|---:|---:|
| marcador `A` / `B` / `C` / `D` | 551 / 72 / 5 / 2.760 | **551 / 72 / 5 / 2.760** |
| `n`, huecos, duplicados | 3.388 / 0 / 0 | **3.388 / 0 / 0** |
| grafo: ficheros / vivos / deprecados / enlaces | 3.853 / 3.385 / 468 / 17.290 | **3.853 / 3.341 / 512 / 17.369** |
| retrato: `A` crudas / colapsos / pares distintos | 551 / 164 / 387 | **551 / 208 / 343** |
| actos (componentes) | 193 | **149** |
| actos `CERRADOS` / `ABIERTOS` | 140 / 53 | **96 / 53** |
| nodos en `CERRADOS` / `ABIERTOS` | 289 / 240 | **201 / 240** |
| cola de costuras | 1.473 | **1.471** |
| colisiones de clase vigentes | 0 | **0** |
| auto-pares (los dos lados al mismo vivo) | 142 | **186** |
| duplicadas historicas: grupos / nodos | 972 / 764 | **955 / 753** |
| operaciones, estados, dependencias rotas | 71, todas `LISTA`, 0 | **71, todas `LISTA`, 0** |
| entradas del inventario | 672 | **672** |
| las cuatro comprobaciones de `08_VERIFICACION` | TODAS OK (529 igual a 529; 387 igual a 387) | **TODAS OK (441 igual a 441; 343 igual a 343)** |

**Y ANTES DEL COMMIT SE CORRIO EL COMPARADOR, que es lo que la regla 1 pide:**
`python scripts/loop/tallar_cabecera_reporte.py --vuelta 57 --comparar docs/loop/REPORTE.md`
([`SALIDA_V57_TALLAR_CABECERA_COMPARAR.txt`](SALIDA_V57_TALLAR_CABECERA_COMPARAR.txt)) da
**`filas cotejadas: 14 | DISTINTAS: 0 | ausentes: 0`** y **`CABECERA: IDENTICA AL TALLADOR`**, exit
0.

**LA APERTURA CALZA AL DIGITO CON EL ESTADO QUE LA PARADA DE LA VUELTA 56 DECLARO.** **Instrumentos
de apertura, todos corridos ANTES de la primera operacion:**
[`SALIDA_V57_APERTURA.txt`](SALIDA_V57_APERTURA.txt),
[`SALIDA_V57_MARCADOR_APERTURA.txt`](SALIDA_V57_MARCADOR_APERTURA.txt),
[`SALIDA_V57_RECOMPUTO_APERTURA.txt`](SALIDA_V57_RECOMPUTO_APERTURA.txt),
[`SALIDA_V57_COLA_APERTURA.txt`](SALIDA_V57_COLA_APERTURA.txt),
[`SALIDA_V57_COLISIONES_APERTURA.txt`](SALIDA_V57_COLISIONES_APERTURA.txt) y
[`SALIDA_V57_DUPLICADAS_APERTURA.txt`](SALIDA_V57_DUPLICADAS_APERTURA.txt). **El cierre esta en los
ficheros `_CIERRE` hermanos, corridos DESPUES del ultimo movimiento.**

**TRES CIFRAS QUE CUADRAN EXACTAS Y SE DICE POR QUE, porque son la huella de la cirugia:** los
colapsos suben **44** (164 a 208), los pares distintos bajan **44** (387 a 343) y los auto-pares
suben **44** (142 a 186), **UNO POR CADA ACTO QUE ESTA VUELTA FUNDIO**. **Aqui la de los auto-pares
tambien es exacta, a diferencia de la vuelta 56**, donde subia 46 y no 47 porque un acto caia sobre
un auto-par que ya existia: en el tramo 4 ninguno lo hace, y eso se mide en vez de suponerse.

**TASA POR DOMINIO AL CIERRE**, leida de
[`SALIDA_V57_MARCADOR_CIERRE.txt`](SALIDA_V57_MARCADOR_CIERRE.txt): compras 0,6 (n 155) | core 22,5
(n 1.445) | entrega 1,2 (n 171) | environmental 16,5 (n 170) | exportacion 11,5 (n 130) |
franquicias 10,1 (n 148) | health_safety 22,4 (n 192) | quality 14,1 (n 844) | risk_management 0,0
(n 106) | seguridad_digital 11,1 (n 27). **Identica a la de la apertura al digito, porque esta
vuelta no volteo ningun veredicto.**

---

## 1. TAREA 1.3 PRIMERO, PORQUE ES LA QUE MIDE: **EL BARRIDO DE LOS PUESTOS VOLTEADOS**

**Nace `scripts/loop/vuelta57_puestos_volteados.py`**, y su motivo esta **MEDIDO antes de escribir
una linea**: el barrido `9.10` **SI tiene una FAMILIA 2 de puestos**, pero la vuelta 56 lo corrio
con **`--puestos 305`**, que es el valor POR DEFECTO heredado de la vuelta 50. Esta escrito en la
cabecera de [`SALIDA_V56_BARRIDO_910_CIERRE.txt`](SALIDA_V56_BARRIDO_910_CIERRE.txt), que imprime
*puestos corregidos : 305*. **El instrumento sabia buscar; nadie le dijo que buscara el 203.** **UNA
GUARDA QUE HAY QUE ACORDARSE DE ENCENDER NO ES UNA GUARDA.**

| seccion | que hace | por que |
|---|---|---|
| **A, los volteados** | los **DERIVA de `git`** comparando el archivo de veredictos contra un commit base | para que **nadie los teclee**, que es donde fallo la 56 |
| **B, el cotejo general** | coteja **TODA cita de puesto con clase** de `docs/` contra la clase VIGENTE | es la que **habria cazado al 246 y al 360 en la vuelta 52** sin que nadie supiera que se habian movido |

**TRES CORRECCIONES SOBRE MI PROPIO INSTRUMENTO, CADA UNA CON SU MEDICION, antes de publicar nada:**

1. **La primera version ataba una clase con CUALQUIER letra suelta del parrafo**, y daba **243
   rojos y 251 ambiguos**, casi todo ruido. Ahora **solo se juzga lo atado de forma EXPLICITA**, por
   columna de tabla o por marcador de clase, y hay **TRES detectores** escritos con nombre.
2. **Leia las paginas de la FRANJA**, que numeran con `puesto_franja` sobre otro archivo, y daba
   **TRES rojos que eran suyos y no del catalogo**: medido, el puesto 1602 es `D` en la franja y `A`
   en el intra. Quedan fuera, declarado.
3. **Leia `2.117` como los puestos 2 y 117.** Los millares cuentan como un solo numero.
4. **Una tabla con DOS columnas de clase (`clase antes` y `clase ahora`) no ata nada**, porque
   quedarse con la primera publica como vigente lo que la propia tabla declara superado.

**EL CASO POSITIVO DEL INSTRUMENTO, EN LAS DOS DIRECCIONES Y CON EL FALLO REAL:** corrido ANTES de
tocar los ficheros, la guarda dura sale **ROJA con SIETE citas** y las nombra una a una
([`SALIDA_V57_PUESTOS_VOLTEADOS_ANTES.txt`](SALIDA_V57_PUESTOS_VOLTEADOS_ANTES.txt)); corrido
DESPUES, **VERDE**, y las citas verdes suben de 188 a 191
([`SALIDA_V57_PUESTOS_VOLTEADOS_DESPUES.txt`](SALIDA_V57_PUESTOS_VOLTEADOS_DESPUES.txt)).
**Re-corrido al cierre, sigue verde**
([`SALIDA_V57_PUESTOS_VOLTEADOS_CIERRE.txt`](SALIDA_V57_PUESTOS_VOLTEADOS_CIERRE.txt)).

**LAS DOS ALTURAS SE SEPARAN A PROPOSITO Y SE DICE POR QUE:** lo que esta **BAJO GUARDA** es el
deber que el `9.10` pone en el MISMO ACTO del volteo, y eso es rojo y detiene; lo **HEREDADO** es
atraso de vueltas viejas, se imprime entero y **no se esconde**, pero no es la falta de esta vuelta.
**El instrumento LISTA las once heredadas y no las corrige**, y va como pregunta al auditor
(seccion 12).

---

## 2. TAREA 1.1 Y 1.2: **LA LISTA ESTABA ENVEJECIDA POR LOS DOS LADOS**

**Instrumento: `scripts/loop/vuelta57_correcciones_tarea1.py`, con ANCLA LITERAL UNICA (rojo si
falta o se repite) e idempotente** ([`SALIDA_V57_CORRECCIONES_T1_IDEMPOTENCIA.txt`](SALIDA_V57_CORRECCIONES_T1_IDEMPOTENCIA.txt),
los ocho sitios en `YA ESTABA`). **19 lineas anadidas y 5 borradas, medido por `git`**, y las cinco
borradas son las cinco lineas que se reescriben CON EL TEXTO VIEJO TACHADO DENTRO.

| | lo que se escribio | donde |
|---|---|---|
| **1.1** | el **203** con `~~**C**~~ **D**` y su nota fechada, con la causa dicha: la vuelta 56 volteo ese puesto y **no barrio esta tabla en el mismo acto**, que es lo que el `9.10` manda y lo que **el precedente del 844** (vuelta 49) si hizo | `INTRA_DOMINIO_INFORME.md`, linea 4169 |
| **1.2** | la lista de las sanas con figura: **salen** el 203, el 246 y el 360; **ENTRA el 494**; la cuenta de **7 a 5** | `03_FUSIONES.md` 167 y `04_ENLACES.md` 313, mas el titulo de su seccion |

**EL HALLAZGO, Y NO ESTABA EN EL ENCARGO:** el encargo mandaba tachar tres. **Medido con `git` sobre
las 194 versiones del archivo de veredictos, el `494` es `C` desde el 15 ago 2026**, por el commit
`7cec9ecc` que lo volteo desde `A` por el tercer ejemplar del banco `9.22`, **y las dos listas no lo
recogieron nunca**. **Una lista publicada envejece por no soltar y tambien por no tomar**, y el
carril del `9.10` solo miraba una de las dos direcciones.

**LA `C` VIGENTE, RECOMPUTADA POR MI DEL ARCHIVO Y NO HEREDADA DEL ENCARGO: 201, 215, 494, 1077 y
1240, CINCO.** Calza con la que el encargo esperaba.

**DONDE VAN LAS NOTAS, Y ES UNA DECISION DE INSTRUMENTO QUE SE DECLARA:** las CELDAS quedan limpias
(solo el tachado y la cifra nueva) y las notas fechadas van en un **BLOQUE DE CITA debajo de su
tabla**, y no dentro de la celda como en la vuelta 56. **El motivo es que la nota nombra letras de
clase**, y una nota dentro de la celda haria que el instrumento de la TAREA 1.3 leyera esa celda
como ambigua. **Va marcado (`D2`).**

---

## 3. TAREA 2: **EL TRAMO 4 ABIERTO, Y LAS DOS LECTURAS CALZAN**

**Abridor: `scripts/loop/vuelta57_tramo4_nomina.py`**, sucesor declarado del de la 56 con la
aritmetica copiada entera ([`SALIDA_V57_TRAMO4_NOMINA.txt`](SALIDA_V57_TRAMO4_NOMINA.txt)).

**LO UNICO QUE NO ES COPIA, Y CAMBIA UNA LECTURA: LA LECTURA B YA NO PUEDE SER UN BLOQUE FIJO DE LA
NOMINA DE LA 48.** El motivo lo mide el propio instrumento: **el tramo 3 realmente abierto NO es el
bloque 101 a 150** (entra `construir_sobre_ideas_ajenas` mas `reglas_brainstorming`, sale
`crecimiento_ingresos_verdes` mas `generacion_ingresos_verdes`), asi que **tomar el bloque 151 a 200
dejaria al acto desplazado FUERA DE LAS DOS LECTURAS**, y la comprobacion se volveria ciega justo
donde la vuelta anterior encontro algo. **La lectura B es la nomina de la 48 EN SU ORDEN saltando
los tramos FIJADOS.** Y los tramos previos se identifican **por su fichero fijado**, con una guarda
nueva: **el fichero del tramo 2 tiene que seguir calzando con su bloque 51 a 100**, y calza.

| | |
|---|---|
| **las dos lecturas** | **CALZAN**, mismo conjunto y mismo orden, sin ninguna divergencia que diagnosticar |
| **guarda del prefijo** | los **19** vivos de los tramos 1, 2 y 3 (11 mas 5 mas 3) ocupan los puestos **1 a 19 sin huecos**, MEDIDO |
| **el tramo** | los puestos **20 a 69** de hoy, que son los **150 a 199** de la 48, encabezado por el acto que la 56 dejo desplazado |
| **figura** | **FUSION PURA, tamano 2 y PURO A, 50 de 50** |
| **los cuatro ajenos** | **VERDE POR LOS DOS CAMINOS**, el literal y el del resolutor |
| **solape con tramos anteriores** | **CERO** |
| **colisiones esperadas** | **100 combinaciones simuladas y CERO que fabriquen colision**, medidas ANTES de tocar un nodo |

**QUE NO HAYA NI UNA COLISION ESPERADA ES LA DIFERENCIA MAS GRANDE CON LA VUELTA 56**, y tiene una
consecuencia que se dice: **esta vuelta NO volteo ni un solo veredicto**, no hubo relectura de filo
y `P.16` no tuvo nada que limpiar. **El marcador es identico al abrir y al cerrar en las CUATRO
clases.**

---

## 4. LOS TRES LOTES: **CUARENTA Y CUATRO FUSIONES**

**LAS TABLAS DE ESTA SECCION NO ESTAN TECLEADAS: salen enteras de
`python scripts/loop/vuelta57_tallar_planes.py`**
([`SALIDA_V57_TALLAR_PLANES.txt`](SALIDA_V57_TALLAR_PLANES.txt)), que las cuenta de los
`PLAN_V57_*.json` **SELLADOS** y cae en rojo con el acto nombrado si un motivo no encaja en ninguna
forma conocida. **Las mismas tablas van al registro del tramo en `03_FUSIONES.md`, recortadas de
esta misma salida por maquina.**

| lote | actos | fundidos | mueren | piezas | enteras | ya dichas | de `INCISO` | perdidas nombradas |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| **A** | 1 a 17 sin el 11, el 13 ni el 14 | **14** | **14** | **74** | 16 | 36 | **22** | **2** |
| **B** | 18 a 34 sin el 24, el 25 ni el 31 | **14** | **14** | **78** | 25 | 28 | **25** | **1** |
| **C** | 35 a 50, **los dieciseis** | **16** | **16** | **93** | 27 | 41 | **25** | **0** |
| **los tres** | | **44** | **44** | **245** | **68** | **105** | **72** | **3** |

| la forma, leida del motivo sellado | cuantos | los actos |
|---|---:|---|
| **UNA SOLA VARA de contenido no empatada, y BASTA** | **18** | 3, 6, 8, 10, 16, 18, 21, 23, 29, 30, 33, 35, 37, 40, 44, 46, 48, 49 |
| **TODAS LAS VARAS de contenido de acuerdo** | **15** | 2, 4, 5, 7, 9, 12, 15, 17, 19, 22, 26, 27, 34, 36, 39 |
| **LA PIEZA DECLARADA GANA A UN CONTEO de contenido** | **4** | 41, 45, 47, 50 |
| **LA PUERTA SOBREVIVE, con el choque registrado** | **2** | 20, 38 |
| **LOS CONTEOS EMPATAN y la PIEZA DECLARADA decide** | **2** | 28, 42 |
| **EL CONTENIDO EMPATA y EL CABLEADO DECIDE SOLO** | **1** | 1 |
| **LA PUERTA SOBREVIVE y los conteos concuerdan, contra la razon declarada** | **1** | 43 |
| **LOS TRES CONTEOS EMPATAN y decide la pieza declarada POR CANTIDAD** | **1** | 32 |
| **suma** | **44** | |

**Guardas, por acto y en los cuarenta y cuatro:** miembros vivos y nomina completa, **guarda 1B por
vacio en los 44**, cobertura exacta de indices sin olvidos ni sobrantes, cero repetidos literales,
**cero auto-aristas y cero duplicadas NUEVAS en los tres lotes**, **censo real de colisiones CERO
contra prediccion CERO (`CALZA: SI`) tras cada lote**, y los campos que la operacion no redacta
intactos.

### LAS TRES ESPECIES DE CHOQUE DE PUERTA, DICHAS APARTE PORQUE NO SON LA MISMA

| acto | sobrevive | la especie, con sus cifras |
|---:|---|---|
| **20** | `seleccion_canales_distribucion` | **DE CONTENIDO**: pasos 4 contra 4 empatados y **condiciones 1 contra 2 A FAVOR DEL OTRO**; el cableado apuntaba a la puerta (4 contra 1). Misma figura que el 35 del tramo 3 |
| **38** | `responsabilidad_prospectiva` | **DE PIEZA DECLARADA, y es NUEVA**: los conteos **EMPATAN AL DIGITO** y el cableado apunta a la puerta, asi que **quien contradice a la guarda es LA RAZON**, no una cifra |
| **43** | `cultura_justa` | **NO ES CHOQUE DE CONTEOS**: los TRES conteos apuntan a la puerta (5v4, 3v2, 16v4) y **solo la razon apunta al otro**, y ella misma se llama *de los mas discutibles* |

**EN LOS TRES, LO QUE LA RAZON PREFERIA VIAJA ENTERO EN EL REPARTO**, y eso es lo que hace
defendible respetar la guarda: en el 20 las dos piezas propias del que muere van de `APPEND`; en el
38, el relato de la persona involucrada y el apoyo a la segunda victima; en el 43, **el grupo de
confianza que revisa los casos ambiguos**, que era la institucion entera por la que la razon
prefería al otro nodo.

### LOS CUATRO ACTOS DONDE **LA PIEZA DECLARADA GANA A UN CONTEO**

**Actos 41, 45, 47 y 50.** La vara aplicada es la del **acta 53 pregunta 3 y el acta 54 pregunta
2**, *gana lo declarado y no el conteo*, que es la que el acta 56 confirmo para el acto 23 del tramo
3. **Se dice el riesgo en vez de callarlo:** el **acta 50, adjudicacion 3**, dice que en el choque
entre la letra y la aritmetica **manda la aritmetica**. **Van marcados (`D3`).**

**Y EN LOS CUATRO SE MIDIO QUE EL REPARTO SALDA LA VARA QUE QUEDO ATRAS**, que es lo unico que
convierte la eleccion en barata: en el **41** las cuatro piezas del que muere viajan aunque tenga
mas pasos que el superviviente; en el **45** y en el **50** la condicion que sostenia el conteo
contrario **viaja entera**, asi que el superviviente termina con tantas condiciones como el otro
tenia; y en el **47** el superviviente pasa de **una** condicion a **tres**.

### LAS TRES PERDIDAS NOMBRADAS, TODAS DE LA MISMA ESPECIE

**Talladas de los planes sellados** con
`python scripts/loop/vuelta56_tallar_perdidas_v55.py --vuelta 57 --lotes A,B,C`
([`SALIDA_V57_TALLAR_PERDIDAS.txt`](SALIDA_V57_TALLAR_PERDIDAS.txt)): **TRES, LAS TRES DE
CONDICIONES** (actos 12, 16 y 23), todas por la causa heredada de que el `INCISO` de condiciones no
existe. **CERO de parametro de paso**, a diferencia de la vuelta 56, y por eso **el `D8` de aquella
vuelta no se repite aqui**: no hay ninguna etiqueta generica cubriendo una especie distinta.

**TRES sobre 245 piezas repartidas** es la cuenta que mide el reparto, y va dicha porque una cuenta
de perdidas sin su denominador no dice nada.

### DOS FIGURAS NUEVAS QUE LAS RAZONES YA TRAIAN ESCRITAS

| figura | acto | que dice |
|---|---:|---|
| **LA MISMA NORMA EN DOS FOLLETOS** | **39** | la repeticion no viene de dos autores que piensan parecido sino de **dos publicaciones del MISMO organismo** (OSHA3885 y OSHA3886) que cubren el mismo requisito con distinto detalle |
| **EL CASO NO ES LA CASA** | **49** | muere el **estudio de caso** de Nakina y sobrevive la **doctrina generica**, porque *el alcance del rol es contenido* (`P.8`) y el entregable del caso lleva la fecha de un terraplen dentro |

**Las dos se trasladan SIN TOCARLAS**: son de las razones, no mias, y el ejecutor las registra en el
plan sellado para que el auditor las vea con su procedencia.

---

## 5. LOS SEIS ACTOS DECLARADOS, CADA UNO CON SU CARRIL

| acto | especie | por que |
|---:|---|---|
| **11** | **EMPATE SIN VARA** | pasos 4v4, condiciones 2v2 **y cableado 2v2**; propio declarado a los dos lados |
| **13** | **CONTEOS QUE CHOCAN, la declarada no desempata** | pasos 6v5 a un lado, condiciones 3v4 al otro; **DOS** perdidas declaradas de cada lado |
| **14** | **CONTEOS QUE CHOCAN, la declarada no desempata** | pasos 5v6 a un lado, condiciones 3v2 al otro; **DOS** y **DOS** |
| **24** | **EMPATE SIN VARA** | 4v4, 2v2 y 2v2, con **UNA** linea propia de cada lado |
| **25** | **LOS DOS MIEMBROS SON PUERTA** | **especie NUEVA**: no queda ningun candidato a absorbido |
| **31** | **CONTEOS QUE CHOCAN, la declarada no desempata** | pasos 4v5 a un lado, condiciones 3v2 al otro; **UNA** y **UNA** |

**EL ACTO 25 ES LA NOVEDAD Y VA CON SU NOMBRE PROPIO.** La guarda 1B dice desde la vuelta 48 que un
nodo que es semilla o extremo de puente **no se absorbe**, y hasta hoy habia mordido con **UNA**
puerta en el acto: entonces la vara del acta 54 pregunta 1 resolvia el caso (la guarda restringe y
el contenido elige entre lo permitido). **Aqui los DOS son puerta**, y cualquiera de las dos
elecciones deprecaria una. **No es que el contenido no separe** (separa, y por mucho: pasos 6 contra
4 y condiciones 3 contra 2, con la razon declarando subconjunto estricto): **es que la guarda no
deja fundir en ninguna direccion**. Va como **PENDIENTE DE DOCTRINA 5**, con las dos salidas
imaginables nombradas y **ninguna elegida aqui**.

**Y EL 24 TRAE UN MATIZ QUE LO SEPARA DE TODOS LOS EMPATES ANTERIORES:** sus dos piezas propias son
**las dos respuestas OPUESTAS al mismo problema**, un nodo **cede** ante la barrera (ajustar el
producto) y el otro **insiste** (dar seguimiento hasta que se resuelva). **Un empate cuyas dos
mitades son opuestas no se rompe eligiendo la mas larga.**

**El pendiente de doctrina 1 pasa de SEIS actos a ONCE**: los 4, 20 y 42 del tramo 2, los 27, 37 y
45 del tramo 3, y ahora el 11, el 13, el 14, el 24 y el 31.

---

## 6. LA DUPLICADA QUE **SOLO SE VE POR EL RESOLUTOR**

**La simulacion del lote A salio en ROJO, y la guarda hizo lo correcto:**

> `DUPLICADA NUEVA: documentacion_exportacion en nodos_previos resuelve dos veces a
> incoterms_reglas_comerciales_internacionales`

**LA CAUSA, MEDIDA:** ese nodo nombra en sus previos a `glosario_terminos_incoterms`, que **YA HOY**
resuelve al superviviente, y ademas a `terminos_de_venta_incoterms`, que el acto 17 absorbe. **El
ejecutor de fusiones sustituye y deduplica LITERAL**, y por eso esta duplicada le sobrevive: las dos
cadenas son distintas y **solo el resolutor las ve iguales**. **Es la misma grieta que la guarda de
los ajenos destapo en la vuelta 56, en otro sitio.**

**Nace `scripts/loop/vuelta57_retirar_duplicada_por_alias.py`**, sucesor declarado de
`scripts/loop/vuelta43_retirar_arista_interna.py`, con su forma de trabajo copiada entera: **retirar
ANTES, en los DOS sentidos, y dejar que el ejecutor corra despues ENTERO Y SIN TOCAR**. Comprueba
**por nodo** que el tercer nodo sigue unido al superviviente por el otro camino antes de retirar
nada, y es **ROJO** si alguna duplicada no la fabrica un absorbido del plan, porque **el pasivo
ajeno es de `OP-S-12`**.

**Y UNA CORRECCION SOBRE MI PROPIO INSTRUMENTO ANTES DE TOCAR UN NODO:** su primera version
encontraba **CUATRO** y habria retirado **TRES de mas**. Medido: en esas tres la otra entrada **ERA
el superviviente escrito con su propio nombre**, y ahi la sustitucion literal del ejecutor deja el
id repetido y su deduplicacion lo resuelve sola. **La unica real es la que llega por un ALIAS.**
Retiradas: **DOS entradas**, la del tercer nodo y su reciproca. En los lotes B y C se corrio igual y
salio **sin nada que retirar**.

---

## 7. LA GUARDA DE LA JUNTURA: **IMPEDIR EN VEZ DE REPARAR**

**La vuelta 56 escribio SEIS junturas de PUNTO MAS COMA** en sus lotes A y B y tuvo que repararlas
**DESPUES** con un instrumento aparte. **En el generador de planes de esta vuelta la juntura se
comprueba ANTES de sellar el plan**, y mordio **DOS VECES DE VERDAD**:

| lote | acto | que paso |
|---|---:|---|
| **A** | **9** | los dos incisos caian sobre pasos de `compra_offsets_carbono`, que terminan en punto. **ROJO, no escribio nada**, y los nexos se reescribieron |
| **C** | **49** | el paso 2 del superviviente termina en punto y el nexo abria con coma. **ROJO**, y el nexo se reescribio |

**Una guarda que se corre despues del dano repara; esta impide.**

---

## 8. EL CASO POSITIVO: **UNA GUARDA MAS Y UNA FIGURA NUEVA**

**El de la vuelta 56 se re-corrio PRIMERO como contraste y sale verde con sus cinco guardas**
([`SALIDA_V57_CASO_POSITIVO_V56.txt`](SALIDA_V57_CASO_POSITIVO_V56.txt)). **El de esta vuelta,
`scripts/loop/vuelta57_caso_positivo.py`, se fabrica sobre EL ACTO 37 DEL TRAMO 3**, otro
**DECLARADO** que esta vuelta no toca, **y que es SIMETRICO AL DIGITO** (5 pasos contra 5 y 1
condicion contra 1). **Las vueltas 55 y 56 usaron actos ASIMETRICOS**, y la simetria es la peor
figura para la guarda de cobertura, porque un plan que se equivoque de miembro cubre igual de bien
los dos lados.

| guarda | la mentira | resultado |
|---|---|---|
| **`1`** (**NUEVA**) | un absorbido **YA DEPRECADO**, con un deprecado **REAL** del catalogo (`6s_lugar_trabajo`) y no un id inventado | **exit 1**, `YA esta deprecado`: la rama probada es esa y no la de id inexistente |
| **`1B`** | un absorbido que es puerta (`domina_lo_que_compras`) | **exit 1, `ROJO`, aborta sin escribir** |
| **cobertura, POR OLVIDO** | el plan se salta el paso 3 | **exit 1, `faltan ['3']`**, y enciende **DOS** lineas |
| **cobertura, POR SOBRANTE** | el plan declara un paso 6 que el absorbido no tiene | **exit 1, `sobran ['6']`**, y enciende **UNA SOLA** |
| **INCISO VERBATIM** | un inciso que es parafrasis | **exit 1, `NO es trozo verbatim`** |
| **colisiones** | censo contra una cuenta esperada FALSA de 7 | **`MEDIDA: 0 \| CALZA: NO`** |

**LAS SEIS MUERDEN**, al abrir y al cerrar
([`SALIDA_V57_CASO_POSITIVO.txt`](SALIDA_V57_CASO_POSITIVO.txt) y
[`SALIDA_V57_CASO_POSITIVO_CIERRE.txt`](SALIDA_V57_CASO_POSITIVO_CIERRE.txt)). **La guarda 1 nunca
se habia puesto a mentir**: las vueltas 55 y 56 la declaraban verde en todos los actos, y **una
guarda que solo se declara verde no se sabe si muerde**.

**Y EL INSTRUMENTO MIDE LA FIGURA DEL ACTO EN CADA CORRIDA:** si el absorbido cambiara de forma, la
cobertura exacta escrita dentro mentiria, y el instrumento sale **rojo sin correr una sola mentira**.

---

## 9. EL BARRIDO `9.10` DEL CIERRE

**Con las cifras viejas DE HOY** (`--viejo 551,72,5,2760 --retrato 164,387`,
[`SALIDA_V57_BARRIDO_910_CIERRE.txt`](SALIDA_V57_BARRIDO_910_CIERRE.txt)). **CINCO celdas
corregidas** ([`SALIDA_V57_CORRECCIONES_910.txt`](SALIDA_V57_CORRECCIONES_910.txt), **idempotente**:
al re-correrlo las ocho salen `YA ESTABA`):

| la celda | decia | **medido al cierre** |
|---|---:|---:|
| `RECOMPUTO_3388.md` **247**, colapsos **y su contador** | 164, contador DIEZ | **208, contador ONCE** |
| **248**, pares distintos **y su contador** | 387, contador TRECE | **343, contador CATORCE** |
| **528**, el checkpoint `ii` en sus dos parentesis **y su nota** | 387 igual a 387 | **343 igual a 343, sigue OK** |

**EL MARCADOR NO SE MUEVE Y NO ES UN OLVIDO**, y aqui el motivo es **mas fuerte que en la vuelta
56**: esta vuelta **no volteo ni un solo veredicto**, porque las colisiones esperadas del tramo
entero salieron CERO. **Las filas del marcador del informe y las dos tablas por dominio hermanas
tampoco se tocan**: la hermandad se cumple **POR VACIO** y se dice.

**Y UNA CELDA QUE NO SE TOCA CON SU MOTIVO ESCRITO:** la seccion **PASO 3** de `RECOMPUTO_3388.md`
publica **852 nodos con `A` y 334 componentes**, y hoy el instrumento da otras cifras. **NO se
corrige, y el motivo esta en la propia seccion**: dice literalmente que esta *calculado sobre el
retrato del paso 1 (las 583 A resueltas)*, o sea que es **el retrato de un dia con su corte
declarado**, y eso no es una tabla envejecida. Es la distincion que el **LIMITE DECLARADO** del
barrido `9.10` nombra. **Va marcado (`D6`).**

---

## 10. GATE 0, LAS SUITES Y EL REGISTRO

| que | como salio |
|---|---|
| **Gate 0**, ciclo de **TRES** comandos | `run_phase1 --reaplico-curaduria` con **`GATE 0: OK`** las **cuatro** veces (apertura y tres lotes); `etiquetas_de_cara --aplicar`; `sync_assets_web` |
| **suite del motor** | **25 de 25** tras cada lote, **sin ninguna caida real esta vez** |
| **suite web** | **80** ficheros, **1.030** pasadas y **3** saltadas, las tres veces |
| `tsc --noEmit` | **CERO** lineas |
| duplicadas / auto-aristas **NUEVAS** | **CERO** y **CERO** en los tres lotes |
| censo de colisiones tras cada lote | **CERO**, con `--esperadas 0` y **`CALZA: SI`** las tres veces |
| `reanclar_por_resolutor.py` | corrido **ENTRE la fusion y `run_phase1`** en los tres lotes, que es el orden que la vuelta 56 se salto en su lote A. **En blanco las tres veces** |
| `verificar_mapas_destejido.py` | **OK** (vara 1; la 2 no se corrio, no hay mapa de particion nuevo) |
| **registro del tramo 4** | escrito en `03_FUSIONES.md` con `scripts/loop/vuelta57_registro_tramo.py`, **cada cifra extraida de su salida** y las cinco tablas **recortadas por maquina** de la salida de su tallador |
| **hook guardian** | verde en todos los commits |

---

## 11. CORRECCIONES DECLARADAS SOBRE MI PROPIO TRABAJO

1. **EL INSTRUMENTO DE LA TAREA 1.3 NACIO DEMASIADO SUELTO Y LO CACE MIDIENDO, NO LEYENDO:** su
   primera version daba **243 rojos y 251 ambiguos**. Las cuatro correcciones estan en la seccion 1
   con su medicion cada una. **Si lo hubiera publicado asi, habria sido un barrido que grita y por
   eso no se puede auditar**, que es el primo hermano del barrido que tranquiliza sin mirar.
2. **EL INSTRUMENTO DE LA P.16 POR ALIAS ENCONTRABA CUATRO Y TRES ERAN SUYAS.** Corregido antes de
   tocar un nodo, con el motivo medido escrito dentro del propio fichero.
3. **DOS ANCLAS DE LA TAREA 1 FALLARON EN LA PRIMERA CORRIDA POR EL FINAL DE LINEA:**
   `04_ENLACES.md` viene con **CRLF** y las otras dos con **LF**, asi que un ancla de varias lineas
   escrita con LF no aparecia. **El instrumento lo dijo en rojo y no escribio nada**; ahora adapta
   el final de linea por fichero y lleva el motivo escrito.
4. **EL TALLADOR DE PLANES SALIO ROJO CON 23 ACTOS** porque este tramo estreno cinco formas de
   veredicto que su tabla de frases no conocia. **La guarda hizo lo correcto** (no clasifica por
   defecto), y las cinco formas nuevas se anadieron **marcadas como nuevas**, sin tocar ni renombrar
   ninguna de las viejas.
5. **UN MANEJO MIO SIN CONSECUENCIA SOBRE NINGUN DATO:** al fabricar el tallador de planes por copia
   corte el docstring por el sitio equivocado y el fichero no compilaba. Se arreglo antes de la
   primera corrida.
6. **Ficheros tocados que el encargo no nombraba, declarados:** `docs/COSTURAS_INTERNAS.jsonl` y
   `docs/COSTURAS_INTERNAS_RESUMEN.md`, `docs/plan/ARISTAS_DUPLICADAS.jsonl`, `dataset/metadata/*` y
   `web/lib/assets/*` (los reescriben los instrumentos y el ciclo de Gate 0). **Mismo alcance que
   las vueltas 48 a 56 MENOS el banco de rumbos**, que esta vuelta no toco porque el re-anclaje
   salio en blanco las tres veces.

---

## 12. LOS DISCUTIBLES MARCADOS, para la relectura ciega

**Marcados ANTES de saber si acierto. Son OCHO.**

| # | el discutible | por que lo marco |
|---:|---|---|
| **D1** | **Corregi una celda que el encargo NO nombraba**: la fila hermana de la tabla de `03_FUSIONES.md` publicaba `B, dudosas` en **89** y la `B` de hoy es **72**. | Corregir el `7` y publicar el `89` de al lado sin mirarlo es exactamente la especie que la regla 1 castiga, y la celda vive en la misma tabla que el encargo si manda tocar. **Pero es alcance que yo me di**, y un lector estricto puede decir que una celda no nombrada va a la lista de atraso y no al mismo acto |
| **D2** | **Puse las notas fechadas DEBAJO de la tabla y no DENTRO de la celda**, que es la forma que la vuelta 56 uso. | El motivo es de instrumento y esta medido: la nota nombra letras de clase, y dentro de la celda haria que el instrumento de la TAREA 1.3 leyera esa celda como AMBIGUA en vez de verde. **Pero cambio una forma de registro por conveniencia de mi propio instrumento**, y eso se puede leer como acomodar el papel a la maquina |
| **D3** | **En CUATRO actos (41, 45, 47 y 50) deje que LA PIEZA DECLARADA ganara a un conteo de contenido.** | `P.8` cuenta el material propio declarado como contenido, la razon nombra el superviviente con todas sus letras, y el acta 53 pregunta 3 dice *gana lo declarado*. **Pero el acta 50, adjudicacion 3, dice que en el choque entre la letra y la aritmetica MANDA LA ARITMETICA**, y son cuatro actos, no uno: si la vara es la otra, hay cuatro fusiones al reves |
| **D4** | **En el acto 32 rompi un empate TRIPLE (5v5, 2v2, 3v3) con la CANTIDAD de lineas propias declaradas**, una contra dos. | El material propio declarado es vara de contenido (acta 54, pregunta 4), asi que el contenido no calla y no es empate sin vara. **Pero contar LINEAS DECLARADAS como si fueran una vara numerica es aritmetica sobre la letra**, y nadie ha adjudicado que se pueda; con la lectura contraria el 32 seria el septimo declarado |
| **D5** | **En los actos 38 y 43 deje que la GUARDA 1B decidiera contra el superviviente que la RAZON declara.** | La guarda no es negociable y en los dos casos **lo que la razon prefería viaja entero** en el reparto, asi que no se pierde nada medible. **Pero en el 43 la razon se llama a si misma *de los mas discutibles* y avisa de que muere el nodo de cinco pasos contra el de cuatro**, y aqui muere el de cuatro por la puerta: es la lectura contraria de su propio aviso |
| **D6** | **NO corregi la seccion PASO 3 de `RECOMPUTO_3388.md`** (852 nodos con `A`, 334 componentes), que mi propia vuelta movio. | La seccion declara su corte con todas sus letras (*las 583 A resueltas*), y una cifra con su corte declarado no es una tabla envejecida: es el LIMITE que el propio barrido `9.10` nombra. **Pero mi vuelta la movio, y el `9.10` dice que quien mueve barre**; un lector puede decir que el corte declarado exime de recomputar pero no de anotar el desfase |
| **D7** | **Deje ONCE citas heredadas envejecidas SIN corregir** y solo listadas por el instrumento. | No son la falta de esta vuelta, el encargo nombraba tres sitios, y varias pueden ser el retrato de un dia con su corte declarado, que es una diferencia de lectura que ningun instrumento lexico sabe hacer. **Pero acabo de escribir un instrumento que las ve y las publico sin arreglarlas**, y eso deja el catalogo con una lista de deudas conocidas |
| **D8** | **Amplie el tallador de planes con CINCO formas nuevas en vez de escribirle un sucesor**, y lo hice sobre un fichero que YA es sucesor. | Es un fichero nuevo (`vuelta57_tallar_planes.py`) y las formas viejas quedan intactas y sin renombrar, asi que las dos corridas siguen comparables. **Pero la frontera del acta 54 pregunta 3 habla de instrumentos cuyas cifras cita una pagina, y este las cita el registro del tramo 4 desde hoy**: la amplie antes, pero la frontera la trazo yo |

---

## 13. PENDIENTES DE DOCTRINA

1. **DONDE VIVE LA PIEZA DECLARADA CUANDO EL ACTO TIENE UN SOLO PAR, Y QUE PRELACION HAY ENTRE
   CONTEOS.** **Heredado y ENGORDADO A ONCE ACTOS**: los 4, 20 y 42 del tramo 2, los 27, 37 y 45 del
   tramo 3, y los **11, 13, 14, 24 y 31** de este. **Y esta vuelta le anade DOS ramas nuevas**: los
   cuatro actos donde la declarada **gana** a un conteo (`D3`), y el acto 32 donde se rompe un
   empate triple **por la cantidad** de lineas declaradas (`D4`).
2. **EL `INCISO` PARA CONDICIONES SIGUE SIN EXISTIR EN EL INSTRUMENTO.** **Heredado, y esta vuelta
   lo paga TRES veces** (actos 12, 16 y 23). **Tres sobre 245 piezas**, que es una tasa mucho mas
   baja que la de la vuelta 56 y conviene decirlo con su denominador.
3. **QUIEN CONTESTA UNA PREGUNTA DE POLITICA DE CATALOGO.** **Heredado y sin cambio hoy.**
4. **LA GUARDA DE LOS CUATRO AJENOS NO DICE SI HABLA DE IDS O DE NODOS.** **Heredado.** Esta vuelta
   **no lo paga** (los cuatro salen verdes por los dos caminos) pero **la misma grieta aparecio en
   otro sitio**: la duplicada que solo se ve por el resolutor (seccion 6). **Es la segunda vez que
   la diferencia entre leer literal y leer resuelto cuesta algo**, y eso sugiere que la pregunta no
   es de esa guarda sino del catalogo entero.
5. **QUE SE HACE CON UN ACTO CERRADO CUYOS DOS MIEMBROS SON PUERTA.** **NUEVO**, y lo destapa el acto
   25. La vara del acta 54 pregunta 1 esta escrita para el acto con **UNA** puerta. Hay al menos dos
   salidas imaginables y **ninguna esta escrita**: fundir moviendo antes el puente o la semilla al
   superviviente, o dejar el par como enlace permanente. **No se elige aqui.**
6. **HEREDADOS Y SIN CAMBIO HOY**: el esquema de `OPERACIONES.jsonl` **sigue sin distinguir
   ejecutada de pendiente** (71 en `LISTA`, medido hoy) y el campo `orden` de la fase 03 **sigue sin
   ser su criterio de orden**.

---

## 14. LO QUE ESTA VUELTA NO HIZO, DICHO EN VEZ DE CALLADO

1. **NO FUNDIO LOS SEIS ACTOS DECLARADOS DEL TRAMO 4** (11, 13, 14, 24, 25 y 31). **Es el
   incumplimiento de la vuelta y va el primero.** Los seis estan vivos al cerrar, en los puestos
   **20 a 25** de la nomina del cierre.
2. **NO TOCO LOS DIECINUEVE VIVOS DE LOS TRAMOS 1, 2 Y 3.** Siguen en los puestos **1 a 19**,
   medido.
3. **NO ABRIO EL TRAMO 5.** Al cerrar quedan **96 actos CERRADOS** en la nomina, de los que **25**
   son los vivos de los cuatro tramos, asi que **quedan 71 sin tocar**.
4. **NO CORRIGIO LAS ONCE CITAS HEREDADAS** que su propio instrumento nuevo encontro (`D7`), ni la
   seccion PASO 3 de `RECOMPUTO_3388.md` (`D6`).
5. **NO EJECUTO NINGUNA ARISTA NI PODA DE SOLAPES**: son de la fase 04.
6. **NO RESOLVIO LAS DUPLICADAS HISTORICAS** (955 grupos sobre 753 nodos al cierre) ni el alias
   durmiente `modelo_spin_2`: son de `OP-S-12`.
7. **NO CORRIO LA VARA 2 DE `verificar_mapas_destejido.py`**: no hay mapa de particion nuevo que
   pasarle, y se dice en vez de dejar creer que se corrio entera.

---

## 15. LAS PREGUNTAS PARA EL AUDITOR

1. **Cuando la PIEZA DECLARADA y un CONTEO de contenido apuntan a lados distintos, quien gana?**
   (`D3`.) El acta 53 pregunta 3 dice *lo declarado*; el acta 50 adjudicacion 3 dice *la
   aritmetica*. **Segui lo declarado, cuatro veces.** Si la vara es la otra, hay cuatro fusiones que
   deshacer como el 23 de la vuelta 55.
2. **Se puede romper un empate TRIPLE contando las LINEAS PROPIAS DECLARADAS de cada lado?** (`D4`.)
   **Lo hice en el acto 32**, una linea contra dos. Con la lectura contraria ese acto seria el
   septimo declarado.
3. **Que se hace con un acto CERRADO cuyos DOS miembros son PUERTA?** (Pendiente 5, acto 25.) **No
   lo elegi**: lo declare con las dos salidas imaginables nombradas.
4. **Cuando la GUARDA 1B y la RAZON DECLARADA piden supervivientes distintos, basta con que lo que
   la razon prefería viaje entero en el reparto?** (`D5`, actos 38 y 43.) **Lo di por bastante**, y
   lo medi pieza a pieza.
5. **Una cifra con su CORTE DECLARADO exime de recomputar, o solo de recomputar en silencio?**
   (`D6`.) **La deje intacta** por el limite que el propio barrido `9.10` nombra, pero mi vuelta la
   movio.
6. **Que se hace con las ONCE citas heredadas envejecidas que el instrumento nuevo encontro?**
   (`D7`.) **Las publique enteras sin corregirlas**, porque el encargo nombraba tres sitios. La
   pregunta es si el atraso se vacia de una vez, se reparte por vueltas, o se declara como pasivo
   de una operacion con nombre.
