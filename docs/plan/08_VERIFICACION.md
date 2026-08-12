# FASE 08: LA VERIFICACION

**Operacion: `OP-V-01`. LISTA.**

---

## EL CRITERIO DE HECHO, y es uno solo

> **UNA FASE ESTA HECHA CUANDO SU VERIFICACION SE CAERIA SI EL FALLO VOLVIERA.**
>
> **No cuando pasa verde: cuando se CAERIA.**

**Es el criterio del CASO POSITIVO de la FASE 0, aplicado a todo el plan.** Y tiene
una comprobacion barata: **correr la prueba ANTES del arreglo. Si pasa, no prueba
nada.**

---

## POR FASE

| fase | que tiene que dar verde |
|---|---|
| **0 CODIGO** | cada caso positivo **se cae antes** del arreglo y pasa despues |
| **01 FUENTES** | ningun nodo de la clase con pasos alterados; **el material del segundo libro reubicado, no borrado** |
| **02 DESTEJIDOS** | los **quince congelados** releidos; **cada perdida en el bloque del que proviene** |
| **03 FUSIONES** | un superviviente por acto, el resto **DEPRECADO CON ALIAS**; `resolverId` devuelve el superviviente |
| **04 ENLACES** | cada arista nueva **confirmada por lectura**, no por el instrumento; ninguna crea auto-arista tras resolver |
| **05 SANEO** | ningun id vivo con tratado extinto; los tres de Incoterms con su version; ningun nodo cablea `export.gov`; ninguna de las seis herramientas muertas; ningun nodo con dos claves de fase; **ningun nodo se cita a si mismo tras resolver** |
| **06 MESAS** | cada decision escrita **con su motivo y su cobertura al lado** (banco 9.26) |
| **07 ADUANA** | los cuatro controles mecanicos **corriendo en Gate 0** |

---

## LA VERIFICACION TRANSVERSAL, y su orden importa

1. **Gate 0 verde**
2. **suite verde**
3. **vuelo completo**
4. **prueba de rumbos** (ya comprueba que ningun ancla este deprecada)
5. **reindexado semantico**

> **EL REINDEXADO VA AL FINAL, DESPUES DE MOVER IDS.** El indice **guarda ids** y
> es **una de las fuentes externas que `OP-S-08` identifico**. Reindexar antes deja
> el indice apuntando a la era anterior, **y el sintoma no aparece en el
> reindexado: aparece semanas despues en el recorrido de una persona.**

---

## LA COMPROBACION QUE SOLO SE PUEDE HACER AL FINAL

**Recomputar el cierre transitivo** y comprobar dos cosas:

- **los actos ejecutados desaparecieron**
- **ninguno nuevo aparecio por sorpresa**

> **Y por la regla P.1 del banco del plan: ese recomputo, como cualquier conteo que
> toque ids, PASA POR EL RESOLUTOR ANTES DE CONTAR.** Un recomputo literal sobre un
> grafo recien fusionado **contaria los absorbidos como nodos vivos.**

---

## EL DISPARADOR DEL RECOMPUTO

**Se dispara EL DIA QUE EL CRIBADO LLEGUE AL PUESTO 3.388**, y no antes. Es la
**unica** recomputacion general del plan (banco 9.21).

> **Por que una sola vez y no en cada checkpoint: un barrido de cruce cuesta lo
> mismo con 2.117 pares que con 3.388, y solo el ultimo es el bueno.** Los de en
> medio producen cifras que hay que volver a escribir.

### QUE SE RECOMPUTA, Y EN ESTE ORDEN

**El orden no es de comodidad: cada paso usa la salida del anterior.**

| # | que | por que va aqui |
|---:|---|---|
| **1** | **EL RETRATO DE LAS A** | es el insumo de todo lo demas: la lista de A vigentes al cierre |
| **2** | **EL BARRIDO DE CONFIRMADAS contra las A** | cruza las costuras confirmadas contra el retrato del paso 1. **Da las curas acopladas** |
| **3** | **EL CIERRE TRANSITIVO** | las componentes se calculan **sobre el retrato del paso 1**, no sobre el archivo crudo |
| **4** | **LAS NOMINAS Y LOS ACTOS** | cada racimo y cada acto se re-mide **con su cobertura al lado** (banco 9.26), usando las componentes del paso 3 |

> **Y por la regla P.1 del banco del plan, LOS CUATRO RESUELVEN ANTES DE CONTAR.**
> Un recomputo literal sobre un grafo ya fusionado **contaria los absorbidos como
> nodos vivos**, y sobre uno sin fusionar **no veria las auto-aristas via alias**.

### QUE OPERACIONES CAMBIAN DE ESTADO CON EL RESULTADO

| operacion | hoy | despues del recomputo |
|---|---|---|
| **`OP-U-02`** | DECISION PENDIENTE | **pasa a LISTA** con la lista definitiva de actos cerrados. Es la unica que el recomputo desbloquea por si solo |
| **`OP-U-01`** | LISTA con **173 actos** | **la cifra se reescribe**: algunos de los 48 abiertos habran cerrado, y **puede que alguno de los 173 haya crecido y se abra** |
| **`OP-L-02`** | DECISION PENDIENTE | **el universo de 205 se remide**: cada A nueva puede crear pares internos nuevos fuera de cola |
| **`OP-M-01` a `OP-M-05`** | DECISION PENDIENTE | **sus nominas se re-miden con cobertura**. Una mesa puede **crecer**, y la mesa unida es la candidata |
| **`OP-D-01` a `OP-D-06`** | LISTA | **los trece actos del cierre transitivo se recomputan.** Los repartos de perdidas **no cambian**; los tamanos si pueden |

> **LO QUE EL RECOMPUTO NO PUEDE CAMBIAR, y conviene decirlo para que nadie lo
> espere:** el **ORDEN** de la fase 02. Se decide por **congelados liberados**, y
> **una A nueva no mueve un congelado.**

### EL LOTE DE LECTURA QUE VIAJA CON EL RECOMPUTO

**ADJUDICADO el 11 ago 2026: el inventario final NO lleva ninguna nomina con
cobertura incompleta pudiendo cerrarla con cinco lecturas.**

| nomina | cobertura hoy | lecturas que faltan |
|---|---|---:|
| **el sales roadmap** | **10 de 15**, MEZCLADO desde el puesto 872 | **5** |

**LOS CINCO PARES**, nombrados para que el lote no haya que reconstruirlo:

- `customer_validation_sales_roadmap` contra `estrategia_de_ventas`
- `customer_validation_sales_roadmap` contra `sales_roadmap`
- `estrategia_de_ventas` contra `hoja_de_ruta_de_ventas`
- `estrategia_de_ventas` contra `refinar_sales_roadmap`
- `estrategia_de_ventas` contra `sales_roadmap_vs_sales_force`

> **Se leen CON el recomputo y no antes**, por dos razones que se suman: su clase
> ya esta decidida, asi que no urgen; y **el recomputo puede meter miembros nuevos
> en la nomina**, con lo que leer antes obligaria a volver.

> **Y la regla que esto deja escrita, que es mas grande que estos cinco: TODA
> NOMINA QUE SE PUEDA CERRAR CON UNA TANDA CORTA SE CIERRA ANTES DEL INVENTARIO
> FINAL.** Una nomina con cobertura incompleta en el inventario **no dice lo que
> hay: dice hasta donde se miro.**

---

### LA COMPROBACION DE QUE EL RECOMPUTO CORRIO BIEN

**Tres cifras que tienen que cuadrar entre si**, y si no cuadran el recomputo esta
mal hecho:

1. **nodos en actos** igual a la suma de los tamanos de las componentes
2. **A vigentes** igual a la suma de aristas internas de todas las componentes
3. **todo acto marcado CERRADO** tiene sus pares internos leidos **y** ningun
   miembro con par pendiente

> **Y una cuarta, que es la que caza el error de P.1**: **ningun nodo deprecado
> aparece dentro de una componente.** Si aparece, el instrumento no resolvio.
