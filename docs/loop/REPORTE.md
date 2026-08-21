# REPORTE DE LA VUELTA 64 (20 ago 2026, ejecutor Opus 5)

**LO PRIMERO, PORQUE ES LO QUE LA VUELTA ENTREGA: EL PUESTO 2 DE LA FASE 03 ABRE CON SU PRIMERA
FUSION EJECUTABLE.** Adjudicado el orden del puesto en el acta 63 y consumida la primera de la lista,
esta vuelta ejecuta **`OP-M-03-II`**, que es **la TERCERA fusion de mesa de la campana** y **la
aplicacion mas dura de `P.8` que hay en el plan**: el cableado dice lo contrario y por mucho, **10
contra 5**, y aun asi gana el contenido. Ademas queda **FIJADO EL TRAMO UNICO DE `OP-U-02`, sin
fundir ni un acto suyo**, la **TAREA 1 entera** (registro del acta 63 con las 33 citas cotejadas, la
relectura conjunta del `D10` resuelta y las CINCO fichas consumidas corregidas), y **DOS `ROJO`
propios cazados y arreglados**.

**LA FECHA ESTA MEDIDA POR DOS RELOJES Y NO SUPUESTA:** `date` da `2026-08-20` y
`git log -1 --date=format:'%Y-%m-%d'` da `2026-08-20`. Es la misma medicion que el campo `fecha` del
plan sellado, que la lee del reloj y no de una constante.

**LA RACHA DE REPORTE VENIA EN CERO Y ESTA VUELTA LA ROMPE, Y LO DICE ANTES QUE NADA.** El mensaje
del commit `6e1784c0` publico **tres celdas del barrido que no salieron de la corrida de ese
momento**, sino de la anterior. Esta dicho entero en la seccion 7, con la corrida buena al lado y sin
tapar el texto viejo, que sigue en el mensaje de aquel commit.

| | |
|---|---|
| **rama** | `pasada-unica` |
| **hash de apertura** | `f0f8605b` (el commit del acta 63), **arbol limpio y todo pusheado; la regla 3 se cumplio POR VACIO y se dice asi en vez de darla por cumplida** (`git status --porcelain` VACIO, comprobado) |
| **hash final** | **`ca74f202`**, el commit de este reporte, **pusheado a `origin/pasada-unica`**, mas este ultimo, que **solo escribe esta celda y la de abajo** porque el commit del reporte no podia contener su propio hash |
| **commits de la vuelta** | **7**, leidos de `git log --format=%h f0f8605b..HEAD`: `22afe95f` (apertura medida), `be69bc56` (TAREA 1.b y 1.c), `6e1784c0` (TAREA 1.a), `4d16c100` (los dos `ROJO` propios), `7a160a25` (`OP-M-03-II`), `2cc84e86` (registro y tramo unico), `ca74f202` (este reporte), **mas el que escribe esta celda** |
| **arbol al cierre** | limpio tras el commit del reporte |

---

## 0. LA APERTURA Y EL CIERRE, LA TABLA TALLADA POR INSTRUMENTO (regla 1)

**NINGUNA CELDA ESTA TECLEADA:** sale entera de
`python scripts/loop/tallar_cabecera_reporte.py --vuelta 64`
([`SALIDA_V64_TALLAR_CABECERA.txt`](SALIDA_V64_TALLAR_CABECERA.txt)). **Las dos columnas se leen de
ficheros DISTINTOS.**

| | **apertura**, antes de la 1.ª operacion | **cierre, RECOMPUTADO al cierre** |
|---|---:|---:|
| marcador `A` / `B` / `C` / `D` | 551 / 72 / 5 / 2.760 | **551 / 72 / 5 / 2.760** |
| `n`, huecos, duplicados | 3.388 / 0 / 0 | **3.388 / 0 / 0** |
| grafo: ficheros / vivos / deprecados / enlaces | 3.853 / 3.272 / 581 / 17.490 | **3.853 / 3.271 / 582 / 17.496** |
| retrato: `A` crudas / colapsos / pares distintos | 551 / 277 / 274 | **551 / 278 / 273** |
| actos (componentes) | 80 | **79** |
| actos `CERRADOS` / `ABIERTOS` | 27 / 53 | **26 / 53** |
| nodos en `CERRADOS` / `ABIERTOS` | 63 / 240 | **61 / 240** |
| cola de costuras | 1.456 | **1.455** |
| colisiones de clase vigentes | 0 | **2** |
| auto-pares (los dos lados al mismo vivo) | 255 | **256** |
| duplicadas historicas: grupos / nodos | 927 / 734 | **925 / 733** |
| operaciones, estados, dependencias rotas | 71, todas `LISTA`, 0 | **71, todas `LISTA`, 0** |
| entradas del inventario | 672 | **672** |
| las cuatro comprobaciones de `08_VERIFICACION` | TODAS OK (303 igual a 303; 274 igual a 274) | **TODAS OK (301 igual a 301; 273 igual a 273)** |

**LA APERTURA CALZA AL DIGITO CON EL CIERRE QUE EL ACTA 63 MIDIO POR CORRIDA PROPIA**, y eso es
contraste, no fuente: marcador, cola, colisiones y duplicadas dan **`diff` VACIO**, el estado difiere
solo en la etiqueta y el recomputo en **UNA linea**, la de la ruta del `--salida`. **EL BARRIDO
DIFIERE EN TRES FICHEROS BARRIDOS** (410 contra 407) **y la causa esta medida, no supuesta**: son los
**tres `.py` que el auditor committeo con el acta 63** (`_auditor_v63_ciega.py`,
`_auditor_v63_cuenta.py`, `_auditor_v63_mesas.py`), leidos de `git show --stat f0f8605b`; `ROJO`,
`AMBAR`, `ROTULADO`, `CENSO` e `ILEGIBLE` salen identicos.

Instrumentos de apertura corridos **ANTES de la primera operacion y con el arbol limpio**:
[`SALIDA_V64_APERTURA.txt`](SALIDA_V64_APERTURA.txt),
[`SALIDA_V64_MARCADOR_APERTURA.txt`](SALIDA_V64_MARCADOR_APERTURA.txt),
[`SALIDA_V64_RECOMPUTO_APERTURA.txt`](SALIDA_V64_RECOMPUTO_APERTURA.txt),
[`SALIDA_V64_COLA_APERTURA.txt`](SALIDA_V64_COLA_APERTURA.txt),
[`SALIDA_V64_COLISIONES_APERTURA.txt`](SALIDA_V64_COLISIONES_APERTURA.txt),
[`SALIDA_V64_DUPLICADAS_APERTURA.txt`](SALIDA_V64_DUPLICADAS_APERTURA.txt) y
[`SALIDA_V64_BARRIDO_APERTURA.txt`](SALIDA_V64_BARRIDO_APERTURA.txt). **Las tres que reescriben sus
ficheros salieron IDEMPOTENTES**, verificado por `git status`, que no listo **ni un fichero rastreado
modificado**.

**LA MEDICION DE CIERRE SE RE-CORRIO DESPUES DE ESCRIBIR LOS REGISTROS**, que es lo que la regla 1
manda: la cabecera de arriba es la ULTIMA medicion y no una heredada.

**LAS CELDAS QUE SE MUEVEN, TODAS MEDIDAS Y TODAS PREDICHAS POR LA UNICA FUSION DE LA VUELTA:** vivos
bajan **1**, deprecados suben **1**, colapsos suben **1**, pares distintos bajan **1**, actos bajan
**1**, `CERRADOS` bajan **1** y nodos en `CERRADOS` bajan **2**, auto-pares suben **1** y duplicadas
bajan **2 grupos**. **El delta de deprecados se midio en la propia ejecucion** (`+1` sobre `+1`
esperado).

**LAS TRES CELDAS QUE NO SE MUEVEN ASI, MEDIDAS Y NO SUPUESTAS:**

1. **LOS ENLACES SUBEN 6** (17.490 a 17.496). El superviviente hereda los vecinos del que muere por
   la simetrizacion del paso 5 de Gate 0, y la fusion dedupica por literal, asi que el saldo no es
   multiplo de nada. **Redirecciones sobre nodos VIVOS: 10**, leidas de
   [`SALIDA_V64_OPM03II_EJEC.txt`](SALIDA_V64_OPM03II_EJEC.txt).
2. **LA COLA BAJA 1** (1.456 a 1.455), **y la causa esta en el `diff` del propio fichero, no
   supuesta**: `pivotar_o_proceder` sale de la cola por quedar deprecado, y `pivote_o_proceder`
   **SUBE** de `50,7` con pareja `[4, 5]` a `55,0` con pareja `[8, 9]`, porque su pareja mas cercana
   pasa a ser la de **los dos pasos que heredo de `APPEND`**. Un nodo menos, y el que queda con otra
   puntuacion.
3. **LAS COLISIONES DE CLASE VIGENTES SUBEN DE 0 A 2, Y ESA CELDA SE PUBLICA EN ROJO EN VEZ DE
   ESCONDERSE.** Son **predichas, medidas y NO TOCADAS**, y el desarrollo entero esta en la
   **seccion 4.4**.

**TASA POR DOMINIO AL CIERRE**, leida de
[`SALIDA_V64_MARCADOR_CIERRE.txt`](SALIDA_V64_MARCADOR_CIERRE.txt): compras 0,6 (n 155) | core 22,5
(n 1.445) | entrega 1,2 (n 171) | environmental 16,5 (n 170) | exportacion 11,5 (n 130) | franquicias
10,1 (n 148) | health_safety 22,4 (n 192) | quality 14,1 (n 844) | risk_management 0,0 (n 106) |
seguridad_digital 11,1 (n 27). **IDENTICA a la de la apertura al digito: fundir no voltea
veredictos.**

---

## 1. TAREA 1.a: **EL REGISTRO DEL ACTA 63, CON LAS TREINTA Y TRES CITAS COTEJADAS ANTES DE ESCRIBIR**

Va al final de [`docs/plan/03_FUSIONES.md`](../plan/03_FUSIONES.md), **adosado y SIN reescribir una
sola linea de las secciones de arriba** (**+180 lineas, de 3.303 a 3.483**, contadas por el propio
instrumento). Es la via que esa pagina ya uso **CUATRO** veces: acta 52 (linea **1250**), acta 57
sobre el acto 25 (**2475**), acta 61 (**2689**) y acta 62 (**2933**).

**LA GUARDA DE CITAS MORDIO ANTES DE ESCRIBIR**, y su salida esta committeada
([`SALIDA_V64_REGISTRO_ACTA63.txt`](SALIDA_V64_REGISTRO_ACTA63.txt)): **33 citas de DOS ficheros**
(24 del acta y 9 de la propia pagina), **0 MALAS**, y el instrumento cae en `ROJO` sin escribir si
una sola no calza. **Re-cotejo tras adosar: las nueve sedes de arriba siguen en su linea.**

**Y LAS DOS TABLAS SE PEGAN, NO SE TECLEAN** (regla 1): la de desbloqueos sale de
`scripts/loop/vuelta64_puesto2.py` y la de las consumidas de `scripts/loop/vuelta64_consumidas.py`,
**las dos IMPORTADAS por el registrador**, no copiadas. **La frase que nombra la primera ejecutable
del puesto tampoco se teclea: sale de la propia medicion.**

Contenido: los **NUEVE `A FAVOR`** con su vara citable y su linea, **LA REGLA DE LA FICHA ENVEJECIDA**
escrita entera con sus tres ramas, el orden del puesto 2 con su tabla, las **CINCO CONSUMIDAS**, la
**caida de acta del auditor con su nombre** (de 5 a 6) y el `D10` resuelto.

**UNA GUARDA DE IDEMPOTENCIA ANADIDA AL REGISTRADOR, y nace de un riesgo real:** adosar dos veces
publicaria la misma adjudicacion dos veces, **y una pagina con la seccion duplicada no falla, dice
que si**. Re-corrido: `YA ADOSADA`.

---

## 2. TAREA 1.b: **EL `D10`, RELECTURA CONJUNTA. SE SELLA**

**El caso del auditor:** la condicion 1 de `fases_de_retencion_de_clientes` quedo `CUBIERTO:1` **sin
perdida sellada**, y **ese mismo dia `OP-M-03-I` sello DOS perdidas `DE CONDICIONES` por la misma
especie**. El auditor no adjudico: mando **verificar contra el grafo y decidir con la vara**.

**MEDIDO HOY sobre el json vivo** (`python scripts/loop/vuelta64_d10.py`,
[`SALIDA_V64_D10.txt`](SALIDA_V64_D10.txt)):

| | el texto de HOY |
|---|---|
| **muere** (condicion 1 de `fases_de_retencion_de_clientes`) | *Cuando la empresa solo tiene procesos disenados para atraer y cerrar ventas, pero no para despues de la compra* |
| **sobrevive** (condicion 1 de `ocho_fases_experiencia_cliente`) | *Cuando el usuario necesita una estructura sistematica para gestionar la experiencia del cliente despues de la venta* |

**LA BUSQUEDA NEGATIVA SE CORRIO EN VEZ DE CITARSE** (regla 9): las **cinco** agujas del encuadre del
sintoma salen **AUSENTES sobre el json ENTERO del superviviente**, no solo sobre sus condiciones.

**LA DECISION: SE SELLA, Y EL `CUBIERTO` SE SOSTIENE.** El disparador operativo (**el DESPUES DE LA
VENTA**) esta en la condicion 1 del superviviente con todas sus letras, asi que la marca no se toca;
**lo que se anade es el sello de la mitad que muere**, el encuadre del sintoma, que es el diagnostico
por el que un lector se reconoce a si mismo.

**LA VARA, LEIDA ENTERA** (acta 55, pregunta 5): *las perdidas de condiciones no van de `APPEND` por
defecto, y la perdida NOMBRADA es el carril mientras el pendiente del `INCISO` de condiciones siga
abierto*. **Esa vara reparte DOS marcas y no una**: `APPEND` para el disparador **distinto**, y
`CUBIERTO` **con la perdida nombrada** para el **mismo** disparador con un matiz que muere. **Lo que
no contempla en ninguna de sus dos ramas es el `CUBIERTO` CON SILENCIO.** Y es **la misma especie**
que las dos hermanas de `OP-M-03-I` (*el mismo fenomeno sin la pendiente*, *el mismo callejon sin la
imagen*): tratar igual lo medido igual dentro de la misma vuelta es la regla de trabajo **declarada y
uniforme** del acta 55, pregunta 4.

**COMO SE ESCRIBE:** correccion declarada en el campo `perdidas` y en la `nota_del_reparto` de
[`PLAN_V63_OPM02PROG.json`](PLAN_V63_OPM02PROG.json), **citando VERBATIM la frase que decia lo
contrario** (extraida del propio fichero por el instrumento, que cae en `ROJO` si no la encuentra),
y en el registro de `03_FUSIONES.md` citando las lineas **3189** y **3193** del registro viejo, **que
no se toca**. **El tallador lo confirma por maquina:** `tallar_perdidas_del_plan.py` da **5 perdidas
nombradas en los dos planes de la vuelta 63** (**3 `DE CONDICIONES`, 2 `DE PARAMETRO DE PASO`**),
donde antes daba 4
([`SALIDA_V64_TALLAR_PERDIDAS_V63.txt`](SALIDA_V64_TALLAR_PERDIDAS_V63.txt)).

**NADA DEL GRAFO SE TOCA:** la fusion esta ejecutada y auditada, y esto es registro.

---

## 3. TAREA 1.c: **LAS CINCO CONSUMIDAS, MEDIDAS POR CAMINO PROPIO Y CORREGIDAS**

**El auditor lo midio con instrumento propio y el ejecutor lo volvio a medir por camino propio antes
de escribir una sola correccion**, que es lo que el protocolo de relectura conjunta pide. **LA TABLA
SALE ENTERA** de `python scripts/loop/vuelta64_consumidas.py`
([`SALIDA_V64_CONSUMIDAS.txt`](SALIDA_V64_CONSUMIDAS.txt)):

| ficha | superviviente de la **ficha** (12 ago) | el que quedo **VIVO** | coinciden | quien la consumio | linea |
|---|---|---|:---:|---|---:|
| `OP-M-02-MEDIOS` | `seis_medios_comunicacion_cliente` | `estrategia_multicanal_bienvenida` | **NO** | `OP-U-01`, TRAMO 3, vuelta 56, acto 32, lote B | **2091** |
| `OP-M-02-ASSESS` | `fase_assess_ciclo_cliente` | `fase_assess_ciclo_cliente` | si | `OP-U-01`, TRAMO 2, vuelta 55, acto 30, lote A | **1832** |
| `OP-M-02-ADMIT` | `fase_admit` | `fase_admit_celebracion` | **NO** | `OP-U-01`, TRAMO 2, vuelta 55, acto 38, lote B | **1840** |
| `OP-M-02-ACTIVATE` | `fase_activate_primera_impresion` | `fase_activate_primera_impresion` | si | `OP-U-01`, TRAMO 1, vuelta 48, acto 44 | **417** |
| `OP-M-02-ACCOMPLISH` | `fase_accomplish_experiencia_cliente` | `fase_accomplish_experiencia_cliente` | si | `OP-U-01`, TRAMO 3, vuelta 56, acto 9, lote A | **2069** |

**LAS DOS MEDICIONES CALZAN AL DIGITO** en la unica que el auditor situo (`MEDIOS`: tramo 3, vuelta
56, lote B, acto 32, linea **2091**, con su perdida en la **2132**), y **las otras cuatro quedan
situadas por el mismo camino**. **Cada correccion va en el campo `nota` de su ficha, por el carril
del banco `9.10`, con el texto viejo entero y sin tachar**, y en `MEDIOS` y `ADMIT` **la divergencia
de superviviente va DECLARADA como contraste** en vez de resolverse copiando. **NADA DEL GRAFO SE
TOCA.**

**POR QUE NO SE ESTRENA CLAVE NUEVA EN `OPERACIONES.jsonl`, dicho para que no parezca descuido:** su
esquema es **un pendiente de doctrina heredado** (acta 55, seccion 5) y **estrenar clave en 5 de las
71 fichas seria decidirlo de tapadillo**. El campo `nota` es ademas el sitio que estas fichas ya
usan: `OP-F-01`, `OP-D-01`, `OP-D-03`, `OP-D-04`, `OP-S-06`, `OP-S-07`, `OP-C-04` y `OP-U-01` traen
ahi su correccion declarada. **Guardas tras escribir:** 71 fichas antes y despues, **las 18 claves
intactas en las 71**, las cinco con su `fecha_corte` del 12 ago, cero guiones largos y cero medios
([`SALIDA_V64_CORRECCIONES_CONSUMIDAS.txt`](SALIDA_V64_CORRECCIONES_CONSUMIDAS.txt)).

**Y EL ORDEN DEL PUESTO 2, RE-MEDIDO EN ESTA VUELTA** y no copiado del acta
([`SALIDA_V64_PUESTO2.txt`](SALIDA_V64_PUESTO2.txt)):

| puesto | operacion | **desbloquea** | cuales, leidas de su `depende_de` | estado HOY |
|---:|---|---:|---|---|
| **1.a** | `OP-M-02-MEDIOS` | **5** | `OP-M-02-ASSESS`, `OP-M-02-ADMIT`, `OP-M-02-ACTIVATE`, `OP-M-02-ACCLIMATE`, `OP-M-02-ACCOMPLISH` | **CONSUMIDA**, su par ya resuelve a un solo vivo |
| **2.a** | `OP-M-03-II` | **4** | `OP-M-03-ENLACES`, `OP-M-05-INDICE`, `OP-M-05-EDIFICIO`, `OP-M-05-APERTURA` | ejecutable, 2 miembros a 2 vivos |
| **3.a** | `OP-U-02` | **1** | `OP-E-03` | ejecutable; **SIN nomina de nodos en su ficha**, su universo se abre aparte |

---

## 4. TAREA 2.a: **`OP-M-03-II` EJECUTADA**

### 4.1 La regla de la ficha envejecida, aplicada y declarada

**Las mediciones selladas se RE-CORRIERON HOY antes de fundir**
([`SALIDA_V64_LECTURA_OPM03II.txt`](SALIDA_V64_LECTURA_OPM03II.txt),
[`SALIDA_V64_SIM_OPM03II.txt`](SALIDA_V64_SIM_OPM03II.txt)) **y TODAS LAS VIAS CONVERGEN** en
`pivote_o_proceder`:

| via, medida hoy | cifra | apunta a |
|---|---:|---|
| vara de **pasos** | 7 contra 5 | `pivote_o_proceder` |
| vara de **condiciones** | 1 contra 2 | `pivotar_o_proceder` |
| las dos varas de contenido | **`CHOCAN`** | **decide LA PIEZA DECLARADA** (acta 53, pregunta 3), que es la adjudicacion sellada y nombra a `pivote_o_proceder` |
| vara de **cableado** | 10 contra 5 | `pivotar_o_proceder`, **y NO ENTRA**: `P.8` dice que el cableado **desempata, no decide**, y solo habla a contenido **EMPATADO**. Aqui el contenido no empata |

**LA CORRECCION DECLARADA QUE LA FICHA YA TRAIA SIGUE SIENDO CIERTA CONTRA EL GRAFO DE HOY:** el
expediente escribio que el cableado *no desempata* y la ficha lo corrigio el 12 ago diciendo que son
**10 contra 5**; **medido hoy con la vara del instrumento: 10 contra 5, IDENTICO AL DIGITO**.

**UNA VARA MIA DICHA, Y SON DOS VARAS Y NO UNA DISCREPANCIA:** mi cuenta cruda de cableado (cada nodo
que lo nombra UNA vez, deprecados incluidos) da **12 contra 6**; **la publicada es la del
instrumento** (entrantes sobre nodos no deprecados, los dos campos por separado), que es la que la
ficha uso. **Es el mismo manejo que el acta 63 declaro para los enlaces.**

**LECTURA DE ACTO POR `P.5`, HECHA ANTES DE FUNDIR:** los dos nodos declaran el **MISMO libro**
(*The Startup Owner's Manual*, de Steve Blank), la **MISMA `fase_proyecto`** (`validacion`) y el
**MISMO `dominio`** (`core`), **y las tres calzan por maquina**. **UNA familia, no dos.**

**LA SIMULACION DE HOY ES IDENTICA AL DIGITO A LA SELLADA**, y se dice porque es la primera fusion de
mesa de la campana en la que eso pasa: **10 entradas redirigidas, 2 duplicadas nuevas nombradas una a
una y 0 auto-aristas**, los mismos nombres y los mismos campos que la ficha escribio el 12 ago.
**NI UNA DIVERGENCIA QUE DECLARAR en la simulacion.**

### 4.2 El reparto y sus cuatro perdidas

**SIETE PIEZAS: tres viajan enteras, tres ya estaban dichas y UNA de `INCISO`.**

- **LA PIEZA QUE LA FICHA MANDA PRESERVAR VIAJA ENTERA:** clasificar las respuestas del cliente
  **desde amor total hasta indiferencia** (paso 3 del que muere), **verificada en el texto final**
  (paso 9 del superviviente). **Y su paso gemelo viaja con ella**, que es lo que la hace utilizable:
  revisar **evidencia real, no opiniones**, sobre el entusiasmo. El superviviente mira datos reales
  en su paso 2, pero mira **como trabaja el cliente**, que es otro objeto.
- **EL UNICO `INCISO` SE ADOSA PORQUE CABE LIMPIO:** el paso resultante es *Anota tu decision final:
  cambias de rumbo (pivotas) o sigues adelante **hacia la validacion con clientes***, y el trozo se
  **EXTRAJO VERBATIM** del paso 4 del que muere.
- **LOS DOS `CUBIERTO` DE PASO VAN CON SU PERDIDA NOMBRADA Y CON EL MOTIVO DE POR QUE EL `INCISO` NO
  CABE**, que es la mitad que el `D9` exige argumentar. **VAN MARCADOS DISCUTIBLES EN LA SECCION 6.**
- **CUATRO PERDIDAS SELLADAS EN CAMPO PROPIO**, tres `DE PARAMETRO DE PASO` y una `DE CONDICIONES`.
- **EL SUPERVIVIENTE QUEDA EN NUEVE PASOS Y DOS CONDICIONES**, y se dice en vez de callarlo: es
  **candidato legitimo a la poda de la fase 04**, que es el limite que el acta 62 escribio para los
  repartos anchos del `D5`.

### 4.3 Las guardas, una por una

| guarda | resultado |
|---|---|
| guarda 1, miembros vivos y nomina completa | **OK** |
| guarda 1B, ningun absorbido es semilla ni extremo de puente | **OK** |
| guarda 2, cobertura exacta de indices | **OK** |
| guarda 3, cero repetidos literales en el resultado | **OK** |
| guarda A, cero auto-aristas nuevas | **OK (0)** |
| guarda B, cero duplicadas nuevas tras resolver | **OK (0)** |
| guarda C, los cinco campos que la operacion no redacta | **5 de 5 intactos** |
| guarda D, el absorbido conserva su texto INTACTO | **OK** |
| `P.16`, duplicadas que la propia fusion fabrica | **2, limpiadas en el mismo commit**; verificacion de cero: **NINGUNA** |
| re-anclar por resolutor | **nada que re-anclar** |
| Gate 0 con el ciclo de tres | **OK** (71 etiquetas re-aplicadas, 6 assets mas manifest) |
| motor / web / `tsc` | **25/25** ; **80 ficheros, 1.030 pasadas, 3 saltadas** ; **CERO lineas** |
| verificacion propia, por camino propio | **TODAS EN VERDE** |

**`P.16` CONTRA LA LETRA DE LA FICHA, Y MANDA `P.16`:** la ficha del 12 ago dice que las dos
duplicadas quedan para `OP-S-12`; `P.16` (decision del fundador, 14 ago, **posterior**) dice que
quien fabrica limpia en el mismo commit, y su punto 3 hace de `OP-S-12` una **verificacion de cero**.
Es el carril que el acta 63 adjudico `A FAVOR` en su `D5`.

**EL `diff` DE DUPLICADAS POR INSTRUMENTO**
([`SALIDA_V64_DIFF_DUPLICADAS_OPM03II.txt`](SALIDA_V64_DIFF_DUPLICADAS_OPM03II.txt)):
**CERO grupos fabricados** y **cero renombrados**. **Y DOS GRUPOS DESAPARECEN QUE NO SON LOS DOS QUE
`P.16` LIMPIO, y eso se MIDIO en vez de explicarse** (comprobacion 7 de
[`SALIDA_V64_VERIFICAR_OPM03II.txt`](SALIDA_V64_VERIFICAR_OPM03II.txt)): **los dos eran duplicadas
historicas DENTRO de `pivotar_o_proceder`**, y **salen del censo porque el censo solo revisa nodos
VIVOS** (3.272 antes, 3.271 despues). **No se han reparado: siguen enteras en su nodo**, con la
contraprueba corrida. **Las dos que `P.16` si limpio nunca entraron en el censo** porque nacieron y
murieron dentro de la misma corrida, **y por eso el `diff` da cero fabricadas**.

### 4.4 **DOS COLISIONES DE CLASE FABRICADAS, PREDICHAS Y NO TOCADAS**

**Esto es lo mas discutible de la vuelta y va con todo el detalle.**

**PRIMERO, MI PROPIO ERROR DE PROCEDIMIENTO:** corri el censo de colisiones con `--esperadas 0`
**sin haber medido esa cifra**. **La cuenta esperada salio de mi cabeza y no de un instrumento**, que
es exactamente lo que la regla 1 prohibe, y el censo midio **2**. **La medi despues, como debia
haberla medido antes**, con `scripts/loop/vuelta64_colisiones_opm03ii.py`
([`SALIDA_V64_COLISIONES_OPM03II.txt`](SALIDA_V64_COLISIONES_OPM03II.txt)), simulando la fusion sobre
el mapa de alias del **arbol de ANTES**:

| | |
|---|---:|
| colisiones **antes** de fundir | **0** |
| colisiones **ESPERADAS**, simuladas sobre el arbol de antes | **2** |
| colisiones **MEDIDAS** sobre el arbol de hoy | **2** |
| **son LAS MISMAS dos** | **si**, y por eso **`CALZA`** |

| par resuelto | puestos que chocan |
|---|---|
| `pivote_o_proceder` contra `pivote_startup` | **668** en `B` (`pivote_o_proceder` + `pivote_startup`) y **1312** en `D` (`pivotar_o_proceder` + `pivote_startup`) |
| `pivote_o_proceder` contra `reunion_pivotar_o_perseverar` | **968** en `B` y **1305** en `D` |

**NO SE TOCA NI UN VEREDICTO, Y SE DICE POR QUE, con la medicion delante:**

1. **EL 668 ES DE LA MESA.** La ficha de `OP-M-03` lo nombra **literalmente** entre sus **siete
   dudosos** (*puestos 668, 737, 771, 843, 957, 1298 y 753*) y su expediente del 12 ago **ya lo
   posiciona**: *el 668 y el 737 se resuelven como PUERTA CONTRA ACTO CON ENLACE*. **El 1312 esta
   nombrado entre sus TRES sanos.** Re-leerlos **seria ejecutar la adjudicacion de una mesa que no
   se ha ejecutado**, que es lo que `AUDITOR.md` seccion 3 llama improvisacion.
2. **`pivote_startup` ES MIEMBRO DE `OP-M-03-III`, PENDIENTE.**
3. **NO SE RESUELVEN SOLAS, Y ESO TAMBIEN ESTA MEDIDO:** simulada la ejecucion de `OP-M-03-III` sobre
   el arbol de hoy, **las colisiones pasan de DOS a TRES**, no a cero. **La deuda crece con cada
   fusion de esa mesa**, y por eso no basta con esperar.
4. **LO QUE SI ESTA VERDE:** las guardas por operacion que `AUDITOR.md` seccion 3 enumera
   (simulacion previa, Gate 0 y suites, caso positivo, **cero duplicadas o auto-aristas tras
   resolver**) estan **TODAS en verde**. El censo de colisiones es una guarda que el encargo anade,
   y **hoy CALZA**: esperadas 2, medidas 2, las mismas.

**VAN A LA MESA `OP-M-03` CON SU MEDICION, y quedan registradas en `03_FUSIONES.md`.** **Marcado
discutible en la seccion 6 y con pregunta abierta en la seccion 8.**

### 4.5 **EL CASO POSITIVO DE LA VUELTA 63 CADUCO EN ESTA OPERACION**

**Y caduco en su propia carne, que es lo que lo hace util.** Su regla de trabajo (acta 54, pregunta
7) manda fabricar el caso positivo **sobre un acto que la vuelta no toque, para que no caduque**; el
ancestro cumplio la regla en su vuelta y eligio **`OP-M-03-II`**, que es **justo lo que ESTA vuelta
ejecuta**. **Re-corrido hoy da `ROJO` en CUATRO de sus nueve pruebas** (la 3, la 4, la 5 y la 6), y
**no porque las guardas se hayan roto**: `pivotar_o_proceder` ya esta deprecado, **el generador cae
antes en la guarda de miembro vivo y NUNCA llega** a las de cobertura, `INCISO` y perdida, que
quedarian **dadas por no mordidas**. Su `ROJO` va committeado como contraste
([`SALIDA_V64_CASO_POSITIVO_MESA_ANCESTRO.txt`](SALIDA_V64_CASO_POSITIVO_MESA_ANCESTRO.txt)).

**LA LECCION MEDIDA: LA REGLA NO BASTA SI EL SUJETO ESTA TALLADO EN EL FICHERO.** El sujeto de una
vuelta es el ejecutado de la siguiente. **Nace `scripts/loop/caso_positivo_de_fusion_de_mesa.py`, de
NOMBRE ESTABLE y sucesor declarado**, con tres cambios y ninguno de aritmetica: `--id-op`
**REQUERIDO**, las marcas de mentira **armadas de la forma real de los nodos** en vez de talladas, y
**UNA GUARDA NUEVA** que cae en `ROJO` si el sujeto esta consumido **en vez de dar cuatro guardas por
no mordidas**. **El ancestro queda entero y re-corrible.**

**MEDIDO:** **LAS NUEVE MUERDEN** sobre `OP-M-02-ACCLIMATE`
([`SALIDA_V64_CASO_POSITIVO_MESA.txt`](SALIDA_V64_CASO_POSITIVO_MESA.txt)) y **la guarda nueva
muerde** sobre `OP-M-03-II`
([`SALIDA_V64_CASO_POSITIVO_MESA_CONSUMIDO.txt`](SALIDA_V64_CASO_POSITIVO_MESA_CONSUMIDO.txt)).
**El heredado de tramos re-corrido: LAS SEIS MUERDEN.**

---

## 5. TAREA 2.b: **EL TRAMO UNICO DE `OP-U-02`, FIJADO SIN FUNDIR NI UN ACTO**

Nace `scripts/loop/fijar_tramo_de_opu02.py`, de **NOMBRE ESTABLE** y **HERMANO, no sucesor**, de
`abrir_tramo_de_opu01.py`. **La diferencia es de forma del tramo y no de aritmetica:** aquel corta
cincuenta de una nomina que no cabe entera y por eso necesita dos lecturas, guarda de prefijo y
guarda de solape; **aqui no hay nada que cortar**, porque el acta 63 (pregunta 5) adjudico que el
tramo es **prefijo con tope y no minimo** y **los 47 caben bajo el tope de cincuenta**. **TRAMO UNICO
Y FINAL POR AGOTAMIENTO, declarado al abrirlo.**

**LAS CINCO GUARDAS, contra el grafo de HOY**
([`SALIDA_V64_TRAMO_OPU02.txt`](SALIDA_V64_TRAMO_OPU02.txt)):

| guarda | resultado |
|---|---|
| **1.** identidad de la nomina contra las componentes `ABIERTAS` de hoy, **por conjunto de miembros resueltos (`P.1`)**, no por posicion ni por tamano | **53 de 53**, y **CERO componentes abiertas sin fila** |
| **2.** ningun miembro que abre esta deprecado hoy | **0 sobre 201 nodos** |
| **3.** los 6 que quedan fuera **siguen con dueno de mesa o destejido, RE-MEDIDO hoy** y no heredado del fichero | **6 de 6**, y los duenos calzan uno a uno con lo que la nomina decia |
| **4.** los que abren caben bajo el tope de 50 | **47, caben** |
| **5.** la suma cierra | **47 mas 6 igual a 53** |

**FIJADO** en [`TRAMO_UNICO_OPU02_V64.jsonl`](TRAMO_UNICO_OPU02_V64.jsonl), **47 filas en su
`orden_universo`**, **201 nodos**, por tamano de acto **3: 23 | 4: 10 | 5: 7 | 6: 4 | 8: 1 | 10: 1 |
15: 1**. Los 6 de fuera suman **39 nodos**. **Calza al digito con el 47/201 y el 6/39 que el acta 63
midio por corrida propia.**

**EL FICHERO NO SE LLAMA `TRAMO<N>_V<vuelta>.jsonl` A PROPOSITO, y se dice:** ese es el patron con el
que `abrir_tramo_de_opu01.py` **descubre** los tramos ya fijados de `OP-U-01` (su `RE_FIJADO`), y
meterle dentro un tramo de **otra operacion** le movia la cuenta del siguiente tramo **sin que nadie
lo notara**. **Fallar ruidoso empieza por no fabricar la trampa.**

**LO QUE ESTA TAREA NO HACE:** no elige superviviente, no reparte piezas, no declara ningun acto y
**no funde nada**. **Su primer lote es de la vuelta que el orden alcance, no de esta.**

---

## 6. LOS DISCUTIBLES, MARCADOS ANTES DE SABER SI ACIERTO

- **`D1`, SELLAR EL `D10` EN VEZ DE DEJARLO CUBIERTO CON SILENCIO.** Acto 1 de
  `PLAN_V63_OPM02PROG.json`, miembros `ocho_fases_experiencia_cliente` y
  `fases_de_retencion_de_clientes`. **Corrijo un plan ya sellado, ejecutado y auditado.** Lo que lo
  sostiene: la vara del acta 55 pregunta 5 leida entera no contempla el `CUBIERTO` con silencio, y la
  misma especie se sello dos veces el mismo dia. Lo que lo hace discutible: **el auditor podia haber
  querido que un plan ejecutado no se re-abra ni para anadir**, y la asimetria podia haberse
  registrado sin tocar el plan.
- **`D2`, MARCAR `CUBIERTO` CON PERDIDA NOMBRADA EN EL PASO 1 DE `pivotar_o_proceder` PUDIENDO PONER
  UN `INCISO`.** Acto 1 de `PLAN_V64_OPM03II.json`, miembros `pivote_o_proceder` y
  `pivotar_o_proceder`. **La guarda de la juntura NO lo habria rechazado** (ese paso no cierra en
  punto); **lo rechazo yo, por legibilidad del paso resultante**, que es el criterio escrito de la
  politica pero lo aplique **con mi ojo**. El paso resultante seria *...y si tienes inversores,
  sumalos tambien, a evaluar con calma en que punto estas*, con el inciso colgando de **sumalos** y
  no de **sientate**. **Es exactamente el limite que el acta 62 le puso al `D9`.**
- **`D3`, MARCAR `CUBIERTO` CON PERDIDA NOMBRADA EN EL PASO 5 POR NO APILAR UN SEGUNDO `INCISO`.**
  Mismo acto y mismos miembros. El paso 7 **ya recibe** el `INCISO` del paso 4, y apilarle *los
  criterios que usaste para tomarla* lo dejaria diciendo que sigues adelante hacia la validacion
  **y los criterios**. **Discutible porque el instrumento no prohibe dos incisos al mismo paso: lo
  decido yo.**
- **`D4`, EJECUTAR DEJANDO DOS COLISIONES DE CLASE VIVAS.** La celda de la cabecera pasa de 0 a 2 y
  **la publico en rojo**. Lo que lo sostiene: estan **predichas y medidas** (esperadas 2, medidas 2,
  las mismas), los puestos son **de la mesa `OP-M-03`** por su propia ficha, y las guardas que
  `AUDITOR.md` enumera estan verdes. Lo que lo hace discutible: **la campana venia dejando el censo
  en cero tras cada operacion**, y esta lo deja en dos.
- **`D5`, MEDIR LA CUENTA ESPERADA DE COLISIONES DESPUES DE FUNDIR.** La corri con `--esperadas 0`
  adivinado. **La medicion posterior sale identica a la que habria salido antes** (la simulacion se
  hace sobre el arbol de `4d16c100`, que es el de antes de fundir), **pero el orden fue el
  equivocado** y va marcado como lo que es.
- **`D6`, ESTRENAR DOS INSTRUMENTOS DE NOMBRE ESTABLE Y USARLOS EL MISMO DIA**
  (`caso_positivo_de_fusion_de_mesa.py` y `fijar_tramo_de_opu02.py`). Es el carril del `D3` del acta
  63, **con la diferencia de que el primero HACE CRECER UNA GUARDA** (la de sujeto consumido). Lo que
  lo sostiene: la guarda nueva **muerde en la corrida de hoy** sobre el sujeto consumido, el ancestro
  queda entero y su `ROJO` va committeado.
- **`D7`, NO ESTRENAR CLAVE NUEVA EN `OPERACIONES.jsonl` PARA LAS CONSUMIDAS.** Meti la correccion en
  el campo `nota`. **Discutible al reves que los demas**: se puede sostener que una ficha consumida
  merece un campo propio y que no darselo la deja pareciendo ejecutable.
- **`D8`, DEJAR LAS CINCO CONSUMIDAS EN ESTADO `LISTA`.** Consecuencia del `D7`: la celda de la
  cabecera sigue diciendo **71, todas `LISTA`**, y **cinco de esas 71 no se pueden ejecutar**. **No
  lo cambio porque el encargo no lo pide y el esquema es pendiente de doctrina**, pero la cifra
  publicada dice algo que ya no es del todo cierto y **prefiero decirlo yo antes que lo diga el
  auditor**.
- **`D9`, LA VARA DE CABLEADO QUE PUBLICO NO ES LA QUE YO CONTARIA.** Publico **10 contra 5** (la del
  instrumento) y mi cuenta cruda da **12 contra 6**. Elegi la del instrumento **porque es la que la
  ficha uso**, no porque sea mejor.

**PROMESAS DE MARCADO, COTEJADAS POR MAQUINA ANTES DE SELLAR ESTE REPORTE:** ver la seccion 7.6.
**Y una promesa que NO se re-reclama aqui, dicha con su motivo en vez de callada:**
`PLAN_V63_OPM03I.json` promete marcado **en el reporte de SU vuelta**, la 63, donde se cumplio y el
auditor lo adjudico `A FAVOR` (`D4`). **No se vuelve a marcar en este reporte**, y por eso ese plan
no entra en la corrida del comprobador.

---

## 7. LOS `ROJO` PROPIOS Y LA CAIDA DE REPORTE, CON LAS DOS MITADES

### 7.1 **CAIDA DE REPORTE MIA, CON NOMBRE**

**El mensaje del commit `6e1784c0` dice:** *Barrido tras la TAREA 1: 417 ficheros, `ROJO` 32 sin
mover, y mis cuatro scripts nuevos sin un solo hallazgo.* **LAS TRES CELDAS ESTABAN MAL.** La corrida
de ese momento decia **415 ficheros, `ROJO` 33 y `AMBAR` 2**, y **los tres hallazgos eran MIOS.**

**LA ESPECIE, dicha sin adorno:** corri el barrido, mire la cola de la salida **y escribi la cifra de
la corrida anterior**. Es la especie que la regla 1 persigue (*medir temprano y publicar tarde sin
remedir*), **y no la disculpa que la corrida estuviera hecha**: leerla y no leerla es lo mismo si lo
que se publica sale de la memoria. **El texto viejo no se borra: sigue entero en el mensaje de aquel
commit.**

### 7.2 **`ROJO` PROPIO 1: ROTULO HUERFANO**

`vuelta64_registrar_acta63.py`, linea 23. Copie el `ROTULO` de `PROCEDENCIA` del registrador de la
vuelta 63 **sin comprobar que aqui cubriera algo**, y no cubria nada: el barrido clasifica el titulo
de este fichero como `CENSO` (sello fijo) y no como `AMBAR`. **RETIRADO.** Los **dos `AMBAR`** de
`vuelta64_puesto2.py` (`VUELTA 47` en cabecera y en un `print`) **si son procedencia de verdad** (el
titulo nombra **la vara del orden de la fase 03**, adjudicada en la 47 y no en esta) y quedan
**declarados con un `ROTULO` cotejado por maquina** contra `03_FUSIONES.md`.

### 7.3 **`ROJO` PROPIO 2: EL INSTRUMENTO SE CONTABA A SI MISMO**

Al adosar el registro de la TAREA 1.a, **la tabla de las cinco consumidas quedo dentro de
`03_FUSIONES.md`**, y `vuelta64_consumidas.py` volvio a encontrar el par de `MEDIOS` y el de `ADMIT`
**en su propia tabla**: **2 sitios donde la correccion necesita 1**, y el instrumento cayo en `ROJO`
al re-correrlo. **La guarda mordio, que es lo que tenia que pasar.** **ARREGLADO SIN ESCONDER NADA:**
el sitio que vale es el que vive **bajo una cabecera de tramo de `OP-U-01`**, y los demas se
**DECLARAN** en una linea propia. **La tabla publicada no cambia ni una celda.**

### 7.4 **UN TERCER `ROJO` QUE SE ARREGLO ANTES DE ESCRIBIR NADA**

`vuelta64_consumidas.py` buscaba el id **como subcadena suelta** y daba por bueno un sitio falso para
`OP-M-02-ACTIVATE` (**la linea 2112**, donde `fase_activate` es subcadena de
`seis_herramientas_comunicacion_fase_activate`). **Corregido a buscar el id entre comillas inversas
ANTES de escribir la correccion**, y con la vara estrecha `ACTIVATE` pasa de 1 a 0 rastros sueltos.
**Acertar por casualidad no es acertar.**

### 7.5 **Y UN `ROJO` DE MI PROPIO VERIFICADOR, cazado antes de publicar**

`_v64_verificar_opm03ii.py` dio `ROJO` en su comprobacion 2 diciendo que `merged_originals` no
cargaba el id que muere. **La averia era mia:** **ese campo NO tiene una sola forma en el catalogo**.
En `pivotar_o_perseverar` (vuelta 63) es **lista de cadenas**; aqui es **lista de diccionarios** con
`node_id`, `titulo` y `fuente`. **El verificador lee ahora las dos formas, imprime cual es, y cae en
`ROJO` si un nodo las MEZCLA.** **Queda dicho como hallazgo de esquema.**

### 7.6 **LAS PROMESAS DE MARCADO, POR MAQUINA**

**MEDIDO EN ESTA VUELTA:** `python scripts/loop/comprobar_promesas_de_marcado.py --reporte
docs/loop/REPORTE.md --plan docs/loop/PLAN_V64_OPM03II.json --plan docs/loop/PLAN_V63_OPM02PROG.json`
da **2 promesas, 2 CUMPLIDAS, 0 INCUMPLIDAS**
([`SALIDA_V64_PROMESAS_CUMPLIDAS.txt`](SALIDA_V64_PROMESAS_CUMPLIDAS.txt)).

**Y LA PRIMERA CORRIDA DIO UNA, NO DOS, Y ESO ES UN HALLAZGO QUE VA DICHO.** El comprobador busca la
frase **`VA MARCADO COMO DISCUTIBLE`, en singular**, y la nota del reparto de `PLAN_V64_OPM03II.json`
la habia escrito **en plural** (*LAS DOS VAN MARCADAS COMO DISCUTIBLES*). **La maquina no la vio.**
La regla que ese instrumento existe para volver mecanica **se estaba cumpliendo solo por atencion**,
que es exactamente lo que el acta 62 dejo dicho que no basta.

**COMO SE ARREGLA, y las dos mitades:** se anade al plan **la frase en la forma que la maquina lee**,
por **correccion declarada**, **sin quitar la otra y sin tocar ni una marca, ni una perdida, ni el
motivo** (comprobado tras escribir: las 7 marcas identicas, las 4 perdidas intactas, el motivo
identico y el texto viejo dentro). **Y LA ESTRECHEZ DE LA AGUJA NO LA ARREGLO YO:** tocar un
instrumento de **nombre estable** al cierre de la vuelta, y encima **uno que se coteja contra
reportes viejos**, es lo que se trae al auditor. **Va como pregunta en la seccion 8.**

---

## 8. PENDIENTES DE DOCTRINA Y PREGUNTAS

1. **PENDIENTE DE DOCTRINA (heredado y engordado): EL `INCISO` DE CONDICIONES NO EXISTE.** Esta
   vuelta anade **DOS** perdidas `DE CONDICIONES` mas por esa causa (la del `D10` y la de la
   condicion 1 de `pivotar_o_proceder`). **Es el costo medido de que ese instrumento no exista.**
2. **PENDIENTE DE DOCTRINA (heredado): EL ESQUEMA DE `OPERACIONES.jsonl`.** Ver `D7` y `D8`.
3. **PREGUNTA, y es la que mas me importa: QUIEN RESUELVE UNA COLISION DE CLASE CUYOS PUESTOS SON DE
   UNA MESA QUE NO SE HA EJECUTADO?** El carril general de colisiones (registrado en
   `03_FUSIONES.md`, linea **1377**) reparte en **volteo por maquina** (una `A` arrastrada contra un
   directo `D`) y **relectura en el mismo acto**. **Ninguna de las dos formas cubre este caso**: los
   cuatro puestos son `B` contra `D`, **el 668 esta nombrado literalmente entre los siete dudosos de
   `OP-M-03`** y su expediente **ya lo posiciona**, y `pivote_startup` es miembro de `OP-M-03-III`,
   pendiente. **No lo toco, y lo traigo.** Y con el una segunda mitad medida: **la deuda CRECE**,
   porque simulada `OP-M-03-III` las colisiones pasan de **2 a 3**.
4. **PREGUNTA: LAS FUSIONES DE MESA DEBEN CORRER ANTES QUE SUS PROPIAS MESAS?** Lo de arriba tiene
   una lectura mas ancha: `OP-M-03-I`, `OP-M-03-II` y `OP-M-03-III` son **fusiones que la mesa
   `OP-M-03` adjudico**, y **la mesa como tal no se ha ejecutado**. **No propongo cambiar el orden**
   (lo fija el `00_INDICE` y el campo `orden`), pero **queda dicho** que ejecutar las hijas antes que
   la madre es lo que fabrica estas colisiones.
5. **PREGUNTA: SE PUEDE APILAR MAS DE UN `INCISO` SOBRE EL MISMO PASO DEL SUPERVIVIENTE?** Ni el
   instrumento lo prohibe ni la doctrina lo permite con letra. **Lo resolvi como `NO`** (ver `D3`),
   **y si la respuesta es otra, el paso 5 de `pivotar_o_proceder` se puede rehacer sin tocar el
   grafo**, porque su perdida esta sellada y enrutada.
6. **PREGUNTA: LA AGUJA DEL COMPROBADOR DE PROMESAS DEBE ADMITIR EL PLURAL?** Hoy busca solo
   `VA MARCADO COMO DISCUTIBLE` y **una nota en plural se le escapa entera**, como se le escapo la de
   esta vuelta (seccion 7.6). **No lo toco**, porque es un instrumento de nombre estable que se
   coteja contra reportes viejos y ensancharle la aguja podria volver INCUMPLIDAS promesas que hoy no
   ve. **Lo traigo con la medicion: una promesa invisible es peor que una promesa incumplida, porque
   la segunda al menos sale en rojo.**
7. **PREGUNTA: UN CASO POSITIVO PUEDE APUNTAR A UN SUJETO QUE LA PROPIA VUELTA VA A EJECUTAR?** La
   regla dice que no, **y esta vuelta demuestra por que**. Lo que dejo abierto es si el sujeto
   deberia escogerse **por medicion** (el instrumento eligiendo un par vivo que la vuelta no toque)
   en vez de pasarse a mano, que sigue pudiendo equivocarse.

---

## 9. RUTAS TOCADAS, CORRECCIONES DECLARADAS Y CENSOS

**Del grafo (12 nodos, todos por la fusion):** `pivote_o_proceder`, `pivotar_o_proceder`,
`categorias_entusiasmo_cliente`, `checkpoints_validacion`, `decision_pivotar_o_proceder`,
`filosofia_validacion_clientes`, `mapa_flujo_trabajo_cliente`, `presentacion_solucion_producto`,
`product_market_fit`, `scorecard_descubrimiento_cliente`, `validar_posicionamiento_con_analistas` y
`verificar_modelo_ingresos`, mas `dataset/metadata/master_graph.json`,
`dataset/metadata/phase1_run_log.json` y los assets de `web/lib/assets/`.

**De registro:** `docs/plan/03_FUSIONES.md` (**+180** del acta 63 y **+126** del registro de la
fusion), `docs/plan/OPERACIONES.jsonl` (**5 notas**), `docs/loop/PLAN_V63_OPM02PROG.json`
(correccion declarada del `D10`), `docs/plan/ARISTAS_DUPLICADAS.jsonl`,
`docs/COSTURAS_INTERNAS.jsonl` y su resumen.

**CORRECCIONES DECLARADAS DE ESTA VUELTA, las SEIS, todas con el texto viejo entero:** las **cinco**
de las fichas consumidas (banco `9.10`) y la del `D10` sobre el plan de `OP-M-02-PROG`.

**Instrumentos nuevos.** De **nombre ESTABLE**: `scripts/loop/caso_positivo_de_fusion_de_mesa.py` y
`scripts/loop/fijar_tramo_de_opu02.py`. **De vuelta**: `vuelta64_consumidas.py`,
`vuelta64_correcciones_consumidas.py`, `vuelta64_d10.py`, `vuelta64_puesto2.py`,
`vuelta64_registrar_acta63.py`, `vuelta64_lectura_opm03ii.py` y `vuelta64_colisiones_opm03ii.py`.
**De contenido**: `_v64_opm03ii.py` y `_v64_verificar_opm03ii.py`.

**CENSO DE PLANTILLAS TALLADAS:** **CERO TALLADOS en los 22 instrumentos de nombre estable**
([`SALIDA_V64_CENSO_PLANTILLAS.txt`](SALIDA_V64_CENSO_PLANTILLAS.txt)), y son **22 y no 20** porque
los **dos nuevos entran en el censo**.

**BARRIDO AL CIERRE**, leido de la corrida de cierre y **no de ninguna anterior**
([`SALIDA_V64_BARRIDO_CIERRE.txt`](SALIDA_V64_BARRIDO_CIERRE.txt)): **421 ficheros barridos**,
**`ROJO` 32** (la linea de base heredada, **sin mover**), **`AMBAR` 0**, `ROTULADO` **37**, `CENSO`
**219**, `ILEGIBLE` **1**.

**FIGURAS Y FAMILIAS AL DIA:** esta vuelta no abre figura nueva. El acto fundido es **fusion de mesa
de par**, la misma figura de `OP-M-03-I` y `OP-M-02-PROG`, y la familia del pivote queda con
**`OP-M-03-III` pendiente** y con la mesa `OP-M-03` **sin ejecutar**.
