# REPORTE DE LA VUELTA 65 (20 ago 2026, ejecutor Opus 5)

**LO PRIMERO, PORQUE ES LO QUE LA VUELTA ENCUENTRA Y NO LO QUE ENTREGA: EL PRIMER ACTO DEL PREFIJO DEL
TRAMO UNICO DE `OP-U-02` NO SE PUEDE FUNDIR, Y LA LETRA QUE LO DICE YA ESTABA ESCRITA.** El acto 1
tiene **quince miembros, DIEZ pares `D` internos, TRES nodos puente y SEIS triangulos puente**, y
`P.10` del banco del plan dice con todas sus letras que **una componente con un nodo puente NO SE
FUNDE hasta que ese triangulo se cierre**. Va **`DECLARADO Y NO FUNDIDO` con motivo sellado**, y es
**la primera vez que la campana declara un acto por `P.10`**. **NO ES UNA PARADA**: el lote se entrega
entero.

**LO SEGUNDO: EL ACTO 3 SE FUNDE, Y ES LA PRIMERA FUSION DE MAS DE DOS MIEMBROS DE LA CAMPANA.** Diez
nodos de Deming a uno, **58 piezas repartidas sobre NUEVE absorbidos** y **trece perdidas selladas en
campo propio**.

**LO TERCERO, Y VA ANTES QUE EL RESTO PORQUE SIN ELLO NADA DE LO ANTERIOR HABRIA PODIDO CORRERSE: LOS
DOS INSTRUMENTOS DE TRAMO NO PODIAN CORRER SOBRE `OP-U-02` Y ESTA MEDIDO, NO SUPUESTO.** Corridos tal
cual, `dossier_del_tramo.py` y `generar_plan_del_lote.py` daban los dos
`ROJO: el fichero del tramo tiene 0 claves de ordinal ([]). PARADA`. Se corrigen **por correccion
declarada con el texto viejo citado verbatim y con caso positivo de no regresion**, y **las dos
correcciones van marcadas discutibles**.

**LA TAREA 1 VA ENTERA:** el registro del acta 64 adosado con **las 37 citas cotejadas antes de
escribir**, y **la aguja del comprobador de promesas ensanchada** con caso positivo en dos mitades.

**LA FECHA ESTA MEDIDA POR DOS RELOJES Y NO SUPUESTA:** `date` da `2026-08-20` y
`git log -1 --date=format:'%Y-%m-%d'` da `2026-08-20`. Es la misma medicion que el campo `fecha` del
plan sellado, que la lee del reloj y no de una constante.

**LA RACHA DE REPORTE VENIA EN UNO** (acta 64, linea **16989**). **Esta vuelta no publica ninguna
cifra tomada de una corrida que no sea la suya**, y las **CINCO** averias propias que si hubo estan
enteras en la seccion 7, **todas cazadas antes de que llegaran a una cifra publicada**.

| | |
|---|---|
| **rama** | `pasada-unica` |
| **hash de apertura** | `b93c28f6` (el commit del acta 64), **arbol limpio y todo pusheado; la regla 3 se cumplio POR VACIO y se dice asi en vez de darla por cumplida** (`git status --porcelain` VACIO, comprobado) |
| **hash final** | el commit de este reporte, **pusheado a `origin/pasada-unica`**, mas el ultimo, que **solo escribe esta celda y la de abajo** porque el commit del reporte no podia contener su propio hash |
| **commits de la vuelta** | **8**, leidos de `git log --format=%h b93c28f6..HEAD`: `7897d0e8` (apertura medida), `ae539bb5` (TAREA 1 entera), `c8c6b685` (correccion de los dos instrumentos de tramo), `1ac8c2c4` (la lectura `P.5` y `P.10` del tramo), `a0d6873c` (el LOTE A ejecutado), `778815fd` (el registro del tramo), `a1ca38d0` (medicion de cierre y el `AMBAR` rotulado), mas el de este reporte **y el que escribe esta celda** |
| **arbol al cierre** | limpio tras el commit del reporte |

---

## 0. LA APERTURA Y EL CIERRE, LA TABLA TALLADA POR INSTRUMENTO (regla 1)

**NINGUNA CELDA ESTA TECLEADA:** sale entera de
`python scripts/loop/tallar_cabecera_reporte.py --vuelta 65`
([`SALIDA_V65_TALLAR_CABECERA.txt`](SALIDA_V65_TALLAR_CABECERA.txt)). **Las dos columnas se leen de
ficheros DISTINTOS.**

| | **apertura**, antes de la 1.ª operacion | **cierre, RECOMPUTADO al cierre** |
|---|---:|---:|
| marcador `A` / `B` / `C` / `D` | 551 / 72 / 5 / 2.760 | **551 / 72 / 5 / 2.760** |
| `n`, huecos, duplicados | 3.388 / 0 / 0 | **3.388 / 0 / 0** |
| grafo: ficheros / vivos / deprecados / enlaces | 3.853 / 3.271 / 582 / 17.496 | **3.853 / 3.262 / 591 / 17.511** |
| retrato: `A` crudas / colapsos / pares distintos | 551 / 278 / 273 | **551 / 292 / 259** |
| actos (componentes) | 79 | **78** |
| actos `CERRADOS` / `ABIERTOS` | 26 / 53 | **26 / 52** |
| nodos en `CERRADOS` / `ABIERTOS` | 61 / 240 | **61 / 230** |
| cola de costuras | 1.455 | **1.453** |
| colisiones de clase vigentes | 2 | **2** |
| auto-pares (los dos lados al mismo vivo) | 256 | **257** |
| duplicadas historicas: grupos / nodos | 925 / 733 | **921 / 730** |
| operaciones, estados, dependencias rotas | 71, todas `LISTA`, 0 | **71, todas `LISTA`, 0** |
| entradas del inventario | 672 | **672** |
| las cuatro comprobaciones de `08_VERIFICACION` | TODAS OK (301 igual a 301; 273 igual a 273) | **TODAS OK (291 igual a 291; 259 igual a 259)** |

**LA APERTURA CALZA AL DIGITO CON EL CIERRE QUE EL ACTA 64 MIDIO POR CORRIDA PROPIA**, y eso es
contraste, no fuente: marcador, cola, colisiones y duplicadas dan **`diff` VACIO**, el estado difiere
solo en la etiqueta y el recomputo en **UNA linea**, la de la ruta del `--salida`. **EL BARRIDO
DIFIERE EN UN FICHERO BARRIDO** (422 contra 421) **y la causa esta medida, no supuesta**:
`git diff --name-status 10186e4f b93c28f6` sobre las cuatro carpetas barridas da **UN solo `.py`
anadido**, `docs/loop/_auditor_v64_cuenta.py`, el que el auditor committeo con su acta; `ROJO` 32,
`AMBAR` 0, `ROTULADO` 37, `CENSO` 219 e `ILEGIBLE` 1 salen **identicos**.

Instrumentos de apertura corridos **ANTES de la primera operacion y con el arbol limpio**:
[`SALIDA_V65_APERTURA.txt`](SALIDA_V65_APERTURA.txt),
[`SALIDA_V65_MARCADOR_APERTURA.txt`](SALIDA_V65_MARCADOR_APERTURA.txt),
[`SALIDA_V65_RECOMPUTO_APERTURA.txt`](SALIDA_V65_RECOMPUTO_APERTURA.txt),
[`SALIDA_V65_COLA_APERTURA.txt`](SALIDA_V65_COLA_APERTURA.txt),
[`SALIDA_V65_COLISIONES_APERTURA.txt`](SALIDA_V65_COLISIONES_APERTURA.txt),
[`SALIDA_V65_DUPLICADAS_APERTURA.txt`](SALIDA_V65_DUPLICADAS_APERTURA.txt) y
[`SALIDA_V65_BARRIDO_APERTURA.txt`](SALIDA_V65_BARRIDO_APERTURA.txt). **Las dos que reescriben sus
ficheros salieron IDEMPOTENTES**, verificado por `git status`, que no listo **ni un fichero rastreado
modificado**.

**LA MEDICION DE CIERRE SE RE-CORRIO DESPUES DE ESCRIBIR LOS REGISTROS**, que es lo que la regla 1
manda: la cabecera de arriba es la ULTIMA medicion y no una heredada.

**LAS CELDAS QUE SE MUEVEN, TODAS PREDICHAS POR LA UNICA FUSION DE LA VUELTA, que absorbe NUEVE
nodos:** vivos bajan **9**, deprecados suben **9**, colapsos suben **14** (son los 14 pares `A`
internos del acto, que pasan a auto-arista), pares distintos bajan **14**, actos bajan **1**,
`ABIERTOS` bajan **1** y nodos en `ABIERTOS` bajan **10**, auto-pares suben **1** (los 14 veredictos
colapsan en UN solo grupo resuelto) y duplicadas bajan **4 grupos** y **3 nodos**, que es lo que
`P.16` limpio.

**LAS DOS CELDAS QUE NO SE MUEVEN ASI, MEDIDAS Y NO SUPUESTAS:**

1. **LOS ENLACES SUBEN 15** (17.496 a 17.511). El superviviente hereda los vecinos de los nueve que
   mueren por la simetrizacion del paso 5 de Gate 0, la fusion dedupica por literal y `P.16` retira
   seis duplicadas: el saldo no es multiplo de nada y por eso se publica medido.
2. **LAS COLISIONES DE CLASE VIGENTES SE QUEDAN EN 2, QUE ES LA LINEA BASE DECLARADA** (acta 64,
   pregunta 3). **Son las dos de la mesa `OP-M-03` y NO SE HAN TOCADO.** La cuenta esperada se midio
   **ANTES de fundir** y dio **cero nuevas**; el censo de cierre con `--esperadas 2` da **MEDIDA 2,
   CALZA SI**.

**TASA POR DOMINIO AL CIERRE**, leida de
[`SALIDA_V65_MARCADOR_CIERRE.txt`](SALIDA_V65_MARCADOR_CIERRE.txt): compras 0,6 (n 155) | core 22,5
(n 1.445) | entrega 1,2 (n 171) | environmental 16,5 (n 170) | exportacion 11,5 (n 130) | franquicias
10,1 (n 148) | health_safety 22,4 (n 192) | quality 14,1 (n 844) | risk_management 0,0 (n 106) |
seguridad_digital 11,1 (n 27). **IDENTICA a la de la apertura al digito: fundir no voltea
veredictos.**

---

## 1. TAREA 1.a: **EL REGISTRO DEL ACTA 64, CON LAS TREINTA Y SIETE CITAS COTEJADAS ANTES DE ESCRIBIR**

Va al final de [`docs/plan/03_FUSIONES.md`](../plan/03_FUSIONES.md), **adosado y SIN reescribir una
sola linea de arriba** (**+119 lineas y CERO borradas**, medido con `git diff --numstat`). Lo escribe
`python scripts/loop/vuelta65_registrar_acta64.py`
([`SALIDA_V65_REGISTRO_ACTA64.txt`](SALIDA_V65_REGISTRO_ACTA64.txt)), que **cae en `ROJO` sin escribir
si una sola de las 37 citas no calza**: salieron **37 cotejadas, 0 malas**. **La guarda de
idempotencia MUERDE**: la segunda corrida dice *YA ADOSADA* y no escribe. **Las 8 sedes de arriba
siguen en su linea tras adosar**, re-cotejadas.

**LO QUE SE REGISTRA, que es exactamente lo que el encargo pedia:** los nueve discutibles con su vara
citada linea a linea; **el carril de las dos colisiones con la mesa `OP-M-03` como duena nombrada y
la linea base del censo en `2`**; **la regla de no apilar mas de un `INCISO`**; **la caida de reporte
`7.1` con su nombre y la racha en uno**; y **las respuestas de las preguntas 4 y 7, registradas y no
encargadas**, mas una nota que dice donde quedaron las otras cinco para que no parezca omision.

### 1.1 **UNA DIVERGENCIA DECLARADA EN VEZ DE RESOLVERSE COPIANDO, Y VA MARCADA COMO DISCUTIBLE**

**El mensaje del commit del acta 64 y el encargo de esta vuelta dicen los dos NUEVE discutibles
`A FAVOR`**, con el parentesis *el `D5` registrado como caida de procedimiento autodeclarada*. **El
TEXTO del acta, que es la vara, NO adjudica el `D5` `A FAVOR`**: su linea **16876**, leida hoy, abre
diciendo *caida de procedimiento del ejecutor, autodeclarada, registrada en la seccion 3*.

**Registro OCHO `A FAVOR` y UNO como caida**, y **el texto del resumen del commit queda entero y sin
tachar como contraste** (regla 2: si discrepan, la discrepancia se declara en vez de resolverse
copiando). **Ninguna de las dos lecturas mueve una sola cifra ni un solo dato**: el `D5` esta
registrado en las dos y lo unico que cambia es el rotulo con que se le nombra. **Es el `D1` de la
seccion 6.**

---

## 2. TAREA 1.b: **EL ENSANCHE DE LA AGUJA DEL COMPROBADOR DE PROMESAS**

**LO PRIMERO FUE MEDIR SI EL ENSANCHE DESTAPABA UNA PROMESA INCUMPLIDA HOY INVISIBLE**, porque el acta
64 mandaba **PARAR** si asi era. **Barridos los 62 `PLAN_*.json` de `docs/loop`, la forma plural
aparece en UNO solo** (`PLAN_V64_OPM03II.json`, acto 1, `nota_del_reparto`) **y ESE MISMO campo ya
trae la singular**. **CERO promesas nuevas y CERO incumplidas destapadas: NO HAY PARADA**, y el
ensanche no es regresion ni hallazgo, es aguja.

**LA CORRECCION VA DECLARADA EN EL DOCSTRING con el texto viejo citado verbatim** (*Cuenta como
PROMESA la frase VA MARCADO COMO DISCUTIBLE, comparada sin distinguir mayusculas*) **y no se quita
nada**: la constante vieja `PROMESA` conserva su nombre y su valor, se anade `PROMESA_PLURAL` y las
dos entran juntas en `FORMAS`. **Un campo con CUALQUIERA de las dos formas, o con las dos, cuenta como
UNA sola promesa**, que es lo que deja el conteo viejo intacto. El instrumento **imprime ahora sus dos
agujas y la forma hallada en cada fila**, para que la vara no dependa del docstring.

### 2.1 El caso positivo, **en las dos mitades que el encargo pide**

`python scripts/loop/vuelta65_caso_positivo_promesas.py`
([`SALIDA_V65_CASO_POSITIVO_PROMESAS.txt`](SALIDA_V65_CASO_POSITIVO_PROMESAS.txt)), **VERDE**:

| mitad | que mide | resultado |
|---|---|---|
| **NO REGRESION** | las corridas selladas de las vueltas **63** y **64**, re-corridas con la aguja ensanchada **contra el reporte de SU PROPIA vuelta** | **2 de 2** y **2 de 2 CUMPLIDAS**, `exit 0`, **identicas al digito** a `SALIDA_V63_PROMESAS_CUMPLIDAS.txt` y `SALIDA_V64_PROMESAS_CUMPLIDAS.txt` |
| **VISIBILIDAD** | un **plan de mentira** con la nota **SOLO en plural** | la aguja **VIEJA ve 0**; la **NUEVA ve 1**, y sale **`INCUMPLIDA` con `exit 1`** porque la seccion 6 no nombra ese acto inventado |

**DOS COSAS QUE ESE CASO POSITIVO HACE Y SE DICEN PORQUE SON LA MITAD DE SU VALOR.** La primera: **el
reporte de cada vuelta se saca de `git`, no se recuerda**, porque `docs/loop/REPORTE.md` se sobrescribe
cada vuelta; sin eso la mitad 1 estaria comparando contra el reporte equivocado. La segunda: **la
aguja vieja NO se re-teclea**, se reconstruye del propio instrumento quitandole la forma plural, asi
que si manana alguien cambia la constante la prueba cambia con ella. **El plan de mentira se BORRA
tras la prueba y el borrado se comprueba e imprime.**

**CENSO DE PLANTILLAS TRAS EL ENSANCHE: CERO TALLADOS en los 22 instrumentos de nombre estable**
([`SALIDA_V65_CENSO_PLANTILLAS_TAREA1.txt`](SALIDA_V65_CENSO_PLANTILLAS_TAREA1.txt)).

---

## 3. TAREA 2, PASO PREVIO: **LOS DOS INSTRUMENTOS DE TRAMO NO PODIAN CORRER SOBRE `OP-U-02`**

**MEDIDO ANTES DE TOCAR NADA Y NO SUPUESTO.** Corridos tal cual sobre
`docs/loop/TRAMO_UNICO_OPU02_V64.jsonl`, **los dos** dan la misma linea:

```
ROJO: el fichero del tramo tiene 0 claves de ordinal ([]). PARADA.
```

La clave del tramo unico es `orden_universo` y **los dos solo conocian `orden_tramo`**. Y el generador
tenia ademas **una segunda averia mas grave, que no para sino que MIENTE**: su linea
`ab = [x for x in mi if x != sup][0]` **habria sellado el acto 1, de quince miembros, con UN solo
absorbido y los otros TRECE desaparecidos en silencio**. **El fundidor `fundir_por_plan.py` YA era
N-ario**, medido leyendo su bucle `for muere in abs_`: lo unico que faltaba era que el generador
supiera sellarlo.

**SE CORRIGEN POR CORRECCION DECLARADA, que es el carril con el que la vuelta 63 corrigio la cabecera
de ESTE MISMO generador** (banco `9.10`), **con el texto viejo citado VERBATIM en el sitio donde
muerde y enumerado en el docstring**, y **las dos van MARCADAS DISCUTIBLES** por las dos condiciones
del acta 61 (`D2` y pregunta 2). **El titulo del generador, que decia `OP-U-01`, tambien se corrige
con su texto viejo citado.** En el dossier, ademas, **un acto de mas de dos publica ahora la razon de
CADA par interno** en vez de decir `NO ENCONTRADO`, que es lo que su propio docstring ya prometia.

### 3.1 El caso positivo, y **su vara esta declarada porque la primera que eligi era mala**

`python scripts/loop/vuelta65_caso_positivo_generador.py`
([`SALIDA_V65_CASO_POSITIVO_GENERADOR.txt`](SALIDA_V65_CASO_POSITIVO_GENERADOR.txt)), **VERDE**:

| mitad | resultado |
|---|---|
| **NO REGRESION DEL GENERADOR** | el **ANCESTRO** (sacado de `git ae539bb5`) y el **CORREGIDO**, los dos **HOY**, sobre el **mismo** tramo de dos miembros vivos y el **mismo** contenido: **0 campos distintos** salvo la fecha |
| **NO REGRESION DEL DOSSIER** | ancestro contra corregido, los dos hoy: **0 lineas distintas** |
| **QUE LA CORRECCION SIRVA** | las dos ramas nuevas **dejan de caer** por el ordinal, y **la guarda del acto de mas de dos SIN reparto MUERDE** sobre el acto 1 de quince miembros |

**POR QUE NO SE COMPARA CONTRA LAS SALIDAS SELLADAS DE LAS VUELTAS 61 Y 62, dicho porque fue mi primer
intento y dio ROJO:** los nodos del tramo 6 de `OP-U-01` **se fundieron en la vuelta 62 y hoy estan
deprecados y con otro texto**, asi que esa comparacion mide **el movimiento del ARBOL** y no el de la
correccion (dio **808 lineas distintas** y dos re-generaciones imposibles). **La comparacion que si
aisla la correccion es ancestro contra corregido sobre el mismo arbol**, y es la que queda. Esta en
la seccion 7.

**Y ESE CASO POSITIVO YA MORDIO UNA VEZ, que es lo que lo hace creible:** ver la seccion **7.2**.

---

## 4. TAREA 2: **LA LECTURA `P.5` DEL TRAMO Y SU MITAD DIAGNOSTICA `P.10`**

**En `OP-U-01` la componente ERA el par y la pregunta de `P.5` se contestaba leyendo ese par. Aqui los
actos van de 3 a 15 miembros, y ahi manda `P.10`**, que dice con todas sus letras:

> **UN NODO PUENTE es el que tiene `A` con dos nodos que entre si son `D`.** La componente que forma
> puede ser **UNA familia o DOS pegadas por el**, y **el cierre transitivo no lo distingue**.
> **Si aparece, la componente NO se funde hasta que ese triangulo se cierre.**
> **LO QUE NUNCA ES SALIDA: fundir la componente entera porque el cierre transitivo la junta. El
> cierre transitivo no lee: cuenta.**

**MEDIDO SOBRE LOS 47 ACTOS** con `python scripts/loop/vuelta65_puentes_del_tramo.py`
([`SALIDA_V65_PUENTES_TRAMO.txt`](SALIDA_V65_PUENTES_TRAMO.txt)), con los ids pasados por el resolutor
(`P.1`), **cuya maquina se copia de `scripts/plan/aristas_duplicadas_tras_resolver.py` lineas 38 a 46
para que dos instrumentos de la campana no resuelvan distinto en silencio**:

| | |
|---|---:|
| actos mirados | **47** |
| **actos CON al menos un nodo puente** | **9** (los actos **1, 10, 11, 17, 20, 21, 23, 24 y 27**) |
| actos SIN ningun nodo puente | **38** |
| actos con algun par SIN veredicto escrito | **47** |

**ESTO NO ES UN HALLAZGO SOBRE EL ACTO 1: ES SOBRE EL TRAMO ENTERO.** Nueve de los cuarenta y siete
actos que quedan de `OP-U-02` **no se pueden fundir enteros mientras su triangulo no se cierre**, y
eso cambia la forma de lo que queda de la operacion. **Se publica ahora y no cuando llegue su turno.**

---

## 5. TAREA 2: **EL LOTE A, DECLARADO AL ABRIRLO Y ENTREGADO ENTERO**

**EL LOTE ES PREFIJO SIN SALTOS del `orden_universo`: LOS ACTOS 1 Y 3**, que son los dos primeros del
tramo fijado. **Los dos CIERRAN ENTEROS**: el 1 `DECLARADO Y NO FUNDIDO` y el 3 **FUNDIDO**.

### 5.1 **EL ACTO 1: `DECLARADO Y NO FUNDIDO` POR `P.10`**

| | |
|---|---:|
| miembros | **15**, y **ninguno se toca** |
| combinaciones internas | 105 |
| pares `A` internos | 20 |
| **pares `D` internos** | **10**, leidos y declarados DISTINTOS |
| pares sin veredicto escrito | 75 |
| **NODOS PUENTE** | **3** |
| **TRIANGULOS PUENTE** | **6** |

`errores_como_consecuencia` hace de puente en **cuatro**, `human_error_como_sintoma` en **uno** y
`vieja_vision_vs_nueva_vision_seguridad` en **uno**. **Fundir la componente entera desmentiria DIEZ
lecturas que ya estan escritas.**

**LAS TRES SALIDAS DE `P.10`, RECORRIDAS UNA A UNA en vez de elegir la comoda:** *leer el par que
falta* es la unica que resuelve de verdad **y quedan 75 combinaciones sin veredicto**, que es trabajo
de cribado y no de esta operacion; *releer contra el superviviente* **no aplica**, porque no hay
superviviente elegido ni nodo que vaya a cambiar; *fundir solo el subconjunto CERRADO y enlazar el
resto* **pide que TODAS las lecturas esten hechas, y no lo estan**.

> **Y HAY UNA SEGUNDA RAZON INDEPENDIENTE, TAMBIEN MEDIDA, QUE SOLA BASTARIA: DOS de los quince son
> PUERTA** con la marca *TIENE QUE SOBREVIVIR* (`enfoque_situacional_vs_personal` y
> `fallas_activas_condiciones_latentes`, leidas de la salida del dossier). **La GUARDA 1B no deja
> absorber ninguna de las dos**, y una fusion a un solo superviviente tendria que absorber una.

### 5.2 **EL ACTO 3: LA PRIMERA FUSION DE MAS DE DOS MIEMBROS DE LA CAMPANA**

**LA PREGUNTA DE `P.5` CONTESTADA CON MEDICION:** los **diez** miembros del **mismo libro** (*Out of
the Crisis*, Deming), **14 pares internos con veredicto y TODOS de clase `A`**, **CERO pares `D`
internos** y **CERO nodos puente**. **UNA SOLA FAMILIA.**

**SOBREVIVE `causas_comunes_vs_especiales` POR CONTENIDO, con las TRES varas por forma a su lado y
ninguna en contra** (`TODAS DE ACUERDO`, que funde a su lado): **6 pasos contra un maximo de 5**, **3
condiciones contra 2** y **cableado 14 contra un maximo de 9**. **Ni el rotulo solo ni la cantidad
deciden**: decide que es el unico del acto que trae el procedimiento entero de punta a punta.
**NINGUN miembro es puerta**, medido al sellar.

| | |
|---|---:|
| absorbidos | **9** |
| piezas repartidas | **58** |
| **enteras (`APPEND`)** | **16** |
| **ya dichas (`CUBIERTO`)** | **39** |
| **de `INCISO`** | **3** |
| **perdidas selladas en campo propio** | **13** (10 `DE PARAMETRO DE PASO`, 3 `DE CONDICIONES`) |

**LAS TRES COSAS QUE EL REPARTO DICE EN VEZ DE CALLAR, cada una con letra citable:**

1. **POR QUE HAY TRES `INCISO` Y NO SEIS.** El paso 4 del superviviente recibe **UN** inciso y **NO**
   el segundo que pedia `trampa_del_promedio_como_estandar`, **porque NO SE APILA MAS DE UN `INCISO`
   SOBRE EL MISMO PASO** (acta 64, pregunta 5, **registrada en esta misma vuelta**). Esa pieza va
   `CUBIERTO` **con la perdida nombrada y enrutada**, y el motivo esta escrito dentro de la perdida.
2. **LAS ADVERTENCIAS NO SON PASOS** (`P.11`): *evitar sanciones*, *evitar conclusiones apresuradas*,
   *evitar tratar cada defecto como causa especial* y *dejar de usar el promedio como linea de corte*
   **califican el acto y no lo constituyen**, asi que van `CUBIERTO` **con su perdida nombrada** en
   vez de `APPEND`.
3. **LOS SOLAPES VAN DECLARADOS** para la poda de la fase 04, que es el carril escrito de la pieza
   mitad propia y mitad ya dicha.

**EL SUPERVIVIENTE PASA DE 6 A 15 PASOS Y DE 3 A 10 CONDICIONES**, y esa cifra se publica **porque es
la mas alta de la campana**: es consecuencia de fundir DIEZ nodos, no de repartir mal. **Va marcada
discutible.**

### 5.3 **LAS GUARDAS, UNA POR UNA**

| guarda | resultado |
|---|---|
| **cuenta esperada de colisiones, medida ANTES de fundir** | linea base **2 COMPROBADA, no supuesta**; **CERO nuevas** y **CERO idas** ([`SALIDA_V65_COLISIONES_ESPERADAS.txt`](SALIDA_V65_COLISIONES_ESPERADAS.txt)) |
| **censo de cierre con la esperada MEDIDA** | **ESPERADA 2 \| MEDIDA 2 \| CALZA: SI** |
| **`P.16`, duplicadas que la propia fusion fabrica** | **6**, limpiadas **en el mismo commit** |
| **`P.16` por instrumento**, grupos FABRICADOS de verdad | **0**, y 4 grupos que DESAPARECEN ([`SALIDA_V65_DIFF_DUPLICADAS.txt`](SALIDA_V65_DIFF_DUPLICADAS.txt)) |
| **guarda 1**, miembros vivos y nomina completa | **OK** |
| **guarda 1B**, ningun absorbido es semilla ni extremo de puente | **OK** |
| **guarda 2**, cobertura exacta de indices | **OK** |
| **guarda 3**, cero repetidos literales en el resultado | **OK** |
| **guarda A**, cero auto-aristas nuevas | **OK (0)** |
| **guarda B**, cero duplicadas nuevas tras resolver | **OK (0)** |
| **guarda C**, los cinco campos que la operacion NO redacta | **5 de 5** |
| **guarda D**, los 9 absorbidos con su texto INTACTO | **OK** |
| **reanclar** | *nada que re-anclar: ninguna referencia apunta a un absorbido* |
| **Gate 0 con su ciclo de tres** | **OK** (71 etiquetas, 6 assets mas manifest) |
| **motor** | **25/25** |
| **web** | **80 ficheros, 1.030 pasadas, 3 saltadas** |
| **`tsc`** | **CERO lineas** |
| **caso positivo de mesa** (`--id-op OP-M-02-ACCLIMATE`, sujeto que la vuelta NO toca) | **LAS NUEVE MUERDEN** |
| **la guarda NUEVA de sujeto consumido** (sobre `OP-M-03-II`) | **MUERDE, `exit 1`** |
| **caso positivo heredado de tramos** | **LAS SEIS MUERDEN** |

**EL REGISTRO EN `03_FUSIONES.md`:** **+230 lineas y CERO borradas**, bajo su cabecera de tramo,
**sin una sola tabla tecleada** (la del acto declarado, la de piezas por absorbido y la del reparto
pieza a pieza **se generan del plan sellado**; la de perdidas **se recorta entera** de la salida del
tallador; las celdas de guardas y colisiones **se extraen por aguja** de las salidas). Guarda de citas
**5 de 5** antes y despues, y **guarda de idempotencia MORDIENDO**.

**NO SE FUNDIO NINGUN ACTO CON DUENO, no se toco la mesa `OP-M-03` ni sus colisiones, y las cinco
fichas `OP-M-02` consumidas no se ejecutaron.**

---

## 6. LOS DISCUTIBLES, MARCADOS ANTES DE SABER SI ACIERTO

**`D1`. REGISTRAR OCHO `A FAVOR` Y NO NUEVE.** El mensaje del commit del acta 64 y el encargo dicen
NUEVE; el texto del acta, linea **16876**, abre el `D5` llamandolo caida de procedimiento. **Elegi la
vara del TEXTO y declare la divergencia sin tachar el resumen**, en vez de copiar la cifra del
encargo. Es discutible porque **un encargo tambien es una instruccion**, no solo un resumen.

**`D2`. CORREGIR DOS INSTRUMENTOS DE NOMBRE ESTABLE EN VEZ DE ESCRIBIR SUCESORES.** El encargo decia
`generar_plan_del_lote.py con --operacion OP-U-02` con todas sus letras, y ese fichero no podia
correr. **Elegi corregirlo en el sitio por correccion declarada, que es lo que la vuelta 63 hizo con
este mismo fichero, en vez de escribir un sucesor de nombre nuevo.** Es discutible: la campana usa
las dos vias y la de sucesor deja el ancestro re-corrible sin tocar.

**`D3`. LA CAPACIDAD N-ARIA DEL GENERADOR ES UNA GUARDA QUE CRECE Y SE ESTRENA EL MISMO DIA.** El
cambio 7 anade una guarda nueva (*un acto de mas de dos SIN reparto es `ROJO`*) y se usa en la misma
vuelta que nace. **Va enumerada en el docstring y marcada aqui, que son las dos condiciones del acta
61**, pero el estreno del mismo dia es el `D6` del acta 64 otra vez.

**`D3.b`. EL `ACTO 3` ES LA PRIMERA FUSION DE MAS DE DOS MIEMBROS DE LA CAMPANA, Y SU MOTIVO SELLADO
LO PROMETIO AQUI.** El acto **3** del tramo unico funde **diez** nodos a
`causas_comunes_vs_especiales`, absorbiendo `distincion_causas_comunes_especiales`,
`distincion_causas_comunes_especiales_2`, `distincion_causas_comunes_especiales_incidentes`,
`distincion_causas_especiales_comunes`, `identificacion_causa_raiz_no_culpa_individual`,
`moral_y_sistema_no_individuo`, `politica_no_culpar_trabajador`, `trampa_del_promedio_como_estandar` y
`variacion_del_sistema_vs_individuo`. **Es discutible por si mismo, y no solo por el instrumento que
lo permite:** hasta hoy la campana solo habia fundido pares, **y una fusion de diez es una decision
sobre diez nodos tomada de una vez**, con `P.5` contestada por medicion (cero `D` internos, cero
puentes, misma fuente) pero **sin ningun precedente de tamano al que compararla**. Lo marco entero, y
el reparto pieza a pieza esta en `03_FUSIONES.md` para que se pueda leer contra los textos.

**`D4`. UN TRAMO SIN NUMERO NO SE NUMERA.** El rotulo del tramo se lee del campo `tramo` del propio
fichero (`UNICO Y FINAL POR AGOTAMIENTO`) en vez de inventarle un ordinal. Discutible porque **el
titulo del generador ahora publica una frase donde antes publicaba un digito**.

**`D5`. DECLARAR EL ACTO 1 POR `P.10` EN VEZ DE INTENTAR CERRAR SUS TRIANGULOS.** Elegi **no leer los
75 pares** (es trabajo de cribado y la campana esta en fase de ejecucion, regla 4) y **no fundir el
subconjunto cerrado** (`P.10` lo condiciona a que todas las lecturas esten hechas). **El resultado es
que el primer acto del prefijo cierra sin fundir nada.**

**`D6`. LEER UN VEREDICTO AUSENTE COMO *NO CANDIDATO* Y NO COMO *PAR SIN LEER*.** Si un veredicto
ausente contara como *sin leer* a efectos de `P.10`, **NINGUNO de los 47 actos del tramo podria
fundirse** y `OP-U-02` quedaria entera bloqueada. **Lo mejor sostenido, y es lo que aplique: el
disparador de `P.10` es el TRIANGULO `A` mas `A` mas `D`, que es mecanico y esta medido.** Va tambien
como **PENDIENTE DE DOCTRINA** en la seccion 8.

**`D7`. UN LOTE DE DOS ACTOS, Y EL PRIMERO SIN FUSION.** Declare el lote pequeno porque la vuelta se
gasto en el paso previo (los dos instrumentos) y en la lectura del tramo. **Entregue lo declarado**,
pero un lote con UNA sola fusion es un lote corto y se dice.

**`D8`. `CUBIERTO` CON PERDIDA EN LAS CUATRO ADVERTENCIAS, PUDIENDO SER `APPEND`.** `P.11` dice que
una advertencia es linea y no procedimiento, **pero cuatro advertencias con perdida sellada tambien
son cuatro perdidas**. Elegi la vara escrita sobre el bulto.

**`D9`. DIECISEIS `APPEND` QUE LLEVAN EL SUPERVIVIENTE A 15 PASOS Y 10 CONDICIONES.** Es el nodo mas
largo que la campana ha fabricado. **La alternativa era `CUBIERTO` con perdida en varios de ellos**,
que habria dado un nodo mas corto y un catalogo mas pobre. Elegi que la fase 04 pode.

**`D10`. TRES PERDIDAS SELLADAS *CON ATENUANTE DECLARADO* cuyo contenido SI llega por el `APPEND` de
un hermano.** Sellar una perdida que quiza no se pierde es **sobre-sellar**. Lo hice por el carril del
`D8` del acta 63 (*una perdida con atenuante declarado es mas auditable que un silencio*), pero
**inflar la cuenta de perdidas tiene su propio costo** y por eso va marcado.

**`D11`. EL `INCISO` AL PASO 6, el de la proporcion estimada.** Es el menos limpio de los tres: el
inciso se adosa al final de un paso que ya cierra en *para cada tipo de causa*. **Lo juzgue legible;
es el que mas facilmente cae.**

**`D12`. ENSANCHAR EL DOSSIER PARA QUE UN ACTO DE MAS DE DOS PUBLIQUE TODOS SUS PARES INTERNOS.** No
estaba encargado. Lo hice porque **el propio docstring del dossier ya lo prometia** (*la razon entera
de cada par interno pegada al lado*) y sin eso `P.5` no se puede leer en un acto de quince.

---

## 7. LAS AVERIAS PROPIAS, LAS CINCO, TODAS CAZADAS ANTES DE UNA CIFRA PUBLICADA

**CERO de ellas llego a una cifra publicada ni a un dato movido.** Se cuentan enteras porque callarlas
seria la especie que la casa persigue.

### 7.1 **EL CENSO DE AUTO-PARES QUE NO ERA COPIA**

La primera version de `vuelta65_colisiones_esperadas.py` **conto los auto-pares por VEREDICTO y dio
278**, donde el censo de la casa los cuenta **por GRUPO RESUELTO DISTINTO y da 256**, que es la cifra
publicada en la cabecera de la vuelta 64. **Dos instrumentos de la campana contando distinto en
silencio es justo lo que la regla 2 persigue.** Re-copie la aritmetica del ancestro (`lineas 56 a 72`)
y **la averia queda escrita en el docstring del instrumento**. **La cifra mala no se publico**: la
cace comparandola contra la cabecera de la vuelta anterior antes de escribir nada.

### 7.2 **EL CASO POSITIVO DEL GENERADOR MORDIO SOBRE MI PROPIA CORRECCION**

Al mover el cuerpo que marca pasos y condiciones dentro del bucle por absorbido, **el bloque que
asigna las marcas quedo dentro del bucle de las perdidas**, que para el fixture estaba vacio: **el
plan salia con `pasos {}`**. **Lo cazo la mitad 1 del caso positivo antes de sellar un solo plan
real**, comparando ancestro contra corregido. Queda dicho en el docstring del generador.

### 7.3 **CORRI `run_phase1` UNA CUARTA VEZ Y REVERTI LA CURADURIA**

El ciclo es de **TRES** y el orden lo dice el propio aviso de `run_phase1`: **recompilar**,
`etiquetas_de_cara.py --aplicar` y `sync_assets_web.py`. **Corri `run_phase1` otra vez despues del
sync**, que **recompila y revierte**, y **la suite web cayo con 6 fallos de etiquetas**. **La caza fue
la suite, no mi ojo**, y eso tambien se dice. Rehecho en el orden debido: 71 etiquetas en los dos
grafos y las tres suites en verde.

### 7.4 **ELEGI MAL LA VARA DEL PRIMER CASO POSITIVO**

Mi primera version comparaba el generador corregido **contra los planes y el dossier SELLADOS de las
vueltas 61 y 62**, y dio **ROJO: 808 lineas distintas**. **La causa no era la correccion**: los nodos
de aquel tramo **se fundieron en la vuelta 62 y hoy estan deprecados**. Una comparacion contra una
salida sellada **mide el movimiento del arbol, no el del cambio**. La vara buena (ancestro contra
corregido, los dos hoy) **queda escrita en el docstring del caso positivo junto con el motivo del
descarte**.

### 7.5 **UNA CITA DE LINEA MAL CALCULADA, CAZADA POR SU GUARDA**

En `vuelta65_registro_tramo.py` cite la seccion del acta 64 en la linea **3729** cuando esta en la
**3613**. **La guarda de citas la caza y NO escribio nada** (`MAL (FUERA DE RANGO)`). Es exactamente
para lo que la guarda existe.

### 7.6 **LAS PROMESAS DE MARCADO, POR MAQUINA**

**MEDIDO EN ESTA VUELTA** con el instrumento **ya ensanchado**:
`python scripts/loop/comprobar_promesas_de_marcado.py --reporte docs/loop/REPORTE.md --plan
docs/loop/PLAN_V65_OPU02_LOTE_A.json`
([`SALIDA_V65_PROMESAS_CUMPLIDAS.txt`](SALIDA_V65_PROMESAS_CUMPLIDAS.txt)).

---

## 8. PENDIENTES DE DOCTRINA Y PREGUNTAS

1. **UN VEREDICTO AUSENTE, ES UN PAR SIN LEER A EFECTOS DE `P.10`?** (nuevo, y es el grande). **Los 47
   actos del tramo tienen pares sin veredicto escrito** porque solo entraron en la cola los pares que
   la semejanza propuso. **Si un ausente contara como *sin leer*, ninguno de los 47 podria fundirse y
   `OP-U-02` quedaria bloqueada entera.** Registro lo mejor sostenido (**el disparador de `P.10` es el
   triangulo `A` mas `A` mas `D`, mecanico y medido**) y **lo subo**. **No paro**, por la regla 5.
2. **EL SUBCONJUNTO CERRADO DE UN ACTO CON PUENTE: QUIEN LO FUNDE Y CUANDO?** `P.10` lo nombra como
   tercera salida y la condiciona a que **todas** las lecturas esten hechas. **Nueve actos de este
   tramo estan en ese estado.** No hay letra que diga si el subconjunto cerrado se funde en la misma
   operacion, en otra, o si el acto entero se enruta a una mesa. **Pendiente nombrado, no parada.**
3. **UN ACTO CON DOS PUERTAS NO SE PUEDE FUNDIR A UNO, Y NO HAY CARRIL ESCRITO PARA EL.** La guarda 1B
   dice que una puerta no se absorbe, pero **no dice que hacer con un acto que tiene dos**. Aqui la
   pregunta no mordio porque `P.10` ya lo detenia, **pero mordera en cuanto aparezca un acto de dos
   puertas y sin puente**. Pendiente nombrado.
4. **EN UN ACTO N-ARIO NO HAY MARCA PARA *YA LO DICE EL `APPEND` DE UN HERMANO*.** `CUBIERTO:n` solo
   puede apuntar a los pasos ORIGINALES del superviviente. Resolvi por el carril escrito (`APPEND`
   entero con **solape declarado**, o `CUBIERTO` con **atenuante declarado**), **pero es un carril
   pensado para actos de dos**. Pendiente nombrado.
5. **EL `INCISO` DE CONDICIONES SIGUE SIN EXISTIR** (heredado): **tres perdidas `DE CONDICIONES` mas
   en esta vuelta**, enrutadas a la fase 04 por el carril del acta 55, pregunta 5.
6. **EL ESQUEMA DE `OPERACIONES.jsonl`** (heredado): sigue pendiente y el campo `nota` lo cubre.

---

## 9. RUTAS TOCADAS, CORRECCIONES DECLARADAS Y CENSOS

**Del grafo (34 ficheros, todos por la fusion del acto 3):** `causas_comunes_vs_especiales` y sus
**nueve** absorbidos (`distincion_causas_comunes_especiales`,
`distincion_causas_comunes_especiales_2`, `distincion_causas_comunes_especiales_incidentes`,
`distincion_causas_especiales_comunes`, `identificacion_causa_raiz_no_culpa_individual`,
`moral_y_sistema_no_individuo`, `politica_no_culpar_trabajador`, `trampa_del_promedio_como_estandar`,
`variacion_del_sistema_vs_individuo`), mas los nodos redirigidos, mas
`dataset/metadata/master_graph.json`, `dataset/metadata/phase1_run_log.json`,
`web/lib/assets/` (6 assets mas manifest), `docs/plan/ARISTAS_DUPLICADAS.jsonl`,
`docs/COSTURAS_INTERNAS.jsonl` y su resumen.

**De registro:** `docs/plan/03_FUSIONES.md` (**+119** del acta 64 y **+230** del registro del tramo,
**CERO borradas** en los dos, medido con `git diff --numstat`).

**CORRECCIONES DECLARADAS DE ESTA VUELTA, las CUATRO, todas con el texto viejo entero:** la aguja del
comprobador de promesas; el titulo de `generar_plan_del_lote.py`; el descubrimiento del ordinal y la
capacidad N-aria del mismo generador; y el ordinal mas los pares internos de `dossier_del_tramo.py`.

**Instrumentos nuevos, todos DE VUELTA:** `vuelta65_registrar_acta64.py`,
`vuelta65_caso_positivo_promesas.py`, `vuelta65_caso_positivo_generador.py`,
`vuelta65_puentes_del_tramo.py`, `vuelta65_colisiones_esperadas.py`, `vuelta65_registro_tramo.py`.
**De contenido:** `_v65_lote_a.py`. **NINGUNO de nombre estable se estrena esta vuelta**, y los dos
estables que se tocan lo hacen por correccion declarada con caso positivo.

**CENSO DE PLANTILLAS TALLADAS: CERO TALLADOS en los 22 instrumentos de nombre estable**, medido dos
veces, tras la TAREA 1 y tras las correcciones de la TAREA 2
([`SALIDA_V65_CENSO_PLANTILLAS_TAREA1.txt`](SALIDA_V65_CENSO_PLANTILLAS_TAREA1.txt),
[`SALIDA_V65_CENSO_PLANTILLAS_TAREA2A.txt`](SALIDA_V65_CENSO_PLANTILLAS_TAREA2A.txt)).

**BARRIDO AL CIERRE**, leido de la corrida de cierre y **no de ninguna anterior**
([`SALIDA_V65_BARRIDO_CIERRE.txt`](SALIDA_V65_BARRIDO_CIERRE.txt)): **429 ficheros barridos** (los 422
de la apertura mas **los 7 instrumentos que esta vuelta escribe**, medido), **`ROJO` 32** (la linea de
base heredada, **sin mover**), **`AMBAR` 0**, `ROTULADO` **38**, `CENSO` **220**, `ILEGIBLE` 1. **El
`AMBAR` que salio no se dejo pasar**: `vuelta65_registrar_acta64.py` declara vuelta 65 y su titulo
dice `VUELTA 64`, y **el barrido dice con todas sus letras que el no decide** si eso es procedencia o
cita envejecida. **Es procedencia**, y se rotulo por el carril que la casa ya usa
(`ROTULO titulo especie=PROCEDENCIA cita=vuelta:64` con su fuente y su literal de prueba), **cotejado
por maquina contra el acta**.

**FIGURAS Y FAMILIAS AL DIA:** esta vuelta **abre una figura nueva y la nombra**: **`FUSION N-ARIA`**,
un acto de mas de dos miembros con un superviviente y varios absorbidos, estrenada en el acto 3 con
diez miembros. Y **estrena un carril de cierre que existia escrito y no se habia usado nunca**:
**`DECLARADO POR P.10`**, un acto que cierra entero sin fundirse porque tiene nodos puente. **Quedan
del tramo unico 45 actos y 176 nodos**, de los cuales **ocho actos mas tienen nodos puente medidos**.
