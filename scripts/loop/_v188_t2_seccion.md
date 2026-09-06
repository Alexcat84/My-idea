### TAREA 2. EL PLAN: LAS CUATRO FICHAS, RESUELTAS CONTRA SU EVIDENCIA. CERRADA CON UNA PARADA DENTRO

**LA VARA CORRIDA CON MI PROPIO CORTE, NO CON EL DEL ACTA.**
`python scripts/loop/vuelta150_3_relectura_expediente.py --corte 5aa9305df3ceb438f92011d1b9e973c58277c6fe`,
que es el HEAD de apertura sellado en `docs/loop/SALIDA_V188_HEAD_APERTURA.txt`.
Salida entera: `docs/loop/SALIDA_V188_T2_VARA_APERTURA.txt`, exitcode **0**. Sus
cifras, contadas de ese fichero:

- `CIFRA fichas del expediente: 71 operaciones`
- `CIFRA fichas que no calzan: 37 operaciones`
- `CIFRA fichas congeladas declaradas: 24 operaciones`
- `CIFRA fichas congeladas en silencio: 12 operaciones`
- `CIFRA fichas HECHA sin ninguna prueba: 1 operaciones`
- **`CIFRA fichas en LISTA sin ninguna prueba: 6 operaciones`**
- **`CIFRA de esas que estan CONSUMIDAS por otra ficha: 2 operaciones`**
- **`CIFRA de esas que son TRABAJO REAL: 4 operaciones`**

**Reproduce lo que el acta 188 publica en su punto 12 con otro corte**, y las
cuatro son **`OP-L-01`, `OP-L-02`, `OP-L-03`** (09_LECTURAS_DIRIGIDAS) y
**`OP-I-01`** (10_INVENTARIO). **Las cuatro son de tipo `MESA`**, contado del
expediente, y **dos tienen `depende_de` vacio**: `OP-L-01` y `OP-I-01`.

#### 2.a LA VARA GANA SU PATA DOCUMENTAL, Y ES CODIGO

**EL HUECO, QUE ES DE FORMA Y NO DE CIFRA.** Las tres pruebas de la vara son **de
grafo, de codigo y de git**, y las tres preguntan por una huella que una `MESA`
no deja: **una mesa produce documentos**. Preguntarle al grafo si una mesa se hizo
es preguntarle a la fuente equivocada, que es la caida escrita en el recuadro de
`AUDITOR.md` 0.

**QUE SE ANADIO EN `scripts/loop/vuelta150_3_relectura_expediente.py`:** tres
funciones (`rutas_de_la_evidencia()`, pura; `localizar_evidencia()`, el unico
lector de disco; y `p4_vara_documental()`) y **un bloque de salida que va DESPUES
de la cifra vieja y no en su lugar**. Para las fichas que no son `MESA` **no
cambia absolutamente nada**: la P4 no se computa y **la ficha ni siquiera aparece
en el diccionario**.

**LAS DOS CIFRAS, JUNTAS Y CON SU DIFERENCIA NOMBRADA**, contadas de
`docs/loop/SALIDA_V188_T2_VARA_CON_PATA.txt`:

- **CIFRA VIEJA, identica a la de siempre: 6 fichas en LISTA sin ninguna de las
  tres pruebas, de las cuales 4 son TRABAJO REAL.**
- **CIFRA NUEVA: de esas 4, 3 son mesas cuyo producto documental SI existe en
  disco, y 1 no lo tiene.**
- **LA DIFERENCIA SON 3 fichas, y no significa que su mesa se hiciera bien:**
  significa que el documento que su propia evidencia nombra **esta**. Si cubre lo
  que la ficha describe **es lectura, y la vara no la hace**.
- `CIFRA fichas de tipo MESA en el expediente: 6` | `CIFRA de esas que estan en
  LISTA: 5`.

**ARNES OBLIGATORIO, Y NACE EN ESTA VUELTA:**
`scripts/loop/vuelta188_tarea2_mutacion_pata_documental.py`. Salida:
`docs/loop/SALIDA_V188_T2_MUTACION_PATA_DOCUMENTAL.txt`, **`CIFRA casos: 11 |
pasan: 11`**, **`CIFRA casos que CAEN al mutar su esperado: 11 de 11`**, **`CIFRA
fallos: 0`**, **`VEREDICTO: VERDE`**, exitcode **0**. Cinco casos: **(A)** la P4
no existe para una ficha que no es `MESA`, y eso es de FORMA; **(B)** una mesa con
fichero que existe sale con su medicion por las dos convenciones, y el fichero se
fabrica **con CRLF a proposito** para que las dos no sean el mismo numero (**disco
23, LF 21**); **(C)** una mesa cuyo fichero no existe sale vacia, o sea **la P4 no
inventa un documento que no esta**; **(D)** una mesa cuya evidencia es prosa
entera sale vacia **pero con 0 menciones**, y esa diferencia con la (C) es medible
sin tocar disco; **(E)** el extractor no traga prosa con puntos, ni versiones, ni
extensiones fuera de la lista. **El temporal se limpia** (`P.16`).

#### 2.b EL PRODUCTO DE CADA UNA, MEDIDO CONTRA LA `evidencia` QUE ELLA NOMBRA

Instrumento: `scripts/loop/vuelta188_tarea2_evidencia_de_las_fichas.py`. Salida:
`docs/loop/SALIDA_V188_T2_EVIDENCIA_DE_LAS_FICHAS.txt`, exitcode **0**. Toda cifra
de esta seccion sale de ese fichero.

| ficha | lo que su `evidencia` nombra | existe | disco | LF |
|---|---|---|---|---|
| `OP-L-01` | `LECTURAS_DIRIGIDAS.md` | SI, en `docs/plan/LECTURAS_DIRIGIDAS.md` | 214916 | 214916 |
| `OP-L-01` | `INTRA_DOMINIO_INFORME.md` | SI, en `docs/INTRA_DOMINIO_INFORME.md` | 943970 | 943970 |
| `OP-L-01` | `BANCO_DE_TEXTOS.md` | SI, en `docs/BANCO_DE_TEXTOS.md` | 182228 | 182228 |
| `OP-L-02` | (su evidencia entera es prosa: 0 menciones de fichero) | NO HAY QUE MEDIR | | |
| `OP-L-03` | `BANCO_DEL_PLAN.md` | SI, en `docs/plan/BANCO_DEL_PLAN.md` | 61554 | 61554 |
| `OP-L-03` | `LECTURAS_DIRIGIDAS.md` | SI, en `docs/plan/LECTURAS_DIRIGIDAS.md` | 214916 | 214916 |
| `OP-I-01` | `INVENTARIO.jsonl` | SI, en `docs/plan/INVENTARIO.jsonl` | 584554 | 584554 |
| `OP-I-01` | `10_INVENTARIO.md` | SI, en `docs/plan/10_INVENTARIO.md` | 34258 | 33845 |

**Y ese ultimo es el unico de los siete cuyas dos convenciones NO son el mismo
numero**, que es exactamente el motivo por el que se miden las dos y no se
suponen.

**LO QUE LA FICHA PROMETE CONTRA LO QUE HAY, RECOMPUTADO Y NO CREIDO AL ACTA:**

- **`OP-L-01` describe once lecturas** (su `adjudicacion` dice literalmente
  *"TANDA DE ONCE LECTURAS DIRIGIDAS"* y su `nota` enumera **11** etiquetas,
  `LD-01` a `LD-11`). `docs/plan/LECTURAS_DIRIGIDAS.md` mide **214916 bytes por
  las dos convenciones**, `sha256` LF `dda1cdd67042c733` y **2230 lineas**. **Las
  once estan en cabecera: 11 de 11.** Y el documento ha crecido muy por encima:
  **68 etiquetas distintas por toda aparicion** y **60 en cabecera**.
- **`OP-I-01` promete 323 entradas**, leido de su propio texto. `INVENTARIO.jsonl`
  tiene **672 entradas no vacias**, las **672 JSON valido**: **+349**. El reparto
  por tipo, contado del fichero: **acto 556, familia_de_ids 54, figura 20, defecto
  19, racimo 13, dominio 10**.

**Y AQUI VA UN CONTRASTE CONTRA EL ACTA QUE SE DECLARA EN VEZ DE RESOLVERSE
COPIANDO** (`EJECUTOR.md` 2). El acta 188 punto 12 dice que el documento lleva
etiquetas *"de `LD-01` hasta `LD-98`"*. **Mi medicion de hoy da como maximo
`LD-154`.** **Ninguna de las dos cifras es falsa, y lo compruebo con su linea:**
`LD-98` esta en cabecera en la **1953** y `LD-154` en la **662**. **El documento
no numera en orden de posicion**, asi que el mayor por numero y el mayor por
posicion no son el mismo. Se dicen los dos.

#### 2.c EL DESFASE DE LOS CORTES, MEDIDO Y NO REPARADO

| ficha | `fecha_corte` | marcador que cita | de que frase sale | hoy | desfase |
|---|---|---|---|---:|---:|
| `OP-L-01` | 2026-08-11 | 2.117 | *"marcador del cribado no se mueve: sigue en 2.117"* | 3388 | +1271 |
| `OP-L-02` | 2026-08-11 | 2.117 | *"marcador del cribado no se mueve: sigue en 2.117"* | 3388 | +1271 |
| `OP-L-03` | 2026-08-11 | 2117 | *"corte puesto 2117"* | 3388 | +1271 |
| `OP-I-01` | 2026-08-11 | 2117 | *"corte del puesto 2117"* | 3388 | +1271 |

**LA FRASE DE LA QUE SALE CADA CIFRA VA PUBLICADA, Y NO ES ADORNO.** El primer
patron que escribi (`sigue en (\d+)` a secas) daba **671** para `OP-I-01`, que
**no es un marcador**: es la frase *"el archivo sigue en 671 lineas"* hablando del
propio inventario. **Contar bien un patron y atribuirlo al sujeto equivocado es la
caida del recuadro de `AUDITOR.md` 0**, y por eso el patron lleva su contexto y la
salida publica la frase.

**EL HUECO MAYOR QUE `OP-I-01` NOMBRA, COTEJADO CONTRA EL ARCHIVO DE HOY.** La
ficha dice *"CUATRO DOMINIOS no han entrado al cribado intra (quality 792,
health_safety 283, risk_management 55 y seguridad_digital 55), o sea 1.185 nodos
vivos, un tercio del catalogo"*. Hoy el archivo tiene **10 dominios distintos** y
esos cuatro traen **quality 844, health_safety 192, risk_management 106 y
seguridad_digital 27** pares. **`CIFRA de los cuatro que HOY siguen sin un solo
par en el archivo: 0`.** **Se mide y se publica. La ficha NO se reescribe: eso es
plan, y si hace falta, se trae.**

#### 2.d EL ESTADO DE CADA UNA, EN UNA DE LAS TRES FORMAS Y EN NINGUNA OTRA

- **`OP-L-01` -> (a) SU PRODUCTO ESTA Y LA CUBRE.**
  `docs/plan/LECTURAS_DIRIGIDAS.md` existe (**214916 bytes por las dos
  convenciones**) y trae **en cabecera las 11 de 11** que la ficha describe.
- **`OP-L-02` -> (c) NO HAY EVIDENCIA QUE LA DECIDA. ES PARADA Y SE TRAE.** Su
  `evidencia` entera es una sola linea de prosa (*"MEDIDO el 11 ago 2026: 205
  pares fuera de cola, 11 leidos, 194 pendientes"*) y **no nombra ningun
  fichero**, asi que **no hay documento que medir**. Su `verificacion` habla de
  *"las tres nominas afectadas"* y de *"cada grupo del backlog"*, y **ninguna de
  las dos cosas tiene sede declarada en la ficha**. **No se inventa una.**
- **`OP-L-03` -> (b) SU PRODUCTO ESTA PERO NO LA CUBRE.** Sus dos ficheros existen
  (`docs/plan/BANCO_DEL_PLAN.md`, **61554 bytes**, y
  `docs/plan/LECTURAS_DIRIGIDAS.md`, **214916 bytes**), pero **lo que falta
  exactamente** es esto: la ficha describe **55 lecturas repartidas en 29 actos** y
  su `evidencia` dice *"LECTURAS_DIRIGIDAS.md, el reparto por acto"*, y **contar
  "el reparto por acto" no es contar un fichero**: no hay cifra que cotejar contra
  las 55.
- **`OP-I-01` -> (a) SU PRODUCTO ESTA Y LA CUBRE.** `INVENTARIO.jsonl` existe
  (**584554 bytes por las dos convenciones**) con **672 entradas, las 672 JSON
  valido**, contra las **323** que promete: **+349**. Y `10_INVENTARIO.md`, la
  vista humana, tambien esta (**34258 en disco y 33845 normalizados a LF**).

**CIFRA en la forma (a): 2 | en la forma (b): 1 | en la forma (c), o sea PARADA:
1.**

#### 2.e LO QUE ESTA TAREA NO HA TOCADO, MEDIDO AL TERMINAR

**El campo `estado` de las cuatro sigue como estaba**: `OP-L-01=LISTA`,
`OP-L-02=LISTA`, `OP-L-03=LISTA`, `OP-I-01=LISTA`. `docs/plan/OPERACIONES.jsonl`
mide al terminar **498085 bytes en disco y 498085 normalizados a LF**, `sha256` LF
`bbdde43a00bdc35c`, **identico al de la apertura de la tarea**.
`docs/INTRA_DOMINIO_VEREDICTOS.jsonl` cierra la tarea en `sha256` LF
`0a77b5a35a962621`, **el mismo con el que abrio la vuelta**. **Ninguna clase se ha
decidido y ningun veredicto se ha movido.**
