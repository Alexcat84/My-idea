# FASE 01: LAS DECISIONES DE FUENTE

**Van primero, y el motivo no es de eficiencia: es que cambian lo que los nodos
dicen.** Una decision de fuente decide **de que libro es un nodo**, y de eso
depende que atribucion carga el superviviente de cualquier fusion posterior.

> **Tres decisiones en vez de dieciocho arreglos de nodo.** Es la misma economia
> de la mesa de racimos: **no se decide nodo por nodo si el checklist se parte; se
> decide una vez por libro y se aplica a todos sus nodos.**

**Operaciones: `OP-F-01`, `OP-F-02`, `OP-F-03`. Las tres DECISION PENDIENTE.**

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

| decision de fuente | nodos | operacion |
|---|---:|---|
| los **formatos lista** del *Basic Guide* | **4** | `OP-F-01` |
| la **tanda de Mollick** | **3** | `OP-F-02` |
| el **pegado de Hugos** | **11** | `OP-F-03` |
| **total** | **18** | |

> **DISCREPANCIA DECLARADA, no resuelta.** La clase LARGO LEGITIMO tiene **SIETE**
> miembros, y la cifra de 18 solo cuenta **CUATRO** de ellos, los del *Basic
> Guide*. **Los otros tres estan en la clase y fuera de la cuenta**: dos de
> *Juran's Quality Handbook* y uno de `core`. Se anota como pregunta de `OP-F-01`
> en vez de sumarse por cuenta propia.

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

**LA PREGUNTA**: el estandar de 3 a 6 pasos, admite una **excepcion nombrada**
para los formatos lista? Y si la admite, **alcanza a los siete o solo a los cuatro
del *Basic Guide***?

**VERIFICACION**: si la decision es admitir, ningun nodo de la lista queda con
pasos alterados. Si es partir, **cada nodo resultante pasa el estandar**.

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

**LA PREGUNTA**: se **retira** la atribucion a Mollick de los tres, se **desteje**
el bloque de IA hacia la familia de 48 que ya existe, o se **conserva** como
segunda fuente legitima?

**LO QUE BLOQUEA**: `brainstorming_divergente` es uno de los tres, y es el ancla
del acto mayor del cierre transitivo. **`OP-F-02` bloquea a `OP-D-04`.**

---

## `OP-F-03`: EL PEGADO DE HUGOS

**Material de cadena de suministro adosado a nodos de otro tema. Confirmado.**
**Once de las cuarenta y seis costuras confirmadas**, y es **la mayor de las tres
decisiones de fuente por numero de nodos**.

> **Y es la unica sin nomina escrita.** La cifra esta publicada en
> `COSTURAS_INTERNAS_RESUMEN.md` seccion 6 y en la ficha de sub-fusion; **la lista
> de los once ids no aparece enumerada en ninguna de las fuentes leidas.**

**LA PREGUNTA, y es de dos partes:**

1. **Cuales son los once ids?** Sin la lista, la operacion no se puede escribir ni
   ejecutar.
2. Una vez haya lista: el apendice de cadena de suministro **se poda** o **se
   reparte** a la subfamilia Hugos del nucleo?

> **La segunda parte no es retorica y ya tiene precedente medido**: en al menos un
> caso verificado contra el grafo, *la mitad de Hugos tiene parientes en el bloque
> Hugos del nucleo*, o sea que **hay adonde repartir**. Podar seria tirar material
> que tiene casa.

---

## LO QUE ESTA FASE LE DEJA A LAS DEMAS

| a quien | que |
|---|---|
| **`02_DESTEJIDOS`** | `brainstorming_divergente` con la fuente ya fijada, o el acto 1 no puede empezar |
| **`02` entero** | el estandar de pasos contra el que se verifica cada nodo resultante |
| **`03_FUSIONES`** | la atribucion correcta de cada superviviente, que es lo unico que no se puede corregir despues |
