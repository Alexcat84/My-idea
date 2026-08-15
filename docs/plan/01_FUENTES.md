# FASE 01: LAS DECISIONES DE FUENTE

**Van primero, y el motivo no es de eficiencia: es que cambian lo que los nodos
dicen.** Una decision de fuente decide **de que libro es un nodo**, y de eso
depende que atribucion carga el superviviente de cualquier fusion posterior.

> **Tres decisiones en vez de dieciocho arreglos de nodo.** Es la misma economia
> de la mesa de racimos: **no se decide nodo por nodo si el checklist se parte; se
> decide una vez por libro y se aplica a todos sus nodos.**

**Operaciones: `OP-F-01`, `OP-F-02`, `OP-F-03`. LAS TRES LISTAS**, adjudicadas el
11 ago 2026.

| operacion | la adjudicacion, en una linea |
|---|---|
| **`OP-F-01`** | **MANDA LA CLASE**, sus ~~SIETE~~ **SEIS** miembros (correccion declarada del 14 ago 2026, ver abajo), no la cuenta de 18, que se recomputa con su corte |
| **`OP-F-02`** | el injerto **se desteje** y el bloque de IA **se REUNE** en un solo destino: el racimo de supervision de la IA, diez miembros |
| **`OP-F-03`** | nomina medida: **VEINTIUN nodos** que declaran Hugos junto a otra fuente. La tarea es verificar en cada uno si el contenido pegado es de cadena de suministro |

---

## EL PRECEDENTE QUE MANDA: FUENTE PRIMERO

**No es una recomendacion de orden. Es que cualquier otro orden obliga a rehacer.**

> **1. LA FUENTE PRIMERO.** Mientras no este decidido de que libro es un nodo,
> cualquier fusion **escribe la atribucion equivocada en el superviviente**. Y el
> superviviente es el que se queda: **el error se vuelve permanente.**
>
> **2. EL DESTEJIDO DESPUES.** Con la fuente ya fijada se le quita la repeticion
> interna. **Antes no**, porque el destejido decide **que bloques sobreviven**, y
> esos bloques son los que van a cargar la atribucion.
>
> **3. LOS GEMELOS AL FINAL, y todos en un solo acto.** Solo con el nodo ya
> destejido se puede ver que le queda propio frente a cada gemelo.

**EVIDENCIA**: `PENDIENTES.md`, seccion *`brainstorming_divergente`: el nodo de
mas frentes del catalogo*, apartado *EL ORDEN ES PROPIO Y NO ES NEGOCIABLE*. Y la
recomendacion escrita en `INTRA_DOMINIO_INFORME.md`, CRUCE 1: *el cruce se ejecuta
FUENTE PRIMERO*.

> **El ejemplar que lo prueba es `brainstorming_divergente`**, y por eso `OP-F-02`
> **bloquea** a `OP-D-04`. Es la unica dependencia dura entre las fases 01 y 02.

---

## LA ARITMETICA DE LOS DIECIOCHO, y una discrepancia que se declara

| decision de fuente | publicado | **adjudicado y medido** | operacion |
|---|---:|---:|---|
| los **formatos lista** | 4 (solo *Basic Guide*) | **7, la clase entera** | `OP-F-01` |
| la **tanda de Mollick** | 3 | **3** | `OP-F-02` |
| el **pegado de Hugos** | 11 confirmadas | **21 con la firma del injerto** | `OP-F-03` |
| **total** | **18** | **31** | |

> **LA DISCREPANCIA QUEDO RESUELTA POR ADJUDICACION: manda la CLASE, no la
> cuenta.** La cifra de 18 tomaba cuatro de los siete miembros de LARGO LEGITIMO y
> dejaba fuera dos de *Juran* y uno de `core`. **La cuenta se recomputa con su
> corte y deja de gobernar el alcance.**

> **Y los dos numeros de Hugos conviven porque cuentan cosas distintas**: **11**
> son costuras confirmadas con pegado de Hugos; **21** son todos los nodos vivos
> con la firma del injerto, o sea los que declaran Hugos **en segundo lugar**
> junto a otro libro. **El plan usa la de 21, por adjudicacion.**

> **CORRECCION DECLARADA, 14 ago 2026 (vuelta 26), AL EJECUTAR `OP-F-01`: LA FILA DE LOS
> FORMATOS LISTA ES DE SEIS Y EL TOTAL DE TREINTA. La tabla de arriba se queda entera.**
> Es la tercera linea de verificacion de `OP-F-01` (*la cifra de 18 se reescribe con su
> corte alli donde este publicada*) aplicada a la sede de este archivo, despues de que
> la decision del fundador del 14 ago 2026 sacara a `background_startup_vs_corporativo`
> de la clase por `P.17`.
>
> | decision de fuente | publicado | adjudicado el 11 ago | **medido hoy, 14 ago 2026** |
> |---|---:|---:|---:|
> | los **formatos lista** | 4 | ~~7~~ | **6** |
> | la **tanda de Mollick** | 3 | 3 | **3** |
> | el **pegado de Hugos** | 11 | 21 | **21** |
> | **total** | **18** | ~~**31**~~ | **30** |
>
> **La cifra sale del campo `nodos` de las tres operaciones en `OPERACIONES.jsonl`, contado
> hoy con `scripts/loop/vuelta26_medir.py`: 6 mas 3 mas 21, treinta ids distintos y cero
> solape entre las tres.** **Lo que NO cambia es la adjudicacion: sigue mandando la clase y
> no la cuenta**, y la cuenta de 18 sigue sin gobernar el alcance.

---

## `OP-F-01`: LOS FORMATOS LISTA

**Que es la clase.** Nodos que **superan el estandar de 3 a 6 pasos pero NO
tienen narracion repetida dentro**. Una lista canonica de principios, un metodo
canonico en secuencia unica o un checklist de criterios **no son narraciones
apiladas: son formatos donde el numero de pasos lo fija el contenido, no el
autor.**

**LOS CUATRO DE LA CUENTA, todos del *Basic Guide to Exporting*:**

| nodo | pasos | corte | que es |
|---|---:|---:|---|
| `seleccion_representante_extranjero` | 9 | 5 | nueve criterios distintos para evaluar a un candidato |
| `internacionalizacion_sitio_web_exportacion` | 9 | **3** | nueve mejoras del sitio para vender fuera |
| `elaboracion_pro_forma_invoice` | 8 | 4 | los campos de un documento: ocho, cero narracion |
| `elementos_plan_exportacion_ejemplo` | 13 | 10 | trece elementos de un plan, ninguno repite a otro |

**LOS TRES DE LA CLASE QUE LA CUENTA NO INCLUYE:**

| nodo | fuente | pasos |
|---|---|---:|
| `principios_medicion_efectiva` | *Juran's Quality Handbook* | 10 |
| `fmea_analisis_de_modos_de_falla` | *Juran's Quality Handbook* | 8 |
| `background_startup_vs_corporativo` | *The Founder's Dilemmas* con *The Hard Thing About Hard Things* | 9 |

> **La firma de la clase es el CONTENIDO, no el ancho del corte.**
> `internacionalizacion_sitio_web_exportacion` tiene **corte 3**, la evidencia mas
> delgada del instrumento, y sigue siendo formato lista. **El corte ancho la
> delata a menudo; no la define.**

> **Y el septimo rompe la exclusividad de los manuales.**
> `background_startup_vs_corporativo` sale de dos libros de fundadores, lo que dice
> que **el formato lista no es propiedad de los manuales, solo su casa mas
> frecuente.**

**ADJUDICADO: MANDA LA CLASE.** La unidad de decision es **la clase entera, sus
~~siete~~ miembros**, y no los cuatro que la aritmetica de los 18 tomaba. **La cuenta
de 18 se recomputa con su corte y deja de gobernar el alcance.**

> **La consecuencia operativa es exacta: el alcance pasa de CUATRO a ~~SIETE~~ nodos,
> y la decision deja de depender de la fuente.** Que el septimo salga de dos libros
> de fundadores y no de un manual **ya no es una excepcion que discutir**: es la
> prueba de que la clase, y no el libro, es lo que manda.

**VERIFICACION**: los ~~siete~~ tratados por la misma regla, sin excepciones caso por
caso; ningun nodo de la clase con pasos alterados; y **la cifra de 18 reescrita
con su corte alli donde este publicada**.

> **CORRECCION DECLARADA (14 ago 2026, decision del fundador, camino A, regla P.17
> del banco del plan): `background_startup_vs_corporativo` SALE de esta clase.** El
> parrafo de arriba y la tabla de los tres se quedan enteros: el nodo SI declaraba
> dos libros de fundadores y esa lectura no era falsa. **Lo que cambio es cual de
> las dos clasificaciones vigentes manda.** El mismo nodo tambien estaba LEIDO Y
> CONFIRMADO como injerto de Horowitz en `OP-F-04-HOR`, con frontera publicada dos
> veces en este archivo (1 a 4 de Wasserman, 5 a 9 de Horowitz, ver LA NOMINA DE LOS
> 14 DE HOROWITZ mas abajo). **Por P.17, LA LECTURA VENCE AL METADATO**: una
> pertenencia confirmada contra los pasos con frontera escrita pesa mas que una
> argumentada por la fuente del nodo. El nodo se desteje por `OP-F-04-HOR`.
> **LA CLASE QUEDA EN SEIS MIEMBROS** (los 4 del Basic Guide mas los 2 de Juran), y
> el alcance pasa de CUATRO a SEIS, no a SIETE. **La leccion de la clase NO se
> cae**, cambia de ejemplar: la clase sigue mandando sobre la fuente para los seis
> que quedan; lo unico que se pierde es este ejemplo particular de que ademas puede
> mandar sobre un libro de fundadores. `OP-F-01` en `OPERACIONES.jsonl` lleva la
> misma correccion en su campo `nodos` y en su `verificacion`.

---

## `OP-F-02`: LA TANDA DE MOLLICK

**Tres nodos de metodo de taller llevan a Mollick pegado como segunda voz**, con
el metodo rehecho con IA como segundo bloque. **Confirmado las tres veces.**

| nodo | su fuente real | lo pegado |
|---|---|---|
| `future_scenarios_planning` | *Business Model Generation* (Osterwalder) | **Mollick** |
| `gut_check` | *The field guide to human-centered design* (IDEO) | **Mollick** |
| `brainstorming_divergente` | *Change by Design* (Tim Brown) | **Mollick** |

> **Lo que la medicion agrava, y no estaba en el encargo: 51 nodos declaran a
> Mollick y 48 son de tema IA por su propio id.** O sea que la tanda entro **dos
> veces y de dos maneras**: como **familia propia de 48 nodos**, que es lo
> correcto, **y ademas como injerto en 3 nodos de taller que ya existian.**
>
> **El material de IA ya tenia adonde ir.** Los tres injertos **no se hicieron por
> falta de sitio.**

**ADJUDICADO: SE DESTEJE Y SE REUNE.** El injerto se separa, y **el bloque de IA
no se poda: se REUNE en un solo destino**, el racimo de la **supervision de la
IA**, que hoy tiene **DIEZ miembros**. **El taller que queda entra a su propia
fusion.**

> **El verbo es REUNIR, y eso cambia la operacion entera.** No se pierde material:
> el bloque de IA de los tres viaja **entero** a donde ya vivia su familia. Y el
> taller conserva su fuente real: Osterwalder, IDEO y Tim Brown.

**AVISO DE COBERTURA (banco 9.26)**: la nomina de diez y su particion provisional
de **5 mas 4 mas 1** estan **vigentes al puesto 1517, con cobertura de 14 pares de
45**. Basta una A entre el bloque humano y el del mapa para que vuelvan a ser uno.
**La reunion no depende de esa particion, pero el destino se re-mide despues.**

**LO QUE BLOQUEA**: `brainstorming_divergente` es uno de los tres, y es el ancla
del acto mayor del cierre transitivo. **`OP-F-02` bloquea a `OP-D-04`.**

### LA FRONTERA DE LOS TRES DE MOLLICK, leida del grafo y publicada ANTES de cortar

**Escrita el 14 ago 2026 (vuelta 26) al ejecutar `OP-F-02`, por el mismo metodo de la
tabla de LOS 14 DE HOROWITZ: se lee cada nodo contra sus `pasos_accionables` y se publica
el tramo.** Los pasos enteros de los tres estan en la salida del instrumento de la vuelta
(`docs/loop/SALIDA_V26_OPF02_LECTURA.txt`, `scripts/loop/vuelta26_medir.py opf02`); aqui
va el saldo de la lectura. **Ningun nodo se toco para escribir esta tabla.**

| # | nodo | libros declarados | pasos | frontera leida | **el bloque de Mollick** |
|---:|---|---|---:|---|---|
| 1 | `future_scenarios_planning` | Osterwalder \| **Mollick** | **13** | **1 a 5 / 6 a 13** | **apendice AL FINAL**, y **entra DOS VECES**: 6 a 9 y 10 a 13 |
| 2 | `gut_check` | IDEO \| **Mollick** | **9** | **1 a 4 / 5 a 9** | **apendice AL FINAL** |
| 3 | `brainstorming_divergente` | Tim Brown \| **Mollick** | **8** | **1 a 4 / 5 a 8** | **apendice AL FINAL** |

**LO QUE SOSTIENE CADA CORTE, y es el ultimo paso del bloque 1 contra el primero del 2:**

| nodo | cierra el bloque 1 | abre el bloque 2 |
|---|---|---|
| `future_scenarios_planning` | paso 5, *formular preguntas por bloque del Canvas (KP, KA, VP, CR, CS, C$, R$)*: **Canvas es Osterwalder** | paso 6, *que tareas criticas podrian automatizarse bajo crecimiento lineal de IA* |
| `gut_check` | paso 4, *estar dispuesto a descartar ideas que no superen la evaluacion critica*: cierra el filtro humano de IDEO | paso 5, *describir el plan o modelo de negocio a la IA con suficiente detalle* |
| `brainstorming_divergente` | paso 4, *registrar todas las ideas visualmente (post-its, pizarra)*: cierra la sesion de Tim Brown | paso 5, *usar la IA como un participante mas en sesiones de brainstorming* |

> **EL PRIMERO NO ES UN SIMPLE APENDICE, y se dice aparte como se dijo de los otros tres
> del plan.** En `future_scenarios_planning` el bloque de IA **entra dos veces**: los pasos
> **6 a 9** (automatizacion lineal, capacidad por 10 o por 100, plan de contingencia,
> revision trimestral) y los **10 a 13** (dos o tres escenarios de evolucion de la IA,
> impacto, senales de alerta, revision periodica) **son la misma cuenta escrita dos veces**.
> Es la misma especie de `coeficiente_viral`, y le toca el mismo remedio: **TOQUE UNICO**,
> se separa el apendice y se desteje la repeticion en el mismo acto.

> **DISCREPANCIA DECLARADA, y no la resuelvo copiando** (regla 1 de `EJECUTOR.md`).
> `INTRA_DOMINIO_INFORME.md` publica, con su corte anterior, que
> `future_scenarios_planning` tiene *trece, de los cuales **nueve** son un bloque de IA
> entero*. **Leido hoy contra sus pasos, el bloque es de OCHO** (6 a 13), porque el paso 5
> es el del Canvas y es de Osterwalder. **Los cinco elementos que aquella nota enumera
> estan todos dentro de mis ocho**, asi que la discrepancia es de conteo y no de contenido.
> **El texto viejo se queda entero donde esta**; esta linea le pone la medida de hoy al
> lado.

### EL DESTINO DE CADA BLOQUE, decidido POR LECTURA sobre la nomina vigente

**CORRECCION DECLARADA, 14 ago 2026 (vuelta 26), al ejecutar `OP-F-02` con la regla de
destino por lectura que el fundador escribio en la nota de la operacion.** La nomina
contra la que se leyo es la **vigente al puesto 1517, DIEZ miembros**, con su cobertura al
lado como manda el banco 9.26: **14 de 45 pares**, PROVISIONAL. Los diez se leyeron enteros
hoy contra sus pasos (`docs/loop/SALIDA_V26_RACIMO_IA.txt`).

**EL OBJETO DEL RACIMO, escrito por el propio informe y no por mi:** *el racimo se definio
por la SUPERVISION, no por la mencion*, y su particion es **quien decide y quien revisa**
(bloque humano, 5), **probar la maquina tarea por tarea y anotar donde rinde** (bloque del
mapa, 4) y **los sesgos y la etica del modelo** (el suelto).

| bloque de IA | su objeto, leido | miembro cuyo objeto coincida | **destino** |
|---|---|---|---|
| `future_scenarios_planning` **6 a 13** | **planificar frente a la EVOLUCION FUTURA de la IA**: escenario lineal contra exponencial, impacto en el modelo de negocio, plan de contingencia, senales de alerta, revision periodica | **ninguno**. El bloque del mapa prueba lo que la maquina hace **HOY**; ninguno de los diez proyecta lo que hara | **NODO PROPIO** dentro del racimo |
| `gut_check` **5 a 9** | **someter TU PLAN a la critica de la IA**: diez formas de fallar, una vision de exito alternativa, personajes que lo critican, documento de riesgos | **ninguno**, y la direccion se invierte: en los diez **el humano supervisa a la IA**; aqui **la IA audita al humano** | **NODO PROPIO** dentro del racimo |
| `brainstorming_divergente` **5 a 8** | **generar ideas CON la IA en la sesion**: participante mas, personas y estilos, lote grande mas filtrado humano, cruce de conceptos | **ninguno**. El mas cercano es `invitar_ia_a_todo` (con `principio_invitar_ia_siempre`), pero su objeto es **probar la IA en todas las tareas para mapear la frontera**, no generar ideas | **NODO PROPIO** dentro del racimo |

> **LA VARA CON QUE DESCARTE AL MAS CERCANO ES LA DEL PROPIO RACIMO**, y no una mia:
> `INTRA_DOMINIO_INFORME.md` 11.bis.2 la escribio al decidir dos absorciones opuestas:
> **una pareja vecina se absorbe cuando HACE LO MISMO que un miembro, y no cuando
> DESARROLLA UNA LINEA suya.** El bloque de `brainstorming_divergente` **desarrolla una
> linea** de *invitar la IA a todo*: es una aplicacion a la ideacion, no el mismo acto. Por
> esa vara **no se absorbe**.

> **Y LO QUE ESTE DESTINO CONFIRMA, dicho porque es lo contrario de lo que parecia:** el
> aviso del informe de que `future_scenarios_planning` **NO es miembro del racimo** sigue
> siendo cierto **y ahora se entiende mejor**. El nodo no entra; **su bloque de IA si**, y
> entra como nodo nuevo, no como miembro reciclado. **Un nodo con pasos de IA no es un nodo
> del racimo de la IA**, pero un bloque de IA destejido **si puede ser uno**.

**LOS TRES DESTINOS SON NODO PROPIO, Y ESO NO SE PUDO EJECUTAR HOY.** El corte quedo SIN
HACER y los tres nodos **estan intactos**. El motivo no es de lectura ni de doctrina: es
que **crear un nodo pone `Gate 0` en ROJO** por el chequeo de vector semantico, y su
remedio escrito necesita credenciales que estan fuera del repo mientras el bucle corre.
**Esta medido y reproducido**, y va como PARADA en el reporte de la vuelta 26
(`docs/loop/REPORTE.md`), con la salida del instrumento en
`docs/loop/SALIDA_V26_MURO_INDICE.txt`.

### EL CORTE SE HIZO, SE VERIFICO ENTERO Y SE DESHIZO: **EL MURO TIENE UNA SEGUNDA HILADA QUE NADIE HABIA MEDIDO** (14 ago 2026, vuelta 27)

**El parrafo de arriba se queda entero, y ahora hay que anadirle lo que le faltaba.** La
decision del fundador (opcion B estricta, registrada en `08_VERIFICACION.md`) levanta la
primera hilada: permite el **ROJO DECLARADO del indice semantico exclusivamente para los ids
que la pasada acaba de crear**, y con ella **el corte de `OP-F-02` se ejecuto entero y paso
todas sus guardas**. Pero **hay una segunda hilada**, medida por primera vez hoy:

> **EL GUARDIAN DE COMMIT (`.githooks/pre-commit`) CORRE LA SUITE DEL MOTOR Y ABORTA EL
> COMMIT SI ESTA EN ROJO**, y `engine/test_aviso_curaduria.py` contiene **el mismo chequeo
> del indice semantico**, midiendo el estado real del repo. **Con los tres nodos nuevos en el
> arbol, NINGUN commit entra al historial**, ni siquiera uno que no los toque.

**El rojo del indice esta permitido en `Gate 0` por decision escrita del fundador, y el
historial lo rechaza igual.** Las dos reglas son vigentes y no se pueden cumplir juntas el
dia que una operacion crea un nodo. **Eso es PARADA, y no la resuelve el ejecutor**: la
salida esta en `docs/loop/SALIDA_V27_MURO_GUARDIAN.txt`, con el hook entero y el commit
abortado. **El corte quedo deshecho y los tres nodos vuelven a estar intactos**; lo que
sigue en pie es la medicion, que se publica aqui para que la proxima vuelta solo tenga que
aplicarla:

| # | origen | frontera aplicada | pasos antes / despues | **nodo propio creado** |
|---:|---|---|---:|---|
| 1 | `future_scenarios_planning` | **1 a 5 / 6 a 13** | 13 -> **5** | **`escenarios_de_evolucion_de_la_ia`**, 6 pasos |
| 2 | `gut_check` | **1 a 4 / 5 a 9** | 9 -> **4** | **`critica_del_plan_con_ia`**, 5 pasos |
| 3 | `brainstorming_divergente` | **1 a 4 / 5 a 8** | 8 -> **4** | **`ideacion_con_ia_en_la_sesion`**, 4 pasos |

**LA FUENTE DE LOS TRES QUEDA REDUCIDA AL LIBRO QUE LES CORRESPONDE**, que es lo que la
operacion manda preservar: Osterwalder, IDEO y Tim Brown. **Ninguno de los tres declara ya
a Mollick**, y **el material de IA no se podo: viaja entero a la familia**, que es el verbo
de la adjudicacion.

**EL TOQUE UNICO DEL PRIMERO, ejecutado y con su mapa al lado.** Los ocho pasos que salen de
`future_scenarios_planning` **entran como SEIS** en el nodo nuevo, porque los tramos 6 a 9 y
10 a 13 eran la misma cuenta escrita dos veces. **Ningun elemento se pierde**, y por eso el
mapa se publica en vez de resumirse:

| paso del nodo nuevo | de que pasos de origen sale |
|---:|---|
| 1, definir dos o tres escenarios de evolucion, del lineal al exponencial | **7 y 10** |
| 2, que tareas criticas podrian automatizarse en cada escenario | **6** |
| 3, impacto en modelo de negocio, fuerza laboral y propuesta de valor | **7 y 11** |
| 4, plan de contingencia o pivote que contemple al menos dos escenarios | **8** |
| 5, senales de alerta temprana regulatorias, tecnologicas y de mercado | **12** |
| 6, revisar y ajustar la adopcion periodicamente segun esas senales | **9 y 13** |

> **LA COBERTURA DEL MAPA ES LA GUARDA: los ocho pasos de origen (6 al 13) aparecen todos en
> la columna derecha.** El instrumento no deja ejecutar un destejido cuyo mapa deje un paso
> fuera (`scripts/loop/vuelta27_cortar.py`, guarda de cobertura).

**LA UNICA ARISTA QUE SE ESCRIBE ES LA QUE LA CREACION DE UN NODO OBLIGA:** de cada origen a
su nodo nuevo (`nodos_siguientes` en el origen, `nodos_previos` en el nuevo). **Cero aristas
mas**, y el campo `aristas_nuevas` de la operacion sigue vacio: **la pertenencia a la familia
la declara la `fuente`**, que es como este plan nombra a las familias de libro.

**EL CASO POSITIVO, corrido antes y despues** (`scripts/loop/vuelta27_caso_positivo.py opf02`):
**seis pruebas, las seis CAEN antes del corte y las seis PASAN despues.** Las salidas de las
dos corridas estan en `docs/loop/SALIDA_V27_OPF02_CASO_ANTES.txt` y
`docs/loop/SALIDA_V27_OPF02_CASO_DESPUES.txt`.

**Y `GATE 0` SALIO CON UN SOLO ROJO Y FUE EL DECLARADO**, medido con el corte aplicado
(`docs/loop/SALIDA_V27_GATE0_OPF02.txt`): *3 activos sin vector*, y son exactamente los tres
ids nuevos, **ninguno mas**; los otros diecinueve chequeos en verde, **71 etiquetas sin
encoger** y las dos copias del grafo en el mismo blob. **La operacion es ejecutable; lo que
no es committeable es su resultado.**

> **EL PLAN DEL CORTE QUEDA ESCRITO Y SELLADO** en `docs/loop/PLAN_V27_OPF02.json`, con la
> frontera, los prefijos de cada paso que sale leidos del grafo de hoy, el mapa del
> destejido y el cuerpo entero de los tres nodos nuevos. **Aplicarlo es un comando**
> (`python scripts/loop/vuelta27_cortar.py docs/loop/PLAN_V27_OPF02.json --ejecutar`), y
> **no hay que volver a leer nada**.

---

## `OP-F-03`: EL PEGADO DE HUGOS

**ADJUDICADO, y la nomina ya existe: VEINTIUN NODOS** que declaran Hugos **junto a
otra fuente**. **La tarea es verificar en cada uno si el contenido pegado es de
cadena de suministro**, como en `gestion_libro_abierto_obm`.

**VERIFICADO CONTRA EL GRAFO el 11 ago 2026: los 21 son nodo VIVO y los 21
declaran Hugos junto a otra fuente. 21 de 21.**

> **Y el barrido independiente del mismo dia explica por que son esos y no otros:
> 128 nodos vivos declaran Hugos, y solo estos 21 lo declaran EN SEGUNDO LUGAR.**
> Los otros 107 lo tienen como fuente unica, que es lo normal. **La firma del
> injerto no es citar a Hugos: es citarlo detras de otro libro.**

**LOS VEINTIUNO, todos de `core`:**

`analisis_tco_roi_b2b`, `asociaciones_clave`, `bundle_ideas`, `co_creation_session`,
`criterios_seleccion_proveedores`, `economia_circular_como_modelo_de_negocio`,
`empoderamiento_de_participantes`, `gestion_cuentas_por_cobrar`,
`gestion_inventario`, `gestion_libro_abierto_obm`, `mapa_de_canal_de_ventas`,
`modelo_hibrido_agile_stage_gate`, `principio_calidad_mvp`,
`procesamiento_paralelo_con_espirales`, `producto_unico_superior`,
`propuesta_gasto_capital`, `ratios_eficiencia_inventario`,
`reduccion_tamano_de_lote_batch_size`, `schedule_management_plan`,
`seleccion_estrategia_pricing`, `transicion_producto_a_experiencia`.

**EL EJEMPLAR DE REFERENCIA**: `gestion_libro_abierto_obm`, que la ficha ya cito
por **declarar un libro cuyo material no aparece en ningun paso**. Ese es el
patron que hay que buscar en los otros veinte.

**LOS DOS DESENLACES, y cada uno tiene su remedio escrito:**

| lo que se encuentre | que se hace |
|---|---|
| **el bloque SI es de cadena de suministro** | se separa, y se decide **poda o reparto** a la subfamilia Hugos del nucleo. **Hay adonde repartir**: la ficha ya verifico que la mitad de Hugos de un nodo tiene parientes ahi |
| **el bloque NO es de cadena de suministro** | **la fuente se corrige**: el nodo declara un libro cuyo material no aparece |

> **TRES DE LOS 21 CRUZAN CON LA FASE 02**: `principio_calidad_mvp` esta en
> `OP-D-01` y en `OP-D-06`; `producto_unico_superior` y `propuesta_gasto_capital`
> estan en `OP-D-06`. **En los tres manda el orden fuente primero.**

### LOS 21 LEIDOS UNO A UNO, con su veredicto y su frontera (14 ago 2026, vuelta 26)

**Es la primera linea de verificacion de `OP-F-03`, ejecutada: *los 21 leidos uno a uno, con
el veredicto escrito: el bloque es de cadena de suministro, si o no*.** Los 21 se leyeron
hoy contra sus `pasos_accionables` con `scripts/loop/vuelta26_medir.py bloque`, salida en
`docs/loop/SALIDA_V26_OPF03_LECTURA.txt`. **Los 21 estan VIVOS y los 21 declaran Hugos en
segunda o posterior posicion**, reproducido hoy: la nomina de 21 no se movio.

**EL SALDO, y la tercera columna es la que no estaba prevista:**

| veredicto | nodos | que se hace, segun la letra de la operacion |
|---|---:|---|
| **SI es de cadena de suministro** | **12** | el bloque se separa, y se decide **poda o reparto** a la subfamilia Hugos del nucleo |
| **NO: la fuente declara un libro cuyo material no aparece** | **2** | **la fuente se corrige** |
| **TERCERA CLASE, que la operacion no contempla: es material de Hugos, pero de su parte de SISTEMAS, no de cadena de suministro** | **7** | **ninguno de los dos remedios encaja.** Ver el pendiente de doctrina de abajo |

**LOS DOCE QUE SI, con su frontera leida:**

| nodo | pasos | frontera | **el bloque de Hugos** |
|---|---:|---|---|
| `analisis_tco_roi_b2b` | 9 | **1 a 4 / 5 a 9** | evaluacion ponderada de **proveedores**: criterios cualitativos, pesos, costo total por proveedor |
| `asociaciones_clave` | 12 | **1 a 4 / 5 a 8 / 9 a 12** | alianzas con **compromiso de compra anticipada a cambio de garantia de suministro**; y un segundo bloque de KPIs conjuntos y horizonte de 3 a 5 anos |
| `co_creation_session` | 9 | **1 a 4 / 5 a 9** | **lo dice con esas palabras**: *invitar a todos los socios relevantes de la cadena de suministro* |
| `criterios_seleccion_proveedores` | 10 | **1 a 6 / 7 a 10** | sourcing: mirar mas alla del precio, **reducir el numero de proveedores para concentrar volumen**, lista de preferidos |
| `economia_circular_como_modelo_de_negocio` | 9 | **1 a 5 / 6 a 9** | remanufactura y **costos de materiales y logistica**, y **repite el bloque 1**: el paso 6 vuelve sobre el ciclo de vida del paso 1 |
| `empoderamiento_de_participantes` | 8 | **1 a 4 / 5 a 8** | coordinacion de **la red operativa**: objetivos comunes, informacion en tiempo real compartida entre nodos |
| `gestion_cuentas_por_cobrar` | 9 | **1 a 4 / 5 a 9** | credito y cobranza como proceso de entrega: politicas de credito, aprobacion de ventas, **EFT y cartas de credito internacionales** |
| `gestion_inventario` | 9 | **1 a 5 / 6 a 9** | **inventario ciclico, stock de seguridad, estacionalidad y punto de reorden**: es Hugos puro |
| `mapa_de_canal_de_ventas` | 8 | **1 a 5 / 6 a 8** | **mapear la cadena entera incluyendo proveedores del proveedor y clientes del cliente** |
| `producto_unico_superior` | 8 | **1 a 6 / 7 a 8** | **el mas delgado de los doce, dos pasos**: proveedores y socios que innovan contigo como ecosistema |
| `ratios_eficiencia_inventario` | 8 | **1 a 4 / 5 a 8** | **el ciclo de conversion de efectivo (cash to cash cycle time)**, metrica canonica de Hugos |
| `transicion_producto_a_experiencia` | 12 | **1 a 4 / 5 a 8 / 9 a 12** | **analizar el impacto en la cadena de suministro**; y un segundo bloque que repite los pasos 5 y 6 y anade las tres interfaces de usuario |

**LOS DOS QUE NO, y su fuente se corrige, que es el remedio escrito:**

| nodo | pasos | que dice la lectura |
|---|---:|---|
| `gestion_libro_abierto_obm` | 10 | **el ejemplar de referencia, CONFIRMADO**: los pasos 6 a 10 son cultura de libro abierto (lenguaje de socios, reglas del juego, marcador visible, recompensas). **No hay una linea de cadena de suministro en los diez** |
| `seleccion_estrategia_pricing` | 6 | **el caso mas limpio de los 21: NO HAY BLOQUE**. Los seis pasos son de Blank de principio a fin (tipo de mercado, precio de la competencia, value contra competitive pricing, ingresos recurrentes, TCO en B2B, validar con clientes) |

**LOS SIETE DE LA TERCERA CLASE, y el patron se repite tan igual que se nombra:**

| nodo | frontera | el bloque, y de donde sale |
|---|---|---|
| `bundle_ideas` | **1 a 4 / 5 a 9** | una sola combinacion de tecnologia o proceso que sirva para varios objetivos, y evaluar riesgo y costo antes de decidir |
| `modelo_hibrido_agile_stage_gate` | **1 a 9 / 10 a 13** | objetivo final ambicioso, **hitos de 30, 60 y 90 dias**, version funcional por ciclo |
| `principio_calidad_mvp` | **1 a 5 / 6 a 10 / 11 a 14** | el tercer bloque: funcionalidades criticas, excluir las secundarias, lanzar la minima viable, iterar con el uso real |
| `procesamiento_paralelo_con_espirales` | **1 a 4 / 5 a 9** | partes independientes, tareas en paralelo, plan B, recortar funciones sin perder lo esencial |
| `propuesta_gasto_capital` | **1 a 5 / 6 a 12** | **costos de hardware y software**, beneficios directos, incrementales, de evitacion e intangibles, VPN trimestral del proyecto |
| `reduccion_tamano_de_lote_batch_size` | **1 a 5 / 6 a 9** | secuencia de proyectos pequenos, **reutilizar infraestructura existente antes de reemplazarla**, time boxes |
| `schedule_management_plan` | **1 a 5 / 6 a 10** | seccion por objetivo, tareas de diseno y construccion, dependencias, **time boxes** |

> **POR QUE SON UNA CLASE Y NO SIETE CASOS SUELTOS.** Los siete traen **el mismo material**:
> *piensa en grande, empieza pequeno, entrega rapido*, hitos de 30, 60 y 90 dias, time boxes,
> reutilizar lo que ya existe, y justificar la inversion contando beneficios directos,
> incrementales, de evitacion e intangibles. **Eso es de Hugos, pero de su parte de COMO SE
> CONSTRUYE UN SISTEMA, no de cadena de suministro.** Y hay una prueba cruzada:
> `transicion_producto_a_experiencia`, que si tiene bloque de cadena de suministro, trae
> ademas en su paso 11 **las tres interfaces de usuario (humano computadora, humano maquina,
> humano humano)**, que es de esa misma parte del libro. **El injerto no vino de un capitulo:
> vino de dos.**

> **PENDIENTE DE DOCTRINA, y lo registro sin escribir la regla** (regla 4 de `EJECUTOR.md`).
> `OP-F-03` ofrece **dos** desenlaces y los siete no caben en ninguno: **la fuente NO esta
> mal** (el material del libro declarado si aparece, asi que corregirla borraria una
> atribucion cierta) **y el bloque NO es de cadena de suministro** (asi que repartirlo a la
> subfamilia Hugos del nucleo lo metaria donde no es). **Lo mejor sostenido que puedo dejar
> escrito es la lectura de arriba, con su frontera por nodo, y la clase nombrada.**

> **SEGUNDO PENDIENTE, y este toca una premisa publicada de `P.3`.** La tabla de `P.3` clasifica
> el caso Hugos como **de OTRO tema** (*cadena de suministro dentro de nodos de producto y de
> finanzas*) y de ahi concluye que **la poda era segura**. **Medido hoy nodo por nodo, la
> premisa falla en al menos cuatro de los doce**: en `gestion_inventario`,
> `ratios_eficiencia_inventario`, `criterios_seleccion_proveedores` y `analisis_tco_roi_b2b`
> **el bloque es del MISMO tema que el nodo** (inventario dentro de un nodo de inventario,
> seleccion de proveedores dentro de un nodo de seleccion de proveedores). **Por la regla de
> `P.3`, y no contra ella, a esos cuatro les toca REPARTO OBLIGATORIO y la poda deja de ser
> opcion.** **La regla se sostiene entera; lo que no se sostiene es aplicar su ejemplo a los
> 21 en bloque.** No lo arreglo yo: va al reporte.

**LO QUE SE EJECUTO HOY DE `OP-F-03`, y lo que NO:**

| | |
|---|---|
| **HECHO** | los 21 leidos uno a uno con veredicto y frontera escritos, que es su primera linea de verificacion; y **la fuente corregida en los dos que la tenian mal**, que es su tercera |
| **NO HECHO** | la separacion del bloque en los doce que si. **Ni un paso se movio**: la eleccion entre poda y reparto no se sostiene mientras la premisa de `P.3` este contradicha por la medicion en cuatro de ellos, y el reparto necesita destinos que hoy chocan con el muro del indice semantico (ver el reporte de la vuelta 26) |

### EL REPARTO, EJECUTADO POR `P.18` EN QUINCE DE LOS DIECINUEVE (14 ago 2026, vuelta 27)

**La tabla de arriba se queda entera: era el estado del dia en que se escribio.** Lo que la
desbloquea son las dos decisiones del fundador del 14 ago 2026: **`P.18` da el metodo para
elegir destino dentro de la familia**, y **el tercer desenlace escrito manda los siete de la
tercera clase a la familia `HUGOS-SISTEMAS`**. La nomina contra la que se leyo se midio HOY,
no se copio: **126 nodos vivos declaran a Hugos y 107 lo declaran como fuente UNICA**
(`docs/loop/SALIDA_V27_FAMILIA_HUGOS.txt`).

**LOS OCHO DE CADENA QUE SE REPARTIERON, con el miembro elegido y la lectura que lo sostiene:**

| origen | frontera | miembro receptor | por que su objeto coincide |
|---|---|---|---|
| `asociaciones_clave` | **5 a 8** | `estrategia_captura_mercado_crecimiento` | los dos hacen el mismo acto: **detectar la tendencia emergente, cerrar alianzas tempranas que aseguren suministro, y capacitar e incentivar a la fuerza de ventas** |
| `asociaciones_clave` | **9 a 12** | `gestion_beneficios_alianza_sostenible` | KPIs conjuntos, horizonte de 3 a 5 anos y **reparto de beneficios**: es literalmente el objeto del miembro |
| `co_creation_session` | **5 a 9** | `coordinacion_colaboracion_cadena_suministro` | sus pasos 4 y 5 ya son **la plataforma de colaboracion en tiempo real y la simulacion jugada entre las partes**, que es lo que el bloque monta |
| `economia_circular_como_modelo_de_negocio` | **6 a 9** | `modelo_simulacion_cadena_suministro_circular` | unico miembro cuyo objeto es la cadena circular, y el ultimo paso del bloque **es su propio entregable**: el impacto en costos de materiales y logistica |
| `empoderamiento_de_participantes` | **5 a 8** | `requisitos_sistema_retroalimentacion` | objetivos comunes, informacion en tiempo real y auto-organizacion **son sus tres requisitos**, dichos con otras palabras |
| `gestion_cuentas_por_cobrar` | **5 a 9** | `gestion_riesgo_credito` | politicas de credito, criterios de riesgo y formas de pago internacionales: **el objeto del miembro es la funcion de credito tomando riesgos inteligentes**. Y **el cableado desempata (`P.8`): el miembro ya era nodo siguiente del origen** |
| `mapa_de_canal_de_ventas` | **6 a 8** | `definicion_alineacion_cadena_suministro` | **identificar tu rol y mapear la cadena entera** son sus dos primeros pasos |
| `producto_unico_superior` | **7 a 8** | `coordinacion_colaboracion_cadena_suministro` | el mas delgado de los doce: **ecosistema que innova contigo y reputacion por encima del precio** son sus pasos 2 y 3 |
| `ratios_eficiencia_inventario` | **5 a 8** | `cuatro_categorias_desempeno_cadena_suministro` | rotacion, retorno sobre ventas y ciclo de conversion de efectivo **son las metricas de una de sus cuatro categorias**, la de eficiencia interna |

**LOS SIETE DE LA TERCERA CLASE, repartidos a `HUGOS-SISTEMAS`:**

| origen | frontera | miembro receptor | por que su objeto coincide |
|---|---|---|---|
| `bundle_ideas` | **6 a 9** | `guias_diseno_sistemas_estrategicos` | **una sola combinacion de tecnologia y proceso para varios objetivos** es su guia 4, y su objeto es comparar disenos antes de construir |
| `modelo_hibrido_agile_stage_gate` | **10 a 13** | `ejecucion_incremental_transicion_tecnologica` | hitos de 30, 60 y 90 dias con version funcional por ciclo: **pasos incrementales evaluando el aprendizaje de cada uno** |
| `principio_calidad_mvp` | **11 a 14** | `ejecucion_incremental_transicion_tecnologica` | lanzar la minima viable y ampliar con el uso real: **el mismo acto** |
| `procesamiento_paralelo_con_espirales` | **5 a 9** | `definicion_objetivos_proyecto_sistema` | partes independientes ejecutables en paralelo: **su objeto es que ningun objetivo dependa de otro**. El cableado desempata otra vez |
| `propuesta_gasto_capital` | **6 a 12** | `tecnologia_como_medio_no_fin` | los beneficios directos, incrementales, de evitacion e intangibles **son la evaluacion que ese nodo pide por entregable**, y su paso 3 la manda calcular antes de decidir |
| `reduccion_tamano_de_lote_batch_size` | **6 a 9** | `ejecucion_incremental_transicion_tecnologica` | **el calce mas literal de los siete**: reutilizar lo existente antes de reemplazarlo y evaluar despues de cada paso |
| `schedule_management_plan` | **6 a 10** | `complejidad_acorde_capacidad_organizacional` | *ambicioso pero factible*, validado con el equipo ejecutor: **su objeto exacto** |

> **TRES BLOQUES CAEN EN EL MISMO MIEMBRO, y se dice en vez de callarse.**
> `ejecucion_incremental_transicion_tecnologica` recibe los de `modelo_hibrido_agile_stage_gate`,
> `principio_calidad_mvp` y `reduccion_tamano_de_lote_batch_size`. **No es un error del
> reparto: es la medida de que los tres traian el mismo material de Hugos**, que es
> justamente lo que la tercera clase afirmaba. **La repeticion que esa reunion crea dentro
> del miembro queda declarada aqui y va a la fase 02**, que es la fase que desteje. **No la
> podo yo: el verbo de la operacion es repartir, no elegir por cual mitad se queda.**

**CORRECCION DECLARADA, y no la resuelvo copiando (`EJECUTOR.md` regla 1): LA FRONTERA DE
`bundle_ideas` ES 1 a 5 / 6 a 9, NO 1 a 4 / 5 a 9.** La tabla de los siete de la tercera clase,
mas arriba en este archivo, publica **1 a 4 / 5 a 9** con su corte de la vuelta 26 **y se queda
entera**. Medido hoy contra los pasos: **el paso 5 (*identifica los huecos logisticos que
queden y llenalos con ideas adicionales*) es del bloque de IDEO**, y lo dice el propio
`resumen_teorico` del nodo, que es de IDEO: *descartando lo que no encaje y completando con
ideas nuevas los huecos que queden en la logistica*. **El bloque de Hugos empieza en el paso
6**, y por ahi se corto.

**LOS CUATRO QUE NO SE PUDIERON EJECUTAR, y el motivo es el mismo muro de `OP-F-02`:** su
destino, leido, **es NODO PROPIO**, y crear un nodo no entra al historial mientras el guardian
de commit corra la suite del motor con el chequeo del indice semantico dentro.

| origen | frontera | destino leido | por que ningun miembro coincide |
|---|---|---|---|
| `analisis_tco_roi_b2b` | **5 a 9** | **nodo propio** `seleccion_de_proveedores_por_costo_total` | la familia tiene el consumo (`gestion_procurement_consumo`), la negociacion (`negociacion_contratos_proveedores`) y el desempeno (`gestion_contratos_desempeno`), **pero no tiene la SELECCION**: ponderar criterios y comparar proveedores por costo total |
| `criterios_seleccion_proveedores` | **7 a 10** | **el mismo nodo propio** | mismo material de Hugos que el anterior: mirar mas alla del precio y **concentrar volumen reduciendo la base de proveedores**. **Los dos bloques van a UN solo nodo, no a dos** |
| `gestion_inventario` | **6 a 9** | **nodo propio** `driver_de_inventario` | la familia tiene los drivers de **produccion, transporte, ubicacion e informacion**, y **le falta el de inventario**: ciclico, de seguridad y estacional con punto de reorden |
| `transicion_producto_a_experiencia` | **5 a 8 y 9 a 12** | **nodo propio** | ningun miembro tiene por objeto **convertir el producto en servicio de acceso**; y su paso 11 (las tres interfaces de usuario) es de la parte de SISTEMAS, como ya senalaba la prueba cruzada |

**LAS GUARDAS DE ESTE REPARTO, corridas todas:** simulacion previa sobre copia en memoria
(**verde en las dos tandas**, y **la primera version se paro en rojo** porque el segundo corte
de `asociaciones_clave` leia la fuente ya recortada por el primero: **la guarda hizo su
trabajo**); guarda de texto por paso y guarda de fuente por nodo; **caso positivo corrido
antes (33 pruebas, 33 CAEN) y despues (33 PASAN)**; **`GATE 0` ENTERO EN VERDE, sin un solo
rojo**, 71 etiquetas sin encoger y las dos copias del grafo en el mismo blob; **suites en
verde**: motor 24 de 24, web 80 ficheros con 1.030 pasadas, `tsc` limpio.

### LA RELECTURA CONJUNTA DE LAS DOS DISCREPANCIAS: LAS DOS VUELCAN (14 ago 2026, vuelta 28)

**Encargada por el acta de la vuelta 27 del auditor (seccion 2), que marco dos
discrepancias DENTRO de los discutibles y las mando a relectura conjunta.** El ejecutor
las verifico hoy contra el grafo con la vara de `P.18` (*el objeto coincide, si o no*),
salida en `docs/loop/SALIDA_V28_RELECTURA_CONJUNTA.txt`. **Las dos lecturas del ejecutor
de la vuelta 27, que estan impresas mas arriba en este archivo, SE QUEDAN ENTERAS: eran
el estado del dia en que se escribieron, y una correccion que tapa lo que corrige no se
puede auditar.**

**CORRECCION DECLARADA 1: `economia_circular_como_modelo_de_negocio` 6 a 9 NO va a
`modelo_simulacion_cadena_suministro_circular`. VA A NODO PROPIO.**

| | |
|---|---|
| **lo publicado en la vuelta 27** | *unico miembro cuyo objeto es la cadena circular, y el ultimo paso del bloque es su propio entregable: el impacto en costos de materiales y logistica* |
| **lo medido hoy** | el entregable del miembro, leido hoy, es **un modelo de simulacion con reporte de P y L y KPIs para al menos dos escenarios**, no el impacto en costos de materiales y logistica. La frase publicada nombraba una clausula del `resumen_teorico`, no el entregable |
| **la vara** | `P.18` decide por **OBJETO**, no por tema. El miembro **SIMULA y COMPARA** (definir entidades, centro de gravedad, correr simulaciones de 14 dias, reportes de P y L, comparar disenos). El bloque **ELIGE la estrategia y DISENA el mecanismo** (mapear el ciclo de vida de hoy, identificar en cual de las cinco estrategias circulares hay mas potencial, disenar el retorno o la remanufactura, calcular el impacto). **Ningun paso del miembro elige ni disena, y ningun paso del bloque simula** |
| **por que no hay otro miembro** | barrido corrido hoy sobre los **111 nodos vivos que declaran a Hugos** (`docs/loop/SALIDA_V28_FAMILIA_HUGOS.txt`): solo **uno** tiene por objeto la cadena circular, y es ese. Los otros dos aciertos del barrido son incidentales (`estrategia_captura_mercado_crecimiento` cita *productos verdes* como ejemplo de mercado emergente; `gestion_beneficios_alianza_sostenible` usa *sostenible* en el sentido de alianza duradera) |
| **el destino** | **NODO PROPIO** por `P.18` punto 3, `estrategia_circular_y_mecanismo_de_retorno`, con `economia_circular_como_modelo_de_negocio` como procedencia y previo. Plan sellado en `docs/loop/PLAN_V28_RELECTURA.json` |

> **EJECUTADA Y DESHECHA EN LA MISMA VUELTA, y se dice entero.** La mudanza corrio con
> sus guardas en verde y su caso positivo (`SALIDA_V28_RELECTURA_CASO_ANTES.txt`: 4 de 6
> pruebas CAEN; `SALIDA_V28_RELECTURA_CASO_DESPUES.txt`: 6 de 6 PASAN), y **se deshizo
> porque el nodo nuevo dejo el arbol incommitteable por una TERCERA hilada del muro**
> (ver abajo). El bloque vuelve a quedar donde la vuelta 27 lo puso, **con esta
> correccion escrita encima y el plan sellado esperando**: es el mismo remedio que el
> acta de la vuelta 27 adjudico CORRECTO en su discutible 8.

**CORRECCION DECLARADA 2, APLICADA Y EN EL ARBOL: `superioridad_producto_beneficios`
7 a 10 se MUDA de `diferencia_ventaja_beneficio` a
`framework_caracteristicas_ventajas_beneficios`.**

| | |
|---|---|
| **lo publicado en la vuelta 27** | el plan sellado de `OP-F-04-RAC` decia: *el entregable del miembro es esa misma decision: los mensajes de venta reclasificados con el momento exacto de la conversacion en que se usa cada uno* |
| **lo medido hoy** | **el bloque no decide ningun momento de conversacion**, y **no nombra la Ventaja ni una sola vez**: opone CARACTERISTICAS y BENEFICIOS y decide el estilo global del discurso segun el posicionamiento de precio |
| **la vara** | el objeto de `diferencia_ventaja_beneficio` es la distincion Ventaja contra Beneficio **y el momento** de usarlas (sus cuatro pasos propios son todos de momento: revisar si ya hay Necesidad Explicita, volver a preguntas de Implicacion, guardar el *esto le ayudara a*, no abrir con Ventajas genericas). El objeto de `framework_caracteristicas_ventajas_beneficios` es **de que clase son los mensajes de tu discurso**, y su entregable lo dice con esas palabras: *guia de clasificacion de mensajes de venta aplicada a la propuesta de valor propia*. Su paso 3 pide que el Beneficio responda a una Necesidad Explicita, que es exactamente el paso premium del bloque |
| **el resultado medido** | `diferencia_ventaja_beneficio` **8 pasos a 4**; `framework_caracteristicas_ventajas_beneficios` **4 pasos a 8**. Cero perdida: la huella *otro posicionamiento de precio* vive hoy en **exactamente un nodo vivo** |

**EL SALDO DE `OP-F-03` TRAS LA RELECTURA, contado hoy:** los quince repartidos de la
vuelta 27 pasan a **CATORCE en el arbol**, porque el de `economia_circular` se deshizo y
espera al muro junto a los cuatro que ya esperaban. **La cuenta de bloques que le faltan
a `OP-F-03` para declararse HECHA sube de cuatro a CINCO**, y los cinco tienen destino
NODO PROPIO leido: `analisis_tco_roi_b2b` y `criterios_seleccion_proveedores` (a UN solo
nodo), `gestion_inventario`, `transicion_producto_a_experiencia` y ahora
`economia_circular_como_modelo_de_negocio`.

### LAS TRES ADJUDICACIONES DEL ACTA 27 QUE ESTA PAGINA REGISTRA (14 ago 2026, vuelta 28)

**1. `OP-F-03` NO SE DECLARA HECHA: queda PARCIAL** (acta de la vuelta 27, seccion 4,
punto 1). Su verificacion escrita (*los que si: el bloque se separa*) no esta entera
mientras existan bloques con destino decidido y sin ejecutar. **El criterio de HECHO de
la fase 08 pide la verificacion entera, y se declara HECHA el dia en que los nodos
propios existan y su caso positivo pase.** Medido hoy: **catorce de diecinueve bloques
en el arbol, cinco pendientes**, los cinco bloqueados por el muro.

**2. LA REPETICION QUE UN REPARTO CREA NO SE DESTEJE EN EL ACTO: entra a la cola de
relectura post fusion de la fase 02** (acta de la vuelta 27, seccion 4, punto 2,
adjudicada POR EXTENSION CITADA de `P.3` mas la cola escrita en `08_VERIFICACION.md`).
**La costura concreta que esta fase crea y deja declarada:**
`ejecucion_incremental_transicion_tecnologica` recibio los bloques de
`modelo_hibrido_agile_stage_gate`, `principio_calidad_mvp` y
`reduccion_tamano_de_lote_batch_size`, y hoy mide **16 pasos**. **No se poda aqui: el
verbo de la operacion es repartir.** Registrada tambien en `08_VERIFICACION.md`, que es
donde vive la cola.

**3. DOS BLOQUES QUE CAEN EN EL MISMO NODO PROPIO SE FUNDEN EN UNO** (acta de la vuelta
27, seccion 4, punto 3, RATIFICADA POR EXTENSION CITADA de `P.18` y de la vara madre de
la campana: el objeto de la fase I es fundir gemelos). **Fabricar dos nodos propios con
el mismo material el dia de su creacion seria fabricar el par que la campana existe para
deshacer.** Aplica hoy a **un solo caso medido**: `analisis_tco_roi_b2b` (5 a 9) y
`criterios_seleccion_proveedores` (7 a 10) van **a UN nodo, no a dos**, con **las dos
procedencias declaradas en su fuente y en su lectura**.

---

## LO QUE ESTA FASE LE DEJA A LAS DEMAS

| a quien | que |
|---|---|
| **`02_DESTEJIDOS`** | `brainstorming_divergente` con la fuente ya fijada, o el acto 1 no puede empezar |
| **`02` entero** | el estandar de pasos contra el que se verifica cada nodo resultante |
| **`03_FUSIONES`** | la atribucion correcta de cada superviviente, que es lo unico que no se puede corregir despues |
| **el racimo de la IA** | tres bloques de material que **se reunen** con su familia, y una nomina de diez que hay que **re-medir despues** |

---

## LA TANDA DE LOS INJERTOS: leidos los 43

**Encargo del 11 ago 2026. Fuente primero manda: se resuelven ANTES que los
destejidos y las fusiones que dependen de ellos.**

### PRIMERO, EL SALDO, y una correccion de la cifra

| | |
|---|---:|
| declaraciones en segunda posicion, sin Hugos ni Mollick | **46** |
| **NODOS DISTINTOS** | **43** |
| **CONFIRMADOS como injerto** | **43** |
| **arrastre** (la fuente declara un libro cuyo material no aparece) | **0** |

> **CORRECCION DECLARADA: la tanda es de 43 NODOS, no de 46.** El 46 contaba
> **declaraciones**, y tres se solapan: `metas_vs_proposito` declara **Horowitz Y
> Coleman**, `viral_loop_marketing` declara **Coleman Y Weinberg**, y
> `decision_de_vender_startup` **declara Horowitz DOS VECES con dos grafias
> distintas**.

> **Ese ultimo caso es evidencia directa para `OP-S-11`**: un solo nodo lleva *The
> Hard Thing About Hard Thing* y *The Hard Thing About Hard Things* **en la misma
> linea**. Sin campo canonico, el recorte cuenta dos libros donde hay uno.

### EL RESULTADO: 43 DE 43 CONFIRMADOS, Y CERO ARRASTRE

> **La firma posicional acerto en todos.** En los cuarenta y tres, **el material
> del libro declarado en segunda posicion ESTA PRESENTE**, y esta siempre de la
> misma forma: **como BLOQUE APENDICE al final de los pasos.**

**LA FORMA, escrita una vez porque es la misma en los 43:**

> El nodo se extrajo del libro 1 y quedo con sus pasos. **Despues, una segunda
> extraccion del libro 2 se PEGO AL FINAL en vez de hacerse nodo propio.** La
> frontera entre los dos bloques **se ve a simple vista**: el ultimo paso del
> bloque 1 cierra un procedimiento y el primero del bloque 2 abre otro.

**LA EVIDENCIA, por grupo y con la frontera del bloque:**

| grupo | nodos | la frontera tipica |
|---|---:|---|
| **COLEMAN** | 15 | el bloque 1 mapea o mide; **el bloque 2 anade el ritual, la celebracion y el seguimiento programado** de los 100 dias |
| **HOROWITZ** | 13 | el bloque 1 es estructura o dilema del fundador; **el bloque 2 es la conversacion dificil**: como degradar, como vender, como evaluar cada trimestre |
| **WEINBERG** | 13 | el bloque 1 es metrica o proceso; **el bloque 2 es el Bullseye y los canales de traccion** |
| **RACKHAM** | 4 | el bloque 1 es metodo de producto; **el bloque 2 es la venta**: preguntas de problema, grupo de control, caracteristicas contra beneficios |

**CUATRO EJEMPLARES CON SU CORTE EXACTO, uno por libro:**

| nodo | libro 1 | corte | bloque 2 |
|---|---|---|---|
| `five_whys_inversion_proporcional` | Ries, cinco porques | **pasos 1 a 5 / 6 a 9** | Rackham: causa raiz de un problema **de ventas**, grabaciones de llamadas |
| `voz_del_cliente_voc` | Cooper, VoC | **1 a 5 / 6 a 10** | Coleman: observar una vez al mes, las pepitas de oro, revisar a los dos dias |
| `background_startup_vs_corporativo` | Wasserman | **1 a 4 / 5 a 9** | Horowitz: la iniciativa propia, el primer mes, desconfiar del equity como motivo |
| `enfoque_motor_unico_crecimiento` | Ries, motor unico | **1 a 4 / 5 a 9** | Weinberg: el anillo medio del **Bullseye**, redirigir todo al canal ganador |

### LOS TRES CASOS QUE NO SON UN SIMPLE APENDICE

**Se nombran aparte porque su arreglo es mayor:**

| nodo | que tiene |
|---|---|
| **`viral_loop_marketing`** | **30 pasos y TRES libros**. Blank, Coleman y Weinberg apilados, **y con repeticion dentro del propio apendice**: los pasos 14 a 17 y 18 a 21 dicen lo mismo con otras palabras |
| **`coeficiente_viral`** | **16 pasos**, y el bloque de Weinberg **entra DOS VECES**: los pasos 6 a 11 y los 12 a 16 son la misma cuenta de K |
| **`decision_de_vender_startup`** | **25 pasos**, Horowitz **declarado dos veces con dos grafias**, y el material repetido tres veces: los pasos 11 a 15, 16 a 20 y 21 a 25 vuelven sobre el precio minimo y la disposicion del equipo . **CORRECCION DECLARADA ADITIVA, 14 ago 2026 (vuelta 21): MANDA EL 34, y el 25 y su tramo se quedan enteros arriba.** Adjudicada por el acta de la vuelta 20 del auditor (seccion 4, punto 1), **que la midio con git**: el blob de `dataset/metadata/master_graph.json` es IDENTICO en `0e5e0c60` (9 ago, ultimo commit que toca el grafo), en `23f9ac32` (11 ago, el commit que CREA este archivo) y en HEAD, asi que **el nodo YA tenia 34 pasos el 11 ago: el 25 era PARCIAL DE NACIMIENTO, no un nodo que crecio**. Reproducido hoy con instrumento propio (`scripts/loop/vuelta21_registros.py`): **34** pasos en el grafo de hoy, **34** leidos del blob de `23f9ac32`, y los tres blobs con la misma firma `bb423c06`. **La frontera vigente (1 a 10 / 11 a 34) ya esta impresa en la tabla de la vuelta 20 de este archivo y se CITA, no se recuenta; el caracter del hallazgo (no es un simple apendice) queda.** |

> **Los tres son costura Y injerto a la vez**, y por eso van con **TOQUE UNICO**:
> se separa el apendice y se desteje la repeticion **en el mismo acto**.

### QUE DECISIONES DE FUENTE NUEVAS SALEN

**CUATRO, una por libro, y son del mismo tipo que las tres que ya existian:**

| decision | nodos | que se decide |
|---|---:|---|
| **`OP-F-04-COL`** | 15 | el bloque de Coleman **se reune** con la serie de los 100 dias, o se poda |
| **`OP-F-04-HOR`** | 13 | el bloque de Horowitz **va a familia propia** o se poda |
| **`OP-F-04-WEI`** | 13 | el bloque de Weinberg **se reune con el Bullseye** de traccion, o se poda |
| **`OP-F-04-RAC`** | 4 | el bloque de Rackham **se reune con SPIN**, o se poda |

> **La aritmetica de las decisiones de fuente pasa de TRES a SIETE, y su alcance
> de 31 nodos a 74.** No es que hayan aparecido injertos nuevos: **es que la firma
> posicional los hizo contables.**

### `OP-F-04-RAC` EJECUTADA ENTERA (14 ago 2026, vuelta 27)

**Es la primera de las cuatro tandas que se ejecuta completa**, y por eso vale como patron de
las otras tres. `P.3` manda **reparto obligatorio** (el tema coincide) hacia la familia de
SPIN; el miembro receptor lo elige `P.18` sobre la nomina **medida hoy: 51 nodos vivos
declaran a Rackham y 47 lo declaran como fuente UNICA**.

| # | origen | frontera leida hoy | miembro receptor | por que su objeto coincide |
|---:|---|---|---|---|
| 1 | `five_whys_inversion_proporcional` | **1 a 5 / 6 a 9** | `diagnostico_sintoma_vs_causa_ventas` | el bloque busca la causa raiz de un problema de ventas mirando grabaciones de llamadas antes de rediseñar el entrenamiento; **el objeto del miembro es ese diagnostico**, distinguir el sintoma de la causa con datos reales de conversaciones |
| 2 | `preguntas_ipo_dolor_cliente` | **1 a 4 / 5 a 7** | `preparacion_preguntas_problema_precall` | identificar **DE ANTEMANO** los problemas tipicos y formular las preguntas: **es literalmente el objeto del miembro**, anticipar tres problemas y redactar sus Preguntas de Problema |
| 3 | `split_testing_experimentos_ab` | **1 a 5 / 6 a 9** | `metodologia_evaluacion_entrenamiento_ventas` | grupo de control de desempeno inicial similar y diferencia neta como evidencia: **es su tercera prueba**, ganancia medible frente a un grupo que no fue entrenado |
| 4 | `superioridad_producto_beneficios` | **1 a 6 / 7 a 10** | `diferencia_ventaja_beneficio` | cuando se enumeran caracteristicas y cuando se habla de beneficios: **es su entregable**, los mensajes reclasificados con el momento exacto de usar cada uno |

**LAS CUATRO FRONTERAS SE LEYERON HOY CONTRA LOS PASOS** y **las cuatro calzan con la
frontera tipica publicada para el grupo** (*el bloque 1 es metodo de producto; el bloque 2 es
la venta*). **Cero destinos a nodo propio en esta tanda**, asi que el muro del indice no la
toca.

**GUARDAS:** simulacion previa verde, guarda de texto y de fuente por nodo, **caso positivo
antes (8 pruebas, 8 CAEN) y despues (8 PASAN)**, **`GATE 0` entero en verde**, 71 etiquetas
sin encoger, las dos copias en el mismo blob, y **suites verdes** (motor 24 de 24, web 80
ficheros con 1.030 pasadas, `tsc` limpio).

> **`OP-F-04-COL`, `OP-F-04-HOR` y `OP-F-04-WEI` NO SE EJECUTARON EN ESTA VUELTA**, y el
> motivo se dice sin adornos: **son 39 bloques mas**, y cada uno pide leer su nomina de
> familia entera y decidir su destino por `P.18`, que es lectura y no mecanica. **La vuelta
> gasto su alcance en medir el muro y en cerrar `OP-F-02`, `OP-F-03` y `RAC`.** Las tres
> quedan **sin tocar un paso**, con su nomina viva medida hoy en el reporte.

> **CORRECCION DECLARADA, 14 ago 2026 (vuelta 26), y la frase de arriba se queda entera:
> EL ALCANCE MEDIDO HOY ES DE 30 A 73, no de 31 a 74.** La unica pieza que se movio es la
> misma de siempre: `background_startup_vs_corporativo` salio de `OP-F-01` por `P.17`, y
> como ese nodo YA estaba dentro de `OP-F-04-HOR`, **la cuenta de las siete baja en uno,
> no en dos**. Contado hoy sobre el campo `nodos` de las siete operaciones de fuente con
> `scripts/loop/vuelta26_medir.py`: **73 ids distintos**, de los cuales **30** en las tres
> primeras y **43** en las cuatro de la tanda, **cero solape entre los dos grupos**.
> **Los 43 de la tanda salen de 15 mas 13 mas 13 mas 4 igual a 45 declaraciones menos los
> dos nodos que estan en dos grupos** (`metas_vs_proposito` en COL y HOR,
> `viral_loop_marketing` en COL y WEI). **La leccion no se toca: la firma posicional es lo
> que los hizo contables.**

> **Y hay una asimetria util con Hugos: alli el material pegado era de OTRO TEMA
> (cadena de suministro dentro de nodos de producto y de finanzas). Aqui, en los
> cuatro libros, EL TEMA COINCIDE**: el bloque de Coleman habla del cliente y el
> nodo tambien; el de Weinberg habla de canal y el nodo tambien. **Eso hace la
> poda mas peligrosa y el reparto mas obligatorio.**

### LA CONSECUENCIA DE ORDEN, y toca a la fase 02

**SEIS de los 43 ya tienen operacion en otra fase**, y por *fuente primero* esta
va antes:

| nodo | donde mas aparece |
|---|---|
| `voz_del_cliente_voc`, `blueprint_de_experiencia`, `customer_journey_mapping` | **`OP-D-02`**, el destejido de la voz del cliente |
| `metricas_de_adquisicion_activacion`, `key_partners_hypothesis`, `retention_metrics` | **`OP-D-06`**, los nueve actos de dos |

> **`voz_del_cliente_voc` es el caso que lo prueba entero**: su destejido ya estaba
> escrito separando **Cooper de Coleman**, y esta tanda **acaba de confirmar por
> el campo `fuente` la misma frontera que la lectura de pasos habia encontrado
> sola.** Dos instrumentos independientes, el mismo corte.

---

### CORRECCION DECLARADA, 14 ago 2026 (vuelta 20): LA TANDA SON **44 NODOS**, Y NADA DE LO DE ARRIBA SE BORRA

**Adjudicada por el acta de la vuelta 19, seccion 4, pregunta 3: *manda el grafo*.**
**Toda cifra de esta subseccion sale de `scripts/loop/vuelta20_horowitz.py` corrido HOY sobre
`dataset/metadata/master_graph.json`, no de una nota ni de un reporte anterior.**

| | lo que publica el saldo de arriba (11 ago 2026) | **medido hoy, 14 ago 2026** |
|---|---:|---:|
| declaraciones en segunda o posterior posicion | **46** | **46** |
| **NODOS DISTINTOS** | **43** | **44** |
| grupo COLEMAN | **15** | **15** |
| **grupo HOROWITZ** | **13** | **14** |
| grupo WEINBERG | **13** | **13** |
| grupo RACKHAM | **4** | **4** |

**LA DIFERENCIA ENTERA ES HOROWITZ, y el 43 sale de una aritmetica que no se sostiene.** El saldo
de arriba explica el paso de 46 declaraciones a 43 nodos con **tres** solapes. Medidos hoy, los
nodos que declaran **dos de los cuatro libros** son **DOS**, no tres: `metas_vs_proposito`
(Horowitz y Coleman) y `viral_loop_marketing` (Coleman y Weinberg). **El tercero,
`decision_de_vender_startup`, no es un solape de nodos: declara a Horowitz DOS VECES con dos
grafias, y un nodo que declara el mismo libro dos veces sigue siendo UN nodo y UN libro.** Con dos
solapes, 46 menos 2 son **44**. **La cifra vieja 43 y sus grupos 15/13/13/4 quedan enteros arriba,
con esta correccion al lado; `docs/plan/10_INVENTARIO.md` no se toca porque su 14 es el correcto.**

> **Y HAY UNA TERCERA SEDE, buscada porque una busqueda negativa no se puede citar:**
> [`RECORTE_POSICIONAL.md`](RECORTE_POSICIONAL.md), **del mismo 11 ago 2026 que el saldo de
> arriba**, ya publica en su seccion *LOS TRES QUE MAS APORTAN* el grupo de Horowitz con **14
> candidatos Y SU NOMINA ESCRITA**. Cotejada hoy nodo por nodo contra el grafo, **la nomina de ese
> doc y la medida hoy son IDENTICAS**, y lo mismo pasa con las otras dos que ese doc nombra
> (Coleman 15 y Hugos 21, identicas las dos). Sus agregados tambien reproducen exactos: **3.521
> nodos vivos, 67 con mas de un libro y 70 declaraciones en segunda o posterior posicion.**
> **O sea que el 13 de arriba ya estaba contradicho EL MISMO DIA por otro documento del plan, y hoy
> el 14 tiene TRES sedes contra UNA.**

### LA NOMINA DE LOS 14 DE HOROWITZ, impresa desde el grafo, y su forma verificada UNO POR UNO

**Por que hacia falta imprimirla, dicho con precision:** lo que **no** esta escrito en ninguna
parte es la nomina de los **13**, asi que sigue sin poderse decir *cual sobra*; la de los **14** si
lo estaba, en `RECORTE_POSICIONAL.md`, y esta subseccion la reproduce desde el grafo **con la forma
verificada**, que es lo que aquel doc no hacia (*"NO ADJUDICA. La lista es de candidatos a injerto,
y su verificacion es por lectura"*, dice el suyo). Los pasos enteros de los catorce estan en la
salida de `scripts/loop/vuelta20_horowitz.py`; aqui va el saldo de la lectura.

> **CORRECCION DECLARADA ADITIVA, 14 ago 2026 (vuelta 21), y las dos frases de arriba se quedan
> ENTERAS: LA NOMINA DE LOS 13 SI ESTA ESCRITA, y SI se puede decir cual sobra.** Vive en
> [`OPERACIONES.jsonl`](OPERACIONES.jsonl), **campo `nodos` de `OP-F-04-HOR`** (fecha_corte
> 2026-08-11, adjudicacion *LEIDOS LOS 13*). **El que sobra es `principio_calidad_mvp`**: medido
> hoy con `scripts/loop/vuelta21_registros.py`, los **14** del grafo menos los **13** de la
> operacion dan exactamente ese nodo, y **ninguno de los 13 falta en el grafo**. No queda
> descubierto: barridas hoy las **71** operaciones, `principio_calidad_mvp` esta en el campo
> `nodos` de **TRES** (`OP-F-03`, el bloque de Hugos; `OP-D-01`, su destejido entero; y tambien
> `OP-D-06`, que el acta no nombra). **Lo de arriba fue una BUSQUEDA NEGATIVA CITADA**, la especie
> que la doctrina prohibe, **y se declara aqui sin borrar la frase que la contiene**. Adjudicado en
> el acta de la vuelta 20 del auditor, secciones 1 y 5.

| # | nodo | libros declarados | frontera leida | **el bloque de Horowitz** |
|---:|---|---|---|---|
| 1 | `actualizacion_posiciones_existentes` | Wasserman \| **Horowitz** | pasos **1 a 4 / 5 a 19** | **apendice AL FINAL** |
| 2 | `background_startup_vs_corporativo` | Wasserman \| **Horowitz** | **1 a 4 / 5 a 9** | **apendice AL FINAL** (ya publicado arriba) |
| 3 | `contratacion_experiencia_vs_potencial` | Wasserman \| **Horowitz** | **1 a 4 / 5 a 10** | **apendice AL FINAL** |
| 4 | `decision_de_salir_a_bolsa` | Wasserman \| **Horowitz** | **1 a 5 / 6 a 10** | **apendice AL FINAL** |
| 5 | `decision_de_vender_startup` | Wasserman \| **Horowitz** \| **Horowitz** | **1 a 10 / 11 a 34** | **apendice AL FINAL**, y es uno de los tres apartados de arriba |
| 6 | `estrategia_de_innovacion_producto` | Cooper \| **Horowitz** | **1 a 3 / 4 a 7** | **apendice AL FINAL** |
| 7 | `manejo_empleados_en_adquisicion` | Feld \| **Horowitz** | **1 a 4 / 5 a 9** | **apendice AL FINAL** |
| 8 | **`metas_vs_proposito`** | Assembling \| **Horowitz** \| Coleman | **1 a 4 / 5 a 9 / 10 a 14** | **presente y con frontera visible, pero NO AL FINAL**: el ultimo bloque es de Coleman |
| 9 | `organizacion_adaptativa` | Ries \| **Horowitz** | **1 a 4 / 5 a 8** | **apendice AL FINAL** |
| 10 | `plan_mejora_procesos` | Book of Forms \| **Horowitz** \| **Horowitz** | **1 a 5 / 6 a 10 / 11 a 15** | **apendice AL FINAL**, con el material repetido dos veces |
| 11 | `posicionamiento_de_empresa` | Blank \| **Horowitz** | **1 a 5 / 6 a 9** | **apendice AL FINAL** |
| 12 | **`principio_calidad_mvp`** | Ries \| **Horowitz** \| Hugos | **1 a 5 / 6 a 10 / 11 a 14** | **presente y con frontera visible, pero NO AL FINAL**: el ultimo bloque es de Hugos |
| 13 | `revisiones_regulares_desempeno_ceo` | Wasserman \| **Horowitz** | **1 a 4 / 5 a 10** | **apendice AL FINAL** |
| 14 | `seleccion_ceo_fundador` | Wasserman \| **Horowitz** | **1 a 4 / 5 a 12** | **apendice AL FINAL** |

**EL CABO QUEDA SALDADO, y en dos mitades que no dicen lo mismo:**

> **POR PRESENCIA DEL MATERIAL: 44 DE 44 CONFIRMADOS.** En los catorce de Horowitz el material del
> libro declarado en segunda posicion **ESTA PRESENTE y con la frontera visible**. Como los 43 ya
> estaban confirmados y el catorceavo de Horowitz es el unico que podia faltar, **sea cual sea el
> que la nomina de 13 dejaba fuera, esta verificado**. Cero arrastre, igual que antes.

> **POR LA FORMA ESTRICTA: 12 DE 14, y los dos que no la tienen se nombran.** El saldo de arriba
> dice que el bloque esta **siempre** *como BLOQUE APENDICE al final de los pasos*. En
> **`metas_vs_proposito`** y **`principio_calidad_mvp`** el bloque de Horowitz **esta pegado y se
> ve, pero queda EN MEDIO**, porque cada uno declara un TERCER libro despues (Coleman y Hugos) y es
> ese tercer bloque el que cierra los pasos. **No es una forma distinta: es la misma forma aplicada
> dos veces sobre el mismo nodo.**

> **Y LOS DOS INSTRUMENTOS VUELVEN A DAR EL MISMO CORTE, como en `voz_del_cliente_voc`.** Sin leer
> un solo paso, la **posicion del libro en el campo `fuente`** ya separa a los mismos dos: un libro
> que no ocupa la ultima posicion declarada **no puede** tener el bloque final. Medido sobre los
> **44**, las declaraciones fuera de la ultima posicion son **TRES**: esas dos, mas
> `viral_loop_marketing` con Coleman, que ya estaba apartado arriba. **La lectura de pasos y la
> medida posicional coinciden nodo por nodo.**

### DOS COSAS MAS QUE LA MEDICION LEVANTO, DECLARADAS Y **NO** ARREGLADAS

> **PRIMERA, y ensancha la evidencia de `OP-S-11` sin tocarlo:** el saldo de arriba nombra a
> `decision_de_vender_startup` como **el** caso de un nodo que declara el mismo libro dos veces con
> dos grafias. Medido hoy sobre los 44 **son DOS**: ese y **`plan_mejora_procesos`**, que trae *The
> Hard Thing About Hard Things* y *The Hard Thing About Hard Thing* en la misma linea. **El texto de
> arriba no se corrige: no afirmaba ser exhaustivo, y esta linea le anade el segundo ejemplar.**

> **SEGUNDA, y es una cifra publicada con dos lecturas que esta vuelta NO adjudica:** la tabla de
> **LOS TRES CASOS QUE NO SON UN SIMPLE APENDICE** publica `decision_de_vender_startup` con **25
> pasos**, y **medido hoy en el grafo tiene 34**. Los otros dos apartados de esa misma tabla calzan
> exactos (`viral_loop_marketing` 30 y `coeficiente_viral` 16), asi que **el que diverge es uno
> solo**. **Censadas TODAS las sedes de `docs/` con instrumento** (`scripts/loop/vuelta20_medir.py`),
> el reparto es **TRES a UNA mas el grafo**: dicen **34** [`FICHA_SUBFUSION_GRADIENTE.md`](../FICHA_SUBFUSION_GRADIENTE.md)
> (*"el peor nodo medido del catalogo"*), [`COSTURAS_INTERNAS_RESUMEN.md`](../COSTURAS_INTERNAS_RESUMEN.md)
> (fila 9 de sus veinte primeros) y la nota de `LA FIRMA POSICIONAL DEL INJERTO (P.2)` en
> `INVENTARIO.jsonl`; dice **25** solo esta tabla. **Aun asi el 25 se queda entero donde esta**, y no
> por duda sobre cual pesa mas: el 25 **no es una cifra suelta**, va cosido a un tramo escrito (*los
> pasos 11 a 15, 16 a 20 y 21 a 25*) que habria que rehacer, y eso es reescribir un hallazgo, no
> anotar una correccion aditiva. **El encargo de esta vuelta no lo scopeaba. Va a la lista de cifras
> con dos lecturas sin adjudicar de `RECOMPUTO_3388.md` (vuelta 20) y al reporte, para que lo
> adjudique el auditor.**
