### TAREA 2. EL PLAN SE MUEVE: EL PAR 2.464 Y EL TRAMO 1 DE LA COLA POST FUSION. **CERRADA.**

> **EL PLAN SE MOVIO.** El `sha256` por la convencion de LF de
> `docs/INTRA_DOMINIO_VEREDICTOS.jsonl` abre en `ea6e850d331d14f0` y cierra en
> `0a77b5a35a962621`. **Son distintos**, y la diferencia se explica par por par
> mas abajo: **una fila tocada de 3388**.

**1. EL DISPARADOR, LEIDO ANTES DE TOCAR NADA Y CITADO CON SU LINEA.** No se cita
de memoria: `scripts/loop/vuelta187_tarea2_cola_post_fusion.py` lo localiza en el
fichero vivo y lo pega. **Si la seccion no estuviera, el instrumento cae en ROJO
y no relee nada.**

| pieza del criterio | donde vive, leido hoy | que dice |
|---|---|---|
| la sede | `docs/plan/08_VERIFICACION.md`, seccion `## LA COLA DE RELECTURA POST FUSION`, lineas **485 a 848** (364 lineas) | |
| **el disparador** | linea **491** | *"UN PAR VUELVE A LA COLA CUANDO UNO DE SUS DOS NODOS MUERE EN UNA FUSION O CAMBIA DE TEXTO"* |
| **la declaracion del tramo** | linea **585** | *"TRAMO 1 y unico con lo medido hoy: el unico par de arriba"*, y *"se relee entero o no cuenta"* |
| **la tabla de destinos** | linea **616** | si sale `A` entra en la fusion; **si sale `D` se queda**; si sale `B` otra vez va al inventario final |
| la tabla del tramo | linea **583** | el puesto **2464** |

**LA DISCREPANCIA CON EL ENCARGO, DECLARADA Y NO RESUELTA COPIANDO**
(`EJECUTOR.md` 2). El encargo dice que el criterio esta escrito *"en
`docs/plan/08_VERIFICACION.md` y en el `BANCO_DEL_PLAN`"*. **Medido hoy sobre
`docs/plan/BANCO_DEL_PLAN.md`: `post fusion` 0, `POST FUSION` 0, `cola post
fusion` 0, `2464` 0, `2.464` 0.** El criterio vive **entero y solo** en
`08_VERIFICACION.md`. **NO ES PARADA**, y se dice por que: el texto de
`08_VERIFICACION.md` **alcanza para ejecutar el tramo sin decidir nada**, que es
la condicion exacta que el encargo pone.

**Y UNA PRECISION SOBRE "CITALO POR NUMERO":** `08_VERIFICACION.md` **no numera
sus clausulas** como el `BANCO_DEL_PLAN` numera sus `P.n`. Se cita **por seccion
y por linea del fichero vivo**, que es la unica numeracion que ese fichero tiene.

**2. EL TAMANO DEL TRAMO, COMPUTADO DEL CRITERIO Y NO INVENTADO.** La criba
escrita en la propia seccion es **2760 `D` -> 99 que declaran diferenciador -> 6
que hoy lo tienen en el otro nodo -> 1 cuyo paso entro DESPUES del veredicto**, y
el parrafo del tramo dice *"el unico par de arriba"*. **ASI QUE EL TRAMO 1 SON 1
PAR: el 2464.** La lista no se tecleo: se leyo de la tabla de la linea 583.

**LA CRIBA, RE CORRIDA HOY SOBRE EL ARCHIVO ENTERO**, con la maquina IMPORTADA de
`scripts/loop/vuelta182_tarea3_diferenciador_movido.py` (varas `VARA_ABSOLUTA 3`
y `VARA_COBERTURA 0.45`, tambien importadas) **y sin correr su `main()`**, que
reescribiria evidencia sellada de la vuelta 182:

| que se conto | cifra |
|---|---:|
| `D` en el archivo | **2760** |
| `D` que declaran diferenciador | **99** |
| `D` con lesion exacta hoy, condiciones 1 y 2 | **6** |
| las que la criba nombra | **1778, 2464, 2530, 2540, 3141, 3232** |
| de ellas, fuera del tramo 1 | **1778, 2530, 2540, 3141, 3232** |

**Y ESAS CINCO DE MAS NO SON UN TRAMO NUEVO: SON LA `PD.1`, Y SE COTEJARON.** Esta
criba corre solo las condiciones 1 y 2; la tercera, que el paso entrara DESPUES
del veredicto, la fecho en git la vuelta 182. Los cinco que no la pasan son
**exactamente** los cinco que el registro `R.49` leyo del acta 187 (`6.1`):
**`SON LOS MISMOS CINCO: SI`**. **No pasan el disparador escrito y no se
encolan**: darles cola seria doctrina nueva, que es del fundador.

**3. LA RELECTURA DEL 2464, CON LOS PASOS DE HOY DE LOS DOS NODOS.**

| | `cero_defectos` | `zero_defects_concepto` |
|---|---:|---:|
| pasos hoy | **7** | **4** |

**LO QUE LA VARA MIDE:** *"hoy el paso 7 de `cero_defectos` cubre 3 palabras del
diferenciador declarado (cobertura 0.50)"*. El item declarado que se movio es
*"ELIMINAR EXPLICITAMENTE EL USO DE NIVELES DE CALIDAD ACEPTABLES como estandar"*
y el paso de hoy que lo cubre es *"Eliminar el lenguaje que normaliza niveles
aceptables de error (AQL)"*.

**LO QUE LA RELECTURA SOSTIENE, Y ES CLASE `D`:**

- la razon declaraba **DOS** cosas que `zero_defects_concepto` traia y el otro
  no. **De las dos, UNA ya no es diferenciador**: el AQL esta hoy en el paso 7 de
  `cero_defectos`, que una fusion nuestra le metio despues del veredicto.
- **LA OTRA SOBREVIVE ENTERA:** el arranque a escala minima. El paso 3 de
  `cero_defectos` habla de *"una fecha de lanzamiento (Dia de Cero Defectos) tras
  un periodo breve de preparacion para darle visibilidad"*, y **no** de *"aunque
  sea contigo mismo"* ni de *"poner por escrito un compromiso entre tu y la
  persona que te ayuda"*, que son los pasos 3 y 4 del otro nodo.
- **los diferenciadores del otro lado siguen intactos:** el despliegue caso por
  caso (paso 2), el reconocimiento genuino evitando el efectivo (paso 4) y la
  extension del estandar a todas las areas (paso 5) **no estan** en los cuatro
  pasos de `zero_defects_concepto`.

> **LOS DOS NODOS SIGUEN SANOS, ASI QUE LA CLASE NO SE MUEVE, QUE ES LO QUE LA
> TABLA DE DESTINOS MANDA PARA UNA `D`.** Lo que SI se movio es **la evidencia**:
> la razon vieja sostenia la `D` en dos diferenciadores y hoy **solo uno de los
> dos es cierto**.

**4. LA CORRECCION DECLARADA, SIN BORRAR EL TEXTO VIEJO.** La razon pasa de
**944 a 3106 caracteres**; **el texto viejo sigue entero dentro del nuevo: `SI`**;
la marca de correccion esta: `SI`; **0 guiones largos o medios**. **Ningun
veredicto se movio en silencio.**

**PENDIENTE DE DOCTRINA (`EJECUTOR.md` 5), Y SE DECLARA EN VEZ DE RESOLVERSE
SOLO.** `docs/INTRA_DOMINIO_VEREDICTOS.jsonl` tiene **ocho campos** y **ninguno es
de correccion**: contadas hoy sus 3388 filas, las claves son `puesto_intra`,
`dominio`, `nodo_a`, `nodo_b`, `clave`, `banda_078_080`, `clase` y `razon`, y
**ninguna fila ha llevado nunca un campo de correccion**. **La FORMA de una
correccion declarada dentro de este archivo no esta escrita en ninguna
doctrina.** Se registro lo mejor sostenido (anexar a la `razon` sin borrar nada,
con marca literal y vuelta) y **queda marcado PENDIENTE DE DOCTRINA dentro de la
propia razon**, para que el fundador decida la sede definitiva. **No se para**,
porque la regla 5 dice expresamente que no se para.

**5. EL MARCADOR, RECOMPUTADO DEL ARCHIVO CON SU COMANDO Y NO AJUSTADO A MANO**
(`python scripts/loop/vuelta187_tarea2_cola_post_fusion.py`, bloques F y H):

| | al abrir | al cerrar |
|---|---:|---:|
| filas | **3388** | **3388** |
| puestos unicos | **3388** | **3388** |
| min / max | **1 / 3388** | **1 / 3388** |
| huecos | **0** | **0** |
| duplicados | **0** | **0** |
| `A` | **551** | **551** |
| `B` | **72** | **72** |
| `C` | **5** | **5** |
| `D` | **2760** | **2760** |

**EL MARCADOR NO SE MOVIO, Y ES LO QUE TIENE QUE PASAR:** la relectura sostiene
la clase, asi que lo que cambia es la **evidencia** de la razon y no el reparto
por clase. **El `sha256` SI cambio**, y por eso hay que decir las dos cosas
juntas.

**6. EL TRAMO SE CIERRA EN SU PROPIA SEDE, Y SUS CIFRAS TAMPOCO SE TECLEAN.**
`scripts/loop/vuelta187_tarea2b_cerrar_tramo1_en_el_plan.py` anexa el registro
`#### REGISTRO: EL TRAMO 1 SE RELEYO Y SE CIERRA` **por adicion y dentro de la
seccion de la cola**, leyendo cada cifra del archivo de veredictos y de la salida
de la TAREA 2. `docs/plan/08_VERIFICACION.md` mide hoy **69068 bytes en disco y 69068 bytes normalizados a LF**,
y lo que crecio lo dice su propio instrumento, citado y no tecleado:

```
   la sede pasa de 67121 a 69068 bytes
```

El
registro se releyo del disco byte a byte; la seccion **sigue siendo una** y ahora
va de la **485 a la 879**; el disparador, la declaracion del tramo y la marca del
registro **siguen los tres dentro**; **0 guiones largos o medios en la sede
entera**.

**LA COMPROBACION QUE LA PROPIA SECCION EXIGE, CORRIDA:** *"al cerrar, ningun par
de la lista sigue con su clase vieja apuntando a un nodo que ya no existe"*.
Medido sobre `dataset/metadata/master_graph.json` (**3853 nodos**): **`nodo_a`
vivo SI, `nodo_b` vivo SI**. **Pasa.**

**7. LO QUE ESTA TAREA NO ABRIO, Y EL ENCARGO SE LO PROHIBE CON ESAS PALABRAS:**
la mesa del `PMF` (puestos **338** y **297**), la del **603** y la de figuras del
**226**. Las tres estan anotadas en el acta 187, seccion `6.2`, con sede en
`docs/PENDIENTES.md`.
